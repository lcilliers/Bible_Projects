# Reference-as-Database Framework Execution — 2026-04-20

| Field | Value |
|---|---|
| Filename | reference-as-database-framework-execution-20260420.md |
| Design | `reference-as-database-design-20260420.md` §10 (3-layer architecture, v1.1) |
| Researcher direction | 2026-04-20 evening: "create the framework and let's start migrating. With each set of references migrated to the database, you need to review the documents in workflow/session B to reset any referencing to the use of the reference, to the json file." |
| Status | IN EXECUTION — M32 cycle starting |
| Produced | 2026-04-20 |

---

## 1. Execution pattern (the framework)

For each migration phase (M32, M33, M34, M35), CC runs this 5-step cycle:

| Step | Action | Artefact |
|---|---|---|
| 1 | Schema + seed migration — new table(s) + initial data | `engine/migrate.py` `_mNN()` + dry-run log |
| 2 | Dry-run on DB copy | Dry-run log |
| 3 | Live apply with per-migration backup | `backups/bible_research_pre_mNN_{ts}.db` |
| 4 | Extractor update + validator rewire | `scripts/build_reference_snapshot.py` + relevant validator sites in `apply_session_patch.py` |
| 5 | **Document sweep** — review `data/imports/WA/Workflow/Framework_B/Session_B/*.md` for references to the migrated content; replace direct citations with "see reference snapshot JSON / DB query" | Updated instruction docs + sweep report |

Only after step 5 completes cleanly does CC proceed to the next migration.

## 2. Migration schedule

Per design §10.4, sequenced for lowest risk first:

| Phase | Scope | Status |
|---|---|---|
| **M32** | L1 taxonomic POC — `wa_vocab_set` + `wa_vocab_member`, seed 11 dimensions + 4–5 other vocabularies (dominant_subject, dimension_confidence, QA flags, manual_override, evidential_status) | IN PROGRESS |
| **M33** | L1 global rules — `wa_rule_registry`, seed from current `wa-global-general-rules-v2_11-20260418.json` | PENDING approval after M32 cycle |
| **M34** | L2 programme prose — extend prose_section_type with `source_stage='programme'` + 6–10 section types (anchor verse, XREF architecture, validation standard, etc.) | PENDING |
| **M35** | L1 remaining — `wa_patch_type_registry`, `wa_file_name_pattern`, `wa_label_pattern` | PENDING |
| **Post-M35** | Populate L2 programme prose (PROSE patches) + deprecate `wa-reference` document | PENDING |

## 3. Schema design (all phases — decided upfront)

Establishing all schemas upfront even if migrations execute in sequence. Prevents rework.

### 3.1 M32 — `wa_vocab_set` + `wa_vocab_member`

```sql
CREATE TABLE wa_vocab_set (
    id              INTEGER PRIMARY KEY,
    set_code        TEXT    NOT NULL UNIQUE,    -- e.g. 'DIMENSION_LABEL'
    name            TEXT    NOT NULL,            -- human-readable
    description     TEXT,
    governing_doc   TEXT,                        -- e.g. 'wa-dimensionreview-instruction [current] §7.7'
    applies_to      TEXT,                        -- e.g. 'wa_dimension_index.dimension'
    deprecated      INTEGER NOT NULL DEFAULT 0,
    deprecation_note TEXT,
    created_at      TEXT    NOT NULL,
    last_modified   TEXT
);

CREATE TABLE wa_vocab_member (
    id              INTEGER PRIMARY KEY,
    set_id          INTEGER NOT NULL REFERENCES wa_vocab_set(id),
    value           TEXT    NOT NULL,            -- canonical string stored in data tables
    label           TEXT,                        -- display label (may differ from value)
    description     TEXT,
    sort_order      INTEGER NOT NULL DEFAULT 0,
    deprecated      INTEGER NOT NULL DEFAULT 0,
    deprecation_note TEXT,
    superseded_by_member_id INTEGER REFERENCES wa_vocab_member(id),
    introduced_at   TEXT,
    created_at      TEXT    NOT NULL,
    last_modified   TEXT,
    UNIQUE (set_id, value)
);

CREATE INDEX idx_vocab_member_set ON wa_vocab_member(set_id) WHERE deprecated = 0;
CREATE INDEX idx_vocab_set_applies ON wa_vocab_set(applies_to) WHERE deprecated = 0;
```

### 3.2 M33 — `wa_rule_registry`

```sql
CREATE TABLE wa_rule_registry (
    id              INTEGER PRIMARY KEY,
    rule_id         TEXT    NOT NULL UNIQUE,    -- e.g. 'GR-LOAD-001'
    category        TEXT    NOT NULL,            -- e.g. 'LOAD', 'REF', 'FILE'
    statement       TEXT    NOT NULL,
    rationale       TEXT,
    scope           TEXT,
    version         TEXT    NOT NULL,
    introduced_at   TEXT,
    deprecated      INTEGER NOT NULL DEFAULT 0,
    deprecation_note TEXT,
    superseded_by   TEXT,
    addendum_ref    TEXT,
    created_at      TEXT    NOT NULL,
    last_modified   TEXT
);

CREATE INDEX idx_rule_category ON wa_rule_registry(category) WHERE deprecated = 0;
```

### 3.3 M34 — prose store programme stage

