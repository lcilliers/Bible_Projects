"""Merge M38 Phase D synthesis segments + remap q_codes + load.

Mirrors the per-characteristic merger but for synthesis (uses [CLUSTER] marker).
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
SEGMENTS = [
    ("seg1", ["T0", "T1"]),
    ("seg2", ["T2", "T3"]),
    ("seg3", ["T4", "T5"]),
    ("seg4", ["T6", "T7"]),
]
PROMPT_HEADER_RE = re.compile(r'^\*\*T\d+\.\d+\.\d+ —', re.MULTILINE)
PROMPT_HEADER_FULL_RE = re.compile(r'^(\*\*)(T\d+\.\d+\.\d+)( —[^\n]+)$', re.MULTILINE)


def expected_qcodes(conn, tiers):
    placeholders = ",".join("?" * len(tiers))
    rows = list(conn.execute(f"""
        SELECT question_code FROM wa_obs_question_catalogue
        WHERE tier IN ({placeholders}) AND COALESCE(deleted,0)=0
        ORDER BY tier, prompt_seq, obs_id
    """, tiers))
    return [r[0] for r in rows]


def remap_segment_qcodes(path, expected_codes):
    text = path.read_text(encoding="utf-8")
    headers = list(PROMPT_HEADER_FULL_RE.finditer(text))
    n_blocks = len(headers)
    new_parts = []
    last_end = 0
    for i, m in enumerate(headers):
        new_parts.append(text[last_end:m.start()])
        if i < len(expected_codes):
            new_parts.append(f"{m.group(1)}{expected_codes[i]}{m.group(3)}")
        else:
            new_parts.append(m.group(0))
        last_end = m.end()
    new_parts.append(text[last_end:])
    path.write_text("".join(new_parts), encoding="utf-8")
    return n_blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    conn = sqlite3.connect(DB)

    seg_files = sorted(OUT_DIR.glob(f"WA-M38-phase-d-cluster-synthesis-findings-seg*-v1-{DATE}.md"))
    if len(seg_files) != 4:
        print(f"ERROR: expected 4 segment files, got {len(seg_files)}")
        sys.exit(1)

    # Remap each segment's q_codes
    total = 0
    for sf in seg_files:
        seg_id = re.search(r'-seg(\d+)-', sf.name).group(1)
        seg_idx = int(seg_id) - 1
        seg_name, tiers = SEGMENTS[seg_idx]
        expected = expected_qcodes(conn, tiers)
        n_blocks = remap_segment_qcodes(sf, expected)
        print(f"  {seg_name}: {n_blocks} blocks ({'+'.join(tiers)} expected {len(expected)})")
        total += n_blocks
        if n_blocks != len(expected):
            print(f"  ⚠ mismatch in {seg_name}")

    # Merge
    merged_lines = []
    for i, sf in enumerate(seg_files):
        text = sf.read_text(encoding="utf-8")
        if i == 0:
            text = re.sub(r'\*\*Tier-segment:\*\* [^\n]+', '**Tier:** Full 189-prompt T0-T7 cluster synthesis', text)
            merged_lines.append(text.rstrip())
        else:
            m = PROMPT_HEADER_RE.search(text)
            if not m:
                continue
            merged_lines.append(text[m.start():].rstrip())

    canonical = OUT_DIR / f"WA-M38-phase-d-cluster-synthesis-findings-v1-{DATE}.md"
    canonical.write_text("\n\n".join(merged_lines) + "\n", encoding="utf-8")
    n_total = len(PROMPT_HEADER_RE.findall(canonical.read_text(encoding="utf-8")))
    print(f"\nMerged: {canonical.name} — {n_total} prompt blocks")

    if n_total != 189:
        print(f"ERROR: expected 189, got {n_total}")
        sys.exit(1)

    if args.dry_run:
        print("Dry-run only")
        return

    cmd = [sys.executable, "scripts/_apply_phase9_cluster_synthesis_20260519.py",
           "--findings", str(canonical), "--cluster-code", "M38"]
    print(f"\nLoading: {' '.join(cmd)}")
    rc = subprocess.run(cmd).returncode
    sys.exit(rc)


if __name__ == "__main__":
    main()
