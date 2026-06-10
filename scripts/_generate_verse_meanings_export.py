"""Read-only export of verse MEANINGS (l2_meaning paragraphs only) for a cluster.

For each covered verse: reference + verse text + the final meaning paragraph.
No tier findings. Grouped by term, verses in canonical (book/chapter/verse) order.

Safe (read-only). Output -> outputs/markdown/<cluster>-verse-meanings-<date>.md
Usage: python scripts/_generate_verse_meanings_export.py [--cluster M02] [--terms t1,t2]
"""
import sqlite3, os, sys, argparse

sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", default="M02")
    ap.add_argument("--terms", default="")  # optional comma list; blank = all covered terms
    args = ap.parse_args()

    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row

    # terms in the cluster that have at least one covered verse, ordered by transliteration
    term_filter = ""
    params = [args.cluster]
    if args.terms.strip():
        wanted = [t.strip() for t in args.terms.split(",") if t.strip()]
        term_filter = " AND m.transliteration IN (%s)" % ",".join("?" * len(wanted))
        params += wanted
    terms = c.execute(
        "SELECT m.id, m.transliteration tl, m.strongs_number sn, COUNT(DISTINCT vc.id) n "
        "FROM mti_terms m JOIN verse_context vc ON vc.mti_term_id=m.id "
        "WHERE m.cluster_code=?" + term_filter + " AND COALESCE(vc.delete_flagged,0)=0 "
        "AND EXISTS (SELECT 1 FROM finding f WHERE f.verse_context_id=vc.id "
        "            AND f.provenance='l2_meaning' AND COALESCE(f.delete_flagged,0)=0) "
        "GROUP BY m.id ORDER BY m.transliteration", params).fetchall()

    total = sum(t["n"] for t in terms)
    out = [f"# {args.cluster} — Verse Meanings ({total} verses, {len(terms)} terms)\n",
           "> Read-only export. Each verse: reference + text + final meaning paragraph "
           "(`l2_meaning`). Generated 2026-06-10.\n",
           "\n## Contents\n"]
    for t in terms:
        anchor = t["tl"].replace(".", "").replace(" ", "-").lower()
        out.append(f"- [{t['tl']} ({t['sn']}) — {t['n']}](#{anchor})")
    out.append("")

    for t in terms:
        anchor = t["tl"].replace(".", "").replace(" ", "-").lower()
        out.append(f'\n---\n\n## <a id="{anchor}"></a>{t["tl"]} ({t["sn"]}) — {t["n"]} verses\n')
        rows = c.execute(
            "SELECT vr.reference ref, vr.verse_text vtext, "
            "       vr.book_id bid, vr.chapter ch, vr.verse_num vn, vc.id vcid "
            "FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
            "WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0 "
            "AND EXISTS (SELECT 1 FROM finding f WHERE f.verse_context_id=vc.id "
            "            AND f.provenance='l2_meaning' AND COALESCE(f.delete_flagged,0)=0) "
            "ORDER BY vr.book_id, vr.chapter, vr.verse_num", (t["id"],)).fetchall()
        for r in rows:
            meaning = c.execute(
                "SELECT finding_value FROM finding WHERE verse_context_id=? "
                "AND provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0 ORDER BY id LIMIT 1",
                (r["vcid"],)).fetchone()
            vt = (r["vtext"] or "").strip().replace("\n", " ")
            out.append(f"**{r['ref']}** — {vt}")
            out.append(f"\n{meaning['finding_value'] if meaning else '(no meaning)'}\n")

    date = "20260610"
    path = os.path.join("outputs", "markdown", f"{args.cluster}-verse-meanings-{date}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote {path}  ({total} verse meanings across {len(terms)} terms)")

if __name__ == "__main__":
    main()
