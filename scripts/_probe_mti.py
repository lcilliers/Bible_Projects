"""Probe MTI tables."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.db import get_connection
conn = get_connection()
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%mti%'").fetchall()
for t in tables:
    name = t['name']
    print('Table:', name)
    cols = conn.execute('PRAGMA table_info(' + name + ')').fetchall()
    for c in cols:
        print('  col:', c['name'])
    cnt = conn.execute('SELECT COUNT(*) FROM ' + name).fetchone()[0]
    print('  rows:', cnt)
    # Show sample rows where registry_id=182 or strongs related to soul
    try:
        rows = conn.execute('SELECT * FROM ' + name + ' LIMIT 3').fetchall()
        for r in rows:
            print('  sample:', dict(r))
    except Exception as e:
        print('  error:', e)
    print()
