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
import re


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


_WORD_LEVEL_QUESTION_PREFIXES = ("M0.1", "M0.5")


def _effective_cluster_code(conn, pass_cluster_code: str, strong: str | None,
                            question_code: str | None) -> str:
    """#1723 front-loading: a word-level (M0.1/M0.5) observation is a fact about the STRONG, not
    about whichever cluster's pass happened to produce it -- resolved fresh from the strong's own
    live cluster_strong M-code membership (never trusted from the caller), same "resolve fresh,
    don't trust the caller's own classification" discipline verse/strong resolution already use
    elsewhere in this module. Relational (M0.6.5) and D7.7.1 observations stay keyed to the PASS's
    own cluster_code -- they are inherently that cluster's own vantage point on the verse, not a
    strong-level fact, and different clusters' M0.6.5 rows about the same verse must coexist, not
    collapse into one. Falls back to the pass's own cluster_code if the strong carries no live
    M-code (shouldn't happen for a word-level question, but never silently produces a NULL)."""
    if not strong or not question_code or not question_code.startswith(_WORD_LEVEL_QUESTION_PREFIXES):
        return pass_cluster_code
    row = conn.execute(
        "SELECT cluster_code FROM cluster_strong WHERE strong=? AND deleted=0 "
        "AND cluster_code LIKE 'M%' ORDER BY cluster_code LIMIT 1", (strong,)).fetchone()
    return row["cluster_code"] if row else pass_cluster_code


def _window_for(conn, question_code: str | None) -> str | None:
    """window is DERIVED from the catalogue question, never invented ad hoc (#1723 -- the old
    #1691 definition duplicated `stage`; the new one is the question's own registered angle)."""
    if not question_code:
        return None
    row = conn.execute(
        "SELECT window FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
        (question_code,)).fetchone()
    return row["window"] if row else None


class InvalidQuestionCode(Exception):
    """question_code doesn't resolve to a real, live catalogue leaf question. Found live 2026-09-17
    redoing M67 under the #1723 front-loading rework: under heavier per-batch load, the model
    sometimes collapsed several M0.1.x/M0.5.x sub-answers into one combined note filed under the
    bare component code ('M0.1'/'M0.5') instead of a real leaf code -- 38 strongs ended up with
    ZERO properly-coded word-level battery answers, just two unbindable blobs each, and (worse)
    the front-loading skip-check would have silently treated them as already-covered forever.
    Confirms and closes the same gap #1719 already flagged for D7.7-vs-D7.7.1 drift and the literal
    string 'none' -- no live FK/validation existed at write time. Refusing the whole observation
    (not writing a phantom row under a bogus code) is the fix, matching checklist rule 0.7 ("a gap
    is a load-time finding, not silently accepted")."""


def _validate_question_code(conn, question_code: str | None) -> None:
    if question_code is None:
        return
    row = conn.execute(
        "SELECT 1 FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0 "
        "AND status='active'", (question_code,)).fetchone()
    if not row:
        raise InvalidQuestionCode(
            f"question_code {question_code!r} does not match a real, live catalogue question -- "
            f"refusing to write a phantom observation under it")


class InvalidTag(Exception):
    """tag doesn't resolve to a real, active `cfg_enum` value for `ib_observation.tag`. Found live
    2026-09-17 (escalation #1723 v10-v15): `tag` had NO write-time validation at all, unlike
    `question_code` (fixed the same day) -- the literal string 'none' (15 rows) leaked through
    despite never being a registered enum value, alongside `answered-no-flag` being used as a
    non-discriminating 77%-of-corpus default. Refusing the write (not silently accepting an
    unregistered string) matches the question_code fix and checklist rule 0.7."""


def _validate_tag(conn, tag: str) -> None:
    row = conn.execute(
        "SELECT 1 FROM cfg_enum WHERE name='ib_observation.tag' AND value=? AND inactive=0",
        (tag,)).fetchone()
    if not row:
        raise InvalidTag(
            f"tag {tag!r} does not match a real, active ib_observation.tag enum value -- "
            f"refusing to write an observation under it")


_DEGENERATE_OBS_TEXT = re.compile(r"^\s*(none|n/?a|null|nothing|-)\s*\.?\s*$", re.I)


class InvalidObservationText(Exception):
    """obs_text is a bare negation with no actual content -- e.g. the literal string "none" alone,
    not "none -- <real explanation>" (the latter has substance despite the awkward lead-in and is
    NOT rejected by this check). Found live 2026-09-17 (escalation #1723 v16), researcher spotting
    it directly: id 524 (H0629/M0.5.4/Ezra.7.17) was the four-character string "none", nothing
    else -- and it TRACED to observation 417, which already held the real answer for this
    strong+question. A content-less duplicate is worse than no row at all: it looks answered
    (defeating the front-loading skip-check) while adding zero information. Same family of gap as
    #282 (question_code) and #283 (tag) -- refusing the write, not silently accepting an empty
    claim, per checklist rule 0.7."""


