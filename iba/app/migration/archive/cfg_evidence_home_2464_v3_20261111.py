"""cfg_evidence_home_2464_v3_20261111.py -- escalation #2464: the retired setting collection.evidence_path no longer names a folder that does not exist.

  setting  collection.evidence_path (inactive since v2) takes the value of surfaces.exports_root, the folder the report really writes to, so the location check of
           Config-Maintenance.ps1 -Step Validate finds a real folder; the setting stays inactive and its use says it is retired
  utility  this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/cfg_evidence_home_2464_v3_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
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
RUN_ID = "DEVMODE-2464-EVIDENCE-HOME-V3-20261111"
MODULE = "cfg_evidence_home_2464_v3_20261111"
KEY = "collection.evidence_path"
MIGRATION_ROW = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2464: the retired collection.evidence_path names the real folder; run_id {RUN_ID}.", 1,
                 "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def plan(conn):
    ops = []
    target = conn.execute("SELECT value FROM cfg_setting WHERE key='surfaces.exports_root'").fetchone()[0]
    value = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (KEY,)).fetchone()[0]
    if json.loads(value) != json.loads(target):
        ops.append(("cfg_setting", "update", {"key": KEY}, {"value": target}))
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
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2464-evidence-home-v3', named=True)}")
    try:
        conn.execute("SAVEPOINT evidence_home3")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE evidence_home3")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO evidence_home3")
        conn.execute("RELEASE evidence_home3")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
