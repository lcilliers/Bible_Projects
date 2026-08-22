"""add_resolution_kind_column_v1_20260822.py — ONE-OFF, idempotent. Stage 2 (schema half) of the
build approved on escalation #798 (design: iba/docs/escalation-decision-vs-defect-axis-proposal-
v5-20260822.md), tracked on #799. Adds the `resolution_kind` column itself — the design's own text
implies it (a value "required at Raise" must have somewhere to live) but Stage 1's migration only
built the config side (enum + requirement row); the column was a gap in that pass, closed here
before Stage 2's code changes need to write to it.

Adds `resolution_kind TEXT` to both `escalation` and `escalation_history`, registers both in
`cfg_column`, and registers this script in `cfg_utility`.

    python -m iba.app.migration.add_resolution_kind_column_v1_20260822
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_MIGRATION_FILE = "iba/app/migration/add_resolution_kind_column_v1_20260822.py"


def _add_column(conn, table, report):
    cols = {r[1] for r in conn.execute(f"PRAGMA table_info({table})")}
    if "resolution_kind" not in cols:
        conn.execute(f"ALTER TABLE {table} ADD COLUMN resolution_kind TEXT")
        report.append(f"{table}.resolution_kind added")
    else:
        report.append(f"{table}.resolution_kind already present")


def _column_row(conn, table, use, report):
    if not conn.execute(
            "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name='resolution_kind'",
            (table,)).fetchone():
        ordinal = conn.execute(
            "SELECT COUNT(*) FROM cfg_column WHERE database='iba' AND table_name=?",
            (table,)).fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
            "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by) "
            "VALUES ('iba',?,?,?,?,0,0,0,NULL,NULL,?,NULL,NULL,?)",
            (table, "resolution_kind", ordinal, "TEXT", use, _MIGRATION_FILE))
        report.append(f"cfg_column ({table}.resolution_kind) added")
    else:
        report.append(f"cfg_column ({table}.resolution_kind) already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _add_column(conn, "escalation", report)
    _add_column(conn, "escalation_history", report)

    _column_row(conn, "escalation",
               "decision_required or self_correctable (cfg_enum resolution_kind) -- required at "
               "Raise, escalation #798/#799. decision_required is terminal and routes to design; "
               "self_correctable is fixed directly by Claude, no approval gate. Mutable in one "
               "direction only: self_correctable -> decision_required via escalate_to_decision(), "
               "never the reverse.", report)
    _column_row(conn, "escalation_history",
               "per-version snapshot of escalation.resolution_kind at that version.", report)

    if not conn.execute(
            "SELECT 1 FROM cfg_utility WHERE file_path=?", (_MIGRATION_FILE,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "config_exempt_reason, crash_escalation_reviewed) VALUES (?,?,?,0,1,?,0)",
            ("add_resolution_kind_column", _MIGRATION_FILE,
             "One-off migration: escalation #798/#799 Stage 2 (schema half) -- adds the "
             "resolution_kind column to escalation/escalation_history, closing a gap left by "
             "Stage 1's config-only pass.",
             "one-off migration script -- writes directly into cfg_* tables via raw sqlite3, "
             "same class as cfgload.py"))
        report.append(f"cfg_utility {_MIGRATION_FILE!r} registered")
    else:
        report.append(f"cfg_utility {_MIGRATION_FILE!r} already registered")

    conn.commit()
    conn.close()

    print("resolution_kind column bootstrap (escalation #798/#799, Stage 2 schema half):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
