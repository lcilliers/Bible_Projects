# Session log 2026-11-20: #2510 programme prose rewritten, open questions listed

Session id: 034d191d-65eb-4489-b8f0-6de0a86bf7d3 (started 2026-11-19, closed 2026-11-20).

## 1. Scope

The session ran the start routine, took up the researcher's review of the three #2510 documents (history, gap list, stage 3 draft), corrected them, answered the researcher's questions on the comment column, the surface groups, the unit of study, batching and fallout from the database and the record, and on the researcher's change of strategy of 2026-11-20 rewrote the programme prose in `bible_research.db`, listed Claude's open questions in one document, and closed the session without answering them.

## 2. Escalations

- #2510 (Update the programme prose to the project as built): updated v18 to v22; the researcher's review of 2026-11-19 and the messages of 2026-11-20 are recorded verbatim at v18, v20 and v22; still in-progress with Claude.
- #2448, #2463, #2507, #2508, #2509: read, not changed; their records feed the open-questions list. #2486 and #2506 not touched.

## 3. Files

- Programme prose in `bible_research.db` (not committed, a database): the preamble, chapters 1 to 6 of the programme book, the Observations Framework section (book Detail design), two glossary entries (claim, engagement); all draft. Applied through `Prose.ps1` from patches under `archive/patches/` (`wa-prose-chapter-supersede-20261120T0606*.json`, `...T0609*.json`, `wa-prose-heading-author-20261120T061024Z.json`, `wa-prose-preamble-20261120T061110Z.json`, `wa-prose-trim-20261120T061137Z.json`, `glossary-2510-20261120.json`); the edit files are archived under `Workflow/Programme/prose-edits/archive/`.
- `outputs/escalation/2510-escalation-history-v2-20261119.md`, `2510-programme-prose-gap-list-v2-20261119.md`, `2510-stage3-verse-lexical-observations-draft-v3-20261120.md`, `2510-stages-unit-surface-group-batching-fallout-v1-20261120.md`, `2510-open-questions-v1-20261120.md` created; `2510-work-index-v1-20261119.md` and `2510-stage4-ib-observations-draft-v1-20261119.md` updated for the new names; the v1 history, gap list and stage 3 draft and the v2 stage 3 draft archived under `outputs/escalation/archive/`.
- `Logs/compliance/COMPLIANCE-20261119-034d191d.md`, this log.
- No code, configuration or schema changed.

## 4. Decisions

- Researcher: the review of the three documents (science reading is part of the claims reading; Claude interprets the evidence with trackable backing; stage 3 closure is a gate for the collection; the prose is an authoritative record for an external reader; no new labels), recorded at #2510 v18.
- Researcher: change of strategy of 2026-11-20 (update the prose, make one list of open questions, close the session without answering them; the study proceeds through stages 3 and 4 with the questions woven in), recorded at #2510 v22 and in `outputs/escalation/2510-open-questions-v1-20261120.md`.
- Claude, self-correctable: the author of the sections rewritten through the import round trip was reset from researcher to claude_code, and headings of the old Session A to D slots were changed to the study's labels, recorded in `archive/patches/wa-prose-heading-author-20261120T061024Z.json`; two retired-method sentences removed, recorded in `archive/patches/wa-prose-trim-20261120T061137Z.json`.

## 5. Open items

For the researcher, to be woven into stages 3 and 4: the 27 questions of `outputs/escalation/2510-open-questions-v1-20261120.md`, carried on #2510; approval or correction of the draft prose sections (#2510). Held with their own records: #2448, #2463, #2486, #2506, #2507, #2508, #2509. Not built: the `cfg_prose_concept` pointers (question 22) and the session-close check that keeps the project map current (question 26), both carried on #2510.

## 6. Git

_(written after the first commit)_
