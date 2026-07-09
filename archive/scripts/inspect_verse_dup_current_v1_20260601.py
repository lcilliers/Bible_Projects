"""Fresh, from-the-DB investigation of active duplicate verse rows (current state).

Re-counts active duplicate (term_id, reference) groups and examines what actually
differs between the duplicate rows — so any dedup recommendation rests on current
facts, not earlier notes.

Read-only. Output: research/investigations/verse-dup-current-20260601.md
"""
import os
import sqlite3
from collections import defaultdict, Counter

DB = "database/bible_research.db"
OUT = "research/investigations/verse-dup-current-20260601.md"


def main():
    c = sqlite3.connect(DB, timeout=30); c.row_factory = sqlite3.Row
    cur = c.cursor()

    # active duplicate (term_id, reference) groups, current DB
    groups = cur.execute("""
        SELECT term_id, reference, COUNT(*) n
        FROM wa_verse_records
        WHERE COALESCE(delete_flagged,0)=0 AND term_id IS NOT NULL AND reference IS NOT NULL
        GROUP BY term_id, reference HAVING COUNT(*)>1
    """).fetchall()
    extra = sum(r["n"] - 1 for r in groups)

    # pull the full rows for these groups to see what differs
    keys = {(r["term_id"], r["reference"]) for r in groups}
    same_mti = diff_mti = 0
    same_file = diff_file = 0
    both_have_vc = one_has_vc = none_has_vc = 0
    identical_rowfields = 0
    rowsby = defaultdict(list)
    for r in cur.execute("SELECT id, term_id, reference, file_id, term_inv_id, mti_term_id, target_word, span_strong_match FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 AND term_id IS NOT NULL AND reference IS NOT NULL"):
        if (r["term_id"], r["reference"]) in keys:
            rowsby[(r["term_id"], r["reference"])].append(r)

    def has_vc(vid):
        return cur.execute("SELECT COUNT(*) FROM verse_context WHERE verse_record_id=? AND COALESCE(delete_flagged,0)=0", (vid,)).fetchone()[0] > 0

    samples = []
    for k, rows in rowsby.items():
        mtis = {r["mti_term_id"] for r in rows}
        files = {r["file_id"] for r in rows}
        (same_mti if len(mtis) == 1 else diff_mti).__add__  # noqa (placeholder)
        if len(mtis) == 1:
            same_mti += 1
        else:
            diff_mti += 1
        if len(files) == 1:
            same_file += 1
        else:
            diff_file += 1
        vcflags = [has_vc(r["id"]) for r in rows]
        nvc = sum(1 for x in vcflags if x)
        if nvc >= 2:
            both_have_vc += 1
        elif nvc == 1:
            one_has_vc += 1
        else:
            none_has_vc += 1
        if len(samples) < 6:
            samples.append((k, rows, vcflags))

    L = [f"# Active duplicate verse rows — current DB (2026-06-01)", "",
         f"**Duplicate (term_id, reference) groups with >1 live row: {len(groups)}** | extra live rows: {extra}", "",
         "## What differs between the duplicate rows (per group)",
         f"- same `mti_term_id` across the dup rows: {same_mti} | different: {diff_mti}",
         f"- same `file_id` (same extraction): {same_file} | different (different registry pulled the verse): {diff_file}",
         f"- live `verse_context` on >=2 of the rows: **{both_have_vc}** | on exactly 1: {one_has_vc} | on none: {none_has_vc}", "",
         "## Sample groups (full row detail)", ""]
    for k, rows, vcflags in samples:
        L.append(f"### {k[0]} @ {k[1]} ({len(rows)} live rows)")
        L.append("| id | file_id | term_inv_id | mti_term_id | target_word | span | has_vc |")
        L.append("|---|---|---|---|---|---|---|")
        for r, vf in zip(rows, vcflags):
            L.append(f"| {r['id']} | {r['file_id']} | {r['term_inv_id']} | {r['mti_term_id']} | {r['target_word']} | {r['span_strong_match']} | {vf} |")
        L.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"dup groups={len(groups)} | extra live rows={extra}")
    print(f"same_mti={same_mti} diff_mti={diff_mti} | same_file={same_file} diff_file={diff_file}")
    print(f"vc on >=2 rows={both_have_vc} | on 1={one_has_vc} | on none={none_has_vc}")
    print("wrote:", OUT)
    c.close()


if __name__ == "__main__":
    main()
