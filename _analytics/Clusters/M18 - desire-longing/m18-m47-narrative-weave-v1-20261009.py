"""M18 x M47 read-back (#1993): apply the narrative changes recorded in m18-m47-validation-register-v1-20261009.csv.

Usage: python m18-m47-narrative-weave-v1-20261009.py [--apply]
Without --apply: checks every quotation in the new text against the ESV in iba.db (read-only) and that each
old string occurs exactly once, and writes nothing. With --apply: writes each chapter as its next version
and moves the prior version to inner-being-narrative/archive/.
"""
import importlib.util, os, re, shutil, sqlite3, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.normpath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v2-20261006.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
DATE = '20261009'

E = {}  # file -> [(old, new)]

# ---------------------------------------------------------------- 10.6 Wanting
E['10-06-wanting-v9-20261008.md'] = [
('''(Chapter 7).

Desire can be aimed at nothing. The Preacher tried everything his heart wanted, and it was "vanity and a striving after wind" (Ecclesiastes 2:11). "Better is the sight of the eyes than the wandering of the appetite [soul]: this also is vanity and a striving after wind" (Ecclesiastes 6:9).
''',
'''(Chapter 7).

Desire can take hold in the heart before anything is done. Jesus says, "everyone who looks at a woman with lustful intent has already committed adultery with her in his heart" (Matthew 5:28). The way in is the eye, and he goes straight on: "If your right eye causes you to sin, tear it out and throw it away" (5:29). Proverbs warns a son in the same order, heart and eyes: "Do not desire her beauty in your heart, and do not let her capture you with her eyelashes" (Proverbs 6:25). The heart is also where desire can be held. Paul speaks of the man who "is firmly established in his heart, being under no necessity but having his desire under control, and has determined this in his heart" (1 Corinthians 7:37). Timothy is told to "flee youthful passions and pursue righteousness, faith, love, and peace, along with those who call on the Lord from a pure heart" (2 Timothy 2:22).

Desire can be aimed at nothing. The Preacher tried everything his heart wanted, and it was "vanity and a striving after wind" (Ecclesiastes 2:11). "Better is the sight of the eyes than the wandering of the appetite [soul]: this also is vanity and a striving after wind" (Ecclesiastes 6:9). He finds envy under much of the striving: "all toil and all skill in work come from a man's envy of his neighbor. This also is vanity and a striving after wind" (4:4). Against it he sets, "Better is a handful of quietness than two hands full of toil and a striving after wind" (4:6). Having everything does not settle it either. He saw "a man to whom God gives wealth, possessions, and honor, so that he lacks nothing of all that he desires, yet God does not give him power to enjoy them" (6:2), and a man whose "soul is not satisfied with life's good things" (6:3). Yet the same book names enjoyment as a gift: "There is nothing better for a person than that he should eat and drink and find enjoyment in his toil. This also, I saw, is from the hand of God, for apart from him who can eat or who can have enjoyment?" (2:24–25). "For to the one who pleases him God has given wisdom and knowledge and joy" (2:26).

Desire can also be pictured as a drive that no one holds back. Israel going after the Baals is "a wild donkey used to the wilderness, in her heat sniffing the wind! Who can restrain her lust?" (Jeremiah 2:24). The people answer, "It is hopeless, for I have loved foreigners, and after them I will go" (2:25).
'''),
('''The Greek word for willing is also used for wanting turned toward harm.''',
'''The words for delight name what a person takes pleasure in, and the verses show delight set on many things.
- **On God's word, against a heart that has stopped feeling:** "their heart is unfeeling like fat, but I delight in your law" (Psalm 119:70).
- **On what satisfies, by invitation:** "Why do you spend your money for that which is not bread, and your labor for that which does not satisfy? Listen diligently to me, and eat what is good, and delight yourselves in rich food" (Isaiah 55:2).
- **On oneself, even in worship:** "in the day of your fast you seek your own pleasure, and oppress all your workers" (Isaiah 58:3; 10.7).
- **Missing where it belongs:** "A fool takes no pleasure in understanding, but only in expressing his opinion" (Proverbs 18:2).
- **On another's harm:** "let those be turned back and brought to dishonor who delight in my hurt!" (Psalm 40:14; 70:2).

Delight can end, and the law then guards the other person. To a man who took a captive woman as his wife: "But if you no longer delight in her, you shall let her go where she wants. But you shall not sell her for money, nor shall you treat her as a slave, since you have humiliated her" (Deuteronomy 21:14). The Hebrew for "where she wants" is her soul. His delight is gone, and her own wanting is protected.

Delight can be misread. The king asked Haman, "What should be done to the man whom the king delights to honor?" And Haman said to himself, "Whom would the king delight to honor more than me?" (Esther 6:6). I read it as a man reading another's delight by his own.

The Greek word for willing is also used for wanting turned toward harm.'''),
('''And what is wanted against God can be given in anger. Israel craved meat, and "while the food was still in their mouths, the anger of God rose against them" (Psalm 78:30–31). They asked for a king: "I gave you a king in my anger" (Hosea 13:11).''',
'''And what is wanted against God can be given in anger. In the wilderness "the rabble that was among them had a strong craving. And the people of Israel also wept again and said, 'Oh that we had meat to eat!'" (Numbers 11:4). They looked back: "it was better for us in Egypt" (11:18). They were given meat "until it comes out at your nostrils and becomes loathsome to you, because you have rejected the Lord who is among you" (11:20). The psalm remembers it: "while the food was still in their mouths, the anger of God rose against them" (Psalm 78:30–31). They asked for a king: "I gave you a king in my anger" (Hosea 13:11). Paul names the same giving over: "God gave them up in the lusts of their hearts to impurity" (Romans 1:24).

Desire can be evil in itself. "The soul of the wicked desires evil; his neighbor finds no mercy in his eyes" (Proverbs 21:10). "The wicked boasts of the desires of his soul, and the one greedy for gain curses and renounces the Lord" (Psalm 10:3). In Micah's day "the great man utters the evil desire of his soul; thus they weave it together" (Micah 7:3). God meets it from the other side: "The Lord does not let the righteous go hungry, but he thwarts the craving of the wicked" (Proverbs 10:3). The sluggard's want gets nothing: "The soul of the sluggard craves and gets nothing, while the soul of the diligent is richly supplied" (Proverbs 13:4). And "Desire without knowledge is not good, and whoever makes haste with his feet misses his way" (Proverbs 19:2).'''),
('''Wanting can be aimed at the living God. "My soul thirsts for God, for the living God. When shall I come and appear before God?" (Psalm 42:2). The thirst is answered with water: "let the one who is thirsty come; let the one who desires take the water of life without price" (Revelation 22:17). A desire met reaches the whole person: "a desire fulfilled is a tree of life" (Proverbs 13:12). And God himself satisfies it: "You open your hand; you satisfy the desire of every living thing" (Psalm 145:16).''',
'''Wanting can be aimed at the living God. "My soul thirsts for God, for the living God. When shall I come and appear before God?" (Psalm 42:2). "In the path of your judgments, O Lord, we wait for you; your name and remembrance are the desire of our soul" (Isaiah 26:8). "My soul is consumed with longing for your rules at all times" (Psalm 119:20). When Judah "had sought him with their whole desire", "he was found by them" (2 Chronicles 15:15). Peter writes, "Like newborn infants, long for the pure spiritual milk, that by it you may grow up into salvation" (1 Peter 2:2), and adds, "if indeed you have tasted that the Lord is good" (2:3). Paul turns an eagerness for the Spirit's gifts outward: "since you are eager for manifestations of the Spirit, strive to excel in building up the church" (1 Corinthians 14:12).

The thirst is answered with water: "let the one who is thirsty come; let the one who desires take the water of life without price" (Revelation 22:17). God hears the desire: "O Lord, you hear the desire of the afflicted; you will strengthen their heart" (Psalm 10:17). He gives it: "You have given him his heart's desire and have not withheld the request of his lips" (Psalm 21:2). A desire met reaches the whole person: "a desire fulfilled is a tree of life" (Proverbs 13:12), and "A desire fulfilled is sweet to the soul, but to turn away from evil is an abomination to fools" (13:19). And God himself satisfies it: "You open your hand; you satisfy the desire of every living thing" (Psalm 145:16).

Wanting can be aimed at a person. "The soul of my son Shechem longs for your daughter," Hamor says (Genesis 34:8), after Shechem "seized her and lay with her and humiliated her" (34:2). The longing is spoken inside a story of outrage. Paul's longing for the churches is the other face: "since we were torn away from you, brothers, for a short time, in person not in heart, we endeavored the more eagerly and with great desire to see you face to face" (1 Thessalonians 2:17). "So, being affectionately desirous of you, we were ready to share with you not only the gospel of God but also our own selves" (2:8). "For I long to see you, that I may impart to you some spiritual gift to strengthen you" (Romans 1:11).

What is desired can be taken away. God tells Ezekiel of the day "when I take from them their stronghold, their joy and glory, the delight of their eyes and their soul's desire, and also their sons and daughters" (Ezekiel 24:25). The sanctuary was "the delight of your eyes, and the yearning of your soul" (24:21). Over Babylon it is said, "The fruit for which your soul longed has gone from you" (Revelation 18:14). And a longing can turn into its opposite: "the twilight I longed for has been turned for me into trembling" (Isaiah 21:4).'''),
('''Gehazi swore by the Lord's life on his way to get what his master had refused: "As the Lord lives, I will run after him and get something from him" (2 Kings 5:20).''',
'''Gehazi swore by the Lord's life on his way to get what his master had refused: "As the Lord lives, I will run after him and get something from him" (2 Kings 5:20). Greed takes life, its own and others': "Such are the ways of everyone who is greedy for unjust gain; it takes away the life of its possessors" (Proverbs 1:19). Ezekiel's princes are "like wolves tearing the prey, shedding blood, destroying lives to get dishonest gain" (Ezekiel 22:27).'''),
('''since desire conceived brings forth death.''',
'''since desire conceived brings forth death; with God's own delight and desire (13.1, *Delight*).'''),
]

