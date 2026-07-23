"""Passage handler — build a book's passages from the candidate stamp. Config-governed.

A passage's sole purpose is to extend a characteristic's context to its adjacent verses so
movement / process / qualifying spans can be assessed with that context — NOT a thematic
unit. Boundaries come from the candidate stamp: a maximal run of consecutive same-chapter
candidate-bearing verses, broken when consecutive verses stop sharing a candidate base-
Strong's (char-continuity) unless -Rule maximal. A run longer than passage.review_over is
flagged needs_review (a long run may be several passages under different char focuses).
"""

from __future__ import annotations

import datetime
import pathlib
import re

from .base import Ctx, Outcome, ok, fail, escalate
from ..lib import escalation as esc, reportkit


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
    rule = ctx.params.get("Rule") or ctx.cfg.setting("passage.default_rule", "char-continuity")
    min_shared = int(ctx.cfg.setting("passage.min_shared_strongs", 1))
    review_over = int(ctx.cfg.setting("passage.review_over", 5))
    cross_chapter = bool(ctx.cfg.setting("passage.cross_chapter", False))
    like = f"{book}.%"

    # candidate base-strongs per candidate-bearing verse
    cand_by_verse: dict[int, set] = {}
    for r in ctx.db.rows(
        "SELECT sp.verse_id AS vid, sc.lemma_key AS lk FROM span_candidate sc "
        "JOIN span sp ON sp.id = sc.span_id JOIN verse v ON v.id = sp.verse_id "
        "WHERE v.osisId LIKE ? AND sc.deleted=0 AND sp.deleted=0 AND v.deleted=0", (like,)):
        cand_by_verse.setdefault(r["vid"], set()).add(r["lk"])
    if not cand_by_verse:
        return fail("no-candidates", f"book {book!r} has no candidate spans — run set-candidates first")

    vinfo = {r["id"]: r["osisId"] for r in ctx.db.rows(
        "SELECT id, osisId FROM verse WHERE osisId LIKE ? AND deleted=0", (like,))}
    verses = sorted(cand_by_verse.keys(), key=lambda vid: _cv(vinfo[vid]))

    # form runs: consecutive same-chapter candidate verses, broken by char-continuity
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
        shares = len(cand_by_verse[vid] & cand_by_verse[cur[-1]]) >= min_shared
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

    msg = f"{len(runs)} passage(s) over {len(verses)} candidate verse(s) in {book} ({rule})"
    if flagged:
        msg += f"; {flagged} need review (>{review_over} verses)"
    return ok(msg, passages=len(runs), candidate_verses=len(verses), needs_review=flagged)


# ── validate (standalone, on-demand) ──────────────────────────────────────────
# review_over already catches passages that are too LONG; nothing catches the opposite —
# the 1.56-verses/passage average found earlier, and passage.cross_chapter being pure
# documentation (handlers never read it — see configmaint's orphan check). This does NOT invent
# a fragmentation threshold — the passage rule itself is still pending the researcher's own
# confirmation (raised earlier this session) — it reports the real distribution and lets the
# researcher decide, same shape as candidate.validate: one escalation per invocation, standalone,
# not tied to every build-passages run.
def _write_quality_report(ctx: Ctx, total: int, avg: float, single: int, dist: list, by_book: list) -> pathlib.Path:
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
    reportkit.write_csv_pairing(ctx.db.conn, "passage.validate", path.parent / "export")
    reportkit.write_report(ctx.db.conn, "passage.validate", path, L)
    return path


def validate(ctx: Ctx) -> Outcome:
    dist = ctx.db.rows(
        "SELECT verse_count, COUNT(*) n FROM passage WHERE deleted=0 GROUP BY verse_count ORDER BY verse_count")
    total = sum(r["n"] for r in dist)
    if not total:
        return ok("no passages built yet — nothing to review")
    single = sum(r["n"] for r in dist if r["verse_count"] == 1)
    avg = sum(r["verse_count"] * r["n"] for r in dist) / total

    by_book = [dict(r) for r in ctx.db.rows(
        "SELECT book, COUNT(*) n, AVG(verse_count) avg, "
        "SUM(CASE WHEN verse_count=1 THEN 1 ELSE 0 END) single "
        "FROM passage WHERE deleted=0 GROUP BY book ORDER BY book")]
    report_path = _write_quality_report(ctx, total, avg, single, dist, by_book)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["answer"]
        if decision == "approve":
            return ok(f"acknowledged: {total} passages, avg {avg:.2f} verses/passage, "
                      f"{single} ({100*single/total:.0f}%) single-verse — researcher confirmed "
                      f"this distribution is acceptable; full detail in {report_path}",
                      total=total, avg_verses=avg, single_verse=single)
        if decision == "reject":
            return fail("findings-rejected",
                       "researcher flagged the passage distribution as needing the rule revisited",
                       total=total, avg_verses=avg, single_verse=single)
        return fail("needs-revision", f"researcher comment: {answered['comment'] or '(none)'}")

    return escalate(
        "needs-review",
        question=(f"Passage distribution across all books: {total} passages, average "
                 f"{avg:.2f} verses/passage, {single} ({100*single/total:.0f}%) are single-verse. "
                 f"passage.review_over only flags passages that are too LONG — nothing flags this. "
                 f"Is this distribution acceptable as the char-continuity rule stands, or does the "
                 f"passage rule need revisiting (per the open question from earlier this session)? "
                 f"Full per-book breakdown written to {report_path}."),
        preset={"total": total, "avg_verses": round(avg, 2), "single_verse": single,
               "distribution": [dict(r) for r in dist[:30]], "report_path": str(report_path)},
        tried="computed the live verse_count distribution across every built passage — approve to "
              "accept as-is, reject to flag the rule for revisiting, or revise with a comment")
