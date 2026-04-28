# WA-PipelineStatusReview-v2-20260330

**Project:** Framework B — Soul Word Analysis Programme
**Version:** 2.0
**Date:** 2026-03-30
**Purpose:** Holistic pipeline status lifecycle review — updated with researcher decisions from session 2026-03-30. Defines cascade reset rules for every re-run scenario, failure patch requirements, and pre-requisite conditions for each stage.
**Supersedes:** WA-PipelineStatusReview-v1-20260330.md
**Change note v2:** Researcher decisions applied — cascade reset rules defined for all four re-run scenarios; failure patch requirement established; mid-stream failure recovery defined; pre-extraction patch requirement specified. G06-A through G06-F re-assessed. New instruction update requirements identified.
**Produced by:** Claude AI — WA session 2026-03-30

---

## 1. Pipeline Stage Map — What Each Stage Owns

This section documents what each stage reads, writes, and requires. It is the factual foundation for all cascade reset rules.

### 1.1 STEP Extraction (word_study_extract.py)

**Pre-requisite:** Word registered in word_registry (no field in word_registry). STEP Bible server available.

**Reads:** STEP Bible API.

**Writes:**
- `research/discovery/{nnn}_{word}_step_data_{YYYYMMDD}.json` — raw STEP extract file only.
- Nothing is written to the database at this stage.

**Status written:** None.

**Output consumed by:** audit_word (Step A3 loads this JSON).

---

### 1.2 audit_word (Session A pipeline — Steps Pre-A1 through A11)

**Pre-requisite:**
- Word registered in word_registry.
- STEP extract JSON available (`research/discovery/`).

**Reads:** STEP extract JSON; existing database state for gap comparison (A4).

**Writes to database:**
- `wa_file_index` — file index record for this registry
- `mti_terms` — new term records; updates to existing terms (STALE_TERM)
- `wa_term_inventory` — term inventory records
- `wa_term_related_words`, `wa_term_root_family` — term metadata
- `wa_term_phase2_flags` — analytical flags (set by engine at import)
- `wa_verse_records` — verse corpus with span filtering
- `wa_data_quality_flags` — DATA_COVERAGE group only (reset and re-derived at A8)
- `word_run_state` — audit run record (A9)
- `wa_file_index` — registry and file index update (A10)

**Writes to word_registry (via COALESCE at A10):**
- `session_b_status` → `Ready for Analysis` **only if current value is NULL**. Never downgrades.

**Does NOT write:**
- `verse_context_status` (set during setup migration M18, or by VerseContext completion)
- `session_b` analytical fields (sb_classification, dimensions, description)
- `wa_term_phase2_flags` — analytical flags set by researcher patches, never by engine
- `wa_session_research_flags` — never touched by engine

**Output consumed by:** VerseContext (batch construction reads from tables written here); DataPrep (reads full JSON export produced at A11).

---

### 1.3 Verse Context

**Pre-requisite:**
- audit_word complete for the registry.
- `verse_context_status = In Progress` (set by M18 setup migration or by re-extraction reset — see Section 3).
- `session_b_status = Verse Context Reset` (or NULL for newly registered words).
- `verse_context_group` and `verse_context` tables: empty (or flagged — after a re-run reset).

**Reads:**
- `mti_terms` — OWNER terms with status extracted/extracted_thin
- `wa_term_inventory` — OWNER terms, delete_flagged = 0
- `wa_verse_records` — verse corpus
- `verse_context` — existing records (for continuation checks)

**Writes to database:**
- `verse_context_group` — contextual meaning groups per OWNER term
- `verse_context` — verse classification records (is_relevant, is_anchor, is_related, group_id)

**Writes to word_registry:**
- `verse_context_status` → `Complete` (when all OWNER terms classified and all XREFs covered)

**Does NOT write:**
- `session_b_status` (unchanged by Verse Context patches)
- Any mti_terms, wa_term_inventory, or analytical fields

