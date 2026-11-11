"""engagement.py -- the step before narration: what each surface of a collection does for the inner being (escalation #2406).

The rule is the researcher's, 2026-11-09 (design v3 answers, detailed design v1): a surface is assessed in each verse it occurs in, with the
role it takes there (a characteristic or a qualifier of an inner-being operation, a word that bears on one, or no bearing); the surface-level
group follows from the roles and replaces the draft group. Nothing here decides a rule: the roles, the tests, the group rule, the stage and the
folders are cfg_setting rows of module `engagement` (governance.rules_must_be_config_driven).

  pull(conn, cfg, name)            the working file of one collection: its member surfaces, their verses with the ESV text, and the observations
                                   already on those verses (any stage). The assessment reads the file, never the tables (D5).
                                   With a batch number (#2388) it is one batch of the same file: see batch_plan.
  check_assessment(...)            the filled assessment, checked whole; every problem is listed and nothing is written when there is one.
  record(...)                      one transaction: the actions on the existing observations, the new observations (one for each surface and
                                   role, a node for each verse where it holds; a no-bearing surface is a silence-kind observation), their nodes.
  group_plan / group_write         the surface-level group of each member surface, from its live nodes of the engagement stage.
  check_collection(...)            every member surface assessed in every one of its verses.

A surface in a verse is one verse_lexical row (its id is the key). A member surface of a collection is the link's own term and the terms whose
base is that term (collectionexport._memberships, own_link=True). Everything the assessment says is inferential (B:4) until the researcher
confirms it. Q5 (cluster): an observation takes the cluster of its first node; a node takes the cluster of the surface's own surface_subgroup row
for its Strong's code, else the first live cluster_strong row of the code. Q6: Group never changes a collection; a surface that moves to `other`
is reported."""
from __future__ import annotations

import collections
import datetime
import hashlib
import json
import pathlib
import re

from . import collectionexport as ce
from . import filingkit
from . import observationrecord as orec

Refused = orec.Refused


class EngagementError(Exception):
    """A usage or setting problem; routed as 'refused' and nothing is written."""


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def settings(cfg) -> dict:
    out = {}
    for key, name in (("engagement.stage", "stage"), ("engagement.roles", "roles"), ("engagement.group_rule", "group_rule"),
                      ("engagement.no_bearing_kind", "no_bearing_kind"), ("engagement.tests", "tests"), ("engagement.working_dir", "working_dir"),
                      ("engagement.group_judged_by", "judged_by"), ("engagement.report_path", "report_path")):
        try:
            out[name] = cfg.required_setting(key)
        except KeyError as exc:
            raise EngagementError(str(exc)) from exc
    loop = cfg.required_setting("reading.verse_loop")
    out["min_chars"] = loop["min_reason_chars"]
    out["results"] = loop["evaluation_results"]
    out["existing_actions"] = loop["existing_actions"]
    out["kinds"] = orec.kinds(cfg)
    out["tiers"] = cfg.required_setting("collection.member_tiers")
    return out


def collection_row(conn, name: str):
    name = (name or "").strip().lower()
    if not name:
        raise EngagementError("-Collection is required: the name of a collection (its core word)")
    row = conn.execute("SELECT c.id, c.name, c.status, t.surface, c.pole_word FROM collection c JOIN surface_term t ON t.id=c.core_term_id "
                       "WHERE c.deleted=0 AND lower(c.name)=?", (name,)).fetchone()
    if row is None:
        raise EngagementError(f"{name!r} is not a collection")
    return row


def member_terms(conn, cid: int, tiers: list) -> dict:
    """surface_term id -> (surface, strongest tier) for the member surfaces of one collection."""
    terms = {r[0]: r for r in conn.execute("SELECT id, surface, origin, surface_group, group_state, base_id FROM surface_term WHERE deleted=0")}
    out = {}
    for sid, mems in ce._memberships(conn, terms, tiers, own_link=True).items():
        mine = [m for m in mems if m[0] == cid]
        if mine:
            out[sid] = (terms[sid][1], min((m[3] for m in mine), key=lambda t: ce.TIER_ORDER.get(t, 9)))
    return out


