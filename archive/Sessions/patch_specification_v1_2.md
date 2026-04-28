# Patch Specification — Session B/C/D JSON Patches

**Version:** 1.2 | **Date:** 2026-03-29
**Applicator:** `scripts/apply_session_patch.py`
**Supersedes:** patch_specification v1.1 (2026-03-26)

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

The `word_registry.session_b_status` column tracks each word's progress through the analysis pipeline. A parallel field `word_registry.verse_context_status` (NULL / In Progress / Complete) tracks the Verse Context stage independently. `Ready for Analysis` is only reachable when `verse_context_status = Complete`.

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
  ▼  (Session B synthesis document produced, all PH2 flags raised)
"Session B Complete"
```

**Who sets each status:**

| Status | Set by | Trigger |
|--------|--------|---------|
| `NULL` | Default | Word registered but not yet extracted |
| `Verse Context Reset` | Setup operation or patch | Prior Session B work superseded — must reprocess |
| `Ready for Analysis` | Claude Code completion check | verse_context_status = Complete confirmed |
| `Pre-Analysis Complete` | `apply_session_patch.py` | Pre-analysis patch with `session_b_status: "Pre-Analysis Complete"` |
| `Analysis Complete` | `apply_session_patch.py` | Session B analysis patch with `session_b_status: "Analysis Complete"` |
| `Session B Complete` | `apply_session_patch.py` | Final Session B patch with `session_b_status: "Session B Complete"` |

**Rules:**
- `audit_word` uses `COALESCE` — sets `Ready for Analysis` only if current status is NULL. Never downgrades.
- `apply_session_patch.py` overwrites `session_b_status` from `_patch_meta.session_b_status` for standard patches.
- PREANALYSIS, SESSIONB, SESSIOND, CLUSTERING, and REPAIR patches MUST include `session_b_status` in `_patch_meta`. Patches without it are rejected.
- **EXCEPTION: VERSECONTEXT, VCGROUP, and VCVERSE patches carry `session_b_status: null`. The applicator MUST NOT reject these.** They do not update `session_b_status` on `word_registry`.
- The status value should reflect what the patch accomplishes, not what comes next.

**Typical patch sequence for a word:**

| Patch | `session_b_status` value | What it does |
|-------|--------------------------|-------------|
| `PATCH-YYYYMMDD-VCB001-VERSECONTEXT-V1` | `null` | Verse context classification — relevance filter, grouping, anchor designation |
| `PATCH-YYYYMMDD-NNN-PREANALYSIS-V1` | `Pre-Analysis Complete` | Term classifications (extracted/delete/xref), bleed removal |
| `PATCH-YYYYMMDD-NNN-SESSIONB-V1` | `Analysis Complete` | MTI reconciliation, PH2 research flags, registry notes update |

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

### 3.10 `bulk_update` on `mti_terms` — Bulk status updates (Session B format)

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

These operations apply exclusively to `verse_context_group` and `verse_context` tables. They are governed by WA-VerseContext-Instruction-v1. Key rules:

- All three Verse Context patch types carry `session_b_status: null` — applicator must not reject
- All corrections are UPDATE operations — no physical deletes
- `verse_context_group` inserts must precede `verse_context` inserts in the same patch
- group_code strings (e.g. `"142-001"`) in verse_context inserts are resolved to integer ids by Claude Code at apply time using `last_insert_rowid()` after each group insert

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
