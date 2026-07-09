"""
TERM-PAIR BINDING prototype (read-only) — the inter-term operation layer.
The per-term signature is single-term; THIS surfaces where two primary terms
(e.g. grace + mercy) operate TOGETHER in a verse, and characterises the binding
mechanically from morphology (coordinate / governed / adjacent / same-clause / distant).

  python -X utf8 scripts/_explore_term_pair_binding_v1_20260627.py --a grace --b mercy
  (--a/--b are registry words; or --astrong/--bstrong comma Strong's)
Output: outputs/markdown/validation/wa-term-pair-binding-<A>-<B>-<date>.md
"""
import sqlite3, os, re, argparse
from collections import defaultdict, Counter
DB=os.path.join('database','bible_research.db')

def canon(s):
    m=re.match(r'^([HG])(\d+)',(s or '').strip().upper()); return f'{m.group(1)}{int(m.group(2)):04d}' if m else None

def family(c, word, strong):
    if strong: return set(canon(s) for s in strong.split(','))
    reg=c.execute("SELECT id FROM word_registry WHERE lower(word)=? LIMIT 1",(word.lower(),)).fetchone()
    if not reg: return set()
    return set(re.sub(r'[A-Z]$','',canon(r['s'])) for r in
               c.execute("SELECT strongs_number s FROM mti_terms WHERE owning_registry_fk=? AND COALESCE(delete_flagged,0)=0",(reg['id'],)))

def is_conj(morph, strong):
    m=(morph or ''); s=canon(strong)
    return m.startswith('HC') or ' HC' in (' '+m) or m=='CONJ' or s=='G2532'  # waw / kai
def is_genitive_or_construct(morph):
    m=(morph or '')
    if m.startswith('H') and m.split()[0].rstrip().endswith('c'): return True   # Hebrew construct
    if not m.startswith('H'):
        p=m.split('-');  return len(p)>1 and p[1].startswith('G')               # Greek genitive
    return False

def classify(spans_between, gap, ma, mb):
    conj = any(is_conj(m,s) for (_,m,s) in spans_between)
    gov  = is_genitive_or_construct(ma) or is_genitive_or_construct(mb)
    if conj and gap<=4: return 'COORDINATE (A and B — paired)'
    if gov: return 'GOVERNED (one qualifies/possesses the other)'
    if gap<=2: return 'ADJACENT (tight, no conjunction)'
    if gap<=6: return 'SAME-CLAUSE (related, looser)'
    return 'DISTANT (likely separate clauses/context)'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--a'); ap.add_argument('--b'); ap.add_argument('--astrong'); ap.add_argument('--bstrong')
    args=ap.parse_args()
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    A=family(c,args.a,args.astrong); B=family(c,args.b,args.bstrong)
    alabel=args.a or args.astrong; blabel=args.b or args.bstrong
    print(f'A({alabel})={len(A)} terms; B({blabel})={len(B)} terms')
    # all spans grouped by verse
    byv=defaultdict(list)
    for r in c.execute('SELECT verse_id, reference, word_index, surface, morph_code, primary_strong FROM verse_span_index'):
        byv[(r['verse_id'],r['reference'])].append(dict(r))
    rows=[]; pat=Counter()
    for (vid,ref),spans in byv.items():
        spans.sort(key=lambda x:x['word_index'])
        aS=[s for s in spans if canon(s['primary_strong']) in A]
        bS=[s for s in spans if canon(s['primary_strong']) in B]
        if not aS or not bS: continue
        # closest A,B pair
        best=None
        for sa in aS:
            for sb in bS:
                g=abs(sa['word_index']-sb['word_index'])
                if best is None or g<best[0]: best=(g,sa,sb)
        g,sa,sb=best
        lo,hi=sorted([sa['word_index'],sb['word_index']])
        between=[(s['surface'],s['morph_code'],s['primary_strong']) for s in spans if lo<s['word_index']<hi]
        cl=classify(between,g,sa['morph_code'],sb['morph_code'])
        pat[cl]+=1
        rows.append((ref,sa['surface'],sb['surface'],g,cl))
    print(f'co-occurrence verses: {len(rows)}')
    out=[f'# Term-pair binding — {alabel} × {blabel}','',
         f'- File: wa-term-pair-binding-{alabel}-{blabel}-20260627.md · read-only · the inter-term operation layer.',
         f'- A({alabel}) terms: {sorted(A)}', f'- B({blabel}) terms: {sorted(B)}','',
         f'**Co-occurrence verses: {len(rows)}**','','## Binding pattern distribution','',
         '| pattern | verses |','|---|---:|']
    for p,n in pat.most_common(): out.append(f'| {p} | {n} |')
    out.append(''); out.append('## Sample co-occurrences')
    out.append('| reference | A | B | gap | binding |'); out.append('|---|---|---|---:|---|')
    for r in sorted(rows, key=lambda x:x[3])[:30]:
        out.append(f'| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |')
    os.makedirs('outputs/markdown/validation',exist_ok=True)
    p=f'outputs/markdown/validation/wa-term-pair-binding-{alabel}-{blabel}-20260627.md'
    open(p,'w',encoding='utf-8').write('\n'.join(out)); print('wrote',p)
    for k,n in pat.most_common(): print(f'   {n:>4}  {k}')
    c.close()

if __name__=='__main__': main()
