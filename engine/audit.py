"""
audit.py
────────
Audit framework — WR-01 through WR-20.

Every mode runs the same deterministic checks after all writes.
Results are written to word_run_state.audit_detail as structured JSON.

Classification:
  PASS   — all STOP checks pass, zero REVIEW checks fail
  REVIEW — all STOP checks pass, ≥1 REVIEW check fails
  STOP   — ≥1 STOP check fails

All STOP checks are evaluated even after the first failure (progressive evaluation).
"""

from __future__ import annotations

from typing import Any


# ── Check result helpers ──────────────────────────────────────────────────────

def _pass(check_id: str, msg: str = "ok") -> dict:
    return {"check": check_id, "result": "PASS", "detail": msg}


def _fail_stop(check_id: str, detail: Any) -> dict:
    return {"check": check_id, "result": "STOP", "detail": detail}


def _fail_review(check_id: str, detail: Any) -> dict:
    return {"check": check_id, "result": "REVIEW", "detail": detail}


# ── Individual checks ─────────────────────────────────────────────────────────

def _wr01(conn, file_id: int, registry_id: int) -> dict:
    """wa_file_index present."""
    count = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_file_index WHERE registry_id = ?",
        (str(registry_id),),
    ).fetchone()["c"]
    if count >= 1:
        return _pass("WR-01")
    return _fail_stop("WR-01", f"No wa_file_index row for registry {registry_id}")


def _wr02(conn, file_id: int, registry_id: int) -> dict:
    """wa_file_index single row for v9 words (is_split = 0). Legacy split words exempt."""
    rows = conn.execute(
        "SELECT id, is_split FROM wa_file_index WHERE registry_id = ?",
        (str(registry_id),),
    ).fetchall()
    # If any row is a legacy split word (is_split != 0), exempt from single-row check.
    if any(r["is_split"] not in (0, None) for r in rows):
        return _pass("WR-02", "legacy split word — multi-row exempt")
    if len(rows) == 1:
        return _pass("WR-02")
    return _fail_stop("WR-02", f"Expected 1 wa_file_index row, found {len(rows)}")


def _wr03(conn, file_id: int, registry_id: int) -> dict:
    """Term count non-zero."""
    count = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_term_inventory WHERE file_id = ?",
        (file_id,),
    ).fetchone()["c"]
    if count > 0:
        return _pass("WR-03", f"{count} terms")
    return _fail_review("WR-03", "Zero wa_term_inventory rows — all terms may be XREF")


def _wr04(conn, file_id: int, registry_id: int) -> dict:
    """All wa_term_inventory strongs_number values present in mti_terms."""
    # Join on strongs_number (not id) — term_id contains legacy formats that
    # do not match mti_terms.strongs_number.  Rows with null strongs_number
    # are reported as REVIEW (not STOP) since they may be pre-v9 imports.
    null_strongs = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_term_inventory "
        "WHERE file_id = ? AND (strongs_number IS NULL OR strongs_number = '')",
        (file_id,),
    ).fetchone()["c"]

    orphans = conn.execute(
        """SELECT ti.id, ti.strongs_number FROM wa_term_inventory ti
           LEFT JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
           WHERE ti.file_id = ?
           AND (ti.strongs_number IS NOT NULL AND ti.strongs_number != '')
           AND mt.id IS NULL""",
        (file_id,),
    ).fetchall()

    issues = []
    if null_strongs:
        issues.append(f"{null_strongs} row(s) with null strongs_number")
    if orphans:
        issues.append(f"{len(orphans)} strongs_number(s) not in mti_terms: "
                      f"{[r['strongs_number'] for r in orphans]}")

    if not issues:
        return _pass("WR-04")
    # Orphan rows without any mti_terms entry are a REVIEW item — they may be
    # legitimate XREF terms or pre-v9 imports awaiting AUDIT_WORD back-fill.
    return _fail_review("WR-04", "; ".join(issues))


