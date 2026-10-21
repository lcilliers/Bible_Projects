"""lexical.py — dispatcher handler for the lexical steps.

  lexical.run (the front door): resolves a selector (`-ClusterCode`/`-Word`/`-StrongList`/
    `-VerseList`, via `lib/lexicalscope.py`) to a verse-id list once; `-Mode` picks the work
    (`Layer1AndLayer2`/`Layer1Only`/`Layer2Only`). Layer 2 always uses the ids Layer 1 resolved.
    Any mode involving Layer 2 first writes the notes briefing pack (`_notes_payload_dict`),
    unless `-SuppressNotes`. `run` calls `build_for_verse_ids` directly, without auto-backfill.
  lexical.build / lexical.enrich: the -Book + range adapters over `lib/lexical.py` /
    `lib/lexicalenrich.py` (payload loading, verse resolution, write-grant checks here; the
    reconciliation and writes in those modules). Verse-scoped: no `passage` row is resolved or
    required (#1451). Auto-backfill as in report.verse_span_meaning
    (`report.auto_backfill_before_render`, `raw.backfill_meaning_for`).
  lexical.readiness: the 3-leg base-data readiness check (#1606).
  lexical.meaning / lexical.relational: the verse-reading stage against ib_observation/ib_node
    (word-level, then relational; #1706, #1860).
"""

from __future__ import annotations

import csv
import datetime
import json
import pathlib
import sys

from .base import Ctx, Outcome, fail, ok
from . import raw as raw_mod
from ..lib import lexical, lexicalenrich, lexicalenrichgenerate, lexicalscope, reportkit
from ..lib import batchcontrol, clusterstatus, recordingpass, stage1coverage, versereadinggenerate
from ..lib.stepapi import Step, StepUnavailable
from ..lib.versespanmeaningreport import fetch_verses, parse_chapters, parse_range


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

    try:
        totals = lexical.build_for_range(ctx.db.conn, book, lo, hi, verse_lo, verse_hi)
    except lexical.NotReady as e:
        return fail("lexical-not-ready", str(e), unready_codes=e.codes)
    ctx.db.conn.commit()

    removed_note = (f", {totals['removed_with_live_notes']} with live notes now dangling — "
                    f"see report.lexical_exceptions" if totals["removed_with_live_notes"] else "")
    return ok(
        f"{book} {lo}-{hi}: {totals['verses']} verse(s), {totals['spans']} span(s), "
        f"{totals['codes']} code(s) resolved ({totals['inserted']} inserted, "
        f"{totals['updated']} updated, {totals['unchanged']} unchanged, "
        f"{totals['removed']} removed{removed_note}){backfill_note}",
        **totals)


# ── lexical.readiness — the 3-leg base-data readiness check (#1606) ────────────────────────────
# Read-only, always persists a report (governance.reports_must_persist), escalates only on a FATAL
# finding. Separate from spine.check: it also checks the cluster-allocation precondition Layer 1's
# `role` column depends on.
#
# Leg 1 -- every live verse has >=1 live span.
# Leg 2 -- every live span's strong_variant code resolves to a live `strong` row.
# Leg 3 -- every live `strong` that occurs in a live span has >=1 live `cluster_strong` allocation
#          (Layer 1's `role` is the JSON array of its cluster codes; an empty one is a hard failure
#          in lib/lexical.py `_check_role_readiness`).

def readiness(ctx: Ctx) -> Outcome:
    conn = ctx.db.conn

    leg1_count = conn.execute(
        "SELECT COUNT(*) FROM verse v WHERE v.deleted=0 AND NOT EXISTS ("
        "SELECT 1 FROM span s WHERE s.verse_id=v.id AND s.deleted=0)").fetchone()[0]
    leg1_sample = [r[0] for r in conn.execute(
        "SELECT v.osisId FROM verse v WHERE v.deleted=0 AND NOT EXISTS ("
        "SELECT 1 FROM span s WHERE s.verse_id=v.id AND s.deleted=0) LIMIT 15").fetchall()]

    span_codes: set[str] = set()
    for r in conn.execute(
            "SELECT strong_variant FROM span WHERE deleted=0 AND strong_variant IS NOT NULL "
            "AND strong_variant != ''"):
        span_codes.update(r[0].split())
    live_strong = {r[0] for r in conn.execute("SELECT strongNumber FROM strong WHERE deleted=0")}
    leg2_missing = sorted(span_codes - live_strong)

    allocated = {r[0] for r in conn.execute(
        "SELECT DISTINCT strong FROM cluster_strong WHERE deleted=0")}
    # cluster_strong.strong carries the exact suffixed code: compare exact codes, never the base
    occurring_live_strong = span_codes & live_strong
    leg3_missing = sorted(occurring_live_strong - allocated)

    findings = dict(leg1_count=leg1_count, leg1_sample=leg1_sample,
                     leg2_count=len(leg2_missing), leg2_sample=leg2_missing[:15],
                     leg3_count=len(leg3_missing), leg3_sample=leg3_missing[:15])
    report_path = _write_readiness_report(ctx, findings)
    fatal_count = findings["leg1_count"] + findings["leg2_count"] + findings["leg3_count"]

    if not fatal_count:
        return ok(f"lexical readiness sound: 0 FATAL findings across all 3 legs — report written "
                  f"to {report_path}", **findings)

    return fail("lexical-not-ready",
               f"{fatal_count} FATAL finding(s) — Leg1 (verse with no span): "
               f"{findings['leg1_count']}, Leg2 (span code with no strong row): "
               f"{findings['leg2_count']}, Leg3 (occurring strong with no cluster_strong "
               f"allocation): {findings['leg3_count']}. Full detail: {report_path}",
               **findings)


