"""stage1coverage.py — deterministic expected-vs-actual coverage validation for Stage 1
(`lexical.meaning` + `lexical.relational`, #1824): the expected result is computed for each scope
and the LLM's result measured against it.

  expected_nodes(conn, cluster_code, verse_ids, family=None) — the (verse, strong, question_code)
      triples Stage 1 should attempt for this scope, from live `verse_lexical` role data, without
      calling the LLM. Uses the same population rules as `versereadinggenerate.py`, with question
      codes from the live catalogue query each call.

  validate_coverage(conn, cluster_code, verse_ids, family=None) — compares that set against the
      live `ib_node`/`ib_observation` state (`stage='verse-reading'`, non-withdrawn): MISSING
      (expected, no live node), UNEXPECTED (live node, not expected), OVER_COUNT (expected once, >1
      live node/observation: an unreconciled duplicate), OK.

`family` (#1860): `None` = every wired question code (used by
`clusterstatus.verse_reading_completeness` and anything scope-agnostic); `'word_level'` = `M0.1`/
`M0.5` (`lexical.meaning`); `'relational'` = `M0.6.5`/`M0.6.6`/`D7.7.1`/`M0.7`/`M0.8.1`
(`lexical.relational`). Each step's post-run `validate_coverage` passes its own family.
"""

from __future__ import annotations

import json
import sqlite3
from collections import Counter

_WORD_LEVEL_PREFIXES = ("M0.1", "M0.5")
_RELATIONAL_EXACT_CODES = ("D7.7.1", "M0.6.5", "M0.6.6", "M0.8.1")


def _wired_question_codes(conn: sqlite3.Connection, family: str | None = None
                          ) -> tuple[list[str], list[str]]:
    """(word_level_codes, per_occurrence_m07_codes) -- the Stage 1 catalogue selection, the same query
    `versereadinggenerate.py` runs. `family='word_level'` returns (word_level_codes, []);
    `'relational'` returns ([], m07_codes). The other relational codes (`D7.7.1`/`M0.6.5`/`M0.6.6`/
    `M0.8.1`) are handled directly in `expected_nodes`."""
    rows = conn.execute(
        "SELECT question_code FROM wa_obs_question_catalogue "
        "WHERE deleted=0 AND (question_code LIKE 'M0.1%' OR question_code LIKE 'M0.5%' "
        "OR question_code LIKE 'M0.7%' "
        "OR question_code IN ('D7.7.1', 'M0.6.5', 'M0.6.6', 'M0.8.1')) "
        "ORDER BY question_code").fetchall()
    codes = [r["question_code"] for r in rows]
    word_level = [c for c in codes if c.startswith(_WORD_LEVEL_PREFIXES)]
    m07 = [c for c in codes if c.startswith("M0.7")]
    if family == "word_level":
        return word_level, []
    if family == "relational":
        return [], m07
    return word_level, m07


