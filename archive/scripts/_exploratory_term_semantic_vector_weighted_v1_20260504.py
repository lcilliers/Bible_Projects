"""_exploratory_term_semantic_vector_weighted_v1_20260504.py — read-only.

Restructured semantic vector with explicit weighted components:

  v_root    — categorical multi-hot of root_code(s); definitional cluster
  v_gloss   — embedding of (transliteration + gloss + step_search_gloss)
  v_meaning — embedding of (senses + meaning text)

Final vector = L2-normalised concat(w_root * v_root, w_gloss * v_gloss,
                                    w_meaning * v_meaning).

Mounce short_def is tracked SEPARATELY as a per-term list of sub-senses
(comma-split). This is exposed via a "mounce bridge map" sidecar — for each
term, the comma-separated sub-senses that may pull the term across clusters.

Output:
  outputs/markdown/term-semantic-weighted-vectors-{date}.npz
  outputs/markdown/term-semantic-weighted-vectors-{date}.meta.json
  outputs/markdown/term-mounce-bridges-{date}.json   (sidecar)
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
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def fetch_terms(conn):
    return conn.execute("""
        SELECT mt.strongs_number,
               mt.transliteration,
               mt.gloss,
               mt.language,
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


def fetch_root_codes(conn, strong):
    rows = conn.execute("""
        SELECT rf.root_code, rf.root_language
          FROM wa_term_root_family rf
          JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
         WHERE ti.strongs_number = ? AND ti.term_owner_type='OWNER'
           AND ti.delete_flagged=0 AND rf.delete_flagged=0
    """, (strong,)).fetchall()
    return [
        f"{(r['root_language'] or '').strip()}:{(r['root_code'] or '').strip()}"
        for r in rows if r["root_code"]
    ]


def fetch_root_glosses(conn, strong):
    rows = conn.execute("""
        SELECT rf.root_gloss
          FROM wa_term_root_family rf
          JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id
         WHERE ti.strongs_number = ? AND ti.term_owner_type='OWNER'
           AND ti.delete_flagged=0 AND rf.delete_flagged=0
           AND rf.root_gloss IS NOT NULL
    """, (strong,)).fetchall()
    return [r["root_gloss"] for r in rows if r["root_gloss"]]


def fetch_senses(conn, parsed_meaning_id):
    if not parsed_meaning_id:
        return ""
    rows = conn.execute("""
        SELECT level_code, sense_text, domain_tag
          FROM wa_meaning_sense
         WHERE parsed_meaning_id = ?
         ORDER BY sort_order
    """, (parsed_meaning_id,)).fetchall()
    return " | ".join(
        " ".join(b for b in [r["level_code"] or "", r["sense_text"] or "",
                              f"({r['domain_tag']})" if r["domain_tag"] else ""]
                 if b)
        for r in rows
    )


MOUNCE_SPLIT_RE = re.compile(r"[,;]|\bor\b")


