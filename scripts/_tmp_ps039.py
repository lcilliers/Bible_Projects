#!/usr/bin/env python
"""Ps 39 (the transience of life; the disciplined tongue). IB ops: guarding the
tongue (muzzling the mouth) before the wicked; the failed silence (distress
worsening); the heart burning until words break out; asking to know one's own
transience; reckoning man as a mere breath/shadow; hope fixed on God alone amid
transience; silent submission to God's dealing ('it is you who have done it');
crying with tears as a fleeting sojourner; the poignant plea for God to look away
so the self may smile before it dies."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=39
r = Reading("Psa", 19, CH, note="Transience+disciplined tongue: guard-tongue, failed-silence, heart-burns, know-my-end, man-a-breath, hope-in-you-alone, silent-submission, cry-as-sojourner, look-away")

r.ch(278017,"guard my ways, muzzle my mouth","volition","the psalmist","the self resolves to guard its ways so as not to sin with the tongue, keeping its mouth with a muzzle while the wicked are near - deliberate speech-restraint","tongue-guarding","muzzle-my-mouth",IB,
     "v1: 'I will GUARD my ways, that I may not sin with my tongue; I will guard my mouth with a MUZZLE, so long as the wicked are in my presence' - the operation is a self-imposed silence, the interior clamping down on speech to avoid sin.")
r.ch(278067,"I was mute, and my distress grew worse","state","the psalmist","the self was mute and silent, held its peace to no avail, and its distress only grew worse - the failure of forced silence","silence's-failure","mute-distress-worse",IB,
     "v2: 'I was MUTE and SILENT; I held my peace to no avail, and my DISTRESS grew WORSE' - the operation is the backfiring of restraint: bottling the words did not ease the interior but inflamed it.")
r.ch(278073,"my heart grew hot, the fire burned","state","the psalmist","the self's heart became hot within it; as it mused the fire burned, until it spoke - inner pressure building to speech","building-pressure","heart-grew-hot",IB,
     "v3: 'My HEART became HOT within me. As I MUSED, the fire BURNED; then I spoke with my tongue' - the operation is the heat of suppressed thought; the interior's fire builds under the muzzle until it must break out.")
r.ch(278083,"make me know my end","volition","the psalmist","the self asks God to make it know its end and the measure of its days, to know how fleeting it is - a request to grasp its own mortality","mortality-awareness","know-my-end",IB,
     "v4: 'O LORD, make me KNOW my END and what is the measure of my days; let me know how FLEETING I am!' - the operation is a strange petition: the interior asks to feel the shortness of its life, wanting the truth of its transience.")
r.ch(278104,"man is a mere breath, a shadow","cognition","the psalmist","the self reckons its days a few handbreadths, all mankind a mere breath, a man going about as a shadow, heaping up in turmoil for nothing - the meditation on human vanity","transience-reckoning","man-a-breath",IB,
     "v5-6: 'Surely all mankind stands as a mere BREATH! Surely a man goes about as a SHADOW!' - the operation is the settled insight of vanity: the interior sees life as vapour and busyness as futile turmoil.")
r.ch(278120,"for what do I wait? my hope is in you","affect","the psalmist","against the vanity, the self asks for what it waits and answers that its hope is in the Lord alone - hope narrowed to God","narrowed-hope","hope-in-you",IB,
     "v7: 'And now, O Lord, for what do I WAIT? My HOPE is in you' - the operation is the collapse of every other hope into one: if all is breath, the interior fastens its whole expectancy on God.")
r.ch(278132,"I am mute, for you have done it","volition","the psalmist","the self is mute and does not open its mouth, because it is God who has done it - silent submission to God's dealing","submissive-silence","mute-you-did-it",IB,
     "v9: 'I am MUTE; I do not open my mouth, for it is you who have DONE it' - distinct from v1's tongue-guard: this silence is submission, the interior accepting the affliction as God's own act and not protesting.")
r.ch(278051,"hold not your peace at my tears","affect","the psalmist","the self asks God to hear its prayer and cry, not to be silent at its tears, for it is a sojourner and guest with him - crying as a passing guest","sojourner-tears","cry-as-sojourner",IB,
     "v12: 'Hear my prayer... hold not your peace at my TEARS! For I am a SOJOURNER with you, a guest' - the operation is a plea from transience: the interior weeps as a passing guest, asking the eternal host not to stay silent.")
r.ch(278059,"look away, that I may smile again","affect","the psalmist","the self asks God to look away from it, that it may smile again before it departs and is no more - a startling plea for the gaze of judgment to relent","plea-for-respite","look-away",IB,
     "v13: 'LOOK AWAY from me, that I may SMILE again, before I depart and am no more!' - the operation is a poignant, almost desperate request: the interior asks the scrutinising God to ease off so it can know one last gladness before death.")

for sid,sense,src,d in [
 (278122,"my hope is in you",278120,"v7: 'My HOPE is in you' - the God the narrowed hope rests on (restated as its object)."),
 (278047,"Hear my prayer",278051,"v12: 'HEAR my prayer, O LORD, and give ear to my cry' - the attention the sojourner's tears plead for."),
 (278034,"you discipline man for sin",278132,"v11: 'When you DISCIPLINE a man with rebukes for sin, you consume like a moth what is dear to him' - the divine dealing the self submits to in silence."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (breath/shadow/moth imagery, handbreadth-days, or God's-discipline label); standalone.")
r.write()