def _write_readiness_report(ctx: Ctx, findings: dict) -> pathlib.Path:
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    path = pathlib.Path(ctx.cfg.required_setting("lexical.readiness_report_path"))
    total = findings["leg1_count"] + findings["leg2_count"] + findings["leg3_count"]
    intro = [
        f"> Generated {now} by `lexical.readiness` (#1606, registered as a persisted check "
        f"2026-09-16, escalation #1706 Phase A). Precondition check for the Layer 1 rebuild -- "
        f"**{total} FATAL finding(s)** across all 3 legs.",
    ]
    sections = {
        "summary": [
            f"Leg 1 (verse with 0 live spans): **{findings['leg1_count']}**",
            f"Leg 2 (span strong_variant code with no live `strong` row): **{findings['leg2_count']}**",
            f"Leg 3 (occurring `strong` with no live `cluster_strong` allocation): "
            f"**{findings['leg3_count']}**",
        ],
        "detail": [
            f"**Leg 1 sample:** {findings['leg1_sample']}",
            f"**Leg 2 sample:** {findings['leg2_sample']}",
            f"**Leg 3 sample:** {findings['leg3_sample']}",
        ],
    }
    L = reportkit.render_scaffold(ctx.db.conn, "lexical.readiness", sections, intro=intro)
    return reportkit.write_report(ctx.db.conn, "lexical.readiness", path, L)


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

    # verse-scoped (#1451): verses resolve directly from -Book/-Range/-Chapters, no passage row
    fetched = fetch_verses(ctx.db.conn, book, lo, hi, verse_lo, verse_hi)
    if not fetched:
        return fail("no-verses", f"{book} this range has no live verse rows")
    verse_ids = [v["id"] for v in fetched]
    verse_id_by_osis = {f"{book}.{v['chapter']}.{v['verse']}": v["id"] for v in fetched}
    passage_id = None

    max_verses = int(ctx.cfg.required_module_setting("cfg_passage", "passage.max_verses"))
    if len(verse_ids) > max_verses:
        return fail("too-many-verses",
                   f"{len(verse_ids)} verses exceeds the {max_verses}-verse cap — split into "
                   f"smaller passage-blocks")

    _may(ctx, "lexical.enrich", "verse_lexical_note")

    # the completeness check runs before commit: an incomplete block rolls back, never a partial
    # write (#1450)
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

    complete, missing = lexicalenrich.check_completeness(ctx.db.conn, verse_ids)
    if not complete:
        ctx.db.conn.rollback()
        return fail("incomplete-block",
                   f"{len(missing)} code(s) in this block have no disposition: "
                   f"{missing[:5]}{' ...' if len(missing) > 5 else ''} — every applicable code "
                   f"needs a finding or an explicit checked_empty/unresolved")

    # per-verse completeness is checked above but not recorded anywhere (no passage row to hold it)
    ctx.db.conn.commit()

    genre_note = " (genre supplied but not persisted -- no per-verse home designed yet)" \
        if counts.get("genre_dropped") else ""
    return ok(f"{book} {lo}-{hi}: {counts['unchanged']} unchanged, {counts['new']} new, "
             f"{counts['changed']} corrected, {counts['removed']} removed note(s); "
             f"block complete{genre_note}", **counts)


# ── lexical.notes briefing pack — produced by lexical.run's Layer 2 path ─────────────────────────
# Built off a verse_id list (a cluster/strong scope is cross-book); `-SuppressNotes` opts out.

def _notes_payload_dict(ctx: Ctx, verse_ids: list[int]) -> dict:
    """Never a DB write: the briefing pack a reading pass needs before deciding what a Layer 2
    payload should say. Every live `verse_lexical` column per code, the verse's base text, any live
    `verse_lexical_note` rows (so a re-run sees what it must re-address), cluster tags, and the full
    `cfg_method_rule`/`cfg_enum` catalogue."""
    # this verse_lexical_note-based Layer 2 path is superseded by ib_observation (#1706); the SQL
    # only avoids columns dropped from verse_lexical
    ph = ",".join("?" * len(verse_ids))
    code_rows = ctx.db.rows(
        f"SELECT vl.id AS verse_lexical_id, v.osisId AS verse, vl.position, vl.code_ordinal, "
        f"vl.strong, vl.role, vl.status, vl.morph_code, "
        f"vl.surface, vl.testament, vl.is_negator, vl.narrative_morph, "
        f"vl.gloss_consistent_in_verse, vl.party_kind "
        f"FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id "
        f"WHERE vl.verse_id IN ({ph}) AND vl.deleted=0 "
        f"ORDER BY v.osisId, vl.position, vl.code_ordinal", tuple(verse_ids))

    vlids = [r["verse_lexical_id"] for r in code_rows]
    notes_by_vlid: dict[int, list] = {}
    if vlids:
        ph2 = ",".join("?" * len(vlids))
        for n in ctx.db.rows(
                f"SELECT verse_lexical_id, note_type, resolution_status, target_verse_lexical_id, "
                f"related_verse_lexical_ids, value_text, evidence_text FROM verse_lexical_note "
                f"WHERE verse_lexical_id IN ({ph2}) AND deleted=0", tuple(vlids)):
            notes_by_vlid.setdefault(n["verse_lexical_id"], []).append(dict(n))

    # cluster tags: computed at request time on the exact strong code, every live membership
    strong_codes = sorted({r["strong"] for r in code_rows if r["strong"]})
    clusters_by_strong: dict[str, list[str]] = {}
    if strong_codes:
        ph3 = ",".join("?" * len(strong_codes))
        for c in ctx.db.rows(
                f"SELECT cs.strong, cl.short_name FROM cluster_strong cs "
                f"JOIN cluster cl ON cl.cluster_code=cs.cluster_code "
                f"WHERE cs.strong IN ({ph3}) AND cs.deleted=0", tuple(strong_codes)):
            clusters_by_strong.setdefault(c["strong"], []).append(c["short_name"])

    codes = []
    for r in code_rows:
        d = dict(r)
        vlid = d.pop("verse_lexical_id")
        d["existing_notes"] = notes_by_vlid.get(vlid, [])
        d["cluster"] = ", ".join(clusters_by_strong.get(d["strong"], [])) or None
        codes.append(d)

    method_rules = [
        {"step": r["step"], "rule_key": r["rule_key"], "rule_text": r["rule_text"],
         "source_doc": r["source_doc"]}
        for r in ctx.db.rows(
            "SELECT step, rule_key, rule_text, source_doc FROM cfg_method_rule "
            "WHERE step IN ('lexical.build','lexical.enrich') AND active=1 "
            "ORDER BY step, ordinal")]
    note_type_values = [r["value"] for r in ctx.db.rows(
        "SELECT value FROM cfg_enum WHERE name='note_type' AND inactive=0 ORDER BY ordinal")]
    resolution_status_values = [r["value"] for r in ctx.db.rows(
        "SELECT value FROM cfg_enum WHERE name='resolution_status' AND inactive=0 "
        "ORDER BY ordinal")]

    verse_rows = ctx.db.rows(
        f"SELECT osisId, text FROM verse WHERE id IN ({ph}) AND deleted=0", tuple(verse_ids))

    # verse.text is NULL for some verses (onboarded without text): reconstructed from the resolved
    # codes' own surface words in position order, and labelled as reconstructed
    surfaces_by_verse: dict[str, list[tuple[int, str]]] = {}
    for c in codes:
        if c["surface"]:
            surfaces_by_verse.setdefault(c["verse"], []).append((c["position"] or 0, c["surface"]))
    verses_out = []
    for r in verse_rows:
        if r["text"] is not None:
            verses_out.append({"verse": r["osisId"], "text": r["text"]})
        else:
            words = [s for _, s in sorted(surfaces_by_verse.get(r["osisId"], []))]
            verses_out.append({
                "verse": r["osisId"], "text": None,
                "text_reconstructed_from_codes": " ".join(words) if words else None})

    return {
        "verses": verses_out,
        "codes": codes,
        "note_type_values": note_type_values,
        "resolution_status_values": resolution_status_values,
        "method_rules": method_rules,
    }