def _clusters(conn, strong: str, surface: str) -> tuple[str | None, list]:
    """(the node's cluster, every live cluster of the code). Q5: the surface's own subgroup row first, else the first cluster_strong row."""
    allc = [r[0] for r in conn.execute("SELECT cluster_code FROM cluster_strong WHERE deleted=0 AND strong=? ORDER BY id", (strong,))]
    own = [r[0] for r in conn.execute("SELECT DISTINCT cluster_code FROM surface_subgroup WHERE deleted=0 AND strong=? AND surface=? ORDER BY id",
                                      (strong, surface))]
    return (own[0] if own else (allc[0] if allc else None)), allc


def batch_plan(surfaces: list, size: int) -> list:
    """The batches of a pull (escalation #2388, researcher: process in batches, work through the verses). A rule, not a choice, so the same
    collection always gives the same batches: the surfaces in the order given (alphabetical), each whole into the batch in hand while it fits within
    `size` verse items, else into a new batch; a surface of more than `size` items starts a new batch and is split in its verse order into batches of
    `size`, the last of them taking the next surface. Returns a list of batches, each a list of (surface index, first item, last item + 1)."""
    if size < 1:
        raise EngagementError("engagement.batch_size must be a whole number of 1 or more")
    batches, cur, used = [], [], 0
    for si, s in enumerate(surfaces):
        n = len(s["items"])
        if n == 0:
            continue
        if n > size:
            if cur:
                batches.append(cur)
            cur, used = [], 0
            for a in range(0, n, size):
                b = min(a + size, n)
                cur, used = [(si, a, b)], b - a
                if b < n:
                    batches.append(cur)
            continue
        if used + n > size:
            batches.append(cur)
            cur, used = [], 0
        cur.append((si, 0, n))
        used += n
    if cur:
        batches.append(cur)
    return batches


def _batch_settings(cfg) -> int:
    try:
        size = cfg.required_setting("engagement.batch_size")
    except KeyError as exc:
        raise EngagementError(str(exc)) from exc
    if not isinstance(size, int) or size < 1:
        raise EngagementError("engagement.batch_size must be a whole number of 1 or more")
    return size


