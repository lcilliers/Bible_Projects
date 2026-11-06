"""surface_cycle_load_2361_v1_20261106.py -- escalation #2361, stage 1b: the one-time load of the recorded surface-cycle work.

Loads, from the import folders of _analytics/surfaces/working_files (the only place a file is ever an input), the work of
2026-10-31 to 2026-11-05 into the tables built by stage 1a, then CHECKS every count against the recorded files and rolls the
whole load back on any mismatch:
  config   cfg_ai_model (5), cfg_ai_prompt (16 versions), cfg_base_construct (79) and four corrections to notes/enums, all
           through configmaint.apply_logged()
  group    6,069 surfaces (+ the empty-string junk surface) with the final group (first-split-v4), 56 corrections as events,
           one ai_call per judged surface
  base     the 79 constructs applied (1,386 hits, leads, siblings), the 707 Ollama answers, the combined base of the 3,850
           surfaces of collection a (workbook of #2359), flags (held pairs, possible opposites, none, failed, possessives, junk)
  collect  48 collections (latest run per seed live), their links in six tiers, poles, listed words, every recorded judgement
           of the five runs that count as ai_call rows, the states of the bases
  tests    252 evaluation cases, all provisional
Recorded model calls are loaded as they were recorded: the request is not stored (it was not recorded), the answer is the
recorded line, via says 'loaded'. Nothing here is a new judgement. Idempotent (a second run changes nothing). One transaction.
A named rollback snapshot is taken before a live apply.

Usage:
    python iba/app/migration/surface_cycle_load_2361_v1_20261106.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import collections
import csv
import datetime
import json
import pathlib
import re
import sys

import openpyxl

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())  # live or archived
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = pathlib.Path(r"C:\Bible_study_projects\iba\app\db\iba.db")
RUN_ID = "DEVMODE-2361-SURFACE-CYCLE-LOAD-20261106"
MODULE = "surface_cycle_load_2361_v1_20261106"
WF = ROOT / "_analytics" / "surfaces" / "working_files"
G, ST, BA, CO = WF / "group" / "import", WF / "structure" / "import", WF / "base" / "import", WF / "collection" / "import"
WORKBOOK = ROOT / "outputs" / "escalation" / "2359-surfaces-and-bases-v1-20261104.xlsx"
TAGS = ["v4", "v5", "v6", "v7", "v8"]          # the five collection runs that count, in order; a later run replaces a seed
SUFFIX = "-20261105"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
INFLECTION_KINDS = ("plural", "past tense", "present participle", "comparative", "superlative")


def jl(path):
    return [(i + 1, json.loads(l)) for i, l in enumerate(open(path, encoding="utf-8")) if l.strip()]


def rel(p):
    return pathlib.Path(p).relative_to(WF).as_posix()


# ---------------------------------------------------------------------------------------------------------------------------
# the config part: audited writes
# ---------------------------------------------------------------------------------------------------------------------------
def plan_cfg(conn):
    ops = []
    has = lambda sql, *a: conn.execute(sql, a).fetchone() is not None  # noqa: E731
    one = lambda sql, *a: conn.execute(sql, a).fetchone()  # noqa: E731
    # corrections to what stage 1a registered
    if not has("SELECT 1 FROM cfg_enum WHERE name='cfg_base_construct.direction' AND value='opposite'"):
        ops.append(("cfg_enum", "insert", {}, {"name": "cfg_base_construct.direction", "value": "opposite", "ordinal": 2, "inactive": 0}))
        ops.append(("cfg_column", "update", {"table_name": "cfg_base_construct", "name": "direction"}, {"use": (
            "same (the base keeps the meaning: accepted as a base), opposite (a negating prefix or suffix: the match is a "
            "possible opposite, a lead, never accepted as a base), candidate (another prefix kept as a lead, not accepted as "
            "the same meaning). Recorded in the control of 2026-11-04")}))
    if has("SELECT 1 FROM cfg_enum WHERE name='surface_term.base_state' AND value='flagged'"):
        ops.append(("cfg_enum", "delete", {"name": "surface_term.base_state", "value": "flagged"}, {}))
        old = one("SELECT use FROM cfg_column WHERE table_name='surface_term' AND name='base_state'")[0]
        new = old.replace(" flagged (an open surface_flag needs the researcher);", "").replace("; flagged (an open surface_flag needs the researcher)", "")
        assert "flagged" not in new, "the base_state note still names flagged"
        new = new.rstrip(" .") + ". Open exceptions are read from surface_flag, not from this state"
        ops.append(("cfg_column", "update", {"table_name": "surface_term", "name": "base_state"}, {"use": new}))
    for tbl, a, b in (("cfg_ai_prompt", "cfg_setting holds only which version is active for a prompt_key; a call can use only an active version",
                       "status says which version is active (at most one per prompt_key); a call can use only an active version"),
                      ("cfg_ai_model", "settings say which model serves the role; this table documents the model",
                       "the active row of a role says which model serves it (at most one per role) and documents the model")):
        cur = one("SELECT use FROM cfg_table WHERE database='iba' AND name=?", tbl)[0]
        if a in cur:
            ops.append(("cfg_table", "update", {"database": "iba", "name": tbl}, {"use": cur.replace(a, b)}))
    if not has("SELECT 1 FROM cfg_write_grant WHERE writer='migration' AND table_name='run' AND database='iba'"):
        ops.append(("cfg_write_grant", "insert", {}, {"writer": "migration", "table_name": "run", "database": "iba", "inactive": 0}))
    # the models, the prompts, the construct rules
    for m in json.load(open(BA / "models-v1-20261106.json", encoding="utf-8")):
        if not has("SELECT 1 FROM cfg_ai_model WHERE name=? AND role=?", m["name"], m["role"]):
            ops.append(("cfg_ai_model", "insert", {}, {**m, "inactive": 0}))
    for p in json.load(open(CO / "prompts-v1-20261106.json", encoding="utf-8")):
        if not has("SELECT 1 FROM cfg_ai_prompt WHERE prompt_key=? AND version=?", p["prompt_key"], p["version"]):
            ops.append(("cfg_ai_prompt", "insert", {"_parent": p["parent_version"]}, {
                "prompt_key": p["prompt_key"], "version": p["version"], "text": p["text"], "hash": p["hash"], "role": p["role"],
                "purpose": p["purpose"], "expected_output": p["expected_output"], "status": p["status"], "change_note": p["change_note"],
                "created_by": "Claude", "created_at": NOW, "activated_at": NOW if p["status"] == "active" else None}))
    ctrl = json.load(open(ST / "surface-match-control-v3-20261104.json", encoding="utf-8"))
    for c in ctrl["constructs"]:
        if not has("SELECT 1 FROM cfg_base_construct WHERE id=?", c["id"]):
            ops.append(("cfg_base_construct", "insert", {}, {
                "id": c["id"], "kind": c["kind"], "direction": c["direction"], "strip": c["strip"], "add": c["add"],
                "undouble": 1 if c["undouble"] else 0, "strip_prefix": c["strip_prefix"], "description": c["description"],
                "example": c["example"], "inactive": 0}))
    if not has("SELECT 1 FROM cfg_utility WHERE module=?", MODULE):
        ops.append(("cfg_utility", "insert", {}, {
            "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
            "purpose": f"ONE-OFF migration -- escalation #2361 stage 1b: the load of the recorded surface-cycle work into the "
                       f"tables of stage 1a, with reconciliation; run_id {RUN_ID}.",
            "config_exempt": 1, "config_exempt_reason": "one-off migration script -- writes cfg_* rows through "
            "configmaint.apply_logged, same class as the other Developer Mode migrations",
            "crash_escalation_reviewed": 0, "crash_escalation_note": None}))
    return ops


def apply_cfg(conn, ops):
    pid = {}
    for t, op, where, set_ in ops:
        parent = None
        if t == "cfg_ai_prompt":
            parent = where.pop("_parent", None)
            if parent is not None:
                row = conn.execute("SELECT id FROM cfg_ai_prompt WHERE prompt_key=? AND version=?", (set_["prompt_key"], parent)).fetchone()
                set_ = {**set_, "parent_id": row[0] if row else None}
        apply_logged(conn, RUN_ID, t, op, where, set_)


# ---------------------------------------------------------------------------------------------------------------------------
# the data part
# ---------------------------------------------------------------------------------------------------------------------------
def load(conn):
    cur = conn.cursor()
    ins = lambda table, d: cur.execute(  # noqa: E731
        f'INSERT INTO "{table}" ({",".join(chr(34) + k + chr(34) for k in d)}) VALUES ({",".join("?" * len(d))})', list(d.values())).lastrowid
    base = {"run_id": RUN_ID, "created_by": "migration"}
    scope = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='surfaces.scope_groups'").fetchone()[0])
    scope_a = set(scope["a"])
    junk = [re.compile(p) for p in json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='surfaces.junk_rules'").fetchone()[0]).values()]
    mid = {(r[1], r[2]): r[0] for r in conn.execute("SELECT id, name, role FROM cfg_ai_model")}
    pid = {(r[1], r[2]): r[0] for r in conn.execute("SELECT id, prompt_key, version FROM cfg_ai_prompt")}
    judge = mid[("qwen3:30b", "judge")]
    cnt = collections.Counter()

    cur.execute("INSERT INTO run (run_id, work_package, params, runs_over, config_version, state, resume_point, started_at, ended_at, outcome, "
                "settings_snapshot, counts) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (RUN_ID, "surface-cycle-load", "{}", "", "app-0.1.0", "done", "load", NOW, NOW,
                 "one-time load of the recorded surface-cycle work (#2361 stage 1b)",
                 json.dumps({"prompts": {k[0] + "@" + str(k[1]): v for k, v in pid.items()}, "models": {k[0] + ":" + k[1]: v for k, v in mid.items()}}), None))

    # ---- 1. the surfaces and their group ---------------------------------------------------------------------------------
    v4 = jl(G / "first-split-v4-20261104.jsonl")
    tid = {}
    for ln, r in v4:
        s = r["surface"]
        tid[s] = ins("surface_term", {**base, "surface": s, "form": "phrase" if " " in s else "word", "origin": "surface",
                     "surface_group": r["group"], "group_reason": r.get("reason"), "group_judged_by": r.get("judged_by"),
                     "group_state": "corrected" if r.get("original_group") else "judged", "base_state": "out_of_scope",
                     "load_ref": f"{rel(G / 'first-split-v4-20261104.jsonl')}#{ln}"})
    cnt["surfaces"] = len(v4)
    tid[""] = ins("surface_term", {**base, "surface": "", "form": "word", "origin": "surface", "group_state": "unjudged",
                  "base_state": "out_of_scope", "deleted": 1, "load_ref": "surface_subgroup (the empty surface, no judged line)"})
    # ---- 2. the group calls and the corrections ----------------------------------------------------------------------------
    for ln, r in v4:
        orig = r.get("original_group") or r["group"]
        ins("ai_call", {**base, "module": "group", "step": "group", "role": "judge", "model_id": judge, "prompt_id": pid[("group.word", 3)],
            "subject_kind": "surface_term", "subject_id": tid[r["surface"]], "answer": json.dumps({"group": orig, "reason": r.get("reason")}),
            "result": orig, "via": "loaded", "outcome": "answered", "tokens_in": r.get("prompt_tokens"), "tokens_out": r.get("out_tokens"),
            "secs": r.get("secs"), "load_ref": f"{rel(G / 'first-split-v4-20261104.jsonl')}#{ln}"})
        cnt["group_calls"] += 1
    wb = openpyxl.load_workbook(G / "surface-repoint-m1-v1-20261104.xlsx", read_only=True)
    applied = list(wb["Applied changes"].iter_rows(values_only=True))[1:]
    for i, a in enumerate(applied):
        ins("surface_event", {**base, "subject_kind": "surface_term", "subject_id": tid[a[0]], "action": "correct", "field": "surface_group",
            "value_before": a[1], "value_after": a[2], "by": "researcher instruction 2026-11-04 (#2359 repoint)",
            "reason": f"{a[5]}; {a[6]}; because of: {a[4]}", "load_ref": f"{rel(G / 'surface-repoint-m1-v1-20261104.xlsx')}#Applied changes row {i + 2}"})
        cnt["corrections"] += 1
    # ---- 3. the recorded outcome of the base work ---------------------------------------------------------------------------
    ctrl = json.load(open(ST / "surface-match-control-v3-20261104.json", encoding="utf-8"))
    cs = {s["surface"]: s for s in ctrl["surfaces"]}
    ws = openpyxl.load_workbook(WORKBOOK, read_only=True)["Surfaces"]
    rows = list(ws.iter_rows(values_only=True))
    ix = {n: i for i, n in enumerate(rows[0])}
    W = {r[ix["surface"]]: {n: r[i] for n, i in ix.items()} for r in rows[1:]}
    assert len(W) == 3850 and set(W) == set(cs), "the workbook and the control do not list the same 3,850 surfaces"
    bases = {W[s]["combined base"] for s in W}
    for b in sorted(bases):
        if b not in tid:
            tid[b] = ins("surface_term", {**base, "surface": b, "form": "phrase" if " " in b else "word", "origin": "computed",
                         "group_state": "unjudged", "base_state": "resolved_own", "base_source": "own",
                         "load_ref": "outputs/escalation/2359-surfaces-and-bases-v1-20261104.xlsx#combined base"})
            cnt["computed_bases"] += 1
    for b in sorted(bases):  # a computed base is its own base
        conn.execute("UPDATE surface_term SET base_id=id WHERE id=? AND origin='computed'", (tid[b],))
    ol = {r["surface"]: (ln, r) for ln, r in jl(BA / "base-form-v1-20261104.jsonl")}
    oll_call = {}
    for s, (ln, r) in ol.items():
        outcome = "answered" if r.get("relation") else ("failed" if any(e.startswith("call failed") for e in r.get("errors", [])) else "refused")
        oll_call[s] = ins("ai_call", {**base, "module": "ai_base", "step": "base", "role": "judge", "model_id": judge, "prompt_id": pid[("base.word", 2)],
                          "subject_kind": "surface_term", "subject_id": tid[s], "answer": json.dumps({k: r.get(k) for k in ("relation", "base", "reason")}),
                          "result": r.get("base") if r.get("relation") else None, "via": "loaded " + str(r.get("relation")), "outcome": outcome,
                          "error": "; ".join(r.get("errors", [])) or None if outcome != "answered" else None,
                          "tokens_in": r.get("prompt_tokens"), "tokens_out": r.get("out_tokens"), "secs": r.get("secs"),
                          "load_ref": f"{rel(BA / 'base-form-v1-20261104.jsonl')}#{ln}"})
        cnt["ollama_calls"] += 1
        cnt["ollama_" + outcome] += 1
    # derivations: structure hits (all directions), leads, siblings, the Ollama answers, own
    def derive(term, method, evidence, kind, word, accepted, ref, call=None, base_term=None):
        ins("surface_derivation", {**base, "term_id": tid[term], "method": method, "evidence": evidence, "kind": kind, "base_word": word,
            "base_term_id": tid.get(base_term if base_term is not None else word), "accepted": 1 if accepted else 0, "ai_call_id": call, "load_ref": ref})
        cnt["deriv_" + method] += 1
    cmap = {c["id"]: c for c in ctrl["constructs"]}
    for i, h in enumerate(ctrl["hits"]):
        c = cmap[h["construct"]]
        if c["direction"] == "opposite":
            kind = "lead_opposite"
        elif c["direction"] == "candidate":
            kind = "lead_other"
        else:
            kind = "inflection" if c["kind"].startswith(INFLECTION_KINDS) else "derivation"
        w = W[h["tested"]]
        acc = c["direction"] == "same" and w["combined base source"] == "structure" and w["combined base"] == h["base"]
        derive(h["tested"], "structure", h["construct"], kind, h["base"], acc, f"{rel(ST / 'surface-match-control-v3-20261104.json')}#hits[{i}]")
        cnt["hits"] += 1
    for s, x in cs.items():
        for e in x.get("base_outside_input") or []:
            m = re.match(r"(.+?) \((C\d+|P\d+), ", e)
            derive(s, "structure", m.group(2) if m else None, "derivation", m.group(1) if m else e, False,
                   f"{rel(ST / 'surface-match-control-v3-20261104.json')}#surfaces.base_outside_input", base_term=m.group(1) if m else e)
            cnt["outside_leads"] += 1
        for y in x.get("starts_with_leads") or []:
            derive(y, "structure", "starts_with", "lead_starts_with", s, False, f"{rel(ST / 'surface-match-control-v3-20261104.json')}#surfaces.starts_with_leads")
            cnt["starts_with_leads"] += 1
        for e in x.get("sibling_via") or []:
            m = re.match(r"(.+?) via (\S+)", e)
            derive(s, "sibling", x.get("sibling_group"), "derivation", m.group(1), False, f"{rel(ST / 'surface-match-control-v3-20261104.json')}#surfaces.sibling_via", base_term="\0")
            cnt["sibling_rows"] += 1
    for s, (ln, r) in ol.items():
        w = W.get(s)
        if r.get("relation") in ("inflection", "derivation"):
            derive(s, "ollama", str(oll_call[s]), r["relation"], r["base"], bool(w and w["combined base source"] == "ollama"),
                   f"{rel(BA / 'base-form-v1-20261104.jsonl')}#{ln}", call=oll_call[s])
        elif r.get("relation") == "none":
            derive(s, "ollama", str(oll_call[s]), "own", r.get("base") or s, False, f"{rel(BA / 'base-form-v1-20261104.jsonl')}#{ln}", call=oll_call[s], base_term=s)
    # the resolved base and the states of the 3,850
    src_map = {"structure": "structure", "ollama": "ollama", "none (own base)": "own"}
    for s, w in W.items():
        b, src = w["combined base"], src_map[w["combined base source"]]
        st2 = cs[s]["status_v2"]
        orel = w["Ollama relation"]
        if cs[s]["form"] == "phrase":
            state = "phrase_not_tested"
        elif src == "structure":
            state = "matched_structure"
        elif src == "ollama":
            state = "ai_answered"
        elif orel == "FAILED":
            state = "ai_failed"
        elif orel == "none":
            state = "ai_none"
        elif st2.startswith("sibling"):
            state = "matched_sibling"
        else:
            state = "resolved_own"
        conn.execute("UPDATE surface_term SET base_id=?, base_source=?, base_state=? WHERE id=?", (tid[b], src, state, tid[s]))
        if src == "own":
            derive(s, "own", None, "own", s, True, "outputs/escalation/2359-surfaces-and-bases-v1-20261104.xlsx#combined base source", base_term=s)
        cnt["state_" + state] += 1
        cnt["source_" + src] += 1
    # ---- 4. flags --------------------------------------------------------------------------------------------------------
    def flag(kind, subject, note, status="open", sk="surface_term"):
        ins("surface_flag", {**base, "subject_kind": sk, "subject_id": subject, "kind": kind, "note": note, "status": status})
        cnt["flag_" + kind] += 1
    held = list(openpyxl.load_workbook(G / "surface-repoint-m1-v1-20261104.xlsx", read_only=True)["Held for decision"].iter_rows(values_only=True))[1:]
    byb = collections.defaultdict(list)
    for h in held:
        byb[h[0]].append(h)
    for b, hs in byb.items():
        flag("held_pair", tid[b], f"base word held in group {hs[0][1]}; derived words not applied: " + "; ".join(f"{h[2]} ({h[3]}) via {h[4]}, {h[5]}" for h in hs))
    # the 22 flags recorded on 2026-11-04 came from an ad hoc string check whose code was not kept and cannot be reproduced from
    # its output; they are loaded as recorded, and the structure control's own negating leads add the others (marked by source)
    res = list(openpyxl.load_workbook(ROOT / "outputs" / "escalation" / "2359-base-form-results-v1-20261104.xlsx", read_only=True)["Accepted"].iter_rows(values_only=True))
    rec22 = {r[0]: r[5] for r in res[1:] if r[5]}
    for s_, why in rec22.items():
        flag("possible_opposite", tid[s_], f"recorded 2026-11-04 in 2359-base-form-results (ad hoc check, code not kept): {why}; AI base {ol[s_][1]['base']}")
    for s, (ln, r) in ol.items():
        if r.get("relation") in ("inflection", "derivation") and cs[s].get("opposite_leads") and s not in rec22:
            flag("possible_opposite", tid[s], f"from the structure control, not in the 2026-11-04 flag: the AI base {r['base']} was accepted but the surface has a negating lead: " + ", ".join(cs[s]["opposite_leads"]))
        if r.get("relation") == "none":
            flag("ai_none", tid[s], "the AI said it has no base of the same root meaning; not yet checked")
        if not r.get("relation"):
            flag("ai_failed", tid[s], "tried, no usable answer; " + "; ".join(r.get("errors", []))[:300])
    for s in list(tid):
        if re.search(r"[’']s$", s) and s:
            flag("possessive", tid[s], "a possessive form kept apart from its base " + re.sub(r"[’']s$", "", s))
    for s in list(tid):
        if any(p.search(s) for p in junk):
            conn.execute("UPDATE surface_term SET deleted=1 WHERE id=?", (tid[s],))
            flag("junk_surface", tid[s], "found by cfg_setting surfaces.junk_rules; soft deleted in surface_subgroup by migration junk_surfaces_2361_v1_20261106", status="settled")
            ins("surface_event", {**base, "subject_kind": "surface_term", "subject_id": tid[s], "action": "mark_deleted", "field": "deleted",
                "value_before": "0", "value_after": "1", "by": "migration junk_surfaces_2361_v1_20261106", "reason": "junk surface by rule"})
    # ---- 5. the collections ----------------------------------------------------------------------------------------------
    sfmap = {}  # word (lower) -> the single-word base it belongs to, from the recorded combined base of the 3,850 surfaces
    for s_, w_ in W.items():
        if " " not in w_["combined base"]:
            sfmap[w_["combined base"].lower()] = w_["combined base"]
    for s_, w_ in W.items():
        if " " not in w_["combined base"]:
            sfmap.setdefault(s_.lower(), w_["combined base"])
    cur_run, runs = {}, {}
    for t in TAGS:
        runs[t] = {"C": json.load(open(CO / f"collections-{t}{SUFFIX}.json", encoding="utf-8")),
                   "judge": jl(CO / f"judge-{t}{SUFFIX}.jsonl"), "lists": {r["seed"]: (ln, r) for ln, r in jl(CO / f"lists-{t}{SUFFIX}.jsonl")},
                   "poles": {r["seed"]: (ln, r) for ln, r in jl(CO / f"poles-{t}{SUFFIX}.jsonl")}, "assoc": jl(CO / f"assoc-{t}{SUFFIX}.jsonl")}
        for s in runs[t]["C"]["collections"]:
            cur_run[s] = t
    cid, jcall = {}, {}
    for s, t in cur_run.items():
        pw = runs[t]["poles"].get(s)
        p = pw[1] if pw else {}
        cid[s] = ins("collection", {**base, "core_term_id": tid[s], "name": s, "status": "indicative", "pole_word": p.get("pole"),
                     "pole_of_pole": p.get("pole_of_pole"), "pole_reciprocal": (1 if p.get("reciprocal") else 0) if p.get("pole") else None,
                     "pole_real_word": 1 if (p.get("pole") and t in ("v7", "v8")) else None,
                     "load_ref": f"{rel(CO / ('collections-' + t + SUFFIX + '.json'))}#{s}"})
        cnt["collections"] += 1
    # every recorded judgement of the five runs as an ai_call (history), the live ones linked
    synonym_p = pid[("collection.synonym", 2)]
    for t in TAGS:
        for ln, r in runs[t]["judge"]:
            b, s = r["b"], r["seed"]
            if b not in tid:
                continue
            jcall[(t, s, b)] = ins("ai_call", {**base, "module": "collection", "step": "candidate", "role": "judge", "model_id": judge, "prompt_id": synonym_p,
                "subject_kind": "surface_term", "subject_id": tid[b], "answer": json.dumps(r), "result": r.get("relation"),
                "via": "loaded " + str(r.get("via") or "quick"), "outcome": "answered" if r.get("relation") else "failed",
                "load_ref": f"{rel(CO / ('judge-' + t + SUFFIX + '.jsonl'))}#{ln} (seed {s})"})
            cnt["judge_calls"] += 1
        for ln, r in runs[t]["assoc"]:
            b = r["b"]
            if b in tid:
                jcall[(t, "assoc", r["seed"], b)] = ins("ai_call", {**base, "module": "collection", "step": "associated", "role": "judge", "model_id": judge,
                    "prompt_id": pid[("collection.associated", 1)], "subject_kind": "surface_term", "subject_id": tid[b], "answer": json.dumps(r),
                    "result": "true" if r.get("associated") else "false", "via": "loaded", "outcome": "answered" if r.get("associated") is not None else "failed",
                    "load_ref": f"{rel(CO / ('assoc-' + t + SUFFIX + '.jsonl'))}#{ln} (seed {r['seed']})"})
                cnt["assoc_calls"] += 1
        for s, (ln, r) in runs[t]["lists"].items():
            ins("ai_call", {**base, "module": "collection", "step": "listing", "role": "judge", "model_id": judge, "prompt_id": pid[("collection.list", 1)],
                "subject_kind": "collection", "subject_id": cid[s], "answer": json.dumps(r), "result": str(len(r["synonyms"])) + " synonyms, " + str(len(r["opposites"])) + " opposites",
                "via": "loaded", "outcome": "answered", "load_ref": f"{rel(CO / ('lists-' + t + SUFFIX + '.jsonl'))}#{ln}"})
            cnt["list_calls"] += 1
        for s, (ln, r) in runs[t]["poles"].items():
            ins("ai_call", {**base, "module": "collection", "step": "pole", "role": "judge", "model_id": judge, "prompt_id": pid[("collection.pole", 1)],
                "subject_kind": "collection", "subject_id": cid[s], "answer": json.dumps(r), "result": r.get("pole"), "via": "loaded", "outcome": "answered",
                "load_ref": f"{rel(CO / ('poles-' + t + SUFFIX + '.jsonl'))}#{ln}"})
            cnt["pole_calls"] += 1
    # links of the live (latest) run of each seed: member > set_aside > possible_opposite > associated
    placed_anywhere = {b for s, t in cur_run.items() for b in runs[t]["C"]["collections"][s]}
    link_of = {}
    def link(s, b, tier, call, reason=None):
        key = (s, b)
        order = ["core", "synonym", "opposite", "set_aside", "possible_opposite", "associated"]
        if key in link_of and order.index(link_of[key][0]) <= order.index(tier):
            return
        link_of[key] = (tier, call, reason)
    for s, t in cur_run.items():
        mem = runs[t]["C"]["collections"][s]
        link(s, s, "core", None, "the seed")
        for b in mem[1:]:
            j = next((r for _, r in runs[t]["judge"] if r["seed"] == s and r["b"] == b), None)
            link(s, b, "opposite" if j and j.get("relation") == "opposite" else "synonym", jcall.get((t, s, b)))
        for w in runs[t]["lists"][s][1]["synonyms"]:
            b = sfmap.get(w)
            if b and b != s and b in tid and b not in placed_anywhere:
                j = next((r for _, r in runs[t]["judge"] if r["seed"] == s and r["b"] == b), None)
                if j and j.get("relation") == "distinct":
                    link(s, b, "set_aside", jcall.get((t, s, b)), "listed by the model, refused by the judge")
        for b in runs[t]["C"]["possible_opposites"][s]:
            if b in tid:
                link(s, b, "possible_opposite", jcall.get((t, s, b)))
        for ln, r in runs[t]["assoc"]:
            if r["seed"] == s and r.get("associated") and r["b"] in tid and r["b"] not in runs[t]["C"]["collections"][s]:
                link(s, r["b"], "associated", jcall.get((t, "assoc", s, r["b"])), r.get("reason"))
    members = collections.defaultdict(set)
    for (s, b), (tier, call, reason) in link_of.items():
        if tier in ("core", "synonym", "opposite"):
            members[b].add(s)
    for (s, b), (tier, call, reason) in link_of.items():
        ins("collection_link", {**base, "collection_id": cid[s], "term_id": tid[b], "tier": tier, "shared": 1 if len(members.get(b, ())) > 1 and tier in ("core", "synonym", "opposite") else 0,
            "ai_call_id": call, "reason": reason, "load_ref": f"{rel(CO / ('collections-' + cur_run[s] + SUFFIX + '.json'))}#{s}"})
        cnt["link_" + tier] += 1
    for s, t in cur_run.items():
        mem = set(runs[t]["C"]["collections"][s])
        r = runs[t]["lists"][s][1]
        seen = set()
        for kind, words in (("synonym", r["synonyms"]), ("opposite", r["opposites"])):
            for w in words:
                if (w, kind) in seen:
                    continue
                seen.add((w, kind))
                b = sfmap.get(w)
                j = next((x for _, x in runs[t]["judge"] if x["seed"] == s and x["b"] == b), None) if b else None
                outcome = "not_in_pool" if not b or b not in tid else ("bound" if b in mem else ("refused" if j else "unjudged"))
                ins("collection_listing", {**base, "collection_id": cid[s], "word": w, "kind": kind, "term_id": tid.get(b) if b else None, "outcome": outcome,
                    "load_ref": f"{rel(CO / ('lists-' + t + SUFFIX + '.jsonl'))}"})
                cnt["listing"] += 1
    # the state of every base as a base in the collections
    base_ids = {r[0] for r in conn.execute("SELECT DISTINCT base_id FROM surface_term WHERE base_id IS NOT NULL")}
    state_of = {}
    for tid_ in base_ids:
        tiers = [r[0] for r in conn.execute("SELECT tier FROM collection_link WHERE term_id=? AND deleted=0", (tid_,))]
        mem_n = sum(1 for x in tiers if x in ("core", "synonym", "opposite"))
        if mem_n > 1:
            st = "shared"
        elif mem_n == 1:
            st = "placed"
        elif "set_aside" in tiers:
            st = "set_aside"
        elif tiers:
            st = "listed_only"
        else:
            st = "untouched"
        conn.execute("UPDATE surface_term SET collection_state=? WHERE id=?", (st, tid_))
        state_of[tid_] = st
    # ---- 6. the evaluation cases (all provisional) -----------------------------------------------------------------------------
    for i, c in enumerate(json.load(open(CO / "eval-cases-v1-20261106.json", encoding="utf-8"))):
        ins("surface_eval_case", {**base, "module": c["module"], "step": c["step"], "a": c["a"], "b": c["b"], "expected": c["expected"], "source": c["source"],
            "standing": "provisional", "note": c["note"], "load_ref": f"{rel(CO / 'eval-cases-v1-20261106.json')}#{i}"})
        cnt["eval_cases"] += 1
    return cnt, tid, state_of


# ---------------------------------------------------------------------------------------------------------------------------
# the reconciliation: every number checked against the recorded files; any mismatch rolls the load back
# ---------------------------------------------------------------------------------------------------------------------------
def reconcile(conn, cnt):
    q = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731
    checks = []
    def chk(name, got, want):
        checks.append((name, got, want, got == want))
    g = dict(conn.execute("SELECT surface_group, count(*) FROM surface_term WHERE origin='surface' AND surface_group IS NOT NULL GROUP BY 1").fetchall())
    chk("surfaces judged", sum(g.values()), 6069)
    chk("behaviour", g.get("behaviour"), 1317); chk("inner_being_state", g.get("inner_being_state"), 2533)
    chk("being", g.get("being"), 716); chk("other (incl. 3 junk)", g.get("other"), 1503)
    chk("group corrections (events and state corrected)", (cnt["corrections"], q("SELECT count(*) FROM surface_term WHERE group_state='corrected'")), (56, 56))
    chk("construct rules", q("SELECT count(*) FROM cfg_base_construct"), 79)
    chk("structure hits (all directions)", cnt["hits"], 1386)
    chk("structure hits by direction same/opposite/candidate", tuple(q("SELECT count(*) FROM surface_derivation WHERE load_ref LIKE '%#hits[%' AND kind IN ({K})".replace("{K}", k)) for k in (
        "'inflection','derivation'", "'lead_opposite'", "'lead_other'")), (1287, 76, 23))
    chk("Ollama calls answered / failed-or-refused", (cnt["ollama_answered"], cnt["ollama_failed"] + cnt["ollama_refused"]), (676, 31))
    chk("Ollama answers by relation inflection/derivation/none", tuple(q("SELECT count(*) FROM ai_call WHERE module='ai_base' AND via=?", "loaded " + r) for r in ("inflection", "derivation", "none")), (196, 191, 289))
    chk("base source structure/ollama/own (surfaces of collection a)", (cnt["source_structure"], cnt["source_ollama"], cnt["source_own"]), (1246, 387, 2217))
    chk("distinct bases of collection a", q("SELECT count(DISTINCT base_id) FROM surface_term WHERE base_id IS NOT NULL AND origin='surface' AND surface_group IN ('behaviour','inner_being_state')"), 2481)
    chk("flags: held pairs (bases) / possible opposites / ai_none / ai_failed", (cnt["flag_held_pair"], cnt["flag_possible_opposite"], cnt["flag_ai_none"], cnt["flag_ai_failed"]), (39, 34, 289, 31))
    chk("possible-opposite flags: recorded on 2026-11-04 / added from the structure control", (q("SELECT count(*) FROM surface_flag WHERE kind='possible_opposite' AND note LIKE 'recorded%'"), q("SELECT count(*) FROM surface_flag WHERE kind='possible_opposite' AND note LIKE 'from the structure control%'")), (22, 12))
    chk("junk terms soft deleted", q("SELECT count(*) FROM surface_term WHERE deleted=1"), 4)
    chk("collections", cnt["collections"], 48)
    chk("recorded judgements of the five runs", cnt["judge_calls"], 4170)
    single = "SELECT count(*) FROM surface_term WHERE base_id=id AND collection_state='{}' AND form='word'"
    single_bases = q("SELECT count(DISTINCT base_id) FROM surface_term t WHERE base_id IS NOT NULL AND (SELECT form FROM surface_term b WHERE b.id=t.base_id)='word' "
                     "AND t.origin='surface' AND t.surface_group IN ('behaviour','inner_being_state')")
    st = dict(conn.execute("SELECT collection_state, count(*) FROM surface_term WHERE collection_state IS NOT NULL AND form='word' GROUP BY 1").fetchall())
    chk("single-word bases", single_bases, 1303)
    chk("tally: placed (placed + shared)", st.get("placed", 0) + st.get("shared", 0), 255)
    chk("tally: shared", st.get("shared", 0), 23)
    chk("tally: set aside", st.get("set_aside", 0), 77)
    chk("tally: listed only (latest run per seed live; the tally file counted 238 with superseded runs)", st.get("listed_only", 0), 235)
    chk("tally: untouched (the tally file said 733)", st.get("untouched", 0), 736)
    chk("every loaded row has a load_ref (rows of the load without one)", q("SELECT count(*) FROM surface_term WHERE run_id=? AND load_ref IS NULL", RUN_ID), 0)
    chk("evaluation cases, all provisional", (cnt["eval_cases"], q("SELECT count(*) FROM surface_eval_case WHERE standing='provisional'")), (252, 252))
    chk("one live link per (collection, term)", q("SELECT count(*) FROM (SELECT 1 FROM collection_link WHERE deleted=0 GROUP BY collection_id, term_id HAVING count(*)>1)"), 0)
    chk("prompts: at most one active per key", q("SELECT count(*) FROM (SELECT 1 FROM cfg_ai_prompt WHERE status='active' GROUP BY prompt_key HAVING count(*)>1)"), 0)
    chk("the active group.word prompt equals the setting the registered tool still reads",
        q("SELECT text FROM cfg_ai_prompt WHERE prompt_key='group.word' AND status='active'") == json.loads(q("SELECT value FROM cfg_setting WHERE key='surface_judge.word_prompt'")), True)
    chk("the active base.word prompt equals the setting the registered tool still reads",
        q("SELECT text FROM cfg_ai_prompt WHERE prompt_key='base.word' AND status='active'") == json.loads(q("SELECT value FROM cfg_setting WHERE key='surface_judge.base_prompt'")), True)
    return checks


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true", help="for a test copy: no rollback snapshot")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    ops = plan_cfg(conn)
    loaded = conn.execute("SELECT count(*) FROM surface_term").fetchone()[0]
    if loaded and not ops:
        print("already applied: surface_term holds rows; nothing changed")
        return 0
    if loaded:
        print("REFUSED: surface_term holds rows but config writes are pending; check the state by hand")
        return 2
    if a.dry_run:
        k = collections.Counter(t for t, _, _, _ in ops)
        print(f"DRY RUN: {len(ops)} cfg write(s) {dict(k)}; the data load is checked by a run on a copy")
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-2361-load', named=True)}")
    try:
        conn.execute("SAVEPOINT surface_cycle_load")
        apply_cfg(conn, ops)
        cnt, tid, state_of = load(conn)
        checks = reconcile(conn, cnt)
        bad = [c for c in checks if not c[3]]
        print("RECONCILIATION")
        for name, got, want, ok in checks:
            print(f"  {'OK ' if ok else 'BAD'} {name}: got {got}, recorded {want}")
        if bad:
            raise RuntimeError(f"{len(bad)} reconciliation check(s) failed; the load is rolled back")
        conn.execute("RELEASE surface_cycle_load")
        conn.commit()
    except Exception:
        conn.execute("ROLLBACK TO surface_cycle_load")
        conn.execute("RELEASE surface_cycle_load")
        raise
    report = ROOT / "Logs" / f"2361-load-reconciliation-{NOW.replace(':', '')}.json"
    report.write_text(json.dumps({"run_id": RUN_ID, "at": NOW, "counts": dict(cnt),
                                  "checks": [{"name": n, "got": g, "recorded": w, "ok": ok} for n, g, w, ok in checks]}, indent=1, default=str), encoding="utf-8")
    print(f"applied (run {RUN_ID}); {len(ops)} cfg write(s); rows loaded {dict(cnt)}; report {report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
