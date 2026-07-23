"""bootstrap_report_content_governance.py — ONE-OFF: Phase 0a of
PLAN-reports-config-governance-v1-20260722.md — schema + seed only, no behaviour change.

Adds the schema that lets a report's TITLE/TOC/SECTIONS/FOOTER/NAMING/ARCHIVING/CSV-PAIRING and a
work package's COMPLETE/PAUSED/NEXT-STEP wording live in config instead of hardcoded Python/
PowerShell strings (researcher's 2026-07-22 ruling — "all reports must be config driven" read in
full: need+type+location (already done, 2026-07-21) AND content-shape AND naming/versioning/
archiving AND run-completion/exception notification wording, for every report).

Every row seeded here reproduces TODAY'S actual text/behaviour exactly — this migration changes
nothing visible; `lib/reportkit.py` and `iba/app/ps/_lib/Notify.ps1` (Phase 0b/0d) are what actually
start reading these rows. `log-retention`/`export_tables_csv` are deliberately NOT seeded here: they
have no `cfg_step` row yet (cfg_report.step is a real FK to cfg_step.step), so their cfg_report rows
are added in Phase 0c, right after they're registered as steps.

Ownership ledger (also going into GOVERNANCE.md in Phase 0e — see the plan §10.1):
  cfg_report(title/show_toc/footer_text)        -> the report's title, ToC, footer
  cfg_report(output_kind/naming_scheme/archive)  -> md vs md+csv, filename stability, archive folder
  cfg_report_section                             -> which sections, heading, order, ToC inclusion
  cfg_report_csv_table                           -> which tables (+ joins) the CSV half dumps
  cfg_on_fail(step,condition).route              -> terminal vs terminal+report, per (step,condition)
  cfg_work_package.complete_message/next_step_hint/paused_message -> the whole-package banners
  notification.* settings                        -> shared boilerplate (header/result-line/paused/
                                                     stopped templates every PS script renders from)

NOTE — report.word/validation.word/validation.book already have their own section-inclusion
toggles (`report.show_*`, `validation.show_*`, pre-existing). `cfg_report_section.include` for
these three steps is NOT a second gate — the generator's own show_* filtering stays authoritative;
cfg_report_section only supplies heading text/order/ToC-label for whatever the generator already
decided to include. (Ownership ledger: show_* owns inclusion for these three; cfg_report_section
owns inclusion for the other 4, which have no show_* toggles of their own.)

    python -m iba.app.migration.bootstrap_report_content_governance
"""

from __future__ import annotations

import json
import sqlite3
import sys

from ..lib.cfg import DB_PATH


def _enum(conn, name, value, report):
    if not conn.execute("SELECT 1 FROM cfg_enum WHERE name=? AND value=?", (name, value)).fetchone():
        n = conn.execute("SELECT COUNT(*) FROM cfg_enum WHERE name=?", (name,)).fetchone()[0]
        conn.execute("INSERT INTO cfg_enum VALUES (?,?,?)", (name, value, n))
        report.append(f"cfg_enum {name} += {value!r}")
    else:
        report.append(f"cfg_enum {name} already has {value!r}")


def _setting(conn, key, value, use, module, report):
    if not conn.execute("SELECT 1 FROM cfg_setting WHERE key=?", (key,)).fetchone():
        conn.execute("INSERT INTO cfg_setting VALUES (?,?,?,?)", (key, value, use, module))
        report.append(f"cfg_setting {key!r} added")
    else:
        report.append(f"cfg_setting {key!r} already present")


def _grant(conn, writer, table, report):
    if not conn.execute("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=?",
                        (writer, table)).fetchone():
        conn.execute("INSERT INTO cfg_write_grant VALUES (?,?)", (writer, table))
        report.append(f"cfg_write_grant ({writer}, {table}) added")
    else:
        report.append(f"cfg_write_grant ({writer}, {table}) already present")


