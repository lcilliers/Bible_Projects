"""add_hib_centric_traversal_method_rules_20260807.py — codifies the researcher's 2026-08-07
correction that the pipeline had lost its HIB-centric focus: the schema was already HIB-capable at
every step (`phenomenon.hib_id` is a real column, the control total is genuinely HIB×verse) but
nothing written down said HIB was the actual *working order* — every step's own natural key
defaulted to verse-first phrasing, and the first real Dan 1 phenomena pass defaulted to
verse-by-verse traversal as a direct result.

Restated in full, with worked examples, in
`iba/app/reports/debate-pipeline-technical-reference-20260806.md` §2.7 (cross-cutting) and short
per-step additions to Steps 2/3/4-5 — this migration is the config-first half of that same change
(`governance.rules_must_be_config_driven`: the doc restates config, it is never the rule's only
home).

Same direct-write convention as `fix_nonhuman_scope_method_rule.py`/
`fix_hib_is_human_only_method_rule.py` (`cfg_method_rule` is not `configmaint.propose`-gated —
confirmed live 2026-08-07 when a `configmaint.propose` attempt on this table correctly refused with
a write-grant violation, same lesson escalation #539 already recorded 2026-08-06).

Idempotent: safe to re-run (checks for an existing identical row before inserting).
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

SOURCE = "researcher direction, 2026-08-07"

NEW_RULES = [
    ("passage.build", "story-organized-by-hib",
     "The story synthesis is told through the passage's own cast, not as a generic plot summary "
     "-- the dominant HIB's own arc as the spine, others introduced as they bear on it. A story "
     "that reads identically with the HIB list deleted has not done this step's job.",
     None),
    ("phenomenon.set", "hib-first-traversal",
     "Work HIB-by-HIB, not verse-by-verse: start with the passage's most dominant HIB (highest "
     "verse-count cross-checked against the story's own throughline), read every verse that HIB "
     "appears in against its own verse_lexical row (full range, not the story or the printed "
     "gloss), complete that HIB's full phenomena list, then move to the next HIB. Stay inside "
     "phenomenon-only territory throughout -- no reasoning yet about source/target or cross-HIB "
     "movement (see operation.set's hib-fanout-dimensions rule).",
     None),
    ("operation.set", "hib-fanout-dimensions",
     "Fanning out from the focused HIB to the rest of the passage's cast has three distinct "
     "dimensions: (A) another HIB as source/target within the focused HIB's own operation; (B) "
     "the mirror once focus switches to that other HIB, checked for consistency, not re-derived; "
     "(C) movement/process BETWEEN two different HIBs' already-registered phenomena/operations, "
     "which belongs to closing.set's passage_linkage (Q7), not to operation.set itself. Only (A) "
     "and (B) are this step's job.",
     None),
]


def run(conn: sqlite3.Connection) -> dict:
    counts = {"inserted": 0, "already_present": 0}
    for step, rule_key, rule_text, enforced_by in NEW_RULES:
        existing = conn.execute(
            "SELECT rule_text FROM cfg_method_rule WHERE step=? AND rule_key=?",
            (step, rule_key)).fetchone()
        if existing:
            counts["already_present"] += 1
            continue
        max_ord = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) FROM cfg_method_rule WHERE step=?", (step,)
        ).fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES (?,?,?,?,?,?,?)",
            (step, rule_key, rule_text, SOURCE, enforced_by, max_ord + 1, 1))
        counts["inserted"] += 1
    conn.commit()
    return counts


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    result = run(conn)
    print("migration result:", result)
    conn.close()
