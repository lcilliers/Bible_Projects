# Mode field (#4) — what the contents look like

> Generated 2026-06-15 (v2 — uses `scripts/analytics/morph_util.py`, the canonical classifier). Mode = `wa_verse_records.morph_code` + `stem`. Greek indeclinables (`ADV`/`CONJ`/`PREP`/`PRT`) and Aramaic codes are now labelled correctly.

## How to read a morph code

| code | language | what it says |
|---|---|---|
| `HVpi3ms` | Hebrew | **V**erb · **Pi**el · imperfect · 3ms |
| `HNcfsc` | Hebrew | **N**oun · common · fem · sing · construct |
| `AVqi3ms` | Aramaic | **V**erb · `q`=Peal · imperfect · 3ms |
| `N-DSF` | Greek | **N**oun · Dative Sing Fem |
| `A-NSM` | Greek | **A**djective · Nom Sing Masc |
| `ADV` | Greek | adverb (indeclinable) |
| (blank) | — | function word — no morphology |

## Psa 78:38 — Hebrew (verbs · nouns · adjective)

| strongs | translit | cc | morph_code | stem | → mode (readable) |
|---|---|---|---|---|---|
| H2534 | che.mah | M02 | `HNcfsc` | — | Hebrew noun |
| H7349 | ra.chum | M05 | `HAamsa` | — | Hebrew adjective |
| H5771G | a.von | M10 | `HNcmsa` | — | Hebrew noun |
| H3722A | kip.per | M11 | `HVpi3ms` | Piel | Hebrew verb · Piel |
| H7235A | ra.vah | M23 | `HVhq3ms` | Hiphil | Hebrew verb · Hiphil |
| H5782 | ur | M25 | `HVhi3ms` | Hiphil | Hebrew verb · Hiphil |
| H7843 | sha.chat | M27 | `HVhi3ms` | Hiphil | Hebrew verb · Hiphil |
| H3722B | ka.phar | M38 | `HVpi3ms` | Piel | Hebrew verb · Piel |
| H7725O | shuv | M45 | `HVhcc` | Hiphil | Hebrew verb · Hiphil |
| H0639G | aph | T2 | `HNcmsc` | — | Hebrew noun |

## Rom 15:13 — Greek (noun · adjective · verb)

| strongs | translit | cc | morph_code | stem | → mode (readable) |
|---|---|---|---|---|---|
| G5479 | chara | M04 | `N-GSF` | — | Greek noun |
| G1680 | elpis | M18 | `N-GSF` | — | Greek noun |
| G0040G | hagios | M22 | `A-GSN` | — | Greek adjective |
| G1411 | dunamis | M23 | `N-DSF` | — | Greek noun |
| G4151G | pneuma | M25 | `N-GSN` | — | Greek noun |
| G4100 | pisteuō | M31 | `V-PAN` | — | Greek verb |
| G1515 | eirēnē | M33 | `N-GSF` | — | Greek noun |
| G4137 | plēroō | T2 | `V-AAO-3S` | — | Greek verb |

## Dan 2:20 — Aramaic (Peal verb + indeclinables)

| strongs | translit | cc | morph_code | stem | → mode (readable) |
|---|---|---|---|---|---|
| H2452 | chokh.mah | M15 | `ANcfsd` | — | Aramaic noun |
| H1370 | ge.vu.rah | T2 | `ANcfsd` | — | Aramaic noun |
| H1934 | ha.va | T2 | `AVqi3ms` | Peal | Aramaic verb · Peal |
| H4481 | min- | T2 | `AR` | — | Aramaic preposition |
| H1768 | di | T2 | `AC` | — | Aramaic conjunction |
| H1932 | hu | T2 | `APp3fs` | — | Aramaic pronoun |

## Corpus distribution (clustered active with mode: 58,654)

| language · category | count |
|---|---|
| Hebrew noun | 20,053 |
| Hebrew verb | 17,512 |
| Greek noun | 4,867 |
| Greek verb | 4,215 |
| Hebrew adjective | 3,517 |
| Hebrew pronoun | 2,111 |
| Hebrew particle | 1,984 |
| Greek adjective | 1,463 |
| Hebrew preposition | 758 |
| Hebrew adverb | 641 |
| Aramaic noun | 241 |
| Aramaic verb | 210 |
| Greek adverb | 177 |
| Hebrew conjunction | 175 |
| Greek preposition | 136 |
| Greek conjunction | 120 |
| Aramaic particle | 112 |
| Aramaic conjunction | 81 |
| Aramaic preposition | 80 |
| Aramaic pronoun | 74 |
| Aramaic adjective | 61 |
| Greek particle | 58 |
| Aramaic adverb | 7 |
| Greek article | 1 |

## Verb stems / binyanim

| stem | count |
|---|---|
| Qal | 10,891 |
| Hiphil | 2,419 |
| Piel | 2,116 |
| Niphal | 1,365 |
| Hithpael | 529 |
| Peal | 133 |
| Pual | 110 |
| Hophal | 77 |
| Pael | 22 |
| Haphel | 20 |
| Hithpeel | 13 |
| Hithpaal | 9 |
| Peil | 8 |
| Polpal | 5 |
| Tiphil | 3 |
| Hithaphel | 1 |
| Nithpael | 1 |