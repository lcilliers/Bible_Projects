"""_pilot_parse_obslog_to_db_v1_20260427.py — pilot obslog parser + validator.

Phase 1 of the Approach (a) capture path: parse a Session B obslog .md into a
structured manifest, validate completeness, and (optionally) compare against
already-applied patches as a regression test.

Phase 2 (separate script) will take the manifest and write to the database.
This script does NOT write to the DB.

Usage:
  python scripts/_pilot_parse_obslog_to_db_v1_20260427.py \
      --obslog Sessions/Patches/wa-obslog-ro-067-goodness-anlys-v2-20260426.md \
      --registry 67 \
      --compare-archive 'archive/patches/wa-067-goodness-patch-*-20260427.json'

Outputs:
  Sessions/Session_B/09_Analysis_output_logs/words/wa-{NNN}-{word}-obslog-parse-manifest-v1-{date}.json
  Sessions/Session_B/09_Analysis_output_logs/words/wa-{NNN}-{word}-obslog-validation-v1-{date}.md
"""
from __future__ import annotations
import argparse
import glob
import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Sessions", "Session_B", "09_Analysis_output_logs", "words")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


# ── Parsers ─────────────────────────────────────────────────────────────


def parse_qa_findings(text: str) -> tuple:
    """Extract Q&A entries from Stage 2b sections.

    Each entry has the pattern:
      **Q&A-NNN | QNNN**
      [optional] Section: ...
      Question: ...
      Disposition: ...
      Answer: <multi-line>
      Anchor verses: ...
      Finding type: ...
      [optional QUESTION REVIEW NOTE: ...]

    Returns (findings, parser_warnings). Section field is often omitted in
    Section 3+ entries — fallback is the most-recent '## Stage 2b Q&A Log
    — Section X' header above the entry. Stub markers (no Question field)
    are detected and surfaced as parser_warnings for review.
    """
    findings = []
    parser_warnings = []
    seen_q_codes = {}  # q_code -> first-seen qa_seq to detect dup markers

    # Pre-build an index of Stage 2b section header positions for fallback
    section_headers = []
    for sh in re.finditer(
        r"^##\s+Stage 2b Q&A Log\s+—\s+Section\s+(\d+).*?$",
        text, re.MULTILINE,
    ):
        section_headers.append((sh.start(), sh.group(1), sh.group(0).strip()))

    def section_for_pos(pos: int) -> str | None:
        """Return the most recent section header above pos."""
        current = None
        for sh_pos, sh_n, sh_line in section_headers:
            if sh_pos < pos:
                current = sh_line
            else:
                break
        if not current:
            return None
        # Extract canonical "Section X — Title" from the header line
        m = re.search(r"Section\s+(\d+)\s*—\s*(.+?)(?:\s*\(|$)", current)
        if m:
            return f"Section {m.group(1)} — {m.group(2).strip()}"
        return current

    # Per analysis-output v1_5 §v2.8: catalogue codes can be QNNN, GAP-N-NNN,
    # GAP-S{n}-NNN, or compound like "Q034 through Q041 (consolidated)" / "GAP-S3 questions".
    # Accept any non-asterisk content as the code; downstream resolution will
    # match against catalogue.question_code where possible (and skip otherwise).
    for m in re.finditer(r"\*\*Q&A-(\d+)\s*\|\s*([^\*\n]+?)\*\*(.*?)$", text, re.MULTILINE):
        start = m.start()
        # Find next Q&A or H2 boundary
        next_m = re.search(r"\n\*\*Q&A-\d+", text[start + 1:])
        next_h2 = re.search(r"\n##\s", text[start + 1:])
        candidates = [c for c in (next_m, next_h2) if c]
        end = (start + 1 + min(c.start() for c in candidates)) if candidates else len(text)
        block = text[start:end]
        qa_seq = int(m.group(1))
        q_code = m.group(2)  # full catalogue code, no Q-prefix prepending
        marker_suffix = m.group(3).strip()  # text after the marker on the same line

        # Detect true stub markers (no Question AND no Disposition). Some Q&As
        # legitimately omit Question text when disposition=NOT APPLICABLE — those
        # are NOT stubs; they're concise NA entries. Accept both flat "Question:"
        # and bullet-list "- Question:" forms.
        question_present = bool(re.search(r"^(?:- )?Question:\s*", block, re.MULTILINE))
        disposition_present = bool(re.search(r"^(?:- )?Disposition:\s*", block, re.MULTILINE))
        if not question_present and not disposition_present:
            parser_warnings.append(
                f"Stub Q&A marker at qa_seq={qa_seq}, q_code={q_code} — no Question and no Disposition "
                f"(suffix on marker line: {marker_suffix!r}). Skipping."
            )
            continue

        # Duplicate-marker check
        if q_code in seen_q_codes:
            parser_warnings.append(
                f"Duplicate Q&A marker {q_code} (already seen at qa_seq={seen_q_codes[q_code]}); "
                f"this occurrence at qa_seq={qa_seq} kept too — review obslog for typo."
            )
        else:
            seen_q_codes[q_code] = qa_seq

        section = _extract_field(block, "Section") or section_for_pos(start)
        question = _extract_field(block, "Question")
        disposition = _extract_field(block, "Disposition")
        answer = _extract_multiline_field(
            block, "Answer",
            stop_fields=("Anchor verses", "Finding type", "Stage 2b note", "[QUESTION REVIEW NOTE",
                         "Evidence basis", "- Anchor verses", "- Finding type", "- Stage 2b note",
                         "- Evidence basis"),
        )
        # NOT APPLICABLE / NOT ANSWERED Q&As use Rationale: instead of Answer:
        if not answer:
            answer = _extract_multiline_field(
                block, "Rationale",
                stop_fields=("Anchor verses", "Finding type", "Stage 2b note", "[QUESTION REVIEW NOTE",
                             "Evidence basis", "- Anchor verses", "- Finding type", "- Stage 2b note",
                             "- Evidence basis"),
            )
        anchor_verses = _extract_field(block, "Anchor verses")
        finding_type = _extract_field(block, "Finding type")
        stage_b_note = _extract_field(block, "Stage 2b note")
        review_note_m = re.search(r"\[QUESTION REVIEW NOTE:\s*(.+?)\]", block, re.DOTALL)
        review_note = review_note_m.group(1).strip() if review_note_m else None
        findings.append({
            "qa_seq": qa_seq,
            "q_code": q_code,
            "section": section,
            "question": question,
            "disposition": disposition,
            "answer": answer,
            "anchor_verses": anchor_verses,
            "finding_type": finding_type,
            "stage_b_note": stage_b_note,
            "review_note": review_note,
        })
    return findings, parser_warnings


