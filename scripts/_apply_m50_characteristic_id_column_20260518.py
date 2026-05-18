"""M50 schema migration: add characteristic_id column to cluster_finding.

Per researcher direction 2026-05-18: Phase 9 findings are authored at
CHARACTERISTIC scope (not sub-group). Need a column to disambiguate
characteristic-scope rows from CLUSTER-scope rows (both have
cluster_subgroup_id=NULL today).

SQLite cannot drop UNIQUE constraints in place; the migration uses the
table-rebuild pattern (PRAGMA foreign_keys=OFF; CREATE new; INSERT…
SELECT; DROP old; RENAME).

Schema bump: 3.23.0 → 3.24.0
"""
from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    current = cur.execute(
        "SELECT version_code, migration_history FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    if current[0] != "3.23.0":
        raise RuntimeError(f"Expected schema 3.23.0, got {current[0]!r}")

    print(f"Current schema_version: {current[0]}")

    # Pre-check: count cluster_finding rows for verification
    pre_count = cur.execute("SELECT COUNT(*) FROM cluster_finding").fetchone()[0]
    print(f"cluster_finding rows pre-migration: {pre_count}")

    cur.execute("PRAGMA foreign_keys = OFF")
    cur.execute("BEGIN")
    try:
        # 1. Create new table with characteristic_id + extended UNIQUE
        cur.execute("""
            CREATE TABLE cluster_finding_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                obs_id INTEGER NOT NULL
                    REFERENCES wa_obs_question_catalogue(obs_id),
                cluster_code TEXT NOT NULL
                    REFERENCES cluster(cluster_code),
                characteristic_id INTEGER
                    REFERENCES characteristic(id),
                cluster_subgroup_id INTEGER
                    REFERENCES cluster_subgroup(id),
                vcg_scope TEXT,
                finding_status TEXT NOT NULL
                    CHECK (finding_status IN ('finding','silent','gap','cluster_synthesis')),
                finding_text TEXT,
                source_file TEXT,
                version TEXT,
                notes TEXT,
                delete_flagged INTEGER DEFAULT 0,
                created_at TEXT,
                last_updated_date TEXT,
                UNIQUE (obs_id, cluster_code, characteristic_id, cluster_subgroup_id, vcg_scope, version)
            )
        """)
        print("  CREATE TABLE cluster_finding_new (with characteristic_id + extended UNIQUE)")

        # 2. Copy data from old table
        cur.execute("""
            INSERT INTO cluster_finding_new (
                id, obs_id, cluster_code, characteristic_id, cluster_subgroup_id, vcg_scope,
                finding_status, finding_text, source_file, version, notes, delete_flagged,
                created_at, last_updated_date
            )
            SELECT
                id, obs_id, cluster_code, NULL, cluster_subgroup_id, vcg_scope,
                finding_status, finding_text, source_file, version, notes, delete_flagged,
                created_at, last_updated_date
            FROM cluster_finding
        """)
        copied = cur.rowcount
        print(f"  Copied {copied} rows from cluster_finding (all with characteristic_id=NULL)")

        # 3. Drop old, rename new
        cur.execute("DROP TABLE cluster_finding")
        cur.execute("ALTER TABLE cluster_finding_new RENAME TO cluster_finding")
        print("  DROP old; RENAME new → cluster_finding")

        # 4. Re-create the AUTOINCREMENT sequence by resetting sqlite_sequence (optional)
        # Done implicitly via PRIMARY KEY AUTOINCREMENT in CREATE.

        # 5. Update schema_version
        history = json.loads(current[1])
        history.append({
            "version": "M50",
            "description": "Add characteristic_id column to cluster_finding; extend UNIQUE to include characteristic_id (Phase 9 at characteristic scope per researcher direction 2026-05-18)",
            "applied_at": NOW_UTC,
        })
        cur.execute(
            "INSERT INTO schema_version (version_code, applied_at, migration_history) VALUES (?, ?, ?)",
            ("3.24.0", NOW_UTC, json.dumps(history)),
        )
        print("  schema_version: 3.23.0 → 3.24.0 (M50)")

        # Verify FK integrity after rebuild
        cur.execute("PRAGMA foreign_key_check")
        violations = cur.fetchall()
        if violations:
            print(f"  FK violations after rebuild: {violations}")
            raise RuntimeError("FK violations detected")

        conn.commit()
        print("\n=== Committed ===")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        cur.execute("PRAGMA foreign_keys = ON")

    # Verify
    post_count = cur.execute("SELECT COUNT(*) FROM cluster_finding").fetchone()[0]
    print(f"\ncluster_finding rows post-migration: {post_count} (expected {pre_count})")
    assert post_count == pre_count, "row count mismatch"

    cols = [r[1] for r in cur.execute("PRAGMA table_info('cluster_finding')").fetchall()]
    print(f"cluster_finding columns: {cols}")
    assert 'characteristic_id' in cols

    null_char = cur.execute("SELECT COUNT(*) FROM cluster_finding WHERE characteristic_id IS NULL").fetchone()[0]
    print(f"Rows with characteristic_id IS NULL: {null_char} (existing v2_4 rows all NULL initially — expected)")

    conn.close()


if __name__ == "__main__":
    main()
