"""surfacemap.py -- the surface mapping of an M cluster (escalation #2293, #2286 U3; design
outputs/escalation/2293-surface-map-design-v1-20261025.md). Behaviour rules B:117 and B:118.

A cluster's subgroups are groups of (code, surface) pairs (surface_subgroup). Per cluster:

  pairs   the pairs file: every pair with its hits, verses, gloss, two sample references, head or tail
          (cfg_setting cluster.surface_map.head_share of the cluster's hits), its inherited subgroup (the
          old one-code placement in cluster_subgroup_strong, #2286 B5) and its live allocation. Claude fills
          the groups and the allocations in session.
  apply   writes the filled file: groups (cluster_subgroup, with kind) and allocations (surface_subgroup).
          Refuses the whole file on any problem. The anomaly group is made once per cluster; pairs with an
          empty surface go to it.
  tail    the pairs still unallocated, allocated by the API to the cluster's groups or its anomaly group
          (assemble_tail builds the package and the estimate; apply_tail writes the reply).
  check   the report: each group's pairs, hits and share, groups of kind group over
          cluster.surface_map.max_group_share, the anomaly group, the unallocated pairs, the two-sense pairs.

Set-based queries over the cluster (B:71). Writes only through the step's grants (the handler checks them).
"""
from __future__ import annotations

import datetime
import json
import re

ANOMALY_LABEL = "Anomalies: pairs and nodes cleared by hand"
INHERITED = "inherited from"


class MapError(ValueError):
    """A request or file the step refuses; the message lists every problem."""


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def norm(surface) -> str:
    return (surface or "").strip().lower()


def anomaly_code(cluster: str) -> str:
    return f"{cluster}_anomaly"


def cluster_row(conn, cluster: str):
    row = conn.execute("SELECT cluster_code, short_name FROM cluster WHERE cluster_code=? AND coalesce(deleted,0)=0",
                       (cluster,)).fetchone()
    if row is None or not cluster.startswith("M"):
        raise MapError(f"{cluster!r} is not a live M cluster (the mapping covers M clusters only, B:117)")
    return row


def pairs(conn, cluster: str, head_share: float) -> list[dict]:
    """Every (code, surface) pair of the cluster, hits first, with head/tail, inherited and live allocation."""
    rows = conn.execute(
        "SELECT l.strong, lower(trim(coalesce(l.surface,''))) AS surface, count(*) AS hits, "
        "count(DISTINCT l.verse_id) AS verses, min(l.verse_id) AS v1, max(l.verse_id) AS v2 "
        "FROM verse_lexical l JOIN cluster_strong cs ON cs.strong=l.strong AND cs.deleted=0 AND cs.cluster_code=? "
        "WHERE l.deleted=0 GROUP BY l.strong, lower(trim(coalesce(l.surface,''))) "
        "ORDER BY hits DESC, l.strong, surface", (cluster,)).fetchall()
    total = sum(r["hits"] for r in rows)
    gloss = {r["strongNumber"]: (r["stepGloss"], r["stepTransliteration"]) for r in conn.execute(
        "SELECT strongNumber, stepGloss, stepTransliteration FROM strong WHERE strongNumber IN "
        "(SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0)", (cluster,))}
    ref = {r["id"]: r["osisId"] for r in conn.execute(
        "SELECT id, osisId FROM verse WHERE id IN (SELECT DISTINCT l.verse_id FROM verse_lexical l JOIN cluster_strong cs "
        "ON cs.strong=l.strong AND cs.deleted=0 AND cs.cluster_code=? WHERE l.deleted=0)", (cluster,))}
    inherited = {r["strong"]: r["subgroup_code"] for r in conn.execute(
        "SELECT css.strong, sg.subgroup_code FROM cluster_subgroup_strong css JOIN cluster_subgroup sg "
        "ON sg.id=css.cluster_subgroup_id WHERE sg.cluster_code=? AND coalesce(sg.delete_flagged,0)=0 "
        "AND css.delete_flagged=0", (cluster,))}
    live = {(r["strong"], r["surface"]): r for r in conn.execute(
        "SELECT ss.strong, ss.surface, ss.two_sense, ss.allocated_by, ss.reason, sg.subgroup_code FROM surface_subgroup ss "
        "JOIN cluster_subgroup sg ON sg.id=ss.cluster_subgroup_id WHERE ss.cluster_code=? AND ss.deleted=0", (cluster,))}
    out, acc = [], 0
    for r in rows:
        part = "head" if acc < head_share * total else "tail"
        acc += r["hits"]
        g, t = gloss.get(r["strong"], (None, None))
        cur = live.get((r["strong"], r["surface"]))
        out.append({"strong": r["strong"], "surface": r["surface"], "hits": r["hits"], "verses": r["verses"],
                    "gloss": g, "transliteration": t, "part": part,
                    "samples": sorted({ref.get(r["v1"]), ref.get(r["v2"])} - {None}),
                    "inherited": inherited.get(r["strong"]),
                    "group": cur["subgroup_code"] if cur else None, "two_sense": cur["two_sense"] if cur else 0,
                    "reason": cur["reason"] if cur else None, "allocated_by": cur["allocated_by"] if cur else None})
    return out


