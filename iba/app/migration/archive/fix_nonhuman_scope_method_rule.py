"""fix_nonhuman_scope_method_rule.py — corrects `cfg_method_rule` per the researcher's direct
2026-08-06 critique of the first real Dan 8 debate run: `non-human-scope` as originally worded let
a horn (a feature of the goat) and a voice (the medium of a command) get registered as their own
HIBs. `cfg_method_rule` is not `configmaint.propose`-gated (BUILD.md §66: "brand-new tables, seeded
directly by their own migrations, same convention cfg_enum's own historical seed rows used") -- this
migration is that same direct-write convention, not a new carve-out. Direct researcher instruction
(the critique itself, verbatim) is the up-front authorization.

Does NOT touch the separate, still-open ram/goat question (symbolic vision-image vs genuine
non-human being) -- raised to the researcher directly, not decided here.

Idempotent: checks current content before writing either row.
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

NEW_NON_HUMAN_SCOPE = (
    "A non-human being is in scope only where its state/characteristics bear directly on a human "
    "in the same context -- otherwise the verse is set aside entirely. A non-human being here means "
    "a genuine, addressable party in its own right (e.g. an angel) -- not a body part or feature of "
    "one (e.g. a horn), and not the medium through which an act is delivered (e.g. a voice); see "
    "not-a-feature-or-medium."
)

NOT_A_FEATURE_OR_MEDIUM = (
    "A body part or feature of a being (e.g. a horn) is not itself a HIB -- its content belongs to "
    "the being it is a feature of, or, once the vision resolves it, to the human referent it comes "
    "to represent. The medium through which an act is delivered (e.g. a voice) is likewise not a "
    "HIB in its own right -- record what it does as part of an operation (source/process), not as a "
    "separate registered party. Found live 2026-08-06: the goat's great horn / the four horns / the "
    "little horn were each wrongly registered as their own HIB, and 'the man's voice' was wrongly "
    "registered as a HIB rather than treated as the medium of Dan 8:16's command."
)


def run(conn: sqlite3.Connection) -> dict:
    counts = {"non_human_scope_updated": 0, "not_a_feature_or_medium_inserted": 0}

    row = conn.execute(
        "SELECT rule_text FROM cfg_method_rule WHERE step='hib.set' AND rule_key='non-human-scope'"
    ).fetchone()
    if row and row[0] != NEW_NON_HUMAN_SCOPE:
        conn.execute(
            "UPDATE cfg_method_rule SET rule_text=? WHERE step='hib.set' AND rule_key='non-human-scope'",
            (NEW_NON_HUMAN_SCOPE,))
        counts["non_human_scope_updated"] = 1

    exists = conn.execute(
        "SELECT 1 FROM cfg_method_rule WHERE step='hib.set' AND rule_key='not-a-feature-or-medium'"
    ).fetchone()
    if not exists:
        max_ord = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) FROM cfg_method_rule WHERE step='hib.set'").fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES (?,?,?,?,?,?,?)",
            ("hib.set", "not-a-feature-or-medium", NOT_A_FEATURE_OR_MEDIUM,
             "researcher direct correction, dan8-debate-run-failure-review-20260806.md", None,
             max_ord + 1, 1))
        counts["not_a_feature_or_medium_inserted"] = 1

    conn.commit()
    return counts


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    result = run(conn)
    print("fix result:", result)
    conn.close()
