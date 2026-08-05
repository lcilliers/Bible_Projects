"""lexical.py — dispatcher handler for `lexical.build` (work package `verse-lexical`, ordinal 0).
Thin adapter over `lib/lexical.py`'s `build_for_range`, same shape as
`handlers/reports.py:verse_span_meaning_report` (the step this replaces).

Auto-backfill reused unchanged from `report.verse_span_meaning`'s own pattern (`report.
auto_backfill_before_render`, `raw.backfill_meaning_for`) — a content-role code with no `strong`
row yet gets pulled from STEP before building, same researcher instruction (2026-07-26), same
setting, not a new one.
"""

from __future__ import annotations

from .base import Ctx, Outcome, fail, ok
from . import raw as raw_mod
from ..lib import lexical
from ..lib.stepapi import Step, StepUnavailable
from ..lib.versespanmeaningreport import parse_chapters, parse_range


def _may(ctx: Ctx, writer: str, table: str) -> None:
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


def build(ctx: Ctx) -> Outcome:
    _may(ctx, "lexical.build", "verse_lexical")

    book = ctx.params["Book"]
    if ctx.params.get("Range"):
        ch, vlo, vhi = parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None

    required = ctx.cfg.setting("step.required_for_runs", True)
    step: Step | None = None
    try:
        Step(ctx.cfg).up()
        step = Step(ctx.cfg)
    except StepUnavailable as e:
        if required:
            return fail("unreachable", str(e))
        step = None

    backfill_note = ""
    if ctx.cfg.setting("report.auto_backfill_before_render", True):
        try:
            result = raw_mod.backfill_meaning_for(ctx, book, lo, hi, verse_lo, verse_hi)
            if result["missing_before"]:
                backfill_note = (f" (auto-backfilled {result['missing_before']} previously-"
                                 f"unregistered strong(s) before building)")
        except StepUnavailable as e:
            if required:
                return fail("unreachable", str(e))

    totals = lexical.build_for_range(ctx.db.conn, book, lo, hi, verse_lo, verse_hi, step)
    ctx.db.conn.commit()

    return ok(
        f"{book} {lo}-{hi}: {totals['verses']} verse(s), {totals['spans']} span(s), "
        f"{totals['codes']} code(s) resolved ({totals['inserted']} written, "
        f"{totals['superseded']} superseded){backfill_note}",
        **totals)
