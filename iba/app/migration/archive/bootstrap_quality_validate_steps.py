"""bootstrap_quality_validate_steps.py — ONE-OFF: register candidate.validate / passage.validate
as standalone work packages, wire up their escalation paths, reclassify two raw.py conditions
that were silently continuing when they represent real judgement calls, and add the
candidate_tag clean-format setting.

Batch/direct, not routed through configmaint.propose, per the researcher's explicit instruction
(2026-07-21): "I definitely do not want to approve each and every issue individually" — this
registers the MACHINERY (work packages, steps, on_fail paths) that makes escalation work at all;
the researcher reviews the result (this file + GOVERNANCE.md), not each row. Once registered, the
REAL escalations these steps raise at runtime (actual data findings) still pause and wait for a
genuine decision every time they're invoked — nothing here suppresses that.

    python -m iba.app.migration.bootstrap_quality_validate_steps
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    # ── new standalone work packages ──
    work_packages = [
        ("candidate-quality", "Candidate-Quality.ps1", "none"),
        ("passage-quality", "Passage-Quality.ps1", "none"),
    ]
    for name, ps, runs_over in work_packages:
        if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?", (name,)).fetchone():
            conn.execute("INSERT INTO cfg_work_package VALUES (?,?,?)", (name, ps, runs_over))
            report.append(f"cfg_work_package {name!r} added")
        else:
            report.append(f"cfg_work_package {name!r} already present")

    steps = [
        ("candidate-quality", 0, "candidate.validate", "iba.app.handlers.candidate:validate", "none",
         "read-only quality check: candidate_tag null/format, lemma_key/strong resolution — "
         "one escalation per invocation, standalone (not part of seed/set)"),
        ("passage-quality", 0, "passage.validate", "iba.app.handlers.passage:validate", "none",
         "read-only quality check: passage verse_count distribution — one escalation per "
         "invocation, standalone (not part of build-passages)"),
    ]
    for wp, ordinal, step, handler, scope, does in steps:
        existing = conn.execute(
            "SELECT handler FROM cfg_step WHERE work_package=? AND step=?", (wp, step)).fetchone()
        if not existing:
            conn.execute("INSERT INTO cfg_step VALUES (?,?,?,?,?,?)",
                         (wp, ordinal, step, handler, scope, does))
            report.append(f"cfg_step {step!r} added under {wp!r}")
        elif existing[0] != handler:
            conn.execute("UPDATE cfg_step SET handler=? WHERE work_package=? AND step=?",
                        (handler, wp, step))
            report.append(f"cfg_step {step!r} handler corrected")
        else:
            report.append(f"cfg_step {step!r} already present")

    # ── on_fail: every condition these new steps (and configmaint.validate's pending one) raise ──
    on_fail = [
        ("configmaint.validate", "needs-review", "pause-continue",
         "cfg_* has advisory findings (orphans/needs-justification) needing researcher judgement"),
        ("configmaint.validate", "findings-rejected", "report-stop",
         "researcher flagged advisory findings as needing action, not acknowledgement"),
        ("configmaint.validate", "needs-revision", "report-stop",
         "researcher asked for more specific investigation (see comment)"),
        ("candidate.validate", "needs-review", "pause-continue",
         "span_candidate has tag/lemma_key quality findings needing researcher judgement"),
        ("candidate.validate", "findings-rejected", "report-stop",
         "researcher flagged candidate quality findings as needing action"),
        ("candidate.validate", "needs-revision", "report-stop",
         "researcher asked for more specific investigation (see comment)"),
        ("passage.validate", "needs-review", "pause-continue",
         "passage verse_count distribution needs researcher judgement"),
        ("passage.validate", "findings-rejected", "report-stop",
         "researcher flagged the passage distribution as needing the rule revisited"),
        ("passage.validate", "needs-revision", "report-stop",
         "researcher asked for more specific investigation (see comment)"),
    ]
    for step, condition, path, message in on_fail:
        if not conn.execute(
                "SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", (step, condition)).fetchone():
            conn.execute("INSERT INTO cfg_on_fail VALUES (?,?,?,?,?)",
                         (step, condition, path, None, message))
            report.append(f"cfg_on_fail ({step}, {condition}) -> {path} added")
        else:
            report.append(f"cfg_on_fail ({step}, {condition}) already present")

    # ── reclassify: these were silently report-continue but represent real judgement calls —
    # raw.verses/shortfall is exactly the class of bug BUILD.md §5 documents finding (STEP's
    # forward-walk under-returning); silently continuing past it once nearly shipped wrong data.
    reclassify = [
        ("raw.detail", "no-vocab", "pause-continue",
         "a strong returned no vocab from STEP — missing lexical data, worth a decision, not a silent continue"),
        ("raw.verses", "shortfall", "pause-continue",
         "STEP returned fewer rows than its own reported total — the exact class of bug BUILD.md "
         "§5 found; must not silently continue"),
    ]
    for step, condition, new_path, new_message in reclassify:
        row = conn.execute("SELECT path FROM cfg_on_fail WHERE step=? AND condition=?",
                          (step, condition)).fetchone()
        if row and row[0] != new_path:
            conn.execute("UPDATE cfg_on_fail SET path=?, message=? WHERE step=? AND condition=?",
                        (new_path, new_message, step, condition))
            report.append(f"cfg_on_fail ({step}, {condition}) RECLASSIFIED {row[0]!r} -> {new_path!r}")
        elif row:
            report.append(f"cfg_on_fail ({step}, {condition}) already {new_path!r}")
        else:
            conn.execute("INSERT INTO cfg_on_fail VALUES (?,?,?,?,?)",
                         (step, condition, new_path, None, new_message))
            report.append(f"cfg_on_fail ({step}, {condition}) -> {new_path} added (was missing)")

    # ── candidate.tag_clean_pattern setting (module: candidate) ──
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key='candidate.tag_clean_pattern'").fetchone():
        pattern_value = json.dumps(r"^[A-Za-z][A-Za-z' -]*$")
        conn.execute("INSERT INTO cfg_setting VALUES (?,?,?,?)",
                     ("candidate.tag_clean_pattern", pattern_value,
                      "a clean candidate_tag: letters/spaces/hyphens/apostrophe only — no "
                      "parenthetical transliteration, punctuation, or multi-clause gloss text",
                      "candidate"))
        report.append("cfg_setting 'candidate.tag_clean_pattern' added")
    else:
        report.append("cfg_setting 'candidate.tag_clean_pattern' already present")

    conn.commit()
    conn.close()

    print("quality-validate-steps bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
