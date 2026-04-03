# WA-SessionB-DataPrep-Instruction-v5_4-20260329

**Framework B — Soul Word Analysis Programme**

**Session B Data Preparation Instruction**

Version 5.4 | March 2026 | Status: Active governing instruction

| **Document** | **Value** |
|---|---|
| Filename | WA-SessionB-DataPrep-Instruction-v5.6-20260330.md |
| Supersedes | WA-SessionB-DataPrep-Instruction-v5.5-20260330.md |
| Change note | v5.6 — Section 4.2: Ready for Analysis documented as legacy state — not the expected pre-DataPrep state for existing registries; treat as equivalent to Verse Context Reset. Section 8 step 6: failure patch rule added — if PREANALYSIS patch is rejected by applicator, produce a REPAIR failure patch before retrying. |
| Companion documents | WA-VerseContext-Instruction-v1.2 │ WA-SessionB-Analysis-Instruction-v5.3 │ WA-SessionB-Extraction-Instruction-v5.4 │ WA-Reference-v5.3 |
| Claude AI role | Classification decisions, scope judgements, ambiguity resolution |
| Claude Code role | Patch application, database updates, JSON re-export, validation queries, pool assembly trigger |
| Interaction model | Interactive — Claude AI and Claude Code operate in sequence with explicit handoff points |

---

## 0. Purpose and Scope

This document governs the data preparation phase that must be completed before any Session B Analysis can begin for a registry. It defines the shared and interactive operation between Claude AI and Claude Code that ensures the term inventory is clean, classified, and ready for analysis.

Data preparation covers: loading and validating the post-Verse-Context word JSON export; classifying unclassified terms; resolving data anomalies; producing and applying the pre-analysis patch; re-exporting the corrected JSON; and confirming readiness for pool assembly.

| This document is self-standing. It does not rely on session memory. It requires two inputs: this document and the word JSON export. |
|---|

---

## 0.1 Pipeline Orientation — Where DataPrep Sits

**Before DataPrep begins, the following has already happened:**

1. **Phase 1 (Session A)** — STEP extraction and audit_word have run. All terms are in the database. All verse records are present and linked via `mti_term_id`. The full word JSON export was produced by audit_word step A11.

2. **Verse Context (Stage 1)** — Claude AI has classified all OWNER terms programme-wide. Every active OWNER term now has `verse_context_group` and `verse_context` records in the database. Anchor verses are designated. The registry's `verse_context_status` was advanced to `Complete` by Claude Code. Claude Code re-exported the full word JSON — this re-export is the input to DataPrep.

3. **What the input export contains at this point:**
   - Registry meta: `session_b_status = Verse Context Reset`, `verse_context_status = Complete`
   - Full term inventory — all terms with their current mti_status (many still NULL from Phase 1)
   - Full verse corpus — all verse records (OWNER verses active, XREF verses delete_flagged)
   - Existing flags from Phase 1 audit
   - Note: the export does not contain verse_context records as a nested field — those live in the database and are queryable. The export confirms via `verse_context_status = Complete` that Verse Context is done.

**What DataPrep does:**
DataPrep's job is to clean and classify the term inventory. At the end of DataPrep, every term in the registry has a deliberate mti_status (extracted, extracted_thin, delete, xref, etc.) — no term is left at NULL. The registry is marked `Pre-Analysis Complete`.

**What DataPrep's output feeds:**
When a registry reaches `Pre-Analysis Complete`, it is ready for Session B Analysis. But Analysis does not begin immediately per registry — it begins per pool. Claude Code monitors all registries in a pool and assembles the pool analysis dataset only when all words in the pool have reached `Pre-Analysis Complete`. DataPrep completion is therefore the trigger for pool assembly monitoring, not for Analysis directly.

**The full pipeline at this point:**
```
Verse Context complete (verse_context_status = Complete)
  │
  ▼ [Claude Code re-exports full word JSON]
Session B DataPrep (this document)
  │
  ▼ [Claude AI classifies terms → patch → Claude Code applies → Pre-Analysis Complete]
Pool assembly monitoring by Claude Code
  │
  ▼ [When all words in pool reach Pre-Analysis Complete]
Session B Analysis (WA-SessionB-Analysis-Instruction-v5.2)
```

