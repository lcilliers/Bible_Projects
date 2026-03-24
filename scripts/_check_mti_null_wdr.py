"""Investigate Issue 2: mti_terms rows with NULL word_data_reference."""
import sqlite3, json

DB = r"G:\My Drive\Bible_study_projects\data\bible_research.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print("=" * 70)
print("ISSUE 2 — NULL word_data_reference in mti_terms")
print("=" * 70)

# Overview: which words/registries have NULL wdr?
cur.execute("""
    SELECT owning_registry, owning_word, owning_part,
           COUNT(*) AS cnt, status
    FROM mti_terms
    WHERE word_data_reference IS NULL
    GROUP BY owning_registry, owning_word, owning_part, status
    ORDER BY CAST(owning_registry AS INTEGER), owning_part
""")
rows = cur.fetchall()
print(f"\nTotal groups with NULL wdr: {len(rows)}")
print(f"{'Registry':<10} {'Word':<20} {'Part':<8} {'Count':<7} Status")
print("-" * 60)
for r in rows:
    print(f"{str(r['owning_registry']):<10} {str(r['owning_word']):<20} {str(r['owning_part']):<8} {r['cnt']:<7} {r['status']}")

# For each owning_registry, check if wa_file_index has matching entries
print("\n\nCross-check: wa_file_index entries for affected registries")
print("-" * 60)
cur.execute("""
    SELECT DISTINCT owning_registry, owning_word
    FROM mti_terms WHERE word_data_reference IS NULL
    ORDER BY CAST(owning_registry AS INTEGER)
""")
registries = cur.fetchall()
for reg in registries:
    rid = reg['owning_registry']
    word = reg['owning_word']
    cur.execute("""
        SELECT id, word, part_number, total_parts, is_split
        FROM wa_file_index WHERE word_registry_fk = ?
        ORDER BY part_number
    """, (rid,))
    fi_rows = cur.fetchall()
    if fi_rows:
        fi_info = ", ".join(f"id={r['id']} part={r['part_number']}" for r in fi_rows)
        print(f"  reg {rid:>4} ({word}): fi entries → {fi_info}")
    else:
        print(f"  reg {rid:>4} ({word}): NO wa_file_index entry")

# Sample some of the NULL rows for detail
print("\n\nSample NULL wdr rows (first 10):")
print("-" * 60)
cur.execute("""
    SELECT id, strongs_number, transliteration, gloss, owning_registry,
           owning_word, owning_part, status, extraction_date
    FROM mti_terms
    WHERE word_data_reference IS NULL
    ORDER BY CAST(owning_registry AS INTEGER), id
    LIMIT 10
""")
for r in cur.fetchall():
    print(f"  id={r['id']} strongs={r['strongs_number']} trans={r['transliteration']} "
          f"reg={r['owning_registry']} word={r['owning_word']} part={r['owning_part']} "
          f"status={r['status']} date={r['extraction_date']}")

conn.close()
