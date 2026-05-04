"""_exploratory_term_anchor_build_v1_20260504.py — read-only.

Builds the per-term cluster ANCHOR record using the user's T1/T2/FLAG
classification.

Input:
  outputs/markdown/wa-term-type-classification-v1-2026-05-04.json
    {strong: {lang, transliteration, gloss, verse_count, multi_term_pct,
              cluster (legacy from 5-way), ib_type (T1|T2|FLAG)}}

Pipeline:
  1. Re-cluster T1-only (Hebrew + Greek separately) on the existing
     weighted-semantic + co-occurrence vectors. T1 is the primary pool;
     T2 are not allowed to drive cluster boundaries.
  2. Compute cluster theme + centroid term + cluster label.
  3. Attach T2 terms to their primary T1 cluster via co-occurrence
     affinity (verse co-occurrence with T1 cluster members).
  4. FLAG terms are output unattached (cluster=null, review_required=true).
  5. LOCI / GENERICS / EXTRACTION-NOISE / QUALIFIERS retain their
     previous bucket designation but are NOT re-clustered.
  6. Per-term anchor JSON: each term gets one record with:
       - strong, lang, transliteration, gloss, verse_count, multi_term_pct
       - bucket: T1|T2|FLAG|LOCUS|GENERIC|EXTRACTION_NOISE|QUALIFIER
       - cluster_id  (T1 primary cluster this term anchors to)
       - cluster_label (theme-derived short label)
       - cluster_centroid (representative term)
       - attachment_affinity (T2 only)
       - review_required (FLAG only)

Outputs:
  outputs/markdown/wa-term-anchor-{date}.json     — per-term anchor records
  outputs/markdown/wa-term-anchor-{date}-clusters.md — cluster catalogue
  outputs/markdown/wa-term-anchor-{date}-flags.md     — FLAG review list
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


def cluster_theme(strongs, term_meta, top_k=8):
    counter = Counter()
    for s in strongs:
        for t in gloss_tokens((term_meta.get(s) or {}).get("gloss") or ""):
            counter[t] += 1
    return counter.most_common(top_k)


def cluster_label_from_theme(theme):
    """Derive a short readable label from theme word list."""
    if not theme:
        return "(unlabelled)"
    return "/".join(w for w, _ in theme[:3])


def cluster_centroid_term(strongs, vectors, idx_map):
    indices = [idx_map[s] for s in strongs if s in idx_map]
    if not indices:
        return None
    v = vectors[indices]
    centroid = v.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = v @ centroid
    return strongs[int(np.argmax(sims))]


def cluster_kmeans(vectors, k, seed=20260504):
    from sklearn.cluster import KMeans
    return KMeans(n_clusters=k, random_state=seed, n_init=10).fit_predict(vectors)


def cluster_quality_metric(strongs, vectors, idx_map, term_meta):
    indices = [idx_map[s] for s in strongs if s in idx_map]
    if len(indices) < 2:
        return {"n": len(strongs), "cohesion": 0.0, "theme_concentration": 0.0}
    v = vectors[indices]
    centroid = v.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = v @ centroid
    counter = Counter()
    for s in strongs:
        for t in gloss_tokens((term_meta.get(s) or {}).get("gloss") or ""):
            counter[t] += 1
    theme_conc = (counter.most_common(1)[0][1] / len(strongs)) if counter else 0.0
    return {
        "n": len(strongs),
        "cohesion": round(float(sims.mean()), 4),
        "theme_concentration": round(theme_conc, 4),
    }


def fetch_verse_to_terms(conn):
    rows = conn.execute("""
        SELECT vr.reference, ti.strongs_number AS strong
          FROM wa_verse_records vr
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                    AND ti.term_owner_type='OWNER'
                                    AND ti.delete_flagged=0
         WHERE vr.delete_flagged=0
    """).fetchall()
    by_ref = defaultdict(set)
    for r in rows:
        by_ref[r["reference"]].add(r["strong"])
    return by_ref


def attach_t2_to_cluster(t2_strongs, t1_strongs, t1_labels, verse_terms_map):
    """For each T2, find the T1 cluster it most co-occurs with.
    Returns {t2_strong: {top_cluster, affinity, alternates}}."""
    t1_to_cluster = dict(zip(t1_strongs, t1_labels))
    t2_set = set(t2_strongs)
    t2_cluster_count = {q: defaultdict(int) for q in t2_strongs}
    t2_total = Counter()
    for ref, terms in verse_terms_map.items():
        present = terms & t2_set
        if not present:
            continue
        for q in present:
            t2_total[q] += 1
            cluster_present = set()
            for t in terms - {q}:
                if t in t1_to_cluster:
                    cluster_present.add(int(t1_to_cluster[t]))
            for c in cluster_present:
                t2_cluster_count[q][c] += 1
    out = {}
    for q in t2_strongs:
        if t2_total[q] == 0 or not t2_cluster_count[q]:
            # T2 either has no verses, or no verses where T1-cluster siblings appear
            out[q] = {"top_cluster": None, "affinity": 0.0, "alternates": []}
            continue
        scored = sorted(
            ((c, n / t2_total[q]) for c, n in t2_cluster_count[q].items()),
            key=lambda x: -x[1]
        )
        out[q] = {
            "top_cluster": int(scored[0][0]),
            "affinity": round(scored[0][1], 4),
            "alternates": [{"cluster": int(c), "affinity": round(a, 4)}
                            for c, a in scored[1:4]],
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--classification", required=True)
    ap.add_argument("--five-way-json", required=True,
                    help="5-way clustering JSON (for LOCI/GENERICS/etc. metadata)")
    ap.add_argument("--semantic", required=True)
    ap.add_argument("--cooccurrence", required=True)
    ap.add_argument("--k-heb-t1-divisor", type=int, default=18,
                    help="k_heb_t1 = max(2, n_heb_t1 / divisor). Default 18.")
    ap.add_argument("--k-gk-t1-divisor", type=int, default=22,
                    help="k_gk_t1 = max(2, n_gk_t1 / divisor). Default 22.")
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown", f"wa-term-anchor-{today_compact()}"
    )

    print("Loading classification...")
    with open(args.classification, encoding="utf-8") as f:
        classification = json.load(f)
    print(f"  {len(classification)} terms classified")

    print("Loading 5-way bucket info (LOCI/GENERICS/etc.)...")
    with open(args.five_way_json, encoding="utf-8") as f:
        five_way = json.load(f)
    bucket_meta = {}
    for bucket_name in ("loci", "generics", "extraction_noise", "qualifiers"):
        for entry in five_way.get(bucket_name, []):
            bucket_meta[entry["strong"]] = {
                "bucket": bucket_name.upper().replace("_", "-"),
                "transliteration": entry.get("transliteration"),
                "gloss": entry.get("gloss"),
                "lang": "H" if entry["strong"].startswith("H") else "G",
                "verse_count": entry.get("verse_count"),
                "multi_term_pct": entry.get("multi_term_pct"),
            }
    print(f"  bucketed terms (loci/generic/noise/qualifier): {len(bucket_meta)}")

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

    # Build term_meta merged
    term_meta = {}
    for s, v in classification.items():
        term_meta[s] = v
    for s, v in bucket_meta.items():
        if s not in term_meta:
            term_meta[s] = v

    # Split T1 / T2 / FLAG by language
    heb_t1 = sorted([s for s, v in classification.items()
                      if v.get("lang") == "H" and v.get("ib_type") == "T1"
                      and s in idx_map])
    heb_t2 = sorted([s for s, v in classification.items()
                      if v.get("lang") == "H" and v.get("ib_type") == "T2"
                      and s in idx_map])
    heb_flag = sorted([s for s, v in classification.items()
                        if v.get("lang") == "H" and v.get("ib_type") == "FLAG"])
    gk_t1 = sorted([s for s, v in classification.items()
                     if v.get("lang") == "G" and v.get("ib_type") == "T1"
                     and s in idx_map])
    gk_t2 = sorted([s for s, v in classification.items()
                     if v.get("lang") == "G" and v.get("ib_type") == "T2"
                     and s in idx_map])
    gk_flag = sorted([s for s, v in classification.items()
                       if v.get("lang") == "G" and v.get("ib_type") == "FLAG"])
    print(f"\n  Hebrew T1={len(heb_t1)} T2={len(heb_t2)} FLAG={len(heb_flag)}")
    print(f"  Greek  T1={len(gk_t1)} T2={len(gk_t2)} FLAG={len(gk_flag)}")

    # Cluster T1-only
    k_heb = max(2, len(heb_t1) // args.k_heb_t1_divisor)
    k_gk = max(2, len(gk_t1) // args.k_gk_t1_divisor)
    print(f"\nClustering Hebrew T1 (k={k_heb})...")
    heb_t1_indices = [idx_map[s] for s in heb_t1]
    heb_t1_labels = cluster_kmeans(combined[heb_t1_indices], k_heb)
    print(f"Clustering Greek T1 (k={k_gk})...")
    gk_t1_indices = [idx_map[s] for s in gk_t1]
    gk_t1_labels = cluster_kmeans(combined[gk_t1_indices], k_gk)

    # Build cluster info per language
    def build_cluster_catalogue(strongs, labels, lang_prefix):
        by_cluster = defaultdict(list)
        for s, lbl in zip(strongs, labels):
            by_cluster[int(lbl)].append(s)
        cat = {}
        for cid, members in by_cluster.items():
            theme = cluster_theme(members, term_meta)
            label = cluster_label_from_theme(theme)
            centroid = cluster_centroid_term(members, combined, idx_map)
            metrics = cluster_quality_metric(members, combined, idx_map, term_meta)
            cat[cid] = {
                "cluster_id": f"{lang_prefix}{cid:03d}",
                "language": "Hebrew" if lang_prefix == "H" else "Greek",
                "n_t1": len(members),
                "label": label,
                "theme": theme,
                "centroid_strong": centroid,
                "centroid_gloss": (term_meta.get(centroid) or {}).get("gloss"),
                "metrics": metrics,
                "members_t1": members,
                "members_t2": [],  # filled after attach
            }
        return cat

    heb_cat = build_cluster_catalogue(heb_t1, heb_t1_labels, "H")
    gk_cat = build_cluster_catalogue(gk_t1, gk_t1_labels, "G")
    print(f"\n  Hebrew T1 clusters: {len(heb_cat)}")
    print(f"  Greek T1 clusters:  {len(gk_cat)}")

    # Attach T2 via co-occurrence affinity
    print("\nFetching verse → terms map for T2 attachment...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    verse_terms_map = fetch_verse_to_terms(conn)
    conn.close()
    print(f"  {len(verse_terms_map):,} verse references")

    print("Attaching Hebrew T2...")
    heb_t2_attach = attach_t2_to_cluster(heb_t2, heb_t1, heb_t1_labels, verse_terms_map)
    print("Attaching Greek T2...")
    gk_t2_attach = attach_t2_to_cluster(gk_t2, gk_t1, gk_t1_labels, verse_terms_map)

    # Fold T2 into cluster catalogue
    for s, info in heb_t2_attach.items():
        cid = info["top_cluster"]
        if cid is not None:
            heb_cat[cid]["members_t2"].append({
                "strong": s, "affinity": info["affinity"]
            })
    for s, info in gk_t2_attach.items():
        cid = info["top_cluster"]
        if cid is not None:
            gk_cat[cid]["members_t2"].append({
                "strong": s, "affinity": info["affinity"]
            })

    # Build per-term anchor records
    print("\nBuilding per-term anchor records...")
    anchors = {}

    # T1 terms: cluster_id from primary clustering
    for s, lbl in zip(heb_t1, heb_t1_labels):
        cat = heb_cat[int(lbl)]
        m = term_meta[s]
        anchors[s] = {
            "strong": s,
            "lang": "H",
            "transliteration": m.get("transliteration"),
            "gloss": m.get("gloss"),
            "verse_count": m.get("verse_count"),
            "multi_term_pct": m.get("multi_term_pct"),
            "bucket": "T1",
            "cluster_id": cat["cluster_id"],
            "cluster_label": cat["label"],
            "cluster_centroid_strong": cat["centroid_strong"],
        }
    for s, lbl in zip(gk_t1, gk_t1_labels):
        cat = gk_cat[int(lbl)]
        m = term_meta[s]
        anchors[s] = {
            "strong": s,
            "lang": "G",
            "transliteration": m.get("transliteration"),
            "gloss": m.get("gloss"),
            "verse_count": m.get("verse_count"),
            "multi_term_pct": m.get("multi_term_pct"),
            "bucket": "T1",
            "cluster_id": cat["cluster_id"],
            "cluster_label": cat["label"],
            "cluster_centroid_strong": cat["centroid_strong"],
        }

    # T2 terms: cluster_id derived from attachment, with affinity
    for s, info in heb_t2_attach.items():
        cid = info["top_cluster"]
        m = term_meta[s]
        cluster_id = heb_cat[cid]["cluster_id"] if cid is not None else None
        cluster_label = heb_cat[cid]["label"] if cid is not None else None
        anchors[s] = {
            "strong": s,
            "lang": "H",
            "transliteration": m.get("transliteration"),
            "gloss": m.get("gloss"),
            "verse_count": m.get("verse_count"),
            "multi_term_pct": m.get("multi_term_pct"),
            "bucket": "T2",
            "cluster_id": cluster_id,
            "cluster_label": cluster_label,
            "attachment_affinity": info["affinity"],
            "alternate_clusters": [
                {**alt,
                 "cluster_id": heb_cat[alt["cluster"]]["cluster_id"]
                 if alt["cluster"] in heb_cat else None}
                for alt in info["alternates"]
            ],
        }
    for s, info in gk_t2_attach.items():
        cid = info["top_cluster"]
        m = term_meta[s]
        cluster_id = gk_cat[cid]["cluster_id"] if cid is not None else None
        cluster_label = gk_cat[cid]["label"] if cid is not None else None
        anchors[s] = {
            "strong": s,
            "lang": "G",
            "transliteration": m.get("transliteration"),
            "gloss": m.get("gloss"),
            "verse_count": m.get("verse_count"),
            "multi_term_pct": m.get("multi_term_pct"),
            "bucket": "T2",
            "cluster_id": cluster_id,
            "cluster_label": cluster_label,
            "attachment_affinity": info["affinity"],
            "alternate_clusters": [
                {**alt,
                 "cluster_id": gk_cat[alt["cluster"]]["cluster_id"]
                 if alt["cluster"] in gk_cat else None}
                for alt in info["alternates"]
            ],
        }

    # FLAG terms: no cluster assignment, review_required
    for s in heb_flag + gk_flag:
        v = classification[s]
        anchors[s] = {
            "strong": s,
            "lang": v.get("lang"),
            "transliteration": v.get("transliteration"),
            "gloss": v.get("gloss"),
            "verse_count": v.get("verse_count"),
            "multi_term_pct": v.get("multi_term_pct"),
            "bucket": "FLAG",
            "cluster_id": None,
            "review_required": True,
            "legacy_cluster": v.get("cluster"),
        }

    # LOCI / GENERICS / EXTRACTION-NOISE / QUALIFIERS
    for s, v in bucket_meta.items():
        if s in anchors:
            continue
        anchors[s] = {
            "strong": s,
            "lang": v.get("lang"),
            "transliteration": v.get("transliteration"),
            "gloss": v.get("gloss"),
            "verse_count": v.get("verse_count"),
            "multi_term_pct": v.get("multi_term_pct"),
            "bucket": v.get("bucket"),
            "cluster_id": None,
        }

    # Output
    out_json = out_prefix + ".json"
    out_clusters_md = out_prefix + "-clusters.md"
    out_flags_md = out_prefix + "-flags.md"
    out_summary = out_prefix + "-summary.md"

    os.makedirs(os.path.dirname(out_json), exist_ok=True)

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "classification_input": args.classification,
            "five_way_input": args.five_way_json,
            "n_terms_total": len(anchors),
            "by_bucket": dict(Counter(a["bucket"] for a in anchors.values())),
            "n_heb_t1_clusters": len(heb_cat),
            "n_gk_t1_clusters": len(gk_cat),
            "k_heb_t1": k_heb,
            "k_gk_t1": k_gk,
        },
        "clusters": {
            "hebrew": {cat["cluster_id"]: {
                **{k: v for k, v in cat.items() if k != "members_t1"},
                "members_t1": [
                    {"strong": s, **{kk: vv for kk, vv in (term_meta.get(s) or {}).items()
                                      if kk in ("transliteration", "gloss",
                                                "verse_count", "multi_term_pct")}}
                    for s in cat["members_t1"]
                ],
                "members_t2": [
                    {"strong": x["strong"], "affinity": x["affinity"],
                     **{kk: vv for kk, vv in (term_meta.get(x["strong"]) or {}).items()
                        if kk in ("transliteration", "gloss",
                                  "verse_count", "multi_term_pct")}}
                    for x in cat["members_t2"]
                ],
            } for cid, cat in heb_cat.items()},
            "greek": {cat["cluster_id"]: {
                **{k: v for k, v in cat.items() if k != "members_t1"},
                "members_t1": [
                    {"strong": s, **{kk: vv for kk, vv in (term_meta.get(s) or {}).items()
                                      if kk in ("transliteration", "gloss",
                                                "verse_count", "multi_term_pct")}}
                    for s in cat["members_t1"]
                ],
                "members_t2": [
                    {"strong": x["strong"], "affinity": x["affinity"],
                     **{kk: vv for kk, vv in (term_meta.get(x["strong"]) or {}).items()
                        if kk in ("transliteration", "gloss",
                                  "verse_count", "multi_term_pct")}}
                    for x in cat["members_t2"]
                ],
            } for cid, cat in gk_cat.items()},
        },
        "term_anchors": anchors,
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)

    # Cluster catalogue MD
    md_lines = [
        "# Term cluster catalogue (T1-driven, T2-attached)",
        "",
        f"**Generated:** {now_iso()}",
        f"**Hebrew T1 clusters:** {len(heb_cat)} (k={k_heb})",
        f"**Greek T1 clusters:** {len(gk_cat)} (k={k_gk})",
        "",
        "Per term: bucket marker = T1 (drove clustering) | T2 (attached) | "
        "FLAG (review) | LOCUS / GENERIC / EXTRACTION-NOISE / QUALIFIER (excluded).",
        "",
        "## Hebrew clusters",
        "",
    ]
    for cid in sorted(heb_cat.keys()):
        cat = heb_cat[cid]
        md_lines.append(
            f"### {cat['cluster_id']} — {cat['label']} "
            f"(T1={cat['n_t1']} + T2={len(cat['members_t2'])}, "
            f"cohesion={cat['metrics']['cohesion']}, "
            f"theme={int(cat['metrics']['theme_concentration']*100)}%)"
        )
        md_lines.append("")
        theme_str = ", ".join(f"{w}({c})" for w, c in cat["theme"][:6])
        md_lines.append(f"**Theme:** {theme_str}")
        md_lines.append(f"**Centroid:** `{cat['centroid_strong']}` — "
                         f"{cat['centroid_gloss']}")
        md_lines.append("")
        md_lines.append("**T1 members (primary):**")
        md_lines.append("")
        md_lines.append("| Strong's | translit | gloss | verses | multi% |")
        md_lines.append("|---|---|---|---|---|")
        for s in sorted(cat["members_t1"],
                         key=lambda x: ((term_meta.get(x) or {}).get("transliteration") or "").lower()):
            m = term_meta.get(s, {})
            md_lines.append(
                f"| {s} | {m.get('transliteration') or ''} | "
                f"{(m.get('gloss') or '')[:50]} | "
                f"{m.get('verse_count') or ''} | "
                f"{m.get('multi_term_pct') or ''}% |"
            )
        if cat["members_t2"]:
            md_lines.append("")
            md_lines.append("**T2 attached (qualifier-type, top affinity):**")
            md_lines.append("")
            md_lines.append("| Strong's | translit | gloss | affinity | verses | multi% |")
            md_lines.append("|---|---|---|---|---|---|")
            for entry in sorted(cat["members_t2"], key=lambda x: -x["affinity"]):
                s = entry["strong"]
                m = term_meta.get(s, {})
                md_lines.append(
                    f"| {s} | {m.get('transliteration') or ''} | "
                    f"{(m.get('gloss') or '')[:50]} | "
                    f"{entry['affinity']:.3f} | "
                    f"{m.get('verse_count') or ''} | "
                    f"{m.get('multi_term_pct') or ''}% |"
                )
        md_lines.append("")
    md_lines.append("## Greek clusters")
    md_lines.append("")
    for cid in sorted(gk_cat.keys()):
        cat = gk_cat[cid]
        md_lines.append(
            f"### {cat['cluster_id']} — {cat['label']} "
            f"(T1={cat['n_t1']} + T2={len(cat['members_t2'])}, "
            f"cohesion={cat['metrics']['cohesion']}, "
            f"theme={int(cat['metrics']['theme_concentration']*100)}%)"
        )
        md_lines.append("")
        theme_str = ", ".join(f"{w}({c})" for w, c in cat["theme"][:6])
        md_lines.append(f"**Theme:** {theme_str}")
        md_lines.append(f"**Centroid:** `{cat['centroid_strong']}` — "
                         f"{cat['centroid_gloss']}")
        md_lines.append("")
        md_lines.append("**T1 members (primary):**")
        md_lines.append("")
        md_lines.append("| Strong's | translit | gloss | verses | multi% |")
        md_lines.append("|---|---|---|---|---|")
        for s in sorted(cat["members_t1"],
                         key=lambda x: ((term_meta.get(x) or {}).get("transliteration") or "").lower()):
            m = term_meta.get(s, {})
            md_lines.append(
                f"| {s} | {m.get('transliteration') or ''} | "
                f"{(m.get('gloss') or '')[:50]} | "
                f"{m.get('verse_count') or ''} | "
                f"{m.get('multi_term_pct') or ''}% |"
            )
        if cat["members_t2"]:
            md_lines.append("")
            md_lines.append("**T2 attached:**")
            md_lines.append("")
            md_lines.append("| Strong's | translit | gloss | affinity | verses | multi% |")
            md_lines.append("|---|---|---|---|---|---|")
            for entry in sorted(cat["members_t2"], key=lambda x: -x["affinity"]):
                s = entry["strong"]
                m = term_meta.get(s, {})
                md_lines.append(
                    f"| {s} | {m.get('transliteration') or ''} | "
                    f"{(m.get('gloss') or '')[:50]} | "
                    f"{entry['affinity']:.3f} | "
                    f"{m.get('verse_count') or ''} | "
                    f"{m.get('multi_term_pct') or ''}% |"
                )
        md_lines.append("")
    with open(out_clusters_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    # FLAG MD
    flag_lines = [
        "# FLAG terms — manual review required",
        "",
        f"**Generated:** {now_iso()}",
        f"**Total FLAGs:** {len(heb_flag) + len(gk_flag)}",
        "",
        "These terms were flagged in the T1/T2 classification as borderline "
        "or requiring manual decision. They are NOT assigned to any cluster.",
        "",
        "| Strong's | lang | translit | gloss | legacy cluster | verses |",
        "|---|---|---|---|---|---|",
    ]
    for s in heb_flag + gk_flag:
        v = classification[s]
        flag_lines.append(
            f"| {s} | {v.get('lang')} | {v.get('transliteration') or ''} | "
            f"{(v.get('gloss') or '')[:50]} | C{v.get('cluster')} | "
            f"{v.get('verse_count') or ''} |"
        )
    with open(out_flags_md, "w", encoding="utf-8") as f:
        f.write("\n".join(flag_lines))

    # Summary
    summary_lines = [
        "# Term anchor build — summary",
        "",
        f"**Generated:** {now_iso()}",
        "",
        "## Bucket distribution",
        "",
        "| Bucket | Count | Role |",
        "|---|---|---|",
    ]
    bucket_counts = Counter(a["bucket"] for a in anchors.values())
    role_descriptions = {
        "T1": "Primary characteristics — drove clustering",
        "T2": "Secondary characteristics — attached to T1 cluster via co-occurrence",
        "FLAG": "Borderline — review required",
        "LOCUS": "Inner-being seat term — clustered separately",
        "GENERIC": "Function word — excluded",
        "EXTRACTION-NOISE": "Physical object — excluded",
        "QUALIFIER": "Adverb / intensifier — excluded from primary clustering",
    }
    for b in ("T1", "T2", "FLAG", "LOCUS", "GENERIC", "EXTRACTION-NOISE", "QUALIFIER"):
        summary_lines.append(
            f"| {b} | {bucket_counts.get(b, 0)} | {role_descriptions.get(b,'')} |"
        )
    summary_lines += [
        "",
        f"**Total anchored terms:** {len(anchors)}",
        "",
        "## Cluster catalogue",
        "",
        f"- Hebrew T1 clusters: **{len(heb_cat)}** (k={k_heb})",
        f"- Greek T1 clusters: **{len(gk_cat)}** (k={k_gk})",
        "",
        "## Cluster ID format",
        "",
        "Cluster IDs use `H001` / `G001` style. Each term carries its anchor "
        "as `cluster_id` in the per-term JSON, plus a derived `cluster_label` "
        "(the top theme words). T2 terms also carry `attachment_affinity`.",
    ]
    with open(out_summary, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))

    print(f"\nWrote: {out_json}")
    print(f"Wrote: {out_clusters_md}")
    print(f"Wrote: {out_flags_md}")
    print(f"Wrote: {out_summary}")
    print(f"\nBucket distribution: {dict(bucket_counts)}")
    print(f"Hebrew T1 clusters: {len(heb_cat)} | Greek T1 clusters: {len(gk_cat)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
