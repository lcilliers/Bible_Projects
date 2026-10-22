"""lexical.py — dispatcher handler for the lexical steps.

  lexical.build: the -Book + range adapter over `lib/lexical.py` (verse resolution and the
    write-grant check here; the writes in that module). Verse-scoped: no `passage` row is
    resolved or required (#1451). Auto-backfill as in report.verse_span_meaning
    (`report.auto_backfill_before_render`, `raw.backfill_meaning_for`).
  lexical.readiness: the 3-leg base-data readiness check (#1606).
  lexical.meaning / lexical.relational: the verse-reading stage against ib_observation/ib_node
    (word-level, then relational; #1706, #1860).
"""

from __future__ import annotations

import csv
import datetime
import json
import pathlib
import sys

from .base import Ctx, Outcome, fail, ok
from . import raw as raw_mod
from ..lib import lexical, lexicalscope, reportkit
from ..lib import batchcontrol, clusterstatus, recordingpass, stage1coverage, versereadinggenerate
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



# ── lexical.meaning — the verse-reading stage (#1706) ───────────────────────────────────────────
# Per-cluster, pre-subgroup, against ib_observation/ib_node. `-Preview` (default true) assembles
# every batch and reports the cost estimate without calling the API or writing. `-Preview:$false`
# runs for real: a live API call per batch, `lib/recordingpass.py` writing each result in the same
# unit of work.

def _chunk_verses_fixed_size(verse_ids: list[int], max_verses: int) -> list[list[int]]:
    """Fixed-size groups of verse_ids in the caller's order, never reordered or split mid-verse.
    The unit of operation is verses, not strongs (#1842); a failure is bounded to one batch."""
    if not verse_ids:
        return []
    return [verse_ids[i:i + max_verses] for i in range(0, len(verse_ids), max_verses)]


def _chunk_verses_by_strong_density(conn, verse_ids: list[int], max_strongs: int
                                    ) -> list[list[int]]:
    """Not called: superseded by `_chunk_verses_fixed_size` (#1842). Grouped verse_ids into chunks
    whose cumulative distinct M-code strong count stays <= max_strongs."""
    if not verse_ids:
        return []
    ph = ",".join("?" * len(verse_ids))
    rows = conn.execute(
        f"SELECT verse_id, strong, role FROM verse_lexical "
        f"WHERE verse_id IN ({ph}) AND deleted=0", verse_ids).fetchall()
    strongs_by_verse: dict[int, set[str]] = {}
    for r in rows:
        if not r["strong"]:
            continue
        roles = json.loads(r["role"]) if r["role"] else []
        if any(c.startswith("M") for c in roles):
            strongs_by_verse.setdefault(r["verse_id"], set()).add(r["strong"])

    chunks: list[list[int]] = []
    current: list[int] = []
    current_strongs: set[str] = set()
    for vid in verse_ids:
        v_strongs = strongs_by_verse.get(vid, set())
        projected = current_strongs | v_strongs
        if current and len(projected) > max_strongs:
            chunks.append(current)
            current, current_strongs = [vid], set(v_strongs)
        else:
            current.append(vid)
            current_strongs = projected
    if current:
        chunks.append(current)
    oversized = [c for c in chunks if len(c) == 1 and len(strongs_by_verse.get(c[0], set())) > max_strongs]
    if oversized:
        print(f"NOTE: {len(oversized)} single-verse chunk(s) individually exceed "
             f"max_strongs={max_strongs} on their own -- not split further, still a truncation "
             f"risk: verse_ids {[c[0] for c in oversized]}", file=sys.stderr)
    return chunks


