"""surfacestructure.py -- module 2 of 5 of the surface cycle (#2361): matching a surface to a base by the shape of the word.

Rebuilt from the recorded output of 2026-11-04 (the control iba/app ... surface-match-control-v3) because the code that made it was never
kept. It is a pure function of three inputs, all read from the database by the caller: the surfaces (text, group, form), the construct
rules (cfg_base_construct) and the settings (cfg_setting module structure). No file is an input.

The method, as reproduced and checked against the recorded control (see iba/app/tools/temp_2361_structure_test_run.py):
  1. Normalise a surface: lower-case, trim, drop a trailing possessive ('s). A possessive form is not tested itself; it takes the
     result of its normalised twin.
  2. Test every single word (a phrase is not tested). A construct applies when the word ends with its strip text (or starts with its
     prefix) and is longer than it; with undouble the stem must end in a doubled letter and one of them is dropped. The base is the
     stem plus the construct's add text and must be at least structure.min_base_length letters.
  3. A hit is a base that is the normalised form of a surface in the input list and not the word itself. The direction of the construct
     says what the hit is: same (the base keeps the meaning), opposite (a negating affix: a lead, never a base), candidate (another
     prefix: a lead).
  4. Status: derived from a base (a 'same' hit; 'more than one root' when its roots differ), base of other words (a word that is
     the base of another), unmatched. Roots follow the chain of bases down to the word that has no base.
  5. For an unmatched word: starts-with leads (the other words that begin with it, when it has at least
     structure.min_starts_with_length letters), outside-list bases (a base found among the judged surfaces that are not in the input list,
     with its group), and sibling groups: unmatched words and bases of other words that share a computed base of at least
     structure.min_computed_base_length letters (found by the 'same' constructs without requiring the base to be a surface) are
     grouped, groups numbered largest first, then alphabetically by their first word.
  6. Status 2: sibling of another word (computed base) > base found outside the input list (leads only) > unmatched; a base of other
     words that has siblings is 'base of other words, and has siblings'.
Every result is inferential about meaning (B:4): the constructs find the shape, the AI base and the researcher decide the meaning.
"""
from __future__ import annotations

import collections
import json
import re

# the settings this module reads (cfg_setting module structure); a missing one stops the run, nothing falls back to a literal
SETTING_KEYS = ["structure.min_base_length", "structure.min_computed_base_length", "structure.min_starts_with_length",
                "structure.possessive_pattern", "structure.tested_form"]
RESOLVE_ENUM = "cfg_base_construct.result_kind"


class StructureError(Exception):
    pass


STATUS_DERIVED = "derived from a base"
STATUS_DERIVED_MANY = "derived from a base (more than one root)"
STATUS_BASE = "base of other words"
STATUS_BASE_SIB = "base of other words, and has siblings"
STATUS_UNMATCHED = "unmatched"
STATUS_PHRASE = "phrase, not tested"
STATUS_SIBLING = "sibling of another word (computed base)"
STATUS_OUTSIDE = "base found outside the input list (leads only)"


def normalise(surface: str, pattern: str) -> str:
    return re.sub(pattern, "", surface.strip().lower())


def apply_construct(x: str, c: dict, min_base: int):
    """The base a construct gives for the word x, or None when it does not apply or the base is too short. (stem, base)."""
    if c["strip_prefix"]:
        p = c["strip_prefix"]
        if not (x.startswith(p) and len(x) > len(p)):
            return None
        stem = x[len(p):]
        base = stem
    else:
        st = c["strip"]
        if not (x.endswith(st) and len(x) > len(st)):
            return None
        stem = x[:len(x) - len(st)]
        if c["undouble"]:
            if not (len(stem) >= 2 and stem[-1] == stem[-2]):
                return None
            stem = stem[:-1]
        base = stem + c["add"]
    return (stem, base) if len(base) >= min_base else None


