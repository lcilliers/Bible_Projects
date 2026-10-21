"""simplify_M0_8_1_elevation_flag_v1_20260923.py — ONE-OFF migration, researcher instruction
verbatim (this chat, 2026-09-23): "fix the solution for M0.8.1" -- worked example given: G4020
(2Th.3.11, 1Ti.5.13) is tagged T2 and so gets no attention from any cluster, yet its behaviour in
those verses is plainly significant on its own terms. "All M0.8.1 is asking for is that an
observation is created to flag [it] as a term that need further attention" -- not a reasoned ruling
on whether to formally elevate it to its own M-code.

Finding, checked against live data before changing anything: the ORIGINAL wording ("does its role
here suggest it names a distinct inner-being characteristic in its own right, warranting elevation
to its own M-code... record none if it genuinely functions as a supporting role (manner,
operation-word, qualifier)") asks for a formal taxonomy ruling, not a flag. Live effect, all 483
M0.8.1 observations: only 11 (2.3%) carry the intended `elevation-candidate` tag; 363 (75%) carry
`not-related-to-meaningful-word` -- a tag that has nothing to do with this question's own subject,
strong evidence the wording is confusing the model about what's actually being asked, not that real
candidates are simply rare.

What this migration does NOT touch, and why: the population/coverage/payload mechanism
(stage1coverage.py's expected_nodes, versereadinggenerate.py's elevation_candidates_by_verse,
recordingpass.py's per-verse dedup family, the `elevation-candidate` tag itself) exactly mirrors the
existing pattern already used for M0.6.5/M0.6.6/D7.7.1 -- checked directly, not assumed -- so it is
proportionate to a per-verse question like this one and is not being ripped out. The actual fix is
narrower: the CATALOGUE WORDING (this file) and the matching LLM-facing prompt paragraph in
versereadinggenerate.py (edited alongside this migration, same unit of work, per
governance.build_md_on_code_change).

Open item, NOT resolved here (researcher's own call, same shape as escalation #1815's parallel
question about its own 149 mislabeled rows): whether the 483 already-recorded M0.8.1 observations
(350 draft + 133 withdrawn) should be re-derived under the simplified wording. Left as-is.

Idempotent (checks live text before writing) -- a second run is a no-op.

    python -m iba.app.migration.simplify_M0_8_1_elevation_flag_v1_20260923
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_CATALOGUE_VERSION = "v10-elevation-flag-simplified-20260923"
_MODIFIED_DATE = "2026-09-23"
_REVIEW_NOTE_SUFFIX = (
    " | Simplified 2026-09-23, researcher instruction ('fix the solution for M0.8.1', worked "
    "example G4020/2Th.3.11+1Ti.5.13): reworded from a formal elevation ruling (with a "
    "disqualifying taxonomy of 'manner, operation-word, qualifier') to a plain flag ask. Live "
    "evidence for the change: only 11/483 (2.3%) prior observations carried the intended "
    "elevation-candidate tag; 363/483 (75%) carried a mismatched tag "
    "('not-related-to-meaningful-word'), indicating the old wording was confusing the model, not "
    "that real candidates are rare.")

_REVISED_TEXT = {
    "M0.8.1": "In this verse, this word carries a T2 or T3 supporting-role tag, not its own "
        "M-code. Does its behavior here make it significant enough on its own terms to deserve "
        "closer attention as a possible characteristic in its own right? If yes, briefly state "
        "why; otherwise record none.",
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
        report.append(f"{code}: question_text updated (elevation ruling -> plain flag)")
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
