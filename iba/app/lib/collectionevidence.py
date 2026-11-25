"""collectionevidence.py -- the evidence data of one collection, a list of collections, or a verse or list of verses (escalations #2464, #2467, #2477).

It exposes the entries that exist in the database for every aspect of the words and verses in scope, from the base data through the observations and
the claims into the narrative, and nothing else: no evaluation, no inferred data, no model call, nothing written to a table. Every row is a join
on a stored key. Where a link in the chain has no row, the report says so (an omission shown, not judged); blatant errors are listed apart under
"stored-data faults", each with the rule that found it.

Scope. A collection: its members are those of the CSV exports (collectionexport.py): a live link of a tier in `collection.member_tiers` reaches its own
term and the terms whose base is that term; their occurrences are the live verse_lexical rows whose surface (lower-cased, trimmed, the key surface_term
uses) is a member surface. Links of the other tiers are listed with their reason and do not reach verses here. A verse list: every live verse_lexical
row of each verse (all words), with the collections and tiers each surface belongs to by any live link.

Nodes are never listed alone (#2469): each observation is a card with a Supports list of every node of the observation (in or out of the scope), grouped by verse
in Scripture order with the verse text, each node with its word, Strong's code (native word, transliteration, gloss), role, disposition and cluster; and each Strong's code of the
occurrences has an entry from the stored tables (strong, strong_sense, strong_meaning_tree, strong_related, strong_lsj_parsed, strong_mounce_parsed, cluster_strong,
surface_subgroup (the retired cluster allocation), strong_verse against verse_lexical).

The chain from the occurrences: the observations are the ib_node rows whose verse_lexical_id is one of the occurrences; the claims are the
narrative_claim_source rows that name one of those observations (observation_id) or one of those verses (verse_id); the narrative is the
narrative_claim_telling of those claims, with its section and chapter.

Order. Verses are in Scripture order: book in cfg_book_order, then chapter, then verse (the key of `scripture_key`). The Markdown report and the Excel workbook
are written from this data by lib/collectionevidencereport.py (#2477).
"""
from __future__ import annotations

import collections
import csv
import json
import pathlib
import re

TIER_ORDER = {"core": 0, "synonym": 1, "opposite": 2, "gathered": 3, "possible_opposite": 4, "associated": 5, "phrase": 6, "set_aside": 7}
CHUNK = 800
COLLECTION_COLS = ("id", "name", "status", "core_term_id", "pole_word", "pole_of_pole", "pole_reciprocal", "pole_real_word", "merged_into_id",
                   "run_id", "created_by", "created_at", "updated_at", "load_ref")
REF_FORM = ("a reference is `Book chapter:verse` (for example Pro 6:14), a range `Pro 6:14-16` or across chapters `Pro 6:30-7:2`, a whole chapter `Pro 6`, "
            "a list of verses of one book `Pro 6:14, 16`; each item starts with its book (as the verse table writes it, such as Mat, 1Sa, Phili, or an alias of "
            "narrative.book_alias_map, such as Matthew, 1Sam, Ps) and items are separated by a semicolon")


class EvidenceError(Exception):
    """A usage or setting problem; routed as 'refused' and nothing is written."""


def read_settings(cfg) -> dict:
    out = {}
    for key, name in (("collection.member_tiers", "tiers"), ("surfaces.exports_root", "path"), ("collection.evidence_name", "name"),
                      ("collection.evidence_verse_name", "verse_name"), ("collection.evidence_catalogue_stages", "catalogue_stages"),
                      ("collection.evidence_text_chars", "text_chars"), ("engagement.stage", "engagement_stage"),
                      ("collection.evidence_pairs", "pairs")):
        out[name] = cfg.setting(key)
        if not out[name]:
            raise EvidenceError(f"cfg_setting {key} is missing")
    return out


def _in(conn, sql: str, ids):
    """Run `sql` containing one '{in}' placeholder over ids in chunks; the rows of all chunks."""
    ids = sorted(set(ids))
    rows = []
    for i in range(0, len(ids), CHUNK):
        part = ids[i:i + CHUNK]
        rows += conn.execute(sql.replace("{in}", ",".join("?" * len(part))), part).fetchall()
    return rows


def _dicts(rows, cols):
    return [dict(zip(cols, r)) for r in rows]


class Order:
    """Scripture order: the key of a verse osisId (Matt.11.29) is (book position in cfg_book_order, chapter, verse)."""

    def __init__(self, conn):
        self.book = {b: o for b, o in conn.execute("SELECT book, ordinal FROM cfg_book_order")}

    def key(self, osis: str) -> tuple:
        m = re.fullmatch(r"([^.]+)\.(\d+)\.(\d+)", osis or "")
        return (self.book.get(m.group(1), 999), int(m.group(2)), int(m.group(3))) if m else (999, 0, 0)


