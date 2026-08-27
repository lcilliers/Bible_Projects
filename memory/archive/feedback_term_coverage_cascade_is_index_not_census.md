---
name: feedback_term_coverage_cascade_is_index_not_census
description: registry→terms→related-terms cascade is an INDEX over the corpus, not a census; STEP relatedNos is shallow/leaky; coverage has structural blind spots; verse-fanout is a better substrate but not an automatic guarantor
metadata:
  type: feedback
---

The term-coverage method = **registry English word → STEP primary Strong's → STEP `relatedNos` related terms.** Validated 2026-06-28 (perek/cruelty miss): this cascade is an **expansion tool / index, NOT a census** of IB-relevant terms.

**Why it leaks (evidenced):** (1) **No English seed = invisible concept** — the ~215 registry words are the entry gate; cruelty had no seed, so its sub-field was unreachable. (2) **STEP `relatedNos` is shallow and sometimes morphological, not semantic** — `perek`'s only STEP relation is the homonym `paroketh` "curtain"; rare words are near-orphans. (3) **Contextual capture** — `arits` (a cruelty word) was pulled under *dread*, and its relations point back to dread, so it never seeds cruelty. Result: **term coverage = closure of a human-curated English list under a leaky association graph** — strictly smaller than "all IB-relevant terms." Blind spots are **structural, not accidental.** A span-orphan audit (corpus base-Strong's never seen by mti/inventory/related-words) found **~45 IB-relevant orphans** incl. `miseo` G3404 "to hate" — orphaned **even though M06 Hate exists** (the cascade leaks *within* seeded concepts too).

**How to apply:**
- Treat the registry as a **seed list, not a coverage boundary.** "Not in the registry" ≠ "not IB-relevant." Expect gaps from various routes over the study's life.
- Do **not** rely on STEP `relatedNos` to deepen a concept's field (too shallow/leaky) — deepen via the verse-fanout + multi-contributor spiderweb ([[project_multi_contributor_spiderweb]]).
- The **verse-fanout is a better substrate** (every term that occurs is present at the verse) **but NOT an automatic guarantor** — catching `perek` was a *human* catch. The mechanical safeguard is a **periodic span-orphan coverage audit** on the span-verse-lexical index (`verse_span_index`), filtered by IB-semantic surface forms.
- **Irreducible weakness:** an IB phenomenon may **never be lexicalised in any verse** — no method catches that. Mitigation = an **open mind**: hold that operations of the inner being may exist that the study does not represent. Do not treat "absent from the corpus" as "does not exist."

Master record: `research/investigations/wa-term-coverage-method-integrity.md`. Triggering case: [[feedback_verse_raw_data_must_pull_all_study_evidence]] / the ruthlessness investigation. Relates to [[feedback_term_corpus_anchors_meaning]], [[project_verse_fanout_operating_model]].
