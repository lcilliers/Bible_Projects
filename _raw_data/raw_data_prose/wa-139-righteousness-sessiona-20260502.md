# Session A Extract — r139 righteousness

_Generated: 2026-05-02T05:53:18Z_
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
registry: 139
version: 1
status: approved
author: claude_code
-->

## Section 1 — Summary (Registry Orientation)

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:53:12Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `word_registry`, `wa_term_inventory`, `wa_verse_records`, `verse_context_group`, `wa_dimension_index` |
| Notes | Word synopsis is researcher-authored (`word_registry.word_synopsis`, M21). NULL means authoring is pending — see Action S programme note. |

### 1.1 Word identity

| Field | Value |
|---|---|
| Word | **righteousness** |
| Registry no | 139 |
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
| shared_term_count | 34 |
| term_sharing_ratio | 1.0 |
| phase1_term_count | 34 |
| phase1_verse_count | 1190 |

### 1.5 Registry-level dimension list

`Moral/Conscience`

### 1.6 Derived counts (confirmatory)

| Field | Value |
|---|---|
| OWNER terms (active) | 1 |
| XREF terms (active) | 33 |
| Active verse records | 10 |
| Active verse-context groups | 1 |
| Active dimension assignments | 1 |

<!-- PROSE_SECTION
type: sa_s1_d2
registry: 139
version: 1
status: approved
author: claude_code
-->

## Section 2 — Meaning (Lexical / Semantic)

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:53:13Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `wa_term_inventory.meaning`, `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` |
| Notes | Rendered per OWNER term (1 terms). Raw meaning text lives in `wa_term_inventory.meaning`; structured parse in `wa_meaning_*` tables. |

### 2.G1345 — G1345 (dikaiōma) — Greek

_step gloss: righteous act · analysis gloss: righteous act_

_No raw meaning text for this term._

**Mounce short def:** regulation, requirement, commandment;righteous act of righteousness

**Parse metadata:** senses=1 · stems=0 · causative=0 · domain_tags=0 · parser=1.0.0

**Senses:**

| # | Level | Stem? | Stem label | Domain | Sense text |
|---|---|---|---|---|---|
| 0 | 1 (d1) | 0 | — | — | regulation, requirement, commandment;righteous act of righteousness  primarily a rightful act, act of justice, equity; a sentence, of condemnation, Rev. 15:4; in NT, of acquittal, justification, Rom. 5:16; a decree, law, ordinance,regulation, requirement Lk. 1:6; Rom. 1:32; 2:26; 8:4; Heb. 9:1, 10; a meritorious act, an instance of perfect righteousness, Rom. 5:18; Rev. 19:8* |

<!-- PROSE_SECTION
type: sa_s1_d4
registry: 139
version: 1
status: approved
author: claude_code
-->

## Section 3 — Terms (OWNER + XREF) with Analytical Metadata

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:53:13Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `wa_term_inventory`, `mti_terms`, `mti_term_flags`, `wa_data_quality_flags`, `wa_term_root_family`, `wa_term_related_words`, `wa_verse_records` |
| Notes | Total active terms: 34. OWNER listed first, then XREF. |

### 3.OWNER.G1345 — G1345 (dikaiōma) — OWNER

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | righteous act |
| Analysis gloss | righteous act |
| Occurrence count | 128 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 139 (this registry) |
| owning_word | righteousness |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1345. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1345 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1345. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1345 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_STRONG | 1 |

**Root family:**

| Root | Language | Gloss | Note |
|---|---|---|---|
| `DIKAIŌ` | Greek | righteous act | Backfilled 2026-04-09 from wa_term_related_words clustering |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=10, active=10, delete_flagged=0.

### 3.XREF.G0091 — G0091 (adikeō) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | to harm |
| Analysis gloss | to harm |
| Occurrence count | 82 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 57 (other) |
| owning_word | evil |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0091. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0091 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0091. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0091 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0091. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0091 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=23, active=0, delete_flagged=23.

### 3.XREF.G0092 — G0092 (adikēma) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | crime |
| Analysis gloss | crime |
| Occurrence count | 19 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | crime |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G0092. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0092. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0092 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G0092. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0092. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0092 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=3, active=0, delete_flagged=3.

### 3.XREF.G0093 — G0093 (adikia) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | unrighteousness |
| Analysis gloss | unrighteousness |
| Occurrence count | 214 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 57 (other) |
| owning_word | evil |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0093. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0093 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0093. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0093 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0093. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0093 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=24, active=0, delete_flagged=24.

### 3.XREF.G0094 — G0094 (adikos) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | unjust |
| Analysis gloss | unjust |
| Occurrence count | 101 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 98 (other) |
| owning_word | unjust |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0094. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0094 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0094. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0094 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=11, active=0, delete_flagged=11.

### 3.XREF.G0095 — G0095 (adikōs) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | unjustly |
| Analysis gloss | unjustly |
| Occurrence count | 22 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | unjustly |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G0095. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0095. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0095 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G0095. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0095. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0095 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 10 — Dependence / Creatureliness | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.G0476 — G0476 (antidikos) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | opponent |
| Analysis gloss | opponent |
| Occurrence count | 12 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | opponent |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 4 confirmed verse records for G0476. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0476. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0476 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 4 confirmed verse records for G0476. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G0476. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G0476 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 10 — Dependence / Creatureliness | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0473 | anti | for | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=4, active=0, delete_flagged=4.

### 3.XREF.G1341 — G1341 (dikaiokrisia) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | justice |
| Analysis gloss | justice |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | justice |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G1341. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1341. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1341 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G1341. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1341. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1341 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 11 — Divine-Human Correspondence | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G2920 | krisis | judgment | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.G1342 — G1342 (dikaios) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | just |
| Analysis gloss | just |
| Occurrence count | 383 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 98 (other) |
| owning_word | just |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1342. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1342 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1342. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1342 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 2 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=74, active=0, delete_flagged=74.

