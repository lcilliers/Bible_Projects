"""Scope the current UT verse load in M46 before the API run."""
import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

# Verse state per term
print('=== M46 active terms — verse state ===')
totals = {'UT':0,'relevant':0,'set_aside':0,'other':0}
for r in c.execute('''
  SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss,
    COUNT(DISTINCT CASE WHEN vc.id IS NULL AND COALESCE(vr.delete_flagged,0)=0 THEN vr.id END) ut,
    COUNT(DISTINCT CASE WHEN vc.is_relevant=1 AND COALESCE(vr.delete_flagged,0)=0 THEN vr.id END) relevant,
    COUNT(DISTINCT CASE WHEN vc.set_aside_reason IS NOT NULL AND COALESCE(vr.delete_flagged,0)=0 THEN vr.id END) set_aside,
    COUNT(DISTINCT CASE WHEN COALESCE(vr.delete_flagged,0)=0 THEN vr.id END) total
  FROM mti_terms mt
  LEFT JOIN wa_verse_records vr ON vr.mti_term_id = mt.id
  LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id AND vc.mti_term_id = mt.id
  WHERE mt.cluster_code='M46' AND COALESCE(mt.delete_flagged,0)=0
  GROUP BY mt.id ORDER BY mt.strongs_number'''):
    totals['UT'] += r['ut']
    totals['relevant'] += r['relevant']
    totals['set_aside'] += r['set_aside']
    print(f"  mti={r['id']:<5} {r['strongs_number']:<8} {r['transliteration']:<14} {(r['gloss'] or '')[:22]:<22} total={r['total']:<4} UT={r['ut']:<4} relevant={r['relevant']:<4} set_aside={r['set_aside']}")

print()
print(f'=== Totals ===  UT={totals["UT"]}  relevant={totals["relevant"]}  set_aside={totals["set_aside"]}')
