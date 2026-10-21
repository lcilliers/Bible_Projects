"""control_kinds_add_tool_usage_v1_20261021.py -- escalation #2187 (USER-GUIDE rewrite, for #2177).

session_close.control_kinds left out tool_usage (USER-GUIDE.md) until the guide was rewritten as
current state only (#2186). The rewrite is done, so the guide joins the SC15 control-file check.
One cfg_setting update through configmaint.apply_logged(). Idempotent.

Usage:
    python iba/app/migration/control_kinds_add_tool_usage_v1_20261021.py [--db PATH]
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
RUN_ID = "DEVMODE-2187-CONTROL-KINDS-TOOL-USAGE-20261021"
KEY = "session_close.control_kinds"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        row = conn.execute("SELECT value FROM cfg_setting WHERE key=?", (KEY,)).fetchone()
        kinds = json.loads(row[0])
        if "tool_usage" not in kinds:
            kinds.append("tool_usage")
            apply_logged(conn, RUN_ID, "cfg_setting", "update", {"key": KEY},
                         {"value": json.dumps(kinds),
                          "use": ("The cfg_control_home kinds whose files session-close SC15 checks "
                                  "(cfgquality.find_control_file_problems). Escalations #2186, #2187.")})
            n += 1
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
