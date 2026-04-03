"""Temporary script to apply data fixes 2-5 on mti_terms and wa_term_inventory."""
import sqlite3
import time

# Retry loop for Google Drive sync lock contention
for attempt in range(10):
    try:
        conn = sqlite3.connect('data/bible_research.db', timeout=120)
        conn.execute("PRAGMA busy_timeout = 120000")
        conn.execute("SELECT 1")
        conn.execute("UPDATE mti_terms SET last_changed = last_changed WHERE id = 1")
        conn.commit()
        print(f"DB write lock acquired (attempt {attempt + 1})")
        break
    except sqlite3.OperationalError as e:
        print(f"Attempt {attempt + 1}: {e} — retrying in 10s...")
        try:
            conn.close()
        except:
            pass
        time.sleep(10)
else:
    print("FAILED: Could not acquire DB lock after 10 attempts")
    raise SystemExit(1)

# FIX 2: status = 'extracted' for NULL-status terms with active verses
mti_with_verses = set(r[0] for r in conn.execute(
    "SELECT DISTINCT mti_term_id FROM wa_verse_records "
    "WHERE delete_flagged = 0 AND mti_term_id IS NOT NULL"
).fetchall())

null_ids = [r[0] for r in conn.execute(
    "SELECT id FROM mti_terms WHERE delete_flagged = 0 AND status IS NULL"
).fetchall()]

to_extract = [i for i in null_ids if i in mti_with_verses]
for i in range(0, len(to_extract), 500):
    chunk = to_extract[i:i+500]
    placeholders = ','.join(str(x) for x in chunk)
    conn.execute(f"UPDATE mti_terms SET status = 'extracted' WHERE id IN ({placeholders})")
conn.commit()
print(f"Fix 2: {len(to_extract)} status set to 'extracted' — committed")

remaining = conn.execute(
    "SELECT COUNT(*) FROM mti_terms WHERE delete_flagged = 0 AND status IS NULL"
).fetchone()[0]
print(f"  Remaining NULL status: {remaining}")

# FIX 3: owning_word NULL -> gloss
rows = conn.execute(
    "SELECT id, gloss FROM mti_terms WHERE delete_flagged = 0 AND owning_word IS NULL"
).fetchall()
for r in rows:
    conn.execute("UPDATE mti_terms SET owning_word = ? WHERE id = ?", (r[1], r[0]))
conn.commit()
print(f"Fix 3: {len(rows)} owning_word fixed — committed")

# FIX 4: extraction_date NULL -> 2026-03-28
conn.execute(
    "UPDATE mti_terms SET extraction_date = '2026-03-28' "
    "WHERE delete_flagged = 0 AND extraction_date IS NULL"
)
n = conn.execute("SELECT changes()").fetchone()[0]
conn.commit()
print(f"Fix 4: {n} extraction_date set to 2026-03-28 — committed")

# FIX 5: word_analysis_gloss NULL -> step_search_gloss
conn.execute(
    "UPDATE wa_term_inventory SET word_analysis_gloss = step_search_gloss "
    "WHERE delete_flagged = 0 AND word_analysis_gloss IS NULL "
    "AND step_search_gloss IS NOT NULL"
)
n = conn.execute("SELECT changes()").fetchone()[0]
conn.commit()
print(f"Fix 5: {n} word_analysis_gloss set from step_search_gloss — committed")

# BONUS: occurrence_count NULL
oc = conn.execute(
    "SELECT id FROM wa_term_inventory WHERE delete_flagged = 0 AND occurrence_count IS NULL"
).fetchall()
for r in oc:
    vc = conn.execute(
        "SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id = ? AND delete_flagged = 0",
        (r[0],)
    ).fetchone()[0]
    conn.execute("UPDATE wa_term_inventory SET occurrence_count = ? WHERE id = ?", (vc, r[0]))
conn.commit()
print(f"Fix occurrence_count: {len(oc)} fixed — committed")

print("\nAll fixes complete.")
conn.close()
