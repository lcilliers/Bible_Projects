"""bootstrap_whole_book_read.py — ONE-OFF, idempotent: registers `report.whole_book_read` (the
whole-book-read gathering report — see `lib/wholebookread.py`) as a real dispatcher work
package/step, matching the established pattern `bootstrap_passage_debate_report.py` used for
`report.passage_debate` — direct `cfg_*` inserts, not routed through `configmaint.propose`
row-by-row, per the same standing instruction not to approve infrastructure registration one field
at a time that justified that precedent (GOVERNANCE.md §9B/§14).

Up-front design approval for this carve-out: the plan approved 2026-07-28
(~/.claude/plans/twinkly-orbiting-dawn.md, Phase 3), written and approved specifically because
every one of Daniel's sixteen passage-debates defers its emergent questions to "the whole-book
read" and no such step existed anywhere in `cfg_work_package` for them to land in.

    python -m iba.app.migration.bootstrap_whole_book_read
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

WP = "whole-book-read"
PS_SCRIPT = "iba/app/ps/WholeBookRead-Report.ps1"
STEP = "report.whole_book_read"
HANDLER = "iba.app.handlers.reports:whole_book_read_report"
DOES = ("whole-book-read gathering report — for a book whose passage debates are (wholly or "
       "partly) filled, pulls every debate_status='filled' passage row in reading order, reads "
       "each debate file, extracts its Emergent-questions and Passage-level-linkages sections "
       "(tolerant heading match, explicit NOT-FOUND if a file's headings don't match), and lays "
       "them out per-passage with an empty Resolution slot for the researcher/AI to fill in; does "
       "not decide how any emergent question actually resolves itself")

_SECTIONS = [
    ("coverage", "## Coverage"),
    ("carried_forward", "## Carried forward per passage"),
    ("not_found", "## Sections not found — verify heading"),
    ("closing", "## Closing synthesis"),
]


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting (key, value, use, module, inactive) "
                    "VALUES (?,?,?,?,0)", (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (WP,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
                    "complete_message, next_step_hint, paused_message, inactive) "
                    "VALUES (?,?,'book',0,NULL,NULL,NULL,0)", (WP, PS_SCRIPT))
        report.append(f"cfg_work_package {WP!r} added")
    else:
        report.append(f"cfg_work_package {WP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (WP, STEP)).fetchone():
        conn.execute("INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                    "inactive) VALUES (?,?,?,?,?,?,0)",
                     (WP, 0, STEP, HANDLER, "book", DOES))
        report.append(f"cfg_step {STEP!r} added")
    else:
        report.append(f"cfg_step {STEP!r} already present")

    # Output location reuses report.verse_analysis_output_dir (same book folder as the debates
    # themselves) — only the naming pattern is new.
    _setting(conn, "report.whole_book_read_naming_pattern",
             json.dumps("WA-{book}-whole-book-read.md"),
             "filename pattern for report.whole_book_read ({book} substituted); stable scheme — "
             "reportkit archives the prior version on regenerate, same convention "
             "report.passage_debate_naming_pattern already uses", "report", report)

    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (STEP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir, inactive) VALUES (?,?,1,NULL,'md','stable','archive',0)",
            (STEP, "{book} -- Whole-Book Read"))
        report.append(f"cfg_report {STEP!r} added")
    else:
        report.append(f"cfg_report {STEP!r} already present")

    for ordinal, (key, heading) in enumerate(_SECTIONS):
        if not conn.execute("SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                            (STEP, key)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                "toc_label, include, inactive) VALUES (?,?,?,?,?,1,0)",
                (STEP, ordinal, key, heading, heading.lstrip("# ").strip()))
            report.append(f"cfg_report_section ({STEP}, {key}) added")
        else:
            report.append(f"cfg_report_section ({STEP}, {key}) already present")

    _on_fail = [
        ("no-debates-found", "report-stop",
         "no debate_status='filled' passage row exists yet for this book — run at least one "
         "report.passage_debate pass and fill it in first", "terminal"),
    ]
    for condition, path, message, route in _on_fail:
        if not conn.execute("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?",
                            (STEP, condition)).fetchone():
            conn.execute(
                "INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, "
                "inactive) VALUES (?,?,?,?,?,?,0)",
                (STEP, condition, path, None, message, route))
            report.append(f"cfg_on_fail ({STEP}, {condition}) added")
        else:
            report.append(f"cfg_on_fail ({STEP}, {condition}) already present")

    conn.commit()
    conn.close()

    print("whole-book-read bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
