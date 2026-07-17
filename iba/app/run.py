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
from .handlers.base import Ctx, Outcome

# path -> what the run does + the process exit code
PATH_EXIT = {"ok": 0, "report-continue": 0, "self-heal": 0, "pause-continue": 2, "report-stop": 3}


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve(handler: str):
    mod, fn = handler.split(":")
    return getattr(importlib.import_module(mod), fn)


def _ensure_run(db: Db, cfg: Cfg, package: str, params: dict, run_id: str):
    if db.get("run", run_id=run_id):
        return
    db.write("run", {
        "run_id": run_id, "work_package": package, "params": json.dumps(params),
        "runs_over": params.get("Word", ""), "config_version": cfg.config_version(),
        "state": "running", "resume_point": "", "started_at": _now()})


def run_step(package: str, step_id: str, params: dict, run_id: str) -> dict:
    cfg = Cfg()
    db = Db(cfg)
    step_cfg = cfg.step(package, step_id)                 # <- handler, scope from config
    handler = _resolve(step_cfg["handler"])
    _ensure_run(db, cfg, package, params, run_id)
    wrow = db.get("word_registry", word=params["Word"])

    ctx = Ctx(db=db, cfg=cfg, step=Step(cfg), run_id=run_id, word=params["Word"],
              word_id=wrow["id"] if wrow else None, params=params, step_id=step_id)

    outcome: Outcome = handler(ctx)

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
        db.write("escalation", {
            "run_id": run_id, "at_step": step_id, "type": e["type"], "question": e["question"],
            "preset": json.dumps(e["preset"]), "tried": e["tried"], "state": "raised",
            "raised_at": _now()})
        db.update("run", {"run_id": run_id}, state="paused", resume_point=step_id)
    elif path == "report-stop":
        db.update("run", {"run_id": run_id}, state="failed", ended_at=_now(), outcome=message)
    else:
        db.update("run", {"run_id": run_id}, resume_point=step_id)

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
