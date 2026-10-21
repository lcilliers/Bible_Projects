"""add_cfg_table_category_column_20260831.py — ONE-OFF: `cfg_table` gains a `category` column
(escalation #1146, approved design 2026-08-31).

Same underlying problem escalation #1146 found: `configmaint.propose`'s write-permission scan
(`_known_cfg_tables()`), the config-completeness check (`find_cfg_tables_missing_configmaint_grant`)
and two other sites all treat "name LIKE 'cfg\\_%'" as synonymous with "is a genuine rule-defining
config table" — which is false for `cfg_change_detail`/`cfg_change_log` (audit-log tables sharing
the prefix by convention, not by kind). Fix: a real classification column, same shape as the
existing `cfg_table.inactive` single-purpose flag, not a hardcoded exclusion list (which would need
manual upkeep every time a new log-shaped table appears — the exact fragility this project has
rejected before).

Values: `rule` (the 32 genuine cfg_* tables that define rules — same set `cfg_table_purpose`
already covers two rows each for), `log` (`cfg_change_detail`/`cfg_change_log` — audit trails, not
rule definitions), `data` (every real data table `cfg_table` also registers — ~180 rows, both
databases). Every `cfg_table` row gets an explicit value; nothing is left NULL.

Schema is DDL, same bootstrap-not-propose exception as every other schema addition in this app.

    python -m iba.app.migration.add_cfg_table_category_column_20260831
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

# The 32 genuine cfg_* RULE tables -- same set covered by cfg_table_purpose (2 rows each).
_RULE_TABLES = (
    "cfg_api", "cfg_behaviour_class", "cfg_behaviour_rule", "cfg_book_order",
    "cfg_candidate_rule", "cfg_column", "cfg_connection", "cfg_content_index_exclude",
    "cfg_content_index_size_override", "cfg_enum", "cfg_escalation",
    "cfg_escalation_requirement", "cfg_escalation_transition", "cfg_index", "cfg_meta",
    "cfg_method_rule", "cfg_on_fail", "cfg_passage", "cfg_prose", "cfg_prose_concept",
    "cfg_quality_check", "cfg_report", "cfg_report_csv_table", "cfg_report_section",
    "cfg_setting", "cfg_status_flow", "cfg_step", "cfg_table", "cfg_unique", "cfg_utility",
    "cfg_work_package", "cfg_write_grant",
)
# Demoted 2026-08-30 (escalation #1146) -- audit logs, not rule definitions.
_LOG_TABLES = ("cfg_change_detail", "cfg_change_log")
# cfg_table_purpose itself is the 33rd cfg_-prefixed table (escalation #1130) -- also a rule table.
_RULE_TABLES = _RULE_TABLES + ("cfg_table_purpose",)


def _has_column(conn: sqlite3.Connection, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f'PRAGMA table_info("{table}")'))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        if not _has_column(conn, "cfg_table", "category"):
            conn.execute('ALTER TABLE "cfg_table" ADD COLUMN "category" TEXT')
            print("cfg_table.category added")
        else:
            print("cfg_table.category already exists — skipped")

        for ordinal, value in enumerate(("rule", "data", "log")):
            if not conn.execute(
                    "SELECT 1 FROM cfg_enum WHERE name='table_category' AND value=?",
                    (value,)).fetchone():
                conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) "
                            "VALUES ('table_category', ?, ?, 0)", (value, ordinal))
                print(f"cfg_enum 'table_category'={value!r} added")

        # backfill -- every cfg_table row gets an explicit value
        for t in _RULE_TABLES:
            conn.execute("UPDATE cfg_table SET category='rule' WHERE database='iba' AND name=?", (t,))
        for t in _LOG_TABLES:
            conn.execute("UPDATE cfg_table SET category='log' WHERE database='iba' AND name=?", (t,))
        conn.execute("UPDATE cfg_table SET category='data' WHERE category IS NULL")
        n_rule, n_log, n_data = (conn.execute(
            "SELECT COUNT(*) FROM cfg_table WHERE category=?", (c,)).fetchone()[0]
            for c in ("rule", "log", "data"))
        print(f"backfilled: {n_rule} rule, {n_log} log, {n_data} data")
        uncategorised = conn.execute(
            "SELECT COUNT(*) FROM cfg_table WHERE category IS NULL").fetchone()[0]
        if uncategorised:
            print(f"WARNING: {uncategorised} cfg_table row(s) still uncategorised")

        if not conn.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND "
                            "table_name='cfg_table' AND name='category'").fetchone():
            ordinal = conn.execute(
                "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE database='iba' "
                "AND table_name='cfg_table'").fetchone()[0]
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, inactive) "
                "VALUES ('iba','cfg_table','category',?,?,0,0,0,NULL,NULL,?,?,?,?,0)",
                (ordinal, "TEXT",
                 "rule (a genuine cfg_* configuration table) | data (a real data table, either "
                 "database) | log (an audit-log table sharing the cfg_ prefix by convention only, "
                 "e.g. cfg_change_detail/cfg_change_log -- never a configmaint.propose write target).",
                 "enum.table_category", "escalation #1146, 2026-08-31",
                 "migration backfill; new rows filled by whichever migration registers the table"))
            print("cfg_column row for cfg_table.category added")

        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    run()
    sys.exit(0)
