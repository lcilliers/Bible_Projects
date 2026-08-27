# Session A Extract — r060 faithfulness

_Generated: 2026-05-02T05:52:55Z_
_Mechanical extract — do not hand-edit body; edit schema and regenerate._

## Table of Contents

- [Section 1 — Summary (Registry Orientation)](#section-1-summary-registry-orientation)
- [Section 2 — Meaning (Lexical / Semantic)](#section-2-meaning-lexical-semantic)
- [Section 3 — Terms (OWNER + XREF) with Analytical Metadata](#section-3-terms-owner-xref-with-analytical-metadata)
- [Section 4 — Verses by Group (with Dimensions and Annotations)](#section-4-verses-by-group-with-dimensions-and-annotations)
- [Section 5 — Research Pointers, Findings, and Cross-Registry Links](#section-5-research-pointers-findings-and-cross-registry-links)
- [Section 6 — Analytic Questions (Catalogue + Registry Extensions)](#section-6-analytic-questions-catalogue-registry-extensions)

---

<!-- PROSE_SECTION
type: sa_s1_d1
registry: 60
version: 1
status: approved
author: claude_code
-->

## Section 1 — Summary (Registry Orientation)

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:52:51Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `word_registry`, `wa_term_inventory`, `wa_verse_records`, `verse_context_group`, `wa_dimension_index` |
| Notes | Word synopsis is researcher-authored (`word_registry.word_synopsis`, M21). NULL means authoring is pending — see Action S programme note. |

### 1.1 Word identity

| Field | Value |
|---|---|
| Word | **faithfulness** |
| Registry no | 60 |
| Cluster | C10 |
| Carry forward | 1 |

### 1.2 Word synopsis

_Word synopsis not yet authored. Researcher to populate `word_registry.word_synopsis` (M21)._

### 1.3 Programme state

| Field | Value |
|---|---|
| session_b_status | Verse Context Reset |
| verse_context_status | Complete |
| dim_review_status | — |
| dim_review_version | — |
| phase1_status | Complete |

### 1.4 Term & verse population (registry-recorded)

| Field | Value |
|---|---|
| unique_term_count | 0 |
| shared_term_count | 29 |
| term_sharing_ratio | 1.0 |
| phase1_term_count | 29 |
| phase1_verse_count | 953 |

### 1.5 Registry-level dimension list

`Moral/Conscience`

### 1.6 Derived counts (confirmatory)

| Field | Value |
|---|---|
| OWNER terms (active) | 1 |
| XREF terms (active) | 28 |
| Active verse records | 242 |
| Active verse-context groups | 7 |
| Active dimension assignments | 7 |

<!-- PROSE_SECTION
type: sa_s1_d2
registry: 60
version: 1
status: approved
author: claude_code
-->

## Section 2 — Meaning (Lexical / Semantic)

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:52:51Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `wa_term_inventory.meaning`, `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` |
| Notes | Rendered per OWNER term (1 terms). Raw meaning text lives in `wa_term_inventory.meaning`; structured parse in `wa_meaning_*` tables. |

### 2.H5414G — H5414G (na.tan) — Hebrew

_step gloss: to give: give · analysis gloss: to give: give_

_No raw meaning text for this term._

**Parse metadata:** senses=1 · stems=0 · causative=0 · domain_tags=0 · parser=1.0.0

**Senses:**

| # | Level | Stem? | Stem label | Domain | Sense text |
|---|---|---|---|---|---|
| 0 | 1 (d1) | 0 | — | — | : give/deliver/send/produce 1) to give, put, set 1a) (Qal) 1a1) to give, bestow, grant, permit, ascribe, employ, devote, consecrate, dedicate, pay wages, sell, exchange, lend, commit, entrust, give over, deliver up, yield produce, occasion, produce, requite to, report, mention, utter, stretch out, extend 1a2) to put, set, put on, put upon, set, appoint, assign, designate 1a3) to make, constitute 1b) (Niphal) 1b1) to be given, be bestowed, be provided, be entrusted to, be granted to, be permitted, be issued, be published, be uttered, be assigned 1b2) to be set, be put, be made, be inflicted 1c) (Hophal) 1c1) to be given, be bestowed, be given up, be delivered up 1c2) to be put upon |

<!-- PROSE_SECTION
type: sa_s1_d4
registry: 60
version: 1
status: approved
author: claude_code
-->

## Section 3 — Terms (OWNER + XREF) with Analytical Metadata

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:52:51Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `wa_term_inventory`, `mti_terms`, `mti_term_flags`, `wa_data_quality_flags`, `wa_term_root_family`, `wa_term_related_words`, `wa_verse_records` |
| Notes | Total active terms: 29. OWNER listed first, then XREF. |

