# WA-SessionB-Extraction-Instruction-v5.5-20260330

**Framework B — Soul Word Analysis Programme**

**Session B Extraction Instruction**

Version 5.5 | March 2026 | Status: Active governing instruction

| **Document** | **Value** |
|---|---|
| Filename | WA-SessionB-Extraction-Instruction-v5.6-20260330.md |
| Supersedes | WA-SessionB-Extraction-Instruction-v5.5-20260330.md |
| Change note | v5.6 — Section 6.3: failure patch rule added — if SESSIONB patch is rejected, produce REPAIR failure patch before retrying. Section 9: failure patch rule added for SESSIONB-COMPLETE patch rejection. |
| Companion documents | WA-SessionB-Analysis-Instruction-v5.4 │ WA-SessionB-DataPrep-Instruction-v5.4 │ WA-Reference-v5.4 |
| Inputs | Completed Session B narrative documents — wa-{nnn}-{word}-analysis-{date}.md (all words in pool) │ Word JSON exports — wa-{nnn}-{word}-extract-{date}.json (for database IDs) │ Pool analysis dataset — wa-pool-{pool_id}-analysis-{date}.json (pool context reference) │ word_registry.json (for also_in_registries resolution) |
| Outputs per word | Session B JSON — wa-{nnn}-{word}-json-{date}.json │ Analysis completion patch — PATCH-{date}-{nnn}-SESSIONB-V1.json │ Final registry extract — wa-{nnn}-{word}-final-{date}.json │ Session D pointers — wa-{nnn}-{word}-sdpointers-{date}.json |
| Claude AI role | Reads narratives, extracts structured data, produces JSON outputs and Session D pointers files |
| Claude Code role | Applies analysis completion patches, re-exports JSONs, confirms completion |

**Change Control Note — v5.3**

| **Change** | **Detail** |
|---|---|
| Section 0 | Pool context added — extraction runs per pool, not per arbitrary batch of five |
| Section 1 | Pool analysis dataset added as required input; narrative format updated from .docx to .md |
| Section 2 | Startup summary updated for pool-based extraction |
| Section 3 | Batching rule replaced: extraction unit is the pool, not five narratives |
| Section 4.8 | SD pointer scope narrowed: intra-pool observations are Session B findings, not SD pointers. Pointer types revised. |
| Section 8.2 | SD pointer production guidance updated to reflect narrowed scope |
| Section 9 | Output confirmation updated |
| Section 10 | Compliance rules updated — SD pointer boundary added |
| Annexure A | analysis_filename extension updated to .md; pool_id field added to meta |
| Annexure D | pointer_type list revised — intra-pool types removed |

---

## 0. Purpose and Scope

This document governs the Session B extraction session — the separate run that takes a set of completed Session B narrative documents (one per word in a pool) and produces four outputs per word: the Session B JSON, the analysis completion patch, the final registry extract, and the Session D pointers file.

This session does not re-run the analysis. It reads the completed narratives and extracts their findings into structured JSON formats. The extraction session runs after all narrative documents for a pool are complete and reviewed.

**Pool-based extraction:** Extraction runs per pool — not per arbitrary batch of five. When a pool analysis session produces narratives for all words in the pool, one extraction session processes the complete set together. This preserves the pool context across all outputs.

The extraction process is inherently evaluative for the post-patch outputs. Producing the final extract and Session D pointers file requires analytical judgement about dimensional weight, pointer significance, synthesis questions, and research depth. This judgement is grounded in the narrative — it does not introduce new analysis — but it does elaborate and structure what the narrative contains.

| Narrative sync obligation: If the extraction process surfaces an observation that appears to be missing from, or inconsistent with, the Session B narrative, this must be recorded in session_b_revision_candidates in the final registry extract. It must not be silently incorporated into the JSON outputs. The narrative is the primary analytical document. The JSON outputs are derived from it. |
|---|

---

## 1. Required Inputs

| **Input** | **Purpose** |
|---|---|
| This document (WA-SessionB-Extraction-Instruction-v5.4) | Governs all extraction behaviour |
| Completed narrative documents — wa-{nnn}-{word}-analysis-{date}.md (all words in pool) | Source for all extracted data — one per word |
| Word JSON exports — wa-{nnn}-{word}-extract-{date}.json (post-analysis re-export, one per word) | Database IDs for patch operations. Use: `term_inv_id` from each term's `mti.id` field (for `update_evidential_status` operations). Use: `file_id` from `files[0].id` — the first Phase 1 file entry. If multiple file entries exist, use the one with `phase = "Phase 1"` and the most recent `produced_date`. |
| Pool analysis dataset — wa-pool-{pool_id}-analysis-{date}.json | Pool context reference — confirms pool membership, shared terms, XREF term profiles |
| word_registry.json | Resolves `also_in_registries` values to `{registry_id, word}` pairs. This is a programme-level export of all word_registry records. Claude Code produces it with: `python -m engine.engine --export-registry`. Re-export at the start of each Extraction session. Minimum required fields per record: `no`, `word`, `cluster_assignment`, `session_b_status`. |

