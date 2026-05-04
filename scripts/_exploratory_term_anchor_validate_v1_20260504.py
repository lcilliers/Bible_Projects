"""_exploratory_term_anchor_validate_v1_20260504.py — read-only.

Two validation checks on the new term-anchor build:

A. CLUSTER QUALITY — re-runs the v2 quality assessment (recursive
   sub-clustering, FREQUENCY-ARTIFACT detection, dual-criterion TIGHT)
   on the new T1-only clusters.

B. UNCLASSIFIED T1 VERSE COVERAGE — counts how many verse-term pairs
   for T1 terms have no verse_context classification yet, plus how
   many distinct verses are involved.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

DB_PATH = os.path.join("database", "bible_research.db")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


TOKEN_RE = re.compile(r"[a-z]+")
THEME_STOPWORDS = {
    "a", "an", "the", "to", "of", "in", "on", "with", "for", "by", "at",
    "be", "is", "was", "are", "were", "am", "been", "being",
    "like", "as", "that", "this", "those", "these", "it", "its",
    "do", "does", "did", "doing", "done", "have", "has", "had", "having",
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
        return {"n": len(members), "cohesion": 1.0 if indices else 0.0,
                "theme_concentration": 0.0, "dispersion": 0.0,
                "mean_verse_count": 0.0}
    v = vectors[indices]
    centroid = v.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = v @ centroid
    counter = Counter()
    verse_counts = []
    for s in members:
        m = term_meta.get(s, {})
        for t in gloss_tokens(m.get("gloss") or ""):
            counter[t] += 1
        if m.get("verse_count") is not None:
            verse_counts.append(m["verse_count"])
    theme_conc = (counter.most_common(1)[0][1] / len(members)) if counter else 0.0
    return {
        "n": len(members),
        "cohesion": round(float(sims.mean()), 4),
        "dispersion": round(float(sims.std()), 4),
        "theme_concentration": round(theme_conc, 4),
        "mean_verse_count": round(float(np.mean(verse_counts))
                                    if verse_counts else 0.0, 1),
    }


def classify_quality(metrics):
    n, coh, theme, mvc = (metrics["n"], metrics["cohesion"],
                            metrics["theme_concentration"],
                            metrics["mean_verse_count"])
    if mvc > 100 and theme < 0.10 and n >= 15:
        return "FREQUENCY-ARTIFACT"
    if coh >= 0.60 and theme >= 0.15:
        return "TIGHT"
    if n <= 12 and coh >= 0.50 and theme >= 0.20:
        return "TIGHT"
    if coh < 0.45 or (n >= 30 and coh < 0.55) or (theme < 0.05 and n >= 10):
        return "LOOSE"
    return "MODERATE"


def cluster_kmeans(vectors, k, seed=20260504):
    from sklearn.cluster import KMeans
    return KMeans(n_clusters=k, random_state=seed, n_init=10).fit_predict(vectors)


def cluster_centroid_term(strongs, vectors, idx_map):
    indices = [idx_map[s] for s in strongs if s in idx_map]
    if not indices:
        return None
    v = vectors[indices]
    centroid = v.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = v @ centroid
    return strongs[int(np.argmax(sims))]


def cluster_theme(strongs, term_meta, top_k=8):
    counter = Counter()
    for s in strongs:
        for t in gloss_tokens((term_meta.get(s) or {}).get("gloss") or ""):
            counter[t] += 1
    return counter.most_common(top_k)


def assess_recursive(members, vectors, idx_map, term_meta,
                      depth=0, max_depth=3, sub_size_divisor=10):
    metrics = cluster_quality(members, vectors, idx_map, term_meta)
    quality = classify_quality(metrics)
    theme = cluster_theme(members, term_meta)
    centroid = cluster_centroid_term(members, vectors, idx_map)
    centroid_gloss = ((term_meta.get(centroid) or {}).get("gloss") or "") if centroid else ""
    node = {
        "members": members, "metrics": metrics, "quality": quality,
        "theme": theme, "centroid": centroid, "centroid_gloss": centroid_gloss,
        "depth": depth, "sub_clusters": None,
    }
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


def collect_leaves(node):
    if not node.get("sub_clusters"):
        return [node]
    out = []
    for sub in node["sub_clusters"]:
        out.extend(collect_leaves(sub))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--anchor-json", required=True)
    ap.add_argument("--semantic", required=True)
    ap.add_argument("--cooccurrence", required=True)
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown", f"wa-term-anchor-validate-{today_compact()}"
    )

    print("Loading anchor JSON...")
    with open(args.anchor_json, encoding="utf-8") as f:
        anchor = json.load(f)
    term_meta = {s: a for s, a in anchor["term_anchors"].items()}

    print("Loading vectors...")
    with np.load(args.semantic, allow_pickle=False) as f:
        sem_strongs = f["strongs"][:]
        sem_vec = f["vectors"][:]
    with np.load(args.cooccurrence, allow_pickle=False) as f:
        coo_strongs = f["strongs"][:]
        coo_vec = f["vectors"][:]
    sem_idx = {str(s): i for i, s in enumerate(sem_strongs)}
    coo_idx = {str(s): i for i, s in enumerate(coo_strongs)}
    common = sorted(set(sem_idx) & set(coo_idx))
    sem_aligned = sem_vec[[sem_idx[s] for s in common]]
    coo_aligned = coo_vec[[coo_idx[s] for s in common]]
    combined = np.concatenate([sem_aligned, coo_aligned], axis=1)
    norms = np.linalg.norm(combined, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    combined = (combined / norms).astype(np.float32)
    idx_map = {s: i for i, s in enumerate(common)}

    # ===== A. CLUSTER QUALITY =====
    print("\n=== A. Cluster quality on T1-only clusters ===")
    heb_assessments, gk_assessments = [], []
    for cid, c in anchor["clusters"]["hebrew"].items():
        members = [m["strong"] for m in c["members_t1"]]
        node = assess_recursive(members, combined, idx_map, term_meta)
        node["cluster_id"] = cid
        node["label"] = c["label"]
        heb_assessments.append(node)
    for cid, c in anchor["clusters"]["greek"].items():
        members = [m["strong"] for m in c["members_t1"]]
        node = assess_recursive(members, combined, idx_map, term_meta)
        node["cluster_id"] = cid
        node["label"] = c["label"]
        gk_assessments.append(node)

    heb_top = Counter(a["quality"] for a in heb_assessments)
    gk_top = Counter(a["quality"] for a in gk_assessments)
    heb_leaf = Counter()
    gk_leaf = Counter()
    for a in heb_assessments:
        for leaf in collect_leaves(a):
            heb_leaf[leaf["quality"]] += 1
    for a in gk_assessments:
        for leaf in collect_leaves(a):
            gk_leaf[leaf["quality"]] += 1

    print(f"\nHebrew T1 ({len(heb_assessments)} clusters):")
    print(f"  Top-level: TIGHT={heb_top['TIGHT']} · MODERATE={heb_top['MODERATE']} · "
          f"LOOSE={heb_top['LOOSE']} · FREQ-ARTIFACT={heb_top['FREQUENCY-ARTIFACT']}")
    print(f"  Leaves:    TIGHT={heb_leaf['TIGHT']} · MODERATE={heb_leaf['MODERATE']} · "
          f"LOOSE={heb_leaf['LOOSE']} · FREQ-ARTIFACT={heb_leaf['FREQUENCY-ARTIFACT']}")
    print(f"\nGreek T1 ({len(gk_assessments)} clusters):")
    print(f"  Top-level: TIGHT={gk_top['TIGHT']} · MODERATE={gk_top['MODERATE']} · "
          f"LOOSE={gk_top['LOOSE']} · FREQ-ARTIFACT={gk_top['FREQUENCY-ARTIFACT']}")
    print(f"  Leaves:    TIGHT={gk_leaf['TIGHT']} · MODERATE={gk_leaf['MODERATE']} · "
          f"LOOSE={gk_leaf['LOOSE']} · FREQ-ARTIFACT={gk_leaf['FREQUENCY-ARTIFACT']}")

    # ===== B. UNCLASSIFIED T1 VERSE COVERAGE =====
    print("\n=== B. Unclassified T1 verse coverage ===")
    t1_strongs = sorted([s for s, a in term_meta.items() if a["bucket"] == "T1"])
    print(f"  T1 terms total: {len(t1_strongs)}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    quoted = ",".join("'" + s + "'" for s in t1_strongs)

    r = conn.execute(f"""
        SELECT COUNT(*) AS total_pairs,
               SUM(CASE WHEN vc.id IS NULL THEN 1 ELSE 0 END) AS unclassified_pairs,
               SUM(CASE WHEN vc.id IS NOT NULL THEN 1 ELSE 0 END) AS classified_pairs
          FROM wa_verse_records vr
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                    AND ti.term_owner_type='OWNER'
                                    AND ti.delete_flagged=0
          JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
                            AND mt.delete_flagged=0
          LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                     AND vc.mti_term_id = mt.id
                                     AND vc.delete_flagged = 0
         WHERE vr.delete_flagged = 0
           AND ti.strongs_number IN ({quoted})
    """).fetchone()
    print(f"\n  T1 (verse, term) pairs:")
    print(f"    total:        {r['total_pairs']:,}")
    print(f"    classified:   {r['classified_pairs']:,} ({100*r['classified_pairs']/r['total_pairs']:.1f}%)")
    print(f"    UNCLASSIFIED: {r['unclassified_pairs']:,} ({100*r['unclassified_pairs']/r['total_pairs']:.1f}%)")

    # Distinct verses with at least one unclassified T1 pair
    r2 = conn.execute(f"""
        SELECT COUNT(DISTINCT vr.reference) AS n_verses
          FROM wa_verse_records vr
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                    AND ti.term_owner_type='OWNER'
                                    AND ti.delete_flagged=0
          JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
                            AND mt.delete_flagged=0
          LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                     AND vc.mti_term_id = mt.id
                                     AND vc.delete_flagged = 0
         WHERE vr.delete_flagged = 0
           AND ti.strongs_number IN ({quoted})
           AND vc.id IS NULL
    """).fetchone()
    print(f"\n  Distinct verses with ≥1 unclassified T1 pair: {r2['n_verses']:,}")

    # All-vs-unclassified distinct verses
    r3 = conn.execute(f"""
        SELECT COUNT(DISTINCT vr.reference) AS n_verses
          FROM wa_verse_records vr
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                    AND ti.term_owner_type='OWNER'
                                    AND ti.delete_flagged=0
         WHERE vr.delete_flagged = 0
           AND ti.strongs_number IN ({quoted})
    """).fetchone()
    print(f"  Distinct verses containing any T1 term:        {r3['n_verses']:,}")
    print(f"  Coverage gap: "
          f"{r2['n_verses']:,} of {r3['n_verses']:,} verses "
          f"({100*r2['n_verses']/r3['n_verses']:.1f}%) need T1-term classification")

    # Per-language breakdown of unclassified T1 pairs
    heb_t1 = [s for s in t1_strongs if s.startswith("H")]
    gk_t1 = [s for s in t1_strongs if s.startswith("G")]
    print(f"\n  Per-language T1 unclassified pairs:")
    for lang_name, lang_list in (("Hebrew T1", heb_t1), ("Greek T1", gk_t1)):
        q = ",".join("'" + s + "'" for s in lang_list)
        rr = conn.execute(f"""
            SELECT COUNT(*) AS n
              FROM wa_verse_records vr
              JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                        AND ti.term_owner_type='OWNER'
                                        AND ti.delete_flagged=0
              JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
                                AND mt.delete_flagged=0
              LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                         AND vc.mti_term_id = mt.id
                                         AND vc.delete_flagged = 0
             WHERE vr.delete_flagged = 0
               AND ti.strongs_number IN ({q})
               AND vc.id IS NULL
        """).fetchone()
        print(f"    {lang_name}: {rr['n']:,}")

    conn.close()

    # Per-cluster unclassified counts (T1 cluster → unclassified pair count)
    print("\n  Computing per-cluster unclassified counts...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    per_cluster = {}
    for lang_block_name in ("hebrew", "greek"):
        for cid, c in anchor["clusters"][lang_block_name].items():
            members = [m["strong"] for m in c["members_t1"]]
            if not members:
                per_cluster[cid] = {"label": c["label"], "n_t1": 0,
                                     "unclassified_pairs": 0,
                                     "unclassified_verses": 0,
                                     "language": lang_block_name}
                continue
            qq = ",".join("'" + s + "'" for s in members)
            cr = conn.execute(f"""
                SELECT COUNT(*) AS n_pairs,
                       COUNT(DISTINCT vr.reference) AS n_verses
                  FROM wa_verse_records vr
                  JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                            AND ti.term_owner_type='OWNER'
                                            AND ti.delete_flagged=0
                  JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
                                    AND mt.delete_flagged=0
                  LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                             AND vc.mti_term_id = mt.id
                                             AND vc.delete_flagged = 0
                 WHERE vr.delete_flagged = 0
                   AND ti.strongs_number IN ({qq})
                   AND vc.id IS NULL
            """).fetchone()
            per_cluster[cid] = {
                "label": c["label"],
                "n_t1": len(members),
                "unclassified_pairs": cr["n_pairs"],
                "unclassified_verses": cr["n_verses"],
                "language": lang_block_name,
            }
    conn.close()

    # Output
    out_md = out_prefix + ".md"
    out_json = out_prefix + ".json"
    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    md_lines = [
        f"# Term anchor validation — quality + unclassified coverage",
        "",
        f"**Generated:** {now_iso()}",
        f"**Anchor input:** `{args.anchor_json}`",
        "",
        "## A. Cluster quality (T1-only clusters)",
        "",
        "Compared against v1 baseline (5-way clustering with T2/qualifiers mixed in).",
        "",
        "### Hebrew T1",
        "",
        f"Top-level ({len(heb_assessments)} clusters):",
        "",
        "| Quality | Count |",
        "|---|---|",
        f"| TIGHT | {heb_top['TIGHT']} |",
        f"| MODERATE | {heb_top['MODERATE']} |",
        f"| LOOSE | {heb_top['LOOSE']} |",
        f"| FREQUENCY-ARTIFACT | {heb_top['FREQUENCY-ARTIFACT']} |",
        "",
        "After recursive sub-clustering — leaves:",
        "",
        "| Quality | Count |",
        "|---|---|",
        f"| TIGHT | {heb_leaf['TIGHT']} |",
        f"| MODERATE | {heb_leaf['MODERATE']} |",
        f"| LOOSE | {heb_leaf['LOOSE']} |",
        f"| FREQUENCY-ARTIFACT | {heb_leaf['FREQUENCY-ARTIFACT']} |",
        "",
        "### Greek T1",
        "",
        f"Top-level ({len(gk_assessments)} clusters):",
        "",
        "| Quality | Count |",
        "|---|---|",
        f"| TIGHT | {gk_top['TIGHT']} |",
        f"| MODERATE | {gk_top['MODERATE']} |",
        f"| LOOSE | {gk_top['LOOSE']} |",
        f"| FREQUENCY-ARTIFACT | {gk_top['FREQUENCY-ARTIFACT']} |",
        "",
        "After recursive sub-clustering — leaves:",
        "",
        "| Quality | Count |",
        "|---|---|",
        f"| TIGHT | {gk_leaf['TIGHT']} |",
        f"| MODERATE | {gk_leaf['MODERATE']} |",
        f"| LOOSE | {gk_leaf['LOOSE']} |",
        f"| FREQUENCY-ARTIFACT | {gk_leaf['FREQUENCY-ARTIFACT']} |",
        "",
        "## B. Unclassified T1 verse coverage",
        "",
        f"- T1 (verse, term) pairs total: **{r['total_pairs']:,}**",
        f"- T1 pairs already classified: **{r['classified_pairs']:,}** "
        f"({100*r['classified_pairs']/r['total_pairs']:.1f}%)",
        f"- T1 pairs **UNCLASSIFIED**: **{r['unclassified_pairs']:,}** "
        f"({100*r['unclassified_pairs']/r['total_pairs']:.1f}%)",
        "",
        f"- Distinct verses containing any T1 term: **{r3['n_verses']:,}**",
        f"- Distinct verses with ≥1 unclassified T1 pair: **{r2['n_verses']:,}** "
        f"({100*r2['n_verses']/r3['n_verses']:.1f}%)",
        "",
        "## Per-cluster unclassified workload (top 15 by pair count)",
        "",
        "| Cluster | Lang | Label | T1 terms | Unclassified pairs | Distinct verses |",
        "|---|---|---|---|---|---|",
    ]
    sorted_clusters = sorted(per_cluster.items(),
                              key=lambda x: -x[1]["unclassified_pairs"])
    for cid, info in sorted_clusters[:15]:
        md_lines.append(
            f"| {cid} | {info['language'][0].upper()} | {info['label']} | "
            f"{info['n_t1']} | {info['unclassified_pairs']:,} | "
            f"{info['unclassified_verses']:,} |"
        )
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    # JSON
    payload = {
        "meta": {
            "generated_at": now_iso(),
            "anchor_input": args.anchor_json,
        },
        "quality_hebrew": {
            "top_level": dict(heb_top), "leaves": dict(heb_leaf),
            "n_clusters": len(heb_assessments),
            "assessments": heb_assessments,
        },
        "quality_greek": {
            "top_level": dict(gk_top), "leaves": dict(gk_leaf),
            "n_clusters": len(gk_assessments),
            "assessments": gk_assessments,
        },
        "coverage": {
            "t1_pairs_total": r["total_pairs"],
            "t1_pairs_classified": r["classified_pairs"],
            "t1_pairs_unclassified": r["unclassified_pairs"],
            "verses_with_t1_term": r3["n_verses"],
            "verses_with_unclassified_t1_pair": r2["n_verses"],
        },
        "per_cluster_unclassified": per_cluster,
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)

    print(f"\nWrote: {out_md}")
    print(f"Wrote: {out_json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
