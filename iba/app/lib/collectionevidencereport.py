"""collectionevidencereport.py -- the Markdown report and the Excel workbook of the collection evidence data (escalation #2477; the data is built by lib/collectionevidence.py).

The report is a reading of stored rows, built up from what the collection stands on to what the study has recorded for it: the Strong's codes behind the member words,
each code's own occurrences (where the member surface is the code's own word) apart from the occurrences the surface only shares with another code's unit, the engagement
verdicts, the other observations, the claims (those resting on an observation of these words apart from those reached only because they cite a verse where a member word
stands), the narrative that tells them, the phrases attached, and the stored-data faults. Nothing is evaluated or inferred; a split is by a stored field (surface_kind, the
observation stage, deleted) and a count is a count of stored rows. Every row of every listing is also a row of the workbook, one sheet for each listing.

The values that are tunable (the catalogue stages, the engagement stage, the length a long text is cut to in the Markdown) are read from cfg_setting by the handler.
"""
from __future__ import annotations

import collections
import pathlib
import re

from .collectionevidence import COLLECTION_COLS

_ILLEGAL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
XLSX_CELL_MAX = 32000


# ══ derived from the stored rows, for both outputs ═══════════════════════════════════════════════
def _cell(v) -> str:
    return "" if v is None else str(v).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def _cut(v, n: int) -> str:
    t = "" if v is None else re.sub(r"\s+", " ", str(v)).strip()
    return t if len(t) <= n else t[:n].rstrip() + " ... (cut; the whole text is in the workbook)"


def _table(head: list, rows: list) -> list[str]:
    if not rows:
        return ["_no rows_", ""]
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(_cell(c) for c in r) + " |" for r in rows]
    return out + [""]


def _label(code, short) -> str:
    """A Strong's code with its native word, transliteration and gloss as stored: H3820A לֵב lev "heart"."""
    s = short.get(code)
    if not s:
        return str(code or "")
    return " ".join(x for x in (code, s[1], s[2]) if x) + (f' "{s[3]}"' if s[3] else "")


def _mark(text: str, surface: str) -> str:
    """The ESV text with the member word marked where its surface is found (the first whole-word match); the text as stored when it is not found."""
    if not text:
        return ""
    m = re.search(r"(?<![A-Za-z])" + re.escape(surface) + r"(?![A-Za-z])", text, re.I) if surface else None
    return text if m is None else text[:m.start()] + "**" + m.group(0) + "**" + text[m.end():]


def prepare(d: dict, v: dict) -> dict:
    """What both outputs need that is not already a stored row: the live observations and nodes of each occurrence, the engagement verdict of each occurrence, the
    observations of the engagement and of the other stages, the claims by what reaches them, and the withdrawn observations with their stored reason."""
    cat, eng = set(v["catalogue_stages"]), v["engagement_stage"]
    occ = d["occurrences"]
    obs = {o["id"]: o for o in d["observations"]}
    by_vl = {o["vl_id"]: o for o in occ}
    per = {o["vl_id"]: {"eng": [], "other": [], "cat": 0, "nodes_deleted_obs": 0} for o in occ}
    obs_vl = collections.defaultdict(set)
    for n in d["nodes"]:
        o = obs.get(n["observation_id"])
        if n["deleted"] or n["vl_id"] not in per:
            continue
        if o is None or o["deleted"]:
            per[n["vl_id"]]["nodes_deleted_obs"] += 1
            continue
        obs_vl[o["id"]].add(n["vl_id"])
        p = per[n["vl_id"]]
        if o["stage"] == eng:
            p["eng"].append(o["tag"])
        elif o["stage"] in cat:
            p["cat"] += 1
        else:
            p["other"].append(o["id"])
    live = [o for o in d["observations"] if not o["deleted"]]
    withdrawn = [o for o in d["observations"] if o["deleted"]]
    why = {}
    for c in d["changes"]:
        if c["node_id"] is None and c["column"] in ("deleted", "status") and str(c["new_value"]) in ("1", "withdrawn") and c["observation_id"] not in why:
            why[c["observation_id"]] = c["reason"]
    verse_occ = collections.defaultdict(list)
    for o in occ:
        verse_occ[o["verse_id"]].append(o)
    obs_of_claim, verse_of_claim = collections.defaultdict(list), collections.defaultdict(list)
    for s in d["claim_sources"]:
        (obs_of_claim if s["via"] == "observation" else verse_of_claim)[s["claim_id"]].append(s)
    claims = []
    for c in d["claims"]:
        via_obs = obs_of_claim.get(c["id"], [])
        via_verse = verse_of_claim.get(c["id"], [])
        reach_obs = []
        for s in via_obs:
            ob = obs.get(s["observation_id"])
            refs = sorted({by_vl[x]["reference"] for x in obs_vl.get(s["observation_id"], ()) if x in by_vl})
            reach_obs.append((s["observation_id"], ob["stage"] if ob else "", ob["tag"] if ob else "", "withdrawn" if (ob is None or ob["deleted"]) else "live", refs))
        reach_verse = []
        for s in via_verse:
            ws = verse_occ.get(s["verse_id"], [])
            reach_verse.append((s["verse_id"], s["ref_as_written"], sorted({(w["surface"], w["strong"]) for w in ws}, key=lambda x: (x[0], x[1] or ""))))
        told = [t for t in d["tellings"] if t["claim_id"] == c["id"]]
        claims.append({"claim": c, "obs": reach_obs, "verse": reach_verse, "told": told,
                       "reaches": "observation and verse" if reach_obs and reach_verse else "observation" if reach_obs else "verse"})
    return {"per": per, "obs": obs, "obs_vl": obs_vl, "live": live, "withdrawn": withdrawn, "why": why, "claims": claims, "by_vl": by_vl, "verse_occ": verse_occ,
            "eng_stage": eng, "cat_stages": cat, "text_chars": int(v["text_chars"])}


