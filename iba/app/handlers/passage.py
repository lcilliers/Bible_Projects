"""Passage handler — register the debate's own input scope as the passage. Config-governed.

**Rule.** A passage IS the debate's input scope (`-Chapters`/`-Range`), registered verbatim, never
algorithmically sub-divided: passaging is about the capacity to digest a scope, not a narrative
structure within it. The payload carries the analyst's reading of the whole scope in light of the
HIBs already identified (`verse_hib`): a high-level story (`story_summary`) and a self-assessment of
whether the scope can be read as a whole without quality loss (`feasible`/`feasibility_note`). If
not, the step refuses (`scope-too-complex`), writes no row, and tells the operator to narrow the
scope. This handler validates, grant-checks and commits the decision.

**Reconciliation, single item.** One row per exact scope. If a live passage exists for this scope,
`story_summary`/`feasibility_note` are compared: identical is a no-op; different needs a
`reconciliation_note` (else `unreconciled`) and the row is updated in place -- same `id`,
`verse_passage` untouched -- so a correction never orphans a `phenomenon`/`operation`.

**Legacy rows.** A live legacy row (`rule IS NULL`) for the exact same scope is soft-deleted on the
one-time transition; a legacy row for another scope is left alone.
"""

from __future__ import annotations

import datetime
import json
import pathlib

from .base import Ctx, Outcome, ok, fail, escalate
from ..lib import escalation as esc, reportkit, passagetrack, versespanmeaningreport
from ..lib.debateaudit import log_change as _log_change
from ..lib.cfg import DB_PATH


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
    """PayloadPath missing/unreadable, not valid JSON, or missing a required key -- turned into a
    clean fail(), never a raw traceback."""


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

    # A verse belongs to at most one live passage (verse_passage.verse_id is unique), so a scope that
    # partly overlaps another live passage is checked before any write: a legacy overlapping passage
    # is retired whole; a new-model passage with a different scope is a conflict and refused.
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
        """Full soft-delete of a legacy passage + its verse_passage children (the legacy transition),
        logged per row."""
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
        # legacy row, exact-scope match: one-time transition, unconditional, not reconciled
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
# Reports the live verse_count distribution and escalates when a book breaches cfg_passage's
# thresholds. One escalation per invocation, not tied to every build-passages run.
def _write_quality_report(ctx: Ctx, total: int, avg: float, single: int, dist: list, by_book: list,
                          scope_sql: str, scope_args: tuple) -> pathlib.Path:
    """Persist the current distribution to the report file (governance.reports_must_persist)."""
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
    # the CSV pairing gets the same deleted=0 rows the report used (row_filter), not a full-table dump
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
    """Corpus-wide by default (no `-Book`); with `-Book`, scoped to one book (e.g. a spot-check of
    the debate-range sizes `report.passage_debate` produced). Checks each book's distribution against
    `cfg_passage` `passage.max_single_verse_pct` / `passage.max_avg_verses_per_passage` and escalates
    only if a book breaches a bound."""
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

    # per-book breach check: the single-verse-pct denominator is the book's total verse count (from
    # `verse`, via the osisId book prefix), not its passage count
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
        # decision_required resolves via Update's vocabulary (approved)
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
# Re-checks a debate file's tracked status after it is filled in by hand: write_scaffold() records
# it only once, when the file still holds the placeholder. Read-only against the debate file (it
# never regenerates it: re-running report.passage_debate on a filled range would overwrite real
# content with a blank scaffold); writes only the tracked `passage` row via
# `passagetrack.record_debate`.
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


# ── passage.suggest_boundary ──────────────────────────────────────────────────────────────────
# Read-only, no table write (#1383). Proposes a candidate next passage boundary from cheap proxy
# signals only (narrative_morph density, the legacy bible_research.db.verse.genre book-level tag, a
# chapter-boundary stop) -- not the genre determination itself (proxy-signals-not-genre-
# determination). It only proposes; the researcher confirms, and `passage.build` registers
# (human-confirmation-gate). The coherence test is a simple binary: is this verse's narrative_morph
# density on the same side of a >0/=0 split as the block's first verse.
def _research_db_path(iba_conn) -> str:
    import json as _json
    row = iba_conn.execute(
        "SELECT value FROM cfg_setting WHERE key='database.bible_research.path'").fetchone()
    if not row:
        raise RuntimeError("no database.bible_research.path setting -- run Start-Iba.ps1 first")
    rel = _json.loads(row[0])
    repo_root = DB_PATH.resolve().parent.parent.parent.parent
    return str(repo_root / rel)


