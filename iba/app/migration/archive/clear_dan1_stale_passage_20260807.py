"""clear_dan1_stale_passage_20260807.py — Dan 1's lexical was judged not at the right standard
(researcher, 2026-08-07); the researcher directed a full clear-and-restart for Dan 1 ahead of the
whole-corpus lexical regeneration, in their own time. `hib.set` already removed the 10 Dan-1-only
HIBs and narrowed the shared "Daniel" HIB back to its Dan 8 verses only (see
`SESSION-LOG-20260807-dan1-clear-for-lexical-redo.md`).

Passage 37466 (Dan 1:1-21) itself has no downstream content (0 phenomena, 0 operations, 0 closing
rows -- debate_status was already NULL/"empty") and now has zero live HIB coverage after the
hib.set clear above. Rather than leave a stale, HIB-less passage row sitting live, this soft-deletes
it the exact same way `handlers/passage.py:build()` already soft-deletes a same-scope passage when
one is resubmitted (UPDATE ... SET deleted=1 on `passage` + its `verse_passage` rows) -- so a future
`passage.build` for the identical Dan 1:1-21 scope, once the new lexical + HIBs exist, registers
clean rather than tripping the `scope-overlaps-existing` guard against a dead row.

Direct-write, one-off. Idempotent (no-ops if the passage is already deleted).
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

PASSAGE_ID = 37466  # Dan 1:1-21


def run(conn: sqlite3.Connection) -> dict:
    row = conn.execute("SELECT deleted FROM passage WHERE id=?", (PASSAGE_ID,)).fetchone()
    if row is None or row[0] == 1:
        return {"passage_cleared": 0, "verse_passage_cleared": 0}
    vp = conn.execute(
        "UPDATE verse_passage SET deleted=1 WHERE deleted=0 AND passage_id=?", (PASSAGE_ID,))
    conn.execute("UPDATE passage SET deleted=1 WHERE id=?", (PASSAGE_ID,))
    conn.commit()
    return {"passage_cleared": 1, "verse_passage_cleared": vp.rowcount}


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    result = run(conn)
    print("migration result:", result)
    conn.close()
