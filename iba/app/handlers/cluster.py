"""cluster.py — the `cluster-assign` work package: `cluster.assign` (DB-wide mechanical sweep,
calls `lib.strongreconcile.reconcile()` per unclassified/promotable strong) and `cluster.validate`
(read-only coverage + exception report, same shape as `lexicon.validate`).

Both standalone steps (like `lexicon-parse`'s own three) — each invoked independently, not chained.
See `backfill-cluster-triage-plan-v3-20260812.md` / `cluster-assign-build-spec-20260812.md`.
"""

from __future__ import annotations

import datetime
import pathlib

from .base import Ctx, Outcome, ok, escalate
from ..lib import escalation as esc, reportkit, strongreconcile


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── assign (DB-wide mechanical sweep; also the promotion trigger for already-classified codes) ──
def assign(ctx: Ctx) -> Outcome:
    codes = [r["strongNumber"] for r in ctx.db.rows(
        "SELECT strongNumber FROM strong WHERE deleted=0 ORDER BY strongNumber")]
    tallies: dict[str, int] = {}
    for code in codes:
        r = strongreconcile.reconcile(ctx, code)
        tallies[r["status"]] = tallies.get(r["status"], 0) + 1

    parts = ", ".join(f"{k}: {v}" for k, v in sorted(tallies.items()))
    return ok(f"{len(codes)} strong(s) checked — {parts}", **tallies)


# ── validate (read-only; coverage + the two named exception shapes; always persists a report) ──
def _write_report(ctx: Ctx, counts: dict, no_word: list[dict], sibling: list[dict]) -> pathlib.Path:
    path = pathlib.Path(ctx.cfg.setting("cluster.quality_report_path",
                                       "iba/app/reports/cluster-assign.md"))
    intro = [
        f"> Generated {_now()} by `cluster.validate`. Read-only findings, not a gate.",
        "",
        f"- `strong` rows with no cluster assignment at all: **{counts['unclassified']}**",
        f"- `backfill`-origin, non-T2 assignment, not yet promoted (should be `word`): "
        f"**{counts['not_promoted']}**",
        f"- exception — non-T2 assignment with no `word_registry` link: **{len(no_word)}**",
        f"- exception — `backfill` code with an active/clustered sibling: **{len(sibling)}**",
    ]
    sections = {
        "summary": [
            f"{counts['total']} strong(s) checked",
            f"unclassified: {counts['unclassified']}",
            f"not yet promoted (backfill, non-T2, has a word): {counts['not_promoted']}",
            f"exception — no word: {len(no_word)}",
            f"exception — sibling conflict: {len(sibling)}",
        ],
        "exceptions_no_word": (
            [f"`{r['strong']}` — {r['stepGloss']!r}, cluster {r['cluster_code']}" for r in no_word]
            or ["(none)"]),
        "exceptions_sibling_conflict": (
            [f"`{r['strong']}` — {r['stepGloss']!r}, cluster {r['cluster_code']}" for r in sibling]
            or ["(none)"]),
    }
    L = reportkit.render_scaffold(ctx.db.conn, "cluster.validate", sections, intro=intro)
    path = reportkit.write_report(ctx.db.conn, "cluster.validate", path, L)
    return path


def validate(ctx: Ctx) -> Outcome:
    total = ctx.db.rows("SELECT COUNT(*) n FROM strong WHERE deleted=0")[0]["n"]

    unclassified = ctx.db.rows(
        "SELECT s.strongNumber FROM strong s WHERE s.deleted=0 AND NOT EXISTS "
        "(SELECT 1 FROM cluster_strong cs WHERE cs.strong = s.strongNumber AND cs.deleted=0)")

    # Both queries mirror reconcile()'s own needs_word test exactly (word-optional set — T2/T3 by
    # default, config-driven — 2026-08-12 correction: T3 is "by its nature ... not word specific",
    # only a real M-cluster/FLAG classification still needs a word_registry link).
    word_optional = strongreconcile._word_optional_clusters(ctx)
    backfill_non_t2 = ctx.db.rows(
        "SELECT s.strongNumber, s.stepGloss, s.origin FROM strong s WHERE s.deleted=0 AND EXISTS "
        "(SELECT 1 FROM cluster_strong cs WHERE cs.strong = s.strongNumber AND cs.deleted=0 "
        "AND cs.cluster_code != 'T2')")
    not_promoted, no_word = [], []
    for r in backfill_non_t2:
        codes = strongreconcile._cluster_codes(ctx, r["strongNumber"])
        needs_word = bool(codes - {"T2"} - word_optional)
        word_linked = ctx.db.count("word_strong", strong=r["strongNumber"], deleted=0) > 0
        if r["origin"] == "backfill" and needs_word and word_linked:
            not_promoted.append(r)
        if needs_word and not word_linked:
            no_word.append({"strong": r["strongNumber"], "stepGloss": r["stepGloss"],
                            "cluster_code": ",".join(sorted(codes))})

    sibling_rows = []
    for r in ctx.db.rows(
            "SELECT strongNumber, stepGloss FROM strong WHERE deleted=0 AND origin='backfill'"):
        if strongreconcile._sibling_conflict(ctx, r["strongNumber"]):
            cc = ",".join(sorted(strongreconcile._cluster_codes(ctx, r["strongNumber"])))
            sibling_rows.append({"strong": r["strongNumber"], "stepGloss": r["stepGloss"],
                                 "cluster_code": cc or "(none)"})

    counts = {"total": total, "unclassified": len(unclassified), "not_promoted": len(not_promoted)}
    report_path = _write_report(ctx, counts, no_word, sibling_rows)

    total_findings = len(no_word) + len(sibling_rows)
    if not total_findings:
        return ok(f"{total} strong(s) checked — {counts['unclassified']} unclassified, "
                 f"{counts['not_promoted']} not-yet-promoted, 0 exceptions — "
                 f"report written to {report_path}", **counts)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision, comment = answered["next_action"], answered["comment"]
        if decision == "approve":
            return ok(f"acknowledged: {len(no_word)} no-word / {len(sibling_rows)} sibling-conflict "
                     f"exception(s) — researcher confirmed known/acceptable; full detail in "
                     f"{report_path}", **counts, no_word=len(no_word), sibling_conflict=len(sibling_rows))
        from .base import fail
        if decision == "reject":
            return fail("findings-rejected",
                       "researcher flagged these exceptions as needing action",
                       **counts, no_word=len(no_word), sibling_conflict=len(sibling_rows))
        return fail("needs-revision", f"researcher comment: {comment or '(none)'}")

    return escalate(
        "needs-review",
        question=(f"Cluster-assignment exceptions: {len(no_word)} strong(s) carry a non-T2 cluster "
                 f"with no word_registry link at all; {len(sibling_rows)} `backfill` strong(s) have "
                 f"an already-active or already-clustered sibling. Neither is auto-resolved — "
                 f"approve to acknowledge as current/known state, reject to flag for action, or "
                 f"revise with a comment. Full detail: {report_path}."),
        preset={"no_word": len(no_word), "sibling_conflict": len(sibling_rows),
               "report_path": str(report_path)},
        tried="reconcile()'s own exception checks, run DB-wide across every backfill-origin strong "
              "with a cluster assignment")
