"""recordingpass.py — the single writer for `ib_observation`/`ib_node` (#1693). Only this module
writes these two tables; every other routine (`versereadinggenerate.py` included) produces JSON
only. Verse references are resolved fresh from `iba.db` at write time, never trusted from
LLM-authored text.

Same/broaden/new for a fresh answer, by question family:
  - per-occurrence questions (M0.7, M0.8.1, M0.5.11: one word in one verse; M0.6.5/M0.6.6/D7.7.1:
    one fact per verse): identity is structural. The candidate pool is scoped to the occurrence
    (or the verse), so 0 candidates = new, 1 = align, 2+ = legacy duplicates, consolidated (#1824,
    #1832).
  - word-level questions (M0.1/M0.5, a fact about the strong, cluster_code NULL): exact text match
    only; anything else is a distinct observation (#1849).
  - every other question: within the cluster-wide pool, a structured-key match (surface + morph +
    meaning keywords) or `difflib.SequenceMatcher` similarity above the threshold aligns and edits
    in place; below it, a new row linked via `ib_node.traced_observation_id`.

The LLM never assigns ids, checks for duplicates, or decides edit-vs-new.
"""

from __future__ import annotations

import datetime
import difflib
import json
import re


SIMILARITY_THRESHOLD = 0.85  # fallback only; callers pass cfg_setting cluster.recording_similarity_threshold


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


_VERSE_LEVEL_OCCURRENCE_CODES = ("M0.6.5", "M0.6.6", "D7.7.1")


def _is_strong_specific_occurrence_question(question_code: str | None) -> bool:
    """Per-occurrence, word-specific questions: M0.7.1-16, M0.8.1 (one non-M-code word's own
    elevation candidacy, #1836) and M0.5.11 (where this occurrence's meaning diverges from the
    term's usual sense). Identity is the exact (verse, strong) occurrence."""
    return bool(question_code) and (
        question_code.startswith("M0.7") or question_code in ("M0.8.1", "M0.5.11"))


def _is_per_occurrence_question(question_code: str | None) -> bool:
    """Per-occurrence questions (#1824): the strong-specific family plus the relational verse-level
    ones. Delegates to the two predicates so the sets cannot drift apart (#1840)."""
    if not question_code:
        return False
    return (_is_strong_specific_occurrence_question(question_code) or
           question_code in _VERSE_LEVEL_OCCURRENCE_CODES)


def _is_verse_level_occurrence_question(question_code: str | None) -> bool:
    """M0.6.5/M0.6.6/D7.7.1: verse-level facts asked once per M-code strong present. Near duplicates
    within a question are not allowed, across clusters and strongs (#1832), so their candidate pool is
    verse-scoped (any strong, any cluster)."""
    return question_code in _VERSE_LEVEL_OCCURRENCE_CODES


def _existing_candidates(conn, cluster_code: str, stage: str, strong: str | None,
                         question_code: str | None,
                         occurrence_refs: set[tuple] | None = None) -> list[dict]:
    """The candidate pool for a fresh answer. Word-level questions: cluster + stage + strong +
    question_code, any verse. Strong-specific occurrence questions: narrowed to candidates already
    citing one of this observation's (strong, verse_reference) occurrences (#1824). Verse-level
    questions: stage + question_code + verse only, any strong, any cluster (#1832)."""
    # `o.` prefix: ib_observation and ib_node both carry cluster_code
    if _is_verse_level_occurrence_question(question_code) and occurrence_refs:
        verse_refs = sorted({verse_ref for _, verse_ref in occurrence_refs})
        ph = ",".join("?" * len(verse_refs))
        rows = conn.execute(
            f"SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id = o.id "
            f"WHERE o.stage=? AND o.question_code=? AND n.verse_reference IN ({ph})",
            [stage, question_code] + verse_refs).fetchall()
        return [dict(r) for r in rows]

    where = ["o.stage=?"]
    params: list = [stage]
    # cluster_code None (word-level) needs IS NULL: NULL never equals a bound "=?"
    if cluster_code is None:
        where.append("o.cluster_code IS NULL")
    else:
        where.append("o.cluster_code=?")
        params.append(cluster_code)
    if strong is None:
        where.append("o.strong IS NULL")
    else:
        where.append("o.strong=?")
        params.append(strong)
    if question_code is None:
        where.append("o.question_code IS NULL")
    else:
        where.append("o.question_code=?")
        params.append(question_code)

    if _is_strong_specific_occurrence_question(question_code) and occurrence_refs:
        pair_clauses = " OR ".join(["(n.strong=? AND n.verse_reference=?)"] * len(occurrence_refs))
        pair_params: list = []
        for occ_strong, verse_ref in occurrence_refs:
            pair_params += [occ_strong, verse_ref]
        rows = conn.execute(
            f"SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id = o.id "
            f"WHERE {' AND '.join(where)} AND ({pair_clauses})",
            params + pair_params).fetchall()
    else:
        rows = conn.execute(
            f"SELECT * FROM ib_observation o WHERE {' AND '.join(where)}", params).fetchall()
    return [dict(r) for r in rows]


