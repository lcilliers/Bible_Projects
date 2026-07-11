import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,130,
  note="Ps130 'Out of the depths' (8v). Operations: the CRY from the abyss; the PLEAS for mercy; the guilt (INIQUITIES) that could not stand if marked; FORGIVENESS that evokes reverence (FEARED - mercy producing awe, not license); the self's active WAITING (WAIT/SOUL/WAITS, the SOUL like watchmen aching for dawn); HOPE in the word, HOPE in the LORD; the INIQUITIES God redeems. God's hear/mark/forgiveness/steadfast-love/redeem = qualifiers; depths/voice/watchmen imagery = standalone.")
CH=[
 (272799,"cry (qara)","action","the psalmist","cry out","from the depths",GOD,"paired with the pleas for mercy",
  "v1: 'Out of the DEPTHS I CRY (qara) to you, O LORD!' - the operation of the cry rising from the abyss: the self at its lowest, voice thrown upward out of the deep."),
 (272809,"pleas for mercy (tachanun)","action","the psalmist","plead for mercy","before God",GOD,"paired with the cry",
  "v2: 'be attentive to the voice of my PLEAS FOR MERCY (tachanun)!' - the supplication, the cry sharpened into a plea for grace."),
 (272813,"iniquities (avon)","state","the psalmist","bear iniquities","that could not stand",IB,"paired with the impossibility of standing",
  "v3: 'If you, O LORD, should mark INIQUITIES (avon), O Lord, who could stand?' - the operation of guilt weighed: the self recognizing that under exact reckoning no one could stand."),
 (272821,"fear (yare)","disposition","the forgiven","revere God","because there is forgiveness",GOD,"paired with the forgiveness that produces it",
  "v4: 'But with you there is forgiveness, that you may be FEARED (yare)' - the operation of mercy: forgiveness does not breed license but reverence, awe deepened by being pardoned."),
 (272822,"wait (qavah)","action","the psalmist","wait","for the LORD",GOD,"paired with the soul's waiting and hope",
  "v5: 'I WAIT (qavah) for the LORD' - the operation of expectant waiting: the whole self stretched forward toward God."),
 (272824,"soul (nephesh)","faculty","the psalmist","wait","for the LORD",IB,"paired with the waiting and hope",
  "v5: 'my SOUL (nephesh) waits' - the inmost self engaged in the waiting, expectation seated in the soul."),
 (272825,"wait (qavah)","action","the psalmist","wait","for the LORD, hoping in his word",GOD,"paired with the soul and hope",
  "v5: 'my soul WAITS (qavah), and in his word I hope' - the waiting doubled and grounded, expectation anchored in God's word."),
 (272828,"hope (yachal)","disposition","the psalmist","hope","in God's word",GOD,"paired with the waiting",
  "v5: 'and in his word I HOPE (yachal)' - the operation of hope: the waiting given a foothold in the word, expectation resting on a promise."),
 (272829,"soul (nephesh)","faculty","the psalmist","long for the Lord","more than watchmen for dawn",IB,"paired with the watchmen's ache",
  "v6: 'my SOUL (nephesh) waits for the Lord more than watchmen for the morning' - the operation of longing imaged: the soul's ache for God like the night-watchman's straining for the first light."),
 (272837,"hope (yachal)","disposition","Israel","hope","in the LORD",GOD,"paired with God's steadfast love and redemption",
  "v7: 'O Israel, HOPE (yachal) in the LORD!' - the hope widened from the self to the whole people, grounded in God's plentiful redemption."),
 (272852,"iniquities (avon)","state","Israel","have iniquities","redeemed by God",IB,"paired with God's redemption",
  "v8: 'And he will redeem Israel from all his INIQUITIES (avon)' - the guilt of the people, the very iniquities of v3 now met not by reckoning but by redemption."),
]
for a in CH: r.ch(*a)
QU=[
 (272802,"hear (shama)",272799,"v2: 'O Lord, HEAR (shama) my voice!' - God's hearing petitioned. Qualifier."),
 (272805,"attentive (qashab)",272809,"v2: 'Let your ears be ATTENTIVE (qashab)' - God's attentive ear petitioned. Qualifier."),
 (272812,"mark (shamar)",272813,"v3: 'If you, O LORD, should MARK (shamar) iniquities' - God's exact reckoning of sin (hypothetical). Qualifier."),
 (272819,"forgiveness (selichah)",272821,"v4: 'But with you there is FORGIVENESS (selichah)' - God's pardon. Qualifier."),
 (272827,"word (dabar)",272828,"v5: 'in his WORD (dabar) I hope' - God's word, ground of the hope. Qualifier."),
 (272842,"steadfast love (chesed)",272837,"v7: 'For with the LORD there is STEADFAST LOVE (chesed)' - God's covenant love. Qualifier."),
 (272844,"plentiful (rabah)",272837,"v7: 'and with him is PLENTIFUL (rabah) redemption' - the abundance of God's redemption. Qualifier."),
 (272845,"redemption (peduth)",272837,"v7: 'plentiful REDEMPTION (peduth)' - God's redemption. Qualifier."),
 (272847,"redeem (padah)",272852,"v8: 'he will REDEEM (padah) Israel from all his iniquities' - God's redeeming. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (272796,"Ascents (maalah)","v0: heading. Standalone."),
 (272798,"depths (maamaq)","v1: 'Out of the DEPTHS (maamaq)' - the abyss from which the cry rises (char cry, 272799), image. Standalone."),
 (272803,"voice (qol)","v2: 'hear my VOICE (qol)!' - the psalmist's voice, object of God's hearing. Standalone."),
 (272807,"voice (qol)","v2: 'the VOICE (qol) of my pleas for mercy' - the pleading voice (char pleas, 272809), image. Standalone."),
 (272816,"stand (amad)","v3: 'who could STAND (amad)?' - the rhetorical impossibility of standing under marked sin, image. Standalone."),
 (272832,"watchmen (shamar)","v6: 'more than WATCHMEN (shamar) for the morning' - the night-guards, image of the soul's longing (char soul, 272829). Standalone."),
 (272834,"watchmen (shamar)","v6: 'more than WATCHMEN (shamar) for the morning' - the watchmen repeated, intensifying the ache for dawn, image. Standalone."),
]: r.st(sid,sense,d)
r.write()
