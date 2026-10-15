"""M09 humility weave (#2148): the angles of 10.14 Humility woven into their chapters, plus the four
rule-77 corrections from the cross-check (s5 items 1-4; item 5 needs no change).

Researcher, 2026-10-15, verbatim: "excellent work.  bring the narrative up to date, and ensure that the
claims register / narrative is updated". Placement decision: 10.14 holds the full account; each angle
is woven into its own chapter in context (m09-humility-narrative-placement-proposal-v1-20261015.md).

Every edit is an exact replacement on the current version and must match once; the script refuses
otherwise and writes nothing. Writes each next version beside the current one (archiving the old
version is a separate step). 10.14 v1 is written separately (10-14-humility-v1-20261015.md).
Usage (repo root): python "_analytics/Clusters/M09 - humility-lowliness/m09-humility-weave-v1-20261015.py"
"""
import pathlib, sys

D = pathlib.Path('_analytics/essay/spirit_soul_body/inner-being-narrative')
DATE = '20261015'
PLAN = {}   # (src file, out file) -> [(old, new)]

def ch(src, ver_to):
    stem = src.rsplit('-v', 1)[0]
    key = (src, f'{stem}-v{ver_to}-{DATE}.md')
    PLAN[key] = []
    return lambda old, new: PLAN[key].append((old, new))

# ------------------------------------------------------------------ 10.0
e = ch('10-00-the-inner-being-at-work-v5-20261002.md', 6)
e('I take these activities one at a time in the sections that follow (10.1 to 10.11).',
  'I take these activities one at a time in the sections that follow (10.1 to 10.11). After them come three that run across all the activities: fear, anger and humility (10.12 to 10.14).')

# ------------------------------------------------------------------ 10.1 (pointers only)
e = ch('10-01-feeling-v21-20261013.md', 22)
e('And it trembles, but at God\'s word, not at a threat: "this is the one to whom I will look: he who is humble and contrite in spirit and trembles at my word" (Isaiah 66:2).',
  'And it trembles, but at God\'s word, not at a threat: "this is the one to whom I will look: he who is humble and contrite in spirit and trembles at my word" (Isaiah 66:2). The humble and contrite spirit is in 10.14.')
e('in the psalm that says "Delight yourself in the Lord" (37:4; 10.6).',
  'in the psalm that says "Delight yourself in the Lord" (37:4; 10.6). The meek are in 10.14.')

# ------------------------------------------------------------------ 10.2
e = ch('10-02-knowing-and-hearing-v17-20261012.md', 18)
e('## Perplexity', '''## Humility and hearing

Twice Proverbs says "humility comes before honor", and both times the verse beside it is about the ear. "The ear that listens to life-giving reproof will dwell among the wise. Whoever ignores instruction despises himself, but he who listens to reproof gains intelligence" (Proverbs 15:31–32). "If one gives an answer before he hears, it is his folly and shame" (Proverbs 18:13). James puts them in one sentence: "let every person be quick to hear, slow to speak, slow to anger … receive with meekness the implanted word" (James 1:19–21). And God looks to the one who "trembles at my word" (Isaiah 66:2). I read humility here as the ear that can take a word against itself, and does not answer before it hears. The whole account is in 10.14.

## Perplexity''')

# ------------------------------------------------------------------ 10.7
e = ch('10-07-choosing-and-setting-direction-v28-20261013.md', 29)
e('## Fear and choosing', '''## Taking the lower place

Some choices are choices of place. Jesus told a parable "when he noticed how they chose the places of honor": "do not sit down in a place of honor … But when you are invited, go and sit in the lowest place, so that when your host comes he may say to you, 'Friend, move up higher'" (Luke 14:7–10). The proverb had the same counsel: "Do not put yourself forward in the king's presence … for it is better to be told, 'Come up here,' than to be put lower in the presence of a noble" (Proverbs 25:6–7). The lower place is chosen before anyone else must give it, and the honour, if it comes, is given.

Company is chosen too: "It is better to be of a lowly spirit with the poor than to divide the spoil with the proud" (Proverbs 16:19). And a whole way: "to walk humbly with your God" (Micah 6:8). Humility is in 10.14.

## Fear and choosing''')

# ------------------------------------------------------------------ 10.8 (correction 2)
e = ch('10-08-right-and-wrong-v7-20261009.md', 8)
e('Wrong done to the weak draws God\'s anger as surely as idols do (Exodus 22:23–24; Micah 6:8; Chapter 13).',
  'Wrong done to the weak draws God\'s anger as surely as idols do (Exodus 22:23–24; 10.13). What the Lord requires is said in one line: "to do justice, and to love kindness, and to walk humbly with your God" (Micah 6:8; 10.14).')

