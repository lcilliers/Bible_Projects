"""Group E (thirst, hunger): one decision per verse (#1993, item F). Read beside the worksheet
m18-group-E-worksheet-v1-20261009.md. Format: reference: (decision, place, reason). Used by m18-group-register-build-v1-20261009.py."""
D = {
 # the one who gives water, thirsty; the spring and the rivers
 'Joh 7:37': ('a', '10.6 Thirst answered', '"If anyone thirsts, let him come to me and drink. Whoever believes in me ... Out of his heart will flow rivers of living water" (7:37-38), "this he said about the Spirit" (7:39). In John 4 the spring wells up in him; here rivers flow out of him (Ch 6).'),
 'Joh 19:28': ('a', '10.6 Thirst answered', '"knowing that all was now finished, said (to fulfill the Scripture), I thirst." The one who offered living water thirsts, and says so knowing. Then "It is finished" (19:30).'),
 'Psa 69:21': ('a', '10.6 Thirst answered', '"for my thirst they gave me sour wine to drink", after "I looked for pity, but there was none, and for comforters, but I found none" (69:20). Thirst answered with mockery; the sour wine of Joh 19:29.'),
 'Mat 5:6': ('a', '10.6 Thirst answered', '"Blessed are those who hunger and thirst for righteousness, for they shall be satisfied." The want itself is called blessed, aimed at righteousness.'),
 'Isa 41:17': ('a', '10.6 Thirst answered', '"When the poor and needy seek water, and there is none, and their tongue is parched with thirst, I the Lord will answer them; I the God of Israel will not forsake them", then rivers on the bare heights (41:18).'),
 'Isa 49:10': ('a', '10.6 Thirst answered', '"they shall not hunger or thirst ... for he who has pity on them will lead them, and by springs of water will guide them." The reason given is his pity.'),
 'Rev 7:16': ('a', '10.6 Thirst answered', '"They shall hunger no more, neither thirst anymore", with "the Lamb ... will be their shepherd, and he will guide them to springs of living water, and God will wipe away every tear" (7:17). Close in wording to Isa 49:10.'),
 'Neh 9:15': ('a', '10.6 Thirst answered', '"water for them out of the rock for their thirst", then "But they ... acted presumptuously and stiffened their neck" (9:16), "not mindful of the wonders" (9:17). Thirst met, then forgotten.'),
 'Isa 48:21': ('a', '10.6 Thirst answered', '"They did not thirst when he led them through the deserts; he made water flow for them from the rock", then "There is no peace ... for the wicked" (48:22).'),
 'Act 10:10': ('a', '10.6 Thirst answered', '"he became hungry and wanted something to eat, but while they were preparing it, he fell into a trance", and saw a sheet of animals (10:11-12). The vision came in the hunger; the verses do not say why.'),
 # hunger and thirst endured
 '1Cor 4:11': ('a', '10.6 Thirst answered', '"To the present hour we hunger and thirst ... When reviled, we bless; when persecuted, we endure" (4:11-12). Want endured, answered outward with blessing.'),
 '2Cor 11:27': ('a', '10.6 Thirst answered', '"in hunger and thirst, often without food", then "the daily pressure on me of my anxiety for all the churches" (11:28). The list ends on an inner weight, not a bodily one.'),
 # thirst as judgment, and its ground
 'Deu 28:48': ('a', '10.6 Thirst answered', '"Because you did not serve the Lord your God with joyfulness and gladness of heart, because of the abundance of all things, therefore you shall serve your enemies ... in hunger and thirst" (28:47-48). The ground named is joyless service in plenty.'),
 'Isa 65:13': ('a', '10.6 Thirst answered', '"my servants shall drink, but you shall be thirsty ... my servants shall sing for gladness of heart, but you shall cry out for pain of heart and shall wail for breaking of spirit" (65:13-14); ground: "chose what I did not delight in" (65:12).'),
 'Isa 5:13': ('a', '10.6 Thirst answered', 'Those who "run after strong drink" and "do not regard the deeds of the Lord" (5:11-12): "my people go into exile for lack of knowledge ... their multitude is parched with thirst". The drinkers end thirsty; the lack is knowledge.'),
 'Amo 8:11': ('a', '10.2 Hearing', '"not a famine of bread, nor a thirst for water, but of hearing the words of the Lord. They shall wander ... to seek the word of the Lord, but they shall not find it" (8:11-12). A hunger for the word, sent as judgment.'),
 'Amo 8:13': ('a', '10.2 Hearing', '"the lovely virgins and the young men shall faint for thirst", in the same day as the famine of hearing.'),
 # thirst met or refused by another person
 'Mat 25:35': ('a', '10.10 Friends, company and care', '"I was thirsty and you gave me drink". The King names the thirst of "the least of these my brothers" as his own (25:40).'),
 'Mat 25:37': ('a', '10.10 Friends, company and care', '"Lord, when did we see you ... thirsty and give you drink?" The righteous did not know whom they served.'),
 'Mat 25:42': ('carried', '10.10 (Mat 25:35, 44)', '"I was thirsty and you gave me no drink": the other side of 25:35.'),
 'Mat 25:44': ('a', '10.10 Friends, company and care', '"Lord, when did we see you hungry or thirsty ... and did not minister to you?" The others did not know either. Both ask the same question.'),
 'Lam 4:4': ('a', '10.10 Friends, company and care', '"The tongue of the nursing infant sticks to the roof of its mouth for thirst; the children beg for food, but no one gives to them", after "Even jackals offer the breast ... but the daughter of my people has become cruel" (4:3).'),
 'Rut 2:9': ('a', '10.10 Friends, company and care', 'Boaz: "when you are thirsty, go to the vessels and drink". Ruth: "Why have I found favor in your eyes, that you should take notice of me, since I am a foreigner?" (2:10).'),
 'Judg 4:19': ('a', '10.10 Friends, company and care', '"Please give me a little water to drink, for I am thirsty." She "opened a skin of milk and gave him a drink and covered him", then the tent peg (4:21). A thirst met as a cover for killing. 4:18 is in 10.5 and 10.12.'),
 'Job 24:11': ('a', '10.10 Friends, company and care', '"they tread the winepresses, but suffer thirst"; "yet God charges no one with wrong" (24:12). The worker thirsts among the wine he makes for another.'),
 # already placed
 'Joh 4:15': ('confirmed', '10.6 Thirst answered', 'Quoted in 10.6 Thirst answered. Sound.'),
 'Joh 4:13': ('confirmed', '10.6 Thirst answered', 'Quoted (4:13-14) in 10.6 Thirst answered. Sound.'),
 'Rom 12:20': ('confirmed', '10.10, 10.13, Ch 14', '"if he is thirsty, give him something to drink" in 10.10, 10.13 and Ch 14. Sound.'),
 # place and figure
 'Jer 48:18': ('route C', '', '"sit on the parched ground": the word is the dry ground of Dibon in an oracle on Moab. Kept as data.'),
 'Eze 19:13': ('route C', '', '"planted in the wilderness, in a dry and thirsty land": the vine of the lament for the princes; the word describes land. Kept as data.'),
}
