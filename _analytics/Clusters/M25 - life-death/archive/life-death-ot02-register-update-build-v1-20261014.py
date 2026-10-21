"""Build the register update JSON for the OT-02 die/death/perish weave (check v2 section E).

Usage (repo root): python "_analytics/Clusters/M25 - life-death/life-death-ot02-register-update-build-v1-20261014.py" OUT.json
Each claim: (key, text, beyond_text, i_read, sources, [(chapter, passage opening, kind)]).
"""
import json, sys

C = []
def cl(key, text, beyond, sources, tells, i_read=False):
    C.append((key, text, beyond, i_read, sources, tells))

B, L, V, W = 'Breath lent', 'Life set before', 'Living before God', 'Life weighed'
# ---- Breath lent, and held by God
cl('r1', "Life is held in the breath, and the breath is God's to give and to take back", 'gathers the verses of God and the breath',
   ['Job 12:10', 'Daniel 5:23', 'Job 34:14-15', 'Psalm 104:29-30', 'Ecclesiastes 8:8'],
   [('2', "Life is held in the breath, and the breath is God's to give", 'in full')])
cl('r2', "When the breath goes, a person's plans go with it", 'reads "plans perish" as the thinking going with the breath',
   ['Psalm 146:4', 'Psalm 144:4', 'Psalm 94:11'], [('2', "Life is held in the breath, and the breath is God's to give", 'in part')])
cl('r3', 'God holds both ends, killing and making alive, and keeps alive between them', 'joins the "I kill and I make alive" sayings with the keeping alive',
   ['Deuteronomy 32:39', '1 Samuel 2:6', '2 Kings 5:7', 'Psalm 33:19', 'Job 36:6', 'Genesis 50:20', 'Deuteronomy 6:24'],
   [('2', 'God holds both ends', 'in full')])
cl('r4', 'The breath also gives understanding, and words come out on it', 'joins the understanding and the speaking verses of the breath',
   ['Job 32:8', 'Proverbs 20:27', 'Job 26:4', 'Proverbs 14:5'], [('2', 'The breath does more than keep a body going', 'in full')])
cl('r5', 'The breath can fail in someone still alive', 'sets two verses as one statement', ['Daniel 10:17', 'Jeremiah 4:31'],
   [('2', 'The breath can fail in a person who is still alive', 'in full')])
cl('r6', 'God gives human frailty as a reason for holding back his anger', 'joins Isaiah 57 and Psalm 78', ['Isaiah 57:16', 'Psalm 78:38-39', 'Psalm 90:9'],
   [('2', 'God gives this frailty as a reason for holding back his anger', 'in full')])
cl('r7', 'Humans and animals share one breath and one lot', 'gathers the verses', ['Ecclesiastes 3:19', 'Genesis 6:17', 'Genesis 7:22'],
   [('2', 'In this, humans and animals share one lot', 'in full')])
# ---- Life set before a person
cl('r8', 'Life and death are set before a person to choose; life is chosen by doing, seeking and holding on', 'gathers the commands that end "and live"',
   ['Deuteronomy 30:15', 'Deuteronomy 30:19', 'Deuteronomy 30:6', 'Leviticus 18:5', 'Deuteronomy 16:20', 'Proverbs 4:4', 'Proverbs 9:6', 'Amos 5:4', 'Amos 5:14', 'Habakkuk 2:4', 'Jeremiah 21:8'],
   [('2', 'Life is set before the inner being as something to choose', 'in full'), ('2', 'Death is set before a person just as plainly', 'in part')])
cl('r9', 'Long days are promised with some commands, and the Preacher sets the righteous who perish beside them; both are stated', 'sets the promise and the Preacher side by side',
   ['Exodus 20:12', 'Deuteronomy 6:2', '1 Peter 3:10', 'Ecclesiastes 7:15', 'Ecclesiastes 8:12'],
   [('2', 'Long days are promised with some of the commands', 'in part'), ('2', 'The Preacher sets another sight beside this', 'in full')])
