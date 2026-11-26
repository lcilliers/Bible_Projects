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


def _gate_items(cfg) -> dict:
    """{step: [gate items]}: the ledger-only items of a loop step other than the old-observation rows (the sweep and the evidence validation of 2.1), from cfg_setting layer.reading."""
    from . import buildvalidate as bv
    from . import layerreading as lr
    s = lr.settings(cfg)
    return {st["key"]: g for st in s["steps"] if (g := [i for i in st["items"] if s["items"].get(i, {}).get("ledger_only") and i != bv.OLD_ITEM])}


def _missing_gates(conn, cid: int, gid: int, step: str, items: list) -> list:
    have = {r[0] for r in conn.execute("SELECT DISTINCT item FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step=? AND deleted=0 AND state!='retired'", (cid, gid, step))}
    return [i for i in items if i not in have]


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
    gates = _gate_items(cfg)
    for gid, gname in _subgroups(conn, cid):
        st = {s: _step_status(conn, cid, gid, s) for s in LOOP_STEPS}
        for s_, items in gates.items():      # a step whose gate rows (the sweep, the evidence validation; #2538) a subgroup does not yet have is not closed for it
            if st.get(s_) in ("closed", "answered") and _missing_gates(conn, cid, gid, s_, items):
                st[s_] = "open"
        done = 0
        for s in LOOP_STEPS:
            if st[s] == "closed":
                done += 1
            else:
                break
        started = done < len(LOOP_STEPS) and st[LOOP_STEPS[done]] != "none"      # its next step is open: in flight, ahead of one with as many closed that has not begun it (#2538)
        out["subgroups"].append({"id": gid, "name": gname, "steps": st, "closed": done, "started": started, "complete": done == len(LOOP_STEPS)})
    out["collection_steps"] = {s: _step_status(conn, cid, None, s) for s in COLLECTION_STEPS}
    return out


def _current(prog: dict):
    """The subgroup in flight: of those not complete, the one furthest through its loop (the earliest on a tie)."""
    todo = [g for g in prog["subgroups"] if not g["complete"]]
    if not todo:
        return None
    return sorted(todo, key=lambda g: (-g["closed"], not g["started"], g["id"]))[0]


def next_action(conn, cfg, name: str) -> dict:
    LOOP_STEPS, COLLECTION_STEPS, WHAT = _steps(cfg)
    p = progress(conn, cfg, name)
    cur = _current(p)
    coll = p["collection"]
    ps = r".\iba\app\ps\Collection-Build.ps1"
    out = {"collection": coll, "progress": [f"{g['name']}: " + " ".join(f"{s}={g['steps'][s]}" for s in LOOP_STEPS) for g in p["subgroups"]],
           "collection_steps": p["collection_steps"]}
    if cur is None:
        from . import layerreading as lr
        left = lr.superseded(conn, p["cid"])
        if left["rows"]:      # 3.1 closes with the sweep of what deleted subgroups left behind (researcher 2026-11-26, #2538)
            out.update({"subgroup": None, "step": "3.1", "state": "sweep", "what": f"the close of 3.1: {len(left['rows'])} live ledger row(s) of deleted subgroups hold {len(left['observations'])} observation(s) that are no longer valid",
                        "commands": [f"{ps} -Action SweepSuperseded -Collection {coll} -Check   (preview)", f"{ps} -Action ReadBehaviours -Collection {coll}   (runs the sweep, then writes the 3.2 package)"]})
            return out
        for s in COLLECTION_STEPS:
            stt = p["collection_steps"][s]
            if stt != "closed":
                sdef = next((x for x in lr.settings(cfg)["steps"] if x["key"] == s), {})
                if sdef.get("read_command_deferred"):      # a step the researcher has deferred is named with the ruling, not opened (#2538, 3.3 waits for every collection complete)
                    out.update({"subgroup": None, "step": s, "state": "deferred", "what": f"{WHAT[s]} -- deferred: {sdef['read_command_deferred']}", "commands": []})
                    return out
                out.update({"subgroup": None, "step": s, "state": stt, "what": WHAT[s], "commands": _read_commands(conn, cfg, p["cid"], 0, s, stt, ps, coll, None) or _commands(ps, coll, s, None, stt)})
                return out
        out.update({"subgroup": None, "step": None, "state": "complete", "what": "every subgroup is through 3.1 and 3.2 and 3.3 are closed: the inner-being validation completes the collection (it can only complete after 3.3)", "commands": [f"{ps} -Action LayerCheck -Collection {coll}"]})
        return out
    step = next(s for s in LOOP_STEPS if cur["steps"][s] != "closed")
    stt = cur["steps"][step]
    cmds = _read_commands(conn, cfg, p["cid"], cur["id"], step, stt, ps, coll, cur["name"]) or _commands(ps, coll, step, cur["name"], stt)
    out.update({"subgroup": cur["name"], "step": step, "state": stt, "what": WHAT[step], "commands": cmds})
    behind = [g["name"] for g in p["subgroups"] if not g["complete"] and g["id"] != cur["id"]]
    out["others_waiting"] = behind
    return out


def _read_commands(conn, cfg, cid: int, gid: int, step: str, state: str, ps: str, coll: str, sub: str) -> list[str]:
    """The read command that answers the next item of the step (cfg_setting layer.read_types: each read names its `command` and the `items` it answers; #2538). For an open step, the
    first item in the step's order with a row not answered and validated; for a step not opened, its first item (the read command opens the step). [] where no read command answers it."""
    import json
    v = cfg.setting("layer.read_types")
    if not v:
        return []
    rts = json.loads(v) if isinstance(v, str) else v
    by_item = {i: t["command"] for t in rts.values() if isinstance(t, dict) and t.get("command") for i in t.get("items", [])}
    from . import layerreading as lr
    items = lr.step_def(lr.settings(cfg), step)["items"]
    if state == "none":
        todo = [i for i in items if i in by_item][:1]
    else:
        rows = conn.execute("SELECT item, state, validated FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step=? AND deleted=0 AND state!='retired'",
                            (cid, gid, step)).fetchall()
        pending = {r[0] for r in rows if r[1] == "open" or not r[2]} | set(_missing_gates(conn, cid, gid, step, _gate_items(cfg).get(step, [])))
        todo = [i for i in items if i in pending and i in by_item][:1]
    if not todo:
        return []
    where = f' -Subgroup "{sub}"' if sub else ""      # a collection step (3.2) is the collection's own and takes no subgroup
    return [f'{ps} -Action {by_item[todo[0]]} -Collection {coll}{where}   (writes the package of the next {todo[0]} row(s); read it, fill its answer, then the matching Record command named in the package)']


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
    ahead = [g for g in p["subgroups"] if not g["complete"] and g["id"] != me["id"]
             and (g["closed"] > me["closed"] or (g["closed"] == me["closed"] and g["started"] and not me["started"]))]
    if not ahead:
        return None
    a = sorted(ahead, key=lambda g: (-g["closed"], not g["started"], g["id"]))[0]
    return (f"the loop is for one subgroup at a time: {a['name']!r} is further through its loop ({a['closed']} of {len(_steps(cfg)[0])} steps closed"
            f"{', its next step open' if a['started'] else ''}) and is not finished, so {me['name']!r} "
            f"({me['closed']} closed) waits. Run Collection-Build.ps1 -Action LayerNext -Collection {p['collection']} to see what to do next.")
