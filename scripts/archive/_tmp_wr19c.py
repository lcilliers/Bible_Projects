#!/usr/bin/env python3
"""WR-19 detail — terms with parse_warnings, file_id=36."""
import sqlite3, os

DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "bible_research.db")
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
FILE_ID = 36

rows = conn.execute(
    """SELECT ti.id AS ti_id, ti.strongs_number, ti.step_search_gloss,
              ti.occurrence_count, mp.parse_warnings, mp.top_sense_count,
              mp.stem_count, mp.has_domain_tags
       FROM wa_meaning_parsed mp
       JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id
       WHERE ti.file_id = ? AND mp.parse_warnings IS NOT NULL
       ORDER BY ti.strongs_number""",
    (FILE_ID,)
).fetchall()

print(f"WR-19: terms with parse_warnings = {len(rows)}\n")
for r in rows:
    code = r['strongs_number']
    ti_id = r['ti_id']

    # Get senses
    senses = conn.execute(
        """SELECT ms.level_code, ms.sense_text, ms.is_stem_label, ms.stem_label
           FROM wa_meaning_sense ms
           JOIN wa_meaning_parsed mp ON mp.id = ms.parsed_meaning_id
           WHERE mp.term_inv_id = ?
           ORDER BY ms.sort_order""",
        (ti_id,)
    ).fetchall()

    print(f"  {code}  '{r['step_search_gloss']}'  occur={r['occurrence_count']}"
          f"  senses={r['top_sense_count']}  stems={r['stem_count']}")
    print(f"    WARNING: {r['parse_warnings']}")
    for s in senses:
        indent = "      " if s['is_stem_label'] else "        "
        print(f"{indent}[{s['level_code']}] {(s['sense_text'] or '')[:90]}")
    print()

conn.close()
