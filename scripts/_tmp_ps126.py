import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,126,
  note="Ps126 'When the LORD restored the fortunes of Zion' (6v). The central operation is GRIEF TRANSFORMED INTO JOY. Chars: the LAUGHTER + JOY that filled the mouth at restoration (v2); the GLADNESS (v3); then the pattern - TEARS in sowing become shouts of JOY in reaping (v5); the sower who goes out WEEPING, BEARING seed, comes home with JOY, BRINGING sheaves (v6). God's restored-fortunes/great-things = qualifiers; dream/streams/seed/sheaves imagery = standalone.")
CH=[
 (272564,"laughter (sechoq)","state","the restored people","laugh","at God's reversal",IB,"paired with the shouts of joy",
  "v2: 'our mouth was filled with LAUGHTER (sechoq)' - the operation of joy overflowing: the reversal so sudden that the mouth fills with helpless laughter, like waking from a dream."),
 (272566,"joy (rinnah)","state","the restored people","shout for joy","at the restoration",IB,"paired with the laughter",
  "v2: 'and our tongue with shouts of JOY (rinnah)' - the joy that bursts into song, the tongue loosed in exultation at what God has done."),
 (272580,"glad (samach)","state","the people","be glad","at God's great deeds",IB,"paired with the great things God has done",
  "v3: 'The LORD has done great things for us; we are GLAD (samach)' - the settled gladness following the first laughter, joy owned and named."),
 (272582,"tears (dimah)","state","the sowers","weep","while sowing",IB,"paired with reaping in joy",
  "v5: 'Those who sow in TEARS (dimah) shall reap with shouts of joy!' - the operation of grief that seeds joy: weeping labour is not wasted but is the very seed of the coming harvest of joy."),
 (272584,"joy (rinnah)","state","the reapers","reap with joy","after sowing in tears",IB,"paired with the tears of sowing",
  "v5: 'shall reap with shouts of JOY (rinnah)!' - the joy that answers the tears, the harvest-shout that repays the sowing-grief."),
 (272587,"weeping (bakah)","state","the sower","go out weeping","bearing seed",IB,"paired with coming home in joy",
  "v6: 'He who goes out WEEPING (bakah), bearing the seed for sowing' - the operation begun in grief: the sower sets out in tears, the loss of the buried seed felt as sorrow."),
 (272588,"bear (nasa)","action","the sower","carry the seed out","in grief",IB,"paired with bringing sheaves home",
  "v6: 'BEARING (nasa) the seed for sowing' - the burdened going-out, carrying the precious seed to be given up to the ground."),
 (272593,"joy (rinnah)","state","the sower","come home with joy","bringing the harvest",IB,"paired with the weeping going-out",
  "v6: 'shall come home with shouts of JOY (rinnah)' - the operation completed: the grief of the going-out answered by the joy of the return."),
 (272594,"bring (nasa)","action","the sower","carry the sheaves home","in joy",IB,"paired with bearing the seed out",
  "v6: 'BRINGING (nasa) his sheaves with him' - the joyful return-burden, the same arms that carried seed in tears now full of sheaves."),
]
for a in CH: r.ch(*a)
QU=[
 (307825,"restored (shuv)",272580,"v1: 'When the LORD RESTORED (shuv) the fortunes of Zion' - God's reversal of the captivity. Qualifier."),
 (272571,"done (asah)",272566,"v2: 'The LORD has DONE (asah) great things for them' - God's mighty deeds. Qualifier."),
 (272572,"great things (gadal)",272566,"v2: 'The LORD has done GREAT THINGS (gadal) for them' - God's great deeds. Qualifier."),
 (272576,"done (asah)",272580,"v3: 'The LORD has DONE (asah) great things for us' - God's deeds. Qualifier."),
 (272577,"great things (gadal)",272580,"v3: 'The LORD has done GREAT THINGS (gadal) for us' - God's great deeds. Qualifier."),
 (307830,"restore (shuv)",272593,"v4: 'RESTORE (shuv) our fortunes, O LORD' - God's restoration petitioned. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (307823,"Ascents (maalah)","v0: heading. Standalone."),
 (307826,"fortunes (shibah)","v1: 'the FORTUNES (shibah) of Zion' - the reversed captivity, image. Standalone."),
 (307829,"dream (chalam)","v1: 'we were like those who DREAM (chalam)' - the dreamlike wonder of the restoration, image. Standalone."),
 (272562,"mouth (peh)","v2: 'our MOUTH (peh) was filled with laughter' - the mouth of the char laughter (272564), image. Standalone."),
 (272563,"filled (male)","v2: 'our mouth was FILLED (male) with laughter' - the overflowing joy, image. Standalone."),
 (307831,"fortunes (shebuth)","v4: 'Restore our FORTUNES (shebuth), O LORD' - the reversal sought, image. Standalone."),
 (307834,"streams (aphiq)","v4: 'like STREAMS (aphiq) in the Negeb!' - the sudden desert torrents, image of swift restoration. Standalone."),
 (272581,"sow (zara)","v5: 'Those who SOW (zara) in tears' - the sowing (char tears, 272582), image of labour. Standalone."),
 (272583,"reap (qatsar)","v5: 'shall REAP (qatsar) with shouts of joy' - the harvest (char joy, 272584), image. Standalone."),
 (272585,"goes out (halak)","v6: 'He who GOES OUT (halak) weeping' - the sower's setting out (char weeping, 272587), image. Standalone."),
 (272586,"out (halak)","v6: 'He who goes OUT (halak)' - the going forth, image. Standalone."),
 (272589,"seed (zera)","v6: 'bearing the SEED (zera) for sowing' - the seed carried out, image. Standalone."),
 (272590,"sowing (meshek)","v6: 'the seed for SOWING (meshek)' - the trail of seed, image. Standalone."),
 (272596,"sheaves (alummah)","v6: 'bringing his SHEAVES (alummah) with him' - the harvest carried home (char bringing, 272594), image. Standalone."),
]: r.st(sid,sense,d)
r.write()
