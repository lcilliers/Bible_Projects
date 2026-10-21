"""bootstrap_book_narrative_generate.py — ONE-OFF, idempotent: registers `report.
book_narrative_generate` (assembles a book's filled passage debates + the two governing narrative
docs, calls the Anthropic Messages API, files the result) as a real dispatcher work package/step,
matching `bootstrap_book_narrative_validate.py`'s established carve-out — direct `cfg_*` inserts,
not routed through `configmaint.propose` row-by-row (GOVERNANCE.md §9B/§14).

Built on direct researcher instruction, 2026-07-30: a PowerShell script (matching every other app
process) that assembles a book's debates, supplies the governing instructions, and calls the API,
so the package submitted is consistent every time — see `lib/narrativegenerate.py`'s module
docstring for the full design, and the researcher's own follow-up instruction the same day that
report content/defaults, narrative style, and file naming/filing must all be config-driven, not
hard-coded — hence the full settings list below rather than literals in the handler.

    python -m iba.app.migration.bootstrap_book_narrative_generate
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

WP = "book-narrative-generate"
PS_SCRIPT = "iba/app/ps/BookNarrative-Generate.ps1"
STEP = "report.book_narrative_generate"
HANDLER = "iba.app.handlers.narrative:generate"
DOES = ("assembles every filled report.passage_debate output for a book plus the hard-constraints "
       "and three-channel guidance docs, submits the package to the Anthropic Messages API "
       "(researcher approval required first, pause-continue on the estimated cost), and files the "
       "returned narrative under report.verse_analysis_output_dir/<book_label>/ — see "
       "lib/narrativegenerate.py")


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

    # 'narrative' is already a real config_module (bootstrap_book_narrative_validate.py added it).

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (WP,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
                    "complete_message, next_step_hint, paused_message, inactive) "
                    "VALUES (?,?,'book',0,?,?,?,0)",
                     (WP, PS_SCRIPT,
                      "Narrative written — run BookNarrative-Validate.ps1 on it next.",
                      "iba\\app\\ps\\BookNarrative-Validate.ps1 -Path <the narrative file>",
                      "Estimated cost/token count printed above — answer the escalation "
                      "(Approve/Reject/Revise) then re-run this exact command to make the live "
                      "API call."))
        report.append(f"cfg_work_package {WP!r} added")
    else:
        report.append(f"cfg_work_package {WP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (WP, STEP)).fetchone():
        conn.execute("INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                    "inactive, kind) VALUES (?,?,?,?,?,?,0,?)",
                     (WP, 0, STEP, HANDLER, "book", DOES, "operations"))
        report.append(f"cfg_step {STEP!r} added")
    else:
        report.append(f"cfg_step {STEP!r} already present")

    _setting(conn, "method.narrative_hard_constraints_path",
             json.dumps("iba/docs/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md"),
             "current version of the book-agnostic hard constraints (nothing invented, open "
             "threads stay open, no forced unity, plain language, no self-reference) every "
             "generated narrative must follow — bump this setting (not memory) when the doc "
             "revises", "narrative", report)
    _setting(conn, "narrative.generate_model", json.dumps("claude-sonnet-5"),
             "the Anthropic model narrative.generate submits the package to", "narrative", report)
    _setting(conn, "narrative.generate_max_output_tokens", json.dumps(16000),
             "max_tokens on the Messages API call — the ceiling on how long the generated "
             "narrative can be", "narrative", report)
    _setting(conn, "narrative.generate_max_cost", json.dumps(3.00),
             "USD cost cap (from the pre-call ESTIMATE) — over this, report.book_narrative_"
             "generate refuses outright (cost-cap-exceeded) rather than pausing for approval; "
             "raise it deliberately for a book large enough to need it", "narrative", report)
    _setting(conn, "narrative.rate_input_per_million", json.dumps(3.00),
             "USD per million input tokens, at narrative.generate_model's current rate — used for "
             "both the pre-call estimate and the real post-call cost; edit if the model default "
             "changes to a different price tier", "narrative", report)
    _setting(conn, "narrative.rate_output_per_million", json.dumps(15.00),
             "USD per million output tokens, at narrative.generate_model's current rate", "narrative",
             report)
    _setting(conn, "narrative.output_pattern", json.dumps("WA-{book}-inner-being-narrative.md"),
             "filename pattern for the generated narrative, written under report.verse_analysis_"
             "output_dir/<book_label>/ — same folder its source debates live in", "narrative",
             report)
    _setting(conn, "narrative.usage_log_path",
             json.dumps("iba/app/reports/export/narrative-generate-usage.csv"),
             "append-only on-disk ledger of every LIVE call's real tokens/cost — scripts/"
             "cost_ledger.py (repo root) only ingests Console CSV exports, not this app's own "
             "calls, so this is the audit trail for those", "narrative", report)

    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", ("narrativegenerate",)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "config_exempt_reason) VALUES (?,?,?,0,0,NULL)",
            ("narrativegenerate", "iba/app/lib/narrativegenerate.py",
             "report.book_narrative_generate's assembly (debates + governing docs), cost "
             "estimate/cap, Anthropic Messages API call, and narrative filing"))
        report.append("cfg_utility 'narrativegenerate' added")
    else:
        report.append("cfg_utility 'narrativegenerate' already present")

    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (STEP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir, inactive) VALUES (?,?,0,?,'md','stable','archive',0)",
            (STEP, "{book_label} — Inner-Being Narrative",
             "*Generated by `report.book_narrative_generate` from the book's filled passage "
             "debates — see `WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` and "
             "`WA-inner-being-narrative-guidance-v1-2026-07-28.md` for the governing "
             "instructions. Run `BookNarrative-Validate.ps1` against this file next.*"))
        report.append(f"cfg_report {STEP!r} added")
    else:
        report.append(f"cfg_report {STEP!r} already present")

    _on_fail = [
        ("no-debates-found", "report-stop",
         "no filled report.passage_debate exists yet for this book", "terminal"),
        ("guidance-doc-missing", "report-stop",
         "a method.* cfg_setting points to a file that does not exist on disk", "terminal"),
        ("cost-cap-exceeded", "report-stop",
         "the pre-call cost estimate exceeds narrative.generate_max_cost", "terminal"),
        ("needs-approval", "pause-continue",
         "researcher approval required before the live API call is made", "terminal"),
        ("declined", "report-stop", "researcher rejected the escalation", "terminal"),
        ("needs-revision", "report-stop", "researcher asked for a change first (see comment)",
         "terminal"),
        ("api-key-missing", "report-stop",
         "ANTHROPIC_API_KEY not found in the environment or repo-root .env", "terminal"),
        ("api-error", "report-stop", "the Messages API returned a non-2xx response", "terminal"),
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

    print("book-narrative-generate bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