# ══ scope: collections ═══════════════════════════════════════════════════════════════════════════
def resolve(conn, names: list[str]) -> list[dict]:
    """The named collections (live rows, by name). A name that is not a collection, or named twice, refuses; nothing is written."""
    seen, out = set(), []
    for raw in names:
        n = (raw or "").strip().lower()
        if not n:
            continue
        if n in seen:
            raise EvidenceError(f"collection {n!r} is named twice")
        seen.add(n)
        r = conn.execute(f"SELECT {', '.join(COLLECTION_COLS)} FROM collection WHERE deleted=0 AND lower(name)=?", (n,)).fetchone()
        if r is None:
            raise EvidenceError(f"{n!r} is not a collection")
        out.append(dict(zip(COLLECTION_COLS, r)))
    if not out:
        raise EvidenceError("-Collection is required: one name or a comma list of names (the core words)")
    return out


MEMBER_TIERS = ("core", "synonym", "opposite", "gathered", "phrase")


def _own_terms(conn, tiers) -> set:
    """The terms with a live link of their own in a member tier. The members are surfaces (#2491): such a term is read by its own links only,
    never also through its base."""
    tiers = list(tiers) or list(MEMBER_TIERS)
    return {r[0] for r in conn.execute(f"SELECT DISTINCT term_id FROM collection_link WHERE deleted=0 AND tier IN ({','.join('?' * len(tiers))})", tiers)}


def _terms(conn):
    terms = {r[0]: r for r in conn.execute("SELECT id, surface, form, origin, surface_group, group_state, base_id, base_source, base_state, collection_state, deleted "
                                           "FROM surface_term")}
    of_base = collections.defaultdict(list)
    for t in terms.values():
        if t[6] is not None and t[6] != t[0]:
            of_base[t[6]].append(t[0])
    return terms, of_base


def build_collection(conn, col: dict, tiers: list, order: Order, lean: bool = False, only_surfaces=None) -> dict:
    """Everything stored for one collection, as lists of dicts, from the tables only. `lean` reads only what the layered reading uses (the links, the member terms and the occurrences);
    the chain of nodes, observations and claims, the phrases and the faults are the evidence report's and are not read (#2538: the read is as targeted as the work in hand).
    `only_surfaces`: the surfaces of one subgroup (researcher 2026-11-24: a subgroup is read in isolation, nothing of the others is read): only their terms and occurrences are read;
    d["all_surfaces"] keeps the surfaces of the whole collection (from the links, no occurrence read) so a word of another subgroup is still typed as a member of the collection."""
    d = {"kind": "collection", "name": col["name"], "collection": col, "tiers": tiers}
    terms, of_base = _terms(conn)
    d["links"] = _dicts(conn.execute(
        "SELECT l.id, l.tier, l.term_id, t.surface, l.shared, l.superseded_by_id, l.reason, l.ai_call_id, l.run_id, l.created_by, l.created_at, l.deleted, l.load_ref "
        "FROM collection_link l LEFT JOIN surface_term t ON t.id=l.term_id WHERE l.collection_id=?", (col["id"],)).fetchall(),
        ("id", "tier", "term_id", "surface", "shared", "superseded_by_id", "reason", "ai_call_id", "run_id", "created_by", "created_at", "deleted", "load_ref"))
    d["links"].sort(key=lambda r: (r["deleted"], TIER_ORDER.get(r["tier"], 9), r["surface"] or "", r["id"]))
    member = {}   # term id -> set of (link id, tier)
    own_terms = _own_terms(conn, tiers)
    for ln in d["links"]:
        if ln["deleted"] or ln["tier"] not in tiers:
            continue
        reach = [s for s in of_base.get(ln["term_id"], []) if s not in own_terms]
        if ln["term_id"] in terms:
            reach.append(ln["term_id"])
        for sid in reach:
            member.setdefault(sid, set()).add((ln["id"], ln["tier"]))
    d["terms"] = []
    for sid in sorted(member, key=lambda i: (terms[i][1], i)):
        t = terms[sid]
        d["terms"].append({"term_id": sid, "surface": t[1], "form": t[2], "origin": t[3], "group": t[4], "group_state": t[5],
                           "base": terms[t[6]][1] if t[6] in terms else None, "base_source": t[7], "base_state": t[8], "collection_state": t[9],
                           "deleted": t[10], "tiers": "/".join(sorted({x[1] for x in member[sid]}, key=lambda x: TIER_ORDER.get(x, 9))),
                           "links": ",".join(str(x) for x in sorted({x[0] for x in member[sid]}))})
    tier_of = collections.defaultdict(set)
    for t in d["terms"]:
        tier_of[t["surface"]].update(t["tiers"].split("/"))
    d["all_surfaces"] = sorted(tier_of)
    surfaces = set(tier_of)
    if only_surfaces is not None:
        surfaces &= set(only_surfaces)
        d["terms"] = [t for t in d["terms"] if t["surface"] in surfaces]
    occ = _occurrences(conn, order, surfaces=surfaces)
    for o in occ:
        o["memb"] = "/".join(sorted(tier_of[o["surface"]], key=lambda x: TIER_ORDER.get(x, 9)))
    occ.sort(key=lambda o: (o["surface"], o["sk"], o["position"] if o["position"] is not None else 0, o["code_ordinal"] or 0, o["vl_id"]))
    d["occurrences"] = occ
    if lean:
        d["phrases"], d["faults"] = [], []
        return d
    _chain(conn, d, order)
    d["phrases"] = _phrases(conn, d)
    d["faults"] = _faults(conn, d, surfaces=surfaces)
    return d


