# AUDIT_WORD Process — Full Design Document

**Date:** 2026-03-23  
**Status:** DRAFT — awaiting researcher review  
**Supersedes:** `audit_word_refactor_review.md` (researcher feedback incorporated)  
**Input source:** `docs/audit_word_refactor_review.md` (all RESPONSE blocks), `docs/word_study_extract_design.md`, full schema `Workflow/schema/create_tables.sql`

---

## 1. Purpose and Scope

`AUDIT_WORD` mode aligns the database with data produced by the Step 1 extract script (`word_study_extract.py`) and, where discrepancies are found, applies researcher-approved corrections across all affected tables. It does **not** re-fetch data from the STEP API — the Step 1 JSON file is the authoritative data input.

### What AUDIT_WORD covers

- Full database read (Word Extract Report) across all 16 content tables
- Three STEP data streams compared against the DB: **Term stream**, **Verse stream**, **Meaning stream**
- Cross-registry and quality flag streams
- DELETE-FLAG mechanism (no actual deletion; deletion is a separate archive run)
- `wa_verse_term_links` population (INSERT missing rows, UPDATE stale rows)
- Meaning parser refresh including legacy field migration (~33 records)
- Flag engine refresh (`wa_data_quality_flags`, `wa_term_phase2_flags`)
- Audit checks WR-01–WR-20
- Full logging: `engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log`

### What AUDIT_WORD does NOT do

- Re-fetch from the STEP API (Step 1 JSON is already the STEP output)
- Perform actual DELETE on any table (all removals are flagged; archive run is a separate mode)
- Modify researcher-owned fields without explicit approval
- Run on words not yet in `wa_file_index` (those go through NEW_WORD mode)

---

## 2. Input and Prerequisites

### 2.1 Step 1 JSON file

The primary data input is the JSON file produced by `scripts/word_study_extract.py`:

```
research/discovery/{registry_no:03d}_{word}_step_data_{YYYYMMDD}.json
```

Examples:
- `research/discovery/182_soul_step_data_20260323.json`
- `research/discovery/004_anger_step_data_20260323.json`

If multiple files exist for the word (different dates), the audit step will present a selection menu. The researcher chooses which file to audit against.

### 2.2 Step 1 JSON structure (used by the audit)

The audit reads the following from the JSON:

**`meta` block:**

| Field | Used for |
|-------|----------|
| `english_anchor` | Word identity check vs `word_registry.word` |
| `generated` | Displayed in audit header; logged in `engine_run_log` |
| `anchor_codes` | Reference when resolving DB_ONLY_TERM codes |
| `include_codes` | The full set of term codes to audit against |
| `exclude_codes` | Listed in DB_ONLY_TERM comparison for context |
| `summary_by_group` | Displayed in audit header |
| `total_terms_evaluated` | Displayed in audit header |

**Per-term record (include_codes only — terms with `action: "include"`):**

| Field | Used for |
|-------|----------|
| `code` | Matches `wa_term_inventory.strongs_number` |
| `gloss` | STEP-owned → `step_search_gloss`, `word_analysis_gloss` |
| `transliteration` | STEP-owned → `wa_term_inventory.transliteration` |
| `language` | Structural → `wa_term_inventory.language` |
| `vocab_count` | STEP-owned → `wa_term_inventory.occurrence_count` |
| `medium_def` | STEP-owned → `wa_term_inventory.meaning`, `meaning_numbered`; also input to meaning parser |
| `lsj_entry` | STEP-owned → `wa_term_inventory.lsj_entry`; also input to LSJ parser |
| `short_def_mounce` | STEP-owned → `wa_term_inventory.short_def_mounce` |
| `related_words` | → `wa_term_related_words` (list of `{strong, form, gloss, translit}`) |
| `meaning_numbered` | → `wa_term_inventory.meaning_numbered` (boolean) |
| `causative_form_present` | → `wa_term_inventory.causative_form_present` (boolean) |
| `data_quality_flags` | Compared against existing `wa_data_quality_flags` |
| `decision_group` | Informational; G1/G2/G2r terms have full verse data |
| `verses` | Array of verse records for verse stream comparison |

**Per-verse record (in `verses` array):**

| Field | Used for |
|-------|----------|
| `ref` | Match key: `wa_verse_records.reference` |
| `book_code` | FK resolution: `book_code_variants` → `books.id` |
| `chapter` | → `wa_verse_records.chapter` |
| `verse_num` | → `wa_verse_records.verse_num` |
| `esv_text` | → `wa_verse_records.verse_text` |
| `target_word` | → `wa_verse_records.target_word`, `wa_verse_term_links.target_word` |
| `testament` | → `wa_verse_records.testament` |
| `span_strong_match` | → `wa_verse_records.span_strong_match`, `wa_verse_term_links.span_strong_match` |
| `span_code_found` | → `wa_verse_term_links.step_subgloss_code` |
| `span_label_found` | → `wa_verse_term_links.step_subgloss_label` |
| `context_before` | → `wa_verse_records.context_before` |
| `context_after` | → `wa_verse_records.context_after` |
| `fetched_under_code` | Used to match verse to its canonical term code (important for sub-gloss verses) |

### 2.3 Researcher-owned fields (never overwritten by audit)

These fields exist in affected tables but are **never compared, never updated** by the audit. Only the researcher modifies them:

**`wa_term_inventory`:** `status_note`, `also_spelled`, `occurrence_count_qualifier`, `parsed_meaning_id` (set by meaning parser in A7, not audit)  
**`wa_term_root_family`:** all fields (root code assignments are researcher decisions)  
**`wa_verse_records`:** `note`, `claude_output`, `translation`  
**`wa_cross_registry_links`:** all fields (researcher-curated)

---

## 3. Architecture — STEP Data Streams

The researcher specified: *"I need to start with STEP search…collect all the parsed data from STEP together, and then compare it against the tables with full INSERT / UPDATE / SET DELETE FLAG."*

The Step 1 JSON already is that STEP collection. The audit process has three primary data streams, each affecting specific tables:

### Stream 1 — Term stream

**Source:** `terms[]` records in the JSON (include_codes only)  
**Tables affected:**

| Table | Action |
|-------|--------|
| `wa_term_inventory` | UPDATE (STEP-owned fields); INSERT (NEW_TERM if approved) |
| `wa_term_related_words` | DELETE old + INSERT from JSON (any approved term update); INSERT for NEW_TERM |
| `mti_terms` | INSERT for NEW_TERM if approved |

### Stream 2 — Verse stream

**Source:** `verses[]` arrays within each include_code term  
**Tables affected:**

| Table | Action |
|-------|--------|
| `wa_verse_records` | INSERT (new refs); UPDATE (STEP fields); SET `delete_flagged=1` (orphan refs) |
| `wa_verse_term_links` | INSERT (missing junction rows); UPDATE (stale span columns) |

