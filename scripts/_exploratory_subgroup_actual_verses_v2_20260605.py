"""_exploratory_subgroup_actual_verses_v2_20260605.py  (READ-ONLY)
Generic: dump a sub-group's verses for a VCG-redo test — ACTUAL verse texts + spans only
(NO analysis_note meaning), canonical order. Existing VCGs listed separately (comparison only).
Usage: python ... --cluster M10 --subgroup M10-H
"""
import sqlite3, os, argparse
ap = argparse.ArgumentParser()
ap.add_argument('--cluster', required=True)
ap.add_argument('--subgroup', required=True)
a = ap.parse_args()

c = sqlite3.connect('database/bible_research.db'); c.row_factory = sqlite3.Row; cur = c.cursor()
OUT = os.path.join('research', 'investigations',
                   f'{a.subgroup.lower()}-actual-verses-input-20260605.md')

label = cur.execute("SELECT label FROM cluster_subgroup WHERE subgroup_code=? AND cluster_code=?",
                    (a.subgroup, a.cluster)).fetchone()
label = label['label'] if label else a.subgroup

rows = cur.execute("""
 SELECT vc.is_anchor, g.group_code vcg, wr.reference ref, wr.book_id, wr.chapter, wr.verse_num,
        wr.target_word span, wr.term_id, mt.gloss, wr.verse_text
 FROM verse_context vc
 JOIN mti_terms mt ON mt.id=vc.mti_term_id
 JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id
 JOIN wa_verse_records wr ON wr.id=vc.verse_record_id
 LEFT JOIN verse_context_group g ON g.id=vc.group_id
 WHERE mt.cluster_code=? AND cs.subgroup_code=?
   AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
 ORDER BY wr.book_id, wr.chapter, wr.verse_num
""", (a.cluster, a.subgroup)).fetchall()

from collections import Counter, defaultdict
tally = Counter(r['vcg'] for r in rows)
members = defaultdict(list)
for r in rows:
    members[r['vcg']].append(r['ref'])

L = [f'# {a.subgroup} "{label}" — actual-verse input (VCG-redo test)', '',
     f'> Read-only, 2026-06-05. **{len(rows)} verses**, canonical order. ACTUAL verse text + span only —',
     '> no stored meaning, anchors not privileged. Group by the application of the term in context.', '',
     '---', '', '## Verses', '']
for i, r in enumerate(rows, 1):
    L.append(f"**{i}. {r['ref']}** — span: *{r['span']}* ({r['term_id']}, '{(r['gloss'] or '').strip()}')")
    L.append(f"> {(r['verse_text'] or '').strip()}")
    L.append('')
L += ['---', '', f'## (Comparison only) {len(tally)} existing VCGs', '']
for code, n in tally.most_common():
    L.append(f'- **{code}** ({n}): {", ".join(members[code][:50])}')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
# distinct terms (is the sense lexically pre-split?)
terms = Counter((r['term_id'], (r['gloss'] or '').strip()) for r in rows)
print(f'{a.subgroup} verses={len(rows)} VCGs={len(tally)} distinct_terms={len(terms)}')
for (t, g), n in terms.most_common(10):
    print(f'  {t:8s} {g[:24]:24s} {n}')
print('wrote', OUT)
