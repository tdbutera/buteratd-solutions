# HANDOFF — Session Continuity

> Per master-prompt context discipline. The one file a future session reads first. Repo is the state; each doc's `SESSION-END STATE:` has the details.

## Operator (confirmed this session)
Navy E-8 High-3, retire **29 Feb 2028**, spouse + 6 homeschooled kids, civilian floor $137K / target $150–180K cleared cyber (TS/SCI). **VA rating: modeling 70% vs 100% P&T as a live fork** (user-confirmed). Verified military floor: **$5,223/mo @70%, $7,632/mo @100%** (CRDP confirmed; matches user's calculator + VA.gov).

## Workspace
- Branch **`retirement-planning`** (clean, local-only; KCM website preserved on `main`). PR **#1** (draft).
- **Markdown docs + one local interactive HTML dashboard** (`retirement-dashboard.html`). Nothing deploys.
- Dashboard verified by a Node DOM-shim harness (`/tmp/verify_dash.js`, `/tmp/check_compare.js`) — re-run after JS edits.

## Built so far
- **Docs:** 00_INDEX · 01_Timeline · 02_Scenario_70_vs_100 · 06_Relocation · 06b_National_Top5 · 06c_Seasons_and_TakeHome · 08_Education_GIBill · 11_Risk_Register · 12_Action_Tracker · 99_VERIFIED_DATA_LOCKED (§A–L).
- **Dashboard tabs:** Overview (home hub) · Finances · 70/100 fork · Relocation (12-state weighted matrix + sensitivity + four-season weight) · Compare 12 (category leaders + sortable table + pros/cons) · Take-home/yr (per-state budget + salary-band legend) · Education · PPM · Timeline · Data. VA-rating toggle + salary slider drive everything.

## Key findings
- **Relocation (national, default weights):** TX 8.31 > AL 7.52 > VA 7.39 > UT 7.26 > FL 7.20 (TN 6th).
- **4-seasons required:** VA > UT > MD > TN > OH > CO > NC.
- **Annual take-home (family of 8, flat $150K):** TN > OH > TX > AL … MD; ~$26K/yr spread (cheap housing+insurance beats no-income-tax headline).
- **Biggest decision lever:** is civilian income **portable**? Collapses job-market weight → cheap/safe/no-tax states rise.

## Open / not yet built
- **Core docs remaining:** 03 VA strategy · 04 Finance & tax · 05 Career · 07 Real estate/homestead · 09 Insurance & risk · 10 ButeraNet · 13 Document inventory · 14 Decision log.
- **Verifications:** TN cap $175K vs $250K (HB1009 enacted?); BLS metro salary percentiles (env-blocked); county property-tax once metro chosen.
- **User has NOT decided:** final state/metro; income portability; whether 100% P&T is genuinely expected.

## Next best action
Resolve the **100% P&T expectation** (drives everything — `11` risk #1) and the **income-portability** question; then narrow to a metro/county. Pending user steer: head-to-head finalist deep-dive was explicitly deferred.

**SESSION-END STATE:** Handoff current. 10 docs + full dashboard built and pushed (PR #1). Plan's load-bearing assumption (100% P&T) is unconfirmed — flagged in `11`. Awaiting user decisions on state, portability, and rating expectation.