# ---------------------------------------------------------------- Ch 5 The soul
E['05-the-soul-v3-20261005.md'] = [
('''"Because you crave meat [your soul desires], you may eat meat whenever you desire" (Deuteronomy 12:20). "Whatever your appetite craves" (Deuteronomy 14:26). "There is … no first-ripe fig that my soul desires" (Micah 7:1).''',
'''"Because you crave meat [your soul desires], you may eat meat whenever you desire" (Deuteronomy 12:20). "There is … no first-ripe fig that my soul desires" (Micah 7:1). The law makes room for the want before God. The tithe could be spent "for whatever you desire — oxen or sheep or wine or strong drink, whatever your appetite craves. And you shall eat there before the Lord your God and rejoice, you and your household" (Deuteronomy 14:26). The same idiom sets the reach of a rule. God says to Jeroboam, "you shall reign over all that your soul desires" (1 Kings 11:37). Abner promises David the same (2 Samuel 3:21), and the Ziphites invite Saul to come down "according to all your heart's desire" to take David (1 Samuel 23:20). There, "heart" is the soul word.'''),
('''- "My soul longs, yes, faints for the courts of the Lord" (Psalm 84:2).
''',
'''- "My soul longs, yes, faints for the courts of the Lord" (Psalm 84:2).
- "My soul is consumed with longing for your rules at all times" (Psalm 119:20).
- "Your name and remembrance are the desire of our soul" (Isaiah 26:8).
'''),
('''Satan's rule is that "all that a man has he will give for his life" (Job 2:4). But before God, nothing buys a soul back: "what shall a man give in return for his soul?" (Matthew 16:26).''',
'''Satan's rule is that "all that a man has he will give for his life" (Job 2:4). No one can pay that price for another: "Truly no man can ransom another, or give to God the price of his life, for the ransom of their life is costly and can never suffice" (Psalm 49:7–8). And before God, nothing buys a soul back: "what shall a man give in return for his soul?" (Matthew 16:26).

A life can be precious in someone's eyes. Saul, spared by David, says, "I will no more do you harm, because my life was precious in your eyes this day" (1 Samuel 26:21). The third captain sent for Elijah fell on his knees: "please let my life, and the life of these fifty servants of yours, be precious in your sight" (2 Kings 1:13–14). Then the angel of the Lord told Elijah to go down with him (1:15). Of the king, the psalm says, "From oppression and violence he redeems their life, and precious is their blood in his sight" (Psalm 72:14). A life can also be hunted because it is precious: "the price of a prostitute is only a loaf of bread, but a married woman hunts down a precious life" (Proverbs 6:26). God's own word, "you are precious in my eyes", is in 13.1 (Isaiah 43:4).

And the soul can be entrusted: "let those who suffer according to God's will entrust their souls to a faithful Creator while doing good" (1 Peter 4:19).'''),
('''"Whoever loves his life loses it, and whoever hates his life in this world will keep it for eternal life" (John 12:25).''',
'''"Whoever loves his life loses it, and whoever hates his life in this world will keep it for eternal life" (John 12:25). The other Gospels put it as wanting: "whoever would save his life will lose it, but whoever loses his life for my sake will find it" (Matthew 16:25; Mark 8:35; Luke 9:24). Paul lives it: "I do not account my life of any value nor as precious to myself, if only I may finish my course" (Acts 20:24).'''),
('''There is a third kind of hating one's life, which is exhaustion rather than discipleship. "I loathe my life" (Job 10:1). "So I hated life" (Ecclesiastes 2:17). Jonah: "take my life from me, for it is better for me to die than to live" (Jonah 4:3). I looked at these death-wishes, and how they are answered, in Chapter 2.''',
'''There is a third kind of hating one's life, and each verse gives its own ground. Job: "I loathe my life; I will give free utterance to my complaint; I will speak in the bitterness of my soul" (Job 10:1). The Preacher: "So I hated life, because what is done under the sun was grievous to me, for all is vanity and a striving after wind" (Ecclesiastes 2:17). Jonah asked to die because God had spared Nineveh: "for I knew that you are a gracious God and merciful … Therefore now, O Lord, please take my life from me, for it is better for me to die than to live" (Jonah 4:2–3). God answered with a question about his anger: "Do you do well to be angry?" (4:4). Only the second time did the wish come with faintness, when "the sun beat down on the head of Jonah so that he was faint" (4:8). I looked at these death-wishes, and how they are answered, in Chapter 2.'''),
]

