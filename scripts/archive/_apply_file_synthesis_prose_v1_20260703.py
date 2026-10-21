"""File a cross-chapter SYNTHESIS document as a DB-canonical prose_section
(feedback_all_study_work_in_db). Not chapter-keyed (unlike the chapter-reading
filer) — keyed by (type_code + metadata scope). Version-aware: supersedes any
prior active synthesis of the same type+scope.

Reusable (feedback_reusable_engine_scripts_and_continuous_learning): pass a new
--code/--scope/--story to file other syntheses (e.g. Proverbs later).

Usage:
  python scripts/_apply_file_synthesis_prose_v1_20260703.py \
      --code=lexical_synthesis_psalter --label="Psalter inner-being synthesis (per characteristic)" \
      --scope="Psalms 1-150" --heading="..." --story=PATH [--live]
"""
import sqlite3, os, sys, io, json
from datetime import datetime, timezone

DB = os.path.join('database', 'bible_research.db')

def arg(n, d=None):
    k = f'--{n}='
    for a in sys.argv:
        if a.startswith(k):
            return a[len(k):]
    return d

def main():
    CODE = arg('code'); LABEL = arg('label', CODE); SCOPE = arg('scope', '')
    HEAD = arg('heading', CODE); STORY = arg('story'); LIVE = '--live' in sys.argv
    if not (CODE and STORY):
        print("need --code and --story"); return
    body = io.open(STORY, encoding='utf-8').read()
    wc = len(body.split())
    NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; cur = conn.cursor()
    # ensure type
    t = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (CODE,)).fetchone()
    if t:
        tid = t['id']
    else:
        nid = (cur.execute("SELECT COALESCE(MAX(id),0)+1 m FROM prose_section_type").fetchone()['m'])
        cur.execute("""INSERT INTO prose_section_type (id,code,label,source_stage,description,sort_order,delete_flagged,created_at)
            VALUES (?,?,?,?,?,?,0,?)""", (nid, CODE, LABEL, 'synthesis', LABEL, nid, NOW))
        tid = nid
    meta = json.dumps({"kind": "psalter-synthesis", "scope": SCOPE})
    prev = cur.execute("""SELECT id,version FROM prose_section WHERE section_type_id=?
        AND json_extract(metadata_json,'$.scope')=? AND COALESCE(delete_flagged,0)=0
        ORDER BY version DESC LIMIT 1""", (tid, SCOPE)).fetchone()
    new_ver = (prev['version'] + 1) if prev and prev['version'] else 1
    print("type:", CODE, "id", tid, "| prior:", dict(prev) if prev else None, "-> version", new_ver, "| words:", wc)
    if not LIVE:
        print("DRY-RUN. Re-run with --live."); return
    cur.execute("""INSERT INTO prose_section
        (registry_id,section_type_id,heading,body,word_count,status,version,supersedes_id,author,created_at,metadata_json,source_file,delete_flagged)
        VALUES (NULL,?,?,?,?, 'approved', ?, ?, 'claude_code', ?, ?, ?, 0)""",
        (tid, HEAD, body, wc, new_ver, (prev['id'] if prev else None), NOW, meta, STORY))
    nid = cur.lastrowid
    if prev:
        cur.execute("UPDATE prose_section SET superseded_by_id=?, delete_flagged=1 WHERE id=?", (nid, prev['id']))
    conn.commit()
    r = cur.execute("SELECT id,heading,version,status,word_count,section_type_id FROM prose_section WHERE id=?", (nid,)).fetchone()
    print("wrote prose_section:", dict(r))

if __name__ == '__main__':
    main()
