"""_build_t2_flag_sample.py — READ-ONLY. Shows real verses + meaning paragraphs from the T2 and FLAG buckets,
separately, spanning the range of term types, so the researcher can judge before any disposition. No DB writes.
"""
import sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row

# curated spread (transliteration, how many examples) per bucket
T2 = ["et", "al", "a.ni", "mi", "yad", "ra.ah", "qe.rev", "o.zen"]      # particles/pronouns → body-part qualifiers
FLAG = ["lev", "kardia", "ne.phesh", "sarx", "mish.pat", "be.rit", "shem", "me.od"]  # seats → substantive → adverb


def examples(cl, tl, k=2):
    rows = c.execute("""SELECT m.strongs_number sn, vr.reference ref, vr.verse_text vt, f.finding_value para,
                              (SELECT fv.finding_value FROM finding fv JOIN finding_question_link lq ON lq.finding_id=fv.id
                               WHERE fv.verse_context_id=f.verse_context_id AND fv.provenance='l2_api' AND lq.question_id=395 LIMIT 1) sense
                       FROM finding f JOIN mti_terms m ON m.id=f.mti_term_id
                       JOIN verse_context vc ON vc.id=f.verse_context_id JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                       WHERE m.cluster_code=? AND m.transliteration=? AND f.provenance='l2_meaning' AND LENGTH(f.finding_value)>80
                       ORDER BY f.id LIMIT ?""", (cl, tl, k)).fetchall()
    return rows


L = ["# T2 and FLAG — sample verses + meanings (for judgement)", "",
     "> READ-ONLY. Real verse text + the meaning paragraph the verse-read wrote, by term, so you can see what "
     "these buckets actually contain. No action taken.", ""]
for cl, terms in (("T2", T2), ("FLAG", FLAG)):
    L.append(f"\n# === {cl} ===")
    for tl in terms:
        rows = examples(cl, tl)
        if not rows:
            continue
        L.append(f"\n## {tl} ({rows[0]['sn']})")
        for r in rows:
            L.append(f"\n**{r['ref']}** — sense: *{(r['sense'] or '?')[:60]}*")
            L.append(f"> {(r['vt'] or '').strip()[:240]}")
            L.append(f"**Meaning:** {r['para']}")
out = "research/investigations/wa-t2-flag-sample-v1-20260609.md"
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w", encoding="utf-8").write("\n".join(L))
print(f"wrote {out}")
