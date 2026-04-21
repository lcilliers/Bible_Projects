# wa-patch-instruction-v2_2-20260421

> Framework B Soul Word Analysis Programme — Patch Preparation and Execution
> Version: v2_2 | Date: 20260421
> Supersedes: wa-patch-instruction-v2_1-20260418.md (itself supersedes wa-patch-instruction-v2_0-20260418.md + wa-patch-specification-v1_14-20260416.md + patch-related sections of wa-sessionb-cc-instructions-v3_6-20260416.md §4, §15, §16)
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
- Rules and addenda update workflow (§13)

This document is NOT authoritative for (pointers, not copies):
- Controlled vocabulary values → wa-reference [current] §2 onwards; `wa_vocab_set` + `wa_vocab_member` in DB are canonical post-M32
- Schema field definitions → wa-reference [current] §13
- File naming rules → GR-FILE-001 through GR-FILE-009; wa-reference [current] §1
- Patch type catalogue → `wa_patch_type_registry` in DB is canonical post-M35; this document's §3.3 table is a synchronised copy
- Directive method → wa-directive-instruction [current]
- CC operational routines outside patch application → wa-claudecode-instruction [current]
- Conversational rules-change protocol → docs/rules-update-protocol.md (cross-referenced from §13)

---

## Change Control — v2_2

| Change | Section |
|---|---|
| Added RULES to patch_type controlled vocabulary (§3.3) and session_b_status table (§3.4 — null-exempt) | §3.3, §3.4 |
| Added CATALOGUE_POPULATION, DIMREVIEW, DIMREVIEW-GRPDESC, PROSE, READINESSSWEEP, SDPOINTERS, SESSIONB_FINDINGS to §3.3 for parity with `wa_patch_type_registry` (M35, 2026-04-20); all null-exempt except where noted | §3.3, §3.4 |
| Added §2.4 — Programme-wide patches (no registry token in filename) | §2.4 |
| New §13 — Rules and Addenda Updates (operation types `insert` / `update` / `deprecate` on `wa_rule_registry`; `insert` / `update` on `wa_addendum_registry`; cross-ref to docs/rules-update-protocol.md) | §13 |
| Self-check §7.1 check 3 updated: "`patch_type` is one of the values listed in §3.3 (copy of `wa_patch_type_registry`)" | §7.1 |
| Appendix A.3 — RULES row added; governing instruction: this document §13 + docs/rules-update-protocol.md | Appendix A.3 |
| Footer updated — produced_by references in examples bumped to v2_2 where regenerated | Throughout |

### Prior change control — v2_1

Operational cross-references migrated to `[current]` token per GR-REF-002; patch index rows updated; provenance references preserved. v2_0 inventory table retained for provenance.

### Prior change control — v2_0

Consolidation version: content drawn from wa-patch-specification-v1_14, wa-sessionb-cc-instructions-v3_6 §4/§15/§16, and global rules addenda ADD-PATCHDIR-001/004/005/007/008. Major version bump for structural reorganisation and content absorption.

---

## 1. Role and Method Selection

Per wa-global-general-rules [current] GR-PROG-005, Claude AI determines what should be done and why; Claude Code executes.

There are two and only two mechanisms for instructing Claude Code to make database changes — **patches** (this document) and **directives** (wa-directive-instruction [current]). Conversational instructions to CC without either format are not valid database change requests — with one scoped exception in §13.2 for conversational rules-change requests, which are drafted by CC into RULES patches for researcher approval.

### 1.1 When to use a patch

Use a patch when Claude AI (or Claude Code, for rules/addenda updates per §13) is certain of:
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

Verse Context patches use a different reference token:
- `wa-vcb001-patch-versecontext-v1-20260329.json` (batch)
- `wa-vcgroup47-patch-v1-20260329.json` (targeted group)
- `wa-vcverse4821-patch-v1-20260329.json` (targeted verse)

### 2.3 Version incrementing

`V{n}` in `patch_id` tracks multiple patches of the same type for the same registry (or subject) in the same session. First is V1; corrections increment to V2, V3. The applicator rejects duplicate `patch_id` values — every patch has a unique id.

