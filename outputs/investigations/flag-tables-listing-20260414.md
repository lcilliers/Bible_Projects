# Flag Tables Listing

> Extracted 2026-04-14
> All flag reference tables and in-use flag codes across the database

---

## 1. phase2_flag_types (25 rows) — Phase 2 / Session B analytical flags

Reference table defining analytical flag codes raised by Claude AI during Session B work. Used by `wa_term_phase2_flags` (per-inventory) and `mti_term_flags` (per-MTI-term).

| id | flag_code | description |
|---:|-----------|-------------|
| 1 | GOD_AS_SUBJECT | God experiences, enacts, or is the direct subject of this inner state |
| 2 | CAUSATIVE_OF_INNER_STATE | Term has an explicit causative grammatical form: Hiphil or Piel (Hebrew) |
| 3 | SOMATIC_INNER_LINK | Meaning block or verses connect this inner state to a specific bodily part |
| 4 | BODY_INNER_EXPRESSION | Inner state manifests through visible outward physical behaviour |
| 5 | NT_FACULTY_NAMING | Greek term directly names an inner faculty (kardia, pneuma, psuche, nous) |
| 6 | GENERATION_RESOLUTION_PAIR | Hebrew-Aramaic or Hebrew-Greek pair resolving to the same referent |
| 7 | CROSS_PART_ROOT | Term shares a root family with terms in another part of the registry |
| 8 | THIN_DATA | Fewer than 5 verse records or very low occurrence count |
| 9 | SMALL_VERSE_SAMPLE | Verse count less than 20% of stated occurrence count |
| 10 | DUPLICATE_RESOLVED | Term appeared as a duplicate entry in the source data; resolved |
| 11 | NO_WORD_ANALYSIS | No STEP word analysis data available for this term |
| 12 | CONSOLIDATION_CANDIDATE | Term likely to merge with a closely related entry during Session B |
| 13 | THEOLOGICAL_ANCHOR | Framework A/B intersection term; Session B analysis deferred |
| 14 | SOMATIC_EXPRESSION | Term expresses inner state through somatic or body-language patterns |
| 15 | HIGH_FREQUENCY_ANCHOR | Term occurs 200+ times; primary anchor for semantic field |
| 16 | SEMANTIC_RANGE_BREADTH | Term covers 4+ distinct semantic domains |
| 17 | MULTI_REGISTRY_ANCHOR | Term appears as cross-reference in 3+ registries |
| 18 | DIVINE_HUMAN_PARALLEL | God and humans as subject in structurally parallel contexts |
| 19 | ESCHATOLOGICAL_USAGE | Term predominant in eschatological or apocalyptic passages |
| 20 | WISDOM_LITERATURE_CONCENTRATION | Term predominant in Proverbs, Job, or Ecclesiastes |
| 21 | METAPHOR_ROOT | Term meaning grounded in concrete physical/sensory metaphor |
| 22 | RELATIONAL_DIRECTION | Term inherently directed toward another person, group, or God |
| 23 | VOLITIONAL_COMPONENT | Term carries a dimension of will, choice, or intention |
| 24 | CROSS_TESTAMENT_SHIFT | Meaningful semantic shift between OT and NT usage |
| 25 | ARAMAIC_FORM | Aramaic form of a Hebrew root (Daniel, Ezra, post-exilic) |

---

## 2. wa_quality_flag_types (14 rows) — Engine-derived and session flags

Reference table for engine-computed quality flags and session-scoped structural flags. Used by `wa_data_quality_flags`.

### Group: DATA_COVERAGE (engine-derived, reset on every audit_word run)

| id | flag_code | description |
|---:|-----------|-------------|
| 1 | NO_VERSES | No verse records found for this term in the source data |
| 2 | THIN_DATA | Fewer verse occurrences than expected; analysis may be limited |
| 3 | SMALL_VERSE_SAMPLE | Only a partial sample of available verses was captured |
| 4 | NO_WORD_ANALYSIS | No word-level analysis is available for this term |
| 23 | SPAN_RESOLUTION_CONFLICT | Queried Strong's not found in any verse span after suffix resolution |
| 24 | SPAN_FILTER_APPLIED | One or more verse records were discarded by span filter |
| 36 | HIGH_FREQUENCY_ANCHOR | (no description) |
| 47 | PROSE_ONLY_MEANING | Meaning stored as single prose block — STEP medium_def content |
| 310 | CONCRETE_PHYSICAL | Term denotes a concrete physical object, substance, or spatial reference |

### Group: SESSION_B

