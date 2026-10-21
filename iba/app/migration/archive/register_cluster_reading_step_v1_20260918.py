"""Registers `cluster.reading` (Stage 3 of #1706's cluster-reading pipeline, `char-reading`) --
process (c), per-subgroup reading. Design: #1682 §2 (process spec) + `ib-observation-governing-
rules-checklist-v1-20260916.md` §2 (18 rules, "design substantially closed").

Rule 14 (role-driven-walk structurally forced) deliberately NOT encoded here -- superseded
2026-09-17 (recorded #1706 v32, confirmed closed 2026-09-18 against three stale docs that still
cited it as pending). Rules 15/16 (pointer-observation tag naming) also not encoded as separate
rows -- still-open tag-naming items, not blocking, tracked at the checklist's own "still-open items"
section, not duplicated here.

Same work package as Stage 2 (`cluster-reading`) -- houses this step alongside `cluster.subgroup`,
char-answers/char-synergy still to come.

Safe to re-run: idempotent (checks existence before each insert).

Usage:
    python iba/app/migration/register_cluster_reading_step_v1_20260918.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

METHOD_RULES = [
    ("per-subgroup-never-whole-cluster",
     "Always run per subgroup -- never the whole cluster in one pass. #1682 §2 rule 1."),
    ("read-3-sources-complementary-reading",
     "Read all three meaning sources in full for every strong, every time -- never dump raw text "
     "unread, never skip a source. Inherited directly from lexical.meaning's own rule of the same "
     "substance, applied here at subgroup grain. #1682 §2 rule 2."),
    ("scan-every-occurrence-no-sampling",
     "Scan every verse occurrence of every subgroup member strong, corpus-wide -- no sampling, "
     "regardless of strong or subgroup size. A high occurrence count is never a reason to sample "
     "or silently drop instances; it is a reason to raise the occurrence cap or split the subgroup, "
     "never to sample quietly. #1682 §2 rule 3."),
    ("grouping-never-excuses-skipping",
     "Similar verses may be grouped where their meaning is genuinely alike, but grouping does not "
     "excuse skipping any instance -- every occurrence is still accounted for individually in the "
     "trace. #1682 §2 rule 4."),
    ("every-instance-states-what-it-is",
     "Every instance states what it is -- a positive reading, not only a contrast with other "
     "instances. #1682 §2 rule 5."),
    ("not-a-single-distilled-meaning",
     "The aim is not a single distilled meaning -- show what a verse's or strong's meaning could "
     "be or is likely to be, including alternative candidate readings where the data supports more "
     "than one. #1682 §2 rule 6."),
    ("difference-is-its-own-observation",
     "A difference or a specific inference is recorded as its own, separate observation -- never "
     "folded silently into the main per-instance reading. #1682 §2 rule 7."),
    ("cross-strong-comparison-is-this-stages-own-task",
     "This stage's own distinct value beyond Stage 1: synergise the similar and different "
     "contextual meaning of THIS SUBGROUP'S member strongs against each other -- where they "
     "genuinely share meaning and where they diverge, given their full occurrence lists and Stage "
     "1/2's own prior observations as grounding. Do not re-derive or duplicate Stage 1's own "
     "per-occurrence M0.1/M0.5 findings. #1682 §2 (objective), this build's own scoping."),
    ("morph-actively-read-not-merely-carried",
     "span.morph must be actively read, not merely carried -- where occurrences of the same strong "
     "show different stems/voices, check whether the variation is meaning-relevant (does the "
     "subject DO the action, HAVE it done to them, or CAUSE another to do it); record a real "
     "distinction as its own difference-inference, and record a genuine no-distinction-found "
     "result too, not silence. #1682 §2 rule 9."),
    ("per-strong-traceability-verified-by-code",
     "Per-strong traceability is verified before that strong's reading counts as done -- every "
     "occurrence from its full corpus-wide list must be cited in >=1 observation's occurrences for "
     "it. Computed by CODE after the write (recordingpass has already written the observations), "
     "never trusted from an LLM self-report -- an improvement on the original 2026-09-11 spec's "
     "self-reported strong_checks, consistent with question_code/tag/obs_text never being trusted "
     "from the model either. #1682 §2 rule 10, this build's own architecture correction."),
    ("homonym-no-context-earmarked-and-left",
     "A strong that is exclusively a homonym/name with no meaningful context for a human reader is "
     "earmarked as such (tag no-human-context) and left there -- no further analysis attempted. "
     "#1682 §2 rule 11."),
    ("data-errors-flagged-separately",
     "Data-quality issues found while reading (wrong cluster/subgroup membership, a broken span/"
     "verse link, a corrupted meaning source) are flagged as tag data-error, in their own section, "
     "never chased down or fixed as part of this process. #1682 §2 rule 13."),
    ("reread-includes-existing-rows",
     "If this is a re-read of a subgroup already in the database, the input includes that "
     "subgroup's existing char-reading ib_observation rows, so the model sees prior findings "
     "rather than starting blind. #1682/checklist §2 rule 17."),
    ("role-driven-walk-not-forced",
     "The role-driven-walk is NOT a structural gate at this stage -- checklist rule 14's own "
     "'structurally forced' framing was superseded 2026-09-17 (researcher: 'no further mechanical "
     "role work necessary... the question is expanded to explore the impact of the roles'), "
     "confirmed closed 2026-09-18 against three stale docs still citing it as pending (#1706 v34). "
     "Recorded here explicitly so this stage's own build doesn't reintroduce the retired framing."),
]

WORK_PACKAGE_NAME = "cluster-reading"  # already exists (Stage 2) -- not re-inserted, just reused

STEP = {
    "work_package": "cluster-reading",
    "ordinal": 1,
    "step": "cluster.reading",
    "handler": "iba.app.handlers.cluster:reading",
    "scope": "subgroup",
    "kind": "operations",
    "does": (
        "The char-reading stage (#1682/#1706 Phase F, process c): given one subgroup's member "
        "strongs, reads every occurrence corpus-wide (no sampling) plus all meaning sources, using "
        "Stage 1 (verse-reading) and Stage 2 (char-subgroup) observations as grounding, and "
        "synergises the similar/different contextual meaning of the subgroup's OWN member strongs "
        "against each other. Writes ib_observation/ib_node via the recording pass "
        "(stage='char-reading'); per-strong completeness is computed by code, not LLM-self-"
        "reported; advances cluster_subgroup.status from ready_for_reading to ready_for_answer on "
        "success."
    ),
}

WRITE_GRANTS = [("cluster.reading", "ib_observation"), ("cluster.reading", "ib_node")]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    actions = []

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?",
                        (WORK_PACKAGE_NAME,)).fetchone():
        actions.append(("MISSING cfg_work_package (expected to already exist from Stage 2)",
                        WORK_PACKAGE_NAME))
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
                "SELECT 1 FROM cfg_method_rule WHERE step='cluster.reading' AND rule_key=?",
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
                "SELECT 1 FROM cfg_method_rule WHERE step='cluster.reading' AND rule_key=?",
                (key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
                "ordinal, active) VALUES ('cluster.reading', ?, ?, ?, ?, 0, 1)",
                (key, text, "#1682 (2026-09-11), ib-observation-governing-rules-checklist-v1-"
                 "20260916.md §2, #1706 (this build, 2026-09-18)",
                 "cluster.reading (handlers/cluster.py:reading) -- registered 2026-09-18"))

    conn.commit()
    print("Applied.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