# ---------------------------------------------------------------- Ch 4 The heart
E['04-the-heart-v12-20261008.md'] = [
('''It is "a stream of water in the hand of the Lord" (Proverbs 21:1). And it is a mirror: "As in water face reflects face, so the heart of man reflects the man" (Proverbs 27:19).''',
'''And it is a mirror: "As in water face reflects face, so the heart of man reflects the man" (Proverbs 27:19). One picture is not of a state at all, but of a heart being directed: "The king's heart is a stream of water in the hand of the Lord; he turns it wherever he will" (Proverbs 21:1). The word for "will" is the word for delight: wherever he pleases (13.1, *Delight*).'''),
('''desires ("the desires of your heart", Psalm 37:4),''',
'''desires ("the desires of your heart", Psalm 37:4), lusts ("has already committed adultery with her in his heart", Matthew 5:28),'''),
]

# ---------------------------------------------------------------- Ch 6 The spirit
E['06-the-spirit-v10-20261008.md'] = [
('''In the Old Testament, some come from God: "a harmful spirit from the Lord tormented him" (1 Samuel 16:14).''',
'''In the Old Testament, some come from God: "a harmful spirit from the Lord tormented him" (1 Samuel 16:14). His servants sought a man to play the lyre (16:16), and when David played, "Saul was refreshed and was well, and the harmful spirit departed from him" (16:23).'''),
('''- **Fills with ability:**''',
'''- **Instructs and leads:** "You gave your good Spirit to instruct them" (Nehemiah 9:20). "Teach me to do your will, for you are my God! Let your good Spirit lead me on level ground!" (Psalm 143:10).
- **Carries those who speak:** "no prophecy was ever produced by the will of man, but men spoke from God as they were carried along by the Holy Spirit" (2 Peter 1:21).
- **Fills with ability:**'''),
]

