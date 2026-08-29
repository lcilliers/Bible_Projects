"""Passage handler — register the debate's own input scope as the passage. Config-governed.

**Redefined 2026-08-06 (researcher direction, following the HIB-distribution visualization across
Dan 8 / Jonah 1 / Hos 1 / Mic 1).** Passaging is about the capacity to digest a scope, not about
finding a narrative structure within it — across all four sampled chapters, no natural sub-chapter
break existed: every HIB's phenomena related to another HIB's, on equal footing with a single HIB's
own movement across verses. The HIB-continuity run-forming algorithm (2026-08-05, B4) is RETIRED
in this pass, not just its parameters tuned — it was still trying to derive a narratively-meaningful
boundary from HIB co-presence, and the visualization showed that doesn't correspond to anything
real at the scale this study reads at (a single chapter, occasionally a short run of them).

**New rule.** A passage IS the debate's own input scope (`-Chapters`/`-Range`) — registered
verbatim, never algorithmically sub-divided. This step's real job: read the whole scope in light of
the HIBs already identified (`verse_hib`, Step 1), synthesise a high-level story (`story_summary`),
and self-assess whether the scope can actually be read as a whole without quality loss
(`feasible`/`feasibility_note`). Refuses outright (`scope-too-complex`) if not — no passage row is
written, and the failure message tells the operator to narrow the scope and resubmit, rather than
silently sub-dividing it. Like `hib.set`/`phenomenon.set`/`operation.set`, this judgement is the
analyst's own, already made before calling this step — the payload carries the decision, this
handler validates, grant-checks, and commits it.

**Reconciliation, single-item shape.** Because a passage is now exactly one row per exact scope,
there is nothing to derive or rebuild. If a live passage already exists for this precise scope, its
`story_summary`/`feasibility_note` are compared to the incoming payload: identical is a no-op,
different requires a `reconciliation_note` (else `unreconciled`), and the row is updated IN PLACE —
same `id`, `verse_passage` rows untouched (verse coverage can't change for an identical scope), so a
story correction can never orphan a `phenomenon`/`operation` the way a boundary change could under
the old algorithm.

**Legacy transition, unchanged in spirit.** A live legacy (`rule IS NULL`, pre-B4) row matching the
EXACT same scope is soft-deleted on the one-time transition — "we are not reconciling the old with
the new." A legacy row for a different scope is simply left alone.

**Retired in this same pass** (BUILD.md): the whole run-forming loop; `passage.min_shared_hibs`,
`passage.cross_chapter`, `passage.default_rule` (no algorithm left to configure); `passage.
review_over`'s auto-flagging (the feasibility self-assessment now does this job, as a real reading
judgement rather than a verse-count threshold) — all deactivated via `configmaint.propose`.
"""

from __future__ import annotations

import datetime
import json
import pathlib

from .base import Ctx, Outcome, ok, fail, escalate
from ..lib import escalation as esc, reportkit, passagetrack, versespanmeaningreport
from ..lib.debateaudit import log_change as _log_change


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _may(ctx: Ctx, writer: str, table: str):
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


def _resolve_range(ctx: Ctx):
    """Same one-of-Chapters/-Range shape every other book-scoped step uses."""
    if ctx.params.get("Range"):
        ch, vlo, vhi = versespanmeaningreport.parse_range(ctx.params["Range"])
        return ch, ch, vlo, vhi
    lo, hi = versespanmeaningreport.parse_chapters(ctx.params["Chapters"])
    return lo, hi, None, None


class BadPayload(Exception):
    """PayloadPath missing/unreadable, not valid JSON, or missing a required key — always caught
    and turned into a clean fail(), never left to crash the run with a raw traceback."""


def _load_payload(ctx: Ctx) -> dict:
    raw = ctx.params.get("PayloadPath")
    if not raw:
        raise BadPayload("-PayloadPath not given")
    path = pathlib.Path(raw)
    if not path.exists():
        raise BadPayload(f"PayloadPath {path} does not exist")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise BadPayload(f"PayloadPath {path} is not valid JSON: {e}")


