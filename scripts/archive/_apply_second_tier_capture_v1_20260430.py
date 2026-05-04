"""_apply_second_tier_capture_v1_20260430.py

Capture parsed second-tier AI analysis output into the database.  For each
word folder under research/investigations/ai_question_test_bundle_20260429/
that contains a parsed-capture-preview.json (produced by
scripts/_tmp_parse_ai_second_tier_output.py), this script writes:

  · `wa_session_b_findings`  — one row per prompt with status A or P,
    finding_type='OBSERVATION', session_b_instruction tagged so v2-derived
    findings remain distinguishable from earlier work; finding_id format
    OBS-NNN-T2-MMM (T2 = catalogue v2 marker).  study_segment carries the
    component code (e.g. 'T0.1'); pass_ref carries the prompt sequence.
  · `wa_finding_catalogue_links` — one row per parsed prompt regardless of
    status, linking finding (or NULL for S/N) to the v2 catalogue question
    via wa_obs_question_catalogue.obs_id; coverage = full/partial/no_finding/
    not_applicable from A/P/S/N; pattern_type carries the notation string.
  · `wa_session_research_flags` — one SB_FINDING per is_gap=True per-prompt
    record (status S OR notation 'Gap identified').  One SD_POINTER per
    session-log session_d_implications entry (deduped against existing).
    One RESEARCHER_DECISION (new flag_code) per session-log
    researcher_decisions entry, where the entry isn't '(none new this
    session)'.

Idempotent per registry: if any wa_session_b_findings row for the registry
already carries session_b_instruction='WA-second-tier-analysis-instruction-
v1-2026-04-30.md', the registry is skipped (re-running with --force would
require explicit deletion of those rows first — not supported here).

Pre-write backup taken automatically.

Usage:
  python scripts/archive/_apply_second_tier_capture_v1_20260430.py
  python scripts/archive/_apply_second_tier_capture_v1_20260430.py --registry 64
  python scripts/archive/_apply_second_tier_capture_v1_20260430.py --live
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
BUNDLE_DIR = os.path.join("research", "investigations", "ai_question_test_bundle_20260429")

INSTRUCTION_TAG = "WA-second-tier-analysis-instruction-v1-2026-04-30.md"
SESSION_RAISED = "Second-tier catalogue v2 application 2026-04-30"
CATALOGUE_VERSION = "v2-2026-04-29"
VALIDATED_BY = "claude_ai_2nd_tier_v1"

STATUS_TO_COVERAGE = {
    "A": "full",
    "P": "partial",
    "S": "no_finding",
    "N": "not_applicable",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def detect_word(folder_name: str) -> tuple[int, str] | None:
    m = re.match(r"[Rr]?(\d{2,3})[ \-_]?([A-Za-z]+)", folder_name)
    if m:
        return (int(m.group(1)), m.group(2).lower())
    return None


def next_seq(conn: sqlite3.Connection, registry_no: int, prefix_re: str) -> int:
    """Return the next sequential MMM number for a finding_id matching the
    given regex (must capture the digit segment as group 1)."""
    rows = conn.execute(
        "SELECT finding_id FROM wa_session_b_findings WHERE registry_id = ?",
        (registry_no,),
    ).fetchall()
    max_n = 0
    pat = re.compile(prefix_re)
    for r in rows:
        m = pat.match(r["finding_id"] or "")
        if m:
            n = int(m.group(1))
            if n > max_n:
                max_n = n
    return max_n + 1


def next_flag_seq(conn: sqlite3.Connection, registry_no: int, prefix_re: str) -> int:
    rows = conn.execute(
        """
        SELECT flag_label FROM wa_session_research_flags
        WHERE registry_id = (SELECT id FROM word_registry WHERE no = ?)
        """,
        (registry_no,),
    ).fetchall()
    max_n = 0
    pat = re.compile(prefix_re)
    for r in rows:
        m = pat.match(r["flag_label"] or "")
        if m:
            n = int(m.group(1))
            if n > max_n:
                max_n = n
    return max_n + 1


def build_question_lookup(conn: sqlite3.Connection) -> dict[tuple[str, int], int]:
    """Map (component_code, prompt_seq) -> obs_id for v2 catalogue rows."""
    rows = conn.execute(
        """
        SELECT obs_id, component_code, prompt_seq
        FROM wa_obs_question_catalogue
        WHERE catalogue_version = ?
        AND (deleted = 0 OR deleted IS NULL)
        """,
        (CATALOGUE_VERSION,),
    ).fetchall()
    return {(r["component_code"], r["prompt_seq"]): r["obs_id"] for r in rows}


def get_file_id(conn: sqlite3.Connection, registry_no: int) -> int | None:
    r = conn.execute(
        "SELECT id FROM wa_file_index WHERE registry_id = ? ORDER BY id LIMIT 1",
        (registry_no,),
    ).fetchone()
    return r["id"] if r else None


def capture_one_word(
    conn: sqlite3.Connection,
    folder_path: str,
    registry_no: int,
    word: str,
    question_lookup: dict[tuple[str, int], int],
    live: bool,
) -> dict:
    """Capture one word's parsed data.  Returns counts dict."""
    preview_path = os.path.join(folder_path, "parsed-capture-preview.json")
    if not os.path.exists(preview_path):
        return {"skipped": "no parsed-capture-preview.json"}

    with open(preview_path, encoding="utf-8") as f:
        preview = json.load(f)

    # Idempotency: if any v2 findings already exist, skip
    existing = conn.execute(
        """
        SELECT COUNT(*) FROM wa_session_b_findings
        WHERE registry_id = ? AND session_b_instruction = ?
        """,
        (registry_no, INSTRUCTION_TAG),
    ).fetchone()[0]
    if existing:
        return {"skipped": f"{existing} v2 findings already captured for R{registry_no:03d}"}

    file_id = get_file_id(conn, registry_no)
    raised_dt = now_iso()
    counts = {
        "findings_inserted": 0,
        "links_inserted": 0,
        "links_skipped_no_question": 0,
        "sb_finding_flags": 0,
        "sd_pointer_flags": 0,
        "researcher_decision_flags": 0,
        "missing_question_codes": [],
    }

    # Findings + links from per-prompt records
    seq = next_seq(conn, registry_no, r"OBS-\d{3}-T2-(\d{3})$")
    sb_seq = next_flag_seq(conn, registry_no, rf"SB-{registry_no:03d}-T2-(\d{{3}})$")
    sd_seq_db = next_flag_seq(conn, registry_no, rf"SP-{registry_no:03d}-(\d{{3}})$")
    rd_seq = next_flag_seq(conn, registry_no, rf"RD-{registry_no:03d}-(\d{{3}})$")

    records = preview.get("analysis", {}).get("records", []) or []

    if live:
        conn.execute("BEGIN")

    try:
        for r in records:
            comp = r.get("component_code")
            pseq = r.get("prompt_seq")
            status = r.get("status")
            body = r.get("body") or ""
            notation = ", ".join(r.get("notation") or []) or None
            obs_id = question_lookup.get((comp, pseq))
            if obs_id is None:
                counts["missing_question_codes"].append(f"{comp}.{pseq}")
                continue

            coverage = STATUS_TO_COVERAGE.get(status)
            if coverage is None:
                # Unknown status — log and continue
                continue

            finding_db_id: int | None = None
            if status in ("A", "P"):
                finding_id_str = f"OBS-{registry_no:03d}-T2-{seq:03d}"
                seq += 1
                if live:
                    cur = conn.execute(
                        """
                        INSERT INTO wa_session_b_findings
                            (finding_id, registry_id, file_id, finding_type, finding,
                             raised_date, session_b_instruction, study_segment,
                             pass_ref, delete_flag, status)
                        VALUES (?, ?, ?, 'OBSERVATION', ?, ?, ?, ?, ?, 0, 'pending')
                        """,
                        (
                            finding_id_str, registry_no, file_id, body,
                            raised_dt, INSTRUCTION_TAG, comp, str(pseq),
                        ),
                    )
                    finding_db_id = cur.lastrowid
                counts["findings_inserted"] += 1

            if live:
                conn.execute(
                    """
                    INSERT INTO wa_finding_catalogue_links
                        (finding_id, question_id, coverage, status, pattern_type,
                         mapped_date, validated_date, validated_by, session_b_note,
                         delete_flagged)
                    VALUES (?, ?, ?, 'active', ?, ?, ?, ?, ?, 0)
                    """,
                    (
                        finding_db_id, obs_id, coverage, notation,
                        raised_dt, raised_dt, VALIDATED_BY, body,
                    ),
                )
            counts["links_inserted"] += 1

            # Gap flag
            if r.get("is_gap"):
                flag_label = f"SB-{registry_no:03d}-T2-{sb_seq:03d}"
                sb_seq += 1
                gap_desc = (
                    f"[Catalogue v2 gap surfaced 2026-04-30] {comp}.{pseq} "
                    f"({r.get('component_title', '')}) — status {status}, notation: {notation or '(none)'}.\n\n"
                    f"Prompt: {r.get('prompt_text', '')}\n\n"
                    f"AI response excerpt: {(body or '')[:400]}"
                )
                if live:
                    conn.execute(
                        """
                        INSERT INTO wa_session_research_flags
                            (registry_id, file_id, flag_code, flag_label, priority,
                             session_target, description, session_raised, raised_date,
                             resolved)
                        VALUES (
                            (SELECT id FROM word_registry WHERE no = ?),
                            ?, 'SB_FINDING', ?, 'MEDIUM', 'B', ?, ?, ?, 0
                        )
                        """,
                        (registry_no, file_id, flag_label, gap_desc, SESSION_RAISED, raised_dt),
                    )
                counts["sb_finding_flags"] += 1

        # Session log items
        sl = preview.get("session_log", {}) or {}

        # Session D implications -> SD_POINTER (skip if exact same description exists)
        for impl in sl.get("session_d_implications") or []:
            text = (impl or "").strip()
            if not text:
                continue
            # dedupe vs existing
            dup = conn.execute(
                """
                SELECT 1 FROM wa_session_research_flags
                WHERE registry_id = (SELECT id FROM word_registry WHERE no = ?)
                AND flag_code = 'SD_POINTER'
                AND SUBSTR(description, 1, 200) = SUBSTR(?, 1, 200)
                """,
                (registry_no, text),
            ).fetchone()
            if dup:
                continue
            flag_label = f"SP-{registry_no:03d}-T2-{sd_seq_db:03d}"
            sd_seq_db += 1
            if live:
                conn.execute(
                    """
                    INSERT INTO wa_session_research_flags
                        (registry_id, file_id, flag_code, flag_label, priority,
                         session_target, description, session_raised, raised_date,
                         resolved)
                    VALUES (
                        (SELECT id FROM word_registry WHERE no = ?),
                        ?, 'SD_POINTER', ?, 'MEDIUM', 'D', ?, ?, ?, 0
                    )
                    """,
                    (registry_no, file_id, flag_label,
                     f"[Catalogue v2 §11 Session-D implication] {text}",
                     SESSION_RAISED, raised_dt),
                )
            counts["sd_pointer_flags"] += 1

        # Researcher decisions -> RESEARCHER_DECISION
        for rd in sl.get("researcher_decisions") or []:
            text = (rd or "").strip()
            if not text or text == "(none new this session)":
                continue
            flag_label = f"RD-{registry_no:03d}-{rd_seq:03d}"
            rd_seq += 1
            if live:
                conn.execute(
                    """
                    INSERT INTO wa_session_research_flags
                        (registry_id, file_id, flag_code, flag_label, priority,
                         session_target, description, session_raised, raised_date,
                         resolved)
                    VALUES (
                        (SELECT id FROM word_registry WHERE no = ?),
                        ?, 'RESEARCHER_DECISION', ?, 'HIGH', 'researcher', ?, ?, ?, 0
                    )
                    """,
                    (registry_no, file_id, flag_label,
                     f"[Catalogue v2 §9 RESEARCHER_DECISION] {text}",
                     SESSION_RAISED, raised_dt),
                )
            counts["researcher_decision_flags"] += 1

        if live:
            conn.commit()

    except Exception:
        if live:
            conn.rollback()
        raise

    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--registry", type=int, default=None)
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(
            BACKUP_DIR, f"bible_research_pre_2nd_tier_capture_{today_compact()}.db"
        )
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    question_lookup = build_question_lookup(conn)
    if not question_lookup:
        print("ERROR: no v2 catalogue rows found (catalogue_version='v2-2026-04-29').")
        return 1
    print(f"v2 catalogue lookup: {len(question_lookup)} (component_code, prompt_seq) entries\n")

    folders = [d for d in sorted(os.listdir(BUNDLE_DIR))
               if os.path.isdir(os.path.join(BUNDLE_DIR, d))]
    targets = []
    for folder_name in folders:
        det = detect_word(folder_name)
        if not det:
            continue
        no, word = det
        if args.registry and no != args.registry:
            continue
        targets.append((folder_name, no, word))

    if not targets:
        print("No matching word folders found.")
        return 1

    grand_totals = {
        "findings_inserted": 0, "links_inserted": 0,
        "links_skipped_no_question": 0,
        "sb_finding_flags": 0, "sd_pointer_flags": 0,
        "researcher_decision_flags": 0,
    }
    for folder_name, no, word in targets:
        folder_path = os.path.join(BUNDLE_DIR, folder_name)
        print(f"\n=== R{no:03d} {word} ({folder_name}) ===")
        counts = capture_one_word(conn, folder_path, no, word, question_lookup, args.live)
        if "skipped" in counts:
            print(f"  [skip] {counts['skipped']}")
            continue
        for k, v in counts.items():
            if k == "missing_question_codes":
                if v:
                    print(f"  missing question codes: {len(v)} (first 5: {v[:5]})")
                continue
            print(f"  {k}: {v}")
            if k in grand_totals:
                grand_totals[k] += v

    print(f"\n=== Grand totals ({'LIVE — committed' if args.live else 'DRY-RUN'}) ===")
    for k, v in grand_totals.items():
        print(f"  {k}: {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
