"""Generate a cluster-level keyword analytics report from verse_context.keywords.

Per the embedded-keyword methodology (2026-05-23): Phase 2 Pass A emits keywords
alongside the meaning into verse_context.keywords. This script reads those keywords
across all relevant verses in a cluster and produces an analytics report that goes
into the Phase 5 brief as a structural input — surfacing inner-being-faculty axes
emergent from the corpus before AI designs sub-groups.

Usage:
  python scripts/_generate_cluster_keyword_analytics_v1_20260523.py --cluster M10

Output:
  Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-keyword-analytics-v{N}-{YYYYMMDD}.md

Report contents:
  §1 Cluster summary (verse count, keyword count, distinct count, per-verse mean)
  §2 Top 50 keywords by frequency
  §3 Top 30 tokens (split keywords on whitespace) with sample keyword families
  §4 Top 40 within-verse co-occurrence pairs
  §5 Per-term keyword density (which terms dominate which token families)
  §6 Per-sub-group breakdowns (if sub-groups exist for the cluster)
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"


def next_version_for(out_dir: Path, prefix: str, date_str: str) -> str:
    pat = re.compile(rf"^{re.escape(prefix)}-v(\d+)-{date_str}\.md$")
    max_v = 0
    if out_dir.exists():
        for p in out_dir.iterdir():
            m = pat.match(p.name)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def fetch_cluster_verses(conn, cluster_code: str) -> list[dict]:
    rows = list(conn.execute("""
        SELECT vc.id AS vc_id, vc.keywords,
               vr.reference, vr.book_id, vr.chapter, vr.verse_num,
               mt.strongs_number, mt.transliteration, mt.gloss,
               cs.subgroup_code, cs.label AS subgroup_label
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE mt.cluster_code = ?
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND COALESCE(mt.delete_flagged, 0) = 0
          AND COALESCE(vr.delete_flagged, 0) = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (cluster_code,)))
    return [dict(r) for r in rows]


def parse_keywords(s: str | None) -> list[str]:
    if not s:
        return []
    try:
        v = json.loads(s)
        if isinstance(v, list):
            return [str(x).strip() for x in v if str(x).strip()]
    except (json.JSONDecodeError, TypeError):
        pass
    # Fall back to comma split (legacy / hand-loaded data)
    return [p.strip() for p in s.split(",") if p.strip()]


def analyse(verses: list[dict]) -> dict:
    all_kws: list[str] = []
    per_vc: dict[int, list[str]] = {}
    per_term: dict[str, list[str]] = defaultdict(list)  # by transliteration
    per_subgroup: dict[str, list[str]] = defaultdict(list)
    for v in verses:
        kws = parse_keywords(v.get("keywords"))
        per_vc[v["vc_id"]] = kws
        all_kws.extend(kws)
        per_term[v["transliteration"] or "?"].extend(kws)
        if v.get("subgroup_code"):
            per_subgroup[v["subgroup_code"]].extend(kws)

    kw_freq = Counter(all_kws)
    tok_freq = Counter()
    for kw in all_kws:
        for t in kw.split():
            tok_freq[t] += 1
    co_occ = Counter()
    for kws in per_vc.values():
        for a, b in combinations(sorted(set(kws)), 2):
            co_occ[(a, b)] += 1

    return {
        "n_verses": len(verses),
        "n_with_keywords": sum(1 for kws in per_vc.values() if kws),
        "n_keywords_total": len(all_kws),
        "n_keywords_distinct": len(kw_freq),
        "keyword_freq": kw_freq,
        "token_freq": tok_freq,
        "co_occurrence": co_occ,
        "per_term": per_term,
        "per_subgroup": per_subgroup,
    }


def token_families(token_freq: Counter, keyword_freq: Counter, top_n: int = 30) -> list[tuple]:
    """For each top token, list (token, total_occurrences, [keywords...])."""
    fams = []
    for tok, _ in token_freq.most_common(top_n):
        kws = sorted(
            [(kw, n) for kw, n in keyword_freq.items() if tok in kw.split()],
            key=lambda x: -x[1],
        )
        fams.append((tok, sum(n for _, n in kws), kws))
    return fams


