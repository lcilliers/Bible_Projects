# wa-patch-instruction-v2_1-20260418

> Framework B Soul Word Analysis Programme — Patch Preparation and Execution
> Version: v2_1 | Date: 20260418
> Supersedes: wa-patch-instruction-v2_0-20260418.md (itself supersedes wa-patch-specification-v1_14-20260416.md + patch-related sections of wa-sessionb-cc-instructions-v3_6-20260416.md §4, §15, §16)
> Governed by: wa-global-general-rules [current]

---

## Document scope (GR-REF-001 Discipline 5)

This document is the authoritative source for:
- Patch JSON format — structure, fields, operation types
- Patch preparation workflow — how Claude AI constructs patches
- Patch execution workflow — how Claude Code applies patches
- Patch filename and patch_id conventions
- REPAIR patch catalogue (cascade resets for pipeline re-runs)
- Failure patch mechanism
- Patch self-check protocol (absorbed from GR-DIR-006)

This document is NOT authoritative for (pointers, not copies):
- Controlled vocabulary values → wa-reference [current] §2 onwards
- Schema field definitions → wa-reference [current] §13
- File naming rules → GR-FILE-001 through GR-FILE-009; wa-reference [current] §1
- Directive method → wa-directive-instruction [current]
- CC operational routines outside patch application → wa-claudecode-instruction [current]

---

## Change Control — v2_1

| Change | Section |
|---|---|
| Operational cross-references migrated to `[current]` token per GR-REF-002 — frontmatter, §8 cross-refs, patch index table in §12 equivalent | Frontmatter, §8, §12-equiv |
| Patch Index rows updated: `wa-sessiond-orientation v3_0` (stale) → `[current]`; `wa-versecontext-instruction v2_7` → `[current]`; `wa-registry-management-guide v5_9` → `[current]` | §12-equivalent (patch index table) |
| Provenance references preserved: Supersedes header, inventory table in v2_0 Change Control, footer Supersedes, `_patch_meta.produced_by` field illustration in §3 | — |
| v2_0 Change Control retained below for provenance | — |

### Prior change control — v2_0

This is a consolidation version. Structure refactored; content drawn from three sources:

| Source | Content absorbed |
|---|---|
| wa-patch-specification-v1_14 | Entire document — JSON format, operation types, applicator rules, validation, appendices |
| wa-sessionb-cc-instructions-v3_6 §4 | Patch application workflow, handoff formats, validation rules, CC actions |
| wa-sessionb-cc-instructions-v3_6 §15 | REPAIR patch catalogue (four cascade reset specifications) |
| wa-sessionb-cc-instructions-v3_6 §16 | Failure patch structure and production rules |
| global rules addendum ADD-PATCHDIR-001 | Patch self-check (GR-DIR-006) absorbed into §7 |
| global rules addendum ADD-PATCHDIR-004 | Physical deletion prohibition (GR-OBS-005) absorbed into §5 |
| global rules addendum ADD-PATCHDIR-005 | When to use patch vs directive (GR-DIR-001) absorbed into §1 |
| global rules addendum ADD-PATCHDIR-007 | Patch format per specification (GR-DIR-003) absorbed into §1 |
| global rules addendum ADD-PATCHDIR-008 | Completion confirmation (GR-DIR-005) absorbed into §6 |

Major version bump (v1_14 → v2_0) because: (1) structural reorganisation with new sections; (2) absorption of content from three source documents; (3) application of GR-REF-001 discipline throughout — duplicated content removed, pointers added.

Change list:
- New §1 — Role and decision: patch vs directive (absorbed from GR-DIR-001)
- §2 patch filename and patch_id conventions — consolidated; lowercase filename and uppercase patch_id distinction clarified
- §3 patch file structure — unchanged substance from v1_14 §2
- §4 supported operations — unchanged substance from v1_14 §3 with clearer subsection numbering
- §5 applicator behaviour — adds deletion discipline (absorbed GR-OBS-005)
- §6 completion confirmation — new section absorbing GR-DIR-005
- §7 patch self-check — new section absorbing GR-DIR-006
- §8 post-patch output files — new section absorbing CC instructions §5.3 content
- §9 REPAIR patch catalogue — absorbed from CC instructions §15
- §10 failure patch — absorbed from CC instructions §16
- §11 operations not supported by the applicator — from v1_14 §4
- §12 Verse Context patch operations — from v1_14 §8
- Appendices — reduced to lookup tables only; governing-document cross-reference table updated to current instruction versions

