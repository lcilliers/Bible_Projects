"""withdraw_out_of_scope_nodes_2491_v1_20261113.py -- escalation #2491, after the rebuild of the collections: the out-of-scope nodes again.

Researcher, 2026-11-13: 'Yes, withdraw' (the live nodes that, after the rebuild, sit on a verse with no member surface, and the observations left with no live node). The rule is the one of 2026-11-12 below, applied to the rebuilt collections.

Researcher, 2026-11-12: 'mark the out of scope nodes as deleted, ensure that the observations go the same way.'
Scope is the one of plan v3 (outputs/escalation/2487-node-salvage-plan-v3-20261112.md) as read by the node workbook
(_analytics/surfaces/exports/node-validation-v4-plan-v3-20261112.xlsx): a verse is in scope if one of its non-gloss words is a
surface of a member base (tiers core, synonym, opposite, gathered, phrase; a link on the surface's own row or on its base).
A live node whose verse is not in scope, or that has no verse, is out of scope: withdrawn the way a reading withdraws one
(observationrecord.delete_node). An observation left with no live node by this step is withdrawn the same way
(observationrecord.soft_delete_observation). An observation that keeps a live node, and observations that had no live node before
this step, are not touched. The run stops and rolls back unless the counts equal the prediction taken before the write.
Idempotent: a second run finds none.
    python iba/app/migration/-m iba.app.migration.withdraw_out_of_scope_nodes_2491_v1_20261113 [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2491-OUT-OF-SCOPE-NODES-20261113"
TIERS = ("core", "synonym", "opposite", "gathered", "phrase")
NODE_REASON = ("the node is out of scope: its verse has no word that is a surface of a collection member, or it has no verse "
               "(researcher rulings of 2026-11-12, #2487, and 2026-11-13, #2491: the scope applied to the rebuilt collections)")
OBS_REASON = ("every live node of the observation was out of scope and withdrawn "
              "(researcher rulings of 2026-11-12, #2487, and 2026-11-13, #2491: the observations go the same way)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    q = lambda s, *p: conn.execute(s, p).fetchall()
    one = lambda s: conn.execute(s).fetchone()[0]

    cols = collections.defaultdict(set)
    for r in q("SELECT l.term_id, l.collection_id FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status IN ('indicative','confirmed') AND l.tier IN (%s)" % ",".join("?" * len(TIERS)), *TIERS):
        cols[r[0]].add(r[1])
    st = collections.defaultdict(list)
    for r in q("SELECT id, surface, base_id FROM surface_term WHERE deleted=0"):
        st[r[1]].append((r[0], r[2]))
    member = {s for s, l in st.items() if any(cols.get(sid) or (b and cols.get(b)) for sid, b in l)}
    vo = {r[0]: r[1] for r in q("SELECT id, osisId FROM verse")}
    inscope = set()
    for r in q("SELECT verse_id, lower(trim(surface)), surface_kind FROM verse_lexical WHERE deleted=0"):
        if r[1] in member and r[2] != "gloss":
            inscope.add(vo.get(r[0]))
    nodes = q("""SELECT n.id, n.observation_id,
                 COALESCE(n.verse_reference, (SELECT ve.osisId FROM verse_lexical v JOIN verse ve ON ve.id=v.verse_id WHERE v.id=n.verse_lexical_id))
                 FROM ib_node n WHERE n.deleted=0""")
    out_ids = [n[0] for n in nodes if n[2] is None or n[2] not in inscope]
    out_set = set(out_ids)
    by_obs = collections.defaultdict(list)
    for n in nodes:
        by_obs[n[1]].append(n[0])
    live_o = {r[0]: r[1] for r in q("SELECT id, status FROM ib_observation WHERE deleted=0")}
    obs_ids = sorted(o for o, l in by_obs.items() if o in live_o and all(x in out_set for x in l))
    live_nodes, live_obs = one("SELECT count(*) FROM ib_node WHERE deleted=0"), one("SELECT count(*) FROM ib_observation WHERE deleted=0")
    changes = one("SELECT count(*) FROM ib_observation_change")
    status_changes = sum(1 for o in obs_ids if live_o[o] != "withdrawn")
    pred = dict(nodes_withdrawn=len(out_ids), observations_withdrawn=len(obs_ids), live_nodes_after=live_nodes - len(out_ids),
                live_obs_after=live_obs - len(obs_ids),
                changes_after=changes + len(out_ids) + len(obs_ids) + status_changes)
    print("predicted:", pred)
    conn.execute("SAVEPOINT w")
    try:
        nd = sum(1 for nid in out_ids if orec.delete_node(conn, nid, NODE_REASON, None, RUN_ID, "Claude"))
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
