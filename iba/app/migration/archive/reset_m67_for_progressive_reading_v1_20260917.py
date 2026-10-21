"""One-off reset: clears `M67`'s verse-reading and char-subgroup output, produced by the OLD
isolated-design mechanism, so it can be redone under the new progressive/relational design
(#1723). Researcher instruction, verbatim, this chat turn: "we must now first work through the
list and reset the verse-reading. I will review the results again thereafter."

`ib_observation`/`ib_node` have no soft-delete mechanism (append-only by design, no `deleted`
column, no 'superseded' status value registered) -- this is a genuine, explicit "throw away and
redo" of data produced by a mechanism the researcher has since corrected, not routine supersession.
Backed up first (see BUILD.md entry for the backup filename). Hard-deletes:

- `M67`'s `stage='verse-reading'` ib_observation rows and their ib_node children (203 rows produced
  under the old per-cluster-isolated design, before the front-loading/relational rework).
- `M67`'s `stage='char-subgroup'` ib_observation rows (the 4 observations from Stage 2's redo,
  since Stage 2 read `M67`'s OLD verse-reading output as its own input -- now stale).
- `M67`'s `cluster_subgroup`/`cluster_subgroup_strong` rows (Stage 2's own subgroup allocation,
  same staleness reason).

Reverts `cluster.status` for `M67` back to `t_cluster_assignment_completed` (ordinal 2) so the
whole pipeline re-progresses cleanly: fresh verse-reading -> auto-advance to
`ready_for_subgroup_allocation` -> fresh subgroup allocation off the new verse-reading data.

NOT idempotent past first run in the normal sense (nothing to reset a second time) -- checks live
state first and reports what it would do; safe to re-run (no-ops once clean).

Usage:
    python iba/app/migration/reset_m67_for_progressive_reading_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import datetime
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
CLUSTER_CODE = "M67"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    vr_obs_ids = [r["id"] for r in conn.execute(
        "SELECT id FROM ib_observation WHERE cluster_code=? AND stage='verse-reading'",
        (CLUSTER_CODE,))]
    cs_obs_ids = [r["id"] for r in conn.execute(
        "SELECT id FROM ib_observation WHERE cluster_code=? AND stage='char-subgroup'",
        (CLUSTER_CODE,))]
    n_subgroups = conn.execute(
        "SELECT COUNT(*) n FROM cluster_subgroup WHERE cluster_code=? AND delete_flagged=0",
        (CLUSTER_CODE,)).fetchone()["n"]
    status = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER_CODE,)).fetchone()["status"]

    print(f"{CLUSTER_CODE}: {len(vr_obs_ids)} verse-reading observation(s), "
         f"{len(cs_obs_ids)} char-subgroup observation(s), {n_subgroups} live subgroup(s), "
         f"cluster.status={status!r}")

    if not vr_obs_ids and not cs_obs_ids and not n_subgroups and status == "t_cluster_assignment_completed":
        print("Already clean -- nothing to do.")
        conn.close()
        return 0

    if args.dry_run:
        print("--dry-run: would delete all of the above and reset cluster.status to ordinal 2.")
        conn.close()
        return 0

    all_obs_ids = vr_obs_ids + cs_obs_ids
    if all_obs_ids:
        ph = ",".join("?" * len(all_obs_ids))
        conn.execute(f"DELETE FROM ib_node WHERE observation_id IN ({ph})", all_obs_ids)
        conn.execute(f"DELETE FROM ib_observation WHERE id IN ({ph})", all_obs_ids)

    conn.execute(
        "DELETE FROM cluster_subgroup_strong WHERE cluster_subgroup_id IN "
        "(SELECT id FROM cluster_subgroup WHERE cluster_code=?)", (CLUSTER_CODE,))
    conn.execute("DELETE FROM cluster_subgroup WHERE cluster_code=?", (CLUSTER_CODE,))

    conn.execute(
        "UPDATE cluster SET status='t_cluster_assignment_completed', status_changed_at=? "
        "WHERE cluster_code=?", (now, CLUSTER_CODE))
    conn.commit()

    after_vr = conn.execute(
        "SELECT COUNT(*) n FROM ib_observation WHERE cluster_code=? AND stage='verse-reading'",
        (CLUSTER_CODE,)).fetchone()["n"]
    after_cs = conn.execute(
        "SELECT COUNT(*) n FROM ib_observation WHERE cluster_code=? AND stage='char-subgroup'",
        (CLUSTER_CODE,)).fetchone()["n"]
    after_sub = conn.execute(
        "SELECT COUNT(*) n FROM cluster_subgroup WHERE cluster_code=? AND delete_flagged=0",
        (CLUSTER_CODE,)).fetchone()["n"]
    after_status = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER_CODE,)).fetchone()["status"]
    print(f"After: verse-reading={after_vr}, char-subgroup={after_cs}, subgroups={after_sub}, "
         f"cluster.status={after_status!r}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
