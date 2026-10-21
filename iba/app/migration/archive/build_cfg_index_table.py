"""build_cfg_index_table.py — ONE-OFF, idempotent: creates `cfg_index`, closing a gap in
`build_data_tables()` itself (`schema-remediation-design-20260807.md` §1).

**Trigger.** Researcher, 2026-08-07 (schema findings follow-up, items d/e): "ensure that lookups
and text scan is minimized... deploy indexes to improve performance (record counts will increase
exponentially)." `build_data_tables()` already emits real `FOREIGN KEY`/`UNIQUE` DDL from
`cfg_column`/`cfg_unique` — but has never had any mechanism for plain secondary indexes. SQLite does
not auto-index FK columns, so every table this app has ever built (not just the debate tables) has
had every join on an FK column run as a full table scan. Fixed as a durable, config-governed
mechanism — same shape as `cfg_unique` — not a one-off `CREATE INDEX` script, so this class of gap
cannot recur the way the debate tables' missing FKs did (config declared the rule, the builder
didn't apply it).

**Shape.** `(table_name, name, col, ordinal)`, `PRIMARY KEY (table_name, name, col)` — one row per
column-in-an-index, multiple rows sharing `(table_name, name)` form one composite index, multiple
distinct `name`s let one table have several indexes (typically one per FK column). Consumed by
`Cfg.indexes(table)` (`lib/cfg.py`) and emitted by `build_data_tables()` (`lib/db.py`) as
`CREATE INDEX IF NOT EXISTS "{name}" ON "{table}" ({cols})`.

This migration only creates the table and registers it (`cfg_table`/`cfg_column`/`cfg_unique`, same
self-description convention `build_quality_check_table.py` used). Populating the actual index rows
(one per live FK column, app-wide) is `populate_cfg_index_rows.py` — kept separate and re-runnable,
since which columns need an index changes every time a table gains a new FK (e.g. this same
session's `operation_party.hib_id`).

    python -m iba.app.migration.build_cfg_index_table
"""
from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

DDL = """
    CREATE TABLE cfg_index (
        table_name TEXT NOT NULL,
        name       TEXT NOT NULL,
        col        TEXT NOT NULL,
        ordinal    INTEGER NOT NULL DEFAULT 0,
        PRIMARY KEY (table_name, name, col)
    )"""

COLUMNS = [
    # is_pk=0 on all three: the real PK is the composite (table_name, name, col), but this app's
    # cfg_column self-description convention (`configmaint.validate`'s _validate_live) treats >1
    # is_pk=1 row as a schema error (found live 2026-08-07, first run of this script) -- no clean
    # way to represent a composite PK here, so left unmarked rather than picking one misleadingly.
    ("cfg_index", "table_name", 0, "TEXT", 0, 1, 0, None, None,
     # fk deliberately NOT 'cfg_table.name' -- configmaint.validate requires an fk target to itself
     # be a row IN cfg_table, and cfg_table describes DATA tables, never itself (found live
     # 2026-08-07, first run: "FK -> unknown table 'cfg_table'").
     "which data table this index is built on", None, None, None),
    ("cfg_index", "name", 1, "TEXT", 0, 1, 0, None, None,
     "index name (unique DB-wide, SQLite requirement) -- convention: idx_{table}_{col}",
     None, None, None),
    ("cfg_index", "col", 2, "TEXT", 0, 1, 0, None, None,
     "one column of this index; multiple rows sharing (table_name, name) form one composite index",
     None, None, None),
    ("cfg_index", "ordinal", 3, "INTEGER", 0, 1, 0, "0", None,
     "column order within a composite index", None, None, None),
]

TABLE = ("cfg_index",
        "Secondary (non-unique) indexes to build per data table -- closes the gap left by "
        "build_data_tables() only ever emitting FK/UNIQUE, never plain indexes "
        "(schema-remediation-design-20260807.md).",
        "cfg_index")

UNIQUES: list[tuple[str, str, int]] = []   # PK (table_name, name, col) IS the natural key; no
                                            # separate cfg_unique row needed (unlike cfg_quality_check)


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def run(conn: sqlite3.Connection) -> None:
    created = False
    if not _table_exists(conn, "cfg_index"):
        conn.execute(DDL)
        created = True

    registered = conn.execute(
        "SELECT 1 FROM cfg_table WHERE name='cfg_index'").fetchone() is not None
    if not registered:
        conn.execute("INSERT INTO cfg_table (name, grain, use) VALUES (?,?,?)",
                    (TABLE[0], TABLE[2], TABLE[1]))
        conn.executemany(
            'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", is_unique, '
            "dflt, fk, use, expectation, source, filled_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            COLUMNS)

    conn.commit()
    print(f"table created this run: {created}")
    print(f"cfg_table/cfg_column registered this run: {not registered}")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
