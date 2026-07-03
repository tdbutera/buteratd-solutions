#!/usr/bin/env python3
"""
KCO-GW-01 (UniFi Dream Machine Pro) end-to-end provisioning script.

Run this from a machine ON the 192.168.2.0/24 network (it talks to the
UDM Pro's private address directly). Python 3.8+, standard library only.

    python3 provision_kco_gw01.py [--host https://192.168.2.1] [--dry-run]

What it builds (see udm-pro/README.md for the full runbook):
  * VLANs 20 (KCO-IoT), 30 (KCO-Kids), 40 (KCO-Guest, guest portal/isolation),
    99 (KCO-Mgmt) -- DHCP enabled on each; default LAN 192.168.2.0/24 kept.
  * One WPA2/WPA3 SSID per segment (names/PSKs prompted at runtime).
  * LAN_IN firewall rules: IoT/Kids blocked from Default+Mgmt, Guest
    internet-only (RFC1918 blocked), Mgmt reachable only from Default,
    established/related always allowed.
  * WireGuard remote-access VPN server + one client peer; the client
    .conf is written next to this script.

Execution rules honored:
  * Before every write it prints the endpoint, the exact JSON payload,
    and the equivalent UI tab, so you have a paper trail.
  * Least-disruptive changes first; firewall rules and any default-LAN
    verification happen LAST (those can drop the API session).
  * After every write it GETs the resource back and confirms it took.
  * On HTTP 401 (session dropped) it re-authenticates and retries once.
  * At the end it writes kco-gw01-config-report.md (PSKs redacted).

Credentials, SSIDs and PSKs are prompted interactively -- never
hardcoded, never written to the report.
"""

import argparse
import base64
import getpass
import http.cookiejar
import json
import os
import secrets
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

# --------------------------------------------------------------------------
# Pure-python X25519 (RFC 7748) so WireGuard keys work without `wg` installed
# --------------------------------------------------------------------------

P = 2 ** 255 - 19
A24 = 121665


def _x25519_scalarmult(k_bytes: bytes, u_bytes: bytes) -> bytes:
    k = int.from_bytes(k_bytes, "little")
    k &= ~(1 << 255)
    k &= ~7
    k |= 1 << 254
    u = int.from_bytes(u_bytes, "little") & ((1 << 255) - 1)
    x1, x2, z2, x3, z3, swap = u, 1, 0, u, 1, 0
    for t in range(254, -1, -1):
        k_t = (k >> t) & 1
        swap ^= k_t
        if swap:
            x2, x3 = x3, x2
            z2, z3 = z3, z2
        swap = k_t
        a = (x2 + z2) % P
        aa = (a * a) % P
        b = (x2 - z2) % P
        bb = (b * b) % P
        e = (aa - bb) % P
        c = (x3 + z3) % P
        d = (x3 - z3) % P
        da = (d * a) % P
        cb = (c * b) % P
        x3 = pow(da + cb, 2, P)
        z3 = (x1 * pow(da - cb, 2, P)) % P
        x2 = (aa * bb) % P
        z2 = (e * (aa + A24 * e)) % P
    if swap:
        x2, x3 = x3, x2
        z2, z3 = z3, z2
    return ((x2 * pow(z2, P - 2, P)) % P).to_bytes(32, "little")


def wg_keypair():
    """Return (private_key_b64, public_key_b64) for WireGuard."""
    priv = bytearray(secrets.token_bytes(32))
    priv[0] &= 248
    priv[31] &= 127
    priv[31] |= 64
    priv = bytes(priv)
    pub = _x25519_scalarmult(priv, (9).to_bytes(32, "little"))
    return base64.b64encode(priv).decode(), base64.b64encode(pub).decode()


# --------------------------------------------------------------------------
# UniFi OS API client
# --------------------------------------------------------------------------

