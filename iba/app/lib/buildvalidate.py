"""buildvalidate.py -- the validation of a collection made part of its build (escalation #2538; plan outputs/escalation/2538-validation-in-the-build-plan-v1-20261124.md;
researcher, 2026-11-24: the validation steps are an integral part of the build, every scan is pinpointed, and no observation or node is left in the air).

What the record of a layer step does with it, for the observations a row has just written (settle_row):
  - the text of each new observation is not the text of another live observation of the collection (RW-03): refused, the other named
  - every older live observation with a node on an occurrence of the row (a stage that is not one of the build's own, layer.reading stages) is answered in fill.older, once:
        keep (with its marker), restate, merge, consume, delete_neither, defer -- each through the functions of validationactions, each answer kept as `build_answer`
  - an older observation already settled (answered here, marked by the validation, or deferred to a named collection) is not asked again
What the check does (row_problems): the same tests re-derived from the tables, so that a row stays validated only while they hold. closing_gate runs the validation's own check
(collectionvalidate.check) for the collection: the evidence layer before stage 4 opens, both layers before the last step closes.

Every lookup is by an indexed column and takes a chunk of ids (cfg_setting layer.scan); none runs once for each item, and the statements run under scanguard.budget.
"""
from __future__ import annotations

import re

from . import observationrecord as orec
from . import scanguard as sg
from . import validationactions as va

WHO = "Claude"
ACTIONS = ("keep", "restate", "merge", "consume", "delete_neither", "defer", "carry")
OLD_ITEM = "old-observation"      # the ledger item that tracks one old observation in scope, from the first step of the loop to its fate (researcher 2026-11-25: the ledger is a record of processing, kept current)
STEP_ORDER = ["S1", "1.1", "1.2", "2.1", "sweep"]     # where an old observation may be carried forward to (researcher 2026-11-25: B1 clears, complex ones carry to B2/B3, the sweep takes the rest)


class BuildValidateError(Exception):
    """A problem the record reports with the others of its file; nothing is written."""


def _qm(n: int) -> str:
    return ",".join("?" * n)


def norm(text: str) -> str:
    return " ".join((text or "").split()).lower()


def build_stages(s: dict) -> set:
    return set(s["stages"].values())


def older_on(conn, cfg, s: dict, vl_ids, layer: int = 99) -> dict:
    """{observation id: {stage, tag, nature, text, occurrences}} for the live observations that have a live node on one of `vl_ids` and a stage that is not the build's own.
    Searched by idx_ib_node_verse_lexical_id, a chunk of ids at a time. In the stage 3 steps (layer 2 and below) only those whose nature is evidence or NULL are the row's to answer
    (researcher 2026-11-24, the pull of 1.1 and 1.2: "existing observations (where nature is evidence or null)"); an older inner-being observation is answered at stage 4 (IB-05, RW-13)."""
    st = sg.settings(cfg)
    stages = sorted(build_stages(s))
    nat = " AND (o.nature IS NULL OR o.nature='evidence')" if layer <= 2 else ""
    out: dict = {}
    for ch in sg.chunks(sorted(set(vl_ids)), st):
        with sg.budget(conn, cfg, "older_on"):
            for r in conn.execute(f"SELECT o.id, o.stage, o.tag, o.nature, o.obs_text, count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id "
                                  f"WHERE n.verse_lexical_id IN ({_qm(len(ch))}) AND n.deleted=0 AND o.deleted=0 AND o.stage NOT IN ({_qm(len(stages))}){nat} GROUP BY o.id",
                                  ch + stages):
                d = out.setdefault(r[0], {"observation": r[0], "stage": r[1], "tag": r[2], "nature": r[3], "text": (r[4] or ""), "occurrences": 0})
                d["occurrences"] += r[5]
    return out


def carried_to_map(conn, ids) -> dict:
    """{observation id: the step it was last carried to}, for the observations that were carried (the latest `carried_to` of each)."""
    out = {}
    ids = sorted(set(ids))
    for i in range(0, len(ids), 400):
        ch = ids[i:i + 400]
        for r in conn.execute(f"SELECT observation_id, new_value FROM ib_observation_change WHERE observation_id IN ({_qm(len(ch))}) AND column_name='carried_to' ORDER BY id", ch):
            out[r[0]] = r[1]
    return out