### Stream 3 — Meaning stream

**Source:** `medium_def`, `lsj_entry`, `short_def_mounce` fields per term  
**Tables affected:**

| Table | Action |
|-------|--------|
| `wa_meaning_parsed` | INSERT/UPSERT per term |
| `wa_meaning_sense` | INSERT/UPSERT per parsed term |
| `wa_meaning_stem` | INSERT/UPSERT per parsed term |
| `wa_lsj_parsed` | INSERT/UPSERT for Greek terms |
| `wa_term_inventory` | UPDATE `parsed_meaning_id`; NULL legacy `meaning`/`meaning_numbered` fields for ~33 migrated records |

---

## 4. Delete-Flag Mechanism

### 4.1 Principle

The researcher specified: *"handling deletions…use flagging for deletion, but using actual deletion as a separate archive run. This may mean that we need a new field on each table that can be used to flag a delete state."*

No row is ever physically deleted by `AUDIT_WORD`. Records identified as candidates for removal are marked with `delete_flagged = 1`. An independent `ARCHIVE` mode (not part of this design) performs the physical deletion after researcher inspection.

### 4.2 New column required — schema migration

The following tables require a new column `delete_flagged INTEGER DEFAULT 0`:

| Table | Reason records can be flagged |
|-------|-------------------------------|
| `wa_term_inventory` | Term was in DB from a prior run but its code is NOT in current Step 1 `include_codes` (DB_ONLY_TERM) |
| `wa_verse_records` | Verse ref was in DB for this term but STEP no longer returns it (orphan verse) |
| `wa_term_related_words` | Related word was in DB but is no longer in STEP related_words (orphan related word) |

Migration SQL:
```sql
ALTER TABLE wa_term_inventory ADD COLUMN delete_flagged INTEGER DEFAULT 0;
ALTER TABLE wa_verse_records ADD COLUMN delete_flagged INTEGER DEFAULT 0;
ALTER TABLE wa_term_related_words ADD COLUMN delete_flagged INTEGER DEFAULT 0;
```

This migration must be applied via `engine/migrate.py` before `AUDIT_WORD` is run.

### 4.3 Active-record filter

All queries that count, display, or compare "current" data must exclude flagged rows:

```sql
AND (delete_flagged = 0 OR delete_flagged IS NULL)
```

This applies in: A2 (DB snapshot), A4 (gap report), A10 (verse counts, testament_coverage, strongs_list).

### 4.4 DB_ONLY_TERM category

Terms present in `wa_term_inventory` for this file_id whose `strongs_number` is **not** in the current Step 1 `include_codes` list are categorised as `DB_ONLY_TERM`. They are listed in the gap report (A4) and the researcher decides at A5 whether to flag them for deletion.

These include legitimately added terms from prior runs (e.g. H4578, H5397 for soul) that STEP's current vocabulary cluster does not return. They are **never silently dropped**.

---

## 5. Full Step Sequence

