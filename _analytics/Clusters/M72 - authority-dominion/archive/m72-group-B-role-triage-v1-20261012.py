"""M72 group B (rule, dominion, authority): role triage of the 275 verses (#1998).

Method: Workflow/Instructions/wa-verse-reading-by-role-guide-v1-20261011.md (rule 73),
under the M72 scope ruling (m72-scope-ruling-and-focus-v2-20261012.md) and the trial
(m72-group-B-trial-reading-v1-20261012.md). Each verse gets one decision:

  read     the B word carries the verse's main inner-being operation (or an inner act
           around ruling); read in depth, in its passage, in a phenomenon group
  carried  already placed in the narrative by the act the B word carries
  forward  the B word qualifies another cluster's characteristic (a setting, an outcome,
           a measure); marked forward to that cluster (OT-97)
  god      the B word is said of God or of Christ: God's character only (13.1, route A)
  spirits  said of angels, other spirits or the beasts of the visions (13.2 / 13.3, route A)
  nature   said of the lights (13.4, route A)
  data     an office, a reign, a territory, a title; no inner-being bearing (route C)

Decisions are made by reading; this script only records them and checks coverage.
Usage: python m72-group-B-role-triage-v1-20261012.py
Writes m72-group-B-role-triage-v1-20261012.csv beside itself.
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'm72-group-B-verses-v1-20261012.csv')
OUT = os.path.join(HERE, 'm72-group-B-role-triage-v1-20261012.csv')

# Reading groups (decision "read" or "carried" inside a group)
GROUPS = {
    'R1': 'What rules within a person',
    'R2': 'Ruling another: the manner',
    'R3': 'Wanting rule, refusing it, resenting it',
    'R4': 'Authority received: where it comes from',
    'R5': 'A right held and not used',
    'R6': 'Living under another\'s rule',
    'R7': 'A king who comes to know that God rules',
    'R8': 'Dominion given to mankind',
    'X': 'Single verses',
}

# reference: (decision, group_or_forward, route, note)
D = {
    # R1 What rules within
    'Psa 119:133': ('read', 'R1', 'B', 'trial: let no iniquity get dominion over me'),
    'Psa 19:13': ('read', 'R1', 'B', 'presumptuous sins: let them not have dominion over me'),
    'Rom 6:14': ('read', 'R1', 'B', 'trial: sin will have no dominion, under grace'),
    '1Cor 6:12': ('read', 'R1', 'B', 'I will not be dominated by anything'),
    'Eph 6:12': ('read', 'R1', 'A;B', 'we wrestle against the authorities (13.3 for the powers)'),
    'Ecc 5:19': ('read', 'R1', 'A;B', 'power to enjoy, given by God (with Ecc 6:2)'),
    'Pro 16:32': ('carried', 'R1', 'B', 'Ch 6, 10.13, Ch 11 sec 7; OT-16 closed for M72 (trial)'),
    'Col 3:15': ('carried', 'R1', 'B', 'Ch 11 sec 7'),
    'Gen 4:7': ('carried', 'R1', 'B', 'Ch 10, 10.6 Wanting that owns, Ch 11 sec 4: you must rule over it'),
    '1Cor 7:37': ('carried', 'R1', 'B', '10.6: his desire under control'),
    'Ecc 8:8': ('carried', 'R1', 'B', 'Ch 2: no man has power to retain the spirit'),
    'Ecc 6:2': ('carried', 'R1', 'B', '10.6: God does not give him power to enjoy them'),
    # R2 Ruling another: the manner
    'Lev 25:43': ('carried', 'R2', 'B', '10.10 The fear of God and the weak (trial: confirmed)'),
    'Lev 25:46': ('read', 'R2', 'B', 'not one over another ruthlessly'),
    'Lev 25:53': ('read', 'R2', 'B', 'not ruthlessly over him in your sight'),
    'Neh 5:15': ('carried', 'R2', 'B', '10.10: I did not do so, because of the fear of God'),
    'Eze 34:4': ('read', 'R2', 'B', 'with force and harshness you have ruled them'),
    'Pro 28:15': ('read', 'R2', 'B', 'a wicked ruler over a poor people'),
    'Ecc 8:9': ('read', 'R2', 'B', 'man had power over man to his hurt'),
    '2Sa 23:3': ('read', 'R2', 'B', 'rules justly, in the fear of God'),
    'Isa 14:6': ('carried', 'R2', 'B', '10.10 Anger between people; OT-16 closed for M72'),
    'Mat 20:25': ('read', 'R2', 'B', 'the rulers of the Gentiles lord it over them; not so among you'),
    'Mar 10:42': ('read', 'R2', 'B', 'parallel of Mat 20:25'),
    'Luk 22:25': ('read', 'R2', 'B', 'exercise lordship, called benefactors'),
    '1Pe 5:3': ('read', 'R2', 'B', 'trial: not domineering, but examples'),
    '2Cor 1:24': ('read', 'R2', 'B', 'not lord it over your faith; workers with you for your joy'),
    '1Ti 2:12': ('read', 'R2', 'B', 'exercise authority over a man'),
    '1Cor 7:4': ('read', 'R2', 'B', 'authority over one\'s own body held by the other'),
    'Est 1:22': ('read', 'R2', 'B', 'every man master in his own household, by decree'),
    'Pro 22:7': ('read', 'R2', 'B', 'the rich rules over the poor'),
    # R3 Wanting rule, refusing it, resenting it
    'Gen 37:8': ('read', 'R3', 'B', 'are you indeed to rule over us? they hated him more'),
    'Gen 42:6': ('read', 'R3', 'B', 'Joseph governor; the brothers bow (37:8 fulfilled)'),
    'Judg 8:22': ('read', 'R3', 'B', 'rule over us, for you have saved us'),
    'Judg 8:23': ('read', 'R3', 'B;A', 'I will not rule over you; the Lord will rule over you'),
    'Judg 9:2': ('read', 'R3', 'B', 'which is better: seventy or one? bone and flesh (M47 register C; re-read for M72)'),
    'Num 16:13': ('read', 'R3', 'B', 'make yourself a prince over us'),
    'Hos 8:4': ('read', 'R3', 'B;A', 'they set up princes, but I knew it not'),
    'Act 8:19': ('read', 'R3', 'B', 'Simon: give me this power also'),
    'Jude 8': ('read', 'R3', 'B', 'reject authority (with 2Pe 2:10)'),
    'Judg 15:11': ('read', 'R6', 'B', 'do you not know that the Philistines are rulers over us?'),
    'Dan 5:16': ('read', 'R3', 'B', 'third ruler offered; Daniel: let your gifts be for yourself (5:17)'),
    '2Pe 2:10': ('carried', 'R3', 'B', 'Ch 7: despise authority'),
    'Luk 4:6': ('carried', 'R3', 'A', '13.3: to you I will give all this authority'),
    'Dan 11:3': ('carried', 'R3', 'B', '10.7 Willing: rule with great dominion and do as he wills'),
    'Dan 11:4': ('carried', 'R3', 'B', '10.7 Willing (with 11:3)'),
    # R4 Authority received: where it comes from
    'Joh 19:10': ('read', 'R4', 'B', 'trial: I have authority to release you'),
    'Joh 19:11': ('read', 'R4', 'B;A', 'trial: given you from above'),
    'Rom 13:1': ('read', 'R4', 'B;A', 'no authority except from God'),
    'Rom 13:2': ('read', 'R4', 'B', 'whoever resists the authorities resists what God has appointed'),
    'Rom 13:3': ('carried', 'R4', 'B', '10.12 (three places)'),
    'Tit 3:1': ('read', 'R4', 'B', 'be submissive to rulers and authorities'),
    'Mat 8:9': ('read', 'R4', 'B', 'the centurion: a man under authority'),
    'Luk 7:8': ('read', 'R4', 'B', 'parallel of Mat 8:9'),
    'Act 9:14': ('read', 'R4', 'B', 'authority from the chief priests to bind'),
    'Act 26:10': ('read', 'R4', 'B', 'after receiving authority; I cast my vote against them'),
    'Act 26:12': ('read', 'R4', 'B', 'with the authority and commission of the chief priests'),
    'Mat 21:23': ('read', 'R4', 'B', 'by what authority? who gave you this authority?'),
    'Mat 21:24': ('read', 'R4', 'B', 'I will ask you one question'),
    'Mat 21:27': ('read', 'R4', 'B', 'we do not know'),
    'Mar 11:28': ('read', 'R4', 'B', 'parallel'),
    'Mar 11:29': ('read', 'R4', 'B', 'parallel'),
    'Mar 11:33': ('read', 'R4', 'B', 'parallel'),
    'Luk 20:2': ('read', 'R4', 'B', 'parallel'),
    'Luk 20:8': ('read', 'R4', 'B', 'parallel'),
    # R5 A right held and not used
    '1Cor 9:4': ('read', 'R5', 'B', 'the right to eat and drink'),
    '1Cor 9:5': ('read', 'R5', 'B', 'the right to take along a believing wife'),
    '1Cor 9:6': ('read', 'R5', 'B', 'the right to refrain from working'),
    '1Cor 9:12': ('read', 'R5', 'B', 'we have not made use of this right'),
    '1Cor 9:18': ('read', 'R5', 'B', 'not to make full use of my right'),
    '2Th 3:9': ('read', 'R5', 'B', 'not because we do not have that right'),
    '1Cor 8:9': ('read', 'R5', 'B', 'this right of yours a stumbling block to the weak'),
    '2Cor 10:8': ('read', 'R5', 'B', 'authority for building up; boast and not be ashamed'),
    '2Cor 13:10': ('read', 'R5', 'B', 'not severe in my use of the authority'),
    # R6 Living under another's rule
    'Lev 26:17': ('read', 'R6', 'B;A', 'those who hate you shall rule over you; flee when none pursues'),
    'Psa 106:41': ('read', 'R6', 'B;A', 'those who hated them ruled over them'),
    'Neh 9:28': ('read', 'R6', 'B;A', 'abandoned to enemies, who had dominion; they turned and cried'),
    'Neh 9:37': ('carried', 'R6', 'B', '10.7 Willing: they rule over our bodies as they please; great distress'),
    'Lam 5:8': ('read', 'R6', 'B', 'slaves rule over us; none to deliver'),
    'Est 9:1': ('read', 'R6', 'B', 'hoped to gain the mastery; the reverse occurred'),
    'Isa 63:19': ('read', 'R6', 'B;A', 'like those over whom you have never ruled'),
    'Hab 1:14': ('read', 'R6', 'B;A', 'like crawling things that have no ruler'),
    'Jer 51:46': ('read', 'R6', 'B', 'let not your heart faint ... ruler against ruler'),
    # R7 A king who comes to know that God rules
    'Dan 4:22': ('read', 'R7', 'B', 'your dominion to the ends of the earth'),
    'Dan 4:26': ('read', 'R7', 'B;A', 'from the time that you know that Heaven rules'),
    'Dan 4:30': ('read', 'R7', 'B', 'by my mighty power ... for the glory of my majesty'),
    'Dan 6:26': ('read', 'R7', 'B;A', 'Darius: tremble and fear before the God of Daniel'),
    'Dan 4:34': ('carried', 'R7', 'B;A', '10.7 Willing: my reason returned to me'),
    'Dan 5:21': ('carried', 'R7', 'B;A', '10.7 Willing; 13.1 Willing'),
    'Dan 4:17': ('carried', 'R7', 'A', '13.1 Willing (trial: God as ruler, character only)'),
    'Dan 4:25': ('carried', 'R7', 'A', '13.1 Willing'),
    'Dan 4:32': ('carried', 'R7', 'A', '13.1 Willing'),
    # R8 Dominion given to mankind
    'Gen 1:26': ('read', 'R8', 'A;B', 'let them have dominion; in our image'),
    'Gen 1:28': ('read', 'R8', 'A;B', 'blessed: subdue it and have dominion'),
    'Psa 8:6': ('read', 'R8', 'A;B', 'you have given him dominion over the works of your hands'),
    'Dan 2:38': ('read', 'R8', 'A;B', 'making you rule over them all'),
    # X Single verses
    'Luk 10:19': ('read', 'X', 'A;B', 'authority given; do not rejoice in this (10:20)'),
    'Luk 12:5': ('read', 'X', 'B;A', 'fear him who has authority to cast into hell'),
    'Hos 12:4': ('read', 'X', 'B;A', 'he strove with the angel and prevailed; wept and sought his favor'),
    'Jer 30:21': ('read', 'X', 'B;A', 'their ruler: who would dare of himself to approach me?'),
    'Psa 49:14': ('read', 'X', 'B', 'the upright shall rule over them in the morning'),
    '1Cor 11:10': ('read', 'X', 'B;A', 'a symbol of authority on her head, because of the angels'),
    # forward: the B word qualifies another cluster's characteristic
    'Pro 29:2': ('forward', 'M04', 'B', 'trial: who rules is the setting; the people rejoice or groan (M04, M03)'),
    'Pro 12:24': ('forward', 'M67', 'B', 'rule is the outcome of diligence; slothful put to forced labor'),
    'Pro 17:2': ('forward', 'M16', 'B', 'rule is the outcome of dealing wisely'),
    'Pro 19:10': ('forward', 'M16', 'B', 'what is not fitting: a fool in luxury, a slave over princes'),
    'Exo 21:8': ('forward', 'M14', 'B', 'the right lost because he broke faith with her'),
    'Ecc 10:4': ('forward', 'M33', 'B', 'the ruler\'s anger is the setting; calmness lays offenses to rest'),
    'Pro 29:12': ('forward', 'M41', 'B', 'the ruler listens to falsehood; his officials become wicked'),
    'Pro 29:26': ('forward', 'M83', 'B', 'seeking a ruler\'s face; justice from the Lord'),
    'Pro 23:1': ('forward', 'M15', 'B', 'eating with a ruler: observe carefully'),
    'Ecc 9:17': ('forward', 'M16', 'B', 'words of the wise in quiet, better than a ruler\'s shouting'),
    'Ecc 7:19': ('forward', 'M16', 'B', 'wisdom gives strength more than ten rulers'),
    'Ecc 10:5': ('forward', 'M58', 'B', 'an error proceeding from the ruler'),
    'Ecc 2:19': ('forward', 'M14', 'B', 'vanity: another will be master of all I toiled for'),
    'Act 5:4': ('forward', 'M14', 'B', 'it was at your disposal: the ground of the lie'),
    'Rom 7:1': ('forward', 'M54', 'B', 'the law binding as long as he lives'),
    'Mar 13:34': ('forward', 'M74', 'B', 'servants in charge; the doorkeeper to stay awake'),
    'Luk 19:17': ('forward', 'M13', 'B', 'authority over ten cities as the outcome of faithfulness'),
    'Rev 2:26': ('forward', 'M23', 'A;B', 'to the one who conquers, authority over the nations'),
    'Joh 1:12': ('forward', 'M19', 'A;B', 'the right to become children, to those who believed'),
    'Rev 22:14': ('forward', 'M80', 'A;B', 'the right to the tree of life'),
    'Rev 20:6': ('forward', 'M80', 'A;B', 'over such the second death has no power'),
    'Luk 20:20': ('forward', 'M14', 'B', 'spies pretended, to deliver him to the governor\'s authority'),
    'Luk 12:11': ('forward', 'M20', 'B', 'before the authorities, do not be anxious'),
    '1Ti 2:2': ('forward', 'M21', 'B', 'prayer for those in high positions, for a quiet life'),
    '1Cor 2:1': ('forward', 'M16', 'B', 'not with lofty speech or wisdom'),
    'Isa 52:5': ('forward', 'M03', 'B', 'their rulers wail'),
    'Eze 19:11': ('forward', 'M08', 'B', 'figure: strong stems became rulers; towered aloft'),
    'Eze 19:14': ('forward', 'M03', 'B', 'figure: no scepter for ruling; a lamentation (OT-16 closed for M72: the M02 tag is "dirge")'),
    'Isa 28:14': ('forward', 'M06', 'B', 'you scoffers who rule this people'),
    'Isa 3:12': ('forward', 'M76', 'B', 'your guides mislead you'),
    'Isa 32:1': ('forward', 'M12', 'B', 'princes will rule in justice'),
    'Pro 8:16': ('forward', 'M16', 'B', 'by me (wisdom) princes rule'),
    'Judg 14:4': ('forward', 'M15', 'B', 'his parents did not know it was from the Lord'),
    'Eze 29:15': ('forward', 'M08', 'A', 'never again exalt itself above the nations'),
    'Lam 1:13': ('forward', 'M73', 'A;B', 'a different sense ("made it descend"); stunned, faint all the day'),
    'Isa 14:2': ('forward', 'M06', 'B', 'rule over those who oppressed them'),
    'Pro 6:7': ('forward', 'M67', 'B', 'the ant, without any ruler'),
    'Job 38:33': ('forward', 'M15', 'A;B', 'do you know the ordinances of the heavens?'),
    'Heb 13:10': ('forward', 'M36', 'B', 'no right to eat from our altar'),
    'Mat 7:29': ('forward', 'M48', 'A;B', 'taught as one who had authority; the crowds astonished (7:28)'),
    'Mar 1:22': ('forward', 'M48', 'A;B', 'astonished at his teaching'),
    'Luk 4:32': ('forward', 'M48', 'A;B', 'astonished: his word possessed authority'),
    'Mar 1:27': ('forward', 'M48', 'A;B', 'all amazed: a new teaching with authority'),
    'Luk 4:36': ('forward', 'M48', 'A;B', 'all amazed: with authority he commands the unclean spirits'),
    'Act 26:18': ('forward', 'M60', 'A;B', 'turn from the power of Satan to God; forgiveness'),
    'Col 1:13': ('forward', 'M45', 'A', 'delivered from the domain of darkness'),
    'Rev 13:4': ('forward', 'M36', 'A;B', 'they worshiped the dragon and the beast'),
    # carried in other homes
    'Isa 49:7': ('carried', '10.7', 'B', '10.7 Others around a choice, Ch 11 sec 4; OT-92 open'),
    'Gen 3:16': ('carried', '10.6', 'B', '10.6 A person; Ch 11 sec 4'),
    'Gen 45:8': ('carried', '10.10', 'B;A', '10.10 Anger between people; Ch 11 sec 4'),
    'Gen 45:26': ('carried', 'Ch 2', 'B', 'Ch 2 Life that returns; 10.2'),
    '2Ki 20:13': ('carried', '10.11', 'B', '10.11 (M18: the whole realm is a qualifier)'),
    'Isa 39:2': ('carried', '10.11', 'B', '10.11 (with 2Ki 20:13)'),
    'Mat 9:8': ('carried', '10.12', 'B;A', '10.12 What fear does'),
    'Rev 16:9': ('carried', '10.13', 'A;B', '10.13 Delivered from the wrath to come'),
    'Jer 33:26': ('carried', '13.1', 'A', '13.1 Choosing; OT-92 open'),
    'Joe 2:17': ('carried', '13.1', 'A;B', '13.1 Jealousy; the M72 word is the homonym "byword"'),
    'Isa 9:7': ('carried', '13.1', 'A', '13.1 Jealousy'),
    'Eph 2:2': ('carried', 'Ch 12', 'A;B', 'Ch 12 spirits that act; Ch 14'),
    'Rev 17:13': ('carried', '10.7', 'A', '10.7 Being chosen'),
    'Gen 1:18': ('carried', '13.4', 'A', 'M18: what the lights do; 13.4'),
    # god: God's character only (13.1)
    'Job 25:2': ('god', '13.1', 'A', 'dominion and fear are with God'),
    'Psa 59:13': ('god', '13.1', 'A', 'that they may know that God rules over Jacob; OT-16 closed for M72'),
    '1Ch 29:12': ('god', '13.1', 'A', 'you rule over all (David\'s blessing)'),
    '2Ch 20:6': ('god', '13.1', 'A', 'you rule over all the kingdoms (Jehoshaphat\'s prayer)'),
    'Psa 66:7': ('god', '13.1', 'A', 'who rules by his might forever; let not the rebellious exalt themselves'),
    'Psa 89:9': ('god', '13.1', 'A', 'you rule the raging of the sea'),
    'Psa 103:19': ('god', '13.1', 'A', 'his kingdom rules over all'),
    'Psa 103:22': ('god', '13.1', 'A;B', 'in all places of his dominion; bless the Lord, O my soul'),
    'Psa 22:28': ('god', '13.1', 'A', 'he rules over the nations'),
    'Psa 114:2': ('god', '13.1', 'A', 'Israel his dominion'),
    'Psa 145:13': ('god', '13.1', 'A', 'your dominion endures throughout all generations'),
    'Isa 40:10': ('god', '13.1', 'A', 'his arm rules for him'),
    'Isa 19:4': ('god', '13.1', 'A', 'I will give over the Egyptians to a hard master'),
    'Isa 14:5': ('god', '13.1', 'A', 'the Lord has broken the scepter of rulers'),
    'Isa 41:2': ('god', '13.1', 'A', 'who stirred up one from the east (the M72 word is "tramples")'),
    'Isa 22:21': ('god', '13.1', 'A', 'I will commit your authority to his hand'),
    'Dan 2:37': ('god', '13.1', 'A', 'the God of heaven has given the kingdom, the power'),
    'Dan 3:27': ('god', '13.1', 'A', 'the fire had no power over their bodies'),
    'Dan 4:3': ('god', '13.1', 'A', 'his dominion endures from generation to generation'),
    'Dan 7:14': ('god', '13.1', 'A', 'to him was given dominion'),
    'Dan 7:27': ('god', '13.1', 'A', 'dominion given to the people of the saints'),
    'Jude 25': ('god', '13.1', 'A', 'doxology'),
    '1Ti 6:15': ('god', '13.1', 'A', 'Lord of lords'),
    'Rom 14:9': ('god', '13.1', 'A', 'Lord both of the dead and of the living'),
    'Rom 6:9': ('god', '13.1', 'A', 'death no longer has dominion over him'),
    'Rev 12:10': ('god', '13.1', 'A', 'the authority of his Christ; the accuser thrown down (13.3)'),
    'Joh 5:27': ('god', '13.1', 'A', 'authority to execute judgment'),
    'Joh 17:2': ('god', '13.1', 'A', 'authority over all flesh'),
    'Mat 28:18': ('god', '13.1', 'A', 'all authority has been given to me'),
    'Act 1:7': ('god', '13.1', 'A;B', 'not for you to know times the Father has fixed by his own authority'),
    'Joh 10:18': ('god', '13.1', 'A', 'authority to lay it down; 13.1 Willing holds the Son\'s will'),
    'Mat 9:6': ('god', '13.1', 'A', 'authority on earth to forgive sins'),
    'Mar 2:10': ('god', '13.1', 'A', 'parallel'),
    'Luk 5:24': ('god', '13.1', 'A', 'parallel'),
    'Mic 5:2': ('god', '13.1', 'A', 'one who is to be ruler in Israel'),
    'Isa 9:6': ('god', '13.1', 'A', 'the government shall be upon his shoulder'),
    'Zec 9:10': ('god', '13.1', 'A', 'he shall speak peace; his rule from sea to sea'),
    'Zec 6:13': ('god', '13.1', 'A', 'rule on his throne; the counsel of peace'),
    'Psa 72:8': ('god', '13.1', 'A', 'may he have dominion from sea to sea'),
    'Psa 110:2': ('god', '13.1', 'A', 'rule in the midst of your enemies'),
    'Rom 9:21': ('god', '13.1', 'A', 'has the potter no right over the clay?'),
    'Mat 10:1': ('god', '13.1', 'A', 'gave them authority over unclean spirits'),
    'Mar 6:7': ('god', '13.1', 'A', 'parallel'),
    'Mar 3:15': ('god', '13.1', 'A', 'parallel'),
    'Luk 9:1': ('god', '13.1', 'A', 'parallel'),
    'Deu 15:6': ('god', '13.1', 'A', 'the Lord will bless you; you shall rule over many nations'),
    'Num 24:19': ('god', '13.1', 'A', 'one from Jacob shall exercise dominion (oracle)'),
    'Mic 4:8': ('god', '13.1', 'A', 'the former dominion shall come'),
    'Jer 22:30': ('god', '13.1', 'A', 'none of his offspring shall succeed ... ruling again'),
    '2Ch 7:18': ('god', '13.1', 'A', 'you shall not lack a man to rule Israel'),
    'Col 2:15': ('god', '13.1', 'A', 'he disarmed the rulers and authorities (13.3)'),
    'Eph 1:21': ('god', '13.1', 'A', 'far above all rule and authority'),
    '1Cor 15:24': ('god', '13.1', 'A', 'after destroying every rule and every authority'),
    'Eph 3:10': ('god', '13.1', 'A', 'wisdom made known to the rulers and authorities'),
    '1Pe 3:22': ('god', '13.1', 'A', 'authorities subjected to him'),
    'Col 1:16': ('god', '13.1', 'A', 'dominions, rulers, authorities created through him'),
    'Col 2:10': ('god', '13.1', 'A', 'the head of all rule and authority'),
    # spirits / angels / beasts of the visions
    'Luk 22:53': ('spirits', '13.3', 'A', 'this is your hour, and the power of darkness'),
    'Act 19:16': ('spirits', '13.3', 'A;B', 'the evil spirit mastered them'),
    'Rev 13:2': ('spirits', '13.3', 'A', 'the dragon gave his power and great authority'),
    'Rev 13:5': ('spirits', '13.3', 'A', 'allowed to exercise authority forty-two months'),
    'Rev 13:7': ('spirits', '13.3', 'A', 'authority given it over every tribe'),
    'Rev 13:12': ('spirits', '13.3', 'A', 'exercises all the authority of the first beast'),
    'Rev 17:12': ('spirits', '13.3', 'A', 'ten kings receive authority with the beast'),
    'Rev 6:8': ('spirits', '13.3', 'A', 'Death and Hades given authority over a fourth of the earth'),
    'Rev 9:3': ('spirits', '13.3', 'A', 'locusts given power like scorpions'),
    'Rev 9:10': ('spirits', '13.3', 'A', 'power to hurt people five months'),
    'Rev 9:19': ('spirits', '13.3', 'A', 'the power of the horses'),
    'Rev 14:18': ('spirits', '13.2', 'A', 'the angel who has authority over the fire'),
    'Rev 18:1': ('spirits', '13.2', 'A', 'another angel having great authority'),
    # nature
    'Gen 1:16': ('nature', '13.4', 'A', 'the greater light to rule the day'),
    'Psa 136:8': ('nature', '13.4', 'A', 'the sun to rule over the day'),
    'Psa 136:9': ('nature', '13.4', 'A', 'the moon and stars to rule over the night'),
    # data: offices, reigns, territories, titles
    'Gen 24:2': ('data', '', 'C', 'the servant who had charge of all'),
    'Psa 105:20': ('data', '', 'C', 'the ruler of the peoples set him free'),
    'Psa 105:21': ('data', '', 'C', 'ruler of all his possessions'),
    '1Ki 4:21': ('data', '', 'C', 'Solomon ruled over all the kingdoms'),
    '1Ki 4:24': ('data', '', 'C', 'dominion west of the Euphrates; peace on all sides'),
    '2Ch 9:26': ('data', '', 'C', 'he ruled over all the kings'),
    'Jos 12:2': ('data', '', 'C', 'Sihon ruled from Aroer'),
    'Jos 12:5': ('data', '', 'C', 'ruled over Mount Hermon'),
    'Ezr 4:20': ('data', '', 'C', 'mighty kings ruled the province'),
    'Ezr 7:24': ('data', '', 'C', 'not lawful to impose tribute'),
    '1Ch 26:6': ('data', '', 'C', 'rulers in their fathers\' houses'),
    '2Ch 23:20': ('data', '', 'C', 'the governors of the people'),
    '1Ki 5:16': ('data', '', 'C', 'officers who had charge of the people'),
    '1Ki 9:23': ('data', '', 'C', 'officers who had charge'),
    '2Ch 8:10': ('data', '', 'C', 'officers who exercised authority'),
    'Psa 68:27': ('data', '', 'C', 'Benjamin in the lead'),
    'Luk 3:1': ('data', '', 'C', 'Pilate governor of Judea'),
    'Luk 23:7': ('data', '', 'C', 'Herod\'s jurisdiction'),
    'Isa 16:1': ('data', '', 'C', 'send the lamb to the ruler of the land'),
    'Jer 34:1': ('data', '', 'C', 'kingdoms under his dominion'),
    'Jer 51:28': ('data', '', 'C', 'every land under their dominion'),
    '2Ch 32:9': ('data', '', 'C', 'Sennacherib with all his forces'),
    'Dan 2:10': ('data', '', 'C', 'no great and powerful king has asked such a thing'),
    'Dan 2:15': ('data', '', 'C', 'Arioch, the king\'s captain'),
    'Dan 2:39': ('data', '', 'C', 'a third kingdom shall rule over all the earth'),
    'Dan 2:48': ('data', '', 'C', 'made Daniel ruler over the province'),
    'Dan 5:7': ('data', '', 'C', 'shall be the third ruler (read with Dan 5:16)'),
    'Dan 5:29': ('data', '', 'C', 'proclaimed the third ruler (read with Dan 5:16)'),
    'Dan 6:24': ('data', '', 'C', 'the lions overpowered them'),
    'Dan 7:6': ('data', '', 'C', 'dominion was given to it (vision)'),
    'Dan 7:12': ('data', '', 'C', 'their dominion was taken away (vision)'),
    'Dan 7:26': ('data', '', 'C', 'his dominion shall be taken away (vision)'),
    'Dan 11:5': ('data', '', 'C', 'one of his princes stronger, and shall rule'),
    'Dan 11:39': ('data', '', 'C', 'make them rulers over many'),
    'Dan 11:43': ('data', '', 'C', 'ruler of the treasures of gold'),
    'Judg 9:22': ('data', '', 'C', 'Abimelech ruled three years (read with Judg 9:2)'),
    '1Ki 9:19': ('data', '', 'C', 'M18: route C; the land of his dominion'),
    '2Ch 8:6': ('data', '', 'C', 'M18: route C'),
    'Rev 11:6': ('data', '', 'C', 'M18: data; the two witnesses\' power'),
    'Isa 3:4': ('data', '', 'C', 'boys their princes (judgment oracle, read with Isa 3:12)'),
}


def main():
    with open(SRC, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    refs = [r['reference'] for r in rows]
    missing = [r for r in refs if r not in D]
    extra = [r for r in D if r not in refs]
    if missing or extra:
        print('missing:', missing)
        print('extra:', extra)
        sys.exit(1)
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['reference', 'b_words', 'other_mcodes', 'decision', 'group_or_forward',
                    'group_name', 'route', 'note', 'narrative_refs', 'text'])
        for r in rows:
            dec, grp, route, note = D[r['reference']]
            w.writerow([r['reference'], r['b_words'], r['other_mcodes'], dec, grp,
                        GROUPS.get(grp, ''), route, note, r['narrative_refs'], r['text']])
    from collections import Counter
    print(Counter(v[0] for v in D.values()))
    print(Counter(v[1] for v in D.values() if v[0] in ('read', 'carried') and v[1] in GROUPS))
    print('wrote', OUT, len(rows))


if __name__ == '__main__':
    main()
