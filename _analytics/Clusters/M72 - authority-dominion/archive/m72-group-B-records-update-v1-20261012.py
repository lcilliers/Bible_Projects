"""M72 group B (#1998), 2026-10-12: records for the Ch 11 sec 7 and faculty/other-beings weave.
Claim register v48 -> v49, narrative index rows, OT-100 in the open threads register. Run once; no DB access."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))
OTR = os.path.normpath(os.path.join(HERE, '..', '..', 'cross-cluster-web', 'open-threads-register.md'))

SEC = '''## Strand updates — authority (M72), group B: current thoughts into Ch 11 §7, and the faculty and other-being parts placed (2026-10-12, #1998)

**Researcher, verbatim:** *"I suggest you add the current thoughts coming out of the M72 reading to ch_11 and place the parts that is specific to the heart, flesh, divine etc. into those sections. from what I can see at the moment rule, authority, giving or having power is more of a state or status that works in collaboration with other characteristics and parties, but this is not yet strongly emerging from the material you are providing."*

**Source:** `../../Clusters/M72 - authority-dominion/m72-group-B-reading-v1-20261012.md` (275 verses triaged; 81 read in 9 groups). Record: `m72-group-B-weave-record-v1-20261012.md`. The 10.x activity sections are not touched (not instructed).

**Original claims changed:** Ch 11 §7's opening, *"Scripture takes the words it uses for ruling … and turns them inward"*, is restated as *"In some verses Scripture takes …"*. The M72 reading found ruling turned inward in a few verses only (Pro 16:32, Gen 4:7, 1Co 7:37, 1Co 6:12), and those join the rule to another act.

| Section | Added or changed | Verdict |
|---|---|---|
| Ch 11 (v30) | §7: new subsection *Authority as a standing*. Authority given before it is held; what moves inside it (fear, pride, wanting, hatred, conviction and fury, faith, care for another, joy, the fear of God, knowing who rules); Saul and Paul compared; turned round; its limits and whose the ruled are; offered, sought, refused; living under it; ruling within. Held as a first reading; working note (OT-100) | Added; I read marked; opening restated |
| Ch 2 (v17) | Psa 49:14, 16 beside 49:15 | Added |
| Ch 4 (v15) | Ecc 8:9 (the heart watching power); Dan 4:30–31, 26 under *A heart lifted up*; Act 8:19–22; Judg 9:2–3; Jer 30:21 | Added; I read marked |
| Ch 5 (v5) | Psa 103:22 | Added |
| Ch 7 (v8) | Kin used to win rule (Judg 9:2–3, 5); flesh and blood beside the powers (Eph 6:12); Jude 8–10 beside 2Pe 2:10 | Added |
| Ch 8 (v7) | 1Co 8:9 in the weak-conscience bullet; Rom 13:1 beside 13:5 | Added; I read marked |
| 13.1 (v22) | New section *Ruling*: he rules over all; his rule to be known; he gives and takes authority; the Son's authority; the Father's own authority (Act 1:7); the ruler to come, with peace; the soul's answer | Added |
| 13.2 (v5) | Angels with authority, and those who did not keep it (Jude 6); Michael (Jude 9); Hos 12:4; 1Co 11:10 recorded without explanation | Added |
| 13.3 (v3) | Eph 6:12–13; Luk 10:17–20; Act 19:16; Luk 22:53; Rev 13:2, 4; Col 2:15 | Added |
| 13.4 (v5) | Lights that rule (Gen 1:16; Psa 136:8–9); creatures under man's dominion (Gen 1:26; Psa 8:6–7) | Added |

**Quote check:** every inserted quotation was checked against the ESV in iba.db, 0 failures. Three were checked by hand: Pro 16:32, the existing bracketed line; Psa 8:6–7, joined at a comma; and the researcher's own words in the working note.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v48-20261012.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v48)') == 1
t = t.replace('checked against the inner-seat reading (v48)', 'checked against the inner-seat reading (v49)', 1)
assert t.count('**Date:** 2026-09-30 (v48:') == 1
t = t.replace('**Date:** 2026-09-30 (v48:', '**Date:** 2026-09-30 (v49: 2026-10-12, M72 group B: current thoughts into Ch 11 §7 (*Authority as a standing*), faculty and other-being parts placed, 10 chapters, #1998; v48:', 1)
anchor = '## Strand updates — desire (M18) × authority (M72): the 51 never-read shared verses'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v49-20261012.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v49 written; v48 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
N = 'M72 group B, #1998; '
notes = {
 '02-life-breath-and-death-v16-20261009.md': ('02-life-breath-and-death-v17-20261012.md', 'v17: Psa 49:14, 16, ' + N),
 '04-the-heart-v14-20261009.md': ('04-the-heart-v15-20261012.md', 'v15: the heart watching power (Ecc 8:9); the boast (Dan 4:30); Act 8:21–22; Judg 9:3; Jer 30:21, ' + N),
 '05-the-soul-v4-20261009.md': ('05-the-soul-v5-20261012.md', 'v5: Psa 103:22, ' + N),
 '07-flesh-v7-20261009.md': ('07-flesh-v8-20261012.md', 'v8: kin used to win rule; Eph 6:12; Jude 8–10, ' + N),
 '08-conscience-and-bosom-v6-20261009.md': ('08-conscience-and-bosom-v7-20261012.md', 'v7: 1Co 8:9; Rom 13:1 beside 13:5, ' + N),
 '11-patterns-of-the-inner-life-v29-20261012.md': ('11-patterns-of-the-inner-life-v30-20261012.md', 'v30: §7 *Authority as a standing* (first reading; title under question, OT-100), ' + N),
 '13-01-divine-v21-20261012.md': ('13-01-divine-v22-20261012.md', 'v22: new section *Ruling*, ' + N),
 '13-02-angels-v4-20261012.md': ('13-02-angels-v5-20261012.md', 'v5: angels with authority; Jude 6, 9; Hos 12:4; 1Co 11:10, ' + N),
 '13-03-other-spirits-v2-20261012.md': ('13-03-other-spirits-v3-20261012.md', 'v3: authorities that are not human (Eph 6:12); Luk 10:17–20; Act 19:16; Luk 22:53; Rev 13, ' + N),
 '13-04-nature-v4-20261009.md': ('13-04-nature-v5-20261012.md', 'v5: lights that rule; creatures under man\'s dominion, ' + N),
}
for old, (new, note) in notes.items():
    key = '`' + old + '` ('
    assert t.count(key) == 1, old
    t = t.replace(key, '`' + new + '` (' + note, 1)
open(idx, 'w', encoding='utf-8').write(t)
print('index rows updated:', len(notes))

ot = open(OTR, encoding='utf-8').read()
row = ('| OT-100 | **The inner-being meaning of authority and ruling: not yet explored to the full.** The M72 group B reading (#1998) '
       'read 81 verses in 9 groups. The researcher\'s reading of it, verbatim: *"I don\'t think we really have discovered, debated or explored to the full the true meaning of authority and ruling from a inner being perspective.  M72 have added to the understanding, but maybe we are looking at it from the wrong direction … rule, authority, giving or having power is more of a state or status that works in collaboration with other characteristics and parties, but this is not yet strongly emerging from the material you are providing. I am not discounting that you are biased in your treatment of readings, so it is likely that I will need to read it again at some point."* '
       'Also: *"I dont\' think the title of ch_11 is true to its contents"*. The current thoughts are in Ch 11 §7 *Authority as a standing* (v30), held as a first reading with a working note. '
       'Inputs: `../Clusters/M72 - authority-dominion/m72-group-B-reading-v1-20261012.md` (in it, the B word is often labelled the characteristic where another act carries the verse; see `m72-group-B-weave-record-v1-20261012.md` §2), the triage CSV, the passages file. '
       '| M72 group B weave (#1998, 2026-10-12) | the researcher re-reads the M72 material, or a later strand reads authority together with the characteristics that move inside it (fear, pride, wanting, care for another); the Ch 11 / §7 title question is answered | open |')
anchor = '| OT-99 |'
lines = ot.split('\n')
i = [k for k, l in enumerate(lines) if l.startswith(anchor)]
assert len(i) == 1
lines.insert(i[0] + 1, row)
open(OTR, 'w', encoding='utf-8').write('\n'.join(lines))
print('OT-100 added')