# payload: {"book": "Dan", "story_summary": "...", "feasible": true, "feasibility_note": "...",
#           "reconciliation_note": "..."  -- required only when correcting an already-live passage
#                                             for this exact scope with different content}
def build(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    lo, hi, vlo, vhi = _resolve_range(ctx)

    try:
        payload = _load_payload(ctx)
    except BadPayload as e:
        return fail("bad-payload", str(e))

    missing = [k for k in ("story_summary", "feasible", "feasibility_note") if k not in payload]
    if missing:
        return fail("bad-payload", f"payload missing required key(s): {missing}")
    story_summary = payload["story_summary"]
    feasible = bool(payload["feasible"])
    feasibility_note = payload["feasibility_note"]
    if not feasibility_note:
        return fail("bad-payload", "feasibility_note is required either way (why the scope was "
                                   "judged feasible, or why it wasn't)")

    if not feasible:
        return fail("scope-too-complex",
                    f"{book} {lo}-{hi}: judged NOT readable as a whole without quality loss -- "
                    f"narrow -Chapters/-Range and resubmit. Reason: {feasibility_note}")

    verses = versespanmeaningreport.fetch_verses(ctx.db.conn, book, lo, hi, vlo, vhi)
    if not verses:
        return fail("no-verses", f"{book} {lo}-{hi}: no live verses found for this scope")
    verses.sort(key=lambda v: (v["chapter"], v["verse"]))
    verse_ids = [v["id"] for v in verses]

    ph = ",".join("?" * len(verse_ids))
    hib_count = ctx.db.rows(
        f"SELECT COUNT(DISTINCT hib_id) n FROM verse_hib WHERE deleted=0 AND verse_id IN ({ph})",
        tuple(verse_ids))[0]["n"]
    if hib_count == 0:
        return fail("no-hibs", f"{book} {lo}-{hi}: no verse_hib data for this scope -- run "
                               f"hib.set (debate digest Step 1) for these verses first")

    _may(ctx, "passage.build", "passage")
    _may(ctx, "passage.build", "verse_passage")
    _may(ctx, "passage.build", "debate_change_detail")

    a_ch, a_vs = verses[0]["chapter"], verses[0]["verse"]
    e_ch, e_vs = verses[-1]["chapter"], verses[-1]["verse"]
    if a_ch == e_ch:
        ref = f"{book} {a_ch}:{a_vs}" if len(verses) == 1 else f"{book} {a_ch}:{a_vs}-{e_vs}"
    else:
        ref = f"{book} {a_ch}:{a_vs}-{e_ch}:{e_vs}"

    existing = passagetrack.find_tracked_passage(ctx.db.conn, book, lo, hi, vlo, vhi)
    now = _now()

    # A verse belongs to at most one live passage (verse_passage.verse_id is DB-unique) -- found
    # live, 2026-08-06: a scope that only PARTIALLY overlaps a wider existing passage (rather than
    # matching it exactly) was neither caught by the exact-match check above nor by anything else,
    # and crashed the write outright on the UNIQUE constraint, mid-transaction (the crash itself
    # then exposed a second bug, in run.py's own crash handler -- see that file). Checked
    # explicitly here, before any write is attempted: every OTHER live passage (not `existing`
    # itself, which the exact-match branch above already handles) that owns any verse in this
    # scope. Legacy (`rule IS NULL`) overlaps are superseded wholesale, same "not reconciling old
    # with new" rule as an exact-match legacy row -- the WHOLE legacy passage is retired, not just
    # the overlapping verses, since partial-splitting historical data isn't worth the complexity.
    # A new-model (`rule IS NOT NULL`) overlap with a genuinely DIFFERENT scope is a real conflict
    # between two operator-chosen scopes and is refused outright, not auto-resolved.
    ph2 = ",".join("?" * len(verse_ids))
    overlaps = ctx.db.rows(
        f"SELECT DISTINCT p.id, p.ref, p.rule FROM passage p JOIN verse_passage vp "
        f"ON vp.passage_id = p.id WHERE p.deleted=0 AND vp.deleted=0 AND vp.verse_id IN ({ph2}) "
        f"AND p.id != ?", tuple(verse_ids) + (existing["id"] if existing else -1,))
    new_model_overlaps = [r for r in overlaps if r["rule"] is not None]
    if new_model_overlaps:
        refs = ", ".join(sorted(r["ref"] for r in new_model_overlaps))
        return fail("scope-overlaps-existing",
                    f"{ref}: overlaps {len(new_model_overlaps)} already-registered passage(s) "
                    f"with a different scope: {refs} -- pick a non-overlapping scope, or address "
                    f"the existing one(s) first")
    def _retire_legacy_passage(row_id: int, ref_hint: str) -> None:
        """Full soft-delete of a legacy passage + its verse_passage children -- the "not
        reconciling old with new" transition, real CRUD delete (not a correction), logged per row
        for the same traceability every other debate writer now carries (2026-08-08)."""
        live_vp = ctx.db.rows(
            "SELECT id, verse_id, is_anchor FROM verse_passage WHERE deleted=0 AND passage_id=?",
            (row_id,))
        for vp in live_vp:
            ctx.db.conn.execute("UPDATE verse_passage SET deleted=1 WHERE id=?", (vp["id"],))
            _log_change(ctx, "passage.build", "verse_passage", "delete", {"id": vp["id"]},
                       before={"passage_id": row_id, "verse_id": vp["verse_id"],
                               "is_anchor": vp["is_anchor"]})
        ctx.db.conn.execute("UPDATE passage SET deleted=1 WHERE id=?", (row_id,))
        _log_change(ctx, "passage.build", "passage", "delete", {"id": row_id},
                   before={"ref": ref_hint})

    legacy_overlaps = [r for r in overlaps if r["rule"] is None]
    for r in legacy_overlaps:
        _retire_legacy_passage(r["id"], r["ref"])

    if existing and existing["rule"] is None:
        # legacy (pre-B4) row, exact-scope match -- one-time transition, unconditional, not
        # reconciled, matching every other legacy-row transition in this pipeline.
        _retire_legacy_passage(existing["id"], existing["ref"])
        existing = None

    if existing:
        current = (existing["story_summary"], existing["feasibility_note"])
        incoming = (story_summary, feasibility_note)
        if current == incoming:
            return ok(f"{ref}: unchanged (already registered, same story/feasibility)",
                     passage_id=existing["id"], changed=False)
        if not payload.get("reconciliation_note"):
            return fail("unreconciled",
                       f"{ref}: a live passage already exists for this exact scope with "
                       f"different story_summary/feasibility_note -- a reconciliation_note is "
                       f"required to change it")
        ctx.db.conn.execute(
            "UPDATE passage SET story_summary=?, feasibility_note=? WHERE id=?",
            (story_summary, feasibility_note, existing["id"]))
        _log_change(ctx, "passage.build", "passage", "update", {"id": existing["id"]},
                   set_={"story_summary": story_summary, "feasibility_note": feasibility_note},
                   before={"story_summary": existing["story_summary"],
                           "feasibility_note": existing["feasibility_note"]})
        ctx.db.conn.commit()
        return ok(f"{ref}: story/feasibility corrected in place (passage_id={existing['id']} "
                  f"unchanged, verse coverage unchanged, nothing orphaned) — "
                  f"{payload['reconciliation_note']}",
                 passage_id=existing["id"], changed=True)

    passage_row = {
        "book": book, "anchor_verse_id": verse_ids[0],
        "start_chapter": a_ch, "start_verse": a_vs, "end_chapter": e_ch, "end_verse": e_vs,
        "ref": ref, "verse_count": len(verses), "rule": "input-scope", "source": "passage-build",
        "needs_review": 0, "story_summary": story_summary, "feasibility_note": feasibility_note,
        "created_at": now, "deleted": 0}
    pid = ctx.db.write("passage", passage_row)
    _log_change(ctx, "passage.build", "passage", "insert", {"id": pid}, set_=passage_row)
    for i, vid in enumerate(verse_ids):
        vp_row = {"passage_id": pid, "verse_id": vid, "is_anchor": 1 if i == 0 else 0,
                 "created_at": now, "deleted": 0}
        vp_id = ctx.db.write("verse_passage", vp_row)
        _log_change(ctx, "passage.build", "verse_passage", "insert", {"id": vp_id}, set_=vp_row)

    ctx.db.conn.commit()
    return ok(f"{ref}: passage registered ({len(verses)} verse(s), {hib_count} distinct HIB(s) "
              f"in scope) — passage_id={pid}",
             passage_id=pid, verse_count=len(verses), hibs_in_scope=hib_count)


# ── validate (standalone, on-demand) ──────────────────────────────────────────
# review_over already catches passages that are too LONG; nothing catches the opposite —
# the 1.56-verses/passage average found earlier, and passage.cross_chapter being pure
# documentation (handlers never read it — see configmaint's orphan check). This does NOT invent
# a fragmentation threshold — the passage rule itself is still pending the researcher's own
# confirmation (raised earlier this session) — it reports the real distribution and lets the
# researcher decide, same shape as candidate.validate: one escalation per invocation, standalone,
# not tied to every build-passages run.
def _write_quality_report(ctx: Ctx, total: int, avg: float, single: int, dist: list, by_book: list,
                          scope_sql: str, scope_args: tuple) -> pathlib.Path:
    """Persist the current distribution — per the researcher's 2026-07-21 ruling that a quality
    check's output must persist to a report file like every other report in the app, not live
    only in a terminal print + an escalation row."""
    path = pathlib.Path(ctx.cfg.required_module_setting("cfg_passage", "passage.quality_report_path"))
    intro = [
        f"> Generated {_now()} by `passage.validate`. Read-only findings, not a gate.", "",
        f"- total passages: **{total}**",
        f"- average verses/passage: **{avg:.2f}**",
        f"- single-verse passages: **{single}** ({100*single/total:.0f}%)",
    ]
    sections = {
        "dist": ["| verse_count | passages |", "|---:|---:|"]
                + [f"| {r['verse_count']} | {r['n']} |" for r in dist],
        "by_book": ["| book | passages | avg verses/passage | single-verse |", "|---|---:|---:|---:|"]
                  + [f"| {r['book']} | {r['n']} | {r['avg']:.2f} | {r['single']} |" for r in by_book],
    }
    L = reportkit.render_scaffold(ctx.db.conn, "passage.validate", sections, intro=intro)
    # Found 2026-07-30 (researcher: "it seems to include deleted items"): `write_csv_pairing`'s
    # default is a verbatim FULL-table dump (no `deleted` filter at all — appropriate for a cfg_*
    # audit trail, wrong here) — for `passage`/`verse_passage` that meant the CSV export sat right
    # next to a report saying "24 passages" while containing all 18,528/25,244 rows, 99%+ of them
    # soft-deleted by the 2026-07-26 passage-system retirement (`retract_passage_system.py`).
    # Harmless before that retirement (the whole table WAS the live data); wrong now that most of
    # it is historical. Pass the same deleted=0 rows the report itself computed from, via
    # `row_filter`, exactly the mechanism `write_csv_pairing` already has for this.
    live_passages = ctx.db.rows(f"SELECT * FROM passage WHERE deleted=0{scope_sql}", scope_args)
    live_ids = [r["id"] for r in live_passages]
    ph = ",".join("?" * len(live_ids)) if live_ids else "NULL"
    live_verse_passages = ctx.db.rows(
        f"SELECT * FROM verse_passage WHERE deleted=0 AND passage_id IN ({ph})", tuple(live_ids))
    reportkit.write_csv_pairing(ctx.db.conn, "passage.validate", path.parent / "export",
                                row_filter={"passage": live_passages,
                                          "verse_passage": live_verse_passages})
    path = reportkit.write_report(ctx.db.conn, "passage.validate", path, L)
    return path


def validate(ctx: Ctx) -> Outcome:
    """Corpus-wide by default (no `-Book`) — the original 2026-07-21 check on the raw
    char-continuity distribution. With `-Book`, scoped to one book — reactivated 2026-07-28
    (`reactivate_passage_quality.py`) for a second, distinct purpose the original check predates:
    a spot-check on the debate-range sizes `report.passage_debate` produced for a completed book
    (e.g. Dan 11's 45-verse range — was that the right call?), not on raw span fragmentation. Both
    purposes share one query/report/escalation shape since both are ultimately "look at the live
    verse_count distribution and judge it" — scoping is the only difference that matters.

    escalation #798/#799 SS3.5: used to `escalate()` unconditionally on every run, no threshold
    at all -- "iterative design, ask every time" (researcher, 2026-08-22). Now checks each book's
    distribution against `cfg_passage.passage.max_single_verse_pct`/
    `passage.max_avg_verses_per_passage` and only escalates if at least one book actually breaches
    a bound; an already-in-bounds distribution is accepted automatically, same shape as
    `cluster.validate`/`lexicon.validate`."""
    book = ctx.params.get("Book")
    scope_sql = " AND book=?" if book else ""
    scope_args = (book,) if book else ()
    scope_label = f"in {book}" if book else "across all books"

    dist = ctx.db.rows(
        f"SELECT verse_count, COUNT(*) n FROM passage WHERE deleted=0{scope_sql} "
        f"GROUP BY verse_count ORDER BY verse_count", scope_args)
    total = sum(r["n"] for r in dist)
    if not total:
        return ok(f"no passages found {scope_label} — nothing to review")
    single = sum(r["n"] for r in dist if r["verse_count"] == 1)
    avg = sum(r["verse_count"] * r["n"] for r in dist) / total
    min_vc = min(r["verse_count"] for r in dist)
    max_vc = max(r["verse_count"] for r in dist)

    by_book = [dict(r) for r in ctx.db.rows(
        f"SELECT book, COUNT(*) n, AVG(verse_count) avg, "
        f"SUM(CASE WHEN verse_count=1 THEN 1 ELSE 0 END) single "
        f"FROM passage WHERE deleted=0{scope_sql} GROUP BY book ORDER BY book", scope_args)]
    report_path = _write_quality_report(ctx, total, avg, single, dist, by_book,
                                        scope_sql, scope_args)

    # per-book breach check against cfg_passage's thresholds -- the book's own TOTAL verse count
    # (from `verse`, via osisId's book prefix) is the single-verse-pct denominator, not the book's
    # passage count.
    verse_book_filter = " AND SUBSTR(osisId, 1, INSTR(osisId, '.') - 1) = ?" if book else ""
    verse_totals = {r["book"]: r["n"] for r in ctx.db.rows(
        f"SELECT SUBSTR(osisId, 1, INSTR(osisId, '.') - 1) book, COUNT(*) n FROM verse "
        f"WHERE deleted=0{verse_book_filter} GROUP BY book", scope_args)}
    max_single_pct = float(ctx.cfg.required_module_setting("cfg_passage", "passage.max_single_verse_pct"))
    max_avg = float(ctx.cfg.required_module_setting("cfg_passage", "passage.max_avg_verses_per_passage"))
    breaches = []
    for row in by_book:
        book_total_verses = verse_totals.get(row["book"], 0)
        single_pct = (row["single"] / book_total_verses * 100) if book_total_verses else 0.0
        reasons = []
        if single_pct > max_single_pct:
            reasons.append(f"{single_pct:.1f}% single-verse (limit {max_single_pct:.0f}%)")
        if row["avg"] > max_avg:
            reasons.append(f"avg {row['avg']:.2f} verses/passage (limit {max_avg:.0f})")
        if reasons:
            breaches.append(f"{row['book']}: {'; '.join(reasons)}")

    if not breaches:
        return ok(f"{total} passages {scope_label}, {min_vc}-{max_vc} verses/passage "
                 f"(avg {avg:.2f}), {single} ({100*single/total:.0f}%) single-verse — every book "
                 f"within passage.max_single_verse_pct/max_avg_verses_per_passage, no review "
                 f"needed; full detail in {report_path}",
                 total=total, avg_verses=avg, min_verses=min_vc, max_verses=max_vc,
                 single_verse=single)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        # escalation #798/#799 SS4: decision_required now resolves via Update()'s manual
        # vocabulary (approved) not AnswerRun's dispatcher vocabulary (approve).
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {total} passages {scope_label}, {min_vc}-{max_vc} "
                      f"verses/passage (avg {avg:.2f}), {single} ({100*single/total:.0f}%) "
                      f"single-verse — researcher confirmed this distribution is acceptable; "
                      f"full detail in {report_path}",
                      total=total, avg_verses=avg, min_verses=min_vc, max_verses=max_vc,
                      single_verse=single)
        if decision == "reject":
            return fail("findings-rejected",
                       "researcher flagged the passage distribution as needing the rule revisited",
                       total=total, avg_verses=avg, min_verses=min_vc, max_verses=max_vc,
                       single_verse=single)
        return fail("needs-revision", f"researcher comment: {answered['comment'] or '(none)'}")

    return escalate(
        "needs-review",
        question=(f"Passage distribution {scope_label} breaches its threshold in "
                 f"{len(breaches)} book(s): {'; '.join(breaches)}. {total} passages total, "
                 f"{min_vc}-{max_vc} verses/passage (average {avg:.2f}), {single} "
                 f"({100*single/total:.0f}%) single-verse overall. Full per-book breakdown "
                 f"written to {report_path}."),
        preset={"total": total, "avg_verses": round(avg, 2), "min_verses": min_vc,
               "max_verses": max_vc, "single_verse": single, "breaches": breaches,
               "distribution": [dict(r) for r in dist[:30]], "report_path": str(report_path)},
        tried=f"computed the live verse_count distribution {scope_label}, checked against "
              f"passage.max_single_verse_pct ({max_single_pct:.0f}%) and "
              f"passage.max_avg_verses_per_passage ({max_avg:.0f}) — approve to accept as-is, "
              f"reject to flag it for revisiting, or revise with a comment",
        resolution_kind="decision_required")


