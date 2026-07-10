#!/usr/bin/env python
# One-off builder for the Ps 78 reread JSON (241 spans). Emits the full genre-aware
# ledger scaffolding so only role + bearer + discovery are hand-authored.
# Chars get the mandatory poetic ledger (101,102,104,105,106,107,108,112,116,114,115);
# qualifiers get 101 + 103(source->char, res=span) + 114 + 115; standalone 101+114+115.
import json, os

def CH(sid, sense, typ, bearer, op, target, coupling, locus, disc):
    return [
        {"n":101,"l":"sense","k":"value","v":sense},
        {"n":102,"l":"type","k":"value","v":typ},
        {"n":104,"l":"seat","k":"pair","v":"none","res":"none"},
        {"n":105,"l":"bearer","k":"pair","v":bearer,"to":sid,"res":"inferred"},
        {"n":106,"l":"operation","k":"event","v":op},
        {"n":107,"l":"target","k":"pair","v":target,"to":sid,"res":"inferred"},
        {"n":108,"l":"manner","k":"pair","v":"none","res":"none"},
        {"n":112,"l":"coupling","k":"pair","v":coupling,"to":sid,"res":"inferred"},
        {"n":116,"l":"locus","k":"value","v":locus},
        {"n":114,"l":"discovery","k":"note","v":disc},
        {"n":115,"l":"role","k":"value","v":"characteristic"},
    ]

def QU(sid, sense, src_to, disc):
    return [
        {"n":101,"l":"sense","k":"value","v":sense},
        {"n":103,"l":"source","k":"pair","v":"God-content qualifier","to":src_to,"res":"span"},
        {"n":114,"l":"discovery","k":"note","v":disc},
        {"n":115,"l":"role","k":"value","v":"qualifier"},
    ]

def ST(sid, sense, disc):
    return [
        {"n":101,"l":"sense","k":"value","v":sense},
        {"n":114,"l":"discovery","k":"note","v":disc},
        {"n":115,"l":"role","k":"value","v":"standalone"},
    ]

IB="internal:ib-state"; GOD="external:god"; PER="external:person"
spans={}
def ch(sid,*a): spans[str(sid)]={"gloss":a[0],"dims":CH(sid,*a)}
def qu(sid,sense,src,disc): spans[str(sid)]={"gloss":sense,"dims":QU(sid,sense,src,disc)}
def st(sid,sense,disc): spans[str(sid)]={"gloss":sense,"dims":ST(sid,sense,disc)}

# ---------------- CHARACTERISTICS (human inner being) ----------------
ch(283001,"give ear / attend (azan)","action","my people","attend / give ear","the teaching that rehearses God's deeds","paired with the received tradition (v3)",PER,
   "'GIVE EAR (azan), O my people, to my teaching' - the summoned attention of the people to the instruction that will hand on God's deeds; the opening call to receive.")
ch(306759,"hear / receive (shama)","action","we (the psalmist's generation)","receive by hearing","the things heard and known","paired with knowing and the fathers' telling",IB,
   "'things that we have HEARD (shama) and known, that our fathers have told us' - tradition taken in by hearing, faith received before it is understood.")
ch(306760,"know (yada)","action","we","know / hold as one's own","the tradition of God's deeds","paired with the hearing",IB,
   "'that we have heard and KNOWN (yada)' - the received story become the community's own settled knowledge.")
ch(306762,"tell / recount (saphar)","action","our fathers","recount / hand on","the deeds of God to the children","paired with the hearing and knowing",PER,
   "'that our fathers have TOLD (saphar) us' - the fathers' handing-on of the story, the living chain of transmission.")
ch(283197,"hide (kachad, refused)","action","we","refuse to conceal","God's deeds from the children","paired with the resolve to tell",PER,
   "'We will not HIDE (kachad) them from their children' - the resolve NOT to conceal God's deeds from the young, transmission as duty.")
ch(283199,"tell / recount (saphar)","action","we","recount / declare","the glorious deeds of the LORD to the coming generation","paired with the refusal to hide",PER,
   "'but TELL (saphar) to the coming generation the glorious deeds of the LORD' - the deliberate declaring of God's works to those yet to come.")
ch(283270,"teach (yada, hiphil)","action","our fathers","teach / make known","the law to their children","paired with the appointed testimony",PER,
   "'which he commanded our fathers to TEACH (yada) to their children' - the charge to instruct the young in God's testimony.")
ch(283351,"know (yada)","action","the next generation","come to know","God's deeds","paired with the telling to children",IB,
   "'that the next generation might KNOW (yada) them, the children yet unborn' - the intended knowing of the generations to come.")
ch(283355,"tell / recount (saphar)","action","the children","recount / hand on","God's deeds to their own children","paired with the coming generation's knowing",PER,
   "'and arise and TELL (saphar) them to their children' - the chain continued, each generation passing on what it knew.")
ch(306764,"set / place (sim)","action","the children","set / fix","their hope on God","paired with the hope, not-forgetting, and keeping (v7)",GOD,
   "'so that they should SET (sim) their hope in God' - the deliberate placing of confidence on God, the act that fixes hope where it belongs.")
ch(306765,"hope / confidence (kesel)","disposition","the children","set one's hope","in God","paired with not forgetting and keeping (v7)",GOD,
   "'so that they should set their HOPE (kesel) in God' - the whole aim of transmission: confidence fixed on God rather than self.")
ch(306768,"forget (shakach, negated)","disposition","the children","refuse to forget","the works of God","paired with hope and obedience",IB,
   "'and not FORGET (shakach) the works of God' - the guarded memory, the safeguard against the fathers' fatal amnesia (v11).")