def expected_nodes(conn: sqlite3.Connection, cluster_code: str, verse_ids: list[int],
                   family: str | None = None) -> list[dict]:
    """Every row has: verse_reference, strong, surface, morph_code, is_home_strong, question_code,
    reason. verse_ids in the caller's processing order. `family`: see the module docstring."""
    if not verse_ids:
        return []
    word_level_codes, m07_codes = _wired_question_codes(conn, family)
    want_word_level = family in (None, "word_level")
    want_relational = family in (None, "relational")

    ph = ",".join("?" * len(verse_ids))
    verse_rows = conn.execute(
        f"SELECT id, osisId FROM verse WHERE id IN ({ph})", verse_ids).fetchall()
    osis_by_id = {r["id"]: r["osisId"] for r in verse_rows}

    lex_rows = conn.execute(
        f"SELECT verse_id, strong, surface, morph_code, role FROM verse_lexical "
        f"WHERE verse_id IN ({ph}) AND deleted=0 ORDER BY verse_id, position", verse_ids).fetchall()
    by_verse: dict[int, list[dict]] = {}
    for r in lex_rows:
        roles = json.loads(r["role"]) if r["role"] else []
        by_verse.setdefault(r["verse_id"], []).append(
            {"strong": r["strong"], "surface": r["surface"], "morph_code": r["morph_code"],
             "roles": roles})

    all_m_strongs: set[str] = set()
    for vid in verse_ids:
        for w in by_verse.get(vid, []):
            if w["strong"] and any(c.startswith("M") for c in w["roles"]):
                all_m_strongs.add(w["strong"])

    # word-level (M0.1/M0.5) questions are expected for every M-code strong in every verse it occurs
    # in, like the other families: each answer is grounded in its own occurrence (#1849); matching
    # answers are consolidated by recordingpass.py at write time

    rows_out: list[dict] = []
    for vid in verse_ids:
        osis = osis_by_id.get(vid)
        if osis is None:
            continue
        words = by_verse.get(vid, [])
        m_strongs_here_raw = [w for w in words if w["strong"] and any(c.startswith("M") for c in w["roles"])]
        # dedupe by (strong, surface, morph_code) (#1865): two occurrences of a strong in one verse with
        # identical surface and morph cannot be told apart, so they are one fact; a different surface or
        # morph stays a separate entry
        seen_occ: set[tuple] = set()
        m_strongs_here = []
        for w in m_strongs_here_raw:
            key = (w["strong"], w["surface"], w["morph_code"])
            if key in seen_occ:
                continue
            seen_occ.add(key)
            m_strongs_here.append(w)
        has_t3 = any("T3" in w["roles"] for w in words)

        if want_relational:
            for w in m_strongs_here:
                for qc in m07_codes:
                    rows_out.append({
                        "verse_reference": osis, "strong": w["strong"], "surface": w["surface"],
                        "morph_code": w["morph_code"],
                        "is_home_strong": cluster_code in w["roles"], "question_code": qc,
                        "reason": "per-occurrence, always expected"})

        if want_word_level:
            for w in m_strongs_here:
                for qc in word_level_codes:
                    rows_out.append({
                        "verse_reference": osis, "strong": w["strong"], "surface": w["surface"],
                        "morph_code": w["morph_code"],
                        "is_home_strong": cluster_code in w["roles"], "question_code": qc,
                        "reason": "span-grounded, always expected (2026-09-23)"})

        # cluster-agnostic (#1824): every M-code strong in the verse, for every family; `is_home_strong`
        # is descriptive only, never a filter
        if want_relational:
            for w in m_strongs_here:
                rows_out.append({
                    "verse_reference": osis, "strong": w["strong"], "surface": w["surface"],
                    "morph_code": w["morph_code"], "is_home_strong": cluster_code in w["roles"],
                    "question_code": "M0.6.5", "reason": "relational, always expected"})

        # M0.6.6 and D7.7.1 are always attempted: the catalogue says "record none" when the condition is
        # absent, so a negative finding is a real answer. D7.7.1 needs only an operation word present
        # (no party-tag requirement).
        if want_relational:
            for w in m_strongs_here:
                rows_out.append({
                    "verse_reference": osis, "strong": w["strong"], "surface": w["surface"],
                    "morph_code": w["morph_code"], "is_home_strong": cluster_code in w["roles"],
                    "question_code": "M0.6.6", "reason": "whole-network, always expected"})

        if want_relational and has_t3:
            for w in m_strongs_here:
                rows_out.append({
                    "verse_reference": osis, "strong": w["strong"], "surface": w["surface"],
                    "morph_code": w["morph_code"], "is_home_strong": cluster_code in w["roles"],
                    "question_code": "D7.7.1",
                    "reason": "operation-permeability, T3 operation word present"})

        # M0.8.1 (#1836): words with a T2/T3 role but no M-code role at all (a word with both is already
        # its own characteristic)
        if want_relational:
            elevation_words_raw = [w for w in words if w["strong"]
                                  and not any(c.startswith("M") for c in w["roles"])
                                  and any(c in ("T2", "T3") for c in w["roles"])]
            seen_elev: set[tuple] = set()
            elevation_words = []
            for w in elevation_words_raw:
                key = (w["strong"], w["surface"], w["morph_code"])
                if key in seen_elev:
                    continue
                seen_elev.add(key)
                elevation_words.append(w)
            for w in elevation_words:
                rows_out.append({
                    "verse_reference": osis, "strong": w["strong"], "surface": w["surface"],
                    "morph_code": w["morph_code"], "is_home_strong": False,
                    "question_code": "M0.8.1",
                    "reason": "T2/T3 elevation-candidate check, always expected for non-M-code role words"})

    return rows_out


def _question_codes_for_family(conn: sqlite3.Connection, family: str | None) -> list[str] | None:
    """The flat code list a `family` covers, so validate_coverage's "existing" query is scoped like
    `expected_nodes`. `None` -> None (no filter)."""
    if family is None:
        return None
    word_level, m07 = _wired_question_codes(conn, None)
    if family == "word_level":
        return word_level
    if family == "relational":
        return m07 + list(_RELATIONAL_EXACT_CODES)
    raise ValueError(f"unknown family {family!r}")