### 3.XREF.G1343 — G1343 (dikaiosunē) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | righteousness |
| Analysis gloss | righteousness |
| Occurrence count | 353 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 98 (other) |
| owning_word | justice |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1343. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1343 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1343. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1343 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 3 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=74, active=0, delete_flagged=74.

### 3.XREF.G1344 — G1344 (dikaioō) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | to justify |
| Analysis gloss | to justify |
| Occurrence count | 71 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 98 (other) |
| owning_word | to justify |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1344. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1344 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1344. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1344 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=36, active=0, delete_flagged=36.

### 3.XREF.G1346 — G1346 (dikaiōs) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | rightly |
| Analysis gloss | rightly |
| Occurrence count | 11 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | rightly |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 11. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1346. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1346 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 11. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1346. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1346 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=5, active=0, delete_flagged=5.

### 3.XREF.G1347 — G1347 (dikaiōsis) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | justification |
| Analysis gloss | justification |
| Occurrence count | 3 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | justification |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G1347. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1347. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1347 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G1347. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1347. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1347 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 08 — Transformation | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=2, active=0, delete_flagged=2.

### 3.XREF.G1348 — G1348 (dikastēs) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | magistrate |
| Analysis gloss | magistrate |
| Occurrence count | 11 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | magistrate |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G1348. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1348. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1348 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G1348. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1348. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1348 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 04 — Volition | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=2, active=0, delete_flagged=2.

### 3.XREF.G1349 — G1349 (dikē) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | condemnation |
| Analysis gloss | condemnation |
| Occurrence count | 21 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 98 (other) |
| owning_word | justice |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G1349. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1349. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1349 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G1349. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1349. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1349 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 3 confirmed verse records for G1349. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1349. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1349 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=3, active=0, delete_flagged=3.

### 3.XREF.G1738 — G1738 (endikos) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | just |
| Analysis gloss | just |
| Occurrence count | 2 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | just |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G1738. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1738. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1738 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for G1738. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G1738. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G1738 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1722 | en | in/on/among | — |
| G2613 | katadikazō | to condemn | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=2, active=0, delete_flagged=2.

### 3.XREF.G2613 — G2613 (katadikazō) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | to condemn |
| Analysis gloss | to condemn |
| Occurrence count | 9 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | to condemn |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 4 confirmed verse records for G2613. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G2613. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G2613 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 4 confirmed verse records for G2613. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G2613. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G2613 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2596 | kata | according to | — |
| G5267 | hupodikos | accountable | — |

**Verse record counts:** total=4, active=0, delete_flagged=4.

### 3.XREF.G5267 — G5267 (hupodikos) — XREF

