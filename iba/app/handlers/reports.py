"""reports handlers — thin dispatcher adapters over report.py / validation.py and the report
modules, in the standard `def h(ctx) -> Outcome` contract. Read-only, except
`verse_span_meaning_report`, which may write to the raw/lexicon-parsed layer via
`raw.backfill_meaning_for` before rendering (gated by `report.auto_backfill_before_render`).
"""

from __future__ import annotations

import pathlib

from .base import Ctx, Outcome, ok, fail, escalate
from . import raw as raw_mod
from .. import report as report_mod
from .. import validation as validation_mod
from ..lib import contentindex as contentindex_mod
from ..lib import behaviour as behaviour_mod
from ..lib import escalation as esc
from ..lib import manifest as manifest_mod
from ..lib import retention as retention_mod
from ..lib import (cataloguereport, clusterreport, registryreport, schemareport, seedreport,
                   spanreport, strongreport, strongversereport)
from ..lib import (lexical, passagedebatereport, passagetrack, reportkit, versespanmeaningreport,
                   wholebookread)
from ..lib.stepapi import StepUnavailable
from ..tools import export_tables_csv


def word_report(ctx: Ctx) -> Outcome:
    out = report_mod.generate(ctx.params["Word"], cfg=ctx.cfg)
    if out is None:
        return fail("word-not-found", f"{ctx.params['Word']!r} is not in the DB")
    return ok(f"wrote {out}", path=str(out))


# validation_word/validation_book: clean is ok(); a FAIL/WARN escalates once per run, like every
# other quality check.
def _validation_outcome(ctx: Ctx, scope_label: str, out, overall: str, p: int, w: int, f: int
                        ) -> Outcome:
    if overall == "PASS":
        return ok(f"{overall} ({p} pass, {w} warn, {f} fail) -> {out}",
                 path=str(out), overall=overall, passes=p, warns=w, fails=f)

    answered = esc.answered_for_run(ctx.db, ctx.run_id, ctx.step_id)
    if answered:
        decision = answered["next_action"]
        # decision_required resolves via Update's vocabulary (approved)
        if decision in ("approve", "approved"):
            return ok(f"acknowledged: {overall} ({p} pass, {w} warn, {f} fail) -> {out} — "
                      f"researcher confirmed these findings are known/acceptable",
                      path=str(out), overall=overall, passes=p, warns=w, fails=f)
        if decision == "reject":
            return fail("findings-rejected",
                       f"researcher flagged {scope_label}'s validation findings as needing action",
                       path=str(out), overall=overall, passes=p, warns=w, fails=f)
        return fail("needs-revision", f"researcher comment: {answered['comment'] or '(none)'}")

    # raised as decision_required for every finding (no per-check classification)
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
    """Rescan the whole project tree — filename/path metadata only — and update file_manifest by path (added, updated, removed);
    the analytic columns of a file that is still there are kept. See lib/manifest.py."""
    summary = manifest_mod.rebuild(ctx.cfg)
    path = pathlib.Path(ctx.cfg.required_setting("manifest.report_path"))
    out = manifest_mod.write_rebuild_report(ctx.cfg, path, summary)
    return ok(f"wrote {out} ({summary['total']} files: {summary['active']} active, "
             f"{summary['archived']} archived; {summary['added']} added, {summary['removed']} removed)", path=str(out),
             total=summary["total"], active=summary["active"], archived=summary["archived"],
             added=summary["added"], removed=summary["removed"])


def manifest_search(ctx: Ctx) -> Outcome:
    """Field:value or free-text search against file_manifest. -Query is a per-call parameter, not
    config."""
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
    """Incremental refresh then a key_type:value (strong:H2734, gloss:anger, word:anger) or bare-value
    lookup against content_index. -Query is a per-call parameter. -Csv (any non-empty value) also
    writes the full result set as .csv (the .md report caps at 500 rows)."""
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


def behaviour_list(ctx: Ctx) -> Outcome:
    """behaviour.list: every active behaviour rule, optionally one -Class, to
    behaviour.list_report_path."""
    path = pathlib.Path(ctx.cfg.required_setting("behaviour.list_report_path"))
    out, total = behaviour_mod.write_list_report(ctx.cfg, ctx.db, path, ctx.params.get("Class") or None)
    return ok(f"{total} active behaviour rule(s) -> {out}", path=str(out))


def table_export(ctx: Ctx) -> Outcome:
    """CSV dump of every DATA table, verbatim; cfg_* content belongs to configmaint.report and is
    excluded. -Out/-Table/-Database are plain per-call overrides; -Database resolves through
    `ctx.cfg.database_path` (the project_database enum). `table_export.output_dir` is a per-database
    map; a database missing from it is a config gap and raises."""
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


