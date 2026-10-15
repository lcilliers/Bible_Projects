"""Builds the narrative-register update JSON for the M09 humility weave (#2148).

Researcher, 2026-10-15, verbatim: "excellent work.  bring the narrative up to date, and ensure that the
claims register / narrative is updated". Writes m09-humility-register-update-v1-20261015.json for
`iba\\app\\ps\\Narrative-Register.ps1 -Action Record -File <json> -By Claude`.
Every new claim is a statement in the new text that goes beyond its verses (rule 77); readings marked
"I read" in the text carry i_read true.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
P = 'm09-humbling'
SRC = [f'_analytics/Clusters/M09 - humility-lowliness/{f}' for f in (
    'm09-cluster-overview-v3-20261015.md', 'm09-no-other-mcode-reading-v1-20261015.md',
    'm09-humbling-fanout-scope-v1-20261015.md', 'm09-humbling-batch1-reading-v1-20261015.md',
    'm09-humbling-batch2-reading-v1-20261015.md', 'm09-humbling-batch3-reading-v1-20261015.md',
    'm09-humbling-batch4-reading-v1-20261015.md', 'm09-humbling-batch5-reading-v1-20261015.md',
    'm09-humbling-ot-nt-and-jesus-v1-20261015.md', 'm09-humbling-crosscheck-v1-20261015.md',
    'm09-humility-narrative-placement-proposal-v1-20261015.md')]
SCRIPTS = [f'_analytics/Clusters/M09 - humility-lowliness/{f}' for f in (
    'm09-humbling-fanout-pull-v1-20261015.py', 'm09-humbling-crosscheck-pull-v1-20261015.py',
    'm09-humility-weave-v1-20261015.py', 'm09-humility-register-update-build-v1-20261015.py')]

update = {
    'update_date': '2026-10-15',
    'title': 'M09 humility: 10.14 Humility written, angles woven into their chapters, four corrections',
    'strand': 'humility (M09), fan-out of humbling oneself (#2148)',
    'researcher_instruction': '"excellent work.  bring the narrative up to date, and ensure that the claims register / narrative is updated" (2026-10-15); placement: "Your recommendation. Ch 14 might expand in scope as we move forward, but it needs its own chapter to encapsulate it properly.  It does have many different  angles that need to be woven onto those chapters in context of each angle."; "humility is not a feeling"; "Jesus is part of divinity and need attention in Ch 13"',
    'method': 'Humbling oneself fanned out across clusters (218 verses: the M09 words and the humility, meekness, contrite and submission words filed in M05, M10, M23, M24, M53, M73, M75, T2, T3), read in five batches by passage; the 27 no-other-M-code verses read; OT/NT comparison and the role of Jesus; cross-check against the narrative, register, M08 and M47. New 10.14 Humility holds the full account; each angle woven into its chapter in context (10.2, 10.7, 10.9, 10.10, Ch 4, 5, 6, 11, 12, 13.1), pointers in 10.1, 10.12, 10.13, 10.0. Cross-check corrections: Ch 12 "weighed most" (uncounted superlative removed); Mic 6:8 taken out of the anger-at-wrong-to-the-weak statements in 10.8 and 10.13 and placed for what it says; Ch 11 "rest that passes from his heart to ours" restated to the verse; Ch 14 held bullet "seven conditions for the Spirit\'s work" (2Ch 7:14) removed, the verse now told in 10.14, claim 10-5 withdrawn. Correction 5 (claim 1-1 sources) needs no change: the claim was widened to heart // spirit on first record.',
    'source_files': SRC,
    'scripts': SCRIPTS,
    'claims_changed_note': '37 new claims (10.14, 13.1); 10-5 withdrawn',
    'not_woven_note': 'The poor and needy are carried by threads OT-105 (the poor as seen by another) and OT-106 (the poor person\'s own side), not woven. The serve/servant words (Mar 10:45; Joh 13; 2Cor 8:9) were not pulled. Ch 1 outline (#2111) not touched.',
    'structure_change': 'New sub-chapter 10.14 Humility (reading order after 10.13). New sections: 10.2 Humility and hearing; 10.7 Taking the lower place; 10.9 Humbling oneself before God; 10.10 Humility toward one another; Ch 4 The heart humbled; Ch 5 Rest for the soul; 13.1 Lowering himself. Ch 6 gains a paragraph (It is gentle, and it is under the person); Ch 11 s4 a face (Who lowers whom, and before whom); Ch 12 the counterpart paragraph. 10.0 names 10.12 to 10.14.',
    'structure_reason': 'Humility is not a feeling (researcher); the readings show it as act, standing, sought quality, state of spirit, place taken, done to a person and God\'s own way, across the activities. A key characteristic gets one full account as its own Ch 10 sub-chapter (#1961), with each angle woven in context (#1920).',
    'quote_parts': 361,
    'quote_failures': 0,
    'quote_note': 'every quoted part in the added lines of the 17 files checked against iba.db verse text in chapter order, case-insensitive (capitals at the start of a quote only)',
    'notes': 'The 10.14 chapter row was added directly to narrative_chapter (reading_order 25, later chapters +1) because no Narrative-Register action adds a chapter.',
}

claims, tellings = [], []
def claim(key, text, beyond, sources, i_read=False):
    claims.append({'key': key, 'new': {'text': text, 'beyond_text': beyond, 'origin': 'narrative',
                                       'verdict': 'New', 'i_read': i_read, 'sources': sources}})
def tell(key, chapter, passage, kind='in full', part=None):
    t = {'claim': key, 'chapter': chapter, 'passage': passage, 'kind': kind, 'action': 'add'}
    if part: t['part'] = part
    tellings.append(t)

H = '10.14'
claim('h1', 'Humility is not a feeling in the verses; they speak of it as an act, a standing, a quality sought and walked in, a state of the spirit, a place taken, something done to a person, and God\'s own way',
      'gathers the faces of humility across the humbling words; no verse read says a person feels humble',
      ['Zephaniah 2:3', 'Micah 6:8', 'Isaiah 57:15', 'Luke 14:10', 'Deuteronomy 8:2', 'Psalm 113:6', 'Philippians 2:8', '2 Kings 22:19'])
tell('h1', H, 'Humility is not a feeling in the verses.')
claim('h2', 'Humility is always set against a rising: the proud heart, the lifted-up self, the stiff neck, the haughty eyes',
      'reads the opposite named beside humbling in every face as one setting',
      ['2 Chronicles 32:25-26', 'Daniel 5:20-23', '2 Chronicles 36:12-13', 'Isaiah 2:11', 'Proverbs 18:12'])
tell('h2', H, 'In every one of these the verses set humility against a rising')
tell('h2', '12', 'The counterpart is humbling oneself', 'pointer')
claim('h3', 'Humbling oneself is done before someone: God, or the prophet who carries his word',
      'joins the "before" of each account; reads Zedekiah\'s refusal of the prophet as refusal of the word',
      ['1 Kings 21:29', '2 Kings 22:19', '2 Chronicles 33:12', 'Daniel 10:12', '2 Chronicles 36:12'])
tell('h3', H, 'Humbling oneself is never done in the air.')
tell('h3', '10.9', 'One way a person comes before God is by lowering himself.', 'in part', 'done before him, or before his word')
claim('h4', 'Most often a person humbles himself when a word reaches him, and the humbling owns that God is right',
      'counts the accounts in which a word comes first; reads "The Lord is righteous" as what the humbling says',
      ['2 Chronicles 12:5-6', '2 Kings 22:19', '1 Kings 21:27', 'Daniel 5:22'])
tell('h4', H, 'Most often a person humbles himself when a word reaches him.')
tell('h4', '10.9', 'One way a person comes before God is by lowering himself.', 'in part', 'its words own that God is right')
claim('h5', 'Humbling happens in the heart; Hezekiah\'s is the same heart turning back from its own pride',
      'places the act in the heart from the heart named in each verse; reads 2Ch 32:25-26 as one heart in two directions',
      ['2 Kings 22:19', '2 Chronicles 34:27', 'Leviticus 26:41', '2 Chronicles 32:25-26', 'Daniel 10:12', 'Daniel 5:22'], True)
tell('h5', H, 'The verses place it in the heart.')
tell('h5', '04', 'The heart is where a person humbles himself.')
tell('h5', '12', 'The counterpart is humbling oneself', 'in part', 'Hezekiah and Belshazzar')
claim('h6', 'The one who exalts himself measures himself against others and lists what he does; the one who humbles himself owns that he is a sinner and asks for mercy',
      'reads the two prayers of the parable as the two acts', ['Luke 18:9-14'])
tell('h6', H, 'Jesus gives it a face.')
claim('h7', 'To humble oneself under God\'s hand is also to put down what one carries, because he cares; the lifting is his to time',
      'joins humbling and casting anxieties in 1Pe 5:6-7 as one act', ['1 Peter 5:6-7', 'James 4:7-10'])
tell('h7', H, 'James and Peter say it as a run of commands.')
tell('h7', '10.9', 'God is said to see it.', 'in part', 'puts down what he carries')
claim('h8', 'Distress does not decide whether a person humbles himself; the same pressure or call meets two hearts, and the verses do not say why',
      'sets Manasseh beside Ahaz and the scorners beside those who came', ['2 Chronicles 33:12', '2 Chronicles 28:22', '2 Chronicles 30:10-11', '2 Chronicles 33:23'])
tell('h8', H, 'Manasseh, captured and bound')
tell('h8', H, 'When Hezekiah\'s couriers carried the call', 'in part', 'the same call met two hearts')
tell('h8', H, 'Nor does it pass from father to son.', 'in part', 'Amon')
claim('h9', 'God sees the one who humbles himself and answers, in measure; the humbling does not hold by itself',
      'gathers the seeing, the measured answers and Rehoboam\'s relapse',
      ['2 Chronicles 12:7-8', '2 Chronicles 12:12', '2 Chronicles 12:14', '1 Kings 21:29', '2 Kings 22:19-20', '2 Chronicles 33:13'])
tell('h9', H, 'The answer is real, and it is measured.')
tell('h9', H, 'It does not hold by itself.', 'in part', 'Rehoboam')
tell('h9', '10.9', 'God is said to see it.', 'in part', 'God sees it')
claim('h10', 'The humbling God does not take knowledge of is kept alongside self-pleasure and oppression and leaves the seen naked uncovered; Ahab\'s, against himself when the word came, was answered',
      'compares Isa 58 with 1Ki 21 and reads the difference in what goes with the acts', ['Isaiah 58:3-7', '1 Kings 21:27-29'], True)
tell('h10', H, 'Ahab\'s sackcloth and fasting were seen and answered')
claim('h11', 'What looks like lowering can puff a person up', 'reads the humility noun as "asceticism" in Col 2 beside the Pharisee\'s fasting',
      ['Colossians 2:18', 'Colossians 2:23', 'Luke 18:12'])
tell('h11', H, 'The New Testament names the same thing.')
claim('h12', 'God humbles to show what is in the heart, to teach what a person lives by, and to do him good in the end, against the heart that lifts itself up in plenty',
      'gathers the stated purposes of God\'s humbling', ['Deuteronomy 8:2-3', 'Deuteronomy 8:14-17', 'Deuteronomy 9:4', 'Psalm 107:11-13', 'Hebrews 12:9-11'])
tell('h12', H, 'To show the heart, and to teach.')
tell('h12', '04', 'God humbles too, and what he reaches is the heart', 'in part', 'testing the heart; hearts bowed down')
claim('h13', 'Being humbled by God can turn a person or harden him', 'sets Ahaz beside Manasseh', ['2 Chronicles 28:19', '2 Chronicles 28:22', '2 Chronicles 33:11-12'])
tell('h13', H, 'Being humbled can turn a person, or harden him.')
claim('h14', 'What God brings low is a bearing, haughty looks and lofty pride, not only a rank, so that the Lord alone is exalted',
      'reads the objects named in the bringing low as a bearing', ['Isaiah 2:7-17', 'Isaiah 5:15', 'Isaiah 13:11', '2 Samuel 22:28'])
tell('h14', H, 'What is brought low is a bearing, not only a rank.')
tell('h14', H, 'In Isaiah the setting is a land', 'in part', 'the lifted-up thing made to give way')
tell('h14', '12', 'The counterpart is humbling oneself', 'in part', 'the day against pride')
claim('h15', 'Only God lifts up and puts down; a person cannot abase the proud', 'joins the challenge to Job with Psa 75', ['Job 40:11-14', 'Psalm 75:6-7', '1 Samuel 2:7'])
tell('h15', H, 'Only God does it.')
claim('h16', 'The boast is moved from what a person has to what God does', 'reads Jam 1:9-10 and 1Co 1:28-31 together', ['James 1:9-10', '1 Corinthians 1:28-31'], True)
tell('h16', H, 'Where the boast goes.')
claim('h17', 'Humility is not held once for all: the humble are told to seek it', 'reads "all you humble … seek humility"', ['Zephaniah 2:3', 'Zephaniah 3:12-13'], True)
tell('h17', H, 'They seek.')
claim('h18', 'The humble are glad at what God did for another', 'reads both psalms as one man\'s rescue made others\' gladness', ['Psalm 34:2', 'Psalm 34:4', 'Psalm 69:29-32'])
tell('h18', H, 'They are glad at what God did for another.')
claim('h19', 'The humble are the teachable, and the teachable own their guilt', 'reads Psa 25:9 with the speaker\'s own prayer for pardon', ['Psalm 25:7-11'], True)
tell('h19', H, 'They are taught.')
claim('h20', 'Meekness stands where another provokes and leaves the answer to God', 'reads Psa 37 and Num 12 together', ['Psalm 37:7-11', 'Numbers 12:1-8', 'Matthew 5:5'], True)
tell('h20', H, 'The meek, where another provokes.')
claim('h21', 'Humility goes with the ear that can take a reproof and a word, and does not answer before it hears',
      'reads the verses set beside "humility comes before honor" as one', ['Proverbs 15:31-33', 'Proverbs 18:12-13', 'James 1:19-21', 'Isaiah 66:2'], True)
tell('h21', H, 'With hearing.')
tell('h21', H, 'I read humility, in these verses, as the ear', 'in part')
tell('h21', '10.2', 'Twice Proverbs says "humility comes before honor"')
claim('h22', 'In four passages what God looks to is set against a religious act; the offering follows the broken heart',
      'counts the four passages; reads Psa 51:19 as the offering following', ['Isaiah 58:3-7', 'Micah 6:6-8', 'Isaiah 66:1-3', 'Psalm 51:16-19'])
tell('h22', H, 'Instead of the offering.')
tell('h22', H, 'Walking with God.', 'in part', 'what to bring, and a way to walk')
tell('h22', H, 'The psalm goes on', 'in part')
claim('h23', 'Where God and a broken heart meet he is near and heals; the verses tell the breaking by its cause and by whether it is brought to God, not by naming contrition or despair',
      'gathers the broken-heart verses by cause and outcome',
      ['Psalm 34:18', 'Psalm 147:3', 'Isaiah 61:1', 'Isaiah 57:15-16', 'Psalm 38:4-9', 'Psalm 51:17', 'Psalm 69:20', 'Psalm 109:22', 'Exodus 6:9', 'Jeremiah 23:9', 'Proverbs 15:13', 'Proverbs 18:14'])
tell('h23', H, 'Where God and a broken heart meet in these verses')
tell('h23', H, 'The breaking has more than one cause.')
tell('h23', H, 'The verses do not divide contrition from despair by name.')
tell('h23', '04', 'The heart can be broken.', 'in part')
claim('h24', 'Humility between people is a way of counting the other, worn toward them, and named with bearing with and forgiving',
      'gathers the humility-toward-one-another verses', ['Philippians 2:3-4', 'Romans 12:16', 'Colossians 3:12-13', '1 Peter 5:5', 'Ephesians 4:2-3', '1 Peter 3:8'])
tell('h24', H, 'Counting others.')
tell('h24', H, 'Worn. Put on then')
tell('h24', '10.10', 'Between people, humility is a way of counting the other')
claim('h25', 'The lower place is taken before anyone gives it; the honour is given, not taken',
      'reads the seat, the title and the child together', ['Luke 14:7-11', 'Proverbs 25:6-7', 'Matthew 23:8-12', 'Matthew 18:4'])
tell('h25', H, 'The seat and the title.')
tell('h25', '10.7', 'Some choices are choices of place.')
claim('h26', 'Gentleness in meeting a wrong is joined to watching oneself, remembering what one was, and leaving the outcome to God',
      'gathers what the gentleness verses join to it', ['Galatians 6:1-3', '2 Timothy 2:25', '1 Peter 3:15', 'Titus 3:2-3'])
tell('h26', H, 'In meeting someone who is wrong.')
tell('h26', H, 'What these verses join to gentleness')
tell('h26', '10.10', 'It shows in how a wrong is met')
claim('h27', 'Submitting to God and humbling oneself are said as one', 'reads Jam 4:7-10 as one run', ['James 4:7-10'])
tell('h27', H, 'To God. Submit yourselves therefore to God')
tell('h27', '10.9', 'God is said to see it.', 'in part', 'submitting and drawing near')
claim('h28', 'Submission among people is told with a ground that faces God and, where the passage goes on, with a duty on the other side',
      'counts the grounds and the paired duties', ['Ephesians 5:21-25', 'Colossians 3:18-19', '1 Peter 2:13-21', '1 Peter 3:1-7', '1 Peter 5:3-5', 'Romans 13:5', 'Hebrews 13:17'])
tell('h28', H, 'To one another, for a reason that faces God.')
tell('h28', H, 'Where the passage goes on, it lays a duty on the other side')
tell('h28', '10.10', 'It is also a submission that runs both ways')
claim('h29', 'Refusing submission is right where the truth of the gospel is at stake', 'reads Gal 2:5 as the limit', ['Galatians 2:4-5'])
tell('h29', H, 'The limit.')
claim('h30', 'One\'s own spirit is under the person: the one who speaks governs what moves in him', 'reads 1Co 14:32 as submission inward', ['1 Corinthians 14:32-33'], True)
tell('h30', H, 'One\'s own spirit.')
tell('h30', '06', 'It is gentle, and it is under the person.', 'in part', 'the spirits of prophets subject to prophets')
claim('h31', 'In the New Testament humility rests on what is said of Jesus; the saying he taught, that whoever humbles himself will be exalted, is what is told of him',
      'ties Phi 2:8-9 and Heb 2:9 back to the saying in the Gospels', ['Philippians 2:3-9', 'Hebrews 2:9', 'Luke 18:14', 'Matthew 23:12', 'Matthew 11:29'], True)
tell('h31', H, 'In the New Testament, humility rests on what the verses say of Jesus.')
tell('h31', H, 'He humbled himself, and was exalted.')
claim('h32', 'Jesus is given as the ground and example of humility toward others', 'gathers the verses that name him as the ground',
      ['Philippians 2:3-5', '1 Peter 2:21', 'Ephesians 5:21', '2 Corinthians 10:1'])
tell('h32', H, 'He is the ground of humility toward others.')
tell('h32', '10.10', 'It is also a submission that runs both ways', 'in part', 'the ground is this mind')
claim('h33', 'John\'s lowering of himself before Jesus is said with joy', 'reads Joh 3:30 with 3:28-29', ['John 3:28-30'])
tell('h33', H, 'Others lower themselves before him.')
claim('h34', 'The same lines of humility run through both Testaments; the New differs in emphasis, adding humility toward one another, and in one new thing, Christ, in whom God\'s lowering is done in a human life',
      'compares the readings of the two Testaments', ['Proverbs 3:34', 'James 4:6', 'Zechariah 9:9', 'Matthew 21:4-5', 'Psalm 8:5-6', 'Hebrews 2:6-9', 'Philippians 2:3-8', '2 Chronicles 12:7'], True)
tell('h34', H, 'Everything above is in both Testaments')
tell('h34', H, 'Before God, then also toward one another.')
tell('h34', H, 'The new thing: Christ.')
claim('h35', 'Humility changes character with who acts, toward whom, and to what end',
      'sets the faces of the same words side by side', ['Judges 3:30', '2 Chronicles 12:7', 'Colossians 2:18', '2 Corinthians 10:1', 'Philippians 4:12', 'Galatians 2:5'])
tell('h35', H, 'The same words wear different faces.')
tell('h35', '11', 'Who lowers whom, and before whom.')
claim('h36', 'The lowering that the Old Testament tells of God is done in the Son in a human life',
      'reads God\'s looking down, dwelling with the lowly, gentleness and being broken beside the Son\'s emptying and humbling',
      ['Psalm 113:5-7', 'Psalm 138:6', 'Isaiah 57:15', '2 Samuel 22:36', 'Ezekiel 6:9', 'Philippians 2:6-9', 'Matthew 11:29', 'Hebrews 2:9', '1 Corinthians 15:28'], True)
tell('h36', '13.1', 'I read the lowering that the Old Testament tells of God')
tell('h36', '13.1', 'The Lord is high, and the verses keep saying that he looks low.', 'in part')
tell('h36', H, 'The new thing: Christ.', 'in part', 'what God did, the Son did in a human life')
claim('h37', 'God sees and answers the one who humbles himself, gives favor to the humble, humbles to test and do good, brings the proud low and looks on a humble estate',
      'gathers God\'s acts toward the humble and the proud', ['2 Chronicles 12:7', '1 Kings 21:29', 'Proverbs 3:34', 'James 4:6', 'Deuteronomy 8:16', 'Isaiah 2:11', 'Luke 1:48'])
tell('h37', '13.1', 'Toward the humble and the proud.')

data = {
    'update': update,
    'refs': [{'kind': 'escalation', 'value': '2148'}, {'kind': 'thread', 'value': 'OT-12'},
             {'kind': 'thread', 'value': 'OT-105'}, {'kind': 'thread', 'value': 'OT-106'}],
    'chapters': [
        {'chapter': '10.14', 'from_version': 0, 'to_version': 1, 'file': '10-14-humility-v1-20261015.md'},
        {'chapter': '10.0', 'from_version': 5, 'to_version': 6, 'file': '10-00-the-inner-being-at-work-v6-20261015.md'},
        {'chapter': '10.1', 'from_version': 21, 'to_version': 22, 'file': '10-01-feeling-v22-20261015.md'},
        {'chapter': '10.2', 'from_version': 17, 'to_version': 18, 'file': '10-02-knowing-and-hearing-v18-20261015.md'},
        {'chapter': '10.7', 'from_version': 28, 'to_version': 29, 'file': '10-07-choosing-and-setting-direction-v29-20261015.md'},
        {'chapter': '10.8', 'from_version': 7, 'to_version': 8, 'file': '10-08-right-and-wrong-v8-20261015.md'},
        {'chapter': '10.9', 'from_version': 23, 'to_version': 24, 'file': '10-09-relating-to-god-v24-20261015.md'},
        {'chapter': '10.10', 'from_version': 26, 'to_version': 27, 'file': '10-10-relating-to-others-v27-20261015.md'},
        {'chapter': '10.12', 'from_version': 10, 'to_version': 11, 'file': '10-12-fear-v11-20261015.md'},
        {'chapter': '10.13', 'from_version': 9, 'to_version': 10, 'file': '10-13-anger-v10-20261015.md'},
        {'chapter': '04', 'from_version': 17, 'to_version': 18, 'file': '04-the-heart-v18-20261015.md'},
        {'chapter': '05', 'from_version': 8, 'to_version': 9, 'file': '05-the-soul-v9-20261015.md'},
        {'chapter': '06', 'from_version': 12, 'to_version': 13, 'file': '06-the-spirit-v13-20261015.md'},
        {'chapter': '11', 'from_version': 33, 'to_version': 34, 'file': '11-other-sides-of-the-inner-being-v34-20261015.md'},
        {'chapter': '12', 'from_version': 22, 'to_version': 23, 'file': '12-when-the-inner-being-goes-wrong-v23-20261015.md'},
        {'chapter': '13.1', 'from_version': 25, 'to_version': 26, 'file': '13-01-divine-v26-20261015.md'},
        {'chapter': '14', 'from_version': 17, 'to_version': 18, 'file': '14-made-new-v18-20261015.md',
         'passages': [{'anchor': "The seven conditions for the Spirit's work", 'new_anchor': None}]},
    ],
    'claims': claims + [{'ref': '10-5', 'edit': {'verdict': 'Withdrawn', 'status': 'withdrawn',
        'note': '2Ch 7:14 read in the M09 humbling fan-out (#2148, batch 1): the verse names humbling, prayer, seeking his face and turning, and God hearing, forgiving and healing; it names no Spirit and no count of seven. Removed from Ch 14 Held; the verse is now told in 10.14 for what it says (researcher, 2026-10-15: "bring the narrative up to date").'}}],
    'tellings': tellings,
}
out = os.path.join(HERE, 'm09-humility-register-update-v1-20261015.json')
json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('claims', len(claims), 'tellings', len(tellings), '->', out)
