"""The handler contract.

A handler is `def name(ctx: Ctx) -> Result`.

    ctx   — what it is given: the open Db, the run, the word/scope, the params, the
            config version. (Researcher: "what the handler is given ... I guess it is
            a word" — here it is the word plus the run context it sits in.)
    Result — what it returns: an on_fail PATH (or "ok"), a message, and counts.
             The path decides the run's next move (base.py maps them):
               ok               -> next step
               report-continue  -> log, next step
               self-heal        -> the named resolver runs, then continue
               pause-continue   -> raise an escalation, pause the run, stop
               report-stop      -> stop, failed

This is the whole contract. It is small on purpose: the run does not need to know
what a handler does, only which path it returned.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Ctx:
    db: "object"            # lib.db.Db — open, committed by the dispatcher after each step
    run_id: str
    word: str
    word_id: int | None
    params: dict
    step_version: str
    step: str = ""


@dataclass
class Result:
    path: str = "ok"        # ok | report-continue | pause-continue | report-stop | self-heal
    message: str = ""
    counts: dict = field(default_factory=dict)
    # for pause-continue:
    escalation: dict | None = None
    # for self-heal:
    resolver: str | None = None


def ok(message="", **counts) -> Result:
    return Result("ok", message, counts)


def stop(message) -> Result:
    return Result("report-stop", message)


def cont(message="", **counts) -> Result:
    return Result("report-continue", message, counts)


def pause(question, preset, tried, at_step) -> Result:
    return Result("pause-continue", question,
                  escalation={"question": question, "preset": preset, "tried": tried,
                              "at_step": at_step, "type": "prompted"})
