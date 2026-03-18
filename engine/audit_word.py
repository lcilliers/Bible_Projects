"""
audit_word.py
─────────────
AUDIT_WORD mode — steps A1 through A10, including A3a.

Purpose: Refresh the audit state for a word that was imported before v9
or that needs its verse records re-examined.

Steps:
  A1  — Registry + file_index confirmation
  A2  — Schema version check
  A3  — Load all wa_verse_records for each file_id
  A3a — Span back-population (new in v4): set span_strong_match for pre-v9 rows
  A4  — Refresh wa_term_inventory from STEP (vocab re-fetch; non-destructive)
  A5  — Meaning parser refresh (run_parser_for_file)
  A6  — Flag engine refresh
  A7  — Audit (WR-01–WR-20)
  A8  — Write SPAN_BACK_POPULATED flag (id=25)
  A9  — Update wa_file_index.testament_coverage
  A10 — Update word_registry
"""

from __future__ import annotations

import sys
import os
from datetime import datetime, timezone

_ROOT = os.path.join(os.path.dirname(__file__), "..")
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from analytics.step_client import StepClient

from .constants import (
    EXPECTED_SCHEMA_VERSION,
    LOCK_SENTINEL,
)
from .db import get_schema_version
from .audit import run_audit
from .flag_engine import run_flag_engine, _flag_id
from .meaning_parser import run_parser_for_file
from .run_log import (
    make_run_id, open_run, close_run,
    write_word_run_state,
)
from .span_filter import apply_span_filter


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def run_audit_word(conn, registry_id: int,
                   dry_run: bool = False,
                   skip_span_backpop: bool = False) -> dict:
    """Execute AUDIT_WORD mode for a single registry entry.

    Args:
        conn:               Open database connection.
        registry_id:        word_registry.no for the target word.
        dry_run:            If True, analyse only; no writes.
        skip_span_backpop:  If True, skip A3a span back-population.

    Returns:
        {"outcome": str, "run_id": str, "audit_result": str, "details": dict}
    """
    run_id = make_run_id("AUDIT_WORD")
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

    if not dry_run:
        open_run(conn, run_id, "AUDIT_WORD", [registry_id])

    print(f"\n=== AUDIT_WORD run {run_id} | registry {registry_id} ===")

    # ── A1: Registry + file_index confirmation ────────────────────────────────
    print("A1  Registry confirmation...")
    reg_row = conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone()
    if not reg_row:
        return _stop(f"A1: No word_registry row for no={registry_id}")

    word = reg_row["word"]
    fi_rows = conn.execute(
        "SELECT id FROM wa_file_index WHERE registry_id = ?",
        (str(registry_id),),
    ).fetchall()
    if not fi_rows:
        return _stop(
            f"A1: No wa_file_index rows for registry {registry_id}. "
            "Run engine --mode=new_word first."
        )
    file_ids = [r["id"] for r in fi_rows]
    print(f"     Word: {word} | file_ids: {file_ids}")

    # ── A2: Schema version check ───────────────────────────────────────────────
    print("A2  Schema version check...")
    schema_ver = get_schema_version(conn)
    if schema_ver != EXPECTED_SCHEMA_VERSION:
        return _stop(
            f"A2: Schema version mismatch — found {schema_ver!r}, "
            f"expected {EXPECTED_SCHEMA_VERSION!r}."
        )

    # ── A3: Load verse records ─────────────────────────────────────────────────
    print("A3  Loading verse records...")
    total_vr = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_verse_records WHERE file_id IN ({})".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchone()["c"]
    print(f"     {total_vr} verse records across {len(file_ids)} file(s).")

    # ── A3a: Span back-population ──────────────────────────────────────────────
    backpop_count = 0
    backpop_filtered = 0

    if not skip_span_backpop:
        print("A3a Span back-population (span_strong_match for pre-v9 verses)...")
        client = StepClient()

        # Find verse records without span_strong_match set
        null_span_rows = conn.execute(
            """SELECT vr.id, vr.term_id, vr.reference, vr.term_inv_id,
                      ti.strongs_number
               FROM wa_verse_records vr
               JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
               WHERE vr.file_id IN ({})
               AND vr.span_strong_match IS NULL""".format(
                ",".join("?" * len(file_ids))),
            file_ids,
        ).fetchall()

        print(f"     {len(null_span_rows)} rows need span_strong_match set.")

        if null_span_rows and not dry_run:
            # Group by strongs_number to batch STEP HTML fetches
            by_strongs: dict[str, list] = {}
            for row in null_span_rows:
                strongs = row["strongs_number"] or row["term_id"]
                by_strongs.setdefault(strongs, []).append(row)

            for strongs, rows in by_strongs.items():
                try:
                    _records, html_map = client.get_verse_records_with_html(strongs)
                except Exception as exc:
                    errors.append(f"A3a: verse fetch failed for {strongs}: {exc}")
                    continue

                for row in rows:
                    # Find matching HTML by reference
                    osis_id = _ref_to_osis(row["reference"])
                    html = html_map.get(osis_id, "")
                    if not html:
                        # Try partial match on reference
                        html = _fuzzy_html_lookup(html_map, row["reference"])

                    if html:
                        result = apply_span_filter(html, strongs)
                        match_val = 1 if result["match"] else 0
                        target = result.get("target_word") or ""
                        conn.execute(
                            "UPDATE wa_verse_records SET span_strong_match = ?, "
                            "target_word = COALESCE(target_word, NULLIF(?, '')) WHERE id = ?",
                            (match_val, target, row["id"]),
                        )
                        if match_val == 1:
                            backpop_count += 1
                        else:
                            backpop_filtered += 1
                    else:
                        # No HTML for this verse in STEP — set to 0 (cannot confirm)
                        conn.execute(
                            "UPDATE wa_verse_records SET span_strong_match = 0 WHERE id = ?",
                            (row["id"],),
                        )
                        backpop_filtered += 1

            conn.commit()
            print(f"     A3a: set match=1 on {backpop_count}, filtered {backpop_filtered} verse rows.")

        elif dry_run and null_span_rows:
            print(f"     [DRY-RUN] Would back-populate {len(null_span_rows)} rows.")

    # ── A4: Refresh wa_term_inventory from STEP ───────────────────────────────
    print("A4  Refreshing term inventory from STEP...")
    if not dry_run:
        client_local = StepClient()
        for file_id in file_ids:
            terms = conn.execute(
                "SELECT id, strongs_number, term_id FROM wa_term_inventory WHERE file_id = ?",
                (file_id,),
            ).fetchall()
            for t in terms:
                strongs = t["strongs_number"] or t["term_id"]
                try:
                    vocab = client_local.get_vocab_info(strongs)
                    if not vocab:
                        continue
                    medium_def = vocab.get("medium_def", "")
                    conn.execute(
                        """UPDATE wa_term_inventory SET
                               step_search_gloss   = COALESCE(NULLIF(step_search_gloss, ''), ?),
                               word_analysis_gloss = COALESCE(NULLIF(word_analysis_gloss, ''), ?),
                               meaning             = COALESCE(NULLIF(meaning, ''), ?),
                               meaning_numbered    = COALESCE(NULLIF(meaning_numbered, ''), ?),
                               occurrence_count    = COALESCE(occurrence_count, ?),
                               lsj_entry           = COALESCE(NULLIF(lsj_entry, ''), ?),
                               short_def_mounce    = COALESCE(NULLIF(short_def_mounce, ''), ?)
                           WHERE id = ?""",
                        (
                            vocab.get("gloss", ""),
                            vocab.get("gloss", ""),
                            medium_def,
                            medium_def,
                            vocab.get("occurrence_count"),
                            vocab.get("lsj_entry") or None,
                            vocab.get("short_def_mounce") or None,
                            t["id"],
                        ),
                    )
                except Exception as exc:
                    errors.append(f"A4: vocab refresh failed for {strongs}: {exc}")
        conn.commit()
    print(f"     A4 complete.")

    # ── A5: Meaning parser refresh ─────────────────────────────────────────────
    print("A5  Meaning parser refresh...")
    if not dry_run:
        for file_id in file_ids:
            terms = conn.execute(
                "SELECT id, strongs_number, term_id, meaning "
                "FROM wa_term_inventory WHERE file_id = ?", (file_id,)
            ).fetchall()
            vocab_map = {}
            for t in terms:
                s = t["strongs_number"] or t["term_id"]
                if t["meaning"]:
                    vocab_map[s] = {"medium_def": t["meaning"]}
            if vocab_map:
                result = run_parser_for_file(conn, file_id, vocab_map)
                counts["total_meanings_parsed"] += result["parsed"]
    print(f"     A5: {counts['total_meanings_parsed']} meanings re-parsed.")

    # ── A6: Flag engine refresh ────────────────────────────────────────────────
    print("A6  Flag engine refresh...")
    if not dry_run:
        for file_id in file_ids:
            run_flag_engine(conn, file_id, registry_id)
    print(f"     A6 complete.")

    # ── A7: Audit (WR-01–WR-20) ───────────────────────────────────────────────
    print("A7  Running audit (WR-01–WR-20)...")
    audit_result = run_audit(conn, file_ids[0], registry_id)
    for check in audit_result["checks"]:
        if check["result"] != "PASS":
            print(f"     {check['result']:6} {check['check']}: {check['detail']}")

    if not dry_run:
        write_word_run_state(
            conn, run_id, registry_id, word,
            "AUDIT_WORD_A7",
            audit_result["result"],
            {c["check"]: {"r": c["result"], "d": c["detail"]} for c in audit_result["checks"]},
            audit_result.get("stop_reason"),
        )

    print(f"     A7: {audit_result['result']}")

    # ── A8: Write SPAN_BACK_POPULATED flag ────────────────────────────────────
    if not skip_span_backpop and not dry_run and null_span_rows:
        print("A8  Writing SPAN_BACK_POPULATED quality flag...")
        fid = _flag_id(conn, "SPAN_BACK_POPULATED")
        if fid:
            for file_id in file_ids:
                conn.execute(
                    """INSERT OR IGNORE INTO wa_data_quality_flags
                           (file_id, term_id, flag_id, description)
                       VALUES (?, NULL, ?, ?)""",
                    (file_id, fid,
                     f"AUDIT_WORD A3a back-populated {backpop_count} verse rows. "
                     f"{backpop_filtered} filtered (span_strong_match=0)."),
                )
        conn.commit()
        print(f"     A8: flag written.")

    # ── A9: Update testament_coverage ─────────────────────────────────────────
    print("A9  Refreshing testament_coverage...")
    if not dry_run:
        for file_id in file_ids:
            testaments = {
                r["testament"]
                for r in conn.execute(
                    "SELECT DISTINCT testament FROM wa_verse_records "
                    "WHERE file_id = ? AND (span_strong_match = 1 OR span_strong_match IS NULL)",
                    (file_id,),
                ).fetchall()
            }
            tc = (
                "OT_only" if testaments == {"OT"} else
                "NT_only" if testaments == {"NT"} else
                "both"    if testaments else None
            )
            conn.execute(
                "UPDATE wa_file_index SET testament_coverage = ? WHERE id = ?",
                (tc, file_id),
            )
        conn.commit()
    print(f"     A9 complete.")

    # ── A10: Update word_registry ─────────────────────────────────────────────
    print("A10 Updating word_registry...")
    if not dry_run:
        verse_count = conn.execute(
            """SELECT COUNT(*) AS c FROM wa_verse_records
               WHERE file_id IN ({}) AND (span_strong_match = 1 OR span_strong_match IS NULL)""".format(
                ",".join("?" * len(file_ids))),
            file_ids,
        ).fetchone()["c"]
        term_count = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_term_inventory WHERE file_id IN ({})".format(
                ",".join("?" * len(file_ids))),
            file_ids,
        ).fetchone()["c"]
        final_status = (
            reg_row["phase1_status"]
            if audit_result["result"] == "PASS"
            else "In Progress"
        )
        conn.execute(
            """UPDATE word_registry SET
                   phase1_term_count   = ?,
                   phase1_verse_count  = ?,
                   last_automation_run = ?,
                   automation_run_id   = ?
               WHERE no = ?""",
            (term_count, verse_count, _now(), run_id, registry_id),
        )
        conn.commit()
        counts["words_complete"] = 1

    close_run(conn, run_id, "COMPLETE", counts)

    print(f"\n=== AUDIT_WORD complete: {word} | {audit_result['result']} ===")
    return {
        "outcome": "COMPLETE",
        "run_id": run_id,
        "audit_result": audit_result["result"],
        "details": {
            "backpop_confirmed": backpop_count,
            "backpop_filtered": backpop_filtered,
            "meanings_parsed": counts["total_meanings_parsed"],
        },
    }


