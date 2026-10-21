"""OT-05 (#2006): group the body / resurrection / glory verses by sense, for the researcher to choose
which groups to read (read-only; a working aid, not a reading).

Usage: python life-death-ot05-grouping-v1-20261014.py CROSSCHECK.csv Q4PULL.csv OUT.csv
CROSSCHECK is the output of life-death-claim-register-crosscheck-v2-20261013.py; Q4PULL is the
2026-10-02 Q4 ledger pull (marks the verses that ledger read).
Each verse gets one word family (first match in FAMILY order) and one sense group, by keywords in
its ESV text. The groups are mechanical: a verse can sit in the wrong group, and the reading decides.
Output columns: reference, family, group, strongs, cited, chapters, claim, in_q4_pull, esv_text.
"""
import csv, re, sqlite3, sys
from collections import defaultdict

cross, q4pull, out = sys.argv[1:4]
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
text = dict(db.execute("SELECT reference, text FROM verse WHERE deleted = 0"))

FAMILY = [  # (family, Strong's) -- the changed-body words first, then resurrection, body, glory
    ('A changed body', {'G0861', 'G0862', 'G0110', 'G5349', 'G5356', 'G2349', 'G3339', 'G4832', 'G3345',
                        'G5591', 'G4636', 'G1902', 'G4984', 'G1746'}),
    ('R raise, rise', {'G0386', 'G1454', 'G1815', 'G4891', 'G1825', 'G1453', 'G0450'}),
    ('B body', {'G4983'}),
    ('G glory', {'G1391', 'G1392'}),
]

def has(t, *pats):
    return any(re.search(p, t, re.I) for p in pats)

def group(fam, t):
    if fam == 'A changed body':
        if has(t, r'spiritual body|natural body|perishable|imperishable|mortal|immortal|put on|swallowed|tent|clothed|further clothed|be changed|transform.{0,40}body|lowly body|conformed to the image|putting it on|naked'):
            return 'A1 the body changed, mortal and imperishable, tent and clothing'
        if has(t, r'natural person|the natural|unspiritual|devoid of the Spirit'):
            return 'A6 natural (psychikos): set against the spiritual'
        if has(t, r'transfigured|transformed|disguise|renewal of your mind|being transformed'):
            return 'A2 transformed: transfiguration, mind, disguise'
        if has(t, r'clothed|put on|wear|dressed|garment|robe|clothing|sackcloth|armor'):
            return 'A3 put on: clothing, put on Christ, the new self'
        if has(t, r'corrupt|perish'):
            return 'A4 corruption and incorruptible in other settings'
        return 'A5 other'
    if fam == 'R raise, rise':
        if has(t, r'Sadducee|no resurrection|resurrection of the dead\?|mocked|in the resurrection.{0,40}wife|whose wife'):
            return 'R1 the resurrection debated or denied'
        if has(t, r'wake from sleep|Awake, O sleeper|Wake up from your drunken'):
            return 'R9 wake: a call to the living'
        if has(t, r'with him|with Christ|together with'):
            return 'R2 raised with Christ, now'
        if has(t, r'Lazarus|little girl|daughter|Tabitha|Dorcas|young man|widow|Eutychus|the girl|bier|bones of Elisha|bodies of the saints|prophets of old|John the Baptist has been raised|John.{0,30}raised'):
            return 'R3 the dead raised in the accounts'
        if has(t, r'third day|raised (him|Jesus|Christ|the Lord)|he has risen|has been raised|was raised|Christ.{0,40}(raised|risen)|risen from the dead|rose from the dead|raised from the dead|after (his|I am) raised|resurrection of (Jesus|Christ)|resurrection of the Christ|has risen|risen indeed|raised up his servant|raising Jesus|God raised up|whom God raised|raised for our justification|raised in glory|raised in power'):
            return 'R4 Christ raised'
        if has(t, r'resurrection|the dead|raise (us|you|them|him) up|raised imperishable|at the last day|from the dead|will rise|shall rise'):
            return 'R5 the dead raised: the coming resurrection'
        if has(t, r'rise up against|rose up against|nation will rise|false prophets|false christs|rise in judgment|arise'):
            return 'R6 rise up: against, in judgment, a nation or prophet'
        if has(t, r'raised you up|raise up (a|for|children|his|offspring)|raised up (a|for|David|judges|Israel)|raise up children|raise it up|raised up for'):
            return 'R7 raise up: a person, offspring, the temple'
        return 'R8 get up, stand, wake: the ordinary act'
    if fam == 'B body':
        if has(t, r'one body|body of Christ|his body, the church|members of (his|the) body|members one of another|the body is one|head of the body|body, the church|the whole body|baptized into one body|one Spirit|one member|parts of the body|belong to the body|which is his body|church, his body'):
            return 'B1 the body of Christ: the church'
        if has(t, r'took bread|this is my body|my body|body of the Lord|body of Jesus|asked for the body|the body of Jesus|anoint my body|took the body|body was laid|did not find the body|through the body of Christ|offering of the body|in his body on the tree|body of his flesh|body you have prepared|discerning the body|guilty concerning the body|did not find his body|granted the corpse'):
            return 'B2 Jesus\' body: the supper, the cross, the tomb'
        if has(t, r'raised|spiritual body|resurrection|redemption of our bodies|mortal body|mortal bodies|lowly body|glorious body|at home in the body|away from the body|body that is to be|gives it a body|heavenly bodies'):
            return 'B3 the body raised, redeemed, away from it'
        if has(t, r'soul|spirit|heart|mind|sin|passions|desire|temple|lamp|eye|immorality|sexual|present your bodies|discipline|members|flesh|lust|honor|holy|anxious|worry|kill the body|deeds of the body|whole body|bridle|tongue|marks|bear|body of death|carrying in the body|in the body or out|judgment seat|bodily presence|glorify God in your body|over her own body|their own bodies|needed for the body|felt in her body'):
            return 'B4 the body with the inner being: soul, spirit, sin, temple, eye, members'
        return 'B5 bodies otherwise: the dead, the healed, things'
    if fam == 'G glory':
        if has(t, r'glory that is to be|be glorified with|glorified with him|eternal glory|hope of (the )?glory|revealed in glory|into glory|in glory|bring many sons to glory|glory of the children|glorified\.|those whom he justified he also glorified|weight of glory|unfading crown of glory|glory to be revealed|share in.{0,20}glory|obtain the glory|called you to his own glory|called (us|you).{0,30}glory|from one degree of glory|with him in glory|for our glory|kingdom and glory|sons to glory|result in praise and glory|glory and honor and peace|which is your glory|glory of God\.?$'):
            return 'G1 glory to come for those who believe'
        if has(t, r'glory from|glory of man|from men|glory from one another|own glory|seek glory|their glory is in their shame|glory of man|vainglory|empty glory|glory of the world|all the kingdoms|Solomon in all his glory|glory of (their|the) (kingdom|nations)|glory of the kings|her glory|glorified by all|be honored|is honored|glorified herself|glory in their shame|our glory and joy|praised by others|their glory|all its glory|magnify my ministry|you will be honored|honor and dishonor|glorious ones|glories of|blaspheme the glor'):
            return 'G2 glory among people, and of the world'
        if has(t, r'give glory|gave glory|giving glory|glorified God|glorifying God|glorify God|glorify your Father|to him be|be glory|glory forever|glory to God|glory in the highest|praising|to the glory of God|for the glory of God|glorify him|to whom be|to the praise|give praise to God|praised God|glorified the God|glorify the God|worthy are you|receive glory|give him glory|blessing and glory|glory and power belong|Father may be glorified|Father is glorified|glorifying the word|honor him as God|bring their glory|word of the Lord may'):
            return 'G3 glory given to God'
        if has(t, r'Son of Man|glorify (the|your) Son|glorify me|glorified (the Son|Jesus|his servant)|his glory, glory as of|the Lord of glory|Christ.{0,40}glory|glory of Christ|my glory|his glorious|in (his|the) glory of (his|the) Father|throne of his glory|glorified in him|glorify you|glorified you|glory of (the|his) Son|glory of God in the face|crowned with glory|more glory than Moses|Jesus was glorified|I am glorified in them|in your glory|subsequent glories|exalt himself|Spirit of glory'):
            return 'G4 the Son\'s glory'
        if has(t, r'glory of (the Lord|God|our God|his grace)|his glory|the glory|glory of the (immortal|incorruptible)|God of glory|Father of glory|majestic glory'):
            return 'G5 God\'s glory'
        return 'G6 other'
    return ''

