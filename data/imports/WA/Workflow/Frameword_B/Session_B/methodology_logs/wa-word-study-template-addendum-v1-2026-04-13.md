# Word Study Template — Database Field Mapping Addendum
**File:** wa-word-study-template-addendum-v1-2026-04-13.md  
**Date:** 2026-04-13  
**Purpose:** Maps each database table and field to the section of the word study where its substance primarily appears. This addendum governs how analytical data from the database is translated into prose — and confirms that every database field has a home in the document.*

---

## How to read this addendum

Each database table is listed with its fields. For each field, the primary section where its substance appears in the word study is noted, along with a brief statement of how it is used. Where a field's substance spans more than one section, the primary and secondary sections are both noted.

The labels S1–S6 refer to the six word study sections.

---

## word_registry

| Field | Section | How it is used in the prose |
|---|---|---|
| `word` | S1 | The word being studied — appears in the title and throughout |
| `description` | S1, S2 | The programme's definition of the word — primary conceptual anchor for Sections 1 and 2 |
| `dimensions` | S2 | The dimension(s) assigned to the registry — named in prose as the kind of inner-being territory the word occupies |
| `cluster_assignment` | S6 | Informs which adjacent characteristics are in the same cluster — shapes the connections section |
| `sb_classification` | S2 | The spirit-soul-body classification — states where in the inner-being structure the characteristic primarily operates |
| `sb_classification_reasoning` | S2 | The reasoning behind the classification — informs the description of the characteristic's source level |
| `unique_term_count` / `shared_term_count` / `term_sharing_ratio` | S5, S6 | Term count and sharing ratio — opening paragraph of Section 5; connectivity statement opening Section 6 |

---

## wa_term_inventory / mti_terms (per term)

| Field | Section | How it is used in the prose |
|---|---|---|
| `gloss` | S5 | The term's primary English gloss — used in Section 5 vocabulary description |
| `transliteration` | S5 | The term's transliteration — appears in parentheses with Strong's number in Section 5 |
| `occurrence_count` | S5 | How many times the term appears — stated in Section 5 term description |
| `testament` | S5 | Whether the term is OT only, NT only, or both — noted in Section 5 |
| `term_owner_type` (OWNER / XREF) | S5, S6 | OWNER terms are described in Section 5. XREF terms appear in Section 6 as connections — their owning registry is the connected characteristic |
| `god_as_subject` | S2, S3 | Where God is the primary actor: informs Section 2 (what the characteristic is at its source level) and Section 3 (what it produces when God acts) |
| `somatic_link` | S3 | Where a bodily dimension is documented: informs Section 3 somatic evidence |
| `causative_form_present` | S3 | Where the term has a causative stem: informs Section 3 — the characteristic can be both experienced and caused in another |
| `status_note` | S6 | Cross-registry notes naming adjacent characteristics: informs Section 6 connections |
| `evidential_status` | S2, S5 | The analytical confidence level for the term's inner-being relevance — informs how confidently the term is described |
| `short_def_mounce` | S5 | Mounce definition: primary source for term description in Section 5 |
| `meaning` / `meaning_numbered` / `meaning_parsed` | S5 | Parsed sense structure: provides the sub-senses described in Section 5 |
| `lsj_entry` / `lsj_parsed` | S5 | LSJ classical Greek entry: informs classical background note in Section 5 for Greek terms |
| `delete_flagged` | Not in prose | Deleted terms are not described in the word study |

---

## phase2_flags (wa_term_phase2_flags)

| Flag code | Section | How it is used in the prose |
|---|---|---|
| `RELATIONAL_DIRECTION` | S2, S3 | The term's meaning is inherently directed toward another — informs Section 2 description of the characteristic's directionality; Section 3 description of its movement |
| `SEMANTIC_RANGE_BREADTH` | S2, S5 | The term covers 4+ semantic domains — signals that Section 2 must describe the full range; Section 5 must cover multiple senses |
| `ESCHATOLOGICAL_USAGE` | S3, S6 | The term appears in eschatological contexts — informs Section 3 (what the characteristic points toward); Section 6 (connection to hope, restoration) |
| `THEOLOGICAL_ANCHOR` | S2, S4 | The term is a theological anchor verse term — the verse carries special weight in Section 4 |
| `SOMATIC_INNER_LINK` | S3 | The term has a documented somatic dimension — the body's involvement is described in Section 3 |
| `BODY_INNER_EXPRESSION` | S3 | The term names a bodily expression of an inner state — described in Section 3 somatic evidence |
| `CAUSATIVE_OF_INNER_STATE` | S3 | The term names something that causes an inner state — described in Section 3 as what produces or is produced by the characteristic |
| `GENERATION_RESOLUTION_PAIR` | S3, S6 | The term pairs with another that it generates or resolves — informs Section 3 dynamic and Section 6 connections |
| `MULTI_REGISTRY_ANCHOR` | S6 | The anchor verse is shared with other registries — informs Section 6 connections |

---

