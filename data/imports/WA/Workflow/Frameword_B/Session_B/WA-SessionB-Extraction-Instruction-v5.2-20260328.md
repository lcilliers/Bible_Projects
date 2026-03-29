**Framework B — Soul Word Analysis Programme**

**Session B Extraction Instruction**

Version 5.2 | March 2026 | Status: Active governing instruction

| **Document** | **Value** |
| --- | --- |
| Filename | WA-SessionB-Extraction-Instruction-v5.2-20260328.docx |
| Supersedes | WA-SessionB-Extraction-Instruction-v5.1-20260327.docx |
| Companion documents | WA-SessionB-Analysis-Instruction-v5 │ WA-SessionB-DataPrep-Instruction-v5 │ WA-Reference-v5.1 |
| Input | Completed Session B narrative document (wa-{nnn}-{word}-analysis-{date}.docx) │ Word JSON export (wa-{nnn}-{word}-extract-{date}.json) │ word_registry.json (for also_in_registries resolution) |
| Outputs | Session B JSON (wa-{nnn}-{word}-json-{date}.json) │ Analysis patch (wa-{nnn}-{word}-patch-{date}.json) │ Final registry extract (wa-{nnn}-{word}-final-{date}.json) │ Session D pointers (wa-{nnn}-{word}-sdpointers-{date}.json) |
| Claude AI role | Reads narrative, extracts structured data, populates JSON and post-patch outputs |
| Claude Code role | Applies analysis patch, updates database, confirms completion, triggers post-patch output production |

**Change Control Note — v5.2**

| **Change** | **Detail** |
| --- | --- |
| Section 0 | Outputs updated — four outputs per registry, not two |
| Section 1 | word_registry.json added as required input (for also_in_registries resolution) |
| Section 2 | Startup summary updated to reflect four-output cycle |
| Section 5 | Database mapping updated to definitive schema v3.7.0 — interim mappings removed |
| Section 6 | Patch operations updated — dedicated fields replace interim mappings |
| Section 8 | Post-patch output section added — Sections 8.1 and 8.2 govern final and sdpointers production |
| Section 9 | Output confirmation updated — four outputs per registry |
| Section 10 | Compliance rules updated — session_b_revision_candidates and narrative sync obligation added |
| Annexure A | Session B JSON template unchanged |
| Annexure B | Patch template updated — dedicated field operations replace interim flag operations |
| Annexure C | New — Final Registry Extract template |
| Annexure D | New — Session D Pointers template |

---

# **0. Purpose and Scope**

This document governs the Session B extraction session — the separate run that takes a completed Session B narrative document and produces four outputs per registry: the Session B JSON, the analysis completion patch, the final registry extract, and the Session D pointers file.

This session does not re-run the analysis. It reads the completed narrative and extracts its findings into structured JSON formats. The extraction session runs after the analysis session is complete and reviewed.

The extraction process is inherently evaluative for the post-patch outputs. Producing the final extract and Session D pointers file requires analytical judgement about dimensional weight, pointer significance, synthesis questions, and research depth. This judgement must be grounded in the narrative — it does not introduce new analysis — but it does elaborate and structure what the narrative contains.

| Narrative sync obligation: If the extraction process surfaces an observation that appears to be missing from, or inconsistent with, the Session B narrative, this must be recorded in session_b_revision_candidates in the final registry extract. It must not be silently incorporated into the JSON outputs. The narrative is the primary analytical document. The JSON outputs are derived from it. They must remain in sync. |
| --- |

| Batching: Extraction sessions are run in batches of approximately five completed narratives. Do not run extraction immediately after each analysis. Wait until a batch of approximately five are ready, then run one extraction session for the batch. |
| --- |

---

# **1. Required Inputs**

| **Input** | **Purpose** |
| --- | --- |
| This document (WA-SessionB-Extraction-Instruction-v5.2) | Governs all extraction behaviour |
| Completed narrative documents — wa-{nnn}-{word}-analysis-{date}.docx (batch of ~5) | Source for all extracted data |
| Word JSON exports — wa-{nnn}-{word}-extract-{date}.json | Database IDs and term_inv_ids for field mapping |
| word_registry.json | Resolution of also_in_registries {registry_id, word} pairs in sdpointers |

