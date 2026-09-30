# Goodness — Analytic-Readiness (R067)

**Generated:** 2026-04-28 15:16 UTC

**Source:** SQLite `database/bible_research.db` (schema v3.17.0).

**Purpose:** the complete structured data layer for goodness — every term, group, dimension assignment, verse-classification count, anchor verse, quality flag, and cross-registry shared anchor that the analysis is built on. No narrative; the prose interpretation lives in [goodness-1-prose.md](goodness-1-prose.md).


## 1. Registry header

| Field | Value |
| --- | --- |
| `no` | 67 |
| `id` (FK) | 67 |
| `word` | goodness |
| `category_hint` | None |
| `dimensions` (registry-level label) | Moral/Conscience |
| `cluster_assignment` | C10 |
| `sb_classification` | None |
| `phase1_status` | Complete |
| `verse_context_status` | Complete |
| `session_b_status` | Analysis Complete |
| `dim_review_status` | None |
| `dim_review_version` | None |
| `phase1_term_count` | 45 |
| `phase1_verse_count` | 2216 |
| `unique_term_count` | 0 |
| `shared_term_count` | 45 |
| `term_sharing_ratio` | 1.0 |
| `strongs_list` | [{"strong": "H3651C", "count": 381}, {"strong": "H2896A", "count": 306}, {"strong": "H5927G", "count": 305}, {"strong": "H5921A", "count": 295}, {"strong": "H5930A", "count": 225}, {"strong": "H5930B", "count": 225}, {"strong": "H5927H", "count": 145}, {"strong": "H3588B", "count": 136}, {"strong": "H4605", "count": 134}, {"strong": "G0018", "count": 90}, {"strong": "H2896B", "count": 89}, {"strong": "H5922", "count": 86}, {"strong": "H5927I", "count": 84}, {"strong": "H2896C", "count": 62}, {"strong": "H2898", "count": 31}, {"strong": "H5945B", "count": 25}, {"strong": "H4609B", "count": 23}, {"strong": "H2895", "count": 20}, {"strong": "H5944", "count": 20}, {"strong": "H5945A", "count": 20}, {"strong": "H5945G", "count": 20}, {"strong": "H5945H", "count": 20}, {"strong": "G2570G", "count": 18}, {"strong": "H4608", "count": 18}, {"strong": "H4609A", "count": 16}, {"strong": "H5929", "count": 13}, {"strong": "H5927J", "count": 11}, {"strong": "H3588C", "count": 10}, {"strong": "H5921B", "count": 10}, {"strong": "H8585A", "count": 9}, {"strong": "H8585B", "count": 9}, {"strong": "G0015", "count": 8}, {"strong": "H3652", "count": 8}, {"strong": "G5544", "count": 7}, {"strong": "H5927L", "count": 7}, {"strong": "H5927M", "count": 7}, {"strong": "H5927K", "count": 6}, {"strong": "G0019", "count": 4}, {"strong": "H5920H", "count": 4}, {"strong": "G0014", "count": 2}, {"strong": "H2869", "count": 2}, {"strong": "H5942", "count": 2}, {"strong": "G0016", "count": 1}, {"strong": "G0017", "count": 1}, {"strong": "G0865", "count": 1}, {"strong": "G5358", "count": 1}, {"strong": "H4607", "count": 1}, {"strong": "H5924", "count": 1}, {"strong": "H5940", "count": 1}] |

**Description (researcher-authored, do not pipeline-overwrite):**

> Goodness is the quality of being genuinely, structurally beneficial — not just pleasing or approved but actually doing good in the deep sense of the word. The Hebrew and Greek vocabulary runs from the aesthetic (pleasant, beautiful) through the moral (righteous, beneficial) to the relational (kind). God is described as good at the very beginning of creation: what he makes is good because it reflects his character. Human goodness is derivative: a participation in and reflection of the goodness that originates in God.

**`inference_note`:** (none)


## 2. Term inventory

**Counts:** 3 OWNER + 42 XREF = 45 total. OWNER active verses = **317**.

XREF rows show `active=0` because XREF verse copies are `delete_flagged=1` by design (verses live on the OWNER side; XREF rows are reference-only). The `total_v` column shows the verse count carried into the file when the term was first ingested.


### 2.1 OWNER terms

| Strong's | Translit | Lang | active | total | step_search_gloss | occ_count |
| --- | --- | --- | ---: | ---: | --- | ---: |
| G0019 | agathōsunē | Greek | 4 | 4 | goodness | 17 |
| G5544 | chrēstotēs | Greek | 7 | 7 | kindness | 23 |
| H2896A | tov | Hebrew | 306 | 306 | pleasant | 409 |

