"""control_file_check_v1_20261021.py -- escalation #2186 (option G of the #2179 review; element of
the IBA app reset, #2177): session-close checks the control files (SC15).

Researcher, 2026-10-21, verbatim: "G should already be in place, but ensure that it is done
properly." It was not: no check read the control documents' own pointers, sizes or leftover
history. The check is cfgquality.find_control_file_problems, run by session.close as SC15; this
migration adds its settings (module validation, beside the other session_close.* settings).

  session_close.control_kinds            the cfg_control_home kinds whose files are checked.
                                         tool_usage (USER-GUIDE.md) joins when its rewrite, #2187,
                                         is done; until then the guide still carries history text.
  session_close.history_pointer_word     a line pointing into an archive/ must carry this word
  session_close.history_markers  replaced-history text that may not stand in a control file
  session_close.always_read_max_bytes    the size limit for a file read every conversation

Every write through configmaint.apply_logged(). Idempotent.

Usage:
    python iba/app/migration/control_file_check_v1_20261021.py [--db PATH]
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
RUN_ID = "DEVMODE-2186-CONTROL-FILE-CHECK-20261021"

SETTINGS = [
    ("session_close.control_kinds",
     ["session_entry", "objective", "mechanism", "session_procedure", "claude_memory"],
     "The cfg_control_home kinds whose files session-close SC15 checks "
     "(cfgquality.find_control_file_problems). tool_usage joins when the USER-GUIDE rewrite "
     "(#2187) is done. Escalation #2186."),
    ("session_close.history_pointer_word", "history",
     "SC15: a line in a control file that points into an archive/ folder must carry this word, "
     "marking it as a pointer to history read deliberately (rule 96). Escalation #2186."),
    ("session_close.history_markers",
     ["~~", r"\bSUPERSEDED\b",
      r"\b(?:Superseded|Corrected|CORRECTED|Restated|REWRITTEN|Amended|Rebuilt) 20\d\d-\d\d-\d\d"],
     "SC15: regular expressions for replaced-history text that may not stand in a control file "
     "(struck-through text, superseded/corrected/amended notes; rule 96). Escalation #2186."),
    ("session_close.always_read_max_bytes", 10000,
     "SC15: the size limit, in bytes, for a control file read every conversation (CLAUDE.md, the "
     "memory index). Escalation #2186."),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        for key, value, use in SETTINGS:
            if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
                apply_logged(conn, RUN_ID, "cfg_setting", "insert", {}, {
                    "key": key, "value": json.dumps(value), "use": use, "module": "validation",
                    "inactive": 0}); n += 1
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
