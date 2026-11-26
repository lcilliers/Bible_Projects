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
import hashlib
import pickle
import datetime
import json
import pathlib

from . import collectionevidence as ev
from . import collectionindex as ci
from . import buildvalidate as bv
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


def conn_of(cfg):
    return cfg.conn


def settings(cfg) -> dict:
    s = cfg.setting("layer.reading")
    if not s:
        raise LayerError("cfg_setting layer.reading is missing")
    missing = []     # the config the validation in the build reads (migration validation_in_build_2538_v1_20261124): said once, plainly, in place of a KeyError deep in a record
    if not cfg.setting("layer.scan"):
        missing.append("cfg_setting layer.scan")
    for key, flag in (("3.1", "open_gate"), ("3.3", "closing_gate")):
        if not any(st["key"] == key and st.get(flag) for st in s.get("steps", [])):
            missing.append(f"layer.reading step {key} {flag}")
    cols_ = {r[1] for r in conn_of(cfg).execute("PRAGMA table_info(collection_layer_item)")}
    for c_ in ("pulled_at", "answered_at", "checked_at"):
        if c_ not in cols_:
            missing.append(f"collection_layer_item.{c_} (apply iba/app/migration/archive/findings_2538_v1_20261125.py)")
    if bv.OLD_ITEM not in s.get("items", {}):
        missing.append(f"layer.reading item {bv.OLD_ITEM} (apply iba/app/migration/archive/findings_2538_v1_20261125.py)")
    if missing:
        raise LayerError("the code is ahead of the config: " + ", ".join(missing) + " not set; apply iba/app/migration/archive/validation_in_build_2538_v1_20261124.py "
                         "(then archive/grouping_first_2538_v1_20261124.py) before the layered reading runs")
    return s


def step_def(s: dict, key: str) -> dict:
    for st in s["steps"]:
        if st["key"] == key:
            return st
    raise LayerError(f"{key!r} is not a step of the layered reading ({', '.join(x['key'] for x in s['steps'])})")


def check_natures(cfg, s: dict, sd: dict) -> None:
    """The marker is set at creation from the item (#2538, VA-05): every item of the step names a nature that is a value of cfg_enum ib_observation.nature.
    A finding file never sets it. A step with an item that has none is refused before anything is read or written."""
    allowed = set(cfg.enum("ib_observation.nature"))
    bad = [i for i in sd["items"] if not s["items"][i].get("ledger_only") and s["items"][i].get("nature") not in allowed]
    if bad:
        raise LayerError(f"the item(s) {bad} of step {sd['key']} have no nature in cfg_setting layer.reading (one of {sorted(allowed)}); nothing is written")


def settle_nodes(conn, s: dict, oid: int, run_id: str, layer: int) -> list[str]:
    """The required columns of the word nodes of a new observation (cfg_setting layer.reading node_required), checked as the nodes are written (#2538, VA-02).
    A column of node_gap_columns that the data cannot give (an empty morph in the source row, a surface with no subgroup) is left empty and its reason is kept on the node
    (disposition_note, validationactions.note_node); any other missing column is a problem, returned for the caller to refuse the whole file with."""
    from . import validationactions as va
    from_layer = s["node_required_from_layer"]       # a column that exists only once an earlier step is done (the subgroup, after the grouping)
    req = [c for c in s["node_required"] if layer >= from_layer.get(c, 0)]
    gaps_ok = set(s["node_gap_columns"])
    problems = []
    for r in conn.execute(f"SELECT id, verse_reference, surface, verse_lexical_id, {', '.join(req)} FROM ib_node WHERE observation_id=? AND deleted=0 "
                          "AND traced_observation_id IS NULL ORDER BY seq", (oid,)).fetchall():
        d = dict(zip(["id", "verse_reference", "surface", "verse_lexical_id"] + req, r))
        missing = [c for c in req if d[c] in (None, "")]
        bad = [c for c in missing if c not in gaps_ok]
        if bad:
            problems.append(f"observation {oid} node {d['id']} ({d['verse_reference']} {d['surface']}) has no {', '.join(bad)}")
            continue
        if missing:
            why = []
            for c in missing:
                if c == "morph_code":
                    src = conn.execute("SELECT morph_code FROM verse_lexical WHERE id=?", (d["verse_lexical_id"],)).fetchone()
                    if src is None or src[0] not in (None, ""):
                        problems.append(f"observation {oid} node {d['id']}: morph_code is empty but its verse_lexical row {d['verse_lexical_id']} holds one")
                        continue
                    why.append("morph_code: the source row verse_lexical %s has none" % d["verse_lexical_id"])
                else:
                    why.append(f"{c}: the surface has no placement in the collection index")
            if why:
                va.note_node(conn, d["id"], "empty at creation, the data gives none -- " + "; ".join(why), run_id, WHO)
    return problems


def needs_pairs(sd: dict) -> bool:
    """A step that reads the typed pairings of the evidence report: the steps of layer 2 and a step that sets `pairs` (3.3)."""
    return sd["layer"] == 2 or bool(sd.get("pairs"))


def _chunks(ids):
    ids = sorted(set(ids))
    for i in range(0, len(ids), CHUNK):
        yield ids[i:i + CHUNK]


# ══ the data of a collection ═══════════════════════════════════════════════════════════════════
def _dataset_path(conn, cid: int, gid: int):
    """Where the dataset of one subgroup is held while its loop runs: beside the database it was pulled from (a copy of the database has its own)."""
    f = conn.execute("PRAGMA database_list").fetchone()[2]
    return (pathlib.Path(f).parent / "dataset" / f"subgroup-{cid}-{gid}.pkl") if f else None


def release_dataset(conn, cid: int, gid: int) -> bool:
    """The dataset is released when step 3.1 closes for the subgroup (the end of its loop), and discarded when a new loop starts."""
    p = _dataset_path(conn, cid, gid)
    if p is not None and p.exists():
        p.unlink()
        return True
    return False


def load(conn, cfg, name: str, pairs: bool = False, subgroup=None) -> dict:
    """The collection, its member occurrences (by the one membership rule of the evidence report), its index rows and groups; with pairs=True the typed pairings of layer 2.
    `subgroup` (a name, an id, or a set of ids): the subgroup being read, in isolation (researcher 2026-11-24, #2538: "for each subgroup in isolation (not all subgroups at once)"; the
    read of the base data is as targeted as possible). Only the occurrences of the surfaces placed in those subgroups, and the verses they stand in, are read. None reads the whole
    collection (the steps that are the collection's own: 3.2 and 3.3)."""
    try:
        cid, cname = ci._collection(conn, name)
        vals = ev.read_settings(cfg)
        order = ev.Order(conn)
        col = ev.resolve(conn, [cname])[0]
    except (ci.IndexError_, ev.EvidenceError) as exc:
        raise LayerError(str(exc))
    index = conn.execute("SELECT i.id, i.term_id, t.surface, i.strong, i.subgroup_id, i.state, i.reason FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id "
                         "WHERE i.deleted=0 AND i.collection_id=?", (cid,)).fetchall()
    groups = {r[0]: {"id": r[0], "name": r[1], "status": r[2]} for r in conn.execute(
        "SELECT id, name, status FROM collection_subgroup WHERE deleted=0 AND collection_id=? AND status!='retired'", (cid,))}
    scope, only = None, None
    if subgroup not in (None, "", set(), frozenset()):
        if isinstance(subgroup, (set, frozenset, list, tuple)):
            scope = set(subgroup)
        elif isinstance(subgroup, int):
            scope = {subgroup}
        else:
            scope = {subgroup_id({"groups": groups, "name": cname}, subgroup)}
        only = {r[2] for r in index if r[4] in scope and r[5] == "placed"}
    # THE SUBGROUP DATASET (researcher 2026-11-25: "B1 - C1 all use the same input data"; lifecycle B1 to C1): the base data of one subgroup (its surfaces, occurrences, verses, the typed pairings) is pulled ONCE
    # and held for the loop; every step reads the same data. The observations are not in it: they are read live from the tables. It is valid while the subgroup's place in the index is what it was
    # (a signature); a change of the grouping discards it and the loop starts again.
    gid1 = next(iter(scope)) if scope and len(scope) == 1 else None
    path = _dataset_path(conn, cid, gid1) if gid1 else None
    sig = hashlib.sha1(json.dumps([cid, gid1, sorted([r[1], r[2], r[3], r[4], r[5]] for r in index if r[4] == gid1)], default=str).encode()).hexdigest() if gid1 else None
    blob = None
    if path is not None and path.exists():
        try:
            blob = pickle.loads(path.read_bytes())
            if blob.get("sig") != sig:
                blob = None
        except Exception:      # an unreadable dataset is rebuilt
            blob = None
    fresh = blob is None
    try:
        d = blob["d"] if blob else ev.build_collection(conn, col, vals["tiers"], order, lean=True, only_surfaces=only)
    except ev.EvidenceError as exc:
        raise LayerError(str(exc))
    L = {"cid": cid, "name": cname, "d": d, "vals": vals, "order": order, "index": index, "groups": groups, "scope": scope}
    if fresh:
        by = {(r[2], r[3]): r for r in index}
        for o in d["occurrences"]:
            r = by.get((o["surface"], o["strong"])) or by.get((o["surface"], None))
            o["group"] = r[4] if r and r[5] == "placed" and r[4] in groups else None
            o["index_state"] = r[5] if r else "not indexed"
    L["col_ids"] = {r[1]: r[0] for r in conn.execute("SELECT id, name FROM collection WHERE deleted=0 AND status='confirmed'")}
    if pairs:
        if blob and blob.get("pairs") is not None:
            L["pairs"] = blob["pairs"]
        else:
            L["pairs"] = ev.build_pairs(conn, d, vals, order)
            fresh = True
    if path is not None and fresh:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(pickle.dumps({"sig": sig, "cid": cid, "gid": gid1, "d": d, "pairs": L.get("pairs") if pairs else (blob or {}).get("pairs")}, protocol=pickle.HIGHEST_PROTOCOL))
    return L


