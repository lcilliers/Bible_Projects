# Directive DIR-20260421-002 — Relax `prose_section.registry_id` NOT NULL

> Produced by: wa-directive-instruction-v1_2-20260421 §10 (schema enablement pattern)
> Governed by: wa-global-general-rules [current]
> Registry: global (programme-level schema change)
> Produced date: 2026-04-21
> Researcher approval: PENDING
> Session reference: prose
> Filename: wa-global-dir-002-prose-registry-nullable-v1-20260421.md

---

## Motivation

The `prose_section` table is declared with `registry_id INTEGER NOT NULL REFERENCES word_registry(id)`. This was correct when `prose_section` held only registry-scoped content (Session A/B/C/D per-word prose). Migration M34 (2026-04-19) seeded eight `prose_section_type` rows with `source_stage = 'programme'` to support programme-wide prose — content that describes the programme as a whole and has no registry. A further nine `prose_section_type` rows for programme-wide content have been prepared in session `prose` (2026-04-21) and are ready to receive prose bodies.

Any `INSERT` on `prose_section` for a programme-wide row fails: `registry_id = NULL` fails the NOT NULL constraint; `registry_id = 0` or any placeholder value fails the FK because no such row exists in `word_registry` (and reserving one would be a category error — programme-wide prose has no registry, not a sentinel registry).

The remedy is to relax the NOT NULL constraint on `prose_section.registry_id` so that `registry_id IS NULL` signals programme-wide scope. This matches the existing convention at type level where `prose_section_type.source_stage = 'programme'` already signals programme-wide scope without requiring a registry.

This directive follows the pattern established by wa-directive-instruction-v1_2-20260421 §10.2 (worked example: programme-wide prose) and §10.3 (SQLite DDL approach: CREATE-copy-RENAME + FTS rebuild).

---

## Scope

**Table:** `prose_section`.

**Column:** `registry_id`.

**Change:** Drop `NOT NULL` on `registry_id`. Retain FK `REFERENCES word_registry(id)`. No other columns, constraints, or indexes changed.

**Companion tables:**
- `prose_section_fts` (FTS5 virtual table) — must be rebuilt because it is keyed to `prose_section.rowid`.
- `prose_section_fts_config`, `prose_section_fts_content`, `prose_section_fts_data`, `prose_section_fts_docsize`, `prose_section_fts_idx` — shadow tables of the FTS5 virtual table; rebuilt as part of the FTS rebuild.

**Rows affected:** zero rows in `prose_section` at directive time (table is empty; confirmed by `section_count = 0` across all programme-stage types in the latest extract). The DDL applies to schema only.

**Indexes to preserve:** `idx_ps_supersedes`, `idx_ps_status`, `idx_ps_registry_type_current` (recreated against the new table as part of the rebuild).

**CHECK constraints to preserve:** `status IN ('draft','in_review','approved','archived')` and `author IN ('claude_ai','claude_code','researcher')`.

**Other FKs to preserve:** `supersedes_id REFERENCES prose_section(id)`, `superseded_by_id REFERENCES prose_section(id)`, `section_type_id REFERENCES prose_section_type(id)`.

---

## Outcome required

After execution, the following conditions must all be true:

1. `prose_section.registry_id` is nullable INTEGER.
2. FK `REFERENCES word_registry(id)` on `registry_id` is retained.
3. All other columns on `prose_section` are preserved: `id`, `section_type_id`, `heading`, `body`, `word_count`, `status`, `version`, `supersedes_id`, `superseded_by_id`, `author`, `created_at`, `approved_at`, `approved_by`, `metadata_json`, `source_file`, `delete_flagged` — types, NOT NULL status, defaults, and FKs as per schema v3.14.0.
4. Both CHECK constraints on `prose_section` are preserved (status; author).
5. The three indexes (`idx_ps_supersedes`, `idx_ps_status`, `idx_ps_registry_type_current`) are present on the rebuilt table.
6. `prose_section_fts` and its shadow tables exist and are populated from `prose_section` (which has zero rows; the rebuild is a structural operation).
7. `prose_section` row count unchanged (zero before, zero after).
8. A subsequent `INSERT INTO prose_section (registry_id, section_type_id, heading, body, word_count, status, version, author, created_at) VALUES (NULL, 27, 'Test', 'Test body', 2, 'draft', 1, 'claude_code', datetime('now'))` succeeds. (This test insert is **optional** — if CC runs it, the test row must be rolled back immediately; the outcome check below does not require this test to have been performed, but a test insert + immediate rollback is recommended as a final verification before the directive is closed.)