def _extract_field(block: str, field_name: str) -> str | None:
    """Extract `{label}: value` — accepts both flat and `- ` bullet-prefixed forms."""
    m = re.search(rf"^(?:- )?{re.escape(field_name)}:\s*(.+)$", block, re.MULTILINE)
    return m.group(1).strip() if m else None


def _extract_multiline_field(block: str, field_name: str, stop_fields: tuple) -> str | None:
    # Match optional bullet prefix, then label, then value spanning lines until
    # a stop field (with or without bullet prefix) is reached.
    pat = (
        rf"(?:^- )?{re.escape(field_name)}:\s*(.+?)"
        + r"(?=" + "|".join(rf"\n(?:- )?{re.escape(s)}" for s in stop_fields) + ")"
    )
    m = re.search(pat, block, re.DOTALL)
    return m.group(1).strip() if m else None


def parse_sd_pointers(text: str) -> list:
    """Extract SD pointers — supports two formats:

    (A) Register table under '## Complete SD Pointer Register':
        | SP-NNN | target | priority | unit |
    (B) Flat `**SP-NNN-NNN** — raised in Unit X, date, priority, target` blocks
        under '## SD Pointer Accumulator' (canonical v1.5 form, §v2.8).
    """
    sd = []
    seen_seqs = set()

    # Format (A): register table
    m = re.search(r"##\s+Complete SD Pointer Register\s*\n", text)
    if m:
        start = m.end()
        section = text[start:start + 8000]
        for row_m in re.finditer(
            r"^\|\s*(SP-\d+)\s*\|\s*(.+?)\s*\|\s*(HIGH|MEDIUM|LOW)\s*\|\s*([^|]+?)\s*\|",
            section, re.MULTILINE,
        ):
            seq = row_m.group(1)
            if seq in seen_seqs:
                continue
            seen_seqs.add(seq)
            sd.append({
                "seq": seq,
                "target": row_m.group(2).strip(),
                "priority": row_m.group(3).strip(),
                "unit_raised": row_m.group(4).strip(),
            })

    # Format (B): flat **SP-NNN-NNN** entries with bullet fields, scanned across
    # the whole document. Multiple accumulator sections (working / Final) may
    # exist; we capture every SP-NNN-NNN block regardless. Variants accepted:
    #   "raised in Unit X" or "raised Unit X" (no "in")
    for row_m in re.finditer(
        r"\*\*SP-(\d{3}-\d{3})\*\*\s+—\s+raised(?:\s+in)?\s+(.+?),\s*(\d{4}-\d{2}-\d{2}),\s*(HIGH|MEDIUM|LOW),\s*([^\n]+?)\n((?:- .+\n)*)",
        text,
    ):
        seq = "SP-" + row_m.group(1)
        if seq in seen_seqs:
            continue
        seen_seqs.add(seq)
        unit = row_m.group(2).strip()
        date = row_m.group(3)
        priority = row_m.group(4)
        session_target = row_m.group(5).strip()
        body = row_m.group(6)

        def field(label, body=body):
            r = re.search(rf"^- {re.escape(label)}:\s*(.+)$", body, re.MULTILINE)
            return r.group(1).strip() if r else None

        target = field("Target") or field("Target registry")
        sd.append({
            "seq": seq,
            "target": target or session_target,
            "priority": priority,
            "unit_raised": unit,
            "session_target": session_target,
            "date": date,
            "detail": {
                "target": target,
                "connecting": field("Connecting term") or field("Connecting term/verse")
                              or field("Connecting verse"),
                "question": field("Question"),
                "evidence": field("Evidence basis"),
            },
        })

    # Per-pointer detail blocks: '**SD POINTER raised — SP-NNN:**'
    detail = {}
    for det_m in re.finditer(
        r"\*\*SD POINTER raised\s+—\s+(SP-\d+):\*\*\s*\n((?:- .+\n)+)",
        text,
    ):
        sp_id = det_m.group(1)
        body = det_m.group(2)
        fields = {}
        for line in body.split("\n"):
            ln = line.strip()
            if not ln.startswith("- "):
                continue
            ln = ln[2:]
            if ":" in ln:
                k, v = ln.split(":", 1)
                fields[k.strip()] = v.strip()
        detail[sp_id] = fields
    for sp in sd:
        if sp["seq"] in detail:
            sp["detail"] = detail[sp["seq"]]
    return sd


