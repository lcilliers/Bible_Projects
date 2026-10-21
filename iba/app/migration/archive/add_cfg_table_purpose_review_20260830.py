"""add_cfg_table_purpose_review_20260830.py — ONE-OFF: new table `cfg_table_purpose`, replacing
the withdrawn column-based attempt (escalation #1130).

Researcher, verbatim, correcting the first attempt: *"it is a config entry not a column ... add
two rows for each cfg table, even those that you have passed validation on -- these two rows are
there for a purpose, to remind you of why the config exist, and how you confirm that you did what
is necessary to make the cfg table doing its work. These entries is made for your benefit."*

Shape: one row per (table_name, kind) — kind is always exactly `purpose` or `success` (cfg_enum
`table_purpose_kind`), so every genuine cfg_* rule table gets EXACTLY 2 rows here, never a column
that would otherwise apply indiscriminately to every row of `cfg_table` (which also registers the
~180 real data tables `verse`/`finding`/etc. — a "success measure" doesn't mean the same thing for
those). Scoped to genuine RULE tables only — the same review that built this also demoted
`cfg_change_detail`/`cfg_change_log` OUT of the config category entirely (escalation #1146); those
two get no rows here.

`purpose` is defined and written BEFORE a table's actual review (the hypothesis); `success` states
the falsifiable test used to check it. Both are written for every table up front, including ones
already reviewed — the point (researcher's own words) is to make Claude actually think each time,
not glance over a table as already-known.

Schema is DDL, same bootstrap-not-propose exception as every other schema addition in this app.

    python -m iba.app.migration.add_cfg_table_purpose_review_20260830
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        exists = conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='cfg_table_purpose'"
        ).fetchone()
        if exists:
            print("cfg_table_purpose already exists — skipped")
        else:
            conn.execute("""CREATE TABLE cfg_table_purpose (
                table_name TEXT NOT NULL,
                kind TEXT NOT NULL,
                text TEXT NOT NULL,
                PRIMARY KEY (table_name, kind)
            )""")
            print("cfg_table_purpose created")

        # cfg_enum group for kind, matching the project's controlled-vocabulary convention
        for ordinal, value in enumerate(("purpose", "success")):
            row = conn.execute(
                "SELECT 1 FROM cfg_enum WHERE name='table_purpose_kind' AND value=?",
                (value,)).fetchone()
            if not row:
                conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) "
                            "VALUES ('table_purpose_kind', ?, ?, 0)", (value, ordinal))
                print(f"cfg_enum 'table_purpose_kind'={value!r} added")

        # self-register in cfg_table + cfg_column, same bootstrap pattern every prior
        # schema-adding migration in this directory uses
        if not conn.execute("SELECT 1 FROM cfg_table WHERE database='iba' AND "
                            "name='cfg_table_purpose'").fetchone():
            conn.execute(
                "INSERT INTO cfg_table (database, name, grain, \"use\", inactive) "
                "VALUES ('iba','cfg_table_purpose','one row per (table_name, kind)',"
                "'Per genuine cfg_* RULE table (never a data table, never a demoted log table like "
                "cfg_change_detail/cfg_change_log), exactly 2 rows: purpose (why it exists, what it "
                "does, its scope) and success (the falsifiable test for whether it is working). "
                "Defined before investigating a table, not derived after the fact -- a working "
                "reminder for Claude, escalation #1130.', 0)")
            print("cfg_table row for cfg_table_purpose added")

        if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer='configmaint.propose' "
                            "AND table_name='cfg_table_purpose' AND database='iba'").fetchone():
            conn.execute("INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                        "VALUES ('configmaint.propose','cfg_table_purpose','iba',0)")
            print("cfg_write_grant row for cfg_table_purpose added -- found missing live, "
                 "escalation #1130, the exact class of gap find_cfg_tables_missing_configmaint_grant "
                 "exists to catch")

        cols = [
            ("table_name", 0, "TEXT", 1, 1, 0, None, "cfg_table.name of the rule table this entry is about."),
            ("kind", 1, "TEXT", 1, 1, 0, "enum.table_purpose_kind", "purpose | success."),
            ("text", 2, "TEXT", 0, 1, 0, None, "The actual statement -- one sentence to a short paragraph."),
        ]
        for name, ordinal, ctype, notnull, is_pk, is_unique, expectation, use_text in cols:
            if conn.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND "
                            "table_name='cfg_table_purpose' AND name=?", (name,)).fetchone():
                continue
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, inactive) "
                "VALUES ('iba','cfg_table_purpose',?,?,?,?,?,?,NULL,NULL,?,?,?,?,0)",
                (name, ordinal, ctype, is_pk, notnull, is_unique, use_text, expectation,
                 "escalation #1130, 2026-08-30", "escalation #1128's per-table review, via configmaint.propose"))
            print(f"cfg_column row for cfg_table_purpose.{name} added")

        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    run()
    sys.exit(0)
