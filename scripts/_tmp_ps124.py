import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,124,
  note="Ps124 'If not for the LORD' (8v). Operations: the foes' ANGER igniting to devour; the self (US x2) on the brink of dissolution under flood/torrent; the act of BLESSING God for rescue; the self's escape (WE) - sudden liberation, the bird slipping the sprung snare. God's help/name = qualifiers; rising/flood/snare imagery = standalone.")
CH=[
 (272488,"anger (aph)","state","the enemies","have anger ignite","to devour the people",IB,"paired with the swallowing alive",
  "v3: 'when their ANGER (aph) was kindled against us' - the operation of hostile fury igniting, wrath flaring to the point of swallowing its victim alive."),
 (272497,"self (nephesh)","faculty","the people","be nearly swept away","by the flood",IB,"paired with the torrent going over",
  "v4: 'the flood would have swept US (nephesh) away' - the self on the brink of dissolution, the person nearly obliterated by the engulfing waters."),
 (272500,"self (nephesh)","faculty","the people","be nearly overwhelmed","by the torrent",IB,"paired with the flood sweeping away",
  "v5: 'then over US (nephesh) would have gone the raging waters' - the self almost drowned, existence hanging on the edge of the torrent."),
 (272504,"bless (barak)","action","the people","bless God","for not being given as prey",GOD,"paired with escaping the teeth",
  "v6: 'BLESSED (barak) be the LORD, who has not given us as prey to their teeth!' - the operation of gratitude: blessing God at the recognition of a devouring just escaped."),
 (272512,"escape (nephesh)","state","the people","escape to freedom","like a bird from the snare",IB,"paired with the broken snare",
  "v7: 'WE (nephesh) have escaped like a bird from the snare of the fowlers' - the operation of sudden liberation: the self, trapped, breaks free in an instant of flight as the snare gives way."),
]
for a in CH: r.ch(*a)
r.qu(307807,"help (ezer)",272504,"v8: 'Our HELP (ezer) is in the name of the LORD' - God the source of rescue. Qualifier.")
r.qu(307808,"name (shem)",272504,"v8: 'in the NAME (shem) of the LORD, who made heaven and earth' - God's name. Qualifier.")
for sid,sense,d in [
 (272477,"Ascents (maalah)","v0: heading. Standalone."),
 (307805,"rose up (qum)","v2: 'when people ROSE UP (qum) against us' - the foes' assault, image. Standalone."),
 (272485,"swallow up (bala)","v3: 'they would have SWALLOWED us up (bala) alive' - the near-devouring, image. Standalone."),
 (272486,"alive (chay)","v3: 'swallowed us up ALIVE (chay)' - the living victim nearly consumed, image. Standalone."),
 (272489,"kindled (charah)","v3: 'when their anger was KINDLED (charah)' - the ignition of the foes' wrath (char anger, 272488), image. Standalone."),
 (272492,"flood (mayim)","v4: 'the FLOOD (mayim) would have swept us away' - the engulfing waters, image. Standalone."),
 (272493,"sweep away (shataph)","v4: 'the flood would have SWEPT us AWAY (shataph)' - the overwhelming current, image. Standalone."),
 (272494,"torrent (nachal)","v4: 'the TORRENT (nachal) would have gone over us' - the flash-flood, image. Standalone."),
 (272495,"gone over (abar)","v4: 'the torrent would have GONE OVER (abar) us' - the waters overtopping, image. Standalone."),
 (272501,"gone over (abar)","v5: 'then over us would have GONE (abar) the raging waters' - the near-drowning, image. Standalone."),
 (272502,"raging (zeidon)","v5: 'the RAGING (zeidon) waters' - the proud, swelling flood, image. Standalone."),
 (272503,"waters (mayim)","v5: 'the raging WATERS (mayim)' - the torrent, image. Standalone."),
 (272509,"prey (tereph)","v6: 'not given us as PREY (tereph) to their teeth' - the food the foes would have made of them, image. Standalone."),
 (272511,"teeth (shen)","v6: 'to their TEETH (shen)' - the devouring teeth, image. Standalone."),
 (272513,"escaped (malat)","v7: 'We have ESCAPED (malat) like a bird' - the escape (char We, 272512), image. Standalone."),
 (272514,"bird (tsippor)","v7: 'like a BIRD (tsippor)' - the freed bird, image of the escape. Standalone."),
 (272516,"snare (pach)","v7: 'from the SNARE (pach) of the fowlers' - the trap, image. Standalone."),
 (272517,"fowlers (yaqosh)","v7: 'of the FOWLERS (yaqosh)' - the bird-catchers, image of the foes. Standalone."),
 (272518,"snare (pach)","v7: 'the SNARE (pach) is broken' - the trap, image. Standalone."),
 (272519,"broken (shabar)","v7: 'the snare is BROKEN (shabar)' - the trap giving way, image of the liberation. Standalone."),
 (272521,"escaped (malat)","v7: 'and we have ESCAPED (malat)!' - the completed escape (char We, 272512), image. Standalone."),
]: r.st(sid,sense,d)
r.write()
