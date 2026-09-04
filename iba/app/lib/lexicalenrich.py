"""lexicalenrich.py — Stage 1 Layer 2 engine: `verse_lexical_note` capture + `passage.genre`/
`lexical_complete_at`, JSON-payload-driven. Escalation #1383, full build spec §C.2/§D.2/§E.2.

Separate module from `lib/lexical.py` (open item 5 of the build spec, resolved by
`migration/build_verse_lexical_window1_layer1_layer2_v1_20260904.py`'s own docstring §4) — Layer 1
(mechanical) and Layer 2 (judgement-bearing) stay in their own files, matching the design doc's own
C.1/C.2 split.

**What this is, and isn't** — same framing `handlers/operations.py` already states for
`phenomenon.set`/`hib.set`: the analytical work (idiom sense, related-word sorting, pronoun/entity
resolution, structural-pattern naming) is done by an AI/researcher reading pass against the method
docs, BEFORE this module is ever called. This module mechanises turning that pass's *already-
decided* findings into validated, grant-checked `verse_lexical_note` rows — a JSON payload in,
structured rows out, same shape as `operations.py`'s own `phenomenon.set`.

**Reconciliation, reused not re-derived** (design doc §E.4): a local copy of `_reconcile()` —
duplicated rather than imported from `handlers/operations.py`, matching this codebase's own
established convention of small per-file helpers (`debateaudit.py`'s own docstring: "unlike this
app's own small `_may`/`_now` helpers, which each handler file defines locally") and keeping this
`lib/` module free of a `lib -> handlers` runtime dependency (no other `lib` module has one).
Every incoming note is classified `unchanged`/`changed`/`new` against the block's current live
state, by key `(verse_lexical_id, note_type)`; every `changed` item needs a `reconciliation_note`;
every pre-existing item not addressed by the payload (repeated or listed under `remove`) is a hard
stop (`unreconciled`), never a silent drop.

**Write convention — differs from `phenomenon.set`, deliberately** (design doc §E.4): a `changed`
note is soft-deleted-and-reinserted (fresh `id`), NOT updated in place — `verse_lexical_note` has
no downstream FK dependent yet (unlike `phenomenon`, whose `id` `operation.phenomenon_id` points
at), so there is nothing to orphan by minting a new id. Matches `verse_lexical`'s own
`write_readings_for_span` convention, not `phenomenon.set`'s in-place UPDATE.

**Addressing a code within a payload note** (design doc §C.2, addressing mechanics resolved here —
the source table names two alternative shapes, "verse+position" or "strong+code_ordinal", without
spelling out the exact resolution when a span carries more than one code at the same `position`;
resolved as a self-correctable implementation choice, not a new design axis): every note key
supplies `verse` (osisId) + `position` (`verse_lexical.position`, the span-level word position) +
`code_ordinal` (defaults to 0 — the common single-code-per-span case) — together these are a unique
key on the NEW `position` column plus the existing `code_ordinal`, resolved directly against
`verse_lexical` with no join back through `span` needed.
"""

from __future__ import annotations

import datetime
import json


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── reconciliation gate — local copy, same contract as handlers/operations.py:_reconcile ───────
class ReconciliationError(Exception):
    def __init__(self, problems: list[str]):
        self.problems = problems
        super().__init__(f"{len(problems)} item(s) need reconciliation")


def _reconcile(current: dict, incoming: dict, removals: dict) -> tuple[list, list, list, list]:
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


# ── resolution: payload verse/position/code_ordinal -> live verse_lexical row ──────────────────

class UnresolvedReference(Exception):
    """Raised when a payload note/removal/target/related-code doesn't resolve to a live row.
    Always caught and turned into a clean fail(), never a partial write."""

    def __init__(self, problems: list[str]):
        self.problems = problems
        super().__init__(f"{len(problems)} unresolved reference(s)")


def resolve_verse_lexical_id(conn, verse_id_by_osis: dict[str, int | None], osis: str,
                             position: int, code_ordinal: int = 0) -> int | None:
    vid = verse_id_by_osis.get(osis)
    if vid is None:
        return None
    row = conn.execute(
        "SELECT id FROM verse_lexical WHERE verse_id=? AND position=? AND code_ordinal=? "
        "AND deleted=0", (vid, position, code_ordinal)).fetchone()
    return row["id"] if row else None


# ── note_type quality checks (design doc §D.2) ──────────────────────────────────────────────────