# ══ the gates ══════════════════════════════════════════════════════════════════════════════════
LEXICAL_STEP = "S1"     # the step of stage 1, the lexical analysis (researcher's stages, #2507 v7); the later steps need it closed
WORD_ITEMS = ("word-sense",)


def lexical_status(conn, cfg, L) -> dict:
    """The lexical precondition (researcher 2026-11-14, #2463 v22: lexical and claims readings do not run together; the lexical observations come first; stage 1 of the
    researcher's stages, #2507 v7). It is the step S1 of the ledger: every word (surface and lettered Strong's code) of the collection answered and validated. Matched by
    content through the ledger, never by the stage of an observation (RS-04)."""
    rows = [r for r in conn.execute("SELECT id, collection_id, step, item, subgroup_id, subject, state, observation_id, reason, validated FROM collection_layer_item WHERE deleted=0 AND collection_id=? AND item=?", (L["cid"], WORD_ITEMS[0])) if r[6] != "retired"]
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
        # a word is read inside the subgroup of its surface (#2538, 2026-11-24): the surface is placed whole in one subgroup, so every occurrence of the word carries the same group
        out += [{"item": i, "subgroup_id": next((o["group"] for o in by[w] if o["group"]), 0), "subject": w} for w in words for i in WORD_ITEMS if i in items]
    if "group-definition" in items:
        out += [{"item": "group-definition", "subgroup_id": g, "subject": ""} for g in gids]
    if "strong-enrichment" in items:
        out += [{"item": "strong-enrichment", "subgroup_id": g, "subject": ""} for g in gids]
    for gate in ("sweep", "evidence-validation"):      # the gates at the end of 2.1 (B4, B5; #2538): one ledger-only row for each subgroup, answered by ReadSweep and ReadEvidence
        if gate in items:
            out += [{"item": gate, "subgroup_id": g, "subject": ""} for g in gids]
    if any(i in items for i in ("pairing", "qualifier", "entity", "direction", "double-meaning")):
        # step 2.1 (researcher 2026-11-24 and 2026-11-25): the rows come from the data, one for each (subgroup, item), and for the pairing one for each partner collection; each is answered by the findings
        # it holds, a finding being one observation with a node for each occurrence (each verse) it holds in ("the same surface for multiple verses = multiple nodes, not multiple observations; the
        # same applies to B3"). No threshold on the number of shared verses (never the researcher's); a subgroup never joins another in an observation (they are pulled together at 3.2).
        name2id = {g["name"]: g["id"] for g in L["groups"].values()}
        partner, qual, ent = set(), set(), set()
        for p in L["pairs"]["pairs"]:
            g = name2id.get(p["member"]["subgroup"])
            if g is None:
                continue
            o = p["other"]
            if o["type"] == "word of another collection":
                for cn in o["collections"]:
                    partner.add((g, cn))
            if o["qualifier"]:
                qual.add(g)
            if o["type"].startswith("entity"):
                ent.add(g)
        if "pairing" in items:
            out += [{"item": "pairing", "subgroup_id": g, "subject": cn} for g, cn in sorted(partner)]
        if "qualifier" in items:
            out += [{"item": "qualifier", "subgroup_id": g, "subject": ""} for g in sorted(qual)]
        if "entity" in items:
            out += [{"item": "entity", "subgroup_id": g, "subject": ""} for g in sorted(ent)]
        if "direction" in items:
            out += [{"item": "direction", "subgroup_id": g, "subject": ""} for g in sorted(ent)]
        if "double-meaning" in items:       # a surface compared across its verses: one for each surface that carries more than one code
            codes = collections.defaultdict(set)
            for o in L["d"]["occurrences"]:
                if o["group"] and o["strong"]:
                    codes[(o["group"], o["surface"])].add(o["strong"])
            out += [{"item": "double-meaning", "subgroup_id": g, "subject": sf} for (g, sf), cs in sorted(codes.items()) if len(cs) >= 2]
    if bv.OLD_ITEM in items:      # the old observations in scope, each tracked in the ledger from the first step to its fate (researcher 2026-11-25)
        sdl = step_def(s, step)["layer"]
        for g in (sorted(L["scope"]) if L.get("scope") else gids):
            vls_ = [o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == g]
            older = bv.older_on(conn, cfg, s, vls_, sdl)
            done = bv.settled(conn, cfg, older)
            cmap = bv.carried_to_map(conn, older)
            out += [{"item": bv.OLD_ITEM, "subgroup_id": g, "subject": str(o)} for o in sorted(older) if o not in done and ((step == "S1" and o not in cmap) or cmap.get(o) == step)]
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


def wordnet_control(conn, L: dict, gid: int) -> dict:
    """The WordNet control of the pairings of a subgroup (researcher, 2026-11-24, #2538: step 2.1 compares the pairings WordNet gives with the pairings the verse-lexical gives).
    {partner collection name: {"pairs": n, "types": {type: n}, "examples": [{"surface", "partner_surface", "type", "weight"}]}} for the surfaces of the subgroup that WordNet relates
    (surface_relation) to a surface that is a member of another collection (collection_link). Indexed lookups on term_a_id and term_b_id, in chunks."""
    mine = [r[1] for r in L["index"] if r[4] == gid and r[5] == "placed"]
    name_of = {r[1]: r[2] for r in L["index"]}
    rel = []
    for part in _chunks(mine):
        marks = ",".join("?" * len(part))
        for a, b, pt, w in conn.execute(f"SELECT term_a_id, term_b_id, pair_type, weight FROM surface_relation WHERE deleted=0 AND term_a_id IN ({marks})", part):
            rel.append((a, b, pt, w))
        for a, b, pt, w in conn.execute(f"SELECT term_b_id, term_a_id, pair_type, weight FROM surface_relation WHERE deleted=0 AND term_b_id IN ({marks})", part):
            rel.append((a, b, pt, w))
    inmine = set(mine)
    others = sorted({b for a, b, _, _ in rel if b not in inmine})
    colls = collections.defaultdict(set)
    for part in _chunks(others):
        for tid, cname in conn.execute(f"SELECT l.term_id, c.name FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE l.deleted=0 AND c.deleted=0 AND c.status='confirmed' "
                                       f"AND c.id!=? AND l.term_id IN ({','.join('?' * len(part))})", [L["cid"]] + part):
            colls[tid].add(cname)
    surf = {}
    for part in _chunks(others):
        surf.update(conn.execute(f"SELECT id, surface FROM surface_term WHERE id IN ({','.join('?' * len(part))})", part).fetchall())
    out = {}
    for a, b, pt, w in rel:
        for cn in colls.get(b, ()):
            d = out.setdefault(cn, {"pairs": 0, "types": collections.Counter(), "examples": []})
            d["pairs"] += 1
            d["types"][pt] += 1
            if len(d["examples"]) < 5:
                d["examples"].append({"surface": name_of.get(a), "partner_surface": surf.get(b), "type": pt, "weight": w})
    for d in out.values():
        d["types"] = dict(d["types"])
    return out