def _engagement_text(p: dict) -> str:
    return ", ".join(sorted(set(p["eng"]))) if p["eng"] else "none recorded"


def _code_groups(d: dict) -> dict:
    """The occurrences by Strong's code, each code's own occurrences (surface_kind own) apart from those the surface shares with another code's unit."""
    g = collections.OrderedDict()
    for o in d["occurrences"]:
        g.setdefault(o["strong"] or "(no code)", {"own": [], "other": []})["own" if o["surface_kind"] == "own" else "other"].append(o)
    return g


# ══ the Markdown report ══════════════════════════════════════════════════════════════════════════
def _meaning(code: str, ent: dict) -> list[str]:
    sh = ent["short"]
    if sh is None:
        return ["_no row in table strong for this code_", ""]
    head, own = ent.get("sense", (None, None))
    L = [f"- **Meaning as stored:** {sh[4]}; native word {sh[1]}, transliteration {sh[2]}; STEP gloss \"{sh[3]}\"" + (f"; sense head \"{head}\"" if head else "")
         + (" (the code is its own lemma)" if own else "") + "."]
    tree = ent["trees"][0] if ent["trees"] else []
    top = [_cut(t, 70) for _, c_, t in tree if c_ and len(re.findall(r"\d+|[a-z]", str(c_).rstrip(")"))) <= 1][:6]
    if top:
        L += ["- **Senses (first level of the meaning tree of the lemma " + ent["lemma"] + "):** " + "; ".join(top) + "."]
    rel = [f"{r[0]} {r[2] or ''} \"{r[3] or ''}\"".replace("  ", " ") for r in ent["related"][:6]]
    if rel:
        L += [f"- **Related terms ({len(ent['related'])}):** " + "; ".join(rel) + ("; more in the workbook." if len(ent["related"]) > 6 else ".")]
    if ent["clusters"]:
        L += ["- **Clusters (cluster_strong):** " + "; ".join(f"{r[0]} {r[1] or ''} ({r[2]})".replace("  ", " ") for r in ent["clusters"][:6]) + "."]
    L += [f"- **Counts, three measures as stored:** STEP token count {sh[5]}; verses STEP attests {ent['attested']}; verse_lexical rows the parse found {ent['lexical']}."]
    return L + [""]


def _occ_table(occ: list, P: dict, short: dict, shared: bool) -> list[str]:
    rows = []
    for o in occ:
        p = P["per"][o["vl_id"]]
        other = ", ".join(str(i) for i in sorted(set(p["other"]))) or "-"
        base = [o["reference"], o["surface"]]
        if shared:
            base += [_label(o["strong"], short), o["unit_surface"], o["unit_role"], o["unit_size"]]
        else:
            base += [o["morph"]]
        rows.append(base + [_engagement_text(p), other, p["cat"], _mark(o["text"], o["surface"])])
    head = ["reference", "member word"] + (["code", "unit word", "unit role", "unit size"] if shared else ["morph"]) + \
           ["engagement", "other observations", "catalogue observations", "verse (ESV)"]
    return _table(head, rows)


