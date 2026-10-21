"""
flag_engine.py
──────────────
Derivable flag evaluation (S5 / N16 / A7).

Evaluates flags determinable from data alone — no researcher judgment needed.
Writes rows to wa_term_phase2_flags and wa_data_quality_flags.

Derivable flags assessed (WR-16):
  DATA_COVERAGE group (wa_data_quality_flags):
    HIGH_FREQUENCY_ANCHOR — occurrence_count >= threshold
    THIN_DATA             — occurrence_count < THIN_DATA_THRESHOLD
    SMALL_VERSE_SAMPLE    — confirmed verse count < SMALL_VERSE_SAMPLE_THRESHOLD
    NO_WORD_ANALYSIS      — meaning IS NULL
    NO_VERSES             — zero confirmed verses AND no SPAN_RESOLUTION_CONFLICT
    SPAN_RESOLUTION_CONFLICT — already queued from fetch step (written here)

All other phase2_flag_types are judgment flags deferred to the researcher.
"""

import json
from .constants import (
    HIGH_FREQ_THRESHOLD,
    THIN_DATA_THRESHOLD,
    SMALL_VERSE_SAMPLE_THRESHOLD,
)
from .db import get_max_id


# ── Flag type ID cache (populated lazily) ─────────────────────────────────────

_FLAG_ID_CACHE: dict[str, int] = {}


def _ensure_flag_type(conn, flag_group: str, flag_code: str, description: str) -> None:
    """Insert a flag type row if it does not already exist."""
    conn.execute(
        """INSERT OR IGNORE INTO wa_quality_flag_types
               (flag_group, flag_code, description)
           VALUES (?, ?, ?)""",
        (flag_group, flag_code, description),
    )


def _flag_id(conn, flag_code: str) -> int | None:
    if flag_code not in _FLAG_ID_CACHE:
        row = conn.execute(
            "SELECT id FROM wa_quality_flag_types WHERE flag_code = ?", (flag_code,)
        ).fetchone()
        if row:
            _FLAG_ID_CACHE[flag_code] = row["id"]
    return _FLAG_ID_CACHE.get(flag_code)


def _write_quality_flag(conn, file_id: int, term_id: str,
                         flag_code: str, description: str) -> None:
    fid = _flag_id(conn, flag_code)
    if fid is None:
        return  # Flag type not in DB — skip silently
    conn.execute(
        """INSERT INTO wa_data_quality_flags
               (file_id, term_id, flag_id, description)
           VALUES (?, ?, ?, ?)""",
        (file_id, term_id, fid, description),
    )