| Field | Value |
|---|---|
| Language | Greek |
| STEP gloss | accountable |
| Analysis gloss | accountable |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_thin` |
| owning_registry_fk | 98 (other) |
| owning_word | accountable |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G5267. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G5267. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G5267 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for G5267. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for G5267. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for G5267 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 11 — Divine-Human Correspondence | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0091 | adikeō | to harm | — |
| G0092 | adikēma | crime | — |
| G0093 | adikia | unrighteousness | — |
| G0094 | adikos | unjust | — |
| G0095 | adikōs | unjustly | — |
| G0476 | antidikos | opponent | — |
| G1341 | dikaiokrisia | justice | — |
| G1342 | dikaios | just | — |
| G1343 | dikaiosunē | righteousness | — |
| G1344 | dikaioō | to justify | — |
| G1345 | dikaiōma | righteous act | — |
| G1346 | dikaiōs | rightly | — |
| G1347 | dikaiōsis | justification | — |
| G1348 | dikastēs | magistrate | — |
| G1349 | dikē | condemnation | — |
| G1738 | endikos | just | — |
| G2613 | katadikazō | to condemn | — |
| G5259G | hupo | by/under: by | — |
| G5259H | hupo | by/under: under | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H0518H — H0518H (im) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | if: surely no |
| Analysis gloss | if: surely no |
| Occurrence count | 105 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 28 (other) |
| owning_word | if: surely no |
| exclusion_reason | Session A v4 relatedNos bleed confirmed by prior Session B review. See FrameworkB-SessionB-Handover-20260324.docx §3.4. |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H0518H. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0509 | a.lats | to urge | — |
| H0512 | el.qo.shi | Elkoshite | — |
| H0514 | el.te.qe | Eltekeh | — |
| H0515 | el.te.qon | Eltekon | — |
| H0518A | im | if | — |
| H0518B | — | if: except | — |
| H0518I | im | if: surely yes | — |
| H0518J | im | if: until | — |
| H3588A | ki | for | — |
| H3588B | ki m | that if: except | — |
| H3588C | ki al ken | for as that: since | — |
| H5921B | — | as | — |

**Verse record counts:** total=94, active=0, delete_flagged=94.

### 3.XREF.H0518I — H0518I (im) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | if: surely yes |
| Analysis gloss | if: surely yes |
| Occurrence count | 81 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 28 (other) |
| owning_word | if: surely yes |
| exclusion_reason | Session A v4 relatedNos bleed confirmed by prior Session B review. See FrameworkB-SessionB-Handover-20260324.docx §3.4. |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H0518I. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518I. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518I. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518I. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518I stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0509 | a.lats | to urge | — |
| H0512 | el.qo.shi | Elkoshite | — |
| H0514 | el.te.qe | Eltekeh | — |
| H0515 | el.te.qon | Eltekon | — |
| H0518A | im | if | — |
| H0518B | — | if: except | — |
| H0518H | im | if: surely no | — |
| H0518J | im | if: until | — |
| H3588A | ki | for | — |
| H3588B | ki m | that if: except | — |
| H3588C | ki al ken | for as that: since | — |
| H5921B | — | as | — |

**Verse record counts:** total=74, active=0, delete_flagged=74.

### 3.XREF.H0518J — H0518J (im) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | if: until |
| Analysis gloss | if: until |
| Occurrence count | 17 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 28 (other) |
| owning_word | if: until |
| exclusion_reason | Session A v4 relatedNos bleed confirmed by prior Session B review. See FrameworkB-SessionB-Handover-20260324.docx §3.4. |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 17. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H0518J. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518J. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518J stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 17. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 17. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518J stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 17. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518J. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518J stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 17. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H0518J. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H0518J stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0509 | a.lats | to urge | — |
| H0512 | el.qo.shi | Elkoshite | — |
| H0514 | el.te.qe | Eltekeh | — |
| H0515 | el.te.qon | Eltekon | — |
| H0518A | im | if | — |
| H0518B | — | if: except | — |
| H0518H | im | if: surely no | — |
| H0518I | im | if: surely yes | — |
| H3588A | ki | for | — |
| H3588B | ki m | that if: except | — |
| H3588C | ki al ken | for as that: since | — |
| H5921B | — | as | — |

**Verse record counts:** total=15, active=0, delete_flagged=15.

### 3.XREF.H1933A — H1933A (ha.va) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | to fall |
| Analysis gloss | to fall |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 43 (other) |
| owning_word | to fall |
| exclusion_reason | Confirmed candidate_delete. Bleed vocabulary or adequately covered by extracted terms. |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 1. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H1933A. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933A. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 1. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H1933A. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933A. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H1933A. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933A. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H1933A. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933A. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H1933A. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933A. STEP returned no word analysis block for this term. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0183 | a.vah | to desire | — |
| H1933B | ha.vah | to be | — |
| H1934 | ha.va | to be | — |
| H1942 | hav.vah | desire | — |
| H1961 | ha.yah | to be | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H1933B — H1933B (ha.vah) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | to be |
| Analysis gloss | to be |
| Occurrence count | 5 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 43 (other) |
| owning_word | to be |
| exclusion_reason | Confirmed candidate_delete. Bleed vocabulary or adequately covered by extracted terms. |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H1933B. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933B. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H1933B. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933B. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933B. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933B. STEP returned no word analysis block for this term. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H1933B. STEP returned no word analysis block for this term. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0183 | a.vah | to desire | — |
| H1933A | ha.va | to fall | — |
| H1934 | ha.va | to be | — |
| H1942 | hav.vah | desire | — |
| H1943 | ho.vah | misfortune | — |
| H1944 | ho.ham | Hoham | — |
| H1953 | ye.ho.sha.ma | Hoshama | — |
| H1961 | ha.yah | to be | — |
| H1962 | hay.yah | calamity | — |
| H3050 | yah | LORD | — |
| H3058G | ye.hu | Jehu | — |
| H3058H | ye.hu | Jehu | — |
| H3058I | ye.hu | Jehu | — |
| H3058J | ye.hu | Jehu | — |
| H3058K | ye.hu | Jehu | — |
| H3059G | ye.ho.a.chaz | Jehoahaz | — |
| H3059H | ye.ho.a.chaz | Jehoahaz | — |
| H3059I | ye.ho.a.chaz | Ahaziah | — |
| H3060G | ye.ho.ash | Jehoash | — |
| H3060H | ye.ho.ash | Jehoash | — |
| H3068G | ye.ho.vah | LORD | — |
| H3068H | ye.ho.vah | The Lord | — |
| H3068I | ye.ho.vah | [Jerusalem of] the Lord | — |
| H3069 | ye.ho.vih | YHWH/God | — |
| H3075G | ye.ho.za.vad | Jehozabad | — |
| H3075H | ye.ho.za.vad | Jehozabad | — |
| H3075I | ye.ho.za.vad | Jehozabad | — |
| H3076G | ye.ho.cha.nan | Johanan | — |
| H3076H | ye.ho.cha.nan | Johanan | — |
| H3076I | ye.ho.cha.nan | Jehohanan | — |
| H3076J | ye.ho.cha.nan | Jehohanan | — |
| H3076K | ye.ho.cha.nan | Jehohanan | — |
| H3076L | ye.ho.cha.nan | Johanan | — |
| H3076M | ye.ho.cha.nan | Jehohanan | — |
| H3076N | ye.ho.cha.nan | Jehohanan | — |
| H3076O | ye.ho.cha.nan | Jehohanan | — |
| H3076P | ye.ho.cha.nan | Jehohanan | — |
| H3076Q | ye.ho.cha.nan | Jehohanan | — |
| H3077G | ye.ho.ya.da | Jehoiada | — |
| H3077H | ye.ho.ya.da | Jehoiada | — |
| H3077I | ye.ho.ya.da | Jehoiada | — |
| H3077J | ye.ho.ya.da | Jehoiada | — |
| H3078 | ye.ho.ya.khin | Jehoiachin | — |
| H3079 | ye.ho.ya.qim | Jehoiakim | — |
| H3080G | ye.ho.ya.riv | Jehoiarib | — |
| H3080H | ye.ho.ya.riv | Jehoiarib | — |
| H3081 | ye.hu.khal | Jehucal | — |
| H3082G | ye.ho.na.dav | Jonadab | — |
| H3082H | ye.ho.na.dav | Jonadab | — |
| H3083G | ye.ho.na.tan | Jonathan | — |
| H3083H | ye.ho.na.tan | Jonathan | — |
| H3083I | ye.ho.na.tan | Jonathan | — |
| H3083J | ye.ho.na.tan | Jonathan | — |
| H3083K | ye.ho.na.tan | Jonathan | — |
| H3083L | ye.ho.na.tan | Jehonathan | — |
| H3083M | ye.ho.na.tan | Jehonathan | — |
| H3083N | ye.ho.na.tan | Jonathan | — |
| H3083O | ye.ho.na.tan | Jonathan | — |
| H3085 | ye.ho.ad.dah | Jehoaddah | — |
| H3086 | ye.ho.ad.dan | Jehoaddan | — |
| H3087 | ye.ho.tsa.daq | Jehozadak | — |
| H3088G | ye.ho.ram | Jehoram | — |
| H3088H | ye.ho.ram | Jehoram | — |
| H3088I | ye.ho.ram | Joram | — |
| H3089 | ye.ho.she.va | Jehosheba | — |
| H3090 | ye.ho.shav.at | Jehoshabeath | — |
| H3091G | ye.ho.shu.a | Joshua | — |
| H3091H | ye.ho.shu.a | Joshua | — |
| H3091I | ye.ho.shu.a | Joshua | — |
| H3091J | ye.ho.shu.a | Joshua | — |
| H3092G | ye.ho.sha.phat | Jehoshaphat | — |
| H3092H | ye.ho.sha.phat | Jehoshaphat | — |
| H3092I | ye.ho.sha.phat | Jehoshaphat | — |
| H3092J | ye.ho.sha.phat | Jehoshaphat | — |
| H3092K | ye.ho.sha.phat | [Valley of] Jehoshaphat | — |
| H3097G | yo.av | Joab | — |
| H3097H | yo.av | Joab | — |
| H3097I | yo.av | Joab | — |
| H3097J | yo.av | Joab | — |
| H3098G | yo.ach | Joah | — |
| H3098H | yo.ach | Joah | — |
| H3098I | yo.ach | Joah | — |
| H3098J | yo.ach | Joah | — |
| H3098K | yo.ach | Joah | — |
| H3098L | yo.ach | Joah | — |
| H3099G | yo.a.chaz | Joahaz | — |
| H3099H | yo.a.chaz | Joahaz | — |
| H3099I | yo.a.chaz | Jehoahaz | — |
| H3100G | yo.el | Joel | — |
| H3100H | yo.el | Joel | — |
| H3100I | yo.el | Joel | — |
| H3100J | yo.el | Joel | — |
| H3100K | yo.el | Joel | — |
| H3100L | yo.el | Joel | — |
| H3100M | yo.el | Joel | — |
| H3100N | yo.el | Joel | — |
| H3100O | yo.el | Joel | — |
| H3100P | yo.el | Joel | — |
| H3100Q | yo.el | Joel | — |
| H3100R | yo.el | Joel | — |
| H3100S | yo.el | Joel | — |
| H3100T | yo.el | Joel | — |
| H3100U | yo.el | Joel | — |
| H3101G | yo.ash | Joash | — |
| H3101H | yo.ash | Joash | — |
| H3101I | yo.ash | Joash | — |
| H3101J | yo.ash | Joash | — |
| H3101K | yo.ash | Joash | — |
| H3101L | yo.ash | Joash | — |
| H3107G | yo.za.vad | Jozacar | — |
| H3107H | yo.za.vad | Jozabad | — |
| H3107I | yo.za.vad | Jozabad | — |
| H3107J | yo.za.vad | Jozabad | — |
| H3107K | yo.za.vad | Jozabad | — |
| H3107L | yo.za.vad | Jozabad | — |
| H3107M | yo.za.vad | Jozabad | — |
| H3107N | yo.za.vad | Jozabad | — |
| H3107O | yo.za.vad | Jozabad | — |
| H3107P | yo.za.vad | Jozabad | — |
| H3107Q | yo.za.vad | Jozabad | — |
| H3108 | yo.za.khar | Jozacar | — |
| H3110G | yo.cha.nan | Johanan | — |
| H3110H | yo.cha.nan | Johanan | — |
| H3110I | yo.cha.nan | Johanan | — |
| H3110J | yo.cha.nan | Johanan | — |
| H3110K | yo.cha.nan | Johanan | — |
| H3110L | yo.cha.nan | Johanan | — |
| H3111G | yo.ya.da | Joiada | — |
| H3111H | yo.ya.da | Joiada | — |
| H3112 | yo.ya.khin | Jehoiachin | — |
| H3113 | yo.ya.qim | Joiakim | — |
| H3114G | yo.ya.riv | Joiarib | — |
| H3114H | yo.ya.riv | Joiarib | — |
| H3114I | yo.ya.riv | Joiarib | — |
| H3115 | yo.khe.ved | Jochebed | — |
| H3116 | yu.khal | Jucal | — |
| H3122G | yo.na.dav | Jonadab | — |
| H3122H | yo.na.dav | Jonadab | — |
| H3129G | yo.na.tan | Jonathan | — |
| H3129H | yo.na.tan | Jonathan | — |
| H3129I | yo.na.tan | Jonathan | — |
| H3129J | yo.na.tan | Jonathan | — |
| H3129K | yo.na.tan | Jonathan | — |
| H3129L | yo.na.tan | Jonathan | — |
| H3129M | yo.na.tan | Jonathan | — |
| H3129N | yo.na.tan | Jonathan | — |
| H3129O | yo.na.tan | Jonathan | — |
| H3129P | yo.na.tan | Jonathan | — |
| H3133 | yo.ed | Joed | — |
| H3134 | yo.e.zer | Joezer | — |
| H3135G | yo.ash | Joash | — |
| H3135H | yo.ash | Joash | — |
| H3136A | yo.tsa.daq | Jozadak | — |
| H3136B | yo.tsa.daq | Jozadak | — |
| H3136G | yo.tsa.daq | Jozadak | — |
| H3137 | yo.qim | Jokim | — |
| H3141G | yo.ram | Joram | — |
| H3141H | yo.ram | Joram | — |
| H3141I | yo.ram | Joram | — |
| H3141J | yo.ram | Joram | — |
| H3146G | yo.sha.phat | Joshaphat | — |
| H3146H | yo.sha.phat | Joshaphat | — |
| H3147G | yo.tam | Jotham | — |
| H3147H | yo.tam | Jotham | — |
| H3147I | yo.tam | Jotham | — |
| H3442G | ye.shu.a | Jeshua | — |
| H3442H | ye.shu.a | Jeshua | — |
| H3442I | ye.shu.a | Jeshua | — |
| H3442J | ye.shu.a | Jeshua | — |
| H3442K | ye.shu.a | Jeshua | — |
| H3442L | ye.shu.a | Jeshua | — |
| H3442M | ye.shu.a | Jeshua | — |
| H3442N | ye.shu.a | Jeshua | — |
| H3442O | ye.shu.a | Jeshua | — |
| H3442P | ye.shu.a | Jeshua | — |
| H3659 | kon.ya.hu | Coniah | — |

**Verse record counts:** total=5, active=0, delete_flagged=5.

### 3.XREF.H3588B — H3588B (ki m) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | that if: except |
| Analysis gloss | that if: except |
| Occurrence count | 313 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 28 (other) |
| owning_word | that if: except |
| exclusion_reason | Session A v4 relatedNos bleed confirmed by prior Session B review. See FrameworkB-SessionB-Handover-20260324.docx §3.4. |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H3588B. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588B. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588B. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588B. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588B. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588B. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588B. STEP returned no word analysis block for this term. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0518A | im | if | — |
| H0518H | im | if: surely no | — |
| H0518I | im | if: surely yes | — |
| H0518J | im | if: until | — |
| H3588A | ki | for | — |
| H3588C | ki al ken | for as that: since | — |
| H3589 | kid | ruin | — |
| H3651A | ken | right | — |
| H3651C | ken | so | — |
| H5921A | al | upon | — |
| H5921B | — | as | — |

**Verse record counts:** total=136, active=0, delete_flagged=136.

### 3.XREF.H3588C — H3588C (ki al ken) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | for as that: since |
| Analysis gloss | for as that: since |
| Occurrence count | 28 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 28 (other) |
| owning_word | for as that: since |
| exclusion_reason | Session A v4 relatedNos bleed confirmed by prior Session B review. See FrameworkB-SessionB-Handover-20260324.docx §3.4. |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H3588C. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588C. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588C. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588C. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588C. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588C. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3588C. STEP returned no word analysis block for this term. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0518A | im | if | — |
| H0518H | im | if: surely no | — |
| H0518I | im | if: surely yes | — |
| H0518J | im | if: until | — |
| H3588A | ki | for | — |
| H3588B | ki m | that if: except | — |
| H3589 | kid | ruin | — |
| H3651A | ken | right | — |
| H3651C | ken | so | — |
| H5921A | al | upon | — |
| H5921B | — | as | — |

**Verse record counts:** total=10, active=0, delete_flagged=10.

### 3.XREF.H3589 — H3589 (kid) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | ruin |
| Analysis gloss | ruin |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 28 (other) |
| owning_word | ruin |
| exclusion_reason | Session A v4 relatedNos bleed confirmed by prior Session B review. See FrameworkB-SessionB-Handover-20260324.docx §3.4. |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Low occurrence count: 1. Statistical patterns unreliable with fewer than 20 occurrences. | — |
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H3589. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3589. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H3589. Threshold is 5. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H3589. Threshold is 5. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H3589. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3589. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H3589. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3589. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0518A | im | if | — |
| H0518H | im | if: surely no | — |
| H0518I | im | if: surely yes | — |
| H0518J | im | if: until | — |
| H3588A | ki | for | — |
| H3588B | ki m | that if: except | — |
| H3588C | ki al ken | for as that: since | — |
| H3651A | ken | right | — |
| H3651C | ken | so | — |
| H5921A | al | upon | — |
| H5921B | — | as | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H3651A — H3651A (ken) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | right |
| Analysis gloss | right |
| Occurrence count | 22 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 121 (other) |
| owning_word | praise |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_MINIMAL` | R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_AI_WIDER_CONTEXT;R_RELEVANCE_REVIEW | Zero confirmed verse records for H3651A. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3651A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3651A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3651A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3651A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3651A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3651A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3651A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3651A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3651A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3651A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3651A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3651A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3651A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H3651A. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H3651A stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0403 | a.khen | surely | — |
| H3199G | ya.khin | Jachin | — |
| H3199H | ya.khin | Jachin | — |
| H3199I | ya.khin | Jachin | — |
| H3199J | ya.khin | Jachin | — |
| H3200 | ya.khi.ni | Jachinite | — |
| H3204 | ye.kho.ne.yah | Jeconiah | — |
| H3559A | kun | to establish: prepare | — |
| H3559B | na.khon | blow | — |
| H3559H | kun | to establish: establish | — |
| H3559I | kun | to establish: make | — |
| H3559J | kun | to establish: commit | — |
| H3559K | kun | to establish: right | — |
| H3560 | kun | Cun | — |
| H3561 | kav.van | bun | — |
| H3562G | ko.nan.ya.hu | Conaniah | — |
| H3563A | kos | cup | — |
| H3563B | kos | owl | — |
| H3651C | ken | so | — |
| H3652 | ken | thus | — |
| H4349 | ma.khon | foundation | — |
| H4350 | me.kho.nah | base | — |
| H4369 | me.khu.nah | base | — |
| H5225 | na.khon | Nacon | — |
| H8498 | te.khu.nah | fitting | — |
| H8499 | te.khu.nah | place | — |

