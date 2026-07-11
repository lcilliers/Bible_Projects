import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,135,
  note="Ps135 Hallel (21v). Human IB: the call to PRAISE (x5) + SING (delight in it, pleasant); KNOWing God's greatness; the idol-makers who BECOME-LIKE their dead idols + all who TRUST them (trust deadening the truster); the fourfold call to BLESS (Israel/Aaron/Levi/those who FEAR). God's deeds (chose/does/struck/gave/vindicate/compassion) = qualifiers; dead-idol catalogue + Egypt/kings imagery = standalone.")
CH=[
 (273045,"praise (halal)","action","the servants","praise","the LORD",GOD,"paired with the fivefold call to praise","v1: 'PRAISE (halal) the LORD! Praise the name of the LORD' - the opening Hallelujah."),
 (273047,"praise (halal)","action","the servants","praise","the LORD",GOD,"paired with the call","v1: 'PRAISE (halal), O servants of the LORD' - the servants summoned to worship."),
 (273050,"praise (halal)","action","the servants","praise","the name of the LORD",GOD,"paired with the call","v1: 'PRAISE (halal) the name of the LORD!' - the worship of God's name."),
 (273117,"praise (halal)","action","the servants","praise","the LORD, for he is good",GOD,"paired with singing","v3: 'PRAISE (halal) the LORD, for the LORD is good' - praise grounded in God's goodness."),
 (273121,"sing (zamar)","action","the servants","sing","to God's pleasant name",GOD,"paired with praising","v3: 'SING (zamar) to his name, for it is pleasant!' - the operation of delighted praise: singing because the worship itself is sweet."),
 (307888,"know (yada)","disposition","the psalmist","know","God's greatness",GOD,"paired with God's sovereign doing","v5: 'For I KNOW (yada) that the LORD is great' - the settled knowledge of God's greatness that grounds the praise."),
 (273096,"become like (kemo)","state","the idol-makers","become like","the dead idols they make",IB,"paired with those who trust them","v18: 'Those who make them BECOME LIKE (kemo) them' - the operation of idolatry deadening its maker: to fashion a lifeless god is to be reduced to its lifelessness."),
 (273099,"trust (batach)","disposition","the idolaters","trust","in dead idols",IB,"paired with becoming like them","v18: 'so do all who TRUST (batach) in them' - the misplaced trust that shares the idol's deadness, reliance on nothing hollowing out the truster."),
 (307926,"bless (barak)","action","the house of Israel","bless","the LORD",GOD,"paired with the fourfold blessing","v19: 'O house of Israel, BLESS (barak) the LORD!' - the people summoned to bless God."),
 (307930,"bless (barak)","action","the house of Aaron","bless","the LORD",GOD,"paired with the fourfold blessing","v19: 'O house of Aaron, BLESS (barak) the LORD!' - the priests summoned to bless."),
 (273103,"bless (barak)","action","the house of Levi","bless","the LORD",GOD,"paired with the fourfold blessing","v20: 'O house of Levi, BLESS (barak) the LORD!' - the Levites summoned to bless."),
 (273105,"fear (yare)","disposition","those who fear God","fear / revere","the LORD",GOD,"paired with blessing him","v20: 'You who FEAR (yare) the LORD, bless the LORD!' - the reverent summoned to bless."),
 (273107,"bless (barak)","action","the God-fearers","bless","the LORD",GOD,"paired with fearing him","v20: 'You who fear the LORD, BLESS (barak) the LORD!' - the fourth call to bless, the God-fearers."),
 (273109,"bless (barak)","action","the worshippers","bless","the LORD from Zion",GOD,"paired with the closing praise","v21: 'BLESSED (barak) be the LORD from Zion, he who dwells in Jerusalem!' - the blessing pronounced from the holy city."),
 (273115,"praise (halal)","action","the worshippers","praise","the LORD",GOD,"paired with blessing him","v21: 'PRAISE (halal) the LORD!' - the closing Hallelujah."),
]
for a in CH: r.ch(*a)
BL=273109
QU=[(273048,"name (shem)"),(273120,"good (tob)"),(273122,"name (shem)"),(273126,"chosen (bachar)"),(273132,"pleases (chaphets)"),(273133,"does (asah)"),(307898,"makes (asah)"),(307901,"brings forth (yatsa)"),(307904,"struck down (nakah)"),(273143,"sent (shalach)"),(273145,"wonders (mopheth)"),(273054,"struck down (nakah)"),(273057,"killed (harag)"),(273060,"gave (nathan)"),(273067,"name (shem)"),(273070,"renown (zeker)"),(273075,"vindicate (din)"),(273077,"compassion (nacham)"),(273095,"make (asah)")]
for sid,sense in QU: r.qu(sid,sense,BL,f"'{sense}' - God's act/attribute in the litany of praise. Qualifier.")
ST=[(307879,"stand"),(307883,"courts"),(273123,"pleasant"),(273129,"own possession"),(273140,"deeps"),(307894,"clouds"),(307895,"rise"),(307896,"end of the earth"),(307899,"lightnings"),(307900,"rain"),(307902,"wind"),(307903,"storehouses"),(307905,"firstborn"),(307908,"beast"),(273144,"signs"),(273058,"mighty"),(273059,"kings"),(307910,"king (Sihon)"),(307913,"king (Og)"),(307916,"kingdoms"),(273062,"heritage"),(273063,"heritage"),(273069,"endures forever"),(273080,"idols"),(273083,"gold"),(273084,"work of hands"),(307918,"mouths"),(307920,"speak"),(307923,"see"),(273089,"hear"),(273092,"breath"),(273094,"mouths"),(273113,"dwells")]
for sid,sense in ST: r.st(sid,sense,f"'{sense}' - image (God's deeds / dead-idol catalogue / place). Standalone.")
r.write()
