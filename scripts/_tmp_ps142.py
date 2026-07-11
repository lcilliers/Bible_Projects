#!/usr/bin/env python
"""Ps 142 (David in the cave, maskil) - the isolated soul. IB ops: crying aloud
for mercy; pouring out complaint and trouble; the fainting spirit; the soul no
one cares for (abandonment); God as refuge and portion in the land of the living;
crying when brought very low; anticipated thanksgiving. God's deliver/bring-out =
qual; prison/persecutor imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=142
r = Reading("Psa", 19, CH, note="The isolated soul in the cave: complaint, fainting spirit, abandonment, God as portion")

r.ch(273770,"cry aloud for mercy","affect","the psalmist","the interior breaks into a loud cry, voicing supplication to the only hearer","crying-out","cry-for-mercy",IB,
     "v1: 'with my voice I CRY OUT to the LORD; I plead for mercy' - trapped in the cave, the self makes its distress audible upward.")
r.ch(273778,"pour out complaint","affect","the psalmist","the complaint and trouble are emptied out before God - full disclosure of the burden","unburdening","pour-out-complaint",IB,
     "v2: 'I POUR OUT my COMPLAINT before him; I tell my TROUBLE before him' - the operation is unloading: nothing withheld, the interior laid bare.")
r.ch(273783,"spirit faints within","state","the psalmist","the spirit fails/faints inside while overwhelmed - the strength of the inner self ebbing","spirit-failing","faint-within",IB,
     "v3: 'when my SPIRIT FAINTS within me, you know my way' - the interior registers its own collapse, yet notes it is still known.")
r.ch(273808,"soul none cares for","state","the psalmist","the desolating sense that no one takes notice, that no one cares for the soul","abandonment","none-cares",IB,
     "v4: 'no refuge remains to me; no one CARES for my SOUL' - the sharpest interior wound is not the cave but the felt abandonment.")
r.ch(273813,"God as refuge and portion","affect","the psalmist","against abandonment the self declares God its refuge and portion among the living","re-grounding","you-are-my-portion",IB,
     "v5: 'You are my REFUGE, my PORTION in the land of the living' - the interior answers isolation by fastening the whole self onto God as its share.")
r.ch(273820,"cry when brought low","affect","the psalmist","brought very low, the self attends and cries - weakness voiced as appeal","low-crying","cry-brought-low",IB,
     "v6: 'Attend to my CRY, for I am brought very low' - distinct from v1: this cry rises from the floor of strength, admitted weakness made plea.")
r.ch(273835,"anticipated thanksgiving","affect","the psalmist","the self already reaches past rescue to thanks - gratitude anticipated among the righteous","hope-in-thanks","thank-when-freed",IB,
     "v7: 'Bring my soul out of prison, that I may GIVE THANKS to your name' - the interior leans forward into future praise, gratitude pre-formed in hope.")

for sid,sense,src,d in [
 (273774,"mercy (chanan)",273770,"v1: 'I plead for MERCY' - the object of the cry."),
 (273818,"Attend (qashab)",273820,"v6: 'ATTEND to my cry' - the divine hearing sought."),
 (273787,"know my way (yada)",273778,"v3: 'you KNOW my way' - God's knowledge amid the poured-out complaint."),
 (273824,"Deliver (natsal)",273820,"v6: 'DELIVER me from my persecutors' - the rescue petition."),
 (273830,"Bring out (yatsa)",273835,"v7: 'BRING my soul out of prison' - the release petition that opens onto thanks."),
 (273840,"deal bountifully (gamal)",273835,"v7: 'you will DEAL BOUNTIFULLY with me' - God's generosity the thanks anticipates."),
 (273838,"surround (kathar)",273835,"v7: 'the righteous will SURROUND me' - the restored fellowship anticipated."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (cave/prison/persecutor imagery or label); standalone.")
r.write()
