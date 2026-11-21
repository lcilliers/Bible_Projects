# Session log 2026-11-21: stage 4 first built (#2528), then stage 2 and stage 4 rebuilt on the researcher's definitions (#2526)

Session id: 307ff161-099e-4868-8f37-cc4ed02af521 (Developer Mode)

## 1. Scope

2026-11-21. Developer Mode session. Started with "Build #2528": built stage 4 (the inner-being analysis) verse-first as steps 3.1 to 3.3, cleared the first grouping of `thought` (B2), retired the cluster reading in config, re-homed its rules, and aligned the stage wording; 44 of 44 tests, applied live. The researcher then showed the stage 2 grouping was wrong (the first attempt changed the unit from the surface to the Strong's code and re-judged membership), so a proposal was written (#2526) and the researcher answered Q1 to Q7: the unit is the surface placed whole, judged by meaning in context, no concept test before stage 4, and stage 4 starts from the subgroups and their stage 3 observations, with the behaviours discovered and only occasional reading back. Stage 2 and stage 4 were rebuilt on those answers and applied live as config; tests on copies 28 of 28 and 36 of 36, older suites green. Committed as b1c76ec7 on the researcher's request. No collection was read: the study is standard-mode work.

## 2. Escalations

- #2528: the stage 4 build; first built verse-first (v1 design, D1 and D2 approved), then redesigned (design v2) after the researcher's Q7 answer; handed over ready_for_approval (v10) with the E1 to E6 decisions for reading.
- #2526: the grouping and subgrouping proposal; the researcher's answers Q1 to Q7 and the clarifications of terms and stages recorded verbatim at close (v9); stage 2 built; assigned to the researcher.
- #2527: its gaps were taken into the audit and the proposal; not updated further.
- #2531: raised by configmaint.validate (66 errors after the cluster reading was retired), resolved self-correctable by the last two migrations.
- #2529, #2530: stage 5 and the narrative following the collections, named in the guide; untouched.

## 3. Files

- Code: iba/app/lib/collectiongroup.py (rewritten, surface as the unit), iba/app/lib/layerinner.py (new, rewritten once), iba/app/lib/verseevidence.py (new), iba/app/lib/layerreading.py, iba/app/lib/observationrecord.py, iba/app/lib/lexicalalignment.py, iba/app/lib/reading.py, iba/app/handlers/collectionbuild.py, iba/app/ps/Collection-Build.ps1.
- Tests: iba/app/tools/temp_2526_stage4_test_run.py (new), iba/app/tools/temp_2509_grouping_test_run.py (rewritten), iba/app/tools/temp_2503_collection_index_test_run.py, iba/app/tools/temp_2505_layers_test_run.py, iba/app/tools/archive/temp_2528_stage4_test_run.py (archived).
- Migrations (archive, applied live through apply_logged after named snapshots): iba/app/migration/archive/clear_thought_grouping_2528_v1_20261121.py, stage4_config_2528_v1_20261121.py, stage_wording_2528_v1_20261121.py, retire_cluster_reading_2528_v1_20261121.py, rehome_reading_rules_2528_v1_20261121.py, retire_cluster_reading_grants_2528_v1_20261121.py, fullpaths_2528_v1_20261121.py, stage2_surface_grouping_2526_v1_20261121.py, stage4_observation_led_2526_v1_20261121.py, ib_rule_names_2526_v1_20261121.py.
- Documents: iba/app/BUILD.md (entries 544 and 545), iba/app/USER-GUIDE.md, iba/docs/project-map.md.
- Deliverables: outputs/escalation/2526-grouping-and-subgrouping-proposal-v1-20261121.md, outputs/escalation/2528-stage-4-design-v2-20261121.md, outputs/escalation/2526-stage-2-and-4-test-results-v1-20261121.md, outputs/escalation/2526-stages-1-to-4-readiness-audit-v1-20261121.md; archived: outputs/escalation/archive/2528-stage-4-design-v1-20261121.md, outputs/escalation/archive/2528-stage-4-test-results-v1-20261121.md.
- Prose patches (archive/patches/): wa-prose-stage4-built-20261121T073702Z.json, wa-prose-stage2-4-redefined-20261121T131350Z.json; extract regenerated under Workflow/Programme/programme_prose/.
- Reports: Logs/compliance/COMPLIANCE-20261121-307ff161.md, outputs/configs/CONFIG-REPORT-v804-20261121.md.

## 4. Decisions

- Researcher: the unit of the grouping is the surface, placed whole in one subgroup (Q1, Q2); the evidence is the meaning in context, with hidden meaning in the different Strong's codes (Q3); `thought` and `thoughts` form a subgroup of their own (Q4); concepts come into play only in stage 4 (Q5); a small collection is one subgroup by default (Q6). Recorded on #2526 v9 and in outputs/escalation/2526-grouping-and-subgrouping-proposal-v1-20261121.md (4.10), cfg_setting group.reading, cfg_method_rule GP-01 to GP-04.
- Researcher: stage 4 starts from the subgroups and their stage 3 observations; behaviours are discovered from them with only occasional reading back; stage 4 sets building-block observations and formulates no claim; stage 5 pulls observations into behaviour statements and the subgroups fall away; surface groups are the four main groups, a collection consists of subgroups (Q7 and the clarifications). Recorded on #2526 v9, in outputs/escalation/2528-stage-4-design-v2-20261121.md, cfg_setting layer.reading and layer.interventions, cfg_method_rule IB-01 to IB-06, cfg_behaviour_rule 132, and archive/patches/wa-prose-stage2-4-redefined-20261121T131350Z.json.
- Researcher: build stage 2 and stage 4 in succession in Developer Mode; recorded on #2526 v9 and in iba/app/BUILD.md (entry 545).
- Researcher: D1 and D2 of the verse-first stage 4 design (every occurrence carries a node; a finding that links two subgroups sits on the lower id); superseded by design v2 and no longer in force; recorded in outputs/escalation/archive/2528-stage-4-design-v1-20261121.md.
- Claude (for the researcher's reading): behaviours are discovery flags gathering element observations by traced nodes; reading back is recorded with verse and reason; earlier-method observations are shown and never demanded; decisions E1 to E6 in outputs/escalation/2528-stage-4-design-v2-20261121.md, #2528 v10.
- Claude: the verse-first design, its test and its config items were retired the same day; recorded in iba/app/BUILD.md (entry 545) and cfg_setting layer.reading.

## 5. Open items

- #2526, #2528: with the researcher for approval; design v2 decisions E1 to E6 unread.
- #2526: stage 1 (the words) for `thought`, then the grouping, then stages 3 and 4: study work for a standard session (`/start-project`).
- N14 node validation flag: undefined; needs the researcher's definition (#2526).
- #2526: F9, no content check exists before a stage closes (the readiness audit).
- The retired cluster reading code and its 10 `reading` rows are kept: the researcher decides whether to delete them (#2529, #2530).
- Stage 5 (the claims) and the narrative structure: undecided (#2529, #2530).

## 6. Git

Branch: main. Commits: b1c76ec7 (the build, committed on the researcher's request) and 71fb1cda (the session close: log, compliance, close report). Push: `To https://github.com/lcilliers/Bible_Projects.git   7c23eb2b..71fb1cda  main -> main`. This log's git section is committed alone as "session 20261121: session log git confirmation".