| Step | Label | Purpose | Tables read | Tables written | STOP/REVIEW |
|------|-------|---------|-------------|----------------|-------------|
| **Pre-A1** | Lock sentinel + run open | Set lock; open run log | `word_registry` | `word_registry`, `engine_run_log` | Stale lock → STOP |
| **A1** | Explicit invocation + registry display | Require typed `CONFIRM`; show full registry entry + notes | `word_registry`, `wa_file_index` | — | No CONFIRM → abort. No `wa_file_index` → redirect NEW_WORD |
| **A2** | DB snapshot read (Word Extract Report) | Load ALL tables for this word into memory; display report; check STOP criteria | All 16 content tables | — | Missing Sections 3, 4, 8, or 9 (mti) AND word not COVERED/REPLACED → STOP + show full report |
| **A3** | Load + validate Step 1 JSON | Find, load, and validate the extract JSON; display meta summary | — | `engine_stream_checkpoint` (open streams) | File not found → STOP. Word mismatch → STOP |
| **A4** | Build gap report (all streams) | Compare JSON vs DB per stream; categorise every discrepancy; print report. No DB writes. | In-memory A2 data | — | Always show; proceed to A5 |
| **A5** | Researcher review gate | Interactive approve/skip per gap category | — | — | None approved → clean exit |
| **A6** | Apply approved changes | Atomic transactions per stream; INSERT, UPDATE, SET delete_flagged | See stream tables | `wa_term_inventory`, `wa_term_related_words`, `mti_terms`, `wa_verse_records`, `wa_verse_term_links`, `engine_stream_checkpoint` | Stream failure → STOP + rollback that stream only |
| **A7** | Meaning handler | Re-parse all meanings; migrate 33 legacy records to tables | `wa_term_inventory` (meaning fields) | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed`, `wa_term_inventory` | Parse error → REVIEW |
| **A8** | Flag engine | Re-derive all derivable flags | All content tables | `wa_data_quality_flags`, `wa_term_phase2_flags` | Cannot fail |
| **A9** | Audit checks | WR-01–WR-20; write word_run_state | All content tables | `word_run_state` | STOP result → researcher approval before A10 |
| **A10** | Word registry + file index update | Compute strongs_list, testament_coverage, term/verse counts; update notes; close run; clear lock | `wa_verse_records`, `wa_term_inventory` | `wa_file_index`, `word_registry`, `engine_run_log` | Should not fail |

---

## 6. Step-by-Step Detail

### Pre-A1 — Lock Sentinel and Run Open

**Purpose:** Prevent concurrent runs; open the engine_run_log row before any other operation.

**Procedure:**
1. Read `word_registry.last_automation_run` WHERE id = registry_id.
2. If value = `'IN_PROGRESS'` (the LOCK_SENTINEL from `engine/constants.py`): print stale-lock warning; prompt researcher to confirm override or abort. Default = abort (STOP).
3. If clear: `UPDATE word_registry SET last_automation_run = 'IN_PROGRESS' WHERE id = ?`; commit immediately.
4. Call `make_run_id("AUDIT_WORD")` → `run_id`.
5. Call `open_run(conn, run_id, "AUDIT_WORD", [registry_id])` — inserts `engine_run_log` row with `outcome = 'RUNNING'`.

**Tables written:** `word_registry` (lock), `engine_run_log` (open row)  
**STOP:** Stale lock and researcher did not confirm override.

---

### A1 — Explicit Invocation + Registry Display

**Purpose:** Require deliberate researcher confirmation; display the full registry entry for review.

**Procedure:**
1. Load the full `word_registry` row: `SELECT * FROM word_registry WHERE id = ?`
2. Display ALL columns in a formatted terminal block:
   ```
   ╔══════════════════════════════════════════════════════════
   ║ AUDIT_WORD — Registry Entry
   ╠══════════════════════════════════════════════════════════
   ║ id:                  182
   ║ word:                soul
   ║ source_list:         High Confidence
   ║ phase1_status:       Complete
   ║ phase1_term_count:   26
   ║ phase1_verse_count:  1143
   ║ strongs_list:        [{"strong":"H5315G","count":179}, ...]
   ║ notes:               [full text displayed]
   ║ ...all other fields...
   ╚══════════════════════════════════════════════════════════
   ```
3. If `word_registry.notes` is non-NULL: display notes prominently with a `[NOTES]` header, as researcher instructions may be present.
4. Check `wa_file_index` for rows with `registry_id = str(registry_id)`. If none found: STOP → "No file index records found. Run NEW_WORD mode first."
5. Display file_ids found: `found {n} file_index record(s): file_ids = [...]`
6. Prompt: `Type CONFIRM to proceed with audit of '{word}' (registry {id}): `
7. If researcher does not type exactly `CONFIRM`: print "Audit aborted." → clean exit (not a STOP; no error logged). Clear lock sentinel.

**Tables read:** `word_registry`, `wa_file_index`  
**Tables written:** None  
**STOP:** No `wa_file_index` rows → redirect to NEW_WORD.

---

### A2 — DB Snapshot Read (Word Extract Report)

**Purpose:** Load all existing data for this word into memory across all 16 affected tables; detect structural completeness problems early; display the Word Extract Report.

**Procedure:**

**A2.1 — Load all tables into memory:**

Read using `file_ids` from A1 and `registry_id`. All queries are SELECT only.

| Query group | SQL pattern |
|-------------|------------|
| File index | `SELECT * FROM wa_file_index WHERE registry_id = ?` |
| Terms | `SELECT * FROM wa_term_inventory WHERE file_id IN (...)` |
| Related words | `SELECT * FROM wa_term_related_words WHERE term_inv_id IN (...)` |
| Root family | `SELECT * FROM wa_term_root_family WHERE term_inv_id IN (...)` |
| Phase2 flags | `SELECT * FROM wa_term_phase2_flags WHERE term_inv_id IN (...)` |
| Quality flags | `SELECT * FROM wa_data_quality_flags WHERE file_id IN (...)` |
| Cross-registry | `SELECT * FROM wa_cross_registry_links WHERE file_id IN (...)` |
| MTI terms | `SELECT * FROM mti_terms WHERE owning_registry = ?` |
| MTI flags | `SELECT * FROM mti_term_flags WHERE mti_term_id IN (...)` |
| MTI cross-refs | `SELECT * FROM mti_term_cross_refs WHERE mti_term_id IN (...)` |
| Meaning parsed | `SELECT * FROM wa_meaning_parsed WHERE term_inv_id IN (...)` |
| Meaning sense | `SELECT * FROM wa_meaning_sense WHERE parsed_meaning_id IN (...)` |
| Meaning stem | `SELECT * FROM wa_meaning_stem WHERE parsed_meaning_id IN (...)` |
| LSJ parsed | `SELECT * FROM wa_lsj_parsed WHERE term_inv_id IN (...)` |
| Verse records | `SELECT * FROM wa_verse_records WHERE file_id IN (...)` |
| Verse term links | `SELECT * FROM wa_verse_term_links WHERE verse_id IN (...)` |

All results stored as in-memory dicts keyed by their primary ID for O(1) lookup in A4.

**A2.2 — Schema version check:**

Read `schema_version` table. If version ≠ `EXPECTED_SCHEMA_VERSION` from `engine/constants.py`: STOP → schema mismatch message.

**A2.3 — Structural completeness check (STOP criteria):**

Check whether the following are populated for this word. Use only active records (where `delete_flagged = 0 OR delete_flagged IS NULL`):

| Section | Check | Required tables |
|---------|-------|-----------------|
| Section 3 | wa_file_index rows > 0 | `wa_file_index` |
| Section 4 | wa_term_inventory rows > 0 | `wa_term_inventory` |
| Section 8 | wa_verse_records rows > 0 | `wa_verse_records` |
| Section 9 | mti_terms rows > 0 | `mti_terms` |

If any check fails AND `word_registry.phase1_status` NOT IN `('COVERED', 'REPLACED', 'SPECIAL_HANDLING')`:

→ STOP. Display:
```
[STOP] A2: Structural data missing for word '{word}' (registry {id}).
Missing sections: wa_term_inventory, wa_verse_records
This word has not been fully initialised. Run NEW_WORD mode or check source data.

