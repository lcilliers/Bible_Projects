"""layerreading.py -- the layered reading of a collection: layer 1 (step 1.1 groups, step 1.2 Strong's enrichment) and layer 2 (step 2.1 pairings)
(escalation #2505; design outputs/escalation/2505-layers-1-2-build-design-v1-20261115.md; researcher's definition on #2463 v16).

What it holds and why. Each step asks for a set of aspects, each answered by an observation with nodes (or, where the setting allows, by a recorded "none" with its reason).
The aspects are derived from the data when a step is opened and kept in the ledger `collection_layer_item`, so that nothing hangs in the air: a step is closed only when every
row is answered and validated, and the next step cannot be opened before that. The nodes of an observation are built from the data (the occurrences of the group, the partners),
never typed, so they are complete; the interpretation is the observation text. The check re-derives what each answered row demands and validates it against the tables.
The content of the layers (steps, items, kinds, thresholds, roles) is cfg_setting layer.reading; the code holds none of it.
"""
from __future__ import annotations

import collections
import datetime
import json
import pathlib

from . import collectionevidence as ev
from . import collectionindex as ci
from . import observationrecord as orec
from . import recordingpass

CHUNK = 800
NOW = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"
WHO = "Claude"
BY = "layer-reading"


class LayerError(Exception):
    """A usage or setting problem; routed as 'refused' and nothing is written."""


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def settings(cfg) -> dict:
    s = cfg.setting("layer.reading")
    if not s:
        raise LayerError("cfg_setting layer.reading is missing")
    return s


def step_def(s: dict, key: str) -> dict:
    for st in s["steps"]:
        if st["key"] == key:
            return st
    raise LayerError(f"{key!r} is not a step of the layered reading ({', '.join(x['key'] for x in s['steps'])})")


def _chunks(ids):
    ids = sorted(set(ids))
    for i in range(0, len(ids), CHUNK):
        yield ids[i:i + CHUNK]


# ══ the data of a collection ═══════════════════════════════════════════════════════════════════
def load(conn, cfg, name: str, pairs: bool = False) -> dict:
    """The collection, its member occurrences (by the one membership rule of the evidence report), its index rows and groups; with pairs=True the typed pairings of layer 2."""
    try:
        cid, cname = ci._collection(conn, name)
        vals = ev.read_settings(cfg)
        order = ev.Order(conn)
        d = ev.build_collection(conn, ev.resolve(conn, [cname])[0], vals["tiers"], order)
    except (ci.IndexError_, ev.EvidenceError) as exc:
        raise LayerError(str(exc))
    L = {"cid": cid, "name": cname, "d": d, "vals": vals, "order": order}
    L["index"] = conn.execute("SELECT i.id, i.term_id, t.surface, i.strong, i.subgroup_id, i.state, i.reason FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id "
                              "WHERE i.deleted=0 AND i.collection_id=?", (cid,)).fetchall()
    L["groups"] = {r[0]: {"id": r[0], "name": r[1], "status": r[2]} for r in conn.execute(
        "SELECT id, name, status FROM collection_subgroup WHERE deleted=0 AND collection_id=? AND status!='retired'", (cid,))}
    by = {(r[2], r[3]): r for r in L["index"]}
    for o in d["occurrences"]:
        r = by.get((o["surface"], o["strong"])) or by.get((o["surface"], None))
        o["group"] = r[4] if r and r[5] == "placed" and r[4] in L["groups"] else None
        o["index_state"] = r[5] if r else "not indexed"
    L["col_ids"] = {r[1]: r[0] for r in conn.execute("SELECT id, name FROM collection WHERE deleted=0 AND status='confirmed'")}
    if pairs:
        L["pairs"] = ev.build_pairs(conn, d, vals, order)
    return L


