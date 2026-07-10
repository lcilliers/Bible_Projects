import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,79,
  note="Ps79 community lament over ravaged Jerusalem (Asaph). Passages: DESOLATION v1-4 (temple defiled, bodies to birds, become a reproach); APPEAL v5-13 (how-long/pour wrath on the godless nations, do-not-remember our iniquities, help/deliver/atone, avenge the blood, groans of prisoners, vow of thanks forever). Human IB: the FAITHFUL slain; the SHAME of becoming a reproach; the nations who do not KNOW/CALL on God; the confessed INIQUITIES/SINS; being BROUGHT very low; the GROANS of the prisoners; the vow to GIVE-THANKS + RECOUNT God's praise. God's anger/jealousy/compassion/help/deliver/atone/avenge/power = qualifiers; temple/bodies/blood/taunts imagery = standalone.")
# --- CHARS ---
r.ch(283508,"faithful / godly ones (chasid)","status","the godly ones (chasidim) of the people","be the faithful, now slain","given to the beasts","paired with the shame of the ravaged city",IB,
  "v2: 'the flesh of your FAITHFUL (chasid) to the beasts of the earth' - the covenant-faithful, the godly ones, now corpses; their very faithfulness makes the outrage sharper - it is God's devoted who lie unburied.")
r.ch(283511,"become a reproach (cherpah)","state","we (the people)","become an object of scorn","to the neighbours","paired with being mocked and derided",IB,
  "v4: 'We have BECOME (cherpah) a taunt to our neighbours' - the communal humiliation, the shame of a people whose God seems to have abandoned them; disgrace felt as an inner wound.")
r.ch(283530,"know (yada, negated)","disposition","the nations","fail to know","God","paired with not calling on his name",GOD,
  "v6: 'the nations that do not KNOW (yada) you' - the godless ignorance of the nations, their refusal to acknowledge God; the wicked's inner posture toward him, ground of the plea for wrath on them.")
r.ch(283535,"call upon (qara, negated)","action","the kingdoms","fail to call upon","God's name","paired with not knowing God",GOD,
  "v6: 'and on the kingdoms that do not CALL (qara) upon your name' - the nations' refusal to invoke God, godlessness expressed as prayerlessness.")
r.ch(283540,"iniquities (avon)","state","we (the people)","bear former guilt","before God","paired with being brought low and the plea not to remember",IB,
  "v8: 'Do not remember against us our former INIQUITIES (avon)' - the confessed guilt of the fathers, owned by the praying community; sin acknowledged as the deeper cause of the ruin.")
r.ch(283544,"be brought low (dalal)","state","we (the people)","be brought very low","under judgment","paired with the confessed iniquities",IB,
  "v8: 'for we are BROUGHT (dalal) very low' - the abasement of the people, reduced and weakened; the low estate that grounds the appeal for speedy compassion.")
r.ch(283554,"sins (chattath)","state","we (the people)","bear sin","before God","paired with the plea to atone",IB,
  "v9: 'and atone for our SINS (chattath), for your name's sake' - the people's sins owned in the appeal for pardon; guilt confessed so that atonement may be sought.")
r.ch(283471,"groans (anaqah)","state","the prisoners","groan in captivity","before God","paired with the plea to preserve those doomed to die",IB,
  "v11: 'Let the GROANS (anaqah) of the prisoners come before you' - the anguished sighing of the captives, the sound of suffering lifted to God as its own petition.")
r.ch(283493,"give thanks (yadah)","action","we your people","give thanks","to God, forever","paired with recounting his praise",GOD,
  "v13: 'But we your people... will GIVE THANKS (yadah) to you forever' - the vow of praise that closes the lament, gratitude promised across generations even out of desolation.")
r.ch(283498,"recount / declare (saphar)","action","we your people","recount / declare","God's praise to every generation","paired with the vow of thanks",GOD,
  "v13: 'from generation to generation we will RECOUNT (saphar) your praise' - the promise to hand on God's praiseworthy deeds, thanksgiving become transmission.")
