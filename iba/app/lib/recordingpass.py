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


SIMILARITY_THRESHOLD = 0.85  # fallback default only (escalation #1753 B3) -- live callers pass
                              # cfg_setting cluster.recording_similarity_threshold instead; this
                              # constant is what a caller gets if it omits similarity_threshold
                              # entirely (e.g. a one-off migration).


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
    """M0.7.1-16 and M0.8.1 -- explicitly about "[this word]" (versereadinggenerate.py's own
    prompt text), a genuinely word-specific finding even though it's per-verse not per-strong-ever.
    M0.8.1 (#1836, 2026-09-22, T2/T3 elevation-candidate) joins this family for the same reason:
    it is a fact about ONE specific non-M-code word's own candidacy, never a shared verse-level
    fact multiple words could co-report (unlike M0.6.5/M0.6.6/D7.7.1). Identity for these stays
    exact (verse, strong) occurrence -- count-based same/broaden/new (#1824 v10/v11 Fix 1/2),
    unchanged by the #1824 v22 cross-strong fix below.

    M0.5.11 joins this family, 2026-09-23: caught live while extending the word-level (M0.1/M0.5)
    branch to structural matching -- its own text is "In this verse, where this occurrence's
    meaning diverges from the term's usual sense elsewhere..." -- exactly this family's shape
    (per-verse, word-specific, genuinely varies occurrence to occurrence), not a once-ever-per-
    strong fact. It only ever matched `_WORD_LEVEL_QUESTION_PREFIXES`' bare "M0.5" prefix, which
    was never meant to catch it. Confirmed live before fixing: H1245 (baqash) alone had 148 live
    M0.5.11 rows, each about a genuinely different verse -- forcing the word-level branch's "2+
    candidates = same fact" rule over this pool would have wrongly consolidated 147 distinct
    findings into one. Caught in verification, never run live."""
    return bool(question_code) and (
        question_code.startswith("M0.7") or question_code in ("M0.8.1", "M0.5.11"))


def _is_per_occurrence_question(question_code: str | None) -> bool:
    """#1824 v10 (design doc `iba/docs/1824-stage1-reconciliation-design-v1-20260922.md`, Fix 1):
    M0.7.*/M0.8.1 and the relational questions are explicitly per-verse -- 'a strong can genuinely
    behave differently verse to verse' (BUILD #310) -- as opposed to M0.1/M0.5's word-level, verse-
    invariant facts. #1840, 2026-09-22: this used to restate `question_code.startswith("M0.7")`
    itself rather than calling `_is_strong_specific_occurrence_question` -- when M0.8.1 joined that
    family (#1836), only THIS function's own copy of the condition was updated to include it, not
    the one below, so M0.8.1 silently fell through to the word-level keyword/similarity branch
    instead of the exact-occurrence count-based one. Confirmed live: Ezra.7.17/H9010/M0.8.1 has 3
    `ib_observation` rows all citing the SAME single node (surface='bulls'), chained via
    `traced_observation_id` -- the tell-tale sign of the word-level "new-expands-existing" path,
    not genuine distinct occurrences. Delegating to the single strong-specific predicate below
    (rather than keeping two hand-written copies of the same set) is the actual fix "prevent it
    going forward" asks for -- the two conditions can no longer drift apart because there is only
    one of them."""
    if not question_code:
        return False
    return (_is_strong_specific_occurrence_question(question_code) or
           question_code in _VERSE_LEVEL_OCCURRENCE_CODES)


