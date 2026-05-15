import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

print('=== BOUNDARY rows across all clusters ===')
rows = list(c.execute("""SELECT cluster_code, subgroup_code, label, status, core_description
                         FROM cluster_subgroup
                         WHERE subgroup_code LIKE '%BOUNDARY%'
                            OR label LIKE '%BOUNDARY%'
                            OR status = 'boundary'
                         ORDER BY cluster_code"""))
print(f'count: {len(rows)}')
for r in rows:
    print(f'  {dict(r)}')
print()
print('=== mti_term_subgroup columns ===')
for r in c.execute('PRAGMA table_info(mti_term_subgroup)'):
    print(f"  {r['name']} {r['type']}")
print()
print('=== M20 cluster_subgroup rows (reference) ===')
for r in c.execute("""SELECT subgroup_code, label, status, version
                      FROM cluster_subgroup WHERE cluster_code='M20'
                      ORDER BY sort_order"""):
    print(f"  {r['subgroup_code']:<14} status={r['status']:<10} version={r['version'] or '':<5} label={r['label']}")
print()
print('=== distinct status values used in cluster_subgroup ===')
for r in c.execute("SELECT DISTINCT status, COUNT(*) c FROM cluster_subgroup GROUP BY status"):
    print(f"  status={r['status']!r:<14} count={r['c']}")
