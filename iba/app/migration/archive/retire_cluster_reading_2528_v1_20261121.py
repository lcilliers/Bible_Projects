"""retire_cluster_reading_2528_v1_20261121.py -- escalation #2528 (build brief B6; audit finding F5 of outputs/escalation/2526-stages-1-to-4-readiness-audit-v1-20261121.md).

Stage 4 of the study is now built on the collection, the subgroup and the ledger (steps 3.1 to 3.3, lib/layerinner.py). The earlier reading of a cluster or a subgroup of the cluster allocation, whose
observe phase did the lexical and the inner-being work in one pass, is retired as a way to start work. This migration does it in the configuration, reversibly (the code is not deleted):
  - cfg_step reading.open, reading.observe, reading.record and reading.reopen: inactive=1, the description starting RETIRED (the dispatcher refuses an inactive step, run.py);
  - cfg_method_rule RM-03 no-whole-cluster and RO8 no-whole-cluster (they name the cluster reading start, whose setting reading.whole_cluster_reading_start is already inactive): active=0.
The narrative steps (reading.synergy, apply, narrate, publish, account, check) stay; the 10 reading rows already made keep their state. Behaviour rules 119 and 120 already describe the collection scope
(rewritten at #2505) and are not changed; RO13 was already inactive.
Every write is apply_logged. Idempotent.

Usage:
    python iba/app/migration/retire_cluster_reading_2528_v1_20261121.py [--db PATH]
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
RUN_ID = "DEVMODE-2528-RETIRE-CLUSTER-READING-20261121"
STEPS = ("reading.open", "reading.observe", "reading.record", "reading.reopen")
RULES = ("RM-03 no-whole-cluster", "RO8 no-whole-cluster")
MARK = "RETIRED (#2528): the reading of a cluster or a subgroup of the cluster allocation is replaced by the layered reading of the collection (stage 4 is steps 3.1 to 3.3, Collection-Build.ps1 LayerOpen). "


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    n = 0
    with conn:
        for st in STEPS:
            row = conn.execute("SELECT work_package, does, inactive FROM cfg_step WHERE step=?", (st,)).fetchone()
            if row and not row[2]:
                apply_logged(conn, RUN_ID, "cfg_step", "update", {"work_package": row[0], "step": st}, {"inactive": 1, "does": MARK + (row[1] or "")})
                n += 1
        for key in RULES:
            row = conn.execute("SELECT id, active FROM cfg_method_rule WHERE rule_key=?", (key,)).fetchone()
            if row and row[1]:
                apply_logged(conn, RUN_ID, "cfg_method_rule", "update", {"id": row[0]}, {"active": 0})
                n += 1
    print(f"{n} cfg write(s) (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
