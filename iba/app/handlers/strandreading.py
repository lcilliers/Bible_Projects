"""strandreading handlers -- work package `strand-reading` (#2172).

One handler per Strand-Reading.ps1 step, dispatched through run.py (cfg_behaviour_rule 43). The logic
is in lib/strandreading.py; a handler checks the caller, opens the step's write grants, writes the
step's report under strand_reading.output_dir/<strand>/ and turns a lib Refused into the routed
condition 'refused' (cfg_on_fail: report-continue). Write steps need -By Claude|Researcher."""
from __future__ import annotations

import pathlib

from ..lib import escalation
from ..lib import narrativeregister as nr
from ..lib import reportkit
from ..lib import strandreading as sr
from .base import Ctx, Outcome, fail, ok


def _who(ctx: Ctx) -> str:
    who = ctx.params.get("By")
    if who not in ("Claude", "Researcher"):
        raise nr.Refused("-By Claude|Researcher is required for a write step (who made the change)")
    return who


def _writer(ctx: Ctx) -> nr.Writer:
    return nr.Writer(ctx.cfg.conn, ctx.step_id, _who(ctx))


def _report_path(ctx: Ctx, stem: str) -> pathlib.Path:
    code = (ctx.params.get("Strand") or "strand").strip()
    return pathlib.Path(ctx.cfg.required_setting("strand_reading.output_dir")) / code / f"{code}-{stem}.md"


def _unresolved(ctx: Ctx, w: nr.Writer, message: str) -> str:
    if w.unresolved:                     # an unresolved reference is an error (#2134)
        eid = nr.raise_unresolved(ctx.cfg, ctx.db, w)
        message += "".join(f"\n  unresolved: {u}" for u in w.unresolved)
        message += f"\n  escalation #{eid} raised for {len(w.unresolved)} unresolved reference(s)"
    return message


def _write(ctx: Ctx, fn) -> Outcome:
    """A write step; the register's published files are regenerated after it."""
    try:
        w = _writer(ctx)
        message = fn(w)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    message = _unresolved(ctx, w, message)
    paths = nr.export(ctx.cfg)
    return ok(f"{message}\n  published: {', '.join(p.name for p in paths)}")


def _report(ctx: Ctx, fn, stem: str, w: nr.Writer | None = None) -> Outcome:
    try:
        lines, console = fn(ctx.cfg, w, ctx.params) if w is not None else fn(ctx.cfg, ctx.params)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    out = reportkit.write_report(ctx.db.conn, ctx.step_id, _report_path(ctx, stem), lines)
    return ok(f"-> {out}\n  {console}", path=str(out))


def define(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: sr.define(ctx.cfg, w, ctx.params))


def context(ctx: Ctx) -> Outcome:
    try:
        w = _writer(ctx)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    return _report(ctx, sr.context, "context", w)


def record(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: sr.record(ctx.cfg, w, ctx.params, ctx.run_id))


def gather(ctx: Ctx) -> Outcome:
    return _report(ctx, sr.gather, "gather")


def map_blocks(ctx: Ctx) -> Outcome:
    """Statements held as items go onto the strand's escalation as one comment, quoted."""
    try:
        w = _writer(ctx)
        message, items = sr.map_blocks(ctx.cfg, w, ctx.params)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    message = _unresolved(ctx, w, message)
    if items:
        s = sr.strand(ctx.cfg.conn, ctx.params.get("Strand"))
        try:
            message += "\n  " + escalation.update(
                ctx.cfg, ctx.db, s["escalation_id"], originator=_who(ctx),
                comment=f"Strand-Reading Map ({s['code']}, {ctx.run_id}): statements in the narrative held, "
                        f"no claim yet:\n" + "\n".join(f"- {i}" for i in items))
        except ValueError as exc:
            message += f"\n  NOT recorded on #{s['escalation_id']} ({exc}); the held statements:\n  " + "\n  ".join(items)
    paths = nr.export(ctx.cfg)
    return ok(f"{message}\n  published: {', '.join(p.name for p in paths)}")


def derive(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: sr.derive(ctx.cfg, w, ctx.params, ctx.run_id))


def rewrite(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: sr.rewrite(ctx.cfg, w, ctx.params))


def account(ctx: Ctx) -> Outcome:
    return _report(ctx, sr.account, "account")