def meaning(ctx: Ctx) -> Outcome:
    _may(ctx, "lexical.meaning", "ib_observation")
    _may(ctx, "lexical.meaning", "ib_node")
    _may(ctx, "lexical.meaning", "run_batch")

    cluster_code = ctx.params.get("ClusterCode")
    if not cluster_code:
        return fail("bad-selector", "-ClusterCode is required")
    # ctx.params values are strings: "false"/"0"/"" are off; missing means preview on
    preview_raw = ctx.params.get("Preview", "true")
    preview = str(preview_raw).strip().lower() not in ("false", "0", "no")
    # -Force: a deliberate reconciliation rerun bypasses batchcontrol.already_committed's skip; the only
    # lever that corrects existing ib_observation rows (via fresh output). Off unless set.
    force_raw = ctx.params.get("Force", "false")
    force = str(force_raw).strip().lower() in ("true", "1", "yes")

    conn = ctx.db.conn
    try:
        strongs = lexicalscope.resolve_strongs(conn, cluster_code=cluster_code)
    except ValueError as e:
        return fail("bad-selector", str(e))
    # -VerseList narrows which of this cluster's verses to run (e.g. a cheap test on a few verses);
    # -ClusterCode is still required for member strongs, prompt framing and the relational vantage
    verse_list_raw = ctx.params.get("VerseList")
    if verse_list_raw:
        refs = [x.strip() for x in verse_list_raw.split(",") if x.strip()]
        try:
            verse_ids = lexicalscope.resolve_verse_ids_for_refs(conn, refs)
        except ValueError as e:
            return fail("bad-selector", str(e))
    else:
        verse_ids = lexicalscope.resolve_verse_ids_for_strongs(conn, strongs)
    if not verse_ids:
        return fail("no-verses", f"{cluster_code} resolved to 0 verses")

    # freshness gate (#1719): refuse if Layer 1 role data is stale against current cluster_strong
    # membership. Hard stop, never a partial run.
    stale = lexical.stale_role_strongs_for_cluster(conn, cluster_code, strongs)
    if stale:
        return fail("layer1-stale",
                   f"{len(stale)} of {len(strongs)} member strong(s) have live verse_lexical rows "
                   f"that never carry {cluster_code!r} in role, despite cluster_strong currently "
                   f"listing them as members -- Layer 1 is stale for this cluster (#1719). Re-run "
                   f"lexical.build for the verses containing these strongs before verse-reading: "
                   f"{stale}")

    # whole-verse exclusion (#1824): the first cluster's pass to touch a verse analyses every M-code
    # word in it, so a later cluster does not re-derive it. -Force bypasses this.
    fully_covered_ids: set = set()
    if not force:
        fully_covered_ids = stage1coverage.fully_covered_verse_ids(
            conn, cluster_code, verse_ids, family="word_level")
        if fully_covered_ids:
            verse_ids = [v for v in verse_ids if v not in fully_covered_ids]
    if not verse_ids:
        return ok(f"{cluster_code}: all {len(fully_covered_ids)} requested verse(s) are already "
                 f"fully covered (every expected question answered by an earlier pass) -- "
                 f"nothing to do. Use -Force to re-examine them anyway.",
                 preview=preview, cluster_code=cluster_code,
                 fully_covered_verse_count=len(fully_covered_ids))

    # fixed verse-count chunking (#1842)
    max_verses = int(ctx.cfg.setting("lexical.meaning_max_verses_per_batch", 1))
    max_cost_per_batch = float(ctx.cfg.setting("lexical.llm_max_cost_per_batch", 1.00))
    chunks = _chunk_verses_fixed_size(verse_ids, max_verses)

    batch_summaries = []
    llm_summary = []
    record_summary = {"by_action": {}, "unresolved_occurrence_count": 0, "unresolved_detail": []}
    skipped_batches = 0

    for idx, chunk in enumerate(chunks):
        chunk_label = f"{idx + 1}/{len(chunks)}"
        package = versereadinggenerate.assemble_word_level_batch_package(
            ctx, cluster_code, chunk, force=force)
        content_key = batchcontrol.content_key([str(v) for v in chunk])
        already_done = batchcontrol.already_committed(
            conn, "lexical.meaning", cluster_code, content_key)
        batch_summaries.append({
            "chunk": chunk_label, "verses": package["verse_count"],
            "cluster_member_strongs": package["cluster_member_strong_count"],
            "est_input_tokens": package["est_input_tokens"],
            "est_cost_usd": package["est_cost_usd"],
            "already_committed": already_done})
        if package["est_cost_usd"] > max_cost_per_batch:
            return fail("cost-cap-exceeded",
                       f"chunk {chunk_label} ({package['verse_count']} verses) estimated cost "
                       f"${package['est_cost_usd']:.2f} exceeds lexical.llm_max_cost_per_batch "
                       f"(${max_cost_per_batch:.2f}) -- raise the cap via configmaint.propose or "
                       f"narrow the selector")
        if preview:
            continue

        # resume/skip (#1756): a batch already committed (matched by content, checked fresh) is not
        # re-paid; -Force overrides
        if already_done and not force:
            skipped_batches += 1
            continue

        batch_id = batchcontrol.start_batch(
            conn, ctx.run_id, "verse-lexical", "lexical.meaning", cluster_code, idx + 1,
            content_key)
        try:
            try:
                result = versereadinggenerate.call_api(ctx, package)
            except versereadinggenerate.ApiKeyMissing as e:
                batchcontrol.fail_batch(conn, batch_id, str(e))
                return fail("api-key-missing", str(e))
            except versereadinggenerate.ApiCallFailed as e:
                batchcontrol.fail_batch(conn, batch_id, str(e))
                return fail("api-error", f"chunk {chunk_label}: {e}")
            rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
            rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
            real_cost = (result["input_tokens"] / 1_000_000 * rate_in +
                        result["output_tokens"] / 1_000_000 * rate_out)
            versereadinggenerate.log_usage(
                ctx.cfg, ctx.run_id, chunk_label, package["model"], result["input_tokens"],
                result["output_tokens"], real_cost)
            llm_summary.append({"chunk": chunk_label, "verses": package["verse_count"],
                                "input_tokens": result["input_tokens"],
                                "output_tokens": result["output_tokens"],
                                "cost_usd": round(real_cost, 4)})

            try:
                parsed = versereadinggenerate.parse_response(result["text"])
            except versereadinggenerate.BadModelResponse as e:
                conn.rollback()
                batchcontrol.fail_batch(conn, batch_id, f"bad-model-response: {e}")
                return fail("bad-model-response", f"chunk {chunk_label}: {e}")

            chunk_record = recordingpass.record_batch(
                conn, cluster_code, "verse-reading", parsed, source_json_serial=idx + 1,
                similarity_threshold=float(ctx.cfg.setting("cluster.recording_similarity_threshold", 0.85)))
            conn.commit()
        except Exception as e:
            # crash safeguard (#1756): record any exception in the risky window before re-raising, so a
            # run_batch row left at 'running' means only a real process death
            batchcontrol.fail_batch(conn, batch_id, f"{type(e).__name__}: {e}")
            raise
        batchcontrol.commit_batch(conn, batch_id, cost_usd=round(real_cost, 4))
        for action, n in chunk_record["by_action"].items():
            record_summary["by_action"][action] = record_summary["by_action"].get(action, 0) + n
        record_summary["unresolved_occurrence_count"] += chunk_record["unresolved_occurrence_count"]
        record_summary["unresolved_detail"] += chunk_record["unresolved_detail"]

    if preview:
        already_n = sum(1 for b in batch_summaries if b["already_committed"])
        # cost: only uncommitted batches, unless -Force re-calls every batch
        total_cost = sum(b["est_cost_usd"] for b in batch_summaries
                         if force or not b["already_committed"])
        already_note = ("" if not already_n else
                        f", {already_n} of {len(chunks)} already committed by a prior run "
                        f"({'will be RE-RUN, -Force is set' if force else 'will be skipped'})")
        fully_covered_note = (f", {len(fully_covered_ids)} verse(s) excluded entirely (already "
                             f"fully covered by an earlier pass)" if fully_covered_ids else "")
        return ok(f"PREVIEW {cluster_code}: {len(chunks)} batch(es), {len(verse_ids)} verse(s), "
                 f"{len(strongs)} strong(s), estimated ${total_cost:.4f} total for the "
                 f"{'forced re-run' if force else 'remaining work'}{already_note}"
                 f"{fully_covered_note} -- no API call "
                 f"made, nothing written. Re-run with -Preview:$false to execute for real.",
                 preview=True, batches=batch_summaries, cluster_code=cluster_code,
                 verse_count=len(verse_ids), strong_count=len(strongs), force=force)

    # cluster.status advances in relational(), the final verse-reading stage (#1860)

    # LLM validation check (#1824): expected vs received word-level rows over the full requested
    # scope, read-only. Per-row detail goes to a report; the summary counts go into the message, the
    # only part run.outcome keeps.
    coverage = stage1coverage.validate_coverage(conn, cluster_code, verse_ids, family="word_level")
    # report path from config (report.stage1_coverage_validation_pattern)
    coverage_pattern = ctx.cfg.required_setting("report.stage1_coverage_validation_pattern")
    coverage_report_path = pathlib.Path(
        coverage_pattern.format(cluster_code=cluster_code, run_id=ctx.run_id))
    coverage_report_path.parent.mkdir(parents=True, exist_ok=True)
    with coverage_report_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["category", "verse_reference", "strong", "question_code", "live_node_count"])
        for v, s, q in coverage["missing_sample"]:
            w.writerow(["MISSING", v, s, q, 0])
        for v, s, q in coverage["unexpected_sample"]:
            w.writerow(["UNEXPECTED", v, s, q, ""])
        for (v, s, q), n in coverage["over_count_sample"]:
            w.writerow(["OVER_COUNT", v, s, q, n])
    coverage_note = (f"; validation: {coverage['ok_count']} ok, {coverage['missing_count']} "
                     f"missing, {coverage['unexpected_count']} unexpected, "
                     f"{coverage['over_count_count']} over-count (of {coverage['expected_count']} "
                     f"expected) -- {coverage_report_path}")

    total_cost = sum(c["cost_usd"] for c in llm_summary)
    unresolved_n = record_summary["unresolved_occurrence_count"]
    # the reasons themselves go into the message: run.outcome keeps only the message string
    unresolved_note = (f", {unresolved_n} unresolved occurrence(s): "
                       f"{'; '.join(record_summary['unresolved_detail'][:5])}"
                       f"{' ...' if unresolved_n > 5 else ''}") if unresolved_n else ""
    skipped_note = f", {skipped_batches} batch(es) skipped (already committed)" if skipped_batches else ""
    fully_covered_note = (f", {len(fully_covered_ids)} verse(s) excluded entirely (already fully "
                         f"covered by an earlier pass)" if fully_covered_ids else "")
    return ok(f"{cluster_code}: {len(chunks)} batch(es){skipped_note}{fully_covered_note}, "
             f"${total_cost:.4f} spent, "
             f"observations {record_summary['by_action']}{unresolved_note}"
             f"{coverage_note}; word-level only -- run lexical.relational next for this cluster",
             preview=False, batches=batch_summaries, llm_calls=llm_summary,
             record_summary=record_summary, cluster_code=cluster_code,
             skipped_batches=skipped_batches, coverage=coverage,
             fully_covered_verse_count=len(fully_covered_ids))