---

## 1. Role and Method Selection

Per wa-global-general-rules [current] GR-PROG-005, Claude AI determines what should be done and why; Claude Code executes.

There are two and only two mechanisms for instructing Claude Code to make database changes — **patches** (this document) and **directives** (wa-directive-instruction [current]). Conversational instructions to CC without either format are not valid database change requests.

### 1.1 When to use a patch

Use a patch when Claude AI is certain of:
- The field names affected
- The FK keys to match on
- The table structure
- The exact operations required

The patch specification defines the exact JSON format and Claude Code applies it via the applicator script. Patches are machine-readable, idempotent, and auditable.

### 1.2 When to use a directive

Use a directive (per wa-directive-instruction [current]) when Claude AI knows the outcome required but is not certain of the exact execution path. Claude AI describes in plain language what needs to happen and why; Claude Code inspects the database, determines the correct operations, and executes.

### 1.3 Common rules (both methods)

- Researcher approval before Claude Code acts — per GR-PROC-004
- Stated completion confirmation — per §6 below for patches (parallel content in wa-directive-instruction §6 for directives)
- Where a patch operation is not yet supported by the applicator: Claude AI flags it for manual application and notes this in `_patch_meta.description`

---

## 2. Patch Filename and Patch ID

### 2.1 Two distinct identifiers

| Identifier | Format | Purpose |
|---|---|---|
| Patch filename | `wa-{nnn}-{word}-patch-{type}-v{n}-{YYYYMMDD}.json` (fully lowercase per GR-FILE-007) | Human-readable file on disk |
| `patch_id` (internal) | `PATCH-{YYYYMMDD}-{registry_no}-{TYPE}-V{n}` (uppercase retained) | Applicator idempotency key stored in `_patch_meta.patch_id` |

Per wa-reference [current] §1.5. Uppercase `patch_id` is an applicator-compatibility convention and is not changed by GR-FILE-007 which governs filenames, not internal field values.

### 2.2 Patch filename by type

Standard word-level patches:
- `wa-097-fear-patch-preanalysis-v1-20260327.json`
- `wa-097-fear-patch-sessionb-v1-20260327.json`
- `wa-097-fear-patch-repair-vc-rerun-v1-20260327.json`

Verse Context patches use different reference token:
- `wa-vcb001-patch-versecontext-v1-20260329.json` (batch)
- `wa-vcgroup47-patch-v1-20260329.json` (targeted group)
- `wa-vcverse4821-patch-v1-20260329.json` (targeted verse)

### 2.3 Version incrementing

`V{n}` in `patch_id` tracks multiple patches of the same type for the same registry in the same session. First is V1; corrections increment to V2, V3. The applicator rejects duplicate `patch_id` values — every patch has a unique id.

---

## 3. Patch File Structure

### 3.1 Top-level structure

Every patch has exactly three top-level keys:

```json
{
  "_patch_meta": { ... },
  "operations": [ ... ],
  "_patch_summary": { ... }
}
```

