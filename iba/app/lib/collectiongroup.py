"""collectiongroup.py -- the grouping of the surfaces of a collection into subgroups by their meaning in context (stage 2; escalation #2509, reshaped by #2526, 2026-11-21).

The researcher's rulings: the unit that is grouped is the SURFACE, the ESV word (#2463 v16); membership of the collection is settled and is not re-judged (#2515 v20); the basis is the meaning of
the surface in context, recognising that a surface may carry a hidden meaning in the different Strong's codes used for it (#2526 Q3, 2026-11-21); the subgroups have nothing to do with the inner
being, a concept (a behaviour) comes into play only in stage 4 (#2526 Q5). So:

  pull(...)    writes a working file with ONE ROW FOR EACH SURFACE of the collection (never one for each Strong's code): the surface, its word family, its link in the collection, its occurrences,
               its Strong's codes with their counts and the dictionary sense of each as a pointer, a spread of its verses with the text (the meaning in context), and, where stage 1 has been
               recorded, the stage 1 observations of the surface.
  record(...)  checks the filled file whole and writes it in one savepoint, or refuses all of it: every surface answered once; every subgroup a unique name and a definition of the meaning its
               surfaces share; every subgroup holding a surface; a surface is placed WHOLE in one subgroup (never split by code); a surface plainly not a member in meaning is set aside with its
               reason, to be moved out of the collection by the change procedure. The writes are collectionindex.make_group and place: each change a surface_event with its reason; the nodes of a
               placed surface take its subgroup.

The tunable values are cfg_setting group.reading; the code holds none of them. Nothing here judges what a word does for the inner being.
"""
from __future__ import annotations

import collections
import datetime
import json
import pathlib

from . import collectionindex as ci
from . import layerreading as lr

WHO = "Claude"


class GroupError(Exception):
    """A usage or setting problem; routed as 'refused' and nothing is written."""


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def settings(cfg) -> dict:
    s = cfg.setting("group.reading")
    if not s:
        raise GroupError("cfg_setting group.reading is missing")
    return s


def _index(conn, cid: int):
    return conn.execute(
        "SELECT i.id, i.term_id, t.surface, i.strong, i.subgroup_id, i.state, i.reason FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id "
        "WHERE i.deleted=0 AND i.collection_id=? ORDER BY t.surface, i.strong", (cid,)).fetchall()


def _surfaces(conn, cid: int, cname: str) -> list:
    """The live index rows of a collection, one for each surface. A row split by Strong's code is a leftover of the retired grouping by code (#2509 v5): the grouping is by surface, so it is refused."""
    rows = _index(conn, cid)
    if not rows:
        raise GroupError(f"collection {cname} has no index rows (run Collection-Build.ps1 -Action Index)")
    split = sorted({r[2] for r in rows if r[3]})
    if split:
        raise GroupError(f"collection {cname}: {len(split)} surfaces are split by Strong's code in the index ({', '.join(split[:8])}); the grouping is by surface since #2526 (a surface is placed whole). "
                         "Reset the index of the collection (Collection-Build.ps1 -Action Index) before grouping")
    return rows


def _tiers(conn, cid: int, term_id: int) -> str:
    r = [x[0] for x in conn.execute("SELECT tier FROM collection_link WHERE deleted=0 AND collection_id=? AND term_id=?", (cid, term_id))]
    if r:
        return ", ".join(sorted(set(r)))
    b = conn.execute("SELECT base_id FROM surface_term WHERE id=?", (term_id,)).fetchone()
    if b and b[0] and b[0] != term_id:
        r = [x[0] for x in conn.execute("SELECT tier FROM collection_link WHERE deleted=0 AND collection_id=? AND term_id=?", (cid, b[0]))]
        return "through its base: " + ", ".join(sorted(set(r))) if r else "through its base"
    return ""


def _spread(by_code: dict, n: int) -> list:
    """Up to n occurrences, taken from the commonest code first and round and round, so that every code the surface carries is seen in a verse before one code is seen twice."""
    order = sorted(by_code, key=lambda c: -len(by_code[c]))
    out, i = [], 0
    while len(out) < n and any(i < len(by_code[c]) for c in order):
        for c in order:
            if i < len(by_code[c]) and len(out) < n:
                out.append((c, by_code[c][i]))
        i += 1
    return out


