"""operations.py — the writer mechanism for the debate analytic process's core schema (BUILD.md
§61's `hib`/`hib_referent_option`/`verse_hib`/`phenomenon`/`operation`/`operation_party`), work
package `operations-ingest`. Full design record: `iba/app/reports/
b3-b5-operations-schema-design-20260805.md` (the two shapes named there; this is shape 1, a
registered write step) + `iba/app/reports/debate-analytic-process-digest-20260805.md` (Steps 1,
3-5, and "how this gets controlled").

**What this is, and isn't.** The analytical work — identifying a HIB, isolating a phenomenon,
writing an operation's process/source/target — is still done by an AI/researcher reading pass
against the method docs, exactly as every other analytical boundary in this app draws it (Claude
Code mechanical, Claude AI/researcher analytical). What THIS module mechanises is turning that
pass's *already-decided* findings into validated, grant-checked DB rows — a JSON payload file in,
structured rows out, same shape as the main Bible-study programme's own patch-application pattern
(`apply_session_patch.py`), adapted to this app's dispatcher/cfg_step architecture instead of a
side-script.

**Reconciliation-gated writes (2026-08-06, closing BUILD.md §61-63's own open gap).** The original
build of this module (§61-63) wrote every table with unconditional "clean re-derivation" —
soft-delete everything in the write's scope, blind-insert everything in the payload — identical to
`passage.build`'s own convention. That's the *correct* shape for `passage.build` (a passage is a
pure, deterministic derivation FROM `verse_hib` — recomputing it is re-deriving a materialized view
off already-adjudicated data, not re-deciding anything). It is the WRONG shape here: `hib`/
`phenomenon`/`operation` are themselves the adjudicated, interpretive record — re-running one of
these three steps against a book/passage that already has rows must not be able to silently discard
prior findings just because a fresh payload didn't happen to repeat them.

The researcher's own description of how Step 1 (and, by the same shape, Steps 3-5) actually works,
first run or re-run alike: **read the verses in scope; get every item per the definition; compare
that reading against what's already in the DB; validate the list against the DB; where the fresh
reading differs, adjudicate and correct the DB** — intelligent reconciliation, not blind
regeneration. `_reconcile()` below is the mechanical enforcement of exactly that, shared by all
three writers:

- Every incoming item is classified against the current live DB rows for the same scope, by a
  natural key (HIB: `label`; phenomenon: `verse` + `hib_label` + `ordinal`; operation: `verse` +
  `hib_label` + `phenomenon_ordinal`) — **unchanged** (identical content, left completely untouched,
  original row/id/created_at preserved), **changed** (same key, different content), or **new**.
- **Every pre-existing row not addressed by the incoming payload at all is a hard stop, not a
  silent drop.** The payload must either repeat it (unchanged or corrected) or name it explicitly
  in a `remove` list with a `reason`. This is the direct mechanical answer to "use the DB info to
  ensure the read isn't missing something" — the write refuses to proceed while any pre-existing
  item is unaccounted for, rather than trusting the payload to be exhaustive on faith.
- **Every `changed` item and every `remove` entry must carry a reconciliation note** (why the prior
  DB content was wrong, or why the item no longer belongs) — missing one fails the whole call
  (`unreconciled`) before any row is touched. `new`/`unchanged` items need no note — there's nothing
  to reconcile.
- Only once every existing row is accounted for and every change/removal is justified does the
  write proceed — `unchanged` rows are left alone, `new` rows are inserted, `changed` rows are
  soft-deleted-and-reinserted (their note kept in the reconciliation log below, not the row itself —
  none of the six tables carry a note column; adding one is future schema work, not required to
  close this gap), `removed` rows are soft-deleted only.
- **A reconciliation report is written on every call, changes or none** — filed book-scoped under
  `report.verse_analysis_output_dir/<book_label or book>/` (fixed 2026-08-08; previously
  `lib.reportkit.oneoff_path`, landing flat in `governance.oneoff_report_dir` — a real filing bug,
  not the intended design; see `_write_reconciliation_report`'s own docstring), versioned +
  archived-on-regenerate via `reportkit.write_report` — an auditable record of what was found
  unchanged, what was corrected and why, what was added, and what was removed and why, for every
  invocation, not only the ones with corrections.

**Three steps, one per digest stage, each fails cleanly (never partially writes) on any unresolved
reference OR any unreconciled item:**

- `hib.set` (scope book) — Step 1's HIB register: `hib` + `hib_referent_option` + `verse_hib`.
- `phenomenon.set` (scope book, needs -Chapters/-Range) — Step 3's phenomena register for one
  already-tracked passage. **Sets `passage.phenomena_complete_at`** once written, iff every
  `verse_hib` pair for the passage's verses now has a matching live `phenomenon` row (unchanged +
  new + corrected) — the mechanical half of the digest's "how does phase separation get controlled"
  question (the other half is `operation.set` refusing to run at all until this is set).
- `operation.set` (scope book, needs -Chapters/-Range) — Step 4-5's operations + parties. Refuses
  outright (`phenomena-incomplete`) if `passage.phenomena_complete_at` is still NULL.

Payload JSON shape for each step is documented on its own function below.
"""

from __future__ import annotations

import datetime
import json
import pathlib

from .base import Ctx, Outcome, ok, fail
from ..lib import passagetrack, reportkit
from ..lib.debateaudit import log_change as _log_change
from ..lib.versespanmeaningreport import parse_chapters, parse_range, fetch_verses


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _may(ctx: Ctx, writer: str, table: str) -> None:
    if table not in ctx.cfg.may_write(writer):
        raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")


def _resolve_range(ctx: Ctx):
    """Same one-of-Chapters/-Range shape every other book-scoped step uses; -Range/-Chapters
    exclusivity itself is validated by the PS wrapper, same convention as those other steps."""
    if ctx.params.get("Range"):
        ch, vlo, vhi = parse_range(ctx.params["Range"])
        return ch, ch, vlo, vhi
    lo, hi = parse_chapters(ctx.params["Chapters"])
    return lo, hi, None, None


class BadPayload(Exception):
    """PayloadPath missing/unreadable, not valid JSON, or missing a required key — always caught
    and turned into a clean fail(), never left to crash the run with a raw traceback."""


class ReconciliationError(Exception):
    """Raised by `_reconcile()` when the payload doesn't fully account for the DB's current state
    for this scope: a changed or removed item with no note, or a pre-existing item the payload
    neither repeats nor lists under `remove`. Carries the list of problems found; always caught and
    turned into a clean fail() — no row is ever touched while this is raised."""

    def __init__(self, problems: list[str]):
        self.problems = problems
        super().__init__(f"{len(problems)} item(s) need reconciliation")


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


def _verse_id(ctx: Ctx, osis: str) -> int | None:
    r = ctx.db.rows("SELECT id FROM verse WHERE osisId=? AND deleted=0", (osis,))
    return r[0]["id"] if r else None


def _find_new_model_passage(ctx: Ctx, book: str, lo: int, hi: int, vlo, vhi):
    """`phenomenon.set`/`operation.set` must only ever attach real analytical content to a
    `hib-continuity` (B4-era) passage row, never a legacy (`rule IS NULL`, pre-B4 char-continuity)
    one — even though `passagetrack.find_tracked_passage` itself resolves by range identity alone
    and doesn't distinguish the two (it's shared with `report.passage_debate`/`passage.debate_sync`,
    which legitimately still work against legacy rows for books not yet re-processed under
    HIB-continuity, so that shared function is deliberately left as-is, not narrowed here).

    Why this matters: `passage.build` reruns freely wipe any `rule IS NOT NULL` row with no linked
    content, but never touches a legacy row except on the one-time transition. If `phenomenon.set`
    were ever able to resolve a legacy row for an exact-matching range, real Step 3+ content could
    get attached to a row a later `passage.build` run has no reconciliation-awareness of at all
    (legacy rows aren't checked for linked phenomena the way `rule IS NOT NULL` rows are) — silently
    orphaning it. Returns `(row, problem)`: `row` is `None` and `problem` names the issue whenever
    nothing resolves, or only a legacy row does."""
    row = passagetrack.find_tracked_passage(ctx.db.conn, book, lo, hi, vlo, vhi)
    if row is None:
        return None, None
    if row["rule"] is None:
        return None, (f"passage {row['id']} ({row['ref']}) matches this range but is a legacy "
                      f"(pre-hib-continuity) row — run Build-Passages.ps1 -Book {book} first so "
                      f"this range gets a real hib-continuity passage to attach to")
    return row, None


class LexicalIncomplete(Exception):
    """Raised by `_check_lexical_complete` — always caught and turned into a clean
    `lexical-incomplete` fail(), never a partial write."""

    def __init__(self, missing: list[str]):
        self.missing = missing
        super().__init__(f"{len(missing)} verse(s) with no live verse_lexical row")


def _check_lexical_complete(ctx: Ctx, verse_ids: set[int], osis_by_id: dict[int, str]) -> None:
    """Digest Step 0, now a coded hard gate rather than an analyst-confirmed fact (2026-08-06,
    researcher direction: "step 1 of the debate pipeline is to validate that the book+chapter has a
    valid lexical... if lexicals are incomplete, hard stop"). Scoped to exactly the verses a
    `hib.set` payload references — not the whole book — since that's the actual scope the analyst
    is working (a book-wide sweep naturally covers a book-wide set of verse ids; a single-chapter
    pass covers just that chapter's).

    Deliberately verse-existence-agnostic: only checks verses that ARE live in `verse` (the caller
    already filtered `hib.set`'s payload down to resolvable verse ids before calling this) — a verse
    genuinely absent from the `verse` table is `governance.verse_gap_by_design` (2026-07-29 ruling:
    concordance-driven onboarding, not a data-integrity error) and is never a candidate here at all,
    exactly the researcher's "ignore missing verses in the verse table, it is intentional."

    "Deleted" filtering, both directions: only live (`deleted=0`) verse rows ever reach this
    function (via `_verse_id`), and only live (`deleted=0`) `verse_lexical` rows count toward
    coverage — a verse whose only lexical rows were soft-deleted (e.g. superseded by a re-run) reads
    as genuinely missing, not covered by stale rows."""
    if not verse_ids:
        return
    ph = ",".join("?" * len(verse_ids))
    covered = {r["verse_id"] for r in ctx.db.rows(
        f"SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND verse_id IN ({ph})",
        tuple(verse_ids))}
    missing_ids = verse_ids - covered
    if missing_ids:
        raise LexicalIncomplete(sorted(osis_by_id[vid] for vid in missing_ids))