def _phrases(conn, d: dict) -> list[dict]:
    """The live links of tier phrase (attached by the route of their reason, not members): each phrase with its route and the live observation nodes that carry its words."""
    out = []
    for ln in d["links"]:
        if ln["deleted"] or ln["tier"] != "phrase":
            continue
        route = re.split(r"\s+\(Researcher", ln["reason"] or "", maxsplit=1)[0]
        n = conn.execute("SELECT count(*), count(DISTINCT n.observation_id) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
                         "WHERE n.deleted=0 AND o.deleted=0 AND lower(trim(n.surface))=?", ((ln["surface"] or "").strip().lower(),)).fetchone()
        out.append({"link": ln["id"], "term_id": ln["term_id"], "phrase": ln["surface"], "route": route, "nodes": n[0], "observations": n[1], "run": ln["run_id"],
                    "by": ln["created_by"], "created": ln["created_at"]})
    out.sort(key=lambda p: (p["phrase"] or "", p["link"]))
    return out


# ══ scope: verses ════════════════════════════════════════════════════════════════════════════════
# ══ the pairings: what lives with the member words in their verses (#2502) ═══════════════════════
def _morph_class(morph: str, testament: str, table: dict) -> str:
    """A grammar hint from the morph code (the classes are cfg_setting collection.evidence_pairs morph_class): NT the part before the first hyphen, OT the letter after the
    language letter (H or A). A hint only; the morph code itself is shown beside it."""
    if not morph:
        return ""
    if testament == "NT":
        return table.get("NT", {}).get(morph.split("-")[0], "")
    return table.get("OT", {}).get(morph[1:2], "") if len(morph) > 1 else ""


