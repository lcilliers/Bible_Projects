"""add_cfg_table_inactive_column.py — ONE-OFF: `cfg_table` gains an `inactive` column
(escalation #678, researcher's full bible_research.db table review, 2026-08-17).

`bootstrap_inactive_column.py` (escalation #310, earlier) deliberately EXCLUDED `cfg_table`/
`cfg_column`/`cfg_unique` — at the time, these were judged to "describe the SCHEMA of other tables,
not a toggleable config item themselves." `governance.tables` was written after that (or not
reconciled with it): "each table in the project must be listed in cfg_table with a proper use
text... tables no longer in use must be set as inactive" — a direct requirement the schema has
never actually supported. Confirmed live, not assumed: `PRAGMA table_info(cfg_table)` before this
migration has no `inactive` column at all.

The researcher's #678 escalation ("which of the 110 bible_research.db tables are superseded vs.
genuinely still canonical") produced a full per-table review (`iba/app/reports/cfg_tables for
review 2026-08-17.csv`) with an explicit active/inactive verdict per row — work that has nowhere to
land without this column. This migration reverses #310's exclusion for `cfg_table` specifically
(not `cfg_column`/`cfg_unique`, which remain schema-of-schema with no comparable value-review
driving a need for it yet); same physical-ALTER + cfg_column-self-document pattern as #310's own
bootstrap.

    python -m iba.app.migration.add_cfg_table_inactive_column
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    cols = {r[1] for r in conn.execute('PRAGMA table_info("cfg_table")')}
    if "inactive" not in cols:
        conn.execute('ALTER TABLE "cfg_table" ADD COLUMN inactive INTEGER NOT NULL DEFAULT 0')
        report.append("cfg_table.inactive column added (physical ALTER)")
    else:
        report.append("cfg_table.inactive already present")

    if not conn.execute(
            "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='cfg_table' "
            "AND name='inactive'").fetchone():
        ordinal = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column "
            "WHERE database='iba' AND table_name='cfg_table'").fetchone()[0]
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, "type", is_pk, '
            '"notnull", is_unique, dflt, fk, "use", expectation, source, filled_by) '
            "VALUES ('iba','cfg_table','inactive',?,'INTEGER',0,1,0,'0',NULL,?,NULL,NULL,"
            "'migration/add_cfg_table_inactive_column.py')",
            (ordinal,
             "a data table no longer in use (superseded, retired, or abandoned scaffolding) is "
             "marked inactive=1 here rather than deleted from cfg_table — governance.tables' own "
             "requirement, unsupported by schema until escalation #678's full table review made "
             "the gap concrete. Reverses bootstrap_inactive_column.py's (#310) earlier exclusion "
             "of cfg_table as 'schema-of-schema, not toggleable' — cfg_column/cfg_unique remain "
             "excluded, no comparable review driving a need for it there yet."))
        report.append("cfg_column row for cfg_table.inactive added")
    else:
        report.append("cfg_column row for cfg_table.inactive already present")

    conn.commit()
    conn.close()

    print("cfg_table.inactive bootstrap (escalation #678):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
