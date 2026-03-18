"""
gap_fill.py
───────────
GAP_FILL mode — steps S1 through S8.

Operates on already-imported words that have missing data in one or more streams.
Runs streams independently; each stream is idempotent and checkpointed.

Streams:
  S1  — phase1_status gate + lock
  S2  — identify gap streams required
  S3  — verse gap-fill (re-fetch + span filter for terms with 0 verses)
  S4  — meaning gap-fill (terms with meaning IS NULL)
  S5  — flag engine refresh
  S6  — audit refresh (WR-01–WR-20)
  S7  — registry update
  S8  — lock release
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
from .db import get_max_id, get_book_id, get_schema_version
from .audit import run_audit
from .flag_engine import run_flag_engine
from .meaning_parser import run_parser_for_file
from .run_log import (
    make_run_id, open_run, close_run,
    write_word_run_state, log_fetch, upsert_checkpoint,
)
from .span_filter import filter_verse_records


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def run_gap_fill(conn, registry_id: int,
                 streams: list[str] | None = None,
                 dry_run: bool = False) -> dict:
    """Run GAP_FILL mode for a single registry entry.

    Args:
        conn:         Open database connection.
        registry_id:  word_registry.no for the target word.
        streams:      Subset of streams to run, e.g. ['S3', 'S4']. None = all.
        dry_run:      If True, identify gaps only; no writes.

    Returns:
        {"outcome": str, "run_id": str, "streams_run": list[str], "details": dict}
    """
    ALL_STREAMS = ["S3", "S4", "S5", "S6"]
    active_streams = streams if streams else ALL_STREAMS
    run_id = make_run_id("GAP_FILL")
    errors = []
    counts = {
        "words_attempted": 1, "words_complete": 0, "words_stopped": 0,
        "total_terms_new": 0, "total_terms_xref": 0,
        "total_verses_inserted": 0, "total_verses_filtered": 0,
        "total_meanings_parsed": 0, "errors": errors,
    }
    streams_run = []

    def _stop(msg: str) -> dict:
        counts["words_stopped"] = 1
        errors.append(msg)
        print(f"\n  [STOP] {msg}")
        if not dry_run:
            try:
                close_run(conn, run_id, "STOPPED", counts)
            except Exception:
                pass
        return {"outcome": "STOPPED", "run_id": run_id, "streams_run": streams_run,
                "details": errors}

    def _review(msg: str) -> None:
        print(f"\n  [REVIEW] {msg}")

    if not dry_run:
        open_run(conn, run_id, "GAP_FILL", [registry_id])

    print(f"\n=== GAP_FILL run {run_id} | registry {registry_id} ===")

    # ── S1: phase1_status gate + lock ─────────────────────────────────────────
    print("S1  Status gate + lock...")
    reg_row = conn.execute(
        "SELECT * FROM word_registry WHERE no = ?", (registry_id,)
    ).fetchone()
    if not reg_row:
        return _stop(f"S1: No word_registry row for no={registry_id}")

    word = reg_row["word"]
    status = reg_row["phase1_status"]
    if status not in ("In Progress", "Complete", "Pending"):
        return _stop(f"S1: Unexpected phase1_status='{status}' for registry {registry_id}.")

    # Schema version check
    schema_ver = get_schema_version(conn)
    if schema_ver != EXPECTED_SCHEMA_VERSION:
        return _stop(
            f"S1: Schema version mismatch — found {schema_ver!r}, "
            f"expected {EXPECTED_SCHEMA_VERSION!r}."
        )

    if not dry_run:
        existing_lock = reg_row["last_automation_run"]
        if existing_lock == LOCK_SENTINEL:
            return _stop(
                f"S1: IN_PROGRESS lock already set for registry {registry_id}. "
                f"Use: engine.py --clear-lock --registry={registry_id}"
            )
        conn.execute(
            "UPDATE word_registry SET last_automation_run = ? WHERE no = ?",
            (LOCK_SENTINEL, registry_id),
        )
        conn.commit()

    # ── S2: Identify gap streams ───────────────────────────────────────────────
    print("S2  Identifying gaps...")
    fi_rows = conn.execute(
        "SELECT id FROM wa_file_index WHERE registry_id = ?",
        (str(registry_id),),
    ).fetchall()
    if not fi_rows:
        if not dry_run:
            conn.execute(
                "UPDATE word_registry SET last_automation_run = NULL WHERE no = ?",
                (registry_id,),
            )
            conn.commit()
        return _stop(
            f"S2: No wa_file_index rows for registry {registry_id}. "
            "Run engine --mode=new_word first."
        )

    file_ids = [r["id"] for r in fi_rows]
    print(f"     {len(file_ids)} wa_file_index entries: {file_ids}")

    # Detect which streams have actual gaps
    gaps = {}

    # S3 gap: terms with zero confirmed verses
    zero_verse_terms = conn.execute(
        """SELECT ti.id, ti.strongs_number, ti.term_id
           FROM wa_term_inventory ti
           WHERE ti.file_id IN ({})
           AND NOT EXISTS (
               SELECT 1 FROM wa_verse_records vr
               WHERE vr.term_inv_id = ti.id AND (vr.span_strong_match = 1 OR vr.span_strong_match IS NULL)
           )""".format(",".join("?" * len(file_ids))),
        file_ids,
    ).fetchall()
    gaps["S3"] = [{"ti_id": r["id"], "strongs": r["strongs_number"] or r["term_id"]}
                  for r in zero_verse_terms]

    # S4 gap: terms with missing meaning
    no_meaning_terms = conn.execute(
        """SELECT ti.id, ti.strongs_number, ti.term_id
           FROM wa_term_inventory ti
           WHERE ti.file_id IN ({}) AND (ti.meaning IS NULL OR ti.meaning = '')""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchall()
    gaps["S4"] = [{"ti_id": r["id"], "strongs": r["strongs_number"] or r["term_id"]}
                  for r in no_meaning_terms]

    print(f"     S3 gaps (zero verses): {len(gaps['S3'])}  "
          f"S4 gaps (no meaning): {len(gaps['S4'])}")

    if dry_run:
        close_run(conn, run_id, "DRY_RUN", counts) if not dry_run else None
        return {
            "outcome": "DRY_RUN", "run_id": run_id, "streams_run": [],
            "details": gaps,
        }

    # ── S3: Verse gap-fill ─────────────────────────────────────────────────────
    if "S3" in active_streams and gaps["S3"]:
        print(f"S3  Verse gap-fill ({len(gaps['S3'])} terms)...")
        upsert_checkpoint(conn, run_id, "S3", "running")
        client = StepClient()
        span_conflicts: set[str] = set()
        s3_inserted = 0
        s3_filtered = 0

        for gap in gaps["S3"]:
            strongs = gap["strongs"]
            ti_id = gap["ti_id"]
            try:
                raw_records, html_map = client.get_verse_records_with_html(strongs)
                # Get resolved strong from vocab
                resolved = strongs
                ti_row = conn.execute(
                    "SELECT strongs_number, term_id, transliteration, file_id "
                    "FROM wa_term_inventory WHERE id = ?", (ti_id,)
                ).fetchone()
                file_id = ti_row["file_id"]

                filter_result = filter_verse_records(raw_records, resolved, html_map)
                stored   = filter_result["stored"]
                filtered = filter_result["filtered"]
                conflict = filter_result["conflict"]

                if conflict:
                    span_conflicts.add(strongs)

                for rec in stored:
                    book_id = get_book_id(conn, rec["book_code"])
                    if not book_id:
                        errors.append(f"S3: Unknown book code {rec['book_code']!r}")
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
                            ti_row["transliteration"] or "",
                            book_id,
                            rec["ref"], rec["chapter"], rec["verse_num"],
                            rec["testament"],
                            rec["esv_text"],
                            rec.get("target_word", ""),
                            rec.get("span_strong_match", 1),
                        ),
                    )
                    s3_inserted += 1
                s3_filtered += len(filtered)

                log_fetch(
                    conn, run_id, registry_id, strongs, resolved, 0,
                    "ok", "zero_results" if not stored else "ok",
                    len(raw_records), len(stored), len(filtered),
                    1 if conflict else 0, None,
                )

            except Exception as exc:
                errors.append(f"S3: failed for {strongs}: {exc}")

        conn.commit()
        counts["total_verses_inserted"] += s3_inserted
        counts["total_verses_filtered"] += s3_filtered
        upsert_checkpoint(conn, run_id, "S3", "complete",
                          rows_written=s3_inserted, rows_filtered=s3_filtered)
        streams_run.append("S3")
        print(f"     S3: inserted {s3_inserted}, filtered {s3_filtered}")

    # ── S4: Meaning gap-fill ───────────────────────────────────────────────────
    if "S4" in active_streams and gaps["S4"]:
        print(f"S4  Meaning gap-fill ({len(gaps['S4'])} terms)...")
        upsert_checkpoint(conn, run_id, "S4", "running")
        client = StepClient()
        s4_parsed = 0

        for gap in gaps["S4"]:
            strongs = gap["strongs"]
            ti_id = gap["ti_id"]
            try:
                vocab = client.get_vocab_info(strongs)
                if not vocab:
                    errors.append(f"S4: No vocab data for {strongs}")
                    continue
                medium_def = vocab.get("medium_def", "")
                if medium_def:
                    conn.execute(
                        """UPDATE wa_term_inventory
                           SET meaning = ?, meaning_numbered = ?,
                               step_search_gloss = COALESCE(step_search_gloss, ?),
                               word_analysis_gloss = COALESCE(word_analysis_gloss, ?)
                           WHERE id = ?""",
                        (medium_def, medium_def,
                         vocab.get("gloss", ""), vocab.get("gloss", ""),
                         ti_id),
                    )
                lsj = vocab.get("lsj_entry", "")
                if lsj:
                    conn.execute(
                        "UPDATE wa_term_inventory SET lsj_entry = COALESCE(lsj_entry, ?) WHERE id = ?",
                        (lsj, ti_id),
                    )
                s4_parsed += 1

            except Exception as exc:
                errors.append(f"S4: failed for {strongs}: {exc}")

        conn.commit()

        # Re-run meaning parser with freshly fetched data
        for file_id in file_ids:
            terms = conn.execute(
                "SELECT id, strongs_number, term_id, language, meaning "
                "FROM wa_term_inventory WHERE file_id = ?", (file_id,)
            ).fetchall()
            vocab_map = {
                (r["strongs_number"] or r["term_id"]): {"medium_def": r["meaning"]}
                for r in terms if r["meaning"]
            }
            if vocab_map:
                run_parser_for_file(conn, file_id, vocab_map)

        counts["total_meanings_parsed"] += s4_parsed
        upsert_checkpoint(conn, run_id, "S4", "complete", rows_written=s4_parsed)
        streams_run.append("S4")
        print(f"     S4: updated {s4_parsed} terms.")

    # ── S5: Flag engine refresh ───────────────────────────────────────────────
    if "S5" in active_streams:
        print("S5  Flag engine refresh...")
        upsert_checkpoint(conn, run_id, "S5", "running")
        s5_flags = 0
        s5_conflicts = span_conflicts if "S3" in streams_run else set()
        for file_id in file_ids:
            result = run_flag_engine(conn, file_id, registry_id, s5_conflicts)
            s5_flags += result["flags_written"]
        upsert_checkpoint(conn, run_id, "S5", "complete", rows_written=s5_flags)
        streams_run.append("S5")
        print(f"     S5: {s5_flags} flags written.")

    # ── S6: Audit refresh ─────────────────────────────────────────────────────
    if "S6" in active_streams:
        print("S6  Audit refresh (WR-01–WR-20)...")
        upsert_checkpoint(conn, run_id, "S6", "running")
        # Run audit per file_id (use the first/only in typical case)
        audit_result = run_audit(conn, file_ids[0], registry_id)
        for check in audit_result["checks"]:
            if check["result"] != "PASS":
                print(f"     {check['result']:6} {check['check']}: {check['detail']}")
        write_word_run_state(
            conn, run_id, registry_id, word, "GAP_FILL_S6",
            audit_result["result"],
            {c["check"]: {"r": c["result"], "d": c["detail"]} for c in audit_result["checks"]},
            audit_result.get("stop_reason"),
        )
        upsert_checkpoint(conn, run_id, "S6", "complete")
        streams_run.append("S6")
        print(f"     S6: Audit result — {audit_result['result']}")

    # ── S7: Registry update ───────────────────────────────────────────────────
    print("S7  Updating word_registry...")
    audit_res = (
        audit_result["result"]
        if "S6" in streams_run
        else conn.execute(
            "SELECT audit_result FROM word_run_state WHERE registry_id = ? "
            "ORDER BY id DESC LIMIT 1",
            (str(registry_id).zfill(3),),
        ).fetchone()["audit_result"]
        if conn.execute(
            "SELECT id FROM word_run_state WHERE registry_id = ? LIMIT 1",
            (str(registry_id).zfill(3),),
        ).fetchone() else "UNKNOWN"
    )

    final_status = "In Progress" if audit_res in ("STOP", "REVIEW", "UNKNOWN") else reg_row["phase1_status"]

    # Recount verses
    verse_count = conn.execute(
        """SELECT COUNT(*) AS c FROM wa_verse_records
           WHERE file_id IN ({}) AND (span_strong_match = 1 OR span_strong_match IS NULL)""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchone()["c"]

    # Recount terms
    term_count = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_term_inventory WHERE file_id IN ({})".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchone()["c"]

    conn.execute(
        """UPDATE word_registry SET
               phase1_status       = ?,
               phase1_term_count   = ?,
               phase1_verse_count  = ?,
               last_automation_run = ?,
               automation_run_id   = ?
           WHERE no = ?""",
        (final_status, term_count, verse_count, _now(), run_id, registry_id),
    )
    conn.commit()
    print(f"     S7: status={final_status}, terms={term_count}, verses={verse_count}")

    # ── S8: Lock release ──────────────────────────────────────────────────────
    print("S8  Lock release...")
    # Lock was already overwritten in S7 (last_automation_run = run_id).
    # Nothing additional required; IN_PROGRESS is gone.
    streams_run.append("S7")
    streams_run.append("S8")

    counts["words_complete"] = 1
    close_run(conn, run_id, "COMPLETE", counts)

    print(f"\n=== GAP_FILL complete: {word} | {final_status} | streams: {streams_run} ===")
    return {
        "outcome": "COMPLETE",
        "run_id": run_id,
        "streams_run": streams_run,
        "details": {
            "verses_inserted": counts["total_verses_inserted"],
            "verses_filtered": counts["total_verses_filtered"],
            "meanings_updated": counts["total_meanings_parsed"],
            "audit_result": audit_res,
        },
    }
