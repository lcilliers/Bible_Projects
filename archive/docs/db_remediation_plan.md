# Framework B — Database Remediation Plan
**Database:** `bible_research.db` | Schema 3.1.0  
**Prepared:** 2026-03-22  
**Basis:** db_relationship_report.md + live database validation  
**Delivery:** Standalone repair scripts in `scripts/_repair_*.py` — not wired into `migrate.py`

---

## Corrections to Prior Draft

Nine issues were identified in the first draft. Each is resolved below before any fix is described.

| # | Issue | Resolution applied |
|---|---|---|
| 1 | Fix numbering conflict — Phase 3 and 4 both claimed "Fix 6" | Renumbered cleanly throughout this document |
| 2 | All `INSERT INTO new SELECT * FROM old` silently misalign when column order changes | Every INSERT uses explicit named-column lists derived from live `PRAGMA table_info` |
| 3 | Phases 6/13 referenced `word_registry(no)` as FK target — `no` has no UNIQUE index, invalid FK | Confirmed: `id` is the PK, `no` is not unique-indexed. All FKs use `word_registry(id)`. `id` and `no` are identical in value for all 211 rows, so `word_registry_fk` values are correct as-is |
| 4 | `parsed_meaning_id` is actively written by `meaning_parser.py` — dropping it would break the engine | Column retained in all recreations. The bidirectional soft loop is documented but left structurally intact |
| 5 | Phase 5 LEFT JOIN could produce duplicate rows if a term appears multiple times | Confirmed: 2 duplicate `(file_id, term_id)` pairs exist in `wa_term_inventory`. The INSERT for `wa_data_quality_flags` uses a subquery with `MIN(wti.id)` to resolve deterministically |
| 6 | 53 orphan flags need researcher classification before a script can resolve them | Orphans are classified into 4 categories (see Section 9 and the audit CSV). Script exports audit CSV and halts; researcher applies decisions before re-run |
| 7 | Index recreation SQL not included | Every recreation script includes explicit `CREATE INDEX` statements matching the live database exactly |
| 8 | No backup step | Every script takes a timestamped `.db.bak` backup as its first action before any write |
| 9 | Delivery mechanism not specified | All scripts are standalone `scripts/_repair_*.py` files, not wired into `migrate.py` |

---

## Validated Facts From Live Database

These were confirmed by querying the live database before writing any fix.

- `word_registry.id` is the INTEGER PRIMARY KEY. `word_registry.no` has no UNIQUE index and must not be used as an FK target.
- `id` and `no` have identical values for all 211 rows (`SELECT COUNT(*) WHERE id != no` = 0), so `word_registry_fk` values in `wa_file_index` are already correct integers pointing to `word_registry.id`.
- `wa_term_inventory` has 2 duplicate `(file_id, term_id)` pairs: `(29, G0150)` and `(48, H7999A)`. Both are deliberate STRONGS_RECONCILED consolidations. The INSERT for `wa_data_quality_flags` must handle this.
- `wa_term_inventory.parsed_meaning_id` is an active write target. It is retained.
- The 53 orphan flags break into: 6 `NO STRONG-…` placeholders, 3 `_related` suffix variants, 0 wrong-file matches, 44 terms genuinely absent from `wa_term_inventory`.
- All existing index DDL has been captured from `sqlite_master` and is reproduced exactly in each script.

---

## Execution Order

Run scripts in this sequence. Each script is safe to re-run (it checks for prior completion).

| Step | Script | What it does | Data risk |
|---|---|---|---|
| T-00 | Backup | Timestamped file copy before any script runs | None |
| Fix 1 | `_repair_01_fk_pragma.py` | Enable FK enforcement in `db_client.py` and `engine/db.py` | Code only |
| Fix 2 | `_repair_02_zero_padding.py` | Normalise zero-padded registry IDs in 4 tables | Low — UPDATE only |
| Fix 3 | `_repair_03_wa_file_index.py` | Recreate `wa_file_index` with FK to `word_registry(id)` registered | Medium |
| Fix 4 | `_repair_04_wa_term_inventory.py` | Recreate `wa_term_inventory` with FK to `wa_file_index(id)` registered | Medium |
| Fix 5 | `_repair_05_wa_term_related_words.py` | Recreate with FK to `wa_term_inventory(id)` | Low |
| Fix 6 | `_repair_06_wa_term_root_family.py` | Recreate with FK to `wa_term_inventory(id)` | Low |
| Fix 7 | `_repair_07_wa_verse_records.py` | Recreate with FKs to `wa_file_index(id)` and `wa_term_inventory(id)` | High — 57,130 rows |
| Fix 8 (part 1) | `_repair_08a_dqf_audit.py` | Export orphan flag audit CSV — **no writes** | None |
| Fix 8 (part 2) | `_repair_08b_dqf_rebuild.py` | Recreate `wa_data_quality_flags` with integer `term_inv_id` FK | Medium — run after researcher reviews audit CSV |
| Fix 9 | `_repair_09_mti.py` | Recreate `mti_terms` and `mti_term_cross_refs` with integer FK columns | Medium |

