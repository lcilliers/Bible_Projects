"""collectionevidence.py -- the evidence report of one collection, a list of collections, or a verse or list of verses (escalations #2464, #2467).

It exposes the entries that exist in the database for every aspect of the words and verses in scope, from the base data through the observations and
the claims into the narrative, and nothing else: no evaluation, no inferred data, no model call, nothing written to a table. Every row is a join
on a stored key. Where a link in the chain has no row, the report says so (an omission shown, not judged); blatant errors are listed apart under
"stored-data faults", each with the rule that found it.

Scope. A collection: its members are those of the CSV exports (collectionexport.py): a live link of a tier in `collection.export_tiers` reaches its own
term and the terms whose base is that term; their occurrences are the live verse_lexical rows whose surface (lower-cased, trimmed, the key surface_term
uses) is a member surface. Links of the other tiers are listed with their reason and do not reach verses here. A verse list: every live verse_lexical
row of each verse (all words), with the collections and tiers each surface belongs to by any live link.

Nodes are never listed alone (#2469): each observation is a card with a Supports list of every node of the observation (in or out of the scope), grouped by verse
in Scripture order with the verse text, each node with its word, Strong's code (native word, transliteration, gloss), role, disposition and cluster; and each Strong's code of the
occurrences has an entry from the stored tables (strong, strong_sense, strong_meaning_tree, strong_related, strong_lsj_parsed, strong_mounce_parsed, cluster_strong,
surface_subgroup with concept and domain, strong_verse against verse_lexical).

The chain from the occurrences: the observations are the ib_node rows whose verse_lexical_id is one of the occurrences; the claims are the
narrative_claim_source rows that name one of those observations (observation_id) or one of those verses (verse_id); the narrative is the
narrative_claim_telling of those claims, with its section and chapter.

Order. Verses are in Scripture order: book in cfg_book_order, then chapter, then verse (the key of `scripture_key`). Two layouts of the same rows:
by unit then by type (the default: a collection report has a section for each member word, a verse report one for each verse) and by type
(`by_type`: one section for each type across the whole scope).
"""
from __future__ import annotations

import collections
import csv
import pathlib
import re

TIER_ORDER = {"core": 0, "synonym": 1, "opposite": 2, "gathered": 3, "possible_opposite": 4, "associated": 5, "phrase": 6, "set_aside": 7}
CHUNK = 800
COLLECTION_COLS = ("id", "name", "status", "core_term_id", "pole_word", "pole_of_pole", "pole_reciprocal", "pole_real_word", "merged_into_id", "concept_id",
                   "run_id", "created_by", "created_at", "updated_at", "load_ref")
REF_FORM = ("a reference is `Book chapter:verse` (for example Pro 6:14), a range `Pro 6:14-16` or across chapters `Pro 6:30-7:2`, a whole chapter `Pro 6`, "
            "a list of verses of one book `Pro 6:14, 16`; each item starts with its book (as the verse table writes it, such as Mat, 1Sa, Phili, or an alias of "
            "narrative.book_alias_map, such as Matthew, 1Sam, Ps) and items are separated by a semicolon")


class EvidenceError(Exception):
    """A usage or setting problem; routed as 'refused' and nothing is written."""


def read_settings(cfg) -> dict:
    out = {}
    for key, name in (("collection.export_tiers", "tiers"), ("collection.evidence_path", "path"), ("collection.evidence_name", "name"),
                      ("collection.evidence_verse_name", "verse_name")):
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


def _terms(conn):
    terms = {r[0]: r for r in conn.execute("SELECT id, surface, form, origin, surface_group, group_state, base_id, base_source, base_state, collection_state, deleted "
                                           "FROM surface_term")}
    of_base = collections.defaultdict(list)
    for t in terms.values():
        if t[6] is not None and t[6] != t[0]:
            of_base[t[6]].append(t[0])
    return terms, of_base


