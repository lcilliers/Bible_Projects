"""Temporary introspection script — outputs JSON for report generation."""
import sqlite3
import json

db = "data/bible_research.db"
conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row

# 1. Tables + row counts
tables = [r[0] for r in conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
).fetchall()]

print("=== TABLES ===")
for t in tables:
    cnt = conn.execute(f"SELECT COUNT(*) FROM [{t}]").fetchone()[0]
    print(f"  {t}: {cnt}")

# 2. Foreign keys
print("\n=== FOREIGN KEYS ===")
for t in tables:
    fks = conn.execute(f"PRAGMA foreign_key_list([{t}])").fetchall()
    for fk in fks:
        print(f"  FK|{t}|{fk['from']}|{fk['table']}|{fk['to']}|{fk['on_update']}|{fk['on_delete']}")

# 3. Indexes
print("\n=== INDEXES ===")
idxs = conn.execute(
    "SELECT name, tbl_name, sql FROM sqlite_master WHERE type='index' ORDER BY tbl_name, name"
).fetchall()
for idx in idxs:
    print(f"  IDX|{idx['tbl_name']}|{idx['name']}")

# 4. Schema version
print("\n=== SCHEMA VERSION ===")
try:
    sv = conn.execute("SELECT * FROM schema_version WHERE id=1").fetchone()
    if sv:
        print(f"  version_code={sv['version_code']}")
        print(f"  applied_at={sv['applied_at']}")
        hist = json.loads(sv['migration_history'] or '[]')
        print(f"  migrations_applied={','.join(hist)}")
except Exception as e:
    print(f"  ERROR: {e}")

# 5. FK integrity check
print("\n=== FK INTEGRITY (foreign_key_check) ===")
try:
    violations = conn.execute("PRAGMA foreign_key_check").fetchall()
    if not violations:
        print("  PASS: no violations")
    else:
        for v in violations:
            print(f"  VIOLATION|{v[0]}|rowid={v[1]}|ref_table={v[2]}|fk_id={v[3]}")
except Exception as e:
    print(f"  ERROR: {e}")

# 6. Check soft-link columns (TEXT FK-like columns that have no formal FK)
print("\n=== SOFT LINK CHECK ===")

soft_checks = [
    # (table, column, ref_table, ref_col, label)
    ("wa_file_index",          "registry_id",      "word_registry", "id",   "wa_file_index.registry_id -> word_registry.id (TEXT, no FK)"),
    ("mti_terms",              "owning_registry",  "word_registry", "id",   "mti_terms.owning_registry -> word_registry.id (TEXT, no FK)"),
    ("mti_term_cross_refs",    "registry",         "word_registry", "id",   "mti_term_cross_refs.registry -> word_registry.id (TEXT, no FK)"),
    ("word_run_state",         "registry_id",      "word_registry", "id",   "word_run_state.registry_id -> word_registry.id (TEXT, no FK)"),
    ("term_fetch_log",         "registry_id",      "word_registry", "id",   "term_fetch_log.registry_id -> word_registry.id (TEXT, no FK)"),
    ("wa_term_inventory",      "parsed_meaning_id","wa_meaning_parsed","id", "wa_term_inventory.parsed_meaning_id -> wa_meaning_parsed.id (no FK constraint)"),
    ("wa_verse_records",       "term_id",          "wa_term_inventory","term_id","wa_verse_records.term_id ~ wa_term_inventory.term_id (TEXT match, no FK)"),
    ("wa_data_quality_flags",  "term_id",          "wa_term_inventory","term_id","wa_data_quality_flags.term_id ~ wa_term_inventory.term_id (TEXT match, no FK)"),
    ("mti_terms",              "word_data_reference","wa_file_index","id",   "mti_terms.word_data_reference -> wa_file_index.id (TEXT, future FK)"),
    ("mti_term_cross_refs",    "word_data_reference","wa_file_index","id",   "mti_term_cross_refs.word_data_reference -> wa_file_index.id (TEXT, future FK)"),
    ("word_registry",          "automation_run_id","engine_run_log","run_id","word_registry.automation_run_id -> engine_run_log.run_id (TEXT, no FK)"),
]

for tbl, col, ref_tbl, ref_col, label in soft_checks:
    try:
        # Count rows where col is not null
        total = conn.execute(f"SELECT COUNT(*) FROM [{tbl}] WHERE [{col}] IS NOT NULL").fetchone()[0]
        # Count orphans (cast to TEXT for comparison)
        orphan = conn.execute(
            f"SELECT COUNT(*) FROM [{tbl}] t "
            f"WHERE t.[{col}] IS NOT NULL "
            f"AND CAST(t.[{col}] AS TEXT) NOT IN (SELECT CAST([{ref_col}] AS TEXT) FROM [{ref_tbl}])"
        ).fetchone()[0]
        pct = f"{(orphan/total*100):.1f}%" if total > 0 else "N/A"
        print(f"  SOFT|{label}|non_null={total}|orphans={orphan}|orphan_rate={pct}")
    except Exception as e:
        print(f"  SOFT_ERR|{label}|{e}")

# 7. Column inventory for all tables
print("\n=== COLUMN INVENTORY ===")
for t in tables:
    cols = conn.execute(f"PRAGMA table_info([{t}])").fetchall()
    col_desc = "; ".join(f"{c['name']}({c['type']})" for c in cols)
    print(f"  TABLE|{t}|{col_desc}")

conn.close()
print("\nDONE")
