"""
DRY-RUN (read-only): verse-grounded FACULTY reset per the researcher's rule
(2026-06-26): faculty appears on a verse ONLY if explicitly mentioned / inferred
ON THE VERSE, never via the lemma.

Mechanism = repurpose lemma_faculty_map (map-batch*.json) as a "which words carry
which faculty" lexicon, then read each VERSE's own word inventory (verse_morphology):

  - 815 lemmas carry NO faculty (conduct/quality)  -> contribute nothing
  - 751 MONOVALENT lemmas (exactly 1 faculty)      -> that faculty is explicit when the word is in the verse
  -  ~10 POLYVALENT SEATS (heart/spirit, 3-6 facs) -> contribute NOTHING on their own (this is the over-fire we kill)

Two variants for the unit's faculty (the genuine fork):
  A (term-only, tightest): the ANALYSED term's own faculty, but ONLY if that term is monovalent.
                           Seats + polyvalent + none -> EMPTY. (most conservative; seats deferred to inferred/depth)
  B (verse-scan):          A, PLUS any MONOVALENT faculty contributed by OTHER words present in the same verse
                           (so a seat inherits a faculty when the verse explicitly specifies one). Reads the verse;
                           cost = cross-word binding is not proven (ceiling).

Writes nothing. Emits a report to outputs/markdown/validation/ + prints sample verses.
"""
import sqlite3, os, json, glob, re
from collections import defaultdict, Counter

DB=os.path.join('database','bible_research.db')
MAPDIR='research/VE-lexical/faculty-map-build'

def canon(s):
    """H430 / H0430 / H3820A -> H0430 / H3820A  (zero-pad numeric to 4, keep trailing letter)."""
    if not s: return None
    s=s.strip().upper()
    m=re.match(r'^([HG])(\d+)([A-Z]?)$', s)
    if not m: return None
    L,num,suf=m.groups()
    return f'{L}{int(num):04d}{suf}'

def load_map():
    """Return {canon_strongs: [faculties]} for both suffixed and base keys."""
    fac={}
    for f in sorted(glob.glob(f'{MAPDIR}/map-batch*.json')):
        for r in json.load(open(f,encoding='utf-8')):
            ck=canon(r['s'])
            if ck: fac[ck]=r.get('faculty') or []
    return fac

def faculties_of(strong, FAC):
    """Look up a strong in the map, trying suffixed then base form."""
    ck=canon(strong)
    if ck is None: return []
    if ck in FAC: return FAC[ck]
    base=re.sub(r'[A-Z]$','',ck)  # drop suffix letter
    return FAC.get(base, [])