def _is_verse_level_occurrence_question(question_code: str | None) -> bool:
    """M0.6.5/M0.6.6/D7.7.1 -- researcher instruction 2026-09-22 (escalation #1832), verbatim:
    "near duplicates are not allowed. this applies across clusters and strongs." ... "duplication
    across questions should not be eliminated, however, near duplication within a question is an
    issue." Investigated live: these three ARE genuinely verse-level facts asked redundantly once
    per M-code strong present (D7.7.1's operation word, M0.6.6's whole-network composition are the
    SAME fact regardless which strong "asks"; M0.6.5's own progressive-per-word design still
    produces heavy content overlap even though each strong's own vantage clause differs) --
    confirmed live: 20/23/18 separate observations across just a 5-verse test, one per (verse,
    strong), none ever sharing a citation, because `_existing_candidates` hard-filtered by
    strong+cluster_code for every per-occurrence question including these three. Candidate pool
    for these three is now verse-scoped only (any strong, any cluster) -- identity is no longer
    "guaranteed same fact by exact occurrence match" (M0.7's own reasoning), so matching uses the
    same keyword/similarity mechanism word-level questions already use, not count-based 0/1/>1;
    a genuinely distinct per-word contribution (e.g. M0.6.5's own vantage) scores low and is kept
    as its own new-expands-existing row, never forced to merge."""
    return question_code in _VERSE_LEVEL_OCCURRENCE_CODES


def _existing_candidates(conn, cluster_code: str, stage: str, strong: str | None,
                         question_code: str | None,
                         occurrence_refs: set[tuple] | None = None) -> list[dict]:
    """#1824 v10, Fix 1 -- researcher's own question: "how do you know what row to expect."
    Checked live and confirmed a real gap: this pool used to be cluster+stage+strong+question_code
    ONLY, no verse filter, for every question type -- correct for word-level questions (a fact
    about the strong, not any one verse) but wrong for per-occurrence ones, where it let a fresh
    answer get compared against a candidate from a COMPLETELY DIFFERENT VERSE (confirmed: 22 of 61
    matches in a live test traced cross-verse). For M0.7 (strong-specific), first narrow to
    candidates that already have an `ib_node` citation for one of THIS observation's own
    (strong, verse_reference) occurrence pairs -- a direct lookup answering "does a row for this
    occurrence exist," not a heuristic guess left to keyword/similarity scoring downstream.

    #1832, 2026-09-22 -- for M0.6.5/M0.6.6/D7.7.1 (verse-level occurrence questions), `strong` and
    `cluster_code` are BOTH dropped from the filter: the researcher's own instruction ("near
    duplicates are not allowed... applies across clusters and strongs... duplication across
    questions should not be eliminated, however, near duplication within a question is an issue")
    scopes the candidate pool to stage+question_code+VERSE only, any strong, any cluster's pass.
    #1832 v2 correction: identity within this pool is NOT decided by keyword/similarity scoring
    (tried first, failed live -- `meaning_keywords` is freely LLM-generated, not a stable identity
    key across separate calls) -- these three are architecturally single-fact-per-verse questions,
    so `record_one_observation` treats "2+ candidates in this pool" as guaranteed same-fact legacy
    duplication, same count-based logic M0.7 already uses."""
    # `o.` prefix throughout -- both ib_observation and ib_node carry a cluster_code column, so an
    # unqualified reference is ambiguous the moment the JOIN branch below is used (found live:
    # "OperationalError: ambiguous column name: cluster_code" on the first real test of this).
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
    # cluster_code=None (word-level M0.1/M0.5, 2026-09-23 ruling) needs "IS NULL", not "=?" --
    # SQL NULL never equals NULL via "=?", so passing None as a bound param here would silently
    # match ZERO existing rows on every call, breaking word-level identity entirely (every answer
    # would look "new," never recognised as already-covered). Same IS-NULL pattern already used
    # below for strong/question_code, applied here for the same reason.
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
    """#1824 v10/v11, Fix 2 rule 3 -- called ONLY when a real fresh answer for an exact occurrence
    (per Fix 1's own correct scoping) finds MORE than one pre-existing candidate: legacy
    duplication from before Fix 1 existed. Soft-withdraws the duplicates (never a physical delete,
    matching the project's existing soft-delete convention) and re-points their `ib_node`
    citations onto the canonical so no occurrence record is lost.

    Deliberately does NOT use `ib_observation.supersedes_observation_id` -- checked its own
    `cfg_column.use` before touching it (per `governance.table_columns`) and it reads "synthesis
    stage only, ... the append-only supersedes chain": a different stage's own column, not this
    one's to repurpose. Same principle BUILD #312 already applied this session (a genuinely new
    column for `meaning_keywords` rather than overloading `stable_key`'s unrelated documented
    purpose) -- `status='withdrawn'` alone (a value this column's own use-text already lists:
    "observation is incorrect or not useful") is sufficient for Stage 1's own needs; which
    observation now holds an occurrence's citations is reconstructable from `ib_node` directly,
    without a forward pointer this table's own governance doesn't authorise here."""
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
    """M0.1.x/M0.5.x -- a fact about the STRONG alone. Researcher ruling, 2026-09-23 (escalation
    #1849 follow-on, verbatim: "cluster has no role to play, the keys for further analysis is
    strong and verse"): these questions no longer carry any cluster/characteristic framing (see
    the 2026-09-23 catalogue reword) and no longer resolve or need a cluster_code at all -- one
    canonical `ib_observation` per (strong, question_code), full stop, `cluster_code IS NULL`.

    EXCLUDES M0.5.11 despite the "M0.5" prefix match -- it is a strong-specific OCCURRENCE
    question (see `_is_strong_specific_occurrence_question`'s own docstring), not a once-ever
    word-level fact; routed there instead, checked explicitly here so the two predicates can never
    silently overlap."""
    return (bool(question_code) and question_code.startswith(_WORD_LEVEL_QUESTION_PREFIXES)
           and not _is_strong_specific_occurrence_question(question_code))


