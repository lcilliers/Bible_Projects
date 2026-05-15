"""Last verification round: real vc rows, constraints."""
import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

# ag3 — find real vc row for Psa 23:5 / da.shen (mti=111)
print("=== ag3 — actual vc row for Psa 23:5 / mti=111 / group_id=51 ===")
for r in c.execute("""SELECT vc.id vc_id, vc.verse_record_id, vr.reference,
                             vc.mti_term_id, vc.group_id, vc.is_relevant,
                             vc.cluster_subgroup_id
                      FROM verse_context vc
                      LEFT JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                      WHERE vc.mti_term_id=111 AND COALESCE(vc.delete_flagged,0)=0
                      ORDER BY vc.id"""):
    print(f"  vc={r['vc_id']:<6} vr={r['verse_record_id']:<6} {r['reference']:<14} "
          f"group_id={r['group_id']} relevant={r['is_relevant']} sg_id={r['cluster_subgroup_id']}")

# ag4 — verse_context constraints (uniqueness on (verse_record_id, mti_term_id)?)
print("\n=== verse_context indexes / unique constraints ===")
for r in c.execute("PRAGMA index_list(verse_context)"):
    print(f"  index={r['name']} unique={r['unique']}")
    for col in c.execute(f"PRAGMA index_info({r['name']})"):
        print(f"    col: {col['name']}")

# ag4 — find existing vc rows for 1Ti 6:6 / 2Cor 9:8 with mti=743 — can a 2nd row exist?
print("\n=== ag4 — existing vc rows for autarkeia (mti=743) at the 2 target verses ===")
for r in c.execute("""SELECT vc.id vc_id, vc.verse_record_id, vr.reference, vc.mti_term_id,
                             vc.group_id, vc.is_relevant, vc.cluster_subgroup_id
                      FROM verse_context vc
                      LEFT JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                      WHERE vc.mti_term_id=743
                        AND vc.verse_record_id IN (15117, 148147)
                        AND COALESCE(vc.delete_flagged,0)=0"""):
    print(f"  vc={r['vc_id']:<6} vr={r['verse_record_id']:<7} {r['reference']:<10} "
          f"group_id={r['group_id']} relevant={r['is_relevant']} sg_id={r['cluster_subgroup_id']}")

# H4924B — does the gloss/translit pattern match the directive's "mish.man / fatness"?
print("\n=== H4924B verification — does it match 'mish.man / fatness'? ===")
r = c.execute("SELECT id, strongs_number, transliteration, gloss, cluster_code FROM mti_terms WHERE id=4696").fetchone()
print(f"  mti=4696: {r['strongs_number']} '{r['transliteration']}' gloss='{r['gloss']}' cluster={r['cluster_code']}")
