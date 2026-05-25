"""Schema migration M52 — add finding_citation table.

Bumps schema 3.25.0 → 3.26.0.

Rationale: per researcher direction 2026-05-25, extract structured citations from
the prose bodies of cluster_finding (4,158 rows) and cluster_observation rows into
a queryable table. Enables queries like "which findings cite Psa 51:4?", "which
characteristics cross-reference each other most often?", "where does H2398 cha.ta
appear in the analytical record?".

Polymorphic source: a row can cite from either cluster_finding or
cluster_observation. Four citation types: verse references (canonical book
chapter:verse), Strong's codes (H/G prefix + digits), cross-characteristic
references (CHAR-N mid-body, NOT the opening scope marker), and VCG codes
(derived layer — verse citations matched back to verse_context_group via the
verse_context join).

Operations:
  1. CREATE TABLE finding_citation
  2. Create indexes for the expected query patterns
  3. Insert schema_version 3.26.0 row

Idempotent: skipped if the table already exists.
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
    out = REPO / "backups" / f"bible_research_backup_{ts}_M52-finding-citation.db"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def table_exists(conn, name: str) -> bool:
    r = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone()
    return r is not None


def fetch_schema_version(conn) -> str:
    r = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY rowid DESC LIMIT 1"
    ).fetchone()
    return r["version_code"]


def apply(conn) -> dict:
    pre_version = fetch_schema_version(conn)
    log(f"  Prev schema version: {pre_version}")

    if table_exists(conn, "finding_citation"):
        log("  finding_citation already exists — skipping CREATE")
    else:
        log("  CREATE TABLE finding_citation")
        conn.execute("""
            CREATE TABLE finding_citation (
                id                INTEGER PRIMARY KEY AUTOINCREMENT,
                source_table      TEXT NOT NULL
                                  CHECK (source_table IN ('cluster_finding','cluster_observation')),
                source_id         INTEGER NOT NULL,
                citation_type     TEXT NOT NULL
                                  CHECK (citation_type IN ('verse','strongs','cross_char','vcg')),
                citation_value    TEXT NOT NULL,
                position          INTEGER,
                delete_flagged    INTEGER DEFAULT 0,
                created_at        TEXT
            )
        """)
        log("  CREATE INDEXes")
        for idx_sql in [
            "CREATE INDEX ix_fc_source ON finding_citation(source_table, source_id)",
            "CREATE INDEX ix_fc_type_value ON finding_citation(citation_type, citation_value)",
            "CREATE INDEX ix_fc_value ON finding_citation(citation_value)",
        ]:
            conn.execute(idx_sql)

    log("  Inserting schema_version 3.26.0 ...")
    prior_history_row = conn.execute(
        "SELECT migration_history FROM schema_version WHERE version_code=? LIMIT 1",
        (pre_version,)
    ).fetchone()
    history = json.loads(prior_history_row["migration_history"]) if prior_history_row else []
    history.append({
        "version": "M52",
        "description": (
            "Add finding_citation table (polymorphic; cluster_finding + cluster_observation "
            "as sources). Three citation types: verse refs, Strong's codes, cross-char refs."
        ),
        "applied_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    })
    conn.execute(
        "INSERT INTO schema_version (version_code, applied_at, migration_history) "
        "VALUES (?, ?, ?)",
        ("3.26.0", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
         json.dumps(history)),
    )

    n_existing = conn.execute(
        "SELECT COUNT(*) FROM finding_citation"
    ).fetchone()[0]
    return {"finding_citation_rowcount_post": n_existing}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()
    dry_run = not args.live

    log("Migration M52 — finding_citation table")
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
            ver = fetch_schema_version(conn)
            log(f"  Verified post-commit: schema version={ver}")
        log(f"\nDONE — {result}")
    except Exception:
        try: conn.execute("ROLLBACK")
        except Exception: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
