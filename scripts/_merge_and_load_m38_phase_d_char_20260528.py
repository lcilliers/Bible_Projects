"""Merge M38 Phase D segments + load into cluster_finding.

For one characteristic at a time:
  1. Collect the 4 segment files (seg1..seg4)
  2. Concatenate into a single canonical findings .md file
  3. Use _apply_phase9_characteristic_findings_*.py to load into DB

Usage:
    python scripts/_merge_and_load_m38_phase_d_char_20260528.py --char-seq N
"""
from __future__ import annotations
import argparse, re, subprocess, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = "20260528"
PROMPT_HEADER_RE = re.compile(r'^\*\*T\d+\.\d+\.\d+ —', re.MULTILINE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--char-seq", type=int, required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    # Find all segment files for this characteristic
    seg_files = sorted(OUT_DIR.glob(f"WA-M38-phase-d-char{args.char_seq}-*-findings-seg*-*-v1-{DATE}.md"))
    if len(seg_files) != 4:
        print(f"ERROR: expected 4 segment files for char {args.char_seq}, got {len(seg_files)}: {seg_files}")
        sys.exit(1)

    # Extract short_name from first seg's filename
    first_name = seg_files[0].stem
    # Pattern: WA-M38-phase-d-char{N}-{SHORT}-findings-seg{X}-{tiers}-v1-{date}
    m = re.match(rf"WA-M38-phase-d-char{args.char_seq}-(.+?)-findings-seg\d+", first_name)
    if not m:
        print(f"ERROR: can't extract short name from {first_name}")
        sys.exit(1)
    short = m.group(1)

    canonical = OUT_DIR / f"WA-M38-phase-d-char{args.char_seq}-{short}-findings-v1-{DATE}.md"

    # Concatenate: keep first segment's header, strip subsequent segment headers (everything before first prompt)
    merged_lines = []
    for i, sf in enumerate(seg_files):
        text = sf.read_text(encoding="utf-8")
        if i == 0:
            # Keep the whole text, but replace the tier-segment line in the header
            text = re.sub(r'\*\*Tier-segment:\*\* [^\n]+', '**Tier:** Full 189-prompt T0-T7 catalogue', text)
            merged_lines.append(text.rstrip())
        else:
            # Strip everything before the first prompt
            m = PROMPT_HEADER_RE.search(text)
            if not m:
                print(f"WARNING: no prompt blocks in {sf.name}")
                continue
            merged_lines.append(text[m.start():].rstrip())

    canonical.write_text("\n\n".join(merged_lines) + "\n", encoding="utf-8")

    # Count blocks
    n_blocks = len(PROMPT_HEADER_RE.findall(canonical.read_text(encoding="utf-8")))
    print(f"Merged: {canonical.name}")
    print(f"Prompt blocks: {n_blocks} (expected 189)")

    if n_blocks != 189:
        print(f"ERROR: prompt count mismatch — cannot load")
        sys.exit(1)

    if args.dry_run:
        print("Dry-run only — not loading.")
        return

    # Load via existing loader
    cmd = [
        sys.executable, "scripts/_apply_phase9_characteristic_findings_20260518.py",
        "--findings", str(canonical),
        "--cluster-code", "M38",
        "--char-seq", str(args.char_seq),
    ]
    print(f"\nLoading via: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