def main():
    FAC=load_map()
    mono={k:v[0] for k,v in FAC.items() if len(v)==1}
    poly={k:v for k,v in FAC.items() if len(v)>=2}
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row

    # units to (re)compute: clustered, non-deleted inner-being terms-in-verse
    units=c.execute("""
      SELECT vc.id vcid, vr.verse_id vid, m.strongs_number s,
             m.transliteration tr, vr.reference ref
      FROM verse_context vc
      JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
      JOIN mti_terms m ON m.id = vc.mti_term_id
      WHERE m.cluster_code IS NOT NULL
        AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(m.delete_flagged,0)=0
        AND (m.status IS NULL OR m.status NOT IN ('delete','candidate_delete','excluded'))
        AND vr.verse_id IS NOT NULL
    """).fetchall()

    # per-verse monovalent faculties present (for variant B), from full verse word inventory
    verse_mono=defaultdict(set)
    for r in c.execute("SELECT verse_id, strongs FROM verse_morphology WHERE strongs IS NOT NULL"):
        for tok in (r['strongs'] or '').split():
            f=faculties_of(tok, FAC)
            if len(f)==1: verse_mono[r['verse_id']].add(f[0])

    # current faculty per unit (the lemma-derived rows we'd replace)
    cur=defaultdict(set)
    for r in c.execute("SELECT verse_context_id v, value val FROM ve_lexical WHERE ve_label='faculty' AND COALESCE(delete_flagged,0)=0"):
        cur[r['v']].add(r['val'])

    # verse faculty-profile (variant C): union of faculties of genuine FACULTY-WORDS (1-3 facs) present in the verse
    SEAT_MIN=4   # >=4 faculties == over-firing seat (empirically the 8 heart/spirit lemmas)
    verse_profile=defaultdict(set)
    for r in c.execute("SELECT verse_id, strongs FROM verse_morphology WHERE strongs IS NOT NULL"):
        for tok in (r['strongs'] or '').split():
            f=faculties_of(tok, FAC)
            if 1<=len(f)<=3: verse_profile[r['verse_id']].update(f)

    A=defaultdict(set); B=defaultdict(set); C=defaultdict(set)
    for u in units:
        own=faculties_of(u['s'], FAC)
        # A: term-only, monovalent
        A[u['vcid']]=set([own[0]]) if len(own)==1 else set()
        # B: A + any co-present monovalent faculty (noisy)
        B[u['vcid']]=set(A[u['vcid']]) | verse_mono.get(u['vid'], set())
        # C: faculty-word (1-3) carries own; seat (>=4) inherits verse faculty-profile; none -> empty
        if 1<=len(own)<=3:
            C[u['vcid']]=set(own)
        elif len(own)>=SEAT_MIN:
            C[u['vcid']]=set(verse_profile.get(u['vid'], set()))
        else:
            C[u['vcid']]=set()

    def stats(D):
        nfac=sum(1 for u in units if D[u['vcid']])
        perunit=Counter(len(D[u['vcid']]) for u in units)
        valdist=Counter(f for u in units for f in D[u['vcid']])
        return nfac, perunit, valdist

    nA,puA,vdA=stats(A); nB,puB,vdB=stats(B); nC,puC,vdC=stats(C)
    curn=sum(1 for u in units if cur.get(u['vcid']))
    curpu=Counter(len(cur.get(u['vcid'],set())) for u in units)

    out=[]
    out.append('# Faculty reset — dry-run (verse-grounded) — variants A & B')
    out.append('')
    out.append(f'- **File:** wa-faculty-reset-dryrun-v1-20260626.md · read-only, no DB write.')
    out.append(f'- Map: {len(FAC)} lemmas ({len(mono)} monovalent, {len(poly)} polyvalent seats, {sum(1 for v in FAC.values() if not v)} no-faculty).')
    out.append(f'- Units in scope (clustered, non-deleted): **{len(units)}**.')
    out.append('')
    out.append('## Coverage / over-fire comparison')
    out.append('')
    out.append('| metric | CURRENT (lemma) | A (term-only) | B (verse-scan) | C (faculty-word + seat-inherit) |')
    out.append('|--------|----------------:|--------------:|---------------:|--------------------------------:|')
    out.append(f'| units carrying a faculty | {curn} | {nA} | {nB} | {nC} |')
    for k in sorted(set(list(curpu)+list(puA)+list(puB)+list(puC))):
        out.append(f'| units with {k} faculties | {curpu.get(k,0)} | {puA.get(k,0)} | {puB.get(k,0)} | {puC.get(k,0)} |')
    out.append('')
    out.append(f'- max faculties/unit — CURRENT={max(curpu)} A={max(puA)} B={max(puB)} C={max(puC)}')
    out.append(f'- A value distribution: {dict(vdA.most_common())}')
    out.append(f'- B value distribution: {dict(vdB.most_common())}')
    out.append(f'- C value distribution: {dict(vdC.most_common())}')
    out.append('')
    out.append('## Sample verses (the diagnostic cases)')
    out.append('')
    want=['Mat 5:8','Heb 9:14','Eze 36:25','Gen 6:5','Deu 6:5','Psa 51:10']
    seen=set()
    for u in units:
        ref=(u['ref'] or '')
        if any(ref.startswith(w) for w in want) and (ref,u['s']) not in seen:
            seen.add((ref,u['s']))
            out.append(f"- **{ref}** {u['tr']} ({u['s']}) — own={faculties_of(u['s'],FAC)} | "
                       f"CURRENT={sorted(cur.get(u['vcid'],set()))} | A={sorted(A[u['vcid']])} | B={sorted(B[u['vcid']])} | **C={sorted(C[u['vcid']])}**")
    out.append('')
    out.append('## Note')
    out.append('- A is fully defensible (every value = a monovalent word explicitly in the verse). Seats end EMPTY (their faculty is a reading = inferred = deferred).')
    out.append('- B rescues seats by reading the verse, but attributes any co-present monovalent faculty to the unit without proving binding (ceiling). Higher coverage, some noise.')
    txt='\n'.join(out)
    p='outputs/markdown/validation/wa-faculty-reset-dryrun-v1-20260626.md'
    open(p,'w',encoding='utf-8').write(txt)
    print(txt)
    print('\nwrote',p)
    c.close()

if __name__=='__main__': main()
