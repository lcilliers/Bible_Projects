**Framework B — Soul Word Analysis Programme**

**Session B Data Preparation Instruction**

Version 5.2  |  March 2026  |  Status: Active governing instruction

| **Document** | **Value** |
| --- | --- |
| Filename | WA-SessionB-DataPrep-Instruction-v5.2-20260329.md |
| Supersedes | WA-SessionB-DataPrep-Instruction-v5.1-20260327.docx |
| Change note | v5.2 — Section 4 updated: added `Verse Context Reset` and `In Progress` gate checks. DataPrep may not begin unless `verse_context_status = Complete`. Companion documents updated to reference v5.3 instruction suite. |
| Companion documents | WA-SessionB-Analysis-Instruction-v5 │ WA-SessionB-Extraction-Instruction-v5 │ WA-Reference-v5.3 │ WA-VerseContext-Instruction-v1 |
| Claude AI role | Classification decisions, scope judgements, ambiguity resolution |
| Claude Code role | Patch application, database updates, JSON re-export, validation queries |
| Interaction model | Interactive — Claude AI and Claude Code operate in sequence with explicit handoff points |

# **0. Purpose and Scope**

This document governs the data preparation phase that must be completed before any Session B analysis can begin. It defines the shared and interactive operation between Claude AI and Claude Code that ensures the term inventory is clean, classified, and ready for analysis.

Data preparation covers: loading and validating the word JSON export; classifying unclassified terms; resolving data anomalies; producing and applying the pre-analysis patch; re-exporting the corrected JSON; and confirming readiness for analysis.

| This document is self-standing. It does not rely on session memory. It requires two inputs: this document and the word JSON export. |
| --- |

# **1. The Two-System Model**

| **System** | **Role in data preparation** |
| --- | --- |
| Claude AI | Reads the JSON export. Performs all classification decisions — which terms are in scope, which are delete, which are uncertain. Identifies data anomalies. Produces the patch file. Makes all judgements about term relevance and scope. |
| Claude Code | Receives the patch file. Applies patch operations to bible_research.db. Re-exports the corrected JSON. Runs validation queries to confirm the patch was applied correctly. Does not make classification decisions. |

| **⚠  Claude Code does not classify terms, make scope decisions, or assess analytical relevance. All classification is Claude AI's responsibility.** |
| --- |

# **2. Required Inputs**

| **Input** | **Purpose** |
| --- | --- |
| This document (WA-SessionB-DataPrep-Instruction-v5.2) | Governs all data preparation behaviour |
| Word JSON export — wa-{nnn}-{word}-extract-{date}.json | Current term inventory, registry meta, session_b_status, verse_context_status, and any existing flags |

# **3. Startup Sequence**

- Read this instruction document in full.

- Load and parse the word JSON export. Confirm registry number, word label, term count, verse count.

- Read `session_b_status` AND `verse_context_status` from the JSON meta tag. Validate both against Section 4.

- Run the Pre-Analysis Data Check (Section 5).

- State the startup summary before any other output.

| Startup summary format: 'DataPrep v5.2 startup complete. Registry [no] — [word]. Terms: [n] total, [n] active, [n] with status None. Verses: [n]. session_b_status: [status]. verse_context_status: [status]. Data check findings: [PASS or list issues]. Ready to proceed.' |
| --- |

# **4. Registry Status Validation**

Both `session_b_status` and `verse_context_status` must be checked before proceeding.

## **4.1 verse_context_status gate — check first**

| **verse_context_status** | **Required action** |
| --- | --- |
| NULL | Phase 1 excluded or zero-term registry. DataPrep is not applicable. Report to researcher. |
| In Progress | Verse Context is not yet complete for this registry. **Stop immediately.** DataPrep cannot begin until `verse_context_status = Complete`. Direct researcher to complete Verse Context for all OWNER terms in this registry before returning. |
| Complete | Verse Context is complete. Proceed to session_b_status check. |

