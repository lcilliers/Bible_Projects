#!/usr/bin/env python
"""Ps 30 (thanksgiving for healing). IB ops: extolling God for being drawn up;
crying for help and being healed; summoning the saints to sing/thank; the
reflection that weeping tarries the night but joy comes with morning; the false
security of prosperity ('I shall never be moved'); the dismay when God hid his
face; crying and pleading for mercy from the pit; the mortality-argument (the
dead cannot praise); the received turn from mourning to dancing; the vow of
unceasing thanks. God's heal/restore = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=30
r = Reading("Psa", 19, CH, note="Healing-thanks: extol, cried+healed, summon saints, weeping->morning-joy, false security, dismay at hidden face, plead from pit, mortality-argument, mourning->dancing, unceasing thanks")

r.ch(276570,"extol you, for you drew me up","affect","the psalmist","the self extols God for drawing it up and not letting its foes rejoice over it - praise for being lifted from the depths","exalting-praise","extol-drawn-up",IB,
     "v1: 'I will EXTOL you, O LORD, for you have DRAWN me up and have not let my foes rejoice over me' - the operation lifts God high in praise, matching the lifting the self has received.")
r.ch(306206,"cried for help, and you healed me","affect","the psalmist","the self cried to God for help and was healed - the appeal answered with restoration","crying-answered","cried-and-healed",IB,
     "v2: 'O LORD my God, I CRIED to you for help, and you have HEALED me' - the operation states the whole pattern: the cry met by healing.")
r.ch(276607,"summon the saints to sing and thank","volition","the saints","the self calls God's saints to sing praises and give thanks to his holy name - drawing the community into thanksgiving","summoning-praise","saints-sing",IB,
     "v4: 'SING praises to the LORD, O you his SAINTS, and give thanks to his holy name' - the operation widens the private healing into a corporate summons to praise.")
r.ch(276619,"weeping tarries the night, joy at morning","cognition","the psalmist","the self reflects that God's anger is momentary but his favour lifelong; weeping may tarry for the night, but joy comes with the morning - a hard-won reading of grief's arc","grief's-arc","weeping-to-joy",IB,
     "v5: 'WEEPING may tarry for the night, but JOY comes with the morning' - the operation is a settled insight: the interior learns that sorrow is temporary and joy is the sure dawn.")
r.ch(276627,"in prosperity, 'I shall never be moved'","cognition","the psalmist","the self recalls that in its ease it presumed it would never be moved - the complacency of good times, now confessed","complacency","never-be-moved",IB,
     "v6: 'As for me, I said in my prosperity, I shall never be MOVED' - the operation names a past over-confidence: prosperity had lulled the interior into a false sense of permanence.")
r.ch(276638,"you hid your face; I was dismayed","state","the psalmist","when God hid his face, the self was dismayed - the collapse of the false security once favour was withdrawn","dismay","hidden-face-dismay",IB,
     "v7: 'you HID your face; I was DISMAYED' - the operation is the terror that exposed the complacency: the moment God withdrew, the interior fell apart.")
r.ch(276641,"cry and plead for mercy","affect","the psalmist","from the dismay the self cries to the LORD and pleads for mercy - the appeal from the edge of the pit","pleading","cry-and-plead",IB,
     "v8: 'To you, O LORD, I CRY, and to the Lord I PLEAD for mercy' - the operation is the turn from dismay to petition; the shaken interior lifts a cry.")
r.ch(276651,"will the dust praise you?","cognition","the psalmist","the self argues its case: what profit in its death? can the dust praise God or tell his faithfulness? - motivating rescue by love of praising","mortality-argument","dust-cannot-praise",IB,
     "v9: 'What PROFIT is there in my death... Will the DUST PRAISE you? Will it TELL of your faithfulness?' - the operation pleads for life by its desire to keep praising; the interior wants to remain among the worshippers.")
r.ch(276583,"you turned my mourning into dancing","affect","the psalmist","God turned the self's mourning into dancing, loosed its sackcloth and clothed it with gladness - the received reversal","transformation","mourning-to-dancing",IB,
     "v11: 'You have TURNED for me my MOURNING into DANCING; you have loosed my sackcloth and clothed me with GLADNESS' - the operation is the felt reversal: the interior is re-dressed from grief to joy.")
r.ch(276591,"my glory shall sing, not be silent","volition","the psalmist","the self vows that its glory will sing God's praise and not be silent; it will give thanks forever - a pledge of unending praise","unceasing-praise","not-be-silent",IB,
     "v12: 'that my glory may SING your praise and not be SILENT. O LORD my God, I will give thanks to you forever' - the operation binds the interior to perpetual praise; the rescued self will not fall silent.")

for sid,sense,src,d in [
 (306207,"you healed me",306206,"v2: 'and you have HEALED me' - the restoration the cry received."),
 (276600,"brought up my soul from Sheol",276570,"v3: 'you have BROUGHT UP my soul from Sheol' - the deliverance the extolling celebrates."),
 (276617,"his favour is for a lifetime",276619,"v5: 'his FAVOUR is for a lifetime' - the lasting grace behind the morning-joy insight."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (Sheol/pit/sackcloth imagery or label); standalone.")
r.write()
