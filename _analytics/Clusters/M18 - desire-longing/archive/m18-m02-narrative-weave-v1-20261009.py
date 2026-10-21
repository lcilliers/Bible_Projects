"""Weave of the M18 x M02 read-back into the narrative (#1993, handoff item C; OT-19), 2026-10-09.

Reading: m18-m02-inner-being-reading-v1-20261009.md. Register: m18-m02-validation-register-v1-20261009.csv.
Same mechanics as m18-m25-held-narrative-weave-v1-20261009.py (modes after_line, before_line, replace, append_line;
each anchor must match one line; prior version archived; new version v+1, today's date).
"""
import glob, os, re, shutil, sys

NARR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DATE = '20261009'

OPS = {
'13-01-': [
 ('before_line', "A person's jealousy is in 10.6 (*Jealousy and envy*).",
  '''- **What rouses it.** *"They stirred him to jealousy with strange gods; with abominations they provoked him to anger"* (Deuteronomy 32:16). The verses around it name what came before: *"Jeshurun grew fat, and kicked … then he forsook God who made him"* (32:15), and *"You were unmindful of the Rock that bore you"* (32:18). Again: *"they moved him to jealousy with their idols"* (Psalm 78:58). I read his jealousy as roused where the bond he made is given to another, after a fullness that kicked and a forgetting.
- **Answered in kind.** *"They have made me jealous with what is no god; they have provoked me to anger with their idols. So I will make them jealous with those who are no people"* (Deuteronomy 32:21). The measure of the answer is the offence itself: "no god" for "no people".
- **Against his own, as against an unfaithful wife.** *"I will judge you as women who commit adultery and shed blood are judged, and bring upon you the blood of wrath and jealousy"* (Ezekiel 16:38). *"I will direct my jealousy against you, that they may deal with you in fury"* (23:25). It is carried out by the lovers she once desired (*Stirring*, below).
- **Against one man who blesses himself.** *"the anger of the Lord and his jealousy will smoke against that man"* (Deuteronomy 29:20), the man who *"blesses himself in his heart, saying, 'I shall be safe'"* (29:19). It is set against an inner act of self-assurance.
- **For Zion, ending in his dwelling.** *"I am jealous for Zion with great jealousy, and I am jealous for her with great wrath"*, and the next words: *"I have returned to Zion and will dwell in the midst of Jerusalem"* (Zechariah 8:2–3).
- **Over the whole earth.** *"Neither their silver nor their gold shall be able to deliver them on the day of the wrath of the Lord. In the fire of his jealousy, all the earth shall be consumed"* (Zephaniah 1:18). *"For in my jealousy and in my blazing wrath I declare, On that day there shall be a great earthquake"*, and *"all the people who are on the face of the earth, shall quake at my presence"* (Ezekiel 38:19–20). Zephaniah's second word on the fire of his jealousy is followed at once by *"For at that time I will change the speech of the peoples to a pure speech, that all of them may call upon the name of the Lord"* (Zephaniah 3:8–9). The passage puts the fire and the pure speech side by side.
- **Jealous, and slow to anger.** *"The Lord is a jealous and avenging God … and keeps wrath for his enemies. The Lord is slow to anger and great in power"* (Nahum 1:2–3). Both are said in one breath. I do not reconcile them.
- **It ends, and something follows.** *"So will I satisfy my wrath on you, and my jealousy shall depart from you. I will be calm and will no more be angry"* (Ezekiel 16:42). The next verse names what had enraged him: *"Because you have not remembered the days of your youth"* (16:43). Its stated end can be knowing: *"And they shall know that I am the Lord—that I have spoken in my jealousy"* (5:13).
- **Asked about in lament.** *"How long, O Lord? Will you be angry forever? Will your jealousy burn like fire? Pour out your anger on the nations that do not know you"* (Psalm 79:5–6). The people ask for it to end on them and turn on others.
- **Shared by a man.** Phinehas *"was jealous with my jealousy"*, and the wrath turned back (Numbers 25:11; 10.6, 10.9).

I read one jealousy, aimed in different ways: against his people when they give the bond to another, for them when others scorn them, and over them, met with "more grace".
'''),
 ('after_line', '- A fast he does not accept:',
  '- What his anger gives way to: *"He does not retain his anger forever, because he delights in steadfast love"* (Micah 7:18). The reason the anger ends is what he delights in. Isaiah puts wrath and favour in one sentence: *"for in my wrath I struck you, but in my favor I have had mercy on you"* (Isaiah 60:10), as *"his favor is for a lifetime"* (Psalm 30:5; 10.13).'),
 ('after_line', 'and answers it with the potter',
  'Three verses on, his will and his patience stand in one question: *"What if God, desiring to show his wrath and to make known his power, has endured with much patience vessels of wrath prepared for destruction, in order to make known the riches of his glory for vessels of mercy"* (Romans 9:22–23). It is a question, "What if", and I leave it as one.'),
],
'10-06-': [
 ('after_line', 'Moses wants it given to all.',
  'Phinehas was also jealous for God, and his jealousy turned out otherwise. *"Phinehas … has turned back my wrath from the people of Israel, in that he was jealous with my jealousy among them"*. He was given *"my covenant of peace"*, *"because he was jealous for his God and made atonement for the people of Israel"* (Numbers 25:11–13; 10.9). Phinehas\'s jealousy was God\'s own, and it stood with the people and turned the wrath from them. Elijah\'s ended in "I, even I only, am left". I read that the same jealousy for God can stand with the people or end in standing alone.'),
 ('after_line', 'Envy looks at what the other has now. The answer looks to "a future".',
  'Psalm 37 opens with the same pair, envy and heat: *"Fret not yourself because of evildoers; be not envious of wrongdoers! For they will soon fade like the grass"* (Psalm 37:1–2). "Fret" is literally *heat yourself* (10.1). The answer comes in two parts. The first is what will happen to the envied: they fade. The second is a run of acts toward God: *"Trust in the Lord, and do good … Delight yourself in the Lord … Commit your way to the Lord … Be still before the Lord and wait patiently for him"* (37:3–7). Delight is among them. Envy wants what another has. The answer gives delight a new object. Proverbs repeats it: *"Fret not yourself because of evildoers, and be not envious of the wicked, for the evil man has no future"* (Proverbs 24:19–20). Two verses before, it says, *"Do not rejoice when your enemy falls, and let not your heart be glad when he stumbles"* (24:17). Envy of the wicked who prosper and gladness at an enemy\'s fall stand side by side. Job disowns the second in his oath (10.10).'),
 ('after_line', 'The middle word of James\'s three, "unspiritual", is literally "soulish".',
  '''**Jealousy as not yet grown.** *"But I, brothers, could not address you as spiritual people, but as people of the flesh, as infants in Christ. I fed you with milk … for while there is jealousy and strife among you, are you not of the flesh and behaving only in a human way? For when one says, 'I follow Paul,' and another, 'I follow Apollos,' are you not being merely human?"* (1 Corinthians 3:1–4). The figure is infancy, and jealousy is named as the sign of not having grown. It shows itself in attachment to a favourite teacher. Peter uses infancy the other way: *"Like newborn infants, long for the pure spiritual milk, that by it you may grow up"* (1 Peter 2:2; *Aimed at God*). One infancy longs for milk in order to grow. The other stays on milk and quarrels.

Paul also pictures it as belonging to the night: *"the hour has come for you to wake from sleep … The night is far gone; the day is at hand … Let us walk properly as in the daytime … not in quarreling and jealousy. But put on the Lord Jesus Christ, and make no provision for the flesh, to gratify its desires"* (Romans 13:11–14). The answer is a garment to put on, not a stronger effort, and with it goes a refusal to make "provision" for the flesh's desires.'''),
 ('after_line', 'Desire can be evil in itself.',
  'The proverbs judge a desire by where it ends: *"The desire of the righteous ends only in good, the expectation of the wicked in wrath"* (Proverbs 11:23). The psalm sets the end beside a sight. The righteous man *"has distributed freely; he has given to the poor … his horn is exalted in honor. The wicked man sees it and is angry; he gnashes his teeth and melts away; the desire of the wicked will perish!"* (Psalm 112:9–10). No word for envy is used there. The verse names the sight, the anger and the end of the desire.'),
 ('append_line', 'What is desired can be taken away. God tells Ezekiel',
  ' Lamentations mourns it after the fact, and names who took it: *"He has bent his bow like an enemy … and he has killed all who were delightful in our eyes"*; *"The Lord has become like an enemy"* (Lamentations 2:4–5).'),
],
'10-07-': [
 ('after_line', "- **Other people's eyes, set against his choosing.**",
  '- **One\'s own "better", set against his word.** *"But Naaman was angry and went away, saying, \'Behold, I thought that he would surely come out to me …\' Are not Abana and Pharpar, the rivers of Damascus, better than all the waters of Israel?"* (2 Kings 5:11–12). His own measure ("better") and his own picture of how it should go ("I thought") stood against the prophet\'s word. His servants answered with a question: *"My father, it is a great word the prophet has spoken to you; will you not do it? Has he actually said to you, \'Wash, and be clean\'?"* (5:13). He went down, and *"his flesh was restored like the flesh of a little child"* (5:14). A measure of "better" nearly cost him the cure, and a question let him lay it down.'),
 ('after_line', '- a warning: Abner told Asahel twice',
  '- a feast: the older brother *"was angry and refused to go in. His father came out and entreated him"* (Luke 15:28). His anger took the form of a will that would not go in, and the father did not wait inside for it to change (10.13).'),
 ('after_line', '**The will made absolute.**',
  'Daniel sees it again in a later king: *"And the king shall do as he wills. He shall exalt himself and magnify himself above every god … He shall prosper till the indignation is accomplished; for what is decreed shall be done"* (Daniel 11:36). The absolute will runs, and runs only until a time already set.'),
],
'10-10-': [
 ('append_line', "- **The anger of the powerful decides others' fate.**",
  ' Its favour has a ground too: *"A servant who deals wisely has the king\'s favor, but his wrath falls on one who acts shamefully"* (Proverbs 14:35); *"his favor is like dew on the grass"* (19:12).'),
 ('before_line', 'Love between two people has its own time in the Song',
  'People hold wishes about one another, and Paul fears what disappointment would bring: *"For I fear that perhaps when I come I may find you not as I wish, and that you may find me not as you wish—that perhaps there may be quarreling, jealousy, anger, hostility, slander, gossip, conceit, and disorder"* (2 Corinthians 12:20). Each side has a wish about the other. I read expectation between people as the ground on which quarrel and jealousy grow, named by the one who fears it.\n'),
],
'10-05-': [
 ('after_line', 'A silence can also be held too long.',
  'Job gives the weight inside as the reason for his words: *"Oh that my vexation were weighed, and all my calamity laid in the balances! For then it would be heavier than the sand of the sea; therefore my words have been rash"* (Job 6:2–3). The psalmist\'s heat came out as a prayer. Job owns that his came out rash, and asks that the weight be weighed with it.'),
],
'10-01-': [
 ('replace', 'Grief makes it tender; jealousy makes it hard: "jealousy makes a man furious … He will accept no compensation" (Proverbs 6:34–35).',
  'Joined with grief, it is Jesus "grieved at their hardness of heart" (Mark 3:5). Joined with jealousy, it refuses every gift: "jealousy makes a man furious … He will accept no compensation" (Proverbs 6:34–35). I read grief as making it tender and jealousy as making it hard.'),
],
'11-': [
 ('after_line', '- **Spirit is shared and passed on.**',
  '- **Zeal passes on.** *"I know your readiness, of which I boast about you to the people of Macedonia … And your zeal has stirred up most of them"* (2 Corinthians 9:2). The stirring verb is the one used of fathers who provoke their children (Colossians 3:21). Here it is aimed at good.'),
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
