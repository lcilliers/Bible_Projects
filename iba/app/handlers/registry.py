"""Registry handlers — config-governed. The status values come from cfg_status_flow /
cfg_enum, not from string literals in the code."""

from __future__ import annotations

import datetime

from .base import Ctx, Outcome, ok, fail


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _status_for(ctx: Ctx, set_by: str) -> str:
    """The status a step sets, from cfg_status_flow — not a literal."""
    for r in ctx.cfg.conn.execute(
            "SELECT status FROM cfg_status_flow WHERE entity='word' AND set_by LIKE ?",
            (f"%{set_by}%",)):
        return r["status"]
    return None


def exists(ctx: Ctx) -> Outcome:
    row = ctx.db.get("word_registry", word=ctx.word)
    if row and not row["deleted"]:
        # condition 'word-exists'; the PATH (report-stop) is in cfg_on_fail
        return fail("word-exists", f"the word {ctx.word!r} already exists (id {row['id']})")
    return ok("word is new")


def create(ctx: Ctx) -> Outcome:
    # NOTE: the researcher-approval escalation (proposed -> approved) is where
    # util.escalation would pause; stubbed to approve so the slice completes.
    status = _status_for(ctx, "registry.create")        # <- from cfg_status_flow
    rid = ctx.db.write("word_registry", {
        "word": ctx.word, "source": ctx.params.get("Source", ""),
        "status": status, "created_at": _now()})
    ctx.word_id = rid
    return ok(f"registered {ctx.word!r} as id {rid}, status {status}", word_id=rid)
