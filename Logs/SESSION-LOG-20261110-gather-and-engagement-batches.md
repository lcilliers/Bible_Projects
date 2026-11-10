# Session log 2026-11-10 -- Gather, engagement in batches, and the engagement of the 85 uncovered word bases

Session: `41e7251b-aae0-4234-9426-2f9fe391cad2` (standard mode, started 2026-11-07; this log covers 2026-11-10)

## 1. Scope

2026-11-10. Escalation #2388: the collection batch finished (223 sub-groups: 217 done, 5 skipped, the stumble redone). The 85 word bases left in no collection were gathered into one collection (`Collection-Build.ps1 -Action Gather`), engaged in 18 batches (`Engagement.ps1 -Pull -Batch`), grouped, and checked. The researcher decided (verbatim) "Let them stand (B)": no Review of the 1708 no-bearing verses. #2388 closed.

## 2. Escalations

- #2388 updated v20 to v30: Gather and batches proposed, the run recorded, the Review question put and answered, closed (v30).
- #2432 (collection.gather step), #2433 (its on-fail rule), #2434 (gathered tier in collection.export_tiers), #2435 (engagement.batch_size 150): proposed through configmaint.propose, approved by the researcher in chat, applied, completed.
- #2405 found already completed (the redo of the stumble).
- #2436 raised for the researcher: three decisions left after the run.
- #2437 raised after the close: the multi-word phrases and their head words.
- #2379, #2392 not changed: acknowledged in chat. #2357 not touched.

## 3. Files

- Edited code: `iba/app/lib/collectionbuild.py`, `iba/app/handlers/collectionbuild.py`, `iba/app/ps/Collection-Build.ps1`, `iba/app/lib/engagement.py`, `iba/app/handlers/engagement.py`, `iba/app/ps/Engagement.ps1`.
- Tests: `iba/app/tools/temp_2388_gather_test_run.py` (13 of 13), `iba/app/tools/temp_2388_batch_test_run.py` (15 cases).
- Documents: `iba/app/USER-GUIDE.md`, `iba/app/BUILD.md` (entries 478 and 479), `iba/docs/ps tools worksheet.xlsx` (tab Collection-Build).
- Outputs: `outputs/escalation/2388-uncovered-word-bases-v1-20261110.md`, `outputs/reports/engagement/engagement-uncovered-words-check-20261110-v2.md`, and the pull, assessment and review files under `_analytics/surfaces/working_files/engagement/` (`engagement-uncovered-words-*-20261110.json`).
- Run state: `Logs/longrun/collection-batch.progress.json`; `Logs/compliance/COMPLIANCE-20261107-41e7251b.md`.

## 4. Decisions

- Researcher: combine the 85 bases in one collection and run it through Engagement: recorded in #2388 v21.
- Researcher: Gather approved ("Approve Gather"): recorded in #2432 v4 and #2433 v4.
- Researcher: gathered tier in the export tiers ("Approve #2434"): recorded in #2434 v4.
- Researcher: engagement in batches ("Approve batches"): recorded in #2435 v4.
- Researcher: no Review of the no-bearing verses ("Let them stand (B)"): recorded in #2388 v29.
- Claude, self-correctable: Links ignores collections made by `collection-gather`: recorded in `iba/app/BUILD.md` entry 478.
- Claude, self-correctable: a per-surface key in the batch builder: recorded in `iba/app/BUILD.md` entry 479.
- Claude: the three leftovers went to the researcher as a decision item: recorded in #2436 v1.

## 5. Open items

- #2436 (Researcher): observation 20534, the 13 base words without verses, and the two previews.
- #2437 (Claude): design for attaching the 1166 multi-word phrases to a collected head word; goes to the researcher first.
- #2379 (Claude): multi-session exploration of the surface work, carried unchanged.
- #2392 (Claude): grouping-evidence decision, on hold, carried unchanged.
- #2357 (Researcher): the config validate finding, carried unchanged.

## 6. Git

Branch: `main`. Commit: `23587c0547439d8a47182355fdbbd44542f750a0` (session 20261110: Gather and engagement in batches (#2388), engagement of the 85 uncovered word bases ...).
Push output: `To https://github.com/lcilliers/Bible_Projects.git` / `3c2f1802..23587c05  main -> main`.