| **⚠ The extraction session does not require WA-SessionB-Analysis-Instruction-v5.2. That document governed the analysis. This session reads the completed output of that analysis.** |
|---|

---

## 2. Startup Sequence

- Read this instruction in full.
- Load all narrative documents for the pool. Confirm each has a compliance statement in Section 11.
- Load the pool analysis dataset to confirm pool membership and shared terms.
- Load the corresponding word JSON exports to obtain term_inv_ids and file_ids for database mapping.
- Load word_registry.json and retain for also_in_registries resolution throughout the session.
- State the startup summary:

```
Extraction v5.4 startup complete.
Pool: {pool_id}
Words in pool: {n} — {list: registry_no — word}
All narratives loaded and compliance statements confirmed.
Pool analysis dataset loaded — {n} shared terms across pool.
word_registry loaded for cross-registry resolution.
Ready to extract.
```

---

## 3. Extraction Process

For each word in the pool:

- Read the narrative document in full.
- Extract all fields into the Session B JSON template (Section 4 and Annexure A).
- Map every field to its database table and column using the definitive mapping (Section 5).
- Produce the analysis completion patch (Section 6).
- Submit patch to Claude Code and await confirmation of application.
- Once patch is confirmed, produce the final registry extract (Section 8.1 and Annexure C).
- Produce the Session D pointers file (Section 8.2 and Annexure D).
- Confirm all four outputs complete (Section 9).

Process all words in the pool before confirming extraction complete for the pool.

| **⚠ Do not re-interpret or re-analyse during extraction of the Session B JSON and patch. The JSON captures what the narrative says. If the narrative is unclear on a point, note it as an extraction flag — do not resolve it analytically.** |
|---|

| **⚠ The final registry extract and sdpointers file require evaluative judgement about dimensional weight, pointer significance, and synthesis questions. This judgement is grounded in the narrative. Any apparent gap between the narrative and the JSON outputs must be recorded in session_b_revision_candidates.** |
|---|

---

## 4. Session B JSON — Field Definitions

### 4.1 Meta Block

| **Field** | **Description** |
|---|---|
| json_template_version | Always: session_b_json_v1.1 |
| json_filename | wa-{nnn}-{word}-json-{YYYYMMDD}.json |
| analysis_filename | Exact filename of the source narrative document |
| analysis_date | Date the narrative analysis was produced (from narrative header) |
| json_date | Date this JSON was produced (today) |
| pool_id | Pool identifier from narrative header |
| pool_approach | `simultaneous` or `word_by_word_fallback` — from narrative compliance statement |
| chat_session_ref | Chat reference from narrative compliance statement if recorded, else null |
| session_b_instruction_version | Always: WA-SessionB-Analysis-Instruction-v5.2 |
| patch_type | Always: SESSIONB |
| patch_status | Always: pending on first production |

### 4.2 Registry Block

| **Field** | **Maps to** |
|---|---|
| registry_id | word_registry.no |
| word_label | word_registry.word |
| pool_id | From pool analysis dataset meta |
| active_term_count | Count of OWNER terms with evidential status from narrative Section 3 |
| xref_term_count | Count of XREF terms from narrative Section 3 |
| total_anchor_verses | From narrative header |
| session_b_status | Always: Analysis Complete (set by patch) |
| cluster_assignment | From word_registry.cluster_assignment — confirm from JSON export |

### 4.3 Terms Array

One entry per active OWNER term from narrative Section 3 — all terms with evidential status assigned. XREF terms are not included in the terms array — they are in the xref_terms block (Section 4.3a).

| **Field** | **Source / Maps to** |
|---|---|
| strongs_id | From narrative term inventory / wa_term_inventory.strongs_number |
| transliteration | From narrative / wa_term_inventory.transliteration |
| language | Hebrew or Greek / wa_term_inventory.language |
| mti_status | From JSON export (confirmed in data prep) / mti_terms.status |
| anchor_verse_count | From pool analysis dataset — count of anchor verses across all groups for this term |
| related_verse_count | From pool analysis dataset — count of related verses across all groups |
| term_inv_id | From JSON export — required for patch operations |
| evidential_status | Assigned in narrative Section 9 — confirmed/plausible/uncertain/instrumental/relational_only |
| retention_note | From narrative — required for all non-confirmed terms, null for confirmed |

### 4.3a XREF Terms Block

Informational only — no patch operations on XREF terms.

| **Field** | **Source** |
|---|---|
| strongs_id | From narrative Section 3 |
| transliteration | From narrative |
| gloss | From pool analysis dataset xref_terms |
| owner_registry_id | From pool analysis dataset xref_terms |
| owner_word | From pool analysis dataset xref_terms |
| contextual_groups_used | How this word engaged the XREF term — which OWNER groups were referenced in the narrative |

### 4.4 Dimensions Block

