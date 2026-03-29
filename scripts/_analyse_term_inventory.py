"""Deep analysis of wa_term_inventory — standalone, no joins to other tables."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

# Schema
print("=== SCHEMA ===")
for c in conn.execute("PRAGMA table_info(wa_term_inventory)").fetchall():
    print(f"  {c['cid']:>2} {c['name']:<25} {c['type']:<10} notnull={c['notnull']}  default={c['dflt_value']}")

total = conn.execute("SELECT COUNT(*) FROM wa_term_inventory").fetchone()[0]
active = conn.execute("SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0").fetchone()[0]
print(f"\n=== ROW COUNTS ===")
print(f"  Total: {total}   Active: {active}   Deleted: {total - active}")

print(f"\n=== COLUMN-BY-COLUMN (active rows) ===")

def col_report(name, extra_sql=""):
    nulls = conn.execute(f"SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0 AND {name} IS NULL").fetchone()[0]
    empty = 0
    try:
        empty = conn.execute(f"SELECT COUNT(*) FROM wa_term_inventory WHERE delete_flagged = 0 AND {name} = ''").fetchone()[0]
    except:
        pass
    populated = active - nulls - empty
    print(f"\n{name}:")
    print(f"  Populated: {populated}   NULL: {nulls}   Empty: {empty}")
    if extra_sql:
        for r in conn.execute(extra_sql).fetchall():
            vals = list(r)
            print(f"  {vals}")

# file_id
col_report("file_id")
file_dist = conn.execute(
    "SELECT COUNT(DISTINCT file_id) as files, MIN(file_id), MAX(file_id) "
    "FROM wa_term_inventory WHERE delete_flagged = 0"
).fetchone()
print(f"  Distinct file_ids: {file_dist[0]}  Range: {file_dist[1]}-{file_dist[2]}")
top_files = conn.execute(
    "SELECT file_id, COUNT(*) as c FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY file_id ORDER BY c DESC LIMIT 5"
).fetchall()
print(f"  Largest files: {', '.join(f'{r[0]}({r[1]})' for r in top_files)}")

# language
col_report("language")
for r in conn.execute(
    "SELECT language, COUNT(*) as c FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY language ORDER BY c DESC"
).fetchall():
    print(f"  {r[0] or 'NULL':<10} {r[1]:>5}")

# strongs_number
col_report("strongs_number")
distinct = conn.execute("SELECT COUNT(DISTINCT strongs_number) FROM wa_term_inventory WHERE delete_flagged = 0").fetchone()[0]
print(f"  Distinct strongs: {distinct}")
dup_within = conn.execute(
    "SELECT COUNT(*) FROM (SELECT strongs_number, file_id, COUNT(*) as c "
    "FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY strongs_number, file_id HAVING c > 1)"
).fetchone()[0]
print(f"  Duplicate within same file: {dup_within}")
dup_across = conn.execute(
    "SELECT COUNT(*) FROM (SELECT strongs_number, COUNT(DISTINCT file_id) as c "
    "FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY strongs_number HAVING c > 1)"
).fetchone()[0]
print(f"  Appearing in multiple files: {dup_across}")

# term_id
col_report("term_id")
distinct_tid = conn.execute("SELECT COUNT(DISTINCT term_id) FROM wa_term_inventory WHERE delete_flagged = 0").fetchone()[0]
print(f"  Distinct term_ids: {distinct_tid}")

# transliteration
col_report("transliteration")

# step_search_gloss
col_report("step_search_gloss")

# word_analysis_gloss
col_report("word_analysis_gloss")

# occurrence_count
col_report("occurrence_count")
stats = conn.execute(
    "SELECT MIN(occurrence_count), MAX(occurrence_count), AVG(occurrence_count), "
    "SUM(CASE WHEN occurrence_count = 0 THEN 1 ELSE 0 END) "
    "FROM wa_term_inventory WHERE delete_flagged = 0"
).fetchone()
print(f"  Min: {stats[0]}  Max: {stats[1]}  Avg: {stats[2]:.1f}  Zeros: {stats[3]}")

# occurrence_count_qualifier
col_report("occurrence_count_qualifier")
for r in conn.execute(
    "SELECT occurrence_count_qualifier, COUNT(*) as c FROM wa_term_inventory "
    "WHERE delete_flagged = 0 GROUP BY occurrence_count_qualifier ORDER BY c DESC"
).fetchall():
    print(f"  {r[0] or 'NULL':<15} {r[1]:>5}")

# meaning
col_report("meaning")
avg_len = conn.execute(
    "SELECT AVG(LENGTH(meaning)) FROM wa_term_inventory WHERE delete_flagged = 0 AND meaning IS NOT NULL"
).fetchone()[0]
print(f"  Avg length: {avg_len:.0f} chars" if avg_len else "  Avg length: N/A")

# meaning_numbered
col_report("meaning_numbered")

# also_spelled
col_report("also_spelled")

# lsj_entry
col_report("lsj_entry")

# testament
col_report("testament")
for r in conn.execute(
    "SELECT testament, COUNT(*) as c FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY testament ORDER BY c DESC"
).fetchall():
    print(f"  {r[0] or 'NULL':<10} {r[1]:>5}")

# god_as_subject
col_report("god_as_subject")
for r in conn.execute(
    "SELECT god_as_subject, COUNT(*) as c FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY god_as_subject ORDER BY c DESC"
).fetchall():
    print(f"  {str(r[0]):<10} {r[1]:>5}")

# somatic_link
col_report("somatic_link")
for r in conn.execute(
    "SELECT somatic_link, COUNT(*) as c FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY somatic_link ORDER BY c DESC"
).fetchall():
    print(f"  {str(r[0]):<10} {r[1]:>5}")

# causative_form_present
col_report("causative_form_present")
for r in conn.execute(
    "SELECT causative_form_present, COUNT(*) as c FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY causative_form_present ORDER BY c DESC"
).fetchall():
    print(f"  {str(r[0]):<10} {r[1]:>5}")

# status_note
col_report("status_note")

# last_changed
col_report("last_changed")

# short_def_mounce
col_report("short_def_mounce")

# parsed_meaning_id
col_report("parsed_meaning_id")

# evidential_status
col_report("evidential_status")
for r in conn.execute(
    "SELECT evidential_status, COUNT(*) as c FROM wa_term_inventory WHERE delete_flagged = 0 "
    "GROUP BY evidential_status ORDER BY c DESC"
).fetchall():
    print(f"  {r[0] or 'NULL':<20} {r[1]:>5}")

# retention_note
col_report("retention_note")

# delete_flagged (all rows)
print(f"\ndelete_flagged (all rows):")
for r in conn.execute("SELECT delete_flagged, COUNT(*) as c FROM wa_term_inventory GROUP BY delete_flagged"):
    print(f"  {r[0]}  {r[1]:>5}")

conn.close()