def _legacy_genre_tag(ctx: Ctx, osis: str) -> str | None:
    """Cross-database read: the legacy coarse genre tag lives in bible_research.db.verse. Returns None
    (never raises) if the legacy DB/table/row isn't reachable; a missing signal narrows the
    proposal's signal_summary, it never blocks it."""
    import sqlite3 as _sqlite3
    try:
        path = _research_db_path(ctx.db.conn)
        rconn = _sqlite3.connect(path)
        try:
            row = rconn.execute(
                "SELECT genre FROM verse WHERE osisId=?", (osis,)).fetchone()
            return row[0] if row else None
        finally:
            rconn.close()
    except Exception:
        return None


def _parse_chapter_verse(osis: str, book: str) -> tuple[int, int] | None:
    """`verse` has no chapter/verse columns: derived by parsing `osisId`, as
    `versespanmeaningreport.fetch_verses` does."""
    parts = (osis or "").split(".")
    if len(parts) != 3 or parts[0] != book or not parts[1].isdigit() or not parts[2].isdigit():
        return None
    return int(parts[1]), int(parts[2])


def suggest_boundary(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    max_verses = int(ctx.cfg.required_module_setting("cfg_passage", "passage.max_verses"))

    all_verses = ctx.db.rows(
        "SELECT id, osisId FROM verse WHERE osisId LIKE ? AND deleted=0", (f"{book}.%",))
    passaged_ids = {r["verse_id"] for r in ctx.db.rows(
        "SELECT verse_id FROM verse_passage WHERE deleted=0")}
    parsed = []
    for r in all_verses:
        cv = _parse_chapter_verse(r["osisId"], book)
        if cv is None:
            continue
        parsed.append({"id": r["id"], "osisId": r["osisId"], "chapter": cv[0], "verse": cv[1],
                       "passaged": r["id"] in passaged_ids})
    parsed.sort(key=lambda v: (v["chapter"], v["verse"]))

    start = next((v for v in parsed if not v["passaged"]), None)
    if start is None:
        return fail("book-complete",
                   f"every verse in {book} already belongs to a live passage — nothing to suggest")

    candidates = [v for v in parsed
                 if v["chapter"] == start["chapter"] and v["verse"] >= start["verse"]]

    def density(verse_id: int) -> float:
        rows = ctx.db.rows(
            "SELECT COUNT(*) n, SUM(CASE WHEN narrative_morph IS NOT NULL THEN 1 ELSE 0 END) hit "
            "FROM verse_lexical WHERE verse_id=? AND deleted=0", (verse_id,))
        n, hit = rows[0]["n"], rows[0]["hit"] or 0
        return (hit / n) if n else 0.0

    block: list[dict] = []
    baseline_side = None
    genre_tags: set[str] = set()
    for v in candidates:
        d = density(v["id"])
        side = d > 0
        if baseline_side is None:
            baseline_side = side
        elif side != baseline_side:
            break
        if len(block) >= max_verses:
            break
        block.append(v)
        tag = _legacy_genre_tag(ctx, v["osisId"])
        if tag:
            genre_tags.add(tag)

    if not block:
        return fail("no-stable-boundary",
                   f"could not find a stable boundary starting at {start['osisId']} — manual "
                   f"passage.build registration needed")

    end = block[-1]
    end_ref = f"{end['chapter']}:{end['verse']}"
    start_ref = f"{start['chapter']}:{start['verse']}"
    summary = {
        "narrative_morph_density_side": "present" if baseline_side else "absent",
        "legacy_genre_tags_seen": sorted(genre_tags),
        "stopped_at": ("book-boundary" if len(block) == len(candidates) else
                      ("verse-cap" if len(block) >= max_verses else "signal-break")),
    }
    proposal = {"book": book, "start_ref": start_ref, "end_ref": end_ref,
               "verse_count": len(block), "signal_summary": summary}
    return ok(f"{book} {start_ref}-{end_ref}: {len(block)} verse(s) proposed — {summary} — "
             f"confirm with Build-Passages.ps1 -Suggest -Confirm, or adjust -Chapters/-Range and "
             f"resubmit", **proposal)
