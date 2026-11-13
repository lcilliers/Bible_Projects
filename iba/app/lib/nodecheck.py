"""nodecheck.py -- the node and observation checker (escalation #2484): every live node and live observation against the node rules
(cfg_behaviour_rule `nodes-index-the-collection-and-comply-with-the-node-rules` and `observations-are-founded-unique-and-fit-the-node-rules`),
listed by the check it fails, with counts and every row. Reads only: nothing is written to a table.

Each check is a statement of one part of the rules, answered from the stored rows. A finding says what is wrong or missing, never what to do; where a
finding is a candidate that needs a reading (a repeat of the verse text, a role, a supported surface) it says so and does not judge. The member surfaces of
the live collections are read by the shared reader (collectionexport._memberships: own row, else base), so the checker and the exports agree.

Checks (key, rule, what is listed):
  N-no-live-observation      B:130  a live node whose observation is deleted or missing
  N-no-surface               B:130  a live node with no surface
  N-no-occurrence            B:130  a live node with no verse_lexical_id
  N-occurrence-mismatch      B:130  a node whose surface, Strong's code, morph code or verse differs from its verse_lexical row
  N-no-strong / N-no-morph   B:130  a node with no Strong's code / morph code
  N-no-role                  B:130  a node that names a word and has no role, or a role outside the enum
  N-out-of-scope             B:130  a live node on a verse that holds no member surface of a live collection
  N-no-collection            B:130  an in-scope node with no collection: of a collection surface (derivable) or of another surface (supportive: what its observation offers)
  N-collection-disagrees     B:130  a node whose collection is not the one collection of its surface, or is not a live collection
  N-duplicate                B:130  a live node whose indexing columns equal those of another live node of the same observation
  O-no-live-node             B:131  a live observation with no live node
  O-not-tied                 B:131  an observation none of whose live nodes has a surface (malformed: not tied to a surface)
  O-no-role-node             B:131  an observation with no node of role characteristic, qualifier or standalone
  O-duplicate-text           B:131  two or more live observations with the same text
  O-no-collection            B:131  an observation none of whose live nodes carries a collection (not discoverable through a collection)
  O-verse-copy               B:131  candidate: an observation repeating more than max_verse_words_copied consecutive words of a verse of its nodes (to be read)
  O-out-of-scope             B:131  an observation all of whose live nodes are out of scope
  C-surface-no-node          B:130  a member surface of a live collection with no live node (rule: every collection surface has at least one finding)
"""
from __future__ import annotations

import collections
import json
import re

from . import collectionexport as cx

CHECKS = [
    ("N-no-live-observation", "B:130", "live node whose observation is deleted or missing"),
    ("N-no-surface", "B:130", "live node with no surface"),
    ("N-no-occurrence", "B:130", "live node with no verse_lexical_id"),
    ("N-occurrence-mismatch", "B:130", "node whose surface, Strong's code, morph code or verse differs from its verse_lexical row"),
    ("N-no-strong", "B:130", "live node with a surface and no Strong's code"),
    ("N-no-morph", "B:130", "live node with a surface and no morph code"),
    ("N-no-role", "B:130", "node that names a word and has no role, or a role outside cfg_enum observation_role"),
    ("N-out-of-scope", "B:130", "live node on a verse that holds no member surface of a live collection"),
    ("N-no-collection", "B:130", "in-scope node with no collection (collection surface: derivable; other surface: what its observation offers)"),
    ("N-collection-disagrees", "B:130", "node whose collection is not the one collection of its surface, or is not a live collection"),
    ("N-duplicate", "B:130", "live node with the same indexing columns as another live node of its observation"),
    ("O-no-live-node", "B:131", "live observation with no live node"),
    ("O-not-tied", "B:131", "observation none of whose live nodes has a surface (malformed: not tied to a surface)"),
    ("O-no-role-node", "B:131", "observation with no node of role characteristic, qualifier or standalone"),
    ("O-duplicate-text", "B:131", "live observations with the same text"),
    ("O-no-collection", "B:131", "observation none of whose live nodes carries a collection (not discoverable through a collection)"),
    ("O-verse-copy", "B:131", "candidate, to be read: observation repeating more than max_verse_words_copied consecutive words of a verse of its nodes"),
    ("O-out-of-scope", "B:131", "observation all of whose live nodes are out of scope"),
    ("C-surface-no-node", "B:130", "member surface of a live collection with no live node"),
]
HEAD = ["node_id", "observation_id", "verse", "surface", "detail"]
_WORD = re.compile(r"[a-z0-9']+")


def _words(text: str) -> list[str]:
    return _WORD.findall((text or "").lower())


def _norm(text: str) -> str:
    return " ".join(_words(text))