### 2.2 XREF terms

| Strong's | Translit | Lang | total | step_search_gloss | occ_count | source |
| --- | --- | --- | ---: | --- | ---: | --- |
| G0014 | agathoergeō | Greek | 2 | to do good | 2 |  |
| G0015 | agathopoieō | Greek | 8 | to do good | 14 |  |
| G0016 | agathopoiia | Greek | 1 | doing good | 1 |  |
| G0017 | agathopoios | Greek | 1 | doing good | 1 |  |
| G0018 | agathos | Greek | 90 | good | 505 |  |
| G0865 | afilagathos | Greek | 1 | hating good | 1 |  |
| G5358 | filagathos | Greek | 1 | lover of good | 1 |  |
| H2869 | tav | Hebrew | 2 | fine | 2 |  |
| H2895 | tov | Hebrew | 20 | be pleasing | 23 |  |
| H2896B | tov | Hebrew | 89 | good | 90 |  |
| H2896C | to.vah | Hebrew | 62 | welfare | 64 |  |
| H2898 | tuv | Hebrew | 31 | goodness | 32 |  |
| H3588B | ki m | Hebrew | 136 | that if: except | 313 |  |
| H3588C | ki al ken | Hebrew | 10 | for as that: since | 28 |  |
| H3652 | ken | Hebrew | 8 | thus | 8 |  |
| H4605 | ma.al | Hebrew | 134 | above | 144 |  |
| H4607 | mo.al | Hebrew | 1 | lifting | 1 |  |
| H4608 | ma.a.leh | Hebrew | 18 | ascent | 27 |  |
| H4609A | ma.a.lah | Hebrew | 16 | thought | 1 |  |
| H4609B | ma.a.lah | Hebrew | 23 | step | 53 |  |
| H5920H | al | Hebrew | 4 | height | 4 |  |
| H5922 | al | Hebrew | 86 | since | 133 |  |
| H5924 | el.la | Hebrew | 1 | above | 1 |  |
| H5927G | a.lah | Hebrew | 305 | to ascend: rise | 624 |  |
| H5927H | a.lah | Hebrew | 145 | to ascend: establish | 153 |  |
| H5927I | a.lah | Hebrew | 84 | to ascend: offer up | 91 |  |
| H5927J | a.lah | Hebrew | 11 | to ascend: attack | 12 |  |
| H5927K | a.lah | Hebrew | 6 | to ascend: copulate | 6 |  |
| H5927L | a.lah | Hebrew | 7 | to ascend: dawn | 10 |  |
| H5927M | a.lah | Hebrew | 7 | to ascend: regurgitate | 9 |  |
| H5929 | a.leh | Hebrew | 13 | leaf | 18 |  |
| H5930A | o.lah | Hebrew | 225 | burnt offering | 288 |  |
| H5930B | o.lah | Hebrew | 225 | ascent | 4 |  |
| H5940 | e.li | Hebrew | 1 | pestle | 1 |  |
| H5942 | il.li | Hebrew | 2 | upper | 2 |  |
| H5944 | a.liy.yah | Hebrew | 20 | upper room | 20 |  |
| H5945A | el.yon | Hebrew | 20 | high | 20 |  |
| H5945B | el.yon | Hebrew | 25 | Most High [God] | 25 |  |
| H5945G | el.yon | Hebrew | 20 | Upper [Beth Horon] | 3 |  |
| H5945H | el.yon | Hebrew | 20 | [LORD] Most High | 5 |  |
| H8585A | te.a.lah | Hebrew | 9 | conduit | 9 |  |
| H8585B | te.a.lah | Hebrew | 9 | healing | 2 |  |

## 3. Verse Context groups (OWNER terms)

**Total groups:** 12.

### 884-001 (Strong's H2896A)

- **Relevant verses:** 22  ·  **Anchor verses:** 2  ·  **Related verses:** 20
- **Description:** Term declares God's inner being as good — the foundational doxological assertion that God's character, name, steadfast love, and Spirit are good, and that his goodness governs his relationship to all he has made
- **Anchors:**
  - **Psa 34:8** — Psa 34:8 Oh, taste and see that the Lord is good ! Blessed is the man who takes refuge in him !
  - **Psa 119:68** — Psa 119:68 You are good and do good ; teach me your statutes .

### 884-002 (Strong's H2896A)

