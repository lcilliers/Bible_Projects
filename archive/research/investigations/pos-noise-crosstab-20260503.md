# POS-Based Noise Cross-Tab

_Generated 2026-05-03T12:29:52Z_  ·  source: `scripts/_exploratory_pos_noise_crosstab_v1_20260503.py`

Every active OWNER Strong's (3,712) is classified by part-of-speech derived from STEP's local OSHB / SBLG_th morphology. Verse-context state (anchor / relevant / set-aside / muddled) is then aggregated per POS category.

**Filter logic:**
- A Strong's whose POS is a pronoun/particle/preposition/conjunction/
  interjection/article/suffix/adverb is a **grammatical-noise candidate**.
- A Strong's whose POS is noun/verb/adjective carries content; the verse
  classification on it must be evaluated semantically, not auto-filtered.
- The 'suffix' POS is OSHM's tag for pronominal suffixes ('-his', '-her',
  '-my', '-your') attached to nouns and verbs as inflectional morphology.
  These appear as separate Strong's in `mti_terms` and `verse_context` but
  carry no analytical signal in their own right.

## Cross-tab summary

| Category | # Strong's | Total vc | Still relevant | Anchors | Cleanly set aside | Muddled |
|---|---:|---:|---:|---:|---:|---:|
| CONTENT: adjective | 296 | 3,310 | 2,985 | 490 | 128 | 197 |
| CONTENT: noun | 1,275 | 17,687 | 15,612 | 2,160 | 284 | 1,791 |
| CONTENT: verb | 822 | 15,940 | 14,444 | 1,758 | 247 | 1,249 |
| NOISE: adverb | 47 | 437 | 425 | 73 | 0 | 12 |
| NOISE: conjunction | 7 | 136 | 16 | 3 | 0 | 120 |
| NOISE: particle | 50 | 1,105 | 809 | 126 | 0 | 296 |
| NOISE: preposition | 11 | 499 | 190 | 29 | 2 | 307 |
| NOISE: pronoun | 21 | 451 | 59 | 15 | 0 | 392 |
| UNKNOWN: no STEP morph | 20 | 92 | 91 | 22 | 0 | 1 |

## Aggregate noise vs content

| | # Strong's | Total vc | Still relevant | Anchors | Cleanly set aside | Muddled |
|---|---:|---:|---:|---:|---:|---:|
| **NOISE (grammatical)** | 136 | 2,628 | 1,499 | 246 | 2 | 1,127 |
| **CONTENT (noun/verb/adj)** | 2,393 | 36,937 | 33,041 | 4,408 | 659 | 3,237 |

## Top 50 noise Strong's by anchor count

Each row is a Strong's flagged as grammatical noise that nevertheless carries one or more **anchor** designations.

| strongs | translit | gloss | lang | POS | anchors | still rel | total vc |
|---|---|---|---|---|---:|---:|---:|
| `H4310` | mi | who? | H | particle | 20 | 62 | 62 |
| `H2009` | hin.neh | behold | H | particle | 14 | 98 | 98 |
| `H0408` | al | not | H | particle | 14 | 76 | 76 |
| `H3966` | me.od | much | H | adverb | 12 | 93 | 93 |
| `H2005` | hen | look! | H | particle | 12 | 77 | 77 |
| `H4480A` | min- | from | H | preposition | 8 | 25 | 25 |
| `H3808` | lo | not | H | particle | 6 | 56 | 56 |
| `H5978` | im.ma.di | with me | H | preposition | 6 | 18 | 18 |
| `H0639G` | aph | face: anger | H | particle | 5 | 23 | 23 |
| `H3809` | la | not | H | particle | 5 | 23 | 23 |
| `H4069` | mad.du.a | why? | H | particle | 4 | 51 | 51 |
| `H3644G` | ke.mo | like | H | preposition | 4 | 37 | 37 |
| `H4994` | na | please | H | particle | 4 | 27 | 27 |
| `H0587` | a.nach.nu | we | H | pronoun | 4 | 17 | 17 |
| `H5750` | od | still | H | adverb | 4 | 14 | 14 |
| `G1211` | dē | so | G | particle | 4 | 5 | 5 |
| `H1571` | gam | also | H | particle | 3 | 132 | 132 |
| `G3361` | mē | not | G | adverb | 3 | 55 | 55 |
| `H3426` | yesh | there | H | particle | 3 | 40 | 40 |
| `G3779` | houtōs | thus(-ly) | G | adverb | 3 | 32 | 32 |
| `H5227` | no.khach | before | H | preposition | 3 | 7 | 7 |
| `H0328B` | it.ti | mutterer | H | adverb | 3 | 5 | 5 |
| `G0870` | afobōs | fearlessly | G | adverb | 3 | 4 | 4 |
| `G1537` | ek | out from | G | preposition | 2 | 54 | 54 |
| `H3162B` | ya.che.dav | together | H | adverb | 2 | 47 | 47 |
| `H4616` | ma.an | because | H | preposition | 2 | 38 | 38 |
| `G3842` | pantote | always | G | adverb | 2 | 33 | 33 |
| `H1836` | de.nah | this | H | pronoun | 2 | 19 | 19 |
| `H2486` | cha.li.lah | forbid | H | particle | 2 | 19 | 19 |
| `H2493` | che.lem | dream | H | particle | 2 | 18 | 18 |
| `H1097` | be.li | without | H | particle | 2 | 13 | 13 |
| `H6435` | pen- | lest | H | conjunction | 2 | 13 | 13 |
| `H0194` | u.lay | perhaps | H | adverb | 2 | 12 | 12 |
| `H2098` | zu | this | H | particle | 2 | 12 | 12 |
| `H0551` | om.nam | truly | H | adverb | 2 | 9 | 9 |
| `H5974` | im | with | H | preposition | 2 | 8 | 8 |
| `H4101` | mah | what? | H | pronoun | 2 | 7 | 7 |
| `H4479` | man | who? | H | pronoun | 2 | 7 | 7 |
| `G3843` | pantōs | surely | G | adverb | 2 | 6 | 6 |
| `H0363` | i.lan | tree | H | particle | 2 | 6 | 6 |
| `H2090` | zoh | this | H | pronoun | 2 | 6 | 6 |
| `H2417` | chay | living | H | particle | 2 | 6 | 6 |
| `G1346` | dikaiōs | rightly | G | adverb | 2 | 5 | 5 |
| `G3837` | pantachou | everywhere | G | adverb | 2 | 5 | 5 |
| `H0370` | a.yin | where? | H | particle | 2 | 5 | 5 |
| `H1780` | din | judgment | H | particle | 2 | 5 | 5 |
| `G3785` | ofelon | I wish! | G | particle | 2 | 4 | 4 |
| `H2008` | hen.nah | here/thus | H | adverb | 2 | 4 | 4 |
| `H5973B` | me.im | from with | H | preposition | 2 | 3 | 3 |
| `H7535` | raq | except | H | particle | 2 | 3 | 3 |

