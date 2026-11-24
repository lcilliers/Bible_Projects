"""surfacerelation.py -- the relations between English surfaces held in iba.db (escalation #2548, brief of 2026-11-24).

An outside source (WordNet 3.0, read through NLTK) links the single-word surfaces of the relation study. This module holds the rule; the handler
iba/app/handlers/surfacerelation.py and Surface-Relation.ps1 call it. Nothing is hard-coded: the scope of the study (cfg_setting
surfaces.relation_scope), the pair types, their order and the weight (surfaces.relation_pair_rules) and the WordNet folder
(surfaces.wordnet_data_dir) are settings.

  plan_load / write_load      the pairs of the study surfaces into surface_relation (a changed pair or a pair no longer linked is flipped to
                              deleted = 1 and a changed one added again; nothing is physically deleted)
  plan_groups / write_groups  the connected groups of the live pairs into surface_network_group (the earlier grouping is kept, deleted = 1)
  plan_flags / write_flags    one surface_flag (kind wordnet_no_pair) for each surface of a reviewed list that has no pair
  validate                    the WordNet same_base pairs and groups against surface_term.base_id (reads; writes nothing to base_id)

WordNet is modern general English, an outside source: its links are candidate relations to read, not study findings.
"""
from __future__ import annotations

import collections
import itertools
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]


class RelationError(Exception):
    """A usage problem (a missing setting, an unreadable file, a list that does not match): the routed condition 'refused'."""


def read_settings(cfg) -> dict:
    s = {k: cfg.setting(k) for k in ("surfaces.relation_scope", "surfaces.relation_pair_rules", "surfaces.wordnet_data_dir",
                                      "surfaces.exports_root")}
    miss = [k for k, v in s.items() if v is None]
    if miss:
        raise RelationError("cfg_setting missing or inactive: " + ", ".join(miss))
    rules = s["surfaces.relation_pair_rules"]
    for k in ("source", "source_version", "type_order", "small_group_min"):
        if k not in rules:
            raise RelationError(f"cfg_setting surfaces.relation_pair_rules has no {k!r}")
    return {"scope": s["surfaces.relation_scope"], "rules": rules, "wn_dir": ROOT / s["surfaces.wordnet_data_dir"],
            "exports": ROOT / s["surfaces.exports_root"]}


def scope_terms(conn, scope: dict) -> list[tuple[int, str]]:
    """The live surface_term rows of the relation study, as (id, surface) sorted by surface: form and origin as set, a group in
    scope['groups'], or unjudged, or a surface_event of surface_group recording a move from scope['moved_from_groups'] on or after
    scope['moved_since']."""
    ph = lambda xs: ",".join("?" * len(xs))  # noqa: E731
    sql = (f"SELECT t.id, t.surface FROM surface_term t WHERE t.deleted=0 AND t.form=? AND t.origin IN ({ph(scope['origin'])}) AND ("
           f"t.surface_group IN ({ph(scope['groups'])})"
           + (" OR t.surface_group IS NULL" if scope.get("include_unjudged") else "")
           + f" OR EXISTS (SELECT 1 FROM surface_event e WHERE e.subject_kind='surface_term' AND e.subject_id=t.id "
             f"AND e.field='surface_group' AND e.deleted=0 AND e.value_before IN ({ph(scope['moved_from_groups'])}) AND e.created_at>=?)) "
             "ORDER BY t.surface")
    args = [scope["form"], *scope["origin"], *scope["groups"], *scope["moved_from_groups"], scope["moved_since"]]
    return [(r[0], r[1]) for r in conn.execute(sql, args)]


def _wordnet(wn_dir: pathlib.Path):
    try:
        import nltk
    except ImportError as exc:  # pragma: no cover
        raise RelationError(f"NLTK is not installed: {exc}")
    if not (wn_dir / "corpora" / "wordnet").is_dir():
        raise RelationError(f"WordNet is not at {wn_dir} (cfg_setting surfaces.wordnet_data_dir): the folder that holds corpora/wordnet")
    nltk.data.path.insert(0, str(wn_dir))
    from nltk.corpus import wordnet as wn
    return wn


