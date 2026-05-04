"""_tmp_check_v17_stage2b.py

Verify Stage 2b completeness for the 5 v1.7-style words by parsing the
original AI second-tier-analysis output files directly.
"""
from __future__ import annotations

import os
import re

WORDS = {23: "compassion", 30: "contrition", 62: "fellowship", 64: "forgiveness", 68: "grace"}

# Match the original AI analysis files (NOT instruction docs or session logs).
ANALYSIS_PATTERNS = [
    re.compile(r"^WA-R(\d{3})-second-tier-analysis-v\d.*\.md$", re.IGNORECASE),
    re.compile(r"^WA-grace-prompt-test-v\d.*\.md$", re.IGNORECASE),  # R068's pilot file
]

QA_HEADER = re.compile(r"^\*\*Q&A-\d+\s*\|\s*(\S+?)\*\*\s*$", re.MULTILINE)
STATUS_LINE = re.compile(r"^\*\*Status:?\s*([APSN])\b", re.MULTILINE)


def find_analysis_file(folder: str, registry_no: int) -> str | None:
    if not os.path.exists(folder):
        return None
    for f in os.listdir(folder):
        for pat in ANALYSIS_PATTERNS:
            m = pat.match(f)
            if m:
                # If pattern captures the registry, verify
                if m.groups() and int(m.group(1)) != registry_no:
                    continue
                return os.path.join(folder, f)
    return None


def parse_qa_blocks(path: str) -> dict:
    """Parse a v1.7-style second-tier-analysis file. Format:
       ### T0.1 — Divine Nature Reflected   (component header)
       **Prompt 1:** ...                     (prompt)
       **Status: A** | *notation*            (status)

       Walk components → prompts → status, keyed by tier_prompt_code.
    """
    with open(path, encoding="utf-8") as f:
        c = f.read()

    counts = {"A": 0, "P": 0, "S": 0, "N": 0}
    codes_seen: set[str] = set()
    statuses_per_code: dict[str, str] = {}

    component_re = re.compile(r"^### (T\d\.\d+)\b", re.MULTILINE)
    prompt_re = re.compile(r"^\*\*Prompt (\d+):", re.MULTILINE)
    status_re = re.compile(r"^\*\*Status:?\s*([APSN])\b", re.MULTILINE)

    # Build a position-based walk: for each component, find prompts and their statuses
    # Approach: split on component headers, then within each component split on prompt headers
    # then find status within prompt's body region.

    # Find component starts
    comp_matches = list(component_re.finditer(c))
    if not comp_matches:
        return {"path": path, "qa_count": 0, "by_status": counts, "codes_seen": codes_seen,
                "statuses": statuses_per_code, "format": "unknown"}

    for i, cm in enumerate(comp_matches):
        comp_code = cm.group(1)  # e.g. T0.1
        comp_start = cm.end()
        comp_end = comp_matches[i + 1].start() if i + 1 < len(comp_matches) else len(c)
        comp_block = c[comp_start:comp_end]

        # Find prompts within this component
        prompt_matches = list(prompt_re.finditer(comp_block))
        for j, pm in enumerate(prompt_matches):
            pseq = int(pm.group(1))
            full_code = f"{comp_code}.{pseq}"
            codes_seen.add(full_code)
            p_start = pm.end()
            p_end = prompt_matches[j + 1].start() if j + 1 < len(prompt_matches) else len(comp_block)
            p_block = comp_block[p_start:p_end]
            sm = status_re.search(p_block)
            if sm:
                status = sm.group(1)
                counts[status] += 1
                statuses_per_code[full_code] = status

    return {
        "path": path,
        "qa_count": len(codes_seen),
        "by_status": counts,
        "codes_seen": codes_seen,
        "statuses": statuses_per_code,
        "format": "v1.7",
    }


def main() -> int:
    print("=== Stage 2b completeness audit — 5 v1.7-style words ===\n")
    print("Source: original AI second-tier-analysis output files in each word's prior/ folder.")
    print(f"Target: 189 v2 catalogue prompts (T0-T7) all dispositioned.\n")

    print(f'{"Reg":>4s} {"word":13s} {"A":>4s} {"P":>4s} {"S":>4s} {"N":>4s} {"total":>6s} {"verdict":25s}')

    for no, word in WORDS.items():
        base = os.path.join("Sessions", "Session_B", "words", f"{no:03d}_{word}", "prior")
        path = find_analysis_file(base, no)
        if not path:
            print(f"  R{no:03d} {word:13s} <no analysis file found in {base}>")
            continue

        result = parse_qa_blocks(path)
        c = result["by_status"]
        total = result["qa_count"]
        if total >= 189:
            verdict = "COMPLETE"
        elif total > 0:
            verdict = f"PARTIAL ({189-total} short of 189)"
        else:
            verdict = "EMPTY (parse fail or 0 markers)"

        print(f'  R{no:03d} {word:13s} {c["A"]:>4d} {c["P"]:>4d} {c["S"]:>4d} {c["N"]:>4d} {total:>6d} {verdict:25s}')
        print(f'         file: {os.path.basename(path)}')


if __name__ == "__main__":
    main()
