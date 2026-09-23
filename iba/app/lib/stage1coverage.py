"""stage1coverage.py — deterministic expected-vs-actual coverage validation for Stage 1
(`lexical.meaning` + `lexical.relational`), escalation #1824 v14, researcher instruction
2026-09-22, verbatim: "stage 1 need to pre-calculate the expected result for each scope, and
measure the result received from llm as the llm validation check."

Two halves, deliberately separate (one never calls an LLM, the other only reads what's already
written):

  expected_nodes(conn, cluster_code, verse_ids, family=None) — the deterministic (verse, strong,
      question_code) triples Stage 1 SHOULD attempt for this scope, computed from live
      `verse_lexical` role data + current `ib_observation` battery-coverage state, WITHOUT calling
      the LLM. Reuses the exact population/gating rules `versereadinggenerate.py`'s own
      instruction text encodes (word-level vs per-occurrence, `M0.6.6`'s other-M-code gate,
      `D7.7.1`'s T3+party gate) — re-derived from the live catalogue query each call, not a
      hardcoded duplicate that could drift.

  validate_coverage(conn, cluster_code, verse_ids, family=None) — compares that expected set
      against the LIVE `ib_node`/`ib_observation` state (`stage='verse-reading'`, non-withdrawn)
      for the same scope: MISSING (expected, no live node), UNEXPECTED (live node, not expected),
      OVER_COUNT (expected once, but >1 live node/observation still exists — an un-reconciled
      legacy duplicate), OK.

`family` (escalation #1860, 2026-09-23, word-level/relational Stage 1 split): `None` (default)
keeps the original combined behaviour (every wired question code, used by
`clusterstatus.verse_reading_completeness`'s cross-cutting checks and anything scope-agnostic).
`'word_level'` restricts to `M0.1`/`M0.5` (the `lexical.meaning` step's own scope after the split).
`'relational'` restricts to `M0.6.5`/`M0.6.6`/`D7.7.1`/`M0.7`/`M0.8.1` (the new `lexical.relational`
step's scope) — each step's own post-run `validate_coverage` call must pass its own family, or a
`lexical.meaning` run would misreport the relational codes it was never asked to write as MISSING.

First built and validated by hand (`outputs/stage1-expected-nodes-20260922.csv`,
`outputs/stage1-expected-vs-existing-comparison-20260922.csv`) before being made a real, reusable
part of the codebase here — the ad hoc numbers and this module's own output are expected to match
exactly for the same scope, since this module is a direct port of that same logic.
"""

from __future__ import annotations

import json
import sqlite3
from collections import Counter

_WORD_LEVEL_PREFIXES = ("M0.1", "M0.5")
_RELATIONAL_EXACT_CODES = ("D7.7.1", "M0.6.5", "M0.6.6", "M0.8.1")