### 3.2 `_patch_meta` required fields

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-20260325-061-PREANALYSIS-V1",
    "registry_id": 61,
    "word": "fear",
    "produced_date": "20260325",
    "produced_by": "wa-sessionb-analysis-readiness-v1_5",
    "patch_type": "PREANALYSIS",
    "session_b_status": "Pre-Analysis Complete",
    "description": "Brief summary of what this patch does"
  }
}
```

| Field | Required | Notes |
|---|---|---|
| patch_id | Yes | Unique; applicator rejects duplicates. Format per §2.1. |
| registry_id | Yes | `word_registry.no` (integer) |
| word | Yes | English word |
| produced_date | Yes | Compact format `YYYYMMDD` per GR-FILE-009 |
| produced_by | Yes | Governing instruction name and version |
| patch_type | Yes | Controlled vocabulary — see §3.3 |
| session_b_status | Required for PREANALYSIS, SESSIONB, REPAIR (non-null) | `null` for VERSECONTEXT, VCGROUP, VCVERSE — see §3.4 |
| description | Yes | One-sentence summary |

### 3.3 Valid `patch_type` values

PREANALYSIS | SESSIONB | VERSECONTEXT | VCGROUP | VCVERSE | SESSIOND | CLUSTERING | REPAIR

### 3.4 Valid `session_b_status` values per patch type

| Patch type | `session_b_status` in `_patch_meta` |
|---|---|
| PREANALYSIS | `"Pre-Analysis Complete"` (required, non-null) |
| SESSIONB | `"Analysis Complete"` or `"Session B Complete"` (required, non-null) |
| REPAIR | Current status or reset target (required, non-null) |
| VERSECONTEXT | `null` — applicator must not reject |
| VCGROUP | `null` — applicator must not reject |
| VCVERSE | `null` — applicator must not reject |
| SESSIOND | `null` |
| CLUSTERING | `null` |

### 3.5 `_patch_summary` structure

Mandatory. Summarises the operations array:

```json
{
  "_patch_summary": {
    "total_operations": 12,
    "mti_updates": 8,
    "bulk_deletes": 2,
    "research_flag_inserts": 2
  }
}
```

`total_operations` must equal `operations.length`. Additional count fields as relevant for the patch type.

### 3.6 Typical patch sequence through the pipeline

| Patch filename | `session_b_status` | Purpose |
|---|---|---|
| `wa-vcb001-patch-versecontext-v1-{date}.json` | null | Verse context classification |
| `wa-{nnn}-{word}-patch-preanalysis-v1-{date}.json` | Pre-Analysis Complete | Term classifications, bleed removal |
| `wa-{nnn}-{word}-patch-sessionb-v1-{date}.json` | Analysis Complete | Full analytical data |
| `wa-{nnn}-{word}-patch-sessionb-complete-v1-{date}.json` | Session B Complete | Final output confirmation |

---

## 4. Supported Operation Types

Each operation in `operations[]` is a JSON object with `op_id`, `operation`, and operation-specific fields.

### 4.1 `update_mti_status` — single-term classification

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

Valid `status` values per wa-reference [current] §2.

Matches on `strongs_number` only. If `owning_registry_fk` is NULL, it is set from patch `registry_id`. Non-existent columns in `set` are silently dropped.

### 4.2 `update_registry` — update word_registry fields

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

**⚠ Do not confuse with `update` on `word_registry`** — two distinct operations both target `word_registry`:

| Operation | Key field | Section |
|---|---|---|
| `update_registry` | `registry_no` (top-level integer) | §4.2 (this section) |
| `update` on `word_registry` | `match: {id: N}` (match dict) | §4.9 |

`update_registry` with a `match` dict will be silently skipped by the applicator. `update` on `word_registry` without a `match` dict will fail validation.

### 4.3 `bulk_confirm_candidate_delete` — bulk confirm

```json
{
  "op_id": "OP-013",
  "operation": "bulk_confirm_candidate_delete",
  "filter": "registry_no=183 AND mti_status=candidate_delete",
  "set": {
    "status": "delete",
    "exclusion_reason": "Bleed confirmed by researcher"
  }
}
```

Filter must contain `registry_no=N`. Applicator parses, finds all candidate_delete terms linked to the registry, applies the set.

### 4.4 `bulk_update_none_to_delete`

Same format; matches `status IS NULL` terms.

### 4.5 `bulk_confirm_delete_flagged`

Same format; matches `delete_flagged=1` terms with NULL status.

### 4.6 `bulk_update_note` — bulk with filter or strongs list

**Format A — filter-based:**
```json
{
  "op_id": "OP-007",
  "operation": "bulk_update_note",
  "filter": "registry_no=4 AND delete_flagged=1 AND mti_status IS NULL",
  "set": { "status": "delete", "exclusion_reason": "Confirmed bleed" }
}
```

**Format B — explicit strongs list:**
```json
{
  "op_id": "OP-008",
  "operation": "bulk_update_note",
  "bulk_strongs": ["G3844", "H5674A", "H6440H"],
  "set": { "status": "delete", "exclusion_reason": "Bleed family" },
  "xref_exceptions": {
    "H7307G": "xref_spirit — primary in spirit registry"
  }
}
```

`xref_exceptions` optional — overrides status for listed strongs to the specified xref value.

### 4.7 `insert` on research flags

```json
{
  "op_id": "OP-017",
  "operation": "insert",
  "table": "wa_session_research_flags",
  "record": {
    "registry_id": 182,
    "flag_code": "PH2_CROSS_REF_ENRICHMENT",
    "flag_label": "PH2-182-001",
    "strongs_reference": "H5317",
    "priority": "MEDIUM",
    "session_target": "D",
    "description": "Detailed description",
    "session_raised": "Session B v3.0",
    "raised_date": "2026-03-24",
    "resolved": 0
  }
}
```

Required record fields: `registry_id`, `flag_code`, `flag_label` (unique), `description`, `session_raised`, `raised_date`.
Optional: `file_id`, `strongs_reference`, `cross_registry_id`, `priority` (default MEDIUM), `session_target` (default D), `resolved` (default 0).

`flag_label` convention: `PH2-{registry_no}-{3-digit-sequence}` per wa-reference [current] §5.4.

Both `wa_phase2_flags` and `wa_session_research_flags` table names accepted — both route to `wa_session_research_flags`.

### 4.8 `update` on `mti_terms` — Session B format

```json
{
  "op_id": "OP-001",
  "operation": "update",
  "table": "mti_terms",
  "match": { "strongs_number": "G5590G", "owning_registry_fk": 182 },
  "set": { "status": "extracted", "strongs_reconciled": 1 }
}
```

### 4.9 `update` on `word_registry` — Session B format

```json
{
  "op_id": "OP-023",
  "operation": "update",
  "table": "word_registry",
  "match": { "id": 182 },
  "set": { "notes": "Updated notes text" }
}
```

### 4.10 `update_evidential_status` — Session B Extraction format

Targets `wa_term_inventory`. Sets `evidential_status` and `retention_note`. One operation per active OWNER term in the registry during Session B Extraction analysis completion.

```json
{
  "op_id": "OP-001",
  "operation": "update_evidential_status",
  "table": "wa_term_inventory",
  "term_inv_id": 1234,
  "strongs_number": "H0157",
  "set": {
    "evidential_status": "confirmed",
    "retention_note": "Note or null"
  }
}
```

Valid `evidential_status` values per wa-reference [current] §10.

### 4.11 `bulk_update` on `mti_terms` — Session B analysis format

**Format A — nested:**
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

**Format B — flat:**
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

### 4.12 Documentation-only operations

Logged to console, no DB change:
- `schema_investigation_note` — anomaly flagged for CC investigation
- `registry_note` — informational annotation
- `phase1_supplement_required` — signals additional terms need extraction

---

## 5. Applicator Behaviour

### 5.1 Transaction model

All operations in a patch run in a single transaction — all-or-nothing. On any failure, full rollback; the patch file remains in place on disk for correction.

### 5.2 On success

- `patch_id` logged to `engine_run_log`
- Patch file moved to `archive/patches/`
- `last_changed` auto-set on all updated rows

### 5.3 Non-existent columns in `set`

Silently dropped with a console note. Not a failure condition.

### 5.4 Deletion discipline (absorbed from GR-OBS-005)

No database record is ever physically deleted by the applicator. Records that are superseded, incorrect, or out of scope are marked with `delete_flagged = 1`, `obsolete_reason`, and `obsolete_date`. The original record is retained for audit. This applies to all tables across all phases. Claude Code must never execute DELETE statements against analytical records.

Patches that attempt physical deletion via `operation: "delete"` or raw SQL DELETE are rejected.

### 5.5 Validation rules (pre-application)

The applicator validates before applying. Failure rejects the entire patch — no partial application.

1. `patch_id` has not been previously applied (checked in engine_run_log)
2. All `strongs_number` values in `update_mti_status` exist in `mti_terms`
3. All `flag_label` values in research flag inserts are unique
4. All `registry_no` / `registry_id` values exist in `word_registry`
5. `session_b_status` present in `_patch_meta` where required per §3.4
6. For REPAIR patches: `update_registry` operations that set `session_b_status` to a value it already holds are accepted without error — idempotent

---

## 6. Completion Confirmation (absorbed from GR-DIR-005)

Every patch specifies the completion confirmation that Claude Code must return to close the operation.

### 6.1 What counts as confirmation

A specific query result, row count, or field state check. Not a general acknowledgement. Not "patch applied successfully" — that is transaction confirmation, not completion confirmation. Completion confirmation verifies the outcome.

### 6.2 What Claude Code returns

Claude Code returns the confirmation output to Claude AI and the researcher. Example:

```
PATCH-20260327-097-PREANALYSIS-V1 applied.
Completion confirmation:
  SELECT session_b_status FROM word_registry WHERE no = 97;
  → "Pre-Analysis Complete"
  SELECT COUNT(*) FROM mti_terms
    WHERE owning_registry_fk = 97 AND status = 'delete';
  → 14
