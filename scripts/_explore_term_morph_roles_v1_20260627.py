"""
TERM MORPHOLOGICAL-ROLE SIGNATURE  (read-only, reusable)
=========================================================
Method (researcher 2026-06-27): the TERM is shared across verses; each SPAN
instantiates one morphology. So for any term, pull all its spans, group by
distinct morphology, and decode each morphology to the grammatical ROLE/relation
it signals. This is the SHARED term-level layer that feeds the per-span meaning graph.

  Greek: CASE = role          (Nom=agent/subject · Acc=object/patient · Gen=source/of · Dat=recipient/means · Voc=address)
  Greek: VOICE/MOOD           (active/middle/passive ; indicative/infinitive=purpose/participle…)
  Hebrew: STATE               (absolute=stands alone · construct="X of"=bound)
  Hebrew: STEM (verbs)        (Qal=simple · Niphal=passive/reflexive · Piel=intensive · Hiphil=CAUSATIVE · …)

Usage:
  python -X utf8 scripts/_explore_term_morph_roles_v1_20260627.py --strong G5485
  python -X utf8 scripts/_explore_term_morph_roles_v1_20260627.py --strong H2580,H2603
  python -X utf8 scripts/_explore_term_morph_roles_v1_20260627.py --word grace
Output: outputs/markdown/validation/wa-term-morph-roles-<key>-<date>.md  (+ console)
"""
import sqlite3, os, re, argparse
DB=os.path.join('database','bible_research.db')

GK_CASE={'N':'Nominative → subject/AGENT','G':'Genitive → source/of/possession','D':'Dative → recipient/INSTRUMENT/means','A':'Accusative → OBJECT/patient','V':'Vocative → address'}
GK_VOICE={'A':'active','M':'middle','P':'passive','E':'middle/passive','D':'middle-deponent','O':'passive-deponent','N':'middle/passive-deponent'}
GK_MOOD={'I':'indicative','M':'imperative','S':'subjunctive','O':'optative','N':'infinitive (often purpose/complement)','P':'participle (backgrounded/attributive)'}
GK_TENSE={'P':'present','I':'imperfect','F':'future','A':'aorist','X':'perfect','Y':'pluperfect','R':'perfect'}
GK_POS={'N':'noun','A':'adjective','V':'verb','R':'rel.pronoun','C':'conjunction','D':'demonstr.','T':'article','P':'pronoun','F':'reflexive','Q':'interrog./correl.','PREP':'preposition','ADV':'adverb','CONJ':'conjunction','X':'particle','I':'interjection'}
HE_TYPE={'N':'noun','V':'verb','A':'adjective','R':'preposition','C':'conjunction','T':'particle','S':'suffix','P':'pronoun','D':'adverb'}
HE_STATE={'a':'absolute (stands alone)','c':'construct ("X of…" — bound)','d':'determined'}
HE_STEM={'q':'Qal (simple action)','N':'Niphal (passive/reflexive)','p':'Piel (intensive/factitive)','P':'Pual (passive of Piel)','h':'Hiphil (CAUSATIVE)','H':'Hophal (passive causative)','t':'Hithpael (reflexive/iterative)','v':'Qal passive'}

def decode(morph):
    """Decode the term's OWN (first) morphology token to a role hint."""
    if not morph: return '(no morph)'
    first=morph.split()[0]
    if first.startswith('H'):  # Hebrew
        body=first[1:]
        t=body[0] if body else '?'
        if t=='N':  # noun: ...last letter = state
            st=HE_STATE.get(body[-1],'')
            return f'Hebrew noun · {st}'
        if t=='V':
            stem=HE_STEM.get(body[1],'?stem') if len(body)>1 else '?'
            return f'Hebrew verb · {stem}'
        if t=='A': return 'Hebrew adjective (qualifier)'
        if t in ('R','C','T','S'): return f'Hebrew {HE_TYPE.get(t,t)} (relation/edge marker)'
        return f'Hebrew {HE_TYPE.get(t,t)}'
    else:  # Greek
        if first in ('PREP','ADV','CONJ'): return f'Greek {GK_POS.get(first,first)} (relation/edge marker)'
        parts=first.split('-')
        pos=GK_POS.get(parts[0][0],parts[0]) if parts else '?'
        feats=parts[1] if len(parts)>1 else ''
        if parts[0][0] in ('N','A','R','D','T','P','F') and feats:
            case=GK_CASE.get(feats[0],'')
            return f'Greek {pos} · {case}'
        if parts[0][0]=='V' and feats:
            tense=GK_TENSE.get(feats[0],''); voice=GK_VOICE.get(feats[1],'') if len(feats)>1 else ''; mood=GK_MOOD.get(feats[2],'') if len(feats)>2 else ''
            return f'Greek verb · {tense} {voice} {mood}'.replace('  ',' ').strip()
        return f'Greek {pos}'