class UniFiClient:
    def __init__(self, host: str, username: str, password: str, dry_run: bool = False):
        self.host = host.rstrip("/")
        self.username = username
        self.password = password
        self.dry_run = dry_run
        self.csrf = None
        self.log_lines = []
        ctx = ssl.create_default_context()
        ctx.check_hostname = False              # self-signed cert on the UDM
        ctx.verify_mode = ssl.CERT_NONE
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPSHandler(context=ctx),
            urllib.request.HTTPCookieProcessor(self.jar),
        )

    # -- logging ------------------------------------------------------------
    def log(self, msg: str):
        print(msg)
        self.log_lines.append(msg)

    # -- raw request --------------------------------------------------------
    def _request(self, method: str, path: str, payload=None):
        url = self.host + path
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Accept", "application/json")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        if self.csrf:
            req.add_header("X-CSRF-Token", self.csrf)
        resp = self.opener.open(req, timeout=30)
        new_csrf = resp.headers.get("X-CSRF-Token") or resp.headers.get("x-csrf-token")
        if new_csrf:
            self.csrf = new_csrf
        body = resp.read().decode() or "{}"
        return json.loads(body)

    # -- auth ---------------------------------------------------------------
    def login(self):
        self.log(f"[auth] POST {self.host}/api/auth/login (capturing TOKEN cookie + X-CSRF-Token)")
        self._request("POST", "/api/auth/login",
                      {"username": self.username, "password": self.password,
                       "rememberMe": False})
        if not self.csrf:
            # Some firmware only exposes the CSRF token inside the TOKEN JWT
            for c in self.jar:
                if c.name == "TOKEN":
                    try:
                        pl = c.value.split(".")[1]
                        pl += "=" * (-len(pl) % 4)
                        self.csrf = json.loads(base64.urlsafe_b64decode(pl)).get("csrfToken")
                    except Exception:
                        pass
        self.log(f"[auth] OK  csrf={'yes' if self.csrf else 'MISSING'}")

    def call(self, method: str, path: str, payload=None, ui: str = "", retry: bool = True):
        """Print endpoint/payload/UI equivalent, execute, re-auth on 401."""
        if payload is not None:
            self.log(f"\n--- {method} {path}")
            if ui:
                self.log(f"    UI equivalent: {ui}")
            shown = {k: ("<redacted>" if k.startswith("x_") else v)
                     for k, v in payload.items()}   # never log PSKs/private keys
            self.log("    payload: " + json.dumps(shown, indent=2).replace("\n", "\n    "))
            if self.dry_run:
                self.log("    [dry-run] not sent")
                return {"meta": {"rc": "dry-run"}, "data": [payload]}
        try:
            return self._request(method, path, payload)
        except urllib.error.HTTPError as e:
            if e.code == 401 and retry:
                self.log("[auth] session dropped (401) -- re-authenticating and retrying")
                self.login()
                return self.call(method, path, payload, ui, retry=False)
            body = e.read().decode(errors="replace")
            raise RuntimeError(f"{method} {path} -> HTTP {e.code}: {body}") from e

    # -- network-app convenience ---------------------------------------------
    def net(self, method, sub, payload=None, ui=""):
        return self.call(method, f"/proxy/network/api/s/default{sub}", payload, ui)

    def verify(self, sub: str, match: dict, label: str):
        """GET the collection back and confirm an item matching `match` exists."""
        if self.dry_run:
            self.log(f"    [verify:{label}] skipped (dry-run)")
            return match
        items = self.net("GET", sub).get("data", [])
        for it in items:
            if all(it.get(k) == v for k, v in match.items()):
                self.log(f"    [verify:{label}] confirmed present (_id={it.get('_id')})")
                return it
        raise RuntimeError(f"[verify:{label}] NOT FOUND after write -- match={match}")


# --------------------------------------------------------------------------
# Configuration data
# --------------------------------------------------------------------------

VLANS = [
    dict(name="KCO-IoT",   vlan=20, subnet="192.168.20", guest=False),
    dict(name="KCO-Kids",  vlan=30, subnet="192.168.30", guest=False),
    dict(name="KCO-Guest", vlan=40, subnet="192.168.40", guest=True),
    dict(name="KCO-Mgmt",  vlan=99, subnet="192.168.99", guest=False),
]

WG_SUBNET = "192.168.50"   # WireGuard tunnel network
WG_PORT = 51820


def network_payload(v):
    return {
        "name": v["name"],
        "purpose": "guest" if v["guest"] else "corporate",
        "networkgroup": "LAN",
        "enabled": True,
        "vlan_enabled": True,
        "vlan": v["vlan"],
        "ip_subnet": f"{v['subnet']}.1/24",
        "dhcpd_enabled": True,
        "dhcpd_start": f"{v['subnet']}.100",
        "dhcpd_stop": f"{v['subnet']}.254",
        "dhcpd_leasetime": 86400,
        "is_nat": True,
        "setting_preference": "manual",
    }


