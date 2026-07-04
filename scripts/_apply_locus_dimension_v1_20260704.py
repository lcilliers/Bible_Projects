"""Derive a LOCUS dimension (ve_nr 116) on target/bearer spans: IB-internal vs external.

Restores the queryable IB<->outside boundary lost when cross-verse source/effect were
turned off for poetic (see wa-integrity-implications-20260704.md §3b, "backfill A").
MECHANICAL derivation from morphology + lemma tables - no re-reading. Additive + idempotent
(soft-deletes prior locus rows of this provenance, re-inserts). Does NOT touch existing lexical.

Classifies the entity a target(107)/bearer(105) row points at, by its Strong's + morph:
  external:god        - deity lemmas
  external:adversary  - enemy/foe/adversary lemmas
  external:proper     - a proper noun (person/place) that is not deity
  internal:seat       - heart/soul/spirit/flesh/kidneys/inward-parts
  internal:ib-state   - a Strong's that is itself a study (gate-1) term = an inner-being state
  internal:body       - a body-part (eye/hand/mouth/tongue/foot/lips/face/ear)
  external:thing      - default: a concrete common noun, none of the above
Answers, once populated: "which characteristics act on something OUTSIDE the self"
(IB->external target) and "whose characteristic is this" (bearer locus). The reverse
(external->IB inducement) is NOT recoverable mechanically - that is backfill B (a re-read).

Usage:
  python scripts/_apply_locus_dimension_v1_20260704.py            # dry-run: classification report
  python scripts/_apply_locus_dimension_v1_20260704.py --live
  python scripts/_apply_locus_dimension_v1_20260704.py --sample   # print a read-back sample
"""
import sqlite3, os, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

DB = os.path.join('database', 'bible_research.db')
PROV = 'locus-derivation-v1-20260704'
WISDOM = (18, 19, 20, 21, 25)

DEITY = {'H0430','H3068','H0410','H0433','H5945','H7706','H0136','H3050','H3069','H0113'}
ADVERSARY = {'H0341','H6862','H6887','H7854','H6145'}
SEAT = {'H3820','H3824','H5315','H7307','H5397','H1320','H3629','H4578','H7130','H2436'}
BODY = {'H5869','H3027','H6310','H3956','H7272','H8193','H6440','H0241','H7218','H3409','H6106','H7785'}

def canon(s):
    s = (str(s) if s is not None else '').strip().upper()
    if not s: return ''
    if s.startswith('H') and s[1:].isdigit():
        return 'H' + s[1:].zfill(4)
    return s

def main():
    LIVE = '--live' in sys.argv
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; cur = conn.cursor()

    # study-term Strong's = any Strong's ever tagged gate-1 (a primary inner-being term)
    ib_terms = set()
    for r in cur.execute("SELECT DISTINCT primary_strong FROM verse_span_index s "
                         "JOIN ve_lexical l ON l.verse_span_id=s.id "
                         "WHERE l.gate LIKE '1%' AND COALESCE(l.delete_flagged,0)=0"):
        if r[0]: ib_terms.add(canon(r[0]))

    # span metadata: id -> (primary_strong, morph_code, surface, verse_id, book_id)
    span = {}
    for r in cur.execute("SELECT s.id, s.primary_strong ps, s.morph_code mc, s.surface surf, s.verse_id vid, v.book_id bk "
                         "FROM verse_span_index s JOIN verse v ON s.verse_id=v.id WHERE v.book_id IN (18,19,20,21,25)"):
        span[r['id']] = r
    # strong -> is-proper-noun? (from any span whose morph marks a proper noun)
    proper = set()
    for r in span.values():
        mc = (r['mc'] or '')
        # Hebrew proper-noun morph tags contain 'Np' (ETCBC/OSHB style) or an 'N' with proper flag
        if 'Np' in mc or ',np' in mc.lower():
            if r['ps']: proper.add(canon(r['ps']))

    def classify(strong, surface):
        st = canon(strong); sl = (surface or '').lower()
        if st in DEITY or sl in ('god','lord','almighty','most high'): return 'external:god'
        if st in ADVERSARY: return 'external:adversary'
        if st in SEAT: return 'internal:seat'
        if st in BODY: return 'internal:body'
        if st in ib_terms: return 'internal:ib-state'
        if st in proper: return 'external:proper'
        return 'external:thing'

    # target(107): entity = to_span (a Strong's).  bearer(105): entity = the span's own primary_strong.
    todo = []   # (ve_lexical_id, verse_span_id, gate, role, entity_strong, entity_surface)
    for r in cur.execute("SELECT id, verse_span_id vsi, gate, ve_nr, ve_label, value, from_span, to_span "
                         "FROM ve_lexical l WHERE ve_nr IN (105,107) AND COALESCE(delete_flagged,0)=0 "
                         "AND verse_span_id IN (SELECT s.id FROM verse_span_index s JOIN verse v ON s.verse_id=v.id WHERE v.book_id IN (18,19,20,21,25))"):
        if r['ve_nr'] == 107:
            ent = r['to_span']; sp = span.get(r['vsi']); surf = None
        else:
            sp = span.get(r['vsi']); ent = sp['ps'] if sp else None; surf = sp['surf'] if sp else None
        todo.append((r['id'], r['vsi'], r['gate'], r['ve_label'], ent, surf or r['value']))

    dist = Counter(); by_role = defaultdict(Counter)
    rows_out = []
    for lid, vsi, gate, role, ent, surf in todo:
        loc = classify(ent, surf)
        dist[loc] += 1; by_role[role][loc] += 1
        rows_out.append((vsi, gate, loc, ent))

    print(f"study-term (gate-1) Strong's in inventory: {len(ib_terms)} · proper-noun lemmas detected: {len(proper)}")
    print(f"target/bearer spans to classify (5 books): {len(todo)}")
    print("locus distribution:")
    for k, n in dist.most_common(): print(f"   {k:20} {n}")
    print("by role:")
    for role, c in by_role.items():
        print(f"   {role}: " + " · ".join(f"{k.split(':')[1]}={v}" for k, v in c.most_common()))

    if not LIVE:
        print("DRY-RUN. Re-run with --live.")
        return

    NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    cur.execute("UPDATE ve_lexical SET delete_flagged=1 WHERE ve_nr=116 AND source_provenance=?", (PROV,))
    ins = 0
    for vsi, gate, loc, ent in rows_out:
        cur.execute("""INSERT INTO ve_lexical (verse_span_id, gate, ve_nr, ve_label, value, source_provenance, delete_flagged, created_at)
                       VALUES (?,?,?,?,?,?,0,?)""", (vsi, gate, 116, 'locus', loc, PROV, NOW))
        ins += 1
    conn.commit()
    print(f"inserted {ins} locus rows (ve_nr 116, provenance {PROV}). committed.")

if __name__ == '__main__':
    main()
