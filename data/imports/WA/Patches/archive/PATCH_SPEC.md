# Bible Projects — Database Patch JSON Specification
Version: 1.3  
Date: 2026-03-20

This specification defines the required format for all database patch files targeting the Bible Projects SQLite database. Pass these instructions to any system (Claude or other) producing patch files.

---

## File naming convention

```
<scope>-patch-<YYYYMMDD>-v<N>.json
```

Examples:
- `registry-patch-20260317-v1.json`
- `phase2-flag-reassessment-20260319-v1.json`
- `stem-extraction-patch-20260319-v1.json`
- `word-descriptions-patch-20260319-v1.json`

Use lowercase with hyphens. Increment `v<N>` for revisions within the same session.

---

## Patch formats

Two formats are recognised. Choose based on the nature of the operation.

### Format A — Structured operation-block format (recommended for INSERT/UPDATE patches against a single table or tightly related tables)

Uses `_meta` + named operation blocks. The import script generates SQL from the structured data. Suitable when explicit ID assignment and cross-block FK references are needed.

See sections below for full specification.

### Format B — Simplified flat format (used for Claude-native analysis patches)

Used when Claude produces analytical output covering many terms across the corpus (e.g. flag assessments, meaning stem extraction, word descriptions). Top-level keys are free-form; list sections replace the operation-block structure.

```json
{
  "patch_id":    "descriptive-name-YYYYMMDD-v1",
  "produced_at": "2026-03-19T17:51:31Z",
  "description": "One sentence describing what this patch does.",
  "summary":     { "terms_assessed": 1517, "flags_to_insert": 2361, ... },
  "inserts":     [ { "term_inv_id": 1, "flag_code": "THIN_DATA", ... } ],
  "deletes":     [ { "term_inv_id": 30, "flag_code": "CROSS_PART_ROOT", ... } ]
}
```

Rules for Format B:
- `patch_id` and `produced_at` are required.
- `summary` is required and contains counts for human verification.
- List sections (`inserts`, `deletes`, `records`, etc.) are named descriptively.
- FKs in list rows use **code/name values** (e.g. `flag_code`, `strongs_number`) — the apply script resolves integer IDs from the live DB. Never include raw integer FK IDs.
- Apply scripts for Format B patches must **always resolve FKs by code lookup** and never trust patch-internal integer IDs.

---

## Top-level structure (Format A)

Every Format A patch file must have exactly these top-level keys:

```json
{
  "_meta": { ... },
  "<block_name>": { ... },
  "<block_name_2>": { ... }
}
```

- `_meta` — required, always first.
- One or more named **operation blocks** — name them descriptively, e.g. `phase2_flag_types_insert`, `word_registry_insert`, `wa_term_inventory_update`.
- No `sql_statements` array — SQL is generated from the structured data. Do not include it.

---

## `_meta` block

```json
"_meta": {
  "patch_id": "REG-PATCH-20260317-002",
  "supersedes": "REG-PATCH-20260317-001",
  "date": "2026-03-17",
  "description": "One sentence describing what this patch does.",
  "reason": "Why this patch is needed. Can be multi-sentence.",
  "produced_by": "Claude (session context)",
  "import_order": [
    "1. Execute word_registry_insert first",
    "2. Then execute wa_file_index_insert"
  ],
  "format": "bible-projects-patch-spec-v1.1",
  "id_baseline": {
    "word_registry": 194,
    "phase2_flag_types": 14
  }
}
```

Required fields: `patch_id`, `date`, `description`, `id_baseline`, `format`.  
Optional fields: `supersedes`, `reason`, `produced_by`, `import_order`.  
`import_order` is required when the patch contains more than one operation block.

`id_baseline` records the `MAX(id)` values queried from the DB at the time the patch was produced. This lets the import script verify the DB has not changed between patch creation and application, and lets any human reviewer understand how IDs were assigned.

```json
"id_baseline": {
  "word_registry": 194,
  "phase2_flag_types": 14
}
```

---

## ID assignment — required procedure for the source system

