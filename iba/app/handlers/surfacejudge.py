"""surfacejudge handlers -- work package `surface-judge` (#2354), one step per Surface-Judge.ps1 action.

Status reads a batch file against the list of surfaces; Run judges the surfaces not yet judged (lib/surfacejudge.py);
Cycle runs the whole list unattended in work periods with a cool-down between, Progress reads its progress file and
Stop asks it to end. None writes the database: the answers go to the batch file in cfg_setting
surface_judge.batch_dir (the progress file and stop flag sit beside it). A usage problem (bad batch name, missing
setting) is the routed condition 'refused' and writes nothing."""
from __future__ import annotations

import pathlib
import re
import sys
import time

from ..lib import surfacejudge as sj
from .base import Ctx, Outcome, fail, ok

BATCH_NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*-v[1-9][0-9]*-[0-9]{8}")


def _batch(ctx: Ctx) -> pathlib.Path:
    name = ctx.params.get("Batch")
    if not name:
        raise sj.JudgeError("-Batch is required: the name of the batch file, like first-split-v1-20261102")
    if not BATCH_NAME.fullmatch(name):
        raise sj.JudgeError(f"-Batch {name!r} is not lower-case words joined by hyphens, then -v and a number, "
                            "then -yyyymmdd (like first-split-v1-20261102)")
    folder = ctx.cfg.setting("surface_judge.batch_dir")
    if not folder:
        raise sj.JudgeError("cfg_setting surface_judge.batch_dir is missing")
    return pathlib.Path(folder) / f"{name}.jsonl"


def status(ctx: Ctx) -> Outcome:
    try:
        out = _batch(ctx)
        groups = sj.stored_groups(sj.settings(ctx.cfg))
    except sj.JudgeError as exc:
        return fail("refused", str(exc))
    s = sj.status(ctx.cfg.conn, groups, out)
    lines = [f"batch {out.as_posix()}" + ("" if out.exists() else " (no file yet)"),
             f"list (distinct live surfaces of surface_subgroup): {s['list']}",
             f"judged: {s['judged']}  " + "  ".join(f"{g} {n}" for g, n in s["per_group"].items()),
             f"failed (tried, no usable answer; tried again on the next run): {s['failed']}",
             f"left: {s['left']}"]
    if s["not_on_list"]:
        lines.append(f"in the file but no longer on the list: {s['not_on_list']}")
    return ok("\n  ".join(lines), judged=s["judged"], failed=s["failed"], left=s["left"])


def run(ctx: Ctx) -> Outcome:
    try:
        out = _batch(ctx)
        vals = sj.settings(ctx.cfg)
        limit = ctx.params.get("Limit")
        if limit not in (None, ""):
            if not str(limit).isdigit() or int(limit) < 1:
                raise sj.JudgeError(f"-Limit is a whole number of at least 1, not {limit!r}")
            limit = int(limit)
        else:
            limit = None
    except sj.JudgeError as exc:
        return fail("refused", str(exc))
    surfaces = [s for s, _ in sj.surface_list(ctx.cfg.conn)]
    ctx.cfg.conn.commit()  # run.py holds the write lock on its run row until the step ends: release it before the long work
    # progress goes to stderr: stdout carries the step's JSON result
    try:
        res = sj.run_words(vals, surfaces, out, limit, emit=lambda m: print(m, file=sys.stderr, flush=True))
    except sj.JudgeError as exc:  # the server check before the first surface: nothing was sent or written
        return fail("refused", str(exc))
    left = sj.status(ctx.cfg.conn, sj.stored_groups(vals), out)["left"]
    msg = (f"judged {res['judged']}, failed {res['failed']}" + (", stopped by Ctrl+C" if res["stopped"] else "")
           + f"; {left} left; batch {out.as_posix()}")
    if res["halted"]:
        return fail("halted", f"halted after {vals['max_consecutive_failures']} surfaces in a row with no usable "
                              f"answer (the server stopped answering?): {msg}", judged=res["judged"],
                    failed=res["failed"], left=left)
    return ok(msg, judged=res["judged"], failed=res["failed"], left=left)


