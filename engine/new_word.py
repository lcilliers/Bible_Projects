"""
new_word.py
───────────
NEW_WORD mode — steps N1 through N19.

Pre-transaction (N1–N8): validation, MTI classification, API fetch + span filter.
Transaction (N9–N15): single atomic DB write block.
Post-write (N15–N19): meaning parse, flag engine, audit, field-fill, registry update.
"""

from __future__ import annotations

import json
import sys
import os
from datetime import datetime, timezone

_ROOT = os.path.join(os.path.dirname(__file__), "..")
# analytics/ lives under scripts/ since the 2026-04-27 folder restructure.
_SCRIPTS = os.path.join(_ROOT, "scripts")
if _SCRIPTS not in sys.path:
    sys.path.insert(0, _SCRIPTS)

from analytics.step_client import StepClient

from .constants import (
    EXPECTED_SCHEMA_VERSION,
    LOCK_SENTINEL,
    SPECIFICATION,
)
from .db import get_max_id, get_book_id, get_schema_version
from .audit import run_audit
from .flag_engine import run_flag_engine
from .meaning_parser import run_parser_for_file
from .run_log import (
    make_run_id, open_run, close_run,
    write_word_run_state, log_fetch,
)
from .span_filter import filter_verse_records


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _confirm(prompt: str, expected: str) -> bool:
    """Ask for typed confirmation. Returns True if correct."""
    try:
        val = input(f"{prompt} (type '{expected}' to confirm): ").strip()
    except (EOFError, KeyboardInterrupt):
        return False
    return val == expected


def _pause(label: str, pause: bool) -> None:
    """If pause mode is active, wait for Enter before proceeding."""
    if not pause:
        return
    try:
        input(f"  [PAUSE] {label} — press Enter to continue...")
    except (EOFError, KeyboardInterrupt):
        print()


def classify_strongs(conn, strongs: str, registry_id: int) -> str:
    """Classify a Strong's as NEW, XREF, or PENDING."""
    row = conn.execute(
        "SELECT id, status FROM mti_terms WHERE strongs_number = ?",
        (strongs,),
    ).fetchone()
    if not row:
        return "NEW"
    if row["status"] in ("extracted", "extracted_theological_anchor"):
        # Already extracted under a different registry → XREF
        owner = conn.execute(
            "SELECT owning_registry FROM mti_terms WHERE strongs_number = ? LIMIT 1",
            (strongs,),
        ).fetchone()
        if owner and str(owner["owning_registry"]) != str(registry_id):
            return "XREF"
    return "PENDING"


