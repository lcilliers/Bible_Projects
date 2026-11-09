# Session log 2026-11-09 -- collections from the unassigned bases, and the progress control for long Ollama jobs

Session: `41e7251b-aae0-4234-9426-2f9fe391cad2` (standard mode, started 2026-11-07)

## 1. Scope

2026-11-07 to 2026-11-09. Escalation #2388: build collections from the surfaces (behaviour and states) not yet in any collection, seeded from the dominant sub-group of each base. The researcher ruled the seed rule, had non-state words and computed bases moved to `other`, approved a pilot of ten collections, and then instructed (verbatim): "continue with the other sub groups in the same way, make sure there are a proper monitor on progress, in fact, the ollama processes should always have a proper progress control method to check on progress. ensure that the processes run through the terminal that can be independent of the sleep on the desktop." Built the progress control (`Long-Run.ps1`) and started the batch of 223 sub-groups (about 12 minutes each). The batch was still running at close.

## 2. Escalations

- #2388 updated v1 to v19: raised, rulings recorded, pilot of ten run, batch started, progress and the one failure recorded. Still in progress, assigned to Claude.
- #2389, #2390, #2391 approved by the researcher and applied (recorded in #2388 v8).
- #2394 to #2402 raised through configmaint.propose, approved by the researcher in chat ("Approve all nine"), applied, completed.
- #2404 (validate found the new files unregistered) resolved by the registration, completed.
- #2379, #2392 not changed: acknowledged in chat. #2357, #2366, #2376 not touched.

## 3. Files

- New: `iba/app/lib/longrun.py`, `iba/app/handlers/longrun.py`, `iba/app/ps/Long-Run.ps1`, `iba/app/tools/collection_batch_run.py`, `iba/app/tools/temp_2388_longrun_test_run.py`, `iba/app/tools/temp_2388_set_group_test_run.py`.
- Edited: `iba/app/handlers/surfacegroup.py`, `iba/app/lib/surfacegroup.py`, `iba/app/lib/surfaceresolve.py`, `iba/app/ps/Surface-Group.ps1`, `iba/app/USER-GUIDE.md` (section 8.17), `iba/app/BUILD.md` (entry 472), `iba/docs/ps tools worksheet.xlsx` (tab Long-Run).
- Run files: `Logs/longrun/collection-batch.plan.json`, `Logs/longrun/collection-batch.progress.json`, `Logs/longrun/collection-batch.log`, `Logs/2388-ask-pilot-20261108.log`.
- Records: `outputs/escalation/2388-rulings-and-computed-bases-v1-20261107.md`, `outputs/escalation/2388-pilot-seeds-v1-20261108.json`, `Logs/compliance/COMPLIANCE-20261107-41e7251b.md`.
- Other changed files in the tree come from the other sessions of 2026-11-07 to 2026-11-09.

## 4. Decisions

- Researcher: seed rule is the dominant sub-group ("Sub-cluster (B)"): recorded in #2388 v3.
- Researcher: the Set action design and both computed-base lists approved ("Approve both"): recorded in #2388 v5.
- Researcher: judge the 37 computed bases ("Approve, judge the 37"): recorded in #2388 v8.
- Researcher: options A and B and a pilot of ten ("A, B, pilot of 10"): recorded in #2388 v10.
- Researcher: continue with the other sub-groups with a proper progress control that survives desktop sleep: recorded in #2388 v16.
- Researcher: registration of the progress control ("Approve all nine"): recorded in #2394 v3 and applied in the `cfg_work_package`, `cfg_step` and `cfg_utility` tables.
- Claude, self-correctable: the driver reads the output text for refusals because the collection script exits 0 on a refusal: recorded in `iba/app/BUILD.md` entry 472.
- Claude, self-correctable: #2404 resolved once the files were registered: recorded in #2404 v2.
- Claude: a retry after a database lock is not built; it needs the researcher's say-so: recorded in #2388 v19.

## 5. Open items

- #2388 (Claude): the batch runs until about 2026-11-10 09:00; then one more `Long-Run.ps1 -Action Start -Job collection-batch` for the failed sub-group stumble; then review the collections with the researcher.
- #2392 (Researcher): grouping-evidence decision, carried unchanged.
- #2379 (Claude): multi-session exploration of the surface work, carried unchanged.
- #2357 (Researcher): the config validate finding, carried unchanged.

## 6. Git

Branch: `main`. Commit: `b6c7337d30ff8f6778745701dd339ae619bb183c` (session 20261109: progress control for long Ollama jobs (Long-Run) and the collection batch for #2388 ...).
Push output: `To https://github.com/lcilliers/Bible_Projects.git` / `528f93bf..b6c7337d  main -> main`.