# ---------------------------------------------------------------- Ch 7 Flesh
E['07-flesh-v6-20261005.md'] = [
('''- "The desires of the flesh and the desires of the eyes and pride of life" (1 John 2:16).''',
'''- "The desires of the flesh and the desires of the eyes and pride of life" (1 John 2:16).

The same letters say what is to be done with these desires. "Walk by the Spirit, and you will not gratify the desires of the flesh" (Galatians 5:16). "Those who belong to Christ Jesus have crucified the flesh with its passions and desires" (5:24). "Put on the Lord Jesus Christ, and make no provision for the flesh, to gratify its desires" (Romans 13:14). Peter speaks of living "for the rest of the time in the flesh no longer for human passions but for the will of God" (1 Peter 4:2). In that verse "the flesh" is simply life in the body, and the passions are what it is no longer lived for. The same desires can be used on others. False teachers "entice by sensual passions of the flesh those who are barely escaping from those who live in error" (2 Peter 2:18); they "indulge in the lust of defiling passion and despise authority" (2:10). And flesh can be an outward mark to boast in: "It is those who want to make a good showing in the flesh who would force you to be circumcised", and "they desire to have you circumcised that they may boast in your flesh" (Galatians 6:12–13).'''),
]

# ---------------------------------------------------------------- Ch 8 Conscience
E['08-conscience-and-bosom-v5-20261005.md'] = [
('''"I always take pains to have a clear conscience toward both God and man" (Acts 24:16).''',
'''"I always take pains to have a clear conscience toward both God and man" (Acts 24:16). "Pray for us, for we are sure that we have a clear conscience, desiring to act honorably in all things" (Hebrews 13:18).'''),
]

