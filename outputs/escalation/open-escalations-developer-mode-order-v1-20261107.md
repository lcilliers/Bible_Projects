# Open escalations: order of fixes for Developer Mode (2026-11-07)

Source: `escalation` table, latest version of each item, read live today (8 open, 3 parked).
Boundary used: cfg_behaviour_rule 97 (developer-mode-scope-and-conduct). Developer Mode removes only the
`configmaint.propose` per-row approval gate. Reporting, exploring data and prototyping are standard-mode work.
Statements marked inferential are my reading, not recorded fact (B:4).

## Recommended order

| Order | Item | What it needs | Needs Developer Mode? | Blocked on |
|---|---|---|---|---|
| 1 | #2378 Propose usage: -Title required, guide example lacked it | Researcher accepts a fix already made (iba/app/USER-GUIDE.md line 307) | No | Your approval only |
| 2 | #2363 ib_observation note names 1 of 6 writers | Choice (a) update cfg_table.use of ib_observation through the Propose gate, or (b) retire the stale check iba/app/tools/temp_2231_2232_test_run.py | (a) yes, a config row change the gate would otherwise hold; (b) no | Your choice of a or b |
| 3 | #2381 Fix affix and shared-span surfaces in verse_lexical (with #2380 analysis) | Design the fix, then build it in iba/app/lib/lexical.py plus a rebuild of verse_lexical data | Code change: no. Any cfg row it needs: yes | #2380: your choice among options A to D (B:105: design first, no building before it) |
| 4 | #2372 Surface group: prompt says entity, data says being | Establish two facts read-only (where the answer check reads allowed values; whether the 716 loaded rows were judged on an earlier prompt version), then option A (rename in prompt group.word v3) or B (rename enum value and 716 rows) | A: yes (cfg_ai_prompt row). B: yes, plus a data change | Your choice of A or B; best settled before the next group judge run |
| 5 | #2366 Port judge work-period cycle to group.judge | Build the unattended cycle for group.judge; retire the Surface-Judge.ps1 file route and setting surface_judge.word_prompt | Setting deletion: yes | A design question (where the cycle lives for all AI steps) goes to you first |
| 6 | #2357 cfg_* advisory findings | Acknowledge or reject advisory findings: orphan configs, 3 low-config-density utilities, 1 hand-rolled -v{n} filename, 1 PS worksheet drift, 17 behaviour rules with no control | Fixes to config rows: yes | Your judgement per finding (its options file was not re-read in this pass) |

## Why this order (inferential)

- #2378 and #2363 are small and each ends at one decision from you. Clearing them first removes standing approvals.
- #2381 is the heaviest and affects analysis most (your words: it "fundamentally affects analysis"). Recorded in #2380: 128002 of 140144 H9/G9 rows carry another code's word; 3526 of 6066 surface terms touch an H9 row. It follows your choice at #2380 and, by B:105, a design that returns to you before any build.
- #2372 and #2366 both change the group-judging step. My reading is that surface-cycle results are suspect until #2381 is fixed, so re-running group judging should wait. The cheap #2372 prompt/enum correction can still be settled earlier. Whether the loaded rows are in fact affected is not established.
- #2357 is advisory, has no dependency on the rest, and is the least urgent.

## Not Developer Mode work

- #2379 (assigned to Claude): exploring and analysing the surface results. Standard-mode work under rule 97. Its findings fed #2380; further outputs read better after #2381.
- #2376 Rebuild narrative and #2377 Assemble narration chapter scope: waiting for your scope and work packages. Nothing to build.
- #2368 Rules for whole-cluster reading will change: parked until you state the new rules.

## Decisions needed from you

1. #2378: accept the fix (yes/no).
2. #2363: (a) update the note or (b) retire the stale check.
3. #2380: which of A filter at the consumer, B mark the kind of surface at the source, C blank or own-gloss for affix codes, D extend the #2326 rule. Recorded recommendation: B with A as the interim guard (inferential).
4. #2372: A or B.