**Output consumed by:** DataPrep (reads verse_context_status = Complete from export; verse_context records queried from DB).

---

### 1.4 DataPrep

**Pre-requisite:**
- `verse_context_status = Complete`
- `session_b_status`: Verse Context Reset, NULL, or Ready for Analysis (all valid)
- Full word JSON export current (produced by Claude Code after Verse Context completes)

**Reads:** Full word JSON export; DataPrep instruction.

**Writes to database (via PREANALYSIS patch):**
- `mti_terms.status` — term classifications (extracted, delete, xref, etc.) via update_mti_status
- `wa_session_research_flags` — PH2 research flag inserts
- `word_registry.session_b_status` → `Pre-Analysis Complete`

**Does NOT write:**
- `verse_context_group` or `verse_context`
- `wa_term_inventory.evidential_status` (written by Extraction only)
- Analytical fields on word_registry (dimensions, sb_classification etc.)

**Output consumed by:** Pool assembly monitoring (CC waits for all pool members to reach Pre-Analysis Complete); Analysis (reads pool analysis dataset constructed from DataPrep-classified terms).

---

### 1.5 Session B Analysis

**Pre-requisite:**
- All words in pool: `session_b_status = Pre-Analysis Complete`
- All words in pool: `verse_context_status = Complete`
- Pool analysis dataset assembled by Claude Code

**Reads:** Pool analysis dataset JSON; Analysis instruction.

**Writes to database (via ANALYSIS patch):**
- `word_registry.session_b_status` → `Analysis Complete` (via update_registry)
- `registry_note` (logging only — no data fields)

**Does NOT write:**
- Any term-level fields
- Analytical fields (these belong to Extraction)

**Output consumed by:** Extraction (reads completed narrative documents; reads post-analysis JSON export).

---

### 1.6 Session B Extraction

**Pre-requisite:**
- `session_b_status = Analysis Complete` for all words in pool
- Completed narrative documents for all words in pool
- word_registry.json current

**Reads:** Narrative documents; word JSON exports (for term_inv_ids, file_ids); pool analysis dataset; word_registry.json.

**Writes to database (via SESSIONB patch):**
- `wa_term_inventory.evidential_status` and `retention_note` — per OWNER term
- `wa_session_b_dimensions` — dimensional profile record
- `word_registry.sb_classification`, `sb_classification_reasoning`, `carry_forward`
- `word_registry.dimensions` (comma-delimited)
- `word_registry.description`
- `wa_session_b_findings` — key findings
- `wa_session_research_flags` — SD_POINTER flags
- `word_registry.session_b_status` → `Analysis Complete` (overwrite — idempotent)

**Writes via SESSIONB-COMPLETE patch:**
- `word_registry.session_b_status` → `Session B Complete`

**Output consumed by:** Session D (reads final registry extract and sdpointers files).

---

## 2. The Two Status Tracks — Complete Transition Table

### 2.1 session_b_status

| Value | Set by | Trigger | Valid previous states |
|---|---|---|---|
| NULL | word_registry INSERT | Word registration | — |
| Verse Context Reset | M18 setup migration; REPAIR patch | Programme-wide reset of prior Session B work | Any |
| Ready for Analysis | audit_word COALESCE (A10) | audit_word completes; only if current status is NULL | NULL only |
| Pre-Analysis Complete | apply_session_patch.py | PREANALYSIS patch applied | Verse Context Reset, NULL, Ready for Analysis |
| Analysis Complete | apply_session_patch.py | ANALYSIS patch (from Analysis session) or SESSIONB patch (from Extraction) | Pre-Analysis Complete |
| Session B Complete | apply_session_patch.py | SESSIONB-COMPLETE patch | Analysis Complete |

### 2.2 verse_context_status

