# Keyword corpus — directional assessment

> READ-ONLY (`scripts/_assess_keyword_corpus_report.py`) over the preliminary P1 map. A general read on vocabulary size, distribution, generic-vs-discriminating, residual noise, and per-cluster signature strength. No DB writes.

## Scale
- **1660 terms · 12059 allocations · 4019 distinct keywords** (7.3 avg/term).
- **Hapax: 2046 (51%)** of the vocabulary appears on only one term (the long tail).
- Terms with **zero** keywords: 0.

## Genericness — in how many clusters does each keyword appear?

| spread | # keywords | reading |
|---|---|---|
| 1 clusters | 2585 | **cluster-signature** (discriminating) |
| 2-3 clusters | 1065 | near-signature |
| 4-9 clusters | 329 | shared theme |
| 10-19 clusters | 32 | generic |
| 20+ clusters | 8 | **near-universal** (low value) |

## Most frequent keywords (the backbone vocabulary)

| keyword | # terms | # clusters |
|---|---|---|
| make ⚠glue | 85 | 34 |
| primarily | 79 | 34 |
| god | 71 | 25 |
| cause ⚠glue | 57 | 23 |
| give ⚠glue | 51 | 22 |
| passive | 48 | 24 |
| one's | 48 | 23 |
| mind | 45 | 21 |
| strength | 44 | 3 |
| act ⚠glue | 43 | 19 |
| oneself | 39 | 16 |
| power | 39 | 8 |
| desire | 38 | 9 |
| strong | 36 | 7 |
| put ⚠glue | 36 | 16 |
| good ⚠glue | 33 | 15 |
| take ⚠glue | 32 | 14 |
| become ⚠glue | 31 | 16 |
| fear | 28 | 4 |
| terror | 28 | 3 |
| means | 27 | 19 |
| praise | 27 | 7 |
| sin | 27 | 8 |
| thought | 26 | 7 |
| call ⚠glue | 26 | 5 |
| evil | 25 | 13 |
| show | 25 | 14 |
| person | 24 | 15 |
| keep ⚠glue | 24 | 10 |
| purpose | 24 | 8 |
| moral | 23 | 15 |
| distress | 23 | 4 |
| place ⚠glue | 23 | 16 |
| implication | 23 | 15 |
| set ⚠glue | 23 | 11 |

**Residual noise gauge:** 12 of the top-50 keywords are low-content glue words (make, cause, give, act, put, good, take, become, call, keep, place, set).

## Per-cluster signature strength

