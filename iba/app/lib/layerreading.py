"""layerreading.py -- the layered reading of a collection: stage 1 (step S1 the words), the groups by meaning (step 1.1), the Strong's enrichment (step 1.2) and the pairings (step 2.1)
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
from . import strandreading as sr

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


def needs_pairs(sd: dict) -> bool:
    """A step that reads the typed pairings of the evidence report: the steps of layer 2 and a step that sets `pairs` (3.3)."""
    return sd["layer"] == 2 or bool(sd.get("pairs"))


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
LEXICAL_STEP = "S1"     # the step of stage 1, the lexical analysis (researcher's stages, #2507 v7); the later steps need it closed
WORD_ITEMS = ("word-sense",)


def lexical_status(conn, cfg, L) -> dict:
    """The lexical precondition (researcher 2026-11-14, #2463 v22: lexical and claims readings do not run together; the lexical observations come first; stage 1 of the
    researcher's stages, #2507 v7). It is the step S1 of the ledger: every word (surface and lettered Strong's code) of the collection answered and validated. Matched by
    content through the ledger, never by the stage of an observation (RS-04)."""
    rows = [r for r in _rows(conn, L["cid"], LEXICAL_STEP) if r[6] != "retired"]
    opn = [r for r in rows if r[6] == "open"]
    bad = [r for r in rows if r[6] in ("observed", "none") and r[9] != 1]
    return {"rows": len(rows), "open": len(opn), "unvalidated": len(bad), "closed": bool(rows) and not opn and not bad}


def _is_function(cfg, o: dict) -> bool:
    """RG-22: a function word (preposition, particle, pronoun, article, suffix and the like) gets no observation of its own, except a negator and a connective, which are read for what
    they do (RG-07). The class comes from the morph code by cfg_setting collection.evidence_pairs morph_class; the classes are layer.reading function_classes."""
    if o.get("is_negator"):
        return False
    m = o.get("morph") or ""
    nt = "-" in m or m in ("PREP", "CONJ", "PRT", "ADV", "COND", "INJ", "X")
    table = (cfg.setting("collection.evidence_pairs") or {}).get("morph_class", {})
    cls = table.get("NT" if nt else "OT", {}).get(m.split("-")[0] if nt else (m[1:2] if len(m) > 1 else ""), "")
    return cls in settings(cfg).get("function_classes", [])


def word_subject(o: dict) -> str:
    """The subject of a word item: the surface and the lettered Strong's code (B:113, RG-21), never the bare lemma."""
    return f"{o['surface']}|{o['strong'] or ''}"


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
    if step_def(s, step)["layer"] == 3:     # stage 4, the inner-being analysis (#2528)
        from . import layerinner
        return layerinner.derive(conn, cfg, L, step)
    items = step_def(s, step)["items"]
    th = s["thresholds"]
    out = []
    gids = sorted(L["groups"])
    if any(i in items for i in WORD_ITEMS):
        by = collections.defaultdict(list)
        for o in L["d"]["occurrences"]:
            by[word_subject(o)].append(o)
        words = sorted(w for w, occs in by.items() if not all(_is_function(cfg, o) for o in occs))   # a word of function occurrences only is read with its unit (RG-22)
        out += [{"item": i, "subgroup_id": 0, "subject": w} for w in words for i in WORD_ITEMS if i in items]
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
    if item in WORD_ITEMS:
        return [(o, "member") for o in L["d"]["occurrences"] if word_subject(o) == subject]
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
    L = load(conn, cfg, name, pairs=needs_pairs(sd))
    problems = []
    if sd["layer"] >= 1:
        problems += grouping_gate(conn, cfg, L)
    for need in sd["needs"]:
        if not step_closed(conn, L["cid"], need):
            problems.append(f"step {need} is not closed (every row answered and validated: LayerCheck)"
                            + (" -- the lexical analysis of the words comes first (stage 1)" if need == LEXICAL_STEP else ""))
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
def _lexicon(conn, strong: str, limit: int = 700) -> dict:
    """What the three meaning sources and STEP say of one lettered code (RG-08: read together, none picked and the others dropped): the head sense, the range by the exact code,
    the Greek lexicons (LSJ, Mounce), and the related words. Read-only; trimmed."""
    if not strong:
        return {}
    head = conn.execute("SELECT head FROM strong_sense WHERE strong=? AND deleted=0", (strong,)).fetchone()
    tree = [f"{r[0] or ''} {r[1] or ''}".strip() for r in conn.execute(
        "SELECT sense_code, sense_text FROM strong_meaning_tree WHERE strong_variant=? AND deleted=0 ORDER BY sort", (strong,))]
    lex = conn.execute("SELECT lsj, mounce FROM strong_lexicon WHERE strong=? AND deleted=0", (strong,)).fetchone()
    rel = [f"{r[0]} {r[1] or ''} {r[2] or ''}".strip() for r in conn.execute(
        "SELECT related_strong, related_form, related_gloss FROM strong_related WHERE strong=? AND deleted=0 LIMIT 12", (strong,))]
    return {"sense_head": head[0] if head else None, "meaning_range": "; ".join(tree)[:limit], "lsj": (lex[0] or "")[:limit] if lex else "", "mounce": (lex[1] or "")[:limit] if lex else "",
            "related": rel}


