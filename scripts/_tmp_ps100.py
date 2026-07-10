import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,100,
  note="Ps100 the great thanksgiving hymn (5v). IB = worship acts: make a JOYFUL-NOISE; SERVE the LORD with GLADNESS, come with SINGING; KNOW that the LORD is God; enter with THANKSGIVING + PRAISE, GIVE-THANKS + BLESS his name. God's made-us/name/good/steadfast-love/faithfulness = qualifiers; sheep/pasture/gates/courts imagery + the todah superscription = standalone.")
CH=[
 (268779,"joyful noise (rua)","action","all the earth","make a joyful noise","to the LORD",GOD,"paired with serving with gladness","v1: 'Make a JOYFUL NOISE (rua) to the LORD, all the earth!' - the glad shout of all the earth to God, worship as exuberant acclamation."),
 (268783,"serve (abad)","action","the worshippers","serve","the LORD with gladness",GOD,"paired with gladness and singing","v2: 'SERVE (abad) the LORD with gladness!' - the glad service of God, worship as joyful obedience."),
 (268785,"gladness (simchah)","state","the worshippers","serve with gladness","before God",IB,"paired with serving and singing","v2: 'Serve the LORD with GLADNESS (simchah)!' - the joy that fills God's service, worship offered gladly not grudgingly."),
 (268788,"singing (renanah)","action","the worshippers","come with singing","into God's presence",GOD,"paired with gladness","v2: 'Come into his presence with SINGING (renanah)!' - the sung approach to God, worship as joyful song."),
 (307174,"know (yada)","action","the worshippers","know","that the LORD is God, our maker",GOD,"paired with being his people and sheep","v3: 'KNOW (yada) that the LORD, he is God!' - the acknowledgement that grounds the worship, that God is God and we are his."),
 (268791,"thanksgiving (todah)","action","the worshippers","enter with thanksgiving","God's gates",GOD,"paired with praise","v4: 'Enter his gates with THANKSGIVING (todah)' - the grateful approach into God's courts, thanks as the way in."),
 (268793,"praise (tehillah)","action","the worshippers","enter with praise","God's courts",GOD,"paired with thanksgiving","v4: 'and his courts with PRAISE (tehillah)!' - the praise that fills God's courts, worship as adoration."),
 (268794,"give thanks (yadah)","action","the worshippers","give thanks","to God",GOD,"paired with blessing his name","v4: 'GIVE THANKS (yadah) to him' - the gratitude rendered to God, thanks as the heart of worship."),
 (268795,"bless (barak)","action","the worshippers","bless","God's name",GOD,"paired with giving thanks","v4: 'BLESS (barak) his name!' - the adoration of God's name, praise as blessing."),
]
for a in CH: r.ch(*a)
QU=[
 (307180,"made (asah)",307174,"v3: 'It is he who MADE (asah) us, and we are his' - God our maker. Qualifier."),
 (268797,"name (shem)",268795,"v4: 'bless his NAME (shem)!' - God's name. Qualifier."),
 (268800,"good (tob)",268794,"v5: 'For the LORD is GOOD (tob)' - God's goodness. Qualifier."),
 (268801,"steadfast love (chesed)",268794,"v5: 'his STEADFAST LOVE (chesed) endures forever' - God's covenant love. Qualifier."),
 (268802,"endures forever (olam)",268794,"v5: 'his steadfast love ENDURES FOREVER (olam)' - the perpetuity of God's love. Qualifier."),
 (268803,"faithfulness (emunah)",268794,"v5: 'and his FAITHFULNESS (emunah) to all generations' - God's faithfulness. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (268778,"thanksgiving (todah)","v0 superscription: 'A Psalm for giving THANKS (todah)' - the psalm-heading/type. Standalone."),
 (307183,"sheep (tson)","v3: 'we are his people, and the SHEEP (tson) of his pasture' - the flock-image of the people. Standalone."),
 (307185,"pasture (marith)","v3: 'the sheep of his PASTURE (marith)' - the flock-image, God's cared-for people. Standalone."),
 (268790,"gates (shaar)","v4: 'Enter his GATES (shaar) with thanksgiving' - the temple gates, place of entry to worship. Standalone."),
 (268792,"courts (chatser)","v4: 'and his COURTS (chatser) with praise!' - the temple courts, place of worship. Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