| **⚠  DataPrep must not begin unless `verse_context_status = Complete`. This gate is mandatory. Do not proceed if verse_context_status is NULL or In Progress.** |
| --- |

## **4.2 session_b_status check**

| **session_b_status** | **Required action** |
| --- | --- |
| NULL or absent | No Session B work started. Proceed with data preparation normally. |
| Verse Context Reset | Prior Session B work exists but has been superseded. Treat as NULL — proceed with data preparation as a fresh start. Note in the patch description that this is a reset analysis. |
| Ready for Analysis | Data preparation was run previously and the registry was marked ready. Check whether a pre-analysis patch has already been applied. If yes, do not re-apply. Confirm with researcher before proceeding. |
| Pre-Analysis Complete | Term classifications already applied. Do not produce a new pre-analysis patch. Proceed to analysis using WA-SessionB-Analysis-Instruction-v5. |
| Analysis Complete | Session B analysis already applied. Data preparation is not required. Report to researcher. |
| Session B Complete | Full Session B done. Report to researcher. Do not run data preparation again. |

| **⚠  If session_b_status is Pre-Analysis Complete or higher, stop immediately. Do not produce a pre-analysis patch. Duplicate patches will be rejected by the applicator and may corrupt registry state.** |
| --- |

# **5. Pre-Analysis Data Check**

On loading the JSON export, perform these checks before any other work. Report all findings before proceeding.

## **5.1 Required Checks**

- Term count and verse count match the statistics block in the JSON export

- Registry status from meta tag is consistent with the work requested (Section 4)

- Identify all terms with mti_status = None — these require classification before analysis

- Identify any terms with delete_flagged = 1 but mti_status = extracted — contradictory state requiring decision

- Identify any terms where verses_in_export substantially exceeds occurrence_count — possible sub-gloss contamination

- Note any terms with HIGH_FREQUENCY_ANCHOR flag or coverage below 20% — PH2_VOLUME_LIMITATION flag required

- Note any terms with status = candidate_delete — researcher decision required before analysis

## **5.2 Reporting Findings**

| Data check complete. - None-status terms: [n] — [list strongs numbers] - Contradictory state terms: [n] — [list] - Possible contamination: [n] — [list] - Volume limitation candidates: [n] — [list] - Candidate delete terms: [n] — [list] Proceed to classification / Stop for researcher input. |
| --- |

| **⚠  If any finding cannot be resolved without researcher input, stop and report. Do not proceed on assumptions. List all unresolvable findings together rather than stopping sequentially.** |
| --- |

# **6. Term Classification**

All terms with mti_status = None must be classified before analysis can proceed.

| **Status** | **When to assign** |
| --- | --- |
| extracted | Term is genuine vocabulary for this registry. Include in Session B analysis. |
| extracted_thin | Term is relevant but data is thin — few verses or limited gloss. Include with caution note. |
| delete | Term is confirmed bleed, peripheral, or non-registry vocabulary. Exclude. |
| candidate_delete | Term is likely bleed but not yet confirmed. Flag for researcher decision. |
| xref_{word} | Term belongs primarily to another registry. Example: xref_anger, xref_shame. |
| phase2_enrichment | Term needs deeper research before classification can be made. |

## **6.1 Classification Method**

- Read the term's gloss and occurrence count.

- If classification is uncertain from gloss alone, read a sample of the term's verses.

- Do not classify as delete on gloss alone when analytical relevance is uncertain.

- Where a term's scope is genuinely ambiguous, present evidence and options to the researcher. Do not decide unilaterally.

| The retention default applies: a missed inclusion is more costly than an over-inclusion. If in doubt, classify as extracted_thin or candidate_delete rather than delete. |
| --- |

# **7. Patch File Production**

## **7.1 When to Produce a Patch**

A pre-analysis patch is produced when any of the following are true:

- One or more terms have mti_status = None requiring classification
- One or more terms have contradictory state (delete_flagged = 1, mti_status = extracted)
- One or more terms require restore_delete_flagged operations
- One or more PH2 research flags need to be inserted

