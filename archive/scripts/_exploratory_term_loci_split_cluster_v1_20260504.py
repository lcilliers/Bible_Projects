"""_exploratory_term_loci_split_cluster_v1_20260504.py — read-only.

Two clustering passes with LOCI / CHARACTERISTIC split, no registry yardstick.

Locus identification: Strong's whose gloss IS a canonical inner-being seat
noun (heart, soul, spirit, mind, body, flesh, conscience, inner parts,
kidney, bone) — including sense-disambiguated variants like 'soul: life',
'spirit: breath'. Compound adjectives/verbs ('hard-hearted', 'remember',
'self-controlled') are excluded.

Pipeline:
  1. Identify locus Strong's via tight gloss filter.
  2. Cluster the LOCI pool on its own (small, ~30-50 terms).
  3. Cluster the CHARACTERISTICS pool on its own (~2400 terms).
  4. Output cluster contents (Strong's + transliteration + gloss) — no
     registry alignment metric. Registry shown only as a label.

Output:
  outputs/markdown/term-clusters-loci-{date}.md
  outputs/markdown/term-clusters-characteristics-{date}.md
  outputs/markdown/term-clusters-loci-split-{date}.json
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

# Canonical seat-noun glosses. Match if gloss is exactly one of these,
# or "<noun>: <sense>", but not compound words containing them.
LOCUS_NOUNS = {
    "heart", "soul", "spirit", "mind", "body", "flesh",
    "conscience", "inner parts", "kidney", "bone", "being",
    "self", "person", "life", "breath",
}

LOCUS_GLOSS_RE = re.compile(
    r"^(" + "|".join(re.escape(n) for n in LOCUS_NOUNS) + r")(\s*:\s*\w+.*)?$",
    re.IGNORECASE,
)

# POS classes that indicate GENERIC / function / grammatical-glue terms.
# These cross-cut all characteristics like loci do, but for grammatical
# rather than ontological reasons.
GENERIC_POS = {
    "pronoun", "pronoun-personal", "particle", "preposition",
    "conjunction", "conditional-particle", "article",
    "interjection",
}

# Hand-curated generic content-POS Strong's (high-frequency generic
# verbs/nouns whose meaning is grammatical-functional rather than
# inner-being-content).
GENERIC_CONTENT_STRONGS = {
    "H1961",        # hayah — to be
    "H6213A",       # asah — to do/make
    "H0935G",       # bo — to come
    "H1980G",       # halakh — to go
    "H5414G",       # natan — to give
    "H0120G",       # adam — man (generic)
    "H5971L",       # am — people (generic)
    "G1510",        # eimi — to be
    "G1096",        # ginomai — to be/become
    "G2192",        # echo — to have
    "G4160",        # poieo — to do/make
    "G2064",        # erchomai — to come
    "G1325",        # didomi — to give
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def is_locus_gloss(gloss):
    if not gloss:
        return False
    g = gloss.strip().lower()
    return bool(LOCUS_GLOSS_RE.match(g))


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
    if pos and pos in GENERIC_POS:
        return True
    return False


def load_strongs_metadata(conn):
    """Returns {strong: {transliteration, gloss, language, registry}}."""
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


def render_clusters_md(title, strong_to_idx, strongs, labels, meta, k):
    by_cluster = defaultdict(list)
    for s, lbl in zip(strongs, labels):
        by_cluster[int(lbl)].append(str(s))

    lines = [f"# {title}", "",
             f"**Generated:** {now_iso()}",
             f"**Terms clustered:** {len(strongs)}",
             f"**k:** {k}",
             "",
             "Registry is shown as label only; clustering ignores it.",
             ""]
    for lbl in sorted(by_cluster.keys()):
        members = by_cluster[lbl]
        lines.append(f"## Cluster {lbl} — {len(members)} term(s)")
        lines.append("")
        lines.append("| Strong's | translit | gloss | language | registry (label) |")
        lines.append("|---|---|---|---|---|")
        # sort by transliteration for readability
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--semantic", required=True,
                    help="weighted semantic vector .npz")
    ap.add_argument("--cooccurrence", required=True,
                    help="co-occurrence vector .npz")
    ap.add_argument("--k-loci", type=int, default=10)
    ap.add_argument("--k-char", type=int, default=120)
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown", f"term-clusters-loci-split-{today_compact()}"
    )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Loading metadata...")
    meta = load_strongs_metadata(conn)
    print(f"  {len(meta)} terms in metadata")

    print("Loading POS lookup...")
    pos_lookup = load_pos_lookup()
    print(f"  POS entries: {len(pos_lookup)}")

    print("Identifying locus terms...")
    locus_set = {s for s, m in meta.items() if is_locus_gloss(m["gloss"])}
    print(f"  {len(locus_set)} locus terms by tight gloss filter")
    print(f"  examples: " + ", ".join(
        f"{s}={meta[s]['gloss']}" for s in sorted(locus_set)[:8]
    ))

    print("Identifying generic / function terms...")
    generic_set = {s for s in meta if is_generic(s, pos_lookup)
                    and s not in locus_set}
    print(f"  {len(generic_set)} generic terms (POS function or hand-curated)")
    sample = sorted(generic_set)[:10]
    print(f"  examples: " + ", ".join(
        f"{s}={meta[s]['gloss']!r}" for s in sample
    ))

    print("Loading vectors...")
    sem_strongs, sem_vec = load_npz(args.semantic)
    coo_strongs, coo_vec = load_npz(args.cooccurrence)

    coo_idx = {str(s): i for i, s in enumerate(coo_strongs)}
    sem_idx = {str(s): i for i, s in enumerate(sem_strongs)}
    common = sorted(set(sem_idx) & set(coo_idx))
    print(f"  aligned: {len(common)} terms (intersection)")

    # Build combined vectors (weighted sem || co-occ), L2-normalised
    sem_aligned = np.array([sem_vec[sem_idx[s]] for s in common])
    coo_aligned = np.array([coo_vec[coo_idx[s]] for s in common])
    combined = np.concatenate([sem_aligned, coo_aligned], axis=1)
    norms = np.linalg.norm(combined, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    combined = (combined / norms).astype(np.float32)

    locus_idxs = [i for i, s in enumerate(common) if s in locus_set]
    generic_idxs = [i for i, s in enumerate(common)
                    if s in generic_set and s not in locus_set]
    char_idxs = [i for i, s in enumerate(common)
                 if s not in locus_set and s not in generic_set]

    print(f"  loci aligned: {len(locus_idxs)}")
    print(f"  generics aligned: {len(generic_idxs)}")
    print(f"  characteristics aligned: {len(char_idxs)}")

    locus_strongs = [common[i] for i in locus_idxs]
    generic_strongs = [common[i] for i in generic_idxs]
    char_strongs = [common[i] for i in char_idxs]

    # Cluster loci alone
    k_loci = min(args.k_loci, max(2, len(locus_strongs) // 3))
    print(f"\nClustering LOCI (k={k_loci})...")
    locus_labels = cluster_kmeans(combined[locus_idxs], k_loci)

    # Cluster characteristics alone
    k_char = min(args.k_char, max(2, len(char_strongs) // 8))
    print(f"Clustering CHARACTERISTICS (k={k_char})...")
    char_labels = cluster_kmeans(combined[char_idxs], k_char)

    # Render markdown
    out_md_loci = out_prefix + "-loci.md"
    out_md_char = out_prefix + "-characteristics.md"
    out_json = out_prefix + ".json"

    md_loci = render_clusters_md(
        "LOCI cluster (seat / inner-being location terms)",
        sem_idx, locus_strongs, locus_labels, meta, k_loci
    )
    md_char = render_clusters_md(
        "CHARACTERISTIC clusters (inner-being qualities, dispositions, acts)",
        sem_idx, char_strongs, char_labels, meta, k_char
    )

    os.makedirs(os.path.dirname(out_md_loci), exist_ok=True)
    with open(out_md_loci, "w", encoding="utf-8") as f:
        f.write(md_loci)
    with open(out_md_char, "w", encoding="utf-8") as f:
        f.write(md_char)

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "semantic_input": args.semantic,
            "cooccurrence_input": args.cooccurrence,
            "n_locus_terms": len(locus_strongs),
            "n_generic_terms": len(generic_strongs),
            "n_characteristic_terms": len(char_strongs),
            "k_loci": k_loci,
            "k_char": k_char,
            "locus_filter": "gloss equal to canonical seat noun, or '<noun>: <sense>' variant",
            "locus_nouns": sorted(LOCUS_NOUNS),
            "generic_pos_classes": sorted(GENERIC_POS),
            "generic_content_strongs": sorted(GENERIC_CONTENT_STRONGS),
        },
        "loci": [
            {"strong": s, "cluster": int(lbl), **meta.get(s, {})}
            for s, lbl in zip(locus_strongs, locus_labels)
        ],
        "generics": [
            {"strong": s, **meta.get(s, {})}
            for s in generic_strongs
        ],
        "characteristics": [
            {"strong": s, "cluster": int(lbl), **meta.get(s, {})}
            for s, lbl in zip(char_strongs, char_labels)
        ],
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"\nWrote: {out_md_loci}")
    print(f"Wrote: {out_md_char}")
    print(f"Wrote: {out_json}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
