"""#1978, 2026-10-06: pinpointed pull of one M64 Strong's: every verse with the word, its ESV text, the
hits in the verse (surface, morph, position), the other M-cluster words in the same verse, and where the
verse is cited in the narrative. Read-only against iba.db.

Usage: python m64-H6942H-verses-pull-v1-20261006.py [STRONG]   (default H6942H)
"""
import csv, importlib.util, os, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
STRONG = sys.argv[1] if len(sys.argv) > 1 else 'H6942H'
OUT = os.path.join(HERE, f'm64-{STRONG}-verses-v1-20261006.csv')

spec = importlib.util.spec_from_file_location('xref', os.path.join(HERE, 'verse-narrative-ot-crossref-v2-20261006.py'))
xref = importlib.util.module_from_spec(spec)
spec.loader.exec_module(xref)

SQL = """
WITH hits AS (
  SELECT vl.verse_id, vl.position, vl.surface, vl.morph_code, vl.code_ordinal
  FROM verse_lexical vl WHERE vl.deleted = 0 AND vl.strong = :s
),
others AS (
  SELECT vl.verse_id,
         GROUP_CONCAT(cs.cluster_code || ' ' || vl.strong || ' ' || COALESCE(st.stepGloss, '') || ' "' || vl.surface || '" @' || vl.position, ' | ') AS words
  FROM (SELECT * FROM verse_lexical ORDER BY verse_id, position) vl
  JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0
  JOIN cluster c ON c.cluster_code = cs.cluster_code AND c.deleted = 0
  LEFT JOIN strong st ON st.strongNumber = vl.strong
  WHERE vl.deleted = 0 AND cs.cluster_code LIKE 'M%' AND vl.strong <> :s
    AND vl.verse_id IN (SELECT verse_id FROM hits)
  GROUP BY vl.verse_id
)
SELECT v.reference, v.osisId,
       COUNT(*) AS hits,
       GROUP_CONCAT('"' || h.surface || '" ' || COALESCE(h.morph_code, '') || ' @' || h.position, ' | ') AS hit_words,
       o.words AS other_m_words,
       v.text AS esv_text
FROM hits h
JOIN verse v ON v.id = h.verse_id AND v.deleted = 0
LEFT JOIN others o ON o.verse_id = h.verse_id
LEFT JOIN cfg_book_order bo ON bo.book = substr(v.osisId, 1, instr(v.osisId, '.') - 1)
GROUP BY v.id
ORDER BY bo.ordinal,
         CAST(substr(v.osisId, instr(v.osisId, '.') + 1, instr(substr(v.osisId, instr(v.osisId, '.') + 1), '.') - 1) AS INTEGER),
         CAST(substr(substr(v.osisId, instr(v.osisId, '.') + 1), instr(substr(v.osisId, instr(v.osisId, '.') + 1), '.') + 1) AS INTEGER)
"""


def main():
    con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    cur = con.execute(SQL, {'s': STRONG})
    cols = [d[0] for d in cur.description]
    rows = [dict(zip(cols, r)) for r in cur.fetchall()]
    narr = xref.narrative_index()
    for r in rows:
        places = narr.get(xref.ref_key(r['reference']), [])
        r['narrative_n'] = len(places)
        r['narrative_refs'] = ' | '.join(places)
    out_cols = ['reference', 'hits', 'hit_words', 'other_m_words', 'narrative_n', 'narrative_refs', 'esv_text']
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=out_cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    print(f'{STRONG}: {len(rows)} verses, {sum(r["hits"] for r in rows)} rows -> {OUT}')


if __name__ == '__main__':
    main()
