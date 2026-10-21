"""complete_method_config_20260807.py — closes three separate config gaps found while responding to
the researcher's direct instruction (2026-08-07): "ensure that the config rules are in place for
all the observations and changes in this session, and that it is not left undone."

Same direct-write convention as every other `cfg_method_rule`/`cfg_quality_check` migration in this
tree (`configmaint.propose` has no write-grant for either table by design — confirmed live twice
this session, escalation #539 and again here). Idempotent: checks for an existing row before
inserting/updating.

**Gap 1 — `passage.build`'s own documented method rules were never written to the DB.**
`debate-pipeline-technical-reference-20260806.md`'s Step 2 table has always listed 5 rules
(`input-scope-is-the-passage`, `story-synthesis-required`, `feasibility-self-assessment`,
`one-passage-per-verse`, `legacy-superseded-unconditionally`) — found live 2026-08-07 (while
correcting that same document's row-count summary for an unrelated reason) that `cfg_method_rule`
only ever had 0 of them; the document was never wrong about their CONTENT, only about whether they
existed as config at all. Backfilled verbatim from the doc's own already-cited wording.

**Gap 2 — `closing.set` (Step 7) has zero `cfg_method_rule`/`cfg_quality_check` rows.** Its content
(Q7 linkages, insufficiencies register, emergent questions log, debate quality validation, open
decisions) has existed only in `WA-interpretation-questions-v1.4` Part A/B/C prose since 2026-08-02
— cited here directly, not paraphrased from BUILD.md or the digest.

**Gap 3 — the phenomenon.set -> hib.set correction direction was never codified, only its mirror.**
`operation.set` already has both a rule (`operation-from-phenomenon-only`) and a required, enforced
quality-check attestation (`phenomenon-actually-underlies-it`) for "writing this operation revealed
the underlying phenomenon needs correcting -- go fix phenomenon.set." The researcher's own
2026-08-07 examples named the SAME discipline one level up ("the phenomena step discovers that the
HIB has no inner being role or effect... the HIB must be removed") -- phenomenon.set never had the
equivalent rule+check for correcting hib.set. Added as `hib-still-warranted` on both tables,
deliberately NOT contradicting `silence-is-a-finding` (a silent phenomenon is a valid, legitimate
finding on its own -- this rule is about a HIB that, on full review across the whole passage, was
never a genuine candidate at all, not about any HIB with some/all-silent entries being suspect by
default).
"""
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "iba" / "app" / "db" / "iba.db"

DOC_20260806 = "debate-pipeline-technical-reference-20260806.md Step 2 table, 2026-08-06 (verbatim, never before written to cfg_method_rule)"
DOC_V14 = "WA-interpretation-questions-v1.4-2026-08-02.md"
SOURCE_20260807 = "researcher direction, 2026-08-07"

PASSAGE_BUILD_RULES = [
    ("input-scope-is-the-passage",
     "A passage is the debate's own input scope, registered verbatim -- never sub-divided by algorithm.",
     "researcher direction, 2026-08-06, following the HIB-distribution visualization", "passage.py:build"),
    ("story-synthesis-required",
     "Step 2's real output is a high-level story synthesis for the scope, read in light of the "
     "identified HIBs -- not a derived boundary.",
     "researcher direction, 2026-08-06", "schema: passage.story_summary"),
    ("feasibility-self-assessment",
     "Before registering a passage, self-assess whether the scope can be read as a whole without "
     "quality loss; if not, the debate is skipped with a message to revise the input scope, not "
     "silently sub-divided.",
     "researcher direction, 2026-08-06", "passage.py:build (scope-too-complex refusal)"),
    ("one-passage-per-verse",
     "A verse belongs to at most one live passage at a time.",
     "app convention (DB-enforced: verse_passage.verse_id unique)",
     "schema: verse_passage unique constraint + passage.py:build's overlap check"),
    ("legacy-superseded-unconditionally",
     "A legacy (pre-redefinition) passage overlapping a newly-registered scope is superseded "
     "wholesale -- \"not reconciling the old with the new.\"",
     "researcher direction, 2026-08-05/06", "passage.py:build"),
]

