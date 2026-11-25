"""temp_2538_old_observations_test_run.py -- the handling of old observations in the loop (escalation #2538; specification outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md, sections 2A, B1, B4;
lib/validationactions.py delete_neither, lib/buildvalidate.py _answer, carried_later, settle_row, row_problems).

Researcher 2026-11-25: "Deletion includes the node"; B1 clears the old observations in scope, a complex observation is carried forward to B2 and B3, B2 and B3 consider the carried ones first, the sweep takes the rest.
Each case runs the function on real rows of a COPY of iba.db, inside a savepoint that is rolled back, and checks the tables with a query written here.

Usage: python iba/app/tools/temp_2538_old_observations_test_run.py <db copy> [collection]
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import buildvalidate as bv  # noqa: E402
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import validationactions as va  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []
RUN = "TEST-2538-OLD"


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))
    print(f"[{results[-1][2]}] {cid}: {results[-1][3][:160]}", file=sys.stderr, flush=True)


def main(db, name="thought"):
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp)
    _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    cid, cname = ci._collection(conn, name)
    vl_all = [r[0] for r in conn.execute("SELECT vl.id FROM verse_lexical vl WHERE vl.deleted=0 AND lower(trim(vl.surface)) IN (SELECT lower(trim(t.surface)) FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.collection_id=? AND i.deleted=0)", (cid,))]
    home = set(vl_all)
    # old NULL observations with a live node on the collection's occurrences, no marker, no trace to them
    cand = []
    for i in range(0, len(vl_all), 400):
        ch = vl_all[i:i + 400]
        cand += [r[0] for r in conn.execute(f"SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature IS NULL AND o.stage NOT IN ('lexical','layer-1','layer-2','layer-3') "
                                          f"AND n.verse_lexical_id IN ({','.join('?' * len(ch))})", ch)]
    cand = sorted(set(cand))
    cand = [o for o in cand if not conn.execute("SELECT 1 FROM ib_node WHERE traced_observation_id=? AND deleted=0 LIMIT 1", (o,)).fetchone()]

    def split(o):
        here = [r[0] for r in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IN (%s)" % ",".join(str(x) for x in sorted(home)), (o,))] if False else None
        rows = conn.execute("SELECT id, verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL", (o,)).fetchall()
        return [r[0] for r in rows if r[1] in home], [r[0] for r in rows if r[1] not in home]
    own = next((o for o in cand if split(o)[0] and not split(o)[1]), None)
    shared = next((o for o in cand if split(o)[0] and split(o)[1]), None)
    case("O0", "the copy holds an old unmarked observation held only here, and (if any) one held also elsewhere", own is not None, f"only here {own}; also elsewhere {shared}; {len(cand)} candidates")
    conn.execute("SAVEPOINT oldtest")
    try:
        if own is not None:
            nodes_before = [r[0] for r in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (own,))]
            va.delete_neither(cfg, conn, own, "test: states neither what the data show nor how the inner being works", RUN, "Claude")
            live_nodes = conn.execute("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0", (own,)).fetchone()[0]
            deleted = conn.execute("SELECT deleted FROM ib_observation WHERE id=?", (own,)).fetchone()[0]
            case("O1", "deleting an observation deletes its nodes (the observation is deleted and no live node is left of it)", deleted == 1 and live_nodes == 0, f"{len(nodes_before)} nodes before, {live_nodes} live after")
        if shared is not None:
            here, there = split(shared)
            va.delete_neither(cfg, conn, shared, "test: neither; this subgroup's nodes only", RUN, "Claude", node_ids=here)
            live_here = conn.execute(f"SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0 AND id IN ({','.join('?' * len(here))})", [shared] + here).fetchone()[0]
            live_there = conn.execute(f"SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0 AND id IN ({','.join('?' * len(there))})", [shared] + there).fetchone()[0]
            alive = conn.execute("SELECT deleted FROM ib_observation WHERE id=?", (shared,)).fetchone()[0] == 0
            case("O2", "an observation held also by another subgroup or collection loses only the nodes here and stays live for the others", live_here == 0 and live_there == len(there) and alive, f"here {len(here)} gone, elsewhere {len(there)} kept, observation live {alive}")
        else:
            case("O2", "an observation held also elsewhere loses only the nodes here", None, "no such observation on this copy")
        # carry forward
        target = next((o for o in cand if o != own and o != shared), None)
        if target is not None:
            def act(step, to, reason="test: states a structure; B3 is to consider it first"):
                bv._answer(cfg, conn, target, {"action": "carry", "to": to, "reason": reason}, [], RUN, {}, None, step)
            act("S1", "2.1")
            case("O3", "carry forward records carried_to; the observation is not asked at a step before its own, and is asked at its own", target in bv.carried_later(conn, [target], "1.1") and target not in bv.carried_later(conn, [target], "2.1"), "carried S1 to 2.1")
            refused = []
            for step, to in (("2.1", "2.1"), ("2.1", "1.1"), ("sweep", "sweep"), ("3.1", "sweep")):
                try:
                    act(step, to)
                    refused.append((step, to, "accepted"))
                except va.Refused:
                    refused.append((step, to, "refused"))
            case("O4", "carry names a LATER step than the one answering; the sweep and stage 4 cannot carry", all(r[2] == "refused" for r in refused), refused)
            s_ = {}
            vl = [r[0] for r in conn.execute("SELECT verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_lexical_id IS NOT NULL", (target,))]
            problem_s1 = bv.row_problems(conn, cfg, __import__("iba.app.lib.layerreading", fromlist=["x"]).settings(cfg), cid, [], 0, "S1")
            case("O5", "the sweep list still holds a carried observation (it is unmarked and not settled)", target in bv.unmarked_in(conn, cfg, __import__("iba.app.lib.layerreading", fromlist=["x"]).settings(cfg), vl), f"{len(vl)} occurrences")
        else:
            case("O3", "carry forward", None, "no spare candidate on this copy")
        # ── the repairs the evidence validation makes before it judges
        lrmod = __import__("iba.app.lib.layerreading", fromlist=["x"])
        s_ = lrmod.settings(cfg)
        from iba.app.lib import collectionvalidate as cv_
        cols = cv_.settings(cfg)["word_columns"]
        miss_sql = " OR ".join(f"{c} IS NULL" for c in cols)
        bad = [tuple(r) for r in conn.execute(f"SELECT id, verse_lexical_id FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND disposition_note IS NULL AND verse_lexical_id IN (SELECT value FROM json_each(?)) AND ({miss_sql}) LIMIT 300", (json.dumps(vl_all[:2000]),))]
        if bad:
            vls_bad = sorted({r[1] for r in bad})
            before = len(bad)
            out = bv.complete_nodes(conn, cfg, s_, vls_bad, cid, RUN)
            still = conn.execute(f"SELECT count(*) FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND disposition_note IS NULL AND id IN ({','.join(str(r[0]) for r in bad)}) AND ({miss_sql})").fetchone()[0]
            logged = conn.execute("SELECT count(*) FROM ib_observation_change WHERE run_id=? AND (reason LIKE 'completed from the data%' OR column_name='disposition_note')", (RUN,)).fetchone()[0]
            case("O6", "a word node that lacks a required column is completed from the data where the data give it, or its reason is written on it; every change is logged; none is left unexplained", still == 0 and logged > 0, f"{before} nodes lacked a column; {out}; {logged} changes logged; {still} left")
        else:
            case("O6", "a word node that lacks a required column is completed or explained", None, "no such node on this copy")
        un = [r[0] for r in conn.execute(f"SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE n.deleted=0 AND o.deleted=0 AND o.nature IS NULL AND n.verse_lexical_id IN (SELECT value FROM json_each(?)) LIMIT 50", (json.dumps(vl_all[:2000]),))]
        if un:
            out2 = bv.mark_builds(conn, cfg, s_, vl_all[:2000], cid, RUN)
            left = conn.execute(f"SELECT count(*) FROM ib_observation WHERE nature IS NULL AND deleted=0 AND id IN ({','.join(map(str, un))})").fetchone()[0]
            case("O7", "an unmarked observation of the loop's own kind is marked by the item that wrote it, and deferred to its collection where it belongs to another", left == 0 and out2["builds_marked"] >= len(un), f"{len(un)} unmarked builds; {out2}")
        else:
            case("O7", "an unmarked build observation is marked by its item", None, "none on this copy")
    finally:
        conn.execute("ROLLBACK TO oldtest")
        conn.execute("RELEASE oldtest")
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{sum(1 for r in results if r[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r[2] != "FAIL" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
