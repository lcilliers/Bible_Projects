#!/usr/bin/env python
"""Ps 141 (David) - evening prayer for inner restraint. IB ops: prayer as
incense-offering; asking a guard over the mouth; the heart kept from inclining
to evil company; welcoming a righteous man's rebuke as kindness; the eyes toward
God for refuge; the urgent call. God's keep/answer = qual; offering + snare +
death imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=141
r = Reading("Psa", 19, CH, note="Evening prayer for guarded speech and heart; welcoming correction; eyes toward God")

r.ch(273682,"call urgently","volition","the psalmist","an urgent appeal - 'make haste to me' - the interior pressing for a quick hearing","urgent-appeal","call-and-hasten",IB,
     "v1: 'I CALL upon you; make haste to me' - the prayer opens in urgency, the self reaching hard toward God.")
r.ch(273696,"prayer as incense","affect","the psalmist","the prayer is offered upward as incense, the raised hands as an evening sacrifice","offering-upward","prayer-as-incense",IB,
     "v2: 'let my PRAYER be counted as incense before you' - the interior act is framed as liturgy: supplication rising like smoke.")
r.ch(308114,"guard over the mouth","volition","the psalmist","asking that the speech be sentried - a watch set over mouth and lips","speech-restraint","guard-the-mouth",IB,
     "v3: 'Set a GUARD over my MOUTH, keep watch over the door of my lips' - the operation is requested self-restraint of speech, the interior policing its own exits.")
r.ch(273705,"heart not inclined to evil","volition","the psalmist","the heart is fenced against being drawn toward evil deeds and the company of evildoers","heart-guarding","incline-not-to-evil",IB,
     "v4: 'let not my HEART incline to any evil, to busy myself with wicked deeds' - the deeper guard: not the mouth only but the desire, refusing even to relish the delicacies of the wicked.")
r.ch(273722,"rebuke received as kindness","affect","the psalmist","a righteous man's blow/rebuke is welcomed as kindness, oil for the head - correction embraced","embrace-correction","rebuke-is-kindness",IB,
     "v5: 'Let a righteous man strike me - it is a KINDNESS; let him rebuke me - it is oil for my head' - the operation is rare: the interior wants to be corrected, receiving reproof as care.")
r.ch(273754,"eyes toward God for refuge","affect","the psalmist","the eyes are fixed on God, seeking refuge, the self declining to be left defenseless","refuge-seeking","eyes-toward-God",IB,
     "v8: 'my EYES are toward you, O God; in you I seek REFUGE' - the interior orients upward for shelter, entrusting the exposed self.")

for sid,sense,src,d in [
 (273684,"Give ear (azan)",273682,"v1: 'GIVE EAR to my voice when I call' - the divine hearing sought."),
 (273688,"call (qara)",273682,"v1: 'when I CALL to you' - the appeal God is asked to attend."),
 (308111,"Set (shith)",308114,"v3: 'SET a guard' - the requested divine act of guarding speech."),
 (308115,"keep watch (natsar)",308114,"v3: 'KEEP WATCH over the door of my lips' - the guarding petition."),
 (273721,"strike (halam)",273722,"v5: 'let a righteous man STRIKE me' - the correction received as kindness."),
 (273723,"rebuke (yakach)",273722,"v5: 'let him REBUKE me' - the reproof embraced as oil."),
 (273758,"Keep (shamar)",273754,"v9: 'KEEP me from the snares they have laid' - protective petition."),
 (273761,"laid (yaqosh)",273754,"v9: the snares evildoers have LAID - the danger God is asked to keep from."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (offering/snare/death imagery or label); standalone.")
r.write()
