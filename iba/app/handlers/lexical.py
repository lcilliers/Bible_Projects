"""lexical.py — dispatcher handler for the lexical steps.

  lexical.build: the -Book + range adapter over `lib/lexical.py` (verse resolution and the
    write-grant check here; the writes in that module). Verse-scoped: no `passage` row is
    resolved or required (#1451). Auto-backfill as in report.verse_span_meaning
    (`report.auto_backfill_before_render`, `raw.backfill_meaning_for`).
  lexical.readiness: the 3-leg base-data readiness check (#1606).
  (lexical.meaning and lexical.relational, the cluster-based verse-reading stage of #1706 and #1860, are retired, #2507; the lexical
    analysis of the words is stage 1 of the collection reading, lib/layerreading.py, Collection-Build.ps1 -Action LayerOpen -Step S1.)
"""

from __future__ import annotations

import datetime
import pathlib

from .base import Ctx, Outcome, fail, ok
from . import raw as raw_mod
from ..lib import lexical, reportkit
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

    try:
        totals = lexical.build_for_range(ctx.db.conn, book, lo, hi, verse_lo, verse_hi)
    except lexical.NotReady as e:
        return fail("lexical-not-ready", str(e), unready_codes=e.codes)
    ctx.db.conn.commit()

    removed_note = (f", {totals['removed_with_live_notes']} with live notes now dangling — "
                    f"see report.lexical_exceptions" if totals["removed_with_live_notes"] else "")
    return ok(
        f"{book} {lo}-{hi}: {totals['verses']} verse(s), {totals['spans']} span(s), "
        f"{totals['codes']} code(s) resolved ({totals['inserted']} inserted, "
        f"{totals['updated']} updated, {totals['unchanged']} unchanged, "
        f"{totals['removed']} removed{removed_note}){backfill_note}",
        **totals)


# ── lexical.readiness — the 3-leg base-data readiness check (#1606) ────────────────────────────
# Read-only, always persists a report (governance.reports_must_persist), escalates only on a FATAL
# finding. Separate from spine.check: it also checks the cluster-allocation precondition Layer 1's
# `role` column depends on.
#
# Leg 1 -- every live verse has >=1 live span.
# Leg 2 -- every live span's strong_variant code resolves to a live `strong` row.
# Leg 3 -- every live `strong` that occurs in a live span has >=1 live `cluster_strong` allocation
#          (Layer 1's `role` is the JSON array of its cluster codes; an empty one is a hard failure
#          in lib/lexical.py `_check_role_readiness`).

def readiness(ctx: Ctx) -> Outcome:
    conn = ctx.db.conn

    leg1_count = conn.execute(
        "SELECT COUNT(*) FROM verse v WHERE v.deleted=0 AND NOT EXISTS ("
        "SELECT 1 FROM span s WHERE s.verse_id=v.id AND s.deleted=0)").fetchone()[0]
    leg1_sample = [r[0] for r in conn.execute(
        "SELECT v.osisId FROM verse v WHERE v.deleted=0 AND NOT EXISTS ("
        "SELECT 1 FROM span s WHERE s.verse_id=v.id AND s.deleted=0) LIMIT 15").fetchall()]

    span_codes: set[str] = set()
    for r in conn.execute(
            "SELECT strong_variant FROM span WHERE deleted=0 AND strong_variant IS NOT NULL "
            "AND strong_variant != ''"):
        span_codes.update(r[0].split())
    live_strong = {r[0] for r in conn.execute("SELECT strongNumber FROM strong WHERE deleted=0")}
    leg2_missing = sorted(span_codes - live_strong)

    allocated = {r[0] for r in conn.execute(
        "SELECT DISTINCT strong FROM cluster_strong WHERE deleted=0")}
    # cluster_strong.strong carries the exact suffixed code: compare exact codes, never the base
    occurring_live_strong = span_codes & live_strong
    leg3_missing = sorted(occurring_live_strong - allocated)

    findings = dict(leg1_count=leg1_count, leg1_sample=leg1_sample,
                     leg2_count=len(leg2_missing), leg2_sample=leg2_missing[:15],
                     leg3_count=len(leg3_missing), leg3_sample=leg3_missing[:15])
    report_path = _write_readiness_report(ctx, findings)
    fatal_count = findings["leg1_count"] + findings["leg2_count"] + findings["leg3_count"]

    if not fatal_count:
        return ok(f"lexical readiness sound: 0 FATAL findings across all 3 legs — report written "
                  f"to {report_path}", **findings)

    return fail("lexical-not-ready",
               f"{fatal_count} FATAL finding(s) — Leg1 (verse with no span): "
               f"{findings['leg1_count']}, Leg2 (span code with no strong row): "
               f"{findings['leg2_count']}, Leg3 (occurring strong with no cluster_strong "
               f"allocation): {findings['leg3_count']}. Full detail: {report_path}",
               **findings)


def _write_readiness_report(ctx: Ctx, findings: dict) -> pathlib.Path:
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    path = pathlib.Path(ctx.cfg.required_setting("lexical.readiness_report_path"))
    total = findings["leg1_count"] + findings["leg2_count"] + findings["leg3_count"]
    intro = [
        f"> Generated {now} by `lexical.readiness` (#1606, registered as a persisted check "
        f"2026-09-16, escalation #1706 Phase A). Precondition check for the Layer 1 rebuild -- "
        f"**{total} FATAL finding(s)** across all 3 legs.",
    ]
    sections = {
        "summary": [
            f"Leg 1 (verse with 0 live spans): **{findings['leg1_count']}**",
            f"Leg 2 (span strong_variant code with no live `strong` row): **{findings['leg2_count']}**",
            f"Leg 3 (occurring `strong` with no live `cluster_strong` allocation): "
            f"**{findings['leg3_count']}**",
        ],
        "detail": [
            f"**Leg 1 sample:** {findings['leg1_sample']}",
            f"**Leg 2 sample:** {findings['leg2_sample']}",
            f"**Leg 3 sample:** {findings['leg3_sample']}",
        ],
    }
    L = reportkit.render_scaffold(ctx.db.conn, "lexical.readiness", sections, intro=intro)
    return reportkit.write_report(ctx.db.conn, "lexical.readiness", path, L)