## **7.2 Patch File Structure**

| {   "_patch_meta": {     "patch_id": "PATCH-{YYYYMMDD}-{registry_no}-{type}-V{n}",     "registry_id": [integer],     "word": "[word]",     "produced_date": "[yyyy-mm-dd]",     "produced_by": "WA-SessionB-DataPrep-Instruction-v5.2",     "session_b_status": "[status value — required]",     "description": "[summary of what this patch does]"   },   "operations": [ ... ],   "_patch_summary": {     "total_operations": [n],     "update_mti_status": [n],     "insert_research_flags": [n],     "update_registry": [n]   } } |
| --- |

| **⚠  session_b_status is required in every patch's _patch_meta. Patches without it are rejected by the applicator.** |
| --- |

## **7.3 Patch File Naming**

| wa-{nnn}-{word}-patch-{YYYYMMDD}.json  For multiple patches in one session, append -V2, -V3 etc. |
| --- |

## **7.4 Operation Types — Automated**

### **7.4.1 update_mti_status**

| { "op_id": "OP-001", "operation": "update_mti_status",   "strongs_number": "H2617", "term_inv_id": 1234,   "new_status": "extracted",   "description": "Classified as in-scope — core chesed vocabulary" } |
| --- |

### **7.4.2 bulk_confirm_candidate_delete**

| { "op_id": "OP-003", "operation": "bulk_confirm_candidate_delete",   "term_inv_ids": [1238, 1239],   "description": "Researcher confirmed delete on review" } |
| --- |

### **7.4.3 insert on wa_session_research_flags**

| { "op_id": "OP-004", "operation": "insert",   "table": "wa_session_research_flags",   "record": {     "registry_id": 97, "file_id": 36,     "flag_code": "PH2_VOLUME_LIMITATION",     "flag_label": "PH2-097-001",     "strongs_reference": "H1523",     "priority": "MEDIUM", "session_target": "D",     "description": "Insufficient verse coverage for confident analysis",     "session_raised": "WA-SessionB-DataPrep-Instruction-v5.2",     "raised_date": "2026-03-29",     "resolved": 0   } } |
| --- |

### **7.4.4 update_registry**

| { "op_id": "OP-010", "operation": "update_registry",   "registry_no": 97,   "set": { "session_b_status": "Pre-Analysis Complete" },   "description": "Term classifications applied — ready for Session B analysis" } |
| --- |

### **7.4.5 registry_note**

| { "op_id": "OP-011", "operation": "registry_note",   "description": "Analysis document: wa-097-joy-analysis-20260327.docx" } |
| --- |

## **7.5 Operation Types — Manual (Claude Code Intervention Required)**

### **7.5.1 reassign_verses**

| { "op_id": "OP-012", "operation": "reassign_verses",   "description": "Reassign 72 verse records from H2603B to H2603A",   "from_term_inv_id": 2574, "to_term_inv_id": 2566,   "expected_count": 72,   "post_action": "Flag NO_VERSES on source term if empty after reassignment" } |
| --- |

### **7.5.2 restore_delete_flagged**

| { "op_id": "OP-013", "operation": "restore_delete_flagged",   "term_inv_ids": [293, 294],   "description": "Restore H8055 and H8056 — confirmed in scope by researcher" } |
| --- |

### **7.5.3 add_cross_registry_links**

| { "op_id": "OP-014", "operation": "add_cross_registry_links",   "links": [{"from_registry": 97, "to_registry": 42, "type_code": "SHARED_TERM"}] } |
| --- |

### **7.5.4 schema_investigation_note**

| { "op_id": "OP-015", "operation": "schema_investigation_note",   "description": "H8057 verse count (12) substantially exceeds occurrence_count (3) — investigate contamination source" } |
| --- |

## **7.6 Validation Rules**