ch(306771,"keep / observe (natsar)","action","the children","keep / obey","his commandments","paired with hope and remembrance",GOD,
   "'but KEEP (natsar) his commandments' - the obedience that hope in God bears as fruit.")
ch(283442,"be stubborn (sarar)","status","the fathers","be obstinate","against God","paired with rebelliousness and the unsteady heart",IB,
   "'that they should not be like their fathers, a STUBBORN (sarar) and rebellious generation' - the obstinacy the young are warned not to inherit.")
ch(283443,"be rebellious (marah)","status","the fathers","rebel / defy","God","paired with stubbornness",IB,
   "'a stubborn and REBELLIOUS (marah) generation' - the ingrained defiance that marked the wilderness fathers.")
ch(283446,"heart not steadfast (leb)","faculty","the fathers","fail to be fixed","toward God","paired with the unfaithful spirit",IB,
   "'a generation whose HEART (leb) was not steadfast' - the unfixed heart, faith without root, the root defect of the fathers.")
ch(283449,"spirit not faithful (ruach)","faculty","the fathers","fail in fidelity","toward God","paired with the unsteady heart",IB,
   "'whose SPIRIT (ruach) was not faithful to God' - the inner disloyalty, the spirit not held true.")
ch(283451,"be faithful (aman, negated)","disposition","the fathers","fail to be faithful","to God","paired with the unsteady heart",GOD,
   "'whose spirit was not FAITHFUL (aman) to God' - the fidelity of heart that the fathers lacked toward God.")
ch(283010,"keep (shamar, failed)","action","Ephraim / the fathers","fail to keep","God's covenant","paired with the refusal to walk in his law",GOD,
   "'They did not KEEP (shamar) God's covenant' - the covenant unkept, the martial cowardice of v9 traced to unbelief.")
ch(283013,"refuse (maen)","action","the fathers","refuse","to walk according to his law","paired with the covenant unkept",GOD,
   "'and REFUSED (maen) to walk according to his law' - the willed rejection of obedience.")
ch(283016,"forget (shakach)","action","the fathers","forget","God's works and wonders","paired with the wonders no longer believed",IB,
   "'They FORGOT (shakach) his works and the wonders he had shown them' - the forgetting the prologue warned of, now realized in the fathers.")
ch(283044,"sin (chata)","action","they","sin","against God","paired with rebelling against the Most High",GOD,
   "'Yet they SINNED (chata) still more against him, rebelling against the Most High' - sin mounting even amid the wonders.")
ch(283047,"rebel (marah)","action","they","rebel","against the Most High","paired with the sinning",GOD,
   "'REBELLING (marah) against the Most High in the desert' - defiance in the very place of God's provision.")
ch(283050,"test / put to proof (nasah)","action","they","test / try","God","paired with the heart and the craving",GOD,
   "'They TESTED (nasah) God in their heart by demanding the food they craved' - the presumptuous trying of God born of appetite.")
ch(283052,"heart (lebab)","faculty","they","harbour the demand","against God","paired with the testing and craving",IB,
   "'tested God in their HEART (lebab)' - the heart as the seat of the presumptuous demand.")
ch(283054,"demand / ask (shaal)","action","they","demand / ask imperiously","food from God","paired with the testing heart and the craving",GOD,
   "'by DEMANDING (shaal) the food they craved' - the imperious asking born of appetite, the presumptuous claim laid on God.")
ch(283056,"crave (nephesh / desire)","disposition","they","crave / lust after","food","paired with the testing heart",IB,
   "'the food they CRAVED (nephesh)' - the soul-appetite that drove the wilderness rebellion.")
ch(283094,"believe (aman, negated)","disposition","they","fail to believe","in God","paired with not trusting his saving power",GOD,
   "'because they did not BELIEVE (aman) in God' - the root unbelief beneath the complaint.")
ch(283097,"trust (batach, negated)","disposition","they","fail to trust","his saving power","paired with the unbelief",GOD,
   "'and did not TRUST (batach) his saving power' - confidence withheld from the God who had just delivered them.")
ch(283124,"be filled / sated (saba)","state","they","be sated","with the craved food","paired with the craving God indulged",IB,
   "'they ate and were well FILLED (saba), for he gave them what they craved' - the sated appetite God granted even in displeasure.")
ch(283127,"crave (taavah)","disposition","they","crave","the food","paired with the fullness",IB,
   "'he gave them what they CRAVED (taavah)' - the desire God met, the lust indulged unto judgment.")
ch(283129,"craving / lust (taavah)","disposition","they","lust","after food","paired with the wrath that fell mid-meal",IB,
   "'before they had satisfied their CRAVING (taavah), while the food was still in their mouths' - the unslaked lust when wrath struck.")
ch(283146,"sin (chata)","action","they","sin","against God","paired with not believing the wonders",GOD,
   "'In spite of all this, they still SINNED (chata)' - sin persisting past both mercy and judgment.")
ch(283150,"believe (aman, negated)","disposition","they","fail to believe","in his wonders","paired with the persistent sinning",GOD,
   "'and did not BELIEVE (aman) in his wonders' - unbelief that even miracles could not cure.")
ch(283155,"terror / dread (behalah)","state","they","live in dread","under judgment","paired with the vanishing days",IB,
   "'he made their days vanish... and their years in TERROR (behalah)' - the dread in which the faithless, futile years were spent.")
ch(283157,"seek (darash)","action","they","seek / resort to","God","paired with repenting and seeking earnestly",GOD,
   "'When he killed them, they SOUGHT (darash) him' - the seeking that only the sword could compel.")
