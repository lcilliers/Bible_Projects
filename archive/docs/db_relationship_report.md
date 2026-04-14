# Database Relationship Report
**File:** `data/bible_research.db`  
**Schema version:** 3.2.0** (amended — original report was 3.1.0)**  
**Schema applied:** 2026-03-18 (3.1.0) / 2026-03-22 (3.2.0)  
**Report generated:** 2026-03-22  

> **Schema 3.2.0 amendments (2026-03-22):** Fixes 3–7 and 9 from `docs/db_remediation_plan.md` were applied.
> Sections 4, 5, 6, and 7 have been updated in-place to reflect the live 3.2.0 schema.
> See `docs/post_fix_script_review.md` for details of all changes made.
**Purpose:** Deep-dive quality review — full up/down relationship map, constraint gaps, and integrity findings.

---

## Contents

1. [Database Overview](#1-database-overview)
2. [Table Inventory with Row Counts](#2-table-inventory-with-row-counts)
3. [Schema Section Groups](#3-schema-section-groups)
4. [Formal Foreign Key Relationships](#4-formal-foreign-key-relationships)
5. [Missing FK Registrations (Schema vs Live DB)](#5-missing-fk-registrations-schema-vs-live-db)
6. [Soft / Implied Relationships (No FK Constraint)](#6-soft--implied-relationships-no-fk-constraint)
7. [Table-by-Table Relationship Map (Up and Down)](#7-table-by-table-relationship-map-up-and-down)
8. [Critical Issue: FK Enforcement is OFF](#8-critical-issue-fk-enforcement-is-off)
9. [Orphan Analysis](#9-orphan-analysis)
10. [Empty / Underutilised Tables](#10-empty--underutilised-tables)
11. [Summary of Gaps and Issues](#11-summary-of-gaps-and-issues)

---

## 1. Database Overview

| Property | Value |
|---|---|
| Engine | SQLite |
| Schema version | 3.1.0 |
| Total tables | 29 (28 user tables + sqlite_sequence) |
| Total formal FK constraints (PRAGMA) | 19 |
| FK enforcement active | **NO** (`PRAGMA foreign_keys = 0`) |
| FK integrity violations | 0 (pass — but enforcement is off) |

---

## 2. Table Inventory with Row Counts

| Table | Rows | Section |
|---|---|---|
| `book_code_variants` | 112 | 1 — Reference |
| `books` | 66 | 1 — Reference |
| `themes` | **0** | 1 — Reference (empty) |
| `sources` | **0** | 1 — Reference (empty) |
| `word_registry` | 211 | 2 — Registry |
| `wa_file_index` | 199 | 3 — WA File Index |
| `wa_term_inventory` | 1,529 | 4 — WA Term Data |
| `wa_term_related_words` | 10,102 | 4 — WA Term Data |
| `wa_term_root_family` | 641 | 4 — WA Term Data |
| `phase2_flag_types` | 25 | 5 — Phase-2 Flags |
| `wa_term_phase2_flags` | 461 | 5 — Phase-2 Flags |
| `wa_quality_flag_types` | 46 | 6 — WA Quality Flags |
| `wa_data_quality_flags` | 3,254 | 6 — WA Quality Flags |
| `wa_crosslink_type` | 7 | 7 — Cross-Registry |
| `wa_cross_registry_links` | 152 | 7 — Cross-Registry |
| `wa_verse_records` | 57,130 | 8 — Verse Records |
| `mti_terms` | 1,380 | 9 — MTI |
| `mti_term_flags` | 9 | 9 — MTI |
| `mti_term_cross_refs` | 463 | 9 — MTI |
| `engine_run_log` | 36 | 10 — Engine Control |
| `engine_stream_checkpoint` | 7 | 10 — Engine Control |
| `word_run_state` | 188 | 10 — Engine Control |
| `term_fetch_log` | 2,307 | 10 — Engine Control |
| `wa_meaning_parsed` | 1,493 | 11 — Meaning Parsing |
| `wa_meaning_sense` | 6,448 | 11 — Meaning Parsing |
| `wa_meaning_stem` | 695 | 11 — Meaning Parsing |
| `wa_lsj_parsed` | 504 | 11 — Meaning Parsing |
| `schema_version` | 1 | 12 — Metadata |

---

## 3. Schema Section Groups

The schema organises tables into 12 named sections:

| Section | Tables |
|---|---|
| 1 — Reference | `books`, `book_code_variants`, `themes`, `sources` |
| 2 — Registry | `word_registry` |
| 3 — WA File Index | `wa_file_index` |
| 4 — WA Term Data | `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family` |
| 5 — Phase-2 Flags | `phase2_flag_types`, `wa_term_phase2_flags` |
| 6 — WA Quality Flags | `wa_quality_flag_types`, `wa_data_quality_flags` |
| 7 — Cross-Registry | `wa_crosslink_type`, `wa_cross_registry_links` |
| 8 — Verse Records | `wa_verse_records` |
| 9 — MTI Terms | `mti_terms`, `mti_term_flags`, `mti_term_cross_refs` |
| 10 — Engine Control | `engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log` |
| 11 — Meaning Parsing | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` |
| 12 — Schema Metadata | `schema_version` |

---

## 4. Formal Foreign Key Relationships

These are the 19 FK constraints actually registered in the live database (`PRAGMA foreign_key_list`). All are defined with `ON UPDATE NO ACTION / ON DELETE NO ACTION`.

> **Note:** Even though these FKs are registered, they are currently not enforced because `PRAGMA foreign_keys = 0` (see Section 8).

### 4.1 Full FK Map

| # | Child Table | Child Column | → | Parent Table | Parent Column | Notes |
|---|---|---|---|---|---|---|
| 1 | `book_code_variants` | `book_id` | → | `books` | `id` | Maps every book code alias to a canonical book |
| 2 | `engine_stream_checkpoint` | `run_id` | → | `engine_run_log` | `run_id` | Checkpoint belongs to a run |
| 3 | `mti_term_cross_refs` | `mti_term_id` | → | `mti_terms` | `id` | Cross-ref belongs to an MTI term |
| 4 | `mti_term_cross_refs` | `registry_fk` | → | `word_registry` | `id` | *(Added 3.2.0)* Integer FK replacing TEXT `registry` soft link |
| 5 | `mti_term_flags` | `mti_term_id` | → | `mti_terms` | `id` | Flag junction: MTI term |
| 6 | `mti_term_flags` | `flag_id` | → | `phase2_flag_types` | `id` | Flag junction: flag type |
| 7 | `mti_terms` | `owning_registry_fk` | → | `word_registry` | `id` | *(Added 3.2.0)* Integer FK replacing TEXT `owning_registry` soft link |
| 8 | `mti_terms` | `word_data_ref_fk` | → | `wa_file_index` | `id` | *(Added 3.2.0)* Integer FK formalising the "future FK" `word_data_reference` |
| 9 | `term_fetch_log` | `run_id` | → | `engine_run_log` | `run_id` | Fetch log belongs to a run |
| 10 | `wa_cross_registry_links` | `file_id` | → | `wa_file_index` | `id` | Link belongs to a file |
| 11 | `wa_cross_registry_links` | `linked_registry_id` | → | `word_registry` | `id` | Nullable: link to another registry word |
| 12 | `wa_cross_registry_links` | `connection_type_id` | → | `wa_crosslink_type` | `id` | Link type lookup |
| 13 | `wa_data_quality_flags` | `file_id` | → | `wa_file_index` | `id` | Quality flag scoped to a file |
| 14 | `wa_data_quality_flags` | `flag_id` | → | `wa_quality_flag_types` | `id` | Flag type lookup |
| 15 | `wa_file_index` | `word_registry_fk` | → | `word_registry` | `id` | *(Registered 3.2.0)* FK backfilled via Fix 3 |
| 16 | `wa_lsj_parsed` | `term_inv_id` | → | `wa_term_inventory` | `id` | 1:1 LSJ parse ↔ term |
| 17 | `wa_meaning_parsed` | `term_inv_id` | → | `wa_term_inventory` | `id` | 1:1 meaning parse parent ↔ term |
| 18 | `wa_meaning_sense` | `parsed_meaning_id` | → | `wa_meaning_parsed` | `id` | Sense entries belong to a meaning parse |
| 19 | `wa_meaning_stem` | `parsed_meaning_id` | → | `wa_meaning_parsed` | `id` | Stem entries belong to a meaning parse |
| 20 | `wa_term_inventory` | `file_id` | → | `wa_file_index` | `id` | *(Registered 3.2.0)* FK backfilled via Fix 4 |
| 21 | `wa_term_phase2_flags` | `term_inv_id` | → | `wa_term_inventory` | `id` | Flag junction: WA term |
| 22 | `wa_term_phase2_flags` | `flag_id` | → | `phase2_flag_types` | `id` | Flag junction: flag type |
| 23 | `wa_term_related_words` | `term_inv_id` | → | `wa_term_inventory` | `id` | *(Registered 3.2.0)* FK backfilled via Fix 5; CASCADE delete |
| 24 | `wa_term_root_family` | `term_inv_id` | → | `wa_term_inventory` | `id` | *(Registered 3.2.0)* FK backfilled via Fix 6; CASCADE delete |
| 25 | `wa_verse_records` | `book_id` | → | `books` | `id` | Verse located in a book |
| 26 | `wa_verse_records` | `file_id` | → | `wa_file_index` | `id` | *(Registered 3.2.0)* FK backfilled via Fix 7 |
| 27 | `wa_verse_records` | `term_inv_id` | → | `wa_term_inventory` | `id` | *(Registered 3.2.0)* FK backfilled via Fix 7 |
| 28 | `word_run_state` | `run_id` | → | `engine_run_log` | `run_id` | Word run state belongs to a run |

### 4.2 Parent Table Summary (what each parent table "owns" downstream)

| Parent Table | Child Tables (via FK) |
|---|---|
| `books` | `book_code_variants` (via book_id), `wa_verse_records` (via book_id) |
| `engine_run_log` | `engine_stream_checkpoint`, `term_fetch_log`, `word_run_state` |
| `mti_terms` | `mti_term_cross_refs`, `mti_term_flags` |
| `phase2_flag_types` | `mti_term_flags`, `wa_term_phase2_flags` |
| `wa_crosslink_type` | `wa_cross_registry_links` |
| `wa_file_index` | `mti_terms` (via word_data_ref_fk), `wa_cross_registry_links`, `wa_data_quality_flags`, `wa_term_inventory` (via file_id), `wa_verse_records` (via file_id) |
| `wa_meaning_parsed` | `wa_meaning_sense`, `wa_meaning_stem` |
| `wa_quality_flag_types` | `wa_data_quality_flags` |
| `wa_term_inventory` | `wa_lsj_parsed`, `wa_meaning_parsed`, `wa_term_phase2_flags`, `wa_term_related_words`, `wa_term_root_family`, `wa_verse_records` (via term_inv_id) |
| `word_registry` | `mti_term_cross_refs` (via registry_fk), `mti_terms` (via owning_registry_fk), `wa_cross_registry_links` (linked_registry_id, nullable), `wa_file_index` (via word_registry_fk) |

### 4.3 Tables with NO Formal FK to Any Parent

These tables have no FK _outbound_ to a parent, meaning they are root/lookup tables or have all their parent links as soft joins:

| Table | Reason |
|---|---|
| `books` | Root reference table |
| `engine_run_log` | Root engine table |
| `phase2_flag_types` | Lookup table |
| `schema_version` | Metadata only |
| `sources` | Root reference (empty) |
| `themes` | Root reference (empty) |
| `wa_crosslink_type` | Lookup table |
| `wa_data_quality_flags` | FK to file and flag type, but NOT to `wa_term_inventory` despite `term_id` column |
| `wa_quality_flag_types` | Lookup table |
| `word_registry` | Root registry table |

*(3.2.0 note: `mti_terms`, `wa_file_index`, `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family`, and `wa_verse_records` were in this table before schema 3.2.0. All now have registered FKs — see Section 4.1.)*

---

## 5. Missing FK Registrations (Schema vs Live DB)

The current `data/schema/create_tables.sql` defines REFERENCES clauses on these columns, but `PRAGMA foreign_key_list` confirms they are **not registered** in the live database. This means they were added to the schema SQL after the tables were first created, and were never backfilled into the live structures (SQLite's `ALTER TABLE ADD COLUMN` ignores REFERENCES).

| Table | Column | Intended Parent | Parent Column | Orphan Rate |
|---|---|---|---|---|
*(All rows in this section were resolved in schema 3.2.0 via Fixes 3–7 of `docs/db_remediation_plan.md`. Tables were recreated with formal FK clauses. See Section 4.1 for current FK map.)*

| Table | Column | Intended Parent | Parent Column | Status |
|---|---|---|---|---|
| `wa_file_index` | `word_registry_fk` | `word_registry` | `id` | ✅ Registered (Fix 3) |
| `wa_term_inventory` | `file_id` | `wa_file_index` | `id` | ✅ Registered (Fix 4) |
| `wa_term_related_words` | `term_inv_id` | `wa_term_inventory` | `id` | ✅ Registered (Fix 5, CASCADE delete) |
| `wa_term_root_family` | `term_inv_id` | `wa_term_inventory` | `id` | ✅ Registered (Fix 6, CASCADE delete) |
| `wa_verse_records` | `file_id` | `wa_file_index` | `id` | ✅ Registered (Fix 7) |
| `wa_verse_records` | `term_inv_id` | `wa_term_inventory` | `id` | ✅ Registered (Fix 7) |

---

## 6. Soft / Implied Relationships (No FK Constraint)

These relationships exist as TEXT column lookups or integer columns with no FK clause. They are used by application code but carry no database-level enforcement.

| Table | Column | Type | Intended Relationship | Non-Null Count | Orphans | Orphan Rate | Notes |
|---|---|---|---|---|---|---|---|
| `wa_file_index` | `registry_id` | TEXT | → `word_registry.id` | 199 | 17 | 8.5% | Zero-padded format ('001') doesn't match int id (1). `word_registry_fk` is the correct integer FK column for the same purpose. |
| `wa_term_inventory` | `parsed_meaning_id` | INTEGER | → `wa_meaning_parsed.id` | 1,493 | 0 | 0% | Backward pointer; `wa_meaning_parsed.term_inv_id` is the authoritative FK in the other direction. |
| `wa_verse_records` | `term_id` | TEXT | ~ `wa_term_inventory.term_id` | 57,130 | 1 | 0.0% | Denormalised Strong's code; not a true FK join — matches by code not by row id. |
| `wa_data_quality_flags` | `term_id` | TEXT | ~ `wa_term_inventory.term_id` | 3,239 | 53 | 1.6% | Same pattern: TEXT Strong's code. 53 orphan term_ids include legacy codes, 'NO STRONG-…' placeholders, and a '_related' suffix variant. |
| `mti_terms` | `owning_registry` | TEXT | → `word_registry.id` | 1,380 | 0 | 0% | *(3.2.0)* Zero-padding fixed (Fix 2). Integer FK `owning_registry_fk` added (Fix 9) — prefer that for joins. |
| `mti_terms` | `word_data_reference` | TEXT | → `wa_file_index.id` | 1,380 | 0 | 0% | *(3.2.0)* Integer FK `word_data_ref_fk` added (Fix 9) — prefer that for joins. |
| `mti_term_cross_refs` | `registry` | TEXT | → `word_registry.id` | 463 | 0 | 0% | *(3.2.0)* Zero-padding fixed (Fix 2). Integer FK `registry_fk` added (Fix 9) — prefer that for joins. |
| `mti_term_cross_refs` | `word_data_reference` | TEXT | → `wa_file_index.id` | 16 | 0 | 0% | TEXT column retained; no new FK added for this column. |
| `word_run_state` | `registry_id` | TEXT | → `word_registry.id` | 188 | 82 | **44.1%** | **Critical.** Same zero-padding issue — stored as '008', '009' etc., word_registry.id is integer 8, 9. |
| `term_fetch_log` | `registry_id` | TEXT | → `word_registry.id` | 2,307 | 0 | 0% | In this table the IDs appear to be stored without zero-padding. |
| `word_registry` | `automation_run_id` | TEXT | → `engine_run_log.run_id` | 179 | 0 | 0% | Soft back-reference to the last run that processed this word. |

### 6.1 The Zero-Padding Problem

Several tables store registry IDs as zero-padded 3-digit strings (e.g. `'008'`, `'071'`), while `word_registry.id` is a plain INTEGER (e.g. `8`, `71`). When joined as `TEXT = CAST(INTEGER AS TEXT)`, the values don't match. The affected tables and columns are:

- `wa_file_index.registry_id` — 17 rows affected
- `mti_terms.owning_registry` — 16 distinct IDs affected (but 371 rows total because each ID may have multiple terms)
- `mti_term_cross_refs.registry` — 5 distinct IDs affected
- `word_run_state.registry_id` — 82 out of 188 rows affected (44.1%)

`term_fetch_log.registry_id` does NOT have this issue (0 orphans), suggesting it was populated at a later point after the formatting was standardised.

---

## 7. Table-by-Table Relationship Map (Up and Down)

For each table: **upstream** = tables it points to (parents); **downstream** = tables that point to it (children).

---

### `books`
- **Upstream:** none (root reference table)
- **Downstream (formal FK):**
  - `book_code_variants.book_id` — every book alias maps back here
  - `wa_verse_records.book_id` — every verse record has a resolved book

---

### `book_code_variants`
- **Upstream (formal FK):** `books.id` via `book_id`
- **Downstream:** none
- **Purpose:** Translation table — converts STEP/OSIS/variant short codes to canonical `books.id`

---

### `themes`
- **Upstream:** none
- **Downstream:** none
- **Status:** Empty (0 rows). No relationships in use.

---

### `sources`
- **Upstream:** none
- **Downstream:** none
- **Status:** Empty (0 rows). No relationships in use.

---

### `word_registry`
- **Upstream:** none (master root table)
- **Downstream (formal FK):**
  - `wa_cross_registry_links.linked_registry_id` (nullable — 7 NULLs where link was unresolvable)
- **Downstream (soft — as parent):**
  - `wa_file_index.registry_id` (TEXT, 8.5% zero-padding orphans)
  - `wa_file_index.word_registry_fk` (INTEGER, 0 orphans, FK not registered in live DB)
  - `mti_terms.owning_registry` (TEXT, 26.9% orphan rate due to zero-padding)
  - `mti_term_cross_refs.registry` (TEXT, 6.0% orphan rate due to zero-padding)
  - `word_run_state.registry_id` (TEXT, 44.1% orphan rate due to zero-padding)
  - `term_fetch_log.registry_id` (TEXT, 0% orphan rate)
- **Soft back-reference from self:** `automation_run_id` → `engine_run_log.run_id`

---

### `wa_file_index`
- **Upstream (formal FK):** none registered in live DB
- **Upstream (intended, unregistered FK):**
  - `word_registry.id` via `word_registry_fk` (INTEGER, schema has REFERENCES, not in live PRAGMA)
- **Upstream (soft):**
  - `word_registry.id` via `registry_id` (TEXT, dual-column situation)
- **Downstream (formal FK):**
  - `wa_cross_registry_links.file_id`
  - `wa_data_quality_flags.file_id`
- **Downstream (intended, unregistered FK):**
  - `wa_term_inventory.file_id`
  - `wa_verse_records.file_id`
- **Note:** This table has two columns serving the same parent relationship (`registry_id` TEXT soft link and `word_registry_fk` INTEGER intended FK). The TEXT column has formatting inconsistencies; the INTEGER column is clean but its FK is not enforced.

---

### `wa_term_inventory`
- **Upstream (intended, unregistered FK):**
  - `wa_file_index.id` via `file_id`
- **Downstream (formal FK):**
  - `wa_lsj_parsed.term_inv_id`
  - `wa_meaning_parsed.term_inv_id`
  - `wa_term_phase2_flags.term_inv_id`
- **Downstream (intended, unregistered FK):**
  - `wa_term_related_words.term_inv_id`
  - `wa_term_root_family.term_inv_id`
  - `wa_verse_records.term_inv_id`
- **Soft back-reference:** `parsed_meaning_id` → `wa_meaning_parsed.id` (reverse pointer; authoritative direction is the FK in `wa_meaning_parsed`)

---

### `wa_term_related_words`
- **Upstream (intended, unregistered FK):** `wa_term_inventory.id` via `term_inv_id`
- **Downstream:** none

---

### `wa_term_root_family`
- **Upstream (intended, unregistered FK):** `wa_term_inventory.id` via `term_inv_id`
- **Downstream:** none

---

### `phase2_flag_types`
- **Upstream:** none (lookup table)
- **Downstream (formal FK):**
  - `mti_term_flags.flag_id`
  - `wa_term_phase2_flags.flag_id`

---

### `wa_term_phase2_flags`
- **Upstream (formal FK):**
  - `wa_term_inventory.id` via `term_inv_id`
  - `phase2_flag_types.id` via `flag_id`
- **Downstream:** none (junction table)
- **Purpose:** many-to-many between WA terms and Phase-2 flag types

---

### `wa_quality_flag_types`
- **Upstream:** none (lookup table)
- **Downstream (formal FK):**
  - `wa_data_quality_flags.flag_id`

---

### `wa_data_quality_flags`
- **Upstream (formal FK):**
  - `wa_file_index.id` via `file_id`
  - `wa_quality_flag_types.id` via `flag_id`
- **Upstream (soft):**
  - `wa_term_inventory.term_id` via `term_id` (TEXT match, 53 orphans / 1.6%)
- **Downstream:** none
- **Gap:** `term_id` (TEXT) provides term-level context but no FK to `wa_term_inventory`; quality flags are scoped to file+term_id but not to a specific inventory row.

---

### `wa_crosslink_type`
- **Upstream:** none (lookup table)
- **Downstream (formal FK):**
  - `wa_cross_registry_links.connection_type_id`

---

### `wa_cross_registry_links`
- **Upstream (formal FK):**
  - `wa_file_index.id` via `file_id`
  - `word_registry.id` via `linked_registry_id` (nullable)
  - `wa_crosslink_type.id` via `connection_type_id`
- **Downstream:** none
- **Note:** 7 rows have `linked_registry_id = NULL` where the linked word name was composite or could not be resolved to a registry entry.

---

### `wa_verse_records`
- **Upstream (formal FK):**
  - `books.id` via `book_id`
- **Upstream (intended, unregistered FK):**
  - `wa_file_index.id` via `file_id`
  - `wa_term_inventory.id` via `term_inv_id`
- **Upstream (soft TEXT match):**
  - `wa_term_inventory.term_id` via `term_id` (1 orphan out of 57,130)
- **Downstream:** none (leaf table — core research data)

---

### `mti_terms`
- **Upstream (formal FK, added 3.2.0):**
  - `word_registry.id` via `owning_registry_fk` (INTEGER)
  - `wa_file_index.id` via `word_data_ref_fk` (INTEGER)
- **Upstream (soft, retained):**
  - `word_registry.id` via `owning_registry` (TEXT, zero-padding fixed in Fix 2 — 0 orphans)
  - `wa_file_index.id` via `word_data_reference` (TEXT, values valid — 0 orphans)
- **Downstream (formal FK):**
  - `mti_term_cross_refs.mti_term_id`
  - `mti_term_flags.mti_term_id`

---

### `mti_term_flags`
- **Upstream (formal FK):**
  - `mti_terms.id` via `mti_term_id`
  - `phase2_flag_types.id` via `flag_id`
- **Downstream:** none (junction table)
- **Purpose:** many-to-many between MTI terms and Phase-2 flag types (shares the same `phase2_flag_types` lookup as `wa_term_phase2_flags`)

---

### `mti_term_cross_refs`
- **Upstream (formal FK):**
  - `mti_terms.id` via `mti_term_id`
  - `word_registry.id` via `registry_fk` (INTEGER, added 3.2.0)
- **Upstream (soft, retained):**
  - `word_registry.id` via `registry` (TEXT, zero-padding fixed in Fix 2 — 0 orphans)
  - `wa_file_index.id` via `word_data_reference` (TEXT, values valid — 0 orphans)
- **Downstream:** none

---

### `engine_run_log`
- **Upstream:** none (root engine table)
- **Downstream (formal FK):**
  - `engine_stream_checkpoint.run_id`
  - `term_fetch_log.run_id`
  - `word_run_state.run_id`
- **Downstream (soft):**
  - `word_registry.automation_run_id` (back-reference from registry to last run)

---

### `engine_stream_checkpoint`
- **Upstream (formal FK):** `engine_run_log.run_id` via `run_id`
- **Downstream:** none
- **Note:** Only 7 rows exist vs 36 runs. Most runs have no checkpoint records.

---

### `word_run_state`
- **Upstream (formal FK):** `engine_run_log.run_id` via `run_id`
- **Upstream (soft):** `word_registry.id` via `registry_id` (TEXT, 44.1% zero-padding orphans)
- **Downstream:** none

---

### `term_fetch_log`
- **Upstream (formal FK):** `engine_run_log.run_id` via `run_id`
- **Upstream (soft):** `word_registry.id` via `registry_id` (TEXT, 0% orphans — no zero-padding issue)
- **Downstream:** none

---

### `wa_meaning_parsed`
- **Upstream (formal FK):** `wa_term_inventory.id` via `term_inv_id` (UNIQUE — 1:1)
- **Downstream (formal FK):**
  - `wa_meaning_sense.parsed_meaning_id`
  - `wa_meaning_stem.parsed_meaning_id`
- **Note:** Bidirectional soft loop — `wa_term_inventory.parsed_meaning_id` points back here. The authoritative direction is this table's `term_inv_id` FK.

---

### `wa_meaning_sense`
- **Upstream (formal FK):** `wa_meaning_parsed.id` via `parsed_meaning_id`
- **Downstream:** none (hierarchical leaf — sense entries reference each other via `parent_level_code` TEXT, not FK)

---

### `wa_meaning_stem`
- **Upstream (formal FK):** `wa_meaning_parsed.id` via `parsed_meaning_id`
- **Downstream:** none

---

### `wa_lsj_parsed`
- **Upstream (formal FK):** `wa_term_inventory.id` via `term_inv_id` (UNIQUE — 1:1, Greek only)
- **Downstream:** none

---

### `schema_version`
- **Upstream:** none
- **Downstream:** none
- **Purpose:** Single-row metadata table (id=1). No relational links.

---

## 8. Critical Issue: FK Enforcement is OFF

```
PRAGMA foreign_keys = 0   ← confirmed on live DB connection
```

SQLite does not enforce foreign key constraints unless `PRAGMA foreign_keys = ON` is explicitly set per connection. Checking the codebase:

- `data/schema/create_tables.sql` includes `PRAGMA foreign_keys = ON` at the top — but this only applies during schema initialisation, not to runtime connections.
- `analytics/db_client.py` `get_connection()` sets WAL, row_factory, and busy_timeout — but does **not** set `PRAGMA foreign_keys = ON`.
- `engine/db.py` `get_connection()` calls `db_client.get_connection()` and adds `busy_timeout` — but does **not** set `PRAGMA foreign_keys = ON`.

**Result:** All 19 registered FK constraints are architecturally defined but completely unenforced at runtime. Any insert or update that violates a FK will silently succeed.

---

## 9. Orphan Analysis

### 9.1 Zero-padding Orphans (Not True Orphans — Formatting Mismatch)

The following tables store registry IDs as zero-padded 3-digit strings, cause apparent orphan counts when compared to `word_registry.id` (INTEGER):

| Table.Column | Stored Format | word_registry.id Format | Orphan Rows | Distinct Orphan IDs |
|---|---|---|---|---|
| `wa_file_index.registry_id` | `'001'`, `'071'` etc. | `1`, `71` etc. | 17 | 17 |
| `mti_terms.owning_registry` | `'001'`, `'071'` etc. | same | 371 rows | 16 IDs |
| `mti_term_cross_refs.registry` | `'007'`, `'071'` etc. | same | 28 rows | 5 IDs |
| `word_run_state.registry_id` | `'008'`, `'009'` etc. | same | 82 rows | 82 (nearly all) |

The affected registry IDs (from the wa_file_index/mti sets) are: 001, 002, 003, 004, 005, 006, 007, 026, 043, 051, 056, 061, 071, 073, 078, 080, 097. These correspond to the earliest words imported (Session A data), suggesting the zero-padding was introduced early and later corrected.

**For `word_run_state.registry_id`:** 82 of 188 rows are affected (44.1%) — virtually all zero-padded. This column appears to have been consistently populated with zero-padded values throughout, unlike `term_fetch_log.registry_id` which has 0% orphan rate.

### 9.2 True Orphans (Content / Referential Issues)

| Table.Column | Orphan Count | Notes |
|---|---|---|
| `wa_data_quality_flags.term_id` | 53 rows (1.6%) | Flags referencing Strong's codes not in `wa_term_inventory.term_id`. Includes legacy codes (e.g. G5545B), non-standard suffixed codes (G3949_related), and placeholder codes (NO STRONG-043-epithumetos, etc.) |
| `wa_verse_records.term_id` | 1 row (0.0%) | Single verse record with a term_id not in the inventory — negligible. |
| `wa_cross_registry_links.linked_registry_id` | 7 NULLs | Intentional NULLs where link was unresolvable. Not orphans — nullable by design. |

### 9.3 Unresolvable Cross-Links (by Design)

`wa_cross_registry_links.linked_registry_id` is nullable. 7 rows have `NULL`, documented in the schema as "composite or unresolvable names". These are expected and not errors.

---

## 10. Empty / Underutilised Tables

| Table | Rows | Status |
|---|---|---|
| `themes` | 0 | Defined but never populated. No downstream relationships exist. |
| `sources` | 0 | Defined but never populated. No downstream relationships exist. |
| `engine_stream_checkpoint` | 7 | Sparsely populated: only 7 rows across 36 engine runs. Most runs have no checkpoint records. |
| `mti_term_flags` | 9 | Very few MTI terms have Phase-2 flags (9 flag assignments across 1,380 MTI terms). |

---

## 11. Summary of Gaps and Issues

### 11.1 Structural Gaps

| # | Gap | Severity | Tables Affected |
|---|---|---|---|
| G1 | **FK enforcement is OFF** — `PRAGMA foreign_keys` is never set ON at connection time. All 19 registered FKs and all intended-but-unregistered FKs are unenforced. | Critical | All tables |
| G2 | **6 FK constraints defined in schema SQL are not registered in live DB** — columns that have REFERENCES in `create_tables.sql` but are absent from `PRAGMA foreign_key_list` because the tables were created before those FKs were added. | High | `wa_file_index.word_registry_fk`, `wa_term_inventory.file_id`, `wa_term_related_words.term_inv_id`, `wa_term_root_family.term_inv_id`, `wa_verse_records.file_id`, `wa_verse_records.term_inv_id` |
| G3 | **Dual-column registry reference in `wa_file_index`** — both `registry_id` (TEXT) and `word_registry_fk` (INTEGER) serve as references to `word_registry`. The TEXT column has formatting issues; the INTEGER column is clean but its FK is unregistered. Only one authoritative column should exist per relationship. | Medium | `wa_file_index` |
| G4 | **`wa_data_quality_flags.term_id` has no FK to `wa_term_inventory`** — quality flags are scoped to file + term_id (TEXT), not to a specific inventory row (`wa_term_inventory.id`). This means flags cannot be reliably joined to term records where the term_id format has changed. | Medium | `wa_data_quality_flags` |
| G5 | **`wa_meaning_sense.parent_level_code`** references another sense entry within the same table by text code, not by row id. Hierarchical self-reference is via TEXT labels only. | Low | `wa_meaning_sense` |
| G6 | **`mti_terms.word_data_reference` and `mti_term_cross_refs.word_data_reference`** — labelled "future FK" in schema comments. Values exist and are valid but the FK was never formalised. | Low | `mti_terms`, `mti_term_cross_refs` |
| G7 | **`wa_term_inventory.parsed_meaning_id`** is a soft back-pointer to `wa_meaning_parsed.id` with no FK constraint, creating a bidirectional soft loop. The authoritative direction is `wa_meaning_parsed.term_inv_id` FK. | Low | `wa_term_inventory`, `wa_meaning_parsed` |

### 11.2 Data Quality Gaps

| # | Gap | Severity | Tables Affected |
|---|---|---|---|
| D1 | **Zero-padded registry ID formatting** in `word_run_state.registry_id` (44.1% of rows), `mti_terms.owning_registry` (371 rows), `mti_term_cross_refs.registry` (28 rows), `wa_file_index.registry_id` (17 rows). These are not true referential orphans but are functionally unusable in string-based joins. | High | `word_run_state`, `mti_terms`, `mti_term_cross_refs`, `wa_file_index` |
| D2 | **53 quality flags reference term_ids not in `wa_term_inventory`** — includes legacy Strong's codes, non-standard suffixes, and placeholder "NO STRONG-…" codes. These flags cannot be joined to term inventory records. | Medium | `wa_data_quality_flags` |
| D3 | **`engine_stream_checkpoint` sparsely populated** — only 7 rows across 36 engine runs. Most runs have no checkpoint tracking. | Low | `engine_stream_checkpoint` |
| D4 | **`themes` and `sources` tables are empty** — no data, no downstream joins. | Low | `themes`, `sources` |

### 11.3 Missing Downstream Coverage

The following parent tables have **no enforced downstream orphan protection**:

- `word_registry` — the central registry table has no cascade delete; words can be removed while leaving orphan rows in `wa_file_index`, `mti_terms`, `wa_cross_registry_links`, etc.
- `wa_file_index` — removing a file index row would leave orphan rows in `wa_term_inventory` and `wa_verse_records` (those FKs are unregistered and unenforced).
- `wa_term_inventory` — removing a term would leave orphan rows in `wa_term_related_words`, `wa_term_root_family`, and `wa_verse_records` (all FKs unregistered).

---

*End of report.*
