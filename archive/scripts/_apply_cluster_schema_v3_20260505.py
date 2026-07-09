"""_apply_cluster_schema_v3_20260505.py — DB-modifying.

Refines the cluster.gloss content so every distinct Strong's in the cluster
is represented (no gloss-collision collapsing). Format:

  "<gloss> (<translit>)"

Example: "contempt (buz), contempt (biz.za.von), contempt (ne.a.tsah-A), …"

Idempotent: rebuilds cluster.gloss every run from current mti_terms data.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_cluster_gloss_v3.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def main() -> int:
    print(f"DB: {DB_PATH}")
    bak = backup_db()
    print(f"Backup: {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        conn.execute("BEGIN")
        ts = now_iso()

        # Build per-Strong's gloss-with-translit, then GROUP_CONCAT per cluster
        rows = conn.execute("""
            SELECT cluster_code,
                   GROUP_CONCAT(item, ', ') AS gloss_list,
                   COUNT(*) AS n_terms
              FROM (
                SELECT cluster_code,
                       (gloss || ' (' || transliteration || ')') AS item
                  FROM (
                    SELECT DISTINCT
                           cluster_code, strongs_number, gloss, transliteration
                      FROM mti_terms
                     WHERE cluster_code IS NOT NULL
                       AND gloss IS NOT NULL AND gloss != ''
                  )
                 ORDER BY cluster_code, gloss, strongs_number
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
            """, (r["gloss_list"], ts, r["cluster_code"]))
            n_updated += 1
        print(f"Clusters refreshed: {n_updated}")

        # Verify with M06 sample
        r = conn.execute("""
            SELECT cluster_code, description, gloss
              FROM cluster
             WHERE cluster_code = 'M06'
        """).fetchone()
        n_items = r["gloss"].count(", ") + 1 if r["gloss"] else 0
        print(f"\nM06 sample:")
        print(f"  description: {r['description']}")
        print(f"  gloss length: {len(r['gloss'])} chars, "
              f"{n_items} items")
        print(f"  first 250 chars: {r['gloss'][:250]}…")

        conn.execute("COMMIT")
        print("\n✓ Committed.")
        return 0
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n✗ ERROR — rolled back: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
