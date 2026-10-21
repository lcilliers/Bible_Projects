"""M72 group B (#1998), 2026-10-12: Ch 11 retitled; the outstanding M72 placements written into the activity
chapters (10.x), Ch 12 and Ch 14.

Researcher (chat 2026-10-12, verbatim): "'11. Other sides of the inner being' and update the opening paragraph.
you can proceed with writing to the narrative any outstanding parts of M72".
Source: m72-group-B-reading-v1-20261012.md, with the correction in m72-group-B-weave-record-v1-20261012.md §2: each
verse goes where the act that moves in it belongs; authority is the standing that act moves in.
Same mechanics and quote check as m72-group-B-weave-ch11-and-faculties-v1-20261012.py.
Usage: python m72-group-B-weave-activities-v1-20261012.py [--dry]
"""
import glob, os, re, shutil, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
DATE = '20261012'
DRY = '--dry' in sys.argv


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]


CH11_OPEN_OLD = 'When I read the inner words across all of Scripture, and read each passage with what comes before and after it, certain patterns kept coming back. None of them is a doctrine stated in a single verse. I set them out side by side, as the passages give them.'
CH11_OPEN_NEW = 'This chapter gathers what the verses show about the inner being that has no other home in this book. The sections stand side by side. They are not one argument, and nothing joins them except that they belong to the inner being.'

