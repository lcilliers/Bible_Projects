"""M18 group B remaining 94 (#1993, item F), 2026-10-11: claim register v45 -> v46, narrative index rows,
OT-97 (Hos 8:8 added under M30), triage CSV rows for the 15 no-carrier verses (decision -> placed).
Run once. Writes files; no DB access."""
import csv, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))
OTR = os.path.normpath(os.path.join(HERE, '..', '..', 'cross-cluster-web', 'open-threads-register.md'))

SEC = '''## Strand updates — desire (M18), group B: the 94 remaining bucket-1 verses, read by role (2026-10-11, #1993 item F)

**Researcher, verbatim:** *"you will not blanketly read every verse, but will optimise the reading by first assessing the status of the M18 M-code, if it is supportive, for another cluster's reading then the reading is marked forward for when that cluster is read, else if the M-code is central to the verse, then read in in deapth and in context."* Then: *"read the 15 now as recommended, then proceed with the weave"*.

**Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Triage: 24 read in depth, 43 marked forward (OT-97), 15 whose act carries no M-code read by their acts and placed, 12 data only. Records: `../../Clusters/M18 - desire-longing/m18-group-B-remaining-role-reading-v2-20261011.md`, `m18-group-B-no-carrier-reading-v1-20261011.md`, `m18-group-B-remaining-role-triage-v1-20261011.csv`.

**Original claims changed:** none. **Correction in the record:** the reading v1 said Isa 58:13 uses one word twice with opposite objects; "pleasure" is *ḥēpheṣ* and the Sabbath "delight" is *ʿōneg*. Corrected in reading v2; nothing woven from it.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.1 (v19) | *On God's word*: beside meditating (Psa 1:1–2), under pressure (Psa 119:23–24, 92–93, 143), joined to doing (Psa 40:6–8); *In a person*: Psa 16:2–4; measure table +12 rows | Added; I read marked |
| 10.5 (v19) | the vow and the mouth (Ecc 5:2–7) | Added; I read marked |
| 10.6 (v19) | the good eye (Pro 22:9; 23:6); life itself pleasant (Ecc 11:7–9); concern that stops at death (Job 21:19–21); coveting as a fair offer (1Ki 21:2–4); passions in prayer (Jam 4:2–3) | Added; I read marked |
| 10.7 (v24) | Eli yielding (1Sa 3:17–18); Balaam turning (Num 24:1–2); *Whose measure*: 1Sa 14:36–40, Est 3:9–11 and 8:8; *Choosing together*: 1Ch 13:2–4; *A choice that is honoured*: Gen 20:15–16; *Fear and choosing*: 2Ki 10:4–6 | Added |
| 10.9 (v19) | *Waiting, and pleading*: Psa 90:13–17 | Added |
| 10.10 (v21) | *Loyalty and honour*: 2Sa 3:36–37; 2Sa 19:18–30; Gen 19:7–9 | Added; I read marked |
| 10.11 (v5) | *Hiding what I hold*: 1Sa 11:9–11 | Added; I read marked |
| 13.1 (v19) | *Purposing*: his purpose spoken and carried out by another (Isa 44:26–28; 46:9–11; 48:14, referent crux recorded); *Delight*: not from those who put something else in the place of hearing (1Sa 15:21–22; Mal 1:6–10; Ecc 5:4), Psa 135:5–6, Balaam (Num 24:1), delight at creation (Pro 8:22, 29–31) | Added; I read marked |
| Ch 11 (v27) | §4 *Delight*: *ḥēpheṣ* as purpose and as what a man cares for; new face *Good, said of the eye*; *Whose eyes, and whose delight*: "what seems good to you" across six settings | Added |

**Quote check:** 86 inserted quotations checked against the ESV in iba.db, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v45-20261009.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v45)') == 1
t = t.replace('checked against the inner-seat reading (v45)', 'checked against the inner-seat reading (v46)', 1)
assert t.count('**Date:** 2026-09-30 (v45:') == 1
t = t.replace('**Date:** 2026-09-30 (v45:', '**Date:** 2026-09-30 (v46: 2026-10-11, M18 group B remaining 94 read by role: 24 in depth, 15 placed by their acts, 43 marked forward, 9 chapters, #1993 item F; v45:', 1)
anchor = '## Strand updates — desire (M18), group B sets 1 and 2 corrected'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v46-20261011.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v46 written; v45 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
N = 'M18 group B remaining 94 by role, #1993; '
notes = {
 '10-01-feeling-v18-20261009.md': ('10-01-feeling-v19-20261011.md', 'v19: delight beside meditating, under pressure, joined to doing; Psa 16:3; measure table +12, ' + N),
 '10-05-speaking-v18-20261009.md': ('10-05-speaking-v19-20261011.md', 'v19: the vow and the mouth (Ecc 5:2–7), ' + N),
 '10-06-wanting-v18-20261009.md': ('10-06-wanting-v19-20261011.md', 'v19: good eye; Ecc 11:7–9; Job 21:21; 1Ki 21:2; Jam 4:3, ' + N),
 '10-07-choosing-and-setting-direction-v23-20261009.md': ('10-07-choosing-and-setting-direction-v24-20261011.md', 'v24: Eli; Balaam; 1Sa 14; Esther 3 and 8; 1Ch 13; Gen 20:15; 2Ki 10:5, ' + N),
 '10-09-relating-to-god-v18-20261009.md': ('10-09-relating-to-god-v19-20261011.md', 'v19: Psa 90:13–17, ' + N),
 '10-10-relating-to-others-v20-20261009.md': ('10-10-relating-to-others-v21-20261011.md', 'v21: 2Sa 3:36; 2Sa 19:18–30; Gen 19:8, ' + N),
 '10-11-hiding-and-disclosing-v4-20261009.md': ('10-11-hiding-and-disclosing-v5-20261011.md', 'v5: words of surrender (1Sa 11:9–11), ' + N),
 '11-patterns-of-the-inner-life-v26-20261009.md': ('11-patterns-of-the-inner-life-v27-20261011.md', 'v27: §4 delight faces; "what seems good to you", ' + N),
 '13-01-divine-v18-20261009.md': ('13-01-divine-v19-20261011.md', 'v19: *Purposing* Isa 44, 46, 48; *Delight* 1Sa 15:22, Mal 1:10, Ecc 5:4, Psa 135:6, Num 24:1, Pro 8:30–31, ' + N),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v45-20261009.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v45-20261009.md', 'wa-essay-spirit-soul-body-claim-register-v46-20261011.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)

t = open(OTR, encoding='utf-8').read()
a = 'M41, M30, M28/M58,'
assert t.count(a) == 1
t = t.replace(a, 'M41, M30 (with Hos 8:8, placed beside Jer 22:28 by `m18-group-B-no-carrier-reading-v1-20261011.md`), M28/M58,')
a = '43 verses. In each,'
assert t.count(a) == 1
t = t.replace(a, '43 verses, plus Hos 8:8 (44). In each,')
open(OTR, 'w', encoding='utf-8').write(t)
print('OT-97 updated')

p = os.path.join(HERE, 'm18-group-B-remaining-role-triage-v1-20261011.csv')
rows = list(csv.DictReader(open(p, encoding='utf-8-sig')))
PLACED = {'2Ki 10:5': '10.7 Fear and choosing', '2Sa 19:27': '10.10 Loyalty and honour', '2Sa 19:18': '10.10 Loyalty and honour',
          '1Sa 11:10': '10.11 Hiding what I hold', '1Sa 14:36': '10.7 Whose measure', '1Sa 14:40': '10.7 Whose measure',
          'Est 3:11': '10.7 Whose measure', 'Est 8:8': '10.7 Whose measure', '1Ch 13:2': '10.7 Choosing together',
          '1Sa 3:18': '10.7 Choosing before God', 'Gen 19:8': '10.10 Loyalty and honour', 'Gen 20:15': '10.7 A choice that is honoured',
          '1Ki 10:13': '10.6 Precious (confirmed, no change)', '2Ch 9:12': 'parallel of 1Ki 10:13 (no change)'}
fields = list(rows[0].keys()) + ['placed']
for r in rows:
    r['placed'] = ''
    if r['reference'] in PLACED:
        assert r['decision'] == 'no-carrier', r['reference']
        r['decision'] = 'no-carrier, read and placed'
        r['placed'] = PLACED[r['reference']]
    if r['reference'] == 'Hos 8:8':
        r['decision'] = 'no-carrier, forward with Jer 22:28'; r['forward_to'] = 'M30'
nc = [r for r in rows if r['decision'] == 'no-carrier']
assert not nc, [r['reference'] for r in nc]
out = os.path.join(HERE, 'm18-group-B-remaining-role-triage-v2-20261011.csv')
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
shutil.move(p, os.path.join(HERE, 'archive', os.path.basename(p)))
print('triage CSV v2 written; v1 archived')
