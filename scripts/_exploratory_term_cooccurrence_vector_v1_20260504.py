"""_exploratory_term_cooccurrence_vector_v1_20260504.py — read-only.

Replacement for the term-usage vector. Pure co-occurrence signal:
  for each OWNER Strong's, build a vector from which OTHER OWNER Strong's
  it appears alongside in the same verses.

No verse_context_group context_description is used.
No raw verse text is embedded.
The only signal is: terms-co-occur-in-verse.

Pipeline:
  1. For each verse-record, collect the set of OWNER Strong's present.
  2. Count pairwise co-occurrences across all verses.
  3. Compute PPMI (positive pointwise mutual information) — corrects for
     frequency bias so high-volume terms don't dominate.
  4. Truncated SVD → dense low-dimensional term embedding.
  5. L2-normalise.

Output:
  outputs/markdown/term-cooccurrence-vectors-{date}.npz
    - strongs:       (N,) array of Strong's IDs
    - vectors:       (N, dim) float32
    - n_occurrences: (N,) int — verses each term appears in
  outputs/markdown/term-cooccurrence-vectors-{date}.meta.json
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD

DB_PATH = os.path.join("database", "bible_research.db")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_verse_to_terms(conn):
    """For each distinct verse REFERENCE, return the set of OWNER Strong's
    appearing in that verse. wa_verse_records is one row per (verse, term) —
    sibling terms in a verse share the verse REFERENCE, not the row id."""
    rows = conn.execute("""
        SELECT vr.reference  AS reference,
               ti.strongs_number AS strong
          FROM wa_verse_records vr
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                    AND ti.term_owner_type = 'OWNER'
                                    AND ti.delete_flagged = 0
          JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
                            AND mt.delete_flagged = 0
                            AND mt.status IN ('extracted','extracted_thin','extracted_theological_anchor')
         WHERE vr.delete_flagged = 0
    """).fetchall()
    verse_terms = defaultdict(set)
    for r in rows:
        verse_terms[r["reference"]].add(r["strong"])
    return verse_terms


def build_cooccurrence(verse_terms):
    """Returns (strongs_sorted, cooc_dict, totals)."""
    strongs = sorted({s for ts in verse_terms.values() for s in ts})
    cooc = defaultdict(Counter)
    totals = Counter()
    for terms in verse_terms.values():
        for s in terms:
            totals[s] += 1
        terms_list = list(terms)
        for i, s1 in enumerate(terms_list):
            for s2 in terms_list[i+1:]:
                cooc[s1][s2] += 1
                cooc[s2][s1] += 1
    return strongs, cooc, totals


def build_ppmi_sparse(strongs, cooc, totals):
    """Compute PPMI as a sparse matrix (N x N)."""
    idx = {s: i for i, s in enumerate(strongs)}
    n = len(strongs)
    total_pairs = sum(sum(c.values()) for c in cooc.values())  # double-counted, OK
    if total_pairs == 0:
        return csr_matrix((n, n), dtype=np.float32)
    data, row, col = [], [], []
    for s1, neighbors in cooc.items():
        for s2, count in neighbors.items():
            # PMI = log( p(s1,s2) / (p(s1)*p(s2)) )
            #     = log( count * total_pairs / (totals[s1]*totals[s2]) )
            denom = totals[s1] * totals[s2]
            if denom == 0 or count == 0:
                continue
            pmi = math.log((count * total_pairs) / denom)
            if pmi > 0:
                data.append(pmi)
                row.append(idx[s1])
                col.append(idx[s2])
    return csr_matrix((data, (row, col)), shape=(n, n), dtype=np.float32)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-prefix", default=None)
    ap.add_argument("--svd-dim", type=int, default=200)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown",
        f"term-cooccurrence-vectors-{today_compact()}"
    )
    out_npz = out_prefix + ".npz"
    out_meta = out_prefix + ".meta.json"

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Fetching verse → terms map...")
    verse_terms = fetch_verse_to_terms(conn)
    n_verses = len(verse_terms)
    n_pairs = sum(len(t) for t in verse_terms.values())
    avg_terms = n_pairs / max(1, n_verses)
    print(f"  {n_verses:,} verse-records · {n_pairs:,} verse-term placements · "
          f"avg {avg_terms:.2f} terms/verse")

    print("Building co-occurrence matrix...")
    strongs, cooc, totals = build_cooccurrence(verse_terms)
    n_terms = len(strongs)
    n_pairs = sum(sum(c.values()) for c in cooc.values()) // 2
    print(f"  {n_terms:,} distinct Strong's · {n_pairs:,} unique co-occurrence pairs")

    print("Computing PPMI...")
    ppmi = build_ppmi_sparse(strongs, cooc, totals)
    print(f"  PPMI nnz: {ppmi.nnz:,}")

    svd_dim = min(args.svd_dim, n_terms - 1)
    print(f"Truncated SVD → {svd_dim} dims...")
    svd = TruncatedSVD(n_components=svd_dim, random_state=20260504)
    vectors = svd.fit_transform(ppmi).astype(np.float32)

    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    vectors = vectors / norms

    n_occurrences = np.array([totals[s] for s in strongs], dtype=np.int32)

    os.makedirs(os.path.dirname(out_npz), exist_ok=True)
    np.savez_compressed(
        out_npz,
        strongs=np.array(strongs),
        vectors=vectors,
        n_occurrences=n_occurrences,
    )
    meta = {
        "generated_at": now_iso(),
        "n_verses": n_verses,
        "n_terms": n_terms,
        "n_unique_pairs": n_pairs,
        "avg_terms_per_verse": round(avg_terms, 3),
        "ppmi_nnz": int(ppmi.nnz),
        "svd_dim": int(svd_dim),
        "explained_variance_ratio_sum": float(np.sum(svd.explained_variance_ratio_)),
        "method": "OWNER-Strong's co-occurrence in same verse-record → PPMI → TruncatedSVD",
        "no_verse_context_group_used": True,
        "no_verse_text_embedded": True,
    }
    with open(out_meta, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print(f"Wrote: {out_npz}")
    print(f"Wrote: {out_meta}")
    print(f"Shape: {vectors.shape}")
    print(f"Singletons (terms with no co-occurring sibling): "
          f"{int((vectors.sum(axis=1) == 0).sum())}")
    print(f"Top-10 most-occurring terms:")
    for s, c in totals.most_common(10):
        print(f"  {s:<10} {c:>6,} verses")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
