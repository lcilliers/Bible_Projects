"""M08 pride weave (#2156): the angles of 10.15 Pride woven into their chapters in context.

Researcher, 2026-10-15, verbatim: "... then proceed with a consolidated cross batch synergy, updating the
claims register, weaving and cross checking that the narrative is anchored in the claims register for
this group of words". Placement: m08-pride-synergy-v1-20261015.md s3 (10.15 holds the full account, as
10.12-10.14 under #1961; each angle in its chapter in context, #1920).

Every edit is an exact replacement on the current version and must match once; the script refuses
otherwise and writes nothing. Writes each next version beside the current one (archiving the old
version is a separate step). 10.15 v1 is written separately (10-15-pride-v1-20261015.md).
Usage (repo root): python "_analytics/Clusters/M08 - pride-arrogance/m08-pride-weave-v1-20261015.py"
"""
import pathlib, sys

D = pathlib.Path('_analytics/essay/spirit_soul_body/inner-being-narrative')
DATE = '20261015'
PLAN = {}

def ch(src, ver_to):
    stem = src.rsplit('-v', 1)[0]
    key = (src, f'{stem}-v{ver_to}-{DATE}.md')
    PLAN[key] = []
    return lambda old, new: PLAN[key].append((old, new))

# ------------------------------------------------------------------ 10.0
e = ch('10-00-the-inner-being-at-work-v6-20261015.md', 7)
e('After them come three that run across all the activities: fear, anger and humility (10.12 to 10.14).',
  'After them come four that run across all the activities: fear, anger, humility and pride (10.12 to 10.15).')

# ------------------------------------------------------------------ 10.14
e = ch('10-14-humility-v1-20261015.md', 2)
e('Chapter 12 holds pride, and this section holds its counterpart.',
  'Pride is in 10.15, and where it goes wrong in Chapter 12. This section holds its counterpart.')
e('- **Chapter 12:** pride, the counterpart.',
  '- **10.15 *Pride* and Chapter 12:** pride, the counterpart.')

# ------------------------------------------------------------------ 12
e = ch('12-when-the-inner-being-goes-wrong-v23-20261015.md', 24)
e('Pride is placed in the heart and in the spirit.\n',
  'Pride is placed in the heart and in the spirit. The whole account of pride, with the boast and the mock, is in 10.15. Here I keep what shows the inner being going wrong.\n')
e('The others envied the gift, and the tree was proud of it (10.6).',
  'The others envied the gift, and the tree was proud of it (10.6). Section 10.15 shows the same order with strength, healing, wealth and majesty: given, then held as one\'s own.')

# ------------------------------------------------------------------ 10.2
e = ch('10-02-knowing-and-hearing-v18-20261015.md', 19)
e('## Perplexity', '''## Pride and hearing

Pride is set against the ear. "Hear and give ear; be not proud, for the Lord has spoken" (Jeremiah 13:15). The scoffer is known by what he will not hear: he "does not listen to rebuke" (Proverbs 13:1); he "does not like to be reproved; he will not go to the wise" (Proverbs 15:12). "By insolence comes nothing but strife, but with those who take advice is wisdom" (Proverbs 13:10). The word itself can be scorned: "the word of the Lord is to them an object of scorn" (Jeremiah 6:10, above). God opens the ear against it: "he opens the ears of men … that he may turn man aside from his deed and conceal pride from a man" (Job 33:16–17). I read pride as the ear that will not take a word against itself, the opposite of the humility above. The whole account is in 10.15.

## Perplexity''')

