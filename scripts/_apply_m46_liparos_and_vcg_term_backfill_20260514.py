"""Fix-up for M46 — two operations in a single transaction:

  1. INSERT mti_term_subgroup row: G3045 liparos (mti=4702) → M46-A.
  2. Backfill vcg_term rows for the 22 new VCGs from the VCG patch from reading
     (group_code → mti_term_id via the term-prefix convention).

The original VCG patch apply script INSERTed verse_context_group rows but did
not create the vcg_term linkage that cluster-side joins (§4.4 of comprehensive,
grouped report) use. v1_13 §10.4 specifies vcg_term inserts for every NEW VCG
(post-M47). The convention applies whether the VCGs come from a Phase 7
directive or a structural VCG-creation patch.
"""
from __future__ import annotations
import argparse, os, shutil, sqlite3, sys
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = "database/bible_research.db"
BACKUP_DIR = "backups"
LABEL = "M46_LIPAROS_AND_VCG_TERM_BACKFILL_20260514"

LIPAROS_MTI = 4702
M46_A_CODE = "M46-A"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    ts = now_iso()

    print("=" * 72)
    print(f"  M46 liparos placement + vcg_term backfill")
    print(f"  Mode: {'LIVE' if args.live else 'DRY-RUN'}")
    print("=" * 72)

    # ── PRE-FLIGHT ────────────────────────────────────────────────────────
    print("\nPRE-FLIGHT")
    print("-" * 72)
    ok = True

    # Op 1 — liparos
    r = conn.execute(
        "SELECT id, strongs_number, transliteration, cluster_code "
        "FROM mti_terms WHERE id=?", (LIPAROS_MTI,)
    ).fetchone()
    if not r or r["strongs_number"] != "G3045" or r["cluster_code"] != "M46":
        print(f"  ✗ liparos mti={LIPAROS_MTI} pre-state mismatch: {dict(r) if r else None}"); ok = False
    else:
        print(f"  ✓ liparos mti=4702 G3045 in M46")
    sg = conn.execute(
        "SELECT id FROM cluster_subgroup WHERE cluster_code='M46' "
        "AND subgroup_code=? AND COALESCE(delete_flagged,0)=0", (M46_A_CODE,)
    ).fetchone()
    if not sg:
        print(f"  ✗ M46-A sub-group not found"); ok = False
    else:
        M46_A_ID = sg["id"]
        print(f"  ✓ M46-A id={M46_A_ID}")
    n_existing = conn.execute(
        "SELECT COUNT(*) FROM mti_term_subgroup "
        "WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (LIPAROS_MTI,)
    ).fetchone()[0]
    if n_existing:
        print(f"  ⚠ liparos already has {n_existing} placement(s); will skip if (mti, sg) collides")

    # Op 2 — gather new VCGs needing vcg_term backfill
    # Find M46-term VCGs that have no vcg_term row (or only deleted ones)
    new_vcgs = list(conn.execute("""
        SELECT vcg.id AS vcg_id, vcg.group_code, mt.id AS mti_id,
               mt.strongs_number, mt.transliteration
          FROM verse_context_group vcg
          JOIN mti_terms mt
            ON vcg.group_code LIKE mt.id || '-%'
           AND mt.cluster_code='M46'
           AND COALESCE(mt.delete_flagged,0)=0
         WHERE COALESCE(vcg.delete_flagged,0)=0
           AND NOT EXISTS (
             SELECT 1 FROM vcg_term vt
              WHERE vt.vcg_id=vcg.id AND vt.mti_term_id=mt.id
                AND COALESCE(vt.delete_flagged,0)=0
           )
         ORDER BY vcg.id
    """))
    print(f"\n  M46-term VCGs missing vcg_term linkage: {len(new_vcgs)}")
    for r in new_vcgs:
        print(f"    vcg_id={r['vcg_id']:<5} {r['group_code']:<10} → mti={r['mti_id']} ({r['strongs_number']})")

    if not ok:
        print("\nPRE-FLIGHT FAILED")
        return 1

    if not args.live:
        print("\n[DRY-RUN] no changes. Re-run with --live.")
        return 0

    # ── LIVE APPLY ────────────────────────────────────────────────────────
    os.makedirs(BACKUP_DIR, exist_ok=True)
    bp = os.path.join(BACKUP_DIR,
                      f"bible_research_pre_m46_liparos_vcg_term_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
    shutil.copy2(DB, bp)
    print(f"\nBackup: {bp}\n")

    try:
        conn.execute("BEGIN")
        cur = conn.cursor()

        # Op 1 — liparos placement
        cur.execute(
            "INSERT INTO mti_term_subgroup "
            "  (mti_term_id, cluster_subgroup_id, placement_note, "
            "   delete_flagged, created_at, last_updated_date) "
            "VALUES (?, ?, ?, 0, ?, ?)",
            (LIPAROS_MTI, M46_A_ID,
             f"{LABEL}: G3045 liparos → M46-A. Rev 18:14 (only verse) — "
             f"soul oriented toward material luxury fits M46-A inner closure register.",
             ts, ts)
        )
        print(f"  ✓ INSERTED mti_term_subgroup: liparos (4702) → M46-A id=mts_id={cur.lastrowid}")

        # Op 2 — vcg_term backfill
        n_inserted = 0
        for r in new_vcgs:
            cur.execute(
                "INSERT INTO vcg_term "
                "  (vcg_id, mti_term_id, placement_note, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, ?, ?)",
                (r["vcg_id"], r["mti_id"],
                 f"{LABEL}: linkage backfill for VCG created by "
                 f"WA-M46-patch-vcg-from-reading-v1-20260514",
                 ts, ts)
            )
            n_inserted += 1
        print(f"  ✓ INSERTED {n_inserted} vcg_term linkage rows")

        # FK check + commit
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    # ── VERIFICATION ──────────────────────────────────────────────────────
    print("\nVERIFICATION")
    print("-" * 72)

    # liparos placement
    r = conn.execute("""
        SELECT cs.subgroup_code, mts.placement_note
          FROM mti_term_subgroup mts
          JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
         WHERE mts.mti_term_id=4702 AND COALESCE(mts.delete_flagged,0)=0
    """).fetchone()
    print(f"  liparos placement: {r['subgroup_code'] if r else 'MISSING'}")

    # M46-term VCGs with vcg_term
    n_linked = conn.execute("""
        SELECT COUNT(DISTINCT vcg.id) FROM verse_context_group vcg
          JOIN vcg_term vt ON vt.vcg_id=vcg.id AND COALESCE(vt.delete_flagged,0)=0
          JOIN mti_terms mt ON mt.id=vt.mti_term_id
         WHERE mt.cluster_code='M46' AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(vcg.delete_flagged,0)=0
    """).fetchone()[0]
    n_total = conn.execute("""
        SELECT COUNT(*) FROM verse_context_group vcg
         WHERE COALESCE(vcg.delete_flagged,0)=0
           AND EXISTS (SELECT 1 FROM mti_terms mt
                        WHERE mt.cluster_code='M46'
                          AND COALESCE(mt.delete_flagged,0)=0
                          AND vcg.group_code LIKE mt.id || '-%')
    """).fetchone()[0]
    print(f"  M46-term VCGs total: {n_total}")
    print(f"  M46-term VCGs with vcg_term linkage: {n_linked}")

    # M46 sub-group placement counts (should be 22 = 21 + liparos)
    n_pl = conn.execute("""
        SELECT COUNT(*) FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id=mts.mti_term_id
         WHERE mt.cluster_code='M46' AND COALESCE(mts.delete_flagged,0)=0
    """).fetchone()[0]
    print(f"  M46 mti_term_subgroup rows total: {n_pl} (expected 22)")

    conn.close()
    print(f"\n[LIVE] M46 fix-up applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
