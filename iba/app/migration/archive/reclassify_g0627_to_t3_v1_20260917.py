"""Reclassifies G0627 (apologia, 'defence'/'to clear oneself', 2Cor.7.11) from T2 (Supplementary,
a generic catch-all) to T3 (Operations) -- researcher instruction, verbatim, this chat turn: "to
clear must move to T3." Found live: examining 2Cor.7.11's 7-cluster collision (M67/M03/M02/M01/
M18x2/M26/M12), 'eagerness to clear' (the actual corrective ACT the other named states drive
toward) carried no operation tag at all, only the generic T2 bucket -- exactly the kind of
"missed opportunity" the researcher flagged: an operation word invisible to the T3-anchored
relational reading because it was never classified as one.

Soft-delete-and-insert, matching this schema's own convention (never edit a live cluster_strong
row in place, never hard-delete) -- same pattern #1714's own cluster fixes used.

Safe to re-run: idempotent.

Usage:
    python iba/app/migration/reclassify_g0627_to_t3_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    has_t3 = conn.execute(
        "SELECT 1 FROM cluster_strong WHERE strong='G0627' AND cluster_code='T3' AND deleted=0"
    ).fetchone()
    has_t2_live = conn.execute(
        "SELECT 1 FROM cluster_strong WHERE strong='G0627' AND cluster_code='T2' AND deleted=0"
    ).fetchone()

    print(f"G0627 currently: T2 live={bool(has_t2_live)}, T3 live={bool(has_t3)}")

    if has_t3 and not has_t2_live:
        print("Already reclassified -- nothing to do.")
        conn.close()
        return 0

    if args.dry_run:
        print("--dry-run: would soft-delete T2 row (if live) and insert a live T3 row.")
        conn.close()
        return 0

    if has_t2_live:
        conn.execute(
            "UPDATE cluster_strong SET deleted=1 WHERE strong='G0627' AND cluster_code='T2'")
    if not has_t3:
        # Matches #1598's own established T2->T3 reclassification rationale format.
        rationale = (
            "relocated T2->T3 2026-09-17 (researcher instruction, this chat turn: 'to clear "
            "must move to T3'). 'defence: to clear oneself' (apologia) -- genuine "
            "action/operation verb (the corrective act the other named states in 2Cor.7.11 "
            "drive toward), not characteristic-specific. Found examining that verse's 7-cluster "
            "collision -- an unclassified operation word invisible to the relational reading.")
        conn.execute(
            "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
            "rationale) VALUES ('G0627', 'T3', 'researcher-instruction', ?, 0, ?)",
            (now, rationale))
    conn.commit()

    after = conn.execute(
        "SELECT cluster_code, deleted FROM cluster_strong WHERE strong='G0627' ORDER BY cluster_code"
    ).fetchall()
    print("After:", [dict(r) for r in after])
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