No new table. Extend `prose_section_type` with rows where `source_stage = 'programme'`. Seed 6–10 section types (see design §10.2).

### 3.4 M35 — `wa_patch_type_registry` + `wa_file_name_pattern` + `wa_label_pattern`

Schemas detailed in design §10. Summary:

- `wa_patch_type_registry` (type_code, description, session_b_status_exempt, governing_instruction, schema_affected, deprecated, ...)
- `wa_file_name_pattern` (pattern_code, pattern, scope, description, governing_instruction, deprecated, ...)
- `wa_label_pattern` (pattern_code, pattern, entity, description, governing_instruction, deprecated, ...)

## 4. Reference snapshot — structure

`scripts/build_reference_snapshot.py` produces a single JSON:

```
data/exports/reference/wa-reference-snapshot-{YYYYMMDD}.json
```

Structure (grows per migration phase):

```json
{
  "meta": {
    "generated_at": "...",
    "schema_version": "3.12.0",
    "db_path": "...",
    "extraction_version": "1.0"
  },
  "vocabularies": {
    "DIMENSION_LABEL": {
      "set_code": "DIMENSION_LABEL",
      "governing_doc": "wa-dimensionreview-instruction [current] §7.7",
      "applies_to": "wa_dimension_index.dimension",
      "members": [
        { "value": "01 — Emotion — Positive", "description": "Inner states of pleasure, ..." },
        ...
      ]
    },
    "DOMINANT_SUBJECT": { ... },
    ...
  },
  "rules": {          // populated post-M33
    "GR-LOAD-001": {...},
    ...
  },
  "patch_types": { ... },   // populated post-M35
  "file_name_patterns": { ... },   // populated post-M35
  "label_patterns": { ... },   // populated post-M35
  "schema": {
    "tables": [ "word_registry", "mti_terms", ... ],
    "per_table_columns": {
       "word_registry": ["id", "no", ...]
    }
  },
  "programme_prose_index": { ... }    // populated post-M34 (list of programme-stage sections)
}
```

## 5. Validator rewire pattern

Replace hardcoded frozenset in `apply_session_patch.py`:

```python
# Before:
CANONICAL_DIMENSIONS = frozenset({"01 — Emotion — Positive", ...})

# After:
def _load_vocab_set(conn, set_code: str) -> frozenset[str]:
    """Load a controlled vocabulary from DB. Cached per-patch-apply."""
    rows = conn.execute("""
        SELECT m.value FROM wa_vocab_member m
        JOIN wa_vocab_set s ON s.id = m.set_id
        WHERE s.set_code = ? AND m.deprecated = 0 AND s.deprecated = 0
    """, (set_code,)).fetchall()
    return frozenset(r[0] for r in rows)
```

Validator site updates at each vocabulary check. Fallback behaviour: if DB query returns empty (table doesn't exist, migration not run), log `[NOTE]` and fall back to hardcoded frozenset for safety during transition.

## 6. Document-sweep protocol (step 5 of each cycle)

Target directory: `data/imports/WA/Workflow/Framework_B/Session_B/`

For each document, CC searches for references to the migrated content and updates per these rules:

| Current pattern | Replacement pattern |
|---|---|
| Inline vocabulary list (e.g. "valid values: GOD / HUMAN / OTHER_HUMAN / UNSEEN / NONE") | "See reference snapshot `DOMINANT_SUBJECT` vocabulary (`wa-reference-snapshot-{date}.json`)" |
| "per wa-reference §X" citing migrated content | "per reference snapshot `<set_code>`" |
| Hardcoded rule ID citations | Unchanged (rules move to DB in M33; pointers to rule_id stay the same) |
| Inline patch type descriptions | Reference snapshot `patch_types` block (post-M35) |

**Post-sweep artefact:** each cycle produces `outputs/reports/ref-migration-mNN-doc-sweep-{date}.md` listing files touched, lines changed, references migrated.

## 7. Execution record

Updated as each step completes.

### M32 cycle — CLOSED 2026-04-20

| Step | Status | Outcome |
|---|---|---|
| 1 Migration code | ✅ | `engine/migrate.py::_m32` — creates `wa_vocab_set` + `wa_vocab_member` + 2 indexes; seeds 5 vocabs (27 members); bumps schema → 3.12.0 |
| 2 Dry-run | ✅ | `backups/dryrun/bible_research_dryrun_M32_20260420.db` — clean (5 sets, 27 members) |
| 3 Live apply | ✅ | `backups/bible_research_pre_M32_{ts}.db` pre-backup; live DB now at 3.12.0 |
| 4 Extractor + validator rewire | ✅ | `scripts/build_reference_snapshot.py` — JSON + MD view. `apply_session_patch.py` `_canonical_dimensions()` + `_load_vocab_set()` functions; 2 validator sites rewired (dimension + dominant_subject) |
| 5 Doc sweep | ✅ | `outputs/reports/ref-migration-m32-doc-sweep-20260420.md` — wa-reference §4.3 and DimReview §7.7 pointers updated to DB canonical. Other 5 docs: narrative USE left intact (sweep protocol). |

**M32 cycle closed 2026-04-20 evening.** Awaiting researcher approval to proceed with M33 (global rules → DB).

---

*v1.1 — 2026-04-20 evening. M32 complete; framework pattern proven.*
