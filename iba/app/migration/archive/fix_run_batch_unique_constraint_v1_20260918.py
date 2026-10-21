"""Fix `run_batch`'s own design bug, found live minutes after it shipped (escalation #1756's build,
#1758): `UNIQUE(step, selector_key, batch_content_key)` was meant to prevent re-paying for already-
COMMITTED work, but it actually blocks ANY second INSERT at that key -- including a legitimate
retry after a transient failure (M49/C_thankful_disposition hit a DNS resolution error, `start_
batch()`'s own retry then failed on `IntegrityError: UNIQUE constraint failed`, unable to even
record the retry attempt). The resume/skip guarantee was never meant to live in the schema -- it's
`batchcontrol.already_committed()`'s own `WHERE status='committed'` check, consulted BEFORE
`start_batch()` runs, that actually enforces "never re-pay for committed work". The UNIQUE
constraint was a redundant, over-tight belt-and-braces that broke the exact retry path the crash
safeguard exists for.

Fix: recreate `run_batch` with a plain (non-unique) index on `(step, selector_key,
batch_content_key)` for lookup performance, dropping the UNIQUE constraint. SQLite has no ALTER
TABLE DROP CONSTRAINT -- recreate-and-copy is the standard pattern. Preserves all existing rows.

Safe to re-run: no-ops if the UNIQUE constraint is already gone.

Usage:
    python iba/app/migration/fix_run_batch_unique_constraint_v1_20260918.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def has_unique_constraint(cur) -> bool:
    row = cur.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='run_batch'").fetchone()
    return row is not None and "UNIQUE (step, selector_key, batch_content_key)" in row[0]


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

        if not has_unique_constraint(cur):
            report.append("run_batch has no UNIQUE(step, selector_key, batch_content_key) "
                          "constraint -- already fixed, skipped")
        else:
            before = cur.execute("SELECT COUNT(*) FROM run_batch").fetchone()[0]
            cur.execute("DROP INDEX IF EXISTS idx_run_batch_run_id")
            cur.execute("DROP INDEX IF EXISTS idx_run_batch_status")
            cur.execute("ALTER TABLE run_batch RENAME TO run_batch_old")
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
                    cost_usd            REAL
                )
            """)
            cur.execute("""
                INSERT INTO run_batch (id, run_id, work_package, step, selector_key, batch_ordinal,
                    batch_content_key, status, started_at, ended_at, error_message, cost_usd)
                SELECT id, run_id, work_package, step, selector_key, batch_ordinal,
                    batch_content_key, status, started_at, ended_at, error_message, cost_usd
                FROM run_batch_old
            """)
            after = cur.execute("SELECT COUNT(*) FROM run_batch").fetchone()[0]
            cur.execute("DROP TABLE run_batch_old")
            cur.execute("CREATE INDEX idx_run_batch_run_id ON run_batch (run_id)")
            cur.execute("CREATE INDEX idx_run_batch_status ON run_batch (status)")
            cur.execute("CREATE INDEX idx_run_batch_lookup ON run_batch "
                       "(step, selector_key, batch_content_key)")
            if before != after:
                raise RuntimeError(f"row count mismatch after migration: {before} -> {after}")
            report.append(f"recreated run_batch WITHOUT the UNIQUE constraint, "
                         f"non-unique idx_run_batch_lookup added instead -- {after} row(s) preserved")

        # cfg_column.use for batch_content_key no longer says "part of the resume/skip key" via a
        # schema UNIQUE -- correct the text so it doesn't claim a guarantee the schema no longer
        # makes (the guarantee is application-level, in batchcontrol.already_committed()).
        cur.execute(
            "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='run_batch' "
            "AND name='batch_content_key'",
            ("stable hash (batchcontrol.content_key) of the batch's own actual item list (verse "
             "ids, or member strongs) -- content-keyed, not position-keyed, so resume is correct "
             "even if the underlying item list shifts between runs. Indexed together with "
             "step/selector_key for lookup performance, but NOT unique -- the resume/skip "
             "guarantee lives in batchcontrol.already_committed()'s own WHERE status='committed' "
             "check, consulted before start_batch() runs, not in a schema constraint (a UNIQUE "
             "constraint here was tried first and found live, #1758, to incorrectly block a "
             "legitimate retry after a failed attempt at the same content).",))
        report.append("cfg_column.use corrected for run_batch.batch_content_key")

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
