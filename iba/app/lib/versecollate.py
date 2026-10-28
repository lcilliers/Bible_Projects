"""versecollate.py -- what is known, and what is missing, for a scope (escalation #2228 tools 3-5; design
outputs/escalation/2228-verse-collate-design-v1-20261023.md).

The scope comes from versescope.resolve (with its guard). For every verse, one set-based query per source:
its text, its inner-being words (verse_lexical joined to the M clusters), verse_meta.status, the draft
observations on it (ib_node), the strand hits, the claims resting on it and the blocks that tell them, the
blocks citing it, the open thread items that match it (escalation.match_open_items, as Match does), and the
lines of the cluster files that name it (reading_ref; only those lines are read, never a whole file). The
lexicon is given once per strong. Then the gaps per verse. Reads only.
"""
from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import re
import time

from . import escalation
from . import versescope as vs
from .db import Db

GAPS = ("not read", "read in files only", "hit unread", "observed, no claim", "claim not told", "open item",
        "meaning missing")


class CollateError(ValueError):
    """Stopped by the guard: the scope is too wide to collate in the time allowed."""


def _ids(xs) -> str:
    return json.dumps(sorted(set(xs)))


def _disposition(note: str | None) -> str | None:
    m = re.search(r"October disposition:\s*([^;.(]+)", note or "")
    return m.group(1).strip() if m else None


