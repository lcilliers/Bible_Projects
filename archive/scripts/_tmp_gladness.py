import sys
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.db_client import get_connection
conn = get_connection(); c = conn.cursor()
c.execute("SELECT id, word, phase1_status FROM word_registry WHERE word LIKE '%gladness%'")
for r in c.fetchall(): print(tuple(r))
conn.close()
