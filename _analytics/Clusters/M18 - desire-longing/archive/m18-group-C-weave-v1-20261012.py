"""Weave of M18 group C (will, willing, acceptance) (#1993, item F), 2026-10-12.

Researcher (chat 2026-10-12, verbatim): "continue with batches 2 and 3, then weave all".
Sources: m18-group-C-reading-batch1-v1-20261012.md and m18-group-C-reading-batch2-3-v1-20261012.md (with the 14 verses
whose act carries no M-code, read by their acts). Each verse is placed by its main operation (rule 73, guide
Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md).

Same mechanics and quote check as m18-group-B-remaining-weave-v1-20261011.py.
Run with --dry to check only; without it, it writes only if the check passes.
"""
import glob, importlib.util, os, re, shutil, sqlite3, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NARR = os.path.abspath(os.path.join(HERE, '..', '..', 'essay', 'spirit_soul_body', 'inner-being-narrative'))
DB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
spec = importlib.util.spec_from_file_location('xr', os.path.join(HERE, '..', 'M64 - will-resolve', 'verse-narrative-ot-crossref-v3-20261009.py'))
xr = importlib.util.module_from_spec(spec); spec.loader.exec_module(xr)
DATE = '20261012'
NL = '\n'


def current(prefix):
    files = glob.glob(os.path.join(NARR, prefix + '*.md'))
    assert len(files) == 1, (prefix, files)
    return files[0]


R7 = '''**A will that cannot carry itself out.** Paul speaks of a will that is real and wants the good, and does not carry itself out. "For I do not understand my own actions. For I do not do what I want, but I do the very thing I hate. Now if I do what I do not want, I agree with the law, that it is good. So now it is no longer I who do it, but sin that dwells within me" (Romans 7:15–17). "For I have the desire to do what is right, but not the ability to carry it out. For I do not do the good I want, but the evil I do not want is what I keep on doing" (7:18–19). "So I find it to be a law that when I want to do right, evil lies close at hand" (7:21). He does not deny the will. He wants the good, he hates what he does, and his wanting agrees with the law. What does the opposite he calls "no longer I". I read the will here as a true inner act that is not master in its own house. The delight and the war in the members are in 10.1 (7:22–23), the cry in Chapter 2 (7:24), and the divided service in Chapter 7 (7:25).'''

D1 = '''**Doing the will of God.** The verses speak of God's will as something a person prays, knows, does, or fails to do.
- **Prayed.** "Your kingdom come, your will be done, on earth as it is in heaven" (Matthew 6:10). At Gethsemane, the second time: "My Father, if this cannot pass unless I drink it, your will be done" (26:42), after "The spirit indeed is willing, but the flesh is weak" (26:41). The words he taught are the words he prays.
- **Asked within.** "if we ask anything according to his will he hears us" (1 John 5:14). And: "If you abide in me, and my words abide in you, ask whatever you wish, and it will be done for you" (John 15:7). I read the two together: the asking is free where the asker's will has been shaped by his words.
- **Known by willing it.** "If anyone's will is to do God's will, he will know whether the teaching is from God" (John 7:17). The willing comes before the knowing. Paul was "appointed … to know his will" (Acts 22:14), and was asked at once, "And now why do you wait?" (22:16). "Do not be foolish, but understand what the will of the Lord is" (Ephesians 5:17).
- **Known and not done.** "you … know his will and approve what is excellent" (Romans 2:18) is said to one who boasts in God and teaches others (2:17, 19–21). "And that servant who knew his master's will but did not get ready or act according to his will, will receive a severe beating" (Luke 12:47), more than the one who did not know (12:48).
- **Said, and not done.** "Not everyone who says to me, 'Lord, Lord,' will enter the kingdom of heaven, but the one who does the will of my Father who is in heaven" (Matthew 7:21). Of two sons, one said "I will not, but afterward he changed his mind and went", the other "I will, sir, but did not go". "Which of the two did the will of his father?" (21:29–31). Jesus turns the changed mind toward belief: "you did not afterward change your minds and believe him" (21:32).
- **What it is, where the verses say.** "give thanks in all circumstances; for this is the will of God in Christ Jesus for you" (1 Thessalonians 5:18). "For this is the will of God, your sanctification: that you abstain from sexual immorality" (4:3), "not in the passion of lust like the Gentiles who do not know God" (4:5). "that by doing good you should put to silence the ignorance of foolish people" (1 Peter 2:15). After confession, "do his will. Separate yourselves" (Ezra 10:11).
- **With suffering, and with endurance.** "For it is better to suffer for doing good, if that should be God's will, than for doing evil" (1 Peter 3:17), and the next verse, "For Christ also suffered" (3:18). "For you have need of endurance, so that when you have done the will of God you may receive what is promised" (Hebrews 10:36).
- **Those who do it.** "For whoever does the will of my Father in heaven is my brother and sister and mother" (Matthew 12:50; Mark 3:35), said with his hand stretched toward his disciples. "if anyone is a worshiper of God and does his will, God listens to him" (John 9:31), said by the man who had been blind.
- **God working it in them.** "equip you with everything good that you may do his will, working in us that which is pleasing in his sight" (Hebrews 13:21). God "works in you, both to will and to work" (Philippians 2:13; 10.12). The renewed mind discerns "what is the will of God" (Romans 12:2; Chapter 14). Angels do it too (13.2).'''

