"""node_observation_cluster_retire_2495_v2_20261113.py -- escalation #2495, follow-up of v1 (same day): the retired steps' routed conditions (cfg_on_fail) and the write
grants of cluster.surface_apply and cluster.surface_tail are made inactive, so the config is coherent (configmaint.validate found 15 errors after v1).
cfg_* writes through configmaint.apply_logged(). Registers itself (inactive). Refuses to run twice.
Usage: python -m iba.app.migration.node_observation_cluster_retire_2495_v2_20261113 [--db PATH] [--dry-run]"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2495-RETIRE-CLUSTER-SUBGROUP-V2-20261113"
MODULE = "node_observation_cluster_retire_2495_v2_20261113"
STEPS = ("prior_capture.prepare", "prior_capture.record", "prior_capture.report", "node_resolve.plan", "node_resolve.apply",
         "cluster.surface_apply", "cluster.surface_check", "cluster.surface_pairs", "cluster.surface_tail")


def plan(conn):
    ops = []
    q = ",".join("?" * len(STEPS))
    cols = [r[1] for r in conn.execute("PRAGMA table_info(cfg_on_fail)")]
    for row in conn.execute(f"SELECT * FROM cfg_on_fail WHERE inactive=0 AND step IN ({q})", STEPS).fetchall():
        d = dict(zip(cols, row))
        ops.append(("cfg_on_fail", "update", {"step": d["step"], "condition": d["condition"]}, {"inactive": 1}))
    for w, t, db in conn.execute(f"SELECT writer, table_name, database FROM cfg_write_grant WHERE inactive=0 AND writer IN ({q})", STEPS).fetchall():
        ops.append(("cfg_write_grant", "update", {"writer": w, "table_name": t, "database": db}, {"inactive": 1}))
    if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1, "config_exempt": 1,
            "config_exempt_reason": "one-off migration script -- writes cfg_* rows through configmaint.apply_logged, same class as the other Developer Mode migrations",
            "purpose": f"ONE-OFF migration -- escalation #2495 follow-up: routed conditions and grants of the retired steps made inactive; run_id {RUN_ID}."}))
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
        return 0
    with conn:
        for t, op, where, s in ops:
            apply_logged(conn, RUN_ID, t, op, where, s)
    print(f"{len(ops)} write(s) applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