def groups(conn, cluster: str) -> list[dict]:
    return [dict(r) for r in conn.execute(
        "SELECT id, subgroup_code AS code, label, core_description AS description, kind, "
        "anchor_verse_reference AS anchor FROM cluster_subgroup WHERE cluster_code=? AND coalesce(delete_flagged,0)=0 "
        "ORDER BY sort_order, id", (cluster,))]


def build_file(conn, cluster: str, head_share: float) -> dict:
    """The pairs file Claude fills: groups to set, allocations to make. An inherited pair is prefilled with its
    old subgroup and an 'inherited from' reason (B5); a pair already allocated carries its live allocation."""
    row = cluster_row(conn, cluster)
    ps = pairs(conn, cluster, head_share)
    for p in ps:
        if p["group"] is None and p["inherited"]:
            p["group"] = p["inherited"]
            p["reason"] = f"{INHERITED} {p['inherited']} (#2286 B5)"
    head = [p for p in ps if p["part"] == "head"]
    return {"cluster": cluster, "cluster_name": row["short_name"], "built_at": now(), "head_share": head_share,
            "counts": {"pairs": len(ps), "head": len(head), "tail": len(ps) - len(head),
                       "hits": sum(p["hits"] for p in ps), "allocated": sum(1 for p in ps if p["allocated_by"]),
                       "inherited": sum(1 for p in ps if p["inherited"])},
            "how": "Set the groups (code <cluster>_<slug>, label, description, kind: group, qualifier or "
                   "not_this_sense; anchor optional). Give every head pair a group and a reason; tail pairs may be "
                   "left for the Tail step. two_sense 1 where the pair carries two senses. An inherited pair keeps "
                   "its subgroup unless its surface does not fit it: then change the group and start the reason "
                   "with 'correction:'. Then run -Step Apply with this file.",
            "groups": [{k: g[k] for k in ("code", "label", "description", "kind", "anchor")} for g in groups(conn, cluster)],
            "allocations": [{k: p[k] for k in ("strong", "surface", "part", "hits", "verses", "gloss", "transliteration",
                                              "samples", "inherited", "group", "reason", "two_sense")} for p in ps]}


