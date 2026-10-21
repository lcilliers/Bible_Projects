"""Gate-1 orphan onboarding orchestrator (Group C — clean adds to existing/new registries).

Per registry: word_study_extract --anchors -> auto-curate terms array to the intended
strong(s) -> audit_word --add-terms -> stamp anchor_note='gate1-onboard-2026' -> set
cluster_code -> create verse_context. Continues past any term it cannot auto-resolve
(sub-entry ambiguity / missing), logging it for manual handling.

Group A (mti-reconcile) and Group B (XREF->OWNER promotion) are NOT handled here.

Usage:
  python scripts/_run_gate1_onboard_batch_v1_20260706.py --clusters M03,M12    # a cluster batch
  python scripts/_run_gate1_onboard_batch_v1_20260706.py --registries wisdom   # one registry
  python scripts/_run_gate1_onboard_batch_v1_20260706.py --list                # show worklist
Add --dry-curate to only extract+curate (no DB writes) and report match resolution.
"""
import sqlite3, json, argparse, os, subprocess, glob, sys

LIVE = 'database/bible_research.db'
STAMP = 'gate1-onboard-2026'
LEDGER = 'outputs/integrity/gate1_onboard_ledger.jsonl'
ENV = {**os.environ, 'PYTHONUTF8': '1'}

# Group C worklist: strong -> (registry_word, cluster_code_or_None). Qualifier/uncertain -> None cluster.
WORK = {
 # M03 Grief
 'H2427':('agony','M03'),'H2342':('anguish','M03'),'H8428':('grief','M03'),'H7908':('mourning','M03'),'H3642':('longing','M29'),
 # M20 Doubt/betrayal
 'H5800':('betrayal','M20'),'H5640':('doubt',None),'H5641':('doubt','M20'),'H7279':('doubt','M20'),
 # M10 sin/defilement
 'H2556':('bitterness',None),'H5003':('whoredom','M10'),'H2149':('wickedness','M10'),'H2555':('wickedness','M27'),
 'H6231':('wickedness',None),'H8496':('wickedness',None),
 # M39 blessing
 'H0835':('blessing','M39'),
 # M08 pride/contempt
 'H3887':('contempt','M08'),'H3932':('contempt','M08'),'H3933':('contempt','M08'),'H7047':('contempt','M08'),
 'H6277':('pride','M08'),'H7342':('pride',None),'H7426':('pride','M08'),
 # M46 abundance
 'H7646':('contentment','M46'),
 # M11 repentance
 'H1793':('contrition','M11'),
 # M29 desire
 'H1214':('covetousness','M29'),'H6770':('craving','M29'),'H6165':('longing','M29'),'H8373':('longing','M29'),
 'H3368':('worth','M29'),'H3365':('worth','M29'),
 # M14 deceit
 'H2665':('deceit','M14'),'H3576':('deceit','M14'),'H3577':('deceit','M14'),'H6601':('deceit',None),'H7723':('deceit','M14'),
 'H6141':('perverseness','M14'),'H2611':('hypocrisy',None),
 # M04 joy
 'H6149':('delight','M04'),'H5937':('rejoicing','M04'),'H5970':('rejoicing','M04'),
 # M30 obedience
 'H7683':('disobedience','M30'),'H7686':('disobedience','M30'),'H8582':('disobedience','M30'),
 'H5341':('obedience','M30'),'H4784':('rebellion','M30'),
 # M24 weakness / distress
 'H6323':('distress',None),'H6817':('distress',None),
 'H0536':('weakness','M24'),'H2489':('weakness','M24'),'H3021':('weakness','M24'),'H5848':('weakness','M24'),
 'H6199':('weakness','M24'),'H7326':('weakness','M24'),
 # M16 folly / M42 speech
 'H0981':('foolishness',None),'H6612':('foolishness','M16'),
 'H5046':('testimony','M42'),'H1747':('peace',None),
 # M09 humility
 'H8217':('humility','M09'),
 # M12 purity
 'H1249':('purity','M12'),'H1252':('purity','M12'),'H1305':('purity','M12'),'H2135':('purity','M12'),
 # M22 praise
 'H7321':('praise','M22'),
 # M06 rejection / hate
 'H2186':('rejection','M06'),'H3988':('rejection','M06'),'H5010':('rejection','M06'),
 'H7853':('strife','M06'),'H7854':('spiritual powers',None),'H7283':('strife',None),
 # M35 testing
 'H0974':('temptation','M35'),'H5254':('temptation','M35'),
 # M01 fear
 'H1161':('terror','M01'),
 # M15 wisdom
 'H4148':('wisdom','M15'),
 # M02 anger
 'H5359':('wrath','M02'),'H5360':('wrath','M02'),
 # ── Group B (XREF-only → OWNER promotion; same --add-terms path, no active mti) ──
 'H2154':('evil','M27'),'H2451':('wisdom','M15'),'H3689':('hope',None),'H3970':('desire','M29'),
 'H4066':('strife','M02'),'H6419':('pray','M21'),'H7832':('rejoicing','M04'),'H8605':('prayer','M21'),
 # ── Group A (OT-DBR-009 over-deleted mti+verses; empty shell delete-flagged; re-pull into SAME home) ──
 'H2898':('love',None),'H3684':('hope','M16'),'H5036':('heart','M16'),'H5949':('shame',None),
 'H6039':('gentleness','M24'),'H6962':('distress','M06'),'H7045':('shame',None),'H8444':('surrender',None),
 # ── Second orphan set (27; 2026-07-05 span-orphan stubs) — clean 22 fresh-onboard (cluster deferred) ──
 'H0833':('blessing',None),'H2449':('wisdom',None),'H7891':('praise',None),'H3467':('salvation',None),
 'H1350':('salvation',None),'H5382':('memory',None),'H7911':('memory',None),'H5678':('wrath',None),
 'H5358':('wrath',None),'H7810':('corruption',None),'H7309':('comfort',None),'H5087':('commitment',None),
 'H5088':('commitment',None),'H3238':('wickedness',None),'H3905':('wickedness',None),'H3906':('wickedness',None),
 'H0079':('strife',None),'H5319':('strife',None),'H2670':('salvation',None),
 'H0490':('the afflicted',None),'H1800':('the afflicted',None),'H3490':('the afflicted',None),
}

