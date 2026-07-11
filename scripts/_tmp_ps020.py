#!/usr/bin/env python
"""Ps 20 (prayer for the king before battle). IB ops: the heart's desire God is
asked to fulfil; rejoicing over salvation; the assurance 'now I know the LORD
saves his anointed'; trust relocated from chariots/horses to the name of the
LORD; standing upright while foes collapse. God's answer/protect/save =
qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=20
r = Reading("Psa", 19, CH, note="Prayer for the king: heart's-desire, salvation-joy, assurance, trust-not-chariots, standing firm")

r.ch(275423,"the heart's desire fulfilled","volition","the king","the people ask God to grant the king his heart's desire and fulfil all his plans - a longing carried to God","desire-granted","heart's-desire",IB,
     "v4: 'May he grant you your HEART'S DESIRE and FULFIL all your plans' - the operation lifts the king's inmost want to God, asking that the deepest wish be met.")
r.ch(275427,"rejoice over salvation","affect","the people","the people will shout for joy over the king's salvation and set up banners in God's name - communal joy at deliverance","salvation-joy","shout-for-joy",IB,
     "v5: 'May we shout for JOY over your SALVATION, and in the name of our God set up our banners' - the interior of the community leaps in anticipated joy, marking the victory as God's.")
r.ch(275438,"'now I know the LORD saves'","cognition","the psalmist","a settled assurance arrives - now I know the LORD saves his anointed and answers from heaven - confidence crystallising","assurance","now-I-know",IB,
     "v6: 'Now I KNOW that the LORD SAVES his anointed; he will answer him from his holy heaven' - the operation is the moment confidence solidifies into knowledge; petition becomes certainty.")
r.ch(275456,"trust the name, not chariots","affect","the people","some trust in chariots and horses, but the people trust in the name of the LORD - reliance deliberately relocated from might to God","relocated-trust","trust-the-name",IB,
     "v7: 'Some TRUST in chariots and some in horses, but we trust in the NAME of the LORD our God' - the operation is a chosen contrast: the interior withdraws its confidence from military power and fixes it on God.")
r.ch(275465,"we rise and stand upright","state","the people","they collapse and fall, but we rise and stand upright - the steadfast standing of those who trust God","steadfastness","rise-and-stand",IB,
     "v8: 'They COLLAPSE and fall, but we RISE and STAND UPRIGHT' - the operation is the enduring stability of the trusting; where the chariot-trusters fall, the God-trusters stand.")

for sid,sense,src,d in [
 (275408,"protect you",275423,"v1: 'May the name of the God of Jacob PROTECT you' - the defence the heart's-desire prayer invokes."),
 (275413,"support you from Zion",275427,"v2: 'may he SUPPORT you from Zion' - the help that grounds the salvation-joy."),
 (275441,"saves his anointed",275438,"v6: 'the LORD SAVES his anointed' - the divine act the assurance rests on."),
 (275467,"save the king",275456,"v9: 'O LORD, SAVE the king! May he answer us when we call' - the closing plea of the trusting."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (offerings/banners/chariots imagery or label); standalone.")
r.write()