cl('r10', 'Wisdom marks where the way to death ends, and some of what kills a person is named from within', 'gathers the wisdom sayings on the way to death',
   ['Proverbs 14:12', 'Proverbs 12:28', 'Proverbs 8:35-36', 'Proverbs 18:21', 'James 3:8', 'Job 5:2', 'Proverbs 21:25', 'Proverbs 5:23', 'Proverbs 15:10', 'Proverbs 19:16', 'Job 36:12'],
   [('2', 'Death is set before a person just as plainly', 'in full'), ('2', 'Some of what kills a person is named from within', 'in full'), ('2', 'Elihu says it of those who will not hear', 'in full')])
cl('r11', "God has no pleasure in anyone's death and calls for turning; the turning is a considered act that reaches back over the past, and trust can lean the wrong way", 'joins Ezekiel 18 and 33',
   ['Ezekiel 18:23', 'Ezekiel 18:32', 'Ezekiel 33:10-11', 'Ezekiel 18:28', 'Ezekiel 18:22', 'Ezekiel 18:24', 'Ezekiel 33:13'],
   [('2', 'God says what he wants', 'in full'), ('2', 'The turning is a considered act', 'in full')])
cl('r12', 'Life can be wrongly kept or taken by lying words', 'reads Ezekiel 13:19 as a general statement', ['Ezekiel 13:19'],
   [('2', 'Life can also be wrongly kept or taken by words', 'in full')])
cl('c12', 'The same message is death to one and life to another', 'states what 2 Corinthians 2:16 shows of how one thing changes character', ['2 Corinthians 2:16', '2 Corinthians 2:15'],
   [('2', 'The same word can be death to one and life to another', 'in full')])
cl('c14', "Another's death can be laid at a person's hand", 'reads the watchman as a general case', ['Ezekiel 33:8-9', 'Ezekiel 3:18-20'],
   [('2', "Another's death can be laid at a person's hand", 'in full'), ('10.10', "Another's death can be laid at one's hand", 'pointer')])
# ---- Living before God
cl('r13', 'The commonest form of the oath by life is "As the Lord lives" (39 verses); in six of them a second life is joined', 'a count over the oath verses (2026-10-14)',
   ['1 Samuel 20:3', '1 Samuel 25:26', '2 Kings 2:2', '2 Kings 2:4', '2 Kings 2:6', '2 Kings 4:30'],
   [('2', '"As the Lord lives" is its commonest form', 'in full')])
cl('r13b', 'The oath "As the Lord lives" places a promise before the living God and binds the speaker to it by life', 'reads what the oath does', ['1 Samuel 20:3', '2 Kings 2:2', '2 Samuel 15:21', '1 Kings 1:29', '1 Kings 17:1', 'Job 27:2'],
   [('2', 'The opening of this chapter said that life is lived before God', 'in part'), ('2', '"As the Lord lives" is its commonest form', 'in part')], i_read=True)
cl('r14', "The oath's words stay the same while the heart that speaks them differs; it is judged by how it is sworn", 'sets several oaths side by side',
   ['2 Samuel 12:5', '1 Samuel 14:45', '2 Kings 5:20', 'Jeremiah 5:2', 'Jeremiah 4:2'], [('2', 'The words of the oath stay the same', 'in full')])
cl('r15', 'God swears by his own life, and the oath carries what he wants and what he will do', 'gathers the "As I live" oaths', ['Ezekiel 33:11', 'Ezekiel 20:3', 'Romans 14:11'],
   [('2', 'God swears by his own life', 'in full')])
cl('r16', '"The living God" sets him against idols, which have no breath', 'joins the name with Habakkuk 2', ['Jeremiah 10:10', '1 Thessalonians 1:9', 'Habakkuk 2:18-20'],
   [('2', 'The one before whom life is lived is called', 'in full')])
cl('r16b', 'The inner being turns toward the living God, or away from him', 'gathers four verses', ['Psalm 42:2', 'Psalm 84:2', 'Hebrews 3:12', 'Hebrews 10:31'],
   [('2', 'The inner being turns toward him, or away from him', 'in full')])