def build_pairs(conn, d: dict, vals: dict, order: Order) -> dict:
    """The base data of layer 2 for one collection (#2502): every live verse_lexical row of every verse that holds a member occurrence, in word order, each typed
    (member, entity, negator, word of another collection, qualifier candidate, connective, other), and the pairings of each member occurrence with the words of its
    verse, with side and distance. Read-only on the tables; nothing is evaluated: a type is a stored field (party_kind, is_negator, the collection of the surface, the
    qualifier subgroup, the morph class) and a distance is a difference of stored positions. Settings: cfg_setting collection.evidence_pairs."""
    P = vals["pairs"]
    terms, of_base = _terms(conn)
    st = list(P["collection_status"])
    cols = {r[0]: r[1] for r in conn.execute(f"SELECT id, name FROM collection WHERE deleted=0 AND status IN ({','.join('?' * len(st))})", st)}
    own = _own_terms(conn, vals["tiers"])
    surf_cols = collections.defaultdict(set)
    surf_cid, text_id = {}, {}
    for cid, tid in conn.execute(f"SELECT collection_id, term_id FROM collection_link WHERE deleted=0 AND tier IN ({','.join('?' * len(vals['tiers']))})", list(vals["tiers"])):
        if cid not in cols:
            continue
        for sid in [s for s in of_base.get(tid, []) if s not in own] + ([tid] if tid in terms else []):
            surf_cols[terms[sid][1]].add(cols[cid])
            surf_cid[terms[sid][1]] = cid
            text_id[terms[sid][1]] = sid
    idx = {(c_, t_, s_): (g_ or "", st_) for c_, t_, s_, g_, st_ in conn.execute(
        "SELECT i.collection_id, i.term_id, i.strong, g.name, i.state FROM collection_subgroup_surface i LEFT JOIN collection_subgroup g ON g.id=i.subgroup_id AND g.deleted=0 WHERE i.deleted=0")}
    mine = {t["surface"] for t in d["terms"]}
    others_own = set(d.get("all_surfaces") or ()) - mine      # the surfaces of the other subgroups of the collection (empty when the whole collection is read)
    q = P["qualifier"]
    qsub = {}
    for strong, label in conn.execute("SELECT ss.strong, cs.label FROM surface_subgroup ss JOIN cluster_subgroup cs ON cs.id=ss.cluster_subgroup_id "
                                      "WHERE ss.deleted=0 AND cs.kind=?", (q["subgroup_kind"],)):
        qsub.setdefault(strong, label)
    occ_ids = {o["vl_id"] for o in d["occurrences"]}
    vids = sorted({o["verse_id"] for o in d["occurrences"]})
    ref = {r[0]: (r[1], r[2]) for r in _in(conn, "SELECT id, reference, osisId FROM verse WHERE id IN ({in})", vids)}
    rows = []
    for r in _in(conn, "SELECT id, verse_id, lower(trim(surface)), strong, morph_code, position, code_ordinal, unit_role, unit_size, surface_kind, unit_surface, "
                       "is_negator, party_kind, role, testament FROM verse_lexical WHERE deleted=0 AND verse_id IN ({in})", vids):
        x = dict(zip(("vl_id", "verse_id", "surface", "strong", "morph", "position", "code_ordinal", "unit_role", "unit_size", "surface_kind", "unit_surface",
                      "is_negator", "party_kind", "role", "testament"), r))
        x["surface"] = x["surface"] or ""
        x["reference"], x["osis"] = ref[x["verse_id"]]
        x["sk"] = order.key(x["osis"])
        x["morph_class"] = _morph_class(x["morph"], x["testament"], P["morph_class"])
        try:
            x["clusters"] = ", ".join(json.loads(x["role"])) if x["role"] else ""
        except (TypeError, ValueError):
            x["clusters"] = str(x["role"] or "")
        x["collections"] = sorted(surf_cols.get(x["surface"], ()))
        key = (surf_cid.get(x["surface"]), text_id.get(x["surface"]))
        hit = idx.get((key[0], key[1], x["strong"])) or idx.get((key[0], key[1], None))
        x["subgroup"], x["index_state"] = hit if hit else ("", "not indexed")     # the subgroup of the surface in its collection (#2503)
        x["member"] = x["surface"] in mine and x["vl_id"] in occ_ids
        why = []
        if x["is_negator"] or any(c in q["cluster_codes"] for c in x["clusters"].split(", ")):
            why.append("negator")
        if x["strong"] in qsub:
            why.append("qualifier subgroup: " + qsub[x["strong"]])
        if x["morph_class"] in q["morph_classes"]:
            why.append("morph: " + x["morph_class"])
        x["qualifier"] = "; ".join(why)
        if x["member"] or x["surface"] in others_own:
            x["type"] = "member of this collection"
        elif x["party_kind"]:
            x["type"] = "entity (" + x["party_kind"] + ")"
        elif "negator" in why:
            x["type"] = "negator"
        elif x["collections"]:
            x["type"] = "word of another collection"
        elif why:
            x["type"] = "qualifier candidate"
        elif "T6" in x["clusters"].split(", "):
            x["type"] = "connective"
        else:
            x["type"] = "other"
        if not x["surface"] and x["type"] != "member of this collection":     # a word folded into the unit of another (surface_kind shared) has no surface of its own: it cannot be a node (a node has one surface), so it is no partner (found by the audit of 2026-11-25: one such word refused a whole 2.1 file)
            x["type"] = "other"
        rows.append(x)
    rows.sort(key=lambda x: (x["sk"], x["position"] if x["position"] is not None else 0, x["code_ordinal"] or 0, x["vl_id"]))
    vl_ids = [x["vl_id"] for x in rows]
    nodes = _in(conn, "SELECT n.verse_lexical_id, n.observation_id, n.role, n.surface, n.strong, n.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
                      "WHERE n.deleted=0 AND o.deleted=0 AND n.verse_lexical_id IN ({in})", vl_ids)
    obs_of = collections.defaultdict(set)
    for n in nodes:
        obs_of[n[0]].add(n[1])
    for x in rows:
        x["obs"] = sorted(obs_of.get(x["vl_id"], ()))
    obs = {r[0]: r for r in _in(conn, "SELECT id, stage, tag, obs_text, nature FROM ib_observation WHERE id IN ({in})", {n[1] for n in nodes})}
    by_vl = {x["vl_id"]: x for x in rows}
    verse_obs = []
    for n in sorted(nodes, key=lambda n: (by_vl[n[0]]["sk"], by_vl[n[0]]["position"] or 0, n[1], n[5])):
        x = by_vl[n[0]]
        o = obs[n[1]]
        verse_obs.append({"reference": x["reference"], "observation": n[1], "stage": o[1], "tag": o[2], "text": o[3], "nature": o[4], "node_surface": n[3], "node_strong": n[4], "node_role": n[2],
                          "vl_id": n[0], "on_member": x["member"], "type": x["type"]})
    bands = P["bands"]
    by_verse = collections.defaultdict(list)
    for x in rows:
        by_verse[x["verse_id"]].append(x)
    pairs = []
    for m in rows:
        if not m["member"]:
            continue
        for r in by_verse[m["verse_id"]]:
            if r["vl_id"] == m["vl_id"] or r["position"] == m["position"] or r["type"] == "other":
                continue
            dist = abs((r["position"] or 0) - (m["position"] or 0))
            band = "adjacent" if dist <= bands["adjacent"] else "near" if dist <= bands["near"] else "far"
            pairs.append({"member": m, "other": r, "distance": dist, "band": band, "side": "before" if (r["position"] or 0) < (m["position"] or 0) else "after"})
    return {"rows": rows, "pairs": pairs, "observations": verse_obs, "settings": P}


