"""Read-only PIPELINE-INTEGRITY diagnostic for the verse-analysis (inner-being lexical) chain.

Traces and TRACKS POTENTIAL ISSUES across
    verse  ->  verse_morphology / verse_span_index  ->  ve_lexical  ->  segment_unit  ->  lexical_prose_chapter
plus the parallel wa_verse_records ("verse-record") store.

Per book:
  0. Lexical->verse->prose FUNNEL      - staged counts so leaks are visible.
  1. Verse-record completeness         - verses analysed but absent from wa_verse_records; orphaned/NULL-verse_id records.
  2. Span-index / morphology           - verses with no spans or no morphology (can't be lexicalised); span<->morph mismatch.
  3. Lexical completeness              - Phase-1-marked verses with ZERO ve_lexical; gate-1 terms missing a core item
                                         (sense/type/role); DIMENSIONS FALLEN BY THE WAYSIDE (per-book ve_nr coverage).
  4. Never reached prose               - Phase-1 verses whose chapter has no prose; verses in no segment_unit;
                                         prose chapters with no Phase-1 verses.

NOT a scoreboard - every section lists the ACTUAL gap rows (capped) so they can be chased.
NB: verse_span_index has no index on verse_id, so all joins are done IN PYTHON (tables loaded once) - fast + read-only.

Usage:
  python scripts/_assess_pipeline_integrity_v1_20260704.py            # 5 wisdom books -> md report
  python scripts/_assess_pipeline_integrity_v1_20260704.py --all      # every book with any Phase-1 analysis
  python scripts/_assess_pipeline_integrity_v1_20260704.py --stdout   # print instead of writing
"""
import sqlite3, os, sys, io
from collections import Counter, defaultdict
from datetime import datetime, timezone

DB = os.path.join('database', 'bible_research.db')
OUT = os.path.join('verse-analysis', '_reports', 'wa-pipeline-integrity-report-20260704.md')
WISDOM = {19: 'Psalms', 20: 'Proverbs', 21: 'Ecclesiastes', 18: 'Job', 25: 'Lamentations'}
SHORT = {19: 'Psa', 20: 'Pro', 21: 'Ecc', 18: 'Job', 25: 'Lam'}
CANON = {19: 2461, 20: 915, 21: 222, 18: 1070, 25: 154}
PROSE_TYPE = 'lexical_prose_chapter'
CAP = 25

