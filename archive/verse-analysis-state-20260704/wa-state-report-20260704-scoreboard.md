# Verse-analysis — STATE REPORT (live from DB, 2026-07-04)

> Queried directly from `database/bible_research.db`. Point-in-time snapshot of the verse-analysis (inner-being lexical) programme. All figures are active rows (`delete_flagged=0`).

## 1. Phase-2 chapter readings — `prose_section` type `lexical_prose_chapter`
The published, verse-grounded inner-being readings. One `prose_section` per book+chapter.

| Book | Chapters | Versions | prose_section ids | Words |
|---|---|---|---|---|
| Psalms | 150 | v1–v2 | 430–579 | 123,772 |
| Proverbs | 31 | v1 | 582–612 | 19,765 |
| Ecclesiastes | 12 | v1 | 624–635 | 20,693 |
| Job | 42 | v1 | 636–677 | 49,990 |
| Lamentations | 5 | v1 | 678–682 | 9,293 |
| **TOTAL** | **240** | — | — | **223,513** |

*(Psalms carry v2 where the re-alignment sweep re-filed them; all others v1.)*

## 2. Segmentation units — `segment_unit` (discourse-shaped books)
The inner-being units driving Phase-2 for the non-lyric wisdom books. `multi` = units where several characteristics operate together.

| Book | Units | Chapters | multi | Type mix |
|---|---|---|---|---|
| Proverbs | 150 | 31 | 93 | S:79 · D:34 · T:31 · F:6 |
| Ecclesiastes | 47 | 12 | 43 | D:39 · T:5 · C:1 · F:1 · S:1 |
| Job | 101 | 42 | 96 | D:101 |
| Lamentations | 16 | 5 | 16 | D:16 |
| **TOTAL** | **314** | **90** | **248** | — |

*(Psalms use the chapter-driven method — no segmentation layer; the chapter is the unit.)*
*Types: D discourse · S single-saying · C cluster · T thread (recurring) · F frame/arena.*

## 3. Verse layer + Phase-1 lexical substrate
100% chapter completeness (STEP-backfilled) and 100% Phase-1 lexical coverage across all five books.

| Book | Verses (DB / canonical) | Chapters | Phase-1 marked | ve_lexical rows |
|---|---|---|---|---|
| Psalms | 2,461 / 2,461 | 150 | 2,461 | 69,064 |
| Proverbs | 915 / 915 | 31 | 915 | 23,320 |
| Ecclesiastes | 222 / 222 | 12 | 222 | 8,824 |
| Job | 1,070 / 1,070 | 42 | 1,070 | 23,623 |
| Lamentations | 154 / 154 | 5 | 154 | 5,484 |
| **TOTAL** | **4,822 / 4,822** | **240** | **4,822** | **130,315** |

*ve_lexical source_provenance = `lexical-model-2026` (131,322 rows programme-wide).*

## 4. Synthesis + discovery layer (other prose_section types)
| Type | Sections | Words | Note |
|---|---|---|---|
| `lexical_prose_chapter` | 240 | 223,513 | the readings (§1) |
| `ib_characteristic_discovery` | 10 | 11,240 | fork-b discovery docs (10 of ~29) |
| `lexical_synthesis_psalter_essay` | 2 | 5,275 | Psalms→two-book essay |
| `lexical_synthesis_psalter` | 1 | 3,207 | per-characteristic Psalter synthesis v1 |
| `lexical_prose` | 1 | 402 | per-term endpoint sample |

## 5. Characteristic baseline (coverage-validation index, not analytical object)
- **`characteristic` table:** 277 active across 35 clusters — of which **78 PROVISIONAL** (the 2026-07-03 top-down extension, held as validation exemplars only, to be verified verse-by-verse; governed by the validation-not-imputation guardrail).
- **`ib_characteristic` registry:** 29 items (bottom-up movement-level discovery layer).

## 6. Integrity
- Phase-1 **blocked / review** markers across the 5 wisdom books: **0**
- Wisdom-book verses with **no** Phase-1 marker: **0**
- Reproducibility: `prose_section.body` == the filed `.md` (spot-checked byte-for-byte at session end 2026-07-03).

## Headline
The **wisdom/poetry corpus is complete** — Psalms + Proverbs + Ecclesiastes + Job + Lamentations: **240 chapter readings / 223,513 words**, on a substrate of **130,315 Phase-1 lexical items** over **4,822 verses (100% backfilled + marked)**, with **314 segmentation units** for the discourse-shaped books. Next tranche (not started): well-covered prophets (Isaiah/Hosea/the Twelve) + Pauline epistles; Song of Songs held.
