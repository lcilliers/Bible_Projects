"""Pre-patch update: move G3045 liparos (mti=4702) from M46-A to M46-B.

AI's M46 Phase 7 reading (WA-M46-patch-phase7-routing-v1-20260515.json) routes
Rev 18:14 — liparos's only verse — to M46-B (insatiability/deceitfulness face,
gid=3709). Yesterday's backfill script placed the term in M46-A as a snap
decision; this script realigns the term-level placement to match AI's reading.

Mechanism: UPDATE mti_term_subgroup row 381 (mti_term_id=4702) — change
cluster_subgroup_id from 45 (M46-A) to 46 (M46-B). Preserves all other fields.

Idempotent: only updates if currently in M46-A.

Usage: python scripts/_apply_m46_liparos_subgroup_move_20260515.py [--dry-run]
"""
import sqlite3
import sys
from pathlib import Path
from datetime import datetime, timezone

DB = Path(__file__).resolve().parent.parent / "database" / "bible_research.db"

LIPAROS_MTI = 4702
M46_A_ID = 45
M46_B_ID = 46
PLACEMENT_NOTE_APPEND = (
    " | 20260515 CC realignment: moved M46-A -> M46-B to align with AI's Phase 7 reading "
    "(WA-M46-patch-phase7-routing-v1-20260515) — Rev 18:14 routes to M46-B "
    "(insatiability/deceitfulness face, gid=3709). Single-verse term: term placement "
    "must match the verse routing for R4 anchor integrity."
)


def main():
    dry_run = "--dry-run" in sys.argv
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    row = conn.execute("""
SELECT mts.id, mts.mti_term_id, mts.cluster_subgroup_id, mts.placement_note,
       cs.subgroup_code AS cur_code
FROM mti_term_subgroup mts
LEFT JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
WHERE mts.mti_term_id = ? AND COALESCE(mts.delete_flagged,0)=0
""", (LIPAROS_MTI,)).fetchone()

    if not row:
        print("ERROR: no mti_term_subgroup row found for G3045 liparos (mti=4702).")
        sys.exit(1)

    print(f"Current: row id={row['id']}  cluster_subgroup_id={row['cluster_subgroup_id']} ({row['cur_code']})")
    print(f"         placement_note: {row['placement_note']}")

    if row["cluster_subgroup_id"] == M46_B_ID:
        print("Already in M46-B. No change.")
        return

    if row["cluster_subgroup_id"] != M46_A_ID:
        print(f"ERROR: expected current subgroup M46-A (id={M46_A_ID}); got {row['cur_code']} (id={row['cluster_subgroup_id']}).")
        print("Aborting — please investigate manually before re-running.")
        sys.exit(1)

    new_note = (row["placement_note"] or "") + PLACEMENT_NOTE_APPEND
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"\nProposed UPDATE: cluster_subgroup_id {M46_A_ID} -> {M46_B_ID}, last_updated_date -> {now}")
    print(f"New placement_note: {new_note}")

    if dry_run:
        print("\n[DRY RUN] No write performed.")
        return

    conn.execute(
        """UPDATE mti_term_subgroup
        SET cluster_subgroup_id = ?, placement_note = ?, last_updated_date = ?
        WHERE id = ?""",
        (M46_B_ID, new_note, now, row["id"])
    )
    conn.commit()
    print("\nUPDATE applied.")

    # Verify
    after = conn.execute("""
SELECT mts.cluster_subgroup_id, cs.subgroup_code
FROM mti_term_subgroup mts
JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
WHERE mts.id = ?
""", (row["id"],)).fetchone()
    print(f"Verified: row id={row['id']} now in subgroup_code={after['subgroup_code']} (id={after['cluster_subgroup_id']}).")


if __name__ == "__main__":
    main()
