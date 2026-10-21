"""add_verse_substantiation_questions_v1_20260921.py — ONE-OFF migration, escalation #1806,
researcher instruction verbatim: "Start at the char question. work question by question. determine
what must be known from the verse to answer the question. then design the verse-reading question
that will generate the data in the right format... verse-reading does not know, and does not
answer to a char, it purely based on the meaning of the words and there inter relationship."

Adds 16 new, word-level, characteristic-agnostic verse-reading questions (new component `M0.7`) --
one per Category A "char question" (the `D10`/`D3`/`D6`/`D7`/`F0` per-verse family, `gap-closure-
design-20260921.md`). Each is a minimal transformation of its own char-question: strip "the
characteristic" framing entirely, ask about the specific WORD and its own relationships in the
verse instead. `D10.4.1` is the confirmed worked example from this same conversation; the other 15
follow the identical pattern.

**Numbering is 1:1 and traceable**: `M0.7.N` substantiates the Nth char-question in this family
(`M0.7.4` <-> `D10.4.1`, etc.) -- deliberate, so the link is visible in the code itself, not just
in this docstring.

**Placement, per the researcher's own correction this same conversation**: PER-OCCURRENCE, not
front-loaded-once like `M0.1`/`M0.5` -- these are not invariant word-level facts (a word can behave
differently verse to verse, same shape as `M0.5.11`'s existing divergence-check). Consolidation of
genuinely-repeated findings across occurrences is the same/broaden/new mechanism's job, now backed
by the new `concise-and-verse-specific-obs-text` method rule (escalation #1824) that makes that
mechanism actually able to recognise true duplicates.

**What this migration does NOT do**: wire these into Stage 1's actual prompt/selection code (a
separate change, `versereadinggenerate.py`), or wire the original 16 char-questions into Stage 3 to
consume these as their own grounding (a larger, separate change to `charreadinggenerate.py`, which
currently never writes a real `question_code` at all -- out of scope for this migration, flagged
as the necessary next step, not rushed into the same change).

Idempotent (checks for an existing live row before inserting).

    python -m iba.app.migration.add_verse_substantiation_questions_v1_20260921
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_DATE = "2026-09-21"
_CATALOGUE_VERSION = "v8-verse-substantiation-20260921"
_COMPONENT_CODE = "M0.7"
_COMPONENT_TITLE = "Verse Substantiation (word-level, characteristic-agnostic)"

# (new_code, substantiates, window, question_text)
_NEW_QUESTIONS = [
    ("M0.7.1", "D10.1.1", "action-impact",
     "In this verse, does [this word] state or imply any purpose, role, or effect it serves for "
     "the person it relates to -- what it leads them to be, do, or become? Record it if stated; "
     "otherwise record none."),
    ("M0.7.2", "D10.2.1", "affective",
     "In this verse, what first or most immediate inner-being response does [this word] show in "
     "the person it relates to, following from it? Record it, or record none."),
    ("M0.7.3", "D10.3.1", "action-impact",
     "In this verse, what does [this word] produce in the inner being of the person it relates "
     "to, over time -- what states, qualities, capacities, or orientations does it establish? "
     "Record it, or record none."),
    ("M0.7.4", "D10.4.1", "action-impact",
     "In this verse, does [this word] depict or relate to a change in a person's state, "
     "condition, or disposition -- and if so, what changes, is the change in their condition "
     "itself, their orientation/response to it, or both, and does the verse indicate whether the "
     "change is lasting or temporary? Record none if no such change is shown."),
    ("M0.7.5", "D10.5.1", "action-impact",
     "In this verse, does [this word] describe a sequence of inner states the person it relates "
     "to moves through -- a before, during, and after -- and what are those states? Record none "
     "if no sequence is shown."),
    ("M0.7.6", "D10.6.1", "operational",
     "In this verse, by what mechanism does [this word] produce change in the person it relates "
     "to -- discipline, encounter, gradual formation, sudden transformation, or other? Record "
     "none if no mechanism is shown."),
    ("M0.7.7", "D3.1.1", "operational",
     "In this verse, in what distinct mode(s) does [this word] operate within the inner person "
     "-- the manner of its functioning? Record it, or record none if not determinable."),
    ("M0.7.8", "D6.1.1", "constitutional",
     "In this verse, at which constitutional level(s) is [this word] located -- from {spirit, "
     "soul, heart, mind, other soul-subset, a named body part} -- and how is each engaged? "
     "Record every level evidenced, or none."),
    ("M0.7.9", "D7.5.1", "origin",
     "In this verse, where does [this word] originate -- generated within the person, received "
     "from another person, bestowed by God, carried generationally, introduced by another spirit "
     "(angelic or adversarial), or not stated? Record the origin, or record that it is not "
     "stated."),
    ("M0.7.10", "F0.1.1", "faculty",
     "In this verse, does [this word] engage or get affected by any inner-being faculty (the "
     "senses, spiritual discernment, cognition, memory, affect, creativity, volition, agency, "
     "moral evaluation, conscience, conscientiousness, or relational capacity), and if so which "
     "and how? Record none if it does not."),
    ("M0.7.11", "D5.2.1", "relational",
     "In this verse, does [this word] operate in the person's movement toward God -- seeking, "
     "supplication, worship, covenant -- and if so how? Record none if it does not."),
    ("M0.7.12", "D7.1.1", "relational",
     "In this verse, does [this word] operate from God toward the human person, and if so how? "
     "Record none if it does not."),
    ("M0.7.13", "D7.2.1", "relational",
     "In this verse, is [this word] extended by one person toward another, and if so how does it "
     "operate in that extension? Record none if it is not."),
    ("M0.7.14", "D7.3.1", "relational",
     "In this verse, is [this word] taken up by a person from another, and if so how does it "
     "operate in that uptake? Record none if it is not."),
    ("M0.7.15", "D7.4.1", "relational",
     "In this verse, does [this word] operate in relation to other spiritual beings -- angelic "
     "or adversarial -- and if so how? Record none if it does not."),
    ("M0.7.16", "D7.6.1", "relational",
     "In this verse, is [this word] predicated of God or otherwise related to God; if so, in "
     "what relation (God as the one who bears it, acts, gives it, or is its object)? Record the "
     "relation, or record that it is not related to God here."),
]


def apply_migration(conn: sqlite3.Connection) -> list[str]:
    report = []
    for seq, (code, substantiates, window, text) in enumerate(_NEW_QUESTIONS, start=1):
        existing = conn.execute(
            "SELECT 1 FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
            (code,)).fetchone()
        if existing:
            report.append(f"{code}: already exists -- no-op")
            continue
        conn.execute(
            "INSERT INTO wa_obs_question_catalogue (question_code, section, question_text, "
            "scope, status, deleted, date_added, catalogue_version, review_note, tier, "
            "component_code, component_title, prompt_seq, source, last_modified, dimension, "
            "data_mechanism, window) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (code, "M0", text, "Verse-context", "active", 0, _DATE, _CATALOGUE_VERSION,
             f"New {_DATE}, escalation #1806: word-level, characteristic-agnostic verse-reading "
             f"substantiation for {substantiates} -- built following the researcher's own method "
             f"(start at the char question, determine what must be known from the verse, design "
             f"the verse-reading question that supplies it). Stage 1 answers this per occurrence "
             f"(NOT front-loaded/settled-once -- this can genuinely vary verse to verse, same "
             f"shape as M0.5.11); {substantiates} itself and its own aggregate follow-up remain "
             f"the 'char question', to be deduced by a later stage from this observation plus "
             f"static cluster-membership data, per the researcher's own stated architecture. Not "
             f"yet wired into Stage 1's actual prompt/selection code, nor is {substantiates} yet "
             f"wired to consume it -- both separate, not-yet-applied changes.",
             "M0", _COMPONENT_CODE, _COMPONENT_TITLE, seq,
             "escalation #1806, researcher instruction 2026-09-21", _DATE, "M0", None, window))
        report.append(f"{code}: inserted (substantiates {substantiates})")
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = apply_migration(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    print(f"\n{sum(1 for r in report if 'inserted' in r)} inserted, "
         f"{sum(1 for r in report if 'no-op' in r)} already existed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
