"""
Session-A-v9 Empty Words — Action Script
Based on outputs/markdown/Session-A-v9-Empty-Words-Analysis-20260318.md

Actions:
  1. Add REGISTRY_STATUS flag group with NO_FURTHER_ACTION and RESEARCH_REQUIRED
     to wa_quality_flag_types (registry-level flags stored in wa_data_quality_flags
     with file_id = wa_file_index.id for that word).
  2. Write narrative to word_registry.notes for all 30+2 affected entries.
  3. Set automation_eligible = 0 for Covered (10) + Special (2) words.
  4. Set automation_eligible = 0 for Partial (8) words + flag RESEARCH_REQUIRED.
  5. Add 11 new registry entries for Gap words.
  (new_word engine runs are handled separately per entry.)
"""
import sqlite3
import json
from datetime import datetime, timezone

DB = 'data/bible_research.db'
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')

# ─────────────────────────────────────────────────────────────────────────────
# 1. Add new flag types if missing
# ─────────────────────────────────────────────────────────────────────────────
def ensure_flag_type(flag_group, flag_code, description):
    existing = conn.execute(
        'SELECT id FROM wa_quality_flag_types WHERE flag_code = ?', (flag_code,)
    ).fetchone()
    if existing:
        return existing['id']
    conn.execute(
        'INSERT INTO wa_quality_flag_types (flag_group, flag_code, description) VALUES (?,?,?)',
        (flag_group, flag_code, description)
    )
    return conn.execute(
        'SELECT id FROM wa_quality_flag_types WHERE flag_code = ?', (flag_code,)
    ).fetchone()['id']

nfa_flag_id = ensure_flag_type(
    'REGISTRY_STATUS', 'NO_FURTHER_ACTION',
    'Word has no distinct lexical entry; covered by existing registry words or is a meta-concept. No automation or analysis required.'
)
rr_flag_id = ensure_flag_type(
    'REGISTRY_STATUS', 'RESEARCH_REQUIRED',
    'Partial coverage identified. Manual researcher confirmation needed to verify which existing registry entry covers this concept.'
)
conn.commit()
print(f'Flag type NO_FURTHER_ACTION id: {nfa_flag_id}')
print(f'Flag type RESEARCH_REQUIRED  id: {rr_flag_id}')


# ─────────────────────────────────────────────────────────────────────────────
# 2. Helper — get file_id for a registry no (for wa_data_quality_flags)
# ─────────────────────────────────────────────────────────────────────────────
SPEC = 'Session A v9 Automation'

def get_file_id(registry_no):
    row = conn.execute(
        'SELECT id FROM wa_file_index WHERE registry_id = ?', (str(registry_no),)
    ).fetchone()
    return row['id'] if row else None

def set_registry_flag(registry_no, flag_id, description):
    """Write a wa_data_quality_flags row at file level, idempotent."""
    file_id = get_file_id(registry_no)
    if file_id is None:
        print(f'  WARNING: no wa_file_index for registry_no={registry_no}; skipping flag')
        return
    existing = conn.execute(
        'SELECT id FROM wa_data_quality_flags WHERE file_id = ? AND flag_id = ?',
        (file_id, flag_id)
    ).fetchone()
    if existing:
        return
    max_id = conn.execute('SELECT COALESCE(MAX(id),0) AS m FROM wa_data_quality_flags').fetchone()['m'] + 1
    conn.execute(
        'INSERT INTO wa_data_quality_flags (id, file_id, term_id, flag_id, description, last_changed) VALUES (?,?,NULL,?,?,?)',
        (max_id, file_id, flag_id, description, now())
    )

def update_word(registry_no, notes=None, automation_eligible=None):
    updates = []
    params = []
    if notes is not None:
        updates.append('notes = ?')
        params.append(notes)
    if automation_eligible is not None:
        updates.append('automation_eligible = ?')
        params.append(automation_eligible)
    if not updates:
        return
    params.append(registry_no)
    conn.execute(f'UPDATE word_registry SET {", ".join(updates)} WHERE no = ?', params)


# ─────────────────────────────────────────────────────────────────────────────
# 3. COVERED — No Further Action (10 words + emotion #54)
# ─────────────────────────────────────────────────────────────────────────────
print('\n── COVERED + SPECIAL: setting notes + automation_eligible=0 ──')

