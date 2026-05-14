"""Pre-flight for M15 findings load (DIR-20260512-001) + FLAG-M15-006."""
import sqlite3, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass
conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row

print("=== Schema ===")
tabs = [r["name"] for r in conn.execute("""
    SELECT name FROM sqlite_master WHERE type='table'
       AND name IN ('cluster_finding','cluster_subgroup','mti_terms',
                    'wa_obs_question_catalogue','wa_session_b_findings',
                    'cluster','verse_context','verse_context_group')
""")]
print(f"  required tables present: {tabs}")

print()
print("=== Existing cluster_finding rows ===")
n_all = conn.execute("SELECT COUNT(*) FROM cluster_finding").fetchone()[0]
print(f"  total all clusters: {n_all}")
for r in conn.execute("""
    SELECT cluster_code, COUNT(*) n FROM cluster_finding
     GROUP BY cluster_code ORDER BY cluster_code
"""):
    print(f"  {r['cluster_code']:6s} {r['n']}")

print()
print("=== Catalogue ===")
for r in conn.execute("""
    SELECT DISTINCT catalogue_version FROM wa_obs_question_catalogue
     WHERE question_code GLOB 'T[0-9]*'
"""):
    print(f"  T-code catalogue_version: {r[0]}")
n_t = conn.execute("""
    SELECT COUNT(*) FROM wa_obs_question_catalogue
     WHERE question_code GLOB 'T[0-9]*'
""").fetchone()[0]
print(f"  T-code prompts: {n_t}")

print()
print("=== M15 sub-groups (active) ===")
for r in conn.execute("""
    SELECT id, subgroup_code, label FROM cluster_subgroup
     WHERE cluster_code='M15' AND COALESCE(delete_flagged,0)=0
     ORDER BY subgroup_code
"""):
    print(f"  id={r['id']:>4d} {r['subgroup_code']:18s} {r['label']}")

print()
print("=== FLAG-M15-006 — 5 stray cha.shav verses current state ===")
for r in conn.execute("""
    SELECT vc.id AS vc_id, vc.verse_record_id AS vr_id, vr.reference,
           cs.subgroup_code, vc.group_id, vc.is_relevant, vc.set_aside_reason,
           mt.strongs_number, mt.transliteration
      FROM verse_context vc
      JOIN mti_terms mt ON mt.id = vc.mti_term_id
      LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
      LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
     WHERE vc.verse_record_id IN (54610, 54611, 54612, 54613, 54626)
       AND mt.strongs_number = 'H2803G'
       AND COALESCE(vc.delete_flagged,0) = 0
     ORDER BY vr.id
"""):
    print(f"  [{r['vr_id']}] {r['reference']:>15s} "
          f"sg={r['subgroup_code']} grp={r['group_id']} "
          f"rel={r['is_relevant']} sa={r['set_aside_reason']}")

# Find M15-E-VCG05 id
r = conn.execute("""
    SELECT id, context_description FROM verse_context_group
     WHERE group_code = 'M15-E-VCG05' AND COALESCE(delete_flagged,0)=0
""").fetchone()
if r:
    print(f"\nM15-E-VCG05: id={r['id']}")
    print(f"  description: {r['context_description'][:140]}")
else:
    print("\n[ERR] M15-E-VCG05 not found")

# M15 cluster status
print()
print("=== M15 cluster.status ===")
r = conn.execute("SELECT status, version, last_updated_date FROM cluster WHERE cluster_code='M15'").fetchone()
print(f"  status={r['status']!r}  version={r['version']}  last_updated={r['last_updated_date']}")

# wa_session_b_findings baseline for M15 terms
print()
print("=== wa_session_b_findings baseline (M15 terms) ===")
n = conn.execute("""
    SELECT COUNT(*) FROM wa_session_b_findings sbf
      JOIN mti_terms mt ON mt.id = sbf.term_id
     WHERE mt.cluster_code = 'M15'
""").fetchone()[0]
print(f"  rows: {n}")
conn.close()
