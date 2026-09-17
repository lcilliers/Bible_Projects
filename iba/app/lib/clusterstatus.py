"""clusterstatus.py — the `cluster.status` lifecycle transitions `#1697` designed but never built
(found live 2026-09-17, building Stage 2 of `#1706`'s pipeline). Escalation #1697's own closing
resolution said it plainly: *"Design-complete... Nothing built yet."* Confirmed live before writing
this: all 80 live clusters sit at ordinal 2 (`t_cluster_assignment_completed`, the one-time
backfill every cluster started at) with no code anywhere that ever advances one past it, and no
DB trigger or application hook implements `strongs_reassigned` detection at all -- despite the
researcher's own explicit instruction (#1697 v5) that it "must trigger a warning to the chat."

**Two real gaps this module closes:**

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