# ── Helpers ───────────────────────────────────────────────────────────────────

def _ref_to_osis(reference: str) -> str:
    """Convert a reference like 'Gen 1:1' to an OSIS ID like 'Gen.1.1'.
    Returns empty string if conversion fails.
    """
    import re
    m = re.match(r"^(.+?)\s+(\d+):(\d+)$", reference.strip())
    if not m:
        return ""
    book_name, ch, vs = m.group(1), m.group(2), m.group(3)
    # Best-effort: map common abbreviations
    _BOOK_MAP = {
        "Gen": "Gen", "Exod": "Exod", "Lev": "Lev", "Num": "Num",
        "Deut": "Deut", "Josh": "Josh", "Judg": "Judg", "Ruth": "Ruth",
        "1 Sam": "1Sam", "2 Sam": "2Sam", "1 Kgs": "1Kgs", "2 Kgs": "2Kgs",
        "1 Chr": "1Chr", "2 Chr": "2Chr", "Ezra": "Ezra", "Neh": "Neh",
        "Esth": "Esth", "Job": "Job", "Ps": "Ps", "Prov": "Prov",
        "Eccl": "Eccl", "Song": "Song", "Isa": "Isa", "Jer": "Jer",
        "Lam": "Lam", "Ezek": "Ezek", "Dan": "Dan", "Hos": "Hos",
        "Joel": "Joel", "Amos": "Amos", "Obad": "Obad", "Jonah": "Jonah",
        "Mic": "Mic", "Nah": "Nah", "Hab": "Hab", "Zeph": "Zeph",
        "Hag": "Hag", "Zech": "Zech", "Mal": "Mal",
        "Matt": "Matt", "Mark": "Mark", "Luke": "Luke", "John": "John",
        "Acts": "Acts", "Rom": "Rom", "1 Cor": "1Cor", "2 Cor": "2Cor",
        "Gal": "Gal", "Eph": "Eph", "Phil": "Phil", "Col": "Col",
        "1 Thess": "1Thess", "2 Thess": "2Thess", "1 Tim": "1Tim",
        "2 Tim": "2Tim", "Titus": "Titus", "Phlm": "Phlm", "Heb": "Heb",
        "Jas": "Jas", "1 Pet": "1Pet", "2 Pet": "2Pet",
        "1 John": "1John", "2 John": "2John", "3 John": "3John",
        "Jude": "Jude", "Rev": "Rev",
        # Common alternates
        "Ps.": "Ps", "Song of Sol": "Song", "Song of Songs": "Song",
    }
    short = _BOOK_MAP.get(book_name)
    if short:
        return f"{short}.{ch}.{vs}"
    # Fallback: strip spaces and punctuation
    cleaned = re.sub(r"\s+", "", book_name).rstrip(".")
    return f"{cleaned}.{ch}.{vs}"


def _fuzzy_html_lookup(html_map: dict[str, str], reference: str) -> str:
    """Try to find HTML in html_map for a given reference string.
    Returns empty string if not found.
    """
    osis = _ref_to_osis(reference)
    if osis and osis in html_map:
        return html_map[osis]
    # Last-resort: partial key match on book+chapter+verse
    for key, html in html_map.items():
        if osis and osis.lower() in key.lower():
            return html
    return ""