cl('r17', 'Scripture counts a life in days and says what the days are for', 'gathers the "all the days" verses', ['Deuteronomy 4:10', 'Deuteronomy 17:19', 'Deuteronomy 16:3', 'Psalm 146:2', 'Psalm 27:4', 'Genesis 47:9'],
   [('2', 'Scripture counts a life in days', 'in full')])
cl('r18', 'The world where life is lived is named "the land of the living"', 'gathers the phrase', ['Psalm 27:13', 'Psalm 142:5', 'Isaiah 38:11', '1 Samuel 25:29'],
   [('2', 'The world where life is lived has its own name', 'in full')])
# ---- Life weighed
cl('r19', 'People weigh their own lives: loathed, worn down, enjoyed, and not consisting in possessions', 'gathers the verses that weigh a life',
   ['Job 10:1', 'Genesis 27:46', 'Ecclesiastes 2:17', 'Job 3:20', 'Psalm 31:10', 'Psalm 88:3', 'Psalm 88:15', 'Deuteronomy 28:66', '2 Corinthians 1:8', 'Ecclesiastes 9:4', 'Ecclesiastes 9:3', 'Psalm 143:2', 'Ecclesiastes 9:9', 'Ecclesiastes 5:20', 'Luke 12:15', '1 Timothy 6:19', '1 Corinthians 15:19', 'John 12:25'],
   [('2', 'Scripture lets people weigh their own lives', 'in full'), ('2', 'Life can be loathed', 'in part'), ('2', 'Life can be worn down', 'in part'), ('2', 'The living are weighed too', 'in part'), ('2', 'Life can be enjoyed', 'in part'), ('2', 'And Scripture says what life does not consist in', 'in part')])
cl('r20', 'Where the hope of seeing good has gone, life is weighed as a breath', 'joins Psalm 34:12 and Job 7:7', ['Psalm 34:12', 'Job 7:7'],
   [('2', 'The want for life is a want to see good', 'in full')], i_read=True)
cl('r21', 'The difference in how a life is weighed lies in what each verse sets life beside', 'reads the verses of Life weighed together', ['Job 10:1', 'Psalm 31:10', 'Ecclesiastes 9:9', 'Luke 12:15', 'John 12:25'],
   [('2', 'The same life is loathed, worn down, enjoyed and let go', 'in full')], i_read=True)
cl('c2', "Death's certainty can be turned into a reason to indulge, and Scripture answers it", 'joins Isaiah 22 and 1 Corinthians 15', ['Isaiah 22:13-14', '1 Corinthians 15:32'],
   [('2', "Death's certainty can be turned into a reason", 'in full')])
# ---- What death is
cl('c6', 'The law weighs a life by what it has begun, and names what a death can leave unfinished', 'reads Deuteronomy 20:5-7', ['Deuteronomy 20:5-7'],
   [('2', 'The law names what a death can leave unfinished', 'in full')], i_read=True)
cl('c1', 'What lies beyond death is not shown to a person', 'states the point of God\'s question to Job', ['Job 38:17'],
   [('2', 'What lies beyond death is not shown to a person', 'in full')])
cl('ga', 'Scripture speaks of death in more than one way: the body\'s death, death in the living, dying to sin, a death beyond death, death as a power, and the living made like the dead', 'sets the uses of the death words side by side (OT-02 check v2 section G)',
   ['Matthew 8:22', 'Luke 9:60', 'Ephesians 2:1', 'Romans 6:2', 'Revelation 2:11', 'Revelation 20:14', 'Revelation 21:8', 'Romans 5:14', '1 Corinthians 15:56', 'Matthew 28:4', 'Revelation 1:17'],
   [('2', "So far, death is the end of the body's life", 'in full'), ('2', 'The verses speak of death in these ways', 'in full')])
cl('gd', 'The father sets "dead" beside "lost" and "alive" beside "found"; to perish and to be lost are one word', 'joins Luke 15 with the perish verses',
   ['Luke 15:24', 'Luke 15:32', 'Luke 15:4', 'Luke 15:8', 'John 3:16', 'Luke 19:10'],
   [('2', 'The father of the son who came home says', 'in full')])
