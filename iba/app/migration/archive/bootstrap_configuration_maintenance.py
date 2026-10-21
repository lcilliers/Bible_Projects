"""bootstrap_configuration_maintenance.py — ONE-OFF: register the configuration_maintenance
work package and extend `escalation` for three-way answers.

Why this is a direct DB write, not a `configmaint.propose` call: `configuration_maintenance`
is the utility this script is bringing into existence — it cannot register itself through
itself, the same reason `cfgload.py`'s CFG_DDL is the one hard-coded schema bootstrap in the
whole app (GOVERNANCE.md §2). This script is that same class of one-time exception, and is
not meant to be run again once `configuration-maintenance` exists as a registered work
package — from then on, every `cfg_*` change goes through `configmaint.propose`, including
any future change to `configuration_maintenance`'s own config. Idempotent (safe if re-run,
e.g. after an interrupted first run): every write here is INSERT-if-missing.

Approved by the researcher via direct review of the design document
(iba/docs/iba-configuration-maintenance-layered-design-v1-20260721.md, section 2) — see
iba/docs/ for the reasoning behind every table/column/row this script adds.

    python -m iba.app.migration.bootstrap_configuration_maintenance
"""

from __future__ import annotations

import datetime
import sqlite3
import sys

from ..lib import db as dbmod
from ..lib.cfg import Cfg, DB_PATH


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# Every cfg_* table configuration_maintenance is granted to write — this is what "restricts
# every config change to go through it" (rule c) means in the cfg_write_grant mechanism.
CFG_TABLES = (
    "cfg_meta", "cfg_table", "cfg_column", "cfg_unique", "cfg_enum", "cfg_connection",
    "cfg_api", "cfg_write_grant", "cfg_work_package", "cfg_step", "cfg_setting",
    "cfg_on_fail", "cfg_status_flow", "cfg_book_order", "cfg_candidate_rule", "cfg_change_log",
)


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []

    # 1. escalation.comment — the three-way-answer schema change (physical DDL; cfg_column
    #    metadata does NOT retrofit an existing physical table, only CREATE TABLE IF NOT EXISTS
    #    for a fresh one — confirmed by reading lib/db.py's build_data_tables()).
    have_cols = {r["name"] for r in conn.execute("PRAGMA table_info(escalation)")}
    if "comment" not in have_cols:
        conn.execute("ALTER TABLE escalation ADD COLUMN comment TEXT")
        report.append("escalation.comment column added (physical ALTER)")
    else:
        report.append("escalation.comment column already present")

    if not conn.execute(
            "SELECT 1 FROM cfg_column WHERE table_name='escalation' AND name='comment'").fetchone():
        conn.execute(
            "INSERT INTO cfg_column VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            ("escalation", "comment", 12, "TEXT", 0, 0, 0, None, None,
             "researcher feedback on a 'revise' answer (or any answer)", None, None,
             "escalation.answer_for_run"))
        report.append("cfg_column row for escalation.comment added")
    else:
        report.append("cfg_column row for escalation.comment already present")

    # 2. escalation_answer enum — approve | reject | revise (the three-way contract)
    if not conn.execute(
            "SELECT 1 FROM cfg_enum WHERE name='escalation_answer'").fetchone():
        for i, v in enumerate(("approve", "reject", "revise")):
            conn.execute("INSERT INTO cfg_enum VALUES (?,?,?)", ("escalation_answer", v, i))
        report.append("cfg_enum group 'escalation_answer' (approve/reject/revise) added")
    else:
        report.append("cfg_enum group 'escalation_answer' already present")

    # 3. cfg_work_package — configuration-maintenance
    if not conn.execute(
            "SELECT 1 FROM cfg_work_package WHERE name='configuration-maintenance'").fetchone():
        conn.execute("INSERT INTO cfg_work_package VALUES (?,?,?)",
                     ("configuration-maintenance", "Config-Maintenance.ps1", "none"))
        report.append("cfg_work_package 'configuration-maintenance' added")
    else:
        report.append("cfg_work_package 'configuration-maintenance' already present")

    # 4. cfg_step — validate / propose / report
    steps = [
        (0, "configmaint.validate", "iba.app.handlers.configmaint:validate", "none",
         "coherence-check the live cfg_* tables — read-only, no approval needed"),
        (1, "configmaint.propose", "iba.app.handlers.configmaint:propose", "none",
         "the only path that may change a cfg_* row — approval-gated (escalation, 3-way)"),
        (2, "configmaint.report", "iba.app.handlers.configmaint:report", "none",
         "regenerate CONFIG-REPORT.md from the live cfg_* tables — read-only"),
    ]
    for ordinal, step, handler, scope, does in steps:
        existing = conn.execute(
            "SELECT handler FROM cfg_step WHERE work_package='configuration-maintenance' AND step=?",
            (step,)).fetchone()
        if not existing:
            conn.execute("INSERT INTO cfg_step VALUES (?,?,?,?,?,?)",
                         ("configuration-maintenance", ordinal, step, handler, scope, does))
            report.append(f"cfg_step '{step}' added")
        elif existing[0] != handler:
            conn.execute(
                "UPDATE cfg_step SET handler=? WHERE work_package='configuration-maintenance' AND step=?",
                (handler, step))
            report.append(f"cfg_step '{step}' handler corrected: {existing[0]!r} -> {handler!r}")
        else:
            report.append(f"cfg_step '{step}' already present")

    # 5. cfg_setting — configmaint.* (rule e: its own config)
    settings = [
        ("configmaint.report_path", '"iba/app/config/CONFIG-REPORT.md"',
         "where configmaint.report writes the snapshot"),
        ("configmaint.auto_report", "true",
         "whether an approved configmaint.propose automatically chains to configmaint.report"),
        ("configmaint.reference_seed_dir", '"iba/app/config/archive"',
         "REFERENCE ONLY (never reloaded from) — where a one-time completeness cross-check "
         "may look for items missing from the live cfg_* tables; the DB is master"),
    ]
    for key, value, use in settings:
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
            conn.execute("INSERT INTO cfg_setting VALUES (?,?,?)", (key, value, use))
            report.append(f"cfg_setting '{key}' added")
        else:
            report.append(f"cfg_setting '{key}' already present")

    # 5b. cfg_on_fail — every condition validate()/propose() can raise must have a path,
    #     or the dispatcher defaults to report-stop (this is exactly the bug the first
    #     end-to-end test caught: 'needs-approval' fell through to report-stop with no
    #     row here, instead of pausing).
    on_fail = [
        ("configmaint.validate", "invalid", "report-stop", "the live cfg_* store is incoherent"),
        ("configmaint.propose", "invalid-proposal", "report-stop",
         "the proposed change fails a coherence check — never escalated"),
        ("configmaint.propose", "needs-approval", "pause-continue",
         "a config change needs researcher approval"),
        ("configmaint.propose", "change-rejected", "report-stop",
         "the researcher rejected the proposed change"),
        ("configmaint.propose", "needs-revision", "report-stop",
         "the researcher asked for the proposal to be revised (see the comment) and resubmitted"),
    ]
    for step, condition, path, message in on_fail:
        if not conn.execute(
                "SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", (step, condition)).fetchone():
            conn.execute("INSERT INTO cfg_on_fail VALUES (?,?,?,?,?)",
                         (step, condition, path, None, message))
            report.append(f"cfg_on_fail ({step}, {condition}) -> {path} added")
        else:
            report.append(f"cfg_on_fail ({step}, {condition}) already present")

    # 6. cfg_write_grant — configmaint.propose may write every cfg_* table (rule c)
    added = 0
    for t in CFG_TABLES:
        if not conn.execute(
                "SELECT 1 FROM cfg_write_grant WHERE writer='configmaint.propose' AND table_name=?",
                (t,)).fetchone():
            conn.execute("INSERT INTO cfg_write_grant VALUES (?,?)", ("configmaint.propose", t))
            added += 1
    report.append(f"cfg_write_grant: configmaint.propose granted {added} new table(s) "
                  f"(of {len(CFG_TABLES)} total)")

    # 7. cfg_change_detail — the ROW-LEVEL change log configmaint.propose actually needs.
    #    cfg_change_log's existing shape (config_version/seed_hash/loaded_at/validated) has
    #    nowhere to record WHAT changed — it only ever logged whole-reload events. This is a
    #    genuine, small DATA table (registered like any other, via cfg_table/cfg_column), not
    #    a cfg_* meta table, so db.build() (below) creates it physically from these rows.
    if not conn.execute("SELECT 1 FROM cfg_table WHERE name='cfg_change_detail'").fetchone():
        conn.execute("INSERT INTO cfg_table VALUES (?,?,?)",
                     ("cfg_change_detail", "one row per configmaint.propose write",
                      "row-level audit of every cfg_* change actually applied — what "
                      "cfg_change_log's whole-reload shape could not record"))
        detail_cols = [
            ("id", 0, "INTEGER", 1, 0, 0, None, None, "surrogate key", None, None, None),
            ("run_id", 1, "TEXT", 0, 1, 0, None, "run.run_id", "the run that made the change",
             None, None, "configmaint.propose"),
            ("table_name", 2, "TEXT", 0, 1, 0, None, None, "which cfg_* table changed",
             None, None, "configmaint.propose"),
            ("op", 3, "TEXT", 0, 1, 0, None, None, "insert | update | delete",
             "enum.cfg_change_op", None, "configmaint.propose"),
            ("where_json", 4, "TEXT", 0, 0, 0, None, None, "the row's natural key (JSON)",
             None, None, "configmaint.propose"),
            ("set_json", 5, "TEXT", 0, 0, 0, None, None, "the new values written (JSON)",
             None, None, "configmaint.propose"),
            ("before_json", 6, "TEXT", 0, 0, 0, None, None,
             "the row's prior state, for update/delete (JSON, null for insert)",
             None, None, "configmaint.propose"),
            ("applied_at", 7, "TEXT", 0, 1, 0, None, None, "when the write committed",
             None, None, "configmaint.propose"),
        ]
        for name, ordinal, typ, is_pk, notnull, is_unique, dflt, fk, use, expectation, source, filled_by in detail_cols:
            conn.execute("INSERT INTO cfg_column VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         ("cfg_change_detail", name, ordinal, typ, is_pk, notnull, is_unique,
                          dflt, fk, use, expectation, source, filled_by))
        for t in ("configmaint.propose",):
            conn.execute("INSERT OR IGNORE INTO cfg_write_grant VALUES (?,?)",
                         (t, "cfg_change_detail"))
        report.append("cfg_change_detail (row-level change log) registered")
    else:
        report.append("cfg_change_detail already registered")

    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='cfg_change_op'").fetchone():
        for i, v in enumerate(("insert", "update", "delete")):
            conn.execute("INSERT INTO cfg_enum VALUES (?,?,?)", ("cfg_change_op", v, i))
        report.append("cfg_enum group 'cfg_change_op' (insert/update/delete) added")
    else:
        report.append("cfg_enum group 'cfg_change_op' already present")

    # audit this bootstrap itself in cfg_change_log — a real, identifiable entry, not silent
    version_row = conn.execute("SELECT value FROM cfg_meta WHERE key='config_version'").fetchone()
    conn.execute(
        "INSERT INTO cfg_change_log (config_version, seed_hash, loaded_at, validated) VALUES (?,?,?,1)",
        (version_row["value"] if version_row else "?",
         "bootstrap:configuration-maintenance-2026-07-21", _now()))
    report.append("cfg_change_log: bootstrap event recorded")

    conn.commit()
    conn.close()

    # physically create cfg_change_detail (and any other missing data table) from cfg_column —
    # CREATE TABLE IF NOT EXISTS, so this is safe to call even though most tables already exist.
    dbmod.build()
    check = sqlite3.connect(DB_PATH)
    exists = check.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='cfg_change_detail'").fetchone()
    check.close()
    report.append(f"cfg_change_detail physical table: {'present' if exists else 'MISSING — check db.build()'}")

    print("configuration_maintenance bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
