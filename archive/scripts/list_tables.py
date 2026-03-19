from analytics.db_client import get_connection
conn = get_connection()
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
for t in tables:
    print(t[0])
conn.close()