cl('gb', '"Dead in" trespasses and "died to" sin are opposites: death under sin, and death that ends its rule', 'sets Ephesians 2 and Colossians 2 beside Romans 6 and 7 (3 and 6 verses)',
   ['Ephesians 2:1', 'Ephesians 2:5', 'Colossians 2:13', 'Romans 6:2', 'Romans 6:7', 'Romans 6:10', 'Romans 6:11', 'Romans 7:4', 'Galatians 2:19', '1 Peter 2:24'],
   [('2', 'The same word changes character with what it is joined to', 'in full'), ('2', 'It is the opposite of being dead in sin', 'in full')])
cl('gc', 'The word "dead" passes to sin itself, to faith and to works', 'gathers the uses', ['Romans 7:8-9', 'James 2:17', 'James 2:26', 'Hebrews 6:1', 'Hebrews 9:14', 'Romans 8:10'],
   [('2', 'The same word changes character with what it is joined to', 'in part'), ('2', 'Scripture also speaks of death inside a living person', 'in part')])
cl('ge', 'Some are perishing now, set against being saved; what is set against perishing is eternal life', 'gathers the present perishing verses',
   ['1 Corinthians 1:18', '2 Corinthians 2:15', '2 Corinthians 4:3', '2 Thessalonians 2:10', 'Luke 13:3', 'Luke 13:5', 'John 3:16', 'John 10:28'],
   [('2', 'Perishing is spoken of in the same way', 'in full')])
# ---- Death and sin
cl('gj', 'Where a verse sets death against eternal life (Romans 6:23) it speaks of more than the body\'s death; other verses do not say which death, and are left as written', 'reads Romans 6:23 by its opposite',
   ['Romans 6:23', 'James 1:15', 'Romans 8:13', 'Ezekiel 18:4'], [('2', 'These verses do not always say which death they mean', 'in full')], i_read=True)
cl('c9a', 'In Acts a lie contrived in the heart is followed at once by death, and fear comes on all who hear', 'joins Acts 5:3-11', ['Acts 5:3-5', 'Acts 5:10-11'],
   [('2', 'In Acts a lie is followed at once by death', 'in full'), ('2', 'A death can bring fear on others', 'in full')])
# ---- Death in the living
cl('gh', 'Inner things can perish: hope, endurance, courage (the heart), wisdom and truth', 'gathers the perish verses said of inner things',
   ['Job 8:13', 'Lamentations 3:18', 'Ezekiel 37:11', 'Jeremiah 4:9', 'Isaiah 29:14', 'Jeremiah 7:28', 'Ecclesiastes 7:7'],
   [('2', 'Scripture also speaks of death inside a living person', 'in part')])
cl('gf', 'The verses name what brings death in the living, each in its own place; no verse gathers them into one list', 'gathers the stated causes without joining them',
   ['Ephesians 2:1', 'Colossians 2:13', '1 Timothy 5:6', 'Revelation 3:1', '1 John 3:14', 'Romans 8:6', 'Romans 7:13', '2 Corinthians 7:10', '2 Corinthians 3:6', 'Proverbs 8:36'],
   [('2', 'The verses name what brings it, each in its own place', 'in full'), ('2', 'No verse gathers these into one list', 'in full')])
cl('gg', 'The verses name the way out of death in the living: hearing the Son and believing, God making alive with forgiveness, waking, coming home; loving the brothers is its sign', 'gathers the way-out verses',
   ['John 5:24-25', 'Colossians 2:13', 'Ephesians 5:14', 'Luke 15:17-24', '1 John 3:14'], [('2', 'The verses also name the way out', 'in full')])
cl('gi', "One person's freedom can destroy another", 'joins 1 Corinthians 8 and Romans 14', ['1 Corinthians 8:11', 'Romans 14:15'],
   [('2', 'One person can bring it on another', 'in full')])