def _consolidate_duplicates(conn, canonical_id: int, duplicate_ids: list[int]) -> None:
    """When a fresh answer for an exact occurrence finds more than one candidate (legacy
    duplication, #1824): soft-withdraws the duplicates (status='withdrawn', never a delete) and
    re-points their `ib_node` citations onto the canonical, so no occurrence record is lost.
    `supersedes_observation_id` is not used: per its cfg_column.use it belongs to the synthesis stage."""
    _assert_valid_ib_status(conn, "withdrawn")
    for dup_id in duplicate_ids:
        conn.execute("UPDATE ib_observation SET status='withdrawn', updated_at=? WHERE id=?",
                    (_now(), dup_id))
        seq = conn.execute("SELECT COALESCE(MAX(seq), 0) FROM ib_node WHERE observation_id=?",
                           (canonical_id,)).fetchone()[0]
        dup_nodes = conn.execute("SELECT id FROM ib_node WHERE observation_id=? ORDER BY seq",
                                 (dup_id,)).fetchall()
        for n in dup_nodes:
            seq += 1
            conn.execute("UPDATE ib_node SET observation_id=?, seq=? WHERE id=?",
                        (canonical_id, seq, n["id"]))


def _existing_node_refs(conn, observation_id: int) -> set[tuple]:
    rows = conn.execute(
        "SELECT strong, verse_reference FROM ib_node WHERE observation_id=?",
        (observation_id,)).fetchall()
    return {(r["strong"], r["verse_reference"]) for r in rows}


_WORD_LEVEL_QUESTION_PREFIXES = ("M0.1", "M0.5")


def _is_word_level_question(question_code: str | None) -> bool:
    """M0.1.x/M0.5.x -- a fact about the strong alone (researcher ruling, #1849: the keys are strong
    and verse): one canonical `ib_observation` per (strong, question_code), `cluster_code IS NULL`.
    Excludes M0.5.11, a strong-specific occurrence question."""
    return (bool(question_code) and question_code.startswith(_WORD_LEVEL_QUESTION_PREFIXES)
           and not _is_strong_specific_occurrence_question(question_code))


def _effective_cluster_code(conn, pass_cluster_code: str, strong: str | None,
                            question_code: str | None) -> str | None:
    """The cluster_code an observation is filed under: None for word-level questions (strong-only
    facts), otherwise the pass's own cluster_code. Verse-level rows still merge across clusters on
    content (`_existing_candidates`, #1832)."""
    if _is_word_level_question(question_code):
        return None
    return pass_cluster_code


def _window_for(conn, question_code: str | None) -> str | None:
    """window is derived from the catalogue question's own registered angle (#1723), and checked
    against the ib_observation.window cfg_enum (#1796)."""
    if not question_code:
        return None
    row = conn.execute(
        "SELECT window FROM wa_obs_question_catalogue WHERE question_code=? AND deleted=0",
        (question_code,)).fetchone()
    window = row["window"] if row else None
    if window is not None:
        valid = {r[0] for r in conn.execute(
            "SELECT value FROM cfg_enum WHERE name='ib_observation.window' AND inactive=0")}
        if window not in valid:
            raise ValueError(
                f"wa_obs_question_catalogue.window {window!r} for question_code {question_code!r} "
                f"not in live cfg_enum ib_observation.window {sorted(valid)} -- catalogue has "
                f"drifted from the registered enum")
    return window


class InvalidQuestionCode(Exception):
    """question_code doesn't resolve to a live catalogue leaf question (e.g. a bare component code
    such as 'M0.1' or the string 'none', #1723). The whole observation is refused rather than written
    under a bogus code: a gap is a load-time finding, not silently accepted."""


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
    """tag doesn't resolve to an active `cfg_enum` value for `ib_observation.tag` (#1723). Refused,
    as for question_code."""


