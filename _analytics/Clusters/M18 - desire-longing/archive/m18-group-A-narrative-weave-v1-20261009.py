"""Weave of M18 group A (desire, craving, longing) into the narrative (#1993, item F), 2026-10-09.

Reading: m18-group-A-reading-v1-20261009.md. Register: m18-group-A-register-v1-20261009.csv.
Same mechanics as m18-m02-narrative-weave-v1-20261009.py.
"""
import glob, os, re, shutil, sys

NARR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DATE = '20261009'

OPS = {
'10-06-': [
 ('before_line', 'Before that, the first seeing in Scripture is God\'s',
  '''A law case starts in the same place: *"you see among the captives a beautiful woman, and you desire to take her to be your wife"* (Deuteronomy 21:11). Its end, when the delight is gone, is below (*Delight*). In Ezekiel the look is at pictures: *"She saw men portrayed on the wall, the images of the Chaldeans"*, and she *"lusted after the Assyrians … all of them desirable young men"* (Ezekiel 23:14, 12).

The servant of Isaiah is the opposite case: *"he had no form or majesty that we should look at him, and no beauty that we should desire him. He was despised and rejected by men"* (Isaiah 53:2–3). The woman's look at the tree found something "to be desired" and took it. This look found nothing to desire and turned away. I read that the one who *"has borne our griefs"* (53:4) is the one the desiring eye passed over.
'''),
 ('before_line', '## Aimed at nothing, and enjoyment given',
  '''## Coveting

The commandment always names the neighbour's thing: *"You shall not covet your neighbor's house; you shall not covet your neighbor's wife, or his male servant, or his female servant, or his ox, or his donkey, or anything that is your neighbor's"* (Exodus 20:17). Deuteronomy uses two verbs, "covet" for the wife and "desire" for the house and the rest (Deuteronomy 5:21). I read coveting as wanting defined by a relationship: it is wanting what is another's. Paul gives the answer as a love for the same neighbour: *"You shall not covet," and any other commandment, are summed up in this word: "You shall love your neighbor as yourself"* (Romans 13:9).

Coveting runs in the order the woman's look did: seeing, desiring, taking. Achan says it himself: *"when I saw among the spoil a beautiful cloak from Shinar, and 200 shekels of silver, and a bar of gold weighing 50 shekels, then I coveted them and took them. And see, they are hidden in the earth inside my tent"* (Joshua 7:21; 10.11). He adds the fourth act, hiding. Micah adds the night and the power: *"Woe to those who devise wickedness and work evil on their beds! When the morning dawns, they perform it, because it is in the power of their hand. They covet fields and seize them, and houses, and take them away"* (Micah 2:1–2). The covetous wish is planned in bed and done when there is power to do it.

The command itself names the desire, and sin uses the naming: *"I would not have known what it is to covet if the law had not said, 'You shall not covet.' But sin, seizing an opportunity through the commandment, produced in me all kinds of covetousness"* (Romans 7:7–8). I read the command as making the desire known, and sin as using that very knowledge to multiply it.

What is coveted can be a snare: *"You shall not covet the silver or the gold that is on them or take it for yourselves, lest you be ensnared by it"* (Deuteronomy 7:25). Proverbs sets taking against growing: *"Whoever is wicked covets the spoil of evildoers, but the root of the righteous bears fruit"* (Proverbs 12:12). And Paul shows the opposite lived: *"I coveted no one's silver or gold or apparel. You yourselves know that these hands ministered to my necessities … 'It is more blessed to give than to receive'"* (Acts 20:33–35). The hands that might have taken work, and give.
'''),
 ('append_line', 'Desire can be pictured as heat and as a drive that no one holds back.',
  ' Jeremiah ties the heat to fullness: *"When I fed them to the full, they committed adultery … They were well-fed, lusty stallions, each neighing for his neighbor\'s wife"* (Jeremiah 5:7–8). The same is said of Jeshurun, who *"grew fat, and kicked"* (13.1, *Jealousy*). Fullness, then turning away; and the picture makes the desire animal and loud.'),
 ('after_line', '- **On war and on taking:**',
  '- **On scoffing:** *"How long, O simple ones, will you love being simple? How long will scoffers delight in their scoffing and fools hate knowledge?"* (Proverbs 1:22), said by Wisdom as she calls.'),
 ('after_line', 'Waking can show the same mastery.',
  '''The verses give desire the verbs of a person acting on the one who wants. It is obeyed under sin as king: *"Let not sin therefore reign in your mortal body, to make you obey its passions"* (Romans 6:12). It is followed: *"grumblers, malcontents, following their own sinful desires"* (Jude 16); *"scoffers will come in the last days with scoffing, following their own sinful desires. They will say, 'Where is the promise of his coming?'"* (2 Peter 3:3–4). It picks what is heard: *"having itching ears they will accumulate for themselves teachers to suit their own passions, and will turn away from listening to the truth and wander off into myths"* (2 Timothy 4:3–4). The itch is a want to be scratched, and the teachers are gathered to scratch it. It keeps learning from arriving: *"led astray by various passions, always learning and never able to arrive at a knowledge of the truth"* (3:6–7). It deceives: *"your old self … is corrupt through deceitful desires"* (Ephesians 4:22). It baits: *"each person is tempted when he is lured and enticed by his own desire"* (James 1:14). That is the fisherman's or hunter's picture, and it comes before the conceiving of 1:15. It takes captive: *"the treacherous are taken captive by their lust"* (Proverbs 11:6). It crouches like an animal at the threshold: *"sin is crouching at the door. Its desire is for you, and you must rule over it"* (Genesis 4:7). And it can be inherited: *"You are of your father the devil, and your will is to do your father's desires"* (John 8:44). I read these as one act seen from different sides: the want leads, and the one who wants follows.

What the verses set against it is not a stronger want either. In two places the uncontrolled desire stands beside not knowing God: *"not in the passion of lust like the Gentiles who do not know God"* (1 Thessalonians 4:5); *"do not be conformed to the passions of your former ignorance"* (1 Peter 1:14). Against deceitful desires stands a mind made new: *"to be renewed in the spirit of your minds, and to put on the new self"* (Ephesians 4:23–24). Against passions that pass stands the will of God, which lasts: *"so as to live for the rest of the time in the flesh no longer for human passions but for the will of God. For the time that is past suffices for doing what the Gentiles want to do"* (1 Peter 4:2–3); *"the desires of the flesh and the desires of the eyes and pride of life … the world is passing away along with its desires, but whoever does the will of God abides forever"* (1 John 2:16–17). And there is a share in his nature: *"partakers of the divine nature, having escaped from the corruption that is in the world because of sinful desire"* (2 Peter 1:4).'''),
 ('after_line', 'A satisfaction can also be only a dream.',
  'Two hungers wait at a gate. Lazarus *"desired to be fed with what fell from the rich man\'s table"* (Luke 16:21). The younger son was *"longing to be fed with the pods that the pigs ate, and no one gave him anything. But when he came to himself"* (Luke 15:16–17). In both, the want goes unanswered by the one who could answer it. For the younger son, the unmet want is where he comes to himself.'),
 ('append_line', 'What is wanted against God can be given in anger.',
  ''' The verses name what went before the craving: *"they soon forgot his works; they did not wait for his counsel. But they had a wanton craving in the wilderness, and put God to the test in the desert; he gave them what they asked, but sent a wasting disease among them"* (Psalm 106:13–15). And what it was after it was fed: *"they ate and were well filled, for he gave them what they craved. But before they had satisfied their craving"* (Psalm 78:29–30). They were filled, and the craving was not satisfied. I read that the craving was not the hunger, and filling the stomach did not end it. The place kept the name: *"Kibroth-hattaavah, because there they buried the people who had the craving"* (Numbers 11:34), the graves of craving. Paul draws the lesson: *"these things took place as examples for us, that we might not desire evil as they did"* (1 Corinthians 10:6).'''),
 ('after_line', 'The proverbs judge a desire by where it ends:',
  'They set desire against dread: *"What the wicked dreads will come upon him, but the desire of the righteous will be granted"* (Proverbs 10:24). They name where a self-seeking desire leads: *"Whoever isolates himself seeks his own desire; he breaks out against all sound judgment"* (18:1). And they set the craving that never ends against giving: *"All day long he craves and craves, but the righteous gives and does not hold back"* (21:26), the verse after *"The desire of the sluggard kills him"*.'),
 ('after_line', 'Wanting can reach past this life.',
  'Desire is shown by not going back: *"they desire a better country, that is, a heavenly one. … If they had been thinking of that land from which they had gone out, they would have had opportunity to return"* (Hebrews 11:15–16). And wanting itself grows old: *"desire fails, because man is going to his eternal home, and the mourners go about the streets"* (Ecclesiastes 12:5; 10.12).'),
 ('after_line', 'Longing does not give life by itself.',
  '''Longing for God's word is pictured as breathing hard: *"I open my mouth and pant, because I long for your commandments"* (Psalm 119:131). It is weighed by worth and by taste: *"More to be desired are they than gold, even much fine gold; sweeter also than honey and drippings of the honeycomb"* (Psalm 19:10). It can follow a choice: *"I have chosen your precepts. I long for your salvation, O Lord, and your law is my delight"* (119:173–174). And it can be laid open in sickness, when the nearest stand far off: *"O Lord, all my longing is before you; my sighing is not hidden from you"* (Psalm 38:9, 11; 10.11).

Some longing to see is not met in its time: *"many prophets and righteous people longed to see what you see, and did not see it"* (Matthew 13:17). *"The days are coming when you will desire to see one of the days of the Son of Man, and you will not see it. And they will say to you, 'Look, there!' or 'Look, here!' Do not go out or follow them"* (Luke 17:22–23). The longing is real, and it is not to be met by following whoever says "Look, here!"

A day can be wanted wrongly. *"Woe to you who desire the day of the Lord! Why would you have the day of the Lord? It is darkness, and not light, as if a man fled from a lion, and a bear met him"* (Amos 5:18–19). Jeremiah says the opposite of himself: *"nor have I desired the day of sickness"* (Jeremiah 17:16). The people want a day they do not understand, and the picture is of fleeing one danger straight into another. The prophet disowns wanting the disaster he has to announce.'''),
 ('after_line', 'Wanting can be aimed at a person.',
  '''Paul's longing is joined each time to something else. To memory: *"As I remember your tears, I long to see you, that I may be filled with joy"* (2 Timothy 1:4). To Christ's own affection: *"how I yearn for you all with the affection of Christ Jesus"* (Philippians 1:8), after *"I hold you in my heart"* (1:7). To distress for another's distress: Epaphroditus *"has been longing for you all and has been distressed because you heard that he was ill"* (2:26). It runs both ways, and it comforts: *"you … long to see us, as we long to see you—for this reason, brothers, in all our distress and affliction we have been comforted about you"* (1 Thessalonians 3:6–7). It is joined to prayer: *"they long for you and pray for you, because of the surpassing grace of God upon you"* (2 Corinthians 9:14). It holds across years of hindrance: *"I have longed for many years to come to you"* (Romans 15:23). It passes on through a third person: God *"comforted us by the coming of Titus, and not only by his coming but also by the comfort with which he was comforted by you, as he told us of your longing"* (2 Corinthians 7:6–7). And it ends in a charge: *"whom I love and long for, my joy and crown, stand firm thus in the Lord"* (Philippians 4:1). Shechem's longing, above, came after violence. Paul's gives, prays, remembers and carries another's distress.

A longing for home can stand beside fear. Laban says, *"you have gone away because you longed greatly for your father's house"*. Jacob answers, *"Because I was afraid"* (Genesis 31:30–31).

The bride's desire is pictured as shade and taste: *"With great delight I sat in his shadow, and his fruit was sweet to my taste"* (Song of Songs 2:3); *"he is altogether desirable. This is my beloved and this is my friend"* (5:16). And what is to be desired in a person is named: *"What is desired in a man is steadfast love"* (Proverbs 19:22).'''),
 ('before_line', '## Jealousy and envy',
  '''One word for desire, *tĕšûqāh*, is used three times, and each time differently. *"Your desire shall be for your husband, and he shall rule over you"* (Genesis 3:16): after the fall, desire stands with rule. *"sin is crouching at the door. Its desire is for you, and you must rule over it"* (4:7): the desire is sin's, aimed at Cain, and the rule is his to exercise. *"I am my beloved's, and his desire is for me"* (Song of Songs 7:10): it is mutual, and nothing in the verse rules. The word stays the same. What differs is whose the desire is, and whether rule stands beside it. The three are set side by side by their wording; the reading of them together is mine (Chapter 11, §4).
'''),
 ('append_line', 'Psalm 37 opens with the same pair, envy and heat:',
  ' Proverbs adds the wish for company: *"Be not envious of evil men, nor desire to be with them, for their hearts devise violence"* (Proverbs 24:1–2).'),
 ('after_line', 'What is desired can be taken away.',
  '''Before it was a sign to the people it was a man's wife: *"Son of man, behold, I am about to take the delight of your eyes away from you at a stroke; yet you shall not mourn or weep … So I spoke to the people in the morning, and at evening my wife died"* (Ezekiel 24:16–18). The prophet's own delight was taken first, and he was told not to mourn it.

The loss takes many forms. Stripping: *"The enemy has stretched out his hands over all her precious things"* (Lamentations 1:10). A plea from the ruins: *"all our pleasant places have become ruins. Will you restrain yourself at these things, O Lord?"* (Isaiah 64:11–12). A call to the complacent: *"Beat your breasts for the pleasant fields"* (32:11–12). Pleasure built on oppression and withheld: *"because you trample on the poor … you have planted pleasant vineyards, but you shall not drink their wine"* (Amos 5:11). Longing that can do nothing: *"your eyes look on and fail with longing for them all day long, but you shall be helpless"* (Deuteronomy 28:32). And slow, silent loss: *"When you discipline a man with rebukes for sin, you consume like a moth what is dear to him; surely all mankind is a mere breath!"* (Psalm 39:11). The moth takes what is dear without plunder or noise.'''),
 ('after_line', 'Greed harms more than the greedy.',
  '''The verses also give greed's reasons and its roots. A root: *"For the love of money is a root of all kinds of evils. It is through this craving that some have wandered away from the faith and pierced themselves with many pangs"* (1 Timothy 6:10). Refuge in the wrong place: *"See the man who would not make God his refuge, but trusted in the abundance of his riches and sought refuge in his own destruction!"* (Psalm 52:7). What he ran to was his ruin. Safety: *"Woe to him who gets evil gain for his house, to set his nest on high, to be safe from the reach of harm! … you have forfeited your life"* (Habakkuk 2:9–10). The picture is a bird nesting out of reach. Forgetting God: *"you … make gain of your neighbors by extortion; but me you have forgotten"* (Ezekiel 22:12). No contentment: *"Because he knew no contentment in his belly, he will not let anything in which he delights escape him"* (Job 20:20). And it can sit in the leaders, with a false peace: *"everyone is greedy for unjust gain; and from prophet to priest, everyone deals falsely. They have healed the wound of my people lightly, saying, 'Peace, peace,' when there is no peace"* (Jeremiah 6:13–14).

At a ruler's table Proverbs warns against the appetite itself: *"put a knife to your throat if you are given to appetite. Do not desire his delicacies, for they are deceptive food"*; and of riches, *"When your eyes light on it, it is gone, for suddenly it sprouts wings"* (Proverbs 23:2–5). At a stingy man's table the warning is about the host's heart: *"do not desire his delicacies, for he is like one who is inwardly calculating. 'Eat and drink!' he says to you, but his heart is not with you"* (23:6–7). A knife at the throat, riches with wings, and a host whose heart is elsewhere: the desire for the food is warned against because of what the food hides. *"Precious treasure and oil are in a wise man's dwelling, but a foolish man devours it"* (21:20).'''),
],
'13-01-': [
 ('before_line', '**Whom he is pleased with.**',
  '''**What he desires.** The verses also give his desire for a place, a people and a time:
- A place: *"For the Lord has chosen Zion; he has desired it for his dwelling place: 'This is my resting place forever; here I will dwell, for I have desired it'"* (Psalm 132:13–14). The other mountains are pictured looking on with envy: *"Why do you look with hatred, O many-peaked mountain, at the mount that God desired for his abode?"* (Psalm 68:16).
- His people, as his hope for them: *"I said, How I would set you among my sons, and give you a pleasant land, a heritage most beautiful of all nations. And I thought you would call me, My Father, and would not turn from following me. Surely, as a treacherous wife leaves her husband, so have you been treacherous to me"* (Jeremiah 3:19–20). His hope is spoken, and then its disappointment.
- His grief over what is his: *"they have made my pleasant portion a desolate wilderness. They have made it a desolation; desolate, it mourns to me. The whole land is made desolate, but no man lays it to heart"* (Jeremiah 12:10–11).
- His keeping of it: *"A pleasant vineyard, sing of it! I, the Lord, am its keeper; every moment I water it … I have no wrath"* (Isaiah 27:2–4).
- His word on the one who clings to him: *"Because he holds fast to me in love, I will deliver him; I will protect him, because he knows my name"* (Psalm 91:14).
- His guarding of what is left behind for worship: *"no one shall covet your land, when you go up to appear before the Lord your God three times in the year"* (Exodus 34:24).
- What comes to his house: *"the treasures of all nations shall come in, and I will fill this house with glory … The silver is mine, and the gold is mine"* (Haggai 2:7–8).
- His timing: *"When I please, I will discipline them"* (Hosea 10:10).
- The Son's desire: *"I have earnestly desired to eat this Passover with you before I suffer"* (Luke 22:15).
- Job hopes for God's longing: *"You would call, and I would answer you; you would long for the work of your hands"* (Job 14:15).
'''),
 ('after_line', '- "who chose me above your father',
  '- Not for what they were: *"It was not because you were more in number than any other people that the Lord set his love on you and chose you, for you were the fewest of all peoples, but it is because the Lord loves you"* (Deuteronomy 7:7–8). *"Yet the Lord set his heart in love on your fathers and chose their offspring after them … Circumcise therefore the foreskin of your heart"* (10:15–16). His set heart is answered by a call on theirs.'),
],
'13-04-': [
 ('after_line', '**The creatures\' thirst and hunger met.**',
  'When the water fails, the creatures are pictured turning to God: *"Even the beasts of the field pant for you because the water brooks are dried up"* (Joel 1:20). The same verb is used of the sun: it *"hastens to the place where it rises"* (Ecclesiastes 1:5), and of a person panting for God\'s commandments (Psalm 119:131; 10.6).'),
],
'10-07-': [
 ('after_line', '- **Set, beside a wrong love.**',
  '- **Set as an aim.** The word for ambition is used three times by Paul, and its aims are not what ambition usually seeks: *"I make it my ambition to preach the gospel, not where Christ has already been named"* (Romans 15:20); *"whether we are at home or away, we make it our aim to please him. For we must all appear before the judgment seat of Christ"* (2 Corinthians 5:9–10); *"aspire to live quietly, and to mind your own affairs, and to work with your hands"* (1 Thessalonians 4:11). Also: *"If anyone aspires to the office of overseer, he desires a noble task"* (1 Timothy 3:1). I read the aims as going where no one has gone, pleasing him wherever one is, and quietness.'),
],
'11-': [
 ('before_line', '- **The story around it.** A single verse',
  '''- **Whose desire, and whether rule stands beside it.** *tĕšûqāh*: "Your desire shall be for your husband, and he shall rule over you" (Genesis 3:16); sin's "desire is for you, and you must rule over it" (4:7); "I am my beloved's, and his desire is for me" (Song of Songs 7:10) (10.6).
- **What the panting reaches for.** The verb for panting or longing is used of a worn slave who "longs for the shadow" (Job 7:2), of the thirsty who "pant after his wealth" (Job 5:5), of the sun that "hastens" (Ecclesiastes 1:5), of the wild donkey "sniffing the wind" (Jeremiah 2:24), of the psalmist who pants for the commandments (Psalm 119:131), and of God, who will "gasp and pant" like a woman in labour (Isaiah 42:14). What it reaches for decides its character (10.6; 13.1; 13.4).'''),
],
'12-': [
 ('after_line', 'The heart is the place where wrongdoing starts',
  'The psalm names the inner self with a word that elsewhere means desire: *"there is no truth in their mouth; their inmost self is destruction; their throat is an open grave; they flatter with their tongue"* (Psalm 5:9). In Proverbs the same word is the captor: *"the treacherous are taken captive by their lust"* (Proverbs 11:6; 10.6).'),
 ('before_line', 'Isaiah shows the man who makes one',
  'Isaiah first says what the delight comes to: *"All who fashion idols are nothing, and the things they delight in do not profit. Their witnesses neither see nor know, that they may be put to shame"* (Isaiah 44:9).\n'),
],
'02-': [
 ('after_line', 'It comes to everyone.',
  'A death can go unmissed: of Jehoram, *"he departed with no one\'s regret"* (2 Chronicles 21:20). The word is the desire word: no one wanted him back.'),
 ('after_line', 'At the sea, fear set slavery against death',
  'Elihu warns against the other wish: *"Do not long for the night, when peoples vanish in their place"* (Job 36:20).'),
 ('after_line', 'The want for life is a want to see good:',
  'Job pictures a life of longing without rest: *"Like a slave who longs for the shadow, and like a hired hand who looks for his wages, so I am allotted months of emptiness, and nights of misery are apportioned to me"* (Job 7:2–3).'),
],
'10-02-': [
 ('after_line', '**Hearing goes both ways.**',
  'What a person listens to shows what he is: *"An evildoer listens to wicked lips, and a liar gives ear to a mischievous tongue"* (Proverbs 17:4).'),
],
}


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]