def validate_coverage(conn: sqlite3.Connection, cluster_code: str, verse_ids: list[int],
                      family: str | None = None) -> dict:
    """Compares expected_nodes() against the live ib_node/ib_observation state for the same scope
    (stage='verse-reading', non-withdrawn). Returns counts plus capped sample keys per category; the
    full detail belongs in a persisted report. `family` scopes both sides."""
    expected = expected_nodes(conn, cluster_code, verse_ids, family)
    expected_keys = Counter(
        (r["verse_reference"], r["strong"], r["question_code"]) for r in expected)

    family_codes = _question_codes_for_family(conn, family)
    osis_list = [r["osisId"] for r in conn.execute(
        f"SELECT osisId FROM verse WHERE id IN ({','.join('?'*len(verse_ids))})", verse_ids)]
    existing_keys: Counter = Counter()
    if osis_list:
        ph = ",".join("?" * len(osis_list))
        if family_codes is not None:
            cph = ",".join("?" * len(family_codes))
            rows = conn.execute(
                f"SELECT n.verse_reference, n.strong, n.question_code "
                f"FROM ib_node n JOIN ib_observation o ON o.id = n.observation_id "
                f"WHERE o.stage='verse-reading' AND o.deleted=0 "
                f"AND n.verse_reference IN ({ph}) AND n.question_code IN ({cph})",
                (*osis_list, *family_codes)).fetchall()
        else:
            rows = conn.execute(
                f"SELECT n.verse_reference, n.strong, n.question_code "
                f"FROM ib_node n JOIN ib_observation o ON o.id = n.observation_id "
                f"WHERE o.stage='verse-reading' AND o.deleted=0 "
                f"AND n.verse_reference IN ({ph})", osis_list).fetchall()
        existing_keys = Counter((r["verse_reference"], r["strong"], r["question_code"]) for r in rows)

    exp_set, exist_set = set(expected_keys), set(existing_keys)
    missing = sorted(exp_set - exist_set)
    unexpected = sorted(exist_set - exp_set)
    present = exp_set & exist_set
    over_count = sorted((k, existing_keys[k]) for k in present if existing_keys[k] > 1)
    ok_count = len(present) - len(over_count)

    _SAMPLE_LIMIT = 25
    return {
        "cluster_code": cluster_code, "verse_count": len(verse_ids),
        "expected_count": len(exp_set), "existing_count": len(exist_set),
        "ok_count": ok_count, "missing_count": len(missing),
        "unexpected_count": len(unexpected), "over_count_count": len(over_count),
        "missing_sample": missing[:_SAMPLE_LIMIT], "unexpected_sample": unexpected[:_SAMPLE_LIMIT],
        "over_count_sample": over_count[:_SAMPLE_LIMIT],
    }


def fully_covered_verse_ids(conn: sqlite3.Connection, cluster_code: str,
                            verse_ids: list[int], family: str | None = None) -> set[int]:
    """The verse_ids already fully covered (every expected (strong, question_code) triple has a live,
    non-withdrawn node) (#1824): the first cluster's pass to touch a verse analyses every M-code word
    in it, so the caller excludes these before any LLM cost. Not applied under -Force.
    `family` narrows which codes count toward "fully covered"."""
    expected = expected_nodes(conn, cluster_code, verse_ids, family)
    if not expected:
        return set()
    expected_by_verse: dict[str, set[tuple]] = {}
    for r in expected:
        expected_by_verse.setdefault(r["verse_reference"], set()).add(
            (r["strong"], r["question_code"]))

    osis_rows = conn.execute(
        f"SELECT id, osisId FROM verse WHERE id IN ({','.join('?'*len(verse_ids))})",
        verse_ids).fetchall()
    vid_by_osis = {r["osisId"]: r["id"] for r in osis_rows}

    osis_list = list(expected_by_verse.keys())
    ph = ",".join("?" * len(osis_list))
    rows = conn.execute(
        f"SELECT n.verse_reference, n.strong, n.question_code "
        f"FROM ib_node n JOIN ib_observation o ON o.id = n.observation_id "
        f"WHERE o.stage='verse-reading' AND o.deleted=0 "
        f"AND n.verse_reference IN ({ph})", osis_list).fetchall()
    existing_by_verse: dict[str, set[tuple]] = {}
    for r in rows:
        existing_by_verse.setdefault(r["verse_reference"], set()).add(
            (r["strong"], r["question_code"]))

    return {vid_by_osis[osis] for osis, exp in expected_by_verse.items()
           if osis in vid_by_osis and exp <= existing_by_verse.get(osis, set())}


def missing_word_level_coverage(conn: sqlite3.Connection, cluster_code: str,
                                verse_ids: list[int]) -> list[dict]:
    """`lexical.relational`'s readiness gate (#1860): every M-code word in the scope must have a
    committed (non-withdrawn) word-level (`M0.1`/`M0.5`) observation for that verse, since relational
    grounds on those findings. A hard stop, not a per-verse skip. Returns the (verse, strong) gaps;
    empty means ready."""
    expected = expected_nodes(conn, cluster_code, verse_ids, family="word_level")
    if not expected:
        return []
    expected_pairs: dict[str, set[str]] = {}
    for r in expected:
        expected_pairs.setdefault(r["verse_reference"], set()).add(r["strong"])

    osis_list = list(expected_pairs.keys())
    ph = ",".join("?" * len(osis_list))
    rows = conn.execute(
        f"SELECT n.verse_reference, n.strong FROM ib_node n "
        f"JOIN ib_observation o ON o.id = n.observation_id "
        f"WHERE o.stage='verse-reading' AND o.deleted=0 "
        f"AND (o.question_code LIKE 'M0.1%' OR o.question_code LIKE 'M0.5%') "
        f"AND n.verse_reference IN ({ph})", osis_list).fetchall()
    covered_by_verse: dict[str, set[str]] = {}
    for r in rows:
        covered_by_verse.setdefault(r["verse_reference"], set()).add(r["strong"])

    gaps = []
    for osis, strongs in expected_pairs.items():
        missing_strongs = strongs - covered_by_verse.get(osis, set())
        for s in sorted(missing_strongs):
            gaps.append({"verse_reference": osis, "strong": s})
    return gaps