def _prompts(conn, codes: list) -> list[dict]:
    """The catalogue questions of an item, by code (a pointer, not a copy of the bank; they are prompts and are never answered by force, RG-17)."""
    out = []
    for c in codes:
        r = conn.execute("SELECT question_text FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0", (c,)).fetchone()
        if r:
            out.append({"code": c, "question": r[0]})
    return out


def _word_row(conn, s, L, lid, item, idef, subject, nodes, cap, state, reason, seen: dict) -> dict:
    """The working-file row of a word item: every occurrence of the word with its verse and its structural facts from verse_lexical (the base data), the lexicon of its code, the prompts."""
    surface, _, strong = subject.rpartition("|")
    shown = nodes[:cap]
    info = {}
    for part in _chunks([o["vl_id"] for o, _ in shown]):
        for r in conn.execute(f"SELECT id, morph_code, unit_surface, surface_kind, is_negator, party_kind, narrative_morph, gloss_consistent_in_verse FROM verse_lexical "
                              f"WHERE id IN ({','.join('?' * len(part))})", part):
            info[r[0]] = r
    text_of = {}
    for part in _chunks([o["verse_id"] for o, _ in shown]):
        text_of.update({v[0]: v[1] for v in conn.execute(f"SELECT id, text FROM verse WHERE id IN ({','.join('?' * len(part))})", part)})
    ev_nodes = []
    for o, _ in shown:
        i = info.get(o["vl_id"])
        ev_nodes.append({"occurrence": o["vl_id"], "reference": o["reference"], "surface": o["surface"], "strong": o["strong"], "morph": i[1] if i else None,
                         "unit": i[2] if i else None, "surface_kind": i[3] if i else None, "negator": bool(i[4]) if i else False, "party_kind": i[5] if i else None,
                         "gloss_consistent_in_verse": i[7] if i else None, "verse": (text_of.get(o["verse_id"]) or "")[:400]})
    if strong in seen:
        lex = f"same code as the row of {seen[strong]}"
    else:
        seen[strong] = surface
        lex = _lexicon(conn, strong)
    existing = []
    if item in WORD_ITEMS:
        ids = [o["vl_id"] for o, _ in nodes]
        seen_o = {}
        for part in _chunks(ids):
            for r in conn.execute(f"SELECT o.id, o.stage, o.tag, o.question_code, o.obs_text, n.role, n.verse_lexical_id FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id "
                                  f"WHERE o.deleted=0 AND n.deleted=0 AND o.stage!='lexical' AND n.verse_lexical_id IN ({','.join('?' * len(part))}) "
                                  f"AND (o.tag IN ('term','face') OR o.question_code LIKE 'M0.1%' OR o.question_code LIKE 'M0.5%')", part):
                d = seen_o.setdefault(r[0], {"observation": r[0], "stage": r[1], "kind": r[2], "question": r[3], "text": (r[4] or "")[:220], "roles": set(), "occurrences": 0})
                d["roles"].add(r[5])
                d["occurrences"] += 1
        existing = [dict(v, roles=sorted(x for x in v["roles"] if x)) for v in seen_o.values()][:12]
    fill = {"disposition": "observed | adopt", "senses": [{"kind": "term | face", "obs_text": "", "basis": "stated | read", "grounds": "", "occurrences": []}], "member_role": idef["member_role"], "reason": ""}
    if existing:
        fill["observation_id"] = ""
    return {"ledger_id": lid, "item": item, "kind": idef["kind"], "word": surface, "strong": strong, "subject": subject, "asks": idef["asks"],
            "prompts": _prompts(conn, idef.get("prompts", [])) if item in WORD_ITEMS else [], "nodes_total": len(nodes), "nodes_shown": len(ev_nodes), "lexicon": lex,
            "existing_observations": existing, "evidence": ev_nodes, "fill": fill}


