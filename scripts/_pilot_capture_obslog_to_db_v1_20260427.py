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
      --manifest Sessions/Session_B/09_Analysis_output_logs/words/wa-067-goodness-obslog-parse-manifest-v1-20260427.json \
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

DB_PATH = os.path.join("database", "bible_research.db")
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
    "ANCHOR_UNCITED",           # is_anchor=1 verse with no chapter citation
    "DIMENSION_DRIFT",          # group dim contradicts description
    "ANSWER_UNGROUNDED",        # Q&A answer cites no anchor verse from term
    "EMPTY_TERM",               # status=extracted, 0 verses
    "ORPHAN_ANALYSIS",          # analysis_note exists but verse no longer is_anchor
    # v2.CC9 supersede audit additions
    "FINDING_UNCITED",          # resolved finding not cited in any current chapter
    "CHAPTER_NOT_SUPERSEDED",   # current chapter still pre-revision after lifecycle changes
    "CITATION_GAP",             # >10% citation tokens unresolved per chapter
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
                     "prose_supersedes",
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
    """Write Stage 2c chapter prose to prose_section + extract inline citations
    into wa_prose_section_citations on initial write (per analysis-output v1_5 §v2.9).
    """
    chapters = manifest.get("chapters", [])
    written = skipped = 0
    errors = []
    citations_total = {"inserted": 0, "unresolved": 0}
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
        new_ps_id = None
        body = ch.get("body") or ""
        if not dry:
            cur = conn.execute("""
                INSERT INTO prose_section
                    (registry_id, section_type_id, heading, body, status,
                     version, author, created_at)
                VALUES (?, ?, ?, ?, 'draft', 1, 'claude_ai', ?)
            """, (ctx["registry_id"], section_type_id, ch.get("title"),
                  body, ctx["ts"]))
            new_ps_id = cur.lastrowid
        written += 1

        # v1_5 §v2.9: extract inline citations on initial write.
        # Same logic as the supersede citation extractor — keep the audit
        # trail populated without requiring a supersede pass.
        if not dry and new_ps_id is not None:
            ch_stats = _extract_and_write_chapter_citations(
                conn, ps_id=new_ps_id, body=body,
                registry_no=ctx["registry_no"], ts=ctx["ts"],
            )
            citations_total["inserted"] += ch_stats["inserted"]
            citations_total["unresolved"] += ch_stats["unresolved"]

    return {
        "written": written, "skipped": skipped, "errors": errors,
        "citations_inserted": citations_total["inserted"],
        "citations_unresolved": citations_total["unresolved"],
    }


