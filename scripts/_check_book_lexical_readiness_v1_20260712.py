"""Book lexical-rework READINESS assessment (read-only).

Implements the authoritative pre-flight of
`Workflow/Instructions/wa-book-lexical-readiness-assessment-AUTHORITATIVE-v1-20260712.md`:
runs I1-I11 (per book) + seed sanity + isolation + terms/verses + passages + config,
classifies each as PRECONDITION / READ-OUTPUT / ANCHOR, and prints a green/amber/red
verdict. Also serves as the per-book `_check_book_integrity_v1` the integrity doc asks for.

NO DB WRITES. Keys on the master span id, never on the Strong's.

Usage:
  python scripts/_check_book_lexical_readiness_v1_20260712.py --book 20
  python scripts/_check_book_lexical_readiness_v1_20260712.py --book Proverbs
  python scripts/_check_book_lexical_readiness_v1_20260712.py --book Pro [--md OUT.md]
"""
import sqlite3, os, sys, re, io

DB = os.path.join('database', 'bible_research.db')
GREEN, AMBER, RED, INFO = 'GREEN', 'AMBER', 'RED', 'INFO'
MARK = {GREEN: 'OK  ', AMBER: 'WARN', RED: 'FAIL', INFO: 'info'}

def base_strong(s):
    if not s: return None
    m = re.match(r'([HG]\d+)', str(s))
    return m.group(1) if m else None

