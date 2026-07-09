"""_exploratory_term_5way_cluster_v2_20260504.py — read-only.

V4 (5-way bucket split + verse profile per term).

Adds per-term verse profile to all outputs:
  - verse_count       — total OWNER-active verses the term appears in
  - multi_term_count  — verses that also contain another OWNER term
  - multi_term_pct    — multi_term_count / verse_count

Output JSON entries gain three fields. Markdown tables gain two columns
(verses | multi%).

Pipeline otherwise identical to v3 (5-way bucket split + qualifier post-hoc
attachment via co-occurrence affinity).
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
    "throne", "chair", "seat", "bed", "couch", "table", "footstool", "altar",
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
    "vegetable", "tassel", "juice", "oak", "tree", "plant", "flower", "thorn",
    "field", "garden", "harvest", "seed", "grain", "fruit",
}
EXTRACTION_NOISE_RE = re.compile(
    r"^(" + "|".join(re.escape(n) for n in EXTRACTION_NOISE_NOUNS) + r")(\s*:\s*\w+.*)?$",
    re.IGNORECASE,
)

# --- QUALIFIERS -------------------------------------------------------
QUALIFIER_POS = {"adverb"}
QUALIFIER_GLOSS_PREFIXES = (
    "very ", "very-", "much ", "more ", "less ", "most ", "least ",
    "great ", "small ", "abundant", "exceedingly", "altogether",
    "wholly ", "completely", "all ", "many ", "few ",
    "all-", "every ", "exceeding",
)
QUALIFIER_GLOSS_EXACT = {
    "very", "much", "more", "less", "most", "least", "abundant",
    "abundantly", "exceedingly", "altogether", "wholly", "completely",
    "all", "many", "few", "every", "great", "small", "large",
    "perhaps", "barely", "rarely",
    "above", "below", "beneath", "before", "after",
    "indeed", "surely", "truly",
    "again", "always", "never",
    "behold", "look", "see-here",
    "thus", "so",
    "kind", "type", "sort", "manner",
}

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


def is_qualifier(strong, gloss, pos_lookup):
    pos = pos_lookup.get(strong)
    if pos and pos in QUALIFIER_POS:
        return True
    if not gloss:
        return False
    g = gloss.strip().lower().split(":")[0].strip()
    if g in QUALIFIER_GLOSS_EXACT:
        return True
    for prefix in QUALIFIER_GLOSS_PREFIXES:
        if g.startswith(prefix):
            return True
    return False


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


def build_verse_profile(verse_terms_map):
    """Returns {strong: {verse_count, multi_term_count, multi_term_pct}}."""
    counter = Counter()
    multi = Counter()
    for terms in verse_terms_map.values():
        is_multi = len(terms) > 1
        for s in terms:
            counter[s] += 1
            if is_multi:
                multi[s] += 1
    out = {}
    for s, n in counter.items():
        m = multi[s]
        out[s] = {
            "verse_count": n,
            "multi_term_count": m,
            "multi_term_pct": round(100.0 * m / n, 1) if n else 0.0,
        }
    return out


def load_npz(path):
    arr = np.load(path, allow_pickle=False)
    return arr["strongs"], arr["vectors"]


def cluster_kmeans(vectors, k, seed=20260504):
    from sklearn.cluster import KMeans
    return KMeans(n_clusters=k, random_state=seed, n_init=10).fit_predict(vectors)


# ---------------- THEME SUMMARY ---------------------------------------
TOKEN_RE = re.compile(r"[a-z]+")


def gloss_tokens(gloss):
    if not gloss:
        return []
    g = gloss.lower().split(":")[0]
    return [t for t in TOKEN_RE.findall(g)
            if t not in THEME_STOPWORDS and len(t) > 2]


def cluster_theme(strongs, meta):
    counter = Counter()
    for s in strongs:
        for t in gloss_tokens((meta.get(s) or {}).get("gloss") or ""):
            counter[t] += 1
    return counter.most_common(12)


def cluster_centroid_term(strongs, vectors, idx_map):
    indices = [idx_map[s] for s in strongs if s in idx_map]
    if not indices:
        return None
    v = vectors[indices]
    centroid = v.mean(axis=0)
    centroid /= max(1e-12, np.linalg.norm(centroid))
    sims = v @ centroid
    return strongs[int(np.argmax(sims))]


def render_clusters_md(title, strongs, labels, meta, vectors, idx_map,
                        k_label, profile, qualifier_attach=None):
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
        title_extra = " (HDBSCAN noise)" if lbl == -1 else ""
        theme_words = cluster_theme(members, meta)
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

        if qualifier_attach and lbl in qualifier_attach:
            attached = qualifier_attach[lbl]
            if attached:
                lines.append("**Attached qualifiers (top by co-occurrence affinity):**")
                lines.append("")
                lines.append("| Strong's | translit | gloss | verses | multi% | affinity |")
                lines.append("|---|---|---|---|---|---|")
                for q in attached:
                    m = meta.get(q["strong"], {})
                    p = profile.get(q["strong"], {})
                    lines.append(
                        f"| {q['strong']} | {m.get('transliteration') or ''} | "
                        f"{(m.get('gloss') or '')[:40]} | "
                        f"{p.get('verse_count', '')} | "
                        f"{p.get('multi_term_pct', '')}% | "
                        f"{q['affinity']:.3f} |"
                    )
                lines.append("")

        lines.append("| Strong's | translit | gloss | language | verses | multi% |")
        lines.append("|---|---|---|---|---|---|")
        members_sorted = sorted(
            members,
            key=lambda s: ((meta.get(s) or {}).get("transliteration") or "").lower()
        )
        for s in members_sorted:
            m = meta.get(s, {})
            p = profile.get(s, {})
            lines.append(
                f"| {s} | {m.get('transliteration') or ''} | "
                f"{(m.get('gloss') or '')[:60]} | "
                f"{m.get('language') or ''} | "
                f"{p.get('verse_count', '')} | "
                f"{p.get('multi_term_pct', '')}% |"
            )
        lines.append("")
    return "\n".join(lines)


def attach_qualifiers_to_clusters(qualifier_strongs, char_strongs, char_labels,
                                    verse_terms_map, top_n=3):
    char_to_cluster = dict(zip(char_strongs, char_labels))
    qual_cluster_count = {q: defaultdict(int) for q in qualifier_strongs}
    qual_total = Counter()
    for ref, terms in verse_terms_map.items():
        present_quals = terms & set(qualifier_strongs)
        for q in present_quals:
            qual_total[q] += 1
            cluster_membership = set()
            for t in terms - {q}:
                if t in char_to_cluster:
                    cluster_membership.add(int(char_to_cluster[t]))
            for c in cluster_membership:
                qual_cluster_count[q][c] += 1
    qual_top = {}
    for q in qualifier_strongs:
        if qual_total[q] == 0:
            qual_top[q] = []
            continue
        scored = [(c, n, n / qual_total[q]) for c, n in qual_cluster_count[q].items()]
        scored.sort(key=lambda x: -x[2])
        qual_top[q] = [{"cluster": c, "count": n, "affinity": a}
                       for c, n, a in scored[:top_n]]
    cluster_to_quals = defaultdict(list)
    for q, tops in qual_top.items():
        for entry in tops:
            cluster_to_quals[entry["cluster"]].append({
                "strong": q,
                "affinity": entry["affinity"],
                "count": entry["count"],
            })
    for c in cluster_to_quals:
        cluster_to_quals[c].sort(key=lambda x: -x["affinity"])
        cluster_to_quals[c] = cluster_to_quals[c][:8]
    return dict(cluster_to_quals), qual_top


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--semantic", required=True)
    ap.add_argument("--cooccurrence", required=True)
    ap.add_argument("--k-loci", type=int, default=10)
    ap.add_argument("--k-char-hebrew", type=int, default=80)
    ap.add_argument("--k-char-greek", type=int, default=40)
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown", f"term-clusters-5way-v2-{today_compact()}"
    )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Loading metadata + POS...")
    meta = load_strongs_metadata(conn)
    pos_lookup = load_pos_lookup()

    print("Building verse profile (per-term verse counts)...")
    verse_terms_map = fetch_verse_to_terms(conn)
    profile = build_verse_profile(verse_terms_map)
    print(f"  {len(profile):,} terms have at least one verse")

    print("Loading vectors (intersection working set)...")
    sem_strongs, sem_vec = load_npz(args.semantic)
    coo_strongs, coo_vec = load_npz(args.cooccurrence)
    sem_idx = {str(s): i for i, s in enumerate(sem_strongs)}
    coo_idx = {str(s): i for i, s in enumerate(coo_strongs)}
    common = sorted(set(sem_idx) & set(coo_idx))
    print(f"  working set: {len(common):,} terms")

    sem_aligned = np.array([sem_vec[sem_idx[s]] for s in common])
    coo_aligned = np.array([coo_vec[coo_idx[s]] for s in common])
    combined = np.concatenate([sem_aligned, coo_aligned], axis=1)
    norms = np.linalg.norm(combined, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    combined = (combined / norms).astype(np.float32)
    idx_map = {s: i for i, s in enumerate(common)}

    print("\nIdentifying buckets...")
    locus_set, generic_set, noise_set, qualifier_set, char_set = set(), set(), set(), set(), set()
    for s in common:
        m = meta.get(s, {})
        g = m.get("gloss")
        if is_locus_gloss(g):
            locus_set.add(s)
        elif is_generic(s, pos_lookup):
            generic_set.add(s)
        elif is_extraction_noise(g):
            noise_set.add(s)
        elif is_qualifier(s, g, pos_lookup):
            qualifier_set.add(s)
        else:
            char_set.add(s)
    print(f"  loci:           {len(locus_set):>5}")
    print(f"  generics:       {len(generic_set):>5}")
    print(f"  extract-noise:  {len(noise_set):>5}")
    print(f"  qualifiers:     {len(qualifier_set):>5}")
    print(f"  characteristics:{len(char_set):>5}")

    locus_strongs = sorted(locus_set)
    generic_strongs = sorted(generic_set)
    noise_strongs = sorted(noise_set)
    qualifier_strongs = sorted(qualifier_set)
    char_strongs_all = sorted(char_set)

    print("\nClustering LOCI...")
    locus_indices = [idx_map[s] for s in locus_strongs]
    k_loci = min(args.k_loci, max(2, len(locus_strongs) // 3))
    locus_labels = cluster_kmeans(combined[locus_indices], k_loci)

    char_hebrew = [s for s in char_strongs_all if meta[s]["language"] == "Hebrew"]
    char_greek = [s for s in char_strongs_all if meta[s]["language"] == "Greek"]
    print(f"\nClustering Hebrew chars ({len(char_hebrew)}, k={args.k_char_hebrew})...")
    heb_indices = [idx_map[s] for s in char_hebrew]
    k_heb = min(args.k_char_hebrew, max(2, len(char_hebrew) // 8))
    heb_labels = cluster_kmeans(combined[heb_indices], k_heb)
    print(f"Clustering Greek chars ({len(char_greek)}, k={args.k_char_greek})...")
    gk_indices = [idx_map[s] for s in char_greek]
    k_gk = min(args.k_char_greek, max(2, len(char_greek) // 8))
    gk_labels = cluster_kmeans(combined[gk_indices], k_gk)

    print("\nAttaching qualifiers via co-occurrence...")
    heb_quals = [q for q in qualifier_strongs if meta[q]["language"] == "Hebrew"]
    gk_quals = [q for q in qualifier_strongs if meta[q]["language"] == "Greek"]
    heb_attach, heb_qual_top = attach_qualifiers_to_clusters(
        heb_quals, char_hebrew, heb_labels, verse_terms_map
    )
    gk_attach, gk_qual_top = attach_qualifiers_to_clusters(
        gk_quals, char_greek, gk_labels, verse_terms_map
    )

    md_loci = render_clusters_md(
        "LOCI clusters", locus_strongs, locus_labels, meta,
        combined, idx_map, f"k: {k_loci}", profile
    )
    md_heb = render_clusters_md(
        "CHARACTERISTIC clusters — Hebrew (with verse profile + qualifiers)",
        char_hebrew, heb_labels, meta, combined, idx_map,
        f"k: {k_heb}", profile, qualifier_attach=heb_attach
    )
    md_gk = render_clusters_md(
        "CHARACTERISTIC clusters — Greek (with verse profile + qualifiers)",
        char_greek, gk_labels, meta, combined, idx_map,
        f"k: {k_gk}", profile, qualifier_attach=gk_attach
    )

    out_loci = out_prefix + "-loci.md"
    out_heb = out_prefix + "-characteristics-hebrew.md"
    out_gk = out_prefix + "-characteristics-greek.md"
    out_buckets = out_prefix + "-bucket-summary.md"
    out_qualifiers = out_prefix + "-qualifiers.md"
    out_json = out_prefix + ".json"

    os.makedirs(os.path.dirname(out_loci), exist_ok=True)
    with open(out_loci, "w", encoding="utf-8") as f:
        f.write(md_loci)
    with open(out_heb, "w", encoding="utf-8") as f:
        f.write(md_heb)
    with open(out_gk, "w", encoding="utf-8") as f:
        f.write(md_gk)

    bucket_lines = [
        "# 5-way term split — bucket summary (v4 with verse profile)",
        "",
        f"**Generated:** {now_iso()}",
        "",
        f"- Working set: **{len(common):,} terms** (0-verse and deleted excluded)",
        "",
        "## Bucket sizes",
        "",
        "| Bucket | Count | Role in clustering |",
        "|---|---|---|",
        f"| LOCI | {len(locus_strongs)} | Clustered separately |",
        f"| GENERICS | {len(generic_strongs)} | Excluded entirely |",
        f"| EXTRACTION-NOISE | {len(noise_strongs)} | Excluded entirely |",
        f"| QUALIFIERS | {len(qualifier_strongs)} | Excluded from primary clustering; attached post-hoc |",
        f"| CHARACTERISTICS | {len(char_strongs_all)} | **Primary clustering pool** |",
        f"|   ↳ Hebrew | {len(char_hebrew)} | k={k_heb} |",
        f"|   ↳ Greek | {len(char_greek)} | k={k_gk} |",
        "",
        "## Verse profile fields",
        "",
        "Each term entry in JSON now carries:",
        "- `verse_count` — number of distinct OWNER-active verses term appears in",
        "- `multi_term_count` — verses where another OWNER term also appears",
        "- `multi_term_pct` — multi_term_count / verse_count × 100",
    ]
    with open(out_buckets, "w", encoding="utf-8") as f:
        f.write("\n".join(bucket_lines))

    qual_lines = [
        "# Qualifier list with cluster attachments + verse profile",
        "",
        f"**Generated:** {now_iso()}",
        f"**Total qualifiers:** {len(qualifier_strongs)}",
        "",
        "## Hebrew qualifiers",
        "",
        "| Strong's | translit | gloss | verses | multi% | top clusters |",
        "|---|---|---|---|---|---|",
    ]
    for q in heb_quals:
        m = meta.get(q, {})
        p = profile.get(q, {})
        tops = heb_qual_top.get(q, [])
        tops_str = "; ".join(f"H-c{e['cluster']}·{e['affinity']:.2f}"
                              for e in tops) or "—"
        qual_lines.append(
            f"| {q} | {m.get('transliteration') or ''} | "
            f"{(m.get('gloss') or '')[:35]} | "
            f"{p.get('verse_count', '')} | "
            f"{p.get('multi_term_pct', '')}% | {tops_str} |"
        )
    qual_lines.extend(["", "## Greek qualifiers", "",
        "| Strong's | translit | gloss | verses | multi% | top clusters |",
        "|---|---|---|---|---|---|"])
    for q in gk_quals:
        m = meta.get(q, {})
        p = profile.get(q, {})
        tops = gk_qual_top.get(q, [])
        tops_str = "; ".join(f"G-c{e['cluster']}·{e['affinity']:.2f}"
                              for e in tops) or "—"
        qual_lines.append(
            f"| {q} | {m.get('transliteration') or ''} | "
            f"{(m.get('gloss') or '')[:35]} | "
            f"{p.get('verse_count', '')} | "
            f"{p.get('multi_term_pct', '')}% | {tops_str} |"
        )
    with open(out_qualifiers, "w", encoding="utf-8") as f:
        f.write("\n".join(qual_lines))

    def with_profile(s):
        m = meta.get(s, {})
        p = profile.get(s, {})
        return {**m, **p}

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_working_set": len(common),
            "n_locus": len(locus_strongs),
            "n_generic": len(generic_strongs),
            "n_extraction_noise": len(noise_strongs),
            "n_qualifier": len(qualifier_strongs),
            "n_characteristic": len(char_strongs_all),
            "n_char_hebrew": len(char_hebrew),
            "n_char_greek": len(char_greek),
            "k_loci": k_loci, "k_char_hebrew": k_heb, "k_char_greek": k_gk,
            "verse_profile_fields": ["verse_count", "multi_term_count", "multi_term_pct"],
        },
        "loci": [{"strong": s, "cluster": int(lbl), **with_profile(s)}
                 for s, lbl in zip(locus_strongs, locus_labels)],
        "generics": [{"strong": s, **with_profile(s)} for s in generic_strongs],
        "extraction_noise": [{"strong": s, **with_profile(s)} for s in noise_strongs],
        "qualifiers": [{"strong": s, **with_profile(s)} for s in qualifier_strongs],
        "characteristics_hebrew": [
            {"strong": s, "cluster": int(lbl), **with_profile(s)}
            for s, lbl in zip(char_hebrew, heb_labels)
        ],
        "characteristics_greek": [
            {"strong": s, "cluster": int(lbl), **with_profile(s)}
            for s, lbl in zip(char_greek, gk_labels)
        ],
        "qualifier_top_clusters": {
            "hebrew": {q: heb_qual_top.get(q, []) for q in heb_quals},
            "greek": {q: gk_qual_top.get(q, []) for q in gk_quals},
        },
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"\nWrote: {out_loci}")
    print(f"Wrote: {out_heb}")
    print(f"Wrote: {out_gk}")
    print(f"Wrote: {out_buckets}")
    print(f"Wrote: {out_qualifiers}")
    print(f"Wrote: {out_json}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
