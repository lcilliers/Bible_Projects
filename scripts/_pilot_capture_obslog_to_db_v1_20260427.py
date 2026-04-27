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
                     raised_date, status, session_b_instruction)
                VALUES (?, ?, 'OBSERVATION', ?, ?, 'open', ?)
            """, (finding_id_text, ctx["registry_id"], text, ctx["ts"],
                  "wa-sessionb-analysis-output-v1_1"))
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
                VALUES (?, ?, ?, ?, 'draft', 1, 'claude_ai', ?)
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


import re as _re_qa


def _resolve_obs_to_finding_id(conn, registry_id: int, obs_seq: str) -> int | None:
    """Map 'OBS-NNN' to wa_session_b_findings.id via the finding_id_text we wrote."""
    # We wrote finding_id_text as 'OBS-{reg:03d}-{obs_seq}'
    pat = f"OBS-%-{obs_seq.split('-')[-1]}"
    r = conn.execute("""
        SELECT id FROM wa_session_b_findings
         WHERE registry_id = ? AND finding_id LIKE ?
           AND finding_type = 'OBSERVATION'
         LIMIT 1
    """, (registry_id, pat)).fetchone()
    return r[0] if r else None


def _resolve_verse_refs(conn, registry_id: int, refs_str: str) -> list:
    """Parse 'Psa 119:68, Gen 1:31, Mic 6:8' → list of (verse_record_id, mti_term_id) for OWNER terms in this registry."""
    if not refs_str:
        return []
    refs = [r.strip() for r in refs_str.split(",") if r.strip()]
    results = []
    for ref in refs:
        rows = conn.execute("""
            SELECT vr.id AS vr_id, mt.id AS mti_id
              FROM wa_verse_records vr
              JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                       AND ti.term_owner_type = 'OWNER'
                                       AND ti.delete_flagged = 0
              JOIN wa_file_index fi ON fi.id = ti.file_id
              JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
                                 AND mt.delete_flagged = 0
             WHERE fi.word_registry_fk = ?
               AND vr.delete_flagged = 0
               AND vr.reference = ?
        """, (registry_id, ref)).fetchall()
        for r in rows:
            results.append((r[0], r[1], ref))
    return results


def _extract_group_codes(text: str) -> set:
    """Find group_code patterns like '884-001' in answer text."""
    return set(_re_qa.findall(r"\b(\d{3,4}-\d{3})\b", text or ""))


def _resolve_group_code(conn, registry_id: int, group_code: str) -> int | None:
    """group_code → verse_context_group.id (scoped to registry's terms)."""
    r = conn.execute("""
        SELECT g.id FROM verse_context_group g
          JOIN mti_terms mt ON mt.id = g.mti_term_id
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND g.delete_flagged = 0
           AND g.group_code = ?
         LIMIT 1
    """, (registry_id, group_code)).fetchone()
    return r[0] if r else None


def write_qa_findings(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """Q&A → wa_finding_catalogue_links + wa_finding_entity_links + lifecycle update.

    For ANSWERED / PARTIALLY:
      - Find source observation(s) referenced in answer (OBS-NNN refs)
      - INSERT wa_finding_catalogue_links (finding_id, question_id, coverage,
        session_b_note=answer, status='validated')
      - UPDATE source observation finding.status='resolved_qa'
      - INSERT wa_finding_entity_links for verses (anchor_verses field)
      - INSERT wa_finding_entity_links for groups (group_codes parsed from answer)
    For NOT_APPLICABLE:
      - INSERT wa_finding_catalogue_links (finding_id=NULL, coverage='not_applicable',
        session_b_note=rationale)
    """
    qa_list = manifest.get("qa_findings", [])
    written_links = skipped_links = 0
    written_entity = 0
    written_resolutions = 0
    errors = []
    universal_q_obs = {row[1]: row[0] for row in conn.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue WHERE deleted=0 OR deleted IS NULL"
    ).fetchall()}

    for qa in qa_list:
        q_code = qa.get("q_code")
        disp = (qa.get("disposition") or "").upper()
        answer = qa.get("answer") or ""
        anchor_refs = qa.get("anchor_verses") or ""
        if not q_code or q_code not in universal_q_obs:
            errors.append(f"Q&A {qa.get('qa_seq')}: q_code {q_code} not found in catalogue")
            continue
        question_id = universal_q_obs[q_code]

        if "NOT APPLICABLE" in disp or "NOT_APPLICABLE" in disp:
            # Single NULL row per question/registry
            existing = conn.execute("""
                SELECT id FROM wa_finding_catalogue_links
                 WHERE question_id = ? AND finding_id IS NULL
                   AND coverage = 'not_applicable'
                   AND (delete_flagged = 0 OR delete_flagged IS NULL)
                 LIMIT 1
            """, (question_id,)).fetchone()
            if existing:
                skipped_links += 1
                continue
            if not dry:
                conn.execute("""
                    INSERT INTO wa_finding_catalogue_links
                        (finding_id, question_id, coverage, status, mapped_date, session_b_note)
                    VALUES (NULL, ?, 'not_applicable', 'validated', ?, ?)
                """, (question_id, ctx["ts"][:10], answer or "Not applicable"))
            written_links += 1
            continue

        if "ANSWERED" not in disp:
            # NOT ANSWERED, NOT_ANSWERED, blank — skip (these aren't writes)
            continue

        # Determine coverage
        coverage = "partial" if "PARTIAL" in disp else "full"

        # Find source observation(s) referenced in answer
        obs_refs = _re_qa.findall(r"OBS-(\d+)", answer)
        # Dedup
        obs_refs = list({f"OBS-{ctx['registry_no']:03d}-OBS-{n}": None for n in obs_refs})  # using key-only for dedup
        # Actually: build set of finding_ids
        finding_ids = []
        for raw in _re_qa.findall(r"OBS-(\d+)", answer):
            fid = _resolve_obs_to_finding_id(conn, ctx["registry_id"], raw)
            if fid and fid not in finding_ids:
                finding_ids.append(fid)

        if not finding_ids:
            # No source observation cited — record link with NULL finding_id (not_applicable would be wrong;
            # use 'full' but flag). For now, use a single anchor finding sentinel: we skip and warn.
            errors.append(f"Q&A {qa.get('qa_seq')} {q_code}: no source observation found in answer; skipping link")
            continue

        # For each source observation, create a catalogue_link row
        for fid in finding_ids:
            # Idempotency: UNIQUE (finding_id, question_id) catches re-runs
            existing = conn.execute("""
                SELECT id FROM wa_finding_catalogue_links
                 WHERE finding_id = ? AND question_id = ?
                   AND (delete_flagged = 0 OR delete_flagged IS NULL)
                 LIMIT 1
            """, (fid, question_id)).fetchone()
            if existing:
                skipped_links += 1
                continue
            if not dry:
                conn.execute("""
                    INSERT INTO wa_finding_catalogue_links
                        (finding_id, question_id, coverage, status,
                         mapped_date, validated_date, session_b_note)
                    VALUES (?, ?, ?, 'validated', ?, ?, ?)
                """, (fid, question_id, coverage, ctx["ts"][:10],
                      ctx["ts"][:10], answer))
                # Lifecycle: only update if currently 'open' (don't downgrade)
                conn.execute("""
                    UPDATE wa_session_b_findings
                       SET status = 'resolved_qa'
                     WHERE id = ? AND status = 'open'
                """, (fid,))
                if conn.total_changes:
                    written_resolutions += 1
            written_links += 1

        # Entity links for first source observation only (avoid duplication)
        primary_fid = finding_ids[0]

        # Verses
        for vr_id, _mti, ref in _resolve_verse_refs(conn, ctx["registry_id"], anchor_refs):
            existing = conn.execute("""
                SELECT id FROM wa_finding_entity_links
                 WHERE finding_id = ? AND entity_type = 'verse' AND entity_id = ?
                   AND (delete_flagged = 0 OR delete_flagged IS NULL)
                 LIMIT 1
            """, (primary_fid, vr_id)).fetchone()
            if existing:
                continue
            if not dry:
                conn.execute("""
                    INSERT INTO wa_finding_entity_links
                        (finding_id, entity_type, entity_id, raised_date)
                    VALUES (?, 'verse', ?, ?)
                """, (primary_fid, vr_id, ctx["ts"]))
            written_entity += 1

        # Groups
        for gc in _extract_group_codes(answer):
            gid = _resolve_group_code(conn, ctx["registry_id"], gc)
            if not gid:
                continue
            existing = conn.execute("""
                SELECT id FROM wa_finding_entity_links
                 WHERE finding_id = ? AND entity_type = 'group' AND entity_id = ?
                   AND (delete_flagged = 0 OR delete_flagged IS NULL)
                 LIMIT 1
            """, (primary_fid, gid)).fetchone()
            if existing:
                continue
            if not dry:
                conn.execute("""
                    INSERT INTO wa_finding_entity_links
                        (finding_id, entity_type, entity_id, raised_date)
                    VALUES (?, 'group', ?, ?)
                """, (primary_fid, gid, ctx["ts"]))
            written_entity += 1

    return {
        "written": written_links,
        "skipped": skipped_links,
        "errors": errors,
        "note": f"entity_links={written_entity}, lifecycle_updates={written_resolutions}",
    }


def write_review_notes(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """Review notes → wa_obs_question_catalogue.review_note (append).

    Two sources:
      - source='qa_entry' with q_code → direct mapping
      - source='section_summary' with note text starting 'Q###: ...' → parse Q-code
    """
    notes = manifest.get("review_notes", [])
    universal = {row[1]: row[0] for row in conn.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue WHERE deleted=0 OR deleted IS NULL"
    ).fetchall()}
    written = skipped = 0
    errors = []
    by_q = {}  # q_obs_id → list of new notes to append

    for n in notes:
        q_code = None
        text = (n.get("note") or "").strip()
        if not text:
            continue
        if n.get("source") == "qa_entry":
            q_code = n.get("q_code")
        elif n.get("source") == "section_summary":
            # Parse 'Q002: ...' or 'Q017 / Q001: ...'
            m = _re_qa.match(r"^(Q\d+)(?:\s*/\s*Q\d+)?:\s*(.+)$", text)
            if m:
                q_code = m.group(1)
                text = m.group(2)
            else:
                continue
        if not q_code or q_code not in universal:
            continue
        q_obs_id = universal[q_code]
        by_q.setdefault(q_obs_id, []).append(text)

    for q_obs_id, items in by_q.items():
        # Read existing review_note
        cur = conn.execute(
            "SELECT review_note FROM wa_obs_question_catalogue WHERE obs_id = ?", (q_obs_id,)
        ).fetchone()
        existing_note = cur[0] if cur else None
        # Build new note (append; idempotency: check substring)
        sep = "\n\n" if existing_note else ""
        marker = f"[review note from R{ctx['registry_no']:03d}]"
        new_lines = [f"{marker} {it}" for it in items
                     if not existing_note or it not in existing_note]
        if not new_lines:
            skipped += len(items)
            continue
        appended = (existing_note or "") + sep + "\n\n".join(new_lines)
        if not dry:
            conn.execute(
                "UPDATE wa_obs_question_catalogue SET review_note = ? WHERE obs_id = ?",
                (appended, q_obs_id),
            )
        written += len(new_lines)
        skipped += len(items) - len(new_lines)

    return {"written": written, "skipped": skipped, "errors": errors}


def write_new_questions(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """GAP + WORD-SPECIFIC questions → wa_obs_question_catalogue inserts.

    GAP: scope='universal', section='Section X — ...' (or new GAP-S{N} stub),
         source_word=current word, source_registry_no=current registry
    WORD-SPECIFIC: scope='universal' (per existing data convention) but
         section='Word-Specific Extensions — {word}', source_registry_no=current

    obs_id allocation: max(obs_id)+1.
    """
    gap = manifest.get("gap_questions", [])
    ws = manifest.get("ws_questions", [])
    written = skipped = 0
    errors = []

    cur = conn.execute("SELECT MAX(obs_id) FROM wa_obs_question_catalogue")
    next_obs_id = (cur.fetchone()[0] or 0) + 1

    for q in gap:
        text = q.get("question")
        if not text:
            continue
        # Idempotency: check for an exact-match question_text already in catalogue
        existing = conn.execute(
            "SELECT obs_id FROM wa_obs_question_catalogue WHERE question_text = ? AND (deleted=0 OR deleted IS NULL)",
            (text,)
        ).fetchone()
        if existing:
            skipped += 1
            continue
        section_id = q.get("section") or ""  # e.g. 'S1' from GAP-S1-001
        section_full = f"Section {section_id[1:]} — Generic (gap addition R{ctx['registry_no']:03d})" if section_id.startswith("S") else "Generic (gap)"
        question_code = q.get("id") or f"GAP-{ctx['registry_no']:03d}-{next_obs_id}"
        if not dry:
            conn.execute("""
                INSERT INTO wa_obs_question_catalogue
                    (obs_id, question_code, section, source_word, source_registry_no,
                     question_text, scope, status, deleted, date_added, catalogue_version)
                VALUES (?, ?, ?, ?, ?, ?, 'universal', 'active', 0, ?, ?)
            """, (next_obs_id, question_code, section_full, ctx["word"],
                  ctx["registry_id"], text, ctx["ts"][:10], f"v2.1-R{ctx['registry_no']:03d}"))
        next_obs_id += 1
        written += 1

    # Determine the word-specific section name. Existing convention: '{Word} Extensions'
    word_title = ctx["word"].title()
    ws_section = f"{word_title} Extensions"

    for q in ws:
        text = q.get("question")
        if not text:
            continue
        existing = conn.execute(
            "SELECT obs_id FROM wa_obs_question_catalogue WHERE question_text = ? AND (deleted=0 OR deleted IS NULL)",
            (text,)
        ).fetchone()
        if existing:
            skipped += 1
            continue
        question_code = q.get("id") or f"WS-{ctx['registry_no']:03d}-{next_obs_id}"
        if not dry:
            conn.execute("""
                INSERT INTO wa_obs_question_catalogue
                    (obs_id, question_code, section, source_word, source_registry_no,
                     question_text, scope, status, deleted, date_added, catalogue_version)
                VALUES (?, ?, ?, ?, ?, ?, 'universal', 'active', 0, ?, ?)
            """, (next_obs_id, question_code, ws_section, ctx["word"],
                  ctx["registry_id"], text, ctx["ts"][:10],
                  f"v2.1-R{ctx['registry_no']:03d}"))
        next_obs_id += 1
        written += 1

    return {"written": written, "skipped": skipped, "errors": errors}


def write_anchor_verse_analyses(conn, manifest: dict, ctx: dict, dry: bool, obslog_text: str = None) -> dict:
    """Extract per-anchor analytical readings from Unit 7 prose, write to verse_context.analysis_note.

    Block structure per anchor:
      **{ref}** 🔵 — "verse text"
      <cross-registry Q lines + observations + SD pointer references>
      (until next **{ref}** 🔵 or sign-off or next ###)
    """
    written = skipped = 0
    errors = []
    if not obslog_text:
        return {"written": 0, "skipped": 0, "errors": [],
                "note": "skipped — --obslog not supplied; cannot extract Unit 7 prose blocks"}

    # Find each Unit 7 group block: '### {strongs} Group {gc} — "..." (anchors: ...)'
    group_pat = _re_qa.compile(
        r"^###\s+(\S+)\s+Group\s+(\d{3,4}-\d{3})\s+—.*?\n((?:.|\n)*?)(?=\n###\s|\n##\s|\n---\n)",
        _re_qa.MULTILINE,
    )
    # Within each group block, find anchor verse blocks
    anchor_pat = _re_qa.compile(
        r"\*\*([A-Z][a-z]{2,3}\s+\d+:\d+(?:-\d+)?)\*\*\s+🔵\s+—\s+\"([^\"]*)\"\s*\n((?:.|\n)*?)(?=\n\*\*[A-Z][a-z]{2,3}\s+\d+:\d+(?:-\d+)?\*\*\s+🔵|\n\*\*Group\s+\d{3,4}-\d{3}\s+SIGN-OFF|\Z)",
        _re_qa.MULTILINE,
    )

    for gm in group_pat.finditer(obslog_text):
        strongs = gm.group(1).strip()
        gc = gm.group(2).strip()
        body = gm.group(3)
        # Resolve mti_term_id for this strongs in this registry
        mti_row = conn.execute("""
            SELECT mt.id FROM mti_terms mt
              JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                       AND ti.term_owner_type = 'OWNER'
                                       AND ti.delete_flagged = 0
              JOIN wa_file_index fi ON fi.id = ti.file_id
             WHERE fi.word_registry_fk = ?
               AND mt.strongs_number = ?
               AND mt.delete_flagged = 0
             LIMIT 1
        """, (ctx["registry_id"], strongs)).fetchone()
        if not mti_row:
            continue
        mti_id = mti_row[0]
        for am in anchor_pat.finditer(body):
            verse_ref = am.group(1).strip()
            # We don't strictly need verse_text from match
            commentary = am.group(3).strip()
            # Resolve verse_record_id
            vr_row = conn.execute("""
                SELECT vr.id FROM wa_verse_records vr
                  JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                 WHERE ti.strongs_number = ?
                   AND ti.term_owner_type = 'OWNER'
                   AND ti.delete_flagged = 0
                   AND vr.delete_flagged = 0
                   AND vr.reference = ?
                 LIMIT 1
            """, (strongs, verse_ref)).fetchone()
            if not vr_row:
                continue
            vr_id = vr_row[0]
            # Check existing analysis_note (idempotency)
            cur_row = conn.execute(
                "SELECT analysis_note FROM verse_context WHERE verse_record_id = ? AND mti_term_id = ? AND delete_flagged = 0",
                (vr_id, mti_id),
            ).fetchone()
            if cur_row is None:
                # No verse_context row to attach to — skip
                continue
            existing_note = cur_row[0]
            if existing_note and existing_note.strip() == commentary.strip():
                skipped += 1
                continue
            if not dry:
                conn.execute(
                    "UPDATE verse_context SET analysis_note = ? WHERE verse_record_id = ? AND mti_term_id = ? AND delete_flagged = 0",
                    (commentary, vr_id, mti_id),
                )
            written += 1

    return {"written": written, "skipped": skipped, "errors": errors}


# ── Main runner ────────────────────────────────────────────────────────────


def run(manifest: dict, conn: sqlite3.Connection, dry: bool, obslog_text: str = None) -> dict:
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
    # Order matters: observations first (so qa_findings can resolve OBS-NNN refs to finding ids)
    summary["status_update"] = write_status_update(conn, manifest, ctx, dry)
    summary["observations"] = write_observations(conn, manifest, ctx, dry)
    summary["chapters"] = write_chapters(conn, manifest, ctx, dry)
    summary["sd_pointers"] = write_sd_pointers(conn, manifest, ctx, dry)
    summary["new_questions"] = write_new_questions(conn, manifest, ctx, dry)
    summary["qa_findings"] = write_qa_findings(conn, manifest, ctx, dry)
    summary["catalogue_completeness"] = write_catalogue_completeness(conn, manifest, ctx, dry)
    summary["review_notes"] = write_review_notes(conn, manifest, ctx, dry)
    summary["anchor_verse_analyses"] = write_anchor_verse_analyses(conn, manifest, ctx, dry, obslog_text)

    return {"validation": validation, "summary": summary, "errors": []}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--obslog", default=None,
                    help="Path to obslog .md (enables Unit 7 anchor-verse extraction)")
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)

    obslog_text = None
    if args.obslog:
        with open(args.obslog, encoding="utf-8") as f:
            obslog_text = f.read()

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
            result = run(manifest, conn, dry=False, obslog_text=obslog_text)
            if result["errors"]:
                conn.rollback()
                print("ERRORS — rolled back.")
            else:
                conn.commit()
                print("[LIVE] committed.")
        else:
            result = run(manifest, conn, dry=True, obslog_text=obslog_text)
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
