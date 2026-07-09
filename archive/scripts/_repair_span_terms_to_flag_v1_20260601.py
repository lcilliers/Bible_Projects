"""Push not-in-a-cluster terms that have ACTIVE span to the FLAG holding cluster.

Researcher direction 2026-06-01: "push the 37 items with live span to flag
cluster. The set-aside reasoning will be considered in the flag cluster. Any
items in the 107 remaining items with live span follows the same path."

Target (truth-based, uniform):
  a Strong's term where
    - ACTIVE span > 0  (wa_verse_records.span_strong_match=1 AND delete_flagged=0), AND
    - it has NO live (delete_flagged=0) row in a real M-cluster, AND
    - it is not already in FLAG / T2.
This is exactly the 37 deleted-but-used candidates + the 107-remaining-with-span,
with no double counting.

Action on every mti_terms row of each target Strong's:
  cluster_code='FLAG', delete_flagged=0, exclusion_reason=NULL, last_changed=now.
(No verse records touched. Dedup to one row/Strong's is the separate OT-DBR-009 step.)

DEFAULT IS DRY-RUN. Pass --apply to write.
"""
import argparse
import os
import re
import sqlite3
from collections import defaultdict

DB = os.path.join("database", "bible_research.db")
M_RE = re.compile(r"^M\d")
OUT = os.path.join("research", "investigations", "repair-span-terms-to-flag-20260601.md")


def target_strongs(cur):
    active_span = defaultdict(int)
    seen = defaultdict(set)
    for r in cur.execute("SELECT term_id, reference FROM wa_verse_records WHERE span_strong_match=1 AND COALESCE(delete_flagged,0)=0 AND term_id IS NOT NULL AND reference IS NOT NULL"):
        if r["reference"] not in seen[r["term_id"]]:
            seen[r["term_id"]].add(r["reference"]); active_span[r["term_id"]] += 1

    has_live_m = defaultdict(bool); in_flag_t2 = defaultdict(bool); any_deleted = defaultdict(bool)
    for r in cur.execute("SELECT strongs_number sn, cluster_code cc, COALESCE(delete_flagged,0) df FROM mti_terms"):
        if r["df"] == 0 and r["cc"] and M_RE.match(r["cc"]):
            has_live_m[r["sn"]] = True
        if r["cc"] in ("FLAG", "T2"):
            in_flag_t2[r["sn"]] = True
        if r["df"] == 1:
            any_deleted[r["sn"]] = True

    tgt = [sn for sn in active_span if active_span[sn] > 0 and not has_live_m[sn] and not in_flag_t2[sn]]
    return tgt, active_span, any_deleted


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=15); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    tgt, active_span, any_deleted = target_strongs(cur)
    tgt_set = set(tgt)
    placeholders = ",".join("?" * len(tgt))
    rows = cur.execute(f"SELECT id, strongs_number sn, COALESCE(delete_flagged,0) df FROM mti_terms WHERE strongs_number IN ({placeholders})", tgt).fetchall()
    n_rows = len(rows)
    rescued = sorted({r["sn"] for r in rows if r["df"] == 1})

    L = [f"# Push span terms to FLAG — {'APPLY' if a.apply else 'DRY-RUN'}", "",
         f"- target Strong's terms (active span, not in a real cluster, not already FLAG/T2): **{len(tgt)}**",
         f"- mti_terms rows to update: **{n_rows}**",
         f"- of those Strong's, currently carrying a deleted row (rescued from delete): {len(rescued)}",
         f"- total active span verses across target: {sum(active_span[s] for s in tgt)}", "",
         "Action per row: cluster_code='FLAG', delete_flagged=0, exclusion_reason=NULL.", "",
         "| strongs | active span |", "|---|---:|"]
    for sn in sorted(tgt, key=lambda s: -active_span[s]):
        L.append(f"| {sn} | {active_span[sn]} |")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: target strongs={len(tgt)} rows={n_rows} rescued-from-delete={len(rescued)}")
    print(f"Report: {OUT}")
    if not a.apply:
        conn.close(); return

    cur.execute("BEGIN")
    try:
        cur.execute(f"UPDATE mti_terms SET cluster_code='FLAG', delete_flagged=0, exclusion_reason=NULL, last_changed=datetime('now') WHERE strongs_number IN ({placeholders})", tgt)
        n = cur.rowcount
        if n != n_rows:
            conn.rollback(); raise SystemExit(f"ABORT: UPDATE affected {n}, expected {n_rows} — rolled back.")
        conn.commit()
    except Exception:
        conn.rollback(); raise
    print(f"APPLIED: {n} rows -> cluster_code='FLAG', delete_flagged=0, exclusion_reason cleared. No verse rows touched.")
    conn.close()


if __name__ == "__main__":
    main()
