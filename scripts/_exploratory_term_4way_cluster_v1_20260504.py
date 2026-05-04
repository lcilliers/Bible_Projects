"""_exploratory_term_4way_cluster_v1_20260504.py — read-only.

Four-way term split + per-language characteristic clustering + HDBSCAN
sanity check.

Buckets:
  LOCI           — seat / inner-being location nouns (heart, soul, …)
  GENERICS       — pronouns, particles, generic verbs (function words)
  EXTRACTION-NOISE — physical objects, animals, materials, vessels — terms
                    that ended up OWNER'd to inner-being registries but have
                    no inner-being content
  CHARACTERISTICS — the actual inner-being analytical pool

Characteristics are then clustered:
  - Hebrew-only k-means
  - Greek-only k-means
  - Combined HDBSCAN sanity check (organic, density-based)

No registry yardstick anywhere. Registry is shown as label only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
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
# Physical objects, animals, raw materials, vessels, weapons, garments,
# writing materials, body-parts-not-loci. Match if gloss is exactly the
# noun, or "<noun>: <sense>" variant.
EXTRACTION_NOISE_NOUNS = {
    # Weapons / armour
    "weapon", "sword", "knife", "dagger", "spear", "javelin", "bow",
    "arrow", "sling", "staff", "rod", "club",
    "helmet", "shield", "armor", "armour", "breastplate", "scabbard",
    # Vessels / utensils
    "vessel", "jar", "jug", "pot", "cup", "basin", "bowl", "lamp",
    "dish", "pitcher", "censer", "bucket",
    # Furniture / fixtures
    "throne", "chair", "seat", "bed", "couch", "table", "footstool",
    "altar",  # debatable — but mostly physical
    # Clothing / fabric
    "garment", "robe", "tunic", "mantle", "cloak", "sandal", "shoe",
    "belt", "sash", "veil", "cloth", "fabric", "linen", "wool",
    # Writing / sealing
    "ink", "paper", "papyrus", "scroll", "parchment", "tablet",
    "seal", "signet",
    # Animals
    "ass", "donkey", "ox", "bull", "cow", "sheep", "goat", "lamb",
    "ram", "horse", "camel", "dog", "lion", "wolf", "bear", "fox",
    "eagle", "raven", "dove", "swallow", "fish", "serpent",
    "she-ass", "young-ass", "kid", "ewe", "buck",
    # Materials / metals
    "iron", "bronze", "copper", "gold", "silver", "tin", "lead",
    "brass", "steel",
    # Writing / books
    "book", "letter", "scroll", "decree",
    # Body parts (non-locus, anatomical-only)
    "loin", "thigh", "shoulder", "neck", "arm", "leg", "back", "chest",
    "skull", "skin", "tooth", "lip", "nail", "hair", "beard",
    # Other physical
    "knife", "yoke", "cord", "rope", "chain", "fetter",
    # Plant / agricultural
    "wheat", "barley", "grain", "olive", "fig", "vine", "branch",
    # Food / drink (when name only)
    "honey", "milk", "wine", "bread", "meat",
    # Coinage / measures
    "shekel", "ephah", "cubit", "talent",
}
EXTRACTION_NOISE_RE = re.compile(
    r"^(" + "|".join(re.escape(n) for n in EXTRACTION_NOISE_NOUNS) + r")(\s*:\s*\w+.*)?$",
    re.IGNORECASE,
)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def is_locus_gloss(gloss):
    if not gloss:
        return False
    return bool(LOCUS_GLOSS_RE.match(gloss.strip().lower()))


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


def is_extraction_noise(gloss):
    if not gloss:
        return False
    return bool(EXTRACTION_NOISE_RE.match(gloss.strip().lower()))


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
        clusterer = hdbscan.HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
            metric="euclidean",
        )
        return clusterer.fit_predict(vectors)
    except ImportError:
        # fall back to sklearn HDBSCAN if available
        from sklearn.cluster import HDBSCAN
        return HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=min_samples,
        ).fit_predict(vectors)


def render_clusters_md(title, strongs, labels, meta, k_label):
    by_cluster = defaultdict(list)
    for s, lbl in zip(strongs, labels):
        by_cluster[int(lbl)].append(str(s))
    lines = [f"# {title}", "",
             f"**Generated:** {now_iso()}",
             f"**Terms clustered:** {len(strongs)}",
             f"**{k_label}**", "",
             "Registry shown as label only; clustering ignores it.",
             ""]
    # Sort clusters: noise (-1) last, others by size desc
    cluster_order = sorted(
        by_cluster.keys(),
        key=lambda c: (c == -1, -len(by_cluster[c]))
    )
    for lbl in cluster_order:
        members = by_cluster[lbl]
        title_extra = " (HDBSCAN noise)" if lbl == -1 else ""
        lines.append(f"## Cluster {lbl}{title_extra} — {len(members)} term(s)")
        lines.append("")
        lines.append("| Strong's | translit | gloss | language | registry (label) |")
        lines.append("|---|---|---|---|---|")
        members_sorted = sorted(
            members,
            key=lambda s: (meta.get(s, {}).get("transliteration") or "").lower()
        )
        for s in members_sorted:
            m = meta.get(s, {})
            lines.append(
                f"| {s} | {m.get('transliteration') or ''} | "
                f"{(m.get('gloss') or '')[:60]} | "
                f"{m.get('language') or ''} | "
                f"{m.get('registry') or ''} |"
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
        "outputs", "markdown", f"term-clusters-4way-{today_compact()}"
    )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Loading metadata + POS...")
    meta = load_strongs_metadata(conn)
    pos_lookup = load_pos_lookup()

    print("Identifying buckets...")
    locus_set = {s for s, m in meta.items() if is_locus_gloss(m["gloss"])}
    generic_set = {s for s in meta
                    if is_generic(s, pos_lookup) and s not in locus_set}
    noise_set = {s for s, m in meta.items()
                 if is_extraction_noise(m["gloss"])
                 and s not in locus_set and s not in generic_set}
    char_set = {s for s in meta
                if s not in locus_set and s not in generic_set
                and s not in noise_set}
    print(f"  loci:           {len(locus_set):>5}")
    print(f"  generics:       {len(generic_set):>5}")
    print(f"  extract-noise:  {len(noise_set):>5}")
    print(f"  characteristics:{len(char_set):>5}")

    print("Loading vectors...")
    sem_strongs, sem_vec = load_npz(args.semantic)
    coo_strongs, coo_vec = load_npz(args.cooccurrence)
    sem_idx = {str(s): i for i, s in enumerate(sem_strongs)}
    coo_idx = {str(s): i for i, s in enumerate(coo_strongs)}
    common = sorted(set(sem_idx) & set(coo_idx))
    print(f"  aligned: {len(common)} terms")

    sem_aligned = np.array([sem_vec[sem_idx[s]] for s in common])
    coo_aligned = np.array([coo_vec[coo_idx[s]] for s in common])
    combined = np.concatenate([sem_aligned, coo_aligned], axis=1)
    norms = np.linalg.norm(combined, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    combined = (combined / norms).astype(np.float32)

    common_set = set(common)
    locus_idxs = [i for i, s in enumerate(common) if s in locus_set & common_set]
    char_indices_all = [i for i, s in enumerate(common)
                        if s in char_set & common_set]
    char_strongs_all = [common[i] for i in char_indices_all]
    char_languages = [meta[s]["language"] for s in char_strongs_all]

    locus_strongs = [common[i] for i in locus_idxs]
    generic_strongs = sorted(generic_set & common_set)
    noise_strongs = sorted(noise_set & common_set)

    # 1. Cluster LOCI alone
    print("\nClustering LOCI...")
    k_loci = min(args.k_loci, max(2, len(locus_strongs) // 3))
    locus_labels = cluster_kmeans(combined[locus_idxs], k_loci)

    # 2. Cluster CHARACTERISTICS by language separately
    char_hebrew_idxs = [i for i, s in zip(char_indices_all, char_strongs_all)
                       if meta[s]["language"] == "Hebrew"]
    char_greek_idxs = [i for i, s in zip(char_indices_all, char_strongs_all)
                      if meta[s]["language"] == "Greek"]
    char_hebrew_strongs = [common[i] for i in char_hebrew_idxs]
    char_greek_strongs = [common[i] for i in char_greek_idxs]
    print(f"  Hebrew characteristics: {len(char_hebrew_strongs)}")
    print(f"  Greek characteristics:  {len(char_greek_strongs)}")

    print(f"\nClustering Hebrew characteristics (k={args.k_char_hebrew})...")
    k_heb = min(args.k_char_hebrew, max(2, len(char_hebrew_strongs) // 8))
    heb_labels = cluster_kmeans(combined[char_hebrew_idxs], k_heb)

    print(f"Clustering Greek characteristics (k={args.k_char_greek})...")
    k_gk = min(args.k_char_greek, max(2, len(char_greek_strongs) // 8))
    gk_labels = cluster_kmeans(combined[char_greek_idxs], k_gk)

    # 3. HDBSCAN sanity check on combined characteristics
    print(f"\nHDBSCAN on combined characteristics "
          f"(min_cluster_size={args.hdbscan_min_cluster_size})...")
    hdb_labels = cluster_hdbscan(
        combined[char_indices_all],
        min_cluster_size=args.hdbscan_min_cluster_size,
    )
    n_hdb_clusters = len(set(int(l) for l in hdb_labels if l != -1))
    n_hdb_noise = int(sum(1 for l in hdb_labels if l == -1))
    print(f"  organic clusters: {n_hdb_clusters}")
    print(f"  HDBSCAN noise points: {n_hdb_noise}/{len(hdb_labels)}")

    # Render outputs
    md_loci = render_clusters_md(
        "LOCI clusters (seat / inner-being location terms)",
        locus_strongs, locus_labels, meta, f"k: {k_loci}"
    )
    md_heb = render_clusters_md(
        "CHARACTERISTIC clusters — Hebrew",
        char_hebrew_strongs, heb_labels, meta, f"k: {k_heb}"
    )
    md_gk = render_clusters_md(
        "CHARACTERISTIC clusters — Greek",
        char_greek_strongs, gk_labels, meta, f"k: {k_gk}"
    )
    md_hdb = render_clusters_md(
        "CHARACTERISTIC clusters — HDBSCAN organic (Hebrew + Greek combined)",
        char_strongs_all, hdb_labels, meta,
        f"organic clusters: {n_hdb_clusters} · noise: {n_hdb_noise}"
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

    # Buckets summary
    bucket_lines = [
        "# 4-way term split — bucket summary",
        "",
        f"**Generated:** {now_iso()}",
        "",
        "| Bucket | Count | What's in it |",
        "|---|---|---|",
        f"| LOCI | {len(locus_strongs)} | Seat/inner-being location nouns |",
        f"| GENERICS | {len(generic_strongs)} | Function words, particles, generic verbs |",
        f"| EXTRACTION-NOISE | {len(noise_strongs)} | Physical objects mistakenly OWNER'd |",
        f"| CHARACTERISTICS | {len(char_strongs_all)} | Inner-being analytical pool (Heb {len(char_hebrew_strongs)} / Grk {len(char_greek_strongs)}) |",
        "",
        "## EXTRACTION-NOISE candidates",
        "",
        "These are terms whose gloss matches a physical-object pattern. "
        "Inspect — if some are actually inner-being relevant in metaphor, the "
        "filter should be loosened.",
        "",
        "| Strong's | translit | gloss | language | registry (label) |",
        "|---|---|---|---|---|",
    ]
    for s in noise_strongs:
        m = meta.get(s, {})
        bucket_lines.append(
            f"| {s} | {m.get('transliteration') or ''} | "
            f"{(m.get('gloss') or '')[:50]} | "
            f"{m.get('language') or ''} | "
            f"{m.get('registry') or ''} |"
        )
    bucket_lines.append("")
    bucket_lines.append("## GENERICS")
    bucket_lines.append("")
    bucket_lines.append("| Strong's | translit | gloss | language |")
    bucket_lines.append("|---|---|---|---|")
    for s in generic_strongs:
        m = meta.get(s, {})
        bucket_lines.append(
            f"| {s} | {m.get('transliteration') or ''} | "
            f"{(m.get('gloss') or '')[:50]} | "
            f"{m.get('language') or ''} |"
        )

    with open(out_buckets, "w", encoding="utf-8") as f:
        f.write("\n".join(bucket_lines))

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_locus": len(locus_strongs),
            "n_generic": len(generic_strongs),
            "n_extraction_noise": len(noise_strongs),
            "n_characteristic": len(char_strongs_all),
            "n_char_hebrew": len(char_hebrew_strongs),
            "n_char_greek": len(char_greek_strongs),
            "k_loci": k_loci,
            "k_char_hebrew": k_heb,
            "k_char_greek": k_gk,
            "hdbscan_min_cluster_size": args.hdbscan_min_cluster_size,
            "hdbscan_n_organic_clusters": n_hdb_clusters,
            "hdbscan_n_noise": n_hdb_noise,
        },
        "loci": [{"strong": s, "cluster": int(lbl), **meta.get(s, {})}
                 for s, lbl in zip(locus_strongs, locus_labels)],
        "generics": [{"strong": s, **meta.get(s, {})} for s in generic_strongs],
        "extraction_noise": [{"strong": s, **meta.get(s, {})} for s in noise_strongs],
        "characteristics_hebrew": [
            {"strong": s, "cluster": int(lbl), **meta.get(s, {})}
            for s, lbl in zip(char_hebrew_strongs, heb_labels)
        ],
        "characteristics_greek": [
            {"strong": s, "cluster": int(lbl), **meta.get(s, {})}
            for s, lbl in zip(char_greek_strongs, gk_labels)
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