def _body_collection(d: dict, P: dict) -> list[str]:
    short = d["strong_short"]
    c = d["collection"]
    groups = _code_groups(d)
    occ = d["occurrences"]
    ordered = sorted(groups.items(), key=lambda kv: (-len(kv[1]["own"]), kv[0]))
    with_own = [kv for kv in ordered if kv[1]["own"]]
    L = [f"## 2. The collection {c['name']} at a glance", "",
         f"Status {c['status']}; core term {c['core_term_id']}; created {c['created_at']}, updated {c['updated_at']}; run {c['run_id']}. All the collection's fields are in the "
         "workbook sheet `Collection`, all its links in `Links`.", ""]
    nocc = collections.Counter(o["surface"] for o in occ)
    nverse = collections.defaultdict(set)
    for o in occ:
        nverse[o["surface"]].add(o["verse_id"])
    L += [f"### 2.1 The member words ({len(d['terms'])})", "",
          "A member is a term reached by a live link of the member tiers (" + ", ".join(d["tiers"]) + "), the term itself and the terms whose base it is.", ""]
    L += _table(["word", "form", "tiers", "base", "collection_state", "occurrences", "verses"],
                [[t["surface"], t["form"], t["tiers"], t["base"], t["collection_state"], nocc.get(t["surface"], 0), len(nverse.get(t["surface"], ()))] for t in d["terms"]])
    L += [f"### 2.2 The Strong's codes behind the members ({len(groups)})", "",
          "Each English member word translates one or more Hebrew or Greek words in the verses. This table is what the collection stands on: for each code, how many "
          "occurrences are the member surface's own word for it and how many only share it, and what the study has recorded.", ""]
    rows = []
    for code, g in ordered:
        allo = g["own"] + g["other"]
        eng = collections.Counter(t for o in allo for t in set(P["per"][o["vl_id"]]["eng"]))
        sur = collections.Counter(o["surface"] for o in g["own"])
        rows.append([_label(code, short), len(g["own"]), len(g["other"]), len({o["verse_id"] for o in allo}),
                     ", ".join(f"{w} {n}" for w, n in sur.most_common()),
                     ", ".join(f"{t} {n}" for t, n in sorted(eng.items())) or "none",
                     sum(1 for o in allo if P["per"][o["vl_id"]]["other"])])
    L += _table(["code", "own occurrences", "shared occurrences", "verses", "member words (own)", "engagement verdicts", "occurrences with other observations"], rows)
    L += ["## 3. Each Strong's code behind the collection", "",
          "Each section is one code: what it means as stored, the member words that carry it, and its occurrences in Scripture order with the verse and the member word marked. "
          f"The occurrences where the member surface is only shared with another code's unit are in section 3.{len(with_own) + 1}.", ""]
    for n, (code, g) in enumerate(with_own, 1):
        own = g["own"]
        L += [f"### 3.{n} {_label(code, short)}: {_n(len(own), 'own occurrence')} in {_n(len({o['verse_id'] for o in own}), 'verse')}", ""]
        if code in d["strongs"]:
            L += _meaning(code, d["strongs"][code])
        sur = collections.Counter(o["surface"] for o in own)
        eng = collections.Counter(_engagement_text(P["per"][o["vl_id"]]) for o in own)
        L += ["- **Carried by the member words:** " + ", ".join(f"{w} ({k})" for w, k in sur.most_common()) + ".",
              "- **Engagement of these occurrences:** " + ", ".join(f"{t} {k}" for t, k in eng.most_common()) + ".", ""]
        L += _occ_table(own, P, short, False)
    other = [o for _, g in groups.items() for o in g["other"]]
    other.sort(key=lambda o: (o["strong"] or "", o["sk"], o["position"] or 0, o["vl_id"]))
    L += [f"### 3.{len(with_own) + 1} Occurrences where the member surface is shared with another code's unit ({len(other)})", "",
          "In these verse_lexical rows the member word is the surface of a unit of two or more content codes (surface_kind shared); the code shown is one of the unit's codes, "
          "and the unit word is the whole unit's word. They are listed apart so they are not read as the code's own word. Nothing here is judged an error.", ""]
    L += _occ_table(other, P, short, True)
    return L


def _body_verse(d: dict, P: dict) -> list[str]:
    short = d["strong_short"]
    L = ["## 2. The verses requested", ""]
    L += _table(["reference", "as asked", "word rows", "text (ESV)"],
                [[v["reference"], v["asked"], len(P["verse_occ"].get(v["verse_id"], [])), v["text"]] for v in d["verses"]])
    L += ["## 3. The words of each verse", "",
          "Each verse with all its words (live verse_lexical rows): the Strong's code, how far the surface is the code's own, the collections and tiers the surface belongs to, "
          "and what the study has recorded.", ""]
    for v in d["verses"]:
        ws = P["verse_occ"].get(v["verse_id"], [])
        L += [f"### {v['reference']}", "", f"> {v['text']}", ""]
        L += _table(["word", "code", "surface_kind", "unit word", "collections (tier)", "engagement", "other observations", "catalogue observations"],
                    [[o["surface"], _label(o["strong"], short), o["surface_kind"], o["unit_surface"], o["memb"], _engagement_text(P["per"][o["vl_id"]]),
                      ", ".join(str(i) for i in sorted(set(P["per"][o["vl_id"]]["other"]))) or "-", P["per"][o["vl_id"]]["cat"]] for o in ws])
    return L


def _obs_line(o: dict, P: dict, n: int) -> list[str]:
    occ = sorted((P["by_vl"][x] for x in P["obs_vl"].get(o["id"], ()) if x in P["by_vl"]), key=lambda x: (x["sk"], x["vl_id"]))
    refs = list(dict.fromkeys(f"{x['reference']} ({x['surface']})" for x in occ))
    L = [f"- **Observation {o['id']}** ({o['stage']}, tag {o['tag']}, status {o['status']}): {_cut(o['obs_text'], n)}"]
    for k in ("meaning", "implication", "chain"):
        if o[k]:
            L.append(f"  - {k}: {_cut(o[k], n)}")
    L.append(f"  - applies to {len(refs)} occurrence(s): " + ", ".join(refs[:12]) + (f"; and {len(refs) - 12} more (sheet `Observation nodes`)" if len(refs) > 12 else ""))
    return L