def pull(conn, cfg, name: str, batch=None, size=None, missing: bool = False) -> dict:
    """The content of the working file (a dict), from the tables only. With `batch` (a number from 1) only that batch of the collection's surface
    items (batch_plan, `size` or engagement.batch_size) and the existing observations whose first batch it is (the lowest batch that holds one of
    their verses), so that each existing observation takes one action in one batch only. With `missing` (#2479) only the items with no live observation of
    the engagement stage are pulled, so a collection whose words are assessed is pulled again for its new members only."""
    st = settings(cfg)
    col = collection_row(conn, name)
    members = member_terms(conn, col[0], st["tiers"])
    if not members:
        raise EngagementError(f"collection {col[1]!r} has no member surface in the tiers {st['tiers']}")
    terms = {r[0]: r for r in conn.execute("SELECT id, surface, surface_group, group_state FROM surface_term WHERE deleted=0")}
    by_surface = {members[s][0]: s for s in members}
    rows = collections.defaultdict(list)
    for r in conn.execute("SELECT vl.id, vl.verse_id, lower(trim(vl.surface)), vl.strong, vl.morph_code, vl.surface_kind, vl.unit_surface, vl.unit_role, "
                          "v.osisId, v.reference, v.text FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0"):
        if r[2] in by_surface:
            rows[r[2]].append(r)
    surfaces, osis = [], set()
    for surf in sorted(by_surface):
        tid = by_surface[surf]
        items = []
        done = _live_nodes(conn, st["stage"], surf, [r[0] for r in rows.get(surf, [])]) if missing else {}
        for r in sorted(rows.get(surf, []), key=lambda x: (x[8] or "", x[0])):
            if r[0] in done:
                continue
            cluster, allc = _clusters(conn, r[3], surf)
            items.append({"vl_id": r[0], "osisId": r[8], "reference": r[9], "strong": r[3], "morph_code": r[4], "cluster": cluster, "clusters": allc,
                          "surface_kind": r[5], "unit_surface": r[6], "unit_role": r[7], "text": r[10]})
            osis.add(r[8])
        if missing and not items:
            continue
        surfaces.append({"term_id": tid, "surface": surf, "tier": members[tid][1], "group": terms[tid][2], "group_state": terms[tid][3], "items": items})
    if missing and not surfaces:
        raise EngagementError(f"collection {col[1]!r}: every item of its member surfaces already has an engagement observation, nothing to pull with -Missing")
    existing = {}
    for o in conn.execute("SELECT DISTINCT o.id, o.stage, o.tag, o.obs_text, o.status, o.basis FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id "
                          f"WHERE o.deleted=0 AND n.deleted=0 AND n.verse_reference IN ({','.join('?' * len(osis))}) ORDER BY o.id", sorted(osis)):
        nodes = [{"id": n[0], "strong": n[1], "surface": n[2], "role": n[3], "verse_lexical_id": n[4], "cluster": n[5], "verse": n[6]}
                 for n in conn.execute("SELECT id, strong, surface, role, verse_lexical_id, cluster_code, verse_reference FROM ib_node WHERE observation_id=? "
                                       "AND deleted=0 AND verse_reference IN (%s) ORDER BY seq" % ",".join("?" * len(osis)), [o[0]] + sorted(osis))]
        existing[str(o[0])] = {"id": o[0], "stage": o[1], "tag": o[2], "text": o[3], "status": o[4], "basis": o[5], "nodes": nodes}
    batch_info = None
    if batch is not None:
        if not isinstance(batch, int) or batch < 1:
            raise EngagementError("-Batch is a whole number from 1")
        size = size or _batch_settings(cfg)
        plan = batch_plan(surfaces, size)
        if batch > len(plan):
            raise EngagementError(f"-Batch {batch}: the collection has {len(plan)} batches of up to {size} items")
        first = {}                                          # the lowest batch that holds each verse
        for bn, parts in enumerate(plan, 1):
            for si, a, b in parts:
                for it in surfaces[si]["items"][a:b]:
                    first.setdefault(it["osisId"], bn)
        mine = {}
        for si, a, b in plan[batch - 1]:
            mine.setdefault(si, []).extend(surfaces[si]["items"][a:b])
        surfaces = [dict(surfaces[si], items=its) for si, its in sorted(mine.items())]
        existing = {k: o for k, o in existing.items() if min((first.get(n["verse"], 10 ** 9) for n in o["nodes"]), default=10 ** 9) == batch}
        batch_info = {"n": batch, "of": len(plan), "size": size, "items": sum(len(s["items"]) for s in surfaces)}
    return {"engagement": 1, "made_at": _now(), "collection": {"id": col[0], "name": col[1], "status": col[2], "core": col[3], "pole": col[4]},
            "tiers": st["tiers"], "roles": st["roles"], "tests": st["tests"], "no_bearing_kind": st["no_bearing_kind"], "batch": batch_info, "missing": bool(missing),
            "surfaces": surfaces, "existing_observations": existing,
            "how_to_fill": "evaluations: one for each surface item (vl_id); observations: one for each surface and role; existing: an action for each "
                           "existing observation (accept, modify, delete, merge, leave). See USER-GUIDE section 8.18."}


def next_path(cfg, kind: str, collection: str, ext: str = "json") -> pathlib.Path:
    """The path of a new file of a collection, by the filing convention (filingkit: a second file of the day is -v2 and the earlier one moves to archive)."""
    st = settings(cfg)
    out_dir = st["working_dir"] if ext == "json" else st["report_path"]
    return filingkit.versioned_path(cfg, f"engagement-{collection}-{kind}", out_dir=out_dir, ext=ext)