def _quality_problems_for_note(conn, item: dict, verse_lexical_id: int, code_classes) -> list[str]:
    """`item`: the already-resolved note dict (note_type/resolution_status/target_id/related_ids/
    value_text). Returns a list of quality-defect messages (empty = no defect) — checked per
    §D.2's own note_type table, not exhaustively re-derived from first principles."""
    problems: list[str] = []
    note_type = item["note_type"]
    status = item["resolution_status"]
    src = conn.execute(
        "SELECT strong, morph_code, narrative_morph FROM verse_lexical WHERE id=?",
        (verse_lexical_id,)).fetchone()

    if note_type == "chain" and status == "resolved" and not (src and src["narrative_morph"]):
        problems.append(f"{note_type!r} note resolved but source row has no narrative_morph — "
                        f"a chain claim with no morphological basis")
    if note_type == "idiom" and status not in ("resolved", "checked_empty"):
        problems.append(f"{note_type!r} note has resolution_status={status!r} — an idiom test is "
                        f"binary, only 'resolved'/'checked_empty' are valid")
    if note_type == "structural_pattern":
        related = item.get("related_ids") or []
        if len(related) < 2:
            problems.append(f"structural_pattern note names {len(related)} related code(s), "
                            f"needs ≥2")
    if note_type == "recurrence_role_shift":
        target = item.get("target_id")
        related = item.get("related_ids") or []
        compare_ids = ([target] if target else []) + related
        for cid in compare_ids:
            cmp_row = conn.execute(
                "SELECT strong, morph_code FROM verse_lexical WHERE id=?", (cid,)).fetchone()
            if cmp_row and src and (cmp_row["strong"], cmp_row["morph_code"]) != \
                    (src["strong"], src["morph_code"]):
                problems.append("recurrence_role_shift note's target/related row is a DIFFERENT "
                                "(strong, morph_code) pair than the source row")
    if note_type == "cross_lemma_shared_gloss":
        target = item.get("target_id")
        if target:
            cmp_row = conn.execute(
                "SELECT strong, resolved_sense FROM verse_lexical WHERE id=?", (target,)).fetchone()
            if cmp_row and src:
                src_full = conn.execute(
                    "SELECT strong, resolved_sense FROM verse_lexical WHERE id=?",
                    (verse_lexical_id,)).fetchone()
                if cmp_row["strong"] == src_full["strong"]:
                    problems.append("cross_lemma_shared_gloss note's target shares the SAME "
                                    "strong code as the source — that belongs to "
                                    "gloss_consistent_in_verse, not this note_type")
                if cmp_row["resolved_sense"] != src_full["resolved_sense"]:
                    problems.append("cross_lemma_shared_gloss note's target does NOT share the "
                                    "source's resolved_sense")
    return problems


# ── the write, one passage-block at a time ──────────────────────────────────────────────────────

