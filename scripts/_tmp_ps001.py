#!/usr/bin/env python
"""Ps 1 (corrected re-read, Book I remediation) - the two ways. IB ops: the
beatitude; the threefold refusal (walk->stand->sit in counsel->way->seat = a
deepening non-participation); delight in the law; day-and-night meditation. The
tree/chaff similes, the judgment scene, the wicked-labels = standalone; God's
knowing the way = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=1
r = Reading("Psa", 19, CH, note="The two ways: the blessed man's refusal + delight/meditation vs the wicked as chaff")

r.ch(275341,"blessed is the man","affect","the blessed man","the settled well-being of the man whose life is shaped by avoidance-of-evil and delight-in-law","beatitude","blessedness",IB,
     "v1: 'BLESSED is the man' - the psalter opens by weighing a whole life as happy; the interior state named is the flourishing that the following refusals and delight produce.")
r.ch(275344,"walks not in wicked counsel","volition","the blessed man","the first refusal: he does not even walk in step with the counsel of the wicked - declining the casual first association","refusal-1","walk-not",IB,
     "v1: 'WALKS not in the counsel of the wicked' - the mildest, most casual involvement (walking-alongside) is already refused; the interior sets its first boundary.")
r.ch(275348,"stands not in sinners' way","volition","the blessed man","the second, deeper refusal: he does not stop and stand in the way of sinners - declining to settle among them","refusal-2","stand-not",IB,
     "v1: 'nor STANDS in the way of sinners' - read distinct from v1a: standing is more settled than walking; the refusal deepens from passing-by to taking-a-position.")
r.ch(275352,"sits not in scoffers' seat","volition","the blessed man","the third, deepest refusal: he does not sit in the seat of scoffers - declining the settled fellowship of scorn","refusal-3","sit-not",IB,
     "v1: 'nor SITS in the seat of scoffers' - the climax of the descent refused: sitting is permanent belonging, and the company is now the most corrosive (scoffers). The triad walk->stand->sit maps the whole slide the interior declines.")
r.ch(275355,"delight in the law","affect","the blessed man","the positive counterpart to the refusals: his delight is fixed on the LORD's law - desire relocated to the good","delight","delight-in-law",IB,
     "v2: 'his DELIGHT is in the law of the LORD' - the interior does not merely avoid evil; it positively loves the law, the affection that fuels the meditation.")
r.ch(275359,"meditates day and night","cognition","the blessed man","he murmurs/ponders the law continually, day and night - delight become sustained attention","meditation","meditate-continually",IB,
     "v2: 'on his law he MEDITATES day and night' - the operation is unceasing rumination; the delight of v2a becomes a round-the-clock inner occupation that roots him like the tree.")

for sid,sense,src,d in [
 (275392,"knows the way of the righteous",275341,"v6: 'the LORD KNOWS the way of the righteous' - God's intimate acknowledgement that secures the blessed man; the ground of the beatitude."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (tree/chaff simile, judgment scene, or wicked/sinner/scoffer label); standalone.")
r.write()
