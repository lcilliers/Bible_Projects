"""ps_dir_setting_2208_v1_20261021.py -- escalation #2208 option (a): iba/app/lib/cfgquality.py now
reads governance.scripts_ps_dir (ps_dir()) instead of a literal path, so the setting is a plain value
read by code and joins cfg_setting compliance.value_settings (#2206 option 3).
governance.scripts_python_dir stays delivered: no code reads it yet.

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/ps_dir_setting_2208_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2208-PS-DIR-SETTING-20261021"
KEY = "compliance.value_settings"
ADD = "governance.scripts_ps_dir"
MODULE = "ps_dir_setting_2208_v1_20261021"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    row = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (KEY,)).fetchone()
    if row is None:
        print(f"{KEY} missing -- run the #2206 migration first")
        return 1
    keys = json.loads(row[0])
    if ADD not in keys:
        ops.append(("cfg_setting", "update", {"key": KEY}, {"value": json.dumps(sorted(keys + [ADD]))}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2208: adds {ADD} to {KEY}, through "
                       f"configmaint.apply_logged under run_id {RUN_ID}. inactive=1 once applied."}))
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