---

## 1. The Two-System Model

| **System** | **Role in data preparation** |
|---|---|
| Claude AI | Reads the JSON export. Performs all classification decisions — which terms are in scope, which are delete, which are uncertain. Identifies data anomalies. Produces the patch file. Makes all judgements about term relevance and scope. |
| Claude Code | Receives the patch file. Applies patch operations to bible_research.db. Re-exports the corrected JSON. Runs validation queries to confirm the patch was applied correctly. Monitors pool completion — triggers pool assembly when all words in a pool reach Pre-Analysis Complete. Does not make classification decisions. |

| **⚠ Claude Code does not classify terms, make scope decisions, or assess analytical relevance. All classification is Claude AI's responsibility.** |
|---|

---

## 2. Required Inputs

| **Input** | **Source and purpose** |
|---|---|
| This document (WA-SessionB-DataPrep-Instruction-v5.4) | Governs all data preparation behaviour |
| Word JSON export — wa-{nnn}-{word}-extract-{date}.json | Post-Verse-Context re-export produced by Claude Code when `verse_context_status` was advanced to Complete. Contains: registry meta (including both status fields), full term inventory, verse corpus, Phase 1 flags. This is the same `full` scope export format produced by audit_word — it is not a new export type. |

**How to confirm the export is the correct post-Verse-Context version:** The export's meta tag must show `verse_context_status = Complete`. If it shows `In Progress` or `NULL`, this is a stale export from before Verse Context ran. Do not proceed — request a fresh export from Claude Code.

---

## 3. Startup Sequence

- Read this instruction document in full.

- Load and parse the word JSON export. Confirm registry number, word label, term count, verse count.

- Read `session_b_status` AND `verse_context_status` from the JSON meta tag. Validate both against Section 4.

- Run the Pre-Analysis Data Check (Section 5).

- State the startup summary before any other output.

| Startup summary format: 'DataPrep v5.3 startup complete. Registry [no] — [word]. Terms: [n] total, [n] active, [n] with mti_status NULL. Verses: [n] total ([n] OWNER active). session_b_status: [status]. verse_context_status: [status]. Data check findings: [PASS / list issues]. Ready to proceed.' |
|---|

---

## 4. Registry Status Validation

Both `session_b_status` and `verse_context_status` must be checked before proceeding.

### 4.1 verse_context_status gate — check first

| **verse_context_status** | **Required action** |
|---|---|
| NULL | Phase 1 excluded or zero-term registry. DataPrep is not applicable. Report to researcher. |
| In Progress | Verse Context is not yet complete for this registry. **Stop immediately.** DataPrep cannot begin until `verse_context_status = Complete`. Request fresh export from Claude Code once Verse Context completes. |
| Complete | Verse Context is complete. Proceed to session_b_status check. |

| **⚠ DataPrep must not begin unless `verse_context_status = Complete`. This gate is mandatory. Do not proceed if verse_context_status is NULL or In Progress.** |
|---|

### 4.2 session_b_status check

| **session_b_status** | **Required action** |
|---|---|
| NULL or absent | No Session B work started. Proceed with data preparation normally. |
| Verse Context Reset | This is the expected state for all current active registries. Prior Session B work has been superseded (intentional programme-wide reset). Treat as a fresh start — proceed normally. Note in the patch description that this is a reset analysis. |
| Ready for Analysis | **Legacy state** — this value is set by audit_word COALESCE only when session_b_status was previously NULL. It is not the expected pre-DataPrep state for any current active registry (all 181 active registries start at Verse Context Reset). If encountered: treat as equivalent to Verse Context Reset and proceed normally. Do not treat as an error. |
| Pre-Analysis Complete | Term classifications already applied. Do not produce a new pre-analysis patch. Report to researcher — this registry is ready for pool assembly. |
| Analysis Complete | Session B analysis already applied. Data preparation is not required. Report to researcher. |
| Session B Complete | Full Session B cycle done. Report to researcher. Do not run data preparation again. |

| **⚠ If session_b_status is Pre-Analysis Complete or higher, stop immediately. Do not produce a pre-analysis patch. Duplicate patches will be rejected by the applicator and may corrupt registry state.** |
|---|

