"""Test the 'shared-span survival' assumption on G3958 (pascho, 'to suffer').

Assumption under test: a term may carry no live verses of its own, yet because it
was extracted alongside another term in the SAME verses, that other (related) term
is still active for the verse -- so the evidence is not lost when the first term is
deleted.

Method (read-only):
  1. Identify G3958's mti_terms rows + its wa_verse_records (active + deleted).
  2. Take the distinct verse references where G3958 occurs = its 'span'.
  3. For those references, find every OTHER term (term_id != G3958) with an ACTIVE
     (delete_flagged=0) verse record -> the related/co-occurring active terms.
  4. Per reference: is there at least one active related term? (evidence survives)
     Flag references with NO active related term (evidence would be lost).
  5. Note G3958's own active-but-orphaned records (mti_term_id NULL).

Output: research/investigations/g3958-span-survival-test-20260601.md
  python scripts/inspect_g3958_span_test_v1_20260601.py
"""
import os
import sqlite3

DB = os.path.join("database", "bible_research.db")
OUT = os.path.join("research", "investigations", "g3958-span-survival-test-20260601.md")
SN = "G3958"


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    term_rows = cur.execute(
        "SELECT id, strongs_number, transliteration, gloss, status, COALESCE(delete_flagged,0) df, "
        "cluster_code, owning_registry, owning_word FROM mti_terms WHERE strongs_number=?", (SN,)).fetchall()

    recs = cur.execute(
        "SELECT id, reference, mti_term_id, COALESCE(delete_flagged,0) df, target_word "
        "FROM wa_verse_records WHERE term_id LIKE ? ORDER BY reference", (SN + "%",)).fetchall()
    refs = sorted({r["reference"] for r in recs if r["reference"]})
    active_orphan = [r for r in recs if r["df"] == 0 and r["mti_term_id"] is None]

    # co-occurring ACTIVE records at G3958's references, excluding G3958 itself
    placeholders = ",".join("?" * len(refs))
    related = cur.execute(
        f"SELECT reference, term_id, COUNT(1) n FROM wa_verse_records "
        f"WHERE reference IN ({placeholders}) AND COALESCE(delete_flagged,0)=0 "
        f"AND term_id NOT LIKE ? GROUP BY reference, term_id", refs + [SN + "%"]).fetchall()

    by_ref = {}
    for r in related:
        by_ref.setdefault(r["reference"], []).append((r["term_id"], r["n"]))

    # for each related term_id, look up its mti_terms status (active? clustered?)
    rel_terms = sorted({r["term_id"] for r in related})
    term_meta = {}
    for tid in rel_terms:
        m = cur.execute(
            "SELECT strongs_number, transliteration, gloss, status, COALESCE(delete_flagged,0) df, cluster_code "
            "FROM mti_terms WHERE strongs_number=? ORDER BY COALESCE(delete_flagged,0) LIMIT 1", (tid,)).fetchone()
        term_meta[tid] = dict(m) if m else None

    covered = [rf for rf in refs if by_ref.get(rf)]
    uncovered = [rf for rf in refs if not by_ref.get(rf)]

    L = ["# G3958 *pascho* — shared-span survival test", "",
         "**Generated:** 2026-06-01 (read-only). Tests whether G3958's verse evidence survives under related active terms in the same verses.", "",
         "## G3958 term rows (mti_terms)", ""]
    for t in term_rows:
        L.append(f"- id={t['id']} status={t['status']} delete_flagged={t['df']} cluster={t['cluster_code']} registry={t['owning_registry']} ({t['owning_word']})")
    L += ["",
          f"## Verse footprint",
          f"- wa_verse_records for G3958: {len(recs)} total | active(df=0): {sum(1 for r in recs if r['df']==0)} | deleted(df=1): {sum(1 for r in recs if r['df']==1)}",
          f"- active-but-ORPHANED (df=0, mti_term_id NULL): **{len(active_orphan)}** — live verses attached to no mti_terms row",
          f"- distinct references (the 'span'): {len(refs)}",
          f"- references WITH >=1 active related term (evidence survives): **{len(covered)}**",
          f"- references with NO active related term (evidence would be lost): **{len(uncovered)}**", ""]

    if uncovered:
        L += ["### References with NO active related term", ""]
        for rf in uncovered:
            L.append(f"- {rf}")
        L.append("")

    L += ["## Per-reference detail (G3958 verses -> active related terms)", "",
          "| reference | active related terms (strongs x count) |", "|---|---|"]
    for rf in refs:
        rel = by_ref.get(rf, [])
        if rel:
            cell = "; ".join(f"{tid}x{n}" for tid, n in sorted(rel))
        else:
            cell = "**(none — uncovered)**"
        L.append(f"| {rf} | {cell} |")

    L += ["", "## Related terms encountered (status / cluster)", "",
          "| strongs | translit | gloss | status | del | cluster |", "|---|---|---|---|---|---|"]
    for tid in rel_terms:
        m = term_meta[tid]
        if m:
            L.append(f"| {tid} | {m['transliteration'] or ''} | {m['gloss'] or ''} | {m['status']} | {m['df']} | {m['cluster_code']} |")
        else:
            L.append(f"| {tid} | | | (no mti_terms row) | | |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"refs={len(refs)} covered={len(covered)} uncovered={len(uncovered)} active_orphan={len(active_orphan)}")
    print(f"wrote: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
