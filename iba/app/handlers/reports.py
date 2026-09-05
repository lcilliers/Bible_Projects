"""reports handlers — thin dispatcher adapters over report.py / validation.py.

Both modules already had their own reusable generate functions (report.generate, validation.
generate/generate_book); this just wraps them in the standard `def h(ctx) -> Outcome` contract so
they're registered work packages/steps like everything else in the app, instead of standalone
scripts nothing else knows about — the same gap configuration_maintenance closed for
cfgload/cfgcheck/cfgreport. Mostly read-only — the one exception is
`verse_span_meaning_report` (see `report.auto_backfill_before_render`, 2026-07-26): it may write
to the raw/lexicon-parsed layer via `raw.backfill_meaning_for`, gated by that setting, before
rendering. Every other report here writes nothing to the DB.
"""

from __future__ import annotations

import pathlib

from .base import Ctx, Outcome, ok, fail, escalate
from . import raw as raw_mod
from .. import report as report_mod
from .. import validation as validation_mod
from ..lib import contentindex as contentindex_mod
from ..lib import escalation as esc
from ..lib import manifest as manifest_mod
from ..lib import retention as retention_mod
from ..lib import (cataloguereport, clusterreport, registryreport, schemareport, seedreport,
                   spanreport, strongreport, strongversereport, wordregistryspanreport)
from ..lib import (lexical, passagedebatereport, passagetrack, reportkit, versespanmeaningreport,
                   wholebookread)
from ..lib.stepapi import StepUnavailable
from ..tools import export_tables_csv


def word_report(ctx: Ctx) -> Outcome:
    out = report_mod.generate(ctx.params["Word"], cfg=ctx.cfg)
    if out is None:
        return fail("word-not-found", f"{ctx.params['Word']!r} is not in the DB")
    return ok(f"wrote {out}", path=str(out))


# Researcher's standing rule, 2026-07-30: "if a validation runs for a module operation... it would
# escalate and record an escalation report." Found live: validation_word/validation_book computed
# real PASS/WARN/FAIL verdicts but ALWAYS returned ok() regardless — a hard FAIL never surfaced as
# anything but a number inside a message string. Both now follow the same escalate-on-finding shape
# every other quality check in this app already uses (passage.validate/lexicon.validate/
# configmaint.validate) — clean is still a plain ok(), a FAIL/WARN escalates once per run.
def _validation_outcome(ctx: Ctx, scope_label: str, out, overall: str, p: int, w: int, f: int
                        ) -> Outcome:
    if overall == "PASS":
        return ok(f"{overall} ({p} pass, {w} warn, {f} fail) -> {out}",
                 path=str(out), overall=overall, passes=p, warns=w, fails=f)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        # escalation #798/#799 SS4: decision_required now resolves via Update()'s manual
        # vocabulary (approved) not AnswerRun's dispatcher vocabulary (approve).
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {overall} ({p} pass, {w} warn, {f} fail) -> {out} — "
                      f"researcher confirmed these findings are known/acceptable",
                      path=str(out), overall=overall, passes=p, warns=w, fails=f)
        if decision == "reject":
            return fail("findings-rejected",
                       f"researcher flagged {scope_label}'s validation findings as needing action",
                       path=str(out), overall=overall, passes=p, warns=w, fails=f)
        return fail("needs-revision", f"researcher comment: {answered['comment'] or '(none)'}")

    # escalation #798/#799 SS3.7 (researcher, 2026-08-22): built now as uniformly
    # decision_required, per instruction -- the per-check classification (some findings look like
    # real code bugs, some like genuine open questions, per the design doc's own worked examples
    # from validation.py) is NOT built in this pass.
    return escalate(
        "needs-review",
        question=f"Validation for {scope_label}: {overall} ({p} pass, {w} warn, {f} fail) — see "
                 f"{out} for full detail. Approve to acknowledge as known/acceptable, reject to "
                 f"flag for action, or revise with a comment.",
        preset={"scope": scope_label, "overall": overall, "passes": p, "warns": w, "fails": f,
               "report_path": str(out)},
        tried=f"ran the full validation report — {out}",
        resolution_kind="decision_required")


def validation_word(ctx: Ctx) -> Outcome:
    out, overall, (p, w, f) = validation_mod.generate(ctx.params["Word"])
    return _validation_outcome(ctx, f"word {ctx.params['Word']!r}", out, overall, p, w, f)


