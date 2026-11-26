"""readcommands.py -- one command for each read of the layered reading of a collection (escalation #2538; design outputs/escalation/2538-read-commands-design-v1-20261125.md).

Researcher, 2026-11-25: "you need to build each sub process as a separate command, which feeds you with exactly the instruction to read, and what to do with it. The next command then
picks up the result from the database and do the same".

Every read has two halves. `read_<x>` writes ONE package for the reader: the instruction for this read (cfg_setting layer.read_types.<x>: what to read, how, what to write; the rules it
keeps are named there by key and their text is read live from cfg_method_rule, never copied), only the data of this unit, pulled from the database by indexed lookups in chunks, and the
answer template. `record_<x>` takes the filled answer, checks it whole and writes it in one transaction through the recorder of the layered reading (layerreading.record, every check of
the recorder applies), validates the unit's ledger rows (layerreading.check) and names the next command. The next command reads only the database. The reader is Claude in a session
(cfg_method_rule CP-08); no model is called here.

Built so far: the words (step S1, item word-sense; specification v5 section B1), with the older observations on each word's occurrences shown in the package (RW-09) and answered in
the same record (RW-13: the recorder refuses a word whose older observations are not answered); the senses (step 1.1, item group-definition; section B2), the whole subgroup in one
package: its B1 observations, each with the occurrences it holds, gathered by the reader into senses that carry them (`carries`), a B1 observation split between senses by naming its
occurrences, the occurrences no B1 observation holds (function words of a phrase surface) named with the readings of their verse; the enrichment
(step 1.2, item strong-enrichment), one package per subgroup: each 1.1 sense with its codes, and the lexicon of every code (the three sources, cut to lexicon_chars); one
enrichment for each sense, taking the sense's occurrences; the structure (step 2.1, items double-meaning, qualifier, entity, direction, pairing), one item at a time in batches of
rows, the verses of the package once with their stored structure in compact lines, the subgroup's 1.1 senses once; the sweep and the evidence validation (the gates of 2.1); the elements (step 3.1, one package
per subgroup); the behaviours (step 3.2, item collection-gathering; one package for the collection: every inner-being observation of it, each whole with its subgroups and
occurrences, recorded whole through layerinner.record). Step 3.3 (ReadMatches) and the validation after stage 4 wait for every collection to be complete (researcher 2026-11-26).
"""
from __future__ import annotations

import datetime
import json
import pathlib
import re
import time

from . import layerreading as lr
from . import scanguard as sg


class ReadError(Exception):
    """A usage or limit problem; routed as 'refused' and nothing is written."""


def settings(cfg) -> dict:
    v = cfg.required_setting("layer.read_types")
    return json.loads(v) if isinstance(v, str) else v


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def instruction(conn, rt: dict) -> dict:
    """The instruction of one read: its own steps from config, and the text of each rule it keeps, read now from cfg_method_rule, or from cfg_behaviour_rule for a
    rule named B:<id> (a behaviour rule a read depends on, such as B:72, the meaning of the routes of a party finding; #2576). A rule that is missing or inactive refuses."""
    keep, missing = [], []
    for code in rt["rules"]:
        if str(code).startswith("B:"):
            r = conn.execute("SELECT 'B:' || id || ' ' || rule_key, rule_text FROM cfg_behaviour_rule WHERE active=1 AND id=?", (int(str(code)[2:]),)).fetchone()
        else:
            r = conn.execute("SELECT rule_key, rule_text FROM cfg_method_rule WHERE active=1 AND (rule_key=? OR rule_key LIKE ?)", (code, code + " %")).fetchone()
        if r is None:
            missing.append(code)
        else:
            keep.append({"rule": r[0], "text": r[1]})
    if missing:
        raise ReadError(f"the read names rule(s) not active in cfg_method_rule: {', '.join(missing)} (cfg_setting layer.read_types)")
    return {"what": rt["what"], "read": rt["read"], "write": rt["write"], "keep": keep, "not_in_this_read": rt.get("not_in_this_read", "")}


def _subgroup(conn, name: str, subgroup: str) -> tuple[int, int, str]:
    c = conn.execute("SELECT id, name FROM collection WHERE deleted=0 AND lower(name)=?", (name.strip().lower(),)).fetchone()
    if c is None:
        raise ReadError(f"no live collection {name!r}")
    g = conn.execute("SELECT id, name FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (c[0], subgroup.strip().lower())).fetchone()
    if g is None:
        raise ReadError(f"collection {c[1]!r} has no live subgroup {subgroup!r}")
    return c[0], g[0], g[1]


def _word_rows(conn, cid: int, gid: int, step: str, item: str) -> list:
    return [r for r in lr._rows(conn, cid, step) if r[4] == gid and r[3] == item and r[6] != "retired"]


# ══ ReadWords / RecordWords: step S1, the words of one subgroup ═════════════════════════════════════════════════════════════════

def read_words(conn, cfg, run_id: str, name: str, subgroup: str, out_dir: pathlib.Path) -> dict:
    """Write the package of the next words of the subgroup to read. Opens step S1 for the subgroup if it is not open (the order gate and the grouping gate apply)."""
    t0 = time.monotonic()
    st = settings(cfg)
    rt, lim = st["words"], st["limits"]
    s = lr.settings(cfg)
    step, item = rt["step"], rt["item"]
    idef = s["items"][item]
    cid, gid, gname = _subgroup(conn, name, subgroup)
    rows = _word_rows(conn, cid, gid, step, item)
    opened = None
    if not rows:
        opened = lr.open_step(conn, cfg, run_id, name, step, subgroup=gname)
        rows = _word_rows(conn, cid, gid, step, item)
    todo = [r for r in rows if r[6] == "open" or (r[6] == "observed" and not r[9])]
    if not todo:
        raise ReadError(f"every word of {gname!r} is read and validated ({len(rows)} rows); next: " + next_after_words(conn, cid, gid, name, gname, step))
    pulled = {}
    for part in sg.chunks([r[0] for r in todo], cfg):
        pulled.update(dict(conn.execute(f"SELECT id, pulled_at FROM collection_layer_item WHERE id IN ({','.join('?' * len(part))})", part).fetchall()))
    if any(not pulled.get(r[0]) for r in todo):      # a word already in a package and not yet answered is not sent again while any word has not been sent;
        todo = [r for r in todo if not pulled.get(r[0])]      # once every open word is sent, they are offered again, oldest package first (a package lost is not a word lost)
        todo.sort(key=lambda r: (r[6] != "observed", r[5]))      # a recorded row that failed its check first, then the open rows by word
    else:
        todo.sort(key=lambda r: (pulled.get(r[0]) or "", r[5]))
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    words, size, taken, shown_old = [], 0, [], {}
    layer = lr.step_def(s, step)["layer"]
    with sg.budget(conn, cfg, "ReadWords"):
        for r in todo:
            if len(words) >= rt["batch_words"]:
                break
            lid, subject = r[0], r[5]
            surface, _, strong = subject.rpartition("|")
            occ = [o for o, _ in lr.expected_nodes(L, item, gid, subject)]
            info, text_of = {}, {}
            for part in sg.chunks([o["vl_id"] for o in occ], cfg):
                for x in conn.execute("SELECT id, morph_code, unit_surface, surface_kind, is_negator, party_kind, narrative_morph FROM verse_lexical "
                                      f"WHERE id IN ({','.join('?' * len(part))})", part):
                    info[x[0]] = x
            for part in sg.chunks(sorted({o["verse_id"] for o in occ}), cfg):
                text_of.update({v[0]: v[1] for v in conn.execute(f"SELECT id, text FROM verse WHERE id IN ({','.join('?' * len(part))})", part)})
            occs = []
            for o in occ:
                x = info.get(o["vl_id"]) or (None,) * 7
                occs.append({"occurrence": o["vl_id"], "reference": o["reference"], "morph": x[1], "unit": x[2], "surface_kind": x[3], "negator": bool(x[4]),
                             "party_kind": x[5], "narrative": x[6], "verse": text_of.get(o["verse_id"]) or ""})
            older = lr.bv.older_on(conn, cfg, s, [o["vl_id"] for o in occ], layer)      # the older observations on these occurrences: seen in the reading (RW-09), answered with it (RW-13)
            pending = sorted(set(older) - lr.bv.settled(conn, cfg, older) - lr.bv.carried_later(conn, older, step))
            olds, elsewhere = [], []
            for oid in pending:
                if oid in shown_old:
                    elsewhere.append({"observation": oid, "answered_under": shown_old[oid]})
                    continue
                o_ = conn.execute("SELECT id, stage, tag, nature, obs_text FROM ib_observation WHERE id=? AND deleted=0", (oid,)).fetchone()
                if o_ is None:
                    continue
                refs = [x[0] for x in conn.execute("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_reference IS NOT NULL", (oid,))]
                olds.append({"observation": o_[0], "stage": o_[1], "kind": o_[2], "nature": o_[3], "text": o_[4] or "", "verses": refs})
                shown_old[oid] = subject
            w = {"ledger_id": lid, "word": surface, "strong": strong, "lexicon": lr._lexicon(conn, strong), "occurrences": occs, "older": olds}
            if elsewhere:
                w["older_answered_under_another_word"] = elsewhere
            if r[6] == "observed":
                w["recorded_before"] = "this word was recorded but its check failed: read it again (the record replaces the earlier reading)"
            n = len(json.dumps(w, ensure_ascii=False))
            if words and size + n > lim["package_max_chars"]:
                break
            words.append(w)
            taken.append(lid)
            size += n
            if time.monotonic() - t0 > lim["read_max_seconds"]:
                raise ReadError(f"ReadWords for {gname!r} took more than {lim['read_max_seconds']} s (cfg_setting layer.read_types limits) at word {subject}; nothing is written")
    for part in sg.chunks(taken, cfg):      # the ledger is stamped as the work happens: the package is an event of each row it carries
        conn.execute(f"UPDATE collection_layer_item SET pulled_at={lr.NOW}, updated_at={lr.NOW} WHERE id IN ({','.join('?' * len(part))})", part)
    left = len(todo) - len(words)
    kinds = " | ".join(idef.get("kinds", [idef["kind"]]))
    pkg = {"command": "ReadWords", "collection": L["name"], "subgroup": gname, "step": step,
           "made": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "batch": {"words": len(words), "words_left_after_this": left},
           "instruction": instruction(conn, rt), "prompts": lr._prompts(conn, idef.get("prompts", [])), "words": words,
           "answer": {"command": "ReadWords", "collection": L["name"], "subgroup": gname,
                      "rows": [{"ledger_id": w["ledger_id"], "word": f"{w['word']}|{w['strong']}",
                                "readings": [{"kind": kinds, "obs_text": "", "basis": "stated | read", "grounds": "", "occurrences": []}],
                                "older": [{"observation": o["observation"], "action": " | ".join(lr.bv.ACTIONS), "reason": ""} for o in w["older"]]} for w in words]}}
    secs = round(time.monotonic() - t0, 2)
    chars = len(json.dumps(pkg, ensure_ascii=False))
    pkg["measured"] = {"package_chars": chars, "seconds": secs}
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"readwords-{_slug(L['name'])}-{_slug(gname)}-{datetime.datetime.now().strftime('%Y%m%dt%H%M%S')}.json"
    path.write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"path": path, "words": len(words), "left": left, "chars": chars, "seconds": secs, "opened": opened}