**Verse record counts:** total=21, active=0, delete_flagged=21.

### 3.XREF.H4941G — H4941G (mish.pat) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | justice: judgement |
| Analysis gloss | justice: judgement |
| Occurrence count | 220 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 98 (other) |
| owning_word | justice |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H4941G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H4941G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H4941G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H4941G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H4941G. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H4941G stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 03 — Cognition | CLAUDE_AI | 1 |
| 05 — Moral Character | CLAUDE_AI | 1 |
| 06 — Relational Disposition | CLAUDE_AI | 1 |
| 08 — Transformation | CLAUDE_AI | 1 |
| 10 — Dependence / Creatureliness | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H4941H | mish.pat | justice | — |
| H4941I | mish.pat | justice: rule | — |
| H4941J | mish.pat | justice: custom | — |
| H4941K | mish.pat | [Hall of] Judgment | — |
| H8196 | she.phot | judgment | — |
| H8199 | sha.phat | to judge | — |
| H8200 | she.phat | to judge | — |
| H8201 | she.phet | judgment | — |
| H8202G | sha.phat | Shaphat | — |
| H8202H | sha.phat | Shaphat | — |
| H8202I | sha.phat | Shaphat | — |
| H8202J | sha.phat | Shaphat | — |
| H8202K | sha.phat | Shaphat | — |
| H8203G | she.phat.ya.hu | Shephatiah | — |
| H8203H | she.phat.ya.hu | Shephatiah | — |
| H8203I | she.phat.ya.hu | Shephatiah | — |
| H8203J | she.phat.ya.hu | Shephatiah | — |
| H8203K | she.phat.ya.hu | Shephatiah | — |
| H8203L | she.phat.ya.hu | Shephatiah | — |
| H8203M | she.phat.ya.hu | Shephatiah | — |
| H8203N | she.phat.ya.hu | Shephatiah | — |
| H8203O | she.phat.ya.hu | Shephatiah | — |
| H8204 | shiph.tan | Shiphtan | — |

