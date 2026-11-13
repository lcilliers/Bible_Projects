"""node_occurrences_each_2484_v1_20261113.py -- escalation #2484, second fix class, the repeated words (node rules B:130, ruling 4.1).

Researcher, 2026-11-13: 'One per occurrence'. A live node with a surface and no verse_lexical_id whose verse, surface, Strong's code and morph code
match k >= 2 live verse_lexical rows (the same word written more than once in the verse) is tied to the first of them (lowest position, then id), and
a node is added for each of the other k-1, copying every column of the node (observation, codes, collection, role, disposition, source stage, cluster
history) except id, seq (next in the observation), created_at, traced_observation_id and verse_lexical_id. An occurrence the observation already has a
live node for (same verse, occurrence, surface, Strong's code, collection) is not added again. Each set value and each added node is logged in
ib_observation_change with its reason. Stops and rolls back unless the counts equal the prediction.
    python iba/app/migration/node_occurrences_each_2484_v1_20261113.py [--db PATH] [--dry-run] [--limit N]
"""
import argparse
import collections
import datetime
import pathlib
import sqlite3
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.lib import observationrecord as orec  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2484-NODE-OCCURRENCES-EACH-20261113"
SET_REASON = ("node rules B:130: the word is written {k} times in the verse with the same codes; the node is tied to the first occurrence and a node is "
              "added for each other (researcher ruling 4.1 of 2026-11-13, one per occurrence, #2484)")
ADD_REASON = ("node rules B:130: node added for another occurrence of the same word in the verse (a copy of node {src}); one node for each occurrence "
              "(researcher ruling 4.1 of 2026-11-13, #2484)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="pilot: only the first N nodes (by id)")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    one = lambda s: conn.execute(s).fetchone()[0]
    cols = [r[1] for r in conn.execute("PRAGMA table_info(ib_node)")]
    skip = {"id", "seq", "created_at", "traced_observation_id", "verse_lexical_id", "deleted"}

    occ = collections.defaultdict(list)
    for r in conn.execute("SELECT vl.id, v.osisId, vl.surface, vl.strong, vl.morph_code FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
                          "WHERE vl.deleted=0 ORDER BY vl.position, vl.id"):
        occ[(r[1], r[2], r[3], r[4])].append(r[0])
    live = conn.execute("SELECT * FROM ib_node WHERE deleted=0 ORDER BY id").fetchall()
    taken = {(n["observation_id"], n["verse_reference"], n["verse_lexical_id"], n["surface"], n["strong"], n["collection_id"]) for n in live
             if n["verse_lexical_id"] is not None}
    plan = []
    for n in live:
        s = (n["surface"] or "").strip()
        if n["verse_lexical_id"] is not None or not s:
            continue
        m = occ.get((n["verse_reference"], s, n["strong"], n["morph_code"]), [])
        if len(m) >= 2:
            plan.append((n, m))
    if a.limit:
        plan = plan[:a.limit]
    sets, adds = [], []
    for n, m in plan:
        sets.append((n, m[0], len(m)))
        taken.add((n["observation_id"], n["verse_reference"], m[0], n["surface"], n["strong"], n["collection_id"]))
        for vid in m[1:]:
            k = (n["observation_id"], n["verse_reference"], vid, n["surface"], n["strong"], n["collection_id"])
            if k not in taken:
                taken.add(k)
                adds.append((n, vid))
    live_nodes, changes = one("SELECT count(*) FROM ib_node WHERE deleted=0"), one("SELECT count(*) FROM ib_observation_change")
    nulls = one("SELECT count(*) FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NULL")
    pred = dict(occurrence_set=len(sets), nodes_added=len(adds), live_nodes_after=live_nodes + len(adds), null_occurrence_after=nulls - len(sets),
                changes_after=changes + len(sets) + len(adds))
    print("predicted:", pred)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute("SAVEPOINT w")
    try:
        for n, vid, k in sets:
            orec.log(conn, n["observation_id"], n["id"], "verse_lexical_id", None, vid, SET_REASON.format(k=k), None, RUN_ID, "Claude")
            conn.execute("UPDATE ib_node SET verse_lexical_id=? WHERE id=?", (vid, n["id"]))
        for n, vid in adds:
            seq = conn.execute("SELECT COALESCE(MAX(seq),0)+1 FROM ib_node WHERE observation_id=?", (n["observation_id"],)).fetchone()[0]
            use = [c for c in cols if c not in skip]
            vals = [n[c] for c in use] + [seq, now, vid, 0]
            nid = conn.execute("INSERT INTO ib_node (%s) VALUES (%s)" % (",".join(use + ["seq", "created_at", "verse_lexical_id", "deleted"]),
                                                                          ",".join("?" * len(vals))), vals).lastrowid
            orec.log(conn, n["observation_id"], nid, "created", None, vid, ADD_REASON.format(src=n["id"]), None, RUN_ID, "Claude")
        got = dict(occurrence_set=len(sets), nodes_added=len(adds), live_nodes_after=one("SELECT count(*) FROM ib_node WHERE deleted=0"),
                   null_occurrence_after=one("SELECT count(*) FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NULL"),
                   changes_after=one("SELECT count(*) FROM ib_observation_change"))
        bad = one("SELECT count(*) FROM ib_node n JOIN verse_lexical vl ON vl.id=n.verse_lexical_id WHERE n.deleted=0 AND n.id IN "
                  f"(SELECT node_id FROM ib_observation_change WHERE run_id='{RUN_ID}') AND (vl.surface<>n.surface OR vl.strong<>n.strong OR vl.morph_code<>n.morph_code)")
        seen = collections.Counter()
        for r in conn.execute("SELECT observation_id, verse_reference, verse_lexical_id, surface, strong, collection_id FROM ib_node WHERE deleted=0"):
            seen[tuple(r)] += 1
        dup = sum(v - 1 for v in seen.values() if v > 1)
        print("actual:   ", got, "| nodes that disagree with their occurrence:", bad, "| duplicates:", dup)
        if got != pred or bad or dup:
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
