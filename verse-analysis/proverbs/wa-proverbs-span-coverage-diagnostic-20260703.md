# Proverbs Phase-1 span coverage — diagnostic (2026-07-03)

> Prompted by the researcher's check: *"ensure the span taken into account for a verse is ALL the span, not filtered because of narrowing — the lexicals seem light on span, especially qualifier types."* Read-only investigation of `_apply_poetic_chapter_lexical_v1` against the DB.

## 1. Core question — is the span set narrowed? **No.**
- `load_verse()` loads **every** span of a verse from `verse_span_index` (`WHERE reference=? ORDER BY word_index`) — no filter at load.
- The build loop skips a span from getting its own `ve_lexical` row in only **two** deliberate cases: **function-word POS** (particle, preposition, suffix, pronoun, adverb, conjunction) and **T2-tagged** terms (reference qualifiers, per `feedback_t2_reference_flag_reclassify`). Function words are still **used as context** (to find neighbouring verbs/prepositions) — they just don't become findings.
- **Measured coverage (Proverbs):** 6,918 total spans; **5,610 (94% of the 5,940 content spans: noun+verb+adjective) receive active `ve_lexical`.** The remainder = function words + T2. **Psalms is the same rate (93%).** → No undue narrowing; the reading sees all content span.
- **Morphology is intact:** 0/6,918 Proverbs spans lack a `morph_code`. The **backfill did not degrade morphology** — every span (including backfilled ones) carries full morph features. So qualifier derivation is not starved of input.

## 2. The intuition is partly right — qualifiers *are* lighter in Proverbs, but it tracks the genre, not a filter.
Qualifier density (per covered span), Proverbs vs Psalms:

| item | Proverbs | Psalms | why |
|---|---|---|---|
| manner / coupling | 8.2% | 11.9% | Proverbs is **less prepositional** (prep-segment density 16.5% vs 20.8%); manner requires a prep-marked noun near a verb |
| target (verb→object) | 0.55% | 1.8% | the `target` rule needs the **object-marker אֵת (HTo)**, which Proverbs almost never uses (0.3% of spans vs 0.8%) — terse poetry leaves objects unmarked |
| bearer | 4.7% | 21% | Proverbs has **little direct address / few proper nouns** (Psalms is full of "O LORD"); *this is genre-correct and beneficial* — far less bearer=LORD bleed to clean up |
| operation / seat / intensity | comparable | comparable | — |

These differences are **faithful to the text**: Proverbs' terse antithetical couplets carry fewer adverbial/prepositional phrases, fewer marked objects, and less apostrophe than the Psalms' flowing verse.

## 3. The one real limitation (shared by both books, largest un-captured category)
Proverbs' dominant qualifying structure is the **construct chain — "the X *of* the Y"** (mouth-of-the-righteous, fear-of-the-LORD, desire-of-the-righteous). **42% of Proverbs nouns are in construct state (1,440); 628 form an explicit X-of-Y chain** (construct noun + following noun). Psalms is similar (47%).

Today the construct relationship is captured as a qualifier **only in the narrow `seat` case** (206 spans — construct noun resolving to a heart/soul/spirit seat). The **general genitive "of" relationship is not tagged as a pair.** So a large class of qualifying relationships is present in the text and read naturally in the prose, but **under-represented in the lexical *pairs*.**

- **Impact on the readings: negligible.** The construct relationship is transparent in the English ("the mouth of the righteous is a fountain of life"), and the unit readings read it correctly. The gap is in the *machine-tagged pairs*, which matters only if/when we do pair-analysis at scale.
- **Not Proverbs-specific** — Psalms has the same construct density; it just shows up more starkly in Proverbs because the couplets are so noun-and-construct heavy.

## 4. Options (researcher decision — no change made yet)
1. **Leave as-is.** Coverage is complete; the lighter qualifiers are genre-faithful; the reading layer captures the construct relationships anyway. *(Lowest cost; the substrate is sound for the unit synthesis.)*
2. **Add a construct-chain qualifier** to `derive()`: when a construct-state noun is immediately followed by a noun, emit an `of`/`specifier` pair (Y specifies X). Would enrich the *pairs* for both books; a one-rule, reusable change, then a re-run. Also consider **positional object inference** (verb + following unmarked noun → `target`) to recover the objects that את omission hides.
3. **Hybrid:** add construct-chain + positional-object now (cheap, improves both books), re-run Phase-1, then continue the unit synthesis on the richer substrate.

**Recommendation:** **Option 3** — the construct chain is the single biggest un-captured qualifier class and a clean, reusable rule; doing it *before* scaling the unit synthesis means the read-back/validation runs against the richer substrate (and the same enhancement retro-improves the Psalter substrate). It's a ~1-rule change + a re-run, not a rebuild.

---
*Scripts: `_apply_poetic_chapter_lexical_v1` (build), `_inspect_unit_lexical_v1` (read-back). All figures measured live from the DB this date.*
