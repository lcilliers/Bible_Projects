"""add_debate_change_detail_writer_column_20260808.py — ONE-OFF, idempotent: adds
`debate_change_detail.writer` (which step made this change — `hib.set` | `passage.build` |
`phenomenon.set` | `operation.set` | `closing.set`).

**Why.** `run_id` is shared across a WHOLE `Debate-Run.ps1` sequence (one run_id reused for every
step it walks), so it alone can't identify which step made a given row. `table_name` happens to be
1:1 with a writer today, but that's incidental, not a documented guarantee — an explicit `writer`
column is the direct, robust fact, not one the reader has to infer from a table-name mapping.

**Why a direct migration, not `configmaint.propose`.** Adding a column is DDL (same carve-out class
as `migration/bootstrap_inactive_column.py` — `configmaint.propose` can only write rows on
already-existing columns, not add one).

    python -m iba.app.migration.add_debate_change_detail_writer_column_20260808
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

TABLE = "debate_change_detail"


def _column_exists(conn: sqlite3.Connection, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f"PRAGMA table_info({table})").fetchall())


def run(conn: sqlite3.Connection) -> list[str]:
    report: list[str] = []

    if _column_exists(conn, TABLE, "writer"):
        report.append(f"{TABLE}.writer already present")
    else:
        conn.execute(f'ALTER TABLE {TABLE} ADD COLUMN writer TEXT NOT NULL DEFAULT ""')
        # Backfill: every existing row predates this column and was written by hib.set (the only
        # writer live before this session's broader CRUD pass).
        n = conn.execute(f"UPDATE {TABLE} SET writer='hib.set' WHERE writer=''").rowcount
        report.append(f"{TABLE}.writer added, {n} pre-existing row(s) backfilled 'hib.set'")

    if conn.execute(
            "SELECT 1 FROM cfg_column WHERE table_name=? AND name='writer'", (TABLE,)).fetchone():
        report.append("cfg_column row for writer already present")
    else:
        max_ord = conn.execute(
            "SELECT COALESCE(MAX(ordinal),0) FROM cfg_column WHERE table_name=?", (TABLE,)
        ).fetchone()[0]
        conn.execute(
            'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", is_unique, '
            "dflt, fk, use, expectation, source, filled_by) VALUES "
            f"('{TABLE}','writer',{max_ord + 1},'TEXT',0,1,0,NULL,NULL,"
            "'which step made this change -- ''hib.set'' | ''passage.build'' | ''phenomenon.set'' "
            "| ''operation.set'' | ''closing.set''',NULL,NULL,"
            "'migration/add_debate_change_detail_writer_column_20260808.py')")
        report.append("cfg_column row for writer added")

    conn.commit()
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report = run(conn)
    conn.close()
    print(f"{TABLE}.writer column:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