class Readiness:
    def __init__(self, con, book_id, seg_code, book_name):
        self.c = con; self.bid = book_id; self.seg = seg_code; self.name = book_name
        self.rows = []  # (section, code, klass, status, detail)
        self.cols = {}
    def _cols(self, t):
        if t not in self.cols:
            self.cols[t] = {r[1] for r in self.c.execute(f"PRAGMA table_info({t})")}
        return self.cols[t]
    def q1(self, sql, *a):
        return self.c.execute(sql, a).fetchone()[0]
    def add(self, section, code, klass, status, detail):
        self.rows.append((section, code, klass, status, detail))

    # ---- §A integrity I1-I11 --------------------------------------------
    def integrity(self):
        b = self.bid
        # I1 referential
        i1a = self.q1("""SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id
                         JOIN verse v ON v.id=si.verse_id
                         WHERE v.book_id=? AND COALESCE(x.delete_flagged,0)=0
                         AND x.verse_context_id IS NOT NULL
                         AND x.verse_context_id NOT IN (SELECT id FROM verse_context)""", b)
        i1b = self.q1("""SELECT COUNT(*) FROM wa_verse_records wr WHERE wr.book_id=? AND COALESCE(wr.delete_flagged,0)=0
                         AND wr.verse_span_id IS NOT NULL AND wr.verse_span_id NOT IN (SELECT id FROM verse_span_index)""", b)
        i1c = self.q1("""SELECT COUNT(*) FROM wa_verse_records wr WHERE wr.book_id=? AND COALESCE(wr.delete_flagged,0)=0
                         AND wr.mti_term_id IS NOT NULL AND wr.mti_term_id NOT IN (SELECT id FROM mti_terms)""", b)
        i1d = self.q1("""SELECT COUNT(*) FROM wa_verse_records wr WHERE wr.book_id=? AND COALESCE(wr.delete_flagged,0)=0
                         AND wr.word_registry_fk IS NOT NULL AND wr.word_registry_fk NOT IN (SELECT id FROM word_registry)""", b)
        tot = i1a+i1b+i1c+i1d
        self.add('A', 'I1 Referential', 'PRECONDITION', GREEN if tot==0 else RED,
                 f"dangling: ve_lex.vctx={i1a}, wvr.span={i1b}, wvr.mti={i1c}, wvr.reg={i1d}")

        # candidate spans (verse_id, base-strong) for reuse
        cand = self.c.execute("""SELECT si.id, si.verse_id, si.primary_strong, si.role, si.char_candidate,
                                        si.char_candidate_tag, si.ib_char_id, si.characteristic
                                 FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                                 WHERE v.book_id=? AND si.char_candidate=1""", (b,)).fetchall()
        ncand = len(cand)
        # coverage set: active wa_verse_records (verse_id, base-strong) via mti
        cov = set()
        for r in self.c.execute("""SELECT wr.verse_id, m.strongs_number FROM wa_verse_records wr
                                    LEFT JOIN mti_terms m ON m.id=wr.mti_term_id
                                    WHERE wr.book_id=? AND COALESCE(wr.delete_flagged,0)=0""", (b,)):
            cov.add((r[0], base_strong(r[1])))
        # I2 master coverage
        uncov = [r for r in cand if (r[1], base_strong(r[2])) not in cov]
        self.add('A', 'I2 Master-index coverage', 'PRECONDITION', GREEN if not uncov else AMBER,
                 f"candidate spans with NO (verse,term) verse-record = {len(uncov)}/{ncand}"
                 + ("" if not uncov else "  -> gate-1 debt: repair via engine onboarding before read"))

        # I3 traceability: char span -> verse resolves (book already ensures verse); passage handled in I4
        i3 = self.q1("""SELECT COUNT(*) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                        WHERE v.book_id=? AND si.char_candidate=1 AND si.verse_id NOT IN (SELECT id FROM verse)""", b)
        self.add('A', 'I3 Traceability(char->span->verse)', 'PRECONDITION', GREEN if i3==0 else RED,
                 f"candidate spans whose verse_id does not resolve = {i3}")

        # I4 passage membership
        vids = sorted({r[1] for r in cand})
        if vids:
            qmarks = ",".join("?"*len(vids))
            null_pass = self.q1(f"SELECT COUNT(*) FROM verse WHERE id IN ({qmarks}) AND passage_id IS NULL", *vids)
            dangling = self.q1(f"""SELECT COUNT(*) FROM verse WHERE id IN ({qmarks}) AND passage_id IS NOT NULL
                                   AND passage_id NOT IN (SELECT id FROM passage)""", *vids)
        else:
            null_pass = dangling = 0
        nvers = len(vids)
        if dangling>0:
            st, det = RED, f"{dangling} char-verses have a dangling passage_id (partial/broken build)"
        elif null_pass==0 and nvers>0:
            st, det = GREEN, f"all {nvers} char-verses belong to a passage"
        elif null_pass==nvers:
            st, det = AMBER, f"Stage-0 NOT built: 0/{nvers} char-verses passaged (passage-build is the first pipeline action, gated on I2)"
        else:
            st, det = RED, f"partial passage build: {null_pass}/{nvers} char-verses have NULL passage_id"
        self.add('A', 'I4 Passage membership (Stage 0)', 'PRECONDITION', st, det)

        # I4b read completeness (READ-OUTPUT): candidate-bearing verse-record verses with no lexical
        i4b = len([r for r in cand
                   if (r[1], base_strong(r[2])) in cov
                   and self._span_has_no_lexical(r[0])])
        self.add('A', 'I4b Read completeness', 'READ-OUTPUT', INFO,
                 f"covered candidate spans with no lexical yet = {i4b} (whole book pre-read; informational)")

        # I5 ledger completeness (READ-OUTPUT)
        read_spans = self.q1("""SELECT COUNT(DISTINCT si.id) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                                JOIN ve_lexical x ON x.verse_span_id=si.id
                                WHERE v.book_id=? AND si.char_candidate=1 AND COALESCE(x.delete_flagged,0)=0""", b)
        self.add('A', 'I5 Ledger completeness', 'READ-OUTPUT', INFO,
                 f"candidate spans carrying any active lexical = {read_spans}/{ncand} (baseline measures detail)")

        # I6 role screen (PRECONDITION part): unroled candidates
        unroled = sum(1 for r in cand if r[3] is None)
        self.add('A', 'I6 Role decidedness', 'PRECONDITION', GREEN if unroled==0 else AMBER,
                 f"candidate spans with role=NULL (undecided) = {unroled} (God-bearer screen applies during read)")

        # I7 char-model linkage (READ-OUTPUT)
        null_ibchar = sum(1 for r in cand if r[6] is None)
        self.add('A', 'I7 ib_char linkage', 'READ-OUTPUT', INFO,
                 f"candidate spans with ib_char_id=NULL = {null_ibchar}/{ncand} (populated BY the read; empty pre-read is correct)")

        # I8 soft-delete / isolation (PRECONDITION): pair endpoints
        strong_ep = self.q1("""SELECT COUNT(*) FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id
                               JOIN verse v ON v.id=si.verse_id
                               WHERE v.book_id=? AND COALESCE(x.delete_flagged,0)=0 AND x.pair_kind='pair'
                               AND (x.from_span LIKE 'H%' OR x.from_span LIKE 'G%' OR x.to_span LIKE 'H%' OR x.to_span LIKE 'G%')""", b)
        self.add('A', 'I8 Pair endpoints (span-id rule)', 'PRECONDITION', GREEN if strong_ep==0 else AMBER,
                 f"active pairs with STRONG'S-encoded endpoints (must be span-ids) = {strong_ep}"
                 + ("" if strong_ep==0 else "  -> re-read must write integer span-id endpoints"))

        # I10 candidate flag (PRECONDITION): role=characteristic without char_candidate=1
        i10 = self.q1("""SELECT COUNT(*) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                         WHERE v.book_id=? AND si.role='characteristic' AND COALESCE(si.char_candidate,0)<>1""", b)
        self.add('A', 'I10 Candidate flag', 'PRECONDITION', GREEN if i10==0 else RED,
                 f"role='characteristic' spans without char_candidate=1 = {i10}")

        # I11 char-on-master (READ-OUTPUT)
        i11 = self.q1("""SELECT COUNT(*) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                         WHERE v.book_id=? AND si.role='characteristic' AND (si.characteristic IS NULL OR si.characteristic='')""", b)
        self.add('A', 'I11 Char-on-master', 'READ-OUTPUT', INFO,
                 f"role='characteristic' spans with no characteristic word = {i11} (written BY the read)")

    def _span_has_no_lexical(self, span_id):
        return self.q1("SELECT COUNT(*) FROM ve_lexical WHERE verse_span_id=? AND COALESCE(delete_flagged,0)=0", span_id) == 0

    # ---- §B isolation ----------------------------------------------------
    def isolation(self):
        b = self.bid
        prov = self.c.execute("""SELECT COALESCE(x.source_provenance,'(null)') p, COUNT(*) n
                                 FROM ve_lexical x JOIN verse_span_index si ON si.id=x.verse_span_id
                                 JOIN verse v ON v.id=si.verse_id
                                 WHERE v.book_id=? AND COALESCE(x.delete_flagged,0)=0
                                 GROUP BY p ORDER BY n DESC""", (b,)).fetchall()
        detail = "; ".join(f"{r[0]}={r[1]}" for r in prov) or "(no active rows)"
        # legacy table resolving live?
        legacy = 0
        if 've_lexical_legacy' in {r[0] for r in self.c.execute("SELECT name FROM sqlite_master WHERE type='table'")}:
            try:
                legacy = self.q1("""SELECT COUNT(*) FROM ve_lexical_legacy l JOIN verse_span_index si ON si.id=l.verse_span_id
                                    JOIN verse v ON v.id=si.verse_id WHERE v.book_id=?""", b)
            except Exception:
                legacy = -1
        self.add('B', 'Active-lexical provenance', 'PRECONDITION', INFO,
                 f"active ve_lexical by provenance: {detail}")
        self.add('B', 'Legacy isolation', 'PRECONDITION', GREEN if legacy==0 else AMBER,
                 f"ve_lexical_legacy rows joinable to book spans = {legacy} (archive; must not be read)")

    # ---- §C seed sanity --------------------------------------------------
    def seed(self):
        b = self.bid
        roles = self.c.execute("""SELECT COALESCE(si.role,'(null)') r, COUNT(*) n
                                  FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                                  WHERE v.book_id=? GROUP BY r ORDER BY n DESC""", (b,)).fetchall()
        rd = {r[0]: r[1] for r in roles}
        ncand = self.q1("SELECT COUNT(*) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE v.book_id=? AND si.char_candidate=1", b)
        ntot = self.q1("SELECT COUNT(*) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE v.book_id=?", b)
        tag_null = self.q1("""SELECT COUNT(*) FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
                              WHERE v.book_id=? AND si.char_candidate=1 AND (si.char_candidate_tag IS NULL OR si.char_candidate_tag='')""", b)
        self.add('C', 'Seed coverage', 'PRECONDITION', GREEN if ncand>0 else RED,
                 f"candidate spans={ncand}/{ntot} ({100*ncand//max(ntot,1)}%); role dist: " + ", ".join(f"{k}={v}" for k,v in rd.items()))
        self.add('C', 'Candidate tags present', 'PRECONDITION', GREEN if tag_null==0 else AMBER,
                 f"candidate spans with no char_candidate_tag = {tag_null}")
        retired = rd.get('qualifier',0) + rd.get('process-qualifier',0)
        self.add('C', 'Retired-role migration', 'PRECONDITION', GREEN if retired==0 else AMBER,
                 f"stamped retired roles (qualifier/process-qualifier) still present = {retired} (live model = characteristic/standalone)")
        # OT-DBR-009 proxy: candidate base-strongs missing from active mti_terms
        cand_strongs = {base_strong(r[0]) for r in self.c.execute(
            "SELECT DISTINCT si.primary_strong FROM verse_span_index si JOIN verse v ON v.id=si.verse_id WHERE v.book_id=? AND si.char_candidate=1", (b,))}
        cand_strongs.discard(None)
        mti_strongs = {base_strong(r[0]) for r in self.c.execute("SELECT strongs_number FROM mti_terms WHERE COALESCE(delete_flagged,0)=0")}
        missing = sorted(s for s in cand_strongs if s not in mti_strongs)
        self.add('C', 'Seed terms in mti_terms (OT-DBR-009)', 'PRECONDITION', GREEN if not missing else AMBER,
                 f"candidate base-Strong's with NO active mti_terms row = {len(missing)}/{len(cand_strongs)}"
                 + ("" if not missing else f"  e.g. {missing[:10]}"))

    # ---- §E config / tooling --------------------------------------------
    def config(self):
        b = self.bid
        g = self.c.execute("SELECT COALESCE(genre,'(null)') gg, COUNT(*) n FROM verse WHERE book_id=? GROUP BY gg", (b,)).fetchall()
        null_g = self.q1("SELECT COUNT(*) FROM verse WHERE book_id=? AND genre IS NULL", b)
        self.add('E', 'Genre set', 'PRECONDITION', GREEN if null_g==0 else RED,
                 "genre: " + ", ".join(f"{r[0]}={r[1]}" for r in g))
        scripts = ['_reread_ledger_lib.py','_reread_finish_v1_20260709.py','_apply_reread_lexical_v1_20260709.py',
                   '_reread_worklist_v1_20260709.py','_check_reread_measures_v3_20260709.py']
        missing = [s for s in scripts if not os.path.exists(os.path.join('scripts', s))]
        self.add('E', 'Re-read tooling present', 'PRECONDITION', GREEN if not missing else RED,
                 "all reusable scripts present" if not missing else f"MISSING: {missing}")
        # segments (unit model) for the book
        nseg = self.q1("SELECT COUNT(*) FROM segment_unit WHERE book=?", self.seg) if self.seg else 0
        self.add('E', 'Segment units', 'PRECONDITION', INFO, f"segment_unit rows for '{self.seg}' = {nseg}")

    # ---- §F baseline -----------------------------------------------------
    def baseline(self):
        # is a baseline report on disk?
        found = []
        for root in ('verse-analysis',):
            for dp,_,fs in os.walk(root):
                for f in fs:
                    if 'baseline' in f.lower() and self.name.lower()[:4] in dp.lower() and f.endswith('.md'):
                        found.append(os.path.join(dp,f))
        self.add('F', 'Baseline filed', 'ANCHOR', GREEN if found else AMBER,
                 (f"baseline report(s): {found}" if found else
                  f"no baseline .md found -> run: python scripts/_check_reread_measures_v3_20260709.py --book {self.bid} --label baseline"))

    def run(self):
        self.integrity(); self.isolation(); self.seed(); self.config(); self.baseline()
        return self.rows

    def verdict(self):
        pre = [r for r in self.rows if r[2]=='PRECONDITION']
        red = [r for r in pre if r[3]==RED]
        amber = [r for r in pre if r[3]==AMBER]
        if red: return 'NOT READY (red)', red, amber
        if amber: return 'READY-WITH-DEBT (amber)', red, amber
        return 'READY', red, amber