### 3.OWNER.H5414G — H5414G (na.tan) — OWNER

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | to give: give |
| Analysis gloss | to give: give |
| Occurrence count | 1324 |
| Causative form present | 1 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 60 (this registry) |
| owning_word | faithfulness |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_HIGH` | R_AI_WIDER_CONTEXT | High-frequency term: 1324 occurrences. Verse sample represents a subset of all occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H5414G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H5414G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_HIGH` | R_AI_WIDER_CONTEXT | High-frequency term: 1324 occurrences. Verse sample represents a subset of all occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H5414G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H5414G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_HIGH` | R_AI_WIDER_CONTEXT | High-frequency term: 1324 occurrences. Verse sample represents a subset of all occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H5414G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H5414G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 2 |
| 01 — Emotion — Positive | KEYWORD_WEAK | 1 |
| 03 — Cognition | KEYWORD_WEAK | 1 |
| 04 — Volition | KEYWORD_WEAK | 1 |
| 06 — Relational Disposition | KEYWORD_STRONG | 1 |
| 11 — Divine-Human Correspondence | KEYWORD_WEAK | 1 |

**Root family:**

| Root | Language | Gloss | Note |
|---|---|---|---|
| `NATAN` | Hebrew | to give: give | Backfilled 2026-04-09 from wa_term_related_words clustering |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H4976 | mat.tan | gift | — |
| H4977G | mat.tan | Mattan | — |
| H4977H | mat.tan | Mattan | — |
| H4979 | mat.ta.nah | gift | — |
| H4980 | mat.ta.nah | Mattanah | — |
| H4982G | mat.te.nay | Mattenai | — |
| H4982H | mat.te.nay | Mattenai | — |
| H4982I | mat.te.nay | Mattenai | — |
| H4983G | mat.tan.ya.hu | Mattaniah | — |
| H4983H | mat.tan.ya.hu | Mattaniah | — |
| H4983I | mat.tan.ya.hu | Mattaniah | — |
| H4983J | mat.tan.ya.hu | Mattaniah | — |
| H4983K | mat.tan.ya.hu | Mattaniah | — |
| H4983L | mat.tan.ya.hu | Mattaniah | — |
| H4983M | mat.tan.ya.hu | Mattaniah | — |
| H4983N | mat.tan.ya.hu | Mattaniah | — |
| H4983O | mat.tan.ya.hu | Mattaniah | — |
| H4983P | mat.tan.ya.hu | Mattaniah | — |
| H4983Q | mat.tan.ya.hu | Mattaniah | — |
| H4991 | mat.tat | gift | — |
| H4992 | mat.tat.tah | Mattattah | — |
| H4993G | mat.tit.ya.hu | Mattithiah | — |
| H4993H | mat.tit.ya.hu | Mattithiah | — |
| H4993I | mat.tit.ya.hu | Mattithiah | — |
| H4993J | mat.tit.ya.hu | Mattithiah | — |
| H5411 | ne.ti.nim | temple servant | — |
| H5414H | na.tan | to give: put | — |
| H5414I | na.tan | to give: make | — |
| H5414J | na.tan | to give: turn | — |
| H5414K | na.tan | to give: allow | — |
| H5414L | na.tan | to give: throw | — |
| H5414M | na.tan | to give: cry out | — |
| H5414N | na.tan | to give: pay | — |
| H5414O | na.tan | to give: give [marriage] | — |
| H5414P | na.tan | to give: do | — |
| H5414Q | na.tan | to give: if only! | — |
| H5415G | ne.tan | to give: give | — |
| H5415H | ne.tan | to give: put | — |
| H5415I | ne.tan | to give: pay | — |
| H5416G | na.tan | Nathan | — |
| H5416H | na.tan | Nathan | — |
| H5416I | na.tan | Nathan | — |
| H5416J | na.tan | Nathan | — |
| H5416K | na.tan | Nathan | — |
| H5416L | na.tan | Nathan | — |
| H5417G | ne.tan.el | Nethanel | — |
| H5417H | ne.tan.el | Nethanel | — |
| H5417I | ne.tan.el | Nethanel | — |
| H5417J | ne.tan.el | Nethanel | — |
| H5417K | ne.tan.el | Nethanel | — |
| H5417L | ne.tan.el | Nethanel | — |
| H5417M | ne.tan.el | Nethanel | — |
| H5417N | ne.tan.el | Nethanel | — |
| H5417O | ne.tan.el | Nethanel | — |
| H5417P | ne.tan.el | Nethanel | — |
| H5418G | ne.tan.ya.hu | Nethaniah | — |
| H5418H | ne.tan.ya.hu | Nethaniah | — |
| H5418I | ne.tan.ya.hu | Nethaniah | — |
| H5418J | ne.tan.ya.hu | Nethaniah | — |
| H5419 | ne.tan-me.lekh | Nathan-melech | — |

**Verse record counts:** total=242, active=242, delete_flagged=0.

### 3.XREF.G0569 — G0569 (apisteō) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | to disbelieve |
| Analysis gloss | to disbelieve |
| Occurrence count | 8 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 59 (other) |
| owning_word | to disbelieve |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0569. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0569 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0569. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0569 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0569. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0569 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0569. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0569 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 1 |
| 05 — Moral Character | ROOT_INFERRED | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0570 | apistia | unbelief | — |
| G0571 | apistos | unbelieving | — |
| G3640 | oligopistos | of little faith | — |
| G4100 | pisteuō | to trust (in) | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=8, active=0, delete_flagged=8.

### 3.XREF.G0570 — G0570 (apistia) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | unbelief |
| Analysis gloss | unbelief |
| Occurrence count | 12 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 165 (other) |
| owning_word | unbelief |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 12. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0570. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0570 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 12. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0570. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0570 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 12. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0570. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0570 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 12. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0570. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0570 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| — | UNCLASSIFIED | 2 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0571 | apistos | unbelieving | — |
| G3640 | oligopistos | of little faith | — |
| G4100 | pisteuō | to trust (in) | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=11, active=0, delete_flagged=11.

### 3.XREF.G0571 — G0571 (apistos) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | unbelieving |
| Analysis gloss | unbelieving |
| Occurrence count | 26 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 59 (other) |
| owning_word | unbelieving |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0571. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0571 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0571. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0571 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0571. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0571 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0571. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0571 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 2 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0570 | apistia | unbelief | — |
| G3640 | oligopistos | of little faith | — |
| G4100 | pisteuō | to trust (in) | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=21, active=0, delete_flagged=21.

### 3.XREF.G3640 — G3640 (oligopistos) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | of little faith |
| Analysis gloss | of little faith |
| Occurrence count | 5 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 59 (other) |
| owning_word | faith |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 4 confirmed verse records for G3640. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G3640. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G3640 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 4 confirmed verse records for G3640. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G3640. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G3640 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 4 confirmed verse records for G3640. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G3640. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G3640 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 4 confirmed verse records for G3640. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G3640. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G3640 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 02 — Emotion — Negative | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0570 | apistia | unbelief | — |
| G0571 | apistos | unbelieving | — |
| G3641 | oligos | little/few | — |
| G4100 | pisteuō | to trust (in) | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=4, active=0, delete_flagged=4.

### 3.XREF.G4100 — G4100 (pisteuō) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | to trust (in) |
| Analysis gloss | to trust (in) |
| Occurrence count | 297 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 59 (other) |
| owning_word | faith |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4100. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4100 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4100. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4100 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4100. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4100 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4100. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4100 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 03 — Cognition | KEYWORD_STRONG | 1 |
| 03 — Cognition | KEYWORD_WEAK | 1 |
| 05 — Moral Character | ROOT_INFERRED | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0570 | apistia | unbelief | — |
| G0571 | apistos | unbelieving | — |
| G3640 | oligopistos | of little faith | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=120, active=0, delete_flagged=120.

### 3.XREF.G4101 — G4101 (pistikos) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | pure |
| Analysis gloss | pure |
| Occurrence count | 2 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 59 (other) |
| owning_word | pure |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G4101. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4101. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4101 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G4101. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4101. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4101 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G4101. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4101. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4101 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G4101. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4101. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4101 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0570 | apistia | unbelief | — |
| G0571 | apistos | unbelieving | — |
| G3640 | oligopistos | of little faith | — |
| G4100 | pisteuō | to trust (in) | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=2, active=0, delete_flagged=2.

### 3.XREF.G4102G — G4102G (pistis) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | faith |
| Analysis gloss | faith |
| Occurrence count | 281 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 59 (other) |
| owning_word | faith |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4102G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4102G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4102G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4102G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4102G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4102G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4102G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4102G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 1 |
| 05 — Moral Character | ROOT_INFERRED | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0570 | apistia | unbelief | — |
| G0571 | apistos | unbelieving | — |
| G3640 | oligopistos | of little faith | — |
| G4100 | pisteuō | to trust (in) | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=97, active=0, delete_flagged=97.

### 3.XREF.G4102H — G4102H (pistis) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | faith: faithfulness |
| Analysis gloss | faith: faithfulness |
| Occurrence count | 3 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 59 (other) |
| owning_word | faith: faithfulness |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G4102H. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4102H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4102H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G4102H. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4102H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4102H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G4102H. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4102H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4102H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G4102H. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4102H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4102H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0570 | apistia | unbelief | — |
| G0571 | apistos | unbelieving | — |
| G3640 | oligopistos | of little faith | — |
| G4100 | pisteuō | to trust (in) | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=3, active=0, delete_flagged=3.

### 3.XREF.G4103 — G4103 (pistos) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | faithful |
| Analysis gloss | faithful |
| Occurrence count | 114 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 59 (other) |
| owning_word | faith |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4103. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4103 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4103. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4103 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4103. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4103 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4103. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4103 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 3 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0570 | apistia | unbelief | — |
| G0571 | apistos | unbelieving | — |
| G3640 | oligopistos | of little faith | — |
| G4100 | pisteuō | to trust (in) | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4104 | pistoō | be convinced | — |

**Verse record counts:** total=62, active=0, delete_flagged=62.

### 3.XREF.G4104 — G4104 (pistoō) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | be convinced |
| Analysis gloss | be convinced |
| Occurrence count | 12 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 59 (other) |
| owning_word | be convinced |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G4104. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4104. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4104 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G4104. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4104. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4104 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G4104. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4104. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4104 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G4104. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G4104. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G4104 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | ROOT_INFERRED | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0569 | apisteō | to disbelieve | — |
| G0570 | apistia | unbelief | — |
| G0571 | apistos | unbelieving | — |
| G3640 | oligopistos | of little faith | — |
| G4100 | pisteuō | to trust (in) | — |
| G4101 | pistikos | pure | — |
| G4102G | pistis | faith | — |
| G4102H | pistis | faith: faithfulness | — |
| G4103 | pistos | faithful | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H0525 — H0525 (a.mon) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | artisan |
| Analysis gloss | artisan |
| Occurrence count | 2 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 44 (other) |
| owning_word | artisan |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0525. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0525. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0525 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0525. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0525. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0525 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0525. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0525. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0525 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0525. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0525. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0525 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0525. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0525. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0525 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=2, active=0, delete_flagged=2.

### 3.XREF.H0529 — H0529 (e.mun) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | faithful |
| Analysis gloss | faithful |
| Occurrence count | 8 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 59 (other) |
| owning_word | faith |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0529. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0529. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0529. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0529. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 8. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0529. STEP returned no word analysis block for this term. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 04 — Volition | KEYWORD_WEAK | 1 |
| 05 — Moral Character | KEYWORD_STRONG | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=8, active=0, delete_flagged=8.

### 3.XREF.H0530 — H0530 (e.mu.nah) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | faithfulness |
| Analysis gloss | faithfulness |
| Occurrence count | 49 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 59 (other) |
| owning_word | faith |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0530. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0530 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0530. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0530 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0530. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0530 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0530. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0530 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0530. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0530 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 2 |
| 05 — Moral Character | KEYWORD_STRONG | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=49, active=0, delete_flagged=49.

### 3.XREF.H0539 — H0539 (a.man) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | be faithful |
| Analysis gloss | be faithful |
| Occurrence count | 106 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 44 (other) |
| owning_word | despair |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0539. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0539. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0539. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0539. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0539. STEP returned no word analysis block for this term. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 10 — Dependence / Creatureliness | KEYWORD_WEAK | 2 |
| 05 — Moral Character | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0540 | a.man | to trust | — |
| H0541 | a.man | to turn right | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=100, active=0, delete_flagged=100.

### 3.XREF.H0540 — H0540 (a.man) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | to trust |
| Analysis gloss | to trust |
| Occurrence count | 3 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 44 (other) |
| owning_word | to trust |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for H0540. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0540. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for H0540. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0540. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for H0540. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0540. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for H0540. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0540. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for H0540. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0540. STEP returned no word analysis block for this term. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=3, active=0, delete_flagged=3.

### 3.XREF.H0542 — H0542 (am.man) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | artisan |
| Analysis gloss | artisan |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 44 (other) |
| owning_word | artisan |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0542. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0542. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0542 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0542. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0542. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0542 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0542. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0542. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0542 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0542. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0542. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0542 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0542. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0542. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0542 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H0543 — H0543 (a.men) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | amen |
| Analysis gloss | amen |
| Occurrence count | 30 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 44 (other) |
| owning_word | amen |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0543. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0543 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0543. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0543 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0543. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0543 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0543. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0543 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0543. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0543 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| — | UNCLASSIFIED | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=24, active=0, delete_flagged=24.

### 3.XREF.H0544 — H0544 (o.men) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | faithfulness |
| Analysis gloss | faithfulness |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 44 (other) |
| owning_word | faithfulness |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0544. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0544. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0544 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0544. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0544. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0544 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0544. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0544. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0544 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0544. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0544. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0544 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0544. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0544. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0544 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 11 — Divine-Human Correspondence | KEYWORD_STRONG | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H0545 — H0545 (om.nah) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | brought up |
| Analysis gloss | brought up |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 44 (other) |
| owning_word | brought up |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0545. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0545. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0545 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0545. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0545. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0545 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0545. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0545. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0545 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0545. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0545. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0545 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0545. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0545. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0545 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H0546 — H0546 (om.nah) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | truly |
| Analysis gloss | truly |
| Occurrence count | 2 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 44 (other) |
| owning_word | truly |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0546. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0546. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0546 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0546. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0546. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0546 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0546. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0546. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0546 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0546. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0546. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0546 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0546. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0546. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0546 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=2, active=0, delete_flagged=2.

### 3.XREF.H0547 — H0547 (o.me.nah) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | pillar |
| Analysis gloss | pillar |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 44 (other) |
| owning_word | pillar |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0547. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0547. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0547. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0547. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0547. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0547. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0547. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0547. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H0547. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0547. STEP returned no word analysis block for this term. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H0548 — H0548 (a.ma.nah) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | sure |
| Analysis gloss | sure |
| Occurrence count | 2 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 34 (other) |
| owning_word | covenant |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0548. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0548. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0548. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0548. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0548. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0548. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0548. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0548. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0548. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0548. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H0548. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0548. STEP returned no word analysis block for this term. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 04 — Volition | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=2, active=0, delete_flagged=2.

### 3.XREF.H0551 — H0551 (om.nam) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | truly |
| Analysis gloss | truly |
| Occurrence count | 9 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 191 (other) |
| owning_word | doubt |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 9. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0551. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0551 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 9. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0551. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0551 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 9. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0551. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0551 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 9. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0551. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0551 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 9. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0551. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0551 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=9, active=0, delete_flagged=9.

### 3.XREF.H0552 — H0552 (um.nam) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | truly |
| Analysis gloss | truly |
| Occurrence count | 5 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 44 (other) |
| owning_word | truly |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0552. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0552 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0552. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0552 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0552. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0552 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0552. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0552 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0552. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0552 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 06 — Relational Disposition | KEYWORD_STRONG | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=5, active=0, delete_flagged=5.

### 3.XREF.H0571G — H0571G (e.met) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | truth: faithful |
| Analysis gloss | truth: faithful |
| Occurrence count | 66 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 59 (other) |
| owning_word | faith |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 3 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571H | e.met | truth: true | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=66, active=0, delete_flagged=66.

### 3.XREF.H0571H — H0571H (e.met) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | truth: true |
| Analysis gloss | truth: true |
| Occurrence count | 50 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 44 (other) |
| owning_word | truth: true |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 03 — Cognition | KEYWORD_WEAK | 1 |
| 05 — Moral Character | KEYWORD_STRONG | 1 |
| 10 — Dependence / Creatureliness | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571I | e.met | truth: certain | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=48, active=0, delete_flagged=48.

### 3.XREF.H0571I — H0571I (e.met) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | truth: certain |
| Analysis gloss | truth: certain |
| Occurrence count | 11 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 44 (other) |
| owning_word | truth: certain |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 11. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571I. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 11. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571I. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 11. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571I. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 11. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571I. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 11. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0571I. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0571I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 10 — Dependence / Creatureliness | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0071 | a.va.nah | Abana | — |
| H0525 | a.mon | artisan | — |
| H0526G | a.mon | Amon | — |
| H0526H | a.mon | Amon | — |
| H0526I | a.mon | Amon | — |
| H0529 | e.mun | faithful | — |
| H0530 | e.mu.nah | faithfulness | — |
| H0539 | a.man | be faithful | — |
| H0540 | a.man | to trust | — |
| H0542 | am.man | artisan | — |
| H0543 | a.men | amen | — |
| H0544 | o.men | faithfulness | — |
| H0545 | om.nah | brought up | — |
| H0546 | om.nah | truly | — |
| H0547 | o.me.nah | pillar | — |
| H0548 | a.ma.nah | sure | — |
| H0549G | a.ma.nah | Amana | — |
| H0549H | a.ma.nah | Amana | — |
| H0550G | am.non | Amnon | — |
| H0550H | am.non | Amnon | — |
| H0551 | om.nam | truly | — |
| H0552 | um.nam | truly | — |
| H0571G | e.met | truth: faithful | — |
| H0571H | e.met | truth: true | — |
| H0573 | a.mit.tay | Amittai | — |
| H1968G | he.man | Heman | — |
| H1968H | he.man | Heman | — |
| H1968I | he.man | Heman | — |
| H4104 | me.hu.man | Mehuman | — |

**Verse record counts:** total=11, active=0, delete_flagged=11.

### 3.XREF.H2617A — H2617A (che.sed) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | kindness |
| Analysis gloss | kindness |
| Occurrence count | 261 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 103 (other) |
| owning_word | love |
| owning_part | Part1 |

**MTI flags:**
- `VERSE_EVIDENCE_MINIMAL` — Minimal biblical evidence for this term in the extraction. Does NOT mean the term is irrelevant — triggers research inve

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H2617A. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H2617A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H2617A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 2 |
| 06 — Relational Disposition | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H2616A | cha.sad | be kind | — |
| H2616B | cha.sad | to shame | — |
| H2617B | che.sed | shame | — |
| H2618 | che.sed | Hesed | — |
| H2619 | cha.sad.yah | Hasadiah | — |
| H2623 | cha.sid | pious | — |
| H2624 | cha.si.dah | stork | — |

**Verse record counts:** total=49, active=0, delete_flagged=49.

<!-- PROSE_SECTION
type: sa_s1_d3
registry: 60
version: 1
status: approved
author: claude_code
-->

## Section 4 — Verses by Group (with Dimensions and Annotations)

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:52:55Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `verse_context_group`, `wa_dimension_index`, `wa_verse_records`, `verse_context`, `mti_terms` |
| Notes | Active groups: 7. Verses within each group rendered as anchor → related → set-aside. |

### 4.H5414G.872-001 — H5414G · group `872-001`

| Field | Value |
|---|---|
| context_description | Term names divine giving as the expression of covenant faithfulness — God's giving of land, promise, and blessing as the embodiment of his inner covenantal commitment |
| dimension | 05 — Moral Character |
| dimension_confidence | KEYWORD_WEAK |
| dominant_subject | — |
| manual_override | 0 |
| anchor / related / set-aside | 2 / 35 / 122 |

| Role | Reference | Translation | Span match | Text |
|---|---|---|---|---|
| **anchor** | Gen 12:7 | ESV | 1 | Gen 12:7 Then the Lord appeared to Abram and said , “ To your offspring I will give this land .” So he built there an altar to the Lord , who had appeared to him . |
| **anchor** | Gen 15:18 | ESV | 1 | Gen 15:18 On that day the Lord made a covenant with Abram , saying , “ To your offspring I give this land , from the river of Egypt to the great river , the river Euphrates , |
| related | Gen 13:15 | ESV | 1 | Gen 13:15 for all the land that you see I will give to you and to your offspring forever . |
| related | Gen 13:17 | ESV | 1 | Gen 13:17 Arise , walk through the length and the breadth of the land , for I will give it to you .” |
| related | Gen 15:7 | ESV | 1 | Gen 15:7 And he said to him, “ I am the Lord who brought you out from Ur of the Chaldeans to give you this land to possess .” |
| related | Gen 17:16 | ESV | 1 | Gen 17:16 I will bless her , and moreover , I will give you a son by her. I will bless her, and she shall become nations ; kings of peoples shall come from her .” |
| related | Gen 17:8 | ESV | 1 | Gen 17:8 And I will give to you and to your offspring after you the land of your sojournings , all the land of Canaan , for an everlasting possession , and I will be their God .” |
| related | Gen 24:35 | ESV | 1 | Gen 24:35 The Lord has greatly blessed my master , and he has become great . He has given him flocks and herds , silver and gold , male servants and female servants , camels and donkeys . |
| related | Gen 24:36 | ESV | 1 | Gen 24:36 And Sarah my master’s wife bore a son to my master when she was old , and to him he has given all that he has. |
| related | Gen 24:7 | ESV | 1 | Gen 24:7 The Lord , the God of heaven , who took me from my father’s house and from the land of my kindred , and who spoke to me and swore to me, ‘ To your offspring I will give this land ,’ he will send his angel before you , and you shall take a wife for my son from there . |
| related | Gen 26:3 | ESV | 1 | Gen 26:3 Sojourn in this land , and I will be with you and will bless you, for to you and to your offspring I will give all these lands , and I will establish the oath that I swore to Abraham your father . |
| related | Gen 26:4 | ESV | 1 | Gen 26:4 I will multiply your offspring as the stars of heaven and will give to your offspring all these lands . And in your offspring all the nations of the earth shall be blessed , |
| related | Gen 28:13 | ESV | 1 | Gen 28:13 And behold , the Lord stood above it and said , “ I am the Lord , the God of Abraham your father and the God of Isaac . The land on which you lie I will give to you and to your offspring . |
| related | Jer 11:5 | ESV | 1 | Jer 11:5 that I may confirm the oath that I swore to your fathers , to give them a land flowing with milk and honey , as at this day .” Then I answered , “So be it , Lord .” |
| related | Jer 16:15 | ESV | 1 | Jer 16:15 but ‘As the Lord lives who brought up the people of Israel out of the north country and out of all the countries where he had driven them.’ For I will bring them back to their own land that I gave to their fathers . |
| related | Jer 17:4 | ESV | 1 | Jer 17:4 You shall loosen your hand from your heritage that I gave to you, and I will make you serve your enemies in a land that you do not know , for in my anger a fire is kindled that shall burn forever .” |
| related | Jer 7:14 | ESV | 1 | Jer 7:14 therefore I will do to the house that is called by my name , and in which you trust , and to the place that I gave to you and to your fathers , as I did to Shiloh . |
| related | Jer 7:7 | ESV | 1 | Jer 7:7 then I will let you dwell in this place , in the land that I gave of old to your fathers forever . |
| related | Mal 2:5 | ESV | 1 | Mal 2:5 My covenant with him was one of life and peace , and I gave them to him. It was a covenant of fear , and he feared me. He stood in awe of my name . |
| related | Neh 9:13 | ESV | 1 | Neh 9:13 You came down on Mount Sinai and spoke with them from heaven and gave them right rules and true laws , good statutes and commandments , |
| related | Neh 9:15 | ESV | 1 | Neh 9:15 You gave them bread from heaven for their hunger and brought water for them out of the rock for their thirst , and you told them to go in to possess the land that you had sworn to give them . |
| related | Neh 9:22 | ESV | 1 | Neh 9:22 “And you gave them kingdoms and peoples and allotted to them every corner . So they took possession of the land of Sihon king of Heshbon and the land of Og king of Bashan . |
| related | Neh 9:24 | ESV | 1 | Neh 9:24 So the descendants went in and possessed the land , and you subdued before them the inhabitants of the land , the Canaanites , and gave them into their hand , with their kings and the peoples of the land , that they might do with them as they would . |
| related | Neh 9:35 | ESV | 1 | Neh 9:35 Even in their own kingdom , and amid your great goodness that you gave them, and in the large and rich land that you set before them, they did not serve you or turn from their wicked works . |
| related | Neh 9:36 | ESV | 1 | Neh 9:36 Behold , we are slaves this day ; in the land that you gave to our fathers to enjoy its fruit and its good gifts , behold , we are slaves . |
| related | Neh 9:8 | ESV | 1 | Neh 9:8 You found his heart faithful before you, and made with him the covenant to give to his offspring the land of the Canaanite , the Hittite , the Amorite , the Perizzite , the Jebusite , and the Girgashite . And you have kept your promise , for you are righteous . |
| related | Num 10:29 | ESV | 1 | Num 10:29 And Moses said to Hobab the son of Reuel the Midianite , Moses ’ father-in-law , “We are setting out for the place of which the Lord said , ‘I will give it to you.’ Come with us, and we will do good to you, for the Lord has promised good to Israel .” |
| related | Num 13:2 | ESV | 1 | Num 13:2 “ Send men to spy out the land of Canaan , which I am giving to the people of Israel . From each tribe of their fathers you shall send a man , every one a chief among them .” |
| related | Num 15:2 | ESV | 1 | Num 15:2 “ Speak to the people of Israel and say to them, When you come into the land you are to inhabit , which I am giving you , |
| related | Num 20:12 | ESV | 1 | Num 20:12 And the Lord said to Moses and Aaron , “ Because you did not believe in me, to uphold me as holy in the eyes of the people of Israel , therefore you shall not bring this assembly into the land that I have given them .” |
| related | Num 20:24 | ESV | 1 | Num 20:24 “Let Aaron be gathered to his people , for he shall not enter the land that I have given to the people of Israel , because you rebelled against my command at the waters of Meribah . |
| related | Num 21:3 | ESV | 1 | Num 21:3 And the Lord heeded the voice of Israel and gave over the Canaanites , and they devoted them and their cities to destruction. So the name of the place was called Hormah . |
| related | Num 21:34 | ESV | 1 | Num 21:34 But the Lord said to Moses , “Do not fear him, for I have given him into your hand , and all his people , and his land . And you shall do to him as you did to Sihon king of the Amorites , who lived at Heshbon .” |
| related | Num 25:12 | ESV | 1 | Num 25:12 Therefore say , ‘ Behold , I give to him my covenant of peace , |
| related | Num 27:12 | ESV | 1 | Num 27:12 The Lord said to Moses , “ Go up into this mountain of Abarim and see the land that I have given to the people of Israel . |
| related | Num 32:7 | ESV | 1 | Num 32:7 Why will you discourage the heart of the people of Israel from going over into the land that the Lord has given them? |
| related | Num 32:9 | ESV | 1 | Num 32:9 For when they went up to the Valley of Eshcol and saw the land , they discouraged the heart of the people of Israel from going into the land that the Lord had given them. |

### 4.H5414G.872-002 — H5414G · group `872-002`

| Field | Value |
|---|---|
| context_description | Term names divine giving as the expression of inner love and compassion — God gives in direct response to inner need, longing, prayer, or suffering |
| dimension | 04 — Volition |
| dimension_confidence | KEYWORD_WEAK |
| dominant_subject | — |
| manual_override | 0 |
| anchor / related / set-aside | 2 / 28 / 122 |

| Role | Reference | Translation | Span match | Text |
|---|---|---|---|---|
| **anchor** | Gen 29:33 | ESV | 1 | Gen 29:33 She conceived again and bore a son , and said , “ Because the Lord has heard that I am hated , he has given me this son also .” And she called his name Simeon . |
| **anchor** | Hos 11:8 | ESV | 1 | Hos 11:8 How can I give you up, O Ephraim ? How can I hand you over, O Israel ? How can I make you like Admah ? How can I treat you like Zeboiim ? My heart recoils within me; my compassion grows warm and tender . |
| related | Gen 15:2 | ESV | 1 | Gen 15:2 But Abram said , “O Lord God , what will you give me , for I continue childless , and the heir of my house is Eliezer of Damascus ?” |
| related | Gen 15:3 | ESV | 1 | Gen 15:3 And Abram said , “ Behold , you have given me no offspring , and a member of my household will be my heir .” |
| related | Gen 16:5 | ESV | 1 | Gen 16:5 And Sarai said to Abram , “May the wrong done to me be on you! I gave my servant to your embrace , and when she saw that she had conceived , she looked on me with contempt . May the Lord judge between you and me !” |
| related | Gen 20:16 | ESV | 1 | Gen 20:16 To Sarah he said , “Behold, I have given your brother a thousand pieces of silver . It is a sign of your innocence in the eyes of all who are with you , and before everyone you are vindicated .” |
| related | Gen 28:4 | ESV | 1 | Gen 28:4 May he give the blessing of Abraham to you and to your offspring with you, that you may take possession of the land of your sojournings that God gave to Abraham !” |
| related | Gen 30:18 | ESV | 1 | Gen 30:18 Leah said , “ God has given me my wages because I gave my servant to my husband .” So she called his name Issachar . |
| related | Gen 30:6 | ESV | 1 | Gen 30:6 Then Rachel said , “ God has judged me, and has also heard my voice and given me a son .” Therefore she called his name Dan . |
| related | Gen 31:9 | ESV | 1 | Gen 31:9 Thus God has taken away the livestock of your father and given them to me . |
| related | Hag 2:9 | ESV | 1 | Hag 2:9 The latter glory of this house shall be greater than the former , says the Lord of hosts . And in this place I will give peace , declares the Lord of hosts .’” |
| related | Hos 2:8 | ESV | 1 | Hos 2:8 And she did not know that it was I who gave her the grain , the wine , and the oil , and who lavished on her silver and gold , which they used for Baal . |
| related | Isa 40:29 | ESV | 1 | Isa 40:29 He gives power to the faint , and to him who has no might he increases strength . |
| related | Isa 41:27 | ESV | 1 | Isa 41:27 I was the first to say to Zion , “ Behold , here they are !” and I give to Jerusalem a herald of good news . |
| related | Isa 43:20 | ESV | 1 | Isa 43:20 The wild beasts will honor me, the jackals and the ostriches , for I give water in the wilderness , rivers in the desert , to give drink to my chosen people , |
| related | Isa 43:3 | ESV | 1 | Isa 43:3 For I am the Lord your God , the Holy One of Israel , your Savior . I give Egypt as your ransom , Cush and Seba in exchange for you . |
| related | Isa 43:4 | ESV | 1 | Isa 43:4 Because you are precious in my eyes , and honored , and I love you, I give men in return for you , peoples in exchange for your life . |
| related | Isa 45:3 | ESV | 1 | Isa 45:3 I will give you the treasures of darkness and the hoards in secret places , that you may know that it is I , the Lord , the God of Israel , who call you by your name . |
| related | Isa 7:14 | ESV | 1 | Isa 7:14 Therefore the Lord himself will give you a sign . Behold , the virgin shall conceive and bear a son , and shall call his name Immanuel . |
| related | Jer 14:22 | ESV | 1 | Jer 14:22 Are there any among the false gods of the nations that can bring rain ? Or can the heavens give showers ? Are you not he , O Lord our God ? We set our hope on you, for you do all these things . |
| related | Jer 3:15 | ESV | 1 | Jer 3:15 “‘And I will give you shepherds after my own heart , who will feed you with knowledge and understanding . |
| related | Jer 3:19 | ESV | 1 | Jer 3:19 “‘ I said , How I would set you among my sons , and give you a pleasant land , a heritage most beautiful of all nations . And I thought you would call me, My Father , and would not turn from following me . |
| related | Jer 5:24 | ESV | 1 | Jer 5:24 They do not say in their hearts , ‘Let us fear the Lord our God , who gives the rain in its season , the autumn rain and the spring rain , and keeps for us the weeks appointed for the harvest .’ |
| related | Job 24:23 | ESV | 1 | Job 24:23 He gives them security , and they are supported , and his eyes are upon their ways . |
| related | Job 36:6 | ESV | 1 | Job 36:6 He does not keep the wicked alive , but gives the afflicted their right . |
| related | Neh 1:11 | ESV | 1 | Neh 1:11 O Lord , let your ear be attentive to the prayer of your servant , and to the prayer of your servants who delight to fear your name , and give success to your servant today , and grant him mercy in the sight of this man .” Now I was cupbearer to the king . |
| related | Neh 2:8 | ESV | 1 | Neh 2:8 and a letter to Asaph , the keeper of the king’s forest , that he may give me timber to make beams for the gates of the fortress of the temple , and for the wall of the city , and for the house that I shall occupy .” And the king granted me what I asked, for the good hand of my God was upon me . |
| related | Neh 9:27 | ESV | 1 | Neh 9:27 Therefore you gave them into the hand of their enemies , who made them suffer . And in the time of their suffering they cried out to you and you heard them from heaven , and according to your great mercies you gave them saviors who saved them from the hand of their enemies . |
| related | Num 14:8 | ESV | 1 | Num 14:8 If the Lord delights in us, he will bring us into this land and give it to us, a land that flows with milk and honey . |
| related | Num 21:16 | ESV | 1 | Num 21:16 And from there they continued to Beer ; that is the well of which the Lord said to Moses , “ Gather the people together, so that I may give them water .” |

### 4.H5414G.872-003 — H5414G · group `872-003`

| Field | Value |
|---|---|
| context_description | Term names the giving of inner-being capacities — wisdom, spirit, understanding, songs, and strength given directly to the inner life |
| dimension | 03 — Cognition |
| dimension_confidence | KEYWORD_WEAK |
| dominant_subject | — |
| manual_override | 0 |
| anchor / related / set-aside | 2 / 4 / 122 |

| Role | Reference | Translation | Span match | Text |
|---|---|---|---|---|
| **anchor** | Job 38:36 | ESV | 1 | Job 38:36 Who has put wisdom in the inward parts or given understanding to the mind ? |
| **anchor** | Neh 9:20 | ESV | 1 | Neh 9:20 You gave your good Spirit to instruct them and did not withhold your manna from their mouth and gave them water for their thirst . |
| related | Isa 42:5 | ESV | 1 | Isa 42:5 Thus says God , the Lord , who created the heavens and stretched them out , who spread out the earth and what comes from it , who gives breath to the people on it and spirit to those who walk in it : |
| related | Isa 50:4 | ESV | 1 | Isa 50:4 The Lord God has given me the tongue of those who are taught , that I may know how to sustain with a word him who is weary . Morning by morning he awakens ; he awakens my ear to hear as those who are taught . |
| related | Job 3:20 | ESV | 1 | Job 3:20 “ Why is light given to him who is in misery , and life to the bitter in soul , |
| related | Job 35:10 | ESV | 1 | Job 35:10 But none says , ‘ Where is God my Maker , who gives songs in the night , |

### 4.H5414G.872-004 — H5414G · group `872-004`

| Field | Value |
|---|---|
| context_description | Term names divine giving as moral judgement — God gives into the hand of enemies or destruction as the moral expression of his inner response to faithlessness |
| dimension | 05 — Moral Character |
| dimension_confidence | KEYWORD_WEAK |
| dominant_subject | — |
| manual_override | 0 |
| anchor / related / set-aside | 2 / 9 / 122 |

| Role | Reference | Translation | Span match | Text |
|---|---|---|---|---|
| **anchor** | Hos 13:11 | ESV | 1 | Hos 13:11 I gave you a king in my anger , and I took him away in my wrath . |
| **anchor** | Jer 12:7 | ESV | 1 | Jer 12:7 “I have forsaken my house ; I have abandoned my heritage ; I have given the beloved of my soul into the hands of her enemies . |
| related | Hos 9:14 | ESV | 1 | Hos 9:14 Give them, O Lord — what will you give ? Give them a miscarrying womb and dry breasts . |
| related | Isa 42:24 | ESV | 1 | Isa 42:24 Who gave up Jacob to the looter , and Israel to the plunderers ? Was it not the Lord , against whom we have sinned , in whose ways they would not walk , and whose law they would not obey ? |
| related | Isa 43:28 | ESV | 1 | Isa 43:28 Therefore I will profane the princes of the sanctuary , and deliver Jacob to utter destruction and Israel to reviling . |
| related | Isa 47:6 | ESV | 1 | Isa 47:6 I was angry with my people ; I profaned my heritage ; I gave them into your hand ; you showed them no mercy ; on the aged you made your yoke exceedingly heavy . |
| related | Jer 16:13 | ESV | 1 | Jer 16:13 Therefore I will hurl you out of this land into a land that neither you nor your fathers have known , and there you shall serve other gods day and night , for I will show you no favor .’ |
| related | Jer 17:10 | ESV | 1 | Jer 17:10 “ I the Lord search the heart and test the mind , to give every man according to his ways , according to the fruit of his deeds .” |
| related | Jer 8:13 | ESV | 1 | Jer 8:13 When I would gather them, declares the Lord , there are no grapes on the vine , nor figs on the fig tree ; even the leaves are withered , and what I gave them has passed away from them .” |
| related | Neh 4:4 | ESV | 1 | Neh 4:4 Hear , O our God , for we are despised . Turn back their taunt on their own heads and give them up to be plundered in a land where they are captives . |
| related | Neh 9:30 | ESV | 1 | Neh 9:30 Many years you bore with them and warned them by your Spirit through your prophets . Yet they would not give ear . Therefore you gave them into the hand of the peoples of the lands . |

### 4.H5414G.872-005 — H5414G · group `872-005`

| Field | Value |
|---|---|
| context_description | Term names the inner act of human giving — self-giving, sacrificial giving, votive giving, or giving as the expression of inner orientation toward God or community |
| dimension | 06 — Relational Disposition |
| dimension_confidence | KEYWORD_STRONG |
| dominant_subject | — |
| manual_override | 0 |
| anchor / related / set-aside | 2 / 17 / 122 |

| Role | Reference | Translation | Span match | Text |
|---|---|---|---|---|
| **anchor** | Isa 50:6 | ESV | 1 | Isa 50:6 I gave my back to those who strike , and my cheeks to those who pull out the beard ; I hid not my face from disgrace and spitting . |
| **anchor** | Job 1:21 | ESV | 1 | Job 1:21 And he said , “ Naked I came from my mother’s womb , and naked shall I return . The Lord gave , and the Lord has taken away ; blessed be the name of the Lord .” |
| related | Gen 25:34 | ESV | 1 | Gen 25:34 Then Jacob gave Esau bread and lentil stew , and he ate and drank and rose and went his way . Thus Esau despised his birthright . |
| related | Gen 25:5 | ESV | 1 | Gen 25:5 Abraham gave all he had to Isaac . |
| related | Gen 27:28 | ESV | 1 | Gen 27:28 May God give you of the dew of heaven and of the fatness of the earth and plenty of grain and wine . |
| related | Gen 28:20 | ESV | 1 | Gen 28:20 Then Jacob made a vow , saying , “ If God will be with me and will keep me in this way that I go , and will give me bread to eat and clothing to wear , |
| related | Gen 28:22 | ESV | 1 | Gen 28:22 and this stone , which I have set up for a pillar , shall be God’s house . And of all that you give me I will give a full tenth to you .” |
| related | Gen 3:12 | ESV | 1 | Gen 3:12 The man said , “The woman whom you gave to be with me, she gave me fruit of the tree , and I ate .” |
| related | Job 2:4 | ESV | 1 | Job 2:4 Then Satan answered the Lord and said , “ Skin for skin ! All that a man has he will give for his life . |
| related | Job 6:8 | ESV | 1 | Job 6:8 “ Oh that I might have my request , and that God would fulfill my hope , |
| related | Mal 2:2 | ESV | 1 | Mal 2:2 If you will not listen , if you will not take it to heart to give honor to my name , says the Lord of hosts , then I will send the curse upon you and I will curse your blessings . Indeed , I have already cursed them, because you do not lay it to heart . |
| related | Mic 6:7 | ESV | 1 | Mic 6:7 Will the Lord be pleased with thousands of rams , with ten thousands of rivers of oil ? Shall I give my firstborn for my transgression , the fruit of my body for the sin of my soul ?” |
| related | Neh 7:70 | ESV | 1 | Neh 7:70 Now some of the heads of fathers’ houses gave to the work . The governor gave to the treasury 1,000 darics of gold , 50 basins , 30 priests ’ garments and 500 minas of silver. |
| related | Neh 7:71 | ESV | 1 | Neh 7:71 And some of the heads of fathers’ houses gave into the treasury of the work 20,000 darics of gold and 2,200 minas of silver . |
| related | Neh 7:72 | ESV | 1 | Neh 7:72 And what the rest of the people gave was 20,000 darics of gold , 2,000 minas of silver , and 67 priests ’ garments . |
| related | Num 21:2 | ESV | 1 | Num 21:2 And Israel vowed a vow to the Lord and said , “ If you will indeed give this people into my hand , then I will devote their cities to destruction.” |
| related | Num 22:18 | ESV | 1 | Num 22:18 But Balaam answered and said to the servants of Balak , “ Though Balak were to give me his house full of silver and gold , I could not go beyond the command of the Lord my God to do less or more . |
| related | Num 24:13 | ESV | 1 | Num 24:13 ‘ If Balak should give me his house full of silver and gold , I would not be able to go beyond the word of the Lord , to do either good or bad of my own will . What the Lord speaks , that will I speak ’? |
| related | Num 5:7 | ESV | 1 | Num 5:7 he shall confess his sin that he has committed . And he shall make full restitution for his wrong , adding a fifth to it and giving it to him to whom he did the wrong . |

### 4.H5414G.872-006 — H5414G · group `872-006`

| Field | Value |
|---|---|
| context_description | Term names the giving or withholding of glory and honour — the inner-being act of ascribing worth to God, or divine withholding of glory from others |
| dimension | 11 — Divine-Human Correspondence |
| dimension_confidence | KEYWORD_WEAK |
| dominant_subject | — |
| manual_override | 0 |
| anchor / related / set-aside | 2 / 4 / 122 |

| Role | Reference | Translation | Span match | Text |
|---|---|---|---|---|
| **anchor** | Isa 42:8 | ESV | 1 | Isa 42:8 I am the Lord ; that is my name ; my glory I give to no other , nor my praise to carved idols . |
| **anchor** | Jer 13:16 | ESV | 1 | Jer 13:16 Give glory to the Lord your God before he brings darkness , before your feet stumble on the twilight mountains , and while you look for light he turns it into gloom and makes it deep darkness . |
| related | Isa 42:6 | ESV | 1 | Isa 42:6 “ I am the Lord ; I have called you in righteousness ; I will take you by the hand and keep you; I will give you as a covenant for the people , a light for the nations , |
| related | Isa 48:11 | ESV | 1 | Isa 48:11 For my own sake , for my own sake , I do it, for how should my name be profaned ? My glory I will not give to another . |
| related | Isa 56:5 | ESV | 1 | Isa 56:5 I will give in my house and within my walls a monument and a name better than sons and daughters ; I will give them an everlasting name that shall not be cut off . |
| related | Isa 8:18 | ESV | 1 | Isa 8:18 Behold , I and the children whom the Lord has given me are signs and portents in Israel from the Lord of hosts , who dwells on Mount Zion . |

### 4.H5414G.872-007 — H5414G · group `872-007`

| Field | Value |
|---|---|
| context_description | Term names eschatological or restorative giving — God gives to transform inner conditions: ashes to beauty, mourning to gladness, faint spirit to praise |
| dimension | 01 — Emotion — Positive |
| dimension_confidence | KEYWORD_WEAK |
| dominant_subject | — |
| manual_override | 0 |
| anchor / related / set-aside | 2 / 9 / 122 |

| Role | Reference | Translation | Span match | Text |
|---|---|---|---|---|
| **anchor** | Hos 2:15 | ESV | 1 | Hos 2:15 And there I will give her her vineyards and make the Valley of Achor a door of hope . And there she shall answer as in the days of her youth , as at the time when she came out of the land of Egypt . |
| **anchor** | Isa 61:3 | ESV | 1 | Isa 61:3 to grant to those who mourn in Zion — to give them a beautiful headdress instead of ashes , the oil of gladness instead of mourning , the garment of praise instead of a faint spirit ; that they may be called oaks of righteousness , the planting of the Lord , that he may be glorified . |
| related | Hos 2:5 | ESV | 1 | Hos 2:5 For their mother has played the whore ; she who conceived them has acted shamefully . For she said , ‘I will go after my lovers , who give me my bread and my water , my wool and my flax , my oil and my drink .’ |
| related | Isa 30:20 | ESV | 1 | Isa 30:20 And though the Lord give you the bread of adversity and the water of affliction , yet your Teacher will not hide himself anymore , but your eyes shall see your Teacher . |
| related | Isa 35:2 | ESV | 1 | Isa 35:2 it shall blossom abundantly and rejoice with joy and singing . The glory of Lebanon shall be given to it, the majesty of Carmel and Sharon . They shall see the glory of the Lord , the majesty of our God . |
| related | Isa 49:8 | ESV | 1 | Isa 49:8 Thus says the Lord : “ In a time of favor I have answered you; in a day of salvation I have helped you; I will keep you and give you as a covenant to the people , to establish the land , to apportion the desolate heritages , |
| related | Isa 61:8 | ESV | 1 | Isa 61:8 For I the Lord love justice ; I hate robbery and wrong ; I will faithfully give them their recompense , and I will make an everlasting covenant with them . |
| related | Num 18:6 | ESV | 1 | Num 18:6 And behold , I have taken your brothers the Levites from among the people of Israel . They are a gift to you, given to the Lord , to do the service of the tent of meeting . |
| related | Num 18:7 | ESV | 1 | Num 18:7 And you and your sons with you shall guard your priesthood for all that concerns the altar and that is within the veil ; and you shall serve . I give your priesthood as a gift , and any outsider who comes near shall be put to death .” |
| related | Num 18:8 | ESV | 1 | Num 18:8 Then the Lord spoke to Aaron , “Behold, I have given you charge of the contributions made to me, all the consecrated things of the people of Israel . I have given them to you as a portion and to your sons as a perpetual due . |
| related | Num 8:19 | ESV | 1 | Num 8:19 And I have given the Levites as a gift to Aaron and his sons from among the people of Israel , to do the service for the people of Israel at the tent of meeting and to make atonement for the people of Israel , that there may be no plague among the people of Israel when the people of Israel come near the sanctuary .” |

<!-- PROSE_SECTION
type: sa_s1_d5
registry: 60
version: 1
status: approved
author: claude_code
-->

## Section 5 — Research Pointers, Findings, and Cross-Registry Links

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:52:55Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `wa_session_b_findings`, `wa_finding_catalogue_links`, `wa_obs_question_catalogue`, `wa_session_research_flags`, `wa_term_phase2_flags`, `wa_cross_registry_links`, `wa_crosslink_type` |
| Notes | Four sub-blocks: 5a SB findings + SB pointers · 5b SD pointers · 5c cross-registry links · 5d correlation summary. |

### 5a — Session B Pointers and Findings

**Structured findings:**

| Code | Type | Status | Anchor verses | Finding text |
|---|---|---|---|---|
| `DIM-60-001` | DIMENSION_REVIEW | pending | — | Three groups (872-001, 872-002, 872-007) in the faithfulness registry describe divine action — covenantal giving, compassionate giving, and eschatological transformation. The faithfulness registry ope |

**Phase 2 term advisories:**

| Strongs | Flag | Source | Description |
|---|---|---|---|
| G4102G | `—` | bulk_patch | — |
| H5414G | `THIN_DATA` | bulk_patch | — |
| H5921A | `—` | bulk_patch | — |

### 5b — Session D Pointers (cross-registry synthesis queue)

_No Session D pointers for this registry._

### 5c — Cross-Registry Links

_No cross-registry links recorded for this registry._

### 5d — Correlation signals

_Full programme-wide correlation data is not inlined here — see `scripts/build_correlation_extract.py` output. This section reserved for a brief registry-specific summary once correlations are integrated._

<!-- PROSE_SECTION
type: sa_s1_d6
registry: 60
version: 1
status: approved
author: claude_code
-->

## Section 6 — Analytic Questions (Catalogue + Registry Extensions)

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:52:55Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `wa_obs_question_catalogue` |
| Notes | Universal catalogue questions (scope='universal') + any registry-specific extensions (source_registry_no or source_word match). Grouped by catalogue `section`. |

### 6.1 Universal catalogue (242 questions)

#### Compassion Extensions

| Code | Pattern | Question |
|---|---|---|
| `C-001` | — | Does the evidence for the word include a significant cluster of prohibition contexts — and if so, what does the frequency of the word's prohibition reveal about its default status in the inner being? |
| `C-002` | — | Does any verse depict the word winning an inner contest with a competing disposition — and if so, what does this reveal about the word's relationship to other inner-being characteristics that it must overcome? |
| `C-003` | — | Does the evidence assign the word an explicitly everlasting or permanent temporal character — in direct contrast to the momentary character of a competing or opposing disposition? |
| `C-004` | — | Is the word's abstract meaning etymologically derived from a concrete somatic reality — and if so, what does this unusual etymological direction reveal about the relationship between the inner experience and its bodily ground? |
| `C-005` | — | Does the word have a participatory dimension — does it operate as genuine entry into another's experience rather than response from a safe distance — and if so, does this participation carry an eschatological trajectory? |
| `C-006` | — | Does any verse name the violation of the word by the very person who most characteristically bears it — and if so, what does this reveal about the word's resilience or fragility under external pressure? |
| `C-007` | — | Has the word acquired a standardised or institutionalised social form — a normative outward expression that names what the characteristic looks like when it is embodied in social practice? |
| `C-008` | — | Does the word identify a specific category of person who needs it but cannot perceive their own need — and what conditions produce the failure of need-recognition? |

#### Forgiveness Extensions

| Code | Pattern | Question |
|---|---|---|
| `F-001` | — | Does the word have an outer limit — a condition or state in which it is explicitly withheld or cannot operate — and what does that outer limit reveal about the word's nature? |
| `F-002` | — | Can the structure of the word's action be misused or inverted — can the same act-structure produce a wrong result — and what is the evidence? |
| `F-003` | — | Is there a vertical-horizontal structural interdependence in the word's operation — does reception from God structurally enable extension toward others? |
| `F-004` | — | Is the word's primary grammatical subject restricted — is it used exclusively or primarily with one type of subject (divine, human, or other)? |
| `F-005` | — | What is the mechanism through which the word is administered or conveyed — and what is the relationship between the outward mechanism and the inner reality it produces? |
| `F-006` | — | Does the word operate unconditionally — or does it have stated conditions under which it is granted or withheld? |
| `F-007` | — | Is the word a single act or a compound of distinct component acts — and if compound, what are the components and are they always simultaneous? |
| `F-008` | — | What does the word make possible in a relationship that would otherwise be closed or broken — and what relational cycle does it break? |
| `F-009` | — | Does the word function as a prerequisite or enabling condition for another spiritual act or practice — and if so, which one and why? |
| `F-010` | — | Are the downstream inner-being effects of the word proportional to the degree or magnitude of the word received — does more of the word produce more of the effect? |
| `F-011` | — | Does the word share vocabulary with adjacent characteristics — or does it occupy an isolated lexical space? What does the degree of sharing or isolation suggest about the word's relationship to adjacent characteristics? |
| `F-012` | — | Is the word named in Scripture as a divine possession or attribute — something that belongs to God — distinct from an act God performs? What does that naming imply about access to the word? |
| `F-013` | — | What practices, disciplines, or ongoing inner acts feed or sustain the human capacity to extend the word to others? |
| `F-014` | — | Is the word a terminal inner-being state — one in which the person rests — or a transitional one that characteristically produces movement to a further state? What is the evidence either way? |

#### Goodness Extensions

| Code | Pattern | Question |
|---|---|---|
| `WS-001` | — | Does the comparative wisdom idiom (Group 884-004 — better-than sayings) operate as a distinct mode of goodness, or is it a subset of moral character? |
| `WS-002` | — | What is the analytical relationship between agathōsunē (G0019 — goodness) and chrēstotēs (G5544 — kindness) as co-OWNER terms of this registry? Are they aspects of a single characteristic or genuinely distinct inner-being phenomena sharing a registry? |
| `WS-003` | — | What does the Haman instance (Est 5:9 — tov-lev, glad of heart) reveal about the difference between genuine inner well-being and morally ungrounded inner pleasure? |
| `WS-004` | — | What does the liturgical repetition of "the Lord is good, his steadfast love endures forever" (appearing as a refrain across Psalms 106, 107, 118, 136) reveal about goodness as a confessional and community-forming declaration? |
| `WS-005` | — | Does the NT's coinage of agathōsunē as a new abstract noun signal a shift from tov's broad Hebrew range to a more specialised NT understanding of goodness as Spirit-produced virtue — and does this shift represent development or narrowing? |
| `WS-006` | — | Does the programme's tri-registry distribution of the TOV root family (goodness as quality in R67, doing good in R65, relational pleasantness in R103) produce a coherent analytical triad for Session D, or does it create artificial boundaries that need to be addressed at synthesis? |

#### Love Extensions

| Code | Pattern | Question |
|---|---|---|
| `L-001` | — | Does the word hold a foundational position relative to other inner-being characteristics — does it govern, generate, or organise them? |
| `L-002` | — | Where the word has distinct modes of operation, are those modes held simultaneously or do they operate sequentially? |
| `L-003` | — | Does the word have an inherent directionality — is it always oriented toward an object — and what does the choice of object determine about the word's moral character? |
| `L-004` | — | Can the word function as an identity diagnostic — does what a person does with this word reveal what kind of person they are? |
| `L-005` | — | Does the word operate at a level below conscious attention or deliberate will — and if so, what does this imply about its depth in the inner being? |
| `L-006` | — | Does the vocabulary of the word include a systematic taxonomy of its own misdirected forms — and if so, what structural logic organises that taxonomy? |
| `L-007` | — | Can the word increase or grow in the inner being — and if so, by what means? |
| `L-008` | — | Does the word have a definitional outward expression — a form that constitutes what the word is rather than merely evidencing it? |
| `L-009` | — | Is the word named in Scripture as constitutive of the divine essence — what God is — rather than merely as a divine attribute or act? |
| `L-010` | — | Does the word's structural opposite operate under the same moral logic as the word itself — can the contrary also be either rightly or wrongly directed? |
| `L-011` | — | What is the relationship between the word as an inner disposition and the word as an outward act — are they competitors, co-expressions, or in a different structural relationship? |
| `L-012` | — | Does the word carry an epistemic dimension — is knowing and being known a structural component of the word's operation? |
| `L-013` | — | Does the word function as a publicly legible signal — a means by which something about the inner community or person is read by those outside? |
| `L-014` | — | Does the word produce a reorganisation of social dynamics — and if so, in what direction does it reorganise them? |

#### Mercy Extensions

| Code | Pattern | Question |
|---|---|---|
| `M-001` | — | How does the word distinguish itself from its nearest near-synonym — what is the threshold or constitutive difference between them? |
| `M-002` | — | Does the word require a structural asymmetry between giver and receiver — is the positional difference (greater-to-lesser, strong-to-weak) a precondition of the word's operation, or can it operate between equals? |
| `M-003` | — | At what level of the inner being is the word received, and at what level is it expressed — does the word follow a named pathway through the spirit-soul-body structure? |
| `M-004` | — | Is the absence of the word described as a diminishment of what it means to be human — is the word presented as constitutive of humanness rather than merely as a virtue the human person may or may not possess? |
| `M-005` | — | Does the word produce a pastoral capacity in the one who has received it — a specific capacity to minister to others in the condition in which the person themselves was once ministered to? |
| `M-006` | — | Has the word been given an architectural or material realisation in Israel's worship — a physical structure in which the word is spatially located — and if so, what does that materialisation reveal about the word's character and the nature of access to it? |
| `M-007` | — | Does the word share its structural logic (such as gratuitousness or disproportionality) with an apparently contrary reality — does the same principle that governs the word also appear in something that seems to contradict it? |
| `M-008` | — | Does the word's operation involve the face — as the site of favour, judgment, recognition, or relational access — and what does that face-language reveal about the inner-outer structure of the word? |
| `M-009` | — | What is the causal relationship between the word as an inner disposition and the structural mechanism through which it operates — does the disposition produce the mechanism, or does the mechanism produce the disposition? |
| `M-010` | — | What does a documented directional reversal in a key vocabulary term reveal about the word's theological significance — what claim about the nature of the divine-human relationship is encoded in the reversal? |
| `M-011` | — | Does the word's operation traverse all three levels of the inner being — spirit, soul, and body — and if so, what is the function at each level? |

#### T0 — Divine Image and Created Design

| Code | Pattern | Question |
|---|---|---|
| `T0.1.1` | — | What does the verse evidence reveal about the nature or character of God that this characteristic reflects or images? |
| `T0.1.2` | — | Does Scripture explicitly attribute this characteristic to God — and if so, what does that attribution reveal about its significance in the human person? |
| `T0.1.3` | — | Where Scripture is silent about God's possession of this characteristic, what does that silence suggest about the characteristic's place in the divine image? |
| `T0.2.1` | — | What does the verse evidence suggest about the purpose this characteristic serves in the human person as created — what does it equip the person to be, do, or become? |
| `T0.2.2` | — | Does the evidence indicate whether this characteristic is part of the original created design, a response to the fallen condition, or both? |
| `T0.2.3` | — | Is there evidence that this characteristic is oriented toward a future fullness — something the person is moving toward, not only what they currently are? |
| `T0.3.1` | — | In what way does this characteristic express the divine image in the human person — what aspect of being made in God's likeness does it instantiate? |
| `T0.3.2` | — | Does the evidence suggest that this characteristic is shared between God and the human person, or is it exclusively a creaturely analogue to something in God? |
| `T0.3.3` | — | What does the presence or absence of this characteristic in a person reveal about the condition of the divine image in that person? |
| `T0.4.1` | — | Does Scripture use this characteristic typologically — deploying it to point toward or participate in a reality beyond the immediate (covenantal, eschatological, christological)? |
| `T0.4.2` | — | If typological use is present, what is the direction of the typology — does the human instance point toward the divine, or does the divine instance establish the pattern for the human? |
| `T0.4.3` | — | If no typological use is evidenced, note this explicitly. |

#### T1 — Definition

| Code | Pattern | Question |
|---|---|---|
| `T1.1.1` | — | What is this characteristic called in the programme — and what does the name itself signal about its essential nature? |
| `T1.1.2` | — | What do the primary Hebrew and Greek terms reveal at the definitional level — before deeper lexical analysis begins? |
| `T1.1.3` | — | Does the name carry directional, relational, or constitutional implications that orient the enquiry from the outset? |
| `T1.2.1` | — | What kind of inner-being phenomenon does this characteristic appear to be — an act, a disposition, a condition, a quality, or something else? |
| `T1.2.2` | — | Is this characteristic simple in structure or does it appear to have constituent elements at first encounter? |
| `T1.2.3` | — | What is the current best working description of this characteristic — encapsulating its constitutional location, the faculties it primarily engages, and its impact on the person? |
| `T1.3.1` | — | What is the structural opposite of this characteristic — the inner-being reality that stands against or excludes it? |
| `T1.3.2` | — | What does this characteristic explicitly exclude or resist? |
| `T1.3.3` | — | What is this characteristic not — where does it end and something else begin? |
| `T1.4.1` | — | In what distinct ways does this characteristic operate within the inner person? |
| `T1.4.2` | — | Does this characteristic operate differently depending on context, direction, or constitutional level? |
| `T1.4.3` | — | Does this characteristic have a communicative or speech-based mode of operation — and if so, how does it function? |
| `T1.5.1` | — | What is the first or most immediate inner-being response to receiving or encountering this characteristic? |
| `T1.5.2` | — | Is the immediate response consistent across the verse evidence, or does it vary? |
| `T1.5.3` | — | Where the verse evidence is silent on immediate response, note this explicitly. |
| `T1.6.1` | — | What does this characteristic produce in the inner being over time? |
| `T1.6.2` | — | What states, qualities, capacities, or orientations does sustained exposure to or possession of this characteristic establish? |
| `T1.6.3` | — | Does the sustained effect differ from the immediate response — and if so, how? |
| `T1.7.1` | — | What inner conditions or orientations enable genuine reception of this characteristic? |
| `T1.7.2` | — | What inner conditions block, distort, or prevent reception? |
| `T1.7.3` | — | What is the inner-being state of the person who encounters this characteristic but does not receive it? |
| `T1.8.1` | — | What is the primary inner-being dimension of this characteristic from the programme's dimension vocabulary? |
| `T1.8.2` | — | What evidence from the verse evidence supports this classification? |
| `T1.8.3` | — | Does this characteristic carry secondary dimensions — and if so, what are they, and do they compete with the primary classification? |

#### T2 — Constitutional Location and Boundaries

| Code | Pattern | Question |
|---|---|---|
| `T2.1.1` | — | Is this characteristic explicitly located at the spirit level in the verse evidence? |
| `T2.1.2` | — | Does the evidence indicate that this characteristic originates in or is primarily a spirit-level phenomenon? |
| `T2.1.3` | — | What does spirit-level location reveal about the nature and depth of this characteristic? |
| `T2.1.4` | — | If the evidence is silent on spirit-level location, note this explicitly. |
| `T2.10.1` | — | Does this characteristic move across constitutional levels — from spirit to soul, from soul to body, or across boundaries in other directions? |
| `T2.10.2` | — | What does the evidence reveal about the sequence or pattern of that movement? |
| `T2.10.3` | — | If no constitutional movement is evidenced, note this explicitly. |
| `T2.2.1` | — | Is this characteristic identified in the verse evidence as a soul-level phenomenon? |
| `T2.2.2` | — | What does soul-level location reveal about this characteristic's place in the innermost personal experience? |
| `T2.2.3` | — | If the evidence is silent on soul-level location, note this explicitly. |
| `T2.3.1` | — | Does the verse evidence locate this characteristic in the heart? |
| `T2.3.2` | — | What does the heart-location reveal — what aspect of the heart's integrating function (knowing, willing, feeling, moral awareness) does this characteristic engage? |
| `T2.3.3` | — | If the evidence is silent on heart-location, note this explicitly. |
| `T2.4.1` | — | Does the verse evidence locate this characteristic in the mind? |
| `T2.4.2` | — | What does mind-location reveal — what aspect of the mind's function (thought, discernment, understanding) does this characteristic engage? |
| `T2.4.3` | — | If the evidence is silent on mind-location, note this explicitly. |
| `T2.5.1` | — | Does the verse evidence surface any soul-level location beyond heart and mind for this characteristic? |
| `T2.5.2` | — | If so, what is that location, and what does it reveal? |
| `T2.5.3` | — | If the evidence is silent, note this explicitly. |
| `T2.6.1` | — | Does the verse evidence link this characteristic to a specific body part? |
| `T2.6.2` | — | If so, what is Scripture doing by making that link — is it emphatic, functional, expressive, indicative, or mediating? |
| `T2.6.3` | — | If no body-part link is evidenced, note this explicitly. |
| `T2.7.1` | — | Where a body-characteristic link exists, which direction does it run — does the soul express through the body, does the body feed back to the soul, or does it run in both directions? |
| `T2.7.2` | — | What is the consequence of that directionality for understanding the characteristic? |
| `T2.7.3` | — | If no body-characteristic link is evidenced, note this explicitly. |
| `T2.8.1` | — | Does sustained operation of this characteristic leave a constitutional deposit in the body or its design — including DNA or generational consequence? |
| `T2.8.2` | — | What evidence supports or contradicts this? |
| `T2.8.3` | — | If the evidence is silent, note this explicitly. This finding feeds directly into T5.7. |
| `T2.9.1` | — | Where does this characteristic originate constitutionally — is it generated from within the person, received from outside, bestowed by God, or carried generationally? |
| `T2.9.2` | — | What does the evidence reveal about whether the origin is singular or multiple? |
| `T2.9.3` | — | Does the origin of this characteristic change across different contexts evidenced in Scripture? |

#### T3 — The Inner Faculties

| Code | Pattern | Question |
|---|---|---|
| `T3.1.1` | — | Does this characteristic engage the perceptive faculty — the inner senses including hearing, sight, taste, touch, smell, and spiritual discernment — and if so, which inner sense and how? |
| `T3.1.2` | — | Does this characteristic enable, deepen, bypass, or impair the perceptive faculty in the person? |
| `T3.1.3` | — | What does the pattern of engagement or non-engagement with perception reveal about the nature of this characteristic? |
| `T3.10.1` | — | Does this characteristic engage conscientiousness — the integrated response of moral awareness, volition, and action — and if so, how? |
| `T3.10.2` | — | Does this characteristic enable, deepen, bypass, or impair conscientiousness in the person? |
| `T3.10.3` | — | What does the pattern of engagement or non-engagement with conscientiousness reveal about the nature of this characteristic? |
| `T3.11.1` | — | Does this characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how? |
| `T3.11.2` | — | Does this characteristic enable, deepen, bypass, or impair relational capacity in the person? |
| `T3.11.3` | — | What does the pattern of engagement or non-engagement with relational capacity reveal about the nature of this characteristic? |
| `T3.2.1` | — | Does this characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how? |
| `T3.2.2` | — | Does this characteristic enable, deepen, bypass, or impair cognition in the person? |
| `T3.2.3` | — | What does the pattern of engagement or non-engagement with cognition reveal about the nature of this characteristic? |
| `T3.3.1` | — | Does this characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how? |
| `T3.3.2` | — | Does this characteristic enable, deepen, bypass, or impair memory in the person? |
| `T3.3.3` | — | What does the pattern of engagement or non-engagement with memory reveal about the nature of this characteristic? |
| `T3.4.1` | — | Does this characteristic engage the affective faculty — feeling and emotional experience — and if so, how? |
| `T3.4.2` | — | Does this characteristic enable, deepen, bypass, or impair affect in the person? |
| `T3.4.3` | — | What does the pattern of engagement or non-engagement with affect reveal about the nature of this characteristic? |
| `T3.5.1` | — | Does this characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how? |
| `T3.5.2` | — | Does this characteristic enable, deepen, bypass, or impair creativity in the person? |
| `T3.5.3` | — | What does the pattern of engagement or non-engagement with creativity reveal about the nature of this characteristic? |
| `T3.6.1` | — | Does this characteristic engage the volitional faculty — the capacity to choose — and if so, how? |
| `T3.6.2` | — | Does this characteristic enable, deepen, bypass, or impair volition in the person — including its three aspects: capacity, interaction with other characteristics, and the constraints under which it operates? |
| `T3.6.3` | — | What does the pattern of engagement or non-engagement with volition reveal about the nature of this characteristic? |
| `T3.7.1` | — | Does this characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how? |
| `T3.7.2` | — | Does this characteristic enable, deepen, bypass, or impair agency in the person? |
| `T3.7.3` | — | What does the pattern of engagement or non-engagement with agency reveal about the nature of this characteristic? |
| `T3.8.1` | — | Does this characteristic engage the moral evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how? |
| `T3.8.2` | — | Does this characteristic enable, deepen, bypass, or impair moral evaluation in the person? |
| `T3.8.3` | — | What does the pattern of engagement or non-engagement with moral evaluation reveal about the nature of this characteristic? |
| `T3.9.1` | — | Does this characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how? |
| `T3.9.2` | — | Does this characteristic enable, deepen, bypass, or impair conscience in the person? |
| `T3.9.3` | — | What does the pattern of engagement or non-engagement with conscience reveal about the nature of this characteristic? |

#### T4 — Relational Interfaces

| Code | Pattern | Question |
|---|---|---|
| `T4.1.1` | — | Does the verse evidence show this characteristic operating from God toward the human person — and if so, how? |
| `T4.1.2` | — | What does the evidence reveal about the basis on which God extends this characteristic — is it conditional, unconditional, covenantal, or responsive? |
| `T4.1.3` | — | What does God's extension of this characteristic reveal about his disposition toward the human person? |
| `T4.1.4` | — | If the evidence is silent on God-to-human operation, note this explicitly. |
| `T4.2.1` | — | Does the verse evidence show this characteristic operating in the human person's movement toward God — in seeking, supplication, worship, or covenant — and if so, how? |
| `T4.2.2` | — | What does the evidence reveal about the inner posture required for this movement? |
| `T4.2.3` | — | What does the human-to-God direction of this characteristic reveal about the person's relationship with God? |
| `T4.2.4` | — | If the evidence is silent on human-to-God operation, note this explicitly. |
| `T4.3.1` | — | Does the verse evidence show this characteristic being extended by one person toward another — and if so, how does it operate in that giving? |
| `T4.3.2` | — | What inner conditions or orientations in the giver enable genuine extension of this characteristic? |
| `T4.3.3` | — | What does the evidence reveal about what the person must have received or become before they can genuinely give this characteristic? |
| `T4.3.4` | — | If the evidence is silent on the giving direction, note this explicitly. |
| `T4.4.1` | — | Does the verse evidence show this characteristic being received by a person from another — and if so, how does it operate in that reception? |
| `T4.4.2` | — | What inner conditions enable or block reception of this characteristic from another person? |
| `T4.4.3` | — | What is the inner-being state of the person who encounters this characteristic from another but does not receive it? |
| `T4.4.4` | — | If the evidence is silent on the receiving direction, note this explicitly. |
| `T4.5.1` | — | Does the evidence indicate whether this characteristic operates differently within existing relational bonds versus across relational distance or difference? |
| `T4.5.2` | — | Does this characteristic operate within covenantal contexts only, or does it cross covenantal boundaries? |
| `T4.5.3` | — | What does the evidence reveal about the relational scope of this characteristic — who is included and who is not? |
| `T4.5.4` | — | If the evidence is silent on relational boundaries, note this explicitly. |
| `T4.6.1` | — | Does the verse evidence show this characteristic operating in relation to other spiritual beings — angelic or adversarial — and if so, how? |
| `T4.6.2` | — | Is this characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial spiritual powers? |
| `T4.6.3` | — | Is this characteristic communicated, strengthened, or mediated through angelic ministry in the evidence? |
| `T4.6.4` | — | If the evidence is silent on the spiritual beings interface, note this explicitly. |

#### T5 — Formative and Developmental Dimension

| Code | Pattern | Question |
|---|---|---|
| `T5.1.1` | — | Does this characteristic produce transformation in the person — and if so, does it change the person's condition, the person's orientation to their condition, or both? |
| `T5.1.2` | — | Is the transformation produced by this characteristic reversible or irreversible in the verse evidence? |
| `T5.1.3` | — | If the evidence is silent on transformation, note this explicitly. |
| `T5.2.1` | — | Does the verse evidence describe a sequence of inner states through which this characteristic moves the person — a before, during, and after? |
| `T5.2.2` | — | What are those states, and what does the sequence reveal about how this characteristic works? |
| `T5.2.3` | — | If the evidence is silent on sequence, note this explicitly. |
| `T5.3.1` | — | What mechanism does this characteristic use to produce change in the person — discipline, encounter, gradual formation, sudden transformation, or something else? |
| `T5.3.2` | — | Does the evidence distinguish between mechanisms in different contexts? |
| `T5.3.3` | — | If the evidence is silent on mechanism, note this explicitly. |
| `T5.4.1` | — | Does the verse evidence show this characteristic operating in relation to suffering or affliction — as a response to it, a product of it, or a context for it? |
| `T5.4.2` | — | Does suffering deepen, test, reveal, or produce this characteristic in the person? |
| `T5.4.3` | — | If the evidence is silent on the relationship to suffering, note this explicitly. |
| `T5.5.1` | — | Does the verse evidence show this characteristic participating in the longer arc of character formation and sanctification — shaping the person over time toward greater likeness? |
| `T5.5.2` | — | What does the evidence reveal about the role of this characteristic in that longer arc? |
| `T5.5.3` | — | If the evidence is silent on formation and sanctification, note this explicitly. |
| `T5.6.1` | — | Does the verse evidence point this characteristic toward an eschatological fullness — a future state toward which its present operation is oriented? |
| `T5.6.2` | — | What does the present experience of this characteristic anticipate about its future fullness? |
| `T5.6.3` | — | If the evidence is silent on eschatological trajectory, note this explicitly. |
| `T5.7.1` | — | Where T2.8 has identified a constitutional deposit from sustained operation of this characteristic, what developmental consequence does that deposit produce over time? |
| `T5.7.2` | — | Does the evidence indicate generational consequence — a deposit carried forward beyond the individual? |
| `T5.7.3` | — | If T2.8 found no deposit, note this explicitly and close T5.7. |

#### T6 — Structural Relationships with Other Characteristics

| Code | Pattern | Question |
|---|---|---|
| `T6.1.1` | — | Which adjacent characteristics appear most frequently alongside this one in the verse evidence? |
| `T6.1.2` | — | What does the pattern of co-occurrence reveal about this characteristic's place in the inner-being landscape? |
| `T6.1.3` | — | If no significant co-occurrence patterns emerge, note this explicitly. |
| `T6.2.1` | — | Does the verse evidence show this characteristic consistently preceding, following, or accompanying another characteristic in a sequence? |
| `T6.2.2` | — | What does the sequence reveal — is the relationship causal, developmental, or correlational? |
| `T6.2.3` | — | If no sequential pattern is evidenced, note this explicitly. |
| `T6.3.1` | — | Does this characteristic produce another characteristic in the verse evidence — and if so, which one, and by what mechanism? |
| `T6.3.2` | — | Is this characteristic produced by another — and if so, which one? |
| `T6.3.3` | — | Is this characteristic a constituent element of another, or does another characteristic constitute part of this one? |
| `T6.3.4` | — | If no causal or constitutive relationship is evidenced, note this explicitly. |
| `T6.4.1` | — | Does this characteristic share vocabulary terms with other characteristics in the programme? |
| `T6.4.2` | — | Does vocabulary sharing extend to root-level architecture — a shared root that generates terms across two or more characteristics? |
| `T6.4.3` | — | What does vocabulary sharing reveal about the conceptual relationship between characteristics? |
| `T6.4.4` | — | If no significant vocabulary sharing is evidenced, note this explicitly. |
| `T6.5.1` | — | Which adjacent characteristic most closely resembles this one — and what precisely distinguishes them? |
| `T6.5.2` | — | Where the evidence shows apparent overlap, what is the precise boundary? |
| `T6.5.3` | — | Is the distinction between this characteristic and its nearest neighbour one of degree, kind, direction, or constitutional level? |
| `T6.5.4` | — | If no significant distinction work is required, note this explicitly. |
| `T6.6.1` | — | Does any verse in this characteristic's evidence base also function as a primary anchor in another characteristic's study? |
| `T6.6.2` | — | What does the shared anchor reveal about the relationship between the two characteristics? |
| `T6.6.3` | — | If no shared verse anchors are identified, note this explicitly. |
| `T6.7.1` | — | How many of this characteristic's confirmed analytical dimensions are shared with another characteristic in the programme? |
| `T6.7.2` | — | What does the pattern of dimensional sharing reveal about the relationship between this characteristic and those it shares dimensions with? |
| `T6.7.3` | — | If dimensional sharing data is not yet available, note this explicitly. |

#### T7 — Evidential and Methodological Foundation

| Code | Pattern | Question |
|---|---|---|
| `T7.1.1` | — | What are the primary Hebrew and Greek terms for this characteristic — and what do their root meanings reveal? |
| `T7.1.10` | — | What does the full vocabulary arc reveal about this characteristic's complete semantic range? |
| `T7.1.2` | — | What is the grammatical range of the primary term (noun, verb, adjective, participle) — and what does that range reveal about how the characteristic operates? |
| `T7.1.3` | — | What is the semantic range of the primary term — across what breadth of meaning does it operate? |
| `T7.1.4` | — | Does the vocabulary include terms that distinguish distinct aspects of this characteristic — disposition versus act, received versus given, condition versus quality? |
| `T7.1.5` | — | Does the vocabulary include a term for the structural opposite or absence of this characteristic? |
| `T7.1.6` | — | Does the vocabulary include a person-type term — a term for the one who habitually possesses or exercises this characteristic? |
| `T7.1.7` | — | Does the vocabulary include a supplication or seeking term — a term for the act of seeking this characteristic from another? |
| `T7.1.8` | — | What does the LXX use of the vocabulary reveal about continuity or development of this characteristic across the Testaments? |
| `T7.1.9` | — | Is there a term newly coined in the NT period for this characteristic — and if so, what does that coinage reveal? |
| `T7.2.1` | — | What is the function of this characteristic's primary term within its primary verse — what role does it play in the sentence and argument? |
| `T7.2.2` | — | What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic) — and what does that form require for responsible interpretation? |
| `T7.2.3` | — | What is the logical structure of key arguments in the verse evidence — what are the premises and conclusions? |
| `T7.2.4` | — | What contextual setting carries the primary verse evidence (judicial, liturgical, covenantal, communal, eschatological) — and what does that setting reveal? |
| `T7.2.5` | — | Does any verse function as the primary anchor for this characteristic — the verse that most fully and directly expresses its essential character? |
| `T7.2.6` | — | What does the primary anchor verse reveal that no other verse reveals? |
| `T7.3.1` | — | Which human science framework (psychology, moral philosophy, developmental psychology, sociology, anthropology, or other) is most useful as an interpretive lens for this characteristic? |
| `T7.3.2` | — | Where the human science framework illuminates the verse evidence — making a finding more coherent or complete — what does it reveal? |
| `T7.3.3` | — | Where the verse evidence and the human science framework diverge, what does the divergence reveal? |
| `T7.3.4` | — | Does the human science framework surface any aspect of this characteristic that the verse evidence has not yet addressed — and does that absence require further verse investigation? |

### 6.2 Registry-specific extensions (0 questions)

_No registry-specific extensions for this word._