| **⚠  The extraction session does not require WA-SessionB-Analysis-Instruction-v5. That document governed the analysis. This session reads the completed output of that analysis.** |
| --- |

---

# **2. Startup Sequence**

- Read this instruction in full.

- Load all narrative documents in the batch and confirm each has a compliance statement in its final section.

- Load the corresponding word JSON exports to obtain term_inv_ids and file_ids for database mapping.

- Load word_registry.json and retain for also_in_registries resolution throughout the session.

- State the startup summary:

| 'Extraction v5.2 startup complete. Batch: [n] registries — [list]. All narratives confirmed complete. word_registry loaded for cross-registry resolution. Ready to extract.' |
| --- |

---

# **3. Extraction Process**

For each narrative document in the batch:

- Read the narrative document in full.

- Extract all fields into the Session B JSON template (Section 4 and Annexure A).

- Map every field to its database table and column using the definitive mapping (Section 5).

- Produce the analysis completion patch (Section 6).

- Submit patch to Claude Code and await confirmation of application.

- Once patch is confirmed, produce the final registry extract (Section 8.1 and Annexure C).

- Produce the Session D pointers file (Section 8.2 and Annexure D).

- Confirm all four outputs complete (Section 9).

| **⚠  Do not re-interpret or re-analyse during extraction of the Session B JSON and patch. The JSON captures what the narrative says. If the narrative is unclear on a point, note it as an extraction flag — do not resolve it analytically.** |
| --- |

| **⚠  The final registry extract and sdpointers file require evaluative judgement about dimensional weight, pointer significance, and synthesis questions. This judgement is grounded in the narrative. It elaborates and structures what the narrative says — it does not add new analysis. Any apparent gap between the narrative and the JSON outputs must be recorded in session_b_revision_candidates.** |
| --- |

---

# **4. Session B JSON — Field Definitions**

## **4.1 Meta Block**

| **Field** | **Description** |
| --- | --- |
| json_template_version | Always: session_b_json_v1.0 |
| json_filename | wa-{nnn}-{word}-json-{YYYYMMDD}.json |
| analysis_filename | Exact filename of the source narrative document |
| analysis_date | Date the narrative analysis was produced (from narrative header) |
| json_date | Date this JSON was produced (today) |
| chat_session_ref | Chat reference from narrative compliance statement if recorded, else null |
| session_b_instruction_version | Instruction version from narrative compliance statement |
| patch_type | Always: SESSIONB |
| patch_status | Always: pending on first production |

## **4.2 Registry Block**

| **Field** | **Maps to** |
| --- | --- |
| registry_id | word_registry.no |
| word_label | word_registry.word |
| active_term_count | Count of extracted/extracted_thin terms from narrative Section 3 |
| total_verse_count | Total verse count from narrative Section 1 |
| session_b_status | Always: Analysis Complete (set by patch) |
| cluster_assignment | From word_registry.cluster_assignment — confirm from JSON export |

## **4.3 Terms Array**

One entry per active term from narrative Section 3 — all terms with evidential status assigned.

| **Field** | **Source / Maps to** |
| --- | --- |
| strongs_id | From narrative term inventory / wa_term_inventory.strongs_number |
| transliteration | From narrative / wa_term_inventory.transliteration |
| language | Hebrew or Greek / wa_term_inventory.language |
| mti_status | From JSON export (confirmed in data prep) / mti_terms.status |
| verse_count | From narrative or JSON export / wa_term_inventory occurrence data |
| term_inv_id | From JSON export — required for patch operations |
| evidential_status | Assigned in narrative Section 9 — confirmed/plausible/uncertain/instrumental/relational_only |
| retention_note | From narrative — required for all non-confirmed terms, null for confirmed |

## **4.4 Dimensions Block**

