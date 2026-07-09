"""
_exploratory_keyword_bias_extract_v1_20260604.py  (READ-ONLY)

Bias-trap: for three loaded interpretive keywords (eschatological, defilement, corrupt),
pull every meaning+keyword anchor whose keywords contain the token, and lay the actual
verse text, the Pass-A meaning, and the keywords side by side for human review.
"""
import sqlite3, os, json

DB = os.path.join('database', 'bible_research.db')
OUT = os.path.join('research', 'investigations', 'keyword-bias-extract-20260604.md')
TARGETS = ['eschatological', 'defilement', 'corrupt']

conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
cur = conn.cursor()

cluster_name = {r['cluster_code']: (r['short_name'] or r['cluster_code'])
                for r in cur.execute("SELECT cluster_code, short_name FROM cluster")}

def fetch(kw):
    return cur.execute("""
      SELECT wr.reference ref, wr.testament t, b.name book,
             TRIM(mt.cluster_code) code, wr.verse_text vtext,
             vc.analysis_note meaning, vc.keywords keywords
      FROM verse_context vc
      JOIN wa_verse_records wr ON wr.id = vc.verse_record_id
      LEFT JOIN books b      ON b.id = wr.book_id
      LEFT JOIN mti_terms mt ON mt.id = vc.mti_term_id
      WHERE vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
        AND COALESCE(TRIM(vc.analysis_note),'')<>'' AND COALESCE(TRIM(vc.keywords),'')<>''
        AND LOWER(vc.keywords) LIKE ?
      ORDER BY mt.cluster_code, b.book_order, wr.chapter, wr.verse_num
    """, ('%' + kw + '%',)).fetchall()

def fmt_kw(raw):
    try:
        arr = json.loads(raw)
        if isinstance(arr, list):
            return ', '.join(f'`{x}`' for x in arr)
    except Exception:
        pass
    return f'`{raw}`'

L = []
L.append('# Keyword bias-trap — eschatological · defilement · corrupt')
L.append('')
L.append('> **Read-only review extract, 2026-06-04.** For each loaded interpretive keyword, every')
L.append('> meaning+keyword **anchor** whose keywords contain the token, with the **actual verse**, the')
L.append('> **Pass-A meaning**, and the **keywords**. Purpose: trap over-reading / imposed interpretation.')
L.append('> Script: `scripts/_exploratory_keyword_bias_extract_v1_20260604.py`.')
L.append('>')
L.append('> **How to mark up:** flag any row where the meaning/keyword reads *more* into the verse than the')
L.append('> text supports (e.g. "eschatological" on a plainly present/physical rescue; "defilement" or')
L.append('> "corrupt" as a moral verdict the verse does not make). Add your note inline after the entry.')
L.append('')

for kw in TARGETS:
    rows = fetch(kw)
    L.append('---')
    L.append('')
    L.append(f'## `{kw}` — {len(rows)} anchors')
    L.append('')
    cur_code = None
    for r in rows:
        if r['code'] != cur_code:
            cur_code = r['code']
            L.append(f'### {cur_code} — {cluster_name.get(cur_code, "?")}')
            L.append('')
        ref = r['ref'] or '(no ref)'
        L.append(f'**{ref}**  · {r["book"]} ({r["t"]})')
        L.append('')
        L.append(f'- *Verse:* {(r["vtext"] or "").strip()}')
        L.append(f'- *Meaning:* {(r["meaning"] or "").strip()}')
        L.append(f'- *Keywords:* {fmt_kw(r["keywords"])}')
        L.append('')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(L) + '\n')

for kw in TARGETS:
    print(kw, len(fetch(kw)))
print('wrote', OUT)