def parse_observations(text: str, registry_no: int | None = None) -> list:
    """Extract observations — supports two formats:

    (A) Register table under '## Complete Observations Register':
        | OBS-NNN | content | unit |
    (B) Inline `**OBS-{registry:03d}-{seq:03d}:** {content}` markers
        scattered through reading-unit prose (canonical v1.5, §v2.8).

    `registry_no` is required for Format (B) so the regex can disambiguate
    R030's OBS markers from any other registry's that might appear.
    """
    obs = []
    seen = set()

    # Format (A): register table
    m = re.search(r"##\s+Complete Observations Register\s*\n", text)
    if m:
        start = m.end()
        next_h2 = re.search(r"\n##\s", text[start:])
        end = start + (next_h2.start() if next_h2 else len(text) - start)
        section = text[start:end]
        for row_m in re.finditer(
            r"^\|\s*(OBS-\d+)\s*\|\s*(.+?)\s*\|\s*(\S+)\s*\|",
            section, re.MULTILINE,
        ):
            if row_m.group(1) == "OBS":
                continue
            seq = row_m.group(1)
            if seq in seen:
                continue
            seen.add(seq)
            obs.append({
                "seq": seq,
                "content": row_m.group(2).strip(),
                "unit": row_m.group(3).strip(),
            })

    # Format (B): inline **OBS-{reg:03d}-{seq:03d}:** markers
    if registry_no is not None:
        reg_str = f"{registry_no:03d}"
        pat = re.compile(
            rf"^\*\*OBS-{reg_str}-(\d+):\*\*\s+(.+?)"
            rf"(?=\n\*\*OBS-{reg_str}-\d+:|\n###\s|\n##\s|\n\*\*\[|\n\*\*SD POINTER|\n\*\*Set-aside|\Z)",
            re.MULTILINE | re.DOTALL,
        )
        for m_obs in pat.finditer(text):
            seq = m_obs.group(1)
            content = m_obs.group(2).strip()
            # Track unit by walking back to most recent ### UNIT or ### CHAPTER heading
            unit_m = None
            for um in re.finditer(r"^###\s+(UNIT \d+|Unit \d+|CHAPTER \d+|Chapter \d+)[^\n]*",
                                  text[:m_obs.start()], re.MULTILINE):
                unit_m = um
            unit = unit_m.group(0).strip() if unit_m else None
            if seq in seen:
                continue
            seen.add(seq)
            obs.append({
                "seq": seq,
                "content": content,
                "unit": unit,
            })

    obs.sort(key=lambda o: int(re.sub(r"\D", "", o["seq"])) if re.sub(r"\D", "", o["seq"]) else 0)
    return obs


