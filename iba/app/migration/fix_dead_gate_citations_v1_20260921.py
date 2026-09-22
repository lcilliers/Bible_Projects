"""fix_dead_gate_citations_v1_20260921.py — ONE-OFF migration, escalation #1823, researcher
instruction verbatim: "bring the CSV up to date. and ensure that the catalogue questions text does
not include stale terminology that is no longer relevant."

Finding 15 (#1823) found 8 D7-family questions citing a per-verse "gate" question by code
(`(per D7.1.1)` etc.) that is itself `STRUCTURALLY-UNREACHABLE` -- never asked by any stage, ever.
Answering this properly meant checking EVERY `(per CODE)` citation in the live catalogue, not just
the D7 family this was first spotted in -- found the same pattern in `D10`/`D3`/`D5`/`D6` too.
15 questions total cite a dead gate code (some of these citations were authored by the #1814
wording revision itself, applying its own "cite by code" convention without checking the cited
code was reachable -- see BUILD.md/escalation #1823 for the full admission).

Fix: for each, drop the `(per CODE)` citation to a code that will never resolve, and inline the
gate's own filter condition in plain language instead -- same subject+grain convention #1814
already established, just self-contained rather than depending on a citation that points at
nothing. `D7.3.3`'s citation to `D7.3.2` (which IS reachable) is also dropped for consistency/
simplicity, since D7.3.2 is a sibling not a strict prerequisite -- the plain-language condition
already carries the full meaning without it.

NOT touched here (a design/wiring decision, not a text-cleanup one, tracked on #1823): whether the
15 dead gate questions themselves (`D10.2.1`, `D10.4.1`, `D10.6.1`, `D3.1.1`, `D5.2.1`, `D6.1.1`,
`D7.1.1`, `D7.2.1`, `D7.3.1`, `D7.4.2a`, `D7.4.3a`, `D7.5.1`) should have their `scope` corrected
so they become reachable, or should be retired since their own aggregate follow-up no longer
depends on them.

Idempotent (checks live text before writing) -- a second run is a no-op.

    python -m iba.app.migration.fix_dead_gate_citations_v1_20260921
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v5-dead-citation-fix-20260921"
_MODIFIED_DATE = "2026-09-21"
_REVIEW_NOTE_SUFFIX = (
    " | Citation fixed 2026-09-21, escalation #1823: was citing a per-verse gate question by code "
    "that is itself STRUCTURALLY-UNREACHABLE (never asked by any stage) -- filter condition "
    "inlined in plain language instead of citing a dead code.")

_REVISED_TEXT = {
    "D10.2.2": "Across the characteristic's verses that show an immediate inner-being response "
        "following it, is that response consistent, or does it vary by context?",
    "D10.4.2": "Across the characteristic's verses that show it producing transformation in the "
        "person, is that transformation reversible or irreversible?",
    "D10.6.2": "Across the characteristic's verses that show a mechanism of change (discipline, "
        "encounter, gradual formation, sudden transformation, or other), does that mechanism "
        "differ by context, and if so how?",
    "D3.1.2": "Across the characteristic's verses, does its manner of functioning within the "
        "inner person vary by context, direction, or constitutional level; if so how?",
    "D5.2.2": "Across the characteristic's verses that show it operating in the person's "
        "movement toward God (seeking, supplication, worship, covenant), what inner posture does "
        "that movement require?",
    "D5.2.3": "Across the characteristic's verses that show it operating in the person's "
        "movement toward God, what does that direction show about the person's relationship with "
        "God?",
    "D6.2.1": "Across the characteristic's verses that locate it at both a named body part and a "
        "spirit/soul/heart/mind level together, in which direction does that link run -- soul/"
        "spirit expressing through the body, the body feeding back to the soul, or both -- and "
        "what follows from that direction? If no such body link appears, record none.",
    "D7.1.2": "Across the characteristic's verses that show it operating from God toward the "
        "human person, on what basis does God extend it -- conditional, unconditional, "
        "covenantal, or responsive?",
    "D7.1.3": "Across the characteristic's verses that show it operating from God toward the "
        "human person, what does God's extension show about his disposition toward the human "
        "person?",
    "D7.2.2": "Across the characteristic's verses that show it extended by one person toward "
        "another, what inner conditions or orientations in the giver accompany that extension?",
    "D7.2.3": "Across the characteristic's verses that show it extended by one person toward "
        "another, what must a person have received or become before they extend the "
        "characteristic themselves?",
    "D7.3.3": "Across the characteristic's verses that show a person meeting the characteristic "
        "from another but not taking it up, what is their inner-being state?",
    "D7.4.2b": "At the characteristic level, what does the pattern of adversarial spiritual "
        "beings appearing as an acting party in the characteristic's verses show about the "
        "characteristic being a site of adversarial activity?",
    "D7.4.3b": "At the characteristic level, what does the pattern of angelic beings appearing "
        "as an acting party in the characteristic's verses show about the characteristic being "
        "communicated, strengthened, or mediated through angelic ministry?",
    "D7.5.2": "Across the characteristic's verses, is its stated origin (generated within the "
        "person, received from another, bestowed by God, carried generationally, or introduced "
        "by another spirit) single or multiple, and does it change with context?",
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
            report.append(f"{code}: already matches revised text -- no-op")
            continue
        new_note = (current_note or "") + _REVIEW_NOTE_SUFFIX
        conn.execute(
            "UPDATE wa_obs_question_catalogue SET question_text=?, catalogue_version=?, "
            "last_modified=?, review_note=? WHERE question_code=? AND deleted=0",
            (revised_text, _CATALOGUE_VERSION, _MODIFIED_DATE, new_note, code))
        report.append(f"{code}: question_text updated (dead citation removed)")
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
    print(f"\n{sum(1 for r in report if 'updated' in r)} row(s) updated, "
         f"{sum(1 for r in report if 'no-op' in r)} already correct, "
         f"{sum(1 for r in report if 'SKIPPED' in r)} skipped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
