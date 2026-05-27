"""Generic 1:1 characteristic backfill for pre-v2_6 closed clusters.

Per researcher direction 2026-05-27: 9 remaining pre-v2_6 closed clusters
(M01, M02, M05, M06, M15, M20, M26, M39, M46) need characteristic mapping.
"Workable, not perfect" — auto-derive 1:1 from existing sub-group structure.

For each cluster:
  1. Read substantive sub-groups (excluding *-BOUNDARY)
  2. Insert one characteristic row per sub-group, using:
       short_name  = sub-group.label
       definition  = sub-group.core_description
       char_seq    = sub-group.sort_order (preserves ordering)
  3. Insert 1:1 characteristic_subgroup link (is_partial=0)
  4. Backfill cluster_finding.characteristic_id for findings tied to
     each substantive sub-group

Skips clusters already populated (idempotent at cluster grain).
Aborts cluster if it has any existing characteristic rows.

Operations are per-cluster transactions. A failure in one cluster
aborts that cluster only; others proceed.

Usage:
    python scripts/_apply_generic_characteristic_backfill_20260527.py --cluster M01
    python scripts/_apply_generic_characteristic_backfill_20260527.py --clusters M01,M02,M05
    python scripts/_apply_generic_characteristic_backfill_20260527.py --all     # M01,M02,M05,M06,M15,M20,M26,M39,M46
"""
from __future__ import annotations
import argparse, io, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SOURCE = "Pre-v2_6 characteristic backfill 2026-05-27 — 1:1 from sub-group structure"

ALL_CLUSTERS = ["M01", "M02", "M05", "M06", "M15", "M20", "M26", "M39", "M46"]


def is_boundary_subgroup(code: str) -> bool:
    # Two conventions seen across pre-v2_6 clusters:
    #   - "{CLUSTER}-BOUNDARY" (e.g. "M01-BOUNDARY")
    #   - bare "BOUNDARY" (e.g. M06, M15)
    return code.endswith("-BOUNDARY") or code == "BOUNDARY"


