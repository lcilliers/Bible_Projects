# Patch Specification — Session B/C/D JSON Patches

**Version:** 1.9 | **Date:** 2026-04-12
**Applicator:** `scripts/apply_session_patch.py`
**Supersedes:** patch_specification v1.8 (2026-04-12)

**Change note v1.9:**
- Section 3 (Supported operations): **`wa_dimension_index` insert is not yet supported by `apply_session_patch.py`.** Until the applicator is updated, patches needing to insert new `wa_dimension_index` rows must be flagged for manual application by Claude Code. Root cause: PATCH-20260412-023-DIMASSIGN-V1 used `operation: "insert", table: "wa_dimension_index"` — the applicator did not handle it and Claude Code applied it manually. Action required: add `insert` on `wa_dimension_index` to the applicator's supported operations, or define a dedicated `insert_dimension_index` operation type. Claude AI should include the manual-application flag in the patch `_patch_meta.description` until this is resolved.

**Change note v1.8:**
- Section 3.1 (Verse Context group_id resolution): New rule added. When inserting `verse_context` records for newly created groups (groups inserted in the same patch, whose `id` is not yet known at patch-construction time), Claude AI must use a bare `group_code` string (e.g. `"1613-001"`) in the `group_id` field — not a decorated string such as `"RESOLVE:1613-001"`. The applicator's `_resolve_group_id` function expects bare group_code strings. The decorated `"RESOLVE:"` prefix is not handled and caused 23 records to fail in PATCH-20260412-023-VCREPAIR-V1, requiring manual application. Root cause: Claude AI invented a non-standard resolution prefix. Correct pattern documented below.

**Change note v1.7:**
- Section 3.2 (`update_registry`): Confusion alert added. Two distinct operation types update `word_registry`: `update_registry` (Section 3.2) uses `registry_no` as a top-level field; `update` on `word_registry` (Section 3.9) uses a `match` dict. These must not be conflated. Root cause: PATCH-20260411-001-SESSIONB-V1 used `match: {no: 23}` inside an `update_registry` operation — the applicator skipped the operation because `registry_no` was absent at top level. The operation was applied manually. This change adds an explicit confusion alert and contrast example to prevent recurrence.

**Change note v1.6:**
- Section 0.1: Governing document cross-reference table updated — VerseContext patch types (VERSECONTEXT, VCGROUP, VCVERSE) now reference WA-VerseContext-Instruction v1.7 (was v1.5).

**Change note v1.2:**
- Section 0: Status workflow updated — `Verse Context Reset` added; `Ready for Analysis` now only reachable after `verse_context_status = Complete`
- Section 1: VERSECONTEXT, VCGROUP, VCVERSE added to Types
- Section 2: Null `session_b_status` rule added for Verse Context patch types
- Section 8: New section — Verse Context patch operations (insert/update on verse_context_group and verse_context)
- Appendix A.5: `Verse Context Reset` added to valid session_b_status values
- Appendix A.6: VERSECONTEXT, VCGROUP, VCVERSE added with null session_b_status rule
- Appendix A.7: New — verse_context_status vocabulary

---

## 0. Session B Status Workflow

The `word_registry.session_b_status` column tracks each word's progress through the analysis pipeline. A parallel field `word_registry.verse_context_status` (NULL / In Progress / Complete) tracks the Verse Context stage independently.

**Active pipeline path — existing registries (all 181 current active registries start at Verse Context Reset):**

```
NULL / Verse Context Reset
  │
  ▼  (Verse Context complete for all OWNER terms → verse_context_status = Complete)
[verse_context_status = Complete — DataPrep gate open]
  │
  ▼  (pre-analysis patch applied — term classifications, bleed removal)
"Pre-Analysis Complete"
  │
  ▼  (Session B analysis patch applied — full analytical findings, PH2 flags)
"Analysis Complete"
  │
  ▼  (Session B synthesis document produced, all outputs confirmed)
"Session B Complete"
```

**Who sets each status:**

| Status | Set by | Trigger | Applies to |
|--------|--------|---------|------------|
| `NULL` | Default | Word registered but not yet extracted | All registries at registration |
| `Verse Context Reset` | Setup operation or REPAIR patch | Prior Session B work superseded — must reprocess | All 181 existing active registries at programme start |
| `Ready for Analysis` | `audit_word` COALESCE (Step A10) | audit_word completes; **only if current status is NULL** | New registries only — not applicable to existing 181 active registries |
| `Pre-Analysis Complete` | `apply_session_patch.py` | Pre-analysis patch with `session_b_status: "Pre-Analysis Complete"` | All registries via DataPrep |
| `Analysis Complete` | `apply_session_patch.py` | Session B analysis patch OR Extraction SESSIONB patch | All registries via Analysis/Extraction |
| `Session B Complete` | `apply_session_patch.py` | SESSIONB-COMPLETE patch — set by Session B Extraction output confirmation patch (WA-SessionB-Extraction-Instruction Section 9) | All registries via Extraction |

