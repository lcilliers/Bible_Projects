"""Repair M38 Phase D q_codes — the AI numbered codes sequentially within
its own scheme rather than using the catalogue's question_codes. Order was
preserved (verified by question_text alignment), so we can remap by position.

Process per characteristic:
  1. Merge segments into canonical file (re-runs the merge step)
  2. Build catalogue-order list of expected question_codes (same SQL order
     as used at API time)
  3. Walk through merged file's prompt blocks in order, replacing the AI's
     q_code header with the catalogue's expected q_code
  4. Verify: if any block remains unmatched (count mismatch), report it
  5. Load via the standard loader
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

PROMPT_HEADER_RE = re.compile(r'^\*\*T\d+\.\d+\.\d+ —', re.MULTILINE)
PROMPT_HEADER_FULL_RE = re.compile(r'^(\*\*)(T\d+\.\d+\.\d+)( —[^\n]+)$', re.MULTILINE)


def expected_qcodes_in_seg_order(conn, tiers: list[str]) -> list[str]:
    placeholders = ",".join("?" * len(tiers))
    rows = list(conn.execute(f"""
        SELECT question_code FROM wa_obs_question_catalogue
        WHERE tier IN ({placeholders}) AND COALESCE(deleted,0)=0
        ORDER BY tier, prompt_seq, obs_id
    """, tiers))
    return [r[0] for r in rows]


def remap_segment(seg_path: Path, expected_codes: list[str]) -> tuple[int, int, str]:
    """Returns (n_blocks_found, n_blocks_expected, rewritten_text)."""
    text = seg_path.read_text(encoding="utf-8")
    blocks_found = len(PROMPT_HEADER_RE.findall(text))
    n_expected = len(expected_codes)

    # Walk through prompts in order, replacing each AI code with the expected one
    headers = list(PROMPT_HEADER_FULL_RE.finditer(text))
    if len(headers) != blocks_found:
        # mismatch in detection — shouldn't happen with current regex
        pass

    new_text_parts = []
    last_end = 0
    for i, m in enumerate(headers):
        new_text_parts.append(text[last_end:m.start()])
        if i < n_expected:
            new_header = f"{m.group(1)}{expected_codes[i]}{m.group(3)}"
        else:
            # extra block — keep as is (will be flagged as count mismatch)
            new_header = m.group(0)
        new_text_parts.append(new_header)
        last_end = m.end()
    new_text_parts.append(text[last_end:])
    return blocks_found, n_expected, "".join(new_text_parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--char-seq", type=int, required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)

    SEGMENTS = [
        ("seg1", ["T0", "T1"]),
        ("seg2", ["T2", "T3"]),
        ("seg3", ["T4", "T5"]),
        ("seg4", ["T6", "T7"]),
    ]

    seg_files = sorted(OUT_DIR.glob(f"WA-M38-phase-d-char{args.char_seq}-*-findings-seg*-v1-{DATE}.md"))
    if len(seg_files) != 4:
        print(f"ERROR: expected 4 segments, got {len(seg_files)}")
        sys.exit(1)

    # Remap each segment
    total_blocks = 0
    delta_segments = []
    for sf in seg_files:
        # Identify which seg this is
        seg_id = re.search(r'-seg(\d+)-', sf.name).group(1)
        seg_idx = int(seg_id) - 1
        seg_name, tiers = SEGMENTS[seg_idx]
        expected = expected_qcodes_in_seg_order(conn, tiers)
        n_found, n_exp, new_text = remap_segment(sf, expected)
        total_blocks += min(n_found, n_exp)
        flag = "" if n_found == n_exp else f"⚠ {n_found}/{n_exp}"
        print(f"  {seg_name}: {n_found} blocks; {n_exp} expected {flag}")
        if n_found != n_exp:
            delta_segments.append((seg_name, n_found, n_exp))
        sf.write_text(new_text, encoding="utf-8")

    if delta_segments:
        print(f"\n⚠ Count mismatches in {len(delta_segments)} segments — char_seq={args.char_seq} cannot be loaded until fixed.")
        for sn, nf, ne in delta_segments:
            print(f"  {sn}: {nf}/{ne}")
        sys.exit(2)

    # Merge + load
    print(f"\nAll segments remapped — running merge+load...")
    cmd = [
        sys.executable, "scripts/_merge_and_load_m38_phase_d_char_20260528.py",
        "--char-seq", str(args.char_seq),
    ]
    if args.dry_run:
        cmd.append("--dry-run")
    rc = subprocess.run(cmd).returncode
    sys.exit(rc)


if __name__ == "__main__":
    main()
