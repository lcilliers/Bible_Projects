import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,125,
  note="Ps125 'Those who trust' (5v). Operations: TRUST grounding the self so it cannot be moved (immovable stability); the WICKEDNESS of oppressive rule; the RIGHTEOUS on whose land it will not rest, lest they STRETCH-OUT their hands to wrong (prolonged oppression tempting even the upright to reach toward sin); the GOOD/UPRIGHT in HEART; those who TURN-ASIDE to crooked ways, led away with EVILDOERS. God's not-moved/surround/lead-away = qualifiers; Zion/scepter/crooked-ways imagery = standalone.")
CH=[
 (272524,"trust (batach)","disposition","those who trust","ground the self in God","so as to be immovable",IB,"paired with the abiding-forever stability",
  "v1: 'Those who TRUST (batach) in the LORD are like Mount Zion, which cannot be moved' - the operation of trust grounding the self: reliance on God produces the immovability of a mountain."),
 (272534,"wickedness (resha)","status","the wicked","rule oppressively","over the righteous' land",IB,"paired with the righteous it threatens",
  "v3: 'For the scepter of WICKEDNESS (resha) shall not rest on the land allotted to the righteous' - the dominion of the wicked, whose prolonged rule God limits."),
 (272539,"righteous (tsaddiq)","status","the righteous","hold their allotted land","under God's guard",IB,"paired with the wickedness kept off",
  "v3: 'the land allotted to the RIGHTEOUS (tsaddiq)' - the just whose portion God shields from lasting oppression."),
 (272541,"righteous (tsaddiq)","status","the righteous","be tempted under pressure","toward wrong",IB,"paired with stretching out to wrong",
  "v3: 'lest the RIGHTEOUS (tsaddiq) stretch out their hands to do wrong' - the just who, under unrelieved oppression, might themselves be tempted to reach toward sin."),
 (272542,"stretch out the hands (shalach)","action","the righteous","reach toward wrong","under prolonged oppression",IB,"paired with the righteous so tempted",
  "v3: 'lest the righteous STRETCH OUT (shalach) their hands to do wrong' - the operation of endurance failing: oppression drawn out until even the upright reach for wrongdoing."),
 (272548,"good (tob)","status","the good","be good","toward God and men",IB,"paired with the upright in heart",
  "v4: 'Do good, O LORD, to those who are GOOD (tob)' - the good, on whom God's good is asked to rest."),
 (272549,"upright (yashar)","disposition","the upright","be upright","in heart",IB,"paired with the heart",
  "v4: 'and to those who are UPRIGHT (yashar) in their hearts!' - the straight-hearted, marked by inner rectitude."),
 (272551,"hearts (leb)","faculty","the upright","be upright","in the heart",IB,"paired with uprightness",
  "v4: 'upright in their HEARTS (leb)' - the inner seat of the uprightness, integrity lodged in the heart."),
 (272552,"turn aside (natah)","action","the crooked","turn aside","to crooked ways",IB,"paired with the evildoers led away",
  "v5: 'But those who TURN ASIDE (natah) to their crooked ways' - the operation of apostasy: veering off the straight path onto crooked byways."),
 (272557,"evildoers (paal aven)","status","the evildoers","be led away","with the crooked",IB,"paired with those who turn aside",
  "v5: 'the LORD will lead away with the EVILDOERS (paal aven)!' - the workers of iniquity, with whom the turncoats share the same removal."),
]
for a in CH: r.ch(*a)
QU=[
 (272529,"be moved (mot)",272524,"v1: 'which cannot be MOVED (mot)' - the God-given immovability. Qualifier."),
 (272530,"abides (yashab)",272524,"v1: 'but ABIDES (yashab) forever' - God's people enduring like Zion. Qualifier."),
 (307814,"surround (sabib)",272524,"v2: 'As the mountains SURROUND (sabib) Jerusalem' - the encircling image of God's protection. Qualifier."),
 (307817,"surrounds (sabib)",272524,"v2: 'so the LORD SURROUNDS (sabib) his people' - God's encompassing guard. Qualifier."),
 (272546,"do good (yatab)",272548,"v4: 'DO GOOD (yatab), O LORD, to those who are good' - God's doing good petitioned. Qualifier."),
 (272555,"lead away (halak)",272557,"v5: 'the LORD will LEAD AWAY (halak) with the evildoers' - God's removal of the crooked. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (272523,"Ascents (maalah)","v0: heading. Standalone."),
 (272531,"forever (olam)","v1: 'abides FOREVER (olam)' - the perpetuity of the stable; temporal. Standalone."),
 (272533,"scepter (shebet)","v3: 'the SCEPTER (shebet) of wickedness' - the rod of oppressive rule (char wickedness, 272534), image. Standalone."),
 (272536,"rest (nuach)","v3: 'shall not REST (nuach) on the land' - the wicked rule not permitted to settle, image. Standalone."),
 (272538,"land allotted (goral)","v3: 'the LAND ALLOTTED (goral) to the righteous' - the righteous' portion, image. Standalone."),
 (272545,"wrong (avlatah)","v3: 'to do WRONG (avlatah)' - the wrongdoing the tempted righteous might reach toward (char stretch-out, 272542), object. Standalone."),
 (272553,"crooked ways (aqalqal)","v5: 'to their CROOKED WAYS (aqalqal)' - the twisting byways of the apostate (char turn-aside, 272552), image. Standalone."),
 (272558,"peace (shalom)","v5: 'PEACE (shalom) be upon Israel!' - the closing benediction, image. Standalone."),
]: r.st(sid,sense,d)
r.write()