OPS = {
'11-patterns-of-the-inner-life-': [
 ('replace_text', '# 11. Patterns of the inner life', '# 11. Other sides of the inner being'),
 ('replace_text', CH11_OPEN_OLD, CH11_OPEN_NEW),
 ('replace_text', 'The title of this section, and of this chapter, are under question.',
  'The chapter title was changed the same day, on the researcher\'s instruction, to say only that the chapter gathers what has no other home.'),
],
'10-10-relating-to-others-': [
 ('after_prefix', '- "You shall not rule over him ruthlessly but shall fear your God" (Leviticus 25:43).',
  '- The same law gives the limit twice more, each time on another ground. Brotherhood: "over your brothers the people of Israel you shall not rule, one over another ruthlessly" (25:46). The onlooker: "He shall not rule ruthlessly over him in your sight" (25:53). Behind all three: "For it is to me that the people of Israel are servants" (25:55).'),
 ('after_prefix', '- Nehemiah would not burden the people as earlier governors had:',
  '- The ruler God speaks of in David\'s last words: "When one rules justly over men, ruling in the fear of God," (2 Samuel 23:3).\n'
  '- A master is told to "stop your threatening, knowing that he who is both their Master and yours is in heaven, and that there is no partiality with him" (Ephesians 6:9). What checks him is knowing that he has a Master too.'),
 ('before_prefix', '### Making others afraid',
  'Mastery can turn on the day it is hoped for. "on the very day when the enemies of the Jews hoped to gain the mastery over them, the reverse occurred: the Jews gained mastery over those who hated them", and "the fear of them had fallen on all peoples" (Esther 9:1–2).\n'),
 ('before_prefix', '## Loyalty and honour', '''## Holding authority over another

The verses rarely treat holding authority over someone as an act in itself. They speak of a position one person holds over another, and of what fills it. The same position is filled very differently, and what fills it decides what happens to the one beneath (Chapter 11, section 7).

**At its worst.** Ezekiel speaks to the shepherds of Israel: "Ah, shepherds of Israel who have been feeding yourselves! Should not shepherds feed the sheep?" (Ezekiel 34:2). The charge lists the care not given: "The weak you have not strengthened, the sick you have not healed, the injured you have not bound up, the strayed you have not brought back, the lost you have not sought, and with force and harshness you have ruled them" (34:4). The rulers were there, yet "they were scattered, because there was no shepherd" (34:5). I read rule that serves the ruler as counted as no shepherding at all. The proverb sees the same from below: "Like a roaring lion or a charging bear is a wicked ruler over a poor people". The next verse names what lies behind it: "A ruler who lacks understanding is a cruel oppressor, but he who hates unjust gain will prolong his days" (Proverbs 28:15–16). The Preacher watched it with his heart: "when man had power over man to his hurt" (Ecclesiastes 8:9; Chapter 4).

**Where it comes from between people.**
- **Money.** "The rich rules over the poor, and the borrower is the slave of the lender" (Proverbs 22:7). Two verses on: "Whoever has a bountiful eye will be blessed, for he shares his bread with the poor" (22:9).
- **A decree.** After Vashti refused the king (10.13), the counsel was that the noble women "will say the same to all the king's officials, and there will be contempt and wrath in plenty" (Esther 1:18). The decree was meant to bring it about that "all women will give honor to their husbands" (1:20), and "that every man be master in his own household" (1:22). Honour is ordered by law, out of fear of contempt.
- **Given to each other.** In marriage "the wife does not have authority over her own body, but the husband does. Likewise the husband does not have authority over his own body, but the wife does" (1 Corinthians 7:4). The reason follows: "so that Satan may not tempt you because of your lack of self-control" (7:5). Each holds the other's authority, so that neither is left alone with what he does not rule.

**In the church.** "I do not permit a woman to teach or to exercise authority over a man; rather, she is to remain quiet" (1 Timothy 2:12). The verse gives its own grounds: "For Adam was formed first, then Eve; and Adam was not deceived, but the woman was deceived and became a transgressor" (2:13–14). Around it, the men are to pray "without anger or quarreling" (2:8), and the women to "learn quietly with all submissiveness" (2:11). I add nothing beyond what the verses state.

**Turned round.** When "A dispute also arose among them, as to which of them was to be regarded as the greatest", Jesus said, "The kings of the Gentiles exercise lordship over them, and those in authority over them are called benefactors. But not so with you" (Luke 22:24–26). Those who lord it over others take a good name for it as well. In its place: "I am among you as the one who serves" (22:27). Elders are to shepherd "not under compulsion, but willingly", "not domineering over those in your charge, but being examples to the flock" (1 Peter 5:2–3), and all of them, elders too, are to clothe themselves "with humility toward one another" (5:5). Paul had authority and would not use it over faith: "Not that we lord it over your faith, but we work with you for your joy, for you stand firm in your faith" (2 Corinthians 1:24). He had stayed away "to spare you" (1:23).

**Under it.** The verses ask something of the one beneath, and give its ground. "Remind them to be submissive to rulers and authorities, to be obedient, to be ready for every good work, to speak evil of no one, to avoid quarreling, to be gentle", and then "For we ourselves were once foolish, disobedient, led astray" (Titus 3:1–3). The ground is remembering what one was, and God's kindness (3:4; 10.3). Under a foreign rule a people can be turned against its own. "Do you not know that the Philistines are rulers over us? What then is this that you have done to us?", said three thousand men of Judah to Samson, and they bound him "that we may give you into the hands of the Philistines" (Judges 15:11–12).

## A right set aside for another

Paul argues at length that a right is his, and then does not use it. "Do we not have the right to eat and drink? Do we not have the right to take along a believing wife" (1 Corinthians 9:4–5). "Nevertheless, we have not made use of this right, but we endure anything rather than put an obstacle in the way of the gospel of Christ" (9:12). He calls it his own will: "For if I do this of my own will, I have a reward" (9:17; 10.7). The reward is "that in my preaching I may present the gospel free of charge, so as not to make full use of my right in the gospel" (9:18). Then: "For though I am free from all, I have made myself a servant to all, that I might win more of them" (9:19). To another church: "It was not because we do not have that right, but to give you in ourselves an example to imitate" (2 Thessalonians 3:9).

A right that knowledge gives is set aside in the same way. "But take care that this right of yours does not somehow become a stumbling block to the weak" (1 Corinthians 8:9). "And so by your knowledge this weak person is destroyed, the brother for whom Christ died" (8:11). Paul's answer is his own: "if food makes my brother stumble, I will never eat meat, lest I make my brother stumble" (8:13; Chapter 8).

Authority given for a purpose is measured by it. It is "our authority, which the Lord gave for building you up and not for destroying you" (2 Corinthians 10:8), and "I do not want to appear to be frightening you with my letters" (10:9). "For we are glad when we are weak and you are strong. Your restoration is what we pray for" (13:9). He writes "that when I come I may not have to be severe in my use of the authority that the Lord has given me for building up and not for tearing down" (13:10).

In each of these the right is real, and the reason for not using it is another person. I read the right as held loosely, so that it can be laid down for someone else.

'''),
],
'10-06-wanting-': [
 ('before_prefix', '## Aimed at nothing, and enjoyment given',
  'Simon wanted an authority that was God\'s to give, and thought it could be bought. "Now when Simon saw that the Spirit was given through the laying on of the apostles\' hands, he offered them money, saying, \'Give me this power also\'" (Acts 8:18–19). Peter named what was in him: "you thought you could obtain the gift of God with money!", "your heart is not right before God", and "I see that you are in the gall of bitterness and in the bond of iniquity" (8:20–23; Chapter 4).\n'),
 ('before_prefix', '## As heat',
  'The Preacher says it the other way round as well: "Everyone also to whom God has given wealth and possessions and power to enjoy them, and to accept his lot and rejoice in his toil — this is the gift of God", for "God keeps him occupied with joy in his heart" (Ecclesiastes 5:19–20). Owning a thing and having power to enjoy it are two things, and the second is given.\n'),
 ('before_prefix', '## Taken away',
  'The brothers\' hatred had another object too: the prospect of his rule. After the first dream they said, "Are you indeed to reign over us? Or are you indeed to rule over us?", and "they hated him even more for his dreams and for his words" (Genesis 37:8). Years later "Joseph\'s brothers came and bowed themselves before him with their faces to the ground", and "Joseph remembered the dreams that he had dreamed of them" (42:6, 9).\n'),
],
'10-07-choosing-and-setting-direction-': [
 ('before_prefix', '## What draws it',
  '**Convinced that I ought.** A choice can rest on a conviction that is wrong, held with authority from others. "I myself was convinced that I ought to do many things in opposing the name of Jesus of Nazareth. And I did so in Jerusalem. I not only locked up many of the saints in prison after receiving authority from the chief priests, but when they were put to death I cast my vote against them" (Acts 26:9–10). The voice that stopped him named it: "It is hard for you to kick against the goads" (26:14).\n'),
 ('before_prefix', '## Choosing together',
  '''**Rule offered, refused, and sought.** "Rule over us, you and your son and your grandson also, for you have saved us from the hand of Midian." Gideon refused: "I will not rule over you, and my son will not rule over you; the Lord will rule over you" (Judges 8:22–23). Daniel, offered a place as third ruler for reading the writing, refused the reward and did the task: "Let your gifts be for yourself, and give your rewards to another. Nevertheless, I will read the writing to the king and make known to him the interpretation" (Daniel 5:17). Gideon's son sought what his father refused, and won it by kinship. "Which is better for you, that all seventy of the sons of Jerubbaal rule over you, or that one rule over you? Remember also that I am your bone and your flesh." And "their hearts inclined to follow Abimelech, for they said, 'He is our brother'" (Judges 9:2–3). He then killed his seventy brothers (9:5). The verses set refusing and seeking side by side in one family, and say no more about why.

'''),
],
'10-09-relating-to-god-': [
 ('before_prefix', '## The living God', '''## Kept from what would rule

The psalmist names two kinds of sin and asks differently for each. "Who can discern his errors? Declare me innocent from hidden faults. Keep back your servant also from presumptuous sins; let them not have dominion over me! Then I shall be blameless, and innocent of great transgression" (Psalm 19:12–13). Only the sins done knowingly are spoken of as able to rule him, and from those he asks to be held back. Elsewhere, in the same breath as longing for the commandments: "Keep steady my steps according to your promise, and let no iniquity get dominion over me. Redeem me from man's oppression, that I may keep your precepts" (Psalm 119:133–134). Two dominions stand side by side, sin within and oppression without, and he asks God against both (Chapter 14 for sin's rule ended).

## Under rule, and longing for his

Under the rule of others the verses tell of crying out. "Therefore you gave them into the hand of their enemies, who made them suffer. And in the time of their suffering they cried out to you and you heard them from heaven" (Nehemiah 9:27). Then, again, "after they had rest they did evil again before you, and you abandoned them to the hand of their enemies, so that they had dominion over them. Yet when they turned and cried to you, you heard from heaven" (9:28). The psalm tells the same: "he gave them into the hand of the nations, so that those who hated them ruled over them", and "he looked upon their distress, when he heard their cry" (Psalm 106:41, 44). The lament names the shame of who rules and the absence of help: "Slaves rule over us; there is none to deliver us from their hand" (Lamentations 5:8).

The prophet complains in a figure of a world with no one ruling: "You make mankind like the fish of the sea, like crawling things that have no ruler" (Habakkuk 1:14), after "why do you idly look at traitors and remain silent" (1:13). And God's own rule is longed for: "We have become like those over whom you have never ruled, like those who are not called by your name" (Isaiah 63:19). Being ruled by him and being called by his name are set side by side.

## Knowing who rules

A centurion understood Jesus' word from his own place: "For I too am a man under authority, with soldiers under me. And I say to one, 'Go,' and he goes". "When Jesus heard this, he marveled", and said, "with no one in Israel have I found such faith" (Matthew 8:9–10; 10.4). He knew authority from inside it, and trusted a word.

Others claimed to know God while setting up their own rulers. "To me they cry, 'My God, we — Israel — know you.'" God answers, "They made kings, but not through me. They set up princes, but I knew it not. With their silver and gold they made idols for their own destruction" (Hosea 8:2, 4). Their kings and their idols stand in one sentence, both made with their own hands.

A king was told that his kingdom would stand "from the time that you know that Heaven rules", with the counsel "break off your sins by practicing righteousness, and your iniquities by showing mercy to the oppressed" (Daniel 4:26–27; 10.7, Chapter 4). The psalmist, given dominion over the works of God's hands, answers with wonder: "what is man that you are mindful of him", and "O Lord, our Lord, how majestic is your name in all the earth!" (Psalm 8:4, 9).

Nearness to him is his doing. Of the ruler to come: "I will make him draw near, and he shall approach me, for who would dare of himself to approach me? declares the Lord" (Jeremiah 30:21; Chapter 4). Of Jacob: "He strove with the angel and prevailed; he wept and sought his favor", and the call drawn from it is "return, hold fast to love and justice, and wait continually for your God" (Hosea 12:4, 6; 13.2).

'''),
],
'10-12-fear-': [
 ('before_prefix', '## What fear does',
  'Fear can come with no one there to cause it. Among the curses: "I will visit you with panic", and "Those who hate you shall rule over you, and you shall flee when none pursues you" (Leviticus 26:16–17).\n'),
 ('before_prefix', '## Fear set against faith and love',
  'Luke gives the saying with its measure: "fear him who, after he has killed, has authority to cast into hell. Yes, I tell you, fear him!" (Luke 12:5). Three verses later: "Fear not; you are of more value than many sparrows" (12:7). The fear is measured by how far the authority reaches, and the same passage turns it into "Fear not".\n'),
 ('before_prefix', '## Dread laid on others',
  '''Fear sits inside those who hold authority, and moves what they do with it. "When Pilate heard this statement, he was even more afraid" (John 19:8). Then he said, "Do you not know that I have authority to release you and authority to crucify you?" (19:10). I read his claim as coming out of his fear. When the crowd said, "If you release this man, you are not Caesar's friend" (19:12), another authority moved him.

Fear of a crowd decides an answer. Asked whether John's baptism was from heaven or from man, the leaders "discussed it among themselves". "If we say, 'From man,' we are afraid of the crowd, for they all hold that John was a prophet" (Matthew 21:25–26). Luke: "all the people will stone us to death" (Luke 20:6). They answered, "We do not know" (Matthew 21:27; 10.4).

Fear is also forbidden, and commanded. "Let not your heart faint, and be not fearful at the report heard in the land … and violence is in the land, and ruler is against ruler" (Jeremiah 51:46). "Be not afraid when a man becomes rich, when the glory of his house increases" (Psalm 49:16; Chapter 2). And a king decreed fear of God: "I make a decree, that in all my royal dominion people are to tremble and fear before the God of Daniel" (Daniel 6:26), after he "was exceedingly glad" at Daniel's deliverance (6:23).

'''),
],
'10-04-thinking-': [
 ('before_prefix', '## When thinking changes character',
  'Thinking can weigh answers by their cost, not by their truth. Asked by what authority he acted, Jesus asked in return, "The baptism of John, from where did it come? From heaven or from man?" "And they discussed it among themselves, saying, \'If we say, From heaven, he will say to us, Why then did you not believe him? But if we say, From man, we are afraid of the crowd\'" (Matthew 21:25–26). They answered, "We do not know" (21:27). Both answers were weighed against what each would cost them (10.12, 10.11).\n'),
],
'10-11-hiding-and-disclosing-': [
 ('before_prefix', '### Hiding another',
  'An answer can be held back. Asked about John, the leaders said, "We do not know", and Jesus answered, "Neither will I tell you by what authority I do these things" (Matthew 21:27). Their own reasoning shows that they held back what they thought (21:25–26; 10.4).\n'),
],
'10-03-remembering-and-forgetting-': [
 ('before_prefix', '## God remembers',
  '''**Remembered the other way round.** Refusing Moses, Dathan and Abiram called Egypt what the promised land was meant to be: "Is it a small thing that you have brought us up out of a land flowing with milk and honey, to kill us in the wilderness, that you must also make yourself a prince over us?" (Numbers 16:13). The house of slavery is remembered as plenty, and the leader as one who made himself prince.

**Remembering what one was.** Submission is asked on the ground of memory: "to be submissive to rulers and authorities", "For we ourselves were once foolish, disobedient, led astray, slaves to various passions and pleasures" (Titus 3:1, 3; 10.10).

**A dream remembered.** When his brothers bowed before him, "Joseph remembered the dreams that he had dreamed of them" (Genesis 42:9; 10.6).

'''),
],
'10-01-feeling-': [
 ('before_prefix', '## Fear',
  'Joy can be turned from one ground to another. "The seventy-two returned with joy, saying, \'Lord, even the demons are subject to us in your name!\'" Jesus did not take back the authority, but moved their joy: "Nevertheless, do not rejoice in this, that the spirits are subject to you, but rejoice that your names are written in heaven" (Luke 10:17, 20). "In that same hour he rejoiced in the Holy Spirit" (10:21; 13.3).\n'),
],
'10-13-anger-': [
 ('before_prefix', '### Where it sits',
  'Anger can rise at a charge against one\'s own leadership. When Dathan and Abiram accused him of making himself a prince over them, "Moses was very angry and said to the Lord, \'Do not respect their offering. I have not taken one donkey from them, and I have not harmed one of them\'" (Numbers 16:15). He took the anger to the Lord. Fury can also drive authority received from others: "I not only locked up many of the saints in prison after receiving authority from the chief priests", and "in raging fury against them I persecuted them even to foreign cities" (Acts 26:10–11; 10.7).\n'),
],
'12-when-the-inner-being-goes-wrong-': [
 ('before_prefix', '## Hardening and stubbornness',
  'Before the fall named in Daniel 5:20 stands the boast itself: "Is not this great Babylon, which I have built by my mighty power as a royal residence and for the glory of my majesty?" "While the words were still in the king\'s mouth, there fell a voice from heaven" (Daniel 4:30–31; Chapter 4). He had been told that his kingdom would stand "from the time that you know that Heaven rules" (4:26).\n'),
],
'14-made-new-': [
 ('before_prefix', '## Thoughts taken captive',
  '''## Sin's rule ended

"Let not sin therefore reign in your mortal body, to make you obey its passions. Do not present your members to sin as instruments for unrighteousness, but present yourselves to God" (Romans 6:12–13). The reason follows: "For sin will have no dominion over you, since you are not under law but under grace" (6:14). The end of sin's rule is stated as a fact and given as a command. "Do you not know that if you present yourselves to anyone as obedient slaves, you are slaves of the one whom you obey" (6:16). I read the question of who rules within as answered by whom one presents oneself to (Chapter 11, section 7).

'''),
],
}


