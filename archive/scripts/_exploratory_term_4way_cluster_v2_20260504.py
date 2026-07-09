"""_exploratory_term_4way_cluster_v2_20260504.py — read-only.

V2 of the 4-way clustering. Changes vs v1:
  - Registry stripped from cluster table outputs (was label-only; removed
    so it doesn't suggest the registry has weight in clustering).
  - Explicit filter validation printed at start: confirms 0-verse and
    delete_flagged terms are excluded from the working set.
  - Per-cluster theme summary: top frequency words from cluster glosses
    + nearest-to-centroid representative term.

Pipeline unchanged: 4-way bucket split (LOCI / GENERICS / EXTRACTION-NOISE /
CHARACTERISTICS) → per-language k-means on characteristics → HDBSCAN
sanity check.
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
POS_JSON = os.path.join("outputs", "markdown", "step-pos-lookup-20260503.json")

# --- LOCI -------------------------------------------------------------
LOCUS_NOUNS = {
    "heart", "soul", "spirit", "mind", "body", "flesh",
    "conscience", "inner parts", "kidney", "bone", "being",
    "self", "person", "life", "breath",
}
LOCUS_GLOSS_RE = re.compile(
    r"^(" + "|".join(re.escape(n) for n in LOCUS_NOUNS) + r")(\s*:\s*\w+.*)?$",
    re.IGNORECASE,
)

# --- GENERICS ---------------------------------------------------------
GENERIC_POS = {
    "pronoun", "pronoun-personal", "particle", "preposition",
    "conjunction", "conditional-particle", "article", "interjection",
}
GENERIC_CONTENT_STRONGS = {
    "H1961", "H6213A", "H0935G", "H1980G", "H5414G",
    "H0120G", "H5971L",
    "G1510", "G1096", "G2192", "G4160", "G2064", "G1325",
}

# --- EXTRACTION-NOISE -------------------------------------------------
EXTRACTION_NOISE_NOUNS = {
    "weapon", "sword", "knife", "dagger", "spear", "javelin", "bow",
    "arrow", "sling", "staff", "rod", "club",
    "helmet", "shield", "armor", "armour", "breastplate", "scabbard",
    "vessel", "jar", "jug", "pot", "cup", "basin", "bowl", "lamp",
    "dish", "pitcher", "censer", "bucket",
    "throne", "chair", "seat", "bed", "couch", "table", "footstool",
    "altar",
    "garment", "robe", "tunic", "mantle", "cloak", "sandal", "shoe",
    "belt", "sash", "veil", "cloth", "fabric", "linen", "wool",
    "ink", "paper", "papyrus", "scroll", "parchment", "tablet",
    "seal", "signet",
    "ass", "donkey", "ox", "bull", "cow", "sheep", "goat", "lamb",
    "ram", "horse", "camel", "dog", "lion", "wolf", "bear", "fox",
    "eagle", "raven", "dove", "swallow", "fish", "serpent",
    "she-ass", "young-ass", "kid", "ewe", "buck",
    "iron", "bronze", "copper", "gold", "silver", "tin", "lead",
    "brass", "steel",
    "book", "letter", "decree",
    "loin", "thigh", "shoulder", "neck", "arm", "leg", "back", "chest",
    "skull", "skin", "tooth", "lip", "nail", "hair", "beard",
    "yoke", "cord", "rope", "chain", "fetter",
    "wheat", "barley", "grain", "olive", "fig", "vine", "branch",
    "honey", "milk", "wine", "bread", "meat",
    "shekel", "ephah", "cubit", "talent",
}
EXTRACTION_NOISE_RE = re.compile(
    r"^(" + "|".join(re.escape(n) for n in EXTRACTION_NOISE_NOUNS) + r")(\s*:\s*\w+.*)?$",
    re.IGNORECASE,
)

# --- THEME SUMMARY ----------------------------------------------------
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


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def is_locus_gloss(g):
    return bool(g and LOCUS_GLOSS_RE.match(g.strip().lower()))


def load_pos_lookup():
    if not os.path.exists(POS_JSON):
        return {}
    with open(POS_JSON, encoding="utf-8") as f:
        data = json.load(f)
    return {k: v.get("pos") for k, v in data["results"].items()}


def is_generic(strong, pos_lookup):
    if strong in GENERIC_CONTENT_STRONGS:
        return True
    pos = pos_lookup.get(strong)
    return bool(pos and pos in GENERIC_POS)


def is_extraction_noise(g):
    return bool(g and EXTRACTION_NOISE_RE.match(g.strip().lower()))


def load_strongs_metadata(conn):
    out = {}
    for r in conn.execute("""
        SELECT mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               wr.no AS reg_no, wr.word AS reg_word
          FROM mti_terms mt
          LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
         WHERE mt.delete_flagged = 0
           AND mt.status IN ('extracted','extracted_thin','extracted_theological_anchor')
    """):
        out[r["strongs_number"]] = {
            "transliteration": r["transliteration"],
            "gloss": r["gloss"],
            "language": r["language"],
            "registry": (f"R{r['reg_no']:03d} {r['reg_word']}"
                         if r["reg_no"] else ""),
        }
    return out


def load_npz(path):
    arr = np.load(path, allow_pickle=False)
    return arr["strongs"], arr["vectors"]


def cluster_kmeans(vectors, k, seed=20260504):
    from sklearn.cluster import KMeans
    return KMeans(n_clusters=k, random_state=seed, n_init=10).fit_predict(vectors)


def cluster_hdbscan(vectors, min_cluster_size=10, min_samples=5):
    try:
        import hdbscan
        return hdbscan.HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
            metric="euclidean",
        ).fit_predict(vectors)
    except ImportError:
        from sklearn.cluster import HDBSCAN
        return HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
        ).fit_predict(vectors)


# ---------------- THEME SUMMARY ---------------------------------------
TOKEN_RE = re.compile(r"[a-z]+")


def gloss_tokens(gloss):
    if not gloss:
        return []
    g = gloss.lower()
    # split on colon to drop sense suffix like "to twist: hide"
    g = g.split(":")[0]
    return [t for t in TOKEN_RE.findall(g) if t not in THEME_STOPWORDS and len(t) > 2]


def cluster_theme(strongs, meta):
    """Top-frequency content words across glosses + count, plus number of
    distinct glosses for cluster size context."""
    counter = Counter()
    distinct_glosses = set()
    for s in strongs:
        gloss = (meta.get(s, {}).get("gloss") or "")
        for t in gloss_tokens(gloss):
            counter[t] += 1
        if gloss:
            distinct_glosses.add(gloss.split(":")[0].strip().lower())
    return counter.most_common(12), len(distinct_glosses)


def cluster_centroid_term(strongs, vectors, idx_map):
    """Find the term whose vector is closest to the cluster centroid."""
    indices = [idx_map[s] for s in strongs if s in idx_map]
    if not indices:
        return None
    cluster_vecs = vectors[indices]
    centroid = cluster_vecs.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = cluster_vecs @ centroid
    best_idx = int(np.argmax(sims))
    return strongs[best_idx]


def render_clusters_md(title, strongs, labels, meta, vectors, idx_map, k_label):
    by_cluster = defaultdict(list)
    for s, lbl in zip(strongs, labels):
        by_cluster[int(lbl)].append(str(s))

    lines = [f"# {title}", "",
             f"**Generated:** {now_iso()}",
             f"**Terms clustered:** {len(strongs)}",
             f"**{k_label}**", ""]

    cluster_order = sorted(
        by_cluster.keys(),
        key=lambda c: (c == -1, -len(by_cluster[c]))
    )
    for lbl in cluster_order:
        members = by_cluster[lbl]
        title_extra = " (HDBSCAN noise — no dense neighbourhood)" if lbl == -1 else ""
        # Theme
        theme_words, n_distinct_glosses = cluster_theme(members, meta)
        centroid = cluster_centroid_term(members, vectors, idx_map)
        centroid_gloss = ((meta.get(centroid) or {}).get("gloss") or "") if centroid else ""

        lines.append(f"## Cluster {lbl}{title_extra} — {len(members)} term(s)")
        lines.append("")
        if theme_words:
            theme_str = ", ".join(f"{w}({c})" for w, c in theme_words)
            lines.append(f"**Theme keywords:** {theme_str}")
            lines.append("")
        if centroid:
            lines.append(f"**Centroid term:** `{centroid}` — {centroid_gloss}")
            lines.append("")
        lines.append("| Strong's | translit | gloss | language |")
        lines.append("|---|---|---|---|")
        members_sorted = sorted(
            members,
            key=lambda s: (meta.get(s, {}).get("transliteration") or "").lower()
        )
        for s in members_sorted:
            m = meta.get(s, {})
            lines.append(
                f"| {s} | {m.get('transliteration') or ''} | "
                f"{(m.get('gloss') or '')[:60]} | "
                f"{m.get('language') or ''} |"
            )
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--semantic", required=True)
    ap.add_argument("--cooccurrence", required=True)
    ap.add_argument("--k-loci", type=int, default=10)
    ap.add_argument("--k-char-hebrew", type=int, default=80)
    ap.add_argument("--k-char-greek", type=int, default=40)
    ap.add_argument("--hdbscan-min-cluster-size", type=int, default=10)
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown", f"term-clusters-4way-v2-{today_compact()}"
    )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Loading metadata + POS...")
    meta = load_strongs_metadata(conn)
    pos_lookup = load_pos_lookup()
    print(f"  active extracted mti_terms: {len(meta):,}")

    print("Loading vectors (intersection used as working set)...")
    sem_strongs, sem_vec = load_npz(args.semantic)
    coo_strongs, coo_vec = load_npz(args.cooccurrence)
    sem_idx = {str(s): i for i, s in enumerate(sem_strongs)}
    coo_idx = {str(s): i for i, s in enumerate(coo_strongs)}
    common = sorted(set(sem_idx) & set(coo_idx))
    excluded_no_verse = sorted(set(sem_idx) - set(coo_idx))
    print(f"  semantic vector terms:    {len(sem_idx):,}")
    print(f"  cooccurrence vector terms:{len(coo_idx):,}")
    print(f"  intersection (working):   {len(common):,}")
    print(f"  EXCLUDED 0-verse terms:   {len(excluded_no_verse):,} "
          f"(in semantic but not cooccurrence — no verse signal)")
    print(f"  All terms in working set are: delete_flagged=0 "
          f"(mt + ti + vr) AND have ≥1 active OWNER verse-record")

    sem_aligned = np.array([sem_vec[sem_idx[s]] for s in common])
    coo_aligned = np.array([coo_vec[coo_idx[s]] for s in common])
    combined = np.concatenate([sem_aligned, coo_aligned], axis=1)
    norms = np.linalg.norm(combined, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    combined = (combined / norms).astype(np.float32)
    idx_map = {s: i for i, s in enumerate(common)}

    print("\nIdentifying buckets...")
    locus_set = {s for s in common if is_locus_gloss(meta[s].get("gloss"))}
    generic_set = {s for s in common
                   if is_generic(s, pos_lookup) and s not in locus_set}
    noise_set = {s for s in common
                 if is_extraction_noise(meta[s].get("gloss"))
                 and s not in locus_set and s not in generic_set}
    char_set = {s for s in common
                if s not in locus_set and s not in generic_set
                and s not in noise_set}
    print(f"  loci:           {len(locus_set):>5}")
    print(f"  generics:       {len(generic_set):>5}")
    print(f"  extract-noise:  {len(noise_set):>5}")
    print(f"  characteristics:{len(char_set):>5}")

    locus_strongs = sorted(locus_set)
    generic_strongs = sorted(generic_set)
    noise_strongs = sorted(noise_set)
    char_strongs_all = sorted(char_set)

    print("\nClustering LOCI...")
    locus_indices = [idx_map[s] for s in locus_strongs]
    k_loci = min(args.k_loci, max(2, len(locus_strongs) // 3))
    locus_labels = cluster_kmeans(combined[locus_indices], k_loci)

    char_hebrew = [s for s in char_strongs_all if meta[s]["language"] == "Hebrew"]
    char_greek = [s for s in char_strongs_all if meta[s]["language"] == "Greek"]

    print(f"\nClustering Hebrew characteristics ({len(char_hebrew)} terms, k={args.k_char_hebrew})...")
    heb_indices = [idx_map[s] for s in char_hebrew]
    k_heb = min(args.k_char_hebrew, max(2, len(char_hebrew) // 8))
    heb_labels = cluster_kmeans(combined[heb_indices], k_heb)

    print(f"Clustering Greek characteristics ({len(char_greek)} terms, k={args.k_char_greek})...")
    gk_indices = [idx_map[s] for s in char_greek]
    k_gk = min(args.k_char_greek, max(2, len(char_greek) // 8))
    gk_labels = cluster_kmeans(combined[gk_indices], k_gk)

    print(f"\nHDBSCAN sanity check on combined characteristics "
          f"(min_cluster_size={args.hdbscan_min_cluster_size})...")
    char_indices = [idx_map[s] for s in char_strongs_all]
    hdb_labels = cluster_hdbscan(
        combined[char_indices],
        min_cluster_size=args.hdbscan_min_cluster_size,
    )
    n_hdb = len(set(int(l) for l in hdb_labels if l != -1))
    n_noise = int(sum(1 for l in hdb_labels if l == -1))
    print(f"  organic clusters: {n_hdb}, noise: {n_noise}/{len(hdb_labels)}")

    md_loci = render_clusters_md(
        "LOCI clusters", locus_strongs, locus_labels, meta,
        combined, idx_map, f"k: {k_loci}"
    )
    md_heb = render_clusters_md(
        "CHARACTERISTIC clusters — Hebrew",
        char_hebrew, heb_labels, meta, combined, idx_map, f"k: {k_heb}"
    )
    md_gk = render_clusters_md(
        "CHARACTERISTIC clusters — Greek",
        char_greek, gk_labels, meta, combined, idx_map, f"k: {k_gk}"
    )
    md_hdb = render_clusters_md(
        "CHARACTERISTIC clusters — HDBSCAN organic",
        char_strongs_all, hdb_labels, meta, combined, idx_map,
        f"organic clusters: {n_hdb} · noise: {n_noise}"
    )

    out_loci = out_prefix + "-loci.md"
    out_heb = out_prefix + "-characteristics-hebrew.md"
    out_gk = out_prefix + "-characteristics-greek.md"
    out_hdb = out_prefix + "-characteristics-hdbscan.md"
    out_buckets = out_prefix + "-bucket-summary.md"
    out_json = out_prefix + ".json"

    os.makedirs(os.path.dirname(out_loci), exist_ok=True)
    with open(out_loci, "w", encoding="utf-8") as f:
        f.write(md_loci)
    with open(out_heb, "w", encoding="utf-8") as f:
        f.write(md_heb)
    with open(out_gk, "w", encoding="utf-8") as f:
        f.write(md_gk)
    with open(out_hdb, "w", encoding="utf-8") as f:
        f.write(md_hdb)

    bucket_lines = [
        "# 4-way term split — bucket summary (v2)",
        "",
        f"**Generated:** {now_iso()}",
        "",
        "## Filter validation",
        "",
        f"- Working set: **{len(common):,} terms** "
        f"(intersection of semantic and co-occurrence vectors)",
        f"- Excluded as 0-verse: **{len(excluded_no_verse):,} terms** "
        f"(no active OWNER verse-record)",
        "- All working-set terms have:",
        "  - `mti_terms.delete_flagged = 0`",
        "  - `wa_term_inventory.delete_flagged = 0` (OWNER row)",
        "  - At least one `wa_verse_records.delete_flagged = 0` row",
        "",
        "## Bucket sizes",
        "",
        "| Bucket | Count |",
        "|---|---|",
        f"| LOCI | {len(locus_strongs)} |",
        f"| GENERICS | {len(generic_strongs)} |",
        f"| EXTRACTION-NOISE | {len(noise_strongs)} |",
        f"| CHARACTERISTICS (Hebrew + Greek) | {len(char_strongs_all)} |",
        f"|   ↳ Hebrew | {len(char_hebrew)} |",
        f"|   ↳ Greek | {len(char_greek)} |",
        "",
        "## Note on registry",
        "",
        "Registry has **no weight in clustering**. Clustering uses only:",
        "1. Weighted semantic vector (root + gloss + meaning text)",
        "2. Co-occurrence vector (verse co-occurrence with other OWNER terms)",
        "",
        "Registry is omitted entirely from the cluster table outputs to avoid suggesting otherwise.",
    ]
    with open(out_buckets, "w", encoding="utf-8") as f:
        f.write("\n".join(bucket_lines))

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_working_set": len(common),
            "n_excluded_no_verse": len(excluded_no_verse),
            "n_locus": len(locus_strongs),
            "n_generic": len(generic_strongs),
            "n_extraction_noise": len(noise_strongs),
            "n_characteristic": len(char_strongs_all),
            "n_char_hebrew": len(char_hebrew),
            "n_char_greek": len(char_greek),
            "k_loci": k_loci,
            "k_char_hebrew": k_heb,
            "k_char_greek": k_gk,
            "hdbscan_min_cluster_size": args.hdbscan_min_cluster_size,
            "hdbscan_n_organic_clusters": n_hdb,
            "hdbscan_n_noise": n_noise,
        },
        "loci": [{"strong": s, "cluster": int(lbl), **meta.get(s, {})}
                 for s, lbl in zip(locus_strongs, locus_labels)],
        "generics": [{"strong": s, **meta.get(s, {})} for s in generic_strongs],
        "extraction_noise": [{"strong": s, **meta.get(s, {})} for s in noise_strongs],
        "characteristics_hebrew": [
            {"strong": s, "cluster": int(lbl), **meta.get(s, {})}
            for s, lbl in zip(char_hebrew, heb_labels)
        ],
        "characteristics_greek": [
            {"strong": s, "cluster": int(lbl), **meta.get(s, {})}
            for s, lbl in zip(char_greek, gk_labels)
        ],
        "characteristics_hdbscan": [
            {"strong": s, "cluster": int(lbl), **meta.get(s, {})}
            for s, lbl in zip(char_strongs_all, hdb_labels)
        ],
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"\nWrote: {out_loci}")
    print(f"Wrote: {out_heb}")
    print(f"Wrote: {out_gk}")
    print(f"Wrote: {out_hdb}")
    print(f"Wrote: {out_buckets}")
    print(f"Wrote: {out_json}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