# ══ the gates ══════════════════════════════════════════════════════════════════════════════════
def lexical_gate(conn, cfg, L) -> dict:
    """The lexical precondition (researcher 2026-11-14, #2463 v22: lexical and claims readings do not run together; the lexical observations come first): every member occurrence
    carries a live node with a role of reading.node_roles on a live observation that no layer wrote."""
    s = settings(cfg)
    roles = sorted(orec.node_roles(cfg))
    stages = sorted(s["stages"].values())
    ids = [o["vl_id"] for o in L["d"]["occurrences"]]
    covered = set()
    for part in _chunks(ids):
        covered.update(r[0] for r in conn.execute(
            f"SELECT DISTINCT n.verse_lexical_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 "
            f"AND o.stage NOT IN ({','.join('?' * len(stages))}) AND n.role IN ({','.join('?' * len(roles))}) AND n.verse_lexical_id IN ({','.join('?' * len(part))})", stages + roles + part))
    missing = [o for o in L["d"]["occurrences"] if o["vl_id"] not in covered]
    return {"occurrences": len(ids), "covered": len(covered), "missing": missing}


def grouping_gate(conn, cfg, L) -> list[str]:
    """Layer 1 step 1 can be opened only when the grouping is finished: the index filled, every surface placed or isolated (with its reason), every live group holding a surface."""
    out = []
    reach, _, _ = ci.members(conn, ci.member_tiers(cfg))
    expected = {tid for tid, cid in reach.items() if cid == L["cid"]}
    have = {r[1] for r in L["index"]}
    if expected - have:
        out.append(f"{len(expected - have)} member surfaces have no index row (run Collection-Build.ps1 -Action Index)")
    un = [r[2] + (f" ({r[3]})" if r[3] else "") for r in L["index"] if r[5] == "unplaced"]
    if un:
        out.append(f"{len(un)} surfaces are not placed in a subgroup or isolated: {', '.join(sorted(un)[:12])}{' ...' if len(un) > 12 else ''}")
    iso = [r[2] for r in L["index"] if r[5] == "isolated" and (not (r[6] or "").strip() or r[6] == "index fill")]
    if iso:
        out.append(f"isolated surfaces with no reason: {', '.join(sorted(iso))}")
    if not L["groups"]:
        out.append("the collection has no subgroup")
    placed = {r[4] for r in L["index"] if r[5] == "placed"}
    empty = [g["name"] for g in L["groups"].values() if g["id"] not in placed]
    if empty:
        out.append(f"subgroups with no surface: {', '.join(sorted(empty))}")
    return out


# ══ what each step demands ═════════════════════════════════════════════════════════════════════
def derive(conn, cfg, L, step: str) -> list[dict]:
    """The aspects of a step, from the data: [{item, subgroup_id, subject}]. Layer 2 aspects come from the typed pairings of the evidence report (#2502)."""
    s = settings(cfg)
    items = step_def(s, step)["items"]
    th = s["thresholds"]
    out = []
    gids = sorted(L["groups"])
    if "group-definition" in items:
        out += [{"item": "group-definition", "subgroup_id": g, "subject": ""} for g in gids]
    if "strong-enrichment" in items:
        out += [{"item": "strong-enrichment", "subgroup_id": g, "subject": ""} for g in gids]
    if any(i in items for i in ("pairing", "qualifier", "entity", "direction", "group-relation", "double-meaning")):
        name2id = {g["name"]: g["id"] for g in L["groups"].values()}
        partner, qual, ent = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for p in L["pairs"]["pairs"]:
            g = name2id.get(p["member"]["subgroup"])
            if g is None:
                continue
            o, v = p["other"], p["member"]["verse_id"]
            if o["type"] == "word of another collection":
                for cn in o["collections"]:
                    partner[(g, cn)].add(v)
            if o["qualifier"]:
                qual[g].add(v)
            if o["type"].startswith("entity"):
                ent[g].add(v)
        if "pairing" in items:
            out += [{"item": "pairing", "subgroup_id": g, "subject": cn} for (g, cn), vs in sorted(partner.items()) if len(vs) >= th["pair_min_verses"]]
        if "qualifier" in items:
            out += [{"item": "qualifier", "subgroup_id": g, "subject": ""} for g in sorted(qual)]
        if "entity" in items:
            out += [{"item": "entity", "subgroup_id": g, "subject": ""} for g in sorted(ent)]
        if "direction" in items:
            out += [{"item": "direction", "subgroup_id": g, "subject": ""} for g in sorted(ent)]
        if "group-relation" in items:
            vg = collections.defaultdict(set)
            for o in L["d"]["occurrences"]:
                if o["group"]:
                    vg[o["verse_id"]].add(o["group"])
            share = collections.Counter()
            for gs in vg.values():
                for a in gs:
                    for b in gs:
                        if a < b:
                            share[(a, b)] += 1
            out += [{"item": "group-relation", "subgroup_id": a, "subject": str(b)} for (a, b), n in sorted(share.items()) if n >= th["relation_min_verses"]]
        if "double-meaning" in items:
            codes = collections.defaultdict(set)
            for o in L["d"]["occurrences"]:
                if o["group"] and o["strong"]:
                    codes[(o["group"], o["surface"])].add(o["strong"])
            out += [{"item": "double-meaning", "subgroup_id": g, "subject": sf} for (g, sf), cs in sorted(codes.items()) if len(cs) >= 2]
    return out


