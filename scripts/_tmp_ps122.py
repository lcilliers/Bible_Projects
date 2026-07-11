import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,122,
  note="Ps122 'I was glad... to the house of the LORD' (9v). Human IB: the GLADNESS at going to God's house v1; the THANKSGIVING the tribes go up to give v4; the closing devotion to the city - PRAY for its peace, may those who LOVE it be secure, I will SEEK your good v6-9. Jerusalem itself (built/bound-firmly/thrones/walls) + the peace-blessings = imagery/standalone. God's name = qualifier.")
CH=[
 (272385,"glad (samach)","state","the psalmist","be glad","at going to God's house",IB,"paired with the pilgrimage to Jerusalem",
  "v1: 'I was GLAD (samach) when they said to me, Let us go to the house of the LORD!' - the pilgrim's joy at the summons to worship, gladness at the very thought of God's house."),
 (272408,"give thanks (yadah)","action","the tribes","give thanks","to the name of the LORD",GOD,"paired with the tribes going up",
  "v4: 'to which the tribes go up... to GIVE THANKS (yadah) to the name of the LORD' - the thanksgiving that is the aim of the pilgrimage, the tribes gathered to praise God's name."),
 (272418,"pray (shaal)","action","the pilgrims","pray","for the peace of Jerusalem",GOD,"paired with love for the city",
  "v6: 'PRAY (shaal) for the peace of Jerusalem!' - the summons to intercede for the city, prayer as the pilgrim's love in action."),
 (272422,"love (aheb)","disposition","the pilgrims","love","Jerusalem",IB,"paired with praying for its peace",
  "v6: 'May they be secure who LOVE you!' - the love for the holy city, whose lovers are blessed with security."),
 (272439,"seek (baqash)","action","the psalmist","seek","the good of Jerusalem",PER,"paired with the sake of brothers and God's house",
  "v9: 'For the sake of the house of the LORD our God, I will SEEK (baqash) your good' - the resolve to pursue the city's welfare, love issuing in active seeking of its good."),
]
for a in CH: r.ch(*a)
r.qu(272409,"name (shem)",272408,"v4: 'to give thanks to the NAME (shem) of the LORD' - God's name. Qualifier.")
for sid,sense,d in [
 (272383,"Ascents (maalah)","v0 superscription: 'A Song of ASCENTS (maalah), of David' - the pilgrim-song heading. Standalone."),
 (272391,"standing (amad)","v2: 'Our feet have been STANDING (amad) within your gates, O Jerusalem!' - the pilgrims arrived at the gates, image. Standalone."),
 (272395,"built (banah)","v3: 'Jerusalem - BUILT (banah) as a city that is bound firmly together' - the well-built city, image of unity. Standalone."),
 (272398,"bound firmly (chabar)","v3: 'a city that is BOUND FIRMLY (chabar) together' - the compact, united city, image. Standalone."),
 (272401,"tribes (shebet)","v4: 'to which the TRIBES (shebet) go up' - the tribes of Israel, the pilgrims. Standalone."),
 (272402,"go up (alah)","v4: 'to which the tribes GO UP (alah)' - the pilgrimage ascent (char give-thanks, 272408), image. Standalone."),
 (272403,"tribes (shebet)","v4: 'the TRIBES (shebet) of the LORD' - the LORD's tribes, image. Standalone."),
 (272405,"decreed (edut)","v4: 'as was DECREED (edut) for Israel' - the ordinance of pilgrimage, image. Standalone."),
 (272412,"thrones (kisse)","v5: 'There THRONES (kisse) for judgment were set' - the royal judgment-seats, image of Jerusalem as seat of justice. Standalone."),
 (272413,"judgment (mishpat)","v5: 'thrones for JUDGMENT (mishpat)' - the justice administered in the city, image. Standalone."),
 (272414,"set (yashab)","v5: 'thrones for judgment were SET (yashab)' - the establishing of the judgment-seats, image. Standalone."),
 (272415,"thrones (kisse)","v5: 'the THRONES (kisse) of the house of David' - the Davidic seats, image. Standalone."),
 (272419,"peace (shalom)","v6: 'Pray for the PEACE (shalom) of Jerusalem!' - the peace of the city, object of the prayer (char pray, 272418). Standalone."),
 (272421,"be secure (shalah)","v6: 'May they be SECURE (shalah) who love you!' - the security promised the city's lovers (char love, 272422), image. Standalone."),
 (272424,"peace (shalom)","v7: 'PEACE (shalom) be within your walls' - the peace pronounced on the city, blessing-image. Standalone."),
 (272425,"walls (chel)","v7: 'Peace be within your WALLS (chel)' - the city's ramparts, image. Standalone."),
 (272426,"security (shalvah)","v7: 'and SECURITY (shalvah) within your towers!' - the safety wished the city, image. Standalone."),
 (272433,"peace (shalom)","v8: 'For my brothers and companions' sake I will say, PEACE (shalom) be within you!' - the peace the psalmist pronounces for his brethren's sake, blessing-image. Standalone."),
 (272441,"good (tob)","v9: 'I will seek your GOOD (tob)' - the welfare of the city the psalmist seeks (char seek, 272439), object. Standalone."),
]: r.st(sid,sense,d)
r.write()