| **Field** | **Source** |
| --- | --- |
| relational_environment.present | Boolean — from narrative Section 7 |
| relational_environment.note | Brief observation from narrative, or null |
| spirit_soul_body.present | Boolean — from narrative Section 7 |
| spirit_soul_body.note | Brief observation or null |
| inner_operations.present | Boolean — from narrative Section 7 |
| inner_operations.note | Brief observation or null |
| being.present | Boolean — from narrative Section 7 |
| being.note | Brief observation or null |

## **4.5 Inner Being Standing Block**

| **Field** | **Source / Maps to** |
| --- | --- |
| classification | From narrative scope assessment — confirmed_characteristic/plausible/uncertain/instrumental/relational_only |
| reasoning | From narrative Section 2 — required for non-confirmed, null for confirmed |
| carry_forward | Boolean — true unless researcher explicitly excluded |

## **4.6 Key Findings Array**

| **Field** | **Description** |
| --- | --- |
| finding_id | Convention: {nnn}-F{sequence} — e.g. 097-F001 |
| finding_type | etymology / verse_pattern / term_behaviour / theological_note / anomaly |
| finding | Concise statement from narrative Section 6 or Section 8 — not narrative prose |
| anchor_verses | Array of verse references supporting this finding |

## **4.7 Data Flags Array**

| **Field** | **Source / Maps to** |
| --- | --- |
| flag_id | Convention: {nnn}-DQ{sequence} |
| flag_type | From narrative or data prep — PH2_VOLUME_LIMITATION, PH2_DATA_ERROR, etc. |
| strongs_affected | Array of strongs_numbers |
| note | Description of the flag |

## **4.8 Session D Pointers Array**

These are structural observations copied from the narrative. They are the basis for the elaborated sdpointers file produced in Section 8.2.

| **Field** | **Source / Maps to** |
| --- | --- |
| pointer_id | Convention: {nnn}-SD{sequence} |
| pointer_type | term_co_occurrence / verse_overlap / evidential_uncertainty / scope_boundary |
| strongs_id | The term involved in the cross-registry observation |
| also_in_registries | Array of registry_ids — plain IDs at this stage; resolved to pairs in sdpointers |
| note | Structural observation from narrative — copied exactly |

---

# **5. Database Field Mapping — Definitive (Schema v3.7.0)**

The interim mappings from v5.1 are superseded. All fields map to dedicated database locations.

| **JSON section** | **Database table / field** |
| --- | --- |
| meta — json_filename, produced_date | wa_file_index.filename, wa_file_index.produced_date |
| registry — session_b_status | word_registry.session_b_status |
| registry — cluster_assignment | word_registry.cluster_assignment |
| terms — evidential_status | wa_term_inventory.evidential_status |
| terms — retention_note | wa_term_inventory.retention_note |
| dimensions — all fields | wa_session_b_dimensions (dedicated table) |
| inner_being_standing — classification | word_registry.sb_classification |
| inner_being_standing — reasoning | word_registry.sb_classification_reasoning |
| inner_being_standing — carry_forward | word_registry.carry_forward |
| key_findings — all fields | wa_session_b_findings (dedicated table) |
| data_flags — all fields | wa_term_phase2_flags or wa_session_research_flags per flag type |
| session_d_pointers — all fields | wa_session_research_flags — flag_code: SD_POINTER |

---

# **6. Analysis Completion Patch**

After extracting the Session B JSON, produce an analysis completion patch for each registry. This patch writes all Session B analytical results to the database using the definitive schema v3.7.0 mappings.

## **6.1 Required Operations — in order**

Operations 1 through N-1 may appear in any order within their group. The update_registry session_b_status operation must always be last.

**Group A — Term evidential status (one op per active term):**
- operation: update_evidential_status on wa_term_inventory
- Sets evidential_status and retention_note on each term record

**Group B — Dimensional profile (one op):**
- operation: insert on wa_session_b_dimensions
- One record per registry — all four dimensions with boolean and note

