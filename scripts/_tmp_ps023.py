#!/usr/bin/env python
"""Ps 23 (the shepherd). IB ops: the contentment of the shepherded (I shall not
want); the soul restored; fearing no evil in the death-valley; comforted by rod
and staff; the confidence that goodness and mercy pursue; the settled hope of
dwelling with God forever. The green pastures/table/oil/cup = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=23
r = Reading("Psa", 19, CH, note="The shepherd: contentment, restored soul, fearlessness in the valley, comfort, pursued by goodness, dwelling with God")

r.ch(275809,"I shall not want","affect","the psalmist","because the LORD shepherds it, the self lacks nothing - a contentment that rests in being led and fed","contentment","shall-not-want",IB,
     "v1: 'The LORD is my shepherd; I shall not WANT' - the operation is settled sufficiency: the interior, under a shepherd, is freed from craving and anxiety about need.")
r.ch(275819,"he restores my soul","state","the psalmist","the shepherd restores/revives the self's soul, leading it in right paths - inner renewal received","restoration","soul-restored",IB,
     "v3: 'He RESTORES my SOUL; he leads me in paths of righteousness' - the operation is the soul brought back, revived after depletion, the interior renewed by the shepherd's care.")
r.ch(275829,"I will fear no evil","affect","the psalmist","even walking through the valley of the shadow of death, the self fears no evil, for God is with it - fear dissolved by presence","fearlessness","fear-no-evil",IB,
     "v4: 'Even though I WALK through the valley of the shadow of death, I will FEAR no EVIL, for you are with me' - the operation is fear refused; the darkest passage is faced without dread because of the felt companionship.")
r.ch(275838,"your rod and staff comfort me","affect","the psalmist","the shepherd's rod and staff comfort the self - a felt consolation from God's guiding, protecting nearness","consolation","comforted",IB,
     "v4: 'your rod and your staff, they COMFORT me' - the operation is the interior soothed; the very instruments of guidance and defence become a source of comfort.")
r.ch(275854,"goodness and mercy pursue me","affect","the psalmist","the self is confident that goodness and mercy will pursue it all its days - assurance of being chased by good, not evil","assurance","goodness-follows",IB,
     "v6: 'Surely GOODNESS and MERCY shall FOLLOW me all the days of my life' - the operation reverses the usual: instead of enemies pursuing, the interior trusts that God's good is on its trail.")
r.ch(275858,"I shall dwell with God forever","affect","the psalmist","the self will dwell in the house of the LORD forever - a settled, permanent hope of God's presence","settled-hope","dwell-forever",IB,
     "v6: 'and I shall DWELL in the house of the LORD forever' - the operation lands the psalm in a permanent belonging: the interior's final rest is unbroken nearness to God.")

for sid,sense,src,d in [
 (275807,"the LORD is my shepherd",275809,"v1: 'The LORD is my SHEPHERD' - the shepherding that grounds the contentment."),
 (275818,"restores/leads",275819,"v3: 'he leads me in paths of righteousness for his name's sake' - the shepherd's guiding that restores the soul."),
 (275845,"you anoint my head",275838,"v5: 'you ANOINT my head with oil; my cup overflows' - the lavish care that comforts."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (pastures/waters/table/oil/cup imagery or label); standalone.")
r.write()