ch(283158,"repent / turn (shuv)","action","they","turn back","to God","paired with the seeking",GOD,
   "'they REPENTED (shuv) and sought God earnestly' - the turning-back, though (v37) it proved shallow.")
ch(283159,"seek earnestly (shachar)","action","they","seek earnestly","God","paired with the repenting",GOD,
   "'and SOUGHT (shachar) God earnestly' - the eager, early seeking under the rod of judgment.")
ch(283161,"remember (zakar)","action","they","remember","that God was their rock","paired with the flattering that followed",GOD,
   "'They REMEMBERED (zakar) that God was their rock, the Most High their redeemer' - the memory judgment jogged, but only for a moment.")
ch(306806,"flatter / deceive (pathah)","action","they","flatter / coax","God with their mouths","paired with the lying tongue and unsteady heart",GOD,
   "'But they FLATTERED (pathah) him with their mouths' - the hollow, coaxing words masking an unchanged heart.")
ch(306809,"lie (kazab)","action","they","lie","to God with their tongues","paired with the flattering mouth",GOD,
   "'and LIED (kazab) to him with their tongues' - the falsehood of a repentance not seated in the heart.")
ch(283168,"heart not steadfast (leb)","faculty","they","fail to be fixed","toward God","paired with the unfaithful covenant-keeping",IB,
   "'Their HEART (leb) was not steadfast toward him' - the unfixed heart exposed behind the flattery (echoing v8).")
ch(283172,"be faithful (aman, negated)","disposition","they","fail to be faithful","to his covenant","paired with the unsteady heart",GOD,
   "'they were not FAITHFUL (aman) to his covenant' - the fidelity their words feigned but their hearts withheld.")
ch(283178,"iniquity (avon)","state","they","bear guilt","before God","paired with the compassion that atoned it",IB,
   "'Yet he, being compassionate, atoned for their INIQUITY (avon)' - the guilt God's mercy covered rather than destroyed.")
ch(283191,"flesh / frailty (basar)","status","they","be but flesh","mortal and weak","paired with God's remembering their frailty",IB,
   "'He remembered that they were but FLESH (basar), a wind that passes' - the human frailty and transience that moved God's pity.")
ch(283209,"rebel (marah)","action","they","rebel","against God in the wilderness","paired with grieving him",GOD,
   "'How often they REBELLED (marah) against him in the wilderness' - the recurring, wearying defiance.")
ch(283211,"grieve / pain (atsab)","action","they","grieve / cause pain","to God","paired with the rebelling",GOD,
   "'and GRIEVED (atsab) him in the desert' - the pain their rebellion inflicted on God himself.")
ch(283213,"test (nasah)","action","they","test again and again","God","paired with provoking the Holy One",GOD,
   "'They TESTED (nasah) God again and again' - the repeated presumption, testing turned habitual.")
ch(283216,"provoke / pain (tavah)","action","they","provoke / wound","the Holy One of Israel","paired with the testing",GOD,
   "'and PROVOKED (tavah) the Holy One of Israel' - the wounding of the Holy One by their limits set on him.")
ch(283220,"remember (zakar, negated)","action","they","fail to remember","his power and redemption","paired with the deeds of the Exodus they forgot",IB,
   "'They did not REMEMBER (zakar) his power, the day when he redeemed them' - forgetfulness of the very deliverance, the recital that follows being what they forgot.")
ch(283302,"be afraid (pachad, negated)","state","his people","be unafraid / secure","under God's leading","paired with the sea that overwhelmed the foe",IB,
   "'he led them in safety, so that they were not AFRAID (pachad)' - the security of those God shepherds, set against the drowned enemy.")
ch(283323,"test (nasah)","action","they","test","the Most High God","paired with rebelling and not keeping",GOD,
   "'Yet they TESTED (nasah) and rebelled against the Most High God' - the testing renewed even in the promised land.")
ch(283324,"rebel (marah)","action","they","rebel","against the Most High","paired with the testing",GOD,
   "'and REBELLED (marah) against the Most High God' - defiance persisting into settled possession.")
ch(283328,"keep (shamar, negated)","action","they","fail to keep","his testimonies","paired with turning away treacherously",GOD,
   "'and did not KEEP (shamar) his testimonies' - the covenant word still unheld in the land.")
ch(283330,"turn away / back (sug)","action","they","turn away","from God","paired with acting treacherously",GOD,
   "'but TURNED AWAY (sug) and acted treacherously like their fathers' - the apostasy inherited from the fathers.")
ch(283331,"act treacherously (bagad)","action","they","betray / deal faithlessly","with God","paired with turning away",GOD,
   "'and ACTED TREACHEROUSLY (bagad) like their fathers' - the faithless betrayal, family likeness of sin.")
ch(283335,"be deceitful (remiyah)","status","they","prove false","like a slack bow","paired with the treachery",IB,
   "'they twisted like a DECEITFUL (remiyah) bow' - treachery imaged as a warped bow that fails its aim.")
ch(283337,"provoke to anger (kaas)","action","they","provoke to anger","God","paired with moving him to jealousy by idols",GOD,
   "'For they provoked him to ANGER (kaas) with their high places' - the deliberate rousing of God's anger by their idolatry.")
ch(283432,"be upright (tom)","disposition","David","be upright / of integrity","in shepherding the people","paired with the upright heart and skillful hand",IB,
   "'With UPRIGHT (tom) heart he shepherded them' - the integrity of the shepherd-king, the psalm's counter to the faithless generation.")