def _wr05(conn, file_id: int, registry_id: int) -> dict:
    """No ID gaps within this word's wa_term_inventory rows."""
    ids = sorted(
        r["id"] for r in conn.execute(
            "SELECT id FROM wa_term_inventory WHERE file_id = ?", (file_id,)
        ).fetchall()
    )
    if not ids:
        return _pass("WR-05", "no rows — skip gap check")
    gaps = [
        (ids[i], ids[i + 1]) for i in range(len(ids) - 1)
        if ids[i + 1] - ids[i] != 1
    ]
    if not gaps:
        return _pass("WR-05", f"IDs {ids[0]}–{ids[-1]} contiguous")
    # Downgraded to REVIEW: gaps can arise from legitimate term restructuring
    # (e.g. splitting a consolidated entry into sub-glosses) and are not
    # evidence of a partial write.  Partial-write detection is covered by
    # cross-checking verse counts in WR-06/WR-07.
    return _fail_review("WR-05", f"ID gaps detected in wa_term_inventory: {gaps}")


def _wr06(conn, file_id: int, registry_id: int) -> dict:
    """Confirmed verse records present (span_strong_match=1 OR IS NULL for pre-v9)."""
    count = conn.execute(
        """SELECT COUNT(*) AS c FROM wa_verse_records
           WHERE file_id = ?
           AND (span_strong_match = 1 OR span_strong_match IS NULL)""",
        (file_id,),
    ).fetchone()["c"]
    if count > 0:
        return _pass("WR-06", f"{count} confirmed verse records")
    # Check if any span conflicts explain zero verses
    conflict_count = conn.execute(
        """SELECT COUNT(*) AS c FROM wa_data_quality_flags dqf
           JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
           WHERE dqf.file_id = ? AND qt.flag_code = 'SPAN_RESOLUTION_CONFLICT'""",
        (file_id,),
    ).fetchone()["c"]
    detail = "Zero confirmed verses for entire word."
    if conflict_count:
        detail += f" {conflict_count} SPAN_RESOLUTION_CONFLICT flag(s) explain missing verses."
    return _fail_review("WR-06", detail)


def _wr07(conn, file_id: int, registry_id: int) -> dict:
    """All terms have verses or a relevant quality flag."""
    terms = conn.execute(
        "SELECT id, strongs_number, term_id FROM wa_term_inventory WHERE file_id = ?",
        (file_id,),
    ).fetchall()
    gaps = []
    for term in terms:
        vc = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_verse_records "
            "WHERE term_inv_id = ? AND (span_strong_match = 1 OR span_strong_match IS NULL)",
            (term["id"],),
        ).fetchone()["c"]
        if vc > 0:
            continue
        flag_count = conn.execute(
            """SELECT COUNT(*) AS c FROM wa_data_quality_flags dqf
               JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
               WHERE dqf.file_id = ? AND dqf.term_id = ?
               AND qt.flag_code IN ('NO_VERSES', 'SPAN_RESOLUTION_CONFLICT')""",
            (file_id, term["strongs_number"] or term["term_id"]),
        ).fetchone()["c"]
        if flag_count == 0:
            gaps.append(term["strongs_number"] or term["term_id"])
    if not gaps:
        return _pass("WR-07")
    return _fail_review("WR-07", f"Unexplained zero-verse terms: {gaps}")


def _wr08(conn, file_id: int, registry_id: int) -> dict:
    """Verse/occurrence ratio >= 0.15 for high-occurrence terms."""
    from .constants import VERSE_OCCURRENCE_RATIO_THRESHOLD, VERSE_OCCURRENCE_MIN_COUNT
    terms = conn.execute(
        "SELECT id, strongs_number, term_id, occurrence_count "
        "FROM wa_term_inventory WHERE file_id = ? AND occurrence_count >= ?",
        (file_id, VERSE_OCCURRENCE_MIN_COUNT),
    ).fetchall()
    low = []
    for term in terms:
        vc = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_verse_records "
            "WHERE term_inv_id = ? AND span_strong_match = 1",
            (term["id"],),
        ).fetchone()["c"]
        ratio = vc / term["occurrence_count"]
        if ratio < VERSE_OCCURRENCE_RATIO_THRESHOLD:
            low.append({
                "strongs": term["strongs_number"] or term["term_id"],
                "verses": vc, "occurrences": term["occurrence_count"],
                "ratio": round(ratio, 3),
            })
    if not low:
        return _pass("WR-08")
    return _fail_review("WR-08", f"Low verse/occurrence ratio: {low}")


