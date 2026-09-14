"""
Escalation #1700 -- per-question answer-quality review tool.

For a given list of live question_codes, pulls a random sample (default 5, seeded for
reproducibility) of non-blob ("own", i.e. answers a single specific catalogue question, not
fanned out across several) answers per question, and writes one JSON file per section batch for
reading. Excludes finding.delete_flagged=1 and finding_question_link.delete_flagged=1 throughout,
matching every other #1700 query this session.

Usage: edit SECTION_LIKE and OUT_NAME below, then run.
"""
import sqlite3, json, random, sys

random.seed(1700)  # reproducible sampling

SECTION_LIKE = sys.argv[1] if len(sys.argv) > 1 else 'T0%'
OUT_NAME = sys.argv[2] if len(sys.argv) > 2 else 'section'
SAMPLE_N = 5

conn = sqlite3.connect('file:C:/Bible_study_projects/database/bible_research.db?mode=ro', uri=True)
conn.row_factory = sqlite3.Row

questions = conn.execute(
    "SELECT obs_id, question_code, question_text FROM wa_obs_question_catalogue "
    "WHERE deleted=0 AND section LIKE ? ORDER BY obs_id", (SECTION_LIKE,)
).fetchall()

# fan-out map scoped to this section's own question set (a finding could theoretically fan out
# to questions outside the section too, but the section-scoped view is what matters for "is this
# answer specific to this one question")
obs_ids = [q['obs_id'] for q in questions]
placeholders = ','.join('?' * len(obs_ids))
fanout = {}
if obs_ids:
    for r in conn.execute(f'''
        SELECT f.id, COUNT(DISTINCT fql.question_id) n
        FROM finding_question_link fql JOIN finding f ON f.id=fql.finding_id
        WHERE fql.question_id IN ({placeholders}) AND f.delete_flagged=0 AND fql.delete_flagged=0
        GROUP BY f.id
    ''', obs_ids):
        fanout[r['id']] = r['n']

out = []
for q in questions:
    rows = conn.execute('''
        SELECT f.id, f.finding_value, f.cluster_code FROM finding_question_link fql
        JOIN finding f ON f.id=fql.finding_id
        WHERE fql.question_id=? AND f.delete_flagged=0 AND fql.delete_flagged=0
    ''', (q['obs_id'],)).fetchall()
    own = [r for r in rows if fanout.get(r['id'], 1) == 1]
    n_total = len(rows)
    n_own = len(own)
    sample = random.sample(own, min(SAMPLE_N, len(own))) if own else []
    out.append({
        'question_code': q['question_code'],
        'question_text': q['question_text'],
        'n_total_links': n_total,
        'n_own': n_own,
        'sample': [{'id': r['id'], 'cluster': r['cluster_code'], 'text': r['finding_value']} for r in sample],
    })

fname = fr'C:\Bible_study_projects\iba\docs\1700-sample-{OUT_NAME}-v1-20260914.json'
with open(fname, 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

for q in out:
    print(f"{q['question_code']:9} n_own={q['n_own']:4} sampled={len(q['sample'])}")
print('wrote', fname)
