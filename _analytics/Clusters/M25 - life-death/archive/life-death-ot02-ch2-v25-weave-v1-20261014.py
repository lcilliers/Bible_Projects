"""OT-02 weave: Ch 2 v24 -> v25 (check v2 section E, approved 2026-10-14: "proceed with the weave as
proposed, include the perish pull").

Every edit is an exact replacement on the v24 text and must match once; the script refuses otherwise.
Usage (repo root): python "_analytics/Clusters/M25 - life-death/life-death-ot02-ch2-v25-weave-v1-20261014.py"
Writes 02-life-breath-and-death-v25-20261014.md beside v24; archiving v24 is a separate step.
"""
import pathlib, sys

D = pathlib.Path('_analytics/essay/spirit_soul_body/inner-being-narrative')
src = D / '02-life-breath-and-death-v24-20261014.md'
out = D / '02-life-breath-and-death-v25-20261014.md'
t = src.read_text(encoding='utf-8')

EDITS = []
def ed(old, new):
    EDITS.append((old, new))

# ---------------------------------------------------------------- Life set before a person
ed('The same chapter begins the choice with God\'s own work on the heart:',
   'The same chapter also speaks of God\'s own work on the heart:')
ed('all who hate me love death" (Proverbs 8:35–36). To hate wisdom is to love death, a love the person does not know he has.',
   'all who hate me love death" (Proverbs 8:35–36). To hate wisdom is to love death.')
ed('''- "Death and life are in the power of the tongue, and those who love it will eat its fruits" (Proverbs 18:21)
''', '''- "Death and life are in the power of the tongue, and those who love it will eat its fruits" (Proverbs 18:21). James calls the tongue "a restless evil, full of deadly poison" (James 3:8).

The same word can be death to one and life to another. Paul says of the message he carries: "to one a fragrance from death to death, to the other a fragrance from life to life. Who is sufficient for these things?" (2 Corinthians 2:16).
''')
ed('"The desire of the sluggard kills him, for his hands refuse to labor" (Proverbs 21:25). Sections 10.1, 10.5 and 10.6 follow these.',
   '"The desire of the sluggard kills him, for his hands refuse to labor" (Proverbs 21:25). Proverbs names more:\n'
   '- "He dies for lack of discipline, and because of his great folly he is led astray" (Proverbs 5:23)\n'
   '- "whoever hates reproof will die" (Proverbs 15:10)\n'
   '- "he who despises his ways will die" (Proverbs 19:16)\n\n'
   'Elihu says it of those who will not hear: "if they do not listen, they perish by the sword and die without knowledge" (Job 36:12). Sections 10.1, 10.5 and 10.6 follow these.')
ed('''- It reaches back the other way too: when a righteous man turns to injustice, "None of the righteous deeds that he has done shall be remembered" (18:24).

Section 10.7 follows the choosing, and Chapter 14 the turning.''',
   '''- It reaches back the other way too: when a righteous man turns to injustice, "None of the righteous deeds that he has done shall be remembered" (18:24).
- Trust can lean the wrong way: "if he trusts in his righteousness and does injustice, none of his righteous deeds shall be remembered, but in his injustice that he has done he shall die" (33:13).

Another's death can be laid at a person's hand. The watchman who does not warn the wicked is told, "his blood I will require at your hand"; if he warns and is not heeded, "you will have delivered your soul" (Ezekiel 33:8–9). Section 10.10 follows that.

Section 10.7 follows the choosing, and Chapter 14 the turning.''')

# ---------------------------------------------------------------- Living before God (OT-02.10)
ed('Scripture shows it most plainly in an oath that people swore by life itself.',
   'Scripture shows it in an oath that people swore by life itself.')
ed('"As the Lord lives" is its commonest form, and often a second life is joined to it, the life of the one spoken to.',
   '"As the Lord lives" is its commonest form, in 39 verses. In six of them a second life is joined to it, the life of the one spoken to.')

