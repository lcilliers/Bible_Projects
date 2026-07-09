"""Schema migration M51 — add verse_context.keywords TEXT.

Bumps schema 3.24.0 → 3.25.0.

Rationale: per researcher direction 2026-05-23, the Phase 2 Pass A pass now produces
both the `analysis_note` (one-line meaning) AND a set of inner-being keywords per
verse, in the same API call. Keywords are atomic (1-2 word) tokens that name the
inner-being operation, faculty, state or movement evidenced by the verse. They are
stored as a JSON array (TEXT) in `verse_context.keywords`. The keyword pool feeds
the cluster-level keyword analytics report that informs Phase 5 sub-group design.

Operations:
  1. ALTER TABLE verse_context ADD COLUMN keywords TEXT.
  2. Insert schema_version 3.25.0 row.

Idempotent: ALTER skipped if the column already exists.
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
    out = REPO / "backups" / f"bible_research_backup_{ts}_M51-keywords.db"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def column_exists(conn, table: str, column: str) -> bool:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return any(r["name"] == column for r in rows)


def fetch_schema_version(conn) -> str:
    r = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY rowid DESC LIMIT 1"
    ).fetchone()
    return r["version_code"]


def apply(conn) -> dict:
    pre_n = conn.execute("SELECT COUNT(*) FROM verse_context").fetchone()[0]
    log(f"  Pre-migration verse_context rowcount: {pre_n}")
    pre_version = fetch_schema_version(conn)
    log(f"  Prev schema version: {pre_version}")

    if column_exists(conn, "verse_context", "keywords"):
        log("  keywords column already exists — skipping ALTER")
    else:
        log("  ALTER TABLE verse_context ADD COLUMN keywords TEXT")
        conn.execute("ALTER TABLE verse_context ADD COLUMN keywords TEXT")

    # Insert schema_version 3.25.0
    log("  Inserting schema_version 3.25.0 ...")
    prior_history_row = conn.execute(
        "SELECT migration_history FROM schema_version WHERE version_code=? LIMIT 1",
        (pre_version,)
    ).fetchone()
    history = json.loads(prior_history_row["migration_history"]) if prior_history_row else []
    history.append({
        "version": "M51",
        "description": (
            "Add verse_context.keywords TEXT (JSON array of inner-being keywords "
            "per verse, produced by Phase 2 Pass A; feeds Phase 5 keyword analytics)"
        ),
        "applied_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    })
    conn.execute(
        "INSERT INTO schema_version (version_code, applied_at, migration_history) VALUES (?, ?, ?)",
        ("3.25.0", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), json.dumps(history)),
    )

    post_n = conn.execute("SELECT COUNT(*) FROM verse_context").fetchone()[0]
    return {"pre_rowcount": pre_n, "post_rowcount": post_n}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Apply (default: dry-run)")
    args = ap.parse_args()
    dry_run = not args.live

    log("Migration M51 — verse_context.keywords")
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
            n = conn.execute("SELECT COUNT(*) FROM verse_context").fetchone()[0]
            ver = fetch_schema_version(conn)
            log(f"  Verified post-commit: verse_context rows={n}, schema version={ver}")
        log(f"\nDONE — pre={result['pre_rowcount']} post={result['post_rowcount']}")
    except Exception:
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
