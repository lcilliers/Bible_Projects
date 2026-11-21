# Session log 2026-11-21: the Programme book as the single source, and the follow-ups on #2506 to #2518

Session id: 19e3337e-aea1-4434-b72a-e90cdff0b1d6 (standard session; started 2026-11-20, closed 2026-11-21). Another session, 7063fa17 (Developer Mode), ran in the same folder and has its own log; the #2516 build is its work.

## 1. Scope

The researcher's aim for this session: one set of truth, the Programme book in bible_research.db, stating the current status of the project and holding all the descriptive prose from the 2510 work. Every 2510 document was read back into the Programme book and checked against an 89-item coverage list; the Observations Framework material was moved into the Programme book and the Detail design section was restored to its original; the researcher approved the Programme book (#2517). Follow-ups on #2516, #2518, #2515, #2509, #2508, #2507 and #2506 were carried out, and the three config proposals were approved ("Approve all three") and applied. Stages 4 and 5 and the other undefined items stay the researcher's decisions, stated in the Programme book under "what is not yet defined"; the Detail design book's earlier-method sections were not touched.

## 2. Escalations

- #2511, #2512, #2513, #2514: completed (v2 each).
- #2510: completed (v23); its open-item list raised as #2515.
- #2515: Q1 to Q7, Q21 to Q24 and Q27 closed, Q25 delivered, Q26 carried to #2516; completed at v24.
- #2516: raised, approved, built by the developer session, completed (v7).
- #2517: the Programme book as the one truth; completed at v16 on the researcher's "Approved".
- #2518: resolved (v2).
- #2509, #2508, #2507: closed (v9, v5, v18); the anomaly list and rulings carried on #2463 (v40).
- #2506: completed (v7) after the three config proposals were applied.
- #2519, #2521, #2522: the config proposals, approved and applied (v4 each). #2520 withdrawn (v2), replaced by #2522.
- #2463, #2448, #2486, #2376, #2377: superseded (v41, v18, v18, v8, v3) by #2526, #2528, #2529 and #2530 on the researcher's instruction.
- #2526 (collection reading, stages 1 to 3), #2527 (pick-up point and stage ends), #2528 (stage 4), #2529 (the narrative), #2530 (stage 5): raised and updated; #2527 awaits the researcher.

## 3. Files

- Programme book export: Workflow/Programme/programme_prose/wa-programme-prose-extract-20261120.md and .json.
- Prose patches in archive/patches/: wa-prose-programme-status-20261120T180000Z.json, wa-prose-programme-types-20261120T180100Z.json, wa-prose-framework-into-programme-20261120T190000Z.json, wa-prose-detail-design-restore-20261120T190100Z.json, and the wa-prose-author and wa-prose-chapter-supersede patches of 2026-11-20.
- Edit files in Workflow/Programme/prose-edits/ and its archive/: the programme and detail-design chapter edits of 2026-11-20.
- Worksheet: the VerseLexical tab of iba/docs/ps tools worksheet.xlsx (stale columns and retired rows removed).
- Reports: outputs/configs/CONFIG-REPORT.md; the escalation histories of the items above under outputs/escalation/.
- Compliance file: Logs/compliance/COMPLIANCE-20261120-19e3337e.md.
- Later in the session: outputs/escalation/2463-open-items-aligned-to-the-programme-v1-20261121.md, outputs/escalation/2527-where-the-programme-is-picked-up-and-the-stage-end-v2-20261121.md, outputs/escalation/2526-stages-1-to-4-readiness-audit-v1-20261121.md, outputs/escalation/2528-stage-4-and-alignment-build-brief-v1-20261121.md; the prose patch archive/patches/wa-prose-stage4-required-20261121T070000Z.json and the export Workflow/Programme/programme_prose/wa-programme-prose-extract-20261121.md.

## 4. Decisions

- Researcher: the Programme book alone is the one set of truth; the Detail design book is out of scope for the 2510 descriptive prose. Recorded at #2517 v14.
- Researcher: "Approved" for the Programme book. Recorded at #2517 v16.
- Researcher: #2516 approved for follow-up; #2518, #2515, #2509, #2508 resolved or closed; #2506 sorted. Recorded at #2515 v24, #2516 v4, #2506 v5.
- Researcher: "Approve all three" (#2519, #2521, #2522). Recorded at #2519 v3, #2521 v3, #2522 v3.
- Claude, self-correctable: Detail design section 128 restored from the change log after the framework was put there by mistake. Recorded in archive/patches/wa-prose-detail-design-restore-20261120T190100Z.json.
- Claude, self-correctable: #2520 withdrawn and re-proposed as #2522 so the wording does not name a closing item. Recorded at #2520 v2.
- Claude, self-correctable: the worksheet drift fixed. Recorded at #2506 v5.
- Researcher: the five old items are superseded by steps aligned to the Programme book. Recorded at #2526 v1, #2527 v1, #2528 v1, #2529 v1 and the five supersede versions.
- Researcher: stage 4 is to be fully specified and built, and the Programme book says so. Recorded at #2527 v7 and archive/patches/wa-prose-stage4-required-20261121T070000Z.json.
- Researcher: prepare for a developer-mode session to build stage 4. Recorded at #2528 v5 and outputs/escalation/2528-stage-4-and-alignment-build-brief-v1-20261121.md.

## 5. Open items

- #2526: collection reading, stages 1 to 3, assigned to Claude, waiting on the developer-mode build of #2528.
- #2528: the build of stage 4 and the alignment of stages 1 to 3, assigned to Claude, needs a fresh /developer-mode session.
- #2527: pick-up point and stage ends, with the researcher for approval.

## 6. Git

Branch: main

First commit: 6d5bff43, "session 20261121: Programme book as single source (#2517), follow-ups #2506-#2518, config #2519/#2521/#2522 applied, role alignment (#2524, #2525), session-close project-map check (#2516), session log, compliance".

Push: `To https://github.com/lcilliers/Bible_Projects.git   99da595f..6d5bff43  main -> main`.

Not committed by rule: database/bible_research.db (the Programme book lives there) and backups/.