def _stage1(conn, cid: int, cap: int) -> dict:
    """The stage 1 observations of each surface of the collection (the word-sense answers of step S1), read from the ledger: {surface: [{strong, text}]}."""
    out = collections.defaultdict(list)
    for lid, subject in conn.execute("SELECT id, subject FROM collection_layer_item WHERE deleted=0 AND collection_id=? AND step=? AND observation_id IS NOT NULL", (cid, lr.LEXICAL_STEP)).fetchall():
        surface, _, strong = subject.rpartition("|")
        for (txt,) in conn.execute("SELECT obs_text FROM ib_observation WHERE deleted=0 AND stable_key LIKE ?", (f"layer:{lid}:%",)).fetchall():
            out[surface.strip().lower()].append({"strong": strong, "text": (txt or "")[:cap]})
    return out


# ══ pull ═══════════════════════════════════════════════════════════════════════════════════════
def pull(conn, cfg, name: str, out_dir: pathlib.Path) -> tuple[pathlib.Path, int]:
    s = settings(cfg)
    try:
        cid, cname = ci._collection(conn, name)
    except ci.IndexError_ as exc:
        raise GroupError(str(exc))
    rows = _surfaces(conn, cid, cname)
    return _pull(conn, s, cid, cname, rows, out_dir)


def _pull(conn, s, cid, cname, rows, out_dir):
    groups = {r[0]: r[1] for r in conn.execute("SELECT id, name FROM collection_subgroup WHERE deleted=0 AND collection_id=? AND status!='retired'", (cid,))}
    wanted = sorted({(r[2] or "").strip().lower() for r in rows})
    occ = collections.defaultdict(lambda: collections.defaultdict(list))  # surface -> code -> [(verse_id, vl_id)]
    for i in range(0, len(wanted), 500):  # one scan for every occurrence (a lookup for each surface would read the whole of verse_lexical each time)
        part = wanted[i:i + 500]
        for surf, code, vid, vlid in conn.execute("SELECT lower(trim(surface)), strong, verse_id, id FROM verse_lexical WHERE deleted=0 AND strong IS NOT NULL AND lower(trim(surface)) IN (%s) ORDER BY verse_id" % ",".join("?" * len(part)), part):
            occ[surf][code].append((vid, vlid))
    picks = {r[2].strip().lower(): _spread(occ[r[2].strip().lower()], s["sample_verses"]) for r in rows}
    vids = sorted({o[1][0] for p in picks.values() for o in p})
    verse = {}
    for i in range(0, len(vids), 500):
        part = vids[i:i + 500]
        for vid, ref, text in conn.execute("SELECT id, reference, text FROM verse WHERE id IN (%s)" % ",".join("?" * len(part)), part):
            verse[vid] = (ref, text or "")
    base = {}
    for tid, surf, bsurf in conn.execute("SELECT t.id, t.surface, b.surface FROM surface_term t LEFT JOIN surface_term b ON b.id=t.base_id WHERE t.id IN (%s)" % ",".join("?" * len(rows)), [r[1] for r in rows]):
        base[tid] = bsurf or surf
    family = collections.defaultdict(list)
    for r in rows:
        family[base.get(r[1], r[2])].append(r[2])
    st1 = _stage1(conn, cid, s["evidence_chars"])
    out = []
    for iid, tid, surface, strong, gid, state, reason in rows:
        key = surface.strip().lower()
        by_code = occ[key]
        total = sum(len(v) for v in by_code.values())
        ranked = sorted(by_code, key=lambda c: -len(by_code[c]))
        codes = []
        for c in ranked[:s["max_codes_shown"]]:
            lx = lr._lexicon(conn, c, s["evidence_chars"])
            codes.append({"strong": c, "occurrences": len(by_code[c]), "sense_head": lx.get("sense_head"), "meaning_range": lx.get("meaning_range")})
        if len(ranked) > len(codes):
            codes.append({"more_codes": len(ranked) - len(codes), "occurrences": sum(len(by_code[c]) for c in ranked[len(codes):])})
        out.append({"surface": surface, "family": base.get(tid, surface), "family_in_collection": sorted(x for x in family[base.get(tid, surface)] if x != surface),
                    "link": _tiers(conn, cid, tid), "occurrences": total, "codes_total": len(ranked), "codes": codes,
                    "verses": [{"strong": c, "reference": verse.get(vid, ("", ""))[0], "text": verse.get(vid, ("", ""))[1][:s["verse_chars"]]} for c, (vid, _) in picks[key]],
                    "stage1": st1.get(key, []), "current": {"state": state, "group": groups.get(gid)},
                    "fill": {"group": "", "reason": "", "certainty": "decided | uncertain", "uncertain": ""}})
    data = {"collection": cname, "pulled": _now(), "asks": s["asks"], "groups": [{"name": n, "definition": ""} for n in sorted(groups.values())], "rows": out}
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"group-{cname}-{_now()[:10].replace('-', '')}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return path, len(out)


