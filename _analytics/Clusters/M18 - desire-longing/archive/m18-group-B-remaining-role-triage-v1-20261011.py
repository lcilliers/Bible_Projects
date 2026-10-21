"""Item F (#1993), group B: role triage of the 94 remaining bucket-1 verses, by the reading-by-role
guide (Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md, cfg_behaviour_rule 73).

Researcher (chat 2026-10-11, verbatim): "you will not blanketly read every verse, but will optimise the
reading by first assessing the status of the M18 M-code, if it is supportive, for another cluster's
reading then the reading is marked forward for when that cluster is read, else if the M-code is central
to the verse, then read in in deapth and in context."

Inputs (rule 71, no DB query): m18-group-B-bucket1-remaining-v1-20261009.md (the 94),
m18-group-B-pull-v1-20261009.csv (other_mcodes). Narrative citations were taken from the current
chapters with the crossref v3 parser (see the .md record). Decisions below are per verse, read from the
verse text and, for the central verses, its passage (reading: m18-group-B-remaining-central-reading-v1).

decision values:
  read            - the M18 word carries the verse's main IB operation (characteristic): read in depth
  forward         - the M18 word is a qualifier of another characteristic whose M-code is in the verse:
                    marked forward to that cluster's reading
  forward-carried - as forward, and the verse is already placed in the narrative by its operation
  no-carrier      - the M18 word is a qualifier, but the operation it qualifies carries no M-code in the
                    verse, so no cluster reading will bring it back (for the researcher)
  data            - the M18 word is standalone (no inner-being sense: matter, a stone, a name, a day)
Output: m18-group-B-remaining-role-triage-v1-20261011.csv
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: list(csv.DictReader(open(os.path.join(HERE, f), encoding='utf-8-sig')))
pull = {r['reference']: r for r in rd('m18-group-B-pull-v1-20261009.csv')}
md = open(os.path.join(HERE, 'm18-group-B-bucket1-remaining-v1-20261009.md'), encoding='utf-8').read()
rows94 = re.findall(r'^\| \d+ \| ([^|]+?) \| (\S+) "([^"]*)"', md, re.M)

# ref: (role, decision, forward_to, route, main IB operation / note)
T = {
 # --- noun (delight, pleasure) ---
 '2Pe 2:13': ('qualifier', 'forward', 'M28; M58', 'B', 'suffering the wage of wrongdoing; "count it pleasure" measures the reveling (M28), strengthened by deceptions (M14). Worked case in the guide.'),
 'Jam 4:3': ('characteristic', 'read', '', 'B', 'the passions turn the asking (M21) to their own spending; 4:1 the passions at war within'),
 'Ecc 8:6': ('standalone', 'data', '', 'C', '"every matter": no inner sense; the verse is man\'s trouble heavy on him (M24)'),
 '1Ki 10:13': ('qualifier', 'no-carrier', '', 'B', '"all that she desired" measures Solomon\'s giving; already in 10.6 Precious, placed by the queen giving after she had seen'),
 '2Ch 9:12': ('qualifier', 'no-carrier', '', 'B', 'parallel of 1Ki 10:13: the measure of the gift'),
 'Jer 22:28': ('qualifier', 'forward', 'M30', 'A+B', '"a vessel no one cares for" measures Coniah\'s rejection; paired with "despised" (M30)'),
 'Isa 44:28': ('characteristic', 'read', '', 'A', 'God\'s purpose (the delight word) fulfilled through Cyrus'),
 'Jer 48:38': ('qualifier', 'forward', 'M03; M24', 'A+B', '"a vessel for which no one cares" measures Moab broken; lamentation (M03)'),
 '1Sa 15:22': ('characteristic', 'read', 'M41', 'A+B', 'what the Lord delights in: obeying over sacrifice (A read now); Saul\'s obedience (M41) forward'),
 '1Sa 18:25': ('qualifier', 'forward-carried', 'M64', 'B', 'the king\'s "desire" is the bait of Saul\'s plot (M64 devise); placed in 10.10 Plotting'),
 '1Ki 5:8': ('qualifier', 'data', '', 'C', 'Hiram ready to do "all you desire" in a timber agreement; a trade term'),
 'Ecc 12:1': ('qualifier', 'forward', 'M81', 'B', 'remembering the Creator (M81); "no pleasure in them" describes the evil days. Face: pleasure that ends with age'),
 'Isa 46:10': ('characteristic', 'read', '', 'A', 'God\'s counsel stands and he accomplishes all his purpose'),
 'Mal 1:10': ('characteristic', 'read', 'M30', 'A+B', 'God has no pleasure in priests who despise his name (A read now); the priests\' despising (M30) forward'),
 'Mal 3:12': ('qualifier', 'forward', 'M80', 'A+B', '"a land of delight" describes what the nations will call blessed (M80)'),
 '2Sa 23:5': ('qualifier', 'forward', 'M32; M79', 'A+B', 'David\'s assurance in the everlasting covenant (M32); "my desire" beside "my help/salvation" (M79) is what he trusts God to prosper'),
 'Isa 54:12': ('standalone', 'data', '', 'C', '"precious stones" (stones of delight): building material'),
 'Ecc 12:10': ('qualifier', 'forward-carried', 'M83; M65', 'B', '"words of delight" qualifies the words sought (M83) beside "words of truth"; placed in 10.2'),
 'Job 22:3': ('qualifier', 'forward', 'M26', 'B', 'Eliphaz reckons that a man\'s righteousness (M26) gives the Almighty no pleasure or gain: the content of a disputant\'s claim'),
 '1Ki 5:10': ('qualifier', 'data', '', 'C', 'timber supplied "that he desired": a trade term'),
 '1Ki 9:11': ('qualifier', 'data', '', 'C', 'timber and gold "as much as he desired": a trade term'),
 'Job 21:21': ('characteristic', 'read', '', 'B', 'what the wicked care for: their concern does not reach past their own months'),
 'Psa 1:2': ('characteristic', 'read', '', 'B', 'delight in the law, turned over in meditation (M84); cited in 10.4 and 10.9 but missing from 10.1 Delight'),
 'Psa 16:3': ('characteristic', 'read', '', 'B', 'all delight in the saints, beside "I have no good apart from you"'),
 'Psa 107:30': ('qualifier', 'forward', 'M04; M33', 'A+B', '"their desired haven" is the object of the sailors\' gladness (M04) when the sea is quiet (M33)'),
 'Pro 8:11': ('qualifier', 'forward', 'M16', 'B', '"all that you may desire" measures the worth of wisdom (M16). Same shape as Pro 3:15, now in 10.6 Precious: for the M16 read-back'),
 'Ecc 3:1': ('standalone', 'data', '', 'C', '"every matter": no inner sense'),
 'Ecc 5:4': ('characteristic', 'read', '', 'A+B', 'God has no pleasure in fools; the vow made good before him (vow not M-coded)'),
 'Ecc 5:8': ('standalone', 'data', '', 'C', '"the matter": no inner sense; the verse is not being amazed (M01) at oppression'),
 'Hos 8:8': ('qualifier', 'no-carrier', '', 'A+B', '"a useless vessel" (no delight in it) measures Israel swallowed among the nations; same figure as Jer 22:28'),
 'Zec 11:10': ('qualifier', 'forward', 'M32', 'A+B', 'the staff named Favor, broken to annul the covenant (M32): a sign-name'),
 'Zec 11:7': ('qualifier', 'forward', 'M44', 'A+B', 'the staffs Favor and Union (M44) in the shepherd sign-act'),
 'Psa 90:17': ('characteristic', 'read', '', 'A+B', 'the favor (pleasantness) of the Lord asked to rest on his servants and establish their work'),
 'Pro 3:17': ('qualifier', 'forward', 'M16; M33', 'B', '"ways of pleasantness" describes wisdom\'s ways (M16 in context), beside peace (M33)'),
 'Isa 17:10': ('qualifier', 'forward', 'M81', 'B', 'forgetting the God of salvation (M81); "pleasant plants" is what is planted in his place'),
 'Gen 18:12': ('qualifier', 'forward', 'M04', 'B', 'Sarah laughs to herself (M04); "shall I have pleasure?" is the content of her inner question'),
 'Isa 13:22': ('standalone', 'data', '', 'C', '"pleasant palaces": a description of Babylon\'s ruins'),
 'Psa 119:143': ('characteristic', 'read', '', 'B', 'delight in the commandments while trouble and anguish (M24) have found him'),
 'Psa 119:92': ('characteristic', 'read', '', 'B', 'delight in the law as what kept him from perishing in affliction'),
 'Psa 119:24': ('characteristic', 'read', '', 'B', 'the testimonies his delight and his counselors (M16), while princes plot'),
 'Pro 8:30': ('characteristic', 'read', '', 'A', 'Wisdom daily God\'s delight, rejoicing before him (M04)'),
 'Pro 8:31': ('characteristic', 'read', '', 'A', 'Wisdom rejoicing in the world and delighting in the children of man'),
 'Isa 5:7': ('qualifier', 'forward', 'M68; M12', 'A+B', 'he looked for justice (M68, M12) and found bloodshed; "his pleasant planting" grounds the expectation'),
 # --- judged good by someone ---
 'Job 31:16': ('qualifier', 'forward', 'M09', 'B', 'Job\'s oath that he did not withhold from the poor (M09); "what the poor desired" is the object'),
 '2Sa 3:19': ('qualifier', 'forward', 'M65', 'B', 'Abner reports (M65) what Israel "thought good to do": a collective decision, carried in his speaking'),
 '2Sa 3:36': ('characteristic', 'read', '', 'B', 'the people pleased with all the king did, read from his mourning (M05 tags the same word)'),
 'Num 24:1': ('characteristic', 'read', '', 'A+B', 'Balaam sees that it pleased the Lord to bless Israel and stops looking for omens'),
 '1Sa 16:12': ('standalone', 'data', '', 'C', '"handsome": appearance. Pointer: set against 16:7 (the Lord looks on the heart)'),
 '2Ki 10:5': ('qualifier', 'no-carrier', '', 'B', '"do whatever is good in your eyes": rulers yield to Jehu, in fear (10:4)'),
 'Jos 23:13': ('standalone', 'data', '', 'C', '"this good ground": the land'),
 '1Sa 29:9': ('qualifier', 'forward', 'M15', 'B', 'Achish\'s estimate of David, "blameless in my sight", beside what he knows (M15)'),
 '2Sa 19:18': ('qualifier', 'no-carrier', '', 'B', '"to do his pleasure": service to the returning king; Shimei falls down'),
 'Pro 22:9': ('characteristic', 'read', '', 'B', 'the "good eye" is the generous disposition, shown in sharing bread with the poor'),
 'Ecc 11:7': ('characteristic', 'read', '', 'B', 'light sweet and pleasant to see: life enjoyed, with rejoicing and remembering (11:8-9)'),
 '1Ki 21:2': ('qualifier', 'read', '', 'B', 'the tagged word is the courtesy of the offer; the verse\'s operation is Ahab\'s coveting (untagged, M18\'s own characteristic), read in depth'),
 '1Sa 25:8': ('standalone', 'data', '', 'C', '"feast day" (a good day)'),
 '2Sa 19:27': ('qualifier', 'no-carrier', '', 'B', '"do what seems good to you": Mephibosheth leaves his case with the king'),
 'Est 8:5': ('qualifier', 'forward', 'M39; M42', 'B', 'Esther\'s petition rests on favor (M39): "if I am pleasing in his eyes"'),
 'Gen 16:6': ('qualifier', 'forward', 'M24', 'B', 'Abram hands Hagar to Sarai, "as you please"; Sarai deals harshly (M24)'),
 'Judg 19:24': ('qualifier', 'forward', 'M24; M16', 'B', 'the host offers the women "do what seems good to you", to spare the guest the outrage (M16 folly; M24 violate)'),
 '1Ch 13:2': ('qualifier', 'no-carrier', '', 'B', 'David puts the ark plan to the assembly: "if it seems good to you and from the Lord"'),
 'Gen 20:15': ('qualifier', 'no-carrier', '', 'B', 'Abimelech gives Abraham the land, "dwell where it pleases you"'),
 'Judg 10:15': ('qualifier', 'forward', 'M56; M45', 'B', 'Israel confesses "we have sinned" (M56) and yields: "do to us whatever seems good to you; only deliver us" (M45)'),
 '1Sa 3:18': ('qualifier', 'no-carrier', '', 'B', 'Eli yields to the Lord\'s judgment: "let him do what seems good to him" (same words as 2Sa 15:26, 10.7)'),
 '1Sa 11:10': ('qualifier', 'no-carrier', '', 'B', 'the men of Jabesh feign surrender: "do to us whatever seems good to you"'),
 '1Sa 14:36': ('qualifier', 'no-carrier', '', 'B', 'the people defer to Saul; the priest calls them to draw near to God first'),
 '1Sa 14:40': ('qualifier', 'no-carrier', '', 'B', 'the people defer to Saul at the lot'),
 '2Sa 19:38': ('qualifier', 'forward-carried', 'M64', 'B', 'David honours Barzillai\'s wish (M64 choose); placed in 10.7 and 10.6 Beside choosing'),
 '2Sa 24:22': ('qualifier', 'forward', 'M36', 'B', 'Araunah offers all for the offering (M36): "take what seems good"'),
 '1Ch 21:23': ('qualifier', 'forward', 'M36', 'B', 'Ornan\'s parallel offer (M36)'),
 'Est 3:11': ('qualifier', 'no-carrier', '', 'B', 'the king hands a people to Haman, "as it seems good to you"'),
 'Zec 11:12': ('qualifier', 'forward-carried', '', 'B', '"if it seems good to you, give me my wages": the thirty pieces; placed in 10.4 with 11:13'),
 'Mal 2:17': ('qualifier', 'forward', 'M24; M65', 'B', 'their words weary the Lord (M24, M65): "everyone who does evil is good in the sight of the Lord" is the claim'),
 'Est 8:8': ('qualifier', 'no-carrier', '', 'B', 'the king grants Esther and Mordecai to write "as you please"'),
 'Deu 6:18': ('qualifier', 'forward', 'M12; M05', 'B', 'doing what is right (M12) and good in the Lord\'s sight, that it may go well (M05)'),
 'Deu 12:28': ('qualifier', 'forward', 'M12; M41; M74', 'B', 'obeying (M41) and doing what is good and right (M12) in his sight'),
 'Gen 19:8': ('qualifier', 'no-carrier', '', 'B', 'Lot offers his daughters, "do to them as you please", to shield his guests'),
 '2Sa 10:12': ('qualifier', 'forward', 'M23', 'B', 'courage for the people (M23), and the outcome left to the Lord: "may the Lord do what seems good to him"'),
 '1Ch 19:13': ('qualifier', 'forward', 'M23', 'B', 'parallel of 2Sa 10:12 (M23)'),
 'Deu 23:16': ('qualifier', 'forward-carried', 'M64', 'B', 'the escaped slave lives where he chooses (M64), "wherever it suits him"; placed in 10.7'),
 'Jos 9:25': ('qualifier', 'forward', 'M12', 'B', 'the Gibeonites yield, "whatever seems good and right (M12) in your sight"'),
 '2Ch 14:2': ('qualifier', 'forward', 'M12', 'B', 'Asa did what was good and right (M12) in the Lord\'s eyes'),
 'Est 5:8': ('qualifier', 'forward', 'M39; M42', 'B', 'Esther\'s request rests on favor (M39) and petition (M42): "if it please the king"'),
 'Pro 3:4': ('qualifier', 'forward', 'M39; M15', 'B', 'favor (M39) and good success (M15) in the sight of God and man'),
 'Jer 26:14': ('qualifier', 'forward', 'M12', 'B', 'Jeremiah yields himself, "as seems good and right (M12) to you", and warns of innocent blood (26:15)'),
 'Jer 40:4': ('qualifier', 'forward', 'M12; M58', 'B', 'Jeremiah is given the choice to go or stay, "good and right" (M12) or "wrong" (M58) in his own eyes'),
 # --- doing good / doing well ---
 'Rom 15:26': ('qualifier', 'forward', 'M05; M09', 'B', 'the contribution for the poor (M05 fellowship, M09); "pleased to" is the willingness of the giving (as 1Th 3:1, set 2)'),
 'Psa 40:8': ('characteristic', 'read', '', 'A+B', 'delight to do God\'s will, his law within the heart; in 13.1 (Heb 10), not in 10.1'),
 'Psa 135:6': ('characteristic', 'read', '', 'A', 'whatever the Lord pleases he does, in all creation'),
 'Isa 58:13': ('characteristic', 'read', '', 'B', 'one\'s own pleasure set aside, and the Sabbath called a delight; already in 10.1 (confirm)'),
 '1Ki 5:9': ('qualifier', 'data', '', 'C', '"meet my wishes" in the timber agreement: a trade term'),
 'Isa 48:14': ('characteristic', 'read', 'M51', 'A', 'the Lord\'s purpose performed on Babylon by the one he loves (M51)'),
 'Pro 31:13': ('qualifier', 'forward', 'M83', 'B', 'she seeks (M83) wool and flax and works "with willing (delighting) hands": the manner of her work'),
 # --- good set beside evil ---
 'Pro 15:26': ('qualifier', 'forward', 'M65; M06', 'A+B', '"gracious (pleasant) words" set against the thoughts of the wicked (M06): qualifies words (M65)'),
}

assert len(rows94) == 94 and set(r[0].strip() for r in rows94) == set(T), set(r[0].strip() for r in rows94) ^ set(T)
out = os.path.join(HERE, 'm18-group-B-remaining-role-triage-v1-20261011.csv')
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'm18_word', 'other_mcodes', 'm18_role', 'decision', 'forward_to', 'route', 'main_operation_note'])
    for ref, s, word in rows94:
        ref = ref.strip()
        role, dec, fwd, route, note = T[ref]
        w.writerow([ref, f'{s} "{word}"', pull[ref]['other_mcodes'], role, dec, fwd, route, note])
from collections import Counter
print(Counter(v[1] for v in T.values()))
