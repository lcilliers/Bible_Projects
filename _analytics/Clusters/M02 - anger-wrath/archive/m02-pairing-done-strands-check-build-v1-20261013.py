"""Builds m02-pairing-done-strands-check-v1-20261013.md: the decision for each of the 90 verses in the
M02 pairing threads whose paired strand is already read (OT-30 M01, OT-29 M25, OT-51 M20, OT-62 M64).
2026-10-13, researcher: "proceed as recommended". Inputs: m02-pairing-done-strands-crossref-v1-20261013.csv
and the hand-written text m02-pairing-done-strands-check-gaps-v1-20261013.txt (method, gap readings).
Decision codes: C carried (the anger and the paired word are carried together in the narrative);
P carried by a parallel verse; D data (no anger in the verse, or the paired word is only an outcome or
setting of the anger); G gap (read in the check file; weave on instruction); F forward to another thread."""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
DEC = {
    # M01 Fear & Awe (OT-30)
    '2Ch 29:8': ('C', 'horror is what onlookers see of the wrath; carried in 10.13 as the first step back'),
    '2Cor 12:20': ('C', 'Paul fears the quarrel, jealousy and anger he may find (10.10)'),
    '2Cor 7:11': ('C', 'indignation and fear as fruits of godly grief (10.1, 10.13, Ch 14)'),
    '2Cor 7:5': ('C', '"fighting without and fear within" (Ch 7, 10.12)'),
    '2Sa 22:8': ('P', 'parallel of Psa 18:7, carried in 10.13'),
    'Dan 1:10': ('D', 'no anger in the verse; fear of the king only'),
    'Deu 32:27': ('C', "God's fear of the enemy's provocation (10.12, 10.13)"),
    'Deu 9:19': ('C', 'Moses afraid of the anger, and heard (10.13)'),
    'Est 5:9': ('C', 'Mordecai neither rose nor trembled; Haman filled with wrath (Ch 4, 10.10, 10.13, Ch 11)'),
    'Exo 19:18': ('D', 'no anger in the verse; the mountain trembling is carried in Ch 15'),
    'Eze 26:17': ('D', 'the word is lament (qinah), not anger'),
    'Heb 11:27': ('C', "not afraid of the king's anger (10.12, 10.13)"),
    'Isa 13:13': ('C', 'the heavens tremble at the wrath (10.13)'),
    'Isa 13:9': ('D', 'desolation is the outcome; the day of wrath is carried through 13:13'),
    'Isa 51:13': ('C', "fear of the oppressor's wrath where God is forgotten (10.3, 10.9, Ch 11)"),
    'Isa 5:25': ('C', 'anger not turned (10.13); the quaking mountains are nature, not an inner act'),
    'Isa 7:4': ('C', 'do not fear the fierce anger of Rezin (Ch 4, 10.7, 10.13)'),
    'Jer 25:38': ('D', 'the land made waste; outcome only'),
    'Jer 42:18': ('D', 'horror and curse as the outcome of the wrath'),
    'Job 19:29': ('G', 'read in section 3'),
    'Job 6:4': ('C', "the terrors of God borne in Job's spirit (Ch 6, 10.12, 10.13)"),
    'Joe 1:7': ('D', 'no anger in the verse'),
    'Lam 2:22': ('G', 'read in section 3'),
    'Pro 20:2': ('G', 'read in section 3'),
    'Psa 104:32': ('D', 'no anger in the verse'),
    'Psa 18:7': ('C', 'the mountains tremble because he was angry (10.13)'),
    'Psa 55:3': ('C', 'the one attacked: "My heart is in anguish within me" (10.10)'),
    'Psa 58:9': ('D', 'no anger in the verse'),
    'Psa 76:7': ('G', 'partly carried; read in section 3'),
    'Psa 88:16': ('C', 'wrath borne without a turn (10.13)'),
    'Psa 88:7': ('C', 'wrath as weight (10.13)'),
    'Psa 90:11': ('C', 'the power of his anger and the fear of him (10.13)'),
    'Rev 11:18': ('G', 'read in section 3'),
    'Rom 13:4': ('C', 'be afraid; the authority carries out wrath (Ch 8, 10.13)'),
    'Zec 7:14': ('D', 'no anger in the verse'),
    # M20 Doubt & Discouragement (OT-51)
    'Col 3:21': ('C', 'provoked children lose heart (10.1, 10.10, Ch 11, Ch 15)'),
    'Dan 11:30': ('C', 'afraid, then enraged (10.1, 10.13)'),
    'Deu 31:17': ('G', 'partly carried; read in section 3'),
    'Isa 26:20': ('C', 'hiding until the fury passes (10.11, 10.13)'),
    'Isa 54:8': ('C', 'anger for a moment, face hidden (10.9, 10.13)'),
    'Isa 57:17': ('C', 'face hidden in anger, and not noticed (10.9)'),
    'Jer 33:5': ('G', 'read in section 3'),
    'Job 14:13': ('C', 'hide me until your wrath be past (Ch 2, 10.3, 10.11, 10.13)'),
    'Psa 27:9': ('C', 'hide not your face; turn not away in anger (10.9, 10.11, 10.13, Ch 11)'),
    'Psa 89:46': ('G', 'read in section 3'),
    'Rev 6:16': ('C', 'hide us from the wrath of the Lamb (10.11, 10.13)'),
    'Zep 2:3': ('G', 'read in section 3'),
    # M25 Life & Death (OT-29)
    '1Ch 13:10': ('P', 'parallel of 2Sa 6:7, carried in 10.13'),
    '2Sa 12:5': ('C', "David's anger and his oath of death (Ch 2, 10.13, Ch 11)"),
    '2Sa 6:7': ('C', 'anger against Uzzah, and his death (10.13)'),
    'Deu 31:29': ('G', 'read in section 3'),
    'Eze 20:13': ('F', 'forward to OT-01 (life by the statutes): "by which, if a person does them, he shall live"'),
    'Eze 20:21': ('F', 'forward to OT-01 (life by the statutes), with 20:13'),
    'Eze 20:33': ('G', 'read in section 3'),
    'Eze 21:31': ('D', 'wrath on Ammon; no life word in the verse'),
    'Eze 22:20': ('P', 'parallel of 22:21, carried in 10.13'),
    'Eze 22:21': ('C', 'the breath that gives life named in his anger (10.13)'),
    'Eze 35:11': ('C', '"as I live"; anger and envy from hatred (10.13)'),
    'Eze 6:12': ('D', 'death by pestilence, sword and famine; outcome only'),
    'Gen 45:5': ('C', 'angry with oneself; God sent me to preserve life (10.1, 10.13)'),
    'Isa 48:9': ('C', 'anger deferred for his name (10.13)'),
    'Isa 51:17': ('G', 'partly carried; read in section 3'),
    'Isa 57:16': ('C', 'the spirit would faint (Ch 2, Ch 6, 10.13, Ch 14)'),
    'Jer 10:10': ('C', 'the living God (Ch 2); the earth quaking at his wrath is carried through Psa 18:7 and Isa 13:13'),
    'Jer 18:23': ('C', 'Jeremiah prays the anger onto those who dug a pit for his life (10.13)'),
    'Job 4:9': ('C', 'breath, and the blast of his anger (10.13)'),
    'Job 5:2': ('C', 'vexation kills the fool (Ch 2, 10.1, 10.6, 10.13, Ch 11, Ch 12)'),
    'Joh 3:36': ('C', 'life, or wrath remaining (10.13)'),
    'Jon 4:9': ('C', 'angry enough to die (Ch 2, 10.1, 10.13); see the stale 10.13 note in section 4'),
    'Jos 9:20': ('C', 'let them live, lest wrath be upon us (10.10)'),
    'Lev 10:6': ('C', 'mourning held back, lest you die and wrath come (10.13, Ch 11)'),
    'Pro 11:4': ('G', 'read in section 3'),
    'Pro 16:14': ('C', "a king's wrath is a messenger of death (10.13)"),
    'Pro 19:11': ('C', 'good sense makes anger long (10.1, 10.10, Ch 11)'),
    'Pro 29:8': ('G', 'read in section 3'),
    'Psa 124:3': ('C', "swallowed alive in the enemies' anger (10.13)"),
    'Psa 138:7': ('C', "life preserved against the enemies' wrath (10.13)"),
    'Psa 30:5': ('C', 'anger for a moment, favour for a lifetime (10.13, Ch 11, 13.1)'),
    'Psa 78:38': ('C', 'anger restrained; they were but flesh (Ch 2, 10.13, Ch 11, 13.1)'),
    'Psa 78:50': ('C', 'a path for his anger; not spared from death (10.13)'),
    'Psa 7:6': ('C', 'arise in your anger, awake for me (Ch 2, 10.9)'),
    'Rev 15:7': ('D', 'the bowls of the wrath of God who lives forever; no inner act'),
    # M64 Will & Resolve (OT-62)
    '1Sa 20:30': ('C', "Saul's anger at Jonathan's choice (10.7)"),
    '1Ti 2:8': ('C', 'prayer without anger or quarrelling (10.4, 10.10, 10.13, Ch 11)'),
    'Act 5:33': ('C', 'enraged, and wanted to kill them (10.13)'),
    'Deu 29:20': ('C', 'not willing to forgive; anger and jealousy smoke (Ch 4, Ch 11, 13.1)'),
    'Eze 20:8': ('C', 'not willing to listen; wrath said, and held back (10.13)'),
    'Psa 106:23': ('C', 'his chosen one stood in the breach (10.7, 10.13, 13.1)'),
    'Zec 8:14': ('C', 'purposed disaster when provoked, and did not relent (13.1)'),
}
THREAD = {'M01': 'OT-30 (#2031) Anger and Fear & Awe', 'M20': 'OT-51 (#2052) Anger and Doubt & Discouragement',
          'M25': 'OT-29 (#2030) Anger and Life & Death', 'M64': 'OT-62 (#2063) Anger and Will & Resolve'}
