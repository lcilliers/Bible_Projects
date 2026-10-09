# M18 Desire & Longing: cluster overview (strand start)

**Date:** 2026-10-08 · **Escalation:** #1993 · **Status:** data overview only. No verse has been read.

**Source:** read-only against iba.db, the same shape as the M64 quick summary (#1978, query v2): live `cluster_strong` rows only, hits from `verse_lexical`, and the "other" side is every other M-cluster.
- Script: [`m18-cluster-overview-pull-v1-20261008.py`](m18-cluster-overview-pull-v1-20261008.py)
- All hits: [`m18-cluster-hits-v1-20261008.csv`](m18-cluster-hits-v1-20261008.csv) (1,510 rows)
- Per Strong's, with the tag source: [`m18-cluster-strongs-v1-20261008.csv`](m18-cluster-strongs-v1-20261008.csv) (88 rows)
- Other M-codes in the same verses: [`m18-cluster-mcode-cooccurrence-v1-20261008.csv`](m18-cluster-mcode-cooccurrence-v1-20261008.csv)

## 1. The cluster

- **Name:** Desire & Longing. **Definition in `cluster`:** "Desire, craving, longing, thirst, hunger, appetite, zeal (absorbed M29: Desire, Longing and Will)".
- **M29 merge:** 13 Strong's were moved from M29 on 2026-09-06 (#1525, researcher: *"merge M29 into M18 and set M29 as deleted"*): G0594, G4288, G4356, G5093, H1214I, H2974, H3357, H3365, H3368, H5068, H5069, H7522, H7904.
- **How the 88 live Strong's came to be tagged** (`cluster_strong.source`):

| Source | Strong's |
| --- | --- |
| heuristic family grouping (2026-09-05, "family=desire-longing-appetite") | 54 |
| old-system migration | 20 |
| auto-precedent | 8 |
| LLM allocation v1.3 | 5 |
| Claude scan (#1598) | 1 |

- One deleted row: H2638 (*lacking*), not counted.
- Per #1970 the tags are a loose association for analysis. Nothing here proposes a re-tag.

## 2. Scale

| Measure | Count |
| --- | --- |
| M18 Strong's (live), all with hits | 88 (56 Hebrew, 32 Greek) |
| M18 hits (distinct verse · position · Strong's) | 1,510 |
| Verses | 1,370 (OT 951, NT 419) |
| Books | 64 |
| Verses with more than one M18 hit | 132 |
| Verses that also hold another M-code | 1,177 |

For comparison, M64 had 28 Strong's, 493 hits and 468 verses. M18 is about three times its size.

Books with the most M18 verses: Psa 139, Pro 108, Isa 70, Mat 59, Ecc 52, Gen 46, Deu 45, Luk 43, 1Sa 42, 1Ki 41, Joh 37, Eze 36, Rom 33, 2Ch 32.

## 3. The Strong's by gloss

The groups below are a reading aid by gloss only. They are not a finding and not a sub-grouping of the cluster.

| Gloss group | Strong's | Hits |
| --- | --- | --- |
| A. desire, craving, longing | 35 | 258 |
| B. delight, pleasure, pleasant, good | 19 | 640 |
| C. will, willing, acceptance | 9 | 372 |
| D. jealousy, zeal | 9 | 112 |
| E. thirst, hunger | 5 | 45 |
| F. precious, costly | 4 | 60 |
| G. gloss away from desire | 7 | 23 |

Two Strong's hold 614 of the 1,510 hits (41%):
- **H2896A *tov* "pleasant": 408 hits, 381 verses.** The ESV surface is mostly "good" (220), "better" (58 + 14 "Better"), "well" (13), "please" (10), "best" (9).
- **G2309 *thelō* "to will/desire": 206 hits, 196 verses.** Surface: "want" (47), "would" (18), "will" (17), "wish" (15), "wanted" (13), "desire" (12).

### 3A. Desire, craving, longing (35 Strong's, 258 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| G1939 *epithumia* | desire | 38 | 37 | passions (12), desires (12), desire (5), lust (2), covet (1) |
| H0183 *ʾāwāh* | to desire | 26 | 26 | desire (6), desires (6), desired (3), craves (2), longingly (2), craving (2) |
| H2530A *ḥāmad* | to desire | 21 | 20 | covet (6), desired (4), desire (2), delight (1), Precious (1) |
| H8378 *taʾăwāh* | desire | 20 | 20 | desire (10), craving (2), choicest (1), craved (1) |
| G1937 *epithumeō* | to long for | 16 | 16 | desire (3), covet (2), desired (2), long (2), desires (2), lustful (1) |
| H1942 *hawwāh* | desire | 16 | 16 | destruction (4), calamity (3), ruin (3), mischievous (1), deadly (1), wicked (1) |
| H2532A *ḥemdāh* | desire | 16 | 16 | pleasant (5), precious (4), one beloved (1), costly (1), desirable (1) |
| H4261 *maḥmad* | desire | 13 | 13 | delight (3), precious (2), treasures (2), delightful (1) |
| G1971 *epipotheō* | to long for | 9 | 9 | long (4), longing (2), yearn for (1), yearns (1) |
| H1214I *bāṣaʿ* | to gain | 9 | 9 | greedy (5), carried out (1), who gets (1), make gain (1) |
| H2836A *ḥāšaq* | to desire | 8 | 8 | love (3), desired (2), longs (1), heart (1) |
| H7602A *šāʾap* | to long for | 8 | 8 | pant (4), longs (1), sniffing (1), hastens (1) |
| H0185 *ʾawwāh* | desire | 7 | 7 | desire (4), desires (1), please (1), heat (1) |
| H7469 *rĕʿût* | longing | 7 | 7 | striving (7) |
| H2531 *ḥemed* | delight | 6 | 6 | desirable (3), pleasant (3) |
| H3700 *kāsap* | to long | 6 | 5 | long, longed, greatly, eager, longs, shameless (1 each) |
| H2837 *ḥēšeq* | desire | 4 | 4 | desired (2), longed for (1), whatever (1) |
| G3713 *oregō* | to aspire | 3 | 3 | craving, desire, aspires |
| G5389 *philotimeomai* | to aspire | 3 | 3 | ambition, aim, aspire |
| H6165 *ʿārag* | to long for | 3 | 2 | pants (2), pant (1) |
| H8669 *tĕšûqāh* | desire | 3 | 3 | desire (3) |
| G1972 *epipothēsis* | longing | 2 | 2 | longing (2) |
| H8373 *tāʾab* | to long for | 2 | 2 | long (2) |
| 12 others with one hit each | | 12 | | H0035, H0404 "urges", H2968, H3616, H3970, H8375, H7904 "lusty", G1938, G1973, G1974, G2442, G2691 "passions draw" |

### 3B. Delight, pleasure, pleasant, good (19 Strong's, 640 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H2896A *ṭôb* | pleasant | 408 | 381 | good (220), better (58), Better (14), well (13), please (10), best (9) |
| H2654A *ḥāpēṣ* | to delight in | 73 | 69 | delight (19), delights (12), delighted (8), pleasure (6), desire (6), pleases (6) |
| H2656 *ḥēpeṣ* | pleasure | 39 | 38 | pleasure (7), desired (6), delight (5), desire (4), purpose (3), matter (3) |
| G2106 *eudokeō* | to delight | 21 | 21 | pleased (6), well pleased (5), pleasure (4), content (1) |
| H2895 *ṭôb* | be pleasing | 21 | 20 | merry (4), good (4), well (3), better (2), pleased (2) |
| H2655 *ḥāpēṣ* | delighting | 12 | 11 | delight (5), delights (3), please, would, willing, desires |
| H5273A *nāʿîm* | pleasant | 11 | 11 | pleasant (6), pleasures, pleasantness, lovely |
| H6026 *ʿānag* | to delight | 10 | 10 | delight (6), mocking (1), delicately bred (1), delicate (1) |
| H8191 *šaʿăšuʿîm* | delight | 9 | 9 | delight (6), darling, delighting, pleasant |
| H5276 *nāʿēm* | be pleasant | 8 | 8 | pleasant (6), delight, beauty |
| H5278 *nōʿam* | pleasantness | 7 | 7 | Favor (2), gracious, beauty, favor, pleasantness |
| H8173B *šāʿaʿ* | to delight | 6 | 6 | delight (3), cheer, bounced, play |
| G2237 *hēdonē* | pleasure | 5 | 5 | pleasures (2), passions (2), pleasure (1) |
| G0701 *arestos* | pleasing | 4 | 4 | right, pleases, pleasing to, pleased |
| 5 others | | 7 | | H6027 (2), H5282, H5730B, G4913, G5369 "pleasure" |

### 3C. Will, willing, acceptance (9 Strong's, 372 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| G2309 *thelō* | to will/desire | 206 | 196 | want (47), would (18), will (17), wish (15), wanted (13), desire (12) |
| G2307 *thelēma* | will/desire | 62 | 58 | will (60), desires (1), desire (1) |
| H7522 *rāṣôn* | acceptance | 56 | 56 | favor (18), accepted (8), acceptable (6), delight (4), will (4), wills (3) |
| H2974 *yāʾal* | be willing | 19 | 19 | pleased (6), content (3), persisted (3), undertaken (2), please (2) |
| H5068 *nādab* | be willing | 17 | 15 | willingly (5), freely offered (2), moves him, moved him, volunteer |
| G4288 *prothumia* | eagerness | 5 | 5 | readiness (3), good will, eagerness |
| H5069 *nĕdab* | be willing | 4 | 3 | freely offered, freely offers, freewill offerings, vowed willingly |
| G0594 *apodochē* | acceptance | 2 | 2 | acceptance (2) |
| G4356 *proslēmpsis* | acceptance | 1 | 1 | acceptance |

The M64 will reading (#1986) pulled H0014, H6634, H5081G, G1014 and G1013, and left G2309/G2307 aside as M18 (CLAUDE.md, #1986 entry). Those two are here, with 268 hits.

### 3D. Jealousy, zeal (9 Strong's, 112 hits)

| Strong's | Gloss | Hits | Verses | Surface (top) |
| --- | --- | --- | --- | --- |
| H7068 *qinʾāh* | jealousy | 43 | 41 | jealousy (27), zeal (10), envy (4) |
| H7065 *qānāʾ* | be jealous | 34 | 29 | jealous (18), jealousy (4), envious (4), envied (3), envy (2) |
| G2205 *zēlos* | zeal | 17 | 17 | jealousy (9), zeal (5), fury (1), worked (1) |
| G2207 *zēlōtēs* | zealot | 6 | 6 | zealous (5), eager (1) |
| H7067H *qannāʾ* | jealous | 5 | 5 | jealous (5) |
| H7072 *qannôʾ* | jealous | 2 | 2 | jealous (2) |
| G2208, G2581 | Zealot | 4 | 4 | "Zealot" (2 each): Simon the Zealot in the apostle lists (Mat 10:4, Mar 3:18, Luk 6:15, Act 1:13) |
| H7067G *qannāʾ* | Jealous [God] | 1 | 1 | Jealous |

### 3E. Thirst, hunger (5 Strong's, 45 hits)

H6772 *ṣāmāʾ* thirst 17 · G1372 *dipsaō* 16 · H6770 *ṣāmēʾ* 10 · G1373 *dipsos* 1 · G4361 *prospeinos* "very hungry" 1.

### 3F. Precious, costly (4 Strong's, 60 hits)

H3368 *yāqār* 35 (precious 24, costly 4) · G5093 *timios* 13 (precious 5, jewels 3) · H3365 *yāqar* 11 · H3357 *yaqqîr* 1 "dear". All four came from M29.

### 3G. Gloss away from desire (7 Strong's, 23 hits)

G3117 *makros* "long/distant" 13 (far 6, long 3, far off 2) · H4723C *miqweh* "collection" 3 (pools) · G3048 *logia* "collection" 2 · G0275 *amerimnos* "untroubled" 2 · H0627, H2841, H6899 "collection" 1 each.

## 4. Where the surface varies within one Strong's

This is where the change-of-character reading (#1919) would start. No reading has been done.
- H2896A *ṭôb*: "good / better / well / please / best", under the gloss "pleasant".
- H1942 *hawwāh*: "desire" gloss, surface "destruction / calamity / ruin".
- H7469 *rĕʿût*: "longing" gloss, surface "striving" in all 7, all in Ecclesiastes (1:14; 2:11, 17, 26; 4:4, 6; 6:9).
- H2656 *ḥēpeṣ*: pleasure / desired / delight / purpose / matter.
- H7522 *rāṣôn*: favor / accepted / acceptable / delight / will.
- H7068 *qinʾāh* and G2205 *zēlos*: jealousy / zeal / envy / fury.
- H2530A *ḥāmad* and G1937 *epithumeō*: desire / covet / long / lustful.
- H2974 *yāʾal*: pleased / content / persisted / undertaken / determined.
- H6026 *ʿānag*: delight / mocking / delicately bred.

The same surface word sits under several Strong's. For example:
- "desire" is under 16 Strong's, in groups A, B and C: G1937, G1938, G1939, G2307, G2309, G3713, H0035, H0183, H0185, H2530A, H2654A, H2656, H2836A, H7522, H8378, H8669
- "delight" is under 13: G4913, H2530A, H2654A, H2655, H2656, H4261, H5276, H6026, H6027, H7522, H8173B, H8191, H8378
- "precious" is under 8: G5093, H2530A, H2532A, H2656, H2896A, H3365, H3368, H4261
- "jealous" or "jealousy" is under 6: G2205, H7065, H7067G, H7067H, H7068, H7072

## 5. Other M-codes in the same verses

1,177 of the 1,370 verses also hold a word from another M-cluster. Verses shared, top 25:

| M-code | Verses | M-code | Verses |
| --- | --- | --- | --- |
| M47 Inner Seat | 208 | M45 Renewal & Transformation | 56 |
| M72 Authority & Dominion | 182 | M22 Praise & Song | 55 |
| M65 Speech & Tongue | 114 | M56 Sin & Guilt | 55 |
| M25 Life & Death | 111 | M50 Grace & Mercy | 54 |
| M15 Knowing & Understanding | 109 | M06 Malice & Enmity | 53 |
| M12 Righteousness & Integrity | 109 | M46 Wealth & Riches | 53 |
| M58 Wickedness | 103 | M23 Strength & Courage | 49 |
| M24 Faintness & Despair | 69 | M03 Grief & Lament | 47 |
| M42 Prayer & Petition | 69 | M04 Joy & Gladness | 46 |
| M16 Wisdom & Folly | 63 | M41 Being Heard | 44 |
| M05 Kindness & Friendship | 61 | M61 Purity & Holiness | 44 |
| M02 Anger & Wrath | 59 | M36 Worship & Service | 43 |
| | | M14 Deceit & Falsehood | 40 |

Also: **M64 Will & Resolve, 39 verses**; M01 Fear & Awe, 31 verses. The rest are in the CSV.

These counts link to work already done or held:
- **M47 (208 verses):** under the #1979 closure, this strand checks its M47 verses for dropped placements, by word and not by citation, as was done for M64 (#1989; OT-09).
- **M02 (59 verses):** OT-19 holds these, face by face, for when M18 is analysed. Its trigger is now reached.
- **M64 (39 verses):** some will already have been read in the M64 choose, plan and will work.
- **OT-15:** the heat family (*ḥāmam*, H2552, tagged T3) names "a strand on desire (M18)" as one of its triggers, for example Isa 57:5 "you who burn with lust".

## 6. Within-M18 pairs (verses with more than one M18 hit)

149 unordered pairs, in 132 verses. The most frequent:

| Pair | Count |
| --- | --- |
| H2896A + H2896A | 27 |
| H7065 + H7068 (be jealous + jealousy) | 12 |
| G2309 + G2309 | 11 |
| H7065 + H7065 | 5 |
| H2896A + H7469 | 4 |
| H2654A + H2654A | 4 |
| G2307 + G2307 | 4 |
| G1939 + G2307 (desire + will) | 3 |
| H2896A + H5273A | 3 |
| H0183 + H8378 (to desire + desire) | 3 |
| H2896A + H7522 | 3 |

The full list can be rebuilt from the hits CSV.

## 7. Points for your direction

M64 was taken in focused pulls, not broad brush (#1978). M18 is three times its size, and two Strong's hold 41% of the hits. These are the facts that bear on where to start. The choice is yours.

1. **H2896A *ṭôb* (408 hits).** Its surface is mostly "good / better". Taking it in full would set the size of the strand.
2. **G2309/G2307 *thelō*, *thelēma* (268 hits).** These were left aside in the M64 will reading (#1986) as M18. That reading would be the natural comparison.
3. **The core desire words (group A, 258 hits),** with jealousy and zeal (D, 112) and thirst (E, 45), are the words of the cluster definition.
4. **Held threads that name M18:** OT-19 (59 M02 verses) and OT-15 (the heat family).
5. **The M47 check** (208 verses), under #1979.
