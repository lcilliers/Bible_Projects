#!/usr/bin/env python
"""Ps 13 ('How long?'). IB ops: the exhausting inner deliberation - counsel in
the soul with daily heart-sorrow; then the turn - trust in steadfast love; the
heart rejoicing in salvation; singing for God's bounty. God's apparent
forgetting/hiding + consider/answer = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=13
r = Reading("Psa", 19, CH, note="'How long?': the soul's daily counsel/sorrow, then the turn to trust, rejoicing heart, song")

r.ch(273544,"counsel in the soul, sorrow in the heart","cognition","the psalmist","the self carries a wearying inner deliberation, taking counsel in its soul with sorrow in its heart all day - the churn of unrelieved anxiety","inner-churn","counsel-and-sorrow",IB,
     "v2: 'How long must I take COUNSEL in my SOUL and have SORROW in my HEART all the day?' - the operation is the exhausting round of self-consultation that finds no rest, sorrow renewed daily.")
r.ch(273572,"trust in steadfast love","affect","the psalmist","against the churn the self plants itself on God's steadfast love - the deliberate turn to trust","the-turn-to-trust","trust-in-chesed",IB,
     "v5: 'But I have TRUSTED in your steadfast love' - the hinge of the psalm: the interior stops deliberating and rests its weight on God's covenant love.")
r.ch(273575,"heart rejoices in salvation","affect","the psalmist","the heart, having trusted, now rejoices in God's salvation - joy following the decision to trust","rejoicing","heart-rejoice",IB,
     "v5: 'my HEART shall REJOICE in your salvation' - distinct from the trust itself: trust releases joy; the once-sorrowing heart of v2 now rejoices.")
r.ch(306030,"sing for his bounty","affect","the psalmist","the self will sing to the LORD because he has dealt bountifully - gratitude become song","grateful-song","sing-for-bounty",IB,
     "v6: 'I will SING to the LORD, because he has dealt bountifully with me' - the arc closes in song; the remembered bounty turns the interior from 'how long' to melody.")

for sid,sense,src,d in [
 (273532,"how long will you forget me",273544,"v1: 'How long, O LORD? Will you FORGET me forever?' - the felt divine absence that drives the soul's churn."),
 (273536,"hide your face",273544,"v1: 'How long will you HIDE your face from me?' - the sense of God's withdrawal fuelling the sorrow."),
 (273555,"consider and answer",273572,"v3: 'CONSIDER and ANSWER me, O LORD my God' - the petition the turn to trust is voiced alongside."),
 (273559,"light up my eyes",273572,"v3: 'LIGHT UP my eyes, lest I sleep the sleep of death' - the reviving act trust asks for."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (death-sleep imagery, enemy-gloating, or label); standalone.")
r.write()
