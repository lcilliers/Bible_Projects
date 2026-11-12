"""withdraw_nodes_of_withdrawn_observations_2487_v1_20261112.py -- escalation #2487, first corrective step.

A live node (deleted=0) on an observation that is withdrawn (deleted=1) breaks the rule that a node cannot exist without a live
observation. Each such node is withdrawn the way a reading withdraws one (observationrecord.delete_node): deleted=1, the change
kept in ib_observation_change with its reason. The disposition column is left alone (it belongs to the claims step).
The run stops and rolls back unless the counts equal the prediction taken before the write. Idempotent: a second run finds none.
    python iba/app/migration/withdraw_nodes_of_withdrawn_observations_2487_v1_20261112.py [--db PATH] [--dry-run]
"""
import argparse
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import observationrecord as orec  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2487-NODES-ON-WITHDRAWN-OBS-20261112"
REASON = ("the observation this node belongs to is withdrawn, and a node cannot be live without a live observation "
          "(researcher ruling of 2026-11-12, #2487 rule R1)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    one = lambda s: conn.execute(s).fetchone()[0]
    ids = [r[0] for r in conn.execute(
        "SELECT n.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
        "WHERE n.deleted=0 AND o.deleted=1 ORDER BY n.id")]
    pred = dict(withdraw=len(ids), live_after=one("SELECT count(*) FROM ib_node WHERE deleted=0") - len(ids),
                changes_after=one("SELECT count(*) FROM ib_observation_change") + len(ids),
                live_obs=one("SELECT count(*) FROM ib_observation WHERE deleted=0"))
    print("predicted:", pred)
    conn.execute("SAVEPOINT w")
    try:
        done = sum(1 for nid in ids if orec.delete_node(conn, nid, REASON, None, RUN_ID, "Claude"))
        got = dict(withdraw=done, live_after=one("SELECT count(*) FROM ib_node WHERE deleted=0"),
                   changes_after=one("SELECT count(*) FROM ib_observation_change"),
                   live_obs=one("SELECT count(*) FROM ib_observation WHERE deleted=0"))
        left = one("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=1")
        print("actual:   ", got, "| live nodes still on a withdrawn observation:", left)
        if got != pred or left != 0:
            raise RuntimeError("actual differs from predicted: rolled back")
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