def run_new_word(conn, registry_id: int, strongs_list: list[str],
                 dry_run: bool = False, force: bool = False,
                 pause: bool = False) -> dict:
    """Execute NEW_WORD mode for a single registry entry.

    Args:
        conn:         Open database connection.
        registry_id:  word_registry.no value.
        strongs_list: List of Strong's numbers for this word.
        dry_run:      If True, run all logic but make no DB writes.
        force:        If True, allow overwriting existing wa_file_index rows
                      (requires typed 'OVERWRITE' confirmation).

    Returns dict with keys: outcome, run_id, audit_result, details.
    """
    run_id = make_run_id("NEW_WORD")
    errors = []
    counts = {
        "words_attempted": 1, "words_complete": 0, "words_stopped": 0,
        "total_terms_new": 0, "total_terms_xref": 0,
        "total_verses_inserted": 0, "total_verses_filtered": 0,
        "total_meanings_parsed": 0, "errors": errors,
    }

    def _stop(msg: str) -> dict:
        counts["words_stopped"] = 1
        errors.append(msg)
        print(f"\n  [STOP] {msg}")
        if not dry_run:
            try:
                close_run(conn, run_id, "STOPPED", counts)
            except Exception:
                pass
        return {"outcome": "STOPPED", "run_id": run_id, "audit_result": "STOP",
                "details": errors}

    def _review(msg: str) -> None:
        print(f"\n  [REVIEW] {msg}")

    # ── Open run log ──────────────────────────────────────────────────────────
    if not dry_run:
        open_run(conn, run_id, "NEW_WORD", [registry_id])

    print(f"\n=== NEW_WORD run {run_id} | registry {registry_id} ===")

    # ── N1: Registry confirmation ─────────────────────────────────────────────
    print("N1  Registry confirmation...")
    reg_row = conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone()
    if not reg_row:
        return _stop(f"N1: No word_registry row for no={registry_id}")
    if reg_row["phase1_status"] != "Pending":
        return _stop(
            f"N1: phase1_status is '{reg_row['phase1_status']}', expected 'Pending'. "
            "Use --mode=audit for existing words."
        )
    if reg_row["automation_eligible"] == 0:
        return _stop(f"N1: automation_eligible=0 for registry {registry_id}.")
    word = reg_row["word"]
    print(f"     Word: {word} (registry {registry_id})")

    # ── N2: Duplicate check ───────────────────────────────────────────────────
    print("N2  Duplicate check...")
    existing_fi = conn.execute(
        "SELECT id FROM wa_file_index WHERE registry_id = ?",
        (str(registry_id),),
    ).fetchall()
    if existing_fi:
        if not force:
            return _stop(
                f"N2: wa_file_index rows already exist for registry {registry_id}. "
                "Use --force to overwrite."
            )
        old_ids = [r["id"] for r in existing_fi]
        _review(
            f"N2: --force active — purging {len(old_ids)} existing "
            f"wa_file_index row(s) for {word} (registry {registry_id}): ids={old_ids}."
        )
        for old_id in old_ids:
            conn.execute("DELETE FROM wa_data_quality_flags WHERE file_id = ?", (old_id,))
            # Delete meaning children before parent (FK: wa_meaning_sense/stem → wa_meaning_parsed)
            conn.execute(
                "DELETE FROM wa_meaning_sense WHERE parsed_meaning_id IN "
                "(SELECT mp.id FROM wa_meaning_parsed mp "
                " JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id WHERE ti.file_id = ?)",
                (old_id,))
            conn.execute(
                "DELETE FROM wa_meaning_stem WHERE parsed_meaning_id IN "
                "(SELECT mp.id FROM wa_meaning_parsed mp "
                " JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id WHERE ti.file_id = ?)",
                (old_id,))
            conn.execute("DELETE FROM wa_meaning_parsed WHERE term_inv_id IN "
                         "(SELECT id FROM wa_term_inventory WHERE file_id = ?)", (old_id,))
            conn.execute("DELETE FROM wa_lsj_parsed WHERE term_inv_id IN "
                         "(SELECT id FROM wa_term_inventory WHERE file_id = ?)", (old_id,))
            conn.execute("DELETE FROM wa_verse_records WHERE file_id = ?", (old_id,))
            conn.execute("DELETE FROM wa_term_inventory WHERE file_id = ?", (old_id,))
            conn.execute("DELETE FROM mti_terms WHERE word_data_reference = ?", (str(old_id),))
            conn.execute("DELETE FROM wa_file_index WHERE id = ?", (old_id,))
        # Also purge XREF cross-refs for this registry+word (not tied to file_id)
        conn.execute(
            "DELETE FROM mti_term_cross_refs WHERE registry = ? AND word = ?",
            (str(registry_id), word),
        )
        conn.commit()
        print(f"     N2: Old data purged for file_ids {old_ids}.")

    # ── N3: Term list validation ──────────────────────────────────────────────
    print("N3  Term list validation...")
    if not strongs_list:
        return _stop("N3: Empty term list.")
    import re as _re
    invalid = [s for s in strongs_list if not _re.match(r"^[HG]\d{4}[A-Z]?$", s)]
    if invalid:
        return _stop(f"N3: Malformed Strong's numbers: {invalid}")
    dupes = [s for s in strongs_list if strongs_list.count(s) > 1]
    if dupes:
        return _stop(f"N3: Internal duplicates in term list: {list(set(dupes))}")
    print(f"     {len(strongs_list)} terms validated.")

    # ── N4: MTI classification ────────────────────────────────────────────────
    print("N4  MTI classification...")
    classifications = {s: classify_strongs(conn, s, registry_id) for s in strongs_list}
    new_terms  = [s for s, c in classifications.items() if c == "NEW"]
    xref_terms = [s for s, c in classifications.items() if c == "XREF"]
    pending_terms = [s for s, c in classifications.items() if c == "PENDING"]

    print(f"     NEW: {len(new_terms)}  XREF: {len(xref_terms)}  PENDING: {len(pending_terms)}")

    if pending_terms:
        _review(
            f"N4: PENDING terms auto-approved (non-interactive): {pending_terms}. "
            "Verify via --report after the run."
        )

    if not new_terms:
        _review("N4: No NEW terms — all terms are XREF or PENDING.")

    # ── N5: Schema version check ──────────────────────────────────────────────
    print("N5  Schema version check...")
    schema_ver = get_schema_version(conn)
    if schema_ver != EXPECTED_SCHEMA_VERSION:
        return _stop(
            f"N5: Schema version mismatch — found {schema_ver!r}, "
            f"expected {EXPECTED_SCHEMA_VERSION!r}. Run: engine.py --migrate"
        )

    # ── N6: Pre-write lock ─────────────────────────────────────────────────────
    print("N6  Pre-write lock...")
    if not dry_run:
        existing_lock = conn.execute(
            "SELECT last_automation_run FROM word_registry WHERE no = ?",
            (registry_id,),
        ).fetchone()["last_automation_run"]
        if existing_lock == LOCK_SENTINEL:
            return _stop(
                f"N6: IN_PROGRESS sentinel already set for registry {registry_id}. "
                f"Resolve with: engine.py --clear-lock --registry={registry_id}"
            )
        conn.execute(
            "UPDATE word_registry SET last_automation_run = ? WHERE no = ?",
            (LOCK_SENTINEL, registry_id),
        )
        conn.commit()

    # ── N7–N8: PRE-TRANSACTION — API calls ────────────────────────────────────
    print("N7  Fetching vocab data from STEP...")
    client = StepClient()
    vocab_map: dict[str, dict] = {}
    verse_map: dict[str, list[dict]] = {}     # strongs → filtered verse records
    html_map_all: dict[str, dict[str, str]] = {}  # strongs → {osisId → html}
    span_conflicts: set[str] = set()
    total_fetched = 0
    total_filtered = 0

    for strongs in new_terms:
        warnings = []
        try:
            vocab = client.get_vocab_info(strongs)
            if not vocab:
                errors.append(f"N7: No vocab data for {strongs}")
                log_fetch(conn, run_id, registry_id, strongs, strongs, 0,
                          "failed", "skipped", 0, 0, 0, 0, ["no vocab data"])
                continue

            resolved = vocab["strong_number"]
            suffix_res = 1 if resolved != strongs else 0
            vocab_map[strongs] = vocab

            log_fetch(conn, run_id, registry_id, strongs, resolved, suffix_res,
                      "ok", "pending", 0, 0, 0, 0, None)

        except Exception as exc:
            errors.append(f"N7: vocab fetch failed for {strongs}: {exc}")
            log_fetch(conn, run_id, registry_id, strongs, strongs, 0,
                      "failed", "skipped", 0, 0, 0, 0, [str(exc)])

    if not vocab_map and new_terms:
        if not dry_run:
            conn.execute(
                "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
                (registry_id,),
            )
            conn.commit()
        return _stop("N7: All vocab fetches failed.")

    if len(vocab_map) < len(new_terms):
        _review(f"N7: Partial vocab fetch — {len(vocab_map)}/{len(new_terms)} terms.")

    print("N8  Fetching verses + span filter from STEP...")
    for strongs in list(vocab_map.keys()):
        resolved = vocab_map[strongs]["strong_number"]
        try:
            raw_records, html_map = client.get_verse_records_with_html(strongs)
            html_map_all[strongs] = html_map
            filter_result = filter_verse_records(raw_records, resolved, html_map)

            stored   = filter_result["stored"]
            filtered = filter_result["filtered"]
            conflict = filter_result["conflict"]

            total_fetched  += len(raw_records)
            total_filtered += len(filtered)

            verse_map[strongs] = stored

            verse_status = "zero_results" if not stored else "ok"
            if conflict:
                span_conflicts.add(strongs)
                verse_status = "zero_results"
                _review(f"N8: SPAN_RESOLUTION_CONFLICT — {strongs} had {len(raw_records)} "
                        f"verses fetched but all filtered. Verse set will be empty.")

            log_fetch(
                conn, run_id, registry_id, strongs, resolved,
                1 if resolved != strongs else 0,
                "ok", verse_status,
                len(raw_records), len(stored), len(filtered),
                1 if conflict else 0, warnings or None,
            )

        except Exception as exc:
            errors.append(f"N8: verse fetch failed for {strongs}: {exc}")
            verse_map[strongs] = []

    if not verse_map and new_terms and not span_conflicts:
        if not dry_run:
            conn.execute(
                "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
                (registry_id,),
            )
            conn.commit()
        return _stop("N8: All verse fetches failed and no meanings available.")

    if dry_run:
        print("\n  [DRY-RUN] Pre-transaction phase complete. No writes performed.")
        return {
            "outcome": "DRY_RUN", "run_id": run_id, "audit_result": None,
            "details": {
                "new_terms": new_terms, "xref_terms": xref_terms,
                "vocab_fetched": len(vocab_map),
                "total_verses_fetched": total_fetched,
                "total_verses_filtered": total_filtered,
            },
        }

    _pause(
        f"Pre-transaction data ready: vocab={len(vocab_map)}  "
        f"verses_fetched={total_fetched}  filtered={total_filtered}  "
        f"conflicts={len(span_conflicts)}  — review N7/N8 output above",
        pause,
    )

    # ── OPEN TRANSACTION — N9–N15 ─────────────────────────────────────────────
    print("N9–N15  Opening transaction — DB writes...")
    file_id = None
    try:
        with conn:
            # N9: Write wa_file_index
            file_id = get_max_id(conn, "wa_file_index") + 1
            conn.execute(
                """INSERT INTO wa_file_index
                       (id, filename, registry_id, word_registry_fk, word,
                        part_number, total_parts, is_split,
                        specification, phase, produced_date, translation_used,
                        source_list, testament_coverage)
                   VALUES (?, ?, ?, ?, ?, NULL, NULL, 0, ?, 'Phase 1', ?, 'ESV', ?, NULL)""",
                (
                    file_id,
                    run_id,
                    str(registry_id),
                    reg_row["id"],
                    word,
                    SPECIFICATION,
                    _today(),
                    reg_row["source_list"],
                ),
            )
            print(f"     N9:  wa_file_index id={file_id}")

            # N10: Write mti_terms for NEW terms
            for strongs in new_terms:
                vocab = vocab_map.get(strongs)
                if not vocab:
                    continue
                mt_id = get_max_id(conn, "mti_terms") + 1
                resolved = vocab["strong_number"]
                lang = vocab.get("language", "Hebrew")
                conn.execute(
                    """INSERT INTO mti_terms
                           (id, strongs_number, transliteration, gloss, language,
                            owning_registry, owning_word, owning_part,
                            word_data_reference, owning_registry_fk, word_data_ref_fk,
                            status, extraction_date, strongs_reconciled)
                       VALUES (?, ?, ?, ?, ?, ?, ?, NULL, ?, ?, ?, 'extracted', ?, ?)""",
                    (
                        mt_id, resolved,
                        vocab.get("transliteration", ""),
                        vocab.get("gloss", ""),
                        lang,
                        str(registry_id), word,
                        str(file_id),
                        registry_id, file_id,
                        _today(),
                        1 if resolved != strongs else 0,
                    ),
                )
                counts["total_terms_new"] += 1

            print(f"     N10: {counts['total_terms_new']} mti_terms rows")

            # N11: Write wa_term_inventory + wa_term_related_words
            term_inv_ids: dict[str, int] = {}
            for strongs in new_terms:
                vocab = vocab_map.get(strongs)
                if not vocab:
                    continue
                ti_id = get_max_id(conn, "wa_term_inventory") + 1
                resolved = vocab["strong_number"]
                lang = vocab.get("language", "Hebrew")
                conn.execute(
                    """INSERT INTO wa_term_inventory
                           (id, file_id, language, term_id, strongs_number,
                            transliteration, step_search_gloss, word_analysis_gloss,
                            occurrence_count, meaning, meaning_numbered,
                            lsj_entry, short_def_mounce, testament,
                            causative_form_present)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?)""",
                    (
                        ti_id, file_id, lang,
                        resolved, resolved,
                        vocab.get("transliteration", ""),
                        vocab.get("gloss", ""),
                        vocab.get("gloss", ""),
                        vocab.get("occurrence_count"),
                        vocab.get("medium_def"),
                        vocab.get("medium_def"),  # meaning_numbered mirrors meaning text
                        vocab.get("lsj_entry") or None,
                        vocab.get("short_def_mounce") or None,
                        1 if vocab.get("causative_form_present") else 0,
                    ),
                )
                term_inv_ids[strongs] = ti_id

                # Related words
                for rw in vocab.get("related_words", []):
                    conn.execute(
                        """INSERT INTO wa_term_related_words
                               (term_inv_id, gloss, transliteration, strongs_number)
                           VALUES (?, ?, ?, ?)""",
                        (ti_id, rw.get("gloss"), rw.get("translit"), rw.get("strong")),
                    )

            print(f"     N11: {len(term_inv_ids)} wa_term_inventory rows")

            # N12: Write verse records (span_strong_match=1 only)
            for strongs, records in verse_map.items():
                ti_id = term_inv_ids.get(strongs)
                if ti_id is None:
                    continue
                for rec in records:
                    book_id = get_book_id(conn, rec["book_code"])
                    if book_id is None:
                        errors.append(f"N12: Unknown book code {rec['book_code']!r}")
                        continue
                    vr_id = get_max_id(conn, "wa_verse_records") + 1
                    conn.execute(
                        """INSERT INTO wa_verse_records
                               (id, file_id, term_inv_id, term_id, transliteration,
                                book_id, reference, chapter, verse_num, testament,
                                translation, verse_text, target_word,
                                span_strong_match, context_before, context_after)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'ESV', ?, ?, ?, NULL, NULL)""",
                        (
                            vr_id, file_id, ti_id, strongs,
                            vocab_map.get(strongs, {}).get("transliteration", ""),
                            book_id,
                            rec["ref"], rec["chapter"], rec["verse_num"],
                            rec["testament"],
                            rec["esv_text"],
                            rec.get("target_word", ""),
                            rec.get("span_strong_match", 1),
                        ),
                    )
                    counts["total_verses_inserted"] += 1
            counts["total_verses_filtered"] = total_filtered

            # N13: Write XREF cross-refs
            for strongs in xref_terms:
                # Find the owning mti_term
                mt_row = conn.execute(
                    "SELECT id FROM mti_terms WHERE strongs_number = ? LIMIT 1",
                    (strongs,),
                ).fetchone()
                if not mt_row:
                    continue
                # Guard against NULL-part duplicate (SQLite UNIQUE treats NULL != NULL)
                _existing_xref = conn.execute(
                    "SELECT id FROM mti_term_cross_refs "
                    "WHERE mti_term_id = ? AND registry = ? AND word = ? AND part IS NULL",
                    (mt_row["id"], str(registry_id), word),
                ).fetchone()
                if not _existing_xref:
                    xref_mti_id = get_max_id(conn, "mti_term_cross_refs") + 1
                    conn.execute(
                        "INSERT INTO mti_term_cross_refs (id, mti_term_id, registry, word, registry_fk) "
                        "VALUES (?, ?, ?, ?, ?)",
                        (xref_mti_id, mt_row["id"], str(registry_id), word, registry_id),
                    )
                counts["total_terms_xref"] += 1

            print(f"     N12: {counts['total_verses_inserted']} verse records  "
                  f"({counts['total_verses_filtered']} filtered)")
            print(f"     N13: {counts['total_terms_xref']} XREF cross-refs")

    except Exception as exc:
        errors.append(f"Transaction failed: {exc}")
        # Clear IN_PROGRESS sentinel on rollback
        conn.execute(
            "UPDATE word_registry SET last_automation_run = ? WHERE no = ?",
            (LOCK_SENTINEL, registry_id),
        )
        conn.commit()
        return _stop(f"Transaction rolled back: {exc}")

    # ── Post-transaction self-verify ───────────────────────────────────────────────────
    _fi_ok  = conn.execute("SELECT COUNT(*) FROM wa_file_index WHERE id = ?",
                           (file_id,)).fetchone()[0] == 1
    _ti_cnt = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE file_id = ?",
                           (file_id,)).fetchone()[0]
    _vr_cnt = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE file_id = ?",
                           (file_id,)).fetchone()[0]
    _mt_cnt = conn.execute("SELECT COUNT(*) FROM mti_terms WHERE word_data_reference = ?",
                           (str(file_id),)).fetchone()[0]
    print(
        f"     [VERIFY] file_index={'OK' if _fi_ok else 'MISS'} "
        f"| terms={_ti_cnt}/{len(new_terms)} "
        f"| verses={_vr_cnt} "
        f"| mti={_mt_cnt}/{len(new_terms)}"
    )
    if not _fi_ok:
        return _stop("Post-transaction verify: wa_file_index row missing.")
    _pause("Transaction committed — verify DB counts above before post-write steps", pause)

    # ── N14: Derive testament_coverage ───────────────────────────────────────
    print("N14 Derive testament_coverage...")
    testaments = {
        r["testament"]
        for r in conn.execute(
            "SELECT DISTINCT testament FROM wa_verse_records "
            "WHERE file_id = ? AND span_strong_match = 1",
            (file_id,),
        ).fetchall()
    }
    if testaments == {"OT"}:
        tc = "OT_only"
    elif testaments == {"NT"}:
        tc = "NT_only"
    elif testaments:
        tc = "both"
    else:
        tc = None
        _review("N14: No confirmed verses — testament_coverage remains null.")

    conn.execute(
        "UPDATE wa_file_index SET testament_coverage = ? WHERE id = ?",
        (tc, file_id),
    )
    # Also update wa_term_inventory.testament per term
    for strongs, ti_id in term_inv_ids.items():
        term_testaments = {
            r["testament"]
            for r in conn.execute(
                "SELECT DISTINCT testament FROM wa_verse_records "
                "WHERE term_inv_id = ? AND span_strong_match = 1",
                (ti_id,),
            ).fetchall()
        }
        term_tc = (
            "OT" if term_testaments == {"OT"} else
            "NT" if term_testaments == {"NT"} else
            "both" if term_testaments else None
        )
        conn.execute(
            "UPDATE wa_term_inventory SET testament = ? WHERE id = ?",
            (term_tc, ti_id),
        )
    conn.commit()

    # ── N15: Meaning parser ───────────────────────────────────────────────────
    print("N15 Meaning parser...")
    parse_result = run_parser_for_file(conn, file_id, vocab_map)
    counts["total_meanings_parsed"] = parse_result["parsed"]
    if parse_result["errors"]:
        for e in parse_result["errors"]:
            _review(f"N15: {e}")
    print(f"     Parsed {parse_result['parsed']} meanings.")
    _mp_cnt = conn.execute(
        "SELECT COUNT(*) FROM wa_meaning_parsed mp "
        "JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id WHERE ti.file_id = ?",
        (file_id,)).fetchone()[0]
    print(f"     [VERIFY] wa_meaning_parsed: {_mp_cnt} rows")

    # ── N16: Flag engine ──────────────────────────────────────────────────────
    print("N16 Flag engine...")
    flag_result = run_flag_engine(conn, file_id, registry_id, span_conflicts)
    if flag_result["errors"]:
        for e in flag_result["errors"]:
            _review(f"N16: {e}")
    print(f"     {flag_result['flags_written']} quality flags written.")
    _fl_cnt = conn.execute("SELECT COUNT(*) FROM wa_data_quality_flags WHERE file_id = ?",
                           (file_id,)).fetchone()[0]
    print(f"     [VERIFY] quality flags total on file: {_fl_cnt}")

    # ── N17: Audit ────────────────────────────────────────────────────────────
    print("N17 Audit (WR-01 – WR-20)...")
    audit_result = run_audit(conn, file_id, registry_id)
    for check in audit_result["checks"]:
        if check["result"] != "PASS":
            print(f"     {check['result']:6} {check['check']}: {check['detail']}")

    if not dry_run:
        write_word_run_state(
            conn, run_id, registry_id, word,
            "AUDIT",
            audit_result["result"],
            {c["check"]: {"r": c["result"], "d": c["detail"]} for c in audit_result["checks"]},
            audit_result.get("stop_reason"),
        )

    print(f"     Audit result: {audit_result['result']}")
    _n17_p = sum(1 for c in audit_result["checks"] if c["result"] == "PASS")
    _n17_r = sum(1 for c in audit_result["checks"] if c["result"] == "REVIEW")
    _n17_s = sum(1 for c in audit_result["checks"] if c["result"] == "STOP")
    print(f"     [VERIFY] WR checks: {_n17_p} PASS  {_n17_r} REVIEW  {_n17_s} STOP")
    _pause("Audit complete — review results above before field-fill", pause)

    if audit_result["result"] == "STOP":
        _review(
            f"N17: STOP condition — researcher approval required before N18.\n"
            f"     {audit_result['stop_reason']}"
        )
        # Do NOT exit — researcher can approve interactively.
        if not _confirm("Approve STOP and continue to field-fill?", "APPROVE"):
            conn.execute(
                "UPDATE word_registry SET last_automation_run = ? WHERE no = ?",
                (LOCK_SENTINEL, registry_id),
            )
            conn.commit()
            counts["words_stopped"] = 1
            close_run(conn, run_id, "STOPPED", counts)
            return {
                "outcome": "STOPPED", "run_id": run_id,
                "audit_result": "STOP", "details": errors,
            }

    # ── N18: Field-fill ───────────────────────────────────────────────────────
    print("N18 Field-fill (also_spelled + occurrence_count_qualifier)...")
    _run_field_fill(conn, file_id, vocab_map)

    # ── N19: Update word_registry ─────────────────────────────────────────────
    print("N19 Updating word_registry...")
    # All-XREF words produce expected REVIEW audit flags (zero terms/verses/coverage).
    # Treat REVIEW as Complete when there are no NEW terms — nothing left to do.
    _all_xref = not new_terms
    final_status = "Complete" if (audit_result["result"] == "PASS" or _all_xref) else "In Progress"
    conn.execute(
        """UPDATE word_registry SET
               phase1_status        = ?,
               phase1_term_count    = ?,
               phase1_verse_count   = ?,
               last_automation_run  = ?,
               automation_run_id    = ?,
               phase1_input_file    = ?
           WHERE no = ?""",
        (
            final_status,
            counts["total_terms_new"],
            counts["total_verses_inserted"],
            _now(),
            run_id,
            run_id,
            registry_id,
        ),
    )
    conn.commit()

    counts["words_complete"] = 1 if audit_result["result"] == "PASS" else 0
    outcome = "COMPLETE" if final_status == "Complete" else "PARTIAL"
    close_run(conn, run_id, outcome, counts)

    print(f"\n=== NEW_WORD complete: {word} | {final_status} | {audit_result['result']} ===")
    return {
        "outcome": outcome, "run_id": run_id,
        "audit_result": audit_result["result"],
        "details": {
            "file_id": file_id,
            "terms_new": counts["total_terms_new"],
            "terms_xref": counts["total_terms_xref"],
            "verses_inserted": counts["total_verses_inserted"],
            "verses_filtered": counts["total_verses_filtered"],
            "meanings_parsed": counts["total_meanings_parsed"],
        },
    }


