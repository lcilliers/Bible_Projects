"""collectiongroup.py -- the grouping of the surfaces of a collection by their meaning (stage 2; escalation #2509, design v2, approved 2026-11-15).

The researcher's ruling (2026-11-15): the surface groups have nothing to do with the inner being; they are about the meaning of the surface words, which is already in the Strong's meaning, and in
the majority of cases it is a matter of judging the dictionary meaning of the words. So:

  pull(...)    writes a working file with one row for each live row of the collection's index (a member surface, or one Strong's code of a surface already split by code), carrying the dictionary
               evidence of each code (the head sense, the sense tree and the lexicons: lib/layerreading._lexicon), the surface's link in the collection and the count of its occurrences; no verse.
  record(...)  checks the filled file whole and writes it in one savepoint, or refuses all of it: every row answered once; every group a unique name and a definition of its meaning; every group holding
               a surface; a surface set aside (its meaning is not the one the collection gathers) with its reason; a surface answered by code gives every code its own answer. The writes are
               collectionindex.make_group and place: each change a surface_event with the reason "judged from the dictionary meaning" and the file; the nodes of a placed surface take its group.

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


def _tiers(conn, cid: int, term_id: int) -> str:
    r = [x[0] for x in conn.execute("SELECT tier FROM collection_link WHERE deleted=0 AND collection_id=? AND term_id=?", (cid, term_id))]
    if r:
        return ", ".join(sorted(set(r)))
    b = conn.execute("SELECT base_id FROM surface_term WHERE id=?", (term_id,)).fetchone()
    if b and b[0] and b[0] != term_id:
        r = [x[0] for x in conn.execute("SELECT tier FROM collection_link WHERE deleted=0 AND collection_id=? AND term_id=?", (cid, b[0]))]
        return "through its base: " + ", ".join(sorted(set(r))) if r else "through its base"
    return ""


# ══ pull ═══════════════════════════════════════════════════════════════════════════════════════
def pull(conn, cfg, name: str, out_dir: pathlib.Path) -> tuple[pathlib.Path, int]:
    s = settings(cfg)
    try:
        cid, cname = ci._collection(conn, name)
    except ci.IndexError_ as exc:
        raise GroupError(str(exc))
    rows = _index(conn, cid)
    if not rows:
        raise GroupError(f"collection {cname} has no index rows (run Collection-Build.ps1 -Action Index)")
    ci._MEMO = ci.memo_codes(conn, [r[2] for r in rows])
    try:
        return _pull(conn, s, cid, cname, rows, out_dir)
    finally:
        ci._MEMO = None


def _pull(conn, s, cid, cname, rows, out_dir):
    groups = {r[0]: r[1] for r in conn.execute("SELECT id, name FROM collection_subgroup WHERE deleted=0 AND collection_id=? AND status!='retired'", (cid,))}
    wanted = sorted({(r[2] or "").strip().lower() for r in rows})
    counts = {}
    for i in range(0, len(wanted), 500):  # one scan for every count (a lookup for each code would read the whole of verse_lexical each time)
        part = wanted[i:i + 500]
        for surf, code, n in conn.execute("SELECT lower(trim(surface)), strong, count(*) FROM verse_lexical WHERE deleted=0 AND strong IS NOT NULL AND lower(trim(surface)) IN (%s) GROUP BY 1, 2" % ",".join("?" * len(part)), part):
            counts[(surf, code)] = n
    out = []
    for iid, tid, surface, strong, gid, state, reason in rows:
        codes = [strong] if strong else ci._codes(conn, surface)
        ev = {}
        for code in codes:
            lx = lr._lexicon(conn, code, s["evidence_chars"])
            ev[code] = dict(lx, occurrences=counts.get((surface, code), 0))
        sg = conn.execute("SELECT surface_group FROM surface_term WHERE id=?", (tid,)).fetchone()
        fill = {"group": "", "reason": "", "certainty": "decided | uncertain", "uncertain": ""}
        if not strong and len(codes) > 1:
            fill["by_code"] = {c: {"group": "", "reason": ""} for c in codes}
        out.append({"surface": surface, "strong": strong, "link": _tiers(conn, cid, tid), "surface_group": sg[0] if sg else None, "current": {"state": state, "group": groups.get(gid)},
                    "codes": ev, "fill": fill})
    data = {"collection": cname, "pulled": _now(), "asks": s["asks"], "groups": [{"name": n, "definition": ""} for n in sorted(groups.values())], "rows": out}
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"group-{cname}-{_now()[:10].replace('-', '')}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return path, len(out)


# ══ record ═════════════════════════════════════════════════════════════════════════════════════
def _key(surface, strong):
    return ((surface or "").strip().lower(), (strong or None))


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
    index = {_key(r[2], r[3]): r for r in _index(conn, cid)}
    # the groups of the file
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
            errors.append(f"group {gn!r}: its definition (the meaning its surfaces share, from the dictionary) is missing or under {mint} characters")
        gdefs[gn.lower()] = (gn, gd)
    # the rows: each covered once
    answered, plan, held = {}, [], collections.Counter()
    for i, row in enumerate(data.get("rows") or [], 1):
        k = _key(row.get("surface"), row.get("strong"))
        where = f"row {i} ({row.get('surface')}{' ' + row['strong'] if row.get('strong') else ''})"
        if k not in index:
            errors.append(f"{where}: not a live row of the index of {cname}")
            continue
        if k in answered:
            errors.append(f"{where}: answered twice")
            continue
        answered[k] = i
        fill = row.get("fill") or {}
        pairs = []
        by_code = fill.get("by_code")
        if by_code and not k[1]:
            codes = set(ci._codes(conn, k[0]))
            if set(by_code) != codes:
                errors.append(f"{where}: answered by code, every code of the surface needs its own answer ({sorted(codes)})")
            for code, f2 in by_code.items():
                pairs.append((code, f2))
        else:
            pairs.append((k[1], fill))
        for code, f2 in pairs:
            w2 = where + (f" code {code}" if code and not k[1] else "")
            g = (f2.get("group") or "").strip()
            reason = (f2.get("reason") or "").strip()
            if g.lower() in ("set_aside", "set aside", "isolate", "isolated"):
                if len(reason) < minr:
                    errors.append(f"{w2}: a surface set aside gives its reason in words ({minr} characters or more): its meaning is not the one this collection gathers")
                plan.append({"surface": k[0], "strong": code if (code and not k[1]) or k[1] else None, "group": None, "reason": reason})
            else:
                if g.lower() not in gdefs:
                    errors.append(f"{w2}: group {g!r} is not in the file's list of groups")
                else:
                    held[g.lower()] += 1
                plan.append({"surface": k[0], "strong": code if (code and not k[1]) or k[1] else None, "group": gdefs.get(g.lower(), (g, ""))[0], "reason": reason})
            cert = (f2.get("certainty") or "decided").strip().lower()  # an answer by code carries its own certainty; the row's fill is not read for it
            if cert == "uncertain" and len((f2.get("uncertain") or "").strip()) < minr:
                errors.append(f"{w2}: an uncertain placement says what the dictionary leaves open ({minr} characters or more)")
            if cert not in ("decided", "uncertain"):
                errors.append(f"{w2}: certainty is decided or uncertain")
            plan[-1]["uncertain"] = (f2.get("uncertain") or "").strip() if cert == "uncertain" else ""
    missing = [f"{k[0]}{' ' + k[1] if k[1] else ''}" for k in index if k not in answered]
    if missing:
        errors.append(f"{len(missing)} rows of the index are not answered: {', '.join(missing[:12])}{' ...' if len(missing) > 12 else ''}")
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
            why = f"{gd} [judged from the dictionary meaning, {file_name or 'file'}, run {run_id}]"
            if r is None:
                gid_of[low] = ci.make_group(conn, run_id, cname, gn, why)["id"]
                res["groups_made"] += 1
            else:
                gid_of[low] = r[0]
                if (r[1] or "") != why:
                    conn.execute("UPDATE collection_subgroup SET note=?, updated_at=?, run_id=? WHERE id=?", (why, _now(), run_id, r[0]))
                    ci._event(conn, run_id, "collection_subgroup", r[0], "subgroup_define", "note", (r[1] or "")[:200], gd[:200], f"the meaning of the group, from the dictionary: {gn}")
                    res["groups_redefined"] += 1
        for p in plan:
            cur = conn.execute("SELECT i.subgroup_id, i.state FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.collection_id=? AND t.surface=? AND i.strong IS ?",
                               (cid, p["surface"], p["strong"])).fetchone()
            want_gid = gid_of.get(p["group"].lower()) if p["group"] else None
            state = "placed" if p["group"] else "isolated"
            reason = (("[uncertain] " + p["uncertain"] + ": ") if p["uncertain"] else "") + (p["reason"] or f"judged from the dictionary meaning ({file_name or 'file'}, run {run_id})")
            if cur and cur[1] == state and cur[0] == want_gid:
                res["unchanged"] += 1
                continue
            ci.place(conn, run_id, cname, p["group"], [p["surface"]], p["strong"], reason, isolate=not p["group"])
            res["placed" if p["group"] else "set_aside"] += 1
        for gr in conn.execute("SELECT id, name FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND status!='retired'", (cid,)).fetchall():
            if gr[0] not in gid_of.values() and not conn.execute("SELECT 1 FROM collection_subgroup_surface WHERE deleted=0 AND subgroup_id=?", (gr[0],)).fetchone():
                conn.execute("UPDATE collection_subgroup SET deleted=1, updated_at=?, run_id=? WHERE id=?", (_now(), run_id, gr[0]))
                ci._event(conn, run_id, "collection_subgroup", gr[0], "subgroup_retire", "deleted", "0", "1", f"the group {gr[1]} holds no surface after the grouping by meaning")
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
    L = [f"# Subgroups of the collection {cname}", "", "Grouped by the dictionary meaning of the surface words (stage 2). Read-only view of the tables.", ""]
    for gid, gname, note in conn.execute("SELECT id, name, note FROM collection_subgroup WHERE collection_id=? AND deleted=0 AND status!='retired' ORDER BY name", (cid,)).fetchall():
        L += [f"## {gname}", "", f"Meaning: {note}", ""]
        for surface, strong, reason in conn.execute("SELECT t.surface, i.strong, i.reason FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.subgroup_id=? "
                                                    "ORDER BY t.surface", (gid,)):
            L.append(f"- {surface}{' (' + strong + ')' if strong else ''}" + (f": {reason}" if (reason or "").startswith("[uncertain]") else ""))
        L.append("")
    aside = conn.execute("SELECT t.surface, i.strong, i.reason FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.collection_id=? AND i.state='isolated' ORDER BY t.surface", (cid,)).fetchall()
    L += ["## Set aside (the meaning is not the one this collection gathers)", ""] + ([f"- {a[0]}{' (' + a[1] + ')' if a[1] else ''}: {a[2]}" for a in aside] or ["- none"]) + [""]
    un = conn.execute("SELECT t.surface, i.strong FROM collection_subgroup_surface i JOIN surface_term t ON t.id=i.term_id WHERE i.deleted=0 AND i.collection_id=? AND i.state='unplaced' ORDER BY t.surface", (cid,)).fetchall()
    L += ["## Not yet placed", ""] + ([f"- {a[0]}{' (' + a[1] + ')' if a[1] else ''}" for a in un] or ["- none"]) + [""]
    return L
