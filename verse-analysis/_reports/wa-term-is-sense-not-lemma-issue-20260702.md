# Fundamental grain issue — a "term" is a SENSE (span), not a lemma (2026-07-02)

**Raised by the researcher, confirmed against data.** Surfaced when picking the "next dominant term" after ruthlessness: `abad` (H5647) came up as most-frequent, but it is a 261-verse lemma spanning *worship / minister / labour / enslave* — and the enslavement in the ruthlessness passages is only one of its senses.

## The evidence
- The 5 `abad` occurrences in the ruthlessness passages (Exo 1:13,14; Lev 25:39,40,46) are **enslave/serve** (`work`, `slaves`, `make`, `serve`) — **all grounded to the WORSHIP sub-entry** `H5647G` (mti 1252, M36). *The enslave sense is filed under worship — a grounding error.*
- The lemma `H5647` has **261 verses / 4 sub-entries** (worship 88 · minister 142 · labour 30 · burden 2). Rolling up "the term H5647" pulls all 261 — **mostly worship**, not related to enslavement.
- The lexical's cross-references are at inconsistent levels: perek's `operation`/`manner` reference `H5647@Exo 1:13` (**span-level** — good); its `coupling` references bare `H5647` (**lemma-level** — loses the sense).

## The three-part issue (researcher's words, grounded)
1. **A term in the lexicals is a SPAN** — a specific word-occurrence carrying a per-occurrence **sense** — not the bare lemma/Strong's.
2. **"Related verses" is a SENSE set, not a lemma set** — the verses related to a span are the other **same-sense** occurrences, not every occurrence of the lemma. Rolling up by lemma over-collects (worship + enslave together).
3. **The mapping of a lexical to another span may be at the wrong level** — cross-references (coupling/source/effect/target) that key on the bare Strong's collapse the sense; a mapping should resolve to a **span** (strong@verse) or a **sense**, so "what it welds to / comes from" lands on the right occurrences.

## The right level (proposed direction — for researcher decision)
- **The owner/rollup unit = a SENSE (a lemma-sense), not a lemma.** `abad`-enslave and `abad`-worship are different terms for the study; never aggregated. Mono-sense lemmas (perek, radah) are unaffected; polysemous lemmas (abad, and likely fear/others) must roll up by sense.
- **Define "related verses" via the per-occurrence sense** (the STEP subgloss the study already holds), i.e. a **sense index**: group occurrences by their sense, not their Strong's.
- **Cross-reference mappings carry the span (strong@verse) consistently** (fix `coupling` to match `operation`/`manner`), and ideally a sense tag — so relatedness resolves at sense level.
- **Fix the sense-grounding** where a span is filed under the wrong sub-entry (enslave → worship). (This is the OT-DBR-009 / sense-disambiguation family.)

## Impact on the current method
- **"Pick the next dominant term" must be sense-level.** The `abad` that ruthlessness welds to is the **enslave sense**; its related-verse set is the enslave-sense occurrences — a tractable set, not the 261-verse worship lemma. (This is why `radah`, mono-sense, was the clean pick.)
- The **term-driven pipeline (§8) needs one qualification**: "all the term's verses" = all the **sense's** verses. For mono-sense terms this is unchanged; for polysemous lemmas it is the sense's occurrences only.
- **Ruthlessness's own lexical is unaffected** (perek is ~mono-sense); but its `coupling` mapping to `abad` should point at the **enslave sense/span**, not the worship lemma — otherwise following the map lands in worship.

## Status
Diagnostic only — no change made. Confirms a real grain error: the pipeline rolls up and maps by **lemma** where it must do so by **sense/span**. Decision needed on: (a) sense-level rollup unit + a sense index; (b) fixing cross-ref mappings to span/sense; (c) the enslave→worship grounding fix. These are prerequisites before processing polysemous terms like `abad`.

---

## RESOLUTION (2026-07-02) — the grain index exists: `wa_verse_term_links`
The sense/grain index is **`wa_verse_term_links`** (227,358 rows, keyed to `wa_verse_records`; each row = a term-in-verse + its STEP `step_subgloss_code`/`_label` = **the grain**). Reader: `scripts/_produce_grain_index_v1_20260702.py`.

**So the fix is direct — roll up / relate / map by GRAIN, not lemma:**
- **Grains confirmed:** perek H6531 = **1 grain** ("severity", 6v) → mono-grain, unchanged. abad H5647 = **4 grains** (to serve:minister 142 · to serve 88 · to serve:labour 29 · to serve:burden 2).
- **The enslave thread = the grain `H5647G` "to serve" (88v)** — read directly from the index — *not* the 261-verse lemma. (e.g. Gen 15:13 "serve them 400 years").
- **Correction to the earlier point:** the misleading label was the **mti `owning_word`** ("worship" for H5647G), NOT the grain — the grain (subgloss) is "to serve". So grounding uses the **grain code**, and the mti owning_word label is not authoritative for sense.
- **Rollup unit = the grain** (`step_subgloss_code`); **related verses = same grain** (index lookup); **cross-ref mappings = the span (strong@verse), which resolves to a grain** via the index (fix `coupling`'s bare-Strong's to `strong@verse`).

**Status:** grain issue RESOLVED at the index level — the term-driven rollup is now defined by grain. Ready to pick the next term/grain and process it grain-first.
