# Session log 2026-10-25 to 2026-10-26: the surface mapping built and run on all M clusters (#2286 U1 to U4, U8)

**Session:** 3646374f-685b-404e-b3c9-7ec0c57b899f · Developer Mode · compliance file `Logs/compliance/COMPLIANCE-20261025-3646374f.md`

## 1. Scope

2026-10-25 to 2026-10-26, one line: the #2286 prototype design was turned into a build plan (v1 to v4), and units U1 (config), U2 (schema), U3 (the `cluster.surface_map` steps and `Surface-Map.ps1`), U4 (the reading gate) and U8 (the pilot on M18 and M67, then all 80 M clusters live) were built, tested on copies and run. The researcher's answers on the bulk run were recorded, the large-subgroup ruling went into config as RO13, and a kept backup was taken before the held snapshot pruning (#2301).

## 2. Escalations

| Escalation | Outcome this session |
|---|---|
| #2286 | worked v37 to v44: the build plan v1 to v4 and the researcher's rulings B1 to B8 (v38, v40, v41); U8 progress (v43); the close request recorded (v44). Stays in-progress with Claude; next unit U5 |
| #2291 | raised (U1 config), built and tested, approved by the researcher (v3), completed |
| #2292 | raised (U2 schema), built and tested, approved (v4), completed |
| #2293 | raised (U3 steps): design D1 to D4 ruled (v4), built and tested, approved (v6), completed (v7) |
| #2294 | raised (U4 reading gate): G-a ruled (v4), built and tested, approved (v6), completed |
| #2295, #2296, #2297, #2299 | raised as the later units U5, U6, U7, U9; on hold with Claude |
| #2298 | raised (U8): pilot P1 a, P2 a, P3 ruled (v5); bulk run reported; Q1 to Q4 answered (v7); completed (v8) |
| #2300 | raised by `cluster.surface_tail` on M11 (the reply with prose before its JSON); resolved self-correctable (v2, completed) |
| #2301 | raised: named pre-run snapshots pruned by run snapshots; Q4 recorded (v3); backup taken and pruning held to 2026-10-28 or later (v4, on hold with the researcher) |
| #2270 | advisory findings recorded (v5 to v8); with the researcher |
| #2006, #2098, #2109, #2149, #2150, #2218 | thread rows set on-hold by the #2298 thread update; no other change |

## 3. Files

Code and config:
- `iba/app/lib/surfacemap.py` (new), `iba/app/handlers/surfacemap.py` (new), `iba/app/ps/Surface-Map.ps1` (new)
- `iba/app/lib/reading.py`, `iba/app/handlers/cluster.py`
- migrations in `iba/app/migration/archive/`: `surface_subgroup_rules_2291_v1_20261025.py`, `surface_subgroup_schema_2292_v1_20261025.py`, `surface_map_steps_2293_v1_20261025.py`, `reading_gate_2294_v1_20261025.py`, `surface_map_tail_ceiling_2298_v1_20261025.py`, `large_subgroup_segment_2298_v1_20261026.py`
- tests: `iba/app/tools/temp_2293_surface_map_test_run.py`, `iba/app/tools/temp_2294_reading_gate_test_run.py`
- `iba/app/BUILD.md` (entries 409 to 415), `iba/app/USER-GUIDE.md` (sections 7.1, 8.2; the Surface-Map path at line 574), `iba/docs/ps tools worksheet.xlsx`

Reports and data:
- `outputs/escalation/2286-build-plan-v4-20261025.md` (v1 to v3 in `outputs/escalation/archive/`)
- `outputs/escalation/2291-u1-config-test-v1-20261025.md`, `outputs/escalation/2292-u2-schema-test-v1-20261025.md`, `outputs/escalation/2293-surface-map-design-v1-20261025.md`, `outputs/escalation/2293-u3-surface-map-test-v1-20261025.md`, `outputs/escalation/2294-reading-gate-decision-v1-20261025.md`, `outputs/escalation/2294-u4-reading-gate-test-v1-20261025.md`
- `outputs/escalation/2298-pilot-m18-m67-v1-20261025.md` with `outputs/escalation/2298-pilot-files/`; `outputs/escalation/2298-bulk-surface-map-v1-20261026.md` with `outputs/escalation/2298-bulk-files/` (21 specs)
- `outputs/surface-map/` (per-cluster pairs and check reports)
- iba.db: `surface_subgroup` (13,411 pairs), `cluster_subgroup`, cfg rows of the six migrations; kept backup `iba/app/db/iba.db.pre-2301-prune-20261026.bak` (not in git)
- tool reports: `_analytics/Clusters/cluster-assign-v8-20261026.md`, `outputs/configs/CONFIG-REPORT-v655-20261026.md`, `outputs/escalation/escalation-list-v201-20261025.md`, `iba/app/reports/session-close-v194-20261026.md`, `_analytics/lexicon/lexical-extracts/lexical-llm-usage.csv`
- `Logs/compliance/COMPLIANCE-20261025-3646374f.md`

## 4. Decisions

Researcher's decisions:
- The build plan rulings B1 to B8 (B4 to `ib_observation`, B5 existing subgroup data incorporated, B6 the anomaly bucket, B7 pilot on M18 and M67): recorded in #2286 v38, v40, v41.
- U1 approved, B:117 to B:122 as worded: recorded in #2291 v3.
- U2 approved: recorded in #2292 v4.
- D1 30%, D2 one sample verse, D3 reuse `lexical.llm_*`, D4 own script: recorded in #2293 v4; U3 approved in #2293 v6.
- G-a, the reading gate as worded: recorded in #2294 v4; U4 approved in #2294 v6.
- P1 a, P2 a, P3 pilot accepted: recorded in #2298 v5.
- Q1 bulk mapping accepted, Q2 c anomaly pairs left for the reading, Q3 a large subgroups segmented when in focus, Q4 prune after backup with a delay: recorded in #2298 v7 and #2301 v3; Q3 in `cfg_method_rule` (RO13 segment-large-subgroup).

Claude's self-correctable fixes (closed):
- The curly apostrophe match and the output ceiling: `iba/app/BUILD.md` entry 413.
- F6 to F8 (cluster case, prose around JSON, scratch runner): `iba/app/BUILD.md` entry 414; F7 also #2300 v2.
- RO13 renumbered from RO11 and ordinal 68 before live: `iba/app/BUILD.md` entry 415.

## 5. Open items

- #2295 U5, the scope resolver: next, in a Developer Mode session (`/developer-mode` as the first prompt). Claude.
- #2296 U6, #2297 U7, #2299 U9: later units. Claude.
- #2287 (fixed in U5), #2262 (fixed in U6). Claude.
- #2301: pruning held to 2026-10-28 or later; the researcher validates the database first, and the design choice (a), (b) or (c) is still open. Researcher.
- #2270: the advisory findings, with the researcher.

## 6. Git

- branch: `main`
- commit: `55d44cac30dd1e6c77d651c4b9f414c047fef6f9` ("session 20261026: #2286 U1 to U4 and U8 built in Developer Mode ...")
- push: `To https://github.com/lcilliers/Bible_Projects.git` / `b52f7bed..55d44cac  main -> main`
- note: B:26 asks for commits as units complete; this session committed nothing until the close (U1 to U4 and U8 in one commit). Next session commits each unit as it is approved.