def _body_recorded(d: dict, P: dict) -> list[str]:
    n = P["text_chars"]
    occ = d["occurrences"]
    live, wd = P["live"], P["withdrawn"]
    eng_obs = [o for o in live if o["stage"] == P["eng_stage"]]
    cat_obs = [o for o in live if o["stage"] in P["cat_stages"]]
    other_obs = [o for o in live if o["stage"] != P["eng_stage"] and o["stage"] not in P["cat_stages"]]
    none = sum(1 for o in occ if not P["per"][o["vl_id"]]["eng"])
    L = ["## 4. What the study has recorded for these occurrences", "",
         f"Of {len(occ)} occurrences, {len(occ) - none} have an engagement observation and {none} have none recorded. There are {len(live)} live observations on them "
         f"({len(eng_obs)} engagement, {len(other_obs)} of other recorded stages, {len(cat_obs)} of the retired catalogue stages) and {len(wd)} withdrawn.", "",
         f"### 4.1 Engagement: what each word does for the inner being ({len(eng_obs)} observations)", "",
         "An engagement observation states, for the surface in a verse, whether it voices an inner-being operation (use, face) or is silent. Each is one statement applied to "
         "every occurrence it covers.", ""]
    for o in sorted(eng_obs, key=lambda o: (o["tag"] or "", o["id"])):
        L += _obs_line(o, P, n)
    if not eng_obs:
        L += ["_no engagement observation covers these occurrences_"]
    L += ["", f"### 4.2 Other recorded observations ({len(other_obs)})", "",
          "Observations of the stages that carry a written finding (prior-capture, reading, strand-reading and the like), each with the occurrences it applies to.", ""]
    for o in sorted(other_obs, key=lambda o: (o["stage"], o["id"])):
        L += _obs_line(o, P, n)
    if not other_obs:
        L += ["_none_"]
    c = collections.Counter((o["stage"], o["tag"]) for o in cat_obs)
    L += ["", f"### 4.3 The retired catalogue observations ({len(cat_obs)}, live)", "",
          "The September catalogue stages (" + ", ".join(sorted(P["cat_stages"])) + ") recorded one short verdict for each word in each verse. They are counted here by stage and tag; "
          "each one, with its text and nodes, is in the workbook sheets `Observations` and `Observation nodes`.", ""]
    L += _table(["stage", "tag", "live observations"], [[s, t, k] for (s, t), k in sorted(c.items(), key=lambda kv: (kv[0][0], -kv[1]))])
    cw = collections.Counter(o["stage"] for o in wd)
    rs = collections.Counter(P["why"].get(o["id"], "no change record") for o in wd)
    L += [f"### 4.4 Withdrawn observations ({len(wd)})", "",
          "A withdrawn observation (deleted = 1) is no longer a finding. They are counted here, and listed with their reason as stored in ib_observation_change in the workbook sheet "
          "`Withdrawn observations`; they are not part of the sections above.", ""]
    L += _table(["stage", "withdrawn observations"], [[s, k] for s, k in sorted(cw.items(), key=lambda kv: -kv[1])])
    L += _table(["reason as stored", "observations"], [[_cut(r, 160), k] for r, k in rs.most_common(8)])
    return L


def _told(x: dict) -> str:
    """Where a claim is told now (the current tellings); earlier tellings are counted, and listed in the workbook."""
    cur = [t for t in x["told"] if t["status"] == "current"]
    old = len(x["told"]) - len(cur)
    txt = "; ".join(dict.fromkeys(f"chapter {t['chapter_no']} {t['chapter_title'] or ''}, {t['heading']}".replace("  ", " ") for t in cur)) or "not told in a section"
    return txt + (f" ({old} earlier telling(s) in the workbook)" if old else "")


def _n(k: int, word: str) -> str:
    return f"{k} {word}" + ("" if k == 1 else "s")


def _body_claims(d: dict, P: dict) -> list[str]:
    n = P["text_chars"]
    direct = [x for x in P["claims"] if x["obs"]]
    byverse = [x for x in P["claims"] if not x["obs"]]
    L = ["## 5. Claims and the narrative", "",
         f"{len(P['claims'])} claims rest on these occurrences: {len(direct)} on an observation of these words and {len(byverse)} reached only because one of their sources is a verse "
         "where a member word stands. The second group is about its verse, not about the collection; it is kept so that nothing stored is hidden, and labelled.", "",
         f"### 5.1 Claims resting on an observation of these words ({len(direct)})", ""]
    for x in direct:
        c = x["claim"]
        L += [f"- **{c['claim_ref']}** ({c['origin']}, verdict {c['verdict']}, status {c['status']}, in narrative {c['in_narrative']}): {_cut(c['claim_text'], n)}",
              f"  - beyond the text: {_cut(c['beyond_text'], n)}",
              "  - rests on: " + "; ".join(f"observation {i} ({st} {tg}, {state}; " + ", ".join(r[:6]) + ")" for i, st, tg, state, r in x["obs"]),
              f"  - told in: {_told(x)}"]
    if not direct:
        L += ["_none_"]
    L += ["", f"### 5.2 Claims reached by a verse only ({len(byverse)})", "",
          "Each claim names the verse that reached it and the member word in that verse. Read it as a claim about the verse.", ""]
    L += _table(["claim", "claim text", "reached by verse", "member word and code in that verse", "status", "told in"],
                [[x["claim"]["claim_ref"], _cut(x["claim"]["claim_text"], n), "; ".join(dict.fromkeys(str(v[1] or v[0]) for v in x["verse"])),
                  "; ".join(dict.fromkeys(f"{w} {cd or ''}".strip() for v in x["verse"] for w, cd in v[2])), x["claim"]["status"], _told(x)] for x in byverse])
    secs = collections.OrderedDict()
    for x in P["claims"]:
        for t in x["told"]:
            secs.setdefault(t["section_id"], []).append(x["claim"]["claim_ref"])
    L += [f"### 5.3 The narrative sections that tell these claims ({len(d['sections'])})", "",
          "The text of each section is in the workbook sheet `Narrative`.", ""]
    L += _table(["section", "chapter", "heading", "claims told"],
                [[s["id"], f"{s['chapter_no']} {s['chapter_title'] or ''}".strip(), s["heading"], ", ".join(dict.fromkeys(secs.get(s["id"], [])))] for s in d["sections"]])
    return L