**Verse record counts:** total=68, active=0, delete_flagged=68.

### 3.XREF.H6662 — H6662 (tsad.diq) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | righteous |
| Analysis gloss | righteous |
| Occurrence count | 206 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 77 (other) |
| owning_word | righteous |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6662. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6662. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6662. STEP returned no word analysis block for this term. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 01 — Emotion — Positive | KEYWORD_WEAK | 1 |
| 05 — Moral Character | KEYWORD_STRONG | 1 |
| 05 — Moral Character | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H6659G | tsa.doq | Zadok | — |
| H6659H | tsa.doq | Zadok | — |
| H6659I | tsa.doq | Zadok | — |
| H6659J | tsa.doq | Zadok | — |
| H6659K | tsa.doq | Zadok | — |
| H6659L | tsa.doq | Zadok | — |
| H6659M | tsa.doq | Zadok | — |
| H6663 | tsa.deq | to justify | — |
| H6664G | tse.deq | righteousness | — |
| H6664H | tse.deq | Righteousness [God] | — |
| H6666 | tse.da.qah | righteousness | — |
| H6667G | tsid.qiy.ya.hu | Zedekiah | — |
| H6667H | tsid.qiy.ya.hu | Zedekiah | — |
| H6667I | tsid.qiy.ya.hu | Zedekiah | — |
| H6667J | tsid.qiy.ya.hu | Zedekiah | — |
| H6667K | tsid.qiy.ya.hu | Zedekiah | — |
| H6667L | tsid.qiy.ya.hu | Zedekiah | — |

