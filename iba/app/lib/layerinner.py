"""layerinner.py -- stage 4 of the study, the inner-being analysis, as steps 3.1 to 3.3 of the layered reading (escalation #2528, redesigned 2026-11-21 on the researcher's answer to Q7 of #2526;
design outputs/escalation/2528-stage-4-design-v2-20261121.md; the Programme book, Programme flow, stage 4).

The input of stage 4 is the subgroups of a collection and the stage 3 observations on them. The behaviours are DISCOVERED from analysing those observations, with only occasional reading back
into the base data. Stage 4 articulates and sets the observations for the elements of behaviour (the building blocks); it formulates no claim (that is stage 5, which receives the observations and
not the subgroups). It runs on the ledger `collection_layer_item`, the gates, the working files and the check of lib/layerreading.py, which hands a step of layer 3 to this module (derive, pull,
record, check_row). The content (steps, items, the observation items each uses, thresholds) is cfg_setting layer.reading; the rules of a finding are those of lib/observationrecord.py and of
cfg_setting reading.observation_items, reading.observation_rules and reading.node_roles. Nothing is held in code.

  3.1 subgroup-analysis      one row for each subgroup with stage 3 observations: the elements its observations show, each finding resting on named observations (a traced node on each); every
                             stage 3 observation of the subgroup is taken up by a finding or declared not used, with its reason
  3.2 collection-gathering   one row for the collection: the behaviours discovered (each a flag finding of type discovery that gathers element observations by traced nodes), and the findings that
                             relate elements across subgroups; every 3.1 observation is gathered into a behaviour or declared not gathered, with its reason
  3.3 interworking           one row for each UNIQUE MATCH across all the observations whose nodes reference more than one collection (researcher 2026-11-25; no minimum, no cap, no judgement of
                             significance): one new observation per match, tracing every observation the match comes from, with the occurrences of both sides in the shared verses as nodes;
                             the basis for a deeper analysis of what the pairing means. It depends on 3.2 and the pairings recording the collection on the nodes of both sides

An occurrence node of a finding lies within the occurrences of the observations the finding rests on, unless the finding records a read-back (the verse and why): reading back into the base data
is an act on the record (3.1 and 3.2). A filled file is checked whole and written in one savepoint; the written rows are then checked by check_row, the same function LayerCheck uses, and the
whole file is rolled back if any row fails it.
"""
from __future__ import annotations

import collections
import json
import pathlib

from . import buildvalidate as bv
from . import layerreading as lr
from . import observationrecord as orec
from . import verseevidence as ve

WHO = lr.WHO
STATE = "row_state:"   # the prefix of the ledger reason of an observed row: JSON {"not_used": {id: reason}, "not_gathered": {id: reason}, "read_back": {finding key: [{verse, why}]}}; the check re-reads it
SUBGROUP, COLLECTION, CROSS = "subgroup-analysis", "collection-gathering", "interworking"


# ══ what a row demands ═════════════════════════════════════════════════════════════════════════
def _roles(cfg) -> set:
    """The roles an occurrence of a stage 4 node may take: reading.node_roles without the lexical group (the stages 1 to 3 role)."""
    g = orec.node_role_groups(cfg)
    return set(g.get("relevant", [])) | set(g.get("bears_on", [])) | set(g.get("recognised", []))


def _on(conn, vls, nature: str) -> set:
    """The live observations of the given nature with a live word node on one of the occurrences (idx_ib_node_verse_lexical_id, in chunks). The input of stage 4 is chosen by the MARKER, never by the
    stage (researcher 2026-11-24: "extract the evidence observations"; 2026-11-22: the marker follows content, not stage; RS-04)."""
    out = set()
    for part in lr._chunks(sorted(set(int(v) for v in vls))):
        out |= {r[0] for r in conn.execute("SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND n.traced_observation_id IS NULL AND o.nature=? "
                                           "AND n.verse_lexical_id IN (SELECT value FROM json_each(?))", (nature, json.dumps(part)))}
    return out


def _written_under(conn, ledger_ids) -> set:
    """The live observations written under the given ledger rows: a range of the stable key ('layer:<id>:' up to 'layer:<id>;') for each row, by idx_ib_observation_stable_key.
    A join on `stable_key LIKE 'layer:' || c.id || ':%'` scans ib_observation and was refused by the scan guard (#2538, ReadBehaviours on thought, 2026-11-26)."""
    out = set()
    for lid in sorted(set(ledger_ids)):
        out |= {r[0] for r in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};"))}
    return out


def _of_steps(conn, cid: int, steps) -> set:
    """The live observations written under the ledger rows of the given steps of a collection (the stable key of the row)."""
    return _written_under(conn, [r[0] for r in conn.execute("SELECT id FROM collection_layer_item WHERE deleted=0 AND collection_id=? AND step IN (SELECT value FROM json_each(?))",
                                                            (cid, json.dumps(list(steps))))])


def _inner_of_collection(conn, cid: int, own_steps) -> set:
    """Every live inner_being observation with a live node of the collection, by marker (the 3.1 findings and the older ones kept as inner being), without what the given steps of the collection wrote."""
    ids = {r[0] for r in conn.execute("SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature='inner_being' AND n.collection_id=?", (cid,))}
    return ids - _of_steps(conn, cid, own_steps)


MATCH = "match:"


def match_subject(sa, ta, coll, sb, tb) -> str:
    """The subject of a 3.3 row: this collection's word, the partner collection and its word (surface|strong each)."""
    return f"{MATCH}{sa or ''}|{ta or ''}~{coll}:{sb or ''}|{tb or ''}"