def ledger_answer(conn, cid: int, gids, oid: int, step, act: str, reason: str, run_id: str, to=None) -> None:
    """The ledger records the fate of an old observation AS IT IS ANSWERED, not at the end: the row of the observation (item old-observation, subject its id) goes to `observed` with the action and the
    reason; a carry moves the row to the step it is carried to and keeps it open; an observation with no row yet gets one (the ledger shows every answer)."""
    marks = ",".join("?" * len(gids)) if gids else ""
    row = conn.execute("SELECT id, subgroup_id FROM collection_layer_item WHERE collection_id=? AND item=? AND subject=? AND deleted=0 AND state!='retired'"
                       + (f" AND subgroup_id IN ({marks})" if gids else "") + " ORDER BY id LIMIT 1", [cid, OLD_ITEM, str(oid)] + sorted(gids)).fetchone()
    txt = f"{act}" + (f" to {to}" if to else "") + f": {reason}"
    if act == "carry":
        sets, vals = "step=?, state='open', answered_at=NULL, validated=0, reason=?, observation_id=?, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=?", [to, txt, oid, run_id]
    else:
        sets, vals = "state='observed', answered_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), validated=0, reason=?, observation_id=?, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=?", [txt, oid, run_id]
    if row:
        conn.execute(f"UPDATE collection_layer_item SET {sets} WHERE id=?", vals + [row[0]])
    else:
        g = sorted(gids)[0] if gids else 0
        conn.execute("INSERT INTO collection_layer_item (collection_id, step, item, subgroup_id, subject, state, observation_id, reason, validated, run_id, created_by, answered_at) "
                     "VALUES (?,?,?,?,?,?,?,?,0,?,?,strftime('%Y-%m-%dT%H:%M:%SZ','now'))",
                     (cid, to if act == "carry" else (step or "S1"), OLD_ITEM, g, str(oid), "open" if act == "carry" else "observed", oid, txt, run_id, WHO))


def old_fate_ok(conn, oid: int, reason: str, cfg=None) -> str | None:
    """None when the recorded fate of an old observation is on the record (the answer is in the change log); else why not. LayerCheck validates an old-observation row by this."""
    act = (reason or "").split(":", 1)[0].split(" ")[0]
    if act == "settled":
        d = conn.execute("SELECT deleted FROM ib_observation WHERE id=?", (oid,)).fetchone()
        return None if (d and d[0]) or settled(conn, cfg, [oid]) else "it is recorded as settled but the change log does not show it"
    if act not in ACTIONS:
        return "its fate is not recorded"
    if act == "carry":
        return None
    if conn.execute("SELECT 1 FROM ib_observation_change WHERE observation_id=? AND column_name='build_answer' AND new_value=? LIMIT 1", (oid, act)).fetchone() is None:
        return f"the answer {act} is not in the change log of observation {oid}"
    return None


def carried_later(conn, ids, step) -> set:
    """The observations whose latest `carried_to` is a step LATER than `step`: a complex observation B1 cannot settle is carried forward to B2 or B3 (or the sweep), and until its step comes it is not asked again.
    Searched by idx_ib_observation_change_observation_id."""
    if step not in STEP_ORDER:
        return set()
    out = set()
    ids = sorted(set(ids))
    for i in range(0, len(ids), 400):
        ch = ids[i:i + 400]
        last = {}
        for r in conn.execute(f"SELECT observation_id, new_value FROM ib_observation_change WHERE observation_id IN ({_qm(len(ch))}) AND column_name='carried_to' ORDER BY id", ch):
            last[r[0]] = r[1]
        out |= {k for k, v in last.items() if v in STEP_ORDER and STEP_ORDER.index(v) > STEP_ORDER.index(step)}
    return out


def settled(conn, cfg, ids) -> set:
    """The observations of `ids` that a reading has already judged: answered in a build (`build_answer`), marked by the validation (`nature`), deferred to a named collection
    (`deferred_to`) or consumed (`consumed_by`). Searched by idx_ib_observation_change_observation_id."""
    st = sg.settings(cfg)
    out = set()
    for ch in sg.chunks(sorted(set(ids)), st):
        with sg.budget(conn, cfg, "settled"):
            out |= {r[0] for r in conn.execute(f"SELECT DISTINCT observation_id FROM ib_observation_change WHERE observation_id IN ({_qm(len(ch))}) "
                                               "AND column_name IN ('build_answer','nature','deferred_to','consumed_by')", ch)}
    return out


