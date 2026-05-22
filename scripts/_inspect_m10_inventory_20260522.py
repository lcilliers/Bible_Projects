"""Read-only inventory of M10 OWNER terms grouped by home registry.

Uses a single GROUP BY join instead of 88 correlated subqueries so it actually
finishes — there's no index on wa_verse_records.mti_term_id.
"""
import sqlite3, os
from collections import defaultdict

OUT = 'outputs/markdown/_tmp_m10_inventory_20260522.txt'
os.makedirs('outputs/markdown', exist_ok=True)

conn = sqlite3.connect('file:database/bible_research.db?mode=ro', uri=True, timeout=10.0)
cur = conn.cursor()

# 1. Get M10 OWNER terms
terms = cur.execute("""
SELECT mt.id, mt.transliteration, mt.strongs_number, wr.no, wr.word
FROM mti_terms mt
JOIN word_registry wr ON wr.id = mt.owning_registry_fk
WHERE mt.cluster_code='M10' AND COALESCE(mt.delete_flagged,0)=0
ORDER BY wr.no, mt.transliteration
""").fetchall()

term_ids = [t[0] for t in terms]
placeholders = ','.join('?' * len(term_ids))

# 2. Get verse counts in one query
vc_rows = cur.execute(f"""
SELECT mti_term_id, COUNT(*) FROM wa_verse_records
WHERE mti_term_id IN ({placeholders})
  AND COALESCE(delete_flagged,0)=0
GROUP BY mti_term_id
""", term_ids).fetchall()
vc = {r[0]: r[1] for r in vc_rows}

lines = [f'TOTAL OWNER TERMS: {len(terms)}']
g = defaultdict(list)
for t in terms:
    g[(t[3], t[4])].append(t)
lines.append(f'REGISTRIES: {len(g)}')
lines.append('')
for k in sorted(g.keys()):
    rn, rw = k
    ts = g[k]
    tot = sum(vc.get(t[0], 0) for t in ts)
    lines.append(f'R{rn:03d} {rw} | terms={len(ts)} V={tot}')
    for t in ts:
        lemma = (t[1] or '')
        lines.append(f'  id={t[0]:5d} {t[2]:10s} {lemma:<28s} V={vc.get(t[0], 0)}')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('wrote', OUT, len(terms), 'rows', len(g), 'registries')
conn.close()