def _validate_obs_text(conn, obs_text: str) -> None:
    if _DEGENERATE_OBS_TEXT.match(obs_text or ""):
        raise InvalidObservationText(
            f"obs_text {obs_text!r} is a bare negation with no actual content -- refusing to "
            f"write a content-less observation")


def _insert_observation(conn, cluster_code: str, stage: str, tag: str, strong: str | None,
                        question_code: str | None, obs_text: str, meaning_source: str | None,
                        source_json_serial: int | None,
                        supersedes_observation_id: int | None = None) -> int:
    window = _window_for(conn, question_code)
    cur = conn.execute(
        "INSERT INTO ib_observation (cluster_code, stage, tag, strong, question_code, obs_text, "
        "meaning_source, status, supersedes_observation_id, source_json_serial, window, "
        "created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (cluster_code, stage, tag, strong, question_code, obs_text, meaning_source, "resolved",
         supersedes_observation_id, source_json_serial, window, _now()))
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

    try:
        _validate_question_code(conn, question_code)
    except InvalidQuestionCode as e:
        return {"action": "skipped-invalid-question-code", "unresolved": [str(e)]}

    try:
        _validate_tag(conn, tag)
    except InvalidTag as e:
        return {"action": "skipped-invalid-tag", "unresolved": [str(e)]}

    try:
        _validate_obs_text(conn, obs_text)
    except InvalidObservationText as e:
        return {"action": "skipped-invalid-obs-text", "unresolved": [str(e)]}

    # #1723: a word-level (M0.1/M0.5) observation is filed under the STRONG's own actual M-code,
    # not the pass's cluster_code -- lets a later cluster's own pass find it as already covered
    # regardless of which cluster's pass originally front-loaded it.
    effective_cluster_code = _effective_cluster_code(conn, cluster_code, strong, question_code)

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

    candidates = _existing_candidates(conn, effective_cluster_code, stage, strong, question_code)

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
            conn, effective_cluster_code, stage, tag, strong, question_code, obs_text,
            meaning_source, source_json_serial)
        action = "new-expands-existing"
        traced = best["id"]
    else:
        observation_id = _insert_observation(
            conn, effective_cluster_code, stage, tag, strong, question_code, obs_text,
            meaning_source, source_json_serial)
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
            conn, observation_id, effective_cluster_code, strong, o["verse_reference"], o["surface"],
            o["morph_code"], question_code, stage, seq, traced_observation_id=traced)
        written_nodes.append(node_id)

    return {"action": action, "observation_id": observation_id, "node_ids": written_nodes,
           "similarity_score": round(best_score, 3) if best is not None else None,
           "unresolved": unresolved}


def record_batch(conn, cluster_code: str, stage: str, model_output: dict,
                 source_json_serial: int | None = None) -> dict:
    """Every observation in one model reply, in the same unit of work (checklist rule 0.3: assemble
    -> run -> record fires immediately after, never a deferred batch pickup). Caller commits.

    `unresolved_detail` carries the actual reason strings, not just a count (found live 2026-09-17,
    twice -- BUILD.md #274 first flagged this as a gap for Stage 1, then it directly cost real
    diagnostic ability redoing Stage 2's M67 run: a whole observation's citation failure was
    reported only as a bare number, with no way afterward to tell whether it was a real defect or
    an ordinary LLM verse-citation slip, short of a fresh, non-reproducible, real-money re-call).
    Every caller should log/persist this, not just the count."""
    results = [record_one_observation(conn, cluster_code, stage, obs, source_json_serial)
              for obs in model_output.get("observations", [])]
    by_action: dict[str, int] = {}
    for r in results:
        by_action[r["action"]] = by_action.get(r["action"], 0) + 1
    unresolved_detail = [msg for r in results for msg in r.get("unresolved", [])]
    return {"results": results, "by_action": by_action,
           "unresolved_occurrence_count": len(unresolved_detail),
           "unresolved_detail": unresolved_detail}


class SubgroupWriteError(Exception):
    """A defect in process (b)'s own output JSON -- structurally invalid, not a resolvable data
    gap (missing label, missing FLAG reason, a strong placed twice or not at all). Fails the WHOLE
    write, never a partial cluster -- unlike an unresolved ib_node occurrence (a genuine per-item
    gap in live data), these are the LLM violating its own stated output contract."""


_FLAG_LABEL = "FLAG — signpost, not a real subgroup (see member placement_notes for reasons)"


