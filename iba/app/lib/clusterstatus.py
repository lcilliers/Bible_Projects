"""clusterstatus.py — the `cluster.status` lifecycle transitions `#1697` designed but never built
(found live 2026-09-17, building Stage 2 of `#1706`'s pipeline). Escalation #1697's own closing
resolution said it plainly: *"Design-complete... Nothing built yet."* Confirmed live before writing
this: all 80 live clusters sit at ordinal 2 (`t_cluster_assignment_completed`, the one-time
backfill every cluster started at) with no code anywhere that ever advances one past it, and no
DB trigger or application hook implements `strongs_reassigned` detection at all -- despite the
researcher's own explicit instruction (#1697 v5) that it "must trigger a warning to the chat."

**Three real gaps this module closes:**

1. **The ordinal-2 -> ordinal-3 (`ready_for_subgroup_allocation`) transition.** `#1711` names
   `verse_meaning`/`verse-reading` "the pre-subgroup Layer 2 stage" -- the name itself states the
   sequencing. This module's `advance_if_verse_reading_complete` is the missing gate: a cluster
   becomes `ready_for_subgroup_allocation` once every one of its member strongs (per
   `lexicalscope.resolve_strongs`) has at least one live `ib_observation` row from the
   `verse-reading` stage. Not a judgement call -- `#1690` §2's own governing rule (a) requires
   process (b) to read "all gloss and surface values for every strong... FIRST", and `verse-reading`
   is exactly that reading, now formalized as a stage with its own record.

2. **`strongs_reassigned` detection.** `flag_if_reassigned` -- called by anything that changes
   `cluster_strong` membership -- sets `status='strongs_reassigned'` and raises a real,
   `decision_required` escalation (per #1697 v5's explicit instruction: manual control, no automatic
   resubmission) **only when the cluster has already progressed past ordinal 2** (`cfg_column.use`
   on `cluster.status`: "ordinals 1-2... no gating code needed for these" -- nothing downstream
   exists yet to invalidate while a cluster is still there, so nothing needs flagging that early).

3. **The ordinal-3 -> ordinal-4 (`ready_for_reading`) transition, added building Stage 2.**
   `require_ready_for_subgroup_allocation`/`advance_after_subgroup_allocation` -- `#1690` §3 item 5's
   hard precondition + unconditional single-step advance on `cluster.subgroup` (process b)
   completing. Distinct in kind from item 1 above: this transition doesn't wait on a completeness
   check across member strongs (allocation either just fully succeeded or didn't run at all), and
   later transitions past `ready_for_reading` are gated on `cluster_subgroup.status` rollup instead
   (`#1690` §3a) -- not this module's concern, that rollup lives with subgroup-grain code once
   reading/answer are built.
"""

from __future__ import annotations

_STATUS_ORDINAL = {
    "strong_assignment_in_progress": 1,
    "t_cluster_assignment_completed": 2,
    "ready_for_subgroup_allocation": 3,
    "ready_for_reading": 4,
    "ready_for_observations": 5,
    "ready_for_synthesis": 6,
    "completed": 7,
    "strongs_reassigned": 8,
}


def _now() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def verse_reading_completeness(conn, cluster_code: str) -> dict:
    """Every member strong of `cluster_code` (per `cluster_strong`, live) checked against
    `ib_observation` for at least one `stage='verse-reading'` row. Returns the strongs still
    missing, not just a bool -- a caller needs to know WHAT's missing to report it honestly, not
    just that something is."""
    from .lexicalscope import resolve_strongs
    member_strongs = set(resolve_strongs(conn, cluster_code=cluster_code))
    covered = {r[0] for r in conn.execute(
        "SELECT DISTINCT strong FROM ib_observation WHERE cluster_code=? AND stage='verse-reading' "
        "AND strong IS NOT NULL", (cluster_code,))}
    missing = sorted(member_strongs - covered)
    return {"cluster_code": cluster_code, "member_strong_count": len(member_strongs),
           "covered_strong_count": len(covered & member_strongs), "missing_strongs": missing,
           "complete": not missing}