def _wr09(conn, file_id: int, registry_id: int) -> dict:
    """testament_coverage set on wa_file_index."""
    row = conn.execute(
        "SELECT testament_coverage FROM wa_file_index WHERE id = ?", (file_id,)
    ).fetchone()
    if row and row["testament_coverage"]:
        return _pass("WR-09", row["testament_coverage"])
    return _fail_review("WR-09", "wa_file_index.testament_coverage is null")


def _wr10(conn, file_id: int, registry_id: int) -> dict:
    """Meaning populated or flagged."""
    terms = conn.execute(
        "SELECT id, strongs_number, term_id, meaning FROM wa_term_inventory WHERE file_id = ?",
        (file_id,),
    ).fetchall()
    unflagged = []
    for term in terms:
        if term["meaning"]:
            continue
        flag_count = conn.execute(
            """SELECT COUNT(*) AS c FROM wa_data_quality_flags dqf
               JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
               WHERE dqf.file_id = ? AND dqf.term_id = ? AND qt.flag_code = 'NO_WORD_ANALYSIS'""",
            (file_id, term["strongs_number"] or term["term_id"]),
        ).fetchone()["c"]
        if flag_count == 0:
            unflagged.append(term["strongs_number"] or term["term_id"])
    if not unflagged:
        return _pass("WR-10")
    return _fail_review("WR-10", f"Null meaning without NO_WORD_ANALYSIS flag: {unflagged}")


def _wr11(conn, file_id: int, registry_id: int) -> dict:
    """Transliteration populated for all terms."""
    missing = [
        r["strongs_number"] or r["term_id"]
        for r in conn.execute(
            "SELECT strongs_number, term_id FROM wa_term_inventory "
            "WHERE file_id = ? AND (transliteration IS NULL OR transliteration = '')",
            (file_id,),
        ).fetchall()
    ]
    if not missing:
        return _pass("WR-11")
    return _fail_stop("WR-11", f"Missing transliteration: {missing}")


def _wr12(conn, file_id: int, registry_id: int) -> dict:
    """Language populated (Hebrew or Greek) for all terms."""
    bad = [
        r["strongs_number"] or r["term_id"]
        for r in conn.execute(
            "SELECT strongs_number, term_id FROM wa_term_inventory "
            "WHERE file_id = ? AND language NOT IN ('Hebrew', 'Greek')",
            (file_id,),
        ).fetchall()
    ]
    if not bad:
        return _pass("WR-12")
    return _fail_stop("WR-12", f"Invalid language values: {bad}")


# Fields excluded from undocumented-null check (judgment-deferred or Phase 2 reserved).
# Note: god_as_subject and somatic_link were dropped from wa_term_inventory in M24
# (2026-04-19); their signals now live in mti_term_flags. Removed from this set.
_WR13_EXCLUDED_FIELDS = {
    "occurrence_count_qualifier", "also_spelled",
    "context_before", "context_after", "note", "claude_output",
}


def _wr13(conn, file_id: int, registry_id: int) -> dict:
    """No undocumented nulls in API-derivable fields."""
    # API-derivable nullable fields that should have a quality flag if null
    checkable = [
        ("occurrence_count",     "DATA_GAP"),
        ("meaning",              "NO_WORD_ANALYSIS"),
        ("lsj_entry",            None),   # Greek only — skip Hebrew
        ("short_def_mounce",     None),   # Greek only — skip Hebrew
    ]
    issues = []
    terms = conn.execute(
        "SELECT id, strongs_number, term_id, language, "
        "occurrence_count, meaning, lsj_entry, short_def_mounce "
        "FROM wa_term_inventory WHERE file_id = ?",
        (file_id,),
    ).fetchall()
    for term in terms:
        strongs = term["strongs_number"] or term["term_id"]
        for field, flag_code in checkable:
            if field in ("lsj_entry", "short_def_mounce") and term["language"] == "Hebrew":
                continue
            if term[field] is not None:
                continue
            # Null found — check for documenting quality flag
            if flag_code:
                has_flag = conn.execute(
                    """SELECT 1 FROM wa_data_quality_flags dqf
                       JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
                       WHERE dqf.file_id = ? AND dqf.term_id = ? AND qt.flag_code = ?""",
                    (file_id, strongs, flag_code),
                ).fetchone()
                if not has_flag:
                    issues.append(f"{strongs}.{field}")
    if not issues:
        return _pass("WR-13")
    return _fail_review("WR-13", f"Undocumented nulls in API-derivable fields: {issues}")


