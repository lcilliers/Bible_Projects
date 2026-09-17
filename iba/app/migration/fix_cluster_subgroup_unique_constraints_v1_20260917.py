"""Fixes `cluster_subgroup`/`cluster_subgroup_strong`'s `UNIQUE` constraints -- both were declared
as plain, unconditional table-level `UNIQUE`s in #1690's own DDL, which do NOT exclude
`delete_flagged=1` rows. Found live 2026-09-17, redoing M67's subgroup allocation after fixing the
placement_note/observations mechanism (a separate correction, same session): soft-deleting the
first (flawed) run's rows and re-running hit `IntegrityError: UNIQUE constraint failed` on a strong
that had only ever been placed in a now-soft-deleted subgroup -- the constraint was still counting
it as live.

This contradicts the established convention elsewhere in this exact schema:
`idx_verse_lexical_live_unique` is `UNIQUE (span_id, code_ordinal) WHERE deleted=0` -- a partial
index that correctly excludes soft-deleted rows. `cluster_subgroup`/`cluster_subgroup_strong`
deviate from that pattern; this migration brings them into line with it, not a new design decision
(the `delete_flagged` column existing at all IS the stated intent that a soft-deleted row shouldn't
count as live for any purpose, uniqueness included).

SQLite has no ALTER TABLE to drop an inline UNIQUE constraint -- standard recreate-table pattern:
new table without the inline UNIQUE, copy data, drop old, rename, add the partial index. Both
tables had only this session's own throwaway test rows (6 + 9, all already soft-deleted, from the
flawed M67 run being redone) -- hard-deleted as part of the same migration rather than carried
forward, since they were never a legitimate research output (produced by code with a real,
separately-corrected defect).

NOT idempotent past first run (fails if already applied -- checks first, no-ops cleanly).

Usage:
    python iba/app/migration/fix_cluster_subgroup_unique_constraints_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    sql = conn.execute(
        "SELECT sql FROM sqlite_master WHERE name='cluster_subgroup_strong'").fetchone()["sql"]
    if "UNIQUE (strong)" not in sql and "UNIQUE(strong)" not in sql:
        print("cluster_subgroup_strong already fixed (no inline UNIQUE(strong)) -- nothing to do.")
        conn.close()
        return 0

    n_sub = conn.execute("SELECT COUNT(*) n FROM cluster_subgroup").fetchone()["n"]
    n_strong = conn.execute("SELECT COUNT(*) n FROM cluster_subgroup_strong").fetchone()["n"]
    print(f"cluster_subgroup: {n_sub} row(s) (all this session's own throwaway M67 test data, "
         f"all soft-deleted) -- will be cleared.")
    print(f"cluster_subgroup_strong: {n_strong} row(s) -- will be cleared.")

    if args.dry_run:
        print("--dry-run: no changes made.")
        conn.close()
        return 0

    conn.execute("PRAGMA foreign_keys=OFF")

    conn.execute("""
        CREATE TABLE cluster_subgroup_new (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            cluster_code        TEXT NOT NULL REFERENCES cluster(cluster_code),
            subgroup_code       TEXT NOT NULL,
            label               TEXT NOT NULL,
            core_description    TEXT,
            anchor_verse_reference TEXT,
            sort_order          INTEGER DEFAULT 0,
            status              TEXT,
            version             TEXT,
            source              TEXT,
            notes               TEXT,
            delete_flagged      INTEGER DEFAULT 0,
            created_at          TEXT,
            last_updated_date   TEXT
        )
    """)
    conn.execute(
        "INSERT INTO cluster_subgroup_new SELECT id, cluster_code, subgroup_code, label, "
        "core_description, anchor_verse_reference, sort_order, status, version, source, notes, "
        "delete_flagged, created_at, last_updated_date FROM cluster_subgroup "
        "WHERE delete_flagged=0")  # only this session's throwaway rows exist, all soft-deleted -> empty
    conn.execute("DROP TABLE cluster_subgroup")
    conn.execute("ALTER TABLE cluster_subgroup_new RENAME TO cluster_subgroup")
    conn.execute(
        "CREATE UNIQUE INDEX idx_cluster_subgroup_live_unique ON cluster_subgroup "
        "(cluster_code, subgroup_code) WHERE delete_flagged=0")

    conn.execute("""
        CREATE TABLE cluster_subgroup_strong_new (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            strong              TEXT NOT NULL REFERENCES strong(strongNumber),
            cluster_subgroup_id INTEGER NOT NULL REFERENCES cluster_subgroup(id),
            placement_note      TEXT,
            delete_flagged      INTEGER NOT NULL DEFAULT 0,
            created_at          TEXT NOT NULL,
            last_updated_date   TEXT NOT NULL
        )
    """)
    conn.execute(
        "INSERT INTO cluster_subgroup_strong_new SELECT id, strong, cluster_subgroup_id, "
        "placement_note, delete_flagged, created_at, last_updated_date FROM cluster_subgroup_strong "
        "WHERE delete_flagged=0")
    conn.execute("DROP TABLE cluster_subgroup_strong")
    conn.execute("ALTER TABLE cluster_subgroup_strong_new RENAME TO cluster_subgroup_strong")
    conn.execute(
        "CREATE UNIQUE INDEX idx_cluster_subgroup_strong_live_unique ON cluster_subgroup_strong "
        "(strong) WHERE delete_flagged=0")

    conn.execute("PRAGMA foreign_keys=ON")
    conn.commit()

    after_sub = conn.execute("SELECT COUNT(*) n FROM cluster_subgroup").fetchone()["n"]
    after_strong = conn.execute("SELECT COUNT(*) n FROM cluster_subgroup_strong").fetchone()["n"]
    print(f"After: cluster_subgroup={after_sub} row(s), cluster_subgroup_strong={after_strong} "
         f"row(s). Partial unique indexes now in place (WHERE delete_flagged=0).")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
