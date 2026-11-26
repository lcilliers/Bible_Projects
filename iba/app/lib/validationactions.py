"""validationactions.py -- the actions of the validation after stage 4 of a collection (escalation #2538, plan
`outputs/escalation/2538-validation-step-plan-v9-20261122.md`).

Each action does one thing to the observation record and keeps the change with its reason in `ib_observation_change`
(RW-01); nothing is physically deleted. The caller holds the transaction and the snapshot. The actions build on
`observationrecord` (modify, delete, log, check/write) and add what it lacks:

    install_nature      the `nature` column and its cfg_enum (evidence, inner_being), once per database
    set_nature          the marker, with its reason
    defer               a finding left to a named later validation (another collection will touch the observation)
    deferrals_to        the deferrals addressed to one collection (the completeness line of its report)
    annotate            a note on any observation, live or deleted (the 26 undocumented deletions)
    complete_node       a node's role or collection, or its reason for a column the data cannot give
    restate             new wording, validated: the check against the base data is named
    add_trace           a traced node to live evidence
    create_observation  a new observation, marked, traced to its evidence or serving as the evidence of others
    create_evidence     the same for evidence that earns its place (the noise test is the caller's, stated in the reason)
    add_word_node, move_node, drop_node, drop_unrelated_node   a node added, moved, or deleted when carried or unrelated
    note_node           why a column the data cannot give stays empty
    close_deferral      the owning collection has closed a deferred finding
    mark_self_evidencing   IB-07's exemption, recorded with its reason
    trace_gaps          IB-07 over a set: no trace, pending (target not yet marked), dead trace
    release_dead_traces live traced nodes that point at a deleted observation, dropped with their reason (#2618): over a set, or all
    consume             an observation whose meaning a live observation carries: verified, traces re-pointed, then deleted
    delete_neither      an observation that is neither evidence nor inner being: comment first, then deleted
    facts_held          which word occurrences of an observation no other live observation holds

The rules these keep: B:130/B:131 (nodes, observations), principle 2 (repair first), 10 (consumption is verified), 13 (neither is
deleted), 14 (every finding acted on or deferred to a named collection) of the plan.
"""
from __future__ import annotations

from . import observationrecord as orec
from .observationrecord import Refused

NATURE_ENUM = "ib_observation.nature"
NATURES = ("evidence", "inner_being")
MIN_MAPPING = 30          # characters: a mapping or a check is stated in words, not a bare id
CHUNK = 400


def _qm(n: int) -> str:
    return ",".join("?" * n)


def _chunks(seq, n=CHUNK):
    seq = list(seq)
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def _obs(conn, oid: int, live: bool = True):
    o = conn.execute("SELECT * FROM ib_observation WHERE id=?", (oid,)).fetchone()
    if o is None or (live and o["deleted"]):
        raise Refused(f"observation {oid} is not a {'live ' if live else ''}observation")
    return o


def _has_nature(conn) -> bool:
    return any(r[1] == "nature" for r in conn.execute("PRAGMA table_info(ib_observation)"))


def natures(cfg) -> list[str]:
    vals = cfg.enum(NATURE_ENUM)
    if not vals:
        raise Refused(f"cfg_enum {NATURE_ENUM} is empty: run install_nature on this database first")
    return list(vals)


# ══ the marker ═══════════════════════════════════════════════════════════════════════════════════
def install_nature(conn) -> bool:
    """The `nature` column on ib_observation and its enum, once. Returns True when something was added. Run on a copy first
    (tested), and on the live database only at promotion, under a named snapshot."""
    added = False
    if not _has_nature(conn):
        conn.execute("ALTER TABLE ib_observation ADD COLUMN nature TEXT")
        added = True
    have = {r[0] for r in conn.execute("SELECT value FROM cfg_enum WHERE name=?", (NATURE_ENUM,))}
    for i, v in enumerate(NATURES, 1):
        if v not in have:
            conn.execute("INSERT INTO cfg_enum (name, value, ordinal, inactive) VALUES (?,?,?,0)", (NATURE_ENUM, v, i))
            added = True
    return added


