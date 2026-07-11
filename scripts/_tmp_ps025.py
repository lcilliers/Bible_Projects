#!/usr/bin/env python
"""Ps 25 (acrostic - trust, guidance, forgiveness; 88 spans). IB ops: lifting the
soul to God; trust with the plea against shame; waiting on God; asking to know
his ways; waiting all day long; the penitent plea 'remember not the sins of my
youth'; the humble God leads; keeping God's covenant; confessing great guilt and
asking pardon; the God-fearer instructed; the soul abiding in well-being; the
friendship/intimacy of God for those who fear him; the lonely and afflicted
pleading grace; the enlarged troubles of the heart; integrity and uprightness as
guard; taking refuge. God's lead/teach/pardon/consider/redeem = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=25
r = Reading("Psa", 19, CH, note="Acrostic of trust/guidance/forgiveness: lift-soul, trust, wait, know-ways, penitence, humble-led, keep-covenant, pardon, fear-instructed, friendship, affliction, heart-troubles, integrity, refuge")

r.ch(275947,"lift up my soul to you","affect","the psalmist","the self lifts up its soul to God - the whole inner self raised toward him as the psalm opens","self-offering","lift-up-soul",IB,
     "v1: 'To you, O LORD, I LIFT UP my SOUL' - the operation raises the entire interior toward God; the acrostic begins by handing the self over.")
r.ch(275946 if False else 276026,"in you I trust","affect","the psalmist","the self trusts God and pleads not to be put to shame, not to let enemies exult - reliance under threat","trust","trust-not-shamed",IB,
     "v2: 'O my God, in you I TRUST; let me not be put to SHAME' - the operation rests the self on God while the danger of humiliation presses; trust and vulnerability held together.")
r.ch(276058,"none who wait are shamed","affect","those who wait","none who wait for God shall be put to shame, but the wantonly treacherous will - waiting as the vindicated posture","waiting","wait-not-shamed",IB,
     "v3: 'none who WAIT for you shall be put to shame' - the operation generalises the trust into patient waiting; the interior that waits is promised it will not be disappointed.")
r.ch(306186,"make me know your ways","volition","the psalmist","the self asks to be shown God's ways and taught his paths - a desire to be led rightly","desire-for-guidance","know-your-ways",IB,
     "v4: 'Make me to KNOW your WAYS, O LORD; teach me your paths' - the operation is a longing to be taught; the interior wants direction, not just rescue.")
r.ch(276069,"for you I wait all day","affect","the psalmist","the self waits for God all the day long, asking to be led in his truth - sustained, whole-day hope","sustained-waiting","wait-all-day",IB,
     "v5: 'Lead me in your truth and teach me... for you I WAIT all the day long' - distinct from v3: this is the personal, unremitting waiting that fills the whole day.")
r.ch(276080,"remember not my youth's sins","cognition","the psalmist","the self asks God not to remember the sins of its youth but to remember it by steadfast love - penitent appeal for forgetting","penitence","remember-not-sins",IB,
     "v7: 'REMEMBER NOT the SINS of my youth or my transgressions; according to your steadfast love remember me' - the operation is a penitent's plea: let the record of old sin be blotted, and let love be the lens instead.")
r.ch(276100,"the humble God leads","state","the humble","God leads the humble in what is right and teaches them his way - lowliness as the teachable condition","humility","humble-led",IB,
     "v9: 'He LEADS the HUMBLE in what is right, and teaches the humble his way' - the operation names the interior God can guide: only the humble are teachable, and they are led.")
r.ch(275955,"those who keep his covenant","volition","the covenant-keepers","all God's paths are steadfast love and faithfulness for those who keep his covenant - fidelity that walks in love","covenant-fidelity","keep-covenant",IB,
     "v10: 'All the paths of the LORD are steadfast love and faithfulness, for those who KEEP his COVENANT and his testimonies' - the operation is the kept covenant; the interior that holds to God's terms finds all his ways to be love.")
r.ch(275962,"pardon my guilt, for it is great","cognition","the psalmist","the self asks pardon for its guilt, honestly owning that it is great - confession without minimising","honest-confession","pardon-great-guilt",IB,
     "v11: 'For your name's sake, O LORD, PARDON my GUILT, for it is GREAT' - the operation is unflinching confession: the interior does not shrink the sin but names it great and appeals to God's name.")
r.ch(275969,"the God-fearer instructed","affect","the one who fears the LORD","whoever fears the LORD, God will instruct in the way he should choose - reverence rewarded with guidance","reverent-teachability","fearer-instructed",IB,
     "v12: 'Who is the man who FEARS the LORD? Him will he INSTRUCT in the way that he should choose' - the operation ties instruction to fear: the reverent interior is the one God teaches which way to take.")
r.ch(275974,"his soul abides in well-being","state","the God-fearer","the God-fearer's soul abides in well-being and his offspring inherit the land - the interior at ease as the fruit of fear","well-being","soul-abides",IB,
     "v13: 'His SOUL shall abide in WELL-BEING, and his offspring shall inherit the land' - the operation is rest: the fearing interior settles into a lasting good.")
r.ch(275980,"the friendship of the LORD","affect","those who fear him","the intimate friendship/counsel of the LORD is for those who fear him, to whom he makes known his covenant - a shared secret","intimacy","friendship-with-God",IB,
     "v14: 'The FRIENDSHIP of the LORD is for those who FEAR him, and he makes KNOWN to them his covenant' - the operation is intimacy: the God-fearing interior is admitted to God's confidence, told his secret.")
r.ch(276002,"lonely and afflicted, be gracious","state","the psalmist","the self asks God to turn and be gracious, for it is lonely and afflicted - the ache of isolation brought to God","loneliness","lonely-afflicted",IB,
     "v16: 'Turn to me and be GRACIOUS to me, for I am LONELY and AFFLICTED' - the operation names a specific inner condition, solitude joined to affliction, and lays it before God for mercy.")
r.ch(276003,"the troubles of my heart enlarged","state","the psalmist","the troubles of the self's heart are enlarged; it asks to be brought out of its distresses - inner pressure mounting","inner-pressure","heart-troubles-enlarged",IB,
     "v17: 'The TROUBLES of my HEART are ENLARGED; bring me out of my distresses' - the operation registers a swelling of interior anguish, the heart's troubles growing rather than easing.")
r.ch(276042,"integrity and uprightness preserve me","volition","the psalmist","the self asks that integrity and uprightness preserve it, for it waits on God - character offered as its guard","integrity","integrity-preserve",IB,
     "v21: 'May INTEGRITY and UPRIGHTNESS preserve me, for I WAIT for you' - the operation offers the self's own integrity, held in dependence on God, as the thing that keeps it.")
r.ch(276040,"I take refuge in you","affect","the psalmist","the self asks God to guard and deliver its soul, not letting it be shamed, for it takes refuge in him - shelter as the ground of the plea","refuge-taking","take-refuge",IB,
     "v20: 'Oh, GUARD my soul, and deliver me! Let me not be put to shame, for I TAKE REFUGE in you' - the operation shelters the whole self in God; refuge is the reason the plea expects to be answered.")

for sid,sense,src,d in [
 (276063,"Lead me in your truth",306186,"v5: 'LEAD me in your truth and teach me' - the guiding act the desire-to-know asks for."),
 (276065,"teach me",306186,"v5: 'and TEACH me' - the instruction sought."),
 (276072,"remember your mercy",276080,"v6: 'REMEMBER your mercy, O LORD, and your steadfast love' - the love the penitent asks God to recall instead of sin."),
 (276096,"instructs sinners in the way",276100,"v8: 'Good and upright is the LORD; therefore he INSTRUCTS sinners in the way' - God's guiding character behind the leading of the humble."),
 (275962 if False else 276013,"forgive all my sins",275962,"v18: 'Consider my affliction... and FORGIVE all my sins' - the pardon the confession seeks."),
 (276010,"Consider my affliction",276002,"v18: 'CONSIDER my affliction and my trouble' - the divine regard the lonely self pleads for."),
 (276036,"deliver me",276040,"v20: 'DELIVER me' - the rescue the refuge-taking expects."),
 (276049,"Redeem Israel",276042,"v22: 'REDEEM Israel, O God, out of all his troubles' - the corporate deliverance the psalm closes on."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (net/foes/violent-hatred, God's-goodness label, or repeated state-noun already carried by a char); standalone.")
r.write()
