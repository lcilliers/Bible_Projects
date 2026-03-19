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

import json
import re
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
from .db import get_schema_version, get_book_id, get_max_id
from .audit import run_audit
from .flag_engine import run_flag_engine, _flag_id
from .meaning_parser import run_parser_for_file
from .run_log import (
    make_run_id, open_run, close_run,
    write_word_run_state,
)
from .span_filter import apply_span_filter, filter_verse_records


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

    # ── A3a: Verse sync ────────────────────────────────────────────────────────
    backpop_count = 0
    backpop_filtered = 0
    inserted_count = 0
    updated_count  = 0
    orphan_count   = 0

    if not skip_span_backpop:
        print("A3a Verse sync (INSERT missing, UPDATE nulls, mark orphans)...")
        client_a3 = StepClient()
        book_misses: list = []

        for fid in file_ids:
            term_rows = conn.execute(
                """SELECT id, strongs_number, term_id, transliteration, status_note
                   FROM wa_term_inventory WHERE file_id = ?""",
                (fid,),
            ).fetchall()

            for ti in term_rows:
                # Skip terms explicitly marked as having no separate verse record
                if ti["status_note"] and "no separate verse record" in ti["status_note"].lower():
                    continue

                strongs = ti["strongs_number"] or ti["term_id"]
                ti_id   = ti["id"]

                # Fetch from STEP
                try:
                    raw_records, html_map = client_a3.get_verse_records_with_html(strongs)
                except Exception as exc:
                    errors.append(f"A3a: verse fetch failed for {strongs}: {exc}")
                    continue

                filter_result = filter_verse_records(raw_records, strongs, html_map)
                step_verses   = filter_result["stored"]   # list of dicts with ref etc.
                step_refs     = {r["ref"] for r in step_verses}

                # Existing rows in table for this term_inv
                existing_rows = conn.execute(
                    """SELECT id, reference, span_strong_match, target_word, verse_text
                       FROM wa_verse_records WHERE term_inv_id = ?""",
                    (ti_id,),
                ).fetchall()
                existing_by_ref = {r["reference"]: r for r in existing_rows}
                existing_refs   = set(existing_by_ref.keys())

                if not dry_run:
                    # INSERT: in STEP but not in table
                    for rec in step_verses:
                        ref = rec["ref"]
                        if ref in existing_refs:
                            continue
                        book_id = get_book_id(conn, rec["book_code"])
                        if book_id is None:
                            book_misses.append(rec["book_code"])
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
                                vr_id, fid, ti_id, strongs,
                                ti["transliteration"] or "",
                                book_id, ref, rec["chapter"], rec["verse_num"],
                                rec["testament"], rec["esv_text"],
                                rec.get("target_word", ""),
                                rec.get("span_strong_match", 1),
                            ),
                        )
                        inserted_count += 1

                    # UPDATE: rows in both — overwrite all STEP-sourced fields.
                    # Early-stage data may be stale/incomplete; audit is the
                    # canonical refresh pass so we always write the latest values.
                    for rec in step_verses:
                        ref = rec["ref"]
                        if ref not in existing_refs:
                            continue
                        row = existing_by_ref[ref]
                        updates = ["span_strong_match = ?"]
                        params  = [rec.get("span_strong_match", 1)]
                        if rec.get("target_word"):
                            updates.append("target_word = ?")
                            params.append(rec["target_word"])
                        if rec.get("esv_text"):
                            updates.append("verse_text = ?")
                            params.append(rec["esv_text"])
                        if rec.get("context_before") is not None:
                            updates.append("context_before = ?")
                            params.append(rec["context_before"])
                        if rec.get("context_after") is not None:
                            updates.append("context_after = ?")
                            params.append(rec["context_after"])
                        params.append(row["id"])
                        conn.execute(
                            f"UPDATE wa_verse_records SET {', '.join(updates)} WHERE id = ?",
                            params,
                        )
                        updated_count += 1

                    # MARK ORPHANS: in table but not in STEP — set span_strong_match = -1
                    orphan_refs = existing_refs - step_refs
                    for ref in orphan_refs:
                        row = existing_by_ref[ref]
                        if row["span_strong_match"] != -1:
                            conn.execute(
                                "UPDATE wa_verse_records SET span_strong_match = -1 WHERE id = ?",
                                (row["id"],),
                            )
                            orphan_count += 1
                else:
                    # dry-run counts
                    inserted_count += len(step_refs - existing_refs)
                    updated_count  += sum(
                        1 for rec in step_verses
                        if rec["ref"] in existing_refs
                        and existing_by_ref[rec["ref"]]["span_strong_match"] is None
                    )
                    orphan_count += len(existing_refs - step_refs)

        if not dry_run:
            conn.commit()

        # Totals for counts
        backpop_count    = inserted_count + updated_count
        backpop_filtered = orphan_count

        if book_misses:
            _unique_misses = sorted(set(book_misses))
            print(
                f"\n     [BOOK_MISS] {len(_unique_misses)} unrecognized book name(s): "
                f"{_unique_misses}"
            )
            print(
                f"     To register an alias: "
                f'python -m engine.engine --add-book-code "BookName=OsisCode"'
            )

        prefix = "[DRY-RUN] Would" if dry_run else ""
        print(
            f"     A3a: {prefix} inserted={inserted_count}  "
            f"updated={updated_count}  orphans_marked={orphan_count}"
        )
        _total_vr_now = conn.execute(
            "SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN ({})".format(
                ",".join("?" * len(file_ids))), file_ids,
        ).fetchone()[0]
        print(f"     [VERIFY] total verse records now: {_total_vr_now}")

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
    if not dry_run:
        _ti_count = conn.execute(
            "SELECT COUNT(*) FROM wa_term_inventory WHERE file_id IN ({})".format(
                ",".join("?" * len(file_ids))), file_ids,
        ).fetchone()[0]
        print(f"     [VERIFY] wa_term_inventory: {_ti_count} rows")

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
    if not dry_run:
        _mp_count = conn.execute(
            "SELECT COUNT(*) FROM wa_meaning_parsed mp"
            " JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id"
            " WHERE ti.file_id IN ({})".format(",".join("?" * len(file_ids))),
            file_ids,
        ).fetchone()[0]
        print(f"     [VERIFY] wa_meaning_parsed: {_mp_count} rows")

    # ── A6: Flag engine refresh ────────────────────────────────────────────────
    print("A6  Flag engine refresh...")
    if not dry_run:
        for file_id in file_ids:
            run_flag_engine(conn, file_id, registry_id)
    print(f"     A6 complete.")
    if not dry_run:
        _flag_count = conn.execute(
            "SELECT COUNT(*) FROM wa_data_quality_flags WHERE file_id IN ({})".format(
                ",".join("?" * len(file_ids))), file_ids,
        ).fetchone()[0]
        print(f"     [VERIFY] quality flags: {_flag_count} rows")

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
    _a7_p = sum(1 for c in audit_result["checks"] if c["result"] == "PASS")
    _a7_r = sum(1 for c in audit_result["checks"] if c["result"] == "REVIEW")
    _a7_s = sum(1 for c in audit_result["checks"] if c["result"] == "STOP")
    print(f"     [VERIFY] WR checks: {_a7_p} PASS  {_a7_r} REVIEW  {_a7_s} STOP")

    # ── A8: Write SPAN_BACK_POPULATED flag ────────────────────────────────────
    if not skip_span_backpop and not dry_run and backpop_count > 0:
        print("A8  Writing SPAN_BACK_POPULATED quality flag...")
        fid = _flag_id(conn, "SPAN_BACK_POPULATED")
        if fid:
            for file_id in file_ids:
                conn.execute(
                    """INSERT OR IGNORE INTO wa_data_quality_flags
                           (file_id, term_id, flag_id, description)
                       VALUES (?, NULL, ?, ?)""",
                    (file_id, fid,
                     f"AUDIT_WORD A3a verse sync: inserted={inserted_count} "
                     f"updated={updated_count} orphans_marked={orphan_count}."),
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

# Module-level book name → OSIS code map (common abbreviations + full names).
# Override or extend at runtime via register_book_override() or
# data/osis_book_overrides.json.
_BOOK_MAP: dict[str, str] = {
    # Standard OSIS abbreviations
    "Gen": "Gen", "Exod": "Exod", "Lev": "Lev", "Num": "Num",
    "Deut": "Deut", "Josh": "Josh", "Judg": "Judg", "Ruth": "Ruth",
    "1Sam": "1Sam", "2Sam": "2Sam", "1Kgs": "1Kgs", "2Kgs": "2Kgs",
    "1Chr": "1Chr", "2Chr": "2Chr", "Ezra": "Ezra", "Neh": "Neh",
    "Esth": "Esth", "Job": "Job", "Ps": "Ps", "Prov": "Prov",
    "Eccl": "Eccl", "Song": "Song", "Isa": "Isa", "Jer": "Jer",
    "Lam": "Lam", "Ezek": "Ezek", "Dan": "Dan", "Hos": "Hos",
    "Joel": "Joel", "Amos": "Amos", "Obad": "Obad", "Jonah": "Jonah",
    "Mic": "Mic", "Nah": "Nah", "Hab": "Hab", "Zeph": "Zeph",
    "Hag": "Hag", "Zech": "Zech", "Mal": "Mal",
    "Matt": "Matt", "Mark": "Mark", "Luke": "Luke", "John": "John",
    "Acts": "Acts", "Rom": "Rom", "1Cor": "1Cor", "2Cor": "2Cor",
    "Gal": "Gal", "Eph": "Eph", "Phil": "Phil", "Col": "Col",
    "1Thess": "1Thess", "2Thess": "2Thess", "1Tim": "1Tim",
    "2Tim": "2Tim", "Titus": "Titus", "Phlm": "Phlm", "Heb": "Heb",
    "Jas": "Jas", "1Pet": "1Pet", "2Pet": "2Pet",
    "1John": "1John", "2John": "2John", "3John": "3John",
    "Jude": "Jude", "Rev": "Rev",
    # Spaced abbreviations
    "1 Sam": "1Sam", "2 Sam": "2Sam", "1 Kgs": "1Kgs", "2 Kgs": "2Kgs",
    "1 Chr": "1Chr", "2 Chr": "2Chr",
    "1 Cor": "1Cor", "2 Cor": "2Cor",
    "1 Thess": "1Thess", "2 Thess": "2Thess",
    "1 Tim": "1Tim", "2 Tim": "2Tim",
    "1 Pet": "1Pet", "2 Pet": "2Pet",
    "1 John": "1John", "2 John": "2John", "3 John": "3John",
    # Full names
    "Genesis": "Gen", "Exodus": "Exod", "Leviticus": "Lev", "Numbers": "Num",
    "Deuteronomy": "Deut", "Joshua": "Josh", "Judges": "Judg",
    "1 Samuel": "1Sam", "2 Samuel": "2Sam",
    "1 Kings": "1Kgs", "2 Kings": "2Kgs",
    "1 Chronicles": "1Chr", "2 Chronicles": "2Chr",
    "Ezra": "Ezra", "Nehemiah": "Neh", "Esther": "Esth",
    "Psalms": "Ps", "Psalm": "Ps", "Proverbs": "Prov", "Ecclesiastes": "Eccl",
    "Song of Solomon": "Song", "Song of Songs": "Song", "Song of Sol": "Song",
    "Isaiah": "Isa", "Jeremiah": "Jer", "Lamentations": "Lam",
    "Ezekiel": "Ezek", "Daniel": "Dan", "Hosea": "Hos", "Joel": "Joel",
    "Amos": "Amos", "Obadiah": "Obad", "Jonah": "Jonah", "Micah": "Mic",
    "Nahum": "Nah", "Habakkuk": "Hab", "Zephaniah": "Zeph",
    "Haggai": "Hag", "Zechariah": "Zech", "Malachi": "Mal",
    "Matthew": "Matt", "Mark": "Mark", "Luke": "Luke", "John": "John",
    "Acts": "Acts", "Romans": "Rom",
    "1 Corinthians": "1Cor", "2 Corinthians": "2Cor",
    "Galatians": "Gal", "Ephesians": "Eph", "Philippians": "Phil",
    "Colossians": "Col",
    "1 Thessalonians": "1Thess", "2 Thessalonians": "2Thess",
    "1 Timothy": "1Tim", "2 Timothy": "2Tim",
    "Titus": "Titus", "Philemon": "Phlm", "Hebrews": "Heb",
    "James": "Jas",
    "1 Peter": "1Pet", "2 Peter": "2Pet",
    "1 John": "1John", "2 John": "2John", "3 John": "3John",
    "Jude": "Jude", "Revelation": "Rev",
    # Trailing-dot variants
    "Ps.": "Ps",
}

_OVERRIDES_PATH = os.path.join(_ROOT, "data", "osis_book_overrides.json")


def _load_book_overrides() -> None:
    """Load data/osis_book_overrides.json into _BOOK_MAP at module import."""
    if os.path.isfile(_OVERRIDES_PATH):
        try:
            with open(_OVERRIDES_PATH, encoding="utf-8") as f:
                overrides: dict[str, str] = json.load(f)
            _BOOK_MAP.update(overrides)
        except Exception:
            pass


_load_book_overrides()


def register_book_override(source_name: str, osis_code: str) -> None:
    """Register a book name alias and persist it to data/osis_book_overrides.json.

    Example::
        register_book_override("Psalms", "Ps")
        # engine --add-book-code "Psalms=Ps"
    """
    _BOOK_MAP[source_name] = osis_code
    # Persist to JSON file
    existing: dict[str, str] = {}
    if os.path.isfile(_OVERRIDES_PATH):
        try:
            with open(_OVERRIDES_PATH, encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            pass
    existing[source_name] = osis_code
    os.makedirs(os.path.dirname(_OVERRIDES_PATH), exist_ok=True)
    with open(_OVERRIDES_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    print(f"[BOOK_CODE] Registered: {source_name!r} → {osis_code!r}")


    """Convert a reference like 'Gen 1:1' to an OSIS ID like 'Gen.1.1'.
    Returns empty string if conversion fails.
    """
    m = re.match(r"^(.+?)\s+(\d+):(\d+)$", reference.strip())
    if not m:
        return ""
    book_name, ch, vs = m.group(1), m.group(2), m.group(3)
    short = _BOOK_MAP.get(book_name)
    if short:
        return f"{short}.{ch}.{vs}"
    if _misses is not None:
        _misses.append(book_name)
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
