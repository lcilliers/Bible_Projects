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
STAGE = "Analysis_phase_1"
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


def node_role_groups(cfg) -> dict:
    """The roles a new node may take, by the evaluation result of its surface (cfg_setting reading.node_roles, #2320):
    {"relevant": [...], "bears_on": [...]}."""
    v = cfg.required_setting("reading.node_roles")
    return json.loads(v) if isinstance(v, str) else v


def node_roles(cfg) -> list[str]:
    return [r for roles in node_role_groups(cfg).values() for r in roles]


def loop_setting(cfg) -> dict:
    v = cfg.required_setting("reading.verse_loop")
    return json.loads(v) if isinstance(v, str) else v


def _parts_setting(cfg) -> dict:
    v = cfg.required_setting("reading.observation_parts")
    return json.loads(v) if isinstance(v, str) else v


def subgroup_code(conn, cluster: str | None, strong: str, surface: str | None) -> str | None:
    """The subgroup of a word as written: its (code, surface) pair in surface_subgroup (the cluster's, when given);
    None when the pair is in no subgroup or in more than one."""
    sql = ("SELECT DISTINCT g.subgroup_code FROM surface_subgroup s JOIN cluster_subgroup g ON g.id=s.cluster_subgroup_id "
           "WHERE s.deleted=0 AND s.strong=? AND s.surface=?")
    args = [strong, (surface or "").strip().lower()]
    if cluster:
        sql += " AND s.cluster_code=?"
        args.append(cluster)
    rows = [r[0] for r in conn.execute(sql, args)]
    return rows[0] if len(rows) == 1 else None


def check_parts(cfg, parts, where: str, errors: list) -> None:
    """The structured parts of a finding (ib_observation.parts, spec 4.2)."""
    if parts is None:
        return
    spec, loop = _parts_setting(cfg), loop_setting(cfg)
    if not isinstance(parts, dict):
        errors.append(f"{where}: parts is an object with keys from {spec['parts']}")
        return
    bad = sorted(set(parts) - set(spec["parts"]))
    if bad:
        errors.append(f"{where}: parts {bad} are not among {spec['parts']}")
    pol = parts.get("polarity")
    if pol is not None and pol not in loop["polarity"]:
        errors.append(f"{where}: polarity must be one of {loop['polarity']}")
    flags = parts.get("flags")
    if flags is not None:
        if not isinstance(flags, list):
            errors.append(f"{where}: flags is a list of {{type, text}}")
        else:
            for k, f in enumerate(flags):
                if (not isinstance(f, dict) or f.get("type") not in spec["flag_types"]
                        or len((f.get("text") or "").strip()) < loop["min_reason_chars"]):
                    errors.append(f"{where}: flags[{k}] is {{type: one of {spec['flag_types']}, text}} in words")


def live_text(conn, text: str):
    """The live observation holding this exact description, if any."""
    return conn.execute("SELECT id, tag FROM ib_observation WHERE trim(obs_text)=? AND deleted=0 "
                        "ORDER BY id LIMIT 1", ((text or "").strip(),)).fetchone()


