"""
run_log.py
──────────
engine_run_log and word_run_state write helpers.
"""

import json
import re
from datetime import datetime, timezone


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def make_run_id(mode: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    return f"RUN-{ts}-{mode}"


# ── engine_run_log ────────────────────────────────────────────────────────────

def open_run(conn, run_id: str, mode: str, registry_ids: list[int]) -> None:
    conn.execute(
        """INSERT INTO engine_run_log
           (run_id, mode, target_registry_ids, started_at, outcome)
           VALUES (?, ?, ?, ?, 'RUNNING')""",
        (run_id, mode, ",".join(str(i) for i in registry_ids), _now()),
    )
    conn.commit()


def close_run(conn, run_id: str, outcome: str, counts: dict) -> None:
    conn.execute(
        """UPDATE engine_run_log SET
               completed_at          = ?,
               outcome               = ?,
               words_attempted       = ?,
               words_complete        = ?,
               words_stopped         = ?,
               total_terms_new       = ?,
               total_terms_xref      = ?,
               total_verses_inserted = ?,
               total_verses_filtered = ?,
               total_meanings_parsed = ?,
               error_detail          = ?
           WHERE run_id = ?""",
        (
            _now(), outcome,
            counts.get("words_attempted", 0),
            counts.get("words_complete",  0),
            counts.get("words_stopped",   0),
            counts.get("total_terms_new", 0),
            counts.get("total_terms_xref", 0),
            counts.get("total_verses_inserted", 0),
            counts.get("total_verses_filtered", 0),
            counts.get("total_meanings_parsed", 0),
            json.dumps(counts["errors"]) if counts.get("errors") else None,
            run_id,
        ),
    )
    conn.commit()


# ── word_run_state ────────────────────────────────────────────────────────────

def write_word_run_state(conn, run_id: str, registry_id: int, word: str,
                          phase_reached: str, audit_result: str,
                          audit_detail: dict, stop_reason: str | None = None) -> int:
    cur = conn.execute(
        """INSERT INTO word_run_state
               (run_id, registry_id, word, phase_reached,
                audit_result, audit_detail, stop_reason)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            run_id, str(registry_id).zfill(3), word,
            phase_reached, audit_result,
            json.dumps(audit_detail), stop_reason,
        ),
    )
    conn.commit()
    return cur.lastrowid


# ── engine_stream_checkpoint ──────────────────────────────────────────────────

def upsert_checkpoint(conn, run_id: str, stream_name: str, status: str,
                       last_registry_id: str | None = None,
                       last_strong: str | None = None,
                       rows_written: int = 0, rows_filtered: int = 0,
                       error_detail: str | None = None) -> None:
    existing = conn.execute(
        "SELECT id FROM engine_stream_checkpoint WHERE run_id = ? AND stream_name = ?",
        (run_id, stream_name),
    ).fetchone()
    if existing:
        conn.execute(
            """UPDATE engine_stream_checkpoint SET
                   status = ?, last_registry_id = ?, last_strong = ?,
                   rows_written = ?, rows_filtered = ?, error_detail = ?,
                   completed_at = CASE WHEN ? IN ('complete','failed') THEN ? ELSE completed_at END
               WHERE run_id = ? AND stream_name = ?""",
            (status, last_registry_id, last_strong,
             rows_written, rows_filtered, error_detail,
             status, _now(),
             run_id, stream_name),
        )
    else:
        conn.execute(
            """INSERT INTO engine_stream_checkpoint
                   (run_id, stream_name, status, last_registry_id, last_strong,
                    rows_written, rows_filtered, error_detail, started_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (run_id, stream_name, status, last_registry_id, last_strong,
             rows_written, rows_filtered, error_detail, _now()),
        )
    conn.commit()


# ── term_fetch_log ────────────────────────────────────────────────────────────

def log_fetch(conn, run_id: str, registry_id: int, strongs_input: str,
              strongs_resolved: str, suffix_resolution: int,
              vocab_status: str, verse_status: str,
              verse_count_fetched: int, verse_count_stored: int,
              verse_count_filtered: int, span_conflict: int,
              api_warnings: list | None) -> None:
    conn.execute(
        """INSERT INTO term_fetch_log
               (run_id, registry_id, strongs_input, strongs_resolved,
                suffix_resolution, vocab_status, verse_status,
                verse_count_fetched, verse_count_stored,
                verse_count_filtered, span_conflict, api_warnings, fetched_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            run_id, str(registry_id), strongs_input, strongs_resolved,
            suffix_resolution, vocab_status, verse_status,
            verse_count_fetched, verse_count_stored,
            verse_count_filtered, span_conflict,
            json.dumps(api_warnings) if api_warnings else None,
            _now(),
        ),
    )
    conn.commit()