def wordnet_pairs(surfaces: list[str], wn_dir: pathlib.Path, rules: dict) -> tuple[dict, set]:
    """({(a, b): {syn, ant, der, sim, same_base}} with a < b as text, the set of surfaces WordNet holds). A surface is looked up by its own
    text and its WordNet base form (morphy); no word outside `surfaces` is added."""
    wn = _wordnet(wn_dir)
    syn, lemmas, anto = {}, {}, collections.defaultdict(set)
    for s in surfaces:
        ss = wn.synsets(s.lower())
        if not ss:
            continue
        syn[s] = {x.name() for x in ss}
        lemmas[s] = {wn.morphy(s.lower(), p) for p in "nvar"} - {None}
        for x in ss:
            for lem in x.lemmas():
                if lem.name().lower() == s.lower() or lem.name().lower() in lemmas[s]:
                    for a in lem.antonyms():
                        anto[s].add(a.name().lower())
    der = collections.defaultdict(set)
    for s in syn:
        own = {s.lower()} | lemmas[s]
        for x in wn.synsets(s.lower()):
            for lem in x.lemmas():
                if lem.name().lower() in own:
                    for d in lem.derivationally_related_forms() + lem.pertainyms():
                        der[s].add(d.name().lower())
    in_wn = sorted(syn)
    by_syn, by_lemma = collections.defaultdict(list), collections.defaultdict(list)
    for s in in_wn:
        for x in syn[s]:
            by_syn[x].append(s)
        for b in lemmas[s] | {s.lower()}:
            by_lemma[b].append(s)
    shared = collections.Counter()
    for ls in by_syn.values():
        for a, b in itertools.combinations(sorted(ls), 2):
            shared[(a, b)] += 1
    same_base = {k for k in shared if lemmas[k[0]] & lemmas[k[1]]}
    antn = collections.Counter()
    for s in in_wn:
        for a in anto[s]:
            for t in by_lemma.get(a, []):
                if t != s:
                    antn[tuple(sorted((s, t)))] += 1
    derc = {}
    for s in in_wn:
        for nm in der[s]:
            for t in by_lemma.get(nm, []):
                if t != s:
                    derc[tuple(sorted((s, t)))] = 1
    simc = collections.Counter()
    seen = set()
    for x in {wn.synset(n) for v in syn.values() for n in v}:
        for y in x.similar_tos():
            k = tuple(sorted((x.name(), y.name())))
            if k in seen:
                continue
            seen.add(k)
            for a in by_syn.get(x.name(), []):
                for b in by_syn.get(y.name(), []):
                    if a != b:
                        simc[tuple(sorted((a, b)))] += 1
    edges: dict = {}
    for src, key in ((shared, "syn"), (antn, "ant"), (derc, "der"), (simc, "sim")):
        for k, v in src.items():
            edges.setdefault(k, {"syn": 0, "ant": 0, "der": 0, "sim": 0, "same_base": k in same_base})[key] = v
    return edges, set(in_wn)


def pair_type(e: dict, order: list[str]) -> str:
    """The first type of `order` that holds for the link counts e (cfg_setting surfaces.relation_pair_rules type_order)."""
    holds = {"same_base": e["same_base"], "both": bool(e["syn"] and e["ant"]), "synonym": bool(e["syn"]),
             "derivational": bool(e["der"]), "similar": bool(e["sim"]), "antonym": bool(e["ant"])}
    for t in order:
        if holds.get(t):
            return t
    raise RelationError(f"no pair type of {order} holds for {e}")


# ------------------------------------------------------------------ load
def plan_load(conn, cfg) -> dict:
    st = read_settings(cfg)
    terms = scope_terms(conn, st["scope"])
    tid = {s: i for i, s in terms}
    edges, in_wn = wordnet_pairs([s for _, s in terms], st["wn_dir"], st["rules"])
    src, ver = st["rules"]["source"], st["rules"]["source_version"]
    want = {}
    for (a, b), e in edges.items():
        ia, ib = sorted((tid[a], tid[b]))
        want[(ia, ib)] = (pair_type(e, st["rules"]["type_order"]), e["syn"] + e["ant"] + e["der"] + e["sim"], e["syn"], e["ant"], e["der"], e["sim"])
    have = {}
    for r in conn.execute("SELECT id, term_a_id, term_b_id, pair_type, weight, synsets_shared, antonym_links, derivational_links, similar_links, "
                          "source_version FROM surface_relation WHERE deleted=0 AND source=?", (src,)):
        have[(r[1], r[2])] = (r[0], tuple(r[3:9]), r[9])
    add = [k for k in want if k not in have]
    flip = [k for k in have if k not in want or have[k][1] != want[k] or have[k][2] != ver]
    readd = [k for k in flip if k in want]
    counts = collections.Counter(v[0] for v in want.values())
    return {"terms": terms, "tid": tid, "in_wn": in_wn, "want": want, "have": have, "add": add, "flip": flip, "readd": readd, "counts": counts,
            "source": src, "version": ver}