**Group C — Inner being standing (one op):**
- operation: update_registry
- Sets sb_classification, sb_classification_reasoning, carry_forward on word_registry

**Group D — Key findings (one op per finding):**
- operation: insert on wa_session_b_findings
- One record per finding from key_findings array

**Group E — Session D pointer flags (one op per pointer):**
- operation: insert on wa_session_research_flags
- flag_code: SD_POINTER, one record per session_d_pointer

**Final operation:**
- operation: update_registry
- Sets session_b_status = 'Analysis Complete' on word_registry
- Must be the last operation in every patch

## **6.2 Patch Naming**

| wa-{nnn}-{word}-patch-{YYYYMMDD}.json   patch_id: PATCH-{YYYYMMDD}-{nnn}-ANALYSIS-V1 |
| --- |

## **6.3 Handoff to Claude Code**

| PATCH SUBMISSION TO CLAUDE CODE   Patch file: wa-{nnn}-{word}-patch-{date}.json   Action required: Apply analysis completion patch. Confirm all operations applied.   Validation: Confirm session_b_status = 'Analysis Complete' in word_registry. Confirm evidential_status populated on all active terms in wa_term_inventory. Confirm wa_session_b_dimensions record inserted. Confirm wa_session_b_findings records inserted. Confirm SD_POINTER flags inserted in wa_session_research_flags. |
| --- |

---

# **7. Session D Pointer Logging**

The Session D pointers from the Session B JSON (Section 4.8) are logged to wa_session_research_flags with flag_code SD_POINTER as part of the analysis completion patch (Section 6.1 Group E). This makes them queryable by Claude Code.

These flag records are structural breadcrumbs. The elaborated, evaluative version of the pointers — with synthesis questions, significance ratings, and research depth assessments — is produced in the sdpointers file (Section 8.2). The two representations serve different purposes and both are required.

---

# **8. Post-Patch Outputs**

These two outputs are produced after Claude Code has confirmed the analysis completion patch has been applied successfully. They are not produced before patch confirmation.

Both outputs require the word_registry.json to be loaded for also_in_registries resolution. Registry IDs referenced in session_d_pointers are resolved to {registry_id, word} pairs at this stage.

## **8.1 Final Registry Extract**

File: wa-{nnn}-{word}-final-{date}.json
Template: Annexure C
Reference: WA-Reference-v5.1 Section 14.1

The final registry extract is a self-contained cross-table view of the completed registry. It serves as the primary input for Session D synthesis and for the future programme-level categorisation run.

**Production steps:**

- Populate meta block from narrative header and this instruction version.

- Populate registry_summary from narrative, JSON export, and word_registry:
  - dimensions: derive from Session B dimensional analysis — comma-delimited multi-value (see WA-Reference-v5.1 Section 4.3). This is an interpretive step grounded in the narrative.
  - dimensional_profile: assign PRIMARY / SECONDARY / PERIPHERAL to each of the four dimensions based on where the analytical weight falls in the narrative (see WA-Reference-v5.1 Section 4.5).
  - evidential_weight: sum verse counts by evidential status across all terms. dominant_terms: top 5 terms by verse count with their evidential status.

- Populate terms array from Session B JSON terms array — same fields, no raw verse text.

- Populate dimensions block from Session B JSON dimensions block.

- Populate inner_being_standing from Session B JSON.

- Populate key_findings from Session B JSON.

- Populate session_b_revision_candidates:
  - If extraction identified no divergence between narrative and JSON outputs: empty array [].
  - If extraction surfaced any observation that appears missing from or inconsistent with the narrative: add one record per candidate with candidate_id, observation, and recommended_action.
  - An empty array is an explicit confirmation of sync. It must always be present — never omitted.

## **8.2 Session D Pointers File**

File: wa-{nnn}-{word}-sdpointers-{date}.json
Template: Annexure D
Reference: WA-Reference-v5.1 Section 14.2

The Session D pointers file is an analytical handoff document. It elaborates the structural observations from the Session B narrative into evaluated, annotated pointers that actively assist Session D cross-registry synthesis without prejudging the synthesis conclusions.

