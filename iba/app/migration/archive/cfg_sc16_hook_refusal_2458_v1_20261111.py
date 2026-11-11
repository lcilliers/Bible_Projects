"""cfg_sc16_hook_refusal_2458_v1_20261111.py -- escalation #2458: SC16 does not count a hook's refusal as a failure.

  setting  session_close.sc16_designed_stops gains the text `hook error: ` (every PreToolUse denial reads "PreToolUse:<tool> hook error: <message>"), and its `use` says so
  utility  this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/cfg_sc16_hook_refusal_2458_v1_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2458-SC16-HOOK-REFUSAL-20261111"
MODULE = "cfg_sc16_hook_refusal_2458_v1_20261111"
KEY = "session_close.sc16_designed_stops"
ADD = "hook error: "
USE_ADD = (" A hook's refusal (every PreToolUse denial reads 'PreToolUse:<tool> hook error: <message>', for example the retired-script gate) is a refusal by design and is not "
           "counted either (#2458).")
MIGRATION_ROW = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2458: SC16 does not count a hook's refusal; run_id {RUN_ID}.", 1,
                 "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def plan(conn):
    ops = []
    value, use = conn.execute("SELECT value, use FROM cfg_setting WHERE key=?", (KEY,)).fetchone()
    stops = json.loads(value)
    new = {}
    if ADD not in stops:
        new["value"] = json.dumps(stops + [ADD])
    if USE_ADD.strip() not in use:
        new["use"] = use.rstrip() + USE_ADD
    if new:
        ops.append(("cfg_setting", "update", {"key": KEY}, new))
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
        for t, op, where, set_ in ops:
            print(" ", t, op, where or set_.get("module"), set_.get("value", ""))
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2458-sc16-hook-refusal', named=True)}")
    try:
        conn.execute("SAVEPOINT sc16_hook")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE sc16_hook")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO sc16_hook")
        conn.execute("RELEASE sc16_hook")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