def write_json(path: pathlib.Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


def load_json(path) -> dict:
    p = pathlib.Path(path)
    if not p.is_file():
        raise EngagementError(f"{path} is not a file")
    try:
        return json.loads(p.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        raise EngagementError(f"{path} is not valid JSON: {exc}") from exc


def _check_eval(e: dict, where: str, st: dict, errors: list) -> None:
    """One evaluation of a surface item: result, reason, and the role, gives and test it needs."""
    roles = st["roles"]
    res = e.get("result")
    if res not in st["results"]:
        errors.append(f"{where}: result must be one of {st['results']}")
    if len((e.get("reason") or "").strip()) < st["min_chars"]:
        errors.append(f"{where}: reason needs {st['min_chars']} characters or more")
    if res == "relevant":
        if e.get("role") not in roles["relevant"]:
            errors.append(f"{where}: a relevant surface takes the role {roles['relevant']}")
        if e.get("role") == "qualifier" and not (e.get("gives") or "").strip():
            errors.append(f"{where}: a qualifier names what it gives the characteristic (gives)")
    elif res == "bears_on":
        if e.get("role") not in roles["bears_on"]:
            errors.append(f"{where}: a surface that bears on an act takes the role {roles['bears_on']}")
    elif res == "not_relevant" and e.get("role"):
        errors.append(f"{where}: a surface with no bearing has no role")
    if res in ("relevant", "bears_on") and e.get("test") not in st["tests"]:
        errors.append(f"{where}: test must be one of {sorted(st['tests'])} (the test of spec 4.1 the surface passed)")


def _check_observations(cfg, st: dict, items: dict, evals: dict, filled: dict, errors: list) -> tuple[list, dict]:
    """The observations of an assessment against its evaluations: each evaluated item in exactly one observation, kind and role fitting."""
    keys, covered, plan = set(), {}, []
    for n, o in enumerate(filled.get("observations") or []):
        k = o.get("key")
        where = f"observation {k or n + 1}"
        if not k or k in keys:
            errors.append(f"{where}: key missing or repeated")
        keys.add(k)
        kind, vls = o.get("kind"), o.get("vl_ids") or []
        if kind not in st["kinds"]:
            errors.append(f"{where}: kind must be one of {st['kinds']}")
        if o.get("basis") not in cfg.enum("ib_observation.basis"):
            errors.append(f"{where}: basis must be one of {cfg.enum('ib_observation.basis')}")
        if len((o.get("text") or "").strip()) < st["min_chars"]:
            errors.append(f"{where}: text needs {st['min_chars']} characters or more")
        if not vls:
            errors.append(f"{where}: no verses (vl_ids)")
        nodes = []
        for vl in vls:
            key = (o.get("surface"), vl)
            if key not in items:
                errors.append(f"{where}: ({o.get('surface')}, {vl}) is not a surface item of the pull")
                continue
            if key in covered:
                errors.append(f"{where}: ({o.get('surface')}, {vl}) is already in observation {covered[key]}")
                continue
            covered[key] = k
            e = evals.get(key)
            if e is None:
                continue
            if e.get("role") != (o.get("role") or None) and not (e.get("role") in (None, "") and not o.get("role")):
                errors.append(f"{where}: the evaluation of ({o.get('surface')}, {vl}) has the role {e.get('role')!r}, not {o.get('role')!r}")
            if (e.get("result") == "not_relevant") != (kind == st["no_bearing_kind"]):
                errors.append(f"{where}: kind {kind!r} does not fit the result {e.get('result')!r} of ({o.get('surface')}, {vl}) "
                              f"(a no-bearing surface is the kind {st['no_bearing_kind']!r}, and only it)")
            if e.get("result") == "relevant" and e.get("role") == "qualifier" and (e.get("gives") or "").strip() not in (o.get("gives") or ""):
                errors.append(f"{where}: its gives must name what the evaluation of ({o.get('surface')}, {vl}) gives")
            it = items[key][1]
            nodes.append({"verse_lexical_id": vl, "strong": it["strong"], "verse_reference": it["osisId"], "surface": o.get("surface"),
                          "morph_code": it["morph_code"], "cluster": it["cluster"], "role": e.get("role") or None})
        plan.append({"key": k, "surface": o.get("surface"), "kind": kind, "text": (o.get("text") or "").strip(), "meaning": o.get("meaning"),
                     "implication": o.get("implication"), "basis": o.get("basis"), "role": o.get("role") or None, "gives": o.get("gives"),
                     "test": o.get("test"), "nodes": nodes})
    for key, (s, i) in items.items():
        if key in evals and key not in covered:
            errors.append(f"({key[0]}, {key[1]} {i['reference']}) is evaluated but in no observation")
    return plan, covered


def check_assessment(conn, cfg, pulled: dict, filled: dict, errors: list) -> dict:
    """Check the filled assessment against its pull. Problems go to `errors`; returns the plan record() writes."""
    st = settings(cfg)
    roles = st["roles"]
    items = {(s["surface"], i["vl_id"]): (s, i) for s in pulled["surfaces"] for i in s["items"]}
    evals = {}
    for n, e in enumerate(filled.get("evaluations") or []):
        where = f"evaluation {n + 1} ({e.get('surface')}, {e.get('vl_id')})"
        key = (e.get("surface"), e.get("vl_id"))
        if key not in items:
            errors.append(f"{where}: not a surface item of the pull")
            continue
        if key in evals:
            errors.append(f"{where}: evaluated twice")
            continue
        _check_eval(e, where, st, errors)
        evals[key] = e
    for key in items:
        if key not in evals:
            errors.append(f"surface item ({key[0]}, {key[1]} {items[key][1]['reference']}) has no evaluation")
    plan, covered = _check_observations(cfg, st, items, evals, filled, errors)
    acts = {}
    existing = pulled.get("existing_observations") or {}
    for n, a in enumerate(filled.get("existing") or []):
        aid = str(a.get("id"))
        where = f"existing observation {aid}"
        if aid not in existing:
            errors.append(f"{where}: not an existing observation of the pull")
            continue
        if aid in acts:
            errors.append(f"{where}: more than one action")
            continue
        act = a.get("action")
        if act not in st["existing_actions"]:
            errors.append(f"{where}: action must be one of {st['existing_actions']}")
        elif act != "accept" and len((a.get("reason") or "").strip()) < st["min_chars"]:
            errors.append(f"{where}: a {act} needs its reason ({st['min_chars']} characters or more)")
        if act == "merge":
            tgt = a.get("into")
            if not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND deleted=0", (tgt,)).fetchone():
                errors.append(f"{where}: merge into {tgt!r}, which is not a live observation")
        acts[aid] = a
    for aid, o in existing.items():
        if aid not in acts and o["stage"] != st["stage"]:
            errors.append(f"existing observation {aid} (stage {o['stage']}, {o['tag']}): no action; every existing observation of these verses takes one")
    return {"plan": plan, "existing": acts, "evaluations": len(evals)}


def record(conn, cfg, run_id: str, plan: dict, who: str) -> dict:
    """Write a checked plan in the caller's transaction (the caller commits). Returns the counts and the ids."""
    st = settings(cfg)
    done = {"accepted": 0, "modified": 0, "deleted": 0, "merged": 0, "left": 0, "observations": 0, "reused": 0, "nodes": 0, "ids": {}}
    for aid, a in plan["existing"].items():
        oid, act, reason = int(aid), a["action"], (a.get("reason") or "").strip()
        if act == "modify":
            orec.modify_observation(Cfg_on(conn), conn, oid, a.get("set") or {}, reason, None, run_id, who)
            for nid, sets in (a.get("node_set") or {}).items():
                orec.modify_node(Cfg_on(conn), conn, int(nid), sets, reason, None, run_id, who)
            done["modified"] += 1
        elif act == "delete":
            orec.soft_delete_observation(conn, oid, reason, None, run_id, who)
            done["deleted"] += 1
        elif act == "merge":
            orec.merge_observation(conn, oid, int(a["into"]), reason, None, run_id, who)
            done["merged"] += 1
        else:
            done["accepted" if act == "accept" else "left"] += 1
    _write_plan(conn, st, plan["plan"], run_id, done)
    return done


def _write_plan(conn, st: dict, plans: list, run_id: str, done: dict) -> None:
    """Write checked observations and their nodes (reusing a live observation with the same text, skipping a node already there)."""
    now = _now()
    for p in plans:
        if not p["nodes"]:
            continue
        row = conn.execute("SELECT id FROM ib_observation WHERE deleted=0 AND stage=? AND tag=? AND trim(obs_text)=? ORDER BY id LIMIT 1",
                           (st["stage"], p["kind"], p["text"])).fetchone()
        if row:
            oid = row[0]
            done["reused"] += 1
        else:
            parts = {"engagement": True, "surface": p["surface"], "role": p["role"], "test": p["test"]}
            if p["gives"]:
                parts["gives"] = p["gives"]
            cluster = next((n["cluster"] for n in p["nodes"] if n["cluster"]), None)
            oid = conn.execute("INSERT INTO ib_observation (cluster_code, stage, tag, strong, obs_text, meaning, implication, basis, parts, meaning_source, "
                               "status, run_id, created_at) VALUES (?,?,?,?,?,?,?,?,?,'verse-text','draft',?,?)",
                               (cluster, st["stage"], p["kind"], p["nodes"][0]["strong"], p["text"], p["meaning"], p["implication"], p["basis"],
                                json.dumps(parts, ensure_ascii=False), run_id, now)).lastrowid
            done["observations"] += 1
        done["ids"][p["key"]] = oid
        seq = conn.execute("SELECT COALESCE(MAX(seq), 0) FROM ib_node WHERE observation_id=?", (oid,)).fetchone()[0]
        for n in p["nodes"]:
            if conn.execute("SELECT 1 FROM ib_node WHERE observation_id=? AND verse_lexical_id=? AND deleted=0", (oid, n["verse_lexical_id"])).fetchone():
                continue
            if not n["cluster"]:
                raise Refused(f"observation {p['key']}: the Strong's code {n['strong']} has no live cluster (ib_node.cluster_code is required)")
            seq += 1
            sg = orec.subgroup_code(conn, n["cluster"], n["strong"], n["surface"])
            conn.execute("INSERT INTO ib_node (observation_id, cluster_code, cluster_subgroup_code, strong, verse_reference, surface, morph_code, "
                         "source_stage, seq, role, reading_id, created_at, verse_lexical_id) VALUES (?,?,?,?,?,?,?,?,?,?,NULL,?,?)",
                         (oid, n["cluster"], sg, n["strong"], n["verse_reference"], n["surface"], n["morph_code"], st["stage"], seq, n["role"], now,
                          n["verse_lexical_id"]))
            done["nodes"] += 1


def Cfg_on(conn):
    from .cfg import Cfg
    return Cfg.on(conn)


def _live_nodes(conn, stage: str, term_surface: str, vl_ids: list):
    """The live nodes of the engagement stage on these verse_lexical rows: {vl_id: [role, ...]}."""
    out = collections.defaultdict(list)
    for i in range(0, len(vl_ids), 500):
        part = vl_ids[i:i + 500]
        for vl, role in conn.execute("SELECT n.verse_lexical_id, n.role FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 "
                                     f"AND o.deleted=0 AND o.stage=? AND n.verse_lexical_id IN ({','.join('?' * len(part))})", [stage] + part):
            out[vl].append(role)
    return out


def group_plan(conn, cfg, name: str) -> dict:
    """For each member surface of the collection: its group by the rule, from its live engagement nodes. A surface missing an assessment in any of
    its verses is `unassessed` and takes no group; a group the researcher confirmed is `held`."""
    st = settings(cfg)
    rule = st["group_rule"]
    col = collection_row(conn, name)
    members = member_terms(conn, col[0], st["tiers"])
    pl = {"collection": col[1], "change": [], "same": [], "unassessed": [], "held": [], "to_other": []}
    for tid, (surf, tier) in sorted(members.items(), key=lambda m: m[1][0]):
        vls = [r[0] for r in conn.execute("SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))=?", (surf,))]
        nodes = _live_nodes(conn, st["stage"], surf, vls)
        missing = [v for v in vls if v not in nodes]
        cur = conn.execute("SELECT surface_group, group_state, group_judged_by FROM surface_term WHERE id=?", (tid,)).fetchone()
        if missing or not vls:
            pl["unassessed"].append((surf, len(missing), len(vls)))
            continue
        roles = {r for rs in nodes.values() for r in rs}
        new = rule["characteristic"] if "characteristic" in roles else rule["qualifier"] if "qualifier" in roles else rule["none"]
        if cur[1] == "confirmed":
            pl["held"].append((surf, cur[0], new))
        elif cur[0] == new and cur[1] == "corrected" and cur[2] == st["judged_by"]:
            pl["same"].append(surf)
        else:
            pl["change"].append((tid, surf, cur[0], cur[1], new, sorted(r for r in roles if r)))
        if new == rule["none"]:
            pl["to_other"].append((surf, tier))
    return pl


def group_write(conn, cfg, run_id: str, pl: dict) -> int:
    st = settings(cfg)
    now = _now()
    for tid, surf, before, state_before, new, roles in pl["change"]:
        reason = f"engagement assessment of collection {pl['collection']}: roles {', '.join(roles) or 'none'} (#2406; group_state before: {state_before})"
        conn.execute("UPDATE surface_term SET surface_group=?, group_state='corrected', group_judged_by=?, group_reason=?, updated_at=?, run_id=? WHERE id=?",
                     (new, st["judged_by"], reason, now, run_id, tid))
        conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                     "VALUES ('surface_term',?,'set_group','surface_group',?,?,?,?,?,'engagement')", (tid, before, new, st["judged_by"], reason, run_id))
    return len(pl["change"])


def check_collection(conn, cfg, name: str) -> dict:
    """Every member surface assessed in every one of its verses (live nodes of the engagement stage), and the group each stands at."""
    st = settings(cfg)
    col = collection_row(conn, name)
    members = member_terms(conn, col[0], st["tiers"])
    rows, bad = [], 0
    for tid, (surf, tier) in sorted(members.items(), key=lambda m: m[1][0]):
        vls = [r[0] for r in conn.execute("SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))=?", (surf,))]
        nodes = _live_nodes(conn, st["stage"], surf, vls)
        miss = len([v for v in vls if v not in nodes])
        grp = conn.execute("SELECT surface_group, group_state FROM surface_term WHERE id=?", (tid,)).fetchone()
        roles = collections.Counter(r or "no_bearing" for rs in nodes.values() for r in rs)
        rows.append({"surface": surf, "tier": tier, "items": len(vls), "assessed": len(vls) - miss, "unassessed": miss, "roles": dict(roles),
                     "group": grp[0], "group_state": grp[1]})
        bad += 1 if miss or not vls else 0
    nb = conn.execute("SELECT n.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.stage=? AND n.role IS NULL "
                      "AND n.verse_lexical_id IN (SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN (%s))" % ",".join("?" * len(members)),
                      [st["stage"]] + [m[0] for m in members.values()]).fetchall() if members else []
    return {"collection": col[1], "surfaces": rows, "failing": bad, "no_bearing": len(nb), "reviewed": sum(1 for r in nb if _reviewed(conn, r[0]))}


def report_text(res: dict) -> str:
    lines = [f"# Engagement check of collection {res['collection']}", "",
             "Written by `Engagement.ps1 -Action Check` (#2406). Everything assessed is inferential (B:4) until the researcher confirms it.", "",
             "| surface | tier | verse items | assessed | not assessed | roles | group | group state |", "|---|---|---|---|---|---|---|---|"]
    for r in res["surfaces"]:
        lines.append(f"| {r['surface']} | {r['tier']} | {r['items']} | {r['assessed']} | {r['unassessed']} | "
                     f"{', '.join(f'{k} {v}' for k, v in sorted(r['roles'].items())) or '-'} | {r['group']} | {r['group_state']} |")
    lines += ["", f"Surfaces not fully assessed: {res['failing']}.",
              f"No-bearing items: {res.get('no_bearing', 0)}, confirmed in the review: {res.get('reviewed', 0)}."]
    return "\n".join(lines) + "\n"


def _reviewed(conn, node_id: int) -> bool:
    r = conn.execute("SELECT new_value FROM ib_observation_change WHERE node_id=? AND column_name='reviewed' ORDER BY id DESC LIMIT 1", (node_id,)).fetchone()
    return bool(r) and r[0] == "confirmed"


def review_pull(conn, cfg, name: str) -> dict:
    """The review of #2406 (ruling B, #2411): the verses where every member surface was assessed with no bearing, read again surface by surface.
    A verse is set aside only when all its surfaces are confirmed no-bearing; the items still to read are those not yet confirmed."""
    st = settings(cfg)
    col = collection_row(conn, name)
    members = member_terms(conn, col[0], st["tiers"])
    by_verse = collections.defaultdict(list)
    open_verses = set()
    for tid, (surf, tier) in sorted(members.items(), key=lambda m: m[1][0]):
        for r in conn.execute("SELECT vl.id, v.osisId, v.reference, v.text, vl.strong, vl.morph_code, vl.surface_kind, vl.unit_surface, vl.unit_role "
                              "FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.deleted=0 AND lower(trim(vl.surface))=?", (surf,)):
            node = conn.execute("SELECT n.id, n.role, o.id, o.obs_text FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 "
                                "AND o.deleted=0 AND o.stage=? AND n.verse_lexical_id=? ORDER BY n.id DESC LIMIT 1", (st["stage"], r[0])).fetchone()
            if node is None:
                open_verses.add(r[1])             # not assessed: the verse is not for the review yet
            cluster, allc = _clusters(conn, r[4], surf)
            by_verse[r[1]].append({"surface": surf, "tid": tid, "vl_id": r[0], "osisId": r[1], "reference": r[2], "text": r[3], "strong": r[4],
                                   "morph_code": r[5], "cluster": cluster, "clusters": allc, "surface_kind": r[6], "unit_surface": r[7], "unit_role": r[8],
                                   "node_id": node[0] if node else None, "role": node[1] if node else None, "observation_id": node[2] if node else None,
                                   "observation_text": node[3] if node else None, "confirmed": bool(node) and node[1] is None and _reviewed(conn, node[0])})
    surfaces, settled, verses = collections.defaultdict(list), 0, []
    for osis, its in sorted(by_verse.items()):
        if osis in open_verses or any(i["role"] is not None for i in its):
            continue                                     # a surface has bearing, or is not yet assessed: not a no-bearing verse
        if all(i["confirmed"] for i in its):
            settled += 1
            continue
        verses.append(osis)
        for i in its:
            if not i["confirmed"]:
                surfaces[i["surface"]].append({k: v for k, v in i.items() if k not in ("tid", "confirmed", "role")})
    return {"engagement": 1, "review": 1, "made_at": _now(), "collection": {"id": col[0], "name": col[1], "status": col[2], "core": col[3], "pole": col[4]},
            "roles": st["roles"], "tests": st["tests"], "no_bearing_kind": st["no_bearing_kind"], "verses": verses, "verses_set_aside": settled,
            "not_yet_assessed_verses": len(open_verses), "surfaces": [{"surface": k, "items": v} for k, v in sorted(surfaces.items())],
            "how_to_fill": "decisions: one for each item: confirm (still no bearing, with a reason) or reopen (it has bearing: result, role, gives, test, reason), "
                           "and observations for the reopened items as in an assessment. See USER-GUIDE section 8.18."}


def check_close(conn, cfg, rpull: dict, filled: dict, errors: list) -> dict:
    st = settings(cfg)
    items = {(s["surface"], i["vl_id"]): i for s in rpull["surfaces"] for i in s["items"]}
    decided, evals = {}, {}
    for n, d in enumerate(filled.get("decisions") or []):
        key = (d.get("surface"), d.get("vl_id"))
        where = f"decision {n + 1} ({key[0]}, {key[1]})"
        if key not in items:
            errors.append(f"{where}: not an item of the review file")
            continue
        if key in decided:
            errors.append(f"{where}: decided twice")
            continue
        decided[key] = d
        if d.get("decision") == "confirm":
            if len((d.get("reason") or "").strip()) < st["min_chars"]:
                errors.append(f"{where}: a confirm needs its reason ({st['min_chars']} characters or more)")
        elif d.get("decision") == "reopen":
            _check_eval(d, where, st, errors)
            if d.get("result") == "not_relevant":
                errors.append(f"{where}: a reopened item has bearing (result relevant or bears_on); a no-bearing result is a confirm")
            evals[key] = d
        else:
            errors.append(f"{where}: decision must be confirm or reopen")
    for key, i in items.items():
        if key not in decided:
            errors.append(f"review item ({key[0]}, {key[1]} {i['reference']}) has no decision")
    reopen_items = {k: ({"surface": k[0]}, items[k]) for k in evals}
    plan, _ = _check_observations(cfg, st, reopen_items, evals, filled, errors)
    return {"plan": plan, "confirm": [(items[k], d) for k, d in decided.items() if d.get("decision") == "confirm"],
            "reopen": [(items[k], d) for k, d in decided.items() if d.get("decision") == "reopen"]}


def close(conn, cfg, run_id: str, plan: dict, who: str) -> dict:
    st = settings(cfg)
    done = {"confirmed": 0, "reopened": 0, "observations": 0, "reused": 0, "nodes": 0, "ids": {}}
    for i, d in plan["confirm"]:
        orec.log(conn, i["observation_id"], i["node_id"], "reviewed", None, "confirmed", d["reason"].strip(), None, run_id, who)
        done["confirmed"] += 1
    for i, d in plan["reopen"]:
        orec.delete_node(conn, i["node_id"], f"review of the no-bearing result: {d['reason'].strip()}", None, run_id, who)
        if not conn.execute("SELECT 1 FROM ib_node WHERE observation_id=? AND deleted=0", (i["observation_id"],)).fetchone():
            orec.soft_delete_observation(conn, i["observation_id"], "every verse of this no-bearing observation was reopened in the review", None, run_id, who)
        done["reopened"] += 1
    _write_plan(conn, st, plan["plan"], run_id, done)
    return done


def sha(path) -> str:
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()[:16]