```

### 6.3 What Claude AI does with it

Reviews the confirmation against the expected outcome. If they match, the operation is closed. If they do not match, the operation is not complete — diagnose and respond. A rejection or mismatch triggers the failure patch mechanism (§10).

### 6.4 Confirmation specification in `_patch_meta`

The `_patch_meta.description` should include the confirmation spec for non-standard patches. Standard patch types have type-specific confirmation templates — see §6.5.

### 6.5 Standard confirmation templates by patch type

| Patch type | Confirmation query | Expected result |
|---|---|---|
| PREANALYSIS | `SELECT session_b_status FROM word_registry WHERE no = {nnn}` | `'Pre-Analysis Complete'` |
| | `SELECT COUNT(*) FROM mti_terms WHERE owning_registry_fk = {nnn} AND status = 'delete'` | Count matches patch `_patch_summary` |
| SESSIONB (Analysis Complete) | `SELECT session_b_status FROM word_registry WHERE no = {nnn}` | `'Analysis Complete'` |
| | `SELECT COUNT(*) FROM wa_session_research_flags WHERE registry_id = {nnn} AND flag_code = 'SB_FINDING'` | Count matches key findings array |
| SESSIONB (Session B Complete) | `SELECT session_b_status FROM word_registry WHERE no = {nnn}` | `'Session B Complete'` |
| VERSECONTEXT | `SELECT COUNT(*) FROM verse_context WHERE delete_flagged = 0` for affected terms | Count matches patch verse count |
| | Consistency rules R1, R2, R3 (see §12.5) | All zero violations |
| REPAIR | `SELECT session_b_status FROM word_registry WHERE no = {nnn}` | Target reset value |
| | Delete-flagged counts on affected tables | Match patch specification |

---

## 7. Patch Self-Check (absorbed from GR-DIR-006)

Before presenting any patch for researcher approval, Claude AI verifies the six structural compliance points below. A patch that fails any check must not be submitted. Claude AI corrects and re-checks before submission.

### 7.1 The six checks

1. **Top-level structure** — patch has exactly three top-level keys: `_patch_meta`, `operations`, `_patch_summary`
2. **`_patch_meta` completeness** — contains `patch_id`, `registry_id`, `word`, `produced_date`, `produced_by`, `patch_type`, `session_b_status` (non-null for PREANALYSIS/SESSIONB/REPAIR), and `description`
3. **`patch_type` valid** — one of: PREANALYSIS, SESSIONB, VERSECONTEXT, VCGROUP, VCVERSE, SESSIOND, CLUSTERING, REPAIR
4. **`session_b_status` valid for patch type** — per §3.4 table
5. **Operations format** — each operation has `op_id` in `OP-NNN` format; `operation` is a valid lowercase named type from §4; `match` dict and `set` dict present where required
6. **`_patch_summary`** — present; `total_operations` matches `operations[].length`

### 7.2 Filename check

Patch filename follows pattern per §2.1 (lowercase, compact date, versioned). Non-compliant filenames are corrected before submission.

### 7.3 On CC rejection after submission

If Claude Code rejects a patch for format non-compliance after researcher approval and submission, this is a programme compliance failure. Claude AI:
1. Produces the corrected patch
2. Records the deviation and correction in the observations log
3. Resubmits for researcher approval before CC proceeds

### 7.4 Self-check statement

Record the self-check result in the observations log before submission:
```
Patch self-check {patch_id}: [PASS / FAIL — items failing]
```

---

## 8. Post-Patch Output Files

Produced after analysis completion patch is applied and confirmed.

### 8.1 Final Registry Extract

Filename: `wa-{nnn}-{word}-final-v{n}-{YYYYMMDD}.json`
Location: `data/exports/`
Produced by: Claude AI per the Session B analysis-output instruction
Purpose: cross-table registry view for Session D

### 8.2 Session D Pointers

Filename: `wa-{nnn}-{word}-sdpointers-v{n}-{YYYYMMDD}.json`
Location: `data/exports/session_d/`
Produced by: apply_session_patch.py auto-generation from SD_POINTER flags
Purpose: evaluative pointers for Session D synthesis

### 8.3 Template structures

JSON templates for both files are maintained in wa-reference [current] §14.

---

## 9. REPAIR Patch Catalogue — Cascade Resets

All pipeline re-runs require a REPAIR patch applied and confirmed before the re-run begins. REPAIR patches reset status and delete_flag the output records of the stage being re-run, while preserving upstream work.

### 9.1 STEP Extraction Re-run Reset

| Field | Value |
|---|---|
| Patch filename | `wa-{nnn}-{word}-patch-repair-step-rerun-v1-{YYYYMMDD}.json` |
| patch_id | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-STEP-RERUN-V1` |
| When | Before re-running word_study_extract.py for a registry |
| `session_b_status` in meta | Current value; `update_registry` operation inside sets the reset |

