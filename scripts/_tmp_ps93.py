import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,93,
  note="Ps93 'The LORD reigns' (5v; one movement). A PURE kingship-glory hymn: it celebrates God's majesty, his established throne from everlasting, his mastery over the roaring floods, his trustworthy decrees and holy house - but lexicalizes NO human inner-being response. Per the glory-boundary rule, God's cosmic majesty with no human characteristic for a qualifier to attach to is read as OUTWARD GLORY -> all STANDALONE (0 characteristics, 0 qualifiers). This is the honest reading of a pure God-hymn: pure God-content yields no characteristic.")
for sid,sense,d in [
 (285257,"reigns (malak)","v1: 'The LORD REIGNS (malak)' - God's kingship, the hymn's theme; outward glory. Standalone."),
 (285258,"robed (labesh)","v1: 'he is ROBED (labesh) in majesty' - God clothed in royal splendour, image of glory. Standalone."),
 (285259,"majesty (geuth)","v1: 'robed in MAJESTY (geuth)' - God's kingly grandeur, outward glory. Standalone."),
 (285261,"robed (labesh)","v1: 'the LORD is ROBED (labesh); he has put on strength as his belt' - God clothed in strength, image. Standalone."),
 (285262,"strength (oz)","v1: 'he has put on STRENGTH (oz) as his belt' - God's might as royal girdle, image of glory. Standalone."),
 (285263,"belt (azar)","v1: 'put on strength as his BELT (azar)' - the girding of strength, image. Standalone."),
 (285266,"established (kun)","v1: 'Yes, the world is ESTABLISHED (kun); it shall never be moved' - the firm-founded world, image of God's stable rule. Standalone."),
 (285268,"moved (mot)","v1: 'it shall never be MOVED (mot)' - the unshakeable world, image of God's secure kingship. Standalone."),
 (285269,"throne (kisse)","v2: 'Your THRONE (kisse) is established from of old' - God's royal seat, image of his eternal reign. Standalone."),
 (285270,"established (kun)","v2: 'Your throne is ESTABLISHED (kun) from of old' - the ancient firmness of God's throne, image. Standalone."),
 (285275,"everlasting (olam)","v2: 'you are from EVERLASTING (olam)' - God's eternity; temporal descriptor of his glory. Standalone."),
 (285276,"floods (nahar)","v3: 'The FLOODS (nahar) have lifted up, O LORD' - the roaring rivers/chaos-waters, image. Standalone."),
 (285277,"lifted up (nasa)","v3: 'the floods have LIFTED UP (nasa) their voice' - the surging waters, image of tumult. Standalone."),
 (285279,"floods (nahar)","v3: 'the FLOODS (nahar) lift up their voice' - the roaring waters, image. Standalone."),
 (285280,"lifted up (nasa)","v3: 'the floods LIFT UP (nasa) their roaring' - the swelling waters, image. Standalone."),
 (285281,"voice (qol)","v3: 'the floods have lifted up their VOICE (qol)' - the roar of the waters, image. Standalone."),
 (285282,"floods (nahar)","v3: 'the FLOODS (nahar) lift up their pounding waves' - the tumult of the deep, image. Standalone."),
 (285283,"lift up (nasa)","v3: 'the floods LIFT UP (nasa) their roaring' - the rising waters, image. Standalone."),
 (285285,"roaring (dokhi)","v3: 'the floods lift up their ROARING (dokhi)' - the crash of the waves, image. Standalone."),
 (285286,"mightier (addir)","v4: 'MIGHTIER (addir) than the thunders of many waters' - God's supremacy over the chaos-waters, image of glory. Standalone."),
 (285288,"thunders (qol)","v4: 'than the THUNDERS (qol) of many waters' - the roar of the great waters, image. Standalone."),
 (285291,"mightier (addir)","v4: 'the LORD on high is MIGHTIER (addir)' - God's transcendent might, outward glory. Standalone."),
 (285292,"waves (mishbar)","v4: 'mightier than the WAVES (mishbar) of the sea' - the breakers God overmasters, image. Standalone."),
 (285297,"decrees (edah)","v5: 'Your DECREES (edah) are very trustworthy' - God's testimonies, sure and firm; outward glory of his rule. Standalone."),
 (285299,"trustworthy (aman)","v5: 'Your decrees are very TRUSTWORTHY (aman)' - the sureness of God's word, image of his reliable reign. Standalone."),
 (285300,"holiness (qodesh)","v5: 'HOLINESS (qodesh) befits your house' - the holiness fitting God's dwelling, outward glory. Standalone."),
 (285301,"befits (naah)","v5: 'holiness BEFITS (naah) your house, O LORD, forevermore' - the fitness of holiness to God's house, image. Standalone."),
]: r.st(sid,sense,d)
r.write()
