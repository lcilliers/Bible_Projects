"""Dump schema for cluster-process tables to embed in instruction appendix."""
import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

TABLES = ["cluster", "cluster_subgroup", "mti_term_subgroup",
          "verse_context_group", "vcg_term", "verse_context", "cluster_finding"]

for t in TABLES:
    cols = list(c.execute(f"PRAGMA table_info({t})"))
    if not cols:
        print(f"\n## {t} — NOT FOUND")
        continue
    print(f"\n## {t}")
    for r in cols:
        flags = []
        if r['pk']: flags.append('PK')
        if r['notnull']: flags.append('NOT NULL')
        flagstr = f" [{', '.join(flags)}]" if flags else ""
        print(f"  {r['name']} {r['type']}{flagstr}")
