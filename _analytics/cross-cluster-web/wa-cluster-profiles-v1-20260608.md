# Per-cluster L1 profile — qualifier + scenario (roll-up angles 2 & 4)

> READ-ONLY (`scripts/_assess_cluster_profiles.py`). Correlates to the co-occurrence matrix (angle 1). **S5** = cross-cluster verses · **S3** = verses with ≥2 of the cluster's own terms · **S4** = verses where a T2 qualifier co-occurs. No DB writes.

| Cluster | verses | S5 cross % | S3 multi-same % | S4 qualifier % | top qualifiers (verses) |
|---|---|---|---|---|---|
| M01 (Fear) | 930 | 64% | 10% | 45% | al 39, am 26, a.ni 23, bo 19 |
| M02 (Anger) | 634 | 68% | 10% | 53% | aph 136, lo 14, am 13, al 13 |
| M03 (Grief) | 857 | 65% | 11% | 46% | gam 24, a.ni 23, am 22, ma.tsa 18 |
| M04 (Joy) | 1098 | 66% | 11% | 41% | gam 27, a.sah 27, ma.tsa 21, lo 21 |
| M05 (Love) | 1245 | 67% | 22% | 31% | o.lam 24, at.ten 19, aph 19, lo 17 |
| M06 (Hate) | 414 | 74% | 6% | 48% | yad 12, gam 11, aph 10, o.lam 10 |
| M07 (Shame) | 318 | 72% | 15% | 44% | gam 15, hem.mah 8, a.dam 8, ra.ah 7 |
| M08 (Pride) | 633 | 63% | 7% | 41% | o.rekh 23, te.ru.mah 17, min- 10, at.ten 9 |
| M09 (Humility) | 108 | 67% | 2% | 25% | men 3, splanchnon 2, a.sah 2, yad 2 |
| M10 (Sin) | 1252 | 70% | 19% | 45% | at.ten 24, lo 22, hu 22, de 20 |
| M10b (Wickedness) | 514 | 77% | 4% | 38% | gam 15, ra.ah 9, yad 8, hen 7 |
| M10c (Defilement) | 248 | 58% | 10% | 43% | ke.li 12, a.dam 9, lo 9, hu 8 |
| M11 (Repentance) | 327 | 76% | 4% | 33% | aph 8, oikia 6, ma.an 5, ophthalmos 5 |
| M12 (Purity) | 872 | 61% | 10% | 50% | hu 26, a.yil 24, a.yil 24, lo 21 |
| M13 (Truth) | 668 | 70% | 4% | 36% | o.lam 16, lo 12, a.sah 12, sha.va 12 |
| M14 (Deceit) | 365 | 75% | 7% | 42% | ed 13, na.vi 12, re.a 11, sha.va 10 |
| M15 (Wisdom) | 1505 | 65% | 12% | 41% | a.ni 45, lo 40, gam 33, am 30 |
| M16 (Folly) | 156 | 72% | 6% | 40% | a.ni 7, mut 6, gam 4, na 4 |
| M17 (Counsel) | 278 | 72% | 1% | 37% | mi 8, a.sah 7, el 7, gam 6 |
| M18 (Hope) | 270 | 64% | 2% | 36% | ma.tsa 6, min- 6, gam 4, el 4 |
| M19 (Trust) | 338 | 71% | 8% | 41% | at.ten 12, a.ni 11, tsur 9, o.lam 7 |
| M20 (Doubt) | 63 | 57% | 6% | 22% | a.ni 2, ma.tsa 2, mut 2, im.ma.di 1 |
| M21 (Prayer) | 522 | 51% | 3% | 31% | na 14, min- 9, me.im 9, mi 6 |
| M22 (Praise) | 1311 | 62% | 10% | 41% | am 30, she.men 26, o.lam 25, a.ni 22 |
| M23 (Strength) | 2127 | 58% | 8% | 41% | am 55, yad 45, yad 36, hu 33 |
| M24 (Weakness) | 757 | 64% | 5% | 43% | yad 19, am 18, hin.neh 14, ma.tsa 13 |
| M25 (Life) | 764 | 68% | 27% | 48% | mut 25, et 23, sha.va 19, ma.vet 19 |
| M26 (Righteousness) | 910 | 71% | 8% | 35% | kai 16, ma.an 16, at.ten 15, de 15 |
| M27 (Evil) | 540 | 71% | 3% | 49% | lo 18, aph 14, ma.tsa 13, gam 13 |
| M28 (Envy) | 506 | 66% | 12% | 47% | lo 13, a.sah 13, mut 11, hu 10 |
| M29 (Desire) | 296 | 71% | 0% | 27% | am 5, min- 5, im 5, dunamai 5 |
| M30 (Obedience) | 860 | 60% | 3% | 45% | ma.an 25, et 20, gam 17, at.tem 16 |
| M31 (Faith) | 304 | 65% | 5% | 20% | kai 17, ek 14, eimi 11, de 8 |
| M33 (Peace) | 643 | 65% | 4% | 40% | re.gel 14, ma.tsa 13, yad 12, ma.qom 10 |
| M34 (Perseverance) | 218 | 73% | 1% | 34% | na.tsah 7, kai 4, lo 4, o.lam 4 |
| M35 (Testing) | 182 | 62% | 7% | 19% | ginomai 6, ek 5, dunamai 5, kai 3 |
| M36 (Service) | 583 | 60% | 6% | 48% | sha.chah 30, et 22, at.tem 17, am 15 |
| M37 (Calling) | 1091 | 56% | 1% | 47% | ma.qom 54, ya.tsa 40, a.ni 25, at.ten 24 |
| M38 (Salvation) | 353 | 78% | 1% | 38% | dunamai 10, yad 9, o.lam 7, thanatos 6 |
| M39 (Blessing) | 723 | 64% | 3% | 49% | ma.tsa 40, na 23, am 21, ma.an 21 |
| M41 (Remembrance) | 949 | 67% | 2% | 49% | ma.tsa 35, na 27, ra.ah 27, gam 26 |
| M42 (Speech) | 511 | 60% | 3% | 39% | hem.mah 16, na.vi 16, aleimma 11, am 10 |
| M43 (Prophecy) | 143 | 59% | 1% | 36% | am 5, a.sah 4, yad 4, a.dam 4 |
| M44 (Relational) | 622 | 82% | 3% | 50% | yad 31, at.tem 19, sha.va 16, at.ten 13 |
| M45 (Transformation) | 173 | 82% | 2% | 32% | aph 5, a.sah 4, ma.vet 4, na 4 |
| M46 (Abundance) | 271 | 73% | 7% | 39% | gam 8, ma.tsa 6, a.ni 5, bo 5 |

## Top qualifiers by cluster-reach (angle 2)

| Qualifier (T2) | clusters reached | total qualifier-verses |
|---|---|---|
| am | 42 | 484 |
| lo | 42 | 461 |
| a.sah | 42 | 377 |
| ra.ah | 42 | 318 |
| yad | 42 | 318 |
| at.ten | 41 | 433 |
| yad | 41 | 373 |
| hin.neh | 41 | 327 |
| bo | 41 | 299 |
| a.ni | 40 | 438 |
| aph | 40 | 405 |
| ma.tsa | 40 | 393 |
| hu | 40 | 362 |
| el | 40 | 352 |
| o.lam | 40 | 342 |
| dunamai | 40 | 135 |
| gam | 39 | 458 |
| min- | 39 | 316 |
| mut | 39 | 274 |
| hem.mah | 39 | 239 |
