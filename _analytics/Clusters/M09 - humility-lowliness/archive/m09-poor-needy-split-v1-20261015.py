"""M09 group B (poor, needy) + H6035: split by who acts (#2148, researcher 2026-10-15).

Researcher, verbatim: "observing someone else as being poor triggers/or should trigger behaviour in a
IB, as it triggers divine behaviour.  this in itself should become a separate gloss group, and may be
a split off from group B."

Each of the 181 verses was read by Claude (verse text; passage where needed) and given ONE primary code:
  P  another person sees, speaks of, or acts toward the poor (care, give, withhold, oppress, despise,
     judge, partiality, pretext) -> the proposed new gloss group, human side (HIB, route B)
  G  God (or his anointed / the king as his agent where the verse sets God's act) sees, hears,
     delivers, raises, judges for the poor -> new gloss group, divine side (route A, 13.1)
  S  the poor/humble person's own state, standing, voice or act (means, self-declared, prays, gives,
     walks in integrity, perceived lack) -> stays in group B (or C for H6035)
  X  sense away from poverty here (weak, haggard, worthless) or a merism "rich and poor" (data)
A working aid (feedback_filters_are_working_aids_not_decision_items): many verses carry both sides;
the code is the side the verse puts first. Reads the marker CSV; writes the split CSV.
"""
import csv, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = {
 'Pro 14:20':'P','Pro 19:7':'P','Eze 18:12':'P','Luk 14:21':'P','Zep 2:3':'S','Psa 10:14':'G','Est 9:22':'P',
 'Isa 25:4':'G','Psa 41:1':'P','2Cor 8:9':'S','Luk 4:18':'G','Lev 14:21':'S','Isa 61:1':'G','Lev 25:35':'P',
 '2Sa 12:3':'S','Psa 22:26':'G','Psa 69:32':'S','Pro 28:15':'P','Mar 12:43':'S','Luk 6:20':'S','Luk 21:3':'S',
 'Joh 13:29':'P','Rev 3:17':'S','1Sa 18:23':'S','Pro 18:23':'S','Isa 32:7':'P','Psa 74:21':'S','Jer 20:13':'G',
 'Psa 34:2':'S','Pro 14:31':'P','Psa 149:4':'G','Exo 30:15':'S','Pro 22:16':'P','Pro 28:8':'P','Pro 10:15':'S',
 'Gal 4:9':'X','Ecc 4:14':'S','Lev 25:39':'P','Pro 22:7':'S','Luk 16:22':'S','Job 31:19':'P','Psa 9:18':'G',
 'Psa 72:4':'P','Pro 22:22':'P','Amo 2:7':'P','Psa 109:16':'P','Isa 14:30':'G','Job 20:19':'P','Amo 4:1':'P',
 'Luk 14:13':'P','Joh 12:6':'P','Mar 10:21':'P','Luk 18:22':'P','Luk 19:8':'P','Jam 2:3':'P','Luk 16:20':'S',
 'Deu 15:9':'P','Deu 15:11':'P','Judg 6:15':'S','Rut 3:10':'X','2Sa 12:1':'S','2Sa 13:4':'X','Psa 12:5':'G',
 'Psa 35:10':'G','Ecc 9:16':'P','Jer 5:4':'P','Amo 2:6':'P','Psa 86:1':'S','Pro 21:13':'P','Isa 41:17':'G',
 'Psa 107:41':'G','Psa 72:12':'P','Zep 3:12':'S','Psa 72:13':'P','2Sa 12:4':'P','Pro 14:21':'P','Pro 19:17':'P',
 'Pro 19:22':'S','Isa 11:4':'G','Psa 37:14':'P','Psa 82:4':'P','Psa 147:6':'G','Pro 29:7':'P','Lev 19:15':'P',
 'Psa 82:3':'P','Psa 109:31':'G','Pro 29:14':'P','Pro 31:9':'P','Jer 5:28':'P','Isa 29:19':'S','Rom 15:26':'P',
 'Exo 23:3':'P','Exo 23:6':'P','Job 29:16':'P','Psa 132:15':'G','Job 34:28':'G','Psa 10:17':'G','Psa 69:33':'G',
 'Pro 13:8':'S','Amo 8:4':'P','Deu 15:7':'P','Eze 16:49':'P','Pro 16:19':'S','Pro 10:4':'S','Pro 29:13':'S',
 '2Cor 6:10':'S','Amo 5:11':'P','Job 31:16':'P','Ecc 5:8':'P','Pro 19:1':'S','Pro 22:9':'P','Pro 28:6':'S',
 'Ecc 4:13':'S','Jer 22:16':'P','Deu 15:4':'S','Psa 112:9':'P','Pro 3:34':'G','Pro 28:27':'P','Jer 39:10':'P',
 'Psa 37:11':'S','Job 20:10':'P','Pro 17:5':'P','Mat 19:21':'P','Mar 14:7':'P','Mat 11:5':'G','Luk 7:22':'G',
 'Lev 25:25':'P','Lev 25:47':'P','1Sa 2:8':'G','Pro 28:11':'S','Psa 140:12':'G','Amo 5:12':'P','Job 34:19':'G',
 '2Cor 9:9':'P','2Sa 3:1':'X','Job 5:16':'S','Job 24:14':'P','Isa 10:2':'P','Psa 10:8':'P','Psa 10:12':'G',
 'Lev 27:8':'S','Psa 76:9':'G','Jam 2:5':'G','Exo 23:11':'P','Psa 34:10':'S','Mar 14:5':'P','Job 5:15':'G',
 'Job 30:25':'P','Mat 5:3':'S','Psa 40:17':'S','Deu 24:14':'P','Psa 70:5':'S','Psa 109:22':'S','Pro 30:14':'P',
 'Pro 31:20':'P','Isa 26:6':'S','Eze 22:29':'P','Psa 9:12':'G','Jer 2:34':'P','Amo 8:6':'P','Psa 25:9':'G',
 'Pro 13:23':'P','Job 24:4':'P','Pro 22:2':'S','Rev 13:16':'X','Mat 26:9':'P','Pro 13:7':'S','Pro 19:4':'P',
 'Psa 102:17':'G','Ecc 9:15':'P','Gal 2:10':'P','Mar 12:42':'S','Mat 26:11':'P','Joh 12:8':'P','Jam 2:2':'P',
 'Joh 12:5':'P','Num 12:3':'S','Psa 113:7':'G','Jam 2:6':'P','Pro 28:3':'P','Psa 49:2':'X'}
rows = list(csv.DictReader(open(os.path.join(HERE, 'm09-poor-needy-dimension-markers-v1-20261015.csv'), encoding='utf-8')))
missing = [r['reference'] for r in rows if r['reference'] not in CODE]
assert not missing, missing
assert len(CODE) == len(rows), (len(CODE), len(rows))
cnt = Counter(); c35 = Counter()
with open(os.path.join(HERE, 'm09-poor-needy-split-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'code', 'h6035', 'm09_words', 'other_mcodes', 'text'])
    for r in rows:
        k = CODE[r['reference']]; h = int('H6035' in r['m09_words'])
        cnt[k] += 1; c35[k] += h
        w.writerow([r['reference'], k, h, r['m09_words'], r['other_mcodes'], r['text']])
print('all', dict(cnt), 'of which H6035', dict(c35))
