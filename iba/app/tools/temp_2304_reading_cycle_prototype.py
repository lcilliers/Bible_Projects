"""temp_2304_reading_cycle_prototype.py -- the prototype of escalation #2304 (design
outputs/escalation/2304-reading-cycle-one-json-design-v3-20261026.md): one JSON per scope run, built by 0.C (open),
0.GAP pre (gather) and observe, then written by record. Runs only on a copy of iba.db made with lib/dbsnapshot.copy_db;
every file goes to the scratch directory, in a folder named as the home cluster's folder would be. Not wired into
Reading.ps1: the prototype is for the researcher to confirm before the build.

Usage:
    python iba/app/tools/temp_2304_reading_cycle_prototype.py <scratch dir> build <subgroup> [--surface a,b] [--verse "..."]
    python iba/app/tools/temp_2304_reading_cycle_prototype.py <scratch dir> record <filled observe JSON>
"""
import datetime
import json
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import escalation  # noqa: E402
from iba.app.lib import observationrecord as orec  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402
from iba.app.lib import surfacemap  # noqa: E402
from iba.app.lib import versecollate as vc  # noqa: E402
from iba.app.lib import versescope as vs  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2304"
DB = S / "iba.db"
RESPONSES = ("closed", "touched", "forward", "withdrawn", "superseded")


class Refused(ValueError):
    pass


def _now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cluster_folder(conn, code: str) -> str:
    """The home cluster's folder name (cfg_setting report.cluster_folder_naming_convention)."""
    name = conn.execute("SELECT short_name FROM cluster WHERE cluster_code=?", (code,)).fetchone()[0]
    return f"{code} - " + "-".join(re.sub(r"[^a-z0-9 ]", "", name.lower()).split())


# ── a) 0.C: the scope ────────────────────────────────────────────────────────────────────────────────────────────────
def open_(cfg, label, eid, objective, subgroup, surfaces=None, verses=None) -> dict:
    conn = cfg.conn
    row = conn.execute("SELECT id, cluster_code, kind FROM cluster_subgroup WHERE subgroup_code=? AND "
                       "coalesce(delete_flagged,0)=0", (subgroup,)).fetchone()
    if row is None:
        raise Refused(f"{subgroup!r} is not a live subgroup")
    if (row[2] or "group") != "group":
        raise Refused(f"{subgroup} is a {row[2]} group: only a group subgroup is a home (rule 120)")
    gate = surfacemap.reading_refusal(conn, row[1])
    if gate:
        raise Refused(gate)
    request = {"subgroup": [subgroup], "home": [subgroup]}
    out = vs.resolve(cfg, request)
    segment = None
    if surfaces or verses:                                       # D1: a subset of the subgroup
        keep_s = {surfacemap.norm(x) for x in surfaces or []}
        keep_v = None
        if verses:
            r = vs.Resolver(cfg)
            r.verse(verses)
            keep_v = set(r.routes)
        for v in out["verses"]:
            for o in v["occurrences"]:
                if o["home"] and ((keep_s and surfacemap.norm(o["surface"]) not in keep_s) or
                                  (keep_v is not None and v["verse_id"] not in keep_v)):
                    o["home"] = o["in_scope"] = False
        out["verses"] = [v for v in out["verses"] if any(o["home"] for o in v["occurrences"])]
        segment = {"surfaces": sorted(keep_s) or None, "verses": verses or None}
    if not out["verses"]:
        raise Refused("the scope holds no verse")
    occ = [o for v in out["verses"] for o in v["occurrences"]]
    out["segment"] = segment
    out["counts"].update({"verses": len(out["verses"]), "home": sum(o["home"] for o in occ),
                          "in_scope": sum(o["in_scope"] for o in occ)})
    rid = conn.execute("INSERT INTO reading (label, escalation_id, home_cluster, request, state, objective, run_id, "
                       "created_at, created_by) VALUES (?,?,?,?,'open',?,?,?,'Claude')",
                       (label, eid, row[1], json.dumps(request), objective, "PROTO-2304", _now())).lastrowid
    for v in out["verses"]:
        conn.execute("INSERT INTO reading_verse (reading_id, verse_id, routes, created_at, created_by) VALUES "
                     "(?,?,?,?,'Claude')", (rid, v["verse_id"], json.dumps(v["routes"]), _now()))
    conn.commit()
    return {"label": label, "reading_id": rid, "escalation": eid, "objective": objective, "home_cluster": row[1],
            "subgroup": subgroup, "opened_at": _now(), "scope": out}


