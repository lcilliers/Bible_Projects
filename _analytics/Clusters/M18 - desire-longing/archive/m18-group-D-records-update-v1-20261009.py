"""M18 group D (#1993, item F): claim register v37 -> v38 and narrative index rows. Run once. Writes files; no DB access."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — desire (M18), group D: jealousy, zeal (2026-10-09, #1993 item F)

**Researcher, verbatim:** *"proceed with the next section of 1993"*.

**Source:** the 112 group D hits, less the verses already decided in the three read-backs and group A, which leaves 51 verses. Files: `../../Clusters/M18 - desire-longing/m18-group-D-register-v1-20261009.csv` (reasons in `m18-group-D-decisions-v1-20261009.py`) and the reading `m18-group-D-reading-v1-20261009.md`.

**Decisions:** missed and added 37 · confirmed 5 · carried 5 · route C 4 ("Simon the Zealot") · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.6 (v14) | *Jealousy and envy*: zeal read in (the same words). Zeal that consumes (Psa 69:8–9; 119:139, 141; Joh 2:16–17); zeal without knowledge (Rom 10:1–3; Gal 1:13–16; Phi 3:6–7; Act 22:3–4; 21:20–21); zeal on show and zeal that set aside an oath (2Ki 10:16, 31; 2Sa 21:1–2); jealousy that is God's in a man (2Co 11:2–3); zeal for others and for good (Col 4:12–13; 1Pe 3:13–14; Tit 2:14). New *Jealousy against a person* (Gen 37:4, 11; 26:12–16; Psa 106:16–17 with Num 16:3; Act 5:17–18; 13:45; Eze 31:9–10; Isa 11:12–13). Ecc 9:6. New *A husband's jealousy with no witness* (Num 5:14–15, 30–31; Pro 6:35) | Widened; I read marked |
| 13.1 (v14) | *Jealousy*: his name in the commandment (Exo 20:5–6; Deu 5:9–10; Exo 34:14; Deu 4:23–24); 1Ki 14:22; Zec 1:12–16; roused by prayer, joined to pity (Joe 2:17–18; Eze 39:25–26); zeal that does the work (Isa 9:7; 2Ki 19:30–31; Isa 37:31–32); put on when no one stood (Isa 59:16–17); Heb 10:26–27; missed and asked to be seen (Isa 63:15; 26:11). Closing reading widened | Widened |
| 10.3 (v6) | Joh 2:17; Gen 37:11 | Widened |
| Ch 11 (v24) | §4 *Whose jealousy, and for whom*: zeal faces and jealousy against a person | Widened |
| Ch 12 (v17) | *Pride*: Eze 31:9–10 | Widened |

**Quote check:** 66 inserted quotations checked against the ESV in iba.db, 0 failures. Two bare citations that followed an Acts citation now name Philippians and Galatians.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v37-20261009.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v37)') == 1
t = t.replace('checked against the inner-seat reading (v37)', 'checked against the inner-seat reading (v38)', 1)
t = t.replace('**Date:** 2026-09-30 (v37:', '**Date:** 2026-09-30 (v38: 2026-10-09, M18 group D (jealousy, zeal): 51 verses, 5 chapters, #1993 item F; v37:', 1)
anchor = '## Strand updates — desire (M18), group A: desire, craving, longing (2026-10-09, #1993 item F)'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v38-20261009.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v38 written; v37 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
notes = {
 '10-06-wanting-v13-20261009.md': ('10-06-wanting-v14-20261009.md', 'v14: M18 group D: zeal read into *Jealousy and envy*; **new** *Jealousy against a person* and *A husband\'s jealousy with no witness*, #1993; '),
 '13-01-divine-v13-20261009.md': ('13-01-divine-v14-20261009.md', 'v14: *Jealousy* widened from M18 group D: his name in the commandment, roused by prayer, zeal that does the work, put on as a cloak, #1993; '),
 '10-03-remembering-and-forgetting-v5-20261004.md': ('10-03-remembering-and-forgetting-v6-20261009.md', 'v6: Joh 2:17; Gen 37:11, #1993; '),
 '11-patterns-of-the-inner-life-v23-20261009.md': ('11-patterns-of-the-inner-life-v24-20261009.md', 'v24: §4 zeal and jealousy against a person, #1993; '),
 '12-when-the-inner-being-goes-wrong-v16-20261009.md': ('12-when-the-inner-being-goes-wrong-v17-20261009.md', 'v17: Eze 31:9–10, #1993; '),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v37-20261009.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v37-20261009.md', 'wa-essay-spirit-soul-body-claim-register-v38-20261009.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)
