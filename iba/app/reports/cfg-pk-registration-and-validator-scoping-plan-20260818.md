# cfg_column `is_pk` registration + validator database-scoping — three focus areas (parked)

**Raised:** 2026-08-18, investigating `#712` part 2 / escalation `#719`'s fallout. Researcher
instruction: several distinct focus areas surfaced — raise them as separate escalations rather
than fixing inline. This document is the shared evidence record; each escalation below points back
to it (`cfg_escalation.document_reference_grouping`).

## How this was found

Backfilling `cfg_table`/`cfg_column` for the 20 foundational `iba.db` tables (`#712` part 1) and
switching `CFG_TABLES` to derive from `cfg_table` (`#712` part 2) made `configmaint.validate` check
11 tables it had never seen before. It hard-failed: `pk_n > 1` — those 11 tables genuinely have a
compound physical `PRIMARY KEY`, registered truthfully.

That's not a false positive. Checked `lib/db.py` directly: `is_pk` is live-consumed twice —
`_col_ddl()` emits an inline column-level `PRIMARY KEY` for every `is_pk=1` column (SQLite allows
only one such inline declaration per table — multiple would crash `CREATE TABLE` the moment a
table needed rebuilding from scratch), and `Db.upsert()`'s dedup key falls back to `is_pk=1`
columns when no `cfg_unique`/`is_unique` rows exist. So truthfully marking every real PK column
`is_pk=1` on a compound-key table is itself a latent bug, not a documentation nicety — the
established (if incomplete) precedent is `is_pk=0` on all such columns, with the real key
documented via `cfg_unique` instead (`unique_key()`'s first-tier source).

Widening the search past `iba.db` (researcher's direct challenge, since `bible_research.db`
definitely has compound-key junction tables) found the same pattern there too, at zero risk of
`_validate_live` ever catching it: the check is hardcoded to `database='iba'` throughout, so
`bible_research.db`'s own registration quality has no coherence check of any kind.

## Focus area A — `iba.db`: 12 tables need `is_pk`/`cfg_unique` correction (real, live risk)

`cfg_write_grant`, `cfg_table`, `cfg_column`, `cfg_step`, `cfg_enum`, `cfg_candidate_rule`,
`cfg_on_fail`, `cfg_report_csv_table`, `cfg_report_section`, `cfg_status_flow`, `cfg_unique` (all
registered this session, `#712` part 1) plus `cfg_index` (registered 2026-08-07, already
`is_pk=0`-everywhere but with **zero** `cfg_unique` backing rows — an incomplete prior fix, not a
correct one). `Db.build()`/`Db.upsert()` genuinely operate on these — this is the one area with
present-day functional exposure (latent: `CREATE TABLE IF NOT EXISTS` no-ops against the live
tables today, so nothing has broken yet; it would break on any fresh rebuild).

**Fix:** `is_pk=0` on all key columns of these 12 tables; add `cfg_unique` rows (correct PK column
order) for each so `unique_key()` still resolves the real dedup key. `cfg_index` gets its
first-ever `cfg_unique` backing as part of the same pass.

## Focus area B — `bible_research.db`: 7 tables have the identical pattern (metadata-quality, not live-functional today)

`prose_section_dimension_link`, `prose_section_finding_link`, `mti_term_flags`,
`prose_section_fts_idx`, `segment_unit_verse`, `ve_verification_sample`, `wa_term_phase2_flags` —
all `is_pk=1` on 2-3 columns, zero `cfg_unique` rows, found via the same scan run against
`database='bible_research'`. Checked whether this matters today: `lib/cfg.py`'s `Cfg.tables()`/
`.columns()` are hardcoded `WHERE database='iba'` — `Db`/`Cfg` never touch `bible_research.db` at
all (still governed by the legacy `engine/` pipeline, which predates and doesn't read `iba.db`'s
`cfg_*` tables). So this is a real metadata inaccuracy, not a live bug — but the same latent shape,
and it would bite the same way if/when `bible_research.db` tables ever move under this dispatcher
(the stated long-term direction of the governance-alignment consolidation work).

**Fix:** same pattern as A, applied to these 7 rows under `database='bible_research'`.

## Focus area C — the validator itself is not config-driven (the deeper, root gap)

`handlers/configmaint.py`'s `_validate_live` hardcodes the literal string `'iba'` in at least 6
places (table/column/write-grant queries); my own new `_known_cfg_tables` (`#712` part 2, this
session) copied the exact same pattern. Checked what SHOULD drive this instead of a literal:

- `cfg_meta.database='iba'` — a single fact ("which DB this store is"), not a list of databases.
- No `cfg_enum` group names the project's databases at all.
- `governance.project_databases` — prose text, not structured/queryable.
- `SELECT DISTINCT database FROM cfg_table` — the only live structured signal (`bible_research`,
  `iba`), currently read by nothing.

This is the root cause of focus area B being invisible, not a coincidence: the checker was scoped
to one hardcoded database, deliberately (escalation `#653`'s comment: avoiding cross-database
table-name collisions), but that scoping choice also silently dropped `bible_research.db`'s own
coherence checking entirely, with nothing flagging the gap.

**Fix, two parts, for researcher decision:**
1. A proper structured "known databases" registry — most likely a `cfg_enum` group (e.g.
   `project_database`) seeded from the two live `cfg_table.database` values, so it's queryable by
   name the way every other enum is, replacing `governance.project_databases`'s prose-only role for
   this specific purpose (that setting can still stand for human-readable orientation).
2. `_validate_live` (and `_known_cfg_tables`) rewritten to iterate over the registered databases
   generically instead of hardcoding `'iba'` — collision-safe per-database, but no longer blind to
   `bible_research.db`. This closes focus area B's detection gap structurally, rather than needing
   a hand-maintained twin check.

## Not done

No `is_pk`/`cfg_unique` writes for A or B. No changes to `_validate_live`/`_known_cfg_tables` for
C. `configmaint.validate` remains hard-failing (exit 3) until A is resolved — `configmaint.propose`
is unaffected (independent code path, confirmed), so other work isn't blocked by this.
