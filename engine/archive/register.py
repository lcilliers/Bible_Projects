"""
register.py
───────────
REGISTER subcommand — adds a new row to word_registry.

Also provides:
  run_clear_lock(conn, registry_id) — clears a stale IN_PROGRESS sentinel
  check_stale_locks(conn)           — reports any stale lock entries

REGISTER logic:
  1. Determine the next sequence number: MAX(no) FROM word_registry + 1
  2. Insert a new row with phase1_status='Pending', automation_eligible=1
  3. Print the assigned registry no (sequence number) to stdout
"""

from __future__ import annotations

from datetime import datetime, timezone

from .constants import LOCK_SENTINEL, STALE_LOCK_SECONDS


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def run_register(conn, word: str, source_list: str,
                 category_hint: str | None = None) -> dict:
    """Register a new word in word_registry.

    Args:
        conn:          Open database connection.
        word:          English word to register.
        source_list:   Source list label (e.g. 'High Confidence').
        category_hint: Optional category string (e.g. 'Emotion').

    Returns:
        {"no": int, "id": int, "word": str}
    """
    # Check for existing entry with same word
    existing = conn.execute(
        "SELECT no, id FROM word_registry WHERE word = ? LIMIT 1", (word,)
    ).fetchone()
    if existing:
        print(f"  [WARN] word_registry already has '{word}' at no={existing['no']}, "
              f"id={existing['id']}. No new row created.")
        return {"no": existing["no"], "id": existing["id"], "word": word, "new": False}

    # Next sequence number
    row = conn.execute("SELECT MAX(no) AS m FROM word_registry").fetchone()
    next_no = (row["m"] or 0) + 1

    # Next id — word_registry uses explicit id (not AUTOINCREMENT)
    id_row = conn.execute("SELECT MAX(id) AS m FROM word_registry").fetchone()
    next_id = (id_row["m"] or 0) + 1

    conn.execute(
        """INSERT INTO word_registry
               (id, no, word, source_list, category_hint,
                phase1_status, automation_eligible)
           VALUES (?, ?, ?, ?, ?, 'Pending', 1)""",
        (next_id, next_no, word, source_list, category_hint),
    )
    conn.commit()

    print(f"  Registered '{word}' → no={next_no}, id={next_id} "
          f"(source_list='{source_list}')")
    return {"no": next_no, "id": next_id, "word": word, "new": True}


def run_clear_lock(conn, registry_id: int, force: bool = False) -> dict:
    """Clear an IN_PROGRESS lock on word_registry.no = registry_id.

    A 2-hour staleness check is applied unless force=True.

    Returns:
        {"cleared": bool, "reason": str}
    """
    row = conn.execute(
        "SELECT no, word, last_automation_run, automation_run_id "
        "FROM word_registry WHERE no = ?",
        (registry_id,),
    ).fetchone()
    if not row:
        return {"cleared": False, "reason": f"No registry row for no={registry_id}"}

    current = row["last_automation_run"]
    word = row["word"]

    if current != LOCK_SENTINEL:
        return {
            "cleared": False,
            "reason": (
                f"No IN_PROGRESS sentinel for {word} (no={registry_id}). "
                f"last_automation_run = {current!r}"
            ),
        }

    if not force:
        # Check staleness — only clear if run_id implies the lock is old enough
        run_id = row["automation_run_id"] or ""
        # Run IDs have format RUN-YYYYMMDD_HHMMss-MODE
        # Try to parse the timestamp from the last engine_run_log entry
        log_row = conn.execute(
            "SELECT started_at FROM engine_run_log WHERE run_id = ? LIMIT 1",
            (run_id,),
        ).fetchone()
        if log_row and log_row["started_at"]:
            try:
                started = datetime.fromisoformat(log_row["started_at"].replace("Z", "+00:00"))
                now_utc = datetime.now(timezone.utc)
                # Make started timezone-aware if naive
                if started.tzinfo is None:
                    from datetime import timezone as _tz
                    started = started.replace(tzinfo=_tz.utc)
                age_seconds = (now_utc - started).total_seconds()
                if age_seconds < STALE_LOCK_SECONDS:
                    remaining = int(STALE_LOCK_SECONDS - age_seconds)
                    return {
                        "cleared": False,
                        "reason": (
                            f"Lock for {word} (no={registry_id}) is only "
                            f"{int(age_seconds)}s old (threshold={STALE_LOCK_SECONDS}s). "
                            f"Use --force to clear immediately, or wait {remaining}s. "
                            f"Run ID: {run_id}"
                        ),
                    }
            except (ValueError, TypeError):
                pass  # Can't parse timestamp — allow clear

    conn.execute(
        "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
        (registry_id,),
    )
    conn.commit()

    print(f"  Cleared IN_PROGRESS lock for '{word}' (no={registry_id}).")
    return {"cleared": True, "reason": "ok"}


def check_stale_locks(conn) -> list[dict]:
    """Return list of word_registry rows that carry the IN_PROGRESS sentinel."""
    rows = conn.execute(
        "SELECT no, id, word, last_automation_run, automation_run_id "
        "FROM word_registry WHERE last_automation_run = ?",
        (LOCK_SENTINEL,),
    ).fetchall()

    locks = []
    for row in rows:
        run_id = row["automation_run_id"] or ""
        age_str = "unknown age"
        log_row = conn.execute(
            "SELECT started_at FROM engine_run_log WHERE run_id = ? LIMIT 1",
            (run_id,),
        ).fetchone()
        if log_row and log_row["started_at"]:
            try:
                started = datetime.fromisoformat(log_row["started_at"])
                age_secs = int(
                    (datetime.now(timezone.utc) - started.replace(tzinfo=timezone.utc)
                     ).total_seconds()
                )
                age_str = f"{age_secs}s old"
                stale = age_secs >= STALE_LOCK_SECONDS
            except (ValueError, TypeError):
                stale = True
        else:
            stale = True

        locks.append({
            "no": row["no"],
            "id": row["id"],
            "word": row["word"],
            "run_id": run_id,
            "age": age_str,
            "stale": stale,
        })

    return locks
