"""register_20261021_migrations_v1_20261021.py -- escalation #2196 (element of the IBA app reset,
#2177): the nine Developer Mode migrations written on 2026-10-21 under #2178-#2187 were never
registered in cfg_utility (governance.new_utility_registration_timing). Each gets a row matching
the existing one-off migration rows (inactive=1: already applied; config_exempt=1). This script
registers itself in the same transaction.

Written through configmaint.apply_logged() (Developer Mode removes propose's gate, never the
audit). Idempotent: a module already registered is skipped. One transaction.

Usage:
    python iba/app/migration/register_20261021_migrations_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2196-REGISTER-MIGRATIONS-20261021"
EXEMPT_REASON = ("one-off migration script -- writes cfg_* rows through configmaint.apply_logged, "
                 "same class as the other Developer Mode migrations")

# module stem -> (escalation, what it did, its run_id)
MIGRATIONS = {
    "rule63_approval_handover_checks_v1_20261021":
        ("#2178", "adds the approval hand-over checks to cfg_behaviour_rule 63",
         "DEVMODE-2178-RULE63-HANDOVER-20261021"),
    "control_map_v1_20261021":
        ("#2180", "the control map (cfg_control_home)", "DEVMODE-2180-CONTROL-MAP-20261021"),
    "claude_md_rules_to_config_v1_20261021":
        ("#2181", "moves the rules CLAUDE.md held with no cfg_* home into config",
         "DEVMODE-2181-CLAUDE-MD-RULES-20261021"),
    "history_out_of_read_path_v1_20261021":
        ("#2183", "replaced history out of the read path (rule 96)",
         "DEVMODE-2183-HISTORY-OUT-20261021"),
    "devmode_rule_from_command_v1_20261021":
        ("#2183", "moves the Developer Mode scope and conduct rule out of the /developer-mode "
                  "command into cfg_behaviour_rule", "DEVMODE-2183-DEVMODE-RULE-20261021"),
    "memory_rules_to_config_v1_20261021":
        ("#2184", "moves the live rules held only in Claude memory into config",
         "DEVMODE-2184-MEMORY-RULES-20261021"),
    "rule_delivery_scope_v1_20261021":
        ("#2185", "scopes the start-up rule print and the compliance restatement to the session "
                  "(deliver_when)", "DEVMODE-2185-RULE-DELIVERY-SCOPE-20261021"),
    "control_file_check_v1_20261021":
        ("#2186", "session-close control-file check SC15", "DEVMODE-2186-CONTROL-FILE-CHECK-20261021"),
    "control_kinds_add_tool_usage_v1_20261021":
        ("#2187", "adds tool_usage (USER-GUIDE.md) to session_close.control_kinds",
         "DEVMODE-2187-CONTROL-KINDS-TOOL-USAGE-20261021"),
    "register_20261021_migrations_v1_20261021":
        ("#2196", "registers the 2026-10-21 Developer Mode migrations in cfg_utility (this file)",
         RUN_ID),
}


def row(module: str) -> dict:
    esc, what, run_id = MIGRATIONS[module]
    return {"module": module,
            "file_path": f"iba/app/migration/{module}.py",
            "purpose": f"ONE-OFF migration -- escalation {esc}: {what}, every cfg_* write through "
                       f"configmaint.apply_logged under run_id {run_id}. inactive=1 once applied.",
            "inactive": 1, "config_exempt": 1, "config_exempt_reason": EXEMPT_REASON}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    missing = [m for m in MIGRATIONS if not (ROOT / "iba/app/migration" / f"{m}.py").exists()]
    if missing:
        print("not on disk -- nothing done: " + ", ".join(missing))
        return 1
    todo = [m for m in MIGRATIONS
            if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (m,)).fetchone()]
    if not todo:
        print("all registered -- skipped")
        return 0
    if a.dry_run:
        print("DRY RUN -- would register:\n  " + "\n  ".join(todo))
        return 0
    with conn:
        for m in todo:
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, row(m))
    print(f"{len(todo)} migration(s) registered (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
