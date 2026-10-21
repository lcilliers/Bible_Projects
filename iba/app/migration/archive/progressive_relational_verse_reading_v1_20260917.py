"""Implements the catalogue/schema side of the progressive, relational verse-reading redesign
(escalation #1723, iba/docs/1706-progressive-relational-verse-reading-v1-20260917.md). Researcher
instruction, this chat turn: "go through the open items and work through the suggested fixes."

Six things, all from #1723's own accumulated findings:

1. **`window` redefined** -- was a 4-value pipeline-stage enum duplicating `stage` (#1691,
   2026-09-13, predates the 5-stage naming). Replaced with the researcher's own redefinition: the
   ANALYTICAL ANGLE an item is looked at from, not which stage produced it. New values: `meaning`,
   `action-impact`, `relational`. (`qualifying` deliberately NOT added yet -- #1598's qualifier
   T-code work is still deferred, item 5 below; no point adding a window value with nothing
   classified under it.)
2. **`window` made derivable, not duplicated** -- new `wa_obs_question_catalogue.window` column is
   now the authoritative source (each question implies one angle); `ib_observation.window` is
   populated FROM the question's own value at write time (recordingpass.py), never invented ad hoc.
3. **`M0.5.11` added** -- the "alternative meaning" gap (#1723, surface/stepGloss divergence from
   the base lemma, its nuance and impact in THIS context vs the word's other occurrences). Lives
   under the existing `M0.5` (Lexical and Semantic Analysis) component -- the natural home, already
   word-level-scoped.
4. **`M0.6.5` added** -- the core progressive/relational mechanism's own question: what role does
   this characteristic play in relation to the OTHER M-code characteristics present in this verse,
   building on whatever earlier cluster-passes over the same verse already found (never duplicating
   it). Lives under the existing `M0.6` (Verse and Literary Interpretation) component -- already
   verse-scoped, already partly about a term's function within the verse's own argument (`M0.6.1`),
   just not yet wired into Stage 1's active question set.
5. **Tag vocabulary corrected** -- `instance-meaning`/`cross-cluster-significance` retired
   (`inactive=1`): both were window-labels doing duty as tags, which is exactly why 95% of 203
   observations collapsed into two non-discriminating buckets (#1723's own tag-distribution
   finding). Two new tags added for the new relational question's real findings: `tightly-related`,
   `no-direct-connection`.
6. **Qualifier T-codes -- explicitly NOT touched here.** `#1598`'s own blocked design (a
   content-defined T-code boundary for state/measure/intensity words) is a large, separate
   reclassification project (hundreds of adjective/adverb candidates by its own estimate) -- folding
   it into a verse-reading reset risks a rushed, hard-to-reverse classification call. Left for its
   own pass.

Safe to re-run: idempotent (checks existence before each insert/update).

Usage:
    python iba/app/migration/progressive_relational_verse_reading_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

WINDOW_VALUES = ["meaning", "action-impact", "relational"]

QUESTION_WINDOW = {
    "M0.1.1": "meaning", "M0.1.2": "meaning", "M0.1.3": "meaning",
    "M0.5.1": "meaning", "M0.5.2": "meaning", "M0.5.3": "meaning", "M0.5.4": "meaning",
    "M0.5.5": "meaning", "M0.5.6": "meaning", "M0.5.7": "meaning", "M0.5.8": "meaning",
    "M0.5.9": "meaning", "M0.5.10": "meaning",
    "D7.7.1": "action-impact",
}

NEW_QUESTIONS = [
    {
        "question_code": "M0.5.11",
        "section": "M0", "dimension": "M0", "component_code": "M0.5",
        "component_title": "Lexical and Semantic Analysis",
        "question_text": (
            "Where this occurrence's surface form/contextual sense diverges from the base lemma's "
            "general stepGloss, what nuance is that divergence carrying in THIS context, what is "
            "its impact here, and how does it compare against the word's other occurrences? Record "
            "none if this occurrence sits squarely within the base gloss with no notable shift."),
        "scope": "Word/term (lexical)", "window": "meaning", "prompt_seq": 11,
        "data_mechanism": ("Direct LLM comparison of this occurrence's surface/context against "
                           "strong.stepGloss and the 3 meaning sources."),
        "source": "#1723, researcher instruction 2026-09-17",
    },
    {
        "question_code": "M0.6.5",
        "section": "M0", "dimension": "M0", "component_code": "M0.6",
        "component_title": "Verse and Literary Interpretation",
        "question_text": (
            "What role does this characteristic play in relation to the OTHER M-code "
            "characteristics present in this verse? Build on whatever earlier cluster-passes over "
            "this SAME verse already found (given as prior context) -- do not re-derive or "
            "duplicate their findings; the focus shifts to what THIS characteristic's own "
            "vantage point adds. Record none if no other M-code characteristic is present."),
        "scope": "The verse", "window": "relational", "prompt_seq": 5,
        "data_mechanism": ("Direct LLM reading of roles_in_verse's full M-code set, plus any prior "
                           "ib_observation rows already recorded against this verse under "
                           "question_code M0.6.5."),
        "source": "#1723, researcher instruction 2026-09-17 (the 2Cor.7.11 M67->M03->M18 chain)",
    },
]

TAGS_TO_RETIRE = ["instance-meaning", "cross-cluster-significance"]
TAGS_TO_ADD = ["tightly-related", "no-direct-connection"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    actions = []

    has_window_col = any(r["name"] == "window" for r in
                         conn.execute("PRAGMA table_info(wa_obs_question_catalogue)"))
    if not has_window_col:
        actions.append(("add column", "wa_obs_question_catalogue.window"))

    if has_window_col:
        for code, window in QUESTION_WINDOW.items():
            row = conn.execute(
                "SELECT window FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
                (code,)).fetchone()
            if row is not None and row["window"] != window:
                actions.append(("set window", f"{code} -> {window}"))
    else:
        actions.append(("set window", f"{len(QUESTION_WINDOW)} existing question(s)"))

    for q in NEW_QUESTIONS:
        exists = conn.execute(
            "SELECT 1 FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
            (q["question_code"],)).fetchone()
        if not exists:
            actions.append(("insert question", q["question_code"]))

    for v in TAGS_TO_RETIRE:
        row = conn.execute(
            "SELECT inactive FROM cfg_enum WHERE name='ib_observation.tag' AND value=?",
            (v,)).fetchone()
        if row and row["inactive"] == 0:
            actions.append(("retire tag", v))
    for v in TAGS_TO_ADD:
        exists = conn.execute(
            "SELECT 1 FROM cfg_enum WHERE name='ib_observation.tag' AND value=?", (v,)).fetchone()
        if not exists:
            actions.append(("add tag", v))

    old_window_vals = [r["value"] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.window'")]
    if sorted(old_window_vals) != sorted(WINDOW_VALUES):
        actions.append(("replace window enum", f"{old_window_vals} -> {WINDOW_VALUES}"))

    print(f"{len(actions)} pending action(s):")
    for a in actions:
        print(" -", a)

    if args.dry_run or not actions:
        print("--dry-run or nothing to do: no changes made.")
        conn.close()
        return 0

    if not has_window_col:
        conn.execute("ALTER TABLE wa_obs_question_catalogue ADD COLUMN window TEXT")
        conn.execute(
            'INSERT INTO cfg_column (database, table_name, name, ordinal, type, is_pk, "notnull", '
            "is_unique, use, source, filled_by, inactive) VALUES "
            "('iba', 'wa_obs_question_catalogue', 'window', 18, 'TEXT', 0, 0, 0, "
            "'The analytical angle this question looks through -- meaning / action-impact / "
            "relational (cfg_enum ib_observation.window). Authoritative source; ib_observation."
            "window is populated FROM this at write time, never invented ad hoc. Replaces the old "
            "#1691 4-value pipeline-stage definition, which duplicated stage.', "
            "'#1723, 2026-09-17', 'progressive_relational_verse_reading_v1_20260917.py', 0)")

    for code, window in QUESTION_WINDOW.items():
        conn.execute(
            "UPDATE wa_obs_question_catalogue SET window=? WHERE question_code=? AND deleted=0",
            (window, code))

    for q in NEW_QUESTIONS:
        exists = conn.execute(
            "SELECT 1 FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
            (q["question_code"],)).fetchone()
        if not exists:
            conn.execute(
                "INSERT INTO wa_obs_question_catalogue (question_code, section, question_text, "
                "scope, status, deleted, date_added, catalogue_version, tier, component_code, "
                "component_title, prompt_seq, source, dimension, window) VALUES "
                "(?,?,?,?,'active',0,datetime('now'),'v3-progressive-relational-20260917',NULL,"
                "?,?,?,?,?,?)",
                (q["question_code"], q["section"], q["question_text"], q["scope"],
                 q["component_code"], q["component_title"], q["prompt_seq"], q["source"],
                 q["dimension"], q["window"]))

    for v in TAGS_TO_RETIRE:
        conn.execute(
            "UPDATE cfg_enum SET inactive=1 WHERE name='ib_observation.tag' AND value=?", (v,))
    max_ord = conn.execute(
        "SELECT MAX(ordinal) m FROM cfg_enum WHERE name='ib_observation.tag'").fetchone()["m"]
    for i, v in enumerate(TAGS_TO_ADD, start=1):
        exists = conn.execute(
            "SELECT 1 FROM cfg_enum WHERE name='ib_observation.tag' AND value=?", (v,)).fetchone()
        if not exists:
            conn.execute(
                "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES "
                "('ib_observation.tag', ?, ?, 0)", (v, max_ord + i))

    conn.execute("DELETE FROM cfg_enum WHERE name='ib_observation.window'")
    for i, v in enumerate(WINDOW_VALUES, start=1):
        conn.execute(
            "INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES "
            "('ib_observation.window', ?, ?, 0)", (v, i))
    conn.execute(
        "UPDATE cfg_column SET use=? WHERE database='iba' AND table_name='ib_observation' "
        "AND name='window'",
        ("The analytical angle this row looks through -- meaning / action-impact / relational "
         "(cfg_enum ib_observation.window). Populated FROM wa_obs_question_catalogue.window at "
         "write time (recordingpass.py), never invented ad hoc. Redefined #1723, 2026-09-17 -- "
         "was a 4-value pipeline-stage enum (#1691) that duplicated `stage`.",))

    conn.commit()
    print("Applied.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
