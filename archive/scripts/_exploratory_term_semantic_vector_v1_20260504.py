"""_exploratory_term_semantic_vector_v1_20260504.py — read-only.

Vector 1: term semantic vector. Builds an embedding per OWNER + XREF
Strong's from its lexical metadata (transliteration, gloss, mounce def,
meaning text, senses, root family).

Output:
  outputs/markdown/term-semantic-vectors-{date}.npz
    - strongs:    array of Strong's IDs (str)
    - vectors:    (N, dim) float32 array
    - languages:  array of "Hebrew"|"Greek"
    - registries: array of "R### word" (or empty)
  outputs/markdown/term-semantic-vectors-{date}.meta.json
    - model name, dim, build params

Default model: sentence-transformers/all-MiniLM-L6-v2 (384-dim, fast).
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

import numpy as np

DB_PATH = os.path.join("database", "bible_research.db")
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_terms(conn):
    """One row per distinct Strong's that has at least one OWNER inventory
    row, joined with mti_terms metadata + registry. parsed_meaning_id and
    other lexical fields come from the OWNER wa_term_inventory row."""
    return conn.execute("""
        SELECT mt.strongs_number,
               mt.transliteration,
               mt.gloss,
               mt.language,
               mt.status,
               mt.owning_registry_fk,
               wr.no   AS reg_no,
               wr.word AS reg_word,
               ti.parsed_meaning_id,
               ti.short_def_mounce,
               ti.step_search_gloss,
               ti.meaning
          FROM mti_terms mt
          LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
          LEFT JOIN wa_term_inventory ti
                 ON ti.strongs_number = mt.strongs_number
                AND ti.term_owner_type = 'OWNER'
                AND ti.delete_flagged = 0
         WHERE mt.delete_flagged = 0
           AND mt.status IN ('extracted','extracted_thin','extracted_theological_anchor')
         GROUP BY mt.strongs_number
         ORDER BY mt.strongs_number
    """).fetchall()


def fetch_senses(conn, parsed_meaning_id):
    if not parsed_meaning_id:
        return ""
    rows = conn.execute("""
        SELECT level_code, sense_text, domain_tag
          FROM wa_meaning_sense
         WHERE parsed_meaning_id = ?
         ORDER BY sort_order
    """, (parsed_meaning_id,)).fetchall()
    parts = []
    for r in rows:
        bits = [r["level_code"] or "", r["sense_text"] or ""]
        if r["domain_tag"]:
            bits.append(f"({r['domain_tag']})")
        parts.append(" ".join(b for b in bits if b))
    return " | ".join(parts)


def fetch_root_family(conn, strong):
    rows = conn.execute("""
        SELECT root_code, root_language, root_gloss, note
          FROM wa_term_root_family rf
          JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
         WHERE ti.strongs_number = ? AND ti.term_owner_type='OWNER'
           AND ti.delete_flagged=0 AND rf.delete_flagged=0
         LIMIT 8
    """, (strong,)).fetchall()
    parts = []
    for r in rows:
        bits = []
        if r["root_code"]:
            bits.append(r["root_code"])
        if r["root_gloss"]:
            bits.append(f"({r['root_gloss']})")
        if bits:
            parts.append(" ".join(bits))
    return ", ".join(parts)


def build_doc(meta, senses_text, root_text):
    """Concatenate term metadata into one document for embedding."""
    parts = []
    if meta["transliteration"]:
        parts.append(f"transliteration: {meta['transliteration']}")
    if meta["gloss"]:
        parts.append(f"gloss: {meta['gloss']}")
    if meta["step_search_gloss"] and meta["step_search_gloss"] != meta["gloss"]:
        parts.append(f"search-gloss: {meta['step_search_gloss']}")
    if meta["short_def_mounce"]:
        parts.append(f"def: {meta['short_def_mounce']}")
    if senses_text:
        parts.append(f"senses: {senses_text[:1500]}")
    if root_text:
        parts.append(f"roots: {root_text[:400]}")
    if meta["meaning"]:
        parts.append(f"meaning: {meta['meaning'][:1500]}")
    parts.append(f"language: {meta['language']}")
    return "\n".join(parts) or meta["strongs_number"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--out-prefix", default=None)
    ap.add_argument("--limit", type=int, default=None,
                    help="for smoke testing only")
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown",
        f"term-semantic-vectors-{today_compact()}"
    )
    out_npz = out_prefix + ".npz"
    out_meta = out_prefix + ".meta.json"

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Fetching terms...")
    terms = fetch_terms(conn)
    if args.limit:
        terms = terms[:args.limit]
    print(f"Term rows: {len(terms):,}")

    print(f"Loading model: {args.model}")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(args.model)

    docs = []
    strongs = []
    languages = []
    registries = []
    print("Building per-term documents...")
    for i, t in enumerate(terms, 1):
        senses_text = fetch_senses(conn, t["parsed_meaning_id"])
        root_text = fetch_root_family(conn, t["strongs_number"])
        doc = build_doc(t, senses_text, root_text)
        docs.append(doc)
        strongs.append(t["strongs_number"])
        languages.append(t["language"] or "")
        if t["reg_no"]:
            registries.append(f"R{t['reg_no']:03d} {t['reg_word']}")
        else:
            registries.append("")
        if i % 500 == 0:
            print(f"  built {i}/{len(terms)} docs")

    print(f"Encoding {len(docs)} documents...")
    vectors = model.encode(
        docs,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)

    os.makedirs(os.path.dirname(out_npz), exist_ok=True)
    np.savez_compressed(
        out_npz,
        strongs=np.array(strongs),
        vectors=vectors,
        languages=np.array(languages),
        registries=np.array(registries),
    )
    meta = {
        "generated_at": now_iso(),
        "model": args.model,
        "n_terms": len(strongs),
        "dim": int(vectors.shape[1]),
        "doc_fields": [
            "transliteration", "gloss", "step_search_gloss",
            "short_def_mounce", "senses", "root_family", "meaning", "language"
        ],
        "normalize": True,
        "source_db": DB_PATH,
    }
    with open(out_meta, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print(f"Wrote: {out_npz}")
    print(f"Wrote: {out_meta}")
    print(f"Shape: {vectors.shape}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
