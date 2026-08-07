"""rehome_multi_chapter_vigilance_rule_20260807.py — `multi-chapter-vigilance` was filed under
`phenomenon.set` with its own text admitting it doesn't belong there ("Belongs to Phase 3/Step 7,
not Step 3 itself... correctly homed once Step 7's own cfg_method_rule rows are built") — found
doing the researcher-requested full audit of every rule's step-linkage, 2026-08-07, now that
`closing.set` (Step 6/Phase 3) actually has rows to move it to.

Moves it to `closing.set`, alongside `debate-quality-validation` (the same Phase 3 pass this rule
refines with a specific thing to watch for), and drops the now-stale parenthetical.

Direct-write convention. Idempotent (checks current step before moving).
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

NEW_TEXT = (
    "Where a debate document spans multiple chapters, Phase 3 validation should pay particular "
    "attention to phenomena/justifications that read as though they are describing the passage's "
    "own literary architecture rather than a specific inner being's own state -- this is the exact "
    "failure mode phase-separation (phenomenon.set) exists to prevent, and this validation pass is "
    "the last check that it did not recur."
)


def run(conn: sqlite3.Connection) -> dict:
    row = conn.execute(
        "SELECT step FROM cfg_method_rule WHERE rule_key='multi-chapter-vigilance'").fetchone()
    if row is None or row[0] == "closing.set":
        return {"moved": 0}
    max_ord = conn.execute(
        "SELECT COALESCE(MAX(ordinal), -1) FROM cfg_method_rule WHERE step='closing.set'"
    ).fetchone()[0]
    conn.execute(
        "UPDATE cfg_method_rule SET step='closing.set', ordinal=?, rule_text=? "
        "WHERE rule_key='multi-chapter-vigilance'", (max_ord + 1, NEW_TEXT))
    conn.commit()
    return {"moved": 1}


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    result = run(conn)
    print("migration result:", result)
    conn.close()
