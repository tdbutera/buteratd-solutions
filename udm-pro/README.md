# KCO-GW-01 — UDM Pro Provisioning Runbook

End-to-end configuration of the UniFi Dream Machine Pro (console
**KCO-GW-01**, `https://192.168.2.1`) via the UniFi OS integrated API
(`/proxy/network/api/s/default/...`).

> **Why a script instead of a live session?** Claude Code cloud sessions run
> in an isolated container whose egress gateway blocks all RFC1918
> destinations, so the UDM's private address is unreachable from the cloud.
> This script performs the identical API sequence from any machine on the
> `192.168.2.0/24` network. (Alternative: run Claude Code locally on a LAN
> machine and paste the original task prompt — it can then drive the device
> interactively.)

## Usage

```bash
# from a machine on 192.168.2.0/24 — Python 3.8+, no pip packages needed
python3 provision_kco_gw01.py                 # live run
python3 provision_kco_gw01.py --dry-run       # print every request, send nothing
python3 provision_kco_gw01.py --host https://192.168.2.1
```

The script prompts for the admin credentials and for each segment's SSID +
passphrase at runtime. Nothing secret is hardcoded or committed.

## What it does, in order

| # | Step | Endpoint | UI equivalent |
|---|------|----------|---------------|
| 0 | Authenticate (TOKEN cookie + `X-CSRF-Token`), list existing networks | `POST /api/auth/login`, `GET .../rest/networkconf` | — |
| 1 | Create VLANs 20/30/40/99 with DHCP | `POST .../rest/networkconf` | Settings › Networks › New Virtual Network |
| 2 | One WPA2/WPA3 SSID per segment, mapped to its VLAN | `POST .../rest/wlanconf` | Settings › WiFi › Create New |
| 3 | WireGuard VPN server (192.168.50.1/24, UDP 51820) + client peer; writes `kco-wg-client-tdbutera.conf` | `POST .../rest/networkconf` (`purpose: remote-user-vpn`) | Settings › VPN › VPN Server |
| 4 | **Last** (can drop the API session): LAN_IN firewall rules + `KCO-RFC1918` IP group | `POST .../rest/firewallrule`, `POST .../rest/firewallgroup` | Settings › Security › Firewall Rules |
| 5 | Verify default LAN untouched (192.168.2.0/24, gw .1); write `kco-gw01-config-report.md` | `GET .../rest/networkconf` | Settings › Networks |

Every write prints the endpoint, exact JSON payload, and UI tab before
sending, then **GETs the resource back to confirm it took**. A `401`
mid-run triggers automatic re-authentication and a retry.

## Target configuration

### Networks

| Network | VLAN | Subnet | DHCP pool | Notes |
|---|---|---|---|---|
| Default | — | 192.168.2.0/24 | existing | Staff/management; **left untouched** |
| KCO-IoT | 20 | 192.168.20.0/24 | .100–.254 | |
| KCO-Kids | 30 | 192.168.30.0/24 | .100–.254 | |
| KCO-Guest | 40 | 192.168.40.0/24 | .100–.254 | `purpose: guest` → UniFi guest isolation |
| KCO-Mgmt | 99 | 192.168.99.0/24 | .100–.254 | |

### Firewall (LAN_IN, evaluated top-down)

| Index | Rule | Action |
|---|---|---|
| 2000 | established/related | accept |
| 2005 | Default → Mgmt | accept |
| 2010–2013 | IoT/Kids → Default, IoT/Kids → Mgmt | drop |
| 2014 | Guest → RFC1918 (`KCO-RFC1918` group: 10/8, 172.16/12, 192.168/16) | drop |
| 2020 | any → Mgmt (catch-all) | drop |

Internet stays open for every segment because the drops only match internal
destinations; Mgmt is reachable exclusively from Default (2005 allow before
the 2020 catch-all, with 2000 handling return traffic).

### WireGuard

- Server `KCO-WireGuard`: tunnel net 192.168.50.1/24, UDP 51820.
- Keys are generated locally by the script (pure-Python X25519 — no `wg`
  binary required).
- Client `tdbutera-client-1` (192.168.50.2) → config written to
  `kco-wg-client-tdbutera.conf`, `AllowedIPs = 192.168.0.0/16`. Import it
  into the WireGuard app. **Firmware note:** if your Network-app version
  rejects the inline `wireguard_clients` field, add the client in
  Settings › VPN › VPN Server › Clients using the public key the script
  prints — the generated `.conf` remains valid as-is.

## Outputs (git-ignored — never commit)

- `kco-wg-client-tdbutera.conf` — WireGuard client config (contains a private key)
- `kco-gw01-config-report.md` — full run report: config tables + complete
  session log (endpoints, payloads, verification results). PSKs are redacted.

## Rollback

Bench device: factory-reset via the UDM's reset pin or UniFi OS
Console Settings › Reset. All changes are additive except the firewall
rules; deleting the `KCO-*` rules, group, networks, and WLANs from the UI
also fully reverts.
