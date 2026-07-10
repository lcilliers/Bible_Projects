import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,87,
  note="Ps87 Zion, birthplace of the nations (Korah, 7v; one movement). Almost wholly about God's love for / founding / registering of Zion (qualifiers) and the roll of peoples (imagery). Human IB: those who KNOW God among the nations (Rahab, Babylon, Philistia... 'this one was born there'); and the SINGERS whose springs are all in God. God's founding/loving/recording = qualifiers; the nation-names + born-there refrain = standalone.")
for a in [
 (284392,"know (yada)","action","the nations","come to know","God","paired with being counted born in Zion",GOD,"v4: 'Among those who KNOW (yada) me I mention Rahab and Babylon' - the nations brought to acknowledge God, foreigners reckoned citizens of Zion by knowing him."),
 (307010,"singers (shir)","action","the singers and dancers","sing / celebrate","that all springs are in God","paired with the springs in Zion",GOD,"v7: 'SINGERS (shir) and dancers alike say, All my springs are in you' - the worshippers whose every source of life is found in God/Zion, joy rooted in him."),
]: r.ch(*a)
for sid,sense,src,d in [
 (284388,"holy (qodesh)",284392,"v1: 'His foundation is on the HOLY (qodesh) mountains' - God's holiness set on Zion. Qualifier."),
 (284390,"founded (yesud)",284392,"v1: 'his FOUNDATION (yesud) is on the holy mountains' - God's founding of Zion. Qualifier."),
 (306983,"loves (aheb)",284392,"v2: 'The LORD LOVES (aheb) the gates of Zion' - God's love for Zion. Qualifier."),
 (306990,"glorious things (kabad)",284392,"v3: 'GLORIOUS THINGS (kabad) of you are spoken, O city of God' - God's glory declared of Zion. Qualifier."),
 (306991,"spoken (dabar)",284392,"v3: 'glorious things of you are SPOKEN (dabar)' - what God declares of the city. Qualifier."),
 (284393,"mention (zakar)",284392,"v4: 'I MENTION (zakar) Rahab and Babylon' - God's naming of the nations as his own. Qualifier."),
 (307001,"establish (kun)",307010,"v5: 'the Most High himself will ESTABLISH (kun) her' - God's establishing of Zion. Qualifier."),
 (307003,"records (saphar)",307010,"v6: 'The LORD RECORDS (saphar) as he registers the peoples' - God's enrolling of the nations. Qualifier."),
 (307004,"registers (kathab)",307010,"v6: 'as he REGISTERS (kathab) the peoples' - God's writing them in the citizen-roll. Qualifier."),
]: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (284400,"this one (zeh)","v4: 'THIS ONE (zeh) was born there' - the refrain reckoning a foreigner a native of Zion. Standalone."),
 (284401,"born (yalad)","v4: 'This one was BORN (yalad) there' - the birth-in-Zion motif, image of belonging. Standalone."),
 (306999,"born (yalad)","v5: 'This one and that one were BORN (yalad) in her' - the born-in-Zion refrain. Standalone."),
 (307006,"one (zeh)","v6: 'This ONE (zeh) was born there' - the refrain. Standalone."),
 (307007,"born (yalad)","v6: 'This one was BORN (yalad) there' - the citizen-birth motif. Standalone."),
 (307011,"dancers (chalal)","v7: 'Singers and DANCERS (chalal) alike' - the festal dancers of Zion. Standalone."),
 (307014,"springs (mayan)","v7: 'All my SPRINGS (mayan) are in you' - the fountains of life, image of all blessing found in Zion/God. Standalone."),
]: r.st(sid,sense,d)
r.write()
