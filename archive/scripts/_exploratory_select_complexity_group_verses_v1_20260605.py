"""_exploratory_select_complexity_group_verses_v1_20260605.py  (READ-ONLY)
Find one representative M01 verse in each of the 4 complexity groups:
  possible-set-aside | single-span | T2+T1 | multi-T1
"""
import sqlite3
c = sqlite3.connect('database/bible_research.db'); c.row_factory = sqlite3.Row; cur = c.cursor()
named = {r['cluster_code'] for r in cur.execute("SELECT cluster_code FROM cluster WHERE bucket='NAMED'")}

# M01 verses + whether the M01 span(s) is_relevant
m01 = {}
for r in cur.execute('''
  SELECT wr.book_id b, wr.chapter ch, wr.verse_num v, MAX(vc.is_relevant) any_rel, wr.reference ref
  FROM verse_context vc JOIN wa_verse_records wr ON wr.id=vc.verse_record_id
  JOIN mti_terms mt ON mt.id=vc.mti_term_id
  WHERE mt.cluster_code='M01' AND COALESCE(vc.delete_flagged,0)=0
  GROUP BY wr.book_id,wr.chapter,wr.verse_num'''):
    m01[(r['b'],r['ch'],r['v'])] = {'rel': r['any_rel'], 'ref': r['ref']}

# all spans per verse -> bucket tallies
from collections import defaultdict
spans = defaultdict(lambda: {'total':0,'namedOther':set(),'t2':0,'flag':0})
for r in cur.execute('''SELECT wr.book_id b,wr.chapter ch,wr.verse_num v, TRIM(mt.cluster_code) cc
  FROM wa_verse_records wr JOIN mti_terms mt ON mt.id=wr.mti_term_id
  WHERE COALESCE(wr.delete_flagged,0)=0 AND COALESCE(TRIM(mt.cluster_code),'')<>'' '''):
    k=(r['b'],r['ch'],r['v']); s=spans[k]; s['total']+=1
    if r['cc']=='T2': s['t2']+=1
    elif r['cc']=='FLAG': s['flag']+=1
    elif r['cc'] in named and r['cc']!='M01': s['namedOther'].add(r['cc'])

groups={'set_aside':[], 'single':[], 't2t1':[], 'multi':[]}
for k,info in m01.items():
    s=spans[k]
    if info['rel']==0: groups['set_aside'].append((k,info,s))
    elif s['total']==1: groups['single'].append((k,info,s))
    elif not s['namedOther'] and s['t2']>=1: groups['t2t1'].append((k,info,s))
    elif len(s['namedOther'])>=1: groups['multi'].append((k,info,s))

for g,items in groups.items():
    print(f'=== {g}: {len(items)} M01 verses ===')
    # show a few candidates, prefer moderate span counts for readability
    items.sort(key=lambda x: (len(x[2]['namedOther']), x[2]['total']))
    for k,info,s in items[:4]:
        print(f"   {info['ref']:14s} total_spans={s['total']} otherT1={sorted(s['namedOther'])} t2={s['t2']} flag={s['flag']} rel={info['rel']}")
    print()
