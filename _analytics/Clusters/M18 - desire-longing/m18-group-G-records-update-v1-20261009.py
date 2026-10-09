"""M18 group G (#1993, item F): claim register v40 -> v41 and narrative index rows. Run once. Writes files; no DB access."""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — desire (M18), group G: gloss away from desire (2026-10-09, #1993 item F)

**Researcher, verbatim:** *"proceed with G"*.

**Source:** the 23 group G hits, less the verses already decided in the three read-backs and groups A, D, E and F, which leaves 21 verses. The M18 words here are glossed "far, long", "collection, gathering" and "untroubled"; each verse was read in its passage for what it carries. Files: `../../Clusters/M18 - desire-longing/m18-group-G-register-v1-20261009.csv` (reasons in `m18-group-G-decisions-v1-20261009.py`) and the reading `m18-group-G-reading-v1-20261009.md`.

**Decisions:** missed and added 12 (Mar 12:34 was cited, but "not far from the kingdom" was not carried, #1987) · confirmed 1 · carried 1 · route C 7 (gathered waters, the collection for the saints, thick clouds, a far country) · held 0.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| Ch 14 (v14) | **New** *Brought near*: far off and without hope, brought near; the hostility killed; peace to far and near (Eph 2:12–18) | New section; I read marked |
| 10.9 (v17) | *Sought, and not far* (Act 17:27–28); *Recognised, and gone to* (Joh 21:7–8) | Widened; I read marked |
| 10.10 (v19) | The son's self-rating set aside by the father (Luk 15:19–22) | Widened; I read marked |
| 10.4 (v10) | *It reckons*: the centurion reckoned worthy by others, not by himself (Luk 7:4–9) | Widened |
| 10.6 (v17) | *A person*: Paul's wish for Agrippa and his hearers (Act 26:28–29) | Widened |
| 10.2 (v14) | Hearing that stops at one word (Act 22:18–22); words as goads and nails (Ecc 12:10–12) | Widened; I read marked |
| 10.5 (v17) | *When mouth and heart part*: long prayers for a pretense, and the widow (Mar 12:38–44) | Widened |
| 10.11 (v4) | *Hiding another*: what the guards told, covered with money and a story (Mat 28:11–15) | Widened |
| Ch 3 (v3) | "You are not far from the kingdom of God" added to the cited Mark 12:33–34 | Wording widened in place |

**Quote check:** 28 inserted quotations checked against the ESV in iba.db, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v40-20261009.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v40)') == 1
t = t.replace('checked against the inner-seat reading (v40)', 'checked against the inner-seat reading (v41)', 1)
assert t.count('**Date:** 2026-09-30 (v40:') == 1
t = t.replace('**Date:** 2026-09-30 (v40:', '**Date:** 2026-09-30 (v41: 2026-10-09, M18 group G (gloss away from desire): 21 verses, 9 chapters, #1993 item F; v40:', 1)
anchor = '## Strand updates — desire (M18), group F: precious (2026-10-09, #1993 item F)'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v41-20261009.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v41 written; v40 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
notes = {
 '14-made-new-v13-20261008.md': ('14-made-new-v14-20261009.md', 'v14: **new** *Brought near* (Eph 2:12–18), M18 group G, #1993; '),
 '10-09-relating-to-god-v16-20261009.md': ('10-09-relating-to-god-v17-20261009.md', 'v17: sought and not far (Act 17:27); recognised and gone to (Joh 21:7–8), #1993; '),
 '10-10-relating-to-others-v18-20261009.md': ('10-10-relating-to-others-v19-20261009.md', 'v19: the father and the son’s self-rating (Luk 15:19–22), #1993; '),
 '10-04-thinking-v9-20261009.md': ('10-04-thinking-v10-20261009.md', 'v10: the centurion (Luk 7:4–9), #1993; '),
 '10-06-wanting-v16-20261009.md': ('10-06-wanting-v17-20261009.md', 'v17: Paul’s wish (Act 26:28–29), #1993; '),
 '10-02-knowing-and-hearing-v13-20261009.md': ('10-02-knowing-and-hearing-v14-20261009.md', 'v14: hearing stopped at one word (Act 22:18–22); goads and nails (Ecc 12:10–12), #1993; '),
 '10-05-speaking-v16-20261009.md': ('10-05-speaking-v17-20261009.md', 'v17: long prayers for a pretense, and the widow (Mar 12:38–44), #1993; '),
 '10-11-hiding-and-disclosing-v3-20261008.md': ('10-11-hiding-and-disclosing-v4-20261009.md', 'v4: the guards’ report covered with money (Mat 28:11–15), #1993; '),
 '03-one-inner-person-v2-20261002.md': ('03-one-inner-person-v3-20261009.md', 'v3: "not far from the kingdom" (Mar 12:34), #1993; '),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v40-20261009.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v40-20261009.md', 'wa-essay-spirit-soul-body-claim-register-v41-20261009.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)
