"""_exploratory_term_cluster_crosslang_v1_20260504.py — read-only.

Cross-language alignment between Hebrew and Greek characteristic clusters.

Premise: Hebrew/Greek clusters can't align via verse co-occurrence (no
shared verses), but they CAN align via the semantic vector (gloss + root
+ meaning text — the language-bridging signal).

Method:
  1. For each cluster, build a SEMANTIC-ONLY centroid (mean of members'
     weighted-semantic-vectors — root + gloss + meaning). Co-occurrence
     vector excluded since it's language-locked.
  2. Compute pairwise cosine similarity between every Hebrew and Greek
     centroid.
  3. For each Greek cluster, find top-3 nearest Hebrew clusters.
  4. Classify alignment:
     - ALIGNED      — top-1 similarity >= 0.55 AND theme overlap >= 1
     - PARTIAL      — 0.40 <= top-1 < 0.55, OR strong sim but no shared theme word
     - ORPHAN       — top-1 < 0.40 (no close Hebrew counterpart)
  5. Report orphan Greek clusters with hypothesised reason.

Outputs:
  outputs/markdown/term-clusters-crosslang-{date}.md
  outputs/markdown/term-clusters-crosslang-{date}.json
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


def build_centroid(members, sem_vec, sem_idx):
    """Mean of members' semantic-only vectors (no co-occurrence)."""
    indices = [sem_idx[s] for s in members if s in sem_idx]
    if not indices:
        return None
    v = sem_vec[indices]
    centroid = v.mean(axis=0)
    norm = np.linalg.norm(centroid)
    if norm == 0:
        return None
    return centroid / norm


def cluster_themes_set(members, term_meta, top_k=10):
    counter = Counter()
    for s in members:
        for t in gloss_tokens((term_meta.get(s) or {}).get("gloss") or ""):
            counter[t] += 1
    return set(w for w, _ in counter.most_common(top_k))


