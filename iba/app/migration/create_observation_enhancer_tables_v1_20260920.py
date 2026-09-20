"""Create `cfg_observation_enhancer_rule` + `ib_observation_enhancer_log` -- the observation_enhancer
utility (escalation #1778, researcher-approved design 2026-09-20: proposal doc
iba/docs/1778-correction-rule-utility-proposal-v1-20260919.md, verbatim researcher instruction
"proceed with the build as planned").

Reading #1778's own history precisely: the researcher does not want Claude inventing rules -- they
want the MECHANISM (a utility that applies an externally-supplied rule to `ib_observation`), while
the rules themselves come from researcher-driven exploration as gaps are found in the data,
progressively, over time. Two parts:

  `cfg_observation_enhancer_rule` -- rule storage. A `cfg_*` table per governance.rules_must_be_
  config_driven (an earlier draft of this proposal offered a JSON-file alternative -- that WAS a
  real deviation from that governance rule, corrected before this build, see #1778 v4). Rows are
  added/edited the same way every other cfg_* row is -- via `configmaint.propose`, approval-gated --
  NOT via a bespoke add/confirm mechanism built here. A rule's own `status` column (draft ->
  confirmed -> active -> retired) is the researcher's per-rule confirmation gate (#1778's own
  answer to "selector scope": safety is process -- look at a real -Action Preview run's actual
  matches, THEN confirm -- not a restricted selector grammar).

  `ib_observation_enhancer_log` -- one row per (observation, field) actually changed by a rule
  application. This app's own established discipline (governance.reports_must_persist / every
  other write path logs what it did) -- the audit trail answering "which rule touched this row, and
  what did it change" months later, matching `ib_node`'s own `traced_observation_id`/`source_stage`.

Safe to re-run: every insert is guarded, no-ops if already applied.

Usage:
    python iba/app/migration/create_observation_enhancer_tables_v1_20260920.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

_RULE_STATUS_ENUM = [
    (1, "draft"),
    (2, "confirmed"),
    (3, "active"),
    (4, "retired"),
]


def table_exists(cur, table: str) -> bool:
    return cur.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone() is not None


def register_table(cur, name: str, grain: str, use: str, category: str) -> None:
    if not cur.execute("SELECT 1 FROM cfg_table WHERE name=?", (name,)).fetchone():
        cur.execute("INSERT INTO cfg_table (database, name, grain, use, inactive, category) "
                   "VALUES ('iba', ?, ?, ?, 0, ?)", (name, grain, use, category))


def register_column(cur, table: str, name: str, ordinal: int, ctype: str, is_pk: int,
                    notnull: int, is_unique: int, fk: str | None, use: str) -> None:
    if not cur.execute("SELECT 1 FROM cfg_column WHERE database='iba' AND table_name=? AND "
                       "name=?", (table, name)).fetchone():
        cur.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
            "is_unique, dflt, fk, use, expectation, source, filled_by, inactive) "
            "VALUES ('iba',?,?,?,?,?,?,?,NULL,?,?,NULL,NULL,NULL,0)",
            (table, name, ordinal, ctype, is_pk, notnull, is_unique, fk, use))


def register_enum(cur, name: str, values: list[tuple[int, str]], use: str) -> None:
    for ordinal, value in values:
        if not cur.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?",
                          (name, value)).fetchone():
            cur.execute(
                "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)",
                (name, value, ordinal))


def register_utility(cur, module: str, file_path: str, purpose: str) -> None:
    if not cur.execute("SELECT 1 FROM cfg_utility WHERE module=?", (module,)).fetchone():
        cur.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "crash_escalation_reviewed) VALUES (?,?,?,0,0,0)",
            (module, file_path, purpose))


def register_write_grant(cur, writer: str, table_name: str) -> None:
    if not cur.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND "
                       "database='iba'", (writer, table_name)).fetchone():
        cur.execute(
            "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
            "VALUES (?,?,'iba',0)", (writer, table_name))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db, timeout=30)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        # ── cfg_observation_enhancer_rule ────────────────────────────────────────────────────
        if not table_exists(cur, "cfg_observation_enhancer_rule"):
            cur.execute("""
                CREATE TABLE cfg_observation_enhancer_rule (
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    rule_key        TEXT NOT NULL UNIQUE,
                    description     TEXT NOT NULL,
                    selector_sql    TEXT NOT NULL,
                    update_json     TEXT NOT NULL,
                    status          TEXT NOT NULL DEFAULT 'draft',
                    confirmed_at    TEXT,
                    created_at      TEXT NOT NULL,
                    ordinal         INTEGER NOT NULL DEFAULT 0,
                    active          INTEGER NOT NULL DEFAULT 1
                )
            """)
            report.append("CREATED cfg_observation_enhancer_rule")
        else:
            report.append("cfg_observation_enhancer_rule already exists — skipped")

        register_table(cur, "cfg_observation_enhancer_rule",
                      "one row per researcher-authored rule",
                      "Rule storage for the observation_enhancer utility (escalation #1778) -- "
                      "pairs a selector_sql (SELECT returning ib_observation.id) with an "
                      "update_json (column->value) applied via direct UPDATE. Added/edited via "
                      "configmaint.propose like any other cfg_* row -- NOT a bespoke add/confirm "
                      "mechanism. status is the researcher's own per-rule confirmation gate "
                      "(draft -> confirmed, after reviewing a real -Action Preview run -> active, "
                      "set automatically on first successful apply -> retired).", "rule")
        for ordinal, name, ctype, is_pk, notnull, is_unique, fk, use in (
            (0, "id", "INTEGER", 1, 1, 0, None, "surrogate PK"),
            (1, "rule_key", "TEXT", 0, 1, 1, None,
             "stable human-chosen identifier, e.g. '1769-placeholder-filler' -- what -Action "
             "Preview/-Action Apply take as -RuleKey"),
            (2, "description", "TEXT", 0, 1, 0, None,
             "what the rule does and why, for a future reader -- not re-derivable from the SQL alone"),
            (3, "selector_sql", "TEXT", 0, 1, 0, None,
             "a single SELECT (no ';', no INSERT/UPDATE/DELETE/DROP/ATTACH/PRAGMA/ALTER) against "
             "ib_observation returning an 'id' column -- checked live by handlers/"
             "observationenhancer.py before every run, not just at authoring time"),
            (4, "update_json", "TEXT", 0, 1, 0, None,
             "JSON object of ib_observation column -> new value, applied via UPDATE to every row "
             "selector_sql matches. Column names checked against ib_observation's real columns "
             "live; the primary key column cannot be targeted."),
            (5, "status", "TEXT", 0, 1, 0, None,
             "cfg_enum-governed (cfg_observation_enhancer_rule.status): draft (authored, not yet "
             "reviewed against real data) | confirmed (researcher has run -Action Preview and "
             "approved -- -Action Apply now permitted) | active (has been applied at least once) | "
             "retired (no longer applied). -Action Apply refuses any rule not confirmed/active."),
            (6, "confirmed_at", "TEXT", 0, 0, 0, None, "ISO-8601 UTC, set when status first becomes confirmed"),
            (7, "created_at", "TEXT", 0, 1, 0, None, "ISO-8601 UTC, set at insert (configmaint.propose)"),
            (8, "ordinal", "INTEGER", 0, 1, 0, None, "display/authoring order only"),
            (9, "active", "INTEGER", 0, 1, 0, None,
             "soft-delete flag distinct from status='retired' -- 0 hides a rule entirely (e.g. "
             "authored in error), matching this app's standard active convention"),
        ):
            register_column(cur, "cfg_observation_enhancer_rule", name, ordinal, ctype, is_pk,
                            notnull, is_unique, fk, use)
        register_enum(cur, "cfg_observation_enhancer_rule.status", _RULE_STATUS_ENUM,
                     "The observation_enhancer rule lifecycle (escalation #1778).")
        report.append("cfg_enum cfg_observation_enhancer_rule.status registered (4 values)")

        # ── ib_observation_enhancer_log ──────────────────────────────────────────────────────
        if not table_exists(cur, "ib_observation_enhancer_log"):
            cur.execute("""
                CREATE TABLE ib_observation_enhancer_log (
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    rule_id         INTEGER NOT NULL,
                    rule_key        TEXT NOT NULL,
                    observation_id  INTEGER NOT NULL,
                    field_changed   TEXT NOT NULL,
                    before_value    TEXT,
                    after_value     TEXT NOT NULL,
                    applied_at      TEXT NOT NULL,
                    run_id          TEXT,
                    FOREIGN KEY (rule_id) REFERENCES cfg_observation_enhancer_rule(id),
                    FOREIGN KEY (observation_id) REFERENCES ib_observation(id)
                )
            """)
            cur.execute("CREATE INDEX idx_ib_obs_enh_log_observation ON "
                       "ib_observation_enhancer_log (observation_id)")
            cur.execute("CREATE INDEX idx_ib_obs_enh_log_rule ON "
                       "ib_observation_enhancer_log (rule_id)")
            report.append("CREATED ib_observation_enhancer_log (+ 2 indexes)")
        else:
            report.append("ib_observation_enhancer_log already exists — skipped")

        register_table(cur, "ib_observation_enhancer_log",
                      "one row per (observation, field) actually changed by a rule application",
                      "Audit trail for the observation_enhancer utility (escalation #1778) -- "
                      "answers 'which rule touched this row, and what did it change' months later, "
                      "the same kind of traceability ib_node's own traced_observation_id/"
                      "source_stage already gives the write-time pipeline. Written only by "
                      "handlers/observationenhancer.py:apply.", "log")
        for ordinal, name, ctype, is_pk, notnull, is_unique, fk, use in (
            (0, "id", "INTEGER", 1, 1, 0, None, "surrogate PK"),
            (1, "rule_id", "INTEGER", 0, 1, 0, "cfg_observation_enhancer_rule.id",
             "which rule made this change"),
            (2, "rule_key", "TEXT", 0, 1, 0, None,
             "denormalised copy of the rule's own key at apply time -- readable even if the rule "
             "row is later retired/edited"),
            (3, "observation_id", "INTEGER", 0, 1, 0, "ib_observation.id",
             "which observation was changed"),
            (4, "field_changed", "TEXT", 0, 1, 0, None, "the ib_observation column that was updated"),
            (5, "before_value", "TEXT", 0, 0, 0, None, "the field's value immediately before this change (stringified)"),
            (6, "after_value", "TEXT", 0, 1, 0, None, "the value written (stringified)"),
            (7, "applied_at", "TEXT", 0, 1, 0, None, "ISO-8601 UTC"),
            (8, "run_id", "TEXT", 0, 0, 0, None, "the run.run_id of the -Action Apply call that made this change"),
        ):
            register_column(cur, "ib_observation_enhancer_log", name, ordinal, ctype, is_pk,
                            notnull, is_unique, fk, use)

        register_utility(cur, "observationenhancer", "iba/app/handlers/observationenhancer.py",
                        "observationenhancer.py -- the observation_enhancer utility (escalation "
                        "#1778). preview(ctx)/apply(ctx): applies a researcher-confirmed "
                        "cfg_observation_enhancer_rule (selector_sql + update_json) to "
                        "ib_observation, logging every change to ib_observation_enhancer_log.")
        report.append("cfg_utility observationenhancer registered")

        register_write_grant(cur, "observation_enhancer.apply", "ib_observation")
        register_write_grant(cur, "observation_enhancer.apply", "ib_observation_enhancer_log")
        register_write_grant(cur, "observation_enhancer.apply", "cfg_observation_enhancer_rule")
        report.append("cfg_write_grant observation_enhancer.apply registered for ib_observation/"
                      "ib_observation_enhancer_log/cfg_observation_enhancer_rule (the last for its "
                      "own draft->active promotion on first successful apply)")
        # governance.config_control: every cfg_* table needs a writer through the sanctioned gate --
        # rule rows (insert/edit/confirm) are added via the ordinary configmaint.propose cycle, not
        # a bespoke command, so THAT is cfg_observation_enhancer_rule's real writer for authoring.
        # Found live by configmaint.validate immediately after the first build pass (missing this
        # exact grant) -- fixed in the same unit of work, not left for a second pass.
        register_write_grant(cur, "configmaint.propose", "cfg_observation_enhancer_rule")
        report.append("cfg_write_grant configmaint.propose -> cfg_observation_enhancer_rule "
                      "registered (rule authoring/confirmation goes through the standard propose "
                      "cycle, not a bespoke mechanism)")

        if not cur.execute("SELECT 1 FROM cfg_work_package WHERE name=?",
                          ("observation-enhancer",)).fetchone():
            cur.execute(
                "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
                "complete_message, next_step_hint, paused_message, inactive) "
                "VALUES (?,?,?,?,?,?,?,0)",
                ("observation-enhancer", "iba/app/ps/Observation-Enhancer.ps1", "none", 0, None,
                 None, None))
            report.append("cfg_work_package observation-enhancer inserted")
        else:
            report.append("cfg_work_package observation-enhancer already present — skipped")

        for step, handler, does in (
            ("observation_enhancer.preview", "iba.app.handlers.observationenhancer:preview",
             "Read-only. Given -RuleKey, runs that rule's selector_sql against live "
             "ib_observation and returns the match count plus a sample of matched rows (id/"
             "cluster_code/stage/tag/strong/status/obs_text, up to 10) and the update_json that "
             "would be applied. Any rule status -- does not require confirmed. No write."),
            ("observation_enhancer.apply", "iba.app.handlers.observationenhancer:apply",
             "Given -RuleKey, refuses unless the rule's status is confirmed/active (the "
             "researcher's own per-rule confirmation gate, escalation #1778 -- run -Action "
             "Preview and confirm via configmaint.propose first). Runs selector_sql, applies "
             "update_json to every matched row via UPDATE, logs each (observation, field) change "
             "to ib_observation_enhancer_log, and promotes a first-time confirmed rule to active."),
        ):
            if not cur.execute("SELECT 1 FROM cfg_step WHERE step=? AND work_package=?",
                              (step, "observation-enhancer")).fetchone():
                cur.execute(
                    "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                    "inactive, kind) VALUES (?,0,?,?,?,?,0,?)",
                    ("observation-enhancer", step, handler, "none", does, "utility"))
                report.append(f"cfg_step {step} inserted")
            else:
                report.append(f"cfg_step {step} already present — skipped")

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