# ---------------------------------------------------------------- What death is
ed('Yet the Preacher can write that "the day of death" is better "than the day of birth" (Ecclesiastes 7:1).',
   'Yet the Preacher can write that "the day of death" is better "than the day of birth" (Ecclesiastes 7:1). Asaph, who says "I was envious" of the wicked, noticed that "they have no pangs until death" (Psalm 73:3–4).\n\n'
   'The law names what a death can leave unfinished. A man who has built a house, planted a vineyard or betrothed a wife is sent home from the battle, "lest he die in the battle and another man dedicate it … enjoy its fruit … take her" (Deuteronomy 20:5–7). I read the law as weighing a life by what it has begun.\n\n'
   'What lies beyond death is not shown to a person. God asks Job, "Have the gates of death been revealed to you, or have you seen the gates of deep darkness?" (Job 38:17).\n\n'
   '''### Death spoken of in more than one way

So far, death is the end of the body's life. Scripture also uses the word for more than that, sometimes in one sentence. "Leave the dead to bury their own dead" (Matthew 8:22; Luke 9:60). The first "dead" are living people; the second is the man's father. Jesus does not explain the first.

The father of the son who came home says, "this my son was dead, and is alive again; he was lost, and is found" (Luke 15:24). He sets "dead" beside "lost", and "alive" beside "found". The son had not died in body. The word for "lost", *apollymi* ("to destroy, perish, lose"), is used of the sheep and the coin in the same chapter (15:4, 8). It is the word in "whoever believes in him should not perish but have eternal life" (John 3:16), and in "the Son of Man came to seek and to save the lost" (Luke 19:10).

The verses speak of death in these ways:
- **the body's death**: the breath taken, the return to dust (above)
- **death in the living**: people still alive called dead (below, "Death in the living")
- **dying *to***: a death the believer has already died, to sin and to the law (below, "Dead to sin")
- **a death beyond death**: "the second death" (Revelation 2:11; 20:14; 21:8; below, "Life, and judgment")
- **death as a power** that reigns and stings (Romans 5:14; 1 Corinthians 15:56; "Going down to Sheol")
- **the living made like the dead**: for fear, the guards at the tomb "became like dead men" (Matthew 28:4); John "fell at his feet as though dead" (Revelation 1:17)

The same word changes character with what it is joined to. Of the same people Paul says that they "were dead in" their trespasses (Ephesians 2:1, 5; Colossians 2:13) and that they "died to sin" (Romans 6:2, 11). Dead *in* trespasses is death under them. Dead *to* sin is a death that ends their rule: "one who has died has been set free from sin" (Romans 6:7). The word passes even to sin itself: "apart from the law, sin lies dead"; then, "when the commandment came, sin came alive and I died" (Romans 7:8–9). It is said of faith, and set beside the body: "as the body apart from the spirit is dead, so also faith apart from works is dead" (James 2:26). And Paul says both of one person: "although the body is dead because of sin, the Spirit is life because of righteousness" (Romans 8:10).

Perishing is spoken of in the same way. Some are perishing now: "the word of the cross is folly to those who are perishing, but to us who are being saved it is the power of God" (1 Corinthians 1:18); "even if our gospel is veiled, it is veiled to those who are perishing" (2 Corinthians 4:3). Paul gives a reason in one place: "because they refused to love the truth and so be saved" (2 Thessalonians 2:10). Jesus warns, "unless you repent, you will all likewise perish" (Luke 13:3). What is set against perishing is eternal life: "I give them eternal life, and they will never perish" (John 10:28).''')

# ---------------------------------------------------------------- Death and sin
ed('''Scripture ties death to sin from the first command. "of the tree of the knowledge of good and evil you shall not eat, for in the day that you eat of it you shall surely die" (Genesis 2:17). The first word spoken against that command''',
   '''Scripture ties death to sin from the first command. "of the tree of the knowledge of good and evil you shall not eat, for in the day that you eat of it you shall surely die" (Genesis 2:17). The woman repeats it with more than was said: "neither shall you touch it, lest you die" (Genesis 3:3). The first word spoken against that command''')