def cluster_top_themes(members, term_meta, top_k=8):
    counter = Counter()
    for s in members:
        for t in gloss_tokens((term_meta.get(s) or {}).get("gloss") or ""):
            counter[t] += 1
    return counter.most_common(top_k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-json", required=True,
                    help="5-way cluster JSON")
    ap.add_argument("--semantic", required=True,
                    help="weighted semantic vector .npz")
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown",
        f"term-clusters-crosslang-{today_compact()}"
    )

    print("Loading inputs...")
    with open(args.input_json, encoding="utf-8") as f:
        data = json.load(f)
    arr = np.load(args.semantic, allow_pickle=False)
    sem_strongs = arr["strongs"]
    sem_vec = arr["vectors"]
    sem_idx = {str(s): i for i, s in enumerate(sem_strongs)}

    # Build term meta lookup
    term_meta = {}
    for k in ("loci", "characteristics_hebrew", "characteristics_greek",
              "qualifiers", "generics", "extraction_noise"):
        for e in data.get(k, []):
            term_meta[e["strong"]] = e

    # Build cluster maps
    heb_clusters = defaultdict(list)
    for e in data["characteristics_hebrew"]:
        heb_clusters[int(e["cluster"])].append(e["strong"])
    gk_clusters = defaultdict(list)
    for e in data["characteristics_greek"]:
        gk_clusters[int(e["cluster"])].append(e["strong"])

    def member_records(strong_list):
        """Return [{strong, translit, gloss, verse_count, multi_term_pct}]
        sorted by transliteration."""
        out = []
        for s in strong_list:
            m = term_meta.get(s, {})
            out.append({
                "strong": s,
                "transliteration": m.get("transliteration"),
                "gloss": m.get("gloss"),
                "verse_count": m.get("verse_count"),
                "multi_term_pct": m.get("multi_term_pct"),
            })
        out.sort(key=lambda x: ((x.get("transliteration") or "").lower()))
        return out

    print(f"  Hebrew clusters: {len(heb_clusters)}")
    print(f"  Greek clusters:  {len(gk_clusters)}")

    # Build centroids and theme sets
    heb_data = {}
    for cid, members in heb_clusters.items():
        c = build_centroid(members, sem_vec, sem_idx)
        if c is None:
            continue
        heb_data[cid] = {
            "centroid": c,
            "themes_set": cluster_themes_set(members, term_meta),
            "top_themes": cluster_top_themes(members, term_meta),
            "size": len(members),
            "members": member_records(members),
        }

    gk_data = {}
    for cid, members in gk_clusters.items():
        c = build_centroid(members, sem_vec, sem_idx)
        if c is None:
            continue
        gk_data[cid] = {
            "centroid": c,
            "themes_set": cluster_themes_set(members, term_meta),
            "top_themes": cluster_top_themes(members, term_meta),
            "size": len(members),
            "members": member_records(members),
        }

    # Compute Greek -> Hebrew similarity
    print("\nComputing cross-language alignment...")
    heb_ids = list(heb_data.keys())
    heb_centroids = np.stack([heb_data[c]["centroid"] for c in heb_ids])

    alignment = []
    for gk_id, gk_info in gk_data.items():
        sims = heb_centroids @ gk_info["centroid"]
        # Top-3 Hebrew matches
        top_idx = np.argsort(-sims)[:3]
        tops = []
        for i in top_idx:
            heb_id = heb_ids[i]
            sim = float(sims[i])
            heb_themes = heb_data[heb_id]["themes_set"]
            gk_themes = gk_info["themes_set"]
            overlap = sorted(heb_themes & gk_themes)
            tops.append({
                "hebrew_cluster": heb_id,
                "similarity": round(sim, 4),
                "shared_themes": overlap,
                "n_shared": len(overlap),
                "hebrew_size": heb_data[heb_id]["size"],
                "hebrew_top_themes": heb_data[heb_id]["top_themes"][:6],
                "hebrew_members": heb_data[heb_id]["members"],
            })

        top1 = tops[0]
        if top1["similarity"] >= 0.55 and top1["n_shared"] >= 1:
            verdict = "ALIGNED"
        elif top1["similarity"] >= 0.40:
            verdict = "PARTIAL"
        else:
            verdict = "ORPHAN"

        alignment.append({
            "greek_cluster": gk_id,
            "greek_size": gk_info["size"],
            "greek_top_themes": gk_info["top_themes"][:6],
            "greek_members": gk_info["members"],
            "verdict": verdict,
            "top_matches": tops,
        })

    # Reverse: Hebrew -> Greek (for orphan-Hebrew detection)
    gk_ids = list(gk_data.keys())
    gk_centroids = np.stack([gk_data[c]["centroid"] for c in gk_ids])

    heb_alignment = []
    for heb_id, heb_info in heb_data.items():
        sims = gk_centroids @ heb_info["centroid"]
        top_idx = np.argsort(-sims)[:3]
        tops = []
        for i in top_idx:
            gid = gk_ids[i]
            sim = float(sims[i])
            heb_themes = heb_info["themes_set"]
            g_themes = gk_data[gid]["themes_set"]
            overlap = sorted(heb_themes & g_themes)
            tops.append({
                "greek_cluster": gid,
                "similarity": round(sim, 4),
                "shared_themes": overlap,
                "n_shared": len(overlap),
                "greek_size": gk_data[gid]["size"],
                "greek_top_themes": gk_data[gid]["top_themes"][:6],
                "greek_members": gk_data[gid]["members"],
            })
        top1 = tops[0]
        if top1["similarity"] >= 0.55 and top1["n_shared"] >= 1:
            verdict = "ALIGNED"
        elif top1["similarity"] >= 0.40:
            verdict = "PARTIAL"
        else:
            verdict = "ORPHAN"
        heb_alignment.append({
            "hebrew_cluster": heb_id,
            "hebrew_size": heb_info["size"],
            "hebrew_top_themes": heb_info["top_themes"][:6],
            "hebrew_members": heb_info["members"],
            "verdict": verdict,
            "top_matches": tops,
        })

    verdict_counts_gk = Counter(a["verdict"] for a in alignment)
    verdict_counts_heb = Counter(a["verdict"] for a in heb_alignment)

    print(f"\nGreek -> Hebrew alignment:")
    for v in ("ALIGNED", "PARTIAL", "ORPHAN"):
        print(f"  {v}: {verdict_counts_gk[v]}")
    print(f"\nHebrew -> Greek alignment:")
    for v in ("ALIGNED", "PARTIAL", "ORPHAN"):
        print(f"  {v}: {verdict_counts_heb[v]}")

    # Render markdown
    md_lines = [
        "# Hebrew/Greek cluster cross-language alignment",
        "",
        f"**Generated:** {now_iso()}",
        f"**Hebrew clusters analysed:** {len(heb_data)}",
        f"**Greek clusters analysed:** {len(gk_data)}",
        "",
        "## Method",
        "",
        "Each cluster's centroid is computed in the **semantic-only vector space** "
        "(weighted root + gloss + meaning). Co-occurrence vectors are excluded "
        "because they're language-locked (Hebrew/Greek share no verses). "
        "Cosine similarity between Greek and Hebrew centroids quantifies "
        "lexical-semantic alignment. Theme-word overlap quantifies shared "
        "vocabulary.",
        "",
        "Verdict scale:",
        "- **ALIGNED** — top-1 similarity ≥ 0.55 AND ≥ 1 shared theme word",
        "- **PARTIAL** — 0.40 ≤ top-1 < 0.55, OR sim high but no shared theme",
        "- **ORPHAN** — top-1 < 0.40 (no close Hebrew counterpart)",
        "",
        "## Greek → Hebrew verdicts",
        "",
        "| Verdict | Count |",
        "|---|---|",
        f"| ALIGNED | {verdict_counts_gk['ALIGNED']} |",
        f"| PARTIAL | {verdict_counts_gk['PARTIAL']} |",
        f"| ORPHAN | {verdict_counts_gk['ORPHAN']} |",
        "",
        "## Hebrew → Greek verdicts",
        "",
        "| Verdict | Count |",
        "|---|---|",
        f"| ALIGNED | {verdict_counts_heb['ALIGNED']} |",
        f"| PARTIAL | {verdict_counts_heb['PARTIAL']} |",
        f"| ORPHAN | {verdict_counts_heb['ORPHAN']} |",
        "",
    ]

    # Greek cluster-by-cluster
    for verdict_label in ("ALIGNED", "PARTIAL", "ORPHAN"):
        md_lines.append(f"## Greek clusters — {verdict_label}")
        md_lines.append("")
        for a in sorted(
            [x for x in alignment if x["verdict"] == verdict_label],
            key=lambda x: (-x["top_matches"][0]["similarity"], x["greek_cluster"])
        ):
            top1 = a["top_matches"][0]
            gk_themes_str = ", ".join(f"{w}({c})" for w, c in a["greek_top_themes"])
            md_lines.append(
                f"### Greek C{a['greek_cluster']} (n={a['greek_size']}) → "
                f"Hebrew C{top1['hebrew_cluster']} "
                f"(sim={top1['similarity']}, shared={top1['n_shared']})"
            )
            md_lines.append("")
            md_lines.append(f"**Greek theme:** {gk_themes_str}")
            md_lines.append("")
            md_lines.append("Top 3 Hebrew matches:")
            md_lines.append("")
            md_lines.append("| Rank | Hebrew C | sim | shared themes | Hebrew theme |")
            md_lines.append("|---|---|---|---|---|")
            for rank, m in enumerate(a["top_matches"], 1):
                heb_themes_str = ", ".join(f"{w}({c})" for w, c in m["hebrew_top_themes"])
                shared_str = ", ".join(m["shared_themes"]) if m["shared_themes"] else "—"
                md_lines.append(
                    f"| {rank} | C{m['hebrew_cluster']} (n={m['hebrew_size']}) | "
                    f"{m['similarity']} | {shared_str} | {heb_themes_str} |"
                )
            md_lines.append("")

    md_lines.append("## Hebrew clusters with no close Greek counterpart (ORPHAN)")
    md_lines.append("")
    heb_orphans = [x for x in heb_alignment if x["verdict"] == "ORPHAN"]
    md_lines.append(f"Count: {len(heb_orphans)}")
    md_lines.append("")
    if heb_orphans:
        md_lines.append("| Hebrew C | n | top sim to Greek | Hebrew theme |")
        md_lines.append("|---|---|---|---|")
        for h in sorted(heb_orphans, key=lambda x: -x["hebrew_size"]):
            top1 = h["top_matches"][0]
            heb_themes_str = ", ".join(f"{w}({c})" for w, c in h["hebrew_top_themes"])
            md_lines.append(
                f"| C{h['hebrew_cluster']} | {h['hebrew_size']} | "
                f"{top1['similarity']} (G C{top1['greek_cluster']}) | "
                f"{heb_themes_str} |"
            )

    out_md = out_prefix + ".md"
    out_json = out_prefix + ".json"
    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_hebrew_clusters": len(heb_data),
            "n_greek_clusters": len(gk_data),
            "verdict_counts_gk_to_heb": dict(verdict_counts_gk),
            "verdict_counts_heb_to_gk": dict(verdict_counts_heb),
        },
        "greek_to_hebrew": alignment,
        "hebrew_to_greek": heb_alignment,
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"\nWrote: {out_md}")
    print(f"Wrote: {out_json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