def strong_verse_report(ctx: Ctx) -> Outcome:
    """`ctx.word_id` is resolved by the dispatcher (run.py, for any step with 'Word' in params)."""
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
    """Book-scoped, needs -Book plus exactly one of -Chapters/-Range. STEP-dependent (live
    disambiguation of AMBIGUOUS spans): versespanmeaningreport.write_report() raises StepUnavailable
    when STEP is required and down, caught here into a clean fail() (cfg_on_fail
    report.verse_span_meaning / unreachable).

    `report.auto_backfill_before_render` (default True): before rendering, run the same pull as
    `Raw-Backfill.ps1` (raw.backfill_meaning_for) for any span in this book+range whose strong is not
    registered. False makes it a pure read-only render. It does not change whether STEP is required."""
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
    """Book-scoped, needs -Book plus exactly one of -Chapters/-Range. Pure render off
    `verse_lexical` (populated by `lexical.build`): no STEP, no backfill, no DB write. `no-readings`
    when nothing is built for this range (message from cfg_on_fail)."""
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
    """The self-audit / exception report of the lexical work over this verse range (#1383, re-founded on the lexical
    observations, #2507). Read-only against `verse_lexical` and the observations of stage `lexical`. A plain tally against Layer
    1's complete enumeration, no "confirms"/"validates" framing. Verse-scoped (#1451): verses resolve
    via `fetch_verses` and queries filter by `verse_id`; no `passage` row is needed."""
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

    obs_rows = ctx.db.rows(
        f"SELECT o.id, o.tag, o.status, o.basis, o.obs_text FROM ib_observation o WHERE o.stage='lexical' AND o.deleted=0 AND EXISTS ("
        f"SELECT 1 FROM ib_node n JOIN verse_lexical vl ON vl.id=n.verse_lexical_id WHERE n.observation_id=o.id AND n.deleted=0 AND vl.verse_id IN ({ph}))", tuple(verse_ids))
    by_status: dict[str, list] = {}
    for r in obs_rows:
        by_status.setdefault(f"{r['tag']} ({r['status']})", []).append(r)
    # standing integrity check: a live node of a lexical observation on a soft-deleted verse_lexical row, or with no collection or no role, is a genuine fault (B:130)
    orphaned_anchor = ctx.db.rows(
        f"SELECT n.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id JOIN verse_lexical vl ON vl.id=n.verse_lexical_id "
        f"WHERE o.stage='lexical' AND o.deleted=0 AND n.deleted=0 AND vl.verse_id IN ({ph}) AND vl.deleted=1", tuple(verse_ids))
    orphaned_target = ctx.db.rows(
        f"SELECT n.id FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id JOIN verse_lexical vl ON vl.id=n.verse_lexical_id "
        f"WHERE o.stage='lexical' AND o.deleted=0 AND n.deleted=0 AND vl.verse_id IN ({ph}) AND (n.role IS NULL OR n.collection_id IS NULL)", tuple(verse_ids))

    layer1 = [
        f"- codes processed: {len(vl_rows)}",
        f"- negators found: {n_negators}",
        f"- narrative_morph fired: {n_narrative}",
        f"- gloss_consistent_in_verse=0 (data-quality): {n_gloss_bad}",
    ]
    layer2 = [f"- {status}: {len(items)}" for status, items in sorted(by_status.items())]
    if not layer2:
        layer2 = ["- (no lexical observation with a node in these verses yet: Collection-Build.ps1 -Action LayerOpen -Step S1)"]
    judgement = [f"- {r['tag']} (observation {r['id']}): {(r['obs_text'] or '')[:200]}" for r in obs_rows if r["basis"] == "read"]
    if not judgement:
        judgement = ["- (none recorded)"]

    n_orphaned = len(orphaned_anchor) + len(orphaned_target)
    if n_orphaned:
        integrity = [f"- **{n_orphaned} fault(s) in the nodes of the lexical observations -- action needed**:",
                    f"  - {len(orphaned_anchor)} node(s) on a deleted verse_lexical row",
                    f"  - {len(orphaned_target)} node(s) with no role or no collection"]
    else:
        integrity = ["- 0 faults (every live node of a lexical observation is on a live verse_lexical row, with a role and a collection)"]

    sections = {"layer1_tally": layer1, "layer2_dispositions": layer2, "judgement_calls": judgement,
               "integrity": integrity}
    intro = [f"> Generated by `report.lexical_exceptions` for {book} {ctx.params.get('Range') or ctx.params.get('Chapters')} "
            f"({len(verse_ids)} verse(s)). Read-only against verse_lexical and the lexical observations (stage lexical, #2507; the retired verse_lexical_note is not read). "
            f"No `passage` row involved — verse-scoped (escalation #1451)."]
    L = reportkit.render_scaffold(ctx.db.conn, "report.lexical_exceptions", sections, intro=intro,
                                  book=book, range=(ctx.params.get("Range") or ctx.params.get("Chapters")))
    output_dir = pathlib.Path(ctx.cfg.required_setting("report.verse_analysis_output_dir"))
    range_str = versespanmeaningreport._range_str(lo, hi, verse_lo, verse_hi)
    path = output_dir / (book_label or book) / f"{book.lower()}-{range_str}-lexical-exceptions.md"
    path = reportkit.write_report(ctx.db.conn, "report.lexical_exceptions", path, L)
    return ok(f"wrote {path}", path=str(path), codes=len(vl_rows), observations=len(obs_rows),
             dangling_references=n_orphaned)


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
    """The bible_research.db counterpart (#1306); see schemareport.write_report_bible_research."""
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
    """Structural review of `wa_obs_question_catalogue` (bible_research.db) on its own; see
    `lib/cataloguereport.py`."""
    path = pathlib.Path(ctx.cfg.required_setting("report.obs_catalogue_path"))
    out = cataloguereport.write_report(ctx.cfg, path)
    return ok(f"wrote {out}", path=str(out))