def cycle(ctx: Ctx) -> Outcome:
    try:
        out = _batch(ctx)
        vals = sj.settings(ctx.cfg)
        cyc = sj.cycle_settings(ctx.cfg)
    except sj.JudgeError as exc:
        return fail("refused", str(exc))
    surfaces = [s for s, _ in sj.surface_list(ctx.cfg.conn)]
    # run.py holds the write lock on its run row until the step ends; a cycle lasts hours, and every other command
    # (Progress, Stop, Escalation, ...) would fail with 'database is locked': release it before the long work
    ctx.cfg.conn.commit()
    try:
        prog = sj.run_cycle(vals, cyc, surfaces, out, emit=lambda m: print(m, file=sys.stderr, flush=True))
    except sj.JudgeError as exc:  # a cycle on this batch is already running
        return fail("refused", str(exc))
    msg = (f"cycle {prog['state']}: judged {prog['judged']} of {prog['list']}, failed {prog['failed']}, "
           f"left {prog['left']}, {prog['periods']} work periods; batch {out.as_posix()}")
    if prog["state"] == "halted":
        return fail("halted", f"{msg}; {prog['halts_in_a_row']} periods in a row with no progress, the last problem: "
                              f"{prog['last_problem']}", judged=prog["judged"], failed=prog["failed"], left=prog["left"])
    return ok(msg, judged=prog["judged"], failed=prog["failed"], left=prog["left"])


def stop(ctx: Ctx) -> Outcome:
    try:
        out = _batch(ctx)
        vals = sj.settings(ctx.cfg)
    except sj.JudgeError as exc:
        return fail("refused", str(exc))
    prog = sj.read_progress(out)
    if not sj.cycle_alive(prog, float(vals["timeout_seconds"]) + 120):
        last = f" (last state {prog['state']}, updated {prog['updated_at']})" if prog else " (no progress file)"
        return ok("no cycle is running on this batch" + last)
    sj.stop_path(out).write_text("stop requested\n", encoding="utf-8")
    return ok("stop requested: the cycle ends after the surface in hand (about 10 s) or, in a cool-down, within 5 s; "
              "run -Action Cycle again with the same -Batch to resume")


def progress(ctx: Ctx) -> Outcome:
    try:
        out = _batch(ctx)
        vals = sj.settings(ctx.cfg)
    except sj.JudgeError as exc:
        return fail("refused", str(exc))
    p = sj.read_progress(out)
    if p is None:
        return ok(f"no progress file for batch {out.stem}: no cycle has been run on it (use -Action Status for the batch file)")
    age = int(time.time() - p.get("updated_epoch", 0))
    alive = sj.cycle_alive(p, float(vals["timeout_seconds"]) + 120)
    head = f"batch {p['batch']}: state {p['state']}, updated {age} s ago"
    if p["state"] in ("running", "cooling", "waiting_after_halt", "starting") and not alive:
        head += " -- NOT running: the progress has not moved for longer than a surface can take (the cycle was interrupted); run -Action Cycle to resume"
    pct = round(100 * p["judged"] / p["list"], 1) if p["list"] else 0
    lines = [head,
             f"judged {p['judged']} of {p['list']} ({pct} percent): " + "  ".join(f"{g} {n}" for g, n in p["per_group"].items()),
             f"failed (tried again in the next period): {p['failed']}  untried: {p['untried']}  left in all: {p['left']}",
             f"this cycle: {p['periods']} work periods, {p['judged_this_cycle']} surfaces judged since it started {p['started_at']}"
             + (f"; mean of the last 50: {p['mean_secs_last_50']} s" if p["mean_secs_last_50"] is not None else "")]
    if p.get("period_started_at"):
        lines.append(f"current or last work period started {p['period_started_at']}")
    if p.get("next_resume_at"):
        lines.append(f"resumes work at {p['next_resume_at']}")
    if p.get("estimated_finish"):
        lines.append(f"estimated finish {p['estimated_finish']} ({p['estimate_note']})")
    if p.get("last_problem"):
        lines.append(f"last problem: {p['last_problem']} (periods in a row with no progress: {p['halts_in_a_row']})")
    return ok("\n  ".join(lines), judged=p["judged"], failed=p["failed"], left=p["left"])