- **Relevant verses:** 39  ·  **Anchor verses:** 1  ·  **Related verses:** 38
- **Description:** Term names human moral character and conduct as good — the inner quality of the person who walks uprightly, acts honestly, and whose character is recognised and assessed as good before God and others
- **Anchors:**
  - **Mic 6:8** — Mic 6:8 He has told you , O man , what is good ; and what does the Lord require of you but to do justice , and to love kindness , and to walk humbly with your God ?

### 884-003 (Strong's H2896A)

- **Relevant verses:** 36  ·  **Anchor verses:** 1  ·  **Related verses:** 35
- **Description:** Term names goodness as inner experiential good — what is genuinely good for the human person: proximity to God, worship, waiting, communal harmony, and the reorientation of the inner life toward what truly satisfies
- **Anchors:**
  - **Psa 73:28** — Psa 73:28 But for me it is good to be near God ; I have made the Lord God my refuge , that I may tell of all your works .

### 884-004 (Strong's H2896A)

- **Relevant verses:** 42  ·  **Anchor verses:** 2  ·  **Related verses:** 40
- **Description:** Term names comparative wisdom good — the better-than sayings of wisdom literature where inner and relational qualities are ranked as the greater good above material wealth, social status, or external abundance
- **Anchors:**
  - **Pro 15:16** — Pro 15:16 Better is a little with the fear of the Lord than great treasure and trouble with it .
  - **Pro 16:32** — Pro 16:32 Whoever is slow to anger is better than the mighty , and he who rules his spirit than he who takes a city .

### 884-005 (Strong's H2896A)

- **Relevant verses:** 17  ·  **Anchor verses:** 1  ·  **Related verses:** 16
- **Description:** Term names God's good word and promise — the covenantal faithfulness through which God declares, fulfils, and sustains his promised good toward his people
- **Anchors:**
  - **Jos 23:14** — Jos 23:14 “And now I am about to go the way of all the earth , and you know in your hearts and souls , all of you, that not one word has failed of all the good things that the Lord your God promised concerning you. All have come to pass for you; not one of them has failed .

### 884-006 (Strong's H2896A)

- **Relevant verses:** 22  ·  **Anchor verses:** 1  ·  **Related verses:** 21
- **Description:** Term names the moral assessment of conduct, ways, or deeds as not good — the prophetic and wisdom verdict that certain inner orientations and behavioural expressions are contrary to the good God requires
- **Anchors:**
  - **Eze 36:31** — Eze 36:31 Then you will remember your evil ways , and your deeds that were not good , and you will loathe yourselves for your iniquities and your abominations .

### 884-007 (Strong's H2896A)

- **Relevant verses:** 7  ·  **Anchor verses:** 1  ·  **Related verses:** 6
- **Description:** Term names God's evaluative pronouncement on his creation — the divine inner-being action of judging-and-declaring-good in Gen 1, where the Creator inspects what he has made and pronounces it good or very good
- **Anchors:**
  - **Gen 1:31** — Gen 1:31 And God saw everything that he had made , and behold , it was very good . And there was evening and there was morning , the sixth day .

### 884-008 (Strong's H2896A)

- **Relevant verses:** 40  ·  **Anchor verses:** 1  ·  **Related verses:** 39
- **Description:** Term names what is good-in-the-eyes-of / pleasing to / preferred-by an actor — the volitional-preference idiom in which the term is the predicate of someone's will or evaluative agreement, naming what they choose, prefer, agree to, or judge fitting
- **Anchors:**
  - **Jer 26:14** — Jer 26:14 But as for me , behold , I am in your hands . Do with me as seems good and right to you .

### 884-009 (Strong's H2896A)

- **Relevant verses:** 5  ·  **Anchor verses:** 1  ·  **Related verses:** 4
- **Description:** Term names a state of inner well-being — the shalom-condition of being-well, prospering, glad-of-heart, or well-disposed — the inner-being state experienced or sought by the human person
- **Anchors:**
  - **Est 5:9** — Est 5:9 And Haman went out that day joyful and glad of heart . But when Haman saw Mordecai in the king’s gate , that he neither rose nor trembled before him, he was filled with wrath against Mordecai .

### 885-001 (Strong's G0019)

- **Relevant verses:** 4  ·  **Anchor verses:** 1  ·  **Related verses:** 3
- **Description:** Term names goodness as an inner-being disposition and Spirit-produced fruit — a quality that fills the person and is completed by God, expressed in righteous conduct and resolve
- **Anchors:**
  - **Gal 5:22** — Gal 5:22 But the fruit of the Spirit is love , joy , peace , patience , kindness , goodness , faithfulness ,

### 886-001 (Strong's G5544)