def analyse(surfaces: list[dict], constructs: list[dict], outside: dict[str, str], settings: dict | None = None) -> dict:
    """surfaces: [{surface, group, form}] in input order; constructs: dicts with id, kind, direction, strip, add, undouble,
    strip_prefix, ordered by id; outside: {normalised surface: group} of the judged surfaces NOT in the input list.
    Returns {surfaces: [record], hits: [...], sibling_groups: {...}, normalised: {...}, counts: {...}} (the shape of the recorded control)."""
    cfgv = settings or {}
    missing = [k for k in SETTING_KEYS if k not in cfgv]
    if missing:
        raise StructureError(f"cfg_setting missing: {missing}")
    min_base = int(cfgv["structure.min_base_length"])
    min_cb = int(cfgv["structure.min_computed_base_length"])
    min_sw = int(cfgv["structure.min_starts_with_length"])
    pat = cfgv["structure.possessive_pattern"]
    tested_form = cfgv["structure.tested_form"]
    cons = {c["id"]: c for c in constructs}
    order = [c["id"] for c in constructs]
    norm_of = {s["surface"]: normalise(s["surface"], pat) for s in surfaces}
    N = set(norm_of.values())
    is_word = lambda s: s["form"] == tested_form                                  # noqa: E731
    is_tested = lambda s: is_word(s) and norm_of[s["surface"]] == s["surface"].strip().lower()   # noqa: E731

    # ---- step 3: the hits, in input order then construct order
    hits, by_surface = [], collections.defaultdict(list)
    for s in surfaces:
        if not is_tested(s):
            continue
        x = norm_of[s["surface"]]
        for cid in order:
            r = apply_construct(x, cons[cid], min_base)
            if r and r[1] in N and r[1] != x:
                h = {"tested": s["surface"], "construct": cid, "kind": cons[cid]["kind"], "direction": cons[cid]["direction"], "base": r[1]}
                hits.append(h)
                by_surface[x].append(h)
    # a possessive form takes the result of its normalised twin
    twin = {s["surface"]: norm_of[s["surface"]] for s in surfaces}

    def own(s):   # the hits of a surface: its own, or its twin's when it is a possessive form
        return by_surface.get(twin[s["surface"]], []) if is_word(s) else []

    same = {s["surface"]: [h for h in own(s) if h["direction"] == "same"] for s in surfaces}
    derived = {norm_of[s["surface"]] for s in surfaces if same[s["surface"]]}
    pointed = collections.Counter()
    for s in surfaces:
        if is_tested(s):
            for b in {h["base"] for h in same[s["surface"]]}:
                pointed[b] += 1

    def roots(x, seen=()):
        sh = [h for h in by_surface.get(x, []) if h["direction"] == "same"]
        if not sh:
            return {x}
        out = set()
        for b in {h["base"] for h in sh}:
            out |= {b} if b in seen else roots(b, seen + (x,))
        return out

    rec = {}
    for s in surfaces:
        sf, x = s["surface"], norm_of[s["surface"]]
        sh = same[sf]
        bases = sorted({h["base"] for h in sh})
        if not is_word(s):
            status = STATUS_PHRASE
        elif sh:
            status = STATUS_DERIVED_MANY if len(roots(x)) > 1 else STATUS_DERIVED
        elif pointed.get(x, 0):
            status = STATUS_BASE
        else:
            status = STATUS_UNMATCHED
        rec[sf] = {"surface": sf, "group": s["group"], "normalised": x, "form": s["form"], "status": status, "bases": bases,
                   "roots": sorted(roots(x)) if is_word(s) else [], "derived_by": [h["construct"] for h in sh],
                   "pointed_at_by": pointed.get(x, 0),
                   "opposite_leads": [f"{h['base']} ({h['construct']})" for h in own(s) if h["direction"] == "opposite"],
                   "other_leads": [f"{h['base']} ({h['construct']})" for h in own(s) if h["direction"] == "candidate"]}
    # ---- step 5: leads and siblings, for the unmatched
    words = [norm_of[s["surface"]] for s in surfaces if is_word(s)]
    for s in surfaces:
        r = rec[s["surface"]]
        r["starts_with_leads"] = []
        r["base_outside_input"] = []
        if is_tested(s) and r["status"] == STATUS_UNMATCHED:
            x = r["normalised"]
            if len(x) >= min_sw:
                r["starts_with_leads"] = sorted({y for y in words if y.startswith(x) and y != x})
            for cid in order:
                c = cons[cid]
                if c["direction"] != "same":
                    continue
                a = apply_construct(x, c, min_base)
                if a and a[1] in outside and a[1] != x:
                    r["base_outside_input"].append(f"{a[1]} ({cid}, {outside[a[1]]})")
    elig = [s for s in surfaces if is_tested(s) and rec[s["surface"]]["status"] in (STATUS_UNMATCHED, STATUS_BASE)]
    cbmap = collections.defaultdict(set)
    for s in elig:
        x = norm_of[s["surface"]]
        for cid in order:
            c = cons[cid]
            if c["direction"] != "same":
                continue
            a = apply_construct(x, c, min_cb)
            if a and a[1] != x:
                cbmap[a[1]].add((s["surface"], cid))
    shared = {b: v for b, v in cbmap.items() if len({r for r, _ in v}) >= 2}
    parent = {}

    def find(a):
        parent.setdefault(a, a)
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for b, v in shared.items():
        members = sorted({r for r, _ in v})
        for m in members[1:]:
            parent[find(m)] = find(members[0])
    groups = collections.defaultdict(set)
    for b, v in shared.items():
        for r, _ in v:
            groups[find(r)].add(r)
    ordered = sorted(groups.values(), key=lambda m: (-len(m), sorted(m)[0]))
    sibling_groups, member_of = {}, {}
    for i, members in enumerate(ordered, 1):
        gid = f"S{i:04d}"
        cbs = sorted(b for b, v in shared.items() if {r for r, _ in v} & members)
        sibling_groups[gid] = {"roots": sorted(members), "computed_bases": cbs}
        for m in members:
            member_of[m] = gid
    for s in surfaces:
        r = rec[s["surface"]]
        gid = member_of.get(s["surface"], "")
        r["sibling_group"] = gid
        r["sibling_via"] = []
        if gid:
            via = collections.defaultdict(list)
            for b in sibling_groups[gid]["computed_bases"]:
                for rr, cid in sorted(shared[b], key=lambda t: (t[1],)):
                    if rr == s["surface"]:
                        via[b].append(cid)
            r["sibling_via"] = [f"{b} via {cid}" for b in sorted(via) for cid in via[b]]
        # ---- step 6: status 2
        st = r["status"]
        if st == STATUS_UNMATCHED:
            st = STATUS_SIBLING if gid else (STATUS_OUTSIDE if r["base_outside_input"] else STATUS_UNMATCHED)
        elif st == STATUS_BASE and gid:
            st = STATUS_BASE_SIB
        elif st == STATUS_DERIVED_MANY:
            st = STATUS_DERIVED   # version 2 of the control folds the 'more than one root' sub-status back
        r["status_v2"] = st
    # the normalised table: every root (a word with no base of its own) with the words that derive from it
    normalised = collections.defaultdict(set)
    for s in surfaces:
        if is_word(s):
            x = norm_of[s["surface"]]
            member = s["surface"].strip().lower()   # a possessive form is listed by its own text beside its twin
            for rt in (rec[s["surface"]]["roots"] or [x]):
                normalised[rt].add(member)
    normalised = {k: sorted(v) for k, v in sorted(normalised.items())}
    counts = collections.Counter(r["status_v2"] for r in rec.values() if r["form"] == tested_form)
    return {"surfaces": [rec[s["surface"]] for s in surfaces], "hits": hits, "sibling_groups": sibling_groups,
            "normalised": normalised, "counts": dict(counts),
            "roots_before": len(normalised), "roots_after_siblings": len(normalised) - (sum(len(g["roots"]) for g in sibling_groups.values()) - len(sibling_groups))}


