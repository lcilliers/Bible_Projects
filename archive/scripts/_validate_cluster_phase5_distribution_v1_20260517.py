"""Phase 5 sub-group distribution hard-gate validator.

Per v2_2 §8 amendment 2026-05-17: Phase 5 sub-group design must produce a
balanced sub-group structure. A single substantive sub-group holding more
than {MAX_SHARE_PCT}% of the cluster's substantive (non-BOUNDARY) verses
is rejected and AI must re-submit with finer-grained sub-group splits.

Input: AI's Phase 5 mapping JSON
  Sessions/Session_Clusters/{CODE}/files phase 5/WA-{CODE}-subgroup-mapping-v1-{date}.json

Output:
  Sessions/Session_Clusters/{CODE}/WA-{CODE}-phase5-distribution-validation-v1-{date}.md

Exit code:
  0 — PASS (no sub-group exceeds threshold; Phase 6 may proceed)
  2 — FAIL (gate trip; Phase 5 must be re-submitted by AI)
  1 — error (file not found, parse error, etc.)

Thresholds (rationale from closed-cluster benchmarks):
  Default: 40% — passes M01 (35%), M03 (33%); flags M02 (47%) and M04 (81%)
  Optional: 35% — also flags M01

Usage:
  python scripts/_validate_cluster_phase5_distribution_v1_20260517.py --cluster M04
  python scripts/_validate_cluster_phase5_distribution_v1_20260517.py --cluster M04 --max-share 35
  python scripts/_validate_cluster_phase5_distribution_v1_20260517.py --cluster M04 --mapping path/to/mapping.json
"""
from __future__ import annotations
import argparse, json, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
DEFAULT_MAX_SHARE_PCT = 40.0
DEFAULT_NEXT_RATIO_WARN = 3.0  # informational only, not a hard gate

# Closed-cluster benchmark (biggest substantive sub-group share)
BENCHMARKS = {"M01": 35, "M02": 47, "M03": 33}


def find_mapping(cluster: str) -> Path | None:
    """Look for the latest Phase 5 mapping JSON in the cluster's files-phase-5 folder
    or directly under the cluster directory."""
    base = REPO / "Sessions" / "Session_Clusters" / cluster
    candidates = list(base.glob("files phase 5/*subgroup-mapping*.json"))
    candidates += list(base.glob("*subgroup-mapping*.json"))
    if not candidates:
        return None
    # Most recent by mtime
    return max(candidates, key=lambda p: p.stat().st_mtime)


def compute_distribution(conn, cluster: str, mapping_json: Path) -> dict:
    doc = json.loads(mapping_json.read_text(encoding="utf-8"))
    mapping = doc["verse_assignments_by_term"]["mti_term_id_to_subgroup"]

    # Per-sub-group verse counts derived from mapping × DB is_relevant counts
    per_sg_verses: dict[str, int] = defaultdict(int)
    per_sg_terms: dict[str, int] = defaultdict(int)
    boundary_codes = set()
    for sg in doc.get("subgroups", []):
        if "BOUNDARY" in sg["subgroup_code"]:
            boundary_codes.add(sg["subgroup_code"])

    for mti_str, sg in mapping.items():
        mti = int(mti_str)
        r = conn.execute("""
            SELECT COUNT(*) AS n FROM verse_context
            WHERE mti_term_id=? AND is_relevant=1 AND COALESCE(delete_flagged,0)=0
        """, (mti,)).fetchone()
        per_sg_verses[sg] += r["n"]
        per_sg_terms[sg] += 1

    substantive_total = sum(v for sg, v in per_sg_verses.items() if sg not in boundary_codes)
    boundary_total = sum(v for sg, v in per_sg_verses.items() if sg in boundary_codes)

    rows = []
    for sg in sorted(per_sg_verses, key=lambda s: (-per_sg_verses[s], s)):
        is_boundary = sg in boundary_codes
        share = (per_sg_verses[sg] / substantive_total * 100) if (substantive_total > 0 and not is_boundary) else None
        rows.append({
            "sg": sg,
            "is_boundary": is_boundary,
            "terms": per_sg_terms[sg],
            "verses": per_sg_verses[sg],
            "share_substantive_pct": share,
        })
    return {
        "subgroups": rows,
        "substantive_total": substantive_total,
        "boundary_total": boundary_total,
        "cluster_code": cluster,
        "mapping_file": mapping_json,
    }


def grade(dist: dict, max_share_pct: float) -> dict:
    substantive = [r for r in dist["subgroups"] if not r["is_boundary"]]
    if not substantive:
        return {"verdict": "ERROR", "reasons": ["No substantive sub-groups in mapping."]}
    biggest = max(substantive, key=lambda r: r["verses"])
    next_biggest = sorted(substantive, key=lambda r: -r["verses"])[1] if len(substantive) > 1 else None
    ratio = (biggest["verses"] / max(1, next_biggest["verses"])) if next_biggest else None

    reasons = []
    if biggest["share_substantive_pct"] > max_share_pct:
        reasons.append(
            f"Biggest substantive sub-group {biggest['sg']} holds "
            f"{biggest['share_substantive_pct']:.1f}% of substantive verses "
            f"(threshold: {max_share_pct}%)."
        )
    if ratio is not None and ratio > DEFAULT_NEXT_RATIO_WARN:
        # Informational only; not a hard gate
        pass

    return {
        "verdict": "FAIL" if reasons else "PASS",
        "reasons": reasons,
        "biggest": biggest,
        "next_biggest": next_biggest,
        "ratio_biggest_to_next": ratio,
    }


