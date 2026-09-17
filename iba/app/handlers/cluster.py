"""cluster.py — the `cluster-assign` work package: `cluster.assign` (DB-wide mechanical sweep,
calls `lib.strongreconcile.reconcile()` per unclassified/promotable strong) and `cluster.validate`
(read-only coverage + exception report, same shape as `lexicon.validate`).

Both standalone steps (like `lexicon-parse`'s own three) — each invoked independently, not chained.
See `backfill-cluster-triage-plan-v3-20260812.md` / `cluster-assign-build-spec-20260812.md`.
"""

from __future__ import annotations

import datetime
import pathlib

from .base import Ctx, Outcome, fail, ok, escalate
from ..lib import clusterstatus, escalation as esc, lexicalscope, recordingpass, reportkit
from ..lib import strongreconcile, subgroupgenerate


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
def _write_report(ctx: Ctx, counts: dict, unclassified: list[dict], no_word: list[dict],
                  sibling: list[dict]) -> pathlib.Path:
    path = pathlib.Path(ctx.cfg.required_setting("cluster.quality_report_path"))
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
        "unclassified": (
            [f"`{r['strongNumber']}` — {r['stepGloss']!r}" for r in unclassified]
            or ["(none)"]),
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
        "SELECT s.strongNumber, s.stepGloss FROM strong s WHERE s.deleted=0 AND NOT EXISTS "
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
    report_path = _write_report(ctx, counts, unclassified, no_word, sibling_rows)

    # escalation #1606, researcher instruction 2026-09-15: a plain unclassified count used to be
    # reported but never escalated on its own -- exactly why the 111-strong backlog went unnoticed
    # until a manual sweep found it. Now counts as a finding, same footing as the two named
    # exception shapes, not a separate lesser category.
    total_findings = len(unclassified) + len(no_word) + len(sibling_rows)
    if not total_findings:
        return ok(f"{total} strong(s) checked — 0 unclassified, "
                 f"{counts['not_promoted']} not-yet-promoted, 0 exceptions — "
                 f"report written to {report_path}", **counts)

    # escalation #1707, researcher instruction 2026-09-15, verbatim: "this report is as expected.
    # Can be signed off. This situation should no longer create an exception everytime it runs."
    # A fresh run_id every invocation meant a prior run's 'approved' could never be recognised by a
    # later run (answered_for_run below is scoped to THIS run only) -- checked here FIRST, across
    # every past run for this step: if the current findings don't exceed what was already approved,
    # acknowledge silently rather than re-raising the same known backlog. A genuine increase in any
    # count still escalates fresh, same as before.
    current = {"unclassified": len(unclassified), "no_word": len(no_word),
              "sibling_conflict": len(sibling_rows)}
    baseline = esc.answered_baseline_for_step(ctx.db, ctx.step_id, current)
    if baseline is not None:
        return ok(f"{total} strong(s) checked — {len(unclassified)} unclassified, "
                 f"{len(no_word)} no-word / {len(sibling_rows)} sibling-conflict finding(s), none "
                 f"exceeding the baseline already approved on escalation #{baseline['id']} — "
                 f"acknowledged automatically, not re-raised; report written to {report_path}",
                 **counts, no_word=len(no_word), sibling_conflict=len(sibling_rows))

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision, comment = answered["next_action"], answered["comment"]
        # escalation #798/#799 SS4: this is decision_required, so it's now resolved via Update()'s
        # manual vocabulary (approved/reject/revise/noted), not AnswerRun's dispatcher vocabulary
        # (approve/reject/revise/hold/noted) -- only 'approve'/'approved' differ in spelling
        # between the two, everything else already matches.
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {len(unclassified)} unclassified / {len(no_word)} no-word / "
                     f"{len(sibling_rows)} sibling-conflict finding(s) — researcher confirmed "
                     f"known/acceptable; full detail in {report_path}", **counts,
                     no_word=len(no_word), sibling_conflict=len(sibling_rows))
        from .base import fail
        if decision == "reject":
            return fail("findings-rejected",
                       "researcher flagged these exceptions as needing action",
                       **counts, no_word=len(no_word), sibling_conflict=len(sibling_rows))
        return fail("needs-revision", f"researcher comment: {comment or '(none)'}")

    return escalate(
        "needs-review",
        question=(f"Cluster-assignment findings: {len(unclassified)} `strong` row(s) have NO "
                 f"cluster assignment at all; {len(no_word)} strong(s) carry a non-T2 cluster "
                 f"with no word_registry link at all; {len(sibling_rows)} `backfill` strong(s) have "
                 f"an already-active or already-clustered sibling. None is auto-resolved — "
                 f"approve to acknowledge as current/known state, reject to flag for action, or "
                 f"revise with a comment. Full detail: {report_path}."),
        preset={"unclassified": len(unclassified), "no_word": len(no_word),
               "sibling_conflict": len(sibling_rows), "report_path": str(report_path)},
        tried="reconcile()'s own exception checks, run DB-wide across every backfill-origin strong "
              "with a cluster assignment",
        resolution_kind="decision_required")


def _may(ctx: Ctx, writer: str, table: str) -> None:
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


