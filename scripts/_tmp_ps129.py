import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,129,
  note="Ps129 'Greatly have they afflicted me from my youth' (8v). Operation = RESILIENCE under long oppression - affliction from youth that could not prevail. Chars: the AFFLICTED (x2) from youth, yet the foes have not PREVAILED; the PLOWERS who PLOWED the back (oppression imaged as furrowing); the WICKED whose cords God cut; those who HATE Zion PUT-TO-SHAME. God's righteous/cut-cords/name = qualifiers; furrows/rooftop-grass/reaper imagery = standalone.")
CH=[
 (272688,"be afflicted (tsarar)","state","Israel","be afflicted","from youth",IB,"paired with the affliction not prevailing",
  "v1: 'Greatly have they AFFLICTED (tsarar) me from my youth' - the operation of long endurance: affliction pressing from the nation's very youth, borne across its whole history."),
 (272695,"be afflicted (tsarar)","state","Israel","be afflicted","from youth, yet not overcome",IB,"paired with the foes not prevailing",
  "v2: 'Greatly have they AFFLICTED (tsarar) me from my youth, yet they have not prevailed' - the affliction restated, now hinged to its limit: pressed hard but not broken."),
 (272700,"prevail (yakol, negated)","state","the enemies","fail to prevail","against Israel",IB,"paired with the long affliction",
  "v2: 'yet they have not PREVAILED (yakol) against me' - the operation of resilience: the oppressors' repeated blows unable to overcome, affliction outlasted."),
 (272702,"plowers (charash)","status","the oppressors","plow the back","in oppression",IB,"paired with the furrows they made",
  "v3: 'The PLOWERS (charash) plowed upon my back' - the oppressors imaged as ploughmen, driving their furrows across the victim's body."),
 (272703,"plow (charash)","action","the oppressors","plow","long furrows on the back",IB,"paired with the plowers",
  "v3: 'The plowers PLOWED (charash) upon my back; they made long their furrows' - the operation of oppression imaged as ploughing: deep, deliberate, drawn-out wounding of the back."),
 (272713,"wicked (rasha)","status","the wicked","bind with cords","which God cuts",IB,"paired with the cords God cut",
  "v4: 'he has cut the cords of the WICKED (rasha)' - the wicked whose binding ropes the righteous LORD severs, the oppression undone."),
 (272715,"hate (sane)","disposition","those who hate Zion","hate","Zion",IB,"paired with being put to shame",
  "v5: 'May all who HATE (sane) Zion be put to shame and turned backward!' - the enmity toward Zion, whose end is shame."),
 (272717,"put to shame (bosh)","state","the haters of Zion","be put to shame","and turned back",IB,"paired with the hatred of Zion",
  "v5: 'be PUT TO SHAME (bosh) and turned backward!' - the operation of the foes' collapse: the haters of Zion routed and shamed, like rooftop grass that withers."),
]
for a in CH: r.ch(*a)
QU=[
 (272710,"righteous (tsaddiq)",272713,"v4: 'The LORD is RIGHTEOUS (tsaddiq)' - God's righteousness. Qualifier."),
 (272711,"cut (qatsats)",272713,"v4: 'he has CUT (qatsats) the cords of the wicked' - God's severing of the oppressors' bonds. Qualifier."),
 (272732,"name (shem)",272715,"v8: 'We bless you in the NAME (shem) of the LORD!' - God's name. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (272686,"Ascents (maalah)","v0: heading. Standalone."),
 (272690,"youth (naar)","v1: 'from my YOUTH (naar)' - the nation's early days, when affliction began; temporal. Standalone."),
 (272697,"youth (naar)","v2: 'from my YOUTH (naar)' - the long span of affliction; temporal. Standalone."),
 (272705,"back (gab)","v3: 'plowed upon my BACK (gab)' - the body ploughed by oppressors, image. Standalone."),
 (272706,"made long (arak)","v3: 'they MADE LONG (arak) their furrows' - the drawn-out wounding, image. Standalone."),
 (272708,"furrows (maanith)","v3: 'their FURROWS (maanith)' - the plough-cuts of oppression, image. Standalone."),
 (272712,"cords (aboth)","v4: 'the CORDS (aboth) of the wicked' - the binding ropes God cut (char wicked, 272713), image. Standalone."),
 (272718,"turned (sug)","v5: 'and TURNED (sug) backward!' - the foes driven back (char put-to-shame, 272717), image. Standalone."),
 (272719,"backward (achor)","v5: 'turned BACKWARD (achor)!' - the rout of the haters, image. Standalone."),
 (307855,"grass (chatsir)","v6: 'Let them be like the GRASS (chatsir) on the housetops' - the rootless rooftop grass, image of the foes' quick withering. Standalone."),
 (307856,"housetops (gag)","v6: 'the grass on the HOUSETOPS (gag)' - the shallow-soiled roof, image. Standalone."),
 (307857,"withers (yabesh)","v6: 'which WITHERS (yabesh) before it grows up' - the grass dying unrooted, image of the foes' fate. Standalone."),
 (307858,"before (qadam)","v6: 'BEFORE (qadam) it grows up' - the premature withering, image. Standalone."),
 (307859,"grows up (shalaph)","v6: 'before it GROWS UP (shalaph)' - the grass that never matures, image. Standalone."),
 (272720,"reaper (qatsar)","v7: 'with which the REAPER (qatsar) does not fill his hand' - the useless rooftop grass, image. Standalone."),
 (272722,"fill (male)","v7: 'does not FILL (male) his hand' - the empty harvest of the foes, image. Standalone."),
 (272723,"hand (kaph)","v7: 'fill his HAND (kaph)' - the reaper's empty hand, image. Standalone."),
 (272724,"sheaves (omer)","v7: 'nor the binder of SHEAVES (omer) his arms' - the worthless grass, image. Standalone."),
 (272725,"arms (chetsen)","v7: 'his ARMS (chetsen)' - the binder's empty embrace, image. Standalone."),
 (272727,"pass by (abar)","v8: 'nor do those who PASS BY (abar) say' - the passers-by who withhold blessing, image. Standalone."),
 (272729,"blessing (berakah)","v8: 'The BLESSING (berakah) of the LORD be upon you!' - the harvest-blessing withheld from the foes, image. Standalone."),
 (272731,"bless (barak)","v8: 'We BLESS (barak) you in the name of the LORD!' - the blessing the passers-by do not give the grass-like foes, image. Standalone."),
]: r.st(sid,sense,d)
r.write()
