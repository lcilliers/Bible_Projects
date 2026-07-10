import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,97,
  note="Ps97 'The LORD reigns' theophany + moral response (12v). Passages: God reigns in cloud/fire/lightning, earth trembles v1-6; idolaters shamed, Zion glad v7-9; the moral charge to those who love God v10-12. Human IB: the idol-WORSHIPERS PUT-TO-SHAME who BOAST in idols (called to WORSHIP God); ZION HEARS + is GLAD + Judah REJOICEs; those who LOVE the LORD + HATE evil; the SAINTS; the RIGHTEOUS + UPRIGHT in HEART for whom JOY is sown; REJOICE + GIVE-THANKS. God's reign/righteousness/fire/preserve/deliver/exalted = qualifiers; clouds/lightning/mountains-melt + earth/coastlands cosmic joy + idols imagery = standalone.")
CH=[
 (285687,"worshipers of images (abad)","status","idolaters","worship images","instead of God",IB,"paired with being put to shame","v7: 'All WORSHIPERS (abad) of images are put to shame' - those who serve carved gods, false devotion exposed and confounded."),
 (285689,"put to shame (bosh)","state","the idolaters","be put to shame","before the true God",IB,"paired with worshipping images","v7: 'All worshipers of images are PUT TO SHAME (bosh)' - the confounding of idolaters when the true God appears."),
 (285690,"boast (halal)","action","the idolaters","boast","in worthless idols",IB,"paired with worshipping images","v7: 'who make their BOAST (halal) in worthless idols' - the misplaced glorying of the idolater, pride in nothing."),
 (285692,"worship (shachah)","action","the gods / all","worship","God",GOD,"paired with the idolaters shamed","v7: 'WORSHIP (shachah) him, all you gods!' - the call for every power to bow to God, worship due him alone."),
 (285696,"hear (shama)","action","Zion","hear","of God's judgments",IB,"paired with being glad","v8: 'Zion HEARS (shama) and is glad' - the holy city receiving news of God's just reign, hearing that gladdens."),
 (285697,"glad (samach)","state","Zion","be glad","at God's judgments",IB,"paired with hearing","v8: 'Zion hears and is GLAD (samach)' - the joy of God's people at his righteous rule."),
 (285700,"rejoice (gil)","action","the daughters of Judah","rejoice","because of God's judgments",IB,"paired with Zion's gladness","v8: 'and the daughters of Judah REJOICE (gil)' - the towns of Judah exulting in God's justice."),
 (285629,"love (aheb)","disposition","those who love God","love","the LORD",GOD,"paired with hating evil","v10: 'O you who LOVE (aheb) the LORD, hate evil!' - the love of God that is the ground of the moral charge, devotion that shapes conduct."),
 (285631,"hate (sane)","disposition","those who love God","hate","evil",IB,"paired with loving God","v10: 'O you who love the LORD, HATE (sane) evil!' - the aversion to evil that flows from loving God, love and hate rightly ordered."),
 (285635,"saints (chasid)","status","God's saints","be godly","preserved by God",IB,"paired with being delivered from the wicked","v10: 'He preserves the lives of his SAINTS (chasid)' - the faithful whom God guards, the godly community."),
 (285643,"righteous (tsaddiq)","status","the righteous","have light sown","for them",IB,"paired with joy for the upright","v11: 'Light is sown for the RIGHTEOUS (tsaddiq)' - the just for whom God stores up light, brightness appointed the upright."),
 (285644,"joy (simchah)","state","the upright","have joy","sown for them",IB,"paired with the light for the righteous","v11: 'and JOY (simchah) for the upright in heart' - the gladness God prepares for the upright, joy sown to spring up."),
 (285645,"upright (yashar)","status","the upright","be upright","in heart",IB,"paired with the joy sown","v11: 'joy for the UPRIGHT (yashar) in heart' - the straight-hearted for whom joy is stored."),
 (285646,"heart (leb)","faculty","the upright","be upright","in heart",IB,"paired with uprightness","v11: 'joy for the upright in HEART (leb)' - the inner rectitude for which joy is sown."),
 (285647,"rejoice (samach)","action","the righteous","rejoice","in the LORD",GOD,"paired with giving thanks","v12: 'REJOICE (samach) in the LORD, O you righteous' - the summons to the just to find joy in God."),
 (285649,"righteous (tsaddiq)","status","the righteous","rejoice","in God",IB,"paired with rejoicing","v12: 'Rejoice in the LORD, O you RIGHTEOUS (tsaddiq)' - the just called to joy and thanks."),
 (285650,"give thanks (yadah)","action","the righteous","give thanks","to God's holy name",GOD,"paired with rejoicing","v12: 'and GIVE THANKS (yadah) to his holy name!' - the gratitude of the righteous, praise of God's holiness."),
]
for a in CH: r.ch(*a)
QU=[
 (285623,"reigns (malak)",285697,"v1: 'The LORD REIGNS (malak)' - God's kingship. Qualifier."),
 (285657,"righteousness (tsedeq)",285697,"v2: 'RIGHTEOUSNESS (tsedeq) and justice are the foundation of his throne' - God's righteousness. Qualifier."),
 (285658,"justice (mishpat)",285697,"v2: 'righteousness and JUSTICE (mishpat)' - God's justice. Qualifier."),
 (285663,"goes (halak)",285697,"v3: 'Fire GOES (halak) before him' - God's advancing in fire. Qualifier."),
 (285665,"burns up (lahat)",285697,"v3: 'and BURNS UP (lahat) his adversaries' - God's consuming judgment. Qualifier."),
 (285680,"righteousness (tsedeq)",285696,"v6: 'The heavens proclaim his RIGHTEOUSNESS (tsedeq)' - God's righteousness. Qualifier."),
 (285683,"see (raah)",285696,"v6: 'all the peoples SEE (raah) his glory' - the peoples beholding God's glory. Qualifier."),
 (285685,"glory (kabod)",285696,"v6: 'all the peoples see his GLORY (kabod)' - God's glory. Qualifier."),
 (285702,"judgments (mishpat)",285696,"v8: 'because of your JUDGMENTS (mishpat), O LORD' - God's judgments that gladden Zion. Qualifier."),
 (285711,"exalted (alah)",285647,"v9: 'you are EXALTED (alah) far above all gods' - God's supremacy. Qualifier."),
 (285633,"preserve (shamar)",285635,"v10: 'He PRESERVES (shamar) the lives of his saints' - God's guarding of the godly. Qualifier."),
 (285636,"deliver (natsal)",285635,"v10: 'he DELIVERS (natsal) them from the hand of the wicked' - God's rescue of the saints. Qualifier."),
 (285653,"holy name (qodesh)",285650,"v12: 'give thanks to his HOLY NAME (qodesh)' - God's holy name. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
ST=[
 (285625,"rejoice (gil)","v1: 'let the EARTH rejoice (gil)' - the earth's joy, cosmic-geographic personification. Standalone."),
 (285628,"glad (samach)","v1: 'let the many coastlands be GLAD (samach)!' - the distant lands' gladness, cosmic-geographic personification. Standalone."),
 (285654,"clouds (anan)","v2: 'CLOUDS (anan) and thick darkness are all around him' - the storm-cloud of theophany, image. Standalone."),
 (285655,"thick darkness (araphel)","v2: 'clouds and THICK DARKNESS (araphel)' - the dark of God's presence, image. Standalone."),
 (285659,"foundation (makon)","v2: 'the FOUNDATION (makon) of his throne' - the base of God's throne, image. Standalone."),
 (285661,"throne (kisse)","v2: 'the foundation of his THRONE (kisse)' - God's throne, image. Standalone."),
 (285667,"adversaries (tsar)","v3: 'and burns up his ADVERSARIES (tsar)' - God's foes consumed, object. Standalone."),
 (307153,"lightnings (baraq)","v4: 'His LIGHTNINGS (baraq) light up the world' - the theophany lightning, image. Standalone."),
 (307154,"light up (or)","v4: 'his lightnings LIGHT UP (or) the world' - the flash of theophany, image. Standalone."),
 (307157,"sees (raah)","v4: 'the earth SEES (raah) and trembles' - the earth beholding God, cosmic reaction. Standalone."),
 (307158,"trembles (chul)","v4: 'the earth sees and TREMBLES (chul)' - the earth quaking at God, cosmic reaction (not human IB). Standalone."),
 (285670,"melt (masas)","v5: 'The mountains MELT (masas) like wax before the LORD' - the mountains dissolving at God's presence, cosmic image. Standalone."),
 (285671,"wax (donag)","v5: 'melt like WAX (donag)' - the melting wax, image of the mountains before God. Standalone."),
 (285679,"proclaim (nagad)","v6: 'The HEAVENS proclaim (nagad) his righteousness' - the heavens' testimony, cosmic personification. Standalone."),
 (285688,"images (pesel)","v7: 'All worshipers of IMAGES (pesel)' - the carved idols, object of false worship. Standalone."),
 (285691,"worthless idols (elil)","v7: 'who make their boast in WORTHLESS IDOLS (elil)' - the empty idols, image. Standalone."),
 (285632,"evil (ra)","v10: 'hate EVIL (ra)!' - the evil to be hated, object of the char hate (285631). Standalone."),
 (285634,"lives (nephesh)","v10: 'He preserves the LIVES (nephesh) of his saints' - the lives God guards, object. Standalone."),
 (285640,"wicked (rasha)","v10: 'from the hand of the WICKED (rasha)' - the wicked from whom the saints are delivered, object. Standalone."),
 (285641,"light (or)","v11: 'LIGHT (or) is sown for the righteous' - the light stored for the just, image of blessing. Standalone."),
 (285642,"sown (zara)","v11: 'Light is SOWN (zara) for the righteous' - the sowing of light/joy, image. Standalone."),
 (285651,"remembrance (zeker)","v12: 'give thanks to the REMEMBRANCE (zeker) of his holiness' - the memorial of God's holy name, object of thanks. Standalone."),
]
for sid,sense,d in ST: r.st(sid,sense,d)
r.write()
