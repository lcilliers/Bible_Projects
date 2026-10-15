"""M08 pride anchor cross-check (#2156): one decision for every passage that still tells no claim after
update 143 and the follow-up tellings (m08-pride-anchor-scan-final-v1-20261015.csv). Each was read by
Claude (the list was read in full before and after the weave). Decisions:
  quote or pointer   the passage quotes verses with the pride word, or points to another section; nothing
                     beyond the verses is said about pride, so no claim is needed
  other concept      the passage uses a pride-group word, but the statement it makes beyond the verses is
                     about another concept (named); it is reconciled when that concept's strand touches it
                     (rule 77 as amended, #2154: concept-scoped)
Writes m08-pride-anchor-classify-v1-20261015.csv.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
QUOTE = {('02', 'After death', '5'), ('07', 'Flesh in the New Testament', '13'), ('08', 'Conscience', '2'),
         ('08', 'The bosom', '5'), ('10.0', '(opening)', '2'), ('10.1', 'When delight is only', '3'),
         ('10.1', 'When delight is only', '25'), ('10.2', '(opening)', '20'), ('10.2', 'Perplexity', '5'),
         ('10.14', 'What it is set against', '1'), ('10.14', 'What it is set against', '2'),
         ('10.14', 'Being humbled by God', '5'), ('10.14', 'The proud brought low', '1'), ('10.14', 'The humble', '5'),
         ('10.14', 'Connections', '6'), ('10.14', 'Connections', '8'), ('10.15', 'The words', '4'),
         ('10.15', 'Connections', '1'), ('10.15', 'Connections', '3'), ('10.15', 'Connections', '4'),
         ('10.15', 'Connections', '5'), ('10.15', 'Connections', '6'), ('10.15', 'Connections', '7'),
         ('12', 'The heart deceives', '2'), ('12', 'Pride and the lifted-up', '2'), ('12', 'Pride and the lifted-up', '3'),
         ('12', 'Pride and the lifted-up', '4'), ('13.1', '(opening)', '1'), ('14', 'Thoughts taken captive', '4')}
CONCEPT = {'02': 'the nose and face word (life, anger)', '04': 'the will and the heart', '06': 'the spirit (anger, stirring)',
           '07': 'flesh', '10.1': 'delight', '10.2': 'hearing and willing', '10.4': 'thinking', '10.5': 'speech before words',
           '10.6': 'desire, envy, jealousy', '10.7': 'choosing, planning, willing', '10.9': 'relating to God (fear, rule)',
           '10.10': 'relating to others (care, anger, plotting, friends)', '10.11': 'hiding', '10.12': 'fear',
           '10.13': 'anger', '10.14': 'humility', '11': 'thresholds, sequence, change of character, authority',
           '13.1': 'God\'s delight and jealousy', '13.2': 'angels'}
rows = [r for r in csv.DictReader(open(os.path.join(HERE, 'm08-pride-anchor-scan-final-v1-20261015.csv'), encoding='utf-8'))
        if not r['claims_told']]
out = []
for r in rows:
    q = any(r['chapter'] == c and r['section'].startswith(s) and r['ordinal'] == o for c, s, o in QUOTE)
    d = 'quote or pointer' if q else 'other concept: ' + CONCEPT[r['chapter']]
    out.append([r['chapter'], r['section'], r['ordinal'], r['words'], d, r['text'][:240].replace('\n', ' ')])
with open(os.path.join(HERE, 'm08-pride-anchor-classify-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['chapter', 'section', 'ordinal', 'words', 'decision', 'text_start']); w.writerows(out)
print(len(out), Counter(x[4].split(':')[0] for x in out))
print(Counter(x[0] for x in out if x[4].startswith('other')).most_common())
