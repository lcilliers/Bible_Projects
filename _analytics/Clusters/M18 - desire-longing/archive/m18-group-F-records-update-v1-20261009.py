"""M18 group F (#1993, item F): claim register v39 -> v40 and narrative index rows. Run once. Writes files; no DB access."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — desire (M18), group F: precious (2026-10-09, #1993 item F)

**Researcher, verbatim:** *"proceed with group F"*.

**Source:** the 60 group F hits, less the verses already decided in the three read-backs and groups A, D and E, which leaves 44 verses. Files: `../../Clusters/M18 - desire-longing/m18-group-F-register-v1-20261009.csv` (reasons in `m18-group-F-decisions-v1-20261009.py`) and the reading `m18-group-F-reading-v1-20261009.md`.

**Decisions:** missed and added 27 (Pro 3:15 and Act 5:34 were cited, but their M18 word was not carried, #1987) · confirmed 2 · carried 1 · route C 14 (stones, cargo, building material, the city's radiance, "cold", people made "rare") · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.6 (v16) | **New** *Precious*: wisdom above every desire, its worth not known (Pro 3:15; Job 28:13, 16); faith tested (1Pe 1:6–8); the farmer's waiting and the fattened hearts (Jam 5:3–8); the cornerstone and the refuge of lies (Isa 28:15–16; 1Pe 2:6–7); what is honoured shows in what is given (1Ch 29:2–3; Dan 11:37–38); the queen of Sheba (1Ki 10:1–13); honour held (Heb 13:4–5; 1Sa 18:29–30); splendour that entices, passes and covers (Job 31:24–28; Psa 37:1, 20; Rev 17:4). *Aimed at God*: Psa 36:7–8. *Possessions*: two ways to fill a house (Pro 1:13; 24:1–4; 12:27). *Taken away*: the cargo that ends in human souls (Rev 18:11–17) | Widened; new section; I read marked |
| 10.4 (v9) | *It reckons*: the lordly price (Zec 11:12–13; Mat 27:3, 9) | Widened |
| 13.1 (v15) | *Delight*: Ephraim held dear while spoken against (Jer 31:19–20); the price paid (1Pe 1:18–19) | Widened |
| Ch 12 (v18) | *Pride*: the king of Tyre's given splendour (Eze 28:13–17) | Widened |
| 10.2 (v13) | The word rare in Samuel's days; hearing learned (1Sa 3:1–9) | Widened |
| 10.10 (v18) | *Friends, company and care*: the visit kept seldom (Pro 25:16–17) | Widened |
| 10.5 (v16) | *From the heart to the mouth*: utter what is precious (Jer 15:18–19) | Widened |
| 10.13 (v6) | Gamaliel "held in honor by all the people" (Act 5:34) | Wording widened in place |
| Ch 11 (v25) | §4 *Precious*: worth, rarity, splendour, esteem, price, dearness | Widened |

**Quote check:** 64 inserted quotations checked against the ESV in iba.db, 0 failures. The Gamaliel phrase in 10.13 has no citation after it on its line; it was checked by hand against Acts 5:34.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v39-20261009.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v39)') == 1
t = t.replace('checked against the inner-seat reading (v39)', 'checked against the inner-seat reading (v40)', 1)
assert t.count('**Date:** 2026-09-30 (v39:') == 1
t = t.replace('**Date:** 2026-09-30 (v39:', '**Date:** 2026-09-30 (v40: 2026-10-09, M18 group F (precious): 44 verses, 9 chapters, #1993 item F; v39:', 1)
anchor = '## Strand updates — desire (M18), group E: thirst, hunger (2026-10-09, #1993 item F)'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v40-20261009.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v40 written; v39 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
notes = {
 '10-06-wanting-v15-20261009.md': ('10-06-wanting-v16-20261009.md', 'v16: M18 group F: **new** *Precious*; Psa 36:7–8 in *Aimed at God*; two ways to fill a house in *Possessions*; Babylon\'s cargo in *Taken away*, #1993; '),
 '10-04-thinking-v8-20261008.md': ('10-04-thinking-v9-20261009.md', 'v9: the lordly price (Zec 11:13; Mat 27:9), #1993; '),
 '13-01-divine-v14-20261009.md': ('13-01-divine-v15-20261009.md', 'v15: *Delight*: Ephraim my dear son (Jer 31:20); the price paid (1Pe 1:18–19), #1993; '),
 '12-when-the-inner-being-goes-wrong-v17-20261009.md': ('12-when-the-inner-being-goes-wrong-v18-20261009.md', 'v18: Eze 28:13–17, #1993; '),
 '10-02-knowing-and-hearing-v12-20261009.md': ('10-02-knowing-and-hearing-v13-20261009.md', 'v13: the word rare in Samuel\'s days (1Sa 3:1–9), #1993; '),
 '10-10-relating-to-others-v17-20261009.md': ('10-10-relating-to-others-v18-20261009.md', 'v18: the visit kept seldom (Pro 25:16–17), #1993; '),
 '10-05-speaking-v15-20261009.md': ('10-05-speaking-v16-20261009.md', 'v16: utter what is precious (Jer 15:18–19), #1993; '),
 '10-13-anger-v5-20261008.md': ('10-13-anger-v6-20261009.md', 'v6: Gamaliel held in honour (Act 5:34), #1993; '),
 '11-patterns-of-the-inner-life-v24-20261009.md': ('11-patterns-of-the-inner-life-v25-20261009.md', 'v25: §4 precious, #1993; '),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v39-20261009.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v39-20261009.md', 'wa-essay-spirit-soul-body-claim-register-v40-20261009.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)
