"""withdraw_surfaceless_nodes_2487_v1_20261112.py -- escalation #2487, third corrective step.

Researcher, 2026-11-12: the prior-capture draft nodes that have no surface cannot be used downstream (no method of connecting them to
anything useful); 'Yes, withdraw them'. Every live node with no surface (surface null or blank) is withdrawn the way a reading withdraws
one (observationrecord.delete_node). An observation left with no live node by this step is withdrawn the same way
(observationrecord.soft_delete_observation), as in the out-of-scope step. Held back and listed for the researcher, not withdrawn: a
node on an observation that has a row in ib_observation_change before this run, or that another node traces
(ib_node.traced_observation_id). An observation that keeps a live node is not touched. The run stops and rolls back unless the counts
equal the prediction. Idempotent.
    python iba/app/migration/withdraw_surfaceless_nodes_2487_v1_20261112.py [--db PATH] [--dry-run]
"""
import argparse
import collections
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import observationrecord as orec  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2487-SURFACELESS-NODES-20261112"
NODE_REASON = ("the node has no surface, so it cannot be connected to a collection or used downstream; a prior-capture draft "
               "(researcher ruling of 2026-11-12, #2487)")
OBS_REASON = ("every live node of the observation was surfaceless and withdrawn "
              "(researcher ruling of 2026-11-12, #2487: the observations go the same way)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    q = lambda s, *p: conn.execute(s, p).fetchall()
    one = lambda s: conn.execute(s).fetchone()[0]

    held_obs = {r[0] for r in q("SELECT DISTINCT observation_id FROM ib_observation_change "
                  "WHERE observation_id IS NOT NULL AND COALESCE(run_id, '') NOT LIKE 'DEVMODE-2487-%'")}
    held_obs |= {r[0] for r in q("SELECT DISTINCT traced_observation_id FROM ib_node WHERE traced_observation_id IS NOT NULL")}
    nodes = q("SELECT id, observation_id, (surface IS NULL OR trim(surface)='') AS nosurf FROM ib_node WHERE deleted=0")
    target = [n[0] for n in nodes if n[2] and n[1] not in held_obs]
    held_nodes = [n[0] for n in nodes if n[2] and n[1] in held_obs]
    tset = set(target)
    by_obs = collections.defaultdict(list)
    for n in nodes:
        by_obs[n[1]].append(n[0])
    live_o = {r[0]: r[1] for r in q("SELECT id, status FROM ib_observation WHERE deleted=0")}
    obs_ids = sorted(o for o, l in by_obs.items() if o in live_o and all(x in tset for x in l))
    live_nodes, live_obs = one("SELECT count(*) FROM ib_node WHERE deleted=0"), one("SELECT count(*) FROM ib_observation WHERE deleted=0")
    changes = one("SELECT count(*) FROM ib_observation_change")
    status_changes = sum(1 for o in obs_ids if live_o[o] != "withdrawn")
    pred = dict(nodes_withdrawn=len(target), observations_withdrawn=len(obs_ids), live_nodes_after=live_nodes - len(target),
                live_obs_after=live_obs - len(obs_ids), changes_after=changes + len(target) + len(obs_ids) + status_changes)
    print("predicted:", pred)
    print("held back (surfaceless nodes on observations with a change record or traced):", len(held_nodes), "nodes on",
          len({n[1] for n in nodes if n[0] in set(held_nodes)}), "observations")
    conn.execute("SAVEPOINT w")
    try:
        nd = sum(1 for nid in target if orec.delete_node(conn, nid, NODE_REASON, None, RUN_ID, "Claude"))
        for o in obs_ids:
            orec.soft_delete_observation(conn, o, OBS_REASON, None, RUN_ID, "Claude")
        got = dict(nodes_withdrawn=nd, observations_withdrawn=len(obs_ids), live_nodes_after=one("SELECT count(*) FROM ib_node WHERE deleted=0"),
                   live_obs_after=one("SELECT count(*) FROM ib_observation WHERE deleted=0"),
                   changes_after=one("SELECT count(*) FROM ib_observation_change"))
        stranded = one("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=1")
        print("actual:   ", got, "| live nodes on a withdrawn observation:", stranded)
        if got != pred or stranded != 0:
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
