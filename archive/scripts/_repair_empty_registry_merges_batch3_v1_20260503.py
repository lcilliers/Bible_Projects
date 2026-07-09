"""_repair_empty_registry_merges_batch3_v1_20260503.py

Third (and final) batch of empty-registry merges (researcher-directed 2026-05-03):

  R104 loyalty    -> R060 faithfulness  (loyalty is the relational mode of
                                         faithfulness; cross-cluster but
                                         conceptually closest)
  R109 meekness   -> R080 humility      (meekness is strength held under
                                         humility; both C08)
  R138 reverence  -> R176 worship       (reverence is the affective core of
                                         worship; both C15)
  R205 resentment -> R013 bitterness    (resentment = held/unreleased anger
                                         pattern that defines bitterness;
                                         both C07)

Same minimal-merge pattern as batches 1-2: source registries are zero-OWNER
zero-vc, so the merge is a semantic mark only — phase1_status='Excluded'
plus audit trail.

Usage:
  python scripts/_repair_empty_registry_merges_batch3_v1_20260503.py
  python scripts/_repair_empty_registry_merges_batch3_v1_20260503.py --live
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
NOW_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

MERGES = [
    {
        "src_no": 104, "src_word": "loyalty",
        "tgt_no": 60,  "tgt_word": "faithfulness",
        "rationale": "loyalty is the relational mode of faithfulness; "
                     "cross-cluster but conceptually closest",
    },
    {
        "src_no": 109, "src_word": "meekness",
        "tgt_no": 80,  "tgt_word": "humility",
        "rationale": "meekness is strength held under humility; both in cluster C08",
    },
    {
        "src_no": 138, "src_word": "reverence",
        "tgt_no": 176, "tgt_word": "worship",
        "rationale": "reverence is the affective core of worship; both in cluster C15",
    },
    {
        "src_no": 205, "src_word": "resentment",
        "tgt_no": 13,  "tgt_word": "bitterness",
        "rationale": "resentment = held/unreleased anger pattern that defines "
                     "bitterness; both in cluster C07",
    },
]


def fetch_state(conn, no: int):
    return conn.execute(
        "SELECT no, word, phase1_status FROM word_registry WHERE no = ?", (no,)
    ).fetchone()


def execute_one(conn, item):
    src_no = item["src_no"]
    src_word = item["src_word"]
    tgt_no = item["tgt_no"]
    tgt_word = item["tgt_word"]
    rationale = item["rationale"]

    inference_note = (
        f"R{src_no:03d} EXCLUDED 2026-05-03 — empty registry merged into "
        f"R{tgt_no:03d} {tgt_word}. Rationale: {rationale}. "
        f"No structural data moved (R{src_no:03d} had zero OWNER terms and zero "
        f"vc rows); 'merge' is semantic only."
    )
    desc_append = (
        f"Merged 2026-05-03: R{src_no:03d} '{src_word}' identified as semantic "
        f"alias of R{tgt_no:03d} '{tgt_word}' ({rationale})."
    )
    cur = conn.execute("""
        UPDATE word_registry
           SET phase1_status='Excluded',
               session_b_status=NULL,
               verse_context_status=NULL,
               dim_review_status=NULL,
               inference_note=?,
               description=COALESCE(description,'') ||
                           CASE WHEN COALESCE(description,'')='' THEN '' ELSE ' | ' END ||
                           ?
         WHERE no=?
    """, (inference_note, desc_append, src_no))
    return cur.rowcount


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR,
                              f"bible_research_pre_empty_merges_b3_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    print("--- Verifying targets exist and are not Excluded ---")
    for m in MERGES:
        s = fetch_state(conn, m["src_no"])
        t = fetch_state(conn, m["tgt_no"])
        print(f"  src R{m['src_no']:03d} {m['src_word']:<14} status={s['phase1_status']!r}")
        print(f"  tgt R{m['tgt_no']:03d} {m['tgt_word']:<14} status={t['phase1_status']!r}")
    print()

    print("--- Executing ---")
    conn.execute("BEGIN")
    for m in MERGES:
        n = execute_one(conn, m)
        print(f"  R{m['src_no']:03d} {m['src_word']:<14} -> R{m['tgt_no']:03d} {m['tgt_word']:<14}: updated={n}")

    if args.live:
        conn.commit()
        print("[LIVE] Committed.")
    else:
        conn.rollback()
        print("[DRY-RUN] Rolled back.")
    print()

    print("--- AFTER ---")
    for m in MERGES:
        s = fetch_state(conn, m["src_no"])
        print(f"  R{m['src_no']:03d} {m['src_word']:<14} status={s['phase1_status']!r}")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
