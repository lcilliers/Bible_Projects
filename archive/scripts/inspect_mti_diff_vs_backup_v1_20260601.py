"""Read-only diff of mti_terms (delete_flagged / exclusion_reason / cluster_code /
status) between the LIVE db and the 2026-05-28 backup (pre-today's term-writes).

Quantifies exactly what a surgical restore from the backup would revert, so the
reversal of today's flawed deletion streams can be judged before any write.

Read-only (ATTACH backup, compare in memory).
Output: research/investigations/mti-diff-vs-backup-20260601.md
  python scripts/inspect_mti_diff_vs_backup_v1_20260601.py
"""
import os
import sqlite3

DB = os.path.join("database", "bible_research.db")
BACKUP = os.path.join("backups", "bible_research_backup_20260528_065554_wa-cluster-M38-patch-borderline-resolution-v1-20260528.db")
OUT = os.path.join("research", "investigations", "mti-diff-vs-backup-20260601.md")
BACKFILL_REASON = "Bulk deleted, decision not recorded"


def load(path):
    c = sqlite3.connect(path, timeout=10)
    c.row_factory = sqlite3.Row
    d = {}
    for r in c.execute("SELECT id, COALESCE(delete_flagged,0) df, COALESCE(exclusion_reason,'') rsn, cluster_code, status FROM mti_terms"):
        d[r["id"]] = (r["df"], r["rsn"], r["cluster_code"], r["status"])
    c.close()
    return d


def main():
    if not os.path.exists(BACKUP):
        raise SystemExit(f"backup not found: {BACKUP}")
    live = load(DB)
    bak = load(BACKUP)

    df_flips_0to1 = []      # backfill/streamC newly deleted (was df=0, now df=1)
    df_flips_1to0 = []
    reason_added = []       # reason went '' -> backfill signature
    reason_other = []       # reason changed some other way
    cluster_changed = []    # cluster_code changed (e.g. F->FLAG)
    only_in_live = 0
    for tid, lv in live.items():
        bv = bak.get(tid)
        if bv is None:
            only_in_live += 1
            continue
        if lv[0] != bv[0]:
            (df_flips_0to1 if bv[0] == 0 and lv[0] == 1 else df_flips_1to0).append(tid)
        if lv[1] != bv[1]:
            if bv[1] == "" and lv[1] == BACKFILL_REASON:
                reason_added.append(tid)
            else:
                reason_other.append(tid)
        if lv[2] != bv[2]:
            cluster_changed.append(tid)

    # of the backfill-reason rows, how many were df=0 in the backup (newly deleted by me)?
    bf_was_live = [t for t in reason_added if bak[t][0] == 0]

    L = ["# mti_terms diff — live vs 2026-05-28 backup (pre-today)", "",
         f"**Backup:** `{os.path.basename(BACKUP)}`", "",
         f"- rows with `delete_flagged` flipped 0→1 today: **{len(df_flips_0to1)}**",
         f"- rows with `delete_flagged` flipped 1→0 today: {len(df_flips_1to0)}",
         f"- rows where `exclusion_reason` set to backfill signature ('{BACKFILL_REASON}'): **{len(reason_added)}**",
         f"   - of those, were df=0 (NOT deleted) in backup → newly deleted by the backfill: **{len(bf_was_live)}**",
         f"- rows with some other `exclusion_reason` change: {len(reason_other)}",
         f"- rows with `cluster_code` change (e.g. F→FLAG): {len(cluster_changed)}",
         f"- rows present in live but not backup: {only_in_live}", "",
         "A surgical restore = copy (delete_flagged, exclusion_reason) from backup back into live "
         "for the affected rows, re-validate the evidence guard on the term_id link, then redo correctly.",
         "F→FLAG (cluster_code) can be preserved (non-destructive, wanted)." ]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"df 0->1: {len(df_flips_0to1)} | reason->backfill: {len(reason_added)} (of which were live in backup: {len(bf_was_live)}) | cluster changed: {len(cluster_changed)} | other-reason: {len(reason_other)}")
    print(f"wrote: {OUT}")


if __name__ == "__main__":
    main()