# Sub-entry resolutions: intended base strong -> explicit STEP sub-entry code (IB sense).
# Decided from the medium_def glosses (2026-07-06); each is the inner-being sense of a split lemma.
RESOLVE = {
 'H2427':'H2427A',  # agony (primary; B=sub-gloss dup)
 'H2342':'H2342I',  # anguish: writhe in pain (vs dance/give-birth/be-firm)
 'H1793':'H1793A',  # contrite (vs B=dust)
 'H5800':'H5800A',  # forsake (vs restore/release/neglect/location)
 'H1214':'H1214I',  # gain by unjust profit = covetousness
 'H6601':'H6601B',  # entice/deceive (vs A=open wide)
 'H7723':'H7723G',  # falsehood (vs vain/empty)
 'H5640':'H5640A',  # shut up/close (vs B=stopper dup)
 'H6612':'H6612A',  # simple/foolish (vs B=simplicity noun)
 'H7342':'H7342I',  # broad: arrogant = pride (vs wide/location)
 'H2186':'H2186A',  # reject/spurn (vs B=stink)
 'H3988':'H3988A',  # reject/despise (vs B=flow)
 'H5254':'H5254G',  # test/prove (vs try, minor)
 'H5848':'H5848C',  # enfeeble/faint = weakness (vs turn-aside/envelop)
 'H4148':'H4148G',  # discipline/chastening (vs instruction/bonds)
 'H2556':'H2556A',  # to leaven/be sour = embittered (vs red/oppress)
 'H1350':'H1350A',  # to redeem / kinsman-redeemer (vs sub-senses)
}

def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, env=ENV, encoding='utf-8', errors='replace')

def reg_id(word):
    c=sqlite3.connect(LIVE); c.row_factory=sqlite3.Row
    r=c.execute("SELECT id,no FROM word_registry WHERE lower(word)=lower(?)",(word,)).fetchone()
    c.close()
    return (r['id'],r['no']) if r else (None,None)

def base(s):
    return s[:-1] if (len(s)>1 and s[-1].isalpha() and s[0] in 'HG') else s

