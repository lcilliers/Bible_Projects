# Session log 2026-11-22: validation after stage 4 (#2538) built, promoted and applied to one verse; #2540 fixed; marker added to the extract

Session id: 604473ee-65af-4a4c-a924-9175f2fd29f7 (Developer Mode; the session spans 2026-11-21 evening to 2026-11-22 and was continued across two context summaries)

## 1. Scope

2026-11-21 to 2026-11-22, Developer Mode. Escalation #2538: capture the analytic work as a repeatable process, as a validation after stage 4 of a collection (pilot: thought, id 56). The researcher's principles were recorded as they were given (scope a to d, two markers evidence and inner being, trace nodes for every inner-being observation, older observations evaluated, two validations never concurrent). The validation was piloted on 1Chr.28.9 (55 observations), the actions were built (21 functions) and tested on a copy (53 + 27 tests), the validation was promoted to three registered steps (ValidatePull, ValidateRecord, ValidateCheck) with a migration, and on the researcher's word ("Yes, apply it") the 221-action sheet for 1Chr.28.9 was applied to the live data under a named snapshot. #2540 (Escalation.ps1 call failures) was fixed so that Raise and Update refuse a malformed call once, with every problem listed, and closed on the researcher's approval. The researcher then found no marker column in the observations extract; the marker (ib_observation.nature) was added to four sheets of the evidence workbook, tested on the verse report only (the run of the collection form and two tests was stopped by the researcher). The researcher then questioned the cost: 15,461 of 15,511 live observations are unmarked and one verse took the day. The session ended in the researcher's statement that he is unsure whether to continue; nothing was deleted; the direction is his.

## 2. Escalations

- #2538: updated v22 to v24 (v23 the live application, v24 the verbatim record of the researcher's words at close); in progress, assigned Claude, not for approval; the proposal is not yet read by the researcher as a whole.
- #2540: history read, fixed (BUILD.md 549), updated v2 (ready_for_approval to the researcher), closed v3 on his approval ("Approve closure").
- #2541: held by Claude, not started (the four stored-data corrections of #2533).
- #2542: held by Claude, not started (partner words in thought pairings).
- #2539: awaits the researcher's closure approval, not touched.

## 3. Files

- Code: `iba/app/lib/validationactions.py`, `iba/app/lib/collectionvalidate.py`, `iba/app/handlers/collectionbuild.py`, `iba/app/ps/Collection-Build.ps1`, `iba/app/ps/Escalation.ps1`, `iba/app/lib/collectionevidence.py`, `iba/app/lib/collectionevidencereport.py`.
- Config: `iba/app/migration/archive/validation_2538_v1_20261122.py` (applied live; 30 cfg writes and the nature column).
- Tests and scratch (temporary): `iba/app/tools/temp_2538_validation_actions_test_run.py`, `iba/app/tools/temp_2538_validate_step_test_run.py`, `iba/app/tools/temp_2538_validation_apply_1chr28_9.py`, `iba/app/tools/archive/temp_2538_validation_pull.py`.
- Docs: `iba/app/BUILD.md` (546 to 550), `iba/app/USER-GUIDE.md`.
- Reports and sheets: `outputs/escalation/2538-validation-step-plan-v9-20261122.md`, `outputs/escalation/2538-validation-pilot-pull-thought-v1-20261122.md`, `outputs/escalation/2538-validation-pilot-reading-1chr-28-9-v1-20261122.md`, `outputs/escalation/2538-validation-pilot-actions-1chr-28-9-v1-20261122.md`, `outputs/escalation/2538-observations-fitness-1chr-28-9-v1-20261121.md`, `_analytics/surfaces/working_files/layers/validate-sheet-thought-1Chr.28.9.json`, `_analytics/surfaces/exports/validate-check-thought-v2-20261122.md`, `_analytics/surfaces/exports/verse-evidence-1ch-28-9-v1-20261122.xlsx`.
- Live data changed: ib_observation (nature, 4 created, 9 deleted, 17 restated), ib_node, ib_observation_change (25 deferrals, 26 annotations) for 1Chr.28.9, through ValidateRecord. Named snapshots: `iba-20261122T091122Z-pre-2538-validation.db`, `iba-20261122T163601Z-pre-2538-validation-apply-1chr28-9.db`.
- Compliance: `Logs/compliance/COMPLIANCE-20261121-604473ee.md`.

## 4. Decisions

- The researcher's: the marker has two values, evidence and inner being, and follows content not stage; every inner-being observation traces to evidence; older observations are all evaluated; the six observations that are neither are deleted; every finding is acted on or deferred to a named collection; proceed with the reading pilot, build, promote and apply on 1Chr.28.9. Recorded in #2538 (v22 to v24) and in cfg_method_rule VA-01 to VA-06 and IB-07 and cfg_setting validate.reading.
- Closure of #2540: the researcher's approval, recorded in #2540 v3.
- Claude's self_correctable fixes: Raise and Update refuse a malformed call once with every problem listed, recorded in BUILD.md 549 and #2540 v2; the marker column added to the extract, recorded in BUILD.md 550; the USER-GUIDE.md path of validationactions.py corrected at close, recorded in BUILD.md 550.
- Not decided: whether the project continues, and the direction for the 15,461 unmarked live observations (mark at creation in the stage 1 to 4 builds and leave old observations until a build touches them; default marks for structural stages; reading all). Recorded as open in #2538 v24.

## 5. Open items

- #2538: for the researcher's decision on direction; the proposal still to be read as a whole; the rest of thought's 1,175 observations unread (1,125 unmarked); deferrals of 25 observations await the owning collections' validations.
- #2541, #2542: held by Claude, not started.
- #2538: the marker extract change: the collection form of the workbook and the two evidence tests (`temp_2477_evidence_report_test_run.py`, `temp_2502_evidence_pairs_test_run.py`) are not run (stopped by the researcher); BUILD.md 550.
- #2538: config validate: the advisory finding that behaviour rule B:136 is partially enforced stands, for the researcher's judgement.

## 6. Git

_(written after the first commit)_