ed('''- a sting: "The sting of death is sin, and the power of sin is the law" (1 Corinthians 15:56)
''', '''- a sting: "The sting of death is sin, and the power of sin is the law" (1 Corinthians 15:56)

He sets another reign against it: "as sin reigned in death, grace also might reign through righteousness leading to eternal life" (Romans 5:21).
''')
ed('"The very commandment that promised life proved to be death to me" (Romans 7:10). Section 10.6 follows the desire, and Chapter 12 the sin.',
   '"The very commandment that promised life proved to be death to me" (Romans 7:10). Section 10.6 follows the desire, and Chapter 12 the sin.\n\n'
   'These verses do not always say which death they mean. "The wages of sin is death" is set against "eternal life" (Romans 6:23). "Sin when it is fully grown brings forth death" (James 1:15). "If you live according to the flesh you will die" (Romans 8:13). "The soul who sins shall die" (Ezekiel 18:4). I read Romans 6:23, where the opposite is eternal life, as speaking of more than the body\'s death. The others I leave as they are written.\n\n'
   'In Acts a lie is followed at once by death. Peter asks Ananias, "Why is it that you have contrived this deed in your heart? You have not lied to man but to God." "When Ananias heard these words, he fell down and breathed his last. And great fear came upon all who heard of it" (Acts 5:4–5). His wife dies the same way (5:10).')
ed('"But each one shall die for his own sin" (2 Kings 14:6).',
   '"But each one shall die for his own sin" (2 Kings 14:6; from Deuteronomy 24:16). Jeremiah repeats it: "everyone shall die for his own iniquity" (Jeremiah 31:30).')

# ---------------------------------------------------------------- Death in the living
ed('''- **A church can be near it.** "strengthen what remains and is about to die" (Revelation 3:2).
''', '''- **A church can be near it.** "strengthen what remains and is about to die" (Revelation 3:2).
- **Works and faith can be dead.** "repentance from dead works" (Hebrews 6:1); the blood of Christ will "purify our conscience from dead works to serve the living God" (9:14); "faith by itself, if it does not have works, is dead" (James 2:17).
- **It can lie behind a fair outside.** "you are like whitewashed tombs, which outwardly appear beautiful, but within are full of dead people's bones and all uncleanness" (Matthew 23:27).
- **A people can die while it lives.** Ephraim "incurred guilt through Baal and died" (Hosea 13:1). False teachers are "twice dead, uprooted" (Jude 12).
- **Inner things can perish.** "the hope of the godless shall perish" (Job 8:13). "My endurance has perished; so has my hope from the Lord" (Lamentations 3:18). "Our bones are dried up, and our hope is lost" (Ezekiel 37:11). "Courage shall fail both king and officials" (Jeremiah 4:9); the word behind "courage" is *lēḇ* ("heart"), and the verb is *ʾāḇaḏ* ("perish"). "The wisdom of their wise men shall perish" (Isaiah 29:14). "Truth has perished; it is cut off from their lips" (Jeremiah 7:28). "A bribe corrupts the heart" (Ecclesiastes 7:7), with the same verb.

The verses name what brings it, each in its own place:
- trespasses and sins (Ephesians 2:1), "the uncircumcision of your flesh" (Colossians 2:13)
- self-indulgence (1 Timothy 5:6)
- works that look alive: "I know your works. You have the reputation of being alive" (Revelation 3:1)
- not loving (1 John 3:14)
- the mind set on the flesh (Romans 8:6)
- sin taking its opportunity through the commandment: "It was sin, producing death in me through what is good" (Romans 7:13)
- worldly grief (2 Corinthians 7:10)
- the letter: "the letter kills, but the Spirit gives life" (2 Corinthians 3:6)
- hating wisdom: "all who hate me love death" (Proverbs 8:36)

No verse gathers these into one list, and I do not join them into one.

The verses also name the way out. "Truly, truly, I say to you, an hour is coming, and is now here, when the dead will hear the voice of the Son of God, and those who hear will live" (John 5:25); "whoever hears my word and believes him who sent me … has passed from death to life" (5:24). God "made alive together with him, having forgiven us all our trespasses" (Colossians 2:13). To believers: "Awake, O sleeper, and arise from the dead, and Christ will shine on you" (Ephesians 5:14). The lost son "came to himself" and went home, and his father calls it coming alive (Luke 15:17–24). John gives a sign that it has happened: "We know that we have passed out of death into life, because we love the brothers" (1 John 3:14). "Made alive", below, follows this.

One person can bring it on another. "And so by your knowledge this weak person is destroyed, the brother for whom Christ died" (1 Corinthians 8:11); "By what you eat, do not destroy the one for whom Christ died" (Romans 14:15). Section 10.10 follows that.
''')
ed('"among those in full vigor we are like dead men" (Isaiah 59:10).',
   '"among those in full vigor we are like dead men" (Isaiah 59:10). "He has made me dwell in darkness like the dead of long ago" (Lamentations 3:6).')

