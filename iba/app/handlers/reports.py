"""reports handlers — thin dispatcher adapters over report.py / validation.py.

Both modules already had their own reusable generate functions (report.generate, validation.
generate/generate_book); this just wraps them in the standard `def h(ctx) -> Outcome` contract so
they're registered work packages/steps like everything else in the app, instead of standalone
scripts nothing else knows about — the same gap configuration_maintenance closed for
cfgload/cfgcheck/cfgreport. Mostly read-only — the one exception is
`verse_span_meaning_report` (see `report.auto_backfill_before_render`, 2026-07-26): it may write
to the raw/lexicon-parsed layer via `raw.backfill_meaning_for`, gated by that setting, before
rendering. Every other report here writes nothing to the DB.
"""

from __future__ import annotations

import pathlib

from .base import Ctx, Outcome, ok, fail
from . import raw as raw_mod
from .. import report as report_mod
from .. import validation as validation_mod
from ..lib import retention as retention_mod
from ..lib import registryreport, schemareport, seedreport, spanreport, strongreport
from ..lib import passagedebatereport, passagetrack, versespanmeaningreport
from ..lib.stepapi import StepUnavailable
from ..tools import export_tables_csv


def word_report(ctx: Ctx) -> Outcome:
    out = report_mod.generate(ctx.params["Word"], cfg=ctx.cfg)
    if out is None:
        return fail("word-not-found", f"{ctx.params['Word']!r} is not in the DB")
    return ok(f"wrote {out}", path=str(out))


def validation_word(ctx: Ctx) -> Outcome:
    out, overall, (p, w, f) = validation_mod.generate(ctx.params["Word"])
    return ok(f"{overall} ({p} pass, {w} warn, {f} fail) -> {out}",
             path=str(out), overall=overall, passes=p, warns=w, fails=f)


def validation_book(ctx: Ctx) -> Outcome:
    out, overall, (p, w, f) = validation_mod.generate_book(ctx.params["Book"])
    return ok(f"{overall} ({p} pass, {w} warn, {f} fail) -> {out}",
             path=str(out), overall=overall, passes=p, warns=w, fails=f)


def retention_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.setting("retention.report_path", "iba/app/reports/log-retention.md"))
    out = retention_mod.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def table_export(ctx: Ctx) -> Outcome:
    """CSV dump of every DATA table, verbatim — config governs its own concerns; the DEDICATED
    config report writer (configmaint.report) already owns cfg_* content, so this excludes it
    (found 2026-07-22 — the tool used to dump cfg_* too, a real duplication bug). -Out/-Table stay
    plain PS parameters (a one-off destination/subset override), not config — same boundary the
    researcher drew 2026-07-22: a parameter explained in the script's own inline help isn't a
    setting just because the script is now dispatcher-registered."""
    out_dir = pathlib.Path(ctx.params.get("Out") or ctx.cfg.setting("table_export.output_dir",
                                                                    "iba/app/export"))
    only = ctx.params.get("Table")
    only = only.split(",") if isinstance(only, str) else only
    results = export_tables_csv.export(out_dir, only)
    return ok(f"exported {len(results)} table(s) to {out_dir}", path=str(out_dir),
             tables=len(results))


def seed_candidate_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.setting("report.seed_candidate_path",
                                        "iba/app/reports/seed-candidate.md"))
    out = seedreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def strong_meaning_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.setting("report.strong_meaning_path",
                                        "iba/app/reports/strong-meaning.md"))
    out = strongreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def span_analysis_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.setting("report.span_analysis_path",
                                        "iba/app/reports/span-analysis.md"))
    out = spanreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def verse_span_meaning_report(ctx: Ctx) -> Outcome:
    """Book-scoped, needs -Book plus exactly one of -Chapters/-Range. STEP-dependent (AMBIGUOUS-
    span live disambiguation) — versespanmeaningreport.write_report() reads step.required_for_runs
    itself and raises StepUnavailable when required and down; caught here into a clean fail(),
    resolved by cfg_on_fail(report.verse_span_meaning, unreachable) rather than crashing the run.

    `report.auto_backfill_before_render` (cfg_setting, module `report`, default True — researcher's
    direct 2026-07-26 instruction, answering the open question left by the prior session): before
    rendering, run the identical pull `Raw-Backfill.ps1` does (raw.backfill_meaning_for) for any
    span in this exact book+range whose strong is not yet registered. A report is never silently
    left at partial coverage waiting on a separate manual step. Set False to go back to a pure
    read-only render (STEP-down still refuses rendering if step.required_for_runs is True, exactly
    as before — this setting only controls whether a gap gets auto-filled, not whether STEP itself
    is required)."""
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    if ctx.params.get("Range"):
        ch, vlo, vhi = versespanmeaningreport.parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = versespanmeaningreport.parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None
    backfill_note = ""
    try:
        if ctx.cfg.setting("report.auto_backfill_before_render", True):
            result = raw_mod.backfill_meaning_for(ctx, book, lo, hi, verse_lo, verse_hi)
            if result["missing_before"]:
                backfill_note = (f" (auto-backfilled {result['missing_before']} previously-"
                                 f"unregistered strong(s) before rendering)")
        out = versespanmeaningreport.write_report(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                                  book_label=book_label)
    except StepUnavailable as e:
        return fail("unreachable", str(e))
    passage_id = passagetrack.record_extract(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                             book_label, out)
    return ok(f"wrote {out}{backfill_note}", path=str(out), passage_id=passage_id)


def passage_debate_report(ctx: Ctx) -> Outcome:
    """Book-scoped, needs -Book plus exactly one of -Chapters/-Range, same shape as
    `verse_span_meaning_report`. Writes a debate SCAFFOLD, not a finished debate — see
    `lib/passagedebatereport.py`'s module docstring for what is and isn't mechanised. Two
    failure conditions distinct from `report.verse_span_meaning`'s (no STEP dependency here):
    the base extract for this exact range not existing yet, and either `method.*` cfg_setting
    pointing at a file that isn't on disk."""
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    if ctx.params.get("Range"):
        ch, vlo, vhi = versespanmeaningreport.parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = versespanmeaningreport.parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None
    try:
        out = passagedebatereport.write_scaffold(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                                 book_label=book_label)
    except passagedebatereport.BaseExtractMissing as e:
        return fail("base-extract-missing", str(e))
    except passagedebatereport.MethodDocMissing as e:
        return fail("guidance-doc-missing", str(e))
    passage_id = passagetrack.record_debate(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                            book_label, out)
    return ok(f"wrote {out}", path=str(out), passage_id=passage_id)


def schema_overview_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.setting("report.schema_overview_path",
                                        "iba/app/reports/schema-overview.md"))
    out = schemareport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def registry_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.setting("report.registry_path",
                                        "iba/app/reports/registry.md"))
    out = registryreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))