def control_for(L: dict, gid: int, wn: dict) -> dict:
    """What the verse-lexical pairings of the subgroup (the typed pairings of the load, partner collections by word) say against the WordNet control: the collections both name, the ones
    only WordNet relates (a pairing the verses may not show, or one to look for), and the ones only the verses pair (no WordNet relation to check them by)."""
    name = L["groups"][gid]["name"]
    verse = collections.Counter()
    for p in L["pairs"]["pairs"]:
        if p["member"]["subgroup"] == name and p["other"]["type"] == "word of another collection":
            for cn in p["other"]["collections"]:
                verse[cn] += 1
    return {"both": sorted(set(verse) & set(wn)), "wordnet_only": sorted(set(wn) - set(verse)), "verse_only": sorted(set(verse) - set(wn)),
            "verse_pairings": dict(verse), "wordnet_pairs": {k: v["pairs"] for k, v in wn.items()}}


def _rows(conn, cid, step=None):
    q = "SELECT id, collection_id, step, item, subgroup_id, subject, state, observation_id, reason, validated FROM collection_layer_item WHERE deleted=0 AND collection_id=?"
    a = [cid]
    if step:
        q += " AND step=?"
        a.append(step)
    return conn.execute(q + " ORDER BY id", a).fetchall()


def step_closed(conn, cid: int, step: str, gid: int | None = None) -> bool:
    """Every live row of the step answered and validated. With gid (the loop over the subgroups, #2538): the rows of that subgroup only; a subgroup the data demands nothing of in the step
    has no rows and open_step settles that from the data (need_closed)."""
    allrows = [r for r in _rows(conn, cid, step) if r[6] != "retired"]
    rows = allrows if gid is None else [r for r in allrows if r[4] == gid]
    return bool(rows) and all(r[6] in ("observed", "none") and r[9] == 1 for r in rows)


# ══ open: derive the ledger ════════════════════════════════════════════════════════════════════
def need_closed(conn, cfg, L: dict, need: str, gid: int | None) -> bool:
    """A needed step is closed for the collection, or for one subgroup: its rows answered and validated; a subgroup the data demands nothing of in that step (no pairing, say) is closed once
    the step has rows for the collection or for another subgroup of it."""
    if step_closed(conn, L["cid"], need, gid):
        return True
    if gid is None:
        return False
    live = [r for r in _rows(conn, L["cid"], need) if r[6] != "retired"]
    if any(r[4] == gid for r in live):
        return False
    nd = step_def(settings(cfg), need)
    Ln = L if (L.get("pairs") or not needs_pairs(nd)) else load(conn, cfg, L["name"], pairs=True, subgroup=L.get("scope"))
    return not any(w["subgroup_id"] == gid for w in derive(conn, cfg, Ln, need))


def subgroup_id(L: dict, subgroup: str | None) -> int | None:
    """The id of a live subgroup of the collection named in -Subgroup, or None for the whole collection."""
    if not subgroup:
        return None
    hit = [g["id"] for g in L["groups"].values() if g["name"].lower() == subgroup.strip().lower()]
    if not hit:
        raise LayerError(f"{subgroup!r} is not a live subgroup of {L['name']}: {', '.join(sorted(g['name'] for g in L['groups'].values()))}")
    return hit[0]


def legacy_rows(conn, cid: int, step: str, sd: dict, gid, want: list) -> list:
    """The live rows of a step read after the grouping that sit under no subgroup (the reading of the whole collection made before the loop) and name a word the data now demands of the
    subgroup being opened: the word is read again inside its subgroup, so the older row and its observations are superseded."""
    if gid is None or not sd.get("after_grouping"):
        return []
    subj = {w["subject"] for w in want}
    return [r for r in _rows(conn, cid, step) if r[4] in (0, None) and r[6] != "retired" and r[5] in subj]


def superseded_rows(conn, s: dict, cid: int, step: str, gid) -> list:
    """The answered rows of the step being opened for a subgroup, and of every later step (the subgroup's own rows and the rows of the collection, such as 3.2), whose observation is older
    than an observation of an earlier step in that subgroup: the earlier reading was recorded again after the row was answered, so the row stands on a reading that has been replaced and is
    read again (#2538, 2026-11-24). The test is the creation time of the observations (the ledger's updated_at moves with every LayerCheck, so it cannot say)."""
    order = [x["key"] for x in s["steps"]]
    idx = order.index(step)
    if gid is None or idx == 0:
        return []
    rows = _rows(conn, cid)
    up = ""
    for r in rows:
        if r[2] in order[:idx] and r[4] == gid and r[6] == "observed" and r[7]:
            t = conn.execute("SELECT created_at FROM ib_observation WHERE id=? AND deleted=0", (r[7],)).fetchone()
            if t and t[0]:
                up = max(up, t[0])
    out = []
    for r in rows:
        if up and r[2] in order[idx:] and r[2] != "S1" and r[4] in (gid, 0) and r[6] == "observed" and r[7]:
            t = conn.execute("SELECT created_at FROM ib_observation WHERE id=?", (r[7],)).fetchone()
            if t and t[0] and t[0] < up:
                out.append(r)
    return out


def _withdraw_row(conn, r, why: str, run_id: str) -> None:
    """Every live observation of a ledger row (the one it points to and those its findings wrote under its stable key) is withdrawn with its nodes, with the reason."""
    for (prev,) in conn.execute("SELECT id FROM ib_observation WHERE deleted=0 AND (id=? OR (stable_key >= ? AND stable_key < ?))", (r[7] or 0, f"layer:{r[0]}:", f"layer:{r[0]};")).fetchall():
        for (pn,) in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (prev,)).fetchall():
            orec.delete_node(conn, pn, why, None, run_id, WHO)
        orec.soft_delete_observation(conn, prev, why, None, run_id, WHO)


