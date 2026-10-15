"""Builds the register update for the M09 humility claims reconciliation (#2152).

Researcher, 2026-10-15, verbatim: "The method I am proposing is to reconcile the existing claims for the
concepts that is being updated, for instance in this case humility and related.  to reconcile every claim
in the chapter will cause severe disruption because it is not the focus and cannot be resolved in this
session." Scope: the existing passages on humility and related concepts (humble, lowly, meek, contrite,
the broken or crushed heart or spirit, gentleness, submission, brought low; in Ch 12 the pride section
where the counterpart was added) in the chapters touched by update 141. Other concepts in those
chapters wait for their own strands.

Writes m09-humility-reconcile-register-update-v1-20261015.json for Narrative-Register.ps1 -Action Record.
Chapters with text changes get a new version (10.7 v30, Ch 14 v19); the others are re-read (from = to).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

claims, tellings = [], []
def claim(key, text, beyond, sources, i_read=False):
    claims.append({'key': key, 'new': {'text': text, 'beyond_text': beyond, 'origin': 'narrative',
                                       'verdict': 'New', 'i_read': i_read, 'sources': sources}})
def tell(c, ch, passage, kind='in part', part=None):
    t = {'claim': c, 'chapter': ch, 'passage': passage, 'kind': kind, 'action': 'add'}
    if part: t['part'] = part
    tellings.append(t)

# ---- new claims for existing statements with no register entry
claim('n1', 'God\'s anger is roused to save the humble, and the earth falls still before it',
      'joins "when once your anger is roused" with "to save all the humble of the earth"', ['Psalm 76:7-9'])
claim('n2', 'The parts of the inner person give way in sequence: soul, spirit, heart under an enemy, then a turn; heart, then spirit, then body under sorrow',
      'reads Psa 143:3-6 and Pro 15:13 with 17:22 as one chain each', ['Psalm 143:3-6', 'Proverbs 15:13', 'Proverbs 17:22'])
claim('n3', 'The offering is weighed by what is inside the one who brings it: an ear opened, the law in the heart, a broken heart, a love that lasts',
      'gathers the verses that set something inward in place of sacrifice', ['Isaiah 1:11-13', 'Psalm 40:6-8', 'Psalm 51:16-19', 'Hosea 6:4-6', 'Matthew 9:13', 'Matthew 12:7'], True)
claim('p1', 'Pride is placed in the heart and in the spirit', 'gathers the verses that seat pride', ['Deuteronomy 8:14', 'Proverbs 16:5', 'Proverbs 16:18', 'Daniel 5:20'])
claim('p2', 'In pride, thinking goes wrong at the point of comparing: a person makes himself like God, or shrinks God to his own size',
      'sets the self-exaltation of Isa 14 and Eze 28 beside Psa 50:21', ['Isaiah 14:13-14', 'Ezekiel 28:2', 'Psalm 50:21', 'Luke 1:51'])
claim('p3', 'Pride can grow from a beauty that was given: given, blameless, then trade, violence and a proud heart',
      'reads the order of Eze 28 and the great tree of Eze 31', ['Ezekiel 31:9-10', 'Ezekiel 28:13-17'], True)
claim('p4', 'Death brings pride down', 'reads the taunt of Isa 14', ['Isaiah 14:10-11'])
claim('p5', 'Pride can design its own honour, and the honour it designed becomes the measure of its fall',
      'reads Haman\'s proposal and its outcome', ['Esther 6:6-13'], True)

# ---- h22 (C-188): its count of four passages is incomplete across the narrative (13.1 gathers more)
edits = [{'ref': 'C-188', 'edit': {
    'text': 'What God looks to is set against a religious act in the humility passages (the fast, the walk, the house, the broken heart), as in the other passages gathered in 13.1; the offering follows the broken heart',
    'verdict': 'Restated',
    'note': 'The first wording ("In four passages") counted only the humility passages; 13.1 Delight gathers more (Isa 1:11-13; Psa 40:6-8; Hos 6:6; Mat 9:13; 12:7). Found in the reconciliation of #2152.'}}]

# ---- tellings: existing passages on humility and related concepts
tell('1-4', '10.1', 'The spirit is troubled, crushed, faint', 'in part', 'spirit: crushed')
tell('C-189', '10.2', 'Hearing is the main way in.', 'in part', 'a crushed spirit can block hearing')
tell('C-190', '10.7', 'What the chosen are called to.', 'in part', 'Put on: humility put on, turned toward others')
tell('C-176', '10.7', 'An inner act weighed by what God chooses.', 'in part', 'the humbling beside oppression')
tell('C-171', '10.7', 'The will made absolute. Of Nebuchadnezzar', 'in part', 'Belshazzar has not humbled his heart')
tell('2-2', '10.8', 'When Scripture judges a person, it often names the heart.', 'in part', 'the spirit judged: haughty or lowly, crushed or contrite')
tell('C-192', '10.10', 'The spirit is the manner of approach.', 'in part', 'a spirit of gentleness')
tell('C-194', '10.10', 'Turned round.', 'in part', 'elders not domineering; humility toward one another')
tell('C-194', '10.10', 'Under it. The verses ask something of the one beneath', 'in part', 'submission with its ground')
tell('C-192', '10.10', 'Under it. The verses ask something of the one beneath', 'in part', 'remembering what one was')
tell('C-171', '10.13', 'Josiah heard the book read', 'in part', 'the same heart provoked the anger and turned it')
tell('C-175', '10.13', 'Turning can be partial.', 'in part', 'Rehoboam')
tell('C-174', '10.13', 'Distress turns people both ways. Under the judges', 'in full')
tell('C-183', '10.13', 'Zephaniah calls people to seek before the day comes', 'in part', 'the humble told to seek humility')
tell('n1', '10.13', 'Psalm 76 asks the same question', 'in full')
tell('C-174', '10.13', 'Distress under the anger goes two ways', 'in part')
tell('C-171', '04', 'Under God\'s anger, the verses give the heart several roles', 'in part', 'The heart that turns it')
tell('C-189', '04', 'Chapter 2 starts from that verse.', 'in part', 'the heart of the contrite revived')
tell('2-2', '06', 'This matters because it is often said that the human spirit never sins.', 'in full')
tell('5-2', '06', 'The verbs in these verses are many', 'in full')
tell('2-2', '06', 'It is lowly or proud, and it is judged.', 'in part')
tell('C-189', '06', 'It is crushed, and it faints.', 'in part', 'a broken spirit can keep a person from hearing')
tell('n2', '11', 'Psalm 143 shows a collapse spreading', 'in full')
tell('n2', '11', 'Proverbs gives the same chain in two lines', 'in part')
tell('C-189', '11', 'Crushing. Crushed by an enemy', 'in part', 'crushed by an enemy, or offered to God')
tell('C-188', '11', 'An offering. For you will not delight in sacrifice', 'in part')
tell('C-174', '11', 'Distress turns people both ways. In distress Manasseh', 'in part')
tell('C-188', '11', 'What the one who brings it brings first.', 'in part')
tell('p1', '12', 'Pride is placed in the heart and in the spirit.', 'in full')
tell('p2', '12', 'Pride is also a false likeness.', 'in full')
tell('p3', '12', 'Pride can grow from a beauty that was given.', 'in part', 'the great tree')
tell('p3', '12', 'The king of Tyre is lamented in the same way.', 'in full')
tell('p4', '12', 'Death brings pride down.', 'in full')
tell('p5', '12', 'Pride can design its own honour.', 'in full')
tell('2-2', '12', 'The human spirit is judged here beside the heart.', 'in part', 'the spirit weighed: haughty or lowly')
tell('C-176', '13.1', 'What he chooses is turned toward others.', 'in part', 'the self-humbling beside oppression')
tell('C-203', '13.1', 'He does as he wills.', 'in part', 'those who walk in pride he is able to humble')
tell('C-188', '13.1', 'Not the offering itself.', 'in part', 'the offerings delighted in after the broken heart')
tell('n3', '13.1', 'The verses do not say he has no use for offerings', 'in full')
tell('C-189', '14', 'The lowly spirit and the contrite heart revived:', 'in part')

reread = {'10.1': ('10-01-feeling-v22-20261015.md', 22), '10.2': ('10-02-knowing-and-hearing-v18-20261015.md', 18),
          '10.8': ('10-08-right-and-wrong-v8-20261015.md', 8), '10.10': ('10-10-relating-to-others-v27-20261015.md', 27),
          '10.13': ('10-13-anger-v10-20261015.md', 10), '04': ('04-the-heart-v18-20261015.md', 18),
          '06': ('06-the-spirit-v13-20261015.md', 13), '11': ('11-other-sides-of-the-inner-being-v34-20261015.md', 34),
          '12': ('12-when-the-inner-being-goes-wrong-v23-20261015.md', 23), '13.1': ('13-01-divine-v26-20261015.md', 26)}
chapters = [{'chapter': k, 'from_version': v, 'to_version': v, 'file': f} for k, (f, v) in reread.items()]
chapters += [{'chapter': '10.7', 'from_version': 29, 'to_version': 30, 'file': '10-07-choosing-and-setting-direction-v30-20261015.md'},
             {'chapter': '14', 'from_version': 18, 'to_version': 19, 'file': '14-made-new-v19-20261015.md'}]

data = {
 'update': {
  'update_date': '2026-10-15',
  'title': 'M09 humility: existing humility claims reconciled in the touched chapters',
  'strand': 'humility (M09), claims reconciliation of update 141 (#2152)',
  'researcher_instruction': '"We agreed that the claim reconciliation will take place when a particular chapter is touched with updates.  I cannot see how you can update the chapter in the narrative with new information without reviewing the current claims, and ensuring that the claims in the narrative are recorded in the register." and "The method I am proposing is to reconcile the existing claims for the concepts that is being updated, for instance in this case humility and related.  to reconcile every claim in the chapter will cause severe disruption because it is not the focus and cannot be resolved in this session." (2026-10-15)',
  'method': 'In the 15 chapters touched by update 141, the existing passages on humility and related concepts (63 by word search, plus the edited passages that keep older text) were read against the register. Matched to the claims of update 141 or to the untold legacy claims 1-4, 2-2 and 5-2 by new tellings; 8 statements with no claim registered (n1-n3, p1-p5); C-188 restated (its count of four passages was incomplete across the narrative); two statements beyond their verses restated in the text (10.7 "not wrong in itself"; Ch 14 "God\'s reason is tender"). Passages that only quote, or that belong to other concepts (fear, authority, flesh, the gentle waters of Isa 8:6, the gentle lamb of Jer 11:19), were left for their own strands.',
  'source_files': ['_analytics/Clusters/M09 - humility-lowliness/m09-humility-reconcile-v1-20261015.md'],
  'scripts': ['_analytics/Clusters/M09 - humility-lowliness/m09-humility-reconcile-text-v1-20261015.py',
              '_analytics/Clusters/M09 - humility-lowliness/m09-humility-reconcile-register-build-v1-20261015.py'],
  'claims_changed_note': '8 new claims (n1-n3, p1-p5); C-188 restated; 40 tellings on existing passages; legacy 1-4, 2-2, 5-2 now told',
  'not_woven_note': 'Other concepts in the touched chapters (soul, the Spirit given, heart as centre, fear, authority) are not reconciled here; they wait for their strands (researcher ruling on scope).',
  'quote_parts': 0, 'quote_failures': 0,
  'quote_note': 'no new quotations; two restatements remove words',
 },
 'refs': [{'kind': 'escalation', 'value': '2152'}, {'kind': 'escalation', 'value': '2148'}],
 'chapters': chapters,
 'claims': claims + edits,
 'tellings': tellings,
}
out = os.path.join(HERE, 'm09-humility-reconcile-register-update-v1-20261015.json')
json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('claims', len(claims), 'edits', len(edits), 'tellings', len(tellings), '->', out)
