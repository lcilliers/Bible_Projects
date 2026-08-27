---
name: project_column_wise_ve_hypothesis
description: HYPOTHESIS under active development (le Roux, 2026-06-11) — reorganise the verse-read from ROW-WISE (read a verse, answer all 14 VE dimensions + meaning, per verse; ~1 day/cluster, ~40 days left, errors on every review) to COLUMN-WISE (answer each ISOLABLE VE question across the WHOLE corpus as one focused pass; one stable rubric). Three lanes: A mechanical/term-level (no read, scripted), B sense-application spine (one read pass), C interdependent cause/effect/relationship core (stays grouped). GUARDRAIL: never column-split the interdependent core (would re-read each verse N times). Workflow change, not schema.
metadata:
  type: project
---

**The hypothesis.** Row-wise verse-complete reading re-derives 14 rubrics ~31,000 times → structural drift
(the "errors and omissions on every review") and slow (~1 day/cluster, ~40 days outstanding). Doing each
ISOLABLE VE question across the whole corpus as a single pass drives CONSISTENCY (one rubric held stable;
review becomes tractable — inspect one dimension across the corpus, would have caught the boulomai=cognition /
ya.re god-heuristic induces in one place) and cuts TIME (mechanical dimensions leave the metered read entirely).

**Three lanes (proposed, validate vs catalogue):**
- **A — mechanical / term-level, NO verse read:** sense-RANGE, faculty (per-term from lexical meaning,
  [[feedback_faculty_must_be_per_term_not_per_cluster]]), type, constitutional-location, literary-setting,
  compound. Scripted corpus passes; never hit the API.
- **B — sense-application spine:** VE-01 sense APPLIED here (+ meaning anchor). One corpus-wide read pass, one
  question. The spine everything downstream keys off.
- **C — interdependent core:** origin, mode, immediate-response, produces-effect, relational-implication,
  purpose, typology = the cause/effect/relationship DYNAMICS ([[project_verse_extraction_cause_side_gap]], the
  weakest data). Stays ONE grouped per-verse read against the fixed sense+meaning.

A+B cover ~9-10 of 14 ("most in isolation"); C is the irreducible holistic read, now smaller and aimed where
it's needed.

**Guardrail:** do NOT split the interdependent core into separate column-passes — each would re-read every
verse, multiplying reads. Column-wise applies to ISOLABLE dimensions only.

**Deeper reason it matters:** it is the mechanism that breaks the 4-month variation circle —
[[project_meaning_duplicates_then_fabricates]] (separates disciplined extraction from generative prose).
Engine CANNOT currently time dimensions-vs-meaning separately (fused in one model call; meaning ~60% of
generation) — decomposing gives per-phase timing for free.

**Status:** diagnosis + direction, NOT built. Next: prototype the faculty corpus-pass (term-level, already
burned us) and measure consistency+time vs a verse-complete slice. Working note:
research/investigations/wa-column-wise-ve-hypothesis-v1-20260611.md.