def unmarked_in(conn, cfg, s: dict, vl_ids) -> dict:
    """{observation id: {..., "elsewhere": n}} of the older live observations with no marker (nature NULL) that have a live node on one of `vl_ids` and are not yet judged by a reading
    (settled). They are the candidates the loop reviews for deletion. `elsewhere` counts the live nodes of the observation outside `vl_ids` (other subgroups, other collections): an
    observation with any is shown but never deleted here (sweep), because deleting it would remove it from them too; it is answered where all its holders are read."""
    older = older_on(conn, cfg, s, vl_ids)
    open_ = {k: v for k, v in older.items() if v["nature"] is None}
    done = settled(conn, cfg, list(open_))
    out = {k: v for k, v in open_.items() if k not in done}
    mine, st = set(vl_ids), sg.settings(cfg)
    for k in out:
        out[k]["elsewhere"] = 0
    for ch in sg.chunks(sorted(out), st):
        with sg.budget(conn, cfg, "unmarked_elsewhere"):
            for oid, vl in conn.execute(f"SELECT observation_id, verse_lexical_id FROM ib_node WHERE observation_id IN ({_qm(len(ch))}) AND deleted=0", ch):
                if vl not in mine:
                    out[oid]["elsewhere"] += 1
    return out


def sweep(cfg, conn, items: list, allowed: dict, run_id: str) -> list[str]:
    """The `delete_unmarked` answer of a 2.1 file: each names an observation of the pulled candidate list and the reason it is neither evidence nor inner being; each is deleted
    through validationactions.delete_neither (comment first, then deleted) and logged as a build_answer. Returns the problems; the caller refuses the file with them."""
    problems, seen = [], set()
    for i, it in enumerate(items or [], 1):
        oid, reason = it.get("observation"), (it.get("reason") or "").strip()
        where = f"delete_unmarked {i} (observation {oid})"
        if oid in seen:
            problems.append(f"{where}: named twice")
            continue
        seen.add(oid)
        if oid not in allowed:
            problems.append(f"{where}: not in the unmarked observations of this subgroup (pull again; an observation answered in fill.older or already judged is not a candidate)")
            continue
        if allowed[oid].get("elsewhere"):
            problems.append(f"{where}: it also holds {allowed[oid]['elsewhere']} node(s) outside this subgroup (other subgroups or collections); deleting it here would remove it from them (answer it where all its holders are read)")
            continue
        if len(reason) < 20:
            problems.append(f"{where}: the reason says why it is neither evidence nor inner being (20 characters or more)")
            continue
        try:
            va.delete_neither(cfg, conn, oid, reason, run_id, WHO)
        except va.Refused as exc:
            problems.append(f"{where}: {exc}")
            continue
        orec.log(conn, oid, None, "build_answer", None, "delete_neither", reason, None, run_id, WHO)
    return problems


def scope_texts(conn, cfg, cid: int) -> dict:
    """{normalised text: [live observation ids]} of the observations that hold a live node of the collection (idx_ib_node_collection, then the primary key)."""
    out: dict = {}
    with sg.budget(conn, cfg, "scope_texts"):
        for r in conn.execute("SELECT DISTINCT o.id, o.obs_text FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id AND o.deleted=0 "
                              "WHERE n.collection_id=? AND n.deleted=0", (cid,)):
            if r[1]:
                out.setdefault(norm(r[1]), []).append(r[0])
    return out


def _live(conn, cfg, ids) -> set:
    st = sg.settings(cfg)
    out = set()
    for ch in sg.chunks(sorted(set(ids)), st):
        out |= {r[0] for r in conn.execute(f"SELECT id FROM ib_observation WHERE deleted=0 AND id IN ({_qm(len(ch))})", ch)}
    return out


def row_vl_ids(conn, cfg, oids) -> set:
    st = sg.settings(cfg)
    out = set()
    for ch in sg.chunks(sorted(set(oids)), st):
        with sg.budget(conn, cfg, "row_vl_ids"):
            out |= {r[0] for r in conn.execute(f"SELECT DISTINCT verse_lexical_id FROM ib_node WHERE observation_id IN ({_qm(len(ch))}) AND deleted=0 "
                                               "AND verse_lexical_id IS NOT NULL", ch)}
    return out


