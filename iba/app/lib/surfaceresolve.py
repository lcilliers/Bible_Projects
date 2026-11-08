"""surfaceresolve -- module 4 of 5 of the surface cycle: the base of every surface, chosen from the evidence (escalation #2361, stage 3).

The structure module (lib/surfacestructure.py) and the AI base step leave EVIDENCE: rows in surface_derivation (structure, sibling,
ollama) and calls in ai_call. This module reads that evidence and the structure result and decides, for every surface of collection a, its
base: surface_term.base_id, base_source and base_state, and which evidence rows are the accepted ones. It reproduces the combined base of the
recorded workbook of 2026-11-04 (structure 1,232 + 14 ambiguous, sibling 89, Ollama 387 answered / 289 none / 31 failed, own 642 + phrases
1,166), checked in iba/app/tools/temp_2361_resolve_test_run.py.

What each term gets (the first offer in setting resolve.order wins; every offer is evidence about shape or meaning, never a verdict, B:4):
  group outside collection a ........... out_of_scope, no base
  a phrase (form is not structure.tested_form) .. phrase_not_tested, its own base
  structure ............................. the structure found ONE base (inflection or derivation): matched_structure; found more than one:
                                          base_ambiguous, no base, nothing accepted (a choice for the AI step or the researcher)
  sibling ............................... shares a computed base with another word: matched_sibling, its own base
  ollama ................................ the AI base call answered with a base of the same root: ai_answered (a base that is not a surface
                                          becomes a term with origin computed); answered "none": ai_none, own base; refused or failed: ai_failed
                                          (own base, tried again by the AI step); no call yet: unmatched, no base (pending)
  own ................................... a word that is itself a base of other words: resolved_own
A term in a protected state (setting resolve.protected_states: confirmed, resolved) is never touched. Reads only tables; writes the base
fields, the accepted flags, own and ollama evidence rows that are missing, computed terms, and a surface_event per change.
"""
from __future__ import annotations

import datetime
import json

from . import surfacestructure as ss

SETTING_KEYS = ["resolve.order", "resolve.ai_module", "resolve.ai_step", "resolve.protected_states"]


class ResolveError(Exception):
    """A setting is missing or an input is unusable: routed as 'refused', nothing written."""


def read_settings(cfg) -> dict:
    vals = {k: cfg.setting(k) for k in SETTING_KEYS}
    missing = [k for k, v in vals.items() if v is None]
    if missing:
        raise ResolveError(f"cfg_setting missing: {missing}")
    if sorted(vals["resolve.order"]) != ["ollama", "own", "sibling", "structure"]:
        raise ResolveError("cfg_setting resolve.order must name structure, sibling, ollama and own, once each")
    return vals


def ai_results(conn, module: str, step: str) -> dict:
    """{term_id: dict(call_id, outcome, relation, base)} the latest call of the AI base step for each surface term."""
    out = {}
    for cid, sid, outcome, result, answer in conn.execute(
            "SELECT id, subject_id, outcome, result, answer FROM ai_call WHERE module=? AND step=? AND subject_kind='surface_term' AND deleted=0 ORDER BY id",
            (module, step)):
        try:
            rel = (json.loads(answer) or {}).get("relation") if answer else None
        except ValueError:
            rel = None
        out[sid] = {"call": cid, "outcome": outcome, "relation": rel, "base": (result or "").strip().lower() or None}
    return out