# ---------------------------------------------------------------- Ch 12
E['12-when-the-inner-being-goes-wrong-v13-20261008.md'] = [
('''- "Pride goes before destruction, and a haughty spirit before a fall" (Proverbs 16:18).''',
'''- "Pride goes before destruction, and a haughty spirit before a fall" (Proverbs 16:18). The next verse: "It is better to be of a lowly spirit with the poor than to divide the spoil with the proud" (16:19).'''),
]

# ---------------------------------------------------------------- 10.1 Feeling
E['10-01-feeling-v13-20261008.md'] = [
('''and even something that does good: "Sorrow is better than laughter, for by sadness of face the heart is made glad" (Ecclesiastes 7:3).''',
'''and even something that does good: "Sorrow is better than laughter, for by sadness of face the heart is made glad" (Ecclesiastes 7:3). The verse before gives the house of mourning its reason: "for this is the end of all mankind, and the living will lay it to heart" (7:2).'''),
('''"A glad heart makes a cheerful face" (Proverbs 15:13).''',
'''"A glad heart makes a cheerful face" (Proverbs 15:13). "The cheerful of heart has a continual feast" (15:15).'''),
]

# ---------------------------------------------------------------- 10.5 Speaking
E['10-05-speaking-v12-20261004.md'] = [
('''- "Their hearts devise violence, and their lips talk of trouble" (Proverbs 24:2).''',
'''- "Their hearts devise violence, and their lips talk of trouble" (Proverbs 24:2).
- "My heart overflows with a pleasing theme; I address my verses to the king; my tongue is like the pen of a ready scribe" (Psalm 45:1).'''),
('''"The mouth of the righteous is a fountain of life" (Proverbs 10:11).''',
'''"The mouth of the righteous is a fountain of life" (Proverbs 10:11). "Gracious words are like a honeycomb, sweetness to the soul and health to the body" (Proverbs 16:24).'''),
]