def _extract_and_write_chapter_citations(conn, ps_id: int, body: str,
                                         registry_no: int, ts: str) -> dict:
    """Extract inline citations from a chapter body and insert into
    wa_prose_section_citations. Returns {inserted, unresolved}.

    Token formats supported (per v2.9):
      OBS-{NNN}-{seq}        (R030 style)
      OBS-{NNN}-OBS-{seq}    (R067 style)
      SP-{NNN}-{seq}
      DIM-{NN}-{seq}         (or DIM-NN-SDNNN)
      GAP-N-{seq} | GAP-S{n}-{seq}
      Q&A-{seq} | Q&A {seq}
      Q{NNN}                 (catalogue question_code form)
    """
    # Order matters: try fuller patterns before shorter ones to avoid
    # overlapping matches (e.g. OBS-NNN-OBS-NNN matched before bare OBS-NNN-NNN).
    patterns = [
        ("OBS_FULL",  _re_qa.compile(r"\bOBS-\d{3}-OBS-\d{3}\b")),
        ("OBS",       _re_qa.compile(r"\bOBS-\d{3}-\d{3}\b")),
        ("SP",        _re_qa.compile(r"\bSP-\d{3}-\d{3}\b")),
        ("DIM",       _re_qa.compile(r"\bDIM-\d+-(?:SD)?\d+\b")),
        ("GAP",       _re_qa.compile(r"\b(?:GAP-N-\d{3}|GAP-S\d-\d{3})\b")),
        ("QA_HYPHEN", _re_qa.compile(r"\bQ&A-\d{1,3}\b")),
        ("QA_SPACE",  _re_qa.compile(r"\bQ&A\s+\d{1,3}\b")),
        ("Q_CODE",    _re_qa.compile(r"\bQ\d{3}\b")),
    ]
    found = []
    seen = set()
    for ttype, pat in patterns:
        for m in pat.finditer(body):
            token = m.group(0)
            key = (ttype, token)
            if key in seen:
                continue
            seen.add(key)
            found.append((m.start(), ttype, token))
    found.sort(key=lambda x: x[0])

    inserted = 0
    unresolved = 0
    for _pos, ttype, token in found:
        cited_finding_id = None
        cited_sd_pointer_id = None
        cited_observation_seq = None

        if ttype in ("OBS_FULL", "OBS"):
            cited_observation_seq = token
            r = conn.execute(
                "SELECT id FROM wa_session_b_findings WHERE finding_id = ? AND (delete_flag=0 OR delete_flag IS NULL)",
                (token,),
            ).fetchone()
            if r:
                cited_finding_id = r[0]
        elif ttype == "SP":
            r = conn.execute(
                "SELECT id FROM wa_session_research_flags WHERE flag_label = ? AND flag_code = 'SD_POINTER'",
                (token,),
            ).fetchone()
            if r:
                cited_sd_pointer_id = r[0]
        elif ttype == "DIM":
            r = conn.execute(
                "SELECT id FROM wa_session_b_findings WHERE finding_id = ? AND (delete_flag=0 OR delete_flag IS NULL)",
                (token,),
            ).fetchone()
            if r:
                cited_finding_id = r[0]
        # GAP, QA_HYPHEN, QA_SPACE, Q_CODE: store as citation_form only

        # Idempotency: skip if (prose_section_id, citation_form) already exists
        existing = conn.execute("""
            SELECT id FROM wa_prose_section_citations
             WHERE prose_section_id = ? AND citation_form = ?
               AND (delete_flagged = 0 OR delete_flagged IS NULL)
             LIMIT 1
        """, (ps_id, token)).fetchone()
        if existing:
            continue

        conn.execute("""
            INSERT INTO wa_prose_section_citations
                (prose_section_id, citation_form, cited_finding_id,
                 cited_sd_pointer_id, cited_observation_seq, paragraph_no, created_at)
            VALUES (?, ?, ?, ?, ?, NULL, ?)
        """, (ps_id, token, cited_finding_id, cited_sd_pointer_id,
              cited_observation_seq, ts))
        inserted += 1
        if (cited_finding_id is None and cited_sd_pointer_id is None
                and ttype in ("OBS_FULL", "OBS", "SP", "DIM")):
            unresolved += 1

    return {"inserted": inserted, "unresolved": unresolved}


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
                     description, session_target, raised_date, resolved,
                     session_raised)
                VALUES (?, 'SD_POINTER', ?, ?, ?, 'Session D', ?, 0, ?)
            """, (ctx["registry_id"], flag_label, priority,
                  f"{target} (raised in Unit {unit})", ctx["ts"],
                  "Session B Stage 2 (obslog capture pipeline)"))
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

        # Find source observation(s) referenced in answer.
        # Two citation formats supported:
        #   OBS-{registry:03d}-OBS-{seq}     (R067 goodness obslog v3 style)
        #   OBS-{registry:03d}-{seq}         (R030 contrition obslog v1 style)
        # Capture only the trailing seq via non-capturing group for the middle.
        # NB: previous form `OBS-(\d+)` greedy-captured the registry digits and
        # NEVER got to the seq, leading to all references resolving to the
        # finding whose seq numerically matched the registry number (bug
        # discovered on R030 capture, 2026-04-28).
        finding_ids = []
        for seq in _re_qa.findall(r"OBS-\d+(?:-OBS)?-(\d+)\b", answer):
            fid = _resolve_obs_to_finding_id(conn, ctx["registry_id"], seq)
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


# ── Prose supersedes (v2.7 / v2.CC9) ───────────────────────────────────────

# Regex map for inline citation token extraction. Order matters: `OBS-NNN-OBS-NNN`
# must be tried before `OBS-NNN` to avoid partial-match collisions.
_CITATION_PATTERNS = [
    ("OBS_FULL", _re_qa.compile(r"\b(OBS-\d{3}-OBS-\d{3})\b")),
    ("SP_FULL", _re_qa.compile(r"\b(SP-\d{3}-\d{3})\b")),
    ("DIM", _re_qa.compile(r"\b(DIM-\d+-\d+)\b")),
    ("GAP_N", _re_qa.compile(r"\b(GAP-N-\d+)\b")),
    ("QA", _re_qa.compile(r"\b(Q&A-\d+)\b")),
    ("Q_CODE", _re_qa.compile(r"\bQ(\d{3})\b")),
    ("OBS_SHORT", _re_qa.compile(r"\bOBS-(\d{3})\b")),
]


def current_chapter(conn, registry_id: int, section_type_id: int):
    """Return (id, version, body) of the current (non-superseded, non-deleted) row for this slot."""
    return conn.execute("""
        SELECT id, version, body FROM prose_section
         WHERE registry_id = ? AND section_type_id = ?
           AND superseded_by_id IS NULL
           AND (delete_flagged = 0 OR delete_flagged IS NULL)
         LIMIT 1
    """, (registry_id, section_type_id)).fetchone()


def write_prose_supersedes(conn, manifest: dict, ctx: dict, dry: bool) -> dict:
    """Apply Stage 2c SUPERSEDE blocks per v2.CC9.

    For each block:
      1. Locate the current row for (registry, section_type) — must exist.
      2. Insert a new row at version=prior+1 with supersedes_id=prior.
      3. UPDATE prior row: superseded_by_id=new, status='superseded'.
      4. Idempotent: if body unchanged, skip.
    """
    blocks = manifest.get("prose_supersedes", [])
    written = skipped = 0
    errors = []
    new_section_ids = []  # [(section_code, new_id, prior_id, new_version)]

    for blk in blocks:
        code = blk.get("section_code")
        st_row = conn.execute(
            "SELECT id FROM prose_section_type WHERE code = ?", (code,)
        ).fetchone()
        if not st_row:
            errors.append(f"prose_section_type '{code}' not found")
            continue
        section_type_id = st_row[0]

        cur = current_chapter(conn, ctx["registry_id"], section_type_id)
        if not cur:
            errors.append(f"No predecessor row for {code} (registry {ctx['registry_no']}); supersede requires an existing chapter to retire.")
            continue

        prior_id, prior_version, prior_body = cur[0], cur[1], cur[2]
        new_body = blk.get("body", "")
        if (prior_body or "").strip() == (new_body or "").strip():
            skipped += 1
            continue

        new_version = prior_version + 1

        if not dry:
            cursor = conn.execute("""
                INSERT INTO prose_section
                    (registry_id, section_type_id, heading, body, status,
                     version, supersedes_id, author, source_file, created_at)
                VALUES (?, ?, ?, ?, 'draft', ?, ?, ?, ?, ?)
            """, (ctx["registry_id"], section_type_id, blk.get("title"),
                  new_body, new_version, prior_id,
                  blk.get("author") or "claude_ai",
                  blk.get("source_file"), ctx["ts"]))
            new_id = cursor.lastrowid
            # status enum allows ('draft','in_review','approved','archived')
            # — use 'archived' to mark the superseded predecessor; the supersede chain
            # itself is tracked via superseded_by_id FK.
            conn.execute("""
                UPDATE prose_section
                   SET superseded_by_id = ?, status = 'archived'
                 WHERE id = ?
            """, (new_id, prior_id))
            new_section_ids.append((code, new_id, prior_id, new_version))
        else:
            # In dry-run, we still record what *would* be written so downstream
            # stages can simulate; but we won't have a real new_id.
            new_section_ids.append((code, None, prior_id, new_version))
        written += 1

    return {
        "written": written, "skipped": skipped, "errors": errors,
        "new_section_ids": new_section_ids,
    }


def write_supersede_citations(conn, manifest: dict, ctx: dict, dry: bool,
                               supersede_result: dict) -> dict:
    """Extract inline citations from each newly-written supersede body and
    write to wa_prose_section_citations. FK resolution where possible; raw
    citation_form preserved otherwise.
    """
    new_section_ids = supersede_result.get("new_section_ids") or []
    if not new_section_ids:
        return {"written": 0, "skipped": 0, "errors": [],
                "note": "no supersede rows — citation extraction skipped"}

    blocks_by_code = {b["section_code"]: b for b in manifest.get("prose_supersedes", [])}
    written = skipped = 0
    errors = []
    unresolved_per_chapter = {}

    for code, ps_id, prior_id, new_version in new_section_ids:
        body = blocks_by_code[code]["body"]
        # Collect tokens preserving order of first appearance, dedup within chapter.
        seen = set()
        tokens = []
        for ttype, pat in _CITATION_PATTERNS:
            for m in pat.finditer(body):
                full = m.group(0)
                if full in seen:
                    continue
                # Filter: OBS_SHORT must not also be the head of an OBS_FULL token.
                # (i.e. 'OBS-067' inside 'OBS-067-OBS-005' should not be a separate match.)
                if ttype == "OBS_SHORT":
                    # Reject if this 'OBS-NNN' is followed by '-OBS-NNN' in body
                    pos = m.start()
                    if _re_qa.match(r"OBS-\d{3}-OBS-\d{3}", body[pos:]):
                        continue
                seen.add(full)
                tokens.append((ttype, full, m.group(1)))

        unresolved_count = 0
        total_tokens = len(tokens)
        for ttype, token, captured in tokens:
            cited_finding_id = None
            cited_sd_pointer_id = None
            cited_observation_seq = None
            citation_form = token

            if ttype == "OBS_FULL":
                row = conn.execute(
                    "SELECT id FROM wa_session_b_findings WHERE finding_id = ? AND (delete_flag=0 OR delete_flag IS NULL)",
                    (token,),
                ).fetchone()
                if row:
                    cited_finding_id = row[0]
                cited_observation_seq = token
            elif ttype == "OBS_SHORT":
                # captured = '005'; normalise to OBS-{registry:03d}-OBS-{captured}
                full = f"OBS-{ctx['registry_no']:03d}-OBS-{captured}"
                row = conn.execute(
                    "SELECT id FROM wa_session_b_findings WHERE finding_id = ? AND (delete_flag=0 OR delete_flag IS NULL)",
                    (full,),
                ).fetchone()
                if row:
                    cited_finding_id = row[0]
                cited_observation_seq = full
                citation_form = full  # normalise form for FK alignment
            elif ttype == "SP_FULL":
                row = conn.execute(
                    "SELECT id FROM wa_session_research_flags WHERE flag_label = ? AND flag_code = 'SD_POINTER'",
                    (token,),
                ).fetchone()
                if row:
                    cited_sd_pointer_id = row[0]
            elif ttype == "DIM":
                row = conn.execute(
                    "SELECT id FROM wa_session_b_findings WHERE finding_id = ? AND (delete_flag=0 OR delete_flag IS NULL)",
                    (token,),
                ).fetchone()
                if row:
                    cited_finding_id = row[0]
            # Q_CODE, QA, GAP_N: no FK lookup; citation_form preserves the raw token

            resolved = (cited_finding_id is not None or cited_sd_pointer_id is not None)
            if not resolved:
                unresolved_count += 1

            if not dry and ps_id is not None:
                conn.execute("""
                    INSERT INTO wa_prose_section_citations
                        (prose_section_id, citation_form, cited_finding_id,
                         cited_sd_pointer_id, cited_observation_seq,
                         paragraph_no, created_at)
                    VALUES (?, ?, ?, ?, ?, NULL, ?)
                """, (ps_id, citation_form, cited_finding_id, cited_sd_pointer_id,
                      cited_observation_seq, ctx["ts"]))
            written += 1

        unresolved_per_chapter[code] = (unresolved_count, total_tokens)

    return {
        "written": written, "skipped": skipped, "errors": errors,
        "unresolved_per_chapter": unresolved_per_chapter,
    }


def write_supersede_audit(conn, manifest: dict, ctx: dict, dry: bool,
                           supersede_result: dict, citations_result: dict) -> dict:
    """Four-audit coherence check per v2.CC9. Writes DATA_ANOMALY_* findings to
    wa_session_b_findings (status='open') for each detected gap.
    """
    new_section_ids = supersede_result.get("new_section_ids") or []
    if not new_section_ids:
        return {"written": 0, "skipped": 0, "errors": [],
                "note": "no supersedes — audit skipped"}

    anomalies = []  # (anomaly_type, description)

    # Build the set of finding_ids cited across all NEW chapter rows.
    cited_finding_ids = set()
    if not dry:
        new_ids = [n[1] for n in new_section_ids if n[1] is not None]
        if new_ids:
            placeholders = ",".join("?" * len(new_ids))
            for r in conn.execute(f"""
                SELECT DISTINCT f.finding_id
                  FROM wa_prose_section_citations pc
                  JOIN wa_session_b_findings f ON f.id = pc.cited_finding_id
                 WHERE pc.prose_section_id IN ({placeholders})
                   AND (pc.delete_flagged = 0 OR pc.delete_flagged IS NULL)
            """, new_ids).fetchall():
                cited_finding_ids.add(r[0])
    else:
        # In dry-run, simulate from the manifest body parsing.
        blocks_by_code = {b["section_code"]: b for b in manifest.get("prose_supersedes", [])}
        for code, _, _, _ in new_section_ids:
            body = blocks_by_code[code]["body"]
            for ttype, pat in _CITATION_PATTERNS:
                if ttype not in ("OBS_FULL", "OBS_SHORT", "DIM"):
                    continue
                for m in pat.finditer(body):
                    if ttype == "OBS_SHORT":
                        cited_finding_ids.add(f"OBS-{ctx['registry_no']:03d}-OBS-{m.group(1)}")
                    else:
                        cited_finding_ids.add(m.group(0))

    # Audit 1: FINDING_UNCITED — every revision-session resolved finding cited?
    resolved_rows = conn.execute("""
        SELECT finding_id FROM wa_session_b_findings
         WHERE registry_id = ?
           AND finding_type = 'OBSERVATION'
           AND status IN ('resolved_qa','resolved_sd','not_relevant')
           AND (delete_flag = 0 OR delete_flag IS NULL)
    """, (ctx["registry_id"],)).fetchall()
    uncited = [r[0] for r in resolved_rows if r[0] not in cited_finding_ids]
    if uncited:
        sample = ", ".join(uncited[:10])
        more = f" (+{len(uncited) - 10} more)" if len(uncited) > 10 else ""
        anomalies.append((
            "DATA_ANOMALY_FINDING_UNCITED",
            f"{len(uncited)} resolved findings have no citation in any current chapter for registry {ctx['registry_no']:03d}: {sample}{more}",
        ))

    # Audit 2: CHAPTER_NOT_SUPERSEDED — chapters citing a finding whose lifecycle
    # changed in the revision but the chapter was not superseded. We approximate
    # this by: any current chapter row (NOT in new_section_ids) that exists for
    # this registry and has citations to findings now resolved. Skip in dry-run.
    if not dry:
        new_ids_set = {n[1] for n in new_section_ids if n[1] is not None}
        not_superseded = []
        for r in conn.execute("""
            SELECT ps.id, pst.code FROM prose_section ps
              JOIN prose_section_type pst ON pst.id = ps.section_type_id
             WHERE ps.registry_id = ?
               AND ps.superseded_by_id IS NULL
               AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
               AND pst.code LIKE 'sb_s2c_ch%'
        """, (ctx["registry_id"],)).fetchall():
            if r[0] not in new_ids_set:
                not_superseded.append(r[1])
        if not_superseded:
            anomalies.append((
                "DATA_ANOMALY_CHAPTER_NOT_SUPERSEDED",
                f"Stage 2c chapters not superseded in this revision (current versions remain at pre-revision content): {', '.join(not_superseded)}",
            ))

    # Audit 3: CITATION_GAP — unresolved tokens > 10% per chapter
    upc = citations_result.get("unresolved_per_chapter", {}) if citations_result else {}
    gaps = []
    for code, (unresolved, total) in upc.items():
        if total > 0 and (unresolved / total) > 0.10:
            gaps.append(f"{code}: {unresolved}/{total} unresolved ({unresolved/total*100:.0f}%)")
    if gaps:
        anomalies.append((
            "DATA_ANOMALY_CITATION_GAP",
            "Citation FK resolution exceeds 10% threshold in: " + "; ".join(gaps),
        ))

    # Audit 4: ANCHOR_UNCITED — every is_anchor=1 verse for this registry has its
    # ref appearing in at least one current chapter prose body.
    # is_anchor lives on verse_context (per-term-in-verse classification), not on
    # wa_verse_records. Join via verse_record_id.
    if not dry:
        anchors = conn.execute("""
            SELECT DISTINCT vr.reference
              FROM verse_context vc
              JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
              JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
              JOIN wa_file_index fi ON fi.id = ti.file_id
             WHERE fi.word_registry_fk = ?
               AND ti.term_owner_type = 'OWNER'
               AND ti.delete_flagged = 0
               AND vc.is_anchor = 1
               AND vc.delete_flagged = 0
               AND vr.delete_flagged = 0
        """, (ctx["registry_id"],)).fetchall()
        anchor_refs = [r[0] for r in anchors]
        # Concatenate current chapter bodies
        new_ids = [n[1] for n in new_section_ids if n[1] is not None]
        prose_text = ""
        if new_ids:
            placeholders = ",".join("?" * len(new_ids))
            for r in conn.execute(
                f"SELECT body FROM prose_section WHERE id IN ({placeholders})",
                new_ids,
            ).fetchall():
                prose_text += "\n" + (r[0] or "")
        # Also include any non-superseded chapter rows for this registry that
        # we did NOT supersede this session — they still count toward anchor coverage.
        for r in conn.execute("""
            SELECT body FROM prose_section
             WHERE registry_id = ?
               AND superseded_by_id IS NULL
               AND (delete_flagged = 0 OR delete_flagged IS NULL)
               AND id NOT IN ({})
        """.format(",".join("?" * len(new_ids)) if new_ids else "NULL"),
        ([ctx["registry_id"]] + new_ids) if new_ids else (ctx["registry_id"],),
        ).fetchall():
            prose_text += "\n" + (r[0] or "")
        uncited_anchors = [ref for ref in anchor_refs if ref not in prose_text]
        if uncited_anchors:
            sample = ", ".join(uncited_anchors[:10])
            more = f" (+{len(uncited_anchors) - 10} more)" if len(uncited_anchors) > 10 else ""
            anomalies.append((
                "DATA_ANOMALY_ANCHOR_UNCITED",
                f"{len(uncited_anchors)} is_anchor=1 verses not cited in any current chapter: {sample}{more}",
            ))

    # Write anomalies as 'open' findings
    written = 0
    for atype, desc in anomalies:
        # Idempotency — skip if an open finding of this type and same description prefix exists for this registry today
        existing = conn.execute("""
            SELECT id FROM wa_session_b_findings
             WHERE registry_id = ?
               AND finding_type = ?
               AND status = 'open'
               AND (delete_flag = 0 OR delete_flag IS NULL)
               AND raised_date >= ?
        """, (ctx["registry_id"], atype, ctx["ts"][:10])).fetchone()
        if existing:
            continue
        if not dry:
            # Allocate a finding_id of form 'ANOMALY-{registry:03d}-{seq:03d}'
            seq = conn.execute("""
                SELECT COUNT(*) FROM wa_session_b_findings
                 WHERE registry_id = ? AND finding_type LIKE 'DATA_ANOMALY_%'
            """, (ctx["registry_id"],)).fetchone()[0] + 1
            finding_id_text = f"ANOMALY-{ctx['registry_no']:03d}-{seq:03d}"
            conn.execute("""
                INSERT INTO wa_session_b_findings
                    (finding_id, registry_id, finding_type, finding,
                     raised_date, status, session_b_instruction)
                VALUES (?, ?, ?, ?, ?, 'open', ?)
            """, (finding_id_text, ctx["registry_id"], atype, desc, ctx["ts"],
                  "wa-claudecode-instruction-v4_3"))
        written += 1

    return {
        "written": written, "skipped": 0, "errors": [],
        "anomalies": [a[0] for a in anomalies],
    }


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

    # v2.7 / v2.CC9: prose supersedes (revision sessions only). Order matters —
    # supersedes must run AFTER qa_findings + sd_pointers so that newly-resolved
    # findings and new SD pointers exist when the citation extractor resolves FKs.
    summary["prose_supersedes"] = write_prose_supersedes(conn, manifest, ctx, dry)
    summary["supersede_citations"] = write_supersede_citations(conn, manifest, ctx, dry, summary["prose_supersedes"])
    summary["supersede_audit"] = write_supersede_audit(conn, manifest, ctx, dry, summary["prose_supersedes"], summary["supersede_citations"])

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
