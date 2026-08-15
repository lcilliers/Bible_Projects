# Prose Edit — Programme — Chapter 5

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 35 -->
<!-- PROSE_SECTION_TYPE: prog_backup_discipline -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 5 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Backup and schema migration discipline -->
<!-- PROSE_SORT_ORDER: 107 -->
<!-- PROSE_VERSION: 1 -->
<!-- PROSE_SOURCE_FILE: wa-prose_ch5-obslog-v1_0-20260423.md -->

## Backup and schema migration discipline

The programme's database is a single SQLite file. Its integrity under change — under patches that modify rows, under directives that modify schema — depends on a backup discipline that makes change reversible and a migration discipline that makes change traceable. Both are governance principles; both apply uniformly to every change the operational agent applies.

**Backup discipline.** The governing principle is that every state-changing operation against the database is recoverable. A patch that writes rows, a directive that alters schema, a bulk operation that adjusts many rows at once — each is applied against a database state that can be restored if the operation is found wrong. The backup is taken before the operation; the backup's retention outlasts the window in which error-detection is reasonable; the restoration procedure brings a known backup back as the working database. Because the programme's research record is cumulative and the operational agent applies changes over long sequences, a backup discipline that treats every material change as reversible is the difference between a database whose state can be trusted at any point and one whose current state carries unexamined risk from any upstream operation.

**Schema migration discipline.** The database's schema is versioned. The `schema_version` table carries a `version_code`, an `applied_at` timestamp, a `migration_history` record, and an `engine_min_version` field that the pipeline uses to refuse to run against an incompatible schema. Migrations are identified by M-numbers and are authored as directives through the operational agent — the channel for structural operations that fall outside the patch format, as described in the sub-section on the two-AI division.

The principle is that every schema change is a migration: it is authored, reviewed, applied through the directive mechanism, and recorded in `schema_version` as a new row. An ad-hoc schema change — one that does not pass through the directive channel — is a breach of the discipline. The audit trail of the schema's evolution lives in the migration history; the history is what makes it possible, at any later point, to understand the schema state the database was in when a given patch or analytical pass ran.

Backup and migration are paired disciplines. A migration without a backup leaves its change un-reversible; a backup without a migration record leaves its relation to the schema obscure. The two together make the database's evolution auditable — what changed, when, under what directive, with what rollback point available. Where one is present and the other is not, the discipline is incomplete.

---
