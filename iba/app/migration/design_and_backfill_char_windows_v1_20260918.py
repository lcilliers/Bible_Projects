"""Designs and applies the missing `window` categorisation for the char-level (D1-D12/F0/X0)
catalogue dimensions, per researcher instruction 2026-09-18: *"the object of the window on
observations is to show from which angle we are observing the data to make the observation...
the 4 windows already in place came out the lexical read phase, and we have not yet designed the
windows for the char observations... derive the windows for the questions from the component_
title, but name them such to align the objective of the window column."*

**Design method**: read every active leaf question's own `component_title` + `question_text`
(99 rows total, all read in full before deciding -- not skimmed), grouped by what analytical ANGLE
each is actually looking through, not mechanically 1:1 per `component_code` (the existing `meaning`
window already spans 2 different components -- M0.1 and M0.5 -- because both share the same
lexical-identity angle; the new windows below follow that same principle). Result: 8 new angles
alongside the 3 that already exist from the lexical-read phase (`meaning`/`action-impact`/
`relational`), 11 total:

- `meaning` (EXISTING) -- the term's own lexical/definitional identity. Extended here to also
  cover M0.2 (Kind)/M0.3 (Boundary)/M0.4 (Grammatical Form) -- all, like M0.1/M0.5, about what the
  term itself fundamentally IS, not its use in a verse or its relation to anything else.
- `literary` (NEW) -- M0.6.1-4: the verse's own literary/rhetorical structure and anchor-verse
  determination. Kept separate from M0.6.5 (`relational`, already assigned) -- a real, different
  angle under the same component_title (verse-structure vs. cross-characteristic role), not
  collapsed into one just because the title matches.
- `relational` (EXISTING) -- extended to cover every question whose real angle is "how does this
  characteristic relate to another PARTY" -- another characteristic (M0.6.5, X0.1-X0.5), a human
  (D4.1), God (D5.1-D5.3, D7.1, D7.6), another person giving/receiving (D7.2, D7.3), or a spirit
  being (D7.4). All of these ask the same underlying question -- what's on the other end of the
  relation -- just with a different party each time.
- `action-impact` (EXISTING) -- extended to cover D10.1-D10.6 alongside D7.7: both are fundamentally
  "what does the characteristic DO / produce" (D7.7's own narrow operation-word-plus-party case,
  D10's broader purpose/response/effect/transformation/mechanism-of-change case) -- same angle,
  different grain, not two separate windows.
- `cognitive` (NEW) -- D1.1: perception, belief, judgement -- the angle of what the person
  KNOWS/BELIEVES in connection with the characteristic.
- `affective` (NEW) -- D2.1: the FELT quality -- settled vs. transient, consistent vs. variable.
- `operational` (NEW) -- D3.1/D3.2: the mechanical HOW -- modes of operation, conditions under
  which it takes hold or is blocked.
- `constitutional` (NEW) -- D6.1/D6.2/D6.3: WHERE in the human constitution (spirit/soul/body) the
  characteristic locates and moves.
- `origin` (NEW) -- D7.5 (Origin and Source) + D11.1/D11.2 (Created Design vs. Fallen Condition,
  Innate Endowment): where the characteristic comes from / its created-vs-fallen nature -- a
  genuinely different angle from `relational` (this asks about GENESIS, not an ongoing relation).
- `scientific` (NEW) -- D9.1/D9.2/D12.1: the empirical/scientific-literature angle (all three
  questions are explicitly "per the cluster's science extract").
- `faculty` (NEW) -- F0.1: which human faculties (mind/will/emotion/body) are engaged.

Applies in 3 steps: (1) UPDATE `wa_obs_question_catalogue.window` for every active row currently
NULL, per the mapping below; (2) register the 8 new `cfg_enum` values for `ib_observation.window`;
(3) backfill `ib_observation.window` for every existing row that has a `question_code` (re-derives
from the now-updated catalogue, same `_window_for` logic `recordingpass.py` already uses at write
time -- never invented ad hoc, per that column's own `cfg_column.use` text).

Safe to re-run: idempotent (only touches rows currently NULL / not yet registered).

Usage:
    python iba/app/migration/design_and_backfill_char_windows_v1_20260918.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

# component_code -> window. Only components currently NULL need an entry; already-assigned ones
# (M0.1, M0.5, D7.7) are left alone by the UPDATE's own WHERE window IS NULL clause.
COMPONENT_WINDOW = {
    "M0.2": "meaning", "M0.3": "meaning", "M0.4": "meaning",
    "D1.1": "cognitive",
    "D2.1": "affective",
    "D3.1": "operational", "D3.2": "operational",
    "D4.1": "relational",
    "D5.1": "relational", "D5.2": "relational", "D5.3": "relational",
    "D6.1": "constitutional", "D6.2": "constitutional", "D6.3": "constitutional",
    "D7.1": "relational", "D7.2": "relational", "D7.3": "relational", "D7.4": "relational",
    "D7.5": "origin", "D7.6": "relational",
    "D9.1": "scientific", "D9.2": "scientific",
    "D10.1": "action-impact", "D10.2": "action-impact", "D10.3": "action-impact",
    "D10.4": "action-impact", "D10.5": "action-impact", "D10.6": "action-impact",
    "D11.1": "origin", "D11.2": "origin",
    "D12.1": "scientific",
    "F0.1": "faculty",
    "X0.1": "relational", "X0.2": "relational", "X0.3": "relational", "X0.4": "relational",
    "X0.5": "relational",
}

NEW_ENUM_VALUES = ["literary", "cognitive", "affective", "operational", "constitutional",
                  "origin", "scientific", "faculty"]

# M0.6 is a real split within one component_code -- M0.6.5 already got `relational` at write time
# (a different angle: cross-characteristic role, not verse-literary-structure); M0.6.1-4 need
# `literary` specifically, by question_code, not by component_code like everything else above.
M06_LITERARY_CODES = ("M0.6.1", "M0.6.2", "M0.6.3", "M0.6.4")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    # Step 1 preview: catalogue rows to update
    cat_updates = []
    for code, window in COMPONENT_WINDOW.items():
        rows = conn.execute(
            "SELECT question_code FROM wa_obs_question_catalogue WHERE component_code=? "
            "AND deleted=0 AND status='active' AND window IS NULL", (code,)).fetchall()
        cat_updates += [(window, r["question_code"]) for r in rows]
    for qc in M06_LITERARY_CODES:
        row = conn.execute(
            "SELECT question_code FROM wa_obs_question_catalogue WHERE question_code=? "
            "AND deleted=0 AND status='active' AND window IS NULL", (qc,)).fetchone()
        if row:
            cat_updates.append(("literary", row["question_code"]))

    # Step 2 preview: new enum values
    enum_inserts = []
    max_ordinal = conn.execute(
        "SELECT COALESCE(MAX(ordinal), 0) m FROM cfg_enum WHERE name='ib_observation.window'"
    ).fetchone()["m"]
    for i, val in enumerate(NEW_ENUM_VALUES, start=1):
        if not conn.execute(
                "SELECT 1 FROM cfg_enum WHERE name='ib_observation.window' AND value=?",
                (val,)).fetchone():
            enum_inserts.append((val, max_ordinal + i))

    print(f"Step 1: {len(cat_updates)} catalogue question(s) to assign a window.")
    print(f"Step 2: {len(enum_inserts)} new cfg_enum value(s): {[v for v, _ in enum_inserts]}")

    if args.dry_run:
        print("--dry-run: catalogue/enum changes not applied, backfill not run.")
        conn.close()
        return 0

    conn.executemany(
        "UPDATE wa_obs_question_catalogue SET window=? WHERE question_code=?", cat_updates)
    conn.executemany(
        "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES "
        "('ib_observation.window', ?, ?, 0)", enum_inserts)
    conn.commit()
    print(f"Applied: {len(cat_updates)} catalogue row(s), {len(enum_inserts)} enum value(s).")

    # Step 3: backfill ib_observation.window from the now-updated catalogue, same logic
    # recordingpass._window_for uses at write time.
    obs_rows = conn.execute(
        "SELECT id, question_code FROM ib_observation WHERE question_code IS NOT NULL "
        "AND window IS NULL").fetchall()
    obs_updates = []
    unresolved = []
    for r in obs_rows:
        cat = conn.execute(
            "SELECT window FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
            (r["question_code"],)).fetchone()
        if cat and cat["window"]:
            obs_updates.append((cat["window"], r["id"]))
        else:
            unresolved.append((r["id"], r["question_code"]))

    print(f"Step 3: {len(obs_rows)} ib_observation row(s) eligible, {len(obs_updates)} resolved, "
         f"{len(unresolved)} unresolved: {unresolved}")
    conn.executemany("UPDATE ib_observation SET window=? WHERE id=?", obs_updates)
    conn.commit()
    print(f"Backfilled {len(obs_updates)} ib_observation row(s).")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
