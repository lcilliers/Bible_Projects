"""
backup.py
─────────
Database backup management (SG-01, SG-12, SG-13).

Pre-run:   create timestamped backup before any writes; abort if backup fails.
Post-run:  backup final state after COMPLETE or PARTIAL outcome.
Pre-migration: permanent backup before --migrate.
Rolling retention: keep 10 most recent pre-run backups; auto-delete older ones.
"""

import os
import re
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from .constants import BACKUP_RETENTION

_ROOT = Path(__file__).parent.parent
_BACKUPS_DIR = _ROOT / "backups"


def _db_path() -> Path:
    import sys
    sys.path.insert(0, str(_ROOT))
    from dotenv import load_dotenv
    load_dotenv(_ROOT / ".env")
    default = str(_ROOT / "data" / "bible_research.db")
    return Path(os.getenv("DB_PATH", default))


def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def _ensure_dir() -> Path:
    _BACKUPS_DIR.mkdir(exist_ok=True)
    return _BACKUPS_DIR


def pre_run_backup(run_id: str) -> Path:
    """Create a pre-run backup. Raises RuntimeError if the backup fails (SG-01)."""
    src = _db_path()
    if not src.exists():
        raise RuntimeError(f"Database not found at {src}")
    dest = _ensure_dir() / f"bible_research_backup_{_ts()}_{run_id}.db"
    try:
        shutil.copy2(src, dest)
    except Exception as exc:
        raise RuntimeError(f"Pre-run backup failed: {exc}") from exc
    prune_backups()
    return dest


def post_run_backup(run_id: str) -> Path:
    """Create a post-run backup after COMPLETE or PARTIAL outcome."""
    src = _db_path()
    dest = _ensure_dir() / f"bible_research_{_ts()}_{run_id}_post.db"
    shutil.copy2(src, dest)
    return dest


def pre_migration_backup(version: str) -> Path:
    """Create a permanent pre-migration backup."""
    src = _db_path()
    dest = _ensure_dir() / f"bible_research_pre_migration_v{version}.db"
    shutil.copy2(src, dest)
    return dest


def manual_backup(label: str | None = None) -> Path:
    """Create a manual checkpoint backup."""
    src = _db_path()
    suffix = f"_{label}" if label else ""
    dest = _ensure_dir() / f"bible_research_manual_{_ts()}{suffix}.db"
    shutil.copy2(src, dest)
    return dest


def integrity_check(db_path: Path | None = None) -> bool:
    """Run PRAGMA integrity_check. Returns True if clean. (SG-13)"""
    path = db_path or _db_path()
    conn = sqlite3.connect(str(path))
    try:
        result = conn.execute("PRAGMA integrity_check").fetchone()
        return result and result[0] == "ok"
    finally:
        conn.close()


def prune_backups() -> dict[str, int]:
    """Keep only the N most recent backups per category; delete the rest.

    Categories pruned independently (each retains BACKUP_RETENTION newest):
      - pre-run engine backups:        bible_research_backup_<ts>_<label>.db
      - post-run engine backups:       bible_research_<ts>_<label>_post.db
      - manual/checkpoint backups:     bible_research_(manual|checkpoint)_*.db
      - timestamped pre-action backups: bible_research_<ts>_pre_<label>.db
      - dated ad-hoc pre-action:       bible_research_pre_<label>_<date>.db
                                       (excludes pre-migration which is permanent)
      - smoke-test artefacts:          _smoke_*.db (kept while present, never pruned
                                       — they're tiny and named explicitly for tests)

    Pre-migration backups (bible_research_pre_migration_*.db) are never pruned.

    Returns a per-category dict of {pattern_label: deleted_count}.
    """
    categories: list[tuple[str, re.Pattern[str]]] = [
        ("pre_run",
         re.compile(r"^bible_research_backup_\d{8}_\d{6}_.*\.db$")),
        ("post_run",
         re.compile(r"^bible_research_\d{8}_\d{6}_.*_post\.db$")),
        ("manual_checkpoint",
         re.compile(r"^bible_research_(manual|checkpoint)_.*\.db$")),
        # NEW: timestamp-prefix pre-action (e.g. _apply_* scripts)
        ("pre_action_ts",
         re.compile(r"^bible_research_\d{8}_\d{6}_pre_.*\.db$")),
        # NEW: dated ad-hoc pre-action (excludes pre_migration_)
        ("pre_action_dated",
         re.compile(r"^bible_research_pre_(?!migration_).*\.db$")),
    ]
    deleted: dict[str, int] = {}
    if not _BACKUPS_DIR.exists():
        return deleted
    all_files = [p for p in _BACKUPS_DIR.iterdir() if p.is_file()]
    for label, pattern in categories:
        backups = sorted(
            [p for p in all_files if pattern.match(p.name)],
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        n = 0
        for old in backups[BACKUP_RETENTION:]:
            try:
                old.unlink()
                n += 1
            except Exception:
                pass
        deleted[label] = n
    return deleted


# Backwards-compatibility alias for prior callers.
_prune_pre_run_backups = prune_backups