def _collection_id(conn, name: str):
    r = conn.execute("SELECT id FROM collection WHERE name=? AND deleted=0", (name,)).fetchone()
    return r[0] if r else None


def note_empty_nodes(cfg, conn, oid: int, note: str | None, run_id: str) -> int:
    """A kept or restated older observation stays as it was written, so a node of it that lacks a required word column (the role of the occurrence, say) keeps the column empty; the
    reason is recorded on the node (disposition_note, validationactions.note_node) at the answer, or the evidence validation would hold the observation's subgroup at step 3.1
    (#2538, 2026-11-24). `note` (the answer's node_note) is the reason in words; without it the standard reason names the columns."""
    from . import collectionvalidate as cv
    cols = cv.settings(cfg)["word_columns"]
    n = 0
    for r in conn.execute(f"SELECT id, {', '.join(cols)} FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL AND disposition_note IS NULL", (oid,)).fetchall():
        miss = [c for c, v in zip(cols, tuple(r)[1:]) if v in (None, "")]
        if miss:
            why = (note or "").strip() or ("empty at the build: the older observation is kept as written and its data gives no " + ", ".join(miss) + " for this occurrence; it is read where the observation is traced")
            va.note_node(conn, r[0], why, run_id, WHO)
            n += 1
    return n


def _home_nodes(conn, oid: int, home):
    """(the live word nodes of the observation on the occurrences of the subgroup being worked, the ones elsewhere). home = (collection id, set of the subgroup's occurrence ids). An observation held also
    by another subgroup or collection loses only its nodes here (researcher 2026-11-25: "Deletion includes the node"); it is deleted when its last live word node goes."""
    if not home or not home[1]:
        return None, None
    vl = home[1]
    here, there = [], []
    for nid, v in conn.execute("SELECT id, verse_lexical_id FROM ib_node WHERE observation_id=? AND deleted=0 AND traced_observation_id IS NULL", (oid,)):
        (here if v in vl else there).append(nid)
    return here, there


def _answer(cfg, conn, oid: int, a: dict, new_ids: list, run_id: str, s: dict, home=None, step=None) -> None:
    act = a.get("action")
    reason = (a.get("reason") or "").strip()
    if act not in ACTIONS:
        raise va.Refused(f"older observation {oid}: action is one of {list(ACTIONS)}")
    if act in ("keep", "restate"):
        nat = a.get("nature")
        if nat not in va.natures(cfg):
            raise va.Refused(f"older observation {oid}: {act} names its marker, nature one of {va.natures(cfg)}")
        if act == "restate":
            va.restate(cfg, conn, oid, a.get("new_text") or "", a.get("checked") or "", reason, run_id, WHO)
        va.set_nature(cfg, conn, oid, nat, reason, run_id, WHO)
        note_empty_nodes(cfg, conn, oid, a.get("node_note"), run_id)
    elif act == "merge":
        into = a.get("into")
        if into in (None, oid) or into not in _live(conn, cfg, [into]):
            raise va.Refused(f"older observation {oid}: merge names a live observation to keep (into)")
        orec.merge_observation(conn, oid, into, reason, None, run_id, WHO)
    elif act == "consume":
        carriers = [x for c in (a.get("carriers") or []) for x in (new_ids if c == "this" else [c])]
        unc = a.get("uncarried")      # a JSON answer names occurrences as strings; the consumption compares occurrence ids (#2628, every path)
        if isinstance(unc, dict):
            unc = {int(k) if str(k).isdigit() else k: v for k, v in unc.items()}
        va.consume(cfg, conn, oid, carriers, a.get("mapping") or "", run_id, WHO, unc)
    elif act == "delete_neither":
        here, there = _home_nodes(conn, oid, home)
        va.delete_neither(cfg, conn, oid, reason, run_id, WHO, node_ids=here if there else None)     # its nodes here go with it; the nodes of another subgroup or collection stay with the observation
    elif act == "carry":
        to = a.get("to")
        if step not in STEP_ORDER or to not in STEP_ORDER or STEP_ORDER.index(to) <= STEP_ORDER.index(step):
            raise va.Refused(f"older observation {oid}: carry names a LATER step of {STEP_ORDER} (to) than {step}; the sweep is the last")
        if len(reason) < 10:
            raise va.Refused(f"older observation {oid}: carry gives its reason in words (what B2 or B3 is to consider)")
        orec.log(conn, oid, None, "carried_to", None, to, reason, None, run_id, WHO)
        return
    elif act == "defer":
        cid = _collection_id(conn, a.get("collection") or "")
        if cid is None:
            raise va.Refused(f"older observation {oid}: defer names a live collection (collection)")
        if a.get("nature") not in va.natures(cfg):
            raise va.Refused(f"older observation {oid}: a deferred observation is marked now (nature one of {va.natures(cfg)}); only the finding is left to the collection")
        va.set_nature(cfg, conn, oid, a["nature"], a.get("finding") or "deferred", run_id, WHO)
        va.defer(conn, oid, cid, a.get("finding") or "", run_id, WHO)
    orec.log(conn, oid, None, "build_answer", None, act, reason or (a.get("finding") or a.get("mapping") or act + " in the build"), None, run_id, WHO)


