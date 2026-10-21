"""enrich_verse_relational_reading_v1_20260921.py — ONE-OFF migration, escalation #1819 v2,
researcher instruction verbatim: "The objective of the lexical llm read is to have a rich /
comprehensive understanding of the context of the verse in relation to all the M-code strongs in
the verse. That is the objective you need to achieve. Go through all the questions relating to it,
enrich those questions, and add questions that will acheive this objective."

Finding 12 (#1819) established: of Stage 1's ~16 questions, only `M0.6.5`/`D7.7.1` are relational
at all, both narrow. This closes that gap two ways:

1. **`M0.6.5` enriched** -- was an open "what role" narrative with no structured vocabulary; now
   names the actual relation TYPES to check for (cause/enable/intensify/block/respond-to/tension)
   and whether the characteristics share a party or act on different parties -- systematic, not
   left to whatever the LLM happens to volunteer.

2. **`M0.6.6` added (new)** -- `M0.6.5` is deliberately single-vantage per its own progressive
   design (#1723: each cluster's own pass adds ITS vantage on the OTHER characteristics, building a
   chain across passes, never asked as a whole-network question). That design is sound and stays
   unchanged. But nothing asks for the WHOLE network in one place -- `M0.6.6` closes that: taking
   EVERY M-code characteristic present in the verse together, what is the overall relational network
   the verse depicts, and where does this characteristic sit within it. Same per-cluster-pass,
   progressive-build design as `M0.6.5` (own dedicated prior-context feed, not merged with M0.6.5's
   own chain -- a different kind of question, kept as its own stream rather than conflating two
   distinct senses of "building on prior context").

Companion code change (same escalation, not in this file): `iba/app/lib/versereadinggenerate.py`
wires `M0.6.6` into Stage 1's selection query, prompt instructions, and its own
`prior_network_context_by_verse` progressive feed.

Idempotent (checks live state before writing) -- a second run is a no-op.

    python -m iba.app.migration.enrich_verse_relational_reading_v1_20260921
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v6-relational-enrichment-20260921"
_MODIFIED_DATE = "2026-09-21"

_M065_ENRICHED_TEXT = (
    "What role does this characteristic play in relation to the OTHER M-code characteristics "
    "present in this verse -- does it cause, enable, intensify, block, respond to, or stand in "
    "tension with each one, and do they share the same party or act on different parties? Record "
    "none if no other M-code characteristic is present.")
_M065_REVIEW_NOTE_SUFFIX = (
    " | Enriched 2026-09-21, escalation #1819 (researcher instruction: achieve rich/comprehensive "
    "relational understanding across all M-code strongs in a verse): added explicit relation-type "
    "vocabulary (cause/enable/intensify/block/respond-to/tension) and same-party-vs-different-"
    "party framing, so the answer is systematic rather than an open, unguided narrative.")

_M066_TEXT = (
    "Taking every M-code characteristic present in this verse together, what is the overall "
    "relational network this verse depicts -- which characteristics connect to which others, and "
    "how does this characteristic's own role fit within that whole picture? Record none if this "
    "characteristic is the verse's only M-code element.")


def enrich_m065(conn: sqlite3.Connection) -> str:
    row = conn.execute(
        "SELECT question_text, review_note FROM wa_obs_question_catalogue "
        "WHERE question_code='M0.6.5' AND deleted=0").fetchone()
    if row is None:
        return "M0.6.5: SKIPPED -- no live row found"
    current_text, current_note = row
    if current_text == _M065_ENRICHED_TEXT:
        return "M0.6.5: already enriched -- no-op"
    new_note = (current_note or "") + _M065_REVIEW_NOTE_SUFFIX
    conn.execute(
        "UPDATE wa_obs_question_catalogue SET question_text=?, catalogue_version=?, "
        "last_modified=?, review_note=? WHERE question_code='M0.6.5' AND deleted=0",
        (_M065_ENRICHED_TEXT, _CATALOGUE_VERSION, _MODIFIED_DATE, new_note))
    return "M0.6.5: question_text enriched"


def add_m066(conn: sqlite3.Connection) -> str:
    existing = conn.execute(
        "SELECT 1 FROM wa_obs_question_catalogue WHERE question_code='M0.6.6' AND deleted=0"
    ).fetchone()
    if existing:
        return "M0.6.6: already exists -- no-op"
    conn.execute(
        "INSERT INTO wa_obs_question_catalogue (question_code, section, question_text, scope, "
        "status, deleted, date_added, catalogue_version, review_note, tier, component_code, "
        "component_title, prompt_seq, source, last_modified, dimension, data_mechanism, window) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        ("M0.6.6", "M0", _M066_TEXT, "The verse", "active", 0, _MODIFIED_DATE,
         _CATALOGUE_VERSION,
         "New 2026-09-21, escalation #1819 (researcher instruction: achieve rich/comprehensive "
         "relational understanding across all M-code strongs in a verse). M0.6.5 is deliberately "
         "single-vantage (each cluster's own pass adds its own view on the OTHERS, progressive "
         "chain across passes, #1723) -- this closes the whole-network gap that design leaves: "
         "one question synthesising the FULL M-code network present in the verse, not just one "
         "characteristic's own vantage on it.",
         "M0", "M0.6", "Verse and Literary Interpretation", 8,
         "escalation #1819, researcher instruction 2026-09-21", _MODIFIED_DATE, "M0",
         "Every live verse_lexical row's M-code role tags in the verse, read together; "
         "cross-referenced against prior M0.6.6 findings for the same verse (progressive, own "
         "feed, kept separate from M0.6.5's own chain).",
         "relational"))
    return "M0.6.6: inserted"


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        r1 = enrich_m065(conn)
        r2 = add_m066(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print(r1)
    print(r2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
