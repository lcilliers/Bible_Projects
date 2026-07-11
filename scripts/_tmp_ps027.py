#!/usr/bin/env python
"""Ps 27 (the LORD my light; one thing I ask). IB ops: fearlessness because God
is light/stronghold; the heart unafraid though an army encamps; the one consuming
desire - to dwell and gaze on God's beauty; joyful sacrifice with shouts and song;
crying for a hearing; the heart's answer to 'seek my face'; confidence of being
taken up though parents forsake; believing to see God's goodness in the land of
the living; the self-exhortation to wait and take courage."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=27
r = Reading("Psa", 19, CH, note="Light+one-thing: fearlessness, heart unafraid, one consuming desire (gaze on beauty), joyful song, cry, heart seeks face, forsaken-by-parents received, believe-to-see-goodness, wait+courage")

r.ch(276198,"whom shall I fear","affect","the psalmist","with the LORD as light, salvation and stronghold, the self asks whom it should fear - fear dissolved by who God is","fearlessness","whom-shall-I-fear",IB,
     "v1: 'The LORD is my light and my salvation; whom shall I FEAR? The LORD is the STRONGHOLD of my life; of whom shall I be afraid?' - the operation is fear cancelled at its root: the interior finds no ground for dread once God is its light.")
r.ch(276251,"my heart shall not fear","affect","the psalmist","though an army encamps and war rises, the self's heart will not fear but stays confident - courage under siege","siege-courage","heart-not-fear",IB,
     "v3: 'Though an army encamp against me, my HEART shall not FEAR; though war arise against me, yet I will be CONFIDENT' - distinct from v1: this is fearlessness tested against a concrete, massed threat, and it holds.")
r.ch(276264,"one thing I ask - to gaze on his beauty","volition","the psalmist","the self reduces all its desire to one thing: to dwell in God's house and gaze on his beauty - longing consolidated onto a single object","consolidated-longing","one-thing-I-ask",IB,
     "v4: 'One thing have I ASKED... that I may dwell in the house of the LORD... to GAZE upon the BEAUTY of the LORD' - the operation is the gathering of all wants into one; the interior's many desires collapse into the desire to behold God.")
r.ch(276298,"offer sacrifice with shouts and song","affect","the psalmist","head lifted above enemies, the self offers sacrifices with shouts of joy and sings - praise erupting in anticipated victory","joyful-praise","shouts-and-song",IB,
     "v6: 'I will OFFER sacrifices with SHOUTS of joy; I will SING and make melody to the LORD' - the operation is exultant worship; the lifted head turns to loud, musical joy.")
r.ch(276303,"cry aloud for a hearing","affect","the psalmist","the self cries aloud and asks God to be gracious and answer - the appeal for attention","crying-out","cry-aloud",IB,
     "v7: 'HEAR, O LORD, when I CRY aloud; be gracious to me and answer me' - the operation is the lifted voice; from confidence the psalm turns to urgent petition.")
r.ch(276310,"my heart answers 'your face I seek'","affect","the psalmist","when God says 'seek my face', the self's heart answers, 'your face, LORD, do I seek' - the interior echoing the invitation","responsive-seeking","heart-seeks-face",IB,
     "v8: 'You have said, Seek my face. My HEART says to you, Your face, LORD, do I SEEK' - the operation is the heart's immediate, personal answer to God's summons; invitation met by desire.")
r.ch(306194,"though parents forsake, God takes me in","affect","the psalmist","even if father and mother forsake it, the self is confident the LORD will take it up - security beyond the closest human bonds","abandonment-answered","God-takes-me-in",IB,
     "v10: 'For my father and my mother have FORSAKEN me, but the LORD will take me IN' - the operation is trust that outlasts the failure of the deepest human belonging; the interior rests where even parents cannot be relied on.")
r.ch(276222,"I believe I shall see his goodness","affect","the psalmist","the self believes it will look upon the goodness of the LORD in the land of the living - a faith that steadies against despair","sustaining-faith","believe-to-see",IB,
     "v13: 'I BELIEVE that I shall look upon the GOODNESS of the LORD in the land of the living' - the operation is the faith that keeps the interior from collapse; belief that it will yet see good is what holds it.")
r.ch(276229,"wait for the LORD, take courage","volition","the psalmist","the self exhorts itself (and others) to wait for the LORD, be strong, and let the heart take courage - self-command to patient courage","self-exhortation","wait-and-courage",IB,
     "v14: 'WAIT for the LORD; be STRONG, and let your HEART take COURAGE; wait for the LORD!' - the operation is the interior addressing itself, commanding the patience and courage it needs to keep waiting.")

for sid,sense,src,d in [
 (276272,"gaze on his beauty",276264,"v4: 'to GAZE upon the beauty of the LORD' - the object the one consuming desire reaches for."),
 (276306,"answer me",276303,"v7: 'be gracious to me and ANSWER me' - the response the cry seeks."),
 (276208,"lead me on a level path",276229,"v11: 'TEACH me your way, O LORD, and LEAD me on a level path' - the guidance the waiting self asks for amid enemies."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (army/witnesses/altar/temple imagery, God-hide/turn/cast petition, or label); standalone.")
r.write()
