"""M18 group B, set 2 (#1993, item F): claim register v42 -> v43 and narrative index rows. Run once. Writes files; no DB access."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — desire (M18), group B set 2: the pleasant and pleased verbs (2026-10-09, #1993 item F)

**Researcher, verbatim:** *"proceed with set 2"*. Placement as ruled for set 1: *"delight associated with God goes to 13.1, separate section; HIB delight goes into 10.1"*.

**Source:** the 21 bucket-1 verb verses of H5276 *nāʿēm* (be pleasant) and G2106 *eudokeō* (to be well pleased). Files: `../../Clusters/M18 - desire-longing/m18-group-B2-register-v1-20261009.csv` (reasons in `m18-group-B2-decisions-v1-20261009.py`), reading `m18-group-B2-pleasant-reading-v1-20261009.md`, weave `m18-group-B2-narrative-weave-v1-20261009.py`.

**Decisions:** a 15 · carried 3 · confirmed 2 (2Co 5:8, 2Th 2:12) · route C 1 (Eze 32:19) · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.1 (v17) | *Delight*: **new** *What is found pleasant* (Gen 49:14–15; Song 7:5–6; 2Sa 1:26; Pro 9:17–18; Psa 141:4–6; Pro 24:24–25; 2Co 12:8–10); *Wishing* widened (1Th 3:1–3) | New subsection; I read marked |
| 13.1 (v17) | *Delight*: **new** *The voice again, on the mountain* (Mat 17:4–7; 2Pe 1:16–19); **new** *His good pleasure gives* (Luk 12:30–32; 1Co 1:21; Col 1:19–21); not pleased though they shared it all (1Co 10:3–6); Hebrews reads Psalm 40 of Christ (Heb 10:5–10) | Widened |

**Quote check:** 28 inserted quotations checked against the ESV in iba.db, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v42-20261009.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v42)') == 1
t = t.replace('checked against the inner-seat reading (v42)', 'checked against the inner-seat reading (v43)', 1)
assert t.count('**Date:** 2026-09-30 (v42:') == 1
t = t.replace('**Date:** 2026-09-30 (v42:', '**Date:** 2026-09-30 (v43: 2026-10-09, M18 group B set 2 (the pleasant and pleased verbs): 21 verses, 2 chapters, #1993 item F; v42:', 1)
anchor = '## Strand updates — desire (M18), group B set 1: the delight verbs (2026-10-09, #1993 item F)'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v43-20261009.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v43 written; v42 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
notes = {
 '10-01-feeling-v16-20261009.md': ('10-01-feeling-v17-20261009.md', 'v17: *Delight*: **new** *What is found pleasant*; willing because it could not be borne (1Th 3:1), M18 group B set 2, #1993; '),
 '13-01-divine-v16-20261009.md': ('13-01-divine-v17-20261009.md', 'v17: *Delight*: the voice on the mountain; his good pleasure gives; not pleased though they shared it all; Heb 10:5–10, #1993; '),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v42-20261009.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v42-20261009.md', 'wa-essay-spirit-soul-body-claim-register-v43-20261009.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)
