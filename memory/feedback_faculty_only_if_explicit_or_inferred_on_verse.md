---
name: feedback_faculty_only_if_explicit_or_inferred_on_verse
description: "GOVERNING (2026-06-26) — faculty appears on a verse ONLY if explicitly mentioned or inferred ON THE VERSE, never from the lemma; current 29,205 lemma-derived rows are invalid-by-method; rebuild verse-grounded"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ace57f3e-b52e-4cc7-adda-ef61148f91e0
---

GOVERNING RULE (researcher, 2026-06-26): **the `faculty` field appears on a verse only if it is explicitly mentioned or inferred ON THE VERSE — never derived from the lemma.**

**Why:** faculty must report what the verse *does*, not what the word *can* mean in the dictionary. A lemma-derived faculty carries zero verse-level information.

**State that triggered this:** diagnosis (`outputs/markdown/validation/wa-faculty-state-diagnosis-v1-20260626.md`) found `ve_lexical` ve_nr=7 is **100% per-term constant** — 993 terms, every one with an identical faculty-set across all its verses, 0 verse variation. All 29,205 rows came from `faculty-map-v1-20260624` + `v2_engine_iter1` (the lemma-map). So ALL stored faculty is **invalid by method**, not just the visible over-firing on the 8 seat lemmas (kardia → all 6, lev/levav/pneuma → 4 on every verse). 51% of units are also blank.

**How to apply:**
- Faculty has two admissible sources only: (1) **explicit** — a seat word (heart/mind/conscience/spirit/inward parts) or faculty-verb (know/think/remember/devise/choose/desire/discern/perceive) present in the verse; mechanical. The faculty may come from a *different* term in the verse than the one analysed (heart gets cognition/volition from the verb "devises", not from *lev*). (2) **inferred** — verse describes an operation implying a faculty without naming it; a reading, ceiling-bound.
- The lemma-map is **retired as a faculty source** — at most a candidate prompt ("seat term present, check the verse"), never the value.
- No signal → **no faculty** (empty is correct and expected).
- Rebuild = mechanism replacement, not tuning: scope explicit-vs-inferred-vs-empty, rebuild explicit mechanically (`faculty-verse-explicit`), decide inferred (mechanical best-effort vs depth-pass), soft-delete lemma rows (reversible via provenance).

Connects: [[project_faculty_not_gripped_audit_20260624]], [[feedback_faculty_must_be_per_term_not_per_cluster]], [[project_lexical_rules_reset_process_reframe]], [[feedback_transitive_faculty_verb_is_qualifier]], [[project_superstructure_eisegesis_validation_20260624]] (object-kind must cite a per-verse-VARYING field, never a lemma constant — same principle).