**Verse record counts:** total=184, active=0, delete_flagged=184.

### 3.XREF.H6663 — H6663 (tsa.deq) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | to justify |
| Analysis gloss | to justify |
| Occurrence count | 41 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 98 (other) |
| owning_word | justice |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6663. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6663. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6663. STEP returned no word analysis block for this term. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 03 — Cognition | CLAUDE_AI | 1 |
| 05 — Moral Character | CLAUDE_AI | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H6659G | tsa.doq | Zadok | — |
| H6659H | tsa.doq | Zadok | — |
| H6659I | tsa.doq | Zadok | — |
| H6659J | tsa.doq | Zadok | — |
| H6659K | tsa.doq | Zadok | — |
| H6659L | tsa.doq | Zadok | — |
| H6659M | tsa.doq | Zadok | — |
| H6662 | tsad.diq | righteous | — |
| H6664G | tse.deq | righteousness | — |
| H6664H | tse.deq | Righteousness [God] | — |
| H6666 | tse.da.qah | righteousness | — |
| H6667G | tsid.qiy.ya.hu | Zedekiah | — |
| H6667H | tsid.qiy.ya.hu | Zedekiah | — |
| H6667I | tsid.qiy.ya.hu | Zedekiah | — |
| H6667J | tsid.qiy.ya.hu | Zedekiah | — |
| H6667K | tsid.qiy.ya.hu | Zedekiah | — |
| H6667L | tsid.qiy.ya.hu | Zedekiah | — |

**Verse record counts:** total=40, active=0, delete_flagged=40.

### 3.XREF.H6664G — H6664G (tse.deq) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | righteousness |
| Analysis gloss | righteousness |
| Occurrence count | 117 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 98 (other) |
| owning_word | justice |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6664G. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6664G. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6664G. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6664G. STEP returned no word analysis block for this term. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | CLAUDE_AI | 4 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H6659G | tsa.doq | Zadok | — |
| H6659H | tsa.doq | Zadok | — |
| H6659I | tsa.doq | Zadok | — |
| H6659J | tsa.doq | Zadok | — |
| H6659K | tsa.doq | Zadok | — |
| H6659L | tsa.doq | Zadok | — |
| H6659M | tsa.doq | Zadok | — |
| H6662 | tsad.diq | righteous | — |
| H6663 | tsa.deq | to justify | — |
| H6664H | tse.deq | Righteousness [God] | — |
| H6666 | tse.da.qah | righteousness | — |
| H6667G | tsid.qiy.ya.hu | Zedekiah | — |
| H6667H | tsid.qiy.ya.hu | Zedekiah | — |
| H6667I | tsid.qiy.ya.hu | Zedekiah | — |
| H6667J | tsid.qiy.ya.hu | Zedekiah | — |
| H6667K | tsid.qiy.ya.hu | Zedekiah | — |
| H6667L | tsid.qiy.ya.hu | Zedekiah | — |

