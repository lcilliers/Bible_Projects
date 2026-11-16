"""verse_lexical_surface_index_2509_v8_20261115.py -- an expression index for the lookup of verse_lexical by surface (escalation #2509).

Every lookup `lower(trim(surface)) = ?` on verse_lexical (1.5 million rows) read the whole table (about 3 s each); the grouping asked about 600 times and took over four minutes.
The index covers the same expression, with deleted and strong, so the lookup is a search (under a millisecond). It is a plain CREATE INDEX: no cfg_* write, and cfg_index holds
columns only, so it cannot name an expression (recorded on #2509). Idempotent.

Usage: python iba/app/migration/verse_lexical_surface_index_2509_v8_20261115.py [--db PATH]
"""
import argparse
import sqlite3

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"
NAME = "idx_verse_lexical_surface_lc"

ap = argparse.ArgumentParser()
ap.add_argument("--db", default=DEFAULT_DB)
a = ap.parse_args()
conn = sqlite3.connect(a.db)
if conn.execute("SELECT 1 FROM sqlite_master WHERE type='index' AND name=?", (NAME,)).fetchone():
    print("already applied")
else:
    with conn:
        conn.execute(f'CREATE INDEX "{NAME}" ON verse_lexical (lower(trim(surface)), deleted, strong)')
    print("index created")
