import sqlite3, json, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

r = c.execute("""SELECT cluster_code, short_name, gloss, status, version, last_updated_date
                 FROM cluster WHERE cluster_code='M46'""").fetchone()
print('=== M46 cluster row ===')
print(json.dumps(dict(r) if r else 'MISSING', indent=2, ensure_ascii=False))
print()

n = c.execute("""SELECT COUNT(*) c FROM mti_terms
                 WHERE cluster_code='M46' AND COALESCE(delete_flagged,0)=0""").fetchone()['c']
sg = c.execute("""SELECT COUNT(*) c FROM cluster_subgroup
                  WHERE cluster_code='M46' AND COALESCE(delete_flagged,0)=0""").fetchone()['c']
print(f'active mti_terms: {n}')
print(f'cluster_subgroup rows: {sg}')
print()

# vc state already-classified counts (informational)
print('=== M46 verse_context state ===')
for row in c.execute("""
    SELECT
      CASE WHEN vc.id IS NULL THEN 'UT (no vc row)'
           WHEN vc.is_relevant=1 THEN 'relevant'
           WHEN vc.set_aside_reason IS NOT NULL THEN 'set_aside'
           ELSE 'other' END AS state,
      COUNT(*) c
    FROM wa_verse_records vr
    JOIN mti_terms mt ON mt.id = vr.mti_term_id
    LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id AND vc.mti_term_id = mt.id
    WHERE mt.cluster_code='M46' AND COALESCE(mt.delete_flagged,0)=0
      AND COALESCE(vr.delete_flagged,0)=0
    GROUP BY 1
"""):
    print(f"  {row['state']:<22} {row['c']}")
