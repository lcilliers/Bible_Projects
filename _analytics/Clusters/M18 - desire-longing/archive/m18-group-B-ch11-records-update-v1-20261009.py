"""M18 group B, Ch 11 faces (#1993, item F): claim register v43 -> v44 and narrative index row. Run once. Writes files; no DB access."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — desire (M18), group B: three Ch 11 §4 faces (2026-10-09, #1993 item F)

**Researcher, verbatim:** *"proceed with Ch 11"*. These are the faces proposed in `m18-group-B1-delight-reading-v1-20261009.md` §12 and `m18-group-B2-pleasant-reading-v1-20261009.md` §6. Weave: `../../Clusters/M18 - desire-longing/m18-group-B-ch11-faces-weave-v1-20261009.py`.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| Ch 11 (v26) | §4 after *Delight*: *God's delight in a person* (Psa 18:19 / 22:8–9); *An offering* (Psa 51:16–19); *Being well pleased* (Mat 3:17 / 2Co 12:9–10). *What changes the character*: *Whose mouth it is in*; *What the one who brings it brings first* | Widened |

**Quote check:** 9 inserted quotations checked against the ESV in iba.db, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v43-20261009.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v43)') == 1
t = t.replace('checked against the inner-seat reading (v43)', 'checked against the inner-seat reading (v44)', 1)
assert t.count('**Date:** 2026-09-30 (v43:') == 1
t = t.replace('**Date:** 2026-09-30 (v43:', '**Date:** 2026-09-30 (v44: 2026-10-09, M18 group B: three Ch 11 §4 faces, #1993 item F; v43:', 1)
anchor = '## Strand updates — desire (M18), group B set 2: the pleasant and pleased verbs (2026-10-09, #1993 item F)'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v44-20261009.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v44 written; v43 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
old, new = '11-patterns-of-the-inner-life-v25-20261009.md', '11-patterns-of-the-inner-life-v26-20261009.md'
pat = '`' + old + '` ('
assert t.count(pat) == 1
t = t.replace(pat, '`' + new + '` (v26: §4 delight faces: thanks and taunt, an offering refused then delighted in, being well pleased; two *What changes the character* entries, #1993; ', 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v43-20261009.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v43-20261009.md', 'wa-essay-spirit-soul-body-claim-register-v44-20261009.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)