def render_report(cluster: str, dist: dict, grading: dict, max_share_pct: float) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    verdict = grading["verdict"]
    lines = [
        f"# Phase 5 distribution validation — {cluster}",
        "",
        f"**Verdict:** {'✅ PASS — Phase 6 may proceed' if verdict == 'PASS' else '⛔ FAIL — Phase 5 must be re-submitted to AI for re-splitting'}",
        f"**Generated:** {now}",
        f"**Mapping file:** `{dist['mapping_file'].relative_to(REPO)}`",
        f"**Threshold:** any single substantive sub-group ≤ {max_share_pct}% of substantive corpus",
        "",
        "---",
        "",
        "## Sub-group distribution",
        "",
        "| Sub-group | Terms | Verses | % of substantive | Status |",
        "|---|---:|---:|---:|---|",
    ]
    for r in dist["subgroups"]:
        share = f"{r['share_substantive_pct']:.1f}%" if r["share_substantive_pct"] is not None else "—"
        status = "BOUNDARY (excluded)" if r["is_boundary"] else (
            "⛔ EXCEEDS THRESHOLD" if (r["share_substantive_pct"] is not None and r["share_substantive_pct"] > max_share_pct)
            else "ok"
        )
        lines.append(f"| `{r['sg']}` | {r['terms']} | {r['verses']} | {share} | {status} |")
    lines.append(f"| **TOTAL substantive** | | **{dist['substantive_total']}** | 100.0% | |")
    lines.append(f"| **TOTAL BOUNDARY** | | **{dist['boundary_total']}** | (excluded) | |")
    lines.append("")
    lines.append("## Diagnosis")
    lines.append("")
    if grading["biggest"]:
        b = grading["biggest"]
        lines.append(f"- Biggest substantive sub-group: **{b['sg']}** with **{b['verses']} verses** "
                     f"(**{b['share_substantive_pct']:.1f}%** of substantive)")
    if grading.get("next_biggest"):
        nb = grading["next_biggest"]
        lines.append(f"- Next biggest: {nb['sg']} with {nb['verses']} verses")
    if grading.get("ratio_biggest_to_next") is not None:
        lines.append(f"- Biggest-to-next ratio: **{grading['ratio_biggest_to_next']:.1f}×**")
    lines.append("")
    lines.append("## Benchmark — closed clusters under v2_2 methodology")
    lines.append("")
    lines.append("| Cluster | Biggest substantive SG share |")
    lines.append("|---|---:|")
    for c, p in BENCHMARKS.items():
        lines.append(f"| {c} | {p}% |")
    lines.append("")
    if verdict == "FAIL":
        lines.append("## Action required — Phase 5 resubmission")
        lines.append("")
        for r in grading["reasons"]:
            lines.append(f"- {r}")
        lines.append("")
        lines.append(
            f"Phase 5 sub-group design is rejected. AI must re-submit a revised sub-group "
            f"structure that splits the dominant sub-group(s) into finer-grained registers. "
            f"Phase 6 (CC apply) cannot proceed until validation passes."
        )
        lines.append("")
        lines.append("**Guidance for resubmission:** Read the dominant sub-group's term meanings "
                     "carefully and identify the natural register-splits — vertical vs horizontal, "
                     "divine vs human, communal vs individual, OT vs NT-distinctive, present vs "
                     "eschatological, righteous vs corrupt, etc. Each split that produces ≥10 "
                     "verses warrants its own sub-group.")
        lines.append("")
    else:
        lines.append("## Phase 6 readiness")
        lines.append("")
        lines.append("Phase 6 (CC apply sub-group routing) may proceed. The distribution is balanced "
                     "within the threshold envelope.")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*End of validation report.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True, help="Cluster code, e.g. M04")
    ap.add_argument("--mapping", help="Path to Phase 5 mapping JSON (auto-detect if omitted)")
    ap.add_argument("--max-share", type=float, default=DEFAULT_MAX_SHARE_PCT,
                    help=f"Max share of substantive corpus per sub-group (default: {DEFAULT_MAX_SHARE_PCT})")
    ap.add_argument("--out", help="Output report path (default: cluster directory)")
    args = ap.parse_args()

    cluster = args.cluster
    if args.mapping:
        mapping_path = Path(args.mapping)
    else:
        mapping_path = find_mapping(cluster)
        if not mapping_path:
            print(f"No Phase 5 mapping JSON found for {cluster}")
            sys.exit(1)

    if not mapping_path.exists():
        print(f"Mapping not found: {mapping_path}")
        sys.exit(1)

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    try:
        dist = compute_distribution(conn, cluster, mapping_path)
        grading = grade(dist, args.max_share)
        report = render_report(cluster, dist, grading, args.max_share)
    finally:
        conn.close()

    if args.out:
        out_path = Path(args.out)
    else:
        date = datetime.now(timezone.utc).strftime("%Y%m%d")
        out_dir = REPO / "Sessions" / "Session_Clusters" / cluster
        out_path = out_dir / f"WA-{cluster}-phase5-distribution-validation-v1-{date}.md"
    out_path.write_text(report, encoding="utf-8")

    print(f"\nWrote: {out_path.relative_to(REPO)}")
    print(f"\nVERDICT: {grading['verdict']}")
    for r in grading["reasons"]:
        print(f"  · {r}")

    sys.exit(0 if grading["verdict"] == "PASS" else 2)


if __name__ == "__main__":
    main()
