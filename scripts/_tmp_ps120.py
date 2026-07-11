import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,120,
  note="Ps120 first Song of Ascents (7v). Char-arcs: A the cry v1 (in distress I CALLED, he answered); B plea against deceit v2-3 (deliver ME from LYING lips, a DECEITFUL tongue); C sojourn among war-lovers v5-7 (woe that I SOJOURN; the self dwelling too long among those who HATE peace; I am for PEACE, but they are for war). God's answer/deliver = qualifiers; warrior's-arrows/broom-coals + Kedar imagery = standalone.")
CH=[
 (272296,"call (qara)","action","the psalmist","call","to the LORD in distress",GOD,"paired with God's answer",
  "v1: 'In my distress I CALLED (qara) to the LORD, and he answered me' - the cry from distress that God answered, the psalm's opening."),
 (272302,"me / soul (nephesh)","faculty","the psalmist","be delivered","from lying lips",IB,"paired with the lying and deceit",
  "v2: 'DELIVER ME (nephesh), O LORD, from lying lips' - the self pleading rescue from the deceit that surrounds it."),
 (272305,"lying (sheqer)","disposition","the enemies","lie","against the psalmist",IB,"paired with the deceitful tongue",
  "v2: 'from LYING (sheqer) lips' - the falsehood of the foes from which the psalmist begs deliverance."),
 (272308,"deceitful (remiyah)","disposition","the enemies","deceive","with the tongue",IB,"paired with the lying lips",
  "v2: 'from a DECEITFUL (remiyah) tongue' - the treacherous speech the psalmist would be freed from."),
 (272314,"deceitful (remiyah)","disposition","the deceitful tongue","deceive","the psalmist",IB,"paired with the judgment it invites",
  "v3: 'What shall be done to you, you DECEITFUL (remiyah) tongue?' - the treacherous tongue addressed, its recompense weighed."),
 (307783,"sojourn (gur)","state","the psalmist","sojourn as a stranger","among the hostile",IB,"paired with dwelling among the peace-haters",
  "v5: 'Woe to me, that I SOJOURN (gur) in Meshech' - the lament of the pilgrim exiled among aliens, a stranger far from home."),
 (272317,"I / soul (nephesh)","faculty","the psalmist","dwell too long","among peace-haters",IB,"paired with those who hate peace",
  "v6: 'Too long have I (nephesh) had my dwelling among those who hate peace' - the self worn by long dwelling amid enmity."),
 (272320,"hate (sane)","disposition","the enemies","hate","peace",IB,"paired with the psalmist's love of peace",
  "v6: 'among those who HATE (sane) peace' - the enmity of those the psalmist dwells among, haters of the peace he seeks."),
 (272323,"peace (shalom)","disposition","the psalmist","be for peace","toward the hostile",IB,"paired with their bent for war",
  "v7: 'I am for PEACE (shalom), but when I speak, they are for war' - the psalmist's peaceable heart, met with the foes' appetite for war."),
]
for a in CH: r.ch(*a)
QU=[
 (272299,"answered (anah)",272296,"v1: 'and he ANSWERED (anah) me' - God's answer to the cry. Qualifier."),
 (272301,"deliver (natsal)",272302,"v2: 'DELIVER (natsal) me, O LORD, from lying lips' - God's rescue petitioned. Qualifier."),
 (272311,"given (nathan)",272314,"v3: 'What shall be GIVEN (nathan) to you' - God's recompense on the deceitful tongue. Qualifier."),
 (272313,"done (yasaph)",272314,"v3: 'and what more shall be DONE (yasaph) to you' - God's requital on the deceitful tongue. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (272292,"Song (shir)","v0 superscription: 'A SONG (shir) of Ascents' - the psalm-heading. Standalone."),
 (272293,"Ascents (maalah)","v0 superscription: 'A Song of ASCENTS (maalah)' - the pilgrim-song heading. Standalone."),
 (272295,"distress (tsarah)","v1: 'In my DISTRESS (tsarah) I called' - the trouble from which he cried; circumstance. Standalone."),
 (272306,"lips (saphah)","v2: 'from lying LIPS (saphah)' - the lips of the liars (char lying, 272305), image. Standalone."),
 (272309,"tongue (lashon)","v2: 'from a deceitful TONGUE (lashon)' - the organ of deceit (char deceitful, 272308), image. Standalone."),
 (272315,"tongue (lashon)","v3: 'you deceitful TONGUE (lashon)' - the treacherous tongue addressed (char deceitful, 272314), image. Standalone."),
 (307776,"warrior's (gibbor)","v4: 'A WARRIOR'S (gibbor) sharp arrows' - the soldier's weapon, image of the tongue's recompense. Standalone."),
 (307777,"sharp (shanan)","v4: 'a warrior's SHARP (shanan) arrows' - the honed arrows, image. Standalone."),
 (307778,"arrows (chets)","v4: 'a warrior's sharp ARROWS (chets)' - the arrows of judgment, image. Standalone."),
 (307779,"glowing coals (gachal)","v4: 'with GLOWING coals (gachal) of the broom tree!' - the burning coals, image of the tongue's punishment. Standalone."),
 (307780,"broom tree (rethem)","v4: 'coals of the BROOM TREE (rethem)!' - the hot-burning broom-wood, image. Standalone."),
 (307781,"woe (oyah)","v5: 'WOE (oyah) to me, that I sojourn in Meshech' - the lament of the exiled (char sojourn, 307783). Standalone."),
 (307785,"dwell (shakan)","v5: 'that I DWELL (shakan) among the tents of Kedar!' - the dwelling among the hostile nomads, image. Standalone."),
 (272318,"dwelling (shakan)","v6: 'Too long have I had my DWELLING (shakan) among those who hate peace' - the long dwelling amid enmity (char I, 272317). Standalone."),
 (272321,"peace (shalom)","v6: 'those who hate PEACE (shalom)' - the peace the foes hate (char hate, 272320), object. Standalone."),
 (272325,"speak (dabar)","v7: 'but when I SPEAK (dabar), they are for war' - the psalmist's peaceable word met with hostility, image. Standalone."),
 (272327,"war (milchamah)","v7: 'they are for WAR (milchamah)' - the foes' appetite for war, against the psalmist's peace (char, 272323). Standalone."),
]: r.st(sid,sense,d)
r.write()
