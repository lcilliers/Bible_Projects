"""bootstrap_new_reports_phase1.py — ONE-OFF: Phase 1 of
PLAN-reports-config-governance-v1-20260722.md — register the 4 new reports (§3.1-3.4) as real
dispatcher work packages/steps and seed their cfg_report/cfg_report_section/cfg_report_csv_table
rows, built entirely on the Phase-0 scaffolding (lib/reportkit.py) — unlike the original 8 reports,
these were never hardcoded Python headings first; they start config-governed.

    python -m iba.app.migration.bootstrap_new_reports_phase1
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH


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


def _step(conn, wp, step, handler, does, report):
    existing = conn.execute(
        "SELECT handler FROM cfg_step WHERE work_package=? AND step=?", (wp, step)).fetchone()
    if not existing:
        conn.execute("INSERT INTO cfg_step VALUES (?,?,?,?,?,?)",
                     (wp, 0, step, handler, "none", does))
        report.append(f"cfg_step {step!r} added")
    else:
        report.append(f"cfg_step {step!r} already present")


# (work_package, ps_script, step, handler, does, path_setting, path_default, cfg_report title,
#  sections[(key, heading)], csv_tables[(table, join_note)])
_REPORTS = [
    ("seed-candidate-report", "iba/app/ps/SeedCandidate-Report.ps1", "report.seed_candidate",
     "iba.app.handlers.reports:seed_candidate_report",
     "whole-seed candidate_seed analysis — counts by decision/layer/role, tag/lemma "
     "distribution, busiest lemmas, open-vs-resolved over time",
     "report.seed_candidate_path", "iba/app/reports/seed-candidate.md",
     "Seed-candidate report", [
        ("summary", "## Summary"),
        ("distribution", "## Distribution — tag length and rows per lemma"),
        ("top_lemmas", "## Top lemmas by candidate-row count"),
        ("over_time", "## Open vs resolved over time"),
     ], [
        ("candidate_seed", "joined to lemma_inventory.gloss"),
     ]),
    ("strong-meaning-report", "iba/app/ps/StrongMeaning-Report.ps1", "report.strong_meaning",
     "iba.app.handlers.reports:strong_meaning_report",
     "meaning-parse layer coverage — strong/strong_sense/strong_meaning_tree/strong_lexicon "
     "gap list, sense-count distribution, lexicon completeness",
     "report.strong_meaning_path", "iba/app/reports/strong-meaning.md",
     "Strong-meaning report", [
        ("gap_list", "## strong rows with no strong_sense yet (by usage count)"),
        ("sense_distribution", "## Sense-count distribution (strong_meaning_tree)"),
        ("lexicon_completeness", "## Lexicon completeness (lsj / mounce)"),
     ], [
        ("strong_sense", "joined to strong.stepGloss"),
        ("strong_meaning_tree", "joined to strong.stepGloss via lemma_key"),
     ]),
    ("span-analysis-report", "iba/app/ps/SpanAnalysis-Report.ps1", "report.span_analysis",
     "iba.app.handlers.reports:span_analysis_report",
     "span layer coverage per book, confirmed (span) vs candidate (span_candidate) counts, "
     "morph-code distribution",
     "report.span_analysis_path", "iba/app/reports/span-analysis.md",
     "Span-analysis report", [
        ("by_book", "## Coverage by book"),
        ("morph_distribution", "## morph_code distribution"),
        ("particle_split", "## Particle vs non-particle spans"),
     ], [
        ("span", None),
        ("span_candidate", None),
     ]),
    ("schema-overview-report", "iba/app/ps/SchemaOverview-Report.ps1", "report.schema_overview",
     "iba.app.handlers.reports:schema_overview_report",
     "the IBA app's own data-schema snapshot — every data table, columns, types, PK/FK, "
     "indexes, row counts",
     "report.schema_overview_path", "iba/app/reports/schema-overview.md",
     "Schema overview", [
        ("overview", "## Table inventory"),
        ("tables", "## Every data table, in full"),
     ], []),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    for (wp, ps_script, step, handler, does, path_key, path_default, title, sections,
        csv_tables) in _REPORTS:
        _work_package(conn, wp, ps_script, report)
        _step(conn, wp, step, handler, does, report)
        _setting(conn, path_key, json.dumps(path_default),
                f"where {step} persists its output", "report", report)

        if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (step,)).fetchone():
            output_kind = "md+csv" if csv_tables else "md"
            conn.execute(
                "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                "naming_scheme, archive_dir) VALUES (?,?,1,NULL,?,'stable','archive')",
                (step, title, output_kind))
            report.append(f"cfg_report {step!r} added")
        else:
            report.append(f"cfg_report {step!r} already present")

        for ordinal, (key, heading) in enumerate(sections):
            if not conn.execute(
                    "SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                    (step, key)).fetchone():
                conn.execute(
                    "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                    "toc_label, include) VALUES (?,?,?,?,?,1)",
                    (step, ordinal, key, heading, heading.lstrip("# ").strip()))
                report.append(f"cfg_report_section ({step}, {key}) added")
            else:
                report.append(f"cfg_report_section ({step}, {key}) already present")

        for table_name, join_note in csv_tables:
            if not conn.execute(
                    "SELECT 1 FROM cfg_report_csv_table WHERE step=? AND table_name=?",
                    (step, table_name)).fetchone():
                conn.execute(
                    "INSERT INTO cfg_report_csv_table (step, table_name, join_note) VALUES "
                    "(?,?,?)", (step, table_name, join_note))
                report.append(f"cfg_report_csv_table ({step}, {table_name}) added")
            else:
                report.append(f"cfg_report_csv_table ({step}, {table_name}) already present")

    conn.commit()
    conn.close()

    print("new-reports-phase1 bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
