"""M08 batch 1 (the gaon family and majesty): one decision per verse (#2156).

Every verse was read by Claude in its passage (scratch pull, m08-batch-pull-v1-20261015.py 1 2).
The groups are what emerged from the reading, not a frame laid over it (reading:
m08-batch1-reading-v1-20261015.md). Decision values:
  read     read for the pride / majesty act; carried into the account
  carried  already read in an M09 batch (register named); checked here for its pride side
  data     no inner-being or other-being bearing for this study (route C)
Route: A = God / other beings (13.x), B = the human inner being, A B = both, C = data.
Writes m08-batch1-register-v1-20261015.csv and checks every scope verse has one row.
"""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
G1 = 'I. Pride held in the heart and said'
G2 = 'II. Pride that does not listen or seek'
G3 = 'III. Pride set over another'
G4 = 'IV. What a people takes pride in, brought down'
G5 = 'V. Pride given: the honour God gives'
G6 = 'VI. The majesty of God'
G7 = 'VII. Other senses'
M09 = 'carried (M09 batch 1 register)'
R = [
 # I
 ('Isa 9:9', G1, 'read', 'B', '"say in pride and in arrogance of heart": the bricks have fallen, we will build with dressed stones (9:10); the blow is not read'),
 ('Jer 48:29', G1, 'read', 'B', 'five pride words stacked, ending "the haughtiness of his heart"; 48:30 his boasts are false'),
 ('Isa 16:6', G1, 'read', 'B', 'pride, arrogance, insolence; "in his idle boasting he is not right"; Moab is told to give shelter (16:3-4)'),
 ('Pro 8:13', G1, 'read', 'A B', 'wisdom: the fear of the Lord is hatred of evil; "Pride and arrogance ... I hate"'),
 ('Pro 16:18', G1, 'read', 'B', 'pride before destruction, a haughty spirit before a fall'),
 ('Pro 16:19', G1, M09, 'B', 'lowly spirit with the poor, better than dividing spoil with the proud: pride shares the spoil'),
 ('Pro 29:23', G1, M09, 'B', 'one\'s pride will bring him low: the pride itself is the agent'),
 ('Zep 3:11', G1, 'read', 'A B', '"your proudly exultant ones ... no longer be haughty in my holy mountain"; a people humble and lowly left (3:12)'),
 ('Psa 73:6', G1, 'read', 'B', 'pride is their necklace: worn and shown, out of ease, "no pangs" (73:4-5); hearts overflow with follies (73:7)'),
 ('Job 10:16', G1, 'read', 'A B', 'Job: "were my head lifted up, you would hunt me"; he cannot lift his head (10:15)'),
 # II
 ('Hos 5:5', G2, 'read', 'A B', '"The pride of Israel testifies to his face"; their deeds do not permit them to return; they know not the Lord (5:4)'),
 ('Hos 7:10', G2, 'read', 'A B', 'pride testifies to his face, "yet they do not return ... nor seek him"; strangers devour his strength and he knows it not (7:9)'),
 ('Jer 13:9', G2, 'read', 'A B', 'I will spoil the pride of Judah: a people "who refuse to hear my words, who stubbornly follow their own heart" (13:10)'),
 ('Jer 13:17', G2, 'read', 'B', '"if you will not listen, my soul will weep in secret for your pride"; 13:15 "be not proud, for the Lord has spoken"'),
 ('Job 35:12', G2, 'read', 'A B', 'they cry out but he does not answer "because of the pride of evil men"; none says "Where is God my Maker" (35:10)'),
 ('Job 33:17', G2, 'read', 'A B', 'God warns in dreams "that he may turn man aside from his deed and conceal pride from a man"'),
 ('Isa 26:10', G2, 'read', 'A B', 'favour shown, the wicked "does not learn righteousness ... does not see the majesty of the Lord"'),
 # III
 ('Psa 10:2', G3, 'read', 'B', '"In arrogance the wicked hotly pursue the poor"; 10:4 pride of his face, does not seek God'),
 ('Psa 17:10', G3, 'read', 'B', '"They close their hearts to pity; with their mouths they speak arrogantly"'),
 ('Psa 31:18', G3, 'read', 'B', 'lying lips speak insolently against the righteous "in pride and contempt"'),
 ('Psa 31:23', G3, 'read', 'A B', 'the Lord preserves the faithful "but abundantly repays the one who acts in pride"'),
 ('Psa 36:11', G3, 'read', 'B', '"Let not the foot of arrogance come upon me"; pride as a foot that tramples (M72 group D forward)'),
 ('Psa 59:12', G3, 'read', 'B', '"let them be trapped in their pride" for the sin of their mouths, cursing and lies'),
 ('Psa 94:2', G3, 'read', 'A B', '"repay to the proud"; 94:4 they pour out arrogant words, boast; 94:5-6 crush your people, kill the widow'),
 ('Psa 123:4', G3, 'read', 'B', '"Our soul has had more than enough of the scorn of those who are at ease, of the contempt of the proud"'),
 ('Psa 140:5', G3, 'read', 'B', '"The arrogant have hidden a trap for me"'),
 ('Pro 15:25', G3, 'read', 'A B', 'the Lord tears down the house of the proud "but maintains the widow\'s boundaries"'),
 ('Eze 16:49', G3, 'read', 'B', 'Sodom: "pride, excess of food, and prosperous ease, but did not aid the poor and needy"; 16:50 haughty'),
 ('Eze 16:56', G3, 'read', 'B', '"Sodom a byword in your mouth in the day of your pride"'),
 ('Zep 2:10', G3, 'read', 'B', '"their lot in return for their pride, because they taunted and boasted against the people of the Lord"'),
 ('Isa 13:11', G3, M09, 'A B', 'the pomp of the arrogant, the pompous pride of the ruthless laid low'),
 ('Job 22:29', G3, M09, 'B', 'when they are humbled you say, "It is because of pride"; he saves the lowly'),
 # IV
 ('Lev 26:19', G4, 'read', 'A B', '"I will break the pride of your power" if you will not listen (26:18)'),
 ('Amo 6:8', G4, 'read', 'A B', '"I abhor the pride of Jacob and hate his strongholds"; at ease, not grieved over the ruin of Joseph (6:6)'),
 ('Eze 7:20', G4, 'read', 'B', '"His beautiful ornament they used for pride, and they made their abominable images" of it'),
 ('Eze 7:24', G4, 'read', 'A B', '"I will put an end to the pride of the strong"'),
 ('Eze 24:21', G4, 'read', 'A B', 'my sanctuary, "the pride of your power, the delight of your eyes, and the yearning of your soul"'),
 ('Eze 30:6', G4, 'read', 'A B', '"her proud might shall come down"'),
 ('Eze 30:18', G4, 'read', 'A B', '"her proud might shall come to an end in her"'),
 ('Eze 32:12', G4, 'read', 'A B', '"They shall bring to ruin the pride of Egypt"'),
 ('Eze 33:28', G4, 'read', 'A B', '"her proud might shall come to an end"; 33:26 you rely on the sword'),
 ('Isa 13:19', G4, 'read', 'A B', 'Babylon, "the splendor and pomp of the Chaldeans", like Sodom'),
 ('Isa 14:11', G4, 'read', 'A B', '"Your pomp is brought down to Sheol"; 14:13 "You said in your heart, I will ascend"'),
 ('Isa 23:9', G4, 'read', 'A B', '"to defile the pompous pride of all glory, to dishonor all the honored of the earth"'),
 ('Isa 25:11', G4, M09, 'A B', 'the Lord will lay low his pompous pride "together with the skill of his hands"'),
 ('Isa 28:1', G4, 'read', 'B', '"the proud crown of the drunkards of Ephraim ... the fading flower of its glorious beauty"'),
 ('Isa 28:3', G4, 'read', 'A B', 'the proud crown trodden underfoot; 28:5 the Lord a crown of glory to the remnant'),
 ('Zec 9:6', G4, 'read', 'A B', '"I will cut off the pride of Philistia"'),
 ('Zec 10:11', G4, 'read', 'A B', '"The pride of Assyria shall be laid low"'),
 ('Dan 4:37', G4, M09, 'A B', '"those who walk in pride he is able to humble"; Nebuchadnezzar\'s majesty returned to him (4:36)'),
 ('Isa 2:12', G4, M09, 'A B', 'a day against all that is proud and lofty; cedars, mountains, towers (2:13-15)'),
 ('Job 40:11', G4, M09, 'A B', '"look on everyone who is proud and abase him": God\'s challenge to Job'),
 ('Job 40:12', G4, M09, 'A B', 'as 40:11'),
 # V
 ('Psa 47:4', G5, 'read', 'A B', '"He chose our heritage for us, the pride of Jacob whom he loves"'),
 ('Amo 8:7', G5, 'read', 'A', '"The Lord has sworn by the pride of Jacob": I will never forget their deeds (buying the poor, 8:6)'),
 ('Isa 4:2', G5, 'read', 'A B', 'the fruit of the land "the pride and honor of the survivors of Israel"; the branch of the Lord'),
 ('Isa 60:15', G5, 'read', 'A B', 'forsaken and hated, "I will make you majestic forever, a joy"'),
 ('Nah 2:2', G5, 'read', 'A', '"the Lord is restoring the majesty of Jacob as the majesty of Israel"'),
 ('Deu 33:29', G5, 'read', 'A B', 'the Lord "the shield of your help, and the sword of your triumph"'),
 ('Isa 13:3', G5, 'read', 'A', 'God summons "my proudly exulting ones" to execute his anger'),
 # VI
 ('Exo 15:1', G6, 'read', 'A', '"he has triumphed gloriously" (risen, risen): the horse and rider thrown into the sea'),
 ('Exo 15:21', G6, 'read', 'A', 'Miriam: the same words'),
 ('Exo 15:7', G6, 'read', 'A', '"In the greatness of your majesty you overthrow your adversaries"; 15:9 the enemy said "I will ... my desire shall have its fill"'),
 ('Deu 33:26', G6, 'read', 'A', '"who rides through the heavens to your help, through the skies in his majesty"'),
 ('Psa 68:34', G6, 'read', 'A', '"Ascribe power to God, whose majesty is over Israel"; he gives power to his people (68:35)'),
 ('Psa 93:1', G6, 'read', 'A', '"The Lord reigns; he is robed in majesty"; from everlasting (93:2)'),
 ('Isa 12:5', G6, 'read', 'A B', '"Sing praises to the Lord, for he has done gloriously"'),
 ('Isa 24:14', G6, 'read', 'A B', '"over the majesty of the Lord they shout"'),
 ('Job 37:4', G6, 'read', 'A', '"he thunders with his majestic voice"'),
 ('Isa 2:10', G6, 'read', 'A B', 'hide "from the terror of the Lord, and from the splendor of his majesty"; 2:11 man brought low, the Lord alone exalted'),
 ('Isa 2:19', G6, 'read', 'A B', 'as 2:10, "when he rises to terrify the earth"'),
 ('Isa 2:21', G6, 'read', 'A B', 'as 2:19; 2:22 "Stop regarding man ... of what account is he?"'),
 ('Job 40:10', G6, 'read', 'A B', '"Adorn yourself with majesty and dignity": the challenge, joined to abasing the proud (40:11-12) and saving by one\'s own hand (40:14)'),
 ('Mic 5:4', G6, 'read', 'A', 'the ruler from Bethlehem shepherds "in the strength of the Lord, in the majesty of the name of the Lord his God"'),
 ('Psa 89:9', G6, 'read', 'A', '"You rule the raging [rising] of the sea; when its waves rise, you still them"'),
 ('Job 38:11', G6, 'read', 'A', '"here shall your proud waves be stayed": a limit set'),
 ('Luk 9:43', G6, 'read', 'A B', '"astonished at the majesty of God"; then "The Son of Man is about to be delivered into the hands of men" (9:44)'),
 ('2Pe 1:16', G6, 'read', 'A B', '"eyewitnesses of his majesty"; he "received honor and glory from God the Father" (1:17)'),
 ('Heb 1:3', G6, 'read', 'A', 'after making purification for sins "he sat down at the right hand of the Majesty on high"'),
 ('Heb 8:1', G6, 'read', 'A', '"seated at the right hand of the throne of the Majesty in heaven"'),
 ('Jude 25', G6, 'read', 'A', '"to the only God ... through Jesus Christ our Lord, be glory, majesty, dominion, and authority"'),
 ('Act 19:27', G6, 'read', 'C', 'Artemis may "be deposed from her magnificence, she whom all Asia and the world worship": used only as the contrast in the reflection'),
 # VII
 ('Jer 12:5', G7, 'data', 'C', '"the thicket of the Jordan"'), ('Jer 49:19', G7, 'data', 'C', '"the jungle of the Jordan"'),
 ('Jer 50:44', G7, 'data', 'C', '"the thicket of the Jordan"'), ('Zec 11:3', G7, 'data', 'C', '"the thicket of the Jordan is ruined"'),
 ('Eze 47:5', G7, 'data', 'C', '"the water had risen"'), ('Job 8:11', G7, 'data', 'C', '"Can papyrus grow"'),
 ('Job 41:15', G7, 'data', 'C', 'Leviathan: "His back is made of rows of shields" (ESV "back")'),
 ('Pro 14:3', G7, 'data', 'C', '"a rod for his back" (ESV "back"; no pride in the English)'),
 ('Psa 46:3', G7, 'data', 'C', '"the mountains tremble at its swelling"'), ('Isa 9:18', G7, 'data', 'C', '"a column of smoke"'),
]
scope = [r['reference'] for r in csv.DictReader(open(os.path.join(HERE, 'm08-reading-scope-v1-20261015.csv'), encoding='utf-8')) if r['batch'].startswith('1 ')]
refs = [r[0] for r in R]
assert len(refs) == len(set(refs)), [x for x in refs if refs.count(x) > 1]
assert set(refs) == set(scope), (set(scope) - set(refs), set(refs) - set(scope))
with open(os.path.join(HERE, 'm08-batch1-register-v1-20261015.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['reference', 'group', 'decision', 'route', 'note']); w.writerows(R)
print(len(R), Counter(r[2] for r in R), Counter(r[1] for r in R))
