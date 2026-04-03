**Framework B — Soul Word Analysis Programme**

**Reference Document**

Controlled Vocabulary | Naming Conventions | Schema

Version 5.3 | March 2026 | Schema v3.8.0 | Referenced by all instruction documents

| **Document** | **Value** |
| --- | --- |
| Filename | WA-Reference-v5.3-20260329.md |
| Supersedes | WA-Reference-v5.2-20260329.md |
| Purpose | Single authoritative source for all controlled vocabulary, file naming, and schema reference |
| Usage | Referenced by all v5 instruction documents. Do not duplicate these values in other documents — always refer here. |

**Change Control Note — v5.3**

| **Change** | **Detail** |
| --- | --- |
| Section 1.1 | Added Verse Context batch file scope tokens: `vcb-extract` and `vcb-patch` |
| Section 1.1 | Added pool analysis dataset scope token: `pool-analysis` |
| Section 1.3 | Added WA-VerseContext-Instruction and WA-VerseContext-SetupInstruction to instruction document list |
| Section 1.4 | Added patch ID formats for VERSECONTEXT, VCGROUP, VCVERSE patch types |
| Section 3 | Added `Verse Context Reset` status value to session_b_status vocabulary |
| Section 3a | New section: `word_registry.verse_context_status` controlled vocabulary |
| Section 12 | Added VERSECONTEXT, VCGROUP, VCVERSE to patch type vocabulary |
| Section 12 | Renamed to Patch Index — single navigation point for all patch types |
| Section 13.1 | word_registry: anchor_verses removed (M17); source_category renamed to dimensions (M17); verse_context_status added (M18) |
| Section 13.11 | New: verse_context_group table |
| Section 13.12 | New: verse_context table |
| Section 16 | New: Anchor verse definition |
| Section 17 | New: XREF architecture reference |
| Footer | Schema version updated to 3.8.0 |

**Change Control Note — v5.2**

| **Change** | **Detail** |
| --- | --- |
| Section 13.1 | word_registry: added unique_term_count, shared_term_count, term_sharing_ratio |
| Section 13.3 | wa_term_inventory: added term_owner_type (OWNER/XREF) |
| Section 13.6 | wa_verse_records: added mti_term_id (direct FK to mti_terms), target_word, span_strong_match |
| Section 13.11 | New: wa_quality_flag_types — CONCRETE_PHYSICAL flag documented |
| Section 15 | New: Term ownership and housekeeping reference |

---

# **1. File Naming Conventions**

## **1.1 Word-Level Files**

All word-level files follow the pattern: wa-{nnn}-{word}-{scope}-{YYYYMMDD}.{ext}

| **Scope token** | **File type and example** |
| --- | --- |
| analysis | Session B narrative — wa-097-joy-analysis-20260327.docx |
| extract | Word JSON export from database — wa-097-joy-extract-20260327.json |
| json | Session B structured JSON — wa-097-joy-json-20260327.json |
| patch | Patch file for Claude Code — wa-097-joy-patch-20260327.json |
| final | Final cross-table registry extract — wa-097-joy-final-20260327.json |
| sdpointers | Session D pointers file — wa-097-joy-sdpointers-20260327.json |

⚠ The `final` and `sdpointers` files are produced after the analysis completion patch has been applied and confirmed. They are not produced during the patch cycle — they are post-patch outputs.

**Verse Context batch files** follow a separate naming pattern: wa-vcb-{batch_id}-{scope}-{YYYYMMDD}.json

| **Scope token** | **File type and example** |
| --- | --- |
| vcb-extract | Verse Context batch JSON input — wa-vcb-001-extract-20260329.json |
| vcb-patch | Verse Context batch patch output — wa-vcb-001-patch-20260329.json |

**Pool analysis dataset** (Session B Analysis input for pool/cluster batches):