# ── b) 0.GAP pre: the gathering (reads only) ─────────────────────────────────────────────────────────────────────────
def gather(cfg, data: dict) -> dict:
    conn = cfg.conn
    sc = data["scope"]
    vids = [v["verse_id"] for v in sc["verses"]]
    col = vc.collate(cfg, {"subgroup": [data["subgroup"]], "home": [data["subgroup"]]}, ROOT)
    colv = {r["verse_id"]: r for r in col["verses"]}
    lex = {}
    for r in conn.execute("SELECT l.id, l.verse_id, l.morph_code, l.role, l.is_negator, l.party_kind, l.narrative_morph, "
                          "l.gloss_consistent_in_verse, s.stepGloss FROM verse_lexical l LEFT JOIN strong s ON "
                          "s.strongNumber=l.strong WHERE l.deleted=0 AND l.verse_id IN (SELECT value FROM json_each(?))",
                          (json.dumps(vids),)):
        lex.setdefault(r[1], {})[str(r[0])] = {"morph": r[2], "role": r[3], "is_negator": r[4], "party_kind": r[5],
                                               "narrative_morph": r[6], "gloss_consistent": r[7], "gloss": r[8]}
    out, home_occ = {}, {}
    for v in sc["verses"]:
        vid, osis = v["verse_id"], v["osis"]
        place = {n[0]: (n[3], n[4]) for n in vs.node_occurrences(conn, "n.verse_reference=?", (osis,))}
        obs, unplaced = [], []
        for f in rd._findings_on(conn, osis):
            for n in f["nodes"]:
                occ_id, cand = place.get(n["node"], (None, []))
                n["occurrence"] = occ_id
                if occ_id is None and len(cand) > 1:
                    unplaced.append({"node": n["node"], "observation": f["observation"], "candidates": cand})
            obs.append(f)
        docs = []
        for fl in colv[vid]["file_lines"]:
            name = pathlib.PurePosixPath(fl["file"]).name
            imp = [r[0] for r in conn.execute(
                "SELECT DISTINCT o.id FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE "
                "o.status<>'withdrawn' AND o.revisit_note LIKE ? AND n.verse_reference=?", (f"%{name}%", osis))]
            docs.append({"doc": f"{fl['file']}:{fl['line']}", "section": fl["section"], "line_kind": fl["line_kind"],
                         "text": fl["text"], "imported_as": imp})
        for o in v["occurrences"]:
            if o["home"]:
                home_occ[o["id"]] = [f["observation"] for f in obs if any(n["occurrence"] == o["id"]
                                                                          for n in f["nodes"])]
        out[str(vid)] = {"reference": v["reference"], "text": colv[vid]["text"], "passage": rd._passage(conn, osis),
                         "lexical": lex.get(vid, {}), "observations": obs, "unplaced_nodes": unplaced,
                         "documents": docs, "open_items": colv[vid]["open_items"],
                         "meaning_missing": "meaning missing" in colv[vid]["gaps"]}
    # the open items related to the scope, once (D3): matched on the home cluster, the subgroup's codes or a verse
    codes = sorted({o["strong"] for v in sc["verses"] for o in v["occurrences"] if o["home"]})
    refs = {v["reference"]: v["verse_id"] for v in sc["verses"]}
    items, seen = [], set()
    for t, it, qv in escalation.match_open_items(Db(cfg), clusters=[data["home_cluster"]], strongs=codes,
                                                 verses=sorted(refs), home=True):
        ref = f"{t['alias']}.{it['item_no']}"
        if ref in seen:
            continue
        seen.add(ref)
        target = {r[0] for r in conn.execute("SELECT verse_id FROM escalation_thread_item_verse WHERE item_id=? AND "
                                             "deleted=0", (it["id"],))}
        reach = "whole" if target and target <= set(vids) else "in part"
        items.append({"item": ref, "kind": it["kind"], "value": it["value"], "matched_on": qv,
                      "read_for": it["read_for"], "why": it["why"], "comes_back_when": it["comes_back_when"],
                      "target_verses": len(target) or None, "reach": reach})
    data["gathered"] = {"gathered_at": _now(), "verses": out, "existing_on_home_occurrences": {
        str(k): v for k, v in home_occ.items()}, "open_items": items,
        "files_changed_since_indexed": col["files_changed_since_indexed"],
        "counts": {"verses": len(out), "observations": len({f["observation"] for x in out.values()
                                                             for f in x["observations"]}),
                   "home_occurrences_with_existing": sum(1 for v in home_occ.values() if v),
                   "unplaced_nodes": sum(len(x["unplaced_nodes"]) for x in out.values()),
                   "document_lines": len({d["doc"] for x in out.values() for d in x["documents"]}),
                   "document_lines_imported": len({d["doc"] for x in out.values() for d in x["documents"]
                                                   if d["imported_as"]}),
                   "open_items": len(items)}}
    return data


