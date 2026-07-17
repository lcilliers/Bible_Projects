"""run.py — the step dispatcher and the run-state machine.

PowerShell is the orchestrator: it loads the sequence from run.json and calls THIS
module once per step (`python -m iba.app.run <work_package> --step <step_id> ...`).
Python does the work of one step and returns a status line the PS can read.

Resumability (O7): the run's state lives in the DB (`run.state`, `run.resume_point`),
not in memory. A step that returns pause-continue writes an escalation, marks the run
paused at that step, and STOPS. Resuming is just running the package again: steps whose
rows already exist are no-ops (global dedup), and the dispatcher skips to resume_point.

Exit codes let PS branch: 0 ok · 2 paused · 3 stop.
"""

from __future__ import annotations

import argparse
import datetime
import importlib
import json
import pathlib
import sys

from .lib.db import Db, build_db
from .handlers.base import Ctx, Result

APP = pathlib.Path(__file__).resolve().parent
RUN_CFG = json.loads((APP / "config" / "run.json").read_text(encoding="utf-8"))
STEP_VERSION = json.loads((APP / "config" / "step.json").read_text(encoding="utf-8"))["connection"]["version"]

EXIT = {"ok": 0, "pause-continue": 2, "report-stop": 3}


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve(handler: str):
    mod, fn = handler.split(":")
    return getattr(importlib.import_module(mod), fn)


def _ensure_run(db: Db, package: str, params: dict, run_id: str) -> dict:
    row = db.get("run", run_id=run_id)
    if row:
        return dict(row)
    db.write("run", {
        "run_id": run_id, "work_package": package, "params": json.dumps(params),
        "runs_over": params.get("Word", ""), "config_version": RUN_CFG["config_version"],
        "state": "running", "resume_point": "", "started_at": _now(),
    })
    return dict(db.get("run", run_id=run_id))


def run_step(package: str, step_id: str, params: dict, run_id: str) -> Result:
    seq = {s["step"]: s for s in RUN_CFG["work_packages"][package]["sequence"]}
    entry = seq[step_id]
    db = Db()
    try:
        run = _ensure_run(db, package, params, run_id)
        # resume guard: if the run is paused past this step, skip
        wrow = db.get("word_registry", word=params["Word"])
        ctx = Ctx(db=db, run_id=run_id, word=params["Word"],
                  word_id=wrow["id"] if wrow else None, params=params,
                  step_version=STEP_VERSION, step=step_id)

        result: Result = _resolve(entry["handler"])(ctx)

        if result.path == "pause-continue":
            esc = result.escalation
            db.write("escalation", {
                "run_id": run_id, "at_step": esc["at_step"], "type": esc["type"],
                "question": esc["question"], "preset": json.dumps(esc["preset"]),
                "tried": esc["tried"], "state": "raised", "raised_at": _now()})
            db.update("run", {"run_id": run_id}, state="paused", resume_point=step_id)
        elif result.path == "report-stop":
            db.update("run", {"run_id": run_id}, state="failed", ended_at=_now(),
                      outcome=result.message)
        else:
            db.update("run", {"run_id": run_id}, resume_point=step_id)
        db.close()
        return result
    except Exception:
        db.close()
        raise


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("package")
    ap.add_argument("--step", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--param", action="append", default=[], help="Name=Value")
    ap.add_argument("--build-db", action="store_true")
    a = ap.parse_args()
    if a.build_db:
        build_db()
    params = dict(p.split("=", 1) for p in a.param)
    r = run_step(a.package, a.step, params, a.run_id)
    print(json.dumps({"step": a.step, "path": r.path, "message": r.message, "counts": r.counts}))
    return EXIT.get(r.path, 0)


if __name__ == "__main__":
    sys.exit(main())
