# Session log 2026-11-06 — the surface cycle in the database (Developer Mode)

Session id: `325129d4-3704-424e-9f5b-0f131a1db2ab` (window 2026-11-04 to 2026-11-06)

## 1. Scope

Developer Mode. The surface work of 2026-11-04 and 2026-11-05 (surface groups #2354, base forms #2359, collections #2360) was systemised as five repeatable modules over tables in `iba/app/db/iba.db` (escalation #2361, design v3 approved by the researcher on the condition that all of the researcher's comments were built in): files demoted to working files, tables extended rather than duplicated, junk surfaces soft deleted, prompts and models registered and versioned, every AI call through one controlled client with an `ai_call` row, every change traceable, each module reproducing the recorded prototype result and tested on a copy. Stages 0 to 6 were built, applied live (each after a named snapshot) and documented. No real AI run was made.

## 2. Escalations

- #2361 — updated (stage records v16 to v23; the researcher's messages of the window at v23): the whole programme, stages 0 to 6.
- #2359, #2360 — held, untouched (waiting on the researcher's review of the flags, and on a real Seed and Ask).
- #2362 — answered by the researcher ("A: leave them", the 118 empty-string `verse_lexical` rows).
- #2363 — raised and parked (the `ib_observation` note names 1 of 6 writers; old drift found by the older test).
- #2366 — raised: port the judge work-period cycle to `group.judge` (decision_required).
- #2365 — raised: STEP server down, six spine gaps unverified at close (carries the SC2 findings).
- #2357 — advisory findings recorded as new versions by `configmaint.validate` (orphan settings, Node-Resolve); not mine to close.

## 3. Files

- Migrations (archived, `iba/app/migration/archive/`): `junk_surfaces_2361_v1`, `surface_files_2361_v1`, `surface_cycle_schema_2361_v1`, `surface_cycle_load_2361_v1`, `surface_files_register_2361_v1`, `surface_structure_2361_v1`, `surface_cycle_ambiguous_2361_v1`, `surface_group_2361_v1`, `surface_exempt_2361_v1`, `surface_resolve_2361_v1`, `ai_client_2361_v1`, `surface_collection_2361_v1`, `surface_collection_fix_2361_v1`, `surface_collection_ask_2361_v1`, `surface_maps_2361_v1`, `surface_maps_fix_2361_v1`, `surface_hygiene_2361_v1` (all `_20261106`).
- Code, `iba/app/lib/`: `manifest.py` (updated), `surfacestructure.py`, `surfacegroup.py`, `surfaceresolve.py`, `aiclient.py`, `collectionbuild.py`, `collectionask.py`, `surfacecyclemap.py`, `surfacehygiene.py`, `surfacebase.py` (reduced), `cfgreport.py` (sections 16 and 17).
- Code, `iba/app/handlers/`: `surfacestructure.py`, `surfacegroup.py`, `surfaceresolve.py`, `ai.py`, `collectionbuild.py`, `surfacebase.py` (Ask only), `reports.py`, `configmaint.py` (hygiene finding).
- Entry points, `iba/app/ps/`: `Surface-Structure.ps1`, `Surface-Group.ps1`, `Surface-Resolve.ps1`, `Ai-Control.ps1`, `Collection-Build.ps1`, `Surface-Base.ps1` (Ask only), `Manifest-Rebuild.ps1`; worksheet `iba/docs/ps tools worksheet.xlsx` (tabs for each).
- Tests, `iba/app/tools/`: `temp_2361_manifest_test_run.py`, `temp_2361_structure_test_run.py`, `temp_2361_group_test_run.py`, `temp_2361_resolve_test_run.py`, `temp_2361_ai_test_run.py`, `temp_2361_collection_test_run.py`, `temp_2361_collection_ask_test_run.py`, `temp_2361_independence_test_run.py`; `temp_2359_surface_base_test_run.py` moved to `iba/app/tools/archive/`.
- Documents: `iba/app/BUILD.md` sections 456 to 466, `iba/app/USER-GUIDE.md` sections 8.9 to 8.15 and 10, `iba/app/CHARTER.md` section 5, `outputs/escalation/2361-surface-cycle-registration-design-v3-20261106.md` and the stage-0 sweep and mapping files; the config reports `outputs/configs/CONFIG-REPORT-v6xx` to `v705`.
- Data folders: `_analytics/surfaces/working_files`, `_analytics/surfaces/exports`, `_analytics/surfaces/discarded` (the moved prototype files, registered in `file_manifest`).

## 4. Decisions

Researcher's own decisions:
- Design v3 approved, on the condition that all comments were built in — recorded on #2361 and in `outputs/escalation/2361-surface-cycle-registration-design-v3-20261106.md`.
- The junk surfaces are marked deleted, with the tables that reference them — recorded in `iba/app/BUILD.md` section 456 (`surface_term`, `surface_event`).
- The 118 empty-string `verse_lexical` rows are left ("A: leave them") — recorded on #2362 and #2361 v23.
- "Yes, continue" through stages 3, 4 and 5, "Yes, build it" (the embedding call and collection seeding), "Yes, stage 6", "Close session" — recorded on #2361 v23.

Decisions I made and recorded (self-correctable, within the approved design):
- The twelve `a | b` pseudo-base terms of the first load were wrong: they became the state `base_ambiguous` with flags — `iba/app/BUILD.md` section 459 and the table `surface_term`.
- The group repoint: bases judged `other` are corrected by rule, bases judged `being` are only proposed — `iba/app/BUILD.md` section 460 and `cfg_setting` `group.repoint_auto_base_groups`.
- A removed collection link is respected; the 18 pairs the prototype left out are recorded as removed links — `iba/app/BUILD.md` section 463 and the table `collection_link`.
- The order of stages 3 and 4 changed (resolve first; the AI writers with the AI client) — `iba/app/BUILD.md` section 461.
- The shortlist size 60 and the list maximum 20 are my choice, as the recorded runs did not keep them — `iba/app/BUILD.md` section 464 and `cfg_setting` `collection.shortlist_size`.
- The earlier file route of the AI base was retired; `Surface-Judge.ps1` kept until its work-period cycle is ported — `iba/app/BUILD.md` section 465 and `cfg_step`.

## 5. Open items

- #2359 (Claude) — the researcher reviews the structure flags, among them the 14 `base_ambiguous` words (`surface_flag` kind structure_conflict).
- #2360 (Claude) — a real Seed and Ask on a word, and the 18 withheld associated pairs, are the researcher's to start or decide.
- #2363 (Claude, on hold) — `ib_observation` note.
- #2365 (Claude) — start the STEP server and re-run the spine check (the six SC2 gaps).
- #2357 — advisory config findings (three orphan settings; Node-Resolve).
- #2366 (Claude, decision_required) — port the work-period cycle to `group.judge`, then retire the `Surface-Judge.ps1` file route and `surface_judge.word_prompt` (BUILD.md section 465).

## 6. Git

- branch: `main`
- first commit: `f52f8422` — `session 20261106: the surface cycle in the database (#2361, stages 0 to 6), session log, compliance file and close reports` (196 files)
- push: `To https://github.com/lcilliers/Bible_Projects.git   6362537f..f52f8422  main -> main`
- left out of git (regenerable or discarded, via `.gitignore`): `_analytics/surfaces/working_files/collection/embeddings/` and `_analytics/surfaces/discarded/*.npy`
- the second commit (this section) is `session 20261106: session log git confirmation`
