import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,98,
  note="Ps98 'Sing a new song' enthronement hymn (9v). Human IB = the worship acts: SING a new song; make a JOYFUL-NOISE, break into JOYOUS-SONG + SING-PRAISES (x2); JOYFUL-NOISE before the King. God's marvelous-things/salvation/righteousness/steadfast-love/faithfulness/judge = qualifiers; lyre/trumpet/horn + the COSMIC joy (sea roar, rivers clap, hills sing) = standalone.")
CH=[
 (285717,"sing (shir)","action","the worshippers","sing","a new song to the LORD",GOD,"paired with the joyful noise","v1: 'Oh SING (shir) to the LORD a new song, for he has done marvellous things!' - fresh praise for God's saving wonders."),
 (285749,"joyful noise (rua)","action","all the earth","make a joyful noise","to the LORD",GOD,"paired with breaking into song","v4: 'Make a JOYFUL NOISE (rua) to the LORD, all the earth' - the glad shout of the whole earth to God the King."),
 (285754,"joyous song (ranan)","action","all the earth","break into joyous song","to God",GOD,"paired with singing praises","v4: 'break forth into JOYOUS SONG (ranan) and sing praises!' - the outburst of joyful worship."),
 (285755,"sing praises (zamar)","action","all the earth","sing praises","to God",GOD,"paired with the joyous song","v4: 'break forth into joyous song and SING PRAISES (zamar)!' - the sung praise of God the King."),
 (285756,"sing praises (zamar)","action","the worshippers","sing praises","to the LORD with the lyre",GOD,"paired with the joyful noise","v5: 'SING PRAISES (zamar) to the LORD with the lyre' - the instrument-accompanied praise of God."),
 (285767,"joyful noise (rua)","action","the worshippers","make a joyful noise","before the King, the LORD",GOD,"paired with singing praises","v6: 'make a JOYFUL NOISE (rua) before the King, the LORD!' - the acclamation of God as King."),
]
for a in CH: r.ch(*a)
QU=[
 (285722,"done (asah)",285717,"v1: 'for he has DONE (asah) marvellous things!' - God's working. Qualifier."),
 (285723,"marvelous things (pala)",285717,"v1: 'he has done MARVELLOUS THINGS (pala)' - God's wonders. Qualifier."),
 (285725,"holy (qodesh)",285717,"v1: 'his HOLY (qodesh) arm have worked salvation' - God's holy power. Qualifier."),
 (285726,"arm (zeroa)",285717,"v1: 'his right hand and his holy ARM (zeroa)' - God's mighty arm. Qualifier."),
 (285727,"salvation (yasha)",285717,"v1: 'have worked SALVATION (yasha) for him' - God's saving. Qualifier."),
 (285729,"made known (yada)",285717,"v2: 'The LORD has made KNOWN (yada) his salvation' - God's revealing. Qualifier."),
 (285730,"salvation (yeshuah)",285717,"v2: 'made known his SALVATION (yeshuah)' - God's salvation. Qualifier."),
 (285731,"revealed (galah)",285717,"v2: 'he has REVEALED (galah) his righteousness' - God's disclosing. Qualifier."),
 (285733,"righteousness (tsedaqah)",285717,"v2: 'revealed his RIGHTEOUSNESS (tsedaqah)' - God's righteousness. Qualifier."),
 (285736,"remembered (zakar)",285717,"v3: 'He has REMEMBERED (zakar) his steadfast love' - God's mindful faithfulness. Qualifier."),
 (285737,"steadfast love (chesed)",285717,"v3: 'his STEADFAST LOVE (chesed)' - God's covenant love. Qualifier."),
 (285738,"faithfulness (emunah)",285717,"v3: 'and FAITHFULNESS (emunah) to the house of Israel' - God's faithfulness. Qualifier."),
 (285745,"seen (raah)",285717,"v3: 'all the ends of the earth have SEEN (raah) the salvation' - the earth beholding God's salvation. Qualifier."),
 (285746,"salvation (yeshuah)",285717,"v3: 'have seen the SALVATION (yeshuah) of our God' - God's salvation. Qualifier."),
 (285782,"judge (shaphat)",285767,"v9: 'for he comes to JUDGE (shaphat) the earth' - God's coming judgment. Qualifier."),
 (285784,"judge (shaphat)",285767,"v9: 'He will JUDGE (shaphat) the world with righteousness' - God's judgment. Qualifier."),
 (285786,"righteousness (tsedeq)",285767,"v9: 'judge the world with RIGHTEOUSNESS (tsedeq)' - God's righteousness. Qualifier."),
 (285788,"equity (meshar)",285767,"v9: 'and the peoples with EQUITY (meshar)' - God's equity. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (285753,"break forth (patsach)","v4: 'BREAK FORTH (patsach) into joyous song' - the bursting into song, manner of the worship (char, 285754). Standalone."),
 (285761,"sound (qol)","v5: 'with the lyre and the SOUND (qol) of melody!' - the music's sound, worship-medium. Standalone."),
 (285762,"melody (zimrah)","v5: 'the sound of MELODY (zimrah)' - the tune, worship-medium. Standalone."),
 (285764,"trumpets (chatsotserah)","v6: 'With TRUMPETS (chatsotserah)' - the instrument. Standalone."),
 (285765,"sound (qol)","v6: 'and the SOUND (qol) of the horn' - the horn-blast, worship-medium. Standalone."),
 (285766,"horn (shophar)","v6: 'the sound of the HORN (shophar)' - the ram's horn, instrument. Standalone."),
 (307160,"roar (raam)","v7: 'Let the sea ROAR (raam)' - the sea's acclaim, cosmic personification. Standalone."),
 (307161,"fills (melo)","v7: 'and all that FILLS (melo) it' - the sea's fullness joining praise, image. Standalone."),
 (285771,"rivers (nahar)","v8: 'Let the RIVERS (nahar) clap their hands' - the rivers' applause, cosmic personification. Standalone."),
 (285772,"clap (machah)","v8: 'let the rivers CLAP (machah) their hands' - the applause of the waters, cosmic personification. Standalone."),
 (285775,"sing for joy (ranan)","v8: 'let the hills SING FOR JOY (ranan) together' - the hills' song, creation joining worship (cosmic, not human IB). Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