def record_words(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check a filled ReadWords answer whole and write it through the recorder; then validate the subgroup's rows and name the next command. keep=False previews (nothing kept)."""
    rt = settings(cfg)["words"]
    s = lr.settings(cfg)
    step, item = rt["step"], rt["item"]
    idef = s["items"][item]
    if data.get("command") != "ReadWords":
        raise ReadError("this is not a ReadWords answer (its `command` must be ReadWords; fill the `answer` part of the package)")
    name, sub = str(data.get("collection") or ""), str(data.get("subgroup") or "")
    cid, gid, gname = _subgroup(conn, name, sub)
    mine = {r[0]: r for r in _word_rows(conn, cid, gid, step, item)}
    errors, rows = [], []
    for i, row in enumerate(data.get("rows") or [], 1):
        lid = row.get("ledger_id")
        if lid not in mine:
            errors.append(f"row {i}: ledger {lid} is not a word of subgroup {gname!r} in step {step}")
            continue
        rows.append({"ledger_id": lid, "fill": {"disposition": "observed", "senses": row.get("readings") or [], "member_role": idef["member_role"], "older": row.get("older") or []}})
    if not rows and not errors:
        errors.append("the answer holds no row")
    if errors:
        raise ReadError("the answer is refused whole, nothing written:\n  " + "\n  ".join(errors))
    try:
        r = lr.record(conn, cfg, run_id, {"collection": name, "step": step, "subgroup": gname, "rows": rows}, keep)
    except lr.LayerError as exc:
        raise ReadError(str(exc))
    out = {"observed": r["observed"], "nodes": r["nodes"], "rows": len(rows)}
    if not keep:
        return {**out, "preview": True}
    lr.check(conn, cfg, run_id, name, subgroup=gname)
    after = {x[0]: x for x in _word_rows(conn, cid, gid, step, item)}
    failed = [after[x["ledger_id"]][5] for x in rows if not after[x["ledger_id"]][9]]
    left = sum(1 for x in after.values() if x[6] == "open")
    return {**out, "validated": len(rows) - len(failed), "failed": failed, "words_open": left, "next": next_after_words(conn, cid, gid, name, gname, step)}


def _next(conn, cid: int, gid: int, name: str, gname: str, step: str, again: str, then: str, items=None) -> str:
    """The next command once an answer is recorded: `again` while any row of the step is open or failed its check, then `then`. Older observations of the step open on no row's occurrences
    are named: no package of the step carries them."""
    rows = [r for r in lr._rows(conn, cid, step) if r[4] == gid and r[6] != "retired"]
    cmd = f".\\iba\\app\\ps\\Collection-Build.ps1 -Collection {name} -Subgroup '{gname}'"
    if any(r[3] != lr.bv.OLD_ITEM and (items is None or r[3] in items) and (r[6] == "open" or (r[6] == "observed" and not r[9])) for r in rows):
        return f"{cmd} -Action {again}"
    left = sum(1 for r in rows if r[3] == lr.bv.OLD_ITEM and r[6] == "open")
    if left:
        return (f"no command yet: {left} older observation(s) of step {step} are open but on no occurrence of the step's rows, so no package of the step carries them; they are answered by "
                f"the sweep at the end of step 2.1 (ReadSweep)")
    return f"{cmd} -Action {then}"


def next_after_words(conn, cid: int, gid: int, name: str, gname: str, step: str) -> str:
    return _next(conn, cid, gid, name, gname, step, "ReadWords", "ReadSenses")


def next_after_senses(conn, cid: int, gid: int, name: str, gname: str, step: str) -> str:
    return _next(conn, cid, gid, name, gname, step, "ReadSenses", "ReadEnrichment")


def _older(conn, cfg, s: dict, vl_ids: list, layer: int, step: str) -> list:
    """The older observations on these occurrences still to be answered at this step (RW-09, RW-13): not judged by a reading, not carried to a later step; each with its text and verses."""
    older = lr.bv.older_on(conn, cfg, s, vl_ids, layer)
    out = []
    for oid in sorted(set(older) - lr.bv.settled(conn, cfg, older) - lr.bv.carried_later(conn, older, step)):
        o_ = conn.execute("SELECT id, stage, tag, nature, obs_text FROM ib_observation WHERE id=? AND deleted=0", (oid,)).fetchone()
        if o_ is None:
            continue
        refs = [x[0] for x in conn.execute("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_reference IS NOT NULL", (oid,))]
        out.append({"observation": o_[0], "stage": o_[1], "kind": o_[2], "nature": o_[3], "text": o_[4] or "", "verses": refs})
    return out


# ══ ReadSenses / RecordSenses: step 1.1, the senses of one subgroup ══════════════════════════════════════════════════════════════

def _senses_data(conn, cfg, s: dict, rt: dict, L: dict, gid: int, subject: str, item: str) -> dict:
    """The data of a senses read for one subgroup, read only: its occurrences, the B1 observations on them (each with the occurrences of the subgroup it holds), the occurrences no B1
    observation holds, and the sense head and meaning range of each code. Indexed lookups in chunks."""
    occ = {o["vl_id"]: o for o, _ in lr.expected_nodes(L, item, gid, subject)}
    b1 = lr.trace_targets(conn, 0, list(occ), [s["items"][item]["carries_all_of"]], L["cid"])
    held: dict = {}
    for part in sg.chunks(b1, cfg):
        for oid, vl in conn.execute(f"SELECT observation_id, verse_lexical_id FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND observation_id IN ({','.join('?' * len(part))})", part):
            if vl in occ:
                held.setdefault(oid, set()).add(vl)
    meta = {}
    for part in sg.chunks(b1, cfg):
        for r in conn.execute(f"SELECT id, tag, obs_text, basis, parts FROM ib_observation WHERE deleted=0 AND id IN ({','.join('?' * len(part))})", part):
            meta[r[0]] = r
    readings = []
    for oid in b1:
        if oid not in meta or oid not in held:
            continue
        _, tag, text, basis, parts = meta[oid]
        vls = sorted(held[oid], key=lambda v: (occ[v]["verse_id"], v))
        words = sorted({f"{occ[v]['surface']}|{occ[v]['strong']}" for v in vls})
        readings.append({"observation": oid, "words": words, "kind": tag, "text": text or "", "basis": basis, "grounds": (json.loads(parts) if parts else {}).get("grounds"),
                         "occurrences": [{"occurrence": v, "reference": occ[v]["reference"]} for v in vls]})
    covered = set().union(*held.values()) if held else set()
    in_verse: dict = {}      # the readings holding an occurrence in each verse: an occurrence no reading holds (a function word of a phrase surface, RG-22) is placed with its phrase
    for b, vls in held.items():
        for v in vls:
            in_verse.setdefault(occ[v]["verse_id"], set()).add(b)
    loose = [{"occurrence": v, "reference": o["reference"], "word": f"{o['surface']}|{o['strong']}", "readings_in_the_verse": sorted(in_verse.get(o["verse_id"], set()))}
             for v, o in occ.items() if v not in covered]
    codes = {}
    for code in sorted({o["strong"] for o in occ.values() if o["strong"]}):
        surfaces = sorted({o["surface"] for o in occ.values() if o["strong"] == code})
        if rt.get("full_lexicon"):      # the enrichment read: the lexicon is the point (R5): the three sources and the related words, each cut to lexicon_chars
            codes[code] = {"surfaces": surfaces, **lr._lexicon(conn, code, rt["lexicon_chars"])}
            continue
        h = conn.execute("SELECT head FROM strong_sense WHERE strong=? AND deleted=0", (code,)).fetchone()
        tree = [f"{r[0] or ''} {r[1] or ''}".strip() for r in conn.execute("SELECT sense_code, sense_text FROM strong_meaning_tree WHERE strong_variant=? AND deleted=0 ORDER BY sort", (code,))]
        codes[code] = {"surfaces": surfaces, "sense_head": h[0] if h else None, "meaning_range": "; ".join(tree)[:rt["lexicon_chars"]]}
    return {"occ": occ, "readings": readings, "loose": loose, "codes": codes, "held": held}


def read_senses(conn, cfg, run_id: str, name: str, subgroup: str, out_dir: pathlib.Path) -> dict:
    """Write the package of the senses of one subgroup (step 1.1): every B1 observation of the subgroup to gather into senses. Opens 1.1 for the subgroup if it is not open (S1 closed,
    the order gate)."""
    t0 = time.monotonic()
    st = settings(cfg)
    rt, lim = st["senses"], st["limits"]
    s = lr.settings(cfg)
    step, item = rt["step"], rt["item"]
    idef = s["items"][item]
    cid, gid, gname = _subgroup(conn, name, subgroup)
    rows = _word_rows(conn, cid, gid, step, item)
    opened = None
    if not rows:
        opened = lr.open_step(conn, cfg, run_id, name, step, subgroup=gname)
        rows = _word_rows(conn, cid, gid, step, item)
    todo = [r for r in rows if r[6] == "open" or (r[6] == "observed" and not r[9])]
    if not todo:
        raise ReadError(f"the senses of {gname!r} are read and validated; next: " + next_after_senses(conn, cid, gid, name, gname, step))
    r = todo[0]
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    with sg.budget(conn, cfg, "ReadSenses"):
        d = _senses_data(conn, cfg, s, rt, L, gid, r[5], item)
        older = _older(conn, cfg, s, list(d["occ"]), lr.step_def(s, step)["layer"], step)
    conn.execute(f"UPDATE collection_layer_item SET pulled_at={lr.NOW}, updated_at={lr.NOW} WHERE id=?", (r[0],))
    pkg = {"command": "ReadSenses", "collection": L["name"], "subgroup": gname, "step": step,
           "made": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "unit": {"ledger_id": r[0], "occurrences": len(d["occ"]), "readings": len(d["readings"]), "codes": len(d["codes"]), "older": len(older)},
           "instruction": instruction(conn, rt), "prompts": lr._prompts(conn, idef.get("prompts", [])),
           "readings": d["readings"], "occurrences_in_no_reading": d["loose"], "codes": d["codes"], "older": older,
           "answer": {"command": "ReadSenses", "collection": L["name"], "subgroup": gname, "ledger_id": r[0],
                      "senses": [{"kind": idef["kind"], "obs_text": "", "basis": "read | stated", "grounds": "", "carries": [], "occurrences": []}],
                      "older": [{"observation": o["observation"], "action": " | ".join(lr.bv.ACTIONS), "reason": ""} for o in older]}}
    if r[6] == "observed":
        pkg["recorded_before"] = "the senses were recorded but their check failed: read them again (the record replaces the earlier reading)"
    secs = round(time.monotonic() - t0, 2)
    chars = len(json.dumps(pkg, ensure_ascii=False))
    pkg["measured"] = {"package_chars": chars, "seconds": secs}
    if secs > lim["read_max_seconds"]:
        raise ReadError(f"ReadSenses for {gname!r} took {secs} s, more than {lim['read_max_seconds']} s (cfg_setting layer.read_types limits); nothing is written")
    if chars > rt["package_max_chars"]:
        raise ReadError(f"the senses package of {gname!r} is {chars} characters, more than {rt['package_max_chars']} (cfg_setting layer.read_types senses.package_max_chars); nothing is written")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"readsenses-{_slug(L['name'])}-{_slug(gname)}-{datetime.datetime.now().strftime('%Y%m%dt%H%M%S')}.json"
    path.write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"path": path, "readings": len(d["readings"]), "occurrences": len(d["occ"]), "older": len(older), "chars": chars, "seconds": secs, "opened": opened}


