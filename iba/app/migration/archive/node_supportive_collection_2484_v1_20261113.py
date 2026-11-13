"""node_supportive_collection_2484_v1_20261113.py -- escalation #2484, fourth fix class: the supportive nodes with no collection (B:130 N-no-collection).

Researcher, 2026-11-13: 'Missing collections'. Rulings: a node on an entity or other surface takes the collection of the surface it supports, so every node of
a collection is discoverable through it; where it supports surfaces of several collections there is a node for each (ruling 4.1, a variant).
A live node with a surface that is in no collection, in a verse that holds a member surface, with no collection, takes the collection(s) of the live nodes of
its OWN OBSERVATION in the SAME VERSE that carry one: the surface it supports. One collection: set on the node. Several: set the lowest collection id on the
node and add a node for each other (a copy of the node's columns except id, seq, created_at, traced_observation_id and collection_id). A collection the
observation already has a live node for on that occurrence (same verse, occurrence, surface, Strong's code, collection) is not added again.
Not in this step, counted: the nodes whose observation has no collection-bearing node in the verse (the verse's own collection words are a guess about
which surface it supports; for the researcher). Each set value and each added node is logged in ib_observation_change. Stops and rolls back unless the
counts equal the prediction.
    python iba/app/migration/node_supportive_collection_2484_v1_20261113.py [--db PATH] [--dry-run] [--limit N]
"""
import argparse
import collections
import datetime
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionexport as cx  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2484-SUPPORTIVE-COLLECTION-20261113"
R_SET = ("node rules B:130: the node's surface is not in a collection and supports the collection surface(s) of its observation in this verse; it takes "
         "the collection of the surface it supports, a node for each when there are several (researcher rulings of 2026-11-13, #2484)")
R_ADD = ("node rules B:130: node added for the other collection of the surface(s) this node supports in the verse (a copy of node {src}); one node for each "
         "collection (researcher ruling 4.1 of 2026-11-13, #2484)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    one = lambda s: conn.execute(s).fetchone()[0]
    cols = [r[1] for r in conn.execute("PRAGMA table_info(ib_node)")]
    skip = {"id", "seq", "created_at", "traced_observation_id", "collection_id", "deleted"}

    tiers = ["core", "synonym", "opposite", "gathered", "phrase"]
    terms = {r[0]: tuple(r) for r in conn.execute("SELECT id, surface, origin, surface_group, group_state, base_id FROM surface_term WHERE deleted=0")}
    live_cols = {r[0] for r in conn.execute("SELECT id FROM collection WHERE deleted=0 AND status='confirmed'")}
    sc = collections.defaultdict(set)
    for sid, ms in cx._memberships(conn, terms, tiers, own_link=True).items():
        for cid, _, status, _ in ms:
            if cid in live_cols and status == "confirmed":
                sc[(terms[sid][1] or "").strip().lower()].add(cid)
    inscope = set()
    for s, osis in conn.execute("SELECT lower(trim(vl.surface)), v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0"):
        if s in sc:
            inscope.add(osis)
    live = conn.execute("SELECT * FROM ib_node WHERE deleted=0 ORDER BY id").fetchall()
    by = collections.defaultdict(list)
    taken = set()
    for n in live:
        by[n["observation_id"]].append(n)
        if n["collection_id"] is not None:
            taken.add((n["observation_id"], n["verse_reference"], n["verse_lexical_id"], n["surface"], n["strong"], n["collection_id"]))
    plan, no_sibling = [], 0
    for n in live:
        s = (n["surface"] or "").strip().lower()
        if n["collection_id"] is not None or not s or s in sc or n["verse_reference"] not in inscope:
            continue
        cs = sorted({x["collection_id"] for x in by[n["observation_id"]] if x["collection_id"] is not None and x["verse_reference"] == n["verse_reference"]})
        if cs:
            plan.append((n, cs))
        else:
            no_sibling += 1
    if a.limit:
        plan = plan[:a.limit]
    sets, adds, dups = [], [], []
    for n, cs in plan:
        k = lambda cid: (n["observation_id"], n["verse_reference"], n["verse_lexical_id"], n["surface"], n["strong"], cid)  # noqa: E731
        free = [cid for cid in cs if k(cid) not in taken]
        if not free:
            dups.append(n)
            continue
        taken.add(k(free[0]))
        sets.append((n, free[0], len(cs)))
        for cid in free[1:]:
            taken.add(k(cid))
            adds.append((n, cid))
    live_nodes, changes = one("SELECT count(*) FROM ib_node WHERE deleted=0"), one("SELECT count(*) FROM ib_observation_change")
    nocol = one("SELECT count(*) FROM ib_node WHERE deleted=0 AND collection_id IS NULL AND trim(coalesce(surface,''))<>''")
    pred = dict(collection_set=len(sets), nodes_added=len(adds), withdrawn_as_duplicate=len(dups), live_nodes_after=live_nodes + len(adds) - len(dups),
                changes_after=changes + len(sets) + 2 * len(adds) + len(dups))
    print("predicted:", pred, "| no collection-bearing sibling in the verse (left for the researcher):", no_sibling,
          "| no-collection nodes now", nocol)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute("SAVEPOINT w")
    try:
        for n, cid, k in sets:
            orec.log(conn, n["observation_id"], n["id"], "collection_id", None, cid, R_SET, None, RUN_ID, "Claude")
            conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (cid, n["id"]))
        for n, cid in adds:
            seq = conn.execute("SELECT COALESCE(MAX(seq),0)+1 FROM ib_node WHERE observation_id=?", (n["observation_id"],)).fetchone()[0]
            use = [c for c in cols if c not in skip]
            vals = [n[c] for c in use] + [seq, now, cid, 0]
            nid = conn.execute("INSERT INTO ib_node (%s) VALUES (%s)" % (",".join(use + ["seq", "created_at", "collection_id", "deleted"]),
                                                                          ",".join("?" * len(vals))), vals).lastrowid
            orec.log(conn, n["observation_id"], nid, "created", None, cid, R_ADD.format(src=n["id"]), None, RUN_ID, "Claude")
            orec.log(conn, n["observation_id"], nid, "collection_id", None, cid, R_SET, None, RUN_ID, "Claude")
        for n in dups:
            orec.delete_node(conn, n["id"], "duplicate node: the observation already has a live node on this occurrence in each collection it supports; "
                             "withdrawn (node rules B:130, ruling 4.1 of 2026-11-13, #2484)", None, RUN_ID, "Claude")
        got = dict(collection_set=len(sets), nodes_added=len(adds), withdrawn_as_duplicate=len(dups),
                   live_nodes_after=one("SELECT count(*) FROM ib_node WHERE deleted=0"), changes_after=one("SELECT count(*) FROM ib_observation_change"))
        seen = collections.Counter()
        for r in conn.execute("SELECT observation_id, verse_reference, verse_lexical_id, surface, strong, collection_id FROM ib_node WHERE deleted=0"):
            seen[tuple(r)] += 1
        dup = sum(v - 1 for v in seen.values() if v > 1)
        left = one("SELECT count(*) FROM ib_node WHERE deleted=0 AND collection_id IS NULL AND trim(coalesce(surface,''))<>''")
        print("actual:   ", got, "| duplicates:", dup, "| no-collection nodes left:", left)
        if got != pred or dup or left != nocol - len(sets) - len(dups):
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
