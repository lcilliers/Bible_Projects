#!/usr/bin/env python
"""Ps 2 (re-read) - nations rage vs the LORD's anointed. IB ops (rebellion side):
the raging tumult; the vain plotting; the rulers' conspiracy; the resolve to cast
off restraint. (Response side): the summons to be wise/warned; reverent service
with fear; rejoicing with trembling; the homage of the kiss; the beatitude of
refuge. God's laughter/wrath/decree/breaking = qualifier; holy-hill/decree/dash
imagery = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=2
r = Reading("Psa", 19, CH, note="Nations rage vs the anointed: rebellion (rage/plot/conspire/cast-off) vs submission (wise/serve/rejoice/kiss/refuge)")

r.ch(276492,"nations rage","affect","the nations","the peoples seethe in tumultuous uproar against the LORD and his anointed - collective fury","tumult","rage",IB,
     "v1: 'Why do the nations RAGE?' - the interior of the massed peoples is a churning uproar; emotion, not yet plan, the raw heat of revolt.")
r.ch(276494,"peoples plot in vain","cognition","the peoples","the raging becomes scheming - the peoples devise a plot, though it is empty/vain from the start","futile-scheming","plot-vain",IB,
     "v1: 'and the peoples PLOT in VAIN?' - the fury cools into design; distinct from rage, this is the cognitive step - a plan hatched, already stamped futile.")
r.ch(276523,"rulers take counsel together","cognition","the rulers","the kings and rulers conspire in concert against the LORD and his anointed - organised rebellion","conspiracy","take-counsel",IB,
     "v2: 'the rulers TAKE COUNSEL together, against the LORD and his Anointed' - the plot organises into a conspiracy of the powerful, deliberation turned to coordinated revolt.")
r.ch(305964,"cast off the cords","volition","the rebels","the resolve voiced: to burst the bonds and cast away the cords - a will to be free of all rule","throw-off-restraint","cast-off-bonds",IB,
     "v3: 'Let us BURST their bonds apart and CAST away their cords' - the interior motive laid bare: rebellion as the craving to be unbound, to have no yoke.")
r.ch(276498,"be wise, be warned","cognition","the kings","the turn: kings are summoned to prudence, to be warned - the interior called from revolt to sober sense","summons-to-prudence","be-wise",IB,
     "v10: 'Now therefore, O kings, be WISE; be WARNED, O rulers of the earth' - the psalm calls the rebellious interior to reconsider; wisdom offered as the off-ramp from ruin.")
r.ch(276502,"serve the LORD with fear","volition","the kings","the prudent response: to serve the LORD in fear - reverent submission replacing revolt","reverent-service","serve-in-fear",IB,
     "v11: 'SERVE the LORD with FEAR' - the interior reorients from casting-off to serving; fear here is the fitting posture of the once-rebellious before the king.")
r.ch(276505,"rejoice with trembling","affect","the kings","the paradoxical joy: rejoicing held together with trembling - gladness that keeps its awe","awed-joy","rejoice-trembling",IB,
     "v11: 'REJOICE with TREMBLING' - read distinct from serve: the interior is to hold joy and dread together, a submission that is glad but never casual.")
r.ch(276507,"kiss the Son","volition","the kings","the act of homage: to kiss the Son, submission embodied, lest wrath be kindled","homage","kiss-the-son",IB,
     "v12: 'KISS the Son, lest he be angry' - the interior submission takes outward form; the once-conspiring will now does homage.")
r.ch(276517,"take refuge in him","affect","all who trust","the beatitude closing the psalm: blessed are all who take refuge in him - trust as the true end of the summons","refuge-taking","take-refuge",IB,
     "v12: 'BLESSED are all who TAKE REFUGE in him' - the arc from revolt lands here: the interior that stops fighting and shelters in the king is pronounced happy.")

for sid,sense,src,d in [
 (305969,"laughs at them",276494,"v4: 'He who sits in the heavens LAUGHS' - God's derision that exposes the plot as vain."),
 (276529,"speaks in wrath",276523,"v5: 'Then he will SPEAK to them in his wrath' - the divine rebuke that terrifies the conspirators."),
 (276532,"terrifies them",276523,"v5: 'and TERRIFY them in his fury' - God's act breaking the conspiracy's nerve."),
 (276551,"Ask of me",276498,"v8: 'ASK of me, and I will make the nations your heritage' - the grant to the anointed the kings are warned to reckon with."),
 (276509,"lest he be angry",276507,"v12: 'lest he be ANGRY' - the wrath the homage of the kiss forestalls."),
 (276514,"wrath quickly kindled",276507,"v12: 'for his WRATH is quickly KINDLED' - the danger that makes submission urgent."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (holy-hill/decree/rod/dash imagery or label); standalone.")
r.write()
