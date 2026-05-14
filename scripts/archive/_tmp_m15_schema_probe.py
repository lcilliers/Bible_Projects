"""Second probe: placement_note distribution, analysis_note on anchors, cluster-synthesis structure."""
import sqlite3, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass
conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row

print("--- mti_term_subgroup.placement_note distribution (M15) ---")
for r in conn.execute("""
    SELECT COALESCE(mts.placement_note,'(null)') AS pn, COUNT(*) n
      FROM mti_term_subgroup mts
      JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
     WHERE cs.cluster_code='M15' AND COALESCE(mts.delete_flagged,0)=0
     GROUP BY pn ORDER BY n DESC LIMIT 20
"""):
    print(f"  n={r['n']:>3d}  {r['pn'][:90]}")

print("\n--- mti_term_subgroup counts by sub-group (M15) ---")
for r in conn.execute("""
    SELECT cs.subgroup_code,
           COUNT(*) AS total,
           SUM(CASE WHEN mts.placement_note IS NULL OR mts.placement_note='' THEN 1 ELSE 0 END) AS no_note,
           SUM(CASE WHEN LOWER(mts.placement_note) LIKE '%support%' THEN 1 ELSE 0 END) AS supportive
      FROM mti_term_subgroup mts
      JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id
     WHERE cs.cluster_code='M15' AND COALESCE(mts.delete_flagged,0)=0
     GROUP BY cs.subgroup_code ORDER BY cs.subgroup_code
"""):
    print(f"  {r['subgroup_code']:14s} total={r['total']:>3d}  no_note={r['no_note']:>3d}  supportive_note={r['supportive']:>3d}")

print("\n--- verse_context.analysis_note presence on M15 anchors ---")
for r in conn.execute("""
    SELECT COUNT(*) AS n_anchors,
           SUM(CASE WHEN vc.analysis_note IS NOT NULL AND vc.analysis_note != '' THEN 1 ELSE 0 END) AS with_note,
           SUM(CASE WHEN vc.notes IS NOT NULL AND vc.notes != '' THEN 1 ELSE 0 END) AS with_notes_field
      FROM verse_context vc
      JOIN verse_context_group vcg ON vcg.id=vc.group_id
     WHERE vcg.group_code LIKE 'M15-%-VCG%' AND vc.is_anchor=1
       AND COALESCE(vc.delete_flagged,0)=0
"""):
    print(f"  anchors={r['n_anchors']}  with_analysis_note={r['with_note']}  with_notes={r['with_notes_field']}")

print("\n--- sample anchor verse_context with notes ---")
for r in conn.execute("""
    SELECT vc.id, vc.notes, vc.analysis_note, vr.reference, mt.transliteration
      FROM verse_context vc
      JOIN verse_context_group vcg ON vcg.id=vc.group_id
      JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
      JOIN mti_terms mt ON mt.id=vc.mti_term_id
     WHERE vcg.group_code LIKE 'M15-%-VCG%' AND vc.is_anchor=1
       AND COALESCE(vc.delete_flagged,0)=0
     LIMIT 5
"""):
    print(f"  vc_id={r['id']:>5d}  {r['reference']:>12s}  {r['transliteration'][:20]}")
    if r['notes']: print(f"    notes: {r['notes'][:150]}")
    if r['analysis_note']: print(f"    analysis_note: {r['analysis_note'][:150]}")

print("\n--- VCG context_description samples for M15 ---")
for r in conn.execute("""
    SELECT vcg.group_code, vcg.context_description
      FROM verse_context_group vcg
     WHERE vcg.group_code LIKE 'M15-%-VCG%'
       AND COALESCE(vcg.delete_flagged,0)=0
     LIMIT 5
"""):
    cd = (r['context_description'] or '')[:200]
    print(f"  {r['group_code']:14s} {cd}")

print("\n--- M15 cluster-synthesis findings sample ---")
for r in conn.execute("""
    SELECT cf.id, cf.cluster_subgroup_id, cf.obs_id,
           q.question_code, q.tier, q.section,
           SUBSTR(cf.finding_text,1,250) AS ftxt
      FROM cluster_finding cf
      JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
     WHERE cf.cluster_code='M15' AND cf.finding_status='cluster_synthesis'
     ORDER BY q.question_code LIMIT 5
"""):
    sg_id = r['cluster_subgroup_id']
    print(f"  cf={r['id']:>5d} sg_id={sg_id} q={r['question_code']:>10s} ({r['tier']})")
    print(f"    section: {r['section']}")
    print(f"    {r['ftxt']}…")

print("\n--- M15 VCGs per sub-group ---")
for r in conn.execute("""
    SELECT cs.subgroup_code, COUNT(DISTINCT vcg.id) AS n_vcgs,
           COUNT(DISTINCT CASE WHEN vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0 THEN vcg.id END) AS n_vcgs_with_anchor,
           SUM(CASE WHEN vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0 THEN 1 ELSE 0 END) AS n_anchors
      FROM cluster_subgroup cs
      LEFT JOIN verse_context vc ON vc.cluster_subgroup_id=cs.id AND COALESCE(vc.delete_flagged,0)=0
      LEFT JOIN verse_context_group vcg ON vcg.id=vc.group_id AND COALESCE(vcg.delete_flagged,0)=0
                AND vcg.group_code LIKE 'M15-%-VCG%'
     WHERE cs.cluster_code='M15' AND COALESCE(cs.delete_flagged,0)=0
     GROUP BY cs.subgroup_code ORDER BY cs.subgroup_code
"""):
    print(f"  {r['subgroup_code']:14s}  vcgs_total={r['n_vcgs']:>3d}  vcgs_with_anchor={r['n_vcgs_with_anchor']:>3d}  anchors={r['n_anchors']:>3d}")

print("\n--- M15 cluster-synthesis vs subgroup-level counts ---")
for r in conn.execute("""
    SELECT cf.finding_status,
           CASE WHEN cf.cluster_subgroup_id IS NULL THEN 'NULL_sg' ELSE 'has_sg' END AS sg_state,
           COUNT(*) AS n
      FROM cluster_finding cf
     WHERE cf.cluster_code='M15'
     GROUP BY cf.finding_status, sg_state
"""):
    print(f"  {r['finding_status']:25s} {r['sg_state']:8s} n={r['n']}")

conn.close()
