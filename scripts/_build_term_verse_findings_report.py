"""_build_term_verse_findings_report.py — READ-ONLY. For N terms, show up to K verses each with the verse
text, every tier finding (l2_api), the multi-selects (faculty/location), and the meaning paragraph (l2_meaning).
Short per-verse queries (safe to run while another cluster is writing). No DB writes.

Usage:  python scripts/_build_term_verse_findings_report.py --terms 298,266,829,1554,305 --verses 10 --out <file>.md
"""
import argparse, sqlite3, sys, os
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

# obs_id -> field label, in display order
FIELD = [(395, "sense_applied"), (239, "type"), (240, "compound"), (245, "mode"), (285, "origin"),
         (225, "attributed_to_God"), (227, "purpose_equips"), (234, "typology_direction"),
         (248, "immediate_response"), (251, "produces_effect"), (238, "relational_implication"), (404, "literary_setting")]
FACULTY = {291: "perception", 294: "cognition", 297: "memory", 300: "affect", 303: "creativity",
           306: "volition", 309: "agency", 312: "moral-evaluation", 315: "conscience", 321: "relational"}
LOCATION = {260: "spirit", 264: "soul", 267: "heart", 270: "mind", 276: "body"}

ap = argparse.ArgumentParser()
ap.add_argument("--terms", required=True)
ap.add_argument("--verses", type=int, default=10)
ap.add_argument("--out", required=True)
a = ap.parse_args()
ids = [int(x) for x in a.terms.split(",") if x.strip()]
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row

L = [f"# Verse-read findings report — {len(ids)} terms × up to {a.verses} verses", "",
     "> READ-ONLY. Per term: the verse text, every tier finding, and the meaning paragraph.", ""]
for tid in ids:
    t = c.execute("SELECT transliteration tl, strongs_number sn, cluster_code cc FROM mti_terms WHERE id=?", (tid,)).fetchone()
    total = c.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (tid,)).fetchone()[0]
    L.append(f"\n## {t['tl']} ({t['sn']}, {t['cc']}) — {a.verses} of {total} verses\n")
    verses = c.execute("""SELECT vc.id vcid, vr.reference ref, vr.verse_text vt
                          FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                          WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0 ORDER BY vr.id LIMIT ?""",
                       (tid, a.verses)).fetchall()
    for v in verses:
        L.append(f"### {v['ref']}")
        L.append(f"**Verse:** {(v['vt'] or '').strip()}")
        # findings for this (vcid)
        fmap = {r["q"]: r["val"] for r in c.execute(
            """SELECT l.question_id q, f.finding_value val FROM finding f JOIN finding_question_link l ON l.finding_id=f.id
               WHERE f.verse_context_id=? AND f.provenance='l2_api'""", (v["vcid"],))}
        L.append("**Findings:**")
        for obs, lab in FIELD:
            if obs in fmap:
                L.append(f"- {lab}: {fmap[obs]}")
        fac = [FACULTY[o] for o in FACULTY if fmap.get(o) and fmap[o].lower() not in ("none", "")]
        loc = [LOCATION[o] for o in LOCATION if fmap.get(o) and fmap[o].lower() not in ("none", "")]
        L.append(f"- faculty: {', '.join(fac) or 'NONE'}")
        L.append(f"- constitutional_location: {', '.join(loc) or 'NONE'}")
        para = c.execute("SELECT finding_value FROM finding WHERE verse_context_id=? AND mti_term_id=? AND provenance='l2_meaning'", (v["vcid"], tid)).fetchone()
        flag = c.execute("SELECT flagged_for_review FROM finding WHERE verse_context_id=? AND mti_term_id=? AND provenance='l2_meaning'", (v["vcid"], tid)).fetchone()
        fl = " ⚑" if flag and flag[0] else ""
        L.append(f"**Meaning{fl}:** {para[0] if para else '(none)'}\n")

os.makedirs(os.path.dirname(a.out), exist_ok=True)
open(a.out, "w", encoding="utf-8").write("\n".join(L))
print(f"wrote {a.out} ({len(ids)} terms)")
