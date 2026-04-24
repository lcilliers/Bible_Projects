# wa-patch-instruction-v2_7-20260424

> Framework B Soul Word Analysis Programme — Patch Preparation and Execution
> Version: v2_7 | Date: 20260424
> Supersedes: wa-patch-instruction-v2_6-20260424.md
>
> **v2_7 (20260424):** Corrects the match-shape examples in §12.4 and §12.5 that previously required the integer `id` of `verse_context_group` or `verse_context` rows. The classifier cannot supply those ids from the per-term Session A `.md` — it only sees `mti_term_id`, `group_code`, and `verse_record_id`. v2_7 documents the correct match shapes: `verse_context_group` UPDATE matches on `{mti_term_id, group_code}`; `verse_context` UPDATE matches on `{mti_term_id, verse_record_id}` — the latter is DB-unique (enforced by `sqlite_autoindex_verse_context_1`). The applicator always accepted both shapes via `_resolve_group_id` and the per-verse uniqueness index; only the doc was wrong, which caused session stoppages before the v3_5 roll-out. Also propagates the A-06 rowcount-gate behaviour from VC instruction v3_5 §7.8: UPDATE ops on `verse_context` and `verse_context_group` that match 0 rows are rejected by `_exec_update_strict`, transaction rolls back, REPAIR-FAILURE patch produced. Editorial-only correction plus rowcount-gate documentation; no semantic change from v2_6.
>
> **v2_6 (20260424):** Adds the A-03 version-gate support to §15 VCNEW and VCREVISE: `_patch_meta.input_versions` is now a required field — a map of `{mti_term_id: md_version}` declaring the per-term `.md` version the classifier worked from. The applicator rejects any patch whose declared input_version for any term does not match the current DB `mti_terms.md_version`; on successful apply, the version is bumped so any pre-existing `.md` is stale. `_patch_meta.batch_id` is reclassified as optional (A-04). VCSBFLAGS/VCSDPOINTERS do not require input_versions. v2_5 content otherwise unchanged.
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

## Change Control — v2_4

| Change | Section |
|---|---|
| New §14 — Prose Updates. Full operation catalogue for `prose_section` (insert, supersede, approve, delete, bulk_supersede, bulk_approve) and `prose_section_type` (insert, update). Decision logic covering when a PROSE patch is used vs a CATALOGUE_POPULATION patch vs a schema enablement directive. Filename conventions, worked examples, and hard rules against in-place edits on narrative prose | §14 |
| New §4.13 — `insert` / `update` on `prose_section_type` | §4.13 |
| New §4.14 — `insert` / `supersede` / `approve` / `delete` on `prose_section` (summary; full detail in §14) | §4.14 |
| New §4.15 — `section_type_id_lookup:{code}` resolver — parallel pattern to verse_context `group_id` resolver (§12.2). Documents the applicator's lookup contract. | §4.15 |
| §1.4 amended — clear statement of the prose lifecycle decision: schema enablement → directive (§10 of wa-directive-instruction); stub creation + content + lifecycle → PROSE / CATALOGUE_POPULATION patches (this document §14) | §1.4 |
| Appendix A.3 — CATALOGUE_POPULATION row rewritten to include prose_section_type inserts as the second use case alongside catalogue questions | Appendix A.3 |
| Immutability discipline on narrative prose made explicit — `supersede` only; no in-place `update`; `session_a_replace` remains restricted to Session A mechanical extracts (`author = 'claude_code'`) | §14.6, §14 summary |

### Prior change control — v2_3

| Change | Section |
|---|---|
| §13.1 updated — introduces the four-field rule structure (`rule_text` / `rationale` / `application_notes` / `examples`) added by DIR-20260421-001, with the retained legacy `example` column noted | §13.1, §13.2 |
| §13.4.1 insert example rewritten — `record` now shows all four body fields; required/optional field list updated | §13.4.1 |
| §13.4.2 update — note added that any of `rule_text`, `rationale`, `application_notes`, `examples`, `example` can appear in `set` | §13.4.2 |
| §13.5 worked example — short note added explaining the four-field shape; prior session-startup example retained as it still matches the rewritten GR-LOAD-001 v3_2 | §13.5 |
| §13.6 workflow — added step confirming `scripts/build_rules_extract.py` now surfaces the four fields (conditional SELECT, MD renderer prints Rationale / Application notes / Examples) | §13.6 |

### Prior change control — v2_2

Added RULES to patch_type controlled vocabulary (§3.3) and session_b_status null-exempt table (§3.4); synced §3.3 with `wa_patch_type_registry` post-M35 (added CATALOGUE_POPULATION, DIMREVIEW, DIMREVIEW-GRPDESC, PROSE, READINESSSWEEP, SDPOINTERS, SESSIONB_FINDINGS); new §2.4 Programme-wide patches filename convention; new §13 Rules and Addenda Updates; self-check §7.1 updated; Appendix A.3 extended.

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

### 1.4 Decision table — prose lifecycle

The prose store has three distinct change surfaces. The routing is fixed, not a judgement call:

| Change | Method | Document / section |
|---|---|---|
| Add a column to `prose_section` or `prose_section_type`; relax a constraint; add a new table | Directive (schema enablement) | wa-directive-instruction [current] §10 |
| Add a new section-type handle (`prose_section_type` row) | CATALOGUE_POPULATION patch with `insert` on `prose_section_type` | This document §14.2 |
| Edit an existing section-type handle (label, description, chapter_no, sort_order) | CATALOGUE_POPULATION patch with `update` on `prose_section_type` | This document §14.2 |
| Add new prose content (`prose_section` row) | PROSE patch with `insert` on `prose_section` | This document §14.3 |
| Revise existing prose content | PROSE patch with `supersede` on `prose_section` | This document §14.4 |
| Transition prose to `approved` | PROSE patch with `approve` on `prose_section` (single or batch) | This document §14.5 |
| Retire prose | PROSE patch with `delete` on `prose_section` (soft) | This document §14.5 |