| **Scope token** | **File type and example** |
| --- | --- |
| pool-analysis | Pool analysis dataset — wa-pool-c07-anger-pair-analysis-20260329.json |

## **1.2 Programme-Level Files**

| **Pattern** | **File type and example** |
| --- | --- |
| wa-clusters-{date}.json | Clustering run output — wa-clusters-20260327.json |
| wa-{cluster}-sessiond-{date}.json | Session D discovery JSON — wa-c01-sessiond-20260327.json |
| wa-programme-review-{date}.docx | Periodic registry review — wa-programme-review-20260327.docx |

## **1.3 Instruction Documents**

| **Pattern** | **Document** |
| --- | --- |
| WA-VerseContext-Instruction-v{n}-{date}.md | Verse Context stage — integrated Claude AI + Claude Code |
| WA-VerseContext-SetupInstruction-v{n}-{date}.md | Verse Context setup — Claude Code only |
| WA-SessionB-Analysis-Instruction-v{n}-{date}.docx | Session B analysis instruction |
| WA-SessionB-DataPrep-Instruction-v{n}-{date}.docx | Session B data preparation instruction |
| WA-SessionB-Extraction-Instruction-v{n}-{date}.docx | Session B extraction instruction |
| WA-Registry-Management-Guide-v{n}-{date}.md | Registry management guide |
| WA-Implementation-Instruction-v{n}-{date}.docx | Implementation — what needs to happen next |
| WA-Reference-v{n}-{date}.md | This document |
| WA-SessionD-Orientation-v{n}-{date}.docx | Session D orientation |

## **1.4 Patch ID Convention**

Standard word-level patches:
```
PATCH-{YYYYMMDD}-{registry_no}-{type}-V{n}
Examples:
  PATCH-20260327-097-PREANALYSIS-V1
  PATCH-20260327-097-ANALYSIS-V1
```

Verse Context patches:
```
PATCH-{YYYYMMDD}-VCB{batch_id}-VERSECONTEXT-V{n}   (batch)
PATCH-{YYYYMMDD}-VCGROUP{group_id}-V{n}              (targeted group)
PATCH-{YYYYMMDD}-VCVERSE{verse_record_id}-V{n}       (targeted verse)
```

---

# **2. Controlled Vocabulary — mti_terms.status**

Source: bible_research.db schema v3.8.0. Use exact values including correct case.

| **Value** | **When to use** |
| --- | --- |
| NULL | Unclassified — no decision made yet |
| extracted | Term is genuine vocabulary for this registry — include in analysis |
| extracted_thin | Term is relevant but data is thin — include with caution note |
| extracted_theological_anchor | Term is a primary theological anchor for this registry |
| delete | Confirmed bleed, peripheral, or non-registry vocabulary |
| candidate_delete | Likely bleed but not yet confirmed — flag for researcher decision |
| excluded | Excluded from programme scope — not the same as delete |
| xref_{word} | Belongs primarily to another registry — e.g. xref_anger, xref_shame |
| phase2_enrichment | Needs deeper research before classification |

---

# **3. Controlled Vocabulary — word_registry.session_b_status**

| **Value** | **Meaning** |
| --- | --- |
| NULL (absent) | Phase 1 excluded or not yet started |
| Verse Context Reset | Prior Session B work exists but has been superseded — registry must reprocess through Verse Context and pool-based Session B |
| Ready for Analysis | Verse Context complete — term inventory classified and clean — ready for Session B DataPrep |
| Pre-Analysis Complete | Pre-analysis patch applied — term classifications in database |
| Analysis Complete | Session B narrative complete — analysis patch applied |
| Session B Complete | Full Session B cycle done — narrative, JSON, patches, final extract, and sdpointers all complete |

⚠ `Ready for Analysis` is now only reachable after `verse_context_status = Complete`. DataPrep must not begin unless both conditions are met.

# **3a. Controlled Vocabulary — word_registry.verse_context_status**

