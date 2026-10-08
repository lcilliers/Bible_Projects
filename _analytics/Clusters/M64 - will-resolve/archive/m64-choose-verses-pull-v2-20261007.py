"""#1978, 2026-10-07: pinpointed pull of a set of M64 Strong's (the "choose" set): every verse with any of
the words, its ESV text, the hits in the verse (strong, surface, morph, position), the other M-cluster words
in the same verse, and where the verse is cited in the narrative. Read-only against iba.db.
Derived from m64-H6942H-verses-pull-v1-20261006.py (one Strong's) to take a list.

Usage: python m64-choose-verses-pull-v2-20261007.py [STRONG ...] [--tag NAME]
       (default H0977 G0830 H7148 G0140 G4401 H0972 G0138 G1586 G1588 G1589, tag "choose")
v2 2026-10-07: H0972, G0138, G1586, G1588, G1589 added (researcher: "pull H0972 and G0138,G1586,G1588, and G1589 next with the same script").
"""
import csv, importlib.util, json, os, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'iba', 'app', 'db', 'iba.db'))
ARGS = sys.argv[1:]
TAG = 'choose'
if '--tag' in ARGS:
    i = ARGS.index('--tag'); TAG = ARGS[i + 1]; del ARGS[i:i + 2]
STRONGS = ARGS or ['H0977', 'G0830', 'H7148', 'G0140', 'G4401', 'H0972', 'G0138', 'G1586', 'G1588', 'G1589']
OUT = os.path.join(HERE, f'm64-{TAG}-verses-v2-20261007.csv')

spec = importlib.util.spec_from_file_location('xref', os.path.join(HERE, 'verse-narrative-ot-crossref-v2-20261006.py'))
xref = importlib.util.module_from_spec(spec)
spec.loader.exec_module(xref)

SQL = """
WITH hits AS (
  SELECT vl.verse_id, vl.strong, vl.position, vl.surface, vl.morph_code, vl.code_ordinal
  FROM verse_lexical vl WHERE vl.deleted = 0 AND vl.strong IN (SELECT value FROM json_each(:s))
),
others AS (
  SELECT vl.verse_id,
         GROUP_CONCAT(cs.cluster_code || ' ' || vl.strong || ' ' || COALESCE(st.stepGloss, '') || ' "' || vl.surface || '" @' || vl.position, ' | ') AS words
  FROM (SELECT * FROM verse_lexical ORDER BY verse_id, position) vl
  JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0
  JOIN cluster c ON c.cluster_code = cs.cluster_code AND c.deleted = 0
  LEFT JOIN strong st ON st.strongNumber = vl.strong
  WHERE vl.deleted = 0 AND cs.cluster_code LIKE 'M%' AND vl.strong NOT IN (SELECT value FROM json_each(:s))
    AND vl.verse_id IN (SELECT verse_id FROM hits)
  GROUP BY vl.verse_id
)
SELECT v.reference, v.osisId,
       COUNT(*) AS hits,
       GROUP_CONCAT(h.strong || ' "' || h.surface || '" ' || COALESCE(h.morph_code, '') || ' @' || h.position, ' | ') AS hit_words,
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
    cur = con.execute(SQL, {'s': json.dumps(STRONGS)})
    cols = [d[0] for d in cur.description]
    rows = [dict(zip(cols, r)) for r in cur.fetchall()]
    narr = xref.narrative_index()
    for r in rows:
        ref = r['reference']
        if ':' not in ref:  # one-chapter book stored as "2Jo 13" (osisId 2John.1.13): read as chapter 1
            b, v = ref.rsplit(' ', 1); ref = f'{b} 1:{v}'
        places = narr.get(xref.ref_key(ref), [])
        r['narrative_n'] = len(places)
        r['narrative_refs'] = ' | '.join(places)
    out_cols = ['reference', 'hits', 'hit_words', 'other_m_words', 'narrative_n', 'narrative_refs', 'esv_text']
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=out_cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    print(f'{" ".join(STRONGS)}: {len(rows)} verses, {sum(r["hits"] for r in rows)} rows -> {OUT}')


if __name__ == '__main__':
    main()