def apply(text, mode, anchor, ins):
    lines = text.split('\n')
    if mode == 'replace':
        assert text.count(anchor) == 1, ('replace count', anchor[:60], text.count(anchor))
        return text.replace(anchor, ins)
    idx = [i for i, l in enumerate(lines) if anchor in l]
    assert len(idx) == 1, (mode, anchor[:60], idx)
    i = idx[0]
    if mode == 'append_line':
        lines[i] += ins
    elif mode == 'after_line':
        if lines[i].startswith('- ') and ins.startswith('- '):
            lines[i + 1:i + 1] = [ins]
        else:
            lines[i + 1:i + 1] = ['', ins]
    elif mode == 'before_line':
        lines[i:i] = [ins.rstrip('\n'), '']
    return '\n'.join(lines)


dry = '--dry' in sys.argv
for prefix, ops in OPS.items():
    src = current(prefix)
    text = open(src, encoding='utf-8').read()
    for mode, anchor, ins in ops:
        text = apply(text, mode, anchor, ins)
    m = re.match(r'(.*-v)(\d+)-(\d{8})\.md$', os.path.basename(src))
    new = os.path.join(NARR, f'{m.group(1)}{int(m.group(2)) + 1}-{DATE}.md')
    print(os.path.basename(src), '->', os.path.basename(new))
    if dry: continue
    shutil.copy2(src, os.path.join(NARR, 'archive', os.path.basename(src)))
    open(new, 'w', encoding='utf-8').write(text)
    os.remove(src)
