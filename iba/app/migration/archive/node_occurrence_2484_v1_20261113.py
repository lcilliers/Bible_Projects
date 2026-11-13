"""node_occurrence_2484_v1_20261113.py -- escalation #2484, second fix class (nodes with no verse_lexical_id, behaviour rule B:130 N-no-occurrence).

Researcher, 2026-11-13: 'Missing occurrences next'; missing columns that can be derived from the context of the node need no re-read (ruling 4.3).
A live node with a surface and no verse_lexical_id takes the one live verse_lexical row of its verse (verse_reference = verse.osisId) whose surface,
Strong's code and morph code all equal the node's. Only that exact, single match is derived. Left alone and counted: the node whose surface occurs
more than once with the same codes in the verse (it needs a node for each occurrence, ruling 4.1: a decision), the node whose codes differ from every
occurrence of its surface in the verse (stale codes, ruling 4.5), and the surfaceless node. Where the derived key equals that of another live node of the
observation (same verse, verse_lexical_id, surface, Strong's code, collection) the node is the duplicate and is withdrawn (delete_node), the lowest id kept,
as in the duplicate step. Each set value is logged in ib_observation_change with its reason. Stops and rolls back unless the counts equal the prediction.
    python iba/app/migration/node_occurrence_2484_v1_20261113.py [--db PATH] [--dry-run] [--limit N]
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
RUN_ID = "DEVMODE-2484-NODE-OCCURRENCE-20261113"
SET_REASON = ("node rules B:130: a node names the verse_lexical occurrence it is about; derived from the node's own verse, surface, Strong's code and "
              "morph code, which match exactly one occurrence (researcher ruling 4.3 of 2026-11-13, #2484)")
DUP_REASON = ("duplicate node: once its occurrence is derived it has the same observation, verse, occurrence, surface, Strong's code and collection as "
              "node {keep}; a duplicate is withdrawn (node rules B:130, ruling 4.1 of 2026-11-13, #2484)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="pilot: only the first N derivable nodes (by id)")
    a = ap.parse_args()
    conn = sqlite3.connect(a.db)
    conn.row_factory = sqlite3.Row
    one = lambda s: conn.execute(s).fetchone()[0]

    occ = collections.defaultdict(list)
    for r in conn.execute("SELECT vl.id, v.osisId, vl.surface, vl.strong, vl.morph_code FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0"):
        occ[(r[1], r[2], r[3], r[4])].append(r[0])
    live = conn.execute("SELECT * FROM ib_node WHERE deleted=0 ORDER BY id").fetchall()
    taken = {}
    for n in live:
        if n["verse_lexical_id"] is not None:
            taken.setdefault((n["observation_id"], n["verse_reference"], n["verse_lexical_id"], n["surface"], n["strong"], n["collection_id"]), n["id"])
    derive, ambiguous, stale, surfaceless = [], 0, 0, 0
    for n in live:
        if n["verse_lexical_id"] is not None:
            continue
        s = (n["surface"] or "").strip()
        if not s:
            surfaceless += 1
            continue
        m = occ.get((n["verse_reference"], s, n["strong"], n["morph_code"]), [])
        if len(m) == 1:
            derive.append((n, m[0]))
        elif len(m) > 1:
            ambiguous += 1
        else:
            stale += 1
    if a.limit:
        derive = derive[:a.limit]
    sets, dups = [], []
    for n, vid in derive:
        k = (n["observation_id"], n["verse_reference"], vid, n["surface"], n["strong"], n["collection_id"])
        if k in taken:
            dups.append((n["id"], taken[k]))
        else:
            taken[k] = n["id"]
            sets.append((n, vid))
    live_nodes, changes = one("SELECT count(*) FROM ib_node WHERE deleted=0"), one("SELECT count(*) FROM ib_observation_change")
    pred = dict(occurrence_set=len(sets), withdrawn_as_duplicate=len(dups), live_nodes_after=live_nodes - len(dups),
                null_occurrence_after=one("SELECT count(*) FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NULL") - len(sets) - len(dups),
                changes_after=changes + len(sets) + len(dups))
    print("predicted:", pred)
    print("left alone: ambiguous (same codes occur more than once in the verse)", ambiguous, "| stale codes", stale, "| no surface", surfaceless)
    conn.execute("SAVEPOINT w")
    try:
        for n, vid in sets:
            orec.log(conn, n["observation_id"], n["id"], "verse_lexical_id", None, vid, SET_REASON, None, RUN_ID, "Claude")
            conn.execute("UPDATE ib_node SET verse_lexical_id=? WHERE id=?", (vid, n["id"]))
        wd = sum(1 for nid, keep in dups if orec.delete_node(conn, nid, DUP_REASON.format(keep=keep), None, RUN_ID, "Claude"))
        got = dict(occurrence_set=len(sets), withdrawn_as_duplicate=wd, live_nodes_after=one("SELECT count(*) FROM ib_node WHERE deleted=0"),
                   null_occurrence_after=one("SELECT count(*) FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NULL"),
                   changes_after=one("SELECT count(*) FROM ib_observation_change"))
        bad = one("SELECT count(*) FROM ib_node n JOIN verse_lexical vl ON vl.id=n.verse_lexical_id WHERE n.deleted=0 AND n.id IN "
                  f"(SELECT node_id FROM ib_observation_change WHERE run_id='{RUN_ID}' AND column_name='verse_lexical_id') AND (vl.surface<>n.surface OR vl.strong<>n.strong OR vl.morph_code<>n.morph_code)")
        print("actual:   ", got, "| set nodes that disagree with their occurrence:", bad)
        if got != pred or bad:
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
