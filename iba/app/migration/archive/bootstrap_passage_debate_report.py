"""bootstrap_passage_debate_report.py — ONE-OFF, idempotent: registers `report.passage_debate`
(the passage-debate SCAFFOLD generator — see `lib/passagedebatereport.py`) as a real dispatcher
work package/step, matching the established pattern `bootstrap_verse_analysis_report.py` used for
`report.verse_span_meaning` — direct `cfg_*` inserts, not routed through `configmaint.propose`
row-by-row, per the researcher's standing instruction not to approve infrastructure registration
one field at a time (GOVERNANCE.md §9B/§14). The researcher's own request (2026-07-27: "bake in
the analysis/debate process as part of the app... create all the config items... define the
report format, destination, naming, and content in the config... create the leading PS... ensure
all the other requirements... for incorporating a new method") IS the up-front design approval
this carve-out requires.

Two NEW `cfg_setting` rows use a new module, `method` — the current version of each governing
method doc (`WA-passage-read-guidance`, `WA-interpretation-questions`), config-driven rather than
a citation an AI has to remember or a debate's own front-matter asserting a version number that
was never actually bumped on disk. That gap (every pre-registration debate cited a "v1.1" read
guidance that did not exist as a file) is exactly what `governance.rules_must_be_config_driven`
(GOVERNANCE.md §16) exists to close.

    python -m iba.app.migration.bootstrap_passage_debate_report
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

WP = "passage-debate-report"
PS_SCRIPT = "iba/app/ps/PassageDebate-Report.ps1"
STEP = "report.passage_debate"
HANDLER = "iba.app.handlers.reports:passage_debate_report"
DOES = ("passage-debate scaffold generator — verifies the base verse-span-meaning extract and "
       "the current method docs (method.passage_read_guidance_path / "
       "method.interpretation_questions_path) exist, resolves output path/naming, and writes a "
       "debate-document SKELETON (front-matter, per-verse Observation/Operation/Subject-Source-"
       "Target/Interrogative/Decision placeholders, standard closing sections) for the "
       "researcher/AI to fill in; does not generate interpretive content itself")

_SECTIONS = [
    ("preliminaries", "## Preliminaries"),
    ("verses", "## Per-verse debate"),
    ("linkages", "## Passage-level linkages (Q7)"),
    ("insufficiencies", "## Insufficiencies register"),
    ("emergent", "## Emergent questions log (filed against this passage — not merged across "
                "passages; resolved, if at all, at the whole-book read)"),
    ("open_decisions", "## Open decisions / next steps"),
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

    # New cfg_setting module ('method') must be a real enum.config_module value first —
    # configmaint.validate checks every cfg_setting.module against this enum (hard coherence
    # error, not advisory), found the moment this migration was first run.
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='config_module' AND value='method'"
                        ).fetchone():
        n = conn.execute("SELECT COALESCE(MAX(ordinal), -1) FROM cfg_enum WHERE "
                        "name='config_module'").fetchone()[0]
        conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) "
                    "VALUES ('config_module', 'method', ?, 0)", (n + 1,))
        report.append("cfg_enum (config_module, method) added")
    else:
        report.append("cfg_enum (config_module, method) already present")

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

    # Output location: reuses report.verse_analysis_output_dir (the debate lives in the same
    # book folder as its base extract) — only the naming pattern is new.
    _setting(conn, "report.passage_debate_naming_pattern",
             json.dumps("WA-{book}-{range}-debate.md"),
             "filename pattern for report.passage_debate ({book}/{range} substituted); stable "
             "scheme — reportkit archives the prior version on regenerate, no -vN-/date in the "
             "name itself",
             "report", report)

    _setting(conn, "method.passage_read_guidance_path",
             json.dumps("iba/docs/WA-passage-read-guidance-v1.2-2026-07-27.md"),
             "current version of the passage read guidance (steps 1-5 + notes, incl. step 2 "
             "note (f)) — the passage-debate scaffold and any AI applying it must follow this "
             "exact file; bump this setting (not the debates' memory) when the guidance revises",
             "method", report)
    _setting(conn, "method.interpretation_questions_path",
             json.dumps("iba/docs/WA-interpretation-questions-v1.0-2026-07-26.md"),
             "current version of the Q1-Q10 interrogative + Part B guidance of interpretation — "
             "the passage-debate scaffold and any AI applying it must follow this exact file",
             "method", report)

    if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (STEP,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
            "naming_scheme, archive_dir, inactive) VALUES (?,?,1,NULL,'md','stable','archive',0)",
            (STEP, "{book} {range} -- Passage Debate"))
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
        ("base-extract-missing", "report-stop",
         "the base verse-span-meaning extract for this exact book/range was not found — run "
         "VerseSpanMeaning-Report.ps1 first (report.verse_span_meaning)", "terminal"),
        ("guidance-doc-missing", "report-stop",
         "method.passage_read_guidance_path or method.interpretation_questions_path points to a "
         "file that does not exist on disk — the config is stale relative to iba/docs/",
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

    print("passage-debate-report bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