q4 = {r[0] for r in csv.reader(open(q4pull, encoding='utf-8-sig'))}
rows = defaultdict(lambda: {'st': set(), 'ch': set(), 'claim': False})
for r in csv.DictReader(open(cross, encoding='utf-8-sig')):
    d = rows[r['reference']]
    d['st'].update(s.strip() for s in re.split(r'[;,]', r['strongs_in_verse']) if s.strip())
    if r['chapter']:
        d['ch'].add(r['chapter'])
    if r['claims_sourcing_verse']:
        d['claim'] = True

out_rows = []
for ref in rows:  # the cross-check is already in canonical order
    d = rows[ref]
    codes = {s.split(':')[0] for s in d['st']}
    fam = next(f for f, ss in FAMILY if codes & ss)
    t = text.get(ref, '')
    out_rows.append([ref, fam, group(fam, t), '; '.join(sorted(d['st'])), 'Y' if d['ch'] else '',
                     '; '.join(sorted(d['ch'])), 'Y' if d['claim'] else '', 'Y' if ref in q4 else '', t])

with open(out, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'family', 'group', 'strongs', 'cited', 'chapters', 'claim', 'in_q4_pull', 'esv_text'])
    w.writerows(out_rows)

summary = defaultdict(lambda: [0, 0, 0, 0])
for r in out_rows:
    s = summary[r[2]]
    s[0] += 1; s[1] += r[4] == 'Y'; s[2] += r[6] == 'Y'; s[3] += r[7] == 'Y'
print('group | verses | cited | claim | in Q4 pull')
for g in sorted(summary):
    print(g, '|', ' | '.join(map(str, summary[g])))
print(len(out_rows), 'verses ->', out)
