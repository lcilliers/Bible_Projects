"""M18 group C (#1993, item F), 2026-10-12: claim register v46 -> v47, narrative index rows, OT-97 (group C forward marks),
triage CSV v2 (final decisions after reading). Run once. Writes files; no DB access."""
import csv, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ESSAY = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body'))
OTR = os.path.normpath(os.path.join(HERE, '..', '..', 'cross-cluster-web', 'open-threads-register.md'))

SEC = '''## Strand updates — desire (M18), group C: will, willing, acceptance, read by role (2026-10-12, #1993 item F)

**Researcher, verbatim:** *"remove the worktree, then proceed to group C"*; *"continue with batches 2 and 3, then weave all"*.

**Method:** `Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md` (rule 73). Of the 280 verses left after the pull filter, 164 are read in 23 phenomenon groups, 48 are already carried, 29 are marked forward (OT-97), 14 whose act carries no M-code are read by their acts, and 25 are data. Records: `../../Clusters/M18 - desire-longing/m18-group-C-reading-batch1-v1-20261012.md`, `m18-group-C-reading-batch2-3-v1-20261012.md`, `m18-group-C-role-triage-v2-20261012.csv`.

**Original claims changed:** none.

| Section | Added or changed | Verdict |
|---|---|---|
| 10.7 (v25) | *Willing*: the will asked for; a will redirected; refusals extended (feast, plea, reign, threat, urging; the gall; a finger not lifted; being gathered; a light for a while); wanting to go back; content to stay; Pilate, Felix and Festus; Herod's oath; the will to harm stopped short, Hos 5:11; the willing heart extended (1Ch 29, Ezra, Judg 5:2, Neh 11:2, 2Co 8:10–12, 19); the will made absolute seen from below (Dan 11, Neh 9, Mat 17:12); a will that cannot carry itself out (Rom 7:15–21); doing the will of God. *Planning*: Luk 14:28; Paul's plans under God's will. *What follows a choice*: Esau too late (Heb 12:16–17) | Added; I read marked |
| 10.6 (v20) | *Aimed at God*: wanting to see Jesus; *Unmet*: Luk 16:26; *Wanting and death*: Job 6:8–10 | Added |
| 10.9 (v20) | Psa 145:19; the leper's plea to the will (Mat 8:2–3) | Added |
| 10.10 (v22) | another's will met by giving, and the golden rule (Mat 5:40–42; 7:12; Luk 6:31); Act 14:13–15; Luk 9:53–56; Job 6:28–29 | Added; I read marked |
| 10.11 (v6) | Jesus not able to be hidden (Mar 7:24–25; 9:30–31) | Added |
| 10.12 (v6) | *"Fear not"*: Mar 6:48–50; Joh 6:21 | Added |
| 10.5 (v20) | Mat 27:43 beside Psa 22:8; 1Ti 1:5–7 | Added |
| 10.2 (v16) | willing to receive a word (Mat 11:14–15; Act 17:11–12; 1Ti 1:15); 2Pe 3:3, 5 | Added; I read marked |
| 13.1 (v20) | *Choosing*: Mar 3:13–14; *Willing*: the Son's will in its own words (the leper, Jerusalem, Luk 12:49–50, Joh 17:24, Mat 20:14–15), the Father's will (Rev 4:11, 1Co 12:18, Col 1:27, Gal 1:4, 1Ti 2:4, Mat 18:14); *Delight*: Mat 9:13 and 12:7 with Hos 6:6, what makes an offering accepted, his favor | Added; I read marked |
| 13.2 (v4) | Psa 103:20–21 | Added |
| 13.3 (v2) | first content: the devil's will (Luk 4:6–8; 2Ti 2:25–26) | Added |
| Ch 11 (v28) | §4 *What changes the character*: Whose will, and whether it can carry itself out | Added |

**Quote check:** 201 inserted quotations checked against the ESV in iba.db, 0 failures.
'''

src = os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v46-20261011.md')
t = open(src, encoding='utf-8').read()
assert t.count('checked against the inner-seat reading (v46)') == 1
t = t.replace('checked against the inner-seat reading (v46)', 'checked against the inner-seat reading (v47)', 1)
assert t.count('**Date:** 2026-09-30 (v46:') == 1
t = t.replace('**Date:** 2026-09-30 (v46:', '**Date:** 2026-09-30 (v47: 2026-10-12, M18 group C (will, willing) read by role: 164 in 23 groups, 14 by their acts, 29 forward, 12 chapters, #1993 item F; v46:', 1)
anchor = '## Strand updates — desire (M18), group B: the 94 remaining bucket-1 verses'
assert t.count(anchor) == 1
t = t.replace(anchor, SEC.rstrip('\n') + '\n\n' + anchor)
open(os.path.join(ESSAY, 'wa-essay-spirit-soul-body-claim-register-v47-20261012.md'), 'w', encoding='utf-8').write(t)
shutil.move(src, os.path.join(ESSAY, 'archive', os.path.basename(src)))
print('claim register v47 written; v46 archived')

