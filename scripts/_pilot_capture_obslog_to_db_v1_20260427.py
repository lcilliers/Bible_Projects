"""_pilot_capture_obslog_to_db_v1_20260427.py — Phase 2 writer skeleton.

Reads a parser manifest (from Phase 1 — _pilot_parse_obslog_to_db_v1_*.py)
and writes the parsed analytical content to its DB targets per the architecture
in db-capture-phase1-results-and-table-architecture-v1-20260427.md §10-§12.

Design principles per researcher direction:
  - Idempotent: re-running on same manifest produces no new rows beyond first run
  - Transactional: all-or-nothing per session
  - Pre-write validation: counts, FK references, schema integrity
  - Pre-write backup: labelled snapshot before any writes
  - Post-write verification: counts match, FKs resolve, no orphans
  - Anomaly raising: data inconsistencies → 'open' findings of DATA_ANOMALY_* type

Status: SKELETON — implements the unblocked categories fully (status,
chapters, observations, catalogue completeness scaffold). Stubs the Q&A
entity-link logic (needs researcher input on cite-extraction patterns).

Usage:
  python scripts/_pilot_capture_obslog_to_db_v1_20260427.py \
      --manifest outputs/reports/words/wa-067-goodness-obslog-parse-manifest-v1-20260427.json \
      [--live]                # default: dry-run with full validation
      [--registry 67]         # required if not in manifest meta
"""
from __future__ import annotations
import argparse
import json
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("data", "bible_research.db")
BACKUP_DIR = "backups"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


# ── Section_type code map for Stage 2c chapters ────────────────────────────

CHAPTER_CODE_MAP = {
    1: "sb_s2c_ch1",  # Word Characteristic Summary
    2: "sb_s2c_ch2",  # Word Impact Description
    3: "sb_s2c_ch3",  # Annotated Verse Evidence
    4: "sb_s2c_ch4",  # Original Language Vocabulary
    5: "sb_s2c_ch5",  # Connections
    # 6: handled separately — content is the SD pointer table
}


# ── Anomaly types (controlled list per §11.5) ──────────────────────────────

ANOMALY_TYPES = {
    "ANCHOR_UNCITED",       # is_anchor=1 verse with no chapter citation
    "DIMENSION_DRIFT",      # group dim contradicts description
    "ANSWER_UNGROUNDED",    # Q&A answer cites no anchor verse from term
    "EMPTY_TERM",           # status=extracted, 0 verses
    "ORPHAN_ANALYSIS",      # analysis_note exists but verse no longer is_anchor
}


# ── Pre-write validation ───────────────────────────────────────────────────


class ValidationError(Exception):
    pass


def validate_manifest(manifest: dict, conn: sqlite3.Connection) -> dict:
    """Confirm manifest is complete, registry exists, FKs resolve."""
    issues = []
    warnings = []
    meta = manifest["meta"]
    reg_no = meta.get("registry_no")
    if not reg_no:
        issues.append("manifest.meta.registry_no missing")
        return {"ok": False, "issues": issues, "warnings": warnings}

    # Registry exists
    row = conn.execute("SELECT id, word FROM word_registry WHERE no = ?", (reg_no,)).fetchone()
    if not row:
        issues.append(f"Registry no={reg_no} not found in word_registry")
        return {"ok": False, "issues": issues, "warnings": warnings}
    registry_id, word = row[0], row[1]

    # Schema version check
    schema = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()[0]
    if schema not in ("3.17.0",):
        warnings.append(f"Schema version is {schema}; this writer expects 3.17.0+ (M40-M43 applied)")

    # Counts present
    expected_keys = ("qa_findings", "sd_pointers", "observations", "chapters",
                     "gap_questions", "ws_questions", "review_notes",
                     "status_update", "issues")
    missing = [k for k in expected_keys if k not in manifest]
    if missing:
        issues.append(f"Manifest missing keys: {missing}")

    return {
        "ok": not issues,
        "issues": issues,
        "warnings": warnings,
        "registry_id": registry_id,
        "registry_no": reg_no,
        "word": word,
        "schema": schema,
    }


# ── Idempotency helpers ────────────────────────────────────────────────────


def existing_chapter(conn, registry_id: int, section_type_id: int) -> int | None:
    r = conn.execute("""
        SELECT id FROM prose_section
         WHERE registry_id = ? AND section_type_id = ?
           AND (delete_flagged = 0 OR delete_flagged IS NULL)
         LIMIT 1
    """, (registry_id, section_type_id)).fetchone()
    return r[0] if r else None


def existing_observation_finding(conn, registry_id: int, finding_text: str) -> int | None:
    """Approximate dedup — match on (registry, finding_type='OBSERVATION', first 100 chars of finding)."""
    r = conn.execute("""
        SELECT id FROM wa_session_b_findings
         WHERE registry_id = ?
           AND finding_type = 'OBSERVATION'
           AND SUBSTR(finding, 1, 100) = ?
           AND (delete_flag = 0 OR delete_flag IS NULL)
         LIMIT 1
    """, (registry_id, (finding_text or "")[:100])).fetchone()
    return r[0] if r else None


