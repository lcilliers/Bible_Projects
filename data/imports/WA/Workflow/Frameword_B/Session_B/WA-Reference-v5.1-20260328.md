**Framework B — Soul Word Analysis Programme**

**Reference Document**

Controlled Vocabulary | Naming Conventions | Schema

Version 5.1 | March 2026 | Schema v3.7.0 | Referenced by all instruction documents

| **Document** | **Value** |
| --- | --- |
| Filename | WA-Reference-v5.1-20260328.docx |
| Supersedes | WA-Reference-v5-20260327.docx |
| Purpose | Single authoritative source for all controlled vocabulary, file naming, and schema reference |
| Usage | Referenced by all v5 instruction documents. Do not duplicate these values in other documents — always refer here. |

**Change Control Note — v5.1**

| **Change** | **Detail** |
| --- | --- |
| Section 1.1 | Added two new scope tokens: `final` and `sdpointers` |
| Section 4.3 | source_category repurposed as `dimensions` — multi-value, comma-delimited, derived from Session B analysis |
| Section 4.5 | New section: dimensional weight vocabulary (PRIMARY / SECONDARY / PERIPHERAL) |
| Section 10 | Evidential status storage updated to reflect dedicated fields (schema v3.7.0) |
| Section 13 | Schema summary updated to v3.7.0 — new fields and tables added |
| Section 14 | New section: post-patch output file structures (final extract and sdpointers) |

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

## **1.2 Programme-Level Files**

| **Pattern** | **File type and example** |
| --- | --- |
| wa-clusters-{date}.json | Clustering run output — wa-clusters-20260327.json |
| wa-{cluster}-sessiond-{date}.json | Session D discovery JSON — wa-c01-sessiond-20260327.json |
| wa-programme-review-{date}.docx | Periodic registry review — wa-programme-review-20260327.docx |

## **1.3 Instruction Documents**

| **Pattern** | **Document** |
| --- | --- |
| WA-SessionB-Analysis-Instruction-v{n}-{date}.docx | Session B analysis instruction |
| WA-SessionB-DataPrep-Instruction-v{n}-{date}.docx | Session B data preparation instruction |
| WA-SessionB-Extraction-Instruction-v{n}-{date}.docx | Session B extraction instruction |
| WA-Registry-Management-Guide-v{n}-{date}.docx | Registry management guide |
| WA-Implementation-Instruction-v{n}-{date}.docx | Implementation / what needs to happen next |
| WA-Reference-v{n}-{date}.docx | This document |
| WA-SessionD-Orientation-v{n}-{date}.docx | Session D orientation |

## **1.4 Patch ID Convention**

| PATCH-{YYYYMMDD}-{registry_no}-{type}-V{n}  Examples: PATCH-20260327-097-PREANALYSIS-V1 PATCH-20260327-097-ANALYSIS-V1 PATCH-20260327-CLUSTERS-V1 |
| --- |

---

# **2. Controlled Vocabulary — mti_terms.status**

Source: bible_research.db schema v3.7.0. Use exact values including correct case.

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
| NULL (absent) | No Session B work started |
| Ready for Analysis | Data preparation complete — term inventory clean and classified |
| Pre-Analysis Complete | Pre-analysis patch applied — term classifications in database |
| Analysis Complete | Session B narrative complete — analysis patch applied |
| Session B Complete | Full Session B cycle done — narrative, JSON, patches, final extract, and sdpointers all complete |

---

# **4. Controlled Vocabulary — word_registry Fields**

## **4.1 phase1_status**

| Complete │ Excluded │ In Progress |
| --- |

## **4.2 source_list**

| High Confidence │ Low Confidence / Inferred │ Missing Inner Being Words │ Programme Addition |
| --- |

## **4.3 dimensions**

Previously named `source_category`. Repurposed in v5.1.

`dimensions` is a comma-delimited multi-value field on `word_registry`. It is derived from Session B dimensional analysis — not pre-assigned at programme intake. A word may carry multiple dimension values reflecting its analytical profile across the corpus.

Valid dimension values:

