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
    _prune_pre_run_backups()
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


def _prune_pre_run_backups() -> None:
    """Keep only the N most recent pre-run backups; delete the rest."""
    pattern = re.compile(r"bible_research_backup_\d{8}_\d{6}_.*\.db$")
    backups = sorted(
        [p for p in _BACKUPS_DIR.iterdir() if pattern.match(p.name)],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    for old in backups[BACKUP_RETENTION:]:
        try:
            old.unlink()
        except Exception:
            pass