def validation_book(ctx: Ctx) -> Outcome:
    out, overall, (p, w, f) = validation_mod.generate_book(ctx.params["Book"])
    return _validation_outcome(ctx, f"book {ctx.params['Book']!r}", out, overall, p, w, f)


def manifest_rebuild(ctx: Ctx) -> Outcome:
    """Full rescan of the whole project tree — filename/path metadata only. See lib/manifest.py."""
    summary = manifest_mod.rebuild(ctx.cfg)
    path = pathlib.Path(ctx.cfg.required_setting("manifest.report_path"))
    out = manifest_mod.write_rebuild_report(ctx.cfg, path, summary)
    return ok(f"wrote {out} ({summary['total']} files: {summary['active']} active, "
             f"{summary['archived']} archived)", path=str(out), total=summary["total"],
             active=summary["active"], archived=summary["archived"])


def manifest_search(ctx: Ctx) -> Outcome:
    """Field:value or free-text search against file_manifest. -Query is a per-call parameter (like
    table_export's -Table), not config — a search term isn't a policy anyone proposes to change."""
    query = ctx.params.get("Query")
    if not query:
        return fail("missing-query", "manifest.search requires a -Query parameter")
    results = manifest_mod.search(ctx.cfg, query)
    out = manifest_mod.write_search_report(ctx.cfg, query, results)
    return ok(f"{len(results)} match(es) for {query!r} — wrote {out}", path=str(out),
             matches=len(results))


def content_index_rebuild(ctx: Ctx) -> Outcome:
    """Full rescan of every .md file in file_manifest (round 2 of manifest + content-search — see
    lib/contentindex.py). Requires manifest.rebuild to have run at least once; content_index's
    coverage never exceeds file_manifest's."""
    summary = contentindex_mod.rebuild(ctx.cfg)
    path = pathlib.Path(ctx.cfg.required_setting("content_index.report_path"))
    out = contentindex_mod.write_rebuild_report(ctx.cfg, path, summary)
    return ok(f"wrote {out} ({summary['files_scanned']} files scanned, "
             f"{summary['total_hits']} key occurrence(s) indexed)", path=str(out),
             files_scanned=summary["files_scanned"], total_hits=summary["total_hits"])


def content_index_search(ctx: Ctx) -> Outcome:
    """Incremental refresh then a key_type:value (strong:H2734, gloss:anger, word:anger) or
    bare-value lookup against content_index. -Query is a per-call parameter, not config — same
    reasoning as manifest_search's -Query. -Csv (optional, any non-empty value) also writes the
    FULL result set as .csv — the .md report caps at 500 rows for readability, a large query
    (gloss:compassion, 23,098+ hits) needs the untruncated set for real spreadsheet review."""
    query = ctx.params.get("Query")
    if not query:
        return fail("missing-query", "content_index.search requires a -Query parameter")
    hits, refresh_summary = contentindex_mod.search(ctx.cfg, query)
    out = contentindex_mod.write_search_report(ctx.cfg, query, hits, refresh_summary)
    result = {"path": str(out), "matches": len(hits),
             "files_rescanned": refresh_summary["files_scanned"]}
    message = f"{len(hits)} match(es) for {query!r} — wrote {out}"
    if ctx.params.get("Csv"):
        csv_out = contentindex_mod.write_search_csv(ctx.cfg, query, hits)
        result["csv_path"] = str(csv_out)
        message += f" and {csv_out}"
    return ok(message, **result)


def content_index_size_profile(ctx: Ctx) -> Outcome:
    """Every .md file in file_manifest, largest first -- for visual review before deciding
    cfg_content_index_exclude entries. Read-only, no exclusions applied (see lib/contentindex.py)."""
    rows = contentindex_mod.size_profile(ctx.cfg)
    out = contentindex_mod.write_size_profile_report(ctx.cfg, rows)
    total_mb = sum(r["size_mb"] for r in rows)
    return ok(f"wrote {out} ({len(rows)} files, {total_mb:.1f} MB total)", path=str(out),
             files=len(rows), total_mb=round(total_mb, 1))


