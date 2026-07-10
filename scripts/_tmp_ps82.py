import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,82,
  note="Ps82 God arraigns the corrupt divine-council judges (Asaph, 8v; one movement). Human/authority IB: the unjust JUDGING, the INJUSTICE and PARTIALITY that favours the WICKED; the moral blindness - they have neither KNOWLEDGE nor UNDERSTANDING; and the afflicted whose plight indicts them (the WEAK, FATHERLESS, AFFLICTED, DESTITUTE, NEEDY). God's taking-his-place / holding-judgment / arise-and-judge-and-inherit = qualifiers; the enjoined duties (give-justice/rescue/deliver) + darkness/foundations/mortality imagery = standalone.")
for a in [
 (283894,"judge unjustly (shaphat)","action","the corrupt judges ('gods')","judge / give verdicts","unjustly","paired with the injustice and partiality",IB,
  "v2: 'How long will you JUDGE (shaphat) unjustly?' - the corrupt exercise of judgment, authority turned against its own purpose."),
 (283895,"injustice (avel)","disposition","the judges","act unjustly","in verdicts","paired with showing partiality",IB,
  "v2: 'How long will you judge UNJUSTLY (avel)?' - the injustice itself, the crookedness of heart behind the corrupt bench."),
 (283896,"show partiality (nasa panim)","disposition","the judges","show favour","to the wicked","paired with the unjust judging",IB,
  "v2: 'and SHOW PARTIALITY (nasa) to the wicked?' - the favouritism that lifts the guilty face, justice sold to the strong."),
 (283897,"wicked (rasha)","status","the wicked","be favoured","by the corrupt judges","paired with the partiality shown them",IB,
  "v2: 'show partiality to the WICKED (rasha)?' - the guilty whom the corrupt court protects, IB of the favoured evildoer."),
 (283900,"weak (dal)","status","the weak","be denied justice","by the judges","paired with the fatherless",IB,
  "v3: 'Give justice to the WEAK (dal) and the fatherless' - the powerless whose cause the judges neglect; their helpless state indicts the bench."),
 (283901,"fatherless (yathom)","status","the fatherless","lack a defender","before the court","paired with the weak",IB,
  "v3: 'the WEAK and the FATHERLESS (yathom)' - the orphan without protector, the classic object of justice denied."),
 (283903,"afflicted (ani)","status","the afflicted","suffer oppression","under injustice","paired with the destitute",IB,
  "v3: 'maintain the right of the AFFLICTED (ani) and the destitute' - the humbled poor, their affliction the measure of the judges' failure."),
 (283904,"destitute (rush)","status","the destitute","be left in want","by the court","paired with the afflicted",IB,
  "v3: 'the afflicted and the DESTITUTE (rush)' - the utterly poor, whose want cries against corrupt power."),
 (283906,"weak (dal)","status","the weak","need rescue","from the wicked","paired with the needy",IB,
  "v4: 'Rescue the WEAK (dal) and the needy' - the powerless, again named as those the judges should but do not defend."),
 (283907,"needy (ebyon)","status","the needy","need deliverance","from the wicked's hand","paired with the weak",IB,
  "v4: 'the weak and the NEEDY (ebyon)' - the destitute whose deliverance is the judges' abandoned duty."),
 (283911,"wicked (rasha)","status","the wicked","oppress the needy","by their power","paired with the weak they crush",IB,
  "v4: 'deliver them from the hand of the WICKED (rasha)' - the oppressors from whose grip the poor must be freed, IB of the predatory strong."),
 (283913,"knowledge (yada, lacking)","faculty","the judges","lack knowledge","of justice","paired with lacking understanding",IB,
  "v5: 'They have neither KNOWLEDGE (yada) nor understanding' - the moral ignorance of the corrupt, blindness that destabilizes the world."),
 (283915,"understanding (bin, lacking)","faculty","the judges","lack understanding","of right","paired with lacking knowledge",IB,
  "v5: 'neither knowledge nor UNDERSTANDING (bin)' - the want of discernment; they walk in darkness while the foundations shake."),
]: r.ch(*a)
for sid,sense,src,d in [
 (283885,"take one's place (natsab)",283894,"v1: 'God has taken his PLACE (natsab) in the divine council' - God's standing to judge. Qualifier."),
 (283891,"hold judgment (shaphat)",283894,"v1: 'in the midst of the gods he holds JUDGMENT (shaphat)' - God's judging of the judges. Qualifier."),
 (283934,"arise (qum)",283913,"v8: 'ARISE (qum), O God, judge the earth' - God's rising to judge petitioned. Qualifier."),
 (283936,"judge (shaphat)",283913,"v8: 'Arise, O God, JUDGE (shaphat) the earth' - God's righteous judgment. Qualifier."),
 (283939,"inherit (nachal)",283913,"v8: 'for you shall INHERIT (nachal) all the nations' - God's sovereign claim over the nations. Qualifier."),
]: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (283887,"council (edah)","v1: 'in the divine COUNCIL (edah)' - the assembly of the 'gods'/judges, the setting. Standalone."),
 (283899,"give justice (shaphat)","v3: 'GIVE JUSTICE (shaphat) to the weak and fatherless' - the duty enjoined on the judges. Standalone."),
 (283902,"maintain the right (tsadaq)","v3: 'MAINTAIN THE RIGHT (tsadaq) of the afflicted' - the just duty commanded. Standalone."),
 (283905,"rescue (palat)","v4: 'RESCUE (palat) the weak and the needy' - the duty enjoined. Standalone."),
 (283908,"deliver (natsal)","v4: 'DELIVER (natsal) them from the hand of the wicked' - the duty commanded. Standalone."),
 (283916,"walk about (halak)","v5: 'they WALK ABOUT (halak) in darkness' - the judges' benighted conduct, image. Standalone."),
 (283917,"darkness (chashekah)","v5: 'walk about in DARKNESS (chashekah)' - the moral dark of the corrupt, image. Standalone."),
 (283919,"foundations (mosad)","v5: 'all the FOUNDATIONS (mosad) of the earth are shaken' - the world's order undone by injustice, image. Standalone."),
 (283921,"shaken (mot)","v5: 'the foundations of the earth are SHAKEN (mot)' - the tottering of order, image. Standalone."),
 (283930,"die (muth)","v7: 'nevertheless, like men you shall DIE (muth)' - the mortality of the judges, image of their fall. Standalone."),
 (283931,"fall (naphal)","v7: 'and FALL (naphal) like any prince' - the coming downfall of the corrupt, image. Standalone."),
]: r.st(sid,sense,d)
r.write()
