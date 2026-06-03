# OWNER Term Primacy Tiering

_Generated 2026-05-03T06:39:31Z_  ·  source: `scripts/_exploratory_term_primacy_tiering_v1_20260503.py`

Every active OWNER term is classified into one of four tiers based on the rule in the script header. Re-run the script to refresh after DB changes; tweak the rule in `classify()` to refine.

## Tier rule (applied in this order; first match wins)

| Tier | Label | Rule |
|---|---|---|
| **U** | Unanalysed | zero active `verse_context` rows for this term (row presence is authoritative; `mti_terms.vc_status` is stale on most rows and is NOT used) |
| **C** | Marginal | `mti_terms.status` in (`extracted_thin`, `candidate_delete`, `phase2_enrichment`) **or** zero groups & zero anchors **or** anchors=0 & vc_relevant<3 |
| **A** | Primary | `status='extracted_theological_anchor'` **or** anchors≥2 & groups≥1 & vc_relevant≥10 **or** anchors≥1 & groups≥2 & vc_relevant≥20 |
| **B** | Secondary | everything else (the substantive middle) |

## Programme totals

Active OWNER terms classified: **2,617**

| Tier | Label | Count | % |
|---|---|---:|---:|
| **A** | Primary | 622 | 23.8% |
| **B** | Secondary | 1,291 | 49.3% |
| **C** | Marginal | 394 | 15.1% |
| **U** | Unanalysed | 310 | 11.8% |

## By language

| Tier | Hebrew | Greek |
|---|---:|---:|
| A Primary | 424 | 198 |
| B Secondary | 716 | 575 |
| C Marginal | 255 | 139 |
| U Unanalysed | 237 | 73 |

## By cluster

Counts per cluster across the four tiers (registries grouped by their `cluster_assignment` from `word_registry`).

| Cluster | A | B | C | U | total |
|---|---:|---:|---:|---:|---:|
| `C01` | 40 | 68 | 28 | 13 | 149 |
| `C02` | 44 | 63 | 34 | 9 | 150 |
| `C03` | 22 | 44 | 25 | 3 | 94 |
| `C04` | 36 | 41 | 27 | 9 | 113 |
| `C05` | 41 | 143 | 11 | 57 | 252 |
| `C06` | 30 | 83 | 22 | 8 | 143 |
| `C07` | 15 | 51 | 9 | 6 | 81 |
| `C08` | 19 | 45 | 21 | 4 | 89 |
| `C09` | 25 | 55 | 7 | 20 | 107 |
| `C10` | 18 | 31 | 3 | 7 | 59 |
| `C11` | 22 | 72 | 9 | 13 | 116 |
| `C12` | 18 | 52 | 0 | 12 | 82 |
| `C13` | 29 | 49 | 37 | 4 | 119 |
| `C14` | 26 | 30 | 4 | 20 | 80 |
| `C15` | 38 | 52 | 13 | 7 | 110 |
| `C16` | 29 | 62 | 9 | 35 | 135 |
| `C17` | 66 | 94 | 42 | 23 | 225 |
| `C18` | 6 | 26 | 3 | 10 | 45 |
| `C19` | 17 | 36 | 11 | 9 | 73 |
| `C20` | 62 | 155 | 67 | 36 | 320 |
| `C21` | 8 | 13 | 8 | 0 | 29 |
| `C22` | 11 | 26 | 4 | 5 | 46 |

## Per-registry tier composition

Each registry's OWNER term portfolio at a glance. Registries are listed in `no` order. The `archetype` column flags structural patterns:

- **single-pillar** — exactly one Primary, the rest Secondary/Marginal
- **multi-pillar** — two or more Primary terms
- **distributed** — no Primary; analytical weight spread across Secondary terms
- **thin** — only Marginal terms
- **unanalysed** — only Unanalysed terms
- **mixed-no-primary** — a mix without any Primary

| Reg | Word | A | B | C | U | total | archetype |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | abomination | 2 | 13 | 0 | 3 | 18 | multi-pillar |
| 2 | agony | 0 | 20 | 3 | 6 | 29 | distributed |
| 3 | ambition | 0 | 4 | 4 | 0 | 8 | distributed |
| 4 | anger | 8 | 24 | 3 | 0 | 35 | multi-pillar |
| 5 | anguish | 6 | 20 | 1 | 18 | 45 | multi-pillar |
| 6 | anointing | 4 | 18 | 0 | 31 | 53 | multi-pillar |
| 7 | anxiety | 1 | 4 | 5 | 0 | 10 | single-pillar |
| 8 | appetite | 2 | 3 | 6 | 0 | 11 | multi-pillar |
| 11 | awe | 3 | 3 | 3 | 0 | 9 | multi-pillar |
| 13 | bitterness | 0 | 10 | 1 | 0 | 11 | distributed |
| 15 | boastfulness | 2 | 1 | 6 | 0 | 9 | multi-pillar |
| 16 | boldness | 1 | 1 | 3 | 0 | 5 | single-pillar |
| 17 | bondage | 2 | 6 | 0 | 0 | 8 | multi-pillar |
| 18 | brokenness | 1 | 3 | 2 | 1 | 7 | single-pillar |
| 19 | calling | 7 | 9 | 10 | 0 | 26 | multi-pillar |
| 20 | character | 1 | 3 | 0 | 0 | 4 | single-pillar |
| 23 | compassion | 4 | 4 | 10 | 1 | 19 | multi-pillar |
| 24 | condemnation | 2 | 4 | 7 | 0 | 13 | multi-pillar |
| 26 | conscience | 1 | 4 | 3 | 0 | 8 | single-pillar |
| 28 | consecration | 4 | 10 | 6 | 0 | 20 | multi-pillar |
| 29 | contentment | 0 | 2 | 0 | 0 | 2 | distributed |
| 30 | contrition | 0 | 6 | 4 | 0 | 10 | distributed |
| 31 | corruption | 3 | 7 | 7 | 0 | 17 | multi-pillar |
| 32 | counsel | 5 | 5 | 2 | 0 | 12 | multi-pillar |
| 33 | courage | 3 | 9 | 13 | 0 | 25 | multi-pillar |
| 34 | covenant | 6 | 1 | 8 | 0 | 15 | multi-pillar |
| 35 | covetousness | 1 | 0 | 6 | 0 | 7 | single-pillar |
| 39 | debauchery | 2 | 3 | 0 | 0 | 5 | multi-pillar |
| 40 | deceit | 1 | 14 | 2 | 0 | 17 | single-pillar |
| 41 | defilement | 0 | 2 | 0 | 0 | 2 | distributed |
| 42 | delight | 3 | 12 | 15 | 0 | 30 | multi-pillar |
| 43 | desire | 19 | 19 | 9 | 5 | 52 | multi-pillar |
| 44 | despair | 3 | 4 | 8 | 0 | 15 | multi-pillar |
| 46 | devotion | 0 | 5 | 0 | 0 | 5 | distributed |
| 47 | dignity | 1 | 5 | 0 | 1 | 7 | single-pillar |
| 49 | discernment | 0 | 5 | 0 | 3 | 8 | distributed |
| 50 | disobedience | 0 | 3 | 0 | 0 | 3 | distributed |
| 51 | distress | 16 | 42 | 3 | 15 | 76 | multi-pillar |
| 52 | division | 2 | 13 | 3 | 7 | 25 | multi-pillar |
| 53 | dread | 2 | 0 | 1 | 2 | 5 | multi-pillar |
| 55 | endurance | 1 | 2 | 0 | 1 | 4 | single-pillar |
| 56 | envy | 4 | 6 | 4 | 1 | 15 | multi-pillar |
| 57 | evil | 5 | 17 | 0 | 4 | 26 | multi-pillar |
| 58 | experience | 2 | 2 | 0 | 1 | 5 | multi-pillar |
| 59 | faith | 8 | 2 | 8 | 0 | 18 | multi-pillar |
| 60 | faithfulness | 1 | 0 | 0 | 0 | 1 | mixed-no-primary |
| 61 | fear | 12 | 41 | 7 | 2 | 62 | multi-pillar |
| 62 | fellowship | 1 | 8 | 4 | 0 | 13 | single-pillar |
| 63 | foolishness | 4 | 8 | 0 | 0 | 12 | multi-pillar |
| 64 | forgiveness | 5 | 2 | 0 | 0 | 7 | multi-pillar |
| 65 | generosity | 1 | 1 | 4 | 0 | 6 | single-pillar |
| 66 | gentleness | 1 | 4 | 0 | 0 | 5 | single-pillar |
| 67 | goodness | 0 | 2 | 1 | 0 | 3 | distributed |
| 68 | grace | 3 | 1 | 1 | 0 | 5 | multi-pillar |
| 69 | gratitude | 1 | 2 | 0 | 0 | 3 | single-pillar |
| 70 | greed | 1 | 2 | 0 | 0 | 3 | single-pillar |
| 71 | grief | 5 | 13 | 0 | 0 | 18 | multi-pillar |
| 72 | groaning | 2 | 7 | 1 | 0 | 10 | multi-pillar |
| 73 | guilt | 9 | 13 | 0 | 0 | 22 | multi-pillar |
| 74 | hardness | 0 | 2 | 0 | 4 | 6 | distributed |
| 75 | hatred | 1 | 2 | 1 | 1 | 5 | single-pillar |
| 76 | holiness | 3 | 3 | 1 | 1 | 8 | multi-pillar |
| 77 | honesty | 2 | 0 | 0 | 0 | 2 | multi-pillar |
| 78 | hope | 9 | 6 | 11 | 1 | 27 | multi-pillar |
| 80 | humility | 3 | 9 | 0 | 0 | 12 | multi-pillar |
| 81 | hypocrisy | 1 | 4 | 0 | 0 | 5 | single-pillar |
| 83 | idolatry | 1 | 5 | 0 | 0 | 6 | single-pillar |
| 85 | imagination | 0 | 3 | 0 | 0 | 3 | distributed |
| 86 | impurity | 6 | 6 | 0 | 3 | 15 | multi-pillar |
| 87 | indignation | 0 | 2 | 0 | 0 | 2 | distributed |
| 89 | iniquity | 3 | 6 | 0 | 0 | 9 | multi-pillar |
| 90 | innocence | 7 | 8 | 0 | 7 | 22 | multi-pillar |
| 91 | insight | 1 | 1 | 0 | 0 | 2 | single-pillar |
| 92 | integrity | 0 | 3 | 0 | 0 | 3 | distributed |
| 93 | intention | 0 | 1 | 0 | 0 | 1 | distributed |
| 94 | intercession | 1 | 3 | 0 | 0 | 4 | single-pillar |
| 96 | jealousy | 0 | 1 | 0 | 0 | 1 | distributed |
| 97 | joy | 10 | 15 | 4 | 1 | 30 | multi-pillar |
| 98 | justice | 10 | 6 | 16 | 4 | 36 | multi-pillar |
| 99 | kindness | 7 | 9 | 0 | 6 | 22 | multi-pillar |
| 100 | knowledge | 3 | 4 | 1 | 0 | 8 | multi-pillar |
| 102 | longing | 5 | 8 | 0 | 2 | 15 | multi-pillar |
| 103 | love | 19 | 28 | 7 | 3 | 57 | multi-pillar |
| 105 | lust | 2 | 4 | 0 | 0 | 6 | multi-pillar |
| 107 | meaning | 0 | 10 | 0 | 1 | 11 | distributed |
| 108 | meditation | 1 | 4 | 0 | 0 | 5 | single-pillar |
| 110 | memory | 1 | 1 | 0 | 0 | 2 | single-pillar |
| 111 | mercy | 8 | 11 | 6 | 0 | 25 | multi-pillar |
| 112 | mind | 13 | 29 | 12 | 3 | 57 | multi-pillar |
| 113 | mourning | 2 | 7 | 0 | 1 | 10 | multi-pillar |
| 114 | obedience | 1 | 1 | 0 | 0 | 2 | single-pillar |
| 115 | passion | 0 | 3 | 0 | 0 | 3 | distributed |
| 116 | patience | 8 | 3 | 0 | 3 | 14 | multi-pillar |
| 117 | peace | 13 | 30 | 6 | 13 | 62 | multi-pillar |
| 120 | perverseness | 2 | 8 | 0 | 6 | 16 | multi-pillar |
| 121 | praise | 10 | 22 | 0 | 3 | 35 | multi-pillar |
| 122 | prayer | 4 | 2 | 1 | 0 | 7 | multi-pillar |
| 123 | pride | 13 | 29 | 0 | 10 | 52 | multi-pillar |
| 124 | prophecy | 5 | 5 | 0 | 0 | 10 | multi-pillar |
| 125 | purity | 3 | 9 | 0 | 0 | 12 | multi-pillar |
| 126 | purpose | 4 | 2 | 5 | 0 | 11 | multi-pillar |
| 127 | reasoning | 1 | 2 | 0 | 0 | 3 | single-pillar |
| 128 | rebellion | 5 | 15 | 0 | 1 | 21 | multi-pillar |
| 130 | reconciliation | 0 | 6 | 0 | 0 | 6 | distributed |
| 131 | rejection | 0 | 2 | 0 | 1 | 3 | distributed |
| 132 | rejoicing | 0 | 1 | 0 | 0 | 1 | distributed |
| 134 | renewal | 0 | 3 | 4 | 0 | 7 | distributed |
| 135 | repentance | 5 | 5 | 1 | 0 | 11 | multi-pillar |
| 139 | righteousness | 1 | 0 | 0 | 0 | 1 | mixed-no-primary |
| 140 | seeking | 3 | 2 | 0 | 1 | 6 | multi-pillar |
| 142 | self-control | 1 | 11 | 1 | 0 | 13 | single-pillar |
| 146 | shame | 8 | 19 | 1 | 1 | 29 | multi-pillar |
| 147 | sin | 2 | 7 | 0 | 3 | 12 | multi-pillar |
| 148 | sincerity | 0 | 2 | 0 | 0 | 2 | distributed |
| 149 | slander | 2 | 12 | 0 | 3 | 17 | multi-pillar |
| 150 | sorcery | 0 | 4 | 0 | 1 | 5 | distributed |
| 151 | sorrow | 7 | 26 | 1 | 14 | 48 | multi-pillar |
| 152 | strife | 1 | 8 | 0 | 1 | 10 | single-pillar |
| 153 | stubbornness | 0 | 1 | 1 | 2 | 4 | distributed |
| 155 | submission | 1 | 1 | 0 | 0 | 2 | single-pillar |
| 156 | surrender | 0 | 1 | 0 | 11 | 12 | distributed |
| 157 | temptation | 3 | 9 | 0 | 3 | 15 | multi-pillar |
| 158 | terror | 0 | 8 | 0 | 3 | 11 | distributed |
| 159 | testimony | 3 | 5 | 0 | 1 | 9 | multi-pillar |
| 160 | thought | 8 | 10 | 6 | 3 | 27 | multi-pillar |
| 162 | transgression | 2 | 6 | 0 | 0 | 8 | multi-pillar |
| 163 | trust | 3 | 2 | 3 | 0 | 8 | multi-pillar |
| 164 | truthfulness | 1 | 4 | 0 | 0 | 5 | single-pillar |
| 165 | unbelief | 1 | 1 | 1 | 0 | 3 | single-pillar |
| 166 | understanding | 2 | 5 | 0 | 0 | 7 | multi-pillar |
| 167 | unity | 3 | 3 | 0 | 1 | 7 | multi-pillar |
| 168 | uprightness | 3 | 3 | 2 | 0 | 8 | multi-pillar |
| 170 | weakness | 3 | 2 | 0 | 3 | 8 | multi-pillar |
| 171 | whoredom | 1 | 2 | 0 | 0 | 3 | single-pillar |
| 172 | wickedness | 3 | 2 | 0 | 0 | 5 | multi-pillar |
| 173 | will | 12 | 12 | 4 | 4 | 32 | multi-pillar |
| 174 | wisdom | 10 | 11 | 2 | 1 | 24 | multi-pillar |
| 175 | wonder | 2 | 5 | 0 | 1 | 8 | multi-pillar |
| 176 | worship | 9 | 18 | 0 | 3 | 30 | multi-pillar |
| 177 | worth | 3 | 7 | 1 | 5 | 16 | multi-pillar |
| 178 | wrath | 0 | 5 | 0 | 4 | 9 | distributed |
| 179 | yearning | 0 | 0 | 1 | 0 | 1 | thin |
| 180 | yielding | 10 | 9 | 0 | 5 | 24 | multi-pillar |
| 181 | zeal | 2 | 1 | 0 | 0 | 3 | multi-pillar |
| 182 | Soul | 6 | 10 | 2 | 1 | 19 | multi-pillar |
| 183 | heart | 9 | 12 | 3 | 6 | 30 | multi-pillar |
| 184 | spirit | 6 | 6 | 1 | 0 | 13 | multi-pillar |
| 185 | flesh | 5 | 5 | 4 | 2 | 16 | multi-pillar |
| 186 | gladness | 2 | 2 | 1 | 1 | 6 | multi-pillar |
| 187 | strength | 32 | 97 | 27 | 26 | 182 | multi-pillar |
| 188 | weeping | 2 | 5 | 0 | 2 | 9 | multi-pillar |
| 189 | malice | 0 | 1 | 0 | 0 | 1 | distributed |
| 190 | contempt | 4 | 7 | 0 | 0 | 11 | multi-pillar |
| 191 | doubt | 5 | 10 | 1 | 1 | 17 | multi-pillar |
| 192 | comfort | 1 | 2 | 2 | 0 | 5 | single-pillar |
| 193 | craving | 1 | 2 | 0 | 1 | 4 | single-pillar |
| 194 | blessing | 3 | 1 | 0 | 0 | 4 | multi-pillar |
| 196 | power | 4 | 8 | 2 | 0 | 14 | multi-pillar |
| 197 | authority | 18 | 24 | 25 | 4 | 71 | multi-pillar |
| 198 | might | 5 | 12 | 0 | 5 | 22 | multi-pillar |
| 199 | dominion | 3 | 14 | 13 | 1 | 31 | multi-pillar |
| 201 | image | 3 | 3 | 0 | 2 | 8 | multi-pillar |
| 202 | transformation | 1 | 2 | 0 | 0 | 3 | single-pillar |
| 203 | treachery | 0 | 1 | 0 | 0 | 1 | distributed |
| 204 | name | 3 | 0 | 0 | 0 | 3 | multi-pillar |
| 206 | vulnerability | 4 | 9 | 0 | 4 | 17 | multi-pillar |
| 207 | blindness (spiritual) | 3 | 4 | 0 | 0 | 7 | multi-pillar |
| 208 | sloth | 2 | 5 | 0 | 0 | 7 | multi-pillar |
| 209 | likeness | 0 | 2 | 0 | 0 | 2 | distributed |
| 210 | deadness | 4 | 4 | 4 | 0 | 12 | multi-pillar |
| 211 | being | 1 | 6 | 6 | 1 | 14 | single-pillar |
| 212 | pray | 0 | 1 | 1 | 0 | 2 | distributed |
| 213 | listen | 8 | 9 | 18 | 2 | 37 | multi-pillar |