# --- QUALIFIERS (God's attributes/acts) ---
r.qu(283464,"inheritance (nachalah)",283511,"v1: 'the nations have come into your INHERITANCE (nachalah)' - God's own possession invaded; God-content. Qualifier.")
r.qu(283466,"holy (qodesh)",283511,"v1: 'they have defiled your HOLY (qodesh) temple' - God's holiness; God-content. Qualifier.")
r.qu(283519,"be angry (anaph)",283544,"v5: 'How long, O LORD? Will you be ANGRY (anaph) forever?' - God's anger; the divine wrath the lament questions. Qualifier.")
r.qu(283521,"jealousy (qinah)",283544,"v5: 'Will your JEALOUSY (qinah) burn like fire?' - God's jealous zeal. Qualifier.")
r.qu(283522,"burn (baar)",283544,"v5: 'will your jealousy BURN (baar) like fire?' - God's blazing zeal. Qualifier.")
r.qu(283524,"pour out (shaphak)",283530,"v6: 'POUR OUT (shaphak) your anger on the nations' - God's act of judgment petitioned. Qualifier.")
r.qu(283525,"anger (chemah)",283530,"v6: 'pour out your ANGER (chemah) on the nations' - God's wrath. Qualifier.")
r.qu(283536,"name (shem)",283535,"v6: 'that do not call upon your NAME (shem)' - God's name; God-content. Qualifier.")
r.qu(283538,"remember (zakar)",283540,"v8: 'Do not REMEMBER (zakar) against us our former iniquities' - God's remembering, here asked to be withheld. Qualifier.")
r.qu(283541,"compassion (racham)",283544,"v8: 'let your COMPASSION (racham) come speedily to meet us' - God's mercy petitioned. Qualifier.")
r.qu(283542,"come speedily (maher)",283544,"v8: 'let your compassion COME SPEEDILY (maher)' - God's swift mercy. Qualifier.")
r.qu(283543,"meet (qadam)",283544,"v8: 'come speedily to MEET (qadam) us' - God's coming to the low. Qualifier.")
r.qu(283546,"help (azar)",283493,"v9: 'HELP (azar) us, O God of our salvation' - God's helping petitioned. Qualifier.")
r.qu(283548,"salvation (yesha)",283493,"v9: 'O God of our SALVATION (yesha)' - God's saving; God-content. Qualifier.")
r.qu(283550,"glory (kabod)",283493,"v9: 'for the GLORY (kabod) of your name' - God's glory, the motive of the plea. Qualifier.")
r.qu(283551,"name (shem)",283493,"v9: 'for the glory of your NAME (shem)' - God's name. Qualifier.")
r.qu(283552,"deliver (natsal)",283493,"v9: 'DELIVER (natsal) us' - God's rescue petitioned. Qualifier.")
r.qu(283553,"atone (kaphar)",283554,"v9: 'and ATONE (kaphar) for our sins' - God's covering of sin petitioned. Qualifier.")
r.qu(283556,"name's sake (shem)",283493,"v9: 'for your NAME'S (shem) sake' - God's name, the ground of the appeal. Qualifier.")
r.qu(306841,"avenging (naqam)",283471,"v10: 'Let the AVENGING (naqam) of the outpoured blood of your servants be known' - God's vengeance petitioned. Qualifier.")
r.qu(306845,"be known (yada)",283471,"v10: 'be KNOWN (yada) among the nations before our eyes' - God's making his justice known. Qualifier.")
r.qu(283476,"great (godel)",283471,"v11: 'according to your GREAT (godel) power' - God's greatness. Qualifier.")
r.qu(283477,"power / arm (zeroa)",283471,"v11: 'according to your great POWER (zeroa)' - God's mighty arm. Qualifier.")
r.qu(283478,"preserve (yathar)",283471,"v11: 'PRESERVE (yathar) those doomed to die' - God's preserving petitioned. Qualifier.")
r.qu(283481,"return (shuv)",283511,"v12: 'RETURN (shuv) sevenfold into the lap of our neighbours' - God's requiting act petitioned. Qualifier.")
r.qu(283499,"praise (tehillah)",283498,"v13: 'we will recount your PRAISE (tehillah)' - God's praiseworthy renown, what is recounted. Qualifier.")
# --- STANDALONE (imagery / place / temporal) ---
r.st(283465,"defiled (tame)","v1: 'they have DEFILED (tame) your holy temple' - the profaning done by the nations; the desecration event. Standalone.")
r.st(283468,"laid in ruins (sim)","v1: 'they have LAID (sim) Jerusalem in ruins' - the nations' ruining of the city. Standalone.")
r.st(283470,"ruins (i)","v1: 'laid Jerusalem in RUINS (i)' - the heaps of rubble, image of desolation. Standalone.")
r.st(283501,"bodies (nebelah)","v2: 'the BODIES (nebelah) of your servants' - the corpses of the slain, image of the outrage. Standalone.")
r.st(283506,"food (maakal)","v2: 'to the birds of the heavens for FOOD (maakal)' - the dead given as carrion, image. Standalone.")
r.st(283507,"flesh (basar)","v2: 'the FLESH (basar) of your faithful to the beasts' - the bodies of the godly (the char, 283508), image of desecration. Standalone.")
r.st(306823,"poured out (shaphak)","v3: 'They have POURED OUT (shaphak) their blood like water' - the massacre, the nations' act. Standalone.")
r.st(306824,"blood (dam)","v3: 'their BLOOD (dam) like water all around Jerusalem' - the shed blood, image of slaughter. Standalone.")
r.st(306830,"bury (qabar)","v3: 'and there was no one to BURY (qabar) them' - the unburied dead, the crowning dishonour. Standalone.")
r.st(283513,"mocked (laag)","v4: 'MOCKED (laag) and derided by those around us' - the neighbours' scorn, the outward form of the reproach (the char, 283511). Standalone.")
r.st(283514,"derided (qeles)","v4: 'and DERIDED (qeles) by those around us' - the enemies' jeering. Standalone.")
r.st(283532,"kingdoms (mamlakah)","v6: 'and on the KINGDOMS (mamlakah) that do not call upon your name' - the godless nations. Standalone.")
r.st(306832,"devoured (akal)","v7: 'For they have DEVOURED (akal) Jacob' - the nations' consuming of the people, image. Standalone.")
r.st(306834,"laid waste (shamem)","v7: 'and LAID WASTE (shamem) his habitation' - the desolated homeland, image. Standalone.")
r.st(306835,"habitation (naveh)","v7: 'laid waste his HABITATION (naveh)' - the ruined dwelling-place, image. Standalone.")
r.st(283539,"former (rishon)","v8: 'our FORMER (rishon) iniquities' - the sins of earlier generations; temporal. Standalone.")
r.st(306842,"outpoured (shaphak)","v10: 'the OUTPOURED (shaphak) blood of your servants' - the spilled blood crying for vengeance, image. Standalone.")
r.st(306843,"blood (dam)","v10: 'the outpoured BLOOD (dam) of your servants' - the martyrs' blood, image. Standalone.")
r.st(283480,"doomed to die (temuthah)","v11: 'preserve those DOOMED TO DIE (temuthah)' - the condemned prisoners, the objects of the plea. Standalone.")
r.st(283482,"sevenfold (shibathayim)","v12: 'Return SEVENFOLD (shibathayim) into the lap of our neighbours' - the full measure of requital. Standalone.")
r.st(283483,"lap / bosom (cheq)","v12: 'into the LAP (cheq) of our neighbours' - the bosom where the recompense is poured, image. Standalone.")
r.st(283485,"taunts (cherpah)","v12: 'the TAUNTS (cherpah) with which they have taunted you' - the enemies' reproach against God, image. Standalone.")
r.st(283487,"taunted (charaph)","v12: 'with which they have TAUNTED (charaph) you, O Lord' - the enemies' scorn of God. Standalone.")
r.st(283492,"pasture (marith)","v13: 'the sheep of your PASTURE (marith)' - the flock-image of the people. Standalone.")
r.st(283494,"forever (olam)","v13: 'will give thanks to you FOREVER (olam)' - the perpetuity of the vowed thanks; temporal. Standalone.")
r.write()
