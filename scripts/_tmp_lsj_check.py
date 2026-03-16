import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection
conn = get_connection()

total_g = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language='Greek'").fetchone()[0]
lsj_set = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language='Greek' AND lsj_entry IS NOT NULL AND lsj_entry != ''").fetchone()[0]
print(f"Greek terms total:    {total_g}")
print(f"lsj_entry set:        {lsj_set}")
print(f"lsj_entry NULL/empty: {total_g - lsj_set}")

print()
print("=== Greek terms with no meaning: lsj_entry status ===")
for r in conn.execute("""
    SELECT id, transliteration,
           CASE WHEN lsj_entry IS NULL THEN 'lsj=NULL'
                WHEN lsj_entry='' THEN 'lsj=EMPTY'
                ELSE 'lsj=SET' END as lsj_status,
           substr(lsj_entry,1,80) as lsj_preview
    FROM wa_term_inventory
    WHERE language='Greek' AND (meaning IS NULL OR meaning='')
    ORDER BY lsj_status, id
""").fetchall():
    print(f"  id={r[0]:4d}  {r[1]:22s}  {r[2]}  {r[3] or ''}")

print()
print("=== Greek terms WITH meaning: do they also have lsj_entry? ===")
both_g  = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language='Greek' AND meaning IS NOT NULL AND meaning!='' AND lsj_entry IS NOT NULL AND lsj_entry!=''").fetchone()[0]
m_only  = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE language='Greek' AND meaning IS NOT NULL AND meaning!='' AND (lsj_entry IS NULL OR lsj_entry='')").fetchone()[0]
print(f"  meaning + lsj_entry both set: {both_g}")
print(f"  meaning set, lsj_entry empty: {m_only}")

conn.close()