| Value | Set by | Trigger | Valid previous states |
|---|---|---|---|
| NULL | Default; M18 for excluded/zero-term registries | Registration or exclusion | — |
| In Progress | M18 setup migration; re-extraction reset patch | Programme setup; or pre-extraction reset | NULL, Complete |
| Complete | Claude Code direct SQL | OWNER completion check + XREF coverage check both pass | In Progress |

---

## 3. Cascade Reset Rules — Re-run Scenarios

**Governing principle:** When a pipeline stage is re-run, all downstream stages must be reset to their entry conditions. Pre-requisites for each stage must be clean and current before that stage runs. A downstream re-run cannot be valid if upstream data has changed.

**All resets require a patch** — there is no silent reset. Every cascade reset is documented, traceable, and applied via a REPAIR patch before the re-run begins.

---

### 3.1 STEP Extraction Re-run

**What triggers it:** Researcher decides to re-extract from STEP Bible for a registry (new data available, prior extraction was incomplete, Strong's numbers corrected).

**Cascade scope:** Reset ALL statuses on ALL levels to Phase 1 start. The registry is treated as if it were freshly registered.

**Pre-extraction REPAIR patch required — operations:**

```
Operation 1: update_registry
  word_registry fields to reset:
  - session_b_status → NULL
  - verse_context_status → NULL
  - sb_classification → NULL
  - sb_classification_reasoning → NULL
  - carry_forward → NULL
  - dimensions → NULL
  - description → NULL
  Note: no and word are never changed.

Operation 2: delete_flag all verse_context records for all OWNER terms of this registry
  UPDATE verse_context SET delete_flagged = 1
  WHERE mti_term_id IN (
    SELECT mt.id FROM mti_terms mt
    JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.word_registry_fk = {registry_id}
    AND ti.term_owner_type = 'OWNER'
  )
  AND delete_flagged = 0

Operation 3: delete_flag all verse_context_group records for all OWNER terms of this registry
  UPDATE verse_context_group SET delete_flagged = 1
  WHERE mti_term_id IN (same subquery as Operation 2)
  AND delete_flagged = 0

Operation 4: delete_flag all wa_term_inventory records for this registry
  UPDATE wa_term_inventory SET delete_flagged = 1
  WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = {registry_id})
  AND delete_flagged = 0

Operation 5: delete_flag all wa_verse_records for this registry
  UPDATE wa_verse_records SET delete_flagged = 1
  WHERE file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = {registry_id})
  AND delete_flagged = 0

Operation 6: delete_flag all wa_session_b_dimensions, wa_session_b_findings,
  wa_session_research_flags, wa_term_inventory evidential_status records
  for this registry (reset all analytical outputs)

Operation 7: registry_note
  "STEP extraction re-run reset — all pipeline stages reset to Phase 1 start.
   Re-run STEP extraction, then audit_word, then full pipeline from VerseContext."
```

**Patch type:** REPAIR
**Patch naming:** `PATCH-{YYYYMMDD}-{nnn}-REPAIR-STEP-RERUN-V1`
**session_b_status in _patch_meta:** Retain current status (REPAIR type rule)

**After patch is applied:** Run STEP extraction. Then run audit_word. Then pipeline proceeds from Verse Context.

**Note on mti_terms:** mti_terms records are programme-wide (shared across registries). Do NOT delete_flag mti_terms records as part of this reset — other registries may share the same terms. The mti_terms.status is reset to NULL only for terms whose owning_registry_fk matches this registry AND who have no active wa_term_inventory record in any other registry.

---

### 3.2 audit_word Re-run (new Full JSON produced)

**What triggers it:** New STEP data available; correction to verse corpus; span filter re-application needed; terminology update.

**Cascade scope:** Reset ALL statuses to pre-Verse Context state. audit_word will re-populate terms and verses. Verse Context must re-run from scratch because the verse corpus has changed.

**Pre-extraction REPAIR patch required — operations:**

```
Operation 1: update_registry
  word_registry fields to reset:
  - session_b_status → Verse Context Reset
  - verse_context_status → In Progress
  - sb_classification → NULL
  - sb_classification_reasoning → NULL
  - carry_forward → NULL
  - dimensions → NULL
  - description → NULL

Operation 2: delete_flag all verse_context records for all OWNER terms of this registry
  (same SQL as Section 3.1 Operation 2)

Operation 3: delete_flag all verse_context_group records for all OWNER terms of this registry
  (same SQL as Section 3.1 Operation 3)

Operation 4: delete_flag all wa_session_b_dimensions, wa_session_b_findings,
  wa_session_research_flags (SD_POINTER and PH2 types), wa_term_inventory
  evidential_status reset for this registry

Operation 5: registry_note
  "audit_word re-run reset — verse_context and all Session B analytical outputs
   cleared. Verse Context must re-run after audit_word completes."
```

**Patch type:** REPAIR
**Patch naming:** `PATCH-{YYYYMMDD}-{nnn}-REPAIR-AUDITWORD-RERUN-V1`
**session_b_status in _patch_meta:** `Verse Context Reset`

**After patch is applied:** Run audit_word (`python -m engine.engine --mode=audit_word --registry=N`). Then pipeline proceeds from Verse Context.

**Note:** wa_term_inventory records are NOT deleted — audit_word will update them via STALE_TERM handling. The mti_terms.status fields are NOT reset by this patch — audit_word re-classification at A6b will update them. verse_context records are delete_flagged because the verse corpus may have changed — prior contextual groupings may no longer be valid.

---

### 3.3 Verse Context Re-run

**What triggers it:** Verse context classification was incorrect; anchor verses need revision; researcher requests re-classification after analytical review.

**Cascade scope:** Reset to pre-analysis state. DataPrep term classifications remain (mti_terms.status is not reset — it was set by DataPrep, not by Verse Context). All Session B analytical outputs are cleared.

**Pre-extraction REPAIR patch required — operations:**

```
Operation 1: update_registry
  word_registry fields to reset:
  - session_b_status → Verse Context Reset
  - verse_context_status → In Progress
  - sb_classification → NULL
  - sb_classification_reasoning → NULL
  - carry_forward → NULL
  - dimensions → NULL
  - description → NULL

Operation 2: delete_flag existing verse_context records for OWNER terms being re-classified
  If full re-run: all OWNER terms for this registry (same SQL as Section 3.1 Operation 2)
  If partial re-run (specific terms): targeted by mti_term_id

Operation 3: delete_flag existing verse_context_group records
  If full re-run: all groups for OWNER terms of this registry (same SQL as Section 3.1 Operation 3)
  If partial re-run: targeted by mti_term_id

Operation 4: delete_flag all wa_session_b_dimensions, wa_session_b_findings,
  wa_session_research_flags (SD_POINTER), wa_term_inventory evidential_status
  reset for this registry

Operation 5: registry_note
  "Verse Context re-run reset — verse_context records and Session B analytical
   outputs cleared. Re-run Verse Context, then proceed from DataPrep."
```

**Patch type:** REPAIR
**Patch naming:** `PATCH-{YYYYMMDD}-{nnn}-REPAIR-VC-RERUN-V1`
**session_b_status in _patch_meta:** `Verse Context Reset`

**After patch is applied:** Re-run Verse Context for the affected terms. Then re-run DataPrep (because verse_context_status was reset — DataPrep gate requires Complete again). Then Analysis and Extraction.

**Note on mti_terms:** mti_terms.status (set by DataPrep) is NOT reset by a Verse Context re-run. The term classifications are independent of verse context groupings. However, since DataPrep must re-run, the term classifications will be re-verified.

---

### 3.4 Analysis Re-run

**What triggers it:** Narrative analysis is found to be incorrect; researcher requests revision; pool composition changed; anchor verses revised after Verse Context correction.

**Cascade scope:** Reset all analysis outputs. Verse Context and DataPrep results are preserved. The registry returns to Pre-Analysis Complete — ready for Analysis to re-run.

**Pre-extraction REPAIR patch required — operations:**

```
Operation 1: update_registry
  word_registry fields to reset:
  - session_b_status → Pre-Analysis Complete
  - sb_classification → NULL
  - sb_classification_reasoning → NULL
  - carry_forward → NULL
  - dimensions → NULL
  - description → NULL

Operation 2: delete_flag wa_session_b_dimensions records for this registry

Operation 3: delete_flag wa_session_b_findings records for this registry

Operation 4: delete_flag wa_session_research_flags SD_POINTER records for this registry

Operation 5: reset wa_term_inventory.evidential_status to NULL for all OWNER terms
  of this registry

Operation 6: reset wa_term_inventory.retention_note to NULL for all OWNER terms
  of this registry

Operation 7: registry_note
  "Analysis re-run reset — all Session B analytical outputs cleared.
   session_b_status reset to Pre-Analysis Complete. Re-run Session B Analysis
   and Extraction after applying this patch."
```

**Patch type:** REPAIR
**Patch naming:** `PATCH-{YYYYMMDD}-{nnn}-REPAIR-ANALYSIS-RERUN-V1`
**session_b_status in _patch_meta:** `Pre-Analysis Complete`

**After patch is applied:** Re-run Session B Analysis (using current pool analysis dataset or re-assemble if needed). Then re-run Extraction.

---

## 4. Failure Patch Requirement

**Governing rule (from researcher decisions, session 2026-03-30):** When a pipeline process fails, a failure patch must be generated to record the failure. This creates a traceable record in the patch history and prevents the pipeline from silently continuing in an inconsistent state.

### 4.1 Failure Patch Structure

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1",
    "registry_id": 0,
    "word": "{word}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "{governing instruction and version}",
    "patch_type": "REPAIR",
    "session_b_status": "{current status — retain, do not advance}",
    "description": "PIPELINE FAILURE — {stage name} — {brief description of failure}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "registry_note",
      "description": "PIPELINE FAILURE — {stage}: {description of what failed, what was attempted, what the error was}"
    }
  ],
  "_patch_summary": {
    "total_operations": 1,
    "registry_notes": 1
  }
}
```

**The failure patch:**
- Records the failure in the patch history — queryable, traceable
- Does NOT change any status fields (REPAIR type retains current status)
- Is submitted to Claude Code for application before any other action
- Triggers a researcher notification with the failure details

### 4.2 When to produce a failure patch

| Scenario | When to produce |
|---|---|
| PREANALYSIS patch rejected by applicator | Immediately. Do not retry without producing failure patch first. |
| ANALYSIS patch rejected by applicator | Immediately. Do not produce Extraction outputs until failure is recorded. |
| SESSIONB patch rejected by applicator | Immediately. |
| SESSIONB-COMPLETE patch rejected | Immediately. |
| VERSECONTEXT patch rejected | Immediately. |
| Partial completion detected at session startup | At startup. Do not proceed until failure is recorded and researcher has reviewed. |
| All-verses-fail for a term during Verse Context | At end of batch for affected terms. |
| Mid-pool interruption during Analysis | Immediately on resuming — before attempting any further Analysis work. |

### 4.3 Patch rejection recovery procedure

When a patch is rejected:
1. Produce the failure patch (Section 4.1). Submit to Claude Code.
2. Report to researcher: the patch that failed, the rejection reason (from applicator output), and the failure patch that was applied.
3. Diagnose the rejection cause: patch_id already applied; missing session_b_status in _patch_meta; invalid strongs_number; unknown flag_label; registry_no not found.
4. Produce a corrected patch with a new patch_id (increment V1 → V2). All other content may remain the same unless the failure was in the content.
5. Submit corrected patch only after researcher has confirmed the failure patch was applied and reviewed the failure report.

---

## 5. Mid-Pool Interruption Recovery (G06-D)

**Governing rule:** When an Analysis session is interrupted mid-pool (some words have ANALYSIS patches applied, others do not), the recovery must be documented with a patch and the researcher must re-run the Analysis step after corrections.

### 5.1 Detection at startup

At the start of every Analysis session, Claude AI must check the `session_b_status` of all pool words (from the pool analysis dataset meta block). The valid entry state is `Pre-Analysis Complete` for all words. Any deviation must be treated as a system failure:

| State found at startup | Action |
|---|---|
| All words at Pre-Analysis Complete | Proceed normally. |
| Any word at Analysis Complete | Stop. Produce failure patch. Report: "Word {nnn}—{word} is already at Analysis Complete — this word was processed in a prior session. Confirm with researcher whether to re-run or skip." |
| Any word at Session B Complete | Stop. Produce failure patch. Report: "Word {nnn}—{word} has completed the full Session B pipeline. Confirm with researcher." |
| Any word at Verse Context Reset or lower | Stop. Produce failure patch. Report: "Word {nnn}—{word} has not completed DataPrep. Pool is not ready for Analysis." |
| Mixed states (some Pre-Analysis Complete, some Analysis Complete) | This is a mid-pool interruption state. Stop immediately. Produce failure patch. Do not attempt to continue. |

### 5.2 Mid-pool interruption recovery patch

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-REPAIR-MIDPOOL-V1",
    "registry_id": 0,
    "word": "{word}",
    "pool_id": "{pool_id}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-SessionB-Analysis-Instruction-v5.5",
    "patch_type": "REPAIR",
    "session_b_status": "Pre-Analysis Complete",
    "description": "Mid-pool interruption reset — Analysis session was interrupted. Resetting to Pre-Analysis Complete for re-run."
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "registry_note",
      "description": "SYSTEM FAILURE — mid-pool interruption detected. Prior Analysis session did not complete. All pool words reset to Pre-Analysis Complete. Researcher must re-run Analysis for the full pool."
    },
    {
      "op_id": "OP-LAST",
      "operation": "update_registry",
      "registry_no": 0,
      "set": { "session_b_status": "Pre-Analysis Complete" },
      "description": "Reset to Pre-Analysis Complete for Analysis re-run"
    }
  ],
  "_patch_summary": {
    "total_operations": 2,
    "registry_notes": 1,
    "update_registry": 1
  }
}
```