# ══ record ═════════════════════════════════════════════════════════════════════════════════════
def record(conn, cfg, run_id: str, data: dict, keep: bool, file_name: str = "") -> dict:
    s = settings(cfg)
    name = data.get("collection")
    try:
        cid, cname = ci._collection(conn, name)
    except ci.IndexError_ as exc:
        raise GroupError(str(exc))
    ci._MEMO = ci.memo_codes(conn, [r[2] for r in _index(conn, cid)])
    try:
        return _record(conn, cfg, run_id, data, keep, file_name, s, cid, cname)
    finally:
        ci._MEMO = None


def _record(conn, cfg, run_id, data, keep, file_name, s, cid, cname) -> dict:
    minr, mint = s["min_reason_chars"], s["min_text_chars"]
    errors = []
    index = {(r[2] or "").strip().lower(): r for r in _surfaces(conn, cid, cname)}
    # the subgroups of the file
    gdefs, seen = {}, set()
    for i, g in enumerate(data.get("groups") or [], 1):
        gn = (g.get("name") or "").strip()
        gd = (g.get("definition") or "").strip()
        if not gn:
            errors.append(f"group {i}: a name is required")
            continue
        if gn.lower() in seen:
            errors.append(f"group {gn!r}: named twice")
        seen.add(gn.lower())
        if len(gd) < mint:
            errors.append(f"group {gn!r}: its definition (the meaning its surfaces share, read from the surfaces in their verses) is missing or under {mint} characters")
        gdefs[gn.lower()] = (gn, gd)
    # the rows: each surface once, whole
    answered, plan, held = {}, [], collections.Counter()
    for i, row in enumerate(data.get("rows") or [], 1):
        k = (row.get("surface") or "").strip().lower()
        where = f"row {i} ({row.get('surface')})"
        if row.get("strong"):
            errors.append(f"{where}: a surface is placed whole, never by Strong's code (#2526)")
            continue
        if k not in index:
            errors.append(f"{where}: not a surface of the index of {cname}")
            continue
        if k in answered:
            errors.append(f"{where}: answered twice")
            continue
        answered[k] = i
        f2 = row.get("fill") or {}
        if f2.get("by_code"):
            errors.append(f"{where}: an answer by code is not allowed; place the surface whole in one subgroup (its codes are its hidden meanings, recorded in stage 1 and step 1.2)")
            continue
        g = (f2.get("group") or "").strip()
        reason = (f2.get("reason") or "").strip()
        if g.lower() in ("set_aside", "set aside", "isolate", "isolated"):
            if len(reason) < minr:
                errors.append(f"{where}: a surface set aside gives its reason in words ({minr} characters or more): it is plainly not a member in meaning (to be moved out by the change procedure)")
            plan.append({"surface": k, "group": None, "reason": reason})
        else:
            if g.lower() not in gdefs:
                errors.append(f"{where}: group {g!r} is not in the file's list of groups")
            else:
                held[g.lower()] += 1
            plan.append({"surface": k, "group": gdefs.get(g.lower(), (g, ""))[0], "reason": reason})
        cert = (f2.get("certainty") or "decided").strip().lower()
        if cert == "uncertain" and len((f2.get("uncertain") or "").strip()) < minr:
            errors.append(f"{where}: an uncertain placement says what is left open ({minr} characters or more)")
        if cert not in ("decided", "uncertain"):
            errors.append(f"{where}: certainty is decided or uncertain")
        plan[-1]["uncertain"] = (f2.get("uncertain") or "").strip() if cert == "uncertain" else ""
    missing = [k for k in index if k not in answered]
    if missing:
        errors.append(f"{len(missing)} surfaces are not answered: {', '.join(missing[:12])}{' ...' if len(missing) > 12 else ''}")
    empty = [gn for low, (gn, _) in gdefs.items() if not held[low]]
    if empty:
        errors.append(f"groups that hold no surface: {', '.join(empty)}")
    if errors:
        raise GroupError("the file is refused, nothing written; problems:\n  " + "\n  ".join(errors))
    conn.execute("SAVEPOINT group_record")
    res = {"groups_made": 0, "groups_redefined": 0, "groups_retired": 0, "placed": 0, "set_aside": 0, "unchanged": 0}
    try:
        gid_of = {}
        for low, (gn, gd) in gdefs.items():
            r = conn.execute("SELECT id, note FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND lower(name)=?", (cid, low)).fetchone()
            why = f"{gd} [judged from the meaning of the surfaces in context, {file_name or 'file'}, run {run_id}]"
            if r is None:
                gid_of[low] = ci.make_group(conn, run_id, cname, gn, why)["id"]
                res["groups_made"] += 1
            else:
                gid_of[low] = r[0]
                if (r[1] or "") != why:
                    conn.execute("UPDATE collection_subgroup SET note=?, updated_at=?, run_id=? WHERE id=?", (why, _now(), run_id, r[0]))
                    ci._event(conn, run_id, "collection_subgroup", r[0], "subgroup_define", "note", (r[1] or "")[:200], gd[:200], f"the meaning of the subgroup, from its surfaces in context: {gn}")
                    res["groups_redefined"] += 1
        for p in plan:
            cur = index[p["surface"]]
            want_gid = gid_of.get(p["group"].lower()) if p["group"] else None
            state = "placed" if p["group"] else "isolated"
            reason = (("[uncertain] " + p["uncertain"] + ": ") if p["uncertain"] else "") + (p["reason"] or f"judged from the meaning in context ({file_name or 'file'}, run {run_id})")
            if cur[5] == state and cur[4] == want_gid:
                res["unchanged"] += 1
                continue
            ci.place(conn, run_id, cname, p["group"], [p["surface"]], None, reason, isolate=not p["group"])
            res["placed" if p["group"] else "set_aside"] += 1
        for gr in conn.execute("SELECT id, name FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND status!='retired'", (cid,)).fetchall():
            if gr[0] not in gid_of.values() and not conn.execute("SELECT 1 FROM collection_subgroup_surface WHERE deleted=0 AND subgroup_id=?", (gr[0],)).fetchone():
                conn.execute("UPDATE collection_subgroup SET deleted=1, updated_at=?, run_id=? WHERE id=?", (_now(), run_id, gr[0]))
                ci._event(conn, run_id, "collection_subgroup", gr[0], "subgroup_retire", "deleted", "0", "1", f"the subgroup {gr[1]} holds no surface after the grouping by meaning")
                res["groups_retired"] += 1
        conn.execute("RELEASE group_record" if keep else "ROLLBACK TO group_record")
        if not keep:
            conn.execute("RELEASE group_record")
    except Exception:
        conn.execute("ROLLBACK TO group_record")
        conn.execute("RELEASE group_record")
        raise
    return res


