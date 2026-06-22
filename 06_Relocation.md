# 06 · RELOCATION — Shortlist Verdict

> Built on demand. Sources: `99_VERIFIED_DATA_LOCKED.md` §E–I. Interactive model: `retirement-dashboard.html` (Relocation tab). Re-score by adjusting weights there.

## TL;DR

On a full 7-axis weighted scoring with my default weights, **Texas (San Antonio) wins (8.31)** and the presumed front-runner **Tennessee drops to 3rd (7.31)** — its tax/homeschool strengths are outweighed by a weak cleared-job market, the shortlist's weakest disabled-vet property benefit, and the highest crime of the four. **The result is weight-sensitive** — change what you value and it moves. This doc shows the scoring, the sensitivity, and what would change the call.

| Rank | State (focus metro) | Score | One-line |
|---|---|---|---|
| 🥇 1 | **Texas (San Antonio)** | **8.31** | Best cleared-cyber value + strongest homeschool law + no income tax + full property exemption; watch 1.4% property tax (wiped at 100% P&T) and Gulf insurance. |
| 🥈 2 | Florida (Tampa) | 7.48 | MacDill SOCOM/CENTCOM job market, no income tax, strong family climate — but the hurricane/insurance burden ($6K+/yr) is the biggest financial risk. |
| 🥉 3 | Tennessee (Knoxville) | 7.31 | Lowest cost of living + low homeschool reg + no income tax — but weakest job market (Oak Ridge only), capped property benefit, highest crime. |
| 4 | Virginia (Hampton Roads/NoVA) | 7.26 | Safest + cheapest insurance + densest cleared market — but the only income-taxing state and the priciest (NoVA), with moderate homeschool regulation. |

> ⚠️ This assumes **100% P&T** (full property exemptions live). At 70%, no state grants the full exemption and the property axis compresses — see the dashboard's rating toggle.

---

## Scoring matrix (1–10, higher = better for this family)

| Axis | Wt | TN | FL | TX | VA | Tier |
|---|---|---|---|---|---|---|
| Cleared cyber market | 22 | 5 | 7 | **9** | **10** | T2 |
| Income-tax burden | 15 | **10** | **10** | **10** | 4 | T1 |
| Homeschool & parental rights | 14 | 9 | 9 | **10** | 5 | T1 |
| Cost of living | 13 | **9** | 6 | 7 | 4 | T1 (BEA) |
| Vet property tax (@100% P&T) | 12 | 6 | **10** | **10** | **10** | T1 |
| Disaster / insurance | 12 | **8** | 3 | 5 | **8** | T2 |
| Crime / safety | 12 | 5 | 7 | 6 | **9** | T2 |
| **Weighted score** | | 7.31 | 7.48 | **8.31** | 7.26 | |

**Default-weight rationale:** civilian income is the binding goal, so *cleared job market* (22) is heaviest; *income tax* (15) and *homeschool/parental rights* (14) next, reflecting a high earner with 6 homeschooled kids; *cost of living* (13), *property tax* (12), *insurance* (12), *crime* (12) round it out. **These are starting weights — set your own in the dashboard.**

---

## Sensitivity — what flips the ranking

- **TX's lead is ~0.83 pts over FL** — the most robust top slot, anchored by job market + homeschool + no-tax.
- **TN reaches #1 only if** you heavily overweight *cost of living* and *income tax* together while discounting *job market* and *crime* — i.e., if a remote/established income makes the local cyber market irrelevant. If your civilian job is portable (remote ButeraNet/MSP), re-run with job-market weight near 0 and TN/TX battle for the top.
- **VA climbs** if *crime/safety* and *insurance* dominate your weighting (it leads both) — but its income tax on a $150K+ salary (~$8K+/yr) is a permanent drag the others don't have.
- **FL is the hedge** if family-climate + job market matter more than money — but model the **insurance line item explicitly** ($6K+/yr and volatile) before committing.

