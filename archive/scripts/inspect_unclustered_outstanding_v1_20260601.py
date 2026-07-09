"""Single read-only listing of ALL remaining outstanding unclustered terms.

Outstanding = mti_terms with cluster_code IS NULL that are NOT category A
(A = delete_flagged=1 AND has exclusion_reason = already resolved).

Categories (per the remediation plan):
  B suspect   - delete_flagged=1, no reason  (held: carry active evidence)
  C           - delete_flagged=0, status in (delete/excluded), HAS reason (desync / excluded)
  D suspect   - delete_flagged=0, status in (delete/excluded), no reason (held: active evidence)
  E           - delete_flagged=0, status='candidate_delete' (undecided)
  F           - delete_flagged=0, live (extracted/etc), no exclusion decision

Each row: gloss, status, delete_flagged, active_verses (wa_verse_records del=0),
active_vc (verse_context del=0), reason (if any), owning registry.
Fast: two GROUP BY count dicts, no per-row subqueries (avoids the read-lock issue).

Output: research/investigations/unclustered-outstanding-items-20260601.md
  python scripts/inspect_unclustered_outstanding_v1_20260601.py
"""
import os
import sqlite3

DB = os.path.join("database", "bible_research.db")
OUT = os.path.join("research", "investigations", "unclustered-outstanding-items-20260601.md")


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    terms = cur.execute(
        "SELECT id, strongs_number, transliteration, gloss, language, "
        "COALESCE(status,'(null)') status, COALESCE(delete_flagged,0) df, exclusion_reason, "
        "owning_registry, owning_word "
        "FROM mti_terms "
        "WHERE cluster_code IS NULL "
        "AND ( COALESCE(delete_flagged,0)=0 OR exclusion_reason IS NULL OR TRIM(exclusion_reason)='' )"
    ).fetchall()

    vr = {r["mti_term_id"]: r["n"] for r in cur.execute(
        "SELECT mti_term_id, COUNT(1) n FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL GROUP BY mti_term_id")}
    vc = {r["mti_term_id"]: r["n"] for r in cur.execute(
        "SELECT mti_term_id, COUNT(1) n FROM verse_context WHERE COALESCE(delete_flagged,0)=0 AND mti_term_id IS NOT NULL GROUP BY mti_term_id")}

    def categorise(t, hr):
        df, st = t["df"], t["status"]
        decided = st in ("delete", "excluded")
        if df == 1 and not hr:
            return "B suspect"
        if df == 0 and decided and hr:
            return "C reasoned/excluded"
        if df == 0 and decided and not hr:
            return "D suspect"
        if df == 0 and st == "candidate_delete":
            return "E candidate"
        return "F live"

    rows = []
    for t in terms:
        hr = bool(t["exclusion_reason"] and t["exclusion_reason"].strip())
        rows.append((categorise(t, hr), t, vr.get(t["id"], 0), vc.get(t["id"], 0), hr))

    order = {"B suspect": 0, "D suspect": 1, "C reasoned/excluded": 2, "E candidate": 3, "F live": 4}
    rows.sort(key=lambda x: (order[x[0]], -(max(x[2], x[3])), x[1]["strongs_number"] or ""))

    from collections import Counter
    counts = Counter(r[0] for r in rows)

    L = ["# Unclustered — all remaining outstanding terms", "",
         "**Generated:** 2026-06-01 (read-only). Source: mti_terms, cluster_code IS NULL, excluding resolved (category A = deleted-with-reason).",
         f"**Total outstanding: {len(rows)}**", ""]
    for k in ["B suspect", "D suspect", "C reasoned/excluded", "E candidate", "F live"]:
        L.append(f"- {k}: {counts.get(k,0)}")
    L += ["",
          "Categories: **B/D suspect** = no reason yet still carry live evidence (review: reinstate vs delete-with-reason). "
          "**C** = has a reason but delete_flagged=0 (56 status='excluded' + 8 active-evidence held). "
          "**E** = candidate_delete, undecided. **F** = live extracted, never clustered nor excluded.",
          "",
          "active_verses = wa_verse_records del=0; active_vc = verse_context del=0.",
          "",
          "| cat | strongs | translit | gloss | lang | status | del | a_verses | a_vc | reason | reg |",
          "|---|---|---|---|---|---|---:|---:|---:|---|---|"]
    for c, t, av, ac, hr in rows:
        g = (t["gloss"] or "").replace("|", "\\|")
        tr = (t["transliteration"] or "").replace("|", "\\|")
        rsn = (t["exclusion_reason"] or "").replace("|", "\\|").replace("\n", " ")
        rsn = (rsn[:60] + "...") if len(rsn) > 63 else rsn
        L.append(f"| {c} | {t['strongs_number']} | {tr} | {g} | {t['language']} | {t['status']} | {t['df']} | {av} | {ac} | {rsn} | {t['owning_registry']}:{t['owning_word']} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"total outstanding={len(rows)} | " + " ".join(f"{k}={v}" for k, v in counts.items()))
    print(f"wrote: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