def record_senses(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check a filled ReadSenses answer whole: each sense's `carries` (B1 observations of the subgroup) become the occurrences they hold, joined with any `occurrences` named; every B1
    observation is carried or has its occurrences named. Then write through the recorder (exactly once, coverage, text rules, traces to B1, RW-13), validate, name the next command."""
    rt = settings(cfg)["senses"]
    s = lr.settings(cfg)
    step, item = rt["step"], rt["item"]
    idef = s["items"][item]
    if data.get("command") != "ReadSenses":
        raise ReadError("this is not a ReadSenses answer (its `command` must be ReadSenses; fill the `answer` part of the package)")
    name, sub = str(data.get("collection") or ""), str(data.get("subgroup") or "")
    cid, gid, gname = _subgroup(conn, name, sub)
    mine = {r[0]: r for r in _word_rows(conn, cid, gid, step, item)}
    lid = data.get("ledger_id")
    if lid not in mine:
        raise ReadError(f"the answer is refused whole, nothing written:\n  ledger {lid} is not the {item} row of subgroup {gname!r} in step {step}")
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    d = _senses_data(conn, cfg, s, rt, L, gid, mine[lid][5], item)
    errors, senses, carried = [], [], {}
    for k, sn in enumerate(data.get("senses") or [], 1):
        occs = list(sn.get("occurrences") or [])
        for b in sn.get("carries") or []:
            if b not in d["held"]:
                errors.append(f"sense {k}: carries {b!r}, which is not a B1 observation of subgroup {gname!r}")
                continue
            if b in carried:
                errors.append(f"sense {k}: B1 observation {b} is already carried by sense {carried[b]} (each B1 observation is carried by one sense; split it by naming its occurrences)")
            carried[b] = k
            occs += sorted(d["held"][b])
        senses.append({**{x: sn.get(x) for x in ("kind", "obs_text", "basis", "grounds")}, "occurrences": occs})
    named = {o for sn in senses for o in sn["occurrences"] if isinstance(o, int)}
    for b, vls in d["held"].items():
        if b not in carried and not (vls & named):
            errors.append(f"B1 observation {b} is carried by no sense and none of its occurrences is named (every B1 observation of the subgroup is carried)")
    if not senses:
        errors.append("the answer holds no sense")
    if errors:
        raise ReadError("the answer is refused whole, nothing written:\n  " + "\n  ".join(errors))
    rows = [{"ledger_id": lid, "fill": {"disposition": "observed", "senses": senses, "member_role": idef["member_role"], "older": data.get("older") or []}}]
    try:
        r = lr.record(conn, cfg, run_id, {"collection": name, "step": step, "subgroup": gname, "rows": rows}, keep)
    except lr.LayerError as exc:
        raise ReadError(str(exc))
    out = {"observed": r["observed"], "nodes": r["nodes"], "senses": len(senses)}
    if not keep:
        return {**out, "preview": True}
    lr.check(conn, cfg, run_id, name, subgroup=gname)
    after = {x[0]: x for x in _word_rows(conn, cid, gid, step, item)}
    return {**out, "validated": bool(after[lid][9]), "reason": after[lid][8], "next": next_after_senses(conn, cid, gid, name, gname, step)}


# ══ ReadEnrichment / RecordEnrichment: step 1.2, what the codes of each sense say ═════════════════════════════════════════════════

def next_after_enrichment(conn, cid: int, gid: int, name: str, gname: str, step: str) -> str:
    return _next(conn, cid, gid, name, gname, step, "ReadEnrichment", "ReadStructure")


def read_enrichment(conn, cfg, run_id: str, name: str, subgroup: str, out_dir: pathlib.Path) -> dict:
    """Write the package of the enrichment of one subgroup (step 1.2): every 1.1 sense of the subgroup with the occurrences and words it holds, and the lexicon of every code (the three
    sources and the related words, each cut to lexicon_chars): one enrichment for each sense. Opens 1.2 for the subgroup if it is not open (1.1 closed, the order gate)."""
    t0 = time.monotonic()
    st = settings(cfg)
    rt, lim = st["enrichment"], st["limits"]
    s = lr.settings(cfg)
    step, item = rt["step"], rt["item"]
    cid, gid, gname = _subgroup(conn, name, subgroup)
    rows = _word_rows(conn, cid, gid, step, item)
    opened = None
    if not rows:
        opened = lr.open_step(conn, cfg, run_id, name, step, subgroup=gname)
        rows = _word_rows(conn, cid, gid, step, item)
    todo = [r for r in rows if r[6] == "open" or (r[6] == "observed" and not r[9])]
    if not todo:
        raise ReadError(f"the enrichment of {gname!r} is read and validated; next: " + next_after_enrichment(conn, cid, gid, name, gname, step))
    r = todo[0]
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    with sg.budget(conn, cfg, "ReadEnrichment"):
        d = _senses_data(conn, cfg, s, rt, L, gid, r[5], item)
        older = _older(conn, cfg, s, list(d["occ"]), lr.step_def(s, step)["layer"], step)
    conn.execute(f"UPDATE collection_layer_item SET pulled_at={lr.NOW}, updated_at={lr.NOW} WHERE id=?", (r[0],))
    senses = [{"sense": x["observation"], "text": x["text"], "codes": sorted({w.rpartition("|")[2] for w in x["words"]}), "words": x["words"],
               "occurrences": [o["reference"] for o in x["occurrences"]]} for x in d["readings"]]
    idef = s["items"][item]
    pkg = {"command": "ReadEnrichment", "collection": L["name"], "subgroup": gname, "step": step,
           "made": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "unit": {"ledger_id": r[0], "senses": len(senses), "occurrences": len(d["occ"]), "codes": len(d["codes"]), "older": len(older)},
           "instruction": instruction(conn, rt), "prompts": lr._prompts(conn, idef.get("prompts", [])),
           "senses": senses, "occurrences_in_no_sense": d["loose"], "codes": d["codes"], "older": older,
           "answer": {"command": "ReadEnrichment", "collection": L["name"], "subgroup": gname, "ledger_id": r[0],
                      "enrichments": [{"sense": x["sense"], "kind": idef["kind"], "obs_text": "", "basis": "read | stated", "grounds": ""} for x in senses],
                      "older": [{"observation": o["observation"], "action": " | ".join(lr.bv.ACTIONS), "reason": ""} for o in older]}}
    if r[6] == "observed":
        pkg["recorded_before"] = "the enrichment was recorded but its check failed: read it again (the record replaces the earlier reading)"
    secs = round(time.monotonic() - t0, 2)
    chars = len(json.dumps(pkg, ensure_ascii=False))
    pkg["measured"] = {"package_chars": chars, "seconds": secs}
    if secs > lim["read_max_seconds"]:
        raise ReadError(f"ReadEnrichment for {gname!r} took {secs} s, more than {lim['read_max_seconds']} s (cfg_setting layer.read_types limits); nothing is written")
    if chars > rt["package_max_chars"]:
        raise ReadError(f"the enrichment package of {gname!r} is {chars} characters, more than {rt['package_max_chars']} (cfg_setting layer.read_types enrichment.package_max_chars); nothing is written")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"readenrichment-{_slug(L['name'])}-{_slug(gname)}-{datetime.datetime.now().strftime('%Y%m%dt%H%M%S')}.json"
    path.write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"path": path, "senses": len(senses), "codes": len(d["codes"]), "older": len(older), "chars": chars, "seconds": secs, "opened": opened}


def record_enrichment(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check a filled ReadEnrichment answer whole: one enrichment for each 1.1 sense of the subgroup, named by `sense`; each takes the sense's occurrences. An occurrence held by no sense
    is named in an enrichment's `occurrences`. Then write through the recorder (exactly once, coverage, lexicon grounds, traces to the sense, RW-13), validate, name the next command."""
    rt = settings(cfg)["enrichment"]
    s = lr.settings(cfg)
    step, item = rt["step"], rt["item"]
    idef = s["items"][item]
    if data.get("command") != "ReadEnrichment":
        raise ReadError("this is not a ReadEnrichment answer (its `command` must be ReadEnrichment; fill the `answer` part of the package)")
    name, sub = str(data.get("collection") or ""), str(data.get("subgroup") or "")
    cid, gid, gname = _subgroup(conn, name, sub)
    mine = {r[0]: r for r in _word_rows(conn, cid, gid, step, item)}
    lid = data.get("ledger_id")
    if lid not in mine:
        raise ReadError(f"the answer is refused whole, nothing written:\n  ledger {lid} is not the {item} row of subgroup {gname!r} in step {step}")
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    d = _senses_data(conn, cfg, s, rt, L, gid, mine[lid][5], item)
    errors, built, done = [], [], {}
    for k, en in enumerate(data.get("enrichments") or [], 1):
        sid = en.get("sense")
        if sid not in d["held"]:
            errors.append(f"enrichment {k}: sense {sid!r} is not a 1.1 sense of subgroup {gname!r}")
            continue
        if sid in done:
            errors.append(f"enrichment {k}: sense {sid} is already enriched by enrichment {done[sid]} (one enrichment for each sense)")
            continue
        done[sid] = k
        built.append({**{x: en.get(x) for x in ("kind", "obs_text", "basis", "grounds")}, "occurrences": sorted(d["held"][sid]) + list(en.get("occurrences") or [])})
    for sid in sorted(set(d["held"]) - set(done)):
        errors.append(f"sense {sid} has no enrichment (one enrichment for each 1.1 sense of the subgroup)")
    if not built and not errors:
        errors.append("the answer holds no enrichment")
    if errors:
        raise ReadError("the answer is refused whole, nothing written:\n  " + "\n  ".join(errors))
    rows = [{"ledger_id": lid, "fill": {"disposition": "observed", "senses": built, "member_role": idef["member_role"], "older": data.get("older") or []}}]
    try:
        r = lr.record(conn, cfg, run_id, {"collection": name, "step": step, "subgroup": gname, "rows": rows}, keep)
    except lr.LayerError as exc:
        raise ReadError(str(exc))
    out = {"observed": r["observed"], "nodes": r["nodes"], "enrichments": len(built)}
    if not keep:
        return {**out, "preview": True}
    lr.check(conn, cfg, run_id, name, subgroup=gname)
    after = {x[0]: x for x in _word_rows(conn, cid, gid, step, item)}
    return {**out, "validated": bool(after[lid][9]), "reason": after[lid][8], "next": next_after_enrichment(conn, cid, gid, name, gname, step)}


# ══ ReadStructure / RecordStructure: step 2.1, what stands with the subgroup in each verse ═════════════════════════════════════════

STRUCTURE_ITEMS = ("double-meaning", "qualifier", "entity", "direction", "pairing")


def next_after_structure(conn, cid: int, gid: int, name: str, gname: str, step: str) -> str:
    return _next(conn, cid, gid, name, gname, step, "ReadStructure", "ReadSweep", STRUCTURE_ITEMS)


def _verse_lines(conn, cfg, L: dict, refs: set, gid: int) -> list:
    """The verses named, each with its text and one compact line for each word of the verse, from the stored structure (verse_lexical through the pairing load):
    position, surface, code, morph, then what the pairing makes of it (type, the qualifier it carries, a negator, a party), * for an occurrence of the subgroup."""
    rows = [x for x in L["pairs"]["rows"] if x["reference"] in refs]
    text = {}
    for part in sg.chunks(sorted({x["verse_id"] for x in rows}), cfg):
        if part:
            text.update({v[0]: v[1] for v in conn.execute(f"SELECT id, text FROM verse WHERE id IN ({','.join('?' * len(part))})", part)})
    member = {p["member"]["vl_id"]: p["member"] for p in L["pairs"]["pairs"]}
    mine = {o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid}      # the subgroup's occurrences, with or without a pairing in the verse
    other = {p["other"]["vl_id"]: p["other"] for p in L["pairs"]["pairs"]}
    by: dict = {}
    for x in rows:
        by.setdefault(x["verse_id"], []).append(x)
    out = []
    for v in sorted(by, key=lambda i: by[i][0]["sk"]):
        words = []
        for x in sorted(by[v], key=lambda y: (y["position"] if y["position"] is not None else 0, y["code_ordinal"] or 0, y["vl_id"])):
            m = member.get(x["vl_id"]) or other.get(x["vl_id"]) or {}
            tags = [t for t in (m.get("type"), (f"qualifier {m['qualifier']}" if m.get("qualifier") else ""), ("negator" if x.get("is_negator") else ""),
                                (f"party {x['party_kind']}" if x.get("party_kind") else ""),
                                ("collections " + ", ".join(m["collections"]) if m.get("type") == "word of another collection" and m.get("collections") else "")) if t]
            words.append(f"{'*' if x['vl_id'] in mine else ' '}{x['position']} {x['surface']} {x['strong']} {x['morph']}" + (f" | {'; '.join(tags)}" if tags else ""))
        out.append({"reference": by[v][0]["reference"], "text": text.get(v) or "", "words": words})
    return out


def _structure_answer_row(x: dict, s: dict) -> dict:
    """The answer template of one 2.1 row."""
    return {"ledger_id": x["ledger_id"], "item": x["item"], "subject": x["subject"], "disposition": "observed | none" if x["none_allowed"] else "observed",
            "findings": [{"kind": s["items"][x["item"]]["kind"], "obs_text": "", "basis": "read | stated", "grounds": "", "occurrences": []}], "reason": "",
            "older": [{"observation": o["observation"], "action": " | ".join(lr.bv.ACTIONS), "reason": ""} for o in x["older"]]}


def read_structure(conn, cfg, run_id: str, name: str, subgroup: str, out_dir: pathlib.Path, item: str | None = None) -> dict:
    """Write the package of the next rows of step 2.1 for one subgroup: the rows of one item at a time (double-meaning, qualifier, entity, direction, then pairing, one row for each partner
    collection), at most batch_rows, within package_max_chars. Each row carries what it asks, the occurrences it demands (members and partners), the WordNet control of a pairing,
    and the older observations on its occurrences (each once); the verses of the package are given once, with their stored structure; the subgroup's 1.1 senses, which every finding
    traces to, are given once. Opens 2.1 for the subgroup if it is not open (1.2 closed, the order gate)."""
    t0 = time.monotonic()
    st = settings(cfg)
    rt, lim = st["structure"], st["limits"]
    s = lr.settings(cfg)
    step = rt["step"]
    cid, gid, gname = _subgroup(conn, name, subgroup)
    if item and item not in STRUCTURE_ITEMS:
        raise ReadError(f"-Item must be one of {list(STRUCTURE_ITEMS)}")
    rows = [r for r in lr._rows(conn, cid, step) if r[4] == gid and r[3] in STRUCTURE_ITEMS and r[6] != "retired"]
    opened = None
    if not rows:
        opened = lr.open_step(conn, cfg, run_id, name, step, subgroup=gname)
        rows = [r for r in lr._rows(conn, cid, step) if r[4] == gid and r[3] in STRUCTURE_ITEMS and r[6] != "retired"]
    todo = [r for r in rows if (r[6] == "open" or (r[6] == "observed" and not r[9])) and (not item or r[3] == item)]
    if not todo:
        if item and any(r[6] == "open" or (r[6] == "observed" and not r[9]) for r in rows):
            raise ReadError(f"no {item} row of {gname!r} is open; other items are: run ReadStructure without -Item")
        raise ReadError(f"the structure of {gname!r} is read and validated ({len(rows)} rows); next: " + next_after_structure(conn, cid, gid, name, gname, step))
    pulled = {}
    for part in sg.chunks([r[0] for r in todo], cfg):
        pulled.update(dict(conn.execute(f"SELECT id, pulled_at FROM collection_layer_item WHERE id IN ({','.join('?' * len(part))})", part).fetchall()))
    fresh = [r for r in todo if not pulled.get(r[0])]
    pool = fresh or sorted(todo, key=lambda r: pulled.get(r[0]) or "")      # a row sent and not answered is sent again only when every open row has been sent
    first = sorted(pool, key=lambda r: (STRUCTURE_ITEMS.index(r[3]), r[5]))[0][3]
    pool = sorted([r for r in pool if r[3] == first], key=lambda r: r[5])      # one item for each package
    L = lr.load(conn, cfg, name, pairs=True, subgroup=gname)
    layer = lr.step_def(s, step)["layer"]
    out_rows, taken, refs, shown_old, wn = [], [], set(), {}, None
    ins = instruction(conn, rt)
    with sg.budget(conn, cfg, "ReadStructure"):
        l11 = [x[0] for x in conn.execute("SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND step='1.1' AND item='group-definition' AND deleted=0 AND state!='retired'", (cid, gid))]
        senses = []
        for lid1 in l11:
            for oid, text in conn.execute("SELECT id, obs_text FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid1}:", f"layer:{lid1};")):
                refs1 = [x[0] for x in conn.execute("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND deleted=0 AND verse_reference IS NOT NULL", (oid,))]
                senses.append({"sense": oid, "text": text, "verses": refs1})
        size = len(json.dumps(ins, ensure_ascii=False)) + len(json.dumps(senses, ensure_ascii=False)) + 2000      # the fixed parts of the package (and its frame) count against the limit
        for r in pool:
            if len(out_rows) >= rt["batch_rows"]:
                break
            lid, item_, subject = r[0], r[3], r[5]
            idef = s["items"][item_]
            nodes = lr.expected_nodes(L, item_, gid, subject)
            occ = [{"occurrence": o["vl_id"], "reference": o["reference"], "surface": o["surface"], "strong": o["strong"], "as": role} for o, role in nodes]
            olds, elsewhere = [], []
            for o in _older(conn, cfg, s, [o["vl_id"] for o, _ in nodes], layer, step):
                if o["observation"] in shown_old:
                    elsewhere.append({"observation": o["observation"], "answered_under": shown_old[o["observation"]]})
                    continue
                shown_old[o["observation"]] = lid
                olds.append(o)
            row = {"ledger_id": lid, "item": item_, "subject": subject, "asks": idef["asks"], "none_allowed": idef["none_allowed"],
                   "verses": sorted({o["reference"] for o in occ}, key=lambda x: next((o["sk"] for o, _ in nodes if o["reference"] == x), x)), "occurrences": occ, "older": olds}
            if elsewhere:
                row["older_answered_under_another_row"] = elsewhere
            if item_ == "pairing":
                if wn is None:
                    wn = lr.wordnet_control(conn, L, gid)
                row["wordnet_control"] = wn.get(subject.replace("collection:", "")) or "WordNet relates no surface of the subgroup to this collection (a verse-only pairing: no control)"
            if r[6] == "observed":
                row["recorded_before"] = "this row was recorded but its check failed: read it again (the record replaces the earlier reading)"
            n = len(json.dumps(row, ensure_ascii=False)) + sum(len(json.dumps(v, ensure_ascii=False)) for v in _verse_lines(conn, cfg, L, set(row["verses"]) - refs, gid))
            n += len(json.dumps(_structure_answer_row(row, s), ensure_ascii=False))      # its row of the answer template counts too
            if out_rows and size + n > rt["package_max_chars"]:
                break
            out_rows.append(row)
            taken.append(lid)
            refs |= set(row["verses"])
            size += n
            if time.monotonic() - t0 > lim["read_max_seconds"]:
                raise ReadError(f"ReadStructure for {gname!r} took more than {lim['read_max_seconds']} s (cfg_setting layer.read_types limits) at row {lid}; nothing is written")
        verses = _verse_lines(conn, cfg, L, refs, gid)
    for part in sg.chunks(taken, cfg):
        conn.execute(f"UPDATE collection_layer_item SET pulled_at={lr.NOW}, updated_at={lr.NOW} WHERE id IN ({','.join('?' * len(part))})", part)
    left = (len(fresh) if fresh else len(todo)) - len(out_rows)      # the open rows not yet in any package after this one
    pkg = {"command": "ReadStructure", "collection": L["name"], "subgroup": gname, "step": step, "item": first,
           "made": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "batch": {"rows": len(out_rows), "rows_left_after_this": left},
           "instruction": ins, "senses": senses, "verses": verses, "rows": out_rows,
           "answer": {"command": "ReadStructure", "collection": L["name"], "subgroup": gname,
                      "rows": [_structure_answer_row(x, s) for x in out_rows]}}
    secs = round(time.monotonic() - t0, 2)
    chars = len(json.dumps(pkg, ensure_ascii=False))
    pkg["measured"] = {"package_chars": chars, "seconds": secs}
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"readstructure-{_slug(L['name'])}-{_slug(gname)}-{_slug(first)}-{datetime.datetime.now().strftime('%Y%m%dt%H%M%S')}.json"
    path.write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"path": path, "item": first, "rows": len(out_rows), "left": left, "verses": len(verses), "chars": chars, "seconds": secs, "opened": opened}