Per wa-directive-instruction-v1_2 §10.3, the expected DDL path is CREATE-copy-RENAME: create `prose_section_new` with the relaxed constraint, copy data (0 rows), drop the old table, rename, rebuild FTS. CC decides the execution path; this directive specifies the outcome.

---

## Completion confirmation

CC must return the results of the following three queries, verbatim:

**Query 1 — Column nullability:**
```sql
PRAGMA table_info(prose_section);
```
Expected: the row for `registry_id` shows `notnull = 0`. All other `notnull` values should match schema v3.14.0 (e.g. `section_type_id` and `body` remain `notnull = 1`).

**Query 2 — DDL integrity:**
```sql
SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'prose_section';
```
Expected: the CREATE TABLE statement shows `registry_id INTEGER REFERENCES word_registry(id)` (no NOT NULL) and all other columns, constraints, and FKs as per schema v3.14.0.

**Query 3 — FTS companion:**
```sql
SELECT name FROM sqlite_master WHERE name IN ('prose_section_fts', 'prose_section_fts_config', 'prose_section_fts_content', 'prose_section_fts_data', 'prose_section_fts_docsize', 'prose_section_fts_idx');
```
Expected: all six names returned.

**Query 4 (optional) — Test insert:**
```sql
BEGIN TRANSACTION;
INSERT INTO prose_section (registry_id, section_type_id, heading, body, word_count, status, version, author, created_at) VALUES (NULL, 27, 'Test', 'Test body', 2, 'draft', 1, 'claude_code', datetime('now'));
SELECT 'insert succeeded' AS result;
ROLLBACK;
```
Expected: `insert succeeded`. Optional because Queries 1 and 2 are sufficient to confirm the constraint change; the test insert is belt-and-braces for the researcher.

---

## Notes

- **Dependency chain.** After this directive completes and is confirmed, the CATALOGUE_POPULATION patch (`wa-prose-catalogue-chapter0-1-v1-20260421.json`) and the PROSE patch (`wa-prose-programme-chapter0-1-v1-20260421.json`) can apply. If the directive fails or is not confirmed, those patches must not be submitted.

- **Reversibility.** A per-directive DB backup at `backups/bible_research_backup_{timestamp}_DIR-20260421-002.db` is expected before the CREATE-copy-RENAME sequence begins. If the directive fails mid-execution, restore from that backup via a subsequent directive per wa-patch-instruction [current] §13.7.

- **Self-check per wa-directive-instruction-v1_2 §7.**
  - DIRECTIVE ID: present — `DIR-20260421-002`. ✓
  - MOTIVATION: specific, with evidence. ✓
  - SCOPE: table, column, companions, rows affected named. ✓
  - OUTCOME REQUIRED: eight specific conditions, verifiable. ✓
  - COMPLETION CONFIRMATION: three required queries plus one optional, expected results stated. ✓
  - Filename check: `wa-global-dir-002-prose-registry-nullable-v1-20260421.md` — lowercase, compact date, within 20-char description limit (`prose-registry-nullable` is 22 chars — **fails** the §2.1 limit).

### Filename correction

Description `prose-registry-nullable` exceeds the 20-character limit in §2.1. Shortened to `prose-reg-nullable` (18 chars). Final filename:

`wa-global-dir-002-prose-reg-nullable-v1-20260421.md`

Self-check after correction: PASS on all five elements plus filename.

---

*DIR-20260421-002 | Schema enablement directive — relax prose_section.registry_id NOT NULL | PENDING researcher approval*
