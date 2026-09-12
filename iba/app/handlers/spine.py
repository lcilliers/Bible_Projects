"""spine.py — the base-data spine check: verse/span/strong sync (FATAL per `cfg_method_rule`
spine-verse-span-strong-sync-fatal, escalation #1613, researcher ruling 2026-09-10).

**Parse-completeness check REMOVED 2026-09-11 (escalation #1681/#1684/#1686), researcher
instruction verbatim: "spine check must exclude parse tables, they are no longer valid/maintained."**
This check used to also treat a `strong_meaning_tree`/`strong_lexicon` row with no matching
`strong_meaning_parsed`/`strong_lsj_parsed`/`strong_mounce_parsed` row as FATAL
(`cfg_method_rule` spine-extended-meaning-parse-completeness-fatal, now retired/`active=0`) plus a
discoverability pass over the same parsed tables (M-code-tagged strongs in analyzed verses,
`word_strong` codes) missing parse. Root cause of the trigger: H1506's sole gloss ('part') was
dropped by a header-abbreviation collision during the 2026-09-10 lexicon.parse rerun (escalation
#1668) — investigated live and filed to #1681. Those three parse tables and the `lexicon.parse`
step were themselves marked inactive in cfg_table/cfg_step on 2026-09-10 (escalation #1668
resolution, #1675-1679) — frozen, never rebuilt again — so a FATAL/discoverability check against
them was checking a dead table, not live coverage. The meaning-completeness method is being
redesigned from scratch (escalation #1680, in progress under #1682); this check will get a real
replacement once that method is built, not before.

Read-only. Always persists a report (governance.reports_must_persist). Escalates only when a FATAL
finding exists.
"""

from __future__ import annotations

import datetime
import pathlib

from .base import Ctx, Outcome, ok, escalate
from ..lib import escalation as esc, reportkit


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_report(ctx: Ctx, findings: dict) -> pathlib.Path:
    path = pathlib.Path(ctx.cfg.required_setting("spine.quality_report_path"))
    intro = [
        f"> Generated {_now()} by `spine.check`. Read-only findings against the base-data spine "
        f"(`governance.base_data_spine`, escalation #1613, researcher ruling 2026-09-10) — verse "
        f"defines what's included, span defines how meaning is derived, strong is the operative "
        f"anchor. The strong -> extended-meaning-parse check that used to run here was REMOVED "
        f"2026-09-11 (escalation #1681/#1684/#1686) — it checked coverage against "
        f"strong_meaning_parsed/strong_lsj_parsed/strong_mounce_parsed, which were retired and "
        f"frozen on 2026-09-10 and are no longer maintained; see handlers/spine.py module "
        f"docstring for the full history. FATAL findings need action.",
        "",
        f"- **FATAL** verse/span/strong desync (span-referenced codes with no live `strong` row): "
        f"**{findings['desync_count']}**",
    ]
    sections = {
        "summary": [
            f"{findings['desync_count']} verse/span/strong desync (FATAL)",
        ],
        "integrity": [
            f"**verse/span/strong sync** — {findings['desync_count']} code(s) a live `span` row "
            f"actually names with no live `strong` row. Sample: {findings['desync_sample']}",
        ],
    }
    L = reportkit.render_scaffold(ctx.db.conn, "spine.check", sections, intro=intro)
    return reportkit.write_report(ctx.db.conn, "spine.check", path, L)


def check(ctx: Ctx) -> Outcome:
    db = ctx.db

    span_codes = set()
    for r in db.rows("SELECT strong_variant FROM span WHERE deleted=0 AND strong_variant IS NOT "
                      "NULL AND strong_variant != ''"):
        span_codes.update(r["strong_variant"].split())
    live_strong = {r["strongNumber"] for r in db.rows("SELECT strongNumber FROM strong WHERE deleted=0")}
    desync = sorted(span_codes - live_strong)

    findings = dict(desync_count=len(desync), desync_sample=desync[:15])
    report_path = _write_report(ctx, findings)

    fatal_count = findings["desync_count"]

    if not fatal_count:
        return ok(f"spine sound: 0 fatal findings — report written to {report_path}",
                  fatal_count=0)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision, comment = answered["next_action"], answered["comment"]
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {fatal_count} FATAL spine finding(s) — researcher confirmed "
                      f"known/tracked, not fixed here; full detail in {report_path}",
                      fatal_count=fatal_count)
        if decision == "reject":
            from .base import fail
            return fail("spine-fatal-rejected",
                       "researcher flagged these FATAL spine findings as needing action",
                       fatal_count=fatal_count)
        from .base import fail
        return fail("needs-revision", f"researcher comment: {comment or '(none)'}")

    return escalate(
        "spine-fatal-found",
        question=(f"Spine check found {fatal_count} FATAL finding(s) — per "
                 f"governance.base_data_spine, a verse/span/strong desync must be fixed on "
                 f"discovery, not merely acknowledged. {findings['desync_count']} span-strong "
                 f"desync. Approve only to acknowledge as currently tracked (the 409-code desync "
                 f"is already known, open per escalation #1613); reject to require a fix; revise "
                 f"with a comment. Full detail: {report_path}."),
        preset={"fatal_count": fatal_count, "report_path": str(report_path)},
        tried="verse/span/strong set-difference against the live spine tables, per escalation "
              "#1613 section17's own method",
        resolution_kind="decision_required")
