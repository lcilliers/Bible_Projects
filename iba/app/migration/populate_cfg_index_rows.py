"""populate_cfg_index_rows.py — idempotent, RE-RUNNABLE (unlike most migrations here, this one is
meant to be run again every time a table gains a new FK column): syncs `cfg_index` to match the
FK columns `cfg_column` currently declares, app-wide (`schema-remediation-design-20260807.md` §1).

**Rule applied, uniformly, not special-cased per table:** every FK column on every real data table
(`cfg_table` — excludes the `cfg_*` config tables themselves, which aren't built by
`build_data_tables()` and aren't this project's concern) gets an index. Where the table also carries
a `deleted` column (the app's universal soft-delete convention — true for every data table checked),
the index is COMPOSITE `(fk_col, deleted)`, not just `(fk_col)` — every live query in this app's
handlers filters `WHERE {fk_col}=? AND deleted=0` in the same breath (confirmed by direct reading of
`handlers/operations.py`/`passage.py`), so a composite index serves the actual query shape directly
rather than making SQLite intersect two single-column indexes.

Run again after: `fix_cfg_column_fk_gaps.py` (already done, operation_party.hib_id +
strong_meaning_parsed/tree.strong_variant now covered), or any future migration that adds a new FK
column anywhere in the app.

    python -m iba.app.migration.populate_cfg_index_rows
"""
from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"


def run(conn: sqlite3.Connection) -> None:
    fk_cols = conn.execute(
        "SELECT cc.table_name, cc.name FROM cfg_column cc "
        "JOIN cfg_table ct ON ct.name = cc.table_name "
        "WHERE cc.fk IS NOT NULL AND cc.table_name NOT LIKE 'cfg\\_%' ESCAPE '\\' "
        "ORDER BY cc.table_name, cc.name").fetchall()

    existing = {(r["table_name"], r["name"], r["col"]) for r in conn.execute(
        "SELECT table_name, name, col FROM cfg_index").fetchall()}

    to_insert = []
    for r in fk_cols:
        table, col = r["table_name"], r["name"]
        has_deleted = conn.execute(
            "SELECT 1 FROM cfg_column WHERE table_name=? AND name='deleted'", (table,)
        ).fetchone() is not None
        idx_name = f"idx_{table}_{col}"
        if (table, idx_name, col) in existing:
            continue
        to_insert.append((table, idx_name, col, 0))
        if has_deleted:
            to_insert.append((table, idx_name, "deleted", 1))

    if to_insert:
        conn.executemany(
            "INSERT OR IGNORE INTO cfg_index (table_name, name, col, ordinal) VALUES (?,?,?,?)",
            to_insert)
    conn.commit()

    by_table: dict[str, list[str]] = {}
    for table, idx_name, col, ordv in to_insert:
        if ordv == 0:
            by_table.setdefault(table, []).append(idx_name)
    print(f"index definitions added this run: {sum(len(v) for v in by_table.values())}")
    for table in sorted(by_table):
        print(f"  {table}: {by_table[table]}")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
