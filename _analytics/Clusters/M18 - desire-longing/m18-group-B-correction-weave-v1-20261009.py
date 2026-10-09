"""Correction of the M18 group B sets 1 and 2 weave (#1993, item F), 2026-10-09.

Researcher, teaching on 2Pe 2:13 (verbatim): "making something of this verse with pleasure as an entry point will lead to
distorted views"; then "re-read and correct your work". Each verse whose delight word only measures or qualifies another
act is moved to the home of that act; 10.1 *Delight* keeps a table of them (the word's part only). Re-read record:
m18-group-B-correction-reread-v1-20261009.md.

Same mechanics and quote check as m18-group-B1-narrative-weave-v1-20261009.py, plus delete_line (a whole line, by unique prefix).
Run with --dry to check only; without it, it writes only if the check passes.
"""
import glob, importlib.util, os, re, shutil, sqlite3, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
DATE = '20261009'


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]


MEASURE = '''### When delight is only the measure

In many verses a delight word does not name the act the verse is about. It measures or qualifies another act, and the verse is placed with that act. In these verses delight is only the measure:

| Verse | The act the verse is about | Where |
|---|---|---|
| "they delight to draw near to God" (Isaiah 58:2) | seeking God daily, as if righteous, beside oppression | 10.7 |
| "they take no pleasure in it" (Jeremiah 6:10) | ears that cannot listen; the word scorned | 10.2 |
| "We do not desire the knowledge of your ways" (Job 21:14) | telling God to depart, and reckoning prayer by profit | 10.9 |
| "He did not delight in blessing" (Psalm 109:17) | cursing, put on as a coat | 10.5 |
| "why does my lord the king delight in this thing?" (2 Samuel 24:3) | a king's decision made over counsel | 10.7 |
| "the man whom the king delights to honor" (Esther 6:9) | Haman exalting himself, and his fall | Chapter 12 |
| "the king has delight in you" (1 Samuel 18:22) | Saul's snare | 10.10 |
| "If one wished to contend with him" (Job 9:3) | contending with God | 10.9 |
| "I desire to justify you" (Job 33:32) | a friend speaking to set another right | 10.10 |
| "does not wish to take his brother's wife" (Deuteronomy 25:7) | refusing a duty, and the public shame | 10.10 |
| "Whoever favors Joab" (2 Samuel 20:11) | following, past a body | 10.10 |
| "he does whatever he pleases" (Ecclesiastes 8:3) | keeping one's place before a king | 10.10 |
| "we were willing to be left behind at Athens alone" (1 Thessalonians 3:1) | sending Timothy, out of fear for them | 10.10 |
| "you will delight yourself in the Almighty" (Job 22:26) | returning to the Almighty | 10.9 |
| "Will he take delight in the Almighty?" (Job 27:10) | calling on God only in distress | 10.9 |
| "the land was pleasant" (Genesis 49:15) | bowing the shoulder to forced labour | 10.7 |
| "bread eaten in secret is pleasant" (Proverbs 9:17) | Folly's call, and turning in | 10.7 |
| "they shall hear my words, for they are pleasant" (Psalm 141:6) | praying that the heart not lean to evil, and taking a rebuke | 10.7 |
| "those who rebuke the wicked will have delight" (Proverbs 24:25) | judging without partiality | 10.8 |
| "drink deeply with delight" (Isaiah 66:11) | being comforted, as by a mother | 10.9 |
| "shall play over the hole of the cobra" (Isaiah 11:8) | creation at peace | 13.4 |
| "If the Lord delights in us" (Numbers 14:8) | not fearing, on the ground of his delight | 10.9 |
| "By this I know that you delight in me" (Psalm 41:11) | betrayed by a friend, and knowing he is not abandoned | 10.10 |
| "for he delights in him!" (Psalm 22:8) | mockery | 10.5 |
| "I have no pleasure in you" (2 Samuel 15:26) | yielding a choice to God | 10.7 |

God's delight itself, which these verses lean on, read or throw, is in 13.1 (*Delight*).
'''

