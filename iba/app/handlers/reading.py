"""reading handlers -- work package `reading` (#2228).

One handler per Reading.ps1 step, dispatched through run.py (cfg_behaviour_rule 43). The logic is in
lib/reading.py; a handler checks the caller, opens the step's write grants and turns a lib Refused into the
routed condition 'refused' (cfg_on_fail: report-continue). Write steps need -By Claude|Researcher. Account
writes its report under reading.output_dir/<label>/."""
from __future__ import annotations

import json
import pathlib

from ..lib import narrativeregister as nr
from ..lib import reading as rd
from ..lib import reportkit
from .base import Ctx, Outcome, fail, ok

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]


def _writer(ctx: Ctx) -> nr.Writer:
    who = ctx.params.get("By")
    if who not in ("Claude", "Researcher"):
        raise nr.Refused("-By Claude|Researcher is required for a write step (who made the change)")
    return nr.Writer(ctx.cfg.conn, ctx.step_id, who)


def _write(ctx: Ctx, fn, export: bool = False) -> Outcome:
    try:
        w = _writer(ctx)
        message = fn(w)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    if w.unresolved:                     # an unresolved reference is an error (#2134)
        eid = nr.raise_unresolved(ctx.cfg, ctx.db, w)
        message += "".join(f"\n  unresolved: {u}" for u in w.unresolved)
        message += f"\n  escalation #{eid} raised for {len(w.unresolved)} unresolved reference(s)"
    if export:
        message += f"\n  published: {', '.join(p.name for p in nr.export(ctx.cfg))}"
    return ok(message)


def open(ctx: Ctx) -> Outcome:  # noqa: A001 -- the step's name
    file_request = None
    if ctx.params.get("File"):
        f = pathlib.Path(ctx.params["File"])
        f = f if f.is_absolute() else PROJECT_ROOT / f
        if not f.is_file():
            return fail("refused", f"request file not found: {f.as_posix()}")
        try:
            file_request = {k.lower(): v for k, v in json.loads(f.read_text(encoding="utf-8")).items()}
        except (ValueError, AttributeError) as exc:
            return fail("refused", f"request file {f.as_posix()} is not a JSON object: {exc}")
    return _write(ctx, lambda w: rd.open_(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT, file_request))


def record(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.record(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT))


def check(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.check(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT))


def synergy(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.synergy(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT))


def apply(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.apply(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT), export=True)


def publish(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.publish(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT), export=True)


def account(ctx: Ctx) -> Outcome:
    try:
        lines, console = rd.account(ctx.cfg, ctx.params, PROJECT_ROOT)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    label = ctx.params["Label"].strip()
    path = PROJECT_ROOT / ctx.cfg.required_setting("reading.output_dir") / label / f"{label}-account.md"
    out = reportkit.write_report(ctx.db.conn, ctx.step_id, path, lines)
    return ok(f"-> {out}\n  {console}", path=str(out))