---

## 5. Pre-Analysis Data Check

On loading the JSON export, perform these checks before any other work. Report all findings before proceeding.

### 5.1 Required Checks

- Term count and verse count match the statistics block in the JSON export

- Registry status from meta tag is consistent with the work requested (Section 4)

- Identify all terms with mti_status = NULL — these require classification before analysis

- Identify any terms with delete_flagged = 1 but mti_status = extracted — contradictory state requiring decision

- Identify any terms where verse count in export substantially exceeds occurrence_count — possible sub-gloss contamination

- Note any terms with HIGH_FREQUENCY_ANCHOR flag or coverage below 20% — PH2_VOLUME_LIMITATION flag required

- Note any terms with mti_status = candidate_delete — researcher decision required before analysis

- Note any XREF terms (mti_status = xref_{word} or term_owner_type = XREF) — confirm they are correctly flagged and require no classification

### 5.2 Reporting Findings

```
Data check complete.
  NULL-status terms requiring classification: [n] — [list strongs numbers]
  Contradictory state (delete_flagged + extracted): [n] — [list]
  Possible contamination (verse count >> occurrence_count): [n] — [list]
  Volume limitation candidates: [n] — [list]
  Candidate delete terms (researcher decision needed): [n] — [list]
  XREF terms (no classification needed): [n] — [list]

Recommended action: PROCEED with classification / STOP — researcher input required for [list items]
```

| **⚠ If any finding cannot be resolved without researcher input, stop and report. List all unresolvable findings together rather than stopping sequentially.** |
|---|

---

## 6. Term Classification

All terms with mti_status = NULL must be classified before analysis can proceed.

| **Status** | **When to assign** |
|---|---|
| extracted | Term is genuine vocabulary for this registry. Include in Session B analysis. |
| extracted_thin | Term is relevant but data is thin — few verses or limited gloss. Include with caution note. |
| extracted_theological_anchor | Term is the primary theological anchor for this registry. Treat as equivalent to extracted — include in Session B analysis. Do not reclassify. If a term arrives with this status already set, leave it unchanged. |
| delete | Term is confirmed bleed, peripheral, or non-registry vocabulary. Exclude. |
| candidate_delete | Term is likely bleed but not yet confirmed. Flag for researcher decision. |
| xref_{word} | Term belongs primarily to another registry. Example: xref_anger, xref_shame. |
| phase2_enrichment | Term needs deeper research before classification can be made. |

### 6.1 Classification Method

- Read the term's gloss and occurrence count.

- If classification is uncertain from gloss alone, read a sample of the term's verses.

- Do not classify as delete on gloss alone when analytical relevance is uncertain.

- Where a term's scope is genuinely ambiguous, present evidence and options to the researcher. Do not decide unilaterally.

| The retention default applies: a missed inclusion is more costly than an over-inclusion. If in doubt, classify as extracted_thin or candidate_delete rather than delete. |
|---|

### 6.2 XREF terms

Terms already carrying `term_owner_type = XREF` in the export require no classification decision — their mti_status reflects the OWNER registry's classification. Confirm they are correctly showing as XREF and note them in the data check. Do not reclassify XREF terms.

---

## 7. Patch File Production

### 7.1 When to Produce a Patch

A pre-analysis patch is produced when any of the following are true:

- One or more terms have mti_status = NULL requiring classification
- One or more terms have contradictory state (delete_flagged = 1, mti_status = extracted)
- One or more terms require restore_delete_flagged operations
- One or more PH2 research flags need to be inserted

