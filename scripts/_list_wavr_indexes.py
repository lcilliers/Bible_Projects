from analytics.db_client import get_connection
conn = get_connection()
idxs = conn.execute(
    "SELECT name, sql FROM sqlite_master WHERE type='index' AND tbl_name='wa_verse_records'"
).fetchall()
for i in idxs:
    print(i[0], "|", i[1])
conn.close()
