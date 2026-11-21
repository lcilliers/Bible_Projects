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
  3.3 interworking           one row for each subgroup and partner collection that share pair_min_verses verses: how they work together, resting on 3.1 or 3.2 observations

An occurrence node of a finding lies within the occurrences of the observations the finding rests on, unless the finding records a read-back (the verse and why): reading back into the base data
is an act on the record (3.1 and 3.2). A filled file is checked whole and written in one savepoint; the written rows are then checked by check_row, the same function LayerCheck uses, and the
whole file is rolled back if any row fails it.
"""
from __future__ import annotations

import collections
import json
import pathlib

from . import layerreading as lr
from . import observationrecord as orec
from . import verseevidence as ve

WHO = lr.WHO
STATE = "row_state:"   # the prefix of the ledger reason of an observed row: JSON {"not_used": {id: reason}, "not_gathered": {id: reason}, "read_back": {finding key: [{verse, why}]}}; the check re-reads it
SOURCE_STEPS = {"3.2": ("3.1",), "3.3": ("3.1", "3.2")}
SUBGROUP, COLLECTION, CROSS = "subgroup-analysis", "collection-gathering", "interworking"


# ══ what a row demands ═════════════════════════════════════════════════════════════════════════
def _roles(cfg) -> set:
    """The roles an occurrence of a stage 4 node may take: reading.node_roles without the lexical group (the stages 1 to 3 role)."""
    g = orec.node_role_groups(cfg)
    return set(g.get("relevant", [])) | set(g.get("bears_on", [])) | set(g.get("recognised", []))


def _stage3_of_subgroup(conn, s, cid: int, gid: int, with_lexical: bool = False) -> list:
    """The live stage 3 observations (layers 1 and 2; with the stage 1 word senses when with_lexical) that have a live node on the subgroup's words in this collection."""
    st = [s["stages"]["1"], s["stages"]["2"]] + ([s["stages"]["0"]] if with_lexical else [])
    return [r[0] for r in conn.execute(
        "SELECT DISTINCT o.id FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 AND n.collection_id=? AND n.subgroup_id=? "
        "AND o.stage IN (SELECT value FROM json_each(?)) ORDER BY o.id", (cid, gid, json.dumps(st)))]


def _stage4_of(conn, s, cid: int, steps) -> list:
    """The live stage 4 observations written under the ledger rows of the given steps of this collection."""
    return [r[0] for r in conn.execute(
        "SELECT DISTINCT o.id FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE o.deleted=0 AND c.deleted=0 AND c.collection_id=? "
        "AND c.step IN (SELECT value FROM json_each(?)) AND o.stage=? ORDER BY o.id", (cid, json.dumps(list(steps)), s["stages"]["3"]))]


def derive(conn, cfg, L, step: str) -> list[dict]:
    s = lr.settings(cfg)
    items = lr.step_def(s, step)["items"]
    th = s["thresholds"]
    out = []
    occ = [o for o in L["d"]["occurrences"] if o["group"]]
    if SUBGROUP in items:
        out += [{"item": SUBGROUP, "subgroup_id": g, "subject": ""} for g in sorted({o["group"] for o in occ}) if _stage3_of_subgroup(conn, s, L["cid"], g)]
    if COLLECTION in items and occ:
        out += [{"item": COLLECTION, "subgroup_id": 0, "subject": ""}]
    if CROSS in items:
        name2id = {g["name"]: g["id"] for g in L["groups"].values()}
        partner = collections.defaultdict(set)
        for p in L["pairs"]["pairs"]:
            g = name2id.get(p["member"]["subgroup"])
            if g is not None and p["other"]["type"] == "word of another collection":
                for cn in p["other"]["collections"]:
                    partner[(g, cn)].add(p["member"]["verse_id"])
        out += [{"item": CROSS, "subgroup_id": g, "subject": f"collection:{cn}"} for (g, cn), vs in sorted(partner.items()) if len(vs) >= th["pair_min_verses"]]
    return out