**This file is evaluative. It is not a data repeat.**

**Production steps:**

- Populate meta and registry_context blocks.

- For each pointer from Session B JSON session_d_pointers array, produce an elaborated pointer record:
  - pointer_type and pointer_subtype: classify using the controlled vocabulary in WA-Reference-v5.1 Section 11.
  - significance: assign HIGH / MEDIUM / LOW based on analytical significance to Session D — not data quality.
  - also_in_registries: resolve registry_ids to {registry_id, word} pairs using word_registry.json.
  - synthesis_questions: required. One or more concise questions Session D is asked to investigate. These are the primary mechanism for carrying Session B analytical insight into Session D. Multiple questions per pointer are expected where a pointer touches more than one cross-registry dimension. Do not collapse multiple questions into one.
  - research_depth_required: SURFACE / STANDARD / DEEP — honest assessment of what is needed to answer the synthesis questions. DEEP means the answer requires research beyond the programme data currently held.
  - prose_note: fuller explanation — the reasoning, the nuance, what makes this pointer analytically significant. This is where research comments and deeper observations from the narrative are captured and carried forward. If the narrative contains qualifications, caveats, or open questions related to this pointer, they belong here.
  - session_b_source_ref: which section of the narrative this pointer originates from.

- Data quality flags: include as pointer_type data_quality_impact only when the quality issue is analytically relevant to Session D cross-registry work — i.e. when it could affect cross-registry conclusions. Flags that record corrected anomalies with no downstream significance are excluded. Every data_quality_impact pointer must include a synthesis_question explaining why the quality issue matters.

- Populate dimensional_summary with booleans — fast reference for cluster-level comparison.

- Populate pointer_summary: count by type, count by significance, list all registries implicated as {registry_id, word} pairs, count all synthesis_questions across all pointers.

---

# **9. Output Confirmation**

The extraction session is complete for a registry when all of the following are confirmed:

- Session B JSON produced and saved: wa-{nnn}-{word}-json-{date}.json ✓
- Analysis completion patch produced and submitted: wa-{nnn}-{word}-patch-{date}.json ✓
- Claude Code has applied the patch and confirmed all operations successful ✓
- Final registry extract produced and saved: wa-{nnn}-{word}-final-{date}.json ✓
- Session D pointers file produced and saved: wa-{nnn}-{word}-sdpointers-{date}.json ✓

| Output confirmation statement: 'Extraction v5.2 complete. Batch of [n] registries processed. Session B JSONs: [list]. Patches applied: [list]. Final extracts: [list]. SDPointers files: [list]. Session B revision candidates: [n total across batch — list any non-empty]. All registries now at Analysis Complete status.' |
| --- |

---

# **10. Researcher Compliance Rules**

| **⚠  Do not re-analyse or re-interpret during Session B JSON extraction. The JSON captures what the narrative says. Analytical judgements belong in the analysis session, not here.** |
| --- |

| **⚠  Narrative sync is mandatory. If the process of producing the final extract or sdpointers file surfaces an observation that appears to be missing from or inconsistent with the narrative, record it in session_b_revision_candidates. Do not silently incorporate it into the JSON outputs. The narrative and the JSON outputs must remain in sync.** |
| --- |

Additional compliance rules:

- If the narrative is unclear on a point, note it as an extraction flag — do not resolve it analytically
- Do not add findings that are not in the narrative
- Do not modify evidential status assignments from the narrative
- Session D pointers are elaborated from the narrative — the synthesis_questions and prose_notes expand what is there, they do not introduce new cross-registry claims
- also_in_registries must always be resolved to {registry_id, word} pairs — never plain IDs
- session_b_revision_candidates must always be present in the final extract — empty array if no candidates, never omitted
- Data quality flags are carried to sdpointers only when analytically relevant to Session D — never as a full repeat of the data_flags array

---

# **Annexure A — Session B JSON Template**

File naming: wa-{nnn}-{word}-json-{YYYYMMDD}.json