| **Field** | **Source** |
|---|---|
| relational_environment.present | Boolean — from narrative Section 7 |
| relational_environment.note | Brief observation from narrative, or null |
| spirit_soul_body.present | Boolean — from narrative Section 7 |
| spirit_soul_body.note | Brief observation or null |
| inner_operations.present | Boolean — from narrative Section 7 |
| inner_operations.note | Brief observation or null |
| being.present | Boolean — from narrative Section 7 |
| being.note | Brief observation or null |

### 4.5 Inner Being Standing Block

| **Field** | **Source / Maps to** |
|---|---|
| classification | From narrative scope assessment — confirmed_characteristic/plausible/uncertain/instrumental/relational_only |
| reasoning | From narrative Section 2 — required for non-confirmed, null for confirmed |
| carry_forward | Boolean — true unless researcher explicitly excluded |

### 4.6 Key Findings Array

| **Field** | **Description** |
|---|---|
| finding_id | Convention: {nnn}-F{sequence} — e.g. 069-F001 |
| finding_type | etymology / verse_pattern / term_behaviour / theological_note / anomaly / pool_observation |
| finding | Concise statement from narrative Section 6 or Section 8 — not narrative prose |
| anchor_verses | Array of verse references supporting this finding |

**Intra-pool cross-word observations** are distinguished by using `finding_type = "pool_observation"`. Do NOT add an `intra_pool` field — the `wa_session_b_findings` table does not have this column. Use `finding_type` as the discriminator: `pool_observation` means the finding references another word in the pool; all other finding_type values are word-specific.

The `wa_session_b_findings` table columns are: id, finding_id, registry_id, file_id, finding_type, finding, anchor_verses, raised_date, session_b_instruction. The patch insert must only use these columns.

### 4.7 Data Flags Array

| **Field** | **Source / Maps to** |
|---|---|
| flag_id | Convention: {nnn}-DQ{sequence} |
| flag_type | From narrative or data prep — PH2_VOLUME_LIMITATION, PH2_DATA_ERROR, etc. |
| strongs_affected | Array of strongs_numbers |
| note | Description of the flag |

### 4.8 Session D Pointers Array

**Scope:** These are cross-pool and whole-programme observations only. Intra-pool cross-word observations are Session B findings (Section 4.6) and must NOT appear here. See Section 10 compliance rules.

| **Field** | **Source / Maps to** |
|---|---|
| pointer_id | Convention: {nnn}-SD{sequence} |
| pointer_type | scope_boundary / structural_observation / evidential_uncertainty / data_quality_impact |
| strongs_id | The term involved, if term-specific; null if word-level or whole-programme |
| cross_registry_ids | Array of registry_ids outside this pool — must be cross-pool or whole-programme |
| note | Structural observation from narrative Section 10 — copied exactly |

**Valid pointer_type values and when to use:**

| Type | Use when |
|---|---|
| scope_boundary | A term or verse in this word appears in a registry outside this pool — structural fact, no analysis |
| structural_observation | A pattern visible in this word's data that may extend to registries outside this pool — flagged as hypothesis |
| evidential_uncertainty | A thin corpus or boundary term that cannot be fully assessed without cross-pool context |
| data_quality_impact | A quality flag that may affect cross-pool conclusions — carry only if analytically significant |

**Do NOT include as SD pointers:**
- Observations about terms shared between words within this pool — these are Session B findings
- Verse overlaps between words within this pool — these are Session B findings
- Any observation that was fully addressed in the simultaneous analysis session

---

## 5. Database Field Mapping — Definitive (Schema v3.8.0)

| **JSON section** | **Database table / field** |
|---|---|
| meta — json_filename, produced_date | wa_file_index.filename, wa_file_index.produced_date |
| registry — session_b_status | word_registry.session_b_status |
| registry — cluster_assignment | word_registry.cluster_assignment |
| registry — dimensions | word_registry.dimensions (comma-delimited — written by Group F update_registry) |
| registry — description | word_registry.description (Session B confirmed description — written by Group F update_registry) |
| terms — evidential_status | wa_term_inventory.evidential_status (OWNER terms only) |
| terms — retention_note | wa_term_inventory.retention_note (OWNER terms only) |
| dimensions — all fields | wa_session_b_dimensions (dedicated table) |
| inner_being_standing — classification | word_registry.sb_classification |
| inner_being_standing — reasoning | word_registry.sb_classification_reasoning |
| inner_being_standing — carry_forward | word_registry.carry_forward |
| key_findings — all fields | wa_session_b_findings (dedicated table) |
| data_flags — all fields | wa_term_phase2_flags or wa_session_research_flags per flag type |
| session_d_pointers — all fields | wa_session_research_flags — flag_code: SD_POINTER |

---

## 6. Analysis Completion Patch

After extracting the Session B JSON, produce one analysis completion patch per word. This patch writes all Session B analytical results to the database.

### 6.1 Required Operations — in order