def _body_phrases(d: dict, P: dict | None = None) -> list[str]:
    ph = d.get("phrases") or []
    L = [f"## 6. Phrases attached to the collection ({len(ph)})", "",
         "A phrase is attached by the route in its link reason (a Strong's code or an English word shared with a member) and is a member of the collection: its occurrences "
         "are in sections 2 and 3 under their Strong's codes, and what the study recorded for them in sections 4 and 5. Each is shown here with its route, its occurrences and "
         "the live observation nodes whose word is the phrase.", ""]
    per = collections.Counter(o["surface"] for o in d["occurrences"])
    eng = collections.Counter(o["surface"] for o in d["occurrences"] if P is not None and P["per"][o["vl_id"]]["eng"])
    return L + _table(["phrase", "link", "route", "occurrences", "with engagement", "live nodes on the phrase", "observations"],
                      [[p["phrase"], p["link"], _cut(p["route"], 220), per.get((p["phrase"] or "").strip().lower(), 0), eng.get((p["phrase"] or "").strip().lower(), 0),
                        p["nodes"], p["observations"]] for p in ph])


def _body_faults(d: dict, limit: int = 25) -> list[str]:
    L = ["## 7. Stored-data faults", "",
         "Blatant errors and omissions in the stored rows, each found by the rule stated. A fault is shown with the rows that identify it; the first " + str(limit) +
         " of a long list are shown and every row is in the workbook sheet `Faults`.", ""]
    L += _table(["rule", "what it looks for", "found"], [[f["key"], f["how"], len(f["rows"])] for f in d["faults"]])
    for f in d["faults"]:
        if not f["rows"]:
            continue
        L += [f"### {f['key']}: {len(f['rows'])} found", ""]
        if f["key"] == "live-node-on-deleted-observation":
            c = collections.Counter((r[2], r[3], r[4]) for r in f["rows"])
            L += _table(["observation stage", "tag", "status", "nodes"], [list(k) + [v] for k, v in c.most_common(12)])
        L += _table(f["cols"], f["rows"][:limit])
        if len(f["rows"]) > limit:
            L += [f"_{len(f['rows']) - limit} more in the workbook sheet `Faults`_", ""]
    return L


def render(datas: list[dict], vals: dict, run_id: str, stamp: str, wb_name: str) -> str:
    """The Markdown report of one or more collections, or of a verse list."""
    verse = datas[0]["kind"] == "verse"
    title = ("Verse evidence report: " + datas[0]["name"]) if verse else "Collection evidence report: " + ", ".join(d["name"] for d in datas)
    L = [f"# {title}", "",
         f"Generated {stamp} by run {run_id} (`Collection-Build.ps1 -Action Evidence`, escalations #2464, #2467 and #2477). Companion workbook: `{wb_name}`. "
         "Every statement below is a stored table entry or a count of stored rows; nothing is evaluated or inferred and nothing was written to a table. "
         "The joins are in `iba/app/lib/collectionevidence.py`; the report is built by `iba/app/lib/collectionevidencereport.py`.", ""]
    for d in datas:
        P = prepare(d, vals)
        L += ["## 1. What this report holds and how to read it", "",
              ("A verse list: every word of each verse, with the collections each word belongs to and what the study has recorded for it. " if verse else
               "A collection: the member words, the Strong's codes behind them, and what the study has recorded for the occurrences of those words, from the base data through "
               "the observations and the claims into the narrative. ")
              + "Sections 2 and 3 say what the data is; 4 and 5 say what the study has recorded; " + ("" if verse else "6 lists the phrases; ") +
              "7 lists the faults found in the stored rows. Verses are in Scripture order (book in cfg_book_order, chapter, verse). The detail that does not fit a reading "
              "(every Strong's entry in full, every observation and node, the change history, the narrative text) is in the workbook, one sheet for each listing; the sheet is "
              "named where it is cited.", ""]
        L += _body_verse(d, P) if verse else _body_collection(d, P)
        L += _body_recorded(d, P)
        L += _body_claims(d, P)
        L += [] if verse else _body_phrases(d, P)
        L += _body_faults(d)
        L += ["## 8. Sources", "",
              "Occurrences: live verse_lexical rows, with the verse text from table `verse`; Strong's data from `strong`, `strong_sense`, `strong_meaning_tree`, `strong_related`, "
              "`cluster_strong`; observations and nodes from `ib_observation` and `ib_node` (an observation is withdrawn when deleted = 1); claims from `narrative_claim_source` "
              "(by observation_id or verse_id), `narrative_claim`, `narrative_claim_telling` and `narrative_section`. A table or column was used only after its recorded meaning "
              "in `cfg_table` and `cfg_column` was read (rule B:123).", ""]
    return "\n".join(L) + "\n"


