"""Check H4578 and H5397 current state, flags, and spirit overlap."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.db import get_connection
conn = get_connection()

# cross-registry links schema
cols = conn.execute('PRAGMA table_info(wa_cross_registry_links)').fetchall()
print('wa_cross_registry_links cols:', [c['name'] for c in cols])
print()

# H7307 (ruach) in mti_terms - is spirit/breath's ruach the same as neshamah?
mti_ruach = conn.execute(
    'SELECT id, strongs_number, gloss, owning_registry, owning_word FROM mti_terms WHERE strongs_number LIKE "H7307%"'
).fetchall()
print('H7307 (ruach) in mti_terms:')
for r in mti_ruach:
    print(' ', dict(r))
print()

# H4578 and H5397 current state in file_id=36
inv = conn.execute(
    'SELECT ti.id, ti.strongs_number, ti.step_search_gloss, ti.occurrence_count, '
    'COUNT(DISTINCT vr.id) as verse_count, COUNT(DISTINCT vtl.id) as link_count '
    'FROM wa_term_inventory ti '
    'LEFT JOIN wa_verse_records vr ON vr.term_inv_id = ti.id '
    'LEFT JOIN wa_verse_term_links vtl ON vtl.term_inv_id = ti.id '
    'WHERE ti.file_id=36 AND ti.strongs_number IN ("H4578","H5397") '
    'GROUP BY ti.id'
).fetchall()
print('H4578 and H5397 in file_id=36 (soul):')
for r in inv:
    print('  strongs:', r['strongs_number'],
          '| gloss:', r['step_search_gloss'],
          '| occ_count:', r['occurrence_count'],
          '| verses:', r['verse_count'],
          '| links:', r['link_count'])
print()

# Quality flags
flags = conn.execute(
    'SELECT dqf.term_id, qt.flag_code, dqf.description '
    'FROM wa_data_quality_flags dqf '
    'JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id '
    'WHERE dqf.file_id=36 AND dqf.term_id IN ("H4578","H5397")'
).fetchall()
print('Quality flags on H4578, H5397:')
for f in flags:
    print(' ', f['term_id'], '|', f['flag_code'], '|', f['description'])
if not flags:
    print('  (none)')
print()

# Does H5397 (neshamah) appear anywhere in spirit word study?
spirit_terms = conn.execute(
    'SELECT ti.strongs_number, fi.word FROM wa_term_inventory ti '
    'JOIN wa_file_index fi ON fi.id=ti.file_id '
    'WHERE ti.strongs_number="H5397"'
).fetchall()
print('H5397 in wa_term_inventory (all registries):')
for r in spirit_terms:
    print('  word:', r['word'], '| strongs:', r['strongs_number'])
print()

# Was H5397 in STEP's spirit cluster? check spirit file_id
spirit_fi = conn.execute('SELECT id FROM wa_file_index WHERE word_registry_fk=184').fetchone()
if spirit_fi:
    print('Spirit file_id:', spirit_fi['id'])
    sp_terms = conn.execute(
        'SELECT strongs_number, step_search_gloss FROM wa_term_inventory WHERE file_id=?',
        (spirit_fi['id'],)
    ).fetchall()
    print('Spirit terms:', [r['strongs_number'] for r in sp_terms])
print()

# Also check: does any other word registry list H4578 or H5397 as a term?
for code in ['H4578', 'H5397']:
    mti_all = conn.execute(
        'SELECT id, strongs_number, gloss, owning_registry, owning_word FROM mti_terms WHERE strongs_number=?',
        (code,)
    ).fetchall()
    print(f'mti_terms for {code} (ALL registries):')
    for r in mti_all:
        print(' ', dict(r))
