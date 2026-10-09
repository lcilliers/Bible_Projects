"""M18 group B correction (#1993, item F): claim register v44 -> v45 and narrative index rows. Run once. Writes files; no DB access."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — desire (M18), group B sets 1 and 2 corrected: read by the main operation (2026-10-09, #1993 item F)

**Researcher, verbatim (on 2Pe 2:13):** *"making something of this verse with pleasure as an entry point will lead to distorted views"*; then *"yes, re-read and correct your work."*

**What was wrong:** sets 1 and 2 were read with delight as the way in. Twenty-six verses were placed under *Delight* although the delight word only measures or qualifies another act. Each is now placed with the act the verse is about. Record: `../../Clusters/M18 - desire-longing/m18-group-B-correction-reread-v1-20261009.md`.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.1 (v18) | *Delight*: four subsections removed; new table *When delight is only the measure* (26 rows, each pointing to its home) | Corrected |
| 10.2 (v15) | Jer 6:10–11: ears that cannot listen | Moved in |
| 10.5 (v18) | Psa 109:16–18 cursing put on; Psa 22:7–9 mockery before words | Moved in; I read marked |
| 10.7 (v23) | Gen 49:14–15 and Pro 9:13–18 (*What draws it*); 2Sa 15:25–26 (*Choosing before God*); Isa 58:2 (*An inner act weighed*); Psa 141:4–8 (*Setting the heart*); 2Sa 24:3–4, 10 (*Choices weighed by another*) | Moved in; I read marked |
| 10.8 (v7) | Pro 24:23–25 judging without partiality | Moved in |
| 10.9 (v18) | *Comforted as by a mother* (Isa 66:11–13); *Told to depart* (Job 21:13–16); *Returned to* (Job 22:21–27); Job 9:2–3, 13:3–4, 15 contending; Num 14:8–10 not fearing; Job 27:9–10 calling in distress | Moved in; I read marked |
| 10.10 (v20) | 1Sa 18:21–22 snare; Deu 25:7–10 refused duty; 2Sa 20:9–13 following past a body; Ecc 8:2–5 before a king; 1Th 3:1–5, Job 33:30–32, Psa 41:9–11 | Moved in; I read marked |
| Ch 12 (v19) | *Pride*: Haman's designed honour and fall (Est 6:6–13) | Moved in; I read marked |
| 13.1 (v18) | Isa 55:10–11 moved from *Delight* to *Purposing*; *His delight in people's mouths* now points to the acts | Corrected |
| 13.4 (v4) | *Harm ended* (Isa 11:6–9) | Moved in |

**Quote check:** 88 inserted quotations checked against the ESV in iba.db, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v44-20261009.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v44)') == 1
t = t.replace('checked against the inner-seat reading (v44)', 'checked against the inner-seat reading (v45)', 1)
assert t.count('**Date:** 2026-09-30 (v44:') == 1
t = t.replace('**Date:** 2026-09-30 (v44:', '**Date:** 2026-09-30 (v45: 2026-10-09, M18 group B sets 1 and 2 corrected by the main operation: 26 verses moved, 10 chapters, #1993 item F; v44:', 1)
anchor = '## Strand updates — desire (M18), group B: three Ch 11 §4 faces (2026-10-09, #1993 item F)'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v45-20261009.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v45 written; v44 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
N = 'M18 group B correction by main operation, #1993; '
notes = {
 '10-01-feeling-v17-20261009.md': ('10-01-feeling-v18-20261009.md', 'v18: *Delight* corrected: table *When delight is only the measure*, ' + N),
 '10-02-knowing-and-hearing-v14-20261009.md': ('10-02-knowing-and-hearing-v15-20261009.md', 'v15: ears that cannot listen (Jer 6:10–11), ' + N),
 '10-05-speaking-v17-20261009.md': ('10-05-speaking-v18-20261009.md', 'v18: cursing put on (Psa 109:16–18); mockery (Psa 22:7–9), ' + N),
 '10-07-choosing-and-setting-direction-v22-20261009.md': ('10-07-choosing-and-setting-direction-v23-20261009.md', 'v23: Gen 49:15, Pro 9:13–18, 2Sa 15:26, Isa 58:2, Psa 141:4–8, 2Sa 24:3, ' + N),
 '10-08-right-and-wrong-v6-20261009.md': ('10-08-right-and-wrong-v7-20261009.md', 'v7: judging without partiality (Pro 24:23–25), ' + N),
 '10-09-relating-to-god-v17-20261009.md': ('10-09-relating-to-god-v18-20261009.md', 'v18: comforted as by a mother; told to depart; returned to; contending; not fearing; calling in distress, ' + N),
 '10-10-relating-to-others-v19-20261009.md': ('10-10-relating-to-others-v20-20261009.md', 'v20: snare; refused duty; following past a body; before a king; Timothy sent; Elihu; betrayal, ' + N),
 '12-when-the-inner-being-goes-wrong-v18-20261009.md': ('12-when-the-inner-being-goes-wrong-v19-20261009.md', 'v19: *Pride*: Haman (Est 6:6–13), ' + N),
 '13-01-divine-v17-20261009.md': ('13-01-divine-v18-20261009.md', 'v18: Isa 55:10–11 to *Purposing*, ' + N),
 '13-04-nature-v3-20261009.md': ('13-04-nature-v4-20261009.md', 'v4: *Harm ended* (Isa 11:6–9), ' + N),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v44-20261009.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v44-20261009.md', 'wa-essay-spirit-soul-body-claim-register-v45-20261009.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)
