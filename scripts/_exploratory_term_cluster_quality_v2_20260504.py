"""_exploratory_term_cluster_quality_v2_20260504.py — read-only.

V2 of the quality assessor. Refinements based on inspection feedback:

1. TIGHT requires BOTH cohesion >= 0.60 AND theme_concentration >= 0.15
   (was cohesion-only; missed cases like Greek C38 with high cohesion but
   thematically scattered membership).

2. FREQUENCY-ARTIFACT flag: clusters where mean verse_count > 100 AND
   theme_concentration < 0.10. Catches the Hebrew C75 case — clusters
   driven by high-frequency verbs co-occurring with everything rather
   than by genuine semantic similarity.

3. Recursive sub-clustering up to depth 3 (or until every leaf is TIGHT
   / MODERATE / FREQUENCY-ARTIFACT).
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


def gloss_tokens(g):
    if not g:
        return []
    g = g.lower().split(":")[0]
    return [t for t in TOKEN_RE.findall(g)
            if t not in THEME_STOPWORDS and len(t) > 2]


def cluster_quality(members, vectors, idx_map, term_meta):
    indices = [idx_map[s] for s in members if s in idx_map]
    if len(indices) < 2:
        return {
            "n": len(members),
            "cohesion": 1.0 if len(indices) == 1 else 0.0,
            "theme_concentration": 0.0,
            "dispersion": 0.0,
            "mean_verse_count": 0.0,
        }
    v = vectors[indices]
    centroid = v.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = v @ centroid
    cohesion = float(sims.mean())
    dispersion = float(sims.std())
    counter = Counter()
    verse_counts = []
    for s in members:
        m = term_meta.get(s, {})
        for t in gloss_tokens(m.get("gloss") or ""):
            counter[t] += 1
        if m.get("verse_count") is not None:
            verse_counts.append(m["verse_count"])
    theme_conc = (counter.most_common(1)[0][1] / len(members)
                   if counter else 0.0)
    mean_vc = float(np.mean(verse_counts)) if verse_counts else 0.0
    return {
        "n": len(members),
        "cohesion": round(cohesion, 4),
        "dispersion": round(dispersion, 4),
        "theme_concentration": round(theme_conc, 4),
        "mean_verse_count": round(mean_vc, 1),
    }


def classify_quality(metrics):
    n = metrics["n"]
    coh = metrics["cohesion"]
    theme = metrics["theme_concentration"]
    mean_vc = metrics["mean_verse_count"]

    # FREQUENCY-ARTIFACT: high mean verse count, low theme concentration
    if mean_vc > 100 and theme < 0.10 and n >= 15:
        return "FREQUENCY-ARTIFACT"

    # TIGHT requires BOTH cohesion AND theme concentration
    if coh >= 0.60 and theme >= 0.15:
        return "TIGHT"
    # Small clusters can still be tight on cohesion + reasonable theme
    if n <= 12 and coh >= 0.50 and theme >= 0.20:
        return "TIGHT"

    # LOOSE
    if coh < 0.45:
        return "LOOSE"
    if n >= 30 and coh < 0.55:
        return "LOOSE"
    if theme < 0.05 and n >= 10:
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


def assess_recursive(members, vectors, idx_map, term_meta,
                     depth=0, max_depth=3, sub_size_divisor=10):
    """Recursive quality assessment with auto-sub-clustering of LOOSE
    clusters. Returns a tree node dict."""
    metrics = cluster_quality(members, vectors, idx_map, term_meta)
    quality = classify_quality(metrics)
    theme = cluster_theme(members, term_meta)
    centroid = cluster_centroid_term(members, vectors, idx_map)
    centroid_gloss = ((term_meta.get(centroid) or {}).get("gloss") or "") if centroid else ""

    node = {
        "members": members,
        "metrics": metrics,
        "quality": quality,
        "theme": theme,
        "centroid": centroid,
        "centroid_gloss": centroid_gloss,
        "depth": depth,
        "sub_clusters": None,
    }

    # Recurse on LOOSE clusters (and FREQUENCY-ARTIFACT if big enough)
    if (quality in ("LOOSE", "FREQUENCY-ARTIFACT") and len(members) >= 8
            and depth < max_depth):
        k_sub = max(2, len(members) // sub_size_divisor)
        indices = [idx_map[s] for s in members if s in idx_map]
        if len(indices) >= k_sub:
            sub_labels = cluster_kmeans(vectors[indices], k_sub)
            sub_by = defaultdict(list)
            for s, lbl in zip(members, sub_labels):
                sub_by[int(lbl)].append(s)
            node["k_sub"] = k_sub
            node["sub_clusters"] = []
            for sub_cid in sorted(sub_by):
                sub_node = assess_recursive(
                    sub_by[sub_cid], vectors, idx_map, term_meta,
                    depth=depth + 1, max_depth=max_depth,
                    sub_size_divisor=sub_size_divisor
                )
                sub_node["sub_cluster_id"] = sub_cid
                node["sub_clusters"].append(sub_node)
    return node


def collect_leaves(node, path=""):
    """Return list of leaf nodes (no sub_clusters)."""
    if not node.get("sub_clusters"):
        return [(path, node)]
    out = []
    for sub in node["sub_clusters"]:
        sub_path = f"{path}>{sub['sub_cluster_id']}" if path else f"{sub['sub_cluster_id']}"
        out.extend(collect_leaves(sub, sub_path))
    return out


def assess_pool(cluster_terms, vectors, idx_map, term_meta):
    by_cluster = defaultdict(list)
    for entry in cluster_terms:
        by_cluster[int(entry["cluster"])].append(entry["strong"])
    out = []
    for cid in sorted(by_cluster.keys()):
        node = assess_recursive(
            by_cluster[cid], vectors, idx_map, term_meta, depth=0
        )
        node["cluster"] = cid
        out.append(node)
    return out


def render_summary(title, assessment):
    by_q = Counter()
    leaf_qualities = Counter()
    for a in assessment:
        by_q[a["quality"]] += 1
        for _, leaf in collect_leaves(a):
            leaf_qualities[leaf["quality"]] += 1
    lines = [
        f"# {title}",
        "",
        f"**Generated:** {now_iso()}",
        f"**Top-level clusters:** {len(assessment)}",
        "",
        "## Top-level cluster quality",
        "",
        "| Quality | Count |",
        "|---|---|",
    ]
    for q in ["TIGHT", "MODERATE", "LOOSE", "FREQUENCY-ARTIFACT"]:
        lines.append(f"| {q} | {by_q[q]} |")
    lines.append("")
    lines.append("## Leaf-level (after recursive sub-clustering)")
    lines.append("")
    lines.append("| Quality | Count |")
    lines.append("|---|---|")
    for q in ["TIGHT", "MODERATE", "LOOSE", "FREQUENCY-ARTIFACT"]:
        lines.append(f"| {q} | {leaf_qualities[q]} |")
    lines.append("")
    return "\n".join(lines)


def render_clusters_md(title, assessment, term_meta):
    lines = [f"# {title}", "", f"**Generated:** {now_iso()}", ""]
    by_q = defaultdict(list)
    for a in assessment:
        by_q[a["quality"]].append(a)

    for q_label in ["TIGHT", "MODERATE", "LOOSE", "FREQUENCY-ARTIFACT"]:
        lines.append(f"## {q_label} top-level clusters ({len(by_q[q_label])})")
        lines.append("")
        for a in sorted(by_q[q_label], key=lambda x: -x["metrics"]["n"]):
            theme_str = ", ".join(f"{w}({c})" for w, c in a["theme"][:8])
            lines.append(
                f"### Cluster {a['cluster']} — {a['metrics']['n']} terms · "
                f"cohesion {a['metrics']['cohesion']} · "
                f"theme {int(a['metrics']['theme_concentration']*100)}% · "
                f"mean verses {a['metrics']['mean_verse_count']}"
            )
            lines.append("")
            lines.append(f"**Theme:** {theme_str}")
            lines.append("")
            if a["centroid"]:
                lines.append(f"**Centroid:** `{a['centroid']}` — {a['centroid_gloss']}")
                lines.append("")

            if a.get("sub_clusters"):
                lines.append(
                    f"**Recursive sub-clustering** (k_sub={a.get('k_sub','?')}):"
                )
                lines.append("")
                for sub in a["sub_clusters"]:
                    render_subtree(sub, lines, term_meta, indent="  ")
            else:
                lines.append("**Members (sample):**")
                lines.append("")
                lines.append("| Strong's | translit | gloss | verses | multi% |")
                lines.append("|---|---|---|---|---|")
                for s in sorted(a["members"],
                                 key=lambda x: ((term_meta.get(x) or {}).get("transliteration") or "").lower())[:12]:
                    m = term_meta.get(s, {})
                    lines.append(
                        f"| {s} | {m.get('transliteration') or ''} | "
                        f"{(m.get('gloss') or '')[:50]} | "
                        f"{m.get('verse_count') or ''} | "
                        f"{m.get('multi_term_pct') or ''}% |"
                    )
                if len(a["members"]) > 12:
                    lines.append(f"| ... | | (+{len(a['members'])-12} more) | | |")
                lines.append("")
    return "\n".join(lines)


def render_subtree(node, lines, term_meta, indent=""):
    sub_id = node.get("sub_cluster_id", "?")
    theme_str = ", ".join(f"{w}({c})" for w, c in node["theme"][:6])
    lines.append(
        f"{indent}- **Sub {sub_id}** — n={node['metrics']['n']}, "
        f"cohesion={node['metrics']['cohesion']}, "
        f"theme={int(node['metrics']['theme_concentration']*100)}%, "
        f"mean_verses={node['metrics']['mean_verse_count']} → **{node['quality']}**"
    )
    lines.append(f"{indent}  - theme: {theme_str}")
    if node["centroid"]:
        lines.append(f"{indent}  - centroid: `{node['centroid']}` — {node['centroid_gloss']}")

    if node.get("sub_clusters"):
        lines.append(f"{indent}  - **Further sub-clustered (depth={node['depth']+1}, k_sub={node.get('k_sub','?')}):**")
        for sub in node["sub_clusters"]:
            render_subtree(sub, lines, term_meta, indent=indent + "    ")
    else:
        sample_members = sorted(
            node["members"],
            key=lambda x: ((term_meta.get(x) or {}).get("transliteration") or "").lower()
        )[:6]
        member_str = "; ".join(
            f"{(term_meta.get(s) or {}).get('transliteration') or s}"
            f"({((term_meta.get(s) or {}).get('gloss') or '')[:18]})"
            for s in sample_members
        )
        if len(node["members"]) > 6:
            member_str += f"; +{len(node['members'])-6} more"
        lines.append(f"{indent}  - members: {member_str}")
    lines.append("")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-json", required=True)
    ap.add_argument("--semantic", required=True)
    ap.add_argument("--cooccurrence", required=True)
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown", f"term-cluster-quality-v2-{today_compact()}"
    )

    print("Loading inputs...")
    with open(args.input_json, encoding="utf-8") as f:
        data = json.load(f)
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

    term_meta = {}
    for k in ("loci", "characteristics_hebrew", "characteristics_greek",
              "qualifiers", "generics", "extraction_noise"):
        for e in data.get(k, []):
            term_meta[e["strong"]] = e

    print("\nAssessing Hebrew (recursive)...")
    heb = assess_pool(data["characteristics_hebrew"], combined, idx_map, term_meta)
    print(f"  {len(heb)} top-level clusters")

    print("Assessing Greek (recursive)...")
    gk = assess_pool(data["characteristics_greek"], combined, idx_map, term_meta)
    print(f"  {len(gk)} top-level clusters")

    out_summary = out_prefix + "-summary.md"
    out_heb = out_prefix + "-hebrew.md"
    out_gk = out_prefix + "-greek.md"
    out_json = out_prefix + ".json"

    summary = (
        render_summary("Hebrew quality assessment v2", heb) + "\n\n---\n\n" +
        render_summary("Greek quality assessment v2", gk)
    )
    os.makedirs(os.path.dirname(out_summary), exist_ok=True)
    with open(out_summary, "w", encoding="utf-8") as f:
        f.write(summary)
    with open(out_heb, "w", encoding="utf-8") as f:
        f.write(render_clusters_md(
            "Hebrew clusters — quality v2 (recursive)", heb, term_meta
        ))
    with open(out_gk, "w", encoding="utf-8") as f:
        f.write(render_clusters_md(
            "Greek clusters — quality v2 (recursive)", gk, term_meta
        ))
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "generated_at": now_iso(),
                "input_json": args.input_json,
                "criteria_v2": {
                    "TIGHT": "cohesion >= 0.60 AND theme >= 0.15 OR (n <= 12 AND coh >= 0.50 AND theme >= 0.20)",
                    "LOOSE": "coh < 0.45 OR (n >= 30 AND coh < 0.55) OR (theme < 0.05 AND n >= 10)",
                    "FREQUENCY-ARTIFACT": "mean_verse_count > 100 AND theme < 0.10 AND n >= 15",
                    "MODERATE": "in between",
                },
            },
            "hebrew": heb,
            "greek": gk,
        }, f, indent=2, ensure_ascii=False)

    # Top-level + leaf summary
    def count_quality_leaves(pool):
        from collections import Counter
        c = Counter()
        for cluster in pool:
            for _, leaf in collect_leaves(cluster):
                c[leaf["quality"]] += 1
        return c
    heb_top = Counter(a["quality"] for a in heb)
    heb_leaf = count_quality_leaves(heb)
    gk_top = Counter(a["quality"] for a in gk)
    gk_leaf = count_quality_leaves(gk)
    print()
    print(f"Hebrew top-level: TIGHT={heb_top['TIGHT']} · "
          f"MODERATE={heb_top['MODERATE']} · LOOSE={heb_top['LOOSE']} · "
          f"FREQUENCY-ARTIFACT={heb_top['FREQUENCY-ARTIFACT']}")
    print(f"Hebrew leaves:    TIGHT={heb_leaf['TIGHT']} · "
          f"MODERATE={heb_leaf['MODERATE']} · LOOSE={heb_leaf['LOOSE']} · "
          f"FREQUENCY-ARTIFACT={heb_leaf['FREQUENCY-ARTIFACT']}")
    print(f"Greek top-level:  TIGHT={gk_top['TIGHT']} · "
          f"MODERATE={gk_top['MODERATE']} · LOOSE={gk_top['LOOSE']} · "
          f"FREQUENCY-ARTIFACT={gk_top['FREQUENCY-ARTIFACT']}")
    print(f"Greek leaves:     TIGHT={gk_leaf['TIGHT']} · "
          f"MODERATE={gk_leaf['MODERATE']} · LOOSE={gk_leaf['LOOSE']} · "
          f"FREQUENCY-ARTIFACT={gk_leaf['FREQUENCY-ARTIFACT']}")
    print()
    print(f"Wrote: {out_summary}")
    print(f"Wrote: {out_heb}")
    print(f"Wrote: {out_gk}")
    print(f"Wrote: {out_json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
