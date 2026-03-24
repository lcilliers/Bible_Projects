import sqlite3
conn = sqlite3.connect("data/bible_research.db")
tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
print("\n".join(tables))
conn.close()