If none of the above apply — the term inventory is already fully classified and clean — a minimal status-only patch is still required to advance `session_b_status` to `Pre-Analysis Complete`. Produce the following patch:

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-PREANALYSIS-V1",
    "registry_id": 0,
    "word": "{word}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-SessionB-DataPrep-Instruction-v5.4",
    "session_b_status": "Pre-Analysis Complete",
    "description": "Pre-analysis status advance — no term changes required — registry {nnn} — {word}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "registry_note",
      "description": "DataPrep complete — term inventory already classified — no changes required"
    },
    {
      "op_id": "OP-LAST",
      "operation": "update_registry",
      "registry_no": 0,
      "set": { "session_b_status": "Pre-Analysis Complete" },
      "description": "DataPrep complete — no term changes — advancing status"
    }
  ],
  "_patch_summary": {
    "total_operations": 2,
    "registry_notes": 1,
    "update_registry": 1
  }
}
```

### 7.2 Patch File Structure

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{registry_no}-PREANALYSIS-V1",
    "registry_id": 0,
    "word": "{word}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-SessionB-DataPrep-Instruction-v5.4",
    "session_b_status": "Pre-Analysis Complete",
    "description": "Pre-analysis classification patch for registry {nnn} — {word}"
  },
  "operations": [],
  "_patch_summary": {
    "total_operations": 0,
    "update_mti_status": 0,
    "restore_delete_flagged": 0,
    "insert_research_flags": 0,
    "update_registry": 1
  }
}
```

| **⚠ session_b_status is required in every patch's _patch_meta. Patches without it are rejected by the applicator.** |
|---|

### 7.3 Patch File Naming

```
PATCH-{YYYYMMDD}-{nnn}-PREANALYSIS-V1.json
For multiple patches in one session, append -V2, -V3 etc.
```

### 7.4 Operation Types — Automated

#### update_mti_status

```json
{
  "op_id": "OP-001",
  "operation": "update_mti_status",
  "strongs_number": "H2617",
  "term_inv_id": 1234,
  "new_status": "extracted",
  "description": "Classified as in-scope — core chesed vocabulary"
}
```

**XREF rule:** Do not produce update_mti_status operations for XREF terms in this registry. update_mti_status matches on strongs_number programme-wide (patch_specification Section 3.1) — it updates the mti_terms record shared across all registries. XREF terms' mti_terms.status reflects the OWNER registry's classification and must not be overwritten by a DataPrep patch from a different registry. Only produce update_mti_status for terms where term_owner_type = 'OWNER' in this registry's wa_term_inventory.

**Distinction from update_evidential_status:** update_mti_status writes mti_terms.status — a programme-wide term classification shared across all registries. update_evidential_status (used in the Extraction patch) writes wa_term_inventory.evidential_status — a per-word, per-registry analytical assessment on a different table. These are non-overlapping operations on different tables serving different purposes.

#### bulk_confirm_candidate_delete

```json
{
  "op_id": "OP-003",
  "operation": "bulk_confirm_candidate_delete",
  "term_inv_ids": [1238, 1239],
  "description": "Researcher confirmed delete on review"
}
```

#### insert on wa_session_research_flags

```json
{
  "op_id": "OP-004",
  "operation": "insert",
  "table": "wa_session_research_flags",
  "record": {
    "registry_id": 97,
    "file_id": 36,
    "flag_code": "PH2_VOLUME_LIMITATION",
    "flag_label": "PH2-097-001",
    "strongs_reference": "H1523",
    "priority": "MEDIUM",
    "session_target": "D",
    "description": "Insufficient verse coverage for confident analysis",
    "session_raised": "WA-SessionB-DataPrep-Instruction-v5.4",
    "raised_date": "{yyyy-mm-dd}",
    "resolved": 0
  }
}
```

#### update_registry — always the final operation

```json
{
  "op_id": "OP-010",
  "operation": "update_registry",
  "registry_no": 97,
  "set": { "session_b_status": "Pre-Analysis Complete" },
  "description": "Term classifications applied — registry {nnn} ready for pool assembly"
}
```

#### registry_note

```json
{
  "op_id": "OP-011",
  "operation": "registry_note",
  "description": "DataPrep complete — {n} terms classified, {n} flags raised"
}
```

### 7.5 Operation Types — Manual (Claude Code Intervention Required)

#### reassign_verses

```json
{
  "op_id": "OP-012",
  "operation": "reassign_verses",
  "description": "Reassign 72 verse records from H2603B to H2603A",
  "from_term_inv_id": 2574,
  "to_term_inv_id": 2566,
  "expected_count": 72,
  "post_action": "Flag NO_VERSES on source term if empty after reassignment"
}
```

#### restore_delete_flagged

