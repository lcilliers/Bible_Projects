"""add_cfg_write_grant_database_column.py — ONE-OFF: `cfg_write_grant` gains a `database` column,
PK widened to `(writer, table_name, database)` (escalation #680, researcher: "implement table
differentiation in the config tables where it is necessary").

Same root cause as `add_cfg_table_database_column.py` (BUILD.md §125): `iba.db` and
`bible_research.db` share table names (`cluster`/`passage`/`verse`/`word_registry`) for DIFFERENT
tables. `cfg_write_grant.table_name` alone can't say WHICH database's `word_registry` a writer may
touch — this closes that gap in the config layer specifically, per the escalation's own wording.

**Scope, stated plainly**: this is the CONFIG differentiation only. It does not build a runtime
mechanism for a dispatched step to actually open a `bible_research.db` connection and write to it
— `run.py`'s `Db`/`_grant()` is still `iba.db`-only (see `handlers/wordaudit.py`'s module
docstring, `BUILD.md` §127). A `cfg_write_grant` row with `database='bible_research'` documents
INTENT correctly but has no live enforcement path until that separate runtime piece exists. Not
overreached into here — that's still its own follow-up.

All existing rows backfilled `database='iba'` — zero behaviour change for what already exists.
`Cfg.may_write()` gains an optional `database` parameter, default `'iba'`, so every current call
site (none of which pass it) is unaffected.

Schema is DDL (new column + PK widen), same exception class as every other schema migration in
this app — not a `configmaint.propose` call.

    python -m iba.app.migration.add_cfg_write_grant_database_column
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)

    cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_write_grant)")}
    if "database" in cols:
        print("cfg_write_grant already has a database column — nothing to do.")
        conn.close()
        return 0

    conn.execute("""
        CREATE TABLE cfg_write_grant_new (
            writer TEXT, table_name TEXT, database TEXT NOT NULL DEFAULT 'iba',
            inactive INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (writer, table_name, database)
        )""")
    conn.execute("INSERT INTO cfg_write_grant_new (writer, table_name, database, inactive) "
                "SELECT writer, table_name, 'iba', inactive FROM cfg_write_grant")
    n = conn.execute("SELECT COUNT(*) FROM cfg_write_grant_new").fetchone()[0]
    conn.execute("DROP TABLE cfg_write_grant")
    conn.execute("ALTER TABLE cfg_write_grant_new RENAME TO cfg_write_grant")

    # self-document, same convention as add_cfg_table_database_column.py
    if not conn.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND "
                        "table_name='cfg_write_grant' AND name='database'").fetchone():
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, "type", is_pk, '
            '"notnull", is_unique, dflt, fk, "use", expectation, source, filled_by) '
            "VALUES ('iba','cfg_write_grant','database',2,'TEXT',1,1,0,'iba',NULL,?,NULL,NULL,"
            "'migration/add_cfg_write_grant_database_column.py')",
            ("which physical database table_name refers to -- part of the primary key "
             "(escalation #680: iba.db and bible_research.db share table names for different "
             "tables). Config differentiation only -- no runtime cross-database write mechanism "
             "exists yet, see handlers/wordaudit.py's module docstring.",))

    conn.commit()
    conn.close()

    print(f"cfg_write_grant rebuilt: PK (writer, table_name) -> (writer, table_name, database); "
         f"{n} row(s) carried over as database='iba'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
