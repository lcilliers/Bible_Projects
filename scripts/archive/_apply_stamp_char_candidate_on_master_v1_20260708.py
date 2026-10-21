"""_apply_stamp_char_candidate_on_master_v1_20260708.py — M65: stamp the candidate-characteristic
seed onto the master index.

Non-destructive: adds char_candidate (1/0) + char_candidate_tag (the "Reg N word" / "IB:gloss" source)
to verse_span_index, leaving the M64 backfilled `role` intact. A span is flagged when its base
primary_strong is a seed candidate (char_matched or ib_candidate in the lemma-inventory JSON).
Seed = OT (Hebrew/Aramaic) candidate lemmas.

Idempotent: re-run resets + re-stamps from the current JSON. Read-only unless --live.
"""
import sqlite3, os, sys, json, re, shutil, datetime
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
NOW=datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
JSONP='research/discovery/lemma-inventory-master-no-particles-20260707.json'

def base(s):
    m=re.match(r'([HG]\d+)', s or ''); return m.group(1) if m else s

def main():
    data=json.load(open(JSONP,encoding='utf-8'))
    seed={}
    for L in data['lemmas']:
        if L['language'] in ('Hebrew','Aramaic') and (L.get('char_matched') or L.get('ib_candidate')):
            seed[base(L['strong'])] = (L['char_matched'][0] if L.get('char_matched') else 'IB:'+str(L.get('gloss')))
    print('seed candidate lemmas (OT):', len(seed))

    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
    cols=[r['name'] for r in cur.execute('PRAGMA table_info(verse_span_index)')]
    have=all(x in cols for x in ('char_candidate','char_candidate_tag'))

    # count target spans (OT real-strong whose base lemma is a seed candidate)
    rows=cur.execute("""SELECT vsi.id, substr(vsi.primary_strong,1,5) s FROM verse_span_index vsi
      JOIN verse v ON v.id=vsi.verse_id JOIN books b ON b.id=v.book_id
      WHERE b.testament='OT' AND vsi.primary_strong LIKE 'H%' AND vsi.primary_strong NOT LIKE 'H9%'""").fetchall()
    targets=[(r['id'], seed[base(r['s'])]) for r in rows if base(r['s']) in seed]
    print('OT real-strong spans total: %d | to flag as candidate: %d (%.1f%%)'%(len(rows), len(targets), 100*len(targets)/len(rows)))
    if not LIVE:
        print('\nDRY-RUN. Re-run with --live.'); c.close(); return

    bpath='backups/bible_research.pre-charcand-%s.db'%NOW.replace(':','').replace('-','')
    os.makedirs('backups',exist_ok=True); shutil.copy2(DB,bpath); print('backup:',bpath)

    if not have:
        cur.execute("ALTER TABLE verse_span_index ADD COLUMN char_candidate INTEGER")
        cur.execute("ALTER TABLE verse_span_index ADD COLUMN char_candidate_tag TEXT")
        print('columns added.')
    cur.execute("UPDATE verse_span_index SET char_candidate=NULL, char_candidate_tag=NULL")
    cur.executemany("UPDATE verse_span_index SET char_candidate=1, char_candidate_tag=? WHERE id=?",
                    [(tag,sid) for sid,tag in targets])
    # schema_version M65
    row=cur.execute('SELECT id, migration_history FROM schema_version ORDER BY rowid DESC LIMIT 1').fetchone()
    hist=json.loads(row['migration_history'])
    if not any(e.get('version')=='M65' for e in hist):
        hist.append({"version":"M65","description":"Stamp candidate-characteristic seed onto master (verse_span_index.char_candidate/char_candidate_tag); non-destructive, leaves role intact. 3.38.0->3.39.0","applied_at":NOW})
        cur.execute('UPDATE schema_version SET version_code=?, applied_at=?, migration_history=? WHERE id=?',('3.39.0',NOW,json.dumps(hist),row['id']))
        print('schema_version -> 3.39.0 (M65).')
    c.commit()
    n=cur.execute('SELECT COUNT(*) n FROM verse_span_index WHERE char_candidate=1').fetchone()['n']
    v=cur.execute('SELECT COUNT(DISTINCT verse_id) n FROM verse_span_index WHERE char_candidate=1').fetchone()['n']
    tot=cur.execute('SELECT COUNT(*) n FROM verse_span_index').fetchone()['n']
    print('LIVE: char_candidate=1 on %d spans, across %d verses. (master rows intact: %d)'%(n,v,tot))
    c.close()

if __name__=='__main__': main()