def _setting(conn, key, default=None):
    r = conn.execute("SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
    if r is None:
        return default
    v = r[0]
    try:
        return json.loads(v) if isinstance(v, str) else v
    except ValueError:
        return v


def run(conn) -> dict:
    """{"findings": {check key: [row, ...]}, "counts": {...}, "totals": {...}}; a row is (node_id, observation_id, verse, surface, detail)."""
    q = lambda sql, *p: conn.execute(sql, p).fetchall()  # noqa: E731
    tiers = _setting(conn, "collection.member_tiers", ["core", "synonym", "opposite", "gathered", "phrase"])
    max_copy = int(((_setting(conn, "reading.observation_items", {}) or {}).get("max_verse_words_copied")) or 7)
    roles_ok = {r[0] for r in q("SELECT value FROM cfg_enum WHERE name='observation_role' AND inactive=0")}
    relevant = {"characteristic", "qualifier", "standalone"}
    f = {k: [] for k, _, _ in CHECKS}

    # members: surface text -> live collection ids, by the shared reader
    terms = {r[0]: tuple(r) for r in q("SELECT id, surface, origin, surface_group, group_state, base_id FROM surface_term WHERE deleted=0")}
    live_cols = {r[0]: r[1] for r in q("SELECT id, name FROM collection WHERE deleted=0 AND status='confirmed'")}
    mem = cx._memberships(conn, terms, tiers, own_link=True)
    surf_cols = collections.defaultdict(set)
    for sid, ms in mem.items():
        for cid, _, status, _ in ms:
            if cid in live_cols and status == "confirmed":
                surf_cols[(terms[sid][1] or "").strip().lower()].add(cid)
    group_of = {}
    for t in terms.values():
        group_of.setdefault((t[1] or "").strip().lower(), t[3])

    # scope: the verses that hold an occurrence of a member surface
    scope = set()
    for s, osis in q("SELECT lower(trim(vl.surface)), v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0"):
        if s in surf_cols:
            scope.add(osis)

    obs = {r[0]: r for r in q("SELECT id, stage, obs_text, deleted FROM ib_observation")}
    nodes = q("SELECT id, observation_id, verse_reference, surface, strong, morph_code, role, verse_lexical_id, collection_id FROM ib_node WHERE deleted=0")
    vl = {r[0]: r for r in q("SELECT vl.id, v.osisId, lower(trim(vl.surface)), vl.strong, vl.morph_code FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
                             "WHERE vl.id IN (SELECT verse_lexical_id FROM ib_node WHERE deleted=0 AND verse_lexical_id IS NOT NULL)")}
    by_obs = collections.defaultdict(list)
    for n in nodes:
        by_obs[n[1]].append(n)
    node_surf = collections.Counter((n[3] or "").strip().lower() for n in nodes if (n[3] or "").strip())

    def add(key, n, detail, oid=None):
        f[key].append((n[0] if n else None, n[1] if n else oid, n[2] if n else None, n[3] if n else None, detail))

    seen = collections.defaultdict(list)
    for n in nodes:
        nid, oid, verse, surface, strong, morph, role, vlid, cid = n
        s = (surface or "").strip().lower()
        o = obs.get(oid)
        if o is None or o[3]:
            add("N-no-live-observation", n, "observation " + ("missing" if o is None else "deleted"))
        if not s:
            add("N-no-surface", n, "")
        else:
            if not strong:
                add("N-no-strong", n, "")
            if not morph:
                add("N-no-morph", n, "")
            if not role:
                add("N-no-role", n, "no role")
            elif role not in roles_ok:
                add("N-no-role", n, f"role {role!r} is not in observation_role")
        if vlid is None:
            add("N-no-occurrence", n, "")
        else:
            r = vl.get(vlid)
            if r is None:
                add("N-occurrence-mismatch", n, f"verse_lexical {vlid} is missing")
            else:
                bad = []
                if s and r[2] != s:
                    bad.append(f"surface {s!r} vs {r[2]!r}")
                if strong and r[3] and strong != r[3]:
                    bad.append(f"strong {strong} vs {r[3]}")
                if morph and r[4] and morph != r[4]:
                    bad.append(f"morph {morph} vs {r[4]}")
                if verse and r[1] != verse:
                    bad.append(f"verse {verse} vs {r[1]}")
                if bad:
                    add("N-occurrence-mismatch", n, "; ".join(bad))
        inscope = verse in scope
        if not inscope:
            add("N-out-of-scope", n, "")
        cs = surf_cols.get(s, set())
        if cid is not None and cid not in live_cols:
            add("N-collection-disagrees", n, f"collection {cid} is not a live collection")
        elif cid is not None and cs and cid not in cs:
            add("N-collection-disagrees", n, f"collection {cid} but the surface is in {sorted(cs)}")
        elif cid is None and s and inscope:
            if cs:
                add("N-no-collection", n, f"collection surface: derivable, the surface is in {sorted(cs)}")
            else:
                sib = {x[8] for x in by_obs[oid] if x[8] is not None and x[2] == verse}
                sib_any = {x[8] for x in by_obs[oid] if x[8] is not None}
                grp = group_of.get(s) or "no surface_term row"
                where = (f"same verse: {sorted(sib)}" if sib else f"other verse of the observation: {sorted(sib_any)}" if sib_any else "no node of the observation carries a collection")
                add("N-no-collection", n, f"supportive ({grp}); {where}")
        seen[(oid, verse, vlid, s, strong, cid)].append(n)
    for key, grp in seen.items():
        if len(grp) > 1:
            first = min(x[0] for x in grp)
            for n in grp:
                if n[0] != first:
                    add("N-duplicate", n, f"same indexing columns as node {first}")

    texts = collections.defaultdict(list)
    vtext = {r[0]: r[1] for r in q("SELECT osisId, text FROM verse")}
    for oid, o in obs.items():
        if o[3]:
            continue
        ns = by_obs.get(oid, [])
        if not ns:
            add("O-no-live-node", None, o[1], oid)
            continue
        texts[_norm(o[2])].append(oid)
        if all(not (n[3] or "").strip() for n in ns):
            add("O-not-tied", ns[0], f"stage {o[1]}; {len(ns)} node(s), none with a surface")
        if not any(n[6] in relevant for n in ns):
            add("O-no-role-node", ns[0], f"stage {o[1]}; roles {sorted({str(n[6]) for n in ns})}")
        if not any(n[8] is not None for n in ns):
            add("O-no-collection", ns[0], f"stage {o[1]}; {len(ns)} node(s), none with a collection")
        if all(n[2] not in scope for n in ns):
            add("O-out-of-scope", ns[0], f"stage {o[1]}")
        ow = _words(o[2])
        if len(ow) > max_copy:
            grams = {tuple(ow[i:i + max_copy + 1]) for i in range(len(ow) - max_copy)}
            for v in {n[2] for n in ns}:
                vw = _words(vtext.get(v, ""))
                vg = {tuple(vw[i:i + max_copy + 1]) for i in range(len(vw) - max_copy)}
                if grams & vg:
                    add("O-verse-copy", ns[0], f"repeats more than {max_copy} consecutive words of {v}")
                    break
    for t, ids in texts.items():
        if t and len(ids) > 1:
            for oid in ids[1:]:
                add("O-duplicate-text", by_obs[oid][0], f"same text as observation {ids[0]}")

    for sid, ms in sorted(mem.items(), key=lambda kv: terms[kv[0]][1] or ""):
        s = (terms[sid][1] or "").strip().lower()
        live = sorted({cid for cid, _, status, _ in ms if cid in live_cols})
        if live and not node_surf.get(s):
            f["C-surface-no-node"].append((None, None, None, terms[sid][1], "collection " + ", ".join(live_cols[c] for c in live)))

    counts = {k: len(v) for k, v in f.items()}
    bad_nodes = {r[0] for k, rows in f.items() if k.startswith("N-") for r in rows if r[0] is not None}
    totals = {"live nodes": len(nodes), "live nodes with a finding": len(bad_nodes), "live nodes with no finding": len(nodes) - len(bad_nodes),
              "live observations": sum(1 for o in obs.values() if not o[3]), "member surfaces": len(surf_cols), "verses in scope": len(scope)}
    return {"findings": f, "counts": counts, "totals": totals}


def report_lines(res: dict, run_id: str = "", stamp: str = "", sample: int = 5) -> list[str]:
    out = ["# Node and observation check", "",
           f"Run {run_id}, {stamp}. Reads only; nothing is written to a table. Each check is a part of behaviour rules B:130 (nodes) and B:131 (observations); a finding "
           "says what is wrong or missing, not what to do. Every row is in the workbook of the same name, one sheet for each check. Candidates marked 'to be read' "
           "need a reading and are not judged here.", "", "## Totals", "", "| | count |", "|---|---|"]
    out += [f"| {k} | {v:,} |" for k, v in res["totals"].items()]
    out += ["", "## Findings by check", "", "| check | rule | what it lists | count |", "|---|---|---|---|"]
    for k, rule, what in CHECKS:
        out.append(f"| {k} | {rule} | {what} | {res['counts'][k]:,} |")
    for k, rule, what in CHECKS:
        rows = res["findings"][k]
        out += ["", f"### {k} ({rule}): {len(rows):,}", "", what]
        if rows:
            out += ["", "| node | observation | verse | surface | detail |", "|---|---|---|---|---|"]
            out += ["| " + " | ".join("" if x is None else str(x).replace("|", "/") for x in r) + " |" for r in rows[:sample]]
            if len(rows) > sample:
                out.append(f"\n... and {len(rows) - sample:,} more in the workbook.")
    return out


def write_workbook(path, res: dict, run_id: str, stamp: str) -> None:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
    wb = Workbook()
    ws = wb.active
    ws.title = "Read me"
    ws.append([f"Node and observation check, run {run_id}, {stamp}. One sheet for each check; each row is a finding, a view of the stored rows. Nothing is written to a table."])
    ws.append([])
    ws.append(["check", "rule", "what it lists", "rows"])
    for k, rule, what in CHECKS:
        ws.append([k, rule, what, res["counts"][k]])
    for k, _, _ in CHECKS:
        w = wb.create_sheet(k[:31])
        w.append(HEAD)
        for r in res["findings"][k]:
            w.append(["" if x is None else x for x in r])
        for c in w[1]:
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = PatternFill("solid", fgColor="305496")
        w.freeze_panes = "A2"
    wb.save(path)
