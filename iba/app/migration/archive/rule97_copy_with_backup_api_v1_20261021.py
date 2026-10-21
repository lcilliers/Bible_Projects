"""rule97_copy_with_backup_api_v1_20261021.py -- escalation #2193 (element of the IBA app reset,
#2177): a test copy of a database is made with the SQLite backup API.

Rule 97 (developer-mode-scope-and-conduct) requires Developer Mode work to be tested against a
copy. A plain file copy of a WAL-mode database misses writes still in the -wal file, so the rule
now names how the copy is made: iba/app/lib/dbsnapshot.copy_db (or its --copy-to CLI). Amended in
place rather than adding a rule (rule 104: rule 97 already covers the test copy).

Registers itself in cfg_utility in the same transaction. Written through
configmaint.apply_logged(). Idempotent: skipped when the text is already present. One transaction.

Usage:
    python iba/app/migration/rule97_copy_with_backup_api_v1_20261021.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2193-RULE97-BACKUP-COPY-20261021"
OLD = "against a copy (never the live DB or live files)"
NEW = ("against a copy (never the live DB or live files; a database copy is made with "
       "iba/app/lib/dbsnapshot.copy_db, the SQLite backup API, never a file copy)")
SOURCE_ADD = " | Amended 2026-10-21 (escalation #2193): how a database test copy is made."
MODULE = "rule97_copy_with_backup_api_v1_20261021"
UTILITY = {
    "module": MODULE,
    "file_path": f"iba/app/migration/{MODULE}.py",
    "purpose": "ONE-OFF migration -- escalation #2193: rule 97 names dbsnapshot.copy_db as how a "
               f"database test copy is made, through configmaint.apply_logged under run_id "
               f"{RUN_ID}. inactive=1 once applied.",
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
    row = conn.execute("SELECT rule_text, source FROM cfg_behaviour_rule WHERE id=97 AND "
                       "rule_key='developer-mode-scope-and-conduct'").fetchone()
    if row is None:
        print("cfg_behaviour_rule 97 not found -- nothing done")
        return 1
    if NEW in row[0]:
        print("rule 97 already amended -- skipped")
        return 0
    if OLD not in row[0]:
        print("rule 97 no longer carries the expected text -- nothing done")
        return 1
    new = {"rule_text": row[0].replace(OLD, NEW), "source": (row[1] or "") + SOURCE_ADD}
    registered = conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone()
    if a.dry_run:
        print("DRY RUN -- would update cfg_behaviour_rule 97 to:\n" + new["rule_text"])
        return 0
    with conn:
        apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "update", {"id": 97}, new)
        if not registered:
            apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, UTILITY)
    print(f"cfg_behaviour_rule 97 amended (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