def set_nature(cfg, conn, oid: int, nature: str | None, reason: str, run_id: str, who: str) -> bool:
    """The marker of a live observation. `nature` None clears it (a marker given on a reading that later proves wrong). Returns
    False when it was already so."""
    o = _obs(conn, oid)
    if nature is not None and nature not in natures(cfg):
        raise Refused(f"nature must be one of {natures(cfg)}")
    if o["nature"] == nature:
        return False
    orec.log(conn, oid, None, "nature", o["nature"], nature, reason, None, run_id, who)
    conn.execute("UPDATE ib_observation SET nature=?, updated_at=? WHERE id=?", (nature, orec._now(), oid))
    return True


# ══ deferral to a named later validation (principle 14) ══════════════════════════════════════════════
def defer(conn, oid: int, collection_id: int, finding: str, run_id: str, who: str) -> None:
    """A finding the owning collection's validation will close: the observation stays as it is, with the collection and the
    finding recorded (column `deferred_to`). A finding with no named collection is never deferred."""
    _obs(conn, oid)
    if not conn.execute("SELECT 1 FROM collection WHERE id=? AND deleted=0", (collection_id,)).fetchone():
        raise Refused(f"a deferral names a live collection; {collection_id} is not one")
    if len((finding or "").strip()) < MIN_MAPPING:
        raise Refused(f"deferral of {oid}: state the finding the collection is to close, in words ({MIN_MAPPING} characters or more)")
    orec.log(conn, oid, None, "deferred_to", None, collection_id, finding, None, run_id, who)


def close_deferral(conn, oid: int, collection_id: int, reason: str, run_id: str, who: str) -> None:
    """The owning collection's validation has closed the finding deferred to it (column `deferral_closed`)."""
    orec.log(conn, oid, None, "deferral_closed", None, collection_id, reason, None, run_id, who)


def deferrals_to(conn, collection_id: int) -> list[dict]:
    """The live observations with a deferral to this collection not yet closed (the latest row of the pair decides): the line its
    completeness report lists. An observation may be deferred to several collections, each its own row."""
    rows = conn.execute(
        "SELECT c.observation_id, c.reason, c.created_at, c.column_name FROM ib_observation_change c "
        "JOIN ib_observation o ON o.id=c.observation_id AND o.deleted=0 "
        "WHERE c.column_name IN ('deferred_to','deferral_closed') AND c.new_value=? AND c.id=(SELECT MAX(c2.id) FROM ib_observation_change c2 "
        "WHERE c2.observation_id=c.observation_id AND c2.column_name IN ('deferred_to','deferral_closed') AND c2.new_value=c.new_value)",
        (str(collection_id),)).fetchall()
    return [{"observation": r[0], "finding": r[1], "since": r[2]} for r in rows if r[3] == "deferred_to"]


def annotate(conn, oid: int, note: str, run_id: str, who: str) -> bool:
    """A note (revisit_note) on any observation, live or deleted: the one function that reaches a deleted observation (the 26 whose
    delete reason was never recorded). The old note is kept in the change record."""
    o = _obs(conn, oid, live=False)
    if (o["revisit_note"] or "") == note:
        return False
    orec.log(conn, oid, None, "revisit_note", o["revisit_note"], note, note, None, run_id, who)
    conn.execute("UPDATE ib_observation SET revisit_note=?, updated_at=? WHERE id=?", (note, orec._now(), oid))
    return True


