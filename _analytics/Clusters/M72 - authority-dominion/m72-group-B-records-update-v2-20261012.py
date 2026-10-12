"""M72 group B (#1998), 2026-10-12, second records pass: the Ch 11 retitle and the activity-chapter weave.
Claim register v49 -> v50; narrative index rows (13, incl. the Ch 11 rename); open threads: OT-16 and OT-98 closed
for M72, OT-97 gains the 47 M72 forward marks, OT-100 notes the title answer. Run once; no DB access."""
import csv, os, shutil
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))
OTR = os.path.normpath(os.path.join(HERE, '..', '..', 'cross-cluster-web', 'open-threads-register.md'))

SEC = '''## Strand updates — authority (M72), group B: Ch 11 retitled, and the remaining placements written (2026-10-12, #1998)

**Researcher, verbatim:** *"Ch 11 as a whole — the title should not carry any weight in the analysis, it is almost a collection of different inner being elements that does not have another home."* Then: *"'11. Other sides of the inner being' and update the opening paragraph.  you can proceed with writing to the narrative any outstanding parts of M72"*.

**Placement rule:** each verse goes where the act that moves in it belongs. Authority is the standing that act moves in (`../../Clusters/M72 - authority-dominion/m72-group-B-weave-record-v1-20261012.md` §2). Script: `m72-group-B-weave-activities-v1-20261012.py`.

**Original claims changed:** Ch 11's title and opening. The title was *"Patterns of the inner life"*, and the opening said *"certain patterns kept coming back"*. Both claimed a link between the sections that the chapter does not establish. They are restated as a gathering of what has no other home.

| Section | Added or changed | Verdict |
|---|---|---|
| Ch 11 (v31, renamed `11-other-sides-of-the-inner-being`) | Title *Other sides of the inner being*; opening restated; §7 working note updated | Restated |
| 10.10 (v23) | *The fear of God and the weak*: Lev 25:46, 53, 55; 2Sa 23:3; Eph 6:9. *Fear that arrives with a person*: Est 9:1–2. New **Holding authority over another** (at its worst: Eze 34, Pro 28:15–16, Ecc 8:9; from money, a decree, given to each other; in the church, 1Ti 2:11–14; turned round, Luk 22:24–27, 1Pe 5:2–5, 2Co 1:23–24; under it, Tit 3:1–4, Judg 15:11–12). New **A right set aside for another** (1Co 9:4–19; 2Th 3:9; 1Co 8:9–13; 2Co 10:8–9; 13:9–10) | Added; I read marked |
| 10.9 (v21) | New **Kept from what would rule** (Psa 19:12–13; 119:133–134); **Under rule, and longing for his** (Neh 9:27–28; Psa 106:41, 44; Lam 5:8; Hab 1:13–14; Isa 63:19); **Knowing who rules** (Mat 8:9–10; Hos 8:2, 4; Dan 4:26–27; Psa 8:4, 9; Jer 30:21; Hos 12:4, 6) | Added |
| 10.12 (v7) | Lev 26:16–17; Luk 12:5, 7; Pilate's fear and his claim (Joh 19:8–12); fear of the crowd (Mat 21:25–27; Luk 20:6); Jer 51:46; Psa 49:16; Dan 6:23, 26 | Added; I read marked |
| 10.7 (v27) | *Convinced that I ought* (Act 26:9–10, 14); *Rule offered, refused, and sought* (Judg 8:22–23; Dan 5:17; Judg 9:2–3, 5) | Added |
| 10.6 (v22) | Simon (Act 8:18–23); Ecc 5:19–20; Gen 37:8; 42:6, 9 | Added |
| 10.4 (v12) | answers weighed by their cost (Mat 21:25–27) | Added |
| 10.11 (v8) | an answer held back (Mat 21:27) | Added |
| 10.3 (v7) | Num 16:13; Tit 3:1, 3; Gen 42:9 | Added |
| 10.1 (v20) | joy turned (Luk 10:17, 20–21) | Added |
| 10.13 (v7) | Num 16:15; Act 26:10–11 | Added |
| Ch 12 (v20) | Dan 4:30–31, 26 beside 5:20 | Added |
| Ch 14 (v15) | New **Sin's rule ended** (Rom 6:12–14, 16) | Added; I read marked |

**Quote check:** every inserted quotation was checked against the ESV in iba.db, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v49-20261012.md')
t = open(src, encoding='utf-8').read()
t = t.replace('checked against the inner-seat reading (v49)', 'checked against the inner-seat reading (v50)', 1)
assert t.count('**Date:** 2026-09-30 (v49:') == 1
t = t.replace('**Date:** 2026-09-30 (v49:', '**Date:** 2026-09-30 (v50: 2026-10-12, Ch 11 retitled *Other sides of the inner being*; M72 group B remaining placements in 10.x, Ch 12, Ch 14, #1998; v49:', 1)
anchor = '## Strand updates — authority (M72), group B: current thoughts into Ch 11'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v50-20261012.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v50 written; v49 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
N = 'M72 group B, #1998; '
notes = {
 '11-patterns-of-the-inner-life-v30-20261012.md': ('11-other-sides-of-the-inner-being-v31-20261012.md', 'v31: **retitled *Other sides of the inner being*** and opening restated (a gathering of what has no other home), #1998; v30: '),
 '10-10-relating-to-others-v22-20261012.md': ('10-10-relating-to-others-v23-20261012.md', 'v23: new *Holding authority over another* and *A right set aside for another*; Lev 25:46–55; 2Sa 23:3; Eph 6:9; Est 9:1, ' + N),
 '10-09-relating-to-god-v20-20261012.md': ('10-09-relating-to-god-v21-20261012.md', 'v21: new *Kept from what would rule*, *Under rule, and longing for his*, *Knowing who rules*, ' + N),
 '10-12-fear-v6-20261012.md': ('10-12-fear-v7-20261012.md', 'v7: Lev 26:17; Luk 12:5; Pilate; fear of the crowd; Jer 51:46; Dan 6:26, ' + N),
 '10-07-choosing-and-setting-direction-v26-20261012.md': ('10-07-choosing-and-setting-direction-v27-20261012.md', 'v27: *Convinced that I ought*; *Rule offered, refused, and sought*, ' + N),
 '10-06-wanting-v21-20261012.md': ('10-06-wanting-v22-20261012.md', 'v22: Simon (Act 8:18–23); Ecc 5:19–20; Gen 37:8, ' + N),
 '10-04-thinking-v11-20261012.md': ('10-04-thinking-v12-20261012.md', 'v12: Mat 21:25–27, ' + N),
 '10-11-hiding-and-disclosing-v7-20261012.md': ('10-11-hiding-and-disclosing-v8-20261012.md', 'v8: Mat 21:27, ' + N),
 '10-03-remembering-and-forgetting-v6-20261009.md': ('10-03-remembering-and-forgetting-v7-20261012.md', 'v7: Num 16:13; Tit 3:3; Gen 42:9, ' + N),
 '10-01-feeling-v19-20261011.md': ('10-01-feeling-v20-20261012.md', 'v20: joy turned (Luk 10:17–21), ' + N),
 '10-13-anger-v6-20261009.md': ('10-13-anger-v7-20261012.md', 'v7: Num 16:15; Act 26:10–11, ' + N),
 '12-when-the-inner-being-goes-wrong-v19-20261009.md': ('12-when-the-inner-being-goes-wrong-v20-20261012.md', 'v20: Dan 4:30 beside 5:20, ' + N),
 '14-made-new-v14-20261009.md': ('14-made-new-v15-20261012.md', 'v15: new *Sin\'s rule ended* (Rom 6:12–16), ' + N),
}
for old, (new, note) in notes.items():
    key = '`' + old + '` ('
    assert t.count(key) == 1, old
    t = t.replace(key, '`' + new + '` (' + note, 1)
open(idx, 'w', encoding='utf-8').write(t)
print('index rows updated:', len(notes))

rows = list(csv.DictReader(open(os.path.join(HERE, 'm72-group-B-role-triage-v1-20261012.csv'), encoding='utf-8-sig')))
fwd = Counter(r['group_or_forward'] for r in rows if r['decision'] == 'forward')
fwd_txt = ', '.join(f'{k} ({v})' if v > 1 else k for k, v in fwd.most_common())

lines = open(OTR, encoding='utf-8').read().split('\n')


def edit(ot, fn):
    i = [k for k, l in enumerate(lines) if l.startswith(f'| {ot} |')]
    assert len(i) == 1, ot
    cells = lines[i[0]].split(' | ')
    fn(cells)
    lines[i[0]] = ' | '.join(cells)


def ot16(c):
    c[-1] = c[-1].rstrip(' |') + '; **closed for M72 (#1998, 2026-10-12):** the 4 B verses are decided in `../Clusters/M72 - authority-dominion/m72-group-B-role-triage-v1-20261012.csv`: Pro 16:32 confirmed (Ch 6, 10.13, Ch 11 §7); Isa 14:6 carried (10.10); Psa 59:13 God\'s character (13.1 *Ruling*); Eze 19:14 forward to M03 (its M02 tag is "dirge", and the verse holds no anger) |'


def ot98(c):
    c[-1] = c[-1].rstrip(' |') + '; **closed for M72 (#1998, 2026-10-12):** the 18 B verses are decided and placed (group B triage CSV; weave scripts `m72-group-B-weave-*`); the other 164 hold only qualifier, God\'s-character or hand words under the scope ruling |'


def ot97(c):
    c[1] = c[1] + (f' **M72 group B (2026-10-12, #1998):** 47 more in `../Clusters/M72 - authority-dominion/m72-group-B-role-triage-v1-20261012.csv` (decision `forward`). In each, rule or authority is only the setting, outcome or ground of another cluster\'s act. Examples: the people rejoice or groan under their rulers (Pro 29:2), rule as the outcome of diligence (Pro 12:24), and the crowds astonished at his authority (Mat 7:29). These were triaged before the correction recorded in OT-100, so they are to be read again with it.')
    c[3] = c[3] + f'; the M72 group B marks add {fwd_txt}'


def ot100(c):
    c[-1] = c[-1].rstrip(' |') + '; title answered 2026-10-12 (researcher: *"Ch 11 as a whole — the title should not carry any weight in the analysis, it is almost a collection of different inner being elements that does not have another home"*): Ch 11 renamed *Other sides of the inner being* (v31) and its opening restated. The meaning of authority stays open |'


for ot, fn in (('OT-16', ot16), ('OT-98', ot98), ('OT-97', ot97), ('OT-100', ot100)):
    edit(ot, fn)
open(OTR, 'w', encoding='utf-8').write('\n'.join(lines))
print('open threads updated; forward:', fwd_txt)