def run_flag_engine(conn, file_id: int, registry_id: int,
                     queued_span_conflicts: set[str] | None = None) -> dict:
    """Evaluate and write all derivable flags for a word's terms.

    Args:
        conn:                  Open DB connection.
        file_id:               wa_file_index.id for this word.
        registry_id:           word_registry.no for logging.
        queued_span_conflicts: Set of term_ids (strongs_number) where span
                               conflict was detected during fetch (already
                               needs SPAN_RESOLUTION_CONFLICT flag written).

    Returns:
        {"flags_written": int, "errors": list[str]}
    """
    queued_span_conflicts = queued_span_conflicts or set()
    errors = []
    flags_written = 0

    # ── Bootstrap: ensure engine-owned flag types exist ───────────────────────
    _ensure_flag_type(
        conn, "DATA_COVERAGE", "PROSE_ONLY_MEANING",
        "Meaning stored as single prose block — STEP medium_def contains no "
        "structured sense numbering for this term. No further subdivision available.",
    )

    # ── Idempotency: remove any previously written derivable flags for this
    # file before re-evaluating, so re-runs (gap_fill/audit_word) do not
    # accumulate duplicate rows.  Researcher-entered flags (NOTE, ANOMALY_NOTE,
    # CROSS_REGISTRY, etc.) are not in this set and are left untouched.
    _DERIVABLE_FLAGS = {
        "HIGH_FREQUENCY_ANCHOR", "THIN_DATA", "SMALL_VERSE_SAMPLE",
        "NO_WORD_ANALYSIS", "NO_VERSES", "SPAN_RESOLUTION_CONFLICT",
        "PROSE_ONLY_MEANING",
    }
    _ph = ",".join("?" * len(_DERIVABLE_FLAGS))
    conn.execute(
        f"""DELETE FROM wa_data_quality_flags
            WHERE file_id = ?
            AND flag_id IN (
                SELECT id FROM wa_quality_flag_types
                WHERE flag_code IN ({_ph})
            )""",
        (file_id, *_DERIVABLE_FLAGS),
    )

    terms = conn.execute(
        "SELECT * FROM wa_term_inventory WHERE file_id = ?", (file_id,)
    ).fetchall()

    for term in terms:
        term_inv_id = term["id"]
        strongs = term["strongs_number"] or term["term_id"]
        occurrence_count = term["occurrence_count"] or 0
        meaning = term["meaning"]

        # Confirmed verse count for this term
        confirmed_verses = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_verse_records "
            "WHERE term_inv_id = ? AND (span_strong_match = 1 OR span_strong_match IS NULL)",
            (term_inv_id,),
        ).fetchone()["c"]

        # ── DATA_COVERAGE flags ──────────────────────────────────────────────

        if occurrence_count >= HIGH_FREQ_THRESHOLD:
            _write_quality_flag(
                conn, file_id, strongs, "HIGH_FREQUENCY_ANCHOR",
                f"High-frequency term: {occurrence_count} occurrences. "
                "Verse sample represents a subset of all occurrences.",
            )
            flags_written += 1

        if 0 < occurrence_count < THIN_DATA_THRESHOLD:
            _write_quality_flag(
                conn, file_id, strongs, "THIN_DATA",
                f"Low occurrence count: {occurrence_count}. "
                "Statistical patterns unreliable with fewer than "
                f"{THIN_DATA_THRESHOLD} occurrences.",
            )
            flags_written += 1

        if strongs in queued_span_conflicts:
            _write_quality_flag(
                conn, file_id, strongs, "SPAN_RESOLUTION_CONFLICT",
                f"Queried Strong's {strongs} not found in any verse span after "
                "suffix resolution. Verse set is empty. "
                "Manual STEP UI verification required.",
            )
            flags_written += 1
        elif confirmed_verses < SMALL_VERSE_SAMPLE_THRESHOLD:
            if confirmed_verses == 0:
                _write_quality_flag(
                    conn, file_id, strongs, "NO_VERSES",
                    f"Zero confirmed verse records for {strongs}.",
                )
            else:
                _write_quality_flag(
                    conn, file_id, strongs, "SMALL_VERSE_SAMPLE",
                    f"Only {confirmed_verses} confirmed verse records for {strongs}. "
                    f"Threshold is {SMALL_VERSE_SAMPLE_THRESHOLD}.",
                )
            flags_written += 1

        if not meaning:
            _write_quality_flag(
                conn, file_id, strongs, "NO_WORD_ANALYSIS",
                f"meaning field is null for {strongs}. "
                "STEP returned no word analysis block for this term.",
            )
            flags_written += 1

        # ── PROSE_ONLY_MEANING — meaning_parser found no structured senses ──
        mp_row = conn.execute(
            "SELECT parse_warnings FROM wa_meaning_parsed WHERE term_inv_id = ?",
            (term_inv_id,),
        ).fetchone()
        if mp_row and mp_row["parse_warnings"]:
            try:
                warnings = json.loads(mp_row["parse_warnings"])
            except (ValueError, TypeError):
                warnings = []
            if "PROSE_ONLY" in warnings:
                _write_quality_flag(
                    conn, file_id, strongs, "PROSE_ONLY_MEANING",
                    f"Meaning for {strongs} stored as single prose block. "
                    "STEP medium_def contains no structured sense numbering. "
                    "No further subdivision available.",
                )
                flags_written += 1

    conn.commit()
    return {"flags_written": flags_written, "errors": errors}