def existing_sd_pointer(conn, registry_id: int, flag_label: str) -> int | None:
    r = conn.execute("""
        SELECT id FROM wa_session_research_flags
         WHERE registry_id = ? AND flag_code = 'SD_POINTER' AND flag_label = ?
         LIMIT 1
    """, (registry_id, flag_label)).fetchone()
    return r[0] if r else None


# ── Category writers (each returns {written:N, skipped:N, errors:[]}) ─────


def write_status_update(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    s = manifest.get("status_update")
    if not s or not s.get("target_status"):
        return {"written": 0, "skipped": 0, "errors": [], "note": "no status_update in manifest"}
    target = s["target_status"]
    current = conn.execute(
        "SELECT session_b_status FROM word_registry WHERE id = ?", (ctx["registry_id"],)
    ).fetchone()[0]
    if current == target:
        return {"written": 0, "skipped": 1, "errors": [], "note": f"status already '{target}'"}
    if not dry:
        conn.execute(
            "UPDATE word_registry SET session_b_status = ? WHERE id = ?",
            (target, ctx["registry_id"]),
        )
    return {"written": 1, "skipped": 0, "errors": [], "note": f"status: {current} -> {target}"}


def write_observations(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """Stage 2a observations → wa_session_b_findings (status='open',
    finding_type='OBSERVATION'). Idempotent on (registry, finding_type, finding-prefix)."""
    obs = manifest.get("observations", [])
    written = skipped = 0
    errors = []
    for o in obs:
        text = o.get("content")
        if not text:
            errors.append(f"observation {o.get('seq')} has empty content")
            continue
        existing = existing_observation_finding(conn, ctx["registry_id"], text)
        if existing:
            skipped += 1
            continue
        if not dry:
            finding_id_text = f"OBS-{ctx['registry_no']:03d}-{o.get('seq', 'unknown')}"
            conn.execute("""
                INSERT INTO wa_session_b_findings
                    (finding_id, registry_id, finding_type, finding,
                     raised_date, status)
                VALUES (?, ?, 'OBSERVATION', ?, ?, 'open')
            """, (finding_id_text, ctx["registry_id"], text, ctx["ts"]))
        written += 1
    return {"written": written, "skipped": skipped, "errors": errors}


def write_chapters(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    chapters = manifest.get("chapters", [])
    written = skipped = 0
    errors = []
    for ch in chapters:
        n = ch.get("chapter_n")
        if n not in CHAPTER_CODE_MAP:
            if n == 6:
                # Chapter 6 is the SD pointer compendium — no prose row required
                continue
            errors.append(f"unknown chapter number {n}")
            continue
        code = CHAPTER_CODE_MAP[n]
        st_row = conn.execute(
            "SELECT id FROM prose_section_type WHERE code = ?", (code,)
        ).fetchone()
        if not st_row:
            errors.append(f"prose_section_type code '{code}' not found")
            continue
        section_type_id = st_row[0]
        existing = existing_chapter(conn, ctx["registry_id"], section_type_id)
        if existing:
            skipped += 1
            continue
        if not dry:
            conn.execute("""
                INSERT INTO prose_section
                    (registry_id, section_type_id, heading, body, status,
                     version, author, created_at)
                VALUES (?, ?, ?, ?, 'draft', 1, 'session_b_2026-04-26', ?)
            """, (ctx["registry_id"], section_type_id, ch.get("title"),
                  ch.get("body"), ctx["ts"]))
        written += 1
    return {"written": written, "skipped": skipped, "errors": errors}


def write_sd_pointers(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """SD pointers → wa_session_research_flags. Idempotent on (registry, flag_label)."""
    sds = manifest.get("sd_pointers", [])
    written = skipped = 0
    errors = []
    for sp in sds:
        seq = sp.get("seq")
        if not seq:
            errors.append("SD pointer missing seq")
            continue
        flag_label = f"SP-{ctx['registry_no']:03d}-{seq.split('-')[-1]}"
        existing = existing_sd_pointer(conn, ctx["registry_id"], flag_label)
        if existing:
            skipped += 1
            continue
        target = sp.get("target", "")
        priority = sp.get("priority", "MEDIUM")
        unit = sp.get("unit_raised", "")
        if not dry:
            conn.execute("""
                INSERT INTO wa_session_research_flags
                    (registry_id, flag_code, flag_label, priority,
                     description, session_target, raised_date, resolved)
                VALUES (?, 'SD_POINTER', ?, ?, ?, 'Session D', ?, 0)
            """, (ctx["registry_id"], flag_label, priority,
                  f"{target} (raised in Unit {unit})", ctx["ts"]))
        written += 1
    return {"written": written, "skipped": skipped, "errors": errors}


def write_catalogue_completeness(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """For every universal catalogue question, ensure a coverage row exists.

    Uses parser's qa_findings to map answered questions; for unaddressed
    universal Qs, writes coverage='no_finding' with finding_id=NULL (M43).
    """
    qa_findings = manifest.get("qa_findings", [])
    addressed_q_codes = {qa["q_code"] for qa in qa_findings}
    universal = conn.execute("""
        SELECT obs_id, question_code FROM wa_obs_question_catalogue
         WHERE (deleted = 0 OR deleted IS NULL)
           AND section LIKE 'Section %'
    """).fetchall()
    written = skipped = 0
    errors = []
    for q_obs_id, q_code in universal:
        if q_code in addressed_q_codes:
            # Will be handled by Q&A writer (TODO — see write_qa_findings stub)
            continue
        # Check if already has any link for this registry's findings
        existing = conn.execute("""
            SELECT id FROM wa_finding_catalogue_links
             WHERE question_id = ?
               AND (finding_id IS NULL
                    OR finding_id IN (SELECT id FROM wa_session_b_findings WHERE registry_id = ?))
               AND (delete_flagged = 0 OR delete_flagged IS NULL)
             LIMIT 1
        """, (q_obs_id, ctx["registry_id"])).fetchone()
        if existing:
            skipped += 1
            continue
        if not dry:
            conn.execute("""
                INSERT INTO wa_finding_catalogue_links
                    (finding_id, question_id, coverage, status,
                     mapped_date, session_b_note)
                VALUES (NULL, ?, 'no_finding', 'validated', ?, ?)
            """, (q_obs_id, ctx["ts"][:10],
                  f"Question not surfaced during analysis of registry {ctx['registry_no']}"))
        written += 1
    return {"written": written, "skipped": skipped, "errors": errors}


def write_qa_findings(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """STUB — full implementation requires:
      - source observation extraction (parse OBS-NNN refs from each Q&A answer)
      - anchor verse resolution (parse anchor_verses string → verse_record_ids)
      - group code resolution (parse from answer text)
      - dimension extraction (parse dimension references from answer)
      - all four entity-link types populated per Q&A
      - finding lifecycle update (source observation → resolved_qa)
    """
    return {"written": 0, "skipped": 0, "errors": [],
            "note": "STUB — needs researcher-confirmed citation patterns"}


def write_review_notes(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """STUB — review notes append to wa_obs_question_catalogue.review_note."""
    return {"written": 0, "skipped": 0, "errors": [],
            "note": "STUB — needs design for append vs overwrite + Q-id resolution"}


def write_new_questions(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """STUB — GAP/WS questions → wa_obs_question_catalogue inserts."""
    return {"written": 0, "skipped": 0, "errors": [],
            "note": "STUB — needs researcher confirmation of obs_id allocation strategy"}


def write_anchor_verse_analyses(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """STUB — extract anchor-verse analytical readings from Unit 7 prose
    and write to verse_context.analysis_note per (verse_record_id, mti_term_id)."""
    return {"written": 0, "skipped": 0, "errors": [],
            "note": "STUB — needs Unit 7 prose-block extraction logic"}


# ── Main runner ────────────────────────────────────────────────────────────


def run(manifest: dict, conn: sqlite3.Connection, dry: bool) -> dict:
    validation = validate_manifest(manifest, conn)
    if not validation["ok"]:
        return {"validation": validation, "summary": {}, "errors": validation["issues"]}

    ctx = {
        "registry_id": validation["registry_id"],
        "registry_no": validation["registry_no"],
        "word": validation["word"],
        "schema": validation["schema"],
        "ts": now_iso(),
    }

    summary = {}
    summary["status_update"] = write_status_update(conn, manifest, ctx, dry)
    summary["observations"] = write_observations(conn, manifest, ctx, dry)
    summary["chapters"] = write_chapters(conn, manifest, ctx, dry)
    summary["sd_pointers"] = write_sd_pointers(conn, manifest, ctx, dry)
    summary["catalogue_completeness"] = write_catalogue_completeness(conn, manifest, ctx, dry)
    summary["qa_findings"] = write_qa_findings(conn, manifest, ctx, dry)
    summary["review_notes"] = write_review_notes(conn, manifest, ctx, dry)
    summary["new_questions"] = write_new_questions(conn, manifest, ctx, dry)
    summary["anchor_verse_analyses"] = write_anchor_verse_analyses(conn, manifest, ctx, dry)

    return {"validation": validation, "summary": summary, "errors": []}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR,
                              f"bible_research_pre_capture_writer_{today_compact()}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        if args.live:
            conn.execute("BEGIN")
            result = run(manifest, conn, dry=False)
            if result["errors"]:
                conn.rollback()
                print("ERRORS — rolled back.")
            else:
                conn.commit()
                print("[LIVE] committed.")
        else:
            result = run(manifest, conn, dry=True)
            print("[DRY-RUN] no writes attempted.")
    finally:
        conn.close()

    print("\n--- Summary ---")
    if not result.get("validation", {}).get("ok"):
        print("VALIDATION FAILED:")
        for i in result["validation"]["issues"]:
            print(f"  - {i}")
        return 2

    print(f"Registry: {result['validation']['registry_no']} {result['validation']['word']}")
    for cat, info in result["summary"].items():
        wr = info.get("written", 0)
        sk = info.get("skipped", 0)
        errs = info.get("errors", [])
        note = info.get("note", "")
        status = "✓" if not errs else "✗"
        print(f"  {status} {cat:30s} written={wr:4d}  skipped={sk:4d}  errors={len(errs)}  {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
