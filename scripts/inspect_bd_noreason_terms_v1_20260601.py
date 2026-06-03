"""Read-only listing of the B+D 'no-reason' unclustered terms with gloss + active verse counts.

B = mti_terms cluster_code IS NULL, delete_flagged=1, no exclusion_reason.
D = cluster_code IS NULL, delete_flagged=0, status in (delete/excluded), no exclusion_reason.

For each term: gloss, status, and two active-verse signals —
  active_verses = wa_verse_records with delete_flagged=0 (literal "verses not deleted")
  active_vc     = verse_context with delete_flagged=0 (classifications; fuller signal)
Terms with either > 0 are the suspect cases (deleted with no reason yet still carry evidence).

Output: research/investigations/unclustered-no-reason-terms-bd-detail-20260601.md
  python scripts/inspect_bd_noreason_terms_v1_20260601.py
"""
import os
import sqlite3

DB = os.path.join("database", "bible_research.db")
OUT = os.path.join("research", "investigations", "unclustered-no-reason-terms-bd-detail-20260601.md")


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    terms = cur.execute(
        "SELECT id, strongs_number, transliteration, gloss, language, "
        "COALESCE(status,'(null)') status, delete_flagged "
        "FROM mti_terms "
        "WHERE cluster_code IS NULL "
        "AND (exclusion_reason IS NULL OR TRIM(exclusion_reason)='') "
        "AND ( delete_flagged=1 OR (COALESCE(delete_flagged,0)=0 AND status IN ('delete','excluded')) )"
    ).fetchall()

    vr = {r["mti_term_id"]: r["n"] for r in cur.execute(
        "SELECT mti_term_id, COUNT(*) n FROM wa_verse_records "
        "WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL GROUP BY mti_term_id")}
    vc = {r["mti_term_id"]: r["n"] for r in cur.execute(
        "SELECT mti_term_id, COUNT(*) n FROM verse_context "
        "WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL GROUP BY mti_term_id")}

    rows = []
    for t in terms:
        c = "B" if t["delete_flagged"] == 1 else "D"
        rows.append((c, t, vr.get(t["id"], 0), vc.get(t["id"], 0)))
    rows.sort(key=lambda x: (-(max(x[2], x[3])), x[0], x[1]["strongs_number"] or ""))

    nB = sum(1 for r in rows if r[0] == "B")
    nD = sum(1 for r in rows if r[0] == "D")
    with_ev = sum(1 for r in rows if r[2] > 0 or r[3] > 0)

    L = ["# Unclustered no-reason terms (B + D) - detail listing", "",
         "**Generated:** 2026-06-01 (read-only). Source: mti_terms, cluster_code IS NULL, no exclusion_reason.",
         f"**B** = soft-deleted, no reason ({nB}). **D** = decided (status delete/excluded), flag not applied, no reason ({nD}). Total {len(rows)}.",
         f"**With live verse evidence (active_verses OR active_vc > 0): {with_ev}** - suspect (no reason, yet still carries evidence).",
         "",
         "active_verses = wa_verse_records delete_flagged=0. active_vc = active verse_context (can exceed active_verses).",
         "",
         "| cat | strongs | translit | gloss | status | del | active_verses | active_vc |",
         "|---|---|---|---|---|---:|---:|---:|"]
    for c, t, av, ac in rows:
        g = (t["gloss"] or "").replace("|", "\\|")
        tr = (t["transliteration"] or "").replace("|", "\\|")
        L.append(f"| {c} | {t['strongs_number']} | {tr} | {g} | {t['status']} | {t['delete_flagged']} | {av} | {ac} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"B={nB} D={nD} total={len(rows)} | with live verse evidence={with_ev}")
    print(f"wrote: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