def _effective_cluster_code(conn, pass_cluster_code: str, strong: str | None,
                            question_code: str | None) -> str | None:
    """Word-level (M0.1/M0.5) observations carry NO cluster_code at all as of 2026-09-23 (see
    `_is_word_level_question`) -- these are strong-only facts, and resolving any cluster for them
    (even the strong's own "true" M-code, as this function used to do pre-2026-09-23 per #1815)
    re-introduces exactly the dependency the researcher's ruling removed. Every other question
    type (relational M0.6.5/M0.6.6/D7.7.1, per-occurrence M0.7/M0.8.1) stays keyed to the PASS's
    own cluster_code, unchanged -- only which cluster nominally "owns" the row's `cluster_code`
    column, not whether the row itself can merge (`_existing_candidates`'s verse-level branch
    already merges across clusters on content, not cluster identity, per #1832)."""
    if _is_word_level_question(question_code):
        return None
    return pass_cluster_code


def _window_for(conn, question_code: str | None) -> str | None:
    """window is DERIVED from the catalogue question, never invented ad hoc (#1723 -- the old
    #1691 definition duplicated `stage`; the new one is the question's own registered angle).
    Cross-checked against the live cfg_enum, added 2026-09-20 (escalation #1796):
    ib_observation.window is a registered cfg_enum group, but the actual value always came from
    wa_obs_question_catalogue.window with nothing ever checking the two stay in sync -- a typo or
    stale row in the catalogue could silently write a window value the enum doesn't even list."""
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


# NOT adding an ib_observation.meaning_source validator here (checked live 2026-09-20, escalation
# #1796, before writing one): 37+ distinct free-form strings are already live against this 3-value
# enum (e.g. "strong_meaning_tree; lsj; mounce", "role list", "cluster_codes") -- enforcing the
# clean 3 values at write time would skip-and-discard nearly every future observation that sets
# this field. Deliberately left as a genuine, still-open orphan rather than papering over it with a
# dormant function that would fool the orphan-checker's text scan without actually protecting
# anything (a real risk: the checker only greps for the lookup TEXT, not whether it's ever called).
# This is exactly escalation #1771's own open question (redesigning the field's shape) -- surfaced
# there with this concrete measurement, not decided here.


