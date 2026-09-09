"""Drop `verse_meta.genre` -- researcher verdict, escalation #1608, 2026-09-09, same session it
was built in.

Verbatim: "Our focus on genre is noise. It really only is relevant in passage reading, and in this
study, the reason for reading wider than the current verse context is to resolve the 'reach' of the
operation of a characteristic. We are reading to find something specific, and not to understand an
entire passage... it has no real meaning or role." Then, on being told the column was marked
inactive rather than dropped: "you can remove the columns from the verse-meta table."

Scope: `verse_meta.genre` ONLY -- the researcher named `verse-meta` specifically.
`passage.genre` is a pre-existing column on older, more consequential infrastructure and was NOT
named for removal; it stays `inactive=1` (already applied, this session) rather than dropped.

This is a genuine schema change (ALTER TABLE ... DROP COLUMN), not just a cfg_column inactive flag
-- the column is gone, not hidden. The `cfg_column` row for it is DELETED, not left inactive
(an inactive row describing a column that no longer physically exists would itself be a fresh
coherence-check violation -- the mirror image of the CA-7 gap this same session already found and
fixed the other way around).

Safe to re-run: no-ops if the column is already gone.

Usage:
    python iba/app/migration/drop_verse_meta_genre_column_v1_20260909.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def column_exists(cur, table: str, col: str) -> bool:
    return any(r[1] == col for r in cur.execute(f"PRAGMA table_info({table})"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        if column_exists(cur, "verse_meta", "genre"):
            cur.execute("ALTER TABLE verse_meta DROP COLUMN genre")
            report.append("DROPPED verse_meta.genre")
        else:
            report.append("verse_meta.genre already absent — skipped")

        deleted = cur.execute(
            "DELETE FROM cfg_column WHERE database='iba' AND table_name='verse_meta' "
            "AND name='genre'"
        ).rowcount
        report.append(f"cfg_column verse_meta.genre row deleted ({deleted} row)")

        remaining = [r[1] for r in cur.execute("PRAGMA table_info(verse_meta)")]
        report.append(f"verse_meta now has {len(remaining)} columns: {remaining}")

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
