"""Drop `cluster.gloss` (`iba.db`), escalation #1720. Researcher, verbatim: "I dont think it make
sense to have gloss on cluster level. gloss is a strong level entity. this column can be removed."

Background: `cluster.gloss` was a one-time migration snapshot (`cfg_column.source =
'migrated:bible_research.db.cluster'`, `filled_by = NULL`, no live refresh mechanism ever
registered) -- 48 of 95 live clusters had NULL/empty gloss simply because they were added, or
never got a value, after that migration ran, and nothing since had backfilled them (#1720's
original finding). Rather than backfill a field the researcher judges shouldn't exist at this
grain at all, it is removed.

Two live call sites depended on it, both fixed in the same unit of work as this migration:
- `iba/app/lib/clusterassign.py:match_precedent` -- P2 (cluster.gloss worked-example match)
  removed; P1 (strong.stepGloss, the strong-level signal the researcher confirmed IS correct)
  unchanged and still the whole mechanism.
- `iba/app/lib/clusterreport.py` (backfill-vocabulary crossmatch section) -- `word_to_clusters`
  rebuilt from live `cluster_strong` + `strong.stepGloss` membership instead of the static
  `cluster.gloss` snapshot; strictly better, now covers all 95 clusters instead of only the 47
  that happened to have a gloss value.

Two one-off migration scripts also referenced `cluster.gloss` (`allocate_strongs.py`,
`fix_cluster_anomalies_v2_20260917.py`) -- left untouched as historical record; neither is a live,
re-runnable tool (no PS script or cfg_utility references either).

`cfg_column` row for `iba.cluster.gloss` is deleted (not just marked inactive) -- the column
itself is gone, so a lingering "registered but inactive" row would be misleading, unlike a
retired-but-still-present table/step. The `bible_research.database.cluster.gloss` cfg_column row
is a different, historical source-DB registration, left untouched -- out of scope, not what was
asked.

NOT idempotent past first run (DROP COLUMN fails if already dropped) -- checks first and no-ops
cleanly if already applied.

Usage:
    python iba/app/migration/drop_cluster_gloss_v1_20260917.py [--db PATH] [--dry-run]
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

    cols = [r["name"] for r in conn.execute("PRAGMA table_info(cluster)")]
    if "gloss" not in cols:
        print("cluster.gloss already dropped -- nothing to do.")
        conn.close()
        return 0

    cfg_row = conn.execute(
        "SELECT * FROM cfg_column WHERE database='iba' AND table_name='cluster' AND name='gloss'"
    ).fetchone()
    print("cluster.gloss present. cfg_column row:", dict(cfg_row) if cfg_row else None)

    if args.dry_run:
        print("--dry-run: no changes made.")
        conn.close()
        return 0

    conn.execute("ALTER TABLE cluster DROP COLUMN gloss")
    conn.execute(
        "DELETE FROM cfg_column WHERE database='iba' AND table_name='cluster' AND name='gloss'")
    conn.commit()

    cols_after = [r["name"] for r in conn.execute("PRAGMA table_info(cluster)")]
    remaining = conn.execute(
        "SELECT COUNT(*) n FROM cfg_column WHERE database='iba' AND table_name='cluster' "
        "AND name='gloss'").fetchone()["n"]
    print("After: cluster columns =", cols_after)
    print("After: cfg_column rows for iba.cluster.gloss =", remaining)

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