Tracks Verse Context completion independently of session_b_status. Operates at registry level — set by Claude Code based on OWNER term completion.

| **Value** | **Meaning** |
| --- | --- |
| NULL | Phase 1 excluded or zero-term registry — outside Verse Context scope |
| In Progress | Verse Context work has begun or is pending for this registry |
| Complete | All OWNER terms with verses have verse_context records — registry may proceed to Session B DataPrep |

---

# **4. Controlled Vocabulary — word_registry Fields**

## **4.1 phase1_status**

| Complete │ Excluded │ In Progress |
| --- |

## **4.2 source_list**

| High Confidence │ Low Confidence / Inferred │ Missing Inner Being Words │ Programme Addition |
| --- |

## **4.3 dimensions**

Column renamed from `source_category` in migration M17 (2026-03-29).

`dimensions` is a comma-delimited multi-value field on `word_registry`. It is derived from Session B dimensional analysis — not pre-assigned at programme intake. A word may carry multiple dimension values reflecting its analytical profile across the corpus.

Valid dimension values:

| Affective/Emotional │ Anthropological/Structural │ Character/Disposition │ Cognitive/Mind │ Identity/Selfhood │ Inner Life │ Moral/Conscience │ Relational/Social │ Sin & Vice │ Spiritual/God-ward │ Volitional/Capacity │ Volitional/Will │ Theological/Divine-Human │ Somatic/Embodied |
| --- |

## **4.4 origin**

| original_list │ programme_addition |
| --- |

## **4.5 Dimensional Weight Vocabulary**

Used in the `dimensional_profile` block of the final registry extract (Section 14.1).

| **Value** | **Meaning** |
| --- | --- |
| PRIMARY | This dimension is the dominant analytical focus of the registry |
| SECONDARY | Substantially present and analytically significant, but not primary |
| PERIPHERAL | Present but limited or incidental corpus engagement |

---

# **5. Controlled Vocabulary — wa_session_research_flags**

## **5.1 flag_code — Known Valid Values**

| CANDIDATE_REGISTRY_WORD │ PH2_BOUNDARY_QUESTION │ PH2_CROSS_REF_ENRICHMENT │ PH2_CROSS_REGISTRY_REQUIRED │ PH2_DATA_ERROR │ PH2_DATA_QUALITY │ PH2_DATA_SPLIT_REQUIRED │ PH2_ESCHATOLOGICAL_STUDY_REQUIRED │ PH2_EXEGETICAL_STUDY_REQUIRED │ PH2_THEOLOGICAL_DEPTH_REQUIRED │ PH2_VOLUME_LIMITATION │ VOLUME_LIMITATION │ SB_FINDING │ SB_DIMENSION │ SB_INNER_BEING │ SD_POINTER │ SD_CLUSTER |
| --- |

## **5.2 priority**

| HIGH │ MEDIUM │ LOW   Default: MEDIUM |
| --- |

## **5.3 session_target**

| B │ C │ D   Default: D |
| --- |

## **5.4 flag_label Convention**

| PH2-{registry_no}-{3-digit-sequence}   Example: PH2-097-001   Must be unique across all records. |
| --- |

---

# **6. Controlled Vocabulary — wa_term_phase2_flags.flag_code**

| GOD_AS_SUBJECT │ CAUSATIVE_OF_INNER_STATE │ SOMATIC_INNER_LINK │ BODY_INNER_EXPRESSION │ NT_FACULTY_NAMING │ GENERATION_RESOLUTION_PAIR │ CROSS_PART_ROOT │ THIN_DATA │ SMALL_VERSE_SAMPLE │ DUPLICATE_RESOLVED │ NO_WORD_ANALYSIS │ CONSOLIDATION_CANDIDATE │ THEOLOGICAL_ANCHOR │ SOMATIC_EXPRESSION │ HIGH_FREQUENCY_ANCHOR │ SEMANTIC_RANGE_BREADTH │ MULTI_REGISTRY_ANCHOR │ DIVINE_HUMAN_PARALLEL │ ESCHATOLOGICAL_USAGE │ WISDOM_LITERATURE_CONCENTRATION │ METAPHOR_ROOT │ RELATIONAL_DIRECTION │ VOLITIONAL_COMPONENT │ CROSS_TESTAMENT_SHIFT │ ARAMAIC_FORM |
| --- |

