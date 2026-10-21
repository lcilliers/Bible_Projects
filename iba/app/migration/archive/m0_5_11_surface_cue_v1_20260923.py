"""m0_5_11_surface_cue_v1_20260923.py — ONE-OFF migration, researcher instruction verbatim (this
chat, 2026-09-23): "actively engage with the surface - this is a good pointer that if the surface
is different for the same term, then the translators must have figured out the verse context is
different and that is what llm must tease out."

M0.5.11 already asks where an occurrence's sense diverges from the term's usual one -- this adds
the concrete, checkable cue for WHERE to look: the occurrence's own surface form/rendering. A
translator's word choice already encodes a judgement about context; a marked surface form is
evidence of that judgement, not incidental bookkeeping. Companion change, same unit of work (not
this file): the general word-level instruction paragraph in versereadinggenerate.py now states the
same principle for the whole M0.1/M0.5 battery.

Idempotent (checks live text before writing) -- a second run is a no-op.

    python -m iba.app.migration.m0_5_11_surface_cue_v1_20260923
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v13-surface-cue-20260923"
_MODIFIED_DATE = "2026-09-23"
_REVISED_TEXT = (
    "In this verse, where this occurrence's meaning diverges from the term's usual sense "
    "elsewhere, what nuance does that divergence carry here, and how does it compare to the "
    "word's other occurrences? Pay particular attention to this occurrence's own surface form/"
    "rendering — a marked or atypical surface form is often the visible trace of the divergence "
    "itself, not a separate fact. Record none if this occurrence matches the term's usual sense."
)
_REVIEW_NOTE_SUFFIX = (
    " | Enriched 2026-09-23, researcher instruction verbatim: 'actively engage with the surface - "
    "this is a good pointer that if the surface is different for the same term, then the "
    "translators must have figured out the verse context is different and that is what llm must "
    "tease out.' Names the surface form explicitly as the diagnostic cue for this question's own "
    "divergence check.")


def apply_fix(conn: sqlite3.Connection) -> list[str]:
    row = conn.execute(
        "SELECT question_text, review_note FROM wa_obs_question_catalogue "
        "WHERE question_code='M0.5.11' AND deleted=0").fetchone()
    if row is None:
        return ["M0.5.11: SKIPPED -- no live row found"]
    current_text, current_note = row
    if current_text == _REVISED_TEXT:
        return ["M0.5.11: already fixed -- no-op"]
    new_note = (current_note or "") + _REVIEW_NOTE_SUFFIX
    conn.execute(
        "UPDATE wa_obs_question_catalogue SET question_text=?, catalogue_version=?, "
        "last_modified=?, review_note=? WHERE question_code='M0.5.11' AND deleted=0",
        (_REVISED_TEXT, _CATALOGUE_VERSION, _MODIFIED_DATE, new_note))
    return ["M0.5.11: question_text updated (surface-form cue added)"]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = apply_fix(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
