import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,131,
  note="Ps131 the weaned-soul psalm (3v). PURE inner-being - 0 qualifiers (no God-acts). Operations: the deliberate LOWERING of ambition (HEART not LIFTED-UP, eyes not RAISED, not OCCUPYing with things too great = humility as self-restraint); the active STILLING of the self (CALMED + QUIETED the SOUL, the SOUL weaned from craving like a weaned child = self-quieting/contentment); HOPE in the LORD. Weaned-child imagery = standalone.")
CH=[
 (272857,"heart (leb)","faculty","the psalmist","keep the heart unproud","before God",IB,"paired with the eyes not raised",
  "v1: 'O LORD, my HEART (leb) is not lifted up' - the operation of humility at its seat: the inner self held low, refusing to swell with pride."),
 (272859,"lifted up (gabah, negated)","disposition","the psalmist","not exalt the heart","in pride",IB,"paired with the unproud heart",
  "v1: 'my heart is not LIFTED UP (gabah)' - the pride deliberately negated, the heart kept from rising."),
 (272862,"raise the eyes (rum, negated)","action","the psalmist","not raise the eyes too high","in ambition",IB,"paired with not occupying with great things",
  "v1: 'my eyes are not RAISED (rum) too high' - the operation of restraint: the gaze kept from reaching above its station."),
 (272865,"occupy (halak, negated)","action","the psalmist","not busy oneself","with things too great",IB,"paired with the marvelous things beyond him",
  "v1: 'I do not OCCUPY (halak) myself with things too great and too marvellous for me' - the self declining to grasp at matters beyond its measure, ambition renounced."),
 (272870,"calm (shavah)","action","the psalmist","calm the soul","from craving",IB,"paired with quieting the soul",
  "v2: 'But I have CALMED (shavah) and quieted my soul' - the operation of self-stilling: the active work of settling the restless self."),
 (272871,"quiet (damam)","action","the psalmist","quiet the soul","into stillness",IB,"paired with calming the soul",
  "v2: 'I have calmed and QUIETED (damam) my soul' - the hushing of the inner clamour, the self brought to silence."),
 (272872,"soul (nephesh)","faculty","the psalmist","be stilled","like a weaned child",IB,"paired with the weaned-child image",
  "v2: 'my SOUL (nephesh)' - the inmost self that is calmed and quieted, the object of the stilling."),
 (272879,"soul (nephesh)","faculty","the psalmist","rest content","weaned from craving",IB,"paired with the weaned child",
  "v2: 'like a weaned child is my SOUL (nephesh) within me' - the operation of contentment: the self weaned from its craving, no longer fretting for what it once demanded, at rest."),
 (272882,"hope (yachal)","disposition","Israel","hope","in the LORD",GOD,"paired with the stilled soul",
  "v3: 'O Israel, HOPE (yachal) in the LORD from this time forth and forevermore' - the stilled trust widened to the whole people, hope as the settled posture."),
]
for a in CH: r.ch(*a)
for sid,sense,d in [
 (272854,"Ascents (maalah)","v0: heading, of David. Standalone."),
 (272867,"marvelous (pala)","v1: 'things too great and too MARVELLOUS (pala) for me' - the matters beyond the self's measure (char occupy, 272865), image. Standalone."),
 (272874,"weaned (gamal)","v2: 'like a WEANED (gamal) child with its mother' - the weaning, image of the stilled soul. Standalone."),
 (272877,"weaned child (gamal)","v2: 'like a WEANED CHILD (gamal)' - the child no longer craving the breast, image of contentment (char soul, 272879). Standalone."),
]: r.st(sid,sense,d)
r.write()
