import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,117,
  note="Ps117 the shortest psalm (2v). IB = the worship acts: PRAISE + EXTOL the LORD, all nations/peoples; closing PRAISE. Ground = God's great STEADFAST-LOVE + FAITHFULNESS (qualifiers). endures-forever = temporal standalone.")
CH=[
 (271023,"praise (halal)","action","all nations","praise","the LORD",GOD,"paired with extolling him",
  "v1: 'PRAISE (halal) the LORD, all nations!' - the summons to every nation to worship God, praise widened to all peoples."),
 (271027,"extol (shabach)","action","all peoples","extol","the LORD",GOD,"paired with praising him",
  "v1: 'EXTOL (shabach) him, all peoples!' - the peoples called to laud God, universal praise."),
 (271037,"praise (halal)","action","all nations","praise","the LORD",GOD,"paired with the ground of his steadfast love",
  "v2: 'PRAISE (halal) the LORD!' - the closing Hallelujah, worship grounded in God's love and faithfulness."),
]
for a in CH: r.ch(*a)
QU=[
 (271031,"great (gabar)",271023,"v2: 'For GREAT (gabar) is his steadfast love toward us' - the greatness of God's love. Qualifier."),
 (271032,"steadfast love (chesed)",271023,"v2: 'great is his STEADFAST LOVE (chesed) toward us' - God's covenant love, the ground of praise. Qualifier."),
 (271034,"faithfulness (emeth)",271023,"v2: 'and the FAITHFULNESS (emeth) of the LORD endures forever' - God's faithfulness. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
r.st(271036,"endures forever (olam)","v2: 'the faithfulness of the LORD ENDURES FOREVER (olam)' - the perpetuity of God's faithfulness; temporal. Standalone.")
r.write()
