"""M18 x M72 shared verses (#1993, handoff item H), 2026-10-12: claim register v47 -> v48, narrative index rows,
triage CSV v2 (decisions after the weave). Run once, after m18-m72-shared-weave-v1-20261012.py. Writes files; no DB access."""
import csv, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))

SEC = '''## Strand updates — desire (M18) × authority (M72): the 51 never-read shared verses, read by role (2026-10-12, #1993 item H)

**Researcher, verbatim:** *"next the M18 strand overview, item F, lists M72 (Authority & Dominion), which shares 182 verses with M18, as recorded so it isn't lost."*; *"weave §9 as proposed"*.

**Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Of the 182 shared verses, 131 were decided earlier in the M18 strand. The 51 never read: 6 read, 8 carried, 8 read by their acts, 23 forward (OT-97; seven to M72 itself, OT-98), 6 data. Records: `../../Clusters/M18 - desire-longing/m18-m72-shared-reading-v1-20261012.md`, `m18-m72-shared-triage-v2-20261012.csv`.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.7 (v26) | *Whose measure*: "The king's pleasure, asked for" (Neh 2:4–8; Est 1:17–19; 5:3–4; 9:12–13; 7:3); *Others around a choice*: Mal 2:17–3:2 beside Isa 58:2 | Added; I read marked |
| 13.1 (v21) | *Delight*: "His delight claimed for evildoers" (Mal 2:17; 3:3) | Added |
| 10.6 (v21) | *Coveting*: David (2Sa 11:1–4; 12:9), no desire word named; *Wanting speaks, and drives thinking*: 2Sa 18:27, 29, 33 | Added; I read marked |
| 10.11 (v7) | *Hiding what I hold*: "It can all be shown" (Isa 39:2–6; 2Ki 20:13; 2Ch 32:31) | Added |
| 10.2 (v17) | a refusal to hear standing on a reading of the past (Jer 44:16–18) | Added; I read marked |
| 10.4 (v11) | *It reckons*: Amos 6:1–3 | Added |
| 10.5 (v21) | *Speech is heard*: the chief baker (Gen 40:16, 19); *The oath*: Shimei (1Ki 2:38, 43) | Added |
| Ch 11 (v29) | §1 *Others steal, sway and turn hearts*: Absalom's words (2Sa 15:3) with 15:6 | Changed (words added) |

**Quote check:** 36 inserted quotations checked against the ESV in iba.db, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v47-20261012.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v47)') == 1
t = t.replace('checked against the inner-seat reading (v47)', 'checked against the inner-seat reading (v48)', 1)
assert t.count('**Date:** 2026-09-30 (v47:') == 1
t = t.replace('**Date:** 2026-09-30 (v47:', '**Date:** 2026-09-30 (v48: 2026-10-12, M18 × M72 shared verses: the 51 never read, read by role, 8 chapters, #1993 item H; v47:', 1)
anchor = '## Strand updates — desire (M18), group C: will, willing, acceptance'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v48-20261012.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v48 written; v47 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
N = 'M18 × M72, #1993 item H; '
notes = {
 '10-02-knowing-and-hearing-v16-20261012.md': ('10-02-knowing-and-hearing-v17-20261012.md', 'v17: Jer 44:16–18, ' + N),
 '10-04-thinking-v10-20261009.md': ('10-04-thinking-v11-20261012.md', 'v11: Amos 6:2, ' + N),
 '10-05-speaking-v20-20261012.md': ('10-05-speaking-v21-20261012.md', 'v21: Gen 40:16; Shimei 1Ki 2:38, ' + N),
 '10-06-wanting-v20-20261012.md': ('10-06-wanting-v21-20261012.md', 'v21: David 2Sa 11:2–4; 2Sa 18:27, ' + N),
 '10-07-choosing-and-setting-direction-v25-20261012.md': ('10-07-choosing-and-setting-direction-v26-20261012.md', 'v26: the king\'s pleasure, asked for; Mal 3:1, ' + N),
 '10-11-hiding-and-disclosing-v6-20261012.md': ('10-11-hiding-and-disclosing-v7-20261012.md', 'v7: Hezekiah shows all, ' + N),
 '11-patterns-of-the-inner-life-v28-20261012.md': ('11-patterns-of-the-inner-life-v29-20261012.md', 'v29: 2Sa 15:3, ' + N),
 '13-01-divine-v20-20261012.md': ('13-01-divine-v21-20261012.md', 'v21: his delight claimed for evildoers (Mal 2:17; 3:3), ' + N),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    assert t.count(pat) == 1, old
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v47-20261012.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v47-20261012.md', 'wa-essay-spirit-soul-body-claim-register-v48-20261012.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)

p = os.path.join(HERE, 'm18-m72-shared-triage-v1-20261012.csv')
rows = list(csv.DictReader(open(p, encoding='utf-8-sig')))
for r in rows:
    if r['decision'] == 'read':
        r['decision'] = 'read and woven'
    elif r['decision'] == 'no-carrier':
        r['decision'] = 'no-carrier, read and placed'
    elif r['reference'] == '2Sa 15:3':
        r['decision'] = 'carried, words added'
out = os.path.join(HERE, 'm18-m72-shared-triage-v2-20261012.csv')
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
shutil.move(p, os.path.join(HERE, 'archive', os.path.basename(p)))
print('triage CSV v2 written; v1 archived')
