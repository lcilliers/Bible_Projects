---
name: project_iba_value_quality_engine_and_candidate_curate
description: "IBA app now has a generic value-quality engine (lib/valuequality.py, cfg_column.expectation) and candidate.curate for correcting candidate_seed rows — built 2026-07-21."
metadata: 
  node_type: memory
  type: project
  originSessionId: 6c41e6ea-2028-48e2-8a88-a3b00af0e8f1
  modified: 2026-07-22T04:33:42.264Z
---

`iba/app/lib/valuequality.py` (new, 2026-07-21) is a generic engine reading
`cfg_column.expectation` to enforce real value-quality rules — three forms: `notblank`, `nohtml`,
`pattern:<cfg_setting key>`. This closes half of GOVERNANCE.md §6's previously-named-but-unbuilt
"V8" increment (the value-quality half; `source`-provenance enforcement is still open). Enum
violations (`enum.<name>` expectations) are checked separately, structurally, in
`handlers/configmaint.py` (`find_enum_violations`) — a hard coherence fault, not an escalation.

Registered: `candidate_seed.tag`, `lemma_inventory.gloss`, `word_registry.word`
(all `pattern:candidate.tag_clean_pattern`), `strong_sense.head` (`nohtml`), `span.surface`
(`notblank`), `span_candidate.candidate_tag` (`pattern:candidate.tag_clean_pattern`, unifying the
original hand-rolled check onto the generic engine), `strong_meaning_tree.sense_text`
(`pattern:raw.meaning_tree_clean_pattern` — see the whitelist/blacklist lesson below).
`candidate.validate` now scans
`span_candidate`+`candidate_seed`+`lemma_inventory` in one pass, one report
(`iba/app/reports/candidate-quality.md`). `validation.py` word/book reports gained a "6. Value
quality" section (same engine, scoped).

Also built: `candidate.curate` (new step, `candidate-curation` work package,
`Candidate-Curate.ps1`) — the ongoing single-row, approval-gated add/correct/remove utility for
`candidate_seed.tag`/`.decision` that `configmaint.propose` can't provide (it's restricted to
`cfg_*` tables only). Method doc:
`iba/docs/iba-candidate-seed-curation-method-v1-20260721.md`. Adding a brand-new candidate lemma
is still the existing `cfg_candidate_rule` accept/reject route via `configmaint.propose` (now
documented, previously wasn't).

Also fixed: a real parser bug in `handlers/raw.py:_split_def` — STEP's `mediumDef` sometimes uses
literal `<br>`/`<BR>` instead of `\n` as its tree separator (case-insensitivity was a second,
same-day miss), so the head/tree split silently failed at TWO levels: `strong_sense.head`
(228/3463 rows — the head/tree boundary itself) and, found in a same-day follow-up,
`strong_meaning_tree.sense_text` (1,383/3,178 lemmas — the tree's *internal* line separator, one
level deeper, never checked in the first pass). Both now 0 violations, repaired via one-off
`migration/repair_strong_sense_head.py` (re-derives the affected set live from the registered
checks, not a fixed list — safe to re-run if the bug shape recurs).

**Whitelist-vs-blacklist lesson:** the first attempt at the tree-text pattern whitelisted only
`<ref>` as an acceptable tag and flagged STEP's entirely legitimate `<b>`/`<i>`/`<greek>`/dynamic
cross-ref (`<H3389>`-shaped) prose formatting as violations (1,561 false positives). Fixed by
inverting to a **blacklist** (reject only `<br>`/`<BR>`, tolerate every other tag) — for any column
that legitimately carries rich, open-ended third-party markup, blacklist the known narrow defect
rather than whitelist every acceptable form; test the pattern against live data before registering
it, not just the handful of examples that prompted writing it.

**How to apply:** Before assuming any IBA data table's free-text column is clean, check
`cfg_column.expectation` for that column and run `lib.valuequality.find_value_quality_findings(cfg)`
— don't re-derive ad hoc regex checks. See
[[feedback_structural_validation_is_not_value_quality_validation]] for why this class of gap is
worth checking proactively, not just when asked.
