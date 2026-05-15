import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

# Directive's claimed (mti_id, strongs) pairs from the SCOPE table
DIRECTIVE_TERMS = [
    (1299, 'H1288'), (888,  'G5485'), (984,  'H2603A'), (889,  'H2580'),
    (5470, 'G5483'), (5471, 'G5487'), (494,  'G2107'),  (2330, 'H2587'),
    (1301, 'G5486'), (989,  'H2604'), (795,  'H7521'),  (632,  'H3190'),
    (542,  'H2895'), (6837, 'G1435'), (2976, 'H7862'),  (633,  'H2868'),
]

print(f'Verifying {len(DIRECTIVE_TERMS)} (mti_id, strongs) pairs against DB:')
print()
mismatches = []
for mti_id, claimed_strongs in DIRECTIVE_TERMS:
    r = c.execute("""SELECT id, strongs_number, transliteration, cluster_code,
                            COALESCE(delete_flagged,0) deleted
                     FROM mti_terms WHERE id=?""", (mti_id,)).fetchone()
    if not r:
        mismatches.append((mti_id, claimed_strongs, 'NOT FOUND'))
        print(f'  mti_id={mti_id} claimed_strongs={claimed_strongs}  ❌ NOT FOUND')
        continue
    if r['strongs_number'] != claimed_strongs:
        mismatches.append((mti_id, claimed_strongs, f"DB has strongs={r['strongs_number']}"))
        print(f"  mti_id={mti_id} claimed_strongs={claimed_strongs}  ❌ DB has {r['strongs_number']}")
        continue
    if r['cluster_code'] != 'M39':
        mismatches.append((mti_id, claimed_strongs, f"cluster_code={r['cluster_code']}"))
        print(f"  mti_id={mti_id} {claimed_strongs:<7}  ❌ cluster_code={r['cluster_code']}")
        continue
    if r['deleted']:
        mismatches.append((mti_id, claimed_strongs, 'delete_flagged=1'))
        print(f'  mti_id={mti_id} {claimed_strongs:<7}  ❌ delete_flagged')
        continue
    print(f"  mti_id={mti_id:<5} {claimed_strongs:<7} {r['transliteration']:<14} ✓")

print()
print(f'Mismatches: {len(mismatches)}')

# Also verify the 16 directive terms cover every active M39 term (no orphans)
db_terms = list(c.execute("""SELECT id, strongs_number FROM mti_terms
                             WHERE cluster_code='M39' AND COALESCE(delete_flagged,0)=0"""))
db_set = set(r['id'] for r in db_terms)
dir_set = set(t[0] for t in DIRECTIVE_TERMS)
missing_from_dir = db_set - dir_set
extra_in_dir = dir_set - db_set
print(f'M39 active terms in DB: {len(db_set)}; in directive: {len(dir_set)}')
print(f'M39 active terms missing from directive: {missing_from_dir}')
print(f'Directive terms not active M39: {extra_in_dir}')