```json
{
  "meta": {
    "json_template_version": "session_b_json_v1.0",
    "json_filename": "wa-{nnn}-{word}-json-{YYYYMMDD}.json",
    "analysis_filename": "wa-{nnn}-{word}-analysis-{YYYYMMDD}.docx",
    "analysis_date": "{YYYYMMDD}",
    "json_date": "{YYYYMMDD}",
    "chat_session_ref": "{ref or null}",
    "session_b_instruction_version": "WA-SessionB-Analysis-Instruction-v5",
    "patch_type": "SESSIONB",
    "patch_status": "pending"
  },
  "registry": {
    "registry_id": "{nnn}",
    "word_label": "{word}",
    "active_term_count": 0,
    "total_verse_count": 0,
    "session_b_status": "Analysis Complete",
    "cluster_assignment": "{cluster_id}"
  },
  "terms": [
    {
      "strongs_id": "{H/Gnnnn}",
      "transliteration": "{transliteration}",
      "language": "{Hebrew or Greek}",
      "mti_status": "{status}",
      "verse_count": 0,
      "term_inv_id": 0,
      "evidential_status": "{confirmed/plausible/uncertain/instrumental/relational_only}",
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
  "data_flags": [
    {
      "flag_id": "{nnn}-DQ001",
      "flag_type": "{PH2_VOLUME_LIMITATION/PH2_DATA_ERROR/etc}",
      "strongs_affected": [],
      "note": "{description}"
    }
  ],
  "session_d_pointers": [
    {
      "pointer_id": "{nnn}-SD001",
      "pointer_type": "{term_co_occurrence/verse_overlap/evidential_uncertainty/scope_boundary}",
      "strongs_id": "{H/Gnnnn}",
      "also_in_registries": [],
      "note": null
    }
  ]
}
```

---

# **Annexure B — Analysis Completion Patch Template**

