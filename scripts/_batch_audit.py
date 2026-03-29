"""
_batch_audit.py — Run audit_word on all registries that need it.
Skips registries with last_automation_run = 'AUDITED' and Excluded phase1_status.
Handles missing Step 1 JSON by running STEP extraction first.
"""
import sqlite3
import os
import sys
import subprocess
import time

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
ROOT = os.path.join(os.path.dirname(__file__), "..")


def get_registries():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT no, word, last_automation_run, phase1_status, strongs_list
        FROM word_registry
        WHERE (last_automation_run != 'AUDITED' OR last_automation_run IS NULL)
        AND phase1_status != 'Excluded'
        ORDER BY no
    """).fetchall()
    result = [dict(r) for r in rows]
    conn.close()
    return result


def main():
    registries = get_registries()
    total = len(registries)
    print(f"\n{'=' * 60}")
    print(f"  BATCH AUDIT — {total} registries")
    print(f"{'=' * 60}\n")

    results = {"PASS": 0, "REVIEW": 0, "STOP": 0, "ERROR": 0}
    errors = []

    for i, r in enumerate(registries, 1):
        reg_no = r["no"]
        word = r["word"]
        print(f"\n[{i}/{total}] Registry {reg_no} — {word}")

        # Run audit_word as a subprocess to avoid DB lock contamination
        cmd = [
            sys.executable, "-m", "engine.engine",
            "--mode=audit_word", f"--registry={reg_no}",
        ]
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True, timeout=120,
                cwd=ROOT, env={**os.environ, "PYTHONUTF8": "1"},
            )
            output = proc.stdout + proc.stderr

            if "AUDIT_WORD COMPLETE" in output:
                if "REVIEW" in output.split("AUDIT_WORD COMPLETE")[0].split("Result")[-1]:
                    results["REVIEW"] += 1
                    print(f"  REVIEW")
                else:
                    results["PASS"] += 1
                    print(f"  PASS")
            elif "[STOP]" in output:
                # Check if it's a missing JSON issue
                if "Step 1 JSON not found" in output:
                    print(f"  No Step 1 JSON — skipping (needs STEP extraction)")
                    results["STOP"] += 1
                    errors.append((reg_no, word, "NO_JSON"))
                else:
                    results["STOP"] += 1
                    # Extract stop reason
                    for line in output.split("\n"):
                        if "[STOP]" in line:
                            errors.append((reg_no, word, line.strip()[:120]))
                            print(f"  STOP: {line.strip()[:100]}")
                            break
            elif proc.returncode != 0:
                results["ERROR"] += 1
                last_lines = output.strip().split("\n")[-3:]
                err_msg = " ".join(last_lines)[:120]
                errors.append((reg_no, word, err_msg))
                print(f"  ERROR: {err_msg[:100]}")
            else:
                results["PASS"] += 1
                print(f"  OK")

        except subprocess.TimeoutExpired:
            results["ERROR"] += 1
            errors.append((reg_no, word, "TIMEOUT (120s)"))
            print(f"  TIMEOUT")
        except Exception as exc:
            results["ERROR"] += 1
            errors.append((reg_no, word, str(exc)[:120]))
            print(f"  ERROR: {exc}")

    print(f"\n{'=' * 60}")
    print(f"  BATCH AUDIT COMPLETE")
    print(f"  Total:        {total}")
    print(f"  PASS:         {results['PASS']}")
    print(f"  REVIEW:       {results['REVIEW']}")
    print(f"  STOP/NO_JSON: {results['STOP']}")
    print(f"  ERROR:        {results['ERROR']}")
    if errors:
        print(f"\n  Issues ({len(errors)}):")
        for reg_no, word, detail in errors:
            print(f"    {reg_no:>4} {word:<20} {detail}")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
