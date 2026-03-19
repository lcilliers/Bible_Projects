import sqlite3
conn = sqlite3.connect('data/bible_research.db')
tbls = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
for tbl in tbls:
    fks = conn.execute(f'PRAGMA foreign_key_list({tbl})').fetchall()
    for fk in fks:
        ref_table = fk[2]
        if 'meaning' in ref_table.lower() or 'lsj' in ref_table.lower() or 'bdb' in ref_table.lower():
            print(f'{tbl} -> {ref_table}: {fk}')

# Also check what tables wa_meaning_parsed itself depends on
print('\nwa_meaning_parsed FK:')
for fk in conn.execute('PRAGMA foreign_key_list(wa_meaning_parsed)').fetchall():
    print(' ', fk)

print('\nwa_lsj_parsed FK:')
for fk in conn.execute('PRAGMA foreign_key_list(wa_lsj_parsed)').fetchall():
    print(' ', fk)
