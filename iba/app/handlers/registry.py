"""Registry handlers — config-governed, with a REAL researcher-approval escalation.

The approval is durable and resumable (util.escalation):
  - a new word is created as 'proposed' and an approval escalation is raised -> the run pauses.
  - the researcher answers (Escalation.ps1 -Action Answer -Word <word> -Decision Approve|Reject —
    Yes|No still accepted as aliases), which sets the word's status to 'approved' or 'rejected'.
  - re-running the package resumes: a 'proposed' word is mid-approval (not a duplicate);
    an 'approved' word proceeds; a 'rejected' word stops.
"""

from __future__ import annotations

import datetime

from ..lib import escalation as esc
from .base import Ctx, Outcome, ok, fail, escalate

# Fallback only — the real value is `cfg_enum` group `word_status_built` (added 2026-07-29,
# closing a completeness gap: `cfg_status_flow` exists for exactly this kind of fact, but which
# statuses count as "already built" used to live only here, in code). Kept byte-identical so
# behaviour is unchanged whether or not the cfg_enum rows have been approved yet.
_BUILT_FALLBACK = ("raw-complete", "signed-off")     # a word past approval — a real duplicate


def _built_statuses(ctx: Ctx) -> tuple[str, ...]:
    return tuple(ctx.cfg.enum("word_status_built")) or _BUILT_FALLBACK


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _status_for(ctx: Ctx, set_by: str) -> str:
    for r in ctx.cfg.conn.execute(
            "SELECT status FROM cfg_status_flow WHERE entity='word' AND set_by LIKE ?",
            (f"%{set_by}%",)):
        return r["status"]
    return None


def _find(ctx: Ctx):
    """The registry row for this word, matched CASE-INSENSITIVELY (soft-deletes excluded)."""
    rows = ctx.db.rows(
        "SELECT * FROM word_registry WHERE lower(word)=lower(?) AND deleted=0", (ctx.word,))
    return rows[0] if rows else None


def exists(ctx: Ctx) -> Outcome:
    """Say the TRUE state of the word — not one vague 'new or mid-build'. Only a fully
    BUILT word stops here; every other state routes on to create with a clear message."""
    row = _find(ctx)
    if not row:
        return ok(f"{ctx.word!r} is not in the registry — a new word")
    st = row["status"]
    if st in _built_statuses(ctx):
        return fail("word-exists", f"{row['word']!r} is already built (status {st})")
    msgs = {
        "proposed": f"{row['word']!r} is in the registry awaiting your approval — will resume its approval",
        "approved": f"{row['word']!r} is approved but its raw layer is not built — will build it",
        "rejected": f"{row['word']!r} was rejected before — will propose it again",
    }
    return ok(msgs.get(st, f"{row['word']!r} is in the registry (status {st})"))


def create(ctx: Ctx) -> Outcome:
    row = _find(ctx)

    # already approved (a resume after a yes) or built -> proceed idempotently
    if row and row["status"] in ("approved",) + _built_statuses(ctx):
        ctx.word_id = row["id"]
        return ok(f"{row['word']!r} already approved (id {row['id']}) — proceeding")

    # previously rejected, and the researcher is running new-word again -> RE-PROPOSE
    # (an explicit re-add is a reconsideration; it still needs a fresh approval).
    if row and row["status"] == "rejected":
        ctx.db.update("word_registry", {"id": row["id"]}, status="proposed")
        ctx.word_id = row["id"]
        return _ask_approval(ctx, row["id"])

    # mid-approval: is there an answer now?
    if row and row["status"] == "proposed":
        ans = esc.answered_for_word(ctx.db, ctx.word, "registry.create")
        if ans and ans["next_action"] == "approve":
            ctx.db.update("word_registry", {"id": row["id"]}, status="approved")
            ctx.word_id = row["id"]
            return ok(f"approval received; {row['word']!r} -> approved")
        if ans and ans["next_action"] == "reject":
            ctx.db.update("word_registry", {"id": row["id"]}, status="rejected")
            return fail("word-rejected", f"{row['word']!r} was rejected")
        # still waiting
        return _ask_approval(ctx, row["id"])

    # brand new: create as 'proposed' and ask
    rid = ctx.db.write("word_registry", {
        "word": ctx.word, "source": ctx.params.get("Source", ""),
        "status": "proposed", "created_at": _now()})
    ctx.word_id = rid
    return _ask_approval(ctx, rid)


def _possible_duplicates(ctx: Ctx, seeds: list[str], self_id: int) -> list[dict]:
    """Existing words that already hold these strongs — a typo/variant check. Returns
    each such word with how many of the seed strongs it shares, most-overlapping first."""
    if not seeds:
        return []
    ph = ",".join("?" * len(seeds))
    rows = ctx.db.rows(
        f"SELECT wr.word AS word, wr.status AS status, COUNT(DISTINCT ws.strong) AS shared "
        f"FROM word_strong ws JOIN word_registry wr ON wr.id = ws.word_id "
        f"WHERE ws.strong IN ({ph}) AND ws.deleted=0 AND wr.deleted=0 AND wr.id != ? "
        f"GROUP BY wr.id ORDER BY shared DESC",
        seeds + [self_id])
    return [dict(r) for r in rows]


def _ask_approval(ctx: Ctx, word_id: int) -> Outcome:
    # the preset details that let the researcher answer: what it will cost.
    d = ctx.step.call1_meanings(ctx.word)
    seeds = [x["strongNumber"] for x in d.get("definitions", [])
             if x.get("strongNumber") and not ctx.step.is_particle(x["strongNumber"])]
    held = [s for s in seeds if ctx.db.get("strong", strongNumber=s)]
    dups = _possible_duplicates(ctx, seeds, word_id)

    # if an existing word already holds >= this fraction of this word's strongs, it is a likely
    # duplicate/typo — turn the approval into an explicit confirmation. Threshold is
    # `registry.duplicate_shared_threshold` (cfg_setting, module `registry`, default 1.0 = ALL
    # strongs shared — added 2026-07-29; previously a hardcoded 100%-only check with no tunable
    # config counterpart at all).
    threshold = ctx.cfg.setting("registry.duplicate_shared_threshold", 1.0)
    question = f"Register the new word {ctx.word!r}?"
    warning = None
    if seeds and dups and dups[0]["shared"] >= threshold * len(seeds):
        other = dups[0]["word"]
        warning = (f"all {len(seeds)} strongs are already held by existing word {other!r} "
                   f"— this may be a duplicate or typo")
        question = (f"{ctx.word!r} shares ALL {len(seeds)} strongs with existing word "
                    f"{other!r}. Register it as a SEPARATE word anyway?")

    return escalate(
        "needs-approval",
        question=question,
        preset={"word": ctx.word, "maps_to_strongs": len(seeds), "strongs": seeds,
                "already_held": held, "meanings_total": d.get("total"),
                "possible_duplicates": dups, "duplicate_warning": warning},
        tried="the app cannot self-approve a new registry word (researcher approval required)")
