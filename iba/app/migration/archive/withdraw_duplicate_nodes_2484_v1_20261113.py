"""withdraw_duplicate_nodes_2484_v1_20261113.py -- escalation #2484, first fix class (the duplicate nodes, behaviour rule B:130 N-duplicate).

Researcher, 2026-11-13 (rulings 4.1 and the node rules): two nodes of one observation whose indexing columns are exactly the same are a
duplicate (or incomplete); a duplicate is withdrawn and never allowed. A group is the live nodes with the same (observation_id,
verse_reference, verse_lexical_id, surface, strong, collection_id) as stored. The lowest-id node of a group is kept (the original; the
later ones are re-capture copies: every other column is the same, only traced_observation_id differs). Each later node is withdrawn the way
a reading withdraws one (observationrecord.delete_node: deleted=1 and a row in ib_observation_change with the reason).
Held back and listed, not withdrawn: a group where a later node carries a disposition that the kept node does not. Not in this step: the nodes
the checker finds as duplicates only after verse_lexical_id is derived (they are incomplete first). The run stops and rolls back unless the
counts equal the prediction. Idempotent.
    python iba/app/migration/withdraw_duplicate_nodes_2484_v1_20261113.py [--db PATH] [--dry-run] [--stages a,b]
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
RUN_ID = "DEVMODE-2484-DUPLICATE-NODES-20261113"
REASON = ("duplicate node: the same observation, verse, surface, Strong's code and collection as the kept node {keep}; a duplicate is "
          "withdrawn and not allowed (node rules B:130, researcher ruling 4.1 of 2026-11-13, #2484)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stages", default="", help="pilot: only nodes whose source_stage is one of these (comma separated)")
    a = ap.parse_args()
    stages = {s for s in a.stages.split(",") if s}
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    one = lambda s: conn.execute(s).fetchone()[0]

    groups = collections.defaultdict(list)
    for r in conn.execute("SELECT id, observation_id, verse_reference, verse_lexical_id, surface, strong, collection_id, disposition, source_stage "
                          "FROM ib_node WHERE deleted=0 ORDER BY id"):
        groups[(r[1], r[2], r[3], r[4], r[5], r[6])].append(r)
    todo, held = [], []
    for g in groups.values():
        if len(g) < 2:
            continue
        keep = g[0]
        for x in g[1:]:
            if x["disposition"] and not keep["disposition"]:
                held.append(x["id"])
            elif not stages or x["source_stage"] in stages:
                todo.append((x["id"], keep["id"]))
    live_nodes, live_obs, changes = (one("SELECT count(*) FROM ib_node WHERE deleted=0"), one("SELECT count(*) FROM ib_observation WHERE deleted=0"),
                                     one("SELECT count(*) FROM ib_observation_change"))
    pred = dict(nodes_withdrawn=len(todo), live_nodes_after=live_nodes - len(todo), live_obs_after=live_obs, changes_after=changes + len(todo))
    print("predicted:", pred, "| held back (a later node has a disposition the kept one lacks):", len(held), held[:20])
    conn.execute("SAVEPOINT w")
    try:
        nd = sum(1 for nid, keep in todo if orec.delete_node(conn, nid, REASON.format(keep=keep), None, RUN_ID, "Claude"))
        got = dict(nodes_withdrawn=nd, live_nodes_after=one("SELECT count(*) FROM ib_node WHERE deleted=0"),
                   live_obs_after=one("SELECT count(*) FROM ib_observation WHERE deleted=0"), changes_after=one("SELECT count(*) FROM ib_observation_change"))
        left = 0
        if not stages:
            seen = collections.Counter()
            for r in conn.execute("SELECT observation_id, verse_reference, verse_lexical_id, surface, strong, collection_id FROM ib_node WHERE deleted=0"):
                seen[tuple(r)] += 1
            left = sum(v - 1 for v in seen.values() if v > 1)
        nokeep = one("SELECT count(*) FROM (SELECT DISTINCT observation_id FROM ib_node WHERE deleted=1 AND id IN (SELECT node_id FROM ib_observation_change "
                     f"WHERE run_id='{RUN_ID}')) d WHERE NOT EXISTS (SELECT 1 FROM ib_node n WHERE n.observation_id=d.observation_id AND n.deleted=0)")
        print("actual:   ", got, "| duplicate nodes left:", left, "(held:", len(held), ") | observations left with no live node:", nokeep)
        if got != pred or nokeep != 0 or (not stages and left != len(held)):
            raise RuntimeError("actual differs from predicted: rolled back")
        if a.dry_run:
            conn.execute("ROLLBACK TO w")
            print("dry run: rolled back")
        else:
            conn.execute("RELEASE w")
            conn.commit()
            print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w")
        conn.commit()
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