| id | flag_code | description |
|---:|-----------|-------------|
| 145 | SB_FINDING | Session B key finding from key_findings array in Session B JSON |
| 146 | SB_DIMENSION | Session B dimensional profile record — one per active dimension |
| 147 | SB_INNER_BEING | Session B inner being standing classification |

### Group: SESSION_D

| id | flag_code | description |
|---:|-----------|-------------|
| 148 | SD_POINTER | Session D pointer — cross-registry structural observation from Session B |
| 149 | SD_CLUSTER | Session D cluster maturity flag — researcher-triggered |

---

## 3. wa_session_research_flags — Distinct flag codes in use (16 codes)

These are the flag codes actually used in the live `wa_session_research_flags` table. Some codes reference the `wa_quality_flag_types` reference; others were introduced ad-hoc during Session B work and do not have a reference entry.

| flag_code | Count | Notes |
|-----------|------:|-------|
| SD_POINTER | 229 | Cross-registry synthesis pointer for Session D |
| PH2_VOLUME_LIMITATION | 33 | Term has low verse coverage — conclusions provisional |
| VOLUME_LIMITATION | 19 | Same as above — naming drift (no PH2_ prefix) |
| PH2_DATA_ERROR | 11 | Data quality error (homonyms, function words, extraction anomalies) |
| DIMREVIEW_SESSION_D | 8 | Dimension Review observation forwarded to Session D |
| PH2_CROSS_REGISTRY_REQUIRED | 7 | Cross-registry analysis needed before synthesis |
| PH2_CROSS_REF_ENRICHMENT | 6 | Cross-reference enrichment opportunity |
| PH2_THEOLOGICAL_DEPTH_REQUIRED | 4 | Verse/passage needs dedicated theological study |
| PH2_DATA_QUALITY | 3 | Data quality concern (root bleed, missing verses) |
| THEMATIC_LINK | 1 | Thematic connection identified during Session B |
| PH2_EXEGETICAL_STUDY_REQUIRED | 1 | Dedicated exegetical study needed |
| PH2_ESCHATOLOGICAL_STUDY_REQUIRED | 1 | Eschatological study needed |
| PH2_DATA_SPLIT_REQUIRED | 1 | Term has multiple senses requiring data split |
| PH2_BOUNDARY_QUESTION | 1 | Boundary/scope question |
| DATA_INTEGRITY | 1 | Data integrity concern |
| CANDIDATE_REGISTRY_WORD | 1 | Candidate for a new registry entry |

**Note:** Only `SD_POINTER` has a corresponding entry in `wa_quality_flag_types` (id 148). The `PH2_*` and other codes were introduced through patches without adding reference rows. This is a reference table completeness gap.

---

## 4. wa_crosslink_type (11 rows) — Cross-registry link types

Reference table for cross-registry connection classifications. Used by `wa_cross_registry_links`.

| id | type_code | description |
|---:|-----------|-------------|
| 1 | SHARED_TERM | The same Hebrew or Greek term appears in both word studies |
| 2 | SEMANTIC_OVERLAP | The two registries share overlapping meaning space |
| 3 | SHARED_ROOT | The registries share a common etymological root |
| 4 | SHARED_VERSE | The same verse references appear in both word studies |
| 5 | THEOLOGICAL | The registries are connected by a theological concept or theme |
| 6 | CO_OCCURRENCE | Terms from the two registries frequently appear together |
| 7 | SEMANTIC_OPPOSITION | The registries represent antonyms or semantic contrasts |
| 8 | SISTER_REGISTRY | Parallel registries covering closely related vocabulary |
| 9 | OVERLAPPING_DOMAIN | Registries sharing terms with overlapping semantic domains |
| 10 | CAUSATIVE_CHAIN | Causal relationship between inner states across registries |
| 11 | THEMATIC_LINK | Thematic connection identified during Session B analysis |

---

## 5. Summary of Flag Storage

| Storage table | Reference table | Purpose |
|---------------|----------------|---------|
| wa_term_phase2_flags (1,580 rows) | phase2_flag_types (25) | Per-inventory analytical flags (Claude AI) |
| mti_term_flags (54 rows) | phase2_flag_types (25) | Per-MTI-term analytical flags (Session B patches) |
| wa_data_quality_flags (22,129 rows) | wa_quality_flag_types (14) | Engine-derived per-term quality indicators |
| wa_session_research_flags (327 rows) | wa_quality_flag_types (partial) | Session research observations, SD pointers, PH2 flags |
| wa_cross_registry_links (158 rows) | wa_crosslink_type (11) | Cross-registry connections (Session A era) |
