"""Schema migration M53 — add cluster.char_structure column.

Bumps schema 3.26.0 → 3.27.0.

Rationale: per researcher direction 2026-05-26, M10 has been confirmed as
a non-standard cluster: 22 'characteristics' are aspects of one true
characteristic (sin). Tools doing cross-cluster char-comparison analytics
need a way to identify this pattern and exclude such clusters from
analyses that assume distinct-faculty chars. Other purposes (overview,
programme state, term counts) include such clusters normally.

Operations:
  1. ALTER TABLE cluster ADD COLUMN char_structure TEXT
  2. INSERT schema_version 3.27.0

Values:
  NULL (default)       — standard cluster (chars are distinct inner-being faculties)
  'aspect_based'       — single-theme cluster with chars as analytical aspects (M10 pattern)

Future values may be added as other non-standard structures come into focus.

Idempotent: skips ALTER if column already exists.
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


def column_exists(conn, table: str, column: str) -> bool:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return any(r[1] == column for r in rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry = not args.live

    print(f"=== Migration M53 — cluster.char_structure (3.26.0 → 3.27.0) — "
          f"mode={'LIVE' if not dry else 'DRY-RUN'} ===")

    if not dry:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        out = REPO / "backups" / f"bible_research_backup_{ts}_M53-cluster-char-structure.db"
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DB, out)
        print(f"Backup: {out.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    pre_version = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY rowid DESC LIMIT 1"
    ).fetchone()["version_code"]
    print(f"Prev schema version: {pre_version}")

    has_col = column_exists(conn, "cluster", "char_structure")
    print(f"cluster.char_structure exists pre-migration: {has_col}")

    if dry:
        print("\n[DRY-RUN — no writes]")
        conn.close()
        return 0

    conn.execute("BEGIN")
    try:
        if not has_col:
            conn.execute("ALTER TABLE cluster ADD COLUMN char_structure TEXT")
            print("Op 1: added cluster.char_structure column")
        else:
            print("Op 1: skipped (column already exists)")

        # Build new migration_history JSON
        prior_history_row = conn.execute(
            "SELECT migration_history FROM schema_version WHERE version_code=? LIMIT 1",
            (pre_version,)
        ).fetchone()
        history = json.loads(prior_history_row["migration_history"]) if prior_history_row else []
        history.append({
            "version": "M53",
            "description": (
                "Add cluster.char_structure column (NULL=standard chars; "
                "'aspect_based'=chars are aspects of one master characteristic — "
                "M10 pattern). Filter for cross-cluster char-comparison analytics."
            ),
            "applied_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        })
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        conn.execute(
            "INSERT INTO schema_version (version_code, applied_at, migration_history) "
            "VALUES (?, ?, ?)",
            ("3.27.0", now, json.dumps(history)),
        )
        print("Op 2: inserted schema_version 3.27.0")

        conn.commit()

        # Verify
        post_cols = [r[1] for r in conn.execute("PRAGMA table_info(cluster)").fetchall()]
        assert "char_structure" in post_cols, "char_structure column missing post-commit"
        post_version = conn.execute(
            "SELECT version_code FROM schema_version ORDER BY rowid DESC LIMIT 1"
        ).fetchone()["version_code"]
        assert post_version == "3.27.0", f"unexpected version: {post_version}"
        print(f"\nVerified post-commit: schema version = {post_version}, "
              f"cluster.char_structure present")
        print(f"COMMITTED at {now}")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
