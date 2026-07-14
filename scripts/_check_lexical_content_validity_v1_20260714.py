#!/usr/bin/env python
"""CONTENT-VALIDITY gate for a re-read book (v1, 2026-07-14).

The missing gate. The readiness battery (`_check_book_lexical_readiness_v1`) checks COMPLETENESS +
INTEGRITY (is every verse read, every FK valid, every span wired) — it passes a book that is fully
read but internally INCONSISTENT. type-drift, locus-convention, DQ-01 transposition, DQ-05 tag
inconsistency all slipped through because nothing tested the VALUES. This gate does.

Three checks, each mapping to a failure the old gates missed:
  V1 value-domain     — controlled dims must hold in-vocabulary values (catches DQ-01: off-enum locus).
  V2 vocabulary drift — controlled dims must not drift with chapter position (catches type/locus drift).
  V3 tag consistency  — identical (lemma, operation) readings should not get contradictory direction tags
                        (catches DQ-05: heart/give-thanks = inward here, toward-god there).

RED = blocking; AMBER = review; GREEN = clean. Read-only.
Usage: python scripts/_check_lexical_content_validity_v1_20260714.py --book 19 [--md OUT]
"""
import sqlite3, os, sys, re, importlib.util
from collections import defaultdict, Counter

DB = os.path.join('database', 'bible_research.db')
PROV = {19: 'reread-psalms-2026', 20: 'reread-proverbs-2026'}
# controlled vocabularies (the head, before ' — ' tail)
VOCAB = {
    116: ('locus', {'internal:ib-state','external:god','external:person','external:world','none',
                    'internal:heart','internal:seat','internal:spirit','internal:mind','internal:will','internal:conscience'}),
    118: ('direction', {'toward-god','inward','outward','reciprocal','static','none'}),
    115: ('role', {'characteristic','qualifier','standalone'}),
    117: ('device', {'literal','metaphor','simile','analogy','personification','paradox','hyperbole',
                     'litotes','metonymy','irony','symbolism','typology','none'}),
}
def head(v): return re.split(r' [—-] ', (v or '').strip(), maxsplit=1)[0].strip()
def base_strong(s):
    m = re.match(r'([HG]\d+)', str(s or '')); return m.group(1) if m else None

def load_drift():
    p = os.path.join('scripts', '_check_dimension_band_drift_v1_20260714.py')
    spec = importlib.util.spec_from_file_location('drift', p); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m

def run(bid, md=None):
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    prov = PROV[bid]; L = []
    def w(s=''): L.append(s)
    bname = c.execute("SELECT name FROM books WHERE id=?", (bid,)).fetchone()[0]
    w(f"# Lexical content-validity gate — {bname}"); w()
    reds = ambers = 0

    # ---- V1 value-domain ----
    w("## V1 value-domain (controlled dims must be in-vocabulary)")
    for ve, (nm, vocab) in VOCAB.items():
        off = Counter()
        for (val,) in c.execute("SELECT value FROM ve_lexical WHERE ve_nr=? AND source_provenance=? AND delete_flagged=0", (ve, prov)):
            h = head(val)
            if h and h not in vocab: off[h] += 1
        n = sum(off.values())
        st = 'GREEN' if n == 0 else 'RED'
        if n: reds += 1
        w(f"- [{st}] **{nm}({ve})**: off-vocabulary values = {n}" + ("" if not n else f"  e.g. {dict(off.most_common(4))}"))
    w()

    # ---- V2 vocabulary drift ----
    w("## V2 vocabulary drift (controlled dims must not track reading-order)")
    drift = load_drift()
    nb = 6
    verdicts = drift.run(bid, nb, os.path.join('outputs','projections',f'{bname.lower()}_dimension_drift_report_v1_20260714.md'))
    for ve, (verdict, ev) in verdicts.items():
        if verdict != 'DRIFT-SUSPECT': continue
        # a-priori confirmed drift for type(102); others are review
        conf = (ve == 102)
        st = 'RED' if conf else 'AMBER'
        if conf: reds += 1
        else: ambers += 1
        w(f"- [{st}] **{drift.DIMS[ve]}({ve})**: {'CONFIRMED reader-drift' if conf else 'drift-suspect (review: text vs reader)'} — {ev}")
    w()

    # ---- V3 tag consistency (DQ-05 class) ----
    w("## V3 tag consistency (same lemma+operation must not get contradictory direction)")
    groups = defaultdict(lambda: Counter())
    for r in c.execute("""SELECT si.primary_strong ps, xo.value op, xd.value dir_
         FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
         JOIN ve_lexical xd ON xd.verse_span_id=si.id AND xd.ve_nr=118 AND xd.source_provenance=? AND xd.delete_flagged=0
         LEFT JOIN ve_lexical xo ON xo.verse_span_id=si.id AND xo.ve_nr=106 AND xo.source_provenance=? AND xo.delete_flagged=0
         WHERE v.book_id=? AND si.role='characteristic' AND si.role_provenance='read-2026'""", (prov, prov, bid)):
        key = (base_strong(r['ps']), head(r['op']))
        if key[0] and key[1]: groups[key][head(r['dir_'])] += 1
    conflicts = []
    for (ps, op), dirs in groups.items():
        if sum(dirs.values()) >= 4 and len(dirs) >= 2:
            top = dirs.most_common()
            minority = sum(n for _, n in top[1:])
            if minority / sum(dirs.values()) >= 0.2:   # >=20% disagree with the plurality tag
                conflicts.append((ps, op, dict(dirs)))
    conflicts.sort(key=lambda x: -sum(x[2].values()))
    st = 'GREEN' if not conflicts else 'AMBER'
    if conflicts: ambers += 1
    w(f"- [{st}] contradictory-direction groups (same lemma+operation, >=20% minority tag) = {len(conflicts)}")
    for ps, op, dirs in conflicts[:8]:
        w(f"    - {ps} / '{op[:24]}': {dirs}")
    w()

    verdict = 'FAIL (red)' if reds else ('REVIEW (amber)' if ambers else 'PASS')
    L.insert(1, f"\n**CONTENT VERDICT: {verdict}**  ·  {reds} red / {ambers} amber\n")
    text = "\n".join(L)
    print(text)
    if md:
        open(md, 'w', encoding='utf-8').write(text); print(f"\n[written] {md}")
    c.close()
    return reds, ambers

if __name__ == '__main__':
    a = sys.argv
    bid = int(a[a.index('--book')+1]) if '--book' in a and a[a.index('--book')+1].isdigit() else 19
    md = a[a.index('--md')+1] if '--md' in a else None
    run(bid, md)
