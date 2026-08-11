# Word → Strong's → old-project cluster mapping — 2026-08-10

**One-off report.** Answers: for every Strong's number attached to an IBA word (`word_strong`), what M-code
cluster did the old project (`database/bible_research.db`) allocate that Strong's to?

## Source tables

- **New (IBA):** `iba/app/db/iba.db` — `word_registry` (178 active words) ⋈ `word_strong` (4,848 active
  word↔Strong's rows).
- **Old:** `database/bible_research.db` — `mti_terms.cluster_code` (the field CLAUDE.md §3 identifies as
  the strongs→cluster allocation) ⋈ `cluster.short_name` for the M-code's display name.

## Method

```sql
ATTACH DATABASE 'database/bible_research.db' AS old;

SELECT wr.word, ws.strong, mt.cluster_code, c.short_name
FROM word_strong ws
JOIN word_registry wr ON wr.id = ws.word_id
LEFT JOIN old.mti_terms mt ON mt.strongs_number = ws.strong
LEFT JOIN old.cluster   c  ON c.cluster_code   = mt.cluster_code
WHERE ws.deleted = 0 AND wr.deleted = 0;
```

Strong's number format matches directly between the two DBs (zero-padded 4-digit, `H`/`G` prefix — e.g.
`G0074`), confirmed by sampling both tables before joining.

## Caveat — old DB has no unique key on `strongs_number`

`mti_terms` has **7,861 rows for a set of Strong's numbers with 1,782 duplicate groups** (this is the
known, unresolved **OT-DBR-009** dedup issue — a Strong's can own more than one `mti_terms` row, typically
one per owning English word/registry in the old project). Of those duplicate groups, **167 strongs_number
values carry conflicting `cluster_code` values** across their duplicate rows (e.g. `G0019` → `M39` in one
row, `M46` in another).

**Resolution used here:** rather than arbitrarily picking one old row per Strong's, every distinct non-null
`cluster_code` found for a given Strong's is kept and unioned. This is a factual aggregation, not a
judgement call — it means a handful of individual Strong's numbers legitimately show up tagged to more
than one M-code below.

## Coverage

| | count | % |
|---|---|---|
| Active `word_strong` rows (178 words) | 4,848 | 100% |
| — matched to ≥1 old `cluster_code` | 2,995 | 61.8% |
| — no old `cluster_code` (old row absent, or present but never clustered) | 1,853 | 38.2% |

Context: only 4,697 of the old DB's 7,861 `mti_terms` rows (59.8%) carry a `cluster_code` at all — most of
the unmatched 38.2% is the old project simply never having reached that term, not a join failure.

**Word-level:** across all 178 words, **every word has at least one Strong's that lands in an old cluster**
(0 words are wholly unmatched). But only **7 of 178 words** have *all* their matched Strong's converge on a
single M-code; the other **171 words spread across multiple old clusters** — expected, since the old
project's `cluster_code` was assigned per-Strong's-number (per owning term), not per English word, and a
single IBA English word typically aggregates dozens of Strong's numbers that the old project's finer-grained
term-level process routed differently.

## Results — per word: dominant old cluster + full spread

`n` = active Strong's for the word · `matched` = how many of those had a `cluster_code` in the old DB ·
**Dominant** = the old cluster the largest share of the word's matched Strong's fall into · **# clusters** =
distinct old clusters touched · **Full spread** = every cluster touched with its Strong's count, ranked.