class QualityCheckIncomplete(Exception):
    """Raised when a new/changed item's payload doesn't attest every REQUIRED, not-already-
    mechanically-enforced `cfg_quality_check` for this step. Always caught and turned into a clean
    `quality-check-incomplete` fail() — no row is ever written while this is raised."""

    def __init__(self, problems: list[str]):
        self.problems = problems
        super().__init__(f"{len(problems)} item(s) missing a required quality-check attestation")


def _required_quality_checks(ctx: Ctx, step: str) -> list[str]:
    """check_keys this step must get a real attestation for -- REQUIRED, ACTIVE, and NOT already
    mechanically enforced elsewhere (`enforced_by IS NULL`; a check like `hib.set/kind-enum-
    membership` is already fully automated by `_valid_hib_kinds` and asking for a redundant note
    on top of an already-automated check would just be noise, not real discipline)."""
    return [r["check_key"] for r in ctx.db.rows(
        "SELECT check_key FROM cfg_quality_check WHERE step=? AND required=1 AND active=1 "
        "AND enforced_by IS NULL ORDER BY ordinal", (step,))]


def _check_quality_attestations(items: dict, required: list[str]) -> None:
    """items: {key: raw payload item dict} for every NEW or CHANGED entry this call is about to
    write (unchanged/removed entries need no fresh attestation -- nothing new is being asserted
    about them). Each item must carry `quality_checks: {check_key: "<the analyst's own reasoning,
    non-empty>"}` covering every key in `required`. Researcher, 2026-08-06: "the controls should
    include self check quality control... does this make sense" -- this is that check, made
    mechanical: not a semantic judge (no code can verify "is this really a human being"), but a
    hard requirement that the judgement was actually made and written down, per item, every time,
    not silently skipped. Raises QualityCheckIncomplete (never partial) if anything's missing."""
    if not required:
        return
    problems = []
    for key, item in items.items():
        answered = item.get("quality_checks") or {}
        missing = [c for c in required if not (answered.get(c) or "").strip()]
        if missing:
            problems.append(f"{key!r} missing quality_checks attestation for: {missing}")
    if problems:
        raise QualityCheckIncomplete(problems)


# ── the reconciliation gate — shared by hib.set / phenomenon.set / operation.set ─────────────────
def _reconcile(current: dict, incoming: dict, removals: dict) -> tuple[list, list, list, list]:
    """current: {key: {"content": comparable-tuple, "id": int}} — the live DB state for this scope.
    incoming: {key: {"content": comparable-tuple, "note": str|None}} — the payload's own items,
        already keyed and content-normalised by the caller (content must be a hashable/`==`-able
        tuple — the caller decides what counts as "the same").
    removals: {key: reason} — the payload's explicit `remove` list, keyed the same way.

    Returns (unchanged_keys, changed_keys, new_keys, removed_keys). Raises ReconciliationError
    (never partially) if: a changed item has no note; a `remove` entry has no reason or names a key
    not currently live; or any current key is addressed by neither `incoming` nor `removals`."""
    problems = []
    unchanged, changed, new = [], [], []
    for k, inc in incoming.items():
        if k not in current:
            new.append(k)
        elif current[k]["content"] == inc["content"]:
            unchanged.append(k)
        else:
            if not inc.get("note"):
                problems.append(f"{k!r} differs from the DB but has no reconciliation_note")
            changed.append(k)

    for k, reason in removals.items():
        if k not in current:
            problems.append(f"'remove' names {k!r}, which is not currently live in the DB")
        elif not reason:
            problems.append(f"'remove' entry {k!r} has no reason")

    unaddressed = set(current) - set(incoming) - set(removals)
    for k in sorted(unaddressed, key=str):
        problems.append(f"{k!r} exists in the DB but this payload doesn't address it — repeat it "
                        f"(unchanged or corrected, with a reconciliation_note if corrected) or "
                        f"list it under 'remove' with a reason")

    if problems:
        raise ReconciliationError(problems)
    return unchanged, changed, new, list(removals.keys())


def _write_reconciliation_report(ctx: Ctx, step: str, scope_label: str, book: str,
                                 book_label: str | None,
                                 unchanged: list, changed: list, new: list, removed: list,
                                 notes: dict, quality_notes: dict | None = None) -> pathlib.Path:
    """Persist an auditable record of every reconciliation decision this call made — every call,
    not only ones with corrections.

    Filing corrected 2026-08-08 (found live: landing flat in `governance.oneoff_report_dir` instead
    of the book-scoped folder every sibling book tool uses). This is per-book analytical output, the
    same class as `lexical.build`/`report.verse_span_meaning`/the narrative — not a "one-off
    investigatory" report (that's what `reportkit.oneoff_path`/`build_verse_span_meaning_extract.py`
    are correctly for). Now files under `report.verse_analysis_output_dir/<book_label or book>/`,
    same inline convention `versespanmeaningreport.py`/`lexical.py`/`passagedebatereport.py`/
    `narrativegenerate.py`/`wholebookread.py` all already use — versioned + archived-on-regenerate
    via `reportkit.write_report` instead of a plain overwrite.

    `quality_notes` (2026-08-06): {key: {check_key: note}} for every new/changed item — the
    quality-check attestations `_check_quality_attestations` already required before this call was
    allowed to write anything. Recorded here so the judgement is auditable after the fact, not just
    gate-checked and discarded — researcher's own standard for reconciliation_note, extended to
    match."""
    lines = [
        f"# {step} reconciliation — {scope_label}", "",
        f"> Generated {_now()}. {len(unchanged)} unchanged, {len(changed)} corrected, "
        f"{len(new)} new, {len(removed)} removed.", "",
    ]
    def _qc_lines(k):
        qn = (quality_notes or {}).get(k) or {}
        return [f"  - quality check {ck!r}: {note}" for ck, note in qn.items()]
    if new:
        lines += ["## New", ""]
        for k in new:
            lines.append(f"- {k}")
            lines += _qc_lines(k)
        lines += [""]
    if changed:
        lines += ["## Corrected (DB had different content — reconciled)", ""]
        for k in changed:
            lines.append(f"- {k}: {notes.get(k, '(no note recorded)')}")
            lines += _qc_lines(k)
        lines += [""]
    if removed:
        lines += ["## Removed", ""]
        lines += [f"- {k}: {notes.get(k, '(no reason recorded)')}" for k in removed]
        lines += [""]
    if unchanged:
        lines += ["## Unchanged (confirmed against DB, left untouched)", ""]
        lines += [f"- {k}" for k in unchanged] + [""]
    output_dir = pathlib.Path(ctx.cfg.setting("report.verse_analysis_output_dir",
                                              "iba/app/verse-analysis"))
    folder = book_label or book
    path = output_dir / folder / f"{step}-reconciliation-{scope_label}.md"
    path = reportkit.write_report(ctx.cfg.conn, f"report.{step}-reconciliation", path, lines)
    return path


# ── hib.set ────────────────────────────────────────────────────────────────────────────────────
# payload: {"book": "Dan", "hibs": [
#   {"label": "Daniel", "kind": "named_individual", "verses": ["Dan.2.13", ...],  <- THIS CALL'S
#      OWN -Chapters/-Range SCOPE ONLY, never a book-wide reconstruction (revised 2026-08-08,
#      researcher direction: "the entire pipeline will only concern itself with the chapter"),
#    "referent_options": [{"reading_text": "...", "textual_grounds": "...", "adopted": true}, ...],
#      -- omit/empty unless THIS call is actually asserting a referent-crux reading; an absent or
#         empty list here never touches (and never wipes) whatever's already on record,
#    "reconciliation_note": "..."   -- required only if this label's SCOPE-VERSE content (or kind,
#                                      or an explicitly-provided referent_options) already differs
#                                      from what's on record for THIS scope; omit for a genuinely
#                                      new HIB or a same-content repeat,
#    "quality_checks": {...}},
#  ...],
#  "remove": [{"label": "...", "reason": "..."}]   -- optional. A label named here must already
#     have a live footprint IN THIS CALL'S OWN SCOPE — a HIB with no presence here (e.g.
#     Belshazzar, Dan 8, when running Dan 2) is never reachable from 'remove' on this call; run the
#     removal from a call scoped to where it actually appears. Removes the WHOLE HIB identity
#     (book-wide), not just this scope's claim on it — narrowing just this scope's verse-set is a
#     'changed' entry (a smaller `verses` list), not a removal.
#
# Matching against an existing HIB is book-wide BY LABEL (so "Daniel" extending from Dan 1 into
# Dan 2 resolves to the SAME row — CRUD, never a duplicate insert) — only the reconciliation
# completeness check ("every pre-existing item must be addressed or removed") and the verse_hib
# writes are scope-limited. See PLAN-revise-hib-set-scope-and-crud-v1-20260808.md for the full
# reasoning; this supersedes the whole-book-payload shape this docstring described until now.
def _verse_sort_key(osis: str) -> tuple[int, int]:
    """(chapter, verse) from an OSIS id, for canonical reading-order comparison. `verse.id` is a
    surrogate PK with NO relationship to reading order (confirmed live, Dan 2: ids scattered
    across the whole numeric range) — `first_verse_id` can never be computed by comparing raw ids,
    only by parsing the OSIS reference itself."""
    parts = osis.split(".")
    if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
        return (int(parts[1]), int(parts[2]))
    return (10**9, 10**9)


def _valid_enum(ctx: Ctx, name: str) -> set[str] | None:
    """`cfg_enum WHERE name=?` — returns None (skip the check) if the enum isn't registered/active
    yet (e.g. its `configmaint.propose` approval is still pending) — a not-yet-approved enum must
    never masquerade as "nothing is valid," it must simply not gate anything until it exists live.
    Shared by `hib.kind` (`hib_kind`, the six-type scheme from the researcher's own prior training
    pass, nahum-1-inner-being-training-20260803.md) and `operation.decision` (`operation_decision`,
    the four-value closed set WA-interpretation-questions-v1.4 Part C names)."""
    rows = ctx.db.rows("SELECT value FROM cfg_enum WHERE name=? AND inactive=0", (name,))
    return {r["value"] for r in rows} if rows else None