Before producing any patch that includes INSERT rows with explicit IDs, the source system **must** query the current maximum ID for every affected table and assign IDs sequentially from `MAX(id) + 1`.

### Why this matters

1. **Correctness** — prevents collisions with rows inserted since the last known state.
2. **Cross-block references** — when one block inserts into table A and a second block needs those new IDs as foreign keys into table B, the IDs must be known at patch-creation time. The source system resolves this by querying MAX(id) first, computing the new IDs, and using them consistently across all blocks in the same patch.
3. **AUTOINCREMENT tables** — SQLite AUTOINCREMENT tables normally assign their own IDs. When a subsequent block in the same patch needs those IDs as FKs, include `id` in the `columns` list and assign explicit values (SQLite honours an explicit `id` on INSERT even for AUTOINCREMENT tables). Record the baseline in `_meta.id_baseline` so the import script can verify the DB state has not diverged.

### Procedure

```
1. Query: SELECT MAX(id) FROM <table>  → baseline_id
2. Assign new rows: baseline_id + 1, baseline_id + 2, ...
3. Record in _meta.id_baseline: { "<table>": baseline_id }
4. Use those IDs in all rows and any cross-block FK references
```

If the table is empty, treat `MAX(id)` as `0`.

### Example — two related blocks in one patch

```json
"_meta": {
  "id_baseline": {
    "wa_file_index": 52,
    "wa_term_inventory": 610
  }
},
"wa_file_index_insert": {
  "target_table": "wa_file_index",
  "operation": "INSERT",
  "conflict_action": "IGNORE",
  "columns": ["id", "filename", "registry_id", "word"],
  "rows": [
    { "id": 53, "filename": "WA-196-power-data-20260317.json", "registry_id": "196", "word": "power" }
  ]
},
"wa_term_inventory_insert": {
  "target_table": "wa_term_inventory",
  "operation": "INSERT",
  "conflict_action": "IGNORE",
  "columns": ["id", "file_id", "language", "term_id", "transliteration"],
  "rows": [
    { "id": 611, "file_id": 53, "language": "Greek", "term_id": "G1411", "transliteration": "dunamis" }
  ]
}
```

Here `file_id: 53` in `wa_term_inventory` matches the explicitly assigned `id: 53` in `wa_file_index`. Both are derived from `MAX(id)` queries made before writing the patch.

---

## Operation block structure

Each operation block describes a single table operation.

### INSERT block

```json
"<table_name>_insert": {
  "target_table": "<exact SQLite table name>",
  "operation": "INSERT",
  "conflict_action": "IGNORE",
  "columns": ["col1", "col2", "col3"],
  "row_counts": {
    "total_rows": 6
  },
  "rows": [
    {
      "col1": "value",
      "col2": 123,
      "col3": null,
      "_ref": {
        "human_note": "Optional — for verification only. Never imported."
      }
    }
  ]
}
```

**`conflict_action`** must be one of:
- `"IGNORE"` — silently skip rows that violate a UNIQUE or PRIMARY KEY constraint. Use this when the patch may be re-run or when partial data may already exist.
- `"REPLACE"` — overwrite existing rows with the same primary key. Use only when intentionally overwriting.
- `"FAIL"` — raise an error on any conflict. Use when you are certain rows are absent and want strict guarantees.

Default for all new patches: `"IGNORE"`.

### UPDATE block

```json
"<table_name>_update": {
  "target_table": "<exact SQLite table name>",
  "operation": "UPDATE",
  "pk_column": "id",
  "columns": ["col_to_update_1", "col_to_update_2"],
  "row_counts": {
    "total_rows": 3
  },
  "rows": [
    {
      "id": 42,
      "col_to_update_1": "new value",
      "col_to_update_2": null,
      "_ref": {
        "human_note": "Optional — for verification only. Never imported."
      }
    }
  ]
}
```

`pk_column` identifies which column is used in the `WHERE` clause. Must match the table's actual primary key or a unique column.  
`columns` lists only the columns being updated — do not repeat the pk_column in `columns`.

---

## Row rules

