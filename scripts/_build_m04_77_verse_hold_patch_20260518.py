"""Build a HOLD patch for the 77 freshly-Pass-A'd M04 verses.

Researcher direction 2026-05-18: "put all of the 77 verses on hold and move on.
The effort to sort out these is not worth it at this stage. There is still
something hidden in the understanding of these verses, but it is beyond me at
the moment."

Implementation:
- Set is_relevant=0 (back to set-aside state for now)
- Preserve analysis_note (the fresh Pass A meaning is the analytical work
  preserved for future revisit)
- set_aside_reason = HOLD marker (queryable; distinguishes from final set-aside)
- Keep cluster_subgroup_id=NULL, group_id=NULL (no sub-group or VCG yet)
- notes records the audit trail

Output: Sessions/Patches/wa-cluster-M04-repair-77-verse-hold-v1-{date}.json
"""
from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUT = Path(f"Sessions/Patches/wa-cluster-M04-repair-77-verse-hold-v1-{TODAY}.json")

HOLD_REASON_PREFIX = "HOLD-PENDING-DEEPER-ANALYSIS"
HOLD_REASON = (
    "HOLD-PENDING-DEEPER-ANALYSIS (2026-05-18): Pass A meaning authored 2026-05-18 "
    "under v2_5 §1.1 scope; researcher disposition deferred per v2_5 §17.5 audit-fix. "
    "Verse demonstrates inner-being potential but requires deeper analysis (researcher: "
    "'there is still something hidden in the understanding of these verses, but it is "
    "beyond me at the moment'). Pass A meaning preserved in analysis_note. To be "
    "revisited in a future research pass; queryable by set_aside_reason LIKE "
    "'HOLD-PENDING-DEEPER-ANALYSIS%'."
)


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Identify the 77 — they're vc rows with the audit-fix RESCUE-reset note AND
    # is_relevant=1 + analysis_note now populated (post-Pass-A).
    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, mt.strongs_number, mt.transliteration, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = 'M04'
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.analysis_note IS NOT NULL
          AND vc.notes LIKE '%audit-fix v2_5%2026-05-18%'
        ORDER BY mt.strongs_number, vr.book_id, vr.chapter, vr.verse_num
        """
    ).fetchall()

    print(f"Verses to HOLD: {len(rows)}")

    operations = []
    for i, r in enumerate(rows, 1):
        operations.append({
            "op_id": f"OP-{i:05d}",
            "operation": "update",
            "table": "verse_context",
            "match": {"id": r["vc_id"]},
            "set": {
                "is_relevant": 0,
                "is_anchor": 0,
                "cluster_subgroup_id": None,
                "group_id": None,
                "set_aside_reason": HOLD_REASON,
                # analysis_note preserved deliberately — not in the set clause
                "notes": (
                    f"[audit-fix v2_5 HOLD 2026-05-18] {r['strongs_number']} {r['transliteration']} {r['reference']} — "
                    f"Pass A re-authored 2026-05-18; researcher deferred disposition. "
                    f"Original state: terse set-aside (physical_only/no_inner_being) suspected bulk-processing bias. "
                    f"Fresh Pass A meaning is in analysis_note for future review."
                ),
            },
            "description": f"HOLD {r['reference']} {r['strongs_number']} {r['transliteration']} (vc={r['vc_id']})",
        })

    patch = {
        "_patch_meta": {
            "patch_id": f"PATCH-{TODAY}-M04-REPAIR-77-VERSE-HOLD-V1",
            "registry_id": None,
            "produced_date": TODAY,
            "produced_by": "scripts/_build_m04_77_verse_hold_patch_20260518.py",
            "patch_type": "REPAIR",
            "cluster_code": "M04",
            "session_b_status": None,
            "governing_instruction": "wa-sessionb-cluster-instruction-v2_5-20260518 §17.5 (audit-fix; cluster.status unchanged)",
            "description": (
                "HOLD the 77 verses (75 tov reset + 2 restored-vr orphans) at researcher "
                "direction 2026-05-18: Pass A meanings preserved in analysis_note; "
                "verses returned to set-aside state with HOLD-PENDING-DEEPER-ANALYSIS "
                "reason. Findable by set_aside_reason LIKE 'HOLD-PENDING-DEEPER-ANALYSIS%'. "
                "Next: M04 retrofit Step 3 (create 6 new sub-groups + assign 69 register-"
                "family BOUNDARY verses) proceeds."
            ),
        },
        "_patch_summary": {
            "total_operations": len(operations),
            "produced_at_utc": NOW_UTC,
            "hold_reason_marker": HOLD_REASON_PREFIX,
        },
        "operations": operations,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Patch written: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