# ---------------------------------------------------------------- 10.7
E['10-07-choosing-and-setting-direction-v18-20261008.md'] = [
('''- rest: *"This is rest; give rest to the weary; and this is repose"; yet they would not hear* (Isaiah 28:12)''',
'''- rest: *"This is rest; give rest to the weary; and this is repose"; yet they would not hear* (Isaiah 28:12); and *"ask for the ancient paths, where the good way is; and walk in it, and find rest for your souls. But they said, 'We will not walk in it'"* (Jeremiah 6:16)
- the one who brought God's word: *"He received living oracles to give to us. Our fathers refused to obey him, but thrust him aside, and in their hearts they turned to Egypt"* (Acts 7:38–39)'''),
('''- After consecration, *"all who were of a willing heart brought burnt offerings"* (2 Chronicles 29:31).''',
'''- After consecration, *"all who were of a willing heart brought burnt offerings"* (2 Chronicles 29:31).
- At the gifts for the temple, *"the people rejoiced because they had given willingly, for with a whole heart they had offered freely to the Lord. David the king also rejoiced greatly"* (1 Chronicles 29:9). David says of his own gift, *"In the uprightness of my heart I have freely offered all these things, and now I have seen your people, who are present here, offering freely and joyously to you"* (29:17).
- In battle: *"My heart goes out to the commanders of Israel who offered themselves willingly among the people. Bless the Lord"* (Judges 5:9).
- Of the churches' gift for Jerusalem: *"For they were pleased to do it, and indeed they owe it to them"* (Romans 15:27).'''),
('''**A will under another.** *"So then it depends not on human will or exertion, but on God, who has mercy"* (Romans 9:16).''',
'''**A will under another.** *"So then it depends not on human will or exertion, but on God, who has mercy"* (Romans 9:16). New birth is *"not of blood nor of the will of the flesh nor of the will of man, but of God"* (John 1:13). The will can be taught and filled: *"Teach me to do your will, for you are my God!"* (Psalm 143:10); Paul prays that the Colossians *"may be filled with the knowledge of his will in all spiritual wisdom and understanding"* (Colossians 1:9). Servants work *"as bondservants of Christ, doing the will of God from the heart"* (Ephesians 6:6), where "heart" is the soul word.'''),
]

# ---------------------------------------------------------------- Ch 11
E['11-patterns-of-the-inner-life-v19-20261008.md'] = [
('''Solomon's people "went to their homes joyful and glad of heart for all the goodness that the Lord had shown" (1 Kings 8:66).''',
'''Solomon's people "went to their homes joyful and glad of heart for all the goodness that the Lord had shown" (1 Kings 8:66). The Preacher commands the merry heart and gives God's approval as the reason: "Go, eat your bread with joy, and drink your wine with a merry heart, for God has already approved what you do" (Ecclesiastes 9:7).'''),
]

# ---------------------------------------------------------------- 13.1
E['13-01-divine-v9-20261008.md'] = [
('''It is one of the creatures God names as beyond a man's control. 13.4 takes up nature.
''',
'''It is one of the creatures God names as beyond a man's control. 13.4 takes up nature.

## Delight

The words for a person's delight and desire are used of God too. The verses say what he delights in and whom he is pleased with, and they show him doing what pleases him.

**What he delights in.**
- *"Those of crooked heart are an abomination to the Lord, but those of blameless ways are his delight"* (Proverbs 11:20).
- David, as he gives freely: *"I know, my God, that you test the heart and have pleasure in uprightness"* (1 Chronicles 29:17).
- A purpose in a heart pleases him even when he does not let it be carried out: *"Whereas it was in your heart to build a house for my name, you did well that it was in your heart. Nevertheless, you shall not build the house"* (1 Kings 8:18–19; 2 Chronicles 6:8–9).
- He *"found in David the son of Jesse a man after my heart, who will do all my will"* (Acts 13:22).
- To Jehu: *"Because you have done well in carrying out what is right in my eyes, and have done to the house of Ahab according to all that was in my heart, your sons of the fourth generation shall sit on the throne of Israel"* (2 Kings 10:30). The next verse turns to Jehu's own heart: *"But Jehu was not careful to walk in the law of the Lord, the God of Israel, with all his heart"* (10:31).
- A people valued: *"Because you are precious in my eyes, and honored, and I love you, I give men in return for you, peoples in exchange for your life"* (Isaiah 43:4). Hezekiah, delivered, says, *"in love you have delivered my life from the pit of destruction, for you have cast all my sins behind your back"* (Isaiah 38:17).
- A fast he does not accept: *"Will you call this a fast, and a day acceptable to the Lord?"* (Isaiah 58:5). What he chooses instead is in *Choosing* (58:6).

**Whom he is pleased with.** At Jesus' baptism *"the Holy Spirit descended on him in bodily form, like a dove; and a voice came from heaven, 'You are my beloved Son; with you I am well pleased'"* (Luke 3:22). In one verse the voice from heaven speaks, the Son is named, and the Spirit comes down. Matthew applies Isaiah's *"my beloved with whom my soul is well pleased"* to Jesus (Matthew 12:18; *Choosing*). Paul says that God *"was pleased to reveal his Son to me"* (Galatians 1:16). And of one who turns back: *"my righteous one shall live by faith, and if he shrinks back, my soul has no pleasure in him"* (Hebrews 10:38).

**He does what pleases him.**
- *"The king's heart is a stream of water in the hand of the Lord; he turns it wherever he will"* (Proverbs 21:1). The word for "will" is the word for delight. The next verse: *"Every way of a man is right in his own eyes, but the Lord weighs the heart"* (21:2).
- Job: *"But he is unchangeable, and who can turn him back? What he desires, that he does"* (Job 23:13). Job does not take it as comfort: *"Therefore I am terrified at his presence"* (23:15).
- The sailors, before they throw Jonah into the sea: *"O Lord, let us not perish for this man's life, and lay not on us innocent blood, for you, O Lord, have done as it pleased you"* (Jonah 1:14). Afterwards *"the men feared the Lord exceedingly"* (1:16).
- Of his servant: *"Yet it was the will of the Lord to crush him; he has put him to grief; when his soul makes an offering for guilt, he shall see his offspring; he shall prolong his days; the will of the Lord shall prosper in his hand"* (Isaiah 53:10). Both times, "the will of the Lord" is the delight word. The verse does not explain it, and I leave it as it stands.

His delight stands beside his choosing (*Choosing*) and his will (*Willing*). What a person delights in is in 10.6.
'''),
]

