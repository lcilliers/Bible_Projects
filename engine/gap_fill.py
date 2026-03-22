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

import json
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
    SPECIFICATION,
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
            (str(registry_id),),
        ).fetchone()["audit_result"]
        if conn.execute(
            "SELECT id FROM word_run_state WHERE registry_id = ? LIMIT 1",
            (str(registry_id),),
        ).fetchone() else "UNKNOWN"
    )

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

    # All-XREF words (0 term_inventory rows) always produce REVIEW audit —
    # treat REVIEW as Complete when there are no NEW terms.
    _all_xref = term_count == 0
    final_status = (
        "Complete"
        if audit_res == "PASS" or (_all_xref and audit_res == "REVIEW")
        else "In Progress"
    )

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


def run_bulk_gap_fill(conn,
                      stages: list[str] | None = None,
                      dry_run: bool = False) -> dict:
    """Run bulk GAP_FILL across all Pending words in word_registry.

    Four sequential stages, each completing for ALL words before the next begins:

      S1 — Term discovery: get_strongs_for_word() → word_registry.strongs_list
      S2 — Vocab fetch + DB init: wa_file_index, mti_terms, wa_term_inventory
      S3 — Verse fetch + span filter: wa_verse_records
      S4 — Meaning parse + flag engine + audit; word_registry → 'In Progress'

    All discovered Strong's are written (Option C — no threshold filtering).
    Low-frequency incidental terms are flagged by the flag engine at S4.

    Args:
        conn:    Open database connection.
        stages:  Subset of stages to run (e.g. ["S1", "S2"]). None = all four.
        dry_run: If True, report what would be done; no writes.

    Returns:
        {"outcome": str, "run_id": str, "stages_run": list[str], "summary": dict}
    """
    ALL_STAGES = ["S1", "S2", "S3", "S4"]
    active_stages = stages if stages is not None else ALL_STAGES
    run_id = make_run_id("BULK_GAP_FILL")
    stages_run: list[str] = []
    errors: list[str] = []
    summary: dict = {
        "words_discovered": 0,
        "words_initialized": 0,
        "terms_inserted": 0,
        "verses_inserted": 0,
        "verses_filtered": 0,
        "meanings_parsed": 0,
        "errors": errors,
    }

    if not dry_run:
        open_run(conn, run_id, "GAP_FILL", [])

    print(f"\n=== BULK_GAP_FILL run {run_id} ===")

    # Load all Pending words upfront for S1 scope reporting.
    pending_all = conn.execute(
        "SELECT no, id, word, strongs_list, source_list "
        "FROM word_registry WHERE phase1_status = 'Pending' ORDER BY no"
    ).fetchall()
    print(f"     Pending words total: {len(pending_all)}")

    # Only bail out early if no Pending words AND the request is purely S1/S2 work.
    # S3 and S4 use specification-scoped queries and are not blocked by pending_all.
    early_stages = {"S1", "S2"}
    if not pending_all and not dry_run and set(active_stages).issubset(early_stages):
        open_run_counts = {
            "words_attempted": 0, "words_complete": 0, "words_stopped": 0,
            "total_terms_new": 0, "total_terms_xref": 0,
            "total_verses_inserted": 0, "total_verses_filtered": 0,
            "total_meanings_parsed": 0, "errors": errors,
        }
        close_run(conn, run_id, "COMPLETE", open_run_counts)
        return {"outcome": "COMPLETE", "run_id": run_id,
                "stages_run": [], "summary": summary}

    # ── S1: Term discovery (English → Strong's) ───────────────────────────────
    if "S1" in active_stages:
        needs_discovery = [r for r in pending_all if not r["strongs_list"]]
        already_done    = len(pending_all) - len(needs_discovery)
        print(f"\nS1  Term discovery — {len(needs_discovery)} to discover, "
              f"{already_done} already populated...")
        if not dry_run:
            upsert_checkpoint(conn, run_id, "S1", "running")
        client = StepClient()
        s1_done = already_done

        for reg in needs_discovery:
            word = reg["word"]
            registry_no = reg["no"]
            try:
                results = client.get_strongs_for_word(word)
                if not dry_run:
                    conn.execute(
                        "UPDATE word_registry SET strongs_list = ? WHERE no = ?",
                        (json.dumps(results), registry_no),
                    )
                    conn.commit()
                s1_done += 1
                top = results[0]["strong"] if results else "none"
                print(f"     [{registry_no:3}] {word}: {len(results)} terms  "
                      f"(top: {top})")
            except Exception as exc:
                errors.append(f"S1: [{registry_no}] {word}: {exc}")
                print(f"     [{registry_no:3}] {word}: ERROR — {exc}")

        summary["words_discovered"] = s1_done
        if not dry_run:
            upsert_checkpoint(conn, run_id, "S1", "complete", rows_written=s1_done)
        stages_run.append("S1")
        print(f"     S1 complete: {s1_done}/{len(pending_all)} words have strongs_list")

    # ── S2: DB init + NEW/XREF classification + vocab fetch ───────────────────
    if "S2" in active_stages:
        # Reload so S1-populated strongs_list is visible.
        pending_s2 = conn.execute(
            "SELECT no, id, word, strongs_list, source_list "
            "FROM word_registry WHERE phase1_status = 'Pending' "
            "AND strongs_list IS NOT NULL ORDER BY no"
        ).fetchall()
        print(f"\nS2  DB init + classify + vocab ({len(pending_s2)} words with strongs_list)...")
        if not dry_run:
            upsert_checkpoint(conn, run_id, "S2", "running")
        client = StepClient()
        s2_done = 0
        s2_terms = 0
        s2_xrefs = 0

        for reg in pending_s2:
            word = reg["word"]
            registry_no = reg["no"]

            # Idempotent: skip if wa_file_index already exists for this word.
            existing_fi = conn.execute(
                "SELECT id FROM wa_file_index WHERE registry_id = ?",
                (str(registry_no),),
            ).fetchone()
            if existing_fi:
                print(f"     [{registry_no:3}] {word}: already initialized "
                      f"(file_id={existing_fi['id']}) — skipping")
                s2_done += 1
                continue

            strongs_data: list[dict] = json.loads(reg["strongs_list"])
            strongs_numbers = [d["strong"] for d in strongs_data]

            if dry_run:
                new_count = sum(
                    1 for s in strongs_numbers
                    if not conn.execute(
                        "SELECT id FROM mti_terms WHERE strongs_number = ?", (s,)
                    ).fetchone()
                )
                print(f"     [{registry_no:3}] {word}: {len(strongs_numbers)} terms "
                      f"(NEW={new_count} XREF={len(strongs_numbers)-new_count}) DRY RUN")
                s2_done += 1
                continue

            # ── Phase A: Write wa_file_index + classify NEW/XREF ──────────────
            # wa_file_index is committed BEFORE any API calls so the anchor
            # persists even if Phase B/C partially fails.
            new_terms: list[str] = []
            xref_terms: list[tuple[str, int]] = []  # (strong, mti_term_id)
            file_id = -1
            try:
                with conn:
                    file_id = get_max_id(conn, "wa_file_index") + 1
                    conn.execute(
                        """INSERT INTO wa_file_index
                               (id, filename, registry_id, word_registry_fk, word,
                                part_number, total_parts, is_split,
                                specification, phase, produced_date, translation_used,
                                source_list, testament_coverage)
                           VALUES (?, ?, ?, ?, ?, NULL, NULL, 0, ?, 'Phase 1', ?, 'ESV', ?, NULL)""",
                        (
                            file_id, run_id,
                            str(registry_no), reg["id"], word,
                            SPECIFICATION, _today(),
                            reg["source_list"],
                        ),
                    )

                    for strong in strongs_numbers:
                        existing_mt = conn.execute(
                            "SELECT id FROM mti_terms WHERE strongs_number = ?",
                            (strong,),
                        ).fetchone()
                        if existing_mt:
                            # XREF: Strong's already owned by another word.
                            xref_id = get_max_id(conn, "mti_term_cross_refs") + 1
                            conn.execute(
                                """INSERT OR IGNORE INTO mti_term_cross_refs
                                       (id, mti_term_id, registry, word, registry_fk)
                                   VALUES (?, ?, ?, ?, ?)""",
                                (xref_id, existing_mt["id"], str(registry_no), word, registry_no),
                            )
                            xref_terms.append((strong, existing_mt["id"]))
                        else:
                            new_terms.append(strong)

                    # Transition: Pending → In Progress at wa_file_index write.
                    conn.execute(
                        "UPDATE word_registry SET phase1_status = 'In Progress', "
                        "automation_run_id = ?, last_automation_run = ? WHERE no = ?",
                        (run_id, _now(), registry_no),
                    )

                # Phase A committed — log XREF classifications outside transaction.
                for strong, _mt_id in xref_terms:
                    log_fetch(conn, run_id, registry_no, strong, strong, 0,
                              "xref", "xref", 0, 0, 0, 0, None)
                s2_xrefs += len(xref_terms)
                print(f"     [{registry_no:3}] {word}: file_id={file_id}  "
                      f"NEW={len(new_terms)}  XREF={len(xref_terms)}")

            except Exception as exc:
                errors.append(f"S2: file_index init failed for [{registry_no}] {word}: {exc}")
                print(f"     [{registry_no:3}] {word}: ERROR in Phase A — {exc}")
                continue

            if not new_terms:
                # All terms are XREF — nothing to fetch.
                s2_done += 1
                continue

            # ── Phase B: Fetch vocab for NEW terms only ────────────────────────
            vocab_map: dict[str, dict] = {}
            for strong in new_terms:
                try:
                    vocab = client.get_vocab_info(strong)
                    if vocab:
                        vocab_map[strong] = vocab
                    else:
                        errors.append(f"S2: no vocab for {strong} [{registry_no}] {word}")
                except Exception as exc:
                    errors.append(f"S2: vocab {strong} for [{registry_no}] {word}: {exc}")

            if not vocab_map:
                errors.append(f"S2: all vocab fetches failed for [{registry_no}] {word}")
                print(f"     [{registry_no:3}] {word}: ERROR — all vocab fetches failed")
                # wa_file_index is committed; word is 'In Progress' but has no terms.
                continue

            # ── Phase C: Write mti_terms + wa_term_inventory for NEW terms ──────
            try:
                with conn:
                    term_inv_ids: dict[str, int] = {}
                    for strong in new_terms:
                        vocab = vocab_map.get(strong)
                        if not vocab:
                            continue
                        resolved = vocab["strong_number"]
                        lang = vocab.get("language", "Hebrew")

                        # mti_terms: global, idempotent — re-check inside transaction.
                        existing_mt = conn.execute(
                            "SELECT id FROM mti_terms WHERE strongs_number = ?",
                            (resolved,),
                        ).fetchone()
                        if not existing_mt:
                            mt_id = get_max_id(conn, "mti_terms") + 1
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
                                    str(registry_no), word,
                                    str(file_id),
                                    registry_no, file_id,
                                    _today(),
                                    1 if resolved != strong else 0,
                                ),
                            )
                            s2_terms += 1

                        # wa_term_inventory: one row per Strong's per file.
                        ti_id = get_max_id(conn, "wa_term_inventory") + 1
                        conn.execute(
                            """INSERT INTO wa_term_inventory
                                   (id, file_id, language, term_id, strongs_number,
                                    transliteration, step_search_gloss, word_analysis_gloss,
                                    occurrence_count, meaning, meaning_numbered,
                                    lsj_entry, short_def_mounce, testament,
                                    causative_form_present, status_note)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?, NULL)""",
                            (
                                ti_id, file_id, lang,
                                resolved, resolved,
                                vocab.get("transliteration", ""),
                                vocab.get("gloss", ""),
                                vocab.get("gloss", ""),
                                vocab.get("occurrence_count"),
                                vocab.get("medium_def"),
                                vocab.get("medium_def"),  # meaning_numbered mirrors meaning
                                vocab.get("lsj_entry") or None,
                                vocab.get("short_def_mounce") or None,
                                1 if vocab.get("causative_form_present") else 0,
                            ),
                        )
                        term_inv_ids[strong] = ti_id

                        # Related words
                        for rw in vocab.get("related_words", []):
                            conn.execute(
                                """INSERT INTO wa_term_related_words
                                       (term_inv_id, gloss, transliteration, strongs_number)
                                   VALUES (?, ?, ?, ?)""",
                                (ti_id, rw.get("gloss"), rw.get("translit"),
                                 rw.get("strong")),
                            )

                # Phase C committed — log fetch results outside transaction.
                for strong in new_terms:
                    vocab = vocab_map.get(strong)
                    if vocab:
                        resolved = vocab["strong_number"]
                        log_fetch(conn, run_id, registry_no, strong, resolved,
                                  1 if resolved != strong else 0,
                                  "ok", "pending", 0, 0, 0, 0, None)
                    else:
                        log_fetch(conn, run_id, registry_no, strong, strong, 0,
                                  "failed", "pending", 0, 0, 0, 0,
                                  ["vocab fetch returned empty"])

                s2_done += 1
                print(f"     [{registry_no:3}] {word}: {len(term_inv_ids)}/{len(new_terms)} "
                      f"NEW terms written")

            except Exception as exc:
                errors.append(f"S2: term write failed for [{registry_no}] {word}: {exc}")
                print(f"     [{registry_no:3}] {word}: ERROR in Phase C — {exc}")

        summary["words_initialized"] = s2_done
        summary["terms_inserted"] = s2_terms
        if not dry_run:
            upsert_checkpoint(conn, run_id, "S2", "complete", rows_written=s2_done)
        stages_run.append("S2")
        print(f"     S2 complete: {s2_done} words initialized, "
              f"{s2_terms} new mti_terms rows, {s2_xrefs} XREF cross-refs")

    # ── S3: Verse fetch + span filter ─────────────────────────────────────────
    if "S3" in active_stages:
        # All term_inventory rows with zero verse records, for v9-initialized words.
        ti_rows = conn.execute(
            """SELECT ti.id AS ti_id, ti.strongs_number, ti.transliteration,
                      fi.id AS file_id, fi.registry_id,
                      wr.no AS registry_no, wr.word
               FROM wa_term_inventory ti
               JOIN wa_file_index fi ON fi.id = ti.file_id
               JOIN word_registry wr ON wr.no = CAST(fi.registry_id AS INTEGER)
               WHERE fi.specification = ?
               AND NOT EXISTS (
                   SELECT 1 FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id
               )
               ORDER BY wr.no, ti.id""",
            (SPECIFICATION,),
        ).fetchall()

        print(f"\nS3  Verse fetch ({len(ti_rows)} terms with 0 verses)...")
        if not dry_run:
            upsert_checkpoint(conn, run_id, "S3", "running")
        client = StepClient()
        s3_inserted = 0
        s3_filtered = 0
        s3_done = 0

        for row in ti_rows:
            strongs = row["strongs_number"]
            ti_id = row["ti_id"]
            file_id = row["file_id"]
            registry_no = row["registry_no"]
            word = row["word"]

            if not strongs:
                continue

            if dry_run:
                print(f"     [{registry_no:3}] {word} / {strongs}: (DRY RUN)")
                continue

            try:
                raw_records, html_map = client.get_verse_records_with_html(strongs)
                resolved = strongs

                filter_result = filter_verse_records(raw_records, resolved, html_map)
                stored          = filter_result["stored"]
                filtered_recs   = filter_result["filtered"]
                conflict        = filter_result["conflict"]

                if conflict:
                    print(f"     [{registry_no:3}] {word} / {strongs}: "
                          f"SPAN_CONFLICT — 0 stored")

                for rec in stored:
                    book_id = get_book_id(conn, rec["book_code"])
                    if not book_id:
                        errors.append(f"S3: unknown book {rec['book_code']!r}")
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
                            row["transliteration"] or "",
                            book_id,
                            rec["ref"], rec["chapter"], rec["verse_num"],
                            rec["testament"],
                            rec["esv_text"],
                            rec.get("target_word", ""),
                            rec.get("span_strong_match", 1),
                        ),
                    )
                    s3_inserted += 1
                s3_filtered += len(filtered_recs)

                log_fetch(
                    conn, run_id, registry_no, strongs, resolved, 0,
                    "ok", "zero_results" if not stored else "ok",
                    len(raw_records), len(stored), len(filtered_recs),
                    1 if conflict else 0, None,
                )
                conn.commit()
                s3_done += 1
                print(f"     [{registry_no:3}] {word} / {strongs}: "
                      f"{len(stored)} verses  ({len(filtered_recs)} filtered)")

            except Exception as exc:
                errors.append(f"S3: [{registry_no}] {word}/{strongs}: {exc}")
                print(f"     [{registry_no:3}] {word} / {strongs}: ERROR — {exc}")

        summary["verses_inserted"] = s3_inserted
        summary["verses_filtered"] = s3_filtered
        if not dry_run:
            upsert_checkpoint(conn, run_id, "S3", "complete",
                              rows_written=s3_inserted, rows_filtered=s3_filtered)
        stages_run.append("S3")
        print(f"     S3 complete: {s3_inserted} verses inserted, "
              f"{s3_filtered} filtered, {s3_done} terms processed")

    # ── S4: Meaning parse + flag engine + audit ───────────────────────────────
    if "S4" in active_stages:
        pending_fi = conn.execute(
            """SELECT fi.id AS file_id, fi.registry_id,
                      wr.no AS registry_no, wr.word
               FROM wa_file_index fi
               JOIN word_registry wr ON wr.no = CAST(fi.registry_id AS INTEGER)
               WHERE fi.specification = ? AND wr.phase1_status = 'In Progress'
               ORDER BY wr.no""",
            (SPECIFICATION,),
        ).fetchall()

        print(f"\nS4  Meaning parse + flags + audit ({len(pending_fi)} words)...")
        if not dry_run:
            upsert_checkpoint(conn, run_id, "S4", "running")
        s4_done = 0
        s4_meanings = 0
        s4_flags = 0

        for row in pending_fi:
            file_id = row["file_id"]
            registry_no = row["registry_no"]
            word = row["word"]

            if dry_run:
                print(f"     [{registry_no:3}] {word}: (DRY RUN)")
                continue

            try:
                terms = conn.execute(
                    "SELECT strongs_number, term_id, meaning "
                    "FROM wa_term_inventory WHERE file_id = ?",
                    (file_id,),
                ).fetchall()
                vocab_map = {
                    (r["strongs_number"] or r["term_id"]): {"medium_def": r["meaning"]}
                    for r in terms if r["meaning"]
                }

                if vocab_map:
                    run_parser_for_file(conn, file_id, vocab_map)
                    s4_meanings += len(vocab_map)

                flag_result = run_flag_engine(conn, file_id, registry_no, set())
                s4_flags += flag_result.get("flags_written", 0)

                audit_result = run_audit(conn, file_id, registry_no)
                audit_res = audit_result["result"]

                write_word_run_state(
                    conn, run_id, registry_no, word, "BULK_GAP_FILL_S4",
                    audit_res,
                    {c["check"]: {"r": c["result"], "d": c["detail"]}
                     for c in audit_result["checks"]},
                    audit_result.get("stop_reason"),
                )

                verse_count = conn.execute(
                    "SELECT COUNT(*) AS c FROM wa_verse_records "
                    "WHERE file_id = ? AND (span_strong_match = 1 OR span_strong_match IS NULL)",
                    (file_id,),
                ).fetchone()["c"]
                term_count = conn.execute(
                    "SELECT COUNT(*) AS c FROM wa_term_inventory WHERE file_id = ?",
                    (file_id,),
                ).fetchone()["c"]

                # All-XREF words (0 term_inventory rows) always produce REVIEW
                # audit result — treat REVIEW as Complete when no NEW terms.
                _all_xref = term_count == 0
                new_status = (
                    "Complete"
                    if audit_res == "PASS" or (_all_xref and audit_res == "REVIEW")
                    else "In Progress"
                )

                conn.execute(
                    """UPDATE word_registry SET
                           phase1_status      = ?,
                           phase1_term_count  = ?,
                           phase1_verse_count = ?
                       WHERE no = ?""",
                    (new_status, term_count, verse_count, registry_no),
                )
                conn.commit()

                s4_done += 1
                print(f"     [{registry_no:3}] {word}: audit={audit_res}  "
                      f"status={new_status}  terms={term_count}  verses={verse_count}")

            except Exception as exc:
                errors.append(f"S4: [{registry_no}] {word}: {exc}")
                print(f"     [{registry_no:3}] {word}: ERROR — {exc}")

        summary["meanings_parsed"] = s4_meanings
        if not dry_run:
            upsert_checkpoint(conn, run_id, "S4", "complete", rows_written=s4_done)
        stages_run.append("S4")
        print(f"     S4 complete: {s4_done} words processed, "
              f"{s4_flags} flags written, {s4_meanings} meanings parsed")

    # ── Close run ─────────────────────────────────────────────────────────────
    close_counts = {
        "words_attempted": len(pending_all),
        "words_complete": summary.get("words_initialized", 0),
        "words_stopped": len(errors),
        "total_terms_new": summary.get("terms_inserted", 0),
        "total_terms_xref": 0,
        "total_verses_inserted": summary.get("verses_inserted", 0),
        "total_verses_filtered": summary.get("verses_filtered", 0),
        "total_meanings_parsed": summary.get("meanings_parsed", 0),
        "errors": errors,
    }
    if not dry_run:
        close_run(conn, run_id, "COMPLETE", close_counts)

    print(f"\n=== BULK_GAP_FILL complete  stages={stages_run}  "
          f"errors={len(errors)} ===")
    if errors:
        for e in errors[:10]:
            print(f"  ERROR: {e}")
        if len(errors) > 10:
            print(f"  … and {len(errors) - 10} more errors")

    return {
        "outcome": "COMPLETE",
        "run_id": run_id,
        "stages_run": stages_run,
        "summary": summary,
    }