**Not supported — do not attempt:** in-place `update` of `prose_section.body`, `heading`, or any content field on a narrative prose row. The `session_a_replace` operation is the only in-place path and is restricted to rows with `author = 'claude_code'` (Session A mechanical extracts). For narrative prose, every edit is a `supersede` — see §14.6.

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
| VERSECONTEXT | yes | Verse Context — batch-level classification (legacy; retained for backwards compatibility with pre-v3_3 VC sessions) |
| **VCNEW** | **yes** | **Verse Context session — new classifications (first-time inserts on `verse_context_group` / `verse_context`). Requires `_patch_meta.terms_covered`. See §15.** |
| **VCREVISE** | **yes** | **Verse Context session — revisions to existing classifications (updates on `verse_context_group` / `verse_context`, including dissolves via `delete_flagged = 1`). Requires `_patch_meta.terms_covered`. See §15.** |
| **VCSBFLAGS** | **yes** | **Verse Context session — Session B observation flags raised while reading verses (`wa_session_research_flags` inserts with `session_target = 'Session B'`). See §15.** |
| **VCSDPOINTERS** | **yes** | **Verse Context session — Session D cross-registry pointer observations (`wa_session_research_flags` inserts with `session_target = 'Session D'` and `cross_registry_id` populated). See §15.** |
| VCGROUP | yes | Verse Context — per-group patch (targeted update outside a full session) |
| VCVERSE | yes | Verse Context — per-verse patch (targeted update outside a full session) |
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
| All other types (VERSECONTEXT, **VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS**, VCGROUP, VCVERSE, DIMREVIEW, DIMREVIEW-GRPDESC, CATALOGUE_POPULATION, CLUSTERING, PROSE, READINESSSWEEP, **RULES**, SDPOINTERS, SESSIOND, SESSIONB_FINDINGS) | `null` — applicator must not reject |

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
| `wa-vcb{nnn}-patch-vcnew-v1-{date}.json` | null | VC session — new classifications (if any) |
| `wa-vcb{nnn}-patch-vcrevise-v1-{date}.json` | null | VC session — revisions to existing classifications (if any) |
| `wa-vcb{nnn}-patch-vcsbflags-v1-{date}.json` | null | VC session — Session B observation flags raised while reading (if any) |
| `wa-vcb{nnn}-patch-vcsdpointers-v1-{date}.json` | null | VC session — cross-registry pointers for Session D (if any) |
| `wa-vcb{nnn}-patch-versecontext-v1-{date}.json` | null | Legacy combined VC patch (pre-v3_3; retained for backwards compatibility) |
| `wa-{nnn}-{word}-patch-preanalysis-v1-{date}.json` | Pre-Analysis Complete | Term classifications, bleed removal |
| `wa-{nnn}-{word}-patch-sessionb-v1-{date}.json` | Analysis Complete | Full analytical data |
| `wa-{nnn}-{word}-patch-sessionb-complete-v1-{date}.json` | Session B Complete | Final output confirmation |

**VC session four-patch set — apply order:** `VCNEW` → `VCREVISE` → `VCSBFLAGS` → `VCSDPOINTERS`. Each independently atomic (own transaction). All four share the session's `batch_id` (VCB-{nnn}) in `_patch_meta` so they trace to one session. A session may produce fewer than four — empty classes produce no patch. See §15 for full detail per type.

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

### 4.14 Prose section type operations (summary)

See §14.2 for the full catalogue. In brief:

- `insert` on `prose_section_type` — add a new section-type handle. Required: `code`, `label`, `source_stage`. Used in CATALOGUE_POPULATION patches (§14.2.1). Applicator uses `INSERT OR IGNORE` on the unique `code`.
- `update` on `prose_section_type` — edit label / description / chapter_no / sort_order / lifecycle_tag / expected_length_min / expected_length_max / source_stage on an existing row. Match on `id` or `code`. Immutable: `id`, `code`. Used in CATALOGUE_POPULATION patches (§14.2.2).

### 4.15 Prose section (content) operations (summary)

See §14.3 – §14.5 for the full catalogue. In brief:

- `insert` on `prose_section` — add a new prose body. Required: `section_type_id` (or `section_type_id_lookup:{code}` — see §4.16), `body`, `status`, `author`. Optional: `registry_id` (NULL = programme-wide), `heading`, `word_count` (auto-derived from body if omitted), `version` (default 1), `metadata_json`, `source_file`.
- `supersede` on `prose_section` — create a new version and link to predecessor. Required: `supersedes_id`, `body`, `author`. `registry_id`, `section_type_id`, and `heading` inherit from the predecessor unless the caller explicitly overrides (rare).
- `approve` on `prose_section` — status → `approved`, stamp `approved_at` + `approved_by`. Accepts `id` (single) or `ids: [...]` (batch). `approved_by` defaults to `"researcher"`.
- `delete` on `prose_section` — soft-delete (`delete_flagged = 1`). Record retained; FTS companion row removed by the `prose_section_ad` trigger. Physical delete is prohibited.
- `bulk_supersede` on `prose_section` — systematic revision across many rows (§14.4.2).

### 4.16 `section_type_id_lookup:{code}` resolver

The applicator accepts either a numeric `section_type_id` or a lookup object `section_type_id_lookup: {"code": "<code>"}` on any `insert` on `prose_section`. When both are present, the numeric id wins. This mirrors the `group_id` string/integer resolution for `verse_context` inserts in §12.2 — the same applicator convention is used, so AI-produced patches do not have to know the integer id at patch-construction time.

