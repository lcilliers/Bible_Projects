"""spancorrection.py -- the correction table for stored span errors (escalation #2551, design adopted 2026-11-24 from #2541 A).

`span` stays immutable. A row of `span_correction` names one field of one span code (span_id, code_ordinal, field), the value the stored data gives (stored_value) and the value it
should give (corrected_value), with its reason and the escalation it comes from. lexical.write_readings_for_span asks `apply` for each row it is about to write:
  - a live correction whose stored_value still equals the value the build produced is applied, and the application is kept on the correction (applied_at, applied_count);
  - a live correction whose stored_value no longer equals it is NOT applied: the source changed under it, so the build stops and names the correction (SpanCorrectionStale), never silently overriding.
A database without the table (before migration span_correction_2551) has no corrections. Lookups are by the unique index on (span_id, code_ordinal, field).
"""
from __future__ import annotations

import sqlite3

FIELDS = ("morph_code", "surface", "is_negator", "narrative_morph", "party_kind", "unit_surface", "surface_kind", "unit_size", "unit_role", "role", "strong", "position")


class SpanCorrectionStale(Exception):
    """A live correction whose stored value is no longer the value the build produces."""


def _has_table(conn) -> bool:
    return conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='span_correction'").fetchone() is not None


def for_span(conn: sqlite3.Connection, span_id: int) -> dict:
    """{code_ordinal: [(id, field, stored_value, corrected_value)]} of the live corrections of one span."""
    if not _has_table(conn):
        return {}
    out: dict = {}
    for r in conn.execute("SELECT id, code_ordinal, field, stored_value, corrected_value FROM span_correction WHERE span_id=? AND deleted=0", (span_id,)):
        out.setdefault(r[1], []).append((r[0], r[2], r[3], r[4]))
    return out


def _text(v) -> str | None:
    return None if v is None else str(v)


def apply(conn: sqlite3.Connection, span_id: int, ordinal: int, content: dict, held: dict, now: str) -> int:
    """Apply the live corrections of (span_id, ordinal) to `content` (the row the build is about to write); returns how many were applied. `held` is for_span(conn, span_id)."""
    n = 0
    for cid, field, stored, corrected in held.get(ordinal, ()):
        if field not in content:
            raise SpanCorrectionStale(f"correction {cid} (span {span_id} code {ordinal}) names the field {field!r}, which the build does not write")
        if _text(content[field]) != stored:
            raise SpanCorrectionStale(f"correction {cid} (span {span_id} code {ordinal} {field}): the build now gives {content[field]!r}, not the stored {stored!r}; review the correction")
        content[field] = corrected
        conn.execute("UPDATE span_correction SET applied_at=?, applied_count=applied_count+1 WHERE id=?", (now, cid))
        n += 1
    return n