| Word | n | matched | Dominant cluster | Dominant share | # clusters | Full spread |
|---|---:|---:|---|---|---:|---|
| abomination | 17 | 11 | M10 (Sin) | 4/17 (23.5%) | 4 | M10(Sin)=4; M06(Hate)=4; M27(Evil)=2; M02(Anger)=1 |
| agony | 11 | 10 | M03 (Grief) | 5/11 (45.5%) | 5 | M03(Grief)=5; M24(Weakness)=2; M34(Perseverance)=1; T2(Supplementary)=1; M01(Fear)=1 |
| ambition | 2 | 2 | M28 (Envy) | 1/2 (50.0%) | 2 | M28(Envy)=1; M18(Hope)=1 |
| anger | 39 | 26 | M02 (Anger) | 19/39 (48.7%) | 6 | M02(Anger)=19; T2(Supplementary)=5; FLAG(Flag)=1; M06(Hate)=1; M30(Obedience)=1; M44(Relational)=1 |
| anguish | 36 | 27 | M03 (Grief) | 19/36 (52.8%) | 6 | M03(Grief)=19; M01(Fear)=5; M24(Weakness)=4; T2(Supplementary)=2; M34(Perseverance)=1; M44(Relational)=1 |
| anointing | 21 | 19 | T2 (Supplementary) | 16/21 (76.2%) | 3 | T2(Supplementary)=16; M12(Purity)=2; M46(Abundance)=1 |
| anxiety | 12 | 9 | M33 (Peace) | 2/12 (16.7%) | 5 | M33(Peace)=2; M18(Hope)=2; M20(Doubt)=2; M01(Fear)=2; T2(Supplementary)=1 |
| appetite | 9 | 3 | M25 (Life) | 1/9 (11.1%) | 3 | M25(Life)=1; M47(Constitution)=1; T2(Supplementary)=1 |
| authority | 38 | 36 | M23 (Strength) | 23/38 (60.5%) | 7 | M23(Strength)=23; T2(Supplementary)=13; M17(Counsel)=1; FLAG(Flag)=1; M09(Humility)=1; M22(Praise)=1; M08(Pride)=1 |
| awe | 19 | 14 | M01 (Fear) | 11/19 (57.9%) | 3 | M01(Fear)=11; M21(Prayer)=2; M04(Joy)=1 |
| being | 444 | 152 | T2 (Supplementary) | 27/444 (6.1%) | 37 | T2(Supplementary)=27; M24(Weakness)=13; M23(Strength)=9; M08(Pride)=7; M33(Peace)=7; M01(Fear)=6; M20(Doubt)=6; M04(Joy)=6; M16(Folly)=6; M02(Anger)=6; M15(Wisdom)=5; M07(Shame)=5; M19(Trust)=5; M29(Desire)=5; M03(Grief)=4; M39(Blessing)=4; M14(Deceit)=3; M09(Humility)=3; M05(Love)=3; M13(Truth)=2; M34(Perseverance)=2; M46(Abundance)=2; M42(Speech)=2; M26(Righteousness)=2; M30(Obedience)=2; M10(Sin)=2; M25(Life)=2; M27(Evil)=2; M36(Service)=1; M31(Faith)=1; M41(Remembrance)=1; M21(Prayer)=1; M47(Constitution)=1; M06(Hate)=1; M12(Purity)=1; M11(Repentance)=1; FLAG(Flag)=1 |
| bitterness | 22 | 13 | M03 (Grief) | 8/22 (36.4%) | 6 | M03(Grief)=8; M02(Anger)=2; M30(Obedience)=2; M28(Envy)=1; T2(Supplementary)=1; M24(Weakness)=1 |
| blessing | 20 | 10 | M39 (Blessing) | 6/20 (30.0%) | 3 | M39(Blessing)=6; M22(Praise)=3; M04(Joy)=1 |
| boastfulness | 31 | 15 | M08 (Pride) | 9/31 (29.0%) | 6 | M08(Pride)=9; M22(Praise)=2; M16(Folly)=2; M34(Perseverance)=1; T2(Supplementary)=1; M23(Strength)=1 |
| boldness | 14 | 12 | M34 (Perseverance) | 3/14 (21.4%) | 7 | M34(Perseverance)=3; M23(Strength)=3; T2(Supplementary)=2; M08(Pride)=2; M04(Joy)=1; M21(Prayer)=1; M19(Trust)=1 |
| bondage | 13 | 9 | M36 (Service) | 8/13 (61.5%) | 2 | M36(Service)=8; M30(Obedience)=1 |
| brokenness | 64 | 17 | M24 (Weakness) | 8/64 (12.5%) | 6 | M24(Weakness)=8; T2(Supplementary)=7; M10(Sin)=1; FLAG(Flag)=1; M01(Fear)=1; M20(Doubt)=1 |
| calling | 49 | 20 | M37 (Calling) | 10/49 (20.4%) | 8 | M37(Calling)=10; T2(Supplementary)=3; M31(Faith)=2; M42(Speech)=2; M05(Love)=1; M29(Desire)=1; FLAG(Flag)=1; M41(Remembrance)=1 |
| character | 3 | 1 | M35 (Testing) | 1/3 (33.3%) | 1 | M35(Testing)=1 |
| comfort | 24 | 16 | M33 (Peace) | 5/24 (20.8%) | 7 | M33(Peace)=5; M04(Joy)=4; M05(Love)=4; M23(Strength)=1; M17(Counsel)=1; M11(Repentance)=1; M19(Trust)=1 |
| compassion | 47 | 29 | M05 (Love) | 19/47 (40.4%) | 8 | M05(Love)=19; T2(Supplementary)=3; M39(Blessing)=2; M24(Weakness)=1; M03(Grief)=1; M33(Peace)=1; M11(Repentance)=1; M45(Transformation)=1 |
| condemnation | 22 | 16 | M26 (Righteousness) | 10/22 (45.5%) | 5 | M26(Righteousness)=10; FLAG(Flag)=4; T2(Supplementary)=3; M10(Sin)=2; M14(Deceit)=1 |
| conscience | 3 | 3 | M47 (Constitution) | 1/3 (33.3%) | 3 | M47(Constitution)=1; M15(Wisdom)=1; T2(Supplementary)=1 |
| consecration | 26 | 17 | T2 (Supplementary) | 6/26 (23.1%) | 5 | T2(Supplementary)=6; M12(Purity)=6; M22(Praise)=3; M37(Calling)=1; M17(Counsel)=1 |
| contempt | 51 | 21 | M06 (Hate) | 12/51 (23.5%) | 4 | M06(Hate)=12; M08(Pride)=4; M07(Shame)=3; T2(Supplementary)=2 |
| contentment | 26 | 16 | M02 (Anger) | 6/26 (23.1%) | 10 | M02(Anger)=6; M46(Abundance)=2; M35(Testing)=1; T2(Supplementary)=1; M28(Envy)=1; M04(Joy)=1; M29(Desire)=1; M39(Blessing)=1; M44(Relational)=1; M41(Remembrance)=1 |
| contrition | 5 | 5 | M24 (Weakness) | 3/5 (60.0%) | 4 | M24(Weakness)=3; M09(Humility)=1; M11(Repentance)=1; T2(Supplementary)=1 |
| corruption | 44 | 16 | M10 (Sin) | 8/44 (18.2%) | 5 | M10(Sin)=8; T2(Supplementary)=5; M25(Life)=1; M28(Envy)=1; M27(Evil)=1 |
| counsel | 18 | 10 | M17 (Counsel) | 6/18 (33.3%) | 3 | M17(Counsel)=6; M15(Wisdom)=3; T2(Supplementary)=1 |
| courage | 15 | 10 | M23 (Strength) | 7/15 (46.7%) | 4 | M23(Strength)=7; M04(Joy)=4; M34(Perseverance)=1; M08(Pride)=1 |
| covenant | 11 | 7 | M44 (Relational) | 3/11 (27.3%) | 3 | M44(Relational)=3; T2(Supplementary)=3; M21(Prayer)=1 |
| covetousness | 15 | 12 | M28 (Envy) | 7/15 (46.7%) | 5 | M28(Envy)=7; M18(Hope)=2; M05(Love)=1; M19(Trust)=1; M29(Desire)=1 |
| craving | 18 | 13 | M28 (Envy) | 5/18 (27.8%) | 6 | M28(Envy)=5; M18(Hope)=3; M21(Prayer)=2; M05(Love)=1; M29(Desire)=1; M24(Weakness)=1 |
| Cursing | 29 | 10 | T2 (Supplementary) | 4/29 (13.8%) | 6 | T2(Supplementary)=4; M07(Shame)=2; M10(Sin)=1; M24(Weakness)=1; M06(Hate)=1; M39(Blessing)=1 |
| deadness | 26 | 10 | T2 (Supplementary) | 6/26 (23.1%) | 4 | T2(Supplementary)=6; M24(Weakness)=2; M47(Constitution)=1; M27(Evil)=1 |
| debauchery | 3 | 3 | M28 (Envy) | 2/3 (66.7%) | 2 | M28(Envy)=2; T2(Supplementary)=1 |
| deceit | 46 | 22 | M14 (Deceit) | 17/46 (37.0%) | 4 | M14(Deceit)=17; M10(Sin)=3; M20(Doubt)=1; M13(Truth)=1 |
| defilement | 30 | 14 | M10 (Sin) | 7/30 (23.3%) | 5 | M10(Sin)=7; M12(Purity)=3; T2(Supplementary)=2; M06(Hate)=1; M27(Evil)=1 |
| delight | 56 | 45 | M04 (Joy) | 29/56 (51.8%) | 9 | M04(Joy)=29; M28(Envy)=5; T2(Supplementary)=5; M05(Love)=2; FLAG(Flag)=1; M12(Purity)=1; M46(Abundance)=1; M39(Blessing)=1; M29(Desire)=1 |
| desire | 62 | 53 | M28 (Envy) | 16/62 (25.8%) | 15 | M28(Envy)=16; M18(Hope)=7; M29(Desire)=7; M04(Joy)=5; M21(Prayer)=5; T2(Supplementary)=2; M41(Remembrance)=2; M05(Love)=2; M17(Counsel)=1; M15(Wisdom)=1; M39(Blessing)=1; M37(Calling)=1; M44(Relational)=1; M47(Constitution)=1; M19(Trust)=1 |
| despair | 19 | 10 | M20 (Doubt) | 2/19 (10.5%) | 8 | M20(Doubt)=2; M24(Weakness)=2; M18(Hope)=1; M07(Shame)=1; M03(Grief)=1; M01(Fear)=1; T2(Supplementary)=1; M27(Evil)=1 |
| devious | 5 | 3 | M14 (Deceit) | 2/5 (40.0%) | 2 | M14(Deceit)=2; M10(Sin)=1 |
| devotion | 27 | 7 | M05 (Love) | 2/27 (7.4%) | 6 | M05(Love)=2; T2(Supplementary)=1; M34(Perseverance)=1; M12(Purity)=1; M39(Blessing)=1; M30(Obedience)=1 |
| dignity | 12 | 9 | M22 (Praise) | 5/12 (41.7%) | 4 | M22(Praise)=5; M08(Pride)=2; M34(Perseverance)=1; M09(Humility)=1 |
| discernment | 26 | 21 | M15 (Wisdom) | 12/26 (46.2%) | 6 | M15(Wisdom)=12; T2(Supplementary)=3; M43(Prophecy)=2; M41(Remembrance)=2; M35(Testing)=1; M14(Deceit)=1 |
| disobedience | 6 | 4 | M30 (Obedience) | 4/6 (66.7%) | 1 | M30(Obedience)=4 |
| distress | 58 | 55 | M03 (Grief) | 19/58 (32.8%) | 14 | M03(Grief)=19; M24(Weakness)=10; M01(Fear)=9; T2(Supplementary)=7; M02(Anger)=4; FLAG(Flag)=4; M23(Strength)=3; M27(Evil)=3; M42(Speech)=2; M06(Hate)=2; M10(Sin)=1; M44(Relational)=1; M28(Envy)=1; M15(Wisdom)=1 |
| division | 25 | 12 | T2 (Supplementary) | 12/25 (48.0%) | 2 | T2(Supplementary)=12; FLAG(Flag)=1 |
| dominion | 26 | 21 | M23 (Strength) | 16/26 (61.5%) | 3 | M23(Strength)=16; T2(Supplementary)=5; M17(Counsel)=1 |
| doubt | 10 | 7 | M20 (Doubt) | 3/10 (30.0%) | 4 | M20(Doubt)=3; M15(Wisdom)=2; M31(Faith)=1; T2(Supplementary)=1 |
| dread | 38 | 27 | M01 (Fear) | 24/38 (63.2%) | 4 | M01(Fear)=24; M20(Doubt)=1; M04(Joy)=1; M06(Hate)=1 |
| endurance | 47 | 20 | M34 (Perseverance) | 4/47 (8.5%) | 10 | M34(Perseverance)=4; T2(Supplementary)=4; M23(Strength)=3; M35(Testing)=2; M24(Weakness)=2; M05(Love)=1; M33(Peace)=1; M13(Truth)=1; M25(Life)=1; M46(Abundance)=1 |
| envy | 10 | 9 | M28 (Envy) | 4/10 (40.0%) | 6 | M28(Envy)=4; M02(Anger)=2; M21(Prayer)=1; M19(Trust)=1; T2(Supplementary)=1; M06(Hate)=1 |
| evil | 44 | 28 | M10 (Sin) | 12/44 (27.3%) | 9 | M10(Sin)=12; M27(Evil)=7; M14(Deceit)=3; M03(Grief)=2; M07(Shame)=1; M24(Weakness)=1; T2(Supplementary)=1; M28(Envy)=1; M15(Wisdom)=1 |
| experience | 6 | 4 | M35 (Testing) | 2/6 (33.3%) | 3 | M35(Testing)=2; M24(Weakness)=1; T2(Supplementary)=1 |
| faith | 25 | 23 | M13 (Truth) | 8/25 (32.0%) | 6 | M13(Truth)=8; M31(Faith)=7; M10(Sin)=3; M05(Love)=3; M18(Hope)=1; M19(Trust)=1 |
| faithfulness | 25 | 23 | M13 (Truth) | 8/25 (32.0%) | 6 | M13(Truth)=8; M31(Faith)=7; M10(Sin)=3; M05(Love)=3; M18(Hope)=1; M19(Trust)=1 |
| fear | 62 | 53 | M01 (Fear) | 42/62 (67.7%) | 6 | M01(Fear)=42; T2(Supplementary)=4; M21(Prayer)=4; M20(Doubt)=2; M31(Faith)=1; M06(Hate)=1 |
| fellowship | 9 | 4 | M05 (Love) | 2/9 (22.2%) | 3 | M05(Love)=2; T2(Supplementary)=1; M17(Counsel)=1 |
| flesh | 16 | 16 | T2 (Supplementary) | 6/16 (37.5%) | 4 | T2(Supplementary)=6; M47(Constitution)=6; M28(Envy)=3; M07(Shame)=1 |
| foolishness | 37 | 25 | M16 (Folly) | 20/37 (54.1%) | 5 | M16(Folly)=20; T2(Supplementary)=3; M15(Wisdom)=1; M08(Pride)=1; M19(Trust)=1 |
| forgiveness | 14 | 10 | M11 (Repentance) | 8/14 (57.1%) | 3 | M11(Repentance)=8; M38(Salvation)=1; M39(Blessing)=1 |
| generosity | 3 | 2 | M05 (Love) | 2/3 (66.7%) | 1 | M05(Love)=2 |
| gentleness | 18 | 11 | M05 (Love) | 8/18 (44.4%) | 3 | M05(Love)=8; M09(Humility)=2; M24(Weakness)=1 |
| gladness | 24 | 22 | M04 (Joy) | 18/24 (75.0%) | 5 | M04(Joy)=18; M22(Praise)=1; T2(Supplementary)=1; M39(Blessing)=1; M42(Speech)=1 |
| goodness | 56 | 20 | M05 (Love) | 9/56 (16.1%) | 8 | M05(Love)=9; M46(Abundance)=3; M39(Blessing)=3; M22(Praise)=2; M04(Joy)=2; M06(Hate)=1; M23(Strength)=1; T2(Supplementary)=1 |
| grace | 9 | 6 | M39 (Blessing) | 4/9 (44.4%) | 3 | M39(Blessing)=4; M05(Love)=1; M21(Prayer)=1 |
| gratitude | 3 | 3 | M04 (Joy) | 2/3 (66.7%) | 2 | M04(Joy)=2; M39(Blessing)=1 |
| greed | 7 | 3 | M28 (Envy) | 2/7 (28.6%) | 2 | M28(Envy)=2; M24(Weakness)=1 |
| grief | 30 | 26 | M03 (Grief) | 17/30 (56.7%) | 6 | M03(Grief)=17; M24(Weakness)=5; T2(Supplementary)=2; M42(Speech)=1; M02(Anger)=1; M10(Sin)=1 |
| groaning | 22 | 14 | M03 (Grief) | 6/22 (27.3%) | 5 | M03(Grief)=6; M42(Speech)=5; T2(Supplementary)=1; M15(Wisdom)=1; M39(Blessing)=1 |
| guilt | 17 | 15 | M10 (Sin) | 11/17 (64.7%) | 4 | M10(Sin)=11; M26(Righteousness)=2; M47(Constitution)=1; T2(Supplementary)=1 |
| hardness | 42 | 25 | T2 (Supplementary) | 7/42 (16.7%) | 10 | T2(Supplementary)=7; M30(Obedience)=5; M23(Strength)=5; M03(Grief)=3; FLAG(Flag)=3; M22(Praise)=1; M08(Pride)=1; M04(Joy)=1; M24(Weakness)=1; M27(Evil)=1 |
| hatred | 14 | 8 | M06 (Hate) | 7/14 (50.0%) | 3 | M06(Hate)=7; M44(Relational)=1; M28(Envy)=1 |
| healing | 44 | 19 | M33 (Peace) | 6/44 (13.6%) | 9 | M33(Peace)=6; M25(Life)=3; M23(Strength)=2; M38(Salvation)=2; T2(Supplementary)=2; M05(Love)=1; M13(Truth)=1; M04(Joy)=1; M12(Purity)=1 |
| heart | 38 | 37 | M47 (Constitution) | 14/38 (36.8%) | 11 | M47(Constitution)=14; T2(Supplementary)=11; M05(Love)=3; M20(Doubt)=2; M04(Joy)=2; M23(Strength)=1; M26(Righteousness)=1; M30(Obedience)=1; M15(Wisdom)=1; M28(Envy)=1; M24(Weakness)=1 |
| holiness | 31 | 24 | M22 (Praise) | 8/31 (25.8%) | 5 | M22(Praise)=8; M12(Purity)=7; T2(Supplementary)=6; M05(Love)=2; M25(Life)=1 |
| honesty | 6 | 6 | M26 (Righteousness) | 3/6 (50.0%) | 3 | M26(Righteousness)=3; M13(Truth)=2; M09(Humility)=1 |
| hope | 33 | 24 | M18 (Hope) | 13/33 (39.4%) | 6 | M18(Hope)=13; M19(Trust)=5; T2(Supplementary)=2; M17(Counsel)=2; M03(Grief)=1; M20(Doubt)=1 |
| humility | 12 | 9 | M09 (Humility) | 6/12 (50.0%) | 2 | M09(Humility)=6; M05(Love)=3 |
| hypocrisy | 5 | 3 | M12 (Purity) | 1/5 (20.0%) | 3 | M12(Purity)=1; M10(Sin)=1; M14(Deceit)=1 |
| idolatry | 5 | 3 | M27 (Evil) | 2/5 (40.0%) | 2 | M27(Evil)=2; M28(Envy)=1 |
| image | 25 | 8 | T2 (Supplementary) | 5/25 (20.0%) | 4 | T2(Supplementary)=5; M43(Prophecy)=2; FLAG(Flag)=1; M27(Evil)=1 |
| imagination | 17 | 12 | M15 (Wisdom) | 5/17 (29.4%) | 7 | M15(Wisdom)=5; T2(Supplementary)=2; M47(Constitution)=1; M42(Speech)=1; M29(Desire)=1; M14(Deceit)=1; M30(Obedience)=1 |
| impurity | 11 | 5 | M10 (Sin) | 4/11 (36.4%) | 2 | M10(Sin)=4; M12(Purity)=1 |
| indignation | 17 | 13 | M02 (Anger) | 10/17 (58.8%) | 4 | M02(Anger)=10; M21(Prayer)=1; M24(Weakness)=1; M30(Obedience)=1 |
| iniquity | 24 | 19 | M10 (Sin) | 15/24 (62.5%) | 4 | M10(Sin)=15; M30(Obedience)=2; M03(Grief)=1; M24(Weakness)=1 |
| innocence | 24 | 17 | M12 (Purity) | 8/24 (33.3%) | 7 | M12(Purity)=8; M26(Righteousness)=3; T2(Supplementary)=2; M07(Shame)=2; M34(Perseverance)=1; M13(Truth)=1; FLAG(Flag)=1 |
| insight | 16 | 13 | M15 (Wisdom) | 10/16 (62.5%) | 3 | M15(Wisdom)=10; M43(Prophecy)=2; M47(Constitution)=1 |
| integrity | 27 | 10 | M13 (Truth) | 4/27 (14.8%) | 4 | M13(Truth)=4; M12(Purity)=3; M26(Righteousness)=2; M34(Perseverance)=1 |
| intention | 22 | 13 | M15 (Wisdom) | 5/22 (22.7%) | 6 | M15(Wisdom)=5; M17(Counsel)=2; T2(Supplementary)=2; M14(Deceit)=2; M41(Remembrance)=1; M29(Desire)=1 |
| intercession | 4 | 4 | M21 (Prayer) | 2/4 (50.0%) | 3 | M21(Prayer)=2; M37(Calling)=1; T2(Supplementary)=1 |
| jealousy | 8 | 4 | M02 (Anger) | 2/8 (25.0%) | 3 | M02(Anger)=2; M21(Prayer)=1; M28(Envy)=1 |
| joy | 29 | 28 | M04 (Joy) | 21/29 (72.4%) | 4 | M04(Joy)=21; M42(Speech)=4; T2(Supplementary)=2; M08(Pride)=1 |
| justice | 26 | 22 | M26 (Righteousness) | 21/26 (80.8%) | 3 | M26(Righteousness)=21; FLAG(Flag)=6; T2(Supplementary)=3 |
| kindness | 33 | 15 | M05 (Love) | 11/33 (33.3%) | 4 | M05(Love)=11; M39(Blessing)=2; M04(Joy)=2; M07(Shame)=1 |
| knowledge | 27 | 16 | M15 (Wisdom) | 13/27 (48.1%) | 3 | M15(Wisdom)=13; T2(Supplementary)=2; M37(Calling)=1 |
| likeness | 36 | 16 | T2 (Supplementary) | 11/36 (30.6%) | 5 | T2(Supplementary)=11; M43(Prophecy)=2; M05(Love)=2; FLAG(Flag)=2; M39(Blessing)=1 |
| listen | 26 | 24 | M41 (Remembrance) | 9/26 (34.6%) | 6 | M41(Remembrance)=9; T2(Supplementary)=9; M21(Prayer)=3; M35(Testing)=1; M30(Obedience)=1; M33(Peace)=1 |
| longing | 78 | 31 | M18 (Hope) | 10/78 (12.8%) | 11 | M18(Hope)=10; T2(Supplementary)=6; M28(Envy)=5; M29(Desire)=3; M34(Perseverance)=1; M25(Life)=1; M08(Pride)=1; M05(Love)=1; M19(Trust)=1; M46(Abundance)=1; M23(Strength)=1 |
| love | 52 | 44 | M05 (Love) | 21/52 (40.4%) | 9 | M05(Love)=21; T2(Supplementary)=9; M28(Envy)=7; M02(Anger)=2; M04(Joy)=2; M33(Peace)=1; M21(Prayer)=1; M39(Blessing)=1; M06(Hate)=1 |
| lust | 17 | 15 | M28 (Envy) | 9/17 (52.9%) | 6 | M28(Envy)=9; M29(Desire)=2; T2(Supplementary)=2; M18(Hope)=1; M04(Joy)=1; M23(Strength)=1 |
| malice | 9 | 8 | M10 (Sin) | 4/9 (44.4%) | 4 | M10(Sin)=4; M06(Hate)=2; M28(Envy)=1; M02(Anger)=1 |
| meaning | 16 | 8 | M15 (Wisdom) | 3/16 (18.8%) | 4 | M15(Wisdom)=3; T2(Supplementary)=3; M07(Shame)=1; M12(Purity)=1 |
| meditation | 21 | 8 | M15 (Wisdom) | 5/21 (23.8%) | 4 | M15(Wisdom)=5; M42(Speech)=1; T2(Supplementary)=1; M03(Grief)=1 |
| memory | 13 | 8 | T2 (Supplementary) | 5/13 (38.5%) | 2 | T2(Supplementary)=5; M41(Remembrance)=3 |
| mercy | 30 | 29 | M05 (Love) | 16/30 (53.3%) | 7 | M05(Love)=16; T2(Supplementary)=4; M38(Salvation)=3; M39(Blessing)=2; M21(Prayer)=2; M12(Purity)=1; M11(Repentance)=1 |
| might | 8 | 7 | M23 (Strength) | 4/8 (50.0%) | 2 | M23(Strength)=4; T2(Supplementary)=3 |
| mind | 58 | 54 | M47 (Constitution) | 17/58 (29.3%) | 16 | M47(Constitution)=17; M15(Wisdom)=11; M41(Remembrance)=7; T2(Supplementary)=5; M16(Folly)=3; M05(Love)=2; M29(Desire)=2; M20(Doubt)=1; M45(Transformation)=1; M19(Trust)=1; M33(Peace)=1; M17(Counsel)=1; M27(Evil)=1; M09(Humility)=1; M11(Repentance)=1; M30(Obedience)=1 |
| mourning | 47 | 30 | M03 (Grief) | 18/47 (38.3%) | 6 | M03(Grief)=18; M42(Speech)=6; M24(Weakness)=2; T2(Supplementary)=2; M10(Sin)=1; M05(Love)=1 |
| name | 19 | 8 | M37 (Calling) | 4/19 (21.1%) | 3 | M37(Calling)=4; T2(Supplementary)=4; FLAG(Flag)=1 |
| obedience | 12 | 8 | M09 (Humility) | 4/12 (33.3%) | 4 | M09(Humility)=4; M41(Remembrance)=2; M23(Strength)=1; M30(Obedience)=1 |
| passion | 11 | 7 | M28 (Envy) | 4/11 (36.4%) | 4 | M28(Envy)=4; M24(Weakness)=2; M04(Joy)=1; T2(Supplementary)=1 |
| patience | 10 | 9 | M34 (Perseverance) | 3/10 (30.0%) | 5 | M34(Perseverance)=3; T2(Supplementary)=3; M33(Peace)=1; M25(Life)=1; M24(Weakness)=1 |
| peace | 43 | 34 | M33 (Peace) | 26/43 (60.5%) | 9 | M33(Peace)=26; M42(Speech)=2; M05(Love)=1; M07(Shame)=1; M22(Praise)=1; T2(Supplementary)=1; M14(Deceit)=1; M19(Trust)=1; M46(Abundance)=1 |
| perverseness | 24 | 14 | M10 (Sin) | 9/24 (37.5%) | 4 | M10(Sin)=9; M14(Deceit)=3; T2(Supplementary)=1; M03(Grief)=1 |
| power | 82 | 66 | M23 (Strength) | 39/82 (47.6%) | 8 | M23(Strength)=39; T2(Supplementary)=26; M17(Counsel)=1; M01(Fear)=1; M06(Hate)=1; M04(Joy)=1; M08(Pride)=1; M34(Perseverance)=1 |
| praise | 60 | 33 | M22 (Praise) | 22/60 (36.7%) | 8 | M22(Praise)=22; M42(Speech)=3; T2(Supplementary)=2; M16(Folly)=2; M08(Pride)=2; M39(Blessing)=1; M33(Peace)=1; M15(Wisdom)=1 |
| prayer | 19 | 14 | M21 (Prayer) | 12/19 (63.2%) | 3 | M21(Prayer)=12; T2(Supplementary)=1; M15(Wisdom)=1 |
| pride | 32 | 28 | M08 (Pride) | 27/32 (84.4%) | 3 | M08(Pride)=27; T2(Supplementary)=2; M04(Joy)=1 |
| prophecy | 9 | 6 | M43 (Prophecy) | 3/9 (33.3%) | 3 | M43(Prophecy)=3; T2(Supplementary)=2; M42(Speech)=1 |
| purity | 18 | 10 | M12 (Purity) | 10/18 (55.6%) | 1 | M12(Purity)=10 |
| purpose | 39 | 23 | M17 (Counsel) | 7/39 (17.9%) | 9 | M17(Counsel)=7; M15(Wisdom)=6; T2(Supplementary)=4; M14(Deceit)=2; M39(Blessing)=1; M04(Joy)=1; FLAG(Flag)=1; M29(Desire)=1; M42(Speech)=1 |
| reasoning | 39 | 17 | M15 (Wisdom) | 6/39 (15.4%) | 7 | M15(Wisdom)=6; M26(Righteousness)=4; T2(Supplementary)=4; M04(Joy)=1; M05(Love)=1; M43(Prophecy)=1; FLAG(Flag)=1 |
| rebellion | 24 | 13 | M30 (Obedience) | 7/24 (29.2%) | 4 | M30(Obedience)=7; M10(Sin)=4; M02(Anger)=1; M08(Pride)=1 |
| reconciliation | 3 | 3 | M38 (Salvation) | 1/3 (33.3%) | 3 | M38(Salvation)=1; M05(Love)=1; M10(Sin)=1 |
| rejection | 41 | 12 | M06 (Hate) | 5/41 (12.2%) | 6 | M06(Hate)=5; M30(Obedience)=3; M11(Repentance)=1; T2(Supplementary)=1; M07(Shame)=1; M20(Doubt)=1 |
| rejoicing | 36 | 29 | M04 (Joy) | 21/36 (58.3%) | 6 | M04(Joy)=21; M08(Pride)=3; M42(Speech)=2; M22(Praise)=1; T2(Supplementary)=1; M23(Strength)=1 |
| renewal | 16 | 4 | M45 (Transformation) | 3/16 (18.8%) | 3 | M45(Transformation)=3; FLAG(Flag)=1; T2(Supplementary)=1 |
| repentance | 14 | 9 | M45 (Transformation) | 5/14 (35.7%) | 4 | M45(Transformation)=5; M11(Repentance)=2; M13(Truth)=1; M05(Love)=1 |
| righteousness | 11 | 9 | M26 (Righteousness) | 9/11 (81.8%) | 1 | M26(Righteousness)=9 |
| Ruthlessness | 9 | 7 | M06 (Hate) | 4/9 (44.4%) | 5 | M06(Hate)=4; M05(Love)=1; M03(Grief)=1; T2(Supplementary)=1; M23(Strength)=1 |
| salvation | 24 | 10 | M38 (Salvation) | 8/24 (33.3%) | 2 | M38(Salvation)=8; T2(Supplementary)=2 |
| seeking | 30 | 16 | M21 (Prayer) | 4/30 (13.3%) | 8 | M21(Prayer)=4; M41(Remembrance)=4; T2(Supplementary)=3; M35(Testing)=1; M28(Envy)=1; M19(Trust)=1; M23(Strength)=1; M37(Calling)=1 |
| self-control | 17 | 13 | M19 (Trust) | 5/17 (29.4%) | 7 | M19(Trust)=5; T2(Supplementary)=4; M15(Wisdom)=2; M28(Envy)=1; M08(Pride)=1; M47(Constitution)=1; M30(Obedience)=1 |
| shame | 40 | 31 | M07 (Shame) | 22/40 (55.0%) | 6 | M07(Shame)=22; M06(Hate)=6; M05(Love)=2; M30(Obedience)=1; M01(Fear)=1; M18(Hope)=1 |
| sin | 48 | 35 | M10 (Sin) | 24/48 (50.0%) | 7 | M10(Sin)=24; T2(Supplementary)=3; M30(Obedience)=3; M12(Purity)=2; M27(Evil)=2; M16(Folly)=1; M03(Grief)=1 |
| sincerity | 13 | 11 | M12 (Purity) | 5/13 (38.5%) | 5 | M12(Purity)=5; M13(Truth)=2; M26(Righteousness)=2; T2(Supplementary)=1; M05(Love)=1 |
| slander | 26 | 17 | M14 (Deceit) | 7/26 (26.9%) | 6 | M14(Deceit)=7; M10(Sin)=5; M42(Speech)=2; M07(Shame)=1; T2(Supplementary)=1; M20(Doubt)=1 |
| sloth | 8 | 6 | M24 (Weakness) | 4/8 (50.0%) | 3 | M24(Weakness)=4; M16(Folly)=1; M14(Deceit)=1 |
| sorcery | 7 | 3 | T2 (Supplementary) | 3/7 (42.9%) | 1 | T2(Supplementary)=3 |
| sorrow | 46 | 42 | M03 (Grief) | 26/46 (56.5%) | 7 | M03(Grief)=26; M24(Weakness)=6; T2(Supplementary)=5; M10(Sin)=2; M01(Fear)=2; M02(Anger)=2; M42(Speech)=1 |
| Soul | 15 | 14 | M47 (Constitution) | 10/15 (66.7%) | 3 | M47(Constitution)=10; M25(Life)=3; T2(Supplementary)=1 |
| spirit | 23 | 17 | M25 (Life) | 5/23 (21.7%) | 6 | M25(Life)=5; T2(Supplementary)=5; M47(Constitution)=4; M22(Praise)=1; M33(Peace)=1; M27(Evil)=1 |
| strength | 78 | 72 | M23 (Strength) | 46/78 (59.0%) | 11 | M23(Strength)=46; T2(Supplementary)=18; M08(Pride)=2; M24(Weakness)=1; M05(Love)=1; M38(Salvation)=1; M04(Joy)=1; M22(Praise)=1; M46(Abundance)=1; M19(Trust)=1; M25(Life)=1 |
| strife | 30 | 16 | M02 (Anger) | 10/30 (33.3%) | 7 | M02(Anger)=10; T2(Supplementary)=3; M44(Relational)=1; M28(Envy)=1; M26(Righteousness)=1; FLAG(Flag)=1; M06(Hate)=1 |
| stubbornness | 18 | 7 | M30 (Obedience) | 3/18 (16.7%) | 5 | M30(Obedience)=3; M23(Strength)=2; FLAG(Flag)=1; T2(Supplementary)=1; M24(Weakness)=1 |
| submission | 4 | 2 | M09 (Humility) | 1/4 (25.0%) | 2 | M09(Humility)=1; M23(Strength)=1 |
| Suffering | 15 | 10 | M03 (Grief) | 5/15 (33.3%) | 4 | M03(Grief)=5; M24(Weakness)=4; FLAG(Flag)=2; T2(Supplementary)=2 |
| surrender | 10 | 6 | T2 (Supplementary) | 5/10 (50.0%) | 2 | T2(Supplementary)=5; M12(Purity)=1 |
| temptation | 6 | 4 | M35 (Testing) | 3/6 (50.0%) | 2 | M35(Testing)=3; M10(Sin)=1 |
| terror | 43 | 37 | M01 (Fear) | 35/43 (81.4%) | 6 | M01(Fear)=35; T2(Supplementary)=2; M03(Grief)=2; FLAG(Flag)=1; M24(Weakness)=1; M06(Hate)=1 |
| testimony | 22 | 9 | T2 (Supplementary) | 5/22 (22.7%) | 5 | T2(Supplementary)=5; M15(Wisdom)=1; M35(Testing)=1; M42(Speech)=1; M13(Truth)=1 |
| the afflicted | 76 | 23 | M24 (Weakness) | 10/76 (13.2%) | 7 | M24(Weakness)=10; T2(Supplementary)=10; FLAG(Flag)=2; M46(Abundance)=1; M05(Love)=1; M28(Envy)=1; M38(Salvation)=1 |
| thought | 47 | 35 | M15 (Wisdom) | 22/47 (46.8%) | 11 | M15(Wisdom)=22; M26(Righteousness)=3; M20(Doubt)=2; M14(Deceit)=2; M47(Constitution)=1; M23(Strength)=1; FLAG(Flag)=1; M16(Folly)=1; M41(Remembrance)=1; M21(Prayer)=1; M01(Fear)=1 |
| transformation | 5 | 2 | M45 (Transformation) | 1/5 (20.0%) | 2 | M45(Transformation)=1; T2(Supplementary)=1 |
| transgression | 17 | 13 | M10 (Sin) | 9/17 (52.9%) | 4 | M10(Sin)=9; M30(Obedience)=2; M36(Service)=1; M16(Folly)=1 |
| treachery | 10 | 8 | M14 (Deceit) | 6/10 (60.0%) | 2 | M14(Deceit)=6; M10(Sin)=2 |
| trust | 37 | 25 | M19 (Trust) | 14/37 (37.8%) | 8 | M19(Trust)=14; M31(Faith)=3; M18(Hope)=2; M13(Truth)=2; M35(Testing)=1; T2(Supplementary)=1; M17(Counsel)=1; M33(Peace)=1 |
| truthfulness | 24 | 14 | M13 (Truth) | 9/24 (37.5%) | 3 | M13(Truth)=9; T2(Supplementary)=3; M26(Righteousness)=2 |
| unbelief | 3 | 3 | M30 (Obedience) | 2/3 (66.7%) | 2 | M30(Obedience)=2; M31(Faith)=1 |
| understanding | 47 | 29 | M15 (Wisdom) | 18/47 (38.3%) | 8 | M15(Wisdom)=18; M41(Remembrance)=3; M47(Constitution)=2; T2(Supplementary)=2; M26(Righteousness)=1; M05(Love)=1; M16(Folly)=1; M43(Prophecy)=1 |
| unity | 3 | 1 | M44 (Relational) | 1/3 (33.3%) | 1 | M44(Relational)=1 |
| uprightness | 24 | 15 | M26 (Righteousness) | 6/24 (25.0%) | 6 | M26(Righteousness)=6; M13(Truth)=4; T2(Supplementary)=3; FLAG(Flag)=2; M11(Repentance)=1; M12(Purity)=1 |
| weakness | 45 | 19 | M24 (Weakness) | 15/45 (33.3%) | 4 | M24(Weakness)=15; M03(Grief)=2; M21(Prayer)=1; T2(Supplementary)=1 |
| wealth | 34 | 16 | M23 (Strength) | 7/34 (20.6%) | 4 | M23(Strength)=7; M46(Abundance)=7; M28(Envy)=1; M22(Praise)=1 |
| weeping | 21 | 11 | M03 (Grief) | 9/21 (42.9%) | 4 | M03(Grief)=9; M42(Speech)=1; T2(Supplementary)=1; M02(Anger)=1 |
| whoredom | 12 | 7 | M28 (Envy) | 4/12 (33.3%) | 3 | M28(Envy)=4; T2(Supplementary)=2; M10(Sin)=1 |
| wickedness | 27 | 21 | M10 (Sin) | 13/27 (48.1%) | 6 | M10(Sin)=13; M27(Evil)=3; M03(Grief)=3; M30(Obedience)=1; T2(Supplementary)=1; M26(Righteousness)=1 |
| will | 26 | 18 | M29 (Desire) | 8/26 (30.8%) | 8 | M29(Desire)=8; T2(Supplementary)=3; M08(Pride)=2; M04(Joy)=2; M15(Wisdom)=1; M34(Perseverance)=1; M30(Obedience)=1; M09(Humility)=1 |
| wisdom | 17 | 16 | M15 (Wisdom) | 13/17 (76.5%) | 3 | M15(Wisdom)=13; T2(Supplementary)=2; M14(Deceit)=1 |
| wonder | 25 | 12 | M04 (Joy) | 6/25 (24.0%) | 5 | M04(Joy)=6; M01(Fear)=3; M15(Wisdom)=1; M43(Prophecy)=1; T2(Supplementary)=1 |
| worship | 42 | 23 | M36 (Service) | 9/42 (21.4%) | 6 | M36(Service)=9; T2(Supplementary)=6; M21(Prayer)=3; M01(Fear)=3; M22(Praise)=2; M31(Faith)=1 |
| worth | 7 | 4 | T2 (Supplementary) | 3/7 (42.9%) | 2 | T2(Supplementary)=3; M22(Praise)=1 |
| wrath | 32 | 18 | M02 (Anger) | 16/32 (50.0%) | 2 | M02(Anger)=16; T2(Supplementary)=2 |
| yearning | 9 | 5 | T2 (Supplementary) | 2/9 (22.2%) | 4 | T2(Supplementary)=2; M18(Hope)=1; M29(Desire)=1; M05(Love)=1 |
| yielding | 29 | 6 | T2 (Supplementary) | 3/29 (10.3%) | 5 | T2(Supplementary)=3; M23(Strength)=1; M29(Desire)=1; M30(Obedience)=1; M12(Purity)=1 |
| zeal | 7 | 4 | M02 (Anger) | 2/7 (28.6%) | 3 | M02(Anger)=2; M21(Prayer)=1; M34(Perseverance)=1 |

## Full per-Strong's detail

The row-level join (word, strong, old cluster_code(s), old cluster name(s)) for all 4,848 active
`word_strong` rows is in the companion CSV:
[`word-strong-cluster-mapping-20260810.csv`](word-strong-cluster-mapping-20260810.csv).

## What this is — and isn't

This is a **factual join of two DBs**, not a new clustering decision. It shows where the *old* project's
Strong's-level cluster allocation lands relative to the *new* app's word→Strong's set. Read as a candidate
cross-reference for the reopened verse-lexical line ([`project_iba_study_reopened_20260805_v4`]), not as an
authoritative recluster — the old M-code allocation predates the reset method and was itself only ~60%
complete (3,164 of the old DB's 7,861 `mti_terms` rows carry no `cluster_code` at all — the reason a chunk
of the 1,853 unmatched `word_strong` rows above go unmatched even where an `mti_terms` row exists).