| Affective/Emotional │ Anthropological/Structural │ Character/Disposition │ Cognitive/Mind │ Identity/Selfhood │ Inner Life │ Moral/Conscience │ Relational/Social │ Sin & Vice │ Spiritual/God-ward │ Volitional/Capacity │ Volitional/Will │ Theological/Divine-Human │ Somatic/Embodied |
| --- |

⚠ This field replaces the former single-value source_category. Words are multi-dimensional; the comma-delimited format reflects this. The field is populated or updated at Session B extraction, not at registry creation. Existing single-value source_category entries remain valid until updated through Session B extraction.

## **4.4 origin**

| original_list │ programme_addition |
| --- |

## **4.5 Dimensional Weight Vocabulary**

Used in the `dimensional_profile` block of the final registry extract (Section 14.1) to indicate where analytical weight falls within a registry across the four Framework B dimensions.

| **Value** | **Meaning** |
| --- | --- |
| PRIMARY | This dimension is the dominant analytical focus of the registry. The majority of the corpus addresses this dimension directly. |
| SECONDARY | This dimension is substantially present and analytically significant, but not the primary focus. |
| PERIPHERAL | This dimension is present but the corpus engagement is limited or incidental. |

Each of the four dimensions (relational_environment, spirit_soul_body, inner_operations, being) receives one of these three values in the final registry extract. A registry may have more than one PRIMARY dimension.

---

# **5. Controlled Vocabulary — wa_session_research_flags**

## **5.1 flag_code — Known Valid Values**

Open vocabulary — new codes can be added. Known valid values from schema v3.7.0:

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

Researcher-owned flags. Use exact values:

| GOD_AS_SUBJECT │ CAUSATIVE_OF_INNER_STATE │ SOMATIC_INNER_LINK │ BODY_INNER_EXPRESSION │ NT_FACULTY_NAMING │ GENERATION_RESOLUTION_PAIR │ CROSS_PART_ROOT │ THIN_DATA │ SMALL_VERSE_SAMPLE │ DUPLICATE_RESOLVED │ NO_WORD_ANALYSIS │ CONSOLIDATION_CANDIDATE │ THEOLOGICAL_ANCHOR │ SOMATIC_EXPRESSION │ HIGH_FREQUENCY_ANCHOR │ SEMANTIC_RANGE_BREADTH │ MULTI_REGISTRY_ANCHOR │ DIVINE_HUMAN_PARALLEL │ ESCHATOLOGICAL_USAGE │ WISDOM_LITERATURE_CONCENTRATION │ METAPHOR_ROOT │ RELATIONAL_DIRECTION │ VOLITIONAL_COMPONENT │ CROSS_TESTAMENT_SHIFT │ ARAMAIC_FORM |
| --- |

---

# **7. Controlled Vocabulary — wa_crosslink_type.type_code**

UPPERCASE required:

| SHARED_TERM │ SEMANTIC_OVERLAP │ SHARED_ROOT │ SHARED_VERSE │ THEOLOGICAL │ CO_OCCURRENCE │ SEMANTIC_OPPOSITION │ SISTER_REGISTRY │ OVERLAPPING_DOMAIN │ CAUSATIVE_CHAIN │ THEMATIC_LINK |
| --- |

---

# **8. Controlled Vocabulary — wa_data_quality_flags.flag_code**

Engine-derived flags, DATA_COVERAGE group:

| HIGH_FREQUENCY_ANCHOR │ NO_VERSES │ NO_WORD_ANALYSIS │ PROSE_ONLY_MEANING │ SMALL_VERSE_SAMPLE │ SPAN_FILTER_APPLIED │ SPAN_RESOLUTION_CONFLICT │ THIN_DATA |
| --- |

---

# **9. Controlled Vocabulary — wa_term_inventory**

## **9.1 language**

| Hebrew │ Greek |
| --- |

## **9.2 testament**

| OT │ NT |
| --- |

---

# **10. Evidential Status Vocabulary**

Used in Session B JSON, final registry extract, and sdpointers file. Stored in dedicated fields `wa_term_inventory.evidential_status` and `wa_term_inventory.retention_note` (schema v3.7.0).

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

