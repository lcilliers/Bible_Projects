"""Repair STEP-missing verse-records — morphology-anchored (researcher direction 2026-07-13).

Root cause: STEP splits some Strong's across lettered sub-codes (e.g. ruach H7307 ->
H7307G/H/I; base H7307 = 0), and the old pull resolved only vocabInfos[0], silently
dropping the sibling codes' verses. The morphology master (verse_span_index) DID pick up
every variant, so the "double control" (morphology vs verse-records) exposes the gap.

Direction of travel:
  1. identify the variant(s) THROUGH THE MORPHOLOGY (the strong's codes on the master
     spans for this book);
  2. do a FULL STEP pull for the strong across all those variants (with morphology);
  3. diff the full pull against what the DB already has -> the previously-missed verses;
  4. bring those verses through (build the records) — via audit_word (separate apply step).

This script does steps 1-3 (DRY, read-only) and reports the recoverable vs genuine-STEP-gap
split per term. Bringing-through (step 4) is a separate audit_word-fed apply.

Usage:
  python scripts/_repair_step_missing_verses_v1_20260713.py --book 20 --strongs H7307,H6424,H3001,H7999
  python scripts/_repair_step_missing_verses_v1_20260713.py --book 20 --candidates   # all uncovered candidate strongs
"""
import sys, os, re, argparse, sqlite3
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analytics'))
from step_client import StepClient

DB = os.path.join('database', 'bible_research.db')
SUFFIXES = [''] + list('ABCDEFGHIJKL')
BOOKCODE = {20: 'Prov'}  # osis book code per book_id (extend as needed)


def numeric_base(s):
    m = re.match(r'([HG]\d+)', s or '')
    return m.group(1) if m else None


def osis_to_ref(osis, osis_book, book_disp):
    # 'Prov.17.22' -> 'Pro 17:22' ONLY for the target book; else None (filter cross-book).
    parts = osis.split('.')
    if len(parts) != 3 or parts[0] != osis_book:
        return None
    return f"{book_disp} {int(parts[1])}:{int(parts[2])}"


def master_variants_and_verses(conn, book_id, base):
    """Morphology: the STEP variant codes + candidate verses this strong uses in the book."""
    rows = conn.execute(
        """SELECT si.reference, si.strongs, si.primary_strong
           FROM verse_span_index si JOIN verse v ON v.id = si.verse_id
           WHERE v.book_id = ? AND si.char_candidate = 1 AND si.primary_strong LIKE ?""",
        (book_id, base + '%')).fetchall()
    variants = set()
    verses = set()
    for r in rows:
        verses.add(r['reference'])
        # strongs field may hold the exact tagged variant (e.g. 'H7307G H9002')
        for tok in (r['strongs'] or '').split():
            if numeric_base(tok) == base:
                variants.add(tok)
    return variants, verses


def step_variant_codes(sc, base):
    """All STEP lettered variants of the base that carry verses (probe; base often 0)."""
    codes = []
    for suf in SUFFIXES:
        code = base + suf
        try:
            if sc._search_range(code).get('total', 0) > 0:
                codes.append(code)
        except Exception:
            pass
    return codes


def full_pull_refs(sc, codes, osis_book, book_disp):
    """Union _paginate_all across the variant codes; return {ref: osisId} for the target book only."""
    refs = {}
    for code in codes:
        for rec in sc._paginate_all(sc._search_range, code):
            osis = rec.get('osisId') or ''
            r = osis_to_ref(osis, osis_book, book_disp)
            if r:
                refs[r] = osis
    return refs


def db_covered_verses(conn, book_id, base):
    covered = set()
    for r in conn.execute(
        """SELECT DISTINCT wr.reference FROM wa_verse_records wr
           WHERE wr.book_id = ? AND COALESCE(wr.delete_flagged,0)=0 AND wr.term_id LIKE ?""",
        (book_id, base + '%')):
        covered.add(r[0])
    return covered


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book', type=int, required=True)
    ap.add_argument('--strongs')
    ap.add_argument('--candidates', action='store_true')
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    book_disp = 'Pro'  # verse_span_index.reference style for Proverbs
    book_code = BOOKCODE.get(a.book, '?')

    if a.strongs:
        strongs = [numeric_base(s) for s in a.strongs.split(',')]
    else:  # all uncovered candidate strongs in the book
        strongs = sorted({numeric_base(r['primary_strong']) for r in conn.execute(
            """SELECT DISTINCT si.primary_strong FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
               WHERE v.book_id=? AND si.char_candidate=1""", (a.book,))})

    sc = StepClient()
    print(f"book={a.book} ({book_code})  strongs={strongs}\n")
    grand = {'recoverable': 0, 'genuine_gap': 0, 'already': 0}
    for base in strongs:
        mvar, mverses = master_variants_and_verses(conn, a.book, base)
        if not mverses:
            continue
        covered = db_covered_verses(conn, a.book, base)
        missing = sorted(v for v in mverses if v not in covered)
        if not missing:
            grand['already'] += len(mverses)
            print(f"{base}: {len(mverses)} candidate verses, all covered.")
            continue
        # full STEP pull across variants (prefer morphology's variants; else probe)
        codes = sorted(mvar) or step_variant_codes(sc, base)
        step_refs = full_pull_refs(sc, codes, book_code, book_disp)
        recoverable = [v for v in missing if v in step_refs]
        genuine_gap = [v for v in missing if v not in step_refs]
        grand['recoverable'] += len(recoverable)
        grand['genuine_gap'] += len(genuine_gap)
        print(f"{base}: morph-variants={sorted(mvar)} | candidate_verses={len(mverses)} "
              f"missing={len(missing)}")
        print(f"    STEP full-pull variants={codes} -> {len(step_refs)} {book_code} verses")
        print(f"    RECOVERABLE (in STEP, bring through)={len(recoverable)} {recoverable}")
        if genuine_gap:
            print(f"    GENUINE STEP GAP (not in STEP under any variant)={len(genuine_gap)} {genuine_gap}")
    print(f"\nTOTAL: recoverable={grand['recoverable']} genuine_gap={grand['genuine_gap']} already_covered={grand['already']}")


if __name__ == '__main__':
    main()