def resolve_verses(conn, cfg, text: str, order: Order) -> list[dict]:
    """The verses of a reference list, in Scripture order. A bad item, a book that is not an alias, a verse or chapter not in the verse table, or a verse
    named twice (an overlap) refuses, naming it; nothing is written."""
    from . import narrativeregister as nr
    vx = nr.VerseIndex(cfg)
    items = [x.strip() for x in re.split(r"[;\n]", text or "") if x.strip()]
    if not items:
        raise EvidenceError(f"-Verse is required: {REF_FORM}")
    ids, where = [], {}
    for it in items:
        m = nr._REF_RX.search(it)
        if not m or m.start() != 0 or m.end() != len(it) or not vx.book(m.group("book")):
            raise EvidenceError(f"{it!r} is not a reference this report reads: {REF_FORM}")
        for r in nr.parse_refs(it, vx, follow_ons=False):
            if r.kind == "whole chapter":
                cm = re.fullmatch(r"(\S+) (\d+)", r.normalised)
                code, ch = cm.group(1), int(cm.group(2))
                if (code, ch) not in vx.last_verse:
                    raise EvidenceError(f"{r.normalised!r} (from {it!r}) is not a chapter in the verse table")
                found = [vx.ids[(code, ch, v)] for v in range(1, vx.last_verse[(code, ch)] + 1) if (code, ch, v) in vx.ids]
            elif r.verse_id is None:
                raise EvidenceError(f"{r.normalised!r} (from {it!r}) is not a verse in the verse table")
            else:
                found = [r.verse_id]
            for vid in found:
                if vid in where:
                    raise EvidenceError(f"verse id {vid} is given twice ({where[vid]!r} and {it!r}): the references overlap")
                where[vid] = it
                ids.append(vid)
    rows = _in(conn, "SELECT id, reference, osisId, text, deleted FROM verse WHERE id IN ({in})", ids)
    out = [{"verse_id": r[0], "reference": r[1], "osis": r[2], "text": r[3], "deleted": r[4], "sk": order.key(r[2]), "asked": where[r[0]]} for r in rows]
    out.sort(key=lambda v: v["sk"])
    return out


def build_verses(conn, verses: list[dict], order: Order) -> dict:
    """Everything stored for a verse list: all words of each verse, with the collections and tiers of each surface."""
    d = {"kind": "verse", "name": ", ".join(dict.fromkeys(v["asked"] for v in verses)), "verses": verses}
    terms, of_base = _terms(conn)
    memb = collections.defaultdict(set)
    own_terms = _own_terms(conn, MEMBER_TIERS)
    for cname, tier, tid in conn.execute("SELECT c.name, l.tier, l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id "
                                         "WHERE l.deleted=0 AND c.deleted=0"):
        reach = [s for s in of_base.get(tid, []) if s not in own_terms] + ([tid] if tid in terms else [])
        for sid in reach:
            memb[terms[sid][1]].add((cname, tier))
    ids = {v["verse_id"] for v in verses}
    occ = _occurrences(conn, order, verse_ids=ids)
    for o in occ:
        o["memb"] = "; ".join(f"{c}:{t}" for c, t in sorted(memb.get(o["surface"], ()), key=lambda x: (x[0], TIER_ORDER.get(x[1], 9))))
    occ.sort(key=lambda o: (o["sk"], o["position"] if o["position"] is not None else 0, o["code_ordinal"] or 0, o["vl_id"]))
    d["occurrences"] = occ
    _chain(conn, d, order)
    d["phrases"] = []
    d["faults"] = _faults(conn, d, surfaces=None)
    return d


# ══ the chain from the occurrences to the narrative ══════════════════════════════════════════════
_OCC_SELECT = ("SELECT vl.id, lower(trim(vl.surface)), vl.strong, vl.morph_code, vl.code_ordinal, vl.position, vl.surface_kind, vl.unit_surface, vl.unit_role, "
               "vl.status, vl.verse_id, v.osisId, v.reference, v.text, v.deleted, vl.role, vl.is_negator, vl.party_kind, vl.unit_size "
               "FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0 AND ")
_OCC_COLS = ("vl_id", "surface", "strong", "morph", "code_ordinal", "position", "surface_kind", "unit_surface", "unit_role", "status",
             "verse_id", "osis", "reference", "text", "verse_deleted", "vl_role", "is_negator", "party_kind", "unit_size")


def _occurrences(conn, order: Order, surfaces=None, verse_ids=None) -> list[dict]:
    """The live verse_lexical rows asked for, read by index and never by a pass over the table (#2538, researcher 2026-11-24: the read of the base data is as targeted as possible).
    `surfaces`: the lower-cased surfaces wanted, found by idx_verse_lexical_surface_lc a chunk at a time; with `verse_ids` as well, the rows of those verses only (the surfaces
    are searched, then the verses kept). `verse_ids` alone: the rows of those verses, by idx_verse_lexical_verse_id."""
    rows = []
    if surfaces is not None:
        keep = None if verse_ids is None else set(verse_ids)
        want = sorted(surfaces)
        for i in range(0, len(want), CHUNK):
            part = want[i:i + CHUNK]
            rows += [r for r in conn.execute(_OCC_SELECT + f"lower(trim(vl.surface)) IN ({','.join('?' * len(part))})", part) if keep is None or r[10] in keep]
    else:
        ids = sorted(set(verse_ids or ()))
        for i in range(0, len(ids), CHUNK):
            part = ids[i:i + CHUNK]
            rows += conn.execute(_OCC_SELECT + f"vl.verse_id IN ({','.join('?' * len(part))})", part).fetchall()
    occ = []
    for r in rows:
        o = dict(zip(_OCC_COLS, r))
        o["sk"] = order.key(o["osis"])
        occ.append(o)
    return occ


