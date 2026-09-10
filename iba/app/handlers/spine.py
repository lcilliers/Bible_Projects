"""spine.py — the base-data spine check: verse/span/strong sync + strong-extended-meaning-parse
completeness (both FATAL per `cfg_method_rule` spine-verse-span-strong-sync-fatal /
spine-extended-meaning-parse-completeness-fatal, escalation #1613, researcher ruling 2026-09-10),
plus a discoverability pass over what's NOT yet pulled/parsed for the two places that matter most
right now: M-code-tagged strongs in verses that have already had Layer 2 analysis, and every
strong a registered study word actually claims (`word_strong`).

Read-only. Always persists a report (governance.reports_must_persist). Escalates only when a FATAL
finding exists — the discoverability counts are informational (they name backlog for the
trigger-on-discovery mechanism `spine-on-demand-pull-mechanism` describes, not yet built) and never
gate on their own.

**Known interim choice, not yet the real thing (see `governance.base_data_spine`,
`cfg_method_rule` spine-on-demand-pull-mechanism, and `iba/docs/1451-window1-layer2-verse-scoped-
redesign-v1-20260905.md`'s own open item):** "a verse subjected to analysis" is computed directly
here as "has >=1 live `verse_lexical_note` row" — `verse_meta.lexical_complete_at` exists for
exactly this (added by #1608) but is not populated by anything live (`lib/lexicalenrich.py:
set_lexical_complete` has been dead code since #1451's verse-scoped redesign). Populating that
column for real — deciding what "every applicable code has a disposition" means at verse grain —
is a separate, still-undesigned decision this check does not make; it uses the direct query so the
report works today, and should switch to reading the column once that decision is made and built.
"""

from __future__ import annotations

import datetime
import pathlib

from .base import Ctx, Outcome, ok, escalate
from ..lib import escalation as esc, reportkit


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _base(code: str) -> str:
    """Strip a trailing sub-entry letter (H0639G -> H0639) — the lemma_key shape."""
    return code[:-1] if code and code[-1].isalpha() and code[:-1] else code


