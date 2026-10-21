"""reframe_what_is_to_what_does_show_v1_20260923.py — ONE-OFF migration, researcher instruction
verbatim (this chat, 2026-09-23): "Instead of asking what is the morph, the question must be what
does the morph tell me, same apply to other questions also."

Principle: a question phrased "what IS <value already sitting in a DB column>" is a wasted call --
the answer is mechanically retrievable (morph_code is a live `verse_lexical` column; no LLM needed
to report it back). The value only comes from interpreting what that stored fact SHOWS about how
the word functions in this specific occurrence. Re-audited all 34 live Stage 1 questions against
this test (not just the ones touched earlier today) -- most already ask "what does X show/tell/
imply" or ask about something that ISN'T a stored field (a relation, a role, a network -- these
inherently need reading the verse, "what is" framing there is not the antipattern). Two concrete
violations found:

M0.5.2 -- literally asked "what IS this occurrence's own grammatical form (per its actual
morph_code)" as part of the question, mirroring the researcher's own morph example exactly. Fixed:
morph_code's possible values stay as parenthetical grounding (so the model knows what kinds of
answer are in scope), the actual ask is only what that form SHOWS.

M0.5.3 -- missed entirely in both of today's earlier reworks (a real gap, not a deliberate
exclusion): still had no "in this verse" anchor at all, and asked "What IS the semantic range of
this term" -- a term-wide aggregate answerable from the lexicon alone, the exact generic-answer
pattern today's span-grounding correction was for. Fixed: reframed to ask where THIS occurrence
sits within the term's known range, and what that placement shows -- genuinely requires reading the
verse to answer, not a lexicon recitation.

Idempotent (checks live text before writing) -- a second run is a no-op.

    python -m iba.app.migration.reframe_what_is_to_what_does_show_v1_20260923
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v14-what-does-it-show-20260923"
_MODIFIED_DATE = "2026-09-23"
_REVIEW_NOTE_SUFFIX = (
    " | Reframed 2026-09-23, researcher instruction verbatim: 'instead of asking what is the "
    "morph, the question must be what does the morph tell me, same apply to other questions "
    "also.' A bare 'what is <stored field>' ask is mechanically answerable without interpretation "
    "-- reworded to ask only what the fact shows about this occurrence.")

_REVISED_TEXT = {
    "M0.5.2": "In this verse, what does this occurrence's own grammatical form (per its "
        "morph_code — e.g. noun, verb, adjective, participle) show about how the term operates "
        "here?",
    "M0.5.3": "In this verse, given this term's known semantic range — the breadth of meaning it "
        "can carry, including idiomatic, analogical, or combinatorial senses — where does this "
        "occurrence sit within that range, and what does that show about how the term operates "
        "here?",
}


def apply_fix(conn: sqlite3.Connection) -> list[str]:
    report = []
    for code, revised_text in sorted(_REVISED_TEXT.items()):
        row = conn.execute(
            "SELECT question_text, review_note FROM wa_obs_question_catalogue "
            "WHERE question_code=? AND deleted=0", (code,)).fetchone()
        if row is None:
            report.append(f"{code}: SKIPPED -- no live row found")
            continue
        current_text, current_note = row
        if current_text == revised_text:
            report.append(f"{code}: already fixed -- no-op")
            continue
        new_note = (current_note or "") + _REVIEW_NOTE_SUFFIX
        conn.execute(
            "UPDATE wa_obs_question_catalogue SET question_text=?, catalogue_version=?, "
            "last_modified=?, review_note=? WHERE question_code=? AND deleted=0",
            (revised_text, _CATALOGUE_VERSION, _MODIFIED_DATE, new_note, code))
        report.append(f"{code}: question_text updated ('what is' -> 'what does it show')")
    return report


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
