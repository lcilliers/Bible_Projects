"""reports handlers — thin dispatcher adapters over report.py / validation.py.

Both modules already had their own reusable generate functions (report.generate, validation.
generate/generate_book); this just wraps them in the standard `def h(ctx) -> Outcome` contract so
they're registered work packages/steps like everything else in the app, instead of standalone
scripts nothing else knows about — the same gap configuration_maintenance closed for
cfgload/cfgcheck/cfgreport. Read-only; no cfg_write_grant needed (nothing writes to the DB).
"""

from __future__ import annotations

import pathlib

from .base import Ctx, Outcome, ok, fail
from .. import report as report_mod
from .. import validation as validation_mod
from ..lib import retention as retention_mod
from ..lib import registryreport, schemareport, seedreport, spanreport, strongreport
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