**Note on Ready for Analysis:** This status is a legacy value from the pre-Verse-Context pipeline. `audit_word` sets it via COALESCE only when `session_b_status` is currently NULL — it does not overwrite Verse Context Reset. For all 181 existing active registries, `audit_word` will not change their status from Verse Context Reset to Ready for Analysis. This status is only reachable for newly registered words completing Phase 1 for the first time. When DataPrep encounters Ready for Analysis, it treats it as equivalent to Verse Context Reset. See WA-Registry-Management-Guide-v5.7 Section 3.3.

**Rules:**
- `audit_word` uses `COALESCE` — sets `Ready for Analysis` only if current status is NULL. Never downgrades.
- `apply_session_patch.py` overwrites `session_b_status` from `_patch_meta.session_b_status` for standard patches.
- PREANALYSIS, SESSIONB, SESSIOND, CLUSTERING, and REPAIR patches MUST include `session_b_status` in `_patch_meta`. Patches without it are rejected.
- **EXCEPTION: VERSECONTEXT, VCGROUP, and VCVERSE patches carry `session_b_status: null`. The applicator MUST NOT reject these.** They do not update `session_b_status` on `word_registry`.
- **REPAIR patches** carry the current status value (no change) unless the patch explicitly resets the status as part of a cascade reset operation.
- The status value should reflect what the patch accomplishes, not what comes next.

**Typical patch sequence for a word:**

| Patch | `session_b_status` value | What it does |
|-------|--------------------------|-------------|
| `PATCH-YYYYMMDD-VCB001-VERSECONTEXT-V1` | `null` | Verse context classification — relevance filter, grouping, anchor designation |
| `PATCH-YYYYMMDD-NNN-PREANALYSIS-V1` | `Pre-Analysis Complete` | Term classifications (extracted/delete/xref), bleed removal |
| `PATCH-YYYYMMDD-NNN-ANALYSIS-V1` | `Analysis Complete` | Status advance — registry_note only |
| `PATCH-YYYYMMDD-NNN-SESSIONB-V1` | `Analysis Complete` | Full analytical data — evidential status, dimensions, findings, SD pointers |
| `PATCH-YYYYMMDD-NNN-SESSIONB-COMPLETE-V1` | `Session B Complete` | Confirms all four outputs produced |

---

## 0.1 Governing Document Cross-Reference

This table is the single navigation point from a patch type to the instruction document that governs its business logic. The patch specification governs how patches are applied (applicator rules, field requirements, operation types). The governing instruction documents govern what goes into each patch and why.

| **Patch type** | **Governing instruction** | **Current version** | **Valid `session_b_status` in `_patch_meta`** | **What the patch contains** |
|---|---|---|---|---|
| VERSECONTEXT | WA-VerseContext-Instruction | v1.7 | `null` — applicator must not reject | verse_context_group inserts; verse_context inserts/updates; full batch |
| VCGROUP | WA-VerseContext-Instruction | v1.7 | `null` | Targeted verse_context_group update |
| VCVERSE | WA-VerseContext-Instruction | v1.7 | `null` | Targeted verse_context insert or update |
| PREANALYSIS | WA-SessionB-DataPrep-Instruction | v5.6 | `"Pre-Analysis Complete"` | Term mti_status classifications; research flag inserts |
| SESSIONB | WA-SessionB-Extraction-Instruction | v5.6 | `"Analysis Complete"` or `"Session B Complete"` | Evidential status; dimensions; findings; SD pointer flags |
| REPAIR | WA-PipelineStatusReview | v2 + WA-SessionB-ClaudeCode-Instructions v3.2 | Current status value (or reset target for cascade resets) | Cascade reset operations; failure recording |
| SESSIOND | WA-SessionD-Orientation | v2.1 | `null` | Session D discovery and synthesis operations |
| CLUSTERING | WA-Implementation-Instruction | v5 | `null` | Cluster assignment updates |

**How to use this table:**
- If you are constructing a patch: find your patch type, then read the governing instruction for the business logic rules
- If you are applying a patch: the applicator rules are in this document; refer back to the governing instruction only if the applicator behaviour is ambiguous
- If you are reviewing a patch: the `produced_by` field in `_patch_meta` should name the governing instruction and version

**Cross-reference to patch index:** The patch index in WA-Reference-v5.3 Section 12 lists the same information from the Reference document's perspective — use whichever is more convenient. The two tables must remain consistent. If a new instruction version is released, update both.