def build_collection(conn, col: dict, tiers: list, order: Order) -> dict:
    """Everything stored for one collection, as lists of dicts, from the tables only."""
    d = {"kind": "collection", "name": col["name"], "collection": col, "tiers": tiers}
    terms, of_base = _terms(conn)
    d["links"] = _dicts(conn.execute(
        "SELECT l.id, l.tier, l.term_id, t.surface, l.shared, l.superseded_by_id, l.reason, l.ai_call_id, l.run_id, l.created_by, l.created_at, l.deleted, l.load_ref "
        "FROM collection_link l LEFT JOIN surface_term t ON t.id=l.term_id WHERE l.collection_id=?", (col["id"],)).fetchall(),
        ("id", "tier", "term_id", "surface", "shared", "superseded_by_id", "reason", "ai_call_id", "run_id", "created_by", "created_at", "deleted", "load_ref"))
    d["links"].sort(key=lambda r: (r["deleted"], TIER_ORDER.get(r["tier"], 9), r["surface"] or "", r["id"]))
    member = {}   # term id -> set of (link id, tier)
    for ln in d["links"]:
        if ln["deleted"] or ln["tier"] not in tiers:
            continue
        reach = list(of_base.get(ln["term_id"], []))
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
    surfaces = set(tier_of)
    occ = _occurrences(conn, order, lambda surface, vid: surface in surfaces)
    for o in occ:
        o["memb"] = "/".join(sorted(tier_of[o["surface"]], key=lambda x: TIER_ORDER.get(x, 9)))
    occ.sort(key=lambda o: (o["surface"], o["sk"], o["position"] if o["position"] is not None else 0, o["code_ordinal"] or 0, o["vl_id"]))
    d["occurrences"] = occ
    _chain(conn, d, order)
    d["faults"] = _faults(conn, d, surfaces=surfaces)
    return d


# ══ scope: verses ════════════════════════════════════════════════════════════════════════════════
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
    for cname, tier, tid in conn.execute("SELECT c.name, l.tier, l.term_id FROM collection_link l JOIN collection c ON c.id=l.collection_id "
                                         "WHERE l.deleted=0 AND c.deleted=0"):
        reach = list(of_base.get(tid, [])) + ([tid] if tid in terms else [])
        for sid in reach:
            memb[terms[sid][1]].add((cname, tier))
    ids = {v["verse_id"] for v in verses}
    occ = _occurrences(conn, order, lambda surface, vid: vid in ids)
    for o in occ:
        o["memb"] = "; ".join(f"{c}:{t}" for c, t in sorted(memb.get(o["surface"], ()), key=lambda x: (x[0], TIER_ORDER.get(x[1], 9))))
    occ.sort(key=lambda o: (o["sk"], o["position"] if o["position"] is not None else 0, o["code_ordinal"] or 0, o["vl_id"]))
    d["occurrences"] = occ
    _chain(conn, d, order)
    d["faults"] = _faults(conn, d, surfaces=None)
    return d