# new subsection Dead to sin, before Going down to Sheol
ed('''## Going down to Sheol
''', '''### Dead to sin

Paul speaks of a death the believer has already died. "How can we who died to sin still live in it?" (Romans 6:2). "Do you not know that all of us who have been baptized into Christ Jesus were baptized into his death?" (6:3). "For one who has died has been set free from sin" (6:7). "So you also must consider yourselves dead to sin and alive to God in Christ Jesus" (6:11).
- **To the law:** "you also have died to the law through the body of Christ, so that you may belong to another, to him who has been raised from the dead, in order that we may bear fruit for God" (Romans 7:4); "through the law I died to the law, so that I might live to God" (Galatians 2:19).
- **To the powers of the world:** "If with Christ you died to the elemental spirits of the world, why, as if you were still alive in the world, do you submit to regulations" (Colossians 2:20).
- **With him:** "If we have died with him, we will also live with him" (2 Timothy 2:11). "One has died for all, therefore all have died" (2 Corinthians 5:14).

This death is spoken of as done, and a putting to death is still to be done. "Put to death therefore what is earthly in you" (Colossians 3:5); "if by the Spirit you put to death the deeds of the body, you will live" (Romans 8:13). Paul also carries a death in his body: "always carrying in the body the death of Jesus, so that the life of Jesus also may be manifested in our bodies" (2 Corinthians 4:10).

It is the opposite of being dead in sin (above). Chapter 14 follows the life that comes out of it.

## Going down to Sheol
''')

# ---------------------------------------------------------------- Sleep and waking
ed('''Scripture speaks of death as sleep. And it gives its hope against death in the same picture: waking.
''', '''Scripture speaks of death as sleep. And it gives its hope against death in the same picture: waking.

The books of Kings and Chronicles tell the deaths of kings this way, 36 times: "Then David slept with his fathers and was buried in the city of David" (1 Kings 2:10). The sleep is with the fathers: the king lies down with those who went before him.
''')
ed('"the girl is not dead but sleeping. And they laughed at him" (Matthew 9:24).',
   '"the girl is not dead but sleeping. And they laughed at him" (Matthew 9:24); Luke adds, "knowing that she was dead" (Luke 8:53).')

# ---------------------------------------------------------------- Life weighed
ed('Paul says of Asia, "we were so utterly burdened beyond our strength that we despaired of life itself" (2 Corinthians 1:8).',
   'Paul says of Asia, "we were so utterly burdened beyond our strength that we despaired of life itself" (2 Corinthians 1:8). A psalmist has lived near death all along: "Afflicted and close to death from my youth up, I suffer your terrors" (Psalm 88:15).')
