"""Read-only quality-check report: N random covered verses per term, showing the
verse text, the diagnostic tier findings, and the final meaning paragraph.

Safe (read-only). Output -> outputs/markdown/M02-meaning-quality-check-<date>.md
Usage: python scripts/_generate_meaning_quality_check.py [--terms t1,t2,...] [--per 5] [--cluster M02]
"""
import sqlite3, os, sys, argparse, datetime
sys.stdout.reconfigure(encoding="utf-8")

DB = os.path.join("database", "bible_research.db")
# Stable positional field order for the first 12 l2_api slots (verse-level extraction spec).
FIELD_LABELS = [
    "sense_applied", "type", "compound", "mode", "origin", "attributed_to_God",
    "purpose_equips", "typology_direction", "immediate_response",
    "produces_effect", "relational_implication", "literary_setting",
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", default="M02")
    ap.add_argument("--terms", default="che.mah,orgE,qin.ah,riv,ka.as")
    ap.add_argument("--per", type=int, default=5)
    args = ap.parse_args()

    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    terms = [t.strip() for t in args.terms.split(",") if t.strip()]

    out = []
    out.append(f"# M02 Meaning Quality Check — {args.per} random verses x {len(terms)} terms\n")
    out.append(f"> Read-only spot check. Generated {datetime.date(2026,6,10)}. "
               f"Cluster {args.cluster}. Each verse shows the diagnostic tier findings "
               f"(first 12 fields) + the final meaning paragraph (l2_meaning).\n")

    for term in terms:
        # resolve the term (case-insensitive contains, owned by cluster)
        trow = c.execute(
            "SELECT id, transliteration, strongs_number FROM mti_terms "
            "WHERE cluster_code=? AND LOWER(transliteration)=LOWER(?) LIMIT 1",
            (args.cluster, term)).fetchone()
        if not trow:
            # fall back to LIKE
            trow = c.execute(
                "SELECT id, transliteration, strongs_number FROM mti_terms "
                "WHERE cluster_code=? AND LOWER(transliteration) LIKE LOWER(?) LIMIT 1",
                (args.cluster, term + "%")).fetchone()
        if not trow:
            out.append(f"\n## {term} — NOT FOUND in {args.cluster}\n")
            continue

        mid, tl, strong = trow["id"], trow["transliteration"], trow["strongs_number"]
        # covered verse_context rows for this term (have an l2_meaning finding)
        rows = c.execute(
            "SELECT vc.id vcid, vr.reference ref, vr.verse_text vtext "
            "FROM verse_context vc "
            "JOIN wa_verse_records vr ON vr.id = vc.verse_record_id "
            "WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0 "
            "AND EXISTS (SELECT 1 FROM finding f WHERE f.verse_context_id=vc.id "
            "            AND f.provenance='l2_meaning' AND COALESCE(f.delete_flagged,0)=0) "
            "ORDER BY RANDOM() LIMIT ?", (mid, args.per)).fetchall()

        tot = c.execute(
            "SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? "
            "AND COALESCE(vc.delete_flagged,0)=0 AND EXISTS "
            "(SELECT 1 FROM finding f WHERE f.verse_context_id=vc.id AND f.provenance='l2_meaning')",
            (mid,)).fetchone()[0]

        out.append(f"\n---\n\n## {tl}  ({strong})  —  {len(rows)} of {tot} covered verses shown\n")

        for r in rows:
            vals = [x["finding_value"] for x in c.execute(
                "SELECT finding_value FROM finding WHERE verse_context_id=? "
                "AND provenance='l2_api' AND COALESCE(delete_flagged,0)=0 ORDER BY id", (r["vcid"],)).fetchall()]
            meaning = c.execute(
                "SELECT finding_value FROM finding WHERE verse_context_id=? "
                "AND provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0 ORDER BY id LIMIT 1",
                (r["vcid"],)).fetchone()
            # faculties = any non-NONE value at slot >=12
            facs = sorted({v for v in vals[12:] if v and v != "NONE"})

            out.append(f"\n### {r['ref']}   *(vcid {r['vcid']})*\n")
            vt = (r["vtext"] or "").strip().replace("\n", " ")
            out.append(f"> {vt}\n")
            for i, lab in enumerate(FIELD_LABELS):
                if i < len(vals) and vals[i] and vals[i] != "NONE":
                    out.append(f"- **{lab}:** {vals[i]}")
            if facs:
                out.append(f"- **faculty/location:** {', '.join(facs)}")
            out.append(f"\n**MEANING:** {meaning['finding_value'] if meaning else '(none)'}\n")

    date = "20260610"
    path = os.path.join("outputs", "markdown", f"M02-meaning-quality-check-{date}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote {path}  ({len(terms)} terms x up to {args.per} verses)")

if __name__ == "__main__":
    main()