NAMES = {'C': 'carried', 'P': 'parallel', 'D': 'data', 'G': 'gap', 'F': 'forward'}

rows = list(csv.DictReader(open(os.path.join(HERE, 'm02-pairing-done-strands-crossref-v1-20261013.csv'), encoding='utf-8-sig')))
missing = [r['reference'] for r in rows if r['reference'] not in DEC]
assert not missing, missing
head, rest = open(os.path.join(HERE, 'm02-pairing-done-strands-check-gaps-v1-20261013.txt'), encoding='utf-8').read().split('<<TABLES>>')
out = os.path.join(HERE, 'm02-pairing-done-strands-check-v1-20261013.md')
with open(out, 'w', encoding='utf-8') as f:
    f.write(head)
    for m in ['M01', 'M20', 'M25', 'M64']:
        rs = [r for r in rows if r['mcode'] == m]
        cnt = {}
        for r in rs:
            k = DEC[r['reference']][0]
            cnt[k] = cnt.get(k, 0) + 1
        summary = ', '.join(f'{NAMES[k]} {v}' for k, v in sorted(cnt.items(), key=lambda kv: 'CPDFG'.index(kv[0])))
        f.write(f'### {THREAD[m]}: {len(rs)} verses ({summary})\n\n'
                '| Verse | Anger face | Decision | Where, or why |\n|---|---|---|---|\n')
        for r in rs:
            d, why = DEC[r['reference']]
            f.write(f"| {r['reference']} | {r['faces'].split(' / ')[0]} | {NAMES[d]} | {why} |\n")
        f.write('\n')
    f.write(rest)
print(out, {NAMES[k]: sum(1 for r in rows if DEC[r['reference']][0] == k) for k in 'CPDFG'})
