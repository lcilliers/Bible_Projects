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
            title: str | None = None, **counts) -> Outcome:
    """`resolution_kind`: a handler-authored `escalate()` is a judgement point the handler cannot
    resolve, so the default is `decision_required`; a handler overrides it only with its own reason.

    `needs_followup` (#1301): True when approval alone does not finish the job and a distinct follow-up
    action follows (e.g. configmaint.propose: the write happens on the re-run with -RunId); approval
    then routes the item back to Claude instead of completing it.

    `title` (#1326): a pre-validated, title-shaped short_description (<=60 chars); `raise_()` uses it
    instead of truncating `question`, which can then be the full description."""
    o = Outcome(condition, question, counts)
    o.escalation = {"question": question, "preset": preset, "tried": tried, "type": "prompted",
                    "resolution_kind": resolution_kind, "needs_followup": needs_followup,
                    "title": title}
    return o