def _valid_hib_kinds(ctx: Ctx) -> set[str] | None:
    return _valid_enum(ctx, "hib_kind")


def _hib_content(kind, verses, referent_options):
    ro = tuple(sorted((o.get("reading_text", ""), o.get("textual_grounds") or "",
                       bool(o.get("adopted"))) for o in referent_options or []))
    return (kind, tuple(sorted(verses or [])), ro)


def hib_set(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    lo, hi, vlo, vhi = _resolve_range(ctx)
    scope_verses = fetch_verses(ctx.db.conn, book, lo, hi, vlo, vhi)
    scope_osis = {f"{book}.{v['chapter']}.{v['verse']}" for v in scope_verses}
    scope_token = ctx.params.get("Chapters") or ctx.params.get("Range") or ""

    try:
        payload = _load_payload(ctx)
        if payload.get("book") != book:
            return fail("payload-mismatch",
                       f"payload book {payload.get('book')!r} != -Book {book!r}")
        hibs = payload.get("hibs", [])
        removals_raw = payload.get("remove", [])
    except (BadPayload, KeyError) as e:
        return fail("bad-payload", str(e))
    if not hibs and not removals_raw:
        return fail("empty-payload", "payload has no 'hibs' or 'remove' entries")

    referenced_osis = {osis for h in hibs for osis in h.get("verses", [])}
    verse_id_by_osis = {osis: _verse_id(ctx, osis) for osis in referenced_osis}
    missing_verses = sorted(osis for osis, vid in verse_id_by_osis.items() if vid is None)
    if missing_verses:
        return fail("unknown-verse",
                    f"{len(missing_verses)} verse reference(s) not found in the verse table: "
                    f"{missing_verses[:5]}{' ...' if len(missing_verses) > 5 else ''}")

    # New 2026-08-08: a payload may only claim verses actually inside THIS call's own scope --
    # "the pipeline will only concern itself with the chapter," enforced, not just intended.
    out_of_scope = sorted(referenced_osis - scope_osis)
    if out_of_scope:
        return fail("out-of-scope-verse",
                    f"{len(out_of_scope)} verse(s) in the payload fall outside this call's own "
                    f"scope ({book} {scope_token}): "
                    f"{out_of_scope[:5]}{' ...' if len(out_of_scope) > 5 else ''}")

    # Step 0/1 hard gate (2026-08-06 direction): every verse this payload actually covers must
    # already have a complete lexical before any HIB work is accepted for it.
    live_verse_ids = {vid for vid in verse_id_by_osis.values() if vid is not None}
    osis_by_id = {vid: osis for osis, vid in verse_id_by_osis.items()}
    try:
        _check_lexical_complete(ctx, live_verse_ids, osis_by_id)
    except LexicalIncomplete as e:
        return fail("lexical-incomplete",
                    f"{len(e.missing)} verse(s) referenced in this payload have no live "
                    f"verse_lexical row — build the lexical first (VerseLexical.ps1): "
                    f"{e.missing[:5]}{' ...' if len(e.missing) > 5 else ''}")

    # Reasonability/existence check (researcher, 2026-08-06: "test for existence and
    # non-existence... the control rules must be defined in config") -- every hib.kind must be a
    # real, live value of enum.hib_kind, not free text. Skipped (not silently passed as "fine") if
    # the enum itself isn't active yet -- see _valid_hib_kinds.
    valid_kinds = _valid_hib_kinds(ctx)
    if valid_kinds is not None:
        bad_kinds = sorted({h["kind"] for h in hibs if h.get("kind") not in valid_kinds})
        if bad_kinds:
            return fail("invalid-kind",
                       f"{len(bad_kinds)} hib.kind value(s) not in enum.hib_kind "
                       f"{sorted(valid_kinds)}: {bad_kinds}")

    # Book-wide identity lookup (2026-08-08) -- separate from the scope-limited completeness check
    # below. Read-only, and book-wide only for identity-matching ("Daniel" extending from Dan 1
    # into Dan 2 must resolve to the SAME row) -- everything else in this call stays inside scope.
    all_by_label: dict[str, dict] = {}
    for r in ctx.db.rows(
            "SELECT id, label, kind, first_verse_id FROM hib WHERE book=? AND deleted=0", (book,)):
        verses = [v["osisId"] for v in ctx.db.rows(
            "SELECT v.osisId FROM verse_hib vh JOIN verse v ON v.id=vh.verse_id "
            "WHERE vh.hib_id=? AND vh.deleted=0", (r["id"],))]
        opts = [dict(o) for o in ctx.db.rows(
            "SELECT ordinal, reading_text, textual_grounds, adopted FROM hib_referent_option "
            "WHERE hib_id=? AND deleted=0 ORDER BY ordinal", (r["id"],))]
        all_by_label[r["label"]] = {"id": r["id"], "kind": r["kind"],
                                    "first_verse_id": r["first_verse_id"],
                                    "verses": verses, "opts": opts}

    incoming_by_label = {h["label"]: h for h in hibs}

    # `current` -- what `_reconcile` checks completeness against -- is scope-LIMITED (2026-08-08):
    # only a label with an EXISTING footprint in this call's own scope is included, so a book HIB
    # with no presence here (Belshazzar, Dan 8, when running Dan 2) is never pulled in and never
    # needs mentioning. Referent options only enter the comparison when the payload itself touches
    # them for this label -- an absent/empty list never wipes (or spuriously conflicts with)
    # whatever's already on record.
    current = {}
    for label, row in all_by_label.items():
        scope_verses_for_label = sorted(v for v in row["verses"] if v in scope_osis)
        if not scope_verses_for_label:
            continue
        h = incoming_by_label.get(label)
        touches_opts = bool(h and h.get("referent_options"))
        current[label] = {
            "content": _hib_content(row["kind"], scope_verses_for_label,
                                    row["opts"] if touches_opts else []),
            "id": row["id"]}

    incoming = {h["label"]: {"content": _hib_content(h["kind"], h.get("verses", []),
                                                      h.get("referent_options", [])),
                             "note": h.get("reconciliation_note"), "raw": h}
               for h in hibs}
    removals = {r["label"]: r.get("reason") for r in removals_raw}

    try:
        unchanged, changed, new, removed = _reconcile(current, incoming, removals)
    except ReconciliationError as e:
        return fail("unreconciled",
                    f"{len(e.problems)} item(s) need reconciliation before this can write: "
                    f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

    try:
        _check_quality_attestations(
            {l: incoming[l]["raw"] for l in (set(new) | set(changed))},
            _required_quality_checks(ctx, "hib.set"))
    except QualityCheckIncomplete as e:
        return fail("quality-check-incomplete",
                    f"{len(e.problems)} item(s), nothing written: "
                    f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

    # Cascade guard (2026-08-07, schema-remediation-design-20260807.md §4 -- Finding 3 of
    # debate-schema-traceability-gap-findings-20260807.md): a HIB removal must not silently orphan
    # already-written Step 3+ work. `removed` labels are, by construction, already restricted to
    # ones with a footprint in THIS scope (they came through `current`, which is scope-filtered) --
    # a book-wide-only removal (no presence here) is never reachable from this call. Refuse
    # OUTRIGHT (never partial) -- same "fail clean before any row is touched" convention as every
    # other check in this function.
    if removed:
        removed_ids = [current[l]["id"] for l in removed]
        ph = ",".join("?" * len(removed_ids))
        dependents = ctx.db.rows(
            f"SELECT h.label AS hib_label, COUNT(*) AS n FROM phenomenon ph "
            f"JOIN hib h ON h.id = ph.hib_id WHERE ph.hib_id IN ({ph}) AND ph.deleted=0 "
            f"GROUP BY h.label", removed_ids)
        if dependents:
            blocked = {r["hib_label"]: r["n"] for r in dependents}
            return fail("hib-has-dependent-phenomena",
                       f"{len(blocked)} HIB(s) in 'remove' still have live phenomenon rows -- "
                       f"remove those phenomena first (phenomenon.set 'remove'), or withdraw this "
                       f"HIB from 'remove': {blocked}")

    _may(ctx, "hib.set", "hib")
    _may(ctx, "hib.set", "hib_referent_option")
    _may(ctx, "hib.set", "verse_hib")
    _may(ctx, "hib.set", "debate_change_detail")

    now = _now()

    # `removed` -- full removal of the HIB entity, book-wide (soft-delete hib + all its children).
    # 'remove' means this identified HIB doesn't genuinely warrant HIB status at all (method rule
    # `hib-still-warranted`), not "retract just this chapter's claim" -- that narrower case is a
    # `changed` scope-verse shrink, handled in the CRUD loop below.
    for label in removed:
        hib_id = current[label]["id"]
        before_row = all_by_label[label]
        ctx.db.conn.execute("UPDATE hib_referent_option SET deleted=1 WHERE hib_id=?", (hib_id,))
        ctx.db.conn.execute("UPDATE verse_hib SET deleted=1 WHERE hib_id=?", (hib_id,))
        ctx.db.conn.execute("UPDATE hib SET deleted=1 WHERE id=?", (hib_id,))
        _log_change(ctx, "hib.set", "hib", "delete", {"id": hib_id},
                   before={"label": label, "kind": before_row["kind"], "book": book})

    n_opt = n_vh_ins = n_vh_del = 0
    for label in list(new) + list(changed):
        h = incoming_by_label[label]
        payload_verses = h.get("verses", [])
        existing = all_by_label.get(label)   # book-wide match, regardless of scope-only new/changed

        if existing:
            # EXTEND an existing book-wide HIB -- real CRUD, never a duplicate insert. Real
            # first_verse_id recompute: canonical-earliest of (existing verses UNION this call's),
            # never the payload's own array order (that convention only ever made sense when a
            # payload was a whole-set replacement, which it no longer is).
            hib_id = existing["id"]
            all_verses_osis = sorted(set(existing["verses"]) | set(payload_verses))
            new_first_osis = min(all_verses_osis, key=_verse_sort_key)
            new_first_id = _verse_id(ctx, new_first_osis)
            kind_changed = h["kind"] != existing["kind"]
            first_verse_changed = new_first_id != existing["first_verse_id"]
            if kind_changed or first_verse_changed:
                before = {"kind": existing["kind"], "first_verse_id": existing["first_verse_id"]}
                ctx.db.conn.execute("UPDATE hib SET kind=?, first_verse_id=? WHERE id=?",
                                   (h["kind"], new_first_id, hib_id))
                _log_change(ctx, "hib.set", "hib", "update", {"id": hib_id},
                           set_={"kind": h["kind"], "first_verse_id": new_first_id}, before=before)
        else:
            # Genuinely new HIB, never seen anywhere in the book before.
            first_osis = min(payload_verses, key=_verse_sort_key)
            first_id = _verse_id(ctx, first_osis)
            hib_id = ctx.db.write("hib", {
                "book": book, "label": label, "kind": h["kind"],
                "first_verse_id": first_id, "created_at": now, "deleted": 0})
            _log_change(ctx, "hib.set", "hib", "insert", {"id": hib_id},
                       set_={"book": book, "label": label, "kind": h["kind"],
                             "first_verse_id": first_id})

        # referent_options -- only touched if THIS call's payload actually provides them for this
        # label; an absent/empty list never wipes what's already on record (2026-08-08). Real
        # per-row CRUD by ordinal position (same upgrade as operation_party, researcher direction:
        # "full CRUD is required for all table update controls") -- only a position whose content
        # actually differs is touched, not a blanket soft-delete-and-reinsert of every option.
        if h.get("referent_options"):
            prior_by_ord = {o["ordinal"]: o for o in (existing or {}).get("opts") or []}
            new_opts = h["referent_options"]
            span = max(len(new_opts), len(prior_by_ord) and max(prior_by_ord) + 1 or 0)
            for i in range(span):
                new_opt = new_opts[i] if i < len(new_opts) else None
                old_opt = prior_by_ord.get(i)
                if new_opt is None and old_opt is not None:
                    ctx.db.conn.execute(
                        "UPDATE hib_referent_option SET deleted=1 WHERE hib_id=? AND ordinal=?",
                        (hib_id, i))
                    _log_change(ctx, "hib.set", "hib_referent_option", "delete",
                               {"hib_id": hib_id, "ordinal": i}, before=dict(old_opt))
                    n_opt += 1
                    continue
                new_row = {"hib_id": hib_id, "reading_text": new_opt["reading_text"],
                          "textual_grounds": new_opt.get("textual_grounds"),
                          "adopted": 1 if new_opt.get("adopted") else 0, "ordinal": i,
                          "created_at": now, "deleted": 0}
                if old_opt is not None:
                    same = (old_opt.get("reading_text") == new_row["reading_text"]
                            and (old_opt.get("textual_grounds") or None) ==
                                (new_row["textual_grounds"] or None)
                            and bool(old_opt.get("adopted")) == bool(new_row["adopted"]))
                    if not same:
                        ctx.db.conn.execute(
                            "UPDATE hib_referent_option SET reading_text=?, textual_grounds=?, "
                            "adopted=? WHERE hib_id=? AND ordinal=?",
                            (new_row["reading_text"], new_row["textual_grounds"],
                             new_row["adopted"], hib_id, i))
                        _log_change(ctx, "hib.set", "hib_referent_option", "update",
                                   {"hib_id": hib_id, "ordinal": i}, set_=new_row,
                                   before=dict(old_opt))
                else:
                    ctx.db.write("hib_referent_option", new_row)
                    _log_change(ctx, "hib.set", "hib_referent_option", "insert",
                               {"hib_id": hib_id, "ordinal": i}, set_=new_row)
                n_opt += 1
                n_opt += 1

        # verse_hib -- real per-row CRUD (2026-08-08): insert only links not already live, delete
        # only links this scope's payload genuinely drops. Never touches a verse_hib row outside
        # this call's own scope, for ANY label, extended or brand new.
        existing_links_in_scope = {v for v in (existing["verses"] if existing else []) if v in scope_osis}
        payload_links = set(payload_verses)
        for osis in payload_links - existing_links_in_scope:
            vid = _verse_id(ctx, osis)
            ctx.db.write("verse_hib", {"verse_id": vid, "hib_id": hib_id, "created_at": now, "deleted": 0})
            _log_change(ctx, "hib.set", "verse_hib", "insert", {"verse_id": vid, "hib_id": hib_id},
                       set_={"verse_id": vid, "hib_id": hib_id})
            n_vh_ins += 1
        for osis in existing_links_in_scope - payload_links:
            vid = _verse_id(ctx, osis)
            ctx.db.conn.execute(
                "UPDATE verse_hib SET deleted=1 WHERE verse_id=? AND hib_id=? AND deleted=0",
                (vid, hib_id))
            _log_change(ctx, "hib.set", "verse_hib", "delete", {"verse_id": vid, "hib_id": hib_id},
                       before={"verse_id": vid, "hib_id": hib_id})
            n_vh_del += 1

    ctx.db.conn.commit()
    notes = {l: incoming[l]["note"] for l in changed} | {l: removals[l] for l in removed}
    quality_notes = {l: incoming[l]["raw"].get("quality_checks", {}) for l in (set(new) | set(changed))}
    scope_label = f"{book}-{scope_token}" if scope_token else book
    report_path = _write_reconciliation_report(ctx, "hib.set", scope_label, book, book_label,
                                               unchanged, changed, new, removed, notes, quality_notes)

    # Output by type (researcher, 2026-08-06: "count by type; list by type") -- the book's FULL
    # live state after this call, unaffected by the scope change above (this report always
    # reflected the whole book, by design, not just what one call touched).
    by_kind: dict[str, list[str]] = {}
    for r in ctx.db.rows("SELECT label, kind FROM hib WHERE book=? AND deleted=0 ORDER BY kind, label",
                         (book,)):
        by_kind.setdefault(r["kind"], []).append(r["label"])
    kind_lines = [f"# hib.set — {book} — live HIBs by type", "",
                 f"> Generated {_now()}. Reflects the book's full live state after this call, not "
                 f"just this call's own changes.", ""]
    for kind in sorted(by_kind):
        kind_lines.append(f"## {kind} ({len(by_kind[kind])})")
        kind_lines.append("")
        kind_lines += [f"- {label}" for label in by_kind[kind]]
        kind_lines.append("")
    kind_output_dir = pathlib.Path(ctx.cfg.setting("report.verse_analysis_output_dir",
                                                    "iba/app/verse-analysis"))
    kind_path = kind_output_dir / (book_label or book) / f"hib.set-by-type-{book}.md"
    kind_path = reportkit.write_report(ctx.cfg.conn, "report.hib.set-by-type", kind_path, kind_lines)

    counts_by_kind = {k: len(v) for k, v in by_kind.items()}
    return ok(f"{book} {scope_token}: {len(unchanged)} unchanged, {len(new)} new, {len(changed)} "
              f"corrected, {len(removed)} removed HIB(s) in this scope; {n_opt} referent option(s), "
              f"{n_vh_ins} verse-HIB link(s) added, {n_vh_del} removed this call; by type "
              f"(book-wide): {counts_by_kind}; reconciliation log: {report_path}; "
              f"by-type log: {kind_path}",
             unchanged=len(unchanged), new=len(new), changed=len(changed), removed=len(removed),
             referent_options=n_opt, verse_hib_added=n_vh_ins, verse_hib_removed=n_vh_del,
             **counts_by_kind)


# ── phenomenon.set ─────────────────────────────────────────────────────────────────────────────
# payload: {"book": "Dan", "phenomena": [
#   {"verse": "Dan.8.1", "hib_label": "Daniel", "description": "...", "textual_warrant": "...",
#    "status": "stated"|"inferred"|"silent", "ordinal": 0, "reconciliation_note": "..."}
#  ...],
#  "remove": [{"verse": "...", "hib_label": "...", "ordinal": 0, "reason": "..."}]}
def _phenomenon_content(description, textual_warrant, status):
    return (description, textual_warrant or "", status)


def phenomenon_set(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    lo, hi, vlo, vhi = _resolve_range(ctx)
    try:
        payload = _load_payload(ctx)
        phenomena = payload.get("phenomena", [])
        removals_raw = payload.get("remove", [])
    except (BadPayload, KeyError) as e:
        return fail("bad-payload", str(e))
    if not phenomena and not removals_raw:
        return fail("empty-payload", "payload has no 'phenomena' or 'remove' entries")

    passage_row, problem = _find_new_model_passage(ctx, book, lo, hi, vlo, vhi)
    if problem:
        return fail("legacy-passage", problem)
    if not passage_row:
        return fail("no-passage", f"no tracked hib-continuity passage for {book} this range — run "
                                  f"Build-Passages.ps1 (passage.build) first")
    passage_id = passage_row["id"]

    hib_by_label = {r["label"]: r["id"] for r in ctx.db.rows(
        "SELECT id, label FROM hib WHERE book=? AND deleted=0", (book,))}

    problems, resolved = [], []   # resolved: (key, verse_id, hib_id, ordinal, item-dict-or-None)
    for p in phenomena:
        vid = _verse_id(ctx, p["verse"])
        hid = hib_by_label.get(p["hib_label"])
        if vid is None:
            problems.append(f"unknown verse {p['verse']!r}")
        elif hid is None:
            problems.append(f"unknown HIB label {p['hib_label']!r} for {book} (run hib.set first)")
        else:
            key = (p["verse"], p["hib_label"], p.get("ordinal", 0))
            resolved.append((key, vid, hid, p.get("ordinal", 0), p))
    removals = {}
    for r in removals_raw:
        vid = _verse_id(ctx, r["verse"])
        hid = hib_by_label.get(r["hib_label"])
        if vid is None:
            problems.append(f"'remove' names unknown verse {r['verse']!r}")
        elif hid is None:
            problems.append(f"'remove' names unknown HIB label {r['hib_label']!r}")
        else:
            removals[(r["verse"], r["hib_label"], r.get("ordinal", 0))] = r.get("reason")
    if problems:
        return fail("unresolved-reference",
                    f"{len(problems)} problem(s): {problems[:5]}{' ...' if len(problems) > 5 else ''}")

    current_rows = ctx.db.rows(
        "SELECT ph.id, v.osisId, h.label, ph.ordinal, ph.description, ph.textual_warrant, "
        "ph.status FROM phenomenon ph JOIN verse v ON v.id=ph.verse_id "
        "JOIN hib h ON h.id=ph.hib_id WHERE ph.passage_id=? AND ph.deleted=0", (passage_id,))
    current = {(r["osisId"], r["label"], r["ordinal"]):
              {"content": _phenomenon_content(r["description"], r["textual_warrant"], r["status"]),
               "id": r["id"]} for r in current_rows}

    incoming = {key: {"content": _phenomenon_content(p["description"], p.get("textual_warrant"),
                                                      p["status"]),
                      "note": p.get("reconciliation_note")}
               for key, vid, hid, ordv, p in resolved}
    by_key = {key: (vid, hid, ordv, p) for key, vid, hid, ordv, p in resolved}

    try:
        unchanged, changed, new, removed = _reconcile(current, incoming, removals)
    except ReconciliationError as e:
        return fail("unreconciled",
                    f"{len(e.problems)} item(s) need reconciliation before this can write: "
                    f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

    try:
        _check_quality_attestations(
            {k: by_key[k][3] for k in (set(new) | set(changed))},
            _required_quality_checks(ctx, "phenomenon.set"))
    except QualityCheckIncomplete as e:
        return fail("quality-check-incomplete",
                    f"{len(e.problems)} item(s), nothing written: "
                    f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

    # Cascade guard (2026-08-07, same rule as hib.set, item h -- "not just for hib"): a phenomenon
    # removal must not silently orphan an already-written operation.
    if removed:
        removed_ids = [current[k]["id"] for k in removed]
        ph = ",".join("?" * len(removed_ids))
        dependents = ctx.db.rows(
            f"SELECT phenomenon_id, COUNT(*) AS n FROM operation "
            f"WHERE phenomenon_id IN ({ph}) AND deleted=0 GROUP BY phenomenon_id", removed_ids)
        if dependents:
            return fail("phenomenon-has-dependent-operations",
                       f"{len(dependents)} phenomenon/a in 'remove' still have live operation "
                       f"rows -- remove those operations first (operation.set 'remove'), or "
                       f"withdraw the phenomenon from 'remove'")

    _may(ctx, "phenomenon.set", "phenomenon")
    _may(ctx, "phenomenon.set", "passage")   # phase-gate write (phenomena_complete_at), below
    _may(ctx, "phenomenon.set", "debate_change_detail")

    now = _now()
    # `changed` phenomena UPDATE the existing row IN PLACE (same id), not soft-delete-and-reinsert
    # -- a new id would silently orphan any `operation.phenomenon_id` already pointing at it (same
    # fix as hib.set; passage.py's own established precedent). `removed` still soft-deletes (the
    # guard above already confirmed no live operation depends on it). Per-row audit logging added
    # 2026-08-07 -- the underlying CRUD here was already correct, only the trace was missing.
    for key in removed:
        row_id = current[key]["id"]
        ctx.db.conn.execute("UPDATE phenomenon SET deleted=1 WHERE id=?", (row_id,))
        _log_change(ctx, "phenomenon.set", "phenomenon", "delete", {"id": row_id},
                   before={"content": current[key]["content"]})

    for key in list(new) + list(changed):
        vid, hid, ordv, p = by_key[key]
        if key in changed:
            row_id = current[key]["id"]
            new_vals = {"description": p["description"], "textual_warrant": p.get("textual_warrant"),
                       "status": p["status"]}
            ctx.db.conn.execute(
                "UPDATE phenomenon SET description=?, textual_warrant=?, status=? WHERE id=?",
                (new_vals["description"], new_vals["textual_warrant"], new_vals["status"], row_id))
            _log_change(ctx, "phenomenon.set", "phenomenon", "update", {"id": row_id},
                       set_=new_vals, before={"content": current[key]["content"]})
        else:
            row = {"passage_id": passage_id, "verse_id": vid, "hib_id": hid,
                  "description": p["description"], "textual_warrant": p.get("textual_warrant"),
                  "status": p["status"], "ordinal": ordv, "created_at": now, "deleted": 0}
            new_id = ctx.db.write("phenomenon", row)
            _log_change(ctx, "phenomenon.set", "phenomenon", "insert", {"id": new_id}, set_=row)

    # completeness check -- every verse_hib pair for this passage's verses must now have a LIVE
    # phenomenon (unchanged + new + corrected; removed items drop back out of the live set).
    verse_ids = [r["verse_id"] for r in ctx.db.rows(
        "SELECT verse_id FROM verse_passage WHERE passage_id=? AND deleted=0", (passage_id,))]
    vh_pairs = set()
    if verse_ids:
        ph = ",".join("?" * len(verse_ids))
        vh_pairs = {(r["verse_id"], r["hib_id"]) for r in ctx.db.rows(
            f"SELECT verse_id, hib_id FROM verse_hib WHERE deleted=0 AND verse_id IN ({ph})",
            verse_ids)}
    live_keys = set(unchanged) | set(new) | set(changed)
    live_pairs = set()
    for key in live_keys:
        if key in by_key:
            vid, hid, _, _ = by_key[key]
        else:
            # unchanged item not resent in this call's payload isn't possible under this design
            # (unchanged still means "present in incoming, matched current") -- kept defensive.
            continue
        live_pairs.add((vid, hid))
    missing = vh_pairs - live_pairs
    if missing:
        # Explicitly re-open the gate, not just "leave it as whatever it was" -- a legitimate
        # removal/correction can make a previously-complete register incomplete again, and
        # operation.set must re-block in that case, not keep trusting a stale phenomena_complete_at
        # from before this call. (Bug in the original §61-63 build: it only ever set the gate
        # forward, never cleared it -- caught and fixed in this same reconciliation pass.)
        ctx.db.conn.execute("UPDATE passage SET phenomena_complete_at=NULL WHERE id=?", (passage_id,))
        _log_change(ctx, "phenomenon.set", "passage", "update", {"id": passage_id},
                   set_={"phenomena_complete_at": None},
                   before={"phenomena_complete_at": passage_row["phenomena_complete_at"]})
        gate_msg = f"phase gate NOT set -- {len(missing)} verse/HIB pair(s) still missing a phenomenon"
    else:
        ctx.db.conn.execute("UPDATE passage SET phenomena_complete_at=? WHERE id=?", (now, passage_id))
        _log_change(ctx, "phenomenon.set", "passage", "update", {"id": passage_id},
                   set_={"phenomena_complete_at": now},
                   before={"phenomena_complete_at": passage_row["phenomena_complete_at"]})
        gate_msg = "phase gate SET -- phenomena register is complete for this passage"

    ctx.db.conn.commit()
    notes = {k: incoming[k]["note"] for k in changed} | {k: removals[k] for k in removed}
    quality_notes = {k: by_key[k][3].get("quality_checks", {}) for k in (set(new) | set(changed))}
    scope_label = f"{book}-{passage_id}"
    report_path = _write_reconciliation_report(ctx, "phenomenon.set", scope_label, book, book_label,
                                               unchanged, changed, new, removed, notes, quality_notes)
    return ok(f"{book} passage {passage_id}: {len(unchanged)} unchanged, {len(new)} new, "
              f"{len(changed)} corrected, {len(removed)} removed phenomenon/phenomena; {gate_msg}; "
              f"reconciliation log: {report_path}",
             unchanged=len(unchanged), new=len(new), changed=len(changed), removed=len(removed),
             gate_set=not missing, missing_pairs=len(missing))


# ── operation.set ──────────────────────────────────────────────────────────────────────────────
# payload: {"book": "Dan", "operations": [
#   {"verse": "Dan.8.1", "hib_label": "Daniel", "phenomenon_ordinal": 0,
#    "process": "...", "action_type": "...", "decision": "retain"|"set_aside"|
#    "retain_referential"|"recorded_silence", "observation_text": "...", "description_text": "...",
#    "sources": [{"kind": "self"|"human"|"non_human"|"object_situation"|"none", "detail": "...",
#                 "hib_label": "..."|omit, "enablement_only": false}],
#    "targets": [{"kind": "...", "detail": "...", "hib_label": "..."|omit}], "reconciliation_note": "..."}
#  ...],
# `hib_label` (2026-08-07, Finding 2 of debate-schema-traceability-gap-findings-20260807.md):
# optional, only when this party genuinely IS a previously-registered HIB (via hib.set) -- resolved
# to `operation_party.hib_id`, a real structural link, not just the `detail` free-text gloss. Must
# name a live HIB for this book or the call fails (unresolved-reference); omit entirely for a party
# that isn't itself a registered HIB (kind='self'/'non_human'/'object_situation'/'none', or a human
# not (yet) worth registering as its own HIB).
#  "remove": [{"verse": "...", "hib_label": "...", "phenomenon_ordinal": 0, "reason": "..."}]}
def _operation_content(o: dict) -> tuple:
    """`p["hib_id"]` must already be resolved (an int or None) on every party dict passed in here
    -- callers building FROM the DB already have it; callers building from a fresh payload resolve
    `hib_label` to `hib_id` via `hib_by_label` before calling (Finding 2, debate-schema-
    traceability-gap-findings-20260807.md -- the party's HIB link is part of the operation's real
    content now, not just `detail` free text, so a hib_label change must register as a 'changed'
    item like anything else)."""
    parties = lambda lst: tuple(sorted(
        ((p["kind"], p.get("detail") or "", bool(p.get("enablement_only")), p.get("hib_id"))
         for p in lst or []),
        key=lambda t: (t[0], t[1], t[2], -1 if t[3] is None else t[3])))
    return (o.get("process"), o.get("action_type"), o.get("decision"),
           o.get("observation_text"), o.get("description_text"),
           parties(o.get("sources")), parties(o.get("targets")))


def operation_set(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    lo, hi, vlo, vhi = _resolve_range(ctx)
    try:
        payload = _load_payload(ctx)
        operations = payload.get("operations", [])
        removals_raw = payload.get("remove", [])
    except (BadPayload, KeyError) as e:
        return fail("bad-payload", str(e))
    if not operations and not removals_raw:
        return fail("empty-payload", "payload has no 'operations' or 'remove' entries")

    passage_row, problem = _find_new_model_passage(ctx, book, lo, hi, vlo, vhi)
    if problem:
        return fail("legacy-passage", problem)
    if not passage_row:
        return fail("no-passage", f"no tracked hib-continuity passage for {book} this range")
    if not passage_row["phenomena_complete_at"]:
        return fail("phenomena-incomplete",
                    f"passage {passage_row['id']}'s phenomena register is not complete yet "
                    f"(passage.phenomena_complete_at is NULL) -- run phenomenon.set to close the "
                    f"whole register for this passage first (debate digest Step 3's phase gate)")
    passage_id = passage_row["id"]

    hib_by_label = {r["label"]: r["id"] for r in ctx.db.rows(
        "SELECT id, label FROM hib WHERE book=? AND deleted=0", (book,))}

    def _find_phenomenon(verse, hib_label, ordinal):
        vid = _verse_id(ctx, verse)
        hid = hib_by_label.get(hib_label)
        if vid is None or hid is None:
            return None, vid, hid
        rows = ctx.db.rows(
            "SELECT id FROM phenomenon WHERE passage_id=? AND verse_id=? AND hib_id=? "
            "AND ordinal=? AND deleted=0", (passage_id, vid, hid, ordinal))
        return (rows[0]["id"] if rows else None), vid, hid

    problems, by_key = [], {}
    for o in operations:
        phen_id, vid, hid = _find_phenomenon(o["verse"], o["hib_label"], o.get("phenomenon_ordinal", 0))
        if vid is None:
            problems.append(f"unknown verse {o['verse']!r}")
        elif hid is None:
            problems.append(f"unknown HIB label {o['hib_label']!r}")
        elif not phen_id:
            problems.append(f"no registered phenomenon for {o['verse']!r}/{o['hib_label']!r} "
                            f"ordinal {o.get('phenomenon_ordinal', 0)}")
        else:
            key = (o["verse"], o["hib_label"], o.get("phenomenon_ordinal", 0))
            by_key[key] = (phen_id, o)
    removals = {}
    for r in removals_raw:
        phen_id, vid, hid = _find_phenomenon(r["verse"], r["hib_label"], r.get("phenomenon_ordinal", 0))
        if vid is None:
            problems.append(f"'remove' names unknown verse {r['verse']!r}")
        elif hid is None:
            problems.append(f"'remove' names unknown HIB label {r['hib_label']!r}")
        elif not phen_id:
            problems.append(f"'remove' names a phenomenon that doesn't exist: {r['verse']!r}/"
                            f"{r['hib_label']!r} ordinal {r.get('phenomenon_ordinal', 0)}")
        else:
            removals[(r["verse"], r["hib_label"], r.get("phenomenon_ordinal", 0))] = r.get("reason")

    # Party hib_label resolution (2026-08-07, Finding 2 of debate-schema-traceability-gap-findings-
    # 20260807.md): an optional `hib_label` on a source/target party -- when the party IS a
    # previously-registered HIB, this is what actually links `operation_party.hib_id` structurally,
    # instead of the free-text `detail` field being the only record of it. Same fail-fast convention
    # as every other reference in this payload: an unresolvable hib_label is a hard stop, not a
    # silently-dropped link.
    for o in operations:
        for party in list(o.get("sources", [])) + list(o.get("targets", [])):
            label = party.get("hib_label")
            if label and label not in hib_by_label:
                problems.append(f"unknown HIB label {label!r} on a party of {o['verse']!r}/"
                                f"{o['hib_label']!r}")
    if problems:
        return fail("unresolved-reference",
                    f"{len(problems)} problem(s): {problems[:5]}{' ...' if len(problems) > 5 else ''}")

    # existence check (2026-08-06): decision is a genuinely closed 4-value set (WA-interpretation-
    # questions-v1.4 Part C) -- action_type deliberately is NOT enum-checked (Part B.10: "no
    # controlled vocabulary is being built"), so only decision gets this treatment.
    valid_decisions = _valid_enum(ctx, "operation_decision")
    if valid_decisions is not None:
        bad = sorted({o.get("decision") for _, o in by_key.values()
                     if o.get("decision") not in valid_decisions})
        if bad:
            return fail("invalid-decision",
                       f"{len(bad)} operation.decision value(s) not in enum.operation_decision "
                       f"{sorted(valid_decisions)}: {bad}")

    current_rows = ctx.db.rows(
        "SELECT op.id, v.osisId, h.label, ph.ordinal AS phenomenon_ordinal, op.process, "
        "op.action_type, op.decision, op.observation_text, op.description_text, op.id AS op_id "
        "FROM operation op JOIN phenomenon ph ON ph.id = op.phenomenon_id "
        "JOIN verse v ON v.id = ph.verse_id JOIN hib h ON h.id = ph.hib_id "
        "WHERE ph.passage_id=? AND op.deleted=0", (passage_id,))
    current = {}
    for r in current_rows:
        parties = [dict(p) for p in ctx.db.rows(
            "SELECT role, kind, detail, enablement_only, hib_id FROM operation_party "
            "WHERE operation_id=? AND deleted=0", (r["op_id"],))]
        sources = [p for p in parties if p["role"] == "source"]
        targets = [p for p in parties if p["role"] == "target"]
        content = _operation_content({"process": r["process"], "action_type": r["action_type"],
                                      "decision": r["decision"],
                                      "observation_text": r["observation_text"],
                                      "description_text": r["description_text"],
                                      "sources": sources, "targets": targets})
        current[(r["osisId"], r["label"], r["phenomenon_ordinal"])] = {"content": content, "id": r["id"]}

    def _with_hib_ids(o: dict) -> dict:
        """Shallow copy of `o` with `hib_id` resolved onto every source/target party from its
        `hib_label` (already validated resolvable, above) -- so content comparison and the eventual
        write both see the real link, not just the free-text `detail`."""
        out = dict(o)
        for role in ("sources", "targets"):
            out[role] = [dict(p, hib_id=hib_by_label.get(p["hib_label"]) if p.get("hib_label")
                              else None) for p in o.get(role, [])]
        return out

    by_key = {key: (phen_id, _with_hib_ids(o)) for key, (phen_id, o) in by_key.items()}
    incoming = {key: {"content": _operation_content(o), "note": o.get("reconciliation_note")}
               for key, (phen_id, o) in by_key.items()}

    try:
        unchanged, changed, new, removed = _reconcile(current, incoming, removals)
    except ReconciliationError as e:
        return fail("unreconciled",
                    f"{len(e.problems)} item(s) need reconciliation before this can write: "
                    f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

    try:
        _check_quality_attestations(
            {k: by_key[k][1] for k in (set(new) | set(changed))},
            _required_quality_checks(ctx, "operation.set"))
    except QualityCheckIncomplete as e:
        return fail("quality-check-incomplete",
                    f"{len(e.problems)} item(s), nothing written: "
                    f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

    # Cascade guard (2026-08-07, same rule as hib.set/phenomenon.set): an operation removal must
    # not silently orphan an already-written passage_linkage (Step 7 can name any operation as
    # either endpoint of a linkage).
    if removed:
        removed_ids = [current[k]["id"] for k in removed]
        ph = ",".join("?" * len(removed_ids))
        dependents = ctx.db.rows(
            f"SELECT id FROM passage_linkage WHERE deleted=0 AND "
            f"(from_operation_id IN ({ph}) OR to_operation_id IN ({ph}))",
            removed_ids + removed_ids)
        if dependents:
            return fail("operation-has-dependent-linkage",
                       f"{len(dependents)} passage_linkage row(s) still reference an operation in "
                       f"'remove' -- remove those linkages first (closing.set 'remove'), or "
                       f"withdraw the operation from 'remove'")

    _may(ctx, "operation.set", "operation")
    _may(ctx, "operation.set", "operation_party")
    _may(ctx, "operation.set", "debate_change_detail")

    now = _now()
    # `changed` operations UPDATE the existing row IN PLACE (same id) -- a new id would silently
    # orphan any `passage_linkage.from/to_operation_id` already pointing at it. `operation_party`
    # children: real per-row CRUD by (role, ordinal) position (2026-08-08, researcher direction --
    # "full CRUD is required for all table update controls", upgraded from the previously-approved
    # soft-delete-and-reinsert-under-a-changed-parent convention, tech ref sec2.2 step 7) -- only a
    # position whose content actually differs is touched; a `removed` operation's parties are still
    # fully soft-deleted (the whole operation is gone, nothing to diff against).
    for key in removed:
        op_id = current[key]["id"]
        live = ctx.db.rows(
            "SELECT id, role, ordinal, kind, detail, enablement_only, hib_id FROM operation_party "
            "WHERE operation_id=? AND deleted=0", (op_id,))
        for p in live:
            ctx.db.conn.execute("UPDATE operation_party SET deleted=1 WHERE id=?", (p["id"],))
            _log_change(ctx, "operation.set", "operation_party", "delete", {"id": p["id"]},
                       before=dict(p))
        ctx.db.conn.execute("UPDATE operation SET deleted=1 WHERE id=?", (op_id,))
        _log_change(ctx, "operation.set", "operation", "delete", {"id": op_id},
                   before={"content": current[key]["content"]})

    n_party = 0
    for key in list(new) + list(changed):
        phen_id, o = by_key[key]
        if key in changed:
            op_id = current[key]["id"]
            new_vals = {"process": o.get("process"), "action_type": o.get("action_type"),
                       "decision": o.get("decision"), "observation_text": o.get("observation_text"),
                       "description_text": o.get("description_text")}
            ctx.db.conn.execute(
                "UPDATE operation SET process=?, action_type=?, decision=?, observation_text=?, "
                "description_text=? WHERE id=?",
                (new_vals["process"], new_vals["action_type"], new_vals["decision"],
                 new_vals["observation_text"], new_vals["description_text"], op_id))
            _log_change(ctx, "operation.set", "operation", "update", {"id": op_id},
                       set_=new_vals, before={"content": current[key]["content"]})
        else:
            row = {"phenomenon_id": phen_id, "process": o.get("process"),
                  "action_type": o.get("action_type"), "decision": o.get("decision"),
                  "observation_text": o.get("observation_text"),
                  "description_text": o.get("description_text"),
                  "created_at": now, "deleted": 0}
            op_id = ctx.db.write("operation", row)
            _log_change(ctx, "operation.set", "operation", "insert", {"id": op_id}, set_=row)

        for role, parties in (("source", o.get("sources", [])), ("target", o.get("targets", []))):
            existing_by_ord = {}
            if key in changed:
                existing_by_ord = {p["ordinal"]: p for p in ctx.db.rows(
                    "SELECT id, ordinal, kind, detail, enablement_only, hib_id FROM operation_party "
                    "WHERE operation_id=? AND role=? AND deleted=0", (op_id, role))}
            span = max(len(parties), len(existing_by_ord) and max(existing_by_ord) + 1 or 0)
            for i in range(span):
                new_party = parties[i] if i < len(parties) else None
                old_party = existing_by_ord.get(i)
                if new_party is None and old_party is not None:
                    ctx.db.conn.execute(
                        "UPDATE operation_party SET deleted=1 WHERE id=?", (old_party["id"],))
                    _log_change(ctx, "operation.set", "operation_party", "delete",
                               {"id": old_party["id"]}, before=dict(old_party))
                    n_party += 1
                    continue
                new_row = {"operation_id": op_id, "role": role, "kind": new_party["kind"],
                          "detail": new_party.get("detail"), "hib_id": new_party.get("hib_id"),
                          "enablement_only": 1 if new_party.get("enablement_only") else 0,
                          "ordinal": i, "created_at": now, "deleted": 0}
                if old_party is not None:
                    same = (old_party["kind"] == new_row["kind"]
                            and (old_party["detail"] or None) == (new_row["detail"] or None)
                            and old_party["enablement_only"] == new_row["enablement_only"]
                            and old_party["hib_id"] == new_row["hib_id"])
                    if not same:
                        ctx.db.conn.execute(
                            "UPDATE operation_party SET kind=?, detail=?, enablement_only=?, "
                            "hib_id=? WHERE id=?",
                            (new_row["kind"], new_row["detail"], new_row["enablement_only"],
                             new_row["hib_id"], old_party["id"]))
                        _log_change(ctx, "operation.set", "operation_party", "update",
                                   {"id": old_party["id"]}, set_=new_row, before=dict(old_party))
                        n_party += 1
                    # same -- genuinely nothing to do, no write, no log, no count (this is the
                    # actual point of real CRUD: an untouched position stays untouched).
                else:
                    party_id = ctx.db.write("operation_party", new_row)
                    _log_change(ctx, "operation.set", "operation_party", "insert",
                               {"id": party_id}, set_=new_row)
                    n_party += 1

    ctx.db.conn.commit()
    notes = {k: incoming[k]["note"] for k in changed} | {k: removals[k] for k in removed}
    quality_notes = {k: by_key[k][1].get("quality_checks", {}) for k in (set(new) | set(changed))}
    scope_label = f"{book}-{passage_id}"
    report_path = _write_reconciliation_report(ctx, "operation.set", scope_label, book, book_label,
                                               unchanged, changed, new, removed, notes, quality_notes)
    return ok(f"{book} passage {passage_id}: {len(unchanged)} unchanged, {len(new)} new, "
              f"{len(changed)} corrected, {len(removed)} removed operation(s), {n_party} party "
              f"record(s) written this call; reconciliation log: {report_path}",
             unchanged=len(unchanged), new=len(new), changed=len(changed), removed=len(removed),
             parties=n_party)


# ── closing.set ────────────────────────────────────────────────────────────────────────────────
# Step 7 (digest) / WA-interpretation-questions-v1.4 Part C sections 4-8, for one already-tracked
# hib-continuity passage. Refuses (`operations-incomplete`) until every live phenomenon in the
# passage has at least one live operation — computed live each call (design doc: "no other counters
# are stored... always computed live from verse_hib/phenomenon/operation"), the same DB-as-control
# principle as the phenomena_complete_at gate, just not itself a stored column (nothing downstream
# needs it as a gate the way operation.set needs phenomena_complete_at — this is the pipeline's
# final content-writing step, so a live check at the point of use is enough).
#
# payload: {"book": "Dan",
#   "linkages": [{"from_verse":"Dan.8.1","from_hib_label":"Daniel","from_phenomenon_ordinal":0,
#                 "to_verse":"Dan.8.15","to_hib_label":"Daniel","to_phenomenon_ordinal":0,
#                 "note":"...", "ordinal":0, "reconciliation_note":"..."}],
#   "insufficiencies": [{"verse":"Dan.8.1"|null, "note":"...", "ordinal":0,
#                        "reconciliation_note":"..."}],
#   "emergent_questions": [{"verse":"Dan.8.1"|null, "question_text":"...",
#                           "kind":"interpretive_fork"|"literary_structural"|"other", "ordinal":0,
#                           "reconciliation_note":"..."}],
#   "validation_notes": [{"phenomenon_verse":"Dan.8.1"|null, "phenomenon_hib_label":"Daniel"|null,
#                         "phenomenon_ordinal":0, "finding_text":"...", "corrected":true,
#                         "ordinal":0, "reconciliation_note":"..."}],
#   "open_decisions_note": "..." (optional; a single evolving summary field, no reconciliation --
#                                  always just set to this call's current text),
#   "remove": {"linkages":[{"ordinal":0,"reason":"..."}], "insufficiencies":[...],
#              "emergent_questions":[...], "validation_notes":[...]}}
def _find_phenomenon_id(ctx: Ctx, passage_id: int, verse: str | None, hib_label: str | None,
                        ordinal: int) -> tuple[int | None, str | None]:
    if verse is None or hib_label is None:
        return None, None
    vid = _verse_id(ctx, verse)
    if vid is None:
        return None, f"unknown verse {verse!r}"
    rows = ctx.db.rows(
        "SELECT ph.id FROM phenomenon ph JOIN hib h ON h.id=ph.hib_id "
        "WHERE ph.passage_id=? AND ph.verse_id=? AND h.label=? AND ph.ordinal=? AND ph.deleted=0",
        (passage_id, vid, hib_label, ordinal))
    if not rows:
        return None, f"no registered phenomenon for {verse!r}/{hib_label!r} ordinal {ordinal}"
    return rows[0]["id"], None


def _find_operation_id(ctx: Ctx, passage_id: int, verse: str, hib_label: str,
                       ordinal: int) -> tuple[int | None, str | None]:
    phen_id, problem = _find_phenomenon_id(ctx, passage_id, verse, hib_label, ordinal)
    if problem:
        return None, problem
    rows = ctx.db.rows("SELECT id FROM operation WHERE phenomenon_id=? AND deleted=0", (phen_id,))
    if not rows:
        return None, (f"no registered operation for {verse!r}/{hib_label!r} ordinal {ordinal} "
                      f"(phenomenon exists, but operation.set hasn't run for it yet)")
    return rows[0]["id"], None


def closing_set(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    book_label = ctx.params.get("BookLabel")
    lo, hi, vlo, vhi = _resolve_range(ctx)
    try:
        payload = _load_payload(ctx)
    except BadPayload as e:
        return fail("bad-payload", str(e))

    passage_row, problem = _find_new_model_passage(ctx, book, lo, hi, vlo, vhi)
    if problem:
        return fail("legacy-passage", problem)
    if not passage_row:
        return fail("no-passage", f"no tracked hib-continuity passage for {book} this range")
    passage_id = passage_row["id"]

    # Operations-completeness, computed live -- every live phenomenon in this passage must have a
    # live operation (digest Step 4: "every phenomenon needs an operation, even if the decision is
    # 'set aside'") before Step 7 closing sections are written against it.
    phen_ids = {r["id"] for r in ctx.db.rows(
        "SELECT id FROM phenomenon WHERE passage_id=? AND deleted=0", (passage_id,))}
    op_phen_ids = {r["phenomenon_id"] for r in ctx.db.rows(
        "SELECT phenomenon_id FROM operation WHERE deleted=0 AND phenomenon_id IN "
        f"({','.join('?' * len(phen_ids))})", tuple(phen_ids))} if phen_ids else set()
    missing_ops = phen_ids - op_phen_ids
    if missing_ops:
        return fail("operations-incomplete",
                    f"passage {passage_id}: {len(missing_ops)} phenomenon/phenomena still have no "
                    f"operation -- run operation.set to cover all of them before Step 7")

    _may(ctx, "closing.set", "passage_linkage")
    _may(ctx, "closing.set", "passage_insufficiency")
    _may(ctx, "closing.set", "passage_emergent_question")
    _may(ctx, "closing.set", "passage_validation_note")
    _may(ctx, "closing.set", "debate_change_detail")

    now = _now()
    problems: list[str] = []
    # Each entry: (list_name, table, current, incoming, resolved_raw, reconciled) -- reconciled but
    # NOT yet written. 2026-08-07: quality-check attestations must be verified BEFORE any row is
    # written (the same boundary hib.set/phenomenon.set/operation.set already draw) -- previously
    # this function wrote each section immediately after reconciling it. Restructured to reconcile
    # all four sections first, check quality attestations once against the combined new+changed
    # set, and only then write anything.
    plan: list[tuple[str, str, dict, dict, dict, tuple]] = []

    # -- linkages --
    current = {r["ordinal"]: {"content": (r["from_id"], r["to_id"], r["note"]), "id": r["id"]}
              for r in ctx.db.rows(
        "SELECT id, ordinal, from_operation_id AS from_id, to_operation_id AS to_id, note "
        "FROM passage_linkage WHERE passage_id=? AND deleted=0", (passage_id,))}
    incoming, resolved_raw = {}, {}
    for item in payload.get("linkages", []):
        from_id, p1 = _find_operation_id(ctx, passage_id, item["from_verse"], item["from_hib_label"],
                                         item.get("from_phenomenon_ordinal", 0))
        to_id, p2 = _find_operation_id(ctx, passage_id, item["to_verse"], item["to_hib_label"],
                                       item.get("to_phenomenon_ordinal", 0))
        if p1: problems.append(f"linkage ordinal {item.get('ordinal', 0)}: {p1}")
        if p2: problems.append(f"linkage ordinal {item.get('ordinal', 0)}: {p2}")
        if not (p1 or p2):
            ordv = item.get("ordinal", 0)
            incoming[ordv] = {"content": (from_id, to_id, item["note"]),
                              "note": item.get("reconciliation_note"), "raw": item}
            resolved_raw[ordv] = (from_id, to_id, item["note"])
    removals = {r["ordinal"]: r.get("reason") for r in payload.get("remove", {}).get("linkages", [])}
    if not problems:
        try:
            reconciled = _reconcile(current, incoming, removals)
        except ReconciliationError as e:
            problems += [f"linkages: {p}" for p in e.problems]
        else:
            plan.append(("linkages", "passage_linkage", current, incoming, resolved_raw, reconciled))

    if problems:
        return fail("unresolved-reference",
                    f"{len(problems)} problem(s), nothing written: "
                    f"{problems[:5]}{' ...' if len(problems) > 5 else ''}")

    # -- insufficiencies --
    current = {r["ordinal"]: {"content": (r["verse"], r["note"]), "id": r["id"]} for r in ctx.db.rows(
        "SELECT pi.id, pi.ordinal, v.osisId AS verse, pi.note FROM passage_insufficiency pi "
        "LEFT JOIN verse v ON v.id=pi.verse_id WHERE pi.passage_id=? AND pi.deleted=0", (passage_id,))}
    incoming, resolved_raw = {}, {}
    for item in payload.get("insufficiencies", []):
        verse = item.get("verse")
        vid = _verse_id(ctx, verse) if verse else None
        if verse and vid is None:
            problems.append(f"insufficiency ordinal {item.get('ordinal', 0)}: unknown verse {verse!r}")
            continue
        ordv = item.get("ordinal", 0)
        incoming[ordv] = {"content": (verse, item["note"]), "note": item.get("reconciliation_note"),
                          "raw": item}
        resolved_raw[ordv] = (vid, item["note"])
    removals = {r["ordinal"]: r.get("reason") for r in payload.get("remove", {}).get("insufficiencies", [])}
    if not problems:
        try:
            reconciled = _reconcile(current, incoming, removals)
        except ReconciliationError as e:
            problems += [f"insufficiencies: {p}" for p in e.problems]
        else:
            plan.append(("insufficiencies", "passage_insufficiency", current, incoming, resolved_raw,
                        reconciled))

    if problems:
        return fail("unresolved-reference",
                    f"{len(problems)} problem(s), nothing written: "
                    f"{problems[:5]}{' ...' if len(problems) > 5 else ''}")

    # -- emergent questions --
    current = {r["ordinal"]: {"content": (r["verse"], r["question_text"], r["kind"]), "id": r["id"]}
              for r in ctx.db.rows(
        "SELECT peq.id, peq.ordinal, v.osisId AS verse, peq.question_text, peq.kind "
        "FROM passage_emergent_question peq LEFT JOIN verse v ON v.id=peq.verse_id "
        "WHERE peq.passage_id=? AND peq.deleted=0", (passage_id,))}
    incoming, resolved_raw = {}, {}
    for item in payload.get("emergent_questions", []):
        verse = item.get("verse")
        vid = _verse_id(ctx, verse) if verse else None
        if verse and vid is None:
            problems.append(f"emergent_question ordinal {item.get('ordinal', 0)}: unknown verse {verse!r}")
            continue
        ordv = item.get("ordinal", 0)
        incoming[ordv] = {"content": (verse, item["question_text"], item["kind"]),
                          "note": item.get("reconciliation_note"), "raw": item}
        resolved_raw[ordv] = (vid, item["question_text"], item["kind"])
    removals = {r["ordinal"]: r.get("reason") for r in payload.get("remove", {}).get("emergent_questions", [])}
    if not problems:
        try:
            reconciled = _reconcile(current, incoming, removals)
        except ReconciliationError as e:
            problems += [f"emergent_questions: {p}" for p in e.problems]
        else:
            plan.append(("emergent_questions", "passage_emergent_question", current, incoming,
                        resolved_raw, reconciled))

    if problems:
        return fail("unresolved-reference",
                    f"{len(problems)} problem(s), nothing written: "
                    f"{problems[:5]}{' ...' if len(problems) > 5 else ''}")

    # -- validation notes --
    current = {r["ordinal"]: {"content": (r["phen_id"], r["finding_text"], r["corrected"]), "id": r["id"]}
              for r in ctx.db.rows(
        "SELECT id, ordinal, phenomenon_id AS phen_id, finding_text, corrected "
        "FROM passage_validation_note WHERE passage_id=? AND deleted=0", (passage_id,))}
    incoming, resolved_raw = {}, {}
    for item in payload.get("validation_notes", []):
        phen_id, p = _find_phenomenon_id(ctx, passage_id, item.get("phenomenon_verse"),
                                         item.get("phenomenon_hib_label"),
                                         item.get("phenomenon_ordinal", 0))
        if p and item.get("phenomenon_verse"):
            problems.append(f"validation_note ordinal {item.get('ordinal', 0)}: {p}")
            continue
        ordv = item.get("ordinal", 0)
        corrected = 1 if item.get("corrected") else 0
        incoming[ordv] = {"content": (phen_id, item["finding_text"], corrected),
                          "note": item.get("reconciliation_note"), "raw": item}
        resolved_raw[ordv] = (phen_id, item["finding_text"], corrected)
    removals = {r["ordinal"]: r.get("reason") for r in payload.get("remove", {}).get("validation_notes", [])}
    if not problems:
        try:
            reconciled = _reconcile(current, incoming, removals)
        except ReconciliationError as e:
            problems += [f"validation_notes: {p}" for p in e.problems]
        else:
            plan.append(("validation_notes", "passage_validation_note", current, incoming,
                        resolved_raw, reconciled))

    if problems:
        return fail("unresolved-reference",
                    f"{len(problems)} problem(s), nothing written: "
                    f"{problems[:5]}{' ...' if len(problems) > 5 else ''}")

    # Quality-check attestations -- BEFORE any row is written (same boundary hib.set/
    # phenomenon.set/operation.set draw). closing.set is the first step with FOUR heterogeneous
    # item types under one step name -- `_required_quality_checks(ctx, "closing.set")` returns
    # every required check_key across ALL of them, which would wrongly demand a linkage's own
    # attestation on an emergent_question (found live, 2026-08-07, before this ever shipped: an
    # emergent_question was asked to attest `linkage-genuinely-registered`). Filtered per list_name
    # by its own check_key naming convention -- checked once per section, not once combined.
    LIST_QUALITY_PREFIX = {
        "linkages": "linkage-", "insufficiencies": "insufficiency-",
        "emergent_questions": "emergent-question-", "validation_notes": "validation-finding-",
    }
    all_required = _required_quality_checks(ctx, "closing.set")
    for list_name, _table, _current, incoming, _resolved_raw, (unchanged, changed, new, removed) in plan:
        prefix = LIST_QUALITY_PREFIX[list_name]
        required = [c for c in all_required if c.startswith(prefix)]
        qc_items = {f"{list_name}:{key}": incoming[key]["raw"] for key in list(new) + list(changed)}
        try:
            _check_quality_attestations(qc_items, required)
        except QualityCheckIncomplete as e:
            return fail("quality-check-incomplete",
                        f"{len(e.problems)} item(s), nothing written: "
                        f"{e.problems[:5]}{' ...' if len(e.problems) > 5 else ''}")

    # Now write every section for real. Real per-row CRUD (2026-08-08, researcher direction --
    # "full CRUD is required for all table update controls"): `changed` items UPDATE the existing
    # row IN PLACE (same id), `new` items INSERT fresh, `removed` items soft-delete only -- was:
    # soft-delete-and-reinsert-under-a-new-id for BOTH changed and new, the same antipattern
    # hib.set/phenomenon.set/operation.set already had fixed for their own parent rows. None of
    # these four tables currently has a downstream FK pointing at its own id, so the old shape
    # never orphaned anything structurally -- but a stable id across a correction is still the more
    # traceable, auditable shape, and the researcher's direction was unqualified.
    ROW_COLUMNS = {
        "passage_linkage": ("from_operation_id", "to_operation_id", "note"),
        "passage_insufficiency": ("verse_id", "note"),
        "passage_emergent_question": ("verse_id", "question_text", "kind"),
        "passage_validation_note": ("phenomenon_id", "finding_text", "corrected"),
    }
    all_summary: dict[str, tuple] = {}
    for list_name, table, current, incoming, resolved_raw, (unchanged, changed, new, removed) in plan:
        cols = ROW_COLUMNS[table]
        for ordv in removed:
            row_id = current[ordv]["id"]
            ctx.db.conn.execute(f"UPDATE {table} SET deleted=1 WHERE id=?", (row_id,))
            _log_change(ctx, "closing.set", table, "delete", {"id": row_id},
                       before={"content": current[ordv]["content"]})
        for ordv in changed:
            row_id = current[ordv]["id"]
            vals = resolved_raw[ordv]
            set_clause = ", ".join(f"{c}=?" for c in cols)
            ctx.db.conn.execute(f"UPDATE {table} SET {set_clause} WHERE id=?", (*vals, row_id))
            _log_change(ctx, "closing.set", table, "update", {"id": row_id},
                       set_=dict(zip(cols, vals)), before={"content": current[ordv]["content"]})
        for ordv in new:
            vals = resolved_raw[ordv]
            row = {"passage_id": passage_id, **dict(zip(cols, vals)),
                  "ordinal": ordv, "created_at": now, "deleted": 0}
            new_id = ctx.db.write(table, row)
            _log_change(ctx, "closing.set", table, "insert", {"id": new_id}, set_=row)
        all_summary[list_name] = (unchanged, changed, new, removed)

    if "open_decisions_note" in payload:
        _may(ctx, "closing.set", "passage")
        before_note = passage_row["open_decisions_note"]
        ctx.db.conn.execute("UPDATE passage SET open_decisions_note=? WHERE id=?",
                            (payload["open_decisions_note"], passage_id))
        _log_change(ctx, "closing.set", "passage", "update", {"id": passage_id},
                   set_={"open_decisions_note": payload["open_decisions_note"]},
                   before={"open_decisions_note": before_note})

    ctx.db.conn.commit()
    counts = {k: {"unchanged": len(u), "changed": len(c), "new": len(n), "removed": len(r)}
             for k, (u, c, n, r) in all_summary.items()}
    scope_label = f"{book}-{passage_id}"
    lines = [f"# closing.set reconciliation — {scope_label}", "",
            f"> Generated {_now()}.", ""]
    for k, c in counts.items():
        lines.append(f"- **{k}**: {c['unchanged']} unchanged, {c['new']} new, {c['changed']} "
                     f"corrected, {c['removed']} removed")
    if "open_decisions_note" in payload:
        lines.append("- **open_decisions_note**: updated")
    closing_output_dir = pathlib.Path(ctx.cfg.setting("report.verse_analysis_output_dir",
                                                       "iba/app/verse-analysis"))
    path = closing_output_dir / (book_label or book) / f"closing.set-reconciliation-{scope_label}.md"
    path = reportkit.write_report(ctx.cfg.conn, "report.closing.set-reconciliation", path, lines)

    return ok(f"{book} passage {passage_id}: closing sections written — "
              + "; ".join(f"{k}: {v}" for k, v in counts.items())
              + f"; reconciliation log: {path}", **counts)