def retention_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.required_setting("retention.report_path"))
    out = retention_mod.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def table_export(ctx: Ctx) -> Outcome:
    """CSV dump of every DATA table, verbatim — config governs its own concerns; the DEDICATED
    config report writer (configmaint.report) already owns cfg_* content, so this excludes it
    (found 2026-07-22 — the tool used to dump cfg_* too, a real duplication bug). -Out/-Table stay
    plain PS parameters (a one-off destination/subset override), not config — same boundary the
    researcher drew 2026-07-22: a parameter explained in the script's own inline help isn't a
    setting just because the script is now dispatcher-registered. -Database (added 2026-08-29,
    escalation #1007) is the same kind of plain override, resolved via `ctx.cfg.database_path` —
    the registered project_database enum, not a literal path — so this can dump bible_research.db
    tables (e.g. the observation-question catalogue) as readily as iba.db's own.

    `table_export.output_dir` is a per-database map (same JSON-map shape as `prose.
    book_output_dir`), not a single path — changed same day, once cross-database dumping made a
    single flat folder mix iba.db and bible_research.db CSVs together (found live: this handler's
    own first bible_research run landed right next to iba.db's, in `Workflow/schema/`, no
    separation at all). A database missing from the map is a real config gap, not something to
    default around — same "unknown book raises" posture `prosestore.output_dir_for` already
    established for the equivalent gap there."""
    only = ctx.params.get("Table")
    only = only.split(",") if isinstance(only, str) else only
    database = ctx.params.get("Database") or "iba"
    db_path = ctx.cfg.database_path(database) if database != "iba" else None
    out_override = ctx.params.get("Out")
    if out_override:
        out_dir = pathlib.Path(out_override)
    else:
        dir_map = ctx.cfg.setting("table_export.output_dir", {})
        if database not in dir_map:
            raise KeyError(f"table_export.output_dir has no entry for database {database!r} — "
                          f"registered: {sorted(dir_map)}")
        out_dir = pathlib.Path(dir_map[database])
    results = export_tables_csv.export(out_dir, only, db_path)
    return ok(f"exported {len(results)} table(s) from {database!r} to {out_dir}", path=str(out_dir),
             tables=len(results))


def seed_candidate_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.required_setting("report.seed_candidate_path"))
    out = seedreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def strong_meaning_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.required_setting("report.strong_meaning_path"))
    out = strongreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def word_registry_span_report(ctx: Ctx) -> Outcome:
    out = wordregistryspanreport.write_report(ctx.cfg, ctx.params["Word"])
    if out is None:
        return fail("word-not-found", f"{ctx.params['Word']!r} is not in the registry")
    return ok(f"wrote {out}", path=str(out))


def strong_verse_report(ctx: Ctx) -> Outcome:
    """`ctx.word_id` is already resolved by the dispatcher (run.py: any step with 'Word' in
    params gets `wrow = db.get('word_registry', word=params['Word'])` before the handler runs) —
    reused here rather than a second lookup. Word-not-found is therefore a dispatcher-level fact,
    not something this handler re-derives."""
    if ctx.word_id is None:
        return fail("word-not-found", f"{ctx.params['Word']!r} is not in the registry")
    strong = ctx.params["Strong"]
    linked = ctx.db.rows(
        "SELECT 1 FROM word_strong WHERE word_id=? AND strong=? AND deleted=0",
        (ctx.word_id, strong))
    if not linked:
        return fail("strong-not-linked",
                    f"{strong!r} is not linked to registry word {ctx.params['Word']!r} "
                    f"(word_strong) — check the word's own -strong-span- report for its linked "
                    f"Strong's list")
    out = strongversereport.write_report(ctx.cfg, ctx.params["Word"], strong, ctx.word_id)
    return ok(f"wrote {out}", path=str(out))


