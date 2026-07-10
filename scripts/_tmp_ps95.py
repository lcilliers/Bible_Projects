import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,95,
  note="Ps95 worship-call + Meribah warning (11v). Passages: come, let us sing to the rock of our salvation v1-5; come, let us worship and kneel before our Maker v6-7b; Today if you hear his voice, do not harden your hearts v7c-11. IB: SING + JOYFUL-NOISE + COME with THANKSGIVING; WORSHIP + BOW-DOWN + KNEEL; HEAR his voice; do not HARDEN your HEARTS; the fathers who TEST + PROVE God; who GO-ASTRAY in HEART and have not KNOWN his ways. God's rock/salvation/made-the-sea/Maker/swore/rest = qualifiers; depths/heights/pasture/sheep imagery = standalone.")
CH=[
 (285443,"sing (ranan)","action","the worshippers","sing","to the LORD",GOD,"paired with the joyful noise","v1: 'Oh come, let us SING (ranan) to the LORD' - the summons to joyful praise, worship as song."),
 (285445,"joyful noise (rua)","action","the worshippers","make a joyful noise","to the rock of salvation",GOD,"paired with the singing","v1: 'let us make a JOYFUL NOISE (rua) to the rock of our salvation!' - the glad shout to God the rock, exuberant acclamation."),
 (285469,"come (qadam)","action","the worshippers","come before God","with thanksgiving",GOD,"paired with thanksgiving","v2: 'Let us COME (qadam) into his presence with thanksgiving' - the drawing near to God, worship as approach."),
 (285471,"thanksgiving (todah)","action","the worshippers","give thanks","to God",GOD,"paired with coming into his presence","v2: 'Let us come into his presence with THANKSGIVING (todah)' - the grateful approach, thanks as the manner of coming."),
 (285472,"joyful noise (rua)","action","the worshippers","make a joyful noise","to God with songs","paired with thanksgiving",GOD,"v2: 'let us make a JOYFUL NOISE (rua) to him with songs of praise!' - the glad music of worship, praise in song."),
 (285490,"worship (shachah)","action","the worshippers","worship / bow","before God",GOD,"paired with bowing and kneeling","v6: 'Oh come, let us WORSHIP (shachah) and bow down' - the reverent prostration before God, worship as homage."),
 (285491,"bow down (kara)","action","the worshippers","bow down","before God",GOD,"paired with worshipping","v6: 'let us WORSHIP and BOW DOWN (kara)' - the bending of the body in reverence, humility before the Maker."),
 (285492,"kneel (barak)","action","the worshippers","kneel","before the LORD our Maker",GOD,"paired with bowing down","v6: 'let us KNEEL (barak) before the LORD our Maker!' - the kneeling of worship, creatures before their creator."),
 (285506,"hear (shama)","action","the people","hear / heed","God's voice today",GOD,"paired with not hardening the heart","v7: 'Today, if you HEAR (shama) his voice' - the summons to heed God now, the hinge from praise to warning."),
 (285509,"harden (qashah)","disposition","the people","harden","their hearts",IB,"paired with the hardened hearts","v8: 'do not HARDEN (qashah) your hearts, as at Meribah' - the obduracy warned against, the heart set against God's voice."),
 (285510,"hearts (lebab)","faculty","the people","harden the heart","against God",IB,"paired with the hardening","v8: 'do not harden your HEARTS (lebab)' - the inner self that must not be closed to God, seat of the warned obduracy."),
 (285517,"test (nasah)","action","the fathers","test / put to proof","God",GOD,"paired with putting God to the proof","v9: 'when your fathers put me to the TEST (nasah)' - the presumptuous testing of God in the wilderness, unbelief made trial."),
 (285518,"put to proof (bachan)","action","the fathers","put to the proof","God",GOD,"paired with the testing","v9: 'and put me to the PROOF (bachan), though they had seen my work' - the demand for proof despite the works already seen."),
 (285455,"go astray (taah)","disposition","that generation","go astray","in heart",IB,"paired with not knowing God's ways","v10: 'they are a people who GO ASTRAY (taah) in their heart' - the wandering heart of the wilderness generation, straying from God."),
 (285456,"heart (lebab)","faculty","that generation","go astray","in the heart",IB,"paired with going astray","v10: 'who go astray in their HEART (lebab)' - the inner self wandering from God, seat of the straying."),
 (285459,"know (yada, negated)","disposition","that generation","fail to know","God's ways",GOD,"paired with going astray in heart","v10: 'and they have not KNOWN (yada) my ways' - the ignorance of God's ways that follows the straying heart."),
]
for a in CH: r.ch(*a)
QU=[
 (285446,"rock (tsur)",285445,"v1: 'the ROCK (tsur) of our salvation' - God as rock. Qualifier."),
 (285448,"salvation (yesha)",285445,"v1: 'the rock of our SALVATION (yesha)' - God's salvation. Qualifier."),
 (285474,"praise (zamir)",285472,"v2: 'with songs of PRAISE (zamir)' - the praise-songs rendered to God. Qualifier."),
 (285485,"made (asah)",285490,"v5: 'The sea is his, for he MADE (asah) it' - God's making of the sea. Qualifier."),
 (285487,"formed (yatsar)",285490,"v5: 'his hands FORMED (yatsar) the dry land' - God's forming of the land. Qualifier."),
 (285495,"Maker (asah)",285490,"v6: 'let us kneel before the LORD our MAKER (asah)' - God as creator. Qualifier."),
 (285463,"swore (shaba)",285459,"v11: 'Therefore I SWORE (shaba) in my wrath' - God's oath. Qualifier."),
 (285468,"rest (menuchah)",285459,"v11: 'they shall not enter my REST (menuchah)' - God's rest, denied the unbelieving. Qualifier."),
 (285451,"loathe (qut)",285455,"v10: 'For forty years I LOATHED (qut) that generation' - God's aversion to the straying generation. Qualifier."),
 (285464,"wrath (aph)",285459,"v11: 'Therefore I swore in my WRATH (aph)' - God's anger, ground of the oath. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (285477,"depths (mechqar)","v4: 'In his hand are the DEPTHS (mechqar) of the earth' - the deep places, image of God's dominion. Standalone."),
 (285479,"heights (toaphah)","v4: 'the HEIGHTS (toaphah) of the mountains are his also' - the mountain peaks, image of God's ownership. Standalone."),
 (285488,"dry land (yabbesheth)","v5: 'his hands formed the DRY LAND (yabbesheth)' - the land, object of God's forming. Standalone."),
 (285501,"pasture (marith)","v7: 'we are the people of his PASTURE (marith)' - the flock-image of the people. Standalone."),
 (285502,"sheep (tson)","v7: 'the SHEEP (tson) of his hand' - the people as God's flock, image. Standalone."),
 (285507,"voice (qol)","v7: 'Today, if you hear his VOICE (qol)' - God's voice, object of the hearing (char, 285506). Standalone."),
 (285521,"work (poal)","v9: 'though they had seen my WORK (poal)' - God's deeds the fathers had witnessed, object. Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
