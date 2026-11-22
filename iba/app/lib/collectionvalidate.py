"""collectionvalidate.py -- the validation after stage 4 of a collection (escalation #2538; plan
`outputs/escalation/2538-validation-step-plan-v9-20261122.md`; the researcher's principles of 2026-11-22).

    pull   the scope of a collection (every live observation related to it) with the structural tests: no live node, a word node missing
           a required column, a trace to a deleted observation, a same-text duplicate, an observation not yet marked; and the worksheet to read
    check  the completeness check in two layers, evidence first, the inner-being layer only when the evidence layer passes; the deferrals
           addressed to the collection and those it made
    record a sheet of actions (validationactions) checked and written in one transaction; any problem refuses all of it; keep=False previews

The scope (principle 1): a) a live node carrying the collection; b) a live node on a verse of the collection; c) a live node on a member
surface with its own lettered Strong's code (the surface|strong subjects of the stage 1 ledger rows), or an observation with no live node whose own
strong is one of them; d) its meaning relates to it: found by reading, not by code. Deleted observations and nodes are excluded. A node that reaches
into another collection is counted: its observation is in scope and each node is verified traceable. The rules the code holds are cfg_setting
validate.reading (the required word columns, the actions a sheet may hold); no tunable value is in the code.
"""
from __future__ import annotations

import inspect
import json
import re
import sqlite3
from collections import Counter, defaultdict

from . import observationrecord as orec
from . import validationactions as va

CHUNK = 400
SAVEPOINT = "validate_record"


class ValidateError(Exception):
    """A usage or data problem: routed as the condition 'refused'; nothing is written."""


def _chunks(seq, n=CHUNK):
    seq = list(seq)
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def _qm(items) -> str:
    return ",".join("?" * len(items))


def settings(cfg) -> dict:
    v = cfg.required_setting("validate.reading")
    return json.loads(v) if isinstance(v, str) else v


def collection_id(conn, name_or_id) -> int:
    if str(name_or_id).strip().isdigit():
        row = conn.execute("SELECT id FROM collection WHERE id=? AND deleted=0", (int(name_or_id),)).fetchone()
    else:
        row = conn.execute("SELECT id FROM collection WHERE name=? AND deleted=0", (str(name_or_id).strip(),)).fetchone()
    if row is None:
        raise ValidateError(f"no live collection {name_or_id!r}")
    return row[0]


# ══ the scope ═════════════════════════════════════════════════════════════════════════════════════
def scope(conn, cid: int) -> dict:
    live_obs = "JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0"
    a = {r[0] for r in conn.execute(f"SELECT DISTINCT n.observation_id FROM ib_node n {live_obs} WHERE n.deleted=0 AND n.collection_id=?", (cid,))}
    verses = [r[0] for r in conn.execute(f"SELECT DISTINCT n.verse_reference FROM ib_node n {live_obs} WHERE n.deleted=0 AND n.collection_id=? "
                                         "AND n.verse_reference IS NOT NULL", (cid,))]
    b = set()
    for ch in _chunks(verses):
        b |= {r[0] for r in conn.execute(f"SELECT DISTINCT n.observation_id FROM ib_node n {live_obs} WHERE n.deleted=0 AND n.verse_reference IN ({_qm(ch)})", ch)}
    pairs = []
    for (subj,) in conn.execute("SELECT DISTINCT subject FROM collection_layer_item WHERE collection_id=? AND step='S1' AND item='word-lexical' AND deleted=0", (cid,)):
        s, _, k = subj.partition("|")
        if s and k:
            pairs.append((s, k))
    c = set()
    for s, k in pairs:
        c |= {r[0] for r in conn.execute(f"SELECT DISTINCT n.observation_id FROM ib_node n {live_obs} WHERE n.deleted=0 AND n.strong=? AND n.surface=?", (k, s))}
    pair_strongs = {k for _, k in pairs}
    orphans = conn.execute("SELECT o.id, o.strong FROM ib_observation o WHERE o.deleted=0 AND NOT EXISTS "
                           "(SELECT 1 FROM ib_node n WHERE n.observation_id=o.id AND n.deleted=0)").fetchall()
    c |= {r[0] for r in orphans if r[1] in pair_strongs}
    unplaced = [r[0] for r in orphans if r[1] not in pair_strongs]
    return {"a": a, "b": b, "c": c, "union": a | b | c, "verses": len(verses), "pairs": len(pairs), "orphans_unplaced": unplaced}