ed('The same life is loathed, worn down, enjoyed and let go.',
   'Death\'s certainty can be turned into a reason. "Let us eat and drink, for tomorrow we die" (Isaiah 22:13). In Isaiah the Lord answers it at once: "Surely this iniquity will not be atoned for you until you die" (22:14). Paul quotes the saying as what would follow if the dead are not raised (1 Corinthians 15:32).\n\n'
   'The same life is loathed, worn down, enjoyed and let go.')

# ---------------------------------------------------------------- Facing death (B1.5, C8, C9)
ed('''Scripture does not make the coming of death a calm thing. It shows the inner being under it:''',
   '''Scripture shows the inner being under the coming of death. Often it is anguish (the calmer deaths are in "Dying to the Lord", below):''')
ed('''- In Gethsemane: "My soul is very sorrowful, even to death" (Matthew 26:38)
''', '''- In Gethsemane: "My soul is very sorrowful, even to death" (Matthew 26:38)

Bildad says the wicked man "is torn from the tent in which he trusted and is brought to the king of terrors" (Job 18:14). He says it of Job, and God's later verdict on Job's friends stands over it (Job 42:7; 10.12). The Preacher pictures old age near its end: "they are afraid also of what is high, and terrors are in the way … and desire fails, because man is going to his eternal home" (Ecclesiastes 12:5).
''')
ed('''Isaac passed off his wife as his sister: "Because I thought, 'Lest I die because of her.'" (Genesis 26:9).''',
   '''Isaac passed off his wife as his sister: "Because I thought, 'Lest I die because of her.'" (Genesis 26:9). Judah kept Shelah from Tamar, "for he feared that he would die, like his brothers" (Genesis 38:11). Lot would not flee to the hills, "lest the disaster overtake me and I die" (Genesis 19:19). Near the tabernacle the people cried, "Behold, we perish, we are undone … Are we all to perish?" (Numbers 17:12–13). And Agag came "cheerfully", saying, "Surely the bitterness of death is past" (1 Samuel 15:32).''')
ed('''Paul gives the nearness of death a purpose:''',
   '''A death can bring fear on others. After Ananias and Sapphira died, "great fear came upon the whole church and upon all who heard of these things" (Acts 5:11).

Paul gives the nearness of death a purpose:''')
ed('and he was heard because of his reverence" (Hebrews 5:7).',
   'and he was heard because of his reverence" (Hebrews 5:7). Paul says the apostles live "like men sentenced to death, because we have become a spectacle to the world, to angels, and to men" (1 Corinthians 4:9).')

# ---------------------------------------------------------------- Those left behind (new, before Wanting to die)
ed('''## Wanting to die
''', '''## Those left behind

A death is met by those who remain, and Scripture shows them.
- Hagar could not watch: "Let me not look on the death of the child." And "she lifted up her voice and wept" (Genesis 21:16).
- David fasted and wept while his child was ill. When the child died, he "arose and ate food", and his servants asked why. He answered, "But now he is dead. Why should I fast? Can I bring him back again? I shall go to him, but he will not return to me" (2 Samuel 12:21, 23).
- His grief for Absalom brought Joab's rebuke: "today I know that if Absalom were alive and all of us were dead today, then you would be pleased" (2 Samuel 19:6).
- Martha met Jesus with, "Lord, if you had been here, my brother would not have died" (John 11:21).
- At Nain a dead man was carried out, "the only son of his mother, and she was a widow". Jesus raised him and "gave him to his mother" (Luke 7:12, 15).
- Paul was spared a death he feared: God had mercy on Epaphroditus, "and not only on him but on me also, lest I should have sorrow upon sorrow" (Philippians 2:27).
- Uriah's wife "lamented over her husband" (2 Samuel 11:26). Jacob speaks of Rachel's death, "to my sorrow" (Genesis 48:7).

The law limits the mourning: "You shall not cut yourselves or make any baldness on your foreheads for the dead" (Deuteronomy 14:1). Under judgment it is withheld: "They shall not be lamented, nor shall they be buried" (Jeremiah 16:4); "No one shall break bread for the mourner, to comfort him for the dead" (16:7). A death can pass with no one taking it in: "The righteous man perishes, and no one lays it to heart" (Isaiah 57:1). And a death can be promised its mourners: "people shall burn spices for you and lament for you, saying, 'Alas, lord!'" (Jeremiah 34:5).

Paul does not forbid the grief. He sets it apart from grief that has no hope (1 Thessalonians 4:13, in "Sleep and waking", above). Section 10.1 follows grief.

## Wanting to die
''')

