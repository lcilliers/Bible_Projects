"""observationrecord.py -- the observation record (escalation #2274; design
`outputs/escalation/2273-2274-reading-phases-and-observation-record-design-v6-20261024.md` sec 1 to 3).

A reading records findings. Each finding is one `ib_observation`, its distinct description: text, meaning,
implication, basis, its kind as tag and, on a party or link finding, its route. Its `ib_node` rows apply it to what it
covers: the verse, the word (strong, surface, morph), the word's own classification (cluster_code, checked against
cluster_strong), the word's role in the finding, the reading that applied it (its home) and, later, where the verse
ends up (disposition). A description already live is never written twice: the finding names it (`existing`) and gains
nodes. Every change to a finding or a node is kept with its reason in `ib_observation_change` (RW-01).

A finding spec (the shape Reading.ps1 -Step Record and -Step Gather read):
    {"key": "f1", "kind": "face|qualification|party|statement|link|use|term|silence",
     "text": "...", "meaning": "...", "implication": "...", "basis": "stated|read", "route": "A|B|C",
     "existing": <observation id, instead of text: the description is already live>,
     "nodes": [{"verse": "Jon 1:10", "strong": "H3372G", "surface": "afraid", "cluster": "M01",
                "role": "characteristic|qualifier|standalone", "question": "M0.5.11"},
               {"strong": "H3372G", "cluster": "M01", "role": "characteristic"},      (a term finding, no verse)
               {"traced": <observation id or a finding key>}]}                        (a finding about a finding)

check() validates a list of specs and returns the plan; write() writes it (the caller holds the write grants and
the transaction). Nothing is written while any spec is wrong.
"""
from __future__ import annotations

import datetime
import json

from . import narrativeregister as nr
from . import recordingpass
from . import strandreading as sr

Refused = nr.Refused
STAGE = "reading"
ROUTE_REQUIRED, ROUTE_ALLOWED = ("party",), ("party", "link")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def kinds(cfg) -> list[str]:
    """The eight kinds of finding (cfg_setting reading.observation_parts), each a live ib_observation.tag value."""
    parts = cfg.required_setting("reading.observation_parts")
    out = list((json.loads(parts) if isinstance(parts, str) else parts)["kinds"])
    missing = set(out) - set(cfg.enum("ib_observation.tag"))
    if missing:
        raise Refused(f"kinds {sorted(missing)} are not ib_observation.tag values")
    return out


def word_clusters(conn, strong: str) -> list[str]:
    return [r[0] for r in conn.execute("SELECT cluster_code FROM cluster_strong WHERE strong=? AND deleted=0 "
                                       "ORDER BY cluster_code", (strong,))]


def live_text(conn, text: str):
    """The live observation holding this exact description, if any."""
    return conn.execute("SELECT id, tag FROM ib_observation WHERE trim(obs_text)=? AND status<>'withdrawn' "
                        "ORDER BY id LIMIT 1", ((text or "").strip(),)).fetchone()


