"""
Collection-lexical GENERATOR (01b Part C, the term-scope layer).
For each owned term in a cluster, aggregates its per-verse ve_lexical (via
verse_context.mti_term_id) and DERIVES the collection items by mechanical rule,
writing them to `term_collection_lexical` (additive table). Idempotent per cluster
(R4): a --live run replaces the cluster's mechanical rows; researcher rows preserved.

Object_type is decided ONLY from per-verse-VARYING evidence (valence-variation,
how/object coverage, sense), NEVER from a lemma-constant alone (type/faculty are
used as DESCRIPTIVE inputs per Part C, with the discipline below). Low-confidence
calls are written UNRESOLVED (→ read), per R1.

Usage:
  python -X utf8 scripts\_apply_generate_collection_lexical_20260624.py --cluster M12 --dry-run
  python -X utf8 scripts\_apply_generate_collection_lexical_20260624.py --cluster M12 --live
"""
import sqlite3, os, argparse, re
from collections import Counter

DB=os.path.join('database','bible_research.db')
MODEL_VERSION='01b-PartC-v3'

DDL="""CREATE TABLE IF NOT EXISTS term_collection_lexical(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  mti_term_id INTEGER NOT NULL,
  cluster_code TEXT,
  ve_label TEXT NOT NULL,
  value TEXT,
  derivation TEXT,            -- mechanical | read | researcher
  model_version TEXT,
  source_ref TEXT,            -- evidence summary / source verse(s)
  notes TEXT,
  delete_flagged INTEGER DEFAULT 0,
  created_at TEXT
);"""

def agg_term(c, mti_term_id):
    """aggregate per-verse ve_lexical for one term."""
    rows=c.execute("""
      select vl.ve_label lbl, vl.value val
      from ve_lexical vl join verse_context vc on vc.id=vl.verse_context_id
      where vc.mti_term_id=? and coalesce(vl.delete_flagged,0)=0 and coalesce(vc.delete_flagged,0)=0
    """,(mti_term_id,)).fetchall()
    nverse=c.execute("""select count(distinct vc.id) n from verse_context vc
      where vc.mti_term_id=? and coalesce(vc.delete_flagged,0)=0""",(mti_term_id,)).fetchone()[0]
    d={'type':Counter(),'sense':Counter(),'valence':Counter(),'object-type':Counter(),
       'how':0,'object':0,'faculty':0,'experiencer':Counter(),'coseat_cluster':Counter()}
    for r in rows:
        lbl=r['lbl']; v=(r['val'] or '').strip()
        if lbl=='type': d['type'][v]+=1
        elif lbl=='sense': d['sense'][v]+=1
        elif lbl=='valence': d['valence'][v]+=1
        elif lbl=='object-type': d['object-type'][v]+=1
        elif lbl=='how': d['how']+=1
        elif lbl=='object': d['object']+=1
        elif lbl=='faculty': d['faculty']+=1
        elif lbl=='experiencer': d['experiencer'][v]+=1
        elif lbl=='compound':
            for m in re.findall(r'\((M\d+[a-z]?|T2|FLAG)\)', v): d['coseat_cluster'][m]+=1
    d['nverse']=nverse
    return d

