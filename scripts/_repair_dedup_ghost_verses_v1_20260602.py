"""Repair dedup-ghost verse_context rows (programme-wide).

A dedup pass soft-deleted duplicate wa_verse_records but did NOT re-point the
verse_context rows that referenced the removed copy. Result: active vc rows hang off a
deleted verse-record (vr.delete_flagged=1) — invisible to Pass A, miscounted by the audit.

For each active vc row (active term) whose verse-record is deleted:
  - find the surviving ACTIVE record for the same book/chapter/verse:
      * exists, and the term has NO active vc on it yet  -> RE-POINT verse_record_id (identity-preserving)
      * exists, but the term ALREADY has an active vc on it -> orphan is a duplicate -> SOFT-DELETE the orphan
      * does not exist (verse genuinely gone)               -> SOFT-DELETE the orphan
RESET-IF-COMPLETE: a SOFT-DELETE (not a re-point) is a material verse change; if it
touches an 'Analysis Complete' cluster, reset that cluster to 'Ready for re-analysis'
(verse-change -> revalidation principle, researcher 2026-06-02). Re-points are
identity-preserving and never reset.

DEFAULT DRY-RUN. --apply to write.
  python scripts/_repair_dedup_ghost_verses_v1_20260602.py [--cluster CODE] [--apply]
"""
import argparse, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DB = "database/bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", default=None)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    c = sqlite3.connect(DB, timeout=60); c.row_factory = sqlite3.Row
    cur = c.cursor()

    where = "AND mt.cluster_code=?" if a.cluster else ""
    params = (a.cluster,) if a.cluster else ()
    orphans = cur.execute(f"""
        SELECT vc.id vcid, vc.mti_term_id, mt.cluster_code, vr.book_id, vr.chapter, vr.verse_num, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id=vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        WHERE COALESCE(vc.delete_flagged,0)=0 AND COALESCE(mt.delete_flagged,0)=0 AND vr.delete_flagged=1 {where}
    """, params).fetchall()

    plan = {"repoint": [], "dup_delete": [], "gone_delete": []}
    for o in orphans:
        active = cur.execute("SELECT id FROM wa_verse_records WHERE book_id=? AND chapter=? AND verse_num=? AND COALESCE(delete_flagged,0)=0 ORDER BY id",
                             (o["book_id"], o["chapter"], o["verse_num"])).fetchone()
        if not active:
            plan["gone_delete"].append(o); continue
        # does this term already have an active vc on the surviving record?
        exists = cur.execute("SELECT 1 FROM verse_context WHERE mti_term_id=? AND verse_record_id=? AND COALESCE(delete_flagged,0)=0",
                             (o["mti_term_id"], active["id"])).fetchone()
        if exists:
            plan["dup_delete"].append((o, active["id"]))
        else:
            plan["repoint"].append((o, active["id"]))

    by_cl = defaultdict(lambda: [0, 0, 0])  # cluster -> [repoint, dup_delete, gone_delete]
    for o, _ in plan["repoint"]: by_cl[o["cluster_code"]][0] += 1
    for o, _ in plan["dup_delete"]: by_cl[o["cluster_code"]][1] += 1
    for o in plan["gone_delete"]: by_cl[o["cluster_code"]][2] += 1

    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: orphans={len(orphans)} | "
          f"repoint={len(plan['repoint'])} dup_delete={len(plan['dup_delete'])} gone_delete={len(plan['gone_delete'])}")
    for cl in sorted(by_cl, key=lambda x: x or ""):
        rp, dd, gd = by_cl[cl]
        st = cur.execute("SELECT status FROM cluster WHERE cluster_code=?", (cl,)).fetchone()
        print(f"  {cl} [{st[0] if st else '?'}]: repoint {rp}, dup_delete {dd}, gone_delete {gd}")

    if not a.apply:
        c.close(); return

    cur.execute("BEGIN")
    try:
        for o, newvr in plan["repoint"]:
            cur.execute("UPDATE verse_context SET verse_record_id=? WHERE id=?", (newvr, o["vcid"]))
        for o, _ in plan["dup_delete"]:
            cur.execute("UPDATE verse_context SET delete_flagged=1, set_aside_reason=? WHERE id=?",
                        ("dedup-ghost: duplicate of an active vc on the surviving verse-record", o["vcid"]))
        for o in plan["gone_delete"]:
            cur.execute("UPDATE verse_context SET delete_flagged=1, set_aside_reason=? WHERE id=?",
                        ("dedup-ghost: verse-record deleted with no surviving active record", o["vcid"]))
        # reset-if-complete: clusters touched by a DELETE (material change) that are Analysis Complete
        deleted_clusters = {o["cluster_code"] for o, _ in plan["dup_delete"]} | {o["cluster_code"] for o in plan["gone_delete"]}
        reset = []
        for cl in sorted(c2 for c2 in deleted_clusters if c2):
            st = cur.execute("SELECT status FROM cluster WHERE cluster_code=?", (cl,)).fetchone()
            if st and st[0] == "Analysis Complete":
                cur.execute("UPDATE cluster SET status='Ready for re-analysis', last_updated_date=? WHERE cluster_code=?", (NOW, cl))
                reset.append(cl)
        c.commit()
    except Exception:
        c.rollback(); raise
    print(f"APPLIED: repointed {len(plan['repoint'])}, dup-deleted {len(plan['dup_delete'])}, gone-deleted {len(plan['gone_delete'])}.")
    if reset:
        print(f"RESET (Analysis Complete -> Ready for re-analysis, verse deletion): {reset}")
    c.close()


if __name__ == "__main__":
    main()