One patch per word that was at Analysis Complete in the interrupted pool. After all patches are applied, the researcher re-runs the full Analysis session for the pool.

---

## 6. G06-A — Ready for Analysis Alignment

**Finding from Section 2.1:** `Ready for Analysis` is set by audit_word COALESCE only when `session_b_status = NULL`. In the current programme, all 181 active registries are at `Verse Context Reset` — audit_word COALESCE does not apply. The status is therefore unreachable for existing registries via any current pipeline operation.

**Researcher decision (session 2026-03-30):** Align with the new pipeline.

**Resolution:** `Ready for Analysis` is removed from the active pipeline path for existing registries. The operative pre-DataPrep states are `Verse Context Reset` (for existing registries) and `NULL` (for newly registered words completing Phase 1 for the first time). DataPrep Section 4.2 must be updated to reflect this — `Ready for Analysis` is a legacy state from the pre-Verse-Context pipeline and is not the expected state for any current registry.

**Documents to update:**
- RMG v5.7 Section 3.3: remove `Ready for Analysis` from the pipeline diagram; show direct path `Verse Context Reset` → `Pre-Analysis Complete`
- DataPrep v5.6 Section 4.2: update the session_b_status check table to note `Ready for Analysis` is a legacy state — if encountered, treat as equivalent to `Verse Context Reset` and proceed
- patch_specification v1.5: update Section 0 status workflow to remove `Ready for Analysis` from the active path for existing registries