def _create_tables(conn, report):
    existing = {r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}

    if "cfg_report" not in existing:
        conn.execute("""
            CREATE TABLE cfg_report (
                step          TEXT PRIMARY KEY REFERENCES cfg_step(step),
                title         TEXT NOT NULL,
                show_toc      INTEGER NOT NULL DEFAULT 1,
                footer_text   TEXT,
                output_kind   TEXT NOT NULL DEFAULT 'md+csv',
                naming_scheme TEXT NOT NULL DEFAULT 'stable',
                archive_dir   TEXT NOT NULL DEFAULT 'archive'
            )
        """)
        report.append("table cfg_report created")
    else:
        report.append("table cfg_report already present")

    if "cfg_report_section" not in existing:
        conn.execute("""
            CREATE TABLE cfg_report_section (
                step         TEXT NOT NULL REFERENCES cfg_report(step),
                ordinal      INTEGER NOT NULL,
                section_key  TEXT NOT NULL,
                heading      TEXT NOT NULL,
                toc_label    TEXT,
                include      INTEGER NOT NULL DEFAULT 1,
                PRIMARY KEY (step, section_key)
            )
        """)
        report.append("table cfg_report_section created")
    else:
        report.append("table cfg_report_section already present")

    if "cfg_report_csv_table" not in existing:
        conn.execute("""
            CREATE TABLE cfg_report_csv_table (
                step        TEXT NOT NULL REFERENCES cfg_report(step),
                table_name  TEXT NOT NULL,
                join_note   TEXT,
                PRIMARY KEY (step, table_name)
            )
        """)
        report.append("table cfg_report_csv_table created")
    else:
        report.append("table cfg_report_csv_table already present")

    cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_on_fail)")}
    if "route" not in cols:
        conn.execute("ALTER TABLE cfg_on_fail ADD COLUMN route TEXT NOT NULL DEFAULT 'terminal'")
        report.append("cfg_on_fail.route column added")
    else:
        report.append("cfg_on_fail.route already present")

    cols = {r[1] for r in conn.execute("PRAGMA table_info(cfg_work_package)")}
    for col in ("complete_message", "next_step_hint", "paused_message"):
        if col not in cols:
            conn.execute(f"ALTER TABLE cfg_work_package ADD COLUMN {col} TEXT")
            report.append(f"cfg_work_package.{col} column added")
        else:
            report.append(f"cfg_work_package.{col} already present")


# (step, title, naming_scheme, sections[(key, heading)], csv_tables[(table, join_note)])
_REPORTS = [
    ("configmaint.report", "IBA app — configuration report", "stable", [
        ("findings", "## 0. Findings — needing researcher judgement"),
        ("connection", "## 1. Connection (STEP)"),
        ("settings", "## 2. Settings — every rule / threshold, grouped by owning module"),
        ("apis", "## 3. STEP apis"),
        ("work_packages", "## 4. Work packages & steps (the sequence)"),
        ("on_fail", "## 5. on_fail — condition -> path (the fork rules)"),
        ("write_grants", "## 6. Write grants — who may write what"),
        ("status_flow", "## 7. Status flow"),
        ("schema", "## 8. Schema — data tables built from config"),
        ("enums", "## 9. Enums"),
        ("book_order", "## 10. Book order"),
        ("change_log", "## 11. Change-log — every accepted load (audit)"),
        ("report_governance", "## 12. Reports — full governance per report"),
    ], [
        ("cfg_*", "every cfg_* table, one CSV per table — the config store's own verbatim dump"),
    ]),
    ("candidate.validate", "Candidate quality report", "stable", [
        ("span_tag", "## span_candidate.candidate_tag (the stamp)"),
        ("seed_tag", "## candidate_seed.tag (the seed decision — a worklist, not a verdict)"),
        ("gloss", "## lemma_inventory.gloss (the independent substrate)"),
        ("orphan_lemmas", "## Lemmas with no strong entry yet (by frequency)"),
    ], [
        ("candidate_seed", None), ("span_candidate", None), ("lemma_inventory", None),
    ]),
    ("candidate.load", "candidate.load report", "stable", [
        ("duplicates", "## Duplicates skipped (not written)"),
        ("exceptions", "## Exception rows"),
    ], [
        ("candidate_seed", "this run's decision='exception' rows"),
    ]),
    ("passage.validate", "Passage quality report", "stable", [
        ("dist", "## verse_count distribution"),
        ("by_book", "## By book"),
    ], [
        ("passage", None), ("verse_passage", None),
    ]),
    ("report.word", "Raw layer — `{word}`", "dated", [
        ("validation", "## Validation"),
        ("strongs", "## The strongs and their meaning (L1 → L2)"),
        ("sample_verses", "## Sample verses — the span layer (one row per code)"),
    ], [
        ("span", "word-scoped"), ("word_strong", "word-scoped"),
    ]),
    ("validation.word", "Validation report — '{word}'", "dated", [
        ("app_db", "## 1. App & DB"),
        ("pre_post", "## 2. Pre/post"),
        ("integrity", "## 3. Integrity"),
        ("references", "## 4. References"),
        ("expectations", "## 5. Expectations"),
        ("value_quality", "## 6. Value quality"),
    ], [
        ("span", "word-scoped, same slice report.word checks"), ("word_strong", "word-scoped"),
    ]),
    ("validation.book", "Base validation report — book '{book}'", "dated", [
        ("app_db", "## 1. App & DB"),
        ("candidate", "## 3. Candidate (L4b)"),
        ("passages", "## 4. Passages"),
        ("value_quality", "## 6. Value quality"),
    ], [
        ("candidate_seed", "book-scoped"), ("passage", "book-scoped"), ("verse_passage", "book-scoped"),
    ]),
]

# (work_package, complete_message, next_step_hint, paused_message)
_WORK_PACKAGES = [
    ("build-passages", "passages built for '{book}'.", None, None),
    ("set-candidates", "candidates set for '{book}'. Next: iba\\app\\ps\\Build-Passages.ps1 -Book {book}",
     None, None),
    ("new-word", "raw layer built for '{word}'.", "report: python -m iba.app.report --word {word}",
     "a researcher escalation was raised; the run is resumable."),
]