OPS = {
'10-01-': [('delete_line', a, None) for a in [
  '- **In place of gold.**', 'Job asks it of the godless:', '### When it looks right, and when it is missing',
  'Delight can look right.', '- **A word scorned.**', '- **Not wanting him, by reckoning.**', '- **No delight in blessing.**',
  '- **Questioned, and overruled.**', '- **Imagined for oneself.**', '- **Claimed falsely.**', '### Wishing',
  'The same Hebrew word is often rendered', '- **To contend with God.**', '- **To justify another.**',
  '- **Not wanting a duty.**', '- **Favour called for over a body.**', "- **A ruler's pleasure.**",
  '- **Willing, because it could not be borne.**', '- **A land, at a price.**', '- **What is stolen.**',
  '- **Food refused, a blow taken, words offered.**', '- **The reward of a rebuke.**', "### A child's delight",
  '- "that you may nurse', '- "The nursing child', "### God's delight in a person's hands",
  'What God delights in is in 13.1 (*Delight*). The verses also show']] + [
  ('before_line', '## When feeling changes character', MEASURE),
 ],
'10-02-': [
 ('after_line', 'Hearing can stop at a single word.',
  'Ears can be closed to a word that is still being spoken. "To whom shall I speak and give warning, that they may hear? Behold, their ears are uncircumcised, they cannot listen; behold, the word of the Lord is to them an object of scorn; they take no pleasure in it" (Jeremiah 6:10). The act is a hearing that does not happen. "Cannot listen" is followed by what they do with the word instead: they scorn it. Taking no pleasure in it is the measure of the scorn. I read the uncircumcised ears as hearing that lacks the mark of belonging to him. The one who must speak is left holding it: "Therefore I am full of the wrath of the Lord; I am weary of holding it in" (6:11).'),
],
'10-09-': [
 ('after_line', '- **God speaks to the heart.**',
  '- **Comforted as by a mother.** "As one whom his mother comforts, so I will comfort you; you shall be comforted in Jerusalem" (Isaiah 66:13). Before it the people are pictured as infants: "that you may nurse and be satisfied from her consoling breast; that you may drink deeply with delight from her glorious abundance" (66:11), "carried upon her hip, and bounced upon her knees" (66:12). The act is being comforted. The delight is the infant\'s, in being fed, and the one who comforts is God (13.1).'),
 ('after_line', '- **Inquired of, not the dead.**',
  '- **Told to depart.** Those who "spend their days in prosperity, and in peace they go down to Sheol" (Job 21:13) "say to God, \'Depart from us! We do not desire the knowledge of your ways. What is the Almighty, that we should serve him? And what profit do we get if we pray to him?\'" (21:14–15). The act is a sending away. It is argued as a sum: serving and praying are weighed for profit and found not worth it. Job answers, "The counsel of the wicked is far from me" (21:16).\n'
  '- **Returned to.** Eliphaz counsels Job: "Agree with God, and be at peace; thereby good will come to you. Receive instruction from his mouth, and lay up his words in your heart. If you return to the Almighty you will be built up" (Job 22:21–23). Then "the Almighty will be your gold and your precious silver" (22:25), and "you will delight yourself in the Almighty and lift up your face to God. You will make your prayer to him, and he will hear you" (22:26–27). The act is returning. Delight comes after it, and prayer after the delight. It is a friend\'s counsel, given as a condition.'),
 ('before_line', '## Fear before God, and the fear of God',
  'Job wants to bring his case to God, and in the same breath judges it hopeless. "Truly I know that it is so: But how can a man be in the right before God? If one wished to contend with him, one could not answer him once in a thousand times" (Job 9:2–3). Four chapters on he turns from his friends to God: "But I would speak to the Almighty, and I desire to argue my case with God. As for you, you whitewash with lies" (13:3–4). And "Though he slay me, I will hope in him; yet I will argue my ways to his face" (13:15). The act is contending with God. What is wished is to argue the case, and what holds the wish is hope.\n'),
 ('before_line', '## When God hides his face',
  'Joshua and Caleb tell the people not to fear, and give the ground: "If the Lord delights in us, he will bring us into this land and give it to us, a land that flows with milk and honey. Only do not rebel against the Lord. And do not fear the people of the land, for they are bread for us. Their protection is removed from them, and the Lord is with us; do not fear them" (Numbers 14:8–9). Their courage rests on what the Lord delights in and on his being with them, not on their own size. "Then all the congregation said to stone them with stones" (14:10).\n'),
 ('before_line', '## Calling on God to wake',
  'A cry can come only in distress. Of the godless: "Will God hear his cry when distress comes upon him? Will he take delight in the Almighty? Will he call upon God at all times?" (Job 27:9–10). The act asked about is calling on God. I read the questions as setting a cry in distress against calling at all times. Delight in him is named as what would make the difference.\n'),
],
'10-07-': [
 ('before_line', '## Whose measure',
  'What is seen as pleasant can draw a person under a yoke. "Issachar is a strong donkey, crouching between the sheepfolds. He saw that a resting place was good, and that the land was pleasant, so he bowed his shoulder to bear, and became a servant at forced labor" (Genesis 49:14–15). The act is bowing the shoulder. What draws it is the rest and the land, seen as good and pleasant. I read a strong animal choosing to lie down, and the rest costing it its freedom.\n\n'
  'Folly draws by what is hidden. "The woman Folly is loud; she is seductive and knows nothing", and she calls, "Whoever is simple, let him turn in here!" and "Stolen water is sweet, and bread eaten in secret is pleasant." "But he does not know that the dead are there, that her guests are in the depths of Sheol" (Proverbs 9:13, 16–18). The act is her call and the turning in. The sweetness is what she claims for stolen water. The one who turns in knows the claim and not the end.\n'),
 ('before_line', '## Being chosen',
  'A choice can be left wholly to God. David, fleeing Absalom, sends the ark back: "If I find favor in the eyes of the Lord, he will bring me back and let me see both it and his dwelling place. But if he says, \'I have no pleasure in you,\' behold, here I am, let him do to me what seems good to him" (2 Samuel 15:25–26). The act is yielding. He does not presume God\'s pleasure, and he does not keep the ark to secure it (13.1).\n'),
 ('after_line', '**An inner act weighed by what God chooses.**',
  'The same passage opens on what they appear to be doing: "Yet they seek me daily and delight to know my ways, as if they were a nation that did righteousness and did not forsake the judgment of their God; they ask of me righteous judgments; they delight to draw near to God" (Isaiah 58:2). The act is seeking and drawing near. Their delight measures how eager it is, and "as if" says what it lacks. I read that eagerness to draw near can sit beside oppressing workers (58:3) without the person seeing the two together.'),
 ('before_line', '## Holding a choice',
  'The heart\'s leaning is prayed against, and a rebuke is welcomed. "Do not let my heart incline to any evil, to busy myself with wicked deeds in company with men who work iniquity, and let me not eat of their delicacies! Let a righteous man strike me—it is a kindness; let him rebuke me—it is oil for my head; let my head not refuse it" (Psalm 141:4–5). The act is a prayer that the heart not lean, and a choice of the hard word over the sweet food. What he calls pleasant is his own words, to be heard when the judges fall: "then they shall hear my words, for they are pleasant" (141:6). The prayer ends, "But my eyes are toward you, O God, my Lord" (141:8).\n'),
 ('before_line', '## What changes the character',
  'A king\'s choice can be questioned and still stand. Joab: "May the Lord your God add to the people a hundred times as many as they are … but why does my lord the king delight in this thing?" (2 Samuel 24:3). "But the king\'s word prevailed against Joab and the commanders of the army" (24:4). Afterwards "David\'s heart struck him after he had numbered the people" (24:10; Chapter 8). The act is a decision made over counsel. Joab names the king\'s delight as what he cannot understand, and the king\'s own heart judges it after.\n'),
],
'10-05-': [
 ('before_line', '## The tongue, the lips and the eyes devise',
  'Cursing can become what a person wears. "For he did not remember to show kindness, but pursued the poor and needy and the brokenhearted, to put them to death. He loved to curse; let curses come upon him! He did not delight in blessing; may it be far from him! He clothed himself with cursing as his coat; may it soak into his body like water, like oil into his bones!" (Psalm 109:16–18). The act is cursing. Loving it, and taking no delight in blessing, measure how wholly he gave himself to it. I read the figure as speech that goes back into the speaker: put on as a coat, then soaked into the bones.\n'),
 ('before_line', '## Anger in words',
  'Mockery can begin without words. "All who see me mock me; they make mouths at me; they wag their heads" (Psalm 22:7), and then the words: "He trusts in the Lord; let him deliver him; let him rescue him, for he delights in him!" (22:8). The mouth and the head move first. The words that follow turn his trust and God\'s delight into a taunt. He answers God, not them: "Yet you are he who took me from the womb" (22:9; 13.1).\n'),
],
'12-': [
 ('before_line', '## Hardening and stubbornness',
  'Pride can design its own honour. The king asks, "What should be done to the man whom the king delights to honor?" And Haman "said to himself, \'Whom would the king delight to honor more than me?\'" (Esther 6:6). He spells it out: "let royal robes be brought, which the king has worn, and the horse that the king has ridden, and on whose head a royal crown is set" (6:8). The king answers, "Hurry; take the robes and the horse, as you have said, and do so to Mordecai the Jew" (6:10). Haman leads Mordecai through the square, then "hurried to his house, mourning and with his head covered" (6:12). His wife and wise men tell him, "you will not overcome him but will surely fall before him" (6:13). The act is self-exaltation. The king\'s delight is only what Haman misreads (10.1, *Delight*). I read that the honour he designed for himself became the measure of his fall.\n'),
],
'10-10-': [
 ('before_line', '## Loyalty and honour',
  'A plot can be dressed as delight. Saul thought, "Let me give her to him, that she may be a snare for him" (1 Samuel 18:21), and told his servants to say to David in private, "Behold, the king has delight in you, and all his servants love you" (18:22). The act is the snare. The delight is the bait, and it is spoken in private.\n'),
 ('before_line', '## Friends, company and care',
  'A duty can be refused, and the law makes the refusal public. "And if the man does not wish to take his brother\'s wife, then his brother\'s wife shall go up to the gate to the elders" (Deuteronomy 25:7). "If he persists, saying, \'I do not wish to take her,\' then his brother\'s wife shall go up to him in the presence of the elders and pull his sandal off his foot and spit in his face" (25:8–9), and "the name of his house shall be called in Israel, \'The house of him who had his sandal pulled off\'" (25:10). The act is refusing to build up a dead brother\'s house. The law does not force the wanting; it names the refusal.\n\n'
  'Loyalty can be called for over a body. Joab killed Amasa as he greeted him: "Is it well with you, my brother?" (2 Samuel 20:9). Then one of his men "took his stand by Amasa and said, \'Whoever favors Joab, and whoever is for David, let him follow Joab\'" (20:11). "And anyone who came by, seeing him, stopped" (20:12). Once the body was covered, "all the people went on after Joab" (20:13). The act is following. I read that the sight held them, and the covering let them go on.\n'),
 ('before_line', "### Speaking to another's fear",
  'A king\'s power calls for care. "I say: Keep the king\'s command, because of God\'s oath to him. Be not hasty to go from his presence. Do not take your stand in an evil cause, for he does whatever he pleases. For the word of the king is supreme, and who may say to him, \'What are you doing?\'" (Ecclesiastes 8:2–4). The act is keeping one\'s place before power, and the king\'s pleasure is the reason given. Then: "the wise heart will know the proper time and the just way" (8:5). The same words, "he does all that he pleases", are said of God (Psalm 115:3; 13.1).\n'),
 ('before_line', '**Connections:** with feeling (10.1), since strife',
  'Care can make a person willing to be alone. "Therefore when we could bear it no longer, we were willing to be left behind at Athens alone, and we sent Timothy" (1 Thessalonians 3:1–2), "for fear that somehow the tempter had tempted you and our labor would be in vain" (3:5). The act is sending Timothy. Being left alone is what it cost Paul, and fear for them is what drove it (10.6, 3:6–7).\n\n'
  'A friend can speak to set another right. Elihu: "Pay attention, O Job, listen to me; be silent, and I will speak. If you have any words, answer me; speak, for I desire to justify you" (Job 33:31–32), "to bring back his soul from the pit" (33:30). The act is speaking to him and inviting his answer. What he desires is Job\'s being found right.\n\n'
  'Betrayal can be met by knowing God\'s favour. "Even my close friend in whom I trusted, who ate my bread, has lifted his heel against me" (Psalm 41:9). "By this I know that you delight in me: my enemy will not shout in triumph over me" (41:11). The act is being betrayed by a friend, and knowing, from what did not happen, that he is not abandoned (13.1).\n'),
],
'10-08-': [
 ('before_line', 'Wrong done to the weak draws God',
  'Judging rightly carries a reward. "Partiality in judging is not good. Whoever says to the wicked, \'You are in the right,\' will be cursed by peoples, abhorred by nations, but those who rebuke the wicked will have delight, and a good blessing will come upon them" (Proverbs 24:23–25). The act is judging without partiality. Delight is what comes to the one who rebukes. The curse is what comes to the one who calls the wicked right (Chapter 11).\n'),
],
'13-04-': [
 ('before_line', '*Verses are gathered here',
  '**Harm ended.** "The wolf shall dwell with the lamb, and the leopard shall lie down with the young goat" (Isaiah 11:6). "The nursing child shall play over the hole of the cobra, and the weaned child shall put his hand on the adder\'s den. They shall not hurt or destroy in all my holy mountain; for the earth shall be full of the knowledge of the Lord as the waters cover the sea" (11:8–9). The act is creation at peace. The child\'s play over the cobra\'s hole shows it: where there is no harm, a child plays without fear. The verse gives the ground, the earth full of the knowledge of the Lord.\n'),
],
'13-01-': [
 ('before_line', '## Willing',
  '**His word carries out what he purposes.** "For as the rain and the snow come down from heaven and do not return there but water the earth" (Isaiah 55:10), "so shall my word be that goes out from my mouth; it shall not return to me empty, but it shall accomplish that which I purpose, and shall succeed in the thing for which I sent it" (55:11). The act is the word going out and doing its work. "Purpose" is a delight word: what he delights in, his word carries out.\n'),
 ('replace', 'Three more verses say it.', 'Two more verses say it.'),
 ('replace', ' And of his word: "it shall not return to me empty, but it shall accomplish that which I purpose" (Isaiah 55:11), where "purpose" is the delight word.', ' His word carries out what he purposes (*Purposing*).'),
 ('replace', 'What the person does with it is in 10.1 (*Delight*).', 'What each person does with it is placed with the act: not fearing (10.9), yielding (10.7), mockery (10.5) and betrayal (10.10).'),
],
}


