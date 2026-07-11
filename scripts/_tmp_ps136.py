import sys, sqlite3; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
c=sqlite3.connect('database/bible_research.db');c.row_factory=sqlite3.Row
cand=[dict(sid=x['id'],v=int(x['reference'].split(':')[1]),surf=x['surface'],ps=x['primary_strong'])
 for x in c.execute("SELECT id,reference,surface,primary_strong FROM verse_span_index WHERE reference LIKE 'Psa 136:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")]
r=Reading("Psa",19,136,
  note="Ps136 the great Hallel (26v). Every deed answered by the refrain 'his steadfast love endures forever' (chesed = qualifier x26; 'endures forever' = temporal standalone x26). Human IB is thin: the fourfold GIVE-THANKS imperative (v1,2,3,26) framing the litany, and the people's LOW-ESTATE that God remembered (v23). God's deeds (does-wonders/made-heavens/struck-Egypt/divided-sea/led/gave-heritage/rescued/gives-food) = qualifiers; creation/Exodus imagery + 'endures forever' = standalone.")
# characteristics: give-thanks (H3034) + low-estate (H8216)
GT={273151:"v1: 'GIVE THANKS (yadah) to the LORD, for he is good' - the opening imperative of the litany, thanks for God's enduring love.",
    273176:"v2: 'GIVE THANKS (yadah) to the God of gods' - thanks to the supreme God.",
    273225:"v3: 'GIVE THANKS (yadah) to the Lord of lords' - thanks to the sovereign Lord.",
    273218:"v26: 'GIVE THANKS (yadah) to the God of heaven' - the closing imperative, sealing the litany of thanks."}
for sid,note in GT.items(): r.ch(sid,"give thanks (yadah)","action","the worshippers","give thanks","to God",GOD,"paired with the antiphonal refrain of steadfast love",note)
r.ch(273198,"low estate (shephel)","state","the people","be in low estate","and remembered by God",IB,"paired with God's remembering","v23: 'It is he who REMEMBERED us in our LOW ESTATE (shephel)' - the people's abasement, the humbled condition that God's love stooped to remember.")
# classify the rest by strong's
QVERB={'H6213','H5186','H1504','H5674','H5287','H1980','H5221','H2026','H5414','H2142','H6561','H7554','H4475'}
QATTR={'H2617','H6381','H8394','H2389','H0216','H2220'}  # steadfast love + God's attribute/works
SNOUN={'H5769','H3394','H3556','H1060','H5488','H1506','H2428','H5159','H6862','H1320','H3899','H2896'}  # endures-forever, moon, stars, firstborn, Red, host, heritage, foes, flesh, food, good
authored={273151,273176,273225,273218,273198}
for x in cand:
    if x['sid'] in authored: continue
    ps=x['ps']; v=x['v']; surf=x['surf']
    if ps=='H2617': r.qu(x['sid'],"steadfast love (chesed)",273151,f"v{v}: 'his STEADFAST LOVE (chesed) endures forever' - God's covenant love, the refrain answering each deed. Qualifier.")
    elif ps=='H5769': r.st(x['sid'],"endures forever (olam)",f"v{v}: 'endures FOREVER (olam)' - the perpetuity of God's love; temporal. Standalone.")
    elif ps in QVERB or ps in QATTR: r.qu(x['sid'],f"{surf} ({ps})",273151,f"v{v}: '{surf}' - God's deed/attribute in the litany. Qualifier.")
    else: r.st(x['sid'],f"{surf} ({ps})",f"v{v}: '{surf}' - image (creation/Exodus). Standalone.")
r.write()
