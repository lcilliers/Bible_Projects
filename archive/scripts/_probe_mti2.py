"""Probe MTI data for soul registry."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.db import get_connection
conn = get_connection()

rows = conn.execute(
    "SELECT id, strongs_number, gloss, owning_registry, owning_word FROM mti_terms WHERE owning_registry_fk=182"
).fetchall()
print('mti_terms for registry 182:')
for r in rows:
    print(' ', dict(r))
print('total:', len(rows))
print()

# Check cross-refs pointing TO soul strongs
soul_strongs = ['H5315G','H5315H','H5315','H5314','H5397','H4578','G5590','G5590G','G5591']
print('Strongs numbers in mti_terms (any registry):')
for s in soul_strongs:
    cnt = conn.execute('SELECT COUNT(*) FROM mti_terms WHERE strongs_number=?', (s,)).fetchone()[0]
    if cnt:
        print(' ', s, '- rows:', cnt)
