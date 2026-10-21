"""M02 pairing threads (OT-29, OT-30, OT-51), 2026-10-13: the 14 gap verses woven, plus two corrections.

Researcher (chat 2026-10-13, verbatim): "weave the 14 gaps and make the two fixes".
Source: m02-pairing-done-strands-check-v1-20261013.md section 3 (readings and placements) and section 4 (the two
corrections: the stale "on hold" working note in 10.13; the Ch 5 pointer to Chapter 2 for Proverbs 20:2).
Mechanics and quote check as ../M72 - authority-dominion/m72-group-B-weave-activities-v1-20261012.py: each chapter
is bumped one version, the prior version archived, and every inserted quotation checked against the ESV in iba.db.
Usage: python m02-pairing-gaps-weave-v1-20261013.py [--dry]
"""
import glob, os, re, shutil, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
DATE = '20261013'
DRY = '--dry' in sys.argv


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]


OPS = {
'10-13-anger-': [
 # M20: Deu 31:17, God's side beside the people's question
 ('replace_text',
  '- **As God\'s absence:** "Have not these evils come upon us because our God is not among us?" (Deuteronomy 31:17).',
  '- **As God\'s absence:** "Have not these evils come upon us because our God is not among us?" (Deuteronomy 31:17). The same verse gives God\'s side first: "my anger will be kindled against them in that day, and I will forsake them and hide my face from them" (10.9).'),
 # M25: Deu 31:27-29
 ('after_prefix', '- **Distress that drives further away:**',
  '- **Known beforehand:** Moses tells them what he has seen in them: "For I know how rebellious and stubborn you are. Behold, even today while I am yet alive with you, you have been rebellious against the Lord. How much more after my death!" (Deuteronomy 31:27). He names where it leads: "provoking him to anger through the work of your hands" (31:29).'),
 # M01: Lam 2:20-22
 ('replace_text',
  'So is the heart: "Pour out your heart like water before the presence of the Lord!" (2:19).',
  'So is the heart: "Pour out your heart like water before the presence of the Lord!" (2:19). The lament speaks to God about his anger, to his face: "Look, O Lord, and see! With whom have you dealt thus?" (2:20). "You summoned as if to a festival day my terrors on every side, and on the day of the anger of the Lord no one escaped or survived; those whom I held and raised my enemy destroyed" (2:22). A festival day calls people together to rejoice. Here what is called together is terror. I read that the speaker does not turn away from God in the terror, but asks him to look at what his anger has done to those "I held and raised".'),
 # M25: Isa 51:17-22
 ('before_prefix', '- **Finished:** "seven angels',
  '- **The cup taken back:** "Wake yourself, wake yourself, stand up, O Jerusalem, you who have drunk from the hand of the Lord the cup of his wrath" (Isaiah 51:17). The one who drank cannot stand alone: "There is none to guide her among all the sons she has borne; there is none to take her by the hand among all the sons she has brought up" (51:18). Her sons "are full of the wrath of the Lord" (51:20), "drunk, but not with wine" (51:21). The hand that ends it is God\'s, "your God who pleads the cause of his people": "Behold, I have taken from your hand the cup of staggering; the bowl of my wrath you shall drink no more" (51:22). I read the figure of drunkenness as wrath that leaves a person staggering and without a guide, and the call to wake as going to one who cannot rise without a hand.'),
 # M20: Zep 2:3; M25: Pro 11:4
 ('after_prefix', 'Some of the time, the call is to shelter while the anger passes.',
  '\nZephaniah calls people to seek before the day comes: "Seek the Lord, all you humble of the land, who do his just commands; seek righteousness; seek humility; perhaps you may be hidden on the day of the anger of the Lord" (Zephaniah 2:3). Those called are already humble and already doing his commands, and they are told to seek humility. The verse promises nothing beyond "perhaps", and the hiding is God\'s to give. What a person has leaned on is tested on that day: "Riches do not profit in the day of wrath, but righteousness delivers from death" (Proverbs 11:4).'),
 # M01: Psa 76:7-9
 ('after_prefix', '"Who can stand before his indignation?',
  '\nPsalm 76 asks the same question and gives the anger\'s purpose: "But you, you are to be feared! Who can stand before you when once your anger is roused? From the heavens you uttered judgment; the earth feared and was still, when God arose to establish judgment, to save all the humble of the earth" (Psalm 76:7–9). The anger is roused to save the humble, and the fear is the earth falling still before it (10.12).'),
 # M25: Pro 29:8, 11
 ('after_prefix', 'In two of these, Jonah and the elder brother,',
  '\nThe proverbs set the one who turns anger away beside the one who stirs it: "Scoffers set a city aflame, but the wise turn away wrath" (Proverbs 29:8). The scoffer\'s words set a whole city alight. Three verses on: "A fool gives full vent to his spirit, but a wise man quietly holds it back" (29:11). I read the wise man who turns another\'s wrath away as the same man who holds back his own.'),
 # M01: Pro 20:2-3; Job 19:29; Rev 11:18
 ('replace_text',
  '- **A ruler\'s anger,** as those beneath it bear it: "A king\'s wrath is a messenger of death, and a wise man will appease it" (Proverbs 16:14).',
  '- **A ruler\'s anger,** as those beneath it bear it: "A king\'s wrath is a messenger of death, and a wise man will appease it" (Proverbs 16:14). "The terror of a king is like the growling of a lion; whoever provokes him to anger forfeits his life" (20:2). The next verse says what to do instead: "It is an honor for a man to keep aloof from strife, but every fool will be quarreling" (20:3).\n'
  '- **Those who pursue another.** Job\'s friends say, "How we will pursue him!" and "The root of the matter is found in him" (Job 19:28). He answers them: "be afraid of the sword, for wrath brings the punishment of the sword, that you may know there is a judgment" (19:29). He says it straight after "I know that my Redeemer lives" (19:25). I read the one accused as turning the fear of wrath back on those who pursue him, from the confidence he has just spoken.\n'
  '- **The nations.** In worship the elders say, "The nations raged, but your wrath came" (Revelation 11:18). Two angers stand in one sentence, and the second answers the first. The same verse names the reward of "those who fear your name, both small and great" (10.12; 13.1).'),
 # correction: stale working note (OT-08 closed 2026-10-09)
 ('replace_text',
  '- The verses in which anger crosses into life and death are kept for Chapter 2, where that placement is on hold. These include Sheol, the plague, "angry enough to die" (Jonah 4:9), and the deaths in the narrative.\n',
  ''),
],
'10-09-relating-to-god-': [
 ('replace_text',
  '- **Sin.** "I will surely hide my face in that day because of all the evil that they have done, because they have turned to other gods" (Deuteronomy 31:18).',
  '- **Sin.** "Then my anger will be kindled against them in that day, and I will forsake them and hide my face from them" (Deuteronomy 31:17). The cause stands on both sides of it: they "will forsake me and break my covenant" (31:16), and "I will surely hide my face in that day because of all the evil that they have done, because they have turned to other gods" (31:18). Those it falls on are given words of their own: "Have not these evils come upon us because our God is not among us?" (31:17). I read that their question names the absence and leaves out the turning that the verses give as its cause (10.13).'),
 ('after_prefix', '- **It is spoken as a complaint.**',
  '- **Time is weighed against it.** "How long, O Lord? Will you hide yourself forever? How long will your wrath burn like fire? Remember how short my time is!" (Psalm 89:46–47). The plea sets the length of the anger against the length of a life (Chapter 2).'),
 ('replace_text',
  '"With everlasting love I will have compassion on you" (Isaiah 54:8). And the last word',
  '"With everlasting love I will have compassion on you" (Isaiah 54:8). Of a city whose houses would be filled with the dead, "for I have hidden my face from this city because of all their evil", the very next word is "Behold, I will bring to it health and healing, and I will heal them" (Jeremiah 33:5–6). And the last word'),
],
'10-12-fear-': [
 ('after_prefix', 'Peter\'s plea is answered:',
  '\nFear before his anger can be a stillness. "But you, you are to be feared! Who can stand before you when once your anger is roused? From the heavens you uttered judgment; the earth feared and was still, when God arose to establish judgment, to save all the humble of the earth" (Psalm 76:7–9; 10.13). When his wrath comes, those who fear his name are named among the rewarded: "the time for the dead to be judged, and for rewarding your servants, the prophets and saints, and those who fear your name, both small and great" (Revelation 11:18).'),
 ('after_prefix', 'Paul\'s account of the ruler holds fear and respect together',
  '\nThe proverb gives the fear of a ruler and what provoking him costs: "The terror of a king is like the growling of a lion; whoever provokes him to anger forfeits his life" (Proverbs 20:2). The next verse gives the other way: "It is an honor for a man to keep aloof from strife, but every fool will be quarreling" (20:3; 10.13).'),
],
'10-04-thinking-': [
 ('before_prefix', '## The inclination: a shaped thing',
  'A thought can be answered by God. To the elders who came "to inquire of the Lord" (Ezekiel 20:1), he names what is in them: "What is in your mind shall never happen—the thought, \'Let us be like the nations, like the tribes of the countries, and worship wood and stone.\'" And he answers it with an oath by his own life: "As I live, declares the Lord God, surely with a mighty hand and an outstretched arm and with wrath poured out I will be king over you" (20:32–33; 13.1).\n'),
],
'13-01-divine-': [
 ('before_prefix', '**The soul\'s answer.**',
  '**His rule answers a thought.** When the people thought, "Let us be like the nations, like the tribes of the countries, and worship wood and stone", he answered: "As I live, declares the Lord God, surely with a mighty hand and an outstretched arm and with wrath poured out I will be king over you" (Ezekiel 20:32–33). The wrath goes with bringing them out and gathering them (20:34), with judgment "face to face" (20:35), and with bringing them "into the bond of the covenant" (20:37; 10.4, 10.13).\n\n'
  '**His reign, and the nations\' rage.** The elders give thanks "for you have taken your great power and begun to reign", and in the next breath: "The nations raged, but your wrath came" (Revelation 11:17–18). His reign and his wrath are spoken together, and the same verse names the reward of "those who fear your name, both small and great" (10.13).\n'),
],
'02-life-breath-and-death-': [
 ('replace_text',
  '"What man can live and never see death? Who can deliver his soul from the power of Sheol?" (Psalm 89:48).',
  '"What man can live and never see death? Who can deliver his soul from the power of Sheol?" (Psalm 89:48). The psalmist asks it inside a plea about God\'s anger: "How long will your wrath burn like fire? Remember how short my time is!" (89:46–47; 10.9).'),
],
'05-the-soul-': [
 # correction: Chapter 2 does not cite Proverbs 20:2; 10.13 now carries it
 ('replace_text', 'Proverbs 20:2), Chapter 2 takes it up.',
  'Proverbs 20:2), 10.13 takes it up under *Other parties*, with the verse that follows it.'),
],
}


