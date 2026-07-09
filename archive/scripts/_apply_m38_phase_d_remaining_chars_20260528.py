"""M38 Phase D — run characteristics 1, 2, 4, 5, 6, 7 sequentially via API,
merge + load each, all in one background batch.

Skips char 3 (already done).
"""
from __future__ import annotations
import subprocess, sys, time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REMAINING = [1, 2, 4, 5, 6, 7]


def run(cmd: list[str]) -> int:
    print(f"\n>>> {' '.join(cmd[:6])}...")
    t0 = time.time()
    result = subprocess.run(cmd)
    dt = time.time() - t0
    print(f"<<< exit={result.returncode} dt={dt:.0f}s")
    return result.returncode


def main():
    t_start = time.time()
    for char_seq in REMAINING:
        print(f"\n========== CHAR {char_seq} ==========")

        # All 4 segments in one go
        rc = run([
            sys.executable,
            "scripts/_apply_m38_phase_d_characteristic_via_api_20260528.py",
            "--char-seq", str(char_seq),
            "--segments", "all",
        ])
        if rc != 0:
            print(f"ERROR: char {char_seq} API run failed; continuing to merge attempt anyway")

        # Merge + load
        rc = run([
            sys.executable,
            "scripts/_merge_and_load_m38_phase_d_char_20260528.py",
            "--char-seq", str(char_seq),
        ])
        if rc != 0:
            print(f"ERROR: char {char_seq} merge+load failed (will continue with next char)")

    print(f"\n========== ALL CHARS COMPLETE ==========")
    print(f"Total wall time: {(time.time() - t_start) / 60:.1f} min")


if __name__ == "__main__":
    main()