CLOSING_SET_RULES = [
    ("linkages-q7",
     "What linkages run to other operations in the passage? Where a linkage is absent, surface "
     "the absence; do not pass over it silently. A Q7 linkage connects two specific, "
     "already-registered phenomena/operations to each other -- it is not licence to narrate a "
     "pattern across a whole chapter range.",
     f"{DOC_V14} Part A Q7 / Part B.12 / Part C item 4", "schema: passage_linkage"),
    ("insufficiencies-register",
     "Where required data (e.g. name etymologies) is absent from the base extract, name it as an "
     "insufficiency; do not substitute remembered or external knowledge.",
     f"{DOC_V14} Part B.7 / Part C item 5", "schema: passage_insufficiency"),
    ("emergent-questions-log",
     "Interpretive forks and genuine literary/structural observations are carried forward here, "
     "named where they bite, weighed against each new data point as the corpus grows, and "
     "answered -- or left open -- by what the accumulating evidence actually shows, not settled "
     "in the abstract before the evidence is in. Not merged with other passages' logs.",
     f"{DOC_V14} Part A Q10 / Part B.8-B.9 / Part C item 6", "schema: passage_emergent_question"),
    ("debate-quality-validation",
     "Once the phenomena register and operations are assembled: a re-examination, for each "
     "phenomenon or a representative sample spanning the range, of whether it is genuinely an "
     "inner-being phenomenon (not a textual/structural pattern mislabeled as one), whether its "
     "Phase 1 justification actually warrants it, and whether its Phase 2 operation tracks "
     "faithfully back to it. CORRECT ANY FAILURE FOUND before the debate is considered filled, "
     "rather than only noting it for later.",
     f"{DOC_V14} Part C item 7", "schema: passage_validation_note (corrected flag)"),
    ("open-decisions",
     "Next steps / open decisions the passage's own analysis surfaces, recorded as a single "
     "evolving summary field, not a repeating structured list.",
     f"{DOC_V14} Part C item 8", "schema: passage.open_decisions_note"),
]

# gap 3 -- phenomenon.set/hib.set direction, mirroring operation.set's existing
# operation-from-phenomenon-only rule + phenomenon-actually-underlies-it quality check.
PHENOMENON_SET_HIB_RULE = (
    "hib-still-warranted",
    "Once a HIB's phenomena list is complete across the whole passage, review whether it still "
    "genuinely warrants being a HIB at all -- if there is no inner-being role or effect anywhere, "
    "and no reasonable basis to infer one, go back and correct hib.set (remove, with reason) "
    "before treating this HIB's phenomena as final. Distinct from silence-is-a-finding: a HIB with "
    "some or all silent entries is not automatically suspect -- silence is a legitimate result. "
    "This rule is for a HIB that, on full review, was never a genuine candidate in the first place.",
    SOURCE_20260807, None,
)
PHENOMENON_SET_HIB_CHECK = (
    "hib-still-warranted",
    "Having completed this HIB's full phenomena list for the passage, does it still genuinely "
    "warrant being a HIB -- or has the review revealed hib.set needs correcting (and has that "
    "correction already been submitted)?",
    "reasonableness", 1, None,
)


def _insert_method_rule(conn, step, rule_key, rule_text, source_doc, enforced_by, counts, key):
    existing = conn.execute(
        "SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?", (step, rule_key)).fetchone()
    if existing:
        counts[key] += 0
        return
    max_ord = conn.execute(
        "SELECT COALESCE(MAX(ordinal), -1) FROM cfg_method_rule WHERE step=?", (step,)).fetchone()[0]
    conn.execute(
        "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
        "ordinal, active) VALUES (?,?,?,?,?,?,?)",
        (step, rule_key, rule_text, source_doc, enforced_by, max_ord + 1, 1))
    counts[key] += 1


def run(conn: sqlite3.Connection) -> dict:
    counts = {"passage_build_backfilled": 0, "closing_set_rules": 0,
              "phenomenon_hib_rule": 0, "phenomenon_hib_check": 0}

    for rule_key, rule_text, source_doc, enforced_by in PASSAGE_BUILD_RULES:
        _insert_method_rule(conn, "passage.build", rule_key, rule_text, source_doc, enforced_by,
                            counts, "passage_build_backfilled")

    for rule_key, rule_text, source_doc, enforced_by in CLOSING_SET_RULES:
        _insert_method_rule(conn, "closing.set", rule_key, rule_text, source_doc, enforced_by,
                            counts, "closing_set_rules")

    rk, rt, sd, eb = PHENOMENON_SET_HIB_RULE
    _insert_method_rule(conn, "phenomenon.set", rk, rt, sd, eb, counts, "phenomenon_hib_rule")

    ck, question, test_kind, required, enforced_by = PHENOMENON_SET_HIB_CHECK
    existing = conn.execute(
        "SELECT 1 FROM cfg_quality_check WHERE step='phenomenon.set' AND check_key=?", (ck,)
    ).fetchone()
    if not existing:
        max_ord = conn.execute(
            "SELECT COALESCE(MAX(ordinal), -1) FROM cfg_quality_check WHERE step='phenomenon.set'"
        ).fetchone()[0]
        conn.execute(
            "INSERT INTO cfg_quality_check (step, check_key, question, test_kind, required, "
            "enforced_by, ordinal, active) VALUES (?,?,?,?,?,?,?,?)",
            ("phenomenon.set", ck, question, test_kind, required, enforced_by, max_ord + 1, 1))
        counts["phenomenon_hib_check"] = 1

    conn.commit()
    return counts


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    result = run(conn)
    print("migration result:", result)
    conn.close()