---

## 7. G06-E — Re-extraction Cascade Rule

**Finding:** When audit_word re-run resets a registry, verse_context_status must be reset to In Progress. If the registry was already at Pre-Analysis Complete or higher, session_b_status must also be reset.

**Resolution (from cascade reset rules Section 3.2):** The pre-extraction REPAIR patch for audit_word re-run covers this. The patch explicitly resets both status fields AND clears verse_context records AND clears analytical outputs. The cascade is enforced by the REPAIR patch — it cannot be bypassed.

**Status:** RESOLVED by Section 3.2.

---

## 8. G06-F — Completion Check Verification

**Finding:** No double-check after writing verse_context_status = Complete.

**Resolution:** Add a confirmation step to VerseContext Instruction Section 13.3: after writing `verse_context_status = Complete`, re-run the OWNER completion check query (Section 13.1) and XREF coverage check query (Section 13.2). If either returns a non-zero count, reverse the Complete write (reset to In Progress) and report the inconsistency to the researcher. This is a safety check — not a new process.

---

## 9. Updated Gap Status

| Gap ID | Description | Status after this review |
|---|---|---|
| G06-A | Ready for Analysis unreachable for existing registries | OPEN — requires RMG v5.7, DataPrep v5.6, patch_spec v1.5 updates |
| G06-B | No failure patch on patch rejection | RESOLVED — failure patch structure defined in Section 4 |
| G06-C | No recovery if ANALYSIS patch rejected | RESOLVED — failure patch at startup covers this; mid-pool check covers detection |
| G06-D | No mid-pool interruption recovery | RESOLVED — mid-pool recovery patch defined in Section 5 |
| G06-E | Re-extraction cascade on session_b_status | RESOLVED — covered by REPAIR patch in Section 3.2 |
| G06-F | No double-check after writing verse_context_status = Complete | OPEN — VerseContext v1.5 Section 13.3 update required |

