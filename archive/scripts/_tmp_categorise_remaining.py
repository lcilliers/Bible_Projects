"""Categorise remaining unclassified terms by type."""
import sqlite3, csv, os

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

remaining = conn.execute('''
    SELECT mt.id as mti_id, mt.strongs_number, mt.transliteration, mt.gloss,
           wr.no as reg_no, wr.word,
           COUNT(vr.id) as verse_count
    FROM mti_terms mt
    JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
      AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
    JOIN wa_file_index fi ON fi.id = ti.file_id
    JOIN word_registry wr ON wr.id = fi.word_registry_fk
    JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
    WHERE mt.delete_flagged = 0
      AND mt.status IN ('extracted', 'extracted_thin')
      AND NOT EXISTS (
          SELECT 1 FROM verse_context vc
          WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
      )
    GROUP BY mt.id
    ORDER BY mt.strongs_number
''').fetchall()

def classify(gloss, strongs):
    g = (gloss or '').lower().strip()

    # Pronouns
    pronouns = ['you [', 'i myself', 'whom', 'who?', 'what?', 'which?',
                'this', 'that [f', 'that [m', 'these', 'those', 'self',
                'one another', 'you (', 'he/', 'she/', 'them', 'we']
    if any(w in g for w in pronouns):
        return 'PRONOUN'

    # Exact-match particles
    exact_particles = {'also', 'not', 'but', 'so', 'thus', 'then', 'yet',
                       'because', 'before', 'after', 'till', 'until', 'much',
                       'very', 'again', 'only', 'even', 'still', 'now',
                       'here', 'there', 'nothing', 'none', 'except', 'surely',
                       'perhaps', 'whether', 'lest', 'how'}
    if g in exact_particles:
        return 'PARTICLE'

    # Prepositions
    preps = ['from/', 'with/', 'to/', 'in/', 'on/', 'by/', 'for/', 'at/', 'of/']
    if any(g.startswith(w) for w in preps):
        return 'PREPOSITION'
    exact_preps = {'from', 'with', 'upon', 'into', 'between', 'beside',
                   'behind', 'above', 'below', 'under', 'over', 'through',
                   'against', 'among', 'around', 'beyond', 'near'}
    if g in exact_preps:
        return 'PREPOSITION'

    # Physical/spatial nouns
    physical = ['hand', 'foot', 'head', 'face', 'mouth', 'bone', 'flesh',
                'blood', 'stone', 'water', 'fire', 'earth', 'land', 'place',
                'house', 'city', 'gate', 'door', 'wall', 'mountain', 'river',
                'sea', 'field', 'tree', 'bread', 'wine', 'oil', 'gold',
                'silver', 'sword', 'bow', 'arrow', 'horse', 'chariot',
                'garment', 'tent', 'altar', 'vessel', 'animal', 'goat',
                'sheep', 'ox', 'bird', 'fish', 'heap', 'wheel', 'bowl',
                'scroll', 'knife', 'cord', 'line', 'spring', 'dung',
                'rotten', 'stork', 'vulture', 'sand', 'nest', 'wing',
                'nail', 'pit', 'enemy', 'scourge', 'craft']
    if any(w in g for w in physical):
        return 'PHYSICAL_NOUN'

    # Proper nouns / place names
    if g.startswith('[') or g[0:1].isupper():
        # Check for known proper nouns
        proper = ['Kue', 'Uzza', 'Gilgal', 'Garden', 'Holy Place']
        if any(w in (gloss or '') for w in proper):
            return 'PROPER_NOUN'
    if 'constellation' in g:
        return 'PROPER_NOUN'

    # Quantifiers / numerics
    if any(w in g for w in ['all', 'every', 'many', 'few', 'number']):
        return 'QUANTIFIER'

    # Generic verbs (action verbs with no inner-being content)
    generic_verbs = ['to come', 'to go', 'to send', 'to put', 'to set',
                     'to take', 'to give', 'to bring', 'to carry',
                     'to stand', 'to sit', 'to lie', 'to rise',
                     'to fall', 'to build', 'to break', 'to cut',
                     'to strike', 'to kill', 'to die', 'to eat',
                     'to drink', 'to run', 'to walk', 'to turn',
                     'to find', 'to gather', 'to plant', 'to multiply',
                     'to fill', 'to open', 'to close', 'to cover',
                     'to write', 'to read', 'to dwell', 'to leave',
                     'to make: do', 'to cast', 'to pour']
    if any(w in g for w in generic_verbs):
        return 'GENERIC_VERB'

    return 'NEEDS_ASSESSMENT'


classified = []
for r in remaining:
    cat = classify(r['gloss'], r['strongs_number'])
    classified.append({
        'category': cat,
        'mti_id': r['mti_id'],
        'strongs': r['strongs_number'],
        'transliteration': r['transliteration'],
        'gloss': r['gloss'],
        'reg_no': r['reg_no'],
        'word': r['word'],
        'verses': r['verse_count'],
    })

# Summary
from collections import defaultdict
cat_summary = defaultdict(lambda: {'terms': 0, 'verses': 0})
for c in classified:
    cat_summary[c['category']]['terms'] += 1
    cat_summary[c['category']]['verses'] += c['verses']

tv = sum(v['verses'] for v in cat_summary.values())
print('REMAINING TERMS BY CATEGORY')
print('=' * 60)
print(f'{"Category":>20s}  {"Terms":>6s}  {"Verses":>7s}  {"% verses":>8s}')
print('-' * 50)
for cat in sorted(cat_summary.keys()):
    s = cat_summary[cat]
    pct = s['verses'] / tv * 100 if tv else 0
    print(f'{cat:>20s}  {s["terms"]:>6d}  {s["verses"]:>7d}  {pct:>7.1f}%')
print(f'{"TOTAL":>20s}  {sum(v["terms"] for v in cat_summary.values()):>6d}  {tv:>7d}')

particle_cats = ('PRONOUN', 'PARTICLE', 'PREPOSITION', 'PHYSICAL_NOUN',
                 'PROPER_NOUN', 'QUANTIFIER', 'GENERIC_VERB')
particle_terms = [c for c in classified if c['category'] in particle_cats]
particle_verses = sum(c['verses'] for c in particle_terms)
needs = [c for c in classified if c['category'] == 'NEEDS_ASSESSMENT']
needs_verses = sum(c['verses'] for c in needs)

print(f'\nBulk-processable candidates: {len(particle_terms)} terms, {particle_verses:,} verses')
print(f'Needs assessment (full classification): {len(needs)} terms, {needs_verses:,} verses')

# Write full CSV
outpath = 'outputs/investigations/remaining-terms-categorised-20260402.csv'
with open(outpath, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['category', 'mti_id', 'strongs', 'transliteration',
                                       'gloss', 'reg_no', 'word', 'verses'])
    w.writeheader()
    for c in sorted(classified, key=lambda x: (x['category'], -x['verses'])):
        w.writerow(c)
print(f'\nFull CSV: {outpath} ({len(classified)} rows)')

conn.close()
