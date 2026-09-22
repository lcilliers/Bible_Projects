"""lexical.py — dispatcher handler for `lexical.build`/`lexical.enrich` (the old `-Book`+range
signature, ordinals 0/2, left in place but superseded for cluster/strong-driven work — see `run`
below) and `lexical.run` (ordinal 5, the real front door since the researcher's 2026-09-07
correction: "it is fundamentally built on books and passages which contradicts the analytic
operation for clusters and groups of strongs"). `build`/`enrich` are thin adapters over
`lib/lexical.py`/`lib/lexicalenrich.py` — payload loading + verse resolution + write-grant checks
live here (handler layer), the actual reconciliation/write logic lives in those lib modules
(escalation #1383, build spec §C.2/§E.2).

`run` (step `lexical.run`) resolves a selector (`-ClusterCode`/`-Word`/`-StrongList`/`-VerseList`,
via `lib/lexicalscope.py`) to a verse-id list ONCE, then `-Mode` picks the work
(`Layer1AndLayer2`/`Layer1Only`/`Layer2Only`) — Layer 2 never independently re-resolves scope, it's
always handed the ids Layer 1 already has. `_notes_payload_dict`/`_write_notes_payload` are the
former standalone `lexical.notes` step (escalation #1549's original ask), folded into `run`'s own
Layer-2 path rather than kept as a separate command to remember to run first — researcher
instruction, 2026-09-07: "yes include lexical.note production, but suppressed by a flag. default -
output the result." Produced on by default whenever `-Mode` includes Layer 2 (before any write is
attempted — it's the briefing pack a reading pass needs BEFORE deciding what a payload should say,
never the payload itself), opt out with `-SuppressNotes`. Content: every live `verse_lexical`
column per code (not the narrower subset `report.lexical_extract` returns), the verse's own base
text, any already-live `verse_lexical_note` rows (so a re-run sees what the reconciliation rule will
require it to re-address), and the catalogue — `cfg_method_rule` (queryable home for every
note_type rule since #1449/#1450/#1451/#1527) plus `cfg_enum`'s `note_type`/`resolution_status`
value lists. Never a DB write itself, regardless of mode.

**Verse-scoped since escalation #1451 (2026-09-05)** — `enrich`/`run` never resolve or require a
`passage` row (dropped the `passagetrack.find_tracked_passage`/`no-passage` gate entirely).
`passage`/`passage.build` is Window 2's own debate-pipeline construct, gated by `hib.set`; Window 1
Layer 2 must never depend on HIB-gated infrastructure — full design record `iba/docs/1451-
window1-layer2-verse-scoped-redesign-v1-20260905.md`.

Auto-backfill reused unchanged from `report.verse_span_meaning`'s own pattern (`report.
auto_backfill_before_render`, `raw.backfill_meaning_for`) — a content-role code with no `strong`
row yet gets pulled from STEP before building, same researcher instruction (2026-07-26), same
setting, not a new one. `build`/`enrich` still use it; `run` calls `build_for_verse_ids` directly
(no auto-backfill wired in yet — open item, not needed for the cases tested so far).
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


# ── lexical.readiness — the 3-leg base-data readiness check (#1606, Phase A item 1) ─────────────
# Registered 2026-09-16 (escalation #1706 Phase A/#1711 build). Researcher's own framing, #1606:
# "lexical readiness is a precursor for the lexical reading stage, which is a precursor for the
# sub group." Read-only, always persists a report (governance.reports_must_persist), escalates
# only on a FATAL finding -- same shape as spine.check, deliberately not merged into it (spine
# covers the whole-project verse/span/strong spine; this is lexical-build-specific: it also checks
# the cluster-allocation precondition Layer 1's new `role` column depends on, which spine.check has
# no reason to know about).
#
# Leg 1 -- every live verse has >=1 live span (a verse present but never segmented can't build).
# Leg 2 -- every live span's strong_variant code resolves to a live `strong` row (same desync
#          spine.check already reports; duplicated here deliberately -- #1606's own framing is one
#          cohesive 3-leg check, not "2 legs plus a pointer to a different report").
# Leg 3 -- every live `strong` row that actually OCCURS in a live span (not every row in the table
#          -- an unused placeholder strong is a different question, not this check's concern) has
#          >=1 live `cluster_strong` allocation. This is the one Layer 1's redesigned `role` column
#          (a JSON array of cluster_strong.cluster_code, #1706 Phase B item 3) depends on directly:
#          a strong with zero allocation would resolve to an empty array, which the new pre-run
#          validator (see `_check_role_readiness` in lib/lexical.py) treats as a hard failure.

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
    # base-strip via lib.lexical._base isn't needed here -- cluster_strong.strong carries the exact
    # suffixed code (same convention as span_codes above), matching reference_strong_related_keyed_
    # on_exact_code_not_base's own lesson: compare exact codes, never base-strip before the lookup.
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

    # Verse-scoped (escalation #1451, 2026-09-05 — full record `iba/docs/1451-window1-layer2-
    # verse-scoped-redesign-v1-20260905.md`): no `passage` row is resolved or required. `passage`/
    # `passage.build` is Window 2's own debate-pipeline construct, gated by `hib.set` — Window 1
    # Layer 2 must never depend on it. Verses resolve directly from -Book/-Range/-Chapters, same
    # helper `lexical.build` and `report.verse_span_meaning` already use.
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

    complete, missing = lexicalenrich.check_completeness(ctx.db.conn, verse_ids)
    if not complete:
        ctx.db.conn.rollback()
        return fail("incomplete-block",
                   f"{len(missing)} code(s) in this block have no disposition: "
                   f"{missing[:5]}{' ...' if len(missing) > 5 else ''} — every applicable code "
                   f"needs a finding or an explicit checked_empty/unresolved")

    # No lexicalenrich.set_lexical_complete() call -- there is no `passage` row to hang
    # completeness on in the verse-scoped design (escalation #1451). Where per-verse completeness
    # should persist long-term is still undesigned; the check above still gates the write, it's
    # just not recorded anywhere yet.
    ctx.db.conn.commit()

    genre_note = " (genre supplied but not persisted -- no per-verse home designed yet)" \
        if counts.get("genre_dropped") else ""
    return ok(f"{book} {lo}-{hi}: {counts['unchanged']} unchanged, {counts['new']} new, "
             f"{counts['changed']} corrected, {counts['removed']} removed note(s); "
             f"block complete{genre_note}", **counts)


# ── lexical.notes briefing pack — folded into lexical.run's Layer 2 path, 2026-09-07 ────────────
#
# Retired as its own Book/Range-scoped step (was never registered -- superseded before approval,
# escalations #1551/#1552). Researcher instruction, this session: "yes include lexical.note
# production, but suppressed by a flag. default - output the result." -- so this is no longer a
# separate command to remember to run first; `run()` produces it automatically as part of any
# Layer-2-involving call, `-SuppressNotes` opts out. Generalized off a verse_id list (no `book`
# param -- a cluster/strong-driven scope is cross-book) rather than Book/Range.

def _notes_payload_dict(ctx: Ctx, verse_ids: list[int]) -> dict:
    """Never a DB write -- this is the briefing pack a reading pass needs BEFORE it can decide what
    a Layer 2 payload should say, not the payload itself (that decision is a human/AI judgement
    call this function cannot make). Same content shape as the original #1549 `lexical.notes`
    design: every live `verse_lexical` column per code, the verse's own base text, any already-live
    `verse_lexical_note` rows (so a re-run sees what the reconciliation rule will require it to
    re-address), cluster tags, and the full `cfg_method_rule`/`cfg_enum` catalogue."""
    # resolved_sense/ambiguity_note/language DROPPED from verse_lexical 2026-09-16 (#1706 Phase B)
    # -- this whole `lexical.enrich`/verse_lexical_note-based Layer 2 path is superseded by the new
    # ib_observation architecture (#1691/#1597 resolution-by-architecture) and retired in cfg_step
    # the same unit of work; this SQL fix keeps it from crashing on the dropped columns in the
    # meantime, it does not resurrect the path as a going concern -- see module docstring banner.
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

    # Cluster tags -- same lookup/rationale as report.lexical_extract (2026-09-05): computed at
    # request time, never a stored verse_lexical column (cluster_strong keeps changing), keyed on
    # the EXACT strong code (strong_related lesson), every live membership returned.
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

    # verse.text is NULL for 722 of 29,759 live verses (found live building this) -- those verses
    # were onboarded via a path (handlers/raw.py:verses/call3_strong) that only ever wrote
    # osisId/reference/preview, never text itself. Rather than silently showing "text": null (a real
    # gap, briefing pack is supposed to be self-contained), reconstruct it from the codes already
    # resolved for that verse -- every one already carries its own `surface` word in position
    # order, no HTML-parsing of `preview` needed. Labeled, not passed off as the genuine field.
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


# ── lexical.run — the real front door, researcher correction 2026-09-07 ────────────────────────
#
# "the current code is stale... it is fundamentally built on books and passages which contradicts
# the analytic operation for clusters and groups of strongs." The real input is a scattered,
# cross-book verse list generated as a subset via a cluster or group of strongs -- resolution:
# ClusterCode/Word -> strong-list (lexicalscope.resolve_strongs) -> verse-list
# (lexicalscope.resolve_verse_ids_for_strongs, span.strong_variant -- NOT strong_verse, see that
# module's own docstring for why). VerseList is a fourth selector for a verse set that's already
# known (e.g. carried forward from a prior session's own finding) -- no strong/cluster involved.
#
# "my vision is that you will be able to set a flag that can select: do layer 1 and layer 2; do
# layer 1 without a refresh of layer 2; do layer 2 without a refresh of layer 1. in all cases input
# is in the front end of layer 1, and the update choice takes place from there. layer 2 always gets
# its primary data [prompt] from layer 1." -- one entry point, `-Mode` picks the work, verse-list
# resolution happens exactly once regardless of mode. Layer 1's own write (`build_for_verse_ids`)
# is already identity-stable (escalation #1520/#1451) -- a Layer1Only or Layer1AndLayer2 call on
# verses that haven't changed is a safe no-op, never orphans a live Layer 2 note. Layer2Only skips
# the write entirely and fails fast (`no-layer1`) naming any verse that has none yet.
#
# Cap: one config setting (`lexical.run_max_verses`), enforced once against the resolved verse-list
# before any work happens -- not split by layer. Researcher, 2026-09-07: "I am OK for adding a max
# cap in config to prevent the system grinding to a halt" -- stated as a blunt safety ceiling, not a
# tuned per-layer budget; "we have as yet no method to confirm or prototype how the reading list
# should look like to be effective" is the reason NOT to over-design this now. A future split
# (Layer 1 unbounded, Layer 2 capped) is a config change, not a code change, if it turns out needed.

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
            # -StrongList is already validated against real span presence inside resolve_strongs
            # itself; -ClusterCode/-Word are NOT (a cluster/word's own tagging can carry a stale
            # code -- found live, 3 real cluster_strong rows do exactly this, see
            # lexicalscope.strongs_with_no_occurrence's own docstring). Surfaced as a named warning
            # in the result, never silently dropped -- narrowing a cluster's content without saying
            # so is exactly the kind of oversight this build was corrected for.
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
        # STEP-availability gate REMOVED here 2026-09-16 (#1706 Phase B) -- Layer 1 no longer
        # calls STEP at all (resolve_code's old live_step_meaning ambiguity fallback is gone with
        # ambiguity_note/resolved_sense); this mode's own write path has no STEP dependency left.
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

        # The briefing pack (old #1549 `lexical.notes`) -- researcher instruction, 2026-09-07:
        # "yes include lexical.note production, but suppressed by a flag. default - output the
        # result." Produced BEFORE any write attempt (reflects current state, "layer 2 always gets
        # its primary data prompt from layer 1" -- this IS that prompt), on by default, opt out
        # with -SuppressNotes.
        if not ctx.params.get("SuppressNotes"):
            notes_path, _ = _write_notes_payload(ctx, verse_ids)

        raw_payload = ctx.params.get("PayloadPath")
        if raw_payload:
            # Manual path -- a payload already decided by a reading pass (human or a separate AI
            # session), unchanged from the original design.
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
            # Explicit opt-out -- the old behaviour, notes briefing only, nothing written.
            if notes_path is None:
                return fail("bad-payload", "-PayloadPath is required to write Layer 2 when both "
                                           "-NoAutoLLM and -SuppressNotes are given -- nothing to do")

        else:
            # DEFAULT since researcher instruction 2026-09-07: "layer 2 will consume llm and it
            # must be part of the routine, rather than parking it." Batched by passage.max_verses
            # (same bound lexical.enrich's own manual path already enforces) -- never one call over
            # the whole resolved scope. Each chunk: assemble -> cost-estimate -> hard cap check
            # (same "an approved specification is the approval" pattern as narrative.generate,
            # escalation #798/#799 SS3.4 -- no separate pause, the configured cap IS the gate) ->
            # live call -> parse -> write via the SAME enrich_passage/check_completeness path the
            # manual payload uses -> log real usage. One chunk's failure stops the whole run
            # (report-stop) rather than silently completing a partial cluster.
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


# ── lexical.meaning — the `verse-reading` stage execution (#1706 Phase C, 2026-09-17) ────────────
#
# Per-cluster, pre-subgroup Layer 2 against the LIVE ib_observation/ib_node architecture -- NOT
# lexical.enrich's retired verse_lexical_note shape. `-Preview` (default true) assembles every batch
# and reports the cost estimate WITHOUT calling the API or writing anything -- this is a brand-new,
# never-yet-run mechanism; the existing project convention ("the configured cost cap IS the
# approval, no separate pause" -- lexical.run's own Layer 2 path) governs ONGOING runs once this has
# been validated live at least once, not the very first invocation of untested code. `-Preview:$false`
# runs for real: live API call per batch, `lib/recordingpass.py` writes every result in the same
# unit of work (checklist rule 0.3), never a deferred batch pickup.

def _chunk_verses_by_strong_density(conn, verse_ids: list[int], max_strongs: int
                                    ) -> list[list[int]]:
    """#1825/#1826/#1827: groups verse_ids (already in caller's own order -- never reordered) into
    chunks whose CUMULATIVE distinct M-code strong count stays <= max_strongs -- front-loading
    means output volume tracks strong count, not verse count, so this is the real cost driver to
    cap, not a proxy. Greedy, single pass: a verse whose own M-code strong set is entirely already
    in the running chunk total costs nothing extra; a verse that would push the chunk over the cap
    starts a new chunk instead. A single verse whose OWN strong count alone exceeds max_strongs
    still gets its own one-verse chunk (never split mid-verse, never silently dropped) -- flagged
    via a printed note since that one chunk will still risk truncation, but the alternative
    (splitting one verse's own front-loaded battery across two calls) is not designed."""
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
    # ctx.params values are always strings (CLI --param Key=Value) -- "false"/"0"/"" must NOT be
    # truthy, unlike a bare Python string. Missing key defaults to preview-on (see module banner:
    # never a live call by default for a just-built, never-yet-run mechanism).
    preview_raw = ctx.params.get("Preview", "true")
    preview = str(preview_raw).strip().lower() not in ("false", "0", "no")
    # -Force (#1824 v10/v11, Fix 3): a deliberate reconciliation rerun needs to bypass
    # batchcontrol.already_committed's permanent skip -- without it, "rerun Stage 1 to reconcile"
    # can never actually re-examine anything already committed. Never the default (missing/"false"/
    # "0" all mean off, same truthy convention as -Preview above); this is the ONLY lever that
    # triggers any correction to existing ib_observation rows, per the design doc's own governing
    # principle (no offline scripts ever touch old data -- only a real rerun's fresh output does).
    force_raw = ctx.params.get("Force", "false")
    force = str(force_raw).strip().lower() in ("true", "1", "yes")

    conn = ctx.db.conn
    try:
        strongs = lexicalscope.resolve_strongs(conn, cluster_code=cluster_code)
    except ValueError as e:
        return fail("bad-selector", str(e))
    # -VerseList (2026-09-22): restricts the run to an explicit, small verse subset instead of the
    # cluster's full remaining-work resolution -- needed for a cheap, disposable live test (e.g.
    # validating a rerun's behaviour against a handful of verses that already carry pre-existing
    # observations), same helper the legacy lexical.run step already uses for its own -VerseList.
    # -ClusterCode is still required alongside it: member-strong context, prompt framing, and the
    # M0.6.5/M0.6.6 relational vantage are all this cluster's own, not derivable from the verses
    # alone -- VerseList narrows WHICH of that cluster's verses to run, not which cluster's pass.
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

    # Pre-verse-reading freshness gate (#1719, researcher instruction 2026-09-17): refuse to run
    # against a cluster whose Layer 1 role data is stale relative to CURRENT cluster_strong
    # membership -- found live on M67/M60, where 9 member strongs were silently invisible to the
    # LLM because cluster_strong changed after Layer 1's last build for their verses. Hard stop,
    # same pattern as every other readiness check in this module -- never a silent partial run.
    stale = lexical.stale_role_strongs_for_cluster(conn, cluster_code, strongs)
    if stale:
        return fail("layer1-stale",
                   f"{len(stale)} of {len(strongs)} member strong(s) have live verse_lexical rows "
                   f"that never carry {cluster_code!r} in role, despite cluster_strong currently "
                   f"listing them as members -- Layer 1 is stale for this cluster (#1719). Re-run "
                   f"lexical.build for the verses containing these strongs before verse-reading: "
                   f"{stale}")

    # Whole-verse exclusion (#1824 v18, researcher instruction 2026-09-22, verbatim: "when M32
    # cluster is processed then all the analysis for verses already analysed previously is not
    # recreated... if the second read of the verse finds additional observations then something
    # went wrong in the first reading"). Since BUILD #316, the FIRST cluster's pass to touch a
    # verse already does complete Stage 1 analysis of every M-code word in it -- a LATER cluster
    # whose own strong happens to occur in that same verse should not re-derive it at all.
    # -Force intentionally bypasses this (a deliberate reconciliation rerun, Fix 3, exists
    # precisely to re-examine already-covered material) -- never applied together.
    fully_covered_ids: set = set()
    if not force:
        fully_covered_ids = stage1coverage.fully_covered_verse_ids(conn, cluster_code, verse_ids)
        if fully_covered_ids:
            verse_ids = [v for v in verse_ids if v not in fully_covered_ids]
    if not verse_ids:
        return ok(f"{cluster_code}: all {len(fully_covered_ids)} requested verse(s) are already "
                 f"fully covered (every expected question answered by an earlier pass) -- "
                 f"nothing to do. Use -Force to re-examine them anyway.",
                 preview=preview, cluster_code=cluster_code,
                 fully_covered_verse_count=len(fully_covered_ids))

    # #1723 front-loading multiplies expected output roughly by strong-density-per-batch, not just
    # verse count. FIXED verse-count chunking (the original #1723 fix, then #1825/#1826/#1827's
    # own halving) was the wrong lever -- checked live, 2026-09-21: M67's own 5-verse chunks range
    # from 6 to 21 distinct M-code strongs (a 3.5x spread), and which chunk actually truncated
    # varied run to run (not reliably the highest-density one), confirming a fixed verse cap can
    # never bound this reliably -- some batches are strong-dense, some aren't, and no single verse
    # count is safe for both without being wasteful for the sparse ones. Chunk by STRONG DENSITY
    # directly instead (`_chunk_verses_by_strong_density`) -- the actual cost driver, not a proxy.
    max_strongs = int(ctx.cfg.setting("lexical.meaning_max_strongs_per_batch", 8))
    max_cost_per_batch = float(ctx.cfg.setting("lexical.llm_max_cost_per_batch", 1.00))
    chunks = _chunk_verses_by_strong_density(conn, verse_ids, max_strongs)

    batch_summaries = []
    llm_summary = []
    record_summary = {"by_action": {}, "unresolved_occurrence_count": 0, "unresolved_detail": []}
    skipped_batches = 0

    for idx, chunk in enumerate(chunks):
        chunk_label = f"{idx + 1}/{len(chunks)}"
        package = versereadinggenerate.assemble_batch_package(ctx, cluster_code, chunk)
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

        # Resume/skip (escalation #1756): this exact batch (by content, not position) was already
        # committed by a PRIOR run -- never re-pay for it. Checked fresh per batch, not cached, so
        # a batch another concurrent/prior process just finished is picked up too. -Force (#1824
        # Fix 3) deliberately overrides this for an explicit reconciliation pass.
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
            # Crash safeguard (#1756): ANY uncaught exception in the risky window (API call
            # through record_batch's own commit) is recorded here before re-raising, so the
            # run_batch row never sits at 'running' forever for a genuinely handled failure --
            # only a real process death (kill, crash, power loss) leaves it there, which is
            # exactly the signal a resume needs to distinguish "dead run" from "not started yet".
            batchcontrol.fail_batch(conn, batch_id, f"{type(e).__name__}: {e}")
            raise
        batchcontrol.commit_batch(conn, batch_id, cost_usd=round(real_cost, 4))
        for action, n in chunk_record["by_action"].items():
            record_summary["by_action"][action] = record_summary["by_action"].get(action, 0) + n
        record_summary["unresolved_occurrence_count"] += chunk_record["unresolved_occurrence_count"]
        record_summary["unresolved_detail"] += chunk_record["unresolved_detail"]

    if preview:
        already_n = sum(1 for b in batch_summaries if b["already_committed"])
        # #1756: only the batches NOT already committed would actually cost anything on a live
        # run -- UNLESS -Force (#1824 Fix 3) is set, in which case every batch will actually be
        # re-called, so the estimate must include the already-committed ones too, not just the
        # remaining-work subset.
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

    # Every live (non-preview) call resolves the CLUSTER's full verse-id list (no partial/manual
    # selector exists on this step) -- so reaching here means the whole cluster was just attempted,
    # making this the right, and only, point to check verse-reading completeness and advance
    # cluster.status. Found live 2026-09-17 building this: the ordinal-2 -> ordinal-3
    # (ready_for_subgroup_allocation) transition #1697 designed was never actually built anywhere
    # -- every one of the 80 live clusters was still sitting at the one-time backfill state. See
    # lib/clusterstatus.py's own module docstring for the full finding.
    status_result = clusterstatus.advance_if_verse_reading_complete(conn, cluster_code)
    conn.commit()

    # LLM validation check (#1824 v14, researcher instruction 2026-09-22, verbatim: "stage 1 need
    # to pre-calculate the expected result for each scope, and measure the result received from
    # llm as the llm validation check"). Runs against the FULL requested verse_ids scope (not just
    # the batches that got a fresh call this time -- -Force-skipped-vs-not doesn't change what
    # SHOULD exist), read-only, no LLM call of its own. Full per-row detail persisted to a report
    # (governance.reports_must_persist); the summary counts are folded into this call's own
    # message text so they survive into `run.outcome` (the counts dict itself is not persisted --
    # same gap BUILD.md #274 already flagged for `unresolved_note` above).
    coverage = stage1coverage.validate_coverage(conn, cluster_code, verse_ids)
    # Config-defined path (escalation #1824 governance audit, 2026-09-22) -- was a hardcoded
    # f-string, which governance.reports_must_persist's own "config-defined report path"
    # requirement doesn't actually allow; report.stage1_coverage_validation_pattern registered to
    # match the established report.batch_progress_path/report.lexical_notes_output_pattern
    # precedent.
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
    # The reasons themselves, not just the count -- run.outcome only ever persists the message
    # STRING (checked live: the `counts` dict this Outcome also carries is never written to the
    # `run` table), so anything not folded into the message is lost the moment this process exits.
    # Found live 2026-09-17 needing to re-call a live API a second time, at real cost, just to see
    # why Stage 2's own observations had failed -- the exact gap BUILD.md #274 first flagged here.
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
