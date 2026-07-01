# 50-STATE DATASET — Dashboard Data Layer

> Powers `retirement-dashboard.html` (Compare 50 + Relocation matrix + Take-home). **Tier-2 overall** — assembled from parallel research agents (taxes, cost-of-living/tuition, insurance/disaster, cyber/climate) plus knowledge for crime/homeschool/tolls. Income-tax, cost-of-living, and property figures are Tier-1/2; insurance, disaster, crime, cyber, seasons are Tier-2/estimated. **Verify any specific cell before relying on it.** Scores in the dashboard are computed by min-max normalization across all 50 states (not hand-set).

## Columns
Inc = top state income-tax % on wages · MilEx = military retirement fully exempt · Prop% = effective property-tax rate · VetProp = disabled-vet homestead @100% P&T · VetTuition = dependent tuition waiver · RPP = cost of living (US=100) · Home = median home $ · Tuition = in-state public $/yr · Ins = avg homeowners premium $/yr · Dis = disaster risk 1-10 · Crime = violent/100k · HS = homeschool reg · Toll = toll burden · Seas = 4-season 1-10 · Cyber = cleared-cyber 1-10

| St | Inc | MilEx | Prop% | VetProp | VetTuit | RPP | Home | Tuition | Ins | Dis | Crime | HS | Toll | Seas | Cyber |
|----|-----|-------|-------|---------|---------|-----|------|---------|-----|-----|-------|----|----|------|-------|
| AL | 5 | Y | 0.4 | Full | Y | 88.6 | 235k | 11.4k | 3.3k | 8 | 450 | Low | None | 5 | 8 |
| AK | 0 | Y | 0.94 | Partial | N | 102.5 | 375k | 8.5k | 1.4k | 3 | 724 | None | None | 7 | 3 |
| AZ | 2.5 | Y | 0.63 | Partial | N | 100.9 | 420k | 12.1k | 1.9k | 5 | 430 | Low | Light | 3 | 5 |
| AR | 3.7 | Y | 0.56 | Full | Y | 86.5 | 210k | 9.7k | 4.1k | 8 | 579 | Mod | None | 6 | 2 |
| CA | 13.3 | N | 0.7 | Partial | Y | 112.6 | 789k | 9.6k | 2.1k | 9 | 430 | Low | Heavy | 4 | 7 |
| CO | 4.25 | N | 0.49 | Partial | N | 103.5 | 538k | 12.0k | 4.3k | 7 | 420 | Mod | Mod | 9 | 8 |
| CT | 6.99 | Y | 1.54 | Full | N | 104.9 | 447k | 15.9k | 1.6k | 4 | 180 | None | Heavy | 8 | 4 |
| DE | 6.6 | N | 0.55 | Partial | N | 99.9 | 385k | 14.7k | 1.4k | 3 | 430 | Low | Heavy | 7 | 3 |
| FL | 0 | Y | 0.74 | Full | Y | 101 | 385k | 6.4k | 6.4k | 10 | 258 | Mod | Heavy | 1 | 6 |
| GA | 5.39 | N | 0.81 | Partial | Y | 93 | 319k | 7.3k | 2.4k | 7 | 390 | Mod | Mod | 5 | 7 |
| HI | 11 | Y | 0.29 | Full | Y | 108.6 | 832k | 12.2k | 0.9k | 6 | 260 | Mod | None | 1 | 5 |
| ID | 5.3 | Y | 0.47 | Partial | Y | 93.4 | 443k | 8.5k | 1.3k | 3 | 240 | Low | None | 8 | 2 |
| IL | 4.95 | Y | 1.95 | Full | Y | 99.6 | 270k | 15.1k | 2.5k | 6 | 440 | None | Heavy | 8 | 3 |
| IN | 3.05 | Y | 0.76 | Full | Y | 91 | 245k | 9.9k | 2.2k | 6 | 300 | None | Mod | 8 | 4 |
| IA | 3.8 | Y | 1.33 | Full | N | 90.6 | 220k | 9.5k | 2.6k | 6 | 290 | None | None | 8 | 2 |
| KS | 5.58 | Y | 1.21 | Full | Y | 90.5 | 235k | 10.2k | 5.5k | 8 | 410 | Low | Mod | 7 | 3 |
| KY | 3.5 | N | 0.74 | Partial | Y | 88.7 | 215k | 11.5k | 3.1k | 7 | 290 | Low | Mod | 7 | 3 |
| LA | 4.25 | Y | 0.55 | Full | Y | 91 | 200k | 11.1k | 6.3k | 9 | 550 | Mod | Mod | 2 | 3 |
| ME | 7.15 | Y | 1.24 | Partial | Y | 99 | 380k | 10.9k | 1.3k | 3 | 100 | Mod | Heavy | 8 | 2 |
| MD | 5.75 | Y | 0.99 | Full | Y | 105.5 | 420k | 10.4k | 1.6k | 4 | 430 | Mod | Heavy | 7 | 10 |
| MA | 9 | Y | 1.14 | Partial | Y | 107.5 | 635k | 14.3k | 1.9k | 4 | 330 | High | Mod | 8 | 5 |
| MI | 4.25 | Y | 1.38 | Full | Y | 93.5 | 245k | 15.3k | 1.7k | 5 | 460 | None | Mod | 9 | 3 |
| MN | 9.85 | N | 1.02 | Partial | Y | 97 | 335k | 14.4k | 2.6k | 6 | 270 | Mod | Light | 9 | 3 |
| MS | 4.7 | Y | 0.75 | Full | Y | 87.3 | 185k | 9.3k | 4.2k | 8 | 280 | Low | None | 3 | 3 |
| MO | 4.7 | Y | 0.91 | None | Y | 90 | 250k | 10.1k | 3.2k | 7 | 490 | None | Light | 7 | 4 |
| MT | 5.9 | N | 0.74 | Partial | N | 95 | 468k | 8.0k | 2.0k | 5 | 470 | Low | None | 8 | 2 |
| NE | 5.2 | Y | 1.44 | Partial | N | 91.5 | 285k | 9.5k | 5.0k | 8 | 330 | Low | None | 8 | 5 |
| NV | 0 | Y | 0.55 | Partial | N | 100.5 | 445k | 8.6k | 1.1k | 4 | 460 | Low | Light | 3 | 3 |
| NH | 0 | Y | 1.61 | Partial | Y | 106 | 480k | 17.4k | 1.0k | 3 | 110 | Mod | Light | 9 | 3 |
| NJ | 10.75 | Y | 2.23 | Full | Y | 108.9 | 569k | 15.6k | 1.4k | 5 | 200 | None | Heavy | 7 | 4 |
| NM | 5.9 | N | 0.67 | Full | Y | 92 | 300k | 8.3k | 1.9k | 5 | 717 | Low | None | 4 | 4 |
| NY | 10.9 | Y | 1.54 | Partial | Y | 106.5 | 508k | 8.6k | 1.6k | 6 | 330 | High | Heavy | 8 | 4 |
| NC | 4.25 | Y | 0.63 | Partial | Y | 93.5 | 330k | 7.4k | 2.4k | 8 | 370 | Mod | Mod | 5 | 4 |
| ND | 2.5 | Y | 0.94 | Partial | Y | 90 | 265k | 9.4k | 2.4k | 5 | 290 | Mod | None | 9 | 3 |
| OH | 3.5 | Y | 1.3 | Partial | Y | 90.5 | 235k | 11.4k | 1.5k | 5 | 290 | Mod | Heavy | 9 | 6 |
| OK | 4.75 | Y | 0.76 | Full | Y | 89.5 | 205k | 9.6k | 5.3k | 9 | 420 | None | Heavy | 6 | 3 |
| OR | 9.9 | N | 0.86 | Partial | N | 103.5 | 495k | 12.1k | 0.9k | 5 | 340 | Mod | None | 6 | 2 |
| PA | 3.07 | Y | 1.36 | Full | N | 98 | 275k | 15.7k | 1.7k | 5 | 310 | High | Heavy | 8 | 4 |
| RI | 5.99 | Y | 1.3 | Partial | N | 103 | 437k | 14.2k | 1.9k | 4 | 230 | High | Heavy | 8 | 3 |
| SC | 6.2 | Y | 0.53 | Full | Y | 94 | 300k | 12.9k | 2.9k | 8 | 437 | Mod | Light | 4 | 5 |
| SD | 0 | Y | 1.08 | Partial | N | 88.1 | 300k | 9.2k | 2.9k | 6 | 480 | Mod | None | 9 | 2 |
| TN | 0 | Y | 0.55 | Partial | N | 91 | 335k | 10.2k | 2.8k | 7 | 592 | Low | None | 6 | 3 |
| TX | 0 | Y | 1.68 | Full | Y | 97 | 307k | 10.9k | 4.9k | 9 | 420 | None | Heavy | 3 | 8 |
| UT | 4.55 | N | 0.55 | Partial | N | 98 | 511k | 7.1k | 0.9k | 3 | 260 | Low | Light | 7 | 5 |
| VT | 8.75 | N | 1.71 | Partial | N | 101.5 | 390k | 17.5k | 0.9k | 2 | 173 | High | None | 10 | 2 |
| VA | 5.75 | Y | 0.8 | Full | Y | 102 | 390k | 14.7k | 2.1k | 6 | 270 | Mod | Heavy | 7 | 10 |
| WA | 0 | Y | 0.87 | Partial | Y | 106.5 | 604k | 12.2k | 1.4k | 5 | 370 | Mod | Light | 6 | 5 |
| WV | 4.82 | Y | 0.55 | Partial | N | 88 | 174k | 9.4k | 1.5k | 4 | 330 | Mod | Mod | 7 | 4 |
| WI | 7.65 | Y | 1.51 | Full | Y | 93 | 310k | 9.5k | 1.5k | 4 | 320 | Low | None | 9 | 3 |
| WY | 0 | Y | 0.55 | Partial | N | 94.5 | 350k | 7.0k | 1.7k | 4 | 203 | Low | None | 8 | 2 |

## Scoring axes (normalized → 1-10, higher=better)
Cyber job market (18) · Low income tax (12) · Vet property tax (10) · Low cost of living (10) · College affordability incl. waivers (8) · Low insurance (8) · Low disaster risk (8) · Safety/crime (8) · Homeschool freedom (8) · Four seasons (6) · Low tolls (4). Weights are the dashboard defaults — adjust live.

## Notable data flags
- **WA** disabled-vet property exemption is income-capped (~$40K) — high earners are disqualified; shown as Partial.
- **CA/DE/CO/UT/OR/MN/MT/NM/VT/MO/GA/KY** do NOT fully exempt military retirement (or only partially) — see MilEx=N.
- **Vet-dependent tuition waivers (VetTuition=Y)** — TX (Hazlewood), FL, AR, IL, IN, KS, MD, VA, and others fully/largely waive public-university tuition for a 100% P&T vet's children. Huge with multiple kids.
- TN property relief is capped; several "Partial" states cap the exemption at a value or dollar amount.

**SESSION-END STATE:** 50-state dataset persisted. Powers the data-driven dashboard (normalized scoring, 11 axes incl. new College/Toll/Disaster). Tier-2 overall; per-cell verification advised. Default matrix winner Alabama; take-home leader West Virginia.
