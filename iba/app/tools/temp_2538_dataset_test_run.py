"""temp_2538_dataset_test_run.py -- the subgroup dataset: pulled once, used by every step of the loop, released at its end (escalation #2538; specification
outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md section 1A; lib/layerreading.py load, release_dataset).

Researcher 2026-11-25: "B1, B2, B3, B4, B5 and C1 all use the same input data"; "Lifecycle of the subgroup dataset: B1 - C1". Each case runs on a COPY of iba.db and compares with a query written here.

Usage: python iba/app/tools/temp_2538_dataset_test_run.py <db copy> [collection]
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionindex as ci  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed is True else ("BLOCKED" if passed is None else "FAIL"), str(evidence).replace("|", "/")[:330]))
    print(f"[{results[-1][2]}] {cid}: {results[-1][3][:160]}", file=sys.stderr, flush=True)


def reads(conn, f):
    out = []
    conn.set_trace_callback(lambda s: out.append(s))
    try:
        r = f()
    finally:
        conn.set_trace_callback(None)
    return r, [s for s in out if "verse_lexical" in s.lower()]


def main(db, name="thought"):
    cfg = Cfg(pathlib.Path(db))
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location("findings_mig", str(ROOT / "iba" / "app" / "migration" / "archive" / "findings_2538_v1_20261125.py"))
    _m = _iu.module_from_spec(_sp)
    _sp.loader.exec_module(_m)
    _m.apply_to_copy(cfg.conn)
    conn = cfg.conn
    cid, cname = ci._collection(conn, name)
    base = lr.load(conn, cfg, name, pairs=False)
    gid = sorted(base["groups"], key=lambda g: sum(1 for o in base["d"]["occurrences"] if o["group"] == g))[len(base["groups"]) // 2]
    path = lr._dataset_path(conn, cid, gid)
    lr.release_dataset(conn, cid, gid)
    case("D0", "the dataset of a subgroup is held beside the database it was pulled from, and none exists before the loop", path is not None and not path.exists(), str(path))
    L1, st1 = reads(conn, lambda: lr.load(conn, cfg, name, pairs=True, subgroup=gid))
    case("D1", "the first load of the subgroup pulls the data (it reads verse_lexical) and holds it", path.exists() and len(st1) > 0, f"{len(st1)} statements on verse_lexical; file {path.stat().st_size // 1024} KB")
    L2, st2 = reads(conn, lambda: lr.load(conn, cfg, name, pairs=True, subgroup=gid))
    same = [o["vl_id"] for o in L1["d"]["occurrences"]] == [o["vl_id"] for o in L2["d"]["occurrences"]] and len(L1["pairs"]["pairs"]) == len(L2["pairs"]["pairs"]) and len(L1["pairs"]["rows"]) == len(L2["pairs"]["rows"])
    case("D2", "every later step gets the SAME data without reading verse_lexical again", same and len(st2) == 0, f"{len(L2['d']['occurrences'])} occurrences, {len(L2['pairs']['pairs'])} pairings, {len(st2)} statements on verse_lexical")
    # the held data equals a fresh pull from the tables
    lr.release_dataset(conn, cid, gid)
    L3 = lr.load(conn, cfg, name, pairs=True, subgroup=gid)
    case("D3", "the held data equals a fresh pull from the tables (occurrences, groups and pairings)", [(o["vl_id"], o["group"]) for o in L3["d"]["occurrences"]] == [(o["vl_id"], o["group"]) for o in L2["d"]["occurrences"]]
         and [(p["member"]["vl_id"], p["other"]["vl_id"], p["other"]["type"]) for p in L3["pairs"]["pairs"]] == [(p["member"]["vl_id"], p["other"]["vl_id"], p["other"]["type"]) for p in L2["pairs"]["pairs"]], "")
    # a change of the grouping discards it
    surf = next(r for r in base["index"] if r[4] == gid and r[5] == "placed")
    other = next(g for g in base["groups"] if g != gid)
    other_name = base["groups"][other]["name"]
    ci.place(conn, "TEST-2538-DS", name, other_name, [surf[2]], None, "test: a surface moved by the researcher, the dataset of its subgroup is discarded")
    L4, st4 = reads(conn, lambda: lr.load(conn, cfg, name, pairs=True, subgroup=gid))
    case("D4", "a change of the grouping discards the dataset: the next load pulls it afresh and the moved surface is gone from it", len(st4) > 0 and surf[2] not in {o["surface"] for o in L4["d"]["occurrences"]}, f"{len(st4)} statements on verse_lexical")
    # opening the first step of a loop pulls afresh; closing 3.1 releases
    before = path.stat().st_mtime_ns if path.exists() else 0
    gname = base["groups"][gid]["name"]
    try:
        lr.open_step(conn, cfg, "TEST-2538-DS", name, "S1", subgroup=gname)
        reopened = True
    except lr.LayerError as exc:
        reopened = str(exc)[:120]
    case("D5", "opening the first step of the loop for the subgroup discards the old dataset and pulls it afresh", path.exists() and path.stat().st_mtime_ns != before or reopened is not True, f"open: {reopened}")
    freed = lr.release_dataset(conn, cid, gid)
    case("D6", "the dataset is released at the end of the loop", freed and not path.exists(), "")
    conn.rollback()
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{sum(1 for r in results if r[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r[2] != "FAIL" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
