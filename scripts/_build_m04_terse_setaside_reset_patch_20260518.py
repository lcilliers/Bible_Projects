"""Build a RESCUE-reset patch for M04's 75 terse set-asides (all H2896A tov).

Researcher direction 2026-05-18: "these verses must all be reset to UT and
re-introduced. meaning generated, and re-evaluated. it is clear that these 75
verses have simply been processed in bulk based on samples, they have not been
read individually."

Under the existing schema the UNIQUE constraint on verse_context applies
regardless of delete_flagged, so we cannot soft-delete + INSERT a fresh vc.
We reset the existing vc rows in place: clear set_aside_reason / analysis_note
/ sub-group / VCG / anchor; set is_relevant=1 to make Pass A pick them up.

After this patch + Pass A run, the 75 verses will have fresh per-verse
meanings authored individually. Researcher then reviews and decides each:
PROMOTE-TO-SUBGROUP, CONFIRM-SET-ASIDE-WITH-PROPER-REASON, or HOLD.

Output: Sessions/Patches/wa-cluster-M04-repair-terse-setaside-reset-v1-{date}.json
"""
from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUT = Path(f"Sessions/Patches/wa-cluster-M04-repair-terse-setaside-reset-v1-{TODAY}.json")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, vc.set_aside_reason, mt.strongs_number, mt.transliteration,
               vr.reference, vr.delete_flagged AS vr_del
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = 'M04'
          AND vc.is_relevant = 0
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.set_aside_reason IN ('physical_only', 'no_inner_being')
        ORDER BY vc.set_aside_reason, vr.book_id, vr.chapter, vr.verse_num
        """
    ).fetchall()

    if len(rows) != 75:
        print(f"WARNING: expected 75 terse set-asides, found {len(rows)}")

    # Check for any with deleted vr — those need vr restore as well
    needs_vr_restore = [r for r in rows if r["vr_del"]]
    if needs_vr_restore:
        print(f"NOTE: {len(needs_vr_restore)} of the 75 have vr.delete_flagged=1 — vr restore needed")

    operations = []
    op_idx = 1

    # First — restore any deleted vrs (so Pass A can read the verse text)
    seen_vr_restore = set()
    for r in rows:
        if r["vr_del"]:
            # Need vr_id; query it
            vr_id = conn.execute("SELECT verse_record_id FROM verse_context WHERE id=?", (r["vc_id"],)).fetchone()[0]
            if vr_id not in seen_vr_restore:
                operations.append({
                    "op_id": f"OP-{op_idx:05d}",
                    "operation": "update",
                    "table": "wa_verse_records",
                    "match": {"id": vr_id},
                    "set": {"delete_flagged": 0},
                    "description": f"Restore vr={vr_id} ({r['reference']}) so Pass A can read the verse text",
                })
                op_idx += 1
                seen_vr_restore.add(vr_id)

    # Then — reset the 75 vc rows
    for r in rows:
        operations.append({
            "op_id": f"OP-{op_idx:05d}",
            "operation": "update",
            "table": "verse_context",
            "match": {"id": r["vc_id"]},
            "set": {
                "is_relevant": 1,
                "is_anchor": 0,
                "set_aside_reason": None,
                "analysis_note": None,
                "cluster_subgroup_id": None,
                "group_id": None,
                "notes": (
                    f"[audit-fix v2_5 RESCUE-reset 2026-05-18] Original set_aside_reason='{r['set_aside_reason']}' "
                    f"was terse and possibly bulk-processed under bias. Reset for fresh individual Pass A reading "
                    f"under v2_5 §1.1 scope. Disposition (PROMOTE / SET-ASIDE-with-proper-reason / HOLD) "
                    f"to be decided per-verse after Pass A meaning is authored."
                ),
            },
            "description": (
                f"Reset vc={r['vc_id']} {r['reference']} {r['strongs_number']} {r['transliteration']} "
                f"(was is_relevant=0 with terse reason '{r['set_aside_reason']}'); now is_relevant=1 + analysis_note NULL for Pass A pickup"
            ),
        })
        op_idx += 1

    patch = {
        "_patch_meta": {
            "patch_id": f"PATCH-{TODAY}-M04-REPAIR-TERSE-SETASIDE-RESET-V1",
            "registry_id": None,
            "produced_date": TODAY,
            "produced_by": "scripts/_build_m04_terse_setaside_reset_patch_20260518.py",
            "patch_type": "REPAIR",
            "cluster_code": "M04",
            "session_b_status": None,
            "governing_instruction": "wa-sessionb-cluster-instruction-v2_5-20260518 §17.5 (audit-fix) + §18.2 RESCUE pattern; §1.1 scope",
            "description": (
                "Reset 75 terse set-asides (all H2896A tov, reasons 'physical_only' or "
                "'no_inner_being') so they re-enter the pipeline at Pass A for fresh "
                "per-verse reading. Researcher direction 2026-05-18: verses were bulk-"
                "processed under bias; require individual reading under v2_5 §1.1 full "
                "inner-being scope. After this patch + Pass A run, each verse will have "
                "a fresh authored meaning. Researcher then dispositions each "
                "(PROMOTE-TO-SUBGROUP / CONFIRM-SET-ASIDE-with-§4.5.1-reason / HOLD)."
            ),
        },
        "_patch_summary": {
            "total_operations": len(operations),
            "vr_restore_count": len(seen_vr_restore),
            "vc_reset_count": len(rows),
            "by_original_reason": {
                "physical_only": sum(1 for r in rows if r["set_aside_reason"] == "physical_only"),
                "no_inner_being": sum(1 for r in rows if r["set_aside_reason"] == "no_inner_being"),
            },
            "produced_at_utc": NOW_UTC,
        },
        "operations": operations,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Patch written: {OUT}")
    print(f"Operations: {len(operations)}")
    conn.close()


if __name__ == "__main__":
    main()