- Every row must contain exactly the fields listed in `columns` (plus optionally `_ref`).
- `_ref` is a human-readable verification object only. It is never imported into the database.
- Null values must be written as JSON `null`, not as empty string `""`.
- Integer booleans use `0` / `1` (SQLite convention), not `true` / `false`.
- Dates use ISO-8601 format: `"2026-03-17"`.

---

## `row_counts` (optional but recommended)

Provide expected counts as a machine-verifiable declaration:

```json
"row_counts": {
  "total_rows": 200,
  "flag_id_1_rows": 85,
  "flag_id_2_rows": 41,
  "flag_id_3_rows": 74
}
```

The import script will validate `total_rows` against the actual row array length and report any mismatch before applying.

---

## What NOT to include

- No `sql_statements` array — SQL is generated from the structured data by the import script.
- No computed or derived columns (e.g. `last_changed`) — the DB schema handles defaults.
- No schema DDL — patches are data-only.
- No rows for tables outside the patch's declared scope.

---

## Complete minimal example

```json
{
  "_meta": {
    "patch_id": "REG-PATCH-20260317-003",
    "date": "2026-03-17",
    "description": "Add word registry entries #201-202.",
    "format": "bible-projects-patch-spec-v1.1",
    "id_baseline": { "word_registry": 200 }
  },
  "word_registry_insert": {
    "target_table": "word_registry",
    "operation": "INSERT",
    "conflict_action": "IGNORE",
    "columns": ["id", "no", "word", "source_list", "category_hint",
                "phase1_input_file", "phase1_status", "phase1_output_file",
                "phase2_datasets", "notes"],
    "row_counts": { "total_rows": 2 },
    "rows": [
      {
        "id": 201,
        "no": 201,
        "word": "example word",
        "source_list": "High Confidence",
        "category_hint": "Emotion/Example",
        "phase1_input_file": null,
        "phase1_status": "Pending",
        "phase1_output_file": null,
        "phase2_datasets": null,
        "notes": "Added 2026-03-17: reason for inclusion.",
        "_ref": { "added_by": "Claude session XYZ" }
      },
      {
        "id": 202,
        "no": 202,
        "word": "another word",
        "source_list": "Medium Confidence",
        "category_hint": "Moral/Virtue",
        "phase1_input_file": null,
        "phase1_status": "Pending",
        "phase1_output_file": null,
        "phase2_datasets": null,
        "notes": "Added 2026-03-17: reason for inclusion."
      }
    ]
  }
}
```

---

## Schema reference (column names per table)

See `data/schema/create_tables.sql` for the authoritative list of columns per table. When producing a patch, always confirm column names against this file — do not invent column names.

Key tables most likely to be patched:

| Table | Primary key | ID assignment | Common patch type |
|---|---|---|---|
| `word_registry` | `id` (INTEGER, explicit) | Always query `MAX(id)`, assign from `MAX+1` | INSERT, UPDATE |
| `phase2_flag_types` | `id` (INTEGER, explicit) | Always query `MAX(id)`, assign from `MAX+1` | INSERT |
| `wa_quality_flag_types` | `id` (AUTOINCREMENT) | Query `MAX(id)`, assign explicitly when cross-referenced | INSERT |
| `wa_data_quality_flags` | `id` (AUTOINCREMENT) | Omit `id`; resolved by apply script from `file_id`+`term_id`+`flag_id` | INSERT, DELETE |
| `wa_term_phase2_flags` | composite `(term_inv_id, flag_id)` | No id column — FKs must reference known IDs | INSERT |
| `wa_file_index` | `id` (AUTOINCREMENT) | Query `MAX(id)`, assign explicitly when subsequent blocks need this FK | INSERT |
| `wa_term_inventory` | `id` (AUTOINCREMENT) | Query `MAX(id)`, assign explicitly when subsequent blocks need this FK | INSERT, UPDATE |
| `wa_term_related_words` | `id` (AUTOINCREMENT) | Omit `id` unless cross-referenced | INSERT |
| `wa_term_root_family` | `id` (AUTOINCREMENT) | Omit `id` unless cross-referenced | INSERT |
| `wa_meaning_parsed` | `id` (AUTOINCREMENT) | Resolved by apply script via `term_inv_id` | UPDATE |
| `wa_meaning_stem` | `id` (AUTOINCREMENT) | Omit `id`; `parsed_meaning_id` resolved by apply script via `term_inv_id` | INSERT |
| `wa_lsj_parsed` | `id` (AUTOINCREMENT) | Omit `id`; `term_inv_id` is the natural key | INSERT, UPDATE |
| `mti_terms` | `id` (AUTOINCREMENT) | Query `MAX(id)`, assign explicitly when cross-referenced | INSERT |
| `mti_term_cross_refs` | `id` (AUTOINCREMENT) | Omit `id` unless cross-referenced | INSERT |
| `wa_cross_registry_links` | `id` (AUTOINCREMENT) | Query `MAX(id)`, assign explicitly when subsequent blocks need this FK | INSERT |