def _validate_stage(conn, stage: str) -> None:
    """stage is caller-supplied (a Python literal naming the calling pipeline stage), never model-
    output -- a mismatch here is a programming bug, not a data-quality finding, so this asserts
    (ValueError) rather than the soft skip-and-report convention used for the model-supplied fields
    above. Added live 2026-09-20 (escalation #1796): ib_observation.stage was a registered cfg_enum
    group nothing ever looked up by name at runtime. Queried fresh each call, same as
    _validate_tag/_validate_question_code above -- not cached, for the same reason they aren't."""
    valid = {r[0] for r in conn.execute(
        "SELECT value FROM cfg_enum WHERE name='ib_observation.stage' AND inactive=0")}
    if stage not in valid:
        raise ValueError(f"stage {stage!r} not in live cfg_enum ib_observation.stage {sorted(valid)}")


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


def _assert_valid_ib_status(conn, status: str) -> None:
    """status is a fixed internal literal at both call sites below ('draft'), never model-output --
    same rationale as _validate_stage: an assertion catching a future typo/drift, not a data-quality
    soft-skip. Added 2026-09-20 (escalation #1796): ib_observation.status was a registered cfg_enum
    group nothing ever looked up by name at runtime."""
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
    """#1824, researcher instruction verbatim: "similarity is not matching sentences. Similarly
    to matching keys... match a) surface b) meaning extraction keywords c) morph." Structured-key
    match, used instead of prose similarity when the model supplies `meaning_keywords` -- BOTH
    conditions must hold, not either alone: matching grammatical form alone (a homonym reused with
    a different sense) isn't enough, and matching keywords alone (two unrelated occurrences that
    happen to share a concept word) isn't enough either."""
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
    """One model-produced observation -> same/broaden/new decision -> DB write(s). Returns a
    small report dict for the caller's own summary, never raises on an unresolved occurrence for
    the WHOLE observation -- only the individual bad occurrence is skipped and reported, per
    checklist rule 0.7 ("a gap is a load-time finding, not silently accepted") -- surfaced, not
    fatal to the rest of the batch.

    `subgroup_id`/`subgroup_code` are the CALLER's own known subgroup (Stage 3/4 are scoped to
    exactly one subgroup by construction -- no lookup or inference needed, the caller already
    knows it). Found live 2026-09-18 (researcher's own review of the data): `ib_observation.
    cluster_subgroup_id`/`ib_node.cluster_subgroup_code` are real, already-registered columns
    (`cfg_column`) this module had never populated at all, for any of the 4 live stages. Per their
    own `cfg_column.use` text, both stay NULL for stage=verse-reading (pre-subgroup) and
    stage=char-subgroup (process (b)'s own cluster-level observations, "above single-subgroup
    scope") -- correct by construction here since neither of those call sites passes a value;
    Stage 3/4 (char-reading/char-answers) now pass their own subgroup explicitly."""
    strong = obs.get("strong")
    question_code = obs.get("question_code")
    tag = obs["tag"]
    obs_text = obs["obs_text"]
    meaning_source = obs.get("meaning_source")

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

    # meaning_source is deliberately NOT validated here -- see this file's own note near
    # ib_observation.meaning_source above for why (massive live drift from the 3-value enum,
    # escalation #1796/#1771).

    # #1723: a word-level (M0.1/M0.5) observation is filed under the STRONG's own actual M-code,
    # not the pass's cluster_code -- lets a later cluster's own pass find it as already covered
    # regardless of which cluster's pass originally front-loaded it.
    effective_cluster_code = _effective_cluster_code(conn, cluster_code, strong, question_code)

    claimed_occurrences = obs.get("occurrences", [])
    resolved_occurrences = []  # list of (occurrence_strong, resolved_dict) -- NOT always `strong`
    unresolved = []
    for occ in claimed_occurrences:
        occ_strong = occ.get("strong", strong)
        try:
            resolved_occurrences.append((occ_strong, resolve_occurrence(
                conn, occ_strong, occ["verse"], occ.get("surface"), occ.get("morph_code"))))
        except UnresolvedOccurrence as e:
            unresolved.append(str(e))
    # Found live 2026-09-18, Stage 4's first real run: a genuine whole-subgroup NEGATIVE finding
    # ("no evidence of X across this subgroup's material") legitimately cites no occurrence at all
    # -- its own evidence is the accumulated Stage 1/2/3 material it was given as input, already
    # grounded elsewhere, not a specific verse. Treating that the same as "the model cited verses
    # that don't resolve" (a REAL data-quality problem, still skipped below) silently discarded 10
    # substantive answers on the very first char-answers run. Distinguish by cause: the model
    # provided zero occurrences (write it, 0 ib_node rows) vs. it provided some and NONE resolved
    # (skip and report, unchanged). Harmless for Stages 1-3, which have never sent an empty
    # `occurrences` list in practice (every claim they make is tied to a specific given verse).
    if not resolved_occurrences and claimed_occurrences:
        return {"action": "skipped-no-resolvable-occurrences", "unresolved": unresolved}

    # Found live 2026-09-18 building Stage 4 (checklist §3 rule 3, subgroup-wide slants with
    # `strong: null` on the observation but a real strong per occurrence): using the OUTER
    # `strong` here (as before) would collapse every occurrence's ref to (None, verse), and
    # `_insert_node` below would then write ib_node.strong=NULL for every occurrence regardless of
    # which member strong it actually belongs to -- silently losing exactly the per-occurrence
    # strong attribution the whole point of a subgroup-wide observation depends on. Harmless for
    # Stages 1-3 (their occurrences never set their own "strong", so occ_strong == strong always,
    # identical behaviour to before).
    new_refs = {(occ_strong, o["verse_reference"]) for occ_strong, o in resolved_occurrences}

    # #1824 v10, Fix 1: per-occurrence questions get their candidate pool narrowed to this exact
    # occurrence BEFORE any matching runs (computed from new_refs, just moved up so it's available
    # here) -- word-level questions are unaffected (occurrence_refs is simply unused for them).
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
        # #1824 v10/v11 Fix 2 (M0.7, exact verse+strong identity) and #1832 v2, 2026-09-22
        # correction (M0.6.5/M0.6.6/D7.7.1, verse+question identity, no strong): identity for
        # EVERY per-occurrence question is now structural, not a keyword/similarity judgement
        # call. `_existing_candidates` already scopes the pool correctly per question type (exact
        # occurrence for M0.7; verse-only, any strong/cluster for the other three) -- given that
        # pool, "2+ existing rows" can ONLY mean legacy duplication of the identical fact, by
        # construction (M0.7: same word, same verse, same question, nothing else it could be;
        # M0.6.5/M0.6.6/D7.7.1: these are architecturally single-fact-per-verse questions -- one
        # operation word, one whole-network composition, one progressive relational synthesis --
        # so multiple strongs asking the same question about the same verse are describing the
        # SAME fact, not independently-different ones). #1832's first attempt used keyword/
        # similarity scoring here instead and failed live testing: `meaning_keywords` is freely
        # LLM-generated text, not a stable identity key -- two independent calls describing the
        # identical fact produced disjoint keyword sets (confirmed: 2Cor.8.7/D7.7.1, zero overlap
        # between "corinthians-initiate/excel-operation/object-of-increase" and "Corinthians-
        # excel/self-directed-growth" for the SAME underlying finding), so a rerun added a new
        # unmerged duplicate instead of clearing anything -- 0 rows withdrawn on a 5-verse live
        # test. Escalation #1834. Count-based matching sidesteps the unstable-keyword problem
        # entirely: no text judgement needed when the pool itself already guarantees "same fact."
        #
        # NOTE: word-level (M0.1/M0.5) questions do NOT belong in this branch, even briefly (an
        # earlier pass this same session put them here, caught and reverted before shipping) --
        # their candidate pool (exact strong+question_code, any VERSE) does NOT guarantee "2+ rows
        # = same fact" the way the exact-occurrence pools above do: two independently span-grounded
        # answers for the same term CAN legitimately differ by occurrence (researcher, 2026-09-23).
        # See the `_is_word_level_question` branch below for their own exact-text-match logic.
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
            # Legacy duplication (multiple existing rows for the SAME occurrence+question, from
            # before Fix 1 existed) -- only discovered and only cleaned up because a real fresh
            # answer just arrived for this exact occurrence (design doc §3, governing principle:
            # no offline consolidation, ever). Canonical = most existing citations (richest),
            # earliest created_at as the deterministic tie-break.
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
        # No similarity score applies here -- identity came from Fix 1's exact-occurrence
        # scoping, not a keyword/similarity comparison. `best`/`best_score` stay None so the
        # return below reports similarity_score=None for every per-occurrence action, honestly.
        best = None
        best_score = None
    elif _is_word_level_question(question_code):
        # 2026-09-23, researcher correction (escalation #1849 follow-on, verbatim): "Every word
        # observation answer must be at span (word in verse context) level. Saying that you can
        # resolve the observation question without looking at the verse/span/morph means it is a
        # generic answer." Generation for these questions now happens per occurrence (the
        # front-loading skip that used to prevent this is retired -- see versereadinggenerate.py),
        # so two candidates in this pool are NOT guaranteed to be the same fact the way the
        # exact-occurrence families above are: a genuinely different occurrence of the same term
        # may show a genuinely different aspect. Identity here is EXACT TEXT MATCH ONLY, never
        # assumed sameness by count -- deliberately the stricter, more conservative choice given
        # this exact codebase's own lesson (escalation #1834) that fuzzy/keyword matching on
        # freely-generated text is unreliable: an exact match is genuine independently-grounded
        # convergence (share it, add this occurrence's node); anything else is kept as its own
        # distinct observation, never force-merged on the assumption it "must really be the same."
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
        # Every other question type (char-reading/char-answers free-form synthesis, science
        # questions, anything with no dedicated identity rule above): unchanged from before --
        # cluster-wide candidate pool, keyword/similarity matching decides update-vs-new exactly
        # as it did prior to #1824 v10. NOT used by word-level (M0.1/M0.5) any more -- see the
        # dedicated branch above.
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
            # Researcher instruction, 2026-09-20 (escalation #1782): editing an existing
            # observation's text invalidates whatever review state it had (e.g. resolved) --
            # reset to 'draft' so it is re-reviewed, same as a brand-new observation, rather than
            # silently keeping a stale status against changed content.
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
    # seq must continue from this observation_id's own current max, not restart at 0 -- UNIQUE
    # (observation_id, seq) fails otherwise the moment a LATER batch/call appends a new occurrence
    # to an observation an EARLIER batch/call already wrote nodes against (the "aligned-superficial-
    # edit" path, the only one that reuses an existing observation_id rather than inserting a fresh
    # one). Found live 2026-09-18: M49's Stage 1 run hit this on its first real multi-batch verse-
    # reading pass. Queried fresh each call (not cached) so it sees writes from this same
    # transaction too, same "resolve fresh, never trust a stale count" discipline this module
    # already applies to strong/verse resolution. The "-consolidated" variant (#1824 v10/v11)
    # reuses observation_id the same way -- `_consolidate_duplicates` already re-pointed the
    # duplicates' own nodes onto it before this line runs, so MAX(seq) here already accounts for
    # them.
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
        node_id = _insert_node(
            conn, observation_id, effective_cluster_code, occ_strong, o["verse_reference"],
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
    """Every observation in one model reply, in the same unit of work (checklist rule 0.3: assemble
    -> run -> record fires immediately after, never a deferred batch pickup). Caller commits.

    `unresolved_detail` carries the actual reason strings, not just a count (found live 2026-09-17,
    twice -- BUILD.md #274 first flagged this as a gap for Stage 1, then it directly cost real
    diagnostic ability redoing Stage 2's M67 run: a whole observation's citation failure was
    reported only as a bare number, with no way afterward to tell whether it was a real defect or
    an ordinary LLM verse-citation slip, short of a fresh, non-reproducible, real-money re-call).
    Every caller should log/persist this, not just the count.

    `subgroup_id`/`subgroup_code`: pass the caller's own known subgroup for a per-subgroup stage
    (Stage 3/4) -- see `record_one_observation`'s own docstring. Omitted (None) for stages not
    scoped to one subgroup (verse-reading, char-subgroup), which is the correct value for them."""
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
