import sqlite3, json

conn = sqlite3.connect("data/bible_research.db")
conn.row_factory = sqlite3.Row

ti = conn.execute(
    "SELECT * FROM wa_term_inventory WHERE strongs_number = 'H2734'"
).fetchone()
print("=== wa_term_inventory ===")
print(json.dumps(dict(ti), indent=2, default=str))

flags = conn.execute("""
    SELECT ft.flag_group, ft.flag_code, f.description
    FROM wa_data_quality_flags f
    JOIN wa_quality_flag_types ft ON ft.id = f.flag_id
    WHERE f.term_id = 'H2734'
""").fetchall()
print("\n=== wa_data_quality_flags ===")
for r in flags:
    print(json.dumps(dict(r), indent=2, default=str))

vcount = conn.execute("""
    SELECT COUNT(*) AS c FROM wa_verse_records
    WHERE term_inv_id = (SELECT id FROM wa_term_inventory WHERE strongs_number='H2734')
""").fetchone()
print(f"\n=== wa_verse_records count: {vcount['c']} ===")

mp = conn.execute("""
    SELECT * FROM wa_meaning_parsed
    WHERE term_inv_id = (SELECT id FROM wa_term_inventory WHERE strongs_number='H2734')
""").fetchone()
print("\n=== wa_meaning_parsed ===")
print(json.dumps(dict(mp), indent=2, default=str) if mp else "None")

rf = conn.execute("""
    SELECT * FROM wa_term_root_family
    WHERE term_inv_id = (SELECT id FROM wa_term_inventory WHERE strongs_number='H2734')
""").fetchall()
print("\n=== wa_term_root_family ===")
for r in rf:
    print(json.dumps(dict(r), indent=2, default=str))

rw = conn.execute("""
    SELECT * FROM wa_term_related_words
    WHERE term_inv_id = (SELECT id FROM wa_term_inventory WHERE strongs_number='H2734')
""").fetchall()
print("\n=== wa_term_related_words ===")
for r in rw:
    print(json.dumps(dict(r), indent=2, default=str))

mti = conn.execute(
    "SELECT * FROM mti_terms WHERE strongs_number = 'H2734'"
).fetchone()
print("\n=== mti_terms ===")
print(json.dumps(dict(mti), indent=2, default=str) if mti else "None")

conn.close()
