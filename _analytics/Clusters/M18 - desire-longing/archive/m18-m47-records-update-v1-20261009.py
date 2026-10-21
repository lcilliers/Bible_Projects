"""M18 x M47 read-back (#1993): claim register v33 -> v34, narrative index rows, open threads OT-95 / OT-96.
Run once. Writes files; no DB access.
"""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))
OTR = os.path.normpath(os.path.join(HERE, '..', '..', 'cross-cluster-web', 'open-threads-register.md'))

# ---------- claim register v33 -> v34
src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v33-20261008.md')
t = open(src, encoding='utf-8').read()
t = t.replace('checked against the inner-seat reading (v33)', 'checked against the inner-seat reading (v34)', 1)
t = t.replace('**Date:** 2026-09-30 (v33:', '**Date:** 2026-09-30 (v34: 2026-10-09, desire (M18) × M47 read-back: 208 verses, 13 chapters, #1993; v33:', 1)
sec = open(os.path.join(HERE, 'm18-m47-claim-register-section-v1-20261009.md'), encoding='utf-8').read()
anchor = '## Strand updates — the 18 include verses (2026-10-08, #1992)'
assert t.count(anchor) == 1
t = t.replace(anchor, sec.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v34-20261009.md'), 'w', encoding='utf-8').write(t)
os.makedirs(os.path.join(ESSAY, 'archive'), exist_ok=True)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v34 written; v33 archived')

# ---------- index rows
idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
notes = {
 '10-06-wanting-v9-20261008.md': ('10-06-wanting-v10-20261009.md', 'v10: M18 × M47 read-back: desire in the heart and held there, the Preacher, delight, the wilderness craving, evil desire, wanting God and people, what is desired taken away, greed, #1993; '),
 '05-the-soul-v3-20261005.md': ('05-the-soul-v4-20261009.md', 'v4: M18 × M47 read-back: "exhaustion" restated, each death-wish with its own ground; a life precious; the ransom; the want before God, #1993; '),
 '04-the-heart-v12-20261008.md': ('04-the-heart-v13-20261009.md', 'v13: Pro 21:1 a heart directed, not a state; Mat 5:28, #1993; '),
 '06-the-spirit-v10-20261008.md': ('06-the-spirit-v11-20261009.md', 'v11: 1Sa 16:16, 23; the Spirit instructs, leads and carries (Neh 9:20; Psa 143:10; 2Pe 1:21), #1993; '),
 '07-flesh-v6-20261005.md': ('07-flesh-v7-20261009.md', 'v7: what is done with the desires of the flesh; flesh as an outward mark, #1993; '),
 '08-conscience-and-bosom-v5-20261005.md': ('08-conscience-and-bosom-v6-20261009.md', 'v6: Heb 13:18, #1993; '),
 '12-when-the-inner-being-goes-wrong-v13-20261008.md': ('12-when-the-inner-being-goes-wrong-v14-20261009.md', 'v14: Pro 16:19, #1993; '),
 '10-01-feeling-v13-20261008.md': ('10-01-feeling-v14-20261009.md', 'v14: Ecc 7:2; Pro 15:15, #1993; '),
 '10-05-speaking-v12-20261004.md': ('10-05-speaking-v13-20261009.md', 'v13: Psa 45:1; Pro 16:24, #1993; '),
 '10-07-choosing-and-setting-direction-v18-20261008.md': ('10-07-choosing-and-setting-direction-v19-20261009.md', 'v19: Jer 6:16; Act 7:38-39; willing gifts with joy; a will under another, #1993; '),
 '11-patterns-of-the-inner-life-v19-20261008.md': ('11-patterns-of-the-inner-life-v20-20261009.md', 'v20: §2 Ecc 9:7, #1993; '),
 '13-01-divine-v9-20261008.md': ('13-01-divine-v10-20261009.md', "v10: **new section *Delight***, God's delight and pleasure, from the M18 × M47 read-back, #1993; "),
 '13-02-angels-v1-20261007.md': ('13-02-angels-v2-20261009.md', 'v2: first content, 1Pe 1:12, #1993; '),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
t = t.replace('(v2: first content, 1Pe 1:12, #1993; **new**, empty) | — | — | empty |',
              '(v2: first content, 1Pe 1:12, #1993; **new**, empty) | — | M18 × M47 read-back (#1993) | draft |')
t = t.replace('`../wa-essay-spirit-soul-body-claim-register-v33-20261008.md`', '`../wa-essay-spirit-soul-body-claim-register-v34-20261009.md`')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated')

# ---------- open threads OT-95, OT-96 (appended after OT-94)
t = open(OTR, encoding='utf-8').read()
rows = open(os.path.join(HERE, 'm18-m47-open-threads-rows-v1-20261009.md'), encoding='utf-8').read().strip('\n')
lines = t.split('\n')
pos = max(i for i, l in enumerate(lines) if l.startswith('| OT-'))
assert lines[pos].startswith('| OT-94 '), lines[pos][:20]
lines[pos + 1:pos + 1] = rows.split('\n')
open(OTR, 'w', encoding='utf-8').write('\n'.join(lines))
print('open threads OT-95, OT-96 added')