def collate(cfg, request: dict, root: pathlib.Path) -> dict:
    """The collation for a normalised request (versescope.normalise_request). Raises vs.ScopeError (the scope)
    or CollateError (past verse_collate.max_seconds)."""
    t0 = time.monotonic()
    max_seconds = float(cfg.required_setting("verse_collate.max_seconds"))

    def check(step: str):
        if time.monotonic() - t0 > max_seconds:
            raise CollateError(f"collating stopped at the time limit (verse_collate.max_seconds {max_seconds:g}) "
                               f"while {step}; reform the scope to a narrower one")

    scope = vs.resolve(cfg, request)
    conn = cfg.conn
    vids = [v["verse_id"] for v in scope["verses"]]
    J = _ids(vids)
    rec = {v["verse_id"]: {"verse_id": v["verse_id"], "reference": v["reference"], "osis": v["osis"],
                           "routes": v["routes"], "occurrences": v["occurrences"], "text": None, "status": None,
                           "words": [], "surfaces": [], "observations": [],
                           "strand_hits": [], "claims": [], "narrative": [], "open_items": [], "file_lines": [],
                           "gaps": []} for v in scope["verses"]}

    for vid, text, status in conn.execute(
            "SELECT v.id, v.text, m.status FROM verse v LEFT JOIN verse_meta m ON m.verse_id=v.id "
            "WHERE v.id IN (SELECT value FROM json_each(?))", (J,)):
        rec[vid]["text"], rec[vid]["status"] = text, status

    strongs: set[str] = set()
    clusters: set[str] = set()
    for vid, surface, strong, cl, name in conn.execute(
            "SELECT vl.verse_id, vl.surface, vl.strong, cs.cluster_code, c.short_name FROM verse_lexical vl "
            "JOIN cluster_strong cs ON cs.strong=vl.strong AND cs.deleted=0 AND cs.cluster_code LIKE 'M%' "
            "LEFT JOIN cluster c ON c.cluster_code=cs.cluster_code "
            "WHERE vl.deleted=0 AND vl.verse_id IN (SELECT value FROM json_each(?)) ORDER BY vl.verse_id, vl.position",
            (J,)):
        rec[vid]["words"].append({"surface": surface, "strong": strong, "cluster": cl, "cluster_name": name})
        strongs.add(strong)
        clusters.add(cl)
    # every surface occurrence of the verse (the path verse_lexical -> cluster_strong -> surface_subgroup ->
    # cluster_subgroup, #2312): its clusters and its subgroups
    cl_of = collections.defaultdict(set)
    for strong, cl in conn.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"):
        cl_of[strong].add(cl)
    sub_of = collections.defaultdict(set)
    for cl, strong, surface, sg in conn.execute(
            "SELECT s.cluster_code, s.strong, s.surface, g.subgroup_code FROM surface_subgroup s JOIN cluster_subgroup g "
            "ON g.id=s.cluster_subgroup_id WHERE s.deleted=0"):
        sub_of[(strong, surface)].add(sg)
    for vid, vlid, pos, surface, strong, morph in conn.execute(
            "SELECT verse_id, id, position, surface, strong, morph_code FROM verse_lexical WHERE deleted=0 AND "
            "verse_id IN (SELECT value FROM json_each(?)) ORDER BY verse_id, position, id", (J,)):
        rec[vid]["surfaces"].append({"occurrence": vlid, "position": pos, "surface": surface, "strong": strong,
                                     "morph": morph, "clusters": sorted(cl_of.get(strong, ())),
                                     "subgroups": sorted(sub_of.get((strong, surface), ()))})
    check("reading the words")

    # every observation of the verse that is not withdrawn (any stage, any status), with the nodes that apply it to
    # this verse: the surface occurrence (verse_lexical_id), its role and its subgroup (#2312, #2276)
    obs_at: dict = {}
    for vid, oid, stage, tag, text, basis, note, status in conn.execute(
            "SELECT DISTINCT v.id, o.id, o.stage, o.tag, coalesce(o.meaning, o.obs_text), o.basis, o.revisit_note, "
            "o.status FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference JOIN ib_observation o ON "
            "o.id=n.observation_id AND o.deleted=0 WHERE v.id IN (SELECT value FROM json_each(?)) "
            "ORDER BY v.id, o.id", (J,)):
        obs_at[(vid, oid)] = {"id": oid, "stage": stage, "tag": tag, "status": status, "text": text, "basis": basis,
                              "october_disposition": _disposition(note), "nodes": []}
        rec[vid]["observations"].append(obs_at[(vid, oid)])
    for vid, oid, nid, strong, surface, role, vlid, sg in conn.execute(
            "SELECT v.id, n.observation_id, n.id, n.strong, n.surface, n.role, n.verse_lexical_id, "
            "n.cluster_subgroup_code FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference WHERE v.id IN "
            "(SELECT value FROM json_each(?)) AND n.deleted=0 "
            "ORDER BY n.id", (J,)):
        if (vid, oid) in obs_at:
            obs_at[(vid, oid)]["nodes"].append({"node": nid, "strong": strong, "surface": surface, "role": role,
                                                "verse_lexical_id": vlid, "subgroup": sg})
    for vid, code, strong, surface, face, reason, oid in conn.execute(
            "SELECT h.verse_id, s.code, h.strong, h.surface, h.face, h.reason, h.observation_id FROM reading_strand_hit h "
            "JOIN reading_strand s ON s.id=h.strand_id WHERE h.verse_id IN (SELECT value FROM json_each(?))", (J,)):
        rec[vid]["strand_hits"].append({"strand": code, "strong": strong, "surface": surface, "face": face,
                                        "reason": reason, "observation_id": oid})
    check("reading observations and strand hits")

    tellings = collections.defaultdict(list)
    for cid, chap, head in conn.execute(
            "SELECT t.claim_id, ch.chapter_no, s.heading FROM narrative_claim_telling t "
            "JOIN narrative_section s ON s.id=t.section_id AND s.last_version IS NULL "
            "JOIN narrative_chapter ch ON ch.id=s.chapter_id AND ch.inactive=0 WHERE t.status='current' AND t.claim_id IN "
            "(SELECT claim_id FROM narrative_claim_source WHERE verse_id IN (SELECT value FROM json_each(?)))", (J,)):
        tellings[cid].append(f"{chap} / {head}")
    for vid, cid, ref, text, status in conn.execute(
            "SELECT DISTINCT s.verse_id, c.id, c.claim_ref, c.claim_text, c.status FROM narrative_claim_source s "
            "JOIN narrative_claim c ON c.id=s.claim_id WHERE s.verse_id IN (SELECT value FROM json_each(?)) "
            "AND c.status IN ('current', 'held') ORDER BY s.verse_id, c.id", (J,)):
        rec[vid]["claims"].append({"claim": ref, "text": text, "status": status, "told_in": tellings.get(cid, [])})
    for vid, chap, head in conn.execute(
            "SELECT DISTINCT ci.verse_id, ch.chapter_no, s.heading FROM narrative_citation ci "
            "JOIN narrative_section s ON s.id=ci.section_id AND s.last_version IS NULL "
            "JOIN narrative_chapter ch ON ch.id=s.chapter_id AND ch.inactive=0 "
            "WHERE ci.last_version IS NULL AND ci.verse_id IN (SELECT value FROM json_each(?))", (J,)):
        rec[vid]["narrative"].append(f"{chap} / {head}")
    check("reading claims and the narrative")

    by_ref = {r["reference"]: vid for vid, r in rec.items()}
    by_strong = collections.defaultdict(set)
    by_cluster = collections.defaultdict(set)
    for vid, r in rec.items():                          # open items reach a verse through its surfaces (#2312)
        for w in r["surfaces"]:
            by_strong[w["strong"]].add(vid)
            for cl in w["clusters"]:
                by_cluster[cl].add(vid)
    seen = set()
    for t, it, qv in escalation.match_open_items(Db(cfg), clusters=sorted(by_cluster), strongs=sorted(by_strong),
                                                 verses=sorted(by_ref), home=False):   # worded items: verses only
        targets = {by_ref[qv]} if qv in by_ref else by_strong.get(qv) or by_cluster.get(qv) or set()
        for vid in targets:
            if (vid, it["id"]) in seen:
                continue
            seen.add((vid, it["id"]))
            rec[vid]["open_items"].append({"item": f"{t['alias']}.{it['item_no']}", "kind": it["kind"],
                                           "value": it["value"], "matched_on": qv, "note": it["note"]})
    check("matching open items")

    files: dict[str, list] = collections.defaultdict(list)
    for vid, path, sha, imported, head, line_no, line_kind, found_by, written in conn.execute(
            "SELECT x.verse_id, f.path, f.sha256, f.imported_observations, s.heading, x.line_no, x.line_kind, x.found_by, "
            "x.ref_as_written "
            "FROM reading_ref x JOIN reading_file f ON f.id=x.file_id AND f.removed=0 "
            "JOIN reading_section s ON s.id=x.section_id WHERE x.deleted=0 "
            "AND x.verse_id IN (SELECT value FROM json_each(?)) ORDER BY f.path, x.line_no", (J,)):
        files[path].append((vid, sha, imported, head, line_no, line_kind, found_by, written))
    stale = []
    for path, hits in files.items():
        p = root / path
        data = p.read_bytes() if p.is_file() else b""
        if hashlib.sha256(data).hexdigest() != hits[0][1]:
            stale.append(path)
        lines = data.decode("utf-8", errors="replace").replace("\r\n", "\n").split("\n")
        for vid, _sha, imported, head, line_no, line_kind, found_by, written in hits:
            rec[vid]["file_lines"].append({"file": path, "section": head, "line": line_no, "line_kind": line_kind,
                                           "found_by": found_by, "as_written": written, "imported": bool(imported),
                                           "text": lines[line_no - 1] if 0 < line_no <= len(lines) else None})
        check("extracting file lines")

    lexicon = {}
    for strong, head in conn.execute("SELECT strong, head FROM strong_sense WHERE deleted=0 AND strong IN "
                                     "(SELECT value FROM json_each(?))", (_ids(strongs),)):
        lexicon[strong] = {"sense": head, "meaning": [], "mounce": None, "lsj_chars": None}
    for strong, text in conn.execute("SELECT strong_variant, sense_text FROM strong_meaning_tree WHERE deleted=0 AND "
                                     "strong_variant IN (SELECT value FROM json_each(?)) ORDER BY strong_variant, sort",
                                     (_ids(strongs),)):
        lexicon.setdefault(strong, {"sense": None, "meaning": [], "mounce": None, "lsj_chars": None})["meaning"].append(text)
    for strong, mounce, lsj in conn.execute("SELECT strong, mounce, length(lsj) FROM strong_lexicon WHERE deleted=0 AND "
                                            "strong IN (SELECT value FROM json_each(?))", (_ids(strongs),)):
        lexicon.setdefault(strong, {"sense": None, "meaning": [], "mounce": None, "lsj_chars": None})
        lexicon[strong]["mounce"], lexicon[strong]["lsj_chars"] = mounce, lsj

    counts = collections.Counter()
    for r in rec.values():
        g = r["gaps"]
        read = bool(r["observations"]) or any(h["face"] for h in r["strand_hits"])
        if not read:
            g.append("not read")
        if r["file_lines"] and not r["observations"]:
            g.append("read in files only")
        if any(not h["face"] and not h["reason"] for h in r["strand_hits"]):
            g.append("hit unread")
        if r["observations"] and not any(c["status"] == "current" for c in r["claims"]):
            g.append("observed, no claim")
        if any(c["status"] == "current" and not c["told_in"] for c in r["claims"]):
            g.append("claim not told")
        if r["open_items"]:
            g.append("open item")
        if any(not lexicon.get(w["strong"], {}).get("meaning") or
               (w["strong"].startswith("G") and not lexicon.get(w["strong"], {}).get("mounce")) for w in r["words"]):
            g.append("meaning missing")
        counts.update(g)
    verses = [rec[v] for v in vids]
    return {"scope": {k: scope[k] for k in ("version", "request", "home", "selectors", "not_resolved", "counts")},
            "verses": verses, "lexicon": lexicon,
            "gaps": {k: counts.get(k, 0) for k in GAPS},
            "files_changed_since_indexed": stale,
            "counts": {"verses": len(verses), "with_a_gap": sum(1 for r in verses if r["gaps"]),
                       "observations": sum(len(r["observations"]) for r in verses),
                       "claims": len({c["claim"] for r in verses for c in r["claims"]}),
                       "file_lines": sum(len(r["file_lines"]) for r in verses),
                       "open_items": len({o["item"] for r in verses for o in r["open_items"]}),
                       "seconds": round(time.monotonic() - t0, 1)}}


