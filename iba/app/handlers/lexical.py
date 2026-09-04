"""lexical.py — dispatcher handler for `lexical.build`/`lexical.enrich` (work package
`verse-lexical`, ordinals 0/2). `build` is a thin adapter over `lib/lexical.py`'s
`build_for_range`, same shape as `handlers/reports.py:verse_span_meaning_report` (the step this
replaces). `enrich` is a thin adapter over `lib/lexicalenrich.py` — payload loading + passage
resolution + write-grant checks live here (handler layer), the actual reconciliation/write logic
lives in `lib/lexicalenrich.py` (escalation #1383, build spec §C.2/§E.2).

Auto-backfill reused unchanged from `report.verse_span_meaning`'s own pattern (`report.
auto_backfill_before_render`, `raw.backfill_meaning_for`) — a content-role code with no `strong`
row yet gets pulled from STEP before building, same researcher instruction (2026-07-26), same
setting, not a new one.
"""

from __future__ import annotations

import json
import pathlib

from .base import Ctx, Outcome, fail, ok
from . import raw as raw_mod
from ..lib import lexical, lexicalenrich, passagetrack
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

    totals = lexical.build_for_range(ctx.db.conn, book, lo, hi, verse_lo, verse_hi, step)
    ctx.db.conn.commit()

    return ok(
        f"{book} {lo}-{hi}: {totals['verses']} verse(s), {totals['spans']} span(s), "
        f"{totals['codes']} code(s) resolved ({totals['inserted']} written, "
        f"{totals['superseded']} superseded){backfill_note}",
        **totals)


# ── lexical.enrich ──────────────────────────────────────────────────────────────────────────────
# payload: {"book": "Dan", "genre": "narrative", "notes": [
#   {"verse": "Dan.1.8", "position": 3, "code_ordinal": 0, "note_type": "connective",
#    "resolution_status": "resolved", "finding": "...", "evidence": "...",
#    "target_verse": "...", "target_position": N,        <- optional (pronoun_resolution etc.)
#    "related_codes": [{"verse": "...", "position": N}],  <- optional (structural_pattern etc.)
#    "reconciliation_note": "..."},                       <- required only when correcting
#  ...],
#  "remove": [{"verse": "...", "position": N, "note_type": "...", "reason": "..."}]}
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


def enrich(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    if ctx.params.get("Range"):
        ch, vlo, vhi = parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None

    try:
        payload = _load_payload(ctx)
        if payload.get("book") != book:
            return fail("payload-mismatch",
                       f"payload book {payload.get('book')!r} != -Book {book!r}")
        notes = payload.get("notes", [])
        removals = payload.get("remove", [])
        genre = payload.get("genre")
    except (BadPayload, KeyError) as e:
        return fail("bad-payload", str(e))
    if not notes and not removals:
        return fail("empty-payload", "payload has no 'notes' or 'remove' entries")

    passage_row = passagetrack.find_tracked_passage(ctx.db.conn, book, lo, hi, verse_lo, verse_hi)
    if passage_row is None:
        return fail("no-passage",
                   f"no tracked passage for {book} this range — run Build-Passages.ps1 "
                   f"(passage.build) first")
    passage_id = passage_row["id"]

    verse_rows = ctx.db.rows(
        "SELECT v.id, v.osisId FROM verse v JOIN verse_passage vp ON vp.verse_id=v.id "
        "WHERE vp.passage_id=? AND vp.deleted=0 AND v.deleted=0", (passage_id,))
    verse_ids = [r["id"] for r in verse_rows]
    verse_id_by_osis = {r["osisId"]: r["id"] for r in verse_rows}

    max_verses = int(ctx.cfg.required_module_setting("cfg_passage", "passage.max_verses"))
    if len(verse_ids) > max_verses:
        return fail("too-many-verses",
                   f"{len(verse_ids)} verses exceeds the {max_verses}-verse cap — split into "
                   f"smaller passage-blocks")

    _may(ctx, "lexical.enrich", "verse_lexical_note")
    _may(ctx, "lexical.enrich", "passage")

    # Real bug found live testing this handler (escalation #1450, 2026-09-04): the completeness
    # check used to run AFTER enrich_passage()'s writes, with the incomplete branch calling
    # commit() -- which committed the whole pending transaction, notes included, on exactly the
    # failure path documented as "never a partial write" (design spec §E.2). Fixed: on
    # incomplete-block, ROLLBACK instead of commit -- verified live (5 test notes written then
    # correctly discarded, 0 live verse_lexical_note rows after the rollback).
    try:
        counts = lexicalenrich.enrich_passage(ctx.db.conn, passage_id, verse_ids, verse_id_by_osis,
                                              genre, notes, removals)
    except lexicalenrich.UnresolvedReference as e:
        ctx.db.conn.rollback()
        return fail("unresolved-reference",
                   f"{len(e.problems)} problem(s): "
                   f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")
    except lexicalenrich.ReconciliationError as e:
        ctx.db.conn.rollback()
        return fail("unreconciled",
                   f"{len(e.problems)} item(s) need reconciliation before this can write: "
                   f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

    complete, missing = lexicalenrich.check_completeness(ctx.db.conn, passage_id, verse_ids)
    if not complete:
        ctx.db.conn.rollback()
        return fail("incomplete-block",
                   f"{len(missing)} code(s) in this block have no disposition: "
                   f"{missing[:5]}{' ...' if len(missing) > 5 else ''} — every applicable code "
                   f"needs a finding or an explicit checked_empty/unresolved")

    lexicalenrich.set_lexical_complete(ctx.db.conn, passage_id, True)
    ctx.db.conn.commit()

    return ok(f"{book} {lo}-{hi} (passage {passage_id}): {counts['unchanged']} unchanged, "
             f"{counts['new']} new, {counts['changed']} corrected, {counts['removed']} removed "
             f"note(s); block complete, lexical_complete_at set", **counts)