def record_structure(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check a filled ReadStructure answer whole and write it through the recorder (each finding's occurrences, exactly the row's demanded occurrences where the item asks for all of them,
    the text rules, traces to the 1.1 senses, a none with its reason where the item allows it, RW-13); validate the subgroup's rows and name the next command. keep=False previews."""
    rt = settings(cfg)["structure"]
    s = lr.settings(cfg)
    step = rt["step"]
    if data.get("command") != "ReadStructure":
        raise ReadError("this is not a ReadStructure answer (its `command` must be ReadStructure; fill the `answer` part of the package)")
    name, sub = str(data.get("collection") or ""), str(data.get("subgroup") or "")
    cid, gid, gname = _subgroup(conn, name, sub)
    mine = {r[0]: r for r in lr._rows(conn, cid, step) if r[4] == gid and r[3] in STRUCTURE_ITEMS and r[6] != "retired"}
    errors, rows = [], []
    for i, row in enumerate(data.get("rows") or [], 1):
        lid = row.get("ledger_id")
        if lid not in mine:
            errors.append(f"row {i}: ledger {lid} is not a 2.1 row of subgroup {gname!r}")
            continue
        idef = s["items"][mine[lid][3]]
        disp = (row.get("disposition") or "").strip()
        if disp not in ("observed", "none"):
            errors.append(f"row {i} (ledger {lid}): disposition must be observed or none")
            continue
        fill = {"disposition": disp, "member_role": idef["member_role"], "partner_role": idef.get("partner_role", ""), "reason": row.get("reason") or "", "older": row.get("older") or []}
        if disp == "observed":
            fill["senses"] = row.get("findings") or []
        rows.append({"ledger_id": lid, "fill": fill})
    if not rows and not errors:
        errors.append("the answer holds no row")
    if errors:
        raise ReadError("the answer is refused whole, nothing written:\n  " + "\n  ".join(errors))
    try:
        r = lr.record(conn, cfg, run_id, {"collection": name, "step": step, "subgroup": gname, "rows": rows}, keep)
    except lr.LayerError as exc:
        raise ReadError(str(exc))
    out = {"observed": r["observed"], "nodes": r["nodes"], "rows": len(rows)}
    if not keep:
        return {**out, "preview": True}
    lr.check(conn, cfg, run_id, name, subgroup=gname)
    after = {x[0]: x for x in lr._rows(conn, cid, step)}
    failed = [f"{after[x['ledger_id']][3]} {after[x['ledger_id']][5]}".strip() + f" ({after[x['ledger_id']][8]})" for x in rows if not after[x["ledger_id"]][9]]
    left = sum(1 for x in after.values() if x[4] == gid and x[3] in STRUCTURE_ITEMS and x[6] == "open")
    return {**out, "validated": len(rows) - len(failed), "failed": failed, "rows_open": left, "next": next_after_structure(conn, cid, gid, name, gname, step)}


# ══ the gate rows of step 2.1: the sweep (B4) and the evidence validation (B5) ═══════════════════════════════════════════════════════════
# Both are ledger-only items of step 2.1, one row for each subgroup (cfg_setting layer.reading items sweep and evidence-validation): step 2.1 closes only when both are answered
# and validated, so 3.1 (which needs 2.1 closed) waits for them, and LayerNext names them. Their readiness and their validation are judged here from the tables.

SWEEP_ITEM, EVIDENCE_ITEM = "sweep", "evidence-validation"
GATE_ITEMS = (SWEEP_ITEM, EVIDENCE_ITEM)


def _ids_in(conn, sql: str, ids, cfg, extra: tuple = ()) -> list:
    out = []
    for part in sg.chunks(sorted(set(ids)), cfg):
        out += conn.execute(sql.replace("{ids}", ",".join("?" * len(part))), list(extra) + list(part)).fetchall()
    return out


def _gate_row(conn, cid: int, gid: int, item: str):
    return next((r for r in lr._rows(conn, cid, "2.1") if r[4] == gid and r[3] == item and r[6] != "retired"), None)


def _structure_done(conn, cid: int, gid: int) -> list:
    """The 2.1 rows of the subgroup not yet answered and validated (the items read by ReadStructure)."""
    return [r for r in lr._rows(conn, cid, "2.1") if r[4] == gid and r[3] in STRUCTURE_ITEMS and r[6] != "retired" and not (r[6] in ("observed", "none") and r[9])]


def _open_gate_rows(conn, cfg, run_id: str, name: str, gname: str, cid: int, gid: int) -> None:
    """The gate rows are made by opening 2.1 for the subgroup again (the order gate applies; nothing answered is touched)."""
    if _gate_row(conn, cid, gid, SWEEP_ITEM) is None or _gate_row(conn, cid, gid, EVIDENCE_ITEM) is None:
        lr.open_step(conn, cfg, run_id, name, "2.1", subgroup=gname)


def sweep_candidates(conn, cfg, s: dict, L: dict, cid: int, gid: int) -> dict:
    """{observation id: {...}}: every observation of the subgroup's scope still unmarked after B1 to B3 -- the older ones on its occurrences (buildvalidate.unmarked_in), any other unmarked
    observation of the scope the evidence validation reads (evidence_scope; for example the build observations of a group the regrouping deleted, whose rows were never retired, found on
    thought 2026-11-26), and those carried to the sweep whose ledger row is open. The same scope as the evidence checks, so the two never disagree."""
    out = dict(lr.unmarked_of(conn, cfg, s, L, gid))
    for oid, o in evidence_scope(conn, cfg, L, cid, gid)["obs"].items():
        if o["nature"] is None and oid not in out:
            out[oid] = {"observation": oid, "stage": o["stage"], "tag": o["kind"], "nature": None, "text": o["text"]}
    for (subj,) in conn.execute("SELECT subject FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND item=? AND step='sweep' AND state='open' AND deleted=0", (cid, gid, lr.bv.OLD_ITEM)):
        if str(subj).isdigit() and int(subj) not in out:
            o_ = conn.execute("SELECT id, stage, tag, nature, obs_text FROM ib_observation WHERE id=? AND deleted=0", (int(subj),)).fetchone()
            if o_:
                out[o_[0]] = {"observation": o_[0], "stage": o_[1], "tag": o_[2], "nature": o_[3], "text": o_[4] or "", "carried_to_sweep": True}
    return out


def read_sweep(conn, cfg, run_id: str, name: str, subgroup: str, out_dir: pathlib.Path) -> dict:
    """The sweep (B4) of one subgroup: the package of its older observations still unmarked, each to be judged by content. Refused while a 2.1 row of the subgroup is not answered and
    validated. When nothing is left to sweep, the sweep row is answered as such from the tables and validated, and the next command is named."""
    t0 = time.monotonic()
    st = settings(cfg)
    rt, lim = st["sweep"], st["limits"]
    s = lr.settings(cfg)
    cid, gid, gname = _subgroup(conn, name, subgroup)
    _open_gate_rows(conn, cfg, run_id, name, gname, cid, gid)
    left = _structure_done(conn, cid, gid)
    if left:
        raise ReadError(f"the sweep of {gname!r} comes after its 2.1 rows: {len(left)} row(s) are not answered and validated; next: " + next_after_structure(conn, cid, gid, name, gname, "2.1"))
    row = _gate_row(conn, cid, gid, SWEEP_ITEM)
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    with sg.budget(conn, cfg, "ReadSweep"):
        cands = sweep_candidates(conn, cfg, s, L, cid, gid)
    if not cands:
        if not (row[6] == "observed" and row[9]):
            conn.execute(f"UPDATE collection_layer_item SET state='observed', answered_at={lr.NOW}, reason=?, updated_at={lr.NOW}, run_id=? WHERE id=?",
                         ("swept: no older observation on the subgroup's occurrences is left unmarked after B1 to B3, and none is carried to the sweep", run_id, row[0]))
            lr.check(conn, cfg, run_id, name, subgroup=gname)
        raise ReadError(f"the sweep of {gname!r} has nothing to read: no older observation is left unmarked; the sweep row is answered as such. Next: "
                        + next_after_gate(conn, cid, gid, name, gname))
    occ = {o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid}
    olds = []
    for oid in sorted(cands):
        c = cands[oid]
        nodes = conn.execute("SELECT n.verse_reference, n.verse_lexical_id, n.collection_id, c.name FROM ib_node n LEFT JOIN collection c ON c.id=n.collection_id "
                             "WHERE n.observation_id=? AND n.deleted=0 AND n.traced_observation_id IS NULL", (oid,)).fetchall()
        olds.append({"observation": oid, "stage": c.get("stage"), "kind": c.get("tag"), "text": c.get("text"), "verses": sorted({n[0] for n in nodes if n[0]}),
                     "nodes_here": sum(1 for n in nodes if n[1] in occ), "nodes_elsewhere": sum(1 for n in nodes if n[1] not in occ),
                     "collections": sorted({n[3] for n in nodes if n[3]}), **({"carried_to_sweep": True} if c.get("carried_to_sweep") else {})})
    conn.execute(f"UPDATE collection_layer_item SET pulled_at={lr.NOW}, updated_at={lr.NOW} WHERE id=?", (row[0],))
    pkg = {"command": "ReadSweep", "collection": L["name"], "subgroup": gname, "step": "2.1", "item": SWEEP_ITEM,
           "made": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "instruction": instruction(conn, rt), "older": olds,
           "answer": {"command": "ReadSweep", "collection": L["name"], "subgroup": gname,
                      "older": [{"observation": o["observation"], "action": "keep | delete_neither | defer", "nature": "evidence | inner_being", "reason": ""} for o in olds]}}
    secs = round(time.monotonic() - t0, 2)
    chars = len(json.dumps(pkg, ensure_ascii=False))
    pkg["measured"] = {"package_chars": chars, "seconds": secs}
    if secs > lim["read_max_seconds"]:
        raise ReadError(f"ReadSweep for {gname!r} took {secs} s, more than {lim['read_max_seconds']} s; nothing is written")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"readsweep-{_slug(L['name'])}-{_slug(gname)}-{datetime.datetime.now().strftime('%Y%m%dt%H%M%S')}.json"
    path.write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"path": path, "older": len(olds), "chars": chars, "seconds": secs}


