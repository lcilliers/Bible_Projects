"""
Create + populate the base index table `verse_span_index`.
Each record = one SPAN (from verse_morphology) with its TERM and its VERSE.
Source = verse_morphology (1 row per span); reference looked up from `verse`.
No mti join — term is the morphology's own Strong's.

Reversible: DROP TABLE verse_span_index to undo. Idempotent (drops + rebuilds).
"""
import sqlite3, os
DB=os.path.join('database','bible_research.db')

DDL="""
CREATE TABLE verse_span_index (
  id             INTEGER PRIMARY KEY,
  -- verse
  verse_id       INTEGER,
  reference      TEXT,
  -- span
  word_index     INTEGER,
  surface        TEXT,
  pos            TEXT,
  morph_code     TEXT,
  stem           TEXT,
  language       TEXT,
  -- term
  strongs        TEXT,
  primary_strong TEXT,
  source         TEXT DEFAULT 'verse_morphology',
  built_at       TEXT DEFAULT (datetime('now'))
)
"""

def main():
    c=sqlite3.connect(DB); cur=c.cursor()
    cur.execute("DROP TABLE IF EXISTS verse_span_index")
    cur.execute(DDL)
    cur.execute("""
        INSERT INTO verse_span_index
          (verse_id, reference, word_index, surface, pos, morph_code, stem, language, strongs, primary_strong)
        SELECT vm.verse_id, v.reference, vm.word_index, vm.surface, vm.pos, vm.morph_code,
               vm.stem, vm.language, vm.strongs, vm.primary_strong
        FROM verse_morphology vm
        LEFT JOIN verse v ON v.id = vm.verse_id
        ORDER BY vm.verse_id, vm.word_index
    """)
    c.commit()
    n=cur.execute("SELECT COUNT(*) FROM verse_span_index").fetchone()[0]
    src=cur.execute("SELECT COUNT(*) FROM verse_morphology").fetchone()[0]
    verses=cur.execute("SELECT COUNT(DISTINCT verse_id) FROM verse_span_index").fetchone()[0]
    terms=cur.execute("SELECT COUNT(DISTINCT primary_strong) FROM verse_span_index").fetchone()[0]
    print(f"verse_span_index built: {n} rows (source verse_morphology={src})  match={'YES' if n==src else 'NO'}")
    print(f"  distinct verses={verses}  distinct primary_strong (terms)={terms}")
    print("  sample:")
    for r in cur.execute("SELECT reference, word_index, surface, strongs, primary_strong FROM verse_span_index WHERE reference='Pro 24:20' ORDER BY word_index"):
        print(f"    {r[0]} [{r[1]}] {r[2]:<10} strongs={r[3]:<14} term={r[4]}")
    c.close()

if __name__=='__main__': main()
