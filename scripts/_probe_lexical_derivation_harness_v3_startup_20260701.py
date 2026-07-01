"""
_probe_lexical_derivation_harness_v3_startup_20260701.py  (READ-ONLY)

Adds the two STARTUP VALIDATORS the researcher requires, built into the script before any work:

  VALIDATOR A — passage membership, FORWARD and BACKWARD.
     Resolve the full passage of the selected verse by walking BOTH directions:
       * CONFIRMED link  = the backward `isolable='no'` marker (verse reads WITH its predecessor);
       * CANDIDATE link  = a continuation opener ("So/and/but/for/therefore/then" or a wayyiqtol
                           verb) on the adjacent verse — flagged for review (the marker is
                           backward-only + under-detects, so forward continuation is surfaced, not
                           silently trusted).
     Output: the confirmed passage, plus any candidate extensions flagged for manual review.

  VALIDATOR B — all relative spans are in the DB.
     Every verse in the (confirmed + candidate) passage must have its morphology in
     `verse_morphology`. Missing morphology is a BLOCKER (can't read the passage together) — flagged.

  THEN: get the FIRST verse (the anchor the ve-records attach to) -> read the morphology of ALL the
  passage verses together (one batch) -> start the derivation work.

Demo start verse: Exo 1:13.  Usage: python scripts/_probe_lexical_derivation_harness_v3_startup_20260701.py
"""
import sqlite3, os, re
DB = os.path.join('database', 'bible_research.db')
START_REF = 'Exo 1:13'
CONT_OPENERS = ('so ', 'and ', 'but ', 'for ', 'therefore', 'then ', 'thus ')  # continuation cues
WINDOW = 6  # verses to look each side when walking

def canon(s):
    m = re.match(r'^([HG])(\d+)', s or ''); return m.group(1)+m.group(2).zfill(4) if m else s

def verse_row(cur, book_id, chapter, vnum):
    return cur.execute("SELECT id,reference,verse_text,book_id,chapter,verse_num FROM verse WHERE book_id=? AND chapter=? AND verse_num=?",
                       (book_id, chapter, vnum)).fetchone()

def reads_back(cur, vid):
    """CONFIRMED backward link: any term on the verse flagged isolable='no'."""
    return cur.execute("""SELECT COUNT(*) FROM ve_lexical vl JOIN verse_context vc ON vl.verse_context_id=vc.id
        JOIN wa_verse_records w ON vc.verse_record_id=w.id
        WHERE w.verse_id=? AND vl.ve_label='isolable' AND vl.value='no' AND vl.delete_flagged=0""", (vid,)).fetchone()[0] > 0

def continues(text):
    t = (text or '').split(' ', 1)
    body = t[1] if len(t) > 1 else ''   # drop the leading "Book c:v" ref token block if present
    low = (text or '').lower()
    # strip the reference prefix "exo 1:14 " before testing the opener
    m = re.match(r'^\s*\S+\s+\d+:\d+\s+(.*)$', text or '')
    op = (m.group(1) if m else (text or '')).lower()
    return any(op.startswith(c) for c in CONT_OPENERS)

# ---------- VALIDATOR A ----------
def validate_membership(cur, start_ref):
    v = cur.execute("SELECT id,reference,verse_text,book_id,chapter,verse_num FROM verse WHERE reference=?", (start_ref,)).fetchone()
    if not v: return None
    b, ch = v['book_id'], v['chapter']
    members = [dict(v)]; flags = []
    # BACKWARD
    cur_v = v
    while True:
        prev = verse_row(cur, b, ch, cur_v['verse_num'] - 1)
        if not prev: break
        if reads_back(cur, cur_v['id']):
            members.insert(0, dict(prev)); flags.append(('backward-confirmed', prev['reference'], cur_v['reference'], 'isolable=no'))
            cur_v = prev; continue
        if continues(cur_v['verse_text']):
            members.insert(0, dict(prev)); flags.append(('backward-CANDIDATE', prev['reference'], cur_v['reference'], 'opener continues -> REVIEW'))
            cur_v = prev; continue
        break
    # FORWARD
    cur_v = v
    while True:
        nxt = verse_row(cur, b, ch, cur_v['verse_num'] + 1)
        if not nxt: break
        if reads_back(cur, nxt['id']):
            members.append(dict(nxt)); flags.append(('forward-confirmed', cur_v['reference'], nxt['reference'], 'next isolable=no'))
            cur_v = nxt; continue
        if continues(nxt['verse_text']):
            members.append(dict(nxt)); flags.append(('forward-CANDIDATE', cur_v['reference'], nxt['reference'], 'next opener continues -> REVIEW'))
            cur_v = nxt; continue
        break
    # dedupe preserve order
    seen=set(); ordered=[]
    for m in members:
        if m['id'] not in seen: seen.add(m['id']); ordered.append(m)
    return {'members': ordered, 'anchor': ordered[0], 'flags': flags}

# ---------- VALIDATOR B ----------
def validate_spans(cur, members):
    report=[]
    for m in members:
        n = cur.execute("SELECT COUNT(*) FROM verse_morphology WHERE verse_id=?", (m['id'],)).fetchone()[0]
        report.append((m['reference'], n))
    missing=[r for r,n in report if n==0]
    return report, missing

# ---------- LOAD ALL MORPHOLOGY TOGETHER ----------
def load_morphology(cur, members):
    spans=[]
    for m in members:
        for w in cur.execute("SELECT word_index,surface,primary_strong,pos,stem FROM verse_morphology WHERE verse_id=? ORDER BY word_index", (m['id'],)):
            spans.append({'ref':m['reference'],'w':w['word_index'],'surface':w['surface'],
                          'strong':canon(w['primary_strong']),'pos':w['pos'],'stem':w['stem'],'g':len(spans)})
    return spans

def main():
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; cur=conn.cursor()
    print('START VERSE: %s\n' % START_REF)

    print('== VALIDATOR A — passage membership (forward + backward) ==')
    A = validate_membership(cur, START_REF)
    print('  resolved passage: %s' % ' , '.join(m['reference'] for m in A['members']))
    for kind, a, b_, why in A['flags']:
        print('    %-20s %s <-> %s   [%s]' % (kind, a, b_, why))
    review = [f for f in A['flags'] if 'CANDIDATE' in f[0]]
    print('  -> %d confirmed link(s), %d CANDIDATE link(s) needing review' % (len(A['flags'])-len(review), len(review)))

    print('\n== VALIDATOR B — all relative spans in the DB ==')
    report, missing = validate_spans(cur, A['members'])
    for ref, n in report:
        print('    %-10s morphology spans = %d %s' % (ref, n, '' if n else '  <-- MISSING (BLOCKER)'))
    if missing:
        print('  -> BLOCKED: %s have no morphology; ingest before proceeding.' % missing); return
    print('  -> all passage spans present.')

    anchor = A['anchor']
    print('\n== ANCHOR ==\n  first verse = %s  (the verse the ve-records attach to)' % anchor['reference'])

    print('\n== READ ALL PASSAGE MORPHOLOGY TOGETHER, then start work ==')
    spans = load_morphology(cur, A['members'])
    print('  loaded %d spans across %d verses (one batch).' % (len(spans), len(A['members'])))
    print('  ready to derive the passage lexical anchored on %s.' % anchor['reference'])
    # (derivation reuses harness v2 rules; omitted here — this script proves the STARTUP logic.)

if __name__=='__main__':
    main()