---

## T-00: Backup

Every script performs this as its first action. Shown here for reference.

```python
import shutil, os
from datetime import datetime

def backup_db(db_path: str) -> str:
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    bak = f"{db_path}.bak_{ts}"
    shutil.copy2(db_path, bak)
    print(f"Backup written: {bak}")
    return bak
```

---

## Fix 1 — Enable FK Enforcement at Every Connection

**File:** `analytics/db_client.py` and `engine/db.py`  
**Change:** Add `PRAGMA foreign_keys = ON` immediately after `sqlite3.connect()` in every `get_connection()` function.

```python
conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON")   # ADD THIS LINE
```

This is a code change only. No data is modified. All 19 registered FKs will now be enforced at runtime. Apply this change, then run `PRAGMA foreign_key_check;` against the live database to confirm zero violations before proceeding.

**Verification:**
```sql
PRAGMA foreign_key_check;
-- Must return 0 rows before proceeding to Fix 2
```

---

## Fix 2 — Normalise Zero-Padded Registry IDs

**Script:** `scripts/_repair_02_zero_padding.py`  
**Tables affected:** `wa_file_index`, `mti_terms`, `mti_term_cross_refs`, `word_run_state`  
**Type:** UPDATE only — no structure change.

**Why:** Several tables store registry IDs as zero-padded 3-character strings (`'007'`, `'071'`) while `word_registry.id` is a plain INTEGER. String joins fail silently. `term_fetch_log` is NOT affected (0% orphan rate — it already stores clean values).

```sql
-- wa_file_index: 17 rows affected
UPDATE wa_file_index
SET registry_id = CAST(CAST(registry_id AS INTEGER) AS TEXT)
WHERE registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT);

-- mti_terms: 371 rows affected (16 distinct IDs)
UPDATE mti_terms
SET owning_registry = CAST(CAST(owning_registry AS INTEGER) AS TEXT)
WHERE owning_registry GLOB '[0-9]*'
  AND owning_registry != CAST(CAST(owning_registry AS INTEGER) AS TEXT);

-- mti_term_cross_refs: 28 rows affected (5 distinct IDs)
UPDATE mti_term_cross_refs
SET registry = CAST(CAST(registry AS INTEGER) AS TEXT)
WHERE registry GLOB '[0-9]*'
  AND registry != CAST(CAST(registry AS INTEGER) AS TEXT);

-- word_run_state: 82 rows affected
UPDATE word_run_state
SET registry_id = CAST(CAST(registry_id AS INTEGER) AS TEXT)
WHERE registry_id GLOB '[0-9]*'
  AND registry_id != CAST(CAST(registry_id AS INTEGER) AS TEXT);
```

**Verification after each UPDATE:**
```sql
-- Should return 0 for each table
SELECT COUNT(*) FROM wa_file_index
WHERE registry_id != CAST(word_registry_fk AS TEXT);

SELECT COUNT(*) FROM mti_terms
WHERE owning_registry GLOB '0[0-9]*';

SELECT COUNT(*) FROM mti_term_cross_refs
WHERE registry GLOB '0[0-9]*';

SELECT COUNT(*) FROM word_run_state
WHERE registry_id GLOB '0[0-9]*';
```

---

## Fix 3 — Recreate `wa_file_index` (Register FK to `word_registry`)

**Script:** `scripts/_repair_03_wa_file_index.py`

**Why:** `word_registry_fk` (INTEGER, clean, 0 orphans) has the FK defined in `create_tables.sql` but it was never registered in the live database. `registry_id` (TEXT) is a legacy duplicate column for the same relationship. After Fix 2, both columns are consistent. This recreation registers the FK on `word_registry_fk`.