# ---------------------------------------------------------------------------------------------------------------------------
# the adapters: everything is read from, and written to, the tables
# ---------------------------------------------------------------------------------------------------------------------------
def read_settings(cfg) -> dict:
    vals = {k: cfg.setting(k) for k in SETTING_KEYS}
    missing = [k for k, v in vals.items() if v is None]
    if missing:
        raise StructureError(f"cfg_setting missing: {missing}")
    return vals


def load_inputs(conn, cfg):
    """(surfaces, constructs, outside) from surface_term and cfg_base_construct. The input list is the live surfaces of
    collection a (the groups of cfg_setting surfaces.scope_groups 'a'), in plain sorted order; outside is the group of every other
    live judged surface that is not in the input list (normalised)."""
    scope = cfg.setting("surfaces.scope_groups")
    if not scope or "a" not in scope:
        raise StructureError("cfg_setting surfaces.scope_groups is missing or has no collection a")
    vals = read_settings(cfg)
    rows = [(r[0], r[1], r[2]) for r in conn.execute(
        "SELECT surface, form, surface_group FROM surface_term WHERE deleted=0 AND origin='surface' AND surface_group IS NOT NULL").fetchall()]
    ins = sorted(({"surface": r[0], "group": r[2], "form": r[1]} for r in rows if r[2] in scope["a"]), key=lambda x: x["surface"])
    n_in = {normalise(x["surface"], vals["structure.possessive_pattern"]) for x in ins}
    outside = {}
    for r in sorted(rows):
        if r[2] not in scope["a"]:
            n = normalise(r[0], vals["structure.possessive_pattern"])
            if n not in n_in:
                outside.setdefault(n, r[2])
    cons = [dict(r) if hasattr(r, "keys") else {"id": r[0], "kind": r[1], "direction": r[2], "strip": r[3], "add": r[4], "undouble": r[5],
                                               "strip_prefix": r[6], "result_kind": r[7]}
            for r in conn.execute("SELECT id, kind, direction, strip, \"add\", undouble, strip_prefix, result_kind FROM cfg_base_construct "
                                  "WHERE inactive=0 ORDER BY id").fetchall()]
    for c in cons:
        c["undouble"] = bool(c["undouble"])
    if not ins:
        raise StructureError("no live surface of collection a in surface_term")
    return ins, cons, outside