cl('gk', 'The believer has already died to sin, to the law and to the powers of the world, and a putting to death is still to be done', 'gathers the dying-to verses',
   ['Romans 6:2-3', 'Romans 6:7', 'Romans 6:11', 'Romans 7:4', 'Galatians 2:19', 'Colossians 2:20', '2 Timothy 2:11', '2 Corinthians 5:14', 'Colossians 3:5', 'Romans 8:13', '2 Corinthians 4:10'],
   [('2', 'Paul speaks of a death the believer has already died', 'in full'), ('2', 'This death is spoken of as done', 'in full'), ('14', 'Died to sin, and to the law', 'pointer')])
# ---- Sleep and waking
cl('gs', 'Kings and Chronicles tell the deaths of kings as sleeping with their fathers (36 verses)', 'a count of "slept with his fathers" (2026-10-14)',
   ['1 Kings 2:10', '1 Kings 11:43', '2 Kings 20:21', '2 Chronicles 32:33'],
   [('2', 'The books of Kings and Chronicles tell the deaths of kings this way', 'in full')])
# ---- Facing death
cl('r22', 'The coming of death is often met with anguish and terror, and the fear of dying shapes what people do', 'gathers the verses of the inner being under the coming of death',
   ['Psalm 55:4', '1 Samuel 20:3', 'Psalm 13:3', 'Matthew 26:38', 'Genesis 26:9', 'Genesis 38:11', 'Genesis 19:19', 'Numbers 17:12-13', '1 Samuel 15:32', 'Isaiah 51:12', 'Hebrews 2:14-15'],
   [('2', 'Scripture shows the inner being under the coming of death', 'in full'), ('2', 'The fear of dying shapes what people do', 'in full')])
cl('c9b', '"The king of terrors" is Bildad\'s word, said of Job, and God\'s verdict on the friends stands over it', 'sets Job 18:14 under Job 42:7', ['Job 18:14', 'Job 42:7', 'Ecclesiastes 12:5'],
   [('2', 'Bildad says the wicked man', 'in full')])
cl('r23', 'The nearness of death is given a purpose: to rely on God who raises the dead', 'joins 2 Corinthians 1:9 and Hebrews 5:7', ['2 Corinthians 1:9', 'Hebrews 5:7', '1 Corinthians 4:9'],
   [('2', 'Paul gives the nearness of death a purpose', 'in full')])
# ---- Those left behind
cl('c7', 'A death is met by those who remain: grief, not watching, fasting and then eating, reproach, limits on mourning, mourning withheld, and death not taken to heart', 'gathers the verses of those left behind',
   ['Genesis 21:16', '2 Samuel 12:21-23', '2 Samuel 19:6', 'John 11:21', 'Luke 7:12-15', 'Philippians 2:27', '2 Samuel 11:26', 'Genesis 48:7', 'Deuteronomy 14:1', 'Jeremiah 16:4', 'Jeremiah 16:7', 'Isaiah 57:1', 'Jeremiah 34:5', '1 Thessalonians 4:13'],
   [('2', 'A death is met by those who remain', 'in full'), ('2', 'The law limits the mourning', 'in full'), ('2', 'Paul does not forbid the grief', 'in part')])
# ---- Wanting to die
cl('r24', 'People sometimes want to die; of the 24 verses with such a wish, 17 name no inner word', 'a count over the wish-to-die verses (2026-10-14)',
   ['1 Kings 19:4', 'Jonah 4:3', 'Job 7:15-16', '2 Samuel 1:9', 'Judges 16:30', 'Job 3:21', 'Job 3:11', 'Job 10:18', 'Jeremiah 20:14-18', 'Genesis 30:1', 'Ecclesiastes 4:2', 'Numbers 20:3'],
   [('2', 'Scripture is honest that people sometimes want to die', 'in full')])
cl('r25', 'Of the seven wishes to die answered in these passages, two are fed, two are answered another way, and three are granted, each to a man already blinded or wounded', 'a count over the answered wishes',
   ['1 Kings 19:4-8', 'Jonah 4:3', 'Jonah 4:9-11', 'Exodus 16:3-4', 'Numbers 21:5-8', 'Judges 16:21', 'Judges 16:30', 'Judges 9:54', '2 Samuel 1:9-16'],
   [('2', 'Of the wishes in this section, four are answered', 'in full'), ('2', 'Three are granted, each to a man already blinded', 'in full'), ('2', 'So, of the seven', 'in full')])
