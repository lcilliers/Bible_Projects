"""surface_subgroup_rules_2291_v1_20261025.py -- escalation #2291 (#2286 build plan U1): the #2286 rulings on the
work unit as behaviour rules, scoped to the scripts they govern; the head cut setting; the observation tag
subgroup-settlement with its guidance.

The rulings and their verbatim sources are in outputs/escalation/2286-bulk-surface-mapping-e3-v2-20261025.md (E1, E2,
E3a, C1 to C5), outputs/escalation/2286-e4-and-t-code-clusters-v2-20261025.md (T-1, T-b, T-c, T-2; E4 on #2286 v33),
outputs/escalation/2286-scope-under-surface-model-v2-20261025.md (S1 to S5) and
outputs/escalation/2286-build-plan-v4-20261025.md (B1 to B6). T-a is rule 70 as amended (#2289). The rulings that
belong to a table or step not yet built (the subgroup kinds and allocation enums, U2; the group size limit and the
tail API, U3) are written with that unit.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Refuses to
run twice.

Usage:
    python iba/app/migration/surface_subgroup_rules_2291_v1_20261025.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import json
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2291-SURFACE-SUBGROUP-RULES-20261025"
MODULE = "surface_subgroup_rules_2291_v1_20261025"
SRC = ("Researcher rulings on escalation #2286 ({v}), verbatim in {doc}; gathered in "
       "outputs/escalation/2286-build-plan-v4-20261025.md; written to config by #2291.")
E3 = "outputs/escalation/2286-bulk-surface-mapping-e3-v2-20261025.md"
T = "outputs/escalation/2286-e4-and-t-code-clusters-v2-20261025.md"
S = "outputs/escalation/2286-scope-under-surface-model-v2-20261025.md"
PLAN = "outputs/escalation/2286-build-plan-v4-20261025.md"

# (rule_key, rule_text, source, scopes)
RULES = [
    ("subgroups-are-surface-groups",
     "A cluster's subgroups are groups of (Strong's code, surface) pairs, the surface being verse_lexical.surface, "
     "never the gloss. Cluster to subgroup is held in cluster_subgroup, pair to subgroup in surface_subgroup, surface "
     "to verse in verse_lexical. The groups are made in bulk before analysis, at the clustering stage, as an "
     "extension of clustering, for the M clusters only: a T-coded word gets pairs in a subgroup only when it joins a "
     "cluster (rule 70). A subgroup has a kind: group, qualifier, not_this_sense or anomaly. The subgroups already "
     "made for M49, M67 and M83 are taken over as they are; a new run touches them only where their data is in error "
     "or missing, and the cluster.subgroup pipeline is retired.",
     SRC.format(v="v20, v22, v24, v38, v41: E1, E2, E3a, T-2, B3, B5", doc=f"{E3}, {T}, {PLAN}"),
     [("ps", "Cluster-Assign.ps1"), ("ps", "ClusterSubgroup.ps1")]),
    ("surface-mapping-conditions",
     "Each M cluster's pairs are allocated with a reason for each. Claude sets the groups and allocates the head (the "
     "pairs covering cfg_setting cluster.surface_map.head_share of the cluster's hits) in session; the API allocates "
     "the tail. A pair carrying two senses is flagged on surface_subgroup. Every allocation is provisional, a way into "
     "the verses and never a finding, and the analytic phase treats it so. Each group gets a size check. Pairs that "
     "fit no group go to the cluster's own anomaly group and are cleared by hand. When a code joins or leaves a "
     "cluster its pairs are allocated again, and a cluster with unallocated or stale pairs is not read until they are.",
     SRC.format(v="v22, v41: C1 to C5, B1, B2", doc=f"{E3}, {PLAN}"),
     [("ps", "Cluster-Assign.ps1"), ("ps", "Reading.ps1")]),
    ("scope-enters-through-surface",
     "A word enters a scope through its surface (verse_lexical.surface) and the subgroups of that surface, never "
     "through word_strong.",
     SRC.format(v="v31: S4", doc=S),
     [("ps", "Verse-Scope.ps1"), ("ps", "Reading.ps1")]),
    ("scope-home-and-multiplicity",
     "A work unit is a subgroup's verses or a subset of them, and that subgroup is the home until all its verses have "
     "been analysed. The other subgroups a verse holds are read in that verse and never add verses to the scope; "
     "where one Strong's code falls in several subgroups, every one of them is read. A qualifier group, and a T "
     "cluster, is never a work unit of its own: a qualifying word, M- or T-coded, is read for what it gives the "
     "characteristic it qualifies, and is not analysed by itself. A T code is raised to M status only by exception; "
     "being used now and then with an M-coded word is no reason for it. A later second reading that synergises all "
     "the M codes of a verse together is not part of the first pass.",
     SRC.format(v="v24, v31, v33: S1, S2, S5, E4, T-1, T-b, T-c", doc=f"{T}, {S}"),
     [("ps", "Verse-Scope.ps1"), ("ps", "Reading.ps1")]),
    ("reading-recorded-per-occurrence",
     "The record of reading is kept per occurrence: each word in each verse, one verse_lexical row. A verse read for "
     "one subgroup is not thereby read for another. A node that cannot be placed on a single occurrence goes to its "
     "cluster's anomaly group and is cleared by hand. Observations that say the same thing over several verses stay "
     "one observation and give one claim, with an anchor verse, traceable to every related verse.",
     SRC.format(v="v31, v34, v41: S3, B6", doc=f"{S}, {PLAN}"),
     [("ps", "Reading.ps1")]),
    ("subgroup-settled-in-claims-step",
     "The observe reading records what the verse says about each word, its role and its face, and changes no "
     "subgroup. Settling a two-sense pair in a verse, and moving a pair to another subgroup, are decided in the claims "
     "step from the tables and written to ib_observation with tag subgroup-settlement, with the reason; a move also "
     "sets the pair's row in surface_subgroup. Until then an occurrence stays in its pair's subgroup.",
     SRC.format(v="v22, v40, v41: C2, C3, B4", doc=f"{E3}, {PLAN}"),
     [("ps", "Reading.ps1")]),
]
SETTINGS = [
    ("cluster.surface_map.head_share", "0.8",
     "#2286 B1 (#2291): the share of a cluster's M-coded hits whose (code, surface) pairs are allocated in session; "
     "the pairs beyond it (the tail) are allocated by the API (behaviour rule surface-mapping-conditions)", "cluster"),
]
TAG = "subgroup-settlement"
TAG_GUIDANCE = ("a claims-step finding (#2286 B4): an occurrence, or every occurrence of a (code, surface) pair, "
                "belongs to the subgroup in cluster_subgroup_id rather than its pair's default, with the reason in "
                "obs_text; applied by its nodes to the occurrences it settles. Written by reading.apply only, never by "
                "the observe reading (behaviour rule subgroup-settled-in-claims-step)")


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan(conn) -> list[tuple]:
    one = lambda sql, *a: conn.execute(sql, a).fetchone()
    ops = []
    nid = one("SELECT max(id) FROM cfg_behaviour_rule")[0]
    for key, text, src, scopes in RULES:
        if one("SELECT 1 FROM cfg_behaviour_rule WHERE class='study_method' AND rule_key=?", key):
            continue
        nid += 1
        ops.append(("cfg_behaviour_rule", "insert", {}, {
            "id": nid, "class": "study_method", "rule_key": key, "rule_text": text, "source": src,
            "enforced_by": "Context-delivered at the first use of the scripts in cfg_rule_scope; built into the "
                           "#2286 units #2292 to #2299, which record their enforcement here",
            "added_at": now(), "active": 1, "enforcement_status": "buildable_not_built",
            "deliver_when": "study_active"}))
        for kind, value in scopes:
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{nid}", "scope_kind": kind,
                                                          "scope_value": value, "inactive": 0}))
    for key, value, use, module in SETTINGS:
        if not one("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": value, "use": use, "module": module,
                                                      "inactive": 0}))
    if not one("SELECT 1 FROM cfg_enum WHERE name='ib_observation.tag' AND value=?", TAG):
        ordn = one("SELECT max(ordinal) FROM cfg_enum WHERE name='ib_observation.tag'")[0] + 1
        ops.append(("cfg_enum", "insert", {}, {"name": "ib_observation.tag", "value": TAG, "ordinal": ordn,
                                               "inactive": 0}))
    guidance = json.loads(one("SELECT value FROM cfg_setting WHERE key='ib_observation.tag_guidance'")[0])
    if TAG not in guidance:
        guidance[TAG] = TAG_GUIDANCE
        ops.append(("cfg_setting", "update", {"key": "ib_observation.tag_guidance"},
                    {"value": json.dumps(guidance, ensure_ascii=False)}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2291 (#2286 U1): the #2286 work-unit rulings as six "
                       f"study_method behaviour rules with their scopes, cluster.surface_map.head_share and the "
                       f"ib_observation tag {TAG}; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID} is in cfg_change_detail)")
        return 0
    ops = plan(conn)
    if a.dry_run:
        for t, op, where, set_ in ops:
            what = (where.get("key") or set_.get("rule_key") or set_.get("key") or set_.get("module")
                    or (set_.get("rule_ref", "") + " " + set_.get("scope_value", "")).strip() or set_.get("value"))
            print(f"  {op:6} {t:20} {what}")
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