ASKED = '''**The will asked for.** Jesus asks people what they want.
- To blind men who had cried out against the crowd's rebuke: "What do you want me to do for you?" "Lord, let our eyes be opened." And "Jesus in pity touched their eyes" (Matthew 20:32–34). To Bartimaeus, the same question, and "your faith has made you well" (Mark 10:51–52).
- To a man ill for thirty-eight years: "Do you want to be healed?" He answers with what he lacks: "Sir, I have no one to put me into the pool" (John 5:6–7). He is healed without the pool (5:8).
- To James and John, who came saying "we want you to do for us whatever we ask of you": "What do you want me to do for you?" They asked for the places of honour, and he answered, "You do not know what you are asking. Are you able to drink the cup that I drink?" (Mark 10:35–38; Matthew 20:21–22).
- To the twelve, when many turned back: "Do you want to go away as well?" "Lord, to whom shall we go? You have the words of eternal life" (John 6:67–68).
The same question is answered with sight, with a lack, with ambition and with staying. I read the question as drawing the will out into words, where it can be met.'''

REDIRECT = '''**A will redirected.** Jesus takes the will to be first and the will to follow, and turns them.
- The disciples "had argued with one another about who was the greatest". "If anyone would be first, he must be last of all and servant of all" (Mark 9:34–35). "whoever would be first among you must be slave of all. For even the Son of Man came not to be served but to serve" (Mark 10:44–45; Matthew 20:27–28).
- After Peter was told "you are not setting your mind on the things of God": "If anyone would come after me, let him deny himself and take up his cross and follow me. For whoever would save his life will lose it" (Matthew 16:23–25; Mark 8:34–35; Luke 9:23–24, "daily").
The will is not removed. Its aim is named, wanting to be first, wanting to save one's life, and it is given another way to that end.'''

BACK = '''**Wanting to go back.** "But now that you have come to know God, or rather to be known by God, how can you turn back again to the weak and worthless elementary principles of the world, whose slaves you want to be once more?" (Galatians 4:9). "Tell me, you who desire to be under the law, do you not listen to the law?" (4:21). Paul is "afraid I may have labored over you in vain" (4:11). After the defeat at Ai, when "the hearts of the people melted", Joshua said, "Would that we had been content to dwell beyond the Jordan!" (Joshua 7:5, 7). In a figure: "no one after drinking old wine desires new, for he says, 'The old is good'" (Luke 5:39). I read the will turning back toward what it knew, even toward slavery, when the new has cost something.

**Content to stay.** "Moses was content to dwell with the man" (Exodus 2:21), and he named his son for being "a sojourner in a foreign land" (2:22). "the Levite was content to dwell with the man", and Micah said, "Now I know that the Lord will prosper me, because I have a Levite as priest" (Judges 17:11, 13). The same willingness to stay sits in two very different settings, and the verses say what each led to.'''