def _validate_tag(conn, tag: str) -> None:
    row = conn.execute(
        "SELECT 1 FROM cfg_enum WHERE name='ib_observation.tag' AND value=? AND inactive=0",
        (tag,)).fetchone()
    if not row:
        raise InvalidTag(
            f"tag {tag!r} does not match a real, active ib_observation.tag enum value -- "
            f"refusing to write an observation under it")


class InvalidMeaningSource(ValueError):
    pass


def normalise_meaning_source(conn, raw: str | None) -> str | None:
    """The model's meaning_source text as the real sources it names (#2207): each part (split on ; , +
    or /) mapped through cfg_setting ib_observation.meaning_source_aliases to a value of cfg_enum
    ib_observation.meaning_source, joined '; ' in enum order. Any 'n/a ...' is 'n/a'. An unknown part
    skips the observation (InvalidMeaningSource), as an unknown tag does. Stored rows are not touched (rule 68)."""
    if raw is None or not str(raw).strip():
        return None
    import json
    import re
    text = str(raw).strip()
    order = [r[0] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.meaning_source' AND inactive=0 "
        "ORDER BY ordinal")]
    if text.lower().startswith("n/a"):
        return "n/a"
    row = conn.execute("SELECT value FROM cfg_setting WHERE key='ib_observation.meaning_source_aliases' "
                       "AND inactive=0").fetchone()
    aliases = json.loads(row[0]) if row else {}
    found = set()
    for part in re.split(r"\s*[;,+/]\s*", text):
        p = part.strip().lower()
        if not p:
            continue
        src = p if p in order else aliases.get(p)
        if src is None:
            raise InvalidMeaningSource(f"meaning_source part {part!r} is not a source in cfg_enum "
                             f"ib_observation.meaning_source nor an alias in "
                             f"ib_observation.meaning_source_aliases -- refusing to write")
        found.add(src)
    return "; ".join(v for v in order if v in found) or None


def _validate_stage(conn, stage: str) -> None:
    """stage is caller-supplied (a literal naming the calling pipeline stage), never model output,
    so a mismatch is a programming bug: asserts (ValueError) against the cfg_enum, queried fresh."""
    valid = {r[0] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.stage' AND inactive=0")}
    if stage not in valid:
        raise ValueError(f"stage {stage!r} not in live cfg_enum ib_observation.stage {sorted(valid)}")


_DEGENERATE_OBS_TEXT = re.compile(r"^\s*(none|n/?a|null|nothing|-)\s*\.?\s*$", re.I)


class InvalidObservationText(Exception):
    """obs_text is a bare negation with no content, e.g. "none" alone ("none -- <explanation>" is
    allowed). Refused: a content-less row looks answered while adding nothing (#1723)."""


def _validate_obs_text(conn, obs_text: str) -> None:
    if _DEGENERATE_OBS_TEXT.match(obs_text or ""):
        raise InvalidObservationText(
            f"obs_text {obs_text!r} is a bare negation with no actual content -- refusing to "
            f"write a content-less observation")


def _assert_valid_ib_status(conn, status: str) -> None:
    """status is a fixed internal literal ('draft'), never model output: asserts against the
    cfg_enum, like _validate_stage."""
    valid = {r[0] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.status' AND inactive=0")}
    if status not in valid:
        raise ValueError(f"status {status!r} not in live cfg_enum ib_observation.status {sorted(valid)}")


def _insert_observation(conn, cluster_code: str, stage: str, tag: str, strong: str | None,
                        question_code: str | None, obs_text: str, meaning_source: str | None,
                        source_json_serial: int | None, subgroup_id: int | None = None,
                        supersedes_observation_id: int | None = None,
                        meaning_keywords: list[str] | None = None) -> int:
    window = _window_for(conn, question_code)
    _assert_valid_ib_status(conn, "draft")
    keywords_json = json.dumps(meaning_keywords, ensure_ascii=False) if meaning_keywords else None
    cur = conn.execute(
        "INSERT INTO ib_observation (cluster_code, stage, tag, strong, question_code, obs_text, "
        "meaning_source, status, supersedes_observation_id, source_json_serial, window, "
        "cluster_subgroup_id, meaning_keywords, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (cluster_code, stage, tag, strong, question_code, obs_text, meaning_source, "draft",
         supersedes_observation_id, source_json_serial, window, subgroup_id, keywords_json, _now()))
    return cur.lastrowid


def _keyword_match_candidate(conn, candidate: dict, new_keywords: set[str],
                             new_forms: set[tuple]) -> bool:
    """Structured-key match, used instead of prose similarity when the model supplies
    `meaning_keywords` (#1824: match surface, meaning keywords and morph). Both form and keywords must
    match: form alone could be a homonym in another sense, keywords alone two unrelated occurrences."""
    cand_keywords_raw = candidate["meaning_keywords"] if "meaning_keywords" in candidate.keys() else None
    if not cand_keywords_raw or not new_keywords:
        return False
    cand_keywords = set(json.loads(cand_keywords_raw))
    if not (cand_keywords & new_keywords):
        return False
    cand_forms = {(r["surface"], r["morph_code"]) for r in conn.execute(
        "SELECT DISTINCT surface, morph_code FROM ib_node WHERE observation_id=?",
        (candidate["id"],))}
    return bool(cand_forms & new_forms)


def _insert_node(conn, observation_id: int, cluster_code: str, strong: str | None,
                 verse_reference: str | None, surface: str | None, morph_code: str | None,
                 question_code: str | None, source_stage: str, seq: int,
                 traced_observation_id: int | None = None,
                 subgroup_code: str | None = None) -> int:
    cur = conn.execute(
        "INSERT INTO ib_node (observation_id, cluster_code, strong, verse_reference, surface, "
        "morph_code, question_code, traced_observation_id, source_stage, seq, "
        "cluster_subgroup_code, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (observation_id, cluster_code, strong, verse_reference, surface, morph_code, question_code,
         traced_observation_id, source_stage, seq, subgroup_code, _now()))
    return cur.lastrowid


