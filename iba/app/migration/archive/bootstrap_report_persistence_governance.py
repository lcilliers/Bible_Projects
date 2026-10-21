"""bootstrap_report_persistence_governance.py — ONE-OFF: codify the "every output must persist to
a report, not just terminal/escalation" standard as a real, code-backed cfg_setting + the
report-path settings candidate.validate/passage.validate now need.

Researcher's ruling (2026-07-21): "should you fix it? why ask? why is there a standard if you
don't follow it - obviously it must be fixed. Errors is not optional to fix it. you can add this
as a app config in settings so you do not have to ask me again for should I fix an error." This is
that config — governance.reports_must_persist states the rule; handlers/configmaint.py's
_validate_live (via lib/cfgquality.find_missing_report_paths) actually enforces it, so it's a real
rule, not a decorative one. Batch/direct, same class of exception as the other bootstrap_*.py
scripts (see bootstrap_quality_validate_steps.py's docstring for why).

    python -m iba.app.migration.bootstrap_report_persistence_governance
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if not conn.execute(
            "SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='governance'").fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name='config_module'").fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES ('config_module','governance',?)", (n,))
        report.append("cfg_enum config_module += 'governance'")
    else:
        report.append("cfg_enum config_module already has 'governance'")

    settings = [
        ("governance.reports_must_persist",
         json.dumps("every quality-check or report-producing step must persist its output to a "
                   "config-defined report path — a terminal print + an escalation row is not "
                   "sufficient; enforced by lib/cfgquality.find_missing_report_paths, checked in "
                   "configmaint.validate"),
         "the researcher's 2026-07-21 standard: deviations are bugs, not judgement calls — fix, "
         "don't ask", "governance"),
        ("candidate.quality_report_path", json.dumps("iba/app/reports/candidate-quality.md"),
         "where candidate.validate persists its findings", "candidate"),
        ("passage.quality_report_path", json.dumps("iba/app/reports/passage-quality.md"),
         "where passage.validate persists its findings", "passage"),
    ]
    for key, value, use, module in settings:
        if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
            conn.execute("INSERT INTO cfg_setting VALUES (?,?,?,?)", (key, value, use, module))
            report.append(f"cfg_setting {key!r} added")
        else:
            report.append(f"cfg_setting {key!r} already present")

    conn.commit()
    conn.close()

    print("report-persistence-governance bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