`parsed_meaning_id` does not appear in this table — no issue 4 concern here.

**Existing indexes to recreate:**
```sql
CREATE INDEX idx_wa_fi_wrfk ON wa_file_index(word_registry_fk);
CREATE INDEX idx_wa_fi_word  ON wa_file_index(word);
CREATE INDEX idx_wa_fi_reg   ON wa_file_index(registry_id);
```

**Script logic:**
```sql
BEGIN TRANSACTION;

CREATE TABLE wa_file_index_new (
    id                           INTEGER PRIMARY KEY,
    filename                     TEXT NOT NULL,
    registry_id                  TEXT NOT NULL,
    word_registry_fk             INTEGER REFERENCES word_registry(id) ON DELETE RESTRICT,
    word                         TEXT NOT NULL,
    part_number                  INTEGER,
    total_parts                  INTEGER,
    is_split                     INTEGER,
    schema_version               TEXT,
    phase                        TEXT,
    produced_date                TEXT,
    source_file                  TEXT,
    translation_used             TEXT,
    specification                TEXT,
    revision_note                TEXT,
    source_list                  TEXT,
    category                     TEXT,
    testament_coverage           TEXT,
    root_families_in_prior_parts TEXT,
    last_changed                 TEXT DEFAULT (datetime('now'))
);

INSERT INTO wa_file_index_new (
    id, filename, registry_id, word_registry_fk, word,
    part_number, total_parts, is_split, schema_version, phase,
    produced_date, source_file, translation_used, specification,
    revision_note, source_list, category, testament_coverage,
    root_families_in_prior_parts, last_changed
)
SELECT
    id, filename, registry_id, word_registry_fk, word,
    part_number, total_parts, is_split, schema_version, phase,
    produced_date, source_file, translation_used, specification,
    revision_note, source_list, category, testament_coverage,
    root_families_in_prior_parts, last_changed
FROM wa_file_index;

DROP TABLE wa_file_index;
ALTER TABLE wa_file_index_new RENAME TO wa_file_index;

CREATE INDEX idx_wa_fi_wrfk ON wa_file_index(word_registry_fk);
CREATE INDEX idx_wa_fi_word  ON wa_file_index(word);
CREATE INDEX idx_wa_fi_reg   ON wa_file_index(registry_id);

COMMIT;
```

**Verification:**
```sql
SELECT COUNT(*) FROM wa_file_index;                    -- must equal 199
SELECT COUNT(*) FROM pragma_foreign_key_list('wa_file_index');  -- must be >= 1
```

---

## Fix 4 — Recreate `wa_term_inventory` (Register FK to `wa_file_index`)

**Script:** `scripts/_repair_04_wa_term_inventory.py`

**Why:** `file_id` FK is defined in `create_tables.sql` but not registered in the live database.

**Issue 4 note:** `parsed_meaning_id` (col 21) is retained exactly as-is. It is an active write target.

**Issue 5 note:** 2 duplicate `(file_id, term_id)` pairs exist — `(29, G0150)` and `(48, H7999A)`. These are legitimate STRONGS_RECONCILED rows with different `id` values. The INSERT is a direct row-for-row copy of the existing data; duplicates are preserved as they are in the source.

**Existing indexes to recreate:**
```sql
CREATE INDEX idx_wa_ti_file    ON wa_term_inventory(file_id);
CREATE INDEX idx_wa_ti_id      ON wa_term_inventory(term_id);
CREATE INDEX idx_wa_ti_lang    ON wa_term_inventory(language);
CREATE INDEX idx_wa_ti_strongs ON wa_term_inventory(strongs_number);
```

