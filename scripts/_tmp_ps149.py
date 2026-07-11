#!/usr/bin/env python
"""Ps 149 - praise + the saints' two-edged sword. IB ops: singing a new song in
the assembly; gladness in the Maker, rejoicing in the King; praise with dance
and music; the humble adorned with salvation; the godly exulting, singing on
their beds; high praise in the throat with a sword in hand (militant praise); the
godly as agents of decreed judgment (v7); the honour of executing the written
judgment (v9). Fetter/sword/nation imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=149
r = Reading("Psa", 19, CH, note="Praise + the saints' sword: new song, gladness in the Maker-King, militant praise, decreed judgment")

r.ch(274453,"sing a new song","affect","the godly","the godly sing a new song in the assembly of the faithful - fresh corporate praise","fresh-praise","new-song-in-assembly",IB,
     "v1: 'SING to the LORD a NEW song, his PRAISE in the assembly of the godly' - the interior of the congregation is roused to a praise that is new, not rote.")
r.ch(274465,"glad in Maker, rejoice in King","affect","Israel / the godly","Israel is glad in its Maker, the children of Zion rejoice in their King - joy grounded in relation","relational-joy","glad-in-Maker",IB,
     "v2: 'Let Israel be GLAD in his MAKER; let the children of Zion REJOICE in their KING' - the operation is joy located precisely in who God is to them: maker and king.")
r.ch(274467,"praise with dance and music","affect","the godly","the name praised with dancing, tambourine and lyre - the whole body drawn into praise","embodied-praise","praise-with-dance",IB,
     "v3: 'Let them PRAISE his name with DANCING, making melody with tambourine and lyre' - the interior joy overflows into the moving, sounding body.")
r.ch(274480,"the humble adorned","state","the humble","the humble are the ones God beautifies with salvation - lowliness crowned","humility","humble-adorned",IB,
     "v4: 'he ADORNS the HUMBLE with salvation' - the interior lowliness is what God delights in and dresses with rescue.")
r.ch(274483,"the godly exult on their beds","affect","the godly","the faithful exult in glory and sing for joy even on their beds - praise into private night","exultation","exult-on-beds",IB,
     "v5: 'Let the godly EXULT in glory; let them SING for joy on their beds' - the operation carries praise past the assembly into the solitary hours of rest.")
r.ch(274488,"high praise with sword in hand","affect","the godly","high praises of God in the throat and a two-edged sword in the hand - praise fused with agency","militant-praise","praise-and-sword",IB,
     "v6: 'Let the HIGH PRAISES of God be in their THROATS and two-edged swords in their hands' - the interior praise is not passive: it arms itself, worship and warrant joined.")
r.ch(308216,"execute the decreed vengeance","volition","the godly","the godly are agents to execute vengeance on the nations and punishments on the peoples","agency-of-judgment","execute-vengeance",IB,
     "v7: 'to EXECUTE vengeance on the nations and punishments on the peoples' - the interior resolve turns outward as commissioned action, carrying out a judgment not self-devised.")
r.ch(274496,"the honour of executing judgment","affect","the godly","to carry out the written judgment is the honour of all God's saints - dignity in obedience","dignified-obedience","honour-in-judgment",IB,
     "v9: 'to EXECUTE on them the JUDGMENT written! This is HONOUR for all his godly ones' - the operation is the sense of dignity in performing the decreed judgment; obedience felt as honour.")

for sid,sense,src,d in [
 (274462,"Maker (asah)",274465,"v2: 'let Israel be glad in his MAKER' - the relation grounding the gladness."),
 (274466,"King (melek)",274465,"v2: 'rejoice in their KING' - the relation grounding the rejoicing."),
 (274476,"takes pleasure in his people",274480,"v4: 'the LORD TAKES PLEASURE in his people' - God's delight that crowns the humble."),
 (274479,"adorns with salvation",274480,"v4: 'he ADORNS the humble with salvation' - the beautifying act."),
 (274499,"honour for the godly",274496,"v9: 'this is HONOUR for all his godly ones' - the dignity conferred by the judgment-task."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (sword/fetter/nation/instrument imagery or label); standalone.")
r.write()
