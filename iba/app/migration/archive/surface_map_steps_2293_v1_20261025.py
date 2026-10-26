"""surface_map_steps_2293_v1_20261025.py -- escalation #2293 (#2286 U3; design
outputs/escalation/2293-surface-map-design-v1-20261025.md, decisions D1 to D4 of #2293 v4): the config of the
surface mapping steps.

1. Work package cluster-surface-map (iba/app/ps/Surface-Map.ps1) with steps cluster.surface_pairs,
   cluster.surface_apply, cluster.surface_tail, cluster.surface_check (handlers/surfacemap.py), their routed
   conditions and write grants.
2. Settings: cluster.surface_map.max_group_share 0.3 (D1), cluster.surface_map.output_dir,
   cluster.surface_map.tail_max_output_tokens. The API settings are lexical.llm_* (D3).
3. cfg_utility for lib/surfacemap.py, handlers/surfacemap.py, Surface-Map.ps1 and this script.
4. Behaviour rules B:117 and B:118 reach Surface-Map.ps1 (cfg_rule_scope), and their enforcement is recorded.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.

Usage:
    python iba/app/migration/surface_map_steps_2293_v1_20261025.py [--db PATH] [--dry-run]
"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2293-SURFACE-MAP-STEPS-20261025"
MODULE = "surface_map_steps_2293_v1_20261025"
WP = "cluster-surface-map"
SEE = "see lib/surfacemap.py (escalation #2293, #2286 U3)"
STEPS = [  # step, ordinal, kind, does, grants
    ("cluster.surface_pairs", 0, "utility", "the pairs file of an M cluster: every (code, surface) pair with its hits, "
     "verses, gloss, samples, head or tail, inherited subgroup and live allocation, for Claude to fill (read-only)", []),
    ("cluster.surface_apply", 1, "operations", "the session pass: a filled pairs file written as groups (with kind) and "
     "pair allocations; the whole file refused on any problem; the cluster's anomaly group made",
     ["cluster_subgroup", "surface_subgroup"]),
    ("cluster.surface_tail", 2, "operations", "the API pass: the pairs still unallocated placed in the cluster's groups "
     "or its anomaly group, each with a reason (a preview with the cost unless -Live)",
     ["cluster_subgroup", "surface_subgroup"]),
    ("cluster.surface_check", 3, "utility", "the report of an M cluster's mapping: group sizes and shares (over "
     "cluster.surface_map.max_group_share flagged), the anomaly group, unallocated and two-sense pairs (read-only)", []),
]
ON_FAIL = {  # condition: (path, message)
    "refused": ("report-continue", "refused, nothing written -- the reason follows (a usage outcome, not recorded as an "
                "escalation)"),
}
TAIL_FAIL = {
    "cost-cap-exceeded": ("report-stop", "the pre-call cost estimate exceeds lexical.llm_max_cost_per_batch"),
    "api-key-missing": ("report-stop", "ANTHROPIC_API_KEY not found in the environment or repo-root .env"),
    "api-error": ("report-stop", "the Messages API returned a non-2xx response"),
    "bad-model-response": ("report-stop", "the reply did not place every tail pair once in a known group with a "
                           "reason; nothing written"),
}
SETTINGS = [
    ("cluster.surface_map.max_group_share", "0.3", "#2293 D1: a subgroup of kind group holding more than this share of "
     "its cluster's hits is flagged by cluster.surface_check (look at it; not a forced split)"),
    ("cluster.surface_map.output_dir", json.dumps("outputs/surface-map"), "#2293: where the pairs files and check "
     "reports of the surface mapping are written (versioned per day by lib/filingkit)"),
    ("cluster.surface_map.tail_max_output_tokens", "16000", "#2293 D3: the output ceiling of one tail call (one call per "
     "cluster); model, rates and the per-call cost cap are the lexical.llm_* settings"),
]
UTILITIES = [
    ("surfacemap", "iba/app/lib/surfacemap.py", "surfacemap.py -- the surface mapping of an M cluster (#2293, #2286 "
     "U3): the pairs file, the session pass, the API tail and the check (behaviour rules B:117, B:118)", 0, None),
    ("handlers_surfacemap", "iba/app/handlers/surfacemap.py", "surfacemap handler -- work package cluster-surface-map: "
     "steps cluster.surface_pairs, cluster.surface_apply, cluster.surface_tail, cluster.surface_check (#2293)", 0, None),
    ("Surface-Map.ps1", "iba/app/ps/Surface-Map.ps1", "PS entry point of work package cluster-surface-map (#2293): "
     "-Step Pairs|Apply|Tail|Check -Cluster <M code> [-File] [-Live]", 1,
     "PS entry point: dispatches through run.py; its settings are the steps' own"),
]
SCOPES = [("subgroups-are-surface-groups", "Surface-Map.ps1"), ("surface-mapping-conditions", "Surface-Map.ps1")]
ENFORCED = {
    "subgroups-are-surface-groups": ("partially_enforced", "iba/app/lib/surfacemap.py (work package "
                                     "cluster-surface-map, #2293): pairs held per surface, kinds, M clusters only, "
                                     "inherited subgroups kept; the retirement of cluster.subgroup is #2299"),
    "surface-mapping-conditions": ("partially_enforced", "iba/app/lib/surfacemap.py (#2293): reason per pair, head in "
                                   "session, tail by the API, two-sense flag, anomaly group, size check; stale pairs "
                                   "after a cluster change are #2294"),
}


def plan(conn) -> list[tuple]:
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    if not has("SELECT 1 FROM cfg_work_package WHERE name=?", WP):
        ops.append(("cfg_work_package", "insert", {}, {
            "name": WP, "ps_script": "iba/app/ps/Surface-Map.ps1", "runs_over": "none", "chained": 0,
            "complete_message": None, "next_step_hint": None, "paused_message": None, "inactive": 0}))
    for step, o, kind, does, grants in STEPS:
        if not has("SELECT 1 FROM cfg_step WHERE step=?", step):
            ops.append(("cfg_step", "insert", {}, {
                "work_package": WP, "ordinal": o, "step": step, "handler": f"iba.app.handlers.surfacemap:"
                f"{step.split('_', 1)[1]}", "scope": "none", "does": f"{does} -- {SEE}", "inactive": 0, "kind": kind}))
        fails = {**ON_FAIL, **(TAIL_FAIL if step == "cluster.surface_tail" else {})}
        for cond, (path, msg) in fails.items():
            if not has("SELECT 1 FROM cfg_on_fail WHERE step=? AND condition=?", step, cond):
                ops.append(("cfg_on_fail", "insert", {}, {"step": step, "condition": cond, "path": path,
                                                          "resolver": None, "message": msg, "route": "terminal",
                                                          "inactive": 0}))
        for table in grants:
            if not has("SELECT 1 FROM cfg_write_grant WHERE writer=? AND table_name=? AND database='iba'", step, table):
                ops.append(("cfg_write_grant", "insert", {}, {"writer": step, "table_name": table, "database": "iba",
                                                              "inactive": 0}))
    for key, value, use in SETTINGS:
        if not has("SELECT 1 FROM cfg_setting WHERE key=?", key):
            ops.append(("cfg_setting", "insert", {}, {"key": key, "value": value, "use": use, "module": "cluster",
                                                      "inactive": 0}))
    for module, path, purpose, exempt, reason in UTILITIES:
        if not has("SELECT 1 FROM cfg_utility WHERE module=?", module):
            ops.append(("cfg_utility", "insert", {}, {"module": module, "file_path": path, "purpose": purpose,
                                                      "inactive": 0, "config_exempt": exempt,
                                                      "config_exempt_reason": reason, "crash_escalation_reviewed": 0,
                                                      "crash_escalation_note": None}))
    for key, ps in SCOPES:
        rid = one("SELECT id FROM cfg_behaviour_rule WHERE class='study_method' AND rule_key=?", key)[0]
        if not has("SELECT 1 FROM cfg_rule_scope WHERE rule_ref=? AND scope_kind='ps' AND scope_value=?", f"B:{rid}", ps):
            ops.append(("cfg_rule_scope", "insert", {}, {"rule_ref": f"B:{rid}", "scope_kind": "ps", "scope_value": ps,
                                                          "inactive": 0}))
    for key, (status, by) in ENFORCED.items():
        r = one("SELECT id, enforcement_status, enforced_by FROM cfg_behaviour_rule WHERE class='study_method' AND "
                "rule_key=?", key)
        if (r[1], r[2]) != (status, by):
            ops.append(("cfg_behaviour_rule", "update", {"id": r[0]}, {"enforcement_status": status,
                                                                       "enforced_by": by}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2293 (#2286 U3): work package cluster-surface-map, its four "
                       f"steps, grants, conditions, settings, utilities and rule scopes; run_id {RUN_ID}."}))
    return ops


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    ops = plan(conn)
    if a.dry_run:
        for t, op, where, set_ in ops:
            what = set_.get("step") or set_.get("key") or set_.get("module") or set_.get("name") or \
                f"{set_.get('writer', '')}{set_.get('rule_ref', '')} {set_.get('table_name') or set_.get('condition') or set_.get('scope_value') or where}"
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
