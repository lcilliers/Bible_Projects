#!/usr/bin/env python
"""Pull a batch of lexicals for MANUAL source-verification of one dimension (read-only, v1 2026-07-14).

For the dimension-by-dimension source check: gives me, per lexical (in canonical order), the SOURCE
(verse text + Hebrew/Greek transliteration + lexicon gloss + morphology) alongside the stored dimension
value, so I can judge each value against the source. It computes NOTHING about correctness — I do that.

Order = book, chapter, verse_num, span_id (the canonical lexical order; "lexical 1" = the first).
Skips lexicals already verified for this ve_nr (resumable).

Usage: python scripts/_pull_verify_batch_v1_20260714.py --book 19 --ve 101 --limit 25
"""
import sqlite3, os, sys, re

DB = os.path.join('database', 'bible_research.db')
PROV = {19: 'reread-psalms-2026', 20: 'reread-proverbs-2026'}

def main():
    a = sys.argv
    bid = int(a[a.index('--book')+1])
    ve = int(a[a.index('--ve')+1])
    limit = int(a[a.index('--limit')+1]) if '--limit' in a else 25
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    prov = PROV[bid]
    done = {r[0] for r in c.execute("SELECT verse_span_id FROM ve_lexical_verification WHERE ve_nr=?", (ve,))}
    rows = c.execute("""SELECT si.id sid, v.reference ref, v.chapter, v.verse_num, si.strongs, si.primary_strong,
              si.surface, si.morph_code, si.stem, v.verse_text,
              x.value stored, x.from_span, x.to_span, x.resolution
           FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
           JOIN ve_lexical x ON x.verse_span_id=si.id AND x.ve_nr=? AND x.source_provenance=? AND x.delete_flagged=0
           WHERE v.book_id=? AND si.role='characteristic' AND si.role_provenance='read-2026'
           ORDER BY v.chapter, v.verse_num, si.id""", (ve, prov, bid)).fetchall()
    todo = [r for r in rows if r['sid'] not in done]
    total = len(rows); ndone = total - len(todo)
    print(f"# D-verify book={bid} ve={ve} | {ndone}/{total} already verified | showing next {min(limit,len(todo))}")
    def lex(strongs):
        base = re.match(r'([HG]\d+)', strongs or '')
        if not base: return ('', '')
        m = c.execute("SELECT transliteration, gloss FROM mti_terms WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0 LIMIT 1", (base.group(1),)).fetchone()
        return (m['transliteration'] or '', m['gloss'] or '') if m else ('', '')
    for i, r in enumerate(todo[:limit]):
        idx = ndone + i + 1
        tr, gl = lex(r['primary_strong'] or r['strongs'])
        pair = f" | PAIR from={r['from_span']} to={r['to_span']} res={r['resolution']}" if r['resolution']=='span' else ""
        print(f"\n[{idx}] span {r['sid']} | {r['ref']} | {r['strongs']} morph={r['morph_code']} | translit={tr!r} gloss={gl!r}")
        print(f"    surface(EN)='{r['surface']}'{pair}")
        print(f"    VERSE: {r['verse_text']}")
        print(f"    STORED ve{ve}: {r['stored']!r}")
    c.close()

if __name__ == '__main__':
    main()
