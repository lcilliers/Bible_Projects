"""Weave of the M18 x M25 read-back and the held items (OT-95, OT-96, OT-15, #1942) into the narrative (#1993, 2026-10-09).

Readings: m18-m25-inner-being-reading-v1-20261009.md, m18-held-items-reading-v1-20261009.md (same folder).
10.6 was rewritten whole as v11 (by hand). This script makes the targeted insertions in the other chapters.
Each op: (chapter prefix, mode, anchor, text). Modes:
  after_line  - insert text as new paragraph(s) after the line that contains the anchor
  before_line - insert before the line that contains the anchor
  replace     - replace the anchor substring with text
  append_line - append text to the end of the line that contains the anchor
Every anchor must match exactly one line. Prior versions are copied to archive/ and the new file gets v+1 and today's date.
"""
import glob, os, re, shutil, sys

NARR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DATE = '20261009'

OPS = {
'10-07-': [
 ('replace', 'Isaiah 1 is the one place in these verses where the will is invited with an "if". Both ways are set before it, as life and death are in the next section.',
  'Isaiah 1 invites the will with an "if", and both ways are set before it, as life and death are in the next section. Jesus does the same. A young man asked about doing: *"Teacher, what good deed must I do to have eternal life?"* He was answered with the will: *"If you would enter life, keep the commandments"* (Matthew 19:16–17). He had kept them, and still asked, *"What do I still lack?"* He was answered with the will again: *"If you would be perfect, go, sell what you possess and give to the poor … and come, follow me"* (19:20–21). *"When the young man heard this he went away sorrowful, for he had great possessions"* (19:22). He knew what he lacked. Asked for the thing he held, his will would not, and the sorrow is what that felt like. The disciples ask, *"Who then can be saved?"*, and are told, *"With man this is impossible, but with God all things are possible"* (19:25–26). *A will under another*, below, ends in the same place.'),
 ('before_line', '- cleansing, after reasoning:',
  '- life itself, from the one who gives it: *"yet you refuse to come to me that you may have life"* (John 5:40). Here the passage says what lies behind the refusal. They had searched the Scriptures (5:39), so it was not that they did not know. *"But I know that you do not have the love of God within you … How can you believe, when you receive glory from one another and do not seek the glory that comes from the only God?"* (5:42, 44). The will refused because the desire was set on glory from people.'),
 ('append_line', 'you will be free from this oath"* (24:7–8).',
  '\n- It can turn when its own cost appears, and another can bind himself instead. The nearer redeemer first says of Naomi\'s land, *"I will redeem it"* (Ruth 4:4). Told that Ruth comes with it, he says, *"I cannot redeem it for myself, lest I impair my own inheritance"* (4:6). It is the same man in the same scene, and his will turns when his own inheritance is touched. Boaz had left room for that will and had bound his own: *"if he is not willing to redeem you, then, as the Lord lives, I will redeem you"* (3:13). Ruth\'s choice frames it: *"you have not gone after young men"* (3:10). One will is bound to self-interest, one by an oath, and one, Ruth\'s, is given in kindness.'),
 ('after_line', 'said after *"your passions are at war within you"* (4:1).',
  '**The will set on godliness.** *"Indeed, all who desire to live a godly life in Christ Jesus will be persecuted"* (2 Timothy 3:12). It is the same verb as *"those who desire to be rich"*. The desire for riches falls into a snare. The desire for godliness walks into persecution. Paul does not promise that the godly will has an easy road. He sets it beside his own sufferings: *"yet from them all the Lord rescued me"* (3:11).'),
 ('after_line', 'God\'s will is in 13.1 (*Willing*).',
  'Peter was told that his own will would be overruled at the end: *"when you were young, you used to dress yourself and walk wherever you wanted, but when you are old, you will stretch out your hands, and another will dress you and carry you where you do not want to go"* (John 21:18). His next words were about someone else: *"Lord, what about this man?"* (21:21). The answer was *"If it is my will that he remain until I come, what is that to you? You follow me!"* (21:22). Told that his own will would be overruled, he turned to compare his lot with another\'s, and Christ\'s will answered both.'),
 ('after_line', 'puts heart and spirit side by side in setting out to give.',
  '- **Set, beside a wrong love.** Jehoshaphat was told, *"Should you help the wicked and love those who hate the Lord? Because of this, wrath has gone out against you from the Lord. Nevertheless, some good is found in you, for you destroyed the Asheroth out of the land, and have set your heart to seek God"* (2 Chronicles 19:2–3). A love wrongly given and a heart set to seek God stand in one king, and the prophet\'s verdict holds both.'),
 ('after_line', '- **Their own fears.**',
  '- **Filled with one\'s own ways.** *"The backslider in heart will be filled with the fruit of his ways, and a good man will be filled with the fruit of his ways"* (Proverbs 14:14). It is the same filling as *"have their fill of their own devices"* (Proverbs 1:31). The verse before it: *"Even in laughter the heart may ache"* (14:13).'),
 ('append_line', 'Of a king\'s plans against strongholds: *"but only for a time"* (Daniel 11:24).',
  ' The next verse says what he roused for it: *"he shall stir up his power and his heart"* (11:25). The heart is stirred up as a resource for war.\n- Counsel that cannot save: *"You are wearied with your many counsels; let them stand forth and save you … No coal for warming oneself is this, no fire to sit before!"* (Isaiah 47:13–14). Many counsels weary the one who keeps them, and they give no warmth.'),
],
'13-01-': [
 ('append_line', 'my soul has no pleasure in him"* (Hebrews 10:38).',
  ' Wisdom says that favour is found by finding her: *"For whoever finds me finds life and obtains favor from the Lord, but he who fails to find me injures himself; all who hate me love death"* (Proverbs 8:35–36). The finding is by daily waiting, *"watching daily at my gates, waiting beside my doors"* (8:34). At the end love and hate are turned over: to hate wisdom is to love death, a love the person does not know he has.'),
 ('before_line', '**He does what pleases him.**',
  '**What he has no pleasure in.** *"Have I any pleasure in the death of the wicked, declares the Lord God, and not rather that he should turn from his way and live?"* (Ezekiel 18:23). It is said to people who accuse him: *"Yet you say, \'The way of the Lord is not just\'"* (18:25). He ends, *"make yourselves a new heart and a new spirit! Why will you die, O house of Israel? For I have no pleasure in the death of anyone, declares the Lord God; so turn, and live"* (18:31–32). He says it again to people in despair, who ask, *"Surely our transgressions and our sins are upon us, and we rot away because of them. How then can we live?"* (33:10). This time it is on oath: *"As I live, declares the Lord God, I have no pleasure in the death of the wicked, but that the wicked turn from his way and live"* (33:11). The same words answer accusing and despairing. I read that his pleasure is told to the inner state of the hearer.\n\nThe death of his own is not taken lightly either: *"Precious in the sight of the Lord is the death of his saints"* (Psalm 116:15). The word is not delight but "precious": weighty, costly. The psalmist had been in *"the snares of death"* (116:3) and was delivered (116:8). I read: not glad of it, but not careless of it. The same word was used between two men: *"my life was precious in your eyes this day"* (1 Samuel 26:21; Chapter 5).\n'),
 ('after_line', 'The verse does not explain it, and I leave it as it stands.',
  '- Of Eli\'s sons: *"But they would not listen to the voice of their father, for it was the will of the Lord to put them to death"* (1 Samuel 2:25). "Will" is the delight word again. Their father had just said, *"if someone sins against the Lord, who can intercede for him?"*, and the next verse sets Samuel beside them, growing *"in favor with the Lord and also with man"* (2:26). Set beside *"I have no pleasure in the death of anyone"* (Ezekiel 18:32), the two verses seem to pull apart. I do not reconcile them. They stand as Isaiah 53:10 stands.'),
 ('replace', 'It is the one place in these verses where two wills are named side by side and one is given up to the other.',
  'Two wills are named side by side here, and one is given up to the other. John has the Son say it beforehand, as the reason he came: *"For I have come down from heaven, not to do my own will but the will of him who sent me. And this is the will of him who sent me, that I should lose nothing of all that he has given me, but raise it up on the last day. For this is the will of my Father, that everyone who looks on the Son and believes in him should have eternal life"* (John 6:38–40). The Father\'s will there has content: that none be lost.'),
 ('after_line', 'to each one individually as he wills"* (1 Corinthians 12:11).',
  '- The Son gives life: *"For as the Father raises the dead and gives them life, so also the Son gives life to whom he will"* (John 5:21).\n- Over a disciple\'s life: *"If it is my will that he remain until I come, what is that to you? You follow me!"* (John 21:22). The saying was misread at once: *"So the saying spread abroad among the brothers that this disciple was not to die"* (21:23). What it meant for Peter is in 10.7 (*Willing*).'),
 ('after_line', '**He is good, upright and holy.**',
  'His goodness is named toward those who wait: *"The Lord is good to those who wait for him, to the soul who seeks him"* (Lamentations 3:25). It is said straight after the soul\'s own word, *"\'The Lord is my portion,\' says my soul, \'therefore I will hope in him\'"* (3:24). And it is asked for the upright under pressure: *"Do good, O Lord, to those who are good, and to those who are upright in their hearts!"* (Psalm 125:4; 10.8).'),
 ('after_line', 'His delight stands beside his choosing (*Choosing*) and his will (*Willing*).',
  '''## Jealousy

The jealousy words are used of God, and the verses say what his jealousy is for and what it is against.
- **For his people, against those who scorned them.** *"Surely I have spoken in my hot jealousy against the rest of the nations and against all Edom, who gave my land to themselves as a possession with wholehearted joy and utter contempt"* (Ezekiel 36:5). *"Behold, I have spoken in my jealous wrath, because you have suffered the reproach of the nations"* (36:6). His jealousy answers another's joy in taking what is his, and his people's shame.
- **Roused after long restraint.** *"The Lord goes out like a mighty man, like a man of war he stirs up his zeal; he cries out, he shouts aloud, he shows himself mighty against his foes. For a long time I have held my peace; I have kept still and restrained myself; now I will cry out like a woman in labor; I will gasp and pant"* (Isaiah 42:13–14). In two verses his zeal is a warrior and a woman giving birth. I read zeal that both fights and brings forth, held in a long time and then let go with a cry. The prophet puts the two pictures together; I only note them.
- **Over his own people's spirit.** *"You adulterous people! Do you not know that friendship with the world is enmity with God? … Or do you suppose it is to no purpose that the Scripture says, 'He yearns jealously over the spirit that he has made to dwell in us'? But he gives more grace"* (James 4:4–6). The picture is a husband's jealousy over a divided love, and it is aimed at the spirit he made to dwell in people. The next words are grace. In Ezekiel his jealousy turns outward on enemies. In James it turns toward his own people, and it is met with more grace.
- **What provokes it.** Ezekiel was brought *"to the entrance of the gateway of the inner court that faces north, where was the seat of the image of jealousy, which provokes to jealousy"*, and *"behold, the glory of the God of Israel was there"* (Ezekiel 8:3–4). The image provokes by standing where he is.
- **Joined with anger,** where other gods are put beside him: *"For the Lord your God in your midst is a jealous God—lest the anger of the Lord your God be kindled against you"* (Deuteronomy 6:15; 10.13).

A person's jealousy is in 10.6 (*Jealousy and envy*).

## Stirring

God acts on the spirits of people, his own and kings who do not know him, and the verses say toward what and on what grounds.

**Toward building.** *"the Lord stirred up the spirit of Cyrus king of Persia, so that he made a proclamation"* (Ezra 1:1; 2 Chronicles 36:22). *"I have stirred him up in righteousness, and I will make all his ways level; he shall build my city and set my exiles free, not for price or reward"* (Isaiah 45:13). *"I stirred up one from the north, and he has come … and he shall call upon my name"* (41:25). Then his own people: *"everyone whose spirit God had stirred to go up to rebuild the house of the Lord"* (Ezra 1:5). Haggai gives the order. They *"obeyed the voice of the Lord"*, and *"the people feared the Lord"* (Haggai 1:12). Haggai brought the word *"I am with you, declares the Lord"* (1:13). *"And the Lord stirred up the spirit of Zerubbabel … and the spirit of all the remnant of the people. And they came and worked on the house of the Lord of hosts, their God"* (1:14). The stirring came after obedience, fear and a word of his presence, and it ended in work.

**Toward judgment.** The verses give the ground each time:
- after broken faith: *"But they broke faith with the God of their fathers … So the God of Israel stirred up the spirit of Pul king of Assyria"* (1 Chronicles 5:25–26)
- after a king's sin and a written warning (2 Chronicles 21:12–15): *"And the Lord stirred up against Jehoram the anger of the Philistines"* (21:16)
- for his purpose: *"The Lord has stirred up the spirit of the kings of the Medes, because his purpose concerning Babylon is to destroy it, for that is the vengeance of the Lord, the vengeance for his temple"* (Jeremiah 51:11; 51:1; 50:9)
- with those once desired: *"I will stir up against you your lovers from whom you turned in disgust"* (Ezekiel 23:22; 10.6)
- with his own people as his weapon: *"For I have bent Judah as my bow; I have made Ephraim its arrow. I will stir up your sons, O Zion"* (Zechariah 9:13). And to bring them back: *"I will stir them up from the place to which you have sold them"* (Joel 3:7)

The place he stirs is the spirit (Chapter 6), whether the end is building or destroying. The one stirred still acts as himself: Cyrus makes a proclamation and puts it in writing. The two foreign agents are described alike. The Medes *"have no regard for silver and do not delight in gold"* (Isaiah 13:17), and Cyrus builds *"not for price or reward"*. I read that God stirs a spirit already fitted to the task. The verses do not say whether the stirring made it so.

**He rouses himself.** *"Be silent, all flesh, before the Lord, for he has roused himself from his holy dwelling"* (Zechariah 2:13). People call on him to wake (10.9). And he holds back: *"he restrained his anger often and did not stir up all his wrath"* (Psalm 78:38; 10.13).'''),
],
'13-02-': [
 ('before_line', '*Verses are gathered here',
  'An angel wakes a prophet to see. *"And the angel who talked with me came again and woke me, like a man who is awakened out of his sleep"* (Zechariah 4:1). His first words are a question: *"What do you see?"* (4:2). The waking is for seeing (10.2).\n'),
],
'10-10-': [
 ('after_line', 'Loyalty between people was sworn by life.',
  'Delight in a person can stand against a father. *"And Saul spoke to Jonathan his son and to all his servants, that they should kill David. But Jonathan, Saul\'s son, delighted much in David"* (1 Samuel 19:1). The writer names him "Saul\'s son" just where he stands against Saul. The delight acts. Jonathan warns David (19:2). He stands beside his father in the field (19:3). He speaks well of David: *"Let not the king sin against his servant David"* (19:4). And he reminds Saul of Saul\'s own joy: *"You saw it, and rejoiced"* (19:5). Saul listens and swears that David shall not be put to death (19:6). Jonathan\'s bond is named twice: his soul *"knit to the soul of David"* (18:1, above), and here, in the danger, his delight. Saul\'s turn had begun with a saying that *"displeased him"*, and *"Saul eyed David from that day on"* (18:8–9). I read delight and displeasure about one man, in a son and a father, with the look on the side of displeasure (10.6, *Jealousy and envy*).'),
 ('after_line', '- **The anger of the powerful decides others\' fate.**',
  '- **The law allows for heat.** The cities of refuge exist *"lest the avenger of blood in hot anger pursue the manslayer and overtake him, because the way is long, and strike him fatally, though the man did not deserve to die, since he had not hated his neighbor in the past"* (Deuteronomy 19:6). The Hebrew is literally "while his heart is hot". The law does not deny the grief. It puts a distance between the heat and the act, because the heat will not tell the innocent from the guilty.'),
 ('before_line', '**Connections:** with feeling (10.1), since strife',
  '''## Friends, company and care

Job pictures friends who fail as a dry stream: *"My brothers are treacherous as a torrent-bed, as torrential streams that pass away, which are dark with ice, and where the snow hides itself. When they melt, they disappear; when it is hot, they vanish from their place"* (Job 6:15–17). Caravans turn aside to them and perish (6:18). A wadi runs full in the cold, when no one needs it, and is dry in the heat, when the travellers come. I read friends who are there when they are not needed and gone when they are.

Against it the Preacher sets company: *"Two are better than one … For if they fall, one will lift up his fellow. But woe to him who is alone when he falls and has not another to lift him up! Again, if two lie together, they keep warm, but how can one keep warm alone?"* (Ecclesiastes 4:9–11).

Care for another's body is something Job swears to before God: *"if I have seen anyone perish for lack of clothing, or the needy without covering, if his body has not blessed me, and if he was not warmed with the fleece of my sheep"* (Job 31:19–20). The body that was warmed is pictured as blessing the one who warmed it.

Two ways of rousing oneself toward another stand in the same book. *"The upright are appalled at this, and the innocent stirs himself up against the godless. Yet the righteous holds to his way"* (Job 17:8–9). But in his oath Job disowns the other: *"If I have rejoiced at the ruin of him who hated me, or exulted when evil overtook him"* (31:29), *"I have not let my mouth sin by asking for his life with a curse"* (31:30). It is the same act of rousing oneself, approved in one place and refused in the other. The difference is what it is aimed at: wrong itself, or a person's ruin. Proverbs puts the two powers between people in one line: *"Hatred stirs up strife, but love covers all offenses"* (Proverbs 10:12). Hatred stirs things up to the surface. Love lays something over them.

Love between two people has its own time in the Song: *"that you not stir up or awaken love until it pleases"* (Song of Songs 2:7; 10.6).
'''),
],
'10-12-': [
 ('replace', '"the people feared the Lord, and they believed in the Lord" (Exodus 14:10, 31).',
  '"the people feared the Lord, and they believed in the Lord" (Exodus 14:10, 31). In between, fear spoke as a preference: "it would have been better for us to serve the Egyptians than to die in the wilderness" (14:12; 10.6, *Shaped by fear*).'),
],
'10-09-': [
 ('append_line', 'then I discerned their end" (Psalm 73:16–17).',
  ' What he had been thinking about was envy: "For I was envious of the arrogant when I saw the prosperity of the wicked" (73:3). In the sanctuary he sees it as "a dream when one awakes" (73:20; 10.6, *Jealousy and envy*).'),
 ('replace', 'In Psalms 7, 35, 44 and 59 the call comes where the psalmist\'s life is sought or taken, and Psalm 80 asks, "give us life" (80:18). ', ''),
 ('after_line', 'he who keeps Israel will neither slumber nor sleep',
  '''Read one by one, the calls rest on different grounds:
- innocence, sworn: "if I have repaid my friend with evil … Arise, O Lord, in your anger … awake for me" (Psalm 7:4–6)
- a cause: "Awake and rouse yourself for my vindication, for my cause, my God and my Lord!" (35:23)
- suffering for his sake: "Yet for your sake we are killed all the day long … Awake!" (44:22–23)
- no fault: "for no fault of mine, they run and make ready. Awake, come to meet me, and see!" (59:4)
- his office: "Give ear, O Shepherd of Israel … stir up your might and come to save us!" (80:1–2), with "give us life" (80:18)
- his past: "Awake, awake, put on strength, O arm of the Lord; awake, as in days of old … Was it not you who dried up the sea" (Isaiah 51:9–10)

Bildad makes it a condition instead: "if you are pure and upright, surely then he will rouse himself for you" (Job 8:6). It is a friend's claim, and the book does not leave his counsel standing (42:7).

In Isaiah the call is answered with the same words turned round. The people say, "Awake, awake, put on strength, O arm of the Lord" (51:9). God says, "Wake yourself, wake yourself, stand up, O Jerusalem, you who have drunk from the hand of the Lord the cup of his wrath" (51:17), and "Awake, awake, put on your strength, O Zion" (52:1). I read the call for God to wake answered by God calling his people to wake. The repeated words are Isaiah's; the reading is mine. The same people cannot rouse themselves: "There is no one who calls upon your name, who rouses himself to take hold of you; for you have hidden your face from us" (64:7; 10.13). The next verse still appeals: "But now, O Lord, you are our Father; we are the clay, and you are our potter" (64:8).

A person can also call himself awake. "My soul was bowed down … My heart is steadfast, O God, my heart is steadfast! I will sing and make melody! Awake, my glory! Awake, O harp and lyre! I will awake the dawn!" (Psalm 57:6–8). The self calls itself up from a bowed soul, through a steadfast heart, and gets ahead of the day. Deborah is called by others: "Awake, awake, Deborah! Awake, awake, break out in a song!" (Judges 5:12). One is roused from inside and one from outside, and both to song.'''),
 ('before_line', '## Calling on God to wake',
  '''## Waiting, and pleading

The soul can speak its hope to itself: "'The Lord is my portion,' says my soul, 'therefore I will hope in him.' The Lord is good to those who wait for him, to the soul who seeks him. It is good that one should wait quietly for the salvation of the Lord" (Lamentations 3:24–26). "Portion" is the word of Psalm 16:5 (10.6). Twice "good" belongs to waiting: the Lord is good to those who wait, and it is good to wait. I read waiting as the place where the soul's hope is put.

A plea can bring one's own record. Hezekiah, told he would die, "turned his face to the wall and prayed": "Please, O Lord, remember how I have walked before you in faithfulness and with a whole heart, and have done what is good in your sight." And he wept bitterly (Isaiah 38:2–3; 2 Kings 20:2–3). The answer came: "I have heard your prayer; I have seen your tears. Behold, I will add fifteen years to your life" (Isaiah 38:5). He brought his record. God named his prayer and his tears. I note what the answer names and go no further. Chapter 2 ("Life asked for") has what he wrote afterwards.
'''),
],
'06-': [
 ('replace', 'The returning exiles were "everyone whose spirit God had stirred" (Ezra 1:5).',
  'The returning exiles were "everyone whose spirit God had stirred" (Ezra 1:5). Not everyone went; the stirred ones rose. Haggai shows what came before the stirring. The people "obeyed the voice of the Lord … And the people feared the Lord", and they were told "I am with you". Then "the Lord stirred up the spirit of Zerubbabel … and the spirit of all the remnant of the people. And they came and worked on the house" (Haggai 1:12–14). The same chapter had them sowing much and harvesting little, clothed and not warm (1:6; 10.6). The spirit is stirred toward destroying too: "the God of Israel stirred up the spirit of Pul king of Assyria" after his people "broke faith" (1 Chronicles 5:25–26), and "the spirit of the kings of the Medes" against Babylon (Jeremiah 51:11). 13.1 (*Stirring*) gathers what the verses say of God in this.'),
],
'04-': [
 ('after_line', 'a man of understanding will draw it out" (Proverbs 20:5).',
  '- The heart can be awake when the body is not, and still not move it: "I slept, but my heart was awake. A sound! My beloved is knocking" (Song of Songs 5:2). She delayed for her comfort, "I had put off my garment; how could I put it on?" (5:3), though "my heart was thrilled within me" (5:4). When she opened, "my beloved had turned and gone" (5:6; 10.6).'),
 ('after_line', 'The heart carries the widest range of feeling',
  'The heart can grow hot with what is held in. "I said, \'I will guard my ways, that I may not sin with my tongue\' … I was mute and silent; I held my peace to no avail, and my distress grew worse. My heart became hot within me. As I mused, the fire burned; then I spoke with my tongue" (Psalm 39:1–3). What came out was a prayer: "O Lord, make me know my end" (39:4; 10.5).'),
 ('after_line', 'The heart is the place into which things are put.',
  'What is bound on it speaks back. "Bind them on your heart always … When you walk, they will lead you; when you lie down, they will watch over you; and when you awake, they will talk with you" (Proverbs 6:21–22). The teaching put into the heart becomes a voice that goes with a person, lies down with him, and is there when he wakes.'),
 ('replace', 'It can be like an oven (Hosea 7:6)',
  'It can be like an oven (Hosea 7:6), and the next verse says where the heat goes: "All of them are hot as an oven, and they devour their rulers … and none of them calls upon me" (7:7)'),
],
'10-05-': [
 ('after_line', 'There can be a pause between thought and word',
  'A silence can also be held too long. "I was mute and silent; I held my peace to no avail, and my distress grew worse. My heart became hot within me. As I mused, the fire burned; then I spoke with my tongue" (Psalm 39:2–3). He had kept silent so as not to sin with his tongue while the wicked were present (39:1). The silence did not end the distress; it heated it. When the words came, they were turned to God: "O Lord, make me know my end and what is the measure of my days" (39:4). The heat did not come out as the sin he had feared.'),
],
'10-02-': [
 ('after_line', 'What is known is also kept and returned to.',
  '''Hearing can be woken. "The Lord God has given me the tongue of those who are taught, that I may know how to sustain with a word him who is weary. Morning by morning he awakens; he awakens my ear to hear as those who are taught. The Lord God has opened my ear, and I was not rebellious; I turned not backward" (Isaiah 50:4–5). The order is the verses' own: the ear is woken before the tongue sustains anyone, and it is woken each morning. The next verse goes on to "I gave my back to those who strike" (50:6), so the woken ear is no shelter from suffering. An angel wakes a prophet too, and the first thing said is "What do you see?" (Zechariah 4:1–2; 13.2).

What is known can be known in heart and soul. Joshua, near death: "you know in your hearts and souls, all of you, that not one word has failed of all the good things that the Lord your God promised concerning you. All have come to pass for you; not one of them has failed" (Joshua 23:14). This is knowing from experience. He turns it into a warning straight away: "But just as all the good things that the Lord your God promised concerning you have been fulfilled for you, so the Lord will bring upon you all the evil things" (23:15). The faithfulness they know from the good is the same faithfulness that stands behind the warnings.'''),
],
'10-08-': [
 ('after_line', 'Fear leads into wrong, and Scripture says so',
  'Pressure can lead into wrong as well. "For the scepter of wickedness shall not rest on the land allotted to the righteous, lest the righteous stretch out their hands to do wrong" (Psalm 125:3). Wicked rule left in place could push even the righteous to it. The next verse is a prayer: "Do good, O Lord, to those who are good, and to those who are upright in their hearts!" (125:4).'),
],
'11-': [
 ('before_line', '- **The story around it.** A single verse',
  '''- **Before whom it is said, and what it rests on.** "Eat, drink, be merry" is folly in the rich man who says it to his own soul over goods laid up (Luke 12:19–20), and it is commended by the Preacher as "his lot" in "the few days of his life that God has given him" (Ecclesiastes 5:18; 8:15). The words are nearly the same (10.6).
- **Whose jealousy, and for whom.** Jealousy is God's for his people against those who scorned them (Ezekiel 36:5), and over his people's own spirit, met with grace (James 4:5–6). It is Elijah's for God (1 Kings 19:10), Joshua's for Moses, refused by Moses (Numbers 11:29), a husband's that will take no compensation (Proverbs 6:34–35), and envy of the wicked that embitters the soul (Psalm 73:3, 21). The word stays the same. What differs is whose it is, whom it is for, and whether it wants God's gift kept narrow (10.6; 13.1).
- **What it is aimed at.** Job rouses himself against the godless and is upright in it (Job 17:8). He disowns rousing himself at an enemy's ruin (31:29). It is the same act of rousing oneself (10.10).
- **When the cost appears.** The nearer redeemer was willing for the land and unwilling when Ruth came with it (Ruth 4:4–6). The will turned when his own inheritance was touched (10.7).
- **Whom the need is spoken to.** The same thirst accuses Moses at Rephidim (Exodus 17:3) and asks God at Lehi (Judges 15:18) (10.6).'''),
 ('append_line', '- **Who rouses, and toward what.**',
  ' Haggai gives the order on the building side: obedience, the fear of the Lord, "I am with you", then the stirring, then the work (Haggai 1:12–14; 13.1, *Stirring*).'),
 ('after_line', 'A person can speak to their own soul, in at least five settings',
  'Three more voices belong here. The soul says its own hope: "\'The Lord is my portion,\' says my soul, \'therefore I will hope in him\'" (Lamentations 3:24). A person calls himself awake: "Awake, my glory!" (Psalm 57:8). And teaching bound on the heart speaks when a person wakes: "when you awake, they will talk with you" (Proverbs 6:22).'),
],
'12-': [
 ('after_line', 'It also starts in the power to imagine and design.',
  'Isaiah shows the man who makes one: "He takes a part of it and warms himself; he kindles a fire and bakes bread. Also he makes a god and worships it" (Isaiah 44:15). "Also he warms himself and says, \'Aha, I am warm, I have seen the fire!\' And the rest of it he makes into a god, his idol, and falls down to it and worships it" (44:16–17). The same log gives him comfort and a god. The prophet says what is inside: "No one considers, nor is there knowledge or discernment" (44:19); "a deluded heart has led him astray, and he cannot deliver himself or say, \'Is there not a lie in my right hand?\'" (44:20). A body satisfied and a heart deceived stand in one man. He is pleased with the warmth and does not see what he has done with the rest. Babylon\'s counsellors are the same kind of fire: "No coal for warming oneself is this, no fire to sit before!" (47:14).'),
],
'02-': [
 ('after_line', 'The life asked for is for something.',
  'Hezekiah asked for his own life with his record and his tears: "Please, O Lord, remember how I have walked before you in faithfulness and with a whole heart, and have done what is good in your sight" (Isaiah 38:3). The answer named the prayer and the tears, and gave fifteen years (38:5; 10.9).'),
 ('after_line', 'Life can be loathed. "I loathe my life',
  'The want for life is a want to see good: "What man is there who desires life and loves many days, that he may see good?" (Psalm 34:12). Job uses the same words for its loss: "my eye will never again see good" (Job 7:7). Where the hope of seeing good has gone, life is weighed as a breath (10.6, *Wanting life*).'),
 ('after_line', '- The Preacher: "I thought the dead',
  '\nAt the sea, fear set slavery against death and preferred slavery: "it would have been better for us to serve the Egyptians than to die in the wilderness" (Exodus 14:12; 10.6, 10.12).'),
 ('after_line', '- "In the path of righteousness is life, and in its pathway there is no death" (Proverbs 12:28)',
  '- Wisdom: "For whoever finds me finds life and obtains favor from the Lord, but he who fails to find me injures himself; all who hate me love death" (Proverbs 8:35–36). To hate wisdom is to love death, a love the person does not know he has.'),
],
}


def current(prefix):
    files = [f for f in glob.glob(os.path.join(NARR, prefix + '*.md'))]
    assert len(files) == 1, (prefix, files)
    return files[0]


def apply(text, mode, anchor, ins):
    lines = text.split('\n')
    idx = [i for i, l in enumerate(lines) if anchor in l]
    if mode == 'replace':
        assert text.count(anchor) == 1, ('replace count', anchor[:60], text.count(anchor))
        return text.replace(anchor, ins)
    assert len(idx) == 1, (mode, anchor[:60], idx)
    i = idx[0]
    if mode == 'append_line':
        lines[i] = lines[i] + ins
    elif mode == 'after_line':
        lines[i + 1:i + 1] = ['', ins] if lines[i].strip() and not lines[i].startswith('- ') else [ins]
        if lines[i].startswith('- ') and not ins.startswith('- '):
            lines[i + 1:i + 2] = ['', ins]
    elif mode == 'before_line':
        lines[i:i] = [ins, ''] if not ins.endswith('\n') else [ins.rstrip('\n'), '']
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
