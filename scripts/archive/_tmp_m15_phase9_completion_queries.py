"""Pull verification data for DIR-20260512-001 completion report."""
import sqlite3, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row

print("# Status × scope distribution")
for r in conn.execute("""
    SELECT COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope,
           cf.finding_status, COUNT(*) n
      FROM cluster_finding cf
      LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
     WHERE cf.cluster_code = 'M15'
     GROUP BY scope, cf.finding_status
     ORDER BY scope, cf.finding_status
"""):
    print(f"  {r['scope']:15s} {r['finding_status']:25s} {r['n']}")

print()
print("# Total M15 rows")
total = conn.execute("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='M15'").fetchone()[0]
print(f"  {total}")

print()
print("# All gap rows")
for r in conn.execute("""
    SELECT q.question_code,
           COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope,
           SUBSTR(cf.finding_text, 1, 100) AS excerpt
      FROM cluster_finding cf
      JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
      LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
     WHERE cf.cluster_code = 'M15' AND cf.finding_status = 'gap'
     ORDER BY q.question_code, scope
"""):
    print(f"  {r['question_code']:>8s}  {r['scope']:12s}  {r['excerpt']}")

print()
print("# wa_session_b_findings for M15 terms")
n = conn.execute("""
    SELECT COUNT(*) FROM wa_session_b_findings sbf
      JOIN mti_terms mt ON mt.id = sbf.term_id
     WHERE mt.cluster_code = 'M15'
""").fetchone()[0]
print(f"  {n}")

print()
print("# 3 sample rows")
for status in ('finding', 'silent', 'cluster_synthesis'):
    r = conn.execute("""
        SELECT q.question_code,
               COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope,
               cf.finding_status,
               SUBSTR(cf.finding_text, 1, 100) AS excerpt
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
          LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
         WHERE cf.cluster_code = 'M15' AND cf.finding_status = ?
         LIMIT 1
    """, (status,)).fetchone()
    if r:
        print(f"\n  -- {status} --")
        print(f"  qcode: {r['question_code']}")
        print(f"  scope: {r['scope']}")
        print(f"  text:  {r['excerpt']}")

print()
print("# FLAG-M15-006 final state")
for r in conn.execute("""
    SELECT vc.verse_record_id AS vr_id, vr.reference,
           cs.subgroup_code, vcg.group_code, vc.is_relevant
      FROM verse_context vc
      JOIN mti_terms mt ON mt.id = vc.mti_term_id
      LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
      LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
      LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
     WHERE vc.verse_record_id IN (54610, 54611, 54612, 54613, 54626)
       AND mt.strongs_number = 'H2803G'
       AND COALESCE(vc.delete_flagged,0) = 0
     ORDER BY vr.id
"""):
    print(f"  [{r['vr_id']}] {r['reference']:>12s}  sg={r['subgroup_code']}  "
          f"grp={r['group_code']}  rel={r['is_relevant']}")
conn.close()
