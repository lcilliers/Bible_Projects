"""surfacebase handlers -- work package `surface-base` (#2359), one step per Surface-Base.ps1 action.

Status reads a batch file against the input list of words; Run asks the Ollama server for the base form of the words
not yet answered (lib/surfacebase.py). Neither writes the database: the answers go to the batch file in cfg_setting
surface_judge.batch_dir. A usage problem (bad batch name, missing setting or input list) is the routed condition
'refused' and writes nothing."""
from __future__ import annotations

import pathlib
import re
import sys

from ..lib import surfacebase as sb
from .base import Ctx, Outcome, fail, ok

BATCH_NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*-v[1-9][0-9]*-[0-9]{8}")


def _batch(ctx: Ctx) -> pathlib.Path:
    name = ctx.params.get("Batch")
    if not name:
        raise sb.BaseError("-Batch is required: the name of the batch file, like base-form-v1-20261104")
    if not BATCH_NAME.fullmatch(name):
        raise sb.BaseError(f"-Batch {name!r} is not lower-case words joined by hyphens, then -v and a number, "
                           "then -yyyymmdd (like base-form-v1-20261104)")
    folder = ctx.cfg.setting("surface_judge.batch_dir")
    if not folder:
        raise sb.BaseError("cfg_setting surface_judge.batch_dir is missing")
    return pathlib.Path(folder) / f"{name}.jsonl"


def status(ctx: Ctx) -> Outcome:
    try:
        out = _batch(ctx)
        vals = sb.settings(ctx.cfg)
        words = sb.input_words(vals, out)
    except sb.BaseError as exc:
        return fail("refused", str(exc))
    s = sb.status(vals, words, out)
    lines = [f"batch {out.as_posix()}" + ("" if out.exists() else " (no file yet)"),
             f"list (words in the input file): {s['list']}",
             f"answered: {s['answered']}  " + "  ".join(f"{r} {n}" for r, n in s["per_relation"].items()),
             f"failed (tried, no usable answer; tried again on the next run): {s['failed']}",
             f"left: {s['left']}"]
    if s["not_on_list"]:
        lines.append(f"in the file but not on the input list: {s['not_on_list']}")
    return ok("\n  ".join(lines), answered=s["answered"], failed=s["failed"], left=s["left"])


def run(ctx: Ctx) -> Outcome:
    try:
        out = _batch(ctx)
        vals = sb.settings(ctx.cfg)
        words = sb.input_words(vals, out)
        limit = ctx.params.get("Limit")
        if limit not in (None, ""):
            if not str(limit).isdigit() or int(limit) < 1:
                raise sb.BaseError(f"-Limit is a whole number of at least 1, not {limit!r}")
            limit = int(limit)
        else:
            limit = None
    except sb.BaseError as exc:
        return fail("refused", str(exc))
    ctx.cfg.conn.commit()  # run.py holds the write lock on its run row until the step ends: release it before the long work
    # progress goes to stderr: stdout carries the step's JSON result
    try:
        res = sb.run_words(vals, words, out, limit, emit=lambda m: print(m, file=sys.stderr, flush=True))
    except sb.BaseError as exc:  # the server check before the first word: nothing was sent or written
        return fail("refused", str(exc))
    left = sb.status(vals, words, out)["left"]
    msg = (f"asked {res['asked']}, failed {res['failed']}" + (", stopped by Ctrl+C" if res["stopped"] else "")
           + f"; {left} left; batch {out.as_posix()}")
    if res["halted"]:
        return fail("halted", f"halted after {vals['max_consecutive_failures']} words in a row with no usable "
                              f"answer (the server stopped answering?): {msg}", asked=res["asked"],
                    failed=res["failed"], left=left)
    return ok(msg, asked=res["asked"], failed=res["failed"], left=left)