def write_load(conn, run_id: str, pl: dict) -> dict:
    flip_ids = [pl["have"][k][0] for k in pl["flip"]]
    for i in range(0, len(flip_ids), 500):
        part = flip_ids[i:i + 500]
        conn.execute(f"UPDATE surface_relation SET deleted=1, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now') WHERE id IN ({','.join('?' * len(part))})", part)
    new = [k for k in pl["want"] if k not in pl["have"] or k in set(pl["readd"])]
    conn.executemany(
        "INSERT INTO surface_relation (term_a_id, term_b_id, pair_type, weight, synsets_shared, antonym_links, derivational_links, similar_links, "
        "source, source_version, run_id, created_by) VALUES (?,?,?,?,?,?,?,?,?,?,?,'Claude')",
        [(a, b, *pl["want"][(a, b)], pl["source"], pl["version"], run_id) for (a, b) in new])
    return {"added": len(new) - len(pl["readd"]), "changed": len(pl["readd"]), "flipped": len(flip_ids), "inserted": len(new)}


# ------------------------------------------------------------------ groups
def plan_groups(conn, cfg) -> dict:
    st = read_settings(cfg)
    terms = scope_terms(conn, st["scope"])
    surf = {i: s for i, s in terms}
    src = st["rules"]["source"]
    parent = {i: i for i in surf}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    outside = 0
    n_rel = 0
    for a, b in conn.execute("SELECT term_a_id, term_b_id FROM surface_relation WHERE deleted=0 AND source=?", (src,)):
        n_rel += 1
        if a in surf and b in surf:
            parent[find(a)] = find(b)
        else:
            outside += 1
    comps = collections.defaultdict(list)
    for i in surf:
        comps[find(i)].append(i)
    ordered = sorted(comps.values(), key=lambda c: (-len(c), min(surf[i] for i in c)))
    smin = st["rules"]["small_group_min"]
    in_wn = {r[0] for r in conn.execute("SELECT DISTINCT term_a_id FROM surface_relation WHERE deleted=0 AND source=? UNION "
                                        "SELECT DISTINCT term_b_id FROM surface_relation WHERE deleted=0 AND source=?", (src, src))}
    iso = [i for c in ordered if len(c) == 1 for i in c if i not in in_wn]
    wn_held = set()
    if iso:  # a surface with no pair is in WordNet or not: asked of WordNet itself
        wn = _wordnet(st["wn_dir"])
        wn_held = {i for i in iso if wn.synsets(surf[i].lower())}
    want = {}
    for n, c in enumerate(ordered, 1):
        kind = "no_pair" if len(c) < smin else ("main" if n == 1 else "small")
        for i in c:
            want[i] = (n, len(c), kind, 1 if (i in in_wn or i in wn_held or len(c) >= smin) else 0)
    have = {r[0]: (r[1], tuple(r[2:6])) for r in conn.execute(
        "SELECT term_id, id, group_no, group_size, kind, in_wordnet FROM surface_network_group WHERE deleted=0")}
    same = set(have) == set(want) and all(have[i][1] == want[i] for i in want)
    counts = collections.Counter(v[2] for v in want.values())
    return {"surf": surf, "want": want, "have": have, "same": same, "counts": counts, "groups": len(ordered), "relations": n_rel, "outside": outside,
            "sizes": [len(c) for c in ordered[:5]], "small": sum(1 for c in ordered[1:] if len(c) >= smin)}


def write_groups(conn, run_id: str, pl: dict) -> dict:
    if pl["same"]:
        return {"flipped": 0, "inserted": 0}
    flipped = conn.execute("UPDATE surface_network_group SET deleted=1, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now') WHERE deleted=0").rowcount
    conn.executemany("INSERT INTO surface_network_group (term_id, group_no, group_size, kind, in_wordnet, run_id, created_by) VALUES (?,?,?,?,?,?,'Claude')",
                     [(i, *v, run_id) for i, v in pl["want"].items()])
    return {"flipped": flipped, "inserted": len(pl["want"])}


