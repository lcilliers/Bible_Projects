"""add_cfg_table_database_column.py — ONE-OFF: `cfg_table`/`cfg_column` gain a `database` column
and their primary keys widen to include it, BEFORE any `bible_research.db` table is registered
(escalation #653).

**Why this has to happen first, found live while starting #653**: `cfg_table.name` is currently the
sole PRIMARY KEY (bare `TEXT PRIMARY KEY`), `cfg_column`'s is `(table_name, name)`. `iba.db` and
`bible_research.db` genuinely have same-named-but-different tables — confirmed live: `cluster`,
`passage`, `verse`, `word_registry` all exist in BOTH databases with different columns. Registering
`bible_research.db`'s tables under the current schema would either crash on the PK collision, or —
worse, if the PK were dropped instead of fixed — silently let `Cfg.tables()`/`Cfg.columns()` (`lib/
cfg.py` — *"THE ONLY WAY THE APP READS CONFIG"*) return BOTH databases' rows merged with no way to
tell them apart, and `lib/db.py:build_data_tables()` (*"reads cfg_column and creates the data
tables from it"*) would then try to CREATE `bible_research.db`'s 110 tables INSIDE `iba.db` too.
Confirmed by reading `build_data_tables()`'s own docstring, not assumed.

Schema is DDL (new column + PK widen on two tables), so — same class of exception as every other
schema addition in this app (`bootstrap_inactive_column.py`, `bootstrap_cfg_utility.py`,
`bootstrap_step_kind.py`) — a direct, documented, idempotent bootstrap, not a `configmaint.propose`
call (that gate is for VALUE changes against an existing schema, not schema DDL itself — matching
every prior DDL migration in this directory). SQLite can't ALTER a PRIMARY KEY in place, so this
rebuilds both tables (create-new / copy / drop-old / rename), same pattern
`repair_strong_sense_head.py` and others already use for this class of change.

All existing rows backfilled `database='iba'` — the only database ever registered before this —
zero behaviour change for anything already there.

    python -m iba.app.migration.add_cfg_table_database_column
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _already_done(conn: sqlite3.Connection) -> bool:
    cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_table)")}
    return "database" in cols


def _rebuild(conn: sqlite3.Connection, report: list[str]) -> None:
    conn.execute("""
        CREATE TABLE cfg_table_new (
            database TEXT NOT NULL DEFAULT 'iba',
            name TEXT NOT NULL,
            grain TEXT,
            "use" TEXT,
            PRIMARY KEY (database, name)
        )""")
    conn.execute("INSERT INTO cfg_table_new (database, name, grain, \"use\") "
                "SELECT 'iba', name, grain, \"use\" FROM cfg_table")
    n = conn.execute("SELECT COUNT(*) FROM cfg_table_new").fetchone()[0]
    conn.execute("DROP TABLE cfg_table")
    conn.execute("ALTER TABLE cfg_table_new RENAME TO cfg_table")
    report.append(f"cfg_table rebuilt: PK (name) -> (database, name); {n} row(s) carried over as "
                 f"database='iba'")

    conn.execute("""
        CREATE TABLE cfg_column_new (
            database TEXT NOT NULL DEFAULT 'iba',
            table_name TEXT, name TEXT, ordinal INTEGER,
            "type" TEXT, is_pk INTEGER, "notnull" INTEGER, is_unique INTEGER,
            dflt TEXT, fk TEXT,
            "use" TEXT, expectation TEXT, source TEXT, filled_by TEXT,
            PRIMARY KEY (database, table_name, name)
        )""")
    conn.execute("""INSERT INTO cfg_column_new
        (database, table_name, name, ordinal, "type", is_pk, "notnull", is_unique,
         dflt, fk, "use", expectation, source, filled_by)
        SELECT 'iba', table_name, name, ordinal, "type", is_pk, "notnull", is_unique,
               dflt, fk, "use", expectation, source, filled_by FROM cfg_column""")
    n = conn.execute("SELECT COUNT(*) FROM cfg_column_new").fetchone()[0]
    conn.execute("DROP TABLE cfg_column")
    conn.execute("ALTER TABLE cfg_column_new RENAME TO cfg_column")
    report.append(f"cfg_column rebuilt: PK (table_name, name) -> (database, table_name, name); "
                 f"{n} row(s) carried over as database='iba'")


def _self_document(conn: sqlite3.Connection, report: list[str]) -> None:
    """cfg_column documents cfg_table's own columns too (same convention
    add_cfg_utility_config_exempt.py used for cfg_utility's new columns) — the new `database`
    column on both tables needs its own cfg_column row, or it's itself an orphan the moment
    someone looks."""
    for table in ("cfg_table", "cfg_column"):
        if conn.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND "
                        "name='database'", (table,)).fetchone():
            report.append(f"cfg_column row for {table}.database already present")
            continue
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, "type", is_pk, '
            '"notnull", is_unique, dflt, fk, "use", expectation, source, filled_by) '
            "VALUES ('iba',?,'database',0,'TEXT',1,1,0,'iba',NULL,?,NULL,NULL,"
            "'migration/add_cfg_table_database_column.py')",
            (table, "which physical database this row describes -- part of the primary key "
                    "(escalation #653: iba.db and bible_research.db genuinely share table names "
                    "like word_registry/cluster/passage/verse for DIFFERENT tables)."))
        report.append(f"cfg_column row for {table}.database added")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if _already_done(conn):
        print("cfg_table/cfg_column already have a database column — nothing to do.")
        conn.close()
        return 0

    _rebuild(conn, report)
    _self_document(conn, report)

    conn.commit()
    conn.close()

    print("cfg_table/cfg_column database-column bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