# ---- Made alive
cl('r26', 'Giving life belongs to the Father, the Son and the Spirit', 'gathers four verses', ['John 5:21', 'Romans 4:17', 'John 6:63', '2 Corinthians 3:6'],
   [('2', 'In the New Testament, giving life belongs to the Father', 'in full')])
cl('r27', 'The dead made alive are living people; the crossing from death to life happens now, and life is spoken of as had now and still to come', 'joins Paul and John',
   ['Colossians 2:13', 'Ephesians 2:5', 'John 5:24', 'John 8:51', 'John 11:26', 'John 6:47', '1 John 5:13', 'Mark 10:30', '1 John 3:14', 'Romans 6:4', 'Colossians 3:3', 'John 6:50', 'Hebrews 11:5'],
   [('2', 'In these verses the dead who are made alive are living people', 'in full')])
cl('r28', 'The making alive rests on a death, and Christ went to it himself', 'joins the verses of his death',
   ['1 Corinthians 15:3', 'Romans 5:8', 'Hebrews 2:9', 'Zechariah 13:7', 'Matthew 26:31', 'Isaiah 53:12', 'Philippians 2:8', 'Romans 6:9-10'],
   [('2', 'The making alive rests on a death', 'in full'), ('2', 'He went to that death himself', 'in full')])
cl('r29', 'That death changes how the living live: no longer for themselves, dead to sin, Christ living in them', 'joins Paul and Peter',
   ['2 Corinthians 5:14-15', 'Galatians 2:19-20', 'Romans 12:1', '1 Peter 2:24'],
   [('2', 'Paul says what that death means for those who live', 'in full'), ('2', 'Paul says who lives in the one made alive', 'in full')])
# ---- Dying to the Lord
cl('r30', 'A death, too, can belong to the Lord, and a dying can go on while a person lives', 'joins Romans 14 with Paul\'s own words',
   ['Romans 14:7-9', 'Philippians 1:20-21', '1 Corinthians 3:22', '1 Corinthians 15:31', '2 Corinthians 4:11', '2 Corinthians 6:9', '2 Corinthians 4:12'],
   [('2', 'Death, too, can belong to the Lord', 'in full')])
cl('r31', 'Scripture speaks of the death of the upright in its own words: precious, wished for, a refuge, in faith, bearing fruit, glorifying God', 'gathers the verses without making one a heading for the rest',
   ['Psalm 116:15', 'Numbers 23:10', 'Proverbs 14:32', 'Hebrews 11:13', 'Hebrews 11:4', 'John 12:24', 'John 21:19'],
   [('2', 'Scripture speaks of the death of the upright in its own words', 'in full')])
cl('c4', 'Some wait to see one thing before they die, and then let go', 'joins Simeon and Jacob', ['Luke 2:26', 'Luke 2:29', 'Genesis 45:28', 'Genesis 46:30'],
   [('2', 'Some wait to see one thing before they die', 'in full')])
cl('c5', 'People hold to someone, or to something, even to death, and the readiness can fail', 'gathers the verses of readiness to die',
   ['Ruth 1:17', 'Joshua 2:14', '1 Samuel 14:43', 'Esther 4:16', 'John 11:16', 'Job 27:5', '1 Corinthians 9:15', 'Revelation 2:10', 'Revelation 12:11', 'Luke 22:33-34', 'Mark 14:31'],
   [('2', 'Others hold to someone, or to something, even to death', 'in full'), ('2', 'The readiness can fail', 'in full'), ('10.10', 'Loyalty can be held even to death', 'pointer')])
# ---- After death
cl('c19', 'The living are told how to deal with the dead: inquiring of them and offering to them are forbidden; kindness to the dead is blessed', 'gathers the verses',
   ['Deuteronomy 18:11', 'Psalm 106:28', 'Ruth 1:8'], [('2', 'The living are told how to deal with the dead', 'in full')])