def derive(d, self_cluster):
    """deterministic collection-item derivation from the aggregate."""
    n=max(d['nverse'],1)
    pos=(d['type'].most_common(1)[0][0] if d['type'] else None)
    vals=set(d['valence'])
    val_varies=len(vals)>1
    tot_val=sum(d['valence'].values()) or 1
    sinful_share=d['valence'].get('sinful',0)/tot_val
    forbidden_share=d['valence'].get('forbidden',0)/tot_val
    pos_share=sum(d['valence'].get(k,0) for k in ('righteous','commanded','neutral'))/tot_val
    # real bivalence = BOTH a sinful AND a positive register are meaningfully present (not a stray tag)
    real_bivalent=(sinful_share+forbidden_share)>=0.20 and pos_share>=0.20
    faculty_present=d['faculty']>0   # LEMMA-CONSTANT — used ONLY for the characteristic_candidate flag, NEVER to call object_type
    obj_cov=d['object']/n
    how_cov=d['how']/n
    person_share=(d['object-type'].get('person',0)/max(sum(d['object-type'].values()),1)) if d['object-type'] else 0
    # --- object_type (ordered, deterministic; from per-verse-VARYING evidence: POS-grammar + valence-variation; NOT faculty) ---
    conf='mechanical'
    # bivalent-FACULTY first (any POS): a faculty exercised + valence flips good/evil (the object/aim sets it).
    # Requires faculty engaged — a valence-varying STATE without a faculty (e.g. tum.ah uncleanness) is a
    # condition with a ritual/moral realm split, NOT a bivalent faculty.
    if real_bivalent and faculty_present:
        ot='bivalent-faculty'
    elif pos=='action':
        ot='expression'                       # an act; manner/binding fills it (characteristic-in-operation is a read promotion)
    elif pos in ('status','quality'):
        ot = 'state' if vals else 'UNRESOLVED'
    else:
        ot='UNRESOLVED'
    # characteristic is NOT auto-called from faculty (the validation trap). Instead flag a read-promotable CANDIDATE:
    # an intransitive disposition with an intrinsic faculty + a lived how-predicate.
    char_candidate = (ot in ('state','expression') and faculty_present and how_cov>=0.50 and obj_cov<0.35)
    # bivalence visible in valence but faculty untagged (faculty signal-list gap) → read promotes (bivalent-faculty) or confirms (realm-state / expression-counterfeit)
    biv_candidate = (ot!='bivalent-faculty' and real_bivalent and not faculty_present)
    items=[]
    sig=f"pos={pos};val={dict(d['valence'])};how_cov={how_cov:.2f};obj_cov={obj_cov:.2f};faculty={'Y' if faculty_present else 'N'};person_share={person_share:.2f};n={n}"
    items.append(('object_type', ot, 'mechanical', sig))
    if char_candidate:
        items.append(('characteristic_candidate', 'YES (confirm by read — intransitive disposition + intrinsic faculty + lived how-predicate)',
                      'mechanical', f"how_cov={how_cov:.2f};obj_cov={obj_cov:.2f};faculty=Y"))
    if biv_candidate:
        items.append(('bivalence_candidate', 'YES (valence flips good/evil; faculty untagged — read: promote to bivalent-faculty vs confirm realm-state/expression-counterfeit)',
                      'mechanical', f"sinful_share={sinful_share+forbidden_share:.2f};pos_share={pos_share:.2f};faculty=N"))
    items.append(('mutability', 'changeable' if val_varies else ('fixed' if vals else 'UNRESOLVED'),
                  'mechanical', f"valence distinct={len(vals)}"))
    items.append(('transitivity', 'transitive' if obj_cov>=0.40 else 'intransitive',
                  'mechanical', f"obj_cov={obj_cov:.2f}"))
    if ot=='bivalent-faculty':
        items.append(('membership_scope','per-occurrence','mechanical','bivalent → per-occurrence'))
        items.append(('valence_discriminator','object/aim sets valence','mechanical',f"valence={dict(d['valence'])}"))
    else:
        items.append(('membership_scope','lemma','mechanical','univalent'))
    if faculty_present:
        items.append(('faculty_intrinsic','present (collection-level; NOT a per-verse seat)','mechanical',f"faculty rows={d['faculty']}"))
    # pole hint: dominant co-seated OTHER cluster
    others=[(k,v) for k,v in d['coseat_cluster'].most_common() if k!=self_cluster]
    if others:
        items.append(('pole_relation_hint', f"top co-cluster {others[0][0]} (×{others[0][1]})",'mechanical',
                      f"co-clusters={dict(others[:5])}"))
    items.append(('valence_register', ','.join(f'{k}:{v}' for k,v in d['valence'].most_common()) or 'NONE','mechanical',''))
    return ot, conf, items

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--cluster',required=True)
    ap.add_argument('--live',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args(); live=a.live and not a.dry_run
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    c.execute(DDL)
    terms=c.execute("""select id,strongs_number s,transliteration t from mti_terms
        where cluster_code=? and coalesce(delete_flagged,0)=0
          and (status is null or status not in ('delete','candidate_delete','excluded'))
        order by strongs_number""",(a.cluster,)).fetchall()
    print(f'#### {a.cluster}: {len(terms)} owned terms · model {MODEL_VERSION} · {"LIVE" if live else "DRY-RUN"}\n')
    if live:
        c.execute("delete from term_collection_lexical where cluster_code=? and derivation='mechanical'",(a.cluster,))
    ot_tally=Counter(); written=0
    for tm in terms:
        d=agg_term(c, tm['id'])
        if not d['nverse']:
            print(f"  {tm['t']:<14} {tm['s']:<9} — 0 verses, skip"); continue
        ot,conf,items=derive(d, a.cluster)
        ot_tally[ot]+=1
        print(f"  {tm['t']:<14} {tm['s']:<9} n={d['nverse']:<4} → object_type={ot}")
        print(f"       {items[0][3]}")
        if live:
            for lbl,val,deriv,src in items:
                c.execute("""insert into term_collection_lexical
                  (mti_term_id,cluster_code,ve_label,value,derivation,model_version,source_ref,created_at)
                  values(?,?,?,?,?,?,?,datetime('now'))""",
                  (tm['id'],a.cluster,lbl,val,deriv,MODEL_VERSION,src))
                written+=1
    if live: c.commit()
    print(f"\n  object_type tally: {dict(ot_tally.most_common())}")
    print(f"  {'WROTE '+str(written)+' rows' if live else 'dry-run (no write)'}")
    c.close()

if __name__=='__main__': main()
