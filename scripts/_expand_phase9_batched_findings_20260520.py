"""Expand batched-header Phase 9 findings into parser-safe per-prompt form.

Researcher direction 2026-05-20: M07 Bundle B's chars 2-6 used a
batched-header format (e.g. `**T2.3.1 through T2.3.3 — Heart location**`)
with one combined finding for multiple prompts. The batching is
intentional — Session C consolidates detail later — but the per-batch
loader needs one **[CHAR-N]** block per prompt.

This script reads a batched findings file and rewrites it to
parser-safe form: for each `T#.#.# through T#.#.#` header, emit N
separate blocks (one per prompt in the range) with the same finding
text duplicated. Single-prompt headers pass through unchanged.

Usage:
    python scripts/_expand_phase9_batched_findings_20260520.py \\
        --in  "path/to/batched-findings.md" \\
        --out "path/to/expanded-findings.md" \\
        --char-seq N
"""
from __future__ import annotations

import argparse
import re
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from pathlib import Path

# Match either:
#   **T0.1.1**
#   **T0.1.1 — text...**
#   **T2.3.1 through T2.3.3 — Heart location**
SINGLE_RE = re.compile(r'^\*\*(T\d+\.\d+\.\d+)\*\*\s*$')
SINGLE_DESC_RE = re.compile(r'^\*\*(T\d+\.\d+\.\d+)\s*(?:—|--)\s*(.*?)\*\*\s*$')
RANGE_RE = re.compile(r'^\*\*(T\d+\.\d+\.\d+)\s+through\s+(T\d+\.\d+\.\d+)(?:\s*(?:—|--)\s*(.*?))?\*\*\s*$')


def expand_range(start_code: str, end_code: str) -> list[str]:
    """Return list of prompt codes from start_code to end_code inclusive,
    iterating only on the last segment (T-prefix and middle must match).
    """
    s_parts = start_code.split('.')
    e_parts = end_code.split('.')
    if len(s_parts) != 3 or len(e_parts) != 3:
        raise ValueError(f"Bad code format: {start_code} / {end_code}")
    if s_parts[0] != e_parts[0] or s_parts[1] != e_parts[1]:
        raise ValueError(f"Range crosses components: {start_code} / {end_code}")
    s_n = int(s_parts[2])
    e_n = int(e_parts[2])
    if e_n < s_n:
        raise ValueError(f"Range goes backwards: {start_code} / {end_code}")
    return [f"{s_parts[0]}.{s_parts[1]}.{n}" for n in range(s_n, e_n + 1)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='in_path', required=True, type=Path)
    ap.add_argument('--out', required=True, type=Path)
    ap.add_argument('--char-seq', type=int, required=True)
    args = ap.parse_args()

    text = args.in_path.read_text(encoding='utf-8')
    lines = text.splitlines()

    out_lines = []
    i = 0
    n = len(lines)
    single_blocks_passed = 0
    expanded_blocks = 0
    expanded_prompts = 0

    while i < n:
        line = lines[i]
        # Try to match a prompt header
        m_range = RANGE_RE.match(line)
        m_single_desc = SINGLE_DESC_RE.match(line)
        m_single = SINGLE_RE.match(line)

        if m_range:
            start_code, end_code = m_range.group(1), m_range.group(2)
            label = (m_range.group(3) or '').strip() or '(no label)'
            prompts = expand_range(start_code, end_code)
            expanded_blocks += 1
            expanded_prompts += len(prompts)

            # Collect the block body — from the next line until the next prompt header or `---` separator
            body_lines = []
            j = i + 1
            while j < n:
                next_line = lines[j]
                if (RANGE_RE.match(next_line) or SINGLE_DESC_RE.match(next_line)
                        or SINGLE_RE.match(next_line) or next_line.startswith('## ')):
                    break
                body_lines.append(next_line)
                j += 1

            # Emit one block per prompt code with the same body
            for code in prompts:
                out_lines.append(f"**{code} — (expanded from '{start_code} through {end_code} — {label}')**")
                out_lines.extend(body_lines)
                # Ensure --- separator at end of block if not already
                if not body_lines or not body_lines[-1].strip().startswith('---'):
                    if body_lines and body_lines[-1].strip() == '':
                        # already has trailing blank; just need ---
                        out_lines.append('---')
                        out_lines.append('')
                    else:
                        out_lines.append('')
                        out_lines.append('---')
                        out_lines.append('')

            i = j
            continue

        elif m_single_desc:
            single_blocks_passed += 1
            out_lines.append(line)
            i += 1
            continue

        elif m_single:
            # Convert `**T0.1.1**` to parser-safe `**T0.1.1 — (no inline label)**`
            code = m_single.group(1)
            single_blocks_passed += 1
            out_lines.append(f"**{code} — (no inline label)**")
            i += 1
            continue

        else:
            # Pass-through line
            out_lines.append(line)
            i += 1

    out_text = "\n".join(out_lines) + ("\n" if not out_lines or out_lines[-1] != '' else '')
    args.out.write_text(out_text, encoding='utf-8')

    # Stats
    PROMPT_HEADER_RE = re.compile(r'^\*\*(T\d+\.\d+\.\d+) —', re.MULTILINE)
    final_count = len(PROMPT_HEADER_RE.findall(out_text))
    print(f"  Single-prompt headers passed through: {single_blocks_passed}")
    print(f"  Batched blocks expanded: {expanded_blocks}")
    print(f"  Prompts produced from batched expansion: {expanded_prompts}")
    print(f"  Final parser-safe prompt headers: {final_count}")
    print(f"  Wrote {args.out}")


if __name__ == '__main__':
    main()