claims, tellings = [], []
for key, text, beyond, iread, src, tells in C:
    claims.append({'key': key, 'new': {'text': text, 'beyond_text': beyond, 'origin': 'narrative', 'verdict': 'New',
                                      'i_read': iread, 'sources': src}})
    for ch, opening, kind in tells:
        tellings.append({'claim': key, 'chapter': ch, 'passage': opening, 'kind': kind})

data = {
  'update': {
    'update_date': '2026-10-14',
    'title': 'OT-02 die, dead and perish words: Ch 2 death part rebuilt, claims registered',
    'strand': 'life and death (M25), OT-02 Q1 What is death?',
    'researcher_instruction': '"proceed with the weave as proposed, include the perish pull. What I am seeing is encouraging that we heading in right direction." (2026-10-14), on check v2; earlier: "check the completeness and validity of existing claims, check narration for unsubstantiated or unrecorded claims, and check the verses for perspectives that were missed in the first round"; "have you adequately recognised the different perspectives of death related to \'spiritual death\', \'dead to sin\', \'causes of death\'"',
    'method': 'Die/death words (H4191, H4194, G0599, G2288) checked against the claims and Ch 2 by unit-2 face; the dead/die words hidden in T-codes (G3498 and 16 others, 250 verses) and the perish words (H0006, G0622, G0684, 271 verses) pulled and read. Ch 2 death part rebuilt by kind of death (Death spoken of in more than one way; Death in the living with stated causes and the way out; new Dead to sin; new Those left behind); 10 statements corrected (OT-02.10 counts); 31 + 16 claims registered with tellings. Pointers in 10.10, 10.12 (working note removed), 12 and 14.',
    'source_files': ['_analytics/Clusters/M25 - life-death/life-death-ot02-die-death-check-v2-20261014.md',
                     '_analytics/Clusters/M25 - life-death/life-death-ot02-die-death-face-coverage-v1-20261014.csv',
                     '_analytics/Clusters/M25 - life-death/life-death-ot02-dead-words-pull-v1-20261014.csv',
                     '_analytics/Clusters/M25 - life-death/life-death-ot02-perish-pull-v1-20261014.csv'],
    'scripts': ['_analytics/Clusters/M25 - life-death/life-death-ot02-ch2-v25-weave-v1-20261014.py',
                '_analytics/Clusters/M25 - life-death/life-death-ot02-face-coverage-v1-20261014.py',
                '_analytics/Clusters/M25 - life-death/life-death-ot02-register-update-build-v1-20261014.py',
                '_analytics/Clusters/M25 - life-death/narrative-quote-check-v1-20261014.py'],
    'structure_change': 'Ch 2: new subsections "Death spoken of in more than one way" and "Dead to sin" under What death is; new section "Those left behind" before Wanting to die',
    'structure_reason': 'The death words were read by face, not by which death; the kinds, the dead-in/dead-to change and the stated causes had no one account; Ch 2 had no place for death as the living meet it in another',
    'quote_parts': 259, 'quote_failures': 0,
    'quote_note': 'the 8 non-matches are section names in quotation marks, not Scripture',
  },
  'refs': [{'kind': 'thread', 'value': 'OT-02'}],
  'chapters': [
    {'chapter': '2', 'from_version': 24, 'to_version': 25, 'file': '02-life-breath-and-death-v25-20261014.md'},
    {'chapter': '10.10', 'from_version': 25, 'to_version': 26, 'file': '10-10-relating-to-others-v26-20261014.md'},
    {'chapter': '10.12', 'from_version': 9, 'to_version': 10, 'file': '10-12-fear-v10-20261014.md'},
    {'chapter': '12', 'from_version': 21, 'to_version': 22, 'file': '12-when-the-inner-being-goes-wrong-v22-20261014.md'},
    {'chapter': '14', 'from_version': 16, 'to_version': 17, 'file': '14-made-new-v17-20261014.md'}],
  'claims': claims, 'tellings': tellings,
}
json.dump(data, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(claims)} claims, {len(tellings)} tellings -> {sys.argv[1]}')