def enrich_passage(conn, passage_id: int, verse_ids_in_passage: list[int],
                   verse_id_by_osis: dict[str, int], genre: str | None,
                   notes_payload: list[dict], removals_payload: list[dict]) -> dict:
    """`notes_payload`/`removals_payload`: already the raw payload's own `notes`/`remove` lists
    (handler has already loaded/parsed the JSON). Returns a dict of counts on success; raises
    `UnresolvedReference`/`ReconciliationError` (handler turns each into a clean `fail()`) —
    never a partial write."""
    problems: list[str] = []
    resolved_notes: dict[tuple, dict] = {}   # key -> {content, note (reconciliation), raw}
    for n in notes_payload:
        vlid = resolve_verse_lexical_id(conn, verse_id_by_osis, n["verse"], n["position"],
                                        n.get("code_ordinal", 0))
        if vlid is None:
            problems.append(f"unknown verse/code {n['verse']}:{n['position']} — has "
                            f"lexical.build run for this verse?")
            continue
        target_id = None
        if n.get("target_verse") and n.get("target_position") is not None:
            target_id = resolve_verse_lexical_id(conn, verse_id_by_osis, n["target_verse"],
                                                  n["target_position"],
                                                  n.get("target_code_ordinal", 0))
            if target_id is None:
                problems.append(f"unknown-target {n['target_verse']}:{n['target_position']}")
        related_ids = []
        for rc in n.get("related_codes") or []:
            rid = resolve_verse_lexical_id(conn, verse_id_by_osis, rc["verse"], rc["position"],
                                           rc.get("code_ordinal", 0))
            if rid is None:
                problems.append(f"unknown-related-code {rc['verse']}:{rc['position']}")
            else:
                related_ids.append(rid)
        key = (vlid, n["note_type"])
        content = (n["resolution_status"], target_id, tuple(sorted(related_ids)),
                  n.get("finding"), n.get("evidence"))
        resolved_notes[key] = {
            "content": content, "note": n.get("reconciliation_note"),
            "raw": {**n, "verse_lexical_id": vlid, "target_id": target_id,
                    "related_ids": related_ids}}

    removals: dict[tuple, str] = {}
    for r in removals_payload:
        vlid = resolve_verse_lexical_id(conn, verse_id_by_osis, r["verse"], r["position"],
                                        r.get("code_ordinal", 0))
        if vlid is None:
            problems.append(f"'remove' names unknown verse/code {r['verse']}:{r['position']}")
            continue
        removals[(vlid, r["note_type"])] = r.get("reason")

    if problems:
        raise UnresolvedReference(problems)

    current_rows = conn.execute(
        "SELECT n.id, n.verse_lexical_id, n.note_type, n.resolution_status, "
        "n.target_verse_lexical_id, n.related_verse_lexical_ids, n.value_text, n.evidence_text "
        "FROM verse_lexical_note n WHERE n.passage_id=? AND n.deleted=0", (passage_id,)).fetchall()

    current: dict[tuple, dict] = {}
    for r in current_rows:
        key = (r["verse_lexical_id"], r["note_type"])
        related = tuple(sorted(json.loads(r["related_verse_lexical_ids"] or "[]")))
        current[key] = {"content": (r["resolution_status"], r["target_verse_lexical_id"], related,
                                    r["value_text"], r["evidence_text"]), "id": r["id"]}

    incoming = {k: {"content": v["content"], "note": v["note"]} for k, v in resolved_notes.items()}
    unchanged, changed, new, removed = _reconcile(current, incoming, removals)

    code_classes = None  # placeholder for future quality-check wiring against cfg_lexical_code_class
    quality_problems: list[str] = []
    for key in list(new) + list(changed):
        raw = resolved_notes[key]["raw"]
        quality_problems += _quality_problems_for_note(conn, raw, raw["verse_lexical_id"],
                                                        code_classes)
    if quality_problems:
        raise UnresolvedReference(quality_problems)   # handler maps to bad-payload, see docstring

    now = _now()
    for key in removed:
        conn.execute("UPDATE verse_lexical_note SET deleted=1 WHERE id=?", (current[key]["id"],))
    for key in changed:
        conn.execute("UPDATE verse_lexical_note SET deleted=1 WHERE id=?", (current[key]["id"],))
    for key in list(new) + list(changed):
        raw = resolved_notes[key]["raw"]
        vlid, note_type = key
        conn.execute(
            "INSERT INTO verse_lexical_note (verse_lexical_id, verse_id, passage_id, note_type, "
            "resolution_status, target_verse_lexical_id, related_verse_lexical_ids, value_text, "
            "evidence_text, created_at, deleted) VALUES (?,?,?,?,?,?,?,?,?,?,0)",
            (vlid, verse_id_by_osis[raw["verse"]], passage_id, note_type,
             raw["resolution_status"], raw.get("target_id"),
             json.dumps(raw["related_ids"]) if raw.get("related_ids") else None,
             raw.get("finding"), raw.get("evidence"), now))

    if genre is not None:
        conn.execute("UPDATE passage SET genre=? WHERE id=?", (genre, passage_id))

    return {"unchanged": len(unchanged), "changed": len(changed), "new": len(new),
           "removed": len(removed)}


def check_completeness(conn, passage_id: int, verse_ids_in_passage: list[int]) -> tuple[bool, list[str]]:
    """§D.2's control-total, applied: every non-'inert'-role code (i.e. every live `verse_lexical`
    row in this passage) must carry ≥1 live `verse_lexical_note` row. Returns (complete, missing)
    — `missing` is a list of `verse:position` strings, capped by the caller for the message
    (same `problems[:5]` convention as every other handler)."""
    if not verse_ids_in_passage:
        return True, []
    ph = ",".join("?" * len(verse_ids_in_passage))
    rows = conn.execute(
        f"SELECT vl.id, v.osisId, vl.position FROM verse_lexical vl "
        f"JOIN verse v ON v.id=vl.verse_id "
        f"WHERE vl.verse_id IN ({ph}) AND vl.deleted=0", tuple(verse_ids_in_passage)).fetchall()
    noted = {r["verse_lexical_id"] for r in conn.execute(
        f"SELECT DISTINCT verse_lexical_id FROM verse_lexical_note WHERE passage_id=? "
        f"AND deleted=0", (passage_id,))}
    missing = [f"{r['osisId']}:{r['position']}" for r in rows if r["id"] not in noted]
    return (len(missing) == 0), missing


def set_lexical_complete(conn, passage_id: int, complete: bool) -> None:
    conn.execute("UPDATE passage SET lexical_complete_at=? WHERE id=?",
               (_now() if complete else None, passage_id))
