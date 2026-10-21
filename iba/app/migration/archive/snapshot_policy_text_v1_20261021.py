"""snapshot_policy_text_v1_20261021.py -- escalation #2193 follow-up: cfg_setting
backup.pre_run_snapshot_policy still said the snapshot was a WAL-checkpointed file copy; since #2193
it is made with the SQLite backup API (lib/dbsnapshot.copy_db). The value is corrected.

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/snapshot_policy_text_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2193-SNAPSHOT-POLICY-TEXT-20261021"
KEY = "backup.pre_run_snapshot_policy"
OLD = "a full DB file snapshot (WAL-checkpointed first)"
NEW = "a full DB snapshot (made with the SQLite backup API, lib/dbsnapshot.copy_db)"
MODULE = "snapshot_policy_text_v1_20261021"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    row = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (KEY,)).fetchone()
    ops = []
    if row and OLD in row[0]:
        ops.append(("cfg_setting", "update", {"key": KEY}, {"value": row[0].replace(OLD, NEW)}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2193: corrects {KEY} to the backup-API "
                       f"snapshot, through configmaint.apply_logged under run_id {RUN_ID}. inactive=1 "
                       f"once applied."}))
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    if not ops:
        print("already applied -- skipped")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
