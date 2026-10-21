"""
_batch_extract.py — Run STEP extraction for all words that need a discovery JSON.
Then run audit_word for each. Each step is a subprocess to avoid DB lock issues.
"""
import json
import os
import subprocess
import sys
import time

ROOT = os.path.join(os.path.dirname(__file__), "..")
LIST_FILE = os.path.join(os.path.dirname(__file__), "_batch_extract_list.json")


def run_extract(word, anchors, reg_no):
    """Run word_study_extract.py as subprocess."""
    cmd = [
        sys.executable, "scripts/word_study_extract.py",
        "--word", word,
    ]
    if anchors:
        cmd += ["--anchors", anchors]

    proc = subprocess.run(
        cmd, capture_output=True, text=True, timeout=300,
        cwd=ROOT, env={**os.environ, "PYTHONUTF8": "1"},
    )
    if proc.returncode == 0 and "Complete" in proc.stdout:
        # Extract term/verse counts from output
        lines = proc.stdout.strip().split("\n")
        for line in lines:
            if "Include / Exclude" in line:
                return "OK", line.strip()
        return "OK", "extracted"
    else:
        err = (proc.stderr or proc.stdout or "unknown error").strip().split("\n")[-1][:120]
        return "FAIL", err


def run_audit(reg_no):
    """Run audit_word as subprocess."""
    cmd = [
        sys.executable, "-m", "engine.engine",
        "--mode=audit_word", f"--registry={reg_no}",
    ]
    proc = subprocess.run(
        cmd, capture_output=True, text=True, timeout=180,
        cwd=ROOT, env={**os.environ, "PYTHONUTF8": "1"},
    )
    output = proc.stdout + proc.stderr
    if "AUDIT_WORD COMPLETE" in output:
        # Extract result
        for line in output.split("\n"):
            if "Result" in line and ":" in line:
                return "OK", line.strip()[:80]
        return "OK", "audited"
    elif "[STOP]" in output:
        for line in output.split("\n"):
            if "[STOP]" in line:
                return "STOP", line.strip()[:120]
        return "STOP", "unknown stop"
    else:
        err = output.strip().split("\n")[-1][:120]
        return "FAIL", err


def main():
    with open(LIST_FILE) as f:
        words = json.load(f)

    total = len(words)
    print(f"\n{'=' * 70}")
    print(f"  BATCH EXTRACT + AUDIT — {total} words")
    print(f"  Phase 1: STEP extraction  |  Phase 2: audit_word")
    print(f"{'=' * 70}")

    # Phase 1: Extract
    print(f"\n{'─' * 70}")
    print(f"  PHASE 1: STEP EXTRACTION")
    print(f"{'─' * 70}")

    extract_ok = 0
    extract_fail = []
    start = time.time()

    for i, w in enumerate(words, 1):
        reg_no = w["no"]
        word = w["word"]
        anchors = w["anchors"]

        # Check if discovery JSON already exists
        discovery_dir = os.path.join(ROOT, "research", "discovery")
        prefix = f"{reg_no:03d}_{word.lower().replace(' ', '_')}_step_data_"
        existing = [f for f in os.listdir(discovery_dir) if f.startswith(prefix) and f.endswith(".json")]
        if existing:
            extract_ok += 1
            elapsed = time.time() - start
            print(f"  [{i}/{total}] {reg_no:>4} {word:<22} SKIP (exists: {existing[-1]})")
            continue

        status, detail = run_extract(word, anchors, reg_no)
        elapsed = time.time() - start
        if status == "OK":
            extract_ok += 1
            print(f"  [{i}/{total}] {reg_no:>4} {word:<22} OK  ({elapsed:.0f}s elapsed)")
        else:
            extract_fail.append((reg_no, word, detail))
            print(f"  [{i}/{total}] {reg_no:>4} {word:<22} FAIL: {detail[:80]}")

    extract_time = time.time() - start
    print(f"\n  Phase 1 complete: {extract_ok} OK, {len(extract_fail)} FAIL ({extract_time:.0f}s)")

    # Phase 2: Audit
    print(f"\n{'─' * 70}")
    print(f"  PHASE 2: AUDIT_WORD")
    print(f"{'─' * 70}")

    audit_ok = 0
    audit_review = 0
    audit_fail = []
    start2 = time.time()

    for i, w in enumerate(words, 1):
        reg_no = w["no"]
        word = w["word"]

        # Skip if extraction failed
        if any(r == reg_no for r, _, _ in extract_fail):
            print(f"  [{i}/{total}] {reg_no:>4} {word:<22} SKIP (extraction failed)")
            continue

        status, detail = run_audit(reg_no)
        elapsed = time.time() - start2
        if status == "OK":
            if "REVIEW" in detail:
                audit_review += 1
                print(f"  [{i}/{total}] {reg_no:>4} {word:<22} REVIEW  ({elapsed:.0f}s)")
            else:
                audit_ok += 1
                print(f"  [{i}/{total}] {reg_no:>4} {word:<22} PASS    ({elapsed:.0f}s)")
        else:
            audit_fail.append((reg_no, word, detail))
            print(f"  [{i}/{total}] {reg_no:>4} {word:<22} {status}: {detail[:80]}")

    audit_time = time.time() - start2
    total_time = time.time() - start + extract_time

    print(f"\n{'=' * 70}")
    print(f"  BATCH COMPLETE")
    print(f"  Extract: {extract_ok} OK, {len(extract_fail)} FAIL ({extract_time:.0f}s)")
    print(f"  Audit:   {audit_ok} PASS, {audit_review} REVIEW, {len(audit_fail)} FAIL ({audit_time:.0f}s)")
    print(f"  Total time: {total_time:.0f}s ({total_time/60:.1f} min)")
    if extract_fail:
        print(f"\n  Extract failures:")
        for r, w, d in extract_fail:
            print(f"    {r:>4} {w:<22} {d}")
    if audit_fail:
        print(f"\n  Audit failures:")
        for r, w, d in audit_fail:
            print(f"    {r:>4} {w:<22} {d}")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    main()
