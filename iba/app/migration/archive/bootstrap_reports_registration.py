"""bootstrap_reports_registration.py — ONE-OFF: register report.py / validation.py as a proper
work package, and add the config that defines each report's output location and content.

Phase 2 of the 2026-07-21 session: "add configs to every place where a output/report need to be
generated, and add configs that define the content of the report." report.py already had partial
content config (report.span_fields etc.); this closes the rest — output paths for both modules,
and section-inclusion toggles for validation.py, which had NONE before this. Batch/direct, same
class of exception as the other bootstrap_*.py scripts (registers machinery, not routed through
configmaint.propose — see bootstrap_quality_validate_steps.py's docstring for why).

    python -m iba.app.migration.bootstrap_reports_registration
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    # ── 'validation' module needs adding to config_module (report/candidate/etc already exist) ──
    if not conn.execute(
            "SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='validation'").fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES ('config_module','validation',?)", (n,))
        report.append("cfg_enum config_module += 'validation'")
    else:
        report.append("cfg_enum config_module already has 'validation'")

    # ── work package + steps ──
    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name='reports'").fetchone():
        conn.execute("INSERT INTO cfg_work_package VALUES ('reports','Reports.ps1','none')")
        report.append("cfg_work_package 'reports' added")
    else:
        report.append("cfg_work_package 'reports' already present")

    steps = [
        (0, "report.word", "iba.app.handlers.reports:word_report", "word",
         "the word-raw report (report.py) — content governed by report.* settings"),
        (1, "validation.word", "iba.app.handlers.reports:validation_word", "word",
         "the raw-layer validation report (validation.py) — sections governed by validation.show_*"),
        (2, "validation.book", "iba.app.handlers.reports:validation_book", "book",
         "the base-layer validation report (validation.py) — sections governed by validation.show_*"),
    ]
    for ordinal, step, handler, scope, does in steps:
        existing = conn.execute(
            "SELECT handler FROM cfg_step WHERE work_package='reports' AND step=?", (step,)).fetchone()
        if not existing:
            conn.execute("INSERT INTO cfg_step VALUES (?,?,?,?,?,?)",
                         ("reports", ordinal, step, handler, scope, does))
            report.append(f"cfg_step {step!r} added")
        elif existing[0] != handler:
            conn.execute("UPDATE cfg_step SET handler=? WHERE work_package='reports' AND step=?",
                        (handler, step))
            report.append(f"cfg_step {step!r} handler corrected")
        else:
            report.append(f"cfg_step {step!r} already present")

    if not conn.execute(
            "SELECT 1 FROM cfg_on_fail WHERE step='report.word' AND condition='word-not-found'").fetchone():
        conn.execute("INSERT INTO cfg_on_fail VALUES (?,?,?,?,?)",
                     ("report.word", "word-not-found", "report-stop", None,
                      "the requested word is not in the registry"))
        report.append("cfg_on_fail (report.word, word-not-found) -> report-stop added")
    else:
        report.append("cfg_on_fail (report.word, word-not-found) already present")

    # ── content/output config ──
    settings = [
        ("report.output_dir", json.dumps("iba/app"), "where report.word writes its output", "report"),
        ("report.output_pattern", json.dumps("report-{word}.md"),
         "filename pattern for report.word's output ({word} substituted)", "report"),
        ("validation.output_dir", json.dumps("iba/app/reports"),
         "where validation.word/validation.book write their output", "validation"),
        ("validation.show_health", json.dumps(True),
         "word/book report: include the App & DB health section", "validation"),
        ("validation.show_delta", json.dumps(True),
         "word report: include the pre/post run-delta section", "validation"),
        ("validation.show_integrity", json.dumps(True),
         "word report: include the config-derived integrity section", "validation"),
        ("validation.show_references", json.dumps(True),
         "word report: include the FK-resolvability section", "validation"),
        ("validation.show_expectations", json.dumps(True),
         "word report: include the semantic-expectations section", "validation"),
        ("validation.show_candidate", json.dumps(True),
         "book report: include the candidate (L4b) section", "validation"),
        ("validation.show_passages", json.dumps(True),
         "book report: include the passages section", "validation"),
    ]
    for key, value, use, module in settings:
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
            conn.execute("INSERT INTO cfg_setting VALUES (?,?,?,?)", (key, value, use, module))
            report.append(f"cfg_setting {key!r} added")
        else:
            report.append(f"cfg_setting {key!r} already present")

    conn.commit()
    conn.close()

    print("reports-registration bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