### 2.4 Programme-wide patches (new in v2_2)

Some patch types are not tied to a single registry — they update programme-wide tables such as `wa_rule_registry`, `wa_addendum_registry`, `wa_obs_question_catalogue`, `wa_patch_type_registry`, or the prose store. These use a subject-scoped filename pattern, not the registry-scoped pattern in §2.2.

| Scope | Filename pattern | `patch_id` pattern | Example |
|---|---|---|---|
| RULES | `wa-rules-{subject}-{action}-v{n}-{YYYYMMDD}.json` | `PATCH-{YYYYMMDD}-RULES-{SUBJECT}-V{n}` | `wa-rules-gr-load-001-update-v1-20260421.json` |
| CATALOGUE_POPULATION | `wa-catalogue-{scope}-v{n}-{YYYYMMDD}.json` | `PATCH-{YYYYMMDD}-CATALOGUE-{SCOPE}-V{n}` | `wa-catalogue-qcov-populate-v1-20260420.json` |
| PROSE | `wa-prose-{section_code}-{action}-v{n}-{YYYYMMDD}.json` | `PATCH-{YYYYMMDD}-PROSE-{SECTION}-V{n}` | `wa-prose-sa-summary-062-v1-20260420.json` |
| CLUSTERING | `wa-clusters-{date}-v{n}.json` | `PATCH-{YYYYMMDD}-CLUSTERS-V{n}` | `wa-clusters-20260418-v1.json` |
| SDPOINTERS | `wa-sdpointers-{batch}-v{n}-{YYYYMMDD}.json` | `PATCH-{YYYYMMDD}-SDPOINTERS-{BATCH}-V{n}` | `wa-sdpointers-b001-v1-20260420.json` |

Programme-wide patches omit `registry_id` and `word` from `_patch_meta` (fields are optional where the patch targets no single registry). `patch_type` and `session_b_status` rules still apply (see §3).

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
| registry_id | Registry-scoped types | `word_registry.no` (integer). Omit for programme-wide types (§2.4). |
| word | Registry-scoped types | English word. Omit for programme-wide types. |
| produced_date | Yes | Compact format `YYYYMMDD` per GR-FILE-009 |
| produced_by | Yes | Governing instruction name and version |
| patch_type | Yes | Controlled vocabulary — see §3.3 (canonical: `wa_patch_type_registry`) |
| session_b_status | Required for non-exempt types (see §3.4) | `null` for exempt types |
| description | Yes | One-sentence summary |

### 3.3 Valid `patch_type` values

**Canonical source:** `wa_patch_type_registry` (DB, post-M35). The table below is a synchronised copy; on conflict the DB wins. Run `python scripts/build_patch_types_extract.py` for a fresh JSON extract.

| `patch_type` | Exempt from session_b_status requirement | Purpose |
|---|---|---|
| PREANALYSIS | no | Session B Stage 1 Pre-Analysis (evidential status + dimensions + pre-analysis prep) |
| SESSIONB | no | Session B Stage 2 analysis-complete patch (findings + dimensions + SD pointers) |
| SESSIONB_FINDINGS | yes | Session B Stage 2b findings-only patch (finer-grained than SESSIONB) |
| VERSECONTEXT | yes | Verse Context — batch-level classification |
| VCGROUP | yes | Verse Context — per-group patch |
| VCVERSE | yes | Verse Context — per-verse patch |
| DIMREVIEW | yes | Dimension Review per-registry (dimension + dominant_subject + Ph2 flags) |
| DIMREVIEW-GRPDESC | yes | Dimension Review group-description correction |
| CATALOGUE_POPULATION | yes | Observation question catalogue population |
| CLUSTERING | yes | Cluster assignment |
| PROSE | yes | Prose section insert/supersede/approve |
| READINESSSWEEP | yes | Readiness sweep mechanical remediation (Path 1 items) |
| REPAIR | yes | Recovery from failed apply or data-state corrections |
| **RULES** | **yes** | **Global rules + addendum updates (see §13)** |
| SDPOINTERS | yes | Session D pointer cluster (batches of SD pointers) |
| SESSIOND | yes | Session D cross-registry synthesis |

