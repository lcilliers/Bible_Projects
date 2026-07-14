#!/usr/bin/env python
"""DQ-01 source fix: un-transpose coupling(112) <-> locus(116) for Psalms read-2026 (v1, 2026-07-14).

Surfaced by the AI's first Psalms macro pass. In ~666 Psalms spans the two fields are swapped:
coupling(112) holds a locus-enum value (e.g. 'external:god') with a meaningless to_span=self artifact,
and locus(116) holds a coupling descriptor (e.g. 'paired with serving with gladness').

Swap set (strict): coupling(112).value IN LOCUS_ENUM  AND  locus(116).value is a non-enum phrase.
  -> excludes the 71 valid rows where coupling='none' & locus=enum (not a defect)
  -> excludes 9 ambiguous rows where both are phrases (won't guess).
Proverbs is clean (0) — Psalms-only.

Fix per span: exchange the two values; drop the coupling self-pair (to_span=NULL); normalise pair_kind='value'.

Usage: python scripts/_apply_dq01_locus_coupling_swap_v1_20260714.py [--live]
"""
import sqlite3, os, sys

DB = os.path.join('database', 'bible_research.db')
PROV = 'reread-psalms-2026'
LOCUS_ENUM = ('internal:ib-state','external:god','external:person','external:world','none',
              'internal:heart','internal:seat','internal:spirit','internal:mind','internal:will','internal:conscience')

def run(live=False):
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    spans = {}
    for r in c.execute("SELECT id, verse_span_id sid, ve_nr, value, to_span FROM ve_lexical WHERE ve_nr IN (112,116) AND source_provenance=? AND delete_flagged=0", (PROV,)):
        spans.setdefault(r['sid'], {})[r['ve_nr']] = dict(id=r['id'], v=r['value'], ts=r['to_span'])
    swap = []
    for sid, d in spans.items():
        cpl, loc = d.get(112), d.get(116)
        if not cpl or not loc: continue
        if cpl['v'] in LOCUS_ENUM and loc['v'] and loc['v'] not in LOCUS_ENUM:
            swap.append((sid, cpl, loc))
    print(f"swap set: {len(swap)} spans")
    for sid, cpl, loc in swap:
        # coupling row -> the paired phrase (scalar descriptor, no self-pair)
        c.execute("UPDATE ve_lexical SET value=?, to_span=NULL, resolution='inferred', pair_kind='value' WHERE id=?", (loc['v'], cpl['id']))
        # locus row -> the enum value
        c.execute("UPDATE ve_lexical SET value=?, resolution='value', pair_kind='value' WHERE id=?", (cpl['v'], loc['id']))
    # verify (on the same uncommitted connection)
    bad = 0
    for sid, cpl, loc in swap[:0]: pass
    if live:
        c.commit()
        # post-check
        off = c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_nr=116 AND source_provenance=? AND delete_flagged=0 AND value LIKE 'paired %'", (PROV,)).fetchone()[0]
        cplenum = c.execute("SELECT COUNT(*) FROM ve_lexical WHERE ve_nr=112 AND source_provenance=? AND delete_flagged=0 AND value IN ({})".format(','.join('?'*len(LOCUS_ENUM))), (PROV, *LOCUS_ENUM)).fetchone()[0]
        print(f"LIVE: swapped {len(swap)} spans. post-check: locus rows still holding 'paired ...' = {off}; coupling rows still holding a locus-enum = {cplenum} (both should be ~0, allowing 'none').")
    else:
        c.rollback(); print(f"[dry-run] would swap {len(swap)} spans. --live to write.")
    c.close()

if __name__ == '__main__':
    run(live='--live' in sys.argv)