def open_step(conn, cfg, run_id: str, name: str, step: str, dry: bool = False, subgroup: str | None = None) -> dict:
    """With `subgroup` the step is opened for that subgroup alone (the loop of #2538, 2026-11-24): its rows are derived and its needs and gates are judged for it; the rows of the other
    subgroups are neither added nor retired. What an earlier reading of the subgroup has replaced is superseded first (the whole-collection S1 rows of its words, the rows built on a
    reading recorded again since: their observations are withdrawn and the rows read again), so the evidence gate judges the subgroup as it will stand; a refusal or a preview undoes it."""
    s = settings(cfg)
    sd = step_def(s, step)
    if subgroup:      # the loop is for ONE subgroup at a time, B1 to C1 (researcher 2026-11-25): a subgroup waits while another is further through its loop and not finished
        from . import layerloop
        why = layerloop.order_gate(conn, cfg, name, subgroup)
        if why:
            raise LayerError(why)
    if subgroup and not dry and step == s["steps"][0]["key"]:      # the first step of the loop pulls the dataset afresh
        try:
            _cid, _ = ci._collection(conn, name)
            _g = [g[0] for g in conn.execute("SELECT id FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (_cid, subgroup.strip().lower()))]
            if _g:
                release_dataset(conn, _cid, _g[0])
        except ci.IndexError_:
            pass
    L = load(conn, cfg, name, pairs=needs_pairs(sd), subgroup=subgroup)
    gid = subgroup_id(L, subgroup)
    problems = []
    if sd["layer"] >= 1 or sd.get("after_grouping"):      # the words (S1) are read after the grouping, inside the subgroup of their surface (#2538, 2026-11-24)
        problems += grouping_gate(conn, cfg, L)
    for need in sd["needs"]:
        if not need_closed(conn, cfg, L, need, gid):
            problems.append(f"step {need} is not closed (every row answered and validated: LayerCheck)"
                            + (" -- the lexical analysis of the words comes first (stage 1)" if need == LEXICAL_STEP else ""))
    if sd.get("open_gate") == "evidence" and gid and not problems:
        n_old = conn.execute("SELECT count(*) FROM collection_layer_item WHERE collection_id=? AND item=? AND subgroup_id=? AND deleted=0 AND state='open'", (L["cid"], bv.OLD_ITEM, gid)).fetchone()[0]
        if n_old:
            problems.append(f"{n_old} old observation(s) of the subgroup are still open in the ledger (carried forward and not taken up, or not answered): answer each (older) before the evidence is judged")
    if sd.get("closing_gate") and not problems:      # 3.3: every partner collection of the aspects the data demands is complete before the step opens
        from . import layerinner
        pn = layerinner.match_partners(w["subject"] for w in derive(conn, cfg, L, step))
        problems += ["partner collection " + x for x in bv.partner_gaps(conn, pn, declared=s.get("partner_complete") or [])]
        problems += ["the nodes do not carry the collections 3.3 reads: " + x for x in layerinner.cross_gaps(conn, L)]      # 3.3 depends on the collection being recorded on the nodes of both sides (researcher 2026-11-25)
    if problems:
        raise LayerError(f"step {step} of {L['name']} cannot be opened:\n  " + "\n  ".join(problems))
    want = [w for w in derive(conn, cfg, L, step) if gid is None or w["subgroup_id"] == gid]
    legacy = legacy_rows(conn, L["cid"], step, sd, gid, want)
    sup = superseded_rows(conn, s, L["cid"], step, gid)
    conn.execute("SAVEPOINT open_step")
    for r in legacy:      # the whole-collection row of a word now read inside its subgroup: retired, its observations withdrawn
        _withdraw_row(conn, r, f"read again inside its subgroup under the loop of #2538 ({run_id})", run_id)
        conn.execute(f"UPDATE collection_layer_item SET state='retired', validated=0, updated_at={NOW}, run_id=?, reason=? WHERE id=?", (run_id, "read again inside its subgroup (#2538)", r[0]))
    for r in sup:         # a row built on a reading that was recorded again since: its observations withdrawn, the row read again
        _withdraw_row(conn, r, f"the reading it rests on was recorded again ({run_id})", run_id)
        conn.execute(f"UPDATE collection_layer_item SET state='open', observation_id=NULL, answered_at=NULL, checked_at=NULL, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (run_id, r[0]))
    gate = []
    if sd.get("open_gate") == "evidence" and not dry:      # the evidence validation repairs first (researcher 2026-11-22: repair first, delete last): nodes completed or explained, builds of other collections marked and deferred
        vls_ = [o["vl_id"] for o in L["d"]["occurrences"] if gid is None or o["group"] == gid]
        done_ = bv.complete_nodes(conn, cfg, s, vls_, L["cid"], run_id)
        done_.update(bv.mark_builds(conn, cfg, s, vls_, L["cid"], run_id))
        out_extra = done_
    else:
        out_extra = {}
    if sd.get("open_gate") == "evidence":
        gate = ["the evidence validation of " + (f"the subgroup {subgroup}" if gid else "the collection") + " does not pass: " + x for x in bv.closing_gate(conn, cfg, L["cid"], "evidence", gid)]
    if gate or dry:
        conn.execute("ROLLBACK TO open_step")
        conn.execute("RELEASE open_step")
    else:
        conn.execute("RELEASE open_step")
    if gate:
        raise LayerError(f"step {step} of {L['name']} cannot be opened:\n  " + "\n  ".join(gate))
    have = {(r[3], r[4], r[5]): r for r in _rows(conn, L["cid"], step) if gid is None or r[4] == gid}
    key = lambda w: (w["item"], w["subgroup_id"], w["subject"])  # noqa: E731
    add = [w for w in want if key(w) not in have]
    wanted = {key(w) for w in want}
    retire = [r for k, r in have.items() if k not in wanted and r[6] != "retired" and not (r[3] == bv.OLD_ITEM and r[6] == "observed")]
    revive = [r for k, r in have.items() if k in wanted and r[6] == "retired"]
    out = {"collection": L["name"], "step": step, "demanded": len(want), "add": len(add), "retire": len(retire), "revive": len(revive) + sum(1 for r in sup if r[2] == step),
           "legacy": len(legacy), "superseded": len(sup), **out_extra}
    if dry:
        return out
    for w in add:
        conn.execute("INSERT INTO collection_layer_item (collection_id, step, item, subgroup_id, subject, state, run_id, created_by) VALUES (?,?,?,?,?,'open',?,?)",
                     (L["cid"], step, w["item"], w["subgroup_id"], w["subject"], run_id, BY))
    for r in retire:
        _withdraw_row(conn, r, f"the data no longer demands this aspect, so the observations of its row are withdrawn ({run_id})", run_id)      # a retired row leaves no live observation behind (found when thought was regrouped: the old groups' observations stayed live)
        conn.execute(f"UPDATE collection_layer_item SET state='retired', validated=0, updated_at={NOW}, run_id=?, reason='the data no longer demands this aspect' WHERE id=?", (run_id, r[0]))
    for k, r in have.items():      # a row retired earlier whose observations are still live (the retire above did not withdraw them then): withdrawn now
        if k not in wanted and r[6] == "retired":
            _withdraw_row(conn, r, f"the row was retired because the data no longer demands it; its observations are withdrawn ({run_id})", run_id)
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
                                  f"WHERE o.deleted=0 AND n.deleted=0 AND o.stage!='lexical' AND (o.nature IS NULL OR o.nature='evidence') AND n.verse_lexical_id IN ({','.join('?' * len(part))}) "
                                  f"AND (o.tag IN ('term','face') OR o.question_code LIKE 'M0.1%' OR o.question_code LIKE 'M0.5%')", part):
                d = seen_o.setdefault(r[0], {"observation": r[0], "stage": r[1], "kind": r[2], "question": r[3], "text": (r[4] or ""), "roles": set(), "occurrences": 0})
                d["roles"].add(r[5])
                d["occurrences"] += 1
        existing = [dict(v, roles=sorted(x for x in v["roles"] if x)) for v in seen_o.values()]      # all of them, in full
    fill = {"disposition": "observed | adopt", "senses": [{"kind": "term | face", "obs_text": "", "basis": "stated | read", "grounds": "", "occurrences": []}], "member_role": idef["member_role"], "reason": ""}
    if existing:
        fill["observation_id"] = ""
    return {"ledger_id": lid, "item": item, "kind": idef["kind"], "word": surface, "strong": strong, "subject": subject, "asks": idef["asks"],
            "prompts": _prompts(conn, idef.get("prompts", [])) if item in WORD_ITEMS else [], "nodes_total": len(nodes), "nodes_shown": len(ev_nodes), "lexicon": lex,
            "existing_observations": existing, "evidence": ev_nodes, "fill": fill}


def pull(conn, cfg, name: str, step: str, out_dir: pathlib.Path, subgroup: str | None = None) -> tuple[pathlib.Path, int]:
    s = settings(cfg)
    sd = step_def(s, step)
    L = load(conn, cfg, name, pairs=needs_pairs(sd) or bool(subgroup), subgroup=subgroup)      # a subgroup pull carries its verses in full (verse-lexical words), so the pairs are built
    only = subgroup_id(L, subgroup)     # None: the whole collection (the loop below reuses the name gid for the group of each row)
    rows = [r for r in _rows(conn, L["cid"], step) if (r[6] == "open" or (r[6] == "observed" and r[9] == 0)) and (only is None or r[4] == only) and r[3] != bv.OLD_ITEM
            and not s["items"].get(r[3], {}).get("ledger_only")]      # a ledger-only row (the sweep, the evidence validation) is answered by its own command, not by a pull
    old_open = conn.execute("SELECT id, subject, step, reason FROM collection_layer_item WHERE collection_id=? AND item=? AND deleted=0 AND state='open'" + (" AND subgroup_id=?" if only else ""),
                            [L["cid"], bv.OLD_ITEM] + ([only] if only else [])).fetchall()
    if not rows and not old_open:
        raise LayerError(f"step {step} of {L['name']} has no open row (run LayerOpen, or LayerCheck to see what is validated)")
    for ids_ in _chunks([r[0] for r in rows] + [r[0] for r in old_open]):      # the ledger is stamped as the work happens: the pull is an event of each row it takes out
        conn.execute(f"UPDATE collection_layer_item SET pulled_at={NOW}, updated_at={NOW} WHERE id IN ({','.join('?' * len(ids_))})", ids_)
    if sd["layer"] == 3:     # stage 4: the rows go out in batches of pull_max_rows (#2528)
        from . import layerinner
        return layerinner.pull(conn, cfg, L, step, rows, out_dir)
    out, seen, ctl, wn_of = [], {}, {}, {}
    for r in rows:
        lid, _, _, item, gid, subject, state, oid, reason, val = r
        idef = s["items"][item]
        nodes = expected_nodes(L, item, gid, subject)
        if sd["key"] == "2.1" and gid and gid not in wn_of:      # the WordNet control, once for each subgroup
            wn_of[gid] = wordnet_control(conn, L, gid)
            ctl[L["groups"][gid]["name"]] = control_for(L, gid, wn_of[gid])
        cap = len(nodes) if idef.get("multi") else s["pull_max_nodes"]      # a row answered by senses or findings is given EVERY occurrence: the record demands every one (found on the biggest subgroup of thought, 212 occurrences against a cap of 80, 2026-11-25)
        if item in WORD_ITEMS:
            out.append(_word_row(conn, s, L, lid, item, idef, subject, nodes, cap, state, reason, seen))
            continue
        text_of = {}
        for part in _chunks([o["verse_id"] for o, _ in nodes[:cap]]):
            text_of.update({v[0]: v[1] for v in conn.execute(f"SELECT id, text FROM verse WHERE id IN ({','.join('?' * len(part))})", part)})
        ev_nodes = [{"occurrence": o["vl_id"], "reference": o["reference"], "surface": o["surface"], "strong": o["strong"], "as": role, "verse": (text_of.get(o["verse_id"]) or "")} for o, role in nodes[:cap]]
        codes = collections.Counter(o["strong"] for o, role in nodes if role == "member" and o["strong"])
        seen_o = {}
        for part in _chunks([o["vl_id"] for o, _ in nodes]):
            for r2 in conn.execute(f"SELECT o.id, o.stage, o.tag, o.obs_text, n.role FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 "
                                   f"AND o.stage NOT IN ('layer-1','layer-2','lexical') AND (o.nature IS NULL OR o.nature='evidence') AND n.verse_lexical_id IN ({','.join('?' * len(part))})", part):
                d2 = seen_o.setdefault(r2[0], {"observation": r2[0], "stage": r2[1], "kind": r2[2], "text": (r2[3] or ""), "roles": set(), "occurrences": 0})
                d2["roles"].add(r2[4])
                d2["occurrences"] += 1
        existing = sorted(({**v, "roles": sorted(x for x in v["roles"] if x)} for v in seen_o.values()), key=lambda v: -v["occurrences"])      # all of them, in full (researcher 2026-11-24)
        carries = []
        for rule_ in ([idef["carries_all_of"]] if idef.get("carries_all_of") else idef.get("traces_to") or []):       # what the row's observations trace to: shown whole, so the senses can be formed and traced
            for xid in trace_targets(conn, 0, [o["vl_id"] for o, _ in nodes], [rule_], L["cid"]):
                r3 = conn.execute("SELECT id, stage, tag, obs_text FROM ib_observation WHERE id=?", (xid,)).fetchone()
                refs3 = [r_[0] for r_ in conn.execute("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_reference IS NOT NULL", (xid,))]
                carries.append({"observation": r3[0], "stage": r3[1], "kind": r3[2], "text": r3[3] or "", "verses": refs3})
        extra = {"to_trace": carries} if carries else {}
        if item == "pairing" and sd["key"] == "2.1":      # the WordNet control of the partner collection of the row
            extra = {**extra, "wordnet_control": wn_of.get(gid, {}).get(subject.replace("collection:", ""))}
        out.append({"ledger_id": lid, "item": item, "kind": idef["kind"], "group": L["groups"][gid]["name"], "subject": subject, "existing_observations": existing, **extra,
                    "asks": idef["asks"], "nodes_total": len(nodes), "nodes_shown": len(ev_nodes), "strong_codes": dict(codes), "evidence": ev_nodes,
                    "fill": ({"disposition": "observed | none" if idef["none_allowed"] else "observed", "senses": [{"kind": idef["kind"], "obs_text": "", "basis": "stated | read", "grounds": "", "occurrences": []}],
                              "member_role": idef["member_role"], "partner_role": idef.get("partner_role", ""), "reason": "",
                              "_how": "one entry for each distinct finding; occurrences: the occurrence ids or the verse references it holds in; together every demanded occurrence"} if idef.get("multi") else
                             {"disposition": "observed | none" if idef["none_allowed"] else "observed", "obs_text": "", "basis": "stated | read",
                              "route": "A | B | C" if idef.get("route") else "", "member_role": idef["member_role"], "partner_role": idef.get("partner_role", ""), "reason": ""})})
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"layer-{L['name']}-{step}-{_now()[:10].replace('-', '')}.json"
    head = {"collection": L["name"], "step": step, "pulled": _now(), **({"control": ctl} if ctl else {})}
    if only:       # the pull of a subgroup in isolation (researcher 2026-11-24): its verses in full (verse text and every verse-lexical word), the subgroup, the WordNet pairings
        head["subgroup"] = L["groups"][only]["name"]
        head["subgroup_surfaces"] = sorted({f"{r[2]}" + (f"|{r[3]}" if r[3] else "") for r in L["index"] if r[4] == only and r[5] == "placed"})
        head["wordnet"] = wn_of.get(only) or wordnet_control(conn, L, only)
        head["verses"] = subgroup_verses(conn, L)
    if old_open:       # the old observations in scope still open in the ledger, whole: answered in a row's `fill.older`, or in the top-level `older` list of the record file
        olds = []
        for lid_, subj_, step_, reason_ in old_open:
            if not str(subj_).isdigit():
                continue
            o_ = conn.execute("SELECT id, stage, tag, nature, obs_text FROM ib_observation WHERE id=? AND deleted=0", (int(subj_),)).fetchone()
            if o_ is None:
                continue
            refs_ = [r_[0] for r_ in conn.execute("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_reference IS NOT NULL", (o_[0],))]
            olds.append({"ledger_id": lid_, "observation": o_[0], "stage": o_[1], "kind": o_[2], "nature": o_[3], "text": o_[4] or "", "verses": refs_, "ledger_step": step_, "note": reason_,
                         "answer": {"observation": o_[0], "action": "keep | restate | merge | consume | delete_neither | defer | carry", "reason": "", "nature": "", "to": ""}})
        head["old_observations"] = olds
    if sd.get("sweep_unmarked") and only:     # the unmarked observations of the subgroup, reviewed for deletion in the loop (#2538)
        head["subgroup"] = L["groups"][only]["name"]
        head["unmarked"] = sorted(unmarked_of(conn, cfg, s, L, only).values(), key=lambda v: -v["occurrences"])
        head["delete_unmarked"] = []     # fill: [{"observation": id, "reason": "why it is neither evidence nor inner being"}]; the others stay and are answered when their row is recorded
    path.write_text(json.dumps({**head, "rows": out}, ensure_ascii=False, indent=1), encoding="utf-8")
    return path, len(out)


def subgroup_verses(conn, L: dict) -> list[dict]:
    """Every verse the subgroup's occurrences stand in, in Scripture order: the full verse text and every live verse-lexical word of the verse (position, surface, Strong's code, morph,
    the type the pairing gives it, whether it is an occurrence of the subgroup). Read for the verse ids of the subgroup only (idx_verse_lexical_verse_id, the verse primary key)."""
    rows = L["pairs"]["rows"]
    vids = sorted({o["verse_id"] for o in L["d"]["occurrences"]})
    text = {}
    for part in _chunks(vids):
        text.update({v[0]: v[1] for v in conn.execute(f"SELECT id, text FROM verse WHERE id IN ({','.join('?' * len(part))})", part)})
    by = collections.defaultdict(list)
    for x in rows:
        by[x["verse_id"]].append(x)
    out = []
    for v in sorted(by, key=lambda i: by[i][0]["sk"]):
        ws = sorted(by[v], key=lambda x: (x["position"] if x["position"] is not None else 0, x["code_ordinal"] or 0, x["vl_id"]))
        out.append({"reference": ws[0]["reference"], "text": text.get(v) or "",
                    "words": [{"vl_id": x["vl_id"], "position": x["position"], "surface": x["surface"], "strong": x["strong"], "morph": x["morph"], "type": x["type"],
                               "qualifier": x["qualifier"], "occurrence_of_subgroup": bool(x["member"])} for x in ws]})
    return out


def unmarked_of(conn, cfg, s: dict, L: dict, gid: int) -> dict:
    """The older live observations without a marker on the occurrences of one subgroup, not yet judged by a reading (buildvalidate.unmarked_in)."""
    return bv.unmarked_in(conn, cfg, s, [o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid])


# ══ record: check whole, write whole ═══════════════════════════════════════════════════════════
def trace_targets(conn, oid: int, vl_ids, rules: list, cid: int) -> list[int]:
    """The live observations a new observation rests on (researcher 2026-11-25: B2 is traceable back to B1, B3 builds on B2 and sometimes B1, the traces are captured in the nodes): for each rule
    {stage, tag?} the live observations of that stage (and tag) of this collection that hold a live word node on any of the given occurrences. Searched by idx_ib_node_verse_lexical_id in chunks."""
    out: list[int] = []
    ids = sorted(set(vl_ids))
    for rule in rules or []:
        for part in _chunks(ids):
            # the ledger row is read from the key ('layer:<row id>:...') and found by its primary key; a LIKE join walked every row of the collection for each observation (#2538)
            q = ("SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
                 "JOIN collection_layer_item c ON c.id=CAST(substr(o.stable_key, 7, instr(substr(o.stable_key, 7), ':') - 1) AS INTEGER) "
                 "WHERE o.stable_key LIKE 'layer:%' AND n.deleted=0 AND o.deleted=0 AND c.deleted=0 AND c.state!='retired' AND c.collection_id=? AND n.traced_observation_id IS NULL AND o.stage=? "
                 # a row of a group that is deleted or retired is not the subgroup's earlier step (#2538: a subgroup opened alone after a regrouping saw the old group's 1.1 sense)
                 "AND NOT EXISTS (SELECT 1 FROM collection_subgroup g WHERE g.id=c.subgroup_id AND (g.deleted=1 OR g.status='retired')) "
                 + ("AND o.tag=? " if rule.get("tag") else "") + f"AND o.id!=? AND n.verse_lexical_id IN ({','.join('?' * len(part))})")
            a = [cid, rule["stage"]] + ([rule["tag"]] if rule.get("tag") else []) + [oid] + part
            for (x,) in conn.execute(q, a):
                if x not in out:
                    out.append(x)
    return sorted(out)


def write_traces(conn, oid: int, targets: list, cid: int, gid, stage: str, seq: int, run_id: str, lid: int) -> int:
    """A TRACED node for each target observation: it names the observation (traced_observation_id) and carries no word of its own. Returns the new last seq."""
    for tid in targets:
        if conn.execute("SELECT 1 FROM ib_node WHERE observation_id=? AND traced_observation_id=? AND deleted=0", (oid, tid)).fetchone():
            continue
        seq += 1
        nid = conn.execute("INSERT INTO ib_node (observation_id, traced_observation_id, source_stage, seq, created_at, collection_id, subgroup_id) VALUES (?,?,?,?,?,?,?)",
                           (oid, tid, stage, seq, _now(), cid, gid)).lastrowid
        orec.log(conn, oid, nid, "node", None, f"traced: rests on observation {tid}", f"layer trace of ledger row {lid}", None, run_id, WHO)
    return seq


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
    from . import validationactions as va
    va.set_nature(cfg, conn, aid, p["idef"]["nature"], why, run_id, WHO)          # an adopted observation takes the marker of the item that adopts it (#2538)
    orec.log(conn, aid, None, "build_answer", None, "adopt", why, None, run_id, WHO)
    conn.execute(f"UPDATE collection_layer_item SET answered_at={NOW}, state='observed', observation_id=?, reason=?, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (aid, "adopted: " + p["reason"], run_id, lid))


def _row_obs(conn, lid: int, oid) -> list[int]:
    """The live observations a ledger row stands on: those with its stable key (idx_ib_observation_stable_key) and the one it points to."""
    ids = {r[0] for r in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};"))}
    if oid:
        ids.add(oid)
    return sorted(ids)


def _text_rules(cfg, conn, s, idef, text: str, basis, grounds, nodes, where: str, errors: list) -> None:
    """The rules of an observation's text, the same ones the readings enforce (observationrecord.check): an observation is founded in its verses and never repeats their text
    (B:131, more than reading.observation_items max_verse_words_copied consecutive words), a quotation is the ESV's wording (the quote check of the narrative and the readings), a read
    observation names its grounds in the words of the verse (parts.grounds, RS-08), and where the item says so the text names the verses it is tied to (B:131)."""
    minr = s["min_reason_chars"]
    lacking = sorted({x["verse_id"] for x, _ in nodes if not x.get("text") and x.get("verse_id")})      # an occurrence from the pairing load (2.1) carries no verse text: read it (#2538)
    if lacking:
        text_of = {}
        for part in _chunks(lacking):
            text_of.update({v[0]: v[1] for v in conn.execute(f"SELECT id, text FROM verse WHERE id IN ({','.join('?' * len(part))})", part)})
        nodes = [({**x, "text": text_of.get(x.get("verse_id")) or ""} if not x.get("text") else x, r) for x, r in nodes]
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


def file_scope(conn, name: str, step: str, data: dict):
    """The subgroups the rows of a filled file belong to: the loop records one subgroup at a time, so the read is limited to it (researcher 2026-11-24). None when a row is the
    collection's own (3.2, 3.3) or the file names a row the ledger does not hold (the record then refuses it)."""
    try:
        cid, _ = ci._collection(conn, name)
    except ci.IndexError_ as exc:
        raise LayerError(str(exc))
    led = {r[0]: r[4] for r in _rows(conn, cid, step)}
    gs = set()
    for row in data.get("rows", []):
        g = led.get(row.get("ledger_id"))
        if not g:
            return None
        gs.add(g)
    if not gs and data.get("subgroup"):      # a file of old-observation answers only names its subgroup
        r = conn.execute("SELECT id FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (cid, str(data["subgroup"]).strip().lower())).fetchone()
        if r:
            gs.add(r[0])
    return gs or None


def record(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check the filled file whole and write it in one savepoint; any problem refuses all. keep=False rolls back (the preview)."""
    s = settings(cfg)
    name, step = data.get("collection"), data.get("step")
    sd = step_def(s, step)
    check_natures(cfg, s, sd)
    if sd["layer"] == 3:     # stage 4: the findings of the inner-being reading (#2528)
        from . import layerinner
        return layerinner.record(conn, cfg, run_id, data, keep)
    L = load(conn, cfg, name, pairs=needs_pairs(sd), subgroup=file_scope(conn, name, step, data))
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
        if idef.get("ledger_only"):
            errors.append(f"{where}: a {item} row is answered by its own command (ReadSweep or ReadEvidence), not by a working file")
            continue
        fill = row.get("fill") or row
        disp = fill.get("disposition")
        if idef.get("multi") and disp not in ("adopt", "none"):
            senses = fill.get("senses") or fill.get("findings") or []
            if (fill.get("route") or "").strip() and not idef.get("route"):
                errors.append(f"{where}: this item takes no route")
            allnodes = expected_nodes(L, item, gid, subject)
            byid = {x[0]["vl_id"]: x for x in allnodes}
            byref = collections.defaultdict(list)
            for x in allnodes:
                byref[x[0]["reference"]].append(x)
            covered, built = set(), []
            if not senses:
                errors.append(f"{where}: {item} is answered by {'senses' if item in WORD_ITEMS else 'its findings'} (fill.senses): at least one, each with its text and the occurrences it holds in")
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
                own = {r_[0] for r_ in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lr[0]}:", f"layer:{lr[0]};"))}
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
                if idef.get("exactly_once"):
                    twice = sorted({x[0]["vl_id"] for x in nodes} & covered)
                    if twice:
                        errors.append(f"{sw}: {len(twice)} occurrence(s) are already in another sense (each occurrence is in exactly one sense; for example {twice[:4]})")
                covered |= {x[0]["vl_id"] for x in nodes}
                if nodes:
                    _text_rules(cfg, conn, s, idef, text, sn.get("basis"), sn.get("grounds"), nodes, sw, errors)
                rests = [x for x in (sn.get("rests_on") or []) if isinstance(x, int)]
                for x in rests:
                    ok_ = conn.execute("SELECT stage FROM ib_observation WHERE id=? AND deleted=0", (x,)).fetchone()
                    if ok_ is None:
                        errors.append(f"{sw}: rests_on names observation {x}, which is not a live observation")
                built.append({"kind": kind, "text": text, "basis": sn.get("basis"), "grounds": (sn.get("grounds") or "").strip() or None, "nodes": nodes, "rests_on": rests})
            if senses and set(byid) - covered:
                errors.append(f"{where}: {len(set(byid) - covered)} occurrences of {subject} are in no sense (every occurrence is read, none left out)")
            plan.append({"ledger": lr, "disp": "multi", "senses": built, "idef": idef, "mrole": (fill.get("member_role") or idef["member_role"]).strip(), "prole": (fill.get("partner_role") or idef.get("partner_role") or "").strip(), "older": fill.get("older")})
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
        plan.append({"ledger": lr, "disp": "observed", "text": text, "grounds": (fill.get("grounds") or "").strip() or None, "basis": fill.get("basis"), "route": route, "mrole": mrole, "prole": prole, "nodes": nodes, "idef": idef, "older": fill.get("older")})
    if errors:
        raise LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
    conn.execute("SAVEPOINT layer_record")
    res = {"observed": 0, "none": 0, "nodes": 0, "withdrawn": 0}
    node_problems: list[str] = []
    texts = bv.scope_texts(conn, cfg, L["cid"]) if any(x["disp"] in ("observed", "multi") for x in plan) else {}
    try:
        stage = s["stages"][str(sd["layer"])]
        vl = _vl(conn, [o["vl_id"] for p in plan if p["disp"] == "observed" for o, _ in p["nodes"]])
        for p in plan:
            lid, old = p["ledger"][0], p["ledger"][7]
            if p["disp"] == "multi":
                for (prev,) in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};")).fetchall():
                    for (pn,) in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (prev,)).fetchall():
                        orec.delete_node(conn, pn, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                    orec.soft_delete_observation(conn, prev, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                    res["withdrawn"] += 1
                first = None
                row_ids: list[int] = []
                stage = s["stages"][str(sd["layer"])]
                vlm = _vl(conn, [o["vl_id"] for sn in p["senses"] for o, _ in sn["nodes"]])
                for k, sn in enumerate(p["senses"], 1):
                    pj = {"item": p["ledger"][3], "step": step, "word": p["ledger"][5]}
                    if sn.get("grounds"):
                        pj["grounds"] = sn["grounds"]
                    pj = json.dumps(pj, ensure_ascii=False)
                    msrc = recordingpass.normalise_meaning_source(conn, p["idef"].get("meaning_source", "verse-text"))
                    oid = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, window, obs_text, basis, route, parts, meaning_source, status, stable_key, run_id, created_at, nature) "
                                       "VALUES (NULL,?,?,?,?,?,NULL,?,?,'draft',?,?,?,?)",
                                       (stage, sn["kind"], p["idef"].get("window"), sn["text"], sn["basis"], pj, msrc, f"layer:{lid}:{run_id}:{k}", run_id, _now(), p["idef"]["nature"])).lastrowid
                    orec.log(conn, oid, None, "created", None, sn["text"], f"layer observation {p['ledger'][3]} for ledger row {lid}", None, run_id, WHO)
                    first = first or oid
                    row_ids.append(oid)
                    seq = 0
                    for o, role_of in sn["nodes"]:
                        v = vlm[o["vl_id"]]
                        seq += 1
                        cid_ = L["cid"]
                        if role_of == "partner" and len(o.get("collections") or []) == 1 and o["collections"][0] in L["col_ids"]:
                            cid_ = L["col_ids"][o["collections"][0]]
                        mr_ = p["mrole"] if role_of == "member" else (p.get("prole") or p["mrole"])
                        nid = conn.execute("INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, reading_id, created_at, verse_lexical_id, collection_id, subgroup_id) "
                                           "VALUES (?,?,?,?,?,?,?,?,NULL,?,?,?,?)", (oid, v[1], v[2], v[3], v[4], stage, seq, mr_, _now(), o["vl_id"], cid_, ci.subgroup_for(conn, cid_, v[5], v[1]))).lastrowid
                        orec.log(conn, oid, nid, "node", None, f"added: {v[2]} {v[3]} ({v[1]}) role {mr_}", f"layer node of ledger row {lid}", None, run_id, WHO)
                        res["nodes"] += 1
                    seq = write_traces(conn, oid, sorted(set(trace_targets(conn, oid, [o["vl_id"] for o, r_ in sn["nodes"] if r_ == "member"], p["idef"].get("traces_to"), L["cid"])) | set(sn.get("rests_on") or [])),
                                       L["cid"], p["ledger"][4], stage, seq, run_id, lid)
                    node_problems += settle_nodes(conn, s, oid, run_id, sd["layer"])
                    res["observed"] += 1
                node_problems += bv.settle_row(conn, cfg, s, L["cid"], row_ids, p.get("older"), run_id, texts, sd["layer"], sd["key"], {o["vl_id"] for o in L["d"]["occurrences"]})
                conn.execute(f"UPDATE collection_layer_item SET answered_at={NOW}, state='observed', observation_id=?, reason=NULL, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (first, run_id, lid))
                continue
            if old and p["disp"] != "adopt" and conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND deleted=0", (old,)).fetchone():
                for (pn,) in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (old,)).fetchall():
                    orec.delete_node(conn, pn, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                orec.soft_delete_observation(conn, old, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                res["withdrawn"] += 1
            if p["disp"] == "none":
                conn.execute(f"UPDATE collection_layer_item SET answered_at={NOW}, state='none', observation_id=NULL, reason=?, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (p["reason"], run_id, lid))
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
            oid = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, window, obs_text, basis, route, parts, meaning_source, status, stable_key, run_id, created_at, nature) "
                               "VALUES (NULL,?,?,?,?,?,?,?,?,'draft',?,?,?,?)",
                               (stage, p["idef"]["kind"], p["idef"].get("window"), p["text"], p["basis"], p["route"], parts, msrc, f"layer:{lid}:{run_id}", run_id, _now(), p["idef"]["nature"])).lastrowid
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
            node_problems += settle_nodes(conn, s, oid, run_id, sd["layer"])
            node_problems += bv.settle_row(conn, cfg, s, L["cid"], [oid], p.get("older"), run_id, texts, sd["layer"], sd["key"], {o["vl_id"] for o in L["d"]["occurrences"]})
            conn.execute(f"UPDATE collection_layer_item SET answered_at={NOW}, state='observed', observation_id=?, reason=NULL, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (oid, run_id, lid))
            res["observed"] += 1
        if data.get("older"):       # the old observations answered at the top of the file (the sweep, and a step with no row left to carry them), the ledger recording each at once
            gids_ = {p["ledger"][4] for p in plan if p.get("ledger") and p["ledger"][4]} or set(L["scope"] or ())
            node_problems += bv.answer_old(conn, cfg, s, L["cid"], gids_, {o["vl_id"] for o in L["d"]["occurrences"]}, data["older"], sd["key"], run_id)
        if data.get("delete_unmarked"):     # the review of the unmarked observations of one subgroup, after the rows have answered theirs (#2538)
            gid_ = subgroup_id(L, data.get("subgroup")) if sd.get("sweep_unmarked") else None
            if gid_ is None:
                node_problems.append("delete_unmarked is part of a file of a step with sweep_unmarked (2.1) pulled for one subgroup (-Subgroup): the file names no subgroup of such a step")
            else:
                node_problems += bv.sweep(cfg, conn, data["delete_unmarked"], unmarked_of(conn, cfg, s, L, gid_), run_id)
                res["deleted_unmarked"] = len(data["delete_unmarked"])
        if node_problems:
            raise LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(node_problems))
        conn.execute("RELEASE layer_record" if keep else "ROLLBACK TO layer_record")
        if not keep:
            conn.execute("RELEASE layer_record")
    except Exception:
        conn.execute("ROLLBACK TO layer_record")
        conn.execute("RELEASE layer_record")
        raise
    return res


# ══ check: validate every answered row against the tables ══════════════════════════════════════
def check(conn, cfg, run_id: str, name: str, dry: bool = False, subgroup: str | None = None) -> dict:
    """Re-derive what each answered row demands and validate it. Sets `validated` (the check alone sets it). Returns the findings by step."""
    s = settings(cfg)
    roles = set(orec.node_roles(cfg))
    L1 = load(conn, cfg, name, pairs=False, subgroup=subgroup)
    gsel = subgroup_id(L1, subgroup)       # with -Subgroup only that subgroup's rows are re-derived and validated; nothing of the others is read
    L2 = None
    rep = {"collection": L1["name"], "grouping": grouping_gate(conn, cfg, L1), "steps": {}}
    rep["lexical"] = lexical_status(conn, cfg, L1)   # stage 1 is read from its own step below, after the checks have set `validated`
    for sd in s["steps"]:
        step = sd["key"]
        if needs_pairs(sd) and L2 is None:
            L2 = load(conn, cfg, name, pairs=True, subgroup=subgroup)
        L = L2 if needs_pairs(sd) else L1
        rows = [r for r in _rows(conn, L["cid"], step) if r[6] != "retired" and (gsel is None or r[4] == gsel)]
        problems, ok_, open_ = [], 0, 0
        for r in rows:
            lid, _, _, item, gid, subject, state, oid, reason, val = r
            label = (f"{item} / {L['groups'].get(gid, {}).get('name', f'group {gid}')}" if gid else f"{item}") + (f" / {subject}" if subject else "")
            if item == bv.OLD_ITEM and state == "open" and str(subject).isdigit() and not dry:
                gone_ = conn.execute("SELECT deleted FROM ib_observation WHERE id=?", (int(subject),)).fetchone()
                if (gone_ is not None and gone_[0]) or (bv.settled(conn, cfg, [int(subject)]) and int(subject) not in bv.carried_later(conn, [int(subject)], step)):
                    conn.execute(f"UPDATE collection_layer_item SET state='observed', answered_at={NOW}, reason='settled: the observation is dealt with on the record (its answer is in the change log)', updated_at={NOW}, run_id=? WHERE id=?", (run_id, lid))
                    state, reason = "observed", "settled: the observation is dealt with on the record (its answer is in the change log)"
            if state == "open":
                open_ += 1
                continue
            if item == bv.OLD_ITEM:      # an old observation's row: its fate is on the record
                fail = bv.old_fate_ok(conn, int(subject), reason, cfg) if str(subject).isdigit() else "its subject is not an observation"
                if fail:
                    problems.append(f"{label}: {fail}")
                else:
                    ok_ += 1
                if not dry:
                    conn.execute(f"UPDATE collection_layer_item SET checked_at={NOW}, validated=?, updated_at={NOW}, run_id=? WHERE id=?", (0 if fail else 1, run_id, lid))
                continue
            if item in ("sweep", "evidence-validation"):      # the gates at the end of 2.1 (B4, B5): judged from the tables by readcommands (#2538)
                from . import readcommands as rcm
                fail = (rcm.sweep_ok(conn, cfg, s, L, L["cid"], gid) if item == "sweep" else rcm.evidence_ok(conn, cfg, L, L["cid"], gid)) if state == "observed" else "answered as none"
                if fail:
                    problems.append(f"{label}: {fail}")
                else:
                    ok_ += 1
                if not dry:
                    conn.execute(f"UPDATE collection_layer_item SET checked_at={NOW}, validated=?, updated_at={NOW}, run_id=? WHERE id=?", (0 if fail else 1, run_id, lid))
                continue
            idef = s["items"][item]
            fail = None
            if gid and gid not in L["groups"]:      # a row of a group the regrouping retired: reopening the step retires it; until then it is named, not crashed on (found when thought was regrouped, 2026-11-25)
                problems.append(f"{label}: its group is retired or missing (the grouping changed; open the step again for the subgroups)")
                if not dry:
                    conn.execute(f"UPDATE collection_layer_item SET checked_at={NOW}, validated=0, updated_at={NOW}, run_id=? WHERE id=?", (run_id, lid))
                continue
            if sd["layer"] == 3:     # stage 4: re-derived and validated by layerinner.check_row (#2528)
                from . import layerinner
                fail = layerinner.check_row(conn, cfg, s, L, sd, r)
                if not fail and state != "none":
                    fail = bv.row_problems(conn, cfg, s, L["cid"], _row_obs(conn, lid, oid), sd["layer"], sd["key"])
                if fail:
                    problems.append(f"{label}: {fail}")
                else:
                    ok_ += 1
                if not dry:
                    conn.execute(f"UPDATE collection_layer_item SET checked_at={NOW}, validated=?, updated_at={NOW}, run_id=? WHERE id=?", (0 if fail else 1, run_id, lid))
                    if not fail and sd["key"] == "3.1" and gid:
                        release_dataset(conn, L["cid"], gid)      # the end of the subgroup's loop: the dataset is released
                continue
            if idef.get("multi") and state == "observed" and not (reason or "").startswith("adopted"):
                obs_ = [r_[0] for r_ in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};"))]
                exp = expected_nodes(L, item, gid, subject)
                want = {x["vl_id"] for x, _ in exp}
                if not obs_:
                    fail = "its observations are missing or withdrawn"
                else:
                    have, bad_kind, bad_node, fail_tr, traced_all = set(), 0, 0, None, set()
                    for oid_ in obs_:
                        o_ = conn.execute("SELECT stage, tag FROM ib_observation WHERE id=?", (oid_,)).fetchone()
                        if o_[0] != s["stages"][str(sd["layer"])] or o_[1] not in idef.get("kinds", [idef["kind"]]):
                            bad_kind += 1
                        nl = conn.execute("SELECT verse_lexical_id, role, collection_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL", (oid_,)).fetchall()
                        if not nl:
                            bad_node += 1
                        have |= {x_[0] for x_ in nl}
                        bad_node += sum(1 for x_ in nl if x_[1] not in roles or x_[2] is None)
                        if idef.get("traces_to") and not fail_tr:
                            own_vl = {o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid}
                            need = trace_targets(conn, oid_, [x_[0] for x_ in nl if x_[0] in own_vl], idef["traces_to"], L["cid"])
                            got_ = {r_[0] for r_ in conn.execute("SELECT traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NOT NULL", (oid_,))}
                            if set(need) - got_:
                                fail_tr = f"observation {oid_} is not traced to {sorted(set(need) - got_)[:4]}, which hold(s) its occurrences"
                            traced_all |= got_
                    if bad_kind:
                        fail = f"{bad_kind} observations have a stage or kind the item does not take"
                    elif want - have or have - want:
                        fail = f"its senses do not cover the occurrences: {len(want - have)} in no sense, {len(have - want)} not demanded"
                    elif bad_node:
                        fail = "an observation has no node, or a node has no valid role or no collection"
                    elif fail_tr:
                        fail = fail_tr
                    elif idef.get("carries_all_of"):       # a sense step: every observation of the earlier step in the subgroup is carried by a sense
                        rule_ = idef["carries_all_of"]
                        vls_ = [o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid]
                        mine_ = set(trace_targets(conn, 0, vls_, [rule_], L["cid"]))
                        if mine_ - traced_all:
                            fail = f"{len(mine_ - traced_all)} observation(s) of the earlier step are carried by no sense (for example {sorted(mine_ - traced_all)[:4]})"
                if not fail:
                    fail = bv.row_problems(conn, cfg, s, L["cid"], obs_, sd["layer"], sd["key"])
                if fail:
                    problems.append(f"{label}: {fail}")
                else:
                    ok_ += 1
                if not dry:
                    conn.execute(f"UPDATE collection_layer_item SET checked_at={NOW}, validated=?, updated_at={NOW}, run_id=? WHERE id=?", (0 if fail else 1, run_id, lid))
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
            if not fail and state != "none" and not (reason or "").startswith("adopted"):
                fail = bv.row_problems(conn, cfg, s, L["cid"], _row_obs(conn, lid, oid), sd["layer"], sd["key"])
            if fail:
                problems.append(f"{label}: {fail}")
            else:
                ok_ += 1
            if not dry:
                conn.execute(f"UPDATE collection_layer_item SET checked_at={NOW}, validated=?, updated_at={NOW}, run_id=? WHERE id=?", (0 if fail else 1, run_id, lid))
        diff = []
        if rows and (sd["layer"] == 0 or not rep["grouping"]):
            have_k = {(r[3], r[4], r[5]) for r in rows}
            diff = [f"missing: {w['item']} / {L['groups'][w['subgroup_id']]['name'] if w['subgroup_id'] else ''} {w['subject']}".strip() for w in derive(conn, cfg, L, step)
                    if (w["item"], w["subgroup_id"], w["subject"]) not in have_k and (gsel is None or w["subgroup_id"] == gsel)]      # with -Subgroup only the subgroup's own rows are demanded (found by the audit of 2026-11-25)
        if sd.get("closing_gate") and rows and not problems and not open_ and not diff:
            from . import layerinner
            problems += ["partner collection " + x for x in bv.partner_gaps(conn, layerinner.match_partners(r[5] for r in rows), declared=s.get("partner_complete") or [])]
        if sd.get("closing_gate") and rows and not problems and not open_ and not diff:
            problems += ["the evidence validation of the collection does not pass: " + x for x in bv.closing_gate(conn, cfg, L["cid"], "evidence")]      # the inner-being validation completes AFTER 3.3 (researcher 2026-11-24)
        rep["steps"][step] = {"rows": len(rows), "validated": ok_, "open": open_, "failed": problems, "not_in_ledger": diff,
                              "closed": bool(rows) and not problems and not open_ and not diff}
    rep["lexical"] = lexical_status(conn, cfg, L1)
    return rep


# ══ the group on the node ══════════════════════════════════════════════════════════════════════
def node_groups(conn, run_id: str, dry: bool = False) -> dict:
    """Set ib_node.subgroup_id of every live node from the index (collectionindex.refresh_nodes)."""
    return ci.refresh_nodes(conn, run_id, dry=dry)