# ══ the Excel workbook ═══════════════════════════════════════════════════════════════════════════
def sheets(datas: list[dict], vals: dict) -> list[dict]:
    """The listings of the report, each as one sheet: name, what it lists, why, its source tables, header and rows (every row of the stored listing)."""
    out = []

    def add(name, lists, why, source, head, rows):
        out.append({"name": name, "lists": lists, "why": why, "source": source, "head": head, "rows": rows})
    Ps = [prepare(d, vals) for d in datas]
    kind = datas[0]["kind"]

    def lead(d):
        return d["name"] if d["kind"] == "collection" else "verses"

    def each(f):
        return [r for d, P in zip(datas, Ps) for r in f(d, P)]
    if kind == "collection":
        add("Collection", "the fields of each collection", "what the collection is, as stored", "collection", ["collection", "field", "value"],
            each(lambda d, P: [[d["name"], k, d["collection"][k]] for k in COLLECTION_COLS]))
        add("Links", "every link of the collection, live first, then removed or superseded", "how each term stands in the collection and why", "collection_link, surface_term",
            ["collection", "link", "tier", "term_id", "word", "shared", "deleted", "superseded_by", "reason", "ai_call", "run", "by", "created", "load_ref"],
            each(lambda d, P: [[d["name"], x["id"], x["tier"], x["term_id"], x["surface"], x["shared"], x["deleted"], x["superseded_by_id"], x["reason"], x["ai_call_id"],
                                x["run_id"], x["created_by"], x["created_at"], x["load_ref"]] for x in d["links"]]))
        add("Members", "the member terms of the collection", "the words whose occurrences the report reads", "surface_term, collection_link",
            ["collection", "term_id", "word", "form", "origin", "tiers", "via links", "group", "group_state", "base", "base_source", "base_state", "collection_state", "occurrences"],
            each(lambda d, P: [[d["name"], t["term_id"], t["surface"], t["form"], t["origin"], t["tiers"], t["links"], t["group"], t["group_state"], t["base"], t["base_source"],
                                t["base_state"], t["collection_state"], sum(1 for o in d["occurrences"] if o["surface"] == t["surface"])] for t in d["terms"]]))
    else:
        add("Verses", "the verses requested", "the scope of the verse report", "verse", ["reference", "osisId", "verse_id", "as asked", "word rows", "text"],
            [[v["reference"], v["osis"], v["verse_id"], v["asked"], len(Ps[0]["verse_occ"].get(v["verse_id"], [])), v["text"]] for v in datas[0]["verses"]])

    def occ_rows(d, P):
        short = d["strong_short"]
        for o in d["occurrences"]:
            p = P["per"][o["vl_id"]]
            sh = short.get(o["strong"]) or (None,) * 4
            yield [lead(d), o["memb"], o["surface"], o["reference"], o["vl_id"], o["strong"], sh[1], sh[2], sh[3], o["morph"], o["position"], o["surface_kind"],
                   "own" if o["surface_kind"] == "own" else "shared with another code's unit", o["unit_surface"], o["unit_role"], o["unit_size"], o["vl_role"], o["is_negator"],
                   o["party_kind"], o["status"], _engagement_text(p), ", ".join(str(i) for i in sorted(set(p["other"]))), p["cat"], p["nodes_deleted_obs"], o["text"]]
    add("Occurrences", "every occurrence of the member words (live verse_lexical rows)", "the base data the rest of the report stands on; sort or filter by code or by kind",
        "verse_lexical, verse, ib_node, ib_observation",
        ["scope", "tiers", "word", "reference", "vl_id", "Strong's code", "native word", "transliteration", "STEP gloss", "morph", "position", "surface_kind", "kind",
         "unit word", "unit role", "unit size", "role (clusters)", "negator", "party", "status", "engagement", "other observations", "catalogue observations",
         "live nodes on withdrawn observations", "verse (ESV)"],
        each(lambda d, P: list(occ_rows(d, P))))
    codes = {}
    for d in datas:
        for code, ent in d["strongs"].items():
            codes.setdefault(code, ent)

    def count(code, own):
        return sum(1 for d in datas for o in d["occurrences"] if o["strong"] == code and (o["surface_kind"] == "own") == own)
    blank = (None,) * 7
    add("Strongs codes", "every Strong's code of the occurrences, with its stored head data", "what each code is, and how many occurrences are its own word and how many shared",
        "strong, strong_sense, strong_verse, verse_lexical",
        ["code", "language", "native word", "transliteration", "STEP gloss", "sense head", "own lemma", "lemma", "STEP token count", "verses STEP attests",
         "verse_lexical rows", "own occurrences in scope", "shared occurrences in scope", "origin"],
        [[c, (e["short"] or blank)[4], (e["short"] or blank)[1], (e["short"] or blank)[2], (e["short"] or blank)[3], (e.get("sense") or (None, None))[0],
          (e.get("sense") or (None, None))[1], e["lemma"], (e["short"] or blank)[5], e["attested"], e["lexical"], count(c, True), count(c, False),
          (e["short"] or blank)[6]] for c, e in sorted(codes.items())])
    tree_rows, rel_rows, lsj_rows, mou_rows, clu_rows = [], [], [], [], []
    for c, e in sorted(codes.items()):
        for i, tr in enumerate(e["trees"], 1):
            for did, code_, text in tr:
                tree_rows.append([c, e["lemma"], i, did, code_, text])
        rel_rows += [[c] + list(r) for r in e["related"]]
        lsj_rows += [[c] + list(r) for r in e["lsj"]]
        mou_rows += [[c] + list(r) for r in e["mounce"]]
        clu_rows += [[c] + list(r) for r in e["clusters"]]
    add("Meaning trees", "the stored meaning trees of each code's lemma", "the senses of the word, as stored", "strong_meaning_tree", ["code", "lemma", "tree", "row", "sense code", "sense text"], tree_rows)
    add("Related terms", "the related terms of each code", "the words stored as related to it", "strong_related", ["code", "related code", "native", "transliteration", "gloss"], rel_rows)
    add("LSJ senses", "the LSJ senses of each Greek code", "the classical lexicon's senses as stored", "strong_lsj_parsed", ["code", "sense", "gloss", "note", "row type"], lsj_rows)
    add("Mounce", "the Mounce entries of each Greek code", "the NT lexicon's entries as stored", "strong_mounce_parsed", ["code", "Mounce", "row type"], mou_rows)
    add("Cluster assignments", "the clusters each code is assigned to", "where the study has placed the word", "cluster_strong, cluster",
        ["code", "cluster", "name", "confidence", "operation", "review flag", "alternatives", "rationale", "source"], clu_rows)
    place = {}
    for d in datas:
        place.update(d["placements"])
    add("Placements", "the placement of each (code, surface) pair in subgroups, with concept and domain", "which subgroup of meaning each member word's use was allocated to",
        "surface_subgroup, cluster_subgroup, concept, concept_domain",
        ["code", "surface", "cluster", "subgroup", "label", "core description", "status", "two sense", "allocated by", "reason", "concept", "domain"],
        [[k[0], k[1]] + list(r) for k, rows in sorted(place.items()) for r in rows])
    obs_cols = ("id", "stage", "tag", "status", "strong", "window", "route", "basis", "obs_text", "setting", "meaning", "implication", "chain", "parties", "parts", "revisit_note",
                "supersedes_observation_id", "run_id", "created_at", "updated_at")
    add("Observations", "every live observation on the occurrences, all stages", "what the study recorded, one row for each finding", "ib_observation, ib_node",
        ["scope"] + list(obs_cols) + ["nodes (all)", "occurrences in scope"],
        each(lambda d, P: [[lead(d)] + [o[k] for k in obs_cols] + [len(d["obs_nodes"].get(o["id"], [])), len(P["obs_vl"].get(o["id"], ()))] for o in P["live"]]))

    def node_rows(d, P):
        ref = {osis: v[0] for osis, v in d["verse_text"].items()}
        for o in P["live"]:
            for n in d["obs_nodes"].get(o["id"], []):
                yield [lead(d), o["id"], o["stage"], o["tag"], n["id"], ref.get(n["verse_reference"], n["verse_reference"]), n["surface"], n["strong"], n["role"], n["disposition"],
                       n["disposition_note"], n["cluster"], n["subgroup"], n["vl_id"], "yes" if n["vl_id"] in d["scope_vl"] else "no", n["deleted"]]
    add("Observation nodes", "every node of every live observation, in or out of the scope", "where each finding applies: the verse, the word and its role", "ib_node",
        ["scope", "observation", "stage", "tag", "node", "verse", "word", "Strong's code", "role", "disposition", "disposition note", "cluster", "subgroup", "vl_id",
         "occurrence in scope", "node deleted"], each(lambda d, P: list(node_rows(d, P))))
    add("Withdrawn observations", "every observation on the occurrences that is withdrawn (deleted = 1)", "kept apart so that no withdrawn finding is read as a finding",
        "ib_observation, ib_observation_change",
        ["scope", "observation", "stage", "tag", "status", "Strong's code", "obs_text", "reason as stored", "nodes (all)"],
        each(lambda d, P: [[lead(d), o["id"], o["stage"], o["tag"], o["status"], o["strong"], o["obs_text"], P["why"].get(o["id"], "no change record"),
                            len(d["obs_nodes"].get(o["id"], []))] for o in P["withdrawn"]]))
    add("Change history", "every change to these observations and their nodes", "the record of what was altered and why", "ib_observation_change",
        ["scope", "id", "observation", "node", "column", "old", "new", "reason", "reading", "run", "created", "by"],
        each(lambda d, P: [[lead(d), x["id"], x["observation_id"], x["node_id"], x["column"], x["old_value"], x["new_value"], x["reason"], x["reading_id"], x["run_id"],
                            x["created_at"], x["created_by"]] for x in d["changes"]]))

    def claim_rows(d, P):
        for x in P["claims"]:
            c = x["claim"]
            yield [lead(d), c["claim_ref"], c["id"], c["origin"], c["verdict"], c["part_verdict"], c["status"], c["in_narrative"], c["i_read"], x["reaches"], c["claim_text"],
                   c["beyond_text"], "; ".join(f"observation {i} ({st} {tg}, {state}): " + ", ".join(r) for i, st, tg, state, r in x["obs"]),
                   "; ".join(f"{v[1] or v[0]}: " + ", ".join(f"{w} {cd or ''}".strip() for w, cd in v[2]) for v in x["verse"]), _told(x)]
    add("Claims", "every claim that rests on these occurrences", "what the register holds about them; the column reaches by says whether an observation of these words or only a verse reached the claim",
        "narrative_claim, narrative_claim_source, narrative_claim_telling",
        ["scope", "claim", "id", "origin", "verdict", "part verdict", "status", "in narrative", "i read", "reaches by", "claim text", "beyond text",
         "rests on observation", "reached by verse (member word and code)", "told in"], each(lambda d, P: list(claim_rows(d, P))))
    add("Claim sources", "every source row that reaches these occurrences", "the link between a claim and the observation or verse it rests on", "narrative_claim_source",
        ["scope", "source", "via", "claim", "kind", "verse_id", "reference as written", "observation", "note", "by"],
        each(lambda d, P: [[lead(d), s["id"], s["via"], next((c["claim_ref"] for c in d["claims"] if c["id"] == s["claim_id"]), s["claim_id"]), s["source_kind"], s["verse_id"],
                            s["ref_as_written"], s["observation_id"], s["note"], s["created_by"]] for s in d["claim_sources"]]))
    add("Narrative", "the narrative sections that tell these claims, with their text", "where the claims are told in the study's narrative",
        "narrative_claim_telling, narrative_section, narrative_chapter",
        ["scope", "section", "chapter", "heading", "level", "last version", "claims told", "text of the section"],
        each(lambda d, P: [[lead(d), s["id"], f"{s['chapter_no']} {s['chapter_title'] or ''}".strip(), s["heading"], s["level"], s["last_version"],
                            ", ".join(dict.fromkeys(x["claim"]["claim_ref"] for x in P["claims"] for t in x["told"] if t["section_id"] == s["id"])), s["block_text"]]
                           for s in d["sections"]]))
    if kind == "collection":
        add("Phrases", "the phrases attached to the collection (tier phrase)", "phrases are members of the collection; each is shown with its route and the observations that name it",
            "collection_link, ib_node",
            ["collection", "phrase", "term_id", "link", "route", "occurrences", "live nodes on the phrase", "observations", "run", "by", "created"],
            each(lambda d, P: [[d["name"], p["phrase"], p["term_id"], p["link"], p["route"], sum(1 for o in d["occurrences"] if o["surface"] == (p["phrase"] or "").strip().lower()), p["nodes"], p["observations"], p["run"], p["by"], p["created"]] for p in d["phrases"]]))
    fa = []
    for d in datas:
        for f in d["faults"]:
            for r in f["rows"]:
                fa.append([lead(d), f["key"], f["how"], " | ".join(f"{c}: {x}" for c, x in zip(f["cols"], r))] + list(r) + [""] * (8 - len(r)))
    add("Faults", "every stored-data fault found, one row for each", "blatant errors and omissions, each with the rule that found it", "the tables named by each rule",
        ["scope", "rule", "what it looks for", "finding", "col 1", "col 2", "col 3", "col 4", "col 5", "col 6", "col 7", "col 8"], fa)
    return out


