"""bootstrap_book_narrative_validate.py — ONE-OFF, idempotent: registers `report.
book_narrative_validate` (structural presence check for the required "Scope self-check" section —
see `handlers/narrative.py` and `WA-inner-being-narrative-guidance-v1-2026-07-28.md`) as a real
dispatcher work package/step, matching `bootstrap_passage_debate_report.py`'s established pattern
— direct `cfg_*` inserts, not routed through `configmaint.propose` row-by-row, per the same
standing instruction that carve-out already relies on (GOVERNANCE.md §9B/§14).

Up-front design approval for this carve-out: the researcher's own request, 2026-07-28, immediately
after a real scope-narrowing was found and fixed in the Daniel narratives — "ensure that the
instructions are clear on this, and that the validation will catch it if it drifts."

Standalone, on-demand, like `passage-quality`/`passage.validate` (not chained into any narrative-
*writing* pipeline, because none is registered — narrative writing itself stays unmechanized
analytical work, per this module's own docstring and the guidance doc's §4).

    python -m iba.app.migration.bootstrap_book_narrative_validate
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

WP = "book-narrative-validate"
PS_SCRIPT = "iba/app/ps/BookNarrative-Validate.ps1"
STEP = "report.book_narrative_validate"
HANDLER = "iba.app.handlers.narrative:validate"
DOES = ("structural presence check on an inner-being narrative file — confirms a '## Scope "
       "self-check' section exists and all three required channel labels (non-human<->human, "
       "human<->human, physical world<->human) are present with non-empty content; a presence "
       "check only, not a judgment of citation quality or content accuracy — see "
       "WA-inner-being-narrative-guidance-v1-2026-07-28.md section 4")


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

    # New cfg_setting module ('narrative') must be a real enum.config_module value first —
    # configmaint.validate checks every cfg_setting.module against this enum (hard coherence
    # error, not advisory) — same gap bootstrap_passage_debate_report.py closed for 'method'.
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='narrative'"
                        ).fetchone():
        n = conn.execute("SELECT COALESCE(MAX(ordinal), -1) FROM cfg_enum WHERE "
                        "name='config_module'").fetchone()[0]
        conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) "
                    "VALUES ('config_module', 'narrative', ?, 0)", (n + 1,))
        report.append("cfg_enum (config_module, narrative) added")
    else:
        report.append("cfg_enum (config_module, narrative) already present")

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (WP,)).fetchone():
        conn.execute("INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
                    "complete_message, next_step_hint, paused_message, inactive) "
                    "VALUES (?,?,'none',0,NULL,NULL,NULL,0)", (WP, PS_SCRIPT))
        report.append(f"cfg_work_package {WP!r} added")
    else:
        report.append(f"cfg_work_package {WP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_step WHERE work_package=? AND step=?",
                        (WP, STEP)).fetchone():
        conn.execute("INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                    "inactive) VALUES (?,?,?,?,?,?,0)",
                     (WP, 0, STEP, HANDLER, "none", DOES))
        report.append(f"cfg_step {STEP!r} added")
    else:
        report.append(f"cfg_step {STEP!r} already present")

    _setting(conn, "method.inner_being_narrative_guidance_path",
             json.dumps("iba/docs/WA-inner-being-narrative-guidance-v1-2026-07-28.md"),
             "current version of the inner-being-narrative guidance (the three-channel scope "
             "requirement + the required Scope self-check section) — report.book_narrative_"
             "validate and any AI writing such a narrative must follow this exact file; bump this "
             "setting (not memory) when the guidance revises", "method", report)
    _setting(conn, "narrative.scope_check_report_path",
             json.dumps("iba/app/reports/book-narrative-scope-check.md"),
             "where report.book_narrative_validate persists its findings", "narrative", report)

    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (STEP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir, inactive) VALUES (?,?,1,NULL,'md','stable','archive',0)",
            (STEP, "Book-Narrative Scope Self-Check — {path}"))
        report.append(f"cfg_report {STEP!r} added")
    else:
        report.append(f"cfg_report {STEP!r} already present")

    if not conn.execute("SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                        (STEP, "findings")).fetchone():
        conn.execute(
            "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, toc_label, "
            "include, inactive) VALUES (?,?,?,?,?,1,0)",
            (STEP, 0, "findings", "## Findings", "Findings"))
        report.append(f"cfg_report_section ({STEP}, findings) added")
    else:
        report.append(f"cfg_report_section ({STEP}, findings) already present")

    _on_fail = [
        ("guidance-doc-missing", "report-stop",
         "method.inner_being_narrative_guidance_path points to a file that does not exist on "
         "disk — the config is stale relative to iba/docs/", "terminal"),
        ("no-path-given", "report-stop", "-Path is required — the narrative file to check",
         "terminal"),
        ("narrative-file-missing", "report-stop", "the given -Path does not exist on disk",
         "terminal"),
        ("scope-check-missing", "report-stop",
         "no '## Scope self-check' section found — add one per the guidance doc section 3",
         "terminal"),
        ("scope-check-incomplete", "report-stop",
         "one or more required channel labels are missing or left as an unfilled placeholder",
         "terminal"),
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

    print("book-narrative-validate bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
