import sqlite3, pathlib
sql = pathlib.Path("g:/My Drive/Bible_study_projects/data/schema/create_tables.sql").read_text(encoding="utf-8")
conn = sqlite3.connect(":memory:")
conn.executescript(sql)
tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
print(f"Tables created: {len(tables)}")
for t in tables:
    n = conn.execute(f"SELECT COUNT(*) FROM pragma_table_info('{t}')").fetchone()[0]
    print(f"  {t}: {n} cols")
conn.close()
print("Syntax OK")