---

## 1. File Naming Convention

```
PATCH-{YYYYMMDD}-{registry_no}-{type}-V{version}.json
```

Examples:
- `PATCH-20260325-061-PREANALYSIS-V1.json`
- `PATCH-20260325-182-SESSIONB-V1.json`

Types: `PREANALYSIS`, `SESSIONB`, `SESSIONC`, `SESSIOND`, `REPAIR`

**Verse Context patch types use different ID formats:**

```
PATCH-{YYYYMMDD}-VCB{batch_id}-VERSECONTEXT-V{n}.json    (batch classification)
PATCH-{YYYYMMDD}-VCGROUP{group_id}-V{n}.json              (targeted group update)
PATCH-{YYYYMMDD}-VCVERSE{verse_record_id}-V{n}.json       (targeted verse update)
```

Examples:
- `PATCH-20260329-VCB001-VERSECONTEXT-V1.json`
- `PATCH-20260329-VCGROUP47-V1.json`
- `PATCH-20260329-VCVERSE4821-V1.json`

---

## 2. File Structure

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-20260325-061-PREANALYSIS-V1",
    "registry_id": 61,
    "word": "fear",
    "produced_date": "2026-03-25",
    "produced_by": "Session B v3.0 pre-analysis",
    "session_b_status": "Pre-Analysis Complete",
    "description": "Brief summary of what this patch does"
  },
  "operations": [ ... ],
  "_patch_summary": {
    "total_operations": 12,
    "mti_updates": 8,
    "bulk_deletes": 2,
    "research_flag_inserts": 2
  }
}
```

**Required fields in `_patch_meta`:**
- `patch_id` — unique identifier (used for idempotency check in engine_run_log)
- `registry_id` — word_registry.no (integer)
- `word` — English word
- `session_b_status` — status to set on word_registry.session_b_status (REQUIRED — patch will be rejected without it)

**Valid `session_b_status` values:**
- `"Pre-Analysis Complete"` — pre-analysis patch applied, ready for Session B analysis
- `"Analysis Complete"` — Session B analysis complete, all classifications finalised
- `"Session B Complete"` — full Session B with research flags and analytical output

---

## 3. Supported Operation Types

### 3.1 `update_mti_status` — Set MTI status on a single term

The primary operation for classifying terms (extracted, delete, xref, etc.).

```json
{
  "op_id": "OP-001",
  "operation": "update_mti_status",
  "strongs_number": "H2865",
  "set": {
    "status": "extracted",
    "status_note": "Reason for classification",
    "exclusion_reason": null
  }
}
```

**Required fields:**
- `op_id` — sequential identifier (OP-001, OP-002, ...)
- `operation` — must be `"update_mti_status"`
- `strongs_number` — the Strong's code to match on
- `set` — dict of column→value pairs for mti_terms

**Valid `status` values:** `extracted`, `extracted_thin`, `delete`, `candidate_delete`, `excluded`, `phase2_enrichment`, `xref_[word]` (e.g. `xref_anger`, `xref_distress`)

**Behaviour:** Matches on `strongs_number` only (not `owning_registry_fk`). If the term has a NULL `owning_registry_fk`, it is set from the patch's `registry_id`. Non-existent columns in `set` are silently dropped. `last_changed` is auto-set.

---

### 3.2 `update_registry` — Update word_registry fields

```json
{
  "op_id": "OP-001",
  "operation": "update_registry",
  "registry_no": 61,
  "set": {
    "anchor_verses": "1 John 4:18",
    "description": "Updated description text"
  }
}
```

**Required fields:** `op_id`, `operation`, `registry_no`, `set`

**Behaviour:** Updates `word_registry WHERE no = ?`. Non-existent columns are silently dropped.

**⚠ CONFUSION ALERT — two distinct operations update `word_registry`:**

| Operation | Key field | Format | Section |
|---|---|---|---|
| `update_registry` | `registry_no` | Top-level integer field | 3.2 (this section) |
| `update` on `word_registry` | `match: {id: N}` | Match dict inside operation | 3.9 |

Do NOT use a `match` dict inside an `update_registry` operation — the applicator looks for `registry_no` at the top level and will silently skip the operation if it is absent.

**Incorrect (applicator will skip silently):**
```json
{
  "op_id": "OP-001",
  "operation": "update_registry",
  "match": { "no": 61 },
  "set": { "description": "..." }
}
```

**Correct:**
```json
{
  "op_id": "OP-001",
  "operation": "update_registry",
  "registry_no": 61,
  "set": { "description": "..." }
}
```

Use `update_registry` (Section 3.2) for simple field updates on `word_registry`. Use `update` on `word_registry` (Section 3.9) when you need the `match` dict pattern for more complex update scenarios.

---

### 3.3 `bulk_confirm_candidate_delete` — Bulk confirm candidate_delete → delete

```json
{
  "op_id": "OP-013",
  "operation": "bulk_confirm_candidate_delete",
  "description": "Confirm all candidate_delete terms as delete",
  "filter": "registry_no=183 AND mti_status=candidate_delete",
  "set": {
    "status": "delete",
    "exclusion_reason": "Bleed confirmed by researcher"
  }
}
```

**Required fields:** `op_id`, `operation`, `filter`, `set`

**`filter` format:** Must contain `registry_no=N`. The applicator parses the registry number and finds all mti_terms with `status='candidate_delete'` linked to that registry via wa_term_inventory → wa_file_index.

---

### 3.4 `bulk_update_none_to_delete` — Bulk set None-status terms to delete

Same format as `bulk_confirm_candidate_delete` but matches `status IS NULL`.

```json
{
  "op_id": "OP-006",
  "operation": "bulk_update_none_to_delete",
  "filter": "registry_no=184",
  "set": {
    "status": "delete",
    "exclusion_reason": "Cross-registry bleed confirmed"
  }
}
```

---

### 3.5 `bulk_confirm_delete_flagged` — Bulk confirm delete-flagged terms

Same format. Matches `delete_flagged=1` terms with NULL status.

```json
{
  "op_id": "OP-068",
  "operation": "bulk_confirm_delete_flagged",
  "filter": "registry_no=183 AND delete_flagged=1",
  "set": {
    "status": "delete",
    "exclusion_reason": "Already delete-flagged. Confirmed."
  }
}
```

---

### 3.6 `bulk_update_note` — Bulk update with filter or strongs list

Two sub-formats:

**Format A — Filter-based (for delete-flagged terms):**
```json
{
  "op_id": "OP-007",
  "operation": "bulk_update_note",
  "filter": "registry_no=4 AND delete_flagged=1 AND mti_status IS NULL",
  "set": {
    "status": "delete",
    "exclusion_reason": "Confirmed bleed"
  }
}
```

**Format B — Explicit strongs list:**
```json
{
  "op_id": "OP-008",
  "operation": "bulk_update_note",
  "bulk_strongs": ["G3844", "H5674A", "H6440H"],
  "set": {
    "status": "delete",
    "exclusion_reason": "Bleed family"
  },
  "xref_exceptions": {
    "H7307G": "xref_spirit — primary in spirit registry"
  }
}
```

**`xref_exceptions`:** Optional dict. For listed strongs, overrides `status` to the xref value instead of the bulk `set.status`.

---

### 3.7 `insert` on `wa_phase2_flags` / `wa_session_research_flags` — Research flag insert

```json
{
  "op_id": "OP-017",
  "operation": "insert",
  "table": "wa_session_research_flags",
  "record": {
    "registry_id": 182,
    "file_id": 36,
    "flag_code": "PH2_CROSS_REF_ENRICHMENT",
    "flag_label": "PH2-182-001",
    "strongs_reference": "H5317",
    "cross_registry_id": null,
    "priority": "MEDIUM",
    "session_target": "D",
    "description": "Detailed description of the research finding",
    "session_raised": "Session B v3.0",
    "raised_date": "2026-03-24",
    "resolved": 0
  }
}
```

**Required record fields:** `registry_id`, `flag_code`, `flag_label` (must be unique), `description`, `session_raised`, `raised_date`

**Optional record fields:** `file_id`, `strongs_reference`, `cross_registry_id`, `priority` (default MEDIUM), `session_target` (default D), `resolved` (default 0)

**`flag_label` convention:** `PH2-{registry_no}-{3-digit-sequence}` (e.g. PH2-182-001)

**Note:** Both `wa_phase2_flags` and `wa_session_research_flags` table names are accepted — both route to `wa_session_research_flags`.

---

### 3.8 `update` on `mti_terms` — Standard MTI update (Session B format)

```json
{
  "op_id": "OP-001",
  "operation": "update",
  "table": "mti_terms",
  "match": {
    "strongs_number": "G5590G",
    "owning_registry_fk": 182
  },
  "set": {
    "status": "extracted",
    "strongs_reconciled": 1,
    "status_note": "Session B confirmation"
  }
}
```

**Note:** `owning_registry_fk` in `match` is used to set the FK if currently NULL, but matching is done on `strongs_number` only.

---

### 3.9 `update` on `word_registry` — Standard registry update (Session B format)

```json
{
  "op_id": "OP-023",
  "operation": "update",
  "table": "word_registry",
  "match": { "id": 182 },
  "set": {
    "notes": "Updated notes text"
  }
}
```

---

### 3.10 `update_evidential_status` — Set evidential status on a single term (Session B Extraction format)

Targets `wa_term_inventory`. Sets `evidential_status` and `retention_note` on the term inventory record for a single term. One operation per active OWNER term in the registry. Used in the Session B Extraction analysis completion patch.

```json
{
  "op_id": "OP-001",
  "operation": "update_evidential_status",
  "table": "wa_term_inventory",
  "term_inv_id": 1234,
  "strongs_number": "{H/Gnnnn}",
  "set": {
    "evidential_status": "{confirmed/plausible/uncertain/instrumental/relational_only}",
    "retention_note": "{note or null}"
  },
  "description": "{strongs_number} {transliteration} — evidential_status: {status}"
}
```

**Required fields:** `op_id`, `operation`, `term_inv_id`, `strongs_number`, `set`
**Behaviour:** Matches on `term_inv_id` primarily; `strongs_number` is for human-readable verification. Updates `wa_term_inventory.evidential_status` and `wa_term_inventory.retention_note`. Implemented in `apply_session_patch.py`.
**Governing instruction:** WA-SessionB-Extraction-Instruction-v5.3 Section 6.1 Group A

---

### 3.10a `bulk_update` on `mti_terms` — Bulk status note updates (Session B Analysis format)

**Format A — Nested match/set:**
```json
{
  "op_id": "OP-011",
  "operation": "bulk_update",
  "table": "mti_terms",
  "records": [
    { "match": {"strongs_number": "G0014"}, "set": {"status": "delete"} }
  ]
}
```

**Format B — Flat (strongs_number + fields):**
```json
{
  "op_id": "OP-011",
  "operation": "bulk_update",
  "table": "mti_terms",
  "records": [
    { "strongs_number": "G0014", "status": "delete", "status_note": "Bleed" }
  ]
}
```

---

### 3.11 Documentation-only operations (no DB action)

These are logged to console but produce no database changes:

- **`schema_investigation_note`** — flags a data anomaly for Claude Code investigation
- **`registry_note`** — informational annotation about registry state
- **`phase1_supplement_required`** — signals that additional terms need extraction

---

### 3.12 REPAIR patch operations

REPAIR patches are used for cascade resets and failure recording. They carry `patch_type: "REPAIR"` in `_patch_meta`.

**Cascade reset patches** use standard operation types (`update_registry`, `registry_note`) with the specific field values defined in WA-PipelineStatusReview-v2-20260330 Sections 3.1–3.4. The `session_b_status` in `_patch_meta` must match the target reset state (e.g. `"Verse Context Reset"` for an audit_word re-run reset).

**Failure patches** use a single `registry_note` operation and carry the current (unchanged) `session_b_status` value. Their purpose is to record the failure in the patch history. They do not change any data fields.

**REPAIR patch naming conventions:**

| Scenario | Patch naming |
|---|---|
| STEP extraction re-run reset | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-STEP-RERUN-V1` |
| audit_word re-run reset | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-AUDITWORD-RERUN-V1` |
| Verse Context re-run reset | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-VC-RERUN-V1` |
| Analysis re-run reset | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-ANALYSIS-RERUN-V1` |
| Mid-pool interruption reset | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-MIDPOOL-V1` |
| Failure recording | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1` |

**Full cascade reset patch specifications:** WA-SessionB-ClaudeCode-Instructions-v3.2 Section 15.
**Failure patch template:** WA-SessionB-ClaudeCode-Instructions-v3.2 Section 16.

---

## 4. Operations NOT Supported by the Applicator

The following require **manual execution** by Claude Code. When these appear in a patch, include clear SQL-level instructions.

### 4.1 Verse reassignment (cross-term contamination)
```json
{
  "op_id": "OP-001",
  "operation": "reassign_verses",
  "description": "Reassign 72 verse records from H2603B → H2603A",
  "from_term_inv_id": 2574,
  "to_term_inv_id": 2566,
  "expected_count": 72,
  "post_action": "Flag NO_VERSES on source term if empty after reassignment"
}
```

### 4.2 Quality flag insertion
```json
{
  "op_id": "OP-006",
  "operation": "add_quality_flag",
  "strongs_number": "G0264",
  "term_inv_id": 2580,
  "flag_code": "HIGH_FREQUENCY_ANCHOR",
  "description": "High-frequency term: 241 occurrences, 15% coverage"
}
```

### 4.3 VTL population (missing term_links)
```json
{
  "op_id": "OP-008",
  "operation": "populate_vtl",
  "term_inv_id": 292,
  "verse_ids": [3364, 3365, 3366, 3367, 3368, 3369, 3370],
  "description": "Populate missing VTL for G0266 verses"
}
```

### 4.4 Delete-flag restoration
```json
{
  "op_id": "OP-005",
  "operation": "restore_delete_flagged",
  "term_inv_ids": [293, 294],
  "description": "Restore G1777 and G2631 — confirmed in scope"
}
```

### 4.5 Cross-registry link insertion
```json
{
  "op_id": "OP-027",
  "operation": "add_cross_registry_links",
  "links": [
    {"from_registry": 212, "to_registry": 61, "type_code": "semantic_overlap"}
  ]
}
```

---

## 5. Validation Rules

The applicator validates before applying:
1. `patch_id` has not been previously applied (checked in engine_run_log)
2. All `strongs_number` values in `update_mti_status` exist in mti_terms
3. All `flag_label` values in research flag inserts are unique
4. All `registry_no` values in registry updates exist in word_registry
5. **REPAIR patches:** `update_registry` operations that set `session_b_status` to a value it already holds are accepted without error — the overwrite is silent and idempotent. This applies to all REPAIR patches and to standard patches where the status write results in no change.

If validation fails, the entire patch is rejected. No partial application.

---

## 6. Post-Application Behaviour

- All operations run in a single transaction — all-or-nothing
- On success: patch_id logged to engine_run_log, patch file moved to `archive/patches/`
- On failure: full rollback, patch file remains in place
- `last_changed` is auto-set on all mti_terms updates
- Non-existent columns in `set` dicts are silently dropped with a console note

---

## 7. Producing Patches — Guidelines for Claude.ai

1. **Use `_patch_meta`** — always include `patch_id`, `registry_id`, `word`
2. **Use `op_id` sequencing** — OP-001, OP-002, etc.
3. **Use `operation` as the key field** — not `action` or `op_type`
4. **Use `update_mti_status`** for individual term classifications — this is the workhorse operation
5. **Use bulk operations** for confirmed bleed deletions — reduces patch size
6. **Use structured operations** (sections 3.1–3.10) wherever possible — these are auto-applied
7. **Use manual operations** (section 4) only for data repairs — these require Claude Code intervention
8. **Include `description`** on every operation — it's logged and aids debugging
9. **Include `_patch_summary`** — helps verify completeness
10. **One patch per registry per session** — don't mix registries in a single patch

---

## 8. Verse Context Patch Operations (new v1.2)

These operations apply exclusively to `verse_context_group` and `verse_context` tables. They are governed by WA-VerseContext-Instruction-v1.7. Key rules:

- All three Verse Context patch types carry `session_b_status: null` — applicator must not reject
- All corrections are UPDATE operations — no physical deletes
- `verse_context_group` inserts must precede `verse_context` inserts in the same patch
- group_code strings (e.g. `"142-001"`) in verse_context inserts are resolved to integer ids by Claude Code at apply time using `last_insert_rowid()` after each group insert

### 8.0 Group ID resolution for same-patch inserts

When a patch inserts a new `verse_context_group` and then inserts `verse_context` records belonging to that new group — all in the same patch — the group's `id` is not known at patch-construction time.

**Correct approach:** Use the bare `group_code` string as the `group_id` value:

```json
{
  "op_id": "OP-010",
  "operation": "insert",
  "table": "verse_context",
  "record": {
    "verse_record_id": 12345,
    "mti_term_id": 1613,
    "group_id": "1613-001",
    "group_code": "1613-001"
  }
}
```

The applicator's `_resolve_group_id` function accepts a bare group_code string and looks up the correct integer `id`. This lookup succeeds after the group insert operation has run earlier in the same patch.

**⚠ Do NOT use a decorated prefix such as `"RESOLVE:1613-001"`.** The resolver does not handle prefixed strings. Using a prefix causes the insert to fail and requires manual intervention. Root cause of PATCH-20260412-023-VCREPAIR-V1 failure: 23 records used `"RESOLVE:group_code"` format instead of bare group_code.

---

### 8.1 Insert new verse_context_group

```json
{
  "op_id": "OP-001",
  "operation": "insert",
  "table": "verse_context_group",
  "record": {
    "mti_term_id": 142,
    "group_code": "142-001",
    "context_description": "{brief phrase — inner-being engagement of this term in this group}",
    "notes": null,
    "delete_flagged": 0
  },
  "description": "New group for {strongs_number}: {context_description}"
}
```

### 8.2 Update existing verse_context_group

```json
{
  "op_id": "OP-002",
  "operation": "update",
  "table": "verse_context_group",
  "match": { "id": 47 },
  "set": {
    "context_description": "{revised text}",
    "notes": "{reason}",
    "delete_flagged": 0
  },
  "description": "Revised group 142-001: {reason}"
}
```

### 8.3 Insert new verse_context record

```json
{
  "op_id": "OP-003",
  "operation": "insert",
  "table": "verse_context",
  "record": {
    "verse_record_id": 4821,
    "mti_term_id": 142,
    "group_id": "142-001",
    "is_anchor": 1,
    "is_relevant": 1,
    "is_related": 0,
    "notes": null,
    "delete_flagged": 0
  },
  "description": "Gen 6:5 — anchor, group 142-001"
}
```

`group_id` may be a group_code string for new groups in the same patch. Claude Code resolves to integer id. For existing groups, use the integer id directly.

### 8.4 Update existing verse_context record

```json
{
  "op_id": "OP-004",
  "operation": "update",
  "table": "verse_context",
  "match": { "id": 892 },
  "set": {
    "group_id": 47,
    "is_anchor": 1,
    "is_relevant": 1,
    "is_related": 0,
    "notes": "{reason for reclassification}",
    "delete_flagged": 0
  },
  "description": "Gen 6:5 — reclassified to anchor, group 142-001"
}
```

### 8.5 Consistency rules (Claude Code validates after application)

| Rule | Check | Expected |
|------|-------|----------|
| R1 | is_relevant=0 rows: group_id NULL, is_anchor=0, is_related=0 | 0 violations |
| R2 | is_anchor=1 rows: is_relevant=1, is_related=0, group_id NOT NULL | 0 violations |
| R3 | is_related=1 rows: group has active anchor | 0 violations |
| R4 | Every term: at least one active is_anchor=1 row | 0 terms without anchor |

---

## Appendix A — Lookup Table Reference

Full extracts of all FK-referenced lookup tables. Use these values when constructing patches.
A machine-readable extract is available at `data/exports/lookup_tables_20260326.json`.

### A.1 wa_quality_flag_types (DATA_COVERAGE — engine-derived)

| id | flag_group | flag_code | Description |
|:--:|-----------|-----------|-------------|
| 1 | DATA_COVERAGE | NO_VERSES | No verse records found for this term |
| 2 | DATA_COVERAGE | THIN_DATA | Fewer verse occurrences than expected |
| 3 | DATA_COVERAGE | SMALL_VERSE_SAMPLE | Only a partial sample of available verses captured |
| 4 | DATA_COVERAGE | NO_WORD_ANALYSIS | No word-level analysis available |
| 23 | DATA_COVERAGE | SPAN_RESOLUTION_CONFLICT | Queried Strong's not found in any verse span |
| 24 | DATA_COVERAGE | SPAN_FILTER_APPLIED | Verse records discarded by span filter |
| 36 | DATA_COVERAGE | HIGH_FREQUENCY_ANCHOR | Term occurs 500+ times |
| 47 | DATA_COVERAGE | PROSE_ONLY_MEANING | Meaning stored as single prose block |

### A.2 phase2_flag_types (researcher-owned term-level analytical flags)

| id | flag_code | Description |
|:--:|-----------|-------------|
| 1 | GOD_AS_SUBJECT | God is direct subject of this inner state |
| 2 | CAUSATIVE_OF_INNER_STATE | Explicit causative grammatical form (Hiphil/Piel/Greek causative) |
| 3 | SOMATIC_INNER_LINK | Inner state connected to bodily organ or physical process |
| 4 | BODY_INNER_EXPRESSION | Inner state manifests through visible physical behaviour |
| 5 | NT_FACULTY_NAMING | Greek term names an inner faculty (kardia, pneuma, psuche, nous) |
| 6 | GENERATION_RESOLUTION_PAIR | Hebrew-Aramaic or Hebrew-Greek pair resolving to same referent |
| 7 | CROSS_PART_ROOT | Root family spans part boundary in split registry |
| 8 | THIN_DATA | Fewer than 5 verse records; too thin for confident analysis |
| 9 | SMALL_VERSE_SAMPLE | Verse count < 20% of occurrence count |
| 10 | DUPLICATE_RESOLVED | Duplicate entry resolved to single record |
| 11 | NO_WORD_ANALYSIS | No STEP word analysis data available |
| 12 | CONSOLIDATION_CANDIDATE | Likely to merge with related entry in Session B |
| 13 | THEOLOGICAL_ANCHOR | Framework A/B intersection term |
| 14 | SOMATIC_EXPRESSION | Expresses inner state through somatic patterns |
| 15 | HIGH_FREQUENCY_ANCHOR | 200+ occurrences; primary anchor for semantic field |
| 16 | SEMANTIC_RANGE_BREADTH | 4+ distinct semantic domains |
| 17 | MULTI_REGISTRY_ANCHOR | Cross-reference in 3+ registries |
| 18 | DIVINE_HUMAN_PARALLEL | God and humans as subject in parallel contexts |
| 19 | ESCHATOLOGICAL_USAGE | Predominant in eschatological/apocalyptic passages |
| 20 | WISDOM_LITERATURE_CONCENTRATION | Predominant in Proverbs, Job, Ecclesiastes |
| 21 | METAPHOR_ROOT | Meaning grounded in concrete physical/sensory metaphor |
| 22 | RELATIONAL_DIRECTION | Inherently directed toward another person/group/God |
| 23 | VOLITIONAL_COMPONENT | Carries dimension of will, choice, or intention |
| 24 | CROSS_TESTAMENT_SHIFT | Meaningful semantic shift between OT and NT usage |
| 25 | ARAMAIC_FORM | Aramaic form of Hebrew root (Daniel, Ezra, post-exilic) |

### A.3 wa_crosslink_type (cross-registry link types)

| id | type_code | Description |
|:--:|-----------|-------------|
| 1 | SHARED_TERM | Same Hebrew/Greek term appears in both registries |
| 2 | SEMANTIC_OVERLAP | Overlapping meaning space |
| 3 | SHARED_ROOT | Common etymological root |
| 4 | SHARED_VERSE | Same verse references in both registries |
| 5 | THEOLOGICAL | Connected by theological concept or theme |
| 6 | CO_OCCURRENCE | Terms frequently appear together in passages |
| 7 | SEMANTIC_OPPOSITION | Antonyms or semantic contrasts |
| 8 | SISTER_REGISTRY | Parallel registries covering closely related vocabulary |
| 9 | OVERLAPPING_DOMAIN | Registries sharing terms with overlapping semantic domains |
| 10 | CAUSATIVE_CHAIN | Causal relationship between inner states |
| 11 | THEMATIC_LINK | Thematic connection identified during Session B |

### A.4 Valid mti_terms.status values

| Value | Meaning |
|-------|---------|
| `NULL` | Unclassified — awaiting Session B pre-analysis |
| `extracted` | Confirmed in-scope, full data |
| `extracted_thin` | In-scope but thin data (< 20 occurrences) |
| `extracted_theological_anchor` | Theological anchor term (divine names, titles) |
| `candidate_delete` | Staged for deletion by A6b — awaiting researcher confirmation |
| `delete` | Confirmed bleed/out-of-scope — researcher decision |
| `excluded` | Excluded during Session A |
| `phase2_enrichment` | Not primary but enriches another term's analysis |
| `xref_[word]` | Cross-registry term — primary analysis in named registry |

### A.5 Valid word_registry.session_b_status values

| Value | Meaning |
|-------|---------|
| `NULL` | Phase 1 excluded or not yet audited |
| `Verse Context Reset` | Prior Session B work superseded — must reprocess through Verse Context and pool-based Session B |
| `Ready for Analysis` | Verse Context complete + extraction + audit complete, awaiting pre-analysis |
| `Pre-Analysis Complete` | Pre-analysis patch applied, term classifications done |
| `Analysis Complete` | Session B analysis patch applied |
| `Session B Complete` | Full Session B complete with all outputs |

### A.6 Valid session_b_status for _patch_meta

| Patch type | session_b_status value | Note |
|-----------|----------------------|------|
| PREANALYSIS | `Pre-Analysis Complete` | Required, non-null |
| SESSIONB | `Analysis Complete` or `Session B Complete` | Required, non-null |
| REPAIR | Current status (do not change) | Required, non-null |
| VERSECONTEXT | `null` | Applicator must NOT reject null for this type |
| VCGROUP | `null` | Applicator must NOT reject null for this type |
| VCVERSE | `null` | Applicator must NOT reject null for this type |

### A.7 Valid word_registry.verse_context_status values (new v1.2)

| Value | Meaning |
|-------|---------|
| `NULL` | Phase 1 excluded or zero-term registry — outside Verse Context scope |
| `In Progress` | Verse Context pending or underway for this registry |
| `Complete` | All OWNER terms with verses classified — DataPrep gate open |

This field is set by Claude Code completion logic only — not by patch files. Not included in `_patch_meta`.

---

*patch_specification_v1.9 | 20260412 | Supersedes v1.8-20260412 | Section 3 note: wa_dimension_index insert not yet supported by applicator — manual application required; action logged*

*patch_specification_v1.8 | 20260412 | Supersedes v1.7-20260412 | Section 8.0: Group ID resolution rule for same-patch inserts — bare group_code only, no RESOLVE prefix*

*patch_specification_v1.7 | 20260412 | Supersedes v1.6-20260330 | Section 3.2: Confusion alert added for update_registry vs update on word_registry — field format distinction*

*patch_specification_v1.6 | 20260330 | Supersedes v1.5-20260330 | Section 0.1: VerseContext governing instruction updated to v1.7*
