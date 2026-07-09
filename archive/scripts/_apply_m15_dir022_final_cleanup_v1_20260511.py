"""_apply_m15_dir022_final_cleanup_v1_20260511.py — DB-modifying.

Apply DIR-20260511-M15-022: final M15 cleanup sweep.

Four passes:

  Pass A — Set-aside audit + normalisation
    Find all active M15 vc rows with set_aside_reason populated.
    Confirm uniform 'no_inner_being_phenomenon'. Normalise group_id=NULL,
    is_relevant=0, is_anchor=0 where they drift.

  Pass B — Orphan VCG soft-delete
    Soft-delete any verse_context_group linked to M15 terms that has zero
    active verse_context rows (catches anything missed by DIR-012, DIR-020).

  Pass C — Duplicate active vc rows
    Find any M15 verse_record_id with >1 active vc row. Keep the row with
    the lowest id (the primary); soft-delete the rest with an audit note.

  Pass D — Stray-item audit (read-only report; no writes)
    M15 vc rows with no group_id AND no set_aside_reason AND is_relevant=1
    (verses left in a sub-group but unassigned and not set aside).
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DIRECTIVE_ID = "DIR-20260511-M15-022"
CANONICAL_SETASIDE_REASON = "no_inner_being_phenomenon"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR,
                     f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"{DIRECTIVE_ID} apply (M15 final cleanup sweep)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # --- Pass A audit ---
    print("Pass A — Set-aside audit")
    print("-" * 72)
    sa_rows = list(conn.execute("""
        SELECT vc.id, vc.verse_record_id, mt.strongs_number, mt.transliteration,
               vc.set_aside_reason, vc.group_id, vc.is_relevant, vc.is_anchor,
               cs.subgroup_code
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
         WHERE mt.cluster_code = 'M15'
           AND COALESCE(vc.delete_flagged,0) = 0
           AND vc.set_aside_reason IS NOT NULL
    """))
    print(f"  Total M15 set-asides: {len(sa_rows)}")
    from collections import Counter
    reasons = Counter(r["set_aside_reason"] for r in sa_rows)
    print(f"  Reason distribution: {dict(reasons)}")
    drifted = [r for r in sa_rows
               if (r["group_id"] is not None
                   or r["is_relevant"] != 0
                   or r["is_anchor"] != 0)]
    non_canonical = [r for r in sa_rows
                     if r["set_aside_reason"] != CANONICAL_SETASIDE_REASON]
    print(f"  Drifted (group_id≠NULL or is_relevant=1 or is_anchor=1): "
          f"{len(drifted)}")
    print(f"  Non-canonical reason text: {len(non_canonical)}")

    # --- Pass B audit ---
    print()
    print("Pass B — Orphan VCG audit")
    print("-" * 72)
    orphans = list(conn.execute("""
        SELECT vcg.id, vcg.group_code,
               SUBSTR(vcg.context_description, 1, 60) AS d
          FROM verse_context_group vcg
         WHERE COALESCE(vcg.delete_flagged,0) = 0
           AND EXISTS (
                 SELECT 1 FROM vcg_term vt
                   JOIN mti_terms mt ON mt.id = vt.mti_term_id
                  WHERE vt.vcg_id = vcg.id
                    AND COALESCE(vt.delete_flagged,0) = 0
                    AND mt.cluster_code = 'M15'
               )
           AND NOT EXISTS (
                 SELECT 1 FROM verse_context vc
                  WHERE vc.group_id = vcg.id
                    AND COALESCE(vc.delete_flagged,0) = 0
               )
    """))
    print(f"  Empty active M15 VCGs: {len(orphans)}")
    for r in orphans[:10]:
        print(f"    {r['group_code']:18s} id={r['id']}  {r['d']}")
    if len(orphans) > 10:
        print(f"    ... and {len(orphans) - 10} more")

    # --- Pass C audit ---
    print()
    print("Pass C — Duplicate active vc audit")
    print("-" * 72)
    dups = list(conn.execute("""
        SELECT vr.id AS vr_id, vc.verse_record_id,
               COUNT(*) AS n_active,
               GROUP_CONCAT(vc.id || ':sg' || COALESCE(vc.cluster_subgroup_id,'∅')
                            || ':grp' || COALESCE(vc.group_id,'∅')) AS detail
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
         WHERE mt.cluster_code = 'M15'
           AND COALESCE(vc.delete_flagged,0) = 0
         GROUP BY vc.verse_record_id, vc.mti_term_id
        HAVING COUNT(*) > 1
    """))
    print(f"  vr_ids with >1 active vc row for same term: {len(dups)}")
    for r in dups:
        print(f"    vr_id={r['vr_id']}  n={r['n_active']}  {r['detail']}")

    # --- Pass D audit ---
    print()
    print("Pass D — Stray-item audit (read-only)")
    print("-" * 72)
    stray = list(conn.execute("""
        SELECT vc.id, vc.verse_record_id, vr.reference,
               mt.strongs_number, mt.transliteration,
               cs.subgroup_code, vc.is_relevant
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
          LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
         WHERE mt.cluster_code = 'M15'
           AND COALESCE(vc.delete_flagged,0) = 0
           AND vc.group_id IS NULL
           AND vc.set_aside_reason IS NULL
           AND vc.is_relevant = 1
        ORDER BY cs.subgroup_code, mt.strongs_number
    """))
    print(f"  Stray vc rows (M15, no group, no set-aside, relevant): {len(stray)}")
    if stray:
        from collections import Counter
        by_sg = Counter(r["subgroup_code"] for r in stray)
        for sg, n in sorted(by_sg.items()):
            print(f"    {sg or '(no sg)':12s}  {n}")
        print(f"  Sample:")
        for r in stray[:10]:
            print(f"    vc_id={r['id']} {r['reference']:>15s} "
                  f"{r['strongs_number']:>8s} {r['transliteration']:<15s} "
                  f"sg={r['subgroup_code']}")

    print()
    if args.live:
        b = take_backup("m15_dir022_final_cleanup")
        print(f"Backup: {b}")
        print()

    counts = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()

        # Pass A — normalise drifted set-asides
        print("APPLY")
        print("-" * 72)
        rc_normalised = 0
        for r in drifted:
            rc_normalised += cur.execute(
                "UPDATE verse_context "
                "   SET group_id = NULL, "
                "       is_relevant = 0, "
                "       is_anchor = 0, "
                "       notes = COALESCE(notes || ' | ', '') || ? "
                " WHERE id = ?",
                (f"{DIRECTIVE_ID}: normalised drifted set-aside", r["id"]),
            ).rowcount
        counts["pass_a_setasides_normalised"] = rc_normalised
        # Normalise non-canonical reason text (preserve original in notes)
        rc_reasoned = 0
        for r in non_canonical:
            rc_reasoned += cur.execute(
                "UPDATE verse_context "
                "   SET set_aside_reason = ?, "
                "       notes = COALESCE(notes || ' | ', '') || ? "
                " WHERE id = ?",
                (CANONICAL_SETASIDE_REASON,
                 f"{DIRECTIVE_ID}: reason normalised from "
                 f"{r['set_aside_reason']!r}",
                 r["id"]),
            ).rowcount
        counts["pass_a_reasons_normalised"] = rc_reasoned
        print(f"  Pass A: {rc_normalised} drifted set-asides normalised, "
              f"{rc_reasoned} reasons normalised")

        # Pass B — soft-delete orphans
        rc_vcg = 0
        rc_vt = 0
        if orphans:
            orphan_ids = [r["id"] for r in orphans]
            ph = ",".join("?" * len(orphan_ids))
            rc_vcg = cur.execute(
                f"UPDATE verse_context_group "
                f"   SET delete_flagged = 1, "
                f"       notes = COALESCE(notes || ' | ', '') || ? "
                f" WHERE id IN ({ph}) "
                f"   AND COALESCE(delete_flagged,0) = 0",
                [f"{DIRECTIVE_ID}: orphan soft-delete (final sweep)"]
                + orphan_ids,
            ).rowcount
            rc_vt = cur.execute(
                f"UPDATE vcg_term "
                f"   SET delete_flagged = 1, "
                f"       last_updated_date = ? "
                f" WHERE vcg_id IN ({ph}) "
                f"   AND COALESCE(delete_flagged,0) = 0",
                [ts] + orphan_ids,
            ).rowcount
        counts["pass_b_orphan_vcgs_soft_deleted"] = rc_vcg
        counts["pass_b_vcg_term_soft_deleted"] = rc_vt
        print(f"  Pass B: {rc_vcg} orphan VCGs soft-deleted, "
              f"{rc_vt} vcg_term rows soft-deleted")

        # Pass C — soft-delete duplicate vc rows
        rc_dups = 0
        for d in dups:
            rows = list(conn.execute("""
                SELECT id FROM verse_context
                 WHERE verse_record_id=? AND COALESCE(delete_flagged,0)=0
                 ORDER BY id ASC
            """, (d["verse_record_id"],)))
            for extra in rows[1:]:  # keep first; soft-delete the rest
                cur.execute(
                    "UPDATE verse_context "
                    "   SET delete_flagged = 1, "
                    "       notes = COALESCE(notes || ' | ', '') || ? "
                    " WHERE id = ?",
                    (f"{DIRECTIVE_ID}: duplicate active vc row for vr_id "
                     f"{d['verse_record_id']} — soft-deleted (primary kept "
                     f"as vc_id {rows[0]['id']})", extra["id"]),
                )
                rc_dups += 1
        counts["pass_c_duplicate_vc_rows_soft_deleted"] = rc_dups
        print(f"  Pass C: {rc_dups} duplicate vc rows soft-deleted")

        # Pass D is read-only; just report
        counts["pass_d_stray_vc_rows_reported"] = len(stray)
        print(f"  Pass D: {len(stray)} stray rows reported (no writes)")

        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}; sample: {fkv[:3]}")
        print()
        print("FK check: ok")

        # Verification — re-audit
        print()
        print("VERIFICATION (post-apply audits)")
        print("-" * 72)
        n_drifted = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
              JOIN mti_terms mt ON mt.id = vc.mti_term_id
             WHERE mt.cluster_code = 'M15'
               AND COALESCE(vc.delete_flagged,0) = 0
               AND vc.set_aside_reason IS NOT NULL
               AND (vc.group_id IS NOT NULL OR vc.is_relevant != 0
                    OR vc.is_anchor != 0)
        """).fetchone()[0]
        n_noncanon = conn.execute("""
            SELECT COUNT(*) FROM verse_context vc
              JOIN mti_terms mt ON mt.id = vc.mti_term_id
             WHERE mt.cluster_code = 'M15'
               AND COALESCE(vc.delete_flagged,0) = 0
               AND vc.set_aside_reason IS NOT NULL
               AND vc.set_aside_reason != ?
        """, (CANONICAL_SETASIDE_REASON,)).fetchone()[0]
        n_orphans = conn.execute("""
            SELECT COUNT(*) FROM verse_context_group vcg
             WHERE COALESCE(vcg.delete_flagged,0) = 0
               AND EXISTS (SELECT 1 FROM vcg_term vt
                            JOIN mti_terms mt ON mt.id = vt.mti_term_id
                           WHERE vt.vcg_id = vcg.id
                             AND COALESCE(vt.delete_flagged,0) = 0
                             AND mt.cluster_code = 'M15')
               AND NOT EXISTS (SELECT 1 FROM verse_context vc
                                WHERE vc.group_id = vcg.id
                                  AND COALESCE(vc.delete_flagged,0) = 0)
        """).fetchone()[0]
        n_dups = conn.execute("""
            SELECT COUNT(*) FROM (
                SELECT vc.verse_record_id
                  FROM verse_context vc
                  JOIN mti_terms mt ON mt.id = vc.mti_term_id
                 WHERE mt.cluster_code = 'M15'
                   AND COALESCE(vc.delete_flagged,0) = 0
                 GROUP BY vc.verse_record_id, vc.mti_term_id
                HAVING COUNT(*) > 1
            )
        """).fetchone()[0]
        print(f"  Drifted set-asides:       {n_drifted} (expected 0)")
        print(f"  Non-canonical reasons:    {n_noncanon} (expected 0)")
        print(f"  Empty orphan VCGs:        {n_orphans} (expected 0)")
        print(f"  Duplicate active vc rows: {n_dups} (expected 0)")

        if args.dry_run:
            conn.execute("ROLLBACK")
            print("\nDRY-RUN: rolled back.")
        else:
            conn.execute("COMMIT")
            print("\nLIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:40s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