Operations within groups may appear in any order. `update_registry` setting `session_b_status = Analysis Complete` must always be last.

**Group A — Term evidential status (one op per active OWNER term):**
- operation: `update_evidential_status` on wa_term_inventory
- Sets `evidential_status` and `retention_note` on each OWNER term record
- **OWNER-only rule:** update_evidential_status targets OWNER records only (term_owner_type = 'OWNER'). One operation per active OWNER term. XREF terms must never be targeted — their evidential status is inherited from the OWNER registry and must not be written by this patch. No update_evidential_status operation is produced for XREF term_inv_ids under any circumstance.

**Distinction from update_mti_status (for clarity):** update_mti_status (used in DataPrep) writes mti_terms.status — a programme-wide term classification shared across all registries. update_evidential_status (used here) writes wa_term_inventory.evidential_status — a per-word, per-registry analytical assessment on a different table. These are non-overlapping operations on different tables.

**Group B — Dimensional profile (one op):**
- operation: `insert` on wa_session_b_dimensions
- One record per word — all four dimensions with boolean and note

**Group C — Inner being standing (one op):**
- operation: `update_registry`
- Sets `sb_classification`, `sb_classification_reasoning`, `carry_forward` on word_registry

**Group D — Key findings (one op per finding):**
- operation: `insert` on wa_session_b_findings
- One record per finding from key_findings array — include both word-specific and pool_observation findings

**Group E — Session D pointer flags (one op per cross-pool pointer):**
- operation: `insert` on wa_session_research_flags
- flag_code: SD_POINTER
- One record per entry in session_d_pointers array (cross-pool/whole-programme only)

**Group F — Registry field updates (one op for dimensions, one op for description):**
- operation: `update_registry` on word_registry
- Sets `dimensions` (comma-delimited multi-value string derived from Session B dimensional analysis — see Section 8.1 and valid values in WA-Reference Section 4.3)
- Sets `description` (Session B confirmed description replacing Phase 1 preliminary value — see Section 8.1)
- These two fields may be combined in a single update_registry operation or split into two. They must appear before the final session_b_status update_registry.

**Final operation:**
- operation: `update_registry`
- Sets `session_b_status = 'Analysis Complete'` on word_registry
- Must be the last operation in every patch

### 6.2 Patch Naming

```
PATCH-{YYYYMMDD}-{nnn}-SESSIONB-V1.json
patch_id: PATCH-{YYYYMMDD}-{nnn}-SESSIONB-V1
```

### 6.3 Handoff to Claude Code

```
PATCH SUBMISSION TO CLAUDE CODE

Pool: {pool_id}
Patches: {n} — one per word

For each patch:
  File: PATCH-{YYYYMMDD}-{nnn}-SESSIONB-V1.json
  Registry: {nnn} — {word}
  Action required:
    1. Apply patch
    2. Confirm: evidential_status on all active OWNER terms
    3. Confirm: wa_session_b_dimensions record inserted
    4. Confirm: wa_session_b_findings records inserted
    5. Confirm: SD_POINTER flags inserted (cross-pool pointers only)
    6. Set session_b_status = Analysis Complete
    7. Re-export JSON: wa-{nnn}-{word}-extract-{date}.json

When all words confirmed at Analysis Complete:
  Report to researcher.
```

