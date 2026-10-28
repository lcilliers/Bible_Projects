# Session log 2026-10-27: Analysis_phase_1: description, specification and build (#2318, #2319, #2320)

Session id: 95543bd0-7cc2-4f14-b7f8-02aa51147ba4. Mode: Developer Mode (marker set 2026-10-27T11:21:17Z).

## 1. Scope

2026-10-27. After the #2316 test failed because steps 1 to 3 were not built to the requirements, the researcher asked for a new escalation to build them correctly (#2318) and named the three steps Analysis_phase_1. The session wrote a description of what the code of the five steps did and which config it read; gathered the specification from the earlier escalations; read the early-September lexical work for what the observations must cover (#2319); wrote the specification through four versions on the researcher's rulings (query by verse, the JSON as an index, accept, modify or soft delete, open items out of phase 1); and then built Analysis_phase_1 to specification v4 (#2320), tested on a copy, applied live.

## 2. Escalations

- #2318 (Rebuild reading steps 1 to 3 to the requirements): raised; description, specification v1 to v4 handed over; the researcher's rulings recorded verbatim (v5 to v13); completed by the researcher's approval (v14).
- #2319 (Analysis_phase_1: define what observations must cover): raised for section 4 of the specification; the digest of the earlier lexical work, the section 4 draft and the researcher's decisions D-a to D-d recorded (v1 to v9); completed by the researcher's approval (v10).
- #2320 (Build Analysis_phase_1 to specification v4): raised; the build, its tests and the live application recorded (v2 to v4); with the researcher for acceptance and the test run.
- #2321 (raised by the failed Config-Maintenance validation, two coherence errors from the retired step reading.gather): resolved self-correctable (v2) by the migration of run DEVMODE-2320-ANALYSIS-PHASE-1-GATHER-RETIRED-20261027.
- #2316 (Test steps 1 to 3 on new and existing subgroups): updated (v9) to point to #2318.

- #2323 (opened by the researcher for the live-test findings): built the `deleted` columns, the fixing of errors in the check, the kind/subgroup/stage rules, unconfirmed fixes and the `leave` action; handed over ready_for_approval (v5 to v10); on the same item the researcher's later messages are recorded (v10).

- #2320 (fourth stretch): the test of Gen 43:27 failed; Record now enforces the rules for stating an observation (spec 4.1, 4.2); handed over ready_for_approval (v11); the researcher's question about a background task is recorded on v12.

- Fifth stretch (2026-10-28): #2323 v7 to v10, #2320 v11 to v19, #2325, #2326, #2327 and #2328 worked and handed over (#2325 v4, #2326 v4, #2327 v2, #2328 v2, #2320 v19 with the researcher).

- Sixth stretch (2026-10-28): #2301 built and handed over (v9, the rollback method); #2320 v20 (node 13896 checked correct, the description file retired); backups/ cleared of 4.9 GB of copies no longer needed (recorded on #2301 v9).

## 3. Files

- outputs/escalation/2318-analysis-phase-1-description-v1-20261027.md (new): the code of Open, Gather, Observe, Record and the two gates as it was before the build, with config read and data tables.
- outputs/escalation/2318-analysis-phase-1-specification-v4-20261027.md (new; v1 to v3 in outputs/escalation/archive/): the specification of Analysis_phase_1.
- outputs/escalation/2319-lexical-phase-1-phase-2-prior-work-v1-20261027.md and outputs/escalation/2319-section-4-draft-v1-20261027.md (new): the digest of the early-September lexical work and the section 4 draft.
- outputs/escalation/2320-test-results-v1-20261027.md (new): the per-case results of the build's tests.
- iba/app/lib/reading.py, iba/app/lib/observationrecord.py, iba/app/handlers/reading.py, iba/app/ps/Reading.ps1 (changed): the build.
- iba/app/migration/archive/analysis_phase_1_2320_v1_20261027.py and iba/app/migration/archive/analysis_phase_1_2320_v2_20261027.py (new): the config and schema migrations, applied live.
- iba/app/tools/temp_2320_analysis_phase_1_test_run.py and iba/app/tools/temp_2320_dispatch_test_run.py (new): the tests.
- iba/app/BUILD.md section 424, iba/app/USER-GUIDE.md section 8.2, iba/docs/ps tools worksheet.xlsx tab Reading (changed): the docs.
- Logs/compliance/COMPLIANCE-20261027-95543bd0.md (new): the session compliance file.
- outputs/escalation/ escalation history files, escalation-list and escalation-context exports (generated).
- iba/app/db/snapshots/iba-20261027T162704Z-pre-2320-analysis-phase-1.db (new): the pre-migration rollback snapshot.
- Database iba.db: escalation rows #2318, #2319, #2320, #2321 and updates to #2316; 27 cfg writes (run DEVMODE-2320-ANALYSIS-PHASE-1-20261027) and 9 cfg writes (run DEVMODE-2320-ANALYSIS-PHASE-1-GATHER-RETIRED-20261027), all in cfg_change_detail; the column ib_observation.parts added. No data row of ib_observation or ib_node was written live.
- .claude/.developer-mode-active (the marker, not tracked).

