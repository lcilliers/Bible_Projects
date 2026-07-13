# Proverbs passage method — the large passages are BUNDLES, not focused reading units (v1, 2026-07-13)

> Test of the researcher hypothesis: *the large v2 passages are a bundle of verses, not a proper passage focused on the underlying candidate chars.* **Confirmed.** The v2 rule (maximal run of consecutive candidate verses) is right for **discourses** but wrong for Proverbs' **sentence-collections**, where every verse is an independent proverb. Read-only analysis; recommends **revisiting the passage-build method for Proverbs** before Stage 4.

## The test — segment_units spanned per large passage

A coherent reading unit ≈ one discourse unit (`segment_unit`). A bundle spans many. Of the **54 passages >4 verses**:

| verdict | passages |
|---|--:|
| **BUNDLE** (>2 segment_units mashed together) | **48** |
| ~coherent (≤2 segments) | 6 |

The largest passages each swallow 8–16 discourse units:

| passage | verses | candidate chars | segment_units spanned |
|---|--:|--:|--:|
| Pro 14:1-35 | 35 | 129 | 14 |
| Pro 15:1-33 | 33 | 113 | 16 |
| Pro 11:1-31 | 31 | 101 | 13 |
| Pro 21:1-31 | 31 | 98 | 12 |
| Pro 10:1-25 | 25 | 82 | 13 |
| Pro 12:1-28 | 28 | 97 | 12 |

## The inspection — Pro 14:1-35 (one "passage")

It is **the whole of chapter 14 — 35 self-contained proverbs**, e.g.:
- 14:1 "The wisest of women builds her house…" (wisdom/folly)
- 14:2 "Whoever walks in uprightness fears the Lord…" (fear of God)
- 14:3 "By the mouth of a fool comes a rod…" (speech/folly)
- 14:5 "A faithful witness does not lie…" (truth/deceit)
- 14:17 "A man of quick temper acts foolishly…" (anger)
- 14:30 "A tranquil heart gives life… envy makes the bones rot" (peace/envy)

These are **different characteristics in unrelated sayings**. The candidate char in 14:2 is not supported by, and does not develop across, the 34 other verses. Chapter 14 already carries **13 thematic `segment_unit`s** (PRO-14-temper, -fear, -heart-known, -self-deception, -generosity, -simple…) — the finer units the v2 run overrode.

## Diagnosis

**Maximal-consecutive-candidate-run is genre-blind.** It works where consecutive verses develop one movement (the Prov 1–9 instruction discourses; poetic laments in Psalms), but in the **sentence-collections (Prov 10–29)** every verse is an independent proverb, so a maximal run = the whole chapter = a bundle. This is exactly the digestion analysis's earlier point (`wa-proverbs-segment-vs-candidate-digestion-analysis-20260708.md`): *keep the §15 segments; do not switch to candidate passages.* The v2 build has now confirmed it on the data.

## Options to revisit the method (researcher decision)

1. **Segment-bounded runs (recommended).** A passage = a maximal candidate run **that never crosses a `segment_unit` boundary** — i.e. intersect the run with the §15 segmentation. Discourses stay whole; sentence-collections split into their thematic segments (temper, fear, generosity…) or single proverbs. Uses the existing `segment_unit` structure; keeps the passage layer but makes it coherent.
2. **`segment_unit` IS the passage** for Proverbs. Set `verse.passage_id` from the thematic segment each verse belongs to (the finest, most-specific unit, not the chapter-wide `F` container). Fully adopts the §15 model the digestion analysis recommended.
3. **Per-proverb for the collections.** In Prov 10–29, each candidate verse (or couplet) is its own single-verse passage; keep maximal runs only in the discourse sections (Prov 1–9, 31). Simplest, matches "each proverb stands alone".

**Recommendation: option 1 or 2** — both make the passage a coherent focus on the candidate char in its real context, and both lean on the `segment_unit` layer that already exists (323 units, median 2 verses). Note the `segment_unit` has a chapter-wide **F container** plus nested thematic **S/T** units — the reading unit should be the **thematic sub-unit**, not the F.

## Status

The v2 passage build (104 passages, `passage-build-2026`) is **applied but should be reconsidered** before the read — do not read the F-frame bundles as-is. Snapshot before the v2 build: `backups/bible_research_pre-passagebuild-v2_*.db`. The readiness gate (I4) is satisfied by any coherent passage layer; the method choice is a genre/structure decision, not an integrity one.

*Filed 2026-07-13. Read-only. Blocks Stage 4 read until the passage method is confirmed.*
