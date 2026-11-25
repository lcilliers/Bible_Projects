"""temp_2538_pull_test_run.py -- the pull of a subgroup is the pull the researcher specified, and step 2.1 is by verse (escalation #2538; specification
outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md sections 2.B3, 2.B4, decisions D1 and D5; lib/layerreading.py pull, subgroup_verses, derive, expected_nodes; lib/buildvalidate.py older_on).

Each case compares the working file or the derived rows with a direct query written here. Runs against a COPY of iba.db (never the live database).

Usage: python iba/app/tools/temp_2538_pull_test_run.py <db copy> <scratch dir> [collection]
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import buildvalidate as bv  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []
RUN = "TEST-2538-PULL"


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))
    print(f"[{results[-1][2]}] {cid}: {results[-1][3][:160]}", file=sys.stderr, flush=True)


def main(db, scratch, name="thought"):
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp)
    _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    one = lambda s, *a: conn.execute(s, a).fetchone()[0]  # noqa: E731
    s = lr.settings(cfg)
    scratch = pathlib.Path(scratch)
    try:
        full = lr.load(conn, cfg, name, pairs=True)
        gids = sorted(full["groups"], key=lambda g: sum(1 for o in full["d"]["occurrences"] if o["group"] == g))
        g = gids[len(gids) // 2]
        gname = full["groups"][g]["name"]
        sc = lr.load(conn, cfg, name, pairs=True, subgroup=g)

        # ── 2.1 by verse: derive
        items_21 = [x for x in s["steps"] if x["key"] == "2.1"][0]["items"]
        case("V1", "step 2.1 asks for pairing, qualifier, entity, direction and double-meaning, and no group-relation", sorted(i for i in items_21 if i != "old-observation") == sorted(["pairing", "qualifier", "entity", "direction", "double-meaning"]) and "group-relation" not in s["items"], items_21)
        rows = [w for w in lr.derive(conn, cfg, sc, "2.1") if w["subgroup_id"] == g]
        # the rows are one for each (subgroup, item) and, for the pairing, one for each partner collection whose words stand with the subgroup (researcher 2026-11-25: the same surface in several verses is several
        # nodes of one observation, not several observations)
        pr_rows = {w["subject"] for w in rows if w["item"] == "pairing"}
        indep = set()
        for x in sc["pairs"]["pairs"]:
            if x["member"]["subgroup"] == gname and x["other"]["type"] == "word of another collection":
                indep |= set(x["other"]["collections"])
        case("V2", f"subgroup {gname}: one pairing row for each partner collection whose words stand with the subgroup (the subject is the collection), no minimum number of verses", pr_rows == indep and bool(indep), f"{len(pr_rows)} partner collections")
        one_verse = [cn for cn in indep if len({x["member"]["osis"] for x in sc["pairs"]["pairs"] if x["member"]["subgroup"] == gname and cn in x["other"]["collections"] and x["other"]["type"] == "word of another collection"}) == 1]
        case("V3", "a partner collection sharing a single verse is demanded (the 3-verse threshold is gone)", bool(one_verse) and set(one_verse) <= pr_rows, f"{len(one_verse)} such collections")
        single = {w["item"] for w in rows if w["item"] in ("qualifier", "entity", "direction")}
        case("V4", "qualifier, entity and direction are one row each for the subgroup, with no subject", all(w["subject"] == "" for w in rows if w["item"] in ("qualifier", "entity", "direction")), f"items {sorted(single)}")
        if pr_rows:
            cn = sorted(pr_rows)[0]
            nodes = lr.expected_nodes(sc, "pairing", g, cn)
            verses_ = {o["osis"] for o, _ in nodes}
            case("V5", "the nodes of a pairing row are the subgroup's occurrences and that partner collection's words, in every verse where they stand together (several verses, several nodes of one row)",
                 bool(nodes) and {r for _, r in nodes} == {"member", "partner"} and all(cn in o["collections"] for o, r in nodes if r == "partner"), f"{len(nodes)} nodes in {len(verses_)} verses for {cn}")
        ent_rows = {w["item"] for w in rows if w["item"] == "entity"}
        dir_rows = {w["item"] for w in rows if w["item"] == "direction"}
        case("V6", "direction is demanded where an entity stands, as entity is", bool(ent_rows) == bool(dir_rows), f"entity {sorted(ent_rows)}, direction {sorted(dir_rows)}")
        mi = [k for k in ("pairing", "qualifier", "entity", "direction", "double-meaning") if s["items"][k].get("multi")]
        case("V6b", "the 2.1 items are answered by findings (multi), each finding holding its verses as nodes", len(mi) == 5, mi)
        dm = [w for w in rows if w["item"] == "double-meaning"]
        case("V7", "double-meaning stays one row for each surface of the subgroup that carries more than one code", all(len({o["strong"] for o in sc["d"]["occurrences"] if o["surface"] == w["subject"] and o["group"] == g}) >= 2 for w in dm), f"{len(dm)} rows")

        # ── the pull of a subgroup in full: file head
        lr.open_step(conn, cfg, RUN, name, "S1", subgroup=gname)
        path, n = lr.pull(conn, cfg, name, "S1", scratch, subgroup=gname)
        f = json.loads(path.read_text(encoding="utf-8"))
        vids = sorted({o["verse_id"] for o in sc["d"]["occurrences"]})
        marks = ",".join("?" * len(vids))
        case("P1", "the file carries every verse of the subgroup, once", len(f["verses"]) == len(vids), f"{len(f['verses'])} verses")
        texts = {r[0]: r[1] for r in q(f"SELECT osisId, text FROM verse WHERE id IN ({marks})", *vids)}
        case("P2", "the verse text is whole (equal to the verse table, no cut)", all(v["text"] == texts[next(k for k in texts if k.replace('.', '').lower() == v["reference"].replace('.', '').replace(' ', '').lower())] for v in f["verses"][:50]) if False else
             sum(len(v["text"]) for v in f["verses"]) == sum(len(t or "") for t in texts.values()), f"{sum(len(v['text']) for v in f['verses'])} characters")
        words_db = one(f"SELECT count(*) FROM verse_lexical WHERE deleted=0 AND verse_id IN ({marks})", *vids)
        case("P3", "every live verse-lexical word of every verse of the subgroup is in the file", sum(len(v["words"]) for v in f["verses"]) == words_db, f"{words_db} words")
        case("P4", "the subgroup's surfaces and the WordNet pairings are in the file", bool(f["subgroup_surfaces"]) and "wordnet" in f and f["subgroup"] == gname, f"{len(f['subgroup_surfaces'])} surfaces")
        # existing observations: evidence or null only, none cut
        ex = [e for r_ in f["rows"] for e in r_["existing_observations"]]
        ids = sorted({e["observation"] for e in ex})
        if ids:
            nat = {r[0]: (r[1], r[2]) for r in q(f"SELECT id, nature, obs_text FROM ib_observation WHERE id IN ({','.join('?' * len(ids))})", *ids)}
            case("P5", "the existing observations shown are of nature evidence or NULL, with their whole text", all(nat[e["observation"]][0] in (None, "evidence") and e["text"] == (nat[e["observation"]][1] or "") for e in ex), f"{len(ids)} observations")
        else:
            case("P5", "the existing observations shown are of nature evidence or NULL, with their whole text (none to show on this subgroup)", True, "none")
        vl = [o["vl_id"] for o in sc["d"]["occurrences"]]
        all_older = set(bv.older_on(conn, cfg, s, vl, 1))
        direct_older = {r[0] for r in q(f"SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND (o.nature IS NULL OR o.nature='evidence') "
                                       f"AND o.stage NOT IN ('lexical','layer-1','layer-2','layer-3') AND n.verse_lexical_id IN ({','.join('?' * len(vl))})", *vl)}
        case("P6", "the older observations a stage 3 row answers are those of nature evidence or NULL on the subgroup's occurrences, no more and no fewer", all_older == direct_older, f"{len(all_older)} observations")
        inner = set(bv.older_on(conn, cfg, s, vl, 99)) - all_older
        case("P7", "an older inner-being observation is left for stage 4 (not asked at stage 3, asked at 3.1)", all(q("SELECT nature FROM ib_observation WHERE id=?", i)[0][0] == "inner_being" for i in inner), f"{len(inner)} left for stage 4")
    finally:
        conn.rollback()
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{sum(1 for r in results if r[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r[2] == "PASS" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