# ------------------------------------------------------------------ 10.10
e = ch('10-10-relating-to-others-v27-20261015.md', 28)
e('## Holding authority over another', '''## Pride over another

Pride between people stands over someone weaker. "In arrogance the wicked hotly pursue the poor" (Psalm 10:2). "Whoever mocks the poor insults his Maker" (Proverbs 17:5). "The Lord tears down the house of the proud but maintains the widow's boundaries" (Proverbs 15:25). Sodom's pride sat with plenty and ease, and the poor and needy were not helped (Ezekiel 16:49). It closes the heart: "They close their hearts to pity; with their mouths they speak arrogantly" (Psalm 17:10). It divides: "Let us not become conceited, provoking one another, envying one another" (Galatians 5:26). And it is set against love: "'knowledge' puffs up, but love builds up" (1 Corinthians 8:1).

The one under it carries it: "Our soul has had more than enough of the scorn of those who are at ease, of the contempt of the proud" (Psalm 123:4).

The word for boasting turns the other way between people when the boast is in another. "I have great pride in you; I am filled with comfort" (2 Corinthians 7:4). "So give proof before the churches of your love and of our boasting about you to these men" (2 Corinthians 8:24). The whole account is in 10.15.

## Holding authority over another''')

# ------------------------------------------------------------------ 10.7
e = ch('10-07-choosing-and-setting-direction-v30-20261015.md', 31)
e('## Willing\n', '''## Presumption

Some choices go beyond what was given. Israel was told, "Do not go up or fight, for I am not in your midst". "So I spoke to you, and you would not listen; but you rebelled against the command of the Lord and presumptuously went up into the hill country" (Deuteronomy 1:42–43). The prophet "who presumes to speak a word in my name that I have not commanded him to speak" (Deuteronomy 18:20) chooses his own word in place of God's. I read presumption as a choice made on one's own word where another word had been given.

A plan can presume on the time it needs. "Come now, you who say, 'Today or tomorrow we will go into such and such a town and spend a year there and trade and make a profit' — yet you do not know what tomorrow will bring … Instead you ought to say, 'If the Lord wills, we will live and do this or that.' As it is, you boast in your arrogance" (James 4:13–16). "Do not boast about tomorrow, for you do not know what a day may bring" (Proverbs 27:1). The whole account of pride is in 10.15.

## Willing
''')

# ------------------------------------------------------------------ 11
e = ch('11-other-sides-of-the-inner-being-v34-20261015.md', 35)
e('''- **Overflow.** One Hebrew word, *ʿebrah*, is the overflow of anger and the overflow of pride. God offers it to Job with irony: "Pour out the overflowings of your anger, and look on everyone who is proud and abase him" (Job 40:11). And "'Scoffer' is the name of the arrogant, haughty man who acts with arrogant pride" (Proverbs 21:24), where the word is the same.''',
'''- **Overflow.** One Hebrew word, *ʿebrah*, is the overflow of anger and the overflow of pride. God offers it to Job with irony: "Pour out the overflowings of your anger, and look on everyone who is proud and abase him" (Job 40:11). And "'Scoffer' is the name of the arrogant, haughty man who acts with arrogant pride" (Proverbs 21:24), where the word is the same.
- **Lifted up.** One Hebrew word names the heart that grew proud when Uzziah was strong (2 Chronicles 26:16) and Jehoshaphat's heart, "courageous in the ways of the Lord" (2 Chronicles 17:6). One family of words is God's majesty and human pride (Exodus 15:7; Jeremiah 48:29). And the boast moves: "Let not the wise man boast in his wisdom" (Jeremiah 9:23), "but let him who boasts boast in this, that he understands and knows me" (9:24). What differs is where the height comes from, and which way it faces (10.15).''')

# ------------------------------------------------------------------ 13.1
e = ch('13-01-divine-v26-20261015.md', 27)
e('It now also holds what the verses on humbling say of his own lowering.',
  'It now also holds what the verses on humbling say of his own lowering, and what the verses on pride say of his majesty.')
