"""_repair_empty_registry_merges_batch2_v1_20260503.py

Second batch of empty-registry merges (researcher-directed 2026-05-03):

  R027 consciousness  -> R166 understanding   (consciousness = the awareness
                                              that understanding requires;
                                              both are C22)
  R129 recognition    -> R166 understanding   (recognition = the moment of
                                              understanding seeing clearly;
                                              both are C22)
  R048 diligence      -> R142 self-control    (diligence = the disciplined
                                              effort that self-control sustains)
  R144 sensuality     -> R086 impurity        (sensuality belongs to the
                                              impurity territory in C12)

Same minimal-merge pattern as batch 1 (resolve→will, energy→strength,
suffering→distress): these source registries are zero-OWNER zero-vc, so the
merge is a semantic mark only — phase1_status='Excluded' + audit trail.

Remaining empty registries (not in this batch): R104 loyalty, R109 meekness,
R138 reverence, R205 resentment.

Usage:
  python scripts/_repair_empty_registry_merges_batch2_v1_20260503.py
  python scripts/_repair_empty_registry_merges_batch2_v1_20260503.py --live
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
        "src_no": 27, "src_word": "consciousness",
        "tgt_no": 166, "tgt_word": "understanding",
        "rationale": "consciousness is the awareness that understanding requires; "
                     "both are in cluster C22",
    },
    {
        "src_no": 129, "src_word": "recognition",
        "tgt_no": 166, "tgt_word": "understanding",
        "rationale": "recognition is the moment of understanding seeing clearly; "
                     "both are in cluster C22",
    },
    {
        "src_no": 48, "src_word": "diligence",
        "tgt_no": 142, "tgt_word": "self-control",
        "rationale": "diligence is the disciplined effort that self-control sustains; "
                     "both are in cluster C08",
    },
    {
        "src_no": 144, "src_word": "sensuality",
        "tgt_no": 86, "tgt_word": "impurity",
        "rationale": "sensuality belongs to the impurity territory; "
                     "both are in cluster C12",
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
                              f"bible_research_pre_empty_merges_b2_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    print("--- Verifying targets exist and are not Excluded ---")
    for m in MERGES:
        t = fetch_state(conn, m["tgt_no"])
        s = fetch_state(conn, m["src_no"])
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