# ------------------------------------------------------------------ 10.9
e = ch('10-09-relating-to-god-v23-20261013.md', 24)
e('## When God hides his face', '''## Humbling oneself before God

One way a person comes before God is by lowering himself. It is done before him, or before his word. Josiah humbled himself "when you heard how I spoke against this place" (2 Kings 22:19). Zedekiah's failure was that "He did not humble himself before Jeremiah the prophet, who spoke from the mouth of the Lord" (2 Chronicles 36:12). Its words own that God is right and ask for mercy: "The Lord is righteous" (2 Chronicles 12:6); "God, be merciful to me, a sinner!" (Luke 18:13).

God is said to see it. "When the Lord saw that they humbled themselves" (2 Chronicles 12:7). "Have you seen how Ahab has humbled himself before me?" (1 Kings 21:29). The one who humbles himself puts down what he carries: "Humble yourselves, therefore, under the mighty hand of God so that at the proper time he may exalt you, casting all your anxieties on him, because he cares for you" (1 Peter 5:6–7). James joins it to submitting and drawing near: "Submit yourselves therefore to God … Draw near to God, and he will draw near to you" (James 4:7–8). The whole account is in 10.14.

## When God hides his face''')

# ------------------------------------------------------------------ 10.10
e = ch('10-10-relating-to-others-v26-20261014.md', 27)
e('## Holding authority over another', '''## Humility toward one another

Between people, humility is a way of counting the other: "in humility count others more significant than yourselves. Let each of you look not only to his own interests, but also to the interests of others" (Philippians 2:3–4). It is set against "selfish ambition or conceit" (2:3), and against being "haughty" or "wise in your own sight" (Romans 12:16). It is worn toward others: "Clothe yourselves, all of you, with humility toward one another" (1 Peter 5:5). And it is named beside "bearing with one another in love" (Ephesians 4:2).

It shows in how a wrong is met: "restore him in a spirit of gentleness. Keep watch on yourself, lest you too be tempted" (Galatians 6:1); "correcting his opponents with gentleness" (2 Timothy 2:25). The reason given is one's own past: "For we ourselves were once foolish" (Titus 3:3).

It is also a submission that runs both ways: "submitting to one another out of reverence for Christ" (Ephesians 5:21), and the elders "not domineering over those in your charge" (1 Peter 5:3). The ground for all of it is "this mind among yourselves, which is yours in Christ Jesus" (Philippians 2:5). The whole account is in 10.14.

## Holding authority over another''')

# ------------------------------------------------------------------ 10.12 (pointer)
e = ch('10-12-fear-v10-20261014.md', 11)
e('It trembles, but at God\'s word: "this is the one to whom I will look: he who is humble and contrite in spirit and trembles at my word" (Isaiah 66:2).',
  'It trembles, but at God\'s word: "this is the one to whom I will look: he who is humble and contrite in spirit and trembles at my word" (Isaiah 66:2). The humble and contrite spirit is in 10.14.')

# ------------------------------------------------------------------ 10.13 (correction 2 + pointer)
e = ch('10-13-anger-v9-20261013.md', 10)
e(' "He has told you, O man, what is good; and what does the Lord require of you but to do justice, and to love kindness, and to walk humbly with your God?" (Micah 6:8).', '')
e('- **Humbling oneself:** "when he humbled himself the wrath of the Lord turned from him" (2 Chronicles 12:12).',
  '- **Humbling oneself:** "when he humbled himself the wrath of the Lord turned from him" (2 Chronicles 12:12; 10.14).')

# ------------------------------------------------------------------ Ch 4
e = ch('04-the-heart-v17-20261013.md', 18)
e('## Is the heart the centre of it all?', '''## The heart humbled

The heart is where a person humbles himself. "Because your heart was penitent, and you humbled yourself before the Lord" (2 Kings 22:19); in the parallel account, "your heart was tender" (2 Chronicles 34:27). "If then their uncircumcised heart is humbled" (Leviticus 26:41). Hezekiah "humbled himself for the pride of his heart" (2 Chronicles 32:26), the same heart that was proud a verse before (32:25). Daniel "set your heart to understand and humbled yourself before your God" (Daniel 10:12). Belshazzar's charge is the refusal: "you … have not humbled your heart, though you knew all this" (Daniel 5:22).

God humbles too, and what he reaches is the heart: "testing you to know what was in your heart" (Deuteronomy 8:2); "he bowed their hearts down with hard labor" (Psalm 107:12). The opposite is named: "Before destruction a man's heart is haughty" (Proverbs 18:12).

The heart can be broken. "Reproaches have broken my heart, so that I am in despair" (Psalm 69:20). "I am poor and needy, and my heart is stricken within me" (Psalm 109:22). "I groan because of the tumult of my heart" (Psalm 38:8). The prophet: "My heart is broken within me … because of the Lord and because of his holy words" (Jeremiah 23:9). And "He heals the brokenhearted and binds up their wounds" (Psalm 147:3).

Jesus speaks of his own: "I am gentle and lowly in heart" (Matthew 11:29). Humility is in 10.14.

## Is the heart the centre of it all?''')

