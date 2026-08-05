"""Passage handler — build a book's passages from HIB continuity. Config-governed.

**Redefined 2026-08-05 (B4, `debate-analytic-process-digest-20260805.md` Step 2).** A passage's
boundary is now the same HIB(s) continuing to be what the text is tracking — NOT a thematic unit,
and NOT the prior characteristic/candidate-stamp definition this handler used before the study's
"characteristics → HIB" reframing. Boundaries come from `verse_hib` (debate digest Step 1's
per-verse HIB presence): a maximal run of consecutive same-chapter HIB-bearing verses, broken when
consecutive verses stop sharing a live HIB (hib-continuity) unless -Rule maximal. A run longer than
passage.review_over is flagged needs_review (a long run may be several passages under different HIB
focuses — the same over-batching concern the debate digest's failure-mode (b) names directly).

**Retired shape, superseded not deleted.** Previously sourced from `span_candidate`
(char-continuity: shared candidate base-Strong's) — that whole candidate system is itself retired
(BUILD.md, `retract_candidate_system.py`); this handler's old body is preserved in git history, not
copied forward, since the algorithm's SHAPE (adjacency + shared-set-membership run-forming) is
identical, only the source table and the meaning of "shared" changed.
"""

from __future__ import annotations

import datetime
import pathlib
import re

from .base import Ctx, Outcome, ok, fail, escalate
from ..lib import escalation as esc, reportkit, passagetrack, versespanmeaningreport


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _cv(osis: str) -> tuple[int, int]:
    """(chapter, verse) from an osisId like 'Prov.3.5'."""
    p = (osis or "").split(".")
    def i(x):
        m = re.match(r"\d+", x or "")
        return int(m.group()) if m else 0
    return (i(p[1]) if len(p) > 1 else 0, i(p[2]) if len(p) > 2 else 0)


def _may(ctx: Ctx, writer: str, table: str):
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


def build(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    rule = ctx.params.get("Rule") or ctx.cfg.setting("passage.default_rule", "hib-continuity")
    min_shared = int(ctx.cfg.setting("passage.min_shared_hibs", 1))
    review_over = int(ctx.cfg.setting("passage.review_over", 10))  # matches DB value (was 5)
    cross_chapter = bool(ctx.cfg.setting("passage.cross_chapter", False))
    like = f"{book}.%"

    # HIBs present per verse (debate digest Step 1's per-verse sweep; verse_hib is the input)
    hibs_by_verse: dict[int, set] = {}
    for r in ctx.db.rows(
        "SELECT vh.verse_id AS vid, vh.hib_id AS hid FROM verse_hib vh "
        "JOIN verse v ON v.id = vh.verse_id "
        "WHERE v.osisId LIKE ? AND vh.deleted=0 AND v.deleted=0", (like,)):
        hibs_by_verse.setdefault(r["vid"], set()).add(r["hid"])
    if not hibs_by_verse:
        return fail("no-hibs", f"book {book!r} has no verse_hib data — HIB identification "
                               f"(debate digest Step 1) must happen for this book before passages "
                               f"can be built")

    vinfo = {r["id"]: r["osisId"] for r in ctx.db.rows(
        "SELECT id, osisId FROM verse WHERE osisId LIKE ? AND deleted=0", (like,))}
    verses = sorted(hibs_by_verse.keys(), key=lambda vid: _cv(vinfo[vid]))

    # form runs: consecutive same-chapter HIB-bearing verses, broken by hib-continuity
    runs: list[list[int]] = []
    cur: list[int] = []
    for vid in verses:
        if not cur:
            cur = [vid]
            continue
        ch, vs = _cv(vinfo[vid])
        pch, pvs = _cv(vinfo[cur[-1]])
        # same chapter, adjacent verse — unless passage.cross_chapter allows crossing.
        # NOTE: crossing a real chapter boundary (last verse of ch N -> verse 1 of ch N+1) still
        # can't be recognised here even with cross_chapter=True, because "adjacent" is computed
        # purely from verse numbers (vs == pvs + 1) and verse numbers reset to 1 each chapter —
        # this app has no per-chapter verse-count reference to detect a true boundary crossing.
        # Wired in 2026-07-22 (was previously read nowhere, per configmaint's orphan-config
        # finding) so the setting is no longer dead, not because true crossing is implemented.
        consecutive = (cross_chapter or ch == pch) and vs == pvs + 1
        shares = len(hibs_by_verse[vid] & hibs_by_verse[cur[-1]]) >= min_shared
        if consecutive and (rule == "maximal" or shares):
            cur.append(vid)
        else:
            runs.append(cur)
            cur = [vid]
    if cur:
        runs.append(cur)

    _may(ctx, "passage.build", "passage")
    # clean re-derivation: drop the book's passages + membership, then rebuild
    ctx.db.conn.execute(
        "DELETE FROM verse_passage WHERE passage_id IN (SELECT id FROM passage WHERE book=?)", (book,))
    ctx.db.conn.execute("DELETE FROM passage WHERE book=?", (book,))

    now = _now()
    flagged = 0
    for run in runs:
        a_ch, a_vs = _cv(vinfo[run[0]])
        e_ch, e_vs = _cv(vinfo[run[-1]])
        vc = len(run)
        needs = 1 if vc > review_over else 0
        flagged += needs
        ref = f"{book} {a_ch}:{a_vs}" if vc == 1 else f"{book} {a_ch}:{a_vs}-{e_vs}"
        pid = ctx.db.write("passage", {
            "book": book, "anchor_verse_id": run[0],
            "start_chapter": a_ch, "start_verse": a_vs, "end_chapter": e_ch, "end_verse": e_vs,
            "ref": ref, "verse_count": vc, "rule": rule, "source": "passage-build",
            "needs_review": needs, "created_at": now, "deleted": 0})
        for i, vid in enumerate(run):
            ctx.db.write("verse_passage", {
                "passage_id": pid, "verse_id": vid, "is_anchor": 1 if i == 0 else 0,
                "created_at": now, "deleted": 0})

    msg = f"{len(runs)} passage(s) over {len(verses)} HIB-bearing verse(s) in {book} ({rule})"
    if flagged:
        msg += f"; {flagged} need review (>{review_over} verses)"
    return ok(msg, passages=len(runs), hib_verses=len(verses), needs_review=flagged)


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
    path = pathlib.Path(ctx.cfg.setting("passage.quality_report_path",
                                       "iba/app/reports/passage-quality.md"))
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
    verse_count distribution and judge it" — scoping is the only difference that matters."""
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

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["answer"]
        if decision == "approve":
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
        question=(f"Passage distribution {scope_label}: {total} passages, {min_vc}-{max_vc} "
                 f"verses/passage (average {avg:.2f}), {single} ({100*single/total:.0f}%) are "
                 f"single-verse. Is this distribution acceptable — no debate range (or raw span, "
                 f"if unscoped) looks like an outlier that should be reconsidered? "
                 f"Full per-book breakdown written to {report_path}."),
        preset={"total": total, "avg_verses": round(avg, 2), "min_verses": min_vc,
               "max_verses": max_vc, "single_verse": single,
               "distribution": [dict(r) for r in dist[:30]], "report_path": str(report_path)},
        tried=f"computed the live verse_count distribution {scope_label} — approve to accept "
              f"as-is, reject to flag it for revisiting, or revise with a comment")


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
