"""run.py — the dispatcher and run-state machine. Config-governed.

The step's handler, its scope, the sequence order — all read from the config store
(cfg_step). The handler returns a CONDITION; this dispatcher looks it up in cfg_on_fail
to get the PATH. The code decides nothing: config maps condition -> path.

    python -m iba.app.run <work_package> --step <id> --run-id <id> --param Name=Value

Exit codes let PowerShell branch: 0 ok/continue · 2 paused · 3 stop.
"""

from __future__ import annotations

import argparse
import datetime
import importlib
import json
import sys

from .lib.cfg import Cfg
from .lib.db import Db
from .lib.stepapi import Step
from .lib.words import normalise
from .lib import dbsnapshot
from .lib.escalation import word_source, raise_ as esc_raise
from .handlers.base import Ctx, Outcome

# path -> what the run does + the process exit code ("error": see main())
PATH_EXIT = {"ok": 0, "report-continue": 0, "self-heal": 0, "pause-continue": 2, "report-stop": 3,
            "error": 1}


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve(handler: str):
    mod, fn = handler.split(":")
    return getattr(importlib.import_module(mod), fn)


def _grant(cfg: Cfg, table: str):
    """The dispatcher writes control tables under the 'run' write grant — config-governed."""
    if table not in cfg.may_write("run"):
        raise PermissionError(f"write-grant violation: 'run' may not write {table!r} (cfg_write_grant)")


# This dispatcher writes the `escalation` table directly (three sites below), not via
# lib/escalation.py, so it carries the same required columns.
def _source_for_step(step_id: str) -> str:
    """cfg_escalation.source_classification: a code-generated row's source is the generating
    module name."""
    return step_id.split(".", 1)[0] if "." in step_id else "code"


def _escalation_type_for(step_id: str, word: str) -> str:
    """The source classification also used to backfill historical rows; kept in step with it."""
    if step_id.startswith("configmaint.propose"):
        return "config"
    if step_id.endswith(".validate"):
        return "issue"
    if word:
        return "task"
    if step_id in ("candidate.curate", "candidate.load"):
        return "issue"
    return "issue"


def _snapshot(db: Db, cfg: Cfg, run_id: str, word: str, phase: str):
    """Record a row-count of every data table as the run's pre/post baseline. Written
    under the 'run' grant into validation_result; delta = post - pre = what the run did."""
    _grant(cfg, "validation_result")
    for t in cfg.tables():
        n = db.rows(f'SELECT COUNT(*) n FROM "{t}"')[0]["n"]
        db.write("validation_result", {
            "run_id": run_id, "word": word, "step": "snapshot",
            "check_name": f"{phase}:{t}", "result": "count", "detail": str(n),
            "ran_at": _now(), "deleted": 0})


def _scope(params: dict) -> str:
    """The run's scope value — a word, a book, or whatever the work package runs over."""
    return params.get("Word") or params.get("Book") or ""


def _ensure_run(db: Db, cfg: Cfg, package: str, params: dict, run_id: str):
    if db.get("run", run_id=run_id):
        return
    # a DB snapshot once per NEW run (not on resume): the pre-write rollback point.
    # IBA_NO_SNAPSHOT=1 skips it for a tight loop (e.g. a book-by-book sweep).
    dbsnapshot.snapshot(f"{package}-{run_id}")
    _grant(cfg, "run")
    db.write("run", {
        "run_id": run_id, "work_package": package, "params": json.dumps(params),
        "runs_over": _scope(params), "config_version": cfg.config_version(),
        "state": "running", "resume_point": "", "started_at": _now()})
    if _scope(params):                                   # skip for scope-less runs (e.g. seed refresh)
        _snapshot(db, cfg, run_id, _scope(params), "pre")


