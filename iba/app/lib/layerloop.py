"""layerloop.py -- the loop of the layered reading, held in code (escalation #2538; researcher 2026-11-25: "the moment I close the chat then you will have no clue what to do").

The specification (outputs/escalation/2538-analytic-phases-1-4-specification-v5-20261125.md, section 1) is: A grouping once; then for ONE subgroup at a time, in isolation, B1 (S1), B2 (1.1, 1.2),
B3 (2.1, with the sweep of the unmarked and the evidence validation), C1 (3.1); then, when every subgroup is through 3.1, C2 (3.2), C3 (3.3) and the inner-being validation. The ledger
`collection_layer_item` is the record of where the work stands; this module reads it and answers two questions from the tables alone, so no session has to remember:

  progress(conn, cfg, name)     for each subgroup, which loop steps are closed (every live row observed or none, and validated), and whether its loop is complete
  next_action(conn, cfg, name)  the ONE thing to do next: the subgroup, the step, what its state is and the verbs to run
  order_gate(conn, cfg, name, subgroup)  the refusal LayerOpen applies: a subgroup may not start or continue a step while another subgroup is further through its loop and not finished
"""
from __future__ import annotations

def _steps(cfg):
    """(loop steps, collection steps, {step: description}) from cfg_setting layer.reading, in its order: a step whose items are the collection's own (collection-gathering, interworking) is a collection step;
    every other step is passed by each subgroup in turn. Nothing about the steps is held in this code (governance.rules_must_be_config_driven)."""
    from . import layerinner as li
    from . import layerreading as lr
    s = lr.settings(cfg)
    coll_items = {li.COLLECTION, li.CROSS}
    loop, coll, what = [], [], {}
    for st in s["steps"]:
        (coll if coll_items & set(st["items"]) else loop).append(st["key"])
        asks = [s["items"][i].get("asks", "") for i in st["items"] if i in s["items"] and not s["items"][i].get("ledger_only")]
        what[st["key"]] = f"{st['name']} (stage {st.get('stage')}; items {', '.join(i for i in st['items'] if not s['items'].get(i, {}).get('ledger_only'))}): " + (asks[0] if asks else "")
    return tuple(loop), tuple(coll), what


def _subgroups(conn, cid: int) -> list[tuple[int, str]]:
    return [(r[0], r[1]) for r in conn.execute("SELECT id, name FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND status!='retired' ORDER BY id", (cid,))]


def _status(rows: list) -> str:
    """none (no live row), open (a row still to answer), answered (answered, not yet validated), closed."""
    live = [r for r in rows if r[0] != "retired"]
    if not live:
        return "none"
    if any(r[0] == "open" for r in live):
        return "open"
    if any(not r[1] for r in live):
        return "answered"
    return "closed"


def _step_status(conn, cid: int, gid, step: str) -> str:
    if gid is None:
        q = conn.execute("SELECT state, validated FROM collection_layer_item WHERE collection_id=? AND step=? AND deleted=0 AND coalesce(subgroup_id,0)=0", (cid, step))
    else:
        q = conn.execute("SELECT state, validated FROM collection_layer_item WHERE collection_id=? AND step=? AND deleted=0 AND subgroup_id=?", (cid, step, gid))
    return _status(q.fetchall())


def progress(conn, cfg, name: str) -> dict:
    from . import collectionindex as ci
    LOOP_STEPS, COLLECTION_STEPS, _w = _steps(cfg)
    cid, cname = ci._collection(conn, name)
    out = {"collection": cname, "cid": cid, "subgroups": [], "collection_steps": {}}
    for gid, gname in _subgroups(conn, cid):
        st = {s: _step_status(conn, cid, gid, s) for s in LOOP_STEPS}
        done = 0
        for s in LOOP_STEPS:
            if st[s] == "closed":
                done += 1
            else:
                break
        out["subgroups"].append({"id": gid, "name": gname, "steps": st, "closed": done, "complete": done == len(LOOP_STEPS)})
    out["collection_steps"] = {s: _step_status(conn, cid, None, s) for s in COLLECTION_STEPS}
    return out