def check(cfg, specs: list[tuple[str, dict]], errors: list, quotes: list) -> list[dict]:
    """[(where, spec)] -> the plan write() takes. Problems go to `errors`, quotations not in the ESV to `quotes`."""
    conn = cfg.conn
    vx = nr.VerseIndex(cfg)
    kinds_ = kinds(cfg)
    bases, routes, roles = cfg.enum("ib_observation.basis"), cfg.enum("observation_route"), cfg.enum("observation_role")
    keys, texts, plan = set(), {}, []
    for where, s in specs:
        if not isinstance(s, dict):
            errors.append(f"{where}: a finding is an object (key, kind, text, basis, nodes)")
            continue
        key = s.get("key")
        if not key or key in keys:
            errors.append(f"{where}: a unique key is required")
        keys.add(key)
        existing = s.get("existing")
        kind = s.get("kind")
        p = {"key": key, "where": where, "existing": None, "nodes": []}
        if existing is not None:
            row = conn.execute("SELECT id, tag, status FROM ib_observation WHERE id=?", (existing,)).fetchone()
            if row is None or row["status"] == "withdrawn":
                errors.append(f"{where}: existing {existing} is not a live observation")
                continue
            if any(s.get(k) for k in ("text", "meaning", "implication", "basis", "route")):
                errors.append(f"{where}: an existing finding takes nodes only (a changed description is a new finding, "
                              f"and the old one withdrawn with its reason)")
            p["existing"], kind = row["id"], row["tag"]
        else:
            if kind not in kinds_:
                errors.append(f"{where}: kind must be one of {kinds_}")
            text = (s.get("text") or "").strip()
            if not text:
                errors.append(f"{where}: text is required")
            else:
                try:
                    recordingpass._validate_obs_text(conn, text)
                except recordingpass.InvalidObservationText as exc:
                    errors.append(f"{where}: {exc}")
                dup = live_text(conn, text)
                if dup:
                    errors.append(f"{where}: this description is already live as observation {dup['id']} -- name it "
                                  f"as existing and give the nodes (one finding, many nodes)")
                if text in texts:
                    errors.append(f"{where}: the same text as {texts[text]} -- one finding, many nodes")
                texts[text] = where
            if s.get("basis") not in bases:
                errors.append(f"{where}: basis must be one of {bases}")
            route = s.get("route")
            if kind in ROUTE_REQUIRED and route not in routes:
                errors.append(f"{where}: a {kind} finding carries its route, one of {routes}")
            elif route is not None and (kind not in ROUTE_ALLOWED or route not in routes):
                errors.append(f"{where}: route ({routes}) is held only on a party or link finding")
            quotes += sr._quote_check(conn, cfg, [s.get(k) for k in ("text", "meaning", "implication")], where)
            p.update({"kind": kind, "text": text, "meaning": s.get("meaning"), "implication": s.get("implication"),
                      "basis": s.get("basis"), "route": route})
        nodes = s.get("nodes") or []
        if not nodes:
            errors.append(f"{where}: at least one node (what the finding applies to)")
        for j, n in enumerate(nodes):
            at = f"{where} nodes[{j}]"
            if not isinstance(n, dict):
                errors.append(f"{at}: a node is an object")
                continue
            if n.get("traced") is not None and not n.get("strong"):
                p["nodes"].append({"traced": n["traced"], "at": at})
                continue
            strong = n.get("strong")
            if not strong:
                errors.append(f"{at}: a node names the word (strong), or the finding it is about (traced)")
                continue
            clusters = word_clusters(conn, strong)
            cluster = n.get("cluster") or (clusters[0] if len(clusters) == 1 else None)
            if not clusters:
                errors.append(f"{at}: {strong} has no cluster (an untagged word): a node is a classification, so carry "
                              f"the word in the finding's text")
                continue
            if cluster not in clusters:
                errors.append(f"{at}: cluster must be one of {strong}'s own clusters {clusters}")
                continue
            if n.get("role") not in roles:
                errors.append(f"{at}: role must be one of {roles} (the word's role in this finding)")
            occ = {"verse_reference": None, "surface": n.get("surface"), "morph_code": None}
            if n.get("verse"):
                try:
                    vr = sr._verse(conn, vx, n["verse"])
                    occ = recordingpass.resolve_occurrence(conn, strong, vr["osisId"], n.get("surface"), None)
                except (Refused, recordingpass.UnresolvedOccurrence) as exc:
                    errors.append(f"{at}: {exc}")
                    continue
            elif kind != "term":
                errors.append(f"{at}: only a term finding applies to a word with no verse")
            p["nodes"].append({"strong": strong, "cluster": cluster, "role": n.get("role"),
                               "question": n.get("question"), "traced": n.get("traced"), "at": at,
                               **{k: occ[k] for k in ("verse_reference", "surface", "morph_code")}})
        if kind == "qualification":
            got = {n.get("role") for n in p["nodes"]}
            if not {"qualifier", "characteristic"} <= got:
                errors.append(f"{where}: a qualification finding applies to its qualifier (role qualifier) and the "
                              f"characteristic it binds to (role characteristic)")
        plan.append(p)
    for p in plan:
        for n in p["nodes"]:
            t = n.get("traced")
            if t is None or t in keys:
                continue
            if not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'", (t,)).fetchone():
                errors.append(f"{n['at']}: traced {t!r} is neither a live observation nor a finding key in this file")
    return plan


