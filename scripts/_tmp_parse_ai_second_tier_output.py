"""_tmp_parse_ai_second_tier_output.py

Parse AI second-tier analysis output files into structured capture-preview
JSON + markdown.  Read-only — does NOT write to the database.

For each word folder under research/investigations/ai_question_test_bundle_20260429/
that contains an analysis file (`WA-*second-tier*` or `WA-*prompt-test*`) and
optionally a session log (`WA-session-log-*`), this script extracts:

  · per-prompt response — status (A/P/S/N), notation flags, body text,
    referenced findings (OBS-NNN-NNN), SD pointers (DIM-NNN-SD###, SP-NNN-NNN),
    inline verse refs, body word count
  · session-log consolidated lists — new findings (§7.2), gap consolidation
    (§8), researcher-decision items (§9), next steps / Session D implications
    (§11)

Output (per word):
  research/investigations/ai_question_test_bundle_20260429/{folder}/parsed-capture-preview.json
  research/investigations/ai_question_test_bundle_20260429/{folder}/parsed-capture-preview.md

Plus a top-level capture-preview-index.md.

Usage:
  python scripts/_tmp_parse_ai_second_tier_output.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone

BUNDLE_DIR = os.path.join("research", "investigations", "ai_question_test_bundle_20260429")

STRONGS_RE = re.compile(r"\b([HG]\d{4}[A-Z]?)\b")
OBS_REF_RE = re.compile(r"\bOBS-\d{2,3}(?:-OBS)?-\d{1,3}\b")
SD_REF_RE = re.compile(r"\b(?:DIM-\d{1,3}-SD\d{2,3}|SP-\d{2,3}-\d{2,3})\b")
DIM_REF_RE = re.compile(r"\bDIM-\d{1,3}(?:-SD\d{2,3})?\b")
GROUP_CODE_RE = re.compile(r"\b\d{3,4}-\d{3}\b")

TIER_RE = re.compile(r"^## (T\d) — (.+?)\s*$")
COMPONENT_RE = re.compile(r"^### (T\d\.\d+)\s*[—-]\s*(.+?)\s*$")
PROMPT_RE = re.compile(r"^\*\*Prompt (\d+):\*\*\s*(.+?)\s*$")
STATUS_RE = re.compile(
    r"^\*\*Status:?\s*([APSN])\b(?:\s*\([^)]*\))?\*\*"
    r"(?:\s*\|\s*\*([^*]+?)\*\s*)?$"
)
INLINE_NOTATION_RE = re.compile(r"\*(Consistent with prior[^*]*|Adds structure[^*]*|New finding[^*]*|Gap identified[^*]*)\*")


def find_verse_refs(text: str, book_codes: set[str]) -> list[str]:
    if not text:
        return []
    out: list[str] = []
    seen: set[str] = set()
    pat = re.compile(r"\b(\d?\s?[A-Z][a-z]{2})\s+(\d+):(\d+)(?:[–—\-]\d+)?\b")
    for m in pat.finditer(text):
        code, ch, vs = m.group(1).strip(), m.group(2), m.group(3)
        code_norm = code.replace(" ", "")
        if code_norm in book_codes:
            ref = f"{code_norm} {ch}:{vs}"
            if ref not in seen:
                seen.add(ref)
                out.append(ref)
    return out


def load_book_codes() -> set[str]:
    """Hard-coded fallback if DB unavailable; otherwise pull from books table."""
    try:
        import sqlite3
        conn = sqlite3.connect("database/bible_research.db")
        codes = {r[0] for r in conn.execute("SELECT short_code FROM books").fetchall()}
        codes |= {r[0] for r in conn.execute("SELECT abbreviation FROM books").fetchall()}
        conn.close()
        return codes
    except Exception:
        return set()


def parse_analysis(path: str, book_codes: set[str]) -> dict:
    """Walk the analysis file, build a list of prompt-response records."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    records: list[dict] = []
    current_tier: str | None = None
    current_tier_title: str | None = None
    current_component: str | None = None
    current_component_title: str | None = None
    current_record: dict | None = None
    body_buf: list[str] = []

    def finalise_record():
        nonlocal current_record, body_buf
        if current_record is not None:
            body = "\n".join(body_buf).strip()
            current_record["body"] = body
            current_record["body_word_count"] = len(body.split())
            current_record["obs_refs"] = sorted(set(OBS_REF_RE.findall(body)))
            current_record["sd_refs"] = sorted(set(SD_REF_RE.findall(body)))
            current_record["dim_refs"] = sorted(set(DIM_REF_RE.findall(body)))
            current_record["strongs_refs"] = sorted(set(STRONGS_RE.findall(body)))
            current_record["group_refs"] = sorted(set(GROUP_CODE_RE.findall(body)))
            current_record["verse_refs"] = find_verse_refs(body, book_codes)
            # Inline notation hits in body (e.g. grace-pilot puts them in body
            # after the answer rather than on the Status line).
            inline_notations = INLINE_NOTATION_RE.findall(body)
            existing = set(current_record.get("notation") or [])
            for n in inline_notations:
                # Strip trailing period/short suffix
                norm = n.strip().rstrip(".").rstrip(":")
                # Normalise to canonical labels
                for canon in ("Consistent with prior analysis", "Adds structure", "New finding", "Gap identified"):
                    if norm.lower().startswith(canon.lower()[:12]):
                        existing.add(canon)
                        break
                else:
                    existing.add(norm)
            current_record["notation"] = sorted(existing)
            current_record["is_new_finding"] = "New finding" in existing
            current_record["is_gap"] = ("Gap identified" in existing) or current_record["status"] == "S"
            records.append(current_record)
        current_record = None
        body_buf = []

    i = 0
    while i < len(lines):
        line = lines[i]
        m = TIER_RE.match(line)
        if m:
            finalise_record()
            current_tier = m.group(1)
            current_tier_title = m.group(2).strip()
            i += 1
            continue
        m = COMPONENT_RE.match(line)
        if m:
            finalise_record()
            current_component = m.group(1)
            current_component_title = m.group(2).strip()
            i += 1
            continue
        m = PROMPT_RE.match(line)
        if m:
            finalise_record()
            current_record = {
                "tier": current_tier,
                "tier_title": current_tier_title,
                "component_code": current_component,
                "component_title": current_component_title,
                "prompt_seq": int(m.group(1)),
                "prompt_text": m.group(2).strip(),
                "status": None,
                "notation": [],
            }
            # Look ahead for the Status line within the next ~10 lines
            for j in range(i + 1, min(i + 12, len(lines))):
                sline = lines[j].strip()
                if not sline:
                    continue
                sm = STATUS_RE.match(sline)
                if sm:
                    current_record["status"] = sm.group(1)
                    if sm.group(2):
                        current_record["notation"].append(sm.group(2).strip())
                    i = j  # body starts after this
                    break
                # Fallback: catch lines like '**Status: S (inverted)**'
                fm = re.match(r"^\*\*Status:?\s*([APSN])\b", sline)
                if fm:
                    current_record["status"] = fm.group(1)
                    i = j
                    break
            i += 1
            body_buf = []
            continue
        if line.strip().startswith("---") and current_record is not None:
            # Treat horizontal rule as record terminator
            finalise_record()
            i += 1
            continue
        if current_record is not None:
            body_buf.append(line)
        i += 1
    # Catch final record
    finalise_record()
    return {
        "source_file": os.path.basename(path),
        "records": records,
    }


