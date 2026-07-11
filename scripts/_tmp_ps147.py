#!/usr/bin/env python
"""Ps 147 (Hallel) - God heals, feeds, orders nature. IB ops: praise as good,
pleasant, fitting; the brokenhearted God heals; the fear + hope in which God
takes pleasure (distinct); Zion summoned to praise; the humble God lifts up.
God's building/healing/feeding/weather acts = qual; the nature imagery (stars,
snow, frost, rain, grass) = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=147
r = Reading("Psa", 19, CH, note="God heals/feeds/orders nature: praise-as-fitting, the brokenhearted, fear+hope, the humble")

r.ch(274268,"praise good and fitting","affect","the psalmist","the self judges praise itself as good, pleasant, fitting - praise reflected on and endorsed","praise-endorsed","praise-is-fitting",IB,
     "v1: 'PRAISE the LORD! For it is GOOD to sing praises to our God; it is PLEASANT, and praise is FITTING' - the interior does not just praise but affirms praising as right and lovely.")
r.ch(274329,"the brokenhearted healed","state","the wounded","the broken heart and its wounds are the object of God's healing - inner injury bound up","heart-woundedness","brokenhearted-healed",IB,
     "v3: 'He HEALS the BROKENHEARTED and binds up their wounds' - the interior wound (a shattered heart) is named as what God mends; the inner injury is real and addressed.")
r.ch(274288,"the fear God delights in","affect","those who fear","the reverent fear of God in which he takes pleasure - not horse or human strength","reverent-fear","fear-God-delights",IB,
     "v11: 'the LORD takes pleasure in those who FEAR him' - against delight in the horse's strength, God's pleasure rests on the fearing interior.")
r.ch(274289,"hope in steadfast love","affect","those who hope","the hope set on God's steadfast love, paired with fear as what pleases God","steadfast-hope","hope-in-chesed",IB,
     "v11: 'in those who HOPE in his steadfast love' - read distinct from fear: hope leans forward onto covenant love where fear looks up in reverence.")
r.ch(274292,"Zion summoned to praise","affect","Zion / Jerusalem","the city and its people are called to praise and extol God who strengthens and blesses them","corporate-summons","Zion-praise",IB,
     "v12: 'PRAISE the LORD, O Jerusalem! Extol your God, O Zion!' - the interior of the whole community is roused to praise the one who secures its gates and children.")
r.ch(274349,"the humble lifted up","state","the humble","the humble are the ones God lifts up while casting the wicked to the ground","humility","humble-lifted",IB,
     "v6: 'The LORD LIFTS UP the HUMBLE; he casts the wicked to the ground' - the interior lowliness is what God raises; humility is the posture met with lifting.")

for sid,sense,src,d in [
 (274271,"good to sing (tob)",274268,"v1: 'it is GOOD to sing praises' - the goodness the self affirms."),
 (274275,"pleasant (naim)",274268,"v1: 'it is PLEASANT' - the loveliness of praise endorsed."),
 (274277,"fitting (naveh)",274268,"v1: 'praise is FITTING' - the rightness of praise affirmed."),
 (274328,"heals (rapha)",274329,"v3: 'He HEALS the brokenhearted' - the divine mending of the inner wound."),
 (274330,"binds up wounds",274329,"v3: 'BINDS UP their wounds' - God's tending of the injured heart."),
 (274278,"delights not in horse",274288,"v10: 'His DELIGHT is not in the strength of the horse' - the false ground of confidence God rejects."),
 (274287,"takes pleasure (ratsah)",274288,"v11: 'the LORD TAKES PLEASURE in those who fear him' - God's regard for the fearing self."),
 (274348,"lifts up the humble",274349,"v6: 'The LORD LIFTS UP the humble' - God's raising act."),
 (274350,"casts down the wicked",274349,"v6: 'he CASTS the wicked to the ground' - the contrast to the lifted humble."),
 (274299,"strengthens the gates",274292,"v13: 'he STRENGTHENS the bars of your gates' - God's securing of Zion."),
 (274302,"blesses your children",274292,"v13: 'BLESSES your children within you' - God's favour on the city."),
 (274305,"makes peace in borders",274292,"v14: 'He MAKES peace in your borders' - the shalom praised."),
 (308164,"builds up Jerusalem",274292,"v2: 'The LORD BUILDS UP Jerusalem' - the act Zion is summoned to praise."),
 (308166,"gathers the outcasts",274292,"v2: 'he GATHERS the outcasts of Israel' - God's regathering."),
 (274312,"declares his word to Jacob",274292,"v19: 'He DECLARES his word to Jacob, his statutes to Israel' - the special revelation Zion praises."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (nature imagery: stars/snow/frost/rain/grass/clouds, or label); standalone.")
r.write()
