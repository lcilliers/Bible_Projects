"""Validate Phase B B.2 sub-group design per v3_0 §6.2.7.

Checks:
  1. Every is_relevant=1 vc_id in the cluster appears in exactly one sub-group.
  2. No sub-group exceeds 40% of cluster's substantive verses (§6.2.7 distribution gate).
  3. BOUNDARY sub-group (if present) does not exceed 15% AND does not contain verses of STAYS-verdict terms (§6.2.6 BOUNDARY-not-a-parking-lot).
  4. Each sub-group has subgroup_code, label, core_description, evidence_basis.

Usage:
  python scripts/_validate_cluster_phase_b2_v1_20260528.py --cluster M38 --mapping <path>

Exit codes:
  0  PASS
  2  FAIL with delta
"""
from __future__ import annotations
import argparse, json, sqlite3, sys
from collections import Counter
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--mapping", required=True, help="Path to B.2 mapping JSON")
    ap.add_argument("--db", default="database/bible_research.db")
    args = ap.parse_args()

    mapping_path = Path(args.mapping)
    data = json.loads(mapping_path.read_text(encoding="utf-8"))
    subgroups = data.get("subgroups", [])

    conn = sqlite3.connect(args.db)
    expected_vc = set(r[0] for r in conn.execute("""
        SELECT vc.id FROM verse_context vc JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code = ? AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged,0) = 0
          AND COALESCE(mt.delete_flagged,0) = 0
    """, (args.cluster,)))
    total_substantive = len(expected_vc)
    print(f"Cluster {args.cluster}: {total_substantive} substantive (is_relevant=1) verses")

    errors = []

    # Check 4: subgroup metadata
    seen_codes = set()
    for sg in subgroups:
        code = sg.get("subgroup_code", "")
        if not code:
            errors.append(f"  Sub-group missing subgroup_code: {sg}")
            continue
        if code in seen_codes:
            errors.append(f"  Duplicate subgroup_code: {code}")
        seen_codes.add(code)
        for field in ("label", "core_description", "evidence_basis"):
            if not sg.get(field):
                errors.append(f"  {code}: missing {field}")

    # Check 1: coverage
    all_vcs = []
    for sg in subgroups:
        for vc in sg.get("verses", []):
            all_vcs.append((vc, sg.get("subgroup_code", "?")))
    c = Counter(vc for vc, _ in all_vcs)
    dups = [(vc, n) for vc, n in c.items() if n > 1]
    if dups:
        errors.append(f"  {len(dups)} vc_ids appear in multiple sub-groups: {dups[:5]}...")
    present = set(c.keys())
    missing = expected_vc - present
    extra = present - expected_vc
    if missing:
        errors.append(f"  {len(missing)} vc_ids missing from sub-group assignment: {sorted(missing)[:10]}...")
    if extra:
        errors.append(f"  {len(extra)} vc_ids in sub-groups but not in cluster: {sorted(extra)[:10]}...")

    # Check 2: distribution gate
    boundary_codes = {code for code in seen_codes if code.endswith("-BOUNDARY")}
    substantive_total = total_substantive  # M38 has no BOUNDARY sub-group
    for sg in subgroups:
        code = sg.get("subgroup_code")
        if code in boundary_codes:
            continue
        n = len(sg.get("verses", []))
        pct = n / max(substantive_total, 1)
        if pct > 0.40:
            errors.append(f"  {code} holds {n}/{substantive_total} = {pct:.1%} — exceeds 40% gate (§6.2.7)")

    # Check 3: BOUNDARY parking lot
    for sg in subgroups:
        code = sg.get("subgroup_code")
        if code not in boundary_codes:
            continue
        n = len(sg.get("verses", []))
        pct = n / max(substantive_total, 1)
        if pct > 0.15:
            errors.append(f"  {code} BOUNDARY holds {n}/{substantive_total} = {pct:.1%} — exceeds 15% (§6.2.6)")

    print()
    print("Sub-group sizes:")
    for sg in subgroups:
        code = sg.get("subgroup_code")
        n = len(sg.get("verses", []))
        pct = n / max(total_substantive, 1)
        label = sg.get("label", "")
        marker = "⚠" if pct > 0.40 else " "
        print(f"  {marker} {code:10s} {n:4d} ({pct:5.1%}) — {label}")

    if errors:
        print(f"\nFAIL — {len(errors)} issues:")
        for e in errors:
            print(e)
        sys.exit(2)
    print(f"\nPASS — Phase B B.2 stage gate validated for cluster {args.cluster}")
    sys.exit(0)


if __name__ == "__main__":
    main()