# ---------------------------------------------------------------- Wanting to die (B1.6-B1.8, C10, C11)
ed('''In the words of Elijah, Jonah, Job and Saul below, the Hebrew word behind "my life" or "I" is *nephesh* ("soul, life"). Most other such wishes name no inner word at all.''',
   '''In the words of Elijah, Jonah, Job, Saul and Samson below, the Hebrew word behind "my life" or "I" is *nephesh* ("soul, life"). Most other such wishes name no inner word at all: of the 24 verses with a wish to die, 17 do not.''')
ed('''and asks, "Why did I not die at birth, come out from the womb and expire?" (Job 3:11).''',
   '''and asks, "Why did I not die at birth, come out from the womb and expire?" (Job 3:11); "Would that I had died before any eye had seen me" (10:18).''')
ed('''- Rachel, envying her sister:''',
   '''- Jeremiah: "Cursed be the day on which I was born!" He wishes he had died before birth, "because he did not kill me in the womb; so my mother would have been my grave", and asks, "Why did I come out from the womb to see toil and sorrow, and spend my days in shame?" (Jeremiah 20:14, 17–18).
- Rachel, envying her sister:''')
ed('"it would have been better for us to serve the Egyptians than to die in the wilderness" (Exodus 14:12; 10.6, 10.12).',
   '"it would have been better for us to serve the Egyptians than to die in the wilderness" (Exodus 14:12; 10.6, 10.12). The complaint comes back in the wilderness: "Would that we had perished when our brothers perished before the Lord!" (Numbers 20:3; also Exodus 14:11; Numbers 21:5).')
ed('What answers these wishes is seldom death.',
   'Of the wishes in this section, four are answered with something other than death:')
ed('Where the wish is granted, it comes at the end of a life already lost. Samson is given one last act of strength (Judges 16:30).',
   'Three are granted, each to a man already blinded or wounded. Samson, blinded and a prisoner (Judges 16:21), is given one last act of strength (16:30).')
ed('In these passages, the one who has had enough is more often fed than taken.',
   'So, of the seven, two are fed, two are answered another way, and three are granted.')

# ---------------------------------------------------------------- Delivered from death (sources)
ed('Even his discipline stops short of it: "The Lord has disciplined me severely, but he has not given me over to death" (Psalm 118:18).',
   'Even his discipline stops short of it: "The Lord has disciplined me severely, but he has not given me over to death" (Psalm 118:18). "In famine he will redeem you from death" (Job 5:20); "He who is bowed down shall speedily be released; he shall not die and go down to the pit" (Isaiah 51:14); a psalm asks him to "preserve those doomed to die" (Psalm 79:11). Habakkuk rests it on who God is: "Are you not from everlasting, O Lord my God, my Holy One? We shall not die" (Habakkuk 1:12).')

# ---------------------------------------------------------------- Made alive (C17, C18, C21)
ed('"If anyone keeps my word, he will never see death" (John 8:51);',
   '"If anyone keeps my word, he will never see death" (John 8:51), and his hearers answer, "Abraham died, as did the prophets" (8:52). Of the bread from heaven he says, "that one may eat of it and not die" (6:50). Hebrews tells of one man who did not see death: "By faith Enoch was taken up so that he should not see death … Now before he was taken he was commended as having pleased God" (Hebrews 11:5).')
