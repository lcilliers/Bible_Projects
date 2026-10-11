"""Weave of the M18 group B remaining bucket-1 verses (#1993, item F), 2026-10-11.

Researcher (chat 2026-10-11, verbatim): "read the 15 now as recommended, then proceed with the weave".
Sources: m18-group-B-remaining-role-reading-v2-20261011.md (24 central verses, section 6 plan) and
m18-group-B-no-carrier-reading-v1-20261011.md (the 15 placed by their acts). Read by the guide
Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md (rule 73): each verse is placed by its
main operation; where the M18 word only measures another act, 10.1 *When delight is only the measure* gets a row.

Same mechanics and quote check as m18-group-B-correction-weave-v1-20261009.py.
Run with --dry to check only; without it, it writes only if the check passes.
"""
import glob, importlib.util, os, re, shutil, sqlite3, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v3-20261009.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
DATE = '20261011'
NL = '\n'


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]


MEASURE_LAST = '| "I have no pleasure in you" (2 Samuel 15:26) | yielding a choice to God | 10.7 |'
MEASURE_ADD = MEASURE_LAST + '''
| "if it seems good to you, I will give you its value in money" (1 Kings 21:2) | wanting another's vineyard, put as a fair offer | 10.6 |
| "Do whatever is good in your eyes" (2 Kings 10:5) | rulers giving up a choice, in fear | 10.7 |
| "Do whatever seems good to you" (1 Samuel 14:36) | a people leaving the choice to the king, the priest asking for God first | 10.7 |
| "to do with them as it seems good to you" (Esther 3:11) | a king handing a people to another's will | 10.7 |
| "you may write as you please" (Esther 8:8) | the same king handing it the other way | 10.7 |
| "If it seems good to you and from the Lord our God" (1 Chronicles 13:2) | an assembly asked to choose as one | 10.7 |
| "Let him do what seems good to him" (1 Samuel 3:18) | yielding to a judgment already spoken | 10.7 |
| "dwell where it pleases you" (Genesis 20:15) | a choice given back after a wrong | 10.7 |
| "do therefore what seems good to you" (2 Samuel 19:27) | leaving one's cause with the king | 10.10 |
| "to do his pleasure" (2 Samuel 19:18) | hurrying to serve the returning king | 10.10 |
| "do to them as you please" (Genesis 19:8) | Lot shielding his guests | 10.10 |
| "you may do to us whatever seems good to you" (1 Samuel 11:10) | words of surrender, with rescue known | 10.11 |'''

