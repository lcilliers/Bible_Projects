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

import json
import pathlib

from .base import Ctx, Outcome, fail, ok
from . import raw as raw_mod
from ..lib import lexical, lexicalenrich, lexicalenrichgenerate, lexicalscope
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

    totals = lexical.build_for_range(ctx.db.conn, book, lo, hi, verse_lo, verse_hi, step)
    ctx.db.conn.commit()

    removed_note = (f", {totals['removed_with_live_notes']} with live notes now dangling — "
                    f"see report.lexical_exceptions" if totals["removed_with_live_notes"] else "")
    return ok(
        f"{book} {lo}-{hi}: {totals['verses']} verse(s), {totals['spans']} span(s), "
        f"{totals['codes']} code(s) resolved ({totals['inserted']} inserted, "
        f"{totals['updated']} updated, {totals['unchanged']} unchanged, "
        f"{totals['removed']} removed{removed_note}){backfill_note}",
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
    ph = ",".join("?" * len(verse_ids))
    code_rows = ctx.db.rows(
        f"SELECT vl.id AS verse_lexical_id, v.osisId AS verse, vl.position, vl.code_ordinal, "
        f"vl.strong, vl.role, vl.status, vl.morph_code, vl.resolved_sense, vl.ambiguity_note, "
        f"vl.surface, vl.language, vl.testament, vl.is_negator, vl.narrative_morph, "
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
        required = ctx.cfg.setting("step.required_for_runs", True)
        step: Step | None = None
        try:
            Step(ctx.cfg).up()
            step = Step(ctx.cfg)
        except StepUnavailable as e:
            if required:
                return fail("unreachable", str(e))
        build_totals = lexical.build_for_verse_ids(conn, verse_ids, step)
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