def _write_report(ctx: Ctx, findings: dict) -> pathlib.Path:
    path = pathlib.Path(ctx.cfg.required_setting("spine.quality_report_path"))
    intro = [
        f"> Generated {_now()} by `spine.check`. Read-only findings against the base-data spine "
        f"(`governance.base_data_spine`, escalation #1613, researcher ruling 2026-09-10) — verse "
        f"defines what's included, span defines how meaning is derived, strong is the operative "
        f"anchor; these three plus the extended-meaning/parse layer below `strong` must stay in "
        f"sync. FATAL findings need action; discoverability findings are backlog, not a gate.",
        "",
        f"- **FATAL** verse/span/strong desync (span-referenced codes with no live `strong` row): "
        f"**{findings['desync_count']}**",
        f"- **FATAL** strong_meaning_tree lemma with no strong_meaning_parsed row: "
        f"**{findings['tree_gap_count']}**",
        f"- **FATAL** strong_lexicon text with no matching lsj/mounce parse: "
        f"**{findings['lex_gap_count']}**",
        f"- discoverability: M-code strongs in analyzed verses missing parse: "
        f"**{findings['mcode_missing_count']}**",
        f"- discoverability: word_strong strongs missing parse: "
        f"**{findings['ws_missing_count']}**",
    ]
    sections = {
        "summary": [
            f"{findings['desync_count']} verse/span/strong desync (FATAL)",
            f"{findings['tree_gap_count']} + {findings['lex_gap_count']} strong-meaning-parse "
            f"break (FATAL)",
            f"{findings['mcode_missing_count']} M-code strongs in analyzed verses missing parse "
            f"(discoverability)",
            f"{findings['ws_missing_count']} word_strong strongs missing parse (discoverability)",
        ],
        "integrity": [
            f"**verse/span/strong sync** — {findings['desync_count']} code(s) a live `span` row "
            f"actually names with no live `strong` row. Sample: {findings['desync_sample']}",
            "",
            f"**strong -> extended meaning -> parse** — {findings['tree_gap_count']} "
            f"`strong_meaning_tree` lemma(s) with no `strong_meaning_parsed` row "
            f"({findings['tree_gap_sample']}); {findings['lex_gap_count']} `strong_lexicon` "
            f"row(s) with real lsj/mounce text but no matching parsed row "
            f"({findings['lex_gap_sample']}).",
        ],
        "discoverability": [
            f"**M-code strongs in analyzed verses, missing parse** ({findings['mcode_missing_count']}"
            f", of {findings['analyzed_verse_count']} verse(s) with live Layer-2 notes): "
            f"{findings['mcode_missing_sample']}",
            "",
            f"**word_strong strongs missing parse** ({findings['ws_missing_count']} of "
            f"{findings['ws_total']} distinct linked codes): {findings['ws_missing_sample']}",
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

    tree_lemmas = {r["lemma_key"] for r in
                   db.rows("SELECT DISTINCT lemma_key FROM strong_meaning_tree WHERE deleted=0")}
    parsed_lemmas = {r["lemma_key"] for r in
                     db.rows("SELECT DISTINCT lemma_key FROM strong_meaning_parsed WHERE deleted=0")}
    tree_gap = sorted(tree_lemmas - parsed_lemmas)

    has_lsj, has_mounce = set(), set()
    for r in db.rows("SELECT strong, lsj, mounce FROM strong_lexicon WHERE deleted=0"):
        if r["lsj"] and r["lsj"].strip():
            has_lsj.add(r["strong"])
        if r["mounce"] and r["mounce"].strip():
            has_mounce.add(r["strong"])
    lsj_parsed = {r["strong"] for r in db.rows("SELECT DISTINCT strong FROM strong_lsj_parsed WHERE deleted=0")}
    mounce_parsed = {r["strong"] for r in db.rows("SELECT DISTINCT strong FROM strong_mounce_parsed WHERE deleted=0")}
    lex_gap = sorted((has_lsj - lsj_parsed) | (has_mounce - mounce_parsed))

    def has_parse(code: str) -> bool:
        return _base(code) in parsed_lemmas or code in lsj_parsed or code in mounce_parsed

    analyzed_verses = [r["verse_id"] for r in
                       db.rows("SELECT DISTINCT verse_id FROM verse_lexical_note WHERE deleted=0")]
    mcode_strongs = {r["strong"] for r in
                     db.rows("SELECT DISTINCT strong FROM cluster_strong WHERE deleted=0 AND "
                             "cluster_code LIKE 'M%'")}
    analyzed_codes = set()
    if analyzed_verses:
        ph = ",".join("?" * len(analyzed_verses))
        analyzed_codes = {r["strong"] for r in
                          db.rows(f"SELECT DISTINCT strong FROM verse_lexical WHERE deleted=0 AND "
                                  f"verse_id IN ({ph})", tuple(analyzed_verses))
                          if r["strong"]}
    mcode_missing = sorted(c for c in (analyzed_codes & mcode_strongs) if not has_parse(c))

    ws_codes = {r["strong"] for r in db.rows("SELECT DISTINCT strong FROM word_strong")}
    ws_missing = sorted(c for c in ws_codes if c in live_strong and not has_parse(c))

    findings = dict(
        desync_count=len(desync), desync_sample=desync[:15],
        tree_gap_count=len(tree_gap), tree_gap_sample=tree_gap[:15],
        lex_gap_count=len(lex_gap), lex_gap_sample=lex_gap[:15],
        mcode_missing_count=len(mcode_missing), mcode_missing_sample=mcode_missing[:15],
        analyzed_verse_count=len(analyzed_verses),
        ws_missing_count=len(ws_missing), ws_missing_sample=ws_missing[:15], ws_total=len(ws_codes),
    )
    report_path = _write_report(ctx, findings)

    fatal_count = findings["desync_count"] + findings["tree_gap_count"] + findings["lex_gap_count"]
    discoverability_count = findings["mcode_missing_count"] + findings["ws_missing_count"]

    if not fatal_count:
        return ok(f"spine sound: 0 fatal findings. {discoverability_count} discoverability "
                  f"finding(s) (M-code-in-analyzed-verse + word_strong, missing parse, backlog "
                  f"not a gate) — report written to {report_path}",
                  fatal_count=0, discoverability_count=discoverability_count)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision, comment = answered["next_action"], answered["comment"]
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {fatal_count} FATAL spine finding(s) — researcher confirmed "
                      f"known/tracked, not fixed here; full detail in {report_path}",
                      fatal_count=fatal_count, discoverability_count=discoverability_count)
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
                 f"governance.base_data_spine, a verse/span/strong desync or a strong-meaning-"
                 f"parse break must be fixed on discovery, not merely acknowledged. "
                 f"{findings['desync_count']} span-strong desync, {findings['tree_gap_count']}+"
                 f"{findings['lex_gap_count']} meaning-parse break. Approve only to acknowledge as "
                 f"currently tracked (the 409-code desync is already known, open per escalation "
                 f"#1613); reject to require a fix; revise with a comment. Full detail: "
                 f"{report_path}."),
        preset={"fatal_count": fatal_count, "discoverability_count": discoverability_count,
               "report_path": str(report_path)},
        tried="verse/span/strong set-difference + lemma/parse NOT-EXISTS checks against the live "
              "spine tables, per escalation #1613 section17's own method",
        resolution_kind="decision_required")
