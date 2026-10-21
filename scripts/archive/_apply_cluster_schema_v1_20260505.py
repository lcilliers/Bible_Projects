"""_apply_cluster_schema_v1_20260505.py — DB-modifying.

Adds the cluster table and the cluster_code FK column on mti_terms,
populating both from the v6 term-anchor JSON (the locked source of truth
from 2026-05-04).

Schema:
  cluster(
    cluster_code      TEXT PRIMARY KEY,    -- 'M01'..'M46', 'T2', 'FLAG'
    description       TEXT,                -- longer-form description
    gloss             TEXT NOT NULL,       -- short canonical label
    source            TEXT,                -- e.g. 'meaning_v2'
    bucket            TEXT,                -- 'NAMED'|'SUPPLEMENTARY'|'REVIEW'
    status            TEXT,                -- 'active'|'proposed'|'archived'
    version           TEXT,                -- 'v6'
    last_updated_date TEXT                 -- ISO timestamp
  );

  ALTER TABLE mti_terms ADD COLUMN cluster_code TEXT
         REFERENCES cluster(cluster_code);
  CREATE INDEX idx_mti_terms_cluster ON mti_terms(cluster_code);

Behaviour:
  - Idempotent: skips create/alter if already exists; refreshes data on rerun.
  - Transactional: all writes in a single transaction; rollback on error.
  - Backup: creates a timestamped .bak copy of the DB before changes.
"""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
V6_PATH = "outputs/markdown/wa-term-anchor-v6-20260504.json"
BACKUP_DIR = "backups"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_cluster_schema.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def table_exists(conn, name) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (name,),
    ).fetchone() is not None


def column_exists(conn, table, col) -> bool:
    return any(
        r["name"] == col
        for r in conn.execute(f"PRAGMA table_info('{table}')").fetchall()
    )


def main() -> int:
    print(f"DB: {DB_PATH}")
    print(f"v6 anchor: {V6_PATH}")
    print()

    print("Loading v6 anchor...", flush=True)
    with open(V6_PATH, encoding="utf-8") as f:
        v6 = json.load(f)
    cluster_labels = v6.get("meaning_cluster_labels", {})
    if not cluster_labels:
        print("ERROR: v6 anchor has no meaning_cluster_labels.", flush=True)
        return 1
    term_anchors = v6.get("term_anchors", {})
    print(f"  cluster labels: {len(cluster_labels)}")
    print(f"  term anchors:   {len(term_anchors):,}")

    # Backup
    print()
    print("Backing up DB...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        conn.execute("BEGIN")

        # 1. cluster table
        if not table_exists(conn, "cluster"):
            print("\nCreating table 'cluster'...", flush=True)
            conn.execute("""
                CREATE TABLE cluster (
                    cluster_code      TEXT PRIMARY KEY,
                    description       TEXT,
                    gloss             TEXT NOT NULL,
                    source            TEXT,
                    bucket            TEXT,
                    status            TEXT,
                    version           TEXT,
                    last_updated_date TEXT
                )
            """)
        else:
            print("\nTable 'cluster' already exists — will refresh rows.",
                  flush=True)

        # 2. mti_terms.cluster_code column
        if not column_exists(conn, "mti_terms", "cluster_code"):
            print("Adding mti_terms.cluster_code column...", flush=True)
            conn.execute(
                "ALTER TABLE mti_terms ADD COLUMN cluster_code TEXT "
                "REFERENCES cluster(cluster_code)"
            )
        else:
            print("Column mti_terms.cluster_code already exists — will "
                  "refresh values.", flush=True)

        # 3. index
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_mti_terms_cluster "
            "ON mti_terms(cluster_code)"
        )

        # 4. populate cluster table
        print("\nPopulating cluster table...", flush=True)
        ts = now_iso()
        rows = []
        for cid in sorted(cluster_labels.keys()):
            label = cluster_labels[cid]
            if cid == "T2":
                bucket = "SUPPLEMENTARY"
            elif cid == "FLAG":
                bucket = "REVIEW"
            else:
                bucket = "NAMED"
            rows.append((
                cid,            # cluster_code
                label,          # description (initial = gloss)
                label,          # gloss
                "meaning_v2",   # source
                bucket,         # bucket
                "active",       # status
                "v6",           # version
                ts,             # last_updated_date
            ))
        conn.executemany("""
            INSERT INTO cluster
              (cluster_code, description, gloss, source, bucket, status,
               version, last_updated_date)
            VALUES (?,?,?,?,?,?,?,?)
            ON CONFLICT(cluster_code) DO UPDATE SET
                gloss = excluded.gloss,
                description = excluded.description,
                source = excluded.source,
                bucket = excluded.bucket,
                status = excluded.status,
                version = excluded.version,
                last_updated_date = excluded.last_updated_date
        """, rows)
        n_clusters = conn.execute(
            "SELECT COUNT(*) FROM cluster"
        ).fetchone()[0]
        print(f"  cluster rows: {n_clusters}")

        # 5. populate mti_terms.cluster_code
        print("\nPopulating mti_terms.cluster_code from v6...", flush=True)
        # Reset all to NULL first to handle re-runs cleanly
        conn.execute("UPDATE mti_terms SET cluster_code = NULL")
        update_rows = []
        for strong, anchor in term_anchors.items():
            cid = anchor.get("cluster_id")
            if cid:
                update_rows.append((cid, strong))
        # Bulk update by Strong's number
        n_updated = 0
        for cid, strong in update_rows:
            cur = conn.execute(
                "UPDATE mti_terms SET cluster_code = ? "
                "WHERE strongs_number = ? AND cluster_code IS NULL",
                (cid, strong),
            )
            n_updated += cur.rowcount
        print(f"  mti_terms updated: {n_updated:,}")

        # 6. verification
        print("\nVerifying...", flush=True)
        bucket_counts = {
            r["bucket"]: r["c"]
            for r in conn.execute(
                "SELECT bucket, COUNT(*) c FROM cluster GROUP BY bucket"
            ).fetchall()
        }
        print(f"  cluster buckets: {bucket_counts}")
        cluster_term_counts = conn.execute("""
            SELECT cluster_code, COUNT(*) AS c
              FROM mti_terms
             WHERE cluster_code IS NOT NULL
             GROUP BY cluster_code
             ORDER BY c DESC
        """).fetchall()
        total_assigned = sum(r["c"] for r in cluster_term_counts)
        print(f"  total terms with cluster_code: {total_assigned:,}")
        # Sanity vs v6
        v6_assigned = sum(
            1 for s, t in term_anchors.items() if t.get("cluster_id")
        )
        print(f"  v6 anchor assigned terms:      {v6_assigned:,}")
        if total_assigned != v6_assigned:
            print(f"  ⚠ mismatch: {v6_assigned - total_assigned} terms "
                  "in v6 but not matched in mti_terms by Strong's number")
        else:
            print("  ✅ counts match v6 exactly")

        # 7. show top 10 clusters by member count
        print("\n  Top 10 clusters by member count:")
        for r in cluster_term_counts[:10]:
            print(f"    {r['cluster_code']:<6s}  {r['c']:>4d}")

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
