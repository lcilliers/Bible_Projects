"""add_escalation_needs_followup_column_20260830.py — ONE-OFF: add
escalation.needs_claude_followup / escalation_history.needs_claude_followup (escalation #1075).

Root cause: cfg_escalation_transition's only rule for next_action='approved' checks
`has_resolution` (does a resolution string exist) — nothing checks whether the work the resolution
describes actually happened. A config-change proposal specifically has two genuinely separate
events (approved, then a SEPARATE re-run with -RunId actually applies it) — found live 2026-08-30
when #1059-1062 all reached state='completed' before the real writes had run.

This column lets Claude flag, at Raise or at the ready_for_approval Update, that finishing this
item needs a further action from Claude AFTER the researcher approves it — see
iba/docs/escalation-followup-flag-design-v1-20260830.md for the full design and the
cfg_escalation_transition rule that consumes this flag.

INTEGER, NOT NULL, DEFAULT 0 — most escalations need nothing further; this only opts in the ones
that do. Idempotent (checks for the column first).

    python -m iba.app.migration.add_escalation_needs_followup_column_20260830
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
        for table in ("escalation", "escalation_history"):
            if _has_column(conn, table, "needs_claude_followup"):
                print(f"{table}.needs_claude_followup already exists — skipped")
                continue
            conn.execute(
                f'ALTER TABLE "{table}" ADD COLUMN "needs_claude_followup" INTEGER NOT NULL '
                f'DEFAULT 0')
            print(f"{table}.needs_claude_followup added")
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    run()
    sys.exit(0)
