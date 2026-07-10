import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,96,
  note="Ps96 'Sing a new song' enthronement hymn (13v). Human IB = the worship acts: SING (x3) + BLESS + TELL + DECLARE + ASCRIBE (x3) + BRING an offering + WORSHIP + TREMBLE before God. God's glory/salvation/splendor/majesty/reigns/judge-with-equity = qualifiers; idols/sanctuary/offering + the COSMIC joy (heavens glad, earth rejoice, sea roar, field exult, trees sing) = standalone (creation-personification, not human IB).")
CH=[
 (307137,"sing (shir)","action","all the earth","sing","a new song to the LORD",GOD,"paired with the repeated call to sing","v1: 'Oh SING (shir) to the LORD a new song' - the summons to fresh praise, worship renewed."),
 (307141,"sing (shir)","action","all the earth","sing","to the LORD",GOD,"paired with the new song","v1: 'SING (shir) to the LORD, all the earth!' - the whole earth called to praise, worship widened to all peoples."),
 (285564,"sing (shir)","action","all the earth","sing / bless","the LORD's name",GOD,"paired with blessing his name","v2: 'SING (shir) to the LORD, bless his name' - the sung blessing of God's name."),
 (285566,"bless (barak)","action","all the earth","bless","God's name",GOD,"paired with singing","v2: 'BLESS (barak) his name' - the adoration of God's name, praise as blessing."),
 (285568,"tell (basar)","action","the worshippers","tell / proclaim","God's salvation day to day",GOD,"paired with declaring his glory","v2: 'TELL (basar) of his salvation from day to day' - the daily proclaiming of God's saving news."),
 (285574,"declare (saphar)","action","the worshippers","declare / recount","God's glory among the nations",GOD,"paired with telling of salvation","v3: 'DECLARE (saphar) his glory among the nations' - the recounting of God's glory to the peoples, worship as witness."),
 (285597,"ascribe (yahab)","action","the families of the peoples","ascribe","glory and strength to the LORD",GOD,"paired with the repeated ascribing","v7: 'ASCRIBE (yahab) to the LORD, O families of the peoples' - the rendering of glory to God, worship as giving him his due."),
 (285601,"ascribe (yahab)","action","the peoples","ascribe","glory and strength to the LORD",GOD,"paired with the first ascribing","v7: 'ASCRIBE (yahab) to the LORD glory and strength!' - the peoples giving God the honour of his might."),
 (285605,"ascribe (yahab)","action","the peoples","ascribe","the glory due God's name",GOD,"paired with bringing an offering","v8: 'ASCRIBE (yahab) to the LORD the glory due his name' - the honour owed God's name, worship as tribute."),
 (285609,"bring (nasa)","action","the worshippers","bring","an offering into God's courts",GOD,"paired with ascribing glory","v8: 'BRING (nasa) an offering, and come into his courts!' - the offering carried to God, worship enacted in gift."),
 (285614,"worship (shachah)","action","all the earth","worship","the LORD in holy splendour",GOD,"paired with trembling before him","v9: 'WORSHIP (shachah) the LORD in the splendour of holiness' - the reverent prostration before the holy God."),
 (285618,"tremble (chul)","state","all the earth","tremble","before God",IB,"paired with worshipping","v9: 'TREMBLE (chul) before him, all the earth!' - the awe of the whole earth before God, worship shot through with holy fear."),
]
for a in CH: r.ch(*a)
QU=[
 (285567,"name (shem)",285566,"v2: 'bless his NAME (shem)' - God's name. Qualifier."),
 (285570,"salvation (yeshuah)",285568,"v2: 'tell of his SALVATION (yeshuah)' - God's saving. Qualifier."),
 (285575,"glory (kabod)",285574,"v3: 'Declare his GLORY (kabod) among the nations' - God's glory. Qualifier."),
 (285578,"marvelous works (pala)",285574,"v3: 'his MARVELLOUS WORKS (pala) among all the peoples' - God's wonders. Qualifier."),
 (285585,"praised (halal)",285618,"v4: 'greatly to be PRAISED (halal)' - God's praiseworthiness. Qualifier."),
 (285586,"feared (yare)",285618,"v4: 'he is to be FEARED (yare) above all gods' - God's fearsomeness. Qualifier."),
 (307151,"made (asah)",285574,"v5: 'but the LORD MADE (asah) the heavens' - God the creator. Qualifier."),
 (285590,"splendor (hod)",285614,"v6: 'SPLENDOUR (hod) and majesty are before him' - God's splendour. Qualifier."),
 (285591,"majesty (hadar)",285614,"v6: 'splendour and MAJESTY (hadar) are before him' - God's majesty. Qualifier."),
 (285593,"strength (oz)",285614,"v6: 'STRENGTH (oz) and beauty are in his sanctuary' - God's strength. Qualifier."),
 (285594,"beauty (tiphereth)",285614,"v6: 'strength and BEAUTY (tiphereth) are in his sanctuary' - God's beauty. Qualifier."),
 (285603,"glory (kabod)",285597,"v7: 'ascribe to the LORD GLORY (kabod) and strength' - God's glory. Qualifier."),
 (285604,"strength (oz)",285597,"v7: 'ascribe to the LORD glory and STRENGTH (oz)' - God's strength. Qualifier."),
 (285607,"glory (kabod)",285605,"v8: 'the GLORY (kabod) due his name' - God's glory. Qualifier."),
 (285608,"name (shem)",285605,"v8: 'the glory due his NAME (shem)' - God's name. Qualifier."),
 (285616,"splendor (hadarah)",285614,"v9: 'in the SPLENDOUR (hadarah) of holiness' - the holy splendour of God. Qualifier."),
 (285617,"holiness (qodesh)",285614,"v9: 'the splendour of HOLINESS (qodesh)' - God's holiness. Qualifier."),
 (285525,"reigns (malak)",285618,"v10: 'Say among the nations, The LORD REIGNS (malak)!' - God's kingship. Qualifier."),
 (285528,"established (kun)",285618,"v10: 'the world is ESTABLISHED (kun)' - God's firm ordering. Qualifier."),
 (285530,"moved (mot)",285618,"v10: 'it shall never be MOVED (mot)' - God's stable rule. Qualifier."),
 (285531,"judge (din)",285618,"v10: 'he will JUDGE (din) the peoples with equity' - God's just judgment. Qualifier."),
 (285533,"equity (meshar)",285618,"v10: 'judge the peoples with EQUITY (meshar)' - God's equity. Qualifier."),
 (285556,"judge (shaphat)",285614,"v13: 'for he comes to JUDGE (shaphat) the earth' - God's coming judgment. Qualifier."),
 (285558,"judge (shaphat)",285614,"v13: 'He will JUDGE (shaphat) the world in righteousness' - God's judgment. Qualifier."),
 (285560,"righteousness (tsedeq)",285614,"v13: 'judge the world in RIGHTEOUSNESS (tsedeq)' - God's righteousness. Qualifier."),
 (285563,"faithfulness (emunah)",285614,"v13: 'and the peoples in his FAITHFULNESS (emunah)' - God's faithfulness. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (307149,"worthless idols (elil)","v5: 'all the gods of the peoples are WORTHLESS IDOLS (elil)' - the empty idols, contrasted with God. Standalone."),
 (285596,"sanctuary (miqdash)","v6: 'strength and beauty are in his SANCTUARY (miqdash)' - God's holy place. Standalone."),
 (285599,"families (mishpachah)","v7: 'O FAMILIES (mishpachah) of the peoples' - the clans of the nations, the worshippers addressed. Standalone."),
 (285610,"offering (minchah)","v8: 'bring an OFFERING (minchah)' - the gift brought to God (char bring, 285609). Standalone."),
 (285613,"courts (chatser)","v8: 'and come into his COURTS (chatser)' - the temple courts, place of worship. Standalone."),
 (285535,"glad (samach)","v11: 'Let the HEAVENS be glad (samach)' - the heavens' joy, creation-personification. Standalone."),
 (285537,"rejoice (gil)","v11: 'and let the earth REJOICE (gil)' - the earth's joy, cosmic personification. Standalone."),
 (285539,"roar (raam)","v11: 'let the sea ROAR (raam)' - the sea's acclaim, cosmic personification. Standalone."),
 (285540,"fills (melo)","v11: 'and all that FILLS (melo) it' - the sea's fullness joining the praise, image. Standalone."),
 (285541,"field (sadeh)","v12: 'let the FIELD (sadeh) exult' - the field's joy, cosmic personification. Standalone."),
 (285542,"exult (alaz)","v12: 'let the field EXULT (alaz), and everything in it!' - the field's exultation, cosmic personification. Standalone."),
 (285546,"trees (ets)","v12: 'then shall all the TREES (ets) of the forest sing for joy' - the trees' praise, cosmic personification. Standalone."),
 (285548,"sing for joy (ranan)","v12: 'all the trees of the forest SING FOR JOY (ranan)' - the forest's song, creation joining worship (cosmic, not human IB). Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
