"""passagetrack.py — the completion-tracking record for the verse-fanout method (`report.
verse_span_meaning` + `report.passage_debate`), built on the repurposed `passage`/`verse_passage`
tables (`migration/repurpose_passage_tracking.py`; the tables' prior candidate-driven use is
retired, BUILD.md §23 — the retired 18,504/24,763 rows stay, `deleted=1`, untouched).

One `passage` row per distinct book/range that has been run through either report step,
cross-referenced to every verse it covers via `verse_passage` — so a book's completion can be
read off directly (which verses have zero passage coverage yet) and any verse can be traced back
to its passage, its extract, and its debate.

**What this deliberately does NOT do.** It does not digest the debate's analytical content
(operations, subjects, decisions) into the DB — the researcher's own words, 2026-07-27: "I have
not yet decided on how to digest the detail of the debate into the DB, this is still emerging."
`debate_status` is a coarse, mechanical signal only (does the file still contain an unreplaced
`<!-- fill in -->` placeholder?), not a content model.

Called from `handlers/reports.py`'s two report handlers on a successful write — `record_extract`
after `report.verse_span_meaning`, `record_debate` after `report.passage_debate` — so the record
updates in the same run that produces the file, per the researcher's explicit requirement that
this be "linked into the run," not a separate manual bookkeeping step.
"""

from __future__ import annotations

import datetime
import pathlib

from .versespanmeaningreport import fetch_verses

FILL_IN_MARKER = "<!-- fill in -->"


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _grant(cfg, writer: str, table: str):
    if table not in cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r} "
                              f"(cfg_write_grant)")


def _find_live_passage(conn, book: str, sc: int, sv: int, ec: int, ev: int):
    return conn.execute(
        "SELECT * FROM passage WHERE book=? AND start_chapter=? AND start_verse=? AND "
        "end_chapter=? AND end_verse=? AND deleted=0", (book, sc, sv, ec, ev)).fetchone()


def _upsert_passage(cfg, writer: str, book: str, book_label: str, verses: list[dict],
                    **fields) -> int:
    """fields are the writer-specific columns to set (verse_span_meaning_* or debate_*).
    Range identity (book/start/end/verse_count/ref/anchor) is always derived from `verses`
    itself, not from the caller's lo/hi/verse_lo/verse_hi — works uniformly whether the run was
    -Chapters or -Range (see module callers)."""
    _grant(cfg, writer, "passage")
    conn = cfg.conn
    sc, sv = verses[0]["chapter"], verses[0]["verse"]
    ec, ev = verses[-1]["chapter"], verses[-1]["verse"]
    ref = f"{book} {sc}:{sv}-{ev}" if sc == ec else f"{book} {sc}:{sv}-{ec}:{ev}"
    anchor_verse_id = verses[0]["id"]

    row = _find_live_passage(conn, book, sc, sv, ec, ev)
    if row:
        sets = ", ".join(f'"{k}"=?' for k in fields)
        conn.execute(f'UPDATE passage SET {sets} WHERE id=?', [*fields.values(), row["id"]])
        return row["id"]

    cols = ["book", "book_label", "anchor_verse_id", "start_chapter", "start_verse",
           "end_chapter", "end_verse", "ref", "verse_count", "created_at", "deleted", *fields]
    vals = [book, book_label, anchor_verse_id, sc, sv, ec, ev, ref, len(verses), _now(), 0,
           *fields.values()]
    ph = ",".join("?" * len(cols))
    cur = conn.execute(f'INSERT INTO passage ({",".join(cols)}) VALUES ({ph})', vals)
    return cur.lastrowid


def _sync_verse_passage(cfg, writer: str, passage_id: int, verses: list[dict],
                        anchor_verse_id: int):
    """Every verse in `verses` ends up pointing (live, deleted=0) at `passage_id`. A verse
    previously live-linked to a DIFFERENT passage (range boundaries changed on a re-run) has
    that old link soft-deleted first — `verse_id` may have at most one LIVE passage link
    (idx_verse_passage_verse_id_live), the same invariant the old system declared, now enforced
    for live rows only."""
    _grant(cfg, writer, "verse_passage")
    conn = cfg.conn
    for v in verses:
        existing = conn.execute(
            "SELECT id, passage_id FROM verse_passage WHERE verse_id=? AND deleted=0",
            (v["id"],)).fetchone()
        is_anchor = 1 if v["id"] == anchor_verse_id else 0
        if existing and existing["passage_id"] == passage_id:
            conn.execute("UPDATE verse_passage SET is_anchor=? WHERE id=?",
                        (is_anchor, existing["id"]))
            continue
        if existing:
            conn.execute("UPDATE verse_passage SET deleted=1 WHERE id=?", (existing["id"],))
        conn.execute(
            "INSERT INTO verse_passage (passage_id, verse_id, is_anchor, created_at, deleted) "
            "VALUES (?,?,?,?,0)", (passage_id, v["id"], is_anchor, _now()))


def record_extract(cfg, book: str, lo: int, hi: int, verse_lo: int | None, verse_hi: int | None,
                   book_label: str | None, path: pathlib.Path) -> int:
    writer = "report.verse_span_meaning"
    verses = fetch_verses(cfg.conn, book, lo, hi, verse_lo, verse_hi)
    label = book_label or book
    passage_id = _upsert_passage(
        cfg, writer, book, label, verses,
        verse_span_meaning_path=str(path), verse_span_meaning_written_at=_now())
    _sync_verse_passage(cfg, writer, passage_id, verses, verses[0]["id"])
    return passage_id


def record_debate(cfg, book: str, lo: int, hi: int, verse_lo: int | None, verse_hi: int | None,
                  book_label: str | None, path: pathlib.Path) -> int:
    writer = "report.passage_debate"
    verses = fetch_verses(cfg.conn, book, lo, hi, verse_lo, verse_hi)
    label = book_label or book
    status = "scaffold" if FILL_IN_MARKER in path.read_text(encoding="utf-8") else "filled"
    passage_id = _upsert_passage(
        cfg, writer, book, label, verses,
        debate_path=str(path), debate_written_at=_now(), debate_status=status)
    _sync_verse_passage(cfg, writer, passage_id, verses, verses[0]["id"])
    return passage_id