```json
{
  "op_id": "OP-013",
  "operation": "restore_delete_flagged",
  "term_inv_ids": [293, 294],
  "description": "Restore H8055 and H8056 — confirmed in scope by researcher"
}
```

#### add_cross_registry_links

```json
{
  "op_id": "OP-014",
  "operation": "add_cross_registry_links",
  "links": [{"from_registry": 97, "to_registry": 42, "type_code": "SHARED_TERM"}]
}
```

#### schema_investigation_note

```json
{
  "op_id": "OP-015",
  "operation": "schema_investigation_note",
  "description": "H8057 verse count (12) substantially exceeds occurrence_count (3) — investigate contamination source"
}
```

### 7.6 Validation Rules

- patch_id must not have been previously applied
- All strongs_number values must exist in mti_terms
- All flag_label values must be unique
- All registry_no values must exist in word_registry
- session_b_status must be present in _patch_meta
- All operations execute in a single transaction — all or nothing
- update_registry setting session_b_status = Pre-Analysis Complete must be the final operation

---

## 8. The Pre-Analysis Patch Cycle

1. Load JSON export. Confirm verse_context_status = Complete (Section 2, Section 4.1).
2. Run data check (Section 5). Report findings.
3. If verse_context_status ≠ Complete, stop — return to Verse Context.
4. If session_b_status is Pre-Analysis Complete or higher, stop — report status.
5. Classify all NULL-status terms. Present scope ambiguities to researcher. Do not proceed past ambiguities unilaterally.
6. Produce pre-analysis patch. Include classification operations, restore_delete_flagged where needed, research flag inserts, registry_note, and update_registry as the final operation. If no term changes were required, produce the minimal status-only patch (Section 7.1). A patch is always produced — `session_b_status` must advance to `Pre-Analysis Complete` via patch in all cases.
7. Submit patch to Claude Code.
8. **If the patch is rejected by the applicator:** produce a REPAIR failure patch immediately (patch naming: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1`; patch_type: REPAIR; session_b_status: current unchanged value; one registry_note operation recording the failure details). Submit the failure patch to Claude Code. Report the failure to the researcher with: the rejected patch_id, the rejection reason, and the failure patch_id. Do not produce a corrected patch until the researcher has reviewed. See WA-SessionB-ClaudeCode-Instructions-v3.2 Section 16 for the failure patch template.
9. Claude Code applies patch, sets session_b_status = Pre-Analysis Complete, re-exports JSON.
10. Load corrected export. Re-run data check. Confirm all term statuses are set and verse counts are clean.
11. Confirm readiness:

```
DataPrep complete. Registry {nnn} — {word}.
  Terms classified: {n} (extracted: {n}, extracted_thin: {n}, delete: {n}, xref: {n}, other: {n})
  Research flags raised: {n}
  session_b_status: Pre-Analysis Complete
  verse_context_status: Complete

This registry is ready for pool assembly. Claude Code will assemble the pool analysis
dataset when all words in pool [{pool_id}] reach Pre-Analysis Complete.
```

---

## 9. Claude Code — Post-DataPrep Pool Assembly Monitoring

After applying a PREANALYSIS patch and confirming Pre-Analysis Complete for a registry, Claude Code checks whether all words in the registry's pool have now reached Pre-Analysis Complete.

### 9.1 Pool membership query

```sql
-- Find all words in the same pool as this registry (single-cluster pools)
SELECT wr.no, wr.word, wr.session_b_status, wr.cluster_assignment
FROM word_registry wr
WHERE wr.cluster_assignment = (
  SELECT cluster_assignment FROM word_registry WHERE no = {registry_no}
)
AND wr.session_b_status IS NOT NULL
ORDER BY wr.no;
```

**Pool membership for multi-cluster pools:** For pools that span multiple cluster assignments (e.g. Pool 1 sub-pools), the cluster_assignment query above is insufficient. Pool membership for multi-cluster pools is defined in WA-Registry-Management-Guide-v5.6 Section 7a — the pool_id controlled vocabulary table lists every pool_id with its exact word membership. Claude Code must reference Section 7a directly to derive the `{list of registry_no values in this pool}` for the readiness check below. No database column stores this — the RMG Section 7a table is the authoritative source and is sufficient for this purpose.

### 9.2 Pool readiness check

```sql
-- Are all active words in this pool at Pre-Analysis Complete or beyond?
SELECT COUNT(*) as not_ready
FROM word_registry wr
WHERE wr.no IN ({list of registry_no values in this pool})
  AND wr.session_b_status NOT IN (
    'Pre-Analysis Complete', 'Analysis Complete', 'Session B Complete'
  )
  AND wr.session_b_status IS NOT NULL;
-- If 0: pool is ready for analysis dataset assembly
```

### 9.3 When pool is ready

Report to researcher:

```
Pool [{pool_id}] — all {n} words at Pre-Analysis Complete or beyond:
  {registry_no} — {word}: {session_b_status}
  [repeat for each word in pool]

Ready to construct pool analysis dataset.
Governing instruction: WA-SessionB-Analysis-Instruction-v5.2 (for pool dataset structure)
Awaiting researcher instruction to proceed with pool assembly.
```

Pool assembly is not automatic — it proceeds on researcher instruction. The researcher confirms the pool and instructs Claude Code to build the pool analysis dataset.

---

## 10. Claude Code Interaction Protocol

### 10.1 Handoff Format

```
PATCH SUBMISSION TO CLAUDE CODE

Patch file: PATCH-{YYYYMMDD}-{nnn}-PREANALYSIS-V1.json
Registry: {nnn} — {word}

Action required:
  1. Apply patch
  2. Set session_b_status = Pre-Analysis Complete
  3. Re-export JSON as wa-{nnn}-{word}-extract-{date}.json
  4. Run validation: confirm all term statuses set, verse counts clean
  5. Check pool assembly readiness (Section 9)
  6. Report: patch applied, export produced, pool status
```

---

## 11. Known Recurring Anomalies

| **Anomaly** | **Resolution** |
|---|---|
| Particle/function word terms incorrectly extracted in Phase 1 | Classify as delete. Use bulk_confirm_candidate_delete. |
| update_registry ops not executing | Verify session_b_status is present in _patch_meta. Check applicator version. |
| Verses substantially exceeding occurrence_count | Check for sub-gloss contamination. Classify bleed terms as delete first. Use reassign_verses if contamination persists after classification. |
| delete_flagged = 1 with mti_status = extracted | Researcher decision required. Use restore_delete_flagged or update mti_status to delete per decision. |
| Export shows verse_context_status = In Progress | Export is stale — Verse Context not yet complete. Request fresh export from Claude Code after Verse Context completion. |

---

## 12. Researcher Compliance Rules

| **⚠ Do not make assumptions or guesses. When uncertain, stop, present the evidence, and ask the researcher.** |
|---|

- Batch all uncertainty questions together rather than stopping sequentially
- Label all assumptions explicitly in the output
- Do not include analytical commentary in patch files — patch files are database operations, not analysis
- Do not ask Claude Code to make classification or scope decisions
- Do not proceed past a stale export — always confirm verse_context_status = Complete before classifying

---

## Annexure A — Pre-Analysis Patch Template

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-PREANALYSIS-V1",
    "registry_id": 0,
    "word": "{word}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-SessionB-DataPrep-Instruction-v5.4",
    "session_b_status": "Pre-Analysis Complete",
    "description": "Pre-analysis classification patch for registry {nnn} — {word}{; reset analysis}" 
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "update_mti_status",
      "strongs_number": "{H/Gnnnn}",
      "term_inv_id": 0,
      "new_status": "{status}",
      "description": "{reason for classification}"
    },
    {
      "op_id": "OP-LAST",
      "operation": "update_registry",
      "registry_no": 0,
      "set": { "session_b_status": "Pre-Analysis Complete" },
      "description": "Term classifications applied — registry {nnn} ready for pool assembly"
    }
  ],
  "_patch_summary": {
    "total_operations": 0,
    "update_mti_status": 0,
    "restore_delete_flagged": 0,
    "insert_research_flags": 0,
    "update_registry": 1
  }
}
```

Note on description field: append `; reset analysis` when session_b_status was `Verse Context Reset` before this patch.

---

## Annexure B — Data Check Report Template

```
DataPrep v5.3 startup complete.
Registry: {nnn} — {word}
Export: wa-{nnn}-{word}-extract-{date}.json

Status fields:
  session_b_status: {status}
  verse_context_status: {status} ← must be Complete to proceed

Term inventory:
  Total terms: {n}
  Active (extracted/extracted_thin): {n}
  NULL-status (require classification): {n} — {list strongs numbers}
  Delete: {n}
  XREF: {n} — {list}
  Candidate delete (researcher decision needed): {n} — {list}
  Verse counts: {n} total ({n} OWNER active, {n} XREF delete_flagged)

Data check findings:
  Contradictory state (delete_flagged + extracted): {n} — {list}
  Possible contamination (verse count >> occurrence_count): {n} — {list}
  Volume limitation candidates: {n} — {list}
  Known anomalies: {describe if any}

Recommended action: PROCEED with classification / STOP — researcher input required for {list}
```

---

## Annexure C — Full Word Export JSON Structure Reference

File naming: `wa-{nnn}-{word}-extract-{YYYYMMDD}_v{N}.json`
Scope token: `full` (pre-analysis) or `final` (post-analysis complete)
Produced by: `python -m engine.engine --export-word --registry=N`

This is the Phase 1 / post-Verse-Context export that DataPrep receives. It does NOT contain verse_context records — those live only in the database. The `verse_context_status` field in the meta block confirms whether Verse Context is complete for this registry.

**Top-level structure:**

```json
{
  "_export": { "export_type, produced_date, schema_version, scope" },
  "registry": {
    "no, word, source_list, phase1_status, phase1_term_count, phase1_verse_count,
     session_b_status, verse_context_status, cluster_assignment, dimensions,
     sb_classification, carry_forward, unique_term_count, shared_term_count,
     term_sharing_ratio, description, notes"
  },
  "files": [ "array of wa_file_index records for this registry" ],
  "run_history": [ "array of engine run history records" ],
  "cross_registry_links": [ "array of wa_cross_registry_links records" ],
  "patch_history": [ "array of applied patches" ],
  "session_research_flags": [ "array of wa_session_research_flags records" ],
  "statistics": { "term_count, verse_count, quality_flag_count, etc." },
  "terms": [
    {
      "id (term_inv_id for patch operations), file_id, language, strongs_number,
       transliteration, step_search_gloss, word_analysis_gloss, occurrence_count,
       testament, delete_flagged, status_note, evidential_status, retention_note,
       term_owner_type,
       mti: { id (mti_term_id), strongs_number, transliteration, gloss, language,
              owning_registry, owning_registry_fk, owning_word, owning_part,
              word_data_reference },
       quality_flags: [ array ],
       phase2_flags: [ array ],
       meaning_parsed: { parsed meaning data },
       related_words: [ array ],
       root_family: [ array ],
       verses: [
         { id (verse_record_id), file_id, term_inv_id, reference, verse_text,
           testament, translation, book_id, chapter, verse_num, delete_flagged,
           target_word, span_strong_match, mti_term_id }
       ]"
    }
  ],
  "verse_term_links_count": 0
}
```

**Key fields used by DataPrep:**

| Field | Purpose |
|---|---|
| registry.session_b_status | Status validation (Section 4.2) |
| registry.verse_context_status | Gate check (Section 4.1) — must be Complete |
| terms[].id | term_inv_id for patch update_mti_status operations |
| terms[].strongs_number | Term identification |
| terms[].mti.status | Current mti classification (mti_terms.status) |
| terms[].delete_flagged | Contradictory state check |
| terms[].occurrence_count vs len(terms[].verses) | Contamination check |
| statistics.term_count, statistics.verse_count | Validation against meta |

**Key fields used by Extraction:**

| Field | Purpose |
|---|---|
| terms[].id | term_inv_id for update_evidential_status operations |
| files[0].id | file_id for wa_session_b_dimensions and wa_session_b_findings inserts — use Phase 1 entry; most recent produced_date if multiple entries exist |

---

*WA-SessionB-DataPrep-Instruction-v5.6 | 20260330 | Supersedes v5.5-20260330 | Section 4.2: Ready for Analysis legacy note; Section 8: failure patch rule on patch rejection*