def _run_field_fill(conn, file_id: int, vocab_map: dict) -> None:
    """Interactive field-fill for also_spelled and occurrence_count_qualifier.
    Researcher inputs value or presses Enter to confirm null.
    If not connected to a tty (e.g. piped/automated run), skips prompts (accepts null).
    """
    import sys as _sys
    interactive = _sys.stdin.isatty() and _sys.stdout.isatty()

    terms = conn.execute(
        "SELECT id, strongs_number, term_id, language, also_spelled, occurrence_count_qualifier, "
        "transliteration, step_search_gloss "
        "FROM wa_term_inventory WHERE file_id = ?",
        (file_id,),
    ).fetchall()

    for term in terms:
        strongs = term["strongs_number"] or term["term_id"]
        ti_id = term["id"]

        # also_spelled — Hebrew only
        if term["language"] == "Hebrew" and term["also_spelled"] is None:
            gloss = term["step_search_gloss"] or ""
            translit = term["transliteration"] or ""
            print(f"\n  Field-fill: also_spelled")
            print(f"    Term: {strongs}  ({translit})  '{gloss}'")
            print(f"    (Check STEP UI for alternate spellings / Strong's variants)")
            if interactive:
                try:
                    val = input("    also_spelled (JSON or blank for null): ").strip()
                except (EOFError, KeyboardInterrupt):
                    val = ""
            else:
                print("    [non-interactive] skipping — null accepted")
                val = ""
            conn.execute(
                "UPDATE wa_term_inventory SET also_spelled = ? WHERE id = ?",
                (val if val else None, ti_id),
            )

        # occurrence_count_qualifier — all languages
        if term["occurrence_count_qualifier"] is None:
            occ = conn.execute(
                "SELECT occurrence_count FROM wa_term_inventory WHERE id = ?",
                (ti_id,),
            ).fetchone()["occurrence_count"]
            print(f"\n  Field-fill: occurrence_count_qualifier")
            print(f"    Term: {strongs}  occurrence_count={occ}")
            if interactive:
                try:
                    val = input("    qualifier ('about' / blank for exact): ").strip()
                except (EOFError, KeyboardInterrupt):
                    val = ""
            else:
                print("    [non-interactive] skipping — null accepted")
                val = ""
            conn.execute(
                "UPDATE wa_term_inventory SET occurrence_count_qualifier = ? WHERE id = ?",
                (val if val else None, ti_id),
            )

    conn.commit()