def relational(ctx: Ctx) -> Outcome:
    """`lexical.relational` (#1860): the relational questions (M0.6.5/M0.6.6/D7.7.1/M0.7.1-16/
    M0.8.1). Same batch/cost/resume/coverage-validation structure as `meaning()`, plus: (1) a hard
    readiness gate refusing any verse whose M-code words lack committed word-level observations;
    (2) the `cluster.status` `t_cluster_assignment_completed -> ready_for_subgroup_allocation`
    transition, since this is the final stage of verse-reading."""
    _may(ctx, "lexical.relational", "ib_observation")
    _may(ctx, "lexical.relational", "ib_node")
    _may(ctx, "lexical.relational", "run_batch")

    cluster_code = ctx.params.get("ClusterCode")
    if not cluster_code:
        return fail("bad-selector", "-ClusterCode is required")
    preview_raw = ctx.params.get("Preview", "true")
    preview = str(preview_raw).strip().lower() not in ("false", "0", "no")
    force_raw = ctx.params.get("Force", "false")
    force = str(force_raw).strip().lower() in ("true", "1", "yes")

    conn = ctx.db.conn
    try:
        strongs = lexicalscope.resolve_strongs(conn, cluster_code=cluster_code)
    except ValueError as e:
        return fail("bad-selector", str(e))
    verse_list_raw = ctx.params.get("VerseList")
    if verse_list_raw:
        refs = [x.strip() for x in verse_list_raw.split(",") if x.strip()]
        try:
            verse_ids = lexicalscope.resolve_verse_ids_for_refs(conn, refs)
        except ValueError as e:
            return fail("bad-selector", str(e))
    else:
        verse_ids = lexicalscope.resolve_verse_ids_for_strongs(conn, strongs)
    if not verse_ids:
        return fail("no-verses", f"{cluster_code} resolved to 0 verses")

    stale = lexical.stale_role_strongs_for_cluster(conn, cluster_code, strongs)
    if stale:
        return fail("layer1-stale",
                   f"{len(stale)} of {len(strongs)} member strong(s) have live verse_lexical rows "
                   f"that never carry {cluster_code!r} in role, despite cluster_strong currently "
                   f"listing them as members -- Layer 1 is stale for this cluster (#1719). Re-run "
                   f"lexical.build for the verses containing these strongs before verse-reading: "
                   f"{stale}")

    # readiness gate (#1860): relational grounds on committed word-level findings, so a verse
    # without them stops the run
    if not force:
        gaps = stage1coverage.missing_word_level_coverage(conn, cluster_code, verse_ids)
        if gaps:
            sample = gaps[:15]
            return fail("word-level-incomplete",
                       f"{len(gaps)} (verse, strong) word-level gap(s) in the requested scope -- "
                       f"lexical.relational refuses to run until every M-code word has a committed "
                       f"lexical.meaning observation. Run lexical.meaning for {cluster_code} (or "
                       f"the relevant verses) first. Sample: "
                       f"{[(g['verse_reference'], g['strong']) for g in sample]}"
                       f"{' ...' if len(gaps) > 15 else ''}")

    fully_covered_ids: set = set()
    if not force:
        fully_covered_ids = stage1coverage.fully_covered_verse_ids(
            conn, cluster_code, verse_ids, family="relational")
        if fully_covered_ids:
            verse_ids = [v for v in verse_ids if v not in fully_covered_ids]
    if not verse_ids:
        return ok(f"{cluster_code}: all {len(fully_covered_ids)} requested verse(s) are already "
                 f"fully covered (every expected question answered by an earlier pass) -- "
                 f"nothing to do. Use -Force to re-examine them anyway.",
                 preview=preview, cluster_code=cluster_code,
                 fully_covered_verse_count=len(fully_covered_ids))

    max_verses = int(ctx.cfg.setting("lexical.relational_max_verses_per_batch", 1))
    max_cost_per_batch = float(ctx.cfg.setting("lexical.llm_max_cost_per_batch", 1.00))
    chunks = _chunk_verses_fixed_size(verse_ids, max_verses)

    batch_summaries = []
    llm_summary = []
    record_summary = {"by_action": {}, "unresolved_occurrence_count": 0, "unresolved_detail": []}
    skipped_batches = 0

    for idx, chunk in enumerate(chunks):
        chunk_label = f"{idx + 1}/{len(chunks)}"
        package = versereadinggenerate.assemble_relational_batch_package(
            ctx, cluster_code, chunk, force=force)
        content_key = batchcontrol.content_key([str(v) for v in chunk])
        already_done = batchcontrol.already_committed(
            conn, "lexical.relational", cluster_code, content_key)
        batch_summaries.append({
            "chunk": chunk_label, "verses": package["verse_count"],
            "cluster_member_strongs": package["cluster_member_strong_count"],
            "est_input_tokens": package["est_input_tokens"],
            "est_cost_usd": package["est_cost_usd"],
            "already_committed": already_done})
        if package["est_cost_usd"] > max_cost_per_batch:
            return fail("cost-cap-exceeded",
                       f"chunk {chunk_label} ({package['verse_count']} verses) estimated cost "
                       f"${package['est_cost_usd']:.2f} exceeds lexical.llm_max_cost_per_batch "
                       f"(${max_cost_per_batch:.2f}) -- raise the cap via configmaint.propose or "
                       f"narrow the selector")
        if preview:
            continue

        if already_done and not force:
            skipped_batches += 1
            continue

        batch_id = batchcontrol.start_batch(
            conn, ctx.run_id, "verse-lexical", "lexical.relational", cluster_code, idx + 1,
            content_key)
        try:
            try:
                result = versereadinggenerate.call_api(ctx, package)
            except versereadinggenerate.ApiKeyMissing as e:
                batchcontrol.fail_batch(conn, batch_id, str(e))
                return fail("api-key-missing", str(e))
            except versereadinggenerate.ApiCallFailed as e:
                batchcontrol.fail_batch(conn, batch_id, str(e))
                return fail("api-error", f"chunk {chunk_label}: {e}")
            rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
            rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
            real_cost = (result["input_tokens"] / 1_000_000 * rate_in +
                        result["output_tokens"] / 1_000_000 * rate_out)
            versereadinggenerate.log_usage(
                ctx.cfg, ctx.run_id, chunk_label, package["model"], result["input_tokens"],
                result["output_tokens"], real_cost)
            llm_summary.append({"chunk": chunk_label, "verses": package["verse_count"],
                                "input_tokens": result["input_tokens"],
                                "output_tokens": result["output_tokens"],
                                "cost_usd": round(real_cost, 4)})

            try:
                parsed = versereadinggenerate.parse_response(result["text"])
            except versereadinggenerate.BadModelResponse as e:
                conn.rollback()
                batchcontrol.fail_batch(conn, batch_id, f"bad-model-response: {e}")
                return fail("bad-model-response", f"chunk {chunk_label}: {e}")

            chunk_record = recordingpass.record_batch(
                conn, cluster_code, "verse-reading", parsed, source_json_serial=idx + 1,
                similarity_threshold=float(ctx.cfg.setting("cluster.recording_similarity_threshold", 0.85)))
            conn.commit()
        except Exception as e:
            batchcontrol.fail_batch(conn, batch_id, f"{type(e).__name__}: {e}")
            raise
        batchcontrol.commit_batch(conn, batch_id, cost_usd=round(real_cost, 4))
        for action, n in chunk_record["by_action"].items():
            record_summary["by_action"][action] = record_summary["by_action"].get(action, 0) + n
        record_summary["unresolved_occurrence_count"] += chunk_record["unresolved_occurrence_count"]
        record_summary["unresolved_detail"] += chunk_record["unresolved_detail"]

    if preview:
        already_n = sum(1 for b in batch_summaries if b["already_committed"])
        total_cost = sum(b["est_cost_usd"] for b in batch_summaries
                         if force or not b["already_committed"])
        already_note = ("" if not already_n else
                        f", {already_n} of {len(chunks)} already committed by a prior run "
                        f"({'will be RE-RUN, -Force is set' if force else 'will be skipped'})")
        fully_covered_note = (f", {len(fully_covered_ids)} verse(s) excluded entirely (already "
                             f"fully covered by an earlier pass)" if fully_covered_ids else "")
        return ok(f"PREVIEW {cluster_code}: {len(chunks)} batch(es), {len(verse_ids)} verse(s), "
                 f"{len(strongs)} strong(s), estimated ${total_cost:.4f} total for the "
                 f"{'forced re-run' if force else 'remaining work'}{already_note}"
                 f"{fully_covered_note} -- no API call "
                 f"made, nothing written. Re-run with -Preview:$false to execute for real.",
                 preview=True, batches=batch_summaries, cluster_code=cluster_code,
                 verse_count=len(verse_ids), strong_count=len(strongs), force=force)

    # the final stage of verse-reading: checked and advanced after every live run (#1860)
    status_result = clusterstatus.advance_if_verse_reading_complete(conn, cluster_code)
    conn.commit()

    coverage = stage1coverage.validate_coverage(conn, cluster_code, verse_ids, family="relational")
    coverage_pattern = ctx.cfg.required_setting("report.stage1_coverage_validation_pattern")
    coverage_report_path = pathlib.Path(
        coverage_pattern.format(cluster_code=cluster_code, run_id=ctx.run_id))
    coverage_report_path.parent.mkdir(parents=True, exist_ok=True)
    with coverage_report_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["category", "verse_reference", "strong", "question_code", "live_node_count"])
        for v, s, q in coverage["missing_sample"]:
            w.writerow(["MISSING", v, s, q, 0])
        for v, s, q in coverage["unexpected_sample"]:
            w.writerow(["UNEXPECTED", v, s, q, ""])
        for (v, s, q), n in coverage["over_count_sample"]:
            w.writerow(["OVER_COUNT", v, s, q, n])
    coverage_note = (f"; validation: {coverage['ok_count']} ok, {coverage['missing_count']} "
                     f"missing, {coverage['unexpected_count']} unexpected, "
                     f"{coverage['over_count_count']} over-count (of {coverage['expected_count']} "
                     f"expected) -- {coverage_report_path}")

    total_cost = sum(c["cost_usd"] for c in llm_summary)
    unresolved_n = record_summary["unresolved_occurrence_count"]
    unresolved_note = (f", {unresolved_n} unresolved occurrence(s): "
                       f"{'; '.join(record_summary['unresolved_detail'][:5])}"
                       f"{' ...' if unresolved_n > 5 else ''}") if unresolved_n else ""
    status_note = (f"; cluster.status -> ready_for_subgroup_allocation" if status_result["advanced"]
                  else f"; {len(status_result['missing_strongs'])} of "
                       f"{status_result['member_strong_count']} strong(s) still need verse-reading "
                       f"before subgroup allocation can start" if not status_result["complete"]
                  else "")
    skipped_note = f", {skipped_batches} batch(es) skipped (already committed)" if skipped_batches else ""
    fully_covered_note = (f", {len(fully_covered_ids)} verse(s) excluded entirely (already fully "
                         f"covered by an earlier pass)" if fully_covered_ids else "")
    return ok(f"{cluster_code}: {len(chunks)} batch(es){skipped_note}{fully_covered_note}, "
             f"${total_cost:.4f} spent, "
             f"observations {record_summary['by_action']}{unresolved_note}{status_note}"
             f"{coverage_note}",
             preview=False, batches=batch_summaries, llm_calls=llm_summary,
             record_summary=record_summary, cluster_code=cluster_code,
             status_result=status_result, skipped_batches=skipped_batches, coverage=coverage,
             fully_covered_verse_count=len(fully_covered_ids))
