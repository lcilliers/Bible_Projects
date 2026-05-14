"""Snapshot the materials M15 has available for Session C cluster-publish.
Goal: confirm what the design can build on, in actual numbers and shape."""
import sqlite3, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass
conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row

print("=== M15 cluster row ===")
r = conn.execute("""
    SELECT cluster_code, short_name, description, LENGTH(gloss) AS gloss_len,
           status, version
      FROM cluster WHERE cluster_code='M15'
""").fetchone()
print(f"  short_name : {r['short_name']}")
print(f"  description: {r['description']}")
print(f"  gloss_len  : {r['gloss_len']} chars (full term-gloss list)")
print(f"  status     : {r['status']}")
print()

print("=== M15 sub-groups ===")
for r in conn.execute("""
    SELECT cs.subgroup_code, cs.label, LENGTH(cs.core_description) AS d_len,
           (SELECT COUNT(*) FROM mti_term_subgroup mts
             WHERE mts.cluster_subgroup_id=cs.id
               AND COALESCE(mts.delete_flagged,0)=0) AS terms,
           (SELECT COUNT(*) FROM verse_context vc
             WHERE vc.cluster_subgroup_id=cs.id
               AND COALESCE(vc.delete_flagged,0)=0) AS vcs
      FROM cluster_subgroup cs
     WHERE cs.cluster_code='M15' AND COALESCE(cs.delete_flagged,0)=0
     ORDER BY cs.subgroup_code
"""):
    print(f"  {r['subgroup_code']:14s} terms={r['terms']:>3d} vcs={r['vcs']:>4d}  {r['label'][:50]} (desc {r['d_len']} chars)")

print()
print("=== M15 VCGs (active, new M15-X-VCG…) ===")
n = conn.execute("""
    SELECT COUNT(*) FROM verse_context_group
     WHERE group_code LIKE 'M15-%-VCG%' AND COALESCE(delete_flagged,0)=0
""").fetchone()[0]
print(f"  total: {n}")

print()
print("=== M15 cluster_finding distribution ===")
for r in conn.execute("""
    SELECT finding_status, COUNT(*) n,
           AVG(LENGTH(finding_text)) avg_len
      FROM cluster_finding
     WHERE cluster_code='M15' GROUP BY finding_status
"""):
    print(f"  {r['finding_status']:25s} n={r['n']:>4d}  avg_text_len={int(r['avg_len'] or 0):>5d} chars")

# Catalogue tier coverage
print()
print("=== Catalogue tiers covered in M15 findings ===")
for r in conn.execute("""
    SELECT SUBSTR(q.question_code,1,2) AS tier, COUNT(DISTINCT q.question_code) AS prompts,
           COUNT(*) AS findings
      FROM cluster_finding cf
      JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
     WHERE cf.cluster_code='M15'
     GROUP BY tier ORDER BY tier
"""):
    print(f"  tier {r['tier']}: {r['prompts']:>3d} distinct prompts, {r['findings']:>4d} findings")

# Anchor verses sample
print()
print("=== M15 anchor verses sample (top 3) ===")
for r in conn.execute("""
    SELECT vcg.group_code, vr.reference, mt.strongs_number, mt.transliteration,
           SUBSTR(vr.verse_text, 1, 80) AS vtxt
      FROM verse_context vc
      JOIN verse_context_group vcg ON vcg.id=vc.group_id
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
      JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
     WHERE vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
       AND vcg.group_code LIKE 'M15-%-VCG%'
       AND mt.cluster_code='M15'
     LIMIT 3
"""):
    print(f"  {r['group_code']:14s} {r['reference']:>12s}  {r['strongs_number']} {r['transliteration']}")
    print(f"    {r['vtxt']}…")

# Sample finding text length distribution
print()
print("=== M15 finding_text length distribution ===")
for label, op in [("<200", "LENGTH(finding_text) < 200"),
                  ("200-500", "LENGTH(finding_text) BETWEEN 200 AND 499"),
                  ("500-1000", "LENGTH(finding_text) BETWEEN 500 AND 999"),
                  ("≥1000", "LENGTH(finding_text) >= 1000")]:
    n = conn.execute(f"""
        SELECT COUNT(*) FROM cluster_finding
         WHERE cluster_code='M15' AND {op}
    """).fetchone()[0]
    print(f"  {label:>8s} chars: {n}")
conn.close()
