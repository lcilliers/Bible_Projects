"""Add all standard OSIS book code variants to book_code_variants table."""
import sqlite3

conn = sqlite3.connect('data/bible_research.db')

# OSIS standard code -> book_id mapping for codes that differ from the DB's primary codes
osis_variants = [
    # OT
    ('Exod',   2),   # Exo
    ('Deut',   5),   # Deu
    ('Josh',   6),   # Jos
    ('Ruth',   8),   # Rut
    ('1Sam',   9),   # 1Sa
    ('2Sam',  10),   # 2Sa
    ('1Kgs',  11),   # 1Ki
    ('2Kgs',  12),   # 2Ki
    ('1Chr',  13),   # 1Ch
    ('2Chr',  14),   # 2Ch
    ('Ezra',  15),   # Ezr
    ('Esth',  17),   # Est
    ('Ps',    19),   # Psa  (OSIS uses Ps for Psalms)
    ('Eccl',  21),   # Ecc
    ('Song',  22),   # Son
    ('Ezek',  26),   # Eze
    ('Joel',  29),   # Joe
    ('Amos',  30),   # Amo
    ('Obad',  31),   # Obd
    ('Jonah', 32),   # Jon
    ('Zeph',  36),   # Zep
    ('Zech',  38),   # Zec
    # NT
    ('Matt',  40),   # Mat
    ('Mark',  41),   # Mar
    ('Luke',  42),   # Luk
    ('John',  43),   # Joh
    # Acts and Prov already added
    ('Phil',  50),   # Php
    ('1Thess',52),   # 1Th
    ('2Thess',53),   # 2Th
    ('1Tim',  54),   # 1Ti
    ('2Tim',  55),   # 2Ti
    ('Titus', 56),   # Tit
    ('Phlm',  57),   # Phm
    ('Jas',   59),   # Jam
    ('1Pet',  60),   # 1Pe
    ('2Pet',  61),   # 2Pe
    ('1John', 62),   # 1Jn
    ('2John', 63),   # 2Jn
    ('3John', 64),   # 3Jn
]

added = 0
skipped = 0
for code, book_id in osis_variants:
    existing = conn.execute(
        'SELECT 1 FROM book_code_variants WHERE code = ?', (code,)
    ).fetchone()
    if existing:
        skipped += 1
    else:
        conn.execute(
            'INSERT INTO book_code_variants (code, book_id) VALUES (?, ?)',
            (code, book_id)
        )
        added += 1

conn.commit()
print(f'Added {added} OSIS variant codes, skipped {skipped} already present.')

# Verify a few
for code in ('Matt', 'Mark', 'Luke', 'John', 'Jas', '1Pet', 'Ezek'):
    row = conn.execute('SELECT book_id FROM book_code_variants WHERE code = ?', (code,)).fetchone()
    print(f'  {code} -> {row[0] if row else "NOT FOUND"}')

conn.close()