**If any SESSIONB patch is rejected by the applicator:** Produce a REPAIR failure patch immediately for that word (naming: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1`; patch_type: REPAIR; session_b_status: current unchanged value; one registry_note recording the failure details). Submit the failure patch. Report to researcher: which patch was rejected, the rejection reason, and the failure patch_id. Do not produce the final registry extract or sdpointers file for this word until the researcher has reviewed and the corrected patch has been successfully applied. See WA-SessionB-ClaudeCode-Instructions-v3.2 Section 16 for the failure patch template.

---

## 7. Session D Pointer Logging

Session D pointers (cross-pool and whole-programme observations only) are logged to `wa_session_research_flags` with `flag_code = SD_POINTER` as part of the analysis completion patch. These flag records are structural breadcrumbs — queryable by Claude Code.

The elaborated, evaluative version of the pointers is in the sdpointers file (Section 8.2). Both representations are required. The flag records enable programme-level query; the sdpointers file enables Session D navigation.

**Intra-pool observations are NOT logged as SD_POINTER flags.** They are logged as `wa_session_b_findings` records with `finding_type = "pool_observation"`.

---

## 8. Post-Patch Outputs

Produced after Claude Code has confirmed the analysis completion patch is applied. Not before.

Both outputs require word_registry.json loaded for also_in_registries resolution.

### 8.1 Final Registry Extract

File: `wa-{nnn}-{word}-final-{date}.json`
Template: Annexure C

The final registry extract is a self-contained cross-table view of the completed registry. It serves as primary input for Session D synthesis and the future programme-level categorisation run.

**Production steps:**

- Populate meta block from narrative header and this instruction version.
- Populate registry_summary:
  - `dimensions`: derive from Session B dimensional analysis — comma-delimited multi-value using the valid dimension values from WA-Reference-v5.4 Section 4.3. Example: "Affective/Emotional,Volitional/Will,Spiritual/God-ward". This is the same value written to word_registry.dimensions via the Group F update_registry operation in the analysis completion patch.
  - `description`: a concise Session B confirmed description of what this word represents as an inner-being characteristic, grounded in the anchor verse evidence. This replaces any Phase 1 preliminary description. This is the same value written to word_registry.description via the Group F update_registry operation.
  - `dimensional_profile`: assign PRIMARY / SECONDARY / PERIPHERAL to each of the four dimensions based on analytical weight in the narrative
  - `evidential_weight`: sum anchor verse counts by evidential status across all OWNER terms. `dominant_terms`: top 5 OWNER terms by anchor verse count with evidential status.
- Populate terms array from Session B JSON terms array.
- Populate xref_terms from Session B JSON xref_terms block.
- Populate dimensions block from Session B JSON.
- Populate inner_being_standing from Session B JSON.
- Populate key_findings from Session B JSON — include pool_observation findings.
- Populate pool_observations: a summary block listing which other words in the pool were observed in relation to this word, and what the key intra-pool findings were. **Note: pool_observations is a file-only artefact — it is not persisted to the database.** If Session D requires programmatic query of intra-pool observations, a database table will need to be designed at that stage. The wa_session_b_findings records with finding_type = 'pool_observation' provide the closest database equivalent.
- Populate session_b_revision_candidates: empty array [] if no divergence found between narrative and JSON. Never omit this field — empty array = explicit confirmation of sync.

### 8.2 Session D Pointers File

File: `wa-{nnn}-{word}-sdpointers-{date}.json`
Template: Annexure D

The Session D pointers file is an analytical handoff document — evaluated, annotated pointers that assist Session D cross-pool synthesis without prejudging its conclusions.

**This file covers cross-pool and whole-programme observations only.** Intra-pool observations are in the final registry extract (pool_observations block) and key_findings. They do not appear in the sdpointers file.

**Production steps:**

- Populate meta and registry_context blocks.
- For each pointer from Session B JSON session_d_pointers array (cross-pool/whole-programme only):
  - `pointer_type`: classify using the valid types in Section 4.8
  - `significance`: HIGH / MEDIUM / LOW — based on analytical significance to Session D
  - `also_in_registries`: resolve registry_ids to {registry_id, word} pairs using word_registry.json. These must all be registries **outside** this pool.
  - `synthesis_questions`: required. One or more concise questions Session D is asked to investigate. These are the primary mechanism for carrying Session B analytical insight into Session D.
  - `research_depth_required`: SURFACE / STANDARD / DEEP
  - `prose_note`: fuller explanation — reasoning, nuance, what makes this pointer analytically significant, open questions from the narrative
  - `session_b_source_ref`: which section of the narrative this pointer originates from (e.g. "Section 10")
- `data_quality_impact` pointers: include only when the quality issue may affect cross-pool conclusions. Every such pointer must include a synthesis_question explaining why.
- Populate dimensional_summary with booleans.
- Populate pointer_summary: counts by type, counts by significance, all registries implicated as {registry_id, word} pairs, total synthesis_questions count.

**If a word in a not-shared pool (no XREFs, no cross-pool shared terms) produces no genuine cross-pool observations:** the sdpointers file is produced with an empty pointers array. This is valid and expected for independent words. The pointer_summary must still be present with zero counts.

---

## 9. Output Confirmation and Session B Complete

Extraction is complete for a pool when all of the following are confirmed for each word:

- Session B JSON produced: wa-{nnn}-{word}-json-{date}.json ✓
- Analysis completion patch produced and applied: PATCH-{date}-{nnn}-SESSIONB-V1.json ✓
- Final registry extract produced: wa-{nnn}-{word}-final-{date}.json ✓
- Session D pointers file produced: wa-{nnn}-{word}-sdpointers-{date}.json ✓

Once all four outputs are confirmed per word, produce a final status patch to advance `session_b_status` to `Session B Complete`:

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-SESSIONB-COMPLETE-V1",
    "registry_id": 0,
    "word": "{word}",
    "pool_id": "{pool_id}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-SessionB-Extraction-Instruction-v5.4",
    "patch_type": "SESSIONB",
    "session_b_status": "Session B Complete",
    "description": "Session B extraction complete — all outputs produced — registry {nnn} — {word}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "registry_note",
      "description": "Session B Complete — JSON: wa-{nnn}-{word}-json-{date}.json | Final: wa-{nnn}-{word}-final-{date}.json | SDPointers: wa-{nnn}-{word}-sdpointers-{date}.json"
    },
    {
      "op_id": "OP-LAST",
      "operation": "update_registry",
      "registry_no": 0,
      "set": { "session_b_status": "Session B Complete" },
      "description": "Session B fully complete — pool {pool_id}"
    }
  ],
  "_patch_summary": {
    "total_operations": 2,
    "registry_notes": 1,
    "update_registry": 1
  }
}
```

Submit this patch to Claude Code after all four outputs per word are confirmed. Claude Code applies it and confirms `session_b_status = Session B Complete`.

**If the SESSIONB-COMPLETE patch is rejected:** The four outputs have already been produced and confirmed — the only missing element is the status advance. Produce a REPAIR failure patch (naming: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1`; one registry_note recording the failure). Report to researcher. The corrected SESSIONB-COMPLETE patch requires only a new patch_id — all other content remains the same.

```
Extraction v5.4 complete.
Pool: {pool_id}
Words processed: {n} — {list}

Outputs per word:
  {nnn} — {word}:
    Session B JSON: wa-{nnn}-{word}-json-{date}.json ✓
    Analysis completion patch applied: PATCH-{date}-{nnn}-SESSIONB-V1.json ✓
    Final extract: wa-{nnn}-{word}-final-{date}.json ✓
    SD pointers: wa-{nnn}-{word}-sdpointers-{date}.json ✓
    Session B Complete patch applied: PATCH-{date}-{nnn}-SESSIONB-COMPLETE-V1.json ✓
    session_b_status: Session B Complete ✓
    session_b_revision_candidates: {n — note any non-empty}
  [repeat]

Pool {pool_id} extraction complete. All words at Session B Complete.
Intra-pool observations: captured in key_findings (finding_type: pool_observation) and pool_observations blocks.
Cross-pool SD pointers: {n total across pool}.
```

---

## 10. Researcher Compliance Rules

| **⚠ Do not re-analyse or re-interpret during Session B JSON extraction. The JSON captures what the narrative says.** |
|---|

| **⚠ SD pointer boundary: intra-pool cross-word observations are Session B findings. They belong in key_findings with `finding_type = "pool_observation"` and in the pool_observations block. They must NOT appear in the session_d_pointers array or sdpointers file. Only cross-pool and whole-programme observations are SD pointers.** |
|---|

| **⚠ Narrative sync is mandatory. Any gap between narrative and JSON outputs goes into session_b_revision_candidates — not silently into the outputs.** |
|---|

Additional compliance rules:
- If the narrative is unclear on a point, note it as an extraction flag — do not resolve it analytically
- Do not add findings that are not in the narrative
- Do not modify evidential status assignments from the narrative
- SD pointer synthesis_questions expand what is in the narrative — they do not introduce new cross-registry claims
- also_in_registries must always resolve to {registry_id, word} pairs — never plain IDs
- also_in_registries in sdpointers must only contain registries outside this pool
- session_b_revision_candidates must always be present in the final extract — empty array if no candidates, never omitted
- Data quality flags are carried to sdpointers only when analytically relevant to Session D and cross-pool in significance

---

## Annexure A — Session B JSON Template

File naming: `wa-{nnn}-{word}-json-{YYYYMMDD}.json`

```json
{
  "meta": {
    "json_template_version": "session_b_json_v1.1",
    "json_filename": "wa-{nnn}-{word}-json-{YYYYMMDD}.json",
    "analysis_filename": "wa-{nnn}-{word}-analysis-{YYYYMMDD}.md",
    "analysis_date": "{YYYYMMDD}",
    "json_date": "{YYYYMMDD}",
    "pool_id": "{pool_id}",
    "pool_approach": "{simultaneous or word_by_word_fallback}",
    "chat_session_ref": "{ref or null}",
    "session_b_instruction_version": "WA-SessionB-Analysis-Instruction-v5.2",
    "patch_type": "SESSIONB",
    "patch_status": "pending"
  },
  "registry": {
    "registry_id": "{nnn}",
    "word_label": "{word}",
    "pool_id": "{pool_id}",
    "active_term_count": 0,
    "xref_term_count": 0,
    "total_anchor_verses": 0,
    "session_b_status": "Analysis Complete",
    "cluster_assignment": "{cluster_id}"
  },
  "terms": [
    {
      "strongs_id": "{H/Gnnnn}",
      "transliteration": "{text}",
      "language": "{Hebrew or Greek}",
      "mti_status": "{status}",
      "anchor_verse_count": 0,
      "related_verse_count": 0,
      "term_inv_id": 0,
      "evidential_status": "{status}",
      "retention_note": null
    }
  ],
  "xref_terms": [
    {
      "strongs_id": "{H/Gnnnn}",
      "transliteration": "{text}",
      "gloss": "{text}",
      "owner_registry_id": 0,
      "owner_word": "{word}",
      "contextual_groups_used": ["{group_code}"]
    }
  ],
  "dimensions": {
    "relational_environment": { "present": false, "note": null },
    "spirit_soul_body": { "present": false, "note": null },
    "inner_operations": { "present": false, "note": null },
    "being": { "present": false, "note": null }
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
      "anchor_verses": [],
      "finding_type": "{etymology/verse_pattern/term_behaviour/theological_note/anomaly/pool_observation}"
    }
  ],
  "data_flags": [],
  "session_d_pointers": [
    {
      "pointer_id": "{nnn}-SD001",
      "pointer_type": "{scope_boundary/structural_observation/evidential_uncertainty/data_quality_impact}",
      "strongs_id": "{H/Gnnnn or null}",
      "cross_registry_ids": [],
      "note": "{structural observation from narrative Section 10}"
    }
  ]
}
```

---

## Annexure B — Analysis Completion Patch Template

File naming: `PATCH-{YYYYMMDD}-{nnn}-SESSIONB-V1.json`

Note: this is the FULL analytical data patch produced by the Extraction session. It is distinct from the lightweight ANALYSIS-type patch produced by the Analysis session (PATCH-{date}-{nnn}-ANALYSIS-V1.json). Both use patch_type SESSIONB but have different patch_id infixes and different operations.

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-SESSIONB-V1",
    "registry_id": 0,
    "word": "{word}",
    "pool_id": "{pool_id}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-SessionB-Extraction-Instruction-v5.5",
    "patch_type": "SESSIONB",
    "session_b_status": "Analysis Complete",
    "description": "Session B extraction — full analytical data — registry {nnn} — {word} — pool {pool_id}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "update_evidential_status",
      "table": "wa_term_inventory",
      "term_inv_id": 0,
      "strongs_number": "{H/Gnnnn}",
      "set": {
        "evidential_status": "{confirmed/plausible/uncertain/instrumental/relational_only}",
        "retention_note": "{note or null}"
      },
      "description": "{strongs_number}: evidential_status={status} — OWNER term only"
    },
    {
      "op_id": "OP-N",
      "operation": "insert",
      "table": "wa_session_b_dimensions",
      "record": {
        "registry_id": 0,
        "file_id": 0,
        "relational_environment": false,
        "relational_environment_note": null,
        "spirit_soul_body": false,
        "spirit_soul_body_note": null,
        "inner_operations": false,
        "inner_operations_note": null,
        "being": false,
        "being_note": null,
        "raised_date": "{yyyy-mm-dd}",
        "session_b_instruction": "WA-SessionB-Analysis-Instruction-v5.4"
      },
      "description": "Dimensional profile for registry {nnn}"
    },
    {
      "op_id": "OP-N",
      "operation": "update_registry",
      "registry_no": 0,
      "set": {
        "sb_classification": "{classification}",
        "sb_classification_reasoning": null,
        "carry_forward": 1
      },
      "description": "Inner being standing for registry {nnn}"
    },
    {
      "op_id": "OP-N",
      "operation": "insert",
      "table": "wa_session_b_findings",
      "record": {
        "finding_id": "{nnn}-F001",
        "registry_id": 0,
        "file_id": 0,
        "finding_type": "{type}",
        "finding": "{concise statement}",
        "anchor_verses": "{verse references}",
        "raised_date": "{yyyy-mm-dd}",
        "session_b_instruction": "WA-SessionB-Analysis-Instruction-v5.4"
      },
      "description": "{nnn}-F001 — {finding_type}"
    },
    {
      "op_id": "OP-N",
      "operation": "insert",
      "table": "wa_session_research_flags",
      "record": {
        "registry_id": 0,
        "file_id": 0,
        "flag_code": "SD_POINTER",
        "flag_label": "{nnn}-SD001",
        "strongs_reference": "{H/Gnnnn or null}",
        "cross_registry_id": 0,
        "priority": "{HIGH/MEDIUM/LOW}",
        "session_target": "D",
        "description": "{structural observation}",
        "session_raised": "WA-SessionB-Extraction-Instruction-v5.5",
        "raised_date": "{yyyy-mm-dd}",
        "resolved": 0
      },
      "description": "{nnn}-SD001 — SD_POINTER (cross-pool)"
    },
    {
      "op_id": "OP-N",
      "operation": "update_registry",
      "registry_no": 0,
      "set": {
        "dimensions": "{comma-delimited values from WA-Reference Section 4.3}",
        "description": "{Session B confirmed description of inner-being characteristic}"
      },
      "description": "Session B registry fields — dimensions and description for registry {nnn}"
    },
    {
      "op_id": "OP-LAST",
      "operation": "update_registry",
      "registry_no": 0,
      "set": { "session_b_status": "Analysis Complete" },
      "description": "Session B extraction complete — registry {nnn} — {word}"
    }
  ],
  "_patch_summary": {
    "total_operations": 0,
    "update_evidential_status": 0,
    "insert_session_b_dimensions": 1,
    "update_registry_sb_classification": 1,
    "insert_session_b_findings": 0,
    "insert_sd_pointer_flags": 0,
    "update_registry_dimensions_description": 1,
    "update_registry_status": 1
  }
}
```

---

## Annexure C — Final Registry Extract Template

File naming: `wa-{nnn}-{word}-final-{YYYYMMDD}.json`

```json
{
  "meta": {
    "json_template_version": "final_v1.1",
    "json_filename": "wa-{nnn}-{word}-final-{YYYYMMDD}.json",
    "registry_id": "{nnn}",
    "word": "{word}",
    "pool_id": "{pool_id}",
    "cluster_assignment": "{cluster_id}",
    "produced_date": "{YYYYMMDD}",
    "session_b_instruction_version": "WA-SessionB-Analysis-Instruction-v5.2",
    "extraction_instruction_version": "WA-SessionB-Extraction-Instruction-v5.4"
  },
  "registry_summary": {
    "word_label": "{word}",
    "dimensions": "{comma-delimited dimension values}",
    "cluster_assignment": "{cluster_id}",
    "pool_id": "{pool_id}",
    "phase1_term_count": 0,
    "phase1_verse_count": 0,
    "owner_term_count": 0,
    "xref_term_count": 0,
    "total_anchor_verses": 0,
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
      "confirmed_anchor_count": 0,
      "plausible_anchor_count": 0,
      "uncertain_anchor_count": 0,
      "dominant_terms": [
        {
          "strongs_id": "{H/Gnnnn}",
          "transliteration": "{text}",
          "anchor_verse_count": 0,
          "evidential_status": "{status}"
        }
      ]
    }
  },
  "terms": [
    {
      "strongs_id": "{H/Gnnnn}",
      "transliteration": "{text}",
      "language": "{Hebrew or Greek}",
      "mti_status": "{status}",
      "anchor_verse_count": 0,
      "evidential_status": "{status}",
      "retention_note": null
    }
  ],
  "xref_terms": [
    {
      "strongs_id": "{H/Gnnnn}",
      "transliteration": "{text}",
      "gloss": "{text}",
      "owner_registry_id": 0,
      "owner_word": "{word}",
      "contextual_groups_used": ["{group_code}"]
    }
  ],
  "pool_observations": [
    {
      "observation_id": "{nnn}-PO001",
      "other_word": "{word}",
      "other_registry_id": 0,
      "observation": "{what was observed about how this word relates to the other word within the pool}"
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
      "anchor_verses": [],
      "finding_type": "{etymology/verse_pattern/term_behaviour/theological_note/anomaly/pool_observation}"
    }
  ],
  "session_b_revision_candidates": []
}
```

---

## Annexure D — Session D Pointers Template

File naming: `wa-{nnn}-{word}-sdpointers-{YYYYMMDD}.json`

**Note:** This file contains cross-pool and whole-programme observations only. Intra-pool observations are in the final registry extract pool_observations block and key_findings.

```json
{
  "meta": {
    "json_template_version": "sdpointers_v1.1",
    "json_filename": "wa-{nnn}-{word}-sdpointers-{YYYYMMDD}.json",
    "registry_id": "{nnn}",
    "word": "{word}",
    "pool_id": "{pool_id}",
    "cluster_assignment": "{cluster_id}",
    "produced_date": "{YYYYMMDD}",
    "extraction_instruction_version": "WA-SessionB-Extraction-Instruction-v5.4",
    "scope_note": "Cross-pool and whole-programme observations only. Intra-pool observations are in the final registry extract."
  },
  "registry_context": {
    "sb_classification": "{classification}",
    "dimensions": "{comma-delimited}",
    "confirmed_count": 0,
    "plausible_count": 0,
    "pool_id": "{pool_id}",
    "pool_words": ["{word}", "{word}"],
    "dominant_terms": [
      {
        "strongs_id": "{H/Gnnnn}",
        "transliteration": "{text}",
        "anchor_verse_count": 0,
        "evidential_status": "{status}"
      }
    ]
  },
  "pointers": [
    {
      "pointer_id": "{nnn}-SD001",
      "pointer_type": "{scope_boundary/structural_observation/evidential_uncertainty/data_quality_impact}",
      "significance": "{HIGH/MEDIUM/LOW}",
      "strongs_id": "{H/Gnnnn or null}",
      "also_in_registries": [
        { "registry_id": 0, "word": "{word}" }
      ],
      "synthesis_questions": [
        "{concise question Session D is asked to investigate}"
      ],
      "research_depth_required": "{SURFACE/STANDARD/DEEP}",
      "prose_note": "{fuller explanation — reasoning, nuance, open questions from narrative}",
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
    "by_type": {
      "scope_boundary": 0,
      "structural_observation": 0,
      "evidential_uncertainty": 0,
      "data_quality_impact": 0
    },
    "by_significance": { "HIGH": 0, "MEDIUM": 0, "LOW": 0 },
    "registries_implicated": [
      { "registry_id": 0, "word": "{word}" }
    ],
    "open_synthesis_questions": 0
  }
}
```

---

*WA-SessionB-Extraction-Instruction-v5.6 | 20260330 | Supersedes v5.5-20260330 | Section 6.3: failure patch rule for SESSIONB rejection; Section 9: failure patch rule for SESSIONB-COMPLETE rejection*
