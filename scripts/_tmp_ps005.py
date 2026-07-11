#!/usr/bin/env python
"""Ps 5 (morning prayer). IB ops: inarticulate groaning God is asked to consider;
directed prayer; the disciplined morning expectancy (prepare and watch); entering
to bow in the fear of God; longing to be led in a straightened way amid foes; the
enemies' grave-throated deceit; their rebellion against God; the joy of those who
take refuge; the love of God's name. God's delight-not/hate/abhor/bless =
qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=5
r = Reading("Psa", 19, CH, note="Morning prayer: groaning/prayer/watching, worship in fear, longing for the straight way, enemies' deceit, refuge-joy")

r.ch(280660,"groaning God is asked to consider","affect","the psalmist","the self brings a groaning too deep for words, asking God to give heed to it - pre-verbal distress","groaning","consider-my-groaning",IB,
     "v1: 'Give ear to my words, O LORD; consider my GROANING' - the interior's first offering is not eloquence but a groan; it asks to be understood beneath the words.")
r.ch(280696,"directed morning prayer","affect","the psalmist","the groaning becomes directed prayer - the cry of the king lifted specifically to God","supplication","pray-to-you",IB,
     "v2: 'Give attention to the sound of my cry, my King and my God, for to you do I PRAY' - the interior shapes its distress into address, praying to a named king.")
r.ch(280702,"prepare and watch at dawn","volition","the psalmist","in the morning the self orders its prayer like a sacrifice and then watches - expectant discipline","expectant-waiting","prepare-and-watch",IB,
     "v3: 'in the morning I PREPARE a sacrifice for you and WATCH' - the operation is disciplined expectancy: the prayer laid out at dawn, then the alert waiting for an answer.")
r.ch(280730,"enter to bow in the fear of God","affect","the psalmist","borne by God's steadfast love, the self enters the house and bows toward the temple in reverent fear","reverent-worship","bow-in-fear",IB,
     "v7: 'through the abundance of your steadfast love I will ENTER your house; I will BOW DOWN toward your holy temple in the FEAR of you' - the interior approaches worship not on its own merit but on God's love, and the posture is fear.")
r.ch(280744,"longing for the straightened way","volition","the psalmist","the self asks to be led in righteousness and have the way made straight before it - the desire for a clear path amid foes","desire-for-guidance","make-way-straight",IB,
     "v8: 'Lead me in your righteousness because of my enemies; make your WAY STRAIGHT before me' - the interior longs not just for rescue but for a level, unambiguous path through the enemies' terrain.")
r.ch(280756,"enemies' grave-throated deceit","cognition","the enemies","their mouth has no truth, their throat an open grave, their tongue flatters - deceit is their inward reality","deceit","flattering-tongue",IB,
     "v9: 'there is no truth in their MOUTH... their throat is an open grave; they FLATTER with their TONGUE' - the enemies' interior is read as radically false; the smooth speech masks a death-dealing inside.")
r.ch(280669,"the enemies have rebelled","volition","the enemies","they have rebelled against God, so the self asks God to let them fall by their own counsels - revolt as their bent","rebellion","rebelled-against-God",IB,
     "v10: 'cast them out, for they have REBELLED against you' - beneath the deceit the deeper diagnosis: their interior is set against God himself; their treachery to the psalmist is really revolt against God.")
r.ch(280672,"the joy of those who take refuge","affect","those who take refuge","all who take refuge in God rejoice and ever sing for joy under his protection - shelter blossoming into song","refuge-joy","refuge-and-sing",IB,
     "v11: 'let all who TAKE REFUGE in you REJOICE; let them ever SING for joy' - over against the rebellious enemies, the interior of the sheltering is glad and vocal.")
r.ch(280677,"those who love your name exult","affect","those who love the name","those who love God's name exult in him - love of the name overflowing into exultation","name-love","love-and-exult",IB,
     "v11: 'and those who LOVE your NAME may EXULT in you' - read distinct from refuge-joy: this joy springs specifically from love of who God is (his name), not only from being sheltered.")

for sid,sense,src,d in [
 (280659,"consider (bin)",280660,"v1: 'CONSIDER my groaning' - the divine heed the groaning asks for."),
 (280699,"hear my voice",280702,"v3: 'O LORD, in the morning you HEAR my voice' - the hearing the watching waits on."),
 (280705,"delights not in wickedness",280669,"v4: 'you are not a God who DELIGHTS in wickedness' - God's character that dooms the rebels."),
 (280716,"hates evildoers",280669,"v5: 'you HATE all evildoers' - the divine aversion the enemies fall under."),
 (280723,"abhors the bloodthirsty",280669,"v6: 'the LORD ABHORS the bloodthirsty and deceitful man' - God's revulsion at the enemies' deceit."),
 (280737,"Lead me in righteousness",280744,"v8: 'LEAD me, O LORD, in your righteousness' - the guiding act the longing asks for."),
 (280682,"bless the righteous",280672,"v12: 'you BLESS the righteous, O LORD' - the favour crowning those who rejoice in refuge."),
 (280685,"cover with favour",280672,"v12: 'you COVER him with FAVOUR as with a shield' - the protection under which they sing."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (house/temple/grave/shield imagery or enemy-label); standalone.")
r.write()