def decide(term: dict, rec: dict | None, ai: dict | None, vals: dict, scope_a: list, tested_form: str) -> dict:
    """Pure: the decision for one live surface term. term: surface, form, group. rec: its structure record (status_v2, bases) or None.
    Returns {state, source, base (a word or None), ev: ('structure'|'ollama'|'own'|None), call}."""
    if term["group"] not in scope_a:
        return {"state": "out_of_scope", "source": None, "base": None, "ev": None}
    if term["form"] != tested_form:
        return {"state": "phrase_not_tested", "source": "own", "base": term["surface"], "ev": "own"}
    status = rec["status_v2"] if rec else None
    offers = {}
    if status in (ss.STATUS_DERIVED, ss.STATUS_DERIVED_MANY):
        bases = sorted(set(rec["bases"]))
        if len(bases) == 1:
            offers["structure"] = {"state": "matched_structure", "source": "structure", "base": bases[0], "ev": "structure"}
        else:
            return {"state": "base_ambiguous", "source": None, "base": None, "ev": None}
    if status == ss.STATUS_SIBLING:
        offers["sibling"] = {"state": "matched_sibling", "source": "own", "base": term["surface"], "ev": "own"}
    if status in (ss.STATUS_UNMATCHED, ss.STATUS_OUTSIDE):
        if ai is None:
            return {"state": "unmatched", "source": None, "base": None, "ev": None}
        if ai["outcome"] != "answered" or ai["relation"] not in ("inflection", "derivation", "none"):
            return {"state": "ai_failed", "source": "own", "base": term["surface"], "ev": "own", "call": ai["call"]}
        if ai["relation"] == "none" or not ai["base"] or ai["base"] == term["surface"]:
            return {"state": "ai_none", "source": "own", "base": term["surface"], "ev": "own", "call": ai["call"]}
        offers["ollama"] = {"state": "ai_answered", "source": "ollama", "base": ai["base"], "ev": "ollama", "call": ai["call"],
                            "relation": ai["relation"]}
    if status in (ss.STATUS_BASE, ss.STATUS_BASE_SIB):
        offers["own"] = {"state": "resolved_own", "source": "own", "base": term["surface"], "ev": "own"}
    for method in vals["resolve.order"]:
        if method in offers:
            return offers[method]
    return {"state": "unmatched", "source": None, "base": None, "ev": None}


def load(conn, cfg):
    """(vals, terms, structure by surface, ai by term id) from the tables."""
    vals = read_settings(cfg)
    svals = ss.read_settings(cfg)
    surfaces, cons, outside = ss.load_inputs(conn, cfg)
    res = ss.analyse(surfaces, cons, outside, svals)
    scope = cfg.setting("surfaces.scope_groups")
    if not scope or "a" not in scope:
        raise ResolveError("cfg_setting surfaces.scope_groups is missing or has no collection a")
    # corpus surfaces, and (#2388) a computed base whose group is judged and outside collection a: it is out of scope too (a computed base in
    # collection a, or not yet judged, has no structure record and is left as it is)
    terms = [dict(id=r[0], surface=r[1], form=r[2], group=r[3], base_id=r[4], source=r[5], state=r[6], cs=r[7])
             for r in conn.execute("SELECT id, surface, form, surface_group, base_id, base_source, base_state, collection_state, origin FROM surface_term "
                                   "WHERE deleted=0 AND (origin='surface' OR (origin='computed' AND surface_group IS NOT NULL)) ORDER BY id")
             if r[8] == "surface" or r[3] not in scope["a"]]
    return vals, svals, scope["a"], terms, {r["surface"]: r for r in res["surfaces"]}, ai_results(conn, vals["resolve.ai_module"], vals["resolve.ai_step"])


def decisions(conn, cfg):
    """[(term, decision)] for every live surface term not in a protected state, and the count of protected ones."""
    vals, svals, scope_a, terms, recs, ai = load(conn, cfg)
    tested = svals["structure.tested_form"]
    prot = set(vals["resolve.protected_states"])
    out = [(t, decide(t, recs.get(t["surface"]), ai.get(t["id"]), vals, scope_a, tested)) for t in terms if t["state"] not in prot]
    return out, sum(1 for t in terms if t["state"] in prot)


def plan(conn, cfg) -> dict:
    """What a run would change: {'changes': [(term, decision)], 'unchanged': n, 'protected': n, 'counts': {state: n}}."""
    decided, kept = decisions(conn, cfg)
    tid_of = {r[0]: r[1] for r in conn.execute("SELECT surface, id FROM surface_term WHERE deleted=0")}
    changes, same = [], 0
    counts: dict = {}
    for t, d in decided:
        counts[d["state"]] = counts.get(d["state"], 0) + 1
        want_base = tid_of.get(d["base"]) if d["base"] else None
        if d["base"] and want_base is None:
            want_base = "new"        # a computed term is created
        cur = (t["base_id"], t["source"], t["state"])
        if d["base"] == t["surface"]:
            want_base = t["id"]
        cs_ok = d["state"] != "out_of_scope" or t["cs"] in (None, "placed", "listed_only", "set_aside", "shared")  # #2388: out of scope holds no collection_state
        if want_base != "new" and cur == (want_base, d["source"], d["state"]) and cs_ok and _evidence_ok(conn, t["id"], d):
            same += 1
        else:
            changes.append((t, d))
    return {"changes": changes, "unchanged": same, "protected": kept, "counts": counts}


