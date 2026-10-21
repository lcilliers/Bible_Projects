#!/usr/bin/env python
"""_apply_psalms_gate1_completeness_v1_20260706.py — Step (d) Gate-1 completeness for PSALMS.

For every CHARACTERISTIC span in Psalms (ve_nr=115, value='characteristic', role-reassess-2026)
ensure the chain is complete and linked:
  (1) TERM RECORDED  - if the base strong is not in mti_terms, register a thin term row
                       (strongs_number, translit, gloss, language) from lexicon. Marked
                       anchor_note='gate1-psalms-2026'. (Un-glossed strongs are SKIPPED + reported.)
  (2) VERSE-RECORD   - if no wa_verse_records row exists for (verse, this strong), create one,
                       assembled from verse_span_index + verse (data already in the DB; no STEP needed
                       for Psalms occurrences, which are already indexed). Linked by the BYPASS FKs
                       verse_id + verse_span_id + mti_term_id; legacy file_id/term_inv_id/word_registry_fk
                       left NULL (per reference_file_index_legacy_use_bypass_fks). note='gate1-psalms-2026'.
  (3) LINKS INTACT   - existing char-span verse-records missing verse_span_id / mti_term_id get them set.

Scope = characteristic spans ONLY (not qualifier/standalone) — this is the reviewed IB cut, not the
whole vocabulary. By-book: Psalms occurrences only; full programme-wide STEP onboarding of any newly
registered term is a separate global action (recorded as debt, not done here). Idempotent. Reversible
(everything stamped 'gate1-psalms-2026'). Read-only unless --live.
"""
import sqlite3, os, sys, re
from collections import defaultdict
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv
NOW='2026-07-06T00:00:00Z'
c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
def base(s): m=re.match(r'(H\d+)', s or ''); return m.group(1) if m else (s or '')
pb=cur.execute("SELECT id FROM books WHERE name='Psalms'").fetchone()['id']

# characteristic spans
spans=cur.execute("""SELECT vsi.id sid, vsi.verse_id vid, substr(vsi.primary_strong,1,5) s,
    vsi.surface, vsi.morph_code, vsi.stem, v.reference ref, v.verse_text vt, v.chapter ch, v.verse_num vn
  FROM ve_lexical vl JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id JOIN verse v ON v.id=vsi.verse_id
  WHERE v.book_id=? AND vl.ve_nr=115 AND vl.value='characteristic' AND vl.source_provenance='role-reassess-2026'
    AND COALESCE(vl.delete_flagged,0)=0""",(pb,)).fetchall()

# mti membership (all zero-pad forms)
mti_ids={}  # base-strong -> mti.id (choose Hebrew, non-deleted)
for r in cur.execute("SELECT id, strongs_number FROM mti_terms WHERE COALESCE(delete_flagged,0)=0 AND COALESCE(status,'') NOT IN ('delete','excluded','candidate_delete')"):
    if r['strongs_number']: mti_ids.setdefault(base(r['strongs_number']), r['id'])
def mti_variants(s):
    b=base(s); m=re.match(r'H0*(\d+)',b); forms=[b]
    if m: forms+=['H'+m.group(1),'H'+m.group(1).zfill(4),'H'+m.group(1).zfill(5)]
    return forms
def find_mti(s):
    for f in mti_variants(s):
        if f in mti_ids: return mti_ids[f]
    return None

# lexicon lookup
def lex(s):
    return cur.execute("SELECT gloss, transliteration t, language l FROM lexicon WHERE strong=? OR strong LIKE ? LIMIT 1",(s,s+'%')).fetchone()

# (1) missing terms
char_strongs=sorted(set(sp['s'] for sp in spans))
missing=[s for s in char_strongs if find_mti(s) is None]
to_register=[]; skipped_nogloss=[]
for s in missing:
    lx=lex(s)
    if not lx or not lx['gloss'] or lx['gloss'] in ('?',''):
        skipped_nogloss.append(s); continue
    to_register.append((s, lx['t'], lx['gloss'], lx['l'] or 'Hebrew'))
print(f"(1) missing terms: {len(missing)} | to register: {len(to_register)} | SKIPPED (no gloss): {skipped_nogloss}")

# existing verse-records keyed (verse_id, base strong)
wavr=defaultdict(list)
for r in cur.execute("SELECT id, verse_id, term_id, verse_span_id, mti_term_id FROM wa_verse_records WHERE book_id=? AND COALESCE(delete_flagged,0)=0",(pb,)):
    wavr[(r['verse_id'], base(r['term_id']))].append(dict(r))