def demanded(L, item: str, gid: int, subject: str) -> list[dict]:
    """The occurrences (verse_lexical rows as the collection load holds them) a row's nodes may name: the subgroup's words, all the collection's grouped words, or the shared verses with a partner."""
    if item == SUBGROUP:
        return [o for o in L["d"]["occurrences"] if o["group"] == gid]
    if item == COLLECTION:
        return [o for o in L["d"]["occurrences"] if o["group"]]
    _kind, _, rest = subject.partition(":")
    return [o for o, _r in lr.expected_nodes(L, "pairing", gid, rest)]


def _allowed(dem: list[dict]) -> set:
    return {int(o["vl_id"]) for o in dem}


def _sources(conn, s, L, sd, gid: int) -> tuple[set, set]:
    """(the observations a finding of the row may rest on, those the row must take up): 3.1 rests on the stage 3 observations (and the stage 1 senses) of the subgroup and takes up the stage 3 ones;
    3.2 rests on the 3.1 observations of the collection and takes up all of them; 3.3 rests on 3.1 and 3.2 observations and takes up none."""
    if sd["key"] == "3.1":
        return set(_stage3_of_subgroup(conn, s, L["cid"], gid, with_lexical=True)), set(_stage3_of_subgroup(conn, s, L["cid"], gid))
    below = set(_stage4_of(conn, s, L["cid"], SOURCE_STEPS[sd["key"]]))
    return below, (below if sd["key"] == "3.2" else set())


def _covered(conn, ids) -> set:
    """The occurrences carried as live nodes by the given observations."""
    out = set()
    for part in lr._chunks(sorted(ids)):
        out |= {r[0] for r in conn.execute("SELECT DISTINCT verse_lexical_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL AND observation_id IN (SELECT value FROM json_each(?))", (json.dumps(part),))}
    return out


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
    nverse = s.get("pull_verse_texts", 12)
    spec = orec.items_setting(cfg)
    by_item = {i["key"]: i for i in spec["items"]}
    inter = cfg.setting("layer.interventions") or []
    prompts = cfg.setting("reading.observe_prompts") or {}
    nuances = cfg.setting("reading.nuance_pointers") or []
    out = []
    for r in rows[:cap]:
        lid, _, _, item, gid, subject, state, oid, reason, val = r
        idef = s["items"][item]
        dem = demanded(L, item, gid, subject)
        sources, required = _sources(conn, s, L, sd, gid)
        uses = [{"item": k, "name": by_item[k]["name"], "kinds": by_item[k]["kinds"], "bases": by_item[k]["bases"], "shared": by_item[k]["shared"],
                 "nuances": [x for x in nuances if x.get("item") == k]} for k in idef["uses"] if k in by_item]
        row = {"ledger_id": lid, "step": step, "item": item, "group": L["groups"][gid]["name"] if gid else None, "subject": subject, "asks": idef["asks"], "uses": uses,
               "node_roles": orec.node_role_groups(cfg), "interventions": inter, "prompts_by_kind": {k: v for k, v in prompts.items() if v},
               "to_take_up": [_obs_line(conn, i) for i in sorted(required)], "may_rest_on_besides": [_obs_line(conn, i) for i in sorted(sources - required)]}
        if step == "3.1":
            verses = _texts(conn, dem)
            row["definition_of_the_subgroup"] = L["groups"][gid].get("note")
            row["occurrences_total"] = len(dem)
            row["verses_of_the_subgroup"] = {k: v for k, v in list(verses.items())[:nverse]}
            row["verses_not_shown"] = max(0, len(verses) - nverse)
            strongs = sorted({o["strong"] for o in dem if o["strong"]})
            row["meaning_by_code"] = ve.meaning(cfg, conn, {c: ("NT" if c.startswith("G") else "OT") for c in strongs})
            earlier = collections.OrderedDict()
            for part in lr._chunks(sorted(_allowed(dem))):
                for r2 in conn.execute("SELECT o.id, o.stage, o.tag, o.obs_text FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 AND o.stage NOT IN "
                                       "(SELECT value FROM json_each(?)) AND n.verse_lexical_id IN (SELECT value FROM json_each(?)) ORDER BY o.id", (json.dumps(sorted(set(s["stages"].values()))), json.dumps(part))):
                    earlier.setdefault(r2[0], {"observation": r2[0], "stage": r2[1], "kind": r2[2], "text": (r2[3] or "")[:260], "action": None})
            row["earlier_observations_for_information"] = list(earlier.values())[:30]
        if step == "3.3":
            row["shared_verses"] = _texts(conn, dem)
        occ = [{"occurrence": o["vl_id"], "reference": o["reference"], "surface": o["surface"], "strong": o["strong"]} for o in dem][:s["pull_max_nodes"]]
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


