import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,101,
  note="Ps101 David's resolve to integrity (8v; a moral-conduct catalogue). Passages: I will sing + walk with integrity of heart v1-2; I hate the crooked, the perverse heart far from me v3-4; I purge the slanderer/haughty/deceitful, the faithful shall minister v5-8. IB: SING+MAKE-MUSIC; PONDER the BLAMELESS way, WALK with INTEGRITY of HEART; the resolve (SET nothing worthless before eyes), HATE the FALL-AWAY, the PERVERSE HEART far, KNOW no evil; the SLANDERS, HAUGHTY, ARROGANT HEART purged; the FAITHFUL who WALK BLAMELESS; the DECEIT/LIES/WICKED expelled. God's steadfast-love/justice (sung) = qualifiers; the purge-verbs (destroy/cut-off) + base-thing/evildoers imagery = standalone.")
CH=[
 (268808,"sing (shir)","action","David","sing","of steadfast love and justice",GOD,"paired with making music to God","v1: 'I will SING (shir) of steadfast love and justice; to you, O LORD, I will make music' - the king's worship, praising the very virtues he means to embody."),
 (268813,"make music (zamar)","action","David","make music","to the LORD",GOD,"paired with the singing","v1: 'to you, O LORD, I will MAKE MUSIC (zamar)' - the sung devotion that frames the resolve of integrity."),
 (268814,"ponder (sakal)","action","David","ponder / give heed","to the blameless way",IB,"paired with walking with integrity","v2: 'I will PONDER (sakal) the way that is blameless' - the deliberate attention to a life of integrity, resolve begun in reflection."),
 (268816,"blameless (tamim)","disposition","David","pursue the blameless way","before God",IB,"paired with pondering it","v2: 'I will ponder the way that is BLAMELESS (tamim)' - the whole, undivided way of life David sets before himself."),
 (268819,"walk (halak)","action","David","walk","with integrity of heart",IB,"paired with integrity of heart","v2: 'I will WALK (halak) with integrity of heart within my house' - the resolve lived out, integrity not merely pondered but practised at home."),
 (268820,"integrity (tom)","disposition","David","have integrity","of heart",IB,"paired with the walking and the heart","v2: 'I will walk with INTEGRITY (tom) of heart' - the wholeness of moral purpose, the king's undivided commitment."),
 (268821,"heart (lebab)","faculty","David","be of integrity","in heart",IB,"paired with integrity","v2: 'with integrity of HEART (lebab) within my house' - the inner self where the integrity is seated, honesty beginning within."),
 (268826,"set (shith)","action","David","refuse to set","anything worthless before his eyes",IB,"paired with hating the crooked","v3: 'I will not SET (shith) before my eyes anything that is worthless' - the resolve to keep the gaze clean, guarding the eyes from base things."),
 (268831,"hate (sane)","disposition","David","hate","the work of the crooked",IB,"paired with refusing evil to cling","v3: 'I HATE (sane) the work of those who fall away' - the settled aversion to apostasy and its deeds."),
 (268833,"fall away (set)","status","the crooked","fall away / turn aside","from God's way",IB,"paired with the hated work","v3: 'the work of those who FALL AWAY (set)' - the turncoats whose deeds David hates, the apostates he will not let cling to him."),
 (268837,"perverse (iqqesh)","disposition","the perverse","have a twisted heart","far from David",IB,"paired with the perverse heart","v4: 'A PERVERSE (iqqesh) heart shall be far from me' - the crookedness of soul David banishes from his presence."),
 (268838,"heart (lebab)","faculty","the perverse","be perverse","in heart",IB,"paired with perverseness","v4: 'A perverse HEART (lebab) shall be far from me' - the twisted inner self David refuses to keep company with."),
 (268841,"know (yada, negated)","disposition","David","know nothing","of evil",IB,"paired with the evil refused","v4: 'I will KNOW (yada) nothing of evil' - the deliberate ignorance of wickedness, refusing intimacy with evil."),
 (268844,"slander (lashan)","action","the slanderer","slander secretly","his neighbour",IB,"paired with being destroyed by the king","v5: 'Whoever SLANDERS (lashan) his neighbour secretly I will destroy' - the secret defamer, the vice the king will not tolerate."),
 (268848,"haughty (gaboah)","disposition","the proud","have a haughty look","before the king",IB,"paired with the arrogant heart","v5: 'The one who has a HAUGHTY (gaboah) look' - the proud eyes the king will not endure, arrogance he purges."),
 (268850,"arrogant (rachab)","disposition","the proud","have an arrogant heart","which the king rejects",IB,"paired with the haughty look","v5: 'and an ARROGANT (rachab) heart I will not endure' - the swollen heart of pride, intolerable to the king."),
 (268851,"heart (lebab)","faculty","the proud","be arrogant","in heart",IB,"paired with arrogance","v5: 'and an arrogant HEART (lebab) I will not endure' - the inner seat of the pride the king expels."),
 (268855,"faithful (aman)","status","the faithful in the land","be faithful","to God",IB,"paired with the blameless who minister","v6: 'I will look with favour on the FAITHFUL (aman) in the land' - the trustworthy whom the king honours, faithfulness rewarded with nearness."),
 (268860,"walk (halak)","action","the blameless servant","walk","in the blameless way",IB,"paired with being blameless","v6: 'he who WALKS (halak) in the way that is blameless shall minister to me' - the servant whose upright walk fits him for the king's service."),
 (268862,"blameless (tamim)","disposition","the servant","be blameless","in the way",IB,"paired with walking","v6: 'he who walks in the way that is BLAMELESS (tamim)' - the integrity that qualifies for the king's household."),
 (268867,"deceit (remiyah)","disposition","the deceitful","practise deceit","in the king's house",IB,"paired with the liar expelled","v7: 'No one who practises DECEIT (remiyah) shall dwell in my house' - the treachery the king bars from his presence."),
 (268873,"lies (sheqer)","action","the liar","utter lies","before the king",IB,"paired with the deceit expelled","v7: 'no one who utters LIES (sheqer) shall continue before my eyes' - the falsehood the king will not let stand."),
 (268881,"wicked (rasha)","status","the wicked","be destroyed","from the city",IB,"paired with the evildoers cut off","v8: 'Morning by morning I will destroy all the WICKED (rasha) in the land' - the godless the king purges daily, evil rooted out of God's city."),
]
for a in CH: r.ch(*a)
QU=[
 (268809,"steadfast love (chesed)",268808,"v1: 'I will sing of STEADFAST LOVE (chesed)' - God's covenant love, the virtue sung. Qualifier."),
 (268810,"justice (mishpat)",268808,"v1: 'of steadfast love and JUSTICE (mishpat)' - God's justice, sung by the king. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (268830,"worthless (beliyaal)","v3: 'anything that is WORTHLESS (beliyaal)' - the base/vile thing David refuses to set before his eyes, object of the resolve (char, 268826). Standalone."),
 (268832,"work (asah)","v3: 'I hate the WORK (asah) of those who fall away' - the deeds of the apostates, object of the hatred. Standalone."),
 (268835,"cling (dabaq)","v3: 'it shall not CLING (dabaq) to me' - the evil that will not cleave to David, the resolve stated. Standalone."),
 (268839,"far (sur)","v4: 'A perverse heart shall be FAR (sur) from me' - the removal of the perverse, the distancing. Standalone."),
 (268843,"evil (ra)","v4: 'I will know nothing of EVIL (ra)' - the wickedness David refuses to know, object of the char (268841). Standalone."),
 (268845,"neighbor (rea)","v5: 'Whoever slanders his NEIGHBOUR (rea) secretly' - the victim of the slander. Standalone."),
 (268846,"secretly (sether)","v5: 'slanders his neighbour SECRETLY (sether)' - the hidden manner of the slander, image. Standalone."),
 (268847,"destroy (tsamath)","v5: 'I will DESTROY (tsamath)' - the king's purging of the slanderer, judicial act. Standalone."),
 (268853,"endure (yakol)","v5: 'an arrogant heart I will not ENDURE (yakol)' - the king's refusal to tolerate pride, the resolve. Standalone."),
 (268858,"dwell (yashab)","v6: 'that they may DWELL (yashab) with me' - the faithful dwelling with the king, the reward. Standalone."),
 (268863,"minister (sharath)","v6: 'shall MINISTER (sharath) to me' - the blameless serving the king, the honour. Standalone."),
 (268866,"practise (asah)","v7: 'No one who PRACTISES (asah) deceit' - the doing of deceit, the act of the char (268867). Standalone."),
 (268868,"dwell (yashab)","v7: 'shall DWELL (yashab) in my house' - the deceitful barred from the house. Standalone."),
 (268872,"utter (dabar)","v7: 'no one who UTTERS (dabar) lies' - the speaking of the char lies (268873). Standalone."),
 (268874,"continue (kun)","v7: 'shall CONTINUE (kun) before my eyes' - the liar not permitted to remain. Standalone."),
 (268879,"destroy (tsamath)","v8: 'I will DESTROY (tsamath) all the wicked' - the king's daily purge, judicial act. Standalone."),
 (268883,"cut off (karath)","v8: 'CUTTING OFF (karath) all the evildoers' - the removal of the wicked from the city, judicial act. Standalone."),
 (268885,"evildoers (paal aven)","v8: 'all the EVILDOERS (paal aven) from the city of the LORD' - the workers of iniquity purged, object. Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