```json
{
  "op_id": "OP-001",
  "operation": "insert",
  "table": "prose_section",
  "record": {
    "section_type_id_lookup": { "code": "prog_purp_mission" },
    "registry_id": null,
    "body": "...",
    "status": "draft",
    "author": "claude_ai"
  }
}
```

If the code does not resolve to an existing `prose_section_type` row, the applicator rejects the operation. When a patch inserts a new `prose_section_type` in an earlier `op_id` and then inserts `prose_section` rows for that type, the lookup resolves within the same transaction.

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
    "produced_by": "wa-patch-instruction-v2_3-20260421",
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

Match on `(mti_term_id, group_code)` — both fields are visible in the per-term Session A `.md` (header `mti_term_id`; Existing-groups table `group_code`). The integer `id` is an internal database value the classifier cannot see. Claude Code resolves `(mti_term_id, group_code)` to the integer id at apply time via `verse_context_group` lookup.

```json
{
  "op_id": "OP-002",
  "operation": "update",
  "table": "verse_context_group",
  "match": {
    "mti_term_id": 142,
    "group_code": "142-001"
  },
  "set": {
    "context_description": "{revised text}",
    "notes": "{reason}",
    "delete_flagged": 0
  }
}
```

### 12.5 Insert / update verse_context

**Insert** — use when no active `verse_context` row exists for `(mti_term_id, verse_record_id)`. The `group_id` field accepts a group_code string (e.g. `"142-001"`) for both same-patch new groups and existing groups from prior patches; Claude Code resolves to integer id.

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

**Update** — match on `(mti_term_id, verse_record_id)`. Both fields are visible in the per-term Session A `.md`. The pair is DB-unique (uniqueness index `sqlite_autoindex_verse_context_1` on `(verse_record_id, mti_term_id)`), so this match resolves to at most one row. Applicator rejects 0-row matches per A-06.

```json
{
  "op_id": "OP-004",
  "operation": "update",
  "table": "verse_context",
  "match": {
    "mti_term_id": 142,
    "verse_record_id": 4821
  },
  "set": {
    "group_id": "142-001",
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

## 13. Rules and Addenda Updates (new in v2_2; four-field shape in v2_3)

### 13.1 Background

Pre-M33, global rules lived in `data/imports/WA/Workflow/Framework_B/Session_B/wa-global-general-rules-v{n}.json` and were edited directly. Post-M33 (2026-04-20), rules and addenda live in `wa_rule_registry` + `wa_addendum_registry`; the JSON seed file is retained for audit only. All rules changes flow through RULES patches so that (a) the DB remains canonical, (b) a per-patch backup is taken, and (c) the change is auditable via `engine_run_log`.

**Four-field rule structure (DIR-20260421-001, 2026-04-21).** Per researcher decision of 2026-04-21 (Option B, Pattern 1 field split), rule content is split across four nullable TEXT fields on `wa_rule_registry`:

| Field | Purpose | Populated |
|---|---|---|
| `rule_text` | Concise binding statement — what the rule requires. Read at session start as the compliance spec. | Always (NOT NULL) |
| `rationale` | Why the rule exists — the failure mode or incident that motivated it. | Where known |
| `application_notes` | How to apply the rule, edge cases, scope discipline, AI drafting checks. | Where needed |
| `examples` | Illustrations, trigger phrases, failure-mode phrases, correct-response phrases. | Where useful |

All four fields are nullable. A minimal rule carries only `rule_text`. A fully-developed rule carries all four. The rewritten GR-LOAD-001 v3_2, GR-HF-001 v1_1, GR-TEMPO-001 v1_1, GR-REF-001 v1_1, GR-REF-002 v1_1 (applied via PATCH-20260421-RULES-WORDY-RESTRUCTURE-V1) are the worked reference models.

The pre-existing singular `example` column is retained (schema back-compat): 3 rules (GR-FILE-001, GR-FILE-007, GR-FILE-009) carry a correct-vs-wrong filename illustration there. New rules should populate `examples` (plural) where multiple illustrations are needed; the singular column is considered legacy and should not accumulate new content.

Companion document: **docs/rules-update-protocol.md** — covers the three ways to initiate a rules change (conversational, markdown round-trip, direct edit — avoid) and the end-to-end workflow for researchers. This section covers the patch format.

### 13.2 When to use a RULES patch

Use a RULES patch to:

- Insert a new rule (`wa_rule_registry`) — populate `rule_text` (required) and any of `rationale`, `application_notes`, `examples` that apply.
- Revise any body field of an existing rule (`rule_text`, `rationale`, `application_notes`, `examples`) or its metadata (`category`, `version`, `subject`, `applies_to`, `addendum_ref`, `source_document`, `example` legacy).
- Deprecate a rule (mark obsolete, optionally record `superseded_by`).
- Insert a new addendum (`wa_addendum_registry`) — rare post-M36; most guidance belongs in a rule field.
- Revise an existing addendum.

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
    "rule_text": "Concise binding statement. What the rule requires, in the form Claude AI reads at session start. Multi-line text uses \\n escapes.",
    "rationale": "Why this rule exists — the failure mode or incident that motivated it. Populated when known.",
    "application_notes": "How to apply the rule. Edge cases, scope discipline, AI drafting checks. Populated when needed.",
    "examples": "Trigger phrases, failure-mode phrases, correct-response phrases. Populated when useful.",
    "applies_to": "all sessions",
    "version": "1.0",
    "added_date": "20260421",
    "source_document": "PATCH-20260421-RULES-GR-NEW-001-INSERT-V1"
  }
}
```

Required: `rule_id` (unique), `category`, `subject`, `rule_text`.
Optional body fields: `rationale`, `application_notes`, `examples` (all TEXT, nullable; see §13.1 on the four-field shape).
Optional metadata: `applies_to`, `version`, `added_date`, `source_document`, `addendum_ref`, `example` (legacy singular — retained for back-compat only; prefer `examples`).