def _kinds(conn) -> set[str]:
    return {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name='cluster_subgroup.kind' AND inactive=0")}


def ensure_anomaly(conn, cluster: str, run_id: str) -> int:
    row = conn.execute("SELECT id FROM cluster_subgroup WHERE cluster_code=? AND kind='anomaly' "
                       "AND coalesce(delete_flagged,0)=0", (cluster,)).fetchone()
    if row:
        return row["id"]
    t = now()
    return conn.execute(
        "INSERT INTO cluster_subgroup (cluster_code, subgroup_code, label, core_description, sort_order, status, "
        "version, source, notes, delete_flagged, created_at, last_updated_date, kind) "
        "VALUES (?,?,?,?,?,?,?,?,?,0,?,?, 'anomaly')",
        (cluster, anomaly_code(cluster), ANOMALY_LABEL, "Pairs that fit no group, and nodes that match more than one "
         "occurrence: cleared by hand (#2286 B2, B6)", 999, None, None, "#2293 cluster.surface_map", run_id,
         t, t)).lastrowid


def _write_pair(conn, cluster: str, p: dict, sg_id: int, allocated_by: str, run_id: str) -> str:
    """Insert, update or leave a pair's live row; returns 'inserted', 'updated' or 'unchanged'."""
    cur = conn.execute("SELECT id, cluster_subgroup_id, two_sense, reason FROM surface_subgroup WHERE cluster_code=? "
                       "AND strong=? AND surface=? AND deleted=0", (cluster, p["strong"], p["surface"])).fetchone()
    two = int(p.get("two_sense") or 0)
    if cur is None:
        conn.execute("INSERT INTO surface_subgroup (cluster_code, strong, surface, cluster_subgroup_id, two_sense, "
                     "status, allocated_by, reason, run_id, created_by) VALUES (?,?,?,?,?,'provisional',?,?,?,?)",
                     (cluster, p["strong"], p["surface"], sg_id, two, allocated_by, p["reason"], run_id, "Claude"))
        return "inserted"
    if (cur["cluster_subgroup_id"], cur["two_sense"], cur["reason"]) == (sg_id, two, p["reason"]):
        return "unchanged"
    conn.execute("UPDATE surface_subgroup SET cluster_subgroup_id=?, two_sense=?, allocated_by=?, reason=?, run_id=?, "
                 "updated_at=? WHERE id=?", (sg_id, two, allocated_by, p["reason"], run_id, now(), cur["id"]))
    return "updated"


def apply_file(conn, cluster: str, data: dict, head_share: float, run_id: str) -> dict:
    """Write a filled pairs file. Every problem is collected; any problem refuses the whole file."""
    cluster_row(conn, cluster)
    problems = []
    if data.get("cluster") != cluster:
        problems.append(f"the file is for {data.get('cluster')!r}, not {cluster}")
    kinds = _kinds(conn) - {"anomaly"}
    existing = {g["code"]: g for g in groups(conn, cluster)}
    new_groups = []
    seen = set()
    for i, g in enumerate(data.get("groups") or []):
        code = (g.get("code") or "").strip()
        if not code:
            problems.append(f"group {i + 1}: no code")
            continue
        if code in seen:
            problems.append(f"group {code}: listed twice")
        seen.add(code)
        if code in existing:
            continue
        if g.get("kind") not in kinds:
            problems.append(f"group {code}: kind {g.get('kind')!r} is not one of {sorted(kinds)}")
        if not (g.get("label") or "").strip():
            problems.append(f"group {code}: no label")
        if not code.startswith(f"{cluster}_") or not re.fullmatch(r"[A-Za-z0-9_]+", code):
            problems.append(f"group {code}: a new code is <cluster>_<slug> (letters, digits, underscores)")
        new_groups.append(g)
    known = set(existing) | {g.get("code") for g in new_groups} | {anomaly_code(cluster)}
    live = {(p["strong"], p["surface"]): p for p in pairs(conn, cluster, head_share)}
    given = {}
    for a in data.get("allocations") or []:
        key = (a.get("strong"), norm(a.get("surface")))
        if key not in live:
            problems.append(f"pair {key[0]} {key[1]!r}: not a pair of {cluster}")
            continue
        if not a.get("group"):
            continue
        if a["group"] not in known:
            problems.append(f"pair {key[0]} {key[1]!r}: group {a['group']!r} is not a group of {cluster}")
        if not (a.get("reason") or "").strip():
            problems.append(f"pair {key[0]} {key[1]!r}: no reason")
        inh = live[key]["inherited"]
        if inh and a["group"] != inh and not (a.get("reason") or "").strip().lower().startswith("correction:"):
            problems.append(f"pair {key[0]} {key[1]!r}: moved from its inherited subgroup {inh} without a "
                            "'correction:' reason (#2286 B5: an inherited pair moves only where its data is in error)")
        if str(a.get("two_sense", 0)) not in ("0", "1"):
            problems.append(f"pair {key[0]} {key[1]!r}: two_sense must be 0 or 1")
        given[key] = a
    for key, p in live.items():
        if p["part"] == "head" and key[1] and key not in given and not p["allocated_by"]:
            problems.append(f"head pair {key[0]} {key[1]!r}: no group")
    if problems:
        raise MapError(f"{len(problems)} problem(s), nothing written:\n  " + "\n  ".join(problems))
    counts = {"groups_added": 0, "inserted": 0, "updated": 0, "unchanged": 0,
              "stale_retired": retire_stale(conn, cluster, run_id)}
    t = now()
    base = conn.execute("SELECT coalesce(max(sort_order),0) FROM cluster_subgroup WHERE cluster_code=? AND kind!='anomaly'",
                        (cluster,)).fetchone()[0]
    for i, g in enumerate(new_groups, 1):
        conn.execute("INSERT INTO cluster_subgroup (cluster_code, subgroup_code, label, core_description, "
                     "anchor_verse_reference, sort_order, status, source, notes, delete_flagged, created_at, "
                     "last_updated_date, kind) VALUES (?,?,?,?,?,?,NULL,'#2293 cluster.surface_map',?,0,?,?,?)",
                     (cluster, g["code"], g["label"].strip(), g.get("description"), g.get("anchor"), base + i, run_id,
                      t, t, g["kind"]))
        counts["groups_added"] += 1
    anomaly = ensure_anomaly(conn, cluster, run_id)
    ids = {r["subgroup_code"]: r["id"] for r in conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code=? AND coalesce(delete_flagged,0)=0", (cluster,))}
    for key, a in given.items():
        p = {"strong": key[0], "surface": key[1], "reason": a["reason"].strip(), "two_sense": a.get("two_sense", 0)}
        inherited = live[key]["inherited"]
        by = "inherited" if inherited and a["group"] == inherited and p["reason"].startswith(INHERITED) else "session"
        counts[_write_pair(conn, cluster, p, ids[a["group"]], by, run_id)] += 1
    for key, p in live.items():
        if not key[1]:
            counts[_write_pair(conn, cluster, {"strong": key[0], "surface": "", "reason": "empty surface in "
                                               "verse_lexical: cleared by hand (#2286 C4)"}, anomaly, "session",
                               run_id)] += 1
    return counts


# ── tail (the API pass, B1, C1) ─────────────────────────────────────────────────────────────────

def tail_pairs(conn, cluster: str, head_share: float) -> list[dict]:
    ps = [p for p in pairs(conn, cluster, head_share) if not p["allocated_by"] and p["surface"]]
    if not ps:
        return ps
    first = {}
    for p in ps:
        if p["samples"]:
            first[(p["strong"], p["surface"])] = p["samples"][0]
    text = {r["osisId"]: r["text"] for r in conn.execute(
        f"SELECT osisId, text FROM verse WHERE deleted=0 AND osisId IN ({','.join('?' * len(set(first.values())))})",
        sorted(set(first.values())))}
    for p in ps:
        ref = first.get((p["strong"], p["surface"]))
        p["sample"] = {"ref": ref, "text": text.get(ref)} if ref else None
    return ps


def _not_this_sense_line(gs: list[dict]) -> str:
    """The instruction for a rendering with no sense of the cluster (#2298 P1): it goes to the cluster's
    not_this_sense group, where it has one."""
    codes = [g["code"] for g in gs if g["kind"] == "not_this_sense"]
    if not codes:
        return ""
    return (f"A rendering whose sense is plainly not the cluster's (a name, a measure, a place, a plain act with no "
            f"sense of the cluster) goes to {codes[0]}. ")


def assemble_tail(cfg, conn, cluster: str, head_share: float) -> dict:
    """The tail package and its estimate; never calls the network (D2: code, gloss, surface, one sample verse)."""
    row = cluster_row(conn, cluster)
    gs = [g for g in groups(conn, cluster)]
    if not [g for g in gs if g["kind"] != "anomaly"]:
        raise MapError(f"{cluster} has no groups yet: run -Step Pairs, fill the groups and the head, then -Step Apply")
    ps = tail_pairs(conn, cluster, head_share)
    head = [p for p in ps if p["part"] == "head"]
    if head:
        raise MapError(f"{cluster}: {len(head)} head pair(s) not yet allocated (the head is allocated in session, "
                       f"B1): fill them in the pairs file and run -Step Apply first")
    rules ="\n".join(f"- {r['rule_key']}: {r['rule_text']}" for r in conn.execute(
        "SELECT rule_key, rule_text FROM cfg_behaviour_rule WHERE active=1 AND class='study_method' AND rule_key IN "
        "('subgroups-are-surface-groups', 'surface-mapping-conditions') ORDER BY id"))
    instructions = (
        f"You allocate the remaining (Strong's code, English surface) pairs of cluster {cluster} "
        f"({row['short_name']}) to its subgroups. The rules:\n{rules}\n\n"
        "For each pair you are given its code, gloss, surface (the ESV rendering) and one verse where it occurs. "
        "Put every pair in exactly one of the groups given, by what the surface says in that verse. "
        f"{_not_this_sense_line(gs)}A pair you cannot decide goes to {anomaly_code(cluster)}, which is cleared by "
        "hand: use it only for that, never for a rendering whose sense is plainly not the cluster's. "
        "Set two_sense 1 where the surface plainly carries two senses "
        "across its uses. Give a short reason for each placement. The placement is provisional, a way into the "
        "verses, not a finding.\n\n"
        'Reply with JSON only: {"allocations": [{"strong": "...", "surface": "...", "group": "...", '
        '"two_sense": 0, "reason": "..."}]}, one entry for every pair, nothing else.')
    content = json.dumps({"cluster": cluster, "groups": [{k: g[k] for k in ("code", "label", "description", "kind")}
                                                         for g in gs],
                          "pairs": [{"strong": p["strong"], "gloss": p["gloss"], "surface": p["surface"],
                                     "sample": p["sample"]} for p in ps]}, ensure_ascii=False)
    cpt = float(cfg.setting("lexical.llm_chars_per_token", 4))
    est_in = int((len(instructions) + len(content)) / cpt)
    max_out = int(cfg.required_setting("cluster.surface_map.tail_max_output_tokens"))
    rate_in = float(cfg.required_setting("lexical.llm_rate_input_per_million"))
    rate_out = float(cfg.required_setting("lexical.llm_rate_output_per_million"))
    return {"instructions": instructions, "content": content, "pairs": ps, "model": cfg.required_setting("lexical.llm_model"),
            "max_output_tokens": max_out, "est_input_tokens": est_in,
            "est_cost_usd": round(est_in / 1e6 * rate_in + max_out / 1e6 * rate_out, 4)}


_FENCE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)
_QUOTES = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"'})


def _match_key(surface) -> str:
    """How a reply's surface is matched to a tail pair: curly quotes and runs of spaces normalised, so a model that
    straightens an apostrophe still names its pair; the pair keeps its exact surface (#2298)."""
    return " ".join(norm(surface).translate(_QUOTES).split())


def parse_tail(text: str, ps: list[dict], codes: set[str]) -> list[dict]:
    """The model's reply, checked: every tail pair exactly once, a known group, a reason. Raises MapError."""
    m = _FENCE.search(text.strip())
    body = m.group(1) if m else text.strip()
    if not m and not body.startswith("{") and "{" in body:   # prose before or after the object (#2298)
        body = body[body.index("{"):body.rindex("}") + 1]
    try:
        reply = json.loads(body, strict=False)
        allocs = reply["allocations"]
    except (ValueError, KeyError, TypeError) as exc:
        raise MapError(f"the reply is not JSON with an 'allocations' list: {exc}; first 300 chars: {text[:300]!r}")
    want = {(p["strong"], p["surface"]) for p in ps}
    exact = {(p["strong"], _match_key(p["surface"])): (p["strong"], p["surface"]) for p in ps}
    got, problems = {}, []
    for a in allocs:
        key = exact.get((a.get("strong"), _match_key(a.get("surface"))), (a.get("strong"), norm(a.get("surface"))))
        if key not in want:
            problems.append(f"{key}: not a tail pair")
        elif key in got:
            problems.append(f"{key}: given twice")
        elif a.get("group") not in codes:
            problems.append(f"{key}: group {a.get('group')!r} unknown")
        elif not (a.get("reason") or "").strip():
            problems.append(f"{key}: no reason")
        else:
            got[key] = a
    problems += [f"{k}: missing" for k in sorted(want - set(got))]
    if problems:
        raise MapError(f"{len(problems)} problem(s) in the reply, nothing written:\n  " + "\n  ".join(problems[:40]))
    return [{"strong": k[0], "surface": k[1], "group": a["group"], "reason": a["reason"].strip(),
             "two_sense": 1 if str(a.get("two_sense", 0)) == "1" else 0} for k, a in got.items()]


def apply_tail(conn, cluster: str, allocs: list[dict], run_id: str) -> dict:
    ensure_anomaly(conn, cluster, run_id)
    ids = {r["subgroup_code"]: r["id"] for r in conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code=? AND coalesce(delete_flagged,0)=0", (cluster,))}
    counts = {"inserted": 0, "updated": 0, "unchanged": 0}
    for a in allocs:
        counts[_write_pair(conn, cluster, a, ids[a["group"]], "api", run_id)] += 1
    return counts


# ── stale and unallocated pairs (C5, #2294) ─────────────────────────────────────────────────────

_STALE = ("SELECT ss.id, ss.cluster_code, ss.strong, ss.surface, ss.reason, "
          "CASE WHEN NOT EXISTS (SELECT 1 FROM cluster_strong cs WHERE cs.cluster_code=ss.cluster_code "
          "AND cs.strong=ss.strong AND cs.deleted=0) THEN 'the code is no longer in the cluster' "
          "ELSE 'the surface no longer occurs for the code' END AS why "
          "FROM surface_subgroup ss WHERE ss.deleted=0 {where} AND (NOT EXISTS (SELECT 1 FROM cluster_strong cs "
          "WHERE cs.cluster_code=ss.cluster_code AND cs.strong=ss.strong AND cs.deleted=0) OR NOT EXISTS "
          "(SELECT 1 FROM verse_lexical l WHERE l.strong=ss.strong AND l.deleted=0 "
          "AND lower(trim(coalesce(l.surface,'')))=ss.surface))")


def stale(conn, cluster: str | None = None) -> list[dict]:
    """Live pairs whose code has left the cluster or whose surface no longer occurs (C5)."""
    where, args = ("AND ss.cluster_code=?", (cluster,)) if cluster else ("", ())
    return [dict(r) for r in conn.execute(_STALE.format(where=where), args)]


def unallocated(conn, cluster: str) -> int:
    return conn.execute(
        "SELECT count(*) FROM (SELECT DISTINCT l.strong, lower(trim(coalesce(l.surface,''))) AS s FROM verse_lexical l "
        "JOIN cluster_strong cs ON cs.strong=l.strong AND cs.deleted=0 AND cs.cluster_code=? WHERE l.deleted=0) p "
        "WHERE NOT EXISTS (SELECT 1 FROM surface_subgroup ss WHERE ss.cluster_code=? AND ss.strong=p.strong "
        "AND ss.surface=p.s AND ss.deleted=0)", (cluster, cluster)).fetchone()[0]


def overview(conn) -> list[dict]:
    """Every M cluster's mapping in one pass: pairs, allocated, unallocated, stale (cluster.validate)."""
    rows = conn.execute(
        "WITH p AS (SELECT DISTINCT cs.cluster_code AS c, l.strong, lower(trim(coalesce(l.surface,''))) AS s "
        "FROM verse_lexical l JOIN cluster_strong cs ON cs.strong=l.strong AND cs.deleted=0 AND cs.cluster_code LIKE 'M%' "
        "WHERE l.deleted=0) SELECT p.c AS cluster, count(*) AS pairs, sum(ss.id IS NOT NULL) AS allocated FROM p "
        "LEFT JOIN surface_subgroup ss ON ss.cluster_code=p.c AND ss.strong=p.strong AND ss.surface=p.s AND ss.deleted=0 "
        "GROUP BY p.c ORDER BY p.c").fetchall()
    st = {}
    for r in stale(conn):
        st[r["cluster_code"]] = st.get(r["cluster_code"], 0) + 1
    return [{"cluster": r["cluster"], "pairs": r["pairs"], "allocated": r["allocated"],
             "unallocated": r["pairs"] - r["allocated"], "stale": st.get(r["cluster"], 0)} for r in rows]


def reading_refusal(conn, cluster: str) -> str | None:
    """The reason reading.open refuses this home cluster, or None (B:118, #2294 G-a): an M cluster with unallocated
    or stale pairs is not read until they are."""
    if not cluster.startswith("M"):
        return None
    n, s = unallocated(conn, cluster), len(stale(conn, cluster))
    if not n and not s:
        return None
    return (f"-Home {cluster}: {n} unallocated and {s} stale (code, surface) pair(s). A cluster with unallocated or "
            f"stale pairs is not read until they are (behaviour rule surface-mapping-conditions). Map it first: "
            f"iba\\app\\ps\\Surface-Map.ps1 -Step Pairs -Cluster {cluster}, then Apply, Tail and Check.")


def retire_stale(conn, cluster: str, run_id: str) -> int:
    """Soft-delete the cluster's stale pairs, the reason kept on the row; returns how many (C5)."""
    rows = stale(conn, cluster)
    for r in rows:
        conn.execute("UPDATE surface_subgroup SET deleted=1, reason=?, run_id=?, updated_at=? WHERE id=?",
                     (f"stale: {r['why']} (was: {r['reason']})", run_id, now(), r["id"]))
    return len(rows)


# ── check ───────────────────────────────────────────────────────────────────────────────────────

def check(conn, cluster: str, head_share: float, max_share: float) -> dict:
    row = cluster_row(conn, cluster)
    ps = pairs(conn, cluster, head_share)
    total = sum(p["hits"] for p in ps) or 1
    gs = groups(conn, cluster)
    by = {g["code"]: {**g, "pairs": 0, "hits": 0} for g in gs}
    for p in ps:
        if p["group"]:
            by[p["group"]]["pairs"] += 1
            by[p["group"]]["hits"] += p["hits"]
    for g in by.values():
        g["share"] = round(g["hits"] / total, 4)
        g["over"] = g["kind"] == "group" and g["share"] > max_share
    return {"cluster": cluster, "cluster_name": row["short_name"], "checked_at": now(), "max_group_share": max_share,
            "pairs": len(ps), "hits": total, "groups": list(by.values()),
            "unallocated": [p for p in ps if not p["group"]],
            "anomaly": [p for p in ps if p["group"] == anomaly_code(cluster)],
            "two_sense": [p for p in ps if p["two_sense"]],
            "stale": [{**r, "gloss": None, "hits": 0} for r in stale(conn, cluster)]}


def check_markdown(r: dict) -> str:
    pct = lambda x: f"{x * 100:.1f}%"  # noqa: E731
    lines = [f"# Surface map check: {r['cluster']} {r['cluster_name']}", "",
             f"Checked {r['checked_at']}. {r['pairs']} pairs, {r['hits']} hits. A group of kind group over "
             f"{pct(r['max_group_share'])} of the cluster's hits is flagged (cfg_setting "
             "cluster.surface_map.max_group_share): look at it, it is not a forced split.", "",
             "## Groups", "", "| code | label | kind | pairs | hits | share | flag |", "|---|---|---|---|---|---|---|"]
    for g in r["groups"]:
        lines.append(f"| {g['code']} | {g['label']} | {g['kind']} | {g['pairs']} | {g['hits']} | {pct(g['share'])} | "
                     f"{'over' if g['over'] else ''} |")
    for title, rows in (("Unallocated pairs", r["unallocated"]), ("Anomaly group", r["anomaly"]),
                        ("Two-sense pairs", r["two_sense"])):
        lines += ["", f"## {title} ({len(rows)})", ""]
        lines += [f"- {p['strong']} {p['surface']!r} ({p['gloss']}; {p['hits']} hits){': ' + p['reason'] if p.get('reason') else ''}"
                  for p in rows] or ["None."]
    lines += ["", f"## Stale pairs ({len(r['stale'])})", "", "Soft-deleted with their reason by the next -Step Apply.", ""]
    lines += [f"- {p['strong']} {p['surface']!r}: {p['why']}" for p in r["stale"]] or ["None."]
    return "\n".join(lines) + "\n"