- **Relevant verses:** 3  ·  **Anchor verses:** 1  ·  **Related verses:** 2
- **Description:** Term names kindness as God's inner disposition of generous goodwill toward humanity — the divine attribute that leads to repentance, governs judgment and mercy, and is displayed supremely in Christ
- **Anchors:**
  - **Rom 11:22** — Rom 11:22 Note then the kindness and the severity of God : severity toward those who have fallen , but God’s kindness to you , provided you continue in his kindness . Otherwise you too will be cut off .

### 886-002 (Strong's G5544)

- **Relevant verses:** 4  ·  **Anchor verses:** 1  ·  **Related verses:** 3
- **Description:** Term names kindness as a Spirit-produced inner quality of the believer — the disposition to act with goodness toward others, listed as fruit of the Spirit and garment of the renewed person
- **Anchors:**
  - **Gal 5:22** — Gal 5:22 But the fruit of the Spirit is love , joy , peace , patience , kindness , goodness , faithfulness ,

## 4. Verse classification summary

| Metric | Count |
| --- | ---: |
| Anchor verses | 14 |
| Relevant (in-group) | 241 |
| Related (cross-reference) | 227 |
| Set-aside (with reason) | 75 |
| Total verse_context rows | 317 |

**Set-aside reason breakdown:**

| Reason | Count |
| --- | ---: |
| physical_only | 59 |
| no_inner_being | 16 |

## 5. Cluster and dimension review

- **Cluster assignment:** `C10`
- **`dim_review_status`:** `None`  ·  **version:** `None`
- **registry-level dimension label (`word_registry.dimensions`):** `Moral/Conscience`

## 6. Group → dimension mapping (per Session B obslog v3)

The 12 OWNER groups carry the following dimension assignments per the goodness Session B Stage 2 work. Three are tagged provisional pending dimension review (SP-067-014, -016, and the GAP-N-related dimensions for 884-007 and 884-009).

| Group | Strong's | Dimension | Status |
| --- | --- | --- | --- |
| 884-001 | H2896A | 11 — Divine-Human Correspondence | confirmed |
| 884-002 | H2896A | 05 — Moral Character | confirmed |
| 884-003 | H2896A | 05 — Moral Character | provisional (SP-067-014: may belong to Dependence/Creatureliness 08) |
| 884-004 | H2896A | 03 — Cognition | confirmed |
| 884-005 | H2896A | 05 — Moral Character | provisional (SP-067-016: may be 11 — divine faithfulness focus) |
| 884-006 | H2896A | 03 — Cognition | confirmed |
| 884-007 | H2896A | 11 provisional | needs sub-category for ontological-creative pronouncement (GAP-N-003 → SP-067-026 substream) |
| 884-008 | H2896A | 04 — Volition | confirmed |
| 884-009 | H2896A | dimension uncertain | no current label fits cleanly (GAP-N-001/002 → SP-067-019/020 substream) |
| 885-001 | G0019 | 04 — Volition | confirmed |
| 886-001 | G5544 | 11 — Divine-Human Correspondence | confirmed (divine chrēstotēs) |
| 886-002 | G5544 | 05 — Moral Character | confirmed (Spirit-produced kindness) |

_Note: dimension assignments are not currently stored as a structured field per group in the schema — they are recorded in the obslog narrative and reflected in `wa_session_research_flags` SP-067-014/-016 and the migrated GAP-N pointers. This table is reproduced here for data-layer completeness; it is not derived from the DB._

## 7. Co-occurrence with other registries (via shared verse references)

Other registries that share verse references with R067's OWNER active verses. Counts are distinct (book, chapter, verse) tuples; the same verse may appear across multiple R067 OWNER terms but is counted once. OWNER-only on both sides.

| Registry | Word | Shared verses |
| ---: | --- | ---: |
| R187 | strength | 32 |
| R103 | love | 28 |
| R043 | desire | 27 |
| R197 | authority | 25 |
| R121 | praise | 22 |
| R044 | despair | 22 |
| R173 | will | 21 |
| R051 | distress | 20 |
| R117 | peace | 18 |
| R100 | knowledge | 17 |
| R090 | innocence | 17 |
| R057 | evil | 15 |
| R008 | appetite | 15 |
| R097 | joy | 15 |
| R182 | Soul | 14 |
| R156 | surrender | 13 |
| R168 | uprightness | 13 |
| R183 | heart | 13 |
| R140 | seeking | 12 |
| R167 | unity | 11 |
| R174 | wisdom | 11 |
| R023 | compassion | 11 |
| R099 | kindness | 11 |
| R198 | might | 10 |
| R213 | listen | 10 |