e('## Lowering himself\n', '''## Majesty

The words that name human pride also name God's majesty, and the verses say what his is like.
- **It is his own.** "The Lord reigns; he is robed in majesty … Your throne is established from of old; you are from everlasting" (Psalm 93:1–2).
- **It is shown in what he does.** "I will sing to the Lord, for he has triumphed gloriously; the horse and his rider he has thrown into the sea" (Exodus 15:1). "In the greatness of your majesty you overthrow your adversaries" (15:7). The enemy's own rising is quoted in the same song: "I will pursue, I will overtake, I will divide the spoil, my desire shall have its fill of them" (15:9).
- **It turns toward help.** "There is none like God, O Jeshurun, who rides through the heavens to your help, through the skies in his majesty" (Deuteronomy 33:26). "Ascribe power to God, whose majesty is over Israel … he is the one who gives power and strength to his people" (Psalm 68:34–35).
- **It goes with what only he does.** God says to Job, "Adorn yourself with majesty and dignity … look on everyone who is proud and abase him … Then will I also acknowledge to you that your own right hand can save you" (Job 40:10–14).
- **It is hidden from.** "Enter into the rock and hide in the dust from before the terror of the Lord, and from the splendor of his majesty" (Isaiah 2:10), in the day when "the Lord alone will be exalted" (2:11).
- **It is not seen by all.** "If favor is shown to the wicked, he does not learn righteousness … and does not see the majesty of the Lord" (Isaiah 26:10).
- **It is a name.** The Son "sat down at the right hand of the Majesty on high" (Hebrews 1:3).

**Only he says it of himself.** "I am the Lord, and there is no other, besides me there is no God" (Isaiah 45:5); "I am God, and there is none like me" (Isaiah 46:9). The proud city says the same in its heart: "I am, and there is no one besides me" (Isaiah 47:8). I read that the words true of him are the words pride takes for itself (10.15).

**He gives height.** He gave Nebuchadnezzar "kingship and greatness and glory and majesty" (Daniel 5:18). He chose for his people "the pride of Jacob whom he loves" (Psalm 47:4). "Not from the east or from the west and not from the wilderness comes lifting up, but it is God who executes judgment, putting down one and lifting up another" (Psalm 75:6–7). Though he is high, "he regards the lowly, but the haughty he knows from afar" (Psalm 138:6).

**It is challenged, and not overturned.** "The kings of the earth set themselves, and the rulers take counsel together, against the Lord and against his Anointed … He who sits in the heavens laughs; the Lord holds them in derision" (Psalm 2:2–4). "But you, O Lord, laugh at them; you hold all the nations in derision" (Psalm 59:8). "Toward the scorners he is scornful, but to the humble he gives favor" (Proverbs 3:34). "God is not mocked" (Galatians 6:7). In these verses his laughter answers only those who rise against him. It is never aimed at the weak, as human mocking is (10.15).

**In the Son.** His majesty is received: "we were eyewitnesses of his majesty. For when he received honor and glory from God the Father" (2 Peter 1:16–17). His place rests on what he is: "that in everything he might be preeminent. For in him all the fullness of God was pleased to dwell" (Colossians 1:18–19). At the moment "all were astonished at the majesty of God", he said, "The Son of Man is about to be delivered into the hands of men" (Luke 9:43–44). Then he was mocked on that very standing: "Hail, King of the Jews!" (Matthew 27:29); "Prophesy! Who is it that struck you?" (Luke 22:64); "He saved others; he cannot save himself" (Mark 15:31). He "made no answer" (Luke 23:9), and he prayed, "Father, forgive them, for they know not what they do" (Luke 23:34). I read that the majesty no one can overturn did not defend itself against mockery. Pride grasps a place that is not its own; he "did not count equality with God a thing to be grasped" (Philippians 2:6; *Lowering himself*, below).

## Lowering himself
''')

# ------------------------------------------------------------------ apply
out = {}
for (src, dst), edits in PLAN.items():
    text = (D / src).read_text(encoding='utf-8')
    for old, new in edits:
        n = text.count(old)
        if n != 1:
            sys.exit(f'REFUSED: {src}: anchor found {n} times: {old[:80]!r}')
        text = text.replace(old, new)
    if (D / dst).exists():
        sys.exit(f'REFUSED: {dst} already exists')
    out[dst] = text
for dst, text in out.items():
    (D / dst).write_text(text, encoding='utf-8')
    print('wrote', dst)