| Cluster | distinct kw | unique-to-cluster | % unique | top signature keywords |
|---|---|---|---|---|
| M01 (Fear) | 182 | 79 | 43% | trembling, dread, fearful, terrified, dismay, dreadful |
| M02 (Anger) | 170 | 70 | 41% | anger, irritate, enraged, heat, quarrel, displeasure |
| M03 (Grief) | 225 | 74 | 33% | groaning, mourn, bewail, weeping, sorrowful, tormented |
| M04 (Joy) | 163 | 62 | 38% | pleasantness, cheerful, cheerfulness, marvel, approve, mirth |
| M05 (Love) | 459 | 168 | 37% | gentleness, building, meekness, manifest, mildness, kiss |
| M06 (Hate) | 84 | 38 | 45% | abhor, hate, opponent, hating, loathe, aversion |
| M07 (Shame) | 136 | 59 | 43% | disgrace, dishonor, dishonour, ignominy, dishonorable, abuse |
| M08 (Pride) | 150 | 70 | 47% | proud, boasting, presumptuous, haughtiness, haughty, proudly |
| M09 (Humility) | 106 | 33 | 31% | humbleness, lowliness, submissiveness, required, ordered, precise |
| M10 (Sin) | 197 | 75 | 38% | perversity, unjust, sin-offering, trespass, unrighteous, contrary |
| M10b (Wickedness) | 96 | 23 | 24% | malignity, badness, surprising, inopportune, unsuitable, absurd |
| M10c (Defilement) | 31 | 8 | 26% | defilement, lewd, defiling, soil, sully, contaminate |
| M11 (Repentance) | 139 | 34 | 24% | pardon, release, abandon, tolerate, dismiss, emit |
| M12 (Purity) | 227 | 86 | 38% | dedicate, consecrate, devote, clean, wholesome, sanctify |
| M13 (Truth) | 122 | 42 | 34% | truly, sureness, reliability, stability, continuance, reliableness |
| M14 (Deceit) | 174 | 80 | 46% | treachery, fraud, deception, deceitful, deceive, cunning |
| M15 (Wisdom) | 390 | 148 | 38% | invent, imagine, accounted, computed, imputed, knowing |
| M16 (Folly) | 102 | 43 | 42% | madness, fool, rave, insane, insanity, stupid |
| M17 (Counsel) | 111 | 47 | 42% | counsellor, counselor, council, origin, position, domain |
| M18 (Hope) | 107 | 33 | 31% | looking, aspire, tarry, untroubled, solicitude, despond |
| M19 (Trust) | 133 | 34 | 26% | refuge, continence, temperate, protection, shelter, staff |
| M20 (Doubt) | 50 | 13 | 26% | perplexed, perplexity, discouraged, puzzled, double-minded, inconstant |
| M21 (Prayer) | 177 | 46 | 26% | pray, supplicate, according, listened, prayers, intercession |
| M22 (Praise) | 214 | 76 | 36% | sanctity, glorious, ornament, splendour, sanctification, requiring |
| M23 (Strength) | 506 | 212 | 42% | dominion, powerful, domineer, kingly, reign, overcome |
| M24 (Weakness) | 277 | 112 | 40% | crush, illness, infirmity, infirm, inefficient, crushing |
| M25 (Life) | 110 | 41 | 37% | breath, alive, commonly, perceived, immaterial, inner |
| M26 (Righteousness) | 231 | 79 | 34% | justice, just, sentence, uprightness, fitting, justification |
| M27 (Evil) | 120 | 52 | 43% | idols, heathen, sacrificed, desolation, torturer, inquisitor |
| M28 (Envy) | 165 | 66 | 40% | fornication, intemperance, lustfulness, debauchery, avaricious, avarice |
| M29 (Desire) | 70 | 21 | 30% | willingness, self-chosen, initiative, chooses, spontaneously, sets |
| M30 (Obedience) | 132 | 46 | 35% | stubbornness, restrain, refrain, obstinacy, ward, protect |
| M31 (Faith) | 126 | 30 | 24% | system, based, follow, faithlessness, little, hardheartedness |
| M33 (Peace) | 194 | 56 | 29% | tranquillity, welfare, contentment, tranquil, concord, quietness |
| M34 (Perseverance) | 195 | 42 | 22% | persevere, dare, combatant, games, risk, outright |
| M35 (Testing) | 167 | 55 | 33% | test, attempt, stumble, testing, temptation, tempt |
| M36 (Service) | 82 | 37 | 45% | serve, slavery, servitude, subjects, worked, tilled |
| M37 (Calling) | 137 | 43 | 31% | named, read, meet, recite, endow, proclaimed |
| M38 (Salvation) | 93 | 35 | 38% | propitiation, forgiven, atoning, traditionally, danger, saving |
| M39 (Blessing) | 119 | 17 | 14% | gratify, graciously, endowment, favourable, gracefulness, approval |
| M41 (Remembrance) | 131 | 38 | 29% | remember, obeyed, proclamation, recollect, recollection, news |
| M42 (Speech) | 111 | 30 | 27% | exclaim, prophesy, growl, outcry, roaring, qol |
| M43 (Prophecy) | 81 | 22 | 27% | explain, prophecy, differentiation, separation, estimating, likeness |
| M44 (Relational) | 73 | 24 | 33% | sister, countrywoman, kinswoman, relative, oneness, confess |
| M45 (Transformation) | 137 | 43 | 31% | transform, changed, past, undergo, elements, composing |
| M46 (Abundance) | 119 | 43 | 36% | abundantly, enriched, enrich, beggar, self-sufficient, sufficient |

## Directional verdict
- **64%** of the vocabulary is cluster-signature (1 cluster); only **1%** is generic (10+ clusters) → the keyword layer **does discriminate**.
- Residual glue in the top band (12/50) is the main quality drag → the source-clean would lift signal, but the layer is **directionally usable now**.