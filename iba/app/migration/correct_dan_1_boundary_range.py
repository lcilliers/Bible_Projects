"""correct_dan_1_boundary_range.py — ONE-OFF: correct Daniel's `1:7-21` passage range to `1:8-21`
(2026-07-29), and restore Dan.1.7's live `verse_passage` link to `1:1-7`, where it is actually
debated.

**The mistake, found by the researcher directly.** Dan.1.7 has always been a genuine boundary
verse shared between `Dan 1:1-7` and (mislabeled) `Dan 1:7-21` — but only `1:1-7` ever contains
its actual analysis; `1:7-21` only ever carried a one-paragraph "Dan 1:7 — carried by reference"
stub pointing back to it (see the debate text itself, both old and new). BUILD.md §28's own
verification treated the mechanical "one live owner per verse" invariant (satisfied by giving the
verse's live link to whichever range was processed later) as sufficient — it never checked which
file's PROSE actually contains the verse's analysis. This migration corrects that: the label
follows the invariant now, but the invariant itself is repointed to match where the analysis
actually lives.

**What this does, in order:**
1. Updates `passage` id 37416 in place: `start_verse` 7 -> 8, `ref` 'Dan 1:7-21' -> 'Dan 1:8-21',
   `verse_span_meaning_path`/`debate_path` -> the new files (already written by hand this session
   — `dan-1-8-21-verse-span-meaning.md`, generated via a direct `versespanmeaningreport.write_report`
   call with no passage-table side effects, and `WA-dan-1-8-21-debate-v1.3-2026-07-29.md`, hand-
   corrected from v1.2 with the Dan.1.7 stub removed), `anchor_verse_id` -> Dan.1.8's verse id,
   `verse_count` 15 -> 14.
2. Soft-deletes the `verse_passage` link (passage 37416, Dan.1.7) — it no longer belongs to this
   range.
3. Restores (un-deletes) the `verse_passage` link (passage 37415 = `Dan 1:1-7`, Dan.1.7) — this
   is where the verse is actually debated, and where it belongged all along.

Does **not** touch `Dan 1:1-7`'s own `verse_count` (already 7, correct once its Dan.1.7 link is
restored) or any other passage row. Does not alter any analytical conclusion, decision, or
silence-finding — only the range boundary, the file pointers, and which passage a `verse_passage`
row currently counts as live.

    python -m iba.app.migration.correct_dan_1_boundary_range
"""

from __future__ import annotations

import datetime
import sqlite3
import sys

from ..lib.cfg import DB_PATH

OLD_PASSAGE_ID = 37416          # Dan "1:7-21", to become "1:8-21"
SIBLING_PASSAGE_ID = 37415       # Dan "1:1-7" — where Dan.1.7 is actually debated
NEW_VERSE_SPAN_MEANING_PATH = "iba\\app\\verse-analysis\\Daniel\\dan-1-8-21-verse-span-meaning.md"
NEW_DEBATE_PATH = "iba\\app\\verse-analysis\\Daniel\\WA-dan-1-8-21-debate-v1.3-2026-07-29.md"


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    now = _now()

    # locate Dan.1.7's and Dan.1.8's verse ids and the two verse_passage rows involved
    dan_1_7 = conn.execute(
        "SELECT id FROM verse WHERE osisId='Dan.1.7' AND deleted=0").fetchone()
    dan_1_8 = conn.execute(
        "SELECT id FROM verse WHERE osisId='Dan.1.8' AND deleted=0").fetchone()
    if not dan_1_7 or not dan_1_8:
        print("Dan.1.7 or Dan.1.8 not found live in `verse` -- aborting, nothing changed.")
        return 1
    v7, v8 = dan_1_7["id"], dan_1_8["id"]

    old_link = conn.execute(
        "SELECT id, deleted FROM verse_passage WHERE passage_id=? AND verse_id=?",
        (OLD_PASSAGE_ID, v7)).fetchone()
    sibling_link = conn.execute(
        "SELECT id, deleted FROM verse_passage WHERE passage_id=? AND verse_id=?",
        (SIBLING_PASSAGE_ID, v7)).fetchone()
    if not old_link or not sibling_link:
        print("Expected verse_passage rows for Dan.1.7 not found on both sides -- aborting.")
        return 1
    if old_link["deleted"] != 0 or sibling_link["deleted"] != 1:
        print(f"Unexpected pre-state (old_link.deleted={old_link['deleted']!r}, "
              f"sibling_link.deleted={sibling_link['deleted']!r}, expected 0 and 1) -- aborting, "
              f"re-check before re-running.")
        return 1

    conn.execute(
        "UPDATE passage SET start_verse=8, ref='Dan 1:8-21', "
        "verse_span_meaning_path=?, verse_span_meaning_written_at=?, "
        "debate_path=?, debate_written_at=?, anchor_verse_id=?, verse_count=14 "
        "WHERE id=?",
        (NEW_VERSE_SPAN_MEANING_PATH, now, NEW_DEBATE_PATH, now, v8, OLD_PASSAGE_ID))
    conn.execute("UPDATE verse_passage SET deleted=1 WHERE id=?", (old_link["id"],))
    conn.execute("UPDATE verse_passage SET deleted=0, is_anchor=0 WHERE id=?",
                 (sibling_link["id"],))
    # the passage row's own anchor_verse_id was repointed to Dan.1.8 above, but the
    # verse_passage row for (OLD_PASSAGE_ID, Dan.1.8) still carries its original is_anchor=0
    # from when it was inserted as a non-anchor member of the (then-correct) 1:7-21 range —
    # flip it to match, so `SELECT ... WHERE is_anchor=1` finds exactly the passage's own
    # anchor_verse_id, not zero anchors.
    conn.execute(
        "UPDATE verse_passage SET is_anchor=1 WHERE passage_id=? AND verse_id=? AND deleted=0",
        (OLD_PASSAGE_ID, v8))

    conn.commit()

    row = conn.execute("SELECT ref, start_verse, verse_count, anchor_verse_id, debate_path "
                       "FROM passage WHERE id=?", (OLD_PASSAGE_ID,)).fetchone()
    print("Dan 1:7-21 -> corrected to:", dict(row))
    print(f"Dan.1.7 verse_passage: passage {OLD_PASSAGE_ID} link soft-deleted; "
          f"passage {SIBLING_PASSAGE_ID} link restored live.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
