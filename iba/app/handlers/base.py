"""The handler contract — now config-governed.

A handler is `def name(ctx: Ctx) -> Result`.

    ctx  — the open Db, the open Cfg, the STEP session, the run, the word, the params.
           Every rule a handler applies is read from ctx.cfg (the config store), not
           decided in the handler.
    Result — a condition + a message + counts. The dispatcher looks the condition up in
             cfg_on_fail to get the PATH (ok/report-*/pause/self-heal). So a handler
             names WHAT HAPPENED; the config decides WHAT TO DO. The handler cannot set
             a path itself.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Ctx:
    db: "object"        # lib.db.Db
    cfg: "object"       # lib.cfg.Cfg
    step: "object"      # lib.stepapi.Step
    run_id: str
    word: str
    word_id: int | None
    params: dict
    step_id: str = ""


@dataclass
class Outcome:
    condition: str = "ok"       # named by the handler; resolved to a path by cfg_on_fail
    message: str = ""
    counts: dict = field(default_factory=dict)
    escalation: dict | None = None


def ok(message="", **counts) -> Outcome:
    return Outcome("ok", message, counts)


def fail(condition: str, message="", **counts) -> Outcome:
    """Name a non-ok condition. The dispatcher reads cfg_on_fail[step, condition] for
    the path — the handler does not choose report-stop vs pause vs continue."""
    return Outcome(condition, message, counts)


def escalate(condition: str, question: str, preset: dict, tried: str,
            resolution_kind: str = "decision_required", needs_followup: bool = False,
            **counts) -> Outcome:
    """`resolution_kind` (escalation #798/#799): every handler-authored `escalate()` call is, by
    construction, a genuine judgement point the handler's own logic decided it can't resolve --
    that's why it's calling this at all, not the config the handler is checking against. Default
    is `decision_required` for exactly that reason; a handler would only ever override it if it
    has its own, narrower reason to believe a given call is self_correctable instead (none do,
    as of this build -- see the design doc's SS3 review).

    `needs_followup` (found live 2026-08-31, escalation #1301): set True when approval alone does
    not finish the job -- the handler's own logic requires a distinct follow-up action after the
    researcher approves (configmaint.propose is the standing example: approving a proposal only
    records the decision, a second Claude-driven re-run with -RunId is what actually calls
    _apply()). Left False, the standard decision_required transition (approved + a resolution ->
    completed) fires immediately on approval, which is correct for a plain judgement call but wrong
    here -- it marked #1238-1256 'completed' while every one of their writes was still unapplied,
    caught only because they were independently re-verified against the live DB rather than
    trusted from the escalation's own state."""
    o = Outcome(condition, question, counts)
    o.escalation = {"question": question, "preset": preset, "tried": tried, "type": "prompted",
                    "resolution_kind": resolution_kind, "needs_followup": needs_followup}
    return o