covered = [
    (9,  'assent',
     'COVERED — No further action required. '
     'The volitional dimension is carried by faith (#59), trust (#163), and obedience (#114). '
     'Assent as a standalone lexical entry does not exist in Hebrew or Greek — the concept is expressed '
     'through the same roots as belief and faithfulness. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (14, 'blamelessness',
     'COVERED — No further action required. '
     'Fully covered by innocence (#90), integrity (#92), and righteousness (#139). Hebrew H8535 (tam, blameless) '
     'is already captured under integrity. Blamelessness is a derived moral state, not a primary inner-being term. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (21, 'commitment',
     'COVERED — No further action required. '
     'Covered by faithfulness (#60), loyalty (#104), and covenant (#34). The Hebrew concept of commitment is '
     'inseparable from chesed (loving-kindness/loyalty) and emunah (faithfulness) — both in the registry. '
     'No distinct lexical entry exists for commitment alone. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (30, 'contrition',
     'COVERED — No further action required. '
     'Fully covered by repentance (#135), brokenness (#18), and grief (#71). Hebrew H1792 (daka, to be '
     'crushed/contrite) appears within the repentance and grief registries. No distinct lexical separation '
     'exists between contrition and brokenness in the Hebrew text. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (79, 'hopelessness',
     'COVERED — No further action required. '
     'Fully covered by the antonym range within hope (#78) — H3615 (kalah, to fail/cease), H2976 (ya\'ash, to '
     'despair), and G1679 (elpizō in negative contexts). The registry already includes the despair/hopelessness '
     'semantic range. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (88, 'ingratitude',
     'COVERED — No further action required. '
     'Covered by the negative dimension within gratitude (#69). Hebrew and Greek have no distinct word for '
     'ingratitude — it is expressed as the absence of praise/thanksgiving (H3034 yadah; G2168 eucharisteō). '
     'The existing gratitude entry covers both poles. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (95, 'intuition',
     'COVERED — No further action required. '
     'Covered by discernment (#49), wisdom (#174), and insight (#91). "Intuition" is a modern psychological '
     'category without a Hebrew or Greek lexical equivalent. The inner knowing described in Scripture is accessed '
     'through the wisdom/discernment/understanding cluster already in the registry. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (118, 'personality',
     'COVERED — No further action required. '
     'Covered by the anthropological core — soul (#182), heart (#183), spirit (#184), and conscience (#26). '
     '"Personality" is a modern psychological construct with no single lexical equivalent in Scripture. '
     'The totality of inner being expressed through these four entries encompasses what personality means '
     'in the biblical framework. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (133, 'reliability',
     'COVERED — No further action required. '
     'Fully covered by faithfulness (#60). H0529 (emun, faithfulness/reliability) and H0571 (emet, '
     'truth/reliability) are both within the faithfulness registry. No distinct lexical entry for reliability '
     'exists separate from the Hebrew emet/emunah family. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (141, 'self-awareness',
     'COVERED — No further action required. '
     'Covered by conscience (#26) and knowledge (#100). The Hebrew concept of self-knowledge (H3045 yada in '
     'reflexive sense) and Greek syneidēsis (conscience as self-awareness before God) are both in the registry. '
     '"Self-awareness" as a modern psychological category does not map to a distinct biblical lexical entry. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
]

special = [
    (54,  'emotion',
     'SPECIAL HANDLING — No further action required. '
     '"Emotion" is a programme-level category descriptor, not a lexical concept. Hebrew and Greek have no word '
     'for emotion as an abstraction — they name specific emotional states. Marked automation_eligible=0; '
     'used only as a category label in programme documentation. Meta-concept — not a lexical entry. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (195, 'spiritual powers',
     'SPECIAL HANDLING — No further action required. '
     'Cross-registry synthesis placeholder that emerges from the power/authority/might/dominion/energy cluster '
     '(#196–200) through Session D analysis. The strongs_list is correctly empty. Session A should not be run '
     'independently for this entry. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
]

for no, word, notes in covered + special:
    update_word(no, notes=notes, automation_eligible=0)
    set_registry_flag(no, nfa_flag_id,
        f'Covered/Special — no further action. See word_registry.notes for detail. ({word})')
    print(f'  ok: [{no:3}] {word}')

conn.commit()


# ─────────────────────────────────────────────────────────────────────────────
# 4. PARTIAL — Research Required (8 words)
# ─────────────────────────────────────────────────────────────────────────────
print('\n── PARTIAL: setting notes + RESEARCH_REQUIRED flag ──')

partial = [
    (10, 'awareness',
     'PARTIAL — Research required. '
     'Overlaps with conscience (#26, H3045 yada), discernment (#49), and knowledge (#100). '
     'Recommend substituting with perception — H0995 (biyn, to discern/perceive) and G1922 (epignōsis, '
     'full knowledge) yield a productive verse set that more precisely targets the awareness dimension. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (22, 'communion',
     'PARTIAL — Research required. '
     'Partially covered by fellowship (#62, G2842 koinōnia) and love (#103). Koinōnia as an inner-being state '
     'of shared participation is distinct enough to warrant its own entry within fellowship. Recommend redirecting '
     'communion to fellowship (#62) and ensuring G2842 (koinōnia, 19 occurrences) is confirmed as the primary '
     'anchor in that registry. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (36, 'cowardice',
     'PARTIAL — Research required. '
     'Covered partially by fear (#61) — G1167 (deilia, cowardice/timidity) and H4116 (mahar, to be afraid/hasty) '
     'both appear in the fear semantic field. G1167 (used distinctively in 2 Tim 1:7) is a specific inner-being '
     'quality. Recommend confirming the fear registry explicitly includes G1167 as a cowardice sub-sense rather '
     'than treating it as a peripheral term. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (45, 'determination',
     'PARTIAL — Research required. '
     'Partially covered by resolve (#137) and will (#173). The Hebrew concept of a set heart (H3559 kun) and '
     'Greek prothesis (purpose/resolve) appear in related registries. Recommend confirming resolve (#137) covers '
     'H3559 (kun, to be firm/determined; ~219 occurrences) and G4286 (prothesis, purpose/resolve; 12 occurrences). '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (106, 'manipulation',
     'PARTIAL — Research required. '
     'Partially covered by deceit (#40). The specific inner orientation of manipulating others — G3834 (panourgia, '
     'craftiness; 5 occurrences) and H6195 (ormah, shrewdness/cunning) — is present in deceit-adjacent registries '
     'but not given its own space. Recommend confirming deceit covers H4820 (mirmah, deceit; 39 occurrences) and '
     'G1388 (dolos, guile/treachery; 11 occurrences). Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (143, 'sensitivity',
     'PARTIAL — Research required. '
     'Partially covered by compassion (#23). Hebrew H7356 (rachamim, compassion/tender mercies) and G4698 '
     '(splagchnon, compassion as visceral inner sensitivity) are in the compassion semantic field. Recommend '
     'confirming compassion (#23) explicitly includes G4698 (11 occurrences) as the inner-sensitivity dimension. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (145, 'sexuality',
     'PARTIAL — Research required. '
     'Partially covered by sensuality (#144), lust (#105), and whoredom (#171). Hebrew H2181 (zanah) and G4202 '
     '(porneia) appear across those registries. However sexuality as a created, positive inner capacity is not '
     'addressed — only its distorted forms. The positive dimension is partially accessible through desire (#43) '
     'in its somatic dimension. Recommend retaining sexuality as an entry but noting this tension in the registry '
     'record. Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
    (169, 'vulnerability',
     'PARTIAL/GAP — Research required. '
     'Originally listed as Partial; moved to Gap on review — no existing partial coverage identified. '
     'Primary anchor: H6168 (arah, to lay bare/expose; ~15 occurrences). Supporting terms: H6174 (arom, '
     'naked/exposed; 16 occurrences); G1131 (gymnos, naked/vulnerable; 15 NT occurrences — including '
     'Heb 4:13 "naked and laid bare before God"). A new registry entry is recommended. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.'),
]

for no, word, notes in partial:
    update_word(no, notes=notes, automation_eligible=0)
    set_registry_flag(no, rr_flag_id,
        f'Partial coverage — researcher must confirm existing registry entry. See word_registry.notes. ({word})')
    print(f'  ok: [{no:3}] {word}')

conn.commit()


# ─────────────────────────────────────────────────────────────────────────────
# 5. Add 11 new registry entries for genuine gaps
# ─────────────────────────────────────────────────────────────────────────────
print('\n── GAP WORDS: adding new word_registry entries ──')

# id is text (e.g. '084a') in existing records? Check actual format.
# no is integer. Max is 200. New entries get 201+.
# id field: existing entries use zero-padded 3-digit strings like '009'.

def next_no():
    return conn.execute('SELECT MAX(no)+1 AS n FROM word_registry').fetchone()['n']

def make_id(no):
    return f'{no:03d}'

gap_words = [
    # (replaces_no, word, category_hint, notes, strongs_list_json)
    (84,  'image',
     'Anthropology',
     'GAP — New entry. Replaces "image of God" (#84). Priority 1. '
     'Primary anchor: H6754 (tselem, image/likeness; 17 occurrences — Gen 1:26-27 central). '
     'Supporting: H1823 (demuth, likeness; 25 occurrences); G1504 (eikōn, image; 23 NT occurrences — '
     'Col 1:15, 2 Cor 4:4, Rom 8:29). HIGHEST PRIORITY GAP — imago Dei terms absent from all existing '
     'registries. Foundational to the entire anthropological framework. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"H6754"},{"strong":"H1823"},{"strong":"G1504"}]'),
    (161, 'transformation',
     'Inner Life',
     'GAP — New entry. Replaces "transformation" (#161). Priority 2. '
     'Primary anchor: G3339 (metamorphoō, to transform; 4 occurrences — Rom 12:2, 2 Cor 3:18, Matt 17:2, '
     'Mk 9:2). Supporting: G0342 (anakainōsis, renewal/transformation; 2 occurrences — Rom 12:2, Tit 3:5); '
     'G3345 (metaschēmatizō; 5 occurrences); H2498 (chalaph, to renew/pass through; ~29 occurrences). '
     'High theological priority — Romans 12:2 anchor. Links with renewal (#134) and likeness (#25 new). '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"G3339"},{"strong":"G0342"},{"strong":"G3345"},{"strong":"H2498"}]'),
    (12,  'treachery',
     'Sin & Vice',
     'GAP — New entry. Replaces "betrayal" (#12). Priority 3. '
     'Primary anchor: H0898 (bagad, to act treacherously; 51 occurrences). '
     'Supporting: H4820 (mirmah, deceit in covenant contexts; 39 occurrences); G4273 (prodotēs, traitor; '
     '3 NT occurrences). Betrayal as relational breach of covenantal trust is distinct from deceit. '
     'H0898 concentrated in Psalms and prophets. "Treachery" is more precise; "betrayal" is registry heading. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"H0898"},{"strong":"H4820"},{"strong":"G4273"}]'),
    (82,  'name',
     'Anthropology',
     'GAP — New entry. Replaces "identity" (#82). Priority 4. '
     'Primary anchor: H8034 (shem, name/identity/character; 864 occurrences). '
     'Supporting: G3686 (onoma, name; 228 NT occurrences, particularly in identity and revelation contexts); '
     'H3045 (yada, to know — God\'s knowing of persons). In biblical anthropology a person\'s name is their '
     'identity — character, reputation, relational standing before God. H8034 is one of the most frequent '
     'Hebrew terms; rich inner-being dimension (Prov 22:1; Isa 43:1; Rev 2:17). '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"H8034"},{"strong":"G3686"}]'),
    (136, 'resentment',
     'Emotion',
     'GAP — New entry. Replaces "resentment" (#136). Priority 5. '
     'Primary anchor: H7107 (qatsaph, to be wrathful/resentful; 46 occurrences). '
     'Supporting: H5006 (na\'ats, to spurn with contempt; 25 occurrences); G3949 (parorgizō, to provoke '
     'to resentment; 2 NT occurrences). Distinct from anger (#4) in temporal persistence and from '
     'bitterness (#13) in relational direction. H7107 not covered in any existing registry. '
     'Primary verse set in Psalms and prophets. Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"H7107"},{"strong":"H5006"},{"strong":"G3949"}]'),
    (169, 'vulnerability',
     'Anthropology',
     'GAP — New entry. Replaces "vulnerability" (#169). Priority 6. '
     'Primary anchor: H6168 (arah, to lay bare/expose; ~15 occurrences). '
     'Supporting: H6174 (arom, naked/exposed; 16 occurrences); G1131 (gymnos, naked/vulnerable; '
     '15 NT occurrences — including Heb 4:13 "naked and laid bare before God"). Inner state of being '
     'uncovered and exposed before God and before others. Heb 4:13 provides strong NT theological basis. '
     '"Vulnerability" is a modern overlay on the nakedness/exposure word family. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"H6168"},{"strong":"H6174"},{"strong":"G1131"}]'),
    (37,  'blindness (spiritual)',
     'Sin & Vice',
     'GAP — New entry. Replaces "darkening" (#37). Priority 7. '
     'Primary anchor: G4656 (skotizō, to darken; 8 occurrences — including Rom 1:21, Rev 9:2). '
     'Supporting: G4457 (pōrōsis, hardening/blindness; 3 occurrences — Mk 3:5, Rom 11:25, Eph 4:18); '
     'G5185 (tuphlos, blind, in inner-state uses); H6272 (atam, to be darkened; rare). '
     'Darkening of mind and heart as inner-being state (Rom 1:21, Eph 4:18) not represented in any '
     'existing registry. Distinct from hardness (#74) in cognitive/perceptive dimension. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"G4656"},{"strong":"G4457"},{"strong":"G5185"}]'),
    (101, 'sloth',
     'Sin & Vice',
     'GAP — New entry. Replaces "laziness" (#101). Priority 8. '
     'Primary anchor: H6103 (atslah, slothfulness; 15 occurrences — concentrated in Proverbs). '
     'Supporting: H6102 (atsel, sluggard; 14 occurrences — Proverbs); H7503 (raphah, to be slack/let drop; '
     '~46 occurrences); G3636 (oknēros, lazy/slothful; 3 NT occurrences). Clearly defined semantic field '
     'not covered by existing entries. Proverbs concentration makes this significant wisdom-literature '
     'inner-being term. Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"H6103"},{"strong":"H6102"},{"strong":"H7503"},{"strong":"G3636"}]'),
    (25,  'likeness',
     'Anthropology',
     'GAP — New entry. Replaces "conformity" (#25). Priority 9. '
     'Primary anchor: G3339 (metamorphoō, to transform/be conformed; 6 occurrences). '
     'Supporting: G4833 (symmorphos, conformed to; 2 occurrences — Rom 8:29, Phil 3:21); G3345 '
     '(metaschēmatizō, to change form; 5 occurrences); H1823 (demuth, likeness). Inner transformation '
     'into Christlikeness is a distinct and high-value theological concept not covered by any existing '
     'entry. Links naturally with transformation (#161 new). '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"G4833"},{"strong":"G3339"},{"strong":"G3345"},{"strong":"H1823"}]'),
    (38,  'deadness',
     'Sin & Vice',
     'GAP — New entry. Replaces "deadness" (#38). Priority 10. '
     'Primary anchor: G3498 (nekros in inner-state sense — Eph 2:1, Col 2:13; ~7 targeted verses). '
     'Supporting: H4191 (muth in spiritual-death contexts); G2348 (thnēskō, to die, in spiritual uses). '
     'Spiritual deadness as inner state is distinct anthropological category in Paul\'s theology. Related to '
     'hardness (#74) but semantically separate — deadness describes absence of spiritual life while hardness '
     'describes resistance. Small but theologically significant verse set. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"G3498"},{"strong":"H4191"},{"strong":"G2348"}]'),
    (119, 'being',
     'Anthropology',
     'GAP — New entry. Replaces "personhood" (#119). Priority 11. '
     'Primary anchor: H5315 (nephesh as the ontological living being — distinct from nephesh as soul/inner life). '
     'Supporting: G5590 (psychē as the individuated self — distinct from psychē as soul/emotion). '
     'Partially overlaps with soul (#182) but the ontological dimension of personhood (the person as a whole '
     'being, not just their inner life) deserves explicit treatment. First confirm whether soul (#182) covers '
     'the personhood dimension of nephesh explicitly; if so, this entry may be merged. '
     'Source: Session-A-v9-Empty-Words-Analysis-20260318.',
     '[{"strong":"H5315"},{"strong":"G5590"}]'),
]

new_entries = []  # (no, word) for reporting
for replaces_no, word, category, notes, strongs_json in gap_words:
    new_no = next_no()
    new_id = make_id(new_no)
    # Update the old entry's notes to indicate it has been replaced
    old_row = conn.execute('SELECT notes FROM word_registry WHERE no = ?', (replaces_no,)).fetchone()
    old_notes = (old_row['notes'] or '') if old_row else ''
    replacement_note = f'REPLACED by new entry #{new_no} ("{word}"). {old_notes}'.strip()
    conn.execute('UPDATE word_registry SET notes = ?, automation_eligible = 0 WHERE no = ?',
                 (replacement_note, replaces_no))

    conn.execute(
        '''INSERT INTO word_registry
               (id, no, word, source_list, category_hint, phase1_status,
                notes, automation_eligible, strongs_list)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (new_id, new_no, word, 'Session A v9 Gap Analysis', category,
         'Pending', notes, 1, strongs_json)
    )
    conn.commit()
    new_entries.append((new_no, word))
    print(f'  added: [{new_no:3}] {word}  (replaces #{replaces_no})')

print(f'\nNew entries created: {len(new_entries)}')
print('\nNew registry numbers for new_word runs:')
for no, word in new_entries:
    # Show the strongs list for the new_word command
    strongs_row = conn.execute('SELECT strongs_list FROM word_registry WHERE no = ?', (no,)).fetchone()
    strongs = json.loads(strongs_row['strongs_list'])
    terms_str = ','.join(s['strong'] for s in strongs)
    print(f'  [{no:3}] {word:30} --registry={no} --terms={terms_str}')

conn.close()
print('\nDone.')