def span_analysis_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.required_setting("report.span_analysis_path"))
    out = spanreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def verse_span_meaning_report(ctx: Ctx) -> Outcome:
    """Book-scoped, needs -Book plus exactly one of -Chapters/-Range. STEP-dependent (AMBIGUOUS-
    span live disambiguation) — versespanmeaningreport.write_report() reads step.required_for_runs
    itself and raises StepUnavailable when required and down; caught here into a clean fail(),
    resolved by cfg_on_fail(report.verse_span_meaning, unreachable) rather than crashing the run.

    `report.auto_backfill_before_render` (cfg_setting, module `report`, default True — researcher's
    direct 2026-07-26 instruction, answering the open question left by the prior session): before
    rendering, run the identical pull `Raw-Backfill.ps1` does (raw.backfill_meaning_for) for any
    span in this exact book+range whose strong is not yet registered. A report is never silently
    left at partial coverage waiting on a separate manual step. Set False to go back to a pure
    read-only render (STEP-down still refuses rendering if step.required_for_runs is True, exactly
    as before — this setting only controls whether a gap gets auto-filled, not whether STEP itself
    is required)."""
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    if ctx.params.get("Range"):
        ch, vlo, vhi = versespanmeaningreport.parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = versespanmeaningreport.parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None
    backfill_note = ""
    try:
        if ctx.cfg.setting("report.auto_backfill_before_render", True):
            result = raw_mod.backfill_meaning_for(ctx, book, lo, hi, verse_lo, verse_hi)
            if result["missing_before"]:
                backfill_note = (f" (auto-backfilled {result['missing_before']} previously-"
                                 f"unregistered strong(s) before rendering)")
        out = versespanmeaningreport.write_report(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                                  book_label=book_label)
    except StepUnavailable as e:
        return fail("unreachable", str(e))
    passage_id = passagetrack.record_extract(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                             book_label, out)
    return ok(f"wrote {out}{backfill_note}", path=str(out), passage_id=passage_id)


def lexical_report(ctx: Ctx) -> Outcome:
    """Book-scoped, needs -Book plus exactly one of -Chapters/-Range, same call shape as
    `verse_span_meaning_report` (the step this replaces). Pure render off `verse_lexical` —
    no STEP dependency, no backfill, no DB write here at all; `lexical.build` (ordinal 0 of
    the same `verse-lexical` work package) is what populates the table this reads. `no-
    readings` fires when nothing has been built yet for this exact range (`cfg_on_fail` resolves
    the message, matching every other step's convention)."""
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    if ctx.params.get("Range"):
        ch, vlo, vhi = versespanmeaningreport.parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = versespanmeaningreport.parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None

    built = ctx.db.conn.execute(
        "SELECT 1 FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
        "WHERE v.osisId LIKE ? AND vl.deleted=0 LIMIT 1", (f"{book}.%",)).fetchone()
    if not built:
        return fail("no-readings", f"no verse_lexical rows exist yet for {book} {lo}-{hi} — "
                                   f"run lexical.build first")

    out = lexical.write_report(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                               book_label=book_label)
    return ok(f"wrote {out}", path=str(out))


