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
import re

from .base import Ctx, Outcome, ok, fail


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
        consecutive = (ch == pch and vs == pvs + 1)          # same chapter, adjacent verse
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