def parse_chapters(text: str) -> list:
    """Extract Stage 2c chapters."""
    chapters = []
    for m in re.finditer(
        r"##\s+Stage 2c\s+—\s+Chapter\s+(\d+):\s+(.+?)\n((?:.|\n)+?)(?=\n##\s+Stage 2c\s+—\s+Chapter|\n##\s+(?!Stage 2c))",
        text,
    ):
        n = int(m.group(1))
        title = m.group(2).strip()
        body = m.group(3).strip()
        # Extract source_questions reference if present
        src_m = re.search(r"\*\*Source questions:\*\*\s*(.+?)\n", body)
        src = src_m.group(1).strip() if src_m else None
        chapters.append({
            "chapter_n": n,
            "title": title,
            "source_questions": src,
            "body": body,
            "char_count": len(body),
        })
    return chapters


def parse_prose_supersedes(text: str) -> list:
    """Extract Stage 2c SUPERSEDE blocks (revision sessions, per v2.7 / v2.CC9).

    Block format:
      ### SUPERSEDE: sb_s2c_ch{n} — {title}

      **registry_id:** {n}
      **author:** claude_ai
      **version:** supersedes prior sb_s2c_ch{n} for registry {n}
      **source_file:** {filename}

      ---

      {body with inline citations}
    """
    blocks = []
    pat = re.compile(
        r"^###\s+SUPERSEDE:\s+(sb_s2c_ch\d+)\s+—\s+(.+?)\n"
        r"((?:.|\n)*?)"
        r"(?=\n###\s+SUPERSEDE:|\n##\s|\Z)",
        re.MULTILINE,
    )
    for m in pat.finditer(text):
        section_code = m.group(1).strip()
        title = m.group(2).strip()
        block_body = m.group(3)

        reg_m = re.search(r"\*\*registry_id:\*\*\s*(\d+)", block_body)
        author_m = re.search(r"\*\*author:\*\*\s*(.+?)$", block_body, re.MULTILINE)
        source_m = re.search(r"\*\*source_file:\*\*\s*(.+?)$", block_body, re.MULTILINE)

        # Body sits after the `---` separator that closes the metadata header.
        # Split on first standalone `---` line; if absent, treat full block as body.
        parts = re.split(r"\n---\s*\n", block_body, maxsplit=1)
        body = parts[1].strip() if len(parts) == 2 else block_body.strip()

        blocks.append({
            "section_code": section_code,
            "title": title,
            "registry_id": int(reg_m.group(1)) if reg_m else None,
            "author": author_m.group(1).strip() if author_m else "claude_ai",
            "source_file": source_m.group(1).strip() if source_m else None,
            "body": body,
            "char_count": len(body),
        })
    return blocks


def parse_gap_and_ws_questions(text: str) -> dict:
    """Extract GAP and WORD-SPECIFIC question proposals from Gap Assessment sections."""
    gaps = []
    ws = []
    for m in re.finditer(r"\[GAP-(S\d+)-(\d+)\s*—\s*PROPOSED ADDITION TO GENERIC CATALOGUE\]\s*\n((?:.|\n)+?)(?=\n\[(?:GAP-|WORD-SPECIFIC-)|\n\*\*[A-Z]|\n##|\n---)", text):
        section = m.group(1)
        seq = m.group(2)
        body = m.group(3)
        gaps.append({
            "id": f"GAP-{section}-{seq}",
            "section": section,
            "question": _line_after_label(body, "Question"),
            "rationale": _line_after_label(body, "Rationale"),
            "answer_for_word": _line_after_label(body, "Answer for R\\d+|Answer for", multiline=True),
        })
    for m in re.finditer(r"\[WORD-SPECIFIC-(\d+)\s*—\s*R(\d+)\]\s*\n((?:.|\n)+?)(?=\n\[(?:GAP-|WORD-SPECIFIC-)|\n\*\*[A-Z]|\n##|\n---)", text):
        seq = m.group(1)
        reg_no = int(m.group(2))
        body = m.group(3)
        ws.append({
            "id": f"WS-{seq}",
            "registry_no": reg_no,
            "question": _line_after_label(body, "Question"),
            "answer": _line_after_label(body, "Answer", multiline=True),
        })
    return {"gap": gaps, "ws": ws}


