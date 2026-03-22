"""
audit_word.py
─────────────
AUDIT_WORD mode — steps A1 through A10.

Purpose: Align the database with STEP as the authoritative source for a single
registered word.  STEP data always wins; researcher-owned fields are never
overwritten.

Two-phase design
────────────────
Phase 1 — DIFF (--dry-run):
  Fetch all STEP data, compute the exact changes that would be made, write a
  diff report to outputs/ and print a summary to console.  No writes to any
  DB table.  The run stops after the report so the researcher can review.

Phase 2 — APPLY (normal run):
  Fetch all STEP data, write the diff report, then apply every change:
    • wa_term_inventory  — overwrite all STEP-owned fields (no COALESCE guards)
    • wa_verse_records   — INSERT new, UPDATE existing, DELETE obsolete
                           (rows not returned by STEP after span-filter are
                            DELETEd, not just marked span_strong_match=-1)
    • wa_meaning_parsed  — re-parsed from refreshed meaning text (A5)
    • wa_data_quality_flags — derivable flags re-derived (A6); researcher
                              flags (not in _DERIVABLE_FLAGS set) are untouched
    • wa_term_phase2_flags — never touched
  Followed by: meaning parser (A5), flag engine (A6), audit checks (A7),
  testament coverage (A9), registry update (A10).

STEP-owned fields in wa_term_inventory (overwritten by audit):
  transliteration, step_search_gloss, word_analysis_gloss, occurrence_count,
  meaning, meaning_numbered, lsj_entry, short_def_mounce

Researcher-owned fields (never overwritten):
  status_note, also_spelled, occurrence_count_qualifier, causative_form_present
  (also: language, term_id, parsed_meaning_id — structural / downstream)

Steps:
  A1  — Registry + file_index confirmation
  A2  — Schema version check
  A3  — STEP fetch: vocab + verses for every term (span-filtered)
  A3r — Build and write diff report (always; stops here on --dry-run)
  A4  — Apply STEP data to wa_term_inventory + wa_verse_records
  A5  — Meaning parser refresh
  A6  — Flag engine refresh
  A7  — Audit (WR-01–WR-20)
  A8  — Update wa_file_index.testament_coverage
  A9  — Update word_registry
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
        dry_run:            Phase 1 only — fetch STEP data, write diff report,
                            print summary, stop without any DB writes.
                            Re-run without --dry-run to apply.
        skip_span_backpop:  Deprecated; retained for CLI compatibility.

    Returns:
        {"outcome": str, "run_id": str, "audit_result": str, "details": dict}
    """
    run_id = make_run_id("AUDIT_WORD")
    errors = []
    counts = {
        "words_attempted": 1, "words_complete": 0, "words_stopped": 0,
        "total_verses_inserted": 0, "total_verses_updated": 0,
        "total_verses_deleted": 0, "total_meanings_parsed": 0,
        "errors": errors,
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

    # ── A3: STEP fetch ────────────────────────────────────────────────────────
    # Fetch vocab + verse data for every term in wa_term_inventory.
    # Same data used for diff report (A3r) and apply (A4).
    print("A3  Fetching data from STEP for all terms...")
    client = StepClient()
    book_misses: list[str] = []

    # step_data[ti_id] = {
    #   "strongs": str, "fid": int,
    #   "vocab": dict | None,
    #   "step_verses": list[dict],   # span-filtered stored list
    #   "step_refs": set[str],
    #   "ti_row": sqlite3.Row,
    # }
    step_data: dict[int, dict] = {}

    for fid in file_ids:
        term_rows = conn.execute(
            """SELECT id, strongs_number, term_id, transliteration, status_note,
                      step_search_gloss, word_analysis_gloss, meaning,
                      meaning_numbered, occurrence_count, lsj_entry, short_def_mounce,
                      language
               FROM wa_term_inventory WHERE file_id = ?""",
            (fid,),
        ).fetchall()

        for ti in term_rows:
            strongs = ti["strongs_number"] or ti["term_id"]
            ti_id = ti["id"]

            vocab = None
            try:
                vocab = client.get_vocab_info(strongs) or None
            except Exception as exc:
                errors.append(f"A3: vocab fetch failed for {strongs}: {exc}")

            step_verses: list[dict] = []
            try:
                if not (ti["status_note"] and
                        "no separate verse record" in ti["status_note"].lower()):
                    raw_records, html_map = client.get_verse_records_with_html(strongs)
                    step_verses = filter_verse_records(raw_records, strongs, html_map)["stored"]
            except Exception as exc:
                errors.append(f"A3: verse fetch failed for {strongs}: {exc}")

            step_data[ti_id] = {
                "strongs":     strongs,
                "fid":         fid,
                "vocab":       vocab,
                "step_verses": step_verses,
                "step_refs":   {r["ref"] for r in step_verses},
                "ti_row":      ti,
            }

    total_terms_fetched = len(step_data)
    print(f"     A3: fetched STEP data for {total_terms_fetched} term(s).")

    # ── A3r: Build diff and write report ──────────────────────────────────────
    print("A3r Building diff report...")

    # STEP-owned wa_term_inventory columns: (db_col, vocab_key)
    _TI_STEP_FIELDS = [
        ("transliteration",     "transliteration"),
        ("step_search_gloss",   "gloss"),
        ("word_analysis_gloss", "gloss"),
        ("occurrence_count",    "occurrence_count"),
        ("meaning",             "medium_def"),
        ("meaning_numbered",    "medium_def"),   # mirrors meaning
        ("lsj_entry",           "lsj_entry"),
        ("short_def_mounce",    "short_def_mounce"),
    ]

    # STEP-owned wa_verse_records columns: (db_col, verse_dict_key)
    _VR_STEP_FIELDS = [
        ("verse_text",        "esv_text"),
        ("target_word",       "target_word"),
        ("span_strong_match", "span_strong_match"),
        ("context_before",    "context_before"),
        ("context_after",     "context_after"),
    ]

    diff: dict[int, dict] = {}

    for ti_id, d in step_data.items():
        ti    = d["ti_row"]
        vocab = d["vocab"]

        # Term inventory field diff
        ti_changes: list[dict] = []
        if vocab:
            for db_col, step_key in _TI_STEP_FIELDS:
                new_val  = vocab.get(step_key) or None
                current  = ti[db_col] or None
                if current != new_val:
                    ti_changes.append({"field": db_col, "current": current, "step": new_val})

        # Verse diff
        step_refs        = d["step_refs"]
        step_by_ref      = {r["ref"]: r for r in d["step_verses"]}
        existing_rows    = conn.execute(
            """SELECT id, reference, verse_text, target_word,
                      span_strong_match, context_before, context_after
               FROM wa_verse_records WHERE term_inv_id = ?""",
            (ti_id,),
        ).fetchall()
        existing_by_ref  = {r["reference"]: r for r in existing_rows}
        existing_refs    = set(existing_by_ref.keys())

        to_insert = sorted(step_refs - existing_refs)
        to_delete = sorted(existing_refs - step_refs)
        to_update = []
        for ref in sorted(step_refs & existing_refs):
            rec = step_by_ref[ref]
            row = existing_by_ref[ref]
            changed = [db_col for db_col, sk in _VR_STEP_FIELDS
                       if rec.get(sk) != row[db_col]]
            if changed:
                to_update.append({"ref": ref, "fields": changed})

        diff[ti_id] = {
            "strongs":    d["strongs"],
            "fid":        d["fid"],
            "ti_changes": ti_changes,
            "to_insert":  to_insert,
            "to_update":  to_update,
            "to_delete":  to_delete,
            "unchanged":  len(step_refs & existing_refs) - len(to_update),
        }

    # Totals for report header
    total_ti_changes = sum(len(d["ti_changes"]) for d in diff.values())
    total_insert     = sum(len(d["to_insert"])   for d in diff.values())
    total_update     = sum(len(d["to_update"])   for d in diff.values())
    total_delete     = sum(len(d["to_delete"])   for d in diff.values())
    total_unchanged  = sum(d["unchanged"]        for d in diff.values())

    mode_label = "DRY-RUN (no changes applied)" if dry_run else "APPLY"
    report_lines: list[str] = [
        "# Audit Diff Report",
        f"**Word:** {word}  |  **Registry:** {registry_id}  |  **Run:** {run_id}",
        f"**Generated:** {_now()}  |  **Mode:** {mode_label}",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Category | Count |",
        "|----------|-------|",
        f"| Terms fetched from STEP | {total_terms_fetched} |",
        f"| Term inventory field changes | {total_ti_changes} |",
        f"| Verse records → INSERT | {total_insert} |",
        f"| Verse records → UPDATE | {total_update} |",
        f"| Verse records → DELETE | {total_delete} |",
        f"| Verse records unchanged | {total_unchanged} |",
        "",
    ]

    if errors:
        report_lines += ["### Fetch Errors", ""]
        for e in errors:
            report_lines.append(f"- {e}")
        report_lines.append("")

    for ti_id, d in diff.items():
        report_lines += ["---", "", f"## Term: {d['strongs']}", ""]

        if d["ti_changes"]:
            report_lines += [
                "### Term Inventory Changes",
                "",
                "| Field | Current DB | STEP | Action |",
                "|-------|-----------|------|--------|",
            ]
            for ch in d["ti_changes"]:
                cur = (str(ch["current"]).replace("\n", " ")[:100]
                       if ch["current"] is not None else "_null_")
                nw  = (str(ch["step"]).replace("\n", " ")[:100]
                       if ch["step"] is not None else "_null_")
                report_lines.append(f"| `{ch['field']}` | {cur} | {nw} | UPDATE |")
            report_lines.append("")
        else:
            report_lines += ["### Term Inventory Changes", "", "_No changes_", ""]

        report_lines.append("### Verse Records")
        report_lines.append("")
        ins_str = ", ".join(d["to_insert"]) if d["to_insert"] else "—"
        report_lines.append(f"**INSERT ({len(d['to_insert'])}):** {ins_str}")
        report_lines.append("")
        if d["to_update"]:
            report_lines.append(f"**UPDATE ({len(d['to_update'])}):**")
            for u in d["to_update"]:
                report_lines.append(f"- {u['ref']}: {', '.join(u['fields'])}")
        else:
            report_lines.append("**UPDATE (0)**")
        report_lines.append("")
        del_str = ", ".join(d["to_delete"]) if d["to_delete"] else "—"
        report_lines.append(
            f"**DELETE ({len(d['to_delete'])}) — no longer returned by STEP after span filter:** {del_str}"
        )
        report_lines.append("")
        report_lines.append(f"**UNCHANGED:** {d['unchanged']}")
        report_lines.append("")

    report_text = "\n".join(report_lines)
    _date_tag        = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    _report_filename = f"audit_diff_{word}_{registry_id}_{_date_tag}.md"
    _outputs_dir     = os.path.join(_ROOT, "outputs")
    os.makedirs(_outputs_dir, exist_ok=True)
    _report_path     = os.path.join(_outputs_dir, _report_filename)
    with open(_report_path, "w", encoding="utf-8") as fh:
        fh.write(report_text)

    print(f"     A3r: report → {_report_path}")
    print(f"          ti_field_changes={total_ti_changes}  "
          f"verses INSERT={total_insert}  UPDATE={total_update}  "
          f"DELETE={total_delete}  unchanged={total_unchanged}")

    if dry_run:
        print(f"\n=== DRY-RUN complete: {word} | diff report written ===")
        print(f"    Review: {_report_path}")
        print(f"    Re-run without --dry-run to apply.")
        return {
            "outcome":      "DRY_RUN",
            "run_id":       run_id,
            "audit_result": "PENDING",
            "details": {
                "report_path":  _report_path,
                "ti_changes":   total_ti_changes,
                "verses_insert": total_insert,
                "verses_update": total_update,
                "verses_delete": total_delete,
                "errors":       errors,
            },
        }

    # ── A4: Apply STEP data ───────────────────────────────────────────────────
    print("A4  Applying STEP data...")

    for ti_id, d in diff.items():
        ti          = step_data[ti_id]["ti_row"]
        vocab       = step_data[ti_id]["vocab"]
        strongs     = d["strongs"]
        step_by_ref = {r["ref"]: r for r in step_data[ti_id]["step_verses"]}

        # A4a: Overwrite all STEP-owned fields in wa_term_inventory (no COALESCE)
        if vocab:
            md = vocab.get("medium_def") or None
            conn.execute(
                """UPDATE wa_term_inventory SET
                       transliteration     = ?,
                       step_search_gloss   = ?,
                       word_analysis_gloss = ?,
                       occurrence_count    = ?,
                       meaning             = ?,
                       meaning_numbered    = ?,
                       lsj_entry           = ?,
                       short_def_mounce    = ?
                   WHERE id = ?""",
                (
                    vocab.get("transliteration") or None,
                    vocab.get("gloss") or None,
                    vocab.get("gloss") or None,
                    vocab.get("occurrence_count"),
                    md, md,
                    vocab.get("lsj_entry") or None,
                    vocab.get("short_def_mounce") or None,
                    ti_id,
                ),
            )

        # A4b: DELETE verses no longer in STEP
        for ref in d["to_delete"]:
            conn.execute(
                "DELETE FROM wa_verse_records WHERE term_inv_id = ? AND reference = ?",
                (ti_id, ref),
            )
            counts["total_verses_deleted"] += 1

        # A4c: INSERT new verses
        for ref in d["to_insert"]:
            rec     = step_by_ref[ref]
            book_id = get_book_id(conn, rec["book_code"])
            if book_id is None:
                book_misses.append(rec["book_code"])
                errors.append(f"A4: unknown book {rec['book_code']!r} ({strongs} {ref})")
                continue
            vr_id = get_max_id(conn, "wa_verse_records") + 1
            conn.execute(
                """INSERT INTO wa_verse_records
                       (id, file_id, term_inv_id, term_id, transliteration,
                        book_id, reference, chapter, verse_num, testament,
                        translation, verse_text, target_word,
                        span_strong_match, context_before, context_after)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'ESV', ?, ?, ?, ?, ?)""",
                (
                    vr_id, d["fid"], ti_id, strongs,
                    ti["transliteration"] or "",
                    book_id, ref, rec["chapter"], rec["verse_num"], rec["testament"],
                    rec.get("esv_text", ""),
                    rec.get("target_word", ""),
                    rec.get("span_strong_match", 1),
                    rec.get("context_before"),
                    rec.get("context_after"),
                ),
            )
            counts["total_verses_inserted"] += 1

        # A4d: UPDATE existing verses (all STEP fields, no guards)
        for u in d["to_update"]:
            rec = step_by_ref[u["ref"]]
            conn.execute(
                """UPDATE wa_verse_records SET
                       verse_text        = ?,
                       target_word       = ?,
                       span_strong_match = ?,
                       context_before    = ?,
                       context_after     = ?
                   WHERE term_inv_id = ? AND reference = ?""",
                (
                    rec.get("esv_text", ""),
                    rec.get("target_word", ""),
                    rec.get("span_strong_match", 1),
                    rec.get("context_before"),
                    rec.get("context_after"),
                    ti_id, u["ref"],
                ),
            )
            counts["total_verses_updated"] += 1

    conn.commit()

    if book_misses:
        _unique = sorted(set(book_misses))
        print(f"     [BOOK_MISS] {len(_unique)} unrecognised book code(s): {_unique}")
        print(f'     Register: python -m engine.engine --add-book-code "Name=OsisCode"')

    _vr_total = conn.execute(
        "SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN ({})".format(
            ",".join("?" * len(file_ids))), file_ids,
    ).fetchone()[0]
    print(
        f"     A4: inserted={counts['total_verses_inserted']}  "
        f"updated={counts['total_verses_updated']}  "
        f"deleted={counts['total_verses_deleted']}"
    )
    print(f"     [VERIFY] total verse records now: {_vr_total}")

    # ── A5: Meaning parser refresh ─────────────────────────────────────────────
    print("A5  Meaning parser refresh...")
    for file_id in file_ids:
        terms = conn.execute(
            "SELECT id, strongs_number, term_id, meaning "
            "FROM wa_term_inventory WHERE file_id = ?", (file_id,)
        ).fetchall()
        vocab_map = {
            (t["strongs_number"] or t["term_id"]): {"medium_def": t["meaning"]}
            for t in terms if t["meaning"]
        }
        if vocab_map:
            result = run_parser_for_file(conn, file_id, vocab_map)
            counts["total_meanings_parsed"] += result["parsed"]
    conn.commit()
    _mp_count = conn.execute(
        "SELECT COUNT(*) FROM wa_meaning_parsed mp"
        " JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id"
        " WHERE ti.file_id IN ({})".format(",".join("?" * len(file_ids))),
        file_ids,
    ).fetchone()[0]
    print(f"     A5: {counts['total_meanings_parsed']} meanings re-parsed.  "
          f"[VERIFY] wa_meaning_parsed: {_mp_count} rows")

    # ── A6: Flag engine refresh ────────────────────────────────────────────────
    print("A6  Flag engine refresh...")
    for file_id in file_ids:
        run_flag_engine(conn, file_id, registry_id)
    conn.commit()
    _flag_count = conn.execute(
        "SELECT COUNT(*) FROM wa_data_quality_flags WHERE file_id IN ({})".format(
            ",".join("?" * len(file_ids))), file_ids,
    ).fetchone()[0]
    print(f"     A6 complete.  [VERIFY] quality flags: {_flag_count} rows")

    # ── A7: Audit (WR-01–WR-20) ───────────────────────────────────────────────
    print("A7  Running audit (WR-01–WR-20)...")
    audit_result = run_audit(conn, file_ids[0], registry_id)
    for check in audit_result["checks"]:
        if check["result"] != "PASS":
            print(f"     {check['result']:6} {check['check']}: {check['detail']}")
    write_word_run_state(
        conn, run_id, registry_id, word,
        "AUDIT_WORD_A7",
        audit_result["result"],
        {c["check"]: {"r": c["result"], "d": c["detail"]} for c in audit_result["checks"]},
        audit_result.get("stop_reason"),
    )
    _a7_p = sum(1 for c in audit_result["checks"] if c["result"] == "PASS")
    _a7_r = sum(1 for c in audit_result["checks"] if c["result"] == "REVIEW")
    _a7_s = sum(1 for c in audit_result["checks"] if c["result"] == "STOP")
    print(f"     A7: {audit_result['result']}  ({_a7_p} PASS  {_a7_r} REVIEW  {_a7_s} STOP)")

    # ── A8: Update testament_coverage ─────────────────────────────────────────
    print("A8  Refreshing testament_coverage...")
    for file_id in file_ids:
        testaments = {
            r["testament"]
            for r in conn.execute(
                "SELECT DISTINCT testament FROM wa_verse_records "
                "WHERE file_id = ? AND span_strong_match = 1",
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
    print("     A8 complete.")

    # ── A9: Update word_registry ──────────────────────────────────────────────
    print("A9  Updating word_registry...")
    verse_count = conn.execute(
        """SELECT COUNT(*) AS c FROM wa_verse_records
           WHERE file_id IN ({}) AND span_strong_match = 1""".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchone()["c"]
    term_count = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_term_inventory WHERE file_id IN ({})".format(
            ",".join("?" * len(file_ids))),
        file_ids,
    ).fetchone()["c"]
    _all_xref    = term_count == 0
    final_status = (
        "Complete"
        if audit_result["result"] == "PASS" or _all_xref
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
    counts["words_complete"] = 1

    close_run(conn, run_id, "COMPLETE", counts)

    print(f"\n=== AUDIT_WORD complete: {word} | {audit_result['result']} ===")
    return {
        "outcome":      "COMPLETE",
        "run_id":       run_id,
        "audit_result": audit_result["result"],
        "details": {
            "report_path":    _report_path,
            "verses_inserted": counts["total_verses_inserted"],
            "verses_updated":  counts["total_verses_updated"],
            "verses_deleted":  counts["total_verses_deleted"],
            "meanings_parsed": counts["total_meanings_parsed"],
            "errors":          errors,
        },
    }