Category convention: lowercase snake-case (`session_startup`, `load_requirement`, `process_discipline`, `document_discipline`, `file_naming`, `programme_orientation`, etc.). Normalise on draft — the reference set is the categories already present in `wa_rule_registry` (visible in the rules extract §8.3).

#### 13.4.2 `update` on `wa_rule_registry`

```json
{
  "op_id": "OP-002",
  "table": "wa_rule_registry",
  "operation": "update",
  "match": { "rule_id": "GR-FILE-003" },
  "set": {
    "rule_text": "Revised binding statement...",
    "rationale": "Added: why the rule exists...",
    "application_notes": "Added: scope discipline + AI drafting check...",
    "examples": "Added: trigger phrases + correct-response phrases...",
    "version": "3.1",
    "category": "file_naming"
  }
}
```

`match` must specify `rule_id`. `set` accepts any updatable column; unknown columns are dropped per §5.3. Immutable fields (`id`, `rule_id`, `created_at`) are protected — the applicator rejects attempts to overwrite them.

Any of the four body fields (`rule_text`, `rationale`, `application_notes`, `examples`) can appear in `set` independently — updating only the rationale, for example, without disturbing the binding statement in `rule_text`. This is the independent-auditability property motivating the four-field split (see §13.1).

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

### 13.5 Worked examples

Two applied RULES patches from 2026-04-21 are the reference models:

