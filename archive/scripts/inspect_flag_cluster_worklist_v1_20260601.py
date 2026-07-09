"""FLAG cluster worklist: every FLAG term + data to decide reallocation.

Read-only. Produces, for triage (-> cluster / -> boundary / set aside):
  - Section A: the cluster taxonomy (46 M-clusters: code, short_name, gloss) = target menu
  - Section B: 433 FLAG terms with strongs, translit, gloss, language, active-span
               (usage), owning registry, status, and a HINT column = clusters whose
               example-term gloss contains this term's transliteration (lexical match,
               a starting suggestion only — the decision is the researcher's/AI's).

Output: research/investigations/flag-cluster-worklist-20260601.md
"""
import os
import re
import sqlite3
from collections import defaultdict

DB = "database/bible_research.db"
OUT = "research/investigations/flag-cluster-worklist-20260601.md"


def main():
    c = sqlite3.connect(DB, timeout=20); c.row_factory = sqlite3.Row

    # active span by term_id (usage)
    span = defaultdict(int)
    for r in c.execute("SELECT term_id, COUNT(DISTINCT reference) n FROM wa_verse_records WHERE span_strong_match=1 AND COALESCE(delete_flagged,0)=0 AND term_id IS NOT NULL GROUP BY term_id"):
        span[r["term_id"]] = r["n"]

    # cluster taxonomy
    clusters = c.execute("SELECT cluster_code cc, short_name sn, gloss FROM cluster WHERE cluster_code LIKE 'M%' ORDER BY cluster_code").fetchall()
    cl_gloss = [(r["cc"], (r["gloss"] or "").lower()) for r in clusters]

    # FLAG terms (distinct strongs, live)
    seen = set(); terms = []
    for r in c.execute("SELECT strongs_number sn, transliteration tr, gloss, language lang, COALESCE(status,'') status, owning_registry reg, owning_word ow FROM mti_terms WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0 ORDER BY strongs_number"):
        if r["sn"] in seen:
            continue
        seen.add(r["sn"])
        terms.append(r)

    def hint(tr):
        if not tr or len(tr) < 3:
            return ""
        t = tr.lower()
        hits = [cc for cc, g in cl_gloss if t in g]
        return ";".join(hits)

    L = ["# FLAG cluster worklist — reallocation triage", "",
         "**Generated:** 2026-06-01 (read-only). 433 live FLAG terms to triage: reallocate to a cluster, mark as a boundary (between clusters), or set aside. HINT = cluster(s) whose example-term gloss contains this term's transliteration (lexical suggestion only).", "",
         "## A. Cluster taxonomy (reallocation targets)", "",
         "| code | short_name | example terms (gloss) |", "|---|---|---|"]
    for r in clusters:
        g = (r["gloss"] or "").replace("|", "/")
        g = (g[:90] + "…") if len(g) > 91 else g
        L.append(f"| {r['cc']} | {r['sn'] or ''} | {g} |")

    # count hint coverage
    hinted = sum(1 for r in terms if hint(r["tr"]))
    L += ["", f"## B. FLAG terms ({len(terms)} distinct, live) — {hinted} have a lexical hint", "",
          "Sorted by language then active-span desc. status shown as-is (note: span-rescued terms may carry a stale 'delete'/'excluded' status — the triage resets it).", "",
          "| strongs | translit | gloss | lang | span | reg | status | HINT cluster(s) |",
          "|---|---|---|---|--:|---|---|---|"]
    for r in sorted(terms, key=lambda r: (r["lang"] or "", -span.get(r["sn"], 0), r["sn"])):
        g = (r["gloss"] or "").replace("|", "/")
        g = (g[:40] + "…") if len(g) > 41 else g
        L.append(f"| {r['sn']} | {r['tr'] or ''} | {g} | {r['lang'] or ''} | {span.get(r['sn'],0)} | {r['reg'] or ''} | {r['status']} | {hint(r['tr'])} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"FLAG terms: {len(terms)} | with lexical hint: {hinted}")
    print("wrote:", OUT)
    c.close()


if __name__ == "__main__":
    main()
