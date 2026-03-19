"""Inspect all relevant table schemas."""
from analytics.db_client import get_connection

conn = get_connection()
tables = [
    'word_registry', 'mti_terms', 'mti_term_flags', 'mti_term_cross_refs',
    'phase2_flag_types',
    'wa_term_inventory', 'wa_file_index', 'wa_term_related_words', 'wa_term_root_family',
    'wa_term_phase2_flags', 'wa_cross_registry_links', 'wa_crosslink_type', 'wa_data_quality_flags',
    'wa_quality_flag_types', 'wa_verse_records'
]
for t in tables:
    print(f"\n=== {t} ===")
    cols = conn.execute(f"PRAGMA table_info({t})").fetchall()
    for c in cols:
        print(f"  {c[1]:35s} {c[2]}")
    count = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"  --> {count} rows")
conn.close()
