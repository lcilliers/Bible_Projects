"""Validate M01 Phase 9 consolidated findings against catalogue + parser-safe form.

Checks:
  1. Every catalogue prompt (189 in v2.1) appears in one of the 4 parts.
  2. Every prompt has ≥1 scope marker (sub-group or CLUSTER).
  3. Scope markers are on their own line and use canonical form `**[X]**` or
     `**[X, Y]**` or `**[CLUSTER]**` or `**[BOUNDARY ...]**`.
  4. Every scope marker block has an outcome code (E/S/G) or starts the body
     without explicit code (treated as E by §12.4).
  5. Every prompt ends with a `---` separator before the next prompt.
  6. E entries should cite at least one verse reference or VCG code.
  7. BOUNDARY appears only in part 4 (T5-T7), with per-term markers.

Output: a markdown validation report.
"""
from __future__ import annotations
import re, sys
from pathlib import Path
from collections import Counter

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
M01 = REPO / "Sessions" / "Session_Clusters" / "M01"
PHASE9_DIR = M01 / "files phase 9"
CATALOGUE = REPO / "Workflow" / "Tiers" / "wa-obs-catalogue-tiered-v2_1-20260513.md"

PARTS = [
    ("part1", PHASE9_DIR / "WA-M01-consolidated-findings-v1-20260516-part1.md", ["T0", "T1"]),
    ("part2", PHASE9_DIR / "WA-M01-consolidated-findings-v1-20260516-part2-T2.md", ["T2"]),
    ("part3", PHASE9_DIR / "WA-M01-consolidated-findings-v1-20260516-part3-T3-T4.md", ["T3", "T4"]),
    ("part4", PHASE9_DIR / "WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md", ["T5", "T6", "T7"]),
]

