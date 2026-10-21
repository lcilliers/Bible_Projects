"""M72 group D (H3027H, hand as power): forward list (#1998). Read-only against iba.db.

Researcher, chat 2026-10-12 (verbatim): "extend my guidance in that hand should not be read as the primary M-code, it
is also a qualifyer and it used figuratively. the main operator is likely to give or take away M-Code."

The hand word is a qualifier, so no D verse is read for M72. Each verse goes forward to the M-codes of its other words
(read when that cluster's strand reaches it). The give/take words are T3 operation words in cluster_strong, not
M-codes, so they are flagged separately. A verse with no other M-code has no strand that will bring it back
(triage order, GOVERNANCE.md §91: an act with no M-code is read by its act).

Input: m72-group-D-verses-v1-20261012.csv. Output: m72-group-D-forward-v1-20261012.csv.
Usage: python m72-group-D-forward-v1-20261012.py
"""
import csv, os, sqlite3
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
INP = os.path.join(HERE, 'm72-group-D-verses-v1-20261012.csv')
OUT = os.path.join(HERE, 'm72-group-D-forward-v1-20261012.csv')

c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
give_take = {s: g for s, g in c.execute("""SELECT s.strongNumber, s.stepGloss FROM strong s
    JOIN cluster_strong cs ON cs.strong = s.strongNumber AND cs.deleted = 0 AND cs.cluster_code = 'T3'
    WHERE s.stepGloss LIKE 'to give%' OR s.stepGloss LIKE 'to take%' OR s.stepGloss LIKE 'to deliver%'
       OR s.stepGloss LIKE 'to sell%'""")}

rows = []
for r in csv.DictReader(open(INP, encoding='utf-8-sig')):
    vid = c.execute('SELECT id FROM verse WHERE reference = ?', (r['reference'],)).fetchone()[0]
    gt = [f'{s} {give_take[s]} "{su}"' for s, su in c.execute(
        'SELECT strong, surface FROM verse_lexical WHERE verse_id = ? AND deleted = 0 ORDER BY position', (vid,)) if s in give_take]
    fwd = sorted({w.split(' ')[0] for w in r['other_mcodes'].split(' ; ') if w})
    status = 'forward' if fwd else ('no M-code; give/take word' if gt else 'no M-code; no give/take word')
    rows.append({'reference': r['reference'], 'status': status, 'forward_to': ' ; '.join(fwd),
                 'give_take_t3': ' ; '.join(gt), 'd_words': r['d_words'], 'other_mcodes': r['other_mcodes'],
                 'narrative_n': r['narrative_n'], 'narrative_refs': r['narrative_refs'], 'ot_pairing': r['ot_pairing'],
                 'in_m18_182': r['in_m18_182'], 'text': r['text']})
with open(OUT, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows), '->', os.path.basename(OUT))
print(Counter(r['status'] for r in rows))
print('forward with a give/take word too:', sum(1 for r in rows if r['status'] == 'forward' and r['give_take_t3']))
print('top forward codes:', Counter(x for r in rows for x in r['forward_to'].split(' ; ') if x).most_common(12))
