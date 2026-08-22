"""bootstrap_decision_vs_defect_axis_v1_20260822.py — ONE-OFF, idempotent. Stage 1 of the build
approved on escalation #798 (design: iba/docs/escalation-decision-vs-defect-axis-proposal-v5-
20260822.md, read with v4 — v5 supersedes v1-v3 in full, v4's §1/§2/§5/§6 are the parts v5 left
unchanged). Build tracked on escalation #799.

Builds, in one atomic unit:
  (a) `cfg_behaviour_rule` (class=development): 'decision-points-are-terminal-not-inline' — the
      governing rule this whole build implements, per the researcher's process statement 2026-08-22.
  (b) `cfg_enum resolution_kind` — decision_required | self_correctable.
  (c) `cfg_escalation_requirement` — resolution_kind required at Raise, both shapes.
  (d) `cfg_passage` — a new per-module settings table (governance.module.config), replacing the 4
      `cfg_setting` rows that used to carry passage's own configuration, plus 2 new threshold
      settings (§3.5/open-input-1 of the design). Full governance registration
      (cfg_table/cfg_column/cfg_write_grant) included.
  (e) This script's own `cfg_utility` registration (governance.new_utility_registration_timing).

Does NOT touch code — that is stages 2-4 of the same build (escalation #799), applied separately
once this stage's own test (below) passes.

    python -m iba.app.migration.bootstrap_decision_vs_defect_axis_v1_20260822
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_DDL = """
CREATE TABLE IF NOT EXISTS cfg_passage (
    key      TEXT PRIMARY KEY,
    value    TEXT,
    "use"    TEXT,
    inactive INTEGER NOT NULL DEFAULT 0
);
"""

_MIGRATION_FILE = "iba/app/migration/bootstrap_decision_vs_defect_axis_v1_20260822.py"


def _behaviour_rule(conn, class_, rule_key, rule_text, source, enforced_by, report):
    if not conn.execute(
            "SELECT 1 FROM cfg_behaviour_rule WHERE class=? AND rule_key=?",
            (class_, rule_key)).fetchone():
        conn.execute(
            "INSERT INTO cfg_behaviour_rule (class, rule_key, rule_text, source, enforced_by, "
            "added_at, active) VALUES (?,?,?,?,?,datetime('now'),1)",
            (class_, rule_key, rule_text, source, enforced_by))
        report.append(f"cfg_behaviour_rule ({class_}/{rule_key}) added")
    else:
        report.append(f"cfg_behaviour_rule ({class_}/{rule_key}) already present")


def _enum(conn, name, value, report):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?,0)", (name, value, n))
        report.append(f"cfg_enum {name} += {value!r}")
    else:
        report.append(f"cfg_enum {name} already has {value!r}")


def _requirement(conn, action, field, condition_key, check_kind, message, report):
    if not conn.execute(
            "SELECT 1 FROM cfg_escalation_requirement WHERE action=? AND field=? AND "
            "condition_key=?", (action, field, condition_key)).fetchone():
        conn.execute(
            "INSERT INTO cfg_escalation_requirement (action, field, condition_key, message, "
            "active, check_kind) VALUES (?,?,?,?,1,?)",
            (action, field, condition_key, message, check_kind))
        report.append(f"cfg_escalation_requirement ({action}/{field}/{condition_key}) added")
    else:
        report.append(f"cfg_escalation_requirement ({action}/{field}/{condition_key}) already present")


def _write_grant(conn, writer, table_name, report):
    if not conn.execute(
            "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'",
            (writer, table_name)).fetchone():
        conn.execute("INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                    "VALUES (?,?,'iba',0)", (writer, table_name))
        report.append(f"cfg_write_grant ({writer!r}, {table_name!r}) added")
    else:
        report.append(f"cfg_write_grant ({writer!r}, {table_name!r}) already present")


def _table_and_columns(conn, name, grain, use, columns, report):
    if not conn.execute("SELECT 1 FROM cfg_table WHERE database='iba' AND name=?", (name,)).fetchone():
        conn.execute("INSERT INTO cfg_table (database, name, grain, \"use\") VALUES ('iba',?,?,?)",
                    (name, grain, use))
        report.append(f"cfg_table {name!r} added")
    else:
        report.append(f"cfg_table {name!r} already present")
    for ordinal, (col, coltype, ispk, notnull, colnuse) in enumerate(columns):
        if not conn.execute(
                "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
                (name, col)).fetchone():
            conn.execute(
                "INSERT INTO cfg_column (database, table_name, name, ordinal, \"type\", is_pk, "
                "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by) "
                "VALUES ('iba',?,?,?,?,?,?,0,NULL,NULL,?,NULL,NULL,?)",
                (name, col, ordinal, coltype, ispk, notnull, colnuse, _MIGRATION_FILE))
            report.append(f"cfg_column ({name}.{col}) added")
        else:
            report.append(f"cfg_column ({name}.{col}) already present")


def _passage_row(conn, key, value, use, report):
    if not conn.execute("SELECT 1 FROM cfg_passage WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_passage (key, value, \"use\", inactive) VALUES (?,?,?,0)",
                    (key, value, use))
        report.append(f"cfg_passage {key!r} added")
    else:
        report.append(f"cfg_passage {key!r} already present")


def _remove_old_passage_setting(conn, key, report):
    row = conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone()
    if row:
        conn.execute("DELETE FROM cfg_setting WHERE key=?", (key,))
        report.append(f"cfg_setting {key!r} removed (moved to cfg_passage)")
    else:
        report.append(f"cfg_setting {key!r} already absent")


def _utility(conn, module, file_path, purpose, report):
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE file_path=?", (file_path,)).fetchone():
        conn.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "config_exempt_reason, crash_escalation_reviewed) VALUES (?,?,?,0,1,?,0)",
            (module, file_path, purpose,
             "one-off migration script -- writes directly into cfg_* tables via raw sqlite3, "
             "same class as cfgload.py"))
        report.append(f"cfg_utility {file_path!r} registered")
    else:
        report.append(f"cfg_utility {file_path!r} already registered")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    # (a) governance rule
    _behaviour_rule(
        conn, "development", "decision-points-are-terminal-not-inline",
        "When building or validating anything -- code, config, or process -- a point that "
        "requires a NEW decision (a judgement call, an ambiguity, something not already "
        "specified) is TERMINAL: it must not be answered inline and resumed. It is recorded as "
        "an open item and routed back into design/specification; work resumes only after the "
        "design is settled and approved. A point that instead reveals Claude's own execution "
        "error against an ALREADY-settled, already-approved design (a typo, a wrong parameter, a "
        "slip) is SELF-CORRECTABLE: Claude fixes it directly, records what was wrong and what "
        "changed, and continues -- no new approval is required, because no new decision was "
        "made. The distinguishing question is always: does resolving this require deciding "
        "something new, or only correcting execution against something already decided? A "
        "recurring decision_required outcome on the same routine, run after run, is itself a "
        "defect -- it means a threshold or parameter that should have been specified once, in "
        "config, during design, was left to be re-asked every time instead. That is a design gap "
        "to close (add the missing config), not a pattern to formalise.",
        "researcher, 2026-08-22, escalation #798",
        "escalation.resolution_kind (decision_required | self_correctable) for escalation-raised "
        "items -- see cfg_enum 'resolution_kind' and cfg_escalation_requirement.",
        report)

    # (b) resolution_kind enum
    _enum(conn, "resolution_kind", "decision_required", report)
    _enum(conn, "resolution_kind", "self_correctable", report)

    # (c) raise-time requirement
    _requirement(
        conn, "raise", "resolution_kind", "always", "field_required",
        "resolution_kind is required at Raise -- decision_required or self_correctable (cfg_enum "
        "resolution_kind). See cfg_behaviour_rule 'decision-points-are-terminal-not-inline'.",
        report)

    # (d) cfg_passage — table + registration + rows
    conn.executescript(_DDL)
    report.append("cfg_passage table ensured")

    _write_grant(conn, "configmaint.propose", "cfg_passage", report)
    _table_and_columns(
        conn, "cfg_passage", "one row per key",
        "Module-specific settings for the passage module (governance.module.config) -- replaces "
        "module=passage rows formerly in the shared cfg_setting table.",
        [("key", "TEXT", 1, 1, "the setting's key, e.g. 'passage.quality_report_path' -- kept "
         "identical to the prior cfg_setting key text so no caller string changes, only the "
         "table read from"),
         ("value", "TEXT", 0, 0, "JSON-encoded value, same convention as cfg_setting.value"),
         ("use", "TEXT", 0, 0, "what the setting controls and why"),
         ("inactive", "INTEGER", 0, 1, "soft-disable flag, same convention as cfg_setting")],
        report)

    _passage_row(conn, "passage.quality_report_path",
                json.dumps("iba/app/reports/passage-quality.md"),
                "where passage.validate persists its findings", report)
    _passage_row(conn, "passage.debate_session_chapter_guideline", json.dumps(3),
                "Advisory session-scope guideline (not hard-enforced) for report.passage_debate "
                "fill-in work: recommended max chapters per Claude Code session before clearing "
                "context and starting a fresh one.", report)
    _passage_row(conn, "passage.debate_run_sequence",
                json.dumps([
                    {"work_package": "operations-ingest", "step": "hib.set"},
                    {"work_package": "build-passages", "step": "passage.build"},
                    {"work_package": "operations-ingest", "step": "phenomenon.set"},
                    {"work_package": "operations-ingest", "step": "operation.set"},
                    {"work_package": "operations-ingest", "step": "closing.set"},
                ]),
                "Ordered step sequence Debate-Run.ps1 walks for one debate scope -- "
                "work_package+step pairs against the EXISTING active registrations.", report)
    _passage_row(conn, "passage.debate_staging_path_pattern",
                json.dumps("iba/app/staging/operations/{book_lower}-{scope}-{step}.json"),
                "Predictable path Debate-Run.ps1 checks for each step payload JSON before "
                "pausing.", report)
    _passage_row(conn, "passage.max_single_verse_pct", json.dumps(20),
                "Per-book threshold: passage.validate escalates only if a book's (single-verse "
                "passage count / total verses in that book) exceeds this percentage. Below it, "
                "the book's distribution is accepted automatically -- no researcher decision "
                "needed for an already-in-bounds result. Researcher, 2026-08-22.", report)
    _passage_row(conn, "passage.max_avg_verses_per_passage", json.dumps(30),
                "Per-book threshold: passage.validate escalates only if a book's average "
                "verses-per-passage exceeds this. Below it, accepted automatically. Researcher, "
                "2026-08-22.", report)

    for key in ("passage.quality_report_path", "passage.debate_session_chapter_guideline",
               "passage.debate_run_sequence", "passage.debate_staging_path_pattern"):
        _remove_old_passage_setting(conn, key, report)

    # raw.zero_strongs_action (open input 2 of the design -- decided: reject)
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key='raw.zero_strongs_action'").fetchone():
        conn.execute(
            "INSERT INTO cfg_setting (key, value, use, module) VALUES "
            "('raw.zero_strongs_action', ?, ?, 'raw')",
            (json.dumps("reject"),
             "What discover() does when a word resolves to zero strongs: 'reject' (default, "
             "researcher 2026-08-22 -- 'it should not happen', treated as anomalous every time "
             "until decided otherwise for a specific case) or 'proceed' (register the word "
             "anyway with zero strongs, no escalation)."))
        report.append("cfg_setting 'raw.zero_strongs_action' added")
    else:
        report.append("cfg_setting 'raw.zero_strongs_action' already present")

    # (e) self-registration
    _utility(conn, "bootstrap_decision_vs_defect_axis",
            _MIGRATION_FILE,
            "One-off migration: escalation #798/#799 Stage 1 -- cfg_behaviour_rule "
            "'decision-points-are-terminal-not-inline', cfg_enum resolution_kind, the raise-time "
            "requirement, the new cfg_passage module table (with governance registration and "
            "6 rows, replacing 4 cfg_setting.passage.* rows), and raw.zero_strongs_action.",
            report)

    conn.commit()
    conn.close()

    print("decision-vs-defect axis bootstrap (escalation #798/#799, Stage 1):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