def record_one_observation(conn, cluster_code: str, stage: str, obs: dict,
                           source_json_serial: int | None, subgroup_id: int | None = None,
                           subgroup_code: str | None = None,
                           similarity_threshold: float = SIMILARITY_THRESHOLD) -> dict:
    """One model-produced observation -> same/broaden/new decision -> DB write(s). Returns a small
    report dict. An unresolved occurrence is skipped and reported, not fatal to the observation.

    `subgroup_id`/`subgroup_code`: the caller's own subgroup for Stage 3/4 (char-reading/
    char-answers), written to ib_observation.cluster_subgroup_id / ib_node.cluster_subgroup_code.
    NULL for verse-reading and char-subgroup, per those columns' cfg_column.use."""
    strong = obs.get("strong")
    question_code = obs.get("question_code")
    tag = obs["tag"]
    obs_text = obs["obs_text"]
    try:
        meaning_source = normalise_meaning_source(conn, obs.get("meaning_source"))
    except InvalidMeaningSource as e:
        return {"action": "skipped-invalid-meaning-source", "unresolved": [str(e)]}

    _validate_stage(conn, stage)

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

    # word-level questions are filed with no cluster_code; others under the pass's cluster
    effective_cluster_code = _effective_cluster_code(conn, cluster_code, strong, question_code)

    claimed_occurrences = obs.get("occurrences", [])
    resolved_occurrences = []  # (occurrence_strong, resolved_dict) -- not always `strong`
    unresolved = []
    for occ in claimed_occurrences:
        occ_strong = occ.get("strong", strong)
        try:
            resolved_occurrences.append((occ_strong, resolve_occurrence(
                conn, occ_strong, occ["verse"], occ.get("surface"), occ.get("morph_code"))))
        except UnresolvedOccurrence as e:
            unresolved.append(str(e))
    # zero occurrences claimed is a legitimate whole-subgroup finding (written with no nodes);
    # occurrences claimed but none resolving is skipped and reported
    if not resolved_occurrences and claimed_occurrences:
        return {"action": "skipped-no-resolvable-occurrences", "unresolved": unresolved}

    # each occurrence keeps its own strong (subgroup-wide observations have strong=None)
    new_refs = {(occ_strong, o["verse_reference"]) for occ_strong, o in resolved_occurrences}

    # per-occurrence questions get their pool narrowed to this exact occurrence first
    candidates = _existing_candidates(conn, effective_cluster_code, stage, strong, question_code,
                                      occurrence_refs=new_refs)

    for cand in candidates:
        if cand["obs_text"] == obs_text:
            existing_refs = _existing_node_refs(conn, cand["id"])
            if new_refs <= existing_refs:
                return {"action": "no-op-exact-duplicate", "observation_id": cand["id"],
                       "unresolved": unresolved}

    new_keywords = set(obs.get("meaning_keywords") or [])
    traced = None

    if _is_per_occurrence_question(question_code):
        # Identity is structural: the pool is already scoped to the occurrence (M0.7 family) or the
        # verse (M0.6.5/M0.6.6/D7.7.1, single-fact-per-verse), so 2+ rows can only be duplicates of the
        # same fact. Keyword/similarity scoring is not used: meaning_keywords is free LLM text, not a
        # stable identity key (#1834). Word-level questions do not belong here (see below).
        if not candidates:
            observation_id = _insert_observation(
                conn, effective_cluster_code, stage, tag, strong, question_code, obs_text,
                meaning_source, source_json_serial, subgroup_id,
                meaning_keywords=sorted(new_keywords) if new_keywords else None)
            action = "new-observation"
        elif len(candidates) == 1:
            best = candidates[0]
            _assert_valid_ib_status(conn, "draft")
            conn.execute("UPDATE ib_observation SET obs_text=?, status=?, updated_at=? WHERE id=?",
                        (obs_text, "draft", _now(), best["id"]))
            observation_id = best["id"]
            action = "aligned-superficial-edit"
        else:
            # legacy duplication, cleaned up only when a fresh answer for this occurrence arrives (no
            # offline consolidation). Canonical = most citations, earliest created_at as tie-break.
            ranked = sorted(
                candidates,
                key=lambda c: (-len(_existing_node_refs(conn, c["id"])), c["created_at"]))
            canonical = ranked[0]
            duplicate_ids = [c["id"] for c in ranked[1:]]
            _assert_valid_ib_status(conn, "draft")
            conn.execute("UPDATE ib_observation SET obs_text=?, status=?, updated_at=? WHERE id=?",
                        (obs_text, "draft", _now(), canonical["id"]))
            _consolidate_duplicates(conn, canonical["id"], duplicate_ids)
            observation_id = canonical["id"]
            action = "aligned-superficial-edit-consolidated"
        # identity came from scoping, not similarity, so no score is reported
        best = None
        best_score = None
    elif _is_word_level_question(question_code):
        # each word-level answer is grounded in its own occurrence (#1849), so two candidates are not
        # assumed to be the same fact: an exact text match shares the observation; anything else is its
        # own distinct observation.
        exact = next((c for c in candidates if c["obs_text"] == obs_text), None)
        if exact is not None:
            observation_id = exact["id"]
            action = "aligned-exact-match"
        else:
            observation_id = _insert_observation(
                conn, effective_cluster_code, stage, tag, strong, question_code, obs_text,
                meaning_source, source_json_serial, subgroup_id,
                meaning_keywords=sorted(new_keywords) if new_keywords else None)
            action = "new-observation"
        best = None
        best_score = None
    else:
        # every other question type: cluster-wide pool, keyword/similarity decides update-vs-new
        new_forms = {(o["surface"], o["morph_code"]) for _, o in resolved_occurrences}
        best = None
        best_score = 0.0
        for cand in candidates:
            if new_keywords and _keyword_match_candidate(conn, cand, new_keywords, new_forms):
                best, best_score = cand, 1.0
                break
            score = _similarity(cand["obs_text"], obs_text)
            if score > best_score:
                best, best_score = cand, score

        if best is not None and best_score >= similarity_threshold:
            # edited text resets the review status to 'draft' (#1782)
            _assert_valid_ib_status(conn, "draft")
            conn.execute("UPDATE ib_observation SET obs_text=?, status=?, updated_at=? WHERE id=?",
                        (obs_text, "draft", _now(), best["id"]))
            observation_id = best["id"]
            action = "aligned-superficial-edit"
        elif best is not None:
            observation_id = _insert_observation(
                conn, effective_cluster_code, stage, tag, strong, question_code, obs_text,
                meaning_source, source_json_serial, subgroup_id,
                meaning_keywords=sorted(new_keywords) if new_keywords else None)
            action = "new-expands-existing"
            traced = best["id"]
        else:
            observation_id = _insert_observation(
                conn, effective_cluster_code, stage, tag, strong, question_code, obs_text,
                meaning_source, source_json_serial, subgroup_id,
                meaning_keywords=sorted(new_keywords) if new_keywords else None)
            action = "new-observation"

    _REUSES_OBSERVATION_ID = ("aligned-superficial-edit", "aligned-superficial-edit-consolidated")
    existing_refs = _existing_node_refs(conn, observation_id) if action in _REUSES_OBSERVATION_ID else set()
    # seq continues from this observation's current max (UNIQUE (observation_id, seq)); queried fresh,
    # so it sees this transaction's own writes and nodes re-pointed by _consolidate_duplicates
    if action in _REUSES_OBSERVATION_ID:
        seq = conn.execute(
            "SELECT COALESCE(MAX(seq), 0) FROM ib_node WHERE observation_id=?",
            (observation_id,)).fetchone()[0]
    else:
        seq = 0
    written_nodes = []
    for occ_strong, o in resolved_occurrences:
        ref = (occ_strong, o["verse_reference"])
        if ref in existing_refs:
            continue
        seq += 1
        # ib_node.cluster_code is the PASS that cited the occurrence (NOT NULL), not the observation's
        # effective_cluster_code, which is None for word-level questions
        node_id = _insert_node(
            conn, observation_id, cluster_code, occ_strong, o["verse_reference"],
            o["surface"], o["morph_code"], question_code, stage, seq, traced_observation_id=traced,
            subgroup_code=subgroup_code)
        written_nodes.append(node_id)

    return {"action": action, "observation_id": observation_id, "node_ids": written_nodes,
           "similarity_score": round(best_score, 3) if best is not None else None,
           "unresolved": unresolved}


