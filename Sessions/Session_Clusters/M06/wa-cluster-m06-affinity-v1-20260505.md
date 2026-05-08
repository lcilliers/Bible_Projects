# M06 Hate, Contempt and Hostility — affinity scan over T2 + FLAG

**Generated:** 2026-05-05T13:12:49Z  
**Centroid built from:** 36 M-cluster terms in the semantic-weighted vector space  
**Candidates scanned:** 627 T2 + 121 FLAG = 748 terms

**Method:**
- *Semantic similarity* — cosine of each candidate's semantic-weighted vector against the M-cluster centroid
- *Keyword hit* — gloss/meaning/Mounce text contains a love-vocabulary keyword (hate, hated, hatred, hateful, hating, contempt, contemptuous, contemptible, …)

**Tiers:**
- ⭐ **LIKELY** — sim ≥ 0.55 OR (keyword match AND sim ≥ 0.4)
- 🔍 **REVIEW** — 0.4 ≤ sim < 0.55, no keyword hit
- 📌 **KEYWORD-ONLY** — keyword hit but sim < 0.4 (semantic distance large but lexical match)

---

## Tier 1 — LIKELY M05 candidates (0)

*(none)*


## Tier 2 — REVIEW (29)

Mid-similarity, no keyword hit — semantically near but worth a manual look.

| Strong's | Lang | Translit | Gloss | Bucket | Registry | Sim |
|---|---|---|---|---|---|---:|
| H7311B | H | ra.mam | be rotten | T1 | R123 pride | 0.492 |
| H2490C | H | cha.lal | to profane/begin: begin | T2 | R151 sorrow | 0.471 |
| H5324 | H | na.tsav | to stand | T2 | R187 strength | 0.466 |
| H8618 | H | te.qo.mem | to confront | T2 | R187 strength | 0.465 |
| H3744 | H | ka.roz | proclaimer | GENERICS | R051 distress | 0.463 |
| G2900 | G | krataios | mighty | T2 | — | 0.461 |
| H2490I | H | cha.lal | to profane/begin: fruit | T2 | R151 sorrow | 0.456 |
| H1598 | H | ga.nan | to defend | T1 | R151 sorrow | 0.452 |
| H2787 | H | cha.rar | to scorch | T1 | R051 distress | 0.449 |
| H3745 | H | ke.raz | to proclaim | T2 | R051 distress | 0.449 |
| H2250 | H | chab.bu.rah | wound | T2 | R062 fellowship | 0.438 |
| H2266 | H | cha.var | to unite | T2 | R062 fellowship | 0.437 |
| H7413 | H | ra.mah | high place | T2 | R123 pride | 0.431 |
| H2118 | H | za.chach | to remove | T1 | R187 strength | 0.429 |
| H2490A | H | cha.lal | to bore | T2 | R151 sorrow | 0.425 |
| H5327B | H | na.tsah | to desolate | T1 | R152 strife | 0.422 |
| G0500 | G | antichristos | antichrist | T2 | R006 anointing | 0.421 |
| H2491B | H | cha.lal | profaned | T2 | R151 sorrow | 0.417 |
| H6105B | H | a.tsam | to shut eyes | T1 | R187 strength | 0.416 |
| H7115 | H | qo.tser | shortness | T2 | R005 anguish | 0.414 |
| H1793B | H | dak.ka | dust | T2 | R030 contrition | 0.413 |
| H2491H | H | cha.lal | slain: wounded | T2 | R151 sorrow | 0.412 |
| H2940 | H | te.em | command | T2 | — | 0.410 |
| H8641 | H | te.ru.mah | contribution | T2 | R123 pride | 0.410 |
| H7293 | H | ra.hav | Rahab | T2 | — | 0.407 |
| H2963 | H | ta.raph | to tear | T1 | R191 doubt | 0.403 |
| H7465 | H | ro.ah | to shatter | T1 | R151 sorrow | 0.402 |
| H7474 | H | ra.yah | darling | T2 | R103 love | 0.401 |
| H8546 | H | te.mu.tah | death | T2 | R210 deadness | 0.401 |

## Tier 3 — KEYWORD-ONLY (1)

Lexical match but semantic distance large — usually homonyms, metaphorical extensions, or peripheral occurrences. Worth a quick scan but not a primary review queue.

| Strong's | Lang | Translit | Gloss | Bucket | Registry | Sim | Keyword hits |
|---|---|---|---|---|---|---:|---|
| G1847 | G | exoudenoō | be rejected | T2 | R190 contempt | C06 | 0.288 | contempt |

## Top-30 by similarity (any bucket)

| # | Strong's | Lang | Gloss | Bucket | Sim | Keyword hits |
|---|---|---|---|---|---:|---|
| 1 | H7311B | H | be rotten | T1 | 0.492 | — |
| 2 | H2490C | H | to profane/begin: begin | T2 | 0.471 | — |
| 3 | H5324 | H | to stand | T2 | 0.466 | — |
| 4 | H8618 | H | to confront | T2 | 0.465 | — |
| 5 | H3744 | H | proclaimer | GENERICS | 0.463 | — |
| 6 | G2900 | G | mighty | T2 | 0.461 | — |
| 7 | H2490I | H | to profane/begin: fruit | T2 | 0.456 | — |
| 8 | H1598 | H | to defend | T1 | 0.452 | — |
| 9 | H2787 | H | to scorch | T1 | 0.449 | — |
| 10 | H3745 | H | to proclaim | T2 | 0.449 | — |
| 11 | H2250 | H | wound | T2 | 0.438 | — |
| 12 | H2266 | H | to unite | T2 | 0.437 | — |
| 13 | H7413 | H | high place | T2 | 0.431 | — |
| 14 | H2118 | H | to remove | T1 | 0.429 | — |
| 15 | H2490A | H | to bore | T2 | 0.425 | — |
| 16 | H5327B | H | to desolate | T1 | 0.422 | — |
| 17 | G0500 | G | antichrist | T2 | 0.421 | — |
| 18 | H2491B | H | profaned | T2 | 0.417 | — |
| 19 | H6105B | H | to shut eyes | T1 | 0.416 | — |
| 20 | H7115 | H | shortness | T2 | 0.414 | — |
| 21 | H1793B | H | dust | T2 | 0.413 | — |
| 22 | H2491H | H | slain: wounded | T2 | 0.412 | — |
| 23 | H2940 | H | command | T2 | 0.410 | — |
| 24 | H8641 | H | contribution | T2 | 0.410 | — |
| 25 | H7293 | H | Rahab | T2 | 0.407 | — |
| 26 | H2963 | H | to tear | T1 | 0.403 | — |
| 27 | H7465 | H | to shatter | T1 | 0.402 | — |
| 28 | H7474 | H | darling | T2 | 0.401 | — |
| 29 | H8546 | H | death | T2 | 0.401 | — |
| 30 | H3795 | H | beaten | T2 | 0.399 | — |

