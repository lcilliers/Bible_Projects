"""Build a REPAIR patch to soft-delete 15 stale orphan vc rows in M04.

Researcher-approved 2026-05-18: these are vc rows pointing to soft-deleted
wa_verse_records (delete_flagged=1) where a live sibling vc exists for the
same Bible reference + term and is fully processed (Pass A meaning + sub-
group + VCG). The orphan adds no analytical value; soft-delete it.

Excludes 4 special-case orphans handled by a separate patch:
- vc=23405 (Dan 1:10 gil)        — needs SET-ASIDE disposition + flag for M01
- vc=23418 (Ezr 6:16 ched.vah)   — restore vr + re-assign sub-group
- vc=28385 (2Sa 23:1 na.im)      — restore vr + Pass A author
- vc=28388 (Psa 81:2 na.im)      — SET-ASIDE with proper §4.5.1 reason

Output: Sessions/Patches/wa-cluster-M04-repair-stale-orphan-cleanup-v1-{date}.json
"""
from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUT = Path(f"Sessions/Patches/wa-cluster-M04-repair-stale-orphan-cleanup-v1-{TODAY}.json")

SPECIAL_CASE_VC_IDS = {23405, 23418, 28385, 28388}


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Find all M04 orphan vc rows (is_relevant=1, no analysis_note, vr.delete_flagged=1)
    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, vc.verse_record_id, vc.cluster_subgroup_id, vc.group_id,
               mt.strongs_number, mt.transliteration, vr.reference,
               cs.subgroup_code, vcg.group_code
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE mt.cluster_code = 'M04'
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vr.delete_flagged = 1
          AND vc.analysis_note IS NULL
        ORDER BY vr.book_id, vr.chapter, vr.verse_num, vc.id
        """
    ).fetchall()

    stale = [r for r in rows if r["vc_id"] not in SPECIAL_CASE_VC_IDS]
    specials = [r for r in rows if r["vc_id"] in SPECIAL_CASE_VC_IDS]

    print(f"Total orphan vc rows: {len(rows)}")
    print(f"Stale orphans (cleanup target): {len(stale)}")
    print(f"Special cases (excluded): {len(specials)}")
    if len(stale) != 15:
        print(f"WARNING: expected 15 stale orphans, found {len(stale)}")

    operations = []
    for i, r in enumerate(stale, start=1):
        # Find live sibling vc for the audit note
        live = conn.execute(
            """
            SELECT vc2.id, vr2.reference
            FROM verse_context vc2
            JOIN wa_verse_records vr2 ON vr2.id = vc2.verse_record_id
            WHERE vc2.mti_term_id = (SELECT mti_term_id FROM verse_context WHERE id = ?)
              AND vr2.book_id = (SELECT book_id FROM wa_verse_records WHERE id = (SELECT verse_record_id FROM verse_context WHERE id = ?))
              AND vr2.chapter = (SELECT chapter FROM wa_verse_records WHERE id = (SELECT verse_record_id FROM verse_context WHERE id = ?))
              AND vr2.verse_num = (SELECT verse_num FROM wa_verse_records WHERE id = (SELECT verse_record_id FROM verse_context WHERE id = ?))
              AND COALESCE(vr2.delete_flagged, 0) = 0
              AND COALESCE(vc2.delete_flagged, 0) = 0
              AND vc2.id != ?
            LIMIT 1
            """,
            (r["vc_id"], r["vc_id"], r["vc_id"], r["vc_id"], r["vc_id"]),
        ).fetchone()
        sibling_id = live["id"] if live else None
        note = (
            f"audit-fix v2_5 stale orphan cleanup ({TODAY}): "
            f"vr={r['verse_record_id']} delete_flagged=1; live sibling vc={sibling_id} "
            f"covers {r['reference']} {r['strongs_number']}. "
            f"Soft-deleted per researcher approval 2026-05-18 — orphan has no analytical content (analysis_note NULL)."
        )
        operations.append({
            "op_id": f"OP-{i:05d}",
            "operation": "update",
            "table": "verse_context",
            "match": {"id": r["vc_id"]},
            "set": {
                "delete_flagged": 1,
                "notes": note,
            },
            "description": (
                f"M04 stale orphan: vc={r['vc_id']} {r['reference']} "
                f"{r['strongs_number']} {r['transliteration']} "
                f"(was is_relevant=1 in {r['subgroup_code']} / {r['group_code']}; "
                f"vr={r['verse_record_id']} deleted; live sibling vc={sibling_id})"
            ),
        })

    patch = {
        "_patch_meta": {
            "patch_id": f"PATCH-{TODAY}-M04-REPAIR-STALE-ORPHAN-CLEANUP-V1",
            "registry_id": None,
            "produced_date": TODAY,
            "produced_by": "scripts/_build_m04_stale_orphan_cleanup_patch_20260518.py",
            "patch_type": "REPAIR",
            "cluster_code": "M04",
            "session_b_status": None,
            "governing_instruction": "wa-sessionb-cluster-instruction-v2_5-20260518 §17.5 (audit-fix; cluster.status unchanged)",
            "description": (
                "Audit-fix per v2_5 audit dated 2026-05-18 — M04 had 15 stale orphan verse_context "
                "rows pointing to soft-deleted wa_verse_records. Each orphan has a live sibling vc "
                "covering the same (Bible reference, term) pair, fully processed (Pass A + sub-group "
                "+ VCG). Soft-delete the 15 orphans to clean up the duplicate noise. 4 additional "
                "orphans (Dan 1:10, Ezr 6:16, 2Sa 23:1, Psa 81:2) require special-case dispositions "
                "and are handled by a separate patch — not included here."
            ),
        },
        "_patch_summary": {
            "total_operations": len(operations),
            "stale_orphan_count": len(stale),
            "special_cases_excluded": len(specials),
            "produced_at_utc": NOW_UTC,
        },
        "operations": operations,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nPatch written: {OUT}")
    print(f"Operations: {len(operations)}")
    conn.close()


if __name__ == "__main__":
    main()