def expected_nodes(L, item: str, gid: int, subject: str) -> list[tuple[dict, str]]:
    """The occurrences an answered aspect must carry as nodes, each as (occurrence row, "member" or "partner"). Built from the data; the recorder writes exactly these."""
    occ = [o for o in L["d"]["occurrences"] if o["group"] == gid]
    if item in ("group-definition", "strong-enrichment"):
        return [(o, "member") for o in occ]
    if item == "double-meaning":
        return [(o, "member") for o in occ if o["surface"] == subject]
    if item == "group-relation":
        other = int(subject)
        vg = collections.defaultdict(set)
        for o in L["d"]["occurrences"]:
            if o["group"] in (gid, other):
                vg[o["verse_id"]].add(o["group"])
        shared = {v for v, gs in vg.items() if len(gs) == 2}
        return [(o, "member") for o in L["d"]["occurrences"] if o["group"] in (gid, other) and o["verse_id"] in shared]
    name = L["groups"][gid]["name"]
    if item == "pairing":
        pick = lambda o: o["type"] == "word of another collection" and subject in o["collections"]  # noqa: E731
    elif item == "qualifier":
        pick = lambda o: bool(o["qualifier"])  # noqa: E731
    else:   # entity, direction
        pick = lambda o: o["type"].startswith("entity")  # noqa: E731
    members, partners = {}, {}
    for p in L["pairs"]["pairs"]:
        if p["member"]["subgroup"] == name and pick(p["other"]):
            members[p["member"]["vl_id"]] = p["member"]
            partners[p["other"]["vl_id"]] = p["other"]
    return [(m, "member") for m in members.values()] + [(o, "partner") for o in partners.values() if o["vl_id"] not in members]


def _rows(conn, cid, step=None):
    q = "SELECT id, collection_id, step, item, subgroup_id, subject, state, observation_id, reason, validated FROM collection_layer_item WHERE deleted=0 AND collection_id=?"
    a = [cid]
    if step:
        q += " AND step=?"
        a.append(step)
    return conn.execute(q + " ORDER BY id", a).fetchall()


def step_closed(conn, cid: int, step: str) -> bool:
    rows = [r for r in _rows(conn, cid, step) if r[6] != "retired"]
    return bool(rows) and all(r[6] in ("observed", "none") and r[9] == 1 for r in rows)


