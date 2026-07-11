#!/usr/bin/env python
"""Ps 4 (evening psalm). IB ops: calling on God who gives relief in distress; the
men's love of vanity and lies; the assurance that God sets apart the godly; anger
disciplined ('be angry and sin not'); the heart's silent self-examination on the
bed; trust in the LORD; God-given joy exceeding harvest-gladness; the many who
crave 'some good'; peaceful sleep in safety. God's hear/relieve/lift-face =
qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=4
r = Reading("Psa", 19, CH, note="Evening psalm: call, disciplined anger, heart-searching, trust, God-given joy, peaceful sleep")

r.ch(279419,"call on the God of righteousness","affect","the psalmist","the self calls to the God who has given relief in past distress - appeal grounded in remembered rescue","appeal","call-for-relief",IB,
     "v1: 'Answer me when I CALL, O God of my righteousness! You have given me relief in distress' - the interior appeals on the basis of a God who has widened the narrow place before.")
r.ch(279433,"men love vanity, seek lies","affect","the men","the sons of men turn honour to shame because they love empty things and chase after lies - misdirected desire","misdirected-love","love-vanity",IB,
     "v2: 'How long will you love VAIN words and seek after LIES?' - the operation diagnosed in the opponents is a disordered affection: the interior fastened on emptiness.")
r.ch(279438,"know the LORD sets apart the godly","cognition","the psalmist","settled knowledge that God has set apart the godly for himself and hears their call - assurance against the slander","assurance","know-set-apart",IB,
     "v3: 'KNOW that the LORD has set apart the godly for himself; the LORD hears when I call' - against the men who shame him, the interior rests on being God's own.")
r.ch(279448,"be angry and do not sin","volition","the hearer","anger is permitted but fenced - to feel it without letting it spill into sin, the passion disciplined","disciplined-anger","angry-not-sin",IB,
     "v4: 'Be ANGRY, and do not SIN' - the operation is the governing of a strong emotion: not its suppression but its restraint short of wrongdoing.")
r.ch(279450,"ponder in your heart, be silent","cognition","the hearer","the counsel to search the heart on the bed and be still - reflective interior quiet","self-examination","ponder-and-still",IB,
     "v4: 'PONDER in your own hearts on your beds, and be SILENT' - the interior is sent inward and hushed; night-time self-searching as the cure for restless anger.")
r.ch(279459,"trust in the LORD","affect","the hearer","after right sacrifices, the call to put trust in the LORD - reliance placed where offerings point","entrustment","put-trust",IB,
     "v5: 'Offer right sacrifices, and put your TRUST in the LORD' - the interior is directed past ritual to reliance; the sacrifices mean nothing without the trust.")
r.ch(305977,"the many who crave 'some good'","volition","the many","the crowd's restless question - who will show us any good? - a diffuse craving for benefit","restless-craving","who-shows-good",IB,
     "v6: 'There are many who say, Who will show us some GOOD?' - the interior of the many is a vague, unanchored hunger for good, contrasted with the psalmist's located joy.")
r.ch(279462,"joy greater than harvest","affect","the psalmist","God has put more joy in the heart than the abundance of grain and wine gives - inner gladness surpassing plenty","surpassing-joy","joy-over-harvest",IB,
     "v7: 'You have put more JOY in my HEART than they have when their grain and wine abound' - the operation is a gladness located in God that outweighs the best material happiness.")
r.ch(279472,"in peace lie down and sleep","state","the psalmist","the self lies down and sleeps in peace, God alone making it dwell in safety - rest as trust's fruit","peaceful-rest","sleep-in-safety",IB,
     "v8: 'In PEACE I will both lie down and SLEEP; for you alone, O LORD, make me dwell in safety' - the evening closes as Ps 3's morning did: sleep is the body's confession of security in God.")

for sid,sense,src,d in [
 (279422,"gave relief in distress",279419,"v1: 'you have GIVEN me RELIEF in distress' - the past rescue the call leans on."),
 (279425,"hear my prayer",279419,"v1: 'be gracious to me and HEAR my prayer' - the divine hearing sought."),
 (279440,"set apart the godly",279438,"v3: 'the LORD has SET APART the godly for himself' - the election the assurance rests on."),
 (279443,"hears when I call",279438,"v3: 'the LORD HEARS when I call to him' - God's attentiveness undergirding the assurance."),
 (305978,"lift the light of your face",279462,"v6: 'LIFT UP the light of your face upon us' - the blessing whose granting is the source of the surpassing joy."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (sacrifice/face/light imagery or label); standalone.")
r.write()