def parse_match(subject):
    """(this surface, this strong, partner collection, partner surface, partner strong) of a 3.3 subject, or None."""
    if not (subject or "").startswith(MATCH):
        return None
    a, _, b = subject[len(MATCH):].partition("~")
    coll, _, w = b.partition(":")
    sa, _, ta = a.rpartition("|")
    sb, _, tb = w.rpartition("|")
    return sa, ta, coll, sb, tb


def match_partners(subjects) -> set:
    """The partner collection names of the match subjects."""
    return {m[2] for m in (parse_match(s_) for s_ in subjects) if m}


def _cross_observations(conn, cid: int) -> dict:
    """{(observation id, verse reference): [(collection id, surface, strong, vl id)]} for every live observation's live word nodes in a verse where the observation has a node of the collection AND a node of
    another collection (the nodes carry the collection: researcher 2026-11-25), except what a 3.3 row wrote (3.3 reads the others). A match is a pairing in a verse. Searched by idx_ib_node_collection."""
    wrote = _written_under(conn, [r[0] for r in conn.execute("SELECT id FROM collection_layer_item WHERE step='3.3'")])
    by = collections.defaultdict(list)
    for oid, ref, col, sf, st, vl in conn.execute("SELECT n.observation_id, n.verse_reference, n.collection_id, n.surface, n.strong, n.verse_lexical_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
                                                  "WHERE n.deleted=0 AND o.deleted=0 AND n.traced_observation_id IS NULL AND n.verse_lexical_id IS NOT NULL AND n.collection_id IS NOT NULL "
                                                  "AND n.observation_id IN (SELECT observation_id FROM ib_node WHERE collection_id=? AND deleted=0)", (cid,)):
        if oid not in wrote:
            by[(oid, ref)].append((col, sf, st, vl))
    return {k: w for k, w in by.items() if len({x[0] for x in w}) > 1 and any(x[0] == cid for x in w)}


_MATCH_CACHE: dict = {}


def matches(conn, L) -> dict:
    key = (id(conn), L["cid"], conn.total_changes)
    if key not in _MATCH_CACHE:
        _MATCH_CACHE.clear()
        _MATCH_CACHE[key] = _matches(conn, L)
    return _MATCH_CACHE[key]


def _matches(conn, L) -> dict:
    """{subject: {"sources": {observation ids}, "occurrences": {vl ids of both sides}, "partner": name}}: one entry for each unique match, a distinct pairing of a word (surface, Strong's code) of this
    collection with a word of another collection that the nodes of one or more observations place together (researcher 2026-11-25: one new observation for each unique match across all observations)."""
    cid = L["cid"]
    names = {v: k for k, v in L["col_ids"].items()}
    out: dict = {}
    for (oid, _ref), w in _cross_observations(conn, cid).items():
        others = {}
        for col, sf, st, vl in w:
            if col != cid:
                others.setdefault((col, sf, st), set()).add(vl)
        for (sa, ta) in {(x[1], x[2]) for x in w if x[0] == cid}:
            mine_vl = {x[3] for x in w if x[0] == cid and (x[1], x[2]) == (sa, ta)}
            for (col, sb, tb), vls in others.items():
                key = match_subject((sa or '').lower(), ta, names.get(col, str(col)), (sb or '').lower(), tb)
                m = out.setdefault(key, {"sources": set(), "occurrences": set(), "partner": names.get(col, str(col)), "partner_id": col})
                m["sources"].add(oid)
                m["occurrences"] |= vls | mine_vl
    return out


def cross_gaps(conn, L) -> list[str]:
    """What stops 3.3 reading the pairings: an observation of this collection's pairing (2.1) or collection-gathering (3.2) rows whose word nodes do not carry the collection (3.3 can then not extract
    the match), and a partner word of the typed pairings whose node on such an observation names no collection or the wrong one. Refused before 3.3 opens (researcher 2026-11-25)."""
    cid = L["cid"]
    gaps = []
    ids = sorted(_written_under(conn, [r[0] for r in conn.execute("SELECT id FROM collection_layer_item WHERE deleted=0 AND collection_id=? AND (item='pairing' OR step='3.2')", (cid,))]))
    for part in lr._chunks(ids):
        for oid, n_ in conn.execute("SELECT observation_id, count(*) FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IS NOT NULL AND collection_id IS NULL "
                                    "AND observation_id IN (SELECT value FROM json_each(?)) GROUP BY observation_id", (json.dumps(part),)):
            gaps.append(f"observation {oid}: {n_} word node(s) carry no collection, so a match cannot be read from them")
    pairs = (L.get("pairs") or {}).get("pairs") or []
    partner_of = {}
    for p in pairs:
        if p["other"]["type"] == "word of another collection":
            partner_of.setdefault(p["other"]["vl_id"], set()).update(L["col_ids"].get(c) for c in p["other"].get("collections") or [])
    if partner_of and ids:
        for part in lr._chunks(partner_of):
            for oid, vl, col in conn.execute("SELECT observation_id, verse_lexical_id, collection_id FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IN (SELECT value FROM json_each(?)) "
                                             "AND observation_id IN (SELECT value FROM json_each(?))", (json.dumps(part), json.dumps(ids))):
                if col not in partner_of[vl]:
                    gaps.append(f"observation {oid}: the node on partner occurrence {vl} names collection {col}, not the partner's {sorted(x for x in partner_of[vl] if x)}")
    return gaps[:50]


def match_occurrences(conn, ids) -> list[dict]:
    """The occurrences of a match as the rows of the collection load hold them (vl_id, osis, verse_id, reference, surface, strong)."""
    out = []
    for part in lr._chunks(ids):
        for r in conn.execute("SELECT vl.id, v.osisId, vl.verse_id, v.reference, vl.surface, vl.strong FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.id IN (SELECT value FROM json_each(?)) ORDER BY vl.id", (json.dumps(part),)):
            out.append({"vl_id": r[0], "osis": r[1], "verse_id": r[2], "reference": r[3], "surface": r[4], "strong": r[5], "group": None})
    return out


