"""_exploratory_term_usage_vector_v1_20260504.py — read-only.

Vector 2: term usage vector. Builds an embedding per OWNER + XREF Strong's
from how the term is actually used — specifically:

  - Verses where the term occurs (verse_record + target_word context window)
  - The verse_context_group.context_description for that (verse, term)
    pair when one exists (richer than raw verse text alone)

Sampling: per term, take up to MAX_VERSES verses across the canon. Random
sample with fixed seed for reproducibility.

Output:
  outputs/markdown/term-usage-vectors-{date}.npz
    - strongs:        array of Strong's IDs
    - vectors:        (N, dim) float32
    - n_verses_used:  per-term sample size
  outputs/markdown/term-usage-vectors-{date}.meta.json
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sqlite3
import sys
from datetime import datetime, timezone

import numpy as np

DB_PATH = os.path.join("database", "bible_research.db")
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
MAX_VERSES = 30
SEED = 20260504


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_strongs(conn):
    """All distinct Strong's that are extracted (OWNER) and have at least
    one verse-record."""
    return [r["strongs_number"] for r in conn.execute("""
        SELECT DISTINCT mt.strongs_number
          FROM mti_terms mt
         WHERE mt.delete_flagged = 0
           AND mt.status IN ('extracted','extracted_thin','extracted_theological_anchor')
           AND EXISTS (
             SELECT 1
               FROM wa_term_inventory ti
               JOIN wa_verse_records vr ON vr.term_inv_id = ti.id
              WHERE ti.strongs_number = mt.strongs_number
                AND ti.term_owner_type='OWNER'
                AND ti.delete_flagged=0
                AND vr.delete_flagged=0
           )
         ORDER BY mt.strongs_number
    """).fetchall()]


def fetch_term_verses(conn, strong, max_n, rng):
    """Return up to max_n verse-record entries for a term, with optional
    group context_description if a (verse, term) classification exists."""
    rows = conn.execute("""
        SELECT vr.id        AS vr_id,
               vr.reference AS reference,
               vr.verse_text AS verse_text,
               vr.target_word AS target_word,
               (SELECT vcg.context_description
                  FROM verse_context vc
                  JOIN verse_context_group vcg ON vcg.id = vc.group_id
                 WHERE vc.verse_record_id = vr.id
                   AND vc.delete_flagged = 0
                   AND vcg.delete_flagged = 0
                   AND vcg.mti_term_id = (
                     SELECT id FROM mti_terms
                      WHERE strongs_number = ? AND delete_flagged=0 LIMIT 1
                   )
                 LIMIT 1) AS context_description
          FROM wa_verse_records vr
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                                    AND ti.term_owner_type='OWNER'
                                    AND ti.delete_flagged=0
         WHERE vr.delete_flagged = 0
           AND ti.strongs_number = ?
    """, (strong, strong)).fetchall()
    if not rows:
        return []
    rows = list(rows)
    rng.shuffle(rows)
    return rows[:max_n]


def build_doc(strong, verses):
    """Aggregate verse snippets into one usage doc."""
    parts = [f"Strong's {strong}"]
    for v in verses:
        bits = [v["reference"] or ""]
        if v["target_word"]:
            bits.append(f"target='{v['target_word']}'")
        if v["context_description"]:
            bits.append(f"meaning: {v['context_description']}")
        elif v["verse_text"]:
            txt = v["verse_text"][:240]
            bits.append(f"verse: {txt}")
        parts.append(" — ".join(b for b in bits if b))
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-verses", type=int, default=MAX_VERSES)
    ap.add_argument("--out-prefix", default=None)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown",
        f"term-usage-vectors-{today_compact()}"
    )
    out_npz = out_prefix + ".npz"
    out_meta = out_prefix + ".meta.json"

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Fetching Strong's list...")
    strongs = fetch_strongs(conn)
    if args.limit:
        strongs = strongs[:args.limit]
    print(f"Distinct Strong's with verse-records: {len(strongs):,}")

    print(f"Loading model: {args.model}")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(args.model)

    rng = random.Random(SEED)
    docs = []
    n_verses_used = []
    print(f"Building per-term usage docs (max {args.max_verses} verses each)...")
    for i, s in enumerate(strongs, 1):
        verses = fetch_term_verses(conn, s, args.max_verses, rng)
        n_verses_used.append(len(verses))
        docs.append(build_doc(s, verses))
        if i % 500 == 0:
            print(f"  built {i}/{len(strongs)}")

    print(f"Encoding {len(docs)} documents...")
    vectors = model.encode(
        docs,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)

    os.makedirs(os.path.dirname(out_npz), exist_ok=True)
    np.savez_compressed(
        out_npz,
        strongs=np.array(strongs),
        vectors=vectors,
        n_verses_used=np.array(n_verses_used, dtype=np.int32),
    )
    meta = {
        "generated_at": now_iso(),
        "model": args.model,
        "n_terms": len(strongs),
        "dim": int(vectors.shape[1]),
        "max_verses_per_term": args.max_verses,
        "seed": SEED,
        "doc_fields": [
            "reference", "target_word",
            "verse_context_group.context_description (if classified)",
            "verse_text (fallback)",
        ],
        "normalize": True,
        "source_db": DB_PATH,
    }
    with open(out_meta, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print(f"Wrote: {out_npz}")
    print(f"Wrote: {out_meta}")
    print(f"Shape: {vectors.shape}")
    print(f"Verses used per term: min={min(n_verses_used)}, "
          f"max={max(n_verses_used)}, "
          f"avg={sum(n_verses_used)/len(n_verses_used):.1f}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
