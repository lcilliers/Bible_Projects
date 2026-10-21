"""fix_compound_pk_registration_v1_20260818.py — ONE-OFF, idempotent. Escalations #721 (iba.db,
12 tables) + #722 (bible_research.db, 7 tables), both researcher-approved 2026-08-18 ("as per
plan" — iba/app/reports/cfg-pk-registration-and-validator-scoping-plan-20260818.md).

Root cause: `lib/db.py`'s `_col_ddl()` emits an inline column-level `PRIMARY KEY` for every
`is_pk=1` column — SQLite allows only one such inline declaration per table, so truthfully marking
every column of a compound physical key `is_pk=1` produces invalid DDL the moment `CREATE TABLE`
(not `IF NOT EXISTS`-guarded, e.g. a fresh rebuild) actually runs. `Db.upsert()`'s dedup key
(`Cfg.unique_key()`) falls back to `is_pk=1` columns only when `cfg_unique` has no row for the
table — so the fix is not just "set is_pk=0", it's "set is_pk=0 AND add the cfg_unique row that
keeps `unique_key()` resolving correctly." `cfg_index` (registered 2026-08-07) already had the
`is_pk=0` half of this but never got the `cfg_unique` half — included here so all 19 tables (12 +
7, `cfg_index` counted once) end up in the SAME complete, consistent state, not 18 fixed properly
and one left half-done.

    python -m iba.app.migration.fix_compound_pk_registration_v1_20260818
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

# (database, table_name, [pk columns in true key order])
_TABLES = [
    ("iba", "cfg_unique", ["database", "table_name", "col"]),
    ("iba", "cfg_write_grant", ["writer", "table_name", "database"]),
    ("iba", "cfg_table", ["database", "name"]),
    ("iba", "cfg_column", ["database", "table_name", "name"]),
    ("iba", "cfg_step", ["work_package", "step"]),
    ("iba", "cfg_enum", ["name", "value"]),
    ("iba", "cfg_candidate_rule", ["kind", "value"]),
    ("iba", "cfg_on_fail", ["step", "condition"]),
    ("iba", "cfg_status_flow", ["entity", "status"]),
    ("iba", "cfg_report_section", ["step", "section_key"]),
    ("iba", "cfg_report_csv_table", ["step", "table_name"]),
    ("iba", "cfg_index", ["table_name", "name", "col"]),
    ("bible_research", "prose_section_dimension_link",
     ["prose_section_id", "dimension_id", "link_type"]),
    ("bible_research", "prose_section_finding_link",
     ["prose_section_id", "finding_id", "link_type"]),
    ("bible_research", "mti_term_flags", ["mti_term_id", "flag_id"]),
    ("bible_research", "prose_section_fts_idx", ["segid", "term"]),
    ("bible_research", "segment_unit_verse", ["unit_id", "verse_id"]),
    ("bible_research", "ve_verification_sample", ["ve_nr", "verse_span_id"]),
    ("bible_research", "wa_term_phase2_flags", ["term_inv_id", "flag_id"]),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for database, table, pk_cols in _TABLES:
        n = conn.execute(
            "UPDATE cfg_column SET is_pk=0 WHERE database=? AND table_name=? AND is_pk=1",
            (database, table)).rowcount
        report.append(f"{database}.{table}: is_pk cleared on {n} column(s)")

        for ordinal, col in enumerate(pk_cols):
            if not conn.execute(
                    "SELECT 1 FROM cfg_unique WHERE database=? AND table_name=? AND col=?",
                    (database, table, col)).fetchone():
                conn.execute(
                    "INSERT INTO cfg_unique (database, table_name, col, ordinal) "
                    "VALUES (?,?,?,?)", (database, table, col, ordinal))
                report.append(f"  cfg_unique ({database}.{table}.{col}) added")
            else:
                report.append(f"  cfg_unique ({database}.{table}.{col}) already present")

    conn.commit()
    conn.close()

    print(f"compound-PK registration fix ({len(_TABLES)} tables, escalations #721/#722):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