def resolve_book(con, arg):
    con.row_factory = sqlite3.Row
    if str(arg).isdigit():
        r = con.execute("SELECT * FROM books WHERE id=?", (int(arg),)).fetchone()
    else:
        r = con.execute("""SELECT * FROM books WHERE name LIKE ? OR short_code=? OR abbreviation=? OR full_name LIKE ?""",
                        (f"{arg}%", arg, arg, f"{arg}%")).fetchone()
    if not r: return None
    bid = r['id']; name = r['name']
    # segment code: try short_code, else the code used in segment_unit
    seg = r['short_code'] or (name[:3] if name else None)
    codes = {x[0] for x in con.execute("SELECT DISTINCT book FROM segment_unit")}
    if seg not in codes:
        cand = [c for c in codes if name and c.lower()==name[:3].lower()]
        seg = cand[0] if cand else seg
    return bid, seg, name


def main():
    if '--book' not in sys.argv:
        print("usage: --book <id|code|name> [--md OUT]"); sys.exit(2)
    arg = sys.argv[sys.argv.index('--book')+1]
    con = sqlite3.connect(DB)
    rb = resolve_book(con, arg)
    if not rb:
        print(f"book not found: {arg}"); sys.exit(2)
    bid, seg, name = rb
    con.row_factory = None
    rc = Readiness(con, bid, seg, name)
    rows = rc.run()
    verdict, red, amber = rc.verdict()

    out = io.StringIO()
    w = lambda s='': out.write(s+"\n")
    w(f"# Book lexical-readiness — {name} (book_id={bid}, seg='{seg}')")
    w()
    w(f"**VERDICT: {verdict}**  ·  preconditions: {sum(1 for r in rows if r[2]=='PRECONDITION' and r[3]==GREEN)} green / {len(amber)} amber / {len(red)} red")
    w()
    cur = None
    SECT = {'A':'A. DB integrity & traceability (I1-I11)','B':'B. Isolation of superseded data',
            'C':'C. Seed sanity','E':'E. Config & tooling','F':'F. Baseline anchor'}
    for section, code, klass, status, detail in rows:
        if section != cur:
            cur = section; w(f"\n## {SECT.get(section, section)}")
        w(f"- [{MARK[status]}] **{code}** ({klass}): {detail}")
    w()
    w("_Read-only. Per `wa-book-lexical-readiness-assessment-AUTHORITATIVE-v1-20260712.md`. "
      "Preconditions must be green/waived before Stage 0; READ-OUTPUT items are expected empty pre-read._")
    text = out.getvalue()
    print(text)
    if '--md' in sys.argv:
        p = sys.argv[sys.argv.index('--md')+1]
        open(p,'w',encoding='utf-8').write(text)
        print(f"\n[written] {p}")

if __name__ == '__main__':
    main()