# ------------------------------------------------------------------ Ch 5
e = ch('05-the-soul-v8-20261014.md', 9)
e('## The soul answers for itself', '''## Rest for the soul

"learn from me, for I am gentle and lowly in heart, and you will find rest for your souls" (Matthew 11:29). The rest is promised to the soul, and it is found by learning from one who is lowly in heart. The word received with meekness "is able to save your souls" (James 1:21). Leaders are to be obeyed because "they are keeping watch over your souls" (Hebrews 13:17). And the soul boasts in the Lord, not in itself: "My soul makes its boast in the Lord; let the humble hear and be glad" (Psalm 34:2). Humility is in 10.14.

## The soul answers for itself''')

# ------------------------------------------------------------------ Ch 6
e = ch('06-the-spirit-v12-20261009.md', 13)
e('A broken spirit can keep a person from even hearing good news.',
  'A broken spirit can keep a person from even hearing good news. Job: "My spirit is broken; my days are extinct; the graveyard is ready for me" (Job 17:1).')
e('"Pride goes before destruction, and a haughty spirit before a fall" (Proverbs 16:18). "Blessed are the poor in spirit"',
  '"Pride goes before destruction, and a haughty spirit before a fall" (Proverbs 16:18). The next verse chooses the company: "It is better to be of a lowly spirit with the poor than to divide the spoil with the proud" (16:19). "One\'s pride will bring him low, but he who is lowly in spirit will obtain honor" (Proverbs 29:23). "Blessed are the poor in spirit"')
e('**In anger it is held back, heated, pressed and embittered.**', '''**It is gentle, and it is under the person.** "restore him in a spirit of gentleness" (Galatians 6:1). "Shall I come to you with a rod, or with love in a spirit of gentleness?" (1 Corinthians 4:21). "a gentle and quiet spirit, which in God's sight is very precious" (1 Peter 3:4). "the spirits of prophets are subject to prophets. For God is not a God of confusion but of peace" (1 Corinthians 14:32–33): the one who speaks governs what moves in him. And every spirit has one Father: "Shall we not much more be subject to the Father of spirits and live?" (Hebrews 12:9). Humility is in 10.14.

**In anger it is held back, heated, pressed and embittered.**''')

# ------------------------------------------------------------------ Ch 11 (correction 3 + face)
e = ch('11-other-sides-of-the-inner-being-v33-20261013.md', 34)
e('Jesus offers rest that passes from his heart to ours: "learn from me, for I am gentle and lowly in heart, and you will find rest for your souls" (Matthew 11:29).',
  'Jesus offers rest, found by learning from him: "learn from me, for I am gentle and lowly in heart, and you will find rest for your souls" (Matthew 11:29).')
e('- **The story around it.**', '''- **Who lowers whom, and before whom.** A king humbling himself before God is answered (2 Chronicles 12:7). A people humbled by God may turn or harden (2 Chronicles 33:12; 28:22). A nation humbled by an enemy is only "subdued" (Judges 3:30). The noun for humility toward one another also names a self-made severity that puffs a person up (Colossians 2:18, 23), and submission is right before God and wrong to those who would enslave the gospel (Galatians 2:5) (10.14).
- **The story around it.**''')

# ------------------------------------------------------------------ Ch 12 (correction 1 + counterpart)
e = ch('12-when-the-inner-being-goes-wrong-v22-20261014.md', 23)
e('The human spirit is judged here beside the heart. Pride and humility are where the spirit is weighed most: haughty or lowly, proud or poor in spirit.',
  '''The human spirit is judged here beside the heart. Pride and humility are where the spirit is weighed: haughty or lowly, proud or poor in spirit.

The counterpart is humbling oneself (10.14). Hezekiah "humbled himself for the pride of his heart" (2 Chronicles 32:26), the verse after "his heart was proud" (32:25). Belshazzar knew what had come of his father's lifted-up heart, and was told, "you … have not humbled your heart, though you knew all this" (Daniel 5:22). The day against pride is named for its end: "The haughty looks of man shall be brought low, and the lofty pride of men shall be humbled, and the Lord alone will be exalted in that day" (Isaiah 2:11).''')

