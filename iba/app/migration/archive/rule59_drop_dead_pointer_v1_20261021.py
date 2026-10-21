"""rule59_drop_dead_pointer_v1_20261021.py -- escalation #2195 (element of the IBA app reset,
#2177): cfg_behaviour_rule 59 points at a file that is no longer on disk.

Rule 59 (claude-code-filing-obligations) ended with "(docs/interaction-preferences.md's own
protocol)". That file was archived under #2177 (archive/docs/interaction-preferences-history-to-
20261021.md), so the pointer led nowhere; the rule already states the protocol itself (confirm the
destination when genuinely unclear). The parenthetical is dropped; nothing else in the rule changes.

Registers itself in cfg_utility in the same transaction (governance.new_utility_registration_timing).
Written through configmaint.apply_logged() (Developer Mode removes propose's gate, never the
audit). Idempotent: skipped when the pointer is already gone. One transaction.

Usage:
    python iba/app/migration/rule59_drop_dead_pointer_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2195-RULE59-POINTER-20261021"
POINTER = " (docs/interaction-preferences.md's own protocol)"
SOURCE_ADD = (" | Amended 2026-10-21 (escalation #2195): pointer to the archived "
              "docs/interaction-preferences.md dropped.")
MODULE = "rule59_drop_dead_pointer_v1_20261021"
UTILITY = {
    "module": MODULE,
    "file_path": f"iba/app/migration/{MODULE}.py",
    "purpose": "ONE-OFF migration -- escalation #2195: drops the dead pointer to the archived "
               "docs/interaction-preferences.md from cfg_behaviour_rule 59, through "
               f"configmaint.apply_logged under run_id {RUN_ID}. inactive=1 once applied.",
    "inactive": 1,
    "config_exempt": 1,
    "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
                            "configmaint.apply_logged, same class as the other Developer Mode "
                            "migrations",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    row = conn.execute("SELECT rule_text, source FROM cfg_behaviour_rule WHERE id=59 AND "
                       "rule_key='claude-code-filing-obligations'").fetchone()
    if row is None:
        print("cfg_behaviour_rule 59 not found -- nothing done")
        return 1
    if POINTER not in row[0]:
        print("rule 59 has no dead pointer -- skipped")
        return 0
    new = {"rule_text": row[0].replace(POINTER, ""), "source": (row[1] or "") + SOURCE_ADD}
    registered = conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone()
    if a.dry_run:
        print("DRY RUN -- would update cfg_behaviour_rule 59 to:\n" + new["rule_text"])
        print("DRY RUN -- would register cfg_utility " + MODULE if not registered else "")
        return 0
    with conn:
        apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": 59}, new)
        if not registered:
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, UTILITY)
    print(f"cfg_behaviour_rule 59 amended (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