ch(283433,"heart (lebab)","faculty","David","be steadfast and true","toward God and people","paired with the uprightness and skill",IB,
   "'with upright HEART (lebab) he shepherded them' - the true, steadfast heart set against the unsteadfast heart of the fathers (v8, v37).")
ch(283437,"skillful / understanding (tabun)","disposition","David","govern skilfully","the people","paired with the upright heart",IB,
   "'and guided them with SKILLFUL (tabun) hand' - the wise competence of David's rule, integrity joined to skill.")

# ---------------- QUALIFIERS (God's acts / attributes) ----------------
qu(283201,"glorious deeds (tehillah)",283199,"v4: 'the GLORIOUS deeds of the LORD' - God's praiseworthy acts, object of the telling. Qualifier.")
qu(283203,"the LORD (Yahweh)",283199,"v4: 'the glorious deeds of the LORD (Yahweh)' - the divine name; God-content. Qualifier.")
qu(283204,"might (ezuz)",283199,"v4: 'and his MIGHT (ezuz)' - God's strength, told to the children. Qualifier.")
qu(283205,"wonders (pele)",283199,"v4: 'and the WONDERS (pele) that he has done' - God's marvels. Qualifier.")
qu(283207,"done (asah)",283199,"v4: 'the wonders that he has DONE (asah)' - God's working. Qualifier.")
qu(283261,"testimony (eduth)",283270,"v5: 'He established a TESTIMONY (eduth) in Jacob' - God's covenant witness. Qualifier.")
qu(283263,"appointed (sum)",283270,"v5: 'and APPOINTED (sum) a law in Israel' - God's establishing. Qualifier.")
qu(283264,"law (torah)",283270,"v5: 'appointed a LAW (torah) in Israel' - God's instruction. Qualifier.")
qu(283267,"commanded (tsavah)",283270,"v5: 'which he COMMANDED (tsavah) our fathers' - God's charge. Qualifier.")
qu(306766,"God (Elohim)",306765,"v7: 'set their hope in GOD (Elohim)' - the object of hope; God-content. Qualifier.")
qu(306769,"works of God (maalal)",306768,"v7: 'not forget the WORKS (maalal) of God' - God's deeds. Qualifier.")
qu(306772,"commandments (mitsvah)",306771,"v7: 'but keep his COMMANDMENTS (mitsvah)' - God's precepts. Qualifier.")
qu(283452,"God (El)",283451,"v8: 'not faithful to GOD (El)' - the divine name; God-content. Qualifier.")
qu(283012,"covenant (berith)",283010,"v10: 'did not keep God's COVENANT (berith)' - God's covenant. Qualifier.")
qu(283015,"law (torah)",283013,"v10: 'refused to walk according to his LAW (torah)' - God's law. Qualifier.")
qu(283017,"works (alilah)",283016,"v11: 'They forgot his WORKS (alilah)' - God's deeds forgotten. Qualifier.")
qu(283018,"wonders (pele)",283016,"v11: 'and the WONDERS (pele) he had shown them' - God's marvels. Qualifier.")
qu(283025,"performed (asah)",283016,"v12: 'In the sight of their fathers he PERFORMED (asah) marvels' - God's working. Qualifier.")
qu(283026,"wonders (pele)",283016,"v12: 'he performed WONDERS (pele) in the land of Egypt' - God's marvels. Qualifier.")
qu(283032,"divided (baqa)",283016,"v13: 'He DIVIDED (baqa) the sea and let them pass through' - God's act at the sea. Qualifier.")
qu(283034,"pass through (abar)",283016,"v13: 'and let them PASS THROUGH (abar)' - God's leading through the sea. Qualifier.")
qu(306774,"led (nachah)",283016,"v14: 'In the daytime he LED (nachah) them with a cloud' - God's guidance. Qualifier.")
qu(283038,"split (baqa)",283016,"v15: 'He SPLIT (baqa) rocks in the wilderness' - God's provision of water. Qualifier.")
qu(283041,"gave drink (shaqah)",283016,"v15: 'and gave them DRINK (shaqah) abundantly as from the deep' - God's provision. Qualifier.")
qu(283048,"Most High (elyon)",283047,"v17: 'rebelling against the MOST HIGH (elyon)' - the divine title. Qualifier.")
qu(283051,"God (El)",283050,"v18: 'They tested GOD (El) in their heart' - the divine name. Qualifier.")
qu(283066,"struck the rock (nakah)",283094,"v20: 'Behold, he STRUCK (nakah) the rock so that water gushed out' - God's act, quoted in their taunt. Qualifier.")
qu(283083,"heard (shama)",283044,"v21: 'Therefore, when the LORD HEARD (shama), he was full of wrath' - God's hearing. Qualifier.")
qu(283084,"full of wrath (abar)",283044,"v21: 'he was FULL OF WRATH (abar)' - God's anger kindled. Qualifier.")
qu(283086,"kindled (nasaq)",283044,"v21: 'a fire was KINDLED (nasaq) against Jacob' - God's judgment. Qualifier.")
qu(283089,"anger (aph)",283044,"v21: 'and ANGER (aph) rose against Israel' - God's anger. Qualifier.")
qu(283090,"rose (alah)",283044,"v21: 'anger ROSE (alah) against Israel' - God's wrath mounting. Qualifier.")
qu(283095,"God (Elohim)",283094,"v22: 'they did not believe in GOD (Elohim)' - the divine name. Qualifier.")
qu(283099,"saving power (yeshuah)",283097,"v22: 'did not trust his SAVING POWER (yeshuah)' - God's salvation. Qualifier.")
qu(306786,"commanded (tsavah)",283124,"v23: 'Yet he COMMANDED (tsavah) the skies above' - God's provision-command. Qualifier.")
qu(306789,"opened (pathach)",283124,"v23: 'and OPENED (pathach) the doors of heaven' - God's opening the heavens. Qualifier.")
qu(283100,"rained down (matar)",283124,"v24: 'and he RAINED DOWN (matar) on them manna to eat' - God's provision. Qualifier.")
qu(306796,"sent (shalach)",283124,"v25: 'he SENT (shalach) them food in abundance' - God's provision. Qualifier.")
qu(283109,"caused to blow (nasa)",283124,"v26: 'He caused the east wind to BLOW (nasa) in the heavens' - God's act. Qualifier.")
qu(283111,"power (oz)",283124,"v26: 'and by his POWER (oz) he led out the south wind' - God's power. Qualifier.")
qu(283112,"led out (nahag)",283124,"v26: 'he LED OUT (nahag) the south wind' - God's directing the winds. Qualifier.")
qu(283114,"rained (matar)",283124,"v27: 'he RAINED (matar) meat on them like dust' - God's provision of quail. Qualifier.")
qu(306800,"let fall (naphal)",283124,"v28: 'he let them FALL (naphal) in the midst of their camp' - God's provision. Qualifier.")
qu(283134,"anger (aph)",283146,"v31: 'the ANGER (aph) of God rose against them' - God's wrath. Qualifier.")
qu(283135,"God (Elohim)",283146,"v31: 'the anger of GOD (Elohim) rose' - the divine name. Qualifier.")
qu(283136,"rose (alah)",283146,"v31: 'the anger of God ROSE (alah) against them' - God's wrath mounting. Qualifier.")
qu(283137,"killed (harag)",283146,"v31: 'and he KILLED (harag) the strongest of them' - God's judgment. Qualifier.")
qu(283139,"laid low (kara)",283146,"v31: 'and LAID LOW (kara) the young men of Israel' - God's judgment. Qualifier.")
qu(283148,"wonders (pele)",283150,"v32: 'and did not believe in his WONDERS (pele)' - God's marvels. Qualifier.")
qu(283152,"made vanish (kalah)",283155,"v33: 'So he made their days VANISH (kalah) like a breath' - God's judgment on their years. Qualifier.")
qu(283156,"killed (harag)",283157,"v34: 'When he KILLED (harag) them, they sought him' - God's judgment that drove them to seek. Qualifier.")
qu(283167,"redeemer (gaal)",283161,"v35: 'the Most High their REDEEMER (gaal)' - God as redeemer. Qualifier.")
qu(283174,"covenant (berith)",283172,"v37: 'not faithful to his COVENANT (berith)' - God's covenant. Qualifier.")
qu(283175,"he (God, compassionate)",283178,"v38: 'Yet HE, being compassionate' - God the subject of mercy. Qualifier.")
qu(283176,"compassionate (rachum)",283178,"v38: 'he, being COMPASSIONATE (rachum), atoned for their iniquity' - God's compassion. Qualifier.")
qu(283177,"atoned (kaphar)",283178,"v38: 'ATONED (kaphar) for their iniquity' - God's covering of sin. Qualifier.")
qu(283180,"destroy (shachath, restrained)",283178,"v38: 'and did not DESTROY (shachath) them' - God's withheld destruction. Qualifier.")
qu(283181,"restrained (shuv)",283178,"v38: 'he RESTRAINED (shuv) his anger often' - God's held-back wrath. Qualifier.")
qu(283182,"anger (aph)",283178,"v38: 'he restrained his ANGER (aph) often' - God's anger restrained. Qualifier.")
qu(283185,"stir up (ur)",283178,"v38: 'and did not STIR UP (ur) all his wrath' - God's mercy in not unleashing full wrath. Qualifier.")
qu(283188,"wrath (chemah)",283178,"v38: 'did not stir up all his WRATH (chemah)' - God's wrath held in check. Qualifier.")
qu(283189,"remembered (zakar)",283191,"v39: 'He REMEMBERED (zakar) that they were but flesh' - God's mindful pity of their frailty. Qualifier.")
qu(283214,"God (El)",283213,"v41: 'They tested GOD (El) again' - the divine name. Qualifier.")
qu(283217,"Holy One (qadosh)",283216,"v41: 'and provoked the HOLY ONE (qadosh) of Israel' - God's holiness. Qualifier.")
qu(283221,"power / hand (yad)",283220,"v42: 'They did not remember his POWER (yad)' - God's mighty hand. Qualifier.")
qu(283224,"redeemed (padah)",283220,"v42: 'the day when he REDEEMED (padah) them from the foe' - God's redemption. Qualifier.")
qu(283228,"performed (sum)",283220,"v43: 'when he PERFORMED (sum) his signs in Egypt' - God's signs. Qualifier.")
qu(283231,"marvels (mopheth)",283220,"v43: 'and his MARVELS (mopheth) in the fields of Zoan' - God's wonders. Qualifier.")
qu(283234,"turned to blood (haphak)",283220,"v44: 'He TURNED (haphak) their rivers to blood' - God's plague. Qualifier.")
qu(283240,"sent (shalach)",283220,"v45: 'He SENT (shalach) among them swarms of flies' - God's plague. Qualifier.")
qu(306812,"destroyed (harag)",283220,"v47: 'He DESTROYED (harag) their vines with hail' - God's plague. Qualifier.")
qu(283246,"gave over (sagar)",283220,"v48: 'He GAVE OVER (sagar) their cattle to the hail' - God's plague. Qualifier.")
qu(283251,"let loose (shalach)",283220,"v49: 'He LET LOOSE (shalach) on them his burning anger' - God's wrath sent. Qualifier.")
qu(283252,"burning anger (charon)",283220,"v49: 'his BURNING (charon) anger' - God's fierce wrath. Qualifier.")
qu(283253,"anger (aph)",283220,"v49: 'his burning ANGER (aph)' - God's wrath. Qualifier.")
qu(283254,"wrath (ebrah)",283220,"v49: 'WRATH (ebrah), indignation, and distress' - God's fury on Egypt. Qualifier.")
qu(283255,"indignation (zaam)",283220,"v49: 'wrath, INDIGNATION (zaam), and distress' - God's wrath. Qualifier.")
qu(283273,"made a path (palas)",283220,"v50: 'He MADE (palas) a path for his anger' - God's directed wrath. Qualifier.")
qu(283275,"anger (aph)",283220,"v50: 'a path for his ANGER (aph)' - God's wrath. Qualifier.")
qu(283278,"spare (chasak, not)",283220,"v50: 'he did not SPARE (chasak) their soul from death' - God's unsparing judgment. Qualifier.")
qu(283281,"gave over (sagar)",283220,"v50: 'but GAVE (sagar) their life over to the plague' - God's judgment. Qualifier.")
qu(283284,"struck down (nakah)",283220,"v51: 'He STRUCK DOWN (nakah) every firstborn in Egypt' - God's climactic plague. Qualifier.")
qu(283292,"led out (nasa)",283302,"v52: 'Then he LED OUT (nasa) his people like sheep' - God's shepherding. Qualifier.")
qu(283296,"guided (nahag)",283302,"v52: 'and GUIDED (nahag) them in the wilderness like a flock' - God's guidance. Qualifier.")
qu(283299,"led (nachah)",283302,"v53: 'He LED (nachah) them in safety' - God's leading. Qualifier.")
qu(283304,"overwhelmed (kasah)",283302,"v53: 'but the sea OVERWHELMED (kasah) their enemies' - God's judgment on the foe. Qualifier.")
qu(283313,"won / acquired (qanah)",283302,"v54: 'the mountain which his right hand had WON (qanah)' - God's acquiring of Zion. Qualifier.")
qu(283314,"drove out (garash)",283323,"v55: 'He DROVE OUT (garash) nations before them' - God's conquest-gift. Qualifier.")
qu(283317,"apportioned (naphal)",283323,"v55: 'and APPORTIONED (naphal) them for a possession' - God's allotment. Qualifier.")
qu(283319,"settled (shakan)",283323,"v55: 'and SETTLED (shakan) the tribes of Israel in their tents' - God's settling. Qualifier.")
qu(283325,"Most High (elyon)",283323,"v56: 'they tested the MOST HIGH (elyon) God' - the divine title. Qualifier.")
qu(283326,"God (Elohim)",283324,"v56: 'tested the Most High GOD (Elohim)' - the divine name. Qualifier.")
qu(283329,"testimonies (eduth)",283328,"v56: 'and did not keep his TESTIMONIES (eduth)' - God's covenant witness. Qualifier.")
qu(283340,"jealousy (qana)",283337,"v58: 'and moved him to JEALOUSY (qana) with their idols' - God's jealousy provoked. Qualifier.")
qu(283343,"heard (shama)",283331,"v59: 'When God HEARD (shama), he was full of wrath' - God's hearing. Qualifier.")
qu(283344,"full of wrath (abar)",283331,"v59: 'he was FULL OF WRATH (abar)' - God's anger. Qualifier.")
qu(283346,"rejected / utterly (maas)",283331,"v59: 'and he utterly REJECTED (maas) Israel' - God's rejection. Qualifier.")
qu(306817,"forsook (natash)",283331,"v60: 'He FORSOOK (natash) his dwelling at Shiloh' - God's abandonment of Shiloh. Qualifier.")
qu(306821,"dwelt (shakan)",283331,"v60: 'the tent where he DWELT (shakan) among mankind' - God's dwelling. Qualifier.")
qu(283365,"gave over (sagar)",283331,"v62: 'He GAVE (sagar) his people over to the sword' - God's judgment. Qualifier.")
qu(283368,"wrath (abar)",283331,"v62: 'and vented his WRATH (abar) on his heritage' - God's anger. Qualifier.")
qu(283392,"put to rout (nakah)",283331,"v66: 'And he PUT (nakah) his adversaries to rout' - God's beating-back of the foe. Qualifier.")
qu(283396,"rejected (maas)",283432,"v67: 'He REJECTED (maas) the tent of Joseph' - God's sovereign rejection of Ephraim. Qualifier.")
qu(283400,"choose (bachar, not)",283432,"v67: 'and did not CHOOSE (bachar) the tribe of Ephraim' - God's election-decision. Qualifier.")
qu(283403,"chose (bachar)",283432,"v68: 'but CHOSE (bachar) the tribe of Judah' - God's election of Judah. Qualifier.")
qu(283409,"loves (aheb)",283432,"v68: 'Mount Zion, which he LOVES (aheb)' - God's love for Zion. Qualifier.")
qu(283417,"chose (bachar)",283432,"v70: 'He CHOSE (bachar) David his servant' - God's election of David. Qualifier.")
qu(283420,"took (laqach)",283432,"v70: 'and TOOK (laqach) him from the sheepfolds' - God's calling of David. Qualifier.")

