# Cross-cluster co-occurrence matrix (L1-sweep roll-up · angle 1)

> READ-ONLY (`scripts/_assess_cross_cluster_cooccurrence.py`). A verse (reference) co-occurs two clusters when it holds active terms from both. T2/FLAG excluded. No DB writes.

**17266 characteristic verses · 7520 (44%) are cross-cluster** (hold ≥2 clusters). This is the connective tissue across the 46 clusters.

## A · Per-cluster cross-cluster exposure

| Cluster | verses | cross-cluster | % | clusters touched | top partners (shared verses) |
|---|---|---|---|---|---|
| M01 (Fear) | 930 | 597 | 64% | 45 | Strength 92, Wisdom 56, Praise 51, Obedience 46 |
| M02 (Anger) | 634 | 434 | 68% | 44 | Strength 75, Sin 52, Purity 45, Evil 44 |
| M03 (Grief) | 857 | 557 | 65% | 44 | Joy 63, Weakness 57, Strength 53, Wisdom 49 |
| M04 (Joy) | 1098 | 728 | 66% | 45 | Praise 95, Love 78, Wisdom 76, Strength 67 |
| M05 (Love) | 1245 | 833 | 67% | 45 | Strength 90, Praise 85, Truth 81, Joy 78 |
| M06 (Hate) | 414 | 306 | 74% | 44 | Relational 47, Strength 38, Sin 28, Evil 27 |
| M07 (Shame) | 318 | 229 | 72% | 44 | Pride 32, Wisdom 26, Fear 25, Strength 24 |
| M08 (Pride) | 633 | 401 | 63% | 44 | Strength 71, Praise 51, Wisdom 36, Joy 34 |
| M09 (Humility) | 108 | 72 | 67% | 38 | Love 11, Strength 10, Sin 9, Pride 8 |
| M10 (Sin) | 1252 | 873 | 70% | 45 | Repentance 109, Righteousness 104, Purity 88, Strength 80 |
| M10b (Wickedness) | 514 | 398 | 77% | 45 | Righteousness 86, Sin 65, Love 33, Strength 30 |
| M10c (Defilement) | 248 | 144 | 58% | 33 | Purity 38, Life 25, Envy 25, Sin 24 |
| M11 (Repentance) | 327 | 249 | 76% | 40 | Sin 109, Salvation 99, Purity 26, Transformation 22 |
| M12 (Purity) | 872 | 528 | 61% | 44 | Sin 88, Strength 74, Praise 57, Anger 45 |
| M13 (Truth) | 668 | 467 | 70% | 43 | Love 81, Righteousness 75, Wisdom 46, Praise 40 |
| M14 (Deceit) | 365 | 272 | 75% | 44 | Wisdom 49, Wickedness 29, Sin 29, Strength 26 |
| M15 (Wisdom) | 1505 | 979 | 65% | 45 | Strength 126, Joy 76, Righteousness 72, Remembrance 71 |
| M16 (Folly) | 156 | 112 | 72% | 36 | Wisdom 50, Anger 9, Pride 9, Weakness 9 |
| M17 (Counsel) | 278 | 201 | 72% | 42 | Wisdom 53, Strength 30, Praise 17, Truth 16 |
| M18 (Hope) | 270 | 172 | 64% | 41 | Love 24, Strength 15, Wisdom 15, Perseverance 14 |
| M19 (Trust) | 338 | 241 | 71% | 43 | Strength 34, Fear 30, Righteousness 19, Obedience 18 |
| M20 (Doubt) | 63 | 36 | 57% | 27 | Wisdom 4, Abundance 4, Love 4, Fear 4 |
| M21 (Prayer) | 522 | 268 | 51% | 43 | Love 32, Wisdom 28, Strength 23, Blessing 22 |
| M22 (Praise) | 1311 | 812 | 62% | 45 | Strength 112, Joy 95, Love 85, Purity 57 |
| M23 (Strength) | 2127 | 1235 | 58% | 45 | Wisdom 126, Praise 112, Fear 92, Weakness 91 |
| M24 (Weakness) | 757 | 488 | 64% | 45 | Strength 91, Grief 57, Love 44, Wisdom 38 |
| M25 (Life) | 764 | 523 | 68% | 44 | Relational 211, Strength 56, Wisdom 49, Praise 43 |
| M26 (Righteousness) | 910 | 646 | 71% | 45 | Sin 104, Wickedness 86, Truth 75, Wisdom 72 |
| M27 (Evil) | 540 | 382 | 71% | 44 | Wisdom 48, Anger 44, Sin 42, Strength 31 |
| M28 (Envy) | 506 | 332 | 66% | 44 | Sin 45, Strength 36, Wisdom 30, Joy 26 |
| M29 (Desire) | 296 | 210 | 71% | 44 | Strength 32, Love 32, Wisdom 27, Praise 15 |
| M30 (Obedience) | 860 | 515 | 60% | 44 | Sin 60, Wisdom 53, Strength 48, Fear 46 |
| M31 (Faith) | 304 | 198 | 65% | 43 | Righteousness 34, Love 28, Strength 27, Wisdom 26 |
| M33 (Peace) | 643 | 420 | 65% | 43 | Strength 57, Love 47, Joy 37, Grief 35 |
| M34 (Perseverance) | 218 | 159 | 73% | 42 | Love 29, Strength 18, Hope 14, Weakness 12 |
| M35 (Testing) | 182 | 112 | 62% | 42 | Strength 14, Prayer 12, Faith 12, Perseverance 12 |
| M36 (Service) | 583 | 350 | 60% | 43 | Strength 65, Praise 38, Obedience 36, Love 36 |
| M37 (Calling) | 1091 | 612 | 56% | 44 | Strength 83, Wisdom 69, Love 55, Praise 51 |
| M38 (Salvation) | 353 | 275 | 78% | 41 | Repentance 99, Sin 75, Strength 28, Faith 25 |
| M39 (Blessing) | 723 | 464 | 64% | 43 | Love 60, Strength 59, Joy 52, Praise 46 |
| M41 (Remembrance) | 949 | 633 | 67% | 45 | Wisdom 71, Strength 65, Sin 59, Love 47 |
| M42 (Speech) | 511 | 308 | 60% | 44 | Grief 46, Praise 42, Joy 33, Love 27 |
| M43 (Prophecy) | 143 | 85 | 59% | 38 | Wisdom 16, Strength 13, Praise 12, Love 11 |
| M44 (Relational) | 622 | 511 | 82% | 42 | Life 211, Strength 51, Hate 47, Remembrance 43 |
| M45 (Transformation) | 173 | 141 | 82% | 44 | Sin 45, Righteousness 24, Strength 23, Repentance 22 |
| M46 (Abundance) | 271 | 198 | 73% | 44 | Strength 48, Praise 31, Wisdom 29, Love 24 |