def record_sweep(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check a filled ReadSweep answer whole and write it in one transaction: each older observation of the package answered once, keep (marked evidence or inner_being), delete_neither
    (comment first, its nodes here go; an observation held elsewhere loses only these) or defer (marked, deferred to a named collection). Then the sweep row is answered and validated."""
    st = settings(cfg)["sweep"]
    s = lr.settings(cfg)
    if data.get("command") != "ReadSweep":
        raise ReadError("this is not a ReadSweep answer (its `command` must be ReadSweep; fill the `answer` part of the package)")
    name, sub = str(data.get("collection") or ""), str(data.get("subgroup") or "")
    cid, gid, gname = _subgroup(conn, name, sub)
    row = _gate_row(conn, cid, gid, SWEEP_ITEM)
    if row is None:
        raise ReadError(f"subgroup {gname!r} has no sweep row: run ReadSweep first")
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    cands = sweep_candidates(conn, cfg, s, L, cid, gid)
    home = (cid, {o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid})
    errors, seen = [], set()
    answers = data.get("older") or []
    for i, a in enumerate(answers, 1):
        oid = a.get("observation")
        if oid in seen:
            errors.append(f"older {i}: observation {oid} is answered twice")
        seen.add(oid)
        if oid not in cands:
            errors.append(f"older {i}: observation {oid} is not an unmarked older observation of {gname!r} (read the sweep again)")
        if a.get("action") not in st["actions"]:
            errors.append(f"older {i} (observation {oid}): the sweep answers with one of {st['actions']}")
        if len((a.get("reason") or "").strip()) < 20:
            errors.append(f"older {i} (observation {oid}): the reason says, in words, what the observation states and why it is so judged (20 characters or more)")
    missing = sorted(set(cands) - seen)
    if missing:
        errors.append(f"{len(missing)} unmarked older observation(s) have no answer (for example {missing[:5]}): the sweep answers every one")
    if errors:
        raise ReadError("the answer is refused whole, nothing written:\n  " + "\n  ".join(errors))
    conn.execute("SAVEPOINT read_sweep")
    try:
        for a in answers:
            if isinstance(a.get("uncarried"), dict):      # a JSON answer names occurrences as strings; the consumption compares occurrence ids
                a = {**a, "uncarried": {int(k): v for k, v in a["uncarried"].items()}}
            lr.bv._answer(cfg, conn, a["observation"], a, [], run_id, s, home=home, step="sweep")
            for (lid_,) in conn.execute("SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND item=? AND subject=? AND state='open' AND deleted=0",
                                        (cid, gid, lr.bv.OLD_ITEM, str(a["observation"]))).fetchall():
                conn.execute(f"UPDATE collection_layer_item SET state='observed', answered_at={lr.NOW}, reason=?, updated_at={lr.NOW}, run_id=? WHERE id=?",
                             (f"{a['action']}: {a['reason']}", run_id, lid_))
        conn.execute(f"UPDATE collection_layer_item SET state='observed', answered_at={lr.NOW}, reason=?, updated_at={lr.NOW}, run_id=? WHERE id=?",
                     (f"swept: {len(answers)} older observation(s) answered by content", run_id, row[0]))
        left = sweep_candidates(conn, cfg, s, L, cid, gid)
        if left:
            raise ReadError(f"after the answers {len(left)} older observation(s) are still unmarked (for example {sorted(left)[:5]}); nothing written")
    except (lr.bv.va.Refused, lr.bv.orec.Refused) as exc:
        conn.execute("ROLLBACK TO read_sweep")
        conn.execute("RELEASE read_sweep")
        raise ReadError(f"the answer is refused whole, nothing written: {exc}")
    except Exception:
        conn.execute("ROLLBACK TO read_sweep")
        conn.execute("RELEASE read_sweep")
        raise
    if not keep:
        conn.execute("ROLLBACK TO read_sweep")
        conn.execute("RELEASE read_sweep")
        return {"answered": len(answers), "preview": True}
    conn.execute("RELEASE read_sweep")
    lr.check(conn, cfg, run_id, name, subgroup=gname)
    r2 = _gate_row(conn, cid, gid, SWEEP_ITEM)
    return {"answered": len(answers), "validated": bool(r2[9]), "reason": r2[8], "next": next_after_gate(conn, cid, gid, name, gname)}


def sweep_ok(conn, cfg, s: dict, L: dict, cid: int, gid: int) -> str | None:
    """None when the sweep of the subgroup holds (LayerCheck validates the sweep row by this); else why not."""
    left = sweep_candidates(conn, cfg, s, L, cid, gid)
    return None if not left else f"{len(left)} older observation(s) are still unmarked on the subgroup's occurrences (for example {sorted(left)[:5]}): run ReadSweep"


# ── the evidence validation (B5) ──

def evidence_scope(conn, cfg, L: dict, cid: int, gid: int) -> dict:
    """The observations of the subgroup (specification v5, 1A and B5): its own (the observations of its ledger rows of S1 to 2.1, by step) and the older ones with a live word node on
    its occurrences. {observation id: {"step": step or None, "item": item or None, "nature": ..., ...}}. Indexed lookups in chunks."""
    out: dict = {}
    for lid, step, item in conn.execute("SELECT id, step, item FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND deleted=0 AND state!='retired' AND step IN ('S1','1.1','1.2','2.1') "
                                        "AND item NOT IN (?,?,?)", (cid, gid, lr.bv.OLD_ITEM, SWEEP_ITEM, EVIDENCE_ITEM)).fetchall():
        for (oid,) in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};")):
            out[oid] = {"step": step, "item": item}
    occ = [o["vl_id"] for o in L["d"]["occurrences"] if o["group"] == gid]
    for (oid,) in _ids_in(conn, "SELECT DISTINCT n.observation_id FROM ib_node n WHERE n.deleted=0 AND n.traced_observation_id IS NULL AND n.verse_lexical_id IN ({ids})", occ, cfg):
        out.setdefault(oid, {"step": None, "item": None})
    for r in _ids_in(conn, "SELECT id, stage, tag, nature, obs_text, basis, parts, deleted FROM ib_observation WHERE id IN ({ids})", list(out), cfg):
        if r[7]:
            out.pop(r[0], None)
            continue
        out[r[0]].update({"stage": r[1], "kind": r[2], "nature": r[3], "text": r[4] or "", "basis": r[5], "grounds": (json.loads(r[6]) if r[6] else {}).get("grounds")})
    return {"occ": occ, "obs": {k: v for k, v in out.items() if "stage" in v}}


def evidence_check(conn, cfg, L: dict, cid: int, gid: int, scope: dict | None = None) -> dict:
    """The code checks of the evidence validation of one subgroup (B5; VA-06, evidence layer only; inner being is not judged here): every observation marked; none without a live node;
    no word node missing a required column without its reason; no live trace to a deleted observation; no two of one text; every B1 observation traced by a sense; every sense traced
    by the 2.1 observations that stand on its occurrences, where there are any; no older observation of the subgroup left open in the ledger. {check: [ids]}; empty lists pass."""
    sc = scope or evidence_scope(conn, cfg, L, cid, gid)
    obs, occ = sc["obs"], set(sc["occ"])
    vr = cfg.required_setting("validate.reading")
    cols = (json.loads(vr) if isinstance(vr, str) else vr)["word_columns"]
    f = {k: [] for k in ("unmarked", "no_node", "word_missing", "traced_dead", "duplicate_text", "b1_not_traced_by_a_sense", "sense_not_traced_by_2_1", "older_open")}
    nodes: dict = {}
    for r in _ids_in(conn, f"SELECT id, observation_id, traced_observation_id, verse_lexical_id, disposition_note, {', '.join(cols)} FROM ib_node WHERE deleted=0 AND observation_id IN ({{ids}})", list(obs), cfg):
        nodes.setdefault(r[1], []).append(r)
    targets = {n[2] for ns in nodes.values() for n in ns if n[2] is not None}
    live = {r[0]: r[1] == 0 for r in _ids_in(conn, "SELECT id, deleted FROM ib_observation WHERE id IN ({ids})", targets, cfg)}
    texts: dict = {}
    for oid, o in obs.items():
        if o["nature"] is None:
            f["unmarked"].append(oid)
        ns = nodes.get(oid, [])
        if not ns:
            f["no_node"].append(oid)
        for n in ns:
            if n[2] is not None and n[3] is None:
                if not live.get(n[2], False) and o["nature"] != "inner_being":      # an inner-being observation's traces are the inner-being layer's (IB-07, C4), not judged here (VA-06)
                    f["traced_dead"].append(oid)
                continue
            if (o["step"] or n[3] in occ) and any(v is None for v in n[5:]) and not n[4]:
                f["word_missing"].append(oid)
        if o["nature"] == "evidence" and o["text"]:
            texts.setdefault((o["stage"], " ".join(o["text"].split()).lower()), []).append(oid)
    f["duplicate_text"] = [v for v in texts.values() if len(v) > 1]
    traces = {oid: {n[2] for n in nodes.get(oid, []) if n[2] is not None and n[3] is None} for oid in obs}
    words = {oid: {n[3] for n in nodes.get(oid, []) if n[3] is not None and n[2] is None} for oid in obs}
    b1 = [o for o, v in obs.items() if v["step"] == "S1"]
    senses = [o for o, v in obs.items() if v["step"] == "1.1"]
    b3 = [o for o, v in obs.items() if v["step"] == "2.1"]
    by_sense = set().union(*[traces[x] for x in senses]) if senses else set()
    f["b1_not_traced_by_a_sense"] = [o for o in b1 if o not in by_sense]
    for x in senses:
        stand = [y for y in b3 if words[y] & words[x]]
        if stand and not any(x in traces[y] for y in stand):
            f["sense_not_traced_by_2_1"].append(x)
    f["older_open"] = [int(r[0]) for r in conn.execute("SELECT subject FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND item=? AND state='open' AND deleted=0",
                                                       (cid, gid, lr.bv.OLD_ITEM)) if str(r[0]).isdigit()]
    f = {k: sorted(set(v)) if k != "duplicate_text" else v for k, v in f.items()}
    return {"findings": f, "passes": not any(f.values()), "observations": len(obs), "evidence": sum(1 for v in obs.values() if v["nature"] == "evidence")}


def evidence_read(conn, cfg, ids) -> set:
    """The observations of `ids` whose truth and coherence a reading has recorded in the evidence validation (column evidence_read of ib_observation_change)."""
    return {r[0] for r in _ids_in(conn, "SELECT DISTINCT observation_id FROM ib_observation_change WHERE column_name='evidence_read' AND observation_id IN ({ids})", ids, cfg)}


def evidence_ok(conn, cfg, L: dict, cid: int, gid: int) -> str | None:
    """None when the evidence validation of the subgroup holds (LayerCheck validates the evidence-validation row by this): the code checks pass and every evidence observation of the
    subgroup is read; else why not."""
    sc = evidence_scope(conn, cfg, L, cid, gid)
    chk = evidence_check(conn, cfg, L, cid, gid, sc)
    if not chk["passes"]:
        return "the code checks do not pass: " + "; ".join(f"{k} {len(v)}" for k, v in chk["findings"].items() if v)
    ev = [o for o, v in sc["obs"].items() if v["nature"] == "evidence"]
    unread = sorted(set(ev) - evidence_read(conn, cfg, ev))
    return None if not unread else f"{len(unread)} evidence observation(s) not yet read for truth and coherence (for example {unread[:5]}): run ReadEvidence"


def _verses_of(conn, cfg, oids) -> tuple[dict, list]:
    """({observation: [references]}, [{reference, text}]) for the live word nodes of the observations (by verse_lexical_id, or by the osis reference of an older node without one), the verses once."""
    by_vl, by_osis = {}, {}
    for oid, vlid, ref in _ids_in(conn, "SELECT observation_id, verse_lexical_id, verse_reference FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND observation_id IN ({ids})", oids, cfg):
        if vlid is not None:
            by_vl.setdefault(vlid, set()).add(oid)
        elif ref:
            by_osis.setdefault(ref, set()).add(oid)
    holders: dict = {}
    for vlid, vid in _ids_in(conn, "SELECT id, verse_id FROM verse_lexical WHERE id IN ({ids})", list(by_vl), cfg):
        holders.setdefault(vid, set()).update(by_vl[vlid])
    for vid, osis in _ids_in(conn, "SELECT id, osisId FROM verse WHERE deleted=0 AND osisId IN ({ids})", list(by_osis), cfg):
        holders.setdefault(vid, set()).update(by_osis[osis])
    refs, verses = {}, []
    for vid, ref, text, osis in sorted((tuple(x) for x in _ids_in(conn, "SELECT id, reference, text, osisId FROM verse WHERE id IN ({ids})", list(holders), cfg)), key=lambda x: x[0]):
        verses.append({"reference": ref or osis, "text": text or ""})
        for oid in holders[vid]:
            refs.setdefault(oid, []).append(ref or osis)
    return refs, verses


def read_evidence(conn, cfg, run_id: str, name: str, subgroup: str, out_dir: pathlib.Path) -> dict:
    """The evidence validation (B5) of one subgroup: the code checks, and the package of the next evidence observations of the subgroup not yet read, in the order of the steps, each with its
    text, basis, grounds, verses and the observations it traces; the verses once. Refused while the sweep of the subgroup is not answered and validated."""
    t0 = time.monotonic()
    st = settings(cfg)
    rt, lim = st["evidence"], st["limits"]
    cid, gid, gname = _subgroup(conn, name, subgroup)
    _open_gate_rows(conn, cfg, run_id, name, gname, cid, gid)
    sw = _gate_row(conn, cid, gid, SWEEP_ITEM)
    if not (sw[6] == "observed" and sw[9]):
        raise ReadError(f"the evidence validation of {gname!r} comes after its sweep; next: " + next_after_gate(conn, cid, gid, name, gname))
    row = _gate_row(conn, cid, gid, EVIDENCE_ITEM)
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    with sg.budget(conn, cfg, "ReadEvidence"):
        sc = evidence_scope(conn, cfg, L, cid, gid)
        from . import validationactions as va      # a trace to a deleted observation supports nothing: released before the checks, so it never holds the gate (#2618)
        va.release_dead_traces(conn, run_id, "Claude", list(sc["obs"]))
        chk = evidence_check(conn, cfg, L, cid, gid, sc)
        ev = [o for o, v in sc["obs"].items() if v["nature"] == "evidence"]
        unread = sorted(set(ev) - evidence_read(conn, cfg, ev), key=lambda o: (["S1", "1.1", "1.2", "2.1", None].index(sc["obs"][o]["step"]), o))
    if not unread:
        if chk["passes"] and not (row[6] == "observed" and row[9]):
            conn.execute(f"UPDATE collection_layer_item SET state='observed', answered_at={lr.NOW}, reason=?, updated_at={lr.NOW}, run_id=? WHERE id=?",
                         (f"validated: the code checks pass and all {len(ev)} evidence observations are read", run_id, row[0]))
            lr.check(conn, cfg, run_id, name, subgroup=gname)
        what = "every evidence observation is read" + ("" if chk["passes"] else "; the code checks do NOT pass: " + "; ".join(f"{k} {v[:5]}" for k, v in chk["findings"].items() if v))
        raise ReadError(f"the evidence validation of {gname!r}: {what}. Next: " + next_after_gate(conn, cid, gid, name, gname))
    traced = {}
    for r in _ids_in(conn, "SELECT observation_id, traced_observation_id FROM ib_node WHERE deleted=0 AND traced_observation_id IS NOT NULL AND observation_id IN ({ids})", unread, cfg):
        traced.setdefault(r[0], []).append(r[1])
    batch, size = [], 0
    for oid in unread:
        if len(batch) >= rt["batch_observations"]:
            break
        o = sc["obs"][oid]
        x = {"observation": oid, "step": o["step"] or f"older ({o['stage']})", "item": o["item"], "kind": o["kind"], "text": o["text"], "basis": o["basis"], "grounds": o["grounds"],
             "traces": sorted(traced.get(oid, []))}
        n = len(json.dumps(x, ensure_ascii=False)) + 300
        if batch and size + n > rt["package_max_chars"]:
            break
        batch.append(x)
        size += n
    refs, verses = _verses_of(conn, cfg, [x["observation"] for x in batch])
    for x in batch:
        x["verses"] = sorted(set(refs.get(x["observation"], [])))
    conn.execute(f"UPDATE collection_layer_item SET pulled_at={lr.NOW}, updated_at={lr.NOW} WHERE id=?", (row[0],))
    pkg = {"command": "ReadEvidence", "collection": L["name"], "subgroup": gname, "step": "2.1", "item": EVIDENCE_ITEM,
           "made": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "batch": {"observations": len(batch), "left_after_this": len(unread) - len(batch), "evidence_in_scope": len(ev), "observations_in_scope": chk["observations"]},
           "code_checks": {"passes": chk["passes"], "findings": chk["findings"]},
           "instruction": instruction(conn, rt), "observations": batch, "verses": verses,
           "answer": {"command": "ReadEvidence", "collection": L["name"], "subgroup": gname,
                      "observations": [{"observation": x["observation"], "verdict": "true | repair", "why": "", "actions": []} for x in batch]}}
    secs = round(time.monotonic() - t0, 2)
    chars = len(json.dumps(pkg, ensure_ascii=False))
    pkg["measured"] = {"package_chars": chars, "seconds": secs}
    if secs > lim["read_max_seconds"]:
        raise ReadError(f"ReadEvidence for {gname!r} took {secs} s, more than {lim['read_max_seconds']} s; nothing is written")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"readevidence-{_slug(L['name'])}-{_slug(gname)}-{datetime.datetime.now().strftime('%Y%m%dt%H%M%S')}.json"
    path.write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"path": path, "observations": len(batch), "left": len(unread) - len(batch), "passes": chk["passes"], "chars": chars, "seconds": secs}


def record_evidence(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check a filled ReadEvidence answer whole and write it in one transaction: each observation of the answer is an evidence observation of the subgroup, answered once, `true` (with
    `why`: what in the verses and the data bears it out) or `repair` (with `why` and the `actions` of the validation that repair it, cfg_setting validate.reading actions). The repairs are
    written through collectionvalidate.record; each observation answered is logged as read (evidence_read). When every evidence observation is read and the code checks pass, the
    evidence-validation row is answered and validated."""
    from . import collectionvalidate as cv
    from . import observationrecord as orec
    if data.get("command") != "ReadEvidence":
        raise ReadError("this is not a ReadEvidence answer (its `command` must be ReadEvidence; fill the `answer` part of the package)")
    name, sub = str(data.get("collection") or ""), str(data.get("subgroup") or "")
    cid, gid, gname = _subgroup(conn, name, sub)
    row = _gate_row(conn, cid, gid, EVIDENCE_ITEM)
    if row is None:
        raise ReadError(f"subgroup {gname!r} has no evidence-validation row: run ReadEvidence first")
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    sc = evidence_scope(conn, cfg, L, cid, gid)
    ev = {o for o, v in sc["obs"].items() if v["nature"] == "evidence"}
    errors, seen, actions = [], set(), []
    items = data.get("observations") or []
    for i, a in enumerate(items, 1):
        oid, verdict, why = a.get("observation"), a.get("verdict"), (a.get("why") or "").strip()
        where = f"observation {i} ({oid})"
        if oid in seen:
            errors.append(f"{where}: answered twice")
        seen.add(oid)
        if oid not in ev:
            errors.append(f"{where}: not an evidence observation of {gname!r}")
        if verdict not in ("true", "repair"):
            errors.append(f"{where}: verdict is true or repair")
        if len(why) < 20:
            errors.append(f"{where}: why says, in words, what in the verses and the data bears it out or what is wrong (20 characters or more)")
        if verdict == "repair" and not a.get("actions"):
            errors.append(f"{where}: a repair names the actions of the validation that make it true")
        if verdict == "true" and a.get("actions"):
            errors.append(f"{where}: a true observation takes no action")
        actions += a.get("actions") or []
    if not items:
        errors.append("the answer holds no observation")
    if errors:
        raise ReadError("the answer is refused whole, nothing written:\n  " + "\n  ".join(errors))
    conn.execute("SAVEPOINT read_evidence")
    try:
        repaired = {}
        if actions:
            repaired = cv.record(conn, cfg, run_id, {"collection": name, "actions": actions}, keep=True)
        for a in items:
            orec.log(conn, a["observation"], None, "evidence_read", None, a["verdict"], a["why"], None, run_id, lr.bv.WHO)
        chk = evidence_check(conn, cfg, L, cid, gid)
        ev2 = [o for o, v in evidence_scope(conn, cfg, L, cid, gid)["obs"].items() if v["nature"] == "evidence"]
        left = sorted(set(ev2) - evidence_read(conn, cfg, ev2))
        if not left and chk["passes"]:
            conn.execute(f"UPDATE collection_layer_item SET state='observed', answered_at={lr.NOW}, reason=?, updated_at={lr.NOW}, run_id=? WHERE id=?",
                         (f"validated: the code checks pass and all {len(ev2)} evidence observations are read", run_id, row[0]))
    except (cv.ValidateError, orec.Refused) as exc:
        conn.execute("ROLLBACK TO read_evidence")
        conn.execute("RELEASE read_evidence")
        raise ReadError(f"the answer is refused whole, nothing written: {exc}")
    except Exception:
        conn.execute("ROLLBACK TO read_evidence")
        conn.execute("RELEASE read_evidence")
        raise
    out = {"read": len(items), "repairs": sum(1 for a in items if a["verdict"] == "repair"), "actions": len(actions), "left": len(left), "checks_pass": chk["passes"],
           "failing": {k: v[:5] for k, v in chk["findings"].items() if v}}
    if not keep:
        conn.execute("ROLLBACK TO read_evidence")
        conn.execute("RELEASE read_evidence")
        return {**out, "preview": True}
    conn.execute("RELEASE read_evidence")
    lr.check(conn, cfg, run_id, name, subgroup=gname)
    r2 = _gate_row(conn, cid, gid, EVIDENCE_ITEM)
    return {**out, "validated": bool(r2[9]), "next": next_after_gate(conn, cid, gid, name, gname)}


def next_after_gate(conn, cid: int, gid: int, name: str, gname: str) -> str:
    """The next command at the end of step 2.1: ReadSweep until the sweep row is validated, then ReadEvidence until the evidence-validation row is, then step 3.1 of the subgroup."""
    cmd = f".\\iba\\app\\ps\\Collection-Build.ps1 -Collection {name} -Subgroup '{gname}'"
    sw, ev = _gate_row(conn, cid, gid, SWEEP_ITEM), _gate_row(conn, cid, gid, EVIDENCE_ITEM)
    if sw is None or not (sw[6] == "observed" and sw[9]):
        return f"{cmd} -Action ReadSweep"
    if ev is None or not (ev[6] == "observed" and ev[9]):
        return f"{cmd} -Action ReadEvidence"
    return f"{cmd} -Action ReadElements  (step 2.1 is closed for the subgroup: step 3.1 is next)"


# ══ ReadElements / RecordElements: step 3.1, the elements of one subgroup (stage 4, C1) ═══════════════════════════════════════════

ELEMENTS_ITEM = "subgroup-analysis"


def next_after_elements(conn, cfg, name: str, gname: str) -> str:
    return (f".\\iba\\app\\ps\\Collection-Build.ps1 -Action LayerNext -Collection {name}  (the loop of {gname!r} is complete once 3.1 is validated: LayerNext names the next subgroup, "
            f"or 3.2 when every subgroup is through 3.1)")


def _elements_row(conn, cid: int, gid: int):
    return next((r for r in lr._rows(conn, cid, "3.1") if r[4] == gid and r[3] == ELEMENTS_ITEM and r[6] != "retired"), None)


def _earlier_readings(conn, cfg, cid: int, gid: int, vls, stages: list) -> list:
    """The inner-being observations of the build stages on the subgroup's occurrences that are not the subgroup's own (an earlier reading of a group the regrouping replaced, kept as inner
    being by the sweep): RW-13 answers only older observations of other stages, so these are answered in the record's `existing` (accept, modify, delete, merge, leave)."""
    own = set()
    for lid, in conn.execute("SELECT id FROM collection_layer_item WHERE collection_id=? AND subgroup_id=? AND deleted=0 AND state!='retired'", (cid, gid)).fetchall():
        own |= {r[0] for r in conn.execute("SELECT id FROM ib_observation WHERE stable_key >= ? AND stable_key < ? AND deleted=0", (f"layer:{lid}:", f"layer:{lid};"))}
    out, seen = [], set()
    for part in sg.chunks(sorted(vls), cfg):
        for r2 in conn.execute(f"SELECT DISTINCT o.id, o.stage, o.tag, o.obs_text FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 "
                               f"AND o.nature='inner_being' AND o.stage IN ({','.join('?' * len(stages))}) AND n.verse_lexical_id IN ({','.join('?' * len(part))})", stages + part):
            if r2[0] not in seen and r2[0] not in own:
                seen.add(r2[0])
                out.append({"observation": r2[0], "stage": r2[1], "kind": r2[2], "text": r2[3] or ""})
    return sorted(out, key=lambda x: x["observation"])


def read_elements(conn, cfg, run_id: str, name: str, subgroup: str, out_dir: pathlib.Path) -> dict:
    """The package of step 3.1 of one subgroup (C1): the evidence observations of the subgroup to take up (by marker, the senses first; layerinner._sources), those it may rest on
    besides, the older inner-being observations on its occurrences to answer, its definition, the meaning by code, every verse of the subgroup with its text, the items a finding may
    use with their kinds, and the answer. One package for the subgroup: a 3.1 row is recorded whole (every observation taken up is rested on or declared not used). Opens 3.1 for the
    subgroup if it is not open (2.1 closed with its gates, the order gate, the evidence gate of 3.1)."""
    from . import layerinner as li
    t0 = time.monotonic()
    st = settings(cfg)
    rt, lim = st["elements"], st["limits"]
    s = lr.settings(cfg)
    cid, gid, gname = _subgroup(conn, name, subgroup)
    row = _elements_row(conn, cid, gid)
    opened = None
    if row is None:
        opened = lr.open_step(conn, cfg, run_id, name, "3.1", subgroup=gname)
        row = _elements_row(conn, cid, gid)
    if row is None:
        raise ReadError(f"step 3.1 has no row for {gname!r}: the subgroup has no evidence observation on its occurrences")
    if row[6] in ("observed", "none") and row[9]:
        raise ReadError(f"the elements of {gname!r} are read and validated; next: " + next_after_elements(conn, cfg, name, gname))
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    sd = lr.step_def(s, "3.1")
    idef = s["items"][ELEMENTS_ITEM]
    with sg.budget(conn, cfg, "ReadElements"):
        dem = li.demanded(L, ELEMENTS_ITEM, gid, "", conn)
        sources, required = li._sources(conn, s, L, sd, gid, "")
        order = {s["stages"]["1"]: 0, s["stages"]["2"]: 1, s["stages"]["0"]: 2}
        take = sorted((li._obs_line(conn, i) for i in required), key=lambda x: (order.get(x["stage"], 3), x["observation"]))
        besides = sorted((li._obs_line(conn, i) for i in sources - required), key=lambda x: (order.get(x["stage"], 3), x["observation"]))
        older = []
        stages = sorted(set(s["stages"].values()))
        seen = set()
        for part in sg.chunks(sorted(li._allowed(dem)), cfg):
            for r2 in conn.execute(f"SELECT DISTINCT o.id, o.stage, o.tag, o.obs_text FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.deleted=0 AND n.deleted=0 "
                                   f"AND o.nature='inner_being' AND o.stage NOT IN ({','.join('?' * len(stages))}) AND n.verse_lexical_id IN ({','.join('?' * len(part))})", stages + part):
                if r2[0] not in seen:
                    seen.add(r2[0])
                    older.append({"observation": r2[0], "stage": r2[1], "kind": r2[2], "text": r2[3] or ""})
        answered = lr.bv.settled(conn, cfg, [o["observation"] for o in older]) | lr.bv.carried_later(conn, [o["observation"] for o in older], "3.1")
        for o in older:      # one answered at an earlier step is shown for the reading (IB-05) and answered again only if a finding changes it
            o["answered_before"] = o["observation"] in answered
        earlier = _earlier_readings(conn, cfg, cid, gid, li._allowed(dem), stages)
        verses = [{"reference": osis, "text": text} for osis, text in sorted(li._texts(conn, dem).items())]
        meaning = {}      # the head sense and the meaning range of each code, cut to lexicon_chars: the full lexicon is read at 1.2, whose enrichments 3.1 takes up (#2538: the whole lexicon was 301,474 of 388,907 characters for reasoning)
        for code in sorted({o["strong"] for o in dem if o["strong"]}):
            lx = lr._lexicon(conn, code, rt["lexicon_chars"])
            meaning[code] = {"sense_head": lx.get("sense_head"), "meaning_range": lx.get("meaning_range")}
    spec = lr.orec.items_setting(cfg)
    by_item = {i["key"]: i for i in spec["items"]}
    uses = [{"item": k, "name": by_item[k]["name"], "kinds": by_item[k]["kinds"], "bases": by_item[k]["bases"]} for k in idef["uses"] if k in by_item]
    conn.execute(f"UPDATE collection_layer_item SET pulled_at={lr.NOW}, updated_at={lr.NOW} WHERE id=?", (row[0],))
    occ = [{"occurrence": o["vl_id"], "reference": o["reference"], "osis": o["osis"], "surface": o["surface"], "strong": o["strong"]} for o in dem]
    pkg = {"command": "ReadElements", "collection": L["name"], "subgroup": gname, "step": "3.1",
           "made": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "unit": {"ledger_id": row[0], "to_take_up": len(take), "may_rest_on_besides": len(besides), "older_inner_being": len(older), "earlier_readings": len(earlier),
                    "occurrences": len(occ), "verses": len(verses)},
           "instruction": instruction(conn, rt), "asks": idef["asks"], "uses": uses, "node_roles": lr.orec.node_role_groups(cfg),
           "definition_of_the_subgroup": L["groups"][gid].get("note"), "meaning_by_code": meaning,
           "to_take_up": take, "may_rest_on_besides": besides, "older_inner_being": older, "earlier_readings": earlier, "occurrences": occ, "verses": verses,
           "answer": {"command": "ReadElements", "collection": L["name"], "subgroup": gname, "ledger_id": row[0],
                      "findings": [{"key": "f1", "kind": "", "text": "", "basis": "read | stated", "parts": {"item": " | ".join(idef["uses"]), "grounds": ""},
                                    "nodes": [{"occurrence": "<occurrence id>", "role": "<a node role>"}, {"traced": "<id of an observation it rests on>"}], "read_back": []}],
                      "not_used": {}, "older": [{"observation": o["observation"], "action": " | ".join(lr.bv.ACTIONS), "reason": ""} for o in older if not o["answered_before"]],
                      "existing": [{"observation": o["observation"], "action": "accept | modify | delete | merge | leave", "reason": ""} for o in earlier]}}
    if row[6] == "observed":
        pkg["recorded_before"] = "the elements were recorded but their check failed: read them again (the record replaces the earlier reading)"
    secs = round(time.monotonic() - t0, 2)
    chars = len(json.dumps(pkg, ensure_ascii=False))
    pkg["measured"] = {"package_chars": chars, "seconds": secs}
    if secs > lim["read_max_seconds"]:
        raise ReadError(f"ReadElements for {gname!r} took {secs} s, more than {lim['read_max_seconds']} s; nothing is written")
    if chars > rt["package_max_chars"]:
        raise ReadError(f"the elements package of {gname!r} is {chars} characters, more than {rt['package_max_chars']} (cfg_setting layer.read_types elements.package_max_chars); nothing is written")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"readelements-{_slug(L['name'])}-{_slug(gname)}-{datetime.datetime.now().strftime('%Y%m%dt%H%M%S')}.json"
    path.write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"path": path, "to_take_up": len(take), "older": len(older), "earlier": len(earlier), "verses": len(verses), "chars": chars, "seconds": secs, "opened": opened}