# ══ open: derive the ledger ════════════════════════════════════════════════════════════════════
def open_step(conn, cfg, run_id: str, name: str, step: str, dry: bool = False) -> dict:
    s = settings(cfg)
    sd = step_def(s, step)
    L = load(conn, cfg, name, pairs=sd["layer"] == 2)
    problems = []
    gate = lexical_gate(conn, cfg, L)
    if gate["missing"]:
        problems.append(f"the lexical gate fails: {len(gate['missing'])} of {gate['occurrences']} member occurrences carry no lexical node with a role (the lexical observations come first; "
                        f"Engagement.ps1 -Action Pull -Collection {L['name']} -Missing)")
    problems += grouping_gate(conn, cfg, L)
    for need in sd["needs"]:
        if need != "lexical-gate" and not step_closed(conn, L["cid"], need):
            problems.append(f"step {need} is not closed (every row answered and validated: LayerCheck)")
    if problems:
        raise LayerError(f"step {step} of {L['name']} cannot be opened:\n  " + "\n  ".join(problems))
    want = derive(conn, cfg, L, step)
    have = {(r[3], r[4], r[5]): r for r in _rows(conn, L["cid"], step)}
    key = lambda w: (w["item"], w["subgroup_id"], w["subject"])  # noqa: E731
    add = [w for w in want if key(w) not in have]
    wanted = {key(w) for w in want}
    retire = [r for k, r in have.items() if k not in wanted and r[6] != "retired"]
    revive = [r for k, r in have.items() if k in wanted and r[6] == "retired"]
    out = {"collection": L["name"], "step": step, "demanded": len(want), "add": len(add), "retire": len(retire), "revive": len(revive)}
    if dry:
        return out
    for w in add:
        conn.execute("INSERT INTO collection_layer_item (collection_id, step, item, subgroup_id, subject, state, run_id, created_by) VALUES (?,?,?,?,?,'open',?,?)",
                     (L["cid"], step, w["item"], w["subgroup_id"], w["subject"], run_id, BY))
    for r in retire:
        conn.execute(f"UPDATE collection_layer_item SET state='retired', validated=0, updated_at={NOW}, run_id=?, reason='the data no longer demands this aspect' WHERE id=?", (run_id, r[0]))
    for r in revive:
        conn.execute(f"UPDATE collection_layer_item SET state='open', validated=0, updated_at={NOW}, run_id=? WHERE id=?", (run_id, r[0]))
    return out


# ══ pull: the working file ═════════════════════════════════════════════════════════════════════
def pull(conn, cfg, name: str, step: str, out_dir: pathlib.Path) -> tuple[pathlib.Path, int]:
    s = settings(cfg)
    sd = step_def(s, step)
    L = load(conn, cfg, name, pairs=sd["layer"] == 2)
    rows = [r for r in _rows(conn, L["cid"], step) if r[6] == "open" or (r[6] == "observed" and r[9] == 0)]
    if not rows:
        raise LayerError(f"step {step} of {L['name']} has no open row (run LayerOpen, or LayerCheck to see what is validated)")
    out = []
    for r in rows:
        lid, _, _, item, gid, subject, state, oid, reason, val = r
        idef = s["items"][item]
        nodes = expected_nodes(L, item, gid, subject)
        cap = s["pull_max_nodes"]
        text_of = {}
        for part in _chunks([o["verse_id"] for o, _ in nodes[:cap]]):
            text_of.update({v[0]: v[1] for v in conn.execute(f"SELECT id, text FROM verse WHERE id IN ({','.join('?' * len(part))})", part)})
        ev_nodes = [{"reference": o["reference"], "surface": o["surface"], "strong": o["strong"], "as": role, "verse": (text_of.get(o["verse_id"]) or "")[:200]} for o, role in nodes[:cap]]
        codes = collections.Counter(o["strong"] for o, role in nodes if role == "member" and o["strong"])
        out.append({"ledger_id": lid, "item": item, "kind": idef["kind"], "group": L["groups"][gid]["name"], "subject": subject,
                    "asks": idef["asks"], "nodes_total": len(nodes), "nodes_shown": len(ev_nodes), "strong_codes": dict(codes), "evidence": ev_nodes,
                    "fill": {"disposition": "observed | none" if idef["none_allowed"] else "observed", "obs_text": "", "basis": "stated | read",
                             "route": "A | B | C" if idef.get("route") else "", "member_role": idef["member_role"], "partner_role": idef.get("partner_role", ""), "reason": ""}})
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"layer-{L['name']}-{step}-{_now()[:10].replace('-', '')}.json"
    path.write_text(json.dumps({"collection": L["name"], "step": step, "pulled": _now(), "rows": out}, ensure_ascii=False, indent=1), encoding="utf-8")
    return path, len(out)


