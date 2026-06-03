"""Validate Phase B B.3 unified VCG creation JSON per v3_0 §6.3.6.

Checks:
  1. Every vc_id in the JSON exists in verse_context with is_relevant=1, delete_flagged=0, cluster_code matching.
  2. No vc_id appears in two VCGs (unless declared dual_membership).
  3. Sum of `verses` per sub-group equals the DB's count of is_relevant vc rows routed to that sub-group at B.2.
  4. Every `anchor_vc_id` is in its VCG's `verses`.
  5. (M38 has no BOUNDARY sub-group so check 5 skipped.)

Usage:
  python scripts/_validate_cluster_phase_b3_v1_20260528.py --cluster M38 --vcg <path> --b2-mapping <path>

Exit codes:
  0  PASS
  2  FAIL
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
    ap.add_argument("--vcg", required=True)
    ap.add_argument("--b2-mapping", required=True)
    ap.add_argument("--db", default="database/bible_research.db")
    args = ap.parse_args()

    vcg_data = json.loads(Path(args.vcg).read_text(encoding="utf-8"))
    b2 = json.loads(Path(args.b2_mapping).read_text(encoding="utf-8"))
    expected_by_sg = {sg["subgroup_code"]: set(sg["verses"]) for sg in b2["subgroups"]}

    errors = []

    conn = sqlite3.connect(args.db)
    valid_cluster_vcs = set(r[0] for r in conn.execute("""
        SELECT vc.id FROM verse_context vc JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code = ? AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(mt.delete_flagged,0)=0
    """, (args.cluster,)))

    for code, sg_data in vcg_data.get("subgroups", {}).items():
        expected = expected_by_sg.get(code)
        if expected is None:
            errors.append(f"  {code}: not in B.2 mapping")
            continue
        all_v = []
        for vcg in sg_data.get("vcgs", []):
            anchor = vcg.get("anchor_vc_id")
            verses = vcg.get("verses", [])
            for vc in verses:
                all_v.append(vc)
                if vc not in valid_cluster_vcs:
                    errors.append(f"  {code} {vcg.get('provisional_code')}: vc_id={vc} not a valid cluster IB vc")
            # Anchor in verses
            if anchor is None:
                errors.append(f"  {code} {vcg.get('provisional_code')}: missing anchor_vc_id")
            elif anchor not in verses:
                errors.append(f"  {code} {vcg.get('provisional_code')}: anchor {anchor} not in verses")

        c = Counter(all_v)
        distinct = set(c.keys())
        declared = {d.get("vc_id") for d in sg_data.get("dual_memberships", [])}
        actual_dups = {vc for vc, n in c.items() if n > 1}
        undecl = actual_dups - declared
        if undecl:
            errors.append(f"  {code}: undeclared duplicates {sorted(undecl)[:10]}")
        if distinct != expected:
            missing = expected - distinct
            extra = distinct - expected
            if missing:
                errors.append(f"  {code}: missing {sorted(missing)[:10]}")
            if extra:
                errors.append(f"  {code}: extra (not in B.2 mapping) {sorted(extra)[:10]}")

    # Coverage across cluster
    all_cluster_vcs_in_b3 = set()
    for sg_data in vcg_data.get("subgroups", {}).values():
        for vcg in sg_data.get("vcgs", []):
            all_cluster_vcs_in_b3.update(vcg.get("verses", []))
    cluster_missing = valid_cluster_vcs - all_cluster_vcs_in_b3
    cluster_extra = all_cluster_vcs_in_b3 - valid_cluster_vcs
    if cluster_missing:
        errors.append(f"  CLUSTER: missing from any VCG {sorted(cluster_missing)[:10]}")
    if cluster_extra:
        errors.append(f"  CLUSTER: extra in VCGs but not IB cluster verses {sorted(cluster_extra)[:10]}")

    # Report
    print(f"Cluster {args.cluster}: {len(valid_cluster_vcs)} IB verses")
    for code, sg_data in sorted(vcg_data.get("subgroups", {}).items()):
        n_vcgs = len(sg_data.get("vcgs", []))
        n_verses = sum(len(v.get("verses", [])) for v in sg_data.get("vcgs", []))
        distinct = len(set(vc for v in sg_data.get("vcgs", []) for vc in v.get("verses", [])))
        expected_n = len(expected_by_sg.get(code, set()))
        print(f"  {code}: {n_vcgs} VCGs, {n_verses} member entries, {distinct} distinct vc_ids (expected {expected_n})")

    if errors:
        print(f"\nFAIL — {len(errors)} issues:")
        for e in errors:
            print(e)
        sys.exit(2)
    print(f"\nPASS — Phase B B.3 stage gate validated for cluster {args.cluster}")
    sys.exit(0)


if __name__ == "__main__":
    main()