---

## The decisive factors, by the numbers

**1. Job market (income engine).** Cleared TS/SCI cyber runs 20–40% above the BLS civilian median ($124,910 / $186,420 p90, May 2024). Density: NoVA (densest, >$180K w/ poly) ≥ San Antonio (16th AF/NSA-TX, best net value) > Tampa (SOCOM) ≫ TN (Oak Ridge/ORNL is its *only* node; Nashville/Memphis/Chattanooga commercial cyber often below the $137K floor). `[T2]`

**2. Income tax.** TN/FL/TX = $0 on wages. VA = 2–5.75%, taxing the civilian salary ~$8K+/yr on $150K. The $40K military-retirement subtraction (TY2026, no age limit) does **not** shelter civilian W-2. `[T1]`

**3. Property tax (100% P&T).** FL/TX/VA = **full homestead exemption** ($0). TN = capped reimbursement on the first **$175K** of market value (operative; a $250K increase, HB1009, is proposed but **not confirmed enacted**) — so on a $450K home TN still owes property tax on ~$275K. `[T1]`

**4. Homeschool & parental rights.** TX strongest (no-notice + 2025 Prop 15 constitutional parental-rights amendment); FL (Parents' Bill of Rights) and TN (low-reg, dense Bible-Belt co-ops) close behind; VA the outlier (moderate regulation: notice + testing/eval; more secular NoVA, though a religious exemption exists). `[T1]`

**5. Cost of living (BEA RPP 2023, US=100).** TN 90.4 (cheapest) < TX 98.4 < VA 101.1 < FL 103.5. Focus-metro median home: San Antonio ~$260K (cheapest) · Knoxville $327K · Nashville/Tampa ~$440K · NoVA $664K. `[T1]`

**6. Disaster / insurance.** Avg homeowners premium: VA ~$2.7K < TN ~$3.0K < TX ~$4.5K < **FL $6K+** (costliest, hurricane exposure; market stabilizing but still the dominant risk). San Antonio (inland) avoids the worst Gulf risk. `[T2]`

**7. Crime.** State violent crime /100K (FBI 2024): VA ~234 (safest) < FL ~258 < TX ~431 < **TN ~592** (4th-highest US). TN's risk concentrates in Memphis and urban Nashville — **Knoxville and suburbs are far safer**, which is why metro choice matters more than the state number. `[T2]`

---

## Recommendation

1. **Default-weight winner: Texas / San Antonio** — it's the only state that's top-tier on the income engine *and* zero income tax *and* full property exemption *and* the strongest homeschool law. Property tax (1.4%) is its one weak spot, and that's wiped at 100% P&T.
2. **If TN stays in contention,** it's on the strength of cost-of-living + a *portable* income. Decide first: **is your civilian income local-market-dependent or remote/portable?** That single question is the biggest swing in the whole matrix — answer it, set the job-market weight accordingly, and re-score.
3. **Drop the weakest challenger after weighting.** Per the original up-to-2-challenger guidance: on these defaults, **Virginia is the natural cut** (income tax + cost with no offsetting category lead), leaving a clean **TX vs FL vs TN** final.

## Open items
- TN $250K property cap — confirm if HB1009/SB0681 is enacted (currently $175K operative).
- Narrow to a **county** before locking property-tax math (rates vary intra-state; effective rates here are statewide averages).
- BLS metro salary percentiles remain environment-blocked — pull from an unblocked network if exact metro bands are needed (cleared premium already dominates the estimate).

---

**SESSION-END STATE:** `06` built — full 7-axis weighted relocation verdict. Default-weight ranking TX > FL > TN > VA; key finding = TN front-runner falls to 3rd under full scoring; decision pivots on whether civilian income is portable. Recommended final cut = drop VA → TX/FL/TN. All axes sourced (§E–I). Dashboard updated to match (7 axes, verified). Next: confirm income portability + target county, or `BUILD 01` timeline.