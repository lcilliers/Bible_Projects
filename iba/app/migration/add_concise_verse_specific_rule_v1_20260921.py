"""add_concise_verse_specific_rule_v1_20260921.py — ONE-OFF migration, escalation #1824,
researcher instruction verbatim: "LLM output was not generic nonsense, and not concide and
specific to the verse, so it was impossible to make any differentiation visible."

Root cause of Finding 16's 0/378 dedup-merge failure: `obs_text` is generic, free-form prose that
varies in sentence structure every time, even when restating the same underlying fact -- the
same/broaden/new similarity check (`recordingpass.py`, character-level `difflib`) can never
recognise two independently-phrased paraphrases of the same fact as the same observation. This is
not an architecture defect -- the LLM already correctly never decides new-vs-existing itself
(`recordingpass.py`'s own #1693 design) -- it is a missing output-format requirement.

Fix: one new `cfg_method_rule`, registered for every stage that writes through `recordingpass.py`
(`lexical.meaning`/Stage 1, `cluster.reading`/Stage 3, `cluster.answer`/Stage 4) -- require
`obs_text` to be concise and tied to the specific verse/occurrence's own content, not a free-
standing restatement of a general/dictionary sense. This does not change the similarity algorithm
-- it changes what the algorithm is asked to compare, so genuinely-same findings converge in text
and genuinely-different findings correctly diverge.

Idempotent (checks for an existing live row with the same rule_key+step before inserting).

    python -m iba.app.migration.add_concise_verse_specific_rule_v1_20260921
"""
from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_RULE_KEY = "concise-and-verse-specific-obs-text"
_RULE_TEXT = (
    "obs_text must be concise and tied to THIS specific verse/occurrence's own content -- state "
    "the finding directly, grounded in what this verse actually shows, not a free-standing "
    "restatement of the word's general/dictionary sense in your own varying prose. Two "
    "occurrences that genuinely show the same finding should produce recognisably similar, "
    "terse text (so the same/broaden/new duplicate check can actually recognise them as the "
    "same observation); padding, scene-setting, or restating background already given elsewhere "
    "in the payload adds nothing and actively defeats that check. Escalation #1824, 2026-09-21: "
    "confirmed live that generic, variably-worded obs_text caused the duplicate-detection "
    "mechanism to never once recognise two answers to the same question about the same strong as "
    "the same finding (0 of 378 real pairwise comparisons ever matched), even when they were "
    "restating the identical underlying fact.")

_STEPS = ("lexical.meaning", "cluster.reading", "cluster.answer")


def apply_rule(conn: sqlite3.Connection) -> list[str]:
    report = []
    for step in _STEPS:
        existing = conn.execute(
            "SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=? AND active=1",
            (step, _RULE_KEY)).fetchone()
        if existing:
            report.append(f"{step}: rule already live -- no-op")
            continue
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, active, ordinal) "
            "VALUES (?,?,?,1,0)",
            (step, _RULE_KEY, _RULE_TEXT))
        report.append(f"{step}: rule registered")
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = apply_rule(conn)
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