Used in session_d_observations.gate:

| automatic │ researcher_triggered |
| --- |

Used in sdpointers file pointer_type (Section 14.2):

| term_co_occurrence │ verse_overlap │ evidential_uncertainty │ scope_boundary │ data_quality_impact │ structural_observation |
| --- |

Used in sdpointers file pointer_subtype (Section 14.2):

| shared_root │ shared_gloss │ shared_domain │ divergent_usage │ shared_verse │ thematic_proximity │ thin_corpus │ boundary_term │ cross_registry_dependency │ registry_border │ cluster_border │ affects_cross_registry │ volume_concern │ classification_risk │ testament_shift │ divine_human_parallel │ conceptual_gap |
| --- |

Used in sdpointers file significance:

| HIGH │ MEDIUM │ LOW |
| --- |

Used in sdpointers file research_depth_required:

| SURFACE │ STANDARD │ DEEP |
| --- |

---

# **12. Patch Type Vocabulary**

| **patch_type value** | **Governing document** |
| --- | --- |
| PREANALYSIS | WA-SessionB-DataPrep-Instruction-v5 |
| SESSIONB | WA-SessionB-Extraction-Instruction-v5 |
| SESSIOND | WA-SessionD-Orientation-v2 (when instruction formalised) |
| CLUSTERING | WA-Implementation-Instruction-v5 |

---

# **13. Database Schema Summary**

Source: database_schema_20260328.json — schema version 3.7.0. Key tables for Session B programme work:

## **13.1 word_registry — Core fields**

| id (PK) │ no │ word │ source_list │ category_hint │ phase1_status │ phase1_term_count │ phase1_verse_count │ session_b_status │ origin │ dimensions (formerly source_category — see Section 4.3) │ notes │ anchor_verses │ cluster_assignment │ sb_classification │ sb_classification_reasoning │ carry_forward |
| --- |

## **13.2 mti_terms — Term classification**

| id (PK) │ strongs_number │ transliteration │ gloss │ language │ owning_registry │ owning_registry_fk │ owning_word │ status │ status_note │ exclusion_reason │ anchor_note |
| --- |

## **13.3 wa_term_inventory — Per-file term record**

| id (PK) │ file_id │ language │ term_id │ strongs_number │ transliteration │ step_search_gloss │ word_analysis_gloss │ occurrence_count │ testament │ delete_flagged │ status_note │ evidential_status (new v3.7.0) │ retention_note (new v3.7.0) |
| --- |

## **13.4 wa_session_research_flags — Research flags**

| id (PK) │ registry_id │ file_id │ flag_code │ flag_label │ strongs_reference │ cross_registry_id │ priority │ session_target │ description │ session_raised │ raised_date │ resolved │ resolved_date │ resolved_note |
| --- |

## **13.5 wa_file_index — File registry**

| id (PK) │ filename │ registry_id │ word_registry_fk │ word │ part_number │ total_parts │ phase │ produced_date │ source_file │ specification │ revision_note |
| --- |

## **13.6 wa_verse_records — Verse corpus**

| id (PK) │ file_id │ term_inv_id │ reference │ verse_text │ testament │ translation │ book_id │ chapter │ verse_num │ delete_flagged |
| --- |

## **13.7 wa_cross_registry_links — Cross-registry connections**

| id (PK) │ file_id │ linked_word │ linked_registry_id │ connection_type_id │ connecting_term │ note |
| --- |

## **13.8 wa_session_b_dimensions — Dimensional profile (new v3.7.0)**

| id (PK) │ registry_id │ file_id │ relational_environment │ relational_environment_note │ spirit_soul_body │ spirit_soul_body_note │ inner_operations │ inner_operations_note │ being │ being_note │ raised_date │ session_b_instruction |
| --- |

## **13.9 wa_session_b_findings — Key findings (new v3.7.0)**

| id (PK) │ finding_id │ registry_id │ file_id │ finding_type │ finding │ anchor_verses │ raised_date │ session_b_instruction |
| --- |