- patch_id must not have been previously applied
- All strongs_number values must exist in mti_terms
- All flag_label values must be unique
- All registry_no values must exist in word_registry
- session_b_status must be present in _patch_meta
- All operations in single transaction — all or nothing

# **8. The Pre-Analysis Patch Cycle**

- Load JSON export. Validate both status fields (Section 4). Run data check (Section 5).
- If verse_context_status ≠ Complete, stop — return to Verse Context.
- If session_b_status is Pre-Analysis Complete or higher, stop.
- Classify all None-status terms. Present scope ambiguities to researcher.
- Produce pre-analysis patch. Include classification operations, restore_delete_flagged, research flag inserts, update_registry as final operation.
- Submit patch to Claude Code.
- Claude Code applies patch, updates registry status, re-exports JSON.
- Load corrected export. Re-run data check. Confirm term statuses correct and verse counts clean.
- Confirm: 'Data preparation complete. Registry [nnn] — [word] is ready for Session B analysis.'
- Handoff: proceed with WA-SessionB-Analysis-Instruction-v5.

# **9. Claude Code Interaction Protocol**

## **9.3 Handoff Format**

| PATCH SUBMISSION TO CLAUDE CODE Patch file: wa-{nnn}-{word}-patch-{date}.json Action required: Apply patch, update session_b_status to Pre-Analysis Complete, re-export JSON as wa-{nnn}-{word}-extract-{date}.json Validation: Confirm term statuses updated and verse counts clean in re-export. |
| --- |

# **10. Known Recurring Anomalies**

| **Anomaly** | **Resolution** |
| --- | --- |
| HFA particles/function words incorrectly extracted | Classify as delete. Use bulk_confirm_candidate_delete. |
| update_registry ops in PREANALYSIS patches not executing | Verify session_b_status is present in _patch_meta. Check applicator version. |
| Verses substantially exceeding occurrence_count | Check for sub-gloss contamination. Classify bleed terms as delete first. |
| delete_flagged=1 with mti_status=extracted | Researcher decision. Use restore_delete_flagged or update mti_status to delete. |

# **11. Researcher Compliance Rules**

| **⚠  Do not make assumptions or guesses. When uncertain, stop, present the evidence, and ask the researcher.** |
| --- |

- Batch all uncertainty questions together
- Label all assumptions explicitly
- Do not include analytical commentary in patch files
- Do not ask Claude Code to make classification or scope decisions

# **Annexure A — Pre-Analysis Patch Template**

| {   "_patch_meta": {     "patch_id": "PATCH-{YYYYMMDD}-{nnn}-PREANALYSIS-V1",     "registry_id": {nnn},     "word": "{word}",     "produced_date": "{yyyy-mm-dd}",     "produced_by": "WA-SessionB-DataPrep-Instruction-v5.2",     "session_b_status": "Pre-Analysis Complete",     "description": "Pre-analysis classification patch for registry {nnn} — {word}"   },   "operations": [     {       "op_id": "OP-001",       "operation": "update_mti_status",       "strongs_number": "{H/Gnnnn}",       "term_inv_id": {integer},       "new_status": "{status}",       "description": "{reason for classification}"     }   ],   "_patch_summary": {     "total_operations": 0,     "update_mti_status": 0,     "restore_delete_flagged": 0,     "insert_research_flags": 0,     "update_registry": 0   } } |
| --- |

# **Annexure B — Data Check Reporting Template**

| DataPrep v5.2 startup complete. Registry: {nnn} — {word} Active terms: {n} │ None-status terms: {n} │ Total verses: {n} session_b_status: {status} │ verse_context_status: {status}  Data check findings:   None-status terms requiring classification: {n} — {list}   Contradictory state: {n} — {list}   Possible contamination: {n} — {list}   Volume limitation candidates: {n} — {list}   Candidate delete terms: {n} — {list}   Known anomalies: {describe}  Recommended action: {PROCEED / STOP — researcher input required} |
| --- |

*WA-SessionB-DataPrep-Instruction-v5.2 | 20260329 | Supersedes v5.1-20260327*