### 3.4 Valid `session_b_status` values per patch type

| Patch type | `session_b_status` in `_patch_meta` |
|---|---|
| PREANALYSIS | `"Pre-Analysis Complete"` (required, non-null) |
| SESSIONB | `"Analysis Complete"` or `"Session B Complete"` (required, non-null) |
| REPAIR | Current status or reset target (required when registry-scoped; else null) |
| All other types (VERSECONTEXT, VCGROUP, VCVERSE, DIMREVIEW, DIMREVIEW-GRPDESC, CATALOGUE_POPULATION, CLUSTERING, PROSE, READINESSSWEEP, **RULES**, SDPOINTERS, SESSIOND, SESSIONB_FINDINGS) | `null` — applicator must not reject |

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

### 4.13 Rules and addenda operations

See §13 — `insert` / `update` / `deprecate` on `wa_rule_registry`; `insert` / `update` on `wa_addendum_registry`. Used exclusively by RULES patches.

---

## 5. Applicator Behaviour

### 5.1 Transaction model

All operations in a patch run in a single transaction — all-or-nothing. On any failure, full rollback; the patch file remains in place on disk for correction.

### 5.2 On success

- `patch_id` logged to `engine_run_log`
- Patch file moved to `archive/patches/`
- `last_changed` (or `last_modified`) auto-set on all updated rows

### 5.3 Non-existent columns in `set`

Silently dropped with a console note. Not a failure condition.

### 5.4 Deletion discipline (absorbed from GR-OBS-005)

No database record is ever physically deleted by the applicator. Records that are superseded, incorrect, or out of scope are marked with `delete_flagged = 1`, `obsolete_reason`, and `obsolete_date`. The original record is retained for audit. This applies to all tables across all phases. Claude Code must never execute DELETE statements against analytical records.

Patches that attempt physical deletion via `operation: "delete"` or raw SQL DELETE are rejected.

For rules and addenda, "deletion" is the `deprecate` operation (§13.4) — it sets `obsolete = 1`, records `obsolete_reason` / `obsolete_date`, and optionally `superseded_by`. Rows are retained for audit.

### 5.5 Validation rules (pre-application)

The applicator validates before applying. Failure rejects the entire patch — no partial application.

1. `patch_id` has not been previously applied (checked in engine_run_log)
2. All `strongs_number` values in `update_mti_status` exist in `mti_terms`
3. All `flag_label` values in research flag inserts are unique
4. All `registry_no` / `registry_id` values exist in `word_registry` (skipped for programme-wide patches with no registry key)
5. `session_b_status` present in `_patch_meta` where required per §3.4
6. For REPAIR patches: `update_registry` operations that set `session_b_status` to a value it already holds are accepted without error — idempotent
7. For RULES patches: all `rule_id` values in `update` / `deprecate` operations exist in `wa_rule_registry`; all `item_id` values in `update` on `wa_addendum_registry` exist

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
| **RULES** | **`SELECT version, category, substr(rule_text, 1, 60) FROM wa_rule_registry WHERE rule_id IN (...)` + row count of `insert`/`deprecate` ops** | **Versions and categories match the patch set clauses; row counts match operation counts** |

---

## 7. Patch Self-Check (absorbed from GR-DIR-006)

Before presenting any patch for researcher approval, Claude AI verifies the six structural compliance points below. A patch that fails any check must not be submitted. Claude AI corrects and re-checks before submission.

### 7.1 The six checks

1. **Top-level structure** — patch has exactly three top-level keys: `_patch_meta`, `operations`, `_patch_summary`
2. **`_patch_meta` completeness** — contains `patch_id`, `produced_date`, `produced_by`, `patch_type`, `description`, and (for registry-scoped patches) `registry_id` + `word`; `session_b_status` non-null for non-exempt types
3. **`patch_type` valid** — one of the values listed in §3.3 (this document; canonical source: `wa_patch_type_registry`)
4. **`session_b_status` valid for patch type** — per §3.4 table
5. **Operations format** — each operation has `op_id` in `OP-NNN` format; `operation` is a valid lowercase named type from §4 or §13; `match` dict and `set` dict present where required
6. **`_patch_summary`** — present; `total_operations` matches `operations[].length`