# (2) spans needing a verse-record  (3) spans whose record needs a link
need_record=[]; need_link=[]
skip_span_nogloss=set(skipped_nogloss)
for sp in spans:
    if sp['s'] in skip_span_nogloss: continue
    recs=wavr.get((sp['vid'], base(sp['s'])),[])
    if not recs:
        need_record.append(sp)
    else:
        # any rec missing link?
        for rec in recs:
            if rec['verse_span_id'] is None or rec['mti_term_id'] is None:
                need_link.append((rec, sp)); break
print(f"(2) characteristic spans needing a NEW verse-record: {len(need_record)}")
print(f"(3) existing char-span verse-records needing link repair: {len(need_link)}")

if not LIVE:
    # show a sample created row
    if need_record:
        sp=need_record[0]; lx=lex(sp['s'])
        print("\nSAMPLE new verse-record:")
        print(f"  ref={sp['ref']} term_id={sp['s']} target={sp['surface']} morph={sp['morph_code']} "
              f"translit={(lx['t'] if lx else '')} verse_span_id={sp['sid']} note=gate1-psalms-2026")
    print("\nDRY-RUN. Re-run with --live."); sys.exit(0)

# --- LIVE ---
# sentinel wa_file_index row for gate-1 completions (file_id is NOT NULL; we never JOIN through it —
# data linkage uses verse_id/verse_span_id/mti_term_id per reference_file_index_legacy_use_bypass_fks)
sent=cur.execute("SELECT id FROM wa_file_index WHERE registry_id='GATE1-PSALMS-2026'").fetchone()
if sent: FILE_ID=sent['id']
else:
    cur.execute("""INSERT INTO wa_file_index (filename, registry_id, word, schema_version, phase, produced_date, revision_note, last_changed)
        VALUES ('GATE1-PSALMS-2026.sentinel','GATE1-PSALMS-2026','(gate1 psalms completions)','3.37.0',
                'Gate-1 completeness (bypass-FK sentinel)', ?, 'sentinel; not a real word file — do not join for data', ?)""",(NOW,NOW))
    FILE_ID=cur.lastrowid
    print(f"  created sentinel wa_file_index id={FILE_ID}")

reg=0
for s,t,g,l in to_register:
    ex=cur.execute("SELECT id FROM mti_terms WHERE strongs_number=?",(s,)).fetchone()
    if ex: mti_ids[base(s)]=ex['id']; continue
    cur.execute("""INSERT INTO mti_terms (strongs_number, transliteration, gloss, language, owning_word,
        status, anchor_note, extraction_date, last_changed, delete_flagged)
        VALUES (?,?,?,?,?, 'extracted_thin','gate1-psalms-2026', ?, ?, 0)""",(s,t,g,l,g,NOW,NOW))
    mti_ids[base(s)]=cur.lastrowid; reg+=1

created=0
for sp in need_record:
    mid=find_mti(sp['s'])
    if mid is None:  # should now exist; skip if still missing
        continue
    lx=lex(sp['s'])
    cur.execute("""INSERT INTO wa_verse_records
        (file_id, term_id, transliteration, testament, reference, verse_text, book_id, chapter, verse_num,
         target_word, span_strong_match, mti_term_id, morph_code, stem, verse_id, verse_span_id,
         note, analysis_marker, delete_flagged, created_at, updated_at)
        VALUES (?,?,?,?,?,?,?,?,?, ?,1,?,?,?,?,?, 'gate1-psalms-2026','gate1-psalms-2026',0,?,?)""",
        (FILE_ID, sp['s'], (lx['t'] if lx else None), 'OT', sp['ref'], sp['vt'], pb, sp['ch'], sp['vn'],
         sp['surface'], mid, sp['morph_code'], sp['stem'], sp['vid'], sp['sid'], NOW, NOW))
    created+=1

linked=0
for rec, sp in need_link:
    mid=find_mti(sp['s'])
    sets=[]; vals=[]
    if rec['verse_span_id'] is None: sets.append("verse_span_id=?"); vals.append(sp['sid'])
    if rec['mti_term_id'] is None and mid: sets.append("mti_term_id=?"); vals.append(mid)
    if sets:
        vals.append(rec['id'])
        cur.execute(f"UPDATE wa_verse_records SET {','.join(sets)} WHERE id=?", vals); linked+=1
c.commit()
print(f"\nLIVE: registered {reg} terms | created {created} verse-records | repaired {linked} links.")