def markdown(out: dict, label: str) -> list[str]:
    """The readable summary: gap counts, one line per verse, the lexicon list. The JSON is the record."""
    c, g = out["counts"], out["gaps"]
    sel = "; ".join(f"{s['kind']} {s['value']} ({s['verses']})" for s in out["scope"]["selectors"])
    L = [f"# Collation -- {label}", "",
         f"> Generated by `Verse-Collate.ps1` (escalation #2228). Scope: {sel}. The full record per verse is the "
         f"JSON beside this file.", "",
         f"- **Verses:** {c['verses']}, of which {c['with_a_gap']} have a gap.",
         f"- **Known:** {c['observations']} observations, {c['claims']} claims, {c['open_items']} open items, "
         f"{c['file_lines']} lines in the cluster files.", ""]
    if out["files_changed_since_indexed"]:
        L += [f"- **Files changed since they were indexed** (run `Reading-Index.ps1 -Step Build`): "
              f"{', '.join(out['files_changed_since_indexed'])}", ""]
    L += ["## Gaps", "", "| gap | verses |", "|---|---|"] + [f"| {k} | {v} |" for k, v in g.items()]
    L += ["", "## Per verse", "", "| verse | inner-being words | obs | hits faced | claims | blocks | file lines | gaps |",
          "|---|---|---|---|---|---|---|---|"]
    for r in out["verses"]:
        words = ", ".join(sorted({f"{w['surface']} ({w['strong']}, {w['cluster']})" for w in r["words"]}))
        faced = sum(1 for h in r["strand_hits"] if h["face"])
        L.append(f"| {r['reference']} | {words.replace('|', '/')} | {len(r['observations'])} | "
                 f"{faced}/{len(r['strand_hits'])} | {len(r['claims'])} | {len(r['narrative'])} | "
                 f"{len(r['file_lines'])} | {', '.join(r['gaps'])} |")
    L += ["", "## Lexicon", "", "| strong | sense | meaning senses | Mounce | LSJ |", "|---|---|---|---|---|"]
    for s, x in sorted(out["lexicon"].items()):
        L.append(f"| {s} | {(x['sense'] or '').replace('|', '/')} | {len(x['meaning'])} | "
                 f"{'yes' if x['mounce'] else ('--' if s.startswith('H') else 'missing')} | "
                 f"{str(x['lsj_chars']) + ' chars' if x['lsj_chars'] else '--'} |")
    return L