HEROD = '''**A will bound by an oath before guests.** Herod "feared John, knowing that he was a righteous and holy man … When he heard him, he was greatly perplexed, and yet he heard him gladly" (Mark 6:20). At his banquet he said to the girl, "Ask me for whatever you wish, and I will give it to you" (6:22). Her mother chose for her, and she asked "with haste": "I want you to give me at once the head of John the Baptist on a platter" (6:24–25). "And the king was exceedingly sorry, but because of his oaths and his guests he did not want to break his word to her" (6:26). His grief and his will pulled two ways, and the oath and the watching guests decided it.'''

OPS = {
'10-07-': [
 ('before_line', '**A will under another.**', R7),
 ('before_line', '## Life and death set before a person', D1),
 ('before_line', '**The will meets something put before it.**', ASKED),
 ('before_line', '**The will meets something put before it.**', REDIRECT),
 ('after_line', '- a feast: the older brother',
  '- a wedding feast: "they would not come", and again, "they paid no attention and went off, one to his farm, another to his business" (Matthew 22:3, 5)'),
 ('after_line', '- a wedding feast:',
  '- a plea for patience: "Have patience with me, and I will pay you." "He refused and went and put him in prison" (Matthew 18:29–30), he who had been forgiven all his debt (18:32)'),
 ('after_line', '- a plea for patience:',
  '- a reign: "his citizens hated him and sent a delegation after him, saying, \'We do not want this man to reign over us\'" (Luke 19:14)'),
 ('after_line', '- a reign:',
  '- a threat: "He would not go about in Judea, because the Jews were seeking to kill him" (John 7:1), and his brothers urged him to go (7:3)'),
 ('after_line', '- a threat:',
  '- an urging between friends: "I strongly urged him to visit you … but it was not at all his will to come now. He will come when he has opportunity" (1 Corinthians 16:12)'),
 ('after_line', '- Against that stands Amnon',
  '- At the cross Jesus was offered "wine to drink, mixed with gall, but when he tasted it, he would not drink it" (Matthew 27:34).'),
 ('after_line', '- Against that stands Amnon',
  '- Those who lay burdens on others "are not willing to move them with their finger" (Matthew 23:4), for "they preach, but do not practice" (23:3).'),
 ('after_line', '- life itself, from the one',
  '- being gathered: "How often would I have gathered your children together as a hen gathers her brood under her wings, and you were not willing!" (Matthew 23:37; Luke 13:34). His will and theirs stand in one verb (13.1).'),
 ('after_line', '- being gathered:',
  '- a light received only for a while: "He was a burning and shining lamp, and you were willing to rejoice for a while in his light" (John 5:35)'),
 ('after_line', '- Others can hold it back',
  '- It can be held back by the owner of the field. "Then do you want us to go and gather them?" "No, lest in gathering the weeds you root up the wheat along with them" (Matthew 13:28–29).'),
 ('after_line', '- It can bend to a crowd.',
  '- It can try, and give way. Pilate asked, "Whom do you want me to release for you: Barabbas, or Jesus who is called Christ? For he knew that it was out of envy that they had delivered him up" (Matthew 27:17–18). He spoke again, "desiring to release Jesus" (Luke 23:20), and asked, "Why? What evil has he done?" (Matthew 27:23). "And their voices prevailed" (Luke 23:23). "he delivered Jesus over to their will" (23:25).'),
 ('after_line', '- It can try, and give way.',
  '- It can bend to please. Felix, "desiring to do the Jews a favor, … left Paul in prison" (Acts 24:27), after hoping "that money would be given him by Paul" (24:26). Festus, "wishing to do the Jews a favor", asked Paul to be tried in Jerusalem, and Paul appealed to Caesar (25:9–11).'),
 ('before_line', '**A resolve is still being weighed.**', HEROD),
 ('after_line', '**The will turned toward harm.**',
  '''The will to harm can be stopped short. "Get away from here, for Herod wants to kill you." Jesus answered, "Go and tell that fox … I must go on my way today and tomorrow and the day following" (Luke 13:31–33). "Some of them wanted to arrest him, but no one laid hands on him", and the officers said, "No one ever spoke like this man!" (John 7:44–46). A man wronging his neighbour turned the will on Moses: "Do you want to kill me as you killed the Egyptian yesterday?" (Acts 7:28), and Moses fled (7:29). A people can be set on what ruins it: "Ephraim is oppressed, crushed in judgment, because he was determined to go after filth" (Hosea 5:11).'''),
 ('before_line', '**Feeling holds the will.**', BACK),
 ('after_line', 'So the willing heart is said both',
  '''The verses on freely offering say more about where it comes from.
- **Asked for, then given.** "Who then will offer willingly, consecrating himself today to the Lord?" (1 Chronicles 29:5). "Then the leaders of fathers' houses made their freewill offerings" (29:6). David prays over it: "But who am I, and what is my people, that we should be able thus to offer willingly? For all things come from you, and of your own have we given you" (29:14), and "all this abundance … comes from your hand and is all your own" (29:16).
- **Stirred, and helped by others.** "everyone whose spirit God had stirred to go up to rebuild", and those about them "aided them … besides all that was freely offered" (Ezra 1:5–6). Some "made freewill offerings for the house of God … according to their ability" (2:68–69).
- **Even from a foreign king.** "the silver and gold that the king and his counselors have freely offered to the God of Israel", with "the freewill offerings of the people and the priests, vowed willingly" (Ezra 7:15–16). The same decree lets "anyone … who freely offers to go to Jerusalem" go (7:13).
- **Offering oneself.** "That the leaders took the lead in Israel, that the people offered themselves willingly, bless the Lord!" (Judges 5:2). "a volunteer for the service of the Lord" (2 Chronicles 17:16). After lots were cast for who would live in Jerusalem, "the people blessed all the men who willingly offered to live in Jerusalem" (Nehemiah 11:1–2).
- **Readiness, and what it is measured by.** "a year ago started not only to do this work but also to desire to do it. So now finish doing it as well, so that your readiness in desiring it may be matched by your completing it out of what you have. For if the readiness is there, it is acceptable according to what a person has, not according to what he does not have" (2 Corinthians 8:10–12). The gift is carried "to show our good will" (8:19).
I read the willing offering as answered by gladness and blessing in these verses, and measured by what a person has, not by its size.'''),
 ('after_line', 'Daniel sees it again',
  '''The will made absolute is seen from below as well. "a mighty king shall arise, who shall rule with great dominion and do as he wills. And as soon as he has arisen, his kingdom shall be broken" (Daniel 11:3–4). Another "shall do as he wills, and none shall stand before him" (11:16), until "a commander shall put an end to his insolence" (11:18). Under such rulers a people says, "They rule over our bodies and over our livestock as they please, and we are in great distress" (Nehemiah 9:37), and says it of kings set over them "because of our sins" (Nehemiah 9:37). The same prayer remembers the land given "that they might do with them as they would" (9:24), and what followed: "they ate and were filled … Nevertheless, they were disobedient" (9:25–26). Of Elijah: "they did not recognize him, but did to him whatever they pleased. So also the Son of Man will certainly suffer at their hands" (Matthew 17:12).'''),
 ('replace', 'A builder who lays a foundation and cannot finish is mocked:',
  '"For which of you, desiring to build a tower, does not first sit down and count the cost, whether he has enough to complete it?" (Luke 14:28). A builder who lays a foundation and cannot finish is mocked:'),
 ('after_line', 'Paul plans the same way, and says so.',
  '''Paul's own plans are said under God's will, again and again, and his wanting stays strong inside them.
- At parting: "I will return to you if God wills" (Acts 18:21), after he "declined" to stay longer (18:20).
- With purpose: "I will come to you soon, if the Lord wills, and I will find out not the talk of these arrogant people but their power" (1 Corinthians 4:19). He then asks their will: "What do you wish? Shall I come to you with a rod, or with love?" (4:21).
- With his own wish: "I do not want to see you now just in passing. I hope to spend some time with you, if the Lord permits" (16:7).
- In prayer: "asking that somehow by God's will I may now at last succeed in coming to you. For I long to see you" (Romans 1:10–11); "so that by God's will I may come to you with joy" (15:32).
- Hindered: "we wanted to come to you, I, Paul, again and again, but Satan hindered us" (1 Thessalonians 2:18), after "with great desire to see you face to face" (2:17).
- Yielded by others: "since he would not be persuaded, we ceased and said, 'Let the will of the Lord be done'" (Acts 21:14), after "What are you doing, weeping and breaking my heart?" (21:13).
- A wish set beside a gift: "I wish that all were as I myself am. But each has his own gift from God" (1 Corinthians 7:7).
The verses keep apart Paul's wanting, God's will, and what hinders, named once as Satan. I read the plan as held open toward God without the wanting being given up.'''),
 ('after_line', '- **Filled with one\'s own ways.**',
  '- **Too late.** Esau "sold his birthright for a single meal. For you know that afterward, when he desired to inherit the blessing, he was rejected, for he found no chance to repent, though he sought it with tears" (Hebrews 12:16–17).'),
],
'10-06-': [
 ('after_line', 'Two hungers wait at a gate.',
  'After death the same rich man is told that wanting cannot cross: "between us and you a great chasm has been fixed, in order that those who would pass from here to you may not be able, and none may cross from there to us" (Luke 16:26).'),
 ('after_line', 'Wanting can reach past this life.',
  'Job wanted death from God\'s hand: "Oh that I might have my request, and that God would fulfill my hope, that it would please God to crush me, that he would let loose his hand and cut me off! This would be my comfort; I would even exult in pain unsparing, for I have not denied the words of the Holy One" (Job 6:8–10). He holds to one thing while he asks it, that he has not denied the words.'),
 ('after_line', '## Aimed at God',
  'Wanting can be aimed at seeing Jesus, and the verses show it ending in different places. Greeks "came to Philip … and asked him, \'Sir, we wish to see Jesus\'", and Jesus answered, "The hour has come for the Son of Man to be glorified" (John 12:21, 23). Herod "was very glad, for he had long desired to see him, because he had heard about him, and he was hoping to see some sign", and "he made no answer" (Luke 23:8–9). His mother and brothers stood outside "desiring to see you", and he said, "My mother and my brothers are those who hear the word of God and do it" (8:20–21).'),
],
'10-09-': [
 ('after_line', '### How God meets those who fear him',
  '"He fulfills the desire of those who fear him; he also hears their cry and saves them" (Psalm 145:19), beside "The Lord is near to all who call on him, to all who call on him in truth" (145:18).'),
 ('after_line', 'A plea can end in asking that one',
  'A plea can be put to his will alone. "Lord, if you will, you can make me clean" (Matthew 8:2). The man does not doubt the power. He asks the will, and the will answers: "I will; be clean" (8:3; Mark 1:40–41; 13.1).'),
],
'10-10-': [
 ('before_line', '## Friends, company and care',
  '''Another person's will to take can be met by giving. "And if anyone would sue you and take your tunic, let him have your cloak as well … Give to the one who begs from you, and do not refuse the one who would borrow from you" (Matthew 5:40–42). One's own wish is made the measure of what is done to others: "So whatever you wish that others would do to you, do also to them, for this is the Law and the Prophets" (Matthew 7:12; Luke 6:31). I read the wish here as turned outward: what a person wants for himself becomes the measure of what he does for another.'''),
 ('after_line', '### Reverence for people',
  'Honour can be pressed on people until it becomes worship. "the priest of Zeus … brought oxen and garlands to the gates and wanted to offer sacrifice with the crowds." Barnabas and Paul "tore their garments": "Men, why are you doing these things? We also are men, of like nature with you" (Acts 14:13–15).'),
 ('after_line', '## Anger between people',
  'A wish to destroy can rise when a person is not received. When a Samaritan village "did not receive him", James and John said, "Lord, do you want us to tell fire to come down from heaven and consume them?" "But he turned and rebuked them. And they went on to another village" (Luke 9:53–56).'),
 ('after_line', '## Friends, company and care',
  'A friend in pain asks to be looked at. "But now, be pleased to look at me, for I will not lie to your face. Please turn; let no injustice be done. Turn now; my vindication is at stake" (Job 6:28–29).'),
],
'10-11-': [
 ('before_line', '### Hiding another',
  'Jesus himself sought to be hidden at times, and could not be. "he entered a house and did not want anyone to know, yet he could not be hidden. But immediately a woman … heard of him and came and fell down at his feet" (Mark 7:24–25). Again, "he did not want anyone to know, for he was teaching his disciples, saying to them, \'The Son of Man is going to be delivered into the hands of men\'" (9:30–31).'),
],
'10-12-': [
 ('after_line', 'Sometimes a hand comes with the word.',
  'On the sea the word came first. "He meant to pass by them, but when they saw him walking on the sea they thought it was a ghost, and cried out … But immediately he spoke to them and said, \'Take heart; it is I. Do not be afraid\'" (Mark 6:48–50). Once he had said it, "they were glad to take him into the boat" (John 6:21).'),
],
'10-05-': [
 ('after_line', 'Mockery can begin without words.',
  'At the cross the psalm\'s words were spoken: "He trusts in God; let God deliver him now, if he desires him. For he said, \'I am the Son of God\'" (Matthew 27:43).'),
 ('before_line', '## Speech before words',
  'Speech can run ahead of understanding. Some, "by swerving from" love "from a pure heart and a good conscience and a sincere faith", have "wandered away into vain discussion, desiring to be teachers of the law, without understanding either what they are saying or the things about which they make confident assertions" (1 Timothy 1:5–7).'),
],
'10-02-': [
 ('before_line', '## Perplexity',
  '''Receiving a word can wait on being willing. "and if you are willing to accept it, he is Elijah who is to come. He who has ears to hear, let him hear" (Matthew 11:14–15). The Bereans "received the word with all eagerness, examining the Scriptures daily to see if these things were so. Many of them therefore believed" (Acts 17:11–12). Paul calls a saying "trustworthy and deserving of full acceptance, that Christ Jesus came into the world to save sinners, of whom I am the foremost" (1 Timothy 1:15). The other way is also named: scoffers "following their own sinful desires … deliberately overlook this fact" (2 Peter 3:3, 5). I read the willing, or the unwilling, as standing before the hearing in these verses.'''),
],
'13-01-': [
 ('before_line', '## Purposing',
  '"he went up on the mountain and called to him those whom he desired, and they came to him. And he appointed twelve … so that they might be with him" (Mark 3:13–14). The calling follows his desire, and the purpose is that they be with him.'),
 ('before_line', '**At Gethsemane the Son\'s will',
  '''**The Son's will, in its own words.**
- **"I will; be clean."** To the leper who said "If you will, you can make me clean", Jesus, "moved with pity, … stretched out his hand and touched him and said to him, 'I will; be clean'" (Mark 1:40–41; Matthew 8:2–3; Luke 5:12–13). His will and his pity are named together, and his hand touches before he speaks.
- **A gathering refused.** "O Jerusalem, Jerusalem, the city that kills the prophets and stones those who are sent to it! How often would I have gathered your children together as a hen gathers her brood under her wings, and you were not willing!" (Matthew 23:37; Luke 13:34). Then: "your house is left to you desolate", and the door left open, "until you say, 'Blessed is he who comes in the name of the Lord'" (23:38–39).
- **A longing joined with distress.** "I came to cast fire on the earth, and would that it were already kindled! I have a baptism to be baptized with, and how great is my distress until it is accomplished!" (Luke 12:49–50).
- **For those given him.** "Father, I desire that they also, whom you have given me, may be with me where I am, to see my glory that you have given me because you loved me before the foundation of the world" (John 17:24).
- **In a parable, the owner's will against the begrudging eye.** "I choose to give to this last worker as I give to you. Am I not allowed to do what I choose with what belongs to me? Or do you begrudge my generosity?" (Matthew 20:14–15). *Do you begrudge* is literally *is your eye evil*, the opposite of the good eye that shares its bread (Proverbs 22:9; 10.6).'''),
 ('before_line', '**At Gethsemane the Son\'s will',
  '''**The Father's will, said of creation and of people.** "for you created all things, and by your will they existed and were created" (Revelation 4:11). "God arranged the members in the body, each one of them, as he chose" (1 Corinthians 12:18). "God chose to make known how great among the Gentiles are the riches of the glory of this mystery, which is Christ in you, the hope of glory" (Colossians 1:27). Christ "gave himself for our sins … according to the will of our God and Father" (Galatians 1:4). God "desires all people to be saved and to come to the knowledge of the truth" (1 Timothy 2:4). And after the shepherd who rejoices over the one found: "So it is not the will of my Father who is in heaven that one of these little ones should perish" (Matthew 18:14).'''),
 ('after_line', '- "For I desire steadfast love',
  '- Jesus sends his hearers to learn it: "Go and learn what this means: \'I desire mercy, and not sacrifice.\' For I came not to call the righteous, but sinners" (Matthew 9:13); "And if you had known what this means, \'I desire mercy, and not sacrifice,\' you would not have condemned the guiltless" (12:7).'),
 ('before_line', '**Delight at creation.**',
  '''**What makes an offering accepted.** In the law the one who brings is accepted through the offering: "he shall offer a male without blemish … that he may be accepted before the Lord. He shall lay his hand on the head of the burnt offering, and it shall be accepted for him to make atonement for him" (Leviticus 1:3–4); "you shall offer it so that you may be accepted" (19:5; 22:29; 23:11); "to be accepted it must be perfect; there shall be no blemish in it" (22:21). The high priest bears the guilt of the holy gifts "that they may be accepted before the Lord" (Exodus 28:38). In the prophets an offering is refused where the person has turned away: "they have not paid attention to my words; and as for my law, they have rejected it. What use to me is frankincense … Your burnt offerings are not acceptable" (Jeremiah 6:19–20). "You cover the Lord's altar with tears, with weeping and groaning because he no longer regards the offering or accepts it with favor from your hand … Because the Lord was witness between you and the wife of your youth, to whom you have been faithless" (Malachi 2:13–14). "The sacrifice of the wicked is an abomination to the Lord, but the prayer of the upright is acceptable to him" (Proverbs 15:8). I read the acceptance as of the person, through the offering, and the refusal as falling where the person's word or covenant is broken.

**His favor.** "For you bless the righteous, O Lord; you cover him with favor as with a shield" (Psalm 5:12). "by your favor our horn is exalted" (89:17). "A false balance is an abomination to the Lord, but a just weight is his delight" (Proverbs 11:1). "the upright enjoy acceptance" (14:9). "He who finds a wife finds a good thing and obtains favor from the Lord" (18:22). After "you have done all this evil", Samuel says, "the Lord will not forsake his people, for his great name's sake, because it has pleased the Lord to make you a people for himself" (1 Samuel 12:20, 22). His favor has a time: "In a time of favor I have answered you" (Isaiah 49:8); "to proclaim the year of the Lord's favor … to comfort all who mourn" (61:2). And a prayer waits on it: "my prayer is to you, O Lord. At an acceptable time, O God, in the abundance of your steadfast love answer me" (Psalm 69:13).'''),
],
'13-02-': [
 ('before_line', '*Verses are gathered here',
  'Angels do his will and are called to bless him for it. "Bless the Lord, O you his angels, you mighty ones who do his word, obeying the voice of his word! Bless the Lord, all his hosts, his ministers, who do his will!" (Psalm 103:20–21).'),
],
'13-03-': [
 ('before_line', '*Nothing has been placed here yet.',
  '''The devil claims a will over what was given into his hand, and seeks worship with it. "To you I will give all this authority and their glory, for it has been delivered to me, and I give it to whom I will. If you, then, will worship me, it will all be yours." Jesus answered, "You shall worship the Lord your God, and him only shall you serve" (Luke 4:6–8). People can be held by that will: opponents are to be corrected with gentleness, "God may perhaps grant them repentance leading to a knowledge of the truth, and they may come to their senses and escape from the snare of the devil, after being captured by him to do his will" (2 Timothy 2:25–26).'''),
 ('replace', '*Nothing has been placed here yet. Verses are gathered here', '*Verses are gathered here'),
],
'11-patterns': [
 ('after_line', '- **When the cost appears.**',
  '- **Whose will, and whether it can carry itself out.** The same verb, "want", is a will that wants the good and cannot do it (Romans 7:19), a will asked out by Jesus, "What do you want me to do for you?" (Mark 10:51), a will made absolute (Daniel 11:3), a will that gives way to a crowd (Luke 23:25), and a will taken up and turned, "If anyone would be first" (Mark 9:35). Willing God\'s will comes before knowing it (John 7:17) (10.7).'),
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