def write_report(cluster_code: str, description: str, analysis: dict, out_path: Path) -> None:
    a = analysis
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {description} — Keyword analytics report")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}")
    lines.append(f"**Cluster:** `{cluster_code}` ({description})")
    lines.append("**Source:** `verse_context.keywords` (Phase 2 Pass A or backfilled)")
    lines.append("")
    lines.append("**Purpose:** structural input for Phase 5 sub-group design. Surfaces inner-being-faculty axes emergent from the verse-meaning corpus (which the AI tagged with atomic keywords during Pass A). AI uses this report alongside the meanings to design characteristic-aligned sub-groups.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # §1 Summary
    lines.append("## §1. Summary")
    lines.append("")
    lines.append(f"- is_relevant verses in cluster: **{a['n_verses']}**")
    lines.append(f"- Verses with keywords: **{a['n_with_keywords']}** ({a['n_with_keywords'] * 100.0 / max(a['n_verses'], 1):.1f}%)")
    if a['n_with_keywords'] < a['n_verses']:
        lines.append(f"  - *Note: {a['n_verses'] - a['n_with_keywords']} verses lack keywords (Pass A pre-embedding or unbackfilled).*")
    lines.append(f"- Total keywords: {a['n_keywords_total']}")
    lines.append(f"- Distinct keywords: {a['n_keywords_distinct']}")
    lines.append(f"- Mean keywords per verse: {a['n_keywords_total'] / max(a['n_verses'], 1):.2f}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # §2 Top 50 keywords
    lines.append("## §2. Top 50 keywords by frequency")
    lines.append("")
    lines.append("| Count | Keyword |")
    lines.append("|---:|---|")
    for kw, n in a["keyword_freq"].most_common(50):
        lines.append(f"| {n} | {kw} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # §3 Top 30 tokens
    lines.append("## §3. Top 30 tokens (faculty-axis indicators)")
    lines.append("")
    lines.append("Each token below appears across multiple keywords — a high-count token typically names an inner-being faculty axis (e.g. `conscience`, `will`, `defection`).")
    lines.append("")
    lines.append("| Count | Token | Sample keyword families (top 10 by freq) |")
    lines.append("|---:|---|---|")
    for tok, total, kws in token_families(a["token_freq"], a["keyword_freq"], top_n=30):
        sample = ", ".join(f"{kw} ({n})" for kw, n in kws[:10])
        lines.append(f"| {a['token_freq'][tok]} | **{tok}** | {sample} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # §4 Co-occurrence pairs
    lines.append("## §4. Top 40 within-verse co-occurrence pairs")
    lines.append("")
    lines.append("Keyword pairs that co-occur in the same verse — these are direct evidence of which faculty axes operate together.")
    lines.append("")
    lines.append("| Co-occ | A | B |")
    lines.append("|---:|---|---|")
    for (a_kw, b_kw), n in a["co_occurrence"].most_common(40):
        lines.append(f"| {n} | {a_kw} | {b_kw} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # §5 Per-term density
    lines.append("## §5. Per-term keyword density (top 15 terms by verse count)")
    lines.append("")
    lines.append("Which terms drive which faculty axes? Higher density means the term's verses repeatedly evidence that keyword family.")
    lines.append("")
    term_sizes = Counter({k: len(v) for k, v in a["per_term"].items()})
    for translit, _n in term_sizes.most_common(15):
        kws = Counter(a["per_term"][translit])
        lines.append(f"### {translit} — {sum(kws.values())} keywords across this term's verses")
        lines.append("")
        lines.append("| Count | Keyword |")
        lines.append("|---:|---|")
        for kw, n in kws.most_common(10):
            lines.append(f"| {n} | {kw} |")
        lines.append("")

    lines.append("---")
    lines.append("")

    # §6 Per-sub-group breakdown (if sub-groups exist)
    if a["per_subgroup"]:
        lines.append("## §6. Per-sub-group top keywords")
        lines.append("")
        lines.append("If Phase 6 has already routed verses to sub-groups, the keyword distribution per sub-group should validate the characteristic claims.")
        lines.append("")
        for sg_code in sorted(a["per_subgroup"].keys()):
            kws_in_sg = a["per_subgroup"][sg_code]
            sg_freq = Counter(kws_in_sg)
            lines.append(f"### {sg_code} — {len(kws_in_sg)} keywords across the sub-group")
            lines.append("")
            lines.append("| Count | Keyword |")
            lines.append("|---:|---|")
            for kw, n in sg_freq.most_common(15):
                lines.append(f"| {n} | {kw} |")
            lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("*End of report.*")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    args = ap.parse_args()

    cluster = args.cluster.strip()
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    try:
        cluster_row = conn.execute(
            "SELECT description FROM cluster WHERE cluster_code=?", (cluster,)
        ).fetchone()
        if not cluster_row:
            raise SystemExit(f"cluster {cluster} not found")
        description = cluster_row["description"]

        verses = fetch_cluster_verses(conn, cluster)
        analysis = analyse(verses)
    finally:
        conn.close()

    out_dir = REPO / "Sessions" / "Session_Clusters" / cluster
    out_dir.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
    version = next_version_for(out_dir, f"wa-cluster-{cluster}-keyword-analytics", date_str)
    out_path = out_dir / f"wa-cluster-{cluster}-keyword-analytics-{version}-{date_str}.md"
    write_report(cluster, description, analysis, out_path)

    print(f"Cluster {cluster}: {analysis['n_verses']} verses, "
          f"{analysis['n_with_keywords']} with keywords, "
          f"{analysis['n_keywords_distinct']} distinct keywords")
    print(f"Wrote: {out_path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
