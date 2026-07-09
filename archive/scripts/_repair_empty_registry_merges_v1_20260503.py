"""_repair_empty_registry_merges_v1_20260503.py

Marks three empty (zero-OWNER) registries as Excluded with merge audit trail:

  R137 resolve     -> R173 will       (resolve = settled will)
  R200 energy      -> R187 strength   (energy = inner-work language for strength)
  R214 suffering   -> R051 distress   (suffering is the umbrella; distress is the
                                       largest specific manifestation in cluster C05)

These registries have NO active OWNER terms and NO vc rows. The 'merge' is
therefore minimal: mark the empty registry as Excluded and record the merge
target. There is nothing structural to move.

The other 8 zero-OWNER registries (consciousness, diligence, loyalty, meekness,
recognition, reverence, sensuality, resentment) are NOT touched here — they
need researcher judgement.

Usage:
  python scripts/_repair_empty_registry_merges_v1_20260503.py            # dry-run
  python scripts/_repair_empty_registry_merges_v1_20260503.py --live     # apply
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
        "src_no": 137, "src_word": "resolve",
        "tgt_no": 173, "tgt_word": "will",
        "rationale": "resolve = settled will; conceptual umbrella is R173 will",
    },
    {
        "src_no": 200, "src_word": "energy",
        "tgt_no": 187, "tgt_word": "strength",
        "rationale": "energy is the inner-work language for what R187 strength studies",
    },
    {
        "src_no": 214, "src_word": "suffering",
        "tgt_no": 51,  "tgt_word": "distress",
        "rationale": "suffering is the umbrella for cluster C05; R051 distress is "
                     "the largest specific manifestation",
    },
]


def fetch_state(conn, no: int) -> dict:
    r = conn.execute("""
        SELECT no, word, phase1_status, session_b_status, verse_context_status,
               dim_review_status, inference_note, description
          FROM word_registry WHERE no = ?
    """, (no,)).fetchone()
    return dict(r) if r else None


def execute_one(conn, item: dict) -> dict:
    cur = conn.cursor()
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

    cur.execute("""
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
    return {"updated": cur.rowcount}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR,
                              f"bible_research_pre_empty_merges_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    print("--- BEFORE ---")
    for m in MERGES:
        s = fetch_state(conn, m["src_no"])
        print(f"  R{m['src_no']:03d} {m['src_word']:<10} phase1_status={s['phase1_status']!r}")
    print()

    print("--- Executing ---")
    conn.execute("BEGIN")
    for m in MERGES:
        result = execute_one(conn, m)
        print(f"  R{m['src_no']:03d} {m['src_word']} -> R{m['tgt_no']:03d} {m['tgt_word']}: "
              f"updated={result['updated']}")

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
        print(f"  R{m['src_no']:03d} {m['src_word']:<10} phase1_status={s['phase1_status']!r}")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
