"""temp_2538_loop_order_test_run.py -- the loop of the layered reading held in code (escalation #2538; lib/layerloop.py; researcher 2026-11-25: B1 to C1 for ONE subgroup at a time, and
"the moment I close the chat then you will have no clue what to do").

Runs on a COPY of iba.db that holds a collection read part of the way (thought), never the live database. Each case compares the library with a query written here.

Usage: python iba/app/tools/temp_2538_loop_order_test_run.py <db copy> [collection]
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import layerloop as ll  # noqa: E402
from iba.app.lib import layerreading as lr  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []


def case(cid, desc, passed, evidence=""):
    results.append((cid, desc, "PASS" if passed is True else ("BLOCKED" if passed is None else "FAIL"), str(evidence).replace("|", "/")[:330]))
    print(f"[{results[-1][2]}] {cid}: {results[-1][3][:170]}", file=sys.stderr, flush=True)


def main(db, name="thought"):
    cfg = Cfg(pathlib.Path(db))
    conn = cfg.conn
    q = lambda s, *a: conn.execute(s, a).fetchall()  # noqa: E731
    cid = q("SELECT id FROM collection WHERE name=? AND deleted=0", name)[0][0]
    p = ll.progress(conn, cfg, name)
    # an independent count of the closed steps of each subgroup
    ok = True
    ev = []
    for g in p["subgroups"]:
        closed = 0
        for s in ll._steps(cfg)[0]:
            rows = q("SELECT state, validated FROM collection_layer_item WHERE collection_id=? AND step=? AND subgroup_id=? AND deleted=0 AND state!='retired'", cid, s, g["id"])
            if rows and all(r[0] in ("observed", "none") and r[1] for r in rows):
                closed += 1
            else:
                break
        ok &= closed == g["closed"]
        ev.append(f"{g['name']}={closed}")
    case("L1", "the progress of each subgroup is the number of loop steps, in order, whose live rows are all answered and validated (equal to an independent query)", ok and bool(p["subgroups"]), "; ".join(ev)[:300])
    nx = ll.next_action(conn, cfg, name)
    inflight = sorted([g for g in p["subgroups"] if not g["complete"]], key=lambda g: (-g["closed"], g["id"]))
    case("L2", "the next action names the subgroup furthest through its loop (the earliest on a tie) and its first step that is not closed", bool(inflight) and nx.get("subgroup") == inflight[0]["name"]
         and nx.get("step") == next(s for s in ll._steps(cfg)[0] if inflight[0]["steps"][s] != "closed"), f"{nx.get('subgroup')} / {nx.get('step')} / {nx.get('state')}")
    case("L3", "the next action gives the verbs to run, naming the collection and the subgroup", bool(nx.get("commands")) and all(name in c for c in nx["commands"] if "LayerRecord" not in c) and any(nx.get("subgroup", "") in c for c in nx["commands"] if "LayerRecord" not in c) and any("LayerRecord" in c for c in nx["commands"] if nx.get("state") == "open"), nx.get("commands", [])[:1])
    others = [g for g in p["subgroups"] if not g["complete"] and g["id"] != inflight[0]["id"] and g["closed"] < inflight[0]["closed"]]
    if others:
        why = ll.order_gate(conn, cfg, name, others[0]["name"])
        case("L4", "a subgroup that is behind another unfinished subgroup is refused, the reason naming the one it waits for and the verb to ask", bool(why) and inflight[0]["name"] in why and "LayerNext" in why, why)
        try:
            lr.open_step(conn, cfg, "TEST-2538-LOOP", name, "S1", dry=True, subgroup=others[0]["name"])
            refused = False
        except lr.LayerError as exc:
            refused = inflight[0]["name"] in str(exc)
        case("L5", "LayerOpen for the waiting subgroup is refused by the gate (a preview too)", refused, "")
    else:
        case("L4", "a waiting subgroup is refused", None, "no subgroup is behind another on this copy")
        case("L5", "LayerOpen for the waiting subgroup is refused", None, "")
    case("L6", "the subgroup in flight is never refused", ll.order_gate(conn, cfg, name, inflight[0]["name"]) is None, "")
    case("L7", "with no subgroup named (a whole-collection step) the gate does not apply", ll.order_gate(conn, cfg, name, None) is None, "")
    import importlib
    hm = importlib.import_module("iba.app.handlers.collectionbuild")
    reg = q("SELECT handler FROM cfg_step WHERE step='collection.layer_next' AND inactive=0")
    case("L8", "the verb is registered (cfg_step collection.layer_next) and its handler loads and exists", bool(reg) and hasattr(hm, "layer_next"), reg)
    conn.rollback()
    print("| case | what | result | evidence |\n|---|---|---|---|")
    for r in results:
        print("| " + " | ".join(r) + " |")
    print(f"\n{sum(1 for r in results if r[2] == 'PASS')} of {len(results)} pass")
    return 0 if all(r[2] != "FAIL" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
