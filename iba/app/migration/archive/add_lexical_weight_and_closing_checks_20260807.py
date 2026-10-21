"""add_lexical_weight_and_closing_checks_20260807.py — two separate researcher directives, same
session, closed together since both extend method-rule/quality-check config the same way.

**1. Full lexical weight in descriptions (`phenomenon.set`/`operation.set`).** Researcher, verbatim:
"when the descriptions of the operations of the phenomena is done, that the full value of the
lexical weight of the words are included, and not just a brief generic description... this is
where the actual meaning of the phenomena in all its glory resides and must not be compromised by
stereotyped namings. it must be context specific." Extends T2's existing discipline ("pull the full
lexical range before assigning a sense", `WA-verse-reading-technique-v4`) from SENSE-SELECTION to
DESCRIPTION-WRITING specifically — the same full-range read must show up in the prose, not just
inform a silent judgement call behind a generic label.

**2. `closing.set` quality checks — "should not be deferred for another day."** The previous same-
day pass added `closing.set`'s method-rule CONTENT but explicitly deferred its quality-check gate
to "the researcher's own planned Step 6/7 review." Researcher's direct instruction supersedes that
deferral: build it now. `handlers/operations.py:closing_set` is changed in the same commit as this
migration to actually call `_check_quality_attestations` (it never did before — a real code gap,
not just a missing config row; the four rows below would have been silently unenforced without it).

Same direct-write convention as every other `cfg_method_rule`/`cfg_quality_check` migration in this
tree. Idempotent.
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

SOURCE = "researcher direction, 2026-08-07"

METHOD_RULES = [
    ("phenomenon.set", "full-lexical-weight-in-description",
     "A phenomenon's description must draw on the word's actual full lexical range (the whole "
     "meaning_tree entry for its governing Strong's code, per T2) -- not a brief, generic, or "
     "stereotyped label. The specific sense operative in THIS context, in its own fullness, is "
     "where the phenomenon's real content resides; flattening it into a stock gloss compromises "
     "that content. Context-specific, every time -- never a reusable stock phrase.",
     None),
    ("operation.set", "full-lexical-weight-in-observation",
     "The same discipline as phenomenon.set's full-lexical-weight-in-description rule, applied to "
     "an operation's observation_text/description_text: draw on the governing word's full lexical "
     "range, in this exact context, not a brief generic label. Distinct from action_type (a short "
     "label, deliberately -- action-type-is-a-label) -- observation/description text is where the "
     "full weight belongs.",
     None),
]

QUALITY_CHECKS = [
    ("phenomenon.set", "description-uses-full-lexical-range",
     "Does this description draw on the governing word's full lexical range and its specific "
     "contextual sense here -- not a brief, generic, or stereotyped label that could apply to any "
     "similar-sounding phenomenon regardless of context?",
     "reasonableness"),
    ("operation.set", "observation-uses-full-lexical-range",
     "Does observation_text/description_text draw on the governing word's full lexical range and "
     "its specific contextual sense here -- not a brief, generic, or stereotyped label?",
     "reasonableness"),
    ("closing.set", "linkage-genuinely-registered",
     "Do both the from/to sides of this linkage reference already-registered phenomena/operations "
     "-- not licence to narrate a pattern across the whole passage as if it were a linkage?",
     "existence"),
    ("closing.set", "insufficiency-genuinely-absent",
     "Is this data genuinely absent from the base extract/lexical, not substituted from "
     "remembered or external knowledge?",
     "non_existence"),
    ("closing.set", "emergent-question-not-resolvable-now",
     "Is this a genuine interpretive fork or literary/structural observation that could not be "
     "resolved within the phenomena/operations themselves -- not something that should have been "
     "settled there directly?",
     "reasonableness"),
    ("closing.set", "validation-finding-corrected-not-just-logged",
     "If this finding identifies a real failure in an existing phenomenon/operation, has it "
     "actually been corrected (corrected=true, and the correction submitted) rather than merely "
     "logged for later?",
     "existence"),
]


def run(conn: sqlite3.Connection) -> dict:
    counts = {"method_rules_inserted": 0, "quality_checks_inserted": 0}

    for step, rule_key, rule_text, enforced_by in METHOD_RULES:
        existing = conn.execute(
            "SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?", (step, rule_key)).fetchone()
        if existing:
            continue
        max_ord = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) FROM cfg_method_rule WHERE step=?", (step,)
        ).fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES (?,?,?,?,?,?,?)",
            (step, rule_key, rule_text, SOURCE, enforced_by, max_ord + 1, 1))
        counts["method_rules_inserted"] += 1

    for step, check_key, question, test_kind in QUALITY_CHECKS:
        existing = conn.execute(
            "SELECT 1 FROM cfg_quality_check WHERE step=? AND check_key=?", (step, check_key)
        ).fetchone()
        if existing:
            continue
        max_ord = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) FROM cfg_quality_check WHERE step=?", (step,)
        ).fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_quality_check (step, check_key, question, test_kind, required, "
            "enforced_by, ordinal, active) VALUES (?,?,?,?,?,?,?,?)",
            (step, check_key, question, test_kind, 1, None, max_ord + 1, 1))
        counts["quality_checks_inserted"] += 1

    conn.commit()
    return counts


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    result = run(conn)
    print("migration result:", result)
    conn.close()
