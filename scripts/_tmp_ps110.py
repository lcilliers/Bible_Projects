import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,110,
  note="Ps110 messianic oracle (7v). Almost entirely God's declaration TO the king-priest (Sit at my right hand; rule; a priest forever after Melchizedek; the LORD shatters kings). Two human-IB moments: the people who offer themselves FREELY on the day of his power (v3, willing devotion); the king who LIFTS-UP his head in triumph (v7). All else = God's oracle-acts (qualifiers, source-linked to the king's exaltation) + royal/priestly imagery (standalone).")
CH=[
 (270518,"offer freely (nedabah)","disposition","the people","offer themselves freely","to the king on the day of his power",GOD,"paired with the king's God-given exaltation",
  "v3: 'Your people will offer themselves FREELY (nedabah) on the day of your power' - the willing self-devotion of the people, allegiance given gladly to the king God exalts."),
 (270560,"lift up (rum)","state","the king","lift up his head","in triumph",GOD,"paired with drinking from the brook by the way",
  "v7: 'therefore he will LIFT UP (rum) his head' - the king's triumphant exaltation, head raised in victory after God has shattered his foes."),
]
for a in CH: r.ch(*a)
K=270560
QU=[
 (270501,"sit (yashab)",K,"v1: 'The LORD says to my Lord: SIT (yashab) at my right hand' - God's enthronement of the king. Qualifier."),
 (270504,"make (shith)",K,"v1: 'until I MAKE (shith) your enemies your footstool' - God's subjugation of the king's foes. Qualifier."),
 (270508,"send forth (shalach)",K,"v2: 'The LORD SENDS FORTH (shalach) from Zion your mighty scepter' - God's extending of the king's rule. Qualifier."),
 (270513,"rule (radah)",K,"v2: 'RULE (radah) in the midst of your enemies!' - God's mandate to the king to reign. Qualifier."),
 (270531,"sworn (shaba)",K,"v4: 'The LORD has SWORN (shaba) and will not change his mind' - God's oath establishing the king-priest. Qualifier."),
 (270533,"change mind (nacham)",K,"v4: 'and will not CHANGE HIS MIND (nacham)' - God's unchanging oath. Qualifier."),
 (270543,"shatter (machats)",K,"v5: 'he will SHATTER (machats) kings on the day of his wrath' - God's shattering of kings for the king. Qualifier."),
 (270546,"wrath (aph)",K,"v5: 'on the day of his WRATH (aph)' - God's wrath. Qualifier."),
 (270547,"execute judgment (din)",K,"v6: 'He will EXECUTE JUDGMENT (din) among the nations' - God's judgment through the king. Qualifier."),
 (270549,"filling (male)",K,"v6: 'FILLING (male) them with corpses' - God's judgment on the nations. Qualifier."),
 (270551,"shatter (machats)",K,"v6: 'he will SHATTER (machats) chiefs over the wide earth' - God's crushing of the rulers. Qualifier."),
 (270555,"drink (shathah)",K,"v7: 'He will DRINK (shathah) from the brook by the way' - the king refreshed in pursuit (God-given victory). Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (270506,"footstool (hadom)","v1: 'until I make your enemies your FOOTSTOOL (hadom)' - the subdued foes, image of dominion. Standalone."),
 (270511,"mighty (oz)","v2: 'your MIGHTY (oz) scepter' - the king's powerful rod, image of rule. Standalone."),
 (270512,"scepter (matteh)","v2: 'your mighty SCEPTER (matteh)' - the king's rod of rule, image. Standalone."),
 (270521,"power (chayil)","v3: 'on the day of your POWER (chayil)' - the day of the king's might, image. Standalone."),
 (270522,"holy (qodesh)","v3: 'in HOLY (qodesh) garments' - the holy attire of the king's people, image. Standalone."),
 (270523,"garments (hadar)","v3: 'in holy GARMENTS (hadar)' - the sacred vestments/array, image. Standalone."),
 (270525,"womb (rechem)","v3: 'from the WOMB (rechem) of the morning' - the dawn's womb, image of the king's fresh host. Standalone."),
 (270526,"morning (mishchar)","v3: 'from the womb of the MORNING (mishchar)' - the dawn, image. Standalone."),
 (270527,"dew (tal)","v3: 'the DEW (tal) of your youth will be yours' - the dew-fresh youth/army, image. Standalone."),
 (270529,"youth (yalduth)","v3: 'the dew of your YOUTH (yalduth)' - the king's youthful vigour/host, image. Standalone."),
 (270535,"priest (kohen)","v4: 'You are a PRIEST (kohen) forever' - the king's priestly office, image. Standalone."),
 (270536,"forever (olam)","v4: 'a priest FOREVER (olam)' - the perpetuity of the priesthood; temporal. Standalone."),
 (270538,"order (dibrah)","v4: 'after the ORDER (dibrah) of Melchizedek' - the Melchizedek priestly order, image. Standalone."),
 (270539,"Melchizedek (malki-tsedeq)","v4: 'after the order of MELCHIZEDEK (malki-tsedeq)' - the priest-king of old, image. Standalone."),
 (270550,"corpses (geviyah)","v6: 'filling them with CORPSES (geviyah)' - the slain of the nations, image of judgment. Standalone."),
 (270552,"chiefs (rosh)","v6: 'he will shatter CHIEFS (rosh) over the wide earth' - the rulers shattered, image. Standalone."),
 (270557,"brook (nachal)","v7: 'He will drink from the BROOK (nachal) by the way' - the wayside stream, image of the pursuing king refreshed. Standalone."),
 (270561,"head (rosh)","v7: 'therefore he will lift up his HEAD (rosh)' - the head lifted in triumph (char lift-up, 270560), image. Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
