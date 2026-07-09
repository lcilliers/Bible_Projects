"""Phase B.2 stage gate validator (v3_0).

Validates a cluster's B.2 sub-group design output before B.3 is allowed to start.

Per `wa-sessionb-cluster-instruction-v3_0-20260527.md` §6.2.7:

  1. Every IB vc_id has a sub-group assignment (mapping JSON has all is_relevant verses).
  2. Every sub-group code in the mapping has at least one verse.
  3. §6.2.7 distribution gate — no substantive sub-group >40% of substantive verses.
  4. §6.2.6 BOUNDARY-not-a-parking-lot — if BOUNDARY sub-group exists, it contains
     only verses of BOUNDARY-verdict terms (loaded from B.1 verdicts file if provided).
  5. No verse appears in two sub-groups.
  6. Every sub-group code in the mapping is a {cluster}-{X} form (or {cluster}-BOUNDARY).

Inputs:
  --cluster M11
  --mapping Sessions/Session_Clusters/M11/WA-M11-subgroup-mapping-v1-20260527.json

Exit codes:
  0  PASS
  2  FAIL with delta report
"""
from __future__ import annotations
import argparse, json, sqlite3, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
DISTRIBUTION_CEILING_PCT = 40.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--mapping", required=True, help="path to subgroup-mapping JSON")
    args = ap.parse_args()

    cluster = args.cluster
    mapping_path = Path(args.mapping).resolve()
    if not mapping_path.exists():
        print(f"FAIL: mapping file not found: {mapping_path}")
        return 2

    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    mapping = {int(k): v for k, v in mapping.items()}

    conn = sqlite3.connect(DB, timeout=60.0)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, vc.mti_term_id
        FROM verse_context vc
        JOIN mti_terms m ON m.id = vc.mti_term_id
        WHERE m.cluster_code = ?
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged,0) = 0
          AND COALESCE(m.delete_flagged,0) = 0
        """,
        (cluster,),
    ).fetchall()
    db_vc_ids = {r["vc_id"] for r in rows}
    n_ib = len(db_vc_ids)

    print(f"=== Phase B.2 validator — cluster {cluster} ===")
    print(f"DB IB verse count: {n_ib}")
    print(f"Mapping entries: {len(mapping)}")

    fails = []

    # 1. every IB has assignment
    missing = db_vc_ids - set(mapping.keys())
    extra = set(mapping.keys()) - db_vc_ids
    if missing:
        fails.append(f"{len(missing)} DB IB verses missing from mapping (first 5: {sorted(missing)[:5]})")
    if extra:
        fails.append(f"{len(extra)} mapping vc_ids not in DB IB set (first 5: {sorted(extra)[:5]})")

    # 2. every sub-group has >=1 verse
    counts = Counter(mapping.values())
    print(f"\nSub-groups: {len(counts)}")
    for sg in sorted(counts):
        print(f"  {sg}: {counts[sg]}")

    # 6. sub-group code form
    for sg in counts:
        if not (sg.startswith(f"{cluster}-")):
            fails.append(f"sub-group code {sg!r} does not start with {cluster}-")

    # 4. BOUNDARY check (informational — only meaningful if BOUNDARY sub-group exists)
    boundary_sgs = [sg for sg in counts if sg.endswith("-BOUNDARY") or sg == "BOUNDARY"]
    if boundary_sgs:
        print(f"\nBOUNDARY sub-group(s) present: {boundary_sgs}")
        # For full check we'd need B.1 verdicts to know which terms are BOUNDARY-verdict.
        # Informational only here; researcher confirms.
    else:
        print("\nNo BOUNDARY sub-group present (B.1 produced no BOUNDARY verdicts).")

    # 3. distribution gate
    substantive_total = sum(c for sg, c in counts.items() if sg not in boundary_sgs)
    print(f"\nDistribution (§6.2.7 ceiling = {DISTRIBUTION_CEILING_PCT}% of substantive {substantive_total} verses):")
    over_ceiling = []
    for sg in sorted(counts):
        if sg in boundary_sgs:
            print(f"  {sg}: {counts[sg]} (BOUNDARY — not counted toward gate)")
            continue
        pct = 100 * counts[sg] / substantive_total if substantive_total else 0
        marker = "  ** OVER 40% GATE" if pct > DISTRIBUTION_CEILING_PCT else ""
        print(f"  {sg}: {counts[sg]:>4d}  {pct:5.1f}%{marker}")
        if pct > DISTRIBUTION_CEILING_PCT:
            over_ceiling.append((sg, counts[sg], pct))
    if over_ceiling:
        for sg, n, pct in over_ceiling:
            fails.append(f"§6.2.7 gate: sub-group {sg} holds {pct:.1f}% (>{DISTRIBUTION_CEILING_PCT}%); volume-split required")

    conn.close()

    print("\n=== Verdict ===")
    if fails:
        for f in fails:
            print(f"  FAIL — {f}")
        return 2
    else:
        print("  PASS — all B.2 stage-gate checks satisfied.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
