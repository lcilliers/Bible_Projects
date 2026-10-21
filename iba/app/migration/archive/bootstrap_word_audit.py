"""bootstrap_word_audit.py — ONE-OFF: registers the `word-audit` work package (escalation #672,
`engine-controls-migration-plan-v4-20260817.md`, Phase 1) — `cfg_utility` for `engine/`'s 15
modules, `cfg_work_package`, the 10-step `cfg_step` sequence, and the 2 `cfg_on_fail` rows.

Step count is 10, not `audit_word.py`'s original 12 — `Pre-A1` (lock+run-log) and half of `A2`
(`_load_snapshot()`'s before-state row-count preview) are redundant with what `run.py`'s own
`_ensure_run()`/`_snapshot()` already do automatically for every word-scoped run; dropped, not
ported. `kind` re-derived per step against real precedent (`BUILD.md` §40), not defaulted to
`operations` — `word.export` is `utility`, matching the existing `report.word`. Full reasoning:
`BUILD.md` §124, plan v4 §Phase 1.

`cfg_write_grant` deliberately NOT populated here — which table each writer may touch depends on
the still-open one-DB-vs-two-DB question (plan §Phase 3), and on a genuinely new piece of plumbing
this bootstrap surfaced while being written: `run.py`'s `Db`/`_grant()` machinery is scoped to
`iba.db`'s own connection only — a `word.*` step writing to a `bible_research.db` table (the
two-DB-kept branch) needs a SECOND connection + its own grant-check path that doesn't exist yet.
Not built here — flagged as its own follow-up, not guessed at.

Handlers are real, dispatchable, and do real bookkeeping (JSON loading/validation, confirm-prompt
display) where that's self-contained within iba.db + the input JSON file; anything that would
require writing bible_research.db data returns a clearly-labelled NOT YET IMPLEMENTED outcome
rather than a fake success — per escalation #656's standing rule (redesign, don't port) and
`feedback_never_model_output_on_prior_unreviewed_pass`, this is deliberately NOT a port of
`engine/audit_word.py`'s actual logic.

Schema is DATA (new work package + its steps), same class of exception as every other bulk
bootstrap in this app — not a `configmaint.propose` call.

    python -m iba.app.migration.bootstrap_word_audit
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_UTILITY_ROWS = [
    # module, file_path, purpose, inactive, config_exempt
    ("engine_audit", "engine/audit.py",
     "Audit framework -- WR-01 through WR-20, run after all writes.", 0, 0),
    ("engine_audit_word", "engine/audit_word.py",
     "AUDIT_WORD mode (v4) -- Pre-A1 through A11, unified new-word + re-audit pipeline.", 0, 0),
    ("engine_backup", "engine/backup.py",
     "DB backup management (SG-01, SG-12, SG-13) -- timestamped pre-run backup, abort if it fails.",
     0, 0),
    ("engine_constants", "engine/constants.py", "Shared constants.", 0, 1),
    ("engine_db", "engine/db.py", "DB access helpers (wraps analytics/db_client.py).", 0, 0),
    ("engine_cli", "engine/engine.py", "CLI entry point (python -m engine.engine).", 0, 0),
    ("engine_flag", "engine/flag_engine.py", "Derivable flag evaluation (S5/N16/A7).", 0, 0),
    ("engine_gap_fill", "engine/gap_fill.py",
     "GAP_FILL mode (S1-S8), superseded by audit_word.", 1, 0),
    ("engine_meaning_parser", "engine/meaning_parser.py",
     "Meaning text parser -> wa_meaning_parsed/_sense/_stem, wa_lsj_parsed.", 0, 0),
    ("engine_migrate", "engine/migrate.py",
     "Schema migration runner v2.2->v3.0 (M01-M10).", 0, 1),
    ("engine_register", "engine/register.py",
     "REGISTER subcommand -- new word_registry row.", 0, 0),
    ("engine_report", "engine/report.py", "Word overview report.", 0, 0),
    ("engine_run_log", "engine/run_log.py",
     "engine_run_log/word_run_state write helpers.", 0, 0),
    ("engine_softdelete", "engine/softdelete.py",
     "Shared soft-delete cascade helpers (H1-H3, H5).", 0, 0),
    ("engine_span_filter", "engine/span_filter.py",
     "STEP masterSearch HTML span filtering (Sec5.2 v4).", 0, 0),
]

_STEP_ROWS = [
    # ordinal, step, does, kind
    (0, "word.load_json",
     "Load + validate latest Step 1 JSON + structural completeness check (merged from old A2/A3)",
     "operations"),
    (1, "word.confirm", "Registry display + CONFIRM prompt", "operations"),
    (2, "word.gap_report", "Build gap report (Term/Related/Verse/VTL streams)", "operations"),
    (3, "word.gap_display", "Display gap report (+ interactive approve gate)", "operations"),
    (4, "word.apply_changes", "Apply changes, one transaction per stream", "operations"),
    (5, "word.meaning", "Meaning handler -- parse + migrate legacy fields", "operations"),
    (6, "word.flag_reset", "Quality flag reset (DATA_COVERAGE), re-derive", "operations"),
    (7, "word.audit_checks", "WR-01-WR-20 + write word_run_state (PROVISIONAL)", "operations"),
    (8, "word.registry_close",
     "Registry + file-index update, last_automation_run='AUDITED'", "operations"),
    (9, "word.export", "Full-word JSON export", "utility"),
]

_ON_FAIL_ROWS = [
    # step, condition, path, message
    ("word.confirm", "needs-confirmation", "pause-continue",
     "word display shown; confirm to proceed"),
    ("word.gap_display", "needs-approval", "pause-continue",
     "gap report shown; approve to apply (only when run --interactive)"),
]

_HANDLER = "iba.app.handlers.wordaudit:{fn}"
_FN_FOR_STEP = {
    "word.load_json": "load_json", "word.confirm": "confirm", "word.gap_report": "gap_report",
    "word.gap_display": "gap_display", "word.apply_changes": "apply_changes",
    "word.meaning": "meaning", "word.flag_reset": "flag_reset",
    "word.audit_checks": "audit_checks", "word.registry_close": "registry_close",
    "word.export": "export",
}

_WORK_PACKAGE = ("word-audit", "iba/app/ps/Word-Audit.ps1", "word", 1,
                 "word-audit complete.", "next: none — full pipeline run.",
                 "word-audit paused — see the message above.")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    if conn.execute("SELECT 1 FROM cfg_work_package WHERE name='word-audit'").fetchone():
        print("word-audit already registered — nothing to do.")
        conn.close()
        return 0

    for module, file_path, purpose, inactive, config_exempt in _UTILITY_ROWS:
        if conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
            report.append(f"cfg_utility {module!r} already present — left alone")
            continue
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "config_exempt_reason) VALUES (?,?,?,?,?,?)",
            (module, file_path, purpose, inactive, config_exempt,
             "values move to cfg_setting instead" if module == "engine_constants" else
             "one-shot historical, same class as iba/app/migration/*" if module == "engine_migrate"
             else None))
        report.append(f"cfg_utility {module!r} -> {file_path}")

    name, ps_script, runs_over, chained, complete_msg, next_hint, paused_msg = _WORK_PACKAGE
    conn.execute(
        "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, complete_message, "
        "next_step_hint, paused_message, inactive) VALUES (?,?,?,?,?,?,?,0)",
        (name, ps_script, runs_over, chained, complete_msg, next_hint, paused_msg))
    report.append(f"cfg_work_package {name!r} registered")

    for ordinal, step, does, kind in _STEP_ROWS:
        handler = _HANDLER.format(fn=_FN_FOR_STEP[step])
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, "
            "kind) VALUES (?,?,?,?,?,?,0,?)",
            ("word-audit", ordinal, step, handler, "word", does, kind))
        report.append(f"cfg_step {step!r} ordinal={ordinal} kind={kind} handler={handler}")

    for step, condition, path, message in _ON_FAIL_ROWS:
        conn.execute(
            "INSERT INTO cfg_on_fail (step, condition, path, resolver, message, route, inactive) "
            "VALUES (?,?,?,NULL,?,?,0)",
            (step, condition, path, message, "terminal"))
        report.append(f"cfg_on_fail {step!r}/{condition!r} -> {path!r}")

    conn.commit()
    conn.close()

    print("word-audit bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
