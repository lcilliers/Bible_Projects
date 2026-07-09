"""Merge M38 Phase D synthesis tier files (T0..T7) + load.

Uses the tier-based output files (one per tier) rather than the truncated
seg-based ones. Remaps q_codes by order then concatenates into a single
canonical synthesis file, then runs the synthesis loader.
"""
from __future__ import annotations
import argparse, re, sqlite3, subprocess, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = "database/bible_research.db"
OUT_DIR = Path("Sessions/Session_Clusters/M38")
DATE = "20260528"
TIERS = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7"]
PROMPT_HEADER_RE = re.compile(r'^\*\*T\d+\.\d+\.\d+ —', re.MULTILINE)
PROMPT_HEADER_FULL_RE = re.compile(r'^(\*\*)(T\d+\.\d+\.\d+)( —[^\n]+)$', re.MULTILINE)


def expected_qcodes(conn, tier):
    return [r[0] for r in conn.execute("""
        SELECT question_code FROM wa_obs_question_catalogue
        WHERE tier=? AND COALESCE(deleted,0)=0
        ORDER BY tier, prompt_seq, obs_id
    """, (tier,))]


def remap_tier(path, expected):
    text = path.read_text(encoding="utf-8")
    headers = list(PROMPT_HEADER_FULL_RE.finditer(text))
    new_parts = []
    last = 0
    for i, m in enumerate(headers):
        new_parts.append(text[last:m.start()])
        if i < len(expected):
            new_parts.append(f"{m.group(1)}{expected[i]}{m.group(3)}")
        else:
            new_parts.append(m.group(0))
        last = m.end()
    new_parts.append(text[last:])
    path.write_text("".join(new_parts), encoding="utf-8")
    return len(headers)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    conn = sqlite3.connect(DB)

    tier_files = {}
    for tier in TIERS:
        files = list(OUT_DIR.glob(f"WA-M38-phase-d-cluster-synthesis-findings-{tier}-v1-{DATE}.md"))
        if len(files) != 1:
            print(f"ERROR: tier {tier}: found {len(files)} files (expected 1)")
            sys.exit(1)
        tier_files[tier] = files[0]

    grand_total = 0
    for tier in TIERS:
        expected = expected_qcodes(conn, tier)
        n = remap_tier(tier_files[tier], expected)
        flag = "" if n == len(expected) else f"⚠ {n}/{len(expected)}"
        print(f"  {tier}: {n} blocks (expected {len(expected)}) {flag}")
        grand_total += min(n, len(expected))

    print(f"\nTotal usable blocks: {grand_total} (expected 189)")
    if grand_total != 189:
        print("ABORT: cannot load with mismatch.")
        sys.exit(2)

    # Merge into canonical
    merged_parts = []
    for i, tier in enumerate(TIERS):
        text = tier_files[tier].read_text(encoding="utf-8")
        if i == 0:
            merged_parts.append(text.rstrip())
        else:
            m = PROMPT_HEADER_RE.search(text)
            if m:
                merged_parts.append(text[m.start():].rstrip())

    canonical = OUT_DIR / f"WA-M38-phase-d-cluster-synthesis-findings-v1-{DATE}.md"
    canonical.write_text("\n\n".join(merged_parts) + "\n", encoding="utf-8")
    n_total = len(PROMPT_HEADER_RE.findall(canonical.read_text(encoding="utf-8")))
    print(f"Merged: {canonical.name} — {n_total} prompt blocks")

    if args.dry_run:
        return

    cmd = [sys.executable, "scripts/_apply_phase9_cluster_synthesis_20260519.py",
           "--findings", str(canonical), "--cluster-code", "M38"]
    print(f"\nLoading: {' '.join(cmd)}")
    sys.exit(subprocess.run(cmd).returncode)


if __name__ == "__main__":
    main()
