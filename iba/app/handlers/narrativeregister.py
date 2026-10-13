"""narrativeregister handlers -- work package `narrative-register` (escalation #2110).

One handler per Narrative-Register.ps1 action, dispatched through run.py (cfg_behaviour_rule 43).
The logic is in lib/narrativeregister.py; a handler only checks the caller, opens the step's write
grants and turns a lib Refused into the routed condition 'refused' (cfg_on_fail: report-continue,
not recorded as an escalation). Write actions need -By Claude|Researcher (no silent default --
the same rule as Escalation.ps1 -AnsweredBy)."""
from __future__ import annotations

import pathlib

from ..lib import narrativeregister as nr
from ..lib import reportkit
from .base import Ctx, Outcome, fail, ok


def _who(ctx: Ctx) -> str:
    who = ctx.params.get("By")
    if who not in ("Claude", "Researcher"):
        raise nr.Refused("-By Claude|Researcher is required for a write action (who made the change)")
    return who


def _write(ctx: Ctx, fn) -> Outcome:
    """A write action, then the published files regenerated (spec sec5: 'The register file is the
    published copy, regenerated from the database after each change')."""
    try:
        w = nr.Writer(ctx.cfg.conn, ctx.step_id, _who(ctx))
        message = fn(ctx.cfg, w, ctx.params)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    paths = nr.export(ctx.cfg)
    return ok(f"{message}\n  published: {', '.join(p.name for p in paths)}")


def _report(ctx: Ctx, fn, stem: str) -> Outcome:
    try:
        lines, console = fn(ctx.cfg, ctx.params)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    out_dir = pathlib.Path(ctx.cfg.required_setting("narrative.register_report_dir"))
    out = reportkit.write_report(ctx.db.conn, ctx.step_id, out_dir / f"{stem}.md", lines)
    return ok("\n  ".join([f"-> {out}"] + console), path=str(out))


def add_claim(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.add_claim)


def edit(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.edit)


def tell(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.tell)


def untell(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.untell)


def withdraw(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.withdraw)


def edit_note(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.edit_note)


def edit_chapter(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.edit_chapter)


def edit_section(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.edit_section)


def record(ctx: Ctx) -> Outcome:
    return _write(ctx, nr.record)


def find(ctx: Ctx) -> Outcome:
    return _report(ctx, nr.find, "narrative-register-find")


def history(ctx: Ctx) -> Outcome:
    claim = (ctx.params.get("Claim") or "claim").replace(" ", "")
    return _report(ctx, nr.history, f"{claim}-narrative-claim-history")


def check(ctx: Ctx) -> Outcome:
    return _report(ctx, nr.check, "narrative-register-check")


def export(ctx: Ctx) -> Outcome:
    paths = nr.export(ctx.cfg)
    return ok("\n  ".join(["wrote"] + [str(p) for p in paths]), files=len(paths))