---

# **7. Controlled Vocabulary — wa_crosslink_type.type_code**

| SHARED_TERM │ SEMANTIC_OVERLAP │ SHARED_ROOT │ SHARED_VERSE │ THEOLOGICAL │ CO_OCCURRENCE │ SEMANTIC_OPPOSITION │ SISTER_REGISTRY │ OVERLAPPING_DOMAIN │ CAUSATIVE_CHAIN │ THEMATIC_LINK |
| --- |

---

# **8. Controlled Vocabulary — wa_data_quality_flags.flag_code**

| HIGH_FREQUENCY_ANCHOR │ NO_VERSES │ NO_WORD_ANALYSIS │ PROSE_ONLY_MEANING │ SMALL_VERSE_SAMPLE │ SPAN_FILTER_APPLIED │ SPAN_RESOLUTION_CONFLICT │ THIN_DATA │ CONCRETE_PHYSICAL |
| --- |

---

# **9. Controlled Vocabulary — wa_term_inventory**

## **9.1 language**

| Hebrew │ Greek |
| --- |

## **9.2 testament**

| OT │ NT |
| --- |

## **9.3 term_owner_type**

| OWNER │ XREF |
| --- |

OWNER — canonical home for this Strong's number. Verses active. Processed by Verse Context.
XREF — cross-reference copy in another registry. Verses delete_flagged. Verse context derived from OWNER.

---

# **10. Evidential Status Vocabulary**

| **Value** | **Meaning** |
| --- | --- |
| confirmed | Clear inner-being vocabulary with direct verse evidence |
| plausible | Relevant but evidence is indirect or interpretively dependent |
| uncertain | Genuine uncertainty about inner-being connection — retain with note |
| instrumental | Acts on the inner being from outside — not itself an inner-being characteristic |
| relational_only | Operates only in relational/social contexts — no direct inner-being referent |

---

# **11. Session D Observation Types**

Used in session_d_observations.observation_type:

| term_co_occurrence │ verse_cluster │ volume_reliability │ scope_boundary |
| --- |

Used in sdpointers file pointer_type:

| term_co_occurrence │ verse_overlap │ evidential_uncertainty │ scope_boundary │ data_quality_impact │ structural_observation |
| --- |

Used in sdpointers file pointer_subtype:

| shared_root │ shared_gloss │ shared_domain │ divergent_usage │ shared_verse │ thematic_proximity │ thin_corpus │ boundary_term │ cross_registry_dependency │ registry_border │ cluster_border │ affects_cross_registry │ volume_concern │ classification_risk │ testament_shift │ divine_human_parallel │ conceptual_gap |
| --- |

Used in sdpointers file significance: | HIGH │ MEDIUM │ LOW |

Used in sdpointers file research_depth_required: | SURFACE │ STANDARD │ DEEP |

---

# **12. Patch Index**

Single navigation point for all patch types in the programme. For applicator rules governing each patch type, see `patch_specification.md`. For business logic, see the governing instruction document listed below.

⚠ `session_b_status` is required and non-null in `_patch_meta` for PREANALYSIS, SESSIONB, SESSIOND, CLUSTERING, and REPAIR patches. Verse Context patch types (VERSECONTEXT, VCGROUP, VCVERSE) carry `session_b_status: null` — the patch applicator must not reject these.

