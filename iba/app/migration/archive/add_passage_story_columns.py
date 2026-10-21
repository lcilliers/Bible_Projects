"""add_passage_story_columns.py — ONE-OFF, idempotent: adds `passage.story_summary` and
`passage.feasibility_note`, the two new fields Step 2's redefinition needs.

**Trigger.** Researcher, 2026-08-06, reviewing the HIB-distribution visualization across four
chapters: passaging is about reading capacity, not narrative structure. New rule — a passage is
set to the debate's own input scope (book + chapters/range), not derived by an algorithm; Step 2's
real job becomes reading the whole scope in light of the identified HIBs, synthesising a
high-level story, and self-assessing whether the scope can be read as a whole without quality
loss. If not, the debate is skipped with a message to narrow the scope, not silently sub-divided.

**Why a direct migration.** New columns are DDL. Same carve-out class as every other schema change
this session — this specific researcher exchange (methodology decided in this conversation, not a
separate reviewed design doc) is the up-front direction, the same standard `cfg_method_rule`/
`cfg_quality_check` used a round earlier today.

**What this retires.** `passage.build`'s old HIB-continuity run-forming algorithm (adjacency +
shared-HIB run detection) is retired in the same pass this migration supports — `passage.
min_shared_hibs`/`passage.cross_chapter`/`passage.review_over` become dead settings, deactivated
via `configmaint.propose` alongside this (ordinary data changes, not DDL, done separately). The
`needs_review` column stays (still meaningful — a long input scope can still be flagged), but its
threshold-based auto-computation goes away; it becomes analyst-set going forward if kept at all —
see BUILD.md for the final call.

    python -m iba.app.migration.add_passage_story_columns
"""
from __future__ import annotations

import sqlite3

DB_PATH = "iba/app/db/iba.db"

COLUMNS = [
    ("story_summary", "TEXT",
     "Step 2's high-level story synthesis for this passage's scope, read in light of the "
     "identified HIBs -- the researcher's own 2026-08-06 redefinition of what Step 2 actually "
     "produces. Written once per passage registration, updated only via reconciliation."),
    ("feasibility_note", "TEXT",
     "Step 2's own self-assessment record: why this scope was judged readable as a whole without "
     "quality loss (or, if the call was refused, why not -- though a refused call writes no "
     "passage row at all, so a live row's feasibility_note is always the 'yes, and here's why' "
     "case)."),
]


def _column_exists(conn: sqlite3.Connection, table: str, col: str) -> bool:
    return any(r[1] == col for r in conn.execute(f"PRAGMA table_info({table})").fetchall())


def run(conn: sqlite3.Connection) -> None:
    added = []
    for name, coltype, _ in COLUMNS:
        if not _column_exists(conn, "passage", name):
            conn.execute(f"ALTER TABLE passage ADD COLUMN {name} {coltype}")
            added.append(name)

    for name, _, expectation in COLUMNS:
        already = conn.execute(
            "SELECT 1 FROM cfg_column WHERE table_name='passage' AND name=?", (name,)).fetchone()
        if not already:
            conn.execute(
                "INSERT INTO cfg_column (table_name, name, ordinal, type, is_pk, \"notnull\", "
                "is_unique, dflt, fk, use, expectation, source, filled_by) VALUES "
                "('passage', ?, NULL, 'TEXT', 0, 0, 0, NULL, NULL, ?, NULL, NULL, 'passage.build')",
                (name, expectation))

    conn.commit()
    print(f"columns added this run: {added or '(none)'}")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    run(conn)
    conn.close()