def advance_if_verse_reading_complete(conn, cluster_code: str) -> dict:
    """Checks completeness; if complete AND the cluster is still at ordinal 2, advances to ordinal
    3 (`ready_for_subgroup_allocation`). Never moves a cluster backward, never touches one already
    past ordinal 2 (idempotent w.r.t. later stages) -- this function's only job is the one
    transition `#1690`/`#1711`'s own sequencing implies."""
    completeness = verse_reading_completeness(conn, cluster_code)
    row = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (cluster_code,)).fetchone()
    if row is None:
        raise ValueError(f"cluster {cluster_code!r} not found")
    current = row[0]
    if not completeness["complete"]:
        return {**completeness, "status_before": current, "status_after": current,
               "advanced": False, "reason": "verse-reading incomplete"}
    if current != "t_cluster_assignment_completed":
        return {**completeness, "status_before": current, "status_after": current,
               "advanced": False,
               "reason": f"cluster is at {current!r}, not ordinal 2 -- no transition applies"}
    conn.execute("UPDATE cluster SET status='ready_for_subgroup_allocation', status_changed_at=? "
                "WHERE cluster_code=?", (_now(), cluster_code))
    return {**completeness, "status_before": current, "status_after": "ready_for_subgroup_allocation",
           "advanced": True, "reason": "verse-reading complete for every member strong"}


def require_ready_for_subgroup_allocation(conn, cluster_code: str) -> None:
    """Hard precondition for `cluster.subgroup` (process b) -- #1690 §3 item 5: 'process (b) must
    not run at all unless cluster.status=ready_for_subgroup_allocation.' Raises ValueError (the
    handler turns this into a clean fail(), not a crash) rather than silently proceeding against a
    cluster that hasn't finished verse-reading, or has been reset to strongs_reassigned."""
    row = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (cluster_code,)).fetchone()
    if row is None:
        raise ValueError(f"cluster {cluster_code!r} not found")
    if row[0] != "ready_for_subgroup_allocation":
        raise ValueError(
            f"{cluster_code} is at status {row[0]!r}, not 'ready_for_subgroup_allocation' -- "
            f"process (b) refuses to run (#1690 §3 item 5)")


def advance_after_subgroup_allocation(conn, cluster_code: str) -> dict:
    """#1690 §3 item 5 / #1693 §0: on successful completion of process (b)'s recording-pass write,
    cluster.status advances unconditionally from ready_for_subgroup_allocation to ready_for_reading
    -- this is a single-step transition (allocation just finished, cluster-wide), not gated on any
    subgroup reaching a later state itself (that rollup gating applies to LATER transitions, past
    ready_for_reading -- #1690 §3a's own RESOLVED note)."""
    row = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (cluster_code,)).fetchone()
    if row is None:
        raise ValueError(f"cluster {cluster_code!r} not found")
    current = row[0]
    if current != "ready_for_subgroup_allocation":
        return {"cluster_code": cluster_code, "status_before": current, "status_after": current,
               "advanced": False,
               "reason": f"cluster is at {current!r}, not ready_for_subgroup_allocation -- no "
                        f"transition applies (should be unreachable if the precondition check ran)"}
    conn.execute("UPDATE cluster SET status='ready_for_reading', status_changed_at=? "
                "WHERE cluster_code=?", (_now(), cluster_code))
    return {"cluster_code": cluster_code, "status_before": current, "status_after": "ready_for_reading",
           "advanced": True, "reason": "subgroup allocation complete"}


def advance_subgroups_after_allocation(conn, cluster_code: str) -> dict:
    """The subgroup-grain analogue of `advance_after_subgroup_allocation`, missing since Stage 2
    shipped 2026-09-17 -- found live building Stage 3 (2026-09-18): `#1690` §3a's own table states
    the rule plainly ("same shape as §3 item 5's cluster-level rule, one grain down") but nothing
    ever called it, so every subgroup Stage 2 has ever written (M67's 4, confirmed live) sat at
    `allocated` indefinitely with no path to `ready_for_reading` at all. Unconditional, single-step,
    every non-FLAG subgroup for this cluster currently at `allocated` -- mirrors the cluster-level
    transition exactly (allocation either just fully succeeded or didn't run), no completeness check
    needed. Idempotent: a subgroup already past `allocated` is left untouched."""
    now = _now()
    cur = conn.execute(
        "UPDATE cluster_subgroup SET status='ready_for_reading', last_updated_date=? "
        "WHERE cluster_code=? AND status='allocated' AND delete_flagged=0", (now, cluster_code))
    return {"cluster_code": cluster_code, "advanced_count": cur.rowcount}


