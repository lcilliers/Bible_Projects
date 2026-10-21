"""bootstrap_word_registry_span_report.py — ONE-OFF, idempotent: registers
`report.word_registry_span` as a real dispatcher work package/step, matching the established
pattern `bootstrap_verse_analysis_report.py`/`bootstrap_new_reports_phase1.py` used — direct
cfg_* inserts, not routed through `configmaint.propose` row-by-row, per the researcher's standing
instruction not to approve infrastructure registration one field at a time (GOVERNANCE.md,
"researcher's explicit instruction not to approve infrastructure registration row-by-row", first
applied `bootstrap_quality_validate_steps.py`). The researcher's own request (2026-08-09: "add this
report into the app as a standard report, define it in the configs, and ensure that it has a
powershell script to run the report") IS the up-front design approval this carve-out requires.

Word-scoped like `report.word`/`validation.word` (which share the `reports` work package), but
given its own work package + dedicated PS script rather than folded into `Reports.ps1` — it's a
distinct concern (registry -> Strong's -> parse-meaning -> span analysis, not the raw/validation
layer `reports` already covers) and files to its own new folder
(`iba/app/verse-analysis/word_registry/`), matching the one-script-per-standalone-report pattern
already used for `strong-meaning-report`/`span-analysis-report`/`schema-overview-report`.

    python -m iba.app.migration.bootstrap_word_registry_span_report
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

WP = "word-registry-span-report"
PS_SCRIPT = "iba/app/ps/WordRegistrySpan-Report.ps1"
STEP = "report.word_registry_span"
HANDLER = "iba.app.handlers.reports:word_registry_span_report"
DOES = ("word_registry : word_strong : strong : strong_meaning_parsed : verse_lexical : span "
       "analysis, for one registry word — every linked Strong's with its parse-meaning breakdown "
       "and unique surface-span applications (with an example verse) — read-only")

_SECTIONS = [
    ("overview", "## Overview"),
    ("strongs", "## Linked Strong's — parse meaning & span analysis"),
]


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting (key, value, use, module) VALUES (?,?,?,?)",
                    (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (WP,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained) "
                    "VALUES (?,?,'word',0)", (WP, PS_SCRIPT))
        report.append(f"cfg_work_package {WP!r} added")
    else:
        report.append(f"cfg_work_package {WP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (WP, STEP)).fetchone():
        conn.execute("INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                    "kind) VALUES (?,?,?,?,?,?,?)",
                     (WP, 0, STEP, HANDLER, "word", DOES, "utility"))
        report.append(f"cfg_step {STEP!r} added")
    else:
        report.append(f"cfg_step {STEP!r} already present")

    _setting(conn, "report.word_registry_span_output_dir",
             json.dumps("iba/app/verse-analysis/word_registry"),
             "base folder for report.word_registry_span output — one file per registry word",
             "report", report)

    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (STEP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir) VALUES (?,?,1,NULL,'md','dated','archive')",
            (STEP, "{word} — linked Strong's, parse meaning, span analysis"))
        report.append(f"cfg_report {STEP!r} added")
    else:
        report.append(f"cfg_report {STEP!r} already present")

    for ordinal, (key, heading) in enumerate(_SECTIONS):
        if not conn.execute("SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                            (STEP, key)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                "toc_label, include) VALUES (?,?,?,?,?,1)",
                (STEP, ordinal, key, heading, heading.lstrip("# ").strip()))
            report.append(f"cfg_report_section ({STEP}, {key}) added")
        else:
            report.append(f"cfg_report_section ({STEP}, {key}) already present")

    if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?",
                        (STEP, "word-not-found")).fetchone():
        conn.execute(
            "INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, inactive) "
            "VALUES (?,?,?,?,?,?,0)",
            (STEP, "word-not-found", "report-stop", None,
             "the requested word is not in the registry", "terminal"))
        report.append(f"cfg_on_fail ({STEP}, word-not-found) added")
    else:
        report.append(f"cfg_on_fail ({STEP}, word-not-found) already present")

    conn.commit()
    conn.close()

    print("word-registry-span-report bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
