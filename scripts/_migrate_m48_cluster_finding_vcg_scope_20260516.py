"""Schema migration M48 — add vcg_scope to cluster_finding + extend UNIQUE.

Bumps schema 3.21.0 → 3.22.0.

Rationale: v2_2 §14 introduces VCG-level scope for cluster_finding rows. Where AI's
Phase 9 output uses VCG-specific scope markers (e.g. [E-VCG-02], [E-VCG-01/03/04/05]),
the loader needs to store the VCG specificity as queryable structure rather than
folding it into row text.

Operations:
  1. Rebuild table cluster_finding with new column `vcg_scope TEXT` (nullable).
  2. Migrate the 6724 existing rows with vcg_scope=NULL (pre-v2_2 rows have whole-
     sub-group scope by default).
  3. Update UNIQUE constraint:
       FROM: (obs_id, cluster_code, cluster_subgroup_id, version)
       TO  : (obs_id, cluster_code, cluster_subgroup_id, vcg_scope, version)
       SQLite NULL-handling: each NULL is treated as distinct, so two rows with
       same other-fields and vcg_scope=NULL would still collide → safe; only
       VCG-specific rows can coexist with NULL-scoped row for same prompt × sub-group.
  4. Re-create indexes.
  5. Insert schema_version 3.22.0 row.
"""
from __future__ import annotations
import argparse, json, shutil, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def backup_db() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    name = f"bible_research_backup_{ts}_M48-vcg-scope.db"
    out = REPO / "backups" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def fetch_pre_rowcount(conn) -> int:
    return conn.execute("SELECT COUNT(*) AS n FROM cluster_finding").fetchone()["n"]


def fetch_schema_version(conn) -> str:
    r = conn.execute("SELECT version_code FROM schema_version ORDER BY rowid DESC LIMIT 1").fetchone()
    return r["version_code"]


def apply(conn) -> dict:
    pre_n = fetch_pre_rowcount(conn)
    log(f"  Pre-migration cluster_finding rowcount: {pre_n}")

    # 1. Build new table
    log("  Creating cluster_finding_new with vcg_scope column...")
    conn.execute("""
        CREATE TABLE cluster_finding_new (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            obs_id              INTEGER NOT NULL
                                REFERENCES wa_obs_question_catalogue(obs_id),
            cluster_code        TEXT NOT NULL
                                REFERENCES cluster(cluster_code),
            cluster_subgroup_id INTEGER
                                REFERENCES cluster_subgroup(id),
            vcg_scope           TEXT,
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
            UNIQUE (obs_id, cluster_code, cluster_subgroup_id, vcg_scope, version)
        )
    """)

    # 2. Migrate rows (vcg_scope=NULL for all pre-v2_2 rows)
    log("  Copying rows (vcg_scope=NULL on all pre-v2_2 rows)...")
    conn.execute("""
        INSERT INTO cluster_finding_new
            (id, obs_id, cluster_code, cluster_subgroup_id, vcg_scope,
             finding_status, finding_text, source_file, version, notes,
             delete_flagged, created_at, last_updated_date)
        SELECT
            id, obs_id, cluster_code, cluster_subgroup_id, NULL,
            finding_status, finding_text, source_file, version, notes,
            delete_flagged, created_at, last_updated_date
        FROM cluster_finding
    """)
    mid_n = conn.execute("SELECT COUNT(*) FROM cluster_finding_new").fetchone()[0]
    assert mid_n == pre_n, f"Row count mismatch: pre={pre_n} new={mid_n}"
    log(f"  Copied {mid_n} rows ✓")

    # 3. Drop old + rename
    log("  Dropping old cluster_finding...")
    conn.execute("DROP TABLE cluster_finding")
    conn.execute("ALTER TABLE cluster_finding_new RENAME TO cluster_finding")

    # 4. Re-create indexes
    log("  Re-creating indexes...")
    for idx_sql in [
        "CREATE INDEX ix_cluster_finding_cluster ON cluster_finding(cluster_code)",
        "CREATE INDEX ix_cluster_finding_subgroup ON cluster_finding(cluster_subgroup_id)",
        "CREATE INDEX ix_cluster_finding_obs ON cluster_finding(obs_id)",
        "CREATE INDEX ix_cluster_finding_status ON cluster_finding(finding_status)",
        "CREATE INDEX ix_cluster_finding_vcg_scope ON cluster_finding(vcg_scope)",
    ]:
        conn.execute(idx_sql)

    # 5. Insert schema_version 3.22.0
    log("  Inserting schema_version 3.22.0...")
    pre_version = fetch_schema_version(conn)
    log(f"     prev version: {pre_version}")
    # Read prior migration_history JSON
    prior_history_row = conn.execute(
        "SELECT migration_history FROM schema_version WHERE version_code=? LIMIT 1",
        (pre_version,)
    ).fetchone()
    history = json.loads(prior_history_row["migration_history"]) if prior_history_row else []
    history.append({
        "version": "M48",
        "description": "Add vcg_scope to cluster_finding + extend UNIQUE; schema 3.21.0 → 3.22.0 (v2_2 §14 vcg-level scope for Phase 9 findings)",
        "applied_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    })
    conn.execute(
        "INSERT INTO schema_version (version_code, applied_at, migration_history) VALUES (?, ?, ?)",
        ("3.22.0", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), json.dumps(history)),
    )

    return {"pre_rowcount": pre_n, "post_rowcount": mid_n}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Migration M48 — cluster_finding + vcg_scope")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("BEGIN")
        result = apply(conn)
        if dry_run:
            log("\nDRY-RUN — rolling back")
            conn.execute("ROLLBACK")
        else:
            log("\nCommitting...")
            conn.execute("COMMIT")
            # Verify post-commit
            n = conn.execute("SELECT COUNT(*) FROM cluster_finding").fetchone()[0]
            ver = fetch_schema_version(conn)
            log(f"  Verified post-commit: cluster_finding rows={n}, schema version={ver}")
        log(f"\nDONE — pre={result['pre_rowcount']} post={result['post_rowcount']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
