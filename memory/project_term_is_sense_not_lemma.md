---
name: project_term_is_sense_not_lemma
description: "FOUNDATIONAL grain issue (2026-07-02): a 'term' in the lexical is a SPAN carrying a per-occurrence SENSE, NOT the bare lemma/Strong's. Term-driven rollup + 'related verses' + cross-ref mappings must be at the SENSE/span level, never the lemma. Rolling up a polysemous lemma (e.g. abad H5647 = worship/serve/enslave, 261 verses) wrongly aggregates unrelated senses."
metadata: 
  node_type: memory
  type: project
  originSessionId: bf6ef2d7-5b5c-4775-88f2-f2ca15223daa
---

**Researcher, 2026-07-02 — confirmed against data.** Builds on [[project_ve_lexical_is_verse_first]] / [[project_term_driven_genre_aware_lexical_method]].

**The unit is the SPAN (a sense), not the lemma.** Evidence: the 5 `abad` (H5647) occurrences in ruthlessness's passages are **enslave/serve** but all grounded to the **worship** sub-entry (H5647G, M36) — a grounding error; and the lemma H5647 has 261 verses across worship/minister/labour/enslave. So:
- **Term-driven rollup ("all the term's verses") must be by SENSE, not lemma.** abad-enslave ≠ abad-worship; never aggregate. Mono-sense lemmas (perek, radah) are fine; polysemous lemmas must roll up by sense.
- **"Related verses" = same-SENSE occurrences** (via the per-occurrence STEP subgloss / a sense index), not same-Strong's.
- **Cross-reference mappings (coupling/source/effect/target) must resolve to a SPAN (strong@verse) or SENSE, not the bare Strong's.** Current bug: perek's `operation`/`manner` use `strong@verse` (ok) but `coupling` uses bare `H5647` (lemma — loses sense).
- **Sense-grounding errors exist** (enslave filed under worship sub-entry) — OT-DBR-009 / sense-disambiguation family; fix before processing polysemous terms.

**RESOLVED 2026-07-02 — the grain index EXISTS: `wa_verse_term_links`** (227k rows, keyed to wa_verse_records; `step_subgloss_code` = the grain). Reader: `scripts/_produce_grain_index_v1_20260702.py` (`--strong` lists grains; `--grain` reads its verses; `--at+--strong` resolves an occurrence→grain). Rollup unit = the GRAIN; related verses = same grain (index lookup); cross-ref mappings = span (`strong@verse`) which resolves to a grain. perek H6531 = 1 grain (severity, 6v); abad H5647 = 4 grains (the enslave thread = `H5647G` "to serve", 88v — NOT the 261 lemma). **`mti_terms.owning_word` is NOT authoritative for sense** (mislabels H5647G as "worship"; the grain is "to serve"). Method §11 restated. Diagnostic: `Workflow/methodology/wa-term-is-sense-not-lemma-issue-20260702.md`.