**Verse record counts:** total=110, active=0, delete_flagged=110.

### 3.XREF.H6664H — H6664H (tse.deq) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | Righteousness [God] |
| Analysis gloss | Righteousness [God] |
| Occurrence count | 2 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted_theological_anchor` |
| owning_registry_fk | 117 (other) |
| owning_word | peace |
| owning_part | 3 |
| anchor_note | Framework A/B intersection term. Ontological ground of inner-being peace. Session B analysis deferred until intersection question formally opened. |

**MTI flags:**
- `VERSE_EVIDENCE_MINIMAL` — Minimal biblical evidence for this term in the extraction. Does NOT mean the term is irrelevant — triggers research inve

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H6664H. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6664H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H6664H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H6664H. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6664H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H6664H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 2 confirmed verse records for H6664H. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6664H. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H6664H stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| G0005 | abba | Abba | — |
| G1682 | elōi | Eloi | — |
| G2241 | ēli | Eli | — |
| G4519 | sabaōth | hosts | — |
| G5310 | hupsistos | Highest | — |
| H0136 | a.do.na | Lord [God] | — |
| H0410G | el | God | — |
| H0410I | el | El [Elohe] | — |
| H0410J | el | El [Most High] | — |
| H0430G | e.lo.him | God | — |
| H0430H | e.lo.him | [LORD]-Elohe | — |
| H0430I | e.lo.him | [Gibeath]-elohim | — |
| H1180 | ba.a.li | Baal [used for God] | — |
| H3050 | yah | LORD | — |
| H3068G | ye.ho.vah | LORD | — |
| H3068H | ye.ho.vah | The Lord | — |
| H3068I | ye.ho.vah | [Jerusalem of] the Lord | — |
| H3070 | yir.eh | Provider [God] | — |
| H5251G | nes | Banner [God] | — |
| H5251H | nes | ensign | — |
| H5769G | o.lam | forever: enduring | — |
| H5769H | o.lam | Everlasting [God] | — |
| H5769I | o.lam | forever: any time | — |
| H5769J | o.lam | forever: antiquity | — |
| H5920H | al | height | — |
| H5943 | il.lay | Most High [God] | — |
| H5945A | el.yon | high | — |
| H5945B | el.yon | Most High [God] | — |
| H5945G | el.yon | Upper [Beth Horon] | — |
| H5945H | el.yon | [LORD] Most High | — |
| H5946 | el.yon | Most High [God] | — |
| H6635A | tsa.va | army | — |
| H6635B | tsa.va | [Lord of] Hosts | — |
| H6635H | tsa.va | army: war | — |
| H6635I | tsa.va | army: duty | — |
| H6664G | tse.deq | righteousness | — |
| H7067G | qan.na | Jealous [God] | — |
| H7067H | qan.na | jealous | — |
| H7200N | ra.ah | Provider [God] | — |
| H7706 | shad.day | Almighty [God] | — |
| H7965G | sha.lom | peace | — |
| H7965H | sha.lom | Peace [God] | — |
| H7965I | sha.lom | peace: well-being | — |
| H7965J | sha.lom | peace: friendship | — |
| H7965K | sha.lom | peace: greeting | — |
| H7965L | sha.lom | peace: completely | — |

**Verse record counts:** total=2, active=0, delete_flagged=2.

### 3.XREF.H6665 — H6665 (tsid.qah) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | righteousness |
| Analysis gloss | righteousness |
| Occurrence count | 1 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `delete` |
| owning_registry_fk | 77 (other) |
| owning_word | righteousness |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H6665. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6665. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H6665 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H6665. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6665. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H6665 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |
| `VERSE_EVIDENCE_CONCENTRATED` | R_STEP_EXHAUST_CHECK;R_AI_WIDER_CONTEXT | Only 1 confirmed verse records for H6665. Threshold is 5. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6665. STEP returned no word analysis block for this term. | — |
| `PROSE_ONLY_MEANING` | — | Meaning for H6665 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available. | — |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H0677 | ets.ba | digit | — |
| H6655 | tsad | side | — |
| H6656 | tse.da | intended | — |
| H6666 | tse.da.qah | righteousness | — |
| H6676 | tsav.var | neck | — |

**Verse record counts:** total=1, active=0, delete_flagged=1.

### 3.XREF.H6666 — H6666 (tse.da.qah) — XREF

| Field | Value |
|---|---|
| Language | Hebrew |
| STEP gloss | righteousness |
| Analysis gloss | righteousness |
| Occurrence count | 165 |
| Causative form present | 0 |
| Evidential status | — |

**MTI (Mounce Term Index) canonical row:**

| Field | Value |
|---|---|
| status | `extracted` |
| owning_registry_fk | 77 (other) |
| owning_word | honesty |

**Data quality flags:**

| Flag | Research actions | Description | Last changed |
|---|---|---|---|
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6666. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6666. STEP returned no word analysis block for this term. | — |
| `NO_WORD_ANALYSIS` | — | meaning field is null for H6666. STEP returned no word analysis block for this term. | — |

**Term-level dimension signal (aggregated across this term's groups):**

| Dimension | Confidence | Group count |
|---|---|---|
| 05 — Moral Character | KEYWORD_STRONG | 2 |
| 01 — Emotion — Positive | KEYWORD_WEAK | 1 |

**Related words:**

| Strongs | Transliteration | Gloss | Relationship |
|---|---|---|---|
| H6659G | tsa.doq | Zadok | — |
| H6659H | tsa.doq | Zadok | — |
| H6659I | tsa.doq | Zadok | — |
| H6659J | tsa.doq | Zadok | — |
| H6659K | tsa.doq | Zadok | — |
| H6659L | tsa.doq | Zadok | — |
| H6659M | tsa.doq | Zadok | — |
| H6662 | tsad.diq | righteous | — |
| H6663 | tsa.deq | to justify | — |
| H6664G | tse.deq | righteousness | — |
| H6664H | tse.deq | Righteousness [God] | — |
| H6665 | tsid.qah | righteousness | — |
| H6667G | tsid.qiy.ya.hu | Zedekiah | — |
| H6667H | tsid.qiy.ya.hu | Zedekiah | — |
| H6667I | tsid.qiy.ya.hu | Zedekiah | — |
| H6667J | tsid.qiy.ya.hu | Zedekiah | — |
| H6667K | tsid.qiy.ya.hu | Zedekiah | — |
| H6667L | tsid.qiy.ya.hu | Zedekiah | — |

**Verse record counts:** total=148, active=0, delete_flagged=148.

<!-- PROSE_SECTION
type: sa_s1_d3
registry: 139
version: 1
status: approved
author: claude_code
-->

## Section 4 — Verses by Group (with Dimensions and Annotations)

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:53:18Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `verse_context_group`, `wa_dimension_index`, `wa_verse_records`, `verse_context`, `mti_terms` |
| Notes | Active groups: 1. Verses within each group rendered as anchor → related → set-aside. |

### 4.G1345.1099-001 — G1345 · group `1099-001`

| Field | Value |
|---|---|
| context_description | Term names the dikaiōma — whether decree, standard, righteous act, or verdict — as the external reality that discloses, qualifies, or re-orients inner-being standing, moral orientation, and response (conformity, defiance, reception of verdict, or worship of divine righteousness revealed). |
| dimension | 05 — Moral Character |
| dimension_confidence | KEYWORD_STRONG |
| dominant_subject | — |
| manual_override | 0 |
| anchor / related / set-aside | 1 / 5 / 4 |

| Role | Reference | Translation | Span match | Text |
|---|---|---|---|---|
| **anchor** | Rev 15:4 | ESV | 1 | Rev 15:4 Who will not fear , O Lord , and glorify your name ? For you alone are holy . All nations will come and worship you , for your righteous acts have been revealed .” |
| **anchor** | Rom 5:16 | ESV | 1 | Rom 5:16 And the free gift is not like the result of that one man’s sin . For the judgment following one trespass brought condemnation , but the free gift following many trespasses brought justification . |
| related | Heb 9:1 | ESV | 1 | Heb 9:1 Now even the first covenant had regulations for worship and an earthly place of holiness . |
| related | Heb 9:10 | ESV | 1 | Heb 9:10 but deal only with food and drink and various washings , regulations for the body imposed until the time of reformation . |
| related | Rev 19:8 | ESV | 1 | Rev 19:8 it was granted her to clothe herself with fine linen , bright and pure ”— for the fine linen is the righteous deeds of the saints . |
| related | Rom 1:32 | ESV | 1 | Rom 1:32 Though they know God’s righteous decree that those who practice such things deserve to die , they not only do them but give approval to those who practice them. |
| related | Rom 2:26 | ESV | 1 | Rom 2:26 So , if a man who is uncircumcised keeps the precepts of the law , will not his uncircumcision be regarded as circumcision ? |
| related | Rom 5:18 | ESV | 1 | Rom 5:18 Therefore , as one trespass led to condemnation for all men , so one act of righteousness leads to justification and life for all men . |
| related | Rom 8:4 | ESV | 1 | Rom 8:4 in order that the righteous requirement of the law might be fulfilled in us , who walk not according to the flesh but according to the Spirit . |
| related | Luk 1:6 | ESV | 1 | Luk 1:6 And they were both righteous before God , walking blamelessly in all the commandments and statutes of the Lord . |

<!-- PROSE_SECTION
type: sa_s1_d5
registry: 139
version: 1
status: approved
author: claude_code
-->

## Section 5 — Research Pointers, Findings, and Cross-Registry Links

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:53:18Z |
| Source stage | `session_a` (mechanical extract) |
| Author | `claude_code` |
| Source tables | `wa_session_b_findings`, `wa_finding_catalogue_links`, `wa_obs_question_catalogue`, `wa_session_research_flags`, `wa_term_phase2_flags`, `wa_cross_registry_links`, `wa_crosslink_type` |
| Notes | Four sub-blocks: 5a SB findings + SB pointers · 5b SD pointers · 5c cross-registry links · 5d correlation summary. |

### 5a — Session B Pointers and Findings

_No Session B findings recorded for this registry._

**Phase 2 term advisories:**

| Strongs | Flag | Source | Description |
|---|---|---|---|
| G1345 | `—` | bulk_patch | — |
| H4941G | `—` | bulk_patch | — |
| H4941G | `SPAN_RESOLUTION_CONFLICT` | bulk_patch | — |

### 5b — Session D Pointers (cross-registry synthesis queue)

_No Session D pointers for this registry._

### 5c — Cross-Registry Links

_No cross-registry links recorded for this registry._

### 5d — Correlation signals

_Full programme-wide correlation data is not inlined here — see `scripts/build_correlation_extract.py` output. This section reserved for a brief registry-specific summary once correlations are integrated._

<!-- PROSE_SECTION
type: sa_s1_d6
registry: 139
version: 1
status: approved
author: claude_code
-->

## Section 6 — Analytic Questions (Catalogue + Registry Extensions)

**Section meta**

| Aspect | Value |
|---|---|
| Generated | 2026-05-02T05:53:18Z |
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

