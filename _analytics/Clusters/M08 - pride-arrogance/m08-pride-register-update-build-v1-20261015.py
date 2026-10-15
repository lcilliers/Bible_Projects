"""Builds the narrative-register update JSON for the M08 pride weave (#2156).

Researcher, 2026-10-15, verbatim: "ensure all the verses that need a re-read, or incorporation into another
cluster read as outstanding items in the register, then proceed with a consolidated cross batch synergy,
updating the claims register, weaving and cross checking that the narrative is anchored in the claims
register for this group of words". Writes m08-pride-register-update-v1-20261015.json for
`iba\\app\\ps\\Narrative-Register.ps1 -Action Record -File <json> -By Claude`.
Every new claim is a statement in the new text that goes beyond its verses (rule 77); readings marked
"I read" in the text carry i_read true. The tellings on passages outside the new text come from the
anchor cross-check (m08-pride-anchor-crosscheck-v1-20261015.md): existing pride passages that told no claim.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
F = '_analytics/Clusters/M08 - pride-arrogance/'
SRC = [F + f for f in (
    'm08-cluster-overview-v1-20261015.md', 'm08-group-B-scan-v1-20261015.md',
    'm08-batch1-reading-v1-20261015.md', 'm08-batch2-reading-v1-20261015.md', 'm08-batch3-reading-v1-20261015.md',
    'm08-batch4-reading-v1-20261015.md', 'm08-batch5-reading-v1-20261015.md', 'm08-reading-summary-v1-20261015.md',
    'm08-pride-synergy-v1-20261015.md', 'm08-pride-anchor-crosscheck-v1-20261015.md')]
SCRIPTS = [F + f for f in (
    'm08-reading-scope-v1-20261015.py', 'm08-batch-pull-v1-20261015.py', 'm08-quote-check-v1-20261015.py',
    'm08-narrative-quote-check-v1-20261015.py', 'm08-pride-anchor-scan-v1-20261015.py',
    'm08-pride-weave-v1-20261015.py', 'm08-pride-register-update-build-v1-20261015.py')]

update = {
    'update_date': '2026-10-15',
    'title': 'M08 pride: 10.15 Pride written, angles woven, pride passages anchored in the register',
    'strand': 'pride and arrogance (M08): pride, boasting, mocking (#2156)',
    'researcher_instruction': '"ensure all the verses that need a re-read, or incorporation into another cluster read as outstanding items in the register, then proceed with a consolidated cross batch synergy, updating the claims register, weaving and cross checking that the narrative is anchored in the claims register for this group of words" (2026-10-15); earlier: "group B - lets do one more scan of these, it seems they are mostly data.  Set them aside as data unless the terms are supporting other M-codes"; "mark the 34 verses forward as suggested. then start reading A, C and D in batches.  The Ch 13 references should include a reflection on a) are any of the pride words indicative of their characteristics? I suspect there is difference between the \'pride\',\'most high\' of God, which is not an assumed position but a undisputed state, verses IB pride that is mostly assumed."',
    'method': 'M08 overview; group B (height words, 211 verses) scanned: 135 data, 42 pride sense, 34 forward (OT-97). Groups A, C, D with the B pride-sense verses and E read in five batches by passage (355 verses: 312 read, 25 carried from M09, 18 data), each with a Ch 13 reflection; Isa 47:8 read from group F. Outstanding items registered as OT-107 (#2157), OT-97.25 and OT-103.22 closed, OT-105 items added. Cross-batch account (m08-pride-synergy). New 10.15 Pride holds the full account (#1961); angles woven in context into 13.1 (Majesty), 10.2 (Pride and hearing), 10.10 (Pride over another), 10.7 (Presumption), Ch 11 s4 (Lifted up); pointers in Ch 12, 10.14, 10.0. Anchor cross-check: every narrative passage using a pride-group word read against the register (151 before the weave, 110 telling no claim); the pride statements among them registered or told; the passages that use a pride word for another concept left to that concept\'s strand.',
    'source_files': SRC,
    'scripts': SCRIPTS,
    'claims_changed_note': '31 new claims (10.15, 13.1, Ch 11 lexical); existing claims C-182, C-207, C-208, C-209, C-210 and 2-2 told in further passages; no claim withdrawn',
    'not_woven_note': 'Held for other strands (OT-107): 13.2 (2Pe 2:10-11; Job 33:23), 13.3 (2Co 12:7; 1Ti 3:6), 13.4 (Job 41:34; Job 38:11; Psa 89:9), the 25 God-on-high height verses, the self-exaltation words outside M08 (H7311A, G5312, H5375L, H7682), H2778A, the M06 scorn words, G2754, G1703, pride against love/mourning/rest for M51/M03/M33, the Ch 12 Held vice lists, Amo 8:7 and Job 9:23 unsettled. Ch 1 outline (#2111) not touched.',
    'structure_change': 'New sub-chapter 10.15 Pride (reading order 26, after 10.14; later chapters +1). New sections: 13.1 Majesty (before Lowering himself); 10.2 Pride and hearing; 10.10 Pride over another; 10.7 Presumption (before Willing). Ch 11 s4 gains the face Lifted up. Ch 12 Pride section points to 10.15; 10.14 opening and Connections name 10.15; 10.0 names 10.12 to 10.15.',
    'structure_reason': 'Pride has its own words, faces, other parties and outcomes across the activities, with God as its counter-measure; a key characteristic gets one full account as its own Ch 10 sub-chapter (#1961), with each angle woven in context (#1920). Ch 12 keeps the passages that show the inner being going wrong.',
    'quote_parts': 214,
    'quote_failures': 0,
    'quote_note': 'every double-quoted part of 10.15 (149) and of the lines added to the eight woven chapters (65), split on the ellipsis, checked against iba.db verse text in canonical order (m08-narrative-quote-check-v1-20261015.py)',
    'notes': 'The 10.15 chapter row was added directly to narrative_chapter (reading_order 26, later chapters +1), as for 10.14, because no Narrative-Register action adds a chapter (#2155).',
}

claims, tellings = [], []
def claim(key, text, beyond, sources, i_read=False):
    claims.append({'key': key, 'new': {'text': text, 'beyond_text': beyond, 'origin': 'narrative',
                                       'verdict': 'New', 'i_read': i_read, 'sources': sources}})
def tell(key, chapter, passage, kind='in full', part=None):
    t = {'claim': key, 'chapter': chapter, 'passage': passage, 'kind': kind, 'action': 'add'}
    if part: t['part'] = part
    tellings.append(t)

P = '10.15'
claim('p1', 'The same Hebrew words name God\'s majesty and human pride; the English marks the difference, not the Hebrew',
      'compares the renderings of one word family across the verses',
      ['Exodus 15:1', 'Exodus 15:7', 'Psalm 93:1', 'Jeremiah 48:29', 'Proverbs 16:18', 'lexical: H1347 gaon, H1346 gaavah, H1348 geut, H1342 gaah: majesty of God and pride of people (iba.db verse_lexical, M08 batch 1)'])
tell('p1', P, 'The words for pride in Scripture are words of height.')
tell('p1', '13.1', 'The words that name human pride also name God\'s majesty', 'in part', 'the same words')
tell('p1', '11', 'Lifted up. One Hebrew word names the heart', 'in part', 'one family of words is God\'s majesty and human pride')
claim('p2', 'Pride, the boast and the mock belong together in the verses',
      'groups three word families as one subject', ['Proverbs 21:24', 'Psalm 94:4', 'Jeremiah 48:29-30', 'Psalm 73:6-8'])
tell('p2', P, 'Pride also speaks.')
claim('p3', 'Pride holds as its own what was given: strength, healing, majesty, wealth, beauty and height are given, and the heart rises on them',
      'reads the accounts side by side as one order, with 1Co 4:7 as its plain statement',
      ['1 Corinthians 4:7', 'Deuteronomy 8:14-18', '2 Chronicles 26:15-16', '2 Chronicles 32:23-25', 'Daniel 5:18-20', 'Ezekiel 28:5', 'Ezekiel 31:9-10'], True)
tell('p3', P, 'The clearest thing the verses say about pride is where it comes from.')
tell('p3', P, 'So the standing in these verses is real.')
tell('p3', '12', 'Pride can grow from a beauty that was given.', 'pointer')
tell('p3', '13.1', 'He gives height.', 'in part', 'the height he gives')
tell('p3', '04', 'The heart is named just before the anger', 'in part', 'Uzziah\'s heart lifted up when he was strong')
tell('p3', '10.3', 'So remembering is commanded.', 'in part', 'against the pride of having')
tell('p3', '10.4', 'The same skill is put to different uses:', 'in part', 'Uzziah strong, then proud')
tell('p3', '10.6', 'A thirst met can be forgotten.', 'in part', 'the giver forgotten')
claim('p4', 'Pride credits to its own hand what was done through it',
      'reads the rod\'s boast with the axe saying of the same passage, and Nebuchadnezzar\'s boast',
      ['Isaiah 10:5', 'Isaiah 10:13', 'Isaiah 10:15', 'Deuteronomy 8:17', 'Daniel 4:30'], True)
tell('p4', P, 'It credits its own hand.')
tell('p4', '10.13', 'Some people carry out God\'s anger, and the verses judge how they do it.', 'in part', 'the rod that boasts')
tell('p4', '11', 'What moves inside it. The same standing is filled by very different acts.', 'in part', 'pride: built by my mighty power')
tell('p4', '12', 'Before the fall named in Daniel 5:20 stands the boast itself', 'in part')
claim('p5', 'The same word names an honour God chooses, gives or restores, and what was given can be turned into pride',
      'sets the honour given beside the given turned to pride',
      ['Psalm 47:4', 'Isaiah 60:15', 'Nahum 2:2', 'Deuteronomy 33:29', 'Ezekiel 24:21', 'Ezekiel 7:20'])
tell('p5', P, 'The same word can name an honour God gives.')
tell('p5', '13.1', 'He gives height.', 'in part', 'the pride of Jacob whom he loves')
claim('p6', 'Pride at its full height says of itself what is true only of God: the proud city\'s "I am, and there is no one besides me" repeats God\'s self-statement',
      'sets Isa 47:8, 10 and Zep 2:15 beside Isa 45:5 and 46:9',
      ['Isaiah 45:5', 'Isaiah 46:9', 'Isaiah 47:8', 'Isaiah 47:10', 'Zephaniah 2:15'], True)
tell('p6', P, 'God says of himself:')
tell('p6', '13.1', 'Only he says it of himself.')
claim('p7', 'Pride claims a place that is God\'s: likeness to the Most High, a god\'s seat, his temple',
      'joins three claims to God\'s place', ['Isaiah 14:13-14', 'Ezekiel 28:2', '2 Thessalonians 2:4'])
tell('p7', P, 'The same claim comes in other words.')
tell('C-208', '11', 'Likening. Comparing is how love praises', 'in part', 'how pride rises')
claim('p8', 'Pride deceives the one who holds it, and the fear one inspires in others can feed it',
      'reads Obd 3 with Jer 49:16', ['Obadiah 3', 'Jeremiah 49:16'])
tell('p8', P, 'It deceives the one who holds it.')
claim('p9', 'Pride shuts God out of the thoughts, is set against faith, and gives no rest',
      'joins Psa 10:4 and Hab 2:4-5', ['Psalm 10:4', 'Habakkuk 2:4-5'])
tell('p9', P, 'It shuts God out of the thoughts.')
claim('p10', 'Pride shows in the eyes, the walk and what is worn, and the verses join it to ease',
      'gathers the outward signs and the ease named beside them', ['Proverbs 21:4', 'Isaiah 3:16', 'Psalm 73:4-6', 'Mark 7:21-22'])
tell('p10', P, 'It shows.')
claim('p11', 'Pride is set against hearing: it will not take rebuke or advice, and the scoffer is known by what he will not receive',
      'gathers the pride and scoffer sayings with the hearing named against them',
      ['Jeremiah 13:15-17', 'Proverbs 13:10', 'Proverbs 13:1', 'Proverbs 15:12', 'Proverbs 9:8', 'Proverbs 14:6', 'Isaiah 28:22-23'], True)
tell('p11', P, 'Across all its words, pride is set against hearing.')
tell('p11', '10.2', 'Pride is set against the ear.')
tell('p11', '10.2', 'Ears can be closed to a word that is still being spoken.', 'in part', 'the word scorned')
claim('p12', 'Presumption acts on its own word where another word was given: speaking what God did not command, going up when told not to, not keeping the decision given',
      'reads the presumption verses as one act; reads Deu 1:41-43 as presumption in the words of repentance',
      ['Deuteronomy 18:20-22', 'Deuteronomy 1:41-43', 'Deuteronomy 17:12-13', 'Nehemiah 9:16-17', 'Psalm 19:13'], True)
tell('p12', P, 'Presumption is pride acting on its own word.')
tell('p12', '10.7', 'Some choices go beyond what was given.')
tell('p12', '10.7', 'Fear is learned there too, at a meal', 'in part', 'presumption is the opposite')
tell('p12', '10.9', 'The psalmist names two kinds of sin', 'in part', 'presumptuous sins that would rule')
claim('p13', 'God works to keep pride from a person: by warnings that open the ear, and by a thorn given against conceit',
      'joins Job 33:16-17 and 2Co 12:7-9', ['Job 33:16-17', '2 Corinthians 12:7-9'])
tell('p13', P, 'God works to keep pride from a person.')
tell('p13', '10.2', 'Learning to fear God takes a life.', 'in part', 'God opens the ear to conceal pride')
claim('p14', 'What the verses set against pride is hearing and the fear of God',
      'names the opposite the verses give', ['Romans 11:20', 'Proverbs 8:13', 'Jeremiah 13:15'])
tell('p14', P, 'What the verses set against pride is hearing, and fear.')
tell('p14', '10.12', 'Fear of God is also called for as a guard, and set against pride.', 'in part')
claim('p15', 'Pride stands over someone: the poor, the widow, the needy left unaided, the righteous; it closes the heart to pity and is set against love',
      'gathers who pride stands over in the verses',
      ['Psalm 10:2', 'Proverbs 17:5', 'Proverbs 15:25', 'Ezekiel 16:49', 'Psalm 31:18', 'Psalm 119:51', 'Psalm 119:69', 'Psalm 119:85', 'Psalm 17:10', '1 Corinthians 8:1', '1 Corinthians 13:4', 'Galatians 5:26', '1 Corinthians 5:2'])
tell('p15', P, 'Pride is seldom alone in these verses.')
tell('p15', '10.10', 'Pride between people stands over someone weaker.')
claim('p16', 'Pride is also felt by the one under it, and the answer given is to look to the Lord', 'reads Psa 123:4 with 123:2', ['Psalm 123:2-4'])
tell('p16', P, 'It is also felt from below.')
tell('p16', '10.10', 'The one under it carries it', 'in part')
claim('p17', 'The verses do not condemn boasting as such; they judge it by what it rests on',
      'compares the boasts judged and the boasts commanded', ['Jeremiah 9:23-24', '1 Corinthians 1:31', 'Galatians 6:14', 'Psalm 49:6-7', 'Proverbs 27:1'])
tell('p17', P, 'A boast is what a person stands on, said aloud.')
tell('C-182', P, 'Moved. The boast is not taken away.')
tell('C-182', '05', 'learn from me, for I am gentle and lowly in heart', 'in part', 'the soul boasts in the Lord, not in itself')
tell('C-182', '11', 'Lifted up. One Hebrew word names the heart', 'in part', 'the boast moves')
claim('p18', 'Boasting in oneself is excluded because what is held was given: grace, gift, and God\'s choosing of the low',
      'gives the ground of the exclusion', ['Ephesians 2:8-9', 'Romans 3:27', '1 Corinthians 1:28-29', '1 Corinthians 4:7'])
tell('p18', P, 'Excluded.')
claim('p19', 'Boasting in weakness claims no more than is so, and makes room for Christ\'s power',
      'reads 2Co 12:6 against pride\'s standing', ['2 Corinthians 11:30', '2 Corinthians 12:5-10'], True)
tell('p19', P, 'In weakness.')
claim('p20', 'The right measure of oneself, and of one\'s boast, is the measure God assigned; thinking oneself something when one is nothing is self-deception',
      'joins the measure of thinking and of boasting', ['Romans 12:3', '2 Corinthians 10:13', 'Galatians 6:3-4'])
tell('p20', P, 'Within a measure.')
claim('p21', 'A boast can be in another person, and it puts the one who boasts at stake on the other\'s conduct',
      'reads Paul\'s boasts of the churches', ['2 Corinthians 7:4', '2 Corinthians 7:14', '2 Corinthians 9:2-4', '2 Corinthians 8:24', '1 Thessalonians 2:19'])
tell('p21', P, 'Of others.')
tell('p21', '10.10', 'The word for boasting turns the other way between people')
claim('p22', 'Mocking takes the sufferer\'s trust in God as its target, and the sufferer answers God, not the mockers',
      'reads the taunt of Psa 22:8 with 22:9 and its use at the cross', ['Psalm 22:7-9', 'Matthew 27:43'])
tell('p22', P, 'Mocking is pride turned outward, on another.')
tell('p22', '10.5', 'Mockery can begin without words.', 'in part')
tell('p22', '11', 'God\'s delight in a person.', 'in part', 'the mockers\' taunt')
tell('p22', '13.1', 'His delight in people\'s mouths.', 'in part', 'the mockers')
claim('p23', 'Mocking God\'s messengers and word goes on until there is no remedy; the same call is met by mocking and by humbling',
      'reads 2Ch 36:16 as the end of the way back, beside 2Ch 30:10-11',
      ['2 Chronicles 36:15-16', '2 Chronicles 30:10-11', 'Galatians 6:7'], True)
tell('p23', P, 'Mocking is pride turned outward, on another.', 'in part', 'until there was no remedy')
claim('p24', 'In the proverbs pride brings its own fall, with no other hand named; elsewhere God brings it down',
      'compares the sayings with no agent and the verses that name God',
      ['Proverbs 16:18', 'Proverbs 29:23', 'Proverbs 11:2', 'Ezekiel 7:10', 'James 4:6', 'Luke 1:51', 'Isaiah 2:11', 'Psalm 75:6-7'])
tell('p24', P, 'Its own fall.')
tell('p24', P, 'God brings it down.')
tell('p24', '10.14', 'Pride brings its own fall.', 'in part')
tell('C-210', P, 'God brings it down.', 'in part', 'Your pomp is brought down to Sheol')
claim('p25', 'The one who is high by nature comes near the low; those who make themselves high are known from afar',
      'reads the contrast of Psa 138:6', ['Psalm 138:6', 'Psalm 113:5-7'], True)
tell('p25', P, 'God\'s height does not do what pride does.')
tell('p25', '13.1', 'He gives height.', 'in part', 'he regards the lowly')
claim('p26', 'The charge of pride can come from another\'s anger or from a ready explanation, and the verses do not make it true',
      'reads Eliab\'s charge against the chapter, and Eliphaz\'s explanation against the book',
      ['1 Samuel 17:17-18', '1 Samuel 17:28-29', 'Job 22:29'], True)
tell('p26', P, 'Pride can be named wrongly.')
tell('p26', '04', 'The angry can read another\'s heart wrongly.', 'in part')
tell('p26', '10.4', 'Anger does not stay a feeling.', 'in part', 'Eliab misreads')
tell('p26', '10.14', 'Reading another\'s fall.')
claim('p27', 'The same words are not pride when the height is given or faces God: a heart lifted up in God\'s ways, strength of soul given, a heart not lifted up and at rest',
      'sets the other face of the words beside their proud uses',
      ['2 Chronicles 17:4-6', '2 Chronicles 26:16', 'Psalm 138:3', 'Isaiah 3:5', 'Psalm 131:1-2', 'Habakkuk 2:5'], True)
tell('p27', P, 'The same words are not pride when the height is given')
tell('p27', '11', 'Lifted up. One Hebrew word names the heart')
claim('g1', 'God\'s majesty is his own and everlasting, shown in what he does, turned toward help, and joined to what only he does',
      'gathers what the majesty verses say of it',
      ['Psalm 93:1-2', 'Exodus 15:1', 'Exodus 15:7', 'Deuteronomy 33:26', 'Psalm 68:34-35', 'Job 40:10-14', 'Isaiah 2:10-11'])
tell('g1', '13.1', 'The words that name human pride also name God\'s majesty')
claim('g2', 'God\'s majesty is challenged and not overturned; his laughter answers only those who rise against him and is never aimed at the weak',
      'compares God\'s derision with human mocking',
      ['Psalm 2:2-4', 'Psalm 59:7-8', 'Proverbs 1:24-26', 'Proverbs 3:34', 'Galatians 6:7', 'Proverbs 17:5', 'Psalm 22:7'], True)
tell('g2', '13.1', 'It is challenged, and not overturned.')
claim('g3', 'The Son\'s majesty is received and grounded, stands beside his being handed over, and does not defend itself against mockery; he did not grasp what pride grasps',
      'reads the majesty, mocking and Php 2:6 verses together',
      ['2 Peter 1:16-17', 'Colossians 1:18-19', 'Luke 9:43-44', 'Matthew 27:29', 'Luke 22:64', 'Mark 15:31', 'Luke 23:9', 'Luke 23:34', 'Philippians 2:6', 'Hebrews 1:3'], True)
tell('g3', '13.1', 'In the Son. His majesty is received')
tell('g3', P, 'Jesus was mocked as king, as prophet and as saviour', 'pointer')
claim('l1', 'One Hebrew word, ebrah, names the overflow of anger and the overflow of pride',
      'lexical: the same word in Job 40:11 and Proverbs 21:24',
      ['Job 40:11', 'Proverbs 21:24', 'lexical: H5678 ebrah, Job 40:11 "overflowings", Proverbs 21:24 "pride" (iba.db verse_lexical)'])
tell('l1', '11', 'Overflow. One Hebrew word')
tell('C-209', '10.6', 'Envy can be pictured in a figure.', 'in part', 'the pride of the tree and the given beauty')
tell('2-2', '09', 'The soul sins; the human spirit never does.', 'in part', 'the spirit haughty before a fall')

data = {
    'update': update,
    'refs': [{'kind': 'escalation', 'value': '2156'}, {'kind': 'escalation', 'value': '2157'},
             {'kind': 'thread', 'value': 'OT-107'}, {'kind': 'thread', 'value': 'OT-97'},
             {'kind': 'thread', 'value': 'OT-103'}, {'kind': 'thread', 'value': 'OT-105'}],
    'chapters': [
        {'chapter': '10.15', 'from_version': 0, 'to_version': 1, 'file': '10-15-pride-v1-20261015.md'},
        {'chapter': '10.0', 'from_version': 6, 'to_version': 7, 'file': '10-00-the-inner-being-at-work-v7-20261015.md'},
        {'chapter': '10.2', 'from_version': 18, 'to_version': 19, 'file': '10-02-knowing-and-hearing-v19-20261015.md'},
        {'chapter': '10.7', 'from_version': 30, 'to_version': 31, 'file': '10-07-choosing-and-setting-direction-v31-20261015.md'},
        {'chapter': '10.10', 'from_version': 27, 'to_version': 28, 'file': '10-10-relating-to-others-v28-20261015.md'},
        {'chapter': '10.14', 'from_version': 1, 'to_version': 2, 'file': '10-14-humility-v2-20261015.md'},
        {'chapter': '11', 'from_version': 34, 'to_version': 35, 'file': '11-other-sides-of-the-inner-being-v35-20261015.md'},
        {'chapter': '12', 'from_version': 23, 'to_version': 24, 'file': '12-when-the-inner-being-goes-wrong-v24-20261015.md'},
        {'chapter': '13.1', 'from_version': 26, 'to_version': 27, 'file': '13-01-divine-v27-20261015.md'},
    ],
    'claims': claims,
    'tellings': tellings,
}
out = os.path.join(HERE, 'm08-pride-register-update-v1-20261015.json')
json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('claims', len(claims), 'tellings', len(tellings), '->', out)