# ══ record: check whole, write whole ═══════════════════════════════════════════════════════════
def _vl(conn, ids) -> dict:
    out = {}
    for part in _chunks(ids):
        for r in conn.execute(f"SELECT vl.id, vl.strong, v.osisId, vl.surface, vl.morph_code, lower(trim(vl.surface)) FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
                              f"WHERE vl.id IN ({','.join('?' * len(part))})", part):
            out[r[0]] = r
    return out


def record(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check the filled file whole and write it in one savepoint; any problem refuses all. keep=False rolls back (the preview)."""
    s = settings(cfg)
    name, step = data.get("collection"), data.get("step")
    sd = step_def(s, step)
    L = load(conn, cfg, name, pairs=sd["layer"] == 2)
    roles, bases, routes = set(orec.node_roles(cfg)), set(cfg.enum("ib_observation.basis")), set(cfg.enum("observation_route"))
    minr = s["min_reason_chars"]
    ledger = {r[0]: r for r in _rows(conn, L["cid"], step)}
    errors, plan, seen = [], [], {}
    for i, row in enumerate(data.get("rows", [])):
        where = f"row {i + 1} (ledger {row.get('ledger_id')})"
        lr = ledger.get(row.get("ledger_id"))
        if lr is None:
            errors.append(f"{where}: not a ledger row of {L['name']} step {step}")
            continue
        if not (lr[6] == "open" or (lr[6] == "observed" and lr[9] == 0)):
            errors.append(f"{where}: the row is {lr[6]}{' and validated' if lr[9] else ''}; only an open or an unvalidated row is recorded")
            continue
        item, gid, subject = lr[3], lr[4], lr[5]
        idef = s["items"][item]
        fill = row.get("fill") or row
        disp = fill.get("disposition")
        if disp == "none":
            if not idef["none_allowed"]:
                errors.append(f"{where}: {item} cannot be recorded as none; it needs an observation")
            elif len((fill.get("reason") or "").strip()) < minr:
                errors.append(f"{where}: none needs its reason, in words ({minr} characters or more)")
            plan.append({"ledger": lr, "disp": "none", "reason": (fill.get("reason") or "").strip()})
            continue
        if disp != "observed":
            errors.append(f"{where}: disposition must be observed or none")
            continue
        text = (fill.get("obs_text") or "").strip()
        try:
            recordingpass._validate_obs_text(conn, text)
        except recordingpass.InvalidObservationText as exc:
            errors.append(f"{where}: {exc}")
        if len(text) < s["min_text_chars"]:
            errors.append(f"{where}: the observation text is missing or under {s['min_text_chars']} characters")
        dup = orec.live_text(conn, text) if text else None
        if dup and dup["id"] != lr[7]:
            errors.append(f"{where}: this description is already live as observation {dup['id']}")
        if text in seen:
            errors.append(f"{where}: the same text as {seen[text]}")
        seen[text] = where
        if fill.get("basis") not in bases:
            errors.append(f"{where}: basis must be one of {sorted(bases)}")
        route = (fill.get("route") or "").strip() or None
        if idef.get("route"):
            if route not in routes:
                errors.append(f"{where}: a {idef['kind']} finding of this item carries its route, one of {sorted(routes)}")
        elif route:
            errors.append(f"{where}: this item takes no route")
        mrole = (fill.get("member_role") or idef["member_role"]).strip()
        prole = (fill.get("partner_role") or idef.get("partner_role") or "").strip()
        for label, rl in (("member_role", mrole), ("partner_role", prole)):
            if rl and rl not in roles:
                errors.append(f"{where}: {label} {rl!r} is not a node role ({sorted(roles)})")
        nodes = expected_nodes(L, item, gid, subject)
        if not nodes:
            errors.append(f"{where}: the data holds no occurrence for this aspect")
        plan.append({"ledger": lr, "disp": "observed", "text": text, "basis": fill.get("basis"), "route": route, "mrole": mrole, "prole": prole, "nodes": nodes, "idef": idef})
    if errors:
        raise LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
    conn.execute("SAVEPOINT layer_record")
    res = {"observed": 0, "none": 0, "nodes": 0, "withdrawn": 0}
    try:
        stage = s["stages"][str(sd["layer"])]
        vl = _vl(conn, [o["vl_id"] for p in plan if p["disp"] == "observed" for o, _ in p["nodes"]])
        for p in plan:
            lid, old = p["ledger"][0], p["ledger"][7]
            if old and conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND deleted=0", (old,)).fetchone():
                orec.soft_delete_observation(conn, old, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                res["withdrawn"] += 1
            if p["disp"] == "none":
                conn.execute(f"UPDATE collection_layer_item SET state='none', observation_id=NULL, reason=?, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (p["reason"], run_id, lid))
                res["none"] += 1
                continue
            parts = json.dumps({"item": p["ledger"][3], "step": step}, ensure_ascii=False)
            oid = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, basis, route, parts, meaning_source, status, stable_key, run_id, created_at) "
                               "VALUES (NULL,?,?,?,?,?,?,'verse-text','draft',?,?,?)",
                               (stage, p["idef"]["kind"], p["text"], p["basis"], p["route"], parts, f"layer:{lid}:{run_id}", run_id, _now())).lastrowid
            orec.log(conn, oid, None, "created", None, p["text"], f"layer observation {p['ledger'][3]} for ledger row {lid}", None, run_id, WHO)
            seq = 0
            for o, role_of in p["nodes"]:
                v = vl[o["vl_id"]]
                cid = L["cid"]
                if role_of == "partner" and len(o["collections"]) == 1 and o["collections"][0] in L["col_ids"]:
                    cid = L["col_ids"][o["collections"][0]]
                role = p["mrole"] if role_of == "member" else (p["prole"] or p["mrole"])
                seq += 1
                nid = conn.execute("INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, reading_id, created_at, verse_lexical_id, collection_id, subgroup_id) "
                                   "VALUES (?,?,?,?,?,?,?,?,NULL,?,?,?,?)", (oid, v[1], v[2], v[3], v[4], stage, seq, role, _now(), o["vl_id"], cid, ci.subgroup_for(conn, cid, v[5], v[1]))).lastrowid
                orec.log(conn, oid, nid, "node", None, f"added: {v[2]} {v[3]} ({v[1]}) role {role}", f"layer node of ledger row {lid}", None, run_id, WHO)
                res["nodes"] += 1
            conn.execute(f"UPDATE collection_layer_item SET state='observed', observation_id=?, reason=NULL, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (oid, run_id, lid))
            res["observed"] += 1
        conn.execute("RELEASE layer_record" if keep else "ROLLBACK TO layer_record")
        if not keep:
            conn.execute("RELEASE layer_record")
    except Exception:
        conn.execute("ROLLBACK TO layer_record")
        conn.execute("RELEASE layer_record")
        raise
    return res


# ══ check: validate every answered row against the tables ══════════════════════════════════════
def check(conn, cfg, run_id: str, name: str, dry: bool = False) -> dict:
    """Re-derive what each answered row demands and validate it. Sets `validated` (the check alone sets it). Returns the findings by step."""
    s = settings(cfg)
    roles = set(orec.node_roles(cfg))
    L1 = load(conn, cfg, name, pairs=False)
    L2 = None
    gate = lexical_gate(conn, cfg, L1)
    rep = {"collection": L1["name"], "lexical_missing": len(gate["missing"]), "lexical_occurrences": gate["occurrences"], "grouping": grouping_gate(conn, cfg, L1), "steps": {}}
    for sd in s["steps"]:
        step = sd["key"]
        if sd["layer"] == 2 and L2 is None:
            L2 = load(conn, cfg, name, pairs=True)
        L = L2 if sd["layer"] == 2 else L1
        rows = [r for r in _rows(conn, L["cid"], step) if r[6] != "retired"]
        problems, ok_, open_ = [], 0, 0
        for r in rows:
            lid, _, _, item, gid, subject, state, oid, reason, val = r
            label = f"{item} / {L['groups'].get(gid, {}).get('name', f'group {gid}')}" + (f" / {subject}" if subject else "")
            if state == "open":
                open_ += 1
                continue
            idef = s["items"][item]
            fail = None
            if state == "none":
                if not idef["none_allowed"] or len((reason or "").strip()) < s["min_reason_chars"]:
                    fail = "recorded as none without a permitted reason"
            else:
                o = conn.execute("SELECT stage, tag, deleted FROM ib_observation WHERE id=?", (oid,)).fetchone() if oid else None
                if o is None or o[2]:
                    fail = "its observation is missing or withdrawn"
                elif o[0] != s["stages"][str(sd["layer"])] or o[1] != idef["kind"]:
                    fail = f"its observation has stage {o[0]} and kind {o[1]}, not {s['stages'][str(sd['layer'])]} and {idef['kind']}"
                elif gid not in L["groups"]:
                    fail = "its group is retired or missing"
                else:
                    exp = expected_nodes(L, item, gid, subject)
                    want = {x["vl_id"] for x, _ in exp}
                    live = conn.execute("SELECT verse_lexical_id, role, collection_id, strong FROM ib_node WHERE observation_id=? AND deleted=0", (oid,)).fetchall()
                    have = {x[0] for x in live}
                    if want != have:
                        fail = f"its nodes do not match the data: {len(want - have)} occurrences missing, {len(have - want)} not demanded"
                    elif any(x[1] not in roles or x[2] is None for x in live):
                        fail = "a node has no valid role or no collection"
                    elif item == "strong-enrichment":
                        codes = {x["strong"] for x, _ in exp if x["strong"]}
                        if codes - {x[3] for x in live}:
                            fail = f"Strong's codes with no node: {sorted(codes - {x[3] for x in live})}"
            if fail:
                problems.append(f"{label}: {fail}")
            else:
                ok_ += 1
            if not dry:
                conn.execute(f"UPDATE collection_layer_item SET validated=?, updated_at={NOW}, run_id=? WHERE id=?", (0 if fail else 1, run_id, lid))
        diff = []
        if rows and not (rep["lexical_missing"] or rep["grouping"]):
            have_k = {(r[3], r[4], r[5]) for r in rows}
            diff = [f"missing: {w['item']} / {L['groups'][w['subgroup_id']]['name']} {w['subject']}".strip() for w in derive(conn, cfg, L, step)
                    if (w["item"], w["subgroup_id"], w["subject"]) not in have_k]
        rep["steps"][step] = {"rows": len(rows), "validated": ok_, "open": open_, "failed": problems, "not_in_ledger": diff,
                              "closed": bool(rows) and not problems and not open_ and not diff}
    return rep


# ══ the group on the node ══════════════════════════════════════════════════════════════════════
def node_groups(conn, run_id: str, dry: bool = False) -> dict:
    """Set ib_node.subgroup_id of every live node from the index (collectionindex.refresh_nodes)."""
    return ci.refresh_nodes(conn, run_id, dry=dry)