**(a) Single-field rewrite — session-startup recategorisation.**
See `archive/patches/wa-rules-gr-load-001-update-v1-20260421.json`. Recategorised GR-LOAD-001 + GR-OBS-001 into `session_startup` and made the startup sequence explicit. Only `rule_text`, `category`, `version`, `added_date` were touched — the new body fields (`rationale`, `application_notes`, `examples`) had not yet been added to the schema.

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-20260421-RULES-SESSION-STARTUP-V1",
    "patch_type": "RULES",
    "produced_by": "wa-patch-instruction-v2_2-20260421",
    "session_b_status": null,
    "researcher_approval": "PENDING"
  },
  "operations": [
    { "op_id": "OP-001", "table": "wa_rule_registry", "operation": "update",
      "match": { "rule_id": "GR-LOAD-001" }, "set": { "category": "session_startup", "rule_text": "...", "version": "3_1", "added_date": "20260421" } }
  ]
}
```

**(b) Four-field restructure — wordy-restructure patch.**
See `archive/patches/wa-rules-wordy-restructure-update-v1-20260421.json`, sequenced after DIR-20260421-001 added the three new columns. Six rules (GR-PROG-005, GR-LOAD-001, GR-HF-001, GR-TEMPO-001, GR-REF-001, GR-REF-002) rewritten with the binding statement narrowed into `rule_text` and commentary moved into `rationale` / `application_notes` / `examples`. Representative operation:

```json
{
  "op_id": "OP-002",
  "table": "wa_rule_registry",
  "operation": "update",
  "match": { "rule_id": "GR-LOAD-001" },
  "set": {
    "rule_text": "Claude AI reads this file in full at the start of every session...",
    "rationale": "Claude AI forgets between sessions. This load gate exists to...",
    "application_notes": "Familiarisation semantics. When the researcher uses the verb 'familiarise'...",
    "examples": "Familiarisation trigger phrases: 'familiarise yourself with the attached'...",
    "version": "3_2",
    "last_modified": "20260421"
  }
}
```

Note `researcher_approval: "PENDING"` in `_patch_meta` — a convention for RULES patches to make the approval step explicit. The applicator does not enforce this field; the researcher's verbal/chat approval remains the gate.

When a RULES patch depends on a schema change (such as the three new columns added by DIR-20260421-001), the directive must be executed and confirmed first; then the patch applies cleanly. Applicator rejection on column-not-found is evidence the ordering was skipped.

### 13.6 Workflow summary

1. Researcher tells CC in chat what to change (conversational path) — or hands over a marked-up MD extract (markdown round-trip).
2. CC drafts the RULES patch per §13.3 / §13.4. When the patch depends on a schema change (new columns, new tables), CC drafts the directive first and the patch second, sequenced per §13.5(b).
3. CC runs the §7 self-check and presents the patch (and any directive) to the researcher.
4. Researcher approves (typically in chat).
5. CC executes the directive (if any), then applies the patch: `python scripts/apply_session_patch.py {patch_file}`.
6. CC regenerates the rules extract: `python scripts/build_rules_extract.py --also-markdown`. `build_rules_extract.py` surfaces all four body fields — `rule_text`, `rationale`, `application_notes`, `examples` — conditionally (back-compat with pre-DIR-20260421-001 databases); the MD renderer prints each as a named section under the rule.
7. CC commits the patch artefact + regenerated extract files.
8. AI sessions starting after the regeneration see the updated vocabulary and rule bodies.

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

## 14. Prose Updates (new in v2_4)

### 14.1 Background

The prose store (`prose_section` + `prose_section_type` + `prose_section_fts` + `prose_section_dimension_link` + `prose_section_finding_link`, schema v3.10.0 M20 + extensions to v3.14.0) holds all narrative output — Session A auto-generated summaries, Session B/C/D analytical prose, and programme-wide narrative. Each row in `prose_section_type` is a handle (a reusable slot), and each row in `prose_section` is a body of text filling that slot for a given registry (or NULL for programme-wide scope, after DIR-20260421-002).

This section is the authoritative operation catalogue for both tables. Use it as the canonical reference — do not duplicate it elsewhere. Decision logic for *when* a change goes through a directive vs a patch is in §1.4 and in wa-directive-instruction [current] §10.

Hard rules applied throughout this section, restated so there is no ambiguity:

- **Narrative prose is supersede-only.** To change the content of a narrative `prose_section` row, create a new row via `supersede`. The predecessor remains in the table as `delete_flagged = 0` with `superseded_by_id` set.
- **Session A mechanical extracts are the single exception** — they use `session_a_replace` (in-place UPDATE), which only applies when `author = 'claude_code'`.
- **Physical deletes are prohibited** — `delete` is soft (`delete_flagged = 1`); the applicator rejects any attempt to execute raw `DELETE FROM prose_section`.
- **Schema changes do not go through patches.** Adding a column, relaxing a constraint, adding a new related table: schema enablement directive per wa-directive-instruction [current] §10.
- **`prose_section_type` edits are live-in-place.** Editing a handle's metadata does not create a new type row — the `update` operation (§14.2.2) modifies in place.

### 14.2 Section-type operations (handles)

Handles (section types) live in `prose_section_type`. They are reusable shells; edits to their metadata (label, description, ordering) are live-in-place.

Filename and `patch_type` conventions for handle changes:

| Field | Value |
|---|---|
| `patch_type` | `CATALOGUE_POPULATION` |
| `session_b_status` | `null` (exempt) |
| Filename | `wa-catalogue-prose-{scope}-v{n}-{YYYYMMDD}.json` — where `{scope}` is the subject (e.g. `programme-ch01`, `session-b-ch2c`) |
| `patch_id` | `PATCH-{YYYYMMDD}-CATALOGUE-PROSE-{SCOPE}-V{n}` (uppercase) |

#### 14.2.1 `insert` on `prose_section_type`

Add a new handle. Uses `INSERT OR IGNORE` on the unique `code` — running the same insert twice is a no-op on the second run.

```json
{
  "op_id": "OP-001",
  "operation": "insert",
  "table": "prose_section_type",
  "record": {
    "code": "prog_purp_mission",
    "label": "Mission",
    "source_stage": "programme",
    "chapter_no": 1,
    "sort_order": 2,
    "description": "One-paragraph statement of what this programme is investigating, why, and what outcome would constitute success.",
    "expected_length_min": 150,
    "expected_length_max": 300,
    "lifecycle_tag": null
  }
}
```

Required: `code` (unique, lowercase snake-case), `label`, `source_stage` (`programme` | `session_a` | `session_b` | `session_c` | `session_d`).
Optional: `chapter_no`, `sort_order` (default 999), `description`, `expected_length_min`, `expected_length_max`, `lifecycle_tag`.

#### 14.2.2 `update` on `prose_section_type`

Edit handle metadata in place. Match on `id` or `code`. `id` and `code` are immutable — silently dropped from `set` if supplied.

```json
{
  "op_id": "OP-002",
  "operation": "update",
  "table": "prose_section_type",
  "match": { "code": "prog_purp_mission" },
  "set": {
    "description": "Revised short description…",
    "sort_order": 2,
    "chapter_no": 1
  }
}
```

Mutable fields: `label`, `description`, `chapter_no`, `sort_order`, `lifecycle_tag`, `expected_length_min`, `expected_length_max`, `source_stage`. Unknown columns are dropped with a `[NOTE]` message; the operation does not fail.

**To rename a handle's `code`:** this is not a field update. Either soft-retire the old handle (no delete op exists for `prose_section_type` — use `update` to move `sort_order` to a large value and add a `[deprecated]` marker to the label, then create a new handle with the new code), or raise a directive for a true rename. The design choice is deliberate: codes are referenced by `section_type_id_lookup` and should not drift.

### 14.3 `insert` on `prose_section`

Add a new prose body under an existing handle.

Filename and `patch_type` conventions for content changes:

| Field | Value |
|---|---|
| `patch_type` | `PROSE` |
| `session_b_status` | `null` (exempt) |
| Filename (programme-wide) | `wa-prose-programme-{topic}-v{n}-{YYYYMMDD}.json` |
| Filename (registry-scoped) | `wa-{nnn}-{word}-prose-{topic}-v{n}-{YYYYMMDD}.json` |
| `patch_id` | `PATCH-{YYYYMMDD}-PROSE-{SCOPE}-V{n}` |

```json
{
  "op_id": "OP-003",
  "operation": "insert",
  "table": "prose_section",
  "record": {
    "section_type_id_lookup": { "code": "prog_purp_mission" },
    "registry_id": null,
    "heading": "Mission",
    "body": "The programme investigates…",
    "status": "draft",
    "version": 1,
    "author": "claude_ai",
    "source_file": "wa-prose-draft-purp-mission-v2-20260422.md"
  }
}
```

Required: `section_type_id` (numeric) **or** `section_type_id_lookup:{code}` (see §4.16); `body`; `status` (`draft` | `in_review` | `approved` | `archived`); `author` (`claude_ai` | `claude_code` | `researcher`).
Optional: `registry_id` (NULL = programme-wide; integer = registry-scoped); `heading`; `word_count` (auto-derived from body whitespace-split if omitted); `version` (default 1); `metadata_json`; `source_file`; `approved_at`; `approved_by`.

Post-insert, the `prose_section_ai` trigger populates `prose_section_fts` automatically — no separate step.

### 14.4 `supersede` on `prose_section` — the only edit path for narrative prose

Revisions to narrative prose always create a new row. The predecessor is retained.

```json
{
  "op_id": "OP-004",
  "operation": "supersede",
  "table": "prose_section",
  "supersedes_id": 2,
  "record": {
    "body": "Revised body for the Mission section…",
    "author": "claude_ai",
    "source_file": "wa-prose-draft-purp-mission-v3-20260423.md",
    "status": "draft"
  }
}
```

Required: `supersedes_id` (the `prose_section.id` of the row being superseded); `body`; `author`.

**Field inheritance (important):** `registry_id`, `section_type_id`, and `heading` are inherited from the predecessor unless the caller explicitly supplies them in `record`. This keeps supersede operations minimal — typical revision payloads carry only `body` + `author`. Override only when relocating prose to a different section type (rare) or correcting a miscategorisation.

Applicator behaviour:
1. Fetch predecessor row.
2. Compute `new_version = predecessor.version + 1`.
3. Insert new row with `supersedes_id = predecessor.id`, inherited + supplied fields.
4. Update predecessor: `superseded_by_id = new.id`.
5. `prose_section_au` trigger updates the FTS row (removes the old, adds the new).

**Authorship on revision.** The `author` field on the new row is **who made the change** — not inherited from the predecessor. A revision drafted by Claude AI of a researcher-authored row carries `author = 'claude_ai'`; provenance of the earlier row is preserved via `supersedes_id`. This is a researcher-confirmed convention (2026-04-22).

#### 14.4.1 `bulk_supersede` — systematic programme-wide revisions

For sweeping edits across many rows (e.g. a terminology pass that touches 20 prose sections), use `bulk_supersede`:

```json
{
  "op_id": "OP-005",
  "operation": "bulk_supersede",
  "table": "prose_section",
  "targets": [
    { "id": 2, "body": "Revised body A…" },
    { "id": 3, "body": "Revised body B…" }
  ],
  "rec_template": { "author": "claude_ai", "status": "draft" }
}
```

Each `targets[i]` can override any field from `rec_template`. Applicator iterates, producing one supersede per target. All in a single transaction — all-or-nothing.

### 14.5 Lifecycle transitions — `approve`, `delete`

#### 14.5.1 `approve` (single row or batch)

Transitions `status` → `'approved'` and stamps `approved_at` + `approved_by`. Rows already at `approved` are skipped (idempotent).

Single row:
```json
{
  "op_id": "OP-006",
  "operation": "approve",
  "table": "prose_section",
  "id": 5,
  "approved_by": "researcher"
}
```

Batch (preferred when approving a session's output in one go):
```json
{
  "op_id": "OP-007",
  "operation": "approve",
  "table": "prose_section",
  "ids": [1, 2, 3, 4, 5, 6, 7],
  "approved_by": "researcher"
}
```

`approved_by` defaults to `"researcher"` if omitted. The applicator returns the count of rows that actually transitioned (rows already `approved` are reported as skipped).

#### 14.5.2 `delete` (soft-delete)

Sets `delete_flagged = 1`. The `prose_section_ad` trigger removes the row from `prose_section_fts`. The row remains in `prose_section` for audit.

```json
{
  "op_id": "OP-008",
  "operation": "delete",
  "table": "prose_section",
  "id": 7
}
```

Required: `id`. No other fields.

Physical deletes are prohibited (GR-OBS-005 / §5.4).

### 14.6 Immutability discipline (restated)

| You want to… | Do this | Do NOT do this |
|---|---|---|
| Fix a typo in a narrative `prose_section` body | `supersede` with the fixed body | Write an `update` operation — there is no in-place update for narrative prose |
| Rename a handle | `update` the `label` (display name) | Attempt to `update` the `code` — it's immutable; codes do not drift |
| Move prose content to a different handle | `supersede` the existing row, supplying the new `section_type_id` in `record` | Create a new row and soft-delete the old — that loses the supersedes chain |
| Replace a Session A auto-generated summary | `session_a_replace` (restricted to `author = 'claude_code'`) | Use `supersede` — mechanical Session A regenerations must not pollute the supersede chain |
| Retire a handle | Re-word the label to mark deprecation; move sort_order to a high number | Delete the handle — no delete op exists, and removing it would orphan existing content rows |

### 14.7 Worked sequence — adding a new area of programme prose

End-to-end example, parallel to the 2026-04-21 chapter 0-1 seed:

1. **Schema enablement directive** (if the change requires schema relaxation, e.g. a new column on `prose_section` — wa-directive-instruction [current] §10). Most prose additions do not need this step; it was required once for the programme-wide case to relax `registry_id NOT NULL`.
2. **CATALOGUE_POPULATION patch** inserting the new handles for the area:
   - Filename: `wa-catalogue-prose-{area}-v1-{YYYYMMDD}.json`
   - One `insert` on `prose_section_type` per handle.
3. **PROSE patch** inserting prose bodies under the new handles:
   - Filename: `wa-prose-{scope}-{topic}-v1-{YYYYMMDD}.json`
   - One `insert` on `prose_section` per body, using `section_type_id_lookup:{code}` to resolve the handle id.
4. **PROSE patch (optional)** — batch approve once the researcher has reviewed:
   - One `approve` operation with `ids: [...]` listing all rows to transition.
5. **Regenerate the extract** — `python scripts/build_programme_prose_extract.py --all-formats` produces JSON + MD + DOCX in `data/exports/reference/` + `outputs/docx/`.
6. **Commit** — patch artefacts (input files auto-archived by applicator), regenerated extracts, any script updates.

### 14.8 Worked sequence — revising existing prose

1. **Produce the revised body** in a source file under `data/imports/WA/Prose/` (convention — the `source_file` field will reference it).
2. **PROSE patch** with one `supersede` per row being revised:
   - Filename: `wa-prose-{scope}-{topic}-rev-v{n}-{YYYYMMDD}.json`
   - `supersedes_id` = the `prose_section.id` being revised.
   - `record.body` = the new body. `record.author` = who drafted the revision.
3. **Regenerate the extract** — the MD / DOCX reflect the new version automatically.
4. **Batch approve** (optional) once reviewed.

### 14.9 Self-check for PROSE and CATALOGUE_POPULATION patches

In addition to the standard §7 self-check:

1. `patch_type` is `PROSE` or `CATALOGUE_POPULATION` (not `RULES` or `REPAIR`).
2. `session_b_status` is `null` (both types are exempt per §3.4).
3. Operations do not mix — a `PROSE` patch contains only `prose_section` operations; a `CATALOGUE_POPULATION` patch contains only `prose_section_type` operations (plus optionally `wa_obs_question_catalogue` inserts for question catalogue population). **A patch that mixes handle inserts and content inserts is split into two patches.**
4. Every `insert` on `prose_section` either supplies `section_type_id` (integer) or `section_type_id_lookup:{code}` — never both absent.
5. Every `supersede` on `prose_section` supplies `supersedes_id`, `record.body`, and `record.author`.
6. Every `approve` supplies either `id` or `ids`.
7. No `update` on `prose_section` (not a supported operation for narrative prose). The self-check rejects any such operation before submission.

---

## 15. VC Session Four-Patch Catalogue (new in v2_5)

A Verse Context session produces up to four independently-applied patches, one per output class. The session is identified by its `batch_id` (VCB-{nnn}) — all four patches of the same session carry the same `batch_id`. Each patch is session_b_status-exempt (`null` required per §3.4). A session may produce fewer than four patches — empty classes produce no patch. See the VC instruction v3_3+ for full session workflow; this section documents patch structure.

### 15.1 Apply order

`VCNEW` → `VCREVISE` → `VCSBFLAGS` → `VCSDPOINTERS`. The order matters only for the first two (VCNEW inserts groups that VCREVISE may reference; both touch `verse_context_group` and `verse_context`). The flag patches (VCSBFLAGS, VCSDPOINTERS) are independent.

Each patch is applied in its own transaction. A failure in any one patch does not roll back prior patches from the same session — the researcher re-prepares and re-applies the failed patch.

### 15.2 VCNEW — new classifications

**Purpose:** insert new `verse_context_group` and `verse_context` rows for terms being classified for the first time in this session.

**Required `_patch_meta` fields** (in addition to §3.2 standard):

- `terms_covered` — array of `mti_term_id`s receiving first-time classification.
- `input_versions` — **required under v2_6 (A-03 version gate)** — a map `{mti_term_id: md_version}` carrying the `md_version` stamped in the per-term `.md` header the classifier worked from. The applicator compares each declared version to the current `mti_terms.md_version` in the DB; **any mismatch rejects the whole patch as stale**. Keys may be JSON numbers or strings; the applicator normalises both to int.
- `governing_instruction` — filename of the governing VC instruction version.
- `batch_id` — **optional (A-04)**. Retained as a convenience field for human audit grouping; the per-term version gate is the authoritative correlation.

**Supported operations:** `insert` on `verse_context_group`, `insert` on `verse_context`. No `update` operations in VCNEW (those belong in VCREVISE).

**Applicator behaviour (per VC-2 extension, post-v3_4):** the applicator runs two gates BEFORE any state change. (1) Version gate: for every term in `terms_covered`, input_versions[term] must equal current `mti_terms.md_version`; mismatch rejects. (2) R1–R4 + orphan-group + coverage validation per term after operations apply. On success: writes `mti_terms.vc_status = 'vc_completed'` (A-02: renamed from 'complete'), `vc_instruction_version = {governing_instruction}`, `vc_status_updated_at = now()`, `vc_status_note = NULL`, and **bumps** `md_version` (any pre-existing `.md` is now stale). Then derives affected registries and runs the aggregation check (see §13 of the VC instruction).

**Example `_patch_summary`:**

```json
{
  "_patch_summary": {
    "total_operations": 14,
    "group_inserts": 4,
    "verse_context_inserts_anchor": 5,
    "verse_context_inserts_related": 3,
    "verse_context_inserts_set_aside": 2
  }
}
```

### 15.3 VCREVISE — revisions to existing classifications

**Purpose:** update existing `verse_context_group` and `verse_context` rows — revise group descriptions, dissolve groups (`delete_flagged = 1`), reclassify verses (move between groups, change relevance, promote/demote anchors).

**Required `_patch_meta` fields:**

- `terms_covered` — array of `mti_term_id`s being revised.
- `input_versions` — **required (A-03 version gate)** — map `{mti_term_id: md_version}`. Same contract as VCNEW: applicator rejects on stale mismatch; bumps on apply.
- `governing_instruction` — filename of the governing VC instruction version.
- `batch_id` — **optional (A-04)**.

**Supported operations:** `update` on `verse_context_group` (including setting `delete_flagged = 1`), `update` on `verse_context`. No `insert` operations in VCREVISE (those belong in VCNEW).

**Applicator behaviour:** same version gate and aggregation logic as VCNEW. Validates per-term R1–R4 + orphan-group + coverage for each term in `terms_covered`. On success: writes `vc_status = 'vc_completed'` (or retains it if already at that state), updates `vc_instruction_version` + `vc_status_updated_at`, and bumps `md_version`. Term-state downgrade (e.g. to `'to_revise'`) is not a VCREVISE effect; that is a separate directive.

**Example `_patch_summary`:**

```json
{
  "_patch_summary": {
    "total_operations": 9,
    "group_updates_description": 2,
    "group_dissolves": 1,
    "verse_context_updates": 4,
    "anchor_promotions": 1,
    "anchor_demotions": 1
  }
}
```

### 15.4 VCSBFLAGS — Session B observation flags

**Purpose:** insert flags into `wa_session_research_flags` for observations raised while reading verses that will need attention at Session B analysis.

**Required `_patch_meta` fields:** `governing_instruction`. `batch_id` and `terms_covered` are optional (each flag row carries `strongs_reference` for term attribution). `input_versions` is **not** required for flag patches — these do not change classification state and do not interact with the A-03 version gate.

**Supported operations:** `insert` on `wa_session_research_flags`. Required record fields per row:

- `registry_id` — integer; the registry the flag is raised against
- `file_id` — integer; resolved by Claude Code from `registry_id` if not supplied
- `flag_code` — one of: `SB_FINDING`, `SB_INNER_BEING`, `PH2_CROSS_REF_ENRICHMENT`, `PH2_THEOLOGICAL_DEPTH_REQUIRED`, `PH2_EXEGETICAL_STUDY_REQUIRED`, `PH2_BOUNDARY_QUESTION`
- `flag_label` — one-line summary
- `strongs_reference` — the term the flag relates to
- `priority` — `'low'` | `'normal'` | `'high'`
- `session_target` — `'Session B'` (fixed for VCSBFLAGS)
- `description` — full observation text, self-contained
- `session_raised` — the session id (`VCB-{nnn}`)
- `raised_date` — ISO timestamp
- `resolved` — `0` at raise time

**Applicator behaviour:** standard `wa_session_research_flags` insert (already supported). No per-term `vc_status` writes (this patch does not touch classification state).

**Example `_patch_summary`:**

```json
{
  "_patch_summary": {
    "total_operations": 5,
    "research_flag_inserts": 5,
    "by_flag_code": {
      "SB_FINDING": 3,
      "SB_INNER_BEING": 1,
      "PH2_CROSS_REF_ENRICHMENT": 1
    }
  }
}
```

### 15.5 VCSDPOINTERS — Session D cross-registry pointers

**Purpose:** insert flags into `wa_session_research_flags` for cross-term or cross-registry observations raised while reading verses — signals that point at another term or registry for Session D synthesis.

**Required `_patch_meta` fields:** same as VCSBFLAGS.

**Supported operations:** `insert` on `wa_session_research_flags`. Required record fields per row (as for VCSBFLAGS, plus):

- `flag_code` — one of: `SD_POINTER`, `SD_CLUSTER`, `PH2_CROSS_REGISTRY_REQUIRED`, `THEMATIC_LINK`
- `cross_registry_id` — the **other** registry the observation points to (required, integer)
- `session_target` — `'Session D'` (fixed for VCSDPOINTERS)

**Applicator behaviour:** standard `wa_session_research_flags` insert. No per-term `vc_status` writes.

**Example `_patch_summary`:**

```json
{
  "_patch_summary": {
    "total_operations": 3,
    "research_flag_inserts": 3,
    "by_flag_code": {
      "SD_POINTER": 2,
      "THEMATIC_LINK": 1
    },
    "distinct_cross_registries": 2
  }
}
```

### 15.6 Self-check for the four VC session patches

In addition to the standard §7 self-check:

1. `patch_type` is exactly one of `VCNEW`, `VCREVISE`, `VCSBFLAGS`, `VCSDPOINTERS`.
2. `session_b_status` is `null` (all four are exempt per §3.4).
3. For `VCNEW` and `VCREVISE`: `terms_covered` is a non-empty array; every `mti_term_id` referenced in operations is present in `terms_covered`.
4. **For `VCNEW` and `VCREVISE` (A-03 version gate):** `input_versions` is a map covering every term in `terms_covered`; every value is a positive integer. At submission time, each `input_versions[{term}]` must equal the `md_version` in the per-term `.md` the classifier worked from. (The applicator will re-verify against current DB state and reject on mismatch.)
5. For `VCNEW`: every operation is an `insert`. No `update` operations.
6. For `VCREVISE`: every operation is an `update`. No `insert` operations.
7. For `VCSBFLAGS`: every operation is `insert` on `wa_session_research_flags`; every record has `session_target = 'Session B'`; `flag_code` from the VCSBFLAGS allowed list (§15.4). `input_versions` not required.
8. For `VCSDPOINTERS`: same but `session_target = 'Session D'`; `cross_registry_id` present and non-null on every row; `flag_code` from the VCSDPOINTERS allowed list (§15.5). `input_versions` not required.
9. No mixing — a patch of one of these four types contains only operations appropriate for that type.
10. `batch_id` is **optional** (A-04). If present, it groups session artefacts for human audit; if absent, no consequence.

---

*wa-patch-instruction-v2_6-20260424 | Supersedes wa-patch-instruction-v2_5-20260424 | v2_6 adds A-03 version-gate support: `_patch_meta.input_versions` (map {mti_term_id: md_version}) required for VCNEW and VCREVISE; applicator rejects stale mismatches and bumps md_version on apply. `_patch_meta.batch_id` reclassified as optional (A-04). §15.2 / §15.3 / §15.4 / §15.5 / §15.6 updated. A-02: vc_status values now reference 'vc_completed' (was 'complete'; 'approved' dropped).*

*Historical: wa-patch-instruction-v2_5-20260424 | Supersedes wa-patch-instruction-v2_4-20260422 | v2_5 adds §15 VC Session Four-Patch Catalogue (VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS) supporting the per-term VC session output model; §3.3 and §3.4 updated; §3.6 pipeline sequence extended with the four new rows.*

*Historical: wa-patch-instruction-v2_4-20260422 | Supersedes wa-patch-instruction-v2_3-20260421 | Prior: v2_2-20260421 + v2_1-20260418 + v2_0-20260418 + wa-patch-specification-v1_14-20260416 + wa-sessionb-cc-instructions-v3_6 §4, §15, §16 | Absorbs addenda ADD-PATCHDIR-001, -004, -005, -007, -008 from global rules v2_10 | v2_3 added four-field rule shape; v2_4 adds full Prose Updates catalogue (§14) with directive-vs-patch decision logic and narrative-prose immutability discipline*