def _line_after_label(body: str, label_pattern: str, multiline: bool = False) -> str | None:
    if multiline:
        m = re.search(rf"({label_pattern}):\s*((?:.|\n)+?)(?=\n[A-Z][a-z]+:|\Z)", body)
    else:
        m = re.search(rf"({label_pattern}):\s*(.+)$", body, re.MULTILINE)
    return m.group(2).strip() if m else None


def parse_review_notes(text: str) -> list:
    """Extract question review notes from Q&A entries and Gap Assessment sections."""
    notes = []
    # Inline notes within Q&A entries
    for m in re.finditer(
        r"\*\*Q&A-(\d+)\s*\|\s*Q(\d+)\*\*[\s\S]*?\[QUESTION REVIEW NOTE:\s*(.+?)\]",
        text,
    ):
        qa_seq = int(m.group(1))
        q_code = "Q" + m.group(2)
        note = m.group(3).strip()
        notes.append({
            "source": "qa_entry",
            "qa_seq": qa_seq,
            "q_code": q_code,
            "note": note,
        })
    # Section-level review-note summaries
    for m in re.finditer(
        r"\*\*SECTION (\d+) QUESTION REVIEW NOTES\s*—\s*SUMMARY:\*\*\s*\n((?:- .+\n)+)",
        text,
    ):
        section_n = int(m.group(1))
        body = m.group(2)
        for ln_m in re.finditer(r"^- (.+)$", body, re.MULTILINE):
            line = ln_m.group(1).strip()
            notes.append({
                "source": "section_summary",
                "section_n": section_n,
                "note": line,
            })
    return notes


def parse_status_update(text: str) -> dict | None:
    """Extract status update intent from one of three locations:

    (1) `## Session Close` → `session_b_status: 'Analysis Complete'` (canonical v1.5).
    (2) `### Category F — Registry Status Update` (legacy patch-flow form).
    (3) Any `session_b_status: 'X'` quoted assignment near the end of the obslog.
    """
    statuses = "(Analysis Complete|Pre-Analysis Complete|Verse Context Reset|Session B Complete|Ready for Analysis|In Progress)"

    # Pattern 1: Session Close section (v1.5 canonical)
    sc = re.search(r"##\s+Session Close\b", text)
    if sc:
        section = text[sc.end():sc.end() + 4000]
        m = re.search(
            rf"session_b_status\s*:?\s*[`'\"]\s*{statuses}\s*[`'\"]",
            section,
        )
        if m:
            return {"target_status": m.group(1).strip()}

    # Pattern 2: legacy Category F section
    m = re.search(
        rf"###\s+Category F\s+—\s+Registry Status Update[\s\S]*?session_b_status[^\n]*?[`'\"]{statuses}[`'\"]",
        text,
    )
    if m:
        return {"target_status": m.group(1).strip()}
    m2 = re.search(
        r"###\s+Category F[\s\S]*?session_b_status\s*→\s*['\"`]?([A-Z][\w\s]+?)['\"`.]",
        text,
    )
    if m2:
        return {"target_status": m2.group(1).strip()}

    # Pattern 3: catch-all — any quoted status assignment
    m3 = re.search(
        rf"session_b_status\s*:?\s*[`'\"]\s*{statuses}\s*[`'\"]",
        text,
    )
    if m3:
        return {"target_status": m3.group(1).strip()}

    return None


def parse_issues(text: str) -> list:
    """Extract from Issues and Gaps Register table."""
    m = re.search(r"##\s+Issues and Gaps Register\s*\n", text)
    if not m:
        return []
    start = m.end()
    next_h2 = re.search(r"\n##\s", text[start:])
    end = start + (next_h2.start() if next_h2 else len(text) - start)
    section = text[start:end]
    issues = []
    for row_m in re.finditer(
        r"^\|\s*(ISSUE-[A-Z\d]+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|",
        section, re.MULTILINE,
    ):
        issues.append({
            "id": row_m.group(1),
            "category": row_m.group(2).strip(),
            "description": row_m.group(3).strip(),
        })
    return issues