def record(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check the filled file whole, write it in one savepoint and check the written rows as LayerCheck does; any problem refuses all (nothing written). keep=False rolls back (the preview)."""
    s = lr.settings(cfg)
    name, step = data.get("collection"), data.get("step")
    sd = lr.step_def(s, step)
    L = lr.load(conn, cfg, name, pairs=lr.needs_pairs(sd))
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
        dem = demanded(L, item, gid, subject)
        if not dem:
            errors.append(f"{where}: the data holds no occurrence for this aspect")
            continue
        allowed = _allowed(dem)
        sources, required = _sources(conn, s, L, sd, gid)
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
            f2 = _norm_nodes(conn, f, allowed, fw, errors)
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
        todo.append({"lrow": lrow, "disp": "observed", "specs": specs, "existing": ex, "where": where,
                     "state": {"not_used": {str(k): v for k, v in decl.items()} if step == "3.1" else {}, "not_gathered": {str(k): v for k, v in decl.items()} if step == "3.2" else {},
                               "read_back": {k: v for k, v in read_back.items() if v}}})
    if errors:
        raise lr.LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
    conn.execute("SAVEPOINT layer_inner")
    res = {"observed": 0, "none": 0, "nodes": 0, "withdrawn": 0}
    try:
        for t in todo:   # an earlier answer of the row is withdrawn first, so that its text is not a duplicate of the new one
            lid = t["lrow"][0]
            for (prev,) in conn.execute("SELECT id FROM ib_observation WHERE stable_key LIKE ? AND deleted=0", (f"layer:{lid}:%",)).fetchall():
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
        if errors:
            raise lr.LayerError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
        stage = s["stages"][str(sd["layer"])]
        for t in todo:
            lid = t["lrow"][0]
            if t["disp"] == "none":
                conn.execute(f"UPDATE collection_layer_item SET state='none', observation_id=NULL, reason=?, validated=0, updated_at={lr.NOW}, run_id=? WHERE id=?", (t["reason"], run_id, lid))
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
            written = orec.write(conn, t["plan"], None, run_id, stage=stage, stable_key=lambda k, lid=lid: f"layer:{lid}:{run_id}:{k}")
            first = min(w["observation"] for w in written.values())
            res["nodes"] += sum(len(w["nodes"]) for w in written.values())
            res["observed"] += sum(1 for w in written.values() if w["new"])
            conn.execute(f"UPDATE collection_layer_item SET state='observed', observation_id=?, reason=?, validated=0, updated_at={lr.NOW}, run_id=? WHERE id=?",
                         (first, STATE + json.dumps(t["state"], ensure_ascii=False, sort_keys=True), run_id, lid))
        L = lr.load(conn, cfg, name, pairs=lr.needs_pairs(sd))     # the grouping on the nodes is read back, so the check sees what was written
        for t in todo:
            if t["disp"] != "observed":
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
    dem = demanded(L, item, gid, subject)
    if not dem:
        return "the data no longer demands this aspect (LayerOpen retires it)"
    allowed = _allowed(dem)
    osis_of = {int(o["vl_id"]): o["osis"] for o in dem}
    stage = s["stages"][str(sd["layer"])]
    inner = _roles(cfg)
    groups = orec.node_role_groups(cfg)
    sources, required = _sources(conn, s, L, sd, gid)
    own = conn.execute("SELECT id, stage, tag, basis, route, parts, obs_text, stable_key FROM ib_observation WHERE deleted=0 AND stable_key LIKE ?", (f"layer:{lid}:%",)).fetchall()
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
            if n[0] not in allowed:
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
        miss = required - traced_all - decl
        if miss:
            return f"{len(miss)} observations are neither rested on by a finding nor declared (first: {sorted(miss)[0]}); nothing the step reads may be left out silently"
        if decl - required:
            return "it declares an observation this row does not take up"
    if step == "3.2" and not discovery:
        return "no behaviour: the collection row needs a flag finding of type discovery (or none, with its reason)"
    return None