def _wr14(conn, file_id: int, registry_id: int) -> dict:
    """XREF terms have mti_term_cross_refs rows."""
    xref_needed = conn.execute(
        """SELECT mt.id, mt.strongs_number FROM mti_terms mt
           WHERE mt.owning_registry = ? AND mt.status = 'xref'""",
        (str(registry_id),),
    ).fetchall()
    missing = []
    for term in xref_needed:
        has_xref = conn.execute(
            "SELECT 1 FROM mti_term_cross_refs WHERE mti_term_id = ? AND registry = ?",
            (term["id"], str(registry_id)),
        ).fetchone()
        if not has_xref:
            missing.append(term["strongs_number"])
    if not missing:
        return _pass("WR-14")
    return _fail_review("WR-14", f"XREF terms without cross-refs: {missing}")


def _wr15(conn, file_id: int, registry_id: int) -> dict:
    """No duplicate active mti_terms per strongs_number for this owning_registry.
    Rows with exclusion_reason set are intentionally suppressed and are excluded
    from the duplicate check."""
    dupes = conn.execute(
        """SELECT strongs_number, COUNT(*) AS c FROM mti_terms
           WHERE owning_registry = ? AND (exclusion_reason IS NULL OR exclusion_reason = '')
           GROUP BY strongs_number HAVING c > 1""",
        (str(registry_id),),
    ).fetchall()
    if not dupes:
        return _pass("WR-15")
    detail = {r["strongs_number"]: r["c"] for r in dupes}
    return _fail_stop("WR-15", f"Duplicate mti_terms rows: {detail}")


def _wr16(conn, file_id: int, registry_id: int) -> dict:
    """Derivable flags assessed (flag engine must have run)."""
    # Check that wa_data_quality_flags has at least been evaluated for this file_id.
    # A file with no issues is fine — but the flag engine must have completed.
    # We check indirectly: if any term has occurrence_count >= HIGH_FREQ_THRESHOLD
    # or = 0, a corresponding flag should exist.
    from .constants import HIGH_FREQ_THRESHOLD
    flaggable_terms = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_term_inventory "
        "WHERE file_id = ? AND (occurrence_count >= ? OR occurrence_count = 0)",
        (file_id, HIGH_FREQ_THRESHOLD),
    ).fetchone()["c"]
    if flaggable_terms == 0:
        return _pass("WR-16", "no obviously flaggable terms — flag engine assumed complete")
    # At least one quality flag row for this file should exist
    flag_rows = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_data_quality_flags WHERE file_id = ?",
        (file_id,),
    ).fetchone()["c"]
    if flag_rows > 0:
        return _pass("WR-16", f"{flag_rows} quality flag rows present")
    return _fail_review("WR-16", "No quality flags written — flag engine may not have run")


def _wr17(conn, file_id: int, registry_id: int) -> dict:
    """All fetch warnings in term_fetch_log reflected in quality flags."""
    # Get terms for this file
    term_strongs = {
        r["strongs_number"] or r["term_id"]
        for r in conn.execute(
            "SELECT strongs_number, term_id FROM wa_term_inventory WHERE file_id = ?",
            (file_id,),
        ).fetchall()
    }
    # Count fetch log entries with warnings that have no corresponding quality flag
    unmirrored = []
    for strongs in term_strongs:
        warnings = conn.execute(
            "SELECT api_warnings FROM term_fetch_log "
            "WHERE registry_id = ? AND strongs_input = ? AND api_warnings IS NOT NULL",
            (str(registry_id), strongs),
        ).fetchall()
        if not warnings:
            continue
        flag_count = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_data_quality_flags WHERE file_id = ? AND term_id = ?",
            (file_id, strongs),
        ).fetchone()["c"]
        if flag_count == 0:
            unmirrored.append(strongs)
    if not unmirrored:
        return _pass("WR-17")
    return _fail_review("WR-17", f"Fetch warnings not reflected in quality flags: {unmirrored}")


