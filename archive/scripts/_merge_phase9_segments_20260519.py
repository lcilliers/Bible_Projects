"""Merge N tier-pair segments of a Phase 9 characteristic findings file
into a single canonical file.

Usage:
    python scripts/_merge_phase9_segments_20260519.py \
        --char-seq 7 --short-name Suffering-Joy \
        --seg-dir "Sessions/Session_Clusters/M04/files phase 9 gladness" \
        [--expected-prompts 189]

Segments are matched by glob:
    WA-M04-phase9-char{seq}-{short_name}-findings-seg*-v1-{date}.md

Output (canonical):
    Sessions/Session_Clusters/M04/WA-M04-phase9-char{seq}-{short_name}-findings-v1-{date}.md

Per-segment headers (everything before the first prompt block) are
stripped. A unified header is prepended.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PROMPT_HEADER_RE = re.compile(r'^\*\*T\d+\.\d+\.\d+ —', re.MULTILINE)
SEG_NUM_RE = re.compile(r'-seg(\d+)-')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cluster-code', default='M04')
    ap.add_argument('--char-seq', type=int, required=True)
    ap.add_argument('--short-name', required=True,
                    help='Short name as it appears in filenames (e.g. "Suffering-Joy")')
    ap.add_argument('--seg-dir', required=True, type=Path,
                    help='Directory holding the segment files')
    ap.add_argument('--out-dir', type=Path, default=Path('Sessions/Session_Clusters/M04'),
                    help='Where to write the merged canonical file')
    ap.add_argument('--expected-prompts', type=int, default=189)
    ap.add_argument('--allow-partial', action='store_true',
                    help='Allow fewer than expected prompts (writes file but warns)')
    args = ap.parse_args()

    pattern = f"WA-{args.cluster_code}-phase9-char{args.char_seq}-{args.short_name}-findings-seg*.md"
    seg_files = sorted(args.seg_dir.glob(pattern),
                       key=lambda p: int(SEG_NUM_RE.search(p.name).group(1)))
    if not seg_files:
        raise SystemExit(f"No segments matched pattern {pattern} in {args.seg_dir}")

    # Identify date from first segment filename: -v1-YYYYMMDD.md
    m = re.search(r'-v(\d+)-(\d{8})\.md$', seg_files[0].name)
    if not m:
        raise SystemExit(f"Cannot parse version+date from {seg_files[0].name}")
    version_num, date = m.group(1), m.group(2)

    out_path = args.out_dir / f"WA-{args.cluster_code}-phase9-char{args.char_seq}-{args.short_name}-findings-v{version_num}-{date}.md"

    print(f"Char {args.char_seq} ({args.short_name})")
    print(f"  Segments found ({len(seg_files)}):")
    seg_counts = []
    for f in seg_files:
        text = f.read_text(encoding='utf-8')
        n = len(PROMPT_HEADER_RE.findall(text))
        seg_counts.append(n)
        print(f"    {f.name} — {n} prompts")
    total = sum(seg_counts)
    print(f"  Total: {total} prompts (expected {args.expected_prompts})")

    if total != args.expected_prompts and not args.allow_partial:
        raise SystemExit(
            f"FAIL: total {total} != expected {args.expected_prompts}. "
            f"Pass --allow-partial to merge anyway."
        )

    # Build merged content
    header = [
        f"# {args.cluster_code} Phase 9 — Characteristic {args.char_seq} ({args.short_name}) — findings",
        "",
        f"**Date:** {date[:4]}-{date[4:6]}-{date[6:]}",
        f"**Characteristic_id:** {args.char_seq}",
        f"**Characteristic name:** {args.short_name}",
        f"**Prompts answered:** {total} of {args.expected_prompts}{' (PARTIAL — see segments)' if total != args.expected_prompts else ''}",
        f"**Source segments (merged):** " + ", ".join(f.name for f in seg_files),
        "",
        "---",
        "",
    ]

    parts = ["\n".join(header)]
    for f in seg_files:
        text = f.read_text(encoding='utf-8')
        m = PROMPT_HEADER_RE.search(text)
        if not m:
            raise SystemExit(f"No prompt header in {f.name}")
        body = text[m.start():].rstrip()
        parts.append("\n" + body + "\n")

    out_path.write_text("\n".join(parts), encoding='utf-8')
    final = out_path.read_text(encoding='utf-8')
    final_count = len(PROMPT_HEADER_RE.findall(final))
    print(f"  Wrote {out_path}")
    print(f"  Merged file size: {out_path.stat().st_size:,} bytes")
    print(f"  Prompt headers in merged file: {final_count}")
    if total != args.expected_prompts:
        print(f"  WARNING: partial merge ({total}/{args.expected_prompts}); do NOT apply via loader without missing segment(s).")


if __name__ == '__main__':
    main()
