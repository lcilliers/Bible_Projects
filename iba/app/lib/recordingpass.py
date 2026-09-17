"""recordingpass.py — the single writer for `ib_observation`/`ib_node` (escalation #1693's design,
built 2026-09-17). Per checklist rule 0.1: only this module ever writes these two tables; every
other routine (`versereadinggenerate.py` included) produces JSON output only. Per rule 0.5: verse
references are resolved fresh from `iba.db` at write time, never trusted from LLM-authored text.

**Same/broaden/new — #1693 §3, implemented as its own explicitly-simple first version**, per that
design's own closing note ("not decided here, deliberately left to implementation... a first
working version is expected to be simple... refined from real behaviour"):
1. Exact match on `obs_text` AND the full set of grounding references — a true duplicate, no-op
   (rule 7, "there is a risk of duplication in such cases -- and would rather have a duplicate,
   than none at all"; only the exact-match case is worth catching cheaply).
2. Same `(cluster_code, stage, strong, question_code)`, different `obs_text`, similarity above the
   threshold — a superficial difference: align, edit `obs_text` in place, add the new occurrence's
   `ib_node` row(s) against the SAME `observation_id` (rule 2).
3. Same coordinates, different `obs_text`, similarity below the threshold — genuinely expands:
   a NEW `ib_observation` row, linked back via `ib_node.traced_observation_id` (rule 3).
4. No existing row at those coordinates at all — a plain new observation.
Similarity (rule 5, "not a direct text match only... judgement, mainly use heuristics and simple
meaning") is `difflib.SequenceMatcher` on the normalized text — a real heuristic, not a from-scratch
similarity engine, exactly as rule 5 asks for.

The LLM never assigns ids, never checks for duplicates, never decides edit-vs-new (rule 0.2) --
all of that is this module's job, not the model's.
"""

from __future__ import annotations

import datetime
import difflib
import json


SIMILARITY_THRESHOLD = 0.85  # exact value not specified by #1693 -- a starting point, per its own
                              # "refined from real behaviour" instruction, not a tuned constant.


class UnresolvedOccurrence(Exception):
    """An occurrence the model claimed doesn't resolve against live verse_lexical data -- never
    written as a phantom node."""


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _normalize(text: str) -> str:
    return " ".join((text or "").lower().split())


def _similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, _normalize(a), _normalize(b)).ratio()


def resolve_occurrence(conn, strong: str, claimed_verse: str, claimed_surface: str | None,
                       claimed_morph: str | None) -> dict:
    """Rule 0.5: resolve fresh from iba.db, never trust the LLM's own verse string. Matches on
    strong + verse.osisId, disambiguating by surface/morph when a strong occurs more than once in
    the same verse. Raises UnresolvedOccurrence rather than writing an unverified node."""
    rows = conn.execute(
        """SELECT vl.strong, vl.surface, vl.morph_code, v.osisId, v.id AS verse_id
           FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id
           WHERE vl.strong=? AND v.osisId=? AND vl.deleted=0""",
        (strong, claimed_verse)).fetchall()
    if not rows:
        raise UnresolvedOccurrence(
            f"strong {strong!r} claimed at {claimed_verse!r} has no matching live verse_lexical row")
    if len(rows) == 1:
        r = rows[0]
    else:
        exact = [r for r in rows if r["surface"] == claimed_surface or r["morph_code"] == claimed_morph]
        r = exact[0] if exact else rows[0]
    return {"verse_reference": r["osisId"], "verse_id": r["verse_id"], "surface": r["surface"],
           "morph_code": r["morph_code"]}


def _existing_candidates(conn, cluster_code: str, stage: str, strong: str | None,
                         question_code: str | None) -> list[dict]:
    where = ["cluster_code=?", "stage=?"]
    params: list = [cluster_code, stage]
    if strong is None:
        where.append("strong IS NULL")
    else:
        where.append("strong=?")
        params.append(strong)
    if question_code is None:
        where.append("question_code IS NULL")
    else:
        where.append("question_code=?")
        params.append(question_code)
    rows = conn.execute(
        f"SELECT * FROM ib_observation WHERE {' AND '.join(where)}", params).fetchall()
    return [dict(r) for r in rows]


def _existing_node_refs(conn, observation_id: int) -> set[tuple]:
    rows = conn.execute(
        "SELECT strong, verse_reference FROM ib_node WHERE observation_id=?",
        (observation_id,)).fetchall()
    return {(r["strong"], r["verse_reference"]) for r in rows}


def _insert_observation(conn, cluster_code: str, stage: str, tag: str, strong: str | None,
                        question_code: str | None, obs_text: str, meaning_source: str | None,
                        source_json_serial: int | None,
                        supersedes_observation_id: int | None = None) -> int:
    cur = conn.execute(
        "INSERT INTO ib_observation (cluster_code, stage, tag, strong, question_code, obs_text, "
        "meaning_source, status, supersedes_observation_id, source_json_serial, created_at) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (cluster_code, stage, tag, strong, question_code, obs_text, meaning_source, "resolved",
         supersedes_observation_id, source_json_serial, _now()))
    return cur.lastrowid


