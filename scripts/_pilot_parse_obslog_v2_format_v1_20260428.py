"""_pilot_parse_obslog_v2_format_v1_20260428.py — Phase 1 parser (v2 obslog format).

The R067 goodness obslog v3 format used:
  - **OBS-067-OBS-NNN** in a ## Complete Observations Register table
  - **Q&A-NNN | QNNN** with Question:/Answer: fields
  - **SD_POINTER — SP-NNN-NNN** in a SD pointer register table

The R030 contrition obslog (2026-04-27) uses a different format:
  - **OBS-030-NNN:** prose markers inline in reading-unit narrative
  - **Q&A NNN** — date, with bullet-list fields (Question code:, Question text:,
    Disposition:, Answer:, Rationale:, Stage 2b note:, Finding type:, ...)
  - **SD POINTER N (NEW)** — raised_in, date, priority, target, with bullet fields
  - ## STAGE 2c — ANALYTIC WORD OUTPUT containing ### CHAPTER N — Title sections

This parser emits the SAME manifest schema as the v1 parser so that the existing
Phase 2 writer (`scripts/_pilot_capture_obslog_to_db_v1_*.py`) consumes it without
any change. Only the parsing logic differs.

Usage:
  python scripts/_pilot_parse_obslog_v2_format_v1_20260428.py \
      --obslog "Sessions/Session_B/09_Analysis_output_logs/words/wa-obslog-ro030-contrition-sb-v1-20260427.md" \
      --registry 30
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Sessions", "Session_B", "09_Analysis_output_logs", "words")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


# ── Parsers ────────────────────────────────────────────────────────────────


def parse_observations(text: str, registry_no: int) -> list:
    """Extract `**OBS-{reg:03d}-{seq}:** {content}` markers, including multi-paragraph content.

    Each marker captures everything until the next OBS marker, the next H3 heading,
    or two newlines followed by something that isn't continuation prose.
    """
    obs = []
    reg_str = f"{registry_no:03d}"
    pat = re.compile(
        rf"^\*\*OBS-{reg_str}-(\d+):\*\*\s+(.+?)(?=\n\*\*OBS-{reg_str}-\d+:|\n###\s|\n##\s|\n\*\*\[|\n\*\*SD POINTER|\n\*\*Set-aside|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    seen = set()
    for m in pat.finditer(text):
        seq = m.group(1)
        content = m.group(2).strip()
        # Capture the unit context (most recent ### UNIT N or ### CHAPTER N heading above)
        unit_m = None
        for um in re.finditer(r"^###\s+(UNIT \d+|CHAPTER \d+)[^\n]*", text[:m.start()], re.MULTILINE):
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
    obs.sort(key=lambda o: int(o["seq"]))
    return obs


def parse_qa_findings(text: str) -> tuple:
    """Extract `**Q&A NNN** — date` entries with bullet-list fields."""
    findings = []
    warnings = []
    seen_qa_seqs = set()

    # Find each Q&A block: from `**Q&A NNN**` to the next `**Q&A NNN**`,
    # `**BATCH N COMPLETE**`, `### Stage 2b Sign-Off`, or `## ` (H2 boundary).
    pat = re.compile(
        r"^\*\*Q&A\s+(\d+)\*\*\s+—\s+(\d{4}-\d{2}-\d{2})\n"
        r"((?:.|\n)*?)"
        r"(?=\n\*\*Q&A\s+\d+[a-z]?\*\*|\n\*\*BATCH\s+\d+\s+COMPLETE|\n###\s|\n##\s)",
        re.MULTILINE,
    )

    # Section headers within Stage 2b log (### Section ...)
    section_headers = []
    for sh in re.finditer(
        r"^####\s+(Section\s+\d+\s+—\s+[^\n]+?)\s+—\s+\d+\s+question",
        text, re.MULTILINE,
    ):
        section_headers.append((sh.start(), sh.group(1).strip()))

    def section_for_pos(pos: int) -> str | None:
        current = None
        for sh_pos, sh_label in section_headers:
            if sh_pos < pos:
                current = sh_label
            else:
                break
        return current

    for m in pat.finditer(text):
        qa_seq = int(m.group(1))
        date = m.group(2)
        body = m.group(3)

        if qa_seq in seen_qa_seqs:
            warnings.append(f"Duplicate Q&A seq {qa_seq}; second occurrence kept too — review obslog.")
        else:
            seen_qa_seqs.add(qa_seq)

        # Bullet-list field extractor: lines like `- Question code: GAP-N-001 (obs_id 221)`
        def extract_field(label: str) -> str | None:
            r = re.search(rf"^- {re.escape(label)}:\s*(.+?)(?=\n- [A-Z]|\n\*\*|\n###|\n##|\Z)",
                          body, re.MULTILINE | re.DOTALL)
            return r.group(1).strip() if r else None

        question_code_raw = extract_field("Question code") or ""
        # Question code may have `(obs_id N)` suffix — strip
        q_code = question_code_raw.split("(")[0].strip() if question_code_raw else None
        question_text = extract_field("Question text")
        scope = extract_field("Scope")
        disposition = extract_field("Disposition")
        # Answer / Rationale / Stage 2b note — disposition determines which we use as 'answer'
        answer = extract_field("Answer")
        rationale = extract_field("Rationale")
        stage_b_note = extract_field("Stage 2b note")
        anchor_verses = extract_field("Anchor verses cited") or extract_field("Anchor verses")
        finding_type = extract_field("Finding type")
        sd_pointer_link = extract_field("SD pointer link")

        # Normalise answer:
        # - ANSWERED / PARTIALLY ANSWERED → use Answer
        # - NOT APPLICABLE → use Rationale
        # - NOT ANSWERED → use Rationale (or whatever explanatory field is present)
        disp_upper = (disposition or "").upper()
        if disp_upper in ("ANSWERED", "PARTIALLY ANSWERED", "FULL", "PARTIAL"):
            primary_answer = answer or rationale
        elif disp_upper in ("NOT APPLICABLE", "N/A", "NA"):
            primary_answer = rationale or answer
        else:
            primary_answer = answer or rationale

        # Skip umbrella entries (have no disposition AND no question_code) — these
        # are section-purpose / "processing batch" headers in the obslog rather than
        # actual Q&As (e.g. Q&A 049, Q&A 050, Q&A 051 in R030 contrition obslog).
        if not disposition and not q_code:
            warnings.append(f"Q&A {qa_seq} skipped — appears to be an umbrella/batch marker (no disposition, no q_code)")
            continue
        # Skip Q&As that explicitly note they couldn't be processed (e.g. Q&A 049 with PROCESS NOTE)
        if not disposition and (not primary_answer or "PROCESS NOTE" in (body or "")):
            warnings.append(f"Q&A {qa_seq} skipped — no disposition recorded (likely abandoned mid-processing)")
            continue

        findings.append({
            "qa_seq": qa_seq,
            "q_code": q_code,
            "section": section_for_pos(m.start()),
            "question": question_text,
            "disposition": disposition,
            "answer": primary_answer,
            "anchor_verses": anchor_verses,
            "finding_type": finding_type,
            "stage_b_note": stage_b_note,
            "review_note": None,
            "scope": scope,
            "date": date,
            "sd_pointer_link": sd_pointer_link,
        })

    findings.sort(key=lambda f: f["qa_seq"])
    return findings, warnings


def parse_sd_pointers(text: str, registry_no: int) -> list:
    """Extract `**SD POINTER N (NEW)** — raised_in, date, priority, session_target` blocks
    plus any `**[PRE-EXISTING] DIM-NN-SDNNN**` references.
    """
    sd = []
    reg_str = f"{registry_no:03d}"

    # New SD pointers from this session
    pat = re.compile(
        r"^\*\*SD POINTER\s+(\d+)\s*\(NEW\)\*\*\s+—\s+([^,\n]+),\s*(\d{4}-\d{2}-\d{2}),\s*(HIGH|MEDIUM|LOW),\s*([^\n]+?)\n"
        r"((?:- .+\n)+)",
        re.MULTILINE,
    )
    for m in pat.finditer(text):
        seq_num = int(m.group(1))
        unit_raised = m.group(2).strip()
        date = m.group(3)
        priority = m.group(4)
        session_target_raw = m.group(5).strip()
        body = m.group(6)

        # Bullets: - Target: ...; - Connecting term/verse: ...; - Question: ...; - Evidence basis: ...
        def field(label: str) -> str | None:
            r = re.search(rf"^- {re.escape(label)}:\s*(.+)$", body, re.MULTILINE)
            return r.group(1).strip() if r else None

        target = field("Target") or field("Target registry")
        connecting = field("Connecting term") or field("Connecting term/verse") or field("Connecting verse")
        question_text = field("Question")
        evidence = field("Evidence basis")

        sd.append({
            "seq": f"SP-{seq_num:03d}",
            "target": target,
            "priority": priority,
            "unit_raised": unit_raised,
            "session_target": session_target_raw,
            "date": date,
            "connecting": connecting,
            "question": question_text,
            "evidence": evidence,
            "detail": {
                "target": target,
                "connecting": connecting,
                "question": question_text,
                "evidence": evidence,
            },
        })

    sd.sort(key=lambda s: int(s["seq"].split("-")[-1]))
    return sd


def parse_chapters(text: str) -> list:
    """Extract `### CHAPTER N — Title` sections under `## STAGE 2c — ANALYTIC WORD OUTPUT`."""
    chapters = []
    # Find Stage 2c block boundaries
    s2c_m = re.search(r"^##\s+STAGE 2c\s+—\s+ANALYTIC WORD OUTPUT", text, re.MULTILINE)
    if not s2c_m:
        return chapters
    start = s2c_m.start()
    # End at next H2 (## ) that's not inside Stage 2c subsections
    next_h2 = re.search(r"\n##\s+(?!STAGE 2c)", text[start + 5:])
    end = (start + 5 + next_h2.start()) if next_h2 else len(text)
    s2c_block = text[start:end]

    # Find each CHAPTER N header
    pat = re.compile(
        r"^###\s+CHAPTER\s+(\d+)\s+—\s+(.+?)\n((?:.|\n)*?)(?=\n###\s+CHAPTER\s+\d+\s+—|\Z)",
        re.MULTILINE,
    )
    for m in pat.finditer(s2c_block):
        n = int(m.group(1))
        title = m.group(2).strip()
        body = m.group(3).strip()
        # Extract source_questions reference if present
        src_m = re.search(r"\*Source observations:.*?\*", body)
        src = src_m.group(0).strip() if src_m else None
        chapters.append({
            "chapter_n": n,
            "title": title,
            "source_questions": src,
            "body": body,
            "char_count": len(body),
        })
    return chapters


def parse_status_update(text: str) -> dict | None:
    """Find session_b_status update intent in SESSION CLOSE / status sections."""
    statuses = ("Analysis Complete", "Pre-Analysis Complete", "Verse Context Reset",
                "Session B Complete", "Ready for Analysis", "In Progress")
    # Look for explicit "session_b_status: → 'X'" or "advance to X"
    for s in statuses:
        if re.search(rf"session_b_status[^.\n]*[`'\"]?{re.escape(s)}[`'\"]?", text):
            return {"target_status": s}
    return None


# ── Validation ─────────────────────────────────────────────────────────────


def validate(manifest: dict, text: str) -> dict:
    issues = []
    warnings = []
    parsed = {
        "qa_findings": len(manifest["qa_findings"]),
        "sd_pointers": len(manifest["sd_pointers"]),
        "observations": len(manifest["observations"]),
        "chapters": len(manifest["chapters"]),
        "prose_supersedes": len(manifest.get("prose_supersedes", [])),
        "gap_questions": len(manifest.get("gap_questions", [])),
        "ws_questions": len(manifest.get("ws_questions", [])),
        "review_notes": len(manifest.get("review_notes", [])),
        "issues": len(manifest.get("issues", [])),
    }
    declared = {}

    # Required fields per Q&A
    qa_missing = [qa["qa_seq"] for qa in manifest["qa_findings"] if not qa.get("q_code")]
    if qa_missing:
        issues.append(f"{len(qa_missing)} Q&A entries missing q_code: {qa_missing[:5]}")
    qa_no_disp = [qa["qa_seq"] for qa in manifest["qa_findings"] if not qa.get("disposition")]
    if qa_no_disp:
        warnings.append(f"{len(qa_no_disp)} Q&A entries missing disposition: {qa_no_disp[:5]}")

    # Required fields per SD pointer
    sd_no_pri = [sp["seq"] for sp in manifest["sd_pointers"] if not sp.get("priority")]
    if sd_no_pri:
        issues.append(f"{len(sd_no_pri)} SD pointers missing priority: {sd_no_pri[:5]}")

    # Chapter count check
    if parsed["chapters"] > 0 and parsed["chapters"] != 6:
        warnings.append(
            f"Chapter count: parser found {parsed['chapters']} (Stage 2c instruction expects 6)"
        )

    return {
        "declared_counts": declared,
        "parsed_counts": parsed,
        "issues": issues,
        "warnings": warnings,
        "ok": len(issues) == 0,
    }


# ── Output ─────────────────────────────────────────────────────────────────


def render_validation_md(manifest: dict, validation: dict, registry_no: int) -> str:
    L = []
    L.append(f"# Obslog Parse — Validation Report — Registry {registry_no:03d} (v2 format)")
    L.append("")
    L.append(f"_Generated {now_iso()}_")
    L.append(f"_Source: {manifest['meta']['source_file']}_")
    L.append("")
    L.append(f"**Parser status:** {'OK' if validation['ok'] else 'ISSUES'}")
    L.append(f"**Issues:** {len(validation['issues'])}  ·  **Warnings:** {len(validation['warnings'])}")
    L.append("")
    L.append("## Counts")
    L.append("")
    L.append("| Category | Parsed |")
    L.append("|---|---:|")
    for cat in ("qa_findings", "sd_pointers", "observations", "chapters",
                "prose_supersedes", "gap_questions", "ws_questions",
                "review_notes", "issues"):
        L.append(f"| {cat} | {validation['parsed_counts'][cat]} |")
    L.append("")
    if validation["issues"]:
        L.append("## Issues")
        L.append("")
        for i in validation["issues"]:
            L.append(f"- {i}")
        L.append("")
    if validation["warnings"]:
        L.append("## Warnings")
        L.append("")
        for w in validation["warnings"]:
            L.append(f"- {w}")
        L.append("")
    return "\n".join(L)


# ── Main ──────────────────────────────────────────────────────────────────


def parse_obslog(obslog_path: str, registry_no: int) -> dict:
    with open(obslog_path, encoding="utf-8") as f:
        text = f.read()

    qa_findings, qa_warnings = parse_qa_findings(text)
    sd_pointers = parse_sd_pointers(text, registry_no)
    observations = parse_observations(text, registry_no)
    chapters = parse_chapters(text)
    status_update = parse_status_update(text)

    return {
        "meta": {
            "source_file": obslog_path,
            "parsed_at": now_iso(),
            "parser_version": "v2-format-v1",
            "registry_no": registry_no,
            "parser_warnings": qa_warnings,
        },
        "qa_findings": qa_findings,
        "sd_pointers": sd_pointers,
        "observations": observations,
        "chapters": chapters,
        "prose_supersedes": [],
        "gap_questions": [],
        "ws_questions": [],
        "review_notes": [],
        "status_update": status_update,
        "issues": [],
    }


def get_word_for_registry(registry_no: int) -> str:
    conn = sqlite3.connect(DB_PATH)
    r = conn.execute("SELECT word FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    conn.close()
    return r[0] if r else f"reg{registry_no:03d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obslog", required=True)
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--out-dir", default=OUT_DIR)
    args = ap.parse_args()

    word = get_word_for_registry(args.registry).replace(" ", "_").lower()
    today = today_compact()

    manifest = parse_obslog(args.obslog, args.registry)
    with open(args.obslog, encoding="utf-8") as f:
        text = f.read()
    validation = validate(manifest, text)

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
        render_validation_md(manifest, validation, args.registry),
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