---

## 10. Instruction Updates Required from This Review

| Document | Current | Target | Changes |
|---|---|---|---|
| WA-PipelineStatusReview | v1 | v2 (this document) | Complete rewrite with cascade rules and failure handling |
| WA-VerseContext-Instruction | v1.4 | v1.5 | Section 13.3: double-check after Complete; Section 11.5: reference REPAIR patch requirement before re-extraction |
| WA-SessionB-DataPrep-Instruction | v5.5 | v5.6 | Section 4.2: Ready for Analysis legacy note; Section 7 or 8: failure patch rule |
| WA-SessionB-Analysis-Instruction | v5.5 | v5.6 | Section 4.4 startup: mid-pool detection rule; Section 12: failure patch on rejection |
| WA-SessionB-Extraction-Instruction | v5.5 | v5.6 | Section 6: failure patch on rejection |
| WA-Registry-Management-Guide | v5.6 | v5.7 | Section 3.3: remove Ready for Analysis from pipeline diagram |
| WA-SessionB-ClaudeCode-Instructions | v3.1 | v3.2 | Section 14: cascade reset patch operations; REPAIR patch catalogue |
| patch_specification | v1.4 | v1.5 | Section 0: remove Ready for Analysis from active path; add REPAIR patch catalogue for cascade resets |

---

## 11. Researcher Decisions Still Required

| # | Question |
|---|---|
| R-A | The re-run REPAIR patches in Section 3 specify which fields to reset. For Sections 3.1 and 3.2: should wa_term_inventory records be delete_flagged as part of the STEP extraction and audit_word re-run resets, or should they be retained and updated by the next audit_word run (which handles STALE_TERM via gap analysis)? The STALE_TERM mechanism in audit_word A6 already handles this — which approach takes precedence? |

---

*WA-PipelineStatusReview-v2-20260330 | Supersedes v1-20260330 | Cascade reset rules for all 4 re-run scenarios; failure patch structure; mid-pool recovery; G06-B through G06-E resolved; G06-A and G06-F require further instruction updates*