ed('''- Isaiah says it of the soul: "he poured out his soul to death and was numbered with the transgressors; yet he bore the sin of many" (Isaiah 53:12)
''', '''- Isaiah says it of the soul: "he poured out his soul to death and was numbered with the transgressors; yet he bore the sin of many" (Isaiah 53:12)

He went to that death himself: "he humbled himself by becoming obedient to the point of death, even death on a cross" (Philippians 2:8). "For the death he died he died to sin, once for all, but the life he lives he lives to God" (Romans 6:10), and "death no longer has dominion over him" (6:9).
''')
ed('Paul says what that death means for those who live: "he died for all,',
   'Paul says what that death means for those who live: "For the love of Christ controls us, because we have concluded this: that one has died for all, therefore all have died; and he died for all,')
ed('(2 Corinthians 5:15). He also speaks of a death the believer has died, and of a putting to death still to be done. "How can we who died to sin still live in it?" (Romans 6:2). "Put to death therefore what is earthly in you" (Colossians 3:5).',
   '(2 Corinthians 5:14–15). He also speaks of a death the believer has died, and of a putting to death still to be done ("Dead to sin", above).')

# ---------------------------------------------------------------- Dying to the Lord (B1.9, B1.10, C4, C5, C16, C20)
ed('''He says it of himself: "Christ will be honored in my body, whether by life or by death. For to me to live is Christ, and to die is gain" (Philippians 1:20–21).''',
   '''"For to this end Christ died and lived again, that he might be Lord both of the dead and of the living" (14:9). He says it of himself: "Christ will be honored in my body, whether by life or by death. For to me to live is Christ, and to die is gain" (Philippians 1:20–21). And to a church: "whether Paul or Apollos or Cephas or the world or life or death or the present or the future—all are yours" (1 Corinthians 3:22).''')
ed('''- "as dying, and behold, we live" (2 Corinthians 6:9)
''', '''- "as dying, and behold, we live" (2 Corinthians 6:9)
- "So death is at work in us, but life in you" (2 Corinthians 4:12)

Death does not part a person from God's love: "For I am sure that neither death nor life, nor angels nor rulers, nor things present nor things to come, nor powers, nor height nor depth, nor anything else in all creation, will be able to separate us from the love of God in Christ Jesus our Lord" (Romans 8:38–39).
''')
ed('''The death of those who belong to God is seen by him. "Precious in the sight of the Lord is the death of his saints" (Psalm 116:15). Balaam says, "Let me die the death of the upright, and let my end be like his!" (Numbers 23:10). "The righteous finds refuge in his death" (Proverbs 14:32). Hebrews says of the patriarchs, "These all died in faith, not having received the things promised" (Hebrews 11:13), and of Abel, "through his faith, though he died, he still speaks" (Hebrews 11:4). Jesus speaks of a death that bears fruit: "unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit" (John 12:24).''',
   '''Scripture speaks of the death of the upright in its own words:
- precious: "Precious in the sight of the Lord is the death of his saints" (Psalm 116:15)
- wished for: Balaam says, "Let me die the death of the upright, and let my end be like his!" (Numbers 23:10)
- a refuge: "The righteous finds refuge in his death" (Proverbs 14:32)
- in faith: "These all died in faith, not having received the things promised" (Hebrews 11:13); of Abel, "through his faith, though he died, he still speaks" (Hebrews 11:4)
- bearing fruit: "unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit" (John 12:24)
- glorifying God: Jesus speaks to Peter of "what kind of death he was to glorify God" (John 21:19)

Some wait to see one thing before they die, and then let go. Simeon had been told "he would not see death before he had seen the Lord's Christ" (Luke 2:26). Holding the child, he says, "Lord, now you are letting your servant depart in peace, according to your word" (2:29). Jacob, told that Joseph lived: "It is enough; Joseph my son is still alive. I will go and see him before I die" (Genesis 45:28); and when he had: "Now let me die, since I have seen your face and know that you are still alive" (46:30).''')
ed('''Some of the last words Scripture records before a death are a blessing or a request:''',
   '''Some of the last words Scripture records before a death are a blessing, a request, or a word about what God will do:''')
