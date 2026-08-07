"""iba/app/lib/debaterun.py — readiness checks + staging-path resolution for Debate-Run.ps1.

The debate pipeline (hib.set -> passage.build -> phenomenon.set -> operation.set -> closing.set)
is entirely DB-driven for its own GATING — each step's own handler already checks the previous
step's DB write (BUILD.md §65/§71). This module exists only so `Debate-Run.ps1` can decide, before
calling a step, whether to (a) skip it (already satisfied — a rerun would just reconcile to the
same state), (b) run it (a staging payload is ready), or (c) stop and name the exact staging path
needed next. It deliberately MIRRORS each handler's own gate check rather than reimplementing new
rules — kept in sync by hand, same as any other small cross-cutting helper in this app; the
handlers themselves remain the authority, this is only a read-only convenience for orchestration.

Deliberately excludes running `lexical.build` itself — the lexical is a separate, book-scoped,
run-ahead-of-time prerequisite (`VerseLexical.ps1`), not part of this per-scope debate sequence
(researcher direction, 2026-08-06). It DOES include `lexical_complete_for_scope` (added 2026-08-07)
— a standalone, whole-scope, pre-flight version of the same check `hib.set`'s own hard gate
(`operations.py:_check_lexical_complete`) already makes, but that one only fires once an analytical
pass has already been submitted as a payload, scoped to exactly the verses THAT payload happens to
reference — never the whole book+chapter scope, and never before reading starts. Found live
2026-08-07: `Debate-Run.ps1` had no equivalent of its own, despite the researcher's own words
(quoted verbatim in `_check_lexical_complete`'s docstring) describing this as genuinely "step 1 of
the debate pipeline," run before HIB reading begins, not a side-effect of trying to submit one.
"""
from __future__ import annotations

import sqlite3

from . import passagetrack
from .versespanmeaningreport import fetch_verses


def scope_token(chapters: str | None, range_: str | None) -> str:
    """Filesystem-safe scope token for the staging path — '1', '1-3', or '8_1-27'."""
    if chapters:
        return chapters
    return (range_ or "").replace(":", "_")


def staging_path(cfg, book: str, scope: str, step: str):
    import pathlib
    pattern = cfg.setting("passage.debate_staging_path_pattern",
                          "iba/app/staging/operations/{book_lower}-{scope}-{step}.json")
    return pathlib.Path(pattern.format(book_lower=book.lower(), scope=scope, step=step))


def resolve_range(chapters: str | None, range_: str | None):
    """(lo, hi, verse_lo, verse_hi) — same call shape every existing report/passage function
    already takes (versespanmeaningreport.parse_chapters/parse_range, inlined here to avoid a
    circular import back into that module)."""
    if chapters:
        if "-" in chapters:
            lo, hi = chapters.split("-", 1)
            return int(lo), int(hi), None, None
        n = int(chapters)
        return n, n, None, None
    ch, sep, vspec = (range_ or "").partition(":")
    if not sep:
        raise ValueError(f"range needs chapter:verse[-verse], e.g. 1:1-7 (got {range_!r})")
    if "-" in vspec:
        vlo, vhi = vspec.split("-", 1)
        return int(ch), int(ch), int(vlo), int(vhi)
    n = int(vspec)
    return int(ch), int(ch), n, n


def _scope_verse_ids(conn: sqlite3.Connection, book: str, chapters, range_) -> list[int]:
    lo, hi, vlo, vhi = resolve_range(chapters, range_)
    return [v["id"] for v in fetch_verses(conn, book, lo, hi, vlo, vhi)]


def lexical_complete_for_scope(conn: sqlite3.Connection, book: str, chapters, range_
                               ) -> tuple[bool, list[str]]:
    """Step 1 of the debate pipeline, run BEFORE any HIB reading starts (researcher direction,
    2026-08-06, quoted verbatim in operations.py:_check_lexical_complete — this is the standalone,
    whole-scope form of that same check, missing until now).

    Reads live verses for the whole book+chapter scope from `verse` (fetch_verses already filters
    `deleted=0`); a verse genuinely absent from `verse` is never fetched at all, so it's
    automatically ignored — matching `governance.verse_gap_by_design` / "ignore missing verses in
    the verse table, it is intentional" without any extra logic. Checks each against live (
    `deleted=0`) `verse_lexical` rows — a verse whose only lexical rows were soft-deleted (e.g.
    superseded by a rerun) reads as genuinely missing, same "filter out deleted... lexicals" rule.

    Returns (complete, missing_osis_ids) — missing is empty and complete=True iff every live verse
    in scope has at least one live verse_lexical row."""
    verses = fetch_verses(conn, book, *resolve_range(chapters, range_))
    if not verses:
        return False, []
    verse_ids = [v["id"] for v in verses]
    # fetch_verses returns id/chapter/verse/reference/text -- no osisId column -- build the same
    # dotted form (book.chapter.verse) fetch_verses itself parsed FROM, for the missing-list message.
    osis_by_id = {v["id"]: f"{book}.{v['chapter']}.{v['verse']}" for v in verses}
    ph = ",".join("?" * len(verse_ids))
    covered = {r["verse_id"] for r in conn.execute(
        f"SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND verse_id IN ({ph})",
        verse_ids).fetchall()}
    missing_ids = set(verse_ids) - covered
    return (not missing_ids), sorted(osis_by_id[vid] for vid in missing_ids)