## B · Strongest cluster links (top 50 pairs by shared verses)

| Cluster A | Cluster B | shared | % of A | % of B |
|---|---|---|---|---|
| M25 (Life) | M44 (Relational) | 211 | 28% | 34% |
| M15 (Wisdom) | M23 (Strength) | 126 | 8% | 6% |
| M22 (Praise) | M23 (Strength) | 112 | 9% | 5% |
| M10 (Sin) | M11 (Repentance) | 109 | 9% | 33% |
| M10 (Sin) | M26 (Righteousness) | 104 | 8% | 11% |
| M11 (Repentance) | M38 (Salvation) | 99 | 30% | 28% |
| M04 (Joy) | M22 (Praise) | 95 | 9% | 7% |
| M01 (Fear) | M23 (Strength) | 92 | 10% | 4% |
| M23 (Strength) | M24 (Weakness) | 91 | 4% | 12% |
| M05 (Love) | M23 (Strength) | 90 | 7% | 4% |
| M10 (Sin) | M12 (Purity) | 88 | 7% | 10% |
| M10b (Wickedness) | M26 (Righteousness) | 86 | 17% | 9% |
| M05 (Love) | M22 (Praise) | 85 | 7% | 6% |
| M23 (Strength) | M37 (Calling) | 83 | 4% | 8% |
| M05 (Love) | M13 (Truth) | 81 | 7% | 12% |
| M10 (Sin) | M23 (Strength) | 80 | 6% | 4% |
| M04 (Joy) | M05 (Love) | 78 | 7% | 6% |
| M04 (Joy) | M15 (Wisdom) | 76 | 7% | 5% |
| M02 (Anger) | M23 (Strength) | 75 | 12% | 4% |
| M13 (Truth) | M26 (Righteousness) | 75 | 11% | 8% |
| M10 (Sin) | M38 (Salvation) | 75 | 6% | 21% |
| M12 (Purity) | M23 (Strength) | 74 | 8% | 3% |
| M15 (Wisdom) | M26 (Righteousness) | 72 | 5% | 8% |
| M08 (Pride) | M23 (Strength) | 71 | 11% | 3% |
| M15 (Wisdom) | M41 (Remembrance) | 71 | 5% | 7% |
| M15 (Wisdom) | M37 (Calling) | 69 | 5% | 6% |
| M04 (Joy) | M23 (Strength) | 67 | 6% | 3% |
| M10 (Sin) | M10b (Wickedness) | 65 | 5% | 13% |
| M23 (Strength) | M41 (Remembrance) | 65 | 3% | 7% |
| M23 (Strength) | M36 (Service) | 65 | 3% | 11% |
| M23 (Strength) | M26 (Righteousness) | 64 | 3% | 7% |
| M03 (Grief) | M04 (Joy) | 63 | 7% | 6% |
| M05 (Love) | M15 (Wisdom) | 63 | 5% | 4% |
| M10 (Sin) | M15 (Wisdom) | 62 | 5% | 4% |
| M05 (Love) | M39 (Blessing) | 60 | 5% | 8% |
| M10 (Sin) | M30 (Obedience) | 60 | 5% | 7% |
| M10 (Sin) | M41 (Remembrance) | 59 | 5% | 6% |
| M23 (Strength) | M39 (Blessing) | 59 | 3% | 8% |
| M23 (Strength) | M33 (Peace) | 57 | 3% | 9% |
| M03 (Grief) | M24 (Weakness) | 57 | 7% | 8% |
| M04 (Joy) | M26 (Righteousness) | 57 | 5% | 6% |
| M12 (Purity) | M22 (Praise) | 57 | 7% | 4% |
| M23 (Strength) | M25 (Life) | 56 | 3% | 7% |
| M01 (Fear) | M15 (Wisdom) | 56 | 6% | 4% |
| M05 (Love) | M37 (Calling) | 55 | 4% | 5% |
| M10 (Sin) | M22 (Praise) | 54 | 4% | 4% |
| M03 (Grief) | M23 (Strength) | 53 | 6% | 2% |
| M15 (Wisdom) | M17 (Counsel) | 53 | 4% | 19% |
| M15 (Wisdom) | M30 (Obedience) | 53 | 4% | 6% |
| M04 (Joy) | M39 (Blessing) | 52 | 5% | 7% |

_Full 46×46 matrix (diagonal = cluster's own verse count): `wa-cross-cluster-cooccurrence-v1-20260608-matrix.csv`._