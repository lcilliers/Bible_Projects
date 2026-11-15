"""add_column_rule_2504_v1_20261115.py -- escalation #2504 (researcher, 2026-11-15: "add the governance rule for adding a column to an existing data table, and ensure that it ties in with the
configs of updating the config for columns"): one behaviour rule, delivered at the point of use of a migration, that states the one thing not stated anywhere: lib/db.build_data_tables creates a missing
table from config but never adds a column to an existing one. It points to rule 62 (the registration in the same unit of work, checked by configmaint.validate) and to governance.table_columns and
restates neither. Checked first against the live corpus (B:104): rule 62 already requires the registration of a table altered and checks both directions of the column drift; nothing states the ALTER.
Writes through apply_logged: the rule, its scope row, the utility row of this migration. Idempotent. Usage: python iba/app/migration/add_column_rule_2504_v1_20261115.py [--db PATH]"""
import argparse
import datetime
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2504-ADD-COLUMN-RULE-20261115"
MODULE = "add_column_rule_2504_v1_20261115"
KEY = "add-column-to-an-existing-data-table"
TEXT = ("A column added to an existing data table is registered and made in the same unit of work: its cfg_column row first (the next ordinal, its type, use, source and filled_by, expectation where "
        "its values are controlled, fk where it references another table; a cfg_index row where it is indexed) through apply_logged, then the physical column with ALTER TABLE ... ADD COLUMN (and its "
        "index) in the same savepoint. lib/db.build_data_tables creates a missing table from config but never adds a column to a table that exists, so the ALTER belongs to the migration. A NOT NULL "
        "column carries a default; a column the existing rows lack is nullable or filled in the same migration. A column is never added by an ALTER with no cfg_column row, and the use text of a column "
        "whose meaning changes is updated through apply_logged in the same unit (governance.table_columns, config-updated-same-unit-of-work-as-change).")
SOURCE = "researcher, 2026-11-15, #2504 v4, verbatim: \"add the the governance rule for adding a column to an existing data table, and ensure that it ties in with the configs of updating the config for columns\""
ENFORCED = ("configmaint.validate -> cfgquality.find_unregistered_tables_and_columns: a live column with no cfg_column row, and an active cfg_column row for a column not on its live table, are hard errors; "
            "delivered at the first use of a migration (cfg_rule_scope command migration)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    if conn.execute("SELECT 1 FROM cfg_behaviour_rule WHERE rule_key=?", (KEY,)).fetchone():
        print("already applied: nothing changed")
        return 0
    nid = conn.execute("SELECT max(id) FROM cfg_behaviour_rule").fetchone()[0] + 1
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute("SAVEPOINT add_column_rule")
    apply_logged(conn, RUN_ID, "cfg_behaviour_rule", "insert", {}, {"id": nid, "class": "development", "rule_key": KEY, "rule_text": TEXT, "source": SOURCE, "enforced_by": ENFORCED,
                                                                    "added_at": now, "active": 1, "enforcement_status": "mechanically_enforced", "deliver_when": "always"})
    apply_logged(conn, RUN_ID, "cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{nid}", "scope_kind": "command", "scope_value": "migration", "inactive": 0})
    apply_logged(conn, RUN_ID, "cfg_utility", "insert", {}, {
        "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "purpose": f"ONE-OFF migration -- escalation #2504: the rule for adding a column to an existing data table; run_id {RUN_ID}.",
        "inactive": 1, "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
        "crash_escalation_reviewed": 0, "crash_escalation_note": None})
    conn.execute("RELEASE add_column_rule")
    conn.commit()
    print(f"applied (run {RUN_ID}): rule B:{nid} {KEY}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