### 7.2 Filename check

Patch filename follows pattern per §2.1 (registry-scoped) or §2.4 (programme-wide): lowercase, compact date, versioned. Non-compliant filenames are corrected before submission.

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

### 8.3 Rules extract (RULES patches only)

After every RULES patch apply, regenerate the rules extract — this is how the updated vocabulary becomes visible to AI sessions starting after the apply:

```bash
python scripts/build_rules_extract.py --also-markdown
```

Default output: `data/exports/reference/wa-global-rules-extract-{YYYYMMDD}.json` + `.md`. Obsolete rules and addenda are excluded by default.

### 8.4 Template structures

JSON templates for final-extract and sd-pointer files are maintained in wa-reference [current] §14.

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

For a failed RULES patch, use a subject token in place of `{nnn}-{word}`, matching the original filename:
- `wa-rules-{subject}-patch-repair-failure-v1-{YYYYMMDD}.json`
- `PATCH-{YYYYMMDD}-RULES-{SUBJECT}-REPAIR-FAILURE-V1`

### 10.2 Structure

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-{nnn}-REPAIR-FAILURE-V1",
    "registry_id": {nnn},
    "word": "{word}",
    "produced_date": "{YYYYMMDD}",
    "produced_by": "wa-patch-instruction-v2_2-20260421",
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

- Any patch rejection (PREANALYSIS, ANALYSIS, SESSIONB, SESSIONB-COMPLETE, VERSECONTEXT, RULES)
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

## 13. Rules and Addenda Updates (new in v2_2)

### 13.1 Background

Pre-M33, global rules lived in `data/imports/WA/Workflow/Framework_B/Session_B/wa-global-general-rules-v{n}.json` and were edited directly. Post-M33 (2026-04-20), rules and addenda live in `wa_rule_registry` + `wa_addendum_registry`; the JSON seed file is retained for audit only. All rules changes flow through RULES patches so that (a) the DB remains canonical, (b) a per-patch backup is taken, and (c) the change is auditable via `engine_run_log`.

Companion document: **docs/rules-update-protocol.md** — covers the three ways to initiate a rules change (conversational, markdown round-trip, direct edit — avoid) and the end-to-end workflow for researchers. This section covers the patch format.

### 13.2 When to use a RULES patch

Use a RULES patch to:
- Insert a new rule (`wa_rule_registry`)
- Revise fields of an existing rule (text, category, version, example, etc.)
- Deprecate a rule (mark obsolete, optionally record `superseded_by`)
- Insert a new addendum (`wa_addendum_registry`)
- Revise an existing addendum

Researcher-initiated rules changes typically arrive conversationally ("update rule GR-X, add point Y"). In that case, Claude Code drafts the RULES patch, shows it for approval, applies on approval, and regenerates the rules extract (§8.3).

### 13.3 Filename, patch_id and `_patch_meta`

Per §2.4 programme-wide convention:

| Field | Value |
|---|---|
| Filename | `wa-rules-{subject}-{action}-v{n}-{YYYYMMDD}.json` |
| `patch_id` | `PATCH-{YYYYMMDD}-RULES-{SUBJECT}-V{n}` |
| `patch_type` | `"RULES"` |
| `session_b_status` | `null` (RULES is exempt per §3.4) |
| `registry_id` / `word` | omit (programme-wide) |

Examples:
- `wa-rules-gr-load-001-update-v1-20260421.json` → `PATCH-20260421-RULES-GR-LOAD-001-UPDATE-V1`
- `wa-rules-gr-new-002-insert-v1-20260425.json` → `PATCH-20260425-RULES-GR-NEW-002-INSERT-V1`
- `wa-rules-batch-deprecation-v1-20260501.json` → `PATCH-20260501-RULES-BATCH-DEPRECATION-V1`

### 13.4 Operation types