# ══ the scrutiny report ═══════════════════════════════════════════════════════════════════════
def report_lines(conn, name: str) -> list[str]:
    cid, cname = ci._collection(conn, name)
    L = [f"# Subgroups of the collection {cname}", "", "Grouped by the meaning of the surface words in context (stage 2); each surface placed whole. Read-only view of the tables.", ""]
    for gid, gname, note in conn.execute("SELECT id, name, note FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND status!='retired' ORDER BY name", (cid,)).fetchall():
        L += [f"## {gname}", "", f"Meaning: {note}", ""]
        for surface, reason in conn.execute("SELECT t.surface, i.reason FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.subgroup_id=? ORDER BY t.surface", (gid,)):
            L.append(f"- {surface}" + (f": {reason}" if (reason or "").startswith("[uncertain]") else ""))
        L.append("")
    aside = conn.execute("SELECT t.surface, i.reason FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.collection_id=? AND i.state='isolated' ORDER BY t.surface", (cid,)).fetchall()
    L += ["## Set aside (plainly not a member in meaning; to be moved out by the change procedure)", ""] + ([f"- {a[0]}: {a[1]}" for a in aside] or ["- none"]) + [""]
    un = conn.execute("SELECT t.surface FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.collection_id=? AND i.state='unplaced' ORDER BY t.surface", (cid,)).fetchall()
    L += ["## Not yet placed", ""] + ([f"- {a[0]}" for a in un] or ["- none"]) + [""]
    return L