# ══ the structural tests ═════════════════════════════════════════════════════════════════════════════
def pull(conn, cfg, cid: int) -> dict:
    st = settings(cfg)
    cols = st["word_columns"]                       # [column, ...] of ib_node a word node must carry
    sc = scope(conn, cid)
    ids = sorted(sc["union"])
    obs: dict[int, dict] = {}
    for ch in _chunks(ids):
        for r in conn.execute(f"SELECT id, stage, tag, obs_text, nature FROM ib_observation WHERE deleted=0 AND id IN ({_qm(ch)})", ch):
            obs[r[0]] = {"id": r[0], "stage": r[1], "tag": r[2], "text": r[3] or "", "nature": r[4]}
    nodes = defaultdict(list)
    sel = ", ".join(cols)
    for ch in _chunks(ids):
        for r in conn.execute(f"SELECT id, observation_id, traced_observation_id, verse_lexical_id, subgroup_id, disposition_note, {sel} "
                              f"FROM ib_node WHERE deleted=0 AND observation_id IN ({_qm(ch)})", ch):
            nodes[r[1]].append(r)
    targets = {n[2] for ns in nodes.values() for n in ns if n[2] is not None}
    live = {}
    for ch in _chunks(sorted(targets)):
        for r in conn.execute(f"SELECT id, deleted FROM ib_observation WHERE id IN ({_qm(ch)})", ch):
            live[r[0]] = (r[1] == 0)
    findings = defaultdict(list)
    by_stage, by_nature, reach_in, missing_cols = Counter(), Counter(), Counter(), Counter()
    word_nodes = traced_nodes = 0
    for oid, o in obs.items():
        by_stage[o["stage"]] += 1
        by_nature[o["nature"] or "unmarked"] += 1
        if o["nature"] is None:
            findings["unmarked"].append(oid)
        ns = nodes.get(oid, [])
        if not ns:
            findings["no_node"].append(oid)
            continue
        for n in ns:
            if n[2] is not None and n[3] is None:                       # a traced node: names another observation, carries no word column
                traced_nodes += 1
                if not live.get(n[2], False):
                    findings["traced_dead"].append((oid, n[0], n[2]))
                continue
            word_nodes += 1
            vals = dict(zip(cols, n[6:]))
            miss = [c for c in cols if vals[c] is None]
            if miss:
                if n[5]:                                                # the reason a column the data cannot give stays empty is recorded
                    findings["word_missing_noted"].append((oid, n[0], tuple(miss)))
                else:
                    findings["word_missing"].append((oid, n[0], tuple(miss)))
                    missing_cols.update(miss)
            if n[4] is None:
                findings["subgroup_empty"].append((oid, n[0]))
            cc = vals.get("collection_id")
            if cc is not None and cc != cid:
                reach_in[cc] += 1
    seen = defaultdict(list)
    for oid, o in obs.items():
        key = (o["stage"], " ".join(o["text"].split()).lower())
        if key[1]:
            seen[key].append(oid)
    findings["duplicate_text"] = [v for v in seen.values() if len(v) > 1]
    return {"collection_id": cid, "scope": {k: len(sc[k]) for k in ("a", "b", "c", "union")}, "verses": sc["verses"], "pairs": sc["pairs"],
            "observations": obs, "by_stage": dict(by_stage), "by_nature": dict(by_nature), "word_nodes": word_nodes, "traced_nodes": traced_nodes,
            "missing_columns": dict(missing_cols), "findings": dict(findings), "reach_in": dict(reach_in), "orphans_unplaced": len(sc["orphans_unplaced"])}


def worksheet(conn, res: dict, name: str) -> dict:
    """The working file to read: every in-scope observation with what the structural tests found on it. The reading decides the marker and the
    actions; the sheet of actions is written apart (ValidateRecord)."""
    f = res["findings"]
    flags = defaultdict(list)
    for key in ("unmarked", "no_node"):
        for oid in f.get(key, []):
            flags[oid].append(key)
    for key in ("word_missing", "word_missing_noted", "traced_dead"):
        for t in f.get(key, []):
            flags[t[0]].append(key)
    for grp in f.get("duplicate_text", []):
        for oid in grp:
            flags[oid].append("duplicate_text")
    rows = []
    for oid, o in sorted(res["observations"].items()):
        rows.append({"id": oid, "stage": o["stage"], "tag": o["tag"], "nature": o["nature"], "flags": sorted(set(flags.get(oid, []))), "text": o["text"]})
    return {"collection": name, "scope": res["scope"], "observations": rows}