NL = chr(10)


def apply(text, mode, anchor, ins):
    lines = text.split('\n')
    if mode == 'delete_line':
        idx = [i for i, l in enumerate(lines) if l.startswith(anchor)]
        assert len(idx) == 1, ('delete', anchor[:60], idx)
        del lines[idx[0]]
        return NL.join(lines)
    if mode == 'replace':
        assert text.count(anchor) == 1, ('replace count', anchor[:60], text.count(anchor))
        return text.replace(anchor, ins)
    idx = [i for i, l in enumerate(lines) if anchor in l]
    assert len(idx) == 1, (mode, anchor[:60], idx)
    i = idx[0]
    if mode == 'after_line':
        if lines[i].startswith('- ') and ins.startswith('- '):
            lines[i + 1:i + 1] = [ins]
        else:
            lines[i + 1:i + 1] = ['', ins]
    elif mode == 'before_line':
        lines[i:i] = [ins.rstrip('\n'), '']
    return '\n'.join(lines)


# ---------------------------------------------------------------- quote check (inserted text only)
c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)


def norm(s):
    s = unicodedata.normalize('NFKC', s).lower()
    s = re.sub(r'\[[^\]]*\]', ' ', s)
    s = s.replace('’', "'").replace('‘', "'")
    s = re.sub(r"[^a-z0-9' ]", ' ', s)
    s = s.replace("'", '')
    return re.sub(r'\s+', ' ', s).strip()