# ── subgroup (process b, the `char-subgroup` stage, #1690/#1693) ────────────────────────────────
#
# Whole-cluster, ONE LLM call, never batched (#1690 §2(a) requires the full member-strong set read
# before any assignment). `-Preview` (default true) assembles the payload and reports the cost
# estimate WITHOUT calling the API or writing anything -- same never-a-live-call-by-default
# discipline `lexical.meaning` established for a just-built, never-yet-run mechanism.
# `-Preview:$false` runs for real: one live API call, `lib/recordingpass.py:record_subgroups`
# writes the result in the same unit of work, then `cluster.status` advances to `ready_for_reading`.

def subgroup(ctx: Ctx) -> Outcome:
    _may(ctx, "cluster.subgroup", "cluster_subgroup")
    _may(ctx, "cluster.subgroup", "cluster_subgroup_strong")
    _may(ctx, "cluster.subgroup", "ib_observation")
    _may(ctx, "cluster.subgroup", "ib_node")

    cluster_code = ctx.params.get("ClusterCode")
    if not cluster_code:
        return fail("bad-selector", "-ClusterCode is required")
    preview_raw = ctx.params.get("Preview", "true")
    preview = str(preview_raw).strip().lower() not in ("false", "0", "no")

    conn = ctx.db.conn
    try:
        clusterstatus.require_ready_for_subgroup_allocation(conn, cluster_code)
    except ValueError as e:
        return fail("not-ready", str(e))

    try:
        member_strongs = lexicalscope.resolve_strongs(conn, cluster_code=cluster_code)
    except ValueError as e:
        return fail("bad-selector", str(e))
    if not member_strongs:
        return fail("no-strongs", f"{cluster_code} resolved to 0 member strongs")

    package = subgroupgenerate.assemble_cluster_package(ctx, cluster_code, member_strongs)
    max_cost = float(ctx.cfg.setting("cluster.subgroup_llm_max_cost", 2.00))
    if package["est_cost_usd"] > max_cost:
        return fail("cost-cap-exceeded",
                   f"{cluster_code} ({package['strong_count']} strongs) estimated cost "
                   f"${package['est_cost_usd']:.2f} exceeds cluster.subgroup_llm_max_cost "
                   f"(${max_cost:.2f}) -- raise the cap via configmaint.propose")

    if preview:
        return ok(f"PREVIEW {cluster_code}: {package['strong_count']} strong(s), estimated "
                 f"${package['est_cost_usd']:.4f} -- no API call made, nothing written. Re-run "
                 f"with -Preview:$false to execute for real.",
                 preview=True, cluster_code=cluster_code, strong_count=package["strong_count"],
                 est_cost_usd=package["est_cost_usd"])

    try:
        result = subgroupgenerate.call_api(ctx, package)
    except subgroupgenerate.ApiKeyMissing as e:
        return fail("api-key-missing", str(e))
    except subgroupgenerate.ApiCallFailed as e:
        return fail("api-error", str(e))
    rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
    rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
    real_cost = (result["input_tokens"] / 1_000_000 * rate_in +
                result["output_tokens"] / 1_000_000 * rate_out)
    subgroupgenerate.log_usage(ctx.cfg, ctx.run_id, "1/1", package["model"],
                               result["input_tokens"], result["output_tokens"], real_cost)

    try:
        parsed = subgroupgenerate.parse_response(result["text"])
    except subgroupgenerate.BadModelResponse as e:
        return fail("bad-model-response", str(e))

    try:
        written = recordingpass.record_subgroups(conn, cluster_code, member_strongs, parsed)
    except recordingpass.SubgroupWriteError as e:
        conn.rollback()
        return fail("bad-subgroup-output", str(e))

    # Observations captured via the SAME mechanism Stage 1 (`lexical.meaning`) already uses --
    # researcher correction, this session: placement_note is a comment on a placement, never the
    # observation itself; any substantive claim the LLM makes goes through record_batch exactly
    # like verse-reading's own observations do, stage='char-subgroup', not a bespoke promotion path.
    obs_summary = recordingpass.record_batch(
        conn, cluster_code, "char-subgroup", parsed, source_json_serial=1)
    conn.commit()

    status_result = clusterstatus.advance_after_subgroup_allocation(conn, cluster_code)
    conn.commit()

    anchor_note = (f", {len(written['unresolved_anchor_verses'])} unresolved anchor verse(s)"
                  if written["unresolved_anchor_verses"] else "")
    obs_note = (f", observations {obs_summary['by_action']}" if obs_summary["by_action"] else
               ", 0 observations")
    # The reasons themselves, not just the count -- run.outcome only ever persists this message
    # STRING, never the `counts` dict, so anything left out here is unrecoverable afterward.
    unresolved_obs_note = (
        f", {obs_summary['unresolved_occurrence_count']} unresolved observation occurrence(s): "
        f"{'; '.join(obs_summary['unresolved_detail'][:5])}"
        f"{' ...' if obs_summary['unresolved_occurrence_count'] > 5 else ''}"
        if obs_summary["unresolved_occurrence_count"] else "")
    return ok(f"{cluster_code}: {written['subgroups']} subgroup(s), {written['members']} member(s) "
             f"({written['flag_members']} FLAG), ${real_cost:.4f} spent{anchor_note}"
             f"{obs_note}{unresolved_obs_note}; cluster.status -> {status_result['status_after']}",
             preview=False, cluster_code=cluster_code, written=written,
             observations=obs_summary, status_result=status_result)
