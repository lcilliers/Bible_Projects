"""fix_escalation_history_write_grant_20260820.py — ONE-OFF: closes escalation #745, found while
compiling the escalation-redesign follow-up list (2026-08-20, same session as BUILD.md §154):
`cfg_write_grant` had no row at all for `escalation_history` — every write to it (from both
`raise_`/`raise_new` and `_snapshot`) was bypassing the grant check entirely, ungoverned, despite
`lib/escalation.py`'s `_grant()` running on every write. Root cause: `_grant()` only ever checks
`table='escalation'`, never `'escalation_history'`, because the original design treated the history
write as an implementation detail of the same operation rather than a second governed table.

Fix: add the missing grant row (writer='escalation', matching the existing 'escalation' grant —
`escalation.py` is the only code that writes `escalation_history`, `run.py` no longer writes either
table directly, see #750). Not a schema change, so no `cfg_column`/`table_ddl()` involved — a plain
`cfg_write_grant` insert, same table already governs the rest of this app's writers.

    python -m iba.app.migration.fix_escalation_history_write_grant_20260820
"""
from __future__ import annotations
from ..lib.cfg import Cfg

DB_PATH = "iba/app/db/iba.db"


def run() -> None:
    cfg = Cfg(DB_PATH)
    conn = cfg.conn
    existing = conn.execute(
        "SELECT 1 FROM cfg_write_grant WHERE writer='escalation' AND table_name='escalation_history' "
        "AND database='iba'").fetchone()
    if existing:
        print("  already present -- no-op")
        cfg.close()
        return
    conn.execute(
        "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
        "VALUES ('escalation', 'escalation_history', 'iba', 0)")
    conn.commit()
    print("  cfg_write_grant: added (writer='escalation', table_name='escalation_history')")
    cfg.close()


if __name__ == "__main__":
    run()