def record_elements(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check a filled ReadElements answer whole and write it through the recorder of stage 4 (layerinner.record: the finding rules, the traces to the evidence, the occurrences within
    what the finding rests on or read back, every observation taken up rested on or declared not used, the older inner-being observations answered, the written row checked as
    LayerCheck checks it); validate the row; name the next command. keep=False previews."""
    from . import layerinner as li
    if data.get("command") != "ReadElements":
        raise ReadError("this is not a ReadElements answer (its `command` must be ReadElements; fill the `answer` part of the package)")
    name, sub = str(data.get("collection") or ""), str(data.get("subgroup") or "")
    cid, gid, gname = _subgroup(conn, name, sub)
    row = _elements_row(conn, cid, gid)
    if row is None or data.get("ledger_id") != row[0]:
        raise ReadError(f"the answer is refused whole, nothing written:\n  ledger {data.get('ledger_id')} is not the 3.1 row of subgroup {gname!r}")
    s = lr.settings(cfg)
    L = lr.load(conn, cfg, name, pairs=False, subgroup=gname)
    dem = li.demanded(L, ELEMENTS_ITEM, gid, "", conn)
    earlier = {o["observation"] for o in _earlier_readings(conn, cfg, cid, gid, li._allowed(dem), sorted(set(s["stages"].values())))}
    named = {e.get("observation") for e in data.get("existing") or [] if isinstance(e, dict)}
    if earlier - named:
        raise ReadError("the answer is refused whole, nothing written:\n  " + f"{len(earlier - named)} earlier reading(s) of the subgroup's scope have no answer in `existing` "
                        f"(for example {sorted(earlier - named)[:6]}): answer each with accept, modify, delete, merge or leave, with its reason")
    fill = {"disposition": "observed", "findings": data.get("findings") or [], "not_used": data.get("not_used") or {}, "older": data.get("older") or [], "existing": data.get("existing") or []}
    try:
        r = li.record(conn, cfg, run_id, {"collection": name, "step": "3.1", "subgroup": gname, "rows": [{"ledger_id": row[0], "fill": fill}]}, keep)
    except lr.LayerError as exc:
        raise ReadError(str(exc))
    out = {"observed": r["observed"], "nodes": r["nodes"]}
    if not keep:
        return {**out, "preview": True}
    lr.check(conn, cfg, run_id, name, subgroup=gname)
    r2 = _elements_row(conn, cid, gid)
    res = {**out, "validated": bool(r2[9]), "reason": (r2[8] or "")[:300] if not r2[9] else "", "next": next_after_elements(conn, cfg, name, gname)}
    if r2[9] and lr.superseded(conn, cid)["rows"]:      # the last subgroup through 3.1 closes 3.1 for the collection: the sweep runs here (researcher 2026-11-26, #2538)
        from . import layerloop
        if all(g["complete"] for g in layerloop.progress(conn, cfg, name)["subgroups"]):
            sw = lr.sweep_superseded(conn, cfg, run_id, name)
            res["swept"] = f"3.1 closed for the collection: {sw['rows']} row(s) of deleted subgroups retired, {sw['observations']} observation(s) removed"
    return res


# ══ ReadBehaviours / RecordBehaviours: step 3.2, the behaviours of the collection (stage 4, C2; #2538) ═════════════════════════════
# Researcher 2026-11-26: "step 3.2 is a fundamental part of the collection process and must be codified. it is not a process that is left open for interactive chat,
# although it is reading based and the method must be called from within a chat." One package for the collection (a 3.2 row is the collection's own and is recorded whole),
# written through the recorder of stage 4 (layerinner.record), checked as LayerCheck checks it.

BEHAVIOURS_ITEM = "collection-gathering"


def _behaviours_row(conn, cid: int):
    return next((r for r in lr._rows(conn, cid, "3.2") if r[3] == BEHAVIOURS_ITEM and r[6] != "retired"), None)


def next_after_behaviours(name: str) -> str:
    return (f".\\iba\\app\\ps\\Collection-Build.ps1 -Action LayerNext -Collection {name}  (3.2 is closed once its row is validated; 3.3 and the validation after stage 4 wait for "
            f"every collection to be complete)")


def _collection_of(conn, name: str) -> tuple[int, str]:
    try:
        return lr.ci._collection(conn, name)
    except lr.ci.IndexError_ as exc:
        raise ReadError(str(exc))


def _take_up_lines(conn, cfg, ids, sub_names: dict) -> list:
    """Each observation 3.2 takes up, whole: its text, kind, item, basis, the subgroups of its nodes, the 3.1 row it was written under (if any), and its occurrences (the nodes a finding may
    name, with their verses), each written "<occurrence id> <reference> (<surface>)". Read in chunks (idx_ib_node_observation_id)."""
    ids = sorted(ids)
    lines = {}
    for part in sg.chunks(ids, cfg):
        q = ",".join("?" * len(part))
        for oid, stage, tag, text, basis, parts, key in conn.execute(f"SELECT id, stage, tag, obs_text, basis, parts, stable_key FROM ib_observation WHERE id IN ({q})", part):
            lines[oid] = {"observation": oid, "stage": stage, "kind": tag, "item": (json.loads(parts) if parts else {}).get("item"), "basis": basis, "text": text or "",
                          "ledger_row": int(key.split(":")[1]) if (key or "").startswith("layer:") else None, "subgroups": set(), "occurrences": []}
        for oid, vl, ref, surf, sgid in conn.execute(f"SELECT observation_id, verse_lexical_id, verse_reference, surface, subgroup_id FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL "
                                                     f"AND verse_lexical_id IS NOT NULL AND observation_id IN ({q}) ORDER BY verse_lexical_id", part):
            lines[oid]["occurrences"].append(f"{vl} {ref} ({surf})")      # compact: "<occurrence id> <reference> (<surface>)"; as objects 3,342 nodes of thought took 241,016 characters
            if sgid in sub_names:
                lines[oid]["subgroups"].add(sub_names[sgid])
    out = []
    for oid in ids:
        x = lines[oid]
        x["subgroups"] = sorted(x["subgroups"])
        out.append(x)
    return sorted(out, key=lambda x: ((x["subgroups"] or ["~"])[0], x["observation"]))


def read_behaviours(conn, cfg, run_id: str, name: str, out_dir: pathlib.Path) -> dict:
    """The package of step 3.2 of a collection (C2): the 3.1 findings of its current subgroups to take up (layerinner._sources; researcher 2026-11-26), each whole with its subgroups and occurrences, the subgroups with their definitions, the items a finding may use with their kinds, the node roles, the older
    observations still unsettled on its occurrences, and the answer. Opens 3.2 if it is not open (every subgroup through 3.1)."""
    from . import layerinner as li
    t0 = time.monotonic()
    st = settings(cfg)
    rt, lim = st["behaviours"], st["limits"]
    s = lr.settings(cfg)
    cid, cname = _collection_of(conn, name)
    swept = None
    if lr.superseded(conn, cid)["rows"]:      # 3.1 closes with the sweep of what deleted subgroups left behind, run here by the method (researcher 2026-11-26, #2538)
        try:
            swept = lr.sweep_superseded(conn, cfg, run_id, cname)
        except lr.LayerError as exc:
            raise ReadError(f"3.1 is not closed for {cname!r}: {exc}")
    row = _behaviours_row(conn, cid)
    opened = None
    if row is None:
        opened = lr.open_step(conn, cfg, run_id, cname, "3.2")
        row = _behaviours_row(conn, cid)
    if row is None:
        raise ReadError(f"step 3.2 has no row for {cname!r}: the collection has no grouped occurrence")
    if row[6] in ("observed", "none") and row[9]:
        raise ReadError(f"the behaviours of {cname!r} are read and validated; next: " + next_after_behaviours(cname))
    L = lr.load(conn, cfg, cname, pairs=False)
    sd = lr.step_def(s, "3.2")
    idef = s["items"][BEHAVIOURS_ITEM]
    subs = {r[0]: {"name": r[1], "definition": r[2]} for r in conn.execute("SELECT id, name, note FROM collection_subgroup WHERE collection_id=? AND deleted=0 ORDER BY id", (cid,))}
    with sg.budget(conn, cfg, "ReadBehaviours"):
        dem = li.demanded(L, BEHAVIOURS_ITEM, 0, "", conn)
        sources, required = li._sources(conn, s, L, sd, 0, "")
        take = _take_up_lines(conn, cfg, required, {k: v["name"] for k, v in subs.items()})
        older = lr.bv.older_on(conn, cfg, s, li._allowed(dem), 99)
        done = lr.bv.settled(conn, cfg, list(older))
        older = [{"observation": k, "stage": v.get("stage"), "kind": v.get("tag"), "nature": v.get("nature"), "text": v.get("text") or ""} for k, v in sorted(older.items()) if k not in done]
    spec = lr.orec.items_setting(cfg)
    by_item = {i["key"]: i for i in spec["items"]}
    uses = [{"item": k, "name": by_item[k]["name"], "kinds": by_item[k]["kinds"], "bases": by_item[k]["bases"]} for k in idef["uses"] if k in by_item]
    conn.execute(f"UPDATE collection_layer_item SET pulled_at={lr.NOW}, updated_at={lr.NOW} WHERE id=?", (row[0],))
    by_sub = {}
    for x in take:
        for g in x["subgroups"] or ["(no subgroup on its nodes)"]:
            by_sub.setdefault(g, []).append(x["observation"])
    pkg = {"command": "ReadBehaviours", "collection": cname, "step": "3.2",
           "made": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "unit": {"ledger_id": row[0], "to_take_up": len(take), "subgroups": len(subs), "older_unsettled": len(older), "occurrences": len(dem)},
           "instruction": instruction(conn, rt), "asks": idef["asks"], "uses": uses, "node_roles": lr.orec.node_role_groups(cfg),
           "subgroups": [{"name": v["name"], "definition": v["definition"], "observations": by_sub.get(v["name"], [])} for v in subs.values()],
           "to_take_up": take, "older_unsettled": older,
           "answer": {"command": "ReadBehaviours", "collection": cname, "ledger_id": row[0], "disposition": "observed | none", "reason": "",
                      "findings": [{"key": "b1", "kind": "", "text": "", "basis": "read | stated", "parts": {"item": "flag", "flag_type": "discovery", "grounds": ""},
                                    "nodes": [{"traced": "<id of an observation this behaviour gathers>"}, {"occurrence": "<occurrence id of a traced observation>", "role": "<a node role>"}],
                                    "read_back": []}],
                      "not_gathered": {}, "older": [{"observation": o["observation"], "action": " | ".join(lr.bv.ACTIONS), "reason": ""} for o in older], "existing": []}}
    if "(no subgroup on its nodes)" in by_sub:
        pkg["subgroups"].append({"name": "(no subgroup on its nodes)", "definition": None, "observations": by_sub["(no subgroup on its nodes)"]})
    if row[6] == "observed":
        pkg["recorded_before"] = "the behaviours were recorded but their check failed: read them again (the record replaces the earlier reading)"
    secs = round(time.monotonic() - t0, 2)
    chars = len(json.dumps(pkg, ensure_ascii=False))
    pkg["measured"] = {"package_chars": chars, "seconds": secs}
    max_s = rt.get("read_max_seconds", lim["read_max_seconds"])
    if secs > max_s:
        raise ReadError(f"ReadBehaviours for {cname!r} took {secs} s, more than {max_s} s (cfg_setting layer.read_types); nothing is written")
    if chars > rt["package_max_chars"]:
        raise ReadError(f"the behaviours package of {cname!r} is {chars} characters, more than {rt['package_max_chars']} (cfg_setting layer.read_types behaviours.package_max_chars); nothing is written")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"readbehaviours-{_slug(cname)}-{datetime.datetime.now().strftime('%Y%m%dt%H%M%S')}.json"
    path.write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding="utf-8")
    out = {"path": path, "to_take_up": len(take), "subgroups": len(subs), "older": len(older), "chars": chars, "seconds": secs, "opened": opened}
    if swept:
        out["swept"] = f"{swept['rows']} row(s) of deleted subgroups retired, {swept['observations']} observation(s) removed"
    return out


def record_behaviours(conn, cfg, run_id: str, data: dict, keep: bool) -> dict:
    """Check a filled ReadBehaviours answer whole and write it through the recorder of stage 4 (layerinner.record: at least one behaviour, a flag finding of type discovery; every finding
    rests on inner-being observations of the collection by traced nodes; its occurrences within theirs or read back; every observation taken up gathered or declared not gathered with
    its reason; the older observations answered; the written row checked as LayerCheck checks it); validate the collection's rows; name the next command. keep=False previews."""
    from . import layerinner as li
    if data.get("command") != "ReadBehaviours":
        raise ReadError("this is not a ReadBehaviours answer (its `command` must be ReadBehaviours; fill the `answer` part of the package)")
    cid, cname = _collection_of(conn, str(data.get("collection") or ""))
    row = _behaviours_row(conn, cid)
    if row is None or data.get("ledger_id") != row[0]:
        raise ReadError(f"the answer is refused whole, nothing written:\n  ledger {data.get('ledger_id')} is not the 3.2 row of {cname!r}")
    disp = data.get("disposition")
    if disp not in ("observed", "none"):
        raise ReadError("the answer is refused whole, nothing written:\n  `disposition` is observed (with findings) or none (with its reason)")
    fill = {"disposition": disp, "reason": data.get("reason") or "", "findings": data.get("findings") or [], "not_gathered": data.get("not_gathered") or {},
            "older": data.get("older") or [], "existing": data.get("existing") or []}
    try:
        r = li.record(conn, cfg, run_id, {"collection": cname, "step": "3.2", "rows": [{"ledger_id": row[0], "fill": fill}]}, keep)
    except lr.LayerError as exc:
        raise ReadError(str(exc))
    out = {"observed": r["observed"], "none": r["none"], "nodes": r["nodes"]}
    if not keep:
        return {**out, "preview": True}
    lr.check(conn, cfg, run_id, cname)
    r2 = _behaviours_row(conn, cid)
    return {**out, "validated": bool(r2[9]), "reason": (r2[8] or "")[:300] if not r2[9] else "", "next": next_after_behaviours(cname)}