def _chain(conn, d: dict, order: Order) -> None:
    """Nodes, observations, change history, claim sources, claims, tellings and sections of the occurrences in d."""
    occ = d["occurrences"]
    vl_ids = [o["vl_id"] for o in occ]
    verse_ids = {o["verse_id"] for o in occ}
    sk_of = {o["vl_id"]: o["sk"] for o in occ}
    nodes = _dicts(_in(conn, "SELECT n.id, n.observation_id, n.verse_lexical_id, n.verse_reference, n.surface, n.strong, n.cluster_code, n.cluster_subgroup_code, "
                             "n.role, n.disposition, n.disposition_note, n.source_stage, n.reading_id, n.seq, n.created_at, n.deleted FROM ib_node n "
                             "WHERE n.verse_lexical_id IN ({in})", vl_ids),
                   ("id", "observation_id", "vl_id", "verse_reference", "surface", "strong", "cluster", "subgroup", "role", "disposition", "disposition_note",
                    "source_stage", "reading_id", "seq", "created_at", "deleted"))
    nodes.sort(key=lambda n: (sk_of[n["vl_id"]], n["id"]))
    d["nodes"] = nodes
    obs_ids = {n["observation_id"] for n in nodes}
    obs_cols = ("id", "stage", "tag", "nature", "status", "deleted", "strong", "window", "route", "basis", "obs_text", "setting", "meaning", "implication", "chain", "parties",
                "parts", "revisit_note", "supersedes_observation_id", "run_id", "created_at", "updated_at")
    d["observations"] = sorted(_dicts(_in(conn, f"SELECT {', '.join(obs_cols)} FROM ib_observation WHERE id IN ({{in}})", obs_ids), obs_cols), key=lambda o: o["id"])
    # every node of each observation, in or out of the scope, so a node is always shown with what it supports (#2469)
    allnodes = _dicts(_in(conn, "SELECT id, observation_id, verse_lexical_id, verse_reference, surface, strong, cluster_code, cluster_subgroup_code, role, disposition, "
                                "disposition_note, deleted FROM ib_node WHERE observation_id IN ({in})", obs_ids),
                      ("id", "observation_id", "vl_id", "verse_reference", "surface", "strong", "cluster", "subgroup", "role", "disposition", "disposition_note", "deleted"))
    for n in allnodes:
        n["sk"] = order.key(n["verse_reference"])
    obs_nodes = collections.defaultdict(list)
    for n in sorted(allnodes, key=lambda n: (n["sk"], n["id"])):
        obs_nodes[n["observation_id"]].append(n)
    d["obs_nodes"] = dict(obs_nodes)
    d["scope_vl"] = set(vl_ids)
    osis = {n["verse_reference"] for n in allnodes if n["verse_reference"]} | {o["osis"] for o in occ}
    d["verse_text"] = {r[0]: (r[1], r[2]) for r in _in(conn, "SELECT osisId, reference, text FROM verse WHERE osisId IN ({in})", osis)}
    _strongs(conn, d, {o["strong"] for o in occ if o["strong"]}, {o["strong"] for o in occ if o["strong"]} | {n["strong"] for n in allnodes if n["strong"]})
    d["changes"] = sorted(_dicts(_in(conn, "SELECT id, observation_id, node_id, column_name, old_value, new_value, reason, reading_id, run_id, created_at, created_by "
                                           "FROM ib_observation_change WHERE observation_id IN ({in})", obs_ids),
                                 ("id", "observation_id", "node_id", "column", "old_value", "new_value", "reason", "reading_id", "run_id", "created_at", "created_by")),
                         key=lambda c: c["id"])
    src_cols = ("id", "claim_id", "source_kind", "verse_id", "ref_as_written", "observation_id", "note", "created_by")
    src_sql = "SELECT id, claim_id, source_kind, verse_id, ref_as_written, observation_id, note, created_by FROM narrative_claim_source WHERE {col} IN ({{in}})"
    by_obs = _dicts(_in(conn, src_sql.format(col="observation_id"), obs_ids), src_cols)
    by_verse = _dicts(_in(conn, src_sql.format(col="verse_id"), verse_ids), src_cols)
    for s in by_obs:
        s["via"] = "observation"
    for s in by_verse:
        s["via"] = "verse"
    d["claim_sources"] = sorted(by_obs + by_verse, key=lambda s: (s["via"], s["claim_id"], s["id"]))
    claim_ids = {s["claim_id"] for s in d["claim_sources"]}
    claim_cols = ("id", "claim_ref", "origin", "claim_text", "beyond_text", "i_read", "verdict", "part_verdict", "part_scope", "main_chapter_id", "main_section_id",
                  "in_narrative", "status", "created_by")
    d["claims"] = sorted(_dicts(_in(conn, f"SELECT {', '.join(claim_cols)} FROM narrative_claim WHERE id IN ({{in}})", claim_ids), claim_cols), key=lambda c: c["id"])
    d["tellings"] = sorted(_dicts(_in(conn, "SELECT t.id, t.claim_id, t.section_id, t.passage_id, t.kind, t.part_told, t.status, s.heading, s.level, s.last_version, "
                                            "c.chapter_no, c.title, c.inactive FROM narrative_claim_telling t LEFT JOIN narrative_section s ON s.id=t.section_id "
                                            "LEFT JOIN narrative_chapter c ON c.id=s.chapter_id WHERE t.claim_id IN ({in})", claim_ids),
                                  ("id", "claim_id", "section_id", "passage_id", "kind", "part_told", "status", "heading", "level", "last_version", "chapter_no",
                                   "chapter_title", "chapter_inactive")), key=lambda t: t["id"])
    sec_ids = {t["section_id"] for t in d["tellings"] if t["section_id"] is not None}
    d["sections"] = sorted(_dicts(_in(conn, "SELECT s.id, c.chapter_no, c.title, s.heading, s.level, s.ordinal, s.last_version, s.block_text FROM narrative_section s "
                                            "LEFT JOIN narrative_chapter c ON c.id=s.chapter_id WHERE s.id IN ({in})", sec_ids),
                                  ("id", "chapter_no", "chapter_title", "heading", "level", "ordinal", "last_version", "block_text")), key=lambda s: s["id"])



