"""_exploratory_m10d_actual_verses_v1_20260605.py  (READ-ONLY)
Dump M10-D 'Guilt as inner-being state' verses for the VCG-redo test:
the ACTUAL verse texts + spans only (NO analysis_note meaning), in canonical order.
Existing VCG assignment is captured SEPARATELY (for post-hoc comparison only).
"""
import sqlite3, os
c = sqlite3.connect('database/bible_research.db'); c.row_factory = sqlite3.Row; cur = c.cursor()
OUT = os.path.join('research', 'investigations', 'm10d-actual-verses-input-20260605.md')

rows = cur.execute("""
 SELECT vc.id vcid, vc.is_anchor, g.group_code vcg,
        wr.reference ref, wr.book_id, wr.chapter, wr.verse_num,
        wr.target_word span, wr.term_id, mt.gloss, wr.verse_text
 FROM verse_context vc
 JOIN mti_terms mt ON mt.id=vc.mti_term_id
 JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id
 JOIN wa_verse_records wr ON wr.id=vc.verse_record_id
 LEFT JOIN verse_context_group g ON g.id=vc.group_id
 WHERE mt.cluster_code='M10' AND cs.subgroup_code='M10-D'
   AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
 ORDER BY wr.book_id, wr.chapter, wr.verse_num
""").fetchall()

# existing VCG tally (comparison only)
from collections import Counter, defaultdict
vcg_tally = Counter(r['vcg'] for r in rows)
vcg_members = defaultdict(list)
for r in rows:
    vcg_members[r['vcg']].append(r['ref'])

L = ['# M10-D "Guilt as inner-being state" — actual-verse input (VCG-redo test)', '',
     f'> Read-only, 2026-06-05. **{len(rows)} verses**, canonical order. ACTUAL verse text + span only —',
     '> **no stored meaning**, anchors not privileged. Group these by the **application of the term in',
     '> context**, then compare to the existing VCGs (listed at the bottom — do not read until after grouping).',
     '', '---', '', '## Verses (read these — form groups from the actual text)', '']
for i, r in enumerate(rows, 1):
    txt = (r['verse_text'] or '').strip()
    L.append(f"**{i}. {r['ref']}** — span: *{r['span']}* ({r['term_id']}, '{(r['gloss'] or '').strip()}')")
    L.append(f"> {txt}")
    L.append('')

L += ['---', '', '## (Comparison only — existing VCGs) ', '',
      f'{len(vcg_tally)} existing VCGs:', '']
for code, n in vcg_tally.most_common():
    L.append(f'- **{code}** ({n}): {", ".join(vcg_members[code][:40])}')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(f'verses={len(rows)} existing_VCGs={len(vcg_tally)} anchors={sum(r["is_anchor"] or 0 for r in rows)}')
print('wrote', OUT)
