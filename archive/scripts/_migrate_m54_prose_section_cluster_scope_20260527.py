"""Schema migration M54 — extend prose_section with cluster scope columns.

Bumps schema 3.27.0 → 3.28.0.

Rationale: prose_section was designed pre-cluster-pivot for per-word prose
(registry_id scope). v3_0 publication pipeline needs cluster-scope and
characteristic-scope prose (per-tier publication prose authored during Phase 9,
per-chapter assembly for Session C, per-sub-group narrative). Add the columns,
extend the FTS5 index to include cluster_code as a filterable field.

Operations:
  1. ALTER TABLE prose_section ADD COLUMN cluster_code TEXT
  2. ALTER TABLE prose_section ADD COLUMN characteristic_id INTEGER
  3. ALTER TABLE prose_section ADD COLUMN cluster_subgroup_id INTEGER
  4. Indexes on each new column
  5. DROP + RECREATE prose_section_fts with cluster_code as new UNINDEXED column
  6. DROP + RECREATE the three FTS sync triggers (ai/au/ad)
  7. Re-populate prose_section_fts from prose_section
  8. Insert schema_version 3.28.0 row

The FTS rebuild is necessary because FTS5 doesn't support ALTER on its column list.
ai/au/ad triggers also re-issued because their column list must match the new FTS.

Idempotent: skipped if cluster_code column already exists.
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


def column_exists(conn, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f"PRAGMA table_info({table})"))


def fetch_schema_version(conn) -> str:
    r = conn.execute("SELECT version_code FROM schema_version ORDER BY rowid DESC LIMIT 1").fetchone()
    return r[0]


def apply(conn) -> dict:
    pre = fetch_schema_version(conn)
    log(f"  Prev schema version: {pre}")

    if column_exists(conn, "prose_section", "cluster_code"):
        log("  cluster_code already present — migration appears applied, skipping ALTERs")
    else:
        log("  ALTER TABLE prose_section ADD cluster_code, characteristic_id, cluster_subgroup_id")
        conn.execute("ALTER TABLE prose_section ADD COLUMN cluster_code TEXT")
        conn.execute("ALTER TABLE prose_section ADD COLUMN characteristic_id INTEGER")
        conn.execute("ALTER TABLE prose_section ADD COLUMN cluster_subgroup_id INTEGER")
        log("  CREATE INDEX idx_prose_section_cluster_code")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_prose_section_cluster_code ON prose_section(cluster_code) WHERE cluster_code IS NOT NULL")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_prose_section_characteristic_id ON prose_section(characteristic_id) WHERE characteristic_id IS NOT NULL")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_prose_section_cluster_subgroup_id ON prose_section(cluster_subgroup_id) WHERE cluster_subgroup_id IS NOT NULL")

    # FTS rebuild — drop + recreate to add cluster_code as UNINDEXED filter column
    log("  DROP existing FTS triggers")
    for trig in ("prose_section_ai", "prose_section_au", "prose_section_ad"):
        conn.execute(f"DROP TRIGGER IF EXISTS {trig}")
    log("  DROP existing prose_section_fts")
    conn.execute("DROP TABLE IF EXISTS prose_section_fts")

    log("  CREATE prose_section_fts with cluster_code column")
    conn.execute("""
        CREATE VIRTUAL TABLE prose_section_fts USING fts5(
            body,
            heading,
            section_type_code UNINDEXED,
            registry_id UNINDEXED,
            cluster_code UNINDEXED,
            characteristic_id UNINDEXED,
            status UNINDEXED,
            tokenize='porter unicode61 remove_diacritics 2'
        )
    """)

    log("  CREATE FTS sync triggers (ai/au/ad)")
    conn.execute("""
        CREATE TRIGGER prose_section_ai AFTER INSERT ON prose_section BEGIN
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code,
                                          registry_id, cluster_code, characteristic_id, status)
            VALUES (new.id, new.body, new.heading,
                    (SELECT code FROM prose_section_type WHERE id=new.section_type_id),
                    new.registry_id, new.cluster_code, new.characteristic_id, new.status);
        END
    """)
    conn.execute("""
        CREATE TRIGGER prose_section_au AFTER UPDATE ON prose_section BEGIN
            INSERT INTO prose_section_fts(prose_section_fts, rowid, body, heading,
                                          section_type_code, registry_id, cluster_code,
                                          characteristic_id, status)
            VALUES ('delete', old.id, old.body, old.heading,
                    (SELECT code FROM prose_section_type WHERE id=old.section_type_id),
                    old.registry_id, old.cluster_code, old.characteristic_id, old.status);
            INSERT INTO prose_section_fts(rowid, body, heading, section_type_code,
                                          registry_id, cluster_code, characteristic_id, status)
            VALUES (new.id, new.body, new.heading,
                    (SELECT code FROM prose_section_type WHERE id=new.section_type_id),
                    new.registry_id, new.cluster_code, new.characteristic_id, new.status);
        END
    """)
    conn.execute("""
        CREATE TRIGGER prose_section_ad AFTER DELETE ON prose_section BEGIN
            INSERT INTO prose_section_fts(prose_section_fts, rowid, body, heading,
                                          section_type_code, registry_id, cluster_code,
                                          characteristic_id, status)
            VALUES ('delete', old.id, old.body, old.heading,
                    (SELECT code FROM prose_section_type WHERE id=old.section_type_id),
                    old.registry_id, old.cluster_code, old.characteristic_id, old.status);
        END
    """)

    log("  Re-populate prose_section_fts from prose_section")
    conn.execute("""
        INSERT INTO prose_section_fts(rowid, body, heading, section_type_code,
                                      registry_id, cluster_code, characteristic_id, status)
        SELECT ps.id, ps.body, ps.heading, pst.code,
               ps.registry_id, ps.cluster_code, ps.characteristic_id, ps.status
        FROM prose_section ps
        JOIN prose_section_type pst ON pst.id = ps.section_type_id
        WHERE COALESCE(ps.delete_flagged,0)=0
    """)
    n_fts = conn.execute("SELECT COUNT(*) FROM prose_section_fts").fetchone()[0]
    log(f"  prose_section_fts rows post-rebuild: {n_fts:,}")

    new_version = "3.28.0"
    log(f"  INSERT schema_version {pre} -> {new_version}")
    prior_row = conn.execute(
        "SELECT migration_history FROM schema_version WHERE version_code=? ORDER BY rowid DESC LIMIT 1",
        (pre,),
    ).fetchone()
    history = json.loads(prior_row["migration_history"]) if prior_row and prior_row["migration_history"] else []
    history.append({
        "version": "M54",
        "description": "Extended prose_section with cluster_code + characteristic_id + cluster_subgroup_id columns; rebuilt prose_section_fts and its three sync triggers to include cluster_code and characteristic_id as UNINDEXED filter columns. Enables cluster-scope publication prose storage and FTS filtering by cluster.",
        "applied_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    })
    conn.execute(
        "INSERT INTO schema_version (version_code, applied_at, migration_history) VALUES (?, ?, ?)",
        (new_version, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), json.dumps(history)),
    )
    return {"pre_version": pre, "new_version": new_version, "fts_rows": n_fts}


def main(live: bool) -> int:
    print(f"=== M54 migration — mode={'LIVE' if live else 'DRY-RUN'} ===")
    if live:
        latest_backup = sorted((REPO / "backups").glob("bible_research_backup_*.db"))
        if latest_backup:
            log(f"  Using latest existing backup: {latest_backup[-1].relative_to(REPO)}")
        else:
            ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            backup = REPO / "backups" / f"bible_research_backup_{ts}_M54-prose-cluster-scope.db"
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(DB, backup)
            log(f"  Backup: {backup.relative_to(REPO)}")

    conn = sqlite3.connect(DB, timeout=120.0)
    conn.execute("PRAGMA busy_timeout = 120000")
    conn.row_factory = sqlite3.Row

    if not live:
        # In dry-run: introspect current state, print plan, no writes
        print(f"Current schema version: {fetch_schema_version(conn)}")
        print(f"prose_section has cluster_code: {column_exists(conn, 'prose_section', 'cluster_code')}")
        print(f"prose_section has characteristic_id: {column_exists(conn, 'prose_section', 'characteristic_id')}")
        print("[DRY-RUN — no writes]")
        conn.close()
        return 0

    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    try:
        result = apply(conn)
        conn.commit()
        print(f"\nCOMMITTED: {result}")
    except Exception as e:
        conn.rollback()
        print(f"ROLLED BACK: {e}")
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    sys.exit(main(args.live))