idx = os.path.join(ESSAY, 'inner-being-narrative', '00-index-and-status-v1-20260930.md')
t = open(idx, encoding='utf-8').read()
N = 'M18 group C (will) by role, #1993; '
notes = {
 '10-02-knowing-and-hearing-v15-20261009.md': ('10-02-knowing-and-hearing-v16-20261012.md', 'v16: willing to receive a word; 2Pe 3:5, ' + N),
 '10-05-speaking-v19-20261011.md': ('10-05-speaking-v20-20261012.md', 'v20: Mat 27:43; 1Ti 1:5–7, ' + N),
 '10-06-wanting-v19-20261011.md': ('10-06-wanting-v20-20261012.md', 'v20: wanting to see Jesus; Luk 16:26; Job 6:8–10, ' + N),
 '10-07-choosing-and-setting-direction-v24-20261011.md': ('10-07-choosing-and-setting-direction-v25-20261012.md', 'v25: *Willing* widened (Rom 7:15–21; doing the will of God; the will asked; redirected; going back; Herod; willing heart), Paul\'s plans, ' + N),
 '10-09-relating-to-god-v19-20261011.md': ('10-09-relating-to-god-v20-20261012.md', 'v20: Psa 145:19; the leper\'s plea, ' + N),
 '10-10-relating-to-others-v21-20261011.md': ('10-10-relating-to-others-v22-20261012.md', 'v22: golden rule; Act 14:13; Luk 9:54; Job 6:28, ' + N),
 '10-11-hiding-and-disclosing-v5-20261011.md': ('10-11-hiding-and-disclosing-v6-20261012.md', 'v6: Jesus not able to be hidden, ' + N),
 '10-12-fear-v5-20261009.md': ('10-12-fear-v6-20261012.md', 'v6: Mar 6:48–50; Joh 6:21, ' + N),
 '11-patterns-of-the-inner-life-v27-20261011.md': ('11-patterns-of-the-inner-life-v28-20261012.md', 'v28: §4 whose will, ' + N),
 '13-01-divine-v19-20261011.md': ('13-01-divine-v20-20261012.md', 'v20: the Son\'s and the Father\'s will; offerings accepted; his favor, ' + N),
 '13-02-angels-v3-20261009.md': ('13-02-angels-v4-20261012.md', 'v4: Psa 103:20–21, ' + N),
 '13-03-other-spirits-v1-20261007.md': ('13-03-other-spirits-v2-20261012.md', 'v2: first content, the devil\'s will, ' + N),
}
for old, (new, note) in notes.items():
    pat = '`' + old + '` ('
    if t.count(pat) != 1:
        pat2 = '`' + old + '`'
        assert t.count(pat2) == 1, old
        t = t.replace(pat2, '`' + new + '` (' + note.rstrip('; ') + ')', 1)
        continue
    t = t.replace(pat, '`' + new + '` (' + note, 1)
n = t.count('wa-essay-spirit-soul-body-claim-register-v46-20261011.md')
t = t.replace('wa-essay-spirit-soul-body-claim-register-v46-20261011.md', 'wa-essay-spirit-soul-body-claim-register-v47-20261012.md')
open(idx, 'w', encoding='utf-8').write(t)
print('index updated; claim register pointers replaced:', n)

# triage CSV v2: final decisions after reading
p = os.path.join(HERE, 'm18-group-C-role-triage-v1-20261012.csv')
rows = list(csv.DictReader(open(p, encoding='utf-8-sig')))
CHANGE = {
 'Est 9:5': ('forward', 'M01', 'read: the Jews did as they pleased after the fear of Mordecai fell (9:3); carried with M01'),
 '2Th 3:10': ('no-carrier, forward', 'work (no M-code)', 'read: a rule on work and support; for the strand that reads work'),
 'Luk 19:27': ('read, data within passage', '', 'carried by Luk 19:14'),
 'Joh 9:27': ('read, data within passage', '', 'irony toward those who would not listen'),
 'Rev 11:5': ('read, data within passage', '', 'apocalyptic protection of the witnesses'),
 '1Ti 4:9': ('read, data within passage', '', 'formula repeated from 1:15'),
 'Deu 33:16': ('read, data within passage', '', 'formula of tribal blessing'),
 'Deu 33:23': ('read, data within passage', '', 'formula of tribal blessing'),
 'Isa 60:7': ('read, data within passage', '', 'acceptance in the restored worship'),
}
fields = list(rows[0].keys())
for r in rows:
    if r['reference'] in CHANGE:
        d, g, note = CHANGE[r['reference']]
        r['decision'], r['note'] = d, note
        if g: r['group_or_forward'] = g
    elif r['decision'] == 'no-carrier':
        r['decision'] = 'no-carrier, read and placed'
    elif r['decision'] == 'read':
        r['decision'] = 'read and woven'
out = os.path.join(HERE, 'm18-group-C-role-triage-v2-20261012.csv')
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
shutil.move(p, os.path.join(HERE, 'archive', os.path.basename(p)))
fwd = [r for r in rows if r['decision'].startswith('forward') or r['decision'] == 'no-carrier, forward']
print('triage CSV v2 written; v1 archived; forward rows:', len(fwd))

t = open(OTR, encoding='utf-8').read()
a = '| M18 group B role triage (#1993, 2026-10-11) '
assert t.count(a) == 1
add = ('**Group C (will, willing; 2026-10-12):** ' + str(len(fwd)) + ' more verses in `../Clusters/M18 - desire-longing/m18-group-C-role-triage-v2-20261012.csv` '
       '(decision `forward`): the will word qualifies another cluster\'s characteristic, for example "called by the will of God" (M42), '
       '"desiring to justify himself" (M26), "I am unwilling to send them away hungry" (M50), "Rachel refused to be comforted" (M03), and Est 9:5 (M01). '
       '2Th 3:10 waits for the strand that reads work (no M-code). ')
t = t.replace(a, add + a)
a2 = 'filter the CSV on `forward_to` '
assert t.count(a2) == 1
t = t.replace(a2, 'filter the CSVs on `forward_to` / `group_or_forward`; group C adds M42, M08, M03, M45, M13, M43, M56, M79, M80, M12, M51, M05, M15, M50, M46, M26, M21, M69, M16, M83, M09, M32, M34, M01 ')
open(OTR, 'w', encoding='utf-8').write(t)
print('OT-97 updated')
