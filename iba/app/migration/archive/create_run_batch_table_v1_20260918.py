"""Create `run_batch` — the batch/step-level control table (escalation #1756, researcher-approved
design, 2026-09-18). Researcher's own instruction, prompted directly by M49's Stage 1 (verse-
reading) run needing two full restarts from batch 1 this session (a crash, #1754/#1755, then a
deliberate stop): *"create a new escalation to build to resume/skip and crash safeguarding...
a run control table that write steps to a table with a timestamp and write to the table on the
start and end of each process - almost like a process batch control table. this table can be used
in your resume skip also."* Approved verbatim, v3: *"This batch control mechanism must be in force
for all long running routines."*

One row per batch/chunk of a live multi-batch (or single-call) run. `UNIQUE(step, selector_key,
batch_content_key)` is deliberately NOT scoped to one `run_id` — a brand-new run_id can still see
and skip a batch a PRIOR run_id already committed; that IS the resume/skip mechanism.
`batch_content_key` is a stable hash of the batch's own actual item list (verse ids, or a
subgroup's member strongs), not just its ordinal position — correct even if the selector's
underlying item list shifts between runs (e.g. a `cluster_strong` reassignment), per the approved
design's own reasoning.

A `running` row with no matching `committed`/`failed` terminal row is the crash safeguard: proof a
process died mid-batch, distinct from a batch that simply hasn't started yet.

Safe to re-run: guarded, no-ops if already applied.

Usage:
    python iba/app/migration/create_run_batch_table_v1_20260918.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

_STATUS_ENUM = [
    (1, "running"),
    (2, "committed"),
    (3, "failed"),
]


def table_exists(cur, table: str) -> bool:
    return cur.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone() is not None


def register_table(cur, name: str, grain: str, use: str) -> None:
    if not cur.execute("SELECT 1 FROM cfg_table WHERE name=?", (name,)).fetchone():
        cur.execute("INSERT INTO cfg_table (database, name, grain, use, inactive, category) "
                   "VALUES ('iba', ?, ?, ?, 0, 'data')", (name, grain, use))


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
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        if not table_exists(cur, "run_batch"):
            cur.execute("""
                CREATE TABLE run_batch (
                    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                    run_id              TEXT NOT NULL,
                    work_package        TEXT NOT NULL,
                    step                TEXT NOT NULL,
                    selector_key        TEXT NOT NULL,
                    batch_ordinal       INTEGER NOT NULL,
                    batch_content_key   TEXT NOT NULL,
                    status              TEXT NOT NULL,
                    started_at          TEXT NOT NULL,
                    ended_at            TEXT,
                    error_message       TEXT,
                    cost_usd            REAL,
                    UNIQUE (step, selector_key, batch_content_key)
                )
            """)
            cur.execute("CREATE INDEX idx_run_batch_run_id ON run_batch (run_id)")
            cur.execute("CREATE INDEX idx_run_batch_status ON run_batch (status)")
            report.append("CREATED run_batch (+ idx_run_batch_run_id, idx_run_batch_status)")
        else:
            report.append("run_batch already exists — skipped")

        register_table(cur, "run_batch", "one row per batch/chunk attempt of a live multi-batch "
                      "(or single-call) run",
                      "The batch/step-level control table (escalation #1756, researcher-approved "
                      "design 2026-09-18) -- resume/skip (a new run_id skips any batch a PRIOR "
                      "run_id already committed, via UNIQUE(step, selector_key, "
                      "batch_content_key)), crash safeguard (a 'running' row with no terminal "
                      "update proves a dead run), and live progress monitoring (BatchProgress.ps1) "
                      "for every long-running LLM-calling step. lib/batchcontrol.py is the sole "
                      "writer. Prompted directly by M49's Stage 1 verse-reading run needing two "
                      "full from-scratch restarts this session with no way to skip already-paid-for "
                      "batches.")
        for ordinal, name, ctype, is_pk, notnull, is_unique, fk, use in (
            (0, "id", "INTEGER", 1, 1, 0, None, "surrogate PK"),
            (1, "run_id", "TEXT", 0, 1, 0, None,
             "the run.run_id that attempted this batch (informational/audit -- NOT part of the "
             "resume/skip key, deliberately, so a later run_id can still see an earlier run_id's "
             "committed work)"),
            (2, "work_package", "TEXT", 0, 1, 0, None, "e.g. verse-lexical, cluster-reading"),
            (3, "step", "TEXT", 0, 1, 0, None,
             "e.g. lexical.meaning, cluster.subgroup -- part of the resume/skip key"),
            (4, "selector_key", "TEXT", 0, 1, 0, None,
             "what this run was scoped to -- cluster_code alone, or cluster_code|subgroup_code for "
             "a subgroup-scoped step. Part of the resume/skip key."),
            (5, "batch_ordinal", "INTEGER", 0, 1, 0, None,
             "this batch's 1-based position within its own run -- display/ordering only, NOT part "
             "of the resume/skip key (batch_content_key is, since ordinal position can drift "
             "between runs if the selector's own item list changes)"),
            (6, "batch_content_key", "TEXT", 0, 1, 0, None,
             "stable hash (batchcontrol.content_key) of the batch's own actual item list (verse "
             "ids, or member strongs) -- THE resume/skip key together with step+selector_key. "
             "Content-keyed, not position-keyed, so resume is correct even if the underlying item "
             "list shifts between runs."),
            (7, "status", "TEXT", 0, 1, 0, None,
             "cfg_enum-governed (run_batch.status): running (written before the API call) | "
             "committed (written after record_batch's own commit succeeds) | failed (written in "
             "an exception handler before re-raising -- the crash safeguard). A 'running' row with "
             "no later committed/failed row for the same id is live proof of a dead run."),
            (8, "started_at", "TEXT", 0, 1, 0, None, "ISO-8601 UTC, set when status='running' is written"),
            (9, "ended_at", "TEXT", 0, 0, 0, None, "ISO-8601 UTC, set when status becomes committed/failed"),
            (10, "error_message", "TEXT", 0, 0, 0, None, "set only when status='failed'"),
            (11, "cost_usd", "REAL", 0, 0, 0, None, "set only when status='committed', the real spent cost"),
        ):
            register_column(cur, "run_batch", name, ordinal, ctype, is_pk, notnull, is_unique, fk, use)
        register_enum(cur, "run_batch.status", _STATUS_ENUM,
                     "run_batch's own per-batch lifecycle (escalation #1756).")
        report.append("cfg_enum run_batch.status registered (3 values)")

        register_utility(cur, "batchcontrol", "iba/app/lib/batchcontrol.py",
                        "batchcontrol.py -- the single writer for run_batch (escalation #1756). "
                        "start_batch/commit_batch/fail_batch wrap every long-running step's own "
                        "API-call-plus-write unit; already_committed/content_key implement "
                        "resume/skip.")
        register_utility(cur, "batchprogressreport", "iba/app/lib/batchprogressreport.py",
                        "batchprogressreport.py -- read-only live progress report generator over "
                        "run_batch (escalation #1756), backing report.batch_progress / "
                        "BatchProgress.ps1.")
        report.append("cfg_utility batchcontrol/batchprogressreport registered")

        for writer in ("lexical.meaning", "cluster.subgroup", "cluster.reading", "cluster.answer"):
            register_write_grant(cur, writer, "run_batch")
        report.append("cfg_write_grant run_batch registered for lexical.meaning/cluster.subgroup/"
                      "cluster.reading/cluster.answer")

        # ── BatchProgress.ps1 / report.batch_progress -- the live monitor half of #1756 ──────────
        if not cur.execute("SELECT 1 FROM cfg_work_package WHERE name='batch-progress-report'").fetchone():
            cur.execute(
                "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, "
                "complete_message, next_step_hint, paused_message, inactive) "
                "VALUES ('batch-progress-report', 'iba/app/ps/BatchProgress.ps1', 'none', 0, "
                "NULL, NULL, NULL, 0)")
        report.append("cfg_work_package batch-progress-report registered")

        if not cur.execute("SELECT 1 FROM cfg_step WHERE work_package='batch-progress-report' "
                          "AND step='report.batch_progress'").fetchone():
            cur.execute(
                "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, "
                "inactive, kind) VALUES ('batch-progress-report', 0, 'report.batch_progress', "
                "'iba.app.handlers.reports:batch_progress_report', 'none', ?, 0, 'utility')",
                ("Read-only live progress over run_batch (#1756) -- -FilterRunId/-Step/"
                 "-SelectorKey all optional, combine with AND; no filters = every currently-"
                 "running batch DB-wide, the live-right-now view.",))
        report.append("cfg_step report.batch_progress registered")

        if not cur.execute("SELECT 1 FROM cfg_setting WHERE key='report.batch_progress_path'").fetchone():
            cur.execute(
                "INSERT INTO cfg_setting (key, value, inactive) VALUES "
                "('report.batch_progress_path', '\"iba/app/reports/batch-progress.md\"', 0)")
        report.append("cfg_setting report.batch_progress_path registered")

        if not cur.execute("SELECT 1 FROM cfg_report WHERE step='report.batch_progress'").fetchone():
            cur.execute(
                "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                "naming_scheme, archive_dir, inactive) VALUES ('report.batch_progress', "
                "'Batch progress monitor', 1, NULL, 'md', 'stable', 'archive', 0)")
        report.append("cfg_report report.batch_progress registered")

        for ordinal, key, heading, toc_label in (
            (0, "summary", "## Summary", "Summary"),
            (1, "running_now", "## Currently running", "Running now"),
            (2, "recent_failures", "## Recent failures", "Recent failures"),
            (3, "recent_committed", "## Recent committed batches", "Recent committed"),
        ):
            if not cur.execute("SELECT 1 FROM cfg_report_section WHERE step='report.batch_progress' "
                              "AND section_key=?", (key,)).fetchone():
                cur.execute(
                    "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                    "toc_label, include, inactive) VALUES "
                    "('report.batch_progress', ?, ?, ?, ?, 1, 0)",
                    (ordinal, key, heading, toc_label))
        report.append("cfg_report_section rows registered for report.batch_progress (4 sections)")

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
