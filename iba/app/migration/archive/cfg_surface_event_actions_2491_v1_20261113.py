"""cfg_surface_event_actions_2491_v1_20261113.py -- escalation #2491 follow-up found at #2484: configmaint.validate reported surface_event.action values
outside cfg_enum surface_event.action: 'add' (646 rows, run DEVMODE-2491-DERIVED-STEP5-20261113) and 'rename' (10 rows, run DEVMODE-2491-NAMES-STEP6-20261113).
The two actions are real (the derived-form step added links; the names step renamed collections), so they are added to the enum. cfg_* write through
configmaint.apply_logged. Refuses to run twice.   python -m iba.app.migration.archive.cfg_surface_event_actions_2491_v1_20261113 [--db PATH] [--dry-run]"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2484-SURFACE-EVENT-ACTIONS-20261113"
MODULE = "cfg_surface_event_actions_2491_v1_20261113"


def plan(conn):
    ops = []
    nxt = conn.execute("SELECT max(ordinal) FROM cfg_enum WHERE name='surface_event.action'").fetchone()[0] + 1
    for v in ("add", "rename"):
        if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='surface_event.action' AND value=?", (v,)).fetchone():
            ops.append(("cfg_enum", "insert", {}, {"name": "surface_event.action", "value": v, "ordinal": nxt, "inactive": 0}))
            nxt += 1
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2491 follow-up: surface_event.action values add and rename added to the enum; run_id {RUN_ID}."}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID})")
        return 0
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, s in ops:
            apply_logged(conn, RUN_ID, t, op, where, s)
    print(f"{len(ops)} write(s) applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