def backfill_one_cluster(conn, cluster: str, live: bool) -> dict:
    """Run backfill for one cluster. Returns summary dict."""
    cur = conn.cursor()

    # Pre-check: no existing characteristics
    n_existing = cur.execute(
        "SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (cluster,),
    ).fetchone()[0]
    if n_existing:
        return {"cluster": cluster, "skipped": True, "reason": f"already has {n_existing} characteristic rows"}

    # Substantive sub-groups (exclude BOUNDARY), in sort_order
    sgs = cur.execute(
        "SELECT id, subgroup_code, label, core_description, sort_order "
        "FROM cluster_subgroup "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        "ORDER BY sort_order, subgroup_code",
        (cluster,),
    ).fetchall()
    substantive = [r for r in sgs if not is_boundary_subgroup(r[1])]
    if not substantive:
        return {"cluster": cluster, "skipped": True, "reason": "no substantive sub-groups (only BOUNDARY)"}

    print(f"\n=== {cluster} ===")
    print(f"  Substantive sub-groups: {len(substantive)} (skipping {len(sgs) - len(substantive)} BOUNDARY)")

    plan = []
    for seq_pos, sg in enumerate(substantive, start=1):
        # Use position-in-substantive-list as char_seq for stable ordering
        n_findings = cur.execute(
            "SELECT COUNT(*) FROM cluster_finding "
            "WHERE cluster_code=? AND cluster_subgroup_id=? AND characteristic_id IS NULL "
            "AND COALESCE(delete_flagged,0)=0",
            (cluster, sg[0]),
        ).fetchone()[0]
        plan.append({
            "char_seq": seq_pos,
            "short_name": (sg[2] or sg[1]),
            "subgroup_id": sg[0],
            "subgroup_code": sg[1],
            "definition": sg[3] or sg[2] or sg[1],
            "n_findings": n_findings,
        })
        print(f"    char_seq={seq_pos} ← {sg[1]} ({n_findings} findings) — {(sg[2] or sg[1])}")

    if not live:
        return {"cluster": cluster, "planned": len(plan), "findings_to_link": sum(p["n_findings"] for p in plan)}

    # Apply
    char_id_by_seq = {}
    for p in plan:
        cur.execute(
            "INSERT INTO characteristic "
            "(cluster_code, char_seq, short_name, definition, source, version, "
            " delete_flagged, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, 'v1', 0, ?, ?)",
            (cluster, p["char_seq"], p["short_name"], p["definition"], SOURCE, NOW, NOW),
        )
        char_id_by_seq[p["char_seq"]] = cur.lastrowid
    for p in plan:
        cur.execute(
            "INSERT INTO characteristic_subgroup "
            "(characteristic_id, cluster_subgroup_id, qualifier_note, is_partial, "
            " delete_flagged, created_at, last_updated_date) "
            "VALUES (?, ?, ?, 0, 0, ?, ?)",
            (char_id_by_seq[p["char_seq"]], p["subgroup_id"],
             f"1:1 mapping from {cluster} sub-group {p['subgroup_code']} (Pre-v2_6 backfill)",
             NOW, NOW),
        )
    n_findings_total = 0
    for p in plan:
        cur.execute(
            "UPDATE cluster_finding SET characteristic_id=?, last_updated_date=? "
            "WHERE cluster_code=? AND cluster_subgroup_id=? AND characteristic_id IS NULL "
            "AND COALESCE(delete_flagged,0)=0",
            (char_id_by_seq[p["char_seq"]], NOW, cluster, p["subgroup_id"]),
        )
        n_findings_total += cur.rowcount
    return {
        "cluster": cluster,
        "chars_inserted": len(plan),
        "findings_backfilled": n_findings_total,
        "subgroups_mapped": [p["subgroup_code"] for p in plan],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--cluster", help="Single cluster code")
    g.add_argument("--clusters", help="Comma-separated cluster codes")
    g.add_argument("--all", action="store_true", help=f"Process all 9 ({','.join(ALL_CLUSTERS)})")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    if args.all:
        clusters = ALL_CLUSTERS
    elif args.clusters:
        clusters = [c.strip() for c in args.clusters.split(",")]
    else:
        clusters = [args.cluster]

    print(f"=== Generic characteristic backfill — mode={'LIVE' if args.live else 'DRY-RUN'} ===")
    print(f"Clusters: {clusters}")

    conn = sqlite3.connect(DB, timeout=120.0)
    conn.execute("PRAGMA busy_timeout = 120000")

    results = []
    for cluster in clusters:
        if args.live:
            conn.execute("BEGIN IMMEDIATE")
            try:
                r = backfill_one_cluster(conn, cluster, live=True)
                conn.commit()
                results.append(r)
                if not r.get("skipped"):
                    print(f"  COMMITTED: {r['chars_inserted']} chars, {r['findings_backfilled']} findings backfilled")
            except Exception as e:
                conn.rollback()
                print(f"  ROLLED BACK ({cluster}): {e}")
                results.append({"cluster": cluster, "error": str(e)})
        else:
            r = backfill_one_cluster(conn, cluster, live=False)
            results.append(r)

    print(f"\n=== Summary ===")
    total_chars = 0
    total_findings = 0
    for r in results:
        if r.get("skipped"):
            print(f"  {r['cluster']:5s} SKIPPED: {r['reason']}")
        elif r.get("error"):
            print(f"  {r['cluster']:5s} ERROR: {r['error']}")
        elif args.live:
            print(f"  {r['cluster']:5s} OK: {r['chars_inserted']} chars, {r['findings_backfilled']} findings")
            total_chars += r["chars_inserted"]
            total_findings += r["findings_backfilled"]
        else:
            print(f"  {r['cluster']:5s} planned: {r['planned']} chars, {r['findings_to_link']} findings")
            total_chars += r["planned"]
            total_findings += r["findings_to_link"]

    if args.live:
        print(f"\nTOTAL: {total_chars} characteristics inserted, {total_findings} findings backfilled")
    else:
        print(f"\nTOTAL (planned): {total_chars} characteristics, {total_findings} findings")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
