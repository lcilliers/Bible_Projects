#!/usr/bin/env python
"""_probe_psalms_gate1_validate_v1_20260706.py — Step (e) full-integrity validation (read-only)."""
import sqlite3, os, re
c=sqlite3.connect(os.path.join('database','bible_research.db')); c.row_factory=sqlite3.Row; cur=c.cursor()
def base(s): m=re.match(r'(H\d+)', s or ''); return m.group(1) if m else (s or '')
pb=cur.execute("SELECT id FROM books WHERE name='Psalms'").fetchone()['id']
ok=True
def chk(label, n, want0=True):
    global ok; flag='OK' if (n==0)==want0 else 'FAIL'
    if flag=='FAIL': ok=False
    print(f"  [{flag}] {label}: {n}")

print("== gate1 verse-records integrity ==")
chk("gate1 records with unresolved verse_id", cur.execute("SELECT COUNT(*) FROM wa_verse_records w WHERE w.note='gate1-psalms-2026' AND NOT EXISTS(SELECT 1 FROM verse v WHERE v.id=w.verse_id)").fetchone()[0])
chk("gate1 records with unresolved verse_span_id", cur.execute("SELECT COUNT(*) FROM wa_verse_records w WHERE w.note='gate1-psalms-2026' AND NOT EXISTS(SELECT 1 FROM verse_span_index s WHERE s.id=w.verse_span_id)").fetchone()[0])
chk("gate1 records with unresolved mti_term_id", cur.execute("SELECT COUNT(*) FROM wa_verse_records w WHERE w.note='gate1-psalms-2026' AND NOT EXISTS(SELECT 1 FROM mti_terms m WHERE m.id=w.mti_term_id)").fetchone()[0])
chk("gate1 records with NULL verse_text", cur.execute("SELECT COUNT(*) FROM wa_verse_records WHERE note='gate1-psalms-2026' AND (verse_text IS NULL OR verse_text='')").fetchone()[0])
chk("gate1 records linked to delete-flagged term", cur.execute("SELECT COUNT(*) FROM wa_verse_records w JOIN mti_terms m ON m.id=w.mti_term_id WHERE w.note='gate1-psalms-2026' AND (m.status IN('delete','excluded','candidate_delete') OR COALESCE(m.delete_flagged,0)=1)").fetchone()[0])

print("== active-duplicate check on reactivated/registered terms ==")
dups=cur.execute("""SELECT strongs_number, COUNT(*) n FROM mti_terms
  WHERE COALESCE(delete_flagged,0)=0 AND COALESCE(status,'') NOT IN('delete','excluded','candidate_delete')
    AND anchor_note LIKE 'gate1-psalms-2026%' GROUP BY strongs_number HAVING COUNT(*)>1""").fetchall()
chk("gate1 terms with >1 active row (duplicate)", len(dups))

print("== whole-chain (all Psalms characteristic spans) ==")
# every characteristic span resolves forward span->verse-record->term and back
gap=cur.execute("""SELECT COUNT(*) FROM ve_lexical vl
  JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id JOIN verse v ON v.id=vsi.verse_id
  WHERE v.book_id=? AND vl.ve_nr=115 AND vl.value='characteristic' AND vl.source_provenance='role-reassess-2026'
    AND COALESCE(vl.delete_flagged,0)=0
    AND NOT EXISTS(SELECT 1 FROM wa_verse_records w WHERE w.verse_id=vsi.verse_id AND base_strong(w.term_id)=substr(vsi.primary_strong,1,5))""",(pb,)).fetchone()[0] if False else None
# (sqlite has no base_strong fn) do it in python
spans=cur.execute("""SELECT vsi.verse_id vid, substr(vsi.primary_strong,1,5) s FROM ve_lexical vl
  JOIN verse_span_index vsi ON vsi.id=vl.verse_span_id JOIN verse v ON v.id=vsi.verse_id
  WHERE v.book_id=? AND vl.ve_nr=115 AND vl.value='characteristic' AND vl.source_provenance='role-reassess-2026'
    AND COALESCE(vl.delete_flagged,0)=0""",(pb,)).fetchall()
have=set()
for r in cur.execute("SELECT verse_id, term_id FROM wa_verse_records WHERE book_id=? AND COALESCE(delete_flagged,0)=0",(pb,)):
    have.add((r['verse_id'], base(r['term_id'])))
miss=sum(1 for sp in spans if (sp['vid'], base(sp['s'])) not in have)
chk("characteristic spans with no verse-record (forward)", miss)

print("\nRESULT:", "ALL PASS ✓" if ok else "FAILURES PRESENT ✗")
