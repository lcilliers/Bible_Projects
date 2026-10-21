#!/usr/bin/env python
"""_apply_psalms_gate1_reactivate_v1_20260706.py — finish Step (d) for Psalms.

Two residual gaps after the main gate-1 completion:
 A) 16 characteristic strongs (prayer H8605, wisdom H2451, to-pray H6419, ...) had ONLY delete-flagged
    mti_terms rows — no active term. The gate1 verse-records were linked to a delete-flagged row.
    FIX: reactivate exactly the row each gate1 record references (status='extracted_thin',
    delete_flagged=0, anchor_note='gate1-psalms-2026-reactivated'). Since no active row existed for these
    strongs, this yields exactly ONE active term each (no active-duplicate created).
 B) H6199 (Psa 102:17 'destitute') had no lexicon gloss so was skipped. Register it (gloss='destitute',
    from surface/context) and create its verse-record.
Reversible (marked). Read-only unless --live.
"""
import sqlite3, os, sys, re
DB=os.path.join('database','bible_research.db'); LIVE='--live' in sys.argv; NOW='2026-07-06T00:00:00Z'
c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; cur=c.cursor()
def base(s): m=re.match(r'(H\d+)', s or ''); return m.group(1) if m else (s or '')
pb=cur.execute("SELECT id FROM books WHERE name='Psalms'").fetchone()['id']

# A) reactivate delete-flagged mti rows referenced by gate1 records
bad=cur.execute("""SELECT DISTINCT w.mti_term_id id, m.strongs_number s
  FROM wa_verse_records w JOIN mti_terms m ON m.id=w.mti_term_id
  WHERE w.note='gate1-psalms-2026'
    AND (m.status IN ('delete','excluded','candidate_delete') OR COALESCE(m.delete_flagged,0)=1)""").fetchall()
print(f"A) mti rows to reactivate: {len(bad)} -> {[r['s'] for r in bad]}")

# B) H6199 span + record
h6=cur.execute("""SELECT vsi.id sid, vsi.verse_id vid, vsi.surface, vsi.morph_code, vsi.stem,
    v.reference ref, v.verse_text vt, v.chapter ch, v.verse_num vn
  FROM ve_lexical vl JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id JOIN verse v ON v.id=vsi.verse_id
  WHERE vl.ve_nr=115 AND vl.value='characteristic' AND vl.source_provenance='role-reassess-2026'
    AND substr(vsi.primary_strong,1,5)='H6199'""").fetchone()
print(f"B) H6199 span: {h6['ref'] if h6 else None}")

if not LIVE:
    print("\nDRY-RUN. Re-run with --live."); sys.exit(0)

for r in bad:
    cur.execute("""UPDATE mti_terms SET status='extracted_thin', delete_flagged=0,
        anchor_note='gate1-psalms-2026-reactivated', last_changed=? WHERE id=?""",(NOW,r['id']))

FILE_ID=cur.execute("SELECT id FROM wa_file_index WHERE registry_id='GATE1-PSALMS-2026'").fetchone()['id']
# register H6199 if no active row
act=cur.execute("SELECT id FROM mti_terms WHERE strongs_number='H6199' AND COALESCE(delete_flagged,0)=0").fetchone()
if act: mid=act['id']
else:
    cur.execute("""INSERT INTO mti_terms (strongs_number, transliteration, gloss, language, owning_word,
        status, anchor_note, extraction_date, last_changed, delete_flagged)
        VALUES ('H6199','ar.ar','destitute','Hebrew','destitute','extracted_thin','gate1-psalms-2026',?,?,0)""",(NOW,NOW))
    mid=cur.lastrowid
# create H6199 verse-record if missing
ex=cur.execute("SELECT id FROM wa_verse_records WHERE verse_id=? AND term_id='H6199' AND COALESCE(delete_flagged,0)=0",(h6['vid'],)).fetchone()
if not ex:
    cur.execute("""INSERT INTO wa_verse_records
        (file_id, term_id, transliteration, testament, reference, verse_text, book_id, chapter, verse_num,
         target_word, span_strong_match, mti_term_id, morph_code, stem, verse_id, verse_span_id,
         note, analysis_marker, delete_flagged, created_at, updated_at)
        VALUES (?,?,?,?,?,?,?,?,?, ?,1,?,?,?,?,?, 'gate1-psalms-2026','gate1-psalms-2026',0,?,?)""",
        (FILE_ID,'H6199','ar.ar','OT',h6['ref'],h6['vt'],pb,h6['ch'],h6['vn'],
         h6['surface'],mid,h6['morph_code'],h6['stem'],h6['vid'],h6['sid'],NOW,NOW))
c.commit()
print(f"\nLIVE: reactivated {len(bad)} terms; H6199 registered + verse-record created.")