def lexical_exceptions_report(ctx: Ctx) -> Outcome:
    """Escalation #1383, build spec §G.1 — the per-run self-audit / exception report for the most
    recent `lexical.enrich` run over this verse range. Read-only against `verse_lexical`/
    `verse_lexical_note`; never an independent write. Deliberately a plain tally against Layer 1's
    complete enumeration, no "confirms"/"validates"/"closes the gap" framing (method-and-drift-
    mitigation doc's own corrected Layer-3 discipline, baked into the template's own structure).

    Verse-scoped since escalation #1451 (2026-09-05, full record `iba/docs/1451-window1-layer2-
    verse-scoped-redesign-v1-20260905.md`) — no `passage` row is resolved or required, same
    correction already made to `handlers/lexical.py:enrich()`. Found live producing this report
    for the first time against real #1451 output: every one of the 10 test verses has no `passage`
    row by design, so the old `passagetrack.find_tracked_passage`/`no-passage` gate would have
    refused all 10. Verses now resolve directly via `fetch_verses`, and both queries below filter
    by `verse_id` instead of joining through `verse_passage`/`passage_id`."""
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    if ctx.params.get("Range"):
        ch, vlo, vhi = versespanmeaningreport.parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = versespanmeaningreport.parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None

    fetched = versespanmeaningreport.fetch_verses(ctx.db.conn, book, lo, hi, verse_lo, verse_hi)
    if not fetched:
        return fail("no-verses", f"{book} this range has no live verse rows")
    verse_ids = [v["id"] for v in fetched]
    ph = ",".join("?" * len(verse_ids))

    vl_rows = ctx.db.rows(
        f"SELECT vl.id, vl.strong, vl.role, vl.is_negator, vl.narrative_morph, "
        f"vl.gloss_consistent_in_verse, v.osisId FROM verse_lexical vl "
        f"JOIN verse v ON v.id=vl.verse_id "
        f"WHERE vl.verse_id IN ({ph}) AND vl.deleted=0", tuple(verse_ids))
    n_negators = sum(1 for r in vl_rows if r["is_negator"])
    n_narrative = sum(1 for r in vl_rows if r["narrative_morph"])
    n_gloss_bad = sum(1 for r in vl_rows if r["gloss_consistent_in_verse"] == 0)

    note_rows = ctx.db.rows(
        f"SELECT note_type, resolution_status, value_text FROM verse_lexical_note "
        f"WHERE verse_id IN ({ph}) AND deleted=0", tuple(verse_ids))
    by_status: dict[str, list] = {}
    for r in note_rows:
        by_status.setdefault(r["resolution_status"], []).append(r)
    connectives = [r for r in note_rows if r["note_type"] == "connective"]
    n_unclassified_conn = sum(1 for r in connectives if (r["value_text"] or "") == "UNCLASSIFIED")

    # Standing integrity check (escalation #1520 root-cause fix, §D of `iba/docs/1520-verse-
    # lexical-crud-safety-review-v1-20260905.md`): a live note whose verse_lexical_id/
    # target_verse_lexical_id points at a soft-deleted verse_lexical row is a genuine dangling
    # reference (the code slot it names truly no longer exists — `write_readings_for_span`'s
    # identity-stable write only ever deletes a slot for real when it disappears from the span).
    # Should always be 0; surfaced here rather than only discoverable via a failed enrich call.
    orphaned_anchor = ctx.db.rows(
        f"SELECT n.id, n.note_type FROM verse_lexical_note n "
        f"JOIN verse_lexical vl ON vl.id=n.verse_lexical_id "
        f"WHERE n.verse_id IN ({ph}) AND n.deleted=0 AND vl.deleted=1", tuple(verse_ids))
    orphaned_target = ctx.db.rows(
        f"SELECT n.id, n.note_type FROM verse_lexical_note n "
        f"JOIN verse_lexical vl ON vl.id=n.target_verse_lexical_id "
        f"WHERE n.verse_id IN ({ph}) AND n.deleted=0 AND n.target_verse_lexical_id IS NOT NULL "
        f"AND vl.deleted=1", tuple(verse_ids))

    layer1 = [
        f"- codes processed: {len(vl_rows)}",
        f"- negators found: {n_negators}",
        f"- narrative_morph fired: {n_narrative}",
        f"- gloss_consistent_in_verse=0 (data-quality): {n_gloss_bad}",
        f"- connective notes: {len(connectives)} ({n_unclassified_conn} UNCLASSIFIED — points at "
        f"the lexicon)",
    ]
    layer2 = [f"- {status}: {len(items)}" for status, items in sorted(by_status.items())]
    if not layer2:
        layer2 = ["- (no verse_lexical_note rows for this passage yet)"]
    judgement = [f"- {r['note_type']}/{r['resolution_status']}: {r['value_text'] or '(no finding text)'}"
                for r in note_rows if r["resolution_status"] not in ("checked_empty",)]
    if not judgement:
        judgement = ["- (none recorded)"]

    n_orphaned = len(orphaned_anchor) + len(orphaned_target)
    if n_orphaned:
        integrity = [f"- **{n_orphaned} DANGLING reference(s) — action needed**:",
                    f"  - {len(orphaned_anchor)} note(s) anchored on a deleted verse_lexical row",
                    f"  - {len(orphaned_target)} note(s) targeting a deleted verse_lexical row"]
    else:
        integrity = ["- 0 dangling references (verse_lexical_id/target_verse_lexical_id all "
                    "point at live rows)"]

    sections = {"layer1_tally": layer1, "layer2_dispositions": layer2, "judgement_calls": judgement,
               "integrity": integrity}
    intro = [f"> Generated by `report.lexical_exceptions` for {book} {ctx.params.get('Range') or ctx.params.get('Chapters')} "
            f"({len(verse_ids)} verse(s)). Read-only against verse_lexical/verse_lexical_note. "
            f"No `passage` row involved — verse-scoped (escalation #1451)."]
    L = reportkit.render_scaffold(ctx.db.conn, "report.lexical_exceptions", sections, intro=intro,
                                  book=book, range=(ctx.params.get("Range") or ctx.params.get("Chapters")))
    output_dir = pathlib.Path(ctx.cfg.required_setting("report.verse_analysis_output_dir"))
    range_str = versespanmeaningreport._range_str(lo, hi, verse_lo, verse_hi)
    path = output_dir / (book_label or book) / f"{book.lower()}-{range_str}-lexical-exceptions.md"
    path = reportkit.write_report(ctx.db.conn, "report.lexical_exceptions", path, L)
    return ok(f"wrote {path}", path=str(path), codes=len(vl_rows), notes=len(note_rows),
             dangling_references=n_orphaned)


