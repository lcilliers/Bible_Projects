"""_exploratory_term_cluster_quality_v1_20260504.py — read-only.

Per-cluster quality assessment + selective sub-clustering for loose clusters.

Premise: cluster quality isn't homogeneous. Some clusters are tight enough
to lock in as analytical units. Others (typically the larger ones) are
loose and need a second pass with finer granularity.

Quality metrics per cluster:
  - n: cluster size
  - cohesion: mean cosine similarity of members to centroid (higher = tighter)
  - theme_concentration: top-1 theme word frequency / cluster size
  - dispersion: std dev of member-to-centroid distance

Classification:
  - TIGHT     — cohesion >= 0.60 OR (n <= 12 AND cohesion >= 0.50)
  - MODERATE  — between
  - LOOSE     — cohesion < 0.45 OR (n >= 30 AND cohesion < 0.55)

For LOOSE clusters, run a second-pass k-means within just that cluster's
members at k_sub = max(2, n // 10). Sub-clusters get their own quality
score so the user can see whether the second pass actually tightens.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def load_npz(path):
    arr = np.load(path, allow_pickle=False)
    return arr["strongs"], arr["vectors"]


def cluster_kmeans(vectors, k, seed=20260504):
    from sklearn.cluster import KMeans
    return KMeans(n_clusters=k, random_state=seed, n_init=10).fit_predict(vectors)


TOKEN_RE = re.compile(r"[a-z]+")
THEME_STOPWORDS = {
    "a", "an", "the", "to", "of", "in", "on", "with", "for", "by", "at",
    "be", "is", "was", "are", "were", "am", "been", "being",
    "like", "as", "that", "this", "those", "these", "it", "its",
    "do", "does", "did", "doing", "done",
    "have", "has", "had", "having",
    "or", "and", "but", "if", "than", "then", "so",
    "from", "into", "onto", "upon", "out", "off", "up", "down",
    "one", "two", "three", "many", "all", "some", "every",
    "self", "his", "her", "my", "your", "our", "their", "him",
}


def gloss_tokens(gloss):
    if not gloss:
        return []
    g = gloss.lower().split(":")[0]
    return [t for t in TOKEN_RE.findall(g)
            if t not in THEME_STOPWORDS and len(t) > 2]


def cluster_quality(cluster_strongs, vectors, idx_map, term_meta):
    """Compute quality metrics for a cluster."""
    indices = [idx_map[s] for s in cluster_strongs if s in idx_map]
    if len(indices) < 2:
        return {
            "n": len(cluster_strongs),
            "cohesion": 1.0 if len(indices) == 1 else 0.0,
            "theme_concentration": 0.0,
            "dispersion": 0.0,
        }
    v = vectors[indices]
    centroid = v.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = v @ centroid
    cohesion = float(sims.mean())
    dispersion = float(sims.std())
    # Theme concentration: top-1 theme word freq / cluster size
    counter = Counter()
    for s in cluster_strongs:
        for t in gloss_tokens((term_meta.get(s) or {}).get("gloss") or ""):
            counter[t] += 1
    if counter:
        top_count = counter.most_common(1)[0][1]
        theme_conc = top_count / len(cluster_strongs)
    else:
        theme_conc = 0.0
    return {
        "n": len(cluster_strongs),
        "cohesion": round(cohesion, 4),
        "dispersion": round(dispersion, 4),
        "theme_concentration": round(theme_conc, 4),
    }


def classify_quality(metrics):
    n = metrics["n"]
    coh = metrics["cohesion"]
    if coh >= 0.60 or (n <= 12 and coh >= 0.50):
        return "TIGHT"
    if coh < 0.45 or (n >= 30 and coh < 0.55):
        return "LOOSE"
    return "MODERATE"


def cluster_centroid_term(strongs, vectors, idx_map):
    indices = [idx_map[s] for s in strongs if s in idx_map]
    if not indices:
        return None
    v = vectors[indices]
    centroid = v.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = v @ centroid
    return strongs[int(np.argmax(sims))]


def cluster_theme(strongs, term_meta):
    counter = Counter()
    for s in strongs:
        for t in gloss_tokens((term_meta.get(s) or {}).get("gloss") or ""):
            counter[t] += 1
    return counter.most_common(10)


def assess_pool(cluster_terms, vectors, idx_map, term_meta, sub_size_divisor=10):
    """Run quality assessment on all clusters in a pool. For LOOSE clusters,
    run sub-k-means and return sub-cluster info."""
    by_cluster = defaultdict(list)
    for entry in cluster_terms:
        by_cluster[int(entry["cluster"])].append(entry["strong"])

    assessment = []
    for cid in sorted(by_cluster.keys()):
        members = by_cluster[cid]
        metrics = cluster_quality(members, vectors, idx_map, term_meta)
        quality = classify_quality(metrics)
        theme = cluster_theme(members, term_meta)
        centroid = cluster_centroid_term(members, vectors, idx_map)
        centroid_gloss = ((term_meta.get(centroid) or {}).get("gloss") or "") if centroid else ""

        entry = {
            "cluster": cid,
            "members": members,
            "metrics": metrics,
            "quality": quality,
            "theme": theme,
            "centroid": centroid,
            "centroid_gloss": centroid_gloss,
            "sub_clusters": None,
        }

        # Sub-cluster if LOOSE and big enough
        if quality == "LOOSE" and len(members) >= 8:
            k_sub = max(2, len(members) // sub_size_divisor)
            indices = [idx_map[s] for s in members if s in idx_map]
            if len(indices) >= k_sub:
                sub_labels = cluster_kmeans(vectors[indices], k_sub)
                sub_by = defaultdict(list)
                for s, lbl in zip(members, sub_labels):
                    sub_by[int(lbl)].append(s)
                sub_list = []
                for sub_cid in sorted(sub_by):
                    sub_members = sub_by[sub_cid]
                    sub_metrics = cluster_quality(sub_members, vectors, idx_map, term_meta)
                    sub_theme = cluster_theme(sub_members, term_meta)
                    sub_centroid = cluster_centroid_term(sub_members, vectors, idx_map)
                    sub_centroid_gloss = (
                        (term_meta.get(sub_centroid) or {}).get("gloss") or ""
                        if sub_centroid else ""
                    )
                    sub_list.append({
                        "sub_cluster": sub_cid,
                        "members": sub_members,
                        "metrics": sub_metrics,
                        "quality": classify_quality(sub_metrics),
                        "theme": sub_theme,
                        "centroid": sub_centroid,
                        "centroid_gloss": sub_centroid_gloss,
                    })
                entry["sub_clusters"] = sub_list
                entry["k_sub"] = k_sub
        assessment.append(entry)
    return assessment


def render_md(title, assessment, term_meta):
    # Group by quality
    by_q = defaultdict(list)
    for a in assessment:
        by_q[a["quality"]].append(a)
    lines = [f"# {title}", "",
             f"**Generated:** {now_iso()}",
             f"**Total clusters:** {len(assessment)}",
             f"**TIGHT:** {len(by_q['TIGHT'])} · "
             f"**MODERATE:** {len(by_q['MODERATE'])} · "
             f"**LOOSE:** {len(by_q['LOOSE'])}",
             ""]

    # Quality summary table
    lines.append("## Quality summary table")
    lines.append("")
    lines.append("| cluster | n | quality | cohesion | theme% | top theme word | centroid term |")
    lines.append("|---|---|---|---|---|---|---|")
    for a in sorted(assessment, key=lambda x: (x["quality"], -x["metrics"]["n"])):
        top_theme = a["theme"][0] if a["theme"] else ("—", 0)
        c = a["centroid"] or ""
        m = (term_meta.get(c) or {}) if c else {}
        cg = (m.get("gloss") or "")[:30]
        lines.append(
            f"| {a['cluster']} | {a['metrics']['n']} | **{a['quality']}** | "
            f"{a['metrics']['cohesion']} | "
            f"{int(a['metrics']['theme_concentration']*100)}% | "
            f"{top_theme[0]}({top_theme[1]}) | "
            f"`{c}` {cg} |"
        )
    lines.append("")

    # Per-quality sections
    for q_label in ["TIGHT", "MODERATE", "LOOSE"]:
        lines.append(f"## {q_label} clusters ({len(by_q[q_label])})")
        lines.append("")
        for a in sorted(by_q[q_label], key=lambda x: -x["metrics"]["n"]):
            lines.append(
                f"### Cluster {a['cluster']} — {a['metrics']['n']} term(s) · "
                f"cohesion {a['metrics']['cohesion']} · "
                f"theme {int(a['metrics']['theme_concentration']*100)}%"
            )
            lines.append("")
            theme_str = ", ".join(f"{w}({c})" for w, c in a["theme"][:8])
            lines.append(f"**Theme:** {theme_str}")
            lines.append("")
            if a["centroid"]:
                lines.append(f"**Centroid:** `{a['centroid']}` — {a['centroid_gloss']}")
                lines.append("")

            if q_label == "LOOSE" and a.get("sub_clusters"):
                lines.append(f"**Sub-clustering at k_sub={a['k_sub']}:**")
                lines.append("")
                lines.append("| sub | n | quality | cohesion | theme | centroid |")
                lines.append("|---|---|---|---|---|---|")
                for sub in a["sub_clusters"]:
                    sub_top = sub["theme"][0] if sub["theme"] else ("—", 0)
                    sm = (term_meta.get(sub["centroid"]) or {})
                    lines.append(
                        f"| {sub['sub_cluster']} | {sub['metrics']['n']} | "
                        f"**{sub['quality']}** | "
                        f"{sub['metrics']['cohesion']} | "
                        f"{sub_top[0]}({sub_top[1]}) | "
                        f"`{sub['centroid']}` {(sm.get('gloss') or '')[:25]} |"
                    )
                lines.append("")
                # Member listing per sub
                for sub in a["sub_clusters"]:
                    lines.append(
                        f"**Sub-cluster {sub['sub_cluster']}** "
                        f"({sub['quality']}, n={sub['metrics']['n']}, "
                        f"cohesion={sub['metrics']['cohesion']}):"
                    )
                    sub_theme_str = ", ".join(
                        f"{w}({c})" for w, c in sub["theme"][:6]
                    )
                    lines.append(f"  - theme: {sub_theme_str}")
                    member_glosses = []
                    for s in sorted(sub["members"], key=lambda x: ((term_meta.get(x) or {}).get("transliteration") or "").lower())[:8]:
                        m = term_meta.get(s, {})
                        member_glosses.append(
                            f"{m.get('transliteration') or s}({(m.get('gloss') or '')[:18]})"
                        )
                    if len(sub["members"]) > 8:
                        member_glosses.append(f"+{len(sub['members'])-8} more")
                    lines.append(f"  - members: {'; '.join(member_glosses)}")
                    lines.append("")
            else:
                # Just show member sample
                lines.append("**Members (sample):**")
                lines.append("")
                lines.append("| Strong's | translit | gloss |")
                lines.append("|---|---|---|")
                for s in sorted(a["members"],
                                 key=lambda x: ((term_meta.get(x) or {}).get("transliteration") or "").lower())[:12]:
                    m = term_meta.get(s, {})
                    lines.append(
                        f"| {s} | {m.get('transliteration') or ''} | "
                        f"{(m.get('gloss') or '')[:50]} |"
                    )
                if len(a["members"]) > 12:
                    lines.append(f"| ... | | (+{len(a['members'])-12} more terms) |")
                lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-json", required=True,
                    help="5-way cluster JSON (e.g. term-clusters-5way-v2-...json)")
    ap.add_argument("--semantic", required=True)
    ap.add_argument("--cooccurrence", required=True)
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown", f"term-cluster-quality-{today_compact()}"
    )

    print("Loading 5-way cluster output...")
    with open(args.input_json, encoding="utf-8") as f:
        data = json.load(f)

    print("Loading vectors...")
    sem_strongs, sem_vec = load_npz(args.semantic)
    coo_strongs, coo_vec = load_npz(args.cooccurrence)
    sem_idx = {str(s): i for i, s in enumerate(sem_strongs)}
    coo_idx = {str(s): i for i, s in enumerate(coo_strongs)}
    common = sorted(set(sem_idx) & set(coo_idx))
    sem_aligned = np.array([sem_vec[sem_idx[s]] for s in common])
    coo_aligned = np.array([coo_vec[coo_idx[s]] for s in common])
    combined = np.concatenate([sem_aligned, coo_aligned], axis=1)
    norms = np.linalg.norm(combined, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    combined = (combined / norms).astype(np.float32)
    idx_map = {s: i for i, s in enumerate(common)}

    # Build term metadata lookup from JSON entries (richer than re-querying DB)
    term_meta = {}
    for bucket_key in ("loci", "characteristics_hebrew", "characteristics_greek",
                        "qualifiers", "generics", "extraction_noise"):
        for entry in data.get(bucket_key, []):
            term_meta[entry["strong"]] = {
                "transliteration": entry.get("transliteration"),
                "gloss": entry.get("gloss"),
                "language": entry.get("language"),
                "registry": entry.get("registry"),
                "verse_count": entry.get("verse_count"),
                "multi_term_pct": entry.get("multi_term_pct"),
            }

    # Assess each pool
    print("\nAssessing Hebrew characteristic clusters...")
    heb_assessment = assess_pool(
        data["characteristics_hebrew"], combined, idx_map, term_meta
    )
    print(f"  {len(heb_assessment)} clusters assessed")

    print("Assessing Greek characteristic clusters...")
    gk_assessment = assess_pool(
        data["characteristics_greek"], combined, idx_map, term_meta
    )
    print(f"  {len(gk_assessment)} clusters assessed")

    # Render markdown
    md_heb = render_md(
        "Hebrew characteristic clusters — quality assessment",
        heb_assessment, term_meta
    )
    md_gk = render_md(
        "Greek characteristic clusters — quality assessment",
        gk_assessment, term_meta
    )

    # Combined summary
    by_q_heb = Counter(a["quality"] for a in heb_assessment)
    by_q_gk = Counter(a["quality"] for a in gk_assessment)
    summary_lines = [
        "# Cluster quality summary (Hebrew + Greek)",
        "",
        f"**Generated:** {now_iso()}",
        "",
        "## Quality breakdown",
        "",
        "| Pool | TIGHT | MODERATE | LOOSE | Total |",
        "|---|---|---|---|---|",
        f"| Hebrew | {by_q_heb['TIGHT']} | {by_q_heb['MODERATE']} | "
        f"{by_q_heb['LOOSE']} | {len(heb_assessment)} |",
        f"| Greek | {by_q_gk['TIGHT']} | {by_q_gk['MODERATE']} | "
        f"{by_q_gk['LOOSE']} | {len(gk_assessment)} |",
        "",
        "## Reading the metrics",
        "",
        "- **cohesion** = mean cosine similarity of members to centroid. Range [0,1]. Higher = tighter.",
        "- **theme%** = top theme word frequency / cluster size. Higher = more thematically concentrated.",
        "- **TIGHT** = cohesion ≥ 0.60 OR (n ≤ 12 AND cohesion ≥ 0.50). Lock in as analytical units.",
        "- **MODERATE** = in between. Acceptable but inspect.",
        "- **LOOSE** = cohesion < 0.45 OR (n ≥ 30 AND cohesion < 0.55). Get sub-clustered automatically.",
    ]
    out_summary = out_prefix + "-summary.md"
    out_heb = out_prefix + "-hebrew.md"
    out_gk = out_prefix + "-greek.md"
    out_json = out_prefix + ".json"

    os.makedirs(os.path.dirname(out_summary), exist_ok=True)
    with open(out_summary, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))
    with open(out_heb, "w", encoding="utf-8") as f:
        f.write(md_heb)
    with open(out_gk, "w", encoding="utf-8") as f:
        f.write(md_gk)

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "input_json": args.input_json,
            "n_hebrew_clusters": len(heb_assessment),
            "n_greek_clusters": len(gk_assessment),
            "by_quality_hebrew": dict(by_q_heb),
            "by_quality_greek": dict(by_q_gk),
        },
        "hebrew": heb_assessment,
        "greek": gk_assessment,
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"\nWrote: {out_summary}")
    print(f"Wrote: {out_heb}")
    print(f"Wrote: {out_gk}")
    print(f"Wrote: {out_json}")
    print(f"\nHebrew quality: TIGHT={by_q_heb['TIGHT']} · "
          f"MODERATE={by_q_heb['MODERATE']} · LOOSE={by_q_heb['LOOSE']}")
    print(f"Greek quality:  TIGHT={by_q_gk['TIGHT']} · "
          f"MODERATE={by_q_gk['MODERATE']} · LOOSE={by_q_gk['LOOSE']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
