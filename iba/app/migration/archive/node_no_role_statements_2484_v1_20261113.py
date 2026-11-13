"""node_no_role_statements_2484_v1_20261113.py -- escalation #2484, fifth fix class, step 1: the 'no inner-being role' statements (ruling 4.2).

Researcher, 2026-11-13: 'B, start with the pilot of 30'. Ruling 4.2: a node of a surface that has no role to play records that the word was recognised
and decided as having no inner-being role on any other surface in the verse; its role is standalone. Such a node supports every collection surface of its
verse, so it is tied to each collection of the member surfaces in the verse (a node for each, ruling 4.1).
The class: a live node with a surface that is in no collection, in a verse that holds a member surface, with no collection and no role, whose observation
states that no inner-being operation / role is named (text matching "no (human )?inner-being (operation|role|content)"), and whose observation has
no collection-bearing node in that verse. Each node of the class: role standalone, the lowest collection id of the verse on the node, and a node added for each
other collection (a copy of the node's columns except id, seq, created_at, traced_observation_id, collection_id). Each set value and added node is logged
in ib_observation_change. --pilot N takes N nodes spread evenly over the class (by id). Stops and rolls back unless the counts equal the prediction.
    python iba/app/migration/node_no_role_statements_2484_v1_20261113.py [--db PATH] [--dry-run] [--pilot N]
"""
import argparse
import collections
import datetime
import pathlib
import re
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionexport as cx  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2484-NO-ROLE-STATEMENTS-20261113"
PAT = re.compile(r"no (human )?inner[- ]being (operation|role|content)", re.I)
R_ROLE = ("node rules B:130, ruling 4.2: the observation states that no inner-being operation is named for the word, so the node records that the word was "
          "recognised and decided as having no role on any other surface in the verse: role standalone (researcher, 2026-11-13, #2484)")
R_COL = ("node rules B:130: a node that decides a word has no role supports every collection surface of its verse; it takes a collection of the verse, a node "
         "for each (researcher rulings 4.2 and 4.1 of 2026-11-13, #2484)")
R_ADD = ("node rules B:130: node added for another collection of the verse (a copy of node {src}); one node for each collection (researcher ruling 4.1 of "
         "2026-11-13, #2484)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--pilot", type=int, default=0)
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
    vcol = collections.defaultdict(set)
    for s, osis in conn.execute("SELECT lower(trim(vl.surface)), v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0"):
        if s in sc:
            vcol[osis] |= sc[s]
    text = {r[0]: r[1] or "" for r in conn.execute("SELECT id, obs_text FROM ib_observation WHERE deleted=0")}
    live = conn.execute("SELECT * FROM ib_node WHERE deleted=0 ORDER BY id").fetchall()
    by = collections.defaultdict(list)
    taken = set()
    for n in live:
        by[n["observation_id"]].append(n)
        if n["collection_id"] is not None:
            taken.add((n["observation_id"], n["verse_reference"], n["verse_lexical_id"], n["surface"], n["strong"], n["collection_id"]))
    cls = []
    for n in live:
        s = (n["surface"] or "").strip().lower()
        if n["collection_id"] is not None or n["role"] or not s or s in sc or n["verse_reference"] not in vcol:
            continue
        if not PAT.search(text.get(n["observation_id"], "")):
            continue
        if any(x["collection_id"] is not None and x["verse_reference"] == n["verse_reference"] for x in by[n["observation_id"]]):
            continue
        cls.append(n)
    total_class = len(cls)
    if a.pilot and a.pilot < len(cls):
        step = len(cls) / a.pilot
        cls = [cls[int(i * step)] for i in range(a.pilot)]
    sets, adds = [], []
    for n in cls:
        cs = sorted(vcol[n["verse_reference"]])
        k = lambda cid: (n["observation_id"], n["verse_reference"], n["verse_lexical_id"], n["surface"], n["strong"], cid)  # noqa: E731
        free = [cid for cid in cs if k(cid) not in taken]
        if not free:
            continue
        taken.add(k(free[0]))
        sets.append((n, free[0]))
        for cid in free[1:]:
            taken.add(k(cid))
            adds.append((n, cid))
    live_nodes, changes = one("SELECT count(*) FROM ib_node WHERE deleted=0"), one("SELECT count(*) FROM ib_observation_change")
    pred = dict(nodes_set=len(sets), nodes_added=len(adds), live_nodes_after=live_nodes + len(adds), changes_after=changes + 2 * len(sets) + 3 * len(adds))
    print("class size:", total_class, "| this run:", len(cls), "| predicted:", pred)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute("SAVEPOINT w")
    try:
        for n, cid in sets:
            orec.log(conn, n["observation_id"], n["id"], "role", None, "standalone", R_ROLE, None, RUN_ID, "Claude")
            orec.log(conn, n["observation_id"], n["id"], "collection_id", None, cid, R_COL, None, RUN_ID, "Claude")
            conn.execute("UPDATE ib_node SET role='standalone', collection_id=? WHERE id=?", (cid, n["id"]))
        for n, cid in adds:
            seq = conn.execute("SELECT COALESCE(MAX(seq),0)+1 FROM ib_node WHERE observation_id=?", (n["observation_id"],)).fetchone()[0]
            use = [c for c in cols if c not in skip and c != "role"]
            vals = [n[c] for c in use] + ["standalone", seq, now, cid, 0]
            nid = conn.execute("INSERT INTO ib_node (%s) VALUES (%s)" % (",".join(use + ["role", "seq", "created_at", "collection_id", "deleted"]),
                                                                          ",".join("?" * len(vals))), vals).lastrowid
            orec.log(conn, n["observation_id"], nid, "created", None, cid, R_ADD.format(src=n["id"]), None, RUN_ID, "Claude")
            orec.log(conn, n["observation_id"], nid, "role", None, "standalone", R_ROLE, None, RUN_ID, "Claude")
            orec.log(conn, n["observation_id"], nid, "collection_id", None, cid, R_COL, None, RUN_ID, "Claude")
        got = dict(nodes_set=len(sets), nodes_added=len(adds), live_nodes_after=one("SELECT count(*) FROM ib_node WHERE deleted=0"),
                   changes_after=one("SELECT count(*) FROM ib_observation_change"))
        seen = collections.Counter()
        for r in conn.execute("SELECT observation_id, verse_reference, verse_lexical_id, surface, strong, collection_id FROM ib_node WHERE deleted=0"):
            seen[tuple(r)] += 1
        dup = sum(v - 1 for v in seen.values() if v > 1)
        print("actual:   ", got, "| duplicates:", dup)
        if got != pred or dup:
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
