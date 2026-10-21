"""fix_characteristic_terminology_stage1_v1_20260923.py — ONE-OFF migration, researcher instruction
verbatim (this chat, 2026-09-23): "fix the questions to use the right terminology."

Finding: escalation #1810 v3 (2026-09-20, researcher verbatim) settled that verse-reading (Stage 1)
is NOT cluster/characteristic-aware -- "no verse is aware of the cluster allocation per se, it is
about what does the verse say - not what does the verse say about the cluster." #1824 v14
(2026-09-22) restated the same principle for the M0.6.5/M0.6.6/D7.7.1 population specifically:
"every M-code word has the same status in the verse and need to be treated the same." Despite both
corrections, the live catalogue text for these three questions still asks about "this characteristic"
/ "M-code characteristics" / an Operation word being classified "for this cluster" -- cluster/
characteristic framing that contradicts the settled per-word, cluster-agnostic design those same
questions are coded to (recordingpass.py's _verse_cluster_agnostic_coverage, versereadinggenerate.py).

Scope: ONLY the three questions where this is a mechanical wording swap that changes no substance
(the word being asked about IS the M-code word in the verse; "characteristic" was simply the wrong
noun for it) -- D7.7.1, M0.6.5, M0.6.6. NOT touched, and not in scope: M0.1.1-3/M0.5.1-10 (ask about
cluster-wide vocabulary/naming facts that cannot be mechanically reworded to "word" without changing
what's being asked -- a scope decision, not a wording bug) and M0.8.1 (legitimately about a role-word
being elevated to its own M-code characteristic -- "characteristic" is the correct term there, that
question is about the classification scheme itself, not verse context). Both flagged separately for
the researcher's own decision, not resolved by this migration.

Idempotent (checks live text before writing) -- a second run is a no-op.

    python -m iba.app.migration.fix_characteristic_terminology_stage1_v1_20260923
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v8-characteristic-terminology-fix-20260923"
_MODIFIED_DATE = "2026-09-23"
_REVIEW_NOTE_SUFFIX = (
    " | Fixed 2026-09-23, researcher instruction ('fix the questions to use the right "
    "terminology'): 'characteristic'/'this cluster' replaced with 'M-code word'/'role-T3' -- "
    "verse-reading is cluster/characteristic-agnostic per escalation #1810 v3 and #1824 v14, but "
    "this question's own wording still asked about the cluster/characteristic. No change to the "
    "underlying evaluation subject (still the M-code word occurring in this verse), only to the "
    "noun used to describe it.")

_REVISED_TEXT = {
    "D7.7.1": "In this verse, where an action or movement word carries the Operation role tag "
        "(role-T3), what is that word's relation to the parties present in the verse -- who "
        "initiates it, and toward whom or what is it directed? Record none if no such operation "
        "word is present.",
    "M0.6.5": "What role does this M-code word play in relation to the OTHER M-code words present "
        "in this verse -- does it cause, enable, intensify, block, respond to, or stand in tension "
        "with each one, and do they share the same party or act on different parties? Record none "
        "if no other M-code word is present.",
    "M0.6.6": "Taking every M-code word present in this verse together, what is the overall "
        "relational network this verse depicts -- which words connect to which others, and how "
        "does this word's own role fit within that whole picture? Record none if this word is the "
        "verse's only M-code element.",
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
        report.append(f"{code}: question_text updated (characteristic/cluster wording removed)")
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