def derive(conn, cfg, L, step: str) -> list[dict]:
    s = lr.settings(cfg)
    items = lr.step_def(s, step)["items"]
    out = []
    occ = [o for o in L["d"]["occurrences"] if o["group"]]
    if SUBGROUP in items:
        out += [{"item": SUBGROUP, "subgroup_id": g, "subject": ""} for g in sorted({o["group"] for o in occ}) if _on(conn, [o["vl_id"] for o in occ if o["group"] == g], "evidence")]
    if COLLECTION in items and occ:
        out += [{"item": COLLECTION, "subgroup_id": 0, "subject": ""}]
    if CROSS in items:
        out += [{"item": CROSS, "subgroup_id": 0, "subject": subj} for subj in sorted(matches(conn, L))]      # one row for each unique match: no minimum, no cap (researcher 2026-11-25)
    return out


def demanded(L, item: str, gid: int, subject: str, conn=None) -> list[dict]:
    """The occurrences (verse_lexical rows as the collection load holds them) a row's nodes may name: the subgroup's words, all the collection's grouped words, or the shared verses with a partner."""
    if item == SUBGROUP:
        return [o for o in L["d"]["occurrences"] if o["group"] == gid]
    if item == COLLECTION:
        return [o for o in L["d"]["occurrences"] if o["group"]]
    m = matches(conn, L).get(subject) if conn is not None else None      # the occurrences of both sides of the match
    return match_occurrences(conn, sorted(m["occurrences"])) if m else []


def _allowed(dem: list[dict]) -> set:
    return {int(o["vl_id"]) for o in dem}


def _sources(conn, s, L, sd, gid: int, subject: str = "") -> tuple[set, set]:
    """(the observations a finding of the row may rest on, those the row must take up), all chosen by the MARKER (researcher 2026-11-24):
    3.1 rests on the EVIDENCE observations of the subgroup (every stage, the senses first) and takes up those at the top of the chain: the sense, pairing and older evidence observations; a word observation a sense
    already carries (a traced node) is rested on through the sense and is not demanded again;
    3.2 rests on, and takes up, the 3.1 findings of the current subgroups (researcher 2026-11-26, #2538; until then it took every inner-being observation of the collection);
    3.3 rests on, and takes up, every observation its match comes from (any nature: those whose nodes reference this collection and the partner's)."""
    if sd["key"] == "3.1":
        vls = [o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid]
        ev = _on(conn, vls, "evidence")
        carried = set()
        if ev:
            carried = {r[0] for r in conn.execute("SELECT DISTINCT n.traced_observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.stage=? "
                                                  "AND n.traced_observation_id IN (SELECT value FROM json_each(?))", (s["stages"]["1"], json.dumps(sorted(ev))))}
            carried = {c for c in carried if conn.execute("SELECT stage FROM ib_observation WHERE id=?", (c,)).fetchone()[0] == s["stages"]["0"]}
        return ev, ev - carried
    if sd["key"] == "3.2":      # the 3.1 findings of the current subgroups (researcher 2026-11-26, #2538: the approach of the draft, spec v5 C2 and IB-04; not every inner-being observation)
        found = _written_under(conn, [r[0] for r in conn.execute("SELECT c.id FROM collection_layer_item c JOIN collection_subgroup s ON s.id=c.subgroup_id WHERE c.collection_id=? "
                                                                  "AND c.step='3.1' AND c.deleted=0 AND c.state!='retired' AND s.deleted=0", (L["cid"],))])
        return found, found
    m = matches(conn, L).get(subject)      # 3.3: the observations the match comes from, every one traced by the observation of the match
    src = set(m["sources"]) if m else set()
    return src, src


def _covered(conn, ids) -> set:
    """The occurrences carried as live nodes by the given observations."""
    out = set()
    for part in lr._chunks(sorted(ids)):
        out |= {r[0] for r in conn.execute("SELECT DISTINCT verse_lexical_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL AND observation_id IN (SELECT value FROM json_each(?))", (json.dumps(part),))}
    return out


def _cover_map(conn, ids) -> dict:
    """{observation: the occurrences it carries as live nodes}, by chunk (RW-14)."""
    out: dict = {}
    for part in lr._chunks(sorted(set(ids))):
        for o, v in conn.execute("SELECT observation_id, verse_lexical_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL "
                                 "AND observation_id IN (SELECT value FROM json_each(?))", (json.dumps(part),)):
            out.setdefault(o, set()).add(v)
    return out


def _qualifier_partners(conn, cid: int, gid) -> set:
    """#2637 G3 (researcher, #2637 v7): the occurrences on the live nodes of the subgroup's 2.1 qualifier observations -- the partner words that
    qualify it. A 3.1 qualification finding may hold them, where the reading judges the qualifier bears on the working (IB-02)."""
    if not gid:
        return set()
    lids = [r[0] for r in conn.execute("SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='2.1' AND item='qualifier' AND deleted=0", (cid, gid))]
    return _covered(conn, _written_under(conn, lids)) if lids else set()