## 8. Explicit cross-registry links (`wa_cross_registry_links`)

_No explicit `wa_cross_registry_links` rows. Cross-registry connections in the prose are derived from shared anchor verses (see §7 above and §9 below) and recorded as SD pointers, not as structured link rows. This is a known data-layer gap._


## 9. Shared anchor verses (verses anchoring multiple registries)

Verses where the same (book, chapter, verse) appears as an anchor in another registry's OWNER VC group.

| Reference | Also anchored in |
| --- | --- |
| Gen 1:31 | experience/R58 |
| Est 5:9 | joy/R97 |
| Psa 34:8 | hope/R78; discernment/R49 |
| Pro 16:32 | patience/R116; anger/R4; dominion/R199 |
| Eze 36:31 | abomination/R1 |
| Mic 6:8 | love/R103; kindness/R99; will/R173; humility/R80; compassion/R23; condemnation/R24 |
| Gal 5:22 | love/R103; patience/R116; joy/R97; peace/R117; faith/R59 |

## 10. Quality flags (`wa_data_quality_flags`)

| flag_code | count |
| --- | ---: |
| NO_WORD_ANALYSIS | 49 |
| PROSE_ONLY_MEANING | 39 |
| VERSE_EVIDENCE_CONCENTRATED | 26 |
| VERSE_EVIDENCE_HIGH | 4 |


**Evidence-flag detail (informational, never gating per M29):**

| flag_code | term_id | description |
| --- | --- | --- |
| VERSE_EVIDENCE_CONCENTRATED | G0014 | Only 2 confirmed verse records for G0014. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | G0015 | Low occurrence count: 14. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | G0016 | Only 1 confirmed verse records for G0016. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | G0017 | Only 1 confirmed verse records for G0017. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | G0019 | Only 4 confirmed verse records for G0019. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | G0865 | Only 1 confirmed verse records for G0865. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | G5358 | Only 1 confirmed verse records for G5358. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | H2869 | Only 2 confirmed verse records for H2869. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | H3652 | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H4607 | Only 1 confirmed verse records for H4607. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | H4609A | Low occurrence count: 1. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5920H | Only 4 confirmed verse records for H5920H. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | H5921B | Low occurrence count: 4. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5924 | Only 1 confirmed verse records for H5924. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | H5927J | Low occurrence count: 12. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5927K | Low occurrence count: 6. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5927L | Low occurrence count: 10. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5927M | Low occurrence count: 9. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5929 | Low occurrence count: 18. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5930B | Low occurrence count: 4. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5940 | Only 1 confirmed verse records for H5940. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | H5942 | Only 2 confirmed verse records for H5942. Threshold is 5. |
| VERSE_EVIDENCE_CONCENTRATED | H5945G | Low occurrence count: 3. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H5945H | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H8585A | Low occurrence count: 9. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_CONCENTRATED | H8585B | Low occurrence count: 2. Statistical patterns unreliable with fewer than 20 occurrences. |
| VERSE_EVIDENCE_HIGH | G0018 | High-frequency term: 505 occurrences. Verse sample represents a subset of all occurrences. |
| VERSE_EVIDENCE_HIGH | H3651C | High-frequency term: 750 occurrences. Verse sample represents a subset of all occurrences. |
| VERSE_EVIDENCE_HIGH | H5921A | High-frequency term: 5802 occurrences. Verse sample represents a subset of all occurrences. |
| VERSE_EVIDENCE_HIGH | H5927G | High-frequency term: 624 occurrences. Verse sample represents a subset of all occurrences. |

## 11. Analytical artefact counts (Session B onward)

| Artefact | Count |
| --- | ---: |
| Active Session B findings (`wa_session_b_findings`) | 52 |
| · of which OBSERVATION type | 49 |
| · of which DATA_ANOMALY_* | 2 |
| · of which DIMENSION_REVIEW | 1 |
| Open `wa_session_research_flags` (any type) | 49 |
| · of which SD_POINTER (Session D) | 26 |
| · of which SB_FINDING | 23 |
| Q&A finding-catalogue links | 76 |
| Distinct cited verses (`wa_finding_entity_links`, type=verse) | 22 |
| Distinct cited groups (`wa_finding_entity_links`, type=group) | 12 |

The linked detail of each finding lives in [goodness-3-open-flags.md](goodness-3-open-flags.md), [goodness-4-qa-list.md](goodness-4-qa-list.md), and [goodness-5-citations.md](goodness-5-citations.md).
