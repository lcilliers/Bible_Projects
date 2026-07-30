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
from .handlers.base import Ctx, Outcome

# path -> what the run does + the process exit code
PATH_EXIT = {"ok": 0, "report-continue": 0, "self-heal": 0, "pause-continue": 2, "report-stop": 3}


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve(handler: str):
    mod, fn = handler.split(":")
    return getattr(importlib.import_module(mod), fn)


def _grant(cfg: Cfg, table: str):
    """The dispatcher writes control tables under the 'run' write grant — config-governed."""
    if table not in cfg.may_write("run"):
        raise PermissionError(f"write-grant violation: 'run' may not write {table!r} (cfg_write_grant)")


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
    # a real DB file snapshot, once per NEW run (not on resume) — the pre-write rollback point
    # this app didn't have until a candidate.load bug found the gap the hard way, 2026-07-22.
    # IBA_NO_SNAPSHOT=1 skips it for a tight loop (e.g. a book-by-book sweep), same escape hatch
    # the legacy engine's own _apply_* snapshotting uses.
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
    # Dispatch gate (escalation #334, 2026-07-29) — checked FIRST, before _ensure_run/any DB
    # write, so a refusal is clean and has no partial effect. Before this, `inactive` was
    # validator-only metadata: nothing stopped `Set-Candidates.ps1 -Book Obad` (a retired work
    # package) from actually running. Raised as PermissionError, uncaught, the same convention
    # every `_grant()`/`_may()` write-grant check in this app already uses for "the config
    # forbids this" — see BUILD.md sec37.
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
    # Second gate, 2026-07-30 (the researcher's own operations/utility model — "routines not in
    # the table[s] need special permission to be used"): a step with no cfg_step.kind classification
    # is refused too, not silently run. "Special permission" = the same configmaint.propose
    # approval gate every other cfg_* change goes through — there is no separate bypass.
    if cfg.step_kind(package, step_id) is None:
        cfg.close()
        raise PermissionError(
            f"step {step_id!r} in work package {package!r} has no cfg_step.kind classification "
            f"(operations|utility) — refusing to dispatch. Classify it first: "
            f"Config-Maintenance.ps1 -Step Propose -Table cfg_step -Op update "
            f"-Where '{{\"work_package\":\"{package}\",\"step\":\"{step_id}\"}}' "
            f"-Set '{{\"kind\":\"operations\"}}' (or \"utility\") -Question \"...\"")
    db = Db(cfg)
    if "Word" in params:                                  # normalise once, at the boundary
        params["Word"] = normalise(params["Word"], cfg)
    step_cfg = cfg.step(package, step_id)                 # <- handler, scope from config
    handler = _resolve(step_cfg["handler"])
    _ensure_run(db, cfg, package, params, run_id)
    wrow = db.get("word_registry", word=params["Word"]) if "Word" in params else None

    ctx = Ctx(db=db, cfg=cfg, step=Step(cfg), run_id=run_id, word=_scope(params),
              word_id=wrow["id"] if wrow else None, params=params, step_id=step_id)

    # Researcher's standing rule, 2026-07-30: "if a validation runs for a module operation, or an
    # error takes place in a module operation, then it would escalate and record an escalation
    # report. It is that simple." Before this, an uncaught exception in a handler propagated as a
    # bare crash — no record, nothing in `escalation`, nothing an Escalation.ps1 -Action List would
    # ever show. Caught here, recorded, then RE-RAISED — this adds a permanent record, it does not
    # soften or hide the failure (the traceback still surfaces exactly as before).
    try:
        outcome: Outcome = handler(ctx)
    except Exception as exc:
        import traceback
        _grant(cfg, "escalation")
        db.write("escalation", {
            "run_id": run_id, "word": ctx.word, "at_step": step_id, "type": "crash",
            "question": f"{step_id} crashed: {exc}",
            "preset": json.dumps({"traceback": traceback.format_exc()}),
            "tried": "uncaught exception — not a routed fail()/escalate() Outcome",
            "state": "raised", "answer": None, "answered_at": None, "raised_at": _now()})
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

    # act on the path
    if path == "pause-continue" and outcome.escalation:
        e = outcome.escalation
        # idempotent: do not raise a duplicate if THIS run already has one pending at this step.
        # Keyed on run_id, not (word, step): a word-less run (every config/quality-check step —
        # configmaint.propose, candidate.validate, ...) has ctx.word == "" for every invocation, so
        # keying on word alone silently treated any second concurrent proposal as a "duplicate" of
        # the first and never wrote its escalation row at all (found 2026-07-22, proposing two
        # governance settings back to back — the run still paused, but only one escalation existed).
        already = db.rows("SELECT id FROM escalation WHERE run_id=? AND at_step=? "
                          "AND state='raised'", (run_id, step_id))
        if not already:
            _grant(cfg, "escalation")
            db.write("escalation", {
                "run_id": run_id, "word": ctx.word, "at_step": step_id, "type": e["type"],
                "question": e["question"], "preset": json.dumps(e["preset"]), "tried": e["tried"],
                "state": "raised", "answer": None, "answered_at": None, "raised_at": _now()})
        db.update("run", {"run_id": run_id}, state="paused", resume_point=step_id)
    elif path == "report-stop":
        # Added 2026-07-30 (the same standing rule): report-stop used to only flip run.state to
        # 'failed' — no escalation row, invisible to Escalation.ps1 -Action List. A hard error is
        # still an error; it now leaves the same permanent, visible record a pause-continue
        # finding does, even though (unlike pause-continue) answering it doesn't resume anything —
        # the run is already terminal. Same idempotency guard as the pause-continue block above.
        already = db.rows("SELECT id FROM escalation WHERE run_id=? AND at_step=? "
                          "AND state='raised'", (run_id, step_id))
        if not already:
            _grant(cfg, "escalation")
            db.write("escalation", {
                "run_id": run_id, "word": ctx.word, "at_step": step_id, "type": "report-stop",
                "question": message,
                "preset": json.dumps(outcome.counts) if outcome.counts else "{}",
                "tried": "hard error (report-stop) — recorded for visibility; answering this does "
                        "not resume the run, which is already terminal",
                "state": "raised", "answer": None, "answered_at": None, "raised_at": _now()})
        db.update("run", {"run_id": run_id}, state="failed", ended_at=_now(), outcome=message)
    else:
        db.update("run", {"run_id": run_id}, resume_point=step_id)
        # Close the run when it's actually finished. For a CHAINED work package (every step runs
        # under one run_id in one PS invocation — new-word, set-candidates, build-passages), that
        # means the LAST step in the cfg_step sequence. For a NON-chained package (each step
        # invoked independently, one per run_id — configuration-maintenance, reports, candidate-
        # quality, passage-quality, candidate-curation), a standalone step can never BE the last
        # step of a multi-step registration it only ever partially executes — it is done as soon
        # as IT resolves on a continue path. Found 2026-07-22: the old "last-in-sequence-only"
        # rule left 185 runs stuck 'paused'/'running' forever despite being fully resolved — see
        # cfg_work_package.chained / migration/add_work_package_chained_column.py.
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
    r = run_step(a.package, a.step, params, a.run_id)
    print(json.dumps(r))
    return PATH_EXIT.get(r["path"], 0)


if __name__ == "__main__":
    sys.exit(main())