def _write_notes_payload(ctx: Ctx, verse_ids: list[int]) -> tuple[pathlib.Path, dict]:
    payload = _notes_payload_dict(ctx, verse_ids)
    output_dir = pathlib.Path(ctx.cfg.required_setting("report.lexical_extract_output_dir"))
    pattern = ctx.cfg.required_setting("report.lexical_notes_output_pattern")
    path = output_dir / pattern.format(run_id=ctx.run_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path, payload


# ── lexical.run — the front door ──────────────────────────────────────────────────────────────
# The input is a cross-book verse list from a cluster or group of strongs: ClusterCode/Word ->
# strong-list (lexicalscope.resolve_strongs) -> verse-list (lexicalscope.
# resolve_verse_ids_for_strongs, via span.strong_variant). VerseList takes a known verse set.
#
# One entry point; `-Mode` picks the work and verse-list resolution happens once. Layer 1's write
# (`build_for_verse_ids`) is identity-stable, so rebuilding unchanged verses is a no-op that never
# orphans a Layer 2 note. Layer2Only skips the write and fails fast (`no-layer1`) naming any verse
# without Layer 1.
#
# Cap: `lexical.run_max_verses`, enforced once against the resolved verse list before any work.

_MODES = ("Layer1AndLayer2", "Layer1Only", "Layer2Only")


def run(ctx: Ctx) -> Outcome:
    selectors = {
        "ClusterCode": ctx.params.get("ClusterCode"),
        "StrongList": ctx.params.get("StrongList"),
        "Word": ctx.params.get("Word"),
        "VerseList": ctx.params.get("VerseList"),
    }
    given = [k for k, v in selectors.items() if v]
    if len(given) != 1:
        return fail("bad-selector", f"exactly one of -ClusterCode/-StrongList/-Word/-VerseList "
                                    f"is required, got {given or 'none'}")
    mode = ctx.params.get("Mode")
    if mode not in _MODES:
        return fail("bad-mode", f"-Mode must be one of {_MODES}, got {mode!r}")

    conn = ctx.db.conn
    zero_occurrence: list[str] = []
    try:
        if given[0] == "VerseList":
            refs = [x.strip() for x in selectors["VerseList"].split(",") if x.strip()]
            verse_ids = lexicalscope.resolve_verse_ids_for_refs(conn, refs)
        else:
            strong_list = ([x.strip() for x in selectors["StrongList"].split(",") if x.strip()]
                          if given[0] == "StrongList" else None)
            strongs = lexicalscope.resolve_strongs(
                conn,
                cluster_code=selectors["ClusterCode"],
                strong_list=strong_list,
                word=selectors["Word"])
            verse_ids = lexicalscope.resolve_verse_ids_for_strongs(conn, strongs)
            # -StrongList is validated against span presence in resolve_strongs; -ClusterCode/-Word are
            # not (a cluster can carry a stale code, lexicalscope.strongs_with_no_occurrence), so such codes
            # are reported as a named warning, never dropped silently
            if given[0] in ("ClusterCode", "Word"):
                zero_occurrence = lexicalscope.strongs_with_no_occurrence(conn, strongs)
    except ValueError as e:
        return fail("bad-selector", str(e))
    if not verse_ids:
        return fail("no-verses", f"{given[0]} resolved to 0 verses")

    cap = int(ctx.cfg.required_setting("lexical.run_max_verses"))
    if len(verse_ids) > cap:
        return fail("too-many-verses",
                   f"{given[0]} resolved to {len(verse_ids)} verses, exceeds the {cap}-verse cap "
                   f"(lexical.run_max_verses) -- narrow the selector or raise the cap")

    verse_id_by_osis = lexicalscope.verse_id_by_osis_for(conn, verse_ids)
    build_totals: dict | None = None

    if mode in ("Layer1AndLayer2", "Layer1Only"):
        _may(ctx, "lexical.run", "verse_lexical")
        # Layer 1 has no STEP dependency (#1706)
        try:
            build_totals = lexical.build_for_verse_ids(conn, verse_ids)
        except lexical.NotReady as e:
            return fail("lexical-not-ready", str(e), unready_codes=e.codes)
        conn.commit()
    else:   # Layer2Only -- Layer 1 must already exist, never rebuilt here
        ph = ",".join("?" * len(verse_ids))
        has = {r["verse_id"] for r in ctx.db.rows(
            f"SELECT DISTINCT verse_id FROM verse_lexical WHERE verse_id IN ({ph}) AND deleted=0",
            tuple(verse_ids))}
        missing_ids = [vid for vid in verse_ids if vid not in has]
        if missing_ids:
            missing_osis = [r["osisId"] for r in ctx.db.rows(
                f"SELECT osisId FROM verse WHERE id IN "
                f"({','.join('?' * len(missing_ids))})", tuple(missing_ids))]
            return fail("no-layer1", f"{len(missing_ids)} verse(s) have no verse_lexical rows -- "
                                     f"Layer2Only requires Layer 1 already present: "
                                     f"{missing_osis[:5]}{' ...' if len(missing_osis) > 5 else ''}")

    enrich_counts: dict | None = None
    notes_path: pathlib.Path | None = None
    llm_summary: list[dict] = []
    if mode in ("Layer1AndLayer2", "Layer2Only"):
        _may(ctx, "lexical.run", "verse_lexical_note")

        # the briefing pack, produced before any write (it is Layer 2's prompt data); -SuppressNotes opts out
        if not ctx.params.get("SuppressNotes"):
            notes_path, _ = _write_notes_payload(ctx, verse_ids)

        raw_payload = ctx.params.get("PayloadPath")
        if raw_payload:
            # manual path: a payload already decided by a reading pass
            path = pathlib.Path(raw_payload)
            if not path.exists():
                return fail("bad-payload", f"PayloadPath {path} does not exist")
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                return fail("bad-payload", f"PayloadPath {path} is not valid JSON: {e}")
            notes = payload.get("notes", [])
            removals = payload.get("remove", [])
            genre = payload.get("genre")
            if not notes and not removals:
                return fail("empty-payload", "payload has no 'notes' or 'remove' entries")

            max_verses = int(ctx.cfg.required_module_setting("cfg_passage", "passage.max_verses"))
            if len(verse_ids) > max_verses:
                return fail("too-many-verses-for-enrich",
                           f"{len(verse_ids)} verses exceeds enrich's own {max_verses}-verse block "
                           f"cap (passage.max_verses) -- separate from lexical.run_max_verses; the "
                           f"resolved scope is bigger than one Layer 2 pass can take")

            try:
                enrich_counts = lexicalenrich.enrich_passage(
                    conn, None, verse_ids, verse_id_by_osis, genre, notes, removals)
            except lexicalenrich.UnresolvedReference as e:
                conn.rollback()
                return fail("unresolved-reference",
                           f"{len(e.problems)} problem(s): "
                           f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")
            except lexicalenrich.ReconciliationError as e:
                conn.rollback()
                return fail("unreconciled",
                           f"{len(e.problems)} item(s) need reconciliation: "
                           f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

            complete, missing = lexicalenrich.check_completeness(conn, verse_ids)
            if not complete:
                conn.rollback()
                return fail("incomplete-block",
                           f"{len(missing)} code(s) have no disposition: "
                           f"{missing[:5]}{' ...' if len(missing) > 5 else ''}")
            conn.commit()

        elif ctx.params.get("NoAutoLLM"):
            # explicit opt-out: notes briefing only, nothing written
            if notes_path is None:
                return fail("bad-payload", "-PayloadPath is required to write Layer 2 when both "
                                           "-NoAutoLLM and -SuppressNotes are given -- nothing to do")

        else:
            # default: LLM Layer 2, batched by passage.max_verses. Each chunk: assemble -> cost estimate ->
            # hard cap check (the configured cap is the approval) -> live call -> parse -> write via the same
            # enrich_passage/check_completeness path as a manual payload -> log real usage. One chunk's
            # failure stops the run (report-stop).
            max_verses = int(ctx.cfg.required_module_setting("cfg_passage", "passage.max_verses"))
            max_cost_per_batch = float(ctx.cfg.setting("lexical.llm_max_cost_per_batch", 1.00))
            chunks = [verse_ids[i:i + max_verses] for i in range(0, len(verse_ids), max_verses)]
            agg = {"unchanged": 0, "new": 0, "changed": 0, "removed": 0}
            for idx, chunk in enumerate(chunks):
                chunk_label = f"{idx + 1}/{len(chunks)}"
                chunk_vd_by_osis = lexicalscope.verse_id_by_osis_for(conn, chunk)
                package = lexicalenrichgenerate.assemble_batch_package(ctx, chunk)
                if package["est_cost_usd"] > max_cost_per_batch:
                    conn.rollback()
                    return fail("cost-cap-exceeded",
                               f"chunk {chunk_label} ({len(chunk)} verses) estimated cost "
                               f"${package['est_cost_usd']:.2f} exceeds lexical.llm_max_cost_per_"
                               f"batch (${max_cost_per_batch:.2f}) -- raise the cap via "
                               f"configmaint.propose or narrow the selector")
                try:
                    result = lexicalenrichgenerate.call_api(ctx, package)
                except lexicalenrichgenerate.ApiKeyMissing as e:
                    conn.rollback()
                    return fail("api-key-missing", str(e))
                except lexicalenrichgenerate.ApiCallFailed as e:
                    conn.rollback()
                    return fail("api-error", f"chunk {chunk_label}: {e}")
                rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
                rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
                real_cost = (result["input_tokens"] / 1_000_000 * rate_in +
                            result["output_tokens"] / 1_000_000 * rate_out)
                lexicalenrichgenerate.log_usage(
                    ctx.cfg, ctx.run_id, chunk_label, package["model"], result["input_tokens"],
                    result["output_tokens"], real_cost)
                llm_summary.append({"chunk": chunk_label, "verses": len(chunk),
                                    "input_tokens": result["input_tokens"],
                                    "output_tokens": result["output_tokens"],
                                    "cost_usd": round(real_cost, 4)})
                try:
                    parsed = lexicalenrichgenerate.parse_response(result["text"])
                except lexicalenrichgenerate.BadModelResponse as e:
                    conn.rollback()
                    return fail("bad-model-response", f"chunk {chunk_label}: {e}")

                try:
                    counts = lexicalenrich.enrich_passage(
                        conn, None, chunk, chunk_vd_by_osis, parsed.get("genre"),
                        parsed.get("notes", []), parsed.get("remove", []))
                except lexicalenrich.UnresolvedReference as e:
                    conn.rollback()
                    return fail("unresolved-reference",
                               f"chunk {chunk_label}: {len(e.problems)} problem(s): "
                               f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")
                except lexicalenrich.ReconciliationError as e:
                    conn.rollback()
                    return fail("unreconciled",
                               f"chunk {chunk_label}: {len(e.problems)} item(s) need "
                               f"reconciliation: {e.problems[:5]}"
                               f"{' ...' if len(e.problems) > 5 else ''}")
                complete, missing = lexicalenrich.check_completeness(conn, chunk)
                if not complete:
                    conn.rollback()
                    return fail("incomplete-block",
                               f"chunk {chunk_label}: {len(missing)} code(s) have no disposition: "
                               f"{missing[:5]}{' ...' if len(missing) > 5 else ''}")
                conn.commit()
                for k in agg:
                    agg[k] += counts[k]
            enrich_counts = agg

    parts = [f"selector={given[0]}, mode={mode}, {len(verse_ids)} verse(s)"]
    if build_totals is not None:
        parts.append(f"Layer1: {build_totals['inserted']} inserted, {build_totals['updated']} "
                     f"updated, {build_totals['unchanged']} unchanged, "
                     f"{build_totals['removed']} removed")
    if notes_path is not None:
        parts.append(f"notes briefing: {notes_path}")
    if enrich_counts is not None:
        parts.append(f"Layer2: {enrich_counts['unchanged']} unchanged, {enrich_counts['new']} new, "
                     f"{enrich_counts['changed']} corrected, {enrich_counts['removed']} removed")
    if llm_summary:
        total_cost = sum(c["cost_usd"] for c in llm_summary)
        total_in = sum(c["input_tokens"] for c in llm_summary)
        total_out = sum(c["output_tokens"] for c in llm_summary)
        parts.append(f"LLM: {len(llm_summary)} call(s), {total_in:,} in / {total_out:,} out "
                     f"tokens, ${total_cost:.4f} total")
    if zero_occurrence:
        parts.append(f"WARNING: {len(zero_occurrence)} strong(s) in this {given[0]} have NO live "
                     f"span occurrence (a stale/base-code tagging gap, not necessarily this run's "
                     f"fault) and contributed 0 verses: {zero_occurrence[:10]}"
                     f"{' ...' if len(zero_occurrence) > 10 else ''}")
    return ok("; ".join(parts), verse_count=len(verse_ids), zero_occurrence_strongs=zero_occurrence,
             notes_path=str(notes_path) if notes_path else None, llm_calls=llm_summary,
             **(build_totals or {}), **({f"note_{k}": v for k, v in (enrich_counts or {}).items()}))


# ── lexical.meaning — the verse-reading stage (#1706) ───────────────────────────────────────────
# Per-cluster, pre-subgroup, against ib_observation/ib_node. `-Preview` (default true) assembles
# every batch and reports the cost estimate without calling the API or writing. `-Preview:$false`
# runs for real: a live API call per batch, `lib/recordingpass.py` writing each result in the same
# unit of work.

def _chunk_verses_fixed_size(verse_ids: list[int], max_verses: int) -> list[list[int]]:
    """Fixed-size groups of verse_ids in the caller's order, never reordered or split mid-verse.
    The unit of operation is verses, not strongs (#1842); a failure is bounded to one batch."""
    if not verse_ids:
        return []
    return [verse_ids[i:i + max_verses] for i in range(0, len(verse_ids), max_verses)]


def _chunk_verses_by_strong_density(conn, verse_ids: list[int], max_strongs: int
                                    ) -> list[list[int]]:
    """Not called: superseded by `_chunk_verses_fixed_size` (#1842). Grouped verse_ids into chunks
    whose cumulative distinct M-code strong count stays <= max_strongs."""
    if not verse_ids:
        return []
    ph = ",".join("?" * len(verse_ids))
    rows = conn.execute(
        f"SELECT verse_id, strong, role FROM verse_lexical "
        f"WHERE verse_id IN ({ph}) AND deleted=0", verse_ids).fetchall()
    strongs_by_verse: dict[int, set[str]] = {}
    for r in rows:
        if not r["strong"]:
            continue
        roles = json.loads(r["role"]) if r["role"] else []
        if any(c.startswith("M") for c in roles):
            strongs_by_verse.setdefault(r["verse_id"], set()).add(r["strong"])

    chunks: list[list[int]] = []
    current: list[int] = []
    current_strongs: set[str] = set()
    for vid in verse_ids:
        v_strongs = strongs_by_verse.get(vid, set())
        projected = current_strongs | v_strongs
        if current and len(projected) > max_strongs:
            chunks.append(current)
            current, current_strongs = [vid], set(v_strongs)
        else:
            current.append(vid)
            current_strongs = projected
    if current:
        chunks.append(current)
    oversized = [c for c in chunks if len(c) == 1 and len(strongs_by_verse.get(c[0], set())) > max_strongs]
    if oversized:
        print(f"NOTE: {len(oversized)} single-verse chunk(s) individually exceed "
             f"max_strongs={max_strongs} on their own -- not split further, still a truncation "
             f"risk: verse_ids {[c[0] for c in oversized]}", file=sys.stderr)
    return chunks


def meaning(ctx: Ctx) -> Outcome:
    _may(ctx, "lexical.meaning", "ib_observation")
    _may(ctx, "lexical.meaning", "ib_node")
    _may(ctx, "lexical.meaning", "run_batch")

    cluster_code = ctx.params.get("ClusterCode")
    if not cluster_code:
        return fail("bad-selector", "-ClusterCode is required")
    # ctx.params values are strings: "false"/"0"/"" are off; missing means preview on
    preview_raw = ctx.params.get("Preview", "true")
    preview = str(preview_raw).strip().lower() not in ("false", "0", "no")
    # -Force: a deliberate reconciliation rerun bypasses batchcontrol.already_committed's skip; the only
    # lever that corrects existing ib_observation rows (via fresh output). Off unless set.
    force_raw = ctx.params.get("Force", "false")
    force = str(force_raw).strip().lower() in ("true", "1", "yes")

    conn = ctx.db.conn
    try:
        strongs = lexicalscope.resolve_strongs(conn, cluster_code=cluster_code)
    except ValueError as e:
        return fail("bad-selector", str(e))
    # -VerseList narrows which of this cluster's verses to run (e.g. a cheap test on a few verses);
    # -ClusterCode is still required for member strongs, prompt framing and the relational vantage
    verse_list_raw = ctx.params.get("VerseList")
    if verse_list_raw:
        refs = [x.strip() for x in verse_list_raw.split(",") if x.strip()]
        try:
            verse_ids = lexicalscope.resolve_verse_ids_for_refs(conn, refs)
        except ValueError as e:
            return fail("bad-selector", str(e))
    else:
        verse_ids = lexicalscope.resolve_verse_ids_for_strongs(conn, strongs)
    if not verse_ids:
        return fail("no-verses", f"{cluster_code} resolved to 0 verses")

    # freshness gate (#1719): refuse if Layer 1 role data is stale against current cluster_strong
    # membership. Hard stop, never a partial run.
    stale = lexical.stale_role_strongs_for_cluster(conn, cluster_code, strongs)
    if stale:
        return fail("layer1-stale",
                   f"{len(stale)} of {len(strongs)} member strong(s) have live verse_lexical rows "
                   f"that never carry {cluster_code!r} in role, despite cluster_strong currently "
                   f"listing them as members -- Layer 1 is stale for this cluster (#1719). Re-run "
                   f"lexical.build for the verses containing these strongs before verse-reading: "
                   f"{stale}")

    # whole-verse exclusion (#1824): the first cluster's pass to touch a verse analyses every M-code
    # word in it, so a later cluster does not re-derive it. -Force bypasses this.
    fully_covered_ids: set = set()
    if not force:
        fully_covered_ids = stage1coverage.fully_covered_verse_ids(
            conn, cluster_code, verse_ids, family="word_level")
        if fully_covered_ids:
            verse_ids = [v for v in verse_ids if v not in fully_covered_ids]
    if not verse_ids:
        return ok(f"{cluster_code}: all {len(fully_covered_ids)} requested verse(s) are already "
                 f"fully covered (every expected question answered by an earlier pass) -- "
                 f"nothing to do. Use -Force to re-examine them anyway.",
                 preview=preview, cluster_code=cluster_code,
                 fully_covered_verse_count=len(fully_covered_ids))

    # fixed verse-count chunking (#1842)
    max_verses = int(ctx.cfg.setting("lexical.meaning_max_verses_per_batch", 1))
    max_cost_per_batch = float(ctx.cfg.setting("lexical.llm_max_cost_per_batch", 1.00))
    chunks = _chunk_verses_fixed_size(verse_ids, max_verses)

    batch_summaries = []
    llm_summary = []
    record_summary = {"by_action": {}, "unresolved_occurrence_count": 0, "unresolved_detail": []}
    skipped_batches = 0

    for idx, chunk in enumerate(chunks):
        chunk_label = f"{idx + 1}/{len(chunks)}"
        package = versereadinggenerate.assemble_word_level_batch_package(
            ctx, cluster_code, chunk, force=force)
        content_key = batchcontrol.content_key([str(v) for v in chunk])
        already_done = batchcontrol.already_committed(
            conn, "lexical.meaning", cluster_code, content_key)
        batch_summaries.append({
            "chunk": chunk_label, "verses": package["verse_count"],
            "cluster_member_strongs": package["cluster_member_strong_count"],
            "est_input_tokens": package["est_input_tokens"],
            "est_cost_usd": package["est_cost_usd"],
            "already_committed": already_done})
        if package["est_cost_usd"] > max_cost_per_batch:
            return fail("cost-cap-exceeded",
                       f"chunk {chunk_label} ({package['verse_count']} verses) estimated cost "
                       f"${package['est_cost_usd']:.2f} exceeds lexical.llm_max_cost_per_batch "
                       f"(${max_cost_per_batch:.2f}) -- raise the cap via configmaint.propose or "
                       f"narrow the selector")
        if preview:
            continue

        # resume/skip (#1756): a batch already committed (matched by content, checked fresh) is not
        # re-paid; -Force overrides
        if already_done and not force:
            skipped_batches += 1
            continue

        batch_id = batchcontrol.start_batch(
            conn, ctx.run_id, "verse-lexical", "lexical.meaning", cluster_code, idx + 1,
            content_key)
        try:
            try:
                result = versereadinggenerate.call_api(ctx, package)
            except versereadinggenerate.ApiKeyMissing as e:
                batchcontrol.fail_batch(conn, batch_id, str(e))
                return fail("api-key-missing", str(e))
            except versereadinggenerate.ApiCallFailed as e:
                batchcontrol.fail_batch(conn, batch_id, str(e))
                return fail("api-error", f"chunk {chunk_label}: {e}")
            rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
            rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
            real_cost = (result["input_tokens"] / 1_000_000 * rate_in +
                        result["output_tokens"] / 1_000_000 * rate_out)
            versereadinggenerate.log_usage(
                ctx.cfg, ctx.run_id, chunk_label, package["model"], result["input_tokens"],
                result["output_tokens"], real_cost)
            llm_summary.append({"chunk": chunk_label, "verses": package["verse_count"],
                                "input_tokens": result["input_tokens"],
                                "output_tokens": result["output_tokens"],
                                "cost_usd": round(real_cost, 4)})

            try:
                parsed = versereadinggenerate.parse_response(result["text"])
            except versereadinggenerate.BadModelResponse as e:
                conn.rollback()
                batchcontrol.fail_batch(conn, batch_id, f"bad-model-response: {e}")
                return fail("bad-model-response", f"chunk {chunk_label}: {e}")

            chunk_record = recordingpass.record_batch(
                conn, cluster_code, "verse-reading", parsed, source_json_serial=idx + 1,
                similarity_threshold=float(ctx.cfg.setting("cluster.recording_similarity_threshold", 0.85)))
            conn.commit()
        except Exception as e:
            # crash safeguard (#1756): record any exception in the risky window before re-raising, so a
            # run_batch row left at 'running' means only a real process death
            batchcontrol.fail_batch(conn, batch_id, f"{type(e).__name__}: {e}")
            raise
        batchcontrol.commit_batch(conn, batch_id, cost_usd=round(real_cost, 4))
        for action, n in chunk_record["by_action"].items():
            record_summary["by_action"][action] = record_summary["by_action"].get(action, 0) + n
        record_summary["unresolved_occurrence_count"] += chunk_record["unresolved_occurrence_count"]
        record_summary["unresolved_detail"] += chunk_record["unresolved_detail"]

    if preview:
        already_n = sum(1 for b in batch_summaries if b["already_committed"])
        # cost: only uncommitted batches, unless -Force re-calls every batch
        total_cost = sum(b["est_cost_usd"] for b in batch_summaries
                         if force or not b["already_committed"])
        already_note = ("" if not already_n else
                        f", {already_n} of {len(chunks)} already committed by a prior run "
                        f"({'will be RE-RUN, -Force is set' if force else 'will be skipped'})")
        fully_covered_note = (f", {len(fully_covered_ids)} verse(s) excluded entirely (already "
                             f"fully covered by an earlier pass)" if fully_covered_ids else "")
        return ok(f"PREVIEW {cluster_code}: {len(chunks)} batch(es), {len(verse_ids)} verse(s), "
                 f"{len(strongs)} strong(s), estimated ${total_cost:.4f} total for the "
                 f"{'forced re-run' if force else 'remaining work'}{already_note}"
                 f"{fully_covered_note} -- no API call "
                 f"made, nothing written. Re-run with -Preview:$false to execute for real.",
                 preview=True, batches=batch_summaries, cluster_code=cluster_code,
                 verse_count=len(verse_ids), strong_count=len(strongs), force=force)

    # cluster.status advances in relational(), the final verse-reading stage (#1860)

    # LLM validation check (#1824): expected vs received word-level rows over the full requested
    # scope, read-only. Per-row detail goes to a report; the summary counts go into the message, the
    # only part run.outcome keeps.
    coverage = stage1coverage.validate_coverage(conn, cluster_code, verse_ids, family="word_level")
    # report path from config (report.stage1_coverage_validation_pattern)
    coverage_pattern = ctx.cfg.required_setting("report.stage1_coverage_validation_pattern")
    coverage_report_path = pathlib.Path(
        coverage_pattern.format(cluster_code=cluster_code, run_id=ctx.run_id))
    coverage_report_path.parent.mkdir(parents=True, exist_ok=True)
    with coverage_report_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["category", "verse_reference", "strong", "question_code", "live_node_count"])
        for v, s, q in coverage["missing_sample"]:
            w.writerow(["MISSING", v, s, q, 0])
        for v, s, q in coverage["unexpected_sample"]:
            w.writerow(["UNEXPECTED", v, s, q, ""])
        for (v, s, q), n in coverage["over_count_sample"]:
            w.writerow(["OVER_COUNT", v, s, q, n])
    coverage_note = (f"; validation: {coverage['ok_count']} ok, {coverage['missing_count']} "
                     f"missing, {coverage['unexpected_count']} unexpected, "
                     f"{coverage['over_count_count']} over-count (of {coverage['expected_count']} "
                     f"expected) -- {coverage_report_path}")

    total_cost = sum(c["cost_usd"] for c in llm_summary)
    unresolved_n = record_summary["unresolved_occurrence_count"]
    # the reasons themselves go into the message: run.outcome keeps only the message string
    unresolved_note = (f", {unresolved_n} unresolved occurrence(s): "
                       f"{'; '.join(record_summary['unresolved_detail'][:5])}"
                       f"{' ...' if unresolved_n > 5 else ''}") if unresolved_n else ""
    skipped_note = f", {skipped_batches} batch(es) skipped (already committed)" if skipped_batches else ""
    fully_covered_note = (f", {len(fully_covered_ids)} verse(s) excluded entirely (already fully "
                         f"covered by an earlier pass)" if fully_covered_ids else "")
    return ok(f"{cluster_code}: {len(chunks)} batch(es){skipped_note}{fully_covered_note}, "
             f"${total_cost:.4f} spent, "
             f"observations {record_summary['by_action']}{unresolved_note}"
             f"{coverage_note}; word-level only -- run lexical.relational next for this cluster",
             preview=False, batches=batch_summaries, llm_calls=llm_summary,
             record_summary=record_summary, cluster_code=cluster_code,
             skipped_batches=skipped_batches, coverage=coverage,
             fully_covered_verse_count=len(fully_covered_ids))


def relational(ctx: Ctx) -> Outcome:
    """`lexical.relational` (#1860): the relational questions (M0.6.5/M0.6.6/D7.7.1/M0.7.1-16/
    M0.8.1). Same batch/cost/resume/coverage-validation structure as `meaning()`, plus: (1) a hard
    readiness gate refusing any verse whose M-code words lack committed word-level observations;
    (2) the `cluster.status` `t_cluster_assignment_completed -> ready_for_subgroup_allocation`
    transition, since this is the final stage of verse-reading."""
    _may(ctx, "lexical.relational", "ib_observation")
    _may(ctx, "lexical.relational", "ib_node")
    _may(ctx, "lexical.relational", "run_batch")

    cluster_code = ctx.params.get("ClusterCode")
    if not cluster_code:
        return fail("bad-selector", "-ClusterCode is required")
    preview_raw = ctx.params.get("Preview", "true")
    preview = str(preview_raw).strip().lower() not in ("false", "0", "no")
    force_raw = ctx.params.get("Force", "false")
    force = str(force_raw).strip().lower() in ("true", "1", "yes")

    conn = ctx.db.conn
    try:
        strongs = lexicalscope.resolve_strongs(conn, cluster_code=cluster_code)
    except ValueError as e:
        return fail("bad-selector", str(e))
    verse_list_raw = ctx.params.get("VerseList")
    if verse_list_raw:
        refs = [x.strip() for x in verse_list_raw.split(",") if x.strip()]
        try:
            verse_ids = lexicalscope.resolve_verse_ids_for_refs(conn, refs)
        except ValueError as e:
            return fail("bad-selector", str(e))
    else:
        verse_ids = lexicalscope.resolve_verse_ids_for_strongs(conn, strongs)
    if not verse_ids:
        return fail("no-verses", f"{cluster_code} resolved to 0 verses")

    stale = lexical.stale_role_strongs_for_cluster(conn, cluster_code, strongs)
    if stale:
        return fail("layer1-stale",
                   f"{len(stale)} of {len(strongs)} member strong(s) have live verse_lexical rows "
                   f"that never carry {cluster_code!r} in role, despite cluster_strong currently "
                   f"listing them as members -- Layer 1 is stale for this cluster (#1719). Re-run "
                   f"lexical.build for the verses containing these strongs before verse-reading: "
                   f"{stale}")

    # readiness gate (#1860): relational grounds on committed word-level findings, so a verse
    # without them stops the run
    if not force:
        gaps = stage1coverage.missing_word_level_coverage(conn, cluster_code, verse_ids)
        if gaps:
            sample = gaps[:15]
            return fail("word-level-incomplete",
                       f"{len(gaps)} (verse, strong) word-level gap(s) in the requested scope -- "
                       f"lexical.relational refuses to run until every M-code word has a committed "
                       f"lexical.meaning observation. Run lexical.meaning for {cluster_code} (or "
                       f"the relevant verses) first. Sample: "
                       f"{[(g['verse_reference'], g['strong']) for g in sample]}"
                       f"{' ...' if len(gaps) > 15 else ''}")

    fully_covered_ids: set = set()
    if not force:
        fully_covered_ids = stage1coverage.fully_covered_verse_ids(
            conn, cluster_code, verse_ids, family="relational")
        if fully_covered_ids:
            verse_ids = [v for v in verse_ids if v not in fully_covered_ids]
    if not verse_ids:
        return ok(f"{cluster_code}: all {len(fully_covered_ids)} requested verse(s) are already "
                 f"fully covered (every expected question answered by an earlier pass) -- "
                 f"nothing to do. Use -Force to re-examine them anyway.",
                 preview=preview, cluster_code=cluster_code,
                 fully_covered_verse_count=len(fully_covered_ids))

    max_verses = int(ctx.cfg.setting("lexical.relational_max_verses_per_batch", 1))
    max_cost_per_batch = float(ctx.cfg.setting("lexical.llm_max_cost_per_batch", 1.00))
    chunks = _chunk_verses_fixed_size(verse_ids, max_verses)

    batch_summaries = []
    llm_summary = []
    record_summary = {"by_action": {}, "unresolved_occurrence_count": 0, "unresolved_detail": []}
    skipped_batches = 0

    for idx, chunk in enumerate(chunks):
        chunk_label = f"{idx + 1}/{len(chunks)}"
        package = versereadinggenerate.assemble_relational_batch_package(
            ctx, cluster_code, chunk, force=force)
        content_key = batchcontrol.content_key([str(v) for v in chunk])
        already_done = batchcontrol.already_committed(
            conn, "lexical.relational", cluster_code, content_key)
        batch_summaries.append({
            "chunk": chunk_label, "verses": package["verse_count"],
            "cluster_member_strongs": package["cluster_member_strong_count"],
            "est_input_tokens": package["est_input_tokens"],
            "est_cost_usd": package["est_cost_usd"],
            "already_committed": already_done})
        if package["est_cost_usd"] > max_cost_per_batch:
            return fail("cost-cap-exceeded",
                       f"chunk {chunk_label} ({package['verse_count']} verses) estimated cost "
                       f"${package['est_cost_usd']:.2f} exceeds lexical.llm_max_cost_per_batch "
                       f"(${max_cost_per_batch:.2f}) -- raise the cap via configmaint.propose or "
                       f"narrow the selector")
        if preview:
            continue

        if already_done and not force:
            skipped_batches += 1
            continue

        batch_id = batchcontrol.start_batch(
            conn, ctx.run_id, "verse-lexical", "lexical.relational", cluster_code, idx + 1,
            content_key)
        try:
            try:
                result = versereadinggenerate.call_api(ctx, package)
            except versereadinggenerate.ApiKeyMissing as e:
                batchcontrol.fail_batch(conn, batch_id, str(e))
                return fail("api-key-missing", str(e))
            except versereadinggenerate.ApiCallFailed as e:
                batchcontrol.fail_batch(conn, batch_id, str(e))
                return fail("api-error", f"chunk {chunk_label}: {e}")
            rate_in = float(ctx.cfg.setting("lexical.llm_rate_input_per_million", 3.00))
            rate_out = float(ctx.cfg.setting("lexical.llm_rate_output_per_million", 15.00))
            real_cost = (result["input_tokens"] / 1_000_000 * rate_in +
                        result["output_tokens"] / 1_000_000 * rate_out)
            versereadinggenerate.log_usage(
                ctx.cfg, ctx.run_id, chunk_label, package["model"], result["input_tokens"],
                result["output_tokens"], real_cost)
            llm_summary.append({"chunk": chunk_label, "verses": package["verse_count"],
                                "input_tokens": result["input_tokens"],
                                "output_tokens": result["output_tokens"],
                                "cost_usd": round(real_cost, 4)})

            try:
                parsed = versereadinggenerate.parse_response(result["text"])
            except versereadinggenerate.BadModelResponse as e:
                conn.rollback()
                batchcontrol.fail_batch(conn, batch_id, f"bad-model-response: {e}")
                return fail("bad-model-response", f"chunk {chunk_label}: {e}")

            chunk_record = recordingpass.record_batch(
                conn, cluster_code, "verse-reading", parsed, source_json_serial=idx + 1,
                similarity_threshold=float(ctx.cfg.setting("cluster.recording_similarity_threshold", 0.85)))
            conn.commit()
        except Exception as e:
            batchcontrol.fail_batch(conn, batch_id, f"{type(e).__name__}: {e}")
            raise
        batchcontrol.commit_batch(conn, batch_id, cost_usd=round(real_cost, 4))
        for action, n in chunk_record["by_action"].items():
            record_summary["by_action"][action] = record_summary["by_action"].get(action, 0) + n
        record_summary["unresolved_occurrence_count"] += chunk_record["unresolved_occurrence_count"]
        record_summary["unresolved_detail"] += chunk_record["unresolved_detail"]

    if preview:
        already_n = sum(1 for b in batch_summaries if b["already_committed"])
        total_cost = sum(b["est_cost_usd"] for b in batch_summaries
                         if force or not b["already_committed"])
        already_note = ("" if not already_n else
                        f", {already_n} of {len(chunks)} already committed by a prior run "
                        f"({'will be RE-RUN, -Force is set' if force else 'will be skipped'})")
        fully_covered_note = (f", {len(fully_covered_ids)} verse(s) excluded entirely (already "
                             f"fully covered by an earlier pass)" if fully_covered_ids else "")
        return ok(f"PREVIEW {cluster_code}: {len(chunks)} batch(es), {len(verse_ids)} verse(s), "
                 f"{len(strongs)} strong(s), estimated ${total_cost:.4f} total for the "
                 f"{'forced re-run' if force else 'remaining work'}{already_note}"
                 f"{fully_covered_note} -- no API call "
                 f"made, nothing written. Re-run with -Preview:$false to execute for real.",
                 preview=True, batches=batch_summaries, cluster_code=cluster_code,
                 verse_count=len(verse_ids), strong_count=len(strongs), force=force)

    # the final stage of verse-reading: checked and advanced after every live run (#1860)
    status_result = clusterstatus.advance_if_verse_reading_complete(conn, cluster_code)
    conn.commit()

    coverage = stage1coverage.validate_coverage(conn, cluster_code, verse_ids, family="relational")
    coverage_pattern = ctx.cfg.required_setting("report.stage1_coverage_validation_pattern")
    coverage_report_path = pathlib.Path(
        coverage_pattern.format(cluster_code=cluster_code, run_id=ctx.run_id))
    coverage_report_path.parent.mkdir(parents=True, exist_ok=True)
    with coverage_report_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["category", "verse_reference", "strong", "question_code", "live_node_count"])
        for v, s, q in coverage["missing_sample"]:
            w.writerow(["MISSING", v, s, q, 0])
        for v, s, q in coverage["unexpected_sample"]:
            w.writerow(["UNEXPECTED", v, s, q, ""])
        for (v, s, q), n in coverage["over_count_sample"]:
            w.writerow(["OVER_COUNT", v, s, q, n])
    coverage_note = (f"; validation: {coverage['ok_count']} ok, {coverage['missing_count']} "
                     f"missing, {coverage['unexpected_count']} unexpected, "
                     f"{coverage['over_count_count']} over-count (of {coverage['expected_count']} "
                     f"expected) -- {coverage_report_path}")

    total_cost = sum(c["cost_usd"] for c in llm_summary)
    unresolved_n = record_summary["unresolved_occurrence_count"]
    unresolved_note = (f", {unresolved_n} unresolved occurrence(s): "
                       f"{'; '.join(record_summary['unresolved_detail'][:5])}"
                       f"{' ...' if unresolved_n > 5 else ''}") if unresolved_n else ""
    status_note = (f"; cluster.status -> ready_for_subgroup_allocation" if status_result["advanced"]
                  else f"; {len(status_result['missing_strongs'])} of "
                       f"{status_result['member_strong_count']} strong(s) still need verse-reading "
                       f"before subgroup allocation can start" if not status_result["complete"]
                  else "")
    skipped_note = f", {skipped_batches} batch(es) skipped (already committed)" if skipped_batches else ""
    fully_covered_note = (f", {len(fully_covered_ids)} verse(s) excluded entirely (already fully "
                         f"covered by an earlier pass)" if fully_covered_ids else "")
    return ok(f"{cluster_code}: {len(chunks)} batch(es){skipped_note}{fully_covered_note}, "
             f"${total_cost:.4f} spent, "
             f"observations {record_summary['by_action']}{unresolved_note}{status_note}"
             f"{coverage_note}",
             preview=False, batches=batch_summaries, llm_calls=llm_summary,
             record_summary=record_summary, cluster_code=cluster_code,
             status_result=status_result, skipped_batches=skipped_batches, coverage=coverage,
             fully_covered_verse_count=len(fully_covered_ids))