def _live_rows(conn, tid):
    return conn.execute("SELECT id, method, kind, base_word, accepted, ai_call_id FROM surface_derivation WHERE term_id=? AND deleted=0", (tid,)).fetchall()


def _desired_accept(rows, d, tid):
    """{row id: 0/1} for the term's evidence rows under decision d, and whether a row must be added."""
    want = {}
    have = False
    for rid, method, kind, bw, acc, call in rows:
        if method not in ("structure", "ollama", "own", "sibling"):
            continue
        hit = False
        if d["ev"] == "structure":
            hit = method == "structure" and kind in ("inflection", "derivation") and bw == d["base"]
        elif d["ev"] == "ollama":
            hit = method == "ollama" and call == d.get("call") and kind != "own"
        elif d["ev"] == "own":
            hit = method == "own"
        want[rid] = 1 if hit else 0
        have = have or hit
    return want, have


def _evidence_ok(conn, tid, d) -> bool:
    rows = _live_rows(conn, tid)
    want, have = _desired_accept(rows, d, tid)
    if d["ev"] in ("own", "ollama") and not have:
        return False
    cur = {r[0]: r[4] for r in rows}
    return all(cur[k] == v for k, v in want.items())


def write(conn, run_id: str, pl: dict) -> dict:
    """Apply the plan in the caller's transaction. Returns counts."""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    done = {"terms": 0, "computed": 0, "evidence_set": 0, "evidence_added": 0}
    sid = {r[1]: r[0] for r in conn.execute("SELECT id, surface FROM surface_term WHERE deleted=0")}
    for t, d in pl["changes"]:
        base_id = None
        if d["base"]:
            if d["base"] == t["surface"]:
                base_id = t["id"]
            elif d["base"] in sid:
                base_id = sid[d["base"]]
            else:
                cur = conn.execute("INSERT INTO surface_term (surface, form, origin, group_state, base_source, base_state, collection_state, run_id, created_by) "
                                   "VALUES (?, 'word', 'computed', 'unjudged', 'own', 'resolved_own', 'untouched', ?, 'surface-resolve')", (d["base"], run_id))
                base_id = cur.lastrowid
                conn.execute("UPDATE surface_term SET base_id=id WHERE id=?", (base_id,))
                sid[d["base"]] = base_id
                done["computed"] += 1
        rows = _live_rows(conn, t["id"])
        want, have = _desired_accept(rows, d, t["id"])
        for rid, v in want.items():
            if conn.execute("SELECT accepted FROM surface_derivation WHERE id=?", (rid,)).fetchone()[0] != v:
                conn.execute("UPDATE surface_derivation SET accepted=?, updated_at=?, run_id=? WHERE id=?", (v, now, run_id, rid))
                done["evidence_set"] += 1
        if d["ev"] == "own" and not have:
            conn.execute("INSERT INTO surface_derivation (term_id, method, evidence, kind, base_word, base_term_id, accepted, ai_call_id, run_id, created_by) "
                         "VALUES (?, 'own', NULL, 'own', ?, ?, 1, NULL, ?, 'surface-resolve')", (t["id"], t["surface"], t["id"], run_id))
            done["evidence_added"] += 1
        if d["ev"] == "ollama" and not have:
            conn.execute("INSERT INTO surface_derivation (term_id, method, evidence, kind, base_word, base_term_id, accepted, ai_call_id, run_id, created_by) "
                         "VALUES (?, 'ollama', ?, ?, ?, ?, 1, ?, ?, 'surface-resolve')",
                         (t["id"], str(d["call"]), d["relation"], d["base"], base_id, d["call"], run_id))
            done["evidence_added"] += 1
        before = f"{t['state']}:{t['base_id']}"
        conn.execute("UPDATE surface_term SET base_id=?, base_source=?, base_state=?, updated_at=?, run_id=? WHERE id=?",
                     (base_id, d["source"], d["state"], now, run_id, t["id"]))
        if d["state"] == "out_of_scope" and t["cs"] == "untouched":
            conn.execute("UPDATE surface_term SET collection_state=NULL WHERE id=?", (t["id"],))
        if (t["base_id"], t["source"], t["state"]) != (base_id, d["source"], d["state"]):
            conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                         "VALUES ('surface_term',?,'set_base','base_id',?,?,'surface-resolve',?,?,'surface-resolve')",
                         (t["id"], before, f"{d['state']}:{base_id}", f"resolved from {d['ev'] or 'no evidence'}", run_id))
        done["terms"] += 1
    return done
