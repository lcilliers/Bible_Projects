"""project_map_check_2516_v1_20261121.py -- escalation #2516 (session-close check that keeps the
project map current; design approved by the researcher 2026-11-20, option A for the home).

Config for the new session-close detection SC17:
  - cfg_control_home row `project_map` (home iba/docs/project-map.md, read at session start);
  - cfg_setting session_close.map_home (the map file);
  - cfg_setting session_close.map_signals (what the map describes, whose change should reach it).
Three audited cfg_* writes through configmaint.apply_logged(). Idempotent.

Usage:
    python iba/app/migration/project_map_check_2516_v1_20261121.py [--db PATH]
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
RUN_ID = "DEVMODE-2516-PROJECT-MAP-CHECK-20261121"
MAP_HOME = "iba/docs/project-map.md"

SIGNALS = [
    {"name": "control_home_row", "kind": "cfg_change", "table": "cfg_control_home",
     "describes": "a control-map row added, changed or retired"},
    {"name": "governance_setting", "kind": "cfg_change", "table": "cfg_setting", "key_like": "governance.%",
     "describes": "a governance.* setting changed (programme stages, study status, narrative home)"},
    {"name": "layer_reading_setting", "kind": "cfg_change", "table": "cfg_setting", "key_like": "layer.reading",
     "describes": "the stages or layers of the collection reading changed"},
    {"name": "table_added", "kind": "cfg_change", "table": "cfg_table", "op": "insert",
     "describes": "a table added to cfg_table"},
    {"name": "mechanism_task_completed", "kind": "task_in_build",
     "describes": "a task completed that BUILD.md names as built this session"},
    {"name": "programme_book_section", "kind": "prose_section",
     "headings": ["Programme flow", "The analytical grouping: collections and subgroups",
                  "The collection reading", "Surfaces, collections and the registry"],
     "describes": "a Programme book section the map rests on was changed"},
]

SETTINGS = [
    ("session_close.map_home", json.dumps(MAP_HOME),
     "The project map file that session-close SC17 keeps current. Its first lines carry "
     "'Current as of: <date> <commit>'. Escalation #2516."),
    ("session_close.map_signals", json.dumps(SIGNALS),
     "What the project map describes, as change signals for session-close SC17: kind cfg_change "
     "(cfg_change_detail rows of a table, optional op and key_like), task_in_build (a completed task "
     "named in what BUILD.md gained), prose_section (Programme book sections by heading). A signal "
     "that fired with the map file unchanged is a finding. Escalation #2516."),
]

CONTROL_HOME = dict(
    kind="project_map",
    description=("The working guide to the whole project: what it is, how the pieces fit, what is "
                 "built and what is not. A working document, not a result: only database results "
                 "are the project's results. Kept current by session-close SC17."),
    home_type="document", home=MAP_HOME, read_when="session_start",
    history_home="git history of iba/docs/project-map.md",
    source="escalation #2516 (design approved by the researcher 2026-11-20)",
    added_at="2026-11-21T00:00:00Z", inactive=0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        if not conn.execute("SELECT 1 FROM cfg_control_home WHERE kind=?", (CONTROL_HOME["kind"],)).fetchone():
            apply_logged(conn, RUN_ID, "cfg_control_home", "insert", {}, CONTROL_HOME)
            n += 1
        for key, value, use in SETTINGS:
            if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
                apply_logged(conn, RUN_ID, "cfg_setting", "insert", {},
                             {"key": key, "value": value, "use": use, "module": "validation", "inactive": 0})
                n += 1
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
