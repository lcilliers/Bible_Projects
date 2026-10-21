"""bootstrap_catalogue_overview_report_v1_20260829.py — ONE-OFF: escalation #1007 second half,
registers the `catalogue-report` work package/step + `report.obs_catalogue` config
(cfg_setting/cfg_report/cfg_report_section) and the `cataloguereport.py` utility, following the
exact idempotent pattern `bootstrap_new_reports_phase1.py` established.

**Corrected same-day, researcher direct instruction (BUILD.md §208 addendum):** the report path
was originally `iba/app/reports/obs-catalogue.md` — "iba/app/reports is not an approved or valid
destination" for this report; it belongs alongside the rest of the observation-question-catalogue
material at `Workflow/Catalogue/` (already an established directory, CLAUDE.md §2). Also originally
registered a `cfg_report_csv_table` row + `output_kind='md+csv'` — dropped: a verbatim
`wa_obs_question_catalogue` CSV dump already exists via the governed `table.export` mechanism
(`table_export.output_dir` → `Workflow/schema/bible_research/`, BUILD.md §201); this report never
needed its own second copy. Both corrections are live in the constants/logic below — this is the
form a fresh apply now produces, not the form actually run first (see BUILD.md §208 for the as-run
sequence and escalation #1052 for the coherence bug the first pass also introduced and self-fixed).

    python -m iba.app.migration.bootstrap_catalogue_overview_report_v1_20260829
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_STEP = "report.obs_catalogue"
_WP = "catalogue-report"
_PATH_KEY = "report.obs_catalogue_path"
_PATH_DEFAULT = "Workflow/Catalogue/obs-catalogue.md"

_SECTIONS = [
    ("overview", "## Overview — lifecycle breakdown"),
    ("lifecycle_conflicts", "## Lifecycle conflicts (status vs deleted)"),
    ("naming_schemes", "## Naming schemes and format inconsistencies"),
    ("tier_structure", "## Tier structure — live, tiered questions"),
    ("unclassified", "## Unclassified — live questions with no tier"),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (_WP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained) VALUES (?,?,'none',0)",
            (_WP, "iba/app/ps/Catalogue-Report.ps1"))
        report.append(f"cfg_work_package {_WP!r} added")
    else:
        report.append(f"cfg_work_package {_WP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (_WP, _STEP)).fetchone():
        conn.execute(
            "INSERT INTO cfg_step VALUES (?,?,?,?,?,?,?,?)",
            (_WP, 0, _STEP, "iba.app.handlers.reports:obs_catalogue_report", "none",
             "structural review of wa_obs_question_catalogue (bible_research.db) on its own -- "
             "no join to finding/finding_question_link -- status/deleted lifecycle conflicts, "
             "section/tier/question_code/catalogue_version/date_added naming inconsistencies, "
             "the live tiered question set for review, and untiered integration candidates",
             0, "utility"))
        report.append(f"cfg_step {_STEP!r} added")
    else:
        report.append(f"cfg_step {_STEP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (_PATH_KEY,)).fetchone():
        conn.execute("INSERT INTO cfg_setting VALUES (?,?,?,?,?)",
                    (_PATH_KEY, json.dumps(_PATH_DEFAULT),
                     f"where {_STEP} persists its output", "report", 0))
        report.append(f"cfg_setting {_PATH_KEY!r} added")
    else:
        report.append(f"cfg_setting {_PATH_KEY!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (_STEP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir) VALUES (?,?,1,NULL,'md','stable','archive')",
            (_STEP, "Observation question catalogue — structural review"))
        report.append(f"cfg_report {_STEP!r} added")
    else:
        report.append(f"cfg_report {_STEP!r} already present")

    for ordinal, (key, heading) in enumerate(_SECTIONS):
        if not conn.execute("SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                           (_STEP, key)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, toc_label, "
                "include) VALUES (?,?,?,?,?,1)",
                (_STEP, ordinal, key, heading, heading.lstrip("# ").strip()))
            report.append(f"cfg_report_section ({_STEP}, {key}) added")
        else:
            report.append(f"cfg_report_section ({_STEP}, {key}) already present")

    # No cfg_report_csv_table row -- a verbatim wa_obs_question_catalogue CSV already exists via
    # the governed table.export mechanism (table_export.output_dir -> Workflow/schema/
    # bible_research/), so this report doesn't register its own second CSV destination.

    if not conn.execute("SELECT 1 FROM cfg_utility WHERE file_path=?",
                        ("iba/app/lib/cataloguereport.py",)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
            "VALUES (?,?,?,0,0)",
            ("cataloguereport", "iba/app/lib/cataloguereport.py",
             f"{_STEP} -- wa_obs_question_catalogue structural review, no findings joins"))
        report.append("cfg_utility cataloguereport.py added")
    else:
        report.append("cfg_utility cataloguereport.py already present")

    _self_path = "iba/app/migration/bootstrap_catalogue_overview_report_v1_20260829.py"
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE file_path=?", (_self_path,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt) "
            "VALUES (?,?,?,1,0)",
            ("bootstrap_catalogue_overview_report_v1_20260829", _self_path,
             "ONE-OFF migration, escalation #1007 -- registers the catalogue-report work "
             "package/step, report.obs_catalogue config, and the cataloguereport.py utility. "
             "inactive=1 once applied -- a one-off, not a reusable routine."))
        report.append(f"cfg_utility (self) {_self_path!r} added")
    else:
        report.append(f"cfg_utility (self) {_self_path!r} already present")

    conn.commit()
    conn.close()

    print("catalogue-overview-report bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
