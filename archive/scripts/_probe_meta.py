"""Quick probe: find run log table and researcher_approved field location."""
from engine.db import get_connection
import sys, os
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

conn = get_connection()
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
for t in tables:
    name = t['name']
    if 'run' in name.lower() or 'log' in name.lower():
        print('Table: ' + name)
        cols = conn.execute('PRAGMA table_info(' + name + ')').fetchall()
        for c in cols:
            print('  ' + c['name'])
        # Show soul rows
        try:
            rows = conn.execute('SELECT * FROM ' + name + ' WHERE file_id=36 ORDER BY id DESC LIMIT 3').fetchall()
            for r in rows:
                print('  ROW:', dict(r))
        except Exception as e:
            print('  (no file_id col or error: ' + str(e) + ')')
        print()