## **13.10 Session D Tables (new v3.7.0)**

| session_d_runs │ session_d_verse_links │ session_d_term_links │ session_d_observations   See WA-Implementation-Instruction-v5 Task 3 for full schema. |
| --- |

---

# **14. Post-Patch Output File Structures**

These two files are produced after the analysis completion patch has been applied and confirmed by Claude Code. They are governed by WA-SessionB-Extraction-Instruction-v5.2. See that document for the production sequence and instructions.

## **14.1 Final Registry Extract — wa-{nnn}-{word}-final-{date}.json**

Purpose: Self-contained cross-table extract of the completed registry. Serves as input to Session D synthesis and to the future programme-level categorisation run. Does not include raw verse text — verse corpus remains in the database.

```json
{
  "meta": {
    "json_template_version": "final_v1.0",
    "json_filename": "wa-{nnn}-{word}-final-{YYYYMMDD}.json",
    "registry_id": "{nnn}",
    "word": "{word}",
    "cluster_assignment": "{cluster_id}",
    "produced_date": "{YYYYMMDD}",
    "session_b_instruction_version": "WA-SessionB-Analysis-Instruction-v5",
    "extraction_instruction_version": "WA-SessionB-Extraction-Instruction-v5.2"
  },
  "registry_summary": {
    "word_label": "{word}",
    "dimensions": "{comma-delimited dimension values — see Section 4.3}",
    "cluster_assignment": "{cluster_id}",
    "phase1_term_count": 0,
    "phase1_verse_count": 0,
    "active_term_count": 0,
    "confirmed_count": 0,
    "plausible_count": 0,
    "uncertain_count": 0,
    "session_b_status": "Analysis Complete",
    "sb_classification": "{confirmed_characteristic/plausible/uncertain/instrumental/relational_only}",
    "carry_forward": true,
    "dimensional_profile": {
      "relational_environment": { "weight": "{PRIMARY/SECONDARY/PERIPHERAL}", "note": "{brief note}" },
      "spirit_soul_body":        { "weight": "{PRIMARY/SECONDARY/PERIPHERAL}", "note": "{brief note}" },
      "inner_operations":        { "weight": "{PRIMARY/SECONDARY/PERIPHERAL}", "note": "{brief note}" },
      "being":                   { "weight": "{PRIMARY/SECONDARY/PERIPHERAL}", "note": "{brief note}" }
    },
    "evidential_weight": {
      "confirmed_verse_count": 0,
      "plausible_verse_count": 0,
      "uncertain_verse_count": 0,
      "dominant_terms": [
        { "strongs_id": "{H/Gnnnn}", "transliteration": "{transliteration}",
          "verse_count": 0, "evidential_status": "{status}" }
      ]
    }
  },
  "terms": [
    {
      "strongs_id": "{H/Gnnnn}",
      "transliteration": "{transliteration}",
      "language": "{Hebrew or Greek}",
      "mti_status": "{status}",
      "verse_count": 0,
      "evidential_status": "{status}",
      "retention_note": null
    }
  ],
  "dimensions": {
    "relational_environment": { "present": false, "note": null },
    "spirit_soul_body":        { "present": false, "note": null },
    "inner_operations":        { "present": false, "note": null },
    "being":                   { "present": false, "note": null }
  },
  "inner_being_standing": {
    "classification": "{confirmed_characteristic/plausible/uncertain/instrumental/relational_only}",
    "reasoning": null,
    "carry_forward": true
  },
  "key_findings": [
    {
      "finding_id": "{nnn}-F001",
      "finding_type": "{etymology/verse_pattern/term_behaviour/theological_note/anomaly}",
      "finding": "{concise statement}",
      "anchor_verses": []
    }
  ],
  "session_b_revision_candidates": []
}
```

**session_b_revision_candidates** — Required field. Empty array if extraction found no divergence from the narrative. Populated with `{candidate_id, observation, recommended_action}` records if extraction surfaces anything warranting narrative review. An empty array is an explicit confirmation, not an omission.

