import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,128,
  note="Ps128 'Blessed is everyone who fears the LORD' (6v). Operation = the FEAR of God producing a flourishing life. Chars: the BLESSED man who FEARS + WALKS in God's ways (v1); the BLESSED enjoying his labour's fruit (v2); the BLESSED man who FEARS again (v4). God's bless-from-Zion = qualifier; wife-as-vine/olive-shoots/prosperity imagery = standalone.")
CH=[
 (272648,"blessed (esher)","state","the God-fearer","be blessed","in fearing God",IB,"paired with fearing and walking",
  "v1: 'BLESSED (esher) is everyone who fears the LORD' - the happiness that flows from the fear of God, the beatitude the psalm unfolds."),
 (272650,"fear (yare)","disposition","the God-fearer","fear / revere","God",GOD,"paired with walking in his ways",
  "v1: 'everyone who FEARS (yare) the LORD' - the reverence that is the root of the flourishing life."),
 (272652,"walk (halak)","action","the God-fearer","walk","in God's ways",GOD,"paired with the fear of God",
  "v1: 'who WALKS (halak) in his ways!' - the operation of the fear worked out: reverence issuing in a whole manner of life along God's paths."),
 (272659,"blessed (esher)","state","the God-fearer","be blessed","eating his labour's fruit",IB,"paired with it being well with him",
  "v2: 'you shall be BLESSED (esher), and it shall be well with you' - the blessedness realized: the fruit of one's own labour enjoyed, a settled well-being."),
 (272665,"blessed (barak)","state","the God-fearer","be blessed","for fearing God",IB,"paired with fearing the LORD",
  "v4: 'Thus shall the man be BLESSED (barak) who fears the LORD' - the blessing pronounced, the summary that the God-fearer is the blessed man."),
 (272666,"fear (yare)","disposition","the God-fearer","fear / revere","God",GOD,"paired with the blessing",
  "v4: 'the man be blessed who FEARS (yare) the LORD' - the fear of God, restated as the ground of the whole blessing."),
]
for a in CH: r.ch(*a)
r.qu(272669,"bless (barak)",272665,"v5: 'The LORD BLESS (barak) you from Zion!' - God's blessing from his holy hill. Qualifier.")
for sid,sense,d in [
 (272647,"Ascents (maalah)","v0: heading. Standalone."),
 (272656,"eat (akal)","v2: 'You shall EAT (akal) the fruit of the labour of your hands' - the enjoyment of one's own toil (char blessed, 272659), image. Standalone."),
 (272657,"labour (yegia)","v2: 'the fruit of the LABOUR (yegia) of your hands' - the work rewarded, image. Standalone."),
 (272660,"well (tob)","v2: 'and it shall be WELL (tob) with you' - the well-being of the God-fearer (char blessed, 272659), image. Standalone."),
 (307842,"wife (ishshah)","v3: 'Your WIFE (ishshah) will be like a fruitful vine' - the wife, image of household flourishing. Standalone."),
 (307843,"fruitful (parah)","v3: 'like a FRUITFUL (parah) vine' - the fruitfulness, image of blessing. Standalone."),
 (307844,"vine (gephen)","v3: 'like a fruitful VINE (gephen)' - the vine within the house, image. Standalone."),
 (307849,"olive (zayith)","v3: 'like OLIVE (zayith) shoots' - the children as olive-shoots, image. Standalone."),
 (307850,"shoots (shatil)","v3: 'like olive SHOOTS (shatil) around your table' - the young around the table, image. Standalone."),
 (272672,"see (raah)","v5: 'May you SEE (raah) the prosperity of Jerusalem' - the beholding of the city's good, the blessing. Standalone."),
 (272673,"prosperity (tub)","v5: 'the PROSPERITY (tub) of Jerusalem' - the city's welfare, object of the blessing. Standalone."),
 (272679,"see (raah)","v6: 'May you SEE (raah) your children's children!' - the long life beholding descendants, the blessing. Standalone."),
 (272682,"peace (shalom)","v6: 'PEACE (shalom) be upon Israel!' - the closing benediction, image. Standalone."),
]: r.st(sid,sense,d)
r.write()