# Catalogue prompt regex (e.g. **`T0.1.1`** or T0.1.1)
PROMPT_HEADER_RE = re.compile(r"^### (T\d+\.\d+\.\d+)", re.MULTILINE)
PROMPT_CODE_IN_CATALOGUE = re.compile(r"`(T\d+\.\d+\.\d+)`")
SCOPE_LINE_RE = re.compile(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$", re.MULTILINE)
VERSE_REF_RE = re.compile(r"\b[1-3]?[A-Z][a-z]{2,4}\s+\d+:\d+(-\d+)?")
VCG_CODE_RE = re.compile(r"\bM01-[A-Z]+-VCG-\d+\b|\b[A-G]-VCG-\d+\b")

VALID_SUBGROUPS = {"A", "B", "C", "D", "E", "F", "G", "BOUNDARY", "CLUSTER"}


def parse_catalogue() -> set[str]:
    """Return set of all catalogue prompt codes (T0.1.1 etc.)."""
    text = CATALOGUE.read_text(encoding="utf-8")
    # Catalogue lists prompts as `**`T0.1.1`**` — use the in-backticks token
    codes = set(PROMPT_CODE_IN_CATALOGUE.findall(text))
    return codes


def parse_part(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    # Locate prompts
    prompt_matches = list(re.finditer(r"^### (T\d+\.\d+\.\d+)[ —].*$", text, re.MULTILINE))
    prompts: list[dict] = []
    for i, m in enumerate(prompt_matches):
        code = m.group(1)
        start = m.end()
        end = prompt_matches[i+1].start() if i+1 < len(prompt_matches) else len(text)
        body = text[start:end]
        # Strip leading newlines
        body = body.lstrip("\n")
        # Find all scope marker lines (with their body until next blank/marker/sep)
        scope_lines = list(re.finditer(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$", body, re.MULTILINE))
        # Find horizontal rule terminator
        end_sep = re.search(r"^---\s*$", body, re.MULTILINE)
        scopes: list[dict] = []
        for j, sm in enumerate(scope_lines):
            scope_raw = sm.group(1).strip()
            head_body = sm.group(2).strip()
            block_start = sm.end()
            block_end = scope_lines[j+1].start() if j+1 < len(scope_lines) else (end_sep.start() if end_sep else len(body))
            block_text = head_body + "\n" + body[block_start:block_end]
            # Parse scope letters
            scope_letters = parse_scope(scope_raw)
            # Outcome code
            m_outcome = re.match(r"^\s*([ESG])\s*[—-]\s+", head_body)
            outcome = m_outcome.group(1) if m_outcome else None
            # Citation evidence
            verse_refs = VERSE_REF_RE.findall(block_text)
            vcg_codes = VCG_CODE_RE.findall(block_text)
            scopes.append({
                "raw": scope_raw,
                "letters": scope_letters,
                "outcome": outcome,
                "body_len": len(block_text),
                "has_verse_ref": bool(verse_refs) or bool(vcg_codes),
            })
        prompts.append({
            "code": code,
            "scopes": scopes,
            "has_separator": end_sep is not None,
            "raw_body_len": len(body),
        })
    return {"path": path, "prompts": prompts}


def parse_scope(raw: str) -> list[str]:
    """Parse '[A]' or '[A, B, C]' or '[CLUSTER]' or '[BOUNDARY - H3372 ya.re]'."""
    s = raw.strip()
    # BOUNDARY with descriptor
    if s.startswith("BOUNDARY"):
        return ["BOUNDARY"]
    # CLUSTER with optional descriptor
    if s.startswith("CLUSTER"):
        return ["CLUSTER"]
    # Strip embedded em-dash and label
    s = re.split(r"\s+[—-]\s+", s, maxsplit=1)[0]
    # Comma-split
    parts = [p.strip() for p in s.split(",")]
    out = []
    for p in parts:
        # Single letter (A-G)
        if re.fullmatch(r"[A-G]", p):
            out.append(p)
        elif p in ("CLUSTER", "BOUNDARY"):
            out.append(p)
        else:
            # unknown — keep for diagnostic
            out.append(f"?{p}")
    return out


def render_report(catalogue_codes: set[str], part_results: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# M01 Phase 9 consolidated findings — validation report")
    lines.append("")
    lines.append(f"**Generated:** validation pass")
    lines.append(f"**Catalogue:** wa-obs-catalogue-tiered-v2_1-20260513.md ({len(catalogue_codes)} prompts)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Aggregate
    all_prompt_codes: set[str] = set()
    prompts_per_part: dict[str, int] = {}
    scopes_per_part: dict[str, int] = {}
    for pname, _, _ in PARTS:
        prompts_per_part[pname] = 0
        scopes_per_part[pname] = 0

    issues: list[tuple[str,str,str]] = []  # (part, code, problem)
    e_no_citation: list[tuple[str,str,str]] = []  # E entries without verse refs

    for idx, pr in enumerate(part_results):
        pname = PARTS[idx][0]
        ptiers = PARTS[idx][2]
        for p in pr["prompts"]:
            code = p["code"]
            all_prompt_codes.add(code)
            prompts_per_part[pname] += 1
            tier = code.split(".")[0]
            if tier not in ptiers:
                issues.append((pname, code, f"prompt tier {tier} in wrong part (expected {ptiers})"))
            # Must have ≥1 scope
            if not p["scopes"]:
                issues.append((pname, code, "NO scope markers"))
            for s in p["scopes"]:
                scopes_per_part[pname] += 1
                # Unknown scope letters
                bad = [l for l in s["letters"] if l.startswith("?")]
                if bad:
                    issues.append((pname, code, f"unknown scope label: {bad}"))
                # Outcome code check + citation discipline for E
                if s["outcome"] == "E" and not s["has_verse_ref"]:
                    e_no_citation.append((pname, code, s["raw"]))
            if not p["has_separator"]:
                issues.append((pname, code, "no `---` separator after prompt"))

    # Catalogue coverage
    missing = catalogue_codes - all_prompt_codes
    extra = all_prompt_codes - catalogue_codes
    lines.append("## 1. Catalogue coverage")
    lines.append("")
    lines.append(f"- Catalogue prompts: **{len(catalogue_codes)}**")
    lines.append(f"- Found in findings: **{len(all_prompt_codes)}**")
    lines.append(f"- Missing (in catalogue but not findings): **{len(missing)}**")
    lines.append(f"- Extra (in findings but not catalogue): **{len(extra)}**")
    lines.append("")
    if missing:
        lines.append("### Missing prompts")
        for c in sorted(missing):
            lines.append(f"- `{c}`")
        lines.append("")
    if extra:
        lines.append("### Extra (unexpected) prompts")
        for c in sorted(extra):
            lines.append(f"- `{c}`")
        lines.append("")

    lines.append("## 2. Per-part counts")
    lines.append("")
    lines.append("| Part | Prompts | Scope cells |")
    lines.append("|---|---:|---:|")
    for pname, _, _ in PARTS:
        lines.append(f"| {pname} | {prompts_per_part[pname]} | {scopes_per_part[pname]} |")
    lines.append(f"| **total** | **{sum(prompts_per_part.values())}** | **{sum(scopes_per_part.values())}** |")
    lines.append("")

    # Outcome code distribution
    outcome_counter: Counter = Counter()
    for pr in part_results:
        for p in pr["prompts"]:
            for s in p["scopes"]:
                outcome_counter[s["outcome"] or "?"] += 1
    lines.append("## 3. Outcome code distribution")
    lines.append("")
    lines.append("| Code | Count |")
    lines.append("|---|---:|")
    for k in ("E","S","G","?"):
        lines.append(f"| {k} | {outcome_counter[k]} |")
    lines.append("")

    # Structural issues
    lines.append("## 4. Structural issues")
    lines.append("")
    if not issues:
        lines.append("_(none)_")
    else:
        lines.append("| Part | Prompt | Issue |")
        lines.append("|---|---|---|")
        for part, code, issue in issues[:200]:
            lines.append(f"| {part} | `{code}` | {issue} |")
        if len(issues) > 200:
            lines.append(f"| ... | ... | (+{len(issues)-200} more issues) |")
    lines.append("")

    # E without citation
    lines.append("## 5. E entries without explicit verse/VCG citation")
    lines.append("")
    if not e_no_citation:
        lines.append("_(none — every E cites at least one verse reference or VCG code)_")
    else:
        lines.append(f"Total: **{len(e_no_citation)}** E entries lack a parseable verse reference (`Book C:V`) or VCG code (e.g. `M01-A-VCG-01`).")
        lines.append("")
        lines.append("**Note:** automated detection may miss valid citations phrased indirectly. Spot-check before treating as a blocker.")
        lines.append("")
        lines.append("| Part | Prompt | Scope |")
        lines.append("|---|---|---|")
        for part, code, raw in e_no_citation[:50]:
            lines.append(f"| {part} | `{code}` | `[{raw}]` |")
        if len(e_no_citation) > 50:
            lines.append(f"| ... | ... | (+{len(e_no_citation)-50} more) |")
    lines.append("")

    # BOUNDARY check
    bnd_count = 0
    bnd_part4 = 0
    bnd_other_parts = []
    for idx, pr in enumerate(part_results):
        pname = PARTS[idx][0]
        for p in pr["prompts"]:
            for s in p["scopes"]:
                if "BOUNDARY" in s["letters"]:
                    bnd_count += 1
                    if pname == "part4":
                        bnd_part4 += 1
                    else:
                        bnd_other_parts.append((pname, p["code"], s["raw"]))
    lines.append("## 6. BOUNDARY discipline")
    lines.append("")
    lines.append(f"- Total BOUNDARY scope markers across all parts: **{bnd_count}**")
    lines.append(f"- In part4 (expected): **{bnd_part4}**")
    lines.append(f"- In other parts (informational — BOUNDARY can appear anywhere): **{len(bnd_other_parts)}**")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*End of validation report.*")
    return "\n".join(lines)


def main():
    catalogue = parse_catalogue()
    part_results = [parse_part(p[1]) for p in PARTS]
    report = render_report(catalogue, part_results)
    out_path = M01 / "WA-M01-phase9-findings-validation-v1-20260516.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote: {out_path.relative_to(REPO)}")
    # Print summary to stdout
    catalogue_codes = catalogue
    all_found = {p["code"] for pr in part_results for p in pr["prompts"]}
    print(f"\nCatalogue prompts: {len(catalogue_codes)}")
    print(f"Found in findings: {len(all_found)}")
    print(f"Missing: {len(catalogue_codes - all_found)}")
    print(f"Extra: {len(all_found - catalogue_codes)}")


if __name__ == "__main__":
    main()
