# Session log 2026-10-30: #2329 the nine observation items, nuance pointers, verse timing (Developer Mode)

Session id: 02063e4e-16df-4e1a-bb9f-7b8cda534e0f (Developer Mode, declared with /developer-mode).

## 1. Scope

2026-10-30: Developer Mode session. On "build 2329", built the Developer Mode part of the #2329 plan: each of the nine items of spec 4.2 is its own observation (`parts.item`), with the config first (`reading.observation_items`, `reading.nuance_pointers`, RS-10, RS-08 and RW-02 restated), the checks in `iba/app/lib/observationrecord.py` and `iba/app/lib/reading.py`, and the time per verse in the scope JSON. Tested on copies, applied live, documented. The researcher approved the build ("Approve build"). The redo of the 39 verses is not run (standard-mode work).

## 2. Escalations

- #2329 (Phase 1 observations: fit for purpose, asking record): taken up (v21 in-progress), build handed over with the test results (v22 ready_for_approval, NeedsFollowup), approved by the researcher (v23), the researcher's backlog remark recorded (v24).
- #2331 (Reading: no way to put a done verse back in hand): completed (v5) with its test result.
- #2332 and #2333 (hard-error records): closed by ResolveSelfCorrectable (not defects; the migration was already in archive/).
- #2268 (Reading process not built on the study's expectations): corrected to on-hold, as the researcher had parked it on 2026-10-25.
- #2259, #2161, #2320: commented (v8, v11, v33): gated on the #2329 redo.
- The on-hold items assigned to Claude (#2171, #2172, #2235, #2276, #2278, #2280, #2303): read, untouched.

## 3. Files

- `iba/app/migration/archive/analysis_phase_1_2329_v3_20261030.py`: the config migration (applied live, run DEVMODE-2329-OBSERVATION-ITEMS-20261030).
- `iba/app/lib/observationrecord.py`: `check_item_parts`, `copies_verse`, `items_setting`, `item_keys`; `check_parts`, `check_party`, `complete_parts` removed.
- `iba/app/lib/reading.py`: the coverage rules in `_validate_sheet`, the sheet's `items`, `nuances` and `items_absent`, the `parts_not_an_item` flag, `in_hand_at` and `elapsed_seconds`.
- `iba/app/tools/temp_2329_observation_items_test_run.py`: the new test, 43 of 43. Adapted: `iba/app/tools/temp_2320_analysis_phase_1_test_run.py` (54 of 54), `iba/app/tools/temp_2323_deleted_and_fixes_test_run.py` (34 of 34), `iba/app/tools/temp_2320_rules_in_config_test_run.py` (19 of 19), `iba/app/tools/temp_2331_reopen_test_run.py`. Retired: `iba/app/tools/archive/temp_2329_fit_for_purpose_test_run.py`.
- `iba/app/USER-GUIDE.md` (the Record rules paragraph), `iba/app/BUILD.md` (entry 435).
- `Logs/compliance/COMPLIANCE-20261030-02063e4e.md`, this log, `iba/app/reports/session-close-v*-20261030.md`, and the escalation exports the scripts wrote under `outputs/escalation/` and `outputs/configs/`.
- Live config rows (through `apply_logged`): `cfg_setting` reading.observation_items and reading.nuance_pointers, reading.observation_parts and reading.observation_rules (old keys removed), `cfg_method_rule` RS-08, RW-02 (restated) and RS-10 (new), the `cfg_utility` row of the migration.
- Named snapshot before the migration: `iba/app/db/snapshots/kept/iba-20261030T093413Z-before-migration-analysis-phase-1-2329-v.db`.

## 4. Decisions

Researcher's own:
- "build 2329. you asked some question which you should answer for yourself by judging if your answer would work and is the right selection to achieve the objective.": the three open decisions of the plan are Claude's to judge; recorded in #2329 v24 and in `iba/app/migration/archive/analysis_phase_1_2329_v3_20261030.py`.
- "Approve build": the Developer Mode build is accepted; recorded in #2329 v23.
- "I see 2329, 2320, 2268, 2259, 2161 are all approved, assigned to you. that tells me it is awaiting an action from you.": recorded in #2329 v24.

Claude's, within the approved build:
- Existing kinds kept, the item held in `parts.item`; the `parts` column kept and small; the mode of an operation as `parts.mode`: `iba/app/migration/archive/analysis_phase_1_2329_v3_20261030.py` and `iba/app/BUILD.md` entry 435.
- Self-correctable: #2332 and #2333 closed (not defects), #2331 completed, #2268 corrected to on-hold: recorded in #2331 v5 and #2268 v26.

## 5. Open items

- #2329 (Claude): the redo of the 39 m21-asking verses in a standard-mode session (plan `outputs/escalation/2329-build-and-redo-plan-v1-20261030.md` section 2).
- #2320 (Claude): gated on the #2329 redo.
- #2259 and #2161 (Claude): gated on the #2329 redo and the claims phase (#2315).
- The tests `iba/app/tools/temp_2325_node_move_test_run.py` and `iba/app/tools/temp_2327_existing_finding_test_run.py` replay sheets of the old twelve-part form and no longer run: carried in #2329 (stated limit; their mechanics are covered by the 2320 and 2323 tests).
- #2171, #2172, #2235, #2276, #2278, #2280 and #2303 (Claude): on hold, untouched.

## 6. Git

(written after the first commit)