**Resets on word_registry:**
- `session_b_status` → NULL
- `verse_context_status` → NULL
- `sb_classification`, `sb_classification_reasoning`, `carry_forward` → NULL
- `dimensions`, `description` → NULL

**Additional operations:**
- delete_flag all `verse_context` records for this registry's OWNER terms
- delete_flag all `verse_context_group` records for this registry's OWNER terms
- delete_flag all `wa_term_inventory` records for this registry
- delete_flag all `wa_verse_records` for this registry
- delete_flag all `wa_session_b_dimensions`, `wa_session_b_findings`, `wa_session_research_flags` (SD_POINTER and PH2) for this registry
- Reset `wa_term_inventory.evidential_status` and `retention_note` to NULL for this registry

**Note on mti_terms:** Do NOT delete_flag — programme-wide. Reset `mti_terms.status` to NULL only for terms whose `owning_registry_fk` = this registry AND who have no active `wa_term_inventory` record in any other registry.

**After patch:** Run STEP extraction, then audit_word, then full pipeline from Verse Context.

### 9.2 audit_word Re-run Reset

| Field | Value |
|---|---|
| Patch filename | `wa-{nnn}-{word}-patch-repair-auditword-rerun-v1-{YYYYMMDD}.json` |
| patch_id | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-AUDITWORD-RERUN-V1` |
| When | Before re-running audit_word for a registry that already has data |
| `session_b_status` in meta | `"Verse Context Reset"` |

**Resets on word_registry:**
- `session_b_status` → `Verse Context Reset`
- `verse_context_status` → `In Progress`
- `sb_classification`, `sb_classification_reasoning`, `carry_forward` → NULL
- `dimensions`, `description` → NULL

**Additional operations:**
- delete_flag all `verse_context` records for this registry's OWNER terms
- delete_flag all `verse_context_group` records for this registry's OWNER terms
- delete_flag all `wa_session_b_dimensions`, `wa_session_b_findings`, `wa_session_research_flags` (SD_POINTER and PH2) for this registry
- Reset `wa_term_inventory.evidential_status` and `retention_note` to NULL

**Important — wa_term_inventory NOT delete_flagged:** audit_word's STALE_TERM mechanism at Step A6 updates existing records from new STEP JSON. This is the authoritative mechanism for wa_term_inventory updates on re-run.

**After patch:** Run audit_word. Pipeline proceeds from Verse Context.

### 9.3 Verse Context Re-run Reset

| Field | Value |
|---|---|
| Patch filename | `wa-{nnn}-{word}-patch-repair-vc-rerun-v1-{YYYYMMDD}.json` |
| patch_id | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-VC-RERUN-V1` |
| When | Before re-running Verse Context classification |
| `session_b_status` in meta | `"Verse Context Reset"` |

