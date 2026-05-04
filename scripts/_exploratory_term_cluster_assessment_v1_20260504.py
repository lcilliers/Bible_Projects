"""_exploratory_term_cluster_assessment_v1_20260504.py — read-only.

Assessment step (post both vectors). Clusters the term embeddings at
multiple granularities and compares the resulting cluster boundaries to
the existing registry boundaries.

Outputs the alignment diagnostic the registry-vs-cluster decision rests on:

  - For each registry: dominant-cluster %, fragmentation count
  - For each cluster: registry mix, cross-cutting flag
  - Combined-vector clustering (semantic + usage) at multiple k
  - Per-vector clustering (semantic alone, usage alone) for comparison

Inputs:
  --semantic  outputs/markdown/term-semantic-vectors-{date}.npz
  --usage     outputs/markdown/term-usage-vectors-{date}.npz

Output:
  outputs/markdown/term-cluster-assessment-{date}.md
  outputs/markdown/term-cluster-assessment-{date}.json
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

DB_PATH = os.path.join("database", "bible_research.db")
GRANULARITIES = [40, 80, 120, 180]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def load_npz(path):
    arr = np.load(path, allow_pickle=False)
    return {
        "strongs": arr["strongs"],
        "vectors": arr["vectors"],
        "registries": arr["registries"] if "registries" in arr.files else None,
    }


def cluster_kmeans(vectors, k, seed=20260504):
    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=k, random_state=seed, n_init=10)
    labels = km.fit_predict(vectors)
    return labels


def fetch_registry_map(conn):
    """Return {strong: 'R### word'} for OWNER mti_terms."""
    out = {}
    for r in conn.execute("""
        SELECT mt.strongs_number, wr.no, wr.word
          FROM mti_terms mt
          JOIN word_registry wr ON wr.id = mt.owning_registry_fk
         WHERE mt.delete_flagged = 0
    """):
        out[r["strongs_number"]] = f"R{r[1]:03d} {r[2]}"
    return out


def alignment_metrics(strongs, labels, reg_map):
    """Compute per-registry and per-cluster diagnostics."""
    by_reg = defaultdict(list)        # registry -> list[label]
    by_cluster = defaultdict(list)    # cluster_label -> list[(strong, registry)]
    for s, lbl in zip(strongs, labels):
        reg = reg_map.get(str(s), "")
        if not reg:
            continue
        by_reg[reg].append(int(lbl))
        by_cluster[int(lbl)].append((str(s), reg))

    # Per-registry
    reg_diag = []
    for reg, lbls in by_reg.items():
        n = len(lbls)
        c = Counter(lbls)
        dominant_cluster, dominant_count = c.most_common(1)[0]
        reg_diag.append({
            "registry": reg,
            "n_owner_terms": n,
            "n_distinct_clusters": len(c),
            "dominant_cluster": int(dominant_cluster),
            "dominant_pct": round(100.0 * dominant_count / n, 1),
            "fragmentation": len(c),
        })
    reg_diag.sort(key=lambda x: x["dominant_pct"])

    # Per-cluster
    clu_diag = []
    for lbl, items in by_cluster.items():
        regs = Counter(r for _, r in items)
        n = len(items)
        n_regs = len(regs)
        top = regs.most_common(3)
        clu_diag.append({
            "cluster": int(lbl),
            "n_terms": n,
            "n_distinct_registries": n_regs,
            "top_registries": [
                {"registry": r, "count": c, "pct": round(100.0*c/n, 1)}
                for r, c in top
            ],
            "cross_cutting": n_regs >= 3 and top[0][1] / n < 0.6,
        })
    clu_diag.sort(key=lambda x: -x["n_distinct_registries"])

    # Aggregate
    n_total_regs = len(reg_diag)
    avg_dominant = float(np.mean([r["dominant_pct"] for r in reg_diag]))
    avg_frag = float(np.mean([r["fragmentation"] for r in reg_diag]))
    n_cross_cutting = sum(1 for c in clu_diag if c["cross_cutting"])

    return {
        "summary": {
            "n_registries": n_total_regs,
            "avg_dominant_cluster_pct": round(avg_dominant, 1),
            "avg_fragmentation": round(avg_frag, 1),
            "n_cross_cutting_clusters": n_cross_cutting,
            "n_clusters_total": len(clu_diag),
        },
        "registry_diag": reg_diag,
        "cluster_diag": clu_diag,
    }


def compare_signals(strongs_sem, vec_sem, strongs_usg, vec_usg):
    """Return aligned subset (intersection of strongs) for combined vector."""
    set_usg = {str(s): i for i, s in enumerate(strongs_usg)}
    pairs = []
    for i, s in enumerate(strongs_sem):
        s = str(s)
        if s in set_usg:
            pairs.append((s, i, set_usg[s]))
    aligned_strongs = np.array([p[0] for p in pairs])
    aligned_sem = vec_sem[[p[1] for p in pairs]]
    aligned_usg = vec_usg[[p[2] for p in pairs]]
    # L2-normalised concat (both already normalised)
    combined = np.concatenate([aligned_sem, aligned_usg], axis=1)
    combined = combined / np.linalg.norm(combined, axis=1, keepdims=True)
    return aligned_strongs, aligned_sem, aligned_usg, combined.astype(np.float32)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--semantic", required=True)
    ap.add_argument("--usage", required=True)
    ap.add_argument("--out-prefix", default=None)
    ap.add_argument("--granularities", default=None,
                    help="comma-separated k values (default 40,80,120,180)")
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown",
        f"term-cluster-assessment-{today_compact()}"
    )
    granularities = [int(x) for x in args.granularities.split(",")] \
        if args.granularities else GRANULARITIES

    print("Loading vectors...")
    sem = load_npz(args.semantic)
    usg = load_npz(args.usage)
    print(f"  semantic: {sem['vectors'].shape}")
    print(f"  usage:    {usg['vectors'].shape}")

    print("Aligning vectors on common Strong's...")
    strongs, sem_v, usg_v, comb_v = compare_signals(
        sem["strongs"], sem["vectors"], usg["strongs"], usg["vectors"]
    )
    print(f"  aligned: {len(strongs)} terms (intersection)")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    print("Fetching registry map...")
    reg_map = fetch_registry_map(conn)
    n_with_reg = sum(1 for s in strongs if str(s) in reg_map)
    print(f"  {n_with_reg} of {len(strongs)} aligned terms have an OWNER registry")

    runs = {}
    for vec_name, vec in [("semantic", sem_v), ("usage", usg_v),
                           ("combined", comb_v)]:
        for k in granularities:
            print(f"Clustering {vec_name} k={k}...")
            labels = cluster_kmeans(vec, k)
            metrics = alignment_metrics(strongs, labels, reg_map)
            runs[f"{vec_name}__k{k}"] = {
                "vector": vec_name,
                "k": k,
                **metrics,
            }
            s = metrics["summary"]
            print(f"  avg_dominant={s['avg_dominant_cluster_pct']}% · "
                  f"avg_frag={s['avg_fragmentation']} · "
                  f"cross_cutting={s['n_cross_cutting_clusters']}/{s['n_clusters_total']}")

    out_payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_aligned_terms": len(strongs),
            "n_terms_with_registry": n_with_reg,
            "granularities": granularities,
            "semantic_input": args.semantic,
            "usage_input": args.usage,
        },
        "runs": runs,
    }

    out_json = out_prefix + ".json"
    out_md = out_prefix + ".md"
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(out_payload, f, indent=2, ensure_ascii=False)

    md_lines = [
        f"# Term cluster assessment — registry vs cluster alignment",
        "",
        f"**Generated:** {out_payload['meta']['generated_at']}",
        f"**Aligned terms:** {len(strongs)} "
        f"({n_with_reg} with OWNER registry)",
        f"**Granularities (k):** {granularities}",
        "",
        "## Summary by run",
        "",
        "| run | k | avg dominant-cluster % | avg fragmentation | cross-cutting clusters |",
        "|---|---|---|---|---|",
    ]
    for run_name, run in runs.items():
        s = run["summary"]
        md_lines.append(
            f"| {run_name} | {run['k']} | {s['avg_dominant_cluster_pct']}% | "
            f"{s['avg_fragmentation']} | "
            f"{s['n_cross_cutting_clusters']}/{s['n_clusters_total']} |"
        )

    md_lines.append("")
    md_lines.append("**Reading the table:**")
    md_lines.append("- Higher *avg dominant %* and lower *avg fragmentation* = registries align well with clusters (registry stays).")
    md_lines.append("- Lower *avg dominant %* and higher *avg fragmentation* = registries miscut the data (cluster pivot is supported).")
    md_lines.append("- *Cross-cutting clusters* = clusters that pull from 3+ registries without a dominant one (analytical units the registry-driven structure misses).")
    md_lines.append("")

    # For the recommended granularity (combined__k120) show worst-aligned regs and most cross-cutting clusters
    rec = "combined__k120" if "combined__k120" in runs else list(runs)[0]
    md_lines.append(f"## Worst-aligned registries — `{rec}`")
    md_lines.append("")
    md_lines.append("| registry | OWNER terms | distinct clusters | dominant cluster % |")
    md_lines.append("|---|---|---|---|")
    for r in runs[rec]["registry_diag"][:20]:
        md_lines.append(
            f"| {r['registry']} | {r['n_owner_terms']} | "
            f"{r['n_distinct_clusters']} | {r['dominant_pct']}% |"
        )

    md_lines.append("")
    md_lines.append(f"## Best-aligned registries — `{rec}`")
    md_lines.append("")
    md_lines.append("| registry | OWNER terms | distinct clusters | dominant cluster % |")
    md_lines.append("|---|---|---|---|")
    for r in sorted(runs[rec]["registry_diag"], key=lambda x: -x["dominant_pct"])[:20]:
        md_lines.append(
            f"| {r['registry']} | {r['n_owner_terms']} | "
            f"{r['n_distinct_clusters']} | {r['dominant_pct']}% |"
        )

    md_lines.append("")
    md_lines.append(f"## Top cross-cutting clusters — `{rec}`")
    md_lines.append("")
    md_lines.append("| cluster | total terms | n distinct registries | top 3 registries (count/pct) |")
    md_lines.append("|---|---|---|---|")
    for c in runs[rec]["cluster_diag"][:20]:
        tops = "; ".join(
            f"{t['registry']} ({t['count']}/{t['pct']}%)" for t in c["top_registries"]
        )
        md_lines.append(
            f"| {c['cluster']} | {c['n_terms']} | "
            f"{c['n_distinct_registries']} | {tops} |"
        )

    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")

    print(f"\nWrote: {out_json}")
    print(f"Wrote: {out_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