# ── c) observe: the slots ────────────────────────────────────────────────────────────────────────────────────────────
def observe(cfg, data: dict) -> dict:
    conn = cfg.conn
    g = data["gathered"]
    slots = []
    for v in data["scope"]["verses"]:
        gv = g["verses"][str(v["verse_id"])]
        docs = [d["doc"] for d in gv["documents"]]
        for o in v["occurrences"]:
            if o["home"]:
                slots.append({"slot": f"occ:{o['id']}", "verse": v["reference"], "word": f"{o['surface']} ({o['strong']})",
                              "existing": g["existing_on_home_occurrences"].get(str(o["id"]), []),
                              "documents": docs, "fill": None})
        pos = {(o["strong"], o["position"]): o["id"] for o in v["context"] + v["occurrences"]}
        for w in rd._focus(cfg, conn, v["verse_id"]):
            if any(c.startswith("M") for c in w["clusters"]):
                continue                                         # an M word: its own subgroup's home, not a slot here
            oid = pos.get((w["strong"], w["position"]))
            slots.append({"slot": f"qual:{oid}", "verse": v["reference"], "word": w["word"],
                          "in_focus_as": w["in_focus_as"], "fill": None})
    seen = set()
    for x in g["verses"].values():
        for d in x["documents"]:
            if d["doc"] not in seen:
                seen.add(d["doc"])
                slots.append({"slot": f"doc:{d['doc']}", "verse": x["reference"], "text": d["text"],
                              "imported_as": d["imported_as"], "fill": None})
    for it in g["open_items"]:
        slots.append({"slot": f"item:{it['item']}", "read_for": it["read_for"], "reach": it["reach"], "fill": None})
    data["observe"] = {
        "built_at": _now(),
        "how": "Fill every slot. A word slot (occ:, qual:) is covered by a finding whose nodes name its occurrence, or "
               "filled {\"use\": <observation id>}, {\"reason\": ...} or {\"item\": \"OT-nn.n\"}. A document slot (doc:) "
               "is filled {\"adopted_as\": <finding key>}, {\"use\": <observation id>} (already imported) or "
               "{\"reason\": ...}: the documents have precedence. An open item slot (item:) is filled {\"response\": "
               "closed|touched|forward|withdrawn|superseded, \"text\": what the reading found}. Findings go in "
               "`findings` in the B2 shape (key, kind, text, meaning, implication, basis, route; nodes [{occurrence, "
               "role}]); an adopted one carries `source` <file>:<line>.",
        "kinds": orec.kinds(cfg), "slots": slots, "findings": [],
        "counts": {k: sum(1 for s in slots if s["slot"].startswith(k + ":")) for k in ("occ", "qual", "doc", "item")}}
    return data


