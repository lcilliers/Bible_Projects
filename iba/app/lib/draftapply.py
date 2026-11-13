"""draftapply.py -- the processing of prepared re-read drafts into the observation record (escalation #2498, design
`outputs/escalation/2498-prior-reread-by-collection-design-v3-20261113.md` section 5; method rules DA-01 to DA-04 on `draft_apply.apply`).

A load file (`outputs/escalation/2498-pilot-load-v1-20261113.json`) holds one row per draft observation, matched to the existing
observation it improves (action enrich), or to none (action add), or left alone (action leave). Per row:
  enrich  the existing observation is changed IN PLACE (its text only: its kind and basis were chosen with the finding and stay) through observationrecord.modify_observation; each node of
          the draft that is already on it takes its role (observationrecord.modify_node); each node it lacks is added, with the
          collection of its surface. Every change is kept with its reason in ib_observation_change.
  add     a new observation (stage prior-reread, status draft) with its nodes.
  leave   nothing.
A node whose collection is None (no collection surface can carry it), or on a verse out of scope (B:130), is not written and is listed. A node already on the observation
for the same occurrence is not written twice, so a second run changes nothing.

apply(keep=False) runs the whole load inside a savepoint and rolls it back: it reports what a real run would do and every problem;
apply(keep=True) does the same and keeps it. A problem anywhere refuses the whole load (nothing is written). Caller commits."""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import sqlite3
import sys

from . import observationrecord as orec
from . import recordingpass
from .cfg import Cfg

Refused = orec.Refused
WHO = "Claude"
ADD_STAGE = "prior-reread"


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _collections(conn) -> dict:
    by_name: dict = {}
    for cid, name in conn.execute("SELECT id, name FROM collection WHERE deleted=0 AND status='confirmed'"):
        by_name.setdefault(name, []).append(cid)
    dup = sorted(n for n, v in by_name.items() if len(v) > 1)
    if dup:
        raise Refused(f"collection names are not unique, so a name cannot place a node: {dup}")
    return {n: v[0] for n, v in by_name.items()}


def _scope(conn) -> set:
    """The verses in scope (B:130): those that hold an occurrence of a member surface of a live collection, read by the shared reader
    (collectionexport._memberships: a surface's own link, else its base), as the node checker reads them."""
    import collections
    from . import collectionexport as cx
    tiers = json.loads(conn.execute("SELECT value FROM cfg_setting WHERE key='collection.member_tiers' AND inactive=0").fetchone()[0])
    terms = {r[0]: tuple(r) for r in conn.execute("SELECT id, surface, origin, surface_group, group_state, base_id FROM surface_term WHERE deleted=0")}
    live = {r[0] for r in conn.execute("SELECT id FROM collection WHERE deleted=0 AND status='confirmed'")}
    surf = set()
    for sid, ms in cx._memberships(conn, terms, tiers, own_link=True).items():
        if any(cid in live and st == "confirmed" for cid, _, st, _ in ms):
            surf.add((terms[sid][1] or "").strip().lower())
    return {o for s, o in conn.execute("SELECT lower(trim(vl.surface)), v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
                                       "WHERE vl.deleted=0") if s in surf}


def _verify_node(conn, n, cols, where, errors):
    vl = conn.execute("SELECT vl.id, vl.surface, vl.strong, vl.morph_code, v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
                      "WHERE vl.id=? AND vl.deleted=0", (n["verse_lexical_id"],)).fetchone()
    if vl is None:
        errors.append(f"{where}: occurrence {n['verse_lexical_id']} is not a live occurrence")
        return None
    if vl["osisId"] != n["verse"] or vl["strong"] != n["strong"]:
        errors.append(f"{where}: occurrence {vl['id']} is {vl['strong']} in {vl['osisId']}, not {n['strong']} in {n['verse']}")
        return None
    if n.get("collection") is not None and n["collection"] not in cols:
        errors.append(f"{where}: {n['collection']!r} is not a live confirmed collection")
        return None
    return vl