# ── Validation ──────────────────────────────────────────────────────────


def validate(manifest: dict, text: str) -> dict:
    """Compare declared counts vs parsed counts. Return validation report."""
    issues = []
    warnings = []
    declared = {}
    parsed = {
        "qa_findings": len(manifest["qa_findings"]),
        "sd_pointers": len(manifest["sd_pointers"]),
        "observations": len(manifest["observations"]),
        "chapters": len(manifest["chapters"]),
        "prose_supersedes": len(manifest.get("prose_supersedes", [])),
        "gap_questions": len(manifest["gap_questions"]),
        "ws_questions": len(manifest["ws_questions"]),
        "review_notes": len(manifest["review_notes"]),
        "issues": len(manifest["issues"]),
    }

    # Declared count assertions from the obslog itself
    declared_qa = re.search(r"(\d+)\s+catalogue questions processed", text)
    if declared_qa:
        declared["qa_findings"] = int(declared_qa.group(1))
        if declared["qa_findings"] != parsed["qa_findings"]:
            issues.append(
                f"Q&A count mismatch: obslog declares {declared['qa_findings']}, parser found {parsed['qa_findings']}"
            )

    declared_sd = re.search(r"SP-001 through SP-(\d+)", text)
    if declared_sd:
        expected = int(declared_sd.group(1))
        declared["sd_pointers"] = expected
        if expected != parsed["sd_pointers"]:
            issues.append(
                f"SD pointer count mismatch: obslog declares SP-001..SP-{expected:03d} = {expected}, parser found {parsed['sd_pointers']}"
            )

    declared_obs = re.search(r"OBS-001 through OBS-(\d+)", text)
    if declared_obs:
        expected = int(declared_obs.group(1))
        declared["observations"] = expected
        if expected > parsed["observations"]:
            warnings.append(
                f"Observations count: obslog declares OBS-001..OBS-{expected:03d} = {expected}, parser found {parsed['observations']} (some may be in Stage 2b/2c text rather than the register)"
            )

    # Chapter count check
    if parsed["chapters"] > 0 and parsed["chapters"] != 6:
        warnings.append(
            f"Chapter count: parser found {parsed['chapters']} (Stage 2c instruction expects 6 — Word Characteristic Summary, Word Impact Description, Annotated Verse Evidence, Original Language Vocabulary, Connections, Open Items)"
        )

    # Required-field checks per Q&A
    qa_missing_fields = []
    for qa in manifest["qa_findings"]:
        missing = [k for k in ("section", "question", "disposition") if not qa.get(k)]
        if missing:
            qa_missing_fields.append((qa["qa_seq"], missing))
    if qa_missing_fields:
        issues.append(f"{len(qa_missing_fields)} Q&A entries missing required fields: {qa_missing_fields[:5]}")

    # Required-field checks per SD pointer
    sd_missing_fields = [sp["seq"] for sp in manifest["sd_pointers"] if not sp.get("priority")]
    if sd_missing_fields:
        issues.append(f"{len(sd_missing_fields)} SD pointers missing priority: {sd_missing_fields[:5]}")

    return {
        "declared_counts": declared,
        "parsed_counts": parsed,
        "issues": issues,
        "warnings": warnings,
        "ok": len(issues) == 0,
    }


# ── Patch comparison (regression test) ──────────────────────────────────


