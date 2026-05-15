"""Pre-flight checks for M39 dir-005 verification-corrections."""
import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row


def divider(s):
    print(f"\n{'=' * 72}\n  {s}\n{'=' * 72}")


# Q1 — confirm catalogue column name + resolve obs_ids
divider("Catalogue: column name + obs_id resolution for prompts cited in dir-005")
print("  schema column is 'question_code' (not 'prompt_code') — confirmed earlier")
print()
needed = ['T1.2.1', 'T5.7.2', 'T6.7.1', 'T6.7.3',
          'T0.4.1', 'T2.3.1', 'T2.6.1', 'T3.9.1', 'T4.2.1', 'T6.3.1']
for q in needed:
    r = c.execute("""SELECT obs_id, question_code, catalogue_version
                     FROM wa_obs_question_catalogue
                     WHERE question_code=? AND COALESCE(deleted,0)=0""", (q,)).fetchone()
    if r:
        print(f"  {q:<10} obs_id={r['obs_id']:<4} v={r['catalogue_version']}")
    else:
        print(f"  {q:<10} NOT FOUND")


# Q2 — cluster_finding constraints (unique on what?)
divider("cluster_finding indexes / unique constraints")
for r in c.execute("PRAGMA index_list(cluster_finding)"):
    print(f"  index: {r['name']} unique={r['unique']}")
    for col in c.execute(f"PRAGMA index_info({r['name']})"):
        print(f"    col: {col['name']}")


# Q3 — does cluster_finding have a 'version' column referenced in M20 precedent's notes?
divider("cluster_finding columns (re-confirm)")
for r in c.execute("PRAGMA table_info(cluster_finding)"):
    print(f"  {r['name']} {r['type']}")


# Q4 — gap rows currently in M39
divider("M39 cluster_finding gap rows (target of Operation 7)")
for r in c.execute("""
    SELECT cf.id, q.question_code,
           COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope,
           cf.finding_status,
           SUBSTR(cf.finding_text, 1, 80) AS preview
    FROM cluster_finding cf
    JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
    LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
    WHERE cf.cluster_code='M39'
      AND cf.finding_status='gap'
    ORDER BY q.question_code, scope
"""):
    print(f"  cf_id={r['id']:<6} {r['question_code']:<10} {r['scope']:<14} {r['finding_status']}")
    print(f"     preview: {r['preview']}")


# Q5 — confirm BOUNDARY exit pre-state
divider("BOUNDARY exit pre-state — terms 633, 6837, 2976")
for mti_id in (633, 6837, 2976):
    r = c.execute("""
        SELECT mt.id, mt.strongs_number, mt.cluster_code,
               (SELECT subgroup_code FROM cluster_subgroup cs
                JOIN mti_term_subgroup mts ON mts.cluster_subgroup_id=cs.id
                WHERE mts.mti_term_id=mt.id AND COALESCE(mts.delete_flagged,0)=0 LIMIT 1) AS sg
        FROM mti_terms mt WHERE mt.id=?
    """, (mti_id,)).fetchone()
    print(f"  mti={mti_id} {r['strongs_number']:<7} cluster={r['cluster_code']} subgroup={r['sg']}")

# Sub-group ids for M39
divider("M39 cluster_subgroup ids (resolved)")
for r in c.execute("""SELECT id, subgroup_code FROM cluster_subgroup
                      WHERE cluster_code='M39' ORDER BY sort_order"""):
    print(f"  id={r['id']:<3} subgroup_code={r['subgroup_code']}")


# Q6 — existing M39 cluster_finding rows at the 7 dōron supplementary prompts (for Op 6 decision)
divider("Op 6 — current M39-A cluster_finding state at the 7 dōron prompts")
for q in ['T0.4.1', 'T1.2.1', 'T2.3.1', 'T2.6.1', 'T3.9.1', 'T4.2.1', 'T6.3.1']:
    rows = list(c.execute("""
        SELECT cf.id, COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope,
               cf.finding_status, LENGTH(cf.finding_text) AS text_len
        FROM cluster_finding cf
        LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
        JOIN wa_obs_question_catalogue qq ON qq.obs_id=cf.obs_id
        WHERE cf.cluster_code='M39' AND qq.question_code=?
        ORDER BY scope
    """, (q,)))
    print(f"  {q}:")
    for r in rows:
        print(f"    cf_id={r['id']:<6} {r['scope']:<14} {r['finding_status']:<20} text_len={r['text_len']}")
