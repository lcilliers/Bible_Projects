"""add_cfg_table_purpose_and_success_columns_20260830.py — ROLLED BACK, same day, same escalation
(#1130). WRONG DESIGN, kept for provenance, do not re-run: `purpose`/`success_measure` as columns
on `cfg_table` would apply to every one of its ~200 rows -- the 34 `cfg_*` tables AND the ~180 real
data tables (`verse`, `finding`, ...) `cfg_table` also registers. A "success measure" doesn't mean
the same thing for a data table as for a rule table. Researcher's correction, verbatim: "it is a
config entry not a column ... add two rows for each cfg table". Superseded by
`add_cfg_table_purpose_review_20260830.py` (a dedicated table, 2 rows per genuine rule table, none
for data tables). The 2 columns this added were dropped back out the same day (raw
`ALTER TABLE ... DROP COLUMN`, no re-run of this file needed to undo it).

ORIGINAL DOCSTRING BELOW, historical only:

`cfg_table` gains `purpose` and `success_measure` columns (escalation #1130).

Researcher, verbatim: "Add two additional config entries for each cfg table: a) purpose — the
purpose of this table is to …....why does it exist, what does it do, the scope it covers b)
success — what must this table have to be successful". Formalises what escalation #1128's
per-table review already states in prose (a purpose + a success measure, defined BEFORE
investigating each table) as real, queryable config content on `cfg_table` itself — not just
buried in escalation comment history.

Schema is DDL (2 new columns on `cfg_table`), so — same class of exception as
`add_cfg_table_database_column.py` and every other schema addition in this app
(`bootstrap_inactive_column.py`, `bootstrap_cfg_utility.py`, `bootstrap_step_kind.py`) — a direct,
documented, idempotent bootstrap, not a `configmaint.propose` call (that gate governs changing an
EXISTING row's value, not schema DDL itself). Also self-registers its own 2 new `cfg_column` rows
describing `cfg_table.purpose`/`cfg_table.success_measure` — the same bootstrap-registers-its-own-
schema pattern every prior schema-adding migration in this directory uses.

Values are NOT backfilled here — filling in real purpose/success text for all 34 cfg_* tables
requires actually working the review (escalation #1128), not asserting shallow one-liners. The 14
tables #1128 has already properly reviewed get their real values via configmaint.propose,
immediately after this migration runs; the rest get theirs as #1128 continues.

    python -m iba.app.migration.add_cfg_table_purpose_and_success_columns_20260830
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _has_column(conn: sqlite3.Connection, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f'PRAGMA table_info("{table}")'))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        for col in ("purpose", "success_measure"):
            if _has_column(conn, "cfg_table", col):
                print(f"cfg_table.{col} already exists — skipped")
                continue
            conn.execute(f'ALTER TABLE "cfg_table" ADD COLUMN "{col}" TEXT')
            print(f"cfg_table.{col} added")

        for col, use_text in (
            ("purpose", "Why this table exists, what it does, the scope it covers -- one sentence "
                       "to a short paragraph, defined BEFORE investigating the table's actual "
                       "content (escalation #1128's own method), not derived after the fact to "
                       "match whatever happens to be in it."),
            ("success_measure", "What this table must have/do to be considered working correctly -- "
                                "a falsifiable test, checked live against real code/data, not "
                                "asserted from the table's own row text."),
        ):
            exists = conn.execute(
                "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='cfg_table' "
                "AND name=?", (col,)).fetchone()
            if exists:
                print(f"cfg_column row for cfg_table.{col} already exists — skipped")
                continue
            ordinal = conn.execute(
                "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE database='iba' "
                "AND table_name='cfg_table'").fetchone()[0]
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, inactive) "
                "VALUES ('iba','cfg_table',?,?,?,0,0,0,NULL,NULL,?,NULL,?,?,0)",
                (col, ordinal, "TEXT", use_text, "escalation #1130, 2026-08-30",
                 "escalation.raise/update (manual backfill via configmaint.propose)"))
            print(f"cfg_column row for cfg_table.{col} added")

        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    run()
    sys.exit(0)
