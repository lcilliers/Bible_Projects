"""temp_2538_scope_test_run.py -- the subgroup is read in isolation (escalation #2538; specification outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md sections 2 and 5;
lib/layerreading.py load(subgroup=), lib/collectionevidence.py build_collection(only_surfaces=), build_pairs).

Each case compares a load scoped to one subgroup with the whole-collection load, filtered to that subgroup, from the tables. Runs against a COPY of iba.db (never the live database).

Usage: python iba/app/tools/temp_2538_scope_test_run.py <db copy> [collection]
"""
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []


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
    t0 = time.time()
    full = lr.load(conn, cfg, name, pairs=True)
    t_full = time.time() - t0
    gids = sorted(full["groups"], key=lambda g: sum(1 for o in full["d"]["occurrences"] if o["group"] == g))
    pick = [gids[0], gids[len(gids) // 2], gids[-1]] if len(gids) >= 3 else gids
    case("S0", "the whole-collection load has occurrences and pairs and at least two subgroups", bool(full["d"]["occurrences"]) and bool(full["pairs"]["pairs"]) and len(gids) >= 2,
         f"{len(full['d']['occurrences'])} occurrences, {len(full['pairs']['pairs'])} pairs, {len(gids)} subgroups, {t_full:.1f}s")
    for g in pick:
        gname = full["groups"][g]["name"]
        t0 = time.time()
        sc = lr.load(conn, cfg, name, pairs=True, subgroup=g)
        t_sc = time.time() - t0
        want_occ = {o["vl_id"] for o in full["d"]["occurrences"] if o["group"] == g}
        have_occ = {o["vl_id"] for o in sc["d"]["occurrences"]}
        case(f"S1-{g}", f"subgroup {gname}: the scoped load holds exactly the occurrences of the subgroup", want_occ == have_occ and bool(want_occ), f"{len(have_occ)} of {len(full['d']['occurrences'])}")
        case(f"S2-{g}", f"subgroup {gname}: every occurrence read carries the subgroup (nothing of another subgroup is read)", all(o["group"] == g for o in sc["d"]["occurrences"]), "")
        key = lambda p: (p["member"]["vl_id"], p["other"]["vl_id"], p["other"]["type"], p["distance"], p["side"])  # noqa: E731
        fp = {key(p) for p in full["pairs"]["pairs"] if p["member"]["subgroup"] == gname}
        sp = {key(p) for p in sc["pairs"]["pairs"] if p["member"]["subgroup"] == gname}
        case(f"S3-{g}", f"subgroup {gname}: the pairings (partner, type, side, distance) are the same as the whole load gives for the subgroup", fp == sp and bool(fp), f"{len(sp)} pairings")
        fr = {r["verse_id"] for r in full["pairs"]["rows"] if r["member"] and full["groups"].get(g) and r["subgroup"] == gname}
        case(f"S4-{g}", f"subgroup {gname}: only the verses of the subgroup's occurrences are read for pairs",
             {r["verse_id"] for r in sc["pairs"]["rows"]} == {o["verse_id"] for o in sc["d"]["occurrences"]}, f"{len(sc['pairs']['rows'])} rows of {len(full['pairs']['rows'])}")
        for step in ("S1", "1.1", "1.2", "2.1"):
            fd = {(w["item"], w["subgroup_id"], w["subject"]) for w in lr.derive(conn, cfg, full, step) if w["subgroup_id"] == g}
            sd_ = {(w["item"], w["subgroup_id"], w["subject"]) for w in lr.derive(conn, cfg, sc, step) if w["subgroup_id"] == g}
            case(f"S5-{g}-{step}", f"subgroup {gname}: step {step} demands the same rows from the scoped load as from the whole load", fd == sd_, f"{len(sd_)} rows")
        if len(gids) > 1 and g == gids[0]:
            case(f"S6-{g}", f"subgroup {gname} (the smallest): the scoped load is faster than the whole-collection load", t_sc < t_full, f"{t_sc:.2f}s against {t_full:.2f}s")
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{sum(1 for r in results if r[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r[2] == "PASS" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