def _expand_nodes(conn, f, sources: set, allowed: set):
    """#2637 X2, the judgement-only form: a finding may name `rests_on` (the observations it rests on) and `role` (the role of the words those
    observations cover, with `roles` {occurrence: role, or "" to leave one out} for the exceptions) in place of writing its nodes. The recorder
    writes a traced node on each observation named and an occurrence node on each occurrence they cover that the row may name. Nodes written by
    hand are kept as they are and win over the expansion."""
    if not isinstance(f, dict) or not f.get("rests_on"):
        return f
    rests = [int(x) for x in f["rests_on"] if str(x).strip().isdigit()]
    nodes = [n for n in (f.get("nodes") or [])]
    have_t = {n.get("traced") for n in nodes if isinstance(n, dict)}
    have_o = {n.get("occurrence") for n in nodes if isinstance(n, dict)}
    nodes += [{"traced": t} for t in rests if t not in have_t]
    role, roles = f.get("role"), {int(k): v for k, v in (f.get("roles") or {}).items() if str(k).strip().isdigit()}
    if role or roles:
        for o in sorted(_covered(conn, [t for t in rests if t in sources]) & allowed):
            r = roles.get(o, role)
            if r and o not in have_o:
                nodes.append({"occurrence": o, "role": r})
    return {**{k: v for k, v in f.items() if k not in ("rests_on", "role", "roles")}, "nodes": nodes}


def _texts(conn, dem: list[dict]) -> dict:
    """{osis: verse text} of the verses of the demanded occurrences (a partner word from the typed pairings carries no text of its own)."""
    out = {}
    for part in lr._chunks(sorted({o["verse_id"] for o in dem})):
        out.update({r[0]: r[1] for r in conn.execute("SELECT osisId, text FROM verse WHERE id IN (SELECT value FROM json_each(?))", (json.dumps(part),))})
    return out


def _in(ids) -> str:
    return json.dumps(sorted(int(i) for i in ids))


def _obs_line(conn, oid: int) -> dict:
    o = conn.execute("SELECT id, stage, tag, obs_text, basis, parts FROM ib_observation WHERE id=?", (oid,)).fetchone()
    refs = [r[0] for r in conn.execute("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_reference IS NOT NULL LIMIT 12", (oid,))]
    return {"observation": o[0], "stage": o[1], "kind": o[2], "item": (json.loads(o[5]) if o[5] else {}).get("item"), "text": (o[3] or "")[:400], "basis": o[4], "verses": refs}


# ══ pull ═══════════════════════════════════════════════════════════════════════════════════════
def pull(conn, cfg, L, step: str, rows: list, out_dir: pathlib.Path):
    s = lr.settings(cfg)
    sd = lr.step_def(s, step)
    cap = s.get("pull_max_rows", 5)
    spec = orec.items_setting(cfg)
    by_item = {i["key"]: i for i in spec["items"]}
    inter = cfg.setting("layer.interventions") or []
    prompts = cfg.setting("reading.observe_prompts") or {}
    nuances = cfg.setting("reading.nuance_pointers") or []
    out = []
    for r in rows[:cap]:
        lid, _, _, item, gid, subject, state, oid, reason, val = r
        idef = s["items"][item]
        dem = demanded(L, item, gid, subject, conn)
        sources, required = _sources(conn, s, L, sd, gid, subject)
        uses = [{"item": k, "name": by_item[k]["name"], "kinds": by_item[k]["kinds"], "bases": by_item[k]["bases"], "shared": by_item[k]["shared"],
                 "nuances": [x for x in nuances if x.get("item") == k]} for k in idef["uses"] if k in by_item]
        row = {"ledger_id": lid, "step": step, "item": item, "group": L["groups"][gid]["name"] if gid else None, "subject": subject, "asks": idef["asks"], "uses": uses,
               "node_roles": orec.node_role_groups(cfg), "interventions": inter, "prompts_by_kind": {k: v for k, v in prompts.items() if v},
               "to_take_up": [_obs_line(conn, i) for i in sorted(required)], "may_rest_on_besides": [_obs_line(conn, i) for i in sorted(sources - required)]}
        if step == "3.1":
            verses = _texts(conn, dem)
            row["definition_of_the_subgroup"] = L["groups"][gid].get("note")
            row["occurrences_total"] = len(dem)
            row["verses_of_the_subgroup"] = verses      # ALL the verses of the subgroup with their text (researcher 2026-11-24)
            strongs = sorted({o["strong"] for o in dem if o["strong"]})
            row["meaning_by_code"] = ve.meaning(cfg, conn, {c: ("NT" if c.startswith("G") else "OT") for c in strongs})
            earlier = collections.OrderedDict()
            for part in lr._chunks(sorted(_allowed(dem))):
                for r2 in conn.execute("SELECT o.id, o.stage, o.tag, o.obs_text, o.nature FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 AND o.stage NOT IN "
                                       "(SELECT value FROM json_each(?)) AND o.nature='inner_being' AND n.verse_lexical_id IN (SELECT value FROM json_each(?)) ORDER BY o.id", (json.dumps(sorted(set(s["stages"].values()))), json.dumps(part))):
                    earlier.setdefault(r2[0], {"observation": r2[0], "stage": r2[1], "kind": r2[2], "nature": r2[4], "text": (r2[3] or ""), "action": None})
            row["older_inner_being_observations"] = list(earlier.values())      # every one, whole: each is answered (accepted, restated, consumed, merged, deleted or deferred) with a trace to evidence (IB-07)
        if step == "3.3":
            row["shared_verses"] = _texts(conn, dem)
        occ = [{"occurrence": o["vl_id"], "reference": o["reference"], "surface": o["surface"], "strong": o["strong"]} for o in dem]
        row["occurrences"] = occ
        fill = {"disposition": "observed | none" if idef["none_allowed"] else "observed",
                "findings": [{"key": "f1", "kind": "", "text": "", "basis": "stated | read", "parts": {"item": "", "grounds": ""},
                              "nodes": [{"occurrence": "<occurrence id>", "role": "<a role of reading.node_roles>"}, {"traced": "<id of an observation this finding rests on>"}],
                              "read_back": [{"verse": "<osis id, only where an occurrence is outside the traced observations>", "why": ""}]}],
                "existing": [], "reason": ""}
        if step == "3.1":
            fill["not_used"] = {"<stage 3 observation id>": "why no element rests on it"}
        if step == "3.2":
            fill["not_gathered"] = {"<3.1 observation id>": "why it belongs to no behaviour"}
        row["fill"] = fill
        out.append(row)
    # the rules of reading and of writing a finding (RG, RW, RS, RO11) are held on the step collection.layer_record (moved there from the retired reading steps, #2528; IB-03); they go once with the file
    rules = [{"rule": r_[0], "text": r_[1]} for r_ in conn.execute(
        "SELECT rule_key, rule_text FROM cfg_method_rule WHERE active=1 AND step='collection.layer_record' AND (rule_key LIKE 'RG-%' OR rule_key LIKE 'RW-%' OR rule_key LIKE 'RS-%' OR rule_key LIKE 'RO11 %' OR rule_key LIKE 'IB-%') ORDER BY ordinal, id")]
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"layer-{L['name']}-{step}-{lr._now()[:10].replace('-', '')}.json"
    path.write_text(json.dumps({"collection": L["name"], "step": step, "pulled": lr._now(), "reading_rules": rules, "rows": out}, ensure_ascii=False, indent=1), encoding="utf-8")
    return path, len(out)