[WORD EXTRACT REPORT — FULL]
...full report follows...
```

**A2.4 — Display Word Extract Report:**

Print a formatted report showing row counts per table and a summary of key fields:

```
╔══════════════════════════════════════════════════════════════
║ WORD EXTRACT REPORT — soul (registry 182)
╠══════════════════════════════════════════════════════════════
║  wa_file_index          : 1 row(s)
║  wa_term_inventory      : 26 row(s)
║  wa_term_related_words  : 47 row(s)
║  wa_term_root_family    : 31 row(s)
║  wa_term_phase2_flags   : 12 row(s)
║  wa_data_quality_flags  : 8 row(s)
║  wa_cross_registry_links: 3 row(s)
║  mti_terms              : 26 row(s)
║  mti_term_flags         : 5 row(s)
║  mti_term_cross_refs    : 2 row(s)
║  wa_meaning_parsed      : 19 row(s)
║  wa_meaning_sense       : 87 row(s)
║  wa_meaning_stem        : 14 row(s)
║  wa_lsj_parsed          : 3 row(s)
║  wa_verse_records       : 1143 row(s)
║  wa_verse_term_links    : 0 row(s)   ← NOTE: table empty, will be populated in A6
╚══════════════════════════════════════════════════════════════
```

**Tables read:** All 16 content tables  
**Tables written:** None  
**STOP:** Schema mismatch. Structural completeness failure with non-exempt word.

---

### A3 — Load and Validate Step 1 JSON

**Purpose:** Locate and load the Step 1 extract file; validate it against the registry entry; open stream checkpoints in the log.

**Procedure:**
1. Search `research/discovery/` for files matching pattern: `{registry_no:03d}_{word}_step_data_*.json`
   - `registry_no` = `str(registry_id).zfill(3)`
   - `word` = `word_registry.word` (lowercase)
2. If no file found: STOP → "Step 1 extract file not found. Run `scripts/word_study_extract.py --word {word}` first."
3. If multiple files found: display list with dates → prompt researcher to select by number.
4. Load and parse the JSON.
5. Validate:
   - `meta.english_anchor` == `word_registry.word` (case-insensitive) → mismatch: STOP.
   - `meta.include_codes` is non-empty → empty: STOP.
6. Display meta summary:
   ```
   [A3] Step 1 JSON loaded: 182_soul_step_data_20260323.json
        Generated:  2026-03-23
        Anchor codes: H5315G, G5590G
        Terms evaluated: 24 (G1:13 G2:10 G2r:1 G3:2 G4:0 G5:0)
        Include codes: 17   Exclude codes: 7
   ```
7. Open `engine_stream_checkpoint` rows for streams: `VOCAB_STREAM`, `VERSE_STREAM`, `VTL_STREAM`, `MEANING_STREAM` — status = `'pending'`.

**Tables read:** None (filesystem only)  
**Tables written:** `engine_stream_checkpoint` (open stream rows)  
**STOP:** File not found. Word mismatch. Empty include_codes.

---

### A4 — Gap Report (All Streams)

**Purpose:** Compare JSON data against the in-memory DB snapshot across all three streams. Categorise every discrepancy. Print full gap report. No DB writes.

#### A4.1 — Term stream comparison

For each code in `include_codes`:

Find the matching `wa_term_inventory` row using `strongs_number = code` (within this file_id's term set). Allow for STEP canonical form vs stored form differences (e.g., `H5315` vs `H5315G` — apply the same stripping/normalisation used in `new_word.py`).

| Condition | Category | Description |
|-----------|----------|-------------|
| No matching `wa_term_inventory` row | `NEW_TERM` | This term code has no DB record at all |
| Matching row exists, no `mti_terms` row | `MISSING_MTI` | Term inventory exists but MTI record is absent |
| Matching row exists, STEP-owned fields differ | `STALE_TERM` | One or more STEP-owned fields have changed upstream |
| Matching row exists, all fields match (within tolerance) | `OK` | No change required |

**STEP-owned fields compared for STALE_TERM detection:**

| wa_term_inventory column | JSON field |
|--------------------------|-----------|
| `transliteration` | `transliteration` |
| `step_search_gloss` | `gloss` |
| `word_analysis_gloss` | `gloss` |
| `occurrence_count` | `vocab_count` |
| `meaning` | `medium_def` (normalised: strip HTML, normalise whitespace) |
| `lsj_entry` | `lsj_entry` |
| `short_def_mounce` | `short_def_mounce` |

**DB_ONLY_TERM detection:**

For each `wa_term_inventory` row in this file_id's term set whose `strongs_number` is NOT in `include_codes`: → `DB_ONLY_TERM`. These represent terms added in prior runs that STEP's current cluster does not return. List each with:
- `strongs_number`, `transliteration`, `gloss`, active verse count for this term.

#### A4.2 — Related words comparison

For each include_code's JSON `related_words` list vs `wa_term_related_words` rows for that term_inv_id:

| Condition | Category |
|-----------|----------|
| JSON has a related word (by strongs_number) not in DB | `MISSING_RELATED` |
| DB has a related word not in current JSON | `ORPHAN_RELATED` |

#### A4.3 — Verse stream comparison

For each include_code and its `verses` array:

Locate the matching `wa_term_inventory` row → get `term_inv_id`. Get all `wa_verse_records` for that `term_inv_id` with `delete_flagged = 0`.

| Condition | Category |
|-----------|----------|
| `ref` in JSON but not in DB | `MISSING_VERSE` |
| `ref` in DB but not in JSON | `ORPHAN_VERSE` (candidate for delete-flag) |
| `ref` in both, STEP fields differ | `STALE_VERSE` |
| `ref` in both, all STEP fields match | `OK` |

**STEP-owned fields compared for STALE_VERSE:**

| wa_verse_records column | JSON field |
|-------------------------|-----------|
| `verse_text` | `esv_text` |
| `target_word` | `target_word` |
| `span_strong_match` | `span_strong_match` |
| `context_before` | `context_before` |
| `context_after` | `context_after` |

#### A4.4 — wa_verse_term_links comparison

For each include_code and each verse in its `verses` array:

Resolve `verse_id` from the in-memory verse records (match by `term_inv_id` + `reference`). Resolve `term_inv_id` from in-memory term records.

Check `wa_verse_term_links` for row where `(verse_id, term_inv_id)` matches.

| Condition | Category |
|-----------|----------|
| No `wa_verse_term_links` row | `MISSING_VTL` |
| Row exists, span columns differ | `STALE_VTL` |
| Row exists, all columns match | `OK` |

Note: If `wa_verse_term_links` is empty for this word (first audit since table was created), all verse-term combinations will be `MISSING_VTL`. This is expected and is reported as a single summary count rather than individual lines.

#### A4.5 — Gap report output

Print a structured report:

```
╔══════════════════════════════════════════════════════════════
║ GAP REPORT — soul (registry 182)  |  JSON: 2026-03-23
╠══════════════════════════════════════════════════════════════
║  STREAM 1 — TERMS
║    NEW_TERM          : 0   [no new term codes in this extract]
║    STALE_TERM        : 3   [H5315G: occurrence_count 249→251; ...]
║    MISSING_MTI       : 0
║    DB_ONLY_TERM      : 2   [H4578 (1 verse), H5397 (3 verses)]
║    OK                : 24
║
║  STREAM 1 — RELATED WORDS
║    MISSING_RELATED   : 2
║    ORPHAN_RELATED    : 1
║
║  STREAM 2 — VERSE RECORDS
║    MISSING_VERSE     : 8   [by term: H5315G: 3, H5314: 1, G5590G: 4]
║    ORPHAN_VERSE      : 2   [by term: H5315G: 2]
║    STALE_VERSE       : 14  [verse_text changed: 12; span_strong_match changed: 2]
║    OK                : 1119
║
║  STREAM 2 — VERSE_TERM_LINKS
║    MISSING_VTL       : 1143  [entire table empty — first audit]
║    STALE_VTL         : 0
║    OK                : 0
╚══════════════════════════════════════════════════════════════
[Detail lines for non-OK items follow]
```

**Tables read:** None (uses in-memory A2 data + A3 JSON)  
**Tables written:** None  
**STOP:** None — gap report always shown.

---

### A5 — Researcher Review Gate

**Purpose:** Present the gap report and require explicit researcher approval for each category before any DB writes occur.

**Procedure:**

Display the gap report (A4.5 output). Then prompt for each category that has non-zero count:

```
─────────────────────────────────────────────────────────────
REVIEW GATE — select actions to approve:
─────────────────────────────────────────────────────────────
 [STREAM 1 — TERMS]
  Update 3 STALE_TERM record(s)?                     [y/n]: 
  Flag 2 DB_ONLY_TERM record(s) for deletion?        [y/n]: 
  Insert 2 MISSING_RELATED word(s)?                  [y/n]: 
  Flag 1 ORPHAN_RELATED word(s) for deletion?        [y/n]: 

 [STREAM 2 — VERSES]
  Insert 8 MISSING_VERSE record(s)?                  [y/n]: 
  Flag 2 ORPHAN_VERSE record(s) for deletion?        [y/n]: 
  Update 14 STALE_VERSE record(s)?                   [y/n]: 
  Insert/update 1143 MISSING_VTL link(s)?            [y/n]: 