def _resolve_verse_reference(conn, ref: str | None) -> str | None:
    """Resolves fresh against iba.db.verse.osisId -- the same column resolve_occurrence/ib_node.
    verse_reference already use, and what the LLM is actually given/constrained to (versereading
    generate.py's own "verse" field is v['osisId']), not the separate, nullable `reference` column."""
    if not ref:
        return None
    row = conn.execute("SELECT osisId FROM verse WHERE osisId=? AND deleted=0", (ref,)).fetchone()
    return row["osisId"] if row else None


def record_subgroups(conn, cluster_code: str, member_strongs: list[str], model_output: dict) -> dict:
    """Writes `cluster_subgroup`/`cluster_subgroup_strong` from process (b)'s whole-cluster output
    (#1690/#1693). First-allocation path only -- re-running process (b) against a cluster that
    already has live subgroups is refused (#1690 §5 item 1's own re-grouping/versioning question is
    explicitly not yet designed; this is not that decision made silently). Caller commits."""
    existing = conn.execute(
        "SELECT COUNT(*) n FROM cluster_subgroup WHERE cluster_code=? AND delete_flagged=0",
        (cluster_code,)).fetchone()["n"]
    if existing:
        raise SubgroupWriteError(
            f"{cluster_code} already has {existing} live cluster_subgroup row(s) -- re-run/"
            f"re-grouping reconciliation is not designed yet (#1690 §5 item 1); refusing rather "
            f"than silently duplicating or guessing how to merge")

    subgroups = model_output.get("subgroups", [])
    if not subgroups:
        raise SubgroupWriteError("model reply has an empty 'subgroups' list")

    seen_strongs: dict[str, str] = {}
    for sg in subgroups:
        code = sg.get("subgroup_code")
        if not code:
            raise SubgroupWriteError(f"a subgroup is missing subgroup_code: {sg!r}")
        if code != "FLAG" and not sg.get("label"):
            raise SubgroupWriteError(f"subgroup {code!r} has no label -- required for every "
                                     f"non-FLAG subgroup (#1690 §2(d)/schema NOT NULL)")
        for m in sg.get("members", []):
            strong = m.get("strong")
            if not strong:
                raise SubgroupWriteError(f"subgroup {code!r} has a member with no strong: {m!r}")
            if code == "FLAG" and not m.get("placement_note"):
                raise SubgroupWriteError(
                    f"FLAG member {strong!r} has no placement_note -- required, must state the "
                    f"reason for the flag (#1690 §2(f)/§3 item 3)")
            if strong in seen_strongs:
                raise SubgroupWriteError(
                    f"strong {strong!r} placed in both {seen_strongs[strong]!r} and {code!r} -- "
                    f"UNIQUE(strong) violated by the model's own output")
            seen_strongs[strong] = code

    missing = sorted(set(member_strongs) - set(seen_strongs))
    if missing:
        raise SubgroupWriteError(
            f"{len(missing)} of {len(member_strongs)} cluster member strong(s) were not placed in "
            f"any subgroup: {missing}")
    extra = sorted(set(seen_strongs) - set(member_strongs))
    if extra:
        raise SubgroupWriteError(
            f"{len(extra)} strong(s) placed that are not members of this cluster: {extra}")

    now = _now()
    written = {"subgroups": 0, "members": 0, "flag_members": 0, "unresolved_anchor_verses": []}
    for sg in subgroups:
        code = sg["subgroup_code"]
        is_flag = code == "FLAG"
        label = _FLAG_LABEL if is_flag else sg["label"]
        anchor = None
        if not is_flag:
            anchor = _resolve_verse_reference(conn, sg.get("anchor_verse_reference"))
            if sg.get("anchor_verse_reference") and not anchor:
                written["unresolved_anchor_verses"].append(
                    {"subgroup_code": code, "claimed": sg.get("anchor_verse_reference")})
        cur = conn.execute(
            "INSERT INTO cluster_subgroup (cluster_code, subgroup_code, label, core_description, "
            "anchor_verse_reference, status, source, created_at, last_updated_date) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            (cluster_code, code, label, sg.get("core_description"), anchor,
             None if is_flag else "allocated", "cluster.subgroup", now, now))
        subgroup_id = cur.lastrowid
        written["subgroups"] += 1
        for m in sg.get("members", []):
            conn.execute(
                "INSERT INTO cluster_subgroup_strong (strong, cluster_subgroup_id, "
                "placement_note, delete_flagged, created_at, last_updated_date) "
                "VALUES (?,?,?,0,?,?)",
                (m["strong"], subgroup_id, m.get("placement_note"), now, now))
            written["members"] += 1
            if is_flag:
                written["flag_members"] += 1

    return written
