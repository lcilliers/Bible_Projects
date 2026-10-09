"""M18 group B, set 1 (#1993, item F): claim register v41 -> v42 and narrative index rows. Run once. Writes files; no DB access."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — desire (M18), group B set 1: the delight verbs (2026-10-09, #1993 item F)

**Researcher, verbatim:** *"split the 77 between delight related words and pleasant related words. and read them in two separate sessions."* At the weave: *"delight associated with God goes to 13.1, separate section; HIB delight goes into 10.1"*.

**Source:** group B (delight, pleasure) after the filter leaves 448 verses. Of these, 171 hold a bucket-1 (inner-being candidate) hit. The 77 whose hit is a verb were split by Strong's number, and set 1 is the 56 delight verses: H2654A *ḥāpēṣ*, H6026 *ʿānag*, H8173B *šāʿaʿ*, G4913 *synēdomai*. Files: `../../Clusters/M18 - desire-longing/m18-group-B1-register-v1-20261009.csv` (reasons in `m18-group-B1-decisions-v1-20261009.py`), reading `m18-group-B1-delight-reading-v1-20261009.md`, weave `m18-group-B1-narrative-weave-v1-20261009.py`.

**Decisions:** a 46 · carried 6 · confirmed 3 (Isa 65:12, 66:4, 56:4) · route C 1 (Jer 6:2) · held 0.

**Structure changed:** a person's delight now has one account, in 10.1. The 10.6 section *Delight* was moved there whole, and 10.6 keeps a pointer.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.1 (v16) | **New** *Delight*: the 10.6 section moved in, plus *On God's word, and on God*; *When it looks right, and when it is missing*; *In a person*; *Wishing*; *A child's delight*; *God's delight in a person's hands*. Delight added to *When feeling changes character* and to the opening | New section; I read marked |
| 10.6 (v18) | *Delight* replaced by a pointer to 10.1; the Deu 21:11 pointer redirected | Moved |
| 13.1 (v16) | *Delight* widened: *Not strength, and truth within* (Jer 9:23–24; Psa 147:10–11; 51:5–6); *Whom he delights in, and why* (2Sa 22:20; Isa 62:4–5; Psa 37:23–24; 1Ki 10:7–9); *His delight in people's mouths* (Num 14:8–10; Psa 41:9–11; 22:8–9; 2Sa 15:26); *Not the offering itself* (Isa 1:11–13; Psa 40:6–8; 51:16–19; Hos 6:4–6); *He does what pleases him* widened (Psa 115:2–5; Isa 42:20–21; 55:11) | Widened; I read marked |

**Quote check:** 82 inserted quotations checked against the ESV in iba.db, 0 failures. The *ḥesed* identity in Hos 6:4 and 6:6 was checked in verse_lexical (H2617A).
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v41-20261009.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v41)') == 1
t = t.replace('checked against the inner-seat reading (v41)', 'checked against the inner-seat reading (v42)', 1)
assert t.count('**Date:** 2026-09-30 (v41:') == 1
t = t.replace('**Date:** 2026-09-30 (v41:', '**Date:** 2026-09-30 (v42: 2026-10-09, M18 group B set 1 (the delight verbs): 56 verses, 3 chapters, 10.1 *Delight* new, #1993 item F; v41:', 1)
anchor = '## Strand updates — desire (M18), group G: gloss away from desire (2026-10-09, #1993 item F)'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v42-20261009.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v42 written; v41 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
notes = {
 '10-01-feeling-v15-20261009.md': ('10-01-feeling-v16-20261009.md', 'v16: **new** *Delight* (a person’s delight; the 10.6 section moved in), M18 group B set 1, #1993; '),
 '10-06-wanting-v17-20261009.md': ('10-06-wanting-v18-20261009.md', 'v18: *Delight* moved to 10.1, pointer kept, #1993; '),
 '13-01-divine-v15-20261009.md': ('13-01-divine-v16-20261009.md', 'v16: *Delight* widened: strength refused, truth within; whom he delights in; his delight in people’s mouths; not the offering itself; does what pleases him, #1993; '),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v41-20261009.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v41-20261009.md', 'wa-essay-spirit-soul-body-claim-register-v42-20261009.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)