## Top entries per noise category

### adverb — 47 Strong's, 437 vc rows, 73 anchors

| strongs | translit | gloss | lang | anchors | still rel | total vc |
|---|---|---|---|---:|---:|---:|
| `H3966` | me.od | much | H | 12 | 93 | 93 |
| `H5750` | od | still | H | 4 | 14 | 14 |
| `G3361` | mē | not | G | 3 | 55 | 55 |
| `G3779` | houtōs | thus(-ly) | G | 3 | 32 | 32 |
| `H0328B` | it.ti | mutterer | H | 3 | 5 | 5 |
| `G0870` | afobōs | fearlessly | G | 3 | 4 | 4 |
| `H3162B` | ya.che.dav | together | H | 2 | 47 | 47 |
| `G3842` | pantote | always | G | 2 | 33 | 33 |
| `H0194` | u.lay | perhaps | H | 2 | 12 | 12 |
| `H0551` | om.nam | truly | H | 2 | 9 | 9 |

### conjunction — 7 Strong's, 136 vc rows, 3 anchors

| strongs | translit | gloss | lang | anchors | still rel | total vc |
|---|---|---|---|---:|---:|---:|
| `H6435` | pen- | lest | H | 2 | 13 | 13 |
| `G3379` | mēpote | lest | G | 1 | 3 | 3 |
| `G1161` | de | then | G | 0 | 0 | 60 |
| `G2532` | kai | and | G | 0 | 0 | 60 |
| `G3303` | men | on the other hand | G | 0 | 0 | 0 |
| `H2006A` | hen | if | H | 0 | 0 | 0 |
| `H2006B` | la.hen | therefore | H | 0 | 0 | 0 |

### particle — 50 Strong's, 1,105 vc rows, 126 anchors

| strongs | translit | gloss | lang | anchors | still rel | total vc |
|---|---|---|---|---:|---:|---:|
| `H4310` | mi | who? | H | 20 | 62 | 62 |
| `H2009` | hin.neh | behold | H | 14 | 98 | 98 |
| `H0408` | al | not | H | 14 | 76 | 76 |
| `H2005` | hen | look! | H | 12 | 77 | 77 |
| `H3808` | lo | not | H | 6 | 56 | 56 |
| `H0639G` | aph | face: anger | H | 5 | 23 | 23 |
| `H3809` | la | not | H | 5 | 23 | 23 |
| `H4069` | mad.du.a | why? | H | 4 | 51 | 51 |
| `H4994` | na | please | H | 4 | 27 | 27 |
| `G1211` | dē | so | G | 4 | 5 | 5 |

### preposition — 11 Strong's, 499 vc rows, 29 anchors

| strongs | translit | gloss | lang | anchors | still rel | total vc |
|---|---|---|---|---:|---:|---:|
| `H4480A` | min- | from | H | 8 | 25 | 25 |
| `H5978` | im.ma.di | with me | H | 6 | 18 | 18 |
| `H3644G` | ke.mo | like | H | 4 | 37 | 37 |
| `H5227` | no.khach | before | H | 3 | 7 | 7 |
| `G1537` | ek | out from | G | 2 | 54 | 54 |
| `H4616` | ma.an | because | H | 2 | 38 | 38 |
| `H5974` | im | with | H | 2 | 8 | 8 |
| `H5973B` | me.im | from with | H | 2 | 3 | 3 |
| `H0413` | el | to[wards] | H | 0 | 0 | 307 |
| `H2500` | che.leph | for | H | 0 | 0 | 2 |

### pronoun — 21 Strong's, 451 vc rows, 15 anchors

| strongs | translit | gloss | lang | anchors | still rel | total vc |
|---|---|---|---|---:|---:|---:|
| `H0587` | a.nach.nu | we | H | 4 | 17 | 17 |
| `H1836` | de.nah | this | H | 2 | 19 | 19 |
| `H4101` | mah | what? | H | 2 | 7 | 7 |
| `H4479` | man | who? | H | 2 | 7 | 7 |
| `H2090` | zoh | this | H | 2 | 6 | 6 |
| `H2097` | zo | this | H | 2 | 2 | 2 |
| `H1668` | da | this | H | 1 | 1 | 1 |
| `H0576B` | a.nah | me | H | 0 | 0 | 16 |
| `H0589` | a.ni | I | H | 0 | 0 | 376 |
| `H0607` | an.tah | you | H | 0 | 0 | 0 |
