"""retire_cluster_reading_grants_2528_v1_20261121.py -- escalation #2528 (build brief B2 and B6), the registrations the retirement left.

configmaint.validate found seven coherence errors after the cluster reading steps were retired and the thought grouping cleared:
  - cfg_on_fail rows of reading.open, reading.observe and reading.record name steps that are not active: made inactive;
  - cfg_write_grant rows whose writer is one of those steps (reading.open, reading.observe, reading.record) are made inactive;
  - surface_event.action gains the two actions the B2 migration wrote (index_reset, subgroup_retire) so that its events are values of the enum.
Every write is apply_logged. Idempotent.

Usage:
    python iba/app/migration/retire_cluster_reading_grants_2528_v1_20261121.py [--db PATH]
After a live run, move this file to iba/app/migration/archive/ (rule 96).
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
RUN_ID = "DEVMODE-2528-RETIRE-CLUSTER-READING-GRANTS-20261121"
STEPS = ("reading.open", "reading.observe", "reading.record", "reading.reopen")
ACTIONS = ("index_reset", "subgroup_retire")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        for st, cond in conn.execute(f"SELECT step, condition FROM cfg_on_fail WHERE inactive=0 AND step IN ({','.join('?' * len(STEPS))})", STEPS).fetchall():
            apply_logged(conn, RUN_ID, "cfg_on_fail", "update", {"step": st, "condition": cond}, {"inactive": 1})
            n += 1
        for w, t, d in conn.execute(f"SELECT writer, table_name, database FROM cfg_write_grant WHERE inactive=0 AND writer IN ({','.join('?' * len(STEPS))})", STEPS).fetchall():
            apply_logged(conn, RUN_ID, "cfg_write_grant", "update", {"writer": w, "table_name": t, "database": d}, {"inactive": 1})
            n += 1
        nxt = conn.execute("SELECT max(ordinal) FROM cfg_enum WHERE name='surface_event.action'").fetchone()[0]
        for v in ACTIONS:
            if not conn.execute("SELECT 1 FROM cfg_enum WHERE name='surface_event.action' AND value=?", (v,)).fetchone():
                nxt += 1
                apply_logged(conn, RUN_ID, "cfg_enum", "insert", {}, {"name": "surface_event.action", "value": v, "ordinal": nxt, "inactive": 0})
                n += 1
    print(f"{n} cfg write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
