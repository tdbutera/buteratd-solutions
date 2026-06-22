# 00 · INDEX — Military Retirement Planning System

> **The repo is the state.** This is the single entry point. Core docs are built **on demand** (`BUILD <doc>`) — only `00_INDEX` and the LOCKED data block exist until you ask for more.
> System spec: `retirement_master_prompt_v3.md` (operator's master prompt). Locked verified data: `99_VERIFIED_DATA_LOCKED.md`.

---

## Operator situation (confirmed this session — 2026-06-22)

- **Member:** Navy **E-8, High-3**, 20 yr 5 mo service. **Retire 29 Feb 2028.**
- **Dates:** TAPS **[Jun 2026 — confirm vs new date]** · PRD **[Jan 2027 — confirm]** · terminal leave / SkillBridge **[TBD]**.
- **Family:** spouse + **6 kids** (b. 2014, 2016, 2017, 2020, 2024, 2026), homeschool (**[BJU Press]**). **Model 8 people.**
- **Civilian income:** floor **$137K**, target **$150–180K+**. Never model below the floor without flagging.
- **VA rating:** **MODEL BOTH — live fork.** 70% vs **100% P&T** scored side-by-side as the core scenario (`02`). `[Verified – user confirmed, Jun 2026]`
- **Relocation shortlist:** **Tennessee (front-runner to beat) + Florida + Texas + Virginia.** `[Verified – user confirmed, Jun 2026]`
  - ⚠️ 3 challengers vs. prompt's "up to 2" — 4-way matrix dilutes weighting. **Plan: drop the weakest after first scoring pass in `06`.**
- **Other levers:** DITY/PPM (~$40K target), TS/SCI clearance, **[certs — fill]**, ButeraNet MSP/cyber consulting.
- **Constraint:** no CWO / officer-recall pathways unless asked.

---

## 🔢 Verified financial baseline (military floor only — civilian income sits ON TOP)

`[Verified – user retirement-calculator screenshots, Jun 2026; VA figures corroborated vs VA.gov 2026 tables in LOCKED block]`

**Shared both ratings:** Retirement pay **$3,450** (taxable) · Tricare Prime Family **−$64** · SBP/VGLI **−$278** ($1,846 SBP / $500K VGLI) · Fed tax **−$340** (MFJ) · adjustments $0.

| | 70% | 100% P&T | Delta |
|---|---|---|---|
| VA disability (tax-free) | $2,455 | $4,864 | **+$2,409/mo** |
| **Net monthly (pension + VA)** | **$5,223** | **$7,632** | **+$2,409/mo** |
| **Net annual** | **$62,676** | **$91,584** | **+$28,908/yr** |

- **CRDP confirmed:** full retirement + full VA stack with no waiver offset (concurrent receipt; applies at both ratings ≥50%).
- Entire net-monthly delta = the **tax-free VA difference**. The 100%-only levers (Ch.35 ×6, state property-tax relief) are **on top of** this and not in these figures.

---

## Core document registry (build with `BUILD <nn>`)

| # | Doc | Status |
|---|---|---|
| 01 | Timeline | ⬜ not built |
| 02 | Scenario comparison (70% vs 100% fork) | ⬜ not built |
| 03 | VA strategy | ⬜ not built |
| 04 | Finance & tax | ⬜ not built |
| 05 | Career | ⬜ not built |
| 06 | Relocation shortlist (TN vs FL/TX/VA) | ⬜ not built |
| 07 | Real estate / homestead | ⬜ not built |
| 08 | Education & GI Bill (Ch.35 ×6 + Ch.33 TEB) | ⬜ not built |
| 09 | Insurance & risk | ⬜ not built |
| 10 | ButeraNet | ⬜ not built |
| 11 | Risk register | ⬜ not built |
| 12 | Action tracker | ⬜ not built |
| 13 | Document inventory | ⬜ not built |
| 14 | Decision log | ⬜ not built |

---

## First-run pull queue (Tier 1 — pending)

- ⬜ TN disabled-veteran property-tax relief — amount/cap + 100% P&T gate.
- ⬜ TN income tax — confirm Hall-tax repeal still in effect (no wage/investment tax).
- ⬜ FL / TX / VA equivalents — disabled-vet property exemption + income tax (for `06` matrix).
- ⬜ $137K+ cyber/ISSM salary bands in TN (+ challenger) metros.
- ⬜ TN homeschool legal category + co-op density.
- ⬜ 2026 DITY/PPM reimbursement rate.
- ⬜ Ch.33 TEB transfer remaining-obligation rules + deadline before 29 Feb 2028.

---

## How to invoke
`ANALYZE <topic>` · `COMPARE <A> vs <B>` · `RED TEAM <plan>` · `BUILD <doc>` · `QUICK <q>`

---

**SESSION-END STATE:** System bootstrapped on clean `retirement-planning` branch (KCM website preserved on `main`). Confirmed inputs locked: VA = both-ratings fork; shortlist = TN+FL+TX+VA; verified military-floor financials captured ($5,223/mo @70%, $7,632/mo @100%, CRDP confirmed). No core docs built yet — awaiting first `BUILD`/`ANALYZE`. Next best action: `BUILD 02` (scenario fork) or run the Tier-1 pull queue.
