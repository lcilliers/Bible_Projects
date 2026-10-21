"""M02 pairing gaps weave (OT-29, OT-30, OT-51), 2026-10-13: records pass.
Claim register v50 -> v51 (new strand-update section); narrative index rows for the 7 chapters bumped by
m02-pairing-gaps-weave-v1-20261013.py. The thread items are closed through Escalation.ps1, not here. Run once."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — anger (M02) pairings with strands already read: 14 gaps woven, two corrections (2026-10-13, OT-29/OT-30/OT-51)

**Researcher, verbatim:** *"proceed as recommended"*, then *"weave the 14 gaps and make the two fixes"*.

**Source:** `../../Clusters/M02 - anger-wrath/m02-pairing-done-strands-check-v1-20261013.md`. The 90 verses that M02 shares with M01, M20, M25 and M64 were checked against the narrative. A verse counted as carried only where the narrative carries the anger and the paired word together. 14 were not carried; each was read in its passage (section 3) and is woven here. Script: `m02-pairing-gaps-weave-v1-20261013.py`.

**Original claims changed:** two. The 10.13 working note said that the life-and-death verses were "kept for Chapter 2, where that placement is on hold". OT-08 was closed on 2026-10-09 and Chapter 2 already carries Jonah 4:9, so the note is removed. Chapter 5 said that Chapter 2 takes up Proverbs 20:2, but Chapter 2 does not cite it. The pointer now names 10.13 *Other parties*, where the verse is placed.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.13 (v8) | *Reading the ruin*: Deu 31:17, God's side beside the people's question. *How it is provoked*: **Known beforehand** (Deu 31:27, 29). *Bearing it*: Lam 2:20, 22 (terrors summoned as to a festival). *How it ends*: **The cup taken back** (Isa 51:17–22). *Shelter, and who can stand*: Zep 2:3; Pro 11:4; Psa 76:7–9. *How it is answered*: Pro 29:8, 11. *Other parties*: Pro 20:2–3 with the ruler's anger; **Those who pursue another** (Job 19:25, 28–29); **The nations** (Rev 11:18). Working note on Chapter 2 "on hold" removed | Added; I read marked; one note removed |
| 10.9 (v22) | *When God hides his face*: the **Sin** bullet widened with Deu 31:16–18 and the people's question; **Time is weighed against it** (Psa 89:46–47); Jer 33:5–6, the hidden face followed at once by healing | Added; I read marked |
| 10.12 (v8) | *Fear before God*: Psa 76:7–9 (fear as stillness); Rev 11:18 (those who fear his name rewarded). *Fear between people*: Pro 20:2–3 | Added |
| 10.4 (v13) | *Where thoughts come from*: a thought answered by God (Eze 20:1, 32–33) | Added |
| 13.1 (v23) | *Ruling*: **His rule answers a thought** (Eze 20:32–37); **His reign, and the nations' rage** (Rev 11:17–18) | Added |
| Ch 2 (v18) | *What death is*: Psa 89:46–47 beside 89:48 | Added |
| Ch 5 (v6) | Pointer for Pro 20:2 corrected from Chapter 2 to 10.13 *Other parties* | Restated |

**Not woven:** Ezekiel 20:13 and 20:21 are forwarded to OT-01 (life by the statutes), which holds Ezekiel 20:11.

**Quote check:** every inserted quotation was checked against the ESV in iba.db: 52 parts, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v50-20261012.md')
t = open(src, encoding='utf-8').read()
t = t.replace('checked against the inner-seat reading (v50)', 'checked against the inner-seat reading (v51)', 1)
assert t.count('**Date:** 2026-09-30 (v50:') == 1
t = t.replace('**Date:** 2026-09-30 (v50:', '**Date:** 2026-09-30 (v51: 2026-10-13, M02 pairing threads OT-29/30/51: 14 gap verses woven, 10.13 hold note removed, Ch 5 pointer corrected; v50:', 1)
anchor = '## Strand updates — authority (M72), group B: Ch 11 retitled'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v51-20261013.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v51 written; v50 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
N = 'M02 pairing gaps, OT-29/30/51; '
notes = {
 '10-13-anger-v7-20261012.md': ('10-13-anger-v8-20261013.md', 'v8: Deu 31:17, 27–29; Lam 2:20–22; Isa 51:17–22; Zep 2:3; Pro 11:4; Psa 76:7–9; Pro 29:8; Pro 20:2; Job 19:29; Rev 11:18; Chapter 2 hold note removed, ' + N),
 '10-09-relating-to-god-v21-20261012.md': ('10-09-relating-to-god-v22-20261013.md', 'v22: Deu 31:16–18; Psa 89:46–47; Jer 33:5–6, ' + N),
 '10-12-fear-v7-20261012.md': ('10-12-fear-v8-20261013.md', 'v8: Psa 76:7–9; Rev 11:18; Pro 20:2–3, ' + N),
 '10-04-thinking-v12-20261012.md': ('10-04-thinking-v13-20261013.md', 'v13: Eze 20:32–33, ' + N),
 '13-01-divine-v22-20261012.md': ('13-01-divine-v23-20261013.md', 'v23: *Ruling* gains Eze 20:32–37 and Rev 11:17–18, ' + N),
 '02-life-breath-and-death-v17-20261012.md': ('02-life-breath-and-death-v18-20261013.md', 'v18: Psa 89:46–47, ' + N),
 '05-the-soul-v5-20261012.md': ('05-the-soul-v6-20261013.md', 'v6: Pro 20:2 pointer corrected to 10.13, ' + N),
}
for old, (new, note) in notes.items():
    key = '`' + old + '` ('
    assert t.count(key) == 1, old
    t = t.replace(key, '`' + new + '` (' + note, 1)
open(idx, 'w', encoding='utf-8').write(t)
print('index rows updated:', len(notes))