**Rule:** For AUTOINCREMENT tables, omit `id` from `columns` *only* when no other block in the same patch needs to reference that row's ID as a foreign key. Whenever cross-block FK references are needed, include `id` explicitly (query `MAX(id)` first) and record the baseline in `_meta.id_baseline`.

### Column reference for frequently patched tables

**`word_registry`** (updated 2026-03-20):
`id, no, word, source_list, category_hint, phase1_input_file, phase1_status, phase1_output_file, phase2_datasets, notes, automation_eligible, last_automation_run, automation_run_id, phase1_term_count, phase1_verse_count, strongs_list, description`

**`wa_term_related_words`** (updated 2026-03-17):
`id, term_inv_id, gloss, transliteration, strongs_number, relationship_note`

**`wa_term_root_family`** (updated 2026-03-17):
`id, term_inv_id, root_code, root_language, root_gloss, note`

**`wa_meaning_parsed`** (added 2026-03-20):
`id, term_inv_id, strongs_number, language, top_sense_count, stem_count, has_causative_stem, has_domain_tags, parsed_at, parse_version, parse_warnings`

**`wa_meaning_stem`** (added 2026-03-20):
`id, parsed_meaning_id, stem_name, stem_type, sense_count, top_sense_text`

**`wa_lsj_parsed`** (added 2026-03-20):
`id, term_inv_id, raw_lsj, lsj_gloss, lsj_domains, lsj_philosophical_note, lsj_etymology_note, lsj_cognate_forms, parsed_at, parse_version`

**`wa_quality_flag_types`** (added 2026-03-20):
`id, flag_group, flag_code, description`

**`wa_data_quality_flags`** (added 2026-03-20):
`id, file_id, term_id, flag_id, description, last_changed`
Note: `term_id` holds the Strong's/STEP code string (e.g. `"H8441"`), not an integer FK.

**`mti_terms`** (added 2026-03-20):
`id, strongs_number, transliteration, gloss, language, owning_registry, owning_word, owning_part, word_data_reference, status, status_note, exclusion_reason, extraction_date, strongs_reconciled, anchor_note, last_changed`

**`mti_term_cross_refs`** (added 2026-03-20):
`id, mti_term_id, registry, word, part, word_data_reference`

---

## Patch inventory

Patches applied to the production database (most recent first):

| File | Date | Type | Summary |
|------|------|------|---------|
| `registry-metadata-patch-20260320-v1.json` | 2026-03-20 | Format B / DDL+UPDATE | Added 4 columns to `word_registry` (`origin`, `source_category`, `inference_note`, `anchor_verses`); all 211 rows populated |
| `word-descriptions-patch-20260319-v1.json` | 2026-03-19 | Format B / UPDATE | `word_registry.description` populated for all 211 words |
| `phase2-flag-reassessment-20260319-v1.json` | 2026-03-19 | Format B / INSERT+DELETE | 2,361 TERM_ANALYSIS quality flags inserted; 141 stale flags deleted; 19 new flag types added |
| `stem-extraction-patch-20260319-v1.json` | 2026-03-19 | Format B / UPDATE+INSERT | 695 `wa_meaning_stem` rows inserted; 643+538 `wa_meaning_parsed` rows updated; 15 causative flag corrections |