# ── report.lexical_extract ──────────────────────────────────────────────────────────────────────
def _parse_filter_list(raw: str) -> list[str]:
    return [v.strip() for v in raw.split(",") if v.strip()]


def lexical_extract(ctx: Ctx) -> Outcome:
    """Escalation #1383, build spec §G.2 — multi-filter JSON extract over verse_lexical/
    verse_lexical_note, feeding Stage 2's own input assembly. Read-only. Every filter accepts a
    single value or a comma-list; a `verse` filter also accepts an OSIS reference range
    (`Gen.1.1-Gen.1.10`). Filters combine with AND across keys, OR within one key's list.
    Omitting every filter is refused (`no-filter`) — this step is never an unbounded full-corpus
    dump."""
    passage_f = ctx.params.get("PassageFilter")
    verse_f = ctx.params.get("VerseFilter")
    surface_f = ctx.params.get("SurfaceFilter")
    strong_f = ctx.params.get("StrongFilter")
    if not any([passage_f, verse_f, surface_f, strong_f]):
        return fail("no-filter", "at least one of -PassageFilter/-VerseFilter/-SurfaceFilter/"
                                 "-StrongFilter is required — an unbounded full-corpus extract is "
                                 "not this step's job")

    where, args = ["vl.deleted=0"], []
    if passage_f:
        ids = _parse_filter_list(passage_f)
        where.append(f"vl.verse_id IN (SELECT verse_id FROM verse_passage WHERE passage_id IN "
                    f"({','.join('?' * len(ids))}) AND deleted=0)")
        args += ids
    if verse_f:
        # Real bug found live testing this step (escalation #1450, 2026-09-04): a naive
        # `osisId >= ? AND osisId <= ?` range compares STRINGS, not chapter/verse numbers —
        # "John.1.10" sorts lexicographically BEFORE "John.1.5" ('1' < '5' at the first differing
        # character), so a "John.1.1-John.1.5" range silently swept in John.1.10-John.1.19 and
        # more. Fixed: every osisId in scope is parsed to (book, chapter, verse) and compared
        # numerically, matching `versespanmeaningreport.fetch_verses`'s own established
        # convention (`verse` has no chapter/verse COLUMNS to filter on directly — checked live).
        resolved_ids: list[int] = []
        for v in _parse_filter_list(verse_f):
            if "-" in v and v.count(".") >= 2:
                lo_ref, hi_ref = v.split("-", 1)
                lo_book, lo_ch, lo_vs = lo_ref.split(".")
                hi_book, hi_ch, hi_vs = hi_ref.split(".")
                if lo_book != hi_book:
                    return fail("bad-filter", f"VerseFilter range {v!r} spans two books")
                lo_ch, lo_vs, hi_ch, hi_vs = int(lo_ch), int(lo_vs), int(hi_ch), int(hi_vs)
                for r in ctx.db.rows(
                        "SELECT id, osisId FROM verse WHERE osisId LIKE ? AND deleted=0",
                        (f"{lo_book}.%",)):
                    parts = r["osisId"].split(".")
                    if len(parts) != 3 or not parts[1].isdigit() or not parts[2].isdigit():
                        continue
                    ch, vs = int(parts[1]), int(parts[2])
                    if (ch, vs) >= (lo_ch, lo_vs) and (ch, vs) <= (hi_ch, hi_vs):
                        resolved_ids.append(r["id"])
            else:
                row = ctx.db.rows("SELECT id FROM verse WHERE osisId=? AND deleted=0", (v,))
                if row:
                    resolved_ids.append(row[0]["id"])
        if not resolved_ids:
            return fail("bad-filter", f"VerseFilter {verse_f!r} resolved to 0 verses")
        where.append(f"vl.verse_id IN ({','.join('?' * len(resolved_ids))})")
        args += resolved_ids
    if surface_f:
        vals = _parse_filter_list(surface_f)
        where.append(f"vl.surface IN ({','.join('?' * len(vals))})")
        args += vals
    if strong_f:
        vals = _parse_filter_list(strong_f)
        clauses = []
        for s in vals:
            if "-" in s and s[0] in "HG":
                clauses.append("vl.strong BETWEEN ? AND ?")
                lo_s, hi_s = s.split("-", 1)
                args += [lo_s, hi_s]
            else:
                clauses.append("vl.strong = ?")
                args.append(s)
        where.append("(" + " OR ".join(clauses) + ")")

    rows = ctx.db.rows(
        f"SELECT vl.id AS verse_lexical_id, v.osisId AS verse, vl.strong, vl.role, vl.position, "
        f"vl.surface, vl.language, vl.testament, vl.resolved_sense, vl.party_kind "
        f"FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id WHERE {' AND '.join(where)} "
        f"ORDER BY v.osisId, vl.position, vl.code_ordinal", tuple(args))

    ids = [r["verse_lexical_id"] for r in rows]
    notes_by_id: dict[int, list] = {}
    if ids:
        ph = ",".join("?" * len(ids))
        for n in ctx.db.rows(
                f"SELECT verse_lexical_id, note_type, resolution_status, value_text, "
                f"evidence_text FROM verse_lexical_note WHERE verse_lexical_id IN ({ph}) "
                f"AND deleted=0", tuple(ids)):
            notes_by_id.setdefault(n["verse_lexical_id"], []).append(
                {"note_type": n["note_type"], "resolution_status": n["resolution_status"],
                 "value_text": n["value_text"], "evidence_text": n["evidence_text"]})

    # Cluster short name(s), computed here at report time -- NOT a stored verse_lexical column
    # (researcher decision, 2026-09-05: avoids the backfill-cost/staleness problem already named
    # in BUILD.md #230 for is_negator/party_kind -- cluster_strong keeps changing, as today's own
    # T4-T9 build proves, and a stored column would go stale every time it does). Joined on the
    # EXACT strong code, never base-stripped (the strong_related lesson, escalation #1451 review
    # session, 2026-09-05 -- cluster_strong is keyed like strong_related, not like the base-keyed
    # cfg_lexical_code_class convention). A code can belong to more than one cluster at once
    # (confirmed live: H0034 is both M24 and T2) -- all live memberships are returned, comma-joined
    # by short_name, never silently collapsed to one.
    strong_codes = sorted(set(r["strong"] for r in rows if r["strong"]))
    clusters_by_strong: dict[str, list[str]] = {}
    if strong_codes:
        ph = ",".join("?" * len(strong_codes))
        for c in ctx.db.rows(
                f"SELECT cs.strong, cl.short_name FROM cluster_strong cs "
                f"JOIN cluster cl ON cl.cluster_code=cs.cluster_code "
                f"WHERE cs.strong IN ({ph}) AND cs.deleted=0", tuple(strong_codes)):
            clusters_by_strong.setdefault(c["strong"], []).append(c["short_name"])

    out_rows = []
    for r in rows:
        d = dict(r)
        d["notes"] = notes_by_id.get(d["verse_lexical_id"], [])
        d["cluster"] = ", ".join(clusters_by_strong.get(d["strong"], [])) or None
        out_rows.append(d)

    payload = {
        "filters_applied": {"passage": passage_f, "verse": verse_f, "surface": surface_f,
                           "strong": strong_f},
        "rows": out_rows, "row_count": len(out_rows),
    }

    import datetime as _dt
    import json as _json
    output_dir = pathlib.Path(ctx.cfg.required_setting("report.lexical_extract_output_dir"))
    pattern = ctx.cfg.required_setting("report.lexical_extract_output_pattern")
    path = output_dir / pattern.format(run_id=ctx.run_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    return ok(f"wrote {path} ({len(out_rows)} row(s))", path=str(path), row_count=len(out_rows))


def passage_debate_report(ctx: Ctx) -> Outcome:
    """Book-scoped, needs -Book plus exactly one of -Chapters/-Range, same shape as
    `verse_span_meaning_report`. Writes a debate SCAFFOLD, not a finished debate — see
    `lib/passagedebatereport.py`'s module docstring for what is and isn't mechanised. Two
    failure conditions distinct from `report.verse_span_meaning`'s (no STEP dependency here):
    the base extract for this exact range not existing yet, and either `method.*` cfg_setting
    pointing at a file that isn't on disk."""
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    if ctx.params.get("Range"):
        ch, vlo, vhi = versespanmeaningreport.parse_range(ctx.params["Range"])
        lo = hi = ch
        verse_lo, verse_hi = vlo, vhi
    else:
        lo, hi = versespanmeaningreport.parse_chapters(ctx.params["Chapters"])
        verse_lo = verse_hi = None
    try:
        out = passagedebatereport.write_scaffold(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                                 book_label=book_label)
    except passagedebatereport.BaseExtractMissing as e:
        return fail("base-extract-missing", str(e))
    except passagedebatereport.MethodDocMissing as e:
        return fail("guidance-doc-missing", str(e))
    passage_id = passagetrack.record_debate(ctx.cfg, book, lo, hi, verse_lo, verse_hi,
                                            book_label, out)
    return ok(f"wrote {out}", path=str(out), passage_id=passage_id)


def whole_book_read_report(ctx: Ctx) -> Outcome:
    """Book-scoped, needs -Book (BookLabel optional, defaults to -Book — same convention
    `passage_debate_report` uses). Gathers every filled `report.passage_debate` output for the
    book and lays out their Emergent-questions/Passage-level-linkages content together — see
    `lib/wholebookread.py`'s module docstring for what is and isn't mechanised."""
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    try:
        out = wholebookread.write_scaffold(ctx.cfg, book, book_label=book_label)
    except wholebookread.NoDebatesFound as e:
        return fail("no-debates-found", str(e))
    return ok(f"wrote {out}", path=str(out))


def schema_overview_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.required_setting("report.schema_overview_path"))
    out = schemareport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def schema_overview_bible_research_report(ctx: Ctx) -> Outcome:
    """The bible_research.db counterpart -- escalation #1306, 2026-08-31. See
    schemareport.write_report_bible_research's own docstring for the design."""
    path = pathlib.Path(ctx.cfg.required_setting("report.schema_overview_bible_research_path"))
    out = schemareport.write_report_bible_research(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def registry_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.required_setting("report.registry_path"))
    out = registryreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def cluster_report(ctx: Ctx) -> Outcome:
    path = pathlib.Path(ctx.cfg.required_setting("report.cluster_path"))
    out = clusterreport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def obs_catalogue_report(ctx: Ctx) -> Outcome:
    """Structural review of `wa_obs_question_catalogue` (bible_research.db) on its own — no join
    to `finding`/`finding_question_link`. See `lib/cataloguereport.py` module docstring for the
    full design rationale (escalation #1007, second half)."""
    path = pathlib.Path(ctx.cfg.required_setting("report.obs_catalogue_path"))
    out = cataloguereport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def escalation_list(ctx: Ctx) -> Outcome:
    """D4/D16/D23 (register v9) — the escalation-reporting work package's List step, now dispatched
    through run.py like every other report instead of Escalation.ps1 invoking
    `python -m iba.app.lib.escalation list` directly. Content unchanged — esc.write_list_report
    already writes the full open-items report, now including the D15 exception sections."""
    path = pathlib.Path(ctx.cfg.required_setting("escalation.list_report_path"))
    out, rows = esc.write_list_report(ctx.cfg, ctx.db, path)
    return ok(f"{len(rows)} open escalation(s) -> {out}", path=str(out), open_count=len(rows))


def escalation_history(ctx: Ctx) -> Outcome:
    """D4/D16/D23 — the escalation-reporting work package's History step. Needs -Id."""
    eid = ctx.params.get("Id")
    if not eid:
        return fail("missing-id", "escalation.history requires a -Id parameter")
    # id-prefixed stem, 2026-08-26 (escalation #857, researcher direct instruction) -- was
    # escalation-{eid}-history.md (id buried mid-name); versioning is now write_report()'s job
    # (BUILD.md sec60), not this path's -- write_history_report returns the actual written path.
    path = pathlib.Path(ctx.cfg.required_setting("escalation.history_report_dir")) / f"{eid}-escalation-history.md"
    out = esc.write_history_report(ctx.cfg, ctx.db, int(eid), path)
    return ok(f"wrote {out}", path=str(out))