def process_registry(regword, terms, dry_curate=False):
    """terms = list of (strong, cluster) for this registry."""
    rid,rno = reg_id(regword)
    if rid is None:
        return {'reg':regword,'status':'NO_REGISTRY'}
    # idempotency: drop terms already onboarded (stamped) for THIS registry
    cc=sqlite3.connect(LIVE); cc.row_factory=sqlite3.Row
    done={base(r['strongs_number']) for r in cc.execute(
        "SELECT strongs_number FROM mti_terms WHERE anchor_note=? AND owning_registry_fk=?",(STAMP,rid))}
    cc.close()
    terms=[t for t in terms if base(t[0]) not in done]
    if not terms:
        return {'reg':regword,'status':'ALREADY_DONE'}
    intended = [t[0] for t in terms]
    # 1. extract
    r = sh(['python','scripts/word_study_extract.py','--word',regword,'--anchors',','.join(intended)])
    if r.returncode!=0:
        return {'reg':regword,'status':'EXTRACT_FAIL','err':r.stderr[-500:]}
    # find newest fresh extract for this registry (exclude curated/addterms derivatives; match space OR underscore)
    def _fresh(pats):
        out=[]
        for p in pats:
            out += [f for f in glob.glob(p) if 'curated' not in f and 'addterms' not in f]
        return sorted(out)
    wlow=regword.lower()
    cand=_fresh([f'research/discovery/{rno:03d}_{wlow}_step_data_*.json',
                 f'research/discovery/{rno:03d}_{wlow.replace(" ","_")}_step_data_*.json'])
    if not cand:
        cand=_fresh([f'research/discovery/*{wlow}_step_data_*.json',
                     f'research/discovery/*{wlow.replace(" ","_")}_step_data_*.json'])
    ext=json.load(open(cand[-1],encoding='utf-8'))
    codes={t['code']:t for t in ext['terms']}
    # 2. curate: match each intended to a code (exact, else unique base-match)
    keep=[]; resolution=[]; unresolved=[]
    for strong in intended:
        if strong in RESOLVE and RESOLVE[strong] in codes:
            keep.append(RESOLVE[strong]); resolution.append((strong,RESOLVE[strong],'resolved'))
        elif strong in codes:
            keep.append(strong); resolution.append((strong,strong,'exact'))
        else:
            b=base(strong)
            cands=[cc for cc in codes if base(cc)==b and not codes[cc].get('is_proper_noun')
                   and (codes[cc].get('verse_count') or 0)>0]
            if len(cands)==1:
                keep.append(cands[0]); resolution.append((strong,cands[0],'base-unique'))
            else:
                unresolved.append((strong,cands)); resolution.append((strong,None,f'UNRESOLVED({cands})'))
    if not keep:
        return {'reg':regword,'status':'NO_MATCH','resolution':resolution,'unresolved':unresolved}
    ext['terms']=[codes[k] for k in keep]
    ext['meta']['include_codes']=sorted(keep); ext['meta']['anchor_codes']=sorted(keep)
    ext['meta']['curated_note']=f'gate1 add-terms: {regword}'
    cur=f'research/discovery/{rno:03d}_{regword.lower().replace(" ","_")}_addterms_curated.json'
    json.dump(ext,open(cur,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    if dry_curate:
        return {'reg':regword,'status':'DRY_CURATE','resolution':resolution,'unresolved':unresolved,'kept':keep,'curated':cur}
    # 3. onboard --add-terms
    r=sh(['python','-m','engine.engine','--mode=audit_word','--registry',str(rno),'--extract-file',cur,'--add-terms'])
    ok = 'AUDIT_WORD COMPLETE' in r.stdout
    if not ok:
        return {'reg':regword,'status':'ONBOARD_FAIL','tail':r.stdout[-800:]+r.stderr[-400:]}
    # 4. stamp + cluster
    c=sqlite3.connect(LIVE)
    kept_bases_map={k:dict(terms).get(k) or dict((s,cl) for s,cl in terms).get(base(k)) for k in keep}
    for k in keep:
        cl=None
        for s,clv in terms:
            if s==k or base(s)==base(k): cl=clv; break
        c.execute("UPDATE mti_terms SET anchor_note=? WHERE strongs_number=? AND owning_registry_fk=?",(STAMP,k,rid))
        if cl:
            c.execute("UPDATE mti_terms SET cluster_code=COALESCE(cluster_code,?) WHERE strongs_number=? AND owning_registry_fk=?",(cl,k,rid))
    c.commit(); c.close()
    # 5. VC
    rvc=sh(['python','scripts/_apply_create_vc_for_onboarded.py','--registries',str(rno)])
    vc_line=[l for l in rvc.stdout.splitlines() if 'created' in l]
    # verse-record count for the new terms
    c=sqlite3.connect(LIVE)
    vrn=c.execute(f"SELECT COUNT(*) FROM wa_verse_records vr JOIN mti_terms mt ON mt.id=vr.mti_term_id WHERE mt.anchor_note=? AND mt.owning_registry_fk=? AND COALESCE(vr.delete_flagged,0)=0",(STAMP,rid)).fetchone()[0]
    c.close()
    rec={'reg':regword,'reg_id':rid,'status':'DONE','kept':keep,'resolution':resolution,
         'unresolved':unresolved,'verse_records':vrn,'vc':vc_line[-1] if vc_line else ''}
    with open(LEDGER,'a',encoding='utf-8') as f: f.write(json.dumps(rec)+'\n')
    return rec

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--clusters'); ap.add_argument('--registries'); ap.add_argument('--list',action='store_true')
    ap.add_argument('--dry-curate',action='store_true')
    a=ap.parse_args()
    # group worklist by registry
    byreg={}
    for strong,(rw,cl) in WORK.items():
        byreg.setdefault(rw,[]).append((strong,cl))
    if a.list:
        for rw in sorted(byreg):
            print(f"  {rw:16} {[s for s,_ in byreg[rw]]}")
        print(f"total: {len(WORK)} terms, {len(byreg)} registries")
        return
    # filter
    sel=set(byreg)
    if a.registries: sel={x.strip().lower() for x in a.registries.split(',')}
    if a.clusters:
        cls={x.strip() for x in a.clusters.split(',')}
        sel={rw for rw in byreg if any(cl in cls for _,cl in byreg[rw])}
    todo=sorted(rw for rw in byreg if rw.lower() in {s.lower() for s in sel} or rw in sel)
    print(f"processing {len(todo)} registries: {todo}")
    for rw in todo:
        res=process_registry(rw, byreg[rw], dry_curate=a.dry_curate)
        flag='' if res['status'] in ('DONE','DRY_CURATE') else '  <-- CHECK'
        print(f"  [{res['status']:12}] {rw:16} kept={res.get('kept')} unresolved={res.get('unresolved')}{flag}")

if __name__=='__main__':
    main()
