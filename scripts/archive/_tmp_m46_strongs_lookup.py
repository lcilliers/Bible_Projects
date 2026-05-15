"""Re-check the problem Strong's with leading-zero and adjacent-number variants."""
import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row


# Check leading-zero variants and adjacents
def search(label, *candidates):
    print(f"\n  {label}:")
    for s in candidates:
        for r in c.execute("""SELECT id, strongs_number, transliteration, gloss, cluster_code
                              FROM mti_terms
                              WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0""", (s,)):
            print(f"    {s:<8} mti={r['id']:<6} '{r['transliteration']}' "
                  f"gloss='{(r['gloss'] or '')[:30]}' cluster={r['cluster_code']}")


search("H4924 mish.man (and adjacents)", "H4924", "H4923", "H4925", "H4924A", "H4924B")
search("G842 autarkēs (leading-zero variants)", "G842", "G0842")
search("H7961 shal.a.nan (verify flag)", "H7961", "H7961A", "H7961B")
# also search by transliteration
print("\n  Search by translit shal.a.nan / shaa.nan:")
for r in c.execute("""SELECT id, strongs_number, transliteration, gloss, cluster_code
                      FROM mti_terms
                      WHERE LOWER(transliteration) LIKE '%shal%anan%'
                         OR LOWER(transliteration) LIKE '%sha%anan%'
                         OR LOWER(transliteration) LIKE '%shaanan%'
                      LIMIT 8"""):
    print(f"    mti={r['id']:<6} {r['strongs_number']:<8} '{r['transliteration']}' "
          f"gloss='{r['gloss']}' cluster={r['cluster_code']}")

# H8080 — directive says 'sha.man' but DB shows 'sha.men' for mti=4697
print("\n  H8080 sanity check:")
for r in c.execute("""SELECT id, strongs_number, transliteration, gloss, cluster_code
                      FROM mti_terms WHERE strongs_number='H8080'"""):
    print(f"    mti={r['id']} translit='{r['transliteration']}' gloss='{r['gloss']}' cluster={r['cluster_code']}")

# Action group 2 — find the real vc rows for mti_id=1870
print("\n  Action group 2 — actual verse_context rows for ke.vud.dah (mti=1870):")
for r in c.execute("""SELECT vc.id, vc.verse_record_id, vr.reference, vc.group_id,
                             vc.is_relevant, vc.cluster_subgroup_id
                      FROM verse_context vc
                      LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                      WHERE vc.mti_term_id=1870 AND COALESCE(vc.delete_flagged,0)=0
                      ORDER BY vc.id"""):
    print(f"    vc_id={r['id']} vr={r['verse_record_id']} ({r['reference']}) "
          f"group_id={r['group_id']} cluster_subgroup_id={r['cluster_subgroup_id']}")

# Action group 3 — verify vc_id=58191
print("\n  Action group 3 — vc_id=58191 verify:")
r = c.execute("""SELECT vc.id, vc.verse_record_id, vr.reference, vc.mti_term_id,
                        vc.group_id, vc.is_relevant, vc.cluster_subgroup_id
                 FROM verse_context vc
                 LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                 WHERE vc.id=58191""").fetchone()
if r:
    print(f"    vc=58191 vr={r['verse_record_id']} ({r['reference']}) "
          f"mti={r['mti_term_id']} group_id={r['group_id']} "
          f"cluster_subgroup_id={r['cluster_subgroup_id']}")
else:
    print(f"    vc=58191 NOT FOUND")

# Action group 4 — G0841 verses for 1Ti 6:6 and 2Co 9:8 already linked
print("\n  Action group 4 — G0841 autarkeia verses in DB:")
for r in c.execute("""SELECT vr.id vr_id, vr.reference, vc.id vc_id, vc.is_relevant
                      FROM wa_verse_records vr
                      LEFT JOIN verse_context vc ON vc.verse_record_id=vr.id AND vc.mti_term_id=vr.mti_term_id
                      WHERE vr.mti_term_id=743 AND COALESCE(vr.delete_flagged,0)=0
                      ORDER BY vr.id"""):
    print(f"    vr={r['vr_id']:<7} '{r['reference']:<14}' vc_id={r['vc_id']} is_relevant={r['is_relevant']}")
