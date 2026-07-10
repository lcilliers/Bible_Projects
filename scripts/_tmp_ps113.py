import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,113,
  note="Ps113 Hallel opener (9v). IB: A the call to PRAISE (x3) + BLESS God's name v1-3; B the objects of God's great reversal - the POOR raised from the dust, the NEEDY from the ash heap, the BARREN-WOMAN made a JOYOUS mother v7-9; closing PRAISE. God's seated-on-high/looks-down/raises/lifts/makes-sit/gives = qualifiers; sun-rising/dust/ash-heap/princes imagery = standalone.")
CH=[
 (270721,"praise (halal)","action","the worshippers","praise","the LORD",GOD,"paired with the servants' praise of his name",
  "v1: 'PRAISE (halal) the LORD!' - the opening Hallelujah of the Hallel."),
 (270723,"praise (halal)","action","the servants of the LORD","praise","the LORD",GOD,"paired with praising his name",
  "v1: 'PRAISE (halal), O servants of the LORD' - the summons to God's servants to worship."),
 (270726,"praise (halal)","action","the servants","praise","the name of the LORD",GOD,"paired with blessing his name",
  "v1: 'PRAISE (halal) the name of the LORD!' - the worship of God's name, the psalm's refrain-theme."),
 (270729,"bless (barak)","action","the worshippers","bless","the name of the LORD",GOD,"paired with praising his name",
  "v2: 'BLESSED (barak) be the name of the LORD from this time forth and forevermore!' - the blessing of God's name across all time."),
 (270763,"poor (dal)","status","the poor","be raised","from the dust by God",IB,"paired with the needy lifted from the ash heap",
  "v7: 'He raises the POOR (dal) from the dust' - the lowly whom God lifts, the first object of his great reversal."),
 (270767,"needy (ebyon)","status","the needy","be lifted","from the ash heap by God",IB,"paired with the poor raised from the dust",
  "v7: 'and lifts the NEEDY (ebyon) from the ash heap' - the destitute God raises to sit with princes."),
 (270779,"barren woman (aqar)","status","the barren woman","be given a home","and made a mother",IB,"paired with becoming a joyous mother",
  "v9: 'He gives the BARREN WOMAN (aqar) a home' - the childless woman, her reproach reversed by God's gift of a household."),
 (270781,"joyous (samach)","state","the once-barren woman","rejoice","as a mother of children",IB,"paired with being given a home",
  "v9: 'making her the JOYOUS (samach) mother of children' - the gladness of the once-barren, barrenness turned to a mother's joy."),
 (270784,"praise (halal)","action","the worshippers","praise","the LORD",GOD,"paired with the whole psalm's praise",
  "v9: 'PRAISE (halal) the LORD!' - the closing Hallelujah, sealing the psalm of God who lifts the lowly."),
]
for a in CH: r.ch(*a)
A=270726; B=270763
QU=[
 (270727,"name (shem)",A,"v1: 'praise the NAME (shem) of the LORD!' - God's name. Qualifier."),
 (270730,"be (hayah)",A,"v2: 'Blessed BE (hayah) the name of the LORD' - the blessing pronounced on God's name. Qualifier."),
 (270731,"name (shem)",A,"v2: 'the NAME (shem) of the LORD' - God's name. Qualifier."),
 (270741,"name (shem)",A,"v3: 'the NAME (shem) of the LORD is to be praised!' - God's name. Qualifier."),
 (270743,"praised (halal)",A,"v3: 'the name of the LORD is to be PRAISED (halal)!' - God's praiseworthiness. Qualifier."),
 (270745,"high (rum)",A,"v4: 'The LORD is HIGH (rum) above all nations' - God's exaltation. Qualifier."),
 (270749,"glory (kabod)",A,"v4: 'his GLORY (kabod) above the heavens!' - God's glory. Qualifier."),
 (270755,"seated (yashab)",A,"v5: 'who is SEATED (yashab) on high' - God enthroned on high. Qualifier."),
 (270757,"looks (raah)",A,"v6: 'who LOOKS (raah) far down on the heavens and the earth' - God's condescending regard. Qualifier."),
 (270758,"far down (shaphel)",A,"v6: 'who looks FAR DOWN (shaphel)' - God stooping to behold the lowly. Qualifier."),
 (270762,"raises (qum)",B,"v7: 'He RAISES (qum) the poor from the dust' - God's lifting of the poor. Qualifier."),
 (270766,"lifts (rum)",B,"v7: 'and LIFTS (rum) the needy from the ash heap' - God's raising of the needy. Qualifier."),
 (270771,"make sit (yashab)",B,"v8: 'to make them SIT (yashab) with princes' - God's exalting of the lowly to honour. Qualifier."),
 (270778,"gives (yashab)",B,"v9: 'He GIVES (yashab) the barren woman a home' - God's gift of a household to the barren. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (270737,"rising (mizrach)","v3: 'From the RISING (mizrach) of the sun to its setting' - the sunrise, image of the whole span of day/earth. Standalone."),
 (270740,"setting (mabo)","v3: 'to its SETTING (mabo)' - the sunset, image of the extent of God's praise. Standalone."),
 (270756,"high (gabah)","v5: 'who is seated on HIGH (gabah)' - the height of God's throne (qual seated, 270755), image. Standalone."),
 (270765,"dust (aphar)","v7: 'He raises the poor from the DUST (aphar)' - the dust of poverty (char poor, 270763), image. Standalone."),
 (270769,"ash heap (ashpoth)","v7: 'lifts the needy from the ASH HEAP (ashpoth)' - the refuse-heap of destitution (char needy, 270767), image. Standalone."),
 (270773,"princes (nadib)","v8: 'to make them sit with PRINCES (nadib)' - the nobles among whom God seats the lifted poor, image of honour. Standalone."),
 (270775,"princes (nadib)","v8: 'with the PRINCES (nadib) of his people' - the nobles of Israel, image. Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