def compare_against_patches(manifest: dict, patch_glob: str) -> dict:
    """Compare parser output against already-applied patches as regression test."""
    patches = sorted(glob.glob(patch_glob))
    results = {"patches": [], "summary": {}}
    if not patches:
        results["summary"]["note"] = f"No patches matched glob: {patch_glob}"
        return results

    parser_sd_seqs = {sp["seq"] for sp in manifest["sd_pointers"]}
    parser_qa_q_codes = {qa["q_code"] for qa in manifest["qa_findings"]}

    for p in patches:
        try:
            with open(p, encoding="utf-8") as f:
                patch = json.load(f)
        except Exception as e:
            results["patches"].append({"file": os.path.basename(p), "error": str(e)})
            continue
        meta = patch.get("_patch_meta", {})
        ops = patch.get("operations", [])
        ptype = meta.get("patch_type")
        entry = {
            "file": os.path.basename(p),
            "patch_type": ptype,
            "operations": len(ops),
        }
        if ptype == "VCSDPOINTERS":
            patch_seqs = set()
            for op in ops:
                fields = op.get("fields", {}) or op.get("values", {})
                fl = fields.get("flag_label", "")
                # Patch labels can be "SP-067-001" (registry-prefixed) or "SP-001"
                # Normalise to canonical "SP-NNN" form by extracting the trailing 3-digit group.
                m = re.search(r"-(\d{3})$", fl) or re.search(r"^SP-(\d+)$", fl)
                if m:
                    patch_seqs.add(f"SP-{int(m.group(1)):03d}")
            entry["patch_sd_pointer_count"] = len(patch_seqs)
            entry["parser_sd_pointer_count"] = len(parser_sd_seqs)
            entry["both_match"] = (patch_seqs == parser_sd_seqs)
            entry["only_in_patch"] = sorted(patch_seqs - parser_sd_seqs)
            entry["only_in_parser"] = sorted(parser_sd_seqs - patch_seqs)
            entry["sample_patch_seqs"] = sorted(patch_seqs)[:5]
        elif ptype == "SESSIONB_FINDINGS":
            patch_q_codes = set()
            for op in ops:
                fields = op.get("fields", {}) or op.get("values", {})
                desc = fields.get("description", "")
                m = re.search(r"\[Q(\d+)\]", desc)
                if m:
                    patch_q_codes.add("Q" + m.group(1))
            entry["patch_qa_finding_count"] = len(ops)
            entry["parser_qa_total"] = len(parser_qa_q_codes)
            entry["parser_qa_answered"] = len([qa for qa in manifest["qa_findings"] if qa.get("disposition") in ("ANSWERED", "PARTIALLY")])
            entry["patch_q_codes_sample"] = sorted(patch_q_codes)[:10]
            entry["note"] = (
                f"Patch contains {len(ops)} findings; parser sees {len(parser_qa_q_codes)} total Q&A. "
                f"The patch is the ANSWERED subset; mismatch in raw count is expected."
            )
        elif ptype == "SESSIONB":
            target = None
            for op in ops:
                if op.get("table") == "word_registry":
                    fields = op.get("fields", {}) or op.get("values", {}) or op.get("set", {})
                    target = fields.get("session_b_status")
            # Some patch shapes carry status in _patch_meta.session_b_status
            if not target:
                target = meta.get("session_b_status")
            entry["patch_target_status"] = target
            su = manifest.get("status_update")
            entry["parser_target_status"] = su.get("target_status") if su else None
            entry["match"] = (target == entry["parser_target_status"])
        results["patches"].append(entry)

    return results


# ── Output ──────────────────────────────────────────────────────────────


def render_validation_md(manifest: dict, validation: dict, comparison: dict, registry_no: int) -> str:
    L = []
    L.append(f"# Obslog Parse — Validation Report — Registry {registry_no:03d}")
    L.append("")
    L.append(f"_Generated {now_iso()}_")
    L.append(f"_Source: {manifest['meta']['source_file']}_")
    L.append("")
    L.append("## Status")
    L.append("")
    L.append(f"**Parser status:** {'✅ OK' if validation['ok'] else '⚠️ Issues found'}")
    L.append(f"**Issues:** {len(validation['issues'])}  ·  **Warnings:** {len(validation['warnings'])}")
    L.append("")
    L.append("## Counts (declared vs parsed)")
    L.append("")
    L.append("| Category | Declared | Parsed | Match |")
    L.append("|---|---:|---:|---|")
    for cat in ("qa_findings", "sd_pointers", "observations", "chapters", "prose_supersedes", "gap_questions", "ws_questions", "review_notes", "issues"):
        d = validation["declared_counts"].get(cat, "—")
        p = validation["parsed_counts"][cat]
        match = "—" if d == "—" else ("✓" if d == p else "⚠️ mismatch")
        L.append(f"| {cat} | {d} | {p} | {match} |")
    L.append("")
    if validation["issues"]:
        L.append("## Issues (must resolve before DB writes)")
        L.append("")
        for i in validation["issues"]:
            L.append(f"- ❌ {i}")
        L.append("")
    if validation["warnings"]:
        L.append("## Warnings")
        L.append("")
        for w in validation["warnings"]:
            L.append(f"- ⚠️ {w}")
        L.append("")
    # Comparison block
    L.append("## Comparison against applied patches (regression test)")
    L.append("")
    if comparison["patches"]:
        for p in comparison["patches"]:
            L.append(f"### `{p['file']}` — type `{p.get('patch_type')}` — {p.get('operations')} ops")
            for k, v in p.items():
                if k in ("file", "patch_type", "operations"):
                    continue
                L.append(f"- **{k}:** {v}")
            L.append("")
    else:
        L.append(comparison.get("summary", {}).get("note", "_No patches compared._"))
        L.append("")
    # Sample first few items per category for visual inspection
    L.append("## Parser samples (first 3 per category)")
    L.append("")
    for cat in ("qa_findings", "sd_pointers", "observations", "chapters", "prose_supersedes", "gap_questions", "ws_questions"):
        L.append(f"### {cat}")
        L.append("")
        items = manifest[cat][:3]
        if not items:
            L.append("_(none parsed)_")
        else:
            for it in items:
                summary = json.dumps(it, ensure_ascii=False)
                L.append(f"- `{summary[:300]}{'…' if len(summary) > 300 else ''}`")
        L.append("")
    return "\n".join(L)