def report_lines(conn, cfg, name: str, res: dict, gates: dict | None = None, sample: int = 8) -> list[str]:
    f = res["findings"]
    L = [f"# Validation: {name}", "",
         f"- scope: a {res['scope']['a']}, b {res['scope']['b']}, c {res['scope']['c']}, union {res['scope']['union']} live observations "
         f"({res['verses']} verses, {res['pairs']} surface|strong pairs); d (meaning) by reading, not counted",
         f"- word nodes {res['word_nodes']}, traced nodes {res['traced_nodes']}",
         f"- marker: " + ", ".join(f"{k} {v}" for k, v in sorted(res["by_nature"].items())), "", "## Live observations by stored stage", ""]
    L += [f"- {k}: {v}" for k, v in sorted(res["by_stage"].items(), key=lambda kv: -kv[1])]
    L += ["", "## Structural findings", "",
          f"- not marked: {len(f.get('unmarked', []))} observations",
          f"- no live node: {len(f.get('no_node', []))} observations in scope by their own strong; {res['orphans_unplaced']} other live observations with no live node are in no collection's scope by structure (left to the reading)",
          f"- word nodes missing a required column and not explained: {len(f.get('word_missing', []))}; by column {res['missing_columns']}; explained in disposition_note: {len(f.get('word_missing_noted', []))}",
          f"- word nodes with no subgroup_id: {len(f.get('subgroup_empty', []))} (reported, not judged)",
          f"- live traced nodes pointing at a deleted observation: {len(f.get('traced_dead', []))}",
          f"- exact-text duplicate groups (same stage, same text): {len(f.get('duplicate_text', []))}",
          f"- nodes reaching into other collections: {sum(res['reach_in'].values())} nodes in {len(res['reach_in'])} collections (their observations are in scope; each node is verified traceable)"]
    for k in ("unmarked", "no_node", "word_missing", "traced_dead", "duplicate_text"):
        if f.get(k):
            L += ["", f"### sample: {k}", ""] + [f"- {x}" for x in f[k][:sample]]
    if gates:
        L += ["", "## Completeness check", ""] + [f"- {g}" for g in gates["lines"]]
    return L


# ══ the completeness check, two layers ═════════════════════════════════════════════════════════════════
def check(conn, cfg, cid: int) -> dict:
    """Evidence layer first: every in-scope observation marked, no live observation without a live node, no word node missing a required column
    without its reason, no live trace to a deleted observation, no two of one meaning (exact text here; by meaning is the reading). The inner-being
    layer is judged only when the evidence layer passes: every inner-being observation traced to evidence marked as such (or recorded
    self-evidencing), none left with no trace; traces to evidence not yet marked are pending. The deferrals addressed to the collection are listed,
    and those the scope's observations carry to other collections are counted: a finding deferred to a named collection is not a failure."""
    res = pull(conn, cfg, cid)
    f = res["findings"]
    obs = res["observations"]
    ev_fail = {"unmarked": f.get("unmarked", []), "no_node": f.get("no_node", []), "word_missing": [x[0] for x in f.get("word_missing", [])],
               "traced_dead": [x[0] for x in f.get("traced_dead", [])], "duplicate_text": [g for g in f.get("duplicate_text", [])]}
    deferred = {}
    for oid in obs:
        for r in conn.execute("SELECT c.new_value FROM ib_observation_change c WHERE c.observation_id=? AND c.column_name='deferred_to' AND c.id=("
                              "SELECT MAX(c2.id) FROM ib_observation_change c2 WHERE c2.observation_id=c.observation_id AND c2.column_name IN ('deferred_to','deferral_closed') "
                              "AND c2.new_value=c.new_value)", (oid,)):
            deferred.setdefault(oid, set()).add(r[0])
    open_ev = {k: v for k, v in ev_fail.items() if v}
    evidence_passes = not open_ev
    gaps = va.trace_gaps(conn, list(obs))
    ib_open = [o for o in gaps["no_trace"] if not deferred.get(o)]
    ib_deferred = [o for o in gaps["no_trace"] if deferred.get(o)]
    incoming = va.deferrals_to(conn, cid)
    lines = []
    for k, v in ev_fail.items():
        lines.append(f"evidence layer, {k}: {len(v)}" + ("" if not v else f" (e.g. {v[:5]})"))
    lines.append(f"evidence layer: {'PASSES' if evidence_passes else 'does not pass'}")
    if evidence_passes:
        lines.append(f"inner-being layer, no trace to evidence and not self-evidencing: {len(gaps['no_trace'])} (deferred to a named collection {len(ib_deferred)}, open {len(ib_open)}{'' if not ib_open else ': ' + str(ib_open[:8])})")
        lines.append(f"inner-being layer, traced to evidence not yet marked (pending): {len(gaps['pending'])}")
        lines.append(f"inner-being layer, live trace to a deleted observation: {len(gaps['dead_trace'])}")
        lines.append(f"inner-being layer: {'PASSES' if not ib_open and not gaps['dead_trace'] else 'does not pass'}")
    else:
        lines.append("inner-being layer: not judged (it opens only when the evidence layer passes)")
    lines.append(f"deferrals addressed to this collection, not closed: {len(incoming)}")
    for d in incoming[:20]:
        lines.append(f"  observation {d['observation']}: {d['finding']}")
    lines.append(f"observations of this scope deferred to other collections: {len(deferred)}")
    return {"collection_id": cid, "result": res, "evidence_passes": evidence_passes, "inner_being_passes": evidence_passes and not ib_open and not gaps["dead_trace"],
            "open_evidence": open_ev, "ib_open": ib_open, "ib_deferred": ib_deferred, "pending": gaps["pending"], "dead_trace": gaps["dead_trace"],
            "incoming": incoming, "deferred_out": len(deferred), "lines": lines}