def _clean(v):
    if isinstance(v, str):
        v = _ILLEGAL.sub(" ", v)
        return v if len(v) <= XLSX_CELL_MAX else v[:XLSX_CELL_MAX] + " ... (cut at the cell limit)"
    return v


def write_workbook(path: pathlib.Path, datas: list[dict], vals: dict, run_id: str, stamp: str) -> list[dict]:
    """Write the workbook: a `Read me` sheet, then one sheet for each listing. Returns the listings (name, row count)."""
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    sh = sheets(datas, vals)
    wb = Workbook()
    ws = wb.active
    ws.title = "Read me"
    ws.append([f"Collection evidence workbook, generated {stamp} by run {run_id}. The Markdown report of the same name is the reading; each sheet here is one listing in full, "
               "a view of the stored rows, nothing evaluated or inferred, nothing written to a table."])
    ws.append([])
    ws.append(["sheet", "what it lists", "why it is listed", "source tables", "rows"])
    for s in sh:
        ws.append([s["name"], s["lists"], s["why"], s["source"], len(s["rows"])])
    for sdef in sh:
        w = wb.create_sheet(sdef["name"][:31])
        w.append(sdef["head"])
        for r in sdef["rows"]:
            w.append([_clean(x) for x in r])
        for c in w[1]:
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = PatternFill("solid", fgColor="305496")
            c.alignment = Alignment(vertical="top", wrap_text=True)
        w.freeze_panes = "A2"
        if sdef["rows"]:
            w.auto_filter.ref = w.dimensions
        for i, h in enumerate(sdef["head"], 1):
            longest = max([len(str(h))] + [len(str(r[i - 1])) for r in sdef["rows"][:200] if i - 1 < len(r) and r[i - 1] is not None])
            w.column_dimensions[get_column_letter(i)].width = max(8, min(60, longest + 2))
    for c in ws[3]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="305496")
    ws["A1"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells("A1:E1")
    ws.row_dimensions[1].height = 48
    for col, wdt in zip("ABCDE", (24, 56, 56, 40, 8)):
        ws.column_dimensions[col].width = wdt
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    return [{"name": s["name"], "rows": len(s["rows"])} for s in sh]