def check(cfg, specs: list[tuple[str, dict]], errors: list, quotes: list) -> list[dict]:
    """[(where, spec)] -> the plan write() takes. Problems go to `errors`, quotations not in the ESV to `quotes`."""
    conn = cfg.conn
    vx = nr.VerseIndex(cfg)
    kinds_ = kinds(cfg)
    bases, routes, roles = cfg.enum("ib_observation.basis"), cfg.enum("observation_route"), node_roles(cfg)
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
            row = conn.execute("SELECT id, tag, deleted FROM ib_observation WHERE id=?", (existing,)).fetchone()
            if row is None or row["deleted"]:
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
            check_parts(cfg, s.get("parts"), where, errors)
            p.update({"kind": kind, "text": text, "meaning": s.get("meaning"), "implication": s.get("implication"),
                      "basis": s.get("basis"), "route": route, "parts": s.get("parts")})
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
            if clusters:
                if cluster is None:
                    errors.append(f"{at}: {strong} is in several clusters {clusters}: name the cluster")
                    continue
                if cluster not in clusters:
                    errors.append(f"{at}: cluster must be one of {strong}'s own clusters {clusters}")
                    continue
            else:          # no cluster of its own: the node's classification is the T-code found relevant (cfg_column use)
                cluster = n.get("cluster")
                if not cluster or not str(cluster).startswith("T") or not conn.execute(
                        "SELECT 1 FROM cluster WHERE cluster_code=? AND coalesce(deleted,0)=0", (cluster,)).fetchone():
                    errors.append(f"{at}: {strong} has no cluster of its own: name the T-code it is classified under "
                                  f"(the T-code found relevant) as `cluster`")
                    continue
            if n.get("role") not in roles:
                errors.append(f"{at}: role must be one of {roles} (the word's role in this finding)")
            occ = {"verse_reference": None, "surface": n.get("surface"), "morph_code": None, "verse_lexical_id": None}
            if n.get("occurrence") is not None:        # the occurrence itself (#2320): a word as written, with its Strong
                row = conn.execute("SELECT vl.id, vl.strong, vl.surface, vl.morph_code, v.osisId FROM verse_lexical vl "
                                   "JOIN verse v ON v.id=vl.verse_id WHERE vl.id=? AND vl.deleted=0",
                                   (n["occurrence"],)).fetchone()
                if row is None or row["strong"] != strong:
                    errors.append(f"{at}: occurrence {n['occurrence']} is not a live occurrence of {strong}")
                    continue
                occ = {"verse_reference": row["osisId"], "surface": row["surface"], "morph_code": row["morph_code"],
                       "verse_lexical_id": row["id"]}
            elif n.get("verse"):
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
                               **{k: occ[k] for k in ("verse_reference", "surface", "morph_code", "verse_lexical_id")}})
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
            if not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND deleted=0", (t,)).fetchone():
                errors.append(f"{n['at']}: traced {t!r} is neither a live observation nor a finding key in this file")
    return plan