def run_step(package: str, step_id: str, params: dict, run_id: str) -> dict:
    cfg = Cfg()
    # Dispatch gate (#334), checked first, before any DB write: an inactive work package or step is
    # refused with PermissionError (uncaught, the convention of every _grant()/_may() check).
    if cfg.work_package_inactive(package):
        cfg.close()
        raise PermissionError(
            f"work package {package!r} is inactive (retired) or unknown — refusing to dispatch "
            f"step {step_id!r} (cfg_work_package.inactive)")
    if cfg.step_inactive(package, step_id):
        cfg.close()
        raise PermissionError(
            f"step {step_id!r} in work package {package!r} is inactive (retired) or unknown — "
            f"refusing to dispatch (cfg_step.inactive)")
    # Second gate: a step with no cfg_step.kind is refused; classifying it goes through the
    # configmaint.propose approval gate.
    if cfg.step_kind(package, step_id) is None:
        cfg.close()
        raise PermissionError(
            f"step {step_id!r} in work package {package!r} has no cfg_step.kind classification "
            f"(operations|utility) — refusing to dispatch. Classify it first: "
            f"Config-Maintenance.ps1 -Step Propose -Table cfg_step -Op update "
            f"-Where '{{\"work_package\":\"{package}\",\"step\":\"{step_id}\"}}' "
            f"-Set '{{\"kind\":\"operations\"}}' (or \"utility\") -Question \"...\"")
    # Third gate, cfg_escalation.module_blocking: DISABLED (#859) pending a redesign; do not re-enable
    # without it.
    # _module = _source_for_step(step_id)
    # _blocker = cfg.conn.execute(
    #     "SELECT id, short_description FROM escalation "
    #     "WHERE state IN ('raised','re-assigned') AND (at_step=? OR source=?) "
    #     "ORDER BY id LIMIT 1", (step_id, _module)).fetchone()
    # if _blocker:
    #     cfg.close()
    #     raise PermissionError(
    #         f"step {step_id!r} in work package {package!r} is blocked by unresolved escalation "
    #         f"#{_blocker['id']} ({_blocker['short_description'][:100]!r}) — resolve it "
    #         f"(Escalation.ps1 -Action AnswerRun) before dispatching (cfg_escalation.module_blocking)")
    db = Db(cfg)
    if "Word" in params:                                  # normalise once, at the boundary
        params["Word"] = normalise(params["Word"], cfg)
    step_cfg = cfg.step(package, step_id)                 # <- handler, scope from config
    handler = _resolve(step_cfg["handler"])
    _ensure_run(db, cfg, package, params, run_id)
    wrow = db.get("word_registry", word=params["Word"]) if "Word" in params else None

    ctx = Ctx(db=db, cfg=cfg, step=Step(cfg), run_id=run_id, word=_scope(params),
              word_id=wrow["id"] if wrow else None, params=params, step_id=step_id)

    # an uncaught handler exception is recorded as an escalation, then re-raised: the traceback
    # still surfaces as before
    try:
        outcome: Outcome = handler(ctx)
    except Exception as exc:
        import traceback
        # roll back first: db.close() commits, so the crashed handler's partial writes must be discarded
        # before the escalation/run-state record is written in a fresh transaction
        db.conn.rollback()
        # an uncaught exception is self_correctable at raise time; escalate_to_decision() converts it
        # if the fix needs a new decision
        try:
            esc_raise(db, run_id, _source_for_step(step_id), step_id,
                     f"{step_id} crashed: {exc}",
                     {"traceback": traceback.format_exc()},
                     "uncaught exception — not a routed fail()/escalate() Outcome",
                     etype="run_error", assigned_to="Claude",
                     resolution_kind="self_correctable")
        except Exception as record_exc:
            # a secondary failure here is logged, never allowed to replace the original traceback
            print(f"[WARN] failed to record crash escalation: {record_exc!r}", file=sys.stderr)
        db.update("run", {"run_id": run_id}, state="failed", ended_at=_now(),
                  outcome=f"crashed: {exc}")
        db.close()
        raise

    # resolve the CONDITION to a PATH via config (cfg_on_fail); 'ok' has no rule
    if outcome.condition == "ok":
        path, message = "ok", outcome.message
    else:
        rule = cfg.on_fail(step_id, outcome.condition)
        path = rule["path"] if rule else "report-stop"
        message = (rule["message"] + " — " if rule and rule["message"] else "") + outcome.message

    # a decision_required escalation is always terminal: `path` becomes report-stop, so the exit code
    # says "stopped"; its content still comes from the handler's own escalate() call (below)
    if (path == "pause-continue" and outcome.escalation
            and outcome.escalation.get("resolution_kind", "decision_required") == "decision_required"):
        path = "report-stop"

    # act on the path
    if path == "pause-continue" and outcome.escalation:
        # only self_correctable reaches here (decision_required was moved to report-stop above)
        e = outcome.escalation
        already = db.rows("SELECT id FROM escalation WHERE run_id=? AND at_step=? "
                          "AND state='raised'", (run_id, step_id))
        if not already:
            source = word_source(ctx.word) if ctx.word else _source_for_step(step_id)
            try:
                esc_raise(db, run_id, source, step_id, e["question"], e["preset"], e["tried"],
                         etype=_escalation_type_for(step_id, ctx.word),
                         assigned_to="Researcher", resolution_kind="self_correctable",
                         title=e.get("title"))
            except Exception as record_exc:
                print(f"[WARN] failed to record self_correctable escalation: {record_exc!r}",
                     file=sys.stderr)
        db.update("run", {"run_id": run_id}, state="paused", resume_point=step_id)
    elif path == "report-stop":
        # report-stop leaves a visible escalation, like pause-continue (the run is already terminal).
        # Two ways to land here:
        #   (a) a fail()-shaped outcome (outcome.escalation is None): self_correctable at raise time.
        #   (b) a handler's escalate() with resolution_kind decision_required: keeps its own
        #       question/preset/tried and decision_required.
        already = db.rows("SELECT id FROM escalation WHERE run_id=? AND at_step=? "
                          "AND state='raised'", (run_id, step_id))
        if not already:
            if outcome.escalation:
                e = outcome.escalation
                question, preset, tried, kind, whom = (
                    e["question"], e["preset"], e["tried"], "decision_required", "Researcher")
                needs_followup = e.get("needs_followup", False)
                title = e.get("title")
            else:
                # `message` is often only a count; append the error text from `outcome.counts` so the question is
                # self-contained (full detail also in `preset`)
                detail = "; ".join(f"{k}: {v}" for k, v in outcome.counts.items() if v)
                question = f"{message} — {detail}" if detail else message
                preset = outcome.counts if outcome.counts else {}
                tried = ("hard error (report-stop) — recorded for visibility; answering this "
                        "does not resume the run, which is already terminal")
                kind, whom = "self_correctable", "Claude"
                needs_followup = False
                title = None
            source = word_source(ctx.word) if ctx.word else _source_for_step(step_id)
            try:
                esc_raise(db, run_id, source, step_id, question, preset, tried,
                         etype=_escalation_type_for(step_id, ctx.word), assigned_to=whom,
                         resolution_kind=kind, needs_followup=needs_followup, title=title)
            except Exception as record_exc:
                print(f"[WARN] failed to record report-stop escalation: {record_exc!r}",
                     file=sys.stderr)
        db.update("run", {"run_id": run_id}, state="failed", ended_at=_now(), outcome=message)
    else:
        db.update("run", {"run_id": run_id}, resume_point=step_id)
        # Close the run when it is finished: for a CHAINED work package (every step under one run_id),
        # at the last step in the cfg_step sequence; for a non-chained package (one step per run_id), as
        # soon as the step resolves on a continue path (cfg_work_package.chained).
        seq = [r["step"] for r in cfg.sequence(package)]
        if not cfg.is_chained(package) or (seq and step_id == seq[-1]):
            db.update("run", {"run_id": run_id}, state="done", ended_at=_now(),
                      outcome=message or "complete")
            if ctx.word:                                   # post-delta only for scoped runs
                _snapshot(db, cfg, run_id, ctx.word, "post")

    db.close()
    return {"step": step_id, "condition": outcome.condition, "path": path,
            "message": message, "counts": outcome.counts}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("package")
    ap.add_argument("--step", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--param", action="append", default=[])
    a = ap.parse_args()
    params = dict(p.split("=", 1) for p in a.param)
    try:
        r = run_step(a.package, a.step, params, a.run_id)
    except Exception as exc:
        # The CLI boundary always prints one JSON line with a `path` key, which every iba/app/ps/*.ps1
        # wrapper reads: an uncaught exception from run_step() (dispatch gates, write-grant checks) is
        # turned into an "error" result here (#1058). Direct Python callers of run_step() still get the
        # raw exception.
        print(json.dumps({"step": a.step, "condition": "error", "path": "error",
                          "message": f"{type(exc).__name__}: {exc}", "counts": {}}))
        return PATH_EXIT["error"]
    print(json.dumps(r))
    return PATH_EXIT.get(r["path"], 0)


if __name__ == "__main__":
    sys.exit(main())