def parse_session_log(path: str) -> dict:
    """Extract consolidated lists from the session log.  Best-effort —
    section presence varies. Returns whatever was found."""
    if not os.path.exists(path):
        return {"present": False, "source_file": None}
    with open(path, encoding="utf-8") as f:
        c = f.read()

    out: dict = {
        "present": True,
        "source_file": os.path.basename(path),
        "status_summary": None,
        "new_findings": [],
        "gaps_complete_silence": [],
        "gaps_partial": [],
        "session_d_priority_gaps": [],
        "researcher_decisions": [],
        "session_d_implications": [],
    }

    # Title-based section finder — robust to varying number schemes.
    def find_section(title_pattern: str) -> str | None:
        """Return the text of a section whose H2 or H3 heading title matches."""
        m = re.search(rf"^(##+)\s+(?:\d+\.[\d.]*\s+)?({title_pattern})\b[^\n]*\n([\s\S]+?)(?=^\1\s|\Z)",
                      c, re.MULTILINE | re.IGNORECASE)
        return m.group(0) if m else None

    # Status summary table — anchored on the **TOTAL** row
    m = re.search(r"^##+\s+(?:\d+\.[\d.]*\s+)?(?:Analysis Results|Status Code Summary|Status Summary)\b[\s\S]+?\|\s*\*\*TOTAL\*\*\s*\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|[^|]+\|", c, re.MULTILINE)
    if m:
        out["status_summary"] = m.group(0).strip()

    # New findings list
    nf_block = find_section(r"(?:7\.2\s+)?New[ -]findings|Key Findings|Substantive Findings")
    if nf_block:
        items = re.findall(r"^\d+\.\s+(.+?)(?=^\d+\.\s+|^---|\Z)", nf_block, re.MULTILINE | re.DOTALL)
        out["new_findings"] = [it.strip().rstrip("-").strip() for it in items if it.strip()]

    # Gaps — by-title rather than by number
    silence_block = find_section(r"Complete[- ]silence|Silenced components|Tier-Wide Silences")
    if silence_block:
        for it in re.findall(r"^[-*]\s+\*\*(.+?)\*\*\s*[—:-]?\s*(.+?)$", silence_block, re.MULTILINE):
            out["gaps_complete_silence"].append({"label": it[0].strip(), "note": it[1].strip()})

    partial_block = find_section(r"Significant partial|Partial gaps|Substantive Partial Gaps")
    if partial_block:
        for it in re.findall(r"^[-*]\s+\*\*(.+?)\*\*\s*[—:-]?\s*(.+?)$", partial_block, re.MULTILINE):
            out["gaps_partial"].append({"label": it[0].strip(), "note": it[1].strip()})

    sdpri_block = find_section(r"Session D priority|Session-D priority|Session D Implications|Session D priorities")
    if sdpri_block:
        for it in re.findall(r"^[-*]\s+(.+?)\(([A-Z0-9-]+)\)\s*$", sdpri_block, re.MULTILINE):
            out["session_d_priority_gaps"].append({"label": it[0].strip().rstrip(' -—'), "ref": it[1].strip()})
        if not out["session_d_priority_gaps"]:
            for line in sdpri_block.split("\n"):
                line = line.strip()
                if line.startswith(("- ", "* ")):
                    out["session_d_priority_gaps"].append({"label": line.lstrip("-* ").strip(), "ref": None})

    # RESEARCHER_DECISION items
    rd_block = find_section(r"RESEARCHER_DECISION|Researcher Decision")
    if rd_block:
        if re.search(r"\bno new RESEARCHER_DECISION\b|\bnone new\b|\bno RESEARCHER_DECISION\b", rd_block, re.IGNORECASE):
            out["researcher_decisions"].append("(none new this session)")
        for m in re.finditer(r"RESEARCHER_DECISION-\d+[^\n]*?(?=\.|\n|$)", rd_block):
            entry = m.group(0).strip().rstrip(".")
            if entry and entry not in out["researcher_decisions"]:
                out["researcher_decisions"].append(entry)

    # Session D implications — sub-section under Next Steps
    next_steps = find_section(r"Next Steps|Next steps")
    if next_steps:
        impl = re.search(r"###?\s+(?:[\d.]+\s+)?(?:Session[- ]D Implications|Session D implications)[\s\S]+?(?=^###?\s|\Z|^##\s)", next_steps, re.MULTILINE | re.IGNORECASE)
        if impl:
            for line in impl.group(0).split("\n"):
                sl = line.strip()
                if sl.startswith(("- ", "* ")):
                    out["session_d_implications"].append(sl.lstrip("-* "))

    return out