### Archetype summary across 214 registries

| Archetype | n |
|---|---:|
| multi-pillar | 105 |
| single-pillar | 33 |
| distributed | 32 |
| mixed-no-primary | 2 |
| thin | 1 |

## All Primary (Tier A) terms — full list

Ordered by anchor count, then vc_relevant.

| reg | word | strongs | translit | gloss | lang | status | anchors | groups | vc_rel | xref→ |
|---:|---|---|---|---|---|---|---:|---:|---:|---:|
| 58 | experience | `H7200G` | ra.ah | to see: see | H | `extracted` | 20 | 10 | 165 | 0 |
| 57 | evil | `H4310` | mi | who? | H | `extracted` | 20 | 10 | 62 | 1 |
| 183 | heart | `H3820A` | lev | heart | H | `extracted` | 16 | 8 | 361 | 5 |
| 198 | might | `H0935G` | bo | to come [in]: come | H | `extracted` | 16 | 3 | 126 | 0 |
| 60 | faithfulness | `H5414G` | na.tan | to give: give | H | `extracted` | 14 | 7 | 120 | 2 |
| 90 | innocence | `H2009` | hin.neh | behold | H | `extracted` | 14 | 7 | 98 | 0 |
| 180 | yielding | `G3860` | paradidōmi | to deliver | G | `extracted` | 14 | 12 | 83 | 0 |
| 147 | sin | `H0408` | al | not | H | `extracted` | 14 | 9 | 76 | 2 |
| 57 | evil | `H3605` | kol | all | H | `extracted` | 14 | 7 | 41 | 0 |
| 117 | peace | `H7965G` | sha.lom | peace | H | `extracted` | 13 | 4 | 83 | 2 |
| 182 | Soul | `H5315G` | ne.phesh | soul | H | `extracted` | 12 | 12 | 179 | 7 |
| 187 | strength | `H3966` | me.od | much | H | `extracted` | 12 | 6 | 93 | 0 |
| 90 | innocence | `H2005` | hen | look! | H | `extracted` | 12 | 6 | 77 | 0 |
| 185 | flesh | `H1320` | ba.sar | flesh | H | `extracted` | 12 | 6 | 75 | 0 |
| 185 | flesh | `H1321` | be.shar | flesh | H | `extracted` | 12 | 6 | 73 | 0 |
| 117 | peace | `H5117` | nu.ach | to rest | H | `extracted` | 11 | 6 | 58 | 0 |
| 181 | zeal | `G4710` | spoudē | diligence | G | `extracted` | 11 | 11 | 12 | 1 |
| 100 | knowledge | `H3045` | ya.da | to know | H | `extracted` | 10 | 5 | 264 | 1 |
| 183 | heart | `H3824` | le.vav | heart | H | `extracted` | 10 | 10 | 237 | 3 |
| 204 | name | `H8034` | shem | name | H | `extracted` | 10 | 5 | 223 | 1 |
| 103 | love | `G0025` | agapaō | to love | G | `extracted` | 10 | 5 | 130 | 0 |
| 187 | strength | `H3581B` | ko.ach | strength | H | `extracted` | 10 | 5 | 99 | 2 |
| 100 | knowledge | `H1847` | da.at | knowledge | H | `extracted` | 10 | 5 | 87 | 1 |
| 187 | strength | `H5797` | oz | strength | H | `extracted` | 10 | 5 | 68 | 3 |
| 100 | knowledge | `G6063` | oida | to know | G | `extracted` | 10 | 5 | 50 | 0 |
| 180 | yielding | `G0591` | apodidōmi | to pay | G | `extracted` | 10 | 10 | 45 | 0 |
| 117 | peace | `H2790B` | cha.resh | be quiet | H | `extracted` | 10 | 6 | 30 | 1 |
| 187 | strength | `G3614G` | oikia | home | G | `extracted` | 10 | 5 | 24 | 0 |
| 15 | boastfulness | `H3519` | ka.vod | glory | H | `extracted` | 9 | 5 | 179 | 2 |
| 183 | heart | `G2588` | kardia | heart | G | `extracted` | 9 | 9 | 151 | 2 |
| 98 | justice | `H4941G` | mish.pat | justice: judgement | H | `extracted` | 9 | 5 | 114 | 2 |
| 204 | name | `G3686` | onoma | name | G | `extracted` | 9 | 5 | 90 | 0 |
| 182 | Soul | `G5590G` | psuchē | soul | G | `extracted` | 9 | 9 | 46 | 2 |
| 210 | deadness | `G3498` | nekros | dead | G | `extracted` | 9 | 5 | 39 | 0 |
| 197 | authority | `H3027G` | yad | hand | H | `extracted` | 8 | 4 | 255 | 6 |
| 194 | blessing | `H1288` | ba.rakh | to bless | H | `extracted` | 8 | 4 | 247 | 1 |
| 91 | insight | `H0995` | bin | to understand | H | `extracted` | 8 | 4 | 160 | 4 |
| 188 | weeping | `H1058` | ba.khah | to weep | H | `extracted` | 8 | 4 | 99 | 0 |
| 123 | pride | `H7311A` | rum | to exalt | H | `extracted` | 8 | 4 | 85 | 0 |
| 98 | justice | `H8199` | sha.phat | to judge | H | `extracted` | 8 | 4 | 80 | 1 |
| 123 | pride | `H7311B` | ra.mam | be rotten | H | `extracted` | 8 | 4 | 77 | 0 |
| 210 | deadness | `H4194` | ma.vet | death | H | `extracted` | 8 | 4 | 75 | 0 |
| 180 | yielding | `G5204` | hudōr | water | G | `extracted` | 8 | 8 | 68 | 0 |
| 187 | strength | `H2220` | ze.ro.a | arm | H | `extracted` | 8 | 4 | 65 | 1 |
| 199 | dominion | `G0932` | basileia | kingdom | G | `extracted` | 8 | 5 | 65 | 0 |
| 210 | deadness | `H4191` | mut | to die | H | `extracted` | 8 | 4 | 62 | 0 |
| 180 | yielding | `G5342` | ferō | to bear/lead | G | `extracted` | 8 | 8 | 60 | 0 |
| 210 | deadness | `G2288` | thanatos | death | G | `extracted` | 8 | 5 | 51 | 0 |
| 99 | kindness | `H0120G` | a.dam | man | H | `extracted` | 8 | 4 | 48 | 0 |
| 185 | flesh | `H3318G` | ya.tsa | to come out: come | H | `extracted` | 8 | 4 | 46 | 1 |
| 187 | strength | `H6106G` | e.tsem | bone | H | `extracted` | 8 | 4 | 43 | 0 |
| 121 | praise | `G1391` | doxa | glory | G | `extracted` | 8 | 4 | 42 | 0 |
| 187 | strength | `H4725` | ma.qom | place | H | `extracted` | 8 | 4 | 34 | 0 |
| 120 | perverseness | `H2015` | ha.phakh | to overturn | H | `extracted` | 8 | 4 | 33 | 0 |
| 187 | strength | `H2428G` | cha.yil | strength | H | `extracted` | 8 | 4 | 32 | 0 |
| 73 | guilt | `G4893` | suneidesis | conscience | G | `extracted` | 8 | 4 | 29 | 3 |
| 89 | iniquity | `H4480A` | min- | from | H | `extracted` | 8 | 4 | 25 | 2 |
| 184 | spirit | `G4151G` | pneuma | spirit/breath: breath | G | `extracted` | 7 | 7 | 341 | 0 |
| 182 | Soul | `H5315I` | ne.phesh | soul: myself | H | `extracted` | 7 | 7 | 126 | 7 |
| 98 | justice | `H6664G` | tse.deq | righteousness | H | `extracted` | 7 | 4 | 105 | 3 |
| 185 | flesh | `G4561` | sarx | flesh | G | `extracted` | 7 | 4 | 86 | 0 |
| 213 | listen | `G2192` | echō | to have/be | G | `extracted` | 7 | 7 | 43 | 0 |
| 117 | peace | `H8252` | sha.qat | to quiet | H | `extracted` | 7 | 4 | 23 | 0 |
| 103 | love | `H2617A` | che.sed | kindness | H | `extracted` | 6 | 3 | 234 | 8 |
| 61 | fear | `H3372G` | ya.re | to fear: revere | H | `extracted` | 6 | 3 | 185 | 4 |
| 182 | Soul | `H5315H` | ne.phesh | soul: life | H | `extracted` | 6 | 6 | 180 | 7 |
| 43 | desire | `H1245` | ba.qash | to seek | H | `extracted` | 6 | 6 | 172 | 1 |
| 187 | strength | `H0341` | o.yev | enemy | H | `extracted` | 6 | 3 | 141 | 0 |
| 59 | faith | `G4100` | pisteuō | to trust (in) | G | `extracted` | 6 | 3 | 114 | 3 |
| 197 | authority | `H3678G` | kis.se | throne | H | `extracted` | 6 | 3 | 109 | 0 |
| 168 | uprightness | `H3477G` | ya.shar | upright:right | H | `extracted` | 6 | 6 | 107 | 1 |
| 73 | guilt | `G0266` | hamartia | sin | G | `extracted` | 6 | 3 | 105 | 1 |
| 103 | love | `G0026` | agapē | love | G | `extracted` | 6 | 3 | 105 | 0 |
| 196 | power | `H0410G` | el | God | H | `extracted` | 6 | 3 | 102 | 0 |
| 124 | prophecy | `H5012` | na.va | to prophesy | H | `extracted` | 6 | 4 | 90 | 0 |
| 187 | strength | `G1849` | exousia | authority | G | `extracted` | 6 | 3 | 90 | 3 |
| 122 | prayer | `G4336` | proseuchomai | to pray | G | `extracted` | 6 | 3 | 85 | 1 |
| 68 | grace | `G5485` | charis | grace | G | `extracted` | 6 | 4 | 84 | 1 |
| 186 | gladness | `H3190` | ya.tav | be good | H | `extracted` | 6 | 3 | 84 | 0 |
| 61 | fear | `G5399` | fobeō | to fear | G | `extracted` | 6 | 3 | 83 | 2 |
| 111 | mercy | `H3722A` | kip.per | to atone | H | `extracted` | 6 | 3 | 81 | 1 |
| 164 | truthfulness | `G0225` | alētheia | truth | G | `extracted` | 6 | 6 | 76 | 0 |
| 98 | justice | `G1343` | dikaiosunē | righteousness | G | `extracted` | 6 | 3 | 74 | 1 |
| 187 | strength | `H1431` | ga.dal | to magnify | H | `extracted` | 6 | 3 | 74 | 0 |
| 124 | prophecy | `G4396` | profētēs | prophet | G | `extracted` | 6 | 3 | 70 | 0 |
| 59 | faith | `H0571G` | e.met | truth: faithful | H | `extracted` | 6 | 3 | 67 | 4 |
| 197 | authority | `G2962H` | kurios | lord: master | G | `extracted` | 6 | 3 | 64 | 1 |
| 59 | faith | `G4103` | pistos | faithful | G | `extracted` | 6 | 3 | 61 | 3 |
| 43 | desire | `G2212` | zēteō | to seek | G | `extracted` | 6 | 6 | 58 | 1 |
| 44 | despair | `H3808` | lo | not | H | `extracted` | 6 | 6 | 56 | 0 |
| 197 | authority | `G0746` | archē | beginning | G | `extracted` | 6 | 3 | 52 | 1 |
| 173 | will | `H1980G` | ha.lakh | to go: went | H | `extracted` | 6 | 6 | 50 | 1 |
| 59 | faith | `H0530` | e.mu.nah | faithfulness | H | `extracted` | 6 | 3 | 46 | 4 |
| 190 | contempt | `H7043` | qa.lal | to lighten | H | `extracted` | 6 | 3 | 46 | 1 |
| 103 | love | `H0160` | a.ha.vah | love | H | `extracted` | 6 | 3 | 45 | 2 |
| 61 | fear | `G5401` | fobos | fear | G | `extracted` | 6 | 3 | 43 | 2 |
| 61 | fear | `H3374` | yir.ah | fear | H | `extracted` | 6 | 3 | 42 | 3 |
| 173 | will | `H3427` | ya.shav | to dwell | H | `extracted` | 6 | 6 | 40 | 0 |
| 194 | blessing | `G2127` | eulogeō | to praise/bless | G | `extracted` | 6 | 3 | 40 | 0 |
| 59 | faith | `H0898` | ba.gad | to act treacherously | H | `extracted` | 6 | 3 | 39 | 1 |
| 90 | innocence | `H5355A` | na.qi | innocent | H | `extracted` | 6 | 3 | 39 | 0 |
| 90 | innocence | `H5355B` | na.qi | innocent | H | `extracted` | 6 | 3 | 39 | 0 |
| 146 | shame | `H3637` | ka.lam | be humiliated | H | `extracted` | 6 | 3 | 38 | 0 |
| 182 | Soul | `G5590H` | psuchē | soul: life | G | `extracted` | 6 | 6 | 33 | 2 |
| 61 | fear | `H2729` | cha.rad | to tremble | H | `extracted` | 6 | 3 | 32 | 0 |
| 187 | strength | `H5923` | ol | yoke | H | `extracted` | 6 | 3 | 31 | 0 |
| 111 | mercy | `G1653` | eleeō | to have mercy | G | `extracted` | 6 | 3 | 28 | 1 |
| 192 | comfort | `G3874` | paraklēsis | encouragement | G | `extracted` | 6 | 3 | 28 | 3 |
| 124 | prophecy | `G4395` | profēteuō | to prophesy | G | `extracted` | 6 | 3 | 27 | 0 |
| 24 | condemnation | `H4941H` | mish.pat | justice | H | `extracted` | 6 | 3 | 26 | 1 |
| 1 | abomination | `H8441` | to.e.vah | abomination | H | `extracted` | 6 | 5 | 25 | 0 |
| 121 | praise | `H8416` | te.hil.lah | praise | H | `extracted` | 6 | 3 | 22 | 0 |
| 187 | strength | `H5956` | a.lam | to conceal | H | `extracted` | 6 | 3 | 22 | 0 |
| 28 | consecration | `H6942G` | qa.dash | to consecrate: consecate | H | `extracted` | 6 | 3 | 21 | 1 |
| 103 | love | `G5368` | fileō | to love | G | `extracted` | 6 | 3 | 21 | 2 |
| 174 | wisdom | `G4678` | sofia | wisdom | G | `extracted` | 6 | 3 | 20 | 1 |
| 187 | strength | `H5324` | na.tsav | to stand | H | `extracted` | 6 | 3 | 20 | 0 |
| 58 | experience | `G1754` | energeō | be active | G | `extracted` | 6 | 3 | 19 | 1 |
| 99 | kindness | `H5978` | im.ma.di | with me | H | `extracted` | 6 | 3 | 18 | 0 |
| 180 | yielding | `G1435` | dōron | gift | G | `extracted` | 6 | 6 | 17 | 0 |
| 187 | strength | `G3618` | oikodomeō | to build | G | `extracted` | 6 | 3 | 16 | 0 |
| 61 | fear | `H0367` | e.mah | terror | H | `extracted` | 6 | 3 | 15 | 1 |
| 31 | corruption | `H7843` | sha.chat | to ruin | H | `extracted` | 6 | 3 | 14 | 0 |
| 121 | praise | `H0259` | e.chad | one | H | `extracted` | 6 | 4 | 14 | 0 |
| 177 | worth | `H7737A` | sha.vah | be like | H | `extracted` | 6 | 6 | 13 | 0 |
| 99 | kindness | `H5971H` | am | People's [Gate] | H | `extracted` | 5 | 3 | 430 | 0 |
| 99 | kindness | `H5971I` | am | [Ibleam]-am | H | `extracted` | 5 | 3 | 430 | 0 |
| 99 | kindness | `H5971L` | am | people: creatures | H | `extracted` | 5 | 3 | 430 | 0 |
| 184 | spirit | `G0040G` | hagios | holy | G | `extracted` | 5 | 5 | 210 | 1 |
| 172 | wickedness | `H7563` | ra.sha | wicked | H | `extracted` | 5 | 5 | 177 | 0 |
| 34 | covenant | `H1285` | be.rit | covenant | H | `extracted` | 5 | 5 | 161 | 0 |
| 176 | worship | `H7812` | sha.chah | to bow | H | `extracted` | 5 | 3 | 148 | 0 |
| 140 | seeking | `H1875` | da.rash | to seek | H | `extracted` | 5 | 4 | 145 | 0 |
| 97 | joy | `H8055` | sa.mach | to rejoice | H | `extracted` | 5 | 3 | 131 | 3 |
| 43 | desire | `H7592` | sha.al | to ask | H | `extracted` | 5 | 5 | 125 | 1 |
| 43 | desire | `G2309` | thelō | to will/desire | G | `extracted` | 5 | 5 | 120 | 1 |
| 78 | hope | `H0982` | ba.tach | to trust | H | `extracted` | 5 | 3 | 117 | 1 |
| 174 | wisdom | `H2450` | cha.kham | wise | H | `extracted` | 5 | 3 | 110 | 2 |
| 32 | counsel | `H6310G` | peh | lip | H | `extracted` | 5 | 5 | 90 | 0 |
| 33 | courage | `H2388G` | cha.zaq | to strengthen: strengthen | H | `extracted` | 5 | 5 | 90 | 1 |
| 65 | generosity | `G0018` | agathos | good | G | `extracted` | 5 | 5 | 90 | 2 |
| 213 | listen | `H0241G` | o.zen | ear | H | `extracted` | 5 | 5 | 89 | 0 |
| 117 | peace | `G1515` | eirēnē | peace | G | `extracted` | 5 | 3 | 84 | 1 |
| 187 | strength | `G1411` | dunamis | power | G | `extracted` | 5 | 3 | 75 | 3 |
| 171 | whoredom | `H2181` | za.nah | to fornicate | H | `extracted` | 5 | 5 | 73 | 1 |
| 66 | gentleness | `H6031B` | a.nah | to afflict | H | `extracted` | 5 | 4 | 72 | 4 |
| 199 | dominion | `H4910` | ma.shal | to rule | H | `extracted` | 5 | 3 | 69 | 1 |
| 19 | calling | `H7121G` | qa.ra | to call: call to | H | `extracted` | 5 | 3 | 48 | 0 |
| 19 | calling | `G2564G` | kaleō | to call: call | G | `extracted` | 5 | 3 | 46 | 2 |
| 182 | Soul | `H5315L` | ne.phesh | soul: appetite | H | `extracted` | 5 | 5 | 45 | 7 |
| 76 | holiness | `H6944G` | qo.desh | holiness | H | `extracted` | 5 | 3 | 44 | 1 |
| 198 | might | `G1096` | ginomai | to be | G | `extracted` | 5 | 1 | 41 | 0 |
| 123 | pride | `G2744` | kauchaomai | to boast | G | `extracted` | 5 | 3 | 31 | 1 |
| 6 | anointing | `H8081` | she.men | oil | H | `extracted` | 5 | 5 | 28 | 0 |
| 59 | faith | `H4604` | ma.al | unfaithfulness | H | `extracted` | 5 | 3 | 28 | 0 |
| 4 | anger | `H0639G` | aph | face: anger | H | `extracted` | 5 | 5 | 23 | 3 |
| 44 | despair | `H3809` | la | not | H | `extracted` | 5 | 5 | 23 | 1 |
| 184 | spirit | `G4152` | pneumatikos | spiritual | G | `extracted` | 5 | 5 | 21 | 0 |
| 121 | praise | `H3034` | ya.dah | to give thanks | H | `extracted` | 5 | 3 | 19 | 0 |
| 197 | authority | `H7287A` | ra.dah | to rule | H | `extracted` | 5 | 1 | 16 | 1 |
| 198 | might | `G4137` | plēroō | to fulfill | G | `extracted` | 5 | 1 | 16 | 0 |
| 15 | boastfulness | `H3513H` | ka.ved | to honor: heavy | H | `extracted` | 5 | 4 | 15 | 2 |
| 206 | vulnerability | `H6174` | a.rom | naked | H | `extracted` | 5 | 5 | 15 | 0 |
| 117 | peace | `H2814` | cha.shah | be silent | H | `extracted` | 5 | 4 | 14 | 0 |
| 165 | unbelief | `G0544` | apeitheō | to disobey | G | `extracted` | 5 | 5 | 14 | 0 |
| 70 | greed | `G0726` | harpazō | to seize | G | `extracted` | 5 | 5 | 11 | 0 |
| 177 | worth | `H6186B` | a.rakh | to value | H | `extracted` | 5 | 5 | 11 | 0 |
| 204 | name | `G3687` | onomazō | to name | G | `extracted` | 5 | 4 | 10 | 0 |
| 160 | thought | `H2142` | za.khar | to remember | H | `extracted` | 4 | 2 | 205 | 2 |
| 73 | guilt | `H2398` | cha.ta | to sin | H | `extracted` | 4 | 3 | 201 | 1 |
| 77 | honesty | `H6662` | tsad.diq | righteous | H | `extracted` | 4 | 3 | 174 | 2 |
| 183 | heart | `H7130H` | qe.rev | entrails: inner parts | H | `extracted` | 4 | 4 | 168 | 0 |
| 166 | understanding | `H8085G` | sha.ma | to hear: hear | H | `extracted` | 4 | 4 | 163 | 1 |
| 180 | yielding | `H2233H` | ze.ra | seed: children | H | `extracted` | 4 | 4 | 160 | 0 |
| 43 | desire | `H0977` | ba.char | to choose | H | `extracted` | 4 | 4 | 143 | 0 |
| 34 | covenant | `H7650` | sha.va | to swear | H | `extracted` | 4 | 4 | 131 | 0 |
| 11 | awe | `H3372H` | ya.re | to fear: revere | H | `extracted` | 4 | 4 | 113 | 3 |
| 59 | faith | `G4102G` | pistis | faith | G | `extracted` | 4 | 2 | 96 | 3 |
| 197 | authority | `G1410` | dunamai | be able | G | `extracted` | 4 | 2 | 94 | 3 |
| 97 | joy | `H8057` | sim.chah | joy | H | `extracted` | 4 | 2 | 89 | 3 |
| 34 | covenant | `H3772H` | ka.rat | to cut: make [covenant] | H | `extracted` | 4 | 4 | 85 | 0 |
| 32 | counsel | `H6098` | e.tsah | counsel | H | `extracted` | 4 | 4 | 82 | 1 |
| 121 | praise | `H1984B` | ha.lal | to boast: praise | H | `extracted` | 4 | 3 | 82 | 0 |
| 19 | calling | `H7121I` | qa.ra | to call: call out | H | `extracted` | 4 | 2 | 80 | 0 |
| 8 | appetite | `H2421` | cha.yah | to live | H | `extracted` | 4 | 4 | 78 | 0 |
| 112 | mind | `H8104H` | sha.mar | to keep: guard | H | `extracted` | 4 | 2 | 76 | 0 |
| 98 | justice | `G1342` | dikaios | just | G | `extracted` | 4 | 2 | 74 | 1 |
| 140 | seeking | `H4672` | ma.tsa | to find | H | `extracted` | 4 | 4 | 74 | 0 |
| 103 | love | `G0027` | agapētos | beloved | G | `extracted` | 4 | 2 | 72 | 0 |
| 146 | shame | `H2781` | cher.pah | reproach | H | `extracted` | 4 | 2 | 72 | 0 |
| 135 | repentance | `H5162G` | na.cham | to be sorry: comfort | H | `extracted` | 4 | 2 | 66 | 3 |
| 97 | joy | `G5463` | chairo | to rejoice | G | `extracted` | 4 | 2 | 64 | 2 |
| 97 | joy | `G5479` | chara | joy | G | `extracted` | 4 | 2 | 63 | 2 |
| 175 | wonder | `H6381` | pa.la | to wonder | H | `extracted` | 4 | 2 | 63 | 0 |
| 57 | evil | `G4190` | ponēros | evil/bad | G | `extracted` | 4 | 4 | 61 | 2 |
| 68 | grace | `H2580` | chen | favor | H | `extracted` | 4 | 3 | 61 | 4 |
| 125 | purity | `H2889` | ta.hor | pure | H | `extracted` | 4 | 4 | 58 | 0 |
| 43 | desire | `H7522` | ra.tson | acceptance | H | `extracted` | 4 | 4 | 56 | 3 |
| 176 | worship | `G4352` | proskuneō | to worship | G | `extracted` | 4 | 3 | 54 | 0 |
| 126 | purpose | `H4284` | ma.cha.sha.vah | plot | H | `extracted` | 4 | 2 | 52 | 2 |
| 187 | strength | `H1397` | ga.ver | great man | H | `extracted` | 4 | 2 | 49 | 1 |
| 53 | dread | `H6343` | pa.chad | dread | H | `extracted` | 4 | 4 | 47 | 2 |
| 196 | power | `H3201` | ya.khol | be able | H | `extracted` | 4 | 2 | 47 | 0 |
| 187 | strength | `H1369` | ge.vu.rah | might | H | `extracted` | 4 | 2 | 46 | 1 |
| 17 | bondage | `G1401` | doulos | slave | G | `extracted` | 4 | 4 | 44 | 0 |
| 97 | joy | `H1523` | gil_verb | to rejoice | H | `extracted` | 4 | 2 | 44 | 1 |
| 117 | peace | `H5207` | ni.cho.ach | soothing | H | `extracted` | 4 | 3 | 43 | 0 |
| 213 | listen | `H7181` | qa.shav | to listen | H | `extracted` | 4 | 4 | 43 | 0 |
| 8 | appetite | `H2416A` | chay | alive | H | `extracted` | 4 | 4 | 42 | 0 |
| 187 | strength | `G4991` | soteria | salvation | G | `extracted` | 4 | 2 | 42 | 1 |
| 98 | justice | `H6663` | tsa.deq | to justify | H | `extracted` | 4 | 2 | 40 | 2 |
| 206 | vulnerability | `H6172` | er.vah | nakedness | H | `extracted` | 4 | 4 | 40 | 0 |
| 123 | pride | `H1347` | ga.on | pride | H | `extracted` | 4 | 2 | 39 | 0 |
| 213 | listen | `H0238` | a.zan | to listen | H | `extracted` | 4 | 4 | 38 | 0 |
| 172 | wickedness | `H3644G` | ke.mo | like | H | `extracted` | 4 | 4 | 37 | 2 |
| 187 | strength | `H0553` | am.mits | strong | H | `extracted` | 4 | 2 | 36 | 1 |
| 208 | sloth | `H7503` | ra.phah | to slacken | H | `extracted` | 4 | 4 | 35 | 1 |
| 43 | desire | `G1014` | boulomai | to plan | G | `extracted` | 4 | 2 | 34 | 4 |
| 122 | prayer | `G4335` | proseuchē | prayer | G | `extracted` | 4 | 2 | 34 | 1 |
| 78 | hope | `G1679` | elpizo | to hope/expect | G | `extracted` | 4 | 2 | 33 | 2 |
| 97 | joy | `H7440` | rin.nah | cry | H | `extracted` | 4 | 2 | 33 | 0 |
| 33 | courage | `H2388H` | cha.zaq | to strengthen: hold | H | `extracted` | 4 | 4 | 32 | 1 |
| 43 | desire | `H2656` | che.phets | pleasure | H | `extracted` | 4 | 4 | 32 | 3 |
| 123 | pride | `H4791` | ma.rom | height | H | `extracted` | 4 | 2 | 32 | 0 |
| 196 | power | `G1415` | dunatos | able | G | `extracted` | 4 | 2 | 30 | 3 |
| 197 | authority | `H6486` | pe.qud.dah | punishment | H | `extracted` | 4 | 2 | 30 | 0 |
| 146 | shame | `H1322` | bo.shet | shame | H | `extracted` | 4 | 2 | 29 | 0 |
| 112 | mind | `H2803H` | cha.shav | to devise: count | H | `extracted` | 4 | 2 | 28 | 2 |
| 121 | praise | `H8426` | to.dah | thanksgiving | H | `extracted` | 4 | 2 | 28 | 0 |
| 57 | evil | `H4994` | na | please | H | `extracted` | 4 | 2 | 27 | 2 |
| 111 | mercy | `G1656` | eleos | mercy | G | `extracted` | 4 | 2 | 27 | 1 |
| 187 | strength | `G3624H` | oikos | house: household | G | `extracted` | 4 | 2 | 27 | 0 |
| 43 | desire | `H0183` | a.vah | to desire | H | `extracted` | 4 | 4 | 26 | 3 |
| 102 | longing | `H3615J` | ka.lah | to end: expend | H | `extracted` | 4 | 2 | 26 | 0 |
| 207 | blindness (spiritual) | `G4655` | skotos | darkness | G | `extracted` | 4 | 4 | 26 | 0 |
| 5 | anguish | `G2347` | thlipsis | pressure | G | `extracted` | 4 | 4 | 25 | 1 |
| 61 | fear | `H6342` | pa.chad | to dread | H | `extracted` | 4 | 3 | 25 | 2 |
| 123 | pride | `H8641` | te.ru.mah | contribution | H | `extracted` | 4 | 2 | 25 | 0 |
| 19 | calling | `H7121H` | qa.ra | to call: call by | H | `extracted` | 4 | 2 | 24 | 0 |
| 23 | compassion | `H2347` | chus | to pity | H | `extracted` | 4 | 2 | 24 | 1 |
| 98 | justice | `H1777` | din | to judge | H | `extracted` | 4 | 2 | 24 | 1 |
| 110 | memory | `H2143` | ze.kher | memorial | H | `extracted` | 4 | 2 | 24 | 2 |
| 123 | pride | `H1361` | ga.vah | to exult | H | `extracted` | 4 | 2 | 24 | 1 |
| 184 | spirit | `H5397` | ne.sha.mah | breath | H | `extracted` | 4 | 4 | 24 | 0 |
| 97 | joy | `H7797` | su.s | to rejoice | H | `extracted` | 4 | 2 | 23 | 1 |
| 32 | counsel | `H5475` | sod | counsel | H | `extracted` | 4 | 4 | 22 | 0 |
| 112 | mind | `H2146` | zik.ka.ron | memorial | H | `extracted` | 4 | 3 | 22 | 2 |
| 97 | joy | `H8056` | sa.me.ach | glad | H | `extracted` | 4 | 2 | 21 | 3 |
| 121 | praise | `H1984H` | ha.lal | to boast: boast | H | `extracted` | 4 | 2 | 21 | 0 |
| 176 | worship | `G3000` | latreuō | to minister | G | `extracted` | 4 | 3 | 21 | 0 |
| 197 | authority | `H1935` | hod | splendor | H | `extracted` | 4 | 2 | 21 | 0 |
| 187 | strength | `H4581` | ma.oz | security | H | `extracted` | 4 | 2 | 20 | 0 |
| 20 | character | `G1381` | dokimazō | to test | G | `extracted` | 4 | 2 | 19 | 0 |
| 111 | mercy | `H6279` | a.tar | to pray | H | `extracted` | 4 | 2 | 19 | 1 |
| 124 | prophecy | `G4394` | profēteia | prophecy | G | `extracted` | 4 | 2 | 19 | 0 |
| 43 | desire | `H2530A` | cha.mad | to desire | H | `extracted` | 4 | 4 | 18 | 2 |
| 97 | joy | `H8342` | sa.s.von | rejoicing | H | `extracted` | 4 | 2 | 18 | 1 |
| 102 | longing | `H3615H` | ka.lah | to end: destroy | H | `extracted` | 4 | 2 | 18 | 0 |
| 173 | will | `H5159` | na.cha.lah | inheritance | H | `extracted` | 4 | 3 | 18 | 0 |
| 191 | doubt | `G1252` | diakrinō | to judge/doubt | G | `extracted` | 4 | 2 | 18 | 0 |
| 98 | justice | `H1779` | din | judgment | H | `extracted` | 4 | 2 | 17 | 1 |
| 121 | praise | `H0587` | a.nach.nu | we | H | `extracted` | 4 | 2 | 17 | 0 |
| 177 | worth | `H6186A` | a.rakh | to arrange | H | `extracted` | 4 | 2 | 17 | 0 |
| 75 | hatred | `H8135` | sin.ah | hating | H | `extracted` | 4 | 3 | 16 | 1 |
| 123 | pride | `H1346` | ga.a.vah | pride | H | `extracted` | 4 | 2 | 16 | 0 |
| 187 | strength | `G2480` | ischuō | be strong | G | `extracted` | 4 | 2 | 16 | 0 |
| 102 | longing | `H3615G` | ka.lah | to end: finish | H | `extracted` | 4 | 2 | 15 | 0 |
| 187 | strength | `H2423` | che.va | beast | H | `extracted` | 4 | 2 | 15 | 0 |
| 187 | strength | `G2478` | ischuros | strong | G | `extracted` | 4 | 2 | 15 | 0 |
| 24 | condemnation | `G2632` | katakrinō | to condemn | G | `extracted` | 4 | 2 | 14 | 0 |
| 103 | love | `H2898` | tuv | goodness | H | `extracted` | 4 | 1 | 14 | 2 |
| 111 | mercy | `H5750` | od | still | H | `extracted` | 4 | 2 | 14 | 1 |
| 116 | patience | `G3115` | makrothumia | patience | G | `extracted` | 4 | 2 | 14 | 0 |
| 117 | peace | `H4496H` | me.nu.chah | resting | H | `extracted` | 4 | 3 | 14 | 0 |
| 186 | gladness | `G2165` | eufrainō | to celebrate | G | `extracted` | 4 | 2 | 14 | 1 |
| 26 | conscience | `H3629` | kil.yah | kidney | H | `extracted` | 4 | 2 | 13 | 1 |
| 32 | counsel | `G1012` | boulē | plan | G | `extracted` | 4 | 2 | 13 | 4 |
| 90 | innocence | `H8535` | tam | complete | H | `extracted` | 4 | 2 | 13 | 2 |
| 187 | strength | `H1433` | go.del | greatness | H | `extracted` | 4 | 2 | 13 | 0 |
| 28 | consecration | `H6922` | qad.dish | holy | H | `extracted` | 4 | 2 | 12 | 1 |
| 187 | strength | `G2904` | kratos | power | G | `extracted` | 4 | 2 | 12 | 1 |
| 19 | calling | `H7621` | she.vu.ah | oath | H | `extracted` | 4 | 2 | 11 | 1 |
| 61 | fear | `H4172A` | mo.rah | fear | H | `extracted` | 4 | 2 | 11 | 4 |
| 199 | dominion | `G0936` | basileuō | to reign | G | `extracted` | 4 | 3 | 11 | 0 |
| 202 | transformation | `H2498` | cha.laph | to pass | H | `extracted` | 4 | 4 | 11 | 1 |
| 206 | vulnerability | `H5903` | e.rom | naked | H | `extracted` | 4 | 4 | 11 | 0 |
| 61 | fear | `H1481C` | gur | to dread | H | `extracted` | 4 | 2 | 10 | 3 |
| 102 | longing | `H3615I` | ka.lah | to end: decides | H | `extracted` | 4 | 2 | 10 | 0 |
| 120 | perverseness | `H8419` | tah.pu.khah | perversity | H | `extracted` | 4 | 2 | 10 | 0 |
| 173 | will | `H7665` | sha.var | to break | H | `extracted` | 4 | 2 | 10 | 1 |
| 206 | vulnerability | `G1131` | gumnos | naked | G | `extracted` | 4 | 4 | 10 | 0 |
| 77 | honesty | `H6666` | tse.da.qah | righteousness | H | `extracted` | 3 | 3 | 148 | 2 |
| 176 | worship | `H5647H` | a.vad | to serve: minister | H | `extracted` | 3 | 2 | 142 | 0 |
| 167 | unity | `H1571` | gam | also | H | `extracted` | 3 | 3 | 132 | 0 |
| 213 | listen | `H8085H` | sha.ma | to hear: obey | H | `extracted` | 3 | 3 | 119 | 0 |
| 40 | deceit | `H8267` | she.qer | deception | H | `extracted` | 3 | 3 | 112 | 0 |
| 86 | impurity | `H2930A` | ta.me | to defile | H | `extracted` | 3 | 2 | 109 | 0 |
| 43 | desire | `G3870` | parakaleō | to plead/comfort | G | `extracted` | 3 | 3 | 106 | 2 |
| 39 | debauchery | `G4982` | sōzō | to save | G | `extracted` | 3 | 3 | 94 | 0 |
| 44 | despair | `H0539` | a.man | be faithful | H | `extracted` | 3 | 3 | 86 | 4 |
| 128 | rebellion | `H5493G` | sur | to turn aside: remove | H | `extracted` | 3 | 3 | 81 | 0 |
| 42 | delight | `H2654A` | cha.phets | to delight in | H | `extracted` | 3 | 3 | 71 | 3 |
| 125 | purity | `H2891` | ta.her | be pure | H | `extracted` | 3 | 3 | 71 | 0 |
| 32 | counsel | `H3289` | ya.ats | to advise | H | `extracted` | 3 | 3 | 68 | 1 |
| 117 | peace | `H1293` | be.ra.khah | blessing | H | `extracted` | 3 | 2 | 63 | 1 |
| 78 | hope | `H5027` | na.vat | to look | H | `extracted` | 3 | 3 | 59 | 0 |
| 43 | desire | `G2307` | thelēma | will/desire | G | `extracted` | 3 | 3 | 58 | 1 |
| 173 | will | `G1510` | eimi | to be | G | `extracted` | 3 | 3 | 58 | 0 |
| 174 | wisdom | `H7919A` | sa.khal | be prudent | H | `extracted` | 3 | 2 | 58 | 3 |
| 51 | distress | `H2199` | za.aq | to cry out | H | `extracted` | 3 | 3 | 56 | 0 |
| 173 | will | `G3361` | mē | not | G | `extracted` | 3 | 3 | 55 | 0 |
| 180 | yielding | `H2232` | za.ra | to sow | H | `extracted` | 3 | 3 | 54 | 1 |
| 42 | delight | `H7521` | ra.tsah | to accept | H | `extracted` | 3 | 3 | 52 | 3 |
| 51 | distress | `H7378` | riv | to contend | H | `extracted` | 3 | 3 | 52 | 1 |
| 33 | courage | `H5030` | na.vi | prophet | H | `extracted` | 3 | 3 | 48 | 1 |
| 43 | desire | `G2065` | erōtaō | to ask | G | `extracted` | 3 | 3 | 48 | 1 |
| 76 | holiness | `H6918G` | qa.dosh | holy | H | `extracted` | 3 | 3 | 48 | 1 |
| 128 | rebellion | `H5493I` | sur | to turn aside: turn aside | H | `extracted` | 3 | 3 | 48 | 0 |
| 64 | forgiveness | `H5545` | sa.lach | to forgive | H | `extracted` | 3 | 3 | 45 | 0 |
| 112 | mind | `H2803I` | cha.shav | to devise: devise | H | `extracted` | 3 | 2 | 43 | 2 |
| 149 | slander | `H7272` | re.gel | foot | H | `extracted` | 3 | 2 | 43 | 0 |
| 78 | hope | `H6960A` | qa.vah | to await | H | `extracted` | 3 | 2 | 42 | 1 |
| 174 | wisdom | `H8394` | te.vu.nah | understanding | H | `extracted` | 3 | 2 | 42 | 4 |
| 173 | will | `H3426` | yesh | there | H | `extracted` | 3 | 3 | 40 | 0 |
| 51 | distress | `H7489A` | ra.a | be evil | H | `extracted` | 3 | 3 | 38 | 6 |
| 43 | desire | `G1939` | epithumia | desire | G | `extracted` | 3 | 3 | 37 | 4 |
| 51 | distress | `H7451I` | ra.ah | distress: evil | H | `extracted` | 3 | 3 | 37 | 6 |
| 56 | envy | `H7068` | qin.ah | jealousy | H | `extracted` | 3 | 3 | 37 | 2 |
| 146 | shame | `H2778A` | cha.raph | to taunt | H | `extracted` | 3 | 2 | 37 | 1 |
| 176 | worship | `H5647G` | a.vad | to serve | H | `extracted` | 3 | 2 | 37 | 0 |
| 78 | hope | `H2620` | cha.sah | to seek refuge | H | `extracted` | 3 | 2 | 36 | 1 |
| 163 | trust | `G3982` | peithō | to persuade | G | `extracted` | 3 | 1 | 35 | 2 |
| 135 | repentance | `H5162H` | na.cham | to be sorry: relent | H | `extracted` | 3 | 2 | 34 | 3 |
| 163 | trust | `H0983` | be.tach | security | H | `extracted` | 3 | 3 | 34 | 1 |
| 64 | forgiveness | `G0863G` | afiēmi | to release: leave | G | `extracted` | 3 | 3 | 32 | 0 |
| 198 | might | `G3779` | houtōs | thus(-ly) | G | `extracted` | 3 | 1 | 32 | 0 |
| 86 | impurity | `G0169` | akathartos | unclean | G | `extracted` | 3 | 2 | 30 | 0 |
| 160 | thought | `G2919` | krinō | to judge | G | `extracted` | 3 | 1 | 30 | 2 |
| 160 | thought | `G3049` | logizomai | to count | G | `extracted` | 3 | 1 | 30 | 0 |
| 183 | heart | `H4578` | me.eh | belly | H | `extracted` | 3 | 3 | 30 | 2 |
| 56 | envy | `H7065` | qa.na | be jealous | H | `extracted` | 3 | 3 | 29 | 2 |
| 86 | impurity | `G2511` | katharizō | to clean | G | `extracted` | 3 | 2 | 29 | 0 |
| 113 | mourning | `H5594` | sa.phad | to mourn | H | `extracted` | 3 | 2 | 29 | 0 |
| 34 | covenant | `G1242` | diathēkē | covenant | G | `extracted` | 3 | 3 | 27 | 0 |
| 51 | distress | `H7186` | qa.sheh | severe | H | `extracted` | 3 | 3 | 27 | 1 |
| 55 | endurance | `H5331` | ne.tsach | perpetuity | H | `extracted` | 3 | 3 | 26 | 0 |
| 78 | hope | `H3176H` | ya.chal | to wait: hope | H | `extracted` | 3 | 2 | 26 | 1 |
| 4 | anger | `H5006` | na.ats | to spurn | H | `extracted` | 3 | 3 | 25 | 1 |
| 63 | foolishness | `H0191` | e.vil | fool[ish] | H | `extracted` | 3 | 3 | 25 | 0 |
| 166 | understanding | `G4920` | suniēmi | to understand | G | `extracted` | 3 | 3 | 25 | 2 |
| 213 | listen | `G3775` | ous | ear | G | `extracted` | 3 | 3 | 24 | 0 |
| 47 | dignity | `H1926` | ha.dar | glory | H | `extracted` | 3 | 3 | 23 | 0 |
| 173 | will | `G3195` | mellō | to ensue | G | `extracted` | 3 | 3 | 23 | 0 |
| 6 | anointing | `G5547` | christos | Christ | G | `extracted` | 3 | 3 | 22 | 0 |
| 16 | boldness | `G3954` | parrēsia | boldness | G | `extracted` | 3 | 3 | 22 | 1 |
| 112 | mind | `G3563` | nous | mind | G | `extracted` | 3 | 3 | 22 | 2 |
| 4 | anger | `H2734` | cha.rah | to be incensed | H | `extracted` | 3 | 3 | 21 | 2 |
| 4 | anger | `H3708B` | ka.a.s | vexation | H | `extracted` | 3 | 3 | 21 | 4 |
| 11 | awe | `H2865` | cha.tat | to to be dismayed | H | `extracted` | 3 | 3 | 21 | 2 |
| 42 | delight | `G2106` | eudokeō | to delight | G | `extracted` | 3 | 3 | 21 | 4 |
| 112 | mind | `G3415` | mnaomai | to remember | G | `extracted` | 3 | 3 | 21 | 0 |
| 176 | worship | `H8334` | sha.rat | to minister | H | `extracted` | 3 | 2 | 21 | 0 |
| 43 | desire | `H8378` | ta.a.vah | desire | H | `extracted` | 3 | 3 | 20 | 3 |
| 51 | distress | `G3076` | lupeō | to grieve | G | `extracted` | 3 | 3 | 20 | 2 |
| 5 | anguish | `H5999` | a.mal | trouble | H | `extracted` | 3 | 3 | 19 | 2 |
| 51 | distress | `H7451A` | ra | bad: harmful | H | `extracted` | 3 | 3 | 19 | 7 |
| 157 | temptation | `G3985H` | peirazō | to test/tempt: test | G | `extracted` | 3 | 1 | 19 | 0 |
| 160 | thought | `H2803G` | cha.shav | to devise: design | H | `extracted` | 3 | 2 | 19 | 2 |
| 1 | abomination | `H8581` | ta.av | to abhor | H | `extracted` | 3 | 3 | 18 | 0 |
| 4 | anger | `H3707` | ka.as | to provoke | H | `extracted` | 3 | 3 | 18 | 4 |
| 6 | anointing | `H4886` | ma.shach | to anoint | H | `extracted` | 3 | 3 | 18 | 0 |
| 17 | bondage | `G1398` | douleuō | be a slave | G | `extracted` | 3 | 3 | 18 | 0 |
| 149 | slander | `G0988` | blasfēmia | blasphemy | G | `extracted` | 3 | 2 | 18 | 0 |
| 151 | sorrow | `H2256M` | che.vel | pain | H | `extracted` | 3 | 2 | 18 | 2 |
| 6 | anointing | `H4899` | ma.shi.ach | anointed | H | `extracted` | 3 | 3 | 17 | 0 |
| 7 | anxiety | `G3309` | merimnaō | to worry | G | `extracted` | 3 | 3 | 17 | 1 |
| 56 | envy | `G2205` | zēlos | zeal | G | `extracted` | 3 | 3 | 17 | 2 |
| 78 | hope | `H4268` | mach.s.seh | refuge | H | `extracted` | 3 | 2 | 17 | 1 |
| 117 | peace | `H7965I` | sha.lom | peace: well-being | H | `extracted` | 3 | 2 | 17 | 2 |
| 18 | brokenness | `H7667` | she.ver | breaking | H | `extracted` | 3 | 3 | 16 | 0 |
| 34 | covenant | `G2537` | kainos | new | G | `extracted` | 3 | 3 | 16 | 2 |
| 122 | prayer | `G1189` | deomai | to pray | G | `extracted` | 3 | 2 | 16 | 1 |
| 170 | weakness | `G0772G` | asthenēs | weak | G | `extracted` | 3 | 3 | 16 | 1 |
| 4 | anger | `H2534` | che.mah | rage | H | `extracted` | 3 | 3 | 15 | 1 |
| 61 | fear | `H6206` | a.rats | to tremble | H | `extracted` | 3 | 2 | 15 | 1 |
| 213 | listen | `G5219` | hupakouō | to obey | G | `extracted` | 3 | 3 | 15 | 0 |
| 5 | anguish | `H6869B` | tsa.rah | distress | H | `extracted` | 3 | 3 | 14 | 2 |
| 53 | dread | `H1368` | gib.bor | mighty man | H | `extracted` | 3 | 3 | 14 | 2 |
| 62 | fellowship | `G2842` | koinōnia | participation | G | `extracted` | 3 | 2 | 14 | 0 |
| 72 | groaning | `H1897` | ha.gah | to mutter | H | `extracted` | 3 | 2 | 14 | 1 |
| 114 | obedience | `G5218` | hupakoē | obedience | G | `extracted` | 3 | 2 | 14 | 0 |
| 183 | heart | `G4698` | splanchnon | affection/entrails | G | `extracted` | 3 | 3 | 14 | 1 |
| 201 | image | `G1504` | eikōn | image | G | `extracted` | 3 | 3 | 14 | 0 |
| 5 | anguish | `H5782` | ur | to rouse | H | `extracted` | 3 | 3 | 13 | 1 |
| 111 | mercy | `H3724A` | ko.pher | ransom | H | `extracted` | 3 | 2 | 13 | 1 |
| 173 | will | `H5157` | na.chal | to inherit | H | `extracted` | 3 | 2 | 13 | 0 |
| 5 | anguish | `H4751` | mar | bitter | H | `extracted` | 3 | 3 | 12 | 3 |
| 31 | corruption | `G1067` | geenna | hell: Gehenna | G | `extracted` | 3 | 2 | 12 | 0 |
| 63 | foolishness | `G3474` | mōros | foolish | G | `extracted` | 3 | 3 | 12 | 1 |
| 112 | mind | `G1271` | dianoia | mind | G | `extracted` | 3 | 3 | 12 | 2 |
| 168 | uprightness | `H3476` | yo.sher | uprightness | H | `extracted` | 3 | 3 | 12 | 1 |
| 174 | wisdom | `H8454` | tu.shiy.yah | wisdom | H | `extracted` | 3 | 2 | 12 | 0 |
| 184 | spirit | `H5301` | na.phach | to breathe | H | `extracted` | 3 | 3 | 12 | 0 |
| 185 | flesh | `H7607` | she.er | flesh | H | `extracted` | 3 | 2 | 12 | 0 |
| 94 | intercession | `H6293` | pa.ga | to fall on | H | `extracted` | 3 | 2 | 11 | 1 |
| 123 | pride | `G2745` | kauchēma | pride | G | `extracted` | 3 | 2 | 11 | 1 |
| 124 | prophecy | `G5578` | pseudoprofētēs | false prophet | G | `extracted` | 3 | 2 | 11 | 0 |
| 174 | wisdom | `G4680` | sofos | wise | G | `extracted` | 3 | 2 | 11 | 1 |
| 61 | fear | `G4576` | sebomai | be devout | G | `extracted` | 3 | 2 | 10 | 0 |
| 71 | grief | `H4843` | ma.rar | to provoke | H | `extracted` | 3 | 2 | 10 | 3 |
| 146 | shame | `H0954` | bosh | be ashamed | H | `extracted` | 3 | 3 | 10 | 0 |
| 201 | image | `H1823` | de.mut | likeness | H | `extracted` | 3 | 3 | 10 | 1 |
| 201 | image | `H6754` | tse.lem | image | H | `extracted` | 3 | 3 | 10 | 0 |
| 197 | authority | `H3027H` | yad | hand: power | H | `extracted` | 2 | 1 | 267 | 6 |
| 112 | mind | `H8104G` | sha.mar | to keep: obey | H | `extracted` | 2 | 1 | 193 | 0 |
| 73 | guilt | `H5771G` | a.von | iniquity: crime | H | `extracted` | 2 | 1 | 162 | 2 |
| 73 | guilt | `H2403B` | chat.tat | sin | H | `extracted` | 2 | 1 | 159 | 1 |
| 103 | love | `H7453` | re.a | neighbor | H | `extracted` | 2 | 1 | 152 | 0 |
| 103 | love | `H8130` | sa.ne | to hate | H | `extracted` | 2 | 1 | 134 | 1 |
| 128 | rebellion | `H6588` | pe.sha | transgression | H | `extracted` | 2 | 2 | 90 | 1 |
| 135 | repentance | `H7725O` | shuv | to return: repent | H | `extracted` | 2 | 2 | 77 | 1 |
| 112 | mind | `H8104J` | sha.mar | to keep: careful | H | `extracted` | 2 | 1 | 75 | 0 |
| 151 | sorrow | `H2490H` | cha.lal | to profane/begin | H | `extracted` | 2 | 1 | 72 | 0 |
| 111 | mercy | `H2603A` | cha.nan | be gracious | H | `extracted` | 2 | 1 | 71 | 4 |
| 151 | sorrow | `H0205G` | a.ven | evil: trouble | H | `extracted` | 2 | 1 | 71 | 5 |
| 11 | awe | `H3373` | ya.re | afraid | H | `extracted` | 2 | 2 | 64 | 3 |
| 121 | praise | `H4210` | miz.mor | melody | H | `extracted` | 2 | 1 | 57 | 0 |
| 197 | authority | `G0757` | archō | be first | G | `extracted` | 2 | 1 | 56 | 1 |
| 140 | seeking | `G1537` | ek | out from | G | `extracted` | 2 | 2 | 54 | 0 |
| 97 | joy | `H7442B` | ra.nan | to sing | H | `extracted` | 2 | 1 | 53 | 0 |
| 197 | authority | `H6485J` | pa.qad | to reckon: overseer | H | `extracted` | 2 | 1 | 53 | 0 |
| 197 | authority | `H6485H` | pa.qad | to reckon: punish | H | `extracted` | 2 | 1 | 48 | 0 |
| 167 | unity | `H3162B` | ya.che.dav | together | H | `extracted` | 2 | 2 | 47 | 0 |
| 51 | distress | `H7379` | riv | strife | H | `extracted` | 2 | 2 | 45 | 1 |
| 73 | guilt | `G0268` | hamartōlos | sinful | G | `extracted` | 2 | 1 | 45 | 1 |
| 103 | love | `H7355` | ra.cham | to have compassion | H | `extracted` | 2 | 1 | 43 | 2 |
| 121 | praise | `H2167` | za.mar | to sing | H | `extracted` | 2 | 1 | 41 | 0 |
| 86 | impurity | `H2931` | ta.me | unclean | H | `extracted` | 2 | 2 | 39 | 0 |
| 103 | love | `H7356B` | ra.cha.mim | compassion | H | `extracted` | 2 | 1 | 39 | 2 |
| 174 | wisdom | `H0998` | bi.nah | understanding | H | `extracted` | 2 | 2 | 39 | 4 |
| 69 | gratitude | `G2168` | eucharisteō | to thank | G | `extracted` | 2 | 1 | 38 | 0 |
| 126 | purpose | `H4616` | ma.an | because | H | `extracted` | 2 | 2 | 38 | 1 |
| 180 | yielding | `H2233G` | ze.ra | seed | H | `extracted` | 2 | 2 | 38 | 0 |
| 207 | blindness (spiritual) | `G5185` | tuflos | blind | G | `extracted` | 2 | 2 | 38 | 0 |
| 64 | forgiveness | `G0863H` | afiēmi | to release: forgive | G | `extracted` | 2 | 2 | 37 | 0 |
| 128 | rebellion | `H6586` | pa.sha | to transgress | H | `extracted` | 2 | 2 | 37 | 1 |
| 147 | sin | `G0264` | hamartanō | to sin | G | `extracted` | 2 | 1 | 37 | 1 |
| 197 | authority | `H6485I` | pa.qad | to reckon: visit | H | `extracted` | 2 | 1 | 37 | 0 |
| 71 | grief | `H6040` | o.ni | affliction | H | `extracted` | 2 | 2 | 36 | 4 |
| 98 | justice | `G1344` | dikaioō | to justify | G | `extracted` | 2 | 1 | 36 | 1 |
| 43 | desire | `H2550` | cha.mal | to spare | H | `extracted` | 2 | 2 | 35 | 4 |
| 51 | distress | `H6697H` | tsur | rock | H | `extracted` | 2 | 2 | 35 | 1 |
| 59 | faith | `H4603` | ma.al | be unfaithful | H | `extracted` | 2 | 1 | 34 | 0 |
| 142 | self-control | `H6113` | a.tsar | to restrain | H | `extracted` | 2 | 2 | 34 | 0 |
| 183 | heart | `H2436G` | cheq | bosom: embrace | H | `extracted` | 2 | 2 | 34 | 0 |
| 73 | guilt | `H2399` | chet | sin | H | `extracted` | 2 | 1 | 33 | 1 |
| 103 | love | `H2623` | cha.sid | pious | H | `extracted` | 2 | 1 | 33 | 6 |
| 172 | wickedness | `H7561` | ra.sha | be wicked | H | `extracted` | 2 | 2 | 33 | 0 |
| 191 | doubt | `G3842` | pantote | always | G | `extracted` | 2 | 1 | 33 | 0 |
| 52 | division | `H6299` | pa.dah | to ransom | H | `extracted` | 2 | 2 | 32 | 0 |
| 135 | repentance | `G3340` | metanoeo | to repent | G | `extracted` | 2 | 1 | 32 | 3 |
| 155 | submission | `G5293` | hupotassō | to subject | G | `extracted` | 2 | 1 | 32 | 0 |
| 51 | distress | `H0926` | ba.hal | to dismay | H | `extracted` | 2 | 2 | 31 | 0 |
| 78 | hope | `H8615B` | tiq.vah | hope | H | `extracted` | 2 | 1 | 31 | 1 |
| 116 | patience | `G5281` | hupomonē | perseverance | G | `extracted` | 2 | 1 | 31 | 1 |
| 197 | authority | `G0758` | archōn | ruler | G | `extracted` | 2 | 1 | 31 | 0 |
| 126 | purpose | `H4399` | me.la.khah | work | H | `extracted` | 2 | 2 | 30 | 0 |
| 73 | guilt | `H0816` | a.sham | be guilty | H | `extracted` | 2 | 2 | 29 | 0 |
| 146 | shame | `H3639` | ke.lim.mah | shame | H | `extracted` | 2 | 1 | 29 | 0 |
| 151 | sorrow | `H7455` | ro.a | evil | H | `extracted` | 2 | 1 | 28 | 6 |
| 188 | weeping | `H1065` | be.khi | weeping | H | `extracted` | 2 | 1 | 28 | 0 |
| 73 | guilt | `H5771H` | a.von | iniquity: guilt | H | `extracted` | 2 | 1 | 27 | 1 |
| 90 | innocence | `H8549H` | ta.mim | unblemished: blameless | H | `extracted` | 2 | 1 | 27 | 2 |
| 103 | love | `H1730G` | dod | beloved | H | `extracted` | 2 | 1 | 27 | 0 |
| 112 | mind | `H2803J` | cha.shav | to devise: think | H | `extracted` | 2 | 2 | 26 | 2 |
| 151 | sorrow | `H4043` | ma.gen | shield | H | `extracted` | 2 | 1 | 25 | 0 |
| 152 | strife | `H7230` | rov | abundance | H | `extracted` | 2 | 1 | 25 | 0 |
| 63 | foolishness | `H0200` | iv.ve.let | folly | H | `extracted` | 2 | 2 | 24 | 0 |
| 80 | humility | `H8213` | sha.phel | to abase | H | `extracted` | 2 | 2 | 24 | 0 |
| 86 | impurity | `H5079` | nid.dah | impurity | H | `extracted` | 2 | 2 | 24 | 0 |
| 197 | authority | `H6490` | piq.qud | precept | H | `extracted` | 2 | 1 | 24 | 0 |
| 23 | compassion | `H7358` | re.chem | womb | H | `extracted` | 2 | 2 | 23 | 2 |
| 39 | debauchery | `G4990` | sōtēr | savior | G | `extracted` | 2 | 2 | 23 | 1 |
| 89 | iniquity | `H6041` | a.ni | afflicted | H | `extracted` | 2 | 2 | 23 | 5 |
| 111 | mercy | `H3727` | kap.po.ret | mercy seat | H | `extracted` | 2 | 1 | 22 | 1 |
| 135 | repentance | `G3341` | metanoia | repentance | G | `extracted` | 2 | 1 | 22 | 3 |
| 196 | power | `H3444` | ye.shu.ah | salvation | H | `extracted` | 2 | 1 | 22 | 0 |
| 80 | humility | `H6035` | a.nav | poor | H | `extracted` | 2 | 2 | 21 | 4 |
| 90 | innocence | `H8537` | tom | integrity | H | `extracted` | 2 | 1 | 21 | 2 |
| 112 | mind | `G3421` | mnēmoneuō | to remember | G | `extracted` | 2 | 2 | 21 | 1 |
| 116 | patience | `H0748` | a.rakh | to prolong | H | `extracted` | 2 | 2 | 21 | 0 |
| 128 | rebellion | `H4775` | ma.rad | to rebel | H | `extracted` | 2 | 2 | 21 | 0 |
| 183 | heart | `H5034B` | na.vel | to wither | H | `extracted` | 2 | 2 | 21 | 1 |
| 4 | anger | `H2195` | za.am | indignation | H | `extracted` | 2 | 2 | 20 | 3 |
| 99 | kindness | `H5971B` | am | kinsman | H | `extracted` | 2 | 1 | 20 | 0 |
| 123 | pride | `H4805H` | me.ri | rebellion | H | `extracted` | 2 | 1 | 20 | 2 |
| 126 | purpose | `G5056` | telos | goal/tax | G | `extracted` | 2 | 2 | 20 | 0 |
| 173 | will | `H6213A` | a.sah | to make: do | H | `extracted` | 2 | 1 | 20 | 1 |
| 4 | anger | `H2740` | cha.ron | burning anger | H | `extracted` | 2 | 2 | 19 | 2 |
| 51 | distress | `H7185` | qa.shah | to harden | H | `extracted` | 2 | 2 | 19 | 1 |
| 89 | iniquity | `H5766A` | a.vel | injustice | H | `extracted` | 2 | 2 | 19 | 1 |
| 105 | lust | `H8457` | taz.nut | fornication | H | `extracted` | 2 | 1 | 19 | 1 |
| 112 | mind | `G5426` | froneō | to reason | G | `extracted` | 2 | 2 | 19 | 5 |
| 151 | sorrow | `H2486` | cha.li.lah | forbid | H | `extracted` | 2 | 1 | 19 | 0 |
| 160 | thought | `G2233` | hēgeomai | to govern | G | `extracted` | 2 | 1 | 19 | 0 |
| 173 | will | `H1836` | de.nah | this | H | `extracted` | 2 | 2 | 19 | 2 |
| 174 | wisdom | `H7922` | se.khel | understanding | H | `extracted` | 2 | 1 | 19 | 1 |
| 176 | worship | `H5656H` | a.vo.dah | service: ministry | H | `extracted` | 2 | 1 | 19 | 0 |
| 64 | forgiveness | `G0863I` | afiēmi | to release: permit | G | `extracted` | 2 | 2 | 18 | 0 |
| 86 | impurity | `G2513` | katharos | clean | G | `extracted` | 2 | 2 | 18 | 0 |
| 103 | love | `H7474` | ra.yah | darling | H | `extracted` | 2 | 1 | 18 | 0 |
| 116 | patience | `H3811` | la.ah | be weary | H | `extracted` | 2 | 1 | 18 | 0 |
| 174 | wisdom | `H2493` | che.lem | dream | H | `extracted` | 2 | 1 | 18 | 0 |
| 187 | strength | `H1396` | ga.var | to prevail | H | `extracted` | 2 | 1 | 18 | 1 |
| 211 | being | `H3665` | ka.na | be humble | H | `extracted` | 2 | 2 | 18 | 0 |
| 51 | distress | `H7878` | si.ach | to muse | H | `extracted` | 2 | 2 | 17 | 3 |
| 81 | hypocrisy | `G5273` | hupokritēs | hypocrite | G | `extracted` | 2 | 2 | 17 | 0 |
| 146 | shame | `H7036` | qa.lon | dishonor | H | `extracted` | 2 | 1 | 17 | 0 |
| 43 | desire | `G1937` | epithumeō | to long for | G | `extracted` | 2 | 2 | 16 | 4 |
| 64 | forgiveness | `G0859` | afesis | forgiveness | G | `extracted` | 2 | 2 | 16 | 0 |
| 102 | longing | `H3617` | ka.lah | consumption | H | `extracted` | 2 | 1 | 16 | 0 |
| 103 | love | `G5384` | filos | friendly/friend | G | `extracted` | 2 | 1 | 16 | 2 |
| 122 | prayer | `G1162` | deēsis | petition | G | `extracted` | 2 | 1 | 16 | 1 |
| 146 | shame | `H2659` | cha.pher | be ashamed | H | `extracted` | 2 | 1 | 16 | 0 |
| 168 | uprightness | `H4339` | me.shar | uprightness | H | `extracted` | 2 | 2 | 16 | 1 |
| 173 | will | `H5352` | na.qah | to clear | H | `extracted` | 2 | 1 | 16 | 1 |
| 184 | spirit | `H0178` | ov | medium | H | `extracted` | 2 | 2 | 16 | 0 |
| 68 | grace | `G5483` | charizō | to give grace | G | `extracted` | 2 | 2 | 15 | 0 |
| 71 | grief | `H4341` | makh.ov | pain | H | `extracted` | 2 | 1 | 15 | 2 |
| 78 | hope | `H4009` | miv.tach | confidence | H | `extracted` | 2 | 2 | 15 | 1 |
| 112 | mind | `H5068` | na.dav | be willing | H | `extracted` | 2 | 1 | 15 | 1 |
| 117 | peace | `H1826H` | da.mam | to silence: silent | H | `extracted` | 2 | 1 | 15 | 0 |
| 187 | strength | `G3619` | oikodomē | building | G | `extracted` | 2 | 1 | 15 | 0 |
| 5 | anguish | `H3015` | ya.gon | sorrow | H | `extracted` | 2 | 2 | 14 | 2 |
| 34 | covenant | `H0423` | a.lah | oath | H | `extracted` | 2 | 2 | 14 | 0 |
| 51 | distress | `H2201` | ze.a.qah | outcry | H | `extracted` | 2 | 2 | 14 | 0 |
| 113 | mourning | `H4553` | mis.ped | mourning | H | `extracted` | 2 | 1 | 14 | 0 |
| 116 | patience | `H0750` | a.rekh | slow | H | `extracted` | 2 | 1 | 14 | 0 |
| 116 | patience | `G5278` | hupomenō | to remain/endure | G | `extracted` | 2 | 1 | 14 | 1 |
| 127 | reasoning | `G1261` | dialogismos | reasoning | G | `extracted` | 2 | 2 | 14 | 2 |
| 159 | testimony | `H5713B` | e.dah | testimony | H | `extracted` | 2 | 1 | 14 | 0 |
| 159 | testimony | `H5715` | e.dut | testimony | H | `extracted` | 2 | 1 | 14 | 1 |
| 160 | thought | `G1260` | dialogizomai | to discuss | G | `extracted` | 2 | 2 | 14 | 2 |
| 160 | thought | `G5429` | fronimos | thoughtful | G | `extracted` | 2 | 1 | 14 | 0 |
| 162 | transgression | `G3900` | paraptōma | trespass | G | `extracted` | 2 | 1 | 14 | 0 |
| 194 | blessing | `G5486` | charisma | gift | G | `extracted` | 2 | 1 | 14 | 0 |
| 208 | sloth | `H6102` | a.tsel | sluggish | H | `extracted` | 2 | 2 | 14 | 0 |
| 23 | compassion | `H2587` | chan.nun | gracious | H | `extracted` | 2 | 1 | 13 | 4 |
| 103 | love | `H2895` | tov | be pleasing | H | `extracted` | 2 | 1 | 13 | 2 |
| 103 | love | `H7349` | ra.chum | compassionate | H | `extracted` | 2 | 1 | 13 | 2 |
| 108 | meditation | `H7879` | si.ach | complaint | H | `extracted` | 2 | 1 | 13 | 3 |
| 123 | pride | `H2086` | zed | arrogant | H | `extracted` | 2 | 1 | 13 | 1 |
| 162 | transgression | `H1097` | be.li | without | H | `extracted` | 2 | 1 | 13 | 1 |
| 170 | weakness | `G0769G` | astheneia | weakness: weak | G | `extracted` | 2 | 2 | 13 | 1 |
| 170 | weakness | `G0770G` | astheneō | be weak: weak | G | `extracted` | 2 | 2 | 13 | 1 |
| 175 | wonder | `H6382` | pe.le | wonder | H | `extracted` | 2 | 1 | 13 | 0 |
| 190 | contempt | `H0959` | ba.zah | to despise | H | `extracted` | 2 | 1 | 13 | 0 |
| 190 | contempt | `H5039` | ne.va.lah | folly | H | `extracted` | 2 | 1 | 13 | 0 |
| 191 | doubt | `H2963` | ta.raph | to tear | H | `extracted` | 2 | 1 | 13 | 0 |
| 197 | authority | `H6496` | pa.qid | overseer | H | `extracted` | 2 | 1 | 13 | 0 |
| 198 | might | `H6435` | pen- | lest | H | `extracted` | 2 | 2 | 13 | 0 |
| 213 | listen | `G0430` | anechō | to endure | G | `extracted` | 2 | 2 | 13 | 0 |
| 23 | compassion | `G4697` | splanchnizō | to pity | G | `extracted` | 2 | 1 | 12 | 1 |
| 43 | desire | `H1942` | hav.vah | desire | H | `extracted` | 2 | 1 | 12 | 2 |
| 43 | desire | `G1934` | epizēteō | to seek after | G | `extracted` | 2 | 2 | 12 | 1 |
| 52 | division | `G3313` | meros | part | G | `extracted` | 2 | 2 | 12 | 0 |
| 61 | fear | `H4549` | ma.sas | to melt | H | `extracted` | 2 | 1 | 12 | 0 |
| 71 | grief | `H2470I` | cha.lah | be weak: grieved | H | `extracted` | 2 | 2 | 12 | 1 |
| 99 | kindness | `H2098` | zu | this | H | `extracted` | 2 | 1 | 12 | 1 |
| 105 | lust | `H7533` | ra.tsats | to crush | H | `extracted` | 2 | 1 | 12 | 1 |
| 116 | patience | `H2442` | cha.khah | to wait | H | `extracted` | 2 | 1 | 12 | 0 |
| 123 | pride | `G2746` | kauchēsis | pride | G | `extracted` | 2 | 1 | 12 | 1 |
| 157 | temptation | `G3985G` | peirazō | to test/tempt: tempt | G | `extracted` | 2 | 1 | 12 | 0 |
| 160 | thought | `H0194` | u.lay | perhaps | H | `extracted` | 2 | 1 | 12 | 0 |
| 163 | trust | `H8172` | sha.an | to lean | H | `extracted` | 2 | 2 | 12 | 0 |
| 167 | unity | `H3173` | ya.chid | only | H | `extracted` | 2 | 2 | 12 | 0 |
| 176 | worship | `H5656G` | a.vo.dah | service | H | `extracted` | 2 | 1 | 12 | 0 |
| 197 | authority | `G1299` | diatassō | to direct | G | `extracted` | 2 | 1 | 12 | 0 |
| 19 | calling | `G2821` | klēsis | calling | G | `extracted` | 2 | 1 | 11 | 1 |
| 35 | covetousness | `G4124` | pleonexia | greediness | G | `extracted` | 2 | 2 | 11 | 1 |
| 51 | distress | `H6887B` | tsa.rar | to constrain | H | `extracted` | 2 | 2 | 11 | 2 |
| 56 | envy | `G2206` | zēloō | be eager | G | `extracted` | 2 | 2 | 11 | 3 |
| 57 | evil | `G0987` | blasfēmeō | to blaspheme | G | `extracted` | 2 | 2 | 11 | 1 |
| 72 | groaning | `H0584` | a.nach | to sigh | H | `extracted` | 2 | 2 | 11 | 1 |
| 80 | humility | `G5013` | tapeinoō | to humble | G | `extracted` | 2 | 2 | 11 | 0 |
| 83 | idolatry | `G1497` | eidōlon | idol | G | `extracted` | 2 | 2 | 11 | 0 |
| 98 | justice | `G0094` | adikos | unjust | G | `extracted` | 2 | 1 | 11 | 1 |
| 103 | love | `H1730H` | dod | beloved | H | `extracted` | 2 | 1 | 11 | 0 |
| 103 | love | `H5273A` | na.im | pleasant | H | `extracted` | 2 | 1 | 11 | 1 |
| 117 | peace | `H2790A` | cha.rash | to plow/plot | H | `extracted` | 2 | 2 | 11 | 1 |
| 117 | peace | `G4623` | siōpaō | be quiet | G | `extracted` | 2 | 1 | 11 | 0 |
| 123 | pride | `H2087` | za.don | arrogance | H | `extracted` | 2 | 1 | 11 | 1 |
| 125 | purity | `H2893` | to.ho.rah | purifying | H | `extracted` | 2 | 2 | 11 | 0 |
| 151 | sorrow | `H0585` | a.na.chah | sighing | H | `extracted` | 2 | 1 | 11 | 1 |
| 157 | temptation | `G3986H` | peirasmos | temptation/testing: testing | G | `extracted` | 2 | 1 | 11 | 0 |
| 159 | testimony | `G3056` | logos | word | G | `extracted` | 2 | 1 | 11 | 0 |
| 174 | wisdom | `H6175` | a.rum | prudent | H | `extracted` | 2 | 2 | 11 | 1 |
| 176 | worship | `H5457` | se.gid | to do homage | H | `extracted` | 2 | 2 | 11 | 0 |
| 180 | yielding | `G1431` | dōrea | free gift | G | `extracted` | 2 | 1 | 11 | 0 |
| 181 | zeal | `G4704` | spoudazō | be eager | G | `extracted` | 2 | 2 | 11 | 1 |
| 187 | strength | `H5810` | a.zaz | be strong | H | `extracted` | 2 | 1 | 11 | 3 |
| 190 | contempt | `G1848` | exoutheneō | to reject | G | `extracted` | 2 | 1 | 11 | 0 |
| 193 | craving | `G3554` | nosos | illness | G | `extracted` | 2 | 1 | 11 | 0 |
| 19 | calling | `G2822` | klētos | called | G | `extracted` | 2 | 1 | 10 | 1 |
| 28 | consecration | `H4720` | miq.dash | sanctuary | H | `extracted` | 2 | 1 | 10 | 1 |
| 28 | consecration | `H5145G` | ne.zer | consecration: Nazirite vow | H | `extracted` | 2 | 1 | 10 | 0 |
| 31 | corruption | `H7845G` | sha.chat | Pit: hell | H | `extracted` | 2 | 1 | 10 | 0 |
| 51 | distress | `H0927` | be.hal | to dismay | H | `extracted` | 2 | 2 | 10 | 0 |
| 51 | distress | `H6693` | tsuq | to press | H | `extracted` | 2 | 2 | 10 | 1 |
| 63 | foolishness | `G0878` | afrōn | foolish | G | `extracted` | 2 | 2 | 10 | 0 |
| 71 | grief | `G3996` | pen.the.o | to mourn | G | `extracted` | 2 | 1 | 10 | 2 |
| 76 | holiness | `G0038` | hagiasmos | holiness | G | `extracted` | 2 | 1 | 10 | 0 |
| 116 | patience | `H0753` | o.rekh | length | H | `extracted` | 2 | 1 | 10 | 0 |
| 139 | righteousness | `G1345` | dikaiōma | righteous act | G | `extracted` | 2 | 1 | 10 | 1 |
| 180 | yielding | `G1929` | epididōmi | to give/deliver | G | `extracted` | 2 | 2 | 10 | 0 |
| 183 | heart | `H2504` | cha.lats | loin | H | `extracted` | 2 | 2 | 10 | 1 |
| 187 | strength | `H5794` | e.zuz | strength | H | `extracted` | 2 | 1 | 10 | 3 |
| 187 | strength | `G3617` | oikodespotēs | householder | G | `extracted` | 2 | 1 | 10 | 0 |
| 191 | doubt | `H2964` | te.reph | prey | H | `extracted` | 2 | 1 | 10 | 0 |
| 191 | doubt | `G3841` | pantokratōr | almighty | G | `extracted` | 2 | 1 | 10 | 0 |
| 197 | authority | `H6485A` | pa.qad | to reckon: list | H | `extracted` | 2 | 1 | 10 | 0 |
| 207 | blindness (spiritual) | `G4653` | skotia | darkness | G | `extracted` | 2 | 2 | 10 | 0 |

