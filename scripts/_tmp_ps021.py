#!/usr/bin/env python
"""Ps 21 (thanksgiving for the king's victory). IB ops: the king's exultant joy
in God's strength and salvation; the granted heart's desire; asking life and
receiving it; gladness in the joy of God's presence; the king's trust that keeps
him unmoved; the enemies' doomed devising of evil; praising God's power. God's
give/bless/save = qualifier; the victory-over-foes = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=21
r = Reading("Psa", 19, CH, note="King's victory-thanks: exultant joy, granted desire, asked-life, gladness in presence, trust->unmoved, enemies' devising, praise")

r.ch(275479,"exult in your strength","affect","the king","the king rejoices in God's strength and exults greatly in his salvation - joy fixed on what God has done","exultation","exult-in-strength",IB,
     "v1: 'O LORD, in your strength the king REJOICES, and in your salvation how greatly he EXULTS!' - the operation is overflowing joy whose object is God's power and rescue, not the king's own prowess.")
r.ch(275503,"the heart's desire granted","affect","the king","God has given the king his heart's desire and not withheld the request of his lips - a longing fully met","fulfilled-longing","desire-not-withheld",IB,
     "v2: 'You have given him his HEART'S DESIRE and have not withheld the REQUEST of his lips' - the operation is the satisfaction of the inmost want; the interior's deepest wish granted.")
r.ch(275515,"asked life, received it","volition","the king","he asked life of God, who gave it - length of days forever - a request answered beyond measure","asking-and-receiving","asked-life",IB,
     "v4: 'He ASKED LIFE of you; you gave it to him, length of days forever and ever' - the operation is a specific petition (life) met with abundance; the interior's request overfulfilled.")
r.ch(275534,"glad with the joy of your presence","affect","the king","God makes the king glad with the joy of his presence - gladness sourced in nearness to God","presence-gladness","glad-in-presence",IB,
     "v6: 'you make him GLAD with the JOY of your presence' - the operation locates the deepest gladness in God's face itself, not merely in the gifts.")
r.ch(275539,"trust that keeps unmoved","affect","the king","the king trusts in the LORD, and through the Most High's steadfast love he shall not be moved - trust yielding stability","trust","trust-unmoved",IB,
     "v7: 'For the king TRUSTS in the LORD, and through the steadfast love of the Most High he shall not be MOVED' - the operation ties stability to trust: the interior's reliance is what makes it immovable.")
r.ch(275489,"the enemies devise doomed evil","cognition","the enemies","the enemies plan evil and devise mischief against God, but they will not succeed - scheming that cannot land","futile-scheming","devise-evil",IB,
     "v11: 'Though they PLAN evil against you, though they DEVISE mischief, they will not succeed' - the enemies' interior is set on harm, but the psalm reads the scheming as already defeated.")
r.ch(275497,"sing and praise God's power","affect","the people","the people will sing and praise God's power, asking him to be exalted in his strength - worship of the victorious God","praise","sing-of-power",IB,
     "v13: 'Be exalted, O LORD, in your strength! We will SING and PRAISE your power' - the operation closes the psalm by turning the victory into song directed at God's might.")

for sid,sense,src,d in [
 (275508,"you meet him with blessings",275503,"v3: 'For you MEET him with rich BLESSINGS' - the divine generosity behind the granted desire."),
 (275528,"you bestow splendour",275534,"v5: 'splendour and majesty you BESTOW on him' - the honour that accompanies the joy of God's presence."),
 (275551,"your hand finds out your foes",275489,"v8: 'Your hand will FIND OUT all your enemies' - the judgment that dooms the devisers of evil."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (crown/blessing/splendour, blazing-fire victory imagery, or label); standalone.")
r.write()
