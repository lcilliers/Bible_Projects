#!/usr/bin/env python
"""Ps 40 (thanksgiving + plea; 92 spans). IB ops: patient waiting, heard; the new
song of praise (others see, fear, trust); the blessedness of trusting God not the
proud; proclaiming God's countless wondrous deeds; delighting to do God's will
(the law within the heart); telling the glad news of deliverance, lips
unrestrained; not hiding God's righteousness in the heart (open testimony); being
overwhelmed by iniquities till the heart fails; those who seek God rejoicing; the
poor and needy self confident God takes thought for it. God's draw-from-pit/
deliver = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=40
r = Reading("Psa", 19, CH, note="Thanks+plea: waited-heard, new-song, blessed-trust, proclaim-wondrous, delight-to-do-will, glad-news-of-deliverance, not-hidden-in-heart, iniquities-overwhelm/heart-fails, seekers-rejoice, poor-and-needy")

r.ch(278212,"I waited patiently, he heard my cry","affect","the psalmist","the self waited patiently for the LORD, who inclined to it and heard its cry - patient waiting rewarded","patient-waiting","waited-and-heard",IB,
     "v1: 'I WAITED PATIENTLY for the LORD; he inclined to me and heard my CRY' - the operation is a sustained, quiet waiting that God bent down to answer; patience met by attention.")
r.ch(278319,"a new song, that many may trust","affect","the psalmist","God put a new song of praise in the self's mouth; many will see, fear, and put their trust in the LORD - praise that propagates trust","contagious-praise","new-song",IB,
     "v3: 'He put a NEW SONG in my mouth, a song of praise to our God. Many will SEE and FEAR, and put their TRUST in the LORD' - the operation is testimony that spreads: the interior's rescued song moves others to reverent trust.")
r.ch(278326,"blessed is the man who trusts the LORD, not the proud","affect","the trusting man","blessed is the man who makes the LORD his trust and does not turn to the proud or to liars - trust rightly placed","rightly-placed-trust","blessed-who-trusts",IB,
     "v4: 'BLESSED is the man who makes the LORD his TRUST, who does not turn to the PROUD, to those who go astray after a lie' - the operation weighs as happy the interior that leans on God rather than on proud liars.")
r.ch(278347,"I will proclaim your countless wondrous deeds","volition","the psalmist","the self proclaims and tells God's wondrous deeds and thoughts, too many to number - praise for the innumerable works","proclaiming-wonders","proclaim-wondrous",IB,
     "v5: 'your WONDROUS deeds and your THOUGHTS toward us; none can compare... I will PROCLAIM and tell of them' - the operation is overflowing testimony; the interior cannot keep silent about deeds beyond counting.")
r.ch(278372,"I delight to do your will, your law within my heart","affect","the psalmist","the self delights to do God's will, its law within its heart - obedience become desire","delighted-obedience","delight-to-do-will",IB,
     "v8: 'I DELIGHT to do your WILL, O my God; your law is within my HEART' - the operation is obedience felt as joy: the law is not an external weight but an internalised delight.")
r.ch(278380,"I told the glad news, I did not restrain my lips","volition","the psalmist","the self has told the glad news of deliverance in the great congregation and has not restrained its lips - unrestrained public witness","unrestrained-witness","glad-news",IB,
     "v9: 'I have told the GLAD NEWS of deliverance in the great congregation; behold, I have not RESTRAINED my lips' - the operation is a witness that refuses to hold back; the interior publishes God's rescue openly.")
r.ch(278221,"I have not hidden your righteousness in my heart","volition","the psalmist","the self has not hidden God's deliverance within its heart but has spoken of his faithfulness and steadfast love - refusing to keep the good news private","open-heartedness","not-hidden-in-heart",IB,
     "v10: 'I have NOT HIDDEN your deliverance within my HEART... I have not CONCEALED your steadfast love' - the operation is the deliberate opposite of secrecy: the interior will not lock God's goodness inside but broadcasts it.")
r.ch(278245,"iniquities overwhelm me, my heart fails","state","the psalmist","evils have encompassed the self beyond number; its iniquities have overtaken it till it cannot see, more than the hairs of its head, so its heart fails - being swamped by guilt","swamped-by-guilt","iniquities-overwhelm",IB,
     "v12: 'my INIQUITIES have overtaken me, till I cannot see; they are more than the hairs of my head; my HEART FAILS me' - the operation is inundation: the interior is buried under uncountable guilt and its courage gives out.")
r.ch(278285,"may all who seek you rejoice","affect","those who seek","the self prays that all who seek God may rejoice and be glad, and those who love his salvation say 'Great is the LORD' - seeking that ends in joyful praise","joyful-seeking","seekers-rejoice",IB,
     "v16: 'may all who SEEK you REJOICE and be GLAD in you; may those who LOVE your salvation say continually, Great is the LORD!' - the operation widens the self's rescue into a prayer that all seekers share its joy.")
r.ch(278295,"I am poor and needy, but the Lord takes thought for me","affect","the psalmist","the self is poor and needy, but the Lord takes thought for it; he is its help and deliverer - lowliness confident of God's attention","confident-lowliness","poor-but-thought-of",IB,
     "v17: 'As for me, I am POOR and NEEDY, but the Lord takes THOUGHT for me. You are my help and my deliverer' - the operation holds together weakness and confidence: the interior owns its poverty yet rests in being remembered by God.")

for sid,sense,src,d in [
 (278217,"he heard my cry",278212,"v1: 'he inclined to me and HEARD my cry' - the answer the patient waiting received."),
 (278303,"he drew me up from the pit",278319,"v2: 'He DREW me up from the pit of destruction... and set my feet upon a rock' - the deliverance the new song celebrates."),
 (278262,"deliver me",278295,"v13: 'Be pleased, O LORD, to DELIVER me!' - the rescue the poor-and-needy self still asks for."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (pit/rock/bog imagery, sacrifice-not-required, scroll/book, enemies'-shame, or God's-act label); standalone.")
r.write()
