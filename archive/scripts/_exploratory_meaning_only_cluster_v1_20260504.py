"""_exploratory_meaning_only_cluster_v1_20260504.py — read-only.

Hypothesis test: does dropping verse-share + verse-count (analytic criteria)
and using ONLY semantic meaning (root + gloss + meaning, weighted) produce
coherent named-characteristic clusters?

Specifically: does the love-faculty (aheb/ahavah/chesed/racham/dod/yadid in
Hebrew + agape/agapaō/agapētos/fileō/philos in Greek) cluster together when
verse-co-occurrence is removed from the signal?

Inputs:
  outputs/markdown/term-semantic-weighted-vectors-20260504.npz
  outputs/markdown/wa-term-anchor-20260504.json   (for OWNER filter + glosses)

Outputs:
  outputs/markdown/wa-meaning-only-clusters-{date}.json
  outputs/markdown/wa-meaning-only-clusters-{date}.md
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np
from sklearn.cluster import KMeans

NPZ_PATH = "outputs/markdown/term-semantic-weighted-vectors-20260504.npz"
ANCHOR_JSON = "outputs/markdown/wa-term-anchor-20260504.json"
DATE = "20260504"

# Probe sets — terms we want to track to test cluster coherence
PROBES = {
    "love-faculty": [
        # Hebrew aheb/ahavah/ahav/chesed/racham/dod/yadid family
        "H0157G", "H0157H", "H0158", "H0160",
        "H2617A",
        "H7355", "H7356A", "H7356B", "H7349", "H7359", "H7362",
        "H4263", "H2551", "H2550",
        "H1730G", "H1730H", "H1730I", "H3039A", "H3033",
        # Greek agape/phileo/agapetos
        "G0025", "G0026", "G0027",
        "G5360", "G5361", "G5362", "G5363",
        "G5368", "G5373", "G5384", "G5387", "G5388", "G5377",
        "G5370", "G2705",
        "G3628",  # oiktirmos compassion
    ],
    "fear-faculty": [
        # Hebrew yare/pachad/charad/ragaz family
        "H3372G", "H3372H", "H3374", "H3373",
        "H6342", "H6343", "H6345",
        "H2729", "H2730", "H2731",
        "H7264",
        # Greek fobeo/fobos
        "G5398", "G5399", "G5401", "G5156",
    ],
    "joy-faculty": [
        # Hebrew samach/simchah/sasvon/ranan/sus/gil family
        "H8055", "H8056", "H8057", "H8342",
        "H7442B", "H7440",
        "H7797",
        "H1523", "H1524A", "H1525",
        "H4885", "H0160",  # ahavah is in joy cluster currently — check
        # Greek chairo/chara/agalliao
        "G5463", "G5479", "G0021", "G0020",
    ],
    "anger-faculty": [
        # Hebrew charah/charon/chemah/qatsaph/qana family
        "H2734", "H2740", "H2534",
        "H7107", "H7110A",
        "H7065", "H7068",
        "H0599",
        # Greek orge/orgizo/parorgizo
        "G3709", "G3710", "G3949", "G3950",
    ],
    "hope-faculty": [
        # Hebrew yachal/qavah/tikvah/batach
        "H3176G", "H3176H", "H3175",
        "H6960A", "H8615B",
        "H0982", "H0983", "H4009",
        "H8431",  # tochelet hope
        # Greek elpis/elpizo
        "G1679", "G1680",
    ],
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_anchor_lookup():
    """Build {strongs: {gloss, language, bucket, cluster_id, ...}} from anchor JSON."""
    with open(ANCHOR_JSON, encoding="utf-8") as f:
        data = json.load(f)
    out = data.get("term_anchors", {})
    return out, data


def load_vectors():
    z = np.load(NPZ_PATH, allow_pickle=True)
    return {
        "strongs": z["strongs"],
        "vectors": z["vectors"],
        "languages": z["languages"],
        "registries": z["registries"],
    }


def cluster_at_k(vectors, k, seed=42):
    print(f"  k-means k={k}...", flush=True)
    km = KMeans(n_clusters=k, random_state=seed, n_init=10)
    labels = km.fit_predict(vectors)
    return labels, km


def report_probe_coherence(probes, strongs, labels):
    """For each probe set, count how many distinct clusters its members span."""
    s_to_idx = {s: i for i, s in enumerate(strongs)}
    out = {}
    for name, term_list in probes.items():
        found = []
        for t in term_list:
            if t in s_to_idx:
                found.append((t, int(labels[s_to_idx[t]])))
        cluster_counts = Counter(c for _, c in found)
        out[name] = {
            "probe_size": len(term_list),
            "found_in_vectors": len(found),
            "distinct_clusters": len(cluster_counts),
            "cluster_distribution": dict(cluster_counts),
            "members_by_cluster": defaultdict(list),
        }
        for t, c in found:
            out[name]["members_by_cluster"][c].append(t)
        out[name]["members_by_cluster"] = dict(out[name]["members_by_cluster"])
    return out


def main():
    print("Loading vectors...", flush=True)
    v = load_vectors()
    print(f"  shape: {v['vectors'].shape}, terms: {len(v['strongs'])}",
          flush=True)
    print(f"  languages: {Counter(v['languages'])}", flush=True)

    print("Loading anchor JSON...", flush=True)
    anchor_lookup, anchor_root = load_anchor_lookup()
    print(f"  anchor terms keyed by Strong's: {len(anchor_lookup)}", flush=True)

    # Filter to OWNER terms only — using the anchor JSON to determine bucket.
    # The anchor JSON may have terms keyed differently; we'll filter where
    # a term has bucket in {T1, T2, FLAG, EXTRACTION-NOISE} (i.e., aligned)
    # OR fall back to using all terms if anchor structure is unknown.
    if anchor_lookup:
        valid_strongs = set(anchor_lookup.keys())
        mask = np.array([s in valid_strongs for s in v["strongs"]])
    else:
        mask = np.ones(len(v["strongs"]), dtype=bool)

    print(f"  retained after anchor filter: {mask.sum():,} / {len(mask):,}",
          flush=True)
    strongs = v["strongs"][mask]
    vectors = v["vectors"][mask]
    languages = v["languages"][mask]

    results = {
        "generated": now_iso(),
        "method": "kmeans on weighted semantic vectors only "
                  "(root 35% + gloss 35% + meaning 30%); "
                  "co-occurrence + usage signals EXCLUDED",
        "input_npz": NPZ_PATH,
        "n_terms": int(len(strongs)),
        "lang_distribution": dict(Counter(languages.tolist())),
        "ks_tested": [],
    }

    for k in [40, 60, 80, 120, 180]:
        labels, km = cluster_at_k(vectors, k)
        # Cluster size distribution
        sizes = Counter(int(l) for l in labels)
        # Cross-language: how many clusters contain BOTH H and G?
        cluster_lang_mix = defaultdict(set)
        for i, l in enumerate(labels):
            cluster_lang_mix[int(l)].add(str(languages[i]))
        n_mixed = sum(1 for langs in cluster_lang_mix.values()
                      if "Hebrew" in langs and "Greek" in langs)
        # Probe coherence
        probe_results = report_probe_coherence(PROBES, strongs, labels)
        results["ks_tested"].append({
            "k": k,
            "size_min": min(sizes.values()),
            "size_max": max(sizes.values()),
            "size_median": int(np.median(list(sizes.values()))),
            "size_mean": round(float(np.mean(list(sizes.values()))), 1),
            "n_clusters_mixed_lang": n_mixed,
            "probes": probe_results,
        })
        # Save labels for the chosen k inline
        if k in (60, 120):
            results[f"labels_k{k}"] = {
                str(s): int(l) for s, l in zip(strongs, labels)
            }
            results[f"cluster_members_k{k}"] = {
                str(c): [str(s) for s, ll in zip(strongs, labels) if ll == c]
                for c in range(k)
            }

    out_json = f"outputs/markdown/wa-meaning-only-clusters-{DATE}.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Wrote: {out_json}", flush=True)

    # Also write a brief markdown headline
    out_md = f"outputs/markdown/wa-meaning-only-clusters-{DATE}.md"
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# Meaning-only clustering — probe results\n\n")
        f.write(f"**Generated:** {results['generated']}  \n")
        f.write(f"**Method:** {results['method']}  \n")
        f.write(f"**Terms:** {results['n_terms']:,}  \n")
        f.write(f"**Language distribution:** "
                f"{results['lang_distribution']}\n\n")
        f.write("## Per-k summary\n\n")
        f.write("| k | min size | median | max | "
                "cross-lang clusters | love distinct | "
                "fear distinct | joy distinct | anger distinct | "
                "hope distinct |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|\n")
        for r in results["ks_tested"]:
            f.write(f"| {r['k']} | {r['size_min']} | "
                    f"{r['size_median']} | {r['size_max']} | "
                    f"{r['n_clusters_mixed_lang']} | "
                    f"{r['probes']['love-faculty']['distinct_clusters']} | "
                    f"{r['probes']['fear-faculty']['distinct_clusters']} | "
                    f"{r['probes']['joy-faculty']['distinct_clusters']} | "
                    f"{r['probes']['anger-faculty']['distinct_clusters']} | "
                    f"{r['probes']['hope-faculty']['distinct_clusters']} |\n")
        f.write("\n*Lower 'distinct' counts = the faculty's terms cluster "
                "together more tightly. Distinct=1 means perfect coherence.*\n")
    print(f"Wrote: {out_md}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
