# 06c · Four-Season Ranking + Annual Take-Home

> Extends `06b`. Two added lenses: (1) re-rank with a true four-season climate as a requirement; (2) model real annual take-home (income minus taxes + full living costs) for a family of 8. Dashboard: **Take-home / yr** tab + draggable **Four-season climate** weight.

## 1. Current top 7 (unchanged)

**1. Texas · 2. Alabama · 3. Virginia · 4. Utah · 5. Florida · 6. Tennessee · 7. Maryland**

## 2. Top 7 — four-season climate *required*

Genuine four-season climates only (drops FL, TX/San Antonio, AL, GA, SC — hot, mild-winter), re-ranked with climate weighted as a requirement:

| # | State | Score | Anchor | Note |
|---|---|---|---|---|
| 1 | **Virginia** | 7.68 | NoVA / Hampton Roads | #1 cyber market + 4 crisp seasons + safe |
| 2 | **Utah** | 7.53 | Hill AFB / SLC | Real winters, low insurance, free homeschool |
| 3 | **Maryland** | 7.25 | Fort Meade | NSA cyber epicenter + 4 seasons (tax/cost heavy) |
| 4 | **Tennessee** | 6.98 | Knoxville | Mild 4 seasons, no income tax, great fall |
| 5 | **Ohio** | 6.83 | Dayton / Wright-Patterson | True Midwest seasons, very cheap, AFRL/NASIC cyber |
| 6 | **Colorado** | 6.73 | Colorado Springs | The premier 4-season cyber town (Space Force/NORAD) |
| 7 | **North Carolina** | 6.43 | RTP / Fort Liberty | 4 seasons in the piedmont, big homeschool community |

**The seasons requirement swaps out Texas, Florida, Alabama → swaps in Ohio, Colorado, North Carolina.** Caveat: San Antonio specifically lacks 4 seasons, but **North Texas (Dallas–Fort Worth)** is more seasonal and keeps Texas in play if you want both.

## 3. Annual take-home — family of 8

**Model:** total net income (military net @100% P&T $91,584 + $150K civilian less ~$4.2K federal after 6× child tax credit) − state income tax − housing (30-yr P&I @6.9% on 80% of the anchor-metro median home) − property tax (—$0 where the 100% P&T exemption is full) − home insurance − groceries/gas/utilities/healthcare (≈$61K base, scaled by state price level). Holds salary constant across states.

| # | State | State tax | Housing/yr | Living/yr | **Take-home / yr** |
|---|---|---|---|---|---|
| 1 | **Tennessee** | $0 | $20.6K | $55.1K | **$161,700** |
| 2 | **Ohio** | $4.9K | $16.0K | $55.1K | **$161,400** |
| 3 | **Texas** | $0 | $17.7K | $59.4K | **$160,400** |
| 4 | **Alabama** | $6.8K | $19.3K | $53.9K | **$157,500** |
| 5 | Georgia | $8.1K | $15.6K | $56.9K | $156,800 |
| 6 | North Carolina | $6.0K | $21.9K | $57.5K | $151,900 |
| 7 | Virginia | $7.5K | $19.3K | $61.2K | $149,300 |
| 8 | South Carolina | $7.5K | $23.9K | $58.1K | $147,800 |
| 9 | Florida | $0 | $28.8K | $61.2K | $147,400 |
| 10 | Utah | $6.8K | $27.4K | $60.0K | $143,200 |
| 11 | Colorado | $6.6K | $29.8K | $63.6K | $137,300 |
| 12 | Maryland | $11.3K | $24.7K | $66.1K | $135,400 |

**Findings:**
- **~$26K/yr spread** between the best (TN) and worst (MD) state on identical income — that's real, recurring money.
- **Cheap housing + low insurance beat the no-income-tax headline.** Florida is no-income-tax yet finishes 9th: its ~$6.4K insurance + pricier homes erase the tax advantage. Ohio (income-taxed) beats it easily on cheap housing.
- **The "all three" winners** (good take-home + decent everything): **Texas (#3), Alabama (#4), Tennessee (#1).**
- **Caveat:** assumes the same $150K everywhere. NoVA/Maryland typically pay more for cleared cyber, which narrows their gap; cheap metros may cap lower. Adjust the civilian salary in the dashboard to test your real offer.

**Cross-lens read:** Texas wins overall and on cash; Tennessee wins on cash and survives the 4-season cut; **Virginia is the standout if you require 4 seasons** (and its lower take-home flips to competitive once you use a realistic NoVA salary).

## 4. Both ratings — the take-home ranking reshuffles at 70%

The table above assumes **100% P&T** (full property exemption live). At **70%** two things change: VA comp is ~$2,409/mo lower (≈$28.9K/yr less income), **and no state grants the full property exemption — so property tax applies everywhere.** That penalizes high-property-tax states and reshuffles the order. *(The dashboard does this live — slide the rating to 70% and the Take-home table re-sorts.)*

| State | Take-home @100% P&T | Take-home @70% | Rank move | Property tax @70% |
|---|---|---|---|---|
| **Ohio** | $161,374 (#2) | **$131,766 (#1)** | ▲ +1 | $3,220 |
| **Tennessee** | $161,689 (#1) | $131,626 (#2) | ▼ −1 | $2,158 |
| **Georgia** | $157,332 (#5) | $127,434 (#3) | ▲ +2 | $2,160 |
| Alabama | $157,436 (#4) | $127,248 (#4) | same | $1,280 |
| **Texas** | $160,342 (#3) | $127,066 (#5) | ▼ −2 | **$4,368** |
| N. Carolina | $151,894 (#6) | $122,657 (#6) | same | $2,482 |
| Virginia | $149,307 (#7) | $117,398 (#7) | same | $3,002 |
| S. Carolina | $147,804 (#8) | $116,544 (#8) | same | $2,352 |
| Florida | $147,351 (#9) | $114,412 (#9) | same | $4,031 |
| Utah | $143,197 (#10) | $111,558 (#10) | same | $2,964 |
| Colorado | $137,302 (#11) | $107,904 (#11) | same | $2,279 |
| Maryland | $135,351 (#12) | $101,718 (#12) | same | $4,725 |

**What flips and why:**
- **Texas drops #3 → #5.** Its full property exemption was carrying it; at 70% the **1.68% rate on the home (~$4,368/yr) is the worst of the affordable states** and there's nothing to offset it. Texas's tax-and-homeschool case stays strong, but its *cash* edge is a P&T artifact.
- **Ohio and Georgia rise** — cheap homes + moderate rates mean they barely notice losing an exemption they only half-had.
- **Tennessee stays top-2 either way** — capped relief means it loses little at 70%, and no income tax + cheap homes carry it.
- Everyone is **~$30K/yr poorer** at 70% (the tax-free VA delta), but the *relative* order is what should drive the location choice if 100% P&T isn't a lock.

> **Plan rule:** if 100% P&T is **not** highly likely, weight the **property-tax-rate** column more and the **exemption** less — which favors low-rate states (AL, GA, TN, CO) over high-rate Texas. See `11_Risk_Register` (the plan's #1 assumption).

---

**SESSION-END STATE:** `06c` added. Four-season-required top 7 = VA > UT > MD > TN > OH > CO > NC. Annual take-home @100% P&T ranks TN > OH > TX > AL > GA … > MD; **at 70% it reshuffles** (§4): OH→#1, TN→#2, GA→#3, **Texas drops #3→#5** on its 1.68% property tax with no exemption; everyone ~$30K/yr poorer. Plan is now dual-track (docs + live dashboard rating slider). If P&T isn't a lock, favor low property-tax-rate states over Texas.