def settle_row(conn, cfg, s: dict, cid: int, new_ids: list, answers: list, run_id: str, texts: dict | None = None, layer: int = 99, step=None, home_vl=None) -> list[str]:
    """The tests of this module for the observations `new_ids` a row has just written (inside the record's savepoint). Returns the problems; the caller refuses the whole file
    with them and the savepoint is rolled back."""
    problems: list[str] = []
    texts = scope_texts(conn, cfg, cid) if texts is None else texts
    vl = row_vl_ids(conn, cfg, new_ids)
    gids = set()
    for ch in sg.chunks(sorted(set(new_ids)), sg.settings(cfg)):
        gids |= {r[0] for r in conn.execute(f"SELECT DISTINCT subgroup_id FROM ib_node WHERE observation_id IN ({_qm(len(ch))}) AND deleted=0 AND subgroup_id IS NOT NULL", ch)}
    home = (cid, set(home_vl or ()))
    older = older_on(conn, cfg, s, vl, layer)
    done = settled(conn, cfg, older) | carried_later(conn, older, step)
    given = {}
    for a in answers or []:
        if not isinstance(a, dict) or not isinstance(a.get("observation"), int):
            problems.append("fill.older is a list of {observation, action, reason, ...}")
            continue
        given[a["observation"]] = a
    for oid in sorted(set(given) - set(older)):
        problems.append(f"fill.older names observation {oid}, which is not an older live observation on the occurrences of this row")
    undone = []
    for oid in sorted(older):
        if oid in done and oid not in given:
            continue
        a = given.get(oid)
        if a is None:
            undone.append(oid)
            continue
        conn.execute("SAVEPOINT older_answer")
        try:
            _answer(cfg, conn, oid, a, new_ids, run_id, s, home, step)
            ledger_answer(conn, cid, gids, oid, step, a.get("action"), (a.get("reason") or "").strip() or (a.get("finding") or a.get("mapping") or ""), run_id, a.get("to"))
            conn.execute("RELEASE older_answer")
        except (va.Refused, orec.Refused) as exc:
            conn.execute("ROLLBACK TO older_answer")
            conn.execute("RELEASE older_answer")
            problems.append(f"older observation {oid}: {exc}")
    if undone:
        problems.append(f"{len(undone)} older live observation(s) on the occurrences of this row have no answer in fill.older (for example {undone[:8]}); answer each with one of "
                        f"{list(ACTIONS)} (RW-13)")
    for oid in new_ids:      # after the answers: an older duplicate merged into the new observation is no longer live
        t = conn.execute("SELECT obs_text FROM ib_observation WHERE id=?", (oid,)).fetchone()[0]
        clash = [x for x in texts.get(norm(t), []) if x != oid and x not in new_ids]
        clash = sorted(_live(conn, cfg, clash))
        if clash:
            problems.append(f"observation {oid}: the same text as live observation {clash[0]} of this collection (RW-03); give it a node there (an `older` merge) or word it for this finding")
    for oid in new_ids:
        texts.setdefault(norm(conn.execute("SELECT obs_text FROM ib_observation WHERE id=?", (oid,)).fetchone()[0]), []).append(oid)
    return problems


def row_problems(conn, cfg, s: dict, cid: int, oids: list, layer: int = 99, step=None) -> str | None:
    """The same tests re-derived from the tables for the live observations of one answered row (LayerCheck): a word node with a missing required column and no reason on it,
    and an older live observation on its occurrences that no reading has judged. None when they hold."""
    st = sg.settings(cfg)
    req = [c for c in s["node_required"] if layer >= s["node_required_from_layer"].get(c, 0)]      # as at creation: the subgroup only once the grouping exists
    miss = []
    for ch in sg.chunks(sorted(set(oids)), st):
        with sg.budget(conn, cfg, "row_problems"):
            for r in conn.execute(f"SELECT id, disposition_note, {', '.join(req)} FROM ib_node WHERE observation_id IN ({_qm(len(ch))}) AND deleted=0 AND traced_observation_id IS NULL", ch):
                if r[1] is None and any(v in (None, "") for v in r[2:]):
                    miss.append(r[0])
    if miss:
        return f"{len(miss)} word node(s) miss a required column with no reason on the node (for example {miss[:5]})"
    older = older_on(conn, cfg, s, row_vl_ids(conn, cfg, oids), layer)
    open_ = sorted(set(older) - settled(conn, cfg, older) - carried_later(conn, older, step))
    if open_:
        return f"{len(open_)} older live observation(s) on its occurrences have no answer (for example {open_[:5]})"
    return None


def _subgroup_obs(conn, gid: int, ids) -> set:
    """Of the observation ids, those with a live node placed in the subgroup (ib_node.subgroup_id)."""
    ids = list(ids)
    out = set()
    for i in range(0, len(ids), 400):
        ch = ids[i:i + 400]
        out |= {r[0] for r in conn.execute(f"SELECT DISTINCT observation_id FROM ib_node WHERE deleted=0 AND subgroup_id=? AND observation_id IN ({','.join('?' * len(ch))})", [gid] + ch)}
    return out


def closing_gate(conn, cfg, cid: int, layers: str = "both", gid: int | None = None) -> list[str]:
    """What the collection's validation (collectionvalidate.check) still finds: the evidence layer ('evidence') or both ('both'). Empty when it passes. With gid, only what concerns the
    observations of that subgroup (a live node placed in it): the gate of one pass of the subgroup loop (#2538)."""
    from . import collectionvalidate as cv
    mine_ids = None
    if gid is not None:      # a subgroup's gate judges the observations with a live node placed in it (idx_ib_node_subgroup), not the whole collection filtered afterwards (#2538)
        mine_ids = {r[0] for r in conn.execute("SELECT DISTINCT n.observation_id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 "
                                               "AND n.subgroup_id=?", (gid,))}
    res = cv.check(conn, cfg, cid, mine_ids)
    out = []
    ev = res["open_evidence"]
    if gid is not None:
        flat = {x for v in ev.values() for g in v for x in (g if isinstance(g, (list, tuple)) else (g,)) if isinstance(x, int)}
        mine = _subgroup_obs(conn, gid, flat)
        ev = {k: [g for g in v if any(x in mine for x in (g if isinstance(g, (list, tuple)) else (g,)))] for k, v in ev.items()}
        ev = {k: v for k, v in ev.items() if v}
    if ev:
        out += [f"evidence layer, {k}: {len(v)} (for example {list(v)[:5]})" for k, v in ev.items()]
    elif not res["evidence_passes"] and gid is not None:
        pass                                    # what is open belongs to other subgroups: this one passes
    elif layers == "both":
        if gid is None and res["ib_open"]:
            out.append(f"inner-being layer, no trace to evidence and not deferred: {len(res['ib_open'])} (for example {res['ib_open'][:5]})")
        elif gid is not None:
            mine = _subgroup_obs(conn, gid, res["ib_open"])
            if mine:
                out.append(f"inner-being layer, no trace to evidence and not deferred: {len(mine)} (for example {sorted(mine)[:5]})")
        if gid is None and res["dead_trace"]:
            out.append(f"inner-being layer, a live trace to a deleted observation: {len(res['dead_trace'])}")
    return out


def partner_gaps(conn, partners, need: str = "3.2", complete: str = "3.3", declared=()) -> list[str]:
    """The partner collections of step 3.3 that are not complete (researcher 2026-11-24: "check against the collection status ... first check then you ask me"). The status is CHECKED first: a partner
    counts when its ledger step 3.3 is closed, or its step `need` (3.2, whose inner-being observations 3.3 reads) is closed, or the researcher has declared it complete (cfg_setting layer.reading
    partner_complete, his answer recorded). Anything else is named, with the instruction to ask the researcher. `partners` are collection names."""
    from . import layerreading as lr
    out = []
    for name in sorted(set(partners)):
        row = conn.execute("SELECT id FROM collection WHERE name=? AND deleted=0 AND status='confirmed'", (name,)).fetchone()
        if row is None:
            out.append(f"{name}: not a confirmed collection")
        elif name in set(declared):
            continue
        elif not (lr.step_closed(conn, row[0], complete) or lr.step_closed(conn, row[0], need)):
            out.append(f"{name}: not shown complete (its step {need} is not closed, nor its step {complete}): ask the researcher whether it is complete and record the answer in layer.reading partner_complete")
    return out


# ══ the repairs the evidence validation makes before it judges ═══════════════════════════════════════
def complete_nodes(conn, cfg, s: dict, vls, cid: int, run_id: str) -> dict:
    """A word node of a live observation that has a node on the given occurrences (so the observation is in scope) and lacks a column the validation requires is COMPLETED from the data where the data
    give it (the surface, strong, morph and verse reference from the verse_lexical row; the collection from the surface's place in the collection, for a node on one of the given occurrences) and, for
    what the data cannot give (the role an older reading never gave the word; the collection of a node that belongs to another collection), the reason is written on the node. The observation is judged
    whole by the validation, so all its word nodes are dealt with. Every change is logged with its reason (researcher 2026-11-22: "every nodes should fill the maximum of every reference column ... and the
    node comment must be clear why not"; plan v9 principle 2). Searched by idx_ib_node_verse_lexical_id and the observation, in chunks."""
    from . import collectionvalidate as cv
    cols = cv.settings(cfg)["word_columns"]
    home = set(vls)
    done = {"nodes_completed": 0, "nodes_explained": 0}
    obs = set()
    for ch in sg.chunks(sorted(home), sg.settings(cfg)):
        with sg.budget(conn, cfg, "complete_nodes"):
            obs |= {r[0] for r in conn.execute(f"SELECT DISTINCT observation_id FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND verse_lexical_id IN ({_qm(len(ch))})", ch)}
    for ch in sg.chunks(sorted(obs), sg.settings(cfg)):
        with sg.budget(conn, cfg, "complete_nodes"):
            rows = conn.execute(f"SELECT id, observation_id, verse_lexical_id, {', '.join(cols)} FROM ib_node WHERE deleted=0 AND traced_observation_id IS NULL AND disposition_note IS NULL "
                                f"AND observation_id IN ({_qm(len(ch))})", ch).fetchall()
        for r in rows:
            d = dict(zip(["id", "observation_id", "verse_lexical_id"] + cols, tuple(r)))
            miss = [c for c in cols if d[c] in (None, "")]
            if not miss:
                continue
            src = conn.execute("SELECT vl.surface, vl.strong, vl.morph_code, v.osisId FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE vl.id=?", (d["verse_lexical_id"],)).fetchone() if d["verse_lexical_id"] else None
            fill = {}
            if src is not None:
                for c, v in (("surface", src[0]), ("strong", src[1]), ("morph_code", src[2]), ("verse_reference", src[3])):
                    if c in miss and v not in (None, ""):
                        fill[c] = v
            if "collection_id" in miss and d["verse_lexical_id"] in home:
                fill["collection_id"] = cid
            if fill:
                orec.modify_node(cfg, conn, d["id"], fill, "completed from the data by the evidence validation: " + ", ".join(sorted(fill)) + " are given by the occurrence", None, run_id, WHO)
                done["nodes_completed"] += 1
            left = [c for c in miss if c not in fill]
            if left:
                why = ("the data give no " + ", ".join(c for c in left if c != "collection_id") + " for this node: the older reading that wrote it gave the word none; it is read where the inner-being layer reaches it") if any(c != "collection_id" for c in left) else ""
                if "collection_id" in left:
                    why = (why + "; " if why else "") + "its collection is not this one: the occurrence belongs to another collection, whose validation completes it"
                va.note_node(conn, d["id"], why, run_id, WHO)
                done["nodes_explained"] += 1
    return done


def mark_builds(conn, cfg, s: dict, vls, cid: int, run_id: str) -> dict:
    """An unmarked observation of the loop's own kind (a layer observation, written under a ledger row) with a live node on the given occurrences, most often another collection's earlier build that
    predates the marker, is MARKED by the item that wrote it (cfg_setting layer.reading items.<item>.nature: the rule at creation, RW-12, never a guess from the stage) and, where it belongs to
    another collection, DEFERRED to it so that collection's own validation closes the rest (plan v9 principle 14)."""
    done = {"builds_marked": 0, "builds_deferred": 0}
    ids = set()
    for ch in sg.chunks(sorted(set(vls)), sg.settings(cfg)):
        with sg.budget(conn, cfg, "mark_builds"):
            ids |= {r[0] for r in conn.execute(f"SELECT DISTINCT o.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND o.nature IS NULL "
                                               f"AND o.stage IN ({_qm(len(build_stages(s)))}) AND n.verse_lexical_id IN ({_qm(len(ch))})", sorted(build_stages(s)) + ch)}
    for oid in sorted(ids):
        row = conn.execute("SELECT c.item, c.collection_id, c.deleted FROM ib_observation o JOIN collection_layer_item c ON o.stable_key LIKE 'layer:' || c.id || ':%' WHERE o.id=?", (oid,)).fetchone()
        if row is None:
            continue
        nat = (s["items"].get(row[0]) or {}).get("nature")
        if nat not in va.natures(cfg):
            continue
        va.set_nature(cfg, conn, oid, nat, f"marked by the item that wrote it ({row[0]}, nature {nat}): the observation predates the marker at creation (RW-12)", run_id, WHO)
        done["builds_marked"] += 1
        if row[1] is not None and row[1] != cid and conn.execute("SELECT 1 FROM collection WHERE id=? AND deleted=0", (row[1],)).fetchone():
            va.defer(conn, oid, row[1], f"an observation of this collection's own build ({row[0]}) that reaches into another collection's verses: its validation closes the rest", run_id, WHO)
            done["builds_deferred"] += 1
    return done


def answer_old(conn, cfg, s: dict, cid: int, gids, home_vl, answers: list, step, run_id: str) -> list[str]:
    """The answers of old observations given at the top of a record file (fill `older`), not inside a row: the sweep, and any step whose rows are all answered. Each names an old observation that is
    still open in the ledger for the subgroup; it is answered as in a row (_answer) and the ledger records the fate at once. Returns the problems; the caller refuses the whole file with them."""
    problems = []
    open_ = {int(r[0]) for r in conn.execute("SELECT subject FROM collection_layer_item WHERE collection_id=? AND item=? AND deleted=0 AND state='open'" + (f" AND subgroup_id IN ({','.join('?' * len(gids))})" if gids else ""),
                                              [cid, OLD_ITEM] + sorted(gids)) if str(r[0]).isdigit()}
    seen = set()
    for a in answers or []:
        oid = a.get("observation") if isinstance(a, dict) else None
        if not isinstance(oid, int) or oid in seen:
            problems.append("older is a list of {observation, action, reason, ...}, each observation once")
            continue
        seen.add(oid)
        if oid not in open_:
            problems.append(f"older observation {oid} is not an open old observation of this subgroup in the ledger (pull again)")
            continue
        conn.execute("SAVEPOINT older_top")
        try:
            _answer(cfg, conn, oid, a, [], run_id, s, (cid, set(home_vl or ())), step)
            ledger_answer(conn, cid, gids, oid, step, a.get("action"), (a.get("reason") or "").strip() or (a.get("finding") or a.get("mapping") or ""), run_id, a.get("to"))
            conn.execute("RELEASE older_top")
        except (va.Refused, orec.Refused) as exc:
            conn.execute("ROLLBACK TO older_top")
            conn.execute("RELEASE older_top")
            problems.append(f"older observation {oid}: {exc}")
    return problems