# ══ the sheet of actions ═════════════════════════════════════════════════════════════════════════════
ID_PARAMS = {"oid", "old_id", "target", "to_obs", "serves", "traces", "carriers", "carried_by"}
_REF = re.compile(r"^@new(\d+)$")


def _actions(cfg) -> dict:
    allowed = settings(cfg)["actions"]
    return {name: getattr(va, name) for name in allowed}


def _signature(fn):
    """(required, optional) parameter names a sheet supplies: the function's own, without cfg, conn, run_id and who."""
    ps = [p for p in inspect.signature(fn).parameters.values() if p.name not in ("cfg", "conn", "run_id", "who")]
    return [p.name for p in ps if p.default is inspect._empty and p.kind not in (p.VAR_KEYWORD,)], [p.name for p in ps]


def _resolve(value, made: dict):
    if isinstance(value, str):
        m = _REF.match(value)
        if m:
            k = int(m.group(1))
            if k not in made:
                raise ValidateError(f"{value}: no earlier create action number {k} in this sheet")
            return made[k]
        return value
    if isinstance(value, list):
        return [_resolve(v, made) for v in value]
    return value


def record(conn, cfg, run_id: str, data: dict, keep: bool = True, who: str = "Claude") -> dict:
    """Check a sheet of actions whole and write it in one transaction. A sheet: {"collection": name, "actions": [{"action": name, <the parameters of
    that validationactions function>}]}. A create_observation action is numbered in the order of the create actions (1, 2, ...) and later actions
    name it "@new1". Any problem refuses the whole sheet; keep=False runs every action and rolls the transaction back (a preview)."""
    if not isinstance(data, dict) or not isinstance(data.get("actions"), list) or not data["actions"]:
        raise ValidateError("a sheet is an object with a collection and a list of actions")
    collection_id(conn, data.get("collection", ""))
    table = _actions(cfg)
    errors = []
    for i, a in enumerate(data["actions"], 1):
        name = a.get("action") if isinstance(a, dict) else None
        if name not in table:
            errors.append(f"action {i}: {name!r} is not an action of the validation (allowed: {sorted(table)})")
            continue
        req, allp = _signature(table[name])
        given = {k for k in a if k != "action"}
        if given - set(allp):
            errors.append(f"action {i} ({name}): unknown parameter(s) {sorted(given - set(allp))}; takes {allp}")
        if set(req) - given:
            errors.append(f"action {i} ({name}): missing parameter(s) {sorted(set(req) - given)}")
    if errors:
        raise ValidateError("; ".join(errors[:12]))
    made, counts = {}, Counter()
    conn.execute(f"SAVEPOINT {SAVEPOINT}")
    try:
        for i, a in enumerate(data["actions"], 1):
            name = a["action"]
            fn = table[name]
            params = {k: _resolve(v, made) for k, v in a.items() if k != "action"}
            kw = {}
            names = set(inspect.signature(fn).parameters)
            if "cfg" in names:
                kw["cfg"] = cfg
            kw["conn"] = conn
            kw["run_id"] = run_id
            kw["who"] = who
            try:
                out = fn(**kw, **params)
            except (orec.Refused, ValueError, sqlite3.Error) as exc:
                raise ValidateError(f"action {i} ({name}): {exc}") from exc
            counts[name] += 1
            if name == "create_observation":
                made[len(made) + 1] = out["observation"]
        if keep:
            conn.execute(f"RELEASE {SAVEPOINT}")
        else:
            conn.execute(f"ROLLBACK TO {SAVEPOINT}")
            conn.execute(f"RELEASE {SAVEPOINT}")
    except Exception:
        conn.execute(f"ROLLBACK TO {SAVEPOINT}")
        conn.execute(f"RELEASE {SAVEPOINT}")
        raise
    return {"actions": sum(counts.values()), "by_action": dict(counts), "created": list(made.values())}