def desired_evidence(result: dict, constructs: list[dict]) -> set:
    """The evidence rows the result stands for, as (surface, method, evidence, kind, base_word)."""
    rk = {c["id"]: c["result_kind"] for c in constructs}
    out = set()
    for h in result["hits"]:
        out.add((h["tested"], "structure", h["construct"], rk[h["construct"]], h["base"]))
    for r in result["surfaces"]:
        for e in r["base_outside_input"]:
            m = re.match(r"(.+?) \((\S+?), ", e)
            out.add((r["surface"], "structure", m.group(2), "derivation", m.group(1)))
        for y in r["starts_with_leads"]:
            out.add((y, "structure", "starts_with", "lead_starts_with", r["normalised"]))
        for e in r["sibling_via"]:
            m = re.match(r"(.+?) via (\S+)", e)
            out.add((r["surface"], "sibling", f"{r['sibling_group']}:{m.group(2)}", "derivation", m.group(1)))
    return out


def plan_write(conn, desired: set) -> dict:
    """What a write would change: rows to add and live rows no longer produced (compared as whole evidence keys)."""
    existing = collections.defaultdict(list)
    for rid, sf, method, ev, kind, bw in conn.execute(
            "SELECT d.id, t.surface, d.method, d.evidence, d.kind, d.base_word FROM surface_derivation d JOIN surface_term t ON t.id=d.term_id "
            "WHERE d.deleted=0 AND d.method IN ('structure','sibling')"):
        existing[(sf, method, ev, kind, bw)].append(rid)
    add = sorted(desired - set(existing))
    remove = sorted((k, ids) for k, ids in existing.items() if k not in desired)
    return {"add": add, "remove": remove, "kept": len(set(existing) & desired)}


def write(conn, run_id: str, plan: dict) -> dict:
    """Apply a plan: new evidence rows (accepted 0: the resolve module decides which evidence makes the base), and the rows no longer
    produced set to deleted = 1 (version-aware, as verse_lexical). Nothing is physically deleted."""
    now = __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tid = {r[0]: r[1] for r in conn.execute("SELECT surface, id FROM surface_term WHERE deleted=0")}
    for sf, method, ev, kind, bw in plan["add"]:
        conn.execute("INSERT INTO surface_derivation (term_id, method, evidence, kind, base_word, base_term_id, accepted, run_id, created_by) "
                     "VALUES (?,?,?,?,?,?,0,?,?)", (tid[sf], method, ev, kind, bw, tid.get(bw), run_id, "surface-structure"))
    n_rm = 0
    for key, ids in plan["remove"]:
        for rid in ids:
            conn.execute("UPDATE surface_derivation SET deleted=1, updated_at=?, run_id=? WHERE id=?", (now, run_id, rid))
            n_rm += 1
    return {"added": len(plan["add"]), "superseded": n_rm, "kept": plan["kept"]}
