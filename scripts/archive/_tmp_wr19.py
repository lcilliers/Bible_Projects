#!/usr/bin/env python3
"""Show WR-19 detail: terms with parse_warnings in wa_meaning_parsed, for soul file_id=36."""
import sqlite3, os

DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "bible_research.db")
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
FILE_ID = 36

rows = conn.execute(
    """SELECT ti.strongs_number, ti.term_id, ti.step_search_gloss, ti.occurrence_count,
              mp.parse_warnings, mp.parsed_sense_count, mp.raw_meaning_text
       FROM wa_meaning_parsed mp
       JOIN wa_term_inventory ti ON ti.id = mp.term_inv_id
       WHERE ti.file_id = ? AND mp.parse_warnings IS NOT NULL
       ORDER BY ti.strongs_number""",
    (FILE_ID,)
).fetchall()

print(f"WR-19 terms with parse_warnings: {len(rows)}\n")
for r in rows:
    code = r['strongs_number'] or r['term_id']
    # check if NOTE flag exists
    note = conn.execute(
        """SELECT 1 FROM wa_data_quality_flags dqf
           JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
           WHERE dqf.file_id=? AND dqf.term_id=? AND qt.flag_code='NOTE'""",
        (FILE_ID, code)
    ).fetchone()
    print(f"{'='*60}")
    print(f"Code          : {code}")
    print(f"Gloss         : {r['step_search_gloss']}")
    print(f"Occurrences   : {r['occurrence_count']}")
    print(f"Senses parsed : {r['parsed_sense_count']}")
    print(f"NOTE flag     : {'YES' if note else 'NO — this is why WR-19 fires'}")
    print(f"parse_warnings: {r['parse_warnings']}")
    print(f"raw_meaning   : {(r['raw_meaning_text'] or '')[:200]}")
    print()

conn.close()