def hib_ready(conn: sqlite3.Connection, book: str, chapters, range_) -> bool:
    """Same check passage.build itself makes (handlers/passage.py:build) — live verse_hib rows
    for every verse this scope covers."""
    verse_ids = _scope_verse_ids(conn, book, chapters, range_)
    if not verse_ids:
        return False
    ph = ",".join("?" * len(verse_ids))
    n = conn.execute(
        f"SELECT COUNT(DISTINCT hib_id) n FROM verse_hib WHERE deleted=0 AND verse_id IN ({ph})",
        verse_ids).fetchone()["n"]
    return n > 0


def find_new_model_passage(conn: sqlite3.Connection, book: str, chapters, range_):
    """Mirrors handlers/operations.py:_find_new_model_passage — a live, rule IS NOT NULL passage
    for this exact scope, or None. A legacy (rule IS NULL) match is deliberately NOT returned —
    same reasoning as the private original: this orchestrator must never treat a legacy row as
    'passage.build already done for the new model'."""
    lo, hi, vlo, vhi = resolve_range(chapters, range_)
    row = passagetrack.find_tracked_passage(conn, book, lo, hi, vlo, vhi)
    if row and row["rule"] is not None:
        return row
    return None


def passage_ready(conn: sqlite3.Connection, book: str, chapters, range_) -> bool:
    return find_new_model_passage(conn, book, chapters, range_) is not None


def phenomenon_ready(conn: sqlite3.Connection, book: str, chapters, range_) -> bool:
    row = find_new_model_passage(conn, book, chapters, range_)
    return bool(row and row["phenomena_complete_at"])


def operation_ready(conn: sqlite3.Connection, book: str, chapters, range_) -> bool:
    """Mirrors handlers/operations.py:closing_set's own live operations-completeness check —
    every live phenomenon in the passage has at least one live operation."""
    row = find_new_model_passage(conn, book, chapters, range_)
    if not row:
        return False
    passage_id = row["id"]
    phen_ids = {r["id"] for r in conn.execute(
        "SELECT id FROM phenomenon WHERE passage_id=? AND deleted=0", (passage_id,)).fetchall()}
    if not phen_ids:
        return False
    ph = ",".join("?" * len(phen_ids))
    op_phen_ids = {r["phenomenon_id"] for r in conn.execute(
        f"SELECT phenomenon_id FROM operation WHERE deleted=0 AND phenomenon_id IN ({ph})",
        tuple(phen_ids)).fetchall()}
    return phen_ids <= op_phen_ids


def closing_ready(conn: sqlite3.Connection, book: str, chapters, range_) -> bool:
    """No stored 'complete' flag for closing.set (BUILD.md §65: deliberately not cached, computed
    live). A live row in any one of the four Step-7 tables, or a non-null open_decisions_note, is
    treated as 'closing.set has run at least once for this passage' — good enough for
    orchestration/skip purposes; closing.set itself is reconciliation-gated and safe to rerun
    regardless if this under-detects."""
    row = find_new_model_passage(conn, book, chapters, range_)
    if not row:
        return False
    passage_id = row["id"]
    if row["open_decisions_note"]:
        return True
    for t in ("passage_linkage", "passage_insufficiency", "passage_emergent_question",
              "passage_validation_note"):
        n = conn.execute(f"SELECT COUNT(*) FROM {t} WHERE passage_id=? AND deleted=0",
                         (passage_id,)).fetchone()[0]
        if n:
            return True
    return False


READY_CHECKS = {
    "hib.set": hib_ready,
    "passage.build": passage_ready,
    "phenomenon.set": phenomenon_ready,
    "operation.set": operation_ready,
    "closing.set": closing_ready,
}


def is_ready(conn: sqlite3.Connection, step: str, book: str, chapters, range_) -> bool:
    check = READY_CHECKS.get(step)
    return bool(check and check(conn, book, chapters, range_))
