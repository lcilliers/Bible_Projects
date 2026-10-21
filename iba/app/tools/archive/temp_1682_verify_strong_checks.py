"""
temp_1682_verify_strong_checks.py (round 2)

Computes the required strong_checks block for a process-(c) family JSON (escalation #1682 spec):
diffs traces.occurrences (across all observations) against Json A's full occurrence list per
strong, and writes strong_checks back into the family JSON in place -- mechanical, not eyeballed,
per the round-2 rule that per-strong traceability must be verified and recorded, not assumed.

Usage:
    python iba/app/tools/temp_1682_verify_strong_checks.py \
        --a <process-a-input.json> --family <family.json>

Exits non-zero if any strong has missing verses, after writing strong_checks into the family file
either way (so the gap is visible in the file, not just in this script's exit code).
"""
import argparse
import json
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="process (a) full-cluster input JSON")
    ap.add_argument("--family", required=True, help="process (c) family JSON to check and update")
    args = ap.parse_args()

    with open(args.a, encoding="utf-8") as f:
        a = json.load(f)
    by_strong = {s["strong"]: s for s in a["strongs"]}

    with open(args.family, encoding="utf-8") as f:
        fam = json.load(f)

    checks = []
    any_missing = False
    for strong in fam["strongs_in_family"]:
        all_verses = {o["osisId"] for o in by_strong[strong]["occurrences"]}
        traced = set()
        for o in fam["observations"]:
            t = o.get("traces", {})
            if t.get("strong") != strong:
                continue
            for occ in t.get("occurrences") or []:
                if occ.get("verse"):
                    traced.add(occ["verse"])
        missing = sorted(all_verses - traced)
        if missing:
            any_missing = True
        checks.append({
            "strong": strong,
            "occurrence_count": len(all_verses),
            "traced_count": len(all_verses & traced),
            "missing_verses": missing,
        })

    fam["strong_checks"] = checks
    with open(args.family, "w", encoding="utf-8") as f:
        json.dump(fam, f, indent=2, ensure_ascii=False)

    for c in checks:
        status = "OK" if not c["missing_verses"] else f"MISSING {c['missing_verses']}"
        print(f"{c['strong']}: {c['occurrence_count']} occ, {c['traced_count']} traced -- {status}")

    if any_missing:
        print("\nRESULT: INCOMPLETE -- fix before this family's output is considered done.")
        return 1
    print("\nRESULT: all strongs fully traced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