# ══ nodes ════════════════════════════════════════════════════════════════════════════════════════
def complete_node(cfg, conn, node_id: int, role: str | None, collection_id: int | None, reason: str, run_id: str, who: str) -> list[str]:
    """Complete a word node: its role (a role of reading.node_roles) and its collection (the one its surface belongs to, B:130).
    A collection is accepted only when the surface of the node is a member of it. Returns the columns changed."""
    n = conn.execute("SELECT * FROM ib_node WHERE id=? AND deleted=0", (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} is not a live node")
    changed = []
    if role is not None and n["role"] != role:
        changed += orec.modify_node(cfg, conn, node_id, {"role": role}, reason, None, run_id, who)
    if collection_id is not None and n["collection_id"] != collection_id:
        own = orec.surface_collection_map(conn).get((n["surface"] or "").strip().lower())
        if own != collection_id:
            raise Refused(f"node {node_id}: the surface {n['surface']!r} belongs to collection {own}, not {collection_id}")
        orec.log(conn, n["observation_id"], node_id, "collection_id", n["collection_id"], collection_id, reason, None, run_id, who)
        conn.execute("UPDATE ib_node SET collection_id=? WHERE id=?", (collection_id, node_id))
        changed.append("collection_id")
    return changed


# ══ wording ══════════════════════════════════════════════════════════════════════════════════════
def restate(cfg, conn, oid: int, new_text: str, checked: str, reason: str, run_id: str, who: str, **more) -> list[str]:
    """New wording for a live observation. A restatement that changes the meaning is validated against the base data
    (principle 2): `checked` names that check in words (the verse, the positions, the code), and is kept with the change."""
    if len((checked or "").strip()) < MIN_MAPPING:
        raise Refused(f"restate {oid}: say in words what was checked against the base data ({MIN_MAPPING} characters or more)")
    return orec.modify_observation(cfg, conn, oid, {"obs_text": new_text, **more}, f"{reason} | checked: {checked.strip()}",
                                   None, run_id, who)


# ══ traces ═══════════════════════════════════════════════════════════════════════════════════════
def _live_traces(conn, oid: int) -> list[int]:
    return [r[0] for r in conn.execute("SELECT traced_observation_id FROM ib_node WHERE observation_id=? AND deleted=0 "
                                       "AND traced_observation_id IS NOT NULL ORDER BY seq", (oid,))]


def _insert_trace(conn, oid: int, target: int, source_stage: str) -> int:
    seq = conn.execute("SELECT COALESCE(MAX(seq), 0) + 1 FROM ib_node WHERE observation_id=?", (oid,)).fetchone()[0]
    return conn.execute("INSERT INTO ib_node (observation_id, traced_observation_id, source_stage, seq, created_at) VALUES (?,?,?,?,?)",
                        (oid, target, source_stage, seq, orec._now())).lastrowid


def add_trace(conn, oid: int, target: int, reason: str, run_id: str, who: str, moved: bool = False) -> int | None:
    """A traced node from `oid` to the live evidence observation `target` (IB-07). Returns the node id, or None when the trace
    is already there. A trace never points at a deleted observation, at itself, or (unless `moved`: a trace the observation
    already held elsewhere, carried over by a consumption) at an observation not marked evidence."""
    o, t = _obs(conn, oid), _obs(conn, target)
    if oid == target:
        raise Refused("an observation does not trace itself")
    if not moved and _has_nature(conn) and t["nature"] != "evidence":
        raise Refused(f"observation {target} is not marked evidence: an inner-being observation traces to evidence (IB-07)")
    if target in _live_traces(conn, oid):
        return None
    nid = _insert_trace(conn, oid, target, o["stage"])
    orec.log(conn, oid, nid, "traced_observation_id", None, target, reason, None, run_id, who)
    return nid


def create_observation(cfg, conn, spec: dict, nature: str, reason: str, run_id: str, who: str, serves: list[int] = (),
                       traces: list[int] = ()) -> dict:
    """A new observation (a finding spec of observationrecord: kind, text, basis, parts, nodes), marked `nature`. Each observation
    in `serves` traces to it (it is their evidence); it traces to each observation in `traces` (it is inner being on that evidence).
    The reason says what it states that no existing observation and no node states (the noise test of the plan). Refused when the
    spec does not pass observationrecord.check, and when a trace's target is not marked evidence."""
    if len((reason or "").strip()) < MIN_MAPPING:
        raise Refused(f"create_observation: say what it states that the existing record does not ({MIN_MAPPING} characters or more)")
    if nature not in natures(cfg):
        raise Refused(f"nature must be one of {natures(cfg)}")
    errors, quotes = [], []
    plan = orec.check(cfg, [("create_observation", dict(spec, key="e1"))], errors, quotes)
    if errors or quotes:
        raise Refused("; ".join(errors + quotes))
    out = orec.write(conn, plan, None, run_id, stage="reading")["e1"]
    oid = out["observation"]
    orec.log(conn, oid, None, "created", None, oid, reason, None, run_id, who)
    set_nature(cfg, conn, oid, nature, f"created by the validation: {reason}", run_id, who)
    for s in serves:
        add_trace(conn, s, oid, f"the evidence for observation {s}: {reason}", run_id, who)
    for t in traces:
        add_trace(conn, oid, t, f"the evidence for the new observation: {reason}", run_id, who)
    return out


def create_evidence(cfg, conn, spec: dict, serves: list[int], reason: str, run_id: str, who: str) -> dict:
    """A new evidence observation, with each observation in `serves` tracing to it (create_observation)."""
    return create_observation(cfg, conn, spec, "evidence", reason, run_id, who, serves=serves)


def add_word_node(cfg, conn, oid: int, occurrence: int, strong: str, role: str, reason: str, run_id: str, who: str) -> int | None:
    """A word node on an existing live observation, resolved by observationrecord.check (collection by the surface, B:130).
    Returns the node id, or None when the observation already holds that occurrence with that role."""
    _obs(conn, oid)
    errors, quotes = [], []
    plan = orec.check(cfg, [("add_word_node", {"key": "n", "existing": oid,
                                                 "nodes": [{"occurrence": occurrence, "strong": strong, "role": role}]})], errors, quotes)
    if errors or quotes:
        raise Refused("; ".join(errors + quotes))
    out = orec.write(conn, plan, None, run_id)["n"]
    if not out["nodes"]:
        return None
    orec.log(conn, oid, out["nodes"][0], "created", None, out["nodes"][0], reason, None, run_id, who)
    return out["nodes"][0]


def move_node(cfg, conn, node_id: int, to_obs: int, reason: str, run_id: str, who: str) -> list[str]:
    """A node moves to another live observation (modify_node); refused when `to_obs` already holds that occurrence."""
    n = conn.execute("SELECT observation_id, verse_lexical_id FROM ib_node WHERE id=? AND deleted=0", (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} is not a live node")
    _obs(conn, to_obs)
    if n["verse_lexical_id"] is not None and conn.execute(
            "SELECT 1 FROM ib_node WHERE observation_id=? AND verse_lexical_id=? AND deleted=0", (to_obs, n["verse_lexical_id"])).fetchone():
        raise Refused(f"node {node_id}: observation {to_obs} already holds that occurrence: drop the node instead")
    return orec.modify_node(cfg, conn, node_id, {"observation_id": to_obs}, reason, None, run_id, who)


def drop_node(conn, node_id: int, carried_by: list[int], reason: str, run_id: str, who: str) -> bool:
    """A word node is deleted because its occurrence is held by a live node of an observation in `carried_by` (principle 2: a node is
    deleted only when another node gives the observation its context). Refused when no carrier holds it."""
    n = conn.execute("SELECT observation_id, verse_lexical_id FROM ib_node WHERE id=? AND deleted=0", (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} is not a live node")
    if n["verse_lexical_id"] is None or n["verse_lexical_id"] not in _held_by(conn, [n["verse_lexical_id"]], list(carried_by)):
        raise Refused(f"node {node_id}: its occurrence is on no live node of {list(carried_by)}")
    return orec.delete_node(conn, node_id, f"carried by observation(s) {list(carried_by)}: {reason}", None, run_id, who)


def mark_self_evidencing(conn, oid: int, reason: str, run_id: str, who: str) -> None:
    """IB-07's exemption, recorded: the observation quotes its verse in full and holds a word node for every word it relies on, so
    its evidence is the verse itself (column `self_evidencing`, with the reason)."""
    _obs(conn, oid)
    if len((reason or "").strip()) < MIN_MAPPING:
        raise Refused(f"self-evidencing {oid}: say in words which words it relies on and that each has its node")
    orec.log(conn, oid, None, "self_evidencing", None, 1, reason, None, run_id, who)


def trace_gaps(conn, ids: list[int]) -> dict:
    """IB-07 over `ids`: `no_trace` are inner-being observations with no live trace at all and not recorded self-evidencing; `pending`
    are those whose live traces point at observations not yet marked (the marking of the target's own scope is still to come, so
    they are not failed); `dead_trace` are live traced nodes that point at a deleted observation. Three statements for each chunk of ids,
    searched by the primary key and by the observation_id indexes, never one for each observation."""
    gaps, pending, dead = [], [], []
    for ch in _chunks(sorted(set(ids))):
        info = {r[0]: (r[1], r[2]) for r in conn.execute(f"SELECT id, nature, deleted FROM ib_observation WHERE id IN ({_qm(len(ch))})", ch)}
        traces: dict = {}
        for r in conn.execute(f"SELECT n.observation_id, t.id, t.deleted, t.nature FROM ib_node n JOIN ib_observation t ON t.id=n.traced_observation_id "
                              f"WHERE n.observation_id IN ({_qm(len(ch))}) AND n.deleted=0", ch):
            traces.setdefault(r[0], []).append(r[1:])
        own = {r[0] for r in conn.execute(f"SELECT DISTINCT observation_id FROM ib_observation_change WHERE observation_id IN ({_qm(len(ch))}) "
                                          "AND column_name='self_evidencing'", ch)}
        for oid in ch:
            o = info.get(oid)
            if o is None or o[1]:
                continue
            tr = traces.get(oid, [])
            dead += [(oid, r[0]) for r in tr if r[1]]
            if o[0] == "inner_being":
                ok = any((not r[1]) and r[2] == "evidence" for r in tr)
                if not ok and oid not in own:
                    if any((not r[1]) and r[2] is None for r in tr):
                        pending.append(oid)
                    else:
                        gaps.append(oid)
    return {"no_trace": gaps, "pending": pending, "dead_trace": dead}


def release_dead_traces(conn, run_id: str, who: str, ids: list[int] | None = None, check: bool = False) -> dict:
    """Live traced nodes of live observations that point at a deleted observation (#2618). Since observationrecord.soft_delete_observation
    releases the traces of what it deletes, a dead trace is one left from before that, or from a path that deleted without it. A trace to a
    deleted observation supports nothing; it is deleted, logged on its holder with the deleted target named. Over the observations in `ids`
    (searched by observation_id), or every live observation when `ids` is None (the database-wide repair, Collection-Build -Action
    ReleaseDeadTraces). `check` counts and writes nothing. Returns {nodes, observations, by_nature, sample}."""
    rows = []
    sql = ("SELECT n.id, n.observation_id, n.traced_observation_id, o.nature FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
           "JOIN ib_observation t ON t.id=n.traced_observation_id WHERE n.deleted=0 AND o.deleted=0 AND t.deleted=1")
    if ids is None:
        rows = conn.execute(sql).fetchall()
    else:
        for ch in _chunks(sorted(set(ids))):
            rows += conn.execute(sql + f" AND n.observation_id IN ({_qm(len(ch))})", ch).fetchall()
    by_nature: dict = {}
    for r in rows:
        by_nature[r[3] or "unmarked"] = by_nature.get(r[3] or "unmarked", 0) + 1
        if not check:
            why = conn.execute("SELECT reason FROM ib_observation_change WHERE observation_id=? AND column_name='deleted' AND node_id IS NULL "
                               "ORDER BY id DESC LIMIT 1", (r[2],)).fetchone()
            orec.delete_node(conn, r[0], f"traced observation {r[2]} is deleted ({(why[0] if why else 'no reason recorded')[:200]}): "
                                         "the trace supports nothing and is dropped (#2618)", None, run_id, who)
    return {"nodes": len(rows), "observations": len({r[1] for r in rows}), "by_nature": by_nature, "sample": [(r[1], r[2]) for r in rows[:5]]}


def drop_unrelated_node(conn, node_id: int, reason: str, run_id: str, who: str) -> bool:
    """A word node is deleted because it cannot support any finding of its observation (principle 2: cannot be referenced), and the
    observation keeps at least one other live word node that gives it its context. The reason says why the word is unrelated."""
    n = conn.execute("SELECT observation_id, verse_lexical_id FROM ib_node WHERE id=? AND deleted=0", (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} is not a live node")
    if len((reason or "").strip()) < MIN_MAPPING:
        raise Refused(f"node {node_id}: say in words why the word supports no finding of the observation ({MIN_MAPPING} characters or more)")
    left = conn.execute("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0 AND id<>? AND verse_lexical_id IS NOT NULL",
                        (n["observation_id"], node_id)).fetchone()[0]
    if not left:
        raise Refused(f"node {node_id} is the last word node of observation {n['observation_id']}: it is not deleted")
    return orec.delete_node(conn, node_id, reason.strip(), None, run_id, who)


def note_node(conn, node_id: int, note: str, run_id: str, who: str) -> bool:
    """The reason a column the data cannot give stays empty (cfg_column use: disposition_note); the change is kept."""
    n = conn.execute("SELECT observation_id, disposition_note FROM ib_node WHERE id=? AND deleted=0", (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} is not a live node")
    if (n["disposition_note"] or "") == note:
        return False
    orec.log(conn, n["observation_id"], node_id, "disposition_note", n["disposition_note"], note, note, None, run_id, who)
    conn.execute("UPDATE ib_node SET disposition_note=? WHERE id=?", (note, node_id))
    return True


# ══ coverage and consumption ═════════════════════════════════════════════════════════════════════
def _occurrences(conn, oid: int) -> dict[int, tuple]:
    return {r[0]: (r[1], r[2], r[3]) for r in conn.execute(
        "SELECT verse_lexical_id, verse_reference, surface, strong FROM ib_node WHERE observation_id=? AND deleted=0 "
        "AND verse_lexical_id IS NOT NULL", (oid,))}


def _held_by(conn, occ_ids, among: list[int] | None) -> set[int]:
    """The occurrences among `occ_ids` held by a live node of a live observation (of `among`, or of any other)."""
    held = set()
    for ch in _chunks(occ_ids):
        sql = ("SELECT DISTINCT n.verse_lexical_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 "
               f"WHERE n.deleted=0 AND n.verse_lexical_id IN ({_qm(len(ch))})")
        args = list(ch)
        if among is not None:
            sql += f" AND n.observation_id IN ({_qm(len(among))})"
            args += among
        held |= {r[0] for r in conn.execute(sql, args)}
    return held


def facts_held(conn, oid: int) -> dict:
    """Which word occurrences of an observation are held by a live node of another live observation: {"nodes", "uncovered":
    [(occurrence, verse, surface, strong)]}. The uncovered are what deleting it would take out of the record."""
    occ = _occurrences(conn, oid)
    other = {i: v for i, v in occ.items()}
    held = set()
    for ch in _chunks(list(other)):
        held |= {r[0] for r in conn.execute(
            "SELECT DISTINCT n.verse_lexical_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 "
            f"WHERE n.deleted=0 AND n.observation_id<>? AND n.verse_lexical_id IN ({_qm(len(ch))})", [oid] + ch)}
    return {"nodes": len(occ), "uncovered": [(i,) + occ[i] for i in occ if i not in held]}


def consume(cfg, conn, old_id: int, carriers: list[int], mapping: str, run_id: str, who: str, uncarried: dict | None = None) -> dict:
    """The meaning of `old_id` is carried by the live observations `carriers` (principle 10). Verified before anything changes:
    every carrier is live; every word occurrence of the old observation is on a live node of a carrier, or is named in
    `uncarried` {occurrence: why it is not carried}; the mapping is stated in words (what the old says, which carrier states each
    part). Then: a node that traces the old observation is re-pointed to the first carrier (or, on a carrier itself, deleted once
    the carrier holds the old observation's own sources); the consumption is kept (`consumed_by`); the old observation is deleted."""
    uncarried = uncarried or {}
    old = _obs(conn, old_id)
    carriers = list(dict.fromkeys(carriers))
    if not carriers or old_id in carriers:
        raise Refused(f"consume {old_id}: name the carrying observations (other than itself)")
    for c in carriers:
        _obs(conn, c)
    if len((mapping or "").strip()) < MIN_MAPPING:
        raise Refused(f"consume {old_id}: the mapping is stated in words ({MIN_MAPPING} characters or more)")
    occ = _occurrences(conn, old_id)
    carried = _held_by(conn, list(occ), carriers)
    missing = [i for i in occ if i not in carried and i not in uncarried]
    if missing:
        raise Refused(f"consume {old_id}: {len(missing)} occurrence(s) are on no node of {carriers} and not named as uncarried: "
                      f"{[(i,) + occ[i] for i in missing[:5]]}")
    for i, why in uncarried.items():
        if len((why or "").strip()) < 10:
            raise Refused(f"consume {old_id}: the occurrence {i} not carried needs its reason")
    old_sources = [t for t in _live_traces(conn, old_id) if t not in carriers and t != old_id]
    moved = dropped = 0
    for nid, holder in conn.execute("SELECT id, observation_id FROM ib_node WHERE traced_observation_id=? AND deleted=0", (old_id,)).fetchall():
        if holder in carriers:
            for t in old_sources:
                if t not in _live_traces(conn, holder) and t != holder:
                    add_trace(conn, holder, t, f"the sources of observation {old_id}, consumed into {holder}", run_id, who, moved=True)
            orec.delete_node(conn, nid, f"the trace to observation {old_id} is replaced: it is consumed into {holder}, which holds its sources",
                             None, run_id, who)
            dropped += 1
        else:
            orec.log(conn, holder, nid, "traced_observation_id", old_id, carriers[0],
                     f"observation {old_id} is consumed into {carriers[0]}: {mapping.strip()}", None, run_id, who)
            conn.execute("UPDATE ib_node SET traced_observation_id=? WHERE id=?", (carriers[0], nid))
            moved += 1
    orec.log(conn, old_id, None, "consumed_by", None, ",".join(map(str, carriers)),
             mapping.strip() + (f" | not carried: {uncarried}" if uncarried else ""), None, run_id, who)
    orec.soft_delete_observation(conn, old_id, f"consumed by {carriers}: {mapping.strip()}", None, run_id, who)
    return {"carriers": carriers, "occurrences": len(occ), "traces_moved": moved, "traces_dropped": dropped}


def delete_neither(cfg, conn, oid: int, reason: str, run_id: str, who: str, node_ids=None) -> dict:
    """An observation that is neither evidence nor inner being (principle 13): comment first (the reason, with the occurrences
    no other live observation holds), then deleted. Refused for an observation already marked evidence or inner being, and for one
    another observation traces (that trace is repaired first)."""
    o = _obs(conn, oid)
    if _has_nature(conn) and o["nature"] in NATURES:
        raise Refused(f"observation {oid} is marked {o['nature']}: only an observation that is neither is deleted here")
    held = conn.execute("SELECT observation_id FROM ib_node WHERE traced_observation_id=? AND deleted=0", (oid,)).fetchall()
    if held:
        raise Refused(f"observation {oid} is traced by {sorted({r[0] for r in held})}: repair those traces first")
    fh = facts_held(conn, oid)
    note = (f"Neither evidence nor inner being: {reason.strip()} Word occurrences not held by another live observation: "
            f"{len(fh['uncovered'])} of {fh['nodes']}.")
    annotate(conn, oid, note, run_id, who)
    # deleting an observation deletes its nodes (researcher 2026-11-25: "Deletion includes the node"); with node_ids only those nodes go (the nodes of this subgroup), and the observation goes when no
    # live word node is left of it
    live = [r[0] for r in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (oid,))]
    gone = set(live) if node_ids is None else (set(node_ids) & set(live))
    for nid in sorted(gone):
        orec.delete_node(conn, nid, note, None, run_id, who)
    left = conn.execute("SELECT count(*) FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL", (oid,)).fetchone()[0]
    if left == 0:
        for (nid,) in conn.execute("SELECT id FROM ib_node WHERE observation_id=? AND deleted=0", (oid,)).fetchall():
            orec.delete_node(conn, nid, note, None, run_id, who)
        orec.soft_delete_observation(conn, oid, note, None, run_id, who)
    return fh
