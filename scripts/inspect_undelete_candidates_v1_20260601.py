"""Inspect the DELETED term population for undelete candidates, judged on active span.

Researcher (2026-06-01): do not reverse en masse. Most deleted terms correctly
stay deleted because the term has no span in their associated verses (not actually
used). Find the minority that SHOULD be undeleted = a deleted term genuinely used.

Definitions:
  - deleted term  = a Strong's with NO live (delete_flagged=0) mti_terms row.
  - ACTIVE span   = wa_verse_records with span_strong_match=1 AND delete_flagged=0
                    (term genuinely used AND the verse record is live), distinct reference.
  - total span    = span_strong_match=1 regardless of the record's delete flag.

Buckets for each deleted term:
  A  active span > 0                      -> UNDELETE CANDIDATE (used, live verses; G3958 class)
  B  active span = 0 but total span > 0   -> review (was used, but all its verse records deleted)
  C  total span = 0                       -> stays deleted (never genuinely used)

Read-only.
Output: research/investigations/undelete-candidates-20260601.md
  python scripts/inspect_undelete_candidates_v1_20260601.py
"""
import os
import sqlite3
from collections import defaultdict

DB = os.path.join("database", "bible_research.db")
OUT = os.path.join("research", "investigations", "undelete-candidates-20260601.md")


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    active_span = defaultdict(set)
    total_span = defaultdict(set)
    for r in cur.execute("SELECT term_id, reference, COALESCE(delete_flagged,0) df FROM wa_verse_records WHERE span_strong_match=1 AND term_id IS NOT NULL AND reference IS NOT NULL"):
        total_span[r["term_id"]].add(r["reference"])
        if r["df"] == 0:
            active_span[r["term_id"]].add(r["reference"])

    # strongs: has a live row? + meta + cluster
    has_live = defaultdict(bool)
    meta = {}
    for r in cur.execute("SELECT strongs_number sn, transliteration tr, gloss, language lang, cluster_code cc, COALESCE(delete_flagged,0) df FROM mti_terms"):
        sn = r["sn"]
        if r["df"] == 0:
            has_live[sn] = True
        m = meta.setdefault(sn, {"tr": r["tr"], "gloss": r["gloss"], "lang": r["lang"], "clusters": set()})
        if r["cc"]:
            m["clusters"].add(r["cc"])

    deleted = [sn for sn in meta if not has_live[sn]]
    A, B, C = [], [], []
    for sn in deleted:
        asp = len(active_span.get(sn, ()))
        tsp = len(total_span.get(sn, ()))
        if asp > 0:
            A.append((sn, asp, tsp))
        elif tsp > 0:
            B.append((sn, asp, tsp))
        else:
            C.append((sn, asp, tsp))
    A.sort(key=lambda x: -x[1]); B.sort(key=lambda x: -x[2])

    L = ["# Undelete candidates — deleted terms judged on active span (usage)", "",
         "**Generated:** 2026-06-01 (read-only). Deleted term = no live `mti_terms` row. "
         "Active span = `span_strong_match=1` AND verse record `delete_flagged=0`, distinct reference.", "",
         f"**Deleted terms (distinct Strong's): {len(deleted)}**",
         f"- **A — UNDELETE CANDIDATES (active span > 0): {len(A)}**  (used, with live verses)",
         f"- B — review (no active span, but was used; verse records all deleted): {len(B)}",
         f"- **C — stay deleted (no span at all, never genuinely used): {len(C)}**", "",
         "## A — undelete candidates (sorted by active span verses)", "",
         "| strongs | translit | gloss | lang | active span | total span | clusters |", "|---|---|---|---|---:|---:|---|"]
    for sn, asp, tsp in A:
        m = meta[sn]
        L.append(f"| {sn} | {m['tr'] or ''} | {(m['gloss'] or '').replace('|','/')} | {m['lang'] or ''} | {asp} | {tsp} | {';'.join(sorted(m['clusters'])) or '-'} |")

    L += ["", "## B — was used but all verse records deleted (review, sorted by total span)", "",
          "| strongs | translit | gloss | lang | active span | total span |", "|---|---|---|---|---:|---:|"]
    for sn, asp, tsp in B[:60]:
        m = meta[sn]
        L.append(f"| {sn} | {m['tr'] or ''} | {(m['gloss'] or '').replace('|','/')} | {m['lang'] or ''} | {asp} | {tsp} |")
    if len(B) > 60:
        L.append(f"| … | | | | | _({len(B)-60} more)_ |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"deleted strongs={len(deleted)} | A undelete-candidates={len(A)} | B review={len(B)} | C stay-deleted={len(C)}")
    print(f"wrote: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
