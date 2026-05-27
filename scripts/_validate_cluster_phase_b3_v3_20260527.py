"""Phase B.3 stage gate validator (v3_0).

Validates a cluster's B.3 unified VCG creation JSON before Phase C apply.

Per `wa-sessionb-cluster-instruction-v3_0-20260527.md` §6.3.5 + §6.3.6:

  1. Every vc_id in JSON exists in verse_context with is_relevant=1,
     delete_flagged=0, and belongs to cluster's term set.
  2. No vc_id appears in two VCGs (unless explicitly flagged dual-membership).
  3. Sum of verses per sub-group equals the B.2 mapping's per-sub-group count.
  4. Every anchor_vc_id is in its VCG's verses array.
  5. Field name must be 'verses' (not 'key_verses', 'members', etc.).
  6. Total verses across whole cluster equals cluster's IB count.
  7. Every VCG has provisional_code, description, verses, anchor_vc_id.

Inputs:
  --cluster M11
  --vcg-json Sessions/Session_Clusters/M11/WA-M11-vcg-creation-v1-20260527.json
  --mapping Sessions/Session_Clusters/M11/WA-M11-subgroup-mapping-v1-20260527.json

Exit codes:
  0  PASS
  2  FAIL with delta report
"""
from __future__ import annotations
import argparse, io, json, sqlite3, sys
from collections import Counter, defaultdict
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--vcg-json", required=True)
    ap.add_argument("--mapping", required=True)
    args = ap.parse_args()

    cluster = args.cluster
    vcg_path = Path(args.vcg_json).resolve()
    mapping_path = Path(args.mapping).resolve()

    if not vcg_path.exists() or not mapping_path.exists():
        print("FAIL: input file(s) missing")
        return 2

    vcg_data = json.loads(vcg_path.read_text(encoding="utf-8"))
    mapping = {int(k): v for k, v in json.loads(mapping_path.read_text(encoding="utf-8")).items()}

    print(f"=== Phase B.3 validator — cluster {cluster} ===")

    fails: list[str] = []

    # DB cluster IB set
    conn = sqlite3.connect(DB, timeout=60.0)
    conn.row_factory = sqlite3.Row
    db_rows = conn.execute(
        """
        SELECT vc.id AS vc_id
        FROM verse_context vc
        JOIN mti_terms m ON m.id = vc.mti_term_id
        WHERE m.cluster_code = ?
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged,0) = 0
          AND COALESCE(m.delete_flagged,0) = 0
        """,
        (cluster,),
    ).fetchall()
    db_ib_ids = {r["vc_id"] for r in db_rows}
    print(f"DB IB verse count: {len(db_ib_ids)}")
    conn.close()

    # Walk VCG JSON
    all_vc_ids: list[int] = []
    vc_to_vcgs: defaultdict[int, list[str]] = defaultdict(list)
    sg_counts: Counter = Counter()

    sub_group_codes_in_mapping = set(mapping.values())
    sub_group_codes_in_vcg_json = set(vcg_data.keys())

    if sub_group_codes_in_mapping != sub_group_codes_in_vcg_json:
        missing = sub_group_codes_in_mapping - sub_group_codes_in_vcg_json
        extra = sub_group_codes_in_vcg_json - sub_group_codes_in_mapping
        if missing:
            fails.append(f"sub-groups in mapping but not in VCG JSON: {sorted(missing)}")
        if extra:
            fails.append(f"sub-groups in VCG JSON but not in mapping: {sorted(extra)}")

    n_vcgs = 0
    for sg_code, vcgs in vcg_data.items():
        for vcg_code, vcg in vcgs.items():
            n_vcgs += 1
            # 5. Field name check
            if "verses" not in vcg:
                fails.append(f"{vcg_code}: missing 'verses' field")
                continue
            for forbidden in ("key_verses", "members", "sample_verses"):
                if forbidden in vcg:
                    fails.append(f"{vcg_code}: forbidden field name {forbidden!r} present")

            # 7. Required fields
            for field in ("description", "verses", "anchor_vc_id"):
                if field not in vcg:
                    fails.append(f"{vcg_code}: missing required field {field!r}")

            verses = vcg.get("verses", [])
            anchor = vcg.get("anchor_vc_id")

            # 4. anchor in verses
            if anchor is not None and anchor not in verses:
                fails.append(f"{vcg_code}: anchor_vc_id={anchor} not in verses array")

            for vc_id in verses:
                all_vc_ids.append(vc_id)
                vc_to_vcgs[vc_id].append(vcg_code)
                sg_counts[sg_code] += 1

    print(f"\nVCGs total: {n_vcgs}")
    print(f"vc_ids in VCG JSON: {len(all_vc_ids)} (unique: {len(set(all_vc_ids))})")

    # 1. existence in DB cluster IB set
    json_set = set(all_vc_ids)
    missing_db = json_set - db_ib_ids
    extra_db = db_ib_ids - json_set
    if missing_db:
        fails.append(f"{len(missing_db)} vc_ids in VCG JSON not in DB cluster IB set (first 5: {sorted(missing_db)[:5]})")
    if extra_db:
        fails.append(f"{len(extra_db)} DB IB vc_ids missing from VCG JSON (first 5: {sorted(extra_db)[:5]})")

    # 2. duplicates across VCGs
    dups = {vc_id: vcgs for vc_id, vcgs in vc_to_vcgs.items() if len(vcgs) > 1}
    if dups:
        for vc_id, vcgs in list(dups.items())[:5]:
            fails.append(f"vc_id={vc_id} appears in multiple VCGs: {vcgs}")

    # 3. per-sub-group sum vs B.2 mapping
    mapping_sg_counts = Counter(mapping.values())
    print(f"\nPer-sub-group sums (VCG JSON vs B.2 mapping):")
    for sg in sorted(set(mapping_sg_counts) | set(sg_counts)):
        a, b = sg_counts[sg], mapping_sg_counts[sg]
        ok = "OK" if a == b else "**MISMATCH**"
        print(f"  {sg}: VCG sum={a}, mapping={b}  {ok}")
        if a != b:
            fails.append(f"{sg}: VCG sum {a} != mapping count {b}")

    # 6. cluster total
    if len(all_vc_ids) != len(db_ib_ids):
        fails.append(f"Total VCG-JSON vc_ids ({len(all_vc_ids)}) != DB IB total ({len(db_ib_ids)})")

    print("\n=== Verdict ===")
    if fails:
        for f in fails:
            print(f"  FAIL — {f}")
        return 2
    else:
        print(f"  PASS — all B.3 stage-gate checks satisfied for {n_vcgs} VCGs / {len(all_vc_ids)} vc_ids.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