# ── debate_sync (standalone, on-demand) ───────────────────────────────────────
# The missing half of the report.passage_debate lifecycle (GOVERNANCE.md §3B, 2026-07-30):
# write_scaffold() writes the file and passagetrack.record_debate() records its tracked status,
# but that only ever runs once, immediately after the scaffold is written — at that instant the
# file always still holds the fill-in placeholder, so the tracked status can only ever come out
# 'scaffold' from that call. Nothing previously re-checked status after the researcher/AI filled
# the file in by hand. This step closes that gap: read-only against the debate file (it does NOT
# regenerate or rewrite it — rerunning report.passage_debate on an already-filled range would
# silently overwrite real content with a blank scaffold and flip status back to 'scaffold',
# exactly the corruption BUILD.md's report.passage_debate entry already warns against), DB-write
# only to the tracked `passage` row via the existing, already-tested `passagetrack.record_debate`.
def debate_sync(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    if ctx.params.get("Range"):
        ch, vlo, vhi = versespanmeaningreport.parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = versespanmeaningreport.parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None

    range_label = f"{book} {lo}:{verse_lo}-{verse_hi}" if verse_lo is not None else (
        f"{book} {lo}" if lo == hi else f"{book} {lo}-{hi}")
    row = passagetrack.find_tracked_passage(ctx.db.conn, book, lo, hi, verse_lo, verse_hi)
    if row is None or not row["debate_path"]:
        return fail("no-debate-file", f"{range_label}: nothing tracked for this exact range")
    path = pathlib.Path(row["debate_path"])
    if not path.exists():
        return fail("debate-file-missing", f"{range_label}: tracked path was {path}")

    prior_status = row["debate_status"]
    passage_id = passagetrack.record_debate(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                            book_label, path)
    new_status = ctx.db.rows("SELECT debate_status FROM passage WHERE id=?",
                             (passage_id,))[0]["debate_status"]
    changed = "" if new_status == prior_status else f" (was {prior_status!r})"
    return ok(f"{path} re-checked — debate_status={new_status!r}{changed}",
             path=str(path), passage_id=passage_id, debate_status=new_status)
