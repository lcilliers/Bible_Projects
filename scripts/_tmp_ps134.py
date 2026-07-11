import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,134,
  note="Ps134 closing Song of Ascents (3v). Operation = the night-watch worship: the servants who BLESS the LORD, LIFT-UP their hands to the holy place, and BLESS him again. God's bless-from-Zion/made = qualifiers; standing-by-night/holy-place imagery = standalone.")
CH=[
 (273030,"bless (barak)","action","the servants","bless","the LORD by night",GOD,"paired with lifting the hands",
  "v1: 'Come, BLESS (barak) the LORD, all you servants of the LORD, who stand by night in the house of the LORD!' - the operation of night-worship: the temple-servants summoned to bless God through the dark hours."),
 (273040,"lift up the hands (nasa)","action","the servants","lift up the hands","to the holy place",GOD,"paired with blessing the LORD",
  "v2: 'LIFT UP (nasa) your hands to the holy place and bless the LORD!' - the gesture of worship: hands raised toward the sanctuary, the body enacting the blessing."),
 (273043,"bless (barak)","action","the servants","bless","the LORD",GOD,"paired with the lifted hands",
  "v2: 'and BLESS (barak) the LORD!' - the repeated call to bless, worship pressed home."),
]
for a in CH: r.ch(*a)
QU=[
 (307872,"bless (barak)",273030,"v3: 'May the LORD BLESS (barak) you from Zion' - God's answering blessing on the worshippers. Qualifier."),
 (307875,"made (asah)",273030,"v3: 'the LORD... who MADE (asah) heaven and earth!' - God the creator. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (273028,"Ascents (maalah)","v0: heading. Standalone."),
 (273035,"stand (amad)","v1: 'who STAND (amad) by night in the house of the LORD!' - the servants' night-station in the temple (char bless, 273030), image. Standalone."),
 (273042,"holy place (qodesh)","v2: 'Lift up your hands to the HOLY PLACE (qodesh)' - the sanctuary toward which the hands are raised, image. Standalone."),
]: r.st(sid,sense,d)
r.write()