def _wired_question_codes(conn: sqlite3.Connection, family: str | None = None
                          ) -> tuple[list[str], list[str]]:
    """(word_level_codes, per_occurrence_m07_codes) -- the exact Stage 1 catalogue selection,
    same query `versereadinggenerate.py`'s own assemble functions run, so this can never drift
    from what the live pipeline actually asks. `family` narrows which half is populated:
    `'word_level'` returns (word_level_codes, []); `'relational'` returns ([], m07_codes) (M0.7 is
    the only one of the "wired" pair that lives in `_wired_question_codes`'s two-tuple shape --
    the other relational codes (`D7.7.1`/`M0.6.5`/`M0.6.6`/`M0.8.1`) are handled directly in
    `expected_nodes` below, not via this tuple)."""
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
    """Every row has: verse_reference, strong, surface, morph_code, is_home_strong,
    question_code, reason. verse_ids should already be in the caller's own processing order
    (determines which verse counts as a word-level strong's "primary" — the one Stage 1 would
    actually attach the once-ever battery node to).

    `family`: `None` (default) = every wired code (original combined behaviour). `'word_level'` =
    `M0.1`/`M0.5` only (the `lexical.meaning` step's scope). `'relational'` = `M0.6.5`/`M0.6.6`/
    `D7.7.1`/`M0.7`/`M0.8.1` only (the `lexical.relational` step's scope) -- escalation #1860."""
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

    # `battery_covered`/`primary_verse_for_strong` ("once ever per strong, only its primary verse")
    # REMOVED 2026-09-23 -- researcher correction, verbatim: "Every word observation answer must be
    # at span (word in verse context) level. Saying that you can resolve the observation question
    # without looking at the verse/span/morph means it is a generic answer." Word-level (M0.1/M0.5)
    # questions are now expected for EVERY M-code strong in EVERY verse it occurs in, exactly the
    # same population as M0.6.5/M0.6.6/D7.7.1/M0.7 below -- generation must consult this specific
    # occurrence every time; consolidating independently-grounded answers that turn out to match is
    # `recordingpass.py`'s job at write time, not a reason to skip asking here.

    rows_out: list[dict] = []
    for vid in verse_ids:
        osis = osis_by_id.get(vid)
        if osis is None:
            continue
        words = by_verse.get(vid, [])
        m_strongs_here_raw = [w for w in words if w["strong"] and any(c.startswith("M") for c in w["roles"])]
        # Dedupe by (strong, surface, morph_code) -- escalation #1865, 2026-09-23: a strong can
        # occur twice in the same verse (two distinct verse_lexical positions) with IDENTICAL
        # surface+morph_code (e.g. 1Tim.5.13's G0692 "idlers", A-NPF, at positions 2 and 8) --
        # structurally indistinguishable by span, so asking for two independently-derived answers
        # is asking for a distinction the data can't actually support. Confirmed live: even before
        # today's stricter "exactly one entry per expected_items triple" instruction existed, the
        # recording pass only ever wrote ONE node for exactly this pair (1Tim.5.13/G0692/M0.7.1,
        # 2026-09-21) -- the data model already treats identical occurrences as one fact; the
        # checklist was the only place still asking for two, which is what made the model choke
        # (wrote explanatory prose instead of a parseable response) once the "same count, no
        # fewer/no more" instruction made that mismatch impossible to satisfy silently. A genuinely
        # DIFFERENT occurrence (different surface or morph_code) stays a separate checklist entry --
        # span-grounded-not-generic still applies whenever the span actually differs.
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

        # #1824 v14 researcher correction, 2026-09-22, verbatim: "verse reading is supposed to be
        # agnostic to cluster definition. every M-code word has the same status in the verse and
        # need to be treated the same." M0.6.5/M0.6.6/D7.7.1 population widened from home-strong-
        # only to every M-code strong in the verse -- the SAME population M0.1/M0.5/M0.7 already
        # use (mirrors the identical fix in versereadinggenerate.py's own prompt/population logic,
        # same commit). `is_home_strong` stays as a descriptive flag only, never a filter, for all
        # four question families now.
        if want_relational:
            for w in m_strongs_here:
                rows_out.append({
                    "verse_reference": osis, "strong": w["strong"], "surface": w["surface"],
                    "morph_code": w["morph_code"], "is_home_strong": cluster_code in w["roles"],
                    "question_code": "M0.6.5", "reason": "relational, always expected"})

        # #1824 v14 correction, 2026-09-22: both gates below were wrong. The catalogue's own
        # question_text for M0.6.6 says "Record none if this characteristic is the verse's only
        # M-code element" and for D7.7.1 "Record none if no such operation word is present" --
        # "record none" means the question is ALWAYS attempted (a null/negative finding is a
        # real answer), not conditionally skipped. The first version of this gate wrongly treated
        # the exclusion condition as "don't expect a node at all," producing 33 false UNEXPECTED
        # rows in the first live validation run (28 D7.7.1, 5 M0.6.6) -- confirmed live: those
        # verses' own role data genuinely lacked the extra condition this gate used to require
        # (M0.6.6: only 1 distinct M-code strong; D7.7.1: no T4/T7/T8/T9-tagged word), yet the
        # LLM correctly answered them anyway, exactly as the catalogue's own "record none" text
        # says it should. D7.7.1 is ALSO corrected to drop the party-tag requirement entirely --
        # that was this module's own invention, never actually stated by the catalogue text (only
        # "an operation word... present" is required); the live T4/T7/T8/T9 tags are sparse
        # (checked live: "God"/H0426 and "others"/G2087 are both tagged plain T2, not their own
        # party code), so requiring them was excluding real, valid cases the model rightly caught
        # by reading the verse text directly.
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

        # #1836, 2026-09-22: M0.8.1 (T2/T3 elevation-candidate) -- population is the OPPOSITE of
        # every other per-occurrence question above: words that carry a T2/T3 role but NO M-code
        # role at all. A word carrying both is already its own characteristic, nothing to flag.
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
    """The flat code list a given `family` covers -- used to scope validate_coverage's own
    "existing" query to the same family as `expected_nodes`, so a `lexical.meaning` (word-level)
    run's coverage check never flags an unrelated `lexical.relational` code as UNEXPECTED just
    because it wasn't in that call's own narrowed expected set. `None` -> None (no filter, original
    combined behaviour)."""
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
    """Compares expected_nodes() against the LIVE ib_node/ib_observation state for the same
    scope (stage='verse-reading', non-withdrawn only). Returns counts plus sample keys (capped)
    for each category — the full detail belongs in a persisted report, not held entirely in
    memory for a large scope. `family`: see `expected_nodes`'s own docstring -- also scopes the
    "existing" side of the comparison to the same question-code set (escalation #1860)."""
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
                f"WHERE o.stage='verse-reading' AND o.status != 'withdrawn' "
                f"AND n.verse_reference IN ({ph}) AND n.question_code IN ({cph})",
                (*osis_list, *family_codes)).fetchall()
        else:
            rows = conn.execute(
                f"SELECT n.verse_reference, n.strong, n.question_code "
                f"FROM ib_node n JOIN ib_observation o ON o.id = n.observation_id "
                f"WHERE o.stage='verse-reading' AND o.status != 'withdrawn' "
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
    """#1824 v18, researcher instruction 2026-09-22, verbatim: "when M32 cluster is processed
    then all the analysis for verses already analysed previously is not recreated... if the
    second read of the verse finds additional observations then something went wrong in the
    first reading." Since BUILD #316, the FIRST cluster's pass to touch a verse already does
    complete Stage 1 analysis of every M-code word in it (cluster-agnostic) -- a LATER cluster
    whose own strong happens to occur in that same verse should not re-derive it at all, not even
    a reduced/skipped-content call. Returns the subset of verse_ids that are ALREADY fully
    covered (every expected (strong, question_code) triple has a live, non-withdrawn node) --
    the caller excludes these from batch/scope construction entirely, before any LLM cost is
    incurred. Never applied when the caller is honouring -Force (a deliberate reconciliation
    rerun, #1824 Fix 3, intentionally re-examines already-covered material).

    `family`: see `expected_nodes`'s own docstring (escalation #1860) -- narrows which question
    codes count toward "fully covered" for the caller's own step. No filter needed on the
    "existing" side: a narrower expected set being a subset of the (unfiltered) existing set is
    still a correct covered/not-covered answer."""
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
        f"WHERE o.stage='verse-reading' AND o.status != 'withdrawn' "
        f"AND n.verse_reference IN ({ph})", osis_list).fetchall()
    existing_by_verse: dict[str, set[tuple]] = {}
    for r in rows:
        existing_by_verse.setdefault(r["verse_reference"], set()).add(
            (r["strong"], r["question_code"]))

    return {vid_by_osis[osis] for osis, exp in expected_by_verse.items()
           if osis in vid_by_osis and exp <= existing_by_verse.get(osis, set())}


def missing_word_level_coverage(conn: sqlite3.Connection, cluster_code: str,
                                verse_ids: list[int]) -> list[dict]:
    """`lexical.relational`'s readiness gate (escalation #1860, 2026-09-23): every M-code word in
    the requested verse scope must already have a committed (non-withdrawn) word-level (`M0.1`/
    `M0.5`) `ib_observation` for that exact verse before relational reading may run at all -- the
    split's whole point is that relational grounds on committed word-level findings
    (`versereadinggenerate._word_level_findings`), so it must not run ahead of them. Hard-stop
    shape, same as `lexical.build`'s stale-role check / `lexical.readiness`'s FATAL stop -- not a
    silent per-verse skip (contrast `fully_covered_verse_ids`, which IS a silent skip, for a
    different purpose). Returns the (verse, strong) gaps -- empty list means ready."""
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
        f"WHERE o.stage='verse-reading' AND o.status != 'withdrawn' "
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
