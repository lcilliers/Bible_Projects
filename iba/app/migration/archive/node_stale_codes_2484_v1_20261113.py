"""node_stale_codes_2484_v1_20261113.py -- escalation #2484, third fix class: the nodes whose stored morph code is stale (ruling 4.5).

Researcher, 2026-11-13: 'Reset stale codes' (ruling 4.5: reset the stale columns that have no valid, current data). A live node with a surface and
no verse_lexical_id whose verse, surface and Strong's code match live verse_lexical rows but whose morph code matches none:
  - one such occurrence: the node takes its verse_lexical_id and the occurrence's morph code;
  - several such occurrences that all carry one morph code (the repeated word): the same, tied to the first (lowest position), and a node added for each
    other occurrence (ruling 4.1, as in the step before), the morph code reset on each.
Held back and counted (a reading decides): the several occurrences that carry different morph codes (which one is meant is not in the node), and the node
whose Strong's code differs from every occurrence of its surface. Each old value, new value and added node is logged in ib_observation_change.
Stops and rolls back unless the counts equal the prediction.
    python iba/app/migration/node_stale_codes_2484_v1_20261113.py [--db PATH] [--dry-run]
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
RUN_ID = "DEVMODE-2484-NODE-STALE-CODES-20261113"
R_OCC = ("node rules B:130: the node's verse, surface and Strong's code match this occurrence (the word is written {k} time(s) in the verse, one node for "
         "each occurrence); its stored morph code was stale (researcher rulings 4.5 and 4.1 of 2026-11-13, #2484)")
R_MORPH = "stale morph code reset from the occurrence it is about (researcher ruling 4.5 of 2026-11-13, #2484); stored {old}, the verse has {new}"
R_ADD = ("node rules B:130: node added for another occurrence of the same word in the verse (a copy of node {src}); one node for each occurrence "
         "(researcher ruling 4.1 of 2026-11-13, #2484)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    one = lambda s: conn.execute(s).fetchone()[0]
    cols = [r[1] for r in conn.execute("PRAGMA table_info(ib_node)")]
    skip = {"id", "seq", "created_at", "traced_observation_id", "verse_lexical_id", "deleted", "morph_code"}

    live = conn.execute("SELECT * FROM ib_node WHERE deleted=0 ORDER BY id").fetchall()
    taken = {(n["observation_id"], n["verse_reference"], n["verse_lexical_id"], n["surface"], n["strong"], n["collection_id"]) for n in live
             if n["verse_lexical_id"] is not None}
    plan, held = [], []
    for n in live:
        s = (n["surface"] or "").strip()
        if n["verse_lexical_id"] is not None or not s:
            continue
        q = conn.execute("SELECT vl.id, vl.strong, vl.morph_code FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE v.osisId=? AND vl.deleted=0 "
                         "AND vl.surface=? ORDER BY vl.position, vl.id", (n["verse_reference"], s)).fetchall()
        if any(x["strong"] == n["strong"] and x["morph_code"] == n["morph_code"] for x in q):
            continue                                   # not stale: the occurrence step handles it
        sm = [x for x in q if x["strong"] == n["strong"]]
        if sm and len({x["morph_code"] for x in sm}) == 1:
            plan.append((n, sm))
        else:
            held.append(n["id"])
    sets, adds, dups = [], [], []
    for n, m in plan:
        k0 = (n["observation_id"], n["verse_reference"], m[0]["id"], n["surface"], n["strong"], n["collection_id"])
        if k0 in taken:
            dups.append(n)
        else:
            taken.add(k0)
            sets.append((n, m[0], len(m)))
        for x in m[1:]:
            k = (n["observation_id"], n["verse_reference"], x["id"], n["surface"], n["strong"], n["collection_id"])
            if k not in taken:
                taken.add(k)
                adds.append((n, x))
    live_nodes, changes = one("SELECT count(*) FROM ib_node WHERE deleted=0"), one("SELECT count(*) FROM ib_observation_change")
    nulls = one("SELECT count(*) FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NULL")
    pred = dict(occurrence_set=len(sets), nodes_added=len(adds), withdrawn_as_duplicate=len(dups),
                live_nodes_after=live_nodes + len(adds) - len(dups), null_occurrence_after=nulls - len(sets) - len(dups),
                changes_after=changes + 2 * len(sets) + 2 * len(adds) + len(dups))
    print("predicted:", pred, "| held back for a reading:", len(held), held)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute("SAVEPOINT w")
    try:
        for n, x, k in sets:
            orec.log(conn, n["observation_id"], n["id"], "verse_lexical_id", None, x["id"], R_OCC.format(k=k), None, RUN_ID, "Claude")
            orec.log(conn, n["observation_id"], n["id"], "morph_code", n["morph_code"], x["morph_code"],
                     R_MORPH.format(old=n["morph_code"], new=x["morph_code"]), None, RUN_ID, "Claude")
            conn.execute("UPDATE ib_node SET verse_lexical_id=?, morph_code=? WHERE id=?", (x["id"], x["morph_code"], n["id"]))
        for n, x in adds:
            seq = conn.execute("SELECT COALESCE(MAX(seq),0)+1 FROM ib_node WHERE observation_id=?", (n["observation_id"],)).fetchone()[0]
            use = [c for c in cols if c not in skip]
            vals = [n[c] for c in use] + [seq, now, x["id"], x["morph_code"], 0]
            nid = conn.execute("INSERT INTO ib_node (%s) VALUES (%s)" % (",".join(use + ["seq", "created_at", "verse_lexical_id", "morph_code", "deleted"]),
                                                                          ",".join("?" * len(vals))), vals).lastrowid
            orec.log(conn, n["observation_id"], nid, "created", None, x["id"], R_ADD.format(src=n["id"]), None, RUN_ID, "Claude")
            orec.log(conn, n["observation_id"], nid, "morph_code", n["morph_code"], x["morph_code"],
                     R_MORPH.format(old=n["morph_code"], new=x["morph_code"]), None, RUN_ID, "Claude")
        for n in dups:
            orec.delete_node(conn, n["id"], "duplicate node: its occurrence is the one another live node of the observation already has; withdrawn "
                             "(node rules B:130, ruling 4.1 of 2026-11-13, #2484)", None, RUN_ID, "Claude")
        got = dict(occurrence_set=len(sets), nodes_added=len(adds), withdrawn_as_duplicate=len(dups),
                   live_nodes_after=one("SELECT count(*) FROM ib_node WHERE deleted=0"),
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