| **Patch type** | **Governing document** | **Valid session_b_status in _patch_meta** | **Purpose** |
| --- | --- | --- | --- |
| PREANALYSIS | WA-SessionB-DataPrep-Instruction | Pre-Analysis Complete | Term classification — extracted/delete/xref |
| SESSIONB | WA-SessionB-Extraction-Instruction | Analysis Complete / Session B Complete | Evidential status, dimensions, findings, SD pointers |
| VERSECONTEXT | WA-VerseContext-Instruction-v1 | null | Full batch: verse relevance filter, contextual grouping, anchor designation |
| VCGROUP | WA-VerseContext-Instruction-v1 | null | Targeted update to a single verse_context_group record |
| VCVERSE | WA-VerseContext-Instruction-v1 | null | Targeted update to a single verse_context record |
| SESSIOND | WA-SessionD-Orientation | null | Session D discovery and synthesis |
| CLUSTERING | WA-Implementation-Instruction | null | Cluster assignment updates |
| REPAIR | Any — per anomaly | Retain current status | Data corrections |

---

# **13. Database Schema Summary**

Source: database_schema_20260329.json — schema version 3.8.0 (M17 + M18 applied 2026-03-29).

## **13.1 word_registry — Core fields**

| id (PK) │ no │ word │ source_list │ category_hint │ phase1_status │ phase1_term_count │ phase1_verse_count │ session_b_status │ verse_context_status (new v5.3/M18) │ origin │ dimensions (renamed from source_category — M17) │ notes │ cluster_assignment │ sb_classification │ sb_classification_reasoning │ carry_forward │ unique_term_count │ shared_term_count │ term_sharing_ratio |
| --- |

Note: `anchor_verses` field removed in M17.

## **13.2 mti_terms — Term classification**

| id (PK) │ strongs_number │ transliteration │ gloss │ language │ owning_registry │ owning_registry_fk │ owning_word │ status │ status_note │ exclusion_reason │ anchor_note |
| --- |

## **13.3 wa_term_inventory — Per-file term record**

| id (PK) │ file_id │ language │ term_id │ strongs_number │ transliteration │ step_search_gloss │ word_analysis_gloss │ occurrence_count │ testament │ delete_flagged │ status_note │ evidential_status │ retention_note │ term_owner_type |
| --- |

## **13.4 wa_session_research_flags — Research flags**

| id (PK) │ registry_id │ file_id │ flag_code │ flag_label │ strongs_reference │ cross_registry_id │ priority │ session_target │ description │ session_raised │ raised_date │ resolved │ resolved_date │ resolved_note |
| --- |

## **13.5 wa_file_index — File registry**

| id (PK) │ filename │ registry_id │ word_registry_fk │ word │ part_number │ total_parts │ phase │ produced_date │ source_file │ specification │ revision_note |
| --- |

## **13.6 wa_verse_records — Verse corpus**

| id (PK) │ file_id │ term_inv_id │ reference │ verse_text │ testament │ translation │ book_id │ chapter │ verse_num │ delete_flagged │ target_word │ span_strong_match │ mti_term_id |
| --- |

## **13.7 wa_cross_registry_links — Cross-registry connections**

| id (PK) │ file_id │ linked_word │ linked_registry_id │ connection_type_id │ connecting_term │ note |
| --- |

## **13.8 wa_session_b_dimensions — Dimensional profile**

| id (PK) │ registry_id │ file_id │ relational_environment │ relational_environment_note │ spirit_soul_body │ spirit_soul_body_note │ inner_operations │ inner_operations_note │ being │ being_note │ raised_date │ session_b_instruction |
| --- |

## **13.9 wa_session_b_findings — Key findings**

| id (PK) │ finding_id │ registry_id │ file_id │ finding_type │ finding │ anchor_verses │ raised_date │ session_b_instruction |
| --- |

## **13.10 Session D Tables**

| session_d_runs │ session_d_verse_links │ session_d_term_links │ session_d_observations |
| --- |

## **13.11 verse_context_group (new M18)**