def wlan_payload(ssid, psk, networkconf_id, usergroup_id, wlangroup_id, ap_group_ids):
    p = {
        "name": ssid,
        "x_passphrase": psk,
        "enabled": True,
        "security": "wpapsk",
        "wpa_mode": "wpa2",
        "wpa3_support": True,          # WPA2/WPA3 transition mode
        "wpa3_transition": True,
        "pmf_mode": "optional",
        "networkconf_id": networkconf_id,
        "usergroup_id": usergroup_id,
        "wlangroup_id": wlangroup_id,
        "ap_group_mode": "all",
    }
    if ap_group_ids:
        p["ap_group_ids"] = ap_group_ids
    return p


# --------------------------------------------------------------------------
# Main flow
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Provision KCO-GW-01 (UDM Pro)")
    ap.add_argument("--host", default="https://192.168.2.1")
    ap.add_argument("--dry-run", action="store_true",
                    help="print every request without sending writes")
    args = ap.parse_args()

    print("== KCO-GW-01 provisioning ==")
    username = input("UniFi admin username: ").strip()
    password = getpass.getpass("UniFi admin password: ")

    c = UniFiClient(args.host, username, password, dry_run=args.dry_run)
    c.login()

    # ---- Step 0: inventory existing config --------------------------------
    c.log("\n== Step 0: existing configuration (GET /rest/networkconf) ==")
    existing = c.net("GET", "/rest/networkconf").get("data", [])
    for n in existing:
        c.log(f"  - {n.get('name')}  purpose={n.get('purpose')} "
              f"vlan={n.get('vlan', '-')} subnet={n.get('ip_subnet', '-')} _id={n.get('_id')}")
    default_lan = next((n for n in existing
                        if n.get("purpose") == "corporate"
                        and str(n.get("ip_subnet", "")).startswith("192.168.2.")), None)
    if default_lan:
        c.log(f"  Default LAN found: {default_lan['name']} {default_lan['ip_subnet']} (left untouched)")
    else:
        c.log("  WARNING: no 192.168.2.x corporate network found -- default LAN check at the end.")

    # ---- Step 1: VLANs -----------------------------------------------------
    c.log("\n== Step 1: create VLANs (Settings > Networks > New Virtual Network) ==")
    net_ids = {}
    if default_lan:
        net_ids["Default"] = default_lan["_id"]
    for v in VLANS:
        already = next((n for n in existing if n.get("vlan") == v["vlan"]), None)
        if already:
            c.log(f"  VLAN {v['vlan']} already exists as '{already['name']}' -- skipping create")
            net_ids[v["name"]] = already["_id"]
            continue
        c.net("POST", "/rest/networkconf", network_payload(v),
              ui=f"Settings > Networks > New Virtual Network ({v['name']}, VLAN {v['vlan']})")
        item = c.verify("/rest/networkconf", {"name": v["name"], "vlan": v["vlan"]}, v["name"])
        net_ids[v["name"]] = item.get("_id", f"dry-run-{v['name']}")

    # ---- Step 2: WLANs -----------------------------------------------------
    c.log("\n== Step 2: WLANs (Settings > WiFi > Create New) ==")
    c.log("Enter SSID + passphrase per segment. Leave SSID blank to skip that segment.")
    groups = {}
    if not c.dry_run:
        ug = c.net("GET", "/rest/usergroup").get("data", [])
        wg_ = c.net("GET", "/rest/wlangroup").get("data", [])
        groups["usergroup"] = next((g["_id"] for g in ug if g.get("attr_no_delete")), ug[0]["_id"] if ug else None)
        groups["wlangroup"] = next((g["_id"] for g in wg_ if g.get("attr_no_delete")), wg_[0]["_id"] if wg_ else None)
        try:
            apg = c.call("GET", "/proxy/network/v2/api/site/default/apgroups")
            groups["apgroups"] = [g["_id"] for g in apg if g.get("attr_no_delete")] or \
                                 [g["_id"] for g in apg]
        except Exception:
            groups["apgroups"] = []   # older firmware: wlangroup is enough
    wifi_segments = [("Default", "Staff / management (untagged LAN)")] + \
                    [(v["name"], f"VLAN {v['vlan']}") for v in VLANS]
    wlans_created = []
    for seg, desc in wifi_segments:
        if seg not in net_ids:
            continue
        ssid = input(f"  SSID for {seg} ({desc}) [blank=skip]: ").strip()
        if not ssid:
            c.log(f"  {seg}: skipped (no SSID given)")
            continue
        psk = getpass.getpass(f"  WPA passphrase for '{ssid}' (8-63 chars): ")
        c.net("POST", "/rest/wlanconf",
              wlan_payload(ssid, psk, net_ids[seg],
                           groups.get("usergroup"), groups.get("wlangroup"),
                           groups.get("apgroups")),
              ui=f"Settings > WiFi > Create New ({ssid} -> network {seg}, WPA2/WPA3)")
        c.verify("/rest/wlanconf", {"name": ssid}, f"wlan:{ssid}")
        wlans_created.append((ssid, seg))

    # ---- Step 3: WireGuard VPN server + client ------------------------------
    c.log("\n== Step 3: WireGuard remote access (Settings > VPN > VPN Server > WireGuard) ==")
    server_priv, server_pub = wg_keypair()
    client_priv, client_pub = wg_keypair()
    wg_payload = {
        "name": "KCO-WireGuard",
        "purpose": "remote-user-vpn",
        "vpn_type": "wireguard-server",
        "enabled": True,
        "ip_subnet": f"{WG_SUBNET}.1/24",
        "local_port": WG_PORT,
        "x_wireguard_private_key": server_priv,
        "wireguard_public_key": server_pub,
        "wireguard_clients": [{
            "name": "tdbutera-client-1",
            "wireguard_public_key": client_pub,
            "tunnel_ip": f"{WG_SUBNET}.2",
        }],
        "setting_preference": "manual",
    }
    c.net("POST", "/rest/networkconf", wg_payload,
          ui="Settings > VPN > VPN Server > Create (WireGuard, port 51820) + Add Client")
    c.verify("/rest/networkconf", {"name": "KCO-WireGuard"}, "wireguard-server")

    wan_ip = ""
    if not c.dry_run:
        try:
            health = c.net("GET", "/stat/health").get("data", [])
            wan = next((h for h in health if h.get("subsystem") == "wan"), {})
            wan_ip = wan.get("wan_ip", "")
        except Exception:
            pass
    if not wan_ip:
        wan_ip = input("  WAN IP/hostname for the WireGuard endpoint: ").strip() or "<WAN-IP>"

    client_conf = f"""[Interface]
# KCO-GW-01 WireGuard client: tdbutera-client-1
PrivateKey = {client_priv}
Address = {WG_SUBNET}.2/32
DNS = 192.168.2.1

[Peer]
PublicKey = {server_pub}
AllowedIPs = 192.168.0.0/16
Endpoint = {wan_ip}:{WG_PORT}
PersistentKeepalive = 25
"""
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "kco-wg-client-tdbutera.conf")
    with open(conf_path, "w") as f:
        f.write(client_conf)
    os.chmod(conf_path, 0o600)
    c.log(f"  WireGuard client config written to {conf_path} (import into the WireGuard app)")
    c.log("  NOTE: if firmware rejects inline wireguard_clients, add the client in "
          "Settings > VPN > VPN Server > Clients using public key "
          f"{client_pub} and tunnel IP {WG_SUBNET}.2 -- the .conf stays valid.")

    # ---- Step 4 (LAST): firewall rules --------------------------------------
    c.log("\n== Step 4 (saved last -- can interrupt the session): LAN_IN firewall rules ==")
    c.log("   (Settings > Security > Traffic & Firewall Rules > LAN)")

    # RFC1918 address group for the guest internet-only rule
    fwg = c.net("POST", "/rest/firewallgroup",
                {"name": "KCO-RFC1918", "group_type": "address-group",
                 "group_members": ["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"]},
                ui="Settings > Profiles > IP Groups > Create (KCO-RFC1918)")
    rfc1918 = c.verify("/rest/firewallgroup", {"name": "KCO-RFC1918"}, "fwgroup")
    rfc1918_id = rfc1918.get("_id", "dry-run")

    def fw_rule(index, name, action, src_net=None, dst_net=None,
                dst_group=None, established=False):
        p = {
            "ruleset": "LAN_IN", "rule_index": index, "name": name,
            "action": action, "enabled": True, "protocol": "all",
            "protocol_match_excepted": False, "logging": False,
            "state_established": established, "state_related": established,
            "state_invalid": False, "state_new": False,
            "src_firewallgroup_ids": [], "dst_firewallgroup_ids": dst_group or [],
            "src_mac_address": "", "ipsec": "",
        }
        if src_net:
            p["src_networkconf_type"] = "NETv4"
            p["src_networkconf_id"] = src_net
        if dst_net:
            p["dst_networkconf_type"] = "NETv4"
            p["dst_networkconf_id"] = dst_net
        c.net("POST", "/rest/firewallrule", p,
              ui=f"Settings > Security > Firewall Rules > LAN > Create ({name})")
        c.verify("/rest/firewallrule", {"name": name}, f"fw:{name}")

    ids = net_ids  # shorthand
    have = lambda *ks: all(k in ids for k in ks)

    # 1) return traffic always allowed
    fw_rule(2000, "KCO allow established/related", "accept", established=True)
    # 2) Mgmt reachable ONLY from Default: explicit allow, then drop-all-to-Mgmt
    if have("Default", "KCO-Mgmt"):
        fw_rule(2005, "KCO allow Default to Mgmt", "accept",
                src_net=ids["Default"], dst_net=ids["KCO-Mgmt"])
    # 3) IoT + Kids: no path to Default or Mgmt (internet stays open --
    #    LAN_IN drops below only match internal destinations)
    for seg in ("KCO-IoT", "KCO-Kids"):
        base = 2010 if seg == "KCO-IoT" else 2012
        if have(seg, "Default"):
            fw_rule(base, f"KCO drop {seg} to Default", "drop",
                    src_net=ids[seg], dst_net=ids["Default"])
        if have(seg, "KCO-Mgmt"):
            fw_rule(base + 1, f"KCO drop {seg} to Mgmt", "drop",
                    src_net=ids[seg], dst_net=ids["KCO-Mgmt"])
    # 4) Guest: internet only (drop every RFC1918 destination)
    if have("KCO-Guest"):
        fw_rule(2014, "KCO drop Guest to all RFC1918", "drop",
                src_net=ids["KCO-Guest"], dst_group=[rfc1918_id])
    # 5) catch-all: nothing else may reach Mgmt
    if have("KCO-Mgmt"):
        fw_rule(2020, "KCO drop any to Mgmt", "drop", dst_net=ids["KCO-Mgmt"])

    # ---- Step 5: final default-LAN verification -----------------------------
    c.log("\n== Step 5: default LAN verification (no changes made) ==")
    nets = existing if c.dry_run else c.net("GET", "/rest/networkconf").get("data", [])
    dl = next((n for n in nets if str(n.get("ip_subnet", "")).startswith("192.168.2.")), None)
    if dl:
        c.log(f"  Default LAN intact: {dl.get('name')} {dl.get('ip_subnet')} (gateway 192.168.2.1)")
    else:
        c.log("  WARNING: could not confirm default LAN -- check Settings > Networks.")

    # ---- Report --------------------------------------------------------------
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "kco-gw01-config-report.md")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(report_path, "w") as f:
        f.write(f"# KCO-GW-01 Configuration Report\n\nGenerated: {now}\n"
                f"Controller: {args.host} (UniFi OS integrated API)\n\n")
        f.write("## Networks\n\n| Network | VLAN | Subnet | DHCP | Purpose |\n"
                "|---|---|---|---|---|\n"
                "| Default | - | 192.168.2.0/24 | existing | Staff/management |\n")
        for v in VLANS:
            f.write(f"| {v['name']} | {v['vlan']} | {v['subnet']}.0/24 | "
                    f"{v['subnet']}.100-254 | {'Guest (isolated)' if v['guest'] else 'Corporate'} |\n")
        f.write("\n## WLANs (WPA2/WPA3 transition, PSKs redacted)\n\n")
        for ssid, seg in wlans_created or [("(none created)", "-")]:
            f.write(f"- **{ssid}** -> {seg}\n")
        f.write(f"\n## WireGuard\n\n- Server: {WG_SUBNET}.1/24, UDP {WG_PORT}, "
                f"endpoint {wan_ip}\n- Server public key: `{server_pub}`\n"
                f"- Client `tdbutera-client-1`: {WG_SUBNET}.2, public key `{client_pub}`\n"
                f"- Client config: `kco-wg-client-tdbutera.conf` (contains the private key -- keep off git)\n")
        f.write("\n## Firewall (LAN_IN)\n\n"
                "| Index | Rule | Action |\n|---|---|---|\n"
                "| 2000 | established/related | accept |\n"
                "| 2005 | Default -> Mgmt | accept |\n"
                "| 2010/2011 | IoT -> Default / Mgmt | drop |\n"
                "| 2012/2013 | Kids -> Default / Mgmt | drop |\n"
                "| 2014 | Guest -> RFC1918 (group KCO-RFC1918) | drop |\n"
                "| 2020 | any -> Mgmt (catch-all) | drop |\n")
        f.write("\n## Session log\n\n```\n" + "\n".join(c.log_lines) + "\n```\n")
    c.log(f"\n== Done. Report written to {report_path} ==")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(1)
