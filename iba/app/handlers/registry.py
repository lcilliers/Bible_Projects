"""Registry handlers — config-governed, with a REAL researcher-approval escalation.

The approval is durable and resumable (util.escalation):
  - a new word is created as 'proposed' and an approval escalation is raised -> the run pauses.
  - the researcher answers (python -m iba.app.escalation answer <word> yes|no), which sets
    the word's status to 'approved' or 'rejected'.
  - re-running the package resumes: a 'proposed' word is mid-approval (not a duplicate);
    an 'approved' word proceeds; a 'rejected' word stops.
"""

from __future__ import annotations

import datetime

from ..lib import escalation as esc
from .base import Ctx, Outcome, ok, fail, escalate

BUILT = ("raw-complete", "signed-off")     # a word past approval — a real duplicate


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _status_for(ctx: Ctx, set_by: str) -> str:
    for r in ctx.cfg.conn.execute(
            "SELECT status FROM cfg_status_flow WHERE entity='word' AND set_by LIKE ?",
            (f"%{set_by}%",)):
        return r["status"]
    return None


def exists(ctx: Ctx) -> Outcome:
    row = ctx.db.get("word_registry", word=ctx.word)
    if row and not row["deleted"] and row["status"] in BUILT:
        return fail("word-exists", f"{ctx.word!r} is already built (status {row['status']})")
    return ok("word is new or mid-build")


def create(ctx: Ctx) -> Outcome:
    row = ctx.db.get("word_registry", word=ctx.word)

    # already approved (a resume after a yes) or built -> proceed idempotently
    if row and row["status"] in ("approved",) + BUILT:
        ctx.word_id = row["id"]
        return ok(f"{ctx.word!r} already approved (id {row['id']}) — proceeding")

    # rejected -> stop
    if row and row["status"] == "rejected":
        return fail("word-rejected", f"{ctx.word!r} was rejected by the researcher")

    # mid-approval: is there an answer now?
    if row and row["status"] == "proposed":
        ans = esc.answered_for_word(ctx.db, ctx.word, "registry.create")
        if ans and ans["answer"] == "yes":
            ctx.db.update("word_registry", {"id": row["id"]}, status="approved")
            ctx.word_id = row["id"]
            return ok(f"approval received; {ctx.word!r} -> approved")
        if ans and ans["answer"] == "no":
            ctx.db.update("word_registry", {"id": row["id"]}, status="rejected")
            return fail("word-rejected", f"{ctx.word!r} was rejected")
        # still waiting
        return _ask_approval(ctx, row["id"])

    # brand new: create as 'proposed' and ask
    rid = ctx.db.write("word_registry", {
        "word": ctx.word, "source": ctx.params.get("Source", ""),
        "status": "proposed", "created_at": _now()})
    ctx.word_id = rid
    return _ask_approval(ctx, rid)


def _ask_approval(ctx: Ctx, word_id: int) -> Outcome:
    # the preset details that let the researcher answer: what it will cost.
    d = ctx.step.call1_meanings(ctx.word)
    seeds = [x["strongNumber"] for x in d.get("definitions", [])
             if x.get("strongNumber") and not ctx.step.is_particle(x["strongNumber"])]
    held = [s for s in seeds if ctx.db.get("strong", strongNumber=s)]
    return escalate(
        "needs-approval",
        question=f"Register the new word {ctx.word!r}?",
        preset={"word": ctx.word, "maps_to_strongs": len(seeds), "strongs": seeds,
                "already_held": held, "meanings_total": d.get("total")},
        tried="the app cannot self-approve a new registry word (researcher approval required)")