def verse_text(book, ch, vs):
    out = []
    for v in vs:
        r = c.execute('SELECT text FROM verse WHERE reference = ? AND deleted = 0', (f'{book} {ch}:{v}',)).fetchone()
        if r: out.append(r[0])
    return ' '.join(out)


QUOTE = re.compile(r'"([^"]+)"')
fails, checked = [], 0
for prefix, ops in OPS.items():
    for mode, anchor, ins in ops:
        if mode == 'delete_line': continue
        if mode == 'replace': ins = ins.replace(anchor, '')
        last_book = None
        for line in ins.split('\n'):
            for m in QUOTE.finditer(line):
                frag = m.group(1)
                if len(frag.split()) < 3: continue
                tail = line[m.end():]
                cm = re.search(r'\(([^()]*\d+:\d+[^()]*)\)', tail)
                if not cm: continue
                cites = list(xr.cites(cm.group(1)))
                if not cites:
                    bare = re.match(r'\s*(\d+):(\d+)(?:[–-](\d+))?', cm.group(1))
                    if bare and last_book:
                        a, b = int(bare.group(2)), int(bare.group(3) or bare.group(2))
                        cites = [(last_book, int(bare.group(1)), v, '') for v in range(a, b + 1)]
                else:
                    last_book = cites[0][0]
                if not cites: fails.append(f'{prefix}: no citation parsed for "{frag[:50]}"'); continue
                book, ch = cites[0][0], cites[0][1]
                vs = sorted({v for b, cc, v, h in cites if b == book and cc == ch})
                text = norm(verse_text(book, ch, range(min(vs) - 1, max(vs) + 2)))
                for part in re.split(r'…|\.\.\.', frag):
                    p = norm(part)
                    if p and p not in text:
                        fails.append(f'{prefix}: "{part.strip()[:70]}" not in {book} {ch}:{vs}')
                checked += 1
print(f'quotes checked: {checked}; failures: {len(fails)}')
for f in fails: print('  FAIL', f)

dry = '--dry' in sys.argv
for prefix, ops in OPS.items():
    src = current(prefix)
    text = open(src, encoding='utf-8').read()
    for mode, anchor, ins in ops:
        text = apply(text, mode, anchor, ins)
    text = re.sub(NL + '{3,}', NL + NL, text)
    m = re.match(r'(.*-v)(\d+)-(\d{8})\.md$', os.path.basename(src))
    new = os.path.join(NARR, f'{m.group(1)}{int(m.group(2)) + 1}-{DATE}.md')
    print(os.path.basename(src), '->', os.path.basename(new))
    if dry or fails: continue
    shutil.copy2(src, os.path.join(NARR, 'archive', os.path.basename(src)))
    open(new, 'w', encoding='utf-8').write(text)
    os.remove(src)
if fails and not dry: sys.exit('not applied: fix failures first')
