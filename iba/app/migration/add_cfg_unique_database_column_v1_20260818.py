"""add_cfg_unique_database_column_v1_20260818.py — ONE-OFF: `cfg_unique` gains a `database`
column, PK widened to `(database, table_name, col)` (escalation #723's supporting infra —
same root cause as `add_cfg_table_database_column.py`/`add_cfg_write_grant_database_column.py`:
`iba.db` and `bible_research.db` share table names, e.g. `passage`, for DIFFERENT tables).

Trigger: escalation #722 is about to add `cfg_unique` rows for 7 `bible_research.db` tables.
Without this column, `cfg_unique.table_name='passage'` (an existing iba.db row) would be
ambiguous against a future `bible_research.db` `passage`-named row, and `Cfg.unique_key()` (the
live dedup-key resolver, `lib/db.py`) has no way to pick the right one for whichever database it's
actually scoped to.

All 34 existing rows backfilled `database='iba'` — verified: every current `cfg_unique.table_name`
(candidate_seed, cfg_method_rule, cfg_quality_check, passage*, phenomenon, span, strong_verse,
verse_hib, verse_lexical, word_strong) is an iba.db-only concept; zero behaviour change for what
already exists. `Cfg.unique_key()` gains a `database` parameter, default `'iba'` (matches
`may_write()`'s existing convention), so the one live call site (`lib/db.py`, always operating on
iba.db) is unaffected.

    python -m iba.app.migration.add_cfg_unique_database_column_v1_20260818
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)

    cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_unique)")}
    if "database" in cols:
        print("cfg_unique already has a database column — nothing to do.")
        conn.close()
        return 0

    conn.execute("""
        CREATE TABLE cfg_unique_new (
            database TEXT NOT NULL DEFAULT 'iba',
            table_name TEXT, col TEXT, ordinal INTEGER,
            PRIMARY KEY (database, table_name, col)
        )""")
    conn.execute("INSERT INTO cfg_unique_new (database, table_name, col, ordinal) "
                "SELECT 'iba', table_name, col, ordinal FROM cfg_unique")
    n = conn.execute("SELECT COUNT(*) FROM cfg_unique_new").fetchone()[0]
    conn.execute("DROP TABLE cfg_unique")
    conn.execute("ALTER TABLE cfg_unique_new RENAME TO cfg_unique")

    if not conn.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND "
                        "table_name='cfg_unique' AND name='database'").fetchone():
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, "type", is_pk, '
            '"notnull", is_unique, dflt, fk, "use", expectation, source, filled_by) '
            "VALUES ('iba','cfg_unique','database',0,'TEXT',1,1,0,'iba',NULL,?,NULL,NULL,"
            "'migration/add_cfg_unique_database_column_v1_20260818.py')",
            ("which physical database table_name refers to -- part of the primary key "
             "(iba.db and bible_research.db share table names, e.g. 'passage', for different "
             "tables; escalations #653/#680 widened cfg_table/cfg_write_grant the same way, "
             "this closes the same gap for cfg_unique). Config differentiation only.",))
        # existing ordinals shift by 1 (database is now column 0)
        conn.execute("UPDATE cfg_column SET ordinal=ordinal+1 WHERE database='iba' AND "
                    "table_name='cfg_unique' AND name!='database'")

    conn.commit()
    conn.close()

    print(f"cfg_unique rebuilt: PK (table_name, col) -> (database, table_name, col); "
         f"{n} row(s) carried over as database='iba'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