def _add_node(conn, oid, stage, vl, n, cols, reason, run_id):
    seq = conn.execute("SELECT COALESCE(MAX(seq),0) FROM ib_node WHERE observation_id=?", (oid,)).fetchone()[0] + 1
    nid = conn.execute(
        "INSERT INTO ib_node (observation_id, strong, verse_reference, surface, morph_code, source_stage, seq, role, reading_id, "
        "created_at, verse_lexical_id, collection_id) VALUES (?,?,?,?,?,?,?,?,NULL,?,?,?)",
        (oid, vl["strong"], vl["osisId"], vl["surface"], vl["morph_code"], stage, seq, n["role"], _now(), vl["id"],
         cols[n["collection"]])).lastrowid
    orec.log(conn, oid, nid, "node", None, f"added: {vl['osisId']} {vl['surface']} ({vl['strong']}) role {n['role']} collection {n['collection']}",
             reason, None, run_id, WHO)
    return nid


def _blocked(n, scope):
    """Why a node cannot be ADDED (an existing node keeps its place and may take its role): its verse is out of scope (B:130), or no
    collection can carry it."""
    if n["verse"] not in scope:
        return "nodes_not_written_out_of_scope"
    if n.get("collection") is None:
        return "nodes_not_written_no_collection"
    return None


def _skip(res, where, n, why):
    res[why].append({"row": where, "verse": n["verse"], "surface": n["surface"], "strong": n["strong"]})