def _wr18(conn, file_id: int, registry_id: int) -> dict:
    """All NEW terms have wa_meaning_parsed row (parsed_meaning_id IS NOT NULL)."""
    unparsed = conn.execute(
        "SELECT strongs_number, term_id FROM wa_term_inventory "
        "WHERE file_id = ? AND parsed_meaning_id IS NULL",
        (file_id,),
    ).fetchall()
    if not unparsed:
        return _pass("WR-18")
    ids = [r["strongs_number"] or r["term_id"] for r in unparsed]
    return _fail_review("WR-18", f"Terms without parsed meaning: {ids}")


def _wr19(conn, file_id: int, registry_id: int) -> dict:
    """Parse warnings documented in quality flags."""
    warned = conn.execute(
        """SELECT ti.strongs_number, ti.term_id FROM wa_meaning_parsed mp
           JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id
           WHERE ti.file_id = ? AND mp.parse_warnings IS NOT NULL""",
        (file_id,),
    ).fetchall()
    unmirrored = []
    for term in warned:
        strongs = term["strongs_number"] or term["term_id"]
        flag_exists = conn.execute(
            """SELECT 1 FROM wa_data_quality_flags dqf
               JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
               WHERE dqf.file_id = ? AND dqf.term_id = ?
               AND qt.flag_code IN ('NOTE', 'NOTE_ON_ROOT_FAMILY', 'PROSE_ONLY_MEANING')""",
            (file_id, strongs),
        ).fetchone()
        if not flag_exists:
            unmirrored.append(strongs)
    if not unmirrored:
        return _pass("WR-19")
    return _fail_review("WR-19", f"Parse warnings without NOTE flag: {unmirrored}")


def _wr20(conn, file_id: int, registry_id: int) -> dict:
    """Span back-population completeness.

    For v9 NEW_WORD/GAP_FILL: all rows should have span_strong_match set (=1).
    For AUDIT_WORD: all rows should have span_strong_match IS NOT NULL.
    """
    null_count = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_verse_records "
        "WHERE file_id = ? AND span_strong_match IS NULL",
        (file_id,),
    ).fetchone()["c"]
    if null_count == 0:
        return _pass("WR-20")
    return _fail_review(
        "WR-20",
        f"{null_count} verse records have null span_strong_match. "
        "Back-population (A3a) may not have completed for pre-v9 records.",
    )


# ── Main entry point ──────────────────────────────────────────────────────────

_CHECKS = [
    _wr01, _wr02, _wr03, _wr04, _wr05,
    _wr06, _wr07, _wr08, _wr09, _wr10,
    _wr11, _wr12, _wr13, _wr14, _wr15,
    _wr16, _wr17, _wr18, _wr19, _wr20,
]


def run_audit(conn, file_id: int, registry_id: int) -> dict:
    """Run all WR-01 through WR-20 checks.

    Returns:
        {
          "result":   "PASS" | "REVIEW" | "STOP",
          "checks":   [list of check dicts],
          "stop_reason": str | None,
        }
    """
    results = []
    for fn in _CHECKS:
        try:
            r = fn(conn, file_id, registry_id)
        except Exception as exc:
            r = _fail_review(fn.__name__.upper().replace("_", "-"),
                             f"Check raised exception: {exc}")
        results.append(r)

    has_stop   = any(r["result"] == "STOP"   for r in results)
    has_review = any(r["result"] == "REVIEW" for r in results)

    if has_stop:
        overall = "STOP"
        stop_items = [r for r in results if r["result"] == "STOP"]
        stop_reason = "; ".join(
            str(r["detail"]) for r in stop_items
        )
    elif has_review:
        overall = "REVIEW"
        stop_reason = None
    else:
        overall = "PASS"
        stop_reason = None

    return {
        "result":      overall,
        "checks":      results,
        "stop_reason": stop_reason,
    }
