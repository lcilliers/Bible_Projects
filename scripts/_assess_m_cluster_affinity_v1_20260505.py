"""_assess_m_cluster_affinity_v1_20260505.py — read-only.

For a chosen M-cluster (e.g. M05), scan terms in T2 and FLAG buckets to
surface candidates that may belong to that M-cluster.

Two signals:
  1. Semantic similarity — cosine sim of each candidate term's
     semantic-weighted vector against the M-cluster centroid.
  2. Keyword affinity — does the candidate's gloss/meaning text contain
     any of a researcher-curated lexicon for the M-cluster theme?

Output:
  - Likely (sim >= LIKELY_SIM OR has keyword AND sim >= MEDIUM_SIM)
  - Review (MEDIUM_SIM <= sim < LIKELY_SIM)
  - Top-30 by sim regardless of bucket

Usage:
  python scripts/_assess_m_cluster_affinity_v1_20260505.py --m-cluster M05
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

import numpy as np

DB_PATH = os.path.join("database", "bible_research.db")
V6_PATH = "archive/Clusters/wa-term-anchor-v6-20260504.json"
NPZ_PATH = "archive/Clusters/term-semantic-weighted-vectors-20260504.npz"

LIKELY_SIM = 0.55
MEDIUM_SIM = 0.40

# Per-M-cluster keyword lexicon. Keys are M-cluster IDs.
LEXICON = {
    "M05": [  # Love, Compassion and Kindness
        "love", "lover", "loving", "beloved", "dear", "dearly",
        "friend", "friendly", "friendship", "companion",
        "affection", "affectionate", "tender",
        "compassion", "compassionate", "pity", "pitiful",
        "mercy", "merciful", "merciless",
        "kind", "kindness", "kindly",
        "gentle", "gentleness", "meek",
        "comfort", "console", "consolation", "encouragement",
        "sympathy", "sympathize", "sympathetic",
        "benevolence", "benevolent",
        "embrace", "kiss",
        "hospitable", "hospitality",
        "graciousness",
    ],
    "M06": [  # Hate, Contempt and Hostility
        "hate", "hated", "hatred", "hateful", "hating",
        "contempt", "contemptuous", "contemptible",
        "despise", "despised", "despising",
        "hostility", "hostile", "enemy", "enmity", "adversary",
        "abhor", "abhorrent", "abhorrence",
        "detest", "detested", "detestable",
        "abomination", "abominable",
        "scorn", "scornful", "mock", "mocking", "mockery",
        "derision", "deride", "ridicule", "taunt", "taunting",
        "spurn", "reject", "rejection",
        "disgust", "disgusting", "loathe", "loathsome", "loathing",
        "revile", "reviling", "revilement", "curse", "cursing",
        "reproach", "reviled", "shame-on", "vilify",
        "antagonism", "animosity", "rancor", "rancour",
        "miseo", "miseō", "echthros", "echthra",
        "sane", "shema", "buz",
    ],
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def keyword_hits(text, lex):
    if not text:
        return []
    t = text.lower()
    hits = []
    for kw in lex:
        # word-boundary search
        if re.search(rf"\b{re.escape(kw)}\b", t):
            hits.append(kw)
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.m_cluster not in LEXICON:
        print(f"WARN: no keyword lexicon for {args.m_cluster}. "
              "Will use semantic similarity only.", flush=True)
    lex = LEXICON.get(args.m_cluster, [])

    _dest_dir = os.path.join("Sessions", "Session_Clusters", args.m_cluster)
    os.makedirs(_dest_dir, exist_ok=True)
    out_path = args.out or os.path.join(
        _dest_dir,
        f"wa-cluster-{args.m_cluster.lower()}-affinity-"
        f"v1-{datetime.now().strftime('%Y%m%d')}.md"
    )

    # Load v6 anchor and split terms by cluster type
    with open(V6_PATH, encoding="utf-8") as f:
        v6 = json.load(f)
    cluster_labels = v6.get("meaning_cluster_labels", {})
    m_label = cluster_labels.get(args.m_cluster, "?")
    print(f"M-cluster {args.m_cluster}: {m_label}", flush=True)

    m_strongs = []
    t2_strongs = []
    flag_strongs = []
    for s, t in v6["term_anchors"].items():
        cid = t.get("cluster_id")
        if cid == args.m_cluster:
            m_strongs.append(s)
        elif cid == "T2":
            t2_strongs.append(s)
        elif cid == "FLAG":
            flag_strongs.append(s)
    print(f"  M-cluster terms: {len(m_strongs)}", flush=True)
    print(f"  T2 terms: {len(t2_strongs)}", flush=True)
    print(f"  FLAG terms: {len(flag_strongs)}", flush=True)

    # Load semantic vectors
    print("Loading semantic-weighted vectors...", flush=True)
    z = np.load(NPZ_PATH, allow_pickle=True)
    npz_strongs = list(z["strongs"])
    vectors = z["vectors"]
    s_to_idx = {s: i for i, s in enumerate(npz_strongs)}
    print(f"  vector universe: {len(npz_strongs)} terms, "
          f"dim {vectors.shape[1]}", flush=True)

    # M-cluster centroid (L2-normalised)
    m_idx = [s_to_idx[s] for s in m_strongs if s in s_to_idx]
    if not m_idx:
        print(f"ERROR: no M-cluster terms found in vector space.", flush=True)
        return 1
    centroid = vectors[m_idx].mean(axis=0)
    cn = np.linalg.norm(centroid)
    if cn > 0:
        centroid = centroid / cn

    # Pull DB metadata for candidates (gloss + meaning text)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    candidate_strongs = t2_strongs + flag_strongs
    placeholders = ",".join("?" * len(candidate_strongs))
    rows = conn.execute(f"""
        SELECT mt.strongs_number, mt.gloss, mt.transliteration, mt.language,
               mt.owning_registry_fk,
               wr.no AS reg_no, wr.word AS reg_word,
               wr.cluster_assignment AS reg_c_cluster,
               ti.meaning AS inv_meaning,
               ti.short_def_mounce AS mounce
          FROM mti_terms mt
          LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
          LEFT JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
         WHERE mt.strongs_number IN ({placeholders})
    """, candidate_strongs).fetchall()
    db_by_strong = {}
    for r in rows:
        s = r["strongs_number"]
        # First-row wins (multiple inventory rows possible)
        if s not in db_by_strong:
            db_by_strong[s] = dict(r)
    conn.close()

    # Score every candidate
    print("Scoring candidates...", flush=True)
    candidates = []
    for s in candidate_strongs:
        anchor = v6["term_anchors"].get(s, {})
        idx = s_to_idx.get(s)
        if idx is None:
            sim = 0.0
            no_vector = True
        else:
            v = vectors[idx]
            n = np.linalg.norm(v)
            sim = float(np.dot(v, centroid) / n) if n > 0 else 0.0
            no_vector = False
        db = db_by_strong.get(s, {})
        gloss = anchor.get("gloss") or db.get("gloss") or ""
        meaning = db.get("inv_meaning") or ""
        mounce = db.get("mounce") or ""
        scan_text = " | ".join([gloss, meaning, mounce])
        hits = keyword_hits(scan_text, lex)
        candidates.append({
            "strong": s,
            "gloss": gloss,
            "translit": anchor.get("transliteration")
                        or db.get("transliteration"),
            "lang": anchor.get("lang") or (db.get("language", "") or "")[:1],
            "bucket": anchor.get("bucket"),
            "current_cluster": anchor.get("cluster_id"),
            "registry": (
                f"R{db.get('reg_no'):03d} {db.get('reg_word')}"
                if db.get("reg_no") else None
            ),
            "reg_c_cluster": db.get("reg_c_cluster"),
            "sim": sim,
            "no_vector": no_vector,
            "kw_hits": hits,
            "n_kw_hits": len(hits),
        })

    # Tier and sort
    likely = []
    review = []
    other_with_kw = []
    for c in candidates:
        if c["no_vector"] and c["n_kw_hits"] > 0:
            other_with_kw.append(c)
            continue
        if c["sim"] >= LIKELY_SIM or (
            c["n_kw_hits"] > 0 and c["sim"] >= MEDIUM_SIM
        ):
            likely.append(c)
        elif c["sim"] >= MEDIUM_SIM:
            review.append(c)
        elif c["n_kw_hits"] > 0:
            # has keyword but low sim — surface for inspection
            other_with_kw.append(c)
    likely.sort(key=lambda x: -x["sim"])
    review.sort(key=lambda x: -x["sim"])
    other_with_kw.sort(key=lambda x: (-x["n_kw_hits"], -x["sim"]))

    # Top-30 by sim regardless
    top30 = sorted(candidates, key=lambda x: -x["sim"])[:30]

    # Render
    lines = []
    lines.append(f"# {args.m_cluster} {m_label} — affinity scan over "
                 "T2 + FLAG\n")
    lines.append(f"**Generated:** {now_iso()}  ")
    lines.append(f"**Centroid built from:** "
                 f"{len(m_idx)} M-cluster terms in the semantic-weighted "
                 "vector space  ")
    lines.append(f"**Candidates scanned:** "
                 f"{len(t2_strongs)} T2 + {len(flag_strongs)} FLAG = "
                 f"{len(candidate_strongs)} terms\n")
    lines.append("**Method:**")
    lines.append("- *Semantic similarity* — cosine of each candidate's "
                 "semantic-weighted vector against the M-cluster centroid")
    lines.append("- *Keyword hit* — gloss/meaning/Mounce text contains a "
                 "love-vocabulary keyword "
                 f"({', '.join(lex[:8])}, …)\n")
    lines.append(f"**Tiers:**")
    lines.append(f"- ⭐ **LIKELY** — sim ≥ {LIKELY_SIM} OR "
                 f"(keyword match AND sim ≥ {MEDIUM_SIM})")
    lines.append(f"- 🔍 **REVIEW** — {MEDIUM_SIM} ≤ sim < {LIKELY_SIM}, "
                 "no keyword hit")
    lines.append(f"- 📌 **KEYWORD-ONLY** — keyword hit but sim < "
                 f"{MEDIUM_SIM} (semantic distance large but lexical match)\n")
    lines.append("---\n")

    lines.append("## Tier 1 — LIKELY M05 candidates "
                 f"({len(likely)})\n")
    if not likely:
        lines.append("*(none)*\n")
    else:
        lines.append("Sorted by similarity descending. Strong candidates "
                     "for reassessment as M-cluster members.\n")
        lines.append("| Strong's | Lang | Translit | Gloss | Bucket | "
                     "Registry | C-cluster | Sim | Keyword hits |")
        lines.append("|---|---|---|---|---|---|---|---:|---|")
        for c in likely:
            lines.append(_row(c))
    lines.append("")

    lines.append(f"## Tier 2 — REVIEW ({len(review)})\n")
    if not review:
        lines.append("*(none)*\n")
    else:
        lines.append("Mid-similarity, no keyword hit — semantically near "
                     "but worth a manual look.\n")
        lines.append("| Strong's | Lang | Translit | Gloss | Bucket | "
                     "Registry | Sim |")
        lines.append("|---|---|---|---|---|---|---:|")
        for c in review[:60]:
            registry = c["registry"] or "—"
            lang = c["lang"] or ""
            translit = c["translit"] or ""
            gloss = c["gloss"] or ""
            lines.append(
                f"| {c['strong']} | {lang} | {translit} | {gloss} | "
                f"{c['bucket'] or '—'} | {registry} | {c['sim']:.3f} |"
            )
        if len(review) > 60:
            lines.append(f"\n*(showing 60 of {len(review)} — see JSON "
                         "companion for full list)*")
    lines.append("")

    lines.append(f"## Tier 3 — KEYWORD-ONLY ({len(other_with_kw)})\n")
    if not other_with_kw:
        lines.append("*(none)*\n")
    else:
        lines.append("Lexical match but semantic distance large — usually "
                     "homonyms, metaphorical extensions, or peripheral "
                     "occurrences. Worth a quick scan but not a primary "
                     "review queue.\n")
        lines.append("| Strong's | Lang | Translit | Gloss | Bucket | "
                     "Registry | Sim | Keyword hits |")
        lines.append("|---|---|---|---|---|---|---:|---|")
        for c in other_with_kw[:40]:
            lines.append(_row(c))
        if len(other_with_kw) > 40:
            lines.append(f"\n*(showing 40 of {len(other_with_kw)})*")
    lines.append("")

    lines.append("## Top-30 by similarity (any bucket)\n")
    lines.append("| # | Strong's | Lang | Gloss | Bucket | Sim | "
                 "Keyword hits |")
    lines.append("|---|---|---|---|---|---:|---|")
    for i, c in enumerate(top30, 1):
        lines.append(
            f"| {i} | {c['strong']} | {c['lang'] or ''} | "
            f"{c['gloss'] or ''} | {c['bucket'] or '—'} | "
            f"{c['sim']:.3f} | "
            f"{', '.join(c['kw_hits']) if c['kw_hits'] else '—'} |"
        )
    lines.append("")

    # Companion JSON
    out_json = out_path.replace(".md", ".json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "generated": now_iso(),
                "m_cluster": args.m_cluster,
                "m_label": m_label,
                "thresholds": {"likely": LIKELY_SIM, "medium": MEDIUM_SIM},
                "n_centroid_terms": len(m_idx),
                "n_candidates": len(candidate_strongs),
            },
            "lexicon": lex,
            "tiers": {
                "likely": likely,
                "review": review,
                "keyword_only": other_with_kw,
            },
            "top30_by_sim": top30,
        }, f, indent=2, ensure_ascii=False)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {out_path}", flush=True)
    print(f"Wrote: {out_json}", flush=True)
    print(f"\nLIKELY={len(likely)} REVIEW={len(review)} "
          f"KEYWORD-ONLY={len(other_with_kw)}", flush=True)
    return 0


def _row(c):
    registry = c["registry"] or "—"
    lang = c["lang"] or ""
    translit = c["translit"] or ""
    gloss = c["gloss"] or ""
    kw = ", ".join(c["kw_hits"]) if c["kw_hits"] else "—"
    return (
        f"| {c['strong']} | {lang} | {translit} | {gloss} | "
        f"{c['bucket'] or '—'} | {registry} | "
        f"{c.get('reg_c_cluster') or '—'} | "
        f"{c['sim']:.3f} | {kw} |"
    )


if __name__ == "__main__":
    sys.exit(main())
