"""cfg_analytic_home_2475_v2_20261111.py -- escalation #2475: the retired setting strand_reading.output_dir follows its moved folder.

  setting  strand_reading.output_dir (inactive) names _analytics/reading-tools/strand-reading, where the retired strand-reading outputs now are, so the location check finds a real folder
  utility  this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/cfg_analytic_home_2475_v2_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import json
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2475-ANALYTIC-HOME-V2-20261111"
MODULE = "cfg_analytic_home_2475_v2_20261111"
KEY = "strand_reading.output_dir"
VALUE = "_analytics/reading-tools/strand-reading"
MIGRATION_ROW = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2475: the retired strand_reading.output_dir follows its moved folder; run_id {RUN_ID}.", 1,
                 "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def plan(conn):
    ops = []
    cur = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (KEY,)).fetchone()[0]
    if json.loads(cur) != VALUE:
        ops.append(("cfg_setting", "update", {"key": KEY}, {"value": json.dumps(VALUE)}))
    module, path, inactive, purpose, exempt, reason = MIGRATION_ROW
    if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone() is None:
        ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose, "inactive": inactive, "config_exempt": exempt,
                                                  "config_exempt_reason": reason, "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN: {len(ops)} cfg write(s)")
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2475-analytic-home-v2', named=True)}")
    try:
        conn.execute("SAVEPOINT analytic_home2")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE analytic_home2")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO analytic_home2")
        conn.execute("RELEASE analytic_home2")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