File naming: wa-{nnn}-{word}-patch-{YYYYMMDD}.json

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-ANALYSIS-V1",
    "registry_id": "{nnn}",
    "word": "{word}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-SessionB-Extraction-Instruction-v5.2",
    "session_b_status": "Analysis Complete",
    "description": "Analysis completion patch for registry {nnn} — {word}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "update_evidential_status",
      "table": "wa_term_inventory",
      "term_inv_id": 0,
      "strongs_number": "{H/Gnnnn}",
      "set": {
        "evidential_status": "{status}",
        "retention_note": null
      },
      "description": "{strongs_id} {transliteration} — evidential_status: {status}"
    },
    {
      "op_id": "OP-N01",
      "operation": "insert",
      "table": "wa_session_b_dimensions",
      "record": {
        "registry_id": "{nnn}",
        "file_id": "{file_id}",
        "relational_environment": 0,
        "relational_environment_note": null,
        "spirit_soul_body": 0,
        "spirit_soul_body_note": null,
        "inner_operations": 0,
        "inner_operations_note": null,
        "being": 0,
        "being_note": null,
        "raised_date": "{yyyy-mm-dd}",
        "session_b_instruction": "WA-SessionB-Extraction-Instruction-v5.2"
      },
      "description": "Dimensional profile for registry {nnn}"
    },
    {
      "op_id": "OP-N02",
      "operation": "update_registry",
      "registry_no": "{nnn}",
      "set": {
        "sb_classification": "{classification}",
        "sb_classification_reasoning": null,
        "carry_forward": 1
      },
      "description": "Inner being standing: {classification}"
    },
    {
      "op_id": "OP-N03",
      "operation": "insert",
      "table": "wa_session_b_findings",
      "record": {
        "finding_id": "{nnn}-F001",
        "registry_id": "{nnn}",
        "file_id": "{file_id}",
        "finding_type": "{type}",
        "finding": "{statement}",
        "anchor_verses": "{comma-separated references}",
        "raised_date": "{yyyy-mm-dd}",
        "session_b_instruction": "WA-SessionB-Extraction-Instruction-v5.2"
      },
      "description": "{nnn}-F001 — {finding_type}"
    },
    {
      "op_id": "OP-N04",
      "operation": "insert",
      "table": "wa_session_research_flags",
      "record": {
        "registry_id": "{nnn}",
        "file_id": "{file_id}",
        "flag_code": "SD_POINTER",
        "flag_label": "{nnn}-SD001",
        "strongs_reference": "{H/Gnnnn or null}",
        "cross_registry_id": "{registry_id or null}",
        "priority": "MEDIUM",
        "session_target": "D",
        "description": "{pointer note}",
        "session_raised": "WA-SessionB-Extraction-Instruction-v5.2",
        "raised_date": "{yyyy-mm-dd}",
        "resolved": 0
      },
      "description": "{nnn}-SD001 — SD_POINTER"
    },
    {
      "op_id": "OP-LAST",
      "operation": "update_registry",
      "registry_no": "{nnn}",
      "set": { "session_b_status": "Analysis Complete" },
      "description": "Session B extraction complete — wa-{nnn}-{word}-analysis-{date}.docx — JSON: wa-{nnn}-{word}-json-{date}.json"
    }
  ],
  "_patch_summary": {
    "total_operations": 0,
    "update_evidential_status": 0,
    "insert_session_b_dimensions": 1,
    "update_registry_sb_classification": 1,
    "insert_session_b_findings": 0,
    "insert_sd_pointer_flags": 0,
    "update_registry_status": 1
  }
}
```

---

# **Annexure C — Final Registry Extract Template**

File naming: wa-{nnn}-{word}-final-{YYYYMMDD}.json

See WA-Reference-v5.1 Section 14.1 for full field definitions and production guidance.

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
    "dimensions": "{comma-delimited dimension values}",
    "cluster_assignment": "{cluster_id}",
    "phase1_term_count": 0,
    "phase1_verse_count": 0,
    "active_term_count": 0,
    "confirmed_count": 0,
    "plausible_count": 0,
    "uncertain_count": 0,
    "session_b_status": "Analysis Complete",
    "sb_classification": "{classification}",
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
        {
          "strongs_id": "{H/Gnnnn}",
          "transliteration": "{transliteration}",
          "verse_count": 0,
          "evidential_status": "{status}"
        }
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
    "classification": "{classification}",
    "reasoning": null,
    "carry_forward": true
  },
  "key_findings": [
    {
      "finding_id": "{nnn}-F001",
      "finding_type": "{type}",
      "finding": "{concise statement}",
      "anchor_verses": []
    }
  ],
  "session_b_revision_candidates": []
}
```

---

# **Annexure D — Session D Pointers Template**

File naming: wa-{nnn}-{word}-sdpointers-{YYYYMMDD}.json

See WA-Reference-v5.1 Section 14.2 for full field definitions and production guidance.

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
      {
        "strongs_id": "{H/Gnnnn}",
        "transliteration": "{transliteration}",
        "verse_count": 0,
        "evidential_status": "{status}"
      }
    ]
  },
  "pointers": [
    {
      "pointer_id": "{nnn}-SD001",
      "pointer_type": "{term_co_occurrence/verse_overlap/evidential_uncertainty/scope_boundary/data_quality_impact/structural_observation}",
      "pointer_subtype": "{see WA-Reference-v5.1 Section 11}",
      "significance": "{HIGH/MEDIUM/LOW}",
      "strongs_id": "{H/Gnnnn or null}",
      "also_in_registries": [
        { "registry_id": 0, "word": "{word}" }
      ],
      "synthesis_questions": [
        "{concise question Session D is asked to investigate}"
      ],
      "research_depth_required": "{SURFACE/STANDARD/DEEP}",
      "prose_note": "{fuller explanation — nuance, context, researcher thinking, open questions from narrative}",
      "session_b_source_ref": "{e.g. Section 10}"
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

---

WA-SessionB-Extraction-Instruction-v5.2 | 20260328 | Supersedes WA-SessionB-Extraction-Instruction-v5.1-20260327.docx
