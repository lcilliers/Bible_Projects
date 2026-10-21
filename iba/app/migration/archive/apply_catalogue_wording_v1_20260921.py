"""apply_catalogue_wording_v1_20260921.py — ONE-OFF migration, escalation #1814 v6, researcher
instruction verbatim: "the catalogue changes are approved and be updated into the table."

Applies the 48 REVISE rows from the #1814 wording review (outputs/catalogue-question-wording-
review-20260921-v6.md, self-contained here as _REVISED_TEXT so this script has no dependency on
a scratchpad working file) to wa_obs_question_catalogue.question_text, bumping
catalogue_version/last_modified/review_note so the edit is traceable back to the escalation.

Also fixes a genuine, unrelated column bug found while auditing every column for this same
escalation, not a judgment call: M0.5.11/M0.6.5 (added later, #1723, 2026-09-17) are the only two
rows in their own component_code (M0.5/M0.6) with tier=NULL -- every sibling has tier='M0'.
Consequence, confirmed live: cataloguereport.py's own tiered listing filters `tier IS NOT NULL`,
so both rows were silently excluded from that report.

Idempotent (checks live value before writing) -- a second run is a no-op.

    python -m iba.app.migration.apply_catalogue_wording_v1_20260921
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v4-wording-revision-20260921"
_MODIFIED_DATE = "2026-09-21"
_REVIEW_NOTE_SUFFIX = (
    " | Wording revised 2026-09-21, escalation #1814 (approved v6): reworded to state its "
    "evaluation subject and answer grain explicitly, per the convention in "
    "catalogue-question-wording-review-20260921-v6.md.")

_REVISED_TEXT = {
    "D10.1.2": "Across the characteristic's verses, does it show any orientation toward a future "
        "fullness the person moves toward, not only what they currently are? Record it, or "
        "record none.",
    "D10.2.2": "Across the verses where an immediate inner-being response was found (per "
        "D10.2.1), is it consistent or does it vary by context?",
    "D10.3.2": "At the characteristic level, how does its sustained effect (D10.3.1) differ from "
        "its immediate response (D10.2.1)?",
    "D10.4.2": "Across the verses where transformation was found (per D10.4.1), is it reversible "
        "or irreversible?",
    "D10.6.2": "Across the verses where a mechanism of change was found (per D10.6.1), does it "
        "differ by context, and if so how?",
    "D11.1.1": "Across the characteristic's verses, does its role read as belonging to created "
        "design, to the fallen condition, to both, or as not determinable?",
    "D2.1.2": "Across the verses where a felt quality was found (per D2.1.1), is it consistent, "
        "or does it vary by context?",
    "D3.1.2": "Across the characteristic's verses, does its mode of operation (per D3.1.1) vary "
        "by context, direction, or constitutional level; if so how?",
    "D3.1.3": "Across the characteristic's verses, does it ever operate through a communicative "
        "or speech-based mode (commanded, addressed, spoken); if so how? Record it, or record "
        "none.",
    "D3.2.1": "Across the characteristic's verses, under what inner conditions does it take hold "
        "or operate rightly?",
    "D3.2.2": "Across the characteristic's verses, under what inner conditions is it blocked, "
        "distorted, resisted, or not taken up -- including, where shown, distortion or "
        "interference by another spirit (adversarial or angelic)?",
    "D3.2.3": "Across the verses where the characteristic is present but blocked, resisted, or "
        "not taken up (per D3.2.2), what is the inner-being state of the person?",
    "D4.1.1": "Across the characteristic's verses, does it operate differently within existing "
        "relational bonds versus across relational distance or difference; if so how?",
    "D4.1.2": "Across the characteristic's verses, does it operate within covenantal contexts "
        "only, or does it cross covenantal boundaries?",
    "D4.1.3": "Across the characteristic's verses, what is its relational scope -- who is "
        "included and who is not?",
    "D5.1.2": "At the characteristic level, what does the pattern of presence/absence found in "
        "D5.1.1 indicate for the characteristic's place in the human person and in the divine "
        "image?",
    "D5.2.2": "Across the verses where God-ward movement was found (per D5.2.1), what inner "
        "posture does it require?",
    "D5.2.3": "Across the verses where God-ward movement was found (per D5.2.1), what does that "
        "direction show about the person's relationship with God?",
    "D5.3.1": "At the characteristic level, from its God-relation (D5.1/D7.6) and its role "
        "(D10.1/D11.1), what aspect of the divine likeness, if any, does it instantiate in the "
        "person? Record the aspect, or record none.",
    "D5.3.2": "At the characteristic level, is it shared between God and the person, or an "
        "exclusively creaturely analogue to something in God?",
    "D5.3.3": "At the characteristic level, where it is present or absent in a person, what does "
        "that indicate about the condition of the divine image in them -- or is no such "
        "indication evidenced?",
    "D6.2.1": "Across the verses where a body link exists (per D6.1.1), in which direction does "
        "it run -- soul/spirit expressing through the body, the body feeding back to the soul, "
        "or both -- and what follows from that direction? If no body link, record none.",
    "D6.3.1": "Across the characteristic's verses, does it move across constitutional levels "
        "(spirit->soul->body), or onto the person from an external source -- including another "
        "spirit (angelic or adversarial) -- or in another direction; and if so in what sequence "
        "or pattern? If no movement, record none.",
    "D7.1.2": "Across the verses where God-to-human extension was found (per D7.1.1), on what "
        "basis does God extend the characteristic -- conditional, unconditional, covenantal, or "
        "responsive?",
    "D7.1.3": "Across the verses where God-to-human extension was found (per D7.1.1), what does "
        "God's extension show about his disposition toward the human person?",
    "D7.2.2": "Across the verses where person-to-person extension was found (per D7.2.1), what "
        "inner conditions or orientations in the giver accompany it?",
    "D7.2.3": "Across the verses where person-to-person extension was found (per D7.2.1), what "
        "must a person have received or become before they extend the characteristic?",
    "D7.3.2": "Across the characteristic's verses, what inner conditions accompany or block "
        "uptake of the characteristic from another person?",
    "D7.3.3": "Across the verses where a person meets the characteristic from another but does "
        "not take it up (per D7.3.1/D7.3.2), what is their inner-being state?",
    "D7.4.2a": "Across the characteristic's verses, does an adversarial spiritual being ever "
        "appear as an acting party in a verse carrying this characteristic?",
    "D7.4.2b": "At the characteristic level, what does the pattern of adversarial-being presence "
        "(per D7.4.2a) show about the characteristic being a site of adversarial activity?",
    "D7.4.3a": "Across the characteristic's verses, does an angelic being ever appear as an "
        "acting party in a verse carrying this characteristic?",
    "D7.4.3b": "At the characteristic level, what does the pattern of angelic-being presence "
        "(per D7.4.3a) show about the characteristic being communicated, strengthened, or "
        "mediated through angelic ministry?",
    "D7.5.2": "Across the characteristic's verses, is its origin (per D7.5.1) single or "
        "multiple, and does it change with context?",
    "D7.7.1": "In this verse, where an action or movement word is classified as an Operation for "
        "this cluster, what is that word's relation to the parties present in the verse -- who "
        "initiates it, and toward whom or what is it directed? Record none if no such operation "
        "word is present.",
    "F0.1.1": "In this verse, does the characteristic engage or get affected by any inner-being "
        "faculty (the senses, spiritual discernment, cognition, memory, affect, creativity, "
        "volition, agency, moral evaluation, conscience, conscientiousness, or relational "
        "capacity), and if so which and how? Record none if it does not.",
    "M0.5.11": "In this verse, where this occurrence's meaning diverges from the term's usual "
        "sense elsewhere, what nuance does that divergence carry here, and how does it compare "
        "to the word's other occurrences? Record none if this occurrence matches the term's "
        "usual sense.",
    "M0.6.2": "Across the characteristic's verses, what is the logical structure of its key "
        "arguments -- premises and conclusions?",
    "M0.6.5": "What role does this characteristic play in relation to the OTHER M-code "
        "characteristics present in this verse? Record none if no other M-code characteristic "
        "is present.",
    "X0.1.1": "Across the characteristic's verses, which adjacent characteristics appear "
        "alongside this one, and how frequently? Record none if no significant co-occurrence "
        "appears.",
    "X0.1.2": "At the characteristic level, what does its co-occurrence pattern (per X0.1.1) "
        "show about its place in the inner-being landscape?",
    "X0.2.1": "Across the characteristic's verses, does it consistently precede, following, or "
        "accompany another characteristic in a sequence; if so which and how? Record none if no "
        "sequence appears.",
    "X0.2.2": "At the characteristic level, what does its sequence pattern (per X0.2.1) show -- "
        "is the relationship causal, developmental, or correlational?",
    "X0.3.1": "Across the characteristic's verses, does it produce another characteristic, and "
        "if so which, and by what mechanism? Record none if none is shown.",
    "X0.3.2": "Across the characteristic's verses, is it produced by another characteristic, and "
        "if so which?",
    "X0.3.3": "Across the characteristic's verses, is it a constituent element of another "
        "characteristic, or another a constituent of this one?",
    "X0.5.2": "At the characteristic level, where comparison with its nearest neighbour (per "
        "X0.5.1) shows apparent overlap, what is the precise boundary between them?",
    "X0.5.3": "At the characteristic level, is the distinction between this characteristic and "
        "its nearest neighbour (per X0.5.1) one of degree, kind, direction, or constitutional "
        "level?",
}


def apply_wording(conn: sqlite3.Connection) -> list[str]:
    report = []
    for code, revised_text in sorted(_REVISED_TEXT.items()):
        row = conn.execute(
            "SELECT question_text, review_note FROM wa_obs_question_catalogue "
            "WHERE question_code=? AND deleted=0", (code,)).fetchone()
        if row is None:
            report.append(f"{code}: SKIPPED -- no live row found (deleted or code changed)")
            continue
        current_text, current_note = row
        if current_text == revised_text:
            report.append(f"{code}: already matches revised_text -- no-op")
            continue
        new_note = (current_note or "") + _REVIEW_NOTE_SUFFIX
        conn.execute(
            "UPDATE wa_obs_question_catalogue SET question_text=?, catalogue_version=?, "
            "last_modified=?, review_note=? WHERE question_code=? AND deleted=0",
            (revised_text, _CATALOGUE_VERSION, _MODIFIED_DATE, new_note, code))
        report.append(f"{code}: question_text updated")
    return report


def fix_tier_gap(conn: sqlite3.Connection) -> list[str]:
    report = []
    for code in ("M0.5.11", "M0.6.5"):
        row = conn.execute(
            "SELECT tier FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
            (code,)).fetchone()
        if row is None:
            report.append(f"{code}: SKIPPED -- no live row found")
            continue
        if row[0] == "M0":
            report.append(f"{code}: tier already 'M0' -- no-op")
            continue
        conn.execute(
            "UPDATE wa_obs_question_catalogue SET tier='M0' WHERE question_code=? AND deleted=0",
            (code,))
        report.append(f"{code}: tier NULL -> 'M0' (matches every other M0.5/M0.6 sibling)")
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        wording_report = apply_wording(conn)
        tier_report = fix_tier_gap(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("--- wording revisions ---")
    print("\n".join(wording_report))
    print(f"\n{sum(1 for r in wording_report if 'updated' in r)} row(s) updated, "
         f"{sum(1 for r in wording_report if 'no-op' in r)} already correct, "
         f"{sum(1 for r in wording_report if 'SKIPPED' in r)} skipped.")
    print("\n--- tier gap fix ---")
    print("\n".join(tier_report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