# ------------------------------------------------------------------ flags
def plan_flags(conn, cfg, path: str) -> dict:
    from openpyxl import load_workbook
    p = pathlib.Path(path)
    if not p.is_absolute():
        p = ROOT / p
    if not p.is_file():
        raise RelationError(f"the review list {path!r} is not a file")
    wb = load_workbook(p, read_only=True)
    if "review" not in wb.sheetnames:
        raise RelationError("the review list has no sheet 'review'")
    rows = list(wb["review"].iter_rows(values_only=True))
    head = list(rows[0])
    need = ["surface", "a_inner_being_or_behaviour", "a_note", "b_reason_kind", "b_detail", "manual_intervention", "who_acts"]
    miss = [h for h in need if h not in head]
    if miss:
        raise RelationError("the review list lacks columns: " + ", ".join(miss))
    rec = [dict(zip(head, r)) for r in rows[1:] if r[0]]
    no_pair = {r[0]: r[1] for r in conn.execute(
        "SELECT g.term_id, t.surface FROM surface_network_group g JOIN surface_term t ON t.id=g.term_id WHERE g.deleted=0 AND g.kind='no_pair'")}
    listed = {r["surface"] for r in rec}
    extra, missing = sorted(listed - set(no_pair.values())), sorted(set(no_pair.values()) - listed)
    if extra or missing:
        raise RelationError(f"the review list and the live no-pair surfaces differ: {len(extra)} listed but not no_pair {extra[:8]}; "
                            f"{len(missing)} no_pair but not listed {missing[:8]}")
    tid = {v: k for k, v in no_pair.items()}
    have = {r[0] for r in conn.execute("SELECT subject_id FROM surface_flag WHERE deleted=0 AND kind='wordnet_no_pair' AND subject_kind='surface_term'")}
    todo = []
    for n, r in enumerate(rec, 2):
        if tid[r["surface"]] in have:
            continue
        note = (f"[{r['manual_intervention']}] who acts: {r['who_acts']}. Why no pair: {r['b_reason_kind']}" + (f" ({r['b_detail']})" if r["b_detail"] else "")
                + f". Claude's reading from the meaning (for the researcher's scrutiny): {r['a_inner_being_or_behaviour']}"
                + (f", {r['a_note']}" if r["a_note"] else ""))
        todo.append((tid[r["surface"]], note, f"{p.name}#review row {n}"))
    cls = collections.Counter(re.sub(r"^\d+ ", "", r["manual_intervention"]) for r in rec)
    return {"todo": todo, "already": len(rec) - len(todo), "total": len(rec), "classes": cls}


def write_flags(conn, run_id: str, pl: dict, escalation_id: int) -> dict:
    conn.executemany("INSERT INTO surface_flag (subject_kind, subject_id, kind, note, status, escalation_id, run_id, created_by, load_ref) "
                     "VALUES ('surface_term', ?, 'wordnet_no_pair', ?, 'open', ?, ?, 'Claude', ?)",
                     [(i, note, escalation_id, run_id, ref) for i, note, ref in pl["todo"]])
    return {"flags": len(pl["todo"])}


# ------------------------------------------------------------------ validate
def validate(conn, cfg) -> dict:
    """WordNet same_base pairs and groups against surface_term.base_id. Reads only; writes nothing to base_id. A disagreement is a case to
    read (WordNet is an outside source and modern English), not a correction."""
    st = read_settings(cfg)
    src = st["rules"]["source"]
    surf = {i: s for i, s in scope_terms(conn, st["scope"])}
    base = {r[0]: r[1] for r in conn.execute("SELECT id, base_id FROM surface_term WHERE deleted=0")}
    grp = {r[0]: (r[1], r[2]) for r in conn.execute("SELECT term_id, group_no, kind FROM surface_network_group WHERE deleted=0")}
    sb_agree, sb_dis = 0, []
    for a, b in conn.execute("SELECT term_a_id, term_b_id FROM surface_relation WHERE deleted=0 AND source=? AND pair_type='same_base'", (src,)):
        (sb_agree, sb_dis) = (sb_agree + 1, sb_dis) if base.get(a) is not None and base.get(a) == base.get(b) else (sb_agree, sb_dis + [(a, b)])
    by_base = collections.defaultdict(list)
    for i in surf:
        if base.get(i) is not None:
            by_base[base[i]].append(i)
    multi = {b: ms for b, ms in by_base.items() if len(ms) >= 2}
    inside, split = 0, []
    for b, ms in multi.items():
        gs = {grp[i][0] for i in ms if i in grp and grp[i][1] != "no_pair"}
        nopair = [i for i in ms if i in grp and grp[i][1] == "no_pair"]
        if len(gs) == 1 and not nopair:
            inside += 1
        else:
            split.append((b, ms, sorted(gs), nopair))
    return {"surf": surf, "base": base, "same_base_agree": sb_agree, "same_base_disagree": sb_dis, "base_groups": len(multi), "base_inside": inside,
            "base_split": split}