def write(conn, plan: list[dict], reading_id: int | None, run_id: str) -> dict:
    """Write a checked plan. Returns {key: {"observation": id, "nodes": [ids], "new": bool}}. Caller commits."""
    out, now = {}, _now()
    for p in plan:
        if p["existing"] is not None:
            oid, new = p["existing"], False
        else:
            parts = p.get("parts")
            oid = conn.execute(
                "INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, meaning, implication, basis, route, "
                "parts, meaning_source, status, run_id, created_at) VALUES (NULL,?,?,?,?,?,?,?,?,'verse-text','draft',?,?)",
                (STAGE, p["kind"], p["text"], p.get("meaning"), p.get("implication"), p["basis"], p.get("route"),
                 json.dumps(parts, ensure_ascii=False) if parts else None, run_id, now)).lastrowid
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
                    "reading_id IS ? AND role IS ? AND verse_lexical_id IS ?",
                    (oid, n["strong"], n["verse_reference"], reading_id, n["role"], n.get("verse_lexical_id"))).fetchone():
                continue                                  # the same application, already written
            seq += 1
            cluster = n.get("cluster")
            if cluster is None and traced is not None:
                row = conn.execute("SELECT cluster_code FROM ib_node WHERE observation_id=? AND cluster_code IS NOT NULL "
                                   "LIMIT 1", (traced,)).fetchone()
                cluster = row[0] if row else None
            if cluster is None:
                raise Refused(f"a node of finding {p['key']} has no cluster (ib_node.cluster_code is required)")
            sg = subgroup_code(conn, cluster, n["strong"], n.get("surface")) if n.get("strong") else None
            nid = conn.execute(
                "INSERT INTO ib_node (observation_id, cluster_code, cluster_subgroup_code, strong, verse_reference, surface, "
                "morph_code, question_code, traced_observation_id, source_stage, seq, role, reading_id, created_at, "
                "verse_lexical_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (oid, cluster, sg, n.get("strong"), n.get("verse_reference"), n.get("surface"), n.get("morph_code"),
                 n.get("question"), traced, STAGE, seq, n.get("role"), reading_id, now,
                 n.get("verse_lexical_id"))).lastrowid
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
    """Where this verse ends up for the finding (cfg_enum observation_disposition; the claims step's ending of a node), the
    change kept. A disposition of withdrawn also deletes the node (the deleted column, #2323). A reading deletes a node with
    delete_node, which leaves the disposition alone."""
    n = conn.execute("SELECT observation_id, disposition, disposition_note, deleted FROM ib_node WHERE id=?",
                     (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} does not exist")
    if (n["disposition"], n["disposition_note"]) == (disposition, note):
        return
    log(conn, n["observation_id"], node_id, "disposition", n["disposition"], disposition, note, reading_id, run_id, who)
    conn.execute("UPDATE ib_node SET disposition=?, disposition_note=? WHERE id=?", (disposition, note, node_id))
    if disposition == "withdrawn" and not n["deleted"]:
        log(conn, n["observation_id"], node_id, "deleted", 0, 1, note, reading_id, run_id, who)
        conn.execute("UPDATE ib_node SET deleted=1 WHERE id=?", (node_id,))


def delete_node(conn, node_id: int, reason: str, reading_id, run_id: str, who: str) -> bool:
    """A reading deletes a node (#2323): the deleted column, the change kept with its reason. Its disposition is not touched.
    Returns False when it was already deleted."""
    n = conn.execute("SELECT observation_id, deleted FROM ib_node WHERE id=?", (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} does not exist")
    if n["deleted"]:
        return False
    log(conn, n["observation_id"], node_id, "deleted", 0, 1, reason, reading_id, run_id, who)
    conn.execute("UPDATE ib_node SET deleted=1 WHERE id=?", (node_id,))
    return True


def soft_delete_observation(conn, observation_id: int, reason: str, reading_id, run_id: str, who: str) -> None:
    """The finding is wrong everywhere: deleted=1 (and status withdrawn, kept equal for the readers that still look at status),
    the change kept with its reason (nothing overwritten, nothing physically deleted)."""
    o = conn.execute("SELECT status, deleted FROM ib_observation WHERE id=?", (observation_id,)).fetchone()
    if o is None or o["deleted"]:
        raise Refused(f"observation {observation_id} is not a live observation")
    log(conn, observation_id, None, "deleted", 0, 1, reason, reading_id, run_id, who)
    if o["status"] != "withdrawn":
        log(conn, observation_id, None, "status", o["status"], "withdrawn", reason, reading_id, run_id, who)
    conn.execute("UPDATE ib_observation SET deleted=1, status='withdrawn', updated_at=? WHERE id=?", (_now(), observation_id))


withdraw_observation = soft_delete_observation        # the name the earlier callers use


def merge_observation(conn, dup_id: int, into_id: int, reason: str, reading_id, run_id: str, who: str) -> dict:
    """A duplicate description is merged into the observation that is kept (#2323, spec 4.7): its live nodes move to it (a node
    the kept observation already holds on the same occurrence and role is deleted instead), then the duplicate is soft deleted.
    Only the same description is merged."""
    d = conn.execute("SELECT * FROM ib_observation WHERE id=?", (dup_id,)).fetchone()
    k = conn.execute("SELECT * FROM ib_observation WHERE id=?", (into_id,)).fetchone()
    if d is None or d["deleted"] or k is None or k["deleted"] or dup_id == into_id:
        raise Refused(f"merge {dup_id} into {into_id}: both must be different live observations")
    if (d["obs_text"] or "").strip() != (k["obs_text"] or "").strip():
        raise Refused(f"merge {dup_id} into {into_id}: a merge is for the same description; the texts differ")
    seq = conn.execute("SELECT COALESCE(MAX(seq), 0) FROM ib_node WHERE observation_id=?", (into_id,)).fetchone()[0]
    moved = dropped = 0
    for n in conn.execute("SELECT * FROM ib_node WHERE observation_id=? AND deleted=0 ORDER BY seq, id", (dup_id,)).fetchall():
        twin = conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0 AND strong IS ? AND verse_reference IS ? "
                            "AND verse_lexical_id IS ? AND role IS ?",
                            (into_id, n["strong"], n["verse_reference"], n["verse_lexical_id"], n["role"])).fetchone()
        if twin:
            delete_node(conn, n["id"], f"the same node is on observation {into_id} (the duplicate description is merged)",
                        reading_id, run_id, who)
            dropped += 1
        else:
            seq += 1
            log(conn, dup_id, n["id"], "observation_id", dup_id, into_id, reason, reading_id, run_id, who)
            conn.execute("UPDATE ib_node SET observation_id=?, seq=? WHERE id=?", (into_id, seq, n["id"]))
            moved += 1
    soft_delete_observation(conn, dup_id, f"merged into observation {into_id}: {reason}", reading_id, run_id, who)
    return {"moved": moved, "dropped": dropped}


def modify_observation(cfg, conn, observation_id: int, sets: dict, reason: str, reading_id, run_id: str, who: str) -> list[str]:
    """A modify (#2320, spec 4.7): the observation is changed IN PLACE. Each changed column keeps its old value, new value and
    reason in ib_observation_change; the live row holds only the current version. Returns the columns changed."""
    loop = loop_setting(cfg)
    o = conn.execute("SELECT * FROM ib_observation WHERE id=?", (observation_id,)).fetchone()
    if o is None or o["deleted"]:
        raise Refused(f"observation {observation_id} is not a live observation")
    errors, quotes = [], []
    bad = sorted(set(sets) - set(loop["observation_set"]))
    if bad:
        raise Refused(f"observation {observation_id}: {bad} cannot be modified (allowed: {loop['observation_set']})")
    new = {k: (json.dumps(v, ensure_ascii=False) if k == "parts" and v is not None else v) for k, v in sets.items()}
    if "tag" in new and new["tag"] not in kinds(cfg):
        errors.append(f"tag must be one of {kinds(cfg)}")
    if "basis" in new and new["basis"] not in cfg.enum("ib_observation.basis"):
        errors.append(f"basis must be one of {cfg.enum('ib_observation.basis')}")
    if "route" in new and new["route"] is not None and new["route"] not in cfg.enum("observation_route"):
        errors.append(f"route must be one of {cfg.enum('observation_route')}")
    if "parts" in sets:
        check_parts(cfg, sets["parts"], "parts", errors)
    if "obs_text" in new:
        text = (new["obs_text"] or "").strip()
        try:
            recordingpass._validate_obs_text(conn, text)
        except recordingpass.InvalidObservationText as exc:
            errors.append(str(exc))
        dup = conn.execute("SELECT id FROM ib_observation WHERE trim(obs_text)=? AND deleted=0 AND id<>? LIMIT 1",
                           (text, observation_id)).fetchone()
        if dup:
            errors.append(f"this description is already live as observation {dup['id']}")
        new["obs_text"] = text
    quotes += sr._quote_check(conn, cfg, [new.get(k) for k in ("obs_text", "meaning", "implication")],
                              f"observation {observation_id}")
    if errors or quotes:
        raise Refused("; ".join(errors + quotes))
    changed = []
    for col, val in new.items():
        if o[col] != val:
            log(conn, observation_id, None, col, o[col], val, reason, reading_id, run_id, who)
            changed.append(col)
    if changed:
        conn.execute("UPDATE ib_observation SET " + ", ".join(f'"{c}"=?' for c in changed) + ", updated_at=? WHERE id=?",
                     [new[c] for c in changed] + [_now(), observation_id])
    return changed


def modify_node(cfg, conn, node_id: int, sets: dict, reason: str, reading_id, run_id: str, who: str) -> list[str]:
    """A modify of a node (#2320, spec 4.7): its occurrence, subgroup, cluster, role, surface or morph, in place, each change
    kept with its reason."""
    loop = loop_setting(cfg)
    n = conn.execute("SELECT * FROM ib_node WHERE id=?", (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} does not exist")
    bad = sorted(set(sets) - set(loop["node_set"]))
    if bad:
        raise Refused(f"node {node_id}: {bad} cannot be modified (allowed: {loop['node_set']})")
    if "role" in sets and sets["role"] not in node_roles(cfg):
        raise Refused(f"node {node_id}: role must be one of {node_roles(cfg)}")
    if "verse_lexical_id" in sets:
        row = conn.execute("SELECT vl.strong, v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
                           "WHERE vl.id=? AND vl.deleted=0", (sets["verse_lexical_id"],)).fetchone()
        if row is None or row["strong"] != n["strong"] or row["osisId"] != n["verse_reference"]:
            raise Refused(f"node {node_id}: occurrence {sets['verse_lexical_id']} is not an occurrence of "
                          f"{n['strong']} in {n['verse_reference']}")
    if "cluster_subgroup_code" in sets and sets["cluster_subgroup_code"] is not None and not conn.execute(
            "SELECT 1 FROM cluster_subgroup WHERE subgroup_code=? AND coalesce(delete_flagged,0)=0",
            (sets["cluster_subgroup_code"],)).fetchone():
        raise Refused(f"node {node_id}: {sets['cluster_subgroup_code']!r} is not a live subgroup")
    if ("cluster_code" in sets and sets["cluster_code"] is not None
            and sets["cluster_code"] not in word_clusters(conn, n["strong"])):
        raise Refused(f"node {node_id}: cluster must be one of {n['strong']}'s own clusters")
    changed = []
    for col, val in sets.items():
        if n[col] != val:
            log(conn, n["observation_id"], node_id, col, n[col], val, reason, reading_id, run_id, who)
            changed.append(col)
    if changed:
        conn.execute("UPDATE ib_node SET " + ", ".join(f'"{c}"=?' for c in changed) + " WHERE id=?",
                     [sets[c] for c in changed] + [node_id])
    return changed
