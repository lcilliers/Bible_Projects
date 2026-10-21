"""Read-only: render the FINAL single-home-per-term registry mapping for the 97 gate1 orphans,
per the researcher's 2026-07-06 directives (accept suggestions; no owner reassignment for Group A;
Satan=third party, vileness=wicked, rest of 3.4 = qualifiers). Validates all 97 covered.
Emits a markdown table grouped by target registry + a flat table. No DB writes.
"""
import sqlite3, sys
BK='backups/bible_research.pre-gate1-ROLLBACK-20260706T141152Z.db'

# strong -> (home_registry, role_hint, new_registry?, note)
# role_hint: C=characteristic, Q=qualifier, R=reference(third party)
GROUP_A_KEEP = {  # keep surviving OWNER home; reconcile mti only (no reassign)
 'H2898':'love','H3684':'hope','H5036':'heart','H5949':'shame',
 'H6039':'gentleness','H6962':'distress','H7045':'shame','H8444':'surrender'}

MAP = {
 # Tier 1 clear
 'H0444':('corruption','C'),'H0536':('weakness','C'),'H1161':('terror','C'),
 'H1249':('purity','C'),'H1252':('purity','C'),'H1305':('purity','C'),'H2135':('purity','C'),
 'H1793':('contrition','C'),'H2186':('rejection','C'),'H3988':('rejection','C'),
 'H2427':('agony','C'),'H2451':('wisdom','C'),'H4784':('rebellion','C'),
 'H6419':('pray','C'),'H8605':('prayer','C'),'H3970':('desire','C'),
 # Tier 2 probable
 'H6612':('foolishness','C'),'H7908':('mourning','C'),'H2342':('anguish','C'),
 'H6277':('pride','C'),'H7426':('pride','C'),'H8217':('humility','C'),
 'H7646':('contentment','C'),'H2489':('weakness','C'),'H7326':('weakness','C'),
 'H3021':('weakness','C'),'H5848':('weakness','C'),'H6199':('weakness','C'),
 'H7723':('deceit','C'),'H3576':('deceit','C'),'H3577':('deceit','C'),'H2665':('deceit','C'),
 'H6141':('perverseness','C'),'H5003':('whoredom','C'),'H7321':('praise','C'),
 'H4066':('strife','C'),'H2154':('evil','C'),'H7832':('rejoicing','C'),
 # Tier 3.1 no-registry -> pick / new
 'H3468':('salvation','C','NEW'),'H4190':('salvation','C','NEW'),'H8668':('salvation','C','NEW'),
 'H5826':('salvation','C'),'H5046':('testimony','C'),'H1747':('peace','Q'),
 'H0981':('foolishness','C'),'H0974':('temptation','C'),'H5254':('temptation','C'),
 'H5359':('wrath','C'),'H5360':('wrath','C'),'H2555':('wickedness','C'),'H6231':('wickedness','C'),
 # Tier 3.2 ambiguous -> first pick
 'H5937':('rejoicing','C'),'H5970':('rejoicing','C'),'H6149':('delight','C'),
 'H0835':('blessing','C'),'H6165':('longing','C'),'H8373':('longing','C'),
 'H6770':('craving','C'),'H1214':('covetousness','C'),'H3368':('worth','C'),'H3365':('worth','C'),
 'H3642':('longing','C'),'H8428':('grief','C'),'H3887':('contempt','C'),'H3932':('contempt','C'),
 'H3933':('contempt','C'),'H7047':('contempt','C'),'H7853':('strife','C'),'H5010':('rejection','C'),
 'H5641':('doubt','C'),'H5800':('betrayal','C'),'H7279':('doubt','C'),'H5640':('doubt','Q'),
 'H7683':('disobedience','C'),'H7686':('disobedience','C'),'H8582':('disobedience','C'),
 'H5341':('obedience','C'),'H4148':('wisdom','C'),
 # Tier 3.4 -> qualifiers / third party / vileness=wicked
 'H7854':('spiritual powers','R'),'H2149':('wickedness','C'),'H7283':('strife','Q'),
 'H6323':('distress','Q'),'H6601':('deceit','Q'),'H2556':('bitterness','Q'),
 'H7342':('pride','Q'),'H2611':('hypocrisy','Q'),'H3689':('hope','Q'),'H8496':('wickedness','Q'),
 'H6817':('distress','Q'),  # to cry out (tsaʿaq) — outcry qualifier
}

bk=sqlite3.connect(BK); bk.row_factory=sqlite3.Row
terms={r['strongs_number']:r['owning_word'] for r in bk.execute(
  "SELECT strongs_number, owning_word FROM mti_terms WHERE anchor_note LIKE 'gate1-psalms-2026%'").fetchall()}
bk.close()

rows=[]
missing=[]
for s,gloss in sorted(terms.items()):
    if s in GROUP_A_KEEP:
        rows.append((s,gloss,GROUP_A_KEEP[s],'C','', 'Group A — keep existing owner (no reassign)'))
    elif s in MAP:
        m=MAP[s]; home,role=m[0],m[1]; new='NEW' if len(m)>2 else ''
        rows.append((s,gloss,home,role,new,''))
    else:
        missing.append(s)

print(f'covered: {len(rows)} / 97   missing: {missing}')
# registry-grouped
from collections import defaultdict
byreg=defaultdict(list)
for s,g,home,role,new,note in rows: byreg[home].append((s,g,role,new))
print('\n## By target registry (onboarding batches)\n')
newregs=sorted({home for s,g,home,role,new,note in rows if new=='NEW'})
print('NEW registries to REGISTER:', newregs or '(none)')
print(f'Distinct target registries: {len(byreg)}\n')
for home in sorted(byreg):
    isnew=' [NEW]' if home in newregs else ''
    membs=byreg[home]
    tag=''.join(sorted({r for _,_,r,_ in membs}))
    print(f'- **{home}**{isnew} ({len(membs)}): ' + ', '.join(f"{s} {g}"+("*" if r!='C' else "") for s,g,r,_ in membs))
print('\n(* = qualifier/reference role, not characteristic)')