def escalation_list(ctx: Ctx) -> Outcome:
    """The escalation-reporting List step (dispatched through run.py): esc.write_list_report."""
    path = pathlib.Path(ctx.cfg.required_setting("escalation.list_report_path"))
    out, rows = esc.write_list_report(ctx.cfg, ctx.db, path)
    n_open = sum(1 for r in rows if r["state"] in esc.state_group(ctx.db, "open"))   # #2173 G1
    return ok(f"{n_open} open, {len(rows) - n_open} parked escalation(s) -> {out}", path=str(out),
              open_count=n_open, parked_count=len(rows) - n_open)


def escalation_history(ctx: Ctx) -> Outcome:
    """The escalation-reporting History step. Needs -Id."""
    eid = ctx.params.get("Id")
    if not eid:
        return fail("missing-id", "escalation.history requires a -Id parameter")
    try:
        eid = esc.resolve_id(ctx.db, eid)      # -Id also takes a thread alias
    except ValueError as exc:
        return fail("bad-parameter", str(exc))
    # id-prefixed stem; write_report() versions it and returns the path written
    path = pathlib.Path(ctx.cfg.required_setting("escalation.history_report_dir")) / f"{eid}-escalation-history.md"
    try:
        out = esc.write_history_report(ctx.cfg, ctx.db, int(eid), path)
    except ValueError as exc:       # an id with no escalation row (#2240), a usage slip, not a crash
        return fail("bad-parameter", str(exc))
    return ok(f"wrote {out}", path=str(out))


def escalation_thread(ctx: Ctx) -> Outcome:
    """The Thread step (`Escalation.ps1 -Action Thread`, #2000): the open threads, or one thread in
    full with -Id OT-nn. Optional -State (on-hold|in-progress) narrows the list. The console message
    carries the short list."""
    path = pathlib.Path(ctx.cfg.required_setting("escalation.thread_report_path"))
    try:
        out, lines = esc.write_thread_report(ctx.cfg, ctx.db, path,
                                             state=ctx.params.get("State"),
                                             ident=ctx.params.get("Id"))
    except ValueError as exc:       # a usage slip (unknown alias, wrong -State), not a crash
        return fail("bad-parameter", str(exc))
    return ok("\n  ".join([f"-> {out}"] + lines), path=str(out), lines=len(lines))


def escalation_thread_export(ctx: Ctx) -> Outcome:
    """The Export step (`Escalation.ps1 -Action Export -Type thread`, #2000): regenerates the open
    threads register .md from the escalation table. Run at session-close."""
    path = pathlib.Path(ctx.cfg.required_setting("escalation.thread_register_path"))
    out, n = esc.write_thread_register(ctx.cfg, ctx.db, path)
    return ok(f"{n} thread(s) -> {out}", path=str(out), threads=n)


def escalation_context(ctx: Ctx) -> Outcome:
    """`Escalation.ps1 -Action Context [-Id n]` (#2173; #2209): every file each open escalation names
    (any field, any version), resolved to its latest live version; with -Id, one escalation, read
    when it is taken up. Read-only."""
    from ..lib import escalationcontext
    path = pathlib.Path(ctx.cfg.required_setting("escalation.context_report_path"))
    eid = ctx.params.get("Id")
    out, items = escalationcontext.write_report(ctx.cfg, ctx.db, path,
                                                int(eid) if eid not in (None, "") else None)
    n_find = sum(len(i["findings"]) for i in items)
    lines = [f"{len(items)} open escalation(s), {sum(len(i['refs']) for i in items)} file "
             f"reference(s), {n_find} finding(s) -> {out}"]
    for i in items:
        for f in i["findings"]:
            lines.append(f"  #{i['escalation']['id']}: {f['status']} `{f['named']}` -- {f['note']}")
    return ok("\n".join(lines), path=str(out), findings=n_find)


def escalation_thread_audit(ctx: Ctx) -> Outcome:
    """`Escalation.ps1 -Action ThreadAudit` (#2173): thread quality, validity and integrity findings
    (T-a .. T-g), by thread item. Read-only."""
    from ..lib import threadaudit
    path = pathlib.Path(ctx.cfg.required_setting("escalation.thread_audit_report_path"))
    out, F = threadaudit.write_report(ctx.cfg, ctx.db, path)
    by: dict[str, int] = {}
    for f in F:
        by[f["check"]] = by.get(f["check"], 0) + 1
    summary = ", ".join(f"{k} {v}" for k, v in sorted(by.items())) or "none"
    return ok(f"{len(F)} thread finding(s) ({summary}) -> {out}", path=str(out), findings=len(F))
