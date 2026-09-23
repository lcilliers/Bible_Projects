"""enforce_span_grounding_word_level_v1_20260923.py — ONE-OFF migration, researcher instruction
verbatim (this chat, 2026-09-23): "Every word observation answer must be at span (word in verse
context) level. Saying that you can resolve the observation question without looking at the
verse/span/morph means it is a generic answer." ... "this is now your opportunity to rectify it. On
all levels. governance, configs, column descriptions, questions, and all the methods in the code
that is related." ... "it will deliver what the intention have been since the first time in about
May that I spotted you are using the wrong values for word analysis."

Root defect being corrected: the 2026-09-23 rewording of M0.1.x/M0.5.x (earlier this same session,
escalation #1849 follow-on) dropped cluster/characteristic framing correctly, but replaced it with
"this term" framing answerable purely from strong/strong_meaning_tree/strong_lexicon/strong_related
-- NONE of it required looking at the actual verse/span/morph. That is the generic-answer pattern
the researcher is naming, and it is the same defect that made `_strongs_needing_battery`'s "answered
once ever per strong, never re-derived" front-loading mechanism (escalation #1723, 2026-09-17) seem
reasonable in the first place -- if the answer never depended on the occurrence, skipping
re-derivation looked harmless. It wasn't: every OTHER live question in this catalogue (M0.7.1-16,
M0.6.5, M0.6.6, D7.7.1, M0.5.11, M0.8.1) already opens "In this verse..." -- these 11 were the only
ones that didn't, and this migration brings them into the same convention, worded so the answer is
only resolvable by consulting this occurrence's own surface/morph_code within its verse, not the
lemma alone.

Companion changes, same unit of work (not this file): `iba/app/lib/recordingpass.py` (dedup no
longer assumes "2+ existing rows = same fact" for these -- exact-text match only, on independently
per-occurrence-grounded answers) and `iba/app/lib/versereadinggenerate.py` (word-level questions no
longer skip strongs with an existing answer elsewhere -- every occurrence is given a chance to be
asked, verse/span/morph included in the payload). Governance: cfg_method_rule proposed
(escalation #1853, span-grounded-not-generic), awaiting researcher approval to apply.

Idempotent (checks live text before writing) -- a second run is a no-op.

    python -m iba.app.migration.enforce_span_grounding_word_level_v1_20260923
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v12-span-grounded-20260923"
_MODIFIED_DATE = "2026-09-23"
_REVIEW_NOTE_SUFFIX = (
    " | Reworded again 2026-09-23 (same day, researcher correction): the prior 'this term' "
    "rewording was still generic -- answerable from strong-level lexicon data alone, without ever "
    "consulting the verse/span/morph. Every other live question in this catalogue opens 'In this "
    "verse...'; these are now brought into the same convention, worded so the answer requires this "
    "occurrence's own surface/morph_code, not the lemma in the abstract.")

_REVISED_TEXT = {
    "M0.1.1": "In this verse, looking at this specific occurrence (its surface form and "
        "morph_code), what does this term's name/form show about its essential nature here?",
    "M0.1.2": "In this verse, drawing on this term's lexicon entries but grounded in how it is "
        "actually used in this occurrence, what does it mean at the definitional level?",
    "M0.1.3": "In this verse, what directional, relational, or constitutional implication does "
        "this term's name carry as it functions in this specific occurrence?",
    "M0.5.1": "In this verse, what does this term's root meaning show about how it operates in "
        "this specific occurrence?",
    "M0.5.2": "In this verse, what is this occurrence's own grammatical form (per its actual "
        "morph_code here — noun, verb, adjective, participle), and what does that form show about "
        "how the term operates in this occurrence?",
    "M0.5.4": "In this verse, does this occurrence express a specific aspect — disposition versus "
        "act, received versus given, condition versus quality? Record which, or none.",
    "M0.5.5": "In this verse, among this term's own related terms, is there one that functions as "
        "this occurrence's structural opposite? Record it, or none.",
    "M0.5.6": "In this verse, among this term's own related terms, is there a person-type term "
        "relevant to this occurrence — one for a person who habitually possesses or exercises it? "
        "Record it, or none.",
    "M0.5.7": "In this verse, among this term's own related terms, is there a supplication or "
        "seeking term relevant to this occurrence — one for the act of seeking it from another? "
        "Record it, or none.",
    "M0.5.8": "In this verse, does this term's Testament context (OT Hebrew vs. NT Greek) affect "
        "how this specific occurrence should be interpreted, and if so, how? Record none if the "
        "Testament context makes no interpretive difference here.",
    "M0.5.9": "In this verse, if this term is newly coined in the NT period, what does that "
        "coinage show about how it functions in this occurrence? Record none if not applicable or "
        "not relevant to this occurrence.",
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
        report.append(f"{code}: question_text updated (generic 'this term' -> span-grounded)")
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
