import sqlite3, sys
db = sys.argv[1] if len(sys.argv) > 1 else "database/bible_research.db"
c = sqlite3.connect(db).cursor()
tables = c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
for (t,) in tables:
    cols = c.execute(f"PRAGMA table_info({t})").fetchall()
    print(f"\n=== {t} ===")
    for col in cols:
        print(f"  {col[1]:35s} {col[2]:20s} pk={col[5]} nn={col[3]}")