def role_axis(morph):
    """Collapse a morphology to its ROLE-RELEVANT axis (the repertoire key):
       Greek nominal -> case ; Greek verb -> voice+mood ; Hebrew noun -> state ; Hebrew verb -> STEM."""
    if not morph: return ('?','(none)')
    first=morph.split()[0]
    if first.startswith('H'):
        body=first[1:]; t=body[0] if body else '?'
        if t=='N': return ('state', HE_STATE.get(body[-1],body[-1]))
        if t=='V': return ('stem', HE_STEM.get(body[1],body[1]) if len(body)>1 else '?')
        if t=='A': return ('pos','adjective')
        if t in ('R','C','T','S'): return ('edge', HE_TYPE.get(t,t)+' (edge marker)')
        return ('pos', HE_TYPE.get(t,t))
    else:
        if first in ('PREP','ADV','CONJ'): return ('edge', GK_POS.get(first,first)+' (edge marker)')
        parts=first.split('-'); feats=parts[1] if len(parts)>1 else ''
        if parts[0][0] in ('N','A','R','D','T','P','F') and feats: return ('case', GK_CASE.get(feats[0],feats[0]))
        if parts[0][0]=='V' and feats:
            voice=GK_VOICE.get(feats[1],'') if len(feats)>1 else ''; mood=GK_MOOD.get(feats[2],'') if len(feats)>2 else ''
            return ('voice/mood', f'{voice} {mood}'.strip())
        return ('pos', GK_POS.get(parts[0][0],parts[0]))

def resolve(c, args):
    if args.strong:
        return [s.strip().upper() for s in args.strong.split(',')]
    # --word : study-term strongs whose gloss/translit matches
    w=args.word.lower()
    rows=c.execute("""SELECT DISTINCT m.strongs_number s FROM mti_terms m JOIN lexicon l ON
        REPLACE(REPLACE(l.strong,'H0','H'),'G0','G')=REPLACE(REPLACE(m.strongs_number,'H0','H'),'G0','G')
        WHERE (lower(l.gloss) LIKE ? OR lower(l.transliteration) LIKE ?)
          AND m.cluster_code IS NOT NULL AND COALESCE(m.delete_flagged,0)=0""",(f'%{w}%',f'%{w}%')).fetchall()
    return sorted(set(re.sub(r'[A-Z]$','',r['s']) for r in rows))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--strong'); ap.add_argument('--word')
    a=ap.parse_args()
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    strongs=resolve(c,a)
    key=(a.strong or a.word or 'term').replace(',','_').replace(' ','-')
    out=[f'# Term morphological-role signature — {a.strong or a.word}', '',
         f'- File: wa-term-morph-roles-{key}-20260627.md · read-only · method: shared-term → unique-morphologies → role repertoire.','']
    for base in strongs:
        # match any sub-letter of this base (e.g. H2580, H2580A)
        rows=c.execute("""SELECT primary_strong, morph_code, COUNT(*) n, MIN(reference) sample
                          FROM verse_span_index WHERE primary_strong=? GROUP BY morph_code ORDER BY n DESC""",(base,)).fetchall()
        if not rows: continue
        lex=c.execute("SELECT gloss, transliteration FROM lexicon WHERE strong LIKE ? LIMIT 1",(base+'%',)).fetchone()
        tot=sum(r['n'] for r in rows)
        out.append(f"## {base} — {lex['transliteration'] if lex else ''} \"{lex['gloss'] if lex else ''}\"")
        out.append(f"- **{tot} spans · {len(rows)} distinct morphologies**")
        out.append('')
        # ROLE REPERTOIRE — collapse to the role-relevant axis
        from collections import defaultdict
        rep=defaultdict(int)
        for r in rows:
            ax,val=role_axis(r['morph_code']); rep[(ax,val)]+=r['n']
        out.append('**Role repertoire** (collapsed to the role-relevant axis — case for nominals, stem for Hebrew verbs):')
        out.append('')
        out.append('| axis | value | spans |')
        out.append('|---|---|---:|')
        for (ax,val),n in sorted(rep.items(), key=lambda kv:-kv[1]):
            out.append(f'| {ax} | {val} | {n} |')
        out.append('')
        out.append('<details><summary>full distinct morphologies</summary>')
        out.append('')
        out.append('| morphology | count | e.g. | role / relation it signals |')
        out.append('|---|---:|---|---|')
        for r in rows:
            out.append(f"| `{r['morph_code'] or '-'}` | {r['n']} | {r['sample']} | {decode(r['morph_code'])} |")
        out.append('')
        out.append('</details>')
        out.append('')
        print(f"{base} {lex['transliteration'] if lex else ''}: {tot} spans, {len(rows)} morphologies")
    os.makedirs('outputs/markdown/validation',exist_ok=True)
    p=f'outputs/markdown/validation/wa-term-morph-roles-{key}-20260627.md'
    open(p,'w',encoding='utf-8').write('\n'.join(out)); print('wrote',p)
    c.close()

if __name__=='__main__': main()
