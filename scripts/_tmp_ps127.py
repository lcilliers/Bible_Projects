import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,127,
  note="Ps127 'Unless the LORD builds the house' (5v). Central operation = the FUTILITY of self-reliant striving without God. Three distinct VAINs (read each off its verse, not merged): the builders' vain toil (v1a), the watchman's vain vigil (v1b), the toiler's vain early-rising/late-resting (v2) - crowned by the ANXIOUS bread of self-effort vs the sleep God gives his beloved. Then the BLESSED man whose quiver is full, unashamed at the gate (not PUT-TO-SHAME). God's builds/watches/gives = qualifiers; children/arrows/quiver imagery = standalone.")
CH=[
 (272606,"vain (shav)","state","the builders","labour in vain","without God's building",IB,"paired with the watchman's vain vigil",
  "v1: 'Unless the LORD builds the house, those who build it labour in VAIN (shav)' - the operation of futility: human building without God is effort spent on nothing, the work undone before it stands."),
 (272613,"vain (shav)","state","the watchman","keep watch in vain","without God's keeping",IB,"paired with the builders' vain toil",
  "v1: 'Unless the LORD watches over the city, the watchman stays awake in VAIN (shav)' - the futility of the vigil: the guard's wakefulness is useless if God does not keep the city."),
 (272614,"vain (shav)","state","the toiler","toil anxiously in vain","from dawn to dark",IB,"paired with the anxious bread and God's gift of sleep",
  "v2: 'It is in VAIN (shav) that you rise up early and go late to rest' - the futility of frantic self-effort: the anxious lengthening of the workday earns nothing that God does not give."),
 (272621,"anxious (etseb)","state","the toiler","eat the bread of anxious toil","in self-reliance",IB,"paired with the sleep God gives the beloved",
  "v2: 'eating the bread of ANXIOUS toil (etseb)' - the operation of care: self-reliance turns even bread into anxiety, over against the sleep God gives his beloved without their striving."),
 (272633,"blessed (esher)","state","the man with children","be blessed","with a full quiver",IB,"paired with not being put to shame",
  "v5: 'BLESSED (esher) is the man who fills his quiver with them!' - the happiness of the man whose children (God's gift, v3) are his strength."),
 (272640,"put to shame (bosh, negated)","state","the man with children","not be put to shame","before enemies at the gate",IB,"paired with the blessed man",
  "v5: 'he shall not be PUT TO SHAME (bosh) when he speaks with his enemies in the gate' - the operation of vindicated standing: the man backed by sons is unashamed in the contest at the city gate."),
]
for a in CH: r.ch(*a)
QU=[
 (272602,"builds (banah)",272606,"v1: 'Unless the LORD BUILDS (banah) the house' - God's building, without which all toil is vain. Qualifier."),
 (272604,"build (banah)",272606,"v1: 'those who BUILD (banah) it labour in vain' - the building God must give effect to. Qualifier."),
 (272609,"watches over (shamar)",272613,"v1: 'Unless the LORD WATCHES OVER (shamar) the city' - God's keeping, without which the watch is vain. Qualifier."),
 (272623,"gives (nathan)",272633,"v2: 'for he GIVES (nathan) to his beloved sleep' - God's gift of rest, the counter to anxious toil. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (272598,"Ascents (maalah)","v0: heading, of Solomon. Standalone."),
 (272605,"labour (amal)","v1: 'those who build it LABOUR (amal) in vain' - the toil (char vain, 272606), image. Standalone."),
 (272610,"city (ir)","v1: 'the LORD watches over the CITY (ir)' - the city guarded, image. Standalone."),
 (272611,"watchman (shamar)","v1: 'the WATCHMAN (shamar) stays awake in vain' - the guard (char vain, 272613), image. Standalone."),
 (272612,"stays awake (shaqad)","v1: 'the watchman STAYS AWAKE (shaqad) in vain' - the vigil, image. Standalone."),
 (272615,"rise up (qum)","v2: 'you RISE UP (qum) early' - the early rising of anxious toil, image. Standalone."),
 (272616,"early (shakam)","v2: 'rise up EARLY (shakam)' - the pre-dawn start, image. Standalone."),
 (272617,"go to rest (yashab)","v2: 'and GO (yashab) late to rest' - the delayed rest, image. Standalone."),
 (272618,"late (achar)","v2: 'go LATE (achar) to rest' - the lengthened day, image. Standalone."),
 (272619,"eating (akal)","v2: 'EATING (akal) the bread of anxious toil' - the anxious meal (char anxious, 272621), image. Standalone."),
 (272620,"bread (lechem)","v2: 'the BREAD (lechem) of anxious toil' - the food of care, image. Standalone."),
 (272624,"beloved (yadid)","v2: 'he gives to his BELOVED (yadid) sleep' - God's loved ones, the object of the gift. Standalone."),
 (272625,"sleep (shena)","v2: 'he gives to his beloved SLEEP (shena)' - the rest God gives, image of grace over striving. Standalone."),
 (272628,"heritage (nachalah)","v3: 'children are a HERITAGE (nachalah) from the LORD' - children as God's gift, image. Standalone."),
 (272630,"fruit (peri)","v3: 'the FRUIT (peri) of the womb a reward' - the offspring, image. Standalone."),
 (272631,"womb (beten)","v3: 'the fruit of the WOMB (beten)' - the source of children, image. Standalone."),
 (272632,"reward (sakar)","v3: 'the fruit of the womb a REWARD (sakar)' - children as reward, image. Standalone."),
 (307837,"arrows (chets)","v4: 'Like ARROWS (chets) in the hand of a warrior' - the sons as arrows, image of strength. Standalone."),
 (307839,"warrior (gibbor)","v4: 'in the hand of a WARRIOR (gibbor)' - the soldier, image. Standalone."),
 (307841,"youth (naar)","v4: 'the children of one's YOUTH (naar)' - the sons of one's prime, image. Standalone."),
 (272636,"fills (male)","v5: 'the man who FILLS (male) his quiver with them' - the full quiver (char blessed, 272633), image. Standalone."),
 (272637,"quiver (ashpah)","v5: 'fills his QUIVER (ashpah) with them' - the arrow-case of sons, image. Standalone."),
 (272645,"gate (shaar)","v5: 'when he speaks with his enemies in the GATE (shaar)' - the place of the contest, image. Standalone."),
]: r.st(sid,sense,d)
r.write()
