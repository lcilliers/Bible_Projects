"""reword_word_level_questions_strong_keyed_v1_20260923.py — ONE-OFF migration, researcher
instruction verbatim (this chat, 2026-09-23): "cluster has no role to play, the keys for further
analysis is strong and verse. ... rephrase the questions so it is explicit and precise."

Scope: the 11 word-level (M0.1.x/M0.5.x) catalogue questions that escalation #1849's full 34-
question review found do not fit Stage 1's verse-context objective -- they ask about the CLUSTER
("characteristic")'s name/vocabulary as a whole, not this verse's content. Researcher's ruling
resolves that: cluster has no role at all; each question is a fact about ONE strong (term), full
stop -- one canonical `ib_observation` per (strong, question_code), one `ib_node` per verse where
that strong occurs. "Primary Hebrew and Greek terms" (a cluster-spanning, two-testament phrase) no
longer means anything once cluster is dropped -- reworded to "this term" throughout, singular,
matching the #1822 precedent for M0.5.2/M0.5.3.

M0.5.5/M0.5.6/M0.5.7/M0.5.8 asked about "the vocabulary" (the cluster's whole member set) --
reworded to ask about THIS term's own `strong_related` entries instead (a strong-keyed table,
confirmed live, not cluster-keyed) -- the relational pool moves from cluster membership to root/
cognate family, matching the researcher's own ruling.

M0.5.8 specifically reworded per researcher's explicit correction, verbatim: "just saying it is NT
or OT add no value - what does make a difference is if the interpretation of the word in context is
affected, and how by the Testament context" -- the question no longer asks for a bare OT/NT label,
it asks whether/how Testament context changes the term's own interpretation.

M0.5.10 ("the full vocabulary arc... the characteristic's complete semantic range") has no referent
left once cluster has no role -- retired (deleted=1), not reworded. M0.5.3 already covers semantic
range at the term level.

Idempotent (checks live text before writing) -- a second run is a no-op.

    python -m iba.app.migration.reword_word_level_questions_strong_keyed_v1_20260923
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v11-strong-keyed-cluster-dropped-20260923"
_MODIFIED_DATE = "2026-09-23"
_REVIEW_NOTE_SUFFIX = (
    " | Reworded 2026-09-23, researcher ruling (escalation #1849 follow-on): cluster has no role "
    "in these questions -- the key is strong and verse only. Reworded from cluster/'characteristic' "
    "framing to a single-term fact; relational questions (M0.5.5-8) now draw their candidate pool "
    "from strong_related (strong-keyed) instead of cluster membership.")

_REVISED_TEXT = {
    "M0.1.1": "What is this term's own name (lemma/transliteration), and what does that name "
        "signal about its essential nature?",
    "M0.1.2": "What does this term show at the definitional level, drawn from its own lexicon "
        "entries (root sense, LSJ, Mounce)?",
    "M0.1.3": "What directional, relational, or constitutional implication does this term's own "
        "name carry?",
    "M0.5.1": "What does this term's root meaning show?",
    "M0.5.2": "What is the grammatical range of this term (noun, verb, adjective, participle), "
        "and what does that range show about how it operates?",
    "M0.5.4": "Does this term itself express a specific aspect — disposition versus act, received "
        "versus given, condition versus quality? Record which, or none.",
    "M0.5.5": "Among this term's own related terms, is there one that functions as its structural "
        "opposite? Record it, or none.",
    "M0.5.6": "Among this term's own related terms, is there a person-type term — one for a "
        "person who habitually possesses or exercises it? Record it, or none.",
    "M0.5.7": "Among this term's own related terms, is there a supplication or seeking term — one "
        "for the act of seeking it from another? Record it, or none.",
    "M0.5.8": "Does this term's Testament context (OT Hebrew vs. NT Greek) affect how it should be "
        "interpreted, and if so, how? Record none if the Testament context makes no interpretive "
        "difference.",
    "M0.5.9": "Is this term newly coined in the NT period; if so, what does that coinage show? "
        "Record it, or none.",
}

_RETIRE = ["M0.5.10"]


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
        report.append(f"{code}: question_text updated (cluster/characteristic -> this term)")

    for code in _RETIRE:
        row = conn.execute(
            "SELECT deleted, review_note FROM wa_obs_question_catalogue "
            "WHERE question_code=?", (code,)).fetchone()
        if row is None:
            report.append(f"{code}: SKIPPED -- no live row found")
            continue
        if row[0] == 1:
            report.append(f"{code}: already retired -- no-op")
            continue
        new_note = (row[1] or "") + (
            " | Retired 2026-09-23: 'the characteristic's complete semantic range' has no referent "
            "once cluster has no role in these questions -- M0.5.3 already covers term-level "
            "semantic range.")
        conn.execute(
            "UPDATE wa_obs_question_catalogue SET deleted=1, last_modified=?, review_note=? "
            "WHERE question_code=?", (_MODIFIED_DATE, new_note, code))
        report.append(f"{code}: retired (deleted=1)")

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
