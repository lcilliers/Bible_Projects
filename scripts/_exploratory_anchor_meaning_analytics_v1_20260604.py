"""
_exploratory_anchor_meaning_analytics_v1_20260604.py  (READ-ONLY)

Across all clusters, isolate the ANCHOR verses that carry BOTH a Pass-A meaning
(analysis_note) AND keywords, ignore the rest, and run analytics:
  - by cluster
  - by Testament
  - by Book
  - by keyword (phrase frequency + token frequency)

Writes a markdown report to research/investigations/.
"""
import sqlite3, os, json, re
from collections import Counter, defaultdict

DB = os.path.join('database', 'bible_research.db')
OUT = os.path.join('research', 'investigations', 'anchor-meaning-analytics-20260604.md')

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# NOTE: no cluster-table join here — it fanned rows out. Cluster names are looked up
# separately from a deduped dict (one row per cluster_code).
BASE = """
FROM verse_context vc
JOIN wa_verse_records wr ON wr.id = vc.verse_record_id
LEFT JOIN books b        ON b.id = wr.book_id
LEFT JOIN mti_terms mt   ON mt.id = vc.mti_term_id
WHERE vc.is_anchor = 1
  AND COALESCE(vc.delete_flagged,0) = 0
  AND COALESCE(TRIM(vc.analysis_note),'') <> ''
  AND COALESCE(TRIM(vc.keywords),'')      <> ''
"""

# cluster_code -> display name (deduped; cluster_code is unique in `cluster`)
cluster_name = {}
for r in cur.execute("SELECT cluster_code, COALESCE(short_name, description, cluster_code) nm FROM cluster"):
    cluster_name[r['cluster_code']] = r['nm']

# ---- headline ----
tot_anchor = cur.execute(
    "SELECT COUNT(*) FROM verse_context WHERE is_anchor=1 AND COALESCE(delete_flagged,0)=0").fetchone()[0]
target = cur.execute("SELECT COUNT(*) " + BASE).fetchone()[0]

# ---- by cluster ----
by_cluster = cur.execute("""
SELECT COALESCE(TRIM(mt.cluster_code),'(none)') code, COUNT(*) n
""" + BASE + " GROUP BY code ORDER BY n DESC").fetchall()

# ---- by testament ----
by_test = cur.execute("""
SELECT COALESCE(NULLIF(TRIM(wr.testament),''), b.testament, '(unknown)') testament, COUNT(*) n
""" + BASE + " GROUP BY 1 ORDER BY n DESC").fetchall()

# ---- by book ----
by_book = cur.execute("""
SELECT COALESCE(b.name,'(unknown)') book, COALESCE(b.testament,'?') t,
       COALESCE(b.book_order,999) ord, COUNT(*) n
""" + BASE + " GROUP BY book, t, ord ORDER BY n DESC, ord ASC").fetchall()

# ---- keywords ----
rows = cur.execute("SELECT vc.keywords " + BASE).fetchall()
phrase_ct = Counter()
token_ct = Counter()
STOP = {'the','a','an','of','to','and','in','is','its','it','as','by','that','this',
        'with','for','on','at','or','be','being','into','from','not'}
n_with_kw = 0
total_phrases = 0
for r in rows:
    raw = r['keywords']
    try:
        arr = json.loads(raw)
        if not isinstance(arr, list):
            arr = [str(arr)]
    except Exception:
        arr = [p.strip() for p in re.split(r'[;,|]', raw) if p.strip()]
    if arr:
        n_with_kw += 1
    for ph in arr:
        ph = str(ph).strip().lower()
        if not ph:
            continue
        phrase_ct[ph] += 1
        total_phrases += 1
        for tok in re.findall(r"[a-z']+", ph):
            if tok not in STOP and len(tok) > 2:
                token_ct[tok] += 1

# ---- write ----
def tbl(rows, headers, fmt):
    out = ['| ' + ' | '.join(headers) + ' |', '|' + '|'.join(['---']*len(headers)) + '|']
    for r in rows:
        out.append('| ' + ' | '.join(fmt(r)) + ' |')
    return '\n'.join(out)

L = []
L.append('# Anchor verses with meaning + keywords — exploratory analytics')
L.append('')
L.append('> **Read-only exploration, 2026-06-04.** Source: `verse_context` (anchors with both a Pass-A')
L.append('> `analysis_note` *and* `keywords`), joined to `wa_verse_records` / `books` / `mti_terms` / `cluster`.')
L.append('> Script: `scripts/_exploratory_anchor_meaning_analytics_v1_20260604.py`.')
L.append('')
L.append('## Headline')
L.append('')
L.append(f'- **{target}** anchor verses carry **both** meaning and keywords — out of **{tot_anchor}** live anchors '
         f'(**{100*target/tot_anchor:.1f}%**).')
L.append(f'- These {target} anchors yield **{total_phrases}** keyword instances '
         f'(**{len(phrase_ct)}** distinct phrases; **{len(token_ct)}** distinct tokens).')
L.append(f'- So ~**{100*(tot_anchor-target)/tot_anchor:.0f}%** of anchor verses are *not yet* Pass-A enriched — '
         f'a direct measure of how much verse-meaning groundwork remains on the anchors specifically.')
L.append('')
L.append(f'## By cluster ({len(by_cluster)} clusters represented)')
L.append('')
L.append(tbl(by_cluster, ['Cluster', 'Name', 'Anchors'],
            lambda r: [r['code'], str(cluster_name.get(r['code'], '(uncategorised)')), str(r['n'])]))
L.append('')
L.append('## By Testament')
L.append('')
L.append(tbl(by_test, ['Testament', 'Anchors'], lambda r: [str(r['testament']), str(r['n'])]))
L.append('')
L.append(f'## By Book ({len(by_book)} books)')
L.append('')
L.append(tbl(by_book, ['Book', 'T', 'Anchors'],
            lambda r: [str(r['book']), str(r['t']), str(r['n'])]))
L.append('')
L.append('## By keyword — top 40 phrases')
L.append('')
L.append(tbl(phrase_ct.most_common(40), ['Keyword phrase', 'Count'],
            lambda r: [r[0], str(r[1])]))
L.append('')
L.append('## By keyword — top 40 tokens (phrases split into words, stopwords removed)')
L.append('')
L.append(tbl(token_ct.most_common(40), ['Token', 'Count'],
            lambda r: [r[0], str(r[1])]))
L.append('')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(L) + '\n')

print('target anchors:', target, '/', tot_anchor)
print('clusters:', len(by_cluster), '| books:', len(by_book),
      '| phrases:', len(phrase_ct), '| tokens:', len(token_ct))
print('wrote', OUT)
