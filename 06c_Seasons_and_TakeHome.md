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

---

**SESSION-END STATE:** `06c` added. Four-season-required top 7 = VA > UT > MD > TN > OH > CO > NC (brings in OH/CO/NC, drops TX/FL/AL). Annual take-home (family of 8) ranks TN > OH > TX > AL > GA … > MD; ~$26K/yr spread; cheap housing+insurance beats no-income-tax headline. Dashboard adds Take-home tab + four-season weight slider; 12 states now in matrix. Verified 9/9 assertions.