def require_subgroup_ready_for_reading(conn, cluster_code: str, subgroup_code: str) -> dict:
    """Hard precondition for `cluster.reading` (process c) -- #1690 §3a / checklist §2 rule 18:
    the target `cluster_subgroup.status` must be `ready_for_reading`. Returns the subgroup row
    (needed by the caller for label/core_description/anchor) rather than making the caller re-query
    it, same shape as `require_ready_for_subgroup_allocation`'s own error discipline."""
    row = conn.execute(
        "SELECT id, status, label, core_description, anchor_verse_reference FROM cluster_subgroup "
        "WHERE cluster_code=? AND subgroup_code=? AND delete_flagged=0",
        (cluster_code, subgroup_code)).fetchone()
    if row is None:
        raise ValueError(f"no live subgroup {subgroup_code!r} found for cluster {cluster_code!r}")
    if row["status"] != "ready_for_reading":
        raise ValueError(
            f"{cluster_code}/{subgroup_code} is at status {row['status']!r}, not "
            f"'ready_for_reading' -- process (c) refuses to run (#1690 §3a)")
    return dict(row)


def advance_subgroup_after_reading(conn, subgroup_id: int) -> dict:
    """#1690 §3a: on successful completion of process (c)'s recording-pass write, this subgroup's
    status advances unconditionally from `ready_for_reading` to `ready_for_answer` -- one-shot,
    same shape as the cluster-level ready_for_subgroup_allocation -> ready_for_reading transition;
    no completeness check needed (reading either just fully succeeded for this subgroup or didn't
    run)."""
    row = conn.execute(
        "SELECT cluster_code, subgroup_code, status FROM cluster_subgroup WHERE id=?",
        (subgroup_id,)).fetchone()
    if row is None:
        raise ValueError(f"cluster_subgroup id {subgroup_id!r} not found")
    current = row["status"]
    if current != "ready_for_reading":
        return {"subgroup_id": subgroup_id, "status_before": current, "status_after": current,
               "advanced": False,
               "reason": f"subgroup is at {current!r}, not ready_for_reading -- no transition "
                        f"applies (should be unreachable if the precondition check ran)"}
    conn.execute("UPDATE cluster_subgroup SET status='ready_for_answer', last_updated_date=? "
                "WHERE id=?", (_now(), subgroup_id))
    return {"subgroup_id": subgroup_id, "cluster_code": row["cluster_code"],
           "subgroup_code": row["subgroup_code"], "status_before": current,
           "status_after": "ready_for_answer", "advanced": True,
           "reason": "reading complete for this subgroup"}


def require_subgroup_ready_for_answer(conn, cluster_code: str, subgroup_code: str) -> dict:
    """Hard precondition for `cluster.answer` (process d) -- #1690 §3a / checklist §3 rule 6: the
    target `cluster_subgroup.status` must be `ready_for_answer`. Same shape as
    `require_subgroup_ready_for_reading`."""
    row = conn.execute(
        "SELECT id, status, label, core_description, anchor_verse_reference FROM cluster_subgroup "
        "WHERE cluster_code=? AND subgroup_code=? AND delete_flagged=0",
        (cluster_code, subgroup_code)).fetchone()
    if row is None:
        raise ValueError(f"no live subgroup {subgroup_code!r} found for cluster {cluster_code!r}")
    if row["status"] != "ready_for_answer":
        raise ValueError(
            f"{cluster_code}/{subgroup_code} is at status {row['status']!r}, not "
            f"'ready_for_answer' -- process (d) refuses to run (#1690 §3a)")
    return dict(row)


def advance_subgroup_after_answer(conn, subgroup_id: int) -> dict:
    """#1690 §3a: on successful completion of process (d)'s recording-pass write, this subgroup's
    status advances unconditionally from `ready_for_answer` to `answer_complete` -- one-shot, same
    shape as the reading-stage transition; no completeness check needed."""
    row = conn.execute(
        "SELECT cluster_code, subgroup_code, status FROM cluster_subgroup WHERE id=?",
        (subgroup_id,)).fetchone()
    if row is None:
        raise ValueError(f"cluster_subgroup id {subgroup_id!r} not found")
    current = row["status"]
    if current != "ready_for_answer":
        return {"subgroup_id": subgroup_id, "status_before": current, "status_after": current,
               "advanced": False,
               "reason": f"subgroup is at {current!r}, not ready_for_answer -- no transition "
                        f"applies (should be unreachable if the precondition check ran)"}
    conn.execute("UPDATE cluster_subgroup SET status='answer_complete', last_updated_date=? "
                "WHERE id=?", (_now(), subgroup_id))
    return {"subgroup_id": subgroup_id, "cluster_code": row["cluster_code"],
           "subgroup_code": row["subgroup_code"], "status_before": current,
           "status_after": "answer_complete", "advanced": True,
           "reason": "answer complete for this subgroup"}


_SUBGROUP_STATUS_ORDINAL = {
    "allocated": 1, "ready_for_reading": 2, "ready_for_answer": 3, "answer_complete": 4,
    "completed": 5, "re_read_needed": 6,
}


def recompute_cluster_status_rollup(conn, cluster_code: str) -> dict:
    """The `ready_for_reading` -> `ready_for_observations` cluster-level rollup, missing since
    Stage 4 shipped (found live 2026-09-18, researcher's own review of the data: `M67` stayed at
    `ready_for_reading` despite all 4 subgroups reaching `answer_complete`). `#1690` §3a / `cfg_
    column` (iba.cluster.status) both state the rule: cluster.status can only progress past
    ready_for_reading once EVERY live subgroup (excluding the never-progressing FLAG bucket) has
    itself reached the matching level. Deliberately scoped to ONLY this one transition -- the
    further ready_for_observations -> ready_for_synthesis step depends on Stage 5 (char-synergy),
    which is not built and not even fully designed yet (#1695/#1698 still open); building that
    transition now would be guessing at an undesigned stage's own precondition, not a root-fix of
    an already-specified rule."""
    row = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (cluster_code,)).fetchone()
    if row is None:
        raise ValueError(f"cluster {cluster_code!r} not found")
    current = row[0]
    if current != "ready_for_reading":
        return {"cluster_code": cluster_code, "status_before": current, "status_after": current,
               "advanced": False,
               "reason": f"cluster is at {current!r}, not ready_for_reading -- no transition "
                        f"applies (either not there yet, or already past it)"}
    subgroup_statuses = [r[0] for r in conn.execute(
        "SELECT status FROM cluster_subgroup WHERE cluster_code=? AND delete_flagged=0 "
        "AND status IS NOT NULL", (cluster_code,))]  # NULL status = FLAG, permanently excluded
    if not subgroup_statuses:
        return {"cluster_code": cluster_code, "status_before": current, "status_after": current,
               "advanced": False, "reason": "cluster has no live, non-FLAG subgroups yet"}
    if any(_SUBGROUP_STATUS_ORDINAL.get(s, 0) < _SUBGROUP_STATUS_ORDINAL["answer_complete"]
          for s in subgroup_statuses):
        return {"cluster_code": cluster_code, "status_before": current, "status_after": current,
               "advanced": False,
               "reason": "not every live subgroup has reached answer_complete yet"}
    conn.execute("UPDATE cluster SET status='ready_for_observations', status_changed_at=? "
                "WHERE cluster_code=?", (_now(), cluster_code))
    return {"cluster_code": cluster_code, "status_before": current,
           "status_after": "ready_for_observations", "advanced": True,
           "reason": "every live subgroup has reached answer_complete"}


def flag_if_reassigned(cfg, db, conn, cluster_code: str, reason: str) -> dict | None:
    """Call this whenever `cluster_strong` membership changes for `cluster_code`. Per #1697 v5
    (researcher, verbatim: "strongs_reassigned must trigger a warning to the chat. I do not see
    that the system can proceed with automated resetting, I want to control that process") --
    fires ONLY when the cluster has already progressed past ordinal 2 (nothing downstream exists to
    invalidate before that); sets status='strongs_reassigned' and raises a real, decision_required
    escalation naming the cluster and the reason. Returns None if no flag was needed."""
    from . import escalation as esc
    row = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (cluster_code,)).fetchone()
    if row is None:
        raise ValueError(f"cluster {cluster_code!r} not found")
    current = row[0]
    if _STATUS_ORDINAL.get(current, 0) < _STATUS_ORDINAL["ready_for_subgroup_allocation"]:
        return None  # still at/before ordinal 2 -- nothing built on this cluster's membership yet
    conn.execute("UPDATE cluster SET status='strongs_reassigned', status_changed_at=? "
                "WHERE cluster_code=?", (_now(), cluster_code))
    escalation_id = esc.raise_new(
        cfg, db,
        short_description=f"{cluster_code}: cluster_strong changed post-allocation",
        source="clusterstatus.flag_if_reassigned", etype="issue",
        comment=f"cluster_strong membership changed for {cluster_code} while it was at "
               f"{current!r} (past ready_for_subgroup_allocation) -- existing subgroup/reading/"
               f"answer work for this cluster may now rest on a stale membership list. Reason for "
               f"the change: {reason}",
        context=f"Per #1697 v5, researcher's own instruction: manual control, no automatic "
               f"resubmission of process (b). status set to 'strongs_reassigned' -- the "
               f"researcher decides the next step (re-run subgroup allocation, or determine the "
               f"change doesn't actually affect existing groupings).",
        assigned_to="Researcher", resolution_kind="decision_required", originator="Claude")
    return {"cluster_code": cluster_code, "status_before": current,
           "status_after": "strongs_reassigned", "escalation_id": escalation_id}