─────────────────────────────────────────────────────────────
```

Note: If NEW_TERM is present, a special prompt appears:
```
  Insert NEW_TERM {code} '{gloss}' into wa_term_inventory + mti_terms?  [y/n]: 
```
(One prompt per NEW_TERM code, since each is a significant structural addition.)

**If researcher answers 'n' to all prompts:** Print "No changes approved. Audit exited cleanly." Update `engine_run_log.outcome = 'APPROVED_NONE'`. Clear lock sentinel. Exit.

**Tables read/written:** None  
**STOP:** None — researcher can exit cleanly.

---

### A6 — Apply Approved Changes

**Purpose:** Execute all approved insertions, updates, and delete-flag modifications. Each stream runs in its own transaction. A stream failure rolls back only that stream.

#### A6.1 — Term stream

**Approved: STALE_TERM update**

For each STALE_TERM code:
```sql
UPDATE wa_term_inventory SET
    transliteration     = ?,
    step_search_gloss   = ?,
    word_analysis_gloss = ?,
    occurrence_count    = ?,
    meaning             = ?,
    meaning_numbered    = ?,
    lsj_entry           = ?,
    short_def_mounce    = ?,
    last_changed        = datetime('now')
WHERE id = ?
```
Fields set from the JSON term record. Researcher-owned fields (status_note, also_spelled, etc.) are NOT in this UPDATE.

**Approved: STALE_TERM related words refresh**

For each STALE_TERM code (and any NEW_TERM):
```sql
DELETE FROM wa_term_related_words WHERE term_inv_id = ?
```
Then INSERT one row per entry in JSON `related_words`:
```sql
INSERT INTO wa_term_related_words (term_inv_id, strongs_number, gloss, transliteration)
VALUES (?, ?, ?, ?)
```

**Approved: NEW_TERM insert**

Order of operations:
1. INSERT `wa_term_inventory` with all STEP-owned fields. Set `file_id`, `language`, `term_id` (= code), `strongs_number` (= code). Leave researcher-owned fields NULL.
2. INSERT `wa_term_related_words` for all related_words in JSON.
3. INSERT `mti_terms` (owning_registry, owning_word, strongs_number, transliteration, gloss, language, extraction_date=NOW).

**Approved: DB_ONLY_TERM delete-flag**

```sql
UPDATE wa_term_inventory SET delete_flagged = 1 WHERE id = ?
```

Update stream checkpoint: `upsert_checkpoint(conn, run_id, 'VOCAB_STREAM', 'complete', rows_written=N)`

#### A6.2 — Verse stream

All verse stream operations resolve `book_id` from `book_code_variants` → `books.id` for new records.

**Approved: MISSING_VERSE insert**

For each MISSING_VERSE ref (from JSON verse record):
```sql
INSERT INTO wa_verse_records (
    file_id, term_inv_id, term_id, transliteration,
    book_id, reference, chapter, verse_num, testament,
    translation, verse_text, target_word,
    span_strong_match, context_before, context_after,
    created_at
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'ESV', ?, ?, ?, ?, ?, datetime('now'))
```

After INSERT: get `lastrowid` as `new_verse_id`. Immediately INSERT into `wa_verse_term_links`:
```sql
INSERT INTO wa_verse_term_links (
    verse_id, term_inv_id,
    step_subgloss_code, step_subgloss_label,
    span_strong_match, target_word
) VALUES (?, ?, ?, ?, ?, ?)
```

**Approved: STALE_VERSE update**

```sql
UPDATE wa_verse_records SET
    verse_text        = ?,
    target_word       = ?,
    span_strong_match = ?,
    context_before    = ?,
    context_after     = ?,
    updated_at        = datetime('now')
WHERE term_inv_id = ? AND reference = ?
```

**Approved: ORPHAN_VERSE delete-flag**

```sql
UPDATE wa_verse_records SET delete_flagged = 1 WHERE term_inv_id = ? AND reference = ?
```

**wa_verse_term_links — MISSING_VTL insert / STALE_VTL update**

For each in-scope (verse_id, term_inv_id) pair:

If row is missing (INSERT):
```sql
INSERT INTO wa_verse_term_links (
    verse_id, term_inv_id,
    step_subgloss_code, step_subgloss_label,
    span_strong_match, target_word
) VALUES (?, ?, ?, ?, ?, ?)
```
Use `span_code_found` from JSON verse as `step_subgloss_code`, `span_label_found` as `step_subgloss_label`.

If row exists but span columns differ (UPDATE):
```sql
UPDATE wa_verse_term_links SET
    step_subgloss_code  = ?,
    step_subgloss_label = ?,
    span_strong_match   = ?,
    target_word         = ?
WHERE verse_id = ? AND term_inv_id = ?
```

Update stream checkpoint: `upsert_checkpoint(conn, run_id, 'VERSE_STREAM', 'complete', ...)` and `upsert_checkpoint(conn, run_id, 'VTL_STREAM', 'complete', ...)`

#### A6.3 — Testament re-derivation per term

After all verse writes, for each `term_inv_id` in the include set:
```sql
SELECT DISTINCT testament
FROM wa_verse_records
WHERE term_inv_id = ? AND span_strong_match = 1
  AND (delete_flagged = 0 OR delete_flagged IS NULL)
```
Compute: `'OT_only'` / `'NT_only'` / `'both'` / NULL.
```sql
UPDATE wa_term_inventory SET testament = ? WHERE id = ?
```

#### A6.4 — Verification

After all stream transactions commit:
```
[A6 VERIFY]
  wa_term_inventory   : {n} rows active  ({n_flagged} flagged for deletion)
  wa_verse_records    : {n} rows active  ({n_flagged} flagged for deletion)
  wa_verse_term_links : {n} rows
