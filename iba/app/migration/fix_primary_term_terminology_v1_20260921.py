"""fix_primary_term_terminology_v1_20260921.py — ONE-OFF migration, escalation #1822 v2,
researcher instruction verbatim: "fix the redundant terminology."

Finding: "the primary term" (M0.5.2/M0.5.3, also M0.4.1/M0.6.1) has no operational definition
anywhere in the live pipeline -- Stage 1 answers M0.1/M0.5 per strong (#1723 front-loading), and
every strong gets its own answer framed as if it alone were "the primary term," with no selection
ever happening. Fix: replace "the primary term" with "this term" everywhere it appears in the live
catalogue -- matches the actual per-strong mechanism exactly (each answer genuinely is about THIS
specific term, no false "primary" designation implied). `M0.5.2`/`M0.5.3` are the escalation's own
named scope (both live, DYNAMIC-STAGE1); `M0.4.1`/`M0.6.1` carry the identical latent issue and are
fixed too for consistency, though both are currently STRUCTURALLY-UNREACHABLE (dead weight either
way) -- avoids the same confusion resurfacing if #1806's original verse-context redesign ever wires
them in. `M0.6.1`'s separate "primary verse" phrase is NOT touched -- a different concept (likely
related to M0.6.3/M0.6.4's anchor-verse idea), not this escalation's scope.

Idempotent (checks live text before writing) -- a second run is a no-op.

    python -m iba.app.migration.fix_primary_term_terminology_v1_20260921
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v7-primary-term-fix-20260921"
_MODIFIED_DATE = "2026-09-21"
_REVIEW_NOTE_SUFFIX = (
    " | Fixed 2026-09-21, escalation #1822: 'the primary term' had no operational definition -- "
    "Stage 1 answers this per strong (#1723 front-loading), every strong treated as if it alone "
    "were primary, no selection ever happens. Replaced with 'this term', matching the actual "
    "per-strong mechanism.")

_REVISED_TEXT = {
    "M0.4.1": "What is the grammatical/stem form of this term in this verse?",
    "M0.5.2": "What is the grammatical range of this term (noun, verb, adjective, participle), "
        "and what does that range show about how the characteristic operates?",
    "M0.5.3": "What is the semantic range of this term — across what breadth of meaning does it "
        "operate, including any idiomatic, analogical, or otherwise implied meaning carried by "
        "its use in combination with other terms?",
    "M0.6.1": "What is the function of this term within its primary verse -- (a) what role does "
        "it play in the sentence, and (b) what role does it play in the verse's own argument, if "
        "a connective/chain edge shows one?",
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
        report.append(f"{code}: question_text updated ('the primary term' -> 'this term')")
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