def apply(text, mode, anchor, new):
    if mode == 'replace_text':
        assert text.count(anchor) == 1, anchor[:60]
        return text.replace(anchor, new)
    lines = text.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith(anchor)]
    assert len(idx) == 1, (anchor[:60], len(idx))
    i = idx[0]
    if mode == 'after_prefix':
        lines.insert(i + 1, new)
    elif mode == 'before_prefix':
        lines.insert(i, new.rstrip('\n') + '\n')
    return '\n'.join(lines)


def bump(path, newbase=None):
    base = os.path.basename(path)
    m = re.match(r'(.+)-v(\d+)-\d{8}\.md$', base)
    stem = newbase or m.group(1)
    return os.path.join(NARR, f'{stem}-v{int(m.group(2)) + 1}-{DATE}.md')


con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
norm = lambda t: re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', t.lower())).strip()
VERSES = [norm(t or '') for (t,) in con.execute('select text from verse where deleted=0')]
ALLOW = ()


def check(text):
    bad = []
    for q in re.findall(r'(?:^|(?<=[\s(*—]))"([^"\n]+?)"(?=[*\s).,;:!?]|$)', text, flags=re.M):
        for part in q.split('…'):
            if len(norm(part).split()) < 3 or part.startswith(ALLOW):
                continue
            chunks = [norm(c) for c in re.split(r'[.;?!,]\s', part) if len(norm(c).split()) >= 3]
            if not all(any(c in v for v in VERSES) for c in chunks):
                bad.append(part)
    return bad


writes = []
for prefix, ops in OPS.items():
    f = current(prefix)
    t = open(f, encoding='utf-8').read()
    ins = ''
    for mode, anchor, new in ops:
        t = apply(t, mode, anchor, new)
        if not (prefix.startswith('11-')):
            ins += new + '\n'
    out = bump(f, '11-other-sides-of-the-inner-being' if prefix.startswith('11-') else None)
    writes.append((f, out, t, ins))

nbad = 0
for f, out, t, ins in writes:
    bad = check(ins)
    nbad += len(bad)
    print(os.path.basename(f), '->', os.path.basename(out), '| failing:', len(bad))
    for x in bad:
        print('    !', x[:170])
if DRY or nbad:
    print('dry run' if DRY else 'quote failures: nothing written')
    sys.exit(0 if DRY else 1)
for f, out, t, ins in writes:
    open(out, 'w', encoding='utf-8').write(t)
    shutil.move(f, os.path.join(NARR, 'archive', os.path.basename(f)))
print('written', len(writes), 'files')