# ══ record ═════════════════════════════════════════════════════════════════════════════════════
def _norm_nodes(conn, finding: dict, allowed: set, where: str, errors: list) -> dict:
    """The finding as observationrecord.check takes it: each node's strong from its occurrence, the occurrence an integer inside the row's reach."""
    f = dict(finding)
    nodes = []
    for j, n in enumerate(finding.get("nodes") or []):
        if not isinstance(n, dict):
            errors.append(f"{where} nodes[{j}]: a node is an object")
            continue
        n = dict(n)
        if n.get("traced") is not None and n.get("occurrence") is None:
            try:
                n["traced"] = int(n["traced"])
            except (TypeError, ValueError):
                errors.append(f"{where} nodes[{j}]: `traced` is the id of an observation")
                continue
            nodes.append(n)
            continue
        try:
            occ = int(n.get("occurrence"))
        except (TypeError, ValueError):
            errors.append(f"{where} nodes[{j}]: a node names the occurrence id of the word (`occurrence`) or the observation it rests on (`traced`)")
            continue
        if occ not in allowed:
            errors.append(f"{where} nodes[{j}]: occurrence {occ} is not an occurrence this row may name")
            continue
        n["occurrence"] = occ
        if not n.get("strong"):
            n["strong"] = conn.execute("SELECT strong FROM verse_lexical WHERE id=?", (occ,)).fetchone()[0]
        nodes.append(n)
    f["nodes"] = nodes
    return f


def _read_back_ok(rb, dem: list[dict], where: str, minr: int, errors: list) -> list:
    """The read-back list of a finding: [{verse, why}], the verse one of the verses of the row's occurrences, the reason in words."""
    out = []
    osis = {o["osis"] for o in dem}
    for e in rb or []:
        if not isinstance(e, dict) or e.get("verse") not in osis or len((e.get("why") or "").strip()) < minr:
            errors.append(f"{where}: a read_back entry is {{verse: an osis id of a verse of this row, why: the reason in words ({minr} characters or more)}}")
        else:
            out.append({"verse": e["verse"], "why": e["why"].strip()})
    return out