**dominant_terms** — Top 5 terms by verse count. Gives Session D the analytical centre of gravity of the registry at a glance.

**evidential_weight verse counts** — Summed from confirmed/plausible/uncertain terms respectively. uncertain_verse_count is always 0 (zero-verse terms carry uncertain status) but must be explicit.

---

## **14.2 Session D Pointers — wa-{nnn}-{word}-sdpointers-{date}.json**

Purpose: Evaluated, elaborated pointer file per registry. This is an analytical handoff document, not a data repeat. It carries evaluated observations, elaborated cross-registry questions, and research depth assessments. Aggregated at cluster level for the Session D run.

⚠ This file is evaluative and analytical. Pointers are not merely structural observations — each pointer must carry at least one synthesis_question and a prose_note that elaborates the significance. Data quality flags are included only when analytically relevant to Session D cross-registry work. Pure data corrections with no cross-registry significance are excluded.

```json
{
  "meta": {
    "json_template_version": "sdpointers_v1.0",
    "json_filename": "wa-{nnn}-{word}-sdpointers-{YYYYMMDD}.json",
    "registry_id": "{nnn}",
    "word": "{word}",
    "cluster_assignment": "{cluster_id}",
    "produced_date": "{YYYYMMDD}",
    "extraction_instruction_version": "WA-SessionB-Extraction-Instruction-v5.2"
  },
  "registry_context": {
    "sb_classification": "{classification}",
    "dimensions": "{comma-delimited}",
    "confirmed_count": 0,
    "plausible_count": 0,
    "dominant_terms": [
      { "strongs_id": "{H/Gnnnn}", "transliteration": "{transliteration}",
        "verse_count": 0, "evidential_status": "{status}" }
    ]
  },
  "pointers": [
    {
      "pointer_id": "{nnn}-SD001",
      "pointer_type": "{term_co_occurrence/verse_overlap/evidential_uncertainty/scope_boundary/data_quality_impact/structural_observation}",
      "pointer_subtype": "{see Section 11 for valid subtypes per type}",
      "significance": "{HIGH/MEDIUM/LOW}",
      "strongs_id": "{H/Gnnnn or null if word-level}",
      "also_in_registries": [
        { "registry_id": 0, "word": "{word}" }
      ],
      "synthesis_questions": [
        "{concise question Session D is asked to investigate}"
      ],
      "research_depth_required": "{SURFACE/STANDARD/DEEP}",
      "prose_note": "{fuller explanation — nuance, context, researcher thinking}",
      "session_b_source_ref": "{e.g. Section 10, Section 7}"
    }
  ],
  "dimensional_summary": {
    "relational_environment": false,
    "spirit_soul_body": false,
    "inner_operations": false,
    "being": false
  },
  "pointer_summary": {
    "total_pointers": 0,
    "by_type": {},
    "by_significance": { "HIGH": 0, "MEDIUM": 0, "LOW": 0 },
    "registries_implicated": [
      { "registry_id": 0, "word": "{word}" }
    ],
    "open_synthesis_questions": 0
  }
}
```

**synthesis_questions** — Required. One or more per pointer. Each is a single concise question that Session D is asked to investigate. Multiple questions are allowed and expected where a pointer touches more than one cross-registry dimension. This field is the primary mechanism by which Session B analytical work is carried into Session D without prejudging the synthesis.

**research_depth_required** — SURFACE means the pointer can likely be resolved by examining the cross-registry term or verse data. STANDARD means it requires cross-registry reading and comparison. DEEP means the question cannot be resolved without further exegetical, etymological, or theological research beyond what the programme data currently holds.

**also_in_registries** — Registry ID and word label pairs, resolved from word_registry at extraction time. Not ID numbers alone.

**pointer_type data_quality_impact** — Used only when a data quality issue is analytically relevant to Session D cross-registry work. Must include a synthesis_question explaining why the quality issue matters for cross-registry conclusions. Pure data corrections are excluded.

---

WA-Reference-v5.1 | 20260328 | Schema v3.7.0 | Supersedes WA-Reference-v5-20260327.docx