def write(conn, plan: list[dict], reading_id: int | None, run_id: str) -> dict:
    """Write a checked plan. Returns {key: {"observation": id, "nodes": [ids], "new": bool}}. Caller commits."""
    out, now = {}, _now()
    for p in plan:
        if p["existing"] is not None:
            oid, new = p["existing"], False
        else:
            oid = conn.execute(
                "INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, meaning, implication, basis, route, "
                "meaning_source, status, run_id, created_at) VALUES (NULL,?,?,?,?,?,?,?,'verse-text','draft',?,?)",
                (STAGE, p["kind"], p["text"], p.get("meaning"), p.get("implication"), p["basis"], p.get("route"),
                 run_id, now)).lastrowid
            new = True
        out[p["key"]] = {"observation": oid, "nodes": [], "new": new}
    for p in plan:
        oid = out[p["key"]]["observation"]
        seq = conn.execute("SELECT COALESCE(MAX(seq), 0) FROM ib_node WHERE observation_id=?", (oid,)).fetchone()[0]
        for n in p["nodes"]:
            traced = n.get("traced")
            traced = out[traced]["observation"] if traced in out else traced
            if n.get("strong") and conn.execute(
                    "SELECT 1 FROM ib_node WHERE observation_id=? AND strong=? AND verse_reference IS ? AND "
                    "reading_id IS ? AND role IS ?",
                    (oid, n["strong"], n["verse_reference"], reading_id, n["role"])).fetchone():
                continue                                  # the same application, already written
            seq += 1
            cluster = n.get("cluster") or conn.execute(
                "SELECT cluster_code FROM ib_node WHERE observation_id=? AND cluster_code IS NOT NULL LIMIT 1",
                (traced,)).fetchone()[0]
            nid = conn.execute(
                "INSERT INTO ib_node (observation_id, cluster_code, strong, verse_reference, surface, morph_code, "
                "question_code, traced_observation_id, source_stage, seq, role, reading_id, created_at) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (oid, cluster, n.get("strong"), n.get("verse_reference"), n.get("surface"), n.get("morph_code"),
                 n.get("question"), traced, STAGE, seq, n.get("role"), reading_id, now)).lastrowid
            out[p["key"]]["nodes"].append(nid)
    return out


# ══ changes, kept with their reasons (RW-01) ═════════════════════════════════════════════════════
def log(conn, observation_id: int, node_id: int | None, column: str, old, new, reason: str, reading_id, run_id: str,
        who: str) -> None:
    if len((reason or "").strip()) < 10:
        raise Refused(f"a change to observation {observation_id} needs its reason, in words (10 characters or more)")
    conn.execute("INSERT INTO ib_observation_change (observation_id, node_id, column_name, old_value, new_value, "
                 "reason, reading_id, run_id, created_by) VALUES (?,?,?,?,?,?,?,?,?)",
                 (observation_id, node_id, column, None if old is None else str(old),
                  None if new is None else str(new), reason.strip(), reading_id, run_id, who))


def set_disposition(conn, node_id: int, disposition: str, note: str, reading_id, run_id: str, who: str) -> None:
    """Where this verse ends up for the finding (cfg_enum observation_disposition), the change kept."""
    n = conn.execute("SELECT observation_id, disposition, disposition_note FROM ib_node WHERE id=?",
                     (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} does not exist")
    if (n["disposition"], n["disposition_note"]) == (disposition, note):
        return
    log(conn, n["observation_id"], node_id, "disposition", n["disposition"], disposition, note, reading_id, run_id, who)
    conn.execute("UPDATE ib_node SET disposition=?, disposition_note=? WHERE id=?", (disposition, note, node_id))


def withdraw_observation(conn, observation_id: int, reason: str, reading_id, run_id: str, who: str) -> None:
    """The finding is wrong everywhere: its status withdrawn, the change kept (nothing overwritten)."""
    o = conn.execute("SELECT status FROM ib_observation WHERE id=?", (observation_id,)).fetchone()
    if o is None or o["status"] == "withdrawn":
        raise Refused(f"observation {observation_id} is not a live observation")
    log(conn, observation_id, None, "status", o["status"], "withdrawn", reason, reading_id, run_id, who)
    conn.execute("UPDATE ib_observation SET status='withdrawn', updated_at=? WHERE id=?", (_now(), observation_id))
