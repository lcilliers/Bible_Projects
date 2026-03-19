import sqlite3

conn = sqlite3.connect('data/bible_research.db')
conn.row_factory = sqlite3.Row

r = conn.execute('SELECT * FROM word_registry WHERE word = ?', ('peace',)).fetchone()

lines = ['# word_registry — peace\n']
for k in r.keys():
    lines.append(f'| {k} | {r[k]} |')

with open('outputs/markdown/inspect_peace_registry.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Written to outputs/markdown/inspect_peace_registry.md')