def record(conn, cfg, run_id: str, data: dict, keep: bool, collect: bool = False) -> dict:
    """Check the filled file whole, write it in one savepoint and check the written rows as LayerCheck does; any problem refuses all (nothing written). keep=False rolls back (the preview)."""
    # collect=True (CheckAnswer, #2637 X3): nothing is kept, and the record does not stop between its stages: the finding rules are checked on every
    # row however its form fared, a row with no problem is written in a savepoint of its own and checked as LayerCheck checks it, and every
    # problem of every stage is listed in one refusal. A row whose findings break a rule is not written: its write would only repeat them.
    if collect:
        keep = False
    s = lr.settings(cfg)
    name, step = data.get("collection"), data.get("step")
    sd = lr.step_def(s, step)
    L = lr.load(conn, cfg, name, pairs=lr.needs_pairs(sd), subgroup=lr.file_scope(conn, name, step, data))
    minr = s["min_reason_chars"]
    loop = orec.loop_setting(cfg)
    ledger = {r[0]: r for r in lr._rows(conn, L["cid"], step)}
    errors, todo = [], []
    for i, row in enumerate(data.get("rows", [])):
        where = f"row {i + 1} (ledger {row.get('ledger_id')})"
        lrow = ledger.get(row.get("ledger_id"))
        if lrow is None:
            errors.append(f"{where}: not a ledger row of {L['name']} step {step}")
            continue
        if not (lrow[6] == "open" or (lrow[6] == "observed" and lrow[9] == 0)):
            errors.append(f"{where}: the row is {lrow[6]}{' and validated' if lrow[9] else ''}; only an open or an unvalidated row is recorded")
            continue
        item, gid, subject = lrow[3], lrow[4], lrow[5]
        idef = s["items"][item]
        fill = row.get("fill") or row
        disp = fill.get("disposition")
        if disp == "none":
            if not idef["none_allowed"]:
                errors.append(f"{where}: {item} cannot be recorded as none; it needs findings")
            elif len((fill.get("reason") or "").strip()) < minr:
                errors.append(f"{where}: none needs its reason, in words ({minr} characters or more)")
            todo.append({"lrow": lrow, "disp": "none", "reason": (fill.get("reason") or "").strip()})
            continue
        if disp != "observed":
            errors.append(f"{where}: disposition must be observed or none")
            continue
        dem = demanded(L, item, gid, subject, conn)
        if not dem:
            errors.append(f"{where}: the data holds no occurrence for this aspect")
            continue
        allowed = _allowed(dem)
        qpart = _qualifier_partners(conn, L["cid"], gid) if step == "3.1" else set()
        sources, required = _sources(conn, s, L, sd, gid, subject)
        findings = fill.get("findings") or []
        if not findings:
            errors.append(f"{where}: the row is answered by findings (fill.findings): at least one, each with its kind, text, basis, parts and nodes")
        osis_of = {int(o["vl_id"]): o["osis"] for o in dem}
        specs, traced_all, read_back, keys = [], set(), {}, set()
        vtexts = set(_texts(conn, dem).values())
        for k, f in enumerate(findings, 1):
            fw = f"{where} finding {k}"
            key = str(f.get("key") or "").strip()
            if not key or key in keys or ":" in key:
                errors.append(f"{fw}: `key` is a short name unique in the row (no colon)")
            keys.add(key)
            alw = allowed | qpart if isinstance(f, dict) and f.get("kind") == "qualification" else allowed      # G3: a qualifier's partner words
            f = _expand_nodes(conn, f, sources, alw)
            f2 = _norm_nodes(conn, f, alw, fw, errors)
            if f2.get("route") in ("", None):    # an empty route is no route (a route is held only on a party or link finding)
                f2.pop("route", None)
            if isinstance(f2.get("parts"), dict) and f2["parts"].get("item") not in idef["uses"]:
                errors.append(f"{fw}: parts.item is one of {idef['uses']}")
            traced = [n["traced"] for n in f2["nodes"] if n.get("traced") is not None]
            if not traced:
                errors.append(f"{fw}: a finding rests on observations: a traced node on each (a stage 3 or stage 1 observation in 3.1, a 3.1 observation in 3.2, a 3.1 or 3.2 observation in 3.3)")
            bad = [t for t in traced if t not in sources]
            if bad:
                errors.append(f"{fw}: observation(s) {bad[:5]} are not observations this row may rest on")
            traced_all |= set(traced)
            rb = _read_back_ok(f.get("read_back"), dem, fw, minr, errors)
            read_back[key] = rb
            if step != "3.3":    # the occurrences of a finding lie in those of the observations it rests on, or its verse is read back (and says why)
                cov = _covered(conn, [t for t in traced if t in sources])
                rbv = {e["verse"] for e in rb}
                out_of = [n["occurrence"] for n in f2["nodes"] if n.get("occurrence") is not None and n["occurrence"] not in cov and osis_of.get(n["occurrence"]) not in rbv]
                if out_of:
                    errors.append(f"{fw}: occurrence(s) {out_of[:5]} are outside the observations the finding rests on; read the verse back and record it in read_back, or drop the node")
            cp = next((c for c in (orec.copies_verse(cfg, [f2.get("text")], t) for t in vtexts) if c), None)
            if cp:
                errors.append(f"{fw}: the text restates the verse ({cp!r}); say what the observations show (B:131, RW-04)")
            specs.append((fw, f2))
        # completeness: nothing the step reads is lost on the way to stage 5
        key_ = "not_used" if step == "3.1" else "not_gathered" if step == "3.2" else None
        decl = fill.get(key_) or {} if key_ else {}
        if key_ and (not isinstance(decl, dict) or any(not str(d).isdigit() for d in decl)):
            errors.append(f"{where}: {key_} is {{observation id: reason}}")
            decl = {}
        declared = {int(d) for d in decl}
        for d, why in decl.items():
            if int(d) not in required or len(str(why).strip()) < minr:
                errors.append(f"{where}: {key_} names an observation this row must take up, with its reason in words ({minr} characters or more): {d}")
        if key_:
            errors += [f"{where}: observation {m} is neither rested on by a finding nor in {key_} with its reason" for m in sorted(required - traced_all - declared)[:20]]
            errors += [f"{where}: observation {m} is both rested on by a finding and in {key_}; keep one" for m in sorted(traced_all & declared)]
        if step == "3.3":
            errors += [f"{where}: observation {m} is part of this match and no finding traces it (every observation the match comes from is traced)" for m in sorted(required - traced_all)[:20]]
        if step == "3.2" and not any(isinstance(f.get("parts"), dict) and f["parts"].get("item") == "flag" and f["parts"].get("flag_type") == "discovery" for _, f in specs):
            errors.append(f"{where}: the collection shows at least one behaviour: a finding of the item flag, flag_type discovery, that gathers its element observations (or record the row as none, with the reason)")
        ex = []
        for e in fill.get("existing") or []:
            a = e.get("action")
            ob = conn.execute("SELECT id, deleted FROM ib_observation WHERE id=?", (e.get("observation"),)).fetchone() if isinstance(e.get("observation"), int) else None
            if a not in loop["existing_actions"] or ob is None or ob[1]:
                errors.append(f"{where}: an `existing` entry names a live observation and an action {loop['existing_actions']}")
            elif a in ("modify", "delete", "merge", "leave") and len((e.get("reason") or "").strip()) < minr:
                errors.append(f"{where}: observation {e['observation']}: a {a} needs its reason ({minr} characters or more)")
            else:
                ex.append(e)
        todo.append({"lrow": lrow, "disp": "observed", "specs": specs, "existing": ex, "where": where, "older": fill.get("older"),
                     "state": {"not_used": {str(k): v for k, v in decl.items()} if step == "3.1" else {}, "not_gathered": {str(k): v for k, v in decl.items()} if step == "3.2" else {},
                               "read_back": {k: v for k, v in read_back.items() if v}}})
    if errors and not collect:
        raise lr.LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
    first_stage = {w for w in (t["where"] for t in todo) if any(e.startswith(w) for e in errors)}
    conn.execute("SAVEPOINT layer_inner")
    res = {"observed": 0, "none": 0, "nodes": 0, "withdrawn": 0}
    try:
        for t in todo:   # an earlier answer of the row is withdrawn first, so that its text is not a duplicate of the new one
            lid = t["lrow"][0]
            for (prev,) in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};")).fetchall():
                for (pn,) in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (prev,)).fetchall():
                    orec.delete_node(conn, pn, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                orec.soft_delete_observation(conn, prev, f"re-recorded under ledger row {lid} ({run_id})", None, run_id, WHO)
                res["withdrawn"] += 1
        for t in todo:
            if t["disp"] != "observed":
                continue
            quotes: list = []
            perr: list = []
            t["plan"] = orec.check(cfg, t["specs"], perr, quotes)
            perr += [f"{t['where']}: {q} is not the ESV's wording (quote check)" if isinstance(q, str) else str(q) for q in quotes]
            errors += perr
            t["bad"] = bool(perr) or t["where"] in first_stage
        if errors and not collect:
            raise lr.LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
        stage = lr.stage_of(s, sd)
        texts = bv.scope_texts(conn, cfg, L["cid"])
        for t in todo:
            if collect and t.get("bad"):
                continue
            if collect:      # a savepoint per row (a `continue` in the body leaves it open inside layer_inner, which a check always rolls back)
                conn.execute("SAVEPOINT inner_row")
            try:
                lid = t["lrow"][0]
                if t["disp"] == "none":
                    conn.execute(f"UPDATE collection_layer_item SET answered_at={lr.NOW}, state='none', observation_id=NULL, reason=?, validated=0, updated_at={lr.NOW}, run_id=? WHERE id=?", (t["reason"], run_id, lid))
                    res["none"] += 1
                    continue
                for e in t["existing"]:
                    a, oid = e["action"], e["observation"]
                    if a == "delete":
                        orec.soft_delete_observation(conn, oid, e["reason"].strip(), None, run_id, WHO)
                    elif a == "merge":
                        orec.merge_observation(conn, oid, e.get("into"), e["reason"].strip(), None, run_id, WHO)
                    elif a == "modify" and e.get("set"):
                        orec.modify_observation(cfg, conn, oid, e["set"], e["reason"].strip(), None, run_id, WHO)
                    for nx in e.get("nodes") or []:
                        if nx.get("action") == "delete":
                            orec.delete_node(conn, nx["node"], (nx.get("reason") or e["reason"]).strip(), None, run_id, WHO)
                        elif nx.get("action") == "modify":
                            orec.modify_node(cfg, conn, nx["node"], nx.get("set") or {}, (nx.get("reason") or e["reason"]).strip(), None, run_id, WHO)
                written = orec.write(conn, t["plan"], None, run_id, stage=stage, stable_key=lambda k, lid=lid: f"layer:{lid}:{run_id}:{k}", nature=s["items"][t["lrow"][3]]["nature"])
                for w in written.values():
                    if w["new"]:
                        errors += lr.settle_nodes(conn, s, w["observation"], run_id, sd["layer"])
                errors += bv.settle_row(conn, cfg, s, L["cid"], [w["observation"] for w in written.values() if w["new"]], t.get("older"), run_id, texts, 99, sd["key"], {int(o["vl_id"]) for o in L["d"]["occurrences"]})
                first = min(w["observation"] for w in written.values())
                res["nodes"] += sum(len(w["nodes"]) for w in written.values())
                res["observed"] += sum(1 for w in written.values() if w["new"])
                conn.execute(f"UPDATE collection_layer_item SET answered_at={lr.NOW}, state='observed', observation_id=?, reason=?, validated=0, updated_at={lr.NOW}, run_id=? WHERE id=?",
                             (first, STATE + json.dumps(t["state"], ensure_ascii=False, sort_keys=True), run_id, lid))
            except Exception as exc:
                if not collect:
                    raise
                conn.execute("ROLLBACK TO inner_row")
                conn.execute("RELEASE inner_row")
                errors.append(f"{t['where']}: the write is refused: {exc}")
                t["bad"] = True
                continue
            if collect:
                conn.execute("RELEASE inner_row")
        L = lr.load(conn, cfg, name, pairs=lr.needs_pairs(sd), subgroup=lr.file_scope(conn, name, step, data))     # the grouping on the nodes is read back, so the check sees what was written
        for t in todo:
            if t["disp"] != "observed" or (collect and t.get("bad")):
                continue
            lrow = next(r for r in lr._rows(conn, L["cid"], step) if r[0] == t["lrow"][0])
            why = check_row(conn, cfg, s, L, sd, lrow)
            if why:
                errors.append(f"{t['where']}: {why}")
        if errors:
            raise lr.LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
        if keep:
            conn.execute("RELEASE layer_inner")
        else:
            conn.execute("ROLLBACK TO layer_inner")
            conn.execute("RELEASE layer_inner")
    except Exception as exc:
        conn.execute("ROLLBACK TO layer_inner")
        conn.execute("RELEASE layer_inner")
        if isinstance(exc, orec.Refused):
            raise lr.LayerError(f"the file is refused, nothing written; problems:\n  {exc}")
        raise
    return res


# ══ check: one row, from the tables alone ═════════════════════════════════════════════════════
def check_row(conn, cfg, s, L, sd, r) -> str | None:
    """None when the answered row agrees with what the tables demand (IB-02 to IB-06), else the first reason it does not. LayerCheck and LayerRecord both call it."""
    lid, _, _, item, gid, subject, state, oid, reason, val = r
    idef = s["items"][item]
    minr = s["min_reason_chars"]
    step = sd["key"]
    if gid and gid not in L["groups"]:
        return "its group is retired or missing"
    if state == "none":
        if not idef["none_allowed"] or len((reason or "").strip()) < minr:
            return "recorded as none without a permitted reason"
        return None
    dem = demanded(L, item, gid, subject, conn)
    if not dem:
        return "the data no longer demands this aspect (LayerOpen retires it)"
    allowed = _allowed(dem)
    qpart = _qualifier_partners(conn, L["cid"], gid) if step == "3.1" else set()
    osis_of = {int(o["vl_id"]): o["osis"] for o in dem}
    stage = lr.stage_of(s, sd)
    inner = _roles(cfg)
    groups = orec.node_role_groups(cfg)
    sources, required = _sources(conn, s, L, sd, gid, subject)
    own = conn.execute("SELECT id, stage, tag, basis, route, parts, obs_text, stable_key FROM ib_observation WHERE deleted=0 AND stable_key >= ? AND stable_key < ?", (f"layer:{lid}:", f"layer:{lid};")).fetchall()
    if not own:
        return "its observations are missing or withdrawn"
    st = {}
    if (reason or "").startswith(STATE):
        try:
            st = json.loads(reason[len(STATE):])
        except ValueError:
            return "its not-used, not-gathered and read-back records are not readable"
    read_back = st.get("read_back") or {}
    verse_texts = set(_texts(conn, dem).values())
    traced_all, discovery = set(), False
    for ob in own:
        pj = json.loads(ob[5]) if ob[5] else None
        perr: list = []
        it = orec.check_item_parts(cfg, pj, ob[2], ob[3], ob[4], "", perr)
        if perr:
            return f"observation {ob[0]}: " + "; ".join(x.lstrip(": ") for x in perr)
        if it not in idef["uses"]:
            return f"observation {ob[0]} is of the item {it!r}, which this row does not use ({idef['uses']})"
        if ob[1] != stage:
            return f"observation {ob[0]} has stage {ob[1]}, not {stage}"
        if it == "flag" and (pj or {}).get("flag_type") == "discovery":
            discovery = True
        nl = conn.execute("SELECT verse_lexical_id, role, collection_id, traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0", (ob[0],)).fetchall()
        real = [n for n in nl if n[0] is not None]
        if not real:
            return f"observation {ob[0]} has no node on an occurrence"
        traced = [n[3] for n in nl if n[3]]
        if not traced:
            return f"observation {ob[0]} rests on no observation (a traced node on each)"
        for tid in traced:
            if tid not in sources:
                return f"observation {ob[0]} rests on observation {tid}, which this row may not rest on"
        traced_all |= set(traced)
        cov = _covered(conn, traced) if step != "3.3" else set()
        rbv = {e.get("verse") for e in read_back.get(str(ob[7]).rsplit(":", 1)[-1]) or []}
        for n in real:
            if n[0] not in allowed and not (ob[2] == "qualification" and n[0] in qpart):
                return f"observation {ob[0]} has a node on occurrence {n[0]}, which this row may not name"
            if n[1] not in inner:
                return f"observation {ob[0]} has a node with no valid stage 4 role ({n[1]!r})"
            if n[2] is None:
                return f"observation {ob[0]} has a node with no collection"
            if step != "3.3" and n[0] not in cov and osis_of.get(n[0]) not in rbv:
                return f"observation {ob[0]} has a node on occurrence {n[0]}, outside the observations it rests on and with no read-back recorded for its verse"
        if orec.rules(cfg)["bears_on_only_refused"] and all(n[1] in groups["bears_on"] for n in real):
            return f"observation {ob[0]}: every node it holds bears on an act; those words are nodes of the observation of the act"
        for t in verse_texts:
            cp = orec.copies_verse(cfg, [ob[6]], t)
            if cp:
                return f"observation {ob[0]} restates the verse ({cp!r})"
    for k, rb in read_back.items():
        for e in rb:
            if len((e.get("why") or "").strip()) < minr:
                return f"a read-back of {e.get('verse')} gives no reason in words"
    if step in ("3.1", "3.2"):
        decl = {int(k) for k in (st.get("not_used") if step == "3.1" else st.get("not_gathered")) or {}}
        for k, why in ((st.get("not_used") if step == "3.1" else st.get("not_gathered")) or {}).items():
            if len(str(why).strip()) < minr:
                return f"observation {k} is declared not {'used' if step == '3.1' else 'gathered'} without a reason in words"
        gone = {r[0] for r in conn.execute("SELECT id FROM ib_observation WHERE deleted=1 AND id IN (SELECT value FROM json_each(?))", (_in(decl),))} if decl else set()
        decl -= gone      # a declared observation removed since by the method (the sweep at the close of 3.1, #2538) no longer needs, or allows, a declaration
        miss = required - traced_all - decl
        if miss:
            return f"{len(miss)} observations are neither rested on by a finding nor declared (first: {sorted(miss)[0]}); nothing the step reads may be left out silently"
        if decl - required:
            return "it declares an observation this row does not take up"
    if step == "3.3" and required - traced_all:
        return f"{len(required - traced_all)} observation(s) of the match are not traced (first: {sorted(required - traced_all)[0]}); every observation the match comes from is traced"
    if step == "3.2" and not discovery:
        return "no behaviour: the collection row needs a flag finding of type discovery (or none, with its reason)"
    return None
