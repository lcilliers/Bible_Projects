#!/usr/bin/env python
"""Ps 33 (praise the LORD - word, creation, providence). vv4-19 (God's word/
works/counsel/providence) = qualifier/standalone. IB ops: the righteous shouting
for joy (praise befits the upright); the skilful new song; the reverent fear God's
eye rests on; the hope in his steadfast love; the soul that waits for the LORD;
the heart glad in trusting his holy name; the community's hope grounding the plea."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=33
r = Reading("Psa", 19, CH, note="Praise+providence: righteous shout for joy, skilful new song, the fear + hope God's eye rests on, soul waits, heart glad in trust, community's hope (word/works/counsel = qual/standalone)")

r.ch(276977,"shout for joy, you righteous","affect","the righteous","the self calls the righteous to shout for joy in the LORD, for praise befits the upright - joy as the fitting act of the righteous","fitting-joy","shout-for-joy",IB,
     "v1: 'Shout for JOY in the LORD, O you righteous! Praise befits the UPRIGHT' - the operation names joyful praise as the proper expression of an upright interior.")
r.ch(277082,"sing a new song, skilfully","affect","the worshippers","the self summons a new song, played skilfully on strings with loud shouts - fresh, crafted praise","fresh-praise","new-song-skilful",IB,
     "v3: 'SING to him a NEW song; play SKILFULLY on the strings, with loud shouts' - the operation is inventive, well-made praise; the interior brings craft and freshness, not rote.")
r.ch(277043,"the fear God's eye rests on","affect","those who fear him","the eye of the LORD is on those who fear him - reverent fear as the posture God watches over","reverent-fear","eye-on-the-fearing",IB,
     "v18: 'Behold, the EYE of the LORD is on those who FEAR him' - the operation names the fearing interior as the one God keeps in view; reverence draws his watchful care.")
r.ch(277045,"hope in his steadfast love","affect","those who hope","the LORD's eye is on those who hope in his steadfast love - hope leaning on covenant love as the ground of God's regard","hope","hope-in-chesed",IB,
     "v18: 'on those who HOPE in his steadfast love' - distinct from fear: this is the forward-leaning trust in God's love, the expectancy that draws his eye alongside reverence.")
r.ch(277062,"our soul waits for the LORD","affect","the community","the self's soul waits for the LORD, its help and shield - patient, dependent expectancy","waiting","soul-waits",IB,
     "v20: 'Our SOUL WAITS for the LORD; he is our help and our shield' - the operation is the interior's patient reliance; the soul holds still and looks to God as its defence.")
r.ch(277070,"our heart is glad in his name","affect","the community","the self's heart is glad in God because it trusts in his holy name - gladness flowing from trust","trusting-gladness","heart-glad-in-trust",IB,
     "v21: 'For our HEART is GLAD in him, because we TRUST in his holy name' - the operation ties gladness to trust: the interior rejoices precisely because it relies on who God is.")
r.ch(277080,"even as we hope in you","affect","the community","the self asks God's steadfast love to be upon it, even as it hopes in him - present hope as the ground of the closing plea","present-hope","as-we-hope",IB,
     "v22: 'Let your steadfast love, O LORD, be upon us, even as we HOPE in you' - distinct from v18's general hopers: this is the community's own present hope, offered as the reason for the plea.")

for sid,sense,src,d in [
 (277049,"deliver their soul from death",277043,"v19: 'that he may DELIVER their soul from death and keep them alive in famine' - the rescue God's eye-on-the-fearing secures."),
 (277066,"our help and our shield",277062,"v20: 'he is our HELP and our SHIELD' - the God the waiting soul looks to."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (God's word/creation/counsel/providence, army-no-salvation, or attribute label); standalone.")
r.write()