def render_markdown_summary(word_no: str, word_label: str, parsed: dict, session: dict) -> str:
    parts: list[str] = []
    P = parts.append
    records = parsed["records"]
    # Counts
    n = len(records)
    by_status = {s: 0 for s in "APSN"}
    n_new = 0
    n_gap = 0
    n_consistent = 0
    n_struct = 0
    obs_set = set()
    sd_set = set()
    word_counts = []
    for r in records:
        if r["status"] in by_status:
            by_status[r["status"]] += 1
        if r["is_new_finding"]:
            n_new += 1
        if r["is_gap"]:
            n_gap += 1
        if "Consistent with prior analysis" in (r["notation"] or []):
            n_consistent += 1
        if "Adds structure" in (r["notation"] or []):
            n_struct += 1
        obs_set.update(r["obs_refs"] or [])
        sd_set.update(r["sd_refs"] or [])
        word_counts.append(r["body_word_count"])
    total_words = sum(word_counts)

    P(f"# {word_label} ({word_no}) — Capture Preview\n")
    P(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    P(f"**Source analysis file:** `{parsed['source_file']}`")
    if session.get("present"):
        P(f"**Source session log:**     `{session['source_file']}`")
    P(f"\n**Read-only preview** — nothing written to the database.  Validate the captures below before approving DB writes.\n")

    P("## 1. Headline counts\n")
    P(f"- Prompts parsed: **{n}**")
    P(f"- Status distribution: A={by_status['A']} · P={by_status['P']} · S={by_status['S']} · N={by_status['N']}")
    P(f"- 'New finding' notation: **{n_new}** prompts")
    P(f"- 'Gap identified' or Silent: **{n_gap}** prompts")
    P(f"- 'Consistent with prior': {n_consistent}  ·  'Adds structure': {n_struct}")
    P(f"- Distinct OBS refs in bodies: {len(obs_set)}")
    P(f"- Distinct SD/SP refs in bodies: {len(sd_set)}")
    P(f"- Total body word count: {total_words:,}\n")

    if session.get("present"):
        P("## 2. From session log\n")
        if session["status_summary"]:
            P("### 2.1 Status summary table (verbatim)\n")
            P("```")
            P(session["status_summary"])
            P("```\n")
        if session["new_findings"]:
            P(f"### 2.2 New findings ({len(session['new_findings'])} listed in §7.2)\n")
            for i, nf in enumerate(session["new_findings"], 1):
                trimmed = nf.split("\n")[0][:240]
                P(f"{i}. {trimmed}")
            P("")
        if session["gaps_complete_silence"]:
            P(f"### 2.3 Complete-silence gaps ({len(session['gaps_complete_silence'])} from §8.1)\n")
            for g in session["gaps_complete_silence"]:
                P(f"- **{g['label']}** — {g['note'][:200]}")
            P("")
        if session["gaps_partial"]:
            P(f"### 2.4 Partial gaps ({len(session['gaps_partial'])} from §8.2)\n")
            for g in session["gaps_partial"]:
                P(f"- **{g['label']}** — {g['note'][:200]}")
            P("")
        if session["session_d_priority_gaps"]:
            P(f"### 2.5 Session D priority gaps ({len(session['session_d_priority_gaps'])} from §8.3)\n")
            for g in session["session_d_priority_gaps"]:
                ref = f" *(ref {g['ref']})*" if g.get("ref") else ""
                P(f"- {g['label']}{ref}")
            P("")
        if session["researcher_decisions"]:
            P(f"### 2.6 RESEARCHER_DECISION items ({len(session['researcher_decisions'])} from §9)\n")
            for rd in session["researcher_decisions"]:
                P(f"- {rd[:240]}")
            P("")
        if session["session_d_implications"]:
            P(f"### 2.7 Session D implications ({len(session['session_d_implications'])} from §11)\n")
            for imp in session["session_d_implications"]:
                P(f"- {imp[:240]}")
            P("")

    # 3. Per-tier prompt audit
    P("## 3. Per-tier prompt audit\n")
    P("Concise per-prompt status table.  See `parsed-capture-preview.json` for the full body text.\n")
    by_tier_records: dict[str, list[dict]] = {}
    for r in records:
        by_tier_records.setdefault(r["tier"] or "?", []).append(r)
    for tier_code in sorted(by_tier_records):
        rs = by_tier_records[tier_code]
        tier_title = rs[0]["tier_title"] if rs else ""
        cnt_a = sum(1 for x in rs if x["status"] == "A")
        cnt_p = sum(1 for x in rs if x["status"] == "P")
        cnt_s = sum(1 for x in rs if x["status"] == "S")
        cnt_n = sum(1 for x in rs if x["status"] == "N")
        cnt_new = sum(1 for x in rs if x["is_new_finding"])
        cnt_gap = sum(1 for x in rs if x["is_gap"])
        P(f"\n### {tier_code} — {tier_title}  ({len(rs)} prompts: A={cnt_a} P={cnt_p} S={cnt_s} N={cnt_n} · new={cnt_new} gap={cnt_gap})\n")
        P("| Component | Prompt | Status | Notation | Body words | OBS refs | SD/SP refs |")
        P("| --- | ---: | :---: | --- | ---: | --- | --- |")
        for r in rs:
            notations = ", ".join(r["notation"] or []) or "—"
            obs_str = ", ".join((r["obs_refs"] or [])[:3])
            sd_str = ", ".join((r["sd_refs"] or [])[:3])
            P(f"| {r['component_code']} {r['component_title']} | {r['prompt_seq']} | {r['status'] or '?'} | {notations} | {r['body_word_count']} | {obs_str} | {sd_str} |")
    P("\n## 4. Capture-target proposal\n")
    P("If approved for DB capture, the parsed material would land as follows:\n")
    P("| Source | Target | Count (this file) |")
    P("| --- | --- | ---: |")
    P(f"| Per-prompt response (status A/P/S/N + body) | `wa_finding_catalogue_links` linking new (or stub) finding to v2 catalogue question | {n} |")
    P(f"| 'New finding' marked prompts | `wa_session_b_findings` (finding_type='OBSERVATION', author='claude_ai', session_b_instruction='WA-second-tier-analysis-instruction-v1-2026-04-30.md') | {n_new} |")
    if session.get("present"):
        P(f"| Session-log §7.2 numbered new findings | Same target as above (deduplicated against per-prompt) | {len(session['new_findings'])} |")
        P(f"| Session-log §8.1 complete-silence gaps | `wa_session_research_flags` (flag_code='SB_FINDING', priority=MEDIUM) | {len(session['gaps_complete_silence'])} |")
        P(f"| Session-log §8.2 partial gaps | `wa_session_research_flags` (flag_code='SB_FINDING') | {len(session['gaps_partial'])} |")
        P(f"| Session-log §11 Session-D implications | `wa_session_research_flags` (flag_code='SD_POINTER') | {len(session['session_d_implications'])} |")
        P(f"| Session-log §9 RESEARCHER_DECISION | `wa_session_research_flags` (need new flag_code? candidate: 'RESEARCHER_DECISION') | {len(session['researcher_decisions'])} |")
    P(f"\n**OBS-NNN-NNN refs encountered ({len(obs_set)}):** these are *references* to prior findings, not new ones — captured as cross-references where useful.")
    P(f"**DIM/SD-NNN refs encountered ({len(sd_set)}):** these are *references* to existing SD pointers in `wa_session_research_flags` — verified live before any DB write.")
    return "\n".join(parts)


def detect_word(folder_name: str) -> tuple[str, str] | None:
    m = re.match(r"[Rr]?(\d{2,3})[ \-_]?([A-Za-z]+)", folder_name)
    if m:
        return (f"R{int(m.group(1)):03d}", m.group(2).lower())
    return None


def find_analysis_file(folder_path: str) -> str | None:
    for f in os.listdir(folder_path):
        if "session-log" in f:
            continue  # excluded — handled by find_session_log
        if (f.startswith("WA-R") and "second-tier-analysis" in f) or "prompt-test-v1" in f:
            return os.path.join(folder_path, f)
    return None


def find_session_log(folder_path: str) -> str | None:
    for f in os.listdir(folder_path):
        if f.startswith("WA-session-log") and "second-tier" in f:
            return os.path.join(folder_path, f)
    return None


def main() -> int:
    book_codes = load_book_codes()
    summary_lines = [
        "# Capture Preview — Index\n",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"**Bundle dir:** `{BUNDLE_DIR}`",
        "",
        "Read-only parsing of AI second-tier analysis output.  No DB writes.  Validate the per-word `parsed-capture-preview.md` files before approving capture.\n",
        "## Per-word output\n",
        "| Word | Folder | Analysis file | Session log | Prompts | A/P/S/N | New | Gap |",
        "| --- | --- | --- | --- | ---: | --- | ---: | ---: |",
    ]

    for entry in sorted(os.listdir(BUNDLE_DIR)):
        path = os.path.join(BUNDLE_DIR, entry)
        if not os.path.isdir(path):
            continue
        det = detect_word(entry)
        if not det:
            continue
        word_no, word_lc = det
        analysis_path = find_analysis_file(path)
        if not analysis_path:
            print(f"[skip] {entry}: no analysis file found")
            continue
        session_path = find_session_log(path)

        parsed = parse_analysis(analysis_path, book_codes)
        session = parse_session_log(session_path) if session_path else {"present": False}

        # Write JSON
        out_json = os.path.join(path, "parsed-capture-preview.json")
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump({"meta": {
                "registry_no": word_no,
                "word": word_lc,
                "parsed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "analysis_file": parsed["source_file"],
                "session_log_file": session.get("source_file"),
            }, "analysis": parsed, "session_log": session}, f, indent=2, ensure_ascii=False)

        # Write MD
        md = render_markdown_summary(word_no, word_lc.title(), parsed, session)
        out_md = os.path.join(path, "parsed-capture-preview.md")
        with open(out_md, "w", encoding="utf-8") as f:
            f.write(md)

        # Index row
        records = parsed["records"]
        by_st = {s: sum(1 for r in records if r["status"] == s) for s in "APSN"}
        n_new = sum(1 for r in records if r["is_new_finding"])
        n_gap = sum(1 for r in records if r["is_gap"])
        st_str = f"A={by_st['A']} P={by_st['P']} S={by_st['S']} N={by_st['N']}"
        summary_lines.append(
            f"| {word_no} {word_lc} | {entry} | "
            f"[{os.path.basename(analysis_path)}]({entry}/{os.path.basename(analysis_path)}) | "
            f"{('[' + os.path.basename(session_path) + '](' + entry + '/' + os.path.basename(session_path) + ')') if session_path else '_(none)_'} | "
            f"{len(records)} | {st_str} | {n_new} | {n_gap} |"
        )
        print(f"  {word_no} {word_lc}: {len(records)} prompts parsed -> "
              f"{os.path.relpath(out_md)} (+ .json)")

    summary_lines.append("\n## Capture-target proposal\n")
    summary_lines.append("Each per-word file's §4 enumerates the proposed DB targets and counts.  No writes occur until the researcher approves a follow-up apply script.")
    summary_lines.append("")
    summary_lines.append("**Proposed targets:**")
    summary_lines.append("- Per-prompt response → `wa_finding_catalogue_links` linking finding ↔ v2 catalogue question (coverage = full/partial/no_finding/not_applicable from A/P/S/N)")
    summary_lines.append("- New finding (per-prompt or session-log §7.2) → `wa_session_b_findings` (finding_type='OBSERVATION', author='claude_ai', session_b_instruction='WA-second-tier-analysis-instruction-v1-2026-04-30.md')")
    summary_lines.append("- Complete-silence + partial gaps (§8.1, §8.2) → `wa_session_research_flags` (flag_code='SB_FINDING')")
    summary_lines.append("- Session D implications (§11) → `wa_session_research_flags` (flag_code='SD_POINTER')")
    summary_lines.append("- RESEARCHER_DECISION items (§9) → `wa_session_research_flags` (proposed new flag_code 'RESEARCHER_DECISION'; awaits researcher approval)")

    index_path = os.path.join(BUNDLE_DIR, "capture-preview-index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))
    print(f"\nIndex: {index_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
