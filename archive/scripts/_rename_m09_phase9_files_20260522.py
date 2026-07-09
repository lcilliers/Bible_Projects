"""Rename M09 Phase 9 char findings to canonical names matching DB short_names."""
from pathlib import Path
import sqlite3
conn = sqlite3.connect('database/bible_research.db')
cur = conn.cursor()
char_names = {r[0]: r[1] for r in cur.execute(
    "SELECT char_seq, short_name FROM characteristic WHERE cluster_code='M09' AND COALESCE(delete_flagged,0)=0"
).fetchall()}
print('Char names:', char_names)

FOLDER = Path('Sessions/Session_Clusters/M09/files phase 9')
for n, short in char_names.items():
    safe = short.replace(' ','-').replace('/','-')
    matches = list(FOLDER.glob(f'wa-cluster-m09-phase9-char{n}-*-findings-v1-20260522.md'))
    if not matches:
        print(f'  char{n}: no file found')
        continue
    src = matches[0]
    dst = src.with_name(f'wa-cluster-M09-phase9-char{n}-{safe}-findings-v1-20260522.md')
    if src != dst:
        src.rename(dst)
        print(f'  char{n}: {src.name} -> {dst.name}')