def _run(conn, cfg, load: dict, run_id: str) -> dict:
    cols = _collections(conn)
    scope = _scope(conn)
    docs = load["documents"]
    errors = []
    res = {"enriched": 0, "added": 0, "left": 0, "nodes_added": 0, "roles_set": 0, "text_changed": 0, "nodes_not_written_no_collection": [], "nodes_not_written_out_of_scope": [], "rows": []}
    for r in load["rows"]:
        doc = docs[str(r["document"])]
        where = f"doc {r['document']} draft {r.get('draft')}"
        reason = r.get("reason") or f"re-read of {doc['path']} lines {r.get('doc_lines')} (#2498)"
        if r["action"] == "leave":
            res["left"] += 1
            continue
        nodes = r.get("nodes") or []
        if not nodes:
            errors.append(f"{where}: no nodes")
            continue
        verses = {n["verse"] for n in nodes}
        vtext = " ".join((conn.execute("SELECT text FROM verse WHERE osisId=?", (v,)).fetchone() or [""])[0] or "" for v in verses)
        run = orec.copies_verse(cfg, [r["obs_text"]], vtext)
        if run:
            errors.append(f"{where}: repeats the verse text ({run!r}): more than the permitted number of consecutive verse words")
            continue
        verified = []
        for j, n in enumerate(nodes):
            vl = _verify_node(conn, n, cols, f"{where} nodes[{j}]", errors)
            if vl is None:
                continue
            if not n.get("role"):
                errors.append(f"{where} nodes[{j}]: a role is required")
                continue
            verified.append((n, vl))
        if r["action"] == "enrich":
            oid = r["existing"]
            o = conn.execute("SELECT * FROM ib_observation WHERE id=? AND deleted=0", (oid,)).fetchone()
            if o is None:
                errors.append(f"{where}: existing observation {oid} is not live")
                continue
            sets = {}
            if (o["obs_text"] or "").strip() != r["obs_text"].strip():
                sets["obs_text"] = r["obs_text"]
            try:
                changed = orec.modify_observation(cfg, conn, oid, sets, reason, None, run_id, WHO) if sets else []
            except Refused as exc:
                errors.append(f"{where}: {exc}")
                continue
            res["text_changed"] += "obs_text" in changed
            have = {x["verse_lexical_id"]: dict(x) for x in conn.execute("SELECT * FROM ib_node WHERE observation_id=? AND deleted=0 ORDER BY id DESC", (oid,))}
            added = roles = 0
            for n, vl in verified:
                ex = have.get(vl["id"])
                if ex is None:
                    why = _blocked(n, scope)
                    if why:
                        _skip(res, where, n, why)
                        continue
                    _add_node(conn, oid, o["stage"], vl, n, cols, reason, run_id)
                    added += 1
                elif ex["role"] != n["role"]:
                    try:
                        changed_node = orec.modify_node(cfg, conn, ex["id"], {"role": n["role"]}, n.get("reason") or reason, None, run_id, WHO)
                    except Refused as exc:
                        errors.append(f"{where}: {exc}")
                        continue
                    roles += 1 if changed_node else 0
                    ex["role"] = n["role"]
            res["enriched"] += 1
            res["nodes_added"] += added
            res["roles_set"] += roles
            res["rows"].append({"row": where, "action": "enrich", "observation": oid, "text_changed": "obs_text" in changed,
                                "nodes_added": added, "roles_set": roles})
        else:  # add
            text = r["obs_text"].strip()
            key = f"{doc['reading_file_id']}:L{str(r['doc_lines']).split()[0].split('-')[0]}:reread-{r['draft']}"
            if conn.execute("SELECT 1 FROM ib_observation WHERE stable_key=? AND deleted=0", (key,)).fetchone():
                res["already_present"] = res.get("already_present", 0) + 1       # a second run: this one was added before
                continue
            try:
                recordingpass._validate_obs_text(conn, text)
            except recordingpass.InvalidObservationText as exc:
                errors.append(f"{where}: {exc}")
                continue
            dup = orec.live_text(conn, text)
            if dup:
                errors.append(f"{where}: this description is already live as observation {dup['id']}")
                continue
            if r["kind"] not in orec.kinds(cfg):
                errors.append(f"{where}: kind {r['kind']!r} is not a kind")
                continue
            stage = load.get("stage_for_added", ADD_STAGE)
            first = str(r["doc_lines"]).split()[0].split("-")[0]
            oid = conn.execute(
                "INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, basis, meaning_source, status, stable_key, revisit_note, "
                "run_id, created_at) VALUES (NULL,?,?,?,?,'verse-text','draft',?,?,?,?)",
                (stage, r["kind"], text, r["basis"], key,
                 f"Re-read from {doc['path']} lines {r.get('doc_lines')} (#2498)", run_id, _now())).lastrowid
            orec.log(conn, oid, None, "created", None, text, reason, None, run_id, WHO)
            added = 0
            for n, vl in verified:
                why = _blocked(n, scope)
                if why:
                    _skip(res, where, n, why)
                    continue
                _add_node(conn, oid, stage, vl, n, cols, reason, run_id)
                added += 1
            res["added"] += 1
            res["nodes_added"] += added
            res["rows"].append({"row": where, "action": "add", "observation": oid, "nodes_added": added})
    if errors:
        raise Refused("the load is refused, nothing written; problems:\n  " + "\n  ".join(errors))
    return res


def apply(conn, load: dict, run_id: str, keep: bool) -> dict:
    """keep=False: applied inside a savepoint and rolled back (a check); keep=True: kept. The caller commits."""
    cfg = Cfg.on(conn)
    conn.row_factory = sqlite3.Row
    conn.execute("SAVEPOINT draft_apply")
    try:
        res = _run(conn, cfg, load, run_id)
    except Exception:
        conn.execute("ROLLBACK TO draft_apply")
        conn.execute("RELEASE draft_apply")
        raise
    if not keep:
        conn.execute("ROLLBACK TO draft_apply")
    conn.execute("RELEASE draft_apply")
    res["kept"] = keep
    return res


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Apply or check a re-read load file (#2498). Default is a check: nothing is kept.")
    ap.add_argument("--db", required=True)
    ap.add_argument("--file", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(argv)
    conn = sqlite3.connect(a.db)
    load = json.loads(pathlib.Path(a.file).read_text(encoding="utf-8"))
    run_id = f"DRAFTAPPLY-{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d_%H%M%S')}"
    try:
        res = apply(conn, load, run_id, keep=a.apply)
    except Refused as exc:
        print(exc)
        return 2
    if a.apply:
        conn.commit()
    print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
