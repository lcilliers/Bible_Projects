"""Registers `cluster.answer` (Stage 4 of #1706's cluster-reading pipeline, `char-answers`) --
process (d), per-subgroup catalogue Q&A. Design: #1682 §4A + `ib-observation-governing-rules-
checklist-v1-20260916.md` §3 (7 rules).

Battery scope deliberately narrowed (52 live questions, see `charanswergenerate.py`'s own
docstring for the full reasoning): the catalogue's 4 "answered across the family's evidence as a
whole" scopes, minus `D7.7.1` (already Stage 1's territory) and the 4 science-extract-dependent
questions (wiring not yet decided, checklist's own Stage 4 status). Rule 5
(`cross_family_or_cluster_flags`) NOT built this round -- its own tag value is still unchosen
(checklist's "still-open items" list), not this build's call to invent.

Same work package as Stages 2/3 (`cluster-reading`).

Safe to re-run: idempotent (checks existence before each insert).

Usage:
    python iba/app/migration/register_cluster_answer_step_v1_20260918.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

METHOD_RULES = [
    ("per-subgroup-answer-never-whole-cluster",
     "Always run per subgroup -- same discipline as reading, never the whole cluster in one "
     "pass. #1682 §4A / checklist §3 rule 1."),
    ("multiple-slants-not-one-distilled-answer",
     "Where a subgroup's own strongs or evidence genuinely point to different answers to the same "
     "catalogue question, every distinct slant is its own observation, all under the same "
     "question_code, each with its own evidence trail -- never flattened into one 'the "
     "characteristic means X' answer. A single slant is correct only when the evidence actually "
     "is uniform, not a default. #1682 §4A / checklist §3 rule 2."),
    ("scope-level-governs-evidence-trail",
     "A slant grounded in one specific member strong sets `strong` to that code and cites its own "
     "occurrences. A slant grounded in the subgroup as a whole leaves `strong` null on the "
     "observation but requires every occurrence to carry its own `strong` field -- an occurrence "
     "with no strong of its own cannot be resolved. #1682 §4A / checklist §3 rule 3."),
    ("adjacent-context-flagged-not-fetched-answer",
     "Where answering a question properly would need surrounding verses beyond what this "
     "subgroup's own evidence carries, flag needs_adjacent_verse_context with the reason stated "
     "explicitly in obs_text -- never fetched ad hoc mid-run. Resolution happens in a later "
     "analytic run (expected to be the synergy stage), not chased down here. #1682 §4A / "
     "checklist §0 rule 5a / §3 rule 4."),
    ("cross-family-flagging-out-of-scope-this-build",
     "Cross-family/cross-cluster relevance is explicitly OUT OF SCOPE for this stage's current "
     "build -- do not attempt it. Its own tag value is not yet chosen (checklist's own "
     "still-open-items list); inventing one here would bake a design decision into a code build "
     "rather than apply one already made. #1682 §4A / checklist §3 rule 5, deliberately deferred."),
    ("battery-scope-excludes-verse-reading-and-science-extract",
     "This stage answers the catalogue's characteristic-grain battery only (scope in "
     "Characteristic (HIB behaviour)/Characteristic relational/The HIB/Other non-human beings), "
     "excluding D7.7.1 (already Stage 1's own territory, per-verse) and every question whose text "
     "depends on the cluster's science-extract file (wiring not yet decided -- checklist's own "
     "Stage 4 status). Queried live from wa_obs_question_catalogue at call time, never hardcoded, "
     "so a catalogue change is picked up automatically. This build's own scoping, 2026-09-18."),
    ("per-question-completeness-verified-by-code",
     "Per-question completeness (did every battery question_code get answered for this subgroup) "
     "is computed by CODE after the write, via ib_node's own strong citations against this "
     "subgroup's member strongs -- never trusted from an LLM self-report, same discipline as "
     "Stage 3's per-strong traceability check. This build's own architecture, 2026-09-18."),
]

STEP = {
    "work_package": "cluster-reading",
    "ordinal": 2,
    "step": "cluster.answer",
    "handler": "iba.app.handlers.cluster:answer",
    "scope": "subgroup",
    "kind": "operations",
    "does": (
        "The char-answers stage (#1682 §4A / #1706 Phase F, process d): given one subgroup's "
        "member strongs and Stage 1/2/3's own accumulated observations, answers the catalogue's "
        "characteristic-grain question battery (52 live questions, science-extract-dependent and "
        "Stage-1-owned D7.7.1 excluded), multiple slants where the evidence genuinely differs. "
        "Writes ib_observation/ib_node via the recording pass (stage='char-answers'); per-question "
        "completeness is computed by code; advances cluster_subgroup.status from ready_for_answer "
        "to answer_complete on success."
    ),
}

WRITE_GRANTS = [("cluster.answer", "ib_observation"), ("cluster.answer", "ib_node")]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    actions = []

    if not conn.execute("SELECT 1 FROM cfg_step WHERE step=? AND work_package=?",
                        (STEP["step"], STEP["work_package"])).fetchone():
        actions.append(("insert cfg_step", STEP["step"]))
    for writer, table in WRITE_GRANTS:
        if not conn.execute(
                "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'",
                (writer, table)).fetchone():
            actions.append(("insert cfg_write_grant", f"{writer} -> {table}"))
    for key, _ in METHOD_RULES:
        if not conn.execute(
                "SELECT 1 FROM cfg_method_rule WHERE step='cluster.answer' AND rule_key=?",
                (key,)).fetchone():
            actions.append(("insert cfg_method_rule", key))

    print(f"{len(actions)} pending action(s):")
    for a in actions:
        print(" -", a)

    if args.dry_run or not actions:
        print("--dry-run or nothing to do: no changes made.")
        conn.close()
        return 0

    if not conn.execute("SELECT 1 FROM cfg_step WHERE step=? AND work_package=?",
                        (STEP["step"], STEP["work_package"])).fetchone():
        conn.execute(
            "INSERT INTO cfg_step (work_package, ordinal, step, handler, scope, does, inactive, "
            "kind) VALUES (?,?,?,?,?,?,0,?)",
            (STEP["work_package"], STEP["ordinal"], STEP["step"], STEP["handler"], STEP["scope"],
             STEP["does"], STEP["kind"]))

    for writer, table in WRITE_GRANTS:
        if not conn.execute(
                "SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'",
                (writer, table)).fetchone():
            conn.execute(
                "INSERT INTO cfg_write_grant (writer, table_name, database, inactive) "
                "VALUES (?,?, 'iba', 0)", (writer, table))

    for key, text in METHOD_RULES:
        if not conn.execute(
                "SELECT 1 FROM cfg_method_rule WHERE step='cluster.answer' AND rule_key=?",
                (key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
                "ordinal, active) VALUES ('cluster.answer', ?, ?, ?, ?, 0, 1)",
                (key, text, "#1682 §4A (2026-09-11), ib-observation-governing-rules-checklist-v1-"
                 "20260916.md §3, #1706 (this build, 2026-09-18)",
                 "cluster.answer (handlers/cluster.py:answer) -- registered 2026-09-18"))

    conn.commit()
    print("Applied.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
