"""_apply_cluster_finding_schema_v1_20260506.py — DB-modifying.

M45: Cluster-level findings table.

Stores atomic findings produced by Claude AI's catalogue-prompt pass for
each (cluster × sub-group × catalogue prompt) cell. Coexists with the
older `wa_session_research_flags` (registry-scope findings) — does not
replace it.

Schema:
  cluster_finding
    id                  INTEGER PK
    obs_id              INTEGER FK → wa_obs_question_catalogue.obs_id
    cluster_code        TEXT FK → cluster.cluster_code  (NOT NULL)
    cluster_subgroup_id INTEGER FK → cluster_subgroup.id  (NULL = cluster-level)
    finding_status      TEXT in ('finding','silent','gap','cluster_synthesis')
    finding_text        TEXT
    source_file         TEXT
    version             TEXT
    notes               TEXT
    delete_flagged      INTEGER DEFAULT 0
    created_at          TEXT
    last_updated_date   TEXT
    UNIQUE (obs_id, cluster_code, cluster_subgroup_id, version)

Indexes:
  ix_cluster_finding_cluster   (cluster_code)
  ix_cluster_finding_subgroup  (cluster_subgroup_id)
  ix_cluster_finding_obs       (obs_id)
  ix_cluster_finding_status    (finding_status)

Idempotent: skips on re-run if structures exist.
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

NEW_VERSION = "3.19.0"
MIGRATION_TAG = "M45"
MIGRATION_DESCRIPTION = (
    "Cluster-level findings table for catalogue-prompt-anchored findings"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db() -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_cluster_finding.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def has_table(conn, name):
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def has_index(conn, name):
    return conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='index' AND name=?", (name,)
    ).fetchone() is not None


def main():
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    actions = []
    try:
        conn.execute("BEGIN")

        if not has_table(conn, "cluster_finding"):
            conn.execute("""
                CREATE TABLE cluster_finding (
                    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                    obs_id              INTEGER NOT NULL
                                        REFERENCES wa_obs_question_catalogue(obs_id),
                    cluster_code        TEXT NOT NULL
                                        REFERENCES cluster(cluster_code),
                    cluster_subgroup_id INTEGER
                                        REFERENCES cluster_subgroup(id),
                    finding_status      TEXT NOT NULL
                                        CHECK (finding_status IN
                                          ('finding','silent','gap','cluster_synthesis')),
                    finding_text        TEXT,
                    source_file         TEXT,
                    version             TEXT,
                    notes               TEXT,
                    delete_flagged      INTEGER DEFAULT 0,
                    created_at          TEXT,
                    last_updated_date   TEXT,
                    UNIQUE (obs_id, cluster_code, cluster_subgroup_id, version)
                )
            """)
            actions.append("CREATE TABLE cluster_finding")
        else:
            actions.append("SKIP: cluster_finding already exists")

        for name, cols in [
            ("ix_cluster_finding_cluster",  "cluster_code"),
            ("ix_cluster_finding_subgroup", "cluster_subgroup_id"),
            ("ix_cluster_finding_obs",      "obs_id"),
            ("ix_cluster_finding_status",   "finding_status"),
        ]:
            if not has_index(conn, name):
                conn.execute(
                    f"CREATE INDEX {name} ON cluster_finding({cols})"
                )
                actions.append(f"CREATE INDEX {name}")
            else:
                actions.append(f"SKIP: {name} already exists")

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
            conn.execute(
                "INSERT INTO schema_version "
                "  (version_code, applied_at, migration_history, "
                "   engine_min_version) "
                "VALUES (?, ?, ?, NULL)",
                (NEW_VERSION, now_iso(), json.dumps(history)),
            )
            actions.append(
                f"INSERT schema_version {NEW_VERSION} (+{MIGRATION_TAG})"
            )

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] ERROR — rolled back: {e}")
        raise

    print("Actions:")
    for a in actions:
        print(f"  - {a}")
    print()

    cols = conn.execute("PRAGMA table_info(cluster_finding)").fetchall()
    print(f"cluster_finding: {len(cols)} columns")
    for r in cols:
        print(f"  {r['name']:22s} {r['type']:10s} notnull={r['notnull']} pk={r['pk']}")

    sv = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    print(f"\nschema_version: {sv['version_code']}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
