"""Add verse_meta.status + verse_meta.status_changed_at, per escalation #1661.

Researcher instruction, verbatim: "Add an additional column to verse_meta to set the status of
the verse. Status values: exclude; anchor; citated; analysed. ... proceed to create column. Also
create a ps routine whereby researcher can update the status for a range of verses by comma
delimited refences. Ignore the status anchor, it is already included as a separate column.
Updated column must be stamped if the status change."

`anchor` is already `verse_meta.is_passage_anchor` (create_verse_meta_table_v1_20260909.py) --
per the instruction, NOT one of this column's own domain values. `status` domain (cfg_enum
verse_meta_status): exclude, citated, analysed. NULL = not yet set (no default value implied by
the instruction).

Columns:
  status              TEXT, nullable, one of cfg_enum verse_meta_status (exclude/citated/analysed)
  status_changed_at   TEXT, nullable, ISO-8601 UTC -- set ONLY when status actually changes value
                       (the "stamped if the status change" requirement), never touched otherwise.

Not populated by this script -- both columns start NULL for every existing row; set going forward
by the researcher via VerseMeta.ps1 -Step SetStatus (lib/versemeta.py), not backfilled with a
guessed default.

Safe to re-run: columns added only if missing.

Usage:
    python iba/app/migration/add_verse_meta_status_column_v1_20260910.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def column_exists(cur, table: str, col: str) -> bool:
    return any(r[1] == col for r in cur.execute(f"PRAGMA table_info({table})"))


def add_columns(cur, report: list[str]) -> None:
    if column_exists(cur, "verse_meta", "status"):
        report.append("COLUMN verse_meta.status already present")
    else:
        cur.execute("ALTER TABLE verse_meta ADD COLUMN status TEXT")
        report.append("ADDED COLUMN verse_meta.status")

    if column_exists(cur, "verse_meta", "status_changed_at"):
        report.append("COLUMN verse_meta.status_changed_at already present")
    else:
        cur.execute("ALTER TABLE verse_meta ADD COLUMN status_changed_at TEXT")
        report.append("ADDED COLUMN verse_meta.status_changed_at")


def register_config(cur, report: list[str]) -> None:
    """cfg_column + cfg_enum + cfg_utility registration, same unit of work as the build -- same
    reasoning as create_verse_meta_table_v1_20260909.py's own register_config: documenting
    already-directed work, not a new runtime judgement call."""
    SRC = "1661-verse-meta-status-column (escalation #1661)"

    def _add_col(name: str, ordinal: int, use: str) -> None:
        exists = cur.execute(
            "SELECT 1 FROM cfg_column WHERE database='iba' AND table_name='verse_meta' "
            "AND name=?", (name,)).fetchone()
        if exists:
            report.append(f"cfg_column verse_meta.{name} already present — skipped")
            return
        cur.execute(
            "INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "
            "\"notnull\", is_unique, dflt, fk, \"use\", expectation, source, filled_by, "
            "inactive) VALUES ('iba','verse_meta',?,?,'TEXT',0,0,0,NULL,NULL,?,NULL,?,?,0)",
            (name, ordinal, use, SRC, "VerseMeta.ps1 -Step SetStatus (lib/versemeta.py)"))
        report.append(f"cfg_column verse_meta.{name} added")

    _add_col("status", 13,
              "Researcher-set verse status, one of cfg_enum verse_meta_status "
              "(exclude/citated/analysed). NULL = not yet set. Deliberately excludes 'anchor' -- "
              "that's already verse_meta.is_passage_anchor, per the researcher's own instruction. "
              "Written only by VerseMeta.ps1 -Step SetStatus, never by application code.")
    _add_col("status_changed_at", 14,
              "ISO-8601 UTC, set ONLY when `status` actually changes value (not touched on every "
              "write) -- the researcher's own 'stamped if the status change' requirement. NULL "
              "means status has never been set.")

    for value, ordinal in (("exclude", 0), ("citated", 1), ("analysed", 2)):
        exists = cur.execute(
            "SELECT 1 FROM cfg_enum WHERE name='verse_meta_status' AND value=?",
            (value,)).fetchone()
        if exists:
            report.append(f"cfg_enum verse_meta_status={value!r} already present — skipped")
            continue
        cur.execute(
            "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES "
            "('verse_meta_status', ?, ?, 0)", (value, ordinal))
        report.append(f"cfg_enum verse_meta_status={value!r} added")

    exists = cur.execute(
        "SELECT 1 FROM cfg_utility WHERE file_path="
        "'iba/app/migration/add_verse_meta_status_column_v1_20260910.py'").fetchone()
    if exists:
        report.append("cfg_utility for this script already present — skipped")
    else:
        cur.execute(
            "INSERT INTO cfg_utility (module, file_path, purpose, inactive, config_exempt, "
            "crash_escalation_reviewed) VALUES (?,?,?,0,0,0)",
            ("add_verse_meta_status_column_v1_20260910",
             "iba/app/migration/add_verse_meta_status_column_v1_20260910.py",
             "Adds verse_meta.status + verse_meta.status_changed_at (domain: cfg_enum "
             "verse_meta_status = exclude/citated/analysed; 'anchor' deliberately excluded, "
             "already verse_meta.is_passage_anchor). Idempotent, safe to re-run. Escalation "
             "#1661."))
        report.append("cfg_utility for add_verse_meta_status_column_v1_20260910.py added")


def validate(cur, report: list[str]) -> list[str]:
    problems = []
    if not column_exists(cur, "verse_meta", "status"):
        problems.append("verse_meta.status missing after migration")
    if not column_exists(cur, "verse_meta", "status_changed_at"):
        problems.append("verse_meta.status_changed_at missing after migration")

    bad = cur.execute(
        "SELECT COUNT(*) FROM verse_meta WHERE status IS NOT NULL "
        "AND status NOT IN (SELECT value FROM cfg_enum WHERE name='verse_meta_status')"
    ).fetchone()[0]
    if bad:
        problems.append(f"{bad} verse_meta rows have a status value outside cfg_enum "
                         f"verse_meta_status")
    else:
        report.append("0 out-of-domain status values")

    n = cur.execute("SELECT COUNT(*) FROM verse_meta WHERE status IS NOT NULL").fetchone()[0]
    report.append(f"{n} verse_meta rows have a status set (expect 0 immediately after this "
                  f"migration — set going forward via VerseMeta.ps1)")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = None
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")
        add_columns(cur, report)
        register_config(cur, report)
        problems = validate(cur, report)

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        if problems:
            print("\nVALIDATION PROBLEMS:")
            for p in problems:
                print("  -", p)
            return 1
        print("\nVALIDATION: clean")
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
