"""noderesolve.py -- the sweep that resolves the references on ib_node (escalation #2308; researcher, chat 2026-10-26: the
sub_group codes missing on nodes are to be looked up through the strong and the verse; method rules NR-01 to NR-06 on
node_resolve.apply).

A node that names a strong and a verse is resolved from the tables, never from the document:
  plan():   for every node with a strong and a missing verse_lexical_id or cluster_subgroup_code, the occurrence(s) of the
            strong in the verse (verse_lexical) and the subgroup of the occurrence's surface in the node's cluster
            (surface_subgroup, cluster_subgroup). Returns what would be filled, and why the rest cannot be. Reads only.
  apply():  writes the planned values, each only where the node still holds what the plan saw (a stale node is skipped
            and listed), only into a null column, in the caller's transaction.
A value already on a node is never overwritten (NR-05).
"""
from __future__ import annotations

import collections
import datetime

from . import surfacemap as sm

FILLS = ("verse_lexical_id", "morph_code", "cluster_subgroup_code")


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan(conn) -> dict:
    sub: dict = {}
    for r in conn.execute("SELECT ss.cluster_code, ss.strong, ss.surface, cs.subgroup_code FROM surface_subgroup ss "
                          "JOIN cluster_subgroup cs ON cs.id=ss.cluster_subgroup_id WHERE ss.deleted=0"):
        sub[(r[0], r[1], sm.norm(r[2]))] = r[3]
    defined = {(k[0], k[1]) for k in sub}
    verse = {r[1]: r[0] for r in conn.execute("SELECT id, osisId FROM verse")}
    occ: dict = collections.defaultdict(list)
    for r in conn.execute("SELECT id, verse_id, strong, surface, morph_code FROM verse_lexical WHERE deleted=0"):
        occ[(r[1], r[2])].append(r)
    changes, left = [], collections.defaultdict(list)
    counts: collections.Counter = collections.Counter()
    q = ("SELECT id, cluster_code, cluster_subgroup_code, strong, verse_reference, surface, morph_code, verse_lexical_id, "
         "source_stage FROM ib_node WHERE strong IS NOT NULL AND (verse_lexical_id IS NULL OR cluster_subgroup_code IS NULL)")
    for n in conn.execute(q):
        nid, cl, sg, strong, vref, surf, morph, vlid, stage = n
        vid = verse.get(vref)
        if vid is None:
            left["the verse is not in the verse table"].append(nid)
            continue
        rows = occ.get((vid, strong), [])
        if vlid:
            rows = [x for x in rows if x[0] == vlid] or rows
        if not rows:
            left["the strong does not occur in the verse (verse_lexical)"].append(nid)
            continue
        pick = rows
        if len(rows) > 1 and surf:
            m = [x for x in rows if sm.norm(x[3]) == sm.norm(surf)]
            if len(m) == 1:
                pick = m
        after: dict = {}
        if len(pick) == 1 and not vlid:
            after["verse_lexical_id"] = pick[0][0]
            if not morph and pick[0][4]:
                after["morph_code"] = pick[0][4]
        if not sg:
            sgs = {sub.get((cl, strong, sm.norm(x[3]))) for x in pick} - {None}
            if (cl, strong) not in defined:
                left["no subgroup is defined for the strong in the cluster"].append(nid)
            elif len(sgs) == 1:
                after["cluster_subgroup_code"] = next(iter(sgs))
            elif not sgs:
                left["no subgroup row for the occurrence's surface"].append(nid)
            else:
                left["the occurrences disagree on the subgroup"].append(nid)
        if after:
            changes.append({"id": nid, "stage": stage, "cluster": cl, "strong": strong, "verse": vref,
                            "before": {"verse_lexical_id": vlid, "morph_code": morph, "cluster_subgroup_code": sg},
                            "after": after})
            for k in after:
                counts[k] += 1
        counts["nodes examined"] += 1
    return {"kind": "node-resolve", "version": 1, "built_at": _now(), "changes": changes,
            "left": {k: v for k, v in left.items()}, "counts": dict(counts)}


def apply(conn, p: dict) -> dict:
    done = stale = 0
    stale_ids = []
    for c in p["changes"]:
        cur = conn.execute("SELECT verse_lexical_id, morph_code, cluster_subgroup_code FROM ib_node WHERE id=?",
                           (c["id"],)).fetchone()
        b = c["before"]
        if cur is None or (cur[0], cur[1], cur[2]) != (b["verse_lexical_id"], b["morph_code"], b["cluster_subgroup_code"]):
            stale += 1
            stale_ids.append(c["id"])
            continue
        sets = ", ".join(f"{k}=?" for k in c["after"])
        conn.execute(f"UPDATE ib_node SET {sets} WHERE id=?", list(c["after"].values()) + [c["id"]])
        done += 1
    return {"applied": done, "stale": stale, "stale_ids": stale_ids[:50]}


def report_lines(p: dict, applied: dict | None = None) -> list[str]:
    ch = p["changes"]
    by_stage = collections.Counter(c["stage"] or "(none)" for c in ch)
    by_cluster = collections.Counter(c["cluster"] for c in ch)
    out = ["# Node reference sweep (#2308)", "",
           f"Built {p['built_at']}. {p['counts'].get('nodes examined', 0)} node(s) examined; {len(ch)} to be filled "
           f"({p['counts'].get('verse_lexical_id', 0)} occurrence id(s), {p['counts'].get('morph_code', 0)} morph code(s), "
           f"{p['counts'].get('cluster_subgroup_code', 0)} subgroup code(s)).", ""]
    if applied:
        out += [f"Applied: {applied['applied']} node(s) written, {applied['stale']} skipped as changed since the plan.", ""]
    out += ["## Nodes filled, by stage", ""] + [f"- {s}: {n}" for s, n in by_stage.most_common()] + ["",
            "## Nodes filled, by cluster (top 25)", ""] + [f"- {s}: {n}" for s, n in by_cluster.most_common(25)] + [
            "", "## Nodes left as they are, and why", ""]
    for reason, ids in sorted(p["left"].items(), key=lambda kv: -len(kv[1])):
        out.append(f"- {reason}: {len(ids)} (for example node ids {', '.join(str(i) for i in ids[:5])})")
    return out + [""]
