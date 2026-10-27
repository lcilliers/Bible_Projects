# Session log 2026-10-27: clear-out of old items for the three steps, and the config alignment table

Session id: `6dfd4a14-17d3-4cdc-936a-98f890167798` (Developer Mode, started 2026-10-27T05:15Z).

## 1. Scope

Developer Mode session. Declaration and compliance file, then the clear-out of open items that belong to the old way of doing 0.C, 0.GAP pre and 0.3 observe (#2314), the approval and follow-up of the #2312 build, and the config alignment for steps 1 to 3 (#2315), which the researcher parked pending the claims phase. No code or config was changed.

## 2. Escalations

- #2260, #2261, #2263 to #2267: closed as completed on the researcher's instruction (capture of observations from the files essentially done). #2260 and #2261 were also corrected (Correction) because the first resolution text said something not checked.
- #2262: closed in error, corrected back to in-progress (v4, v5), then put on hold (v6, v7) for the claims read process.
- #2314: raised, table written, approved by the researcher, completed (v4).
- #2275, #2277, #2279, #2281 to #2285: closed as superseded under #2314 (carried by #2315).
- #2276, #2278, #2280: put on hold for the claims read process.
- #2315: raised, then table v1 and v2 written, handed over (v2, v3), parked on-hold (v4, v5).
- #2316: raised: test steps 1 to 3 on new and existing subgroups, in standard mode.
- #2317: raised: the command check returned no verdict 12 times (environment fault, on hold with the Researcher).
- #2161, #2259, #2308: follow-up comment recorded (v10, v7, v5).
- Held items acknowledged and untouched: #2171, #2172, #2235, #2268, #2296, #2301, #2303, #2305.

## 3. Files

- `outputs/escalation/2314-0c-gap-pre-observe-clearout-table-20261027.md`
- `outputs/escalation/2314-three-steps-design-and-build-status-20261027.md`
- `outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md` (v1 and the inventory file archived)
- `outputs/escalation/2261-escalation-history-v1-20261027.md`, `outputs/escalation/2262-escalation-history-v1-20261027.md`, the escalation list exports
- `Logs/compliance/COMPLIANCE-20261027-6dfd4a14.md`, this log, `iba/app/reports/session-close-v213-20261027.md`
- `scripts/SQLite/IBA_DB/explore.observations-1.sqlite3-query`: the researcher's own scratch query, changed outside this session's work, committed as found
- Database (`iba/app/db/iba.db`, not in git): escalation rows only

## 4. Decisions

- Researcher: #2260 and #2261 completed; #2262 to #2267 completed (all about capturing observations from the files). Recorded in #2260 v7, #2261 v4, #2263 v3, #2264 v3, #2265 v3, #2266 v4, #2267 v3.
- Researcher: #2262 is approved for follow-up; the verse-level read in context and its observations belong in the claims read process. Recorded in #2262 v7, #2276 v3, #2278 v3, #2280 v3 and `outputs/escalation/2314-three-steps-design-and-build-status-20261027.md`.
- Researcher: close the design half of #2275 and move the retire half with #2277, #2279, #2281 to #2285 into one stale-configs item. Recorded in #2314 v3 and #2315 v2.
- Researcher: #2312, #2310, #2308, #2304, #2270, #2161, #2259 approved; #2305 not ready for approval; the older tests are experimental and not to be systemised; nodes without an occurrence id are completed as verses are read, others never reached. Recorded in #2315 v5 and `outputs/escalation/2314-three-steps-design-and-build-status-20261027.md`.
- Researcher: park the config work until the claims phase is defined; test steps 1 to 3 first, in standard mode. Recorded in #2315 v4 and #2316 v1.
- Claude, taken for the researcher to confirm: retire the Stage 1 route and the passage method (unit 10) only after the claims phase is defined. Recorded in `outputs/escalation/2315-config-alignment-steps-1-3-table-v2-20261027.md`.

## 5. Open items

- #2316: test steps 1 to 3 in standard mode (with the Researcher).
- #2315: config alignment for steps 1 to 3, parked until the claims phase is defined; eleven units listed in its table.
- #2305: not ready for approval; what it lacks is not established.
- #2301: the researcher's confirmation that the snapshot deletion was run.
- #2268, #2296, #2235, #2303, #2171, #2172: held as before.

## 6. Git

Branch: `main`. Session commit: `4aad25d73f49b7137738238f40f89319733a8394` ("session 20261027: #2260-#2267 closed ...").

Push output: `0c5e0f48..4aad25d7  main -> main` to `https://github.com/lcilliers/Bible_Projects.git`.