**Script logic:**
```sql
BEGIN TRANSACTION;

CREATE TABLE wa_term_inventory_new (
    id                          INTEGER PRIMARY KEY,
    file_id                     INTEGER NOT NULL REFERENCES wa_file_index(id) ON DELETE RESTRICT,
    language                    TEXT NOT NULL,
    term_id                     TEXT NOT NULL,
    strongs_number              TEXT,
    transliteration             TEXT NOT NULL,
    step_search_gloss           TEXT,
    word_analysis_gloss         TEXT,
    occurrence_count            INTEGER,
    occurrence_count_qualifier  TEXT,
    meaning                     TEXT,
    meaning_numbered            TEXT,
    also_spelled                TEXT,
    lsj_entry                   TEXT,
    testament                   TEXT,
    god_as_subject              INTEGER DEFAULT 0,
    somatic_link                INTEGER DEFAULT 0,
    causative_form_present      INTEGER DEFAULT 0,
    status_note                 TEXT,
    last_changed                TEXT DEFAULT (datetime('now')),
    short_def_mounce            TEXT,
    parsed_meaning_id           INTEGER    -- soft back-pointer to wa_meaning_parsed; retained as active write target
);

INSERT INTO wa_term_inventory_new (
    id, file_id, language, term_id, strongs_number, transliteration,
    step_search_gloss, word_analysis_gloss, occurrence_count,
    occurrence_count_qualifier, meaning, meaning_numbered, also_spelled,
    lsj_entry, testament, god_as_subject, somatic_link, causative_form_present,
    status_note, last_changed, short_def_mounce, parsed_meaning_id
)
SELECT
    id, file_id, language, term_id, strongs_number, transliteration,
    step_search_gloss, word_analysis_gloss, occurrence_count,
    occurrence_count_qualifier, meaning, meaning_numbered, also_spelled,
    lsj_entry, testament, god_as_subject, somatic_link, causative_form_present,
    status_note, last_changed, short_def_mounce, parsed_meaning_id
FROM wa_term_inventory;

DROP TABLE wa_term_inventory;
ALTER TABLE wa_term_inventory_new RENAME TO wa_term_inventory;

CREATE INDEX idx_wa_ti_file    ON wa_term_inventory(file_id);
CREATE INDEX idx_wa_ti_id      ON wa_term_inventory(term_id);
CREATE INDEX idx_wa_ti_lang    ON wa_term_inventory(language);
CREATE INDEX idx_wa_ti_strongs ON wa_term_inventory(strongs_number);

COMMIT;
```

**Verification:**
```sql
SELECT COUNT(*) FROM wa_term_inventory;   -- must equal 1529
```

---

## Fix 5 — Recreate `wa_term_related_words` (Register FK to `wa_term_inventory`)

**Script:** `scripts/_repair_05_wa_term_related_words.py`

**Existing index:**
```sql
CREATE INDEX idx_wa_rw ON wa_term_related_words(term_inv_id);
```

**Script logic:**
```sql
BEGIN TRANSACTION;

CREATE TABLE wa_term_related_words_new (
    id                  INTEGER PRIMARY KEY,
    term_inv_id         INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
    gloss               TEXT,
    transliteration     TEXT,
    strongs_number      TEXT,
    relationship_note   TEXT
);

INSERT INTO wa_term_related_words_new (
    id, term_inv_id, gloss, transliteration, strongs_number, relationship_note
)
SELECT
    id, term_inv_id, gloss, transliteration, strongs_number, relationship_note
FROM wa_term_related_words;

DROP TABLE wa_term_related_words;
ALTER TABLE wa_term_related_words_new RENAME TO wa_term_related_words;

CREATE INDEX idx_wa_rw ON wa_term_related_words(term_inv_id);

COMMIT;
```

**Verification:**
```sql
SELECT COUNT(*) FROM wa_term_related_words;   -- must equal 10102
```

---

## Fix 6 — Recreate `wa_term_root_family` (Register FK to `wa_term_inventory`)

**Script:** `scripts/_repair_06_wa_term_root_family.py`

**Existing index:**
```sql
CREATE INDEX idx_wa_rf ON wa_term_root_family(term_inv_id);
```

**Script logic:**
```sql
BEGIN TRANSACTION;

CREATE TABLE wa_term_root_family_new (
    id              INTEGER PRIMARY KEY,
    term_inv_id     INTEGER NOT NULL REFERENCES wa_term_inventory(id) ON DELETE CASCADE,
    root_code       TEXT NOT NULL,
    root_language   TEXT,
    root_gloss      TEXT,
    note            TEXT
);

INSERT INTO wa_term_root_family_new (
    id, term_inv_id, root_code, root_language, root_gloss, note
)
SELECT
    id, term_inv_id, root_code, root_language, root_gloss, note
FROM wa_term_root_family;

DROP TABLE wa_term_root_family;
ALTER TABLE wa_term_root_family_new RENAME TO wa_term_root_family;

CREATE INDEX idx_wa_rf ON wa_term_root_family(term_inv_id);

COMMIT;
```

**Verification:**
```sql
SELECT COUNT(*) FROM wa_term_root_family;   -- must equal 641
```

---