**Resets on word_registry:**
- `session_b_status` → `Verse Context Reset`
- `verse_context_status` → `In Progress`
- `sb_classification`, `sb_classification_reasoning`, `carry_forward` → NULL
- `dimensions`, `description` → NULL

**Additional operations:**
- delete_flag all `verse_context` records for OWNER terms (or targeted by mti_term_id for partial re-run)
- delete_flag all `verse_context_group` records for OWNER terms (or targeted)
- delete_flag all `wa_session_b_dimensions`, `wa_session_b_findings`, `wa_session_research_flags` (SD_POINTER) for this registry
- Reset `wa_term_inventory.evidential_status` and `retention_note` to NULL

**`mti_terms.status` (set by DataPrep) NOT reset.**

**CC batch preparation routine:** Before constructing VC batch JSON for a registry that had a VC re-run reset:
1. Verify all `verse_context` and `verse_context_group` for this registry's OWNER terms are delete_flagged. If any are not: halt and report to researcher.
2. Treat as fresh start — `existing_groups` in batch JSON will be empty.
3. Check for any terms with `mti_terms.status = NULL` (new or reclassified after re-run). Report to researcher — DataPrep must classify before VC proceeds.

**After patch:** Re-run Verse Context → re-run DataPrep (required because verse_context_status was reset) → Analysis → Extraction.