def split_mounce(short_def):
    if not short_def:
        return []
    parts = MOUNCE_SPLIT_RE.split(short_def)
    return [p.strip() for p in parts if p and p.strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--w-root", type=float, default=0.35)
    ap.add_argument("--w-gloss", type=float, default=0.35)
    ap.add_argument("--w-meaning", type=float, default=0.30)
    ap.add_argument("--out-prefix", default=None)
    args = ap.parse_args()

    out_prefix = args.out_prefix or os.path.join(
        "outputs", "markdown",
        f"term-semantic-weighted-vectors-{today_compact()}"
    )
    out_npz = out_prefix + ".npz"
    out_meta = out_prefix + ".meta.json"
    out_mounce = os.path.join(
        "outputs", "markdown",
        f"term-mounce-bridges-{today_compact()}.json"
    )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Fetching terms...")
    terms = fetch_terms(conn)
    print(f"Term rows: {len(terms):,}")

    # Step 1: collect root codes for all terms (build categorical universe)
    print("Collecting root codes...")
    term_roots = []
    all_roots = set()
    for t in terms:
        codes = fetch_root_codes(conn, t["strongs_number"])
        term_roots.append(codes)
        all_roots.update(codes)
    root_to_idx = {r: i for i, r in enumerate(sorted(all_roots))}
    n_roots = len(root_to_idx)
    print(f"  distinct root codes: {n_roots:,}")
    print(f"  terms with at least one root: "
          f"{sum(1 for rs in term_roots if rs):,} / {len(terms):,}")

    # Step 2: build root signatures (multi-hot, L2-normalised)
    print("Building root signatures...")
    v_root = np.zeros((len(terms), n_roots), dtype=np.float32)
    for i, codes in enumerate(term_roots):
        if not codes:
            continue
        for c in codes:
            v_root[i, root_to_idx[c]] = 1.0
    norms = np.linalg.norm(v_root, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    v_root = v_root / norms

    # Step 3: build gloss texts
    print("Building gloss texts...")
    gloss_texts = []
    for t in terms:
        bits = []
        if t["transliteration"]:
            bits.append(t["transliteration"])
        if t["gloss"]:
            bits.append(t["gloss"])
        if t["step_search_gloss"] and t["step_search_gloss"] != t["gloss"]:
            bits.append(t["step_search_gloss"])
        # also include root_glosses (definitional + cross-language anchor)
        bits += fetch_root_glosses(conn, t["strongs_number"])
        gloss_texts.append(" ".join(bits) or t["strongs_number"])

    # Step 4: build meaning texts
    print("Building meaning texts...")
    meaning_texts = []
    for t in terms:
        senses = fetch_senses(conn, t["parsed_meaning_id"])
        bits = []
        if senses:
            bits.append(senses[:2000])
        if t["meaning"]:
            bits.append(t["meaning"][:2000])
        meaning_texts.append(" | ".join(bits) or t["strongs_number"])

    # Step 5: encode gloss + meaning
    print(f"Loading model: {args.model}")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(args.model)
    print("Encoding gloss texts...")
    v_gloss = model.encode(
        gloss_texts, batch_size=64, show_progress_bar=True,
        convert_to_numpy=True, normalize_embeddings=True
    ).astype(np.float32)
    print("Encoding meaning texts...")
    v_meaning = model.encode(
        meaning_texts, batch_size=64, show_progress_bar=True,
        convert_to_numpy=True, normalize_embeddings=True
    ).astype(np.float32)

    # Step 6: weighted concat + L2-normalise
    w_root, w_gloss, w_meaning = args.w_root, args.w_gloss, args.w_meaning
    weight_sum = w_root + w_gloss + w_meaning
    if abs(weight_sum - 1.0) > 1e-6:
        # normalise
        w_root, w_gloss, w_meaning = (
            w_root / weight_sum, w_gloss / weight_sum, w_meaning / weight_sum
        )
    print(f"Weights (normalised): root={w_root:.3f} · "
          f"gloss={w_gloss:.3f} · meaning={w_meaning:.3f}")

    final = np.concatenate([
        w_root * v_root,
        w_gloss * v_gloss,
        w_meaning * v_meaning,
    ], axis=1)
    final_norms = np.linalg.norm(final, axis=1, keepdims=True)
    final_norms[final_norms == 0] = 1.0
    final = (final / final_norms).astype(np.float32)

    strongs = np.array([t["strongs_number"] for t in terms])
    languages = np.array([t["language"] or "" for t in terms])
    registries = np.array([
        f"R{t['reg_no']:03d} {t['reg_word']}" if t["reg_no"] else ""
        for t in terms
    ])

    os.makedirs(os.path.dirname(out_npz), exist_ok=True)
    np.savez_compressed(
        out_npz,
        strongs=strongs,
        vectors=final,
        languages=languages,
        registries=registries,
    )
    meta = {
        "generated_at": now_iso(),
        "model": args.model,
        "n_terms": len(terms),
        "components": {
            "root": {"dim": n_roots, "weight": w_root,
                     "n_distinct_codes": n_roots},
            "gloss": {"dim": int(v_gloss.shape[1]), "weight": w_gloss},
            "meaning": {"dim": int(v_meaning.shape[1]), "weight": w_meaning},
        },
        "final_dim": int(final.shape[1]),
        "mounce_handling": "tracked separately as bridge map; not in primary vector",
        "source_db": DB_PATH,
    }
    with open(out_meta, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    # Step 7: build the mounce bridge map (sidecar)
    print("Building mounce bridge map...")
    bridges = {}
    for t in terms:
        senses = split_mounce(t["short_def_mounce"])
        if len(senses) >= 2:
            bridges[t["strongs_number"]] = {
                "transliteration": t["transliteration"],
                "gloss": t["gloss"],
                "mounce_short_def": t["short_def_mounce"],
                "sub_senses": senses,
                "owning_registry": (f"R{t['reg_no']:03d} {t['reg_word']}"
                                     if t["reg_no"] else None),
            }
    with open(out_mounce, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "generated_at": now_iso(),
                "n_terms_with_multi_sense_mounce": len(bridges),
                "note": "Each term here has 2+ Mounce sub-senses; treat each "
                        "sub-sense as a potential cross-cluster bridge.",
            },
            "bridges": bridges,
        }, f, indent=2, ensure_ascii=False)

    print(f"Wrote: {out_npz}")
    print(f"Wrote: {out_meta}")
    print(f"Wrote: {out_mounce}")
    print(f"Final vector shape: {final.shape}")
    print(f"Multi-sense mounce bridges: {len(bridges):,} terms")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
