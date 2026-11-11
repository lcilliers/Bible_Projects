"""collectionexport.py -- the two #2379 CSV views of the surface work, as methods that can be run again on demand (escalation #2393).

Both are views of tables (never an input). Every row is one surface of a base, in one verse of verse_lexical, under one cluster of its Strong's
code, with the collection it belongs to if any:

  members-verses   the surfaces of the members of the collections (tiers of `collection.member_tiers`), with the verse text.
  surfaces         every surface of the groups of `surfaces.export_groups` (and the surfaces not yet grouped), with the collection and tier of
                   each membership it has (blank when none), without the verse text.

In `surfaces` a surface that is a member of a collection under two tiers is written once, with the strongest (core, synonym, opposite); in
`members-verses` each tier is a row. A surface that no verse_lexical row carries is written once with the verse columns blank. In `members-verses` a member surface is the link's own term and the
terms whose base is that term; in `surfaces` the surface takes the collections of the links on its base (or on itself when it has no other base). Its base word is the word of its own base (blank when it has none). The surface text joins to verse_lexical.surface lower-cased and
trimmed (the key surface_term uses). The cluster is every live cluster_strong row of the Strong's code; the subgroup is the surface's own
surface_subgroup row for that cluster and code, and the concept and domain are those of the subgroup (concept_subgroup). Rows are ordered by
surface, Strong's code and verse_lexical row, so a second run on the same tables gives the same file.
"""
from __future__ import annotations

import collections
import csv
import pathlib

VIEWS = ("members-verses", "surfaces")
TIER_ORDER = {"core": 0, "synonym": 1, "opposite": 2}

HEAD_V4 = ["collection_id", "collection", "collection_status", "tier", "base_word", "surface", "surface_group", "origin", "strong", "cluster_code", "cluster_name",
           "subgroup_code", "cluster_subgroup_name", "domain", "concept", "reference", "osisId", "verse_text", "surface_kind", "unit_surface", "unit_role"]
HEAD_V3 = ["surface", "origin", "surface_group", "group_state", "base_id", "base_word", "collection_id", "collection", "tier", "strong", "cluster_code",
           "cluster_name", "subgroup_code", "cluster_subgroup_name", "domain", "concept", "osisId", "surface_kind", "unit_surface", "unit_role"]


class ExportError(Exception):
    """A usage or setting problem; routed as 'refused' and nothing is written."""


def read_settings(cfg) -> dict:
    out = {}
    for key, name in (("collection.member_tiers", "tiers"), ("surfaces.export_groups", "groups"), ("surfaces.exports_root", "root")):
        out[name] = cfg.setting(key)
        if not out[name]:
            raise ExportError(f"cfg_setting {key} is missing")
    return out


def _memberships(conn, terms, tiers, own_link: bool):
    """surface term id -> {(collection id, collection name, status, tier)}. A link reaches the terms whose base is its term, and the term itself when
    it is its own base or has none; with own_link it reaches its own term as well even when that term has another base."""
    links = conn.execute("SELECT c.id, c.name, c.status, l.tier, l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id "
                         f"WHERE l.deleted=0 AND c.deleted=0 AND l.tier IN ({','.join('?' * len(tiers))})", list(tiers)).fetchall()
    of_base = collections.defaultdict(list)
    for t in terms.values():
        if t[5] is not None and t[5] != t[0]:
            of_base[t[5]].append(t[0])
    out = collections.defaultdict(set)
    for cid, cname, status, tier, tid in links:
        reach = of_base.get(tid, []) + ([tid] if own_link or (tid in terms and terms[tid][5] in (None, tid)) else [])
        for sid in reach:
            if sid in terms:
                out[sid].add((cid, cname, status, tier))
    return out


def _lexical(conn, surfaces: set, with_text: bool):
    out = collections.defaultdict(list)
    for r in conn.execute("SELECT lower(trim(vl.surface)), vl.strong, v.osisId, vl.surface_kind, vl.unit_surface, vl.unit_role, vl.id, v.reference, v.text "
                          "FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0"):
        if r[0] in surfaces:
            out[r[0]].append(r if with_text else r[:7] + ("", ""))
    return out


def _placement(conn):
    clusters = collections.defaultdict(list)
    for s, cc in conn.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0 ORDER BY id"):
        clusters[s].append(cc)
    names = dict(conn.execute("SELECT cluster_code, short_name FROM cluster").fetchall())
    concept = {g: (n, d) for g, n, d in conn.execute(
        "SELECT cs.cluster_subgroup_id, n.name, d.name FROM concept_subgroup cs JOIN concept n ON n.id=cs.concept_id "
        "LEFT JOIN concept_domain d ON d.id=n.domain_id WHERE cs.deleted=0 ORDER BY cs.id DESC")}
    sub = {(cc, s, surf): (code, label, *concept.get(gid, ("", ""))) for cc, s, surf, code, label, gid in conn.execute(
        "SELECT ss.cluster_code, ss.strong, ss.surface, g.subgroup_code, g.label, g.id FROM surface_subgroup ss "
        "JOIN cluster_subgroup g ON g.id=ss.cluster_subgroup_id WHERE ss.deleted=0")}
    return clusters, names, sub


def build(conn, view: str, tiers: list, groups: list) -> tuple[list, list]:
    """(header, rows) of one view, from the tables only."""
    if view not in VIEWS:
        raise ExportError(f"-View {view!r} is not one of {', '.join(VIEWS)}")
    terms = {r[0]: r for r in conn.execute("SELECT id, surface, origin, surface_group, group_state, base_id FROM surface_term WHERE deleted=0")}
    verses = view == "members-verses"
    member = _memberships(conn, terms, tiers, own_link=verses)
    scope = sorted(member) if verses else sorted(sid for sid, t in terms.items() if t[3] in groups or t[3] is None)
    lex = _lexical(conn, {terms[sid][1] for sid in scope}, verses)
    clusters, cname, sub = _placement(conn)
    out = []
    for sid in sorted(scope, key=lambda i: (terms[i][1], i)):
        _, surface, origin, group, gstate, base_id = terms[sid]
        base_word = terms[base_id][1] if base_id in terms else ""
        mems = sorted(member.get(sid, []), key=lambda m: (m[1], TIER_ORDER.get(m[3], 9), m[0]))
        if not verses:     # one row for each collection of the surface, with its strongest tier
            mems = list({m[0]: m for m in reversed(mems)}.values())[::-1] or [None]
        for v in sorted(lex.get(surface, []), key=lambda r: (r[1], r[6])) or [None]:
            strong = v[1] if v else ""
            for cc in (clusters.get(strong) if v else None) or [None]:
                sg = sub.get((cc, strong, surface), ("", "", "", ""))
                place = [cc or "", cname.get(cc, "") if cc else "", sg[0], sg[1], sg[3] or "", sg[2] or ""]
                kind = [(v[3] or "") if v else "", (v[4] or "") if v else "", (v[5] or "") if v else ""]
                for m in mems:
                    if verses:
                        out.append([m[0], m[1], m[2], m[3], base_word, surface, group or "", origin, strong] + place +
                                   [(v[7] or "") if v else "", (v[2] or "") if v else "", (v[8] or "") if v else ""] + kind)
                    else:
                        out.append([surface, origin, group or "", gstate or "", base_id if base_id is not None else "", base_word,
                                    m[0] if m else "", m[1] if m else "", m[3] if m else "", strong] + place + [(v[2] or "") if v else ""] + kind)
    return (HEAD_V4 if verses else HEAD_V3), out


def write(path: pathlib.Path, head: list, rows: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(head)
        w.writerows(rows)
