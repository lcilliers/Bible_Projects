---
name: feedback_structural_validation_is_not_value_quality_validation
description: "A validate step existing and passing (FK/notnull/enum/dedup) is not proof the underlying VALUES serve the app's purpose — check value quality separately, every time."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6c41e6ea-2028-48e2-8a88-a3b00af0e8f1
  modified: 2026-07-21T19:46:02.854Z
---

Treating "a validate step exists and reports clean" as "this data is trustworthy" is a category
error. Structural checks (row exists, FK resolves, not-null, dedup key holds, enum declared) prove
the shape is right; they say nothing about whether the actual VALUE in a column serves what it is
declared for.

**Why:** Surfaced 2026-07-21 in the IBA app (`iba/app/`). The researcher asked to assess
`candidate_seed` for a proper report and pointed out that `candidate.set`/`passage.build` had
already run on dirty seed data without anyone — including the assistant, reviewing the same
CONFIG-REPORT.md/GOVERNANCE.md moments earlier — registering that the process couldn't meet its
own objective. On audit, EVERY validate step in the app (`configmaint.validate`,
`candidate.validate`, `passage.validate`, `validation.py`) checked structure only; none checked
value quality. Concrete, previously-invisible defects found this way: two enums
(`candidate_decision`/`candidate_source`) declared in `cfg_column.expectation` but referenced by NO
code at all (silently unenforced); a genuine parser bug in `strong_sense.head` (228/3463 rows
contained an entire unsplit `<br>`-joined tree — the single most-read field in the app); dirty
labels in `candidate_seed.tag` (226/1732) and, upstream of that, `lemma_inventory.gloss`
(494/11421) — the gloss field also silently feeds a synonym-matching rule, so its dirt wasn't just
cosmetic. See `iba/docs/iba-candidate-seed-quality-findings-v1-20260721.md` and
[[project_iba_value_quality_engine_and_candidate_curate]].

**How to apply:** When asked "is X validated?" or when reviewing a report that says a validation
step passed, explicitly separate the question into two: (1) does a check exist, and (2) does that
check actually inspect the CONTENT of the values that matter, not just their shape/existence/FK
integrity. When auditing one table/column for this reason, audit the pattern across the whole
schema in the same pass — the same blind spot reliably repeats across every column carrying
human-authored or externally-sourced free text (glosses, labels, parsed HTML, registry names). Do
not stop at the first instance found; grep for literal enum/setting names actually being
referenced by code, not just declared in config — a declared constraint with no code path reading
it is exactly as unenforced as no declaration at all.
