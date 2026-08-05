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

**Three steps, one per digest stage, each fails cleanly (never partially writes) on any unresolved
reference:**

- `hib.set` (scope book) — Step 1's HIB register: `hib` + `hib_referent_option` + `verse_hib`.
  Clean re-derivation per book (soft-delete existing, insert fresh) — same convention
  `passage.build` already uses for `passage`.
- `phenomenon.set` (scope book, needs -Chapters/-Range) — Step 3's phenomena register for one
  already-tracked passage. Clean re-derivation per passage. **Sets `passage.phenomena_complete_at`
  itself**, once written, if-and-only-if every `verse_hib` pair for the passage's verses now has a
  matching `phenomenon` row — the actual mechanical half of the digest's "how does phase separation
  get controlled" question (the other half, below, is `operation.set` refusing to run at all until
  this is set).
- `operation.set` (scope book, needs -Chapters/-Range) — Step 4-5's operations + parties.
  **Refuses outright (`phenomena-incomplete`) if `passage.phenomena_complete_at` is still NULL** —
  this is the literal code enforcement of `WA-interpretation-questions` Part B.12 / the digest's
  Step 3 gate, not a documented convention someone has to remember to follow.

Payload JSON shape for each step is documented on its own function below.
"""

from __future__ import annotations

import datetime
import json
import pathlib

from .base import Ctx, Outcome, ok, fail
from ..lib import passagetrack
from ..lib.versespanmeaningreport import parse_chapters, parse_range


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


# ── hib.set ────────────────────────────────────────────────────────────────────────────────────
# payload: {"book": "Dan", "hibs": [
#   {"label": "Daniel", "kind": "named"|"collective"|"referential", "verses": ["Dan.8.1", ...],
#    "referent_options": [{"reading_text": "...", "textual_grounds": "...", "adopted": true}, ...]}
# ]}
def hib_set(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    try:
        payload = _load_payload(ctx)
        if payload.get("book") != book:
            return fail("payload-mismatch",
                       f"payload book {payload.get('book')!r} != -Book {book!r}")
        hibs = payload["hibs"]
    except (BadPayload, KeyError) as e:
        return fail("bad-payload", str(e))
    if not hibs:
        return fail("empty-payload", "payload has no 'hibs' entries")

    missing_verses = sorted({osis for h in hibs for osis in h.get("verses", [])
                             if _verse_id(ctx, osis) is None})
    if missing_verses:
        return fail("unknown-verse",
                    f"{len(missing_verses)} verse reference(s) not found in the verse table: "
                    f"{missing_verses[:5]}{' ...' if len(missing_verses) > 5 else ''}")

    _may(ctx, "hib.set", "hib")
    _may(ctx, "hib.set", "hib_referent_option")
    _may(ctx, "hib.set", "verse_hib")

    # clean re-derivation: soft-delete this book's existing hib/hib_referent_option/verse_hib,
    # then insert fresh -- same convention passage.build already uses for `passage`.
    existing = [r["id"] for r in ctx.db.rows("SELECT id FROM hib WHERE book=? AND deleted=0", (book,))]
    if existing:
        ph = ",".join("?" * len(existing))
        ctx.db.conn.execute(f"UPDATE hib_referent_option SET deleted=1 WHERE hib_id IN ({ph})", existing)
        ctx.db.conn.execute(f"UPDATE verse_hib SET deleted=1 WHERE hib_id IN ({ph})", existing)
        ctx.db.conn.execute(f"UPDATE hib SET deleted=1 WHERE id IN ({ph})", existing)

    now = _now()
    n_hib = n_opt = n_vh = 0
    for h in hibs:
        verses = h.get("verses", [])
        first_verse_id = _verse_id(ctx, verses[0]) if verses else None
        hib_id = ctx.db.write("hib", {
            "book": book, "label": h["label"], "kind": h["kind"],
            "first_verse_id": first_verse_id, "created_at": now, "deleted": 0})
        n_hib += 1
        for i, opt in enumerate(h.get("referent_options", [])):
            ctx.db.write("hib_referent_option", {
                "hib_id": hib_id, "reading_text": opt["reading_text"],
                "textual_grounds": opt.get("textual_grounds"),
                "adopted": 1 if opt.get("adopted") else 0, "ordinal": i,
                "created_at": now, "deleted": 0})
            n_opt += 1
        for osis in verses:
            ctx.db.write("verse_hib", {
                "verse_id": _verse_id(ctx, osis), "hib_id": hib_id,
                "created_at": now, "deleted": 0})
            n_vh += 1

    ctx.db.conn.commit()
    return ok(f"{book}: {n_hib} HIB(s), {n_opt} referent option(s), {n_vh} verse-HIB link(s) written",
             hibs=n_hib, referent_options=n_opt, verse_hib=n_vh)


# ── phenomenon.set ─────────────────────────────────────────────────────────────────────────────
# payload: {"book": "Dan", "phenomena": [
#   {"verse": "Dan.8.1", "hib_label": "Daniel", "description": "...", "textual_warrant": "...",
#    "status": "stated"|"inferred"|"silent", "ordinal": 0}
# ]}
def phenomenon_set(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    lo, hi, vlo, vhi = _resolve_range(ctx)
    try:
        payload = _load_payload(ctx)
        phenomena = payload["phenomena"]
    except (BadPayload, KeyError) as e:
        return fail("bad-payload", str(e))
    if not phenomena:
        return fail("empty-payload", "payload has no 'phenomena' entries")

    passage_row = passagetrack.find_tracked_passage(ctx.db.conn, book, lo, hi, vlo, vhi)
    if not passage_row:
        return fail("no-passage", f"no tracked passage for {book} this range — run "
                                  f"Build-Passages.ps1 (passage.build) first")
    passage_id = passage_row["id"]

    hib_by_label = {r["label"]: r["id"] for r in ctx.db.rows(
        "SELECT id, label FROM hib WHERE book=? AND deleted=0", (book,))}
    problems, resolved = [], []
    for p in phenomena:
        vid = _verse_id(ctx, p["verse"])
        hid = hib_by_label.get(p["hib_label"])
        if vid is None:
            problems.append(f"unknown verse {p['verse']!r}")
        elif hid is None:
            problems.append(f"unknown HIB label {p['hib_label']!r} for {book} (run hib.set first)")
        else:
            resolved.append((vid, hid, p))
    if problems:
        return fail("unresolved-reference",
                    f"{len(problems)} problem(s): {problems[:5]}{' ...' if len(problems) > 5 else ''}")

    _may(ctx, "phenomenon.set", "phenomenon")
    _may(ctx, "phenomenon.set", "passage")   # phase-gate write (phenomena_complete_at), below

    existing = [r["id"] for r in ctx.db.rows(
        "SELECT id FROM phenomenon WHERE passage_id=? AND deleted=0", (passage_id,))]
    if existing:
        ph = ",".join("?" * len(existing))
        ctx.db.conn.execute(f"UPDATE phenomenon SET deleted=1 WHERE id IN ({ph})", existing)

    now = _now()
    for vid, hid, p in resolved:
        ctx.db.write("phenomenon", {
            "passage_id": passage_id, "verse_id": vid, "hib_id": hid,
            "description": p["description"], "textual_warrant": p.get("textual_warrant"),
            "status": p["status"], "ordinal": p.get("ordinal", 0),
            "created_at": now, "deleted": 0})

    # completeness check -- the control-total comparison the digest's "how this gets controlled"
    # note describes: every verse_hib pair for this passage's verses must now have a phenomenon.
    verse_ids = [r["verse_id"] for r in ctx.db.rows(
        "SELECT verse_id FROM verse_passage WHERE passage_id=? AND deleted=0", (passage_id,))]
    vh_pairs = set()
    if verse_ids:
        ph = ",".join("?" * len(verse_ids))
        vh_pairs = {(r["verse_id"], r["hib_id"]) for r in ctx.db.rows(
            f"SELECT verse_id, hib_id FROM verse_hib WHERE deleted=0 AND verse_id IN ({ph})",
            verse_ids)}
    ph_pairs = {(vid, hid) for vid, hid, _ in resolved}
    missing = vh_pairs - ph_pairs
    if missing:
        gate_msg = f"phase gate NOT set -- {len(missing)} verse/HIB pair(s) still missing a phenomenon"
    else:
        ctx.db.conn.execute("UPDATE passage SET phenomena_complete_at=? WHERE id=?", (now, passage_id))
        gate_msg = "phase gate SET -- phenomena register is complete for this passage"

    ctx.db.conn.commit()
    return ok(f"{book} passage {passage_id}: {len(resolved)} phenomenon/phenomena written; {gate_msg}",
             phenomena=len(resolved), gate_set=not missing, missing_pairs=len(missing))


# ── operation.set ──────────────────────────────────────────────────────────────────────────────
# payload: {"book": "Dan", "operations": [
#   {"verse": "Dan.8.1", "hib_label": "Daniel", "phenomenon_ordinal": 0,
#    "process": "...", "action_type": "...", "decision": "retain"|"set_aside"|
#    "retain_referential"|"recorded_silence", "observation_text": "...", "description_text": "...",
#    "sources": [{"kind": "self"|"human"|"non_human"|"object_situation"|"none", "detail": "...",
#                 "enablement_only": false}],
#    "targets": [{"kind": "...", "detail": "..."}]}
# ]}
def operation_set(ctx: Ctx) -> Outcome:
    book = ctx.params["Book"]
    lo, hi, vlo, vhi = _resolve_range(ctx)
    try:
        payload = _load_payload(ctx)
        operations = payload["operations"]
    except (BadPayload, KeyError) as e:
        return fail("bad-payload", str(e))
    if not operations:
        return fail("empty-payload", "payload has no 'operations' entries")

    passage_row = passagetrack.find_tracked_passage(ctx.db.conn, book, lo, hi, vlo, vhi)
    if not passage_row:
        return fail("no-passage", f"no tracked passage for {book} this range")
    if not passage_row["phenomena_complete_at"]:
        return fail("phenomena-incomplete",
                    f"passage {passage_row['id']}'s phenomena register is not complete yet "
                    f"(passage.phenomena_complete_at is NULL) -- run phenomenon.set to close the "
                    f"whole register for this passage first (debate digest Step 3's phase gate)")
    passage_id = passage_row["id"]

    hib_by_label = {r["label"]: r["id"] for r in ctx.db.rows(
        "SELECT id, label FROM hib WHERE book=? AND deleted=0", (book,))}
    problems, resolved = [], []
    for o in operations:
        vid = _verse_id(ctx, o["verse"])
        hid = hib_by_label.get(o["hib_label"])
        phen_row = None
        if vid is not None and hid is not None:
            rows = ctx.db.rows(
                "SELECT id FROM phenomenon WHERE passage_id=? AND verse_id=? AND hib_id=? "
                "AND ordinal=? AND deleted=0",
                (passage_id, vid, hid, o.get("phenomenon_ordinal", 0)))
            phen_row = rows[0] if rows else None
        if vid is None:
            problems.append(f"unknown verse {o['verse']!r}")
        elif hid is None:
            problems.append(f"unknown HIB label {o['hib_label']!r}")
        elif not phen_row:
            problems.append(f"no registered phenomenon for {o['verse']!r}/{o['hib_label']!r} "
                            f"ordinal {o.get('phenomenon_ordinal', 0)}")
        else:
            resolved.append((phen_row["id"], o))
    if problems:
        return fail("unresolved-reference",
                    f"{len(problems)} problem(s): {problems[:5]}{' ...' if len(problems) > 5 else ''}")

    _may(ctx, "operation.set", "operation")
    _may(ctx, "operation.set", "operation_party")

    phen_ids = [pid for pid, _ in resolved]
    existing = []
    if phen_ids:
        ph = ",".join("?" * len(phen_ids))
        existing = [r["id"] for r in ctx.db.rows(
            f"SELECT id FROM operation WHERE phenomenon_id IN ({ph}) AND deleted=0", phen_ids)]
    if existing:
        ph = ",".join("?" * len(existing))
        ctx.db.conn.execute(f"UPDATE operation_party SET deleted=1 WHERE operation_id IN ({ph})", existing)
        ctx.db.conn.execute(f"UPDATE operation SET deleted=1 WHERE id IN ({ph})", existing)

    now = _now()
    n_op = n_party = 0
    for phen_id, o in resolved:
        op_id = ctx.db.write("operation", {
            "phenomenon_id": phen_id, "process": o.get("process"),
            "action_type": o.get("action_type"), "decision": o.get("decision"),
            "observation_text": o.get("observation_text"),
            "description_text": o.get("description_text"),
            "created_at": now, "deleted": 0})
        n_op += 1
        for role, parties in (("source", o.get("sources", [])), ("target", o.get("targets", []))):
            for i, party in enumerate(parties):
                ctx.db.write("operation_party", {
                    "operation_id": op_id, "role": role, "kind": party["kind"],
                    "detail": party.get("detail"),
                    "enablement_only": 1 if party.get("enablement_only") else 0,
                    "ordinal": i, "created_at": now, "deleted": 0})
                n_party += 1

    ctx.db.conn.commit()
    return ok(f"{book} passage {passage_id}: {n_op} operation(s), {n_party} party record(s) written",
             operations=n_op, parties=n_party)