# ── record: the tables written, all or nothing ───────────────────────────────────────────────────────────────────────
def record(cfg, data: dict) -> dict:
    conn = cfg.conn
    errors = []
    rid = data["reading_id"]
    occ = {}
    for v in data["scope"]["verses"]:
        for o in v["occurrences"] + v["context"]:
            occ[o["id"]] = (v["reference"], o)
    findings = data["observe"]["findings"]
    covered, keys = {}, {f.get("key") for f in findings}
    specs = []
    for i, f in enumerate(findings):
        nodes = []
        for n in f.get("nodes") or []:
            if n.get("occurrence") not in occ:
                errors.append(f"findings[{i}]: occurrence {n.get('occurrence')} is not in the scope's verses")
                continue
            ref, o = occ[n["occurrence"]]
            nodes.append({"verse": ref, "strong": o["strong"], "surface": o["surface"], "role": n.get("role"),
                          "cluster": o.get("cluster") or (o.get("clusters") or [None])[0]})
            covered.setdefault(n["occurrence"], []).append(f.get("key"))
        specs.append((f"findings[{i}] ({f.get('key')})", {**{k: f.get(k) for k in ("key", "kind", "text", "meaning",
                                                                                    "implication", "basis", "route")},
                                                          "nodes": nodes}))
    uses = []
    for s in data["observe"]["slots"]:
        fill, sid = s.get("fill"), s["slot"]
        kind, _, ref = sid.partition(":")
        if kind in ("occ", "qual") and int(ref) in covered:
            continue
        if not isinstance(fill, dict) or len(fill) == 0:
            errors.append(f"{sid}: not filled")
            continue
        if fill.get("reason") is not None:
            if len(str(fill["reason"]).strip()) < 10:
                errors.append(f"{sid}: a reason says why, in words")
        elif fill.get("use") is not None:
            if not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'", (fill["use"],)).fetchone():
                errors.append(f"{sid}: use {fill['use']} is not a live observation")
            elif kind in ("occ", "qual"):
                ref_, o = occ[int(ref)]
                uses.append((fill["use"], {"verse": ref_, "strong": o["strong"], "surface": o["surface"],
                                           "role": fill.get("role", "characteristic"),
                                           "cluster": o.get("cluster") or (o.get("clusters") or [None])[0]}, int(ref)))
        elif fill.get("adopted_as") is not None:
            if kind != "doc" or fill["adopted_as"] not in keys:
                errors.append(f"{sid}: adopted_as names a finding key of this file, on a document slot")
        elif fill.get("item") is not None:
            if not rd._item_exists(conn, fill["item"]):
                errors.append(f"{sid}: item {fill['item']} does not exist")
        elif fill.get("response") is not None:
            if kind != "item" or fill["response"] not in RESPONSES or len(str(fill.get("text") or "")) < 10:
                errors.append(f"{sid}: a response is one of {RESPONSES}, with what the reading found")
        else:
            errors.append(f"{sid}: fill is one of use, reason, item, adopted_as or response")
    for oid, node, occ_id in uses:
        specs.append((f"use {oid} on {occ_id}", {"key": f"use-{oid}-{occ_id}", "existing": oid, "nodes": [node]}))
    quotes = []
    plan = orec.check(cfg, specs, errors, quotes)
    if errors or quotes:
        raise Refused("\n  ".join(["nothing written:"] + errors + quotes))
    written = orec.write(conn, plan, rid, "PROTO-2304")
    # the occurrence on each new node (D5) and the source of an adopted finding (D7)
    for i, f in enumerate(findings):
        w = written[f["key"]]
        for nid, n in zip(w["nodes"], f["nodes"]):
            conn.execute("UPDATE ib_node SET verse_lexical_id=? WHERE id=?", (n["occurrence"], nid))
        if f.get("source"):
            conn.execute("UPDATE ib_observation SET meaning_source=? WHERE id=?", (f["source"], w["observation"]))
    for oid, node, occ_id in uses:
        for nid in written[f"use-{oid}-{occ_id}"]["nodes"]:
            conn.execute("UPDATE ib_node SET verse_lexical_id=? WHERE id=?", (occ_id, nid))
    for s in data["observe"]["slots"]:
        if s["slot"].startswith("item:") and (s.get("fill") or {}).get("response"):
            t, row = rd._thread_item(conn, s["slot"][5:])
            escalation.update(cfg, Db(cfg), t["id"], item_refs=[str(row["item_no"])], response_kind=s["fill"]["response"],
                              respond=f"{s['fill']['text']} (reading {data['label']}, observe)", via=data["escalation"],
                              originator="Claude")
    conn.execute("UPDATE reading SET state='observed', observed_at=? WHERE id=?", (_now(), rid))
    conn.commit()
    return written


def main():
    cmd = sys.argv[2]
    if cmd == "build":
        if DB.exists():
            raise SystemExit(f"{DB} exists: start from a fresh scratch folder")
        copy_db(DB)
        cfg = Cfg(DB)
        args = sys.argv[4:]
        surf = args[args.index("--surface") + 1].split(",") if "--surface" in args else None
        vers = args[args.index("--verse") + 1] if "--verse" in args else None
        sg = sys.argv[3]
        data = open_(cfg, f"proto-{sg.lower().replace('_', '-')}", 2304, "Prototype of the reading cycle (#2304) on "
                     f"{sg}: what the verses say about thirst as a longing of the inner being", sg, surf, vers)
        folder = S / cluster_folder(cfg.conn, data["home_cluster"])
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{data['label']}-v1-20261026.json"
        step = {}
        for name, fn in (("a-scope", None), ("b-gathered", gather), ("c-observe", observe)):
            if fn:
                data = fn(cfg, data)
            snap = folder / f"{data['label']}-after-{name}.json"           # the file as each step leaves it, to show
            snap.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
            step[name] = snap.stat().st_size
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(json.dumps({"file": str(path), "bytes_after_each_step": step, "scope": data["scope"]["counts"],
                          "gathered": data["gathered"]["counts"], "observe": data["observe"]["counts"]}, indent=1))
    elif cmd == "record":
        cfg = Cfg(DB)
        data = json.loads(pathlib.Path(sys.argv[3]).read_text(encoding="utf-8"))
        try:
            print(json.dumps(record(cfg, data), indent=1))
        except Refused as exc:
            print(f"REFUSED: {exc}")


if __name__ == "__main__":
    main()
