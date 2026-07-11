#!/usr/bin/env python
"""Ps 24 (who may ascend the hill; the King of glory). The entrance liturgy /
King-of-glory section (vv7-10) = standalone. IB ops: clean hands and a pure
heart; not lifting the soul to what is false (no devotion to idols/deceit); the
generation that seeks God's face."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=24
r = Reading("Psa", 19, CH, note="Who may ascend: clean-hands/pure-heart, soul not set on falsehood, the God-seeking generation (King-of-glory liturgy = standalone)")

r.ch(275890,"clean hands and a pure heart","state","the worshipper","the one who may ascend has clean hands and a pure heart - integrity of deed matched by integrity of the inner self","purity","clean-hands-pure-heart",IB,
     "v4: 'He who has CLEAN hands and a PURE HEART' - the operation names the qualification for God's presence as a doubled purity: the outward act and the inward heart both undefiled.")
r.ch(275894,"the soul not lifted to falsehood","volition","the worshipper","he does not lift up his soul to what is false or swear deceitfully - the self refuses to devote itself to an idol or a lie","undivided-devotion","soul-not-to-false",IB,
     "v4: 'who does not LIFT UP his SOUL to what is false and does not swear deceitfully' - the operation is a refusal of misdirected devotion: the interior will not give itself to emptiness or back a lie with an oath.")
r.ch(275911,"the generation that seeks God's face","volition","those who seek","such is the generation of those who seek God, who seek the face of the God of Jacob - a whole company oriented to seeking him","God-seeking","seek-his-face",IB,
     "v6: 'Such is the generation of those who SEEK him, who seek the FACE of the God of Jacob' - the operation defines a people by the direction of its desire: the seeking of God's face is what marks them.")

for sid,sense,src,d in [
 (275900,"he will receive blessing",275890,"v5: 'He will RECEIVE blessing from the LORD and righteousness from the God of his salvation' - the reward of the clean-handed, pure-hearted worshipper."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (earth-founded, ascend-the-hill, King-of-glory gates liturgy, or label); standalone.")
r.write()