def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; cur = conn.cursor()
    ALL = '--all' in sys.argv
    tid = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (PROSE_TYPE,)).fetchone()[0]

    # ---- book set ----
    if ALL:
        bids = [r[0] for r in cur.execute("SELECT DISTINCT book_id FROM verse WHERE process_marker IS NOT NULL ORDER BY book_id")]
        books = {}
        for b in bids:
            nm = cur.execute("SELECT name FROM books WHERE id=?", (b,)).fetchone()
            books[b] = nm[0] if nm else f"book{b}"
            SHORT.setdefault(b, (cur.execute("SELECT short_code FROM books WHERE id=?", (b,)).fetchone() or ['?'])[0])
    else:
        books = WISDOM
    bset = set(books)

    # ---- load tables ONCE (join in Python; verse_span_index is unindexed) ----
    verses = {}                          # verse_id -> row
    by_book_ch = defaultdict(set)        # (bid,ch) -> set(verse_id)
    marked = defaultdict(list)           # bid -> [verse rows], process_marker set
    for r in cur.execute("SELECT id, book_id, chapter, verse_num, reference, process_marker FROM verse"):
        if r['book_id'] not in bset: continue
        verses[r['id']] = r
        by_book_ch[(r['book_id'], r['chapter'])].add(r['id'])
        if r['process_marker'] is not None:
            marked[r['book_id']].append(r)

    span2verse = {}                      # span_id -> verse_id
    verse_spans = defaultdict(int)       # verse_id -> span count
    for sid, vid in cur.execute("SELECT id, verse_id FROM verse_span_index"):
        if vid in verses:
            span2verse[sid] = vid; verse_spans[vid] += 1

    morph_count = defaultdict(int)       # verse_id -> morph word count
    for (vid,) in cur.execute("SELECT verse_id FROM verse_morphology"):
        if vid in verses: morph_count[vid] += 1

    # ve_lexical: full scan, join to verse via span
    has_lex = defaultdict(set)           # bid -> set(verse_id)
    dim = defaultdict(Counter)           # bid -> Counter(ve_nr)
    g1 = defaultdict(set)                # bid -> set(span_id) gate-1
    lbl = defaultdict(lambda: defaultdict(set))  # bid -> span_id -> set(label)
    for r in cur.execute("SELECT verse_span_id, gate, ve_nr, ve_label, delete_flagged FROM ve_lexical"):
        if r['delete_flagged']: continue
        vid = span2verse.get(r['verse_span_id'])
        if vid is None: continue
        bid = verses[vid]['book_id']
        has_lex[bid].add(vid); dim[bid][r['ve_nr']] += 1
        if str(r['gate'] or '').startswith('1'): g1[bid].add(r['verse_span_id'])
        lbl[bid][r['verse_span_id']].add(r['ve_label'])

    # wa_verse_records verse_ids (has index ix_wvr_verse)
    vr_verses = defaultdict(set)         # bid -> set(verse_id)
    vr_orphan = defaultdict(int)
    for r in cur.execute("SELECT book_id, verse_id, delete_flagged FROM wa_verse_records"):
        if r['book_id'] not in bset or r['delete_flagged']: continue
        if r['verse_id'] is None or r['verse_id'] not in verses:
            vr_orphan[r['book_id']] += 1
        else:
            vr_verses[r['book_id']].add(r['verse_id'])

    # segment_unit_verse -> covered verse_ids per book
    unit_verses = defaultdict(set)
    for r in cur.execute("""SELECT su.book bk, suv.verse_id vid FROM segment_unit_verse suv
                            JOIN segment_unit su ON su.id=suv.unit_id AND COALESCE(su.delete_flagged,0)=0"""):
        if r['vid'] in verses: unit_verses[verses[r['vid']]['book_id']].add(r['vid'])

    # prose chapters per book
    prose_ch = defaultdict(set)
    for r in cur.execute("""SELECT json_extract(metadata_json,'$.book') bk, json_extract(metadata_json,'$.chapter') ch
                            FROM prose_section WHERE section_type_id=? AND COALESCE(delete_flagged,0)=0""", (tid,)):
        for bid in bset:
            if r['bk'] == SHORT.get(bid) and r['ch'] is not None:
                prose_ch[bid].add(int(r['ch']))

    dims = [(r['ve_nr'], r['ve_label']) for r in cur.execute("SELECT DISTINCT ve_nr, ve_label FROM ve_lexical ORDER BY ve_nr")]

    # ---- render ----
    L = []; p = L.append
    NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    p("# Pipeline-integrity diagnostic — verse-analysis chain (live from DB)"); p("")
    p(f"> Read-only trace generated {NOW} by `scripts/_assess_pipeline_integrity_v1_20260704.py`. "
      f"Scope: {'ALL Phase-1 books' if ALL else 'the 5 wisdom/poetry books'}. Tracks issues across "
      f"`verse → morphology/span-index → ve_lexical → segment_unit → {PROSE_TYPE}` + the parallel `wa_verse_records`. "
      f"**A clean line = 0.** Bold non-zero = rows to chase (examples capped at {CAP}).")
    p("")

    def refs(vids, n=CAP):
        rs = sorted((verses[v]['chapter'], verses[v]['verse_num'], verses[v]['reference']) for v in vids)
        out = [x[2] for x in rs[:n]]
        return ", ".join(out) + (f" … (+{len(rs)-n} more)" if len(rs) > n else "")

    # SECTION 0 — funnel
    p("## 0. Lexical→verse→prose funnel (per book)")
    p("`present/canon`=verse rows vs canonical · `Ph1`=process_marker set · `has_lex`=≥1 ve_lexical · "
      "`in_unit`=covered by a segment_unit (Psalms = chapter-driven, no units) · `ch_prose`=chapters with a filed reading · "
      "`v→noProse`=verses whose chapter has no reading.")
    p("")
    p("| Book | present/canon | Ph1 | has_lex | in_unit | ch_prose | v→noProse |")
    p("|---|---|---|---|---|---|---|")
    for bid, nm in books.items():
        present = sum(1 for v in verses.values() if v['book_id'] == bid)
        ph1 = len(marked[bid]); hl = len(has_lex[bid]); iu = len(unit_verses[bid])
        noprose = sum(1 for v in verses.values() if v['book_id'] == bid and v['chapter'] not in prose_ch[bid])
        iutxt = iu if iu else "— (chapter-driven)"
        p(f"| {nm} | {present}/{CANON.get(bid,'?')} | {ph1} | {hl} | {iutxt} | {len(prose_ch[bid])} | {noprose} |")
    p("")

    # SECTION 1 — verse-record completeness
    p("## 1. Verse-record completeness — `wa_verse_records`")
    p("**Verses analysed (Phase-1 marked) but absent from `wa_verse_records`** — the expected gap for STEP-*backfilled* "
      "verses (backfill writes `verse`+morphology+span-index, **not** `wa_verse_records`).")
    p("")
    p("| Book | Ph1-marked | in wa_verse_records | **analysed NOT in verse-record** | orphaned records |")
    p("|---|---|---|---|---|")
    s1 = []
    for bid, nm in books.items():
        ph1set = {r['id'] for r in marked[bid]}
        gap = ph1set - vr_verses[bid]
        p(f"| {nm} | {len(ph1set)} | {len(vr_verses[bid] & ph1set)} | **{len(gap)}** | {vr_orphan[bid]} |")
        if gap: s1.append((nm, gap))
    p("")
    for nm, gap in s1:
        p(f"- **{nm}** — {len(gap)} analysed verses not in `wa_verse_records`: {refs(gap)}")
    if not s1: p("- *(no gaps)*")
    p("")

    # SECTION 2 — span/morph
    p("## 2. Term-verse-span-index & morphology completeness")
    p("A verse with 0 spans **cannot be lexicalised**. `span≠morph` = span-index and morphology word-counts disagree.")
    p("")
    p("| Book | verses | no span-index | no morphology | span≠morph |")
    p("|---|---|---|---|---|")
    s2 = []
    for bid, nm in books.items():
        vv = [vid for vid, v in verses.items() if v['book_id'] == bid]
        nospan = [vid for vid in vv if verse_spans.get(vid, 0) == 0]
        nomorph = [vid for vid in vv if morph_count.get(vid, 0) == 0]
        mism = sum(1 for vid in vv if verse_spans.get(vid, 0) and morph_count.get(vid, 0) and verse_spans[vid] != morph_count[vid])
        p(f"| {nm} | {len(vv)} | {len(nospan)} | {len(nomorph)} | {mism} |")
        if nospan: s2.append((nm, 'no span-index', nospan))
        if nomorph: s2.append((nm, 'no morphology', nomorph))
    p("")
    for nm, kind, vids in s2:
        p(f"- **{nm}** ({kind}): {refs(vids)}")
    if not s2: p("- *(no gaps — every verse has span-index and morphology)*")
    p("")

    # SECTION 3 — lexical completeness
    p("## 3. Lexical completeness & dimensions that fell by the wayside")
    p("### 3a. Phase-1-marked verses producing ZERO `ve_lexical` (lexical silently failed)")
    p("")
    p("| Book | Ph1-marked | with ≥1 lexical | **marked but 0 lexical** |")
    p("|---|---|---|---|")
    s3a = []
    for bid, nm in books.items():
        ph1set = {r['id'] for r in marked[bid]}
        empty = ph1set - has_lex[bid]
        p(f"| {nm} | {len(ph1set)} | {len(ph1set & has_lex[bid])} | **{len(empty)}** |")
        if empty: s3a.append((nm, empty))
    p("")
    for nm, empty in s3a:
        p(f"- **{nm}** — {len(empty)} marked-but-empty: {refs(empty)}")
    if not s3a: p("- *(no gaps — every Phase-1-marked verse produced lexical rows)*")
    p("")

    p("### 3b. Dimension (ve_nr) coverage per book — thin or absent items")
    p("`·` = 0 rows. Cross-verse items (`source` D2, `effect`) are OFF by design in poetic mode → expect ~0. "
      "Dropped-by-design (**D10 valence, D12 hidden, D13 cohabitation, related_tier**) are absent programme-wide — correct. "
      "A *core* item (`sense`/`type`/`role`) going thin would be a real failure.")
    p("")
    p("| Book | " + " | ".join(f"{lab}​({nr})" for nr, lab in dims) + " |")
    p("|" + "---|" * (len(dims) + 1))
    for bid, nm in books.items():
        cells = [str(dim[bid][nr]) if dim[bid].get(nr) else "·" for nr, _ in dims]
        p(f"| {nm} | " + " | ".join(cells) + " |")
    p("")

    p("### 3c. Gate-1 tagged terms missing a CORE item (sense/type/role expected on every tagged term)")
    p("")
    p("| Book | gate-1 spans | missing sense | missing type | missing role |")
    p("|---|---|---|---|---|")
    for bid, nm in books.items():
        gg = g1[bid]; lb = lbl[bid]
        miss = lambda it: sum(1 for sp in gg if it not in lb.get(sp, ()))
        p(f"| {nm} | {len(gg)} | {miss('sense')} | {miss('type')} | {miss('role')} |")
    p("")

    # SECTION 4 — never reached prose
    p("## 4. Verses / units that never reached prose")
    p("### 4a. Phase-1 verses whose chapter has NO prose reading (broken chain)")
    p("")
    a4 = False
    for bid, nm in books.items():
        chs = sorted({v['chapter'] for r in marked[bid] for v in [r] if r['chapter'] not in prose_ch[bid]})
        if chs:
            a4 = True; p(f"- **{nm}** — Phase-1 chapters without prose: {', '.join(map(str, chs))}")
    if not a4: p("- *(none — every Phase-1 chapter has a filed reading)*")
    p("")

    p("### 4b. Verses covered by NO segment_unit (segmented books; Psalms excluded)")
    p("Expected non-zero only for intended skips (bare superscriptions, e.g. `Job 1:1`, `Ecc 1:1`). Anything else = a missed verse.")
    p("")
    b4 = False
    for bid, nm in books.items():
        if bid == 19: continue
        vv = {vid for vid, v in verses.items() if v['book_id'] == bid}
        uncov = vv - unit_verses[bid]
        if uncov:
            b4 = True; p(f"- **{nm}** — {len(uncov)} verse(s) in no unit: {refs(uncov)}")
    if not b4: p("- *(none — every verse in the segmented books is in a unit)*")
    p("")

    p("### 4c. Prose chapters with NO Phase-1 verses (reverse orphan)")
    p("")
    c4 = False
    for bid, nm in books.items():
        for ch in sorted(prose_ch[bid]):
            if not any(v['process_marker'] is not None for vid in by_book_ch.get((bid, ch), ()) for v in [verses[vid]]):
                c4 = True; p(f"- **{nm} {ch}** — prose filed but 0 Phase-1 verses")
    if not c4: p("- *(none — every filed reading rests on Phase-1 verses)*")
    p("")

    p("---")
    p(f"*Chase any **bold non-zero** above. Re-run: `python scripts/_assess_pipeline_integrity_v1_20260704.py`"
      f"{' --all' if ALL else ''}.*")

    text = "\n".join(L) + "\n"
    if '--stdout' in sys.argv:
        sys.stdout.buffer.write(text.encode('utf-8'))
    else:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        io.open(OUT, 'w', encoding='utf-8').write(text)
        print(f"wrote {OUT}  ({len(L)} lines)")

if __name__ == '__main__':
    main()
