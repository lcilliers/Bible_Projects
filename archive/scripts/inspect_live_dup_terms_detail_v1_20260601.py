"""Detail the 55 live-duplicate strongs: per live row, cluster + analytical attachments.

For each strongs with >1 live (delete_flagged=0) mti_terms row, list each live row's
id / cluster_code / owning_registry / status, and its attachments:
  - vc  = active verse_context rows (mti_term_id = this row id)
  - vcg = active vcg_term rows
  - sub = mti_term_subgroup rows
Summary: same-cluster vs different-cluster dups; attachments on both rows vs one.

Read-only. Output: research/investigations/live-dup-terms-detail-20260601.md
"""
import os
import sqlite3
from collections import defaultdict

DB = "database/bible_research.db"
OUT = "research/investigations/live-dup-terms-detail-20260601.md"


def main():
    c = sqlite3.connect(DB, timeout=20); c.row_factory = sqlite3.Row
    cur = c.cursor()

    live = defaultdict(list)
    for r in cur.execute("SELECT id, strongs_number sn, transliteration tr, gloss, cluster_code cc, owning_registry reg, COALESCE(status,'') st FROM mti_terms WHERE COALESCE(delete_flagged,0)=0"):
        live[r["sn"]].append(r)
    dups = {sn: rows for sn, rows in live.items() if len(rows) > 1}

    def vc(tid):
        return cur.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
    def vcg(tid):
        return cur.execute("SELECT COUNT(*) FROM vcg_term WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
    def sub(tid):
        return cur.execute("SELECT COUNT(*) FROM mti_term_subgroup WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]

    same_cluster = diff_cluster = 0
    attach_both = attach_one = attach_none = 0
    L = [f"# Live-duplicate terms ({len(dups)}) — per-row cluster + attachments", "",
         "**Generated:** 2026-06-01 (read-only). 'attachments' per row: vc=active verse_context, vcg=active vcg_term, sub=mti_term_subgroup. cluster_finding is per-cluster/characteristic, not per-term-row, so term-level findings = verse_context.", "",
         "| strongs | translit | row id | cluster | reg | status | vc | vcg | sub |", "|---|---|---|---|---|---|--:|--:|--:|"]
    for sn in sorted(dups):
        rows = dups[sn]
        clusters = {r["cc"] for r in rows}
        if len(clusters) == 1:
            same_cluster += 1
        else:
            diff_cluster += 1
        attach_counts = []
        for r in rows:
            v, g, s = vc(r["id"]), vcg(r["id"]), sub(r["id"])
            attach_counts.append(v + g + s)
            L.append(f"| {sn} | {(r['tr'] or '')[:14]} | {r['id']} | {r['cc']} | {r['reg']} | {r['st']} | {v} | {g} | {s} |")
        n_attached = sum(1 for x in attach_counts if x > 0)
        if n_attached >= 2:
            attach_both += 1
        elif n_attached == 1:
            attach_one += 1
        else:
            attach_none += 1

    summary = [f"\n## Summary ({len(dups)} live-dup strongs)",
               f"- both/all rows in the **same cluster**: {same_cluster}",
               f"- rows in **different clusters**: {diff_cluster}",
               f"- **attachments on >=2 rows** (merge must repoint both): {attach_both}",
               f"- attachments on exactly 1 row (other row is an empty dup): {attach_one}",
               f"- attachments on no row: {attach_none}"]
    L = L[:4] + summary + [""] + L[4:]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"live-dup strongs: {len(dups)} | same-cluster: {same_cluster} | diff-cluster: {diff_cluster}")
    print(f"attachments: both>=2 rows={attach_both} | one row={attach_one} | none={attach_none}")
    print("wrote:", OUT)
    c.close()


if __name__ == "__main__":
    main()