_NOTIFICATIONS = [
    ("notification.not_initialised",
     "The app is not initialised. Run first:  iba\\app\\ps\\Start-Iba.ps1",
     "shown by every PS script's readiness guard when the app/DB isn't initialised"),
    ("notification.header_work_package", "work package : {work_package}",
     "run-header line 1 — which work package is running"),
    ("notification.header_step", "step         : {step}",
     "run-header line 2 (only scripts with a selectable step print this)"),
    ("notification.header_run_id", "run_id       : {run_id}",
     "run-header line — the run's id, for Escalation.ps1 -RunId"),
    ("notification.header_runs_over", "runs over    : {runs_over}",
     "run-header line (only book/word-scoped work packages print this)"),
    ("notification.step_result_line", "  {0,-20} {1,-14} {2}",
     "per-step result line format (PowerShell -f) — step/path/message, colour by outcome"),
    ("notification.paused_banner_guided",
     "PAUSED — awaiting your decision. Answer with:\n"
     "  .\\Escalation.ps1 -Action AnswerRun -RunId {run_id} -Decision <Approve|Reject|Revise> [-Comment ...]\n"
     "then re-run this exact command with -RunId {run_id} to act on the answer.",
     "non-chained single-step work packages' PAUSED banner (candidate-quality, candidate-curation, "
     "configuration-maintenance, passage-quality)"),
    ("notification.paused_banner_passthrough", "PAUSED — {message}",
     "chained work packages' default PAUSED banner (build-passages, set-candidates) — overridden "
     "per work package by cfg_work_package.paused_message when set (e.g. new-word)"),
    ("notification.stopped_banner", "STOPPED — {message}",
     "chained work packages' STOPPED banner — uniform across build-passages/set-candidates/new-word"),
]


def _seed_reports(conn, report):
    for step, title, naming_scheme, sections, csv_tables in _REPORTS:
        if not conn.execute("SELECT 1 FROM cfg_step WHERE step=?", (step,)).fetchone():
            report.append(f"SKIPPED {step!r} — no cfg_step row yet")
            continue
        if not conn.execute("SELECT 1 FROM cfg_report WHERE step=?", (step,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_report (step, title, show_toc, footer_text, output_kind, "
                "naming_scheme, archive_dir) VALUES (?,?,1,NULL,'md+csv',?,'archive')",
                (step, title, naming_scheme))
            report.append(f"cfg_report {step!r} added")
        else:
            report.append(f"cfg_report {step!r} already present")

        for ordinal, (key, heading) in enumerate(sections):
            if not conn.execute(
                    "SELECT 1 FROM cfg_report_section WHERE step=? AND section_key=?",
                    (step, key)).fetchone():
                conn.execute(
                    "INSERT INTO cfg_report_section (step, ordinal, section_key, heading, "
                    "toc_label, include) VALUES (?,?,?,?,?,1)",
                    (step, ordinal, key, heading, heading.lstrip("# ").strip()))
                report.append(f"cfg_report_section ({step}, {key}) added")
            else:
                report.append(f"cfg_report_section ({step}, {key}) already present")

        for table_name, join_note in csv_tables:
            if not conn.execute(
                    "SELECT 1 FROM cfg_report_csv_table WHERE step=? AND table_name=?",
                    (step, table_name)).fetchone():
                conn.execute(
                    "INSERT INTO cfg_report_csv_table (step, table_name, join_note) VALUES (?,?,?)",
                    (step, table_name, join_note))
                report.append(f"cfg_report_csv_table ({step}, {table_name}) added")
            else:
                report.append(f"cfg_report_csv_table ({step}, {table_name}) already present")


def _seed_work_packages(conn, report):
    for name, complete_message, next_step_hint, paused_message in _WORK_PACKAGES:
        row = conn.execute(
            "SELECT complete_message, next_step_hint, paused_message FROM cfg_work_package "
            "WHERE name=?", (name,)).fetchone()
        if row is None:
            report.append(f"SKIPPED {name!r} — no cfg_work_package row")
            continue
        if row[0] is None and row[1] is None and row[2] is None:
            conn.execute(
                "UPDATE cfg_work_package SET complete_message=?, next_step_hint=?, "
                "paused_message=? WHERE name=?",
                (complete_message, next_step_hint, paused_message, name))
            report.append(f"cfg_work_package {name!r} complete/next-step/paused text seeded")
        else:
            report.append(f"cfg_work_package {name!r} already has notification text — left alone")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _create_tables(conn, report)
    _enum(conn, "config_module", "notification", report)

    for key, value, use in _NOTIFICATIONS:
        _setting(conn, key, json.dumps(value), use, "notification", report)

    _seed_reports(conn, report)
    _seed_work_packages(conn, report)

    for table in ("cfg_report", "cfg_report_section", "cfg_report_csv_table"):
        _grant(conn, "configmaint.propose", table, report)

    conn.commit()
    conn.close()

    print("report-content-governance bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
