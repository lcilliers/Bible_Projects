"""reading_waste_2206_v1_20261021.py -- escalation #2206 option 3: cfg_setting
compliance.value_settings, the governance settings that hold a plain value (a path, a format) read by
the code that uses them, so lib/compliance.py neither delivers nor asks for a restatement of them.
governance.scripts_ps_dir and governance.scripts_python_dir are not in the list: no code reads them
(raised as its own escalation), so they stay delivered.

Registers itself (inactive, at its own archive path) in the same transaction. Written through
configmaint.apply_logged(). Idempotent. One transaction.

Usage:
    python iba/app/migration/reading_waste_2206_v1_20261021.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2206-READING-WASTE-20261021"
KEY = "compliance.value_settings"
VALUE = ["governance.escalation_worksheet_path", "governance.oneoff_report_archive_dir",
         "governance.oneoff_report_dir", "governance.oneoff_report_format",
         "governance.oneoff_report_naming_pattern", "governance.ps_worksheet_path",
         "governance.session_log_dir"]
MODULE = "reading_waste_2206_v1_20261021"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = []
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (KEY,)).fetchone():
        ops.append(("cfg_setting", "insert", {}, {
            "key": KEY, "value": json.dumps(VALUE), "module": "behaviour", "inactive": 0,
            "use": "#2206 option 3: governance settings holding a plain value (a path, a format), "
                   "read by the code that uses them; lib/compliance.py leaves them out of the "
                   "delivered rules and the compliance file"}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows "
            "through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2206: inserts {KEY}, through "
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
