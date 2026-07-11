#!/usr/bin/env python
"""Ps 36 (the wicked's transgression vs God's steadfast love). IB ops (the
wicked's interior): a heart with no fear of God; self-flattery that hides his sin
from himself; the abandonment of wise and good action; bedtime scheming that will
not reject evil. Then the turn: feasting on the abundance of God's house (the river
of his delights); those who know God, upright in heart. God's love/righteousness/
fountain of life (vv5-9) = qualifier/standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=36
r = Reading("Psa", 19, CH, note="Wicked's inner life (no-fear heart, self-flattery, ceased-wise, bed-scheming) vs feasting on God's abundance + knowing him")

r.ch(277496,"no fear of God before his eyes","cognition","the wicked","transgression speaks to the wicked deep in his heart; there is no fear of God before his eyes - reverence simply absent","fearlessness-of-God","no-fear-in-heart",IB,
     "v1: 'Transgression speaks to the WICKED deep in his HEART; there is no FEAR of God before his eyes' - the operation is the root diagnosis: the wicked's interior has no reverence, and sin speaks in the vacuum.")
r.ch(277520,"he flatters himself about his sin","cognition","the wicked","he flatters himself in his own eyes that his iniquity cannot be found out and hated - self-deception about guilt","self-flattery","flatter-himself",IB,
     "v2: 'For he FLATTERS himself in his own eyes that his INIQUITY cannot be found out and HATED' - the operation is self-deceit: the interior tells itself its sin is invisible and unhateable.")
r.ch(277529,"he has ceased to act wisely","volition","the wicked","the words of his mouth are trouble and deceit; he has ceased to act wisely and do good - a deliberate giving-up of wisdom","abandonment-of-good","ceased-wise",IB,
     "v3: 'he has CEASED to act WISELY and do GOOD' - the operation is a chosen abdication: the interior has stopped even trying to be wise or good.")
r.ch(277532,"he plots trouble on his bed","cognition","the wicked","he plots trouble while on his bed, sets himself in a way that is not good, and does not reject evil - scheming in the place of rest","nocturnal-scheming","plot-on-bed",IB,
     "v4: 'He PLOTS trouble while on his bed; he sets himself in a way that is not good; he does not REJECT evil' - the operation is the interior at work even in bed, and its settled refusal to turn from evil.")
r.ch(277570,"they feast on the abundance of your house","affect","those who take refuge","the children of men feast on the abundance of God's house and drink from the river of his delights - satisfaction found in God","satisfaction-in-God","feast-on-abundance",IB,
     "v8: 'They FEAST on the abundance of your house, and you give them DRINK from the river of your DELIGHTS' - the operation contrasts the wicked's dry scheming with an interior that drinks its fill from God himself.")
r.ch(277503,"those who know you, upright in heart","affect","those who know God","the self asks God to continue his steadfast love to those who know him, his righteousness to the upright in heart - knowledge and uprightness as the interior God favours","knowing-God","know-you-upright",IB,
     "v10: 'Oh, continue your steadfast love to those who KNOW you, and your righteousness to the UPRIGHT in HEART!' - the operation names the interior that receives God's love: one that knows him and is straight within.")

for sid,sense,src,d in [
 (277576,"the river of your delights",277570,"v8: 'you give them drink from the RIVER of your delights' - the abundance the satisfied interior drinks from."),
 (277558,"you save man and beast",277503,"v6: 'you SAVE man and beast, O LORD' - God's preserving righteousness the knowers rest on."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (God's love/righteousness/fountain-of-light vv5-9, arrogance-foot/wicked-fallen, or attribute label); standalone.")
r.write()
