import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,99,
  note="Ps99 'The LORD reigns... holy is he' (9v; thrice-holy refrain). IB = worship + response: the peoples TREMBLE; PRAISE his awesome name; EXALT (x2) + WORSHIP (x2) at his footstool/holy mountain; Moses/Aaron/Samuel CALLED on him and KEPT his testimonies; the people's WRONGDOINGS God avenged. God's reign/holiness/might/loves-justice/answered/forgiving/avenger = qualifiers; cherubim/pillar-of-cloud/footstool + earth-quake imagery = standalone.")
CH=[
 (285792,"tremble (ragaz)","state","the peoples","tremble","before the enthroned God",IB,"paired with the earth quaking","v1: 'The LORD reigns; let the peoples TREMBLE (ragaz)!' - the awe of the nations before the King enthroned on the cherubim."),
 (285804,"praise (yadah)","action","the peoples","praise","God's awesome name",GOD,"paired with the holiness of God","v3: 'Let them PRAISE (yadah) your great and awesome name!' - the worship due God's holy name, praise as the fit response to holiness."),
 (285822,"exalt (rum)","action","the worshippers","exalt","the LORD our God",GOD,"paired with worshipping at his footstool","v5: 'EXALT (rum) the LORD our God' - the lifting-up of God in worship, the refrain of adoration."),
 (285825,"worship (shachah)","action","the worshippers","worship","at God's footstool",GOD,"paired with exalting God","v5: 'WORSHIP (shachah) at his footstool!' - the prostration before God, reverence at his holy place."),
 (285833,"call (qara)","action","Moses and Aaron","call upon","the LORD",GOD,"paired with keeping his testimonies","v6: 'Moses and Aaron... they CALLED (qara) upon the LORD' - the intercessory calling of the priests, prayer that God answered."),
 (285836,"call (qara)","action","Samuel","call upon","God's name",GOD,"paired with Moses and Aaron's calling","v6: 'Samuel also was among those who CALLED (qara) upon his name' - the prophet's prayer, joining the calling that God heard."),
 (285846,"keep (shamar)","action","the intercessors","keep","God's testimonies",GOD,"paired with calling upon God","v7: 'They KEPT (shamar) his testimonies and the statute that he gave them' - the obedience of God's servants, keeping joined to calling."),
 (307173,"wrongdoings (alilah)","state","the people","commit wrongdoings","avenged by God",IB,"paired with God as their avenger","v8: 'but an avenger of their WRONGDOINGS (alilah)' - the misdeeds of God's people, which even a forgiving God did not leave unpunished."),
 (285851,"exalt (rum)","action","the worshippers","exalt","the LORD our God",GOD,"paired with worshipping at his holy mountain","v9: 'EXALT (rum) the LORD our God' - the closing refrain of adoration, God lifted up in worship."),
 (285854,"worship (shachah)","action","the worshippers","worship","at God's holy mountain",GOD,"paired with exalting God","v9: 'and WORSHIP (shachah) at his holy mountain' - the reverent worship at Zion, homage to the holy God."),
]
for a in CH: r.ch(*a)
QU=[
 (285790,"reigns (malak)",285792,"v1: 'The LORD REIGNS (malak)' - God's kingship. Qualifier."),
 (285793,"sits enthroned (yashab)",285792,"v1: 'he SITS (yashab) enthroned upon the cherubim' - God's throne. Qualifier."),
 (285800,"exalted (rum)",285804,"v2: 'he is EXALTED (rum) over all the peoples' - God's supremacy. Qualifier."),
 (285806,"awesome (yare)",285804,"v3: 'your great and AWESOME (yare) name' - God's awesomeness. Qualifier."),
 (285807,"name (shem)",285804,"v3: 'your great and awesome NAME (shem)' - God's name. Qualifier."),
 (285808,"holy (qadosh)",285804,"v3: 'HOLY (qadosh) is he!' - God's holiness. Qualifier."),
 (285811,"might (oz)",285822,"v4: 'The King in his MIGHT (oz) loves justice' - God's power. Qualifier."),
 (285812,"loves (aheb)",285822,"v4: 'The King in his might LOVES (aheb) justice' - God's love of justice. Qualifier."),
 (285813,"justice (mishpat)",285822,"v4: 'the King in his might loves JUSTICE (mishpat)' - God's justice. Qualifier."),
 (285815,"established (kun)",285822,"v4: 'You have ESTABLISHED (kun) equity' - God's establishing of justice. Qualifier."),
 (285816,"equity (meshar)",285822,"v4: 'you have established EQUITY (meshar)' - God's equity. Qualifier."),
 (285818,"executed (asah)",285822,"v4: 'you have EXECUTED (asah) justice' - God's doing of justice. Qualifier."),
 (285819,"justice (mishpat)",285822,"v4: 'you have executed JUSTICE (mishpat)' - God's justice. Qualifier."),
 (285820,"righteousness (tsedaqah)",285822,"v4: 'and RIGHTEOUSNESS (tsedaqah) in Jacob' - God's righteousness. Qualifier."),
 (285827,"holy (qadosh)",285825,"v5: 'HOLY (qadosh) is he!' - God's holiness. Qualifier."),
 (285834,"name (shem)",285833,"v6: 'Samuel also... who called upon his NAME (shem)' - God's name. Qualifier."),
 (285840,"answered (anah)",285833,"v6: 'They called upon the LORD, and he ANSWERED (anah) them' - God's answer. Qualifier."),
 (285845,"spoke (dabar)",285846,"v7: 'he SPOKE (dabar) to them in the pillar of cloud' - God's speaking. Qualifier."),
 (285847,"testimonies (edah)",285846,"v7: 'They kept his TESTIMONIES (edah)' - God's testimonies. Qualifier."),
 (285848,"statute (choq)",285846,"v7: 'and the STATUTE (choq) that he gave them' - God's statute. Qualifier."),
 (307168,"answered (anah)",307173,"v8: 'O LORD our God, you ANSWERED (anah) them' - God's answer. Qualifier."),
 (307169,"forgiving (nasa)",307173,"v8: 'you were a FORGIVING (nasa) God to them' - God's pardon. Qualifier."),
 (307171,"avenger (naqam)",307173,"v8: 'but an AVENGER (naqam) of their wrongdoings' - God's requital. Qualifier."),
 (285855,"holy (qodesh)",285854,"v9: 'and worship at his HOLY (qodesh) mountain' - the holy mountain of God. Qualifier."),
 (285860,"holy (qadosh)",285854,"v9: 'for the LORD our God is HOLY (qadosh)!' - God's holiness. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (285794,"cherubim (kerub)","v1: 'he sits enthroned upon the CHERUBIM (kerub)' - the throne-guardians, image of God's kingship. Standalone."),
 (285796,"quake (nut)","v1: 'let the earth QUAKE (nut)!' - the earth's shaking, cosmic reaction (not human IB). Standalone."),
 (285826,"footstool (hadom)","v5: 'worship at his FOOTSTOOL (hadom)' - God's footstool (the ark/temple), place of worship. Standalone."),
 (285843,"pillar (ammud)","v7: 'he spoke to them in the PILLAR (ammud) of cloud' - the cloud-pillar of God's presence, image. Standalone."),
 (285844,"cloud (anan)","v7: 'in the pillar of CLOUD (anan)' - the cloud of theophany, image. Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