# ---------------------------------------------------------------- 13.2
E['13-02-angels-v1-20261007.md'] = [
('''*Nothing has been placed here yet. Verses are gathered here as each part of the study is taken up again (see 13 "Other beings").*''',
'''Angels long to look into what has been told to people. Peter writes of the things "announced to you through those who preached the good news to you by the Holy Spirit sent from heaven, things into which angels long to look" (1 Peter 1:12). The prophets had "searched and inquired carefully" about the same salvation (1:10). The word for the angels' longing is the word used for human desire (10.6).

*Verses are gathered here as each part of the study is taken up again (see 13 "Other beings").*'''),
]

# ---------------------------------------------------------------- quote check
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
for fname, edits in E.items():
    path = os.path.join(NARR, fname)
    src = open(path, encoding='utf-8').read()
    for old, new in edits:
        n = src.count(old)
        if n != 1: fails.append(f'{fname}: old string occurs {n} times: {old[:80]!r}')
        # which part of new is genuinely new
        added = new.replace(old, '') if old in new else new
        prior = list(xr.cites(old))
        last_book = prior[-1][0] if prior else None
        for line in added.split('\n'):
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
                if not cites: fails.append(f'{fname}: no citation parsed for "{frag[:50]}"'); continue
                book, ch = cites[0][0], cites[0][1]
                vs = sorted({v for b, cc, v, h in cites if b == book and cc == ch})
                vs = list(range(min(vs) - 0, max(vs) + 1)) if vs else vs
                text = norm(verse_text(book, ch, range(min(vs), max(vs) + 2)))  # allow spill to next verse
                for part in re.split(r'…|\.\.\.', frag):
                    p = norm(part)
                    if p and p not in text:
                        fails.append(f'{fname}: "{part.strip()[:70]}" not in {book} {ch}:{vs}')
                checked += 1
print(f'quotes checked: {checked}; failures: {len(fails)}')
for f in fails: print('  FAIL', f)

if '--apply' in sys.argv:
    if fails: sys.exit('not applied: fix failures first')
    os.makedirs(os.path.join(NARR, 'archive'), exist_ok=True)
    for fname, edits in E.items():
        path = os.path.join(NARR, fname)
        src = open(path, encoding='utf-8').read()
        for old, new in edits: src = src.replace(old, new)
        m = re.match(r'(.+)-v(\d+)-\d{8}\.md$', fname)
        newname = f'{m.group(1)}-v{int(m.group(2)) + 1}-{DATE}.md'
        open(os.path.join(NARR, newname), 'w', encoding='utf-8').write(src)
        shutil.move(path, os.path.join(NARR, 'archive', fname))
        print('wrote', newname, '; archived', fname)