def pull(conn, cfg, name: str, step: str, out_dir: pathlib.Path) -> tuple[pathlib.Path, int]:
    s = settings(cfg)
    sd = step_def(s, step)
    L = load(conn, cfg, name, pairs=needs_pairs(sd))
    rows = [r for r in _rows(conn, L["cid"], step) if r[6] == "open" or (r[6] == "observed" and r[9] == 0)]
    if not rows:
        raise LayerError(f"step {step} of {L['name']} has no open row (run LayerOpen, or LayerCheck to see what is validated)")
    if sd["layer"] == 3:     # stage 4: the rows go out in batches of pull_max_rows (#2528)
        from . import layerinner
        return layerinner.pull(conn, cfg, L, step, rows, out_dir)
    out, seen = [], {}
    for r in rows:
        lid, _, _, item, gid, subject, state, oid, reason, val = r
        idef = s["items"][item]
        nodes = expected_nodes(L, item, gid, subject)
        cap = s["pull_max_nodes"]
        if item in WORD_ITEMS:
            out.append(_word_row(conn, s, L, lid, item, idef, subject, nodes, cap, state, reason, seen))
            continue
        text_of = {}
        for part in _chunks([o["verse_id"] for o, _ in nodes[:cap]]):
            text_of.update({v[0]: v[1] for v in conn.execute(f"SELECT id, text FROM verse WHERE id IN ({','.join('?' * len(part))})", part)})
        ev_nodes = [{"reference": o["reference"], "surface": o["surface"], "strong": o["strong"], "as": role, "verse": (text_of.get(o["verse_id"]) or "")[:200]} for o, role in nodes[:cap]]
        codes = collections.Counter(o["strong"] for o, role in nodes if role == "member" and o["strong"])
        seen_o = {}
        for part in _chunks([o["vl_id"] for o, _ in nodes]):
            for r2 in conn.execute(f"SELECT o.id, o.stage, o.tag, o.obs_text, n.role FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 "
                                   f"AND o.stage NOT IN ('layer-1','layer-2','lexical') AND n.verse_lexical_id IN ({','.join('?' * len(part))})", part):
                d2 = seen_o.setdefault(r2[0], {"observation": r2[0], "stage": r2[1], "kind": r2[2], "text": (r2[3] or "")[:200], "roles": set(), "occurrences": 0})
                d2["roles"].add(r2[4])
                d2["occurrences"] += 1
        existing = sorted(({**v, "roles": sorted(x for x in v["roles"] if x)} for v in seen_o.values()), key=lambda v: -v["occurrences"])[:12]
        out.append({"ledger_id": lid, "item": item, "kind": idef["kind"], "group": L["groups"][gid]["name"], "subject": subject, "existing_observations": existing,
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


def _adopt(conn, cfg, L, run_id: str, lid: int, p: dict) -> None:
    """RS-04: an existing observation of any stage that already answers an aspect is kept in place (never filtered by its stage): a node it lacks for a demanded occurrence is added, a node
    with no role takes the role of the item, every change kept with its reason; the ledger row points to it and is validated by the check."""
    aid = p["obs"]
    why = f"adopted by the lexical analysis, ledger row {lid} ({run_id}): {p['reason']}"
    have = {r["verse_lexical_id"]: r for r in conn.execute("SELECT id, verse_lexical_id, role, collection_id FROM ib_node WHERE observation_id=? AND deleted=0", (aid,))}
    vl = _vl(conn, [o["vl_id"] for o, _ in p["nodes"]])
    seq = (conn.execute("SELECT coalesce(max(seq),0) FROM ib_node WHERE observation_id=?", (aid,)).fetchone()[0] or 0)
    stage = conn.execute("SELECT stage FROM ib_observation WHERE id=?", (aid,)).fetchone()[0]
    for o, _ in p["nodes"]:
        n = have.get(o["vl_id"])
        if n is None:
            v = vl[o["vl_id"]]
            seq += 1
            nid = conn.execute("INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, reading_id, created_at, verse_lexical_id, collection_id, subgroup_id) "
                               "VALUES (?,?,?,?,?,?,?,?,NULL,?,?,?,?)", (aid, v[1], v[2], v[3], v[4], stage, seq, p["mrole"], _now(), o["vl_id"], L["cid"], ci.subgroup_for(conn, L["cid"], v[5], v[1]))).lastrowid
            orec.log(conn, aid, nid, "node", None, f"added: {v[2]} {v[3]} ({v[1]}) role {p['mrole']}", why, None, run_id, WHO)
        else:
            if not n["role"]:
                orec.modify_node(cfg, conn, n["id"], {"role": p["mrole"]}, why, None, run_id, WHO)
            if n["collection_id"] is None:
                orec.modify_node(cfg, conn, n["id"], {"collection_id": L["cid"]}, why, None, run_id, WHO)
    conn.execute(f"UPDATE collection_layer_item SET state='observed', observation_id=?, reason=?, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (aid, "adopted: " + p["reason"], run_id, lid))


def _text_rules(cfg, conn, s, idef, text: str, basis, grounds, nodes, where: str, errors: list) -> None:
    """The rules of an observation's text, the same ones the readings enforce (observationrecord.check): an observation is founded in its verses and never repeats their text
    (B:131, more than reading.observation_items max_verse_words_copied consecutive words), a quotation is the ESV's wording (the quote check of the narrative and the readings), a read
    observation names its grounds in the words of the verse (parts.grounds, RS-08), and where the item says so the text names the verses it is tied to (B:131)."""
    minr = s["min_reason_chars"]
    for x, _ in nodes:
        cp = orec.copies_verse(cfg, [text], x.get("text") or "")
        if cp:
            errors.append(f"{where}: the text restates the verse {x['reference']} ({cp!r}); say what the word does in it (B:131, RW-04)")
            break
    errors += [f"{b} is not the ESV's wording (quote check)" for b in sr._quote_check(conn, cfg, [text], where)]
    if idef.get("tie_to_verse") and nodes:
        refs = {x[0]["reference"] for x in nodes}
        if not any(rf in text for rf in refs):
            errors.append(f"{where}: B:131 an observation is tied to its verses: the text names none of them ({sorted(refs)[:3]})")
    if basis == "read":
        g = (grounds or "").strip()
        if len(g) < minr:
            errors.append(f"{where}: a read observation names its grounds in the words of the verse (grounds, {minr} characters or more)")
        elif idef.get("grounds_in") == "lexicon":
            blob = " ".join(" ".join(str(v) for v in _lexicon(conn, c, 4000).values() if v) for c in {x[0]["strong"] for x in nodes if x[0].get("strong")}).lower()
            if g.lower() not in blob:
                errors.append(f"{where}: the grounds {g!r} are not words of the lexicon entries of the codes the observation is about (the dictionary meaning is the ground of this item)")
        elif nodes and not any(g.lower() in (x[0].get("text") or "").lower() for x in nodes):
            errors.append(f"{where}: the grounds {g!r} are not words of the verses the observation is tied to")


def record(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check the filled file whole and write it in one savepoint; any problem refuses all. keep=False rolls back (the preview)."""
    s = settings(cfg)
    name, step = data.get("collection"), data.get("step")
    sd = step_def(s, step)
    if sd["layer"] == 3:     # stage 4: the findings of the inner-being reading (#2528)
        from . import layerinner
        return layerinner.record(conn, cfg, run_id, data, keep)
    L = load(conn, cfg, name, pairs=needs_pairs(sd))
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
        if idef.get("multi") and disp != "adopt":
            senses = fill.get("senses") or []
            allnodes = expected_nodes(L, item, gid, subject)
            byid = {x[0]["vl_id"]: x for x in allnodes}
            byref = collections.defaultdict(list)
            for x in allnodes:
                byref[x[0]["reference"]].append(x)
            covered, built = set(), []
            if not senses:
                errors.append(f"{where}: {item} is answered by senses (fill.senses): at least one, each with its text and the occurrences it holds for")
            for k, sn in enumerate(senses, 1):
                sw = f"{where} sense {k}"
                text = (sn.get("obs_text") or "").strip()
                kind = (sn.get("kind") or "").strip()
                if kind not in idef.get("kinds", [idef["kind"]]):
                    errors.append(f"{sw}: kind must be one of {idef.get('kinds', [idef['kind']])}")
                try:
                    recordingpass._validate_obs_text(conn, text)
                except recordingpass.InvalidObservationText as exc:
                    errors.append(f"{sw}: {exc}")
                if len(text) < s["min_text_chars"]:
                    errors.append(f"{sw}: the observation text is missing or under {s['min_text_chars']} characters")
                dup = orec.live_text(conn, text) if text else None
                own = {r_[0] for r_ in conn.execute("SELECT id FROM ib_observation WHERE stable_key LIKE ? AND deleted=0", (f"layer:{lr[0]}:%",))}
                if dup and dup["id"] not in own:
                    errors.append(f"{sw}: this description is already live as observation {dup['id']}")
                if text in seen:
                    errors.append(f"{sw}: the same text as {seen[text]}")
                seen[text] = sw
                if sn.get("basis") not in bases:
                    errors.append(f"{sw}: basis must be one of {sorted(bases)}")
                named = sn.get("occurrences") or []
                nodes = []
                for n_ in named:
                    hit = [byid[n_]] if n_ in byid else byref.get(n_, [])
                    if not hit:
                        errors.append(f"{sw}: {n_!r} is not an occurrence of {subject}")
                    nodes += hit
                nodes = list({x[0]["vl_id"]: x for x in nodes}.values())
                if not nodes:
                    errors.append(f"{sw}: names no occurrence (fill occurrences: occurrence ids or verse references)")
                covered |= {x[0]["vl_id"] for x in nodes}
                if nodes:
                    _text_rules(cfg, conn, s, idef, text, sn.get("basis"), sn.get("grounds"), nodes, sw, errors)
                built.append({"kind": kind, "text": text, "basis": sn.get("basis"), "grounds": (sn.get("grounds") or "").strip() or None, "nodes": nodes})
            if senses and set(byid) - covered:
                errors.append(f"{where}: {len(set(byid) - covered)} occurrences of {subject} are in no sense (every occurrence is read, none left out)")
            plan.append({"ledger": lr, "disp": "multi", "senses": built, "idef": idef, "mrole": (fill.get("member_role") or idef["member_role"]).strip()})
            continue
        if disp == "none":
            if not idef["none_allowed"]:
                errors.append(f"{where}: {item} cannot be recorded as none; it needs an observation")
            elif len((fill.get("reason") or "").strip()) < minr:
                errors.append(f"{where}: none needs its reason, in words ({minr} characters or more)")
            plan.append({"ledger": lr, "disp": "none", "reason": (fill.get("reason") or "").strip()})
            continue
        if disp == "adopt":
            aid, reason = fill.get("observation_id"), (fill.get("reason") or "").strip()
            ob = conn.execute("SELECT id, tag, deleted FROM ib_observation WHERE id=?", (aid,)).fetchone() if aid else None
            if ob is None or ob[2]:
                errors.append(f"{where}: adopt names a live observation (fill.observation_id)")
                continue
            if ob[1] not in idef.get("kinds", [idef["kind"]]):
                errors.append(f"{where}: observation {aid} has kind {ob[1]}, the item takes {idef.get('kinds', [idef['kind']])}")
            if len(reason) < minr:
                errors.append(f"{where}: adopt needs its reason in words ({minr} characters or more): what the observation already says of the word")
            nodes = expected_nodes(L, item, gid, subject)
            if idef.get("subset"):
                named = fill.get("occurrences") or []
                nodes = [x for x in nodes if x[0]["vl_id"] in named or x[0]["reference"] in named]
            groups = orec.node_role_groups(cfg)
            inner = set(groups.get("relevant", [])) | set(groups.get("bears_on", []))
            bad = []
            if nodes and inner:
                bad = [r[0] for r in conn.execute(
                    f"SELECT n.id FROM ib_node n WHERE n.observation_id=? AND n.deleted=0 AND n.role IN ({','.join('?' * len(inner))}) AND n.verse_lexical_id IN ({','.join('?' * len(nodes))})",
                    [aid] + sorted(inner) + [x[0]["vl_id"] for x in nodes])]
            if bad:
                errors.append(f"{where}: observation {aid} is an inner-being finding (its nodes carry an inner-being role); it is not a lexical observation and is not adopted")
            if not nodes:
                errors.append(f"{where}: no occurrence to adopt for")
            plan.append({"ledger": lr, "disp": "adopt", "obs": aid, "reason": reason, "nodes": nodes, "mrole": (fill.get("member_role") or idef["member_role"]).strip(), "idef": idef})
            continue
        if disp != "observed":
            errors.append(f"{where}: disposition must be observed, none or adopt")
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
        if idef.get("subset"):
            named = fill.get("occurrences") or []
            hit = [x for x in nodes if x[0]["vl_id"] in named or x[0]["reference"] in named]
            unknown = [n for n in named if not any(x[0]["vl_id"] == n or x[0]["reference"] == n for x in nodes)]
            if not named:
                errors.append(f"{where}: {item} names the occurrences it is about (fill.occurrences: occurrence ids or verse references); none given")
            if unknown:
                errors.append(f"{where}: occurrences that are not occurrences of {subject}: {unknown[:5]}")
            nodes = hit
        if nodes:
            _text_rules(cfg, conn, s, idef, text, fill.get("basis"), fill.get("grounds"), nodes, where, errors)
        plan.append({"ledger": lr, "disp": "observed", "text": text, "grounds": (fill.get("grounds") or "").strip() or None, "basis": fill.get("basis"), "route": route, "mrole": mrole, "prole": prole, "nodes": nodes, "idef": idef})
    if errors:
        raise LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
    conn.execute("SAVEPOINT layer_record")
    res = {"observed": 0, "none": 0, "nodes": 0, "withdrawn": 0}
    try:
        stage = s["stages"][str(sd["layer"])]
        vl = _vl(conn, [o["vl_id"] for p in plan if p["disp"] == "observed" for o, _ in p["nodes"]])
        for p in plan:
            lid, old = p["ledger"][0], p["ledger"][7]
            if p["disp"] == "multi":
                for (prev,) in conn.execute("SELECT id FROM ib_observation WHERE stable_key LIKE ? AND deleted=0", (f"layer:{lid}:%",)).fetchall():
                    for (pn,) in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (prev,)).fetchall():
                        orec.delete_node(conn, pn, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                    orec.soft_delete_observation(conn, prev, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                    res["withdrawn"] += 1
                first = None
                stage = s["stages"][str(sd["layer"])]
                vlm = _vl(conn, [o["vl_id"] for sn in p["senses"] for o, _ in sn["nodes"]])
                for k, sn in enumerate(p["senses"], 1):
                    pj = {"item": p["ledger"][3], "step": step, "word": p["ledger"][5]}
                    if sn.get("grounds"):
                        pj["grounds"] = sn["grounds"]
                    pj = json.dumps(pj, ensure_ascii=False)
                    msrc = recordingpass.normalise_meaning_source(conn, p["idef"].get("meaning_source", "verse-text"))
                    oid = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, window, obs_text, basis, route, parts, meaning_source, status, stable_key, run_id, created_at) "
                                       "VALUES (NULL,?,?,?,?,?,NULL,?,?,'draft',?,?,?)",
                                       (stage, sn["kind"], p["idef"].get("window"), sn["text"], sn["basis"], pj, msrc, f"layer:{lid}:{run_id}:{k}", run_id, _now())).lastrowid
                    orec.log(conn, oid, None, "created", None, sn["text"], f"layer observation {p['ledger'][3]} for ledger row {lid}", None, run_id, WHO)
                    first = first or oid
                    seq = 0
                    for o, _ in sn["nodes"]:
                        v = vlm[o["vl_id"]]
                        seq += 1
                        nid = conn.execute("INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, reading_id, created_at, verse_lexical_id, collection_id, subgroup_id) "
                                           "VALUES (?,?,?,?,?,?,?,?,NULL,?,?,?,?)", (oid, v[1], v[2], v[3], v[4], stage, seq, p["mrole"], _now(), o["vl_id"], L["cid"], ci.subgroup_for(conn, L["cid"], v[5], v[1]))).lastrowid
                        orec.log(conn, oid, nid, "node", None, f"added: {v[2]} {v[3]} ({v[1]}) role {p['mrole']}", f"layer node of ledger row {lid}", None, run_id, WHO)
                        res["nodes"] += 1
                    res["observed"] += 1
                conn.execute(f"UPDATE collection_layer_item SET state='observed', observation_id=?, reason=NULL, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (first, run_id, lid))
                continue
            if old and p["disp"] != "adopt" and conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND deleted=0", (old,)).fetchone():
                for (pn,) in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (old,)).fetchall():
                    orec.delete_node(conn, pn, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                orec.soft_delete_observation(conn, old, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                res["withdrawn"] += 1
            if p["disp"] == "none":
                conn.execute(f"UPDATE collection_layer_item SET state='none', observation_id=NULL, reason=?, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (p["reason"], run_id, lid))
                res["none"] += 1
                continue
            if p["disp"] == "adopt":
                _adopt(conn, cfg, L, run_id, lid, p)
                res["adopted"] = res.get("adopted", 0) + 1
                continue
            pj = {"item": p["ledger"][3], "step": step}
            if p["ledger"][3] in WORD_ITEMS:
                pj["word"] = p["ledger"][5]
            if p.get("grounds"):
                pj["grounds"] = p["grounds"]
            parts = json.dumps(pj, ensure_ascii=False)
            msrc = recordingpass.normalise_meaning_source(conn, p["idef"].get("meaning_source", "verse-text"))
            oid = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, window, obs_text, basis, route, parts, meaning_source, status, stable_key, run_id, created_at) "
                               "VALUES (NULL,?,?,?,?,?,?,?,?,'draft',?,?,?)",
                               (stage, p["idef"]["kind"], p["idef"].get("window"), p["text"], p["basis"], p["route"], parts, msrc, f"layer:{lid}:{run_id}", run_id, _now())).lastrowid
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
    rep = {"collection": L1["name"], "grouping": grouping_gate(conn, cfg, L1), "steps": {}}
    rep["lexical"] = lexical_status(conn, cfg, L1)   # stage 1 is read from its own step below, after the checks have set `validated`
    for sd in s["steps"]:
        step = sd["key"]
        if needs_pairs(sd) and L2 is None:
            L2 = load(conn, cfg, name, pairs=True)
        L = L2 if needs_pairs(sd) else L1
        rows = [r for r in _rows(conn, L["cid"], step) if r[6] != "retired"]
        problems, ok_, open_ = [], 0, 0
        for r in rows:
            lid, _, _, item, gid, subject, state, oid, reason, val = r
            label = (f"{item} / {L['groups'].get(gid, {}).get('name', f'group {gid}')}" if gid else f"{item}") + (f" / {subject}" if subject else "")
            if state == "open":
                open_ += 1
                continue
            idef = s["items"][item]
            fail = None
            if sd["layer"] == 3:     # stage 4: re-derived and validated by layerinner.check_row (#2528)
                from . import layerinner
                fail = layerinner.check_row(conn, cfg, s, L, sd, r)
                if fail:
                    problems.append(f"{label}: {fail}")
                else:
                    ok_ += 1
                if not dry:
                    conn.execute(f"UPDATE collection_layer_item SET validated=?, updated_at={NOW}, run_id=? WHERE id=?", (0 if fail else 1, run_id, lid))
                continue
            if idef.get("multi") and state == "observed" and not (reason or "").startswith("adopted"):
                obs_ = [r_[0] for r_ in conn.execute("SELECT id FROM ib_observation WHERE stable_key LIKE ? AND deleted=0", (f"layer:{lid}:%",))]
                exp = expected_nodes(L, item, gid, subject)
                want = {x["vl_id"] for x, _ in exp}
                if not obs_:
                    fail = "its observations are missing or withdrawn"
                else:
                    have, bad_kind, bad_node = set(), 0, 0
                    for oid_ in obs_:
                        o_ = conn.execute("SELECT stage, tag FROM ib_observation WHERE id=?", (oid_,)).fetchone()
                        if o_[0] != s["stages"][str(sd["layer"])] or o_[1] not in idef.get("kinds", [idef["kind"]]):
                            bad_kind += 1
                        nl = conn.execute("SELECT verse_lexical_id, role, collection_id FROM ib_node WHERE observation_id=? AND deleted=0", (oid_,)).fetchall()
                        if not nl:
                            bad_node += 1
                        have |= {x_[0] for x_ in nl}
                        bad_node += sum(1 for x_ in nl if x_[1] not in roles or x_[2] is None)
                    if bad_kind:
                        fail = f"{bad_kind} observations have a stage or kind the item does not take"
                    elif want - have or have - want:
                        fail = f"its senses do not cover the occurrences: {len(want - have)} in no sense, {len(have - want)} not demanded"
                    elif bad_node:
                        fail = "an observation has no node, or a node has no valid role or no collection"
                if fail:
                    problems.append(f"{label}: {fail}")
                else:
                    ok_ += 1
                if not dry:
                    conn.execute(f"UPDATE collection_layer_item SET validated=?, updated_at={NOW}, run_id=? WHERE id=?", (0 if fail else 1, run_id, lid))
                continue
            if state == "none":
                if not idef["none_allowed"] or len((reason or "").strip()) < s["min_reason_chars"]:
                    fail = "recorded as none without a permitted reason"
            else:
                o = conn.execute("SELECT stage, tag, deleted FROM ib_observation WHERE id=?", (oid,)).fetchone() if oid else None
                if o is None or o[2]:
                    fail = "its observation is missing or withdrawn"
                elif (o[0] != s["stages"][str(sd["layer"])] and not (reason or "").startswith("adopted")) or o[1] not in idef.get("kinds", [idef["kind"]]):
                    fail = f"its observation has stage {o[0]} and kind {o[1]}, not {s['stages'][str(sd['layer'])]} and {idef['kind']}"
                elif gid and gid not in L["groups"]:
                    fail = "its group is retired or missing"
                else:
                    exp = expected_nodes(L, item, gid, subject)
                    want = {x["vl_id"] for x, _ in exp}
                    live = conn.execute("SELECT verse_lexical_id, role, collection_id, strong FROM ib_node WHERE observation_id=? AND deleted=0", (oid,)).fetchall()
                    have = {x[0] for x in live}
                    if (reason or "").startswith("adopted"):
                        if not want <= have:
                            fail = f"the adopted observation lacks a node for {len(want - have)} demanded occurrences"
                    elif idef.get("subset"):
                        if not have or not have <= want:
                            fail = f"its nodes must be occurrences of the word and at least one: {len(have - want)} not demanded"
                    elif want != have:
                        fail = f"its nodes do not match the data: {len(want - have)} occurrences missing, {len(have - want)} not demanded"
                    if fail:
                        pass
                    elif any(x[1] not in roles or x[2] is None for x in ([y for y in live if y[0] in want] if (reason or "").startswith("adopted") else live)):
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
        if rows and (sd["layer"] == 0 or not rep["grouping"]):
            have_k = {(r[3], r[4], r[5]) for r in rows}
            diff = [f"missing: {w['item']} / {L['groups'][w['subgroup_id']]['name'] if w['subgroup_id'] else ''} {w['subject']}".strip() for w in derive(conn, cfg, L, step)
                    if (w["item"], w["subgroup_id"], w["subject"]) not in have_k]
        rep["steps"][step] = {"rows": len(rows), "validated": ok_, "open": open_, "failed": problems, "not_in_ledger": diff,
                              "closed": bool(rows) and not problems and not open_ and not diff}
    rep["lexical"] = dict(lexical_status(conn, cfg, L1), closed=bool(rep["steps"].get(LEXICAL_STEP, {}).get("closed")))
    return rep


# ══ the group on the node ══════════════════════════════════════════════════════════════════════
def node_groups(conn, run_id: str, dry: bool = False) -> dict:
    """Set ib_node.subgroup_id of every live node from the index (collectionindex.refresh_nodes)."""
    return ci.refresh_nodes(conn, run_id, dry=dry)
