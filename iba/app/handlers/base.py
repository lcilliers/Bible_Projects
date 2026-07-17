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


def escalate(condition: str, question: str, preset: dict, tried: str, **counts) -> Outcome:
    o = Outcome(condition, question, counts)
    o.escalation = {"question": question, "preset": preset, "tried": tried, "type": "prompted"}
    return o