def _lemma(code: str) -> str:
    """The lemma key of a code: the code without its trailing variant letters (H3820A and H3820B share the tree of H3820)."""
    return re.sub(r"[A-Za-z]+$", "", code or "")


def _strongs(conn, d: dict, full: set, every: set) -> None:
    """The stored data about Strong's codes: a short line for every code in `every` (native word, transliteration, gloss, language, STEP count), and the full entry for
    each code in `full`: sense head, meaning tree of the lemma, related terms, LSJ and Mounce senses (Greek), cluster assignments, the placements of (code, surface) in
    subgroups, and the verses STEP attests against the verse_lexical rows (#2469). Every value is a stored row; nothing is derived."""
    d["strong_short"] = {r[0]: r for r in _in(conn, "SELECT strongNumber, accentedUnicode, stepTransliteration, stepGloss, language, count, origin FROM strong "
                                                    "WHERE strongNumber IN ({in})", every)}
    e = {c: {"code": c, "short": d["strong_short"].get(c)} for c in full}
    for c, head, own in _in(conn, "SELECT strong, head, is_own_lemma FROM strong_sense WHERE deleted=0 AND strong IN ({in})", full):
        e[c]["sense"] = (head, own)
    lemmas = {_lemma(c) for c in full}
    tree = collections.defaultdict(list)
    for lk, code, text, sort, did in _in(conn, "SELECT lemma_key, sense_code, sense_text, sort, id FROM strong_meaning_tree WHERE deleted=0 AND lemma_key IN ({in})", lemmas):
        tree[lk].append((did, sort if sort is not None else 0, code, text))
    for c in full:
        e[c]["lemma"] = _lemma(c)
        trees, prev = [], None
        for did, sort, code, text in sorted(tree.get(_lemma(c), [])):      # stored order; a tree starts where `sort` starts again (several trees share one lemma)
            if prev is None or sort <= prev:
                trees.append([])
            trees[-1].append((did, code, text))
            prev = sort
        e[c]["trees"] = trees
    for key, sql, cols in (
            ("related", "SELECT strong, related_strong, related_form, related_transliteration, related_gloss FROM strong_related WHERE deleted=0 AND strong IN ({in}) ORDER BY id", 4),
            ("lsj", "SELECT strong, sense_label, gloss, note, row_type FROM strong_lsj_parsed WHERE deleted=0 AND strong IN ({in}) ORDER BY id", 4),
            ("mounce", "SELECT strong, mounce_parsed, row_type FROM strong_mounce_parsed WHERE deleted=0 AND strong IN ({in}) ORDER BY id", 2)):
        for c in full:
            e[c][key] = []
        for r in _in(conn, sql, full):
            e[r[0]][key].append(r[1:])
        for c in full:
            e[c][key].sort(key=lambda r: 0)    # stable: keeps the id order of the query within a code
    for c in full:
        e[c]["clusters"] = []
    for r in _in(conn, "SELECT cs.strong, cs.cluster_code, c.short_name, cs.confidence, cs.operation, cs.review_flag, cs.alt_clusters, cs.rationale, cs.source FROM cluster_strong cs "
                       "LEFT JOIN cluster c ON c.cluster_code=cs.cluster_code WHERE cs.deleted=0 AND cs.strong IN ({in}) ORDER BY cs.id", full):
        e[r[0]]["clusters"].append(r[1:])
    place = collections.defaultdict(list)
    for r in _in(conn, "SELECT ss.strong, ss.surface, ss.cluster_code, g.subgroup_code, g.label, g.core_description, ss.status, ss.two_sense, ss.allocated_by, ss.reason, "
                       "ss.cluster_subgroup_id FROM surface_subgroup ss JOIN cluster_subgroup g ON g.id=ss.cluster_subgroup_id WHERE ss.deleted=0 AND ss.strong IN ({in}) ORDER BY ss.id", full):
        place[(r[0], r[1])].append(r[2:10])
    d["placements"] = dict(place)
    attested = dict(_in(conn, "SELECT strong, count(*) FROM strong_verse WHERE deleted=0 AND strong IN ({in}) GROUP BY strong", full))
    lexical = dict(_in(conn, "SELECT strong, count(*) FROM verse_lexical WHERE deleted=0 AND strong IN ({in}) GROUP BY strong", full))
    for c in full:
        e[c]["attested"] = attested.get(c, 0)
        e[c]["lexical"] = lexical.get(c, 0)
    d["strongs"] = e