```

---

### A7 — Meaning Handler

**Purpose:** Re-parse all term meanings into the dedicated meaning tables; migrate legacy records where meaning text still lives in `wa_term_inventory` fields.

**Procedure:**

**A7.1 — Identify legacy records**

A "legacy" record is a `wa_term_inventory` row where:
- `meaning` IS NOT NULL (has text in the term row), AND
- No `wa_meaning_parsed` row exists for this `term_inv_id`

These ~33 records pre-date the meaning tables. Query:
```sql
SELECT ti.id, ti.strongs_number, ti.meaning
FROM wa_term_inventory ti
LEFT JOIN wa_meaning_parsed mp ON mp.term_inv_id = ti.id
WHERE ti.file_id IN (?) AND ti.meaning IS NOT NULL AND mp.id IS NULL
```

Display count: `[A7] Found {n} legacy meaning records to migrate.`

**A7.2 — Build vocab_map for meaning parser**

Build a dict keyed by `strongs_number`:
```python
vocab_map = {
    term["strongs_number"]: {"medium_def": json_term["medium_def"]}
    for json_term in include_terms
    if json_term.get("medium_def")
}
```
Prefer the JSON `medium_def` over the DB `meaning` field, since the JSON is the current STEP data. For any term in DB but not in JSON (DB_ONLY_TERMs): use the DB `meaning` field.

**A7.3 — Run meaning parser**

Call `run_parser_for_file(conn, file_id, vocab_map)` for each file_id.

This function (`engine/meaning_parser.py`) INSERTs/UPDATEs:
- `wa_meaning_parsed` (one row per term)
- `wa_meaning_sense` (one or more rows per term)
- `wa_meaning_stem` (if stems detected)
- `wa_lsj_parsed` (Greek terms with `lsj_entry`)

After parsing: UPDATE `wa_term_inventory.parsed_meaning_id` for each term:
```sql
UPDATE wa_term_inventory SET parsed_meaning_id = ?
WHERE id = ?
```

**A7.4 — Legacy field migration**

For each legacy record where `wa_meaning_parsed` row now exists:
1. Confirm `wa_meaning_parsed`, `wa_meaning_sense` rows were written (count > 0 for this term).
2. If confirmed:
   ```sql
   UPDATE wa_term_inventory
   SET meaning = NULL, meaning_numbered = NULL
   WHERE id = ?
   ```
3. Display: `[MIGRATED] {strongs_number} ({gloss}) — meaning moved to wa_meaning_parsed (id={mp_id})`

**A7.5 — Verify**

```sql
SELECT COUNT(*) FROM wa_meaning_parsed mp
JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id
WHERE ti.file_id IN (?)
```
Print: `[A7 VERIFY] wa_meaning_parsed: {n} rows  |  senses: {n}  |  stems: {n}`

Update stream checkpoint: `upsert_checkpoint(conn, run_id, 'MEANING_STREAM', 'complete', rows_written=N)`

**Tables written:** `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed`, `wa_term_inventory` (parsed_meaning_id; NULL legacy fields)

---

### A8 — Flag Engine

**Purpose:** Re-derive all algorithmic (derivable) data quality flags and phase-2 flags for this word.

**Procedure:**

Call `run_flag_engine(conn, file_id, registry_id)` for each `file_id`.

The flag engine:
- Reads `wa_term_inventory`, `wa_verse_records`, `wa_data_quality_flags` (to know which flags are researcher-owned)
- Writes `wa_data_quality_flags` (derivable flags only; researcher-set flags are preserved)
- Writes `wa_term_phase2_flags` (e.g. `GOD_AS_SUBJECT` if `god_as_subject = 1`, `SOMATIC_INNER_LINK` if `somatic_link = 1`)

Print: `[A8] Flag engine complete. Quality flags: {n} rows  |  Phase2 flags: {n} rows`

Update stream checkpoint: `upsert_checkpoint(conn, run_id, 'FLAG_STREAM', 'complete', rows_written=N)`

**Tables written:** `wa_data_quality_flags`, `wa_term_phase2_flags`

---

### A9 — Audit Checks

**Purpose:** Run structured data-quality checks WR-01 through WR-20; write the final per-word outcome.

**Procedure:**

Call `run_audit(conn, file_ids[0], registry_id)` → returns `{"result": "PASS"|"REVIEW"|"STOP", "checks": [...]}`

Display each non-PASS check:
```
[A9] Audit results:
     PASS   WR-01: registry row present
     PASS   WR-02: file_index present
     REVIEW WR-07: 2 terms have no verse records
     STOP   WR-12: mti_terms count (26) ≠ wa_term_inventory count (28)
```

Call `write_word_run_state(conn, run_id, registry_id, word, "AUDIT_WORD_A9", result, detail_dict, stop_reason)`.

If result == `"STOP"`:
Print full stop reason.
Prompt: `Audit result is STOP. Proceed to registry update (A10) anyway? [y/n]: `
If `n`: set `engine_run_log.outcome = 'STOPPED'`; clear lock; exit.

**Tables written:** `word_run_state`

---

### A10 — Word Registry + File Index Update

**Purpose:** Compute all derived values, update the registry entry and file index, close the run log, and clear the lock sentinel.

**Procedure:**

**A10.1 — testament_coverage for each file_id:**
```sql
SELECT DISTINCT testament
FROM wa_verse_records
WHERE file_id = ? AND span_strong_match = 1
  AND (delete_flagged = 0 OR delete_flagged IS NULL)
```
Compute: `'OT_only'` / `'NT_only'` / `'both'` / NULL.
```sql
UPDATE wa_file_index SET testament_coverage = ? WHERE id = ?
```

**A10.2 — Compute strongs_list:**
```sql
SELECT term_id, COUNT(*) as cnt
FROM wa_verse_records
WHERE file_id IN (?) AND span_strong_match = 1
  AND (delete_flagged = 0 OR delete_flagged IS NULL)
GROUP BY term_id
ORDER BY cnt DESC
```
Format as JSON array: `[{"strong": "H5315G", "count": 179}, {"strong": "H5314", "count": 3}, ...]`

**A10.3 — Compute term and verse counts:**
```sql
-- Term count (active, include terms)
SELECT COUNT(*) FROM wa_term_inventory
WHERE file_id IN (?) AND (delete_flagged = 0 OR delete_flagged IS NULL)

-- Verse count (span-confirmed, active)
SELECT COUNT(*) FROM wa_verse_records
WHERE file_id IN (?) AND span_strong_match = 1
  AND (delete_flagged = 0 OR delete_flagged IS NULL)
```

**A10.4 — Compose notes update:**

Append to `word_registry.notes` (do not replace):
- If errors or anomalies exist: list them with `[ANOMALY YYYYMMDD]` prefix.
- If clean run: append `[AUDIT YYYYMMDD] Audit complete. Terms: {n}. Verses: {n}. Result: {result}.`

**A10.5 — Update word_registry:**
```sql
UPDATE word_registry SET
    phase1_status       = ?,     -- 'Complete' if PASS, else 'In Progress'
    phase1_term_count   = ?,
    phase1_verse_count  = ?,
    strongs_list        = ?,     -- JSON string computed in A10.2
    last_automation_run = ?,     -- ISO datetime of this run
    automation_run_id   = ?,     -- run_id
    notes               = ?      -- updated notes field