# ══ the chain from the occurrences to the narrative ══════════════════════════════════════════════
def _occurrences(conn, order: Order, wanted) -> list[dict]:
    occ = []
    for r in conn.execute("SELECT vl.id, lower(trim(vl.surface)), vl.strong, vl.morph_code, vl.code_ordinal, vl.position, vl.surface_kind, vl.unit_surface, vl.unit_role, "
                          "vl.status, vl.verse_id, v.osisId, v.reference, v.text, v.deleted, vl.role, vl.is_negator, vl.party_kind, vl.unit_size FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0"):
        if wanted(r[1], r[10]):
            o = dict(zip(("vl_id", "surface", "strong", "morph", "code_ordinal", "position", "surface_kind", "unit_surface", "unit_role", "status",
                          "verse_id", "osis", "reference", "text", "verse_deleted", "vl_role", "is_negator", "party_kind", "unit_size"), r))
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
    obs_cols = ("id", "stage", "tag", "status", "deleted", "strong", "window", "route", "basis", "obs_text", "setting", "meaning", "implication", "chain", "parties",
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
    subgroups with concept and domain, and the verses STEP attests against the verse_lexical rows (#2469). Every value is a stored row; nothing is derived."""
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
    concept = {g: (n, dm) for g, n, dm in conn.execute(
        "SELECT cs.cluster_subgroup_id, n.name, dm.name FROM concept_subgroup cs JOIN concept n ON n.id=cs.concept_id LEFT JOIN concept_domain dm ON dm.id=n.domain_id "
        "WHERE cs.deleted=0 ORDER BY cs.id DESC")}
    place = collections.defaultdict(list)
    for r in _in(conn, "SELECT ss.strong, ss.surface, ss.cluster_code, g.subgroup_code, g.label, g.core_description, ss.status, ss.two_sense, ss.allocated_by, ss.reason, "
                       "ss.cluster_subgroup_id FROM surface_subgroup ss JOIN cluster_subgroup g ON g.id=ss.cluster_subgroup_id WHERE ss.deleted=0 AND ss.strong IN ({in}) ORDER BY ss.id", full):
        cn = concept.get(r[10], (None, None))
        place[(r[0], r[1])].append(r[2:10] + cn)
    d["placements"] = dict(place)
    attested = dict(_in(conn, "SELECT strong, count(*) FROM strong_verse WHERE deleted=0 AND strong IN ({in}) GROUP BY strong", full))
    lexical = dict(_in(conn, "SELECT strong, count(*) FROM verse_lexical WHERE deleted=0 AND strong IN ({in}) GROUP BY strong", full))
    for c in full:
        e[c]["attested"] = attested.get(c, 0)
        e[c]["lexical"] = lexical.get(c, 0)
    d["strongs"] = e

def _faults(conn, d: dict, surfaces) -> list[dict]:
    """Blatant errors and omissions: each rule, in words, with the rows it found (an empty list is 'none found'). A rule that needs a collection is
    applied only to a collection report."""
    out = []

    def add(key, how, rows):
        out.append({"key": key, "how": how, "rows": rows})
    if d["kind"] == "collection":
        col = d["collection"]
        terms, _ = _terms(conn)
        add("link-to-missing-or-deleted-term", "live collection_link of this collection whose term_id has no live surface_term row",
            [f"link {ln['id']} ({ln['tier']}) term_id {ln['term_id']} surface {ln['surface']!r}" for ln in d["links"]
             if not ln["deleted"] and (ln["term_id"] not in terms or terms[ln["term_id"]][10])])
        bad = []
        mid = col["merged_into_id"]
        if col["status"] == "merged" and not mid:
            bad.append("status merged with no merged_into_id")
        if col["status"] != "merged" and mid:
            bad.append(f"merged_into_id {mid} with status {col['status']}")
        if mid and conn.execute("SELECT 1 FROM collection WHERE id=? AND deleted=0", (mid,)).fetchone() is None:
            bad.append(f"merged_into_id {mid} is not a live collection")
        add("collection-merge-inconsistent", "collection.status and collection.merged_into_id disagree, or the target is not live", bad)
        have = {o["surface"] for o in d["occurrences"]}
        add("member-surface-with-no-occurrence", "member term of origin 'surface' that no live verse_lexical row carries",
            [f"term {t['term_id']} {t['surface']!r} ({t['tiers']})" for t in d["terms"] if t["origin"] == "surface" and t["surface"] not in have])
    else:
        add("verse-not-in-use", "requested verse whose verse row is soft deleted",
            [f"{v['reference']} (verse id {v['verse_id']})" for v in d["verses"] if v["deleted"]])
        have = {o["verse_id"] for o in d["occurrences"]}
        add("verse-with-no-word-rows", "requested verse that no live verse_lexical row carries",
            [f"{v['reference']} (verse id {v['verse_id']})" for v in d["verses"] if v["verse_id"] not in have])
    add("occurrence-in-deleted-verse", "occurrence whose verse row is soft deleted",
        [f"vl {o['vl_id']} {o['reference']}" for o in d["occurrences"] if o["verse_deleted"]])
    obs = {o["id"]: o for o in d["observations"]}
    add("live-node-on-deleted-observation", "ib_node with deleted=0 whose observation is deleted or missing",
        [f"node {n['id']} on observation {n['observation_id']}" for n in d["nodes"] if not n["deleted"] and (n["observation_id"] not in obs or obs[n["observation_id"]]["deleted"])])
    add("claim-source-on-deleted-observation", "narrative_claim_source naming an observation that is deleted or missing",
        [f"source {s['id']} claim {s['claim_id']} observation {s['observation_id']}" for s in d["claim_sources"]
         if s["via"] == "observation" and (s["observation_id"] not in obs or obs[s["observation_id"]]["deleted"])])
    told = {t["claim_id"] for t in d["tellings"] if t["status"] == "current"}
    add("claim-in-narrative-with-no-current-telling", "narrative_claim.in_narrative=1 and no current narrative_claim_telling",
        [f"claim {c['claim_ref']} (id {c['id']})" for c in d["claims"] if c["in_narrative"] and c["id"] not in told])
    refs = {o["osis"] for o in d["occurrences"]}
    unlinked = [f"node {r[0]} observation {r[1]} {r[2]} surface {r[3]!r}" for r in conn.execute(
        "SELECT id, observation_id, verse_reference, lower(trim(surface)) FROM ib_node WHERE verse_lexical_id IS NULL AND deleted=0")
        if r[2] in refs and (surfaces is None or r[3] in surfaces)]
    add("live-node-with-no-verse-lexical-id", "live ib_node in a verse of the report" + (" with a member surface" if surfaces is not None else "") +
        " but verse_lexical_id NULL (stored, tied to no occurrence)", unlinked)
    return out


# ══ the Markdown report ══════════════════════════════════════════════════════════════════════════
def _cell(v) -> str:
    return "" if v is None else str(v).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def _table(head: list, rows: list) -> list[str]:
    if not rows:
        return ["_no rows_", ""]
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(_cell(c) for c in r) + " |" for r in rows]
    return out + [""]


def _slice(d: dict, occ: list[dict]) -> dict:
    """The part of the chain that belongs to these occurrences (a word's, or a verse's): the same rows, restricted by the stored keys."""
    vl = {o["vl_id"] for o in occ}
    vs = {o["verse_id"] for o in occ}
    nodes = [n for n in d["nodes"] if n["vl_id"] in vl]
    obs_ids = {n["observation_id"] for n in nodes}
    srcs = [s for s in d["claim_sources"] if (s["via"] == "observation" and s["observation_id"] in obs_ids) or (s["via"] == "verse" and s["verse_id"] in vs)]
    claim_ids = {s["claim_id"] for s in srcs}
    tells = [t for t in d["tellings"] if t["claim_id"] in claim_ids]
    sec_ids = {t["section_id"] for t in tells if t["section_id"] is not None}
    return {"occurrences": occ, "nodes": nodes, "observations": [o for o in d["observations"] if o["id"] in obs_ids], "obs_nodes": d["obs_nodes"],
            "verse_text": d["verse_text"], "strong_short": d["strong_short"], "strongs": d["strongs"], "placements": d["placements"], "scope_vl": d["scope_vl"],
            "changes": [c for c in d["changes"] if c["observation_id"] in obs_ids], "claim_sources": srcs,
            "claims": [c for c in d["claims"] if c["id"] in claim_ids], "tellings": tells, "sections": [s for s in d["sections"] if s["id"] in sec_ids]}


def _label(code, short) -> str:
    """A Strong's code with its native word, transliteration and gloss as stored: H3820A לֵב lev "heart"."""
    s = short.get(code)
    if not s:
        return str(code or "")
    return " ".join(x for x in (code, s[1], s[2]) if x) + (f' "{s[3]}"' if s[3] else "")


def _node_line(n: dict, short: dict, where: str) -> str:
    parts = [f"node {n['id']}", f"word `{n['surface']}`", f"`{_label(n['strong'], short)}`", f"role {n['role'] or '-'}", f"disposition {n['disposition'] or '-'}"]
    if n["disposition_note"]:
        parts.append(f"note: {_cell(n['disposition_note'])}")
    place = "/".join(x for x in (n["cluster"], n["subgroup"]) if x)
    if place:
        parts.append(f"cluster {place}")
    if n["deleted"]:
        parts.append("node deleted")
    parts.append(where)
    return "  - " + "; ".join(parts)


def _supports(s: dict, nodes: list, slice_vl: set, only_slice: bool) -> list[str]:
    """The nodes of an observation, grouped by verse in Scripture order, each verse with its reference and text once."""
    by = collections.defaultdict(list)
    for n in nodes:
        if not only_slice or n["vl_id"] in slice_vl:
            by[n["verse_reference"] or ""].append(n)
    L = []
    for osis in sorted(by, key=lambda x: by[x][0]["sk"]):
        ref, txt = s["verse_text"].get(osis, (osis or "(no verse)", None))
        L.append(f"- **{ref}**" + (f": {_cell(txt)}" if txt else " (no text found in table verse)"))
        for n in by[osis]:
            where = "in this section" if n["vl_id"] in slice_vl else ("elsewhere in this report" if n["vl_id"] in s["scope_vl"] else "outside this report")
            L.append(_node_line(n, s["strong_short"], where))
    return L


def _strong_entry(code: str, ent: dict, pairs: list, s: dict, lv: int) -> list[str]:
    """One Strong's entry, every stored item of it, as a section of heading level lv."""
    h = "#" * lv
    sh = ent["short"]
    L = [f"{h} Strong's entry {_label(code, s['strong_short'])}", ""]
    if sh is None:
        return L + ["_no row in table strong for this code_", ""]
    head, own = ent.get("sense", (None, None))
    L += [f"- language {sh[4]}; native word {sh[1]}; transliteration {sh[2]}; STEP gloss \"{sh[3]}\"; sense head \"{head}\"" + (" (the code is its own lemma)" if own else "")
          + f"; origin {sh[6]}",
          f"- counts, three different measures as stored: STEP token count {sh[5]} (a frequency, not a verse count); verses STEP attests {ent['attested']} (strong_verse); "
          f"verse_lexical rows the parse found {ent['lexical']}", ""]
    L += [f"{h}# Meaning trees stored under the lemma {ent['lemma']} ({len(ent['trees'])}, strong_meaning_tree; the key is the lemma, so the trees of its variants are stored together and shown in stored order, a repeated tree as stored)", ""]
    for i, tr in enumerate(ent["trees"], 1):
        L += [f"**Tree {i}** (rows {tr[0][0]} to {tr[-1][0]})", ""]
        for _, code_, text in tr:
            depth = max(1, len(re.findall(r"\d+|[a-z]", (code_ or "").rstrip(")"))))
            L.append("  " * (depth - 1) + f"- {code_ + ' ' if code_ else ''}{_cell(text)}")
        L.append("")
    if not ent["trees"]:
        L += ["_no rows in strong_meaning_tree_", ""]
    L += [f"{h}# Related terms ({len(ent['related'])}, strong_related)", ""]
    L += _table(["code", "native", "transliteration", "gloss"], [list(r) for r in ent["related"]])
    if sh[4] == "Greek" or ent["lsj"] or ent["mounce"]:
        L += [f"{h}# LSJ senses ({len(ent['lsj'])}, strong_lsj_parsed) and Mounce ({len(ent['mounce'])}, strong_mounce_parsed)", ""]
        L += _table(["sense", "gloss", "note", "row type"], [list(r) for r in ent["lsj"]])
        L += _table(["Mounce", "row type"], [list(r) for r in ent["mounce"]])
    L += [f"{h}# Cluster assignments ({len(ent['clusters'])}, cluster_strong)", ""]
    L += _table(["cluster", "name", "confidence", "operation", "review flag", "alternatives", "rationale", "source"], [list(r) for r in ent["clusters"]])
    rows = [[surf] + list(r) for surf in sorted(pairs) for r in s["placements"].get((code, surf), [])]
    L += [f"{h}# Placement of the surfaces of this section in subgroups (surface_subgroup, with concept and domain)", ""]
    L += _table(["surface", "cluster", "subgroup", "label", "core description", "status", "two sense", "allocated by", "reason", "concept", "domain"], rows)
    return L


def _types(s: dict, lv: int, numbered: bool, seen: dict, where: str, memb_head: str) -> list[str]:
    """The types of one slice, as sections of heading level `lv`. A body already printed in full for an earlier unit is cited, not repeated."""
    h = "#" * lv
    n = (lambda i: f"{i}. ") if numbered else (lambda i: "")
    short = s["strong_short"]
    L = []
    occ = s["occurrences"]
    slice_vl = {o["vl_id"] for o in occ}
    live = {x["vl_id"] for x in s["nodes"] if not x["deleted"]}
    nodes_of = collections.defaultdict(list)
    for x in s["nodes"]:
        nodes_of[x["vl_id"]].append(x)
    L += [f"{h} {n(3)}Base data: occurrences in verse_lexical ({len(occ)} in {len({o['verse_id'] for o in occ})} verse(s); {sum(o['vl_id'] in live for o in occ)} with a live observation node)", ""]
    L += _table(["vl_id", memb_head, "surface", "reference", "Strong's code", "morph", "pos", "surface_kind", "unit_surface", "unit_size", "unit_role", "role (clusters)", "negator",
                 "party", "status", "observations (node role/disposition)"],
                [[o["vl_id"], o["memb"], o["surface"], o["reference"], _label(o["strong"], short), o["morph"], o["position"], o["surface_kind"], o["unit_surface"], o["unit_size"],
                  o["unit_role"], o["vl_role"], o["is_negator"], o["party_kind"], o["status"],
                  "; ".join(f"{x['observation_id']}: {x['role'] or '-'}/{x['disposition'] or '-'}" + (" (node deleted)" if x["deleted"] else "") for x in nodes_of.get(o["vl_id"], []))]
                 for o in occ])
    L += [f"{'#' * (lv + 1)} Verse texts (ESV, from table `verse`)", ""]
    vt = {}
    for o in occ:
        vt.setdefault(o["verse_id"], (o["sk"], o["reference"], o["text"]))
    L += [f"- {ref}: {txt}" for _, ref, txt in sorted(vt.values())] + [""]
    codes = sorted({o["strong"] for o in occ if o["strong"]})
    L += [f"{h} {n(4)}Strong's entries ({len(codes)} codes of these occurrences)", ""]
    for code in codes:
        if code in seen["strong"]:
            L += [f"- {_label(code, short)}: printed in full under {seen['strong'][code]}", ""]
            continue
        seen["strong"][code] = where
        pairs = sorted({o["surface"] for o in occ if o["strong"] == code})
        L += _strong_entry(code, s["strongs"][code], pairs, s, lv + 1)
    L += [f"{h} {n(5)}Observations ({len(s['observations'])}), each with the nodes that support it ({len(s['nodes'])} nodes on these occurrences)", ""]
    for o in s["observations"]:
        L += [f"{'#' * (lv + 1)} Observation {o['id']}: stage {o['stage']}, tag {o['tag']}, status {o['status']}, deleted {o['deleted']}", ""]
        nodes = s["obs_nodes"].get(o["id"], [])
        if o["id"] in seen["obs"]:
            L += [f"Printed in full under {seen['obs'][o['id']]}. Its nodes in this section:", ""]
            L += _supports(s, nodes, slice_vl, True) + [""]
        else:
            seen["obs"][o["id"]] = where
            meta = [f"{k}: {o[k]}" for k in ("strong", "window", "route", "basis", "run_id", "created_at", "updated_at", "supersedes_observation_id") if o[k] not in (None, "")]
            L += ["- " + "; ".join(meta)]
            for k in ("obs_text", "setting", "meaning", "implication", "chain", "parties", "parts", "revisit_note"):
                if o[k] not in (None, ""):
                    L += [f"- **{k}:** {_cell(o[k])}"]
            L += ["", f"**Supports ({len(nodes)} nodes, by verse in Scripture order):**", ""]
            L += _supports(s, nodes, slice_vl, False) + [""]
    L += [f"{h} {n(6)}Change history of these observations and nodes ({len(s['changes'])})", ""]
    L += _table(["id", "observation", "node", "column", "old", "new", "reason", "reading", "run", "created", "by"],
                [[x["id"], x["observation_id"], x["node_id"], x["column"], x["old_value"], x["new_value"], x["reason"], x["reading_id"], x["run_id"], x["created_at"],
                  x["created_by"]] for x in s["changes"]])
    cl = {x["id"]: x for x in s["claims"]}
    L += [f"{h} {n(7)}Claims ({len(s['claims'])}) and what they rest on ({len(s['claim_sources'])} source rows)", "",
          "A claim source reaches this scope either by naming one of its observations (via observation) or by naming one of its verses (via verse).", ""]
    L += _table(["source", "via", "claim", "kind", "verse_id", "reference as written", "observation", "note", "by"],
                [[x["id"], x["via"], cl[x["claim_id"]]["claim_ref"], x["source_kind"], x["verse_id"], x["ref_as_written"], x["observation_id"], x["note"], x["created_by"]]
                 for x in s["claim_sources"]])
    for x in s["claims"]:
        L += [f"{'#' * (lv + 1)} Claim {x['claim_ref']} (id {x['id']}): origin {x['origin']}, status {x['status']}, verdict {x['verdict']}"
              + (f" / {x['part_verdict']} ({x['part_scope']})" if x["part_verdict"] else "") + f", in_narrative {x['in_narrative']}, i_read {x['i_read']}", ""]
        if x["id"] in seen["claim"]:
            L += [f"Printed in full under {seen['claim'][x['id']]}.", ""]
        else:
            seen["claim"][x["id"]] = where
            L += [f"- **claim_text:** {_cell(x['claim_text'])}", f"- **beyond_text:** {_cell(x['beyond_text'])}", ""]
    L += [f"{h} {n(8)}Narrative: tellings ({len(s['tellings'])}) and sections ({len(s['sections'])})", ""]
    L += _table(["telling", "claim", "kind", "status", "part told", "section", "chapter", "heading", "section last_version"],
                [[t["id"], cl[t["claim_id"]]["claim_ref"], t["kind"], t["status"], t["part_told"], t["section_id"] if t["section_id"] is not None else f"passage {t['passage_id']}",
                  f"{t['chapter_no']} {t['chapter_title'] or ''}".strip(), t["heading"], t["last_version"]] for t in s["tellings"]])
    for sec in s["sections"]:
        L += [f"{'#' * (lv + 1)} Section {sec['id']}: chapter {sec['chapter_no']} {sec['chapter_title'] or ''}, {sec['heading']}", ""]
        if sec["id"] in seen["sec"]:
            L += [f"Printed in full under {seen['sec'][sec['id']]}.", ""]
        else:
            seen["sec"][sec["id"]] = where
            L += ["> " + ln for ln in (sec["block_text"] or "(no block text stored)").splitlines()] + [""]
    return L


def _units(d: dict) -> list[tuple[str, list[dict]]]:
    """The units of the by-unit layout: the member words of a collection (alphabetical), the verses of a verse list (Scripture order)."""
    occ = d["occurrences"]
    if d["kind"] == "collection":
        by = collections.defaultdict(list)
        for o in occ:
            by[o["surface"]].append(o)
        names = sorted({t["surface"] for t in d["terms"]})
        return [(f"Word {w}", by.get(w, [])) for w in names]
    by = collections.defaultdict(list)
    for o in occ:
        by[o["verse_id"]].append(o)
    return [(f"Verse {v['reference']}", by.get(v["verse_id"], [])) for v in d["verses"]]


def render(datas: list[dict], run_id: str, stamp: str, by_type: bool, scope_text: str = "") -> str:
    """The Markdown report of one or more collections, or of a verse list."""
    verse = datas[0]["kind"] == "verse"
    title = ("Verse evidence report: " + datas[0]["name"]) if verse else "Collection evidence report: " + ", ".join(d["name"] for d in datas)
    layout = "by type" if by_type else ("by verse, then by type" if verse else "by word, then by type")
    L = [f"# {title}", "",
         f"Generated {stamp} by run {run_id} (`Collection-Build.ps1 -Action Evidence`, escalations #2464 and #2467). Layout: {layout}"
         + (" (switch -ByType)." if by_type else ".") + " Every row below is a stored table entry; nothing is evaluated or inferred, and nothing was written to a table. "
         "A missing link in the chain is stated as no rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). "
         + ("Each word shows the collections and tiers it belongs to by any live link. " if verse else
            f"Members are the terms reached by a live link of the tiers {', '.join(datas[0]['tiers'])} (the term itself and the terms whose base it is). ")
         + "The joins are in `iba/app/lib/collectionevidence.py`.", ""]
    for d in datas:
        seen = {"obs": {}, "claim": {}, "sec": {}, "strong": {}}
        memb_head = "collections (tier)" if verse else "tiers"
        if verse:
            L += ["## Verses requested", ""]
            L += _table(["reference", "osisId", "verse_id", "as asked", "word rows", "text"],
                        [[v["reference"], v["osis"], v["verse_id"], v["asked"], sum(o["verse_id"] == v["verse_id"] for o in d["occurrences"]), v["text"]] for v in d["verses"]])
        else:
            c = d["collection"]
            L += [f"## Collection {c['name']}", ""]
            L += _table(["field", "value"], [[k, c[k]] for k in COLLECTION_COLS])
            L += ["### 1. Links (live first, then removed or superseded)", ""]
            L += _table(["link", "tier", "term_id", "word", "shared", "deleted", "superseded_by", "reason", "ai_call", "run", "by", "created", "load_ref"],
                        [[x["id"], x["tier"], x["term_id"], x["surface"], x["shared"], x["deleted"], x["superseded_by_id"], x["reason"], x["ai_call_id"], x["run_id"],
                          x["created_by"], x["created_at"], x["load_ref"]] for x in d["links"]])
            L += [f"### 2. Member terms ({len(d['terms'])})", ""]
            L += _table(["term_id", "surface", "form", "origin", "tiers", "via links", "group", "group_state", "base", "base_source", "base_state", "collection_state"],
                        [[t["term_id"], t["surface"], t["form"], t["origin"], t["tiers"], t["links"], t["group"], t["group_state"], t["base"], t["base_source"],
                          t["base_state"], t["collection_state"]] for t in d["terms"]])
        if by_type:
            L += _types(_slice(d, d["occurrences"]), 3, True, seen, "this report", memb_head)
        else:
            L += [f"## {'Verses' if verse else 'Words'}, each by type", ""]
            for label, occ in _units(d):
                L += [f"### {label}", ""]
                L += _types(_slice(d, occ), 4, False, seen, label, memb_head)
        L += ["### Stored-data faults (blatant errors and omissions)", ""]
        for f in d["faults"]:
            L += [f"- **{f['key']}** ({f['how']}): " + (f"{len(f['rows'])} found" if f["rows"] else "none found")]
            L += [f"  - {r}" for r in f["rows"]]
        L += [""]
    return "\n".join(L) + "\n"


CSV_HEAD = ["{lead1}", "{lead2}", "surface", "reference", "vl_id", "strong", "strong_translit", "strong_gloss", "morph", "surface_kind", "node_id", "node_role",
            "node_disposition", "node_deleted", "observation_id", "obs_stage", "obs_status", "obs_deleted", "obs_text", "claim_via", "claim_ref", "claim_status",
            "telling_status", "chapter_no", "section_heading"]
NO_NODE = [""] * 9


def csv_head(kind: str) -> list[str]:
    lead = ("collection", "tiers") if kind == "collection" else ("scope", "collections")
    return [lead[0] if h == "{lead1}" else lead[1] if h == "{lead2}" else h for h in CSV_HEAD]


def csv_rows(datas: list[dict]) -> list[list]:
    """One row for each occurrence, each node on it, each claim that names that node's observation, and each telling of that claim; a claim that names the
    occurrence's verse has its own rows with the node columns blank. Left joins: a missing link leaves its columns blank. The rows are in the order of the
    report: a collection by word then Scripture order, a verse list in Scripture order."""
    out = []
    for d in datas:
        lead = d["name"] if d["kind"] == "collection" else "verses"
        obs = {o["id"]: o for o in d["observations"]}
        cl = {c["id"]: c for c in d["claims"]}
        nodes = collections.defaultdict(list)
        for n in d["nodes"]:
            nodes[n["vl_id"]].append(n)
        src_obs, src_verse = collections.defaultdict(list), collections.defaultdict(list)
        for s in d["claim_sources"]:
            if s["via"] == "observation":
                src_obs[s["observation_id"]].append(s)
            else:
                src_verse[s["verse_id"]].append(s)
        tell = collections.defaultdict(list)
        for t in d["tellings"]:
            tell[t["claim_id"]].append(t)

        def claims(via, srcs):
            rows = []
            for cid in sorted({s["claim_id"] for s in srcs}):
                for t in tell.get(cid) or [None]:
                    rows.append([via, cl[cid]["claim_ref"], cl[cid]["status"], t["status"] if t else "", t["chapter_no"] if t else "", t["heading"] if t else ""])
            return rows or [["", "", "", "", "", ""]]
        for o in d["occurrences"]:
            sh = d["strong_short"].get(o["strong"]) or (None,) * 4
            head = [lead, o["memb"], o["surface"], o["reference"], o["vl_id"], o["strong"], sh[2] or "", sh[3] or "", o["morph"], o["surface_kind"]]
            ns = nodes.get(o["vl_id"]) or []
            if not ns:
                out.append(head + NO_NODE + claims("", [])[0])
            for n in ns:
                ob = obs.get(n["observation_id"], {})
                node = [n["id"], n["role"], n["disposition"], n["deleted"], n["observation_id"], ob.get("stage", ""), ob.get("status", ""), ob.get("deleted", ""), ob.get("obs_text", "")]
                out += [head + node + r for r in claims("observation", src_obs.get(n["observation_id"], []))]
            if src_verse.get(o["verse_id"]):
                out += [head + NO_NODE + r for r in claims("verse", src_verse[o["verse_id"]])]
    return out


def write_csv(path: pathlib.Path, kind: str, rows: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(csv_head(kind))
        w.writerows(rows)
