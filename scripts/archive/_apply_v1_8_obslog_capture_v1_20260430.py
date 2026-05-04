"""_apply_v1_8_obslog_capture_v1_20260430.py

Phase-2 obslog-to-DB capture per wa-sessionb-analysis-output-v1_8.

Parses a v1.8 obslog and writes:
  - Stage 2b Q&A entries → wa_session_b_findings (finding_type='OBSERVATION',
    finding_id='OBS-{NNN}-T2-{seq}') + wa_finding_catalogue_links (one per
    Q&A linking the new finding to the v2 catalogue question; coverage from
    A/P/S/N; session_b_note carries the answer body)
  - Stage 2c synthesis entries (SYN-INTRA / SYN-INTER) →
    wa_session_b_findings (finding_type='SYNTHESIS_INTRA_TIER' /
    'SYNTHESIS_INTER_TIER', synthesis_outcome / tiers_engaged /
    structural_relationship / session_c_chapter / sd_pointer_ref populated)
    + wa_finding_catalogue_links (one row per Source Q&A token, linking the
    synthesis finding to the cited Q&A's question_id)
  - SD pointers in `## SD Pointer Accumulator — Final` →
    wa_session_research_flags (flag_code='SD_POINTER'). Idempotent:
    pointers whose flag_label already exists are skipped.
  - RESEARCHER_DECISION items → wa_session_research_flags
    (flag_code='RESEARCHER_DECISION')
  - `## Session Close` block → word_registry.session_b_status

Audits raised post-write:
  - DATA_ANOMALY_QA_GAP — when Q&A count < 189 (the v2 catalogue total)
  - DATA_ANOMALY_SYNTHESIS_INCOMPLETE — when intra+inter != 7+21=28
  - DATA_ANOMALY_FINDING_UNCITED — synthesis findings with no Source Q&A links

Idempotent per registry: aborts cleanly if a v1.8 capture has already run
(detects via session_b_instruction tag).

Pre-write backup taken automatically.

Usage:
  python scripts/archive/_apply_v1_8_obslog_capture_v1_20260430.py --obslog "research/.../wa-067-goodness-obslog-v4-20260430.md"
  python scripts/archive/_apply_v1_8_obslog_capture_v1_20260430.py --obslog ... --live
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
INSTRUCTION_TAG = "wa-sessionb-analysis-output-v1_8-20260430.md"
SESSION_RAISED = "Stage 2b/2c capture per v1.8 — 2026-04-30"
CATALOGUE_VERSION = "v2-2026-04-29"

STATUS_TO_COVERAGE = {
    "A": "full",
    "P": "partial",
    "S": "no_finding",
    "N": "not_applicable",
}

# Marker patterns
# SYN headers come in two styles:
#   R067 form: `**SYN-INTRA-067-001** | T1 — Definition`  (bold closes after id)
#   R103 form: `**SYN-INTRA-103-001 | T1 — Definition intra-tier**`  (bold wraps full title)
# Both supported by allowing the title to appear either inside or outside the bold.
QA_HEADER_RE = re.compile(r"^\*\*Q&A-(\d+)\s*\|\s*(\S+?)\*\*\s*$")
SYN_INTRA_HEADER_RE = re.compile(
    r"^\*\*SYN-INTRA-(\d{3})-(\d{3})(?:\s*\|\s*([^*\n]+?))?\*\*\s*(?:\|\s*(.*))?$"
)
SYN_INTER_HEADER_RE = re.compile(
    r"^\*\*SYN-INTER-(\d{3})-(\d{3})(?:\s*\|\s*([^*\n]+?))?\*\*\s*(?:\|\s*(.*))?$"
)
SP_HEADER_RE = re.compile(r"^\*\*(SP-\d{3}-(?:T2-)?\d{3})\*\*\s*[—-]\s*(.+)$")
RD_HEADER_RE = re.compile(r"^\*\*(RD-\d{3}-\d{3})\*\*\s*[—-]\s*(.+)$")
# Tier-pair extraction from SYN header titles
SYN_INTRA_TIER_RE = re.compile(r"\b(T\d)\b")
SYN_INTER_TIERS_RE = re.compile(r"\b(T\d)\s*[×x]\s*(T\d)\b")
OBS_CITATION_RE = re.compile(r"\bOBS-(\d{3})-(?:OBS-)?(\d{3})\b")
QA_REF_RE = re.compile(r"\bQ&A-(\d{3})\b")
# Range-style Q&A header codes (R099-style): `T2.4.1–T2.4.3` / `T7.1.4-T7.1.9`
# Always within a single component; expands to individual prompt codes.
TIER_PROMPT_RANGE_RE = re.compile(
    r"^(T\d+)\.(\d+)\.(\d+)\s*[–\-]\s*\1\.\2\.(\d+)$"
)


def expand_tier_prompt_code(code: str) -> list[str]:
    """Expand a Q&A header tier_prompt_code into one or more individual codes.

    Cases:
      - 'T2.4.1' -> ['T2.4.1']
      - 'T2.4.1–T2.4.3' -> ['T2.4.1', 'T2.4.2', 'T2.4.3']
      - 'T7.1.4–T7.1.9' -> ['T7.1.4', 'T7.1.5', ..., 'T7.1.9']
    Returns [code] if the input does not match a recognised range pattern.
    """
    m = TIER_PROMPT_RANGE_RE.match(code.strip())
    if not m:
        return [code]
    tier, comp, start, end = m.group(1), m.group(2), int(m.group(3)), int(m.group(4))
    if end < start:
        return [code]
    return [f"{tier}.{comp}.{p}" for p in range(start, end + 1)]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def parse_obslog(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        c = f.read()

    out: dict = {
        "qa_entries": [],
        "syn_entries": [],
        "sp_entries": [],
        "rd_entries": [],
        "session_close": None,
        "registry_no": None,
    }

    # === Parse Q&A blocks ===
    qa_blocks = re.split(r"(?=^\*\*Q&A-\d+\s*\|)", c, flags=re.MULTILINE)
    for block in qa_blocks:
        m = QA_HEADER_RE.match(block.split("\n", 1)[0].strip())
        if not m:
            continue
        qa_seq = int(m.group(1))
        tier_prompt_code = m.group(2)
        # bullet fields
        fields: dict[str, str] = {}
        # Find each "- Field: value" line where value can span until next "- " or blank section
        body = block[len(block.split("\n", 1)[0]):]
        # Split on lines starting with "- "
        cur_field = None
        cur_buf: list[str] = []
        for line in body.split("\n"):
            if line.startswith("- "):
                if cur_field is not None:
                    fields[cur_field] = "\n".join(cur_buf).strip()
                # Parse "- Field: value"
                fm = re.match(r"^- ([A-Za-z][^:]*?):\s*(.*)$", line)
                if fm:
                    cur_field = fm.group(1).strip()
                    cur_buf = [fm.group(2)]
                else:
                    cur_field = None
                    cur_buf = []
            elif cur_field is not None:
                # Stop if we hit the next H2/H3 heading or a `[QUESTION REVIEW NOTE`
                if line.startswith("##") or line.startswith("**"):
                    break
                cur_buf.append(line)
        if cur_field is not None:
            fields[cur_field] = "\n".join(cur_buf).strip()

        out["qa_entries"].append({
            "qa_seq": qa_seq,
            "tier_prompt_code": tier_prompt_code,
            "fields": fields,
        })

    # === Parse SYN-INTRA / SYN-INTER blocks ===
    # Find the synthesis section — accept variant heading forms
    syn_section_match = re.search(
        r"^## Stage 2c\s*[—-]?\s*Synthesis Entries\s*\n([\s\S]+?)(?=^## |\Z)",
        c, re.MULTILINE,
    )
    if syn_section_match:
        syn_block = syn_section_match.group(1)
        # Split on syn entry headers — match anchor `^**SYN-INTRA-` or `^**SYN-INTER-`
        # and DON'T require closing bold on the same line (R103 form has title inside bold)
        entries = re.split(r"(?=^\*\*SYN-(?:INTRA|INTER)-\d{3}-\d{3})", syn_block, flags=re.MULTILINE)
        for entry in entries:
            entry = entry.strip()
            if not entry.startswith("**SYN-"):
                continue
            first_line = entry.split("\n", 1)[0]
            mi = SYN_INTRA_HEADER_RE.match(first_line)
            mr = SYN_INTER_HEADER_RE.match(first_line)
            if mi:
                kind = "INTRA"
                m = mi
            elif mr:
                kind = "INTER"
                m = mr
            else:
                continue
            registry = int(m.group(1))
            seq = int(m.group(2))
            out["registry_no"] = out["registry_no"] or registry
            # Combine title text from inside-bold or after-bold (whichever matched)
            header_title = (m.group(3) or "") + " " + (m.group(4) or "" if m.lastindex >= 4 else "")
            header_title = header_title.strip()

            # Parse bullet fields
            body = entry[len(first_line):]
            fields: dict[str, str] = {}
            cur_field = None
            cur_buf: list[str] = []
            for line in body.split("\n"):
                if line.startswith("- "):
                    if cur_field is not None:
                        fields[cur_field] = "\n".join(cur_buf).strip()
                    fm = re.match(r"^- ([A-Za-z][^:]*?):\s*(.*)$", line)
                    if fm:
                        cur_field = fm.group(1).strip()
                        cur_buf = [fm.group(2)]
                    else:
                        cur_field = None
                        cur_buf = []
                elif cur_field is not None:
                    if line.startswith("##") or line.startswith("**"):
                        break
                    cur_buf.append(line)
            if cur_field is not None:
                fields[cur_field] = "\n".join(cur_buf).strip()

            # Field-name alias: `Synthesis` is R103 form for what R067 calls `Finding`
            if "Synthesis" in fields and "Finding" not in fields:
                fields["Finding"] = fields["Synthesis"]

            # Tier inference from header title when bullets don't carry it
            if kind == "INTRA" and "Tier" not in fields:
                tm = SYN_INTRA_TIER_RE.search(header_title)
                if tm:
                    fields["Tier"] = tm.group(1)
            if kind == "INTER" and "Tiers" not in fields:
                tm = SYN_INTER_TIERS_RE.search(header_title)
                if tm:
                    fields["Tiers"] = f"{tm.group(1)}, {tm.group(2)}"

            # Outcome strip: 'D — Described' → 'D'
            if "Outcome" in fields:
                outcome_raw = fields["Outcome"]
                tm = re.match(r"\s*([APFNDD])\b", outcome_raw)
                if tm:
                    fields["Outcome"] = tm.group(1)

            out["syn_entries"].append({
                "kind": kind,
                "registry": registry,
                "seq": seq,
                "header_meta": header_title,
                "fields": fields,
            })

    # === Parse SD Pointer Accumulator — Final ===
    # Accept variant headings:
    #   '## SD Pointer Accumulator — Final'
    #   '## SD Pointer Accumulator — Stage 2a (Interim — Final at session close)'
    #   '## SD Pointer Accumulator — Final (...)'
    # Pick the LAST matching accumulator section (most recent / closing one).
    sd_matches = list(re.finditer(
        r"^## SD Pointer Accumulator(?:\s*[—-]\s*[^\n]+)?\s*\n([\s\S]+?)(?=^## |\Z)",
        c, re.MULTILINE,
    ))
    sd_match = sd_matches[-1] if sd_matches else None
    if sd_match:
        sd_block = sd_match.group(1)
        entries = re.split(r"(?=^\*\*SP-\d{3}-(?:T2-)?\d{3}\*\*)", sd_block, flags=re.MULTILINE)
        for entry in entries:
            entry = entry.strip()
            first_line = entry.split("\n", 1)[0] if entry else ""
            m = SP_HEADER_RE.match(first_line)
            if not m:
                continue
            flag_label = m.group(1)
            header_meta = m.group(2)
            body = entry[len(first_line):]
            fields: dict[str, str] = {}
            cur_field = None
            cur_buf: list[str] = []
            for line in body.split("\n"):
                if line.startswith("- "):
                    if cur_field is not None:
                        fields[cur_field] = "\n".join(cur_buf).strip()
                    fm = re.match(r"^- ([A-Za-z][^:]*?):\s*(.*)$", line)
                    if fm:
                        cur_field = fm.group(1).strip()
                        cur_buf = [fm.group(2)]
                    else:
                        cur_field = None
                        cur_buf = []
                elif cur_field is not None:
                    if line.startswith("##") or line.startswith("**"):
                        break
                    cur_buf.append(line)
            if cur_field is not None:
                fields[cur_field] = "\n".join(cur_buf).strip()
            out["sp_entries"].append({
                "flag_label": flag_label,
                "header_meta": header_meta,
                "fields": fields,
            })

    # === Parse RESEARCHER_DECISION Accumulator — Final ===
    rd_match = re.search(
        r"^## RESEARCHER_DECISION Accumulator — Final\s*\n([\s\S]+?)(?=^## |\Z)",
        c, re.MULTILINE,
    )
    if rd_match:
        rd_block = rd_match.group(1)
        entries = re.split(r"(?=^\*\*RD-\d{3}-\d{3}\*\*)", rd_block, flags=re.MULTILINE)
        for entry in entries:
            entry = entry.strip()
            first_line = entry.split("\n", 1)[0] if entry else ""
            m = RD_HEADER_RE.match(first_line)
            if not m:
                continue
            flag_label = m.group(1)
            header_meta = m.group(2)
            body = entry[len(first_line):]
            fields: dict[str, str] = {}
            cur_field = None
            cur_buf: list[str] = []
            for line in body.split("\n"):
                if line.startswith("- "):
                    if cur_field is not None:
                        fields[cur_field] = "\n".join(cur_buf).strip()
                    fm = re.match(r"^- ([A-Za-z][^:]*?):\s*(.*)$", line)
                    if fm:
                        cur_field = fm.group(1).strip()
                        cur_buf = [fm.group(2)]
                    else:
                        cur_field = None
                        cur_buf = []
                elif cur_field is not None:
                    if line.startswith("##") or line.startswith("**"):
                        break
                    cur_buf.append(line)
            if cur_field is not None:
                fields[cur_field] = "\n".join(cur_buf).strip()
            out["rd_entries"].append({
                "flag_label": flag_label,
                "header_meta": header_meta,
                "fields": fields,
            })

    # === Parse Session Close ===
    # Pick the LAST Session Close heading — revision sessions add a fresh one
    # like '## Session Close (v2 — corrected)'.
    sc_matches = list(re.finditer(
        r"^## Session Close(?:[^\n]*?)\s*\n([\s\S]+?)(?=^## |\Z)",
        c, re.MULTILINE,
    ))
    sc_match = sc_matches[-1] if sc_matches else None
    if sc_match:
        sc_block = sc_match.group(1)
        status_match = re.search(r"session_b_status:\s*'([^']+)'", sc_block)
        out["session_close"] = {
            "session_b_status": status_match.group(1) if status_match else None,
            "block": sc_block,
        }

    # Infer registry if not set — try multiple sources
    if out["registry_no"] is None and out["sp_entries"]:
        m = re.match(r"SP-(\d{3})", out["sp_entries"][0]["flag_label"])
        if m:
            out["registry_no"] = int(m.group(1))
    if out["registry_no"] is None:
        # Try filename
        fname_m = re.search(r"wa-(\d{3})-[a-z]+-obslog", os.path.basename(__file__))
        if not fname_m:
            # We don't have the filename here — caller passes path; fall back
            # to scanning content for any *-NNN-* marker
            any_marker = re.search(r"(?:OBS|SP|SYN-INTRA|SYN-INTER|RD)-(\d{3})", c)
            if any_marker:
                out["registry_no"] = int(any_marker.group(1))

    return out


def infer_registry_from_filename(path: str) -> int | None:
    fname = os.path.basename(path)
    m = re.search(r"wa-(\d{3})-[a-zA-Z]+", fname)
    return int(m.group(1)) if m else None


def next_obs_t2_seq(conn: sqlite3.Connection, registry_no: int) -> int:
    rows = conn.execute(
        "SELECT finding_id FROM wa_session_b_findings WHERE registry_id = ?",
        (registry_no,),
    ).fetchall()
    pat = re.compile(rf"OBS-{registry_no:03d}-T2-(\d{{3}})")
    max_n = 0
    for r in rows:
        m = pat.match(r["finding_id"] or "")
        if m:
            max_n = max(max_n, int(m.group(1)))
    return max_n + 1


def capture(args, conn: sqlite3.Connection, parsed: dict) -> dict:
    registry_no = parsed["registry_no"]
    if not registry_no:
        raise ValueError("Could not determine registry_no from obslog")

    counts = {
        "qa_findings_inserted": 0,
        "qa_links_inserted": 0,
        "qa_skipped_no_question": 0,
        "qa_skipped_already_captured": 0,
        "synthesis_findings_inserted": 0,
        "synthesis_skipped_already_captured": 0,
        "synthesis_qa_links_inserted": 0,
        "sd_pointers_inserted": 0,
        "sd_pointers_skipped_existing": 0,
        "rd_inserted": 0,
        "obs_lifecycle_updates": 0,
        "anomalies_raised": 0,
        "missing_question_codes": [],
    }

    raised_dt = now_iso()

    # === Catalogue lookup ===
    # Widen to all ACTIVE question_codes — v2 universal catalogue PLUS any
    # word-specific Extensions still active (e.g. 'L-001' for Love Extensions).
    # Soft-deleted (status='redundant_v1') v1 rows are excluded.
    q_lookup = {
        r["question_code"]: r["obs_id"]
        for r in conn.execute(
            "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
            "WHERE (deleted=0 OR deleted IS NULL) "
            "AND (status IS NULL OR status NOT IN ('redundant_v1','retired'))"
        ).fetchall()
    }

    # Existing OBS findings on this registry — for OBS-NNN-NNN citation lookups
    obs_finding_lookup = {
        r["finding_id"]: r["id"]
        for r in conn.execute(
            "SELECT id, finding_id FROM wa_session_b_findings WHERE registry_id = ? AND delete_flag = 0",
            (registry_no,),
        ).fetchall()
    }

    # === Idempotency note ===
    # The previous behaviour was to abort if any v1.8 finding already exists.
    # Under v1.8 revision-session model, a v2 obslog may add new Q&A entries
    # to a previously-captured registry (gap fill). The script now operates
    # additively: each Q&A / synthesis / SD pointer is captured only if its
    # specific identifier isn't already in the DB.
    existing = conn.execute(
        "SELECT COUNT(*) FROM wa_session_b_findings "
        "WHERE registry_id = ? AND session_b_instruction = ? AND delete_flag = 0",
        (registry_no, INSTRUCTION_TAG),
    ).fetchone()[0]
    if existing:
        print(f"[additive mode] {existing} v1.8 findings already exist for R{registry_no:03d}. Will skip already-captured items.")

    # Build per-item skip sets — scoped to THIS registry only.
    # Q&A: dedupe via finding-linked rows (which carry registry via finding).
    # NULL-finding rows (S/N) are not deduped here — re-capturing them on a
    # revision is harmless (the link table allows multiple NULL finding_id
    # rows; SQLite UNIQUE treats NULL as distinct).
    already_qa_questions = {
        r[0] for r in conn.execute(
            """SELECT DISTINCT l.question_id
               FROM wa_finding_catalogue_links l
               JOIN wa_session_b_findings f ON f.id = l.finding_id
               WHERE l.validated_by = 'claude_ai_v1_8'
               AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
               AND f.registry_id = ? AND f.delete_flag = 0""",
            (registry_no,),
        ).fetchall()
    }
    already_synth_finding_ids = {
        r[0] for r in conn.execute(
            "SELECT finding_id FROM wa_session_b_findings "
            "WHERE registry_id = ? AND finding_type LIKE 'SYNTHESIS_%' AND delete_flag = 0",
            (registry_no,),
        ).fetchall()
    }

    file_id_row = conn.execute(
        "SELECT id FROM wa_file_index WHERE registry_id = ? ORDER BY id LIMIT 1",
        (registry_no,),
    ).fetchone()
    file_id = file_id_row["id"] if file_id_row else None

    if not args.live:
        print(f"[DRY-RUN] R{registry_no:03d} v1.8 obslog capture would write:")

    # === Stage 2b Q&A capture ===
    seq = next_obs_t2_seq(conn, registry_no)
    qa_seq_to_finding_id: dict[int, int] = {}  # qa_seq -> wa_session_b_findings.id
    qa_seq_to_question_id: dict[int, int] = {}  # qa_seq -> wa_obs_question_catalogue.obs_id

    seen_qa_in_obslog = set()  # local dedupe — same question_code twice in obslog
    for qa in parsed["qa_entries"]:
        tpc_raw = qa["tier_prompt_code"]
        # v1.8 obslog allows range-style codes (e.g. 'T2.4.1–T2.4.3') — expand
        # to individual prompt codes; one finding is created and each prompt
        # gets a catalogue link to it.
        expanded_codes = expand_tier_prompt_code(tpc_raw)
        expanded: list[tuple[str, int]] = []  # (code, question_id)
        for code in expanded_codes:
            qid = q_lookup.get(code)
            if qid is None:
                counts["qa_skipped_no_question"] += 1
                counts["missing_question_codes"].append(code)
            else:
                expanded.append((code, qid))
        if not expanded:
            continue

        # Skip if any expanded prompt already captured in DB (additive mode)
        if any(qid in already_qa_questions for _, qid in expanded):
            counts["qa_skipped_already_captured"] += 1
            continue

        # Skip duplicates within this obslog
        if any(qid in seen_qa_in_obslog for _, qid in expanded):
            counts["qa_skipped_already_captured"] += 1
            continue
        for _, qid in expanded:
            seen_qa_in_obslog.add(qid)

        fields = qa["fields"]
        # Accept either field name ("Status tag" per v1.8 §8 spec, or just
        # "Status" as some obslogs use). Take first letter as the status code.
        status_raw = (fields.get("Status tag") or fields.get("Status") or "").strip()
        # Strip leading marker like "A — Answered" → "A"
        m = re.match(r"\s*([APSN])\b", status_raw)
        status_tag = m.group(1) if m else (status_raw[:1].upper() if status_raw else "")
        coverage = STATUS_TO_COVERAGE.get(status_tag)
        if not coverage:
            continue

        answer = fields.get("Answer") or fields.get("Rationale") or ""
        notation = fields.get("Notation", "")
        finding_type_raw = (fields.get("Finding type") or "OBSERVATION").strip()
        finding_type = finding_type_raw if finding_type_raw and finding_type_raw not in ("N/A", "") else "OBSERVATION"

        # Use the first expanded code for finding metadata (study_segment, pass_ref).
        # If the range covers multiple components, use the lead code; range scope
        # is implicit in the multiple catalogue links.
        lead_code = expanded[0][0]

        finding_db_id = None
        if status_tag in ("A", "P"):
            finding_id_str = f"OBS-{registry_no:03d}-T2-{seq:03d}"
            seq += 1
            if args.live:
                cur = conn.execute(
                    """
                    INSERT INTO wa_session_b_findings
                        (finding_id, registry_id, file_id, finding_type, finding,
                         raised_date, session_b_instruction, study_segment,
                         pass_ref, delete_flag, status, anchor_verses)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 'resolved_qa', ?)
                    """,
                    (
                        finding_id_str, registry_no, file_id, finding_type,
                        answer, raised_dt, INSTRUCTION_TAG,
                        # study_segment carries component code (e.g. T0.1).
                        # For range entries, this is the lead component.
                        ".".join(lead_code.split(".")[:2]),
                        # pass_ref: lead prompt seq, with range note if applicable
                        (lead_code.split(".")[-1] if "." in lead_code else None)
                        + (f"–{expanded[-1][0].split('.')[-1]}" if len(expanded) > 1 else ""),
                        fields.get("Anchor verses") or None,
                    ),
                )
                finding_db_id = cur.lastrowid
            counts["qa_findings_inserted"] += 1

        # One catalogue link per expanded prompt — covers range expansion.
        for _, question_id in expanded:
            if args.live:
                conn.execute(
                    """
                    INSERT INTO wa_finding_catalogue_links
                        (finding_id, question_id, coverage, status, pattern_type,
                         mapped_date, validated_date, validated_by, session_b_note,
                         delete_flagged)
                    VALUES (?, ?, ?, 'active', ?, ?, ?, 'claude_ai_v1_8', ?, 0)
                    """,
                    (finding_db_id, question_id, coverage, notation,
                     raised_dt, raised_dt, answer),
                )
            counts["qa_links_inserted"] += 1

        # Record only the lead question_id under the qa_seq; SP/synthesis
        # source-Q&A back-refs map by qa_seq, not by individual prompt.
        qa_seq_to_finding_id[qa["qa_seq"]] = finding_db_id
        qa_seq_to_question_id[qa["qa_seq"]] = expanded[0][1]

        # === Lifecycle: cited OBS findings → status='resolved_qa' ===
        if args.live and status_tag in ("A", "P"):
            cited = OBS_CITATION_RE.findall(answer)
            for reg_str, seq_str in cited:
                # Try multiple existing finding_id formats
                for fmt in (f"OBS-{int(reg_str):03d}-OBS-{int(seq_str):03d}",
                            f"OBS-{int(reg_str):03d}-{int(seq_str):03d}"):
                    cited_id = obs_finding_lookup.get(fmt)
                    if cited_id is not None:
                        n = conn.execute(
                            "UPDATE wa_session_b_findings SET status='resolved_qa' "
                            "WHERE id = ? AND status != 'resolved_qa'",
                            (cited_id,),
                        ).rowcount
                        counts["obs_lifecycle_updates"] += n
                        break

    # === Stage 2c synthesis capture ===
    intra_count = inter_count = 0
    for syn in parsed["syn_entries"]:
        kind = syn["kind"]
        seq_n = syn["seq"]
        registry = syn["registry"]
        fields = syn["fields"]
        outcome = (fields.get("Outcome", "") or "").strip().upper()[:1]
        finding_text = fields.get("Finding") or ""
        tiers_engaged = fields.get("Tier") or fields.get("Tiers") or ""
        components_considered = fields.get("Components considered") or ""
        structural_relationship = fields.get("Structural relationship") or "N/A"
        session_c_chapter = fields.get("Session C chapter") or "N/A"
        sd_ref = fields.get("SD pointer") or "NONE"
        if sd_ref.upper() in ("NONE", "N/A", ""):
            sd_pointer_ref = None
        else:
            sd_pointer_ref = sd_ref.strip()

        finding_id_str = (
            f"SYN-INTRA-{registry:03d}-{seq_n:03d}" if kind == "INTRA"
            else f"SYN-INTER-{registry:03d}-{seq_n:03d}"
        )
        finding_type = "SYNTHESIS_INTRA_TIER" if kind == "INTRA" else "SYNTHESIS_INTER_TIER"

        if kind == "INTRA":
            intra_count += 1
        else:
            inter_count += 1

        # Skip if already captured (additive mode)
        if finding_id_str in already_synth_finding_ids:
            counts["synthesis_skipped_already_captured"] += 1
            continue

        finding_db_id = None
        if args.live:
            cur = conn.execute(
                """
                INSERT INTO wa_session_b_findings
                    (finding_id, registry_id, file_id, finding_type, finding,
                     raised_date, session_b_instruction,
                     study_segment, pass_ref,
                     synthesis_outcome, tiers_engaged, structural_relationship,
                     session_c_chapter, sd_pointer_ref,
                     delete_flag, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 'pending')
                """,
                (
                    finding_id_str, registry, file_id, finding_type,
                    finding_text, raised_dt, INSTRUCTION_TAG,
                    components_considered, str(seq_n),
                    outcome if outcome in ("D", "F", "N") else None,
                    tiers_engaged,
                    structural_relationship,
                    session_c_chapter,
                    sd_pointer_ref,
                ),
            )
            finding_db_id = cur.lastrowid
        counts["synthesis_findings_inserted"] += 1

        # Source links → wa_finding_catalogue_links
        # Two formats supported:
        #   "Source Q&A:" with Q&A-NNN seq references (full v1.8 obslog,
        #   where Stage 2b is in the same file and qa_seq_to_question_id is populated)
        #   "Source prompts:" with component+prompt references (Stage-2c-only
        #   obslog — Stage 2b is in a separate file)
        source_qa_field = fields.get("Source Q&A") or fields.get("Source QA") or ""
        source_prompts_field = fields.get("Source prompts") or fields.get("Source Prompts") or ""

        resolved_qids: set[int] = set()
        # Q&A-NNN references → look up via qa_seq_to_question_id
        for ref_seq in QA_REF_RE.findall(source_qa_field):
            qid = qa_seq_to_question_id.get(int(ref_seq))
            if qid is not None:
                resolved_qids.add(qid)
        # Source prompts: e.g. "T1.1 P1-3, T1.2 P1, T1.3 P1-2"
        if source_prompts_field:
            # Split on commas, parse each entry
            for entry in source_prompts_field.split(","):
                entry = entry.strip()
                # Match "T0.1 P1" or "T0.1 P1-3" (range)
                pm = re.match(r"(T\d\.\d+)\s+P(\d+)(?:-(\d+))?", entry)
                if pm:
                    comp = pm.group(1)
                    p_start = int(pm.group(2))
                    p_end = int(pm.group(3)) if pm.group(3) else p_start
                    for p in range(p_start, p_end + 1):
                        code = f"{comp}.{p}"
                        qid = q_lookup.get(code)
                        if qid is not None:
                            resolved_qids.add(qid)

        for question_id in resolved_qids:
            if args.live:
                conn.execute(
                    """
                    INSERT INTO wa_finding_catalogue_links
                        (finding_id, question_id, coverage, status, pattern_type,
                         mapped_date, validated_date, validated_by, session_b_note,
                         delete_flagged)
                    VALUES (?, ?, 'full', 'active', ?, ?, ?, 'claude_ai_v1_8', ?, 0)
                    """,
                    (finding_db_id, question_id,
                     f"synthesis_source ({outcome})",
                     raised_dt, raised_dt,
                     f"Cited as source by {finding_id_str}: {finding_text[:200]}…"),
                )
            counts["synthesis_qa_links_inserted"] += 1

    # === SD pointer capture (idempotent on flag_label) ===
    existing_sp_labels = {
        r[0] for r in conn.execute(
            "SELECT flag_label FROM wa_session_research_flags WHERE registry_id = ?",
            (conn.execute("SELECT id FROM word_registry WHERE no = ?", (registry_no,)).fetchone()[0],),
        ).fetchall()
    }
    for sp in parsed["sp_entries"]:
        if sp["flag_label"] in existing_sp_labels:
            counts["sd_pointers_skipped_existing"] += 1
            continue
        priority_match = re.search(r"\b(HIGH|MEDIUM|LOW)\b", sp["header_meta"])
        priority = priority_match.group(1) if priority_match else "MEDIUM"
        question = sp["fields"].get("Question") or sp["fields"].get("Description") or ""
        target = sp["fields"].get("Target") or ""
        evidence = sp["fields"].get("Evidence basis") or ""
        connecting_term = sp["fields"].get("Connecting term") or ""
        description = (
            f"[v1.8 obslog SD pointer] {question}\n\n"
            f"Target: {target}\n"
            f"Connecting term: {connecting_term}\n"
            f"Evidence basis: {evidence}"
        )
        if args.live:
            conn.execute(
                """
                INSERT INTO wa_session_research_flags
                    (registry_id, file_id, flag_code, flag_label, priority,
                     session_target, description, session_raised, raised_date,
                     resolved)
                VALUES (
                    (SELECT id FROM word_registry WHERE no = ?),
                    ?, 'SD_POINTER', ?, ?, 'D', ?, ?, ?, 0
                )
                """,
                (registry_no, file_id, sp["flag_label"], priority,
                 description, SESSION_RAISED, raised_dt),
            )
        counts["sd_pointers_inserted"] += 1

    # === RESEARCHER_DECISION capture ===
    for rd in parsed["rd_entries"]:
        if rd["flag_label"] in existing_sp_labels:
            continue
        priority_match = re.search(r"\b(HIGH|MEDIUM|LOW)\b", rd["header_meta"])
        priority = priority_match.group(1) if priority_match else "HIGH"
        decision = rd["fields"].get("Decision required") or ""
        context = rd["fields"].get("Context") or ""
        description = f"[v1.8 obslog RESEARCHER_DECISION] {decision}\n\nContext: {context}"
        if args.live:
            conn.execute(
                """
                INSERT INTO wa_session_research_flags
                    (registry_id, file_id, flag_code, flag_label, priority,
                     session_target, description, session_raised, raised_date,
                     resolved)
                VALUES (
                    (SELECT id FROM word_registry WHERE no = ?),
                    ?, 'RESEARCHER_DECISION', ?, ?, 'researcher', ?, ?, ?, 0
                )
                """,
                (registry_no, file_id, rd["flag_label"], priority,
                 description, SESSION_RAISED, raised_dt),
            )
        counts["rd_inserted"] += 1

    # === Status update from Session Close ===
    if parsed.get("session_close") and parsed["session_close"]["session_b_status"]:
        new_status = parsed["session_close"]["session_b_status"]
        if args.live:
            conn.execute(
                "UPDATE word_registry SET session_b_status = ? WHERE no = ?",
                (new_status, registry_no),
            )
        print(f"  word_registry.session_b_status -> '{new_status}'")

    # === Audits ===
    n_qa = len(parsed["qa_entries"])
    # Compute prompt-level coverage with range expansion: a Q&A header like
    # 'T2.4.1–T2.4.3' contributes 3 prompts to coverage. The 189-prompt
    # universe is the v2 tiered catalogue (tier IS NOT NULL); registry-
    # specific extensions (C-*, L-*, etc.) are excluded from the gap audit.
    covered_in_obslog: set[str] = set()
    for q in parsed["qa_entries"]:
        for code in expand_tier_prompt_code(q["tier_prompt_code"]):
            covered_in_obslog.add(code)
    tiered_codes: set[str] = {
        r["question_code"]
        for r in conn.execute(
            "SELECT question_code FROM wa_obs_question_catalogue "
            "WHERE tier IS NOT NULL AND status='active' "
            "AND (deleted=0 OR deleted IS NULL)"
        ).fetchall()
    }
    # Cumulative coverage across DB: union of this obslog's prompts AND any
    # tiered prompts already linked to active R{NNN} findings via prior
    # captures. Supplemental/top-up obslogs (v2/v3) only add the gap; the
    # audit must consider DB state, not just this file's contents.
    already_covered_codes: set[str] = {
        r[0] for r in conn.execute(
            """SELECT DISTINCT q.question_code
                 FROM wa_finding_catalogue_links l
                 JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
                 LEFT JOIN wa_session_b_findings f ON f.id = l.finding_id
                WHERE q.tier IS NOT NULL
                  AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
                  AND (f.registry_id = ? OR f.id IS NULL)
                  AND l.validated_by = 'claude_ai_v1_8'""",
            (registry_no,),
        ).fetchall()
    }
    cumulative_covered = covered_in_obslog | already_covered_codes
    n_prompts_covered = len(cumulative_covered & tiered_codes)
    # Suppress the QA_GAP anomaly for stage-2c-only obslogs (where Stage 2b
    # was completed in a prior obslog and this file only carries the
    # synthesis pass + closure).
    is_stage2c_only = (n_qa == 0 and len(parsed.get("syn_entries") or []) > 0)
    # Supplemental obslogs: prior R{NNN} v1.8 captures already exist. The
    # synthesis-count audit and the QA_GAP audit look at cumulative DB state
    # rather than just this file.
    is_supplemental = existing > 0
    if n_prompts_covered < 189 and not is_stage2c_only:
        missing = sorted(tiered_codes - cumulative_covered)
        anomaly_text = (
            f"[v1.8 capture audit] Tiered (T0–T7) prompt coverage "
            f"{n_prompts_covered}/189 across all v1.8 captures for R{registry_no:03d}"
            + (" (supplemental obslog)" if is_supplemental else "")
            + f". This obslog: {n_qa} Q&A entries; cumulative DB coverage. "
            f"Missing tier_prompt_codes ({len(missing)}): {missing}"
        )
        if args.live:
            anomaly_seq_row = conn.execute(
                "SELECT MAX(CAST(SUBSTR(finding_id, 13) AS INTEGER)) FROM wa_session_b_findings "
                "WHERE registry_id = ? AND finding_id LIKE 'ANOMALY-%'",
                (registry_no,),
            ).fetchone()
            anomaly_seq = (anomaly_seq_row[0] or 0) + 1
            conn.execute(
                """
                INSERT INTO wa_session_b_findings
                    (finding_id, registry_id, file_id, finding_type, finding,
                     raised_date, session_b_instruction, delete_flag, status)
                VALUES (?, ?, ?, 'DATA_ANOMALY_QA_GAP', ?, ?, ?, 0, 'open')
                """,
                (f"ANOMALY-{registry_no:03d}-{anomaly_seq:03d}", registry_no, file_id,
                 anomaly_text, raised_dt, INSTRUCTION_TAG),
            )
        counts["anomalies_raised"] += 1

    # Synthesis audit: skip for supplemental obslogs (v2/v3 top-up files
    # don't carry synthesis since the original obslog already did).
    if (intra_count != 7 or inter_count != 21) and not is_supplemental:
        anomaly_text = (
            f"[v1.8 capture audit] Synthesis count: intra={intra_count}/7, inter={inter_count}/21. "
            f"Expected 7 + 21 = 28 entries."
        )
        if args.live:
            anomaly_seq_row = conn.execute(
                "SELECT MAX(CAST(SUBSTR(finding_id, 13) AS INTEGER)) FROM wa_session_b_findings "
                "WHERE registry_id = ? AND finding_id LIKE 'ANOMALY-%'",
                (registry_no,),
            ).fetchone()
            anomaly_seq = (anomaly_seq_row[0] or 0) + 1
            conn.execute(
                """
                INSERT INTO wa_session_b_findings
                    (finding_id, registry_id, file_id, finding_type, finding,
                     raised_date, session_b_instruction, delete_flag, status)
                VALUES (?, ?, ?, 'DATA_ANOMALY_SYNTHESIS_INCOMPLETE', ?, ?, ?, 0, 'open')
                """,
                (f"ANOMALY-{registry_no:03d}-{anomaly_seq:03d}", registry_no, file_id,
                 anomaly_text, raised_dt, INSTRUCTION_TAG),
            )
        counts["anomalies_raised"] += 1

    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obslog", required=True)
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if not os.path.exists(args.obslog):
        print(f"ERROR: obslog not found: {args.obslog}")
        return 1

    print(f"Parsing: {args.obslog}")
    parsed = parse_obslog(args.obslog)
    # If still unknown, fall back to filename-based inference
    if parsed["registry_no"] is None:
        parsed["registry_no"] = infer_registry_from_filename(args.obslog)

    print(f"\n=== Parse summary ===")
    print(f"  Registry no:      R{parsed['registry_no']:03d}" if parsed['registry_no'] else "  Registry no: UNKNOWN")
    print(f"  Q&A entries:      {len(parsed['qa_entries'])}")
    print(f"  Synthesis SYN-INTRA: {sum(1 for s in parsed['syn_entries'] if s['kind']=='INTRA')}")
    print(f"  Synthesis SYN-INTER: {sum(1 for s in parsed['syn_entries'] if s['kind']=='INTER')}")
    print(f"  SD pointers (accumulator): {len(parsed['sp_entries'])}")
    print(f"  RD items:         {len(parsed['rd_entries'])}")
    print(f"  Session close:    "
          f"{parsed['session_close']['session_b_status'] if parsed.get('session_close') else 'MISSING'}")

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(
            BACKUP_DIR, f"bible_research_pre_v1_8_obslog_capture_{today_compact()}.db"
        )
        shutil.copy2(args.db, backup)
        print(f"\nBackup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    if args.live:
        conn.execute("BEGIN")

    try:
        counts = capture(args, conn, parsed)
        print(f"\n=== {'LIVE — committing' if args.live else 'DRY-RUN'} ===")
        for k, v in counts.items():
            if k == "missing_question_codes":
                if v:
                    print(f"  {k}: {len(v)} missing — {v[:5]}{' ...' if len(v) > 5 else ''}")
            else:
                print(f"  {k}: {v}")
        if args.live:
            conn.commit()
            print("\n[LIVE] committed.")
    except Exception:
        if args.live:
            conn.rollback()
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