#### 13.4.1 `insert` on `wa_rule_registry`

```json
{
  "op_id": "OP-001",
  "table": "wa_rule_registry",
  "operation": "insert",
  "record": {
    "rule_id": "GR-NEW-001",
    "category": "process_discipline",
    "subject": "New rule — short title",
    "rule_text": "Full rule text here. Multi-line text uses \\n escapes.",
    "applies_to": "all sessions",
    "version": "1.0",
    "added_date": "20260421",
    "source_document": "PATCH-20260421-RULES-GR-NEW-001-INSERT-V1"
  }
}
```

Required: `rule_id` (unique), `category`, `subject`, `rule_text`. Optional: `example`, `applies_to`, `version`, `added_date`, `source_document`, `addendum_ref`.

Category convention: lowercase snake-case (`session_startup`, `load_requirement`, `process_discipline`, `file_naming`, `programme_orientation`, etc.). Normalise on draft — the reference guide is the category set already present in `wa_rule_registry`.

#### 13.4.2 `update` on `wa_rule_registry`

```json
{
  "op_id": "OP-002",
  "table": "wa_rule_registry",
  "operation": "update",
  "match": { "rule_id": "GR-FILE-003" },
  "set": {
    "rule_text": "Revised rule text...",
    "version": "3.1",
    "category": "file_naming"
  }
}
```

`match` must specify `rule_id`. `set` accepts any updatable column; unknown columns are dropped per §5.3. Immutable fields (`id`, `rule_id`, `created_at`) are protected — the applicator rejects attempts to overwrite them.

#### 13.4.3 `deprecate` on `wa_rule_registry`

```json
{
  "op_id": "OP-003",
  "table": "wa_rule_registry",
  "operation": "deprecate",
  "match": { "rule_id": "GR-OLD-001" },
  "record": {
    "obsolete_reason": "Replaced by GR-NEW-001",
    "superseded_by": "GR-NEW-001"
  }
}
```

Sets `obsolete = 1`, `obsolete_date` (auto), `obsolete_reason`, and `superseded_by`. The rule is retained in the table but excluded from the default extract (see §8.3).

#### 13.4.4 `insert` / `update` on `wa_addendum_registry`

Addendum inserts carry `addendum_group`, `rule_id` (optional FK to `wa_rule_registry`), `subject`, `observation`, `source_document`. Update matches on `item_id`. Same applicator rules as rules (column filter, immutable fields).

```json
{
  "op_id": "OP-004",
  "table": "wa_addendum_registry",
  "operation": "insert",
  "record": {
    "item_id": "ADD-DIR-009",
    "addendum_group": "directive_protocol",
    "rule_id": "GR-DIR-003",
    "subject": "Directive envelope format",
    "observation": "All directives must carry a `_directive_meta` envelope with...",
    "source_document": "researcher note 2026-04-25"
  }
}
```

Post-M36 (2026-04-20): all prior 22 addenda are marked obsolete. New addenda additions should be rare — most guidance now belongs directly in a rule or in a process document.

### 13.5 Worked example — the session-startup rules update (2026-04-21)

