"""t_word_and_retire_2297_2299_v1_20261026.py -- escalations #2297 (#2286 U7) and #2299 (#2286 U9), config only, as the
researcher directed on 2026-10-26: "U7 seems like a simple config to add ... U9, just update the configs for the
retirement".

1. U7: cfg_method_rule RA-01 t-word-joins-cluster on reading.apply (T-a under rule 70 as amended, #2289).
2. U9: the cluster.subgroup pipeline retired (B5): steps cluster.subgroup, cluster.reading and cluster.answer made
   inactive; the two rule scopes on iba/app/ps/ClusterSubgroup.ps1 made inactive; B:117's enforcement recorded.
   (Their write grants: retire_grants_2299_v1_20261026.py.)

cfg_* writes through configmaint.apply_logged(). Registers itself (inactive, at its own archive path). Idempotent.

Usage:
    python iba/app/migration/t_word_and_retire_2297_2299_v1_20261026.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2297-2299-T-WORD-RETIRE-20261026"
MODULE = "t_word_and_retire_2297_2299_v1_20261026"
RULE = {"step": "reading.apply", "rule_key": "RA-01 t-word-joins-cluster", "ordinal": 69, "active": 1,
        "rule_text": "Where the claims step finds that a T-coded word is itself the characteristic in its verse (T-a), "
                     "it records the finding in ib_observation with the reason, and the code is added to the "
                     "characteristic's cluster in cluster_strong beside its T tag; it is never moved out of a cluster. "
                     "Surface-Map.ps1 -Step Apply -Cluster <M code> then places the code's new (code, surface) pairs in "
                     "the subgroup, and reading.open refuses the cluster until they are placed (rule 118). The "
                     "cluster's label is reconsidered against its new membership (rule 66). A T-coded word that only "
                     "qualifies is read for what it gives and is not added (rule 120).",
        "source_doc": "#2286 v20-v22 (T-a, P1-a), rule 70 as amended (#2289); #2297",
        "enforced_by": None}
RETIRED_STEPS = ("cluster.subgroup", "cluster.reading", "cluster.answer")
B117 = ("mechanically_enforced",
        "iba/app/lib/surfacemap.py (work package cluster-surface-map, #2293): pairs held per surface, kinds, M clusters "
        "only, inherited subgroups kept; the cluster.subgroup pipeline (cluster.subgroup, cluster.reading, "
        "cluster.answer) is inactive (#2299).")


def plan(conn) -> list[tuple]:
    ops = []
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    if not one("SELECT 1 FROM cfg_method_rule WHERE step=? AND rule_key=?", RULE["step"], RULE["rule_key"]):
        ops.append(("cfg_method_rule", "insert", {}, RULE))
    for s in RETIRED_STEPS:
        if one("SELECT inactive FROM cfg_step WHERE step=?", s)[0] != 1:
            ops.append(("cfg_step", "update", {"step": s}, {"inactive": 1}))
    for (sid,) in conn.execute("SELECT id FROM cfg_rule_scope WHERE scope_kind='ps' AND scope_value='ClusterSubgroup.ps1' "
                               "AND inactive=0").fetchall():
        ops.append(("cfg_rule_scope", "update", {"id": sid}, {"inactive": 1}))
    r = one("SELECT id, enforcement_status, enforced_by FROM cfg_behaviour_rule WHERE class='study_method' AND "
            "rule_key='subgroups-are-surface-groups'")
    if (r[1], r[2]) != B117:
        ops.append(("cfg_behaviour_rule", "update", {"id": r[0]}, {"enforcement_status": B117[0], "enforced_by": B117[1]}))
    if not one("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalations #2297 and #2299 (#2286 U7, U9): method rule RA-01 on "
                       f"reading.apply; the cluster.subgroup pipeline retired; run_id {RUN_ID}."}))
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
            print(f"  {op:6} {t:20} {where or set_.get('rule_key') or set_.get('module')}")
        print(f"DRY RUN -- {len(ops)} write(s)")
        return 0
    with conn:
        for t, op, where, set_ in ops:
            apply_logged(conn, RUN_ID, t, op, where, set_)
    print(f"{len(ops)} write(s) applied (run {RUN_ID}, logged to cfg_change_detail)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