def _current(prog: dict):
    """The subgroup in flight: of those not complete, the one furthest through its loop (the earliest on a tie)."""
    todo = [g for g in prog["subgroups"] if not g["complete"]]
    if not todo:
        return None
    return sorted(todo, key=lambda g: (-g["closed"], g["id"]))[0]


def next_action(conn, cfg, name: str) -> dict:
    LOOP_STEPS, COLLECTION_STEPS, WHAT = _steps(cfg)
    p = progress(conn, cfg, name)
    cur = _current(p)
    coll = p["collection"]
    ps = r".\iba\app\ps\Collection-Build.ps1"
    out = {"collection": coll, "progress": [f"{g['name']}: " + " ".join(f"{s}={g['steps'][s]}" for s in LOOP_STEPS) for g in p["subgroups"]],
           "collection_steps": p["collection_steps"]}
    if cur is None:
        for s in COLLECTION_STEPS:
            stt = p["collection_steps"][s]
            if stt != "closed":
                out.update({"subgroup": None, "step": s, "state": stt, "what": WHAT[s], "commands": _commands(ps, coll, s, None, stt)})
                return out
        out.update({"subgroup": None, "step": None, "state": "complete", "what": "every subgroup is through 3.1 and 3.2 and 3.3 are closed: the inner-being validation completes the collection (it can only complete after 3.3)", "commands": [f"{ps} -Action LayerCheck -Collection {coll}"]})
        return out
    step = next(s for s in LOOP_STEPS if cur["steps"][s] != "closed")
    stt = cur["steps"][step]
    out.update({"subgroup": cur["name"], "step": step, "state": stt, "what": WHAT[step], "commands": _commands(ps, coll, step, cur["name"], stt)})
    behind = [g["name"] for g in p["subgroups"] if not g["complete"] and g["id"] != cur["id"]]
    out["others_waiting"] = behind
    return out


def _commands(ps: str, coll: str, step: str, sub, state: str) -> list[str]:
    sg = f' -Subgroup "{sub}"' if sub else ""
    if state == "none":
        return [f'{ps} -Action LayerOpen -Collection {coll} -Step {step}{sg}', f'{ps} -Action LayerPull -Collection {coll} -Step {step}{sg}']
    if state == "open":
        return [f'{ps} -Action LayerPull -Collection {coll} -Step {step}{sg}   (writes the working file; read it whole, fill every row, answer every older observation in the row it sits on)',
                f'{ps} -Action LayerRecord -File <the working file> -Check', f'{ps} -Action LayerRecord -File <the working file>', f'{ps} -Action LayerCheck -Collection {coll}{sg}']
    return [f'{ps} -Action LayerCheck -Collection {coll}{sg}']


def order_gate(conn, cfg, name: str, subgroup: str | None) -> str | None:
    """None when the subgroup may open a step; else the reason. A subgroup that is not complete may not open a step while another subgroup is further through its loop and not complete: the loop is for
    ONE subgroup at a time, B1 to C1, then the next (researcher 2026-11-25)."""
    if not subgroup:
        return None
    p = progress(conn, cfg, name)
    me = next((g for g in p["subgroups"] if g["name"].lower() == subgroup.strip().lower()), None)
    if me is None or me["complete"]:
        return None
    ahead = [g for g in p["subgroups"] if not g["complete"] and g["id"] != me["id"] and g["closed"] > me["closed"]]
    if not ahead:
        return None
    a = sorted(ahead, key=lambda g: (-g["closed"], g["id"]))[0]
    return (f"the loop is for one subgroup at a time: {a['name']!r} is further through its loop ({a['closed']} of {len(_steps(cfg)[0])} steps closed) and is not finished, so {me['name']!r} "
            f"({me['closed']} closed) waits. Run Collection-Build.ps1 -Action LayerNext -Collection {p['collection']} to see what to do next.")