def _insert_node(conn, observation_id: int, cluster_code: str, strong: str | None,
                 verse_reference: str | None, surface: str | None, morph_code: str | None,
                 question_code: str | None, source_stage: str, seq: int,
                 traced_observation_id: int | None = None) -> int:
    cur = conn.execute(
        "INSERT INTO ib_node (observation_id, cluster_code, strong, verse_reference, surface, "
        "morph_code, question_code, traced_observation_id, source_stage, seq, created_at) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (observation_id, cluster_code, strong, verse_reference, surface, morph_code, question_code,
         traced_observation_id, source_stage, seq, _now()))
    return cur.lastrowid


def record_one_observation(conn, cluster_code: str, stage: str, obs: dict,
                           source_json_serial: int | None) -> dict:
    """One model-produced observation -> same/broaden/new decision -> DB write(s). Returns a
    small report dict for the caller's own summary, never raises on an unresolved occurrence for
    the WHOLE observation -- only the individual bad occurrence is skipped and reported, per
    checklist rule 0.7 ("a gap is a load-time finding, not silently accepted") -- surfaced, not
    fatal to the rest of the batch."""
    strong = obs.get("strong")
    question_code = obs.get("question_code")
    tag = obs["tag"]
    obs_text = obs["obs_text"]
    meaning_source = obs.get("meaning_source")

    resolved_occurrences = []
    unresolved = []
    for occ in obs.get("occurrences", []):
        try:
            resolved_occurrences.append(resolve_occurrence(
                conn, occ.get("strong", strong), occ["verse"], occ.get("surface"),
                occ.get("morph_code")))
        except UnresolvedOccurrence as e:
            unresolved.append(str(e))
    if not resolved_occurrences:
        return {"action": "skipped-no-resolvable-occurrences", "unresolved": unresolved}

    candidates = _existing_candidates(conn, cluster_code, stage, strong, question_code)

    new_refs = {(strong, o["verse_reference"]) for o in resolved_occurrences}
    for cand in candidates:
        if cand["obs_text"] == obs_text:
            existing_refs = _existing_node_refs(conn, cand["id"])
            if new_refs <= existing_refs:
                return {"action": "no-op-exact-duplicate", "observation_id": cand["id"],
                       "unresolved": unresolved}

    best = None
    best_score = 0.0
    for cand in candidates:
        score = _similarity(cand["obs_text"], obs_text)
        if score > best_score:
            best, best_score = cand, score

    if best is not None and best_score >= SIMILARITY_THRESHOLD:
        conn.execute("UPDATE ib_observation SET obs_text=?, updated_at=? WHERE id=?",
                    (obs_text, _now(), best["id"]))
        observation_id = best["id"]
        action = "aligned-superficial-edit"
        traced = None
    elif best is not None:
        observation_id = _insert_observation(
            conn, cluster_code, stage, tag, strong, question_code, obs_text, meaning_source,
            source_json_serial)
        action = "new-expands-existing"
        traced = best["id"]
    else:
        observation_id = _insert_observation(
            conn, cluster_code, stage, tag, strong, question_code, obs_text, meaning_source,
            source_json_serial)
        action = "new-observation"
        traced = None

    existing_refs = _existing_node_refs(conn, observation_id) if action == "aligned-superficial-edit" else set()
    seq = 0
    written_nodes = []
    for o in resolved_occurrences:
        ref = (strong, o["verse_reference"])
        if ref in existing_refs:
            continue
        seq += 1
        node_id = _insert_node(
            conn, observation_id, cluster_code, strong, o["verse_reference"], o["surface"],
            o["morph_code"], question_code, stage, seq, traced_observation_id=traced)
        written_nodes.append(node_id)

    return {"action": action, "observation_id": observation_id, "node_ids": written_nodes,
           "similarity_score": round(best_score, 3) if best is not None else None,
           "unresolved": unresolved}


def record_batch(conn, cluster_code: str, stage: str, model_output: dict,
                 source_json_serial: int | None = None) -> dict:
    """Every observation in one model reply, in the same unit of work (checklist rule 0.3: assemble
    -> run -> record fires immediately after, never a deferred batch pickup). Caller commits."""
    results = [record_one_observation(conn, cluster_code, stage, obs, source_json_serial)
              for obs in model_output.get("observations", [])]
    by_action: dict[str, int] = {}
    for r in results:
        by_action[r["action"]] = by_action.get(r["action"], 0) + 1
    unresolved_total = sum(len(r.get("unresolved", [])) for r in results)
    return {"results": results, "by_action": by_action, "unresolved_occurrence_count": unresolved_total}