| id (PK) │ mti_term_id (FK→mti_terms.id) │ group_code │ context_description │ notes │ delete_flagged |
| --- |

One row per contextual meaning group per term. `group_code` format: `{mti_term_id}-{3-digit-serial}`. Never used as a join key — integer id only for joins.

## **13.12 verse_context (new M18)**

| id (PK) │ verse_record_id (FK→wa_verse_records.id) │ mti_term_id (FK→mti_terms.id) │ group_id (FK→verse_context_group.id) │ is_anchor │ is_relevant │ is_related │ notes │ delete_flagged |
| --- |

UNIQUE on (verse_record_id, mti_term_id, group_id). One row per verse per term per group. See Section 16 for anchor verse definition.

---

# **14. Post-Patch Output File Structures**

Governed by WA-SessionB-Extraction-Instruction-v5.2. See that document for production sequence.

## **14.1 Final Registry Extract — wa-{nnn}-{word}-final-{date}.json**
## **14.2 Session D Pointers — wa-{nnn}-{word}-sdpointers-{date}.json**

Templates unchanged from v5.2. See v5.2 for full JSON templates.

---

# **15. Term Ownership and Housekeeping**

## **15.1 term_owner_type**

| OWNER | Canonical home for this Strong's number. Verses active. Processed by Verse Context. |
| XREF | Cross-reference copy. Verses delete_flagged. Verse context derived from OWNER classification. |

## **15.2 Term Sharing Fields on word_registry**

| unique_term_count | OWNER terms whose Strong's number appears only in this registry |
| shared_term_count | OWNER terms whose Strong's number also appears in other registries |
| term_sharing_ratio | shared / (unique + shared). 0.0 = all unique. 1.0 = all shared. |

## **15.3 mti_term_id on wa_verse_records**

Direct FK to mti_terms.id — one-hop path from verse to master term index.

## **15.4 CONCRETE_PHYSICAL Quality Flag**

Flagged but not excluded. Verse analysis may reveal inner-being usage.

## **15.5 Housekeeping Rules (delete_flagged)**

Records with delete_flagged = 1 excluded from all standard queries and exports. No physical deletion.

---

# **16. Anchor Verse Definition**

An anchor verse is the programme's canonical reference verse for a specific contextual meaning group of a term (`verse_context_group`). It is the verse that most clearly and economically demonstrates the inner-being engagement of the term in that group.

**Dual purpose:**
1. **Efficiency instrument** — Session B Analysis reads anchor verses rather than the full verse corpus
2. **Citation instrument** — anchor verses appear in Session B narratives and Session D synthesis as the evidential foundation for claims about the term

**Minimum requirement:** every term must have at least one active anchor (`is_anchor = 1, delete_flagged = 0`) across all its groups before Session B Analysis may proceed.

**Selection criteria:** unambiguous inner-being function; stands alone without requiring surrounding context; 1–2 per group.

---

# **17. XREF Architecture**

`mti_terms` holds one record per Strong's number — programme-wide, registry-independent.

`wa_term_inventory` holds one record per Strong's number per registry. Each is classified OWNER or XREF:
- **OWNER** — primary analytical home. Verses active. Verse Context processes OWNER terms only.
- **XREF** — cross-reference copy. Verses delete_flagged. Verse context is derived from OWNER classification — the same term has the same contextual meaning regardless of which registry views it.

**Consequence for Session B:** words sharing XREF terms are analysed simultaneously as a pool/cluster batch. XREF terms' contextual profiles (group descriptions and anchor references from the OWNER registry) are included in the pool analysis dataset. Full anchor verse text for XREF terms is available by querying the OWNER registry dataset.

**Current scale:** 5,518 OWNER terms, 1,470 XREF terms, 133,353 active verses (OWNER only).

---

*WA-Reference-v5.3 | 20260329 | Schema v3.8.0 | Supersedes WA-Reference-v5.2-20260329.md*