### 9.4 Analysis Re-run Reset

| Field | Value |
|---|---|
| Patch filename | `wa-{nnn}-{word}-patch-repair-analysis-rerun-v1-{YYYYMMDD}.json` |
| patch_id | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-ANALYSIS-RERUN-V1` |
| When | Before re-running Session B Analysis |
| `session_b_status` in meta | `"Pre-Analysis Complete"` |

**Resets on word_registry:**
- `session_b_status` → `Pre-Analysis Complete`
- `sb_classification`, `sb_classification_reasoning`, `carry_forward` → NULL
- `dimensions`, `description` → NULL

**Additional operations:**
- delete_flag `wa_session_b_dimensions` for this registry
- delete_flag `wa_session_b_findings` for this registry
- delete_flag `wa_session_research_flags` SD_POINTER records for this registry
- Reset `wa_term_inventory.evidential_status` to NULL for all OWNER terms
- Reset `wa_term_inventory.retention_note` to NULL for all OWNER terms

**Verse Context and DataPrep results preserved.**

**After patch:** Re-run Session B Analysis → re-run Extraction.

---

## 10. Failure Patch

When any patch is rejected by the applicator, Claude Code must produce and apply a failure patch before any other action. The failure patch records the failure in the patch history. It does not change any status fields.

### 10.1 Filename and patch_id

| Field | Value |
|---|---|
| Filename | `wa-{nnn}-{word}-patch-repair-failure-v1-{YYYYMMDD}.json` |
| patch_id | `PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1` |

### 10.2 Structure

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1",
    "registry_id": {nnn},
    "word": "{word}",
    "produced_date": "{YYYYMMDD}",
    "produced_by": "wa-patch-instruction-v2_0-20260418",
    "patch_type": "REPAIR",
    "session_b_status": "{current status — unchanged}",
    "description": "PIPELINE FAILURE — {stage} — {brief description}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "registry_note",
      "description": "PIPELINE FAILURE — {stage}: {what failed, what was attempted, what the error was}"
    }
  ],
  "_patch_summary": { "total_operations": 1, "registry_notes": 1 }
}
```

### 10.3 When to produce

- Any patch rejection (PREANALYSIS, ANALYSIS, SESSIONB, SESSIONB-COMPLETE, VERSECONTEXT)
- Partial completion detection at Analysis startup
- All-verses-fail for a term

### 10.4 After failure patch is applied

Claude Code reports to researcher with: failure patch_id, rejected patch filename, rejection reason. Await researcher instruction before producing a corrected patch.

---

## 11. Operations NOT Supported by the Applicator

These operations require manual execution by Claude Code. When they appear in a patch, Claude AI flags for manual application in `_patch_meta.description` and provides clear SQL-level instructions.

### 11.1 Verse reassignment

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

### 11.2 Quality flag insertion

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

### 11.3 VTL population

```json
{
  "op_id": "OP-008",
  "operation": "populate_vtl",
  "term_inv_id": 292,
  "verse_ids": [3364, 3365, 3366, 3367, 3368, 3369, 3370],
  "description": "Populate missing VTL for G0266 verses"
}
```