def apply(text, mode, anchor, new):
    if mode == 'replace_text':
        assert text.count(anchor) == 1, (anchor[:70], text.count(anchor))
        return text.replace(anchor, new)
    lines = text.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith(anchor)]
    assert len(idx) == 1, (anchor[:70], len(idx))
    i = idx[0]
    if mode == 'after_prefix':
        lines.insert(i + 1, new)
    elif mode == 'before_prefix':
        lines.insert(i, new.rstrip('\n') + '\n')
    return '\n'.join(lines)


def bump(path):
    m = re.match(r'(.+)-v(\d+)-\d{8}\.md$', os.path.basename(path))
    return os.path.join(NARR, f'{m.group(1)}-v{int(m.group(2)) + 1}-{DATE}.md')


con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
norm = lambda t: re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', t.lower())).strip()
VERSES = [norm(t or '') for (t,) in con.execute('select text from verse where deleted=0')]


def check(text):
    bad, n = [], 0
    for q in re.findall(r'(?:^|(?<=[\s(*—]))"([^"\n]+?)"(?=[*\s).,;:!?]|$)', text, flags=re.M):
        for part in q.split('…'):
            if len(norm(part).split()) < 3:
                continue
            n += 1
            chunks = [norm(c) for c in re.split(r'[.;?!,]\s', part) if len(norm(c).split()) >= 3]
            if not all(any(c in v for v in VERSES) for c in chunks):
                bad.append(part)
    return bad, n


writes = []
for prefix, ops in OPS.items():
    f = current(prefix)
    t = open(f, encoding='utf-8').read()
    ins = ''
    for mode, anchor, new in ops:
        t = apply(t, mode, anchor, new)
        ins += new + '\n'
    writes.append((f, bump(f), t, ins))

nbad = nq = 0
for f, out, t, ins in writes:
    bad, n = check(ins)
    nbad += len(bad)
    nq += n
    print(os.path.basename(f), '->', os.path.basename(out), '| quote parts:', n, '| failing:', len(bad))
    for x in bad:
        print('    !', x[:170])
print('quote parts checked:', nq)
if DRY or nbad:
    print('dry run' if DRY else 'quote failures: nothing written')
    sys.exit(0 if DRY else 1)
for f, out, t, ins in writes:
    open(out, 'w', encoding='utf-8').write(t)
    shutil.move(f, os.path.join(NARR, 'archive', os.path.basename(f)))
print('written', len(writes), 'files')
