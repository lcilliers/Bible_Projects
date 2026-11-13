"""node_collection_2487_v1_20261112.py -- escalations #2484 and #2487: the collection on the node, first class.

Researcher, 2026-11-12: every observation node with a surface that is in a collection carries its collection; no link table (one
collection on the node); where a surface needs several collections the node would be repeated, and that class is NOT done here
(20,634 new nodes would result, most on words that sit in two or three overlapping collections: for the researcher).

1. Schema: ib_node.collection_id (INTEGER, references collection.id), registered in cfg_column through configmaint.apply_logged,
   then ALTER TABLE.
2. Fill: every live node with a surface whose surface is a member of exactly ONE collection (member tiers core, synonym, opposite,
   gathered, phrase; a link on the surface's own row or on its base) gets that collection_id; each change is kept in
   ib_observation_change (observationrecord.log) with the reason. Nodes in several collections, in none, or with no surface are not
   touched. Stops and rolls back unless the counts equal the prediction. Idempotent.
    python iba/app/migration/node_collection_2487_v1_20261112.py [--db PATH] [--dry-run]
"""
import argparse
import collections
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2487-NODE-COLLECTION-20261112"
TIERS = ("core", "synonym", "opposite", "gathered", "phrase")
REASON = ("the node's surface is a member of exactly one collection, so the node carries it "
          "(researcher ruling of 2026-11-12, #2484 and #2487 rule R11)")
COLUMN = {"database": "iba", "table_name": "ib_node", "name": "collection_id", "ordinal": 19, "type": "INTEGER", "is_pk": 0,
          "notnull": 0, "is_unique": 0, "dflt": None, "fk": "collection.id",
          "use": ("the collection the node belongs to (#2484, #2487; researcher 2026-11-12): the one collection of the node's surface "
                  "(its own row or its base is a member, tiers core, synonym, opposite, gathered or phrase of cfg_setting "
                  "collection.member_tiers). One collection per node: where a surface is in several, the node is not yet filled "
                  "(NULL) and that class waits for the researcher's ruling. NULL on a node with no surface, whose surface is in "
                  "no collection, or that is in several. cluster_code and cluster_subgroup_code are history, not analytic (R13)"),
          "expectation": None, "source": "escalations #2484 and #2487, the researcher's ruling of 2026-11-12",
          "filled_by": "iba/app/migration/archive/node_collection_2487_v1_20261112.py for the existing nodes", "inactive": 0}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    conn.row_factory = __import__("sqlite3").Row
    q = lambda s, *p: conn.execute(s, p).fetchall()
    one = lambda s: conn.execute(s).fetchone()[0]
    has_col = any(r[1] == "collection_id" for r in conn.execute("PRAGMA table_info(ib_node)"))

    cols = collections.defaultdict(set)
    for r in q("SELECT term_id, collection_id FROM collection_link WHERE deleted=0 AND tier IN (%s)" % ",".join("?" * len(TIERS)), *TIERS):
        cols[r[0]].add(r[1])
    st = collections.defaultdict(list)
    for r in q("SELECT id, surface, base_id FROM surface_term WHERE deleted=0"):
        st[r[1]].append((r[0], r[2]))

    def carry(s):
        o = set()
        for sid, b in st.get(s, []):
            o |= cols.get(sid, set()) | (cols.get(b, set()) if b else set())
        return o

    todo = []   # (node id, observation id, collection id)
    where_col = " AND collection_id IS NULL" if has_col else ""
    for r in q("SELECT id, observation_id, lower(trim(surface)) FROM ib_node WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>''" + where_col):
        c = carry(r[2])
        if len(c) == 1:
            todo.append((r[0], r[1], next(iter(c))))
    changes = one("SELECT count(*) FROM ib_observation_change")
    used = {r[0] for r in q("SELECT DISTINCT collection_id FROM ib_node WHERE collection_id IS NOT NULL")} if has_col else set()
    pred = dict(nodes_filled=len(todo), changes_after=changes + len(todo), collections_used=len(used | {t[2] for t in todo}))
    print("predicted:", pred, "| column exists:", has_col)
    if a.dry_run and not has_col:
        print("dry run: would register and add ib_node.collection_id, then fill")
        return 0
    conn.execute("SAVEPOINT w")
    try:
        if not has_col:
            apply_logged(conn, RUN_ID, "cfg_column", "insert", {}, COLUMN)
            conn.execute("ALTER TABLE ib_node ADD COLUMN collection_id INTEGER REFERENCES collection(id)")
        done = 0
        for nid, oid, col in todo:
            orec.log(conn, oid, nid, "collection_id", None, col, REASON, None, RUN_ID, "Claude")
            conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (col, nid))
            done += 1
        got = dict(nodes_filled=done, changes_after=one("SELECT count(*) FROM ib_observation_change"),
                   collections_used=one("SELECT count(DISTINCT collection_id) FROM ib_node WHERE collection_id IS NOT NULL"))
        print("actual:   ", got)
        reg = one("SELECT count(*) FROM cfg_column WHERE table_name='ib_node' AND name='collection_id' AND inactive=0")
        if got != pred or reg != 1:
            raise RuntimeError("actual differs from predicted or the column is not registered once: rolled back")
        if a.dry_run:
            conn.execute("ROLLBACK TO w"); print("dry run: rolled back")
        else:
            conn.execute("RELEASE w"); conn.commit(); print("committed")
    except Exception:
        conn.execute("ROLLBACK TO w"); conn.commit(); raise
    return 0


if __name__ == "__main__":
    sys.exit(main())
