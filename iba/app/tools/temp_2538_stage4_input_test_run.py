"""temp_2538_stage4_input_test_run.py -- the input of stage 4 is chosen by the marker, partner collections are read, and the 3.3 gate (escalation #2538; specification
outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md, C1 to C3; lib/layerinner.py _sources, derive; lib/buildvalidate.py partner_gaps).

Each case compares the library's answer with a query written here, on a COPY of iba.db (never the live database).

Usage: python iba/app/tools/temp_2538_stage4_input_test_run.py <db copy> [collection]
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import buildvalidate as bv  # noqa: E402
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import layerinner as li  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed is True else ("BLOCKED" if passed is None else "FAIL"), str(evidence).replace("|", "/")[:330]))
    print(f"[{results[-1][2]}] {cid}: {results[-1][3][:160]}", file=sys.stderr, flush=True)


def main(db, name="thought"):
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp)
    _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    s = lr.settings(cfg)
    cid, cname = ci._collection(conn, name)
    sd31, sd32, sd33 = (lr.step_def(s, k) for k in ("3.1", "3.2", "3.3"))
    L = lr.load(conn, cfg, name, pairs=True)
    gid = max(L["groups"], key=lambda g: sum(1 for o in L["d"]["occurrences"] if o["group"] == g))
    vls = [o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid]
    ph = ",".join("?" * len(vls))
    # ── 3.1: the evidence observations of the subgroup, by marker, any stage
    ev_ind = {r[0] for r in q(f"SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND n.traced_observation_id IS NULL AND o.nature='evidence' AND n.verse_lexical_id IN ({ph})", *vls)}
    src, req = li._sources(conn, s, L, sd31, gid)
    case("I1", "3.1 may rest on every evidence observation with a node on the subgroup's occurrences, whatever its stage (equal to an independent query)", src == ev_ind and bool(ev_ind), f"{len(src)} evidence observations; stages {sorted({r[0] for r in q('SELECT stage FROM ib_observation WHERE id IN (%s)' % ','.join(map(str, sorted(src))))})}")
    case("I2", "3.1 takes up those not already carried by a sense (a word observation a layer-1 observation traces is rested on through the sense)", req <= src and (src - req) <= {x for x in src if q("SELECT stage FROM ib_observation WHERE id=?", x)[0][0] == "lexical"}, f"{len(req)} to take up of {len(src)}")
    # ── 3.2: all the inner-being observations of the collection by marker
    ib_ind = {r[0] for r in q("SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature='inner_being' AND n.collection_id=?", cid)}
    own = {r[0] for r in q("SELECT DISTINCT o.id FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE o.deleted=0 AND c.collection_id=? AND c.step IN ('3.2','3.3')", cid)}
    src2, req2 = li._sources(conn, s, L, sd32, 0)
    case("I3", "3.2 rests on and takes up ALL the inner-being observations of the collection by marker (the older ones kept as inner being too), less its own and 3.3's", src2 == req2 == ib_ind - own, f"{len(src2)} observations; {len(ib_ind)} inner_being in the collection")
    # ── 3.3: one row for each unique match across the observations whose nodes reference more than one collection (researcher 2026-11-25)
    ms = li.matches(conn, L)
    # an independent query: the live observations with a node of this collection and a node of another collection IN THE SAME VERSE (a pairing in a verse), 3.3's own left out
    ind = set()
    wrote33 = {r[0] for r in q("SELECT DISTINCT o.id FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE o.deleted=0 AND c.step='3.3'")}      # 3.3 reads the others, not its own
    for oid, ref, col, sf, st in q("SELECT n.observation_id, n.verse_reference, n.collection_id, lower(n.surface), n.strong FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND n.traced_observation_id IS NULL "
                                   "AND n.verse_lexical_id IS NOT NULL AND n.collection_id IS NOT NULL AND n.observation_id IN (SELECT observation_id FROM ib_node WHERE collection_id=? AND deleted=0)", cid):
        if oid not in wrote33:
            ind.add((oid, ref, col, sf, st))
    names = {v: k for k, v in L["col_ids"].items()}
    mine_by, oth_by = {}, {}
    for oid, ref, col, sf, st in ind:
        (mine_by if col == cid else oth_by).setdefault((oid, ref), set()).add((col, sf, st))
    want = {}
    for k, mset in mine_by.items():
        for (c1, sa, ta) in mset:
            for (c2, sb, tb) in oth_by.get(k, ()):
                want.setdefault(li.match_subject(sa, ta, names.get(c2, str(c2)), sb, tb), set()).add(k[0])
    case("I4", "3.3 has ONE row for each unique match: each distinct pairing of a word of this collection with a word of another collection that the nodes of an observation place together in a verse (equal to an independent query, with the source observations)",
         set(ms) == set(want) and all(ms[k]["sources"] == want[k] for k in want) and bool(want), f"{len(ms)} matches from {len({o for v in ms.values() for o in v['sources']})} observations; independent {len(want)}")
    rows33 = li.derive(conn, cfg, L, "3.3")
    case("I5", "the rows of 3.3 are exactly those matches: no minimum number of shared verses, no cap, nothing for words without a pairing", {r["subject"] for r in rows33} == set(ms) and len(rows33) == len(ms), f"{len(rows33)} rows")
    if ms:
        subj = sorted(ms)[0]
        src3, req3 = li._sources(conn, s, L, sd33, 0, subj)
        case("I6", "a match may rest on, and must trace, every observation it comes from (any nature); and its nodes are the occurrences of both sides", src3 == req3 == ms[subj]["sources"] and {o["vl_id"] for o in li.demanded(L, "interworking", 0, subj, conn)} == ms[subj]["occurrences"],
             f"{subj}: {len(req3)} observations, {len(ms[subj]['occurrences'])} occurrences")
    else:
        case("I6", "a match traces every observation it comes from", None, "no cross-collection observation on this copy")
    gaps = li.cross_gaps(conn, L)
    # make a gap: a word node of this collection's pairing or 3.2 observation with its collection removed
    row = q("SELECT n.id, n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE n.deleted=0 AND o.deleted=0 AND c.collection_id=? AND (c.item='pairing' OR c.step='3.2') AND n.traced_observation_id IS NULL AND n.verse_lexical_id IS NOT NULL AND n.collection_id IS NOT NULL LIMIT 1", cid)
    if row:
        conn.execute("UPDATE ib_node SET collection_id=NULL WHERE id=?", (row[0][0],))
        gaps2 = li.cross_gaps(conn, L)
        case("I7", "an observation of this collection's pairings or 3.2 whose node carries no collection is named before 3.3 opens (3.3 cannot extract the match from it)", len(gaps2) == len(gaps) + 1 and any(f"observation {row[0][1]}:" in g for g in gaps2), f"{len(gaps)} gaps before, {len(gaps2)} after")
    else:
        case("I7", "an observation whose node carries no collection is named before 3.3 opens", None, "this copy holds no pairing or 3.2 observation of the collection")
    case("I8", "the configuration holds no minimum for 3.3, no cap on the verses 3.1 shows, and the researcher's list of complete partners", "pair_min_verses" not in s["thresholds"] and "pull_verse_texts" not in s and s.get("partner_complete") == [], list(s["thresholds"]))
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{sum(1 for r in results if r[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r[2] != "FAIL" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