## mti_term_flags (authoritative flag mechanism per WA-Reference 13.3)

| Flag type | Section | How it is used in the prose |
|---|---|---|
| `GOD_AS_SUBJECT` (flag_id 1) | S2, S3 | See `god_as_subject` above — this is the authoritative record. Informs what the characteristic is at its source level (S2) and what it produces when God acts (S3) |
| `THEOLOGICAL_ANCHOR` (flag_id 2) | S2, S4 | The term anchors a theologically significant group — the anchor verse receives particular attention in Section 4 |
| `SOMATIC_INNER_LINK` (flag_id 3) | S3 | See `somatic_link` above — authoritative record. Informs Section 3 somatic evidence |
| `BODY_INNER_EXPRESSION` (flag_id 4) | S3 | The term names a bodily expression — described in Section 3 |

---

## verse_context_groups

| Field | Section | How it is used in the prose |
|---|---|---|
| `context_description` | S2, S3 | The semantic description of how the word is used in this group — the full set of context descriptions is the primary source for Sections 2 and 3. Descriptions naming what the characteristic *is* inform S2. Descriptions naming what it *does* or *produces* inform S3 |
| `classification_counts` (anchor / related / set_aside) | S4, S5 | Anchor count informs Section 4 scope. Total verse count informs Section 5 occurrence notes |
| `is_anchor` on verse_context records | S4 | Anchor verses are the primary evidence in Section 4 |
| `verse_text` on anchor records | S4 | The verse text quoted in Section 4 |

---

## dimension_index

| Field | Section | How it is used in the prose |
|---|---|---|
| `dimension` | S2 | The dimension assigned to each group — informs Section 2 description of the characteristic's inner-being territory |
| `dominant_subject` (HUMAN / GOD / BOTH) | S2, S3 | Where GOD is dominant subject: informs Section 2 (what the characteristic is at its source) and Section 3 (what it does when God is the actor). Where HUMAN: informs Section 2 and S3 as the human experience of the characteristic |
| `context_description` | S2, S3 | Mirrors verse_context_group description — see above |

---

## wa_term_related_words

| Field | Section | How it is used in the prose |
|---|---|---|
| Related word glosses (filtered — proper names excluded) | S2, S5 | The related word family: informs Section 2 (adjacent concepts that define the characteristic by contrast or proximity) and Section 5 (vocabulary family description, negative semantic twins, associated terms) |

---

## root_family

| Field | Section | How it is used in the prose |
|---|---|---|
| `root_code` | S5, S6 | The root connecting related terms — informs Section 5 synthesis paragraph; informs Section 6 root-family connections to other registries |
| `root_gloss` | S5 | The root's meaning — informs Section 5 synthesis paragraph |

---

## session_research_flags (SD_POINTER records)

| Field | Section | How it is used in the prose |
|---|---|---|
| `description` of SD_POINTER flags with `session_target = C` | S2–S6 | Any flag specifically targeting Session C contains a researcher or analytical note that should inform the relevant section as indicated in the flag |
| SD_POINTER flags generally | S6 | The cross-registry questions captured as SD pointers inform the open questions in Section 6 connections — they are the analytical source for the questions raised there |

---

## correlations block

| Signal | Section | How it is used in the prose |
|---|---|---|
| `xref_sharing` | S6 | Shared terms with other registries: confirms formal connections in Section 6. The shared terms are named. |
| `verse_cooccurrence` | S6 | Shared verse co-occurrence with other registries: confirms that characteristics travel together in the biblical text — named in Section 6 |
| `dimension_overlap` | S6 | Shared dimension categories: confirms that two characteristics occupy the same inner-being territory — informs Section 6 nature characterisation |
| `root_families` | S5, S6 | Shared root families: informs Section 5 synthesis and Section 6 connections |
| `shared_anchor_verses` | S4, S6 | Specific verses shared as anchors with other registries: may warrant a note in Section 4 annotation; confirmed in Section 6 as formal connections |

---

## cross_registry_links

| Field | Section | How it is used in the prose |
|---|---|---|
| `linked_word` / `linked_registry_id` | S6 | The connected characteristic — named in Section 6 |
| `connection_type_id` | S6 | The type of connection — informs the nature characterisation in Section 6 |
| `connecting_term` | S6 | The specific term creating the link — named in Section 6 |
| `note` | S6 | The analytical note on the connection — informs the key question in Section 6 |

---

## session_b (findings)

| Field | Section | How it is used in the prose |
|---|---|---|
| `finding` text (DIMENSION_REVIEW type) | S2, S3, S4 | Dimension review findings that name analytical observations about groups — inform the relevant section based on whether the finding concerns what the characteristic is (S2), what it does (S3), or a specific verse (S4) |
| Other finding types | Relevant section | Each finding is used in the section corresponding to its analytical content |

---

*This addendum is a working reference for Session C production. It does not replace the Session C Instruction — it supplements it by making the database-to-prose mapping explicit.*

*wa-word-study-template-addendum-v1-2026-04-13.md | 2026-04-13*

