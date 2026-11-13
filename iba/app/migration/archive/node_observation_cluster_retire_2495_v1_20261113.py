"""node_observation_cluster_retire_2495_v1_20261113.py -- escalation #2495: cluster and subgroup retired from the node and observation process
(researcher, 2026-11-13, #2484 ruling 4.4: 'notes and observations should not have any part to play with clusters and sub groups. all rules associated to the
maintenance of clusters and sub groups in the observations process must be retired.'). The code that enforced them is changed in the same unit of work
(BUILD 527), so config and code agree (B:62).

1. cfg_setting reading.verse_loop (node_set) and reading.observation_parts (node): cluster_code and cluster_subgroup_code removed.
2. Behaviour rules retired (inactive, scope rows inactive): 66 (cluster labels), 117 (subgroups are surface groups), 118 (surface mapping conditions).
   Behaviour rule 121 (reading recorded per occurrence) is context-delivered and checked by the node checker.
3. Method rules retired: CP-01 to CP-10 (prior_capture.record) and NR-01 to NR-06 (node_resolve.apply).
4. Work packages prior-capture and node-resolve, and the Surface-Map steps (cluster.surface_*) of work package cluster-surface-map, made inactive with their
   write grants and settings; their scripts moved to archive/ (cfg_utility file_path and inactive).
Behaviour rules 119 and 120 and method rules RO13, RM-03 and RO8 stay: `Reading.ps1 -Step Open` still opens a reading on a subgroup until the reading by
collections (#2448) replaces it.

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.
Usage: python -m iba.app.migration.node_observation_cluster_retire_2495_v1_20261113 [--db PATH] [--dry-run]"""
import argparse
import json
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2495-RETIRE-CLUSTER-SUBGROUP-20261113"
MODULE = "node_observation_cluster_retire_2495_v1_20261113"
RET = ("Retired 2026-11-13 (#2495; researcher, #2484 ruling 4.4: clusters and subgroups served to establish the collections and play no part in nodes and "
       "observations; the rules for their maintenance in the observation process are retired). The code that enforced it was changed in BUILD 527.")
RULES_RETIRE = (66, 117, 118)
B121 = ("Context-delivered at the first use of the reading scripts (cfg_rule_scope); every live node with no occurrence is listed by iba/app/ps/Node-Check.ps1 "
        "(N-no-occurrence), and the writers (iba/app/lib/observationrecord.py, iba/app/lib/draftapply.py) place a node on one occurrence.")
RETIRED_PACKAGES = ("prior-capture", "node-resolve")
RETIRED_STEPS = ("prior_capture.prepare", "prior_capture.record", "prior_capture.report", "node_resolve.plan", "node_resolve.apply",
                 "cluster.surface_apply", "cluster.surface_check", "cluster.surface_pairs", "cluster.surface_tail")
UTILITIES = {   # module -> archive path
    "priorcapture": "iba/app/lib/archive/priorcapture.py", "handlers_priorcapture": "iba/app/handlers/archive/priorcapture.py",
    "Prior-Capture.ps1": "iba/app/ps/archive/Prior-Capture.ps1", "noderesolve": "iba/app/lib/archive/noderesolve.py",
    "handlers_noderesolve": "iba/app/handlers/archive/noderesolve.py", "Node-Resolve.ps1": "iba/app/ps/archive/Node-Resolve.ps1",
    "handlers_surfacemap": "iba/app/handlers/archive/surfacemap.py", "Surface-Map.ps1": "iba/app/ps/archive/Surface-Map.ps1"}


def plan(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    for key, field in (("reading.verse_loop", "node_set"), ("reading.observation_parts", "node")):
        v = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key=?", (key,)).fetchone()[0])
        kept = [x for x in v[field] if x not in ("cluster_code", "cluster_subgroup_code")]
        if kept != v[field]:
            v[field] = kept
            ops.append(("cfg_setting", "update", {"key": key}, {"value": json.dumps(v, ensure_ascii=False)}))
    for rid in RULES_RETIRE:
        if has("SELECT 1 FROM cfg_behaviour_rule WHERE id=? AND active=1", rid):
            ops.append(("cfg_behaviour_rule", "update", {"id": rid}, {"active": 0, "enforcement_status": "deliberately_deferred", "enforced_by": RET}))
            for (sid,) in conn.execute("SELECT id FROM cfg_rule_scope WHERE rule_ref=? AND inactive=0", (f"B:{rid}",)).fetchall():
                ops.append(("cfg_rule_scope", "update", {"id": sid}, {"inactive": 1}))
    if has("SELECT 1 FROM cfg_behaviour_rule WHERE id=121 AND enforcement_status<>'context_delivered'"):
        ops.append(("cfg_behaviour_rule", "update", {"id": 121}, {"enforcement_status": "context_delivered", "enforced_by": B121}))
    for (mid,) in conn.execute("SELECT id FROM cfg_method_rule WHERE active=1 AND step IN ('prior_capture.record','node_resolve.apply')").fetchall():
        ops.append(("cfg_method_rule", "update", {"id": mid}, {"active": 0}))
    for wp in RETIRED_PACKAGES:
        if has("SELECT 1 FROM cfg_work_package WHERE name=? AND inactive=0", wp):
            ops.append(("cfg_work_package", "update", {"name": wp}, {"inactive": 1}))
    for st in RETIRED_STEPS:
        if has("SELECT 1 FROM cfg_step WHERE step=? AND inactive=0", st):
            ops.append(("cfg_step", "update", {"step": st}, {"inactive": 1}))
    for w, t, d in conn.execute("SELECT writer, table_name, database FROM cfg_write_grant WHERE inactive=0 AND writer IN ('prior_capture.record','node_resolve.apply')").fetchall():
        ops.append(("cfg_write_grant", "update", {"writer": w, "table_name": t, "database": d}, {"inactive": 1}))
    for (key,) in conn.execute("SELECT key FROM cfg_setting WHERE inactive=0 AND module IN ('prior_capture','node_resolve')").fetchall():
        ops.append(("cfg_setting", "update", {"key": key}, {"inactive": 1}))
    for module, path in UTILITIES.items():
        if has("SELECT 1 FROM cfg_utility WHERE module=? AND (file_path<>? OR inactive=0)", module, path):
            ops.append(("cfg_utility", "update", {"module": module}, {"file_path": path, "inactive": 1}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2495: cluster and subgroup retired from the node and observation process; run_id {RUN_ID}."}))
    return ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    if conn.execute("SELECT 1 FROM cfg_change_detail WHERE run_id=?", (RUN_ID,)).fetchone():
        print(f"already applied (run {RUN_ID})")
        return 0
    ops = plan(conn)
    if a.dry_run:
        print(f"DRY RUN -- {len(ops)} write(s)")
        for t, op, w, s in ops:
            print("  ", op, t, json.dumps(w), list(s)[:3])
        return 0
    with conn:
        for t, op, where, s in ops:
            apply_logged(conn, RUN_ID, t, op, where, s)
    print(f"{len(ops)} write(s) applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