def record_batch(conn, cluster_code: str, stage: str, model_output: dict,
                 source_json_serial: int | None = None, subgroup_id: int | None = None,
                 subgroup_code: str | None = None,
                 similarity_threshold: float = SIMILARITY_THRESHOLD) -> dict:
    """Every observation in one model reply, in the same unit of work. Caller commits.

    `unresolved_detail` carries the reason strings, not just a count; callers should log them.
    `subgroup_id`/`subgroup_code`: see `record_one_observation`; None for stages not scoped to one
    subgroup."""
    results = [record_one_observation(conn, cluster_code, stage, obs, source_json_serial,
                                      subgroup_id, subgroup_code, similarity_threshold)
              for obs in model_output.get("observations", [])]
    by_action: dict[str, int] = {}
    for r in results:
        by_action[r["action"]] = by_action.get(r["action"], 0) + 1
    unresolved_detail = [msg for r in results for msg in r.get("unresolved", [])]
    return {"results": results, "by_action": by_action,
           "unresolved_occurrence_count": len(unresolved_detail),
           "unresolved_detail": unresolved_detail}


STRAND_STAGE, STRAND_TAG = "strand-reading", "key-statement"
STRAND_PARTS = ("setting", "meaning", "implication", "chain", "basis", "parties")


def record_strand_observations(conn, cluster_code: str, run_id: str, observations: list[dict]) -> dict:
    """The observations of one strand reading (#2172 step 2): one row per key statement, the October
    ledger's parts as columns, grounded by one ib_node per verse and strong. Each observation's
    `occurrences` are resolved by the caller with resolve_occurrence() before anything is written.
    `supersedes` (an observation id) withdraws the earlier row, naming the new one. Caller commits.
    Returns {key: observation id}."""
    _validate_stage(conn, STRAND_STAGE)
    _validate_tag(conn, STRAND_TAG)
    ids = {}
    for o in observations:
        _validate_obs_text(conn, o["text"])
        strongs = {occ["strong"] for occ in o["occurrences"]}
        oid = _insert_observation(conn, cluster_code, STRAND_STAGE, STRAND_TAG,
                                  strongs.pop() if len(strongs) == 1 else None, None, o["text"],
                                  "verse-text", None, supersedes_observation_id=o.get("supersedes"))
        conn.execute(f"UPDATE ib_observation SET {', '.join(p + '=?' for p in STRAND_PARTS)}, run_id=? WHERE id=?",
                     [o.get(p) for p in STRAND_PARTS] + [run_id, oid])
        for seq, occ in enumerate(o["occurrences"]):
            _insert_node(conn, oid, cluster_code, occ["strong"], occ["verse_reference"], occ["surface"],
                         occ["morph_code"], None, STRAND_STAGE, seq)
        if o.get("supersedes"):
            conn.execute("UPDATE ib_observation SET status='withdrawn', revisit_note=?, updated_at=? WHERE id=?",
                         (f"superseded by observation {oid} (run {run_id})", _now(), o["supersedes"]))
        ids[o["key"]] = oid
    return ids


def set_disposition(conn, observation_id: int, status: str, note: str | None, run_id: str) -> None:
    """An observation's disposition (#2172 design decision 5): resolved (a claim carries it), open
    (held as a thread item), silent or withdrawn; the reason or the item goes in revisit_note."""
    _assert_valid_ib_status(conn, status)
    conn.execute("UPDATE ib_observation SET status=?, revisit_note=?, run_id=?, updated_at=? WHERE id=?",
                 (status, note, run_id, _now(), observation_id))


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
