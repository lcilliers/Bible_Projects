"""M72 group B (#1998), 2026-10-12: current thoughts into Ch 11 sec 7; faculty- and other-being-specific parts
into Ch 2, 4, 5, 7, 8 and 13.1-13.4.

Researcher (chat 2026-10-12, verbatim): "I suggest you add the current thoughts coming out of the M72 reading to
ch_11 and place the parts that is specific to the heart, flesh, divine etc. into those sections. from what I can see
at the moment rule, authority, giving or having power is more of a state or status that works in collaboration with
other characteristics and parties, but this is not yet strongly emerging from the material you are providing."

Source: m72-group-B-reading-v1-20261012.md; record: m72-group-B-weave-record-v1-20261012.md.
The 10.x activity sections (10.10 etc.) are NOT touched: not instructed.
Each touched chapter gets a version bump; the prior version moves to archive/. Inserted quotations are checked
against the ESV in iba.db `verse` before anything is written.
Usage: python m72-group-B-weave-ch11-and-faculties-v1-20261012.py [--dry]
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


# ---------------------------------------------------------------- Ch 11 sec 7 (replaces the section body)
CH11_OLD_START = '## 7. The inner being is governed'
CH11_OLD_END = '## 8. God has a heart and a soul'
CH11_NEW = '''## 7. The inner being is governed

In some verses Scripture takes the words it uses for ruling, serving, guarding and judging in society and turns them inward.

- **Ruling:** "he who rules his spirit [is better] than he who takes a city" (Proverbs 16:32). "Let the peace of Christ rule in your hearts" (Colossians 3:15).
- **Guarding:** "Keep your heart with all vigilance" (Proverbs 4:23). "Keep your soul diligently, lest you forget" (Deuteronomy 4:9). "Guard yourselves in your spirit" (Malachi 2:15).
- **Serving:** "I myself serve the law of God with my mind, but with my flesh I serve the law of sin" (Romans 7:25).
- **Judging:** "whenever our heart condemns us, God is greater than our heart" (1 John 3:20).

The words for ruling and guarding are used of the inner being: "A man without self-control is like a city broken into and left without walls" (Proverbs 25:28).

### Authority as a standing

When I read the verses that speak of ruling, dominion and authority, I expected to find ruling as something the inner being does, as it fears or wants. That is not what most of them show. In most of them authority is a place a person stands in, toward others and before God. It is given and received, held and used, set aside, wanted, offered and refused, resented, taken away, and lived under. And it does not act alone. In nearly every passage another inner act is the one moving, and the authority is where it moves, or what it moves toward.

I hold this as a first reading. The verses have not yet been read from this side as a whole, and I may be reading it in.

**Given before it is held.**
- "You would have no authority over me at all unless it had been given you from above" (John 19:11). "For there is no authority except from God, and those that exist have been instituted by God" (Romans 13:1).
- Even power over what a person already owns is given: "Everyone also to whom God has given wealth and possessions and power to enjoy them, and to accept his lot and rejoice in his toil — this is the gift of God" (Ecclesiastes 5:19). And it can be withheld: "yet God does not give him power to enjoy them, but a stranger enjoys them" (6:2).
- It is received from men: Saul acted "after receiving authority from the chief priests" (Acts 26:10). It follows money: "The rich rules over the poor, and the borrower is the slave of the lender" (Proverbs 22:7). In marriage each holds it for the other: "the wife does not have authority over her own body, but the husband does. Likewise the husband does not have authority over his own body, but the wife does" (1 Corinthians 7:4).
- So the question asked of authority is where it comes from. Jesus was asked, "By what authority are you doing these things, and who gave you this authority?" His questioners would not answer the same question about John, "we are afraid of the crowd", and said, "We do not know" (Matthew 21:23–27).

**What moves inside it.** The same standing is filled by very different acts.
- **Fear.** Pilate "was even more afraid" (John 19:8), and then said, "Do you not know that I have authority to release you and authority to crucify you?" (19:10). I read his claim as coming out of his fear.
- **Pride.** "Is not this great Babylon, which I have built by my mighty power as a royal residence and for the glory of my majesty?" (Daniel 4:30). The psalmist, given dominion over the works of God's hands, answers the other way, with wonder: "what is man that you are mindful of him", and "O Lord, our Lord, how majestic is your name in all the earth!" (Psalm 8:4, 9).
- **Wanting it, and trying to buy it.** Simon offered money: "Give me this power also". Peter: "your heart is not right before God" (Acts 8:19, 21).
- **Hatred.** Joseph's brothers: "Are you indeed to reign over us? Or are you indeed to rule over us?" So they hated him even more for his dreams and for his words (Genesis 37:8).
- **Conviction and fury.** "I myself was convinced that I ought to do many things in opposing the name of Jesus of Nazareth"; "in raging fury against them I persecuted them" (Acts 26:9, 11).
- **Faith.** The centurion: "For I too am a man under authority, with soldiers under me." Jesus "marveled": "with no one in Israel have I found such faith" (Matthew 8:9–10).
- **Care for another.** Paul argues that a right is his, and then: "we have not made use of this right, but we endure anything rather than put an obstacle in the way of the gospel of Christ" (1 Corinthians 9:12). To others: "take care that this right of yours does not somehow become a stumbling block to the weak" (8:9). The authority "the Lord gave for building you up and not for destroying you" (2 Corinthians 10:8) he would rather not have to be "severe in my use of" (13:10).
- **Joy.** "do not rejoice in this, that the spirits are subject to you, but rejoice that your names are written in heaven" (Luke 10:20). "Not that we lord it over your faith, but we work with you for your joy" (2 Corinthians 1:24).
- **The fear of God, as its limit.** "You shall not rule over him ruthlessly but shall fear your God" (Leviticus 25:43).
- **Knowing who rules.** "your kingdom shall be confirmed for you from the time that you know that Heaven rules" (Daniel 4:26).

One man shows the difference. Saul's authority from the chief priests went with conviction and raging fury. Paul's authority from the Lord goes with restraint, and with "we are glad when we are weak and you are strong" (2 Corinthians 13:9). I read the authority changing with where it comes from and with what moves in it.

**Turned round.** Jesus does not deny that rulers rule. "The kings of the Gentiles exercise lordship over them, and those in authority over them are called benefactors. But not so with you. Rather, let the greatest among you become as the youngest, and the leader as one who serves" (Luke 22:25–26). He said it when "A dispute also arose among them, as to which of them was to be regarded as the greatest" (22:24). Elders are to shepherd "not under compulsion, but willingly", "not domineering over those in your charge, but being examples to the flock" (1 Peter 5:2–3).

**Its limits, and whose the ruled are.** The law gives the limit three times, each on another ground: the ruler's fear of God (Leviticus 25:43), brotherhood, "over your brothers the people of Israel you shall not rule, one over another ruthlessly" (25:46), and the onlooker, "He shall not rule ruthlessly over him in your sight" (25:53). Behind all three: "For it is to me that the people of Israel are servants" (25:55). A master is told to "stop your threatening, knowing that he who is both their Master and yours is in heaven" (Ephesians 6:9). Where the limit is gone, the verses name what rose in its place. The shepherds fed themselves, did not strengthen the weak or seek the lost, "and with force and harshness you have ruled them", and the sheep "were scattered, because there was no shepherd" (Ezekiel 34:2–5). "A ruler who lacks understanding is a cruel oppressor, but he who hates unjust gain will prolong his days" (Proverbs 28:16).

**Offered, sought, refused.** "Rule over us … for you have saved us from the hand of Midian." Gideon: "I will not rule over you, and my son will not rule over you; the Lord will rule over you" (Judges 8:22–23). Offered a place as third ruler, Daniel said, "Let your gifts be for yourself, and give your rewards to another. Nevertheless, I will read the writing to the king" (Daniel 5:17). The devil offered all authority for worship, and was refused (Luke 4:6–8; 13.3). Gideon's son sought it through kinship: "Remember also that I am your bone and your flesh", and "their hearts inclined to follow Abimelech, for they said, 'He is our brother'" (Judges 9:2–3). He then killed his seventy brothers (9:5).

**Living under it.** Under rule the verses tell of crying out, and of fear with no cause: "after they had rest they did evil again before you, and you abandoned them to the hand of their enemies, so that they had dominion over them. Yet when they turned and cried to you, you heard from heaven" (Nehemiah 9:28). "Those who hate you shall rule over you, and you shall flee when none pursues you" (Leviticus 26:17). Rule can also be accepted as how things are: "Do you not know that the Philistines are rulers over us?", said the men of Judah, and bound Samson to hand him over (Judges 15:11–12). And God's own rule can be longed for: "We have become like those over whom you have never ruled, like those who are not called by your name" (Isaiah 63:19).

**Ruling within.** Even the verses in which a person rules inside himself join the rule to another act. "Whoever is slow to anger is better than the mighty, and he who rules his spirit than he who takes a city" (Proverbs 16:32). "Its desire is for you, and you must rule over it" (Genesis 4:7). A man "having his desire under control" (1 Corinthians 7:37). "'All things are lawful for me,' but I will not be dominated by anything" (1 Corinthians 6:12): what a man is free to do can come to rule him. Elsewhere God is asked: "Keep back your servant also from presumptuous sins; let them not have dominion over me!" (Psalm 19:13). Or it is grace: "sin will have no dominion over you, since you are not under law but under grace" (Romans 6:14), with the command two verses before, "Let not sin therefore reign in your mortal body" (6:12). And one thing no one rules: "No man has power to retain the spirit, or power over the day of death" (Ecclesiastes 8:8).

Where this touches the heart, the soul, the flesh, conscience and death, it is in those chapters. What it says of God, angels, other spirits and the creatures is in 13.1 to 13.4.

*Working note, not part of the narrative text.* Added 2026-10-12 from the first reading of the ruling and authority verses, on the researcher's instruction. Researcher: authority, rule and having power look "more of a state or status that works in collaboration with other characteristics and parties, but this is not yet strongly emerging"; the inner-being meaning of authority has not yet been explored to the full, and the material may need to be read again from that side (OT-100). The title of this section, and of this chapter, are under question.

'''

# ---------------------------------------------------------------- other chapters: (mode, anchor, text)
OPS = {
'04-the-heart-': [
 ('after_prefix', '- **It remembers and holds.**',
  '- **It watches what people do with power.** "All this I observed while applying my heart to all that is done under the sun, when man had power over man to his hurt" (Ecclesiastes 8:9).'),
 ('after_prefix', '- **A heart lifted up.**',
  '  - The words of that heart are given earlier: "Is not this great Babylon, which I have built by my mighty power as a royal residence and for the glory of my majesty?" "While the words were still in the king\'s mouth, there fell a voice from heaven" (Daniel 4:30–31). He had been told that his kingdom would be confirmed "from the time that you know that Heaven rules" (4:26). I read the boast as that heart speaking.\n'
  '- **A heart not right, wanting power.** Simon offered money: "Give me this power also". Peter: "your heart is not right before God … pray to the Lord that, if possible, the intent of your heart may be forgiven you" (Acts 8:19, 21–22).\n'
  '- **Hearts inclined by kinship.** Abimelech asked the men of Shechem to choose one ruler over seventy, "Remember also that I am your bone and your flesh", and "their hearts inclined to follow Abimelech, for they said, \'He is our brother\'" (Judges 9:2–3).\n'
  '- **No one comes near of his own heart.** Of the ruler to come: "I will make him draw near, and he shall approach me, for who would dare of himself to approach me? declares the Lord" (Jeremiah 30:21). The words rendered "dare of himself" carry the word for the heart. The nearness is God\'s doing.'),
],
'05-the-soul-': [
 ('after_prefix', 'The same soul blesses the Lord:',
  'The psalm ends as it began, and sets the soul among all his works under his rule: "Bless the Lord, all his works, in all places of his dominion. Bless the Lord, O my soul!" (Psalm 103:22).'),
],
'07-flesh-': [
 ('after_prefix', '- **Kin.**',
  '  - Kinship is used to win rule. Abimelech: "Remember also that I am your bone and your flesh", and the hearts of Shechem "inclined to follow Abimelech, for they said, \'He is our brother\'" (Judges 9:2–3). He then killed his seventy brothers (9:5).\n'
  '  - And flesh and blood is set beside powers that are not: "For we do not wrestle against flesh and blood, but against the rulers, against the authorities" (Ephesians 6:12; 13.3).'),
 ('after_prefix', 'The same letters say what is to be done with these desires.',
  'Jude sets the same acts together: "relying on their dreams, defile the flesh, reject authority, and blaspheme the glorious ones" (Jude 8). Against them he sets the archangel, who "did not presume to pronounce a blasphemous judgment, but said, \'The Lord rebuke you\'" (9; 13.2). They "blaspheme all that they do not understand" (10).'),
],
'08-conscience-and-bosom-': [
 ('replace_prefix', '- It is **weak, defiled, wounded, seared**:',
  '- It is **weak, defiled, wounded, seared**: "their conscience, being weak, is defiled" (1 Corinthians 8:7). To wound a weak conscience is to "sin against Christ" (8:12). The wound comes from another\'s freedom used without care: "take care that this right of yours does not somehow become a stumbling block to the weak" (8:9). Some have consciences "seared" (1 Timothy 4:2). "Both their minds and their consciences are defiled" (Titus 1:15).'),
 ('replace_prefix', '- It stands **beside the fear of wrath**',
  '- It stands **beside the fear of wrath** as a reason to obey: "Therefore one must be in subjection, not only to avoid God\'s wrath but also for the sake of conscience" (Romans 13:5). The authority is "an avenger who carries out God\'s wrath on the wrongdoer" (13:4). Paul gives two reasons, and conscience is the second (10.13). The passage opens with where the authority comes from: "there is no authority except from God" (13:1). I read the conscience here as answering to that source, not only to the sword.'),
],
'02-life-breath-and-death-': [
 ('replace_text', 'The psalm does not say what being received involves, and I do not fill it in.',
  'The psalm does not say what being received involves, and I do not fill it in. Of those who trust in their wealth it says, "death shall be their shepherd, and the upright shall rule over them in the morning" (49:14), and it draws a word for the living from this: "Be not afraid when a man becomes rich" (49:16).'),
],
'13-01-divine-': [
 ('before_prefix', '---\n\n*Working note, not part of the narrative text.* The wider verses in which God chooses', '''## Ruling

The words for ruling, dominion and authority are used of God more than of anyone else. Here they are read for what they say of him. What a person does with the authority he gives is in Chapter 11, section 7.

**He rules over all.** David blesses him: "Both riches and honor come from you, and you rule over all" (1 Chronicles 29:12). Jehoshaphat prays with it: "You rule over all the kingdoms of the nations. In your hand are power and might, so that none is able to withstand you" (2 Chronicles 20:6). "Dominion and fear are with God; he makes peace in his high heaven" (Job 25:2). "You rule the raging of the sea; when its waves rise, you still them" (Psalm 89:9). "who rules by his might forever, whose eyes keep watch on the nations — let not the rebellious exalt themselves" (Psalm 66:7). "For kingship belongs to the Lord, and he rules over the nations" (Psalm 22:28).

**His rule is to be known.** "that they may know that God rules over Jacob to the ends of the earth" (Psalm 59:13). A king was driven out "till you know that the Most High rules the kingdom of men and gives it to whom he will" (Daniel 4:25), and when his reason returned he blessed him, "for his dominion is an everlasting dominion" (4:34; *Willing*, above).

**He gives authority and takes it away.** "the God of heaven has given the kingdom, the power, and the might, and the glory" (Daniel 2:37). Of a steward removed: "will commit your authority to his hand. And he shall be a father to the inhabitants of Jerusalem" (Isaiah 22:21). "I will give over the Egyptians into the hand of a hard master" (Isaiah 19:4). "The Lord has broken the staff of the wicked, the scepter of rulers" (Isaiah 14:5). Gideon, offered rule, named the one who rules: "the Lord will rule over you" (Judges 8:23). And the potter's question: "Has the potter no right over the clay?" (Romans 9:21).

**The Son's authority.** "All authority in heaven and on earth has been given to me" (Matthew 28:18). "that you may know that the Son of Man has authority on earth to forgive sins" (Matthew 9:6). "he has given him authority to execute judgment, because he is the Son of Man" (John 5:27). "you have given him authority over all flesh, to give eternal life to all whom you have given him" (John 17:2). Over his own life: "I have authority to lay it down, and I have authority to take it up again. This charge I have received from my Father" (John 10:18). He gives it on: "he called to him his twelve disciples and gave them authority over unclean spirits" (Matthew 10:1). He is "the head of all rule and authority" (Colossians 2:10); "He disarmed the rulers and authorities and put them to open shame" (2:15; 13.3).

**The Father's own authority, and a limit for us.** "It is not for you to know times or seasons that the Father has fixed by his own authority" (Acts 1:7).

**The ruler to come.** "the government shall be upon his shoulder, and his name shall be called Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace" (Isaiah 9:6). "he shall speak peace to the nations; his rule shall be from sea to sea" (Zechariah 9:10). "the counsel of peace shall be between them both" (Zechariah 6:13). His rule comes with peace in each of these verses.

**The soul's answer.** "Bless the Lord, all his works, in all places of his dominion. Bless the Lord, O my soul!" (Psalm 103:22; Chapter 5).

'''),
],
'13-02-angels-': [
 ('before_prefix', '*Verses are gathered here',
  '''Angels have authority, and some did not keep it. "another angel came out from the altar, the angel who has authority over the fire" (Revelation 14:18). "another angel coming down from heaven, having great authority, and the earth was made bright with his glory" (18:1). But "the angels who did not stay within their own position of authority, but left their proper dwelling, he has kept in eternal chains under gloomy darkness until the judgment of the great day" (Jude 6). Against those who "reject authority, and blaspheme the glorious ones", Jude sets the archangel: "when the archangel Michael, contending with the devil, was disputing about the body of Moses, he did not presume to pronounce a blasphemous judgment, but said, 'The Lord rebuke you'" (Jude 8–9; Chapter 7). The archangel leaves the rebuke to the Lord.

Jacob "strove with the angel and prevailed; he wept and sought his favor" (Hosea 12:4). The prevailing is told as weeping and seeking favour.

A wife "ought to have a symbol of authority on her head, because of the angels" (1 Corinthians 11:10). The verse does not explain the angels, and I add nothing.

'''),
],
'13-03-other-spirits-': [
 ('before_prefix', '*Verses are gathered here',
  '''The struggle is with authorities that are not human. "For we do not wrestle against flesh and blood, but against the rulers, against the authorities, against the cosmic powers over this present darkness, against the spiritual forces of evil in the heavenly places" (Ephesians 6:12). What is asked is to stand: "Therefore take up the whole armor of God, that you may be able to withstand in the evil day, and having done all, to stand firm" (6:13).

Authority over them is given, and it is not to be the ground of joy. "The seventy-two returned with joy, saying, 'Lord, even the demons are subject to us in your name!'" Jesus: "I have given you authority to tread on serpents and scorpions, and over all the power of the enemy … Nevertheless, do not rejoice in this, that the spirits are subject to you, but rejoice that your names are written in heaven" (Luke 10:17–20). Where it is not given, a spirit masters men: "the man in whom was the evil spirit leaped on them, mastered all of them and overpowered them, so that they fled out of that house naked and wounded" (Acts 19:16).

Their authority is handed on and has its hour. At his arrest: "But this is your hour, and the power of darkness" (Luke 22:53). In the vision, "the dragon gave his power and his throne and great authority" to the beast, and "they worshiped the dragon, for he had given his authority to the beast" (Revelation 13:2, 4). The same powers were disarmed and put "to open shame" (Colossians 2:15; 13.1).

'''),
],
'13-04-nature-': [
 ('before_prefix', '*Verses are gathered here',
  '''**Lights that rule.** "And God made the two great lights — the greater light to rule the day and the lesser light to rule the night — and the stars" (Genesis 1:16). The psalm gives the same with its refrain: "the sun to rule over the day, for his steadfast love endures forever; the moon and stars to rule over the night, for his steadfast love endures forever" (Psalm 136:8–9).

**Creatures under man's dominion.** "And let them have dominion over the fish of the sea and over the birds of the heavens and over the livestock and over all the earth" (Genesis 1:26). "You have given him dominion over the works of your hands; you have put all things under his feet, all sheep and oxen, and also the beasts of the field" (Psalm 8:6–7). The creatures are given under man by the one who made them both (Chapter 11, section 7).

'''),
],
}


def apply(text, mode, anchor, new):
    lines = text.split('\n')
    if mode == 'replace_text':
        assert text.count(anchor) == 1, anchor
        return text.replace(anchor, new)
    idx = [i for i, l in enumerate(lines) if l.startswith(anchor)]
    if mode == 'before_prefix' and '\n' in anchor:
        assert text.count(anchor) == 1, anchor
        return text.replace(anchor, new + anchor)
    assert len(idx) == 1, (anchor, len(idx))
    i = idx[0]
    if mode == 'after_prefix':
        lines.insert(i + 1, new)
    elif mode == 'before_prefix':
        lines.insert(i, new.rstrip('\n') + '\n')
    elif mode == 'replace_prefix':
        lines[i] = new
    return '\n'.join(lines)


def bump(path):
    base = os.path.basename(path)
    m = re.match(r'(.+)-v(\d+)-\d{8}\.md$', base)
    return os.path.join(NARR, f'{m.group(1)}-v{int(m.group(2)) + 1}-{DATE}.md')


# quote check
con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
norm = lambda t: re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', t.lower())).strip()
CORPUS = ' '.join(norm(t or '') for (t,) in con.execute('select text from verse where deleted=0 order by id'))
VERSES = [norm(t or '') for (t,) in con.execute('select text from verse where deleted=0')]


# checked by hand: existing bracketed line (Pro 16:32); the researcher's words; Psa 8:6-7 joined at a comma
ALLOW = ('he who rules his spirit [is better]', 'more of a state or status', 'You have given him dominion over the works of your hands; you have put all things under his feet, all sheep')


def check(text):
    bad = []
    for q in re.findall(r'(?:^|(?<=[\s(*—]))"([^"\n]+?)"(?=[*\s).,;:!?]|$)', text, flags=re.M):
        for part in q.split('…'):
            p = norm(part)
            if len(p.split()) < 3 or part.startswith(ALLOW):
                continue
            # a part may span verses: accept if every sentence-chunk is found
            chunks = [norm(c) for c in re.split(r'[.;?!]\s', part) if len(norm(c).split()) >= 3]
            if not all(any(c in v for v in VERSES) for c in chunks):
                bad.append(part)
    return bad


writes = []
new11 = None
f11 = current('11-patterns-of-the-inner-life-')
t = open(f11, encoding='utf-8').read()
a, b = t.index(CH11_OLD_START), t.index(CH11_OLD_END)
writes.append((f11, t[:a] + CH11_NEW + t[b:], CH11_NEW))
for prefix, ops in OPS.items():
    f = current(prefix)
    t = open(f, encoding='utf-8').read()
    ins = ''
    for mode, anchor, new in ops:
        t = apply(t, mode, anchor, new)
        ins += new + '\n'
    writes.append((f, t, ins))

total_bad = 0
for f, t, ins in writes:
    bad = check(ins)
    total_bad += len(bad)
    print(os.path.basename(f), '->', os.path.basename(bump(f)), '| quote parts failing:', len(bad))
    for x in bad:
        print('    !', x[:160])
if DRY or total_bad:
    print('dry run' if DRY else 'quote failures: nothing written')
    sys.exit(0 if DRY else 1)
for f, t, ins in writes:
    open(bump(f), 'w', encoding='utf-8').write(t)
    shutil.move(f, os.path.join(NARR, 'archive', os.path.basename(f)))
print('written', len(writes), 'files')
