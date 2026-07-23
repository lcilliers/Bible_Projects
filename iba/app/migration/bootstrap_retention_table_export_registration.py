"""bootstrap_retention_table_export_registration.py — ONE-OFF: Phase 0c of
PLAN-reports-config-governance-v1-20260722.md — register `log-retention` and `export_tables_csv`
as real dispatcher work packages/steps (found unregistered, standalone, in the §2C/§2A re-audit),
seed retention.report's cfg_report/cfg_report_section rows (deferred from 0a — cfg_report.step is a
real FK to cfg_step.step, which didn't exist for retention until this migration creates it), and
fix two confirmed bugs:

  - `candidate.load` wrote its report to a path DERIVED from `candidate.quality_report_path`'s
    parent dir, not a path setting of its own — it now gets `candidate.load_report_path`.
  - `export_tables_csv` dumped `cfg_*` tables too, duplicating `configmaint.report`/
    `CONFIG-REPORT.md` (the dedicated config report writer) — fixed in tools/export_tables_csv.py
    itself (table filter); this migration only adds `table_export.output_dir` so its own output
    location is config, matching every other report.

    python -m iba.app.migration.bootstrap_retention_table_export_registration
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _enum(conn, name, value, report):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?)", (name, value, n))
        report.append(f"cfg_enum {name} += {value!r}")
    else:
        report.append(f"cfg_enum {name} already has {value!r}")


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting VALUES (?,?,?,?)", (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def _work_package(conn, name, ps_script, report):
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained) "
                    "VALUES (?,?,'none',0)", (name, ps_script))
        report.append(f"cfg_work_package {name!r} added")
    else:
        report.append(f"cfg_work_package {name!r} already present")


def _step(conn, wp, ordinal, step, handler, does, report):
    existing = conn.execute(
        "SELECT handler FROM cfg_step WHERE work_package=? AND step=?", (wp, step)).fetchone()
    if not existing:
        conn.execute("INSERT INTO cfg_step VALUES (?,?,?,?,?,?)",
                     (wp, ordinal, step, handler, "none", does))
        report.append(f"cfg_step {step!r} added")
    elif existing[0] != handler:
        conn.execute("UPDATE cfg_step SET handler=? WHERE work_package=? AND step=?",
                    (handler, wp, step))
        report.append(f"cfg_step {step!r} handler corrected")
    else:
        report.append(f"cfg_step {step!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    # ── retention: register the work package + step ──
    _work_package(conn, "log-retention", "iba/app/ps/Log-Retention.ps1", report)
    _step(conn, "log-retention", 0, "retention.report",
         "iba.app.handlers.reports:retention_report",
         "run/escalation/validation_result log-retention & run-health report — read-only, "
         "no pruning", report)

    # ── table-export: register the work package + step ──
    _enum(conn, "config_module", "table_export", report)
    _work_package(conn, "table-export", "iba/app/ps/Export-Tables.ps1", report)
    _step(conn, "table-export", 0, "table.export",
         "iba.app.handlers.reports:table_export",
         "CSV dump of every data table, verbatim — excludes cfg_* (configmaint.report already "
         "owns that content)", report)
    _setting(conn, "table_export.output_dir", json.dumps("iba/app/export"),
             "where table.export writes its CSVs", "table_export", report)

    # ── retention.report's cfg_report/cfg_report_section (deferred from 0a — FK needed the step) ──
    if not conn.execute("SELECT 1 FROM cfg_report WHERE step='retention.report'").fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir) VALUES "
            "('retention.report','Log retention & run-health report',1,NULL,'md+csv','stable','archive')")
        report.append("cfg_report 'retention.report' added")
    else:
        report.append("cfg_report 'retention.report' already present")

    sections = [
        (0, "summary", "## Summary"),
        (1, "stuck_chained",
         "## Stuck chained runs (archival candidates — not relabelled; see lib/retention.py)"),
        (2, "open_escalations", "## Open escalations (oldest first)"),
        (3, "recent_failed", "## Recent failed runs (last 50)"),
    ]
    for ordinal, key, heading in sections:
        if not conn.execute(
                "SELECT 1 FROM cfg_report_section WHERE step='retention.report' AND section_key=?",
                (key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, toc_label, "
                "include) VALUES ('retention.report',?,?,?,?,1)",
                (ordinal, key, heading, heading.lstrip("# ").strip()))
            report.append(f"cfg_report_section (retention.report, {key}) added")
        else:
            report.append(f"cfg_report_section (retention.report, {key}) already present")

    for table_name in ("run", "escalation", "validation_result"):
        if not conn.execute(
                "SELECT 1 FROM cfg_report_csv_table WHERE step='retention.report' AND table_name=?",
                (table_name,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report_csv_table (step, table_name, join_note) VALUES "
                "('retention.report',?,NULL)", (table_name,))
            report.append(f"cfg_report_csv_table (retention.report, {table_name}) added")
        else:
            report.append(f"cfg_report_csv_table (retention.report, {table_name}) already present")

    # ── candidate.load: its own report-path setting (was derived from candidate.quality_report_path) ──
    _setting(conn, "candidate.load_report_path", json.dumps("iba/app/reports/candidate-load.md"),
            "where candidate.load persists its per-run duplicates/exceptions report", "candidate",
            report)

    conn.commit()
    conn.close()

    print("retention/table-export registration bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