# ------------------------------------------------------------------ 13.1
e = ch('13-01-divine-v25-20261013.md', 26)
e('and what the verses on willing say of his will.',
  'and what the verses on willing say of his will. It now also holds what the verses on humbling say of his own lowering.')
e('''**The soul's answer.** "Bless the Lord, all his works, in all places of his dominion. Bless the Lord, O my soul!" (Psalm 103:22; Chapter 5).''',
  '''**The soul's answer.** "Bless the Lord, all his works, in all places of his dominion. Bless the Lord, O my soul!" (Psalm 103:22; Chapter 5).

## Lowering himself

The Lord is high, and the verses keep saying that he looks low.
- "Who is like the Lord our God, who is seated on high, who looks far down on the heavens and the earth? He raises the poor from the dust" (Psalm 113:5–7). The verb for looking far down is the one used when he brings the proud low.
- "For though the Lord is high, he regards the lowly, but the haughty he knows from afar" (Psalm 138:6).
- "I dwell in the high and holy place, and also with him who is of a contrite and lowly spirit, to revive the spirit of the lowly, and to revive the heart of the contrite" (Isaiah 57:15).
- David: "You have given me the shield of your salvation, and your gentleness made me great" (2 Samuel 22:36; Psalm 18:35). The word rendered "gentleness" is the word for humility.
- Over his people's unfaithfulness: "how I have been broken over their whoring heart that has departed from me" (Ezekiel 6:9).

**In the Son.** "who, though he was in the form of God, did not count equality with God a thing to be grasped, but emptied himself, by taking the form of a servant, being born in the likeness of men. And being found in human form, he humbled himself by becoming obedient to the point of death, even death on a cross. Therefore God has highly exalted him" (Philippians 2:6–9). He says of himself, "I am gentle and lowly in heart" (Matthew 11:29). He came "humble, and mounted on a donkey" (Matthew 21:5). As a boy, "he went down with them and came to Nazareth and was submissive to them" (Luke 2:51). "In his humiliation justice was denied him" (Acts 8:33). He "for a little while was made lower than the angels … crowned with glory and honor because of the suffering of death" (Hebrews 2:9). These are the words of Psalm 8 about man, read of Jesus (Psalm 8:5). All things are put under him, and at the end "the Son himself will also be subjected to him who put all things in subjection under him, that God may be all in all" (1 Corinthians 15:28).

I read the lowering that the Old Testament tells of God, looking down, dwelling with the lowly, his gentleness, his being broken over a heart, as done in the Son in a human life.

**Toward the humble and the proud.** He sees the one who humbles himself and answers: "When the Lord saw that they humbled themselves" (2 Chronicles 12:7); "Have you seen how Ahab has humbled himself before me?" (1 Kings 21:29). He gives favour: "to the humble he gives favor" (Proverbs 3:34); "God opposes the proud but gives grace to the humble" (James 4:6). He humbles to test, "to do you good in the end" (Deuteronomy 8:16). He brings the proud low, "and the Lord alone will be exalted in that day" (Isaiah 2:11). He looks on a humble estate (Luke 1:48). What this means for the one who humbles himself is in 10.14.''')

# ------------------------------------------------------------------ Ch 14 (correction 4)
e = ch('14-made-new-v17-20261014.md', 18)
e("- The seven conditions for the Spirit's work (2 Chronicles 7:14). This belongs to the companion study of the Holy Spirit.\n", '')

# ------------------------------------------------------------------ run
fails = []
outs = {}
for (src, out), edits in PLAN.items():
    t = (D / src).read_text(encoding='utf-8')
    for old, new in edits:
        n = t.count(old)
        if n != 1:
            fails.append(f'{src}: {n} matches for {old[:70]!r}')
            continue
        t = t.replace(old, new)
    outs[out] = t
if fails:
    print('REFUSED, nothing written:'); print('\n'.join(fails)); sys.exit(1)
for out, t in outs.items():
    if (D / out).exists():
        print('REFUSED: exists', out); sys.exit(1)
for out, t in outs.items():
    (D / out).write_text(t, encoding='utf-8'); print('wrote', out)
