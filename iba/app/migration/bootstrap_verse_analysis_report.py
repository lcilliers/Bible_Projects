"""bootstrap_verse_analysis_report.py — ONE-OFF, idempotent: registers `report.verse_span_meaning`
as a real dispatcher work package/step, matching the established pattern
`bootstrap_new_reports_phase1.py` used for the 4 new reports (BUILD.md §17/GOVERNANCE.md §14) —
direct cfg_* inserts, not routed through `configmaint.propose` row-by-row, per the researcher's
standing instruction not to approve infrastructure registration one field at a time (GOVERNANCE.md
§9B). The researcher's own request (2026-07-26: new verse-analysis folder, book-subfoldered, report
config-driven, "included in the app") IS the up-front design approval this carve-out requires.

Unlike the 4 phase-1 reports, this one is STEP-dependent (AMBIGUOUS-span live disambiguation), so it
also needs a `cfg_on_fail` row for the 'unreachable' condition — mirrors `lexicon.related`'s existing
row exactly (report-stop / terminal, not a crash).

    python -m iba.app.migration.bootstrap_verse_analysis_report
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

WP = "verse-analysis-report"
PS_SCRIPT = "iba/app/ps/VerseSpanMeaning-Report.ps1"
STEP = "report.verse_span_meaning"
HANDLER = "iba.app.handlers.reports:verse_span_meaning_report"
DOES = ("verse : span : meaning extract for a book/chapter-range — per-span meaning from all "
       "three parse tables (meaning_tree/lsj/mounce), live STEP disambiguation for AMBIGUOUS "
       "(sibling-shared-base) spans")

_SECTIONS = [
    ("coverage", "## Meaning coverage (non-particle spans, this range)"),
    ("verses", "## Verses"),
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
                    "VALUES (?,?,'book',0)", (WP, PS_SCRIPT))
        report.append(f"cfg_work_package {WP!r} added")
    else:
        report.append(f"cfg_work_package {WP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (WP, STEP)).fetchone():
        conn.execute("INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does) "
                    "VALUES (?,?,?,?,?,?)",
                     (WP, 0, STEP, HANDLER, "book", DOES))
        report.append(f"cfg_step {STEP!r} added")
    else:
        report.append(f"cfg_step {STEP!r} already present")

    _setting(conn, "report.verse_analysis_output_dir", json.dumps("iba/app/verse-analysis"),
             "base folder for report.verse_span_meaning, sub-foldered per book at write time",
             "report", report)
    _setting(conn, "report.verse_analysis_output_pattern",
             json.dumps("{book}-{range}-verse-span-meaning.md"),
             "filename pattern for report.verse_span_meaning ({book}/{range} substituted)",
             "report", report)

    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (STEP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir) VALUES (?,?,1,NULL,'md','stable','archive')",
            (STEP, "{book} {range} -- verse : span : meaning extract"))
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
                        (STEP, "unreachable")).fetchone():
        conn.execute(
            "INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, inactive) "
            "VALUES (?,?,?,?,?,?,0)",
            (STEP, "unreachable", "report-stop", None,
             "STEP is not reachable — report.verse_span_meaning needs it for AMBIGUOUS-span "
             "disambiguation (step.required_for_runs)", "terminal"))
        report.append(f"cfg_on_fail ({STEP}, unreachable) added")
    else:
        report.append(f"cfg_on_fail ({STEP}, unreachable) already present")

    conn.commit()
    conn.close()

    print("verse-analysis-report bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