# ── Main ────────────────────────────────────────────────────────────────


def parse_obslog(obslog_path: str, registry_no: int) -> dict:
    with open(obslog_path, encoding="utf-8") as f:
        text = f.read()

    qa_findings, qa_warnings = parse_qa_findings(text)
    sd_pointers = parse_sd_pointers(text)
    observations = parse_observations(text, registry_no=registry_no)
    chapters = parse_chapters(text)
    prose_supersedes = parse_prose_supersedes(text)
    gap_ws = parse_gap_and_ws_questions(text)
    review_notes = parse_review_notes(text)
    status_update = parse_status_update(text)
    issues = parse_issues(text)

    return {
        "meta": {
            "source_file": obslog_path,
            "parsed_at": now_iso(),
            "parser_version": "v1",
            "registry_no": registry_no,
            "parser_warnings": qa_warnings,
        },
        "qa_findings": qa_findings,
        "sd_pointers": sd_pointers,
        "observations": observations,
        "chapters": chapters,
        "prose_supersedes": prose_supersedes,
        "gap_questions": gap_ws["gap"],
        "ws_questions": gap_ws["ws"],
        "review_notes": review_notes,
        "status_update": status_update,
        "issues": issues,
    }


def get_word_for_registry(registry_no: int) -> str:
    conn = sqlite3.connect(DB_PATH)
    r = conn.execute("SELECT word FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    conn.close()
    return r[0] if r else f"reg{registry_no:03d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obslog", required=True, help="path to obslog .md")
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--compare-archive", default=None,
                    help="glob pattern of applied patches to compare against")
    ap.add_argument("--out-dir", default=OUT_DIR)
    args = ap.parse_args()

    word = get_word_for_registry(args.registry)
    today = today_compact()

    manifest = parse_obslog(args.obslog, args.registry)
    with open(args.obslog, encoding="utf-8") as f:
        text = f.read()
    validation = validate(manifest, text)
    comparison = (compare_against_patches(manifest, args.compare_archive)
                  if args.compare_archive else {"patches": [], "summary": {"note": "No --compare-archive supplied; comparison skipped."}})

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    base = f"wa-{args.registry:03d}-{word}-obslog"
    manifest_path = out_dir / f"{base}-parse-manifest-v1-{today}.json"
    validation_path = out_dir / f"{base}-validation-v1-{today}.md"

    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    validation_path.write_text(
        render_validation_md(manifest, validation, comparison, args.registry),
        encoding="utf-8",
    )
    print(f"Wrote manifest:    {manifest_path}  ({manifest_path.stat().st_size:,} bytes)")
    print(f"Wrote validation:  {validation_path}")
    print()
    print(f"Parser status: {'OK' if validation['ok'] else 'ISSUES'}")
    print(f"Counts: {validation['parsed_counts']}")
    if validation["issues"]:
        print(f"\n{len(validation['issues'])} ISSUE(S):")
        for i in validation["issues"]:
            print(f"  - {i}")
    if validation["warnings"]:
        print(f"\n{len(validation['warnings'])} warning(s):")
        for w in validation["warnings"]:
            print(f"  - {w}")
    return 0 if validation["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