ed('''- Jacob, on seeing Joseph again: "Now let me die, since I have seen your face and know that you are still alive" (Genesis 46:30)
''', '')
ed('''- "By faith Jacob, when dying, blessed each of the sons of Joseph, bowing in worship over the head of his staff" (Hebrews 11:21)
''', '''- "By faith Jacob, when dying, blessed each of the sons of Joseph, bowing in worship over the head of his staff" (Hebrews 11:21)
- "By faith Joseph, at the end of his life, made mention of the exodus of the Israelites and gave directions concerning his bones" (Hebrews 11:22)
''')
ed('''Others hold to someone even to death. Ruth says to Naomi, "Where you die I will die, and there will I be buried" (Ruth 1:17). Section 10.10 follows that loyalty.''',
   '''Others hold to someone, or to something, even to death.
- Ruth to Naomi: "Where you die I will die, and there will I be buried" (Ruth 1:17).
- The spies to Rahab: "Our life for yours even to death!" (Joshua 2:14).
- Jonathan, condemned by his father's oath: "Here I am; I will die" (1 Samuel 14:43).
- Esther, going to the king: "if I perish, I perish" (Esther 4:16).
- Thomas: "Let us also go, that we may die with him" (John 11:16).
- Job: "till I die I will not put away my integrity from me" (Job 27:5).
- Paul: "I would rather die than have anyone deprive me of my ground for boasting" (1 Corinthians 9:15).
- To a church: "Be faithful unto death, and I will give you the crown of life" (Revelation 2:10). Of the faithful: "they loved not their lives even unto death" (Revelation 12:11).

The readiness can fail. Peter said, "Lord, I am ready to go with you both to prison and to death", and was told, "the rooster will not crow this day, until you deny three times that you know me" (Luke 22:33–34). "If I must die with you, I will not deny you." And they all said the same (Mark 14:31).

Jesus speaks of losing one's life to find it, and asks, "For what does it profit a man if he gains the whole world and loses or forfeits himself?" (Luke 9:24–25; Chapter 5). Section 10.10 follows the loyalty.''')

# ---------------------------------------------------------------- After death (C19, Psa 88:10)
ed('''- "The dead do not praise the Lord, nor do any who go down into silence" (Psalm 115:17)
''', '''- "The dead do not praise the Lord, nor do any who go down into silence" (Psalm 115:17)
- "Do you work wonders for the dead? Do the departed rise up to praise you?" (Psalm 88:10)
''')
ed('''Scripture states both. I leave them side by side.

## What follows''', '''Scripture states both. I leave them side by side.

The living are told how to deal with the dead. Inquiring of them is forbidden: there shall not be found among you "a necromancer or one who inquires of the dead" (Deuteronomy 18:11). Israel is condemned because they "ate sacrifices offered to the dead" (Psalm 106:28). Kindness to the dead is blessed. Naomi says to her daughters-in-law, "May the Lord deal kindly with you, as you have dealt with the dead and with me" (Ruth 1:8).

## What follows''')

# ---------------------------------------------------------------- apply
for old, new in EDITS:
    n = t.count(old)
    if n != 1:
        sys.exit(f'REFUSED: expected 1 match, found {n}: {old[:90]!r}')
    t = t.replace(old, new)
out.write_text(t, encoding='utf-8')
print(f'{len(EDITS)} edits applied -> {out}')
