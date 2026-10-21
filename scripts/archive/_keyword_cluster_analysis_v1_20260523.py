"""Stage 2 keyword clustering analysis for the discovery pass.

Reads the per-sub-group keyword JSONs and produces:
- Top-frequency keywords per sub-group
- Token frequency (split two-word combos into their constituent words)
- Co-occurrence pairs (which keywords appear together in the same verse)
- Candidate faculty axes (keyword families that cluster together)

Output: a single markdown comparison report written to the cluster's files-phase-5 folder.

Usage:
  python scripts/_keyword_cluster_analysis_v1_20260523.py --cluster M10 --subgroups M10-A M10-B M10-F
"""
from __future__ import annotations
import argparse
import io
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent


def load_subgroup(cluster: str, sg: str, date_str: str) -> dict:
    p = (REPO / "Sessions" / "Session_Clusters" / cluster / "files phase 5" /
         f"wa-cluster-{cluster}-{sg.replace(cluster + '-', '', 1)}-keywords-v1-{date_str}.json")
    if not p.exists():
        # Try with full subgroup code
        p = (REPO / "Sessions" / "Session_Clusters" / cluster / "files phase 5" /
             f"wa-cluster-{cluster}-{sg.replace(cluster + '-', '')}-keywords-v1-{date_str}.json")
    return json.loads(p.read_text(encoding="utf-8"))


def analyse(data: dict) -> dict:
    """Frequency + token + co-occurrence analysis."""
    all_kws: list[str] = []
    per_verse_kws: dict[str, list[str]] = {}
    for vc_id, info in data["keywords_by_vc_id"].items():
        kws = info.get("keywords") or []
        per_verse_kws[vc_id] = kws
        all_kws.extend(kws)
    n_verses = len(per_verse_kws)
    n_kws = len(all_kws)

    keyword_freq = Counter(all_kws)
    # Token frequency
    token_freq = Counter()
    for kw in all_kws:
        for tok in kw.split():
            token_freq[tok] += 1
    # Co-occurrence
    co_occ = Counter()
    for kws in per_verse_kws.values():
        for a, b in combinations(sorted(set(kws)), 2):
            co_occ[(a, b)] += 1

    return {
        "n_verses": n_verses,
        "n_keywords_total": n_kws,
        "n_keywords_distinct": len(keyword_freq),
        "keyword_freq": keyword_freq,
        "token_freq": token_freq,
        "co_occurrence": co_occ,
    }


def family_clusters(token_freq: Counter, top_token_count: int = 25,
                     keyword_freq: Counter | None = None) -> list[tuple[str, list[str], int]]:
    """For each top token, list keywords containing it and total occurrences.

    Returns list of (token, [keyword, ...], total_occurrences).
    """
    top_tokens = [t for t, _ in token_freq.most_common(top_token_count)]
    families: list[tuple[str, list[str], int]] = []
    for tok in top_tokens:
        if keyword_freq is None:
            continue
        kws = sorted(
            [(kw, n) for kw, n in keyword_freq.items() if tok in kw.split()],
            key=lambda x: -x[1],
        )
        total = sum(n for _, n in kws)
        families.append((tok, [f"{kw} ({n})" for kw, n in kws[:12]], total))
    families.sort(key=lambda x: -x[2])
    return families


def write_report(cluster: str, sgs: list[str], analyses: dict[str, dict], out_path: Path) -> None:
    lines = [
        f"# {cluster} keyword discovery — cross-subgroup analysis",
        "",
        f"Sub-groups analysed: {', '.join(sgs)}",
        "",
        "---",
        "",
    ]
    for sg in sgs:
        a = analyses[sg]
        lines.append(f"## {sg}")
        lines.append("")
        lines.append(f"- Verses: **{a['n_verses']}**")
        lines.append(f"- Keywords (total): {a['n_keywords_total']}")
        lines.append(f"- Distinct keywords: {a['n_keywords_distinct']}")
        lines.append(f"- Keywords per verse: {a['n_keywords_total'] / a['n_verses']:.2f}")
        lines.append("")
        lines.append("### Top 30 keywords by frequency")
        lines.append("")
        lines.append("| Count | Keyword |")
        lines.append("|---:|---|")
        for kw, n in a["keyword_freq"].most_common(30):
            lines.append(f"| {n} | {kw} |")
        lines.append("")
        lines.append("### Top 25 tokens (across all keywords)")
        lines.append("")
        lines.append("| Count | Token | Sample keyword families |")
        lines.append("|---:|---|---|")
        fams = family_clusters(a["token_freq"], 25, a["keyword_freq"])
        for tok, kws, total in fams:
            sample = ", ".join(kws[:6])
            lines.append(f"| {a['token_freq'][tok]} | **{tok}** | {sample} |")
        lines.append("")
        lines.append("### Top 25 co-occurrence pairs (within a single verse)")
        lines.append("")
        lines.append("| Co-occ | A | B |")
        lines.append("|---:|---|---|")
        for (a_kw, b_kw), n in a["co_occurrence"].most_common(25):
            lines.append(f"| {n} | {a_kw} | {b_kw} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--subgroups", nargs="+", required=True)
    ap.add_argument("--date", default="20260523")
    args = ap.parse_args()

    analyses: dict[str, dict] = {}
    for sg in args.subgroups:
        data = load_subgroup(args.cluster, sg, args.date)
        analyses[sg] = analyse(data)
        print(f"{sg}: {analyses[sg]['n_verses']} verses, "
              f"{analyses[sg]['n_keywords_distinct']} distinct keywords")

    out_dir = REPO / "Sessions" / "Session_Clusters" / args.cluster / "files phase 5"
    out_path = out_dir / f"wa-cluster-{args.cluster}-keyword-analysis-v1-{args.date}.md"
    write_report(args.cluster, args.subgroups, analyses, out_path)
    print(f"\nWrote: {out_path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
