# Session log 2026-11-13 -- node and observation salvage (Developer Mode)

Session id: 6ae98364-8d12-422e-9108-347df7261d1f

## 1. Scope

Developer Mode session on the nodes and observations salvage (#2484): rules B:130 and B:131, a read-only node checker, and fixes of duplicate nodes, missing occurrences, one node per occurrence, stale morph codes, supportive-node collections and "no inner-being role" statements; then the researcher's decision to re-read the analysis documents (handed to its own session, committed in 351e79d1 and a5cf91b8).

## 2. Escalations

- #2484: updated throughout, closed by the researcher; remaining classes handed to #2448.
- #2498: design for the re-read, raised by the re-read session; resolved or closed (#2493 to #2501).
- #2495: closed by the researcher; cluster and subgroup retired from nodes and observations (BUILD 527).
- #2496, #2497: carried; need the researcher's AnswerRun.
- #2481, #2485, #2490, #2492, #2487, #2483: closed on the researcher's instruction.
- #2448: carries the remaining classes (14,133 nodes without a role, 6,260 without a collection, 12 held stale codes, 74 surfaceless nodes).

## 3. Files

- iba/app/migration/archive/withdraw_duplicate_nodes_2484_v1_20261113.py, node_occurrence_2484_v1_20261113.py, node_occurrences_each_2484_v1_20261113.py, node_stale_codes_2484_v1_20261113.py, node_supportive_collection_2484_v1_20261113.py, node_no_role_statements_2484_v1_20261113.py
- iba/app/lib/nodecheck.py, iba/app/ps/Node-Check.ps1, iba/app/handlers/nodecheck.py, iba/app/tools/temp_2484_node_check_test_run.py
- iba/app/BUILD.md (entries 516 to 523)
- _analytics/reading-tools/node-check/no-collection-observations-20261113-v1-20261113.xlsx and .md
- named snapshots in iba/app/db/snapshots/kept/ (seven, pre-2484)
- Logs/compliance/COMPLIANCE-20261113-6ae98364.md

## 4. Decisions

- Researcher: duplicates withdrawn; missing occurrences set; one node per occurrence; stale codes reset; supportive nodes take their surface's collection; option B for no-role statements with a pilot of 30, then the rest; re-read of the 170+ documents first, then soft delete of nonsensical observations and nodes -- recorded in iba/app/BUILD.md entries 516 to 523 and #2448 v15.
- Researcher: #2492, #2481, #2485, #2490, #2487, #2483 closed -- recorded in #2448 v15 and the escalation table.
- Self-correctable fix: a loose no-role pattern (observation 693) reversed and tightened -- recorded in BUILD.md entry 522 and the ib_observation_change table.
- Rulings 4.1 to 4.6 -- recorded in #2484 and the cfg_behaviour_rule rows B:130 and B:131.

## 5. Open items

- the researcher's AnswerRun on the two dispatcher runs: carried #2448.
- #2448: remaining node classes and the evaluation after the re-read; also the test file temp_2320_analysis_phase_1_test_run.py line 216, which disagrees with config on standalone.

## 6. Git

Branch: main. Commit 3a26c1ed `session 20261113: node salvage session log, compliance evidence, close dispositions, close report`. Push: `a5cf91b8..3a26c1ed  main -> main` (https://github.com/lcilliers/Bible_Projects.git). Earlier work of this session was committed in 351e79d1 and a5cf91b8.
