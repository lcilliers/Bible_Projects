"""_apply_cluster_schema_v2_20260505.py — DB-modifying.

Refines the cluster table content (no schema change beyond column-value
semantics):

  - description column = canonical short label (e.g. "Love, Compassion …")
  - gloss column = concatenation of all term glosses currently in the cluster
    (re-derived from mti_terms.cluster_code + mti_terms.gloss)
  - status column = 'Not started' for all rows (default for new clusters)

Valid status values (enforced in app code; not a DB CHECK constraint):
  'Not started', 'Data - In Progress', 'Analysis - In Progress',
  'Analysis Completed', 'Published'

Idempotent: safe to re-run; refreshes gloss from current mti_terms data.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

VALID_STATUS = (
    "Not started",
    "Data - In Progress",
    "Analysis - In Progress",
    "Analysis Completed",
    "Published",
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_cluster_schema_v2.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def main() -> int:
    print(f"DB: {DB_PATH}")
    print()
    print("Backing up DB...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        conn.execute("BEGIN")

        ts = now_iso()

        # 1. Re-populate gloss from concatenated term glosses
        print("\nDeriving gloss from term-glosses (alphabetical, distinct)...")
        rows = conn.execute("""
            SELECT cluster_code,
                   GROUP_CONCAT(gloss, ', ') AS combined_gloss,
                   COUNT(*) AS n_terms
              FROM (
                SELECT DISTINCT cluster_code, gloss
                  FROM mti_terms
                 WHERE cluster_code IS NOT NULL
                   AND gloss IS NOT NULL
                   AND gloss != ''
                 ORDER BY cluster_code, gloss
              )
             GROUP BY cluster_code
        """).fetchall()
        n_updated = 0
        for r in rows:
            conn.execute("""
                UPDATE cluster
                   SET gloss = ?,
                       last_updated_date = ?
                 WHERE cluster_code = ?
            """, (r["combined_gloss"], ts, r["cluster_code"]))
            n_updated += 1
        print(f"  clusters with refreshed gloss: {n_updated}")

        # 2. Reset status to 'Not started' for all (initial state)
        print("\nResetting status='Not started' for all clusters...")
        conn.execute(
            "UPDATE cluster SET status = 'Not started', "
            "last_updated_date = ?", (ts,)
        )
        n_status = conn.execute(
            "SELECT COUNT(*) FROM cluster WHERE status='Not started'"
        ).fetchone()[0]
        print(f"  rows with status='Not started': {n_status}")

        # 3. Verify
        print("\nVerifying...")
        n_total = conn.execute("SELECT COUNT(*) FROM cluster").fetchone()[0]
        n_with_gloss = conn.execute(
            "SELECT COUNT(*) FROM cluster WHERE gloss IS NOT NULL"
        ).fetchone()[0]
        print(f"  total cluster rows: {n_total}")
        print(f"  with gloss populated: {n_with_gloss}")

        print("\nSample (M05, M06, T2):")
        for cid in ("M05", "M06", "T2"):
            r = conn.execute(
                "SELECT cluster_code, description, gloss, bucket, status "
                "FROM cluster WHERE cluster_code = ?", (cid,)
            ).fetchone()
            if r:
                gloss = r["gloss"] or ""
                preview = gloss[:140] + ("…" if len(gloss) > 140 else "")
                print(f"  {r['cluster_code']:6s} description='{r['description']}'")
                print(f"         gloss={preview}")
                print(f"         bucket={r['bucket']} status='{r['status']}'")

        # 4. App-side validation note
        print(f"\nValid status values (enforce in app code):")
        for s in VALID_STATUS:
            print(f"  - '{s}'")

        conn.execute("COMMIT")
        print("\n✓ Committed.")
        return 0
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n✗ ERROR — rolled back: {e}", flush=True)
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
