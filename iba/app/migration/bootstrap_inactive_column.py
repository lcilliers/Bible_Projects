"""bootstrap_inactive_column.py — ONE-OFF: add an `inactive` column to every config-CONTENT
cfg_* table, escalation #310.

Same class of exception as bootstrap_configuration_maintenance.py/bootstrap_setting_module_column.py:
adding a COLUMN to an existing physical table is DDL (ALTER TABLE), which configmaint.propose
cannot do — it only writes/updates/deletes ROWS on already-existing columns. So the column
addition is a direct, documented, idempotent bootstrap here; every actual row is then flipped
inactive/active through the normal `configmaint.propose` path, same as any other config change.

SCOPE — 14 tables, deliberately not all 20 cfg_* tables: excludes cfg_meta/cfg_change_log/
cfg_change_detail (audit trail / internal state, not config content a researcher toggles) and
cfg_table/cfg_column/cfg_unique (describe the SCHEMA of other tables, not a toggleable config item
themselves). See GOVERNANCE.md for the researcher's escalation #310 wording ("add a column in each
config table to mark a config as inactive... excluded from the validation but included as a list in
the report").

    python -m iba.app.migration.bootstrap_inactive_column
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

INACTIVE_TABLES = (
    "cfg_setting", "cfg_step", "cfg_work_package", "cfg_write_grant", "cfg_report",
    "cfg_report_section", "cfg_report_csv_table", "cfg_candidate_rule", "cfg_enum",
    "cfg_on_fail", "cfg_status_flow", "cfg_book_order", "cfg_api", "cfg_connection",
)


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for table in INACTIVE_TABLES:
        cols = {r[1] for r in conn.execute(f'PRAGMA table_info("{table}")')}
        if "inactive" not in cols:
            conn.execute(f'ALTER TABLE "{table}" ADD COLUMN inactive INTEGER NOT NULL DEFAULT 0')
            report.append(f"{table}.inactive column added (physical ALTER)")
        else:
            report.append(f"{table}.inactive already present")

        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE table_name=? AND name='inactive'",
                (table,)).fetchone():
            ordinal = conn.execute(
                "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE table_name=?",
                (table,)).fetchone()[0]
            conn.execute(
                "INSERT INTO cfg_column VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (table, "inactive", ordinal, "INTEGER", 0, 1, 0, 0, None,
                 "deactivate this config row without deleting it — excluded from "
                 "configmaint.validate's coherence/orphan/justification checks, listed "
                 "separately (not silently dropped) in configmaint.report. Set via the normal "
                 "configmaint.propose update path, same as any other cfg_* value.",
                 None, None, "configmaint.propose"))
            report.append(f"cfg_column row for {table}.inactive added")
        else:
            report.append(f"cfg_column row for {table}.inactive already present")

    conn.commit()
    conn.close()

    print("inactive-column bootstrap (escalation #310):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
