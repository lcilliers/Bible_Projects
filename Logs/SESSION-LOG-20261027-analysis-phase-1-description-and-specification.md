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

## 5. Open items

- #2320: with the researcher for acceptance of the build and the test run; it carries a new version of the description file, the trial reading m21-asking-test (46 draft observations from the earlier process, not withdrawn), and the deletion of a stray 894 MB database copy at C:\c, created by Claude's own path error and removable only by the researcher because the folder is a protected path (Claude, then the researcher).
- The B:27 and B:100 rule slips listed in Logs/compliance/COMPLIANCE-20261027-95543bd0.md: carried on #2320 for the next version of the description (Claude).
- The older items assigned to Claude (#2161, #2259, #2305, #2308, #2268, #2301, #2171, #2172, #2235, #2262, #2276, #2278, #2280, #2296, #2303): untouched; #2276, #2278, #2280, #2262, #2296 and #2308 are met by the build and settle after the researcher's test of #2320.

## 6. Git

(written after the commits)
