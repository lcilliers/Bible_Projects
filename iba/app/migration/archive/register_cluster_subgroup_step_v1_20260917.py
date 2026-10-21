"""Registers `cluster.subgroup` (Stage 2 of #1706's cluster-reading pipeline, `char-subgroup`) --
process (b), subgroup formation. Design: #1690 (table/rules), #1693 (recording-pass run structure).

New work package `cluster-reading` (cluster-grain, not book-grain like `verse-lexical`) -- houses
this step now and char-reading/char-answers/char-synergy later, same pattern as `verse-lexical`
housing every Layer 1/2 lexical step.

cfg_method_rule rows encode #1690 §2's governing rules (a-h) plus the two "already resolved" items
(one-strong-one-subgroup, FLAG-is-signpost-not-resolution) -- read dynamically by
`subgroupgenerate.py` at prompt-assembly time, same discipline `lexical.meaning`'s own rules
already established (never hardcode rule text where a query can pull the live row).

Safe to re-run: idempotent (checks existence before each insert).

Usage:
    python iba/app/migration/register_cluster_subgroup_step_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

METHOD_RULES = [
    ("full-cluster-read-before-assignment",
     "All gloss and surface values for every strong in the cluster must be read FIRST, before "
     "subgroup assignment begins for any of them -- not a streaming process that assigns strongs "
     "one at a time as they're read. #1690 §2(a), researcher's own instruction, 2026-09-13."),
    ("meaning-based-not-surface-similar",
     "Subgroups are grouped on actual shared meaning, not on strongs whose glosses merely look "
     "alike or share superficial wording. #1690 §2(b)."),
    ("max-10-subgroups-flag-excluded",
     "A cluster's real (non-FLAG) subgroups top out at 10 -- FLAG is a signpost bucket, not a "
     "subgroup competing for that budget, and is excluded from this cap. #1690 §2(c)."),
    ("label-true-to-essence-not-wordlist",
     "label must be true to the subgroup's essence, not an enumeration of its member glosses -- a "
     "label that names what the subgroup actually IS. #1690 §2(d)."),
    ("singleton-subgroup-valid",
     "A subgroup may legitimately hold exactly one strong, if that strong's meaning is genuinely "
     "unique and doesn't fit any other subgroup -- a singleton is a valid outcome, not a sign of "
     "mis-grouping needing correction. #1690 §2(e)."),
    ("flag-conditions-and-reason-required",
     "A strong is assigned to FLAG when it (i) has no inner-being implication, (ii) actually "
     "belongs to another cluster, or (iii) has some other anomaly preventing assignment -- always "
     "with the reason recorded in placement_note (REQUIRED for FLAG placements). #1690 §2(f)/§3 "
     "item 3. FLAG is a signpost, not a resolution in itself -- corrective action is to re-allocate "
     "the strong or resolve the underlying issue elsewhere, never decided by this stage."),
    ("placement-note-captures-any-observation",
     "placement_note is not FLAG-only -- any observation arising from a subgroup assignment is "
     "captured there, optional but available for any ordinary placement too. #1690 §2(g)."),
    ("anchor-verse-llm-selected",
     "For each real subgroup, select the one verse from its own membership that best "
     "describes/represents the subgroup's shared characteristic -- a judgement call made in this "
     "same pass, not a separate metric (word count, verse length, frequency). #1690 §2(h)/§2A. "
     "FLAG has no anchor verse (it is not a real subgroup)."),
    ("one-strong-one-subgroup",
     "Every strong is placed in exactly one subgroup (including FLAG) -- structurally enforced by "
     "cluster_subgroup_strong's UNIQUE(strong) constraint downstream, but the LLM's own output must "
     "already respect it: a strong never appears under two subgroup_codes. #1690 §2 item 2."),
]

WORK_PACKAGE = {
    "name": "cluster-reading",
    "ps_script": "iba/app/ps/ClusterSubgroup.ps1",
    "runs_over": "cluster",
    "chained": 0,
    "complete_message": "subgroup allocation complete for cluster '{cluster_code}'.",
}

STEP = {
    "work_package": "cluster-reading",
    "ordinal": 0,
    "step": "cluster.subgroup",
    "handler": "iba.app.handlers.cluster:subgroup",
    "scope": "cluster",
    "kind": "operations",
    "does": (
        "The char-subgroup stage (#1690/#1693, process b): reads a cluster's full member-strong "
        "list -- gloss/surface plus its already-captured verse-reading (Stage 1) observations -- "
        "in ONE session (never streamed/batched, rule a requires the whole cluster read before any "
        "assignment), and groups strongs into meaning-based subgroups (max 10, FLAG excluded). "
        "Writes cluster_subgroup/cluster_subgroup_strong via the recording pass; advances "
        "cluster.status from ready_for_subgroup_allocation to ready_for_reading on success."
    ),
}

WRITE_GRANTS = [
    ("cluster.subgroup", "cluster_subgroup"), ("cluster.subgroup", "cluster_subgroup_strong"),
    # Added 2026-09-17, same session: the LLM's own `observations` output (distinct from
    # `placement_note`, researcher correction -- see subgroupgenerate.py's own banner) is captured
    # via the SAME recordingpass.record_batch mechanism Stage 1 (`lexical.meaning`) already uses,
    # stage='char-subgroup' -- reusing the existing ib_observation/ib_node capture, not a new one.
    ("cluster.subgroup", "ib_observation"), ("cluster.subgroup", "ib_node"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    actions = []

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?",
                        (WORK_PACKAGE["name"],)).fetchone():
        actions.append(("insert cfg_work_package", WORK_PACKAGE["name"]))
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
                "SELECT 1 FROM cfg_method_rule WHERE step='cluster.subgroup' AND rule_key=?",
                (key,)).fetchone():
            actions.append(("insert cfg_method_rule", key))

    print(f"{len(actions)} pending action(s):")
    for a in actions:
        print(" -", a)

    if args.dry_run or not actions:
        print("--dry-run or nothing to do: no changes made.")
        conn.close()
        return 0

    if not conn.execute("SELECT 1 FROM cfg_work_package WHERE name=?",
                        (WORK_PACKAGE["name"],)).fetchone():
        conn.execute(
            "INSERT INTO cfg_work_package (name, ps_script, runs_over, chained, complete_message, "
            "inactive) VALUES (?,?,?,?,?,0)",
            (WORK_PACKAGE["name"], WORK_PACKAGE["ps_script"], WORK_PACKAGE["runs_over"],
             WORK_PACKAGE["chained"], WORK_PACKAGE["complete_message"]))

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
                "SELECT 1 FROM cfg_method_rule WHERE step='cluster.subgroup' AND rule_key=?",
                (key,)).fetchone():
            conn.execute(
                "INSERT INTO cfg_method_rule (step, rule_key, rule_text, source_doc, enforced_by, "
                "ordinal, active) VALUES ('cluster.subgroup', ?, ?, ?, ?, 0, 1)",
                (key, text, "#1690 (2026-09-13), #1706 (this build, 2026-09-17)",
                 "cluster.subgroup (handlers/cluster.py:subgroup) -- registered 2026-09-17"))

    conn.commit()
    print("Applied.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
