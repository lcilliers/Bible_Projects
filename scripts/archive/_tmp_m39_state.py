import sqlite3, json, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

print('--- M39 cluster row ---')
r = c.execute("SELECT cluster_code, short_name, gloss, source, bucket, status, version, last_updated_date FROM cluster WHERE cluster_code='M39'").fetchone()
print(json.dumps(dict(r) if r else 'MISSING', indent=2, ensure_ascii=False))
print()

n = c.execute("SELECT COUNT(*) c FROM mti_terms WHERE cluster_code='M39'").fetchone()['c']
sg = c.execute("SELECT COUNT(*) c FROM cluster_subgroup WHERE cluster_code='M39'").fetchone()['c']
print(f'mti_terms in M39: {n}')
print(f'cluster_subgroup in M39: {sg}')
v = c.execute('''SELECT COUNT(DISTINCT vr.id) c
                 FROM wa_verse_records vr
                 JOIN wa_term_inventory wti ON wti.term_inventory_id = vr.wti_id
                 JOIN mti_terms mt ON mt.mti_term_id = wti.mti_term_id
                 WHERE mt.cluster_code='M39' ''').fetchone()['c']
print(f'verse records covered: {v}')
print()

print('--- M39 terms (top-level identity) ---')
for row in c.execute('''SELECT mti_term_id, strongs, transliteration, gloss
                        FROM mti_terms WHERE cluster_code='M39' ORDER BY strongs'''):
    print(f"  {row['strongs']} {row['transliteration'] or '':<22} {row['gloss'] or ''}")

print()
print('--- existing verse_context status counts for M39 ---')
for row in c.execute('''SELECT
        CASE WHEN vc.id IS NULL THEN 'UT'
             WHEN vc.is_relevant=1 THEN 'relevant'
             WHEN vc.set_aside_reason IS NOT NULL THEN 'set_aside'
             ELSE 'other' END as st,
        COUNT(*) c
    FROM wa_verse_records vr
    JOIN wa_term_inventory wti ON wti.term_inventory_id = vr.wti_id
    JOIN mti_terms mt ON mt.mti_term_id = wti.mti_term_id
    LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id AND vc.mti_term_id = mt.mti_term_id
    WHERE mt.cluster_code='M39'
    GROUP BY 1'''):
    print(f"  {row['st']:<12} {row['c']}")