# ---------------- STANDALONE (imagery / cultic / place / people-name / temporal) ----------------
st(283003,"teaching (torah)","v1: 'give ear to my TEACHING (torah)' - the psalmist's instruction, the medium. Standalone.")
st(306749,"open the mouth (pathach)","v2: 'I will OPEN (pathach) my mouth in a parable' - the manner of teaching. Standalone.")
st(306752,"parable (mashal)","v2: 'in a PARABLE (mashal)' - the figurative form of instruction. Standalone.")
st(306755,"dark sayings (chidah)","v2: 'I will utter DARK SAYINGS (chidah) from of old' - the riddles of the past. Standalone.")
st(306758,"things (asher)","v3: 'the THINGS that we have heard' - the content of the tradition. Standalone.")
st(283272,"children (ben)","v5: 'commanded our fathers to teach to their CHILDREN (ben)' - the recipients of transmission. Standalone.")
st(283350,"generation (dor)","v6: 'that the next GENERATION (dor) might know' - the generations to come. Standalone.")
st(283444,"generation (dor)","v8: 'a stubborn and rebellious GENERATION (dor)' - the fathers as a class. Standalone.")
st(283448,"steadfast (kun)","v8: 'whose heart was not STEADFAST (kun)' - the fixity the heart lacked. Standalone (quality).")
st(283455,"bow (ramah, armed)","v9: 'The Ephraimites, armed with the BOW (ramah)' - the martial equipment. Standalone.")
st(283456,"turned back (haphak)","v9: 'TURNED BACK (haphak) on the day of battle' - the martial failure emblematic of faithlessness. Standalone.")
st(283055,"food (okel)","v18: 'demanding the FOOD (okel) they craved' - the object of appetite. Standalone.")
st(283060,"Can God? (yakol)","v19: 'Can (yakol) God spread a table in the wilderness?' - the taunting challenge of unbelief. Standalone.")
st(283069,"gushed out (zub)","v20: 'water GUSHED OUT (zub)' - the water from the rock, image. Standalone.")
st(283071,"overflowed (shataph)","v20: 'and streams OVERFLOWED (shataph)' - the abundant water, image. Standalone.")
st(283072,"Can he? (yakol)","v20: 'CAN (yakol) he also give bread?' - the taunt continued. Standalone.")
st(283077,"provide (kun)","v20: 'or PROVIDE (kun) meat for his people?' - the doubting challenge. Standalone.")
st(283078,"meat (sheer)","v20: 'provide MEAT (sheer) for his people' - the demanded food. Standalone.")
st(283091,"Israel (Yisrael)","v21: 'anger rose against ISRAEL (Yisrael)' - the nation. Standalone.")
st(283102,"manna (dagan/man)","v24: 'he rained down MANNA (man) to eat' - the bread of heaven, image of provision. Standalone.")
st(283103,"eat (akal)","v24: 'manna to EAT (akal)' - the eating of the gift. Standalone.")
st(306793,"ate (akal)","v25: 'Man ATE (akal) the bread of the angels' - the eating. Standalone.")
st(283115,"meat (sheer)","v27: 'he rained MEAT (sheer) on them like dust' - the quail, image. Standalone.")
st(283122,"ate (akal)","v29: 'And they ATE (akal) and were well filled' - the eating. Standalone.")
st(283128,"satisfied / estranged (zur)","v30: 'before they were ESTRANGED (zur) from their craving' - the still-unsated state. Standalone.")
st(306807,"mouths (peh)","v36: 'they flattered him with their MOUTHS (peh)' - the organ of the flattery (the char, 306806). Standalone.")
st(306811,"tongues (lashon)","v36: 'and lied to him with their TONGUES (lashon)' - the organ of the lie (the char, 306809). Standalone.")
st(283170,"steadfast toward (kun)","v37: 'their heart was not STEADFAST (kun) toward him' - the fixity the heart lacked. Standalone (quality).")
st(283186,"all (kol)","v38: 'did not stir up ALL (kol) his wrath' - the totality of wrath withheld. Standalone.")
st(283192,"wind (ruach)","v39: 'a WIND (ruach) that passes and comes not again' - image of human transience. Standalone.")
st(283193,"passes (halak)","v39: 'a wind that PASSES (halak)' - the fleeting movement, image of frailty. Standalone.")
st(283194,"comes not again (shuv)","v39: 'and COMES (shuv) not again' - the irreversibility of the passing breath. Standalone.")
st(283215,"again (shuv)","v41: 'They tested God AGAIN (shuv)' - the repetition of the testing. Standalone (temporal).")
st(283218,"Israel (Yisrael)","v41: 'the Holy One of ISRAEL (Yisrael)' - the nation whose Holy One God is. Standalone.")
st(283238,"drink (shathah)","v44: 'so that they could not DRINK (shathah)' - the effect of the blood-plague. Standalone.")
st(283242,"devoured (akal)","v45: 'swarms of flies, which DEVOURED (akal) them' - the plague-effect. Standalone.")
st(283243,"frogs (tsephardea)","v45: 'and FROGS (tsephardea), which destroyed them' - the plague. Standalone.")
st(283244,"destroyed (shachath)","v45: 'frogs, which DESTROYED (shachath) them' - the plague-effect. Standalone.")
st(305921,"labor / produce (yegia)","v46: 'He gave their crops (yegia, labour) to the destroying locust' - the harvest lost. Standalone.")
st(306814,"hail (barad)","v47: 'He destroyed their vines with HAIL (barad)' - the plague. Standalone.")
st(283248,"hail (barad)","v48: 'He gave their cattle over to the HAIL (barad)' - the plague. Standalone.")
st(283258,"destroying / evil (ra)","v49: 'a company of DESTROYING (ra) angels' - the band of destroyers. Standalone.")
st(283259,"angels / messengers (malak)","v49: 'a company of destroying ANGELS (malak)' - the agents of the plague. Standalone.")
st(283274,"path (nathib)","v50: 'He made a PATH (nathib) for his anger' - the way cleared for wrath, image. Standalone.")
st(283279,"their life / soul (nephesh)","v50: 'did not spare their SOUL (nephesh) from death' - the life given to the plague. Standalone.")
st(283283,"plague / pestilence (deber)","v50: 'but gave their life over to the PLAGUE (deber)' - the pestilence, image of judgment. Standalone.")
st(283289,"firstfruits of strength (on)","v51: 'the firstfruits of their STRENGTH (on) in the tents of Ham' - Egypt's firstborn, image. Standalone.")
st(283300,"safety (betach)","v53: 'He led them in SAFETY (betach)' - the security of the guided people. Standalone.")
st(283308,"holy land / border (qodesh)","v54: 'he brought them to his HOLY (qodesh) land' - the sacred territory. Standalone.")
st(283332,"fathers (ab)","v57: 'acted treacherously like their FATHERS (ab)' - the forebears whose sin they repeated. Standalone.")
st(283334,"twisted (haphak)","v57: 'they TWISTED (haphak) like a deceitful bow' - the warping, image of treachery. Standalone.")
st(283336,"bow (qeshet)","v57: 'like a deceitful BOW (qeshet)' - the failed weapon, image. Standalone.")
st(283338,"high places (bamah)","v58: 'they provoked him with their HIGH PLACES (bamah)' - the idolatrous shrines. Standalone.")
st(283341,"idols (pesil)","v58: 'and moved him to jealousy with their IDOLS (pesil)' - the carved images. Standalone.")
st(283359,"power / glory (oz)","v61: 'and delivered his POWER (oz) to captivity' - the ark/glory given up, image. Standalone.")
st(283360,"captivity (shebi)","v61: 'delivered his power to CAPTIVITY (shebi)' - the exile of the ark. Standalone.")
st(283371,"devoured (akal)","v63: 'Fire DEVOURED (akal) their young men' - the sword/fire of war, image. Standalone.")
st(283373,"young women (bethulah)","v63: 'and their YOUNG WOMEN (bethulah) had no marriage song' - the maidens unwed. Standalone.")
st(283375,"marriage song (halal)","v63: 'had no marriage SONG (halal)' - the wedding-praise silenced by war. Standalone.")
st(283377,"fell (naphal)","v64: 'Their priests FELL (naphal) by the sword' - the priests slain, image. Standalone.")
st(283381,"lamentation (bakah)","v64: 'and their widows made no LAMENTATION (bakah)' - the mourning-rite prevented. Standalone.")
st(283387,"shouting (ranan)","v65: 'like a strong man SHOUTING (ranan) because of wine' - the warrior-simile for God awaking. Standalone.")
st(283389,"wine (yayin)","v65: 'shouting because of WINE (yayin)' - the simile's image. Standalone.")
st(283391,"adversaries (tsar)","v66: 'He put his ADVERSARIES (tsar) to rout' - God's foes. Standalone.")
st(283394,"everlasting (olam)","v66: 'he put them to EVERLASTING (olam) reproach' - the perpetuity of the foes' shame. Standalone (temporal).")
st(283395,"reproach / shame (cherpah)","v66: 'everlasting REPROACH (cherpah)' - the enemies' lasting disgrace. Standalone.")
st(283407,"Zion (Tsiyyon)","v68: 'Mount ZION (Tsiyyon), which he loves' - the chosen place. Standalone.")
st(283416,"forever (olam)","v69: 'like the earth, which he has founded FOREVER (olam)' - the permanence of the sanctuary. Standalone (temporal).")
st(283427,"shepherd (raah)","v71: 'to be the SHEPHERD (raah) of Jacob his people' - David's shepherd-office. Standalone.")
st(283434,"shepherded (raah)","v72: 'With upright heart he SHEPHERDED (raah) them' - the outward act expressing David's upright heart (the char, 283432). Standalone.")
st(283435,"guided (nachah)","v72: 'and GUIDED (nachah) them with skillful hand' - the outward act expressing David's skill (the char, 283437). Standalone.")
st(283438,"hand (kaph)","v72: 'guided them with skillful HAND (kaph)' - the instrument of David's rule. Standalone.")

out=os.path.join("verse-analysis","psalms","_read","psalm-078-reread-v1.json")
doc={"book":"Psa","book_id":19,"chapter":78,"provenance":"reread-psalms-2026",
 "note":"Ps78 Asaph's historical maskil (72v, largest read). Human IB veins: TRANSMISSION (give-ear/heard/known/told/tell/teach/know/hope/forget-not/keep v1-7); UNSTEADFAST GENERATION (stubborn/rebellious/heart/spirit/faithless v8); REBELLION CYCLE (sinned/rebelled/tested/craved/believe-not/trust-not/provoked/grieved/forgot/remember-not); FALSE REPENTANCE (sought/flattered/lied/heart-not-steadfast v34-37); iniquity+flesh that moved God's pity (v38-39); DAVID'S upright, skillful heart (v72). God's acts (wonders/manna/quail/plagues/wrath/compassion/choosing Judah-Zion-David) = qualifiers; plague/manna/bow/idol/sanctuary imagery = standalone.",
 "spans":spans}
with open(out,"w",encoding="utf-8") as f: json.dump(doc,f,ensure_ascii=False,indent=1)
print("wrote",out,"spans:",len(spans))
from collections import Counter
print(Counter(d["dims"][-1]["v"] for d in spans.values()))
