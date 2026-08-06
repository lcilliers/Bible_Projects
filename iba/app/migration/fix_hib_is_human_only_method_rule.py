"""fix_hib_is_human_only_method_rule.py — supersedes the 2026-08-06 non-human-scope wording (which
still allowed a non-human being, e.g. an angel, to be registered as its own HIB when related to a
human) with the researcher's own, more fundamental correction, same day: **HIB = Human Inner Being.
By definition a non-human cannot be a HIB, full stop** — not "in scope conditionally," not at all.
A non-human being (an animal in a symbolic vision, an angel, a voice/physical medium) can only ever
appear as a `source`/`target`/related-object party WITHIN a human HIB's own operation
(`operation_party.kind='non_human'`) — never as its own `hib` row. Where a vision depicts a human
king/kingdom in animal/symbolic form and the text itself later resolves it (e.g. Dan 8:20-23), the
HIB is the resolved HUMAN referent, registered from its first (symbolic) appearance, not the animal
image. Also clarifies (researcher, verbatim): "a HIB can be a part of the operation of another HIB"
— `operation_party.kind='human'` with `detail` naming the other HIB is how one human HIB acting on
another is recorded; no new column needed, `kind='human'` already existed for exactly this.

Same direct-write convention as `fix_nonhuman_scope_method_rule.py` (`cfg_method_rule` is not
`configmaint.propose`-gated). Supersedes that earlier fix's wording rather than compounding it.
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

NEW_NON_HUMAN_SCOPE = (
    "HIB = Human Inner Being. A non-human being can NEVER itself be registered as a HIB, by "
    "definition -- not conditionally, not when related to a human. A non-human being (an animal in a "
    "symbolic vision, an angel, a voice or other physical medium) may only appear as a "
    "source/target/related-object PARTY within a human HIB's own operation "
    "(operation_party.kind='non_human') -- never as its own hib row, phenomenon, or operation. Where "
    "a vision depicts a human king/kingdom in animal or symbolic form and the text itself resolves "
    "that image (e.g. Dan 8:20-23), the HIB is the resolved HUMAN referent, registered from its "
    "first (symbolic) appearance onward -- not the animal/image itself as a separate entity. "
    "Superseded 2026-08-06 (same day as the first wording): the original text still allowed a "
    "non-human being 'in scope' as its own HIB when related to a human (e.g. an angel) -- corrected "
    "directly by the researcher: 'a non human by definition cannot be a HIB.'"
)

NEW_HIB_PART_OF_ANOTHER_HIBS_OPERATION = (
    "A HIB can be a party within another HIB's own operation (e.g. a king acting against Daniel) -- "
    "operation_party.kind='human' with detail naming the other HIB is how this is recorded; no "
    "separate mechanism or schema change is needed, kind='human' already covers it. This is distinct "
    "from a non-human party (kind='non_human'), which never gets its own hib/phenomenon/operation "
    "rows at all (see non-human-scope)."
)


def run(conn: sqlite3.Connection) -> dict:
    counts = {"non_human_scope_updated": 0, "hib_part_of_another_inserted": 0}

    row = conn.execute(
        "SELECT rule_text FROM cfg_method_rule WHERE step='hib.set' AND rule_key='non-human-scope'"
    ).fetchone()
    if row and row[0] != NEW_NON_HUMAN_SCOPE:
        conn.execute(
            "UPDATE cfg_method_rule SET rule_text=? WHERE step='hib.set' AND rule_key='non-human-scope'",
            (NEW_NON_HUMAN_SCOPE,))
        counts["non_human_scope_updated"] = 1

    # the earlier same-day 'not-a-feature-or-medium' rule is now fully subsumed by the rewritten
    # non-human-scope above (features/media are just one case of "non-human, therefore never a HIB")
    # -- deactivate rather than delete, so the record of the intermediate correction stays auditable.
    conn.execute(
        "UPDATE cfg_method_rule SET active=0 WHERE step='hib.set' AND rule_key='not-a-feature-or-medium' "
        "AND active=1")

    exists = conn.execute(
        "SELECT 1 FROM cfg_method_rule WHERE step='operation.set' "
        "AND rule_key='hib-can-be-party-in-another-hibs-operation'").fetchone()
    if not exists:
        max_ord = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) FROM cfg_method_rule WHERE step='operation.set'").fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
            "ordinal, active) VALUES (?,?,?,?,?,?,?)",
            ("operation.set", "hib-can-be-party-in-another-hibs-operation",
             NEW_HIB_PART_OF_ANOTHER_HIBS_OPERATION,
             "researcher direct correction, same session as dan8-debate-run-failure-review-20260806.md",
             "schema: operation_party.kind='human'", max_ord + 1, 1))
        counts["hib_part_of_another_inserted"] = 1

    conn.commit()
    return counts


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    result = run(conn)
    print("fix result:", result)
    conn.close()