## Fix 7 — Recreate `wa_verse_records` (Register FKs to `wa_file_index` and `wa_term_inventory`)

**Script:** `scripts/_repair_07_wa_verse_records.py`

**Why this is the highest-risk fix:** 57,130 rows. Run inside a transaction. Verify row count before committing.

**Existing indexes to recreate (exact DDL from `sqlite_master`):**
```sql
CREATE INDEX idx_wavr_file_term_pos ON wa_verse_records (file_id, term_id, book_id, chapter, verse_num);
CREATE INDEX idx_wavr_term_id       ON wa_verse_records (term_id);
CREATE INDEX idx_wavr_reference     ON wa_verse_records (reference);
CREATE INDEX idx_wavr_book_ch_v     ON wa_verse_records (book_id, chapter, verse_num);
CREATE INDEX idx_wa_vr_term         ON wa_verse_records (term_inv_id);
```

**Script logic:**
```sql
BEGIN TRANSACTION;

CREATE TABLE wa_verse_records_new (
    id                  INTEGER PRIMARY KEY,
    file_id             INTEGER NOT NULL REFERENCES wa_file_index(id) ON DELETE RESTRICT,
    term_inv_id         INTEGER REFERENCES wa_term_inventory(id) ON DELETE RESTRICT,
    term_id             TEXT,
    transliteration     TEXT,
    testament           TEXT,
    reference           TEXT,
    verse_text          TEXT,
    last_changed        TEXT DEFAULT (datetime('now')),
    book_id             INTEGER REFERENCES books(id),
    chapter             INTEGER,
    verse_num           INTEGER,
    translation         TEXT NOT NULL DEFAULT 'ESV',
    note                TEXT,
    claude_output       TEXT,
    created_at          TEXT,
    updated_at          TEXT,
    target_word         TEXT,
    span_strong_match   INTEGER,
    context_before      TEXT,
    context_after       TEXT
);

INSERT INTO wa_verse_records_new (
    id, file_id, term_inv_id, term_id, transliteration, testament,
    reference, verse_text, last_changed, book_id, chapter, verse_num,
    translation, note, claude_output, created_at, updated_at,
    target_word, span_strong_match, context_before, context_after
)
SELECT
    id, file_id, term_inv_id, term_id, transliteration, testament,
    reference, verse_text, last_changed, book_id, chapter, verse_num,
    translation, note, claude_output, created_at, updated_at,
    target_word, span_strong_match, context_before, context_after
FROM wa_verse_records;

-- Verify count BEFORE committing
SELECT COUNT(*) FROM wa_verse_records_new;   -- must equal 57130 — check in script before commit

DROP TABLE wa_verse_records;
ALTER TABLE wa_verse_records_new RENAME TO wa_verse_records;

CREATE INDEX idx_wavr_file_term_pos ON wa_verse_records (file_id, term_id, book_id, chapter, verse_num);
CREATE INDEX idx_wavr_term_id       ON wa_verse_records (term_id);
CREATE INDEX idx_wavr_reference     ON wa_verse_records (reference);
CREATE INDEX idx_wavr_book_ch_v     ON wa_verse_records (book_id, chapter, verse_num);
CREATE INDEX idx_wa_vr_term         ON wa_verse_records (term_inv_id);

-- Recreate trigger: keeps updated_at current on every UPDATE
-- This trigger was on the original table and MUST be recreated after the table swap.
CREATE TRIGGER IF NOT EXISTS wa_verse_records_updated_at
AFTER UPDATE ON wa_verse_records
BEGIN
    UPDATE wa_verse_records
    SET updated_at = strftime('%Y-%m-%dT%H:%M:%S','now')
    WHERE id = NEW.id;
END;

COMMIT;
```

**The script must abort (ROLLBACK) if `COUNT(*) FROM wa_verse_records_new != 57130` before the DROP.**

---

## Fix 8a — Export Orphan Flag Audit CSV (No Writes)

**Script:** `scripts/_repair_08a_dqf_audit.py`  
**Output:** `scripts/orphan_flags_audit.csv`  
**Writes to database:** None. This script is read-only.

The 53 orphan flags fall into 4 categories, confirmed by live query:

| Category | Count | Description |
|---|---|---|
| `NO_STRONG` | 6 flags | `NO STRONG-043-…` and `NO STRONG-135-…` placeholders. These are terms that were in the source data but had no Strong's number. They represent real terms that were noted but could not be registered. |
| `RELATED_SUFFIX` | 3 flags | `G3949_related` — a non-standard suffix variant of `G3949`. The base term `G3949` is also absent from the inventory. |
| `NOT_IN_DB` | 44 flags | Terms listed in flags but entirely absent from `wa_term_inventory`. Includes terms from words `abomination`, `agony`, `anger`, `anguish`, `anointing`, `anxiety`, `desire`, `repentance`, `gladness`. These are terms that were noted in the extraction engine but not carried through to the inventory. |
| `WRONG_FILE` | 0 flags | None — no cases where the term exists in the inventory under a different file. |

**The audit CSV has these columns:**

```
dqf_id, file_id, word, registry_id, term_id, flag_code, flag_description,
analyst_note, category, researcher_decision, resolution_term_inv_id, resolution_notes
```

The `researcher_decision` column is blank for you to fill in. The valid decisions are:

- `KEEP_AS_FILE_LEVEL` — for `NO_STRONG` terms: the flag is valid but term-level scope is wrong. Set `term_id = NULL`, keep flag against the file. The term's name moves to `description`.
- `RESOLVE_TO_TERM` — for `RELATED_SUFFIX` and `NOT_IN_DB` where the flagged term genuinely belongs to a term that should be in the inventory. Provide the correct `term_id` in `resolution_term_inv_id`.
- `DELETE` — flag is no longer meaningful and should be removed.
- `KEEP_UNLINKED` — retain the flag with the TEXT `term_id` as a label, accept that `term_inv_id` will be NULL.

**Fix 8b will not run until this CSV is returned with researcher decisions.**

---

## Fix 8b — Recreate `wa_data_quality_flags` with Integer `term_inv_id` FK

**Script:** `scripts/_repair_08b_dqf_rebuild.py`  
**Prerequisite:** `orphan_flags_audit.csv` must be present with `researcher_decision` column populated.

