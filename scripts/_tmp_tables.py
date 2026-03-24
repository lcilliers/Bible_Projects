from analytics.db_client import get_connection
c = get_connection()
tbls = c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
for t in tbls:
    if "flag" in t[0].lower() or "quality" in t[0].lower():
        print(t[0])
