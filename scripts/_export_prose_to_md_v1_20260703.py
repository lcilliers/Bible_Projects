"""Regenerate folder .md documents FROM the DB corpus (prose_section is canonical),
and/or VERIFY that the DB reproduces the existing folder files byte-for-byte.

Proves the researcher's requirement: the DB is the corpus; folder docs are
regenerable VIEWS, not a second source of truth (feedback_all_study_work_in_db).

Covers the active Psalm chapter-readings (type lexical_prose_chapter, book=Psa) and
the two syntheses (lexical_synthesis_psalter / _essay). The prose_section.body IS the
full markdown, so export = write body; verify = compare body to the file at source_file.

Usage:
  python scripts/_export_prose_to_md_v1_20260703.py --verify
  python scripts/_export_prose_to_md_v1_20260703.py --export --outdir DIR
"""
import sqlite3, os, sys, io

DB = os.path.join('database', 'bible_research.db')

def rows(conn):
    cur = conn.cursor()
    q = """
      SELECT id, section_type_id, heading, body, source_file,
             CAST(json_extract(metadata_json,'$.chapter') AS INT) ch
      FROM prose_section
      WHERE COALESCE(delete_flagged,0)=0
        AND ( (section_type_id=104 AND json_extract(metadata_json,'$.book')='Psa'
               AND json_extract(metadata_json,'$.phase')='2-chapter-reading')
              OR section_type_id IN (105,106) )
      ORDER BY section_type_id, ch, id
    """
    return cur.execute(q).fetchall()

def norm(s):
    return (s or '').replace('\r\n', '\n').rstrip('\n')

def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    data = rows(conn)
    if '--verify' in sys.argv:
        ok = miss = mismatch = 0
        for r in data:
            sf = r['source_file']
            if not sf or not os.path.exists(sf):
                miss += 1; print(f"  [no file] id {r['id']} ({sf})"); continue
            disk = norm(io.open(sf, encoding='utf-8').read())
            if norm(r['body']) == disk:
                ok += 1
            else:
                mismatch += 1
                print(f"  [MISMATCH] id {r['id']} <-> {sf}")
        print(f"\nverify: {ok} reproduce byte-for-byte, {mismatch} mismatched, {miss} file-missing, of {len(data)} corpus docs")
        return
    if '--export' in sys.argv:
        outdir = None
        if '--outdir' in sys.argv:
            outdir = sys.argv[sys.argv.index('--outdir')+1]
        n = 0
        for r in data:
            if r['section_type_id'] == 104:
                sub = os.path.join(outdir or 'verse-analysis/psalms/readings')
                fn = f"wa-psalm{r['ch']}-inner-being-reading.md"
            else:
                sub = os.path.join(outdir or 'verse-analysis/_reports')
                fn = os.path.basename(r['source_file']) if r['source_file'] else f"synthesis-{r['id']}.md"
            os.makedirs(sub, exist_ok=True)
            io.open(os.path.join(sub, fn), 'w', encoding='utf-8').write(norm(r['body']) + '\n')
            n += 1
        print(f"exported {n} docs from DB -> {outdir or '(default dirs)'}")
        return
    print("use --verify or --export [--outdir DIR]")

if __name__ == '__main__':
    main()
