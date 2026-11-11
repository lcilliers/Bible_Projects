"""cfg_evidence_home_2464_v2_20261111.py -- escalation #2464: the evidence report writes to the governed home of collection results (surfaces.exports_root).

  setting  collection.evidence_path made inactive (the report folder is surfaces.exports_root, folder_purpose results; outputs/reports/collection-evidence was not a registered folder)
  step     collection.evidence: its text names surfaces.exports_root
  utility  this migration
All cfg_* writes through configmaint.apply_logged(). A named rollback snapshot is taken before a live apply. Idempotent. One transaction.

Usage:
    python iba/app/migration/cfg_evidence_home_2464_v2_20261111.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2464-EVIDENCE-HOME-20261111"
MODULE = "cfg_evidence_home_2464_v2_20261111"
KEY = "collection.evidence_path"
STEP = "collection.evidence"
OLD_PHRASE = "under collection.evidence_path,"
NEW_PHRASE = "under surfaces.exports_root (the folder of the collection exports),"
RETIRED_USE = ("RETIRED (#2464): the evidence report writes to surfaces.exports_root, the registered folder of collection results (folder_purpose results); "
               "outputs/reports/collection-evidence was not a registered folder.")
MIGRATION_ROW = (MODULE, f"iba/app/migration/archive/{MODULE}.py", 1, f"ONE-OFF migration -- escalation #2464: the evidence report writes to surfaces.exports_root; run_id {RUN_ID}.", 1,
                 "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations")


def plan(conn):
    ops = []
    r = conn.execute("SELECT inactive, use FROM cfg_setting WHERE key=?", (KEY,)).fetchone()
    if r and (r[0] != 1 or r[1] != RETIRED_USE):
        ops.append(("cfg_setting", "update", {"key": KEY}, {"inactive": 1, "use": RETIRED_USE}))
    does = conn.execute("SELECT does FROM cfg_step WHERE step=?", (STEP,)).fetchone()[0]
    if OLD_PHRASE in does:
        ops.append(("cfg_step", "update", {"step": STEP}, {"does": does.replace(OLD_PHRASE, NEW_PHRASE)}))
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
            print(" ", t, op, where or set_.get("module"), sorted(set_))
        return 0
    if not ops:
        print("already applied: nothing changed")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2464-evidence-home', named=True)}")
    try:
        conn.execute("SAVEPOINT evidence_home")
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
        conn.execute("RELEASE evidence_home")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO evidence_home")
        conn.execute("RELEASE evidence_home")
        raise
    print(f"applied (run {RUN_ID}): {len(ops)} cfg write(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