See `archive/patches/wa-rules-gr-load-001-update-v1-20260421.json` for the authoritative example, applied 2026-04-21 to recategorise GR-LOAD-001 + GR-OBS-001 into `session_startup` and make the startup sequence explicit. Structure:

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-20260421-RULES-SESSION-STARTUP-V1",
    "patch_type": "RULES",
    "produced_by": "wa-patch-instruction-v2_2-20260421",
    "produced_at": "2026-04-21T00:00:00Z",
    "motivation": "...",
    "session_b_status": null,
    "researcher_approval": "PENDING"
  },
  "operations": [
    { "op_id": "OP-001", "table": "wa_rule_registry", "operation": "update",
      "match": { "rule_id": "GR-LOAD-001" }, "set": { "category": "session_startup", "rule_text": "...", "version": "3_1", "added_date": "20260421" } },
    { "op_id": "OP-002", "table": "wa_rule_registry", "operation": "update",
      "match": { "rule_id": "GR-OBS-001" }, "set": { "category": "session_startup", "rule_text": "...", "version": "2_0", "added_date": "20260421" } }
  ]
}
```

Note `researcher_approval: "PENDING"` in `_patch_meta` — a convention for RULES patches to make the approval step explicit. The applicator does not enforce this field; the researcher's verbal/chat approval remains the gate.

### 13.6 Workflow summary

1. Researcher tells CC in chat what to change (conversational path) — or hands over a marked-up MD extract (markdown round-trip).
2. CC drafts the RULES patch per §13.3 / §13.4.
3. CC runs the §7 self-check and presents the patch to the researcher.
4. Researcher approves (typically in chat).
5. CC applies: `python scripts/apply_session_patch.py {patch_file}`
6. CC regenerates the rules extract: `python scripts/build_rules_extract.py --also-markdown`
7. CC commits the patch artefact + new extract files.
8. AI sessions starting after the regeneration see the updated vocabulary.

### 13.7 Rollback

Each patch apply creates a per-patch DB backup at `backups/bible_research_backup_{timestamp}_{patch_id}.db`. If the researcher requests rollback:

1. CC confirms which patch is being rolled back.
2. CC restores the DB from the per-patch backup (via a directive, not a patch — rollback is a destructive action per CLAUDE.md).
3. CC regenerates the rules extract so post-rollback vocabulary is visible.

---

## Appendix A — Lookup Tables

Lookup values used in patches. Vocabulary sources are authoritative in wa-reference [current] and in the DB (`wa_vocab_set`, `wa_patch_type_registry`); this appendix shows values used in patch construction.

### A.1 `session_b_status` by patch type

Per §3.4 — repeated here for quick reference.

### A.2 Operation type names

Per §4 and §13.4 — repeated here for quick reference when constructing new patches.

### A.3 Governing-document cross-reference for patch types

| Patch type | Governing instruction | Purpose |
|---|---|---|
| PREANALYSIS | wa-sessionb-analysis-readiness [current] (see FLAG-001 for finalisation status) | Pre-analysis data corrections; phase2 flag dispositions |
| SESSIONB | wa-sessionb-analysis-output [current] (see FLAG-003 for finalisation status) | Evidential status, dimensions, findings, SD pointer flags |
| SESSIONB_FINDINGS | wa-sessionb-analysis-output [current] | Session B Stage 2b findings-only (finer-grained than SESSIONB) |
| REPAIR | This document §9 | Cascade reset operations; failure recording |
| SESSIOND | wa-sessiond-orientation [current] | Session D discovery and synthesis |
| SDPOINTERS | wa-sessiond-orientation [current] | Session D pointer cluster batches |
| CLUSTERING | wa-registry-management-guide [current] | Cluster assignment updates |
| VERSECONTEXT | wa-versecontext-instruction [current] | Verse relevance filter, grouping, anchor designation |
| VCGROUP | wa-versecontext-instruction [current] | Targeted group update |
| VCVERSE | wa-versecontext-instruction [current] | Targeted verse update |
| DIMREVIEW | wa-dimensionreview-instruction [current] | Dimension Review per-registry |
| DIMREVIEW-GRPDESC | wa-dimensionreview-instruction [current] | Dimension Review group-description correction |
| CATALOGUE_POPULATION | wa-reference [current] §13.13 + observation-catalogue notes | Observation question catalogue population |
| PROSE | wa-reference [current] §13.14 (prose store) | Prose section insert/supersede/approve |
| READINESSSWEEP | wa-sessionb-analysis-readiness [current] | Readiness sweep mechanical remediation (Path 1) |
| **RULES** | **This document §13 + docs/rules-update-protocol.md** | **Global rules + addenda updates** |

---

*wa-patch-instruction-v2_2-20260421 | Supersedes wa-patch-instruction-v2_1-20260418 | Prior: v2_0-20260418 + wa-patch-specification-v1_14-20260416 + wa-sessionb-cc-instructions-v3_6 §4, §15, §16 | Absorbs addenda ADD-PATCHDIR-001, -004, -005, -007, -008 from global rules v2_10*