OPS = {
'10-01-': [
 ('after_line', '- **Beside not forgetting, and love.**',
  '- **Beside meditating.** "but his delight is in the law of the Lord, and on his law he meditates day and night" (Psalm 1:2). The "but" sets the delight against the counsel, the way and the seat of the wicked (1:1). What he delights in he turns over day and night (10.4). I read the psalm naming the man by what he delights in, more than by what he avoids.'),
 ('after_line', '- **Beside meditating.**',
  '- **Under pressure.** The delight is held where other things press on it. While "princes sit plotting against me" (Psalm 119:23): "Your testimonies are my delight; they are my counselors" (119:24). What he delights in also counsels him. In affliction: "If your law had not been my delight, I would have perished in my affliction" (119:92). He does not say the law kept him, but his delight in it, and goes on, "I will never forget your precepts, for by them you have given me life" (119:93; 10.3). In anguish: "Trouble and anguish have found me out, but your commandments are my delight" (119:143). The trouble is not taken away. The delight stands beside it.'),
 ('after_line', '- **Under pressure.**',
  '- **Joined to doing.** "I delight to do your will, O my God; your law is within my heart" (Psalm 40:8). The delight is in doing, and the law is inward. Two verses before, it is God who has "not delighted" in sacrifice (40:6; 13.1).'),
 ('after_line', "- **A king's delight decides a life.**",
  '- **In the godly, with God as the only good.** "I say to the Lord, \'You are my Lord; I have no good apart from you.\' As for the saints in the land, they are the excellent ones, in whom is all my delight" (Psalm 16:2–3). The next verse refuses the other company: "their drink offerings of blood I will not pour out or take their names on my lips" (16:4). I read his delight in the saints as going with God being his only good (10.10).'),
 ('replace', MEASURE_LAST, MEASURE_ADD),
],
'10-05-': [
 ('before_line', '## The tongue, the lips and the eyes devise',
  'A vow binds the person by the mouth before God. "Be not rash with your mouth, nor let your heart be hasty to utter a word before God, for God is in heaven and you are on earth. Therefore let your words be few" (Ecclesiastes 5:2). "When you vow a vow to God, do not delay paying it, for he has no pleasure in fools. Pay what you vow. It is better that you should not vow than that you should vow and not pay" (5:4–5). The passage ends, "God is the one you must fear" (5:7). I read the fool here as the one whose mouth runs ahead of his doing: the heart hasty, the word spoken, the paying left undone. What God has no pleasure in is in 13.1.'),
],
'10-06-': [
 ('after_line', 'The servant of Isaiah is the opposite case:',
  'The eye can also give. "Whoever has a bountiful eye will be blessed, for he shares his bread with the poor" (Proverbs 22:9). "Bountiful" is literally "good": a good eye. The same book warns against "the bread of a man who is stingy" (23:6, *Possessions*), literally one with an evil eye. I read the eye here as the way a person looks on another\'s need, and the look moves the hand that shares (10.10).'),
 ('after_line', 'He never solves the riddle he has just named.',
  'Near its end the book says it of life itself. "Light is sweet, and it is pleasant for the eyes to see the sun. So if a person lives many years, let him rejoice in them all; but let him remember that the days of darkness will be many" (Ecclesiastes 11:7–8). To see the sun is to be alive, and the pleasure is in that. It is not left alone: "Rejoice, O young man, in your youth … But know that for all these things God will bring you into judgment" (11:9). The rejoicing is held together with remembering the dark days and with the judgment.'),
 ('after_line', 'Paul names what is to be put to death:',
  'Concern can stop at death. The friends say that God stores up a man\'s iniquity for his children. Job answers: "Let him pay it out to them, that they may know it. Let their own eyes see their destruction … For what do they care for their houses after them, when the number of their months is cut off?" (Job 21:19–21). "Care" is the delight word: what pleasure has he in his house after him? A punishment kept for the children does not reach a man whose concern ends with his own months. I read Job making the reach of a person\'s concern decide what can reach him.'),
 ('after_line', 'The command itself names the desire',
  'Coveting can be put as a fair offer. Ahab to Naboth: "Give me your vineyard, that I may have it for a vegetable garden, because it is near my house, and I will give you a better vineyard for it; or, if it seems good to you, I will give you its value in money" (1 Kings 21:2). The want is dressed as an exchange. Naboth\'s refusal is not about the price: "The Lord forbid that I should give you the inheritance of my fathers" (21:3). The want, refused, goes into the body: Ahab "lay down on his bed and turned away his face and would eat no food" (21:4; 10.1). I read the courtesy of the offer as covering a want that could not bear a no.'),
 ('after_line', 'Unmet wanting turns into fighting.',
  'The same passions reach into prayer. "You do not have, because you do not ask. You ask and do not receive, because you ask wrongly, to spend it on your passions" (James 4:2–3). James names two failures, not asking and asking for the passions. The passions are behind the fighting (4:1) and behind the wrong asking. The prayer is bent toward the one who prays (10.9).'),
],
'10-07-': [
 ('after_line', 'A choice can be left wholly to God.',
  'Eli yields after the word has been spoken. He made Samuel tell him all of it, "Do not hide it from me" (1 Samuel 3:17), and when he had heard the judgment on his house, "he said, \'It is the Lord. Let him do what seems good to him\'" (3:18). David yields before he knows what God will do. Eli yields once he knows.'),
 ('after_line', 'Eli yields after the word has been spoken.',
  'A course can change when God\'s pleasure is seen. "When Balaam saw that it pleased the Lord to bless Israel, he did not go, as at other times, to look for omens, but set his face toward the wilderness" (Numbers 24:1). He had gone aside before, "as at other times". Now that he sees what pleases the Lord, he does not go, and he sets his face. The next verse: "And the Spirit of God came upon him" (24:2). The Lord\'s pleasure itself is in 13.1.'),
 ('after_line', '- **One\'s own "better", set against his word.**',
  '- **The king\'s eyes, or God\'s.** Saul proposed to pursue by night, "And they said, \'Do whatever seems good to you.\' But the priest said, \'Let us draw near to God here\'" (1 Samuel 14:36). God did not answer that day (14:37). When Saul swore that the guilty would die "though it be in Jonathan my son", "there was not a man among all the people who answered him", and then again, "Do what seems good to you" (14:39–40). The people give the king\'s eyes as the measure. The priest asks for God\'s first.'),
 ('after_line', '- **The king\'s eyes, or God\'s.**',
  '- **Another\'s will, given the whole decision.** Haman asks, "If it please the king, let it be decreed that they be destroyed" (Esther 3:9). The king gives him his ring and says, "The money is given to you, the people also, to do with them as it seems good to you" (3:11). Later the same king says to Esther and Mordecai, "you may write as you please with regard to the Jews … for an edict written in the name of the king and sealed with the king\'s ring cannot be revoked" (8:8). The measure is handed over twice, and the first handing cannot be undone.'),
 ('after_line', 'Weighing a case together is also called choosing:',
  'An assembly can be asked to choose with the Lord named in the asking. "If it seems good to you and from the Lord our God, let us send abroad to our brothers … Then let us bring again the ark of our God to us, for we did not seek it in the days of Saul" (1 Chronicles 13:2–3). "All the assembly agreed to do so, for the thing was right in the eyes of all the people" (13:4). Two measures are named in the asking, theirs and the Lord\'s. The verse that records the agreement names the people\'s eyes.'),
 ('after_line', 'The king hands the choice to the man who fed him',
  'A choice can be given back after a wrong. Warned by God in a dream, Abimelech returned Sarah, gave sheep, oxen and servants, and said, "Behold, my land is before you; dwell where it pleases you" (Genesis 20:15). To Sarah: "It is a sign of your innocence in the eyes of all who are with you, and before everyone you are vindicated" (20:16). The wrong is answered by giving the other the choice of where to live, and by clearing her before others.'),
 ('after_line', '- Uriah ',
  '- The rulers of Samaria, told by Jehu to set up a king and fight, "were exceedingly afraid and said, \'Behold, the two kings could not stand before him. How then can we stand?\'" (2 Kings 10:4). They gave up the choice: "We are your servants, and we will do all that you tell us. We will not make anyone king. Do whatever is good in your eyes" (10:5). The next letter used what they had handed over: "take the heads of your master\'s sons" (10:6).'),
],
'10-09-': [
 ('after_line', 'A cry can come only in distress.',
  'A plea can end in asking that one\'s work should last. The prayer of Moses that counts how short a life is (Psalm 90:10, 12) ends: "Return, O Lord! How long? Have pity on your servants!" (Psalm 90:13), "Make us glad for as many days as you have afflicted us" (90:15), "Let your work be shown to your servants" (90:16), and "Let the favor of the Lord our God be upon us, and establish the work of our hands upon us; yes, establish the work of our hands!" (90:17). "Favor" is the word for pleasantness. What they ask to last is their own work, and they ask it under his favor, beside "your work".'),
],
'10-10-': [
 ('before_line', '## Friends, company and care',
  '''A people's approval can read a king's heart. David mourned Abner, wept at the grave, and swore not to eat till sunset (2 Samuel 3:31–35). "And all the people took notice of it, and it pleased them, as everything that the king did pleased all the people. So all the people and all Israel understood that day that it had not been the king's will to put to death Abner the son of Ner" (2 Samuel 3:36–37). They watched what he did, were pleased, and understood what he had not willed (10.2).

When David came back over the Jordan, three men met him. Ziba and his men "crossed the ford to bring over the king's household and to do his pleasure" (2 Samuel 19:18). Shimei fell down before him: "Let not my lord hold me guilty or remember how your servant did wrong … For your servant knows that I have sinned" (19:19–20). Mephibosheth had not cared for his feet or beard or clothes since the king left (19:24). Slandered by Ziba, he did not argue his cause: "my lord the king is like the angel of God; do therefore what seems good to you … What further right have I, then, to cry to the king?" (19:27–28). When the land was divided, he said, "Oh, let him take it all, since my lord the king has come safely home" (19:30). I read his loyalty in what he gives up: the king's return is what he holds to, not the land.

Shelter given to guests can be held above one's own. Lot to the men of Sodom: "I beg you, my brothers, do not act so wickedly. Behold, I have two daughters who have not known any man. Let me bring them out to you, and do to them as you please. Only do nothing to these men, for they have come under the shelter of my roof" (Genesis 19:7–8). The verse gives his reason, the shelter of his roof. The men answer, "This fellow came to sojourn, and he has become the judge!" (19:9). The verses record the offer and the reason, and do not weigh them.'''),
],
'10-11-': [
 ('before_line', '### The hidden trap',
  'Words of surrender can hold back what is known. The men of Jabesh had been told, "Tomorrow, by the time the sun is hot, you shall have salvation", and "they were glad" (1 Samuel 11:9). Then they said to Nahash, "Tomorrow we will give ourselves up to you, and you may do to us whatever seems good to you" (11:10). The next morning Saul\'s army struck the Ammonites (11:11). I read their words as yielding in form, with the rescue they knew of held back.'),
],
'13-01-': [
 ('before_line', '**His word carries out what he purposes.**',
  '**His purpose is spoken, and carried out by another.** The delight word is also used for his purpose. He is the one "who says of Cyrus, \'He is my shepherd, and he shall fulfill all my purpose\'" (Isaiah 44:28), at the end of a line of sayings: "who confirms the word of his servant and fulfills the counsel of his messengers" (44:26). Again: "declaring the end from the beginning and from ancient times things not yet done, saying, \'My counsel shall stand, and I will accomplish all my purpose,\' calling a bird of prey from the east, the man of my counsel from a far country. I have spoken, and I will bring it to pass; I have purposed, and I will do it" (46:10–11). It is said to people told to "remember the former things of old; for I am God, and there is no other" (46:9). And: "Who among them has declared these things? The Lord loves him; he shall perform his purpose on Babylon" (48:14). I read "his purpose" there as the Lord\'s, carried out by the one he loves, as in 44:28; it can also be read as Cyrus\'s own pleasure. In each place the purpose is said aloud, set against idols that declare nothing, and done through a named man. What pleases him is what he will do.'),
 ('after_line', 'The verses do not say he has no use for offerings;',
  '**Not from those who put something else in the place of hearing.** Saul kept back the best of what was to be destroyed, "to sacrifice to the Lord your God in Gilgal" (1 Samuel 15:21). Samuel answered, "Has the Lord as great delight in burnt offerings and sacrifices, as in obeying the voice of the Lord? Behold, to obey is better than sacrifice, and to listen than the fat of rams" (15:22). To priests "who despise my name" (Malachi 1:6) and offer the blind and the lame: "Present that to your governor; will he accept you or show you favor?" (1:8). Then: "Oh that there were one among you who would shut the doors, that you might not kindle fire on my altar in vain! I have no pleasure in you, says the Lord of hosts, and I will not accept an offering from your hand" (1:10). He would rather the doors were shut. And of the vow made and not paid: "When you vow a vow to God, do not delay paying it, for he has no pleasure in fools. Pay what you vow" (Ecclesiastes 5:4; 10.5). I read the three together: in each, what he does not delight in is an offering or a word standing in the place of hearing, honour or doing.'),
 ('replace', 'Two more verses say it.', 'Three more verses say it.'),
 ('replace', 'beside idols that "have mouths, but do not speak" (115:5). ',
  'beside idols that "have mouths, but do not speak" (115:5). Psalm 135 says it of all creation: "Whatever the Lord pleases, he does, in heaven and on earth, in the seas and all deeps" (Psalm 135:6), after "our Lord is above all gods" (135:5). '),
 ('after_line', '- The sailors, before they throw Jonah',
  '- Balaam: "When Balaam saw that it pleased the Lord to bless Israel, he did not go, as at other times, to look for omens" (Numbers 24:1). What pleased the Lord was to bless, and seeing it turned a man from his omens (10.7).'),
 ('before_line', 'His delight stands beside his choosing',
  '**Delight at creation.** Wisdom speaks in the poem of Proverbs 8: "The Lord possessed me at the beginning of his work" (Proverbs 8:22), and "when he marked out the foundations of the earth, then I was beside him, like a master workman, and I was daily his delight, rejoicing before him always, rejoicing in his inhabited world and delighting in the children of man" (8:29–31). It is a figure, Wisdom speaking as a person. Delight runs from God to Wisdom, and from Wisdom to the world and to mankind, and the poem sets it at creation. I read the poem putting delight in people into the work of making the world.'),
],
'11-patterns': [
 ('replace', 'and met in those "who choose the things that please me" (56:4).',
  'and met in those "who choose the things that please me" (56:4). The noun *ḥēpheṣ* names his settled purpose: "he shall fulfill all my purpose" (Isaiah 44:28). It names what a man cares about, and that stops at his death: "what do they care for their houses after them" (Job 21:21).'),
 ('after_line', '- **Delight.** The Hebrew',
  '- **Good, said of the eye.** "Whoever has a bountiful eye will be blessed, for he shares his bread with the poor" (Proverbs 22:9). "Bountiful" is literally "good" (10.6).'),
 ('replace', '"in their sight" (Jeremiah 33:24), "rejected by men but in the sight of God chosen" (1 Peter 2:4).',
  '"in their sight" (Jeremiah 33:24), "rejected by men but in the sight of God chosen" (1 Peter 2:4). The words "what seems good to you" carry different acts: loyalty in Mephibosheth (2 Samuel 19:27), fear in the rulers before Jehu (2 Kings 10:5), a cover in the men of Jabesh (1 Samuel 11:10), a people handed over in a king\'s word (Esther 3:11), and yielding to God in Eli and David (1 Samuel 3:18; 2 Samuel 15:26). The words are the same; the setting decides (10.7, 10.10, 10.11).'),
],
}


def apply(text, mode, anchor, ins):
    lines = text.split(NL)
    if mode == 'replace':
        assert text.count(anchor) == 1, ('replace count', anchor[:60], text.count(anchor))
        return text.replace(anchor, ins)
    idx = [i for i, l in enumerate(lines) if l.startswith(anchor) or (not anchor.startswith('- ') and anchor in l and l.startswith(anchor[:20]))]
    assert len(idx) == 1, (mode, anchor[:60], idx)
    i = idx[0]
    if mode == 'after_line':
        if lines[i].startswith('- ') and ins.startswith('- '):
            lines[i + 1:i + 1] = [ins]
        else:
            lines[i + 1:i + 1] = ['', ins]
    elif mode == 'before_line':
        lines[i:i] = [ins.rstrip(NL), '']
    return NL.join(lines)


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
        if mode == 'replace': ins = ins.replace(anchor, '')
        last_book = None
        for line in ins.split(NL):
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
                text = norm(verse_text(book, ch, range(min(vs) - 2, max(vs) + 3)))
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