### 11.4 Delete-flag restoration

```json
{
  "op_id": "OP-005",
  "operation": "restore_delete_flagged",
  "term_inv_ids": [293, 294],
  "description": "Restore G1777 and G2631 — confirmed in scope"
}
```

### 11.5 Cross-registry link insertion

```json
{
  "op_id": "OP-027",
  "operation": "add_cross_registry_links",
  "links": [
    {"from_registry": 212, "to_registry": 61, "type_code": "semantic_overlap"}
  ]
}
```

### 11.6 Other known gaps

The following require manual application pending applicator updates:

- `insert` on `wa_dimension_index` (logged in v1_10)
- `update` on `wa_session_research_flags` (logged in v1_10)
- `session_b_status: null` on SDPOINTERS-type patches (logged in v1_10)

---

## 12. Verse Context Patch Operations

Governed by wa-versecontext-instruction [current]. This section contains the patch-format rules specific to Verse Context patches.

### 12.1 Three patch types

All carry `session_b_status: null` in `_patch_meta`. Applicator must not reject.

- **VERSECONTEXT** — batch classification
- **VCGROUP** — targeted group update
- **VCVERSE** — targeted verse update

### 12.2 Group ID resolution for same-patch inserts

When a patch inserts a new `verse_context_group` and then inserts `verse_context` records for that new group in the same patch, the group's integer `id` is not known at patch-construction time.

**Correct approach:** use the bare `group_code` string as the `group_id` value:

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

The applicator's `_resolve_group_id` function accepts a bare `group_code` string and looks up the correct integer id.

**Do NOT use a decorated prefix such as `"RESOLVE:1613-001"`.** The resolver does not handle prefixed strings; prefix causes failure.

### 12.3 Insert verse_context_group

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
  }
}
```

### 12.4 Update verse_context_group

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
  }
}
```

### 12.5 Insert / update verse_context

Insert:
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
  }
}
```

Update:
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
  }
}
```

### 12.6 Consistency rules (CC validates after application)

| Rule | Check | Expected |
|---|---|---|
| R1 | `is_relevant=0` rows: `group_id` NULL, `is_anchor=0`, `is_related=0` | 0 violations |
| R2 | `is_anchor=1` rows: `is_relevant=1`, `is_related=0`, `group_id` NOT NULL | 0 violations |
| R3 | `is_related=1` rows: group has active anchor | 0 violations |
| R4 | Every term: at least one active `is_anchor=1` row | 0 terms without anchor |

---

## Appendix A — Lookup Tables

Lookup values used in patches. Vocabulary sources are authoritative in wa-reference [current]; this appendix shows values used in patch construction.

### A.1 `session_b_status` by patch type

Per §3.4 — repeated here for quick reference.

### A.2 Operation type names

Per §4 — repeated here for quick reference when constructing new patches.

### A.3 Governing-document cross-reference for patch types

| Patch type | Governing instruction | Purpose |
|---|---|---|
| PREANALYSIS | wa-sessionb-analysis-readiness [current] (see FLAG-001 for finalisation status) | Pre-analysis data corrections; phase2 flag dispositions |
| SESSIONB | wa-sessionb-analysis-output [current] (see FLAG-003 for finalisation status) | Evidential status, dimensions, findings, SD pointer flags |
| REPAIR | This document §9 | Cascade reset operations; failure recording |
| SESSIOND | wa-sessiond-orientation [current] | Session D discovery and synthesis |
| CLUSTERING | wa-registry-management-guide [current] | Cluster assignment updates |
| VERSECONTEXT | wa-versecontext-instruction [current] | Verse relevance filter, grouping, anchor designation |
| VCGROUP | wa-versecontext-instruction [current] | Targeted group update |
| VCVERSE | wa-versecontext-instruction [current] | Targeted verse update |

---

*wa-patch-instruction-v2_1-20260418 | Supersedes wa-patch-instruction-v2_0-20260418 | Prior: wa-patch-specification-v1_14-20260416 + wa-sessionb-cc-instructions-v3_6 §4, §15, §16 | Absorbs addenda ADD-PATCHDIR-001, -004, -005, -007, -008 from global rules v2_10*