## Anomalies

### Registries with no Primary term (33)

| Reg | Word | B | C | U |
|---:|---|---:|---:|---:|
| 2 | agony | 20 | 3 | 6 |
| 3 | ambition | 4 | 4 | 0 |
| 13 | bitterness | 10 | 1 | 0 |
| 29 | contentment | 2 | 0 | 0 |
| 30 | contrition | 6 | 4 | 0 |
| 41 | defilement | 2 | 0 | 0 |
| 46 | devotion | 5 | 0 | 0 |
| 49 | discernment | 5 | 0 | 3 |
| 50 | disobedience | 3 | 0 | 0 |
| 67 | goodness | 2 | 1 | 0 |
| 74 | hardness | 2 | 0 | 4 |
| 85 | imagination | 3 | 0 | 0 |
| 87 | indignation | 2 | 0 | 0 |
| 92 | integrity | 3 | 0 | 0 |
| 93 | intention | 1 | 0 | 0 |
| 96 | jealousy | 1 | 0 | 0 |
| 107 | meaning | 10 | 0 | 1 |
| 115 | passion | 3 | 0 | 0 |
| 130 | reconciliation | 6 | 0 | 0 |
| 131 | rejection | 2 | 0 | 1 |
| 132 | rejoicing | 1 | 0 | 0 |
| 134 | renewal | 3 | 4 | 0 |
| 148 | sincerity | 2 | 0 | 0 |
| 150 | sorcery | 4 | 0 | 1 |
| 153 | stubbornness | 1 | 1 | 2 |
| 156 | surrender | 1 | 0 | 11 |
| 158 | terror | 8 | 0 | 3 |
| 178 | wrath | 5 | 0 | 4 |
| 179 | yearning | 0 | 1 | 0 |
| 189 | malice | 1 | 0 | 0 |
| 203 | treachery | 1 | 0 | 0 |
| 209 | likeness | 2 | 0 | 0 |
| 212 | pray | 1 | 1 | 0 |

### Registries with only Marginal terms (1)

| Reg | Word | C |
|---:|---|---:|
| 179 | yearning | 1 |

### Registries with only Unanalysed terms (0)

_None._