def _faults(conn, d: dict, surfaces) -> list[dict]:
    """Blatant errors and omissions: each rule in words, with the columns that identify a finding and the rows it found (an empty list is 'none found'). A rule that
    needs a collection is applied only to a collection report."""
    out = []

    def add(key, how, cols, rows):
        out.append({"key": key, "how": how, "cols": cols, "rows": rows})
    ref_of = {osis: v[0] for osis, v in d["verse_text"].items()}
    if d["kind"] == "collection":
        col = d["collection"]
        terms, _ = _terms(conn)
        add("link-to-missing-or-deleted-term", "live collection_link of this collection whose term_id has no live surface_term row", ["link", "tier", "term_id", "word"],
            [[ln["id"], ln["tier"], ln["term_id"], ln["surface"]] for ln in d["links"]
             if not ln["deleted"] and (ln["term_id"] not in terms or terms[ln["term_id"]][10])])
        bad = []
        mid = col["merged_into_id"]
        if col["status"] == "merged" and not mid:
            bad.append("status merged with no merged_into_id")
        if col["status"] != "merged" and mid:
            bad.append(f"merged_into_id {mid} with status {col['status']}")
        if mid and conn.execute("SELECT 1 FROM collection WHERE id=? AND deleted=0", (mid,)).fetchone() is None:
            bad.append(f"merged_into_id {mid} is not a live collection")
        add("collection-merge-inconsistent", "collection.status and collection.merged_into_id disagree, or the target is not live", ["problem"], [[b] for b in bad])
        have = {o["surface"] for o in d["occurrences"]}
        add("member-surface-with-no-occurrence", "member term of origin 'surface' that no live verse_lexical row carries", ["term_id", "word", "tiers"],
            [[t["term_id"], t["surface"], t["tiers"]] for t in d["terms"] if t["origin"] == "surface" and t["surface"] not in have])
    else:
        add("verse-not-in-use", "requested verse whose verse row is soft deleted", ["verse", "verse_id"],
            [[v["reference"], v["verse_id"]] for v in d["verses"] if v["deleted"]])
        have = {o["verse_id"] for o in d["occurrences"]}
        add("verse-with-no-word-rows", "requested verse that no live verse_lexical row carries", ["verse", "verse_id"],
            [[v["reference"], v["verse_id"]] for v in d["verses"] if v["verse_id"] not in have])
    add("occurrence-in-deleted-verse", "occurrence whose verse row is soft deleted", ["vl_id", "reference"],
        [[o["vl_id"], o["reference"]] for o in d["occurrences"] if o["verse_deleted"]])
    obs = {o["id"]: o for o in d["observations"]}
    add("live-node-on-deleted-observation", "ib_node with deleted=0 whose observation is deleted or missing (the node still names a verse and word the observation no longer covers)",
        ["node", "observation", "observation stage", "observation tag", "observation status", "verse", "word", "Strong's code"],
        [[n["id"], n["observation_id"], obs.get(n["observation_id"], {}).get("stage", ""), obs.get(n["observation_id"], {}).get("tag", ""),
          obs.get(n["observation_id"], {}).get("status", "missing"), ref_of.get(n["verse_reference"], n["verse_reference"]), n["surface"], n["strong"]]
         for n in d["nodes"] if not n["deleted"] and (n["observation_id"] not in obs or obs[n["observation_id"]]["deleted"])])
    add("claim-source-on-deleted-observation", "narrative_claim_source naming an observation that is deleted or missing", ["source", "claim", "observation"],
        [[s["id"], s["claim_id"], s["observation_id"]] for s in d["claim_sources"]
         if s["via"] == "observation" and (s["observation_id"] not in obs or obs[s["observation_id"]]["deleted"])])
    told = {t["claim_id"] for t in d["tellings"] if t["status"] == "current"}
    add("claim-in-narrative-with-no-current-telling", "narrative_claim.in_narrative=1 and no current narrative_claim_telling", ["claim", "claim id"],
        [[c["claim_ref"], c["id"]] for c in d["claims"] if c["in_narrative"] and c["id"] not in told])
    refs = {o["osis"] for o in d["occurrences"]}
    add("live-node-with-no-verse-lexical-id", "live ib_node in a verse of the report" + (" with a member surface" if surfaces is not None else "") +
        " but verse_lexical_id NULL (stored, tied to no occurrence)", ["node", "observation", "verse", "word"],
        [[r[0], r[1], ref_of.get(r[2], r[2]), r[3]] for r in conn.execute(
            "SELECT id, observation_id, verse_reference, lower(trim(surface)) FROM ib_node WHERE verse_lexical_id IS NULL AND deleted=0")
         if r[2] in refs and (surfaces is None or r[3] in surfaces)])
    return out