- Files (third close): `iba/app/lib/reading.py`, `observationrecord.py`, `priorcapture.py`, `recordingpass.py`, `stage1coverage.py`, `strandreading.py`, `versecollate.py`, `versescope.py`, `versereadinggenerate.py`; migrations `iba/app/migration/archive/analysis_phase_1_2323_v1_20261027.py` to `..._v4_20261027.py`; tests `iba/app/tools/temp_2323_deleted_and_fixes_test_run.py` (34), `temp_2320_analysis_phase_1_test_run.py` (54), `temp_2320_dispatch_test_run.py` (7); `outputs/escalation/2323-test-results-v1-20261027.md`; BUILD.md section 425; USER-GUIDE section 8.2.

## 4. Decisions

- Researcher: create a new escalation to build the three steps correctly; name them Analysis_phase_1; the description is the whole of what a run may do. Recorded in #2318 v1, v2 and v8.
- Researcher: the specifications are in the earlier escalations. Recorded in #2318 v4 and outputs/escalation/2318-analysis-phase-1-specification-v4-20261027.md.
- Researcher: all surfaces of a scope verse are in scope; the JSON is the one version of the scope; step 2 gathers only; gaps come at step 4. Recorded in #2318 v5, v6, v8 and the specification rows 1.7, 1.9, 2.8, 2.10.
- Researcher: the verse understanding versus the claims; rulings 7.1 to 7.4 and decisions D-a to D-d; polarity belongs to the observation; a standalone word is ignored. Recorded in #2319 v5 to v9 and the specification section 4.
- Researcher: query by verse; the JSON an index; accept, modify or soft delete observations and nodes; modify in place; open items move out of phase 1. Recorded in #2318 v11, v13 and the specification 3, 4.5, 4.7.
- Researcher: #2318 and #2319 approved; start the build of #2320. Recorded in #2318 v14, #2319 v10 and #2320 v2.
- Claude, taken in the build for the researcher to correct: a third evaluation result bears_on; a word with no cluster takes the T-code it is classified under; reading_verse still written by Open; the JSON in outputs/reading/<label>/ and not the cluster folder; identical surfaces count as one evaluation. Recorded in iba/app/BUILD.md section 424 and #2320 v3.
- Claude self-correctable: the retired step reading.gather left its failure routing and write grants, found by the validation and fixed by iba/app/migration/archive/analysis_phase_1_2320_v2_20261027.py (recorded in #2321 v2).
- Claude self-correctable: the first Compliance.ps1 call used the wrong shell; re-run under pwsh 7. Recorded in Logs/compliance/COMPLIANCE-20261027-95543bd0.md (B:28).
- Not decided: a new version of the description file for the code as built (it describes the code before the build); whether a reading may keep the JSON in the cluster folder. Recorded in iba/app/BUILD.md section 424.

- Researcher's decisions after the second close, each recorded on #2323 v10 and in BUILD.md section 425: the delete columns on both tables; fixes found in the check need no separate approval (recorded in `cfg_method_rule` RS-04 and #2323 v10); the kind (tag) and subgroup of a kept observation (#2323 v10); stage Analysis_phase_1 on new rows (cfg_enum ib_observation.stage, #2323 v6); stages must not filter, only the wording, so the action `leave` replaces the own_stages setting (cfg_setting reading.verse_loop, #2323 v9).

- Decisions (fourth stretch): the code enforces the ten parts, the nodes of an act, the primary operation, link and party observations and the reading on kept nodes (cfg_method_rule RS-08, cfg_setting reading.verse_loop, iba/app/BUILD.md section 426, #2320 v11); the researcher's answer on whether this is the enforcement wanted is open.
- Files (fourth stretch): iba/app/lib/reading.py, iba/app/lib/observationrecord.py, iba/app/migration/archive/analysis_phase_1_2320_v3_20261028.py, the three test files, iba/app/BUILD.md section 426, iba/app/USER-GUIDE.md section 8.2.

- Files (fifth stretch): iba/app/lib/reading.py, observationrecord.py, lexical.py, filingkit.py, cfg.py, priorcapture.py, handlers/reading.py, ps/Reading.ps1; migrations iba/app/migration/archive/analysis_phase_1_2320_v4_20261028.py, verse_lexical_multi_code_span_surface_2326_v1_20261028.py, reading_folders_in_cluster_folder_2328_v1_20261028.py, analysis_phase_1_2323_v3 and v4; tests iba/app/tools/temp_2320_rules_in_config_test_run.py (19), temp_2326_surface_migration_test_run.py (14), temp_2328_reading_folder_test_run.py (18), temp_2327_existing_finding_test_run.py (9), temp_2325_node_move_test_run.py (11); BUILD.md sections 425 to 431; GOVERNANCE.md section 3; USER-GUIDE section 8.2; outputs/escalation/2326-verse-lexical-surface-changes-v1-20261028.tsv and 2328-reading-folder-moves-v1-20261028.tsv.
- Decisions (fifth stretch, each recorded on its escalation): the stage does not filter and the action leave decides by wording (#2323 v9); the rules for stating an observation enforced (#2320 v11, cfg_method_rule RS-08); a node moved takes the next seq (#2325 v4); the surface of a code in a multi-code span is its STEP gloss, verse_lexical corrected for 1882 occurrences and the 3 held ones left (#2326 v3, v4); an existing party or link finding gains nodes (#2327 v2); readings filed in their home cluster's folder (#2328 v2); the rules are config rows (#2320 v18, reading.observation_rules, lexical.span_surface, report.cluster_folder_name_rule).

- Files (sixth stretch): iba/app/lib/dbsnapshot.py, migration iba/app/migration/archive/backup_rollback_method_2301_v1_20261028.py, test iba/app/tools/temp_2301_rollback_method_test_run.py (19), iba/app/BUILD.md section 432, iba/app/USER-GUIDE.md (database copies and rollback), outputs/escalation/archive/2318-analysis-phase-1-description-v1-20261027.md (archived).
- Decisions (sixth stretch): the rollback method replaces the full copy per run (cfg_setting backup.rollback_method, #2301 v8); node 13896 stays characteristic and the description file is not kept up to date (#2320 v20); backups/ cleared of unneeded copies (#2301 v9).

## 5. Open items

- #2320: with the researcher for acceptance of the build and the test run; it carries a new version of the description file, the trial reading m21-asking-test (46 draft observations from the earlier process, not withdrawn), and the deletion of a stray 894 MB database copy at C:\c, created by Claude's own path error and removable only by the researcher because the folder is a protected path (Claude, then the researcher).
- The B:27 and B:100 rule slips listed in Logs/compliance/COMPLIANCE-20261027-95543bd0.md: carried on #2320 for the next version of the description (Claude).
- The older items assigned to Claude (#2161, #2259, #2305, #2308, #2268, #2301, #2171, #2172, #2235, #2262, #2276, #2278, #2280, #2296, #2303): untouched; #2276, #2278, #2280, #2262, #2296 and #2308 are met by the build and settle after the researcher's test of #2320.

- #2323: with the researcher for acceptance; open there: restoring the role of strand-reading node 13896 (observation 11877) on the researcher's word;  (`C:\c` was checked on 2026-10-28 and does not exist); #2301 (snapshot pruning) unresolved (Claude, outside Analysis_phase_1).

- #2320: with the researcher for acceptance of the enforcement; the 5 GB task log bak4t901b.output in the Claude temp folder is for the researcher to delete or have deleted (#2320 v12).

## 6. Git

Branch: main. First close, first commit: 347de644 (the description and specification v1; pushed `c40d2878..347de644`), then 025e1dbe "session 20261027: session log git confirmation" (pushed `347de644..025e1dbe`). Second close (the lexical digest, specification v2 to v4, the build of #2320): commit 0ed841c6 "session 20261027: Analysis_phase_1 specification v4 (#2318, #2319) and the build to it (#2320): scope JSON as index, query by verse, accept/modify/soft delete, new gate; migrations, tests, docs; session log and close reports".

Push output: `To https://github.com/lcilliers/Bible_Projects.git   025e1dbe..0ed841c6  main -> main`.

Third close (2026-10-28): branch main; commit 7ea1c897 "session 20261028: #2323 deleted columns ..." (also the other session's untracked compliance file and the reading m21-asking outputs, read first and committed as project records). Push output: `To https://github.com/lcilliers/Bible_Projects.git   59d8c908..7ea1c897  main -> main`.

Fourth close (2026-10-28): branch main; commit 9bf3615c "session 20261028: #2320 Record enforces the rules for stating an observation ...". Push output: `To https://github.com/lcilliers/Bible_Projects.git   5fc7bbff..9bf3615c  main -> main`.

Fifth close (2026-10-28): branch main; commit e2ff7916 "session 20261028: Analysis_phase_1 fixes #2323, #2325, #2326, #2327, #2328; rules for stating an observation enforced and held as config rows ...". Push output: `To https://github.com/lcilliers/Bible_Projects.git   a538ec56..e2ff7916  main -> main`.
