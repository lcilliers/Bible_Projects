"""bootstrap_step_kind.py — ONE-OFF: classify every `cfg_step` row as `operations` (the modules
that actually do the study work — raw/registry/lexicon/passage-debate-prep/narrative) or `utility`
(supports the app's own running — configmaint, general reporting) per the researcher's own mental
model, 2026-07-29/30, which corrected this migration's first draft (the earlier `cfg_utility`
registry covered `lib/*.py` only — "the handler modules are not in the table" was the exact gap).

Schema is DDL (new column + new enum group), so — same class of exception as every other schema
addition in this app (`bootstrap_inactive_column.py`, `bootstrap_cfg_utility.py`) — a direct,
documented, idempotent bootstrap, not a `configmaint.propose` call. Every VALUE assigned here is a
one-time classification backfill; changing a step's kind going forward goes through the normal
`configmaint.propose` path like any other `cfg_step` value.

Classification (35 steps total, all of them — retired ones included, for provenance, same
convention as `inactive`):

  OPERATIONS (22) — raw.*, registry.exists/create, lexicon.parse/related/validate, passage.build/
  validate, candidate.* (retired), report.verse_span_meaning, report.passage_debate,
  report.whole_book_read (the "prepare debate" workflow — spans passage.py AND reports.py, per the
  researcher's own observation), report.book_narrative_validate.

  UTILITY (13) — configmaint.validate/propose/report, retention.report, table.export, and
  `reports.py`'s general-purpose reports: report.word, validation.word, validation.book,
  report.registry, report.schema_overview, report.seed_candidate, report.span_analysis,
  report.strong_meaning.

    python -m iba.app.migration.bootstrap_step_kind
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_OPERATIONS = (
    "report.book_narrative_validate", "passage.build", "candidate.curate", "candidate.load",
    "candidate.validate", "lexicon.parse", "lexicon.related", "lexicon.validate",
    "registry.exists", "registry.create", "raw.discover", "raw.detail", "raw.verses",
    "raw.write", "raw.validate", "report.passage_debate", "passage.validate",
    "raw.backfill_meaning", "candidate.seed", "candidate.set", "report.verse_span_meaning",
    "report.whole_book_read",
)

_UTILITY = (
    "configmaint.validate", "configmaint.propose", "configmaint.report", "retention.report",
    "report.registry", "report.word", "validation.word", "validation.book",
    "report.schema_overview", "report.seed_candidate", "report.span_analysis",
    "report.strong_meaning", "table.export",
)


def _create_column_and_enum(conn: sqlite3.Connection, report: list[str]) -> None:
    cols = {r[1] for r in conn.execute('PRAGMA table_info(cfg_step)')}
    if "kind" not in cols:
        conn.execute('ALTER TABLE cfg_step ADD COLUMN kind TEXT')
        report.append("cfg_step.kind column added (physical ALTER)")
    else:
        report.append("cfg_step.kind already present")

    if not conn.execute(
            "SELECT 1 FROM cfg_column WHERE table_name='cfg_step' AND name='kind'").fetchone():
        ordinal = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) + 1 FROM cfg_column WHERE table_name='cfg_step'"
        ).fetchone()[0]
        conn.execute(
            'INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, "notnull", '
            "is_unique, dflt, fk, use, expectation, source, filled_by) "
            "VALUES ('cfg_step','kind',?,?,0,1,0,NULL,NULL,?,?,NULL,"
            "'migration/bootstrap_step_kind.py')",
            (ordinal, "TEXT",
             "operations (does the study work — raw/registry/lexicon/passage-debate-prep/"
             "narrative) or utility (supports the app's own running — configmaint, general "
             "reporting). REQUIRED for dispatch — run.py refuses a step with no kind (escalation, "
             "2026-07-30).",
             "enum.step_kind"))
        report.append("cfg_column row for cfg_step.kind added")
    else:
        report.append("cfg_column row for cfg_step.kind already present")

    for ordinal, value in enumerate(("operations", "utility")):
        if not conn.execute(
                "SELECT 1 FROM cfg_enum WHERE name='step_kind' AND value=?", (value,)).fetchone():
            conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES "
                        "('step_kind',?,?,0)", (value, ordinal))
            report.append(f"cfg_enum step_kind += {value!r}")
        else:
            report.append(f"cfg_enum step_kind already has {value!r}")


def _classify(conn: sqlite3.Connection, report: list[str]) -> None:
    known = {r[0] for r in conn.execute("SELECT step FROM cfg_step")}
    classified = {r[0] for r in conn.execute("SELECT step FROM cfg_step WHERE kind IS NOT NULL")}

    for step in _OPERATIONS:
        if step not in known:
            report.append(f"SKIPPED {step!r} — not a known cfg_step (list is stale, fix the "
                          f"migration, not the DB)")
            continue
        if step in classified:
            report.append(f"{step!r} already classified — left alone")
            continue
        conn.execute("UPDATE cfg_step SET kind='operations' WHERE step=?", (step,))
        report.append(f"{step!r} -> operations")

    for step in _UTILITY:
        if step not in known:
            report.append(f"SKIPPED {step!r} — not a known cfg_step (list is stale, fix the "
                          f"migration, not the DB)")
            continue
        if step in classified:
            report.append(f"{step!r} already classified — left alone")
            continue
        conn.execute("UPDATE cfg_step SET kind='utility' WHERE step=?", (step,))
        report.append(f"{step!r} -> utility")

    covered = set(_OPERATIONS) | set(_UTILITY)
    missed = known - covered
    for step in sorted(missed):
        report.append(f"NOT COVERED by this migration's lists: {step!r} — still unclassified, "
                      f"run.py will refuse to dispatch it until a configmaint.propose sets "
                      f"cfg_step.kind")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    report: list[str] = []

    _create_column_and_enum(conn, report)
    _classify(conn, report)

    conn.commit()
    conn.close()

    print("step-kind classification bootstrap:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
