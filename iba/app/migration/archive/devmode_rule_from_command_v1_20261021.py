"""devmode_rule_from_command_v1_20261021.py -- escalation #2183 (C), for #2177.

The /developer-mode command (.claude/commands/developer-mode.md) held rule text with no cfg_* home:
the scope boundary of Developer Mode and the conduct inside it. Moved here so the command holds the
procedure only and names the rule by key (control map: a session_procedure names rules, holds none;
rule 3: no rule in two places).

One cfg_behaviour_rule (development) developer-mode-scope-and-conduct, through apply_logged().
Idempotent.

Usage:
    python iba/app/migration/devmode_rule_from_command_v1_20261021.py [--db PATH]
"""
import argparse
import datetime
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2183-DEVMODE-RULE-20261021"

TEXT = ("Developer Mode is used only where the IBA app's controls get in the way or need to be "
        "adjusted without the blocks they enforce. Reporting, exploring the data and prototyping "
        "solutions that should follow the rules are standard-mode work. Every new task in a "
        "Developer Mode session is checked against this boundary; being in the mode does not cover "
        "a task by itself. The mode is the researcher's choice at session start, never switched or "
        "self-selected mid-session (CHARTER.md section 4). Inside it: only configmaint.propose's "
        "per-row approval gate is removed and every other rule applies; every development task has "
        "an escalation as its record; work built is tested in the same session against a copy "
        "(never the live DB or live files), with the result recorded on its escalation; every cfg_* "
        "write goes through apply_logged (rule 75) and registers itself (rule 62). While the mode is "
        "active every reply opens with the Developer Mode banner.")
SOURCE = ("Researcher 2026-08-31, verbatim: 'my plan is to only use developer mode for scenarios "
          "where the IBA app controls get in the way or need to be adjusted without the blockages "
          "that the app control enforce. normal work such as reporting, exploring the data, "
          "prototyping solutions that should follow the rules, will all be in standard mode.' "
          "Testing in the same session: researcher 2026-10-13 (#2137). Moved from "
          ".claude/commands/developer-mode.md 2026-10-21 (#2183).")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        if not conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE class='development' AND "
                            "rule_key='developer-mode-scope-and-conduct'").fetchone():
            apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "insert", {}, {
                "class": "development", "rule_key": "developer-mode-scope-and-conduct",
                "rule_text": TEXT, "source": SOURCE,
                "enforced_by": "The /developer-mode command's freshness gate "
                               "(.claude/hooks/gate_developer_mode_entry.py) enforces the session-start "
                               "choice; the rest is context-delivered (rule 81).",
                "added_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "active": 1, "enforcement_status": "partially_enforced"}); n += 1
    print(f"{n} audited cfg_* write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
