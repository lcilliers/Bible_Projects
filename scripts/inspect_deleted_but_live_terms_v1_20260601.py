"""Scope scan for the G3958 fault: terms deleted at the registry level but still
live in the corpus.

Signature (from the G3958 finding):
  - EVERY mti_terms row for the Strong's number is delete_flagged=1 (fully deleted), and
  - wa_verse_records under that term_id still has active rows (delete_flagged=0).

Such a term has been removed from the term registry while its verse evidence
remains live (and, in G3958's case, orphaned with mti_term_id NULL). These are
candidate wrongly-deleted real terms.

Read-only. Fast grouped dicts (no per-row subqueries).
Output: research/investigations/deleted-but-live-terms-20260601.md
  python scripts/inspect_deleted_but_live_terms_v1_20260601.py
"""
import os
import sqlite3
from collections import defaultdict

DB = os.path.join("database", "bible_research.db")
OUT = os.path.join("research", "investigations", "deleted-but-live-terms-20260601.md")


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # active + orphaned active verse records grouped by term_id
    active = defaultdict(int)
    orphan = defaultdict(int)
    for r in cur.execute("SELECT term_id, COALESCE(delete_flagged,0) df, mti_term_id FROM wa_verse_records WHERE term_id IS NOT NULL"):
        if r["df"] == 0:
            active[r["term_id"]] += 1
            if r["mti_term_id"] is None:
                orphan[r["term_id"]] += 1

    # mti_terms grouped by strongs_number: row count, all-deleted?, gloss, clusters, statuses
    meta = {}
    for r in cur.execute("SELECT strongs_number, transliteration, gloss, status, COALESCE(delete_flagged,0) df, cluster_code FROM mti_terms"):
        sn = r["strongs_number"]
        m = meta.setdefault(sn, {"rows": 0, "alldel": True, "translit": r["transliteration"], "gloss": r["gloss"],
                                  "clusters": set(), "statuses": set()})
        m["rows"] += 1
        if r["df"] == 0:
            m["alldel"] = False
        if r["cluster_code"]:
            m["clusters"].add(r["cluster_code"])
        if r["status"]:
            m["statuses"].add(r["status"])

    # the fault: active verses exist AND (no live mti_terms row)
    hits = []
    no_row = []
    for tid, n in active.items():
        m = meta.get(tid)
        if m is None:
            no_row.append((tid, n, orphan.get(tid, 0)))
            continue
        if m["alldel"]:
            hits.append((tid, n, orphan.get(tid, 0), m))

    hits.sort(key=lambda x: -x[1])
    no_row.sort(key=lambda x: -x[1])
    tot_active = sum(h[1] for h in hits)
    tot_orphan = sum(h[2] for h in hits)

    L = ["# Deleted-but-live terms — scope of the G3958 fault", "",
         "**Generated:** 2026-06-01 (read-only). Signature: every `mti_terms` row for the Strong's is `delete_flagged=1`, yet active (df=0) verse records exist under its `term_id`.", "",
         f"**Fully-deleted terms that still have live verses: {len(hits)}**",
         f"- total active verse records stranded under them: **{tot_active}**",
         f"- of which orphaned (`mti_term_id` NULL): **{tot_orphan}**",
         f"- term_ids with active verses but NO `mti_terms` row at all: {len(no_row)}", "",
         "active = wa_verse_records df=0 under term_id; orphan = those with mti_term_id NULL.", "",
         "| strongs | translit | gloss | mti_rows | statuses | active | orphan | clusters |",
         "|---|---|---|---:|---|---:|---:|---|"]
    for tid, n, orph, m in hits:
        L.append(f"| {tid} | {m['translit'] or ''} | {(m['gloss'] or '').replace('|','/')} | {m['rows']} | {';'.join(sorted(m['statuses'])) or '(null)'} | {n} | {orph} | {';'.join(sorted(m['clusters'])) or '-'} |")

    if no_row:
        L += ["", "## term_ids with active verses but no mti_terms row", "", "| term_id | active | orphan |", "|---|---:|---:|"]
        for tid, n, orph in no_row:
            L.append(f"| {tid} | {n} | {orph} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"deleted-but-live terms={len(hits)} | stranded active verses={tot_active} | orphaned={tot_orphan} | term_ids with no mti row={len(no_row)}")
    print(f"wrote: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