WHERE id = ?
```

**A10.6 — Clear lock sentinel:**
```sql
UPDATE word_registry SET last_automation_run = ? WHERE id = ?
```
Where the value is the actual completion datetime (replaces the `'IN_PROGRESS'` lock).

**A10.7 — Close run:**
```sql
-- via close_run(conn, run_id, outcome, counts)
UPDATE engine_run_log SET
    completed_at = ?,
    outcome = 'COMPLETE',  -- or 'STOPPED' if A9 gate refused
    words_attempted = 1,
    words_complete = 1,
    total_verses_inserted = ?,
    total_verses_updated = ?,
    total_meanings_parsed = ?
WHERE run_id = ?
```

**Print completion banner:**
```
╔══════════════════════════════════════════════════════════════
║  AUDIT_WORD COMPLETE
║  Word:       soul (registry 182)
║  Run ID:     RUN-20260323_XXXXXX-AUDIT_WORD
║  Result:     PASS
║  Verses ins: 8   upd: 14   flagged: 2
║  VTL ins:    1143
║  Meanings:   26 parsed, 3 migrated
╚══════════════════════════════════════════════════════════════
```

**Tables written:** `wa_file_index`, `word_registry`, `engine_run_log`

---

## 7. wa_verse_term_links — Population Rules

This table was not present when `audit_word.py` was originally written. The first audit run for any word will find it completely empty for that word (all MISSING_VTL). This is expected and handled at scale by a single batch INSERT.

### FK resolution

Unlike Step 1 (extract), the audit has full DB access. FKs are resolved from in-memory data loaded in A2:

- `verse_id`: matched from in-memory `wa_verse_records` dict, keyed by `(term_inv_id, reference)`
- `term_inv_id`: matched from in-memory `wa_term_inventory` dict, keyed by `strongs_number`

No additional queries needed at write time.

### Span columns — source of truth

| Column | Source |
|--------|--------|
| `step_subgloss_code` | `span_code_found` from the JSON verse record (the matched `strong=` attribute from the HTML span) |
| `step_subgloss_label` | `span_label_found` from the JSON verse record (looked up at Step 1 time) |
| `span_strong_match` | `span_strong_match` from the JSON verse record |
| `target_word` | `target_word` from the JSON verse record |

### Handling sub-gloss codes

For a verse fetched under code `H5315G`, the span may match a sub-gloss code like `H5315H` (`soul: life`). The JSON already has `span_code_found = "H5315H"` and `span_label_found = "soul: life"` (populated by `word_study_extract.py`). The audit simply writes these values directly into `wa_verse_term_links.step_subgloss_code` and `step_subgloss_label`.

---

## 8. Meaning Handling — Legacy Records

### Background

At schema creation time, a term's full meaning text was stored in `wa_term_inventory.meaning` and `wa_term_inventory.meaning_numbered`. The `wa_meaning_parsed`, `wa_meaning_sense`, and `wa_meaning_stem` tables were introduced later as dedicated meaning structures. Approximately 33 records still have meaning text in the term-level fields.

### Identification

As described in A7.1: a term is "legacy" if `wa_term_inventory.meaning IS NOT NULL` and no `wa_meaning_parsed` row exists.

### Migration behaviour

When A7 runs the meaning parser for a legacy record:
1. The `medium_def` from the Step 1 JSON is used as the parse input (current STEP data — may have changed from the stored value).
2. Parser writes `wa_meaning_parsed` + `wa_meaning_sense` + `wa_meaning_stem`.
3. `parsed_meaning_id` is set on the term row.
4. `meaning` and `meaning_numbered` are cleared (set to NULL) on the term row.

The old values are effectively replaced by the structured meaning tables. If the researcher needs to preserve notes from the old `meaning` field, they should do so before running the audit (the A2 Word Extract Report will display the current content).

---

## 9. Logging Tables

### engine_run_log

One row opened at Pre-A1 (`open_run`), updated at each STOP, closed at A10 (`close_run`).

Key fields set by the audit:

| Field | Set when |
|-------|----------|
| `run_id` | Pre-A1 (`make_run_id("AUDIT_WORD")`) |
| `mode` | Pre-A1 (`"AUDIT_WORD"`) |
| `target_registry_ids` | Pre-A1 (JSON array of registry_id) |
| `started_at` | Pre-A1 |
| `outcome` | A10 (`'COMPLETE'`), or earlier if STOP/abort |
| `completed_at` | A10 |
| `words_attempted` | A10 (= 1) |
| `words_complete` | A10 (= 1 if PASS/REVIEW, 0 if STOP) |
| `words_stopped` | A10 (= 1 if STOP) |
| `total_verses_inserted` | A10 (accumulated from A6) |
| `total_verses_filtered` | A10 (orphan verse count) |
| `total_meanings_parsed` | A10 (from A7) |
| `error_detail` | A10 (JSON list of error strings) |

### engine_stream_checkpoint

One row per stream, opened at A3, updated at each stream completion.

| Stream name | Opened at | Completed at |
|-------------|-----------|--------------|
| `VOCAB_STREAM` | A3 | A6.1 |
| `VERSE_STREAM` | A3 | A6.2 |
| `VTL_STREAM` | A3 | A6.2 |
| `MEANING_STREAM` | A3 | A7 |
| `FLAG_STREAM` | A8 (opened and closed) | A8 |

Key fields: `status` (`'pending'` → `'complete'`/`'failed'`), `rows_written`, `rows_filtered`, `error_detail`.

### word_run_state

One row written at A9 by `write_word_run_state()`.

| Field | Value |
|-------|-------|
| `run_id` | From Pre-A1 |
| `registry_id` | Zero-padded to 3 digits |
| `word` | From `word_registry.word` |
| `phase_reached` | `"AUDIT_WORD_A9"` |
| `audit_result` | `"PASS"` / `"REVIEW"` / `"STOP"` |
| `audit_detail` | JSON dict of WR check results |
| `stop_reason` | Populated only if result = `"STOP"` |

### term_fetch_log

The audit reads data from the Step 1 JSON rather than making live STEP API calls. Therefore `term_fetch_log` rows are **not** written during `AUDIT_WORD`. This table is written by `NEW_WORD` mode and the `word_study_extract.py` script (if extended to log fetches). Note this in the terminal: `[A3] Using cached Step 1 JSON — no STEP API calls. term_fetch_log not written.`

---

## 10. Schema Migration Required

Before implementing `AUDIT_WORD`, the following schema migration must be applied:

```sql
-- Migration: add delete_flagged column to three tables
ALTER TABLE wa_term_inventory    ADD COLUMN delete_flagged INTEGER DEFAULT 0;
ALTER TABLE wa_verse_records     ADD COLUMN delete_flagged INTEGER DEFAULT 0;
ALTER TABLE wa_term_related_words ADD COLUMN delete_flagged INTEGER DEFAULT 0;
```

This migration is added to `engine/migrate.py` as a new migration step. The `EXPECTED_SCHEMA_VERSION` in `engine/constants.py` is bumped accordingly (e.g. `v3.2.0` → `v3.3.0`).

All existing rows gain `delete_flagged = 0` (the column default), so the migration is non-destructive.

---

## 11. Complete Tables Touched Summary

| Step | Table | Action |
|------|-------|--------|
| Pre-A1 | `word_registry` | UPDATE `last_automation_run = 'IN_PROGRESS'` (lock); on completion set to `'AUDITED'` |
| Pre-A1 | `engine_run_log` | INSERT (open run) |
| A3 | `engine_stream_checkpoint` | INSERT stream rows (status='pending') |
| A6.1 | `wa_term_inventory` | UPDATE STEP-owned fields (STALE); INSERT (NEW_TERM); UPDATE `delete_flagged=1` (DB_ONLY) |
| A6.1 | `wa_term_related_words` | DELETE+INSERT for updated terms; INSERT (NEW_TERM); UPDATE `delete_flagged=1` (orphans) |
| A6.1 | `mti_terms` | INSERT (NEW_TERM if approved) |
| A6.2 | `wa_verse_records` | INSERT (MISSING); UPDATE STEP fields (STALE); UPDATE `delete_flagged=1` (ORPHAN) |
| A6.2 | `wa_verse_term_links` | INSERT (MISSING_VTL); UPDATE span columns (STALE_VTL) |
| A6.3 | `wa_term_inventory` | UPDATE `testament` per term |
| A6 | `engine_stream_checkpoint` | UPDATE stream rows (status='complete') |
| A7 | `wa_meaning_parsed` | INSERT/UPSERT per term |
| A7 | `wa_meaning_sense` | INSERT/UPSERT per sense |
| A7 | `wa_meaning_stem` | INSERT/UPSERT per stem |
| A7 | `wa_lsj_parsed` | INSERT/UPSERT (Greek terms) |
| A7 | `wa_term_inventory` | UPDATE `parsed_meaning_id`; SET `meaning = NULL`, `meaning_numbered = NULL` (legacy records) |
| A7 | `engine_stream_checkpoint` | UPDATE MEANING_STREAM |
| A8 | `wa_data_quality_flags` | Derivable flags re-written by flag engine |
| A8 | `wa_term_phase2_flags` | Re-derived from term boolean fields |
| A8 | `engine_stream_checkpoint` | UPDATE FLAG_STREAM |
| A9 | `word_run_state` | INSERT result row |
| A10 | `wa_file_index` | UPDATE `testament_coverage` |
| A10 | `word_registry` | UPDATE `phase1_status`, `phase1_term_count`, `phase1_verse_count`, `strongs_list`, `notes`, `last_automation_run`, `automation_run_id` |
| A10 | `engine_run_log` | UPDATE (close run) |

**Tables audited but researcher-owned (A2 reads, writes only for cascades):**

| Table | Audit action |
|-------|-------------|
| `wa_term_root_family` | Read in A2. `delete_flagged=1` cascaded when parent `wa_term_inventory` row is flagged. No new root codes created from STEP data (researcher-assigned). Missing root rows flagged in gap report. |
| `wa_cross_registry_links` | Read in A2. FK integrity verified. No writes — links are researcher-curated. |
| `mti_term_cross_refs` | Read in A2. FK integrity verified. No writes — cross-refs are researcher-curated. |

**Tables never touched by AUDIT_WORD:**

| Table | Reason |
|-------|--------|
| `books`, `book_code_variants` | Reference data — read-only |
| `themes`, `sources` | Unrelated |
| `wa_crosslink_type`, `phase2_flag_types`, `wa_quality_flag_types` | Lookup tables; not modified by audit |
| `wa_term_phase2_flags` | Researcher-assigned analytical flags — never set or cleared by audit |
| `mti_term_flags` | Not re-derived by audit |
| `word_run_state.researcher_approved` | Set to `'PROVISIONAL'` (via `approved_by` field) — full researcher sign-off is a separate action |
| `term_fetch_log` | Not written (no STEP API calls in AUDIT_WORD — JSON is the cached STEP output) |

---

## 12. Confirmed Decisions

### OD-1 — Review gate mode  ✅ CONFIRMED

**Auto-approve is the default.** All INSERT / UPDATE / SET delete_flagged actions are applied automatically without per-item gates. A `--interactive` flag enables the review gate for testing/debugging purposes. In interactive mode, each gap category (STALE_TERM, MISSING_VERSE, etc.) is presented with a Y/n prompt before any writes occur.

---

### OD-2 — STALE field handling  ✅ CONFIRMED

**STALE fields are updated automatically in auto mode.** STALE diffs are shown in the gap report for information. The interactive gate (testing only) allows individual STALE categories to be skipped.

---

### OD-3 — INSERT / UPDATE / DELETE behaviour  ✅ CONFIRMED

**All changes are applied by default.** Every MISSING record is inserted, every STALE record is updated, and every ORPHAN record is flagged for deletion — without requiring per-item approval. The `--interactive` flag allows per-category skip.

---

### OD-4 — Flag handling  ✅ CONFIRMED

**Quality flags (`wa_data_quality_flags`) are fully reset each run.** All existing quality flag rows for this `file_id` are deleted before re-derivation. Flags are re-derived from STEP data using `run_flag_engine`. **Phase 2 flags (`wa_term_phase2_flags`) are NOT touched by `AUDIT_WORD`** — these are researcher-assigned and cannot be set or cleared by the audit process.

---

### OD-5 — Delete-flag column name  ✅ CONFIRMED

`delete_flagged INTEGER DEFAULT 0` — name confirmed. Tables receiving this column: `wa_term_inventory`, `wa_verse_records`, `wa_term_related_words`, `wa_term_root_family`.

---

### OD-6 — Dismissed (old comment, no action required.

---

## 13. Invocation

```bash
# Standard run (auto-approve, latest JSON auto-selected)
python -m engine.engine --mode=audit_word --registry=182
python -m engine.engine --mode=audit_word --registry=4   # anger

# Dry-run: show gap report only, no writes
python -m engine.engine --mode=audit_word --registry=182 --dry-run

# Interactive mode (show review gate per category — testing/debugging)
python -m engine.engine --mode=audit_word --registry=182 --interactive

# Specify extract file explicitly (bypasses auto-select)
python -m engine.engine --mode=audit_word --registry=182 --extract-file=research/discovery/182_soul_step_data_20260323.json
```

**Auto-select behaviour:** When `--extract-file` is not specified, A3 searches `research/discovery/` for all files matching `{registry_no:03d}_{word}_step_data_*.json` and selects the **latest** (lexicographically last date). An older format without registry prefix (`{word}_step_data_*.json`) is also checked as fallback.

---

*End of document. Save and return comments in RESPONSE blocks or inline. Agent will read all feedback before coding begins.*
