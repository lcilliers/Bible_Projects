"""_apply_cluster_subgroup_schema_v1_20260506.py — DB-modifying.

M44: Cluster sub-group infrastructure.

Adds support for an intra-cluster sub-grouping layer (e.g. within M06
"Hate, Contempt and Hostility": Hatred / Contempt / Abhorrence /
Cruelty / Reproach / Hostility-Enmity).

Changes:
  1. CREATE TABLE cluster_subgroup
     - id (PK), cluster_code (FK → cluster.cluster_code), subgroup_code,
       label, core_description, sort_order, status, version, source,
       notes, delete_flagged, created_at, last_updated_date
     - UNIQUE (cluster_code, subgroup_code)
  2. INDEX cluster_subgroup(cluster_code)
  3. ALTER TABLE mti_terms ADD COLUMN cluster_subgroup_id INTEGER
     REFERENCES cluster_subgroup(id)
  4. INDEX mti_terms(cluster_subgroup_id)
  5. INSERT schema_version row 3.18.0 with M44 migration entry

No data is seeded for any cluster — that follows in a separate apply
script once researcher + AI confirm the term → sub-group mapping.

Idempotent: re-running detects an existing table / column / index and
skips that step. Always backed up first.
"""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

NEW_VERSION = "3.18.0"
MIGRATION_TAG = "M44"
MIGRATION_DESCRIPTION = (
    "Cluster sub-group infrastructure: cluster_subgroup table "
    "+ mti_terms.cluster_subgroup_id FK + indexes"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_cluster_subgroup.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def has_table(conn, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (name,),
    ).fetchone() is not None


def has_column(conn, table: str, col: str) -> bool:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return any(r["name"] == col for r in rows)


def has_index(conn, name: str) -> bool:
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='index' AND name=?",
        (name,),
    ).fetchone() is not None


def main() -> int:
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    actions = []

    try:
        conn.execute("BEGIN")

        # 1. cluster_subgroup table
        if not has_table(conn, "cluster_subgroup"):
            conn.execute("""
                CREATE TABLE cluster_subgroup (
                    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                    cluster_code        TEXT NOT NULL
                        REFERENCES cluster(cluster_code),
                    subgroup_code       TEXT NOT NULL,
                    label               TEXT NOT NULL,
                    core_description    TEXT,
                    sort_order          INTEGER DEFAULT 0,
                    status              TEXT,
                    version             TEXT,
                    source              TEXT,
                    notes               TEXT,
                    delete_flagged      INTEGER DEFAULT 0,
                    created_at          TEXT,
                    last_updated_date   TEXT,
                    UNIQUE (cluster_code, subgroup_code)
                )
            """)
            actions.append("CREATE TABLE cluster_subgroup")
        else:
            actions.append("SKIP: cluster_subgroup already exists")

        # 2. index on cluster_code (FK lookup)
        if not has_index(conn, "ix_cluster_subgroup_cluster_code"):
            conn.execute("""
                CREATE INDEX ix_cluster_subgroup_cluster_code
                  ON cluster_subgroup(cluster_code)
            """)
            actions.append("CREATE INDEX ix_cluster_subgroup_cluster_code")
        else:
            actions.append("SKIP: ix_cluster_subgroup_cluster_code exists")

        # 3. mti_terms.cluster_subgroup_id column
        if not has_column(conn, "mti_terms", "cluster_subgroup_id"):
            # SQLite cannot ADD COLUMN with inline REFERENCES enforcement,
            # but the column carries the FK declaration for documentation
            # and for future table-rebuild migrations.
            conn.execute("""
                ALTER TABLE mti_terms
                  ADD COLUMN cluster_subgroup_id INTEGER
                    REFERENCES cluster_subgroup(id)
            """)
            actions.append("ALTER mti_terms ADD cluster_subgroup_id")
        else:
            actions.append("SKIP: mti_terms.cluster_subgroup_id exists")

        # 4. index on mti_terms.cluster_subgroup_id
        if not has_index(conn, "ix_mti_terms_cluster_subgroup_id"):
            conn.execute("""
                CREATE INDEX ix_mti_terms_cluster_subgroup_id
                  ON mti_terms(cluster_subgroup_id)
            """)
            actions.append("CREATE INDEX ix_mti_terms_cluster_subgroup_id")
        else:
            actions.append("SKIP: ix_mti_terms_cluster_subgroup_id exists")

        # 5. schema_version bump
        latest = conn.execute(
            "SELECT version_code, migration_history FROM schema_version "
            "ORDER BY id DESC LIMIT 1"
        ).fetchone()
        if latest and latest["version_code"] == NEW_VERSION:
            actions.append(f"SKIP: schema_version already {NEW_VERSION}")
        else:
            try:
                history = json.loads(latest["migration_history"]) if latest else []
            except Exception:
                history = []
            history.append({
                "version": MIGRATION_TAG,
                "description": MIGRATION_DESCRIPTION,
                "applied_at": now_iso(),
            })
            conn.execute("""
                INSERT INTO schema_version
                  (version_code, applied_at, migration_history,
                   engine_min_version)
                VALUES (?, ?, ?, NULL)
            """, (NEW_VERSION, now_iso(), json.dumps(history)))
            actions.append(
                f"INSERT schema_version {NEW_VERSION} "
                f"(+{MIGRATION_TAG} migration entry)"
            )

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n✗ ERROR — rolled back: {e}")
        raise

    # --- Verification
    print("Actions:")
    for a in actions:
        print(f"  - {a}")
    print()

    print("Verification:")
    cols = conn.execute("PRAGMA table_info(cluster_subgroup)").fetchall()
    print(f"  cluster_subgroup: {len(cols)} columns")
    for r in cols:
        print(f"    {r['name']:22s} {r['type']:10s} "
              f"notnull={r['notnull']} pk={r['pk']}")

    cnt = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_subgroup"
    ).fetchone()
    print(f"  cluster_subgroup row count: {cnt['n']}")

    has_fk = has_column(conn, "mti_terms", "cluster_subgroup_id")
    print(f"  mti_terms.cluster_subgroup_id present: {has_fk}")

    sv = conn.execute(
        "SELECT version_code FROM schema_version "
        "ORDER BY id DESC LIMIT 1"
    ).fetchone()
    print(f"  schema_version: {sv['version_code']}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
