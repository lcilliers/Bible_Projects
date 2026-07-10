import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,108,
  note="Ps108 David's composite worship+plea (13v; from Ps57+60). Char-arcs: A steadfast-heart worship v1-3 (HEART steadfast, SING/MAKE-MELODY with all my BEING, GIVE-THANKS, SING-PRAISES); B confidence in the plea v12-13 (VAIN is the salvation of man; with God we do VALIANTLY). Between = God's steadfast-love/faithfulness/exaltation + the oracle dividing the land (Shechem/Moab-washbasin) + the war-plea = qualifiers/imagery.")
CH=[
 (270076,"heart (leb)","faculty","the psalmist","be steadfast","toward God",IB,"paired with singing and making melody",
  "v1: 'My HEART (leb) is steadfast, O God!' - the fixed, resolute inner self, worship springing from a settled heart."),
 (270079,"sing (shir)","action","the psalmist","sing","to God",GOD,"paired with making melody and the steadfast heart",
  "v1: 'I will SING (shir) and make melody with all my being!' - the sung praise of the steadfast heart."),
 (270080,"make melody (zamar)","action","the psalmist","make melody","to God",GOD,"paired with singing",
  "v1: 'I will sing and MAKE MELODY (zamar)' - the music of worship from a fixed heart."),
 (270083,"being (kabod)","faculty","the psalmist","worship with the whole self","toward God",IB,"paired with the heart and singing",
  "v1: 'with all my BEING (kabod)!' - the whole self, glory and soul, engaged in praise, nothing held back."),
 (270112,"give thanks (yadah)","action","the psalmist","give thanks","to God among the peoples",GOD,"paired with singing praises",
  "v3: 'I will GIVE THANKS (yadah) to you, O LORD, among the peoples' - the public thanksgiving, praise carried to the nations."),
 (270115,"sing praises (zamar)","action","the psalmist","sing praises","to God among the nations",GOD,"paired with giving thanks",
  "v3: 'I will SING PRAISES (zamar) to you among the nations' - the sung praise before the peoples."),
 (270096,"vain (shav)","disposition","the psalmist","reckon human help vain","against God's",IB,"paired with doing valiantly through God",
  "v12: 'for VAIN (shav) is the salvation of man' - the reckoning that human help is worthless, confidence turned from man to God."),
 (270102,"valiantly (chayil)","disposition","we (with God)","act valiantly","through God",GOD,"paired with the vanity of human help",
  "v13: 'With God we shall DO VALIANTLY (chayil)' - the courage that is God's gift, valour grounded not in man but in him."),
]
for a in CH: r.ch(*a)
A=270076; B=270102
QU=[
 (270119,"steadfast love (chesed)",A,"v4: 'For your STEADFAST LOVE (chesed) is great above the heavens' - God's covenant love. Qualifier."),
 (270124,"faithfulness (emeth)",A,"v4: 'your FAITHFULNESS (emeth) reaches to the clouds' - God's faithfulness. Qualifier."),
 (270126,"be exalted (rum)",A,"v5: 'Be EXALTED (rum), O God, above the heavens!' - God's exaltation petitioned. Qualifier."),
 (270130,"glory (kabod)",A,"v5: 'Let your GLORY (kabod) be over all the earth!' - God's glory. Qualifier."),
 (270136,"delivered (chalats)",B,"v6: 'that your beloved ones may be DELIVERED (chalats)' - God's deliverance. Qualifier."),
 (270137,"give salvation (yasha)",B,"v6: 'GIVE SALVATION (yasha) by your right hand and answer me!' - God's saving petitioned. Qualifier."),
 (270139,"answer (anah)",B,"v6: 'and ANSWER (anah) me!' - God's answer petitioned. Qualifier."),
 (270143,"holiness (qodesh)",B,"v7: 'God has spoken in his HOLINESS (qodesh)' - God's holy word. Qualifier."),
 (270144,"exultation (alaz)",B,"v7: 'With EXULTATION (alaz) I will divide up Shechem' - God's exultant claim (his oracle). Qualifier."),
 (270145,"divide up (chalaq)",B,"v7: 'I will DIVIDE UP (chalaq) Shechem' - God's parcelling of the land. Qualifier."),
 (270147,"portion out (madad)",B,"v7: 'and PORTION OUT (madad) the Valley of Succoth' - God's measuring of the land. Qualifier."),
 (307536,"cast (shalak)",B,"v9: 'upon Edom I CAST (shalak) my shoe' - God's claim of possession over Edom. Qualifier."),
 (307540,"shout in triumph (rua)",B,"v9: 'over Philistia I SHOUT IN TRIUMPH (rua)' - God's triumph over Philistia. Qualifier."),
 (307542,"bring (yabal)",B,"v10: 'Who will BRING (yabal) me to the fortified city?' - God alone can bring the victory. Qualifier."),
 (307546,"lead (nachah)",B,"v10: 'Who will LEAD (nachah) me to Edom?' - God's leading to conquest. Qualifier."),
 (270085,"reject (zanach)",B,"v11: 'Have you not REJECTED (zanach) us, O God?' - God's apparent rejection, the ground of the plea. Qualifier."),
 (270091,"armies (tsaba)",B,"v11: 'you do not go out with our ARMIES (tsaba)' - God's not going out with the hosts. Qualifier."),
 (270092,"grant (yahab)",B,"v12: 'Oh GRANT (yahab) us help against the foe' - God's help petitioned. Qualifier."),
 (270093,"help (ezrah)",B,"v12: 'grant us HELP (ezrah) against the foe' - God's help. Qualifier."),
 (270101,"do (asah)",B,"v13: 'With God we shall DO (asah) valiantly' - the doing empowered by God (with char valiantly, 270102). Qualifier."),
 (270104,"tread down (bus)",B,"v13: 'it is he who will TREAD DOWN (bus) our foes' - God's treading down of the enemy. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (270107,"awake (ur)","v2: 'AWAKE (ur), O harp and lyre!' - the summons to the instruments, image of rousing worship. Standalone."),
 (270110,"awake (ur)","v2: 'I will AWAKE (ur) the dawn!' - the psalmist rousing the dawn with praise, image. Standalone."),
 (270111,"dawn (shachar)","v2: 'I will awake the DAWN (shachar)!' - the daybreak roused by early worship, image. Standalone."),
 (270125,"clouds (shachaq)","v4: 'your faithfulness reaches to the CLOUDS (shachaq)' - the height of the skies, image of God's faithfulness. Standalone."),
 (270135,"beloved ones (yadid)","v6: 'that your BELOVED ONES (yadid) may be delivered' - God's beloved people, the object of the deliverance. Standalone."),
 (270148,"Valley of Succoth (emeq)","v7: 'portion out the VALLEY (emeq) of Succoth' - the land parcelled in the oracle, place. Standalone."),
 (270149,"Succoth (sukkoth)","v7: 'the Valley of SUCCOTH (sukkoth)' - the place in the oracle. Standalone."),
 (270153,"helmet (maoz)","v8: 'Ephraim is my HELMET (maoz)' - Ephraim as God's stronghold, image. Standalone."),
 (270155,"scepter (chaqaq)","v8: 'Judah my SCEPTRE (chaqaq)' - Judah as God's ruling staff, image. Standalone."),
 (307533,"washbasin (sir)","v9: 'Moab is my WASHBASIN (sir)' - Moab as a menial vessel, image of subjection. Standalone."),
 (307537,"shoe (naal)","v9: 'upon Edom I cast my SHOE (naal)' - the shoe as a token of possession, image. Standalone."),
 (307543,"fortified (mibtsar)","v10: 'Who will bring me to the FORTIFIED (mibtsar) city?' - the walled city of Edom, image. Standalone."),
 (270095,"foe (tsar)","v12: 'grant us help against the FOE (tsar)' - the enemy, object of the plea. Standalone."),
 (270097,"salvation (teshuah)","v12: 'for vain is the SALVATION (teshuah) of man' - human help, judged worthless (char vain, 270096). Standalone."),
 (270106,"foes (tsar)","v13: 'it is he who will tread down our FOES (tsar)' - the enemies God treads down, object. Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