**Why:** `wa_data_quality_flags.term_id` is TEXT (Strong's number string) with no FK to `wa_term_inventory`. 53 orphan flags cannot be joined to term records. Adding an integer `term_inv_id` FK column gives every flag a reliable, indexed link to its term row.

**Issue 5 fix:** The join to resolve `term_inv_id` uses `MIN(wti.id)` to handle the 2 duplicate `(file_id, term_id)` cases deterministically. For `(29, G0150)` and `(48, H7999A)` the lower id is selected. This is recorded in the script output for review.

**Existing indexes to recreate:**
```sql
CREATE INDEX idx_wdqf_file ON wa_data_quality_flags (file_id);
CREATE INDEX idx_wdqf_flag ON wa_data_quality_flags (flag_id);
```

**Script logic:**
```sql
BEGIN TRANSACTION;

CREATE TABLE wa_data_quality_flags_new (
    id              INTEGER PRIMARY KEY,
    file_id         INTEGER NOT NULL REFERENCES wa_file_index(id) ON DELETE RESTRICT,
    term_inv_id     INTEGER REFERENCES wa_term_inventory(id) ON DELETE RESTRICT,  -- new integer FK
    term_id         TEXT,       -- retained: Strong's code label and legacy compatibility
    flag_id         INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
    description     TEXT,
    last_changed    TEXT DEFAULT (datetime('now'))
);

-- Populate term_inv_id using MIN(id) to resolve the 2 known duplicates deterministically
INSERT INTO wa_data_quality_flags_new (
    id, file_id, term_inv_id, term_id, flag_id, description, last_changed
)
SELECT
    dqf.id,
    dqf.file_id,
    (
        SELECT MIN(wti.id)
        FROM wa_term_inventory wti
        WHERE wti.term_id  = dqf.term_id
          AND wti.file_id  = dqf.file_id
    ),         -- NULL where no match (53 orphans); researcher decisions applied in next step
    dqf.term_id,
    dqf.flag_id,
    dqf.description,
    dqf.last_changed
FROM wa_data_quality_flags dqf;

-- Apply researcher decisions from audit CSV
-- (script reads orphan_flags_audit.csv and applies each decision here)

DROP TABLE wa_data_quality_flags;
ALTER TABLE wa_data_quality_flags_new RENAME TO wa_data_quality_flags;

CREATE INDEX idx_wdqf_file ON wa_data_quality_flags (file_id);
CREATE INDEX idx_wdqf_flag ON wa_data_quality_flags (flag_id);
-- Add index on the new integer column
CREATE INDEX idx_wdqf_term_inv ON wa_data_quality_flags (term_inv_id);

COMMIT;
```

**Verification:**
```sql
SELECT COUNT(*) FROM wa_data_quality_flags;                            -- must equal 3254
SELECT COUNT(*) FROM wa_data_quality_flags WHERE term_id IS NOT NULL AND term_inv_id IS NULL;
-- Returns the count of flags still unlinked after researcher decisions are applied
-- Target: 0 for NO_STRONG and RELATED_SUFFIX; acceptable residual for genuine NOT_IN_DB
```

---

## Fix 9 — Recreate `mti_terms` and `mti_term_cross_refs` (Register Integer FK Columns)

**Script:** `scripts/_repair_09_mti.py`

**Why:** `mti_terms.owning_registry` (TEXT, now clean after Fix 2) and `mti_term_cross_refs.registry` (TEXT) are the only routes from the MTI back to `word_registry`. `mti_terms.word_data_reference` (TEXT, labelled "future FK" in schema, 0 orphans) links to `wa_file_index.id` but is a TEXT column. Adding integer FK columns gives the MTI proper relational anchoring without breaking any existing TEXT-based queries.

**Existing indexes to recreate (exact DDL from `sqlite_master`):**
```sql
-- mti_terms
CREATE INDEX idx_mti_terms_registry ON mti_terms(owning_registry);
CREATE INDEX idx_mti_terms_status   ON mti_terms(status);
CREATE INDEX idx_mti_terms_word     ON mti_terms(owning_word);
CREATE INDEX idx_mti_terms_strongs  ON mti_terms(strongs_number);

-- mti_term_cross_refs
CREATE INDEX idx_cross_refs_registry ON mti_term_cross_refs(registry, word);
CREATE INDEX idx_cross_refs_term_id  ON mti_term_cross_refs(mti_term_id);
-- Note: sqlite_autoindex_mti_term_cross_refs_1 is system-generated from UNIQUE constraint
-- and will be recreated automatically when the UNIQUE constraint is declared
```

**Script logic — `mti_terms`:**
```sql
BEGIN TRANSACTION;

CREATE TABLE mti_terms_new (
    id                  INTEGER PRIMARY KEY,
    strongs_number      TEXT,
    transliteration     TEXT NOT NULL,
    gloss               TEXT NOT NULL,
    language            TEXT,
    owning_registry     TEXT,           -- retained: TEXT label, now clean after Fix 2
    owning_registry_fk  INTEGER REFERENCES word_registry(id) ON DELETE RESTRICT,  -- new integer FK
    owning_word         TEXT,
    owning_part         TEXT,
    word_data_reference TEXT,           -- retained as TEXT for legacy reads
    word_data_ref_fk    INTEGER REFERENCES wa_file_index(id),  -- new integer FK
    status              TEXT,
    status_note         TEXT,
    exclusion_reason    TEXT,
    extraction_date     TEXT,
    strongs_reconciled  INTEGER DEFAULT 0,
    anchor_note         TEXT,
    last_changed        TEXT DEFAULT (datetime('now'))
);

INSERT INTO mti_terms_new (
    id, strongs_number, transliteration, gloss, language,
    owning_registry, owning_registry_fk,
    owning_word, owning_part,
    word_data_reference, word_data_ref_fk,
    status, status_note, exclusion_reason, extraction_date,
    strongs_reconciled, anchor_note, last_changed
)
SELECT
    id, strongs_number, transliteration, gloss, language,
    owning_registry,
    CAST(owning_registry AS INTEGER),      -- populate integer FK from clean TEXT column
    owning_word, owning_part,
    word_data_reference,
    CAST(word_data_reference AS INTEGER),  -- populate integer FK from TEXT (0 orphans confirmed)
    status, status_note, exclusion_reason, extraction_date,
    strongs_reconciled, anchor_note, last_changed
FROM mti_terms;

DROP TABLE mti_terms;
ALTER TABLE mti_terms_new RENAME TO mti_terms;

CREATE INDEX idx_mti_terms_registry ON mti_terms(owning_registry);
CREATE INDEX idx_mti_terms_status   ON mti_terms(status);
CREATE INDEX idx_mti_terms_word     ON mti_terms(owning_word);
CREATE INDEX idx_mti_terms_strongs  ON mti_terms(strongs_number);
CREATE INDEX idx_mti_terms_reg_fk   ON mti_terms(owning_registry_fk);

COMMIT;
```

**Script logic — `mti_term_cross_refs`:**
```sql
BEGIN TRANSACTION;

CREATE TABLE mti_term_cross_refs_new (
    id              INTEGER PRIMARY KEY,
    mti_term_id     INTEGER NOT NULL REFERENCES mti_terms(id) ON DELETE CASCADE,
    registry        TEXT NOT NULL,          -- retained: TEXT label
    registry_fk     INTEGER REFERENCES word_registry(id),  -- new integer FK
    word            TEXT,
    part            TEXT,
    word_data_reference TEXT,
    UNIQUE (mti_term_id, registry, word, part)  -- recreates the system autoindex
);

INSERT INTO mti_term_cross_refs_new (
    id, mti_term_id, registry, registry_fk, word, part, word_data_reference
)
SELECT
    id, mti_term_id, registry,
    CAST(registry AS INTEGER),   -- populate integer FK from clean TEXT column
    word, part, word_data_reference
FROM mti_term_cross_refs;

DROP TABLE mti_term_cross_refs;
ALTER TABLE mti_term_cross_refs_new RENAME TO mti_term_cross_refs;

CREATE INDEX idx_cross_refs_registry ON mti_term_cross_refs(registry, word);
CREATE INDEX idx_cross_refs_term_id  ON mti_term_cross_refs(mti_term_id);

COMMIT;
```

**Verification:**
```sql
SELECT COUNT(*) FROM mti_terms;            -- must equal 1380
SELECT COUNT(*) FROM mti_term_cross_refs;  -- must equal 463
SELECT COUNT(*) FROM mti_terms WHERE owning_registry_fk IS NULL AND owning_registry IS NOT NULL;
-- Should be 0 after Fix 2 normalised the TEXT column
```

---

## What Is Not Fixed

| Item | Reason |
|---|---|
| `wa_meaning_sense.parent_level_code` (G5) | Self-referencing TEXT hierarchy. Converting to integer self-FK requires assigning stable IDs to level codes. The sense tree is always fetched in full by `parsed_meaning_id` and navigated in application code. Analytical cost of fixing is zero; engineering cost is high. Leave it. |
| `themes` and `sources` (empty tables) | No data, no downstream joins. Structure them when there is a requirement. |
| `mti_term_flags` (9 rows) | Structurally sound — proper FKs to `mti_terms` and `phase2_flag_types`. Sparseness is a population issue, not a schema issue. |
| `engine_stream_checkpoint` sparseness | Operational pipeline table. Sparseness reflects that most runs complete without checkpointing. Not a research data concern. |
| `word_registry.parsed_meaning_id` soft loop (G7) | Retained because `parsed_meaning_id` is an active write target. Document the authoritative direction (`wa_meaning_parsed.term_inv_id`) in schema comments. |

---

## Post-Remediation Integrity Checks

Run these after all scripts complete:

```sql
PRAGMA foreign_key_check;
-- Must return 0 rows

-- Row counts must match pre-repair values
SELECT 'wa_file_index',       COUNT(*) FROM wa_file_index       UNION ALL
SELECT 'wa_term_inventory',   COUNT(*) FROM wa_term_inventory   UNION ALL
SELECT 'wa_term_related_words', COUNT(*) FROM wa_term_related_words UNION ALL
SELECT 'wa_term_root_family', COUNT(*) FROM wa_term_root_family UNION ALL
SELECT 'wa_verse_records',    COUNT(*) FROM wa_verse_records    UNION ALL
SELECT 'wa_data_quality_flags', COUNT(*) FROM wa_data_quality_flags UNION ALL
SELECT 'mti_terms',           COUNT(*) FROM mti_terms           UNION ALL
SELECT 'mti_term_cross_refs', COUNT(*) FROM mti_term_cross_refs;
-- Expected: 199, 1529, 10102, 641, 57130, 3254, 1380, 463

-- Confirm no new orphans introduced
SELECT COUNT(*) FROM wa_term_inventory wti
LEFT JOIN wa_file_index wfi ON wti.file_id = wfi.id
WHERE wfi.id IS NULL;   -- must be 0

SELECT COUNT(*) FROM wa_verse_records wvr
LEFT JOIN wa_term_inventory wti ON wvr.term_inv_id = wti.id
WHERE wvr.term_inv_id IS NOT NULL AND wti.id IS NULL;  -- must be 0
```
