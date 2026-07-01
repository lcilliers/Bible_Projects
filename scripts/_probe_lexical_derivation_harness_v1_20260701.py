"""
_probe_lexical_derivation_harness_v1_20260701.py  (READ-ONLY validation harness)

Round-2 rework of the lexical-item derivation RULES, structured for clarity + efficiency.

Architecture (per researcher direction 2026-07-01):
  * READ ONCE, USE MANY — one batch query each for spans / terms / lexicon / sense over ALL
    test verses; everything after is in-memory. No re-scan of the same data.
  * BUILD ON EACH OTHER — morphology is parsed once into per-span features; item rules run in
    dependency order and read earlier results (sense -> type -> operation -> seat -> target -> ...).
  * ONE FUNCTION PER ITEM — each rule is a small function returning (value, resolution, basis),
    so a rule can be revised in isolation across rounds.

This does NOT write to the DB. It prints the derivation so the rules can be verified against the
text before any build (OQ5). Rules are v1 of an expected several rounds; each is marked RULE / TODO.

Usage: python scripts/_probe_lexical_derivation_harness_v1_20260701.py
"""
import sqlite3, os, re, collections

DB = os.path.join('database', 'bible_research.db')
TEST_REFS = ['Exo 1:13', 'Gen 6:5', 'Lev 25:43', 'Psa 34:4']

# canonical constitutional-seat lemmas (zero-padded)
SEATS = {'H3820':'heart','H3824':'heart','H5315':'soul','H7307':'spirit',
         'H1320':'flesh','H3629':'kidneys','H4578':'inward parts','H7130':'inward parts'}
CAUSAL_PARTICLES = {'H3588':'ki (that/because)'}   # Hebrew ki
PREP_MANNER = ('be','ke')  # be- (with/in), ke- (as) mark adverbial manner on a noun

# ---------- 1. MORPH PARSE (once per span) ----------
def parse_morph(morph_code, pos):
    """Parse the first morph segment into the few features the rules need. Cheap, deterministic."""
    segs = (morph_code or '').split()
    head = segs[0] if segs else ''
    feats = {'is_verb': pos == 'verb', 'is_noun': pos == 'noun', 'is_adj': pos == 'adjective',
             'state': None, 'has_prep': False, 'has_suffix': False, 'has_article': False}
    # noun state: last char of a HN.... head is 'c' (construct) or 'a' (absolute)
    if head.startswith('HN') and head[-1] in ('c', 'a'):
        feats['state'] = 'construct' if head[-1] == 'c' else 'absolute'
    # any segment that is a preposition (HR / HRd) or article (HTd) or suffix (HS..)
    for s in segs:
        if s.startswith('HR'): feats['has_prep'] = True
        if s.startswith('HS'): feats['has_suffix'] = True
        if s.startswith('HT') and s.endswith('d'): feats['has_article'] = True
    return feats

def canon(s):
    m = re.match(r'^([HG])(\d+)', s or ''); return m.group(1)+m.group(2).zfill(4) if m else s

# ---------- 2. LOAD (read once, use many) ----------
class Corpus:
    def __init__(self, conn, refs):
        conn.row_factory = sqlite3.Row; cur = conn.cursor()
        vrows = cur.execute("SELECT id,reference,verse_text FROM verse WHERE reference IN (%s)"
                            % ','.join('?'*len(refs)), refs).fetchall()
        self.vid = {r['reference']: r['id'] for r in vrows}
        self.text = {r['id']: r['verse_text'] for r in vrows}
        vids = list(self.vid.values()); ph = ','.join('?'*len(vids))
        # spans (one scan)
        self.spans = collections.defaultdict(list)
        for m in cur.execute("SELECT verse_id,word_index,surface,primary_strong,pos,morph_code,stem "
                             "FROM verse_morphology WHERE verse_id IN (%s) ORDER BY verse_id,word_index" % ph, vids):
            d = dict(m); d['strong'] = canon(m['primary_strong']); d['feat'] = parse_morph(m['morph_code'], m['pos'])
            self.spans[m['verse_id']].append(d)
        # tagged terms (one scan) — join to mti for cluster + owning word
        self.terms = collections.defaultdict(list)
        for t in cur.execute("""SELECT w.verse_id, w.term_id, w.mti_term_id, w.target_word, mt.owning_word, mt.cluster_code
            FROM wa_verse_records w LEFT JOIN mti_terms mt ON w.mti_term_id=mt.id
            WHERE w.verse_id IN (%s) AND COALESCE(w.delete_flagged,0)=0""" % ph, vids):
            self.terms[t['verse_id']].append(dict(t))

# ---------- 3. RULES (one per item; build on each other) ----------
# Each takes (verse spans, the term's span index) and returns (value, resolution, basis).
def span_of_term(spans, term):
    cs = canon(term['term_id'])
    for i, s in enumerate(spans):
        if s['strong'] == cs: return i
    return None

def r_sense(spans, i, term):
    return term.get('target_word') or spans[i]['surface'], 'span', 'target_word'

def r_type(spans, i, term):
    f = spans[i]['feat']
    v = 'action' if f['is_verb'] else 'status' if f['is_noun'] else 'quality' if f['is_adj'] else 'UNRESOLVED'
    return v, 'span', 'POS=%s' % spans[i]['pos']

def r_operation(spans, i, term):
    # RULE: the governing predicate = the nearest finite VERB in the verse (v1: nearest by index).
    verbs = [j for j,s in enumerate(spans) if s['feat']['is_verb']]
    if not verbs: return None, 'none', 'no verb in verse'
    j = min(verbs, key=lambda j: abs(j-i))
    return '%s (%s)' % (spans[j]['surface'], spans[j]['strong']), 'span', 'nearest finite verb @w%d' % j

def r_seat(spans, i, term):
    # RULE (reworked): a seat attaches to THIS term only via a construct chain, not verse-wide.
    #   if this term is construct-state and a seat noun follows within 2 words -> that seat;
    #   or if this term IS a seat lemma -> itself. Otherwise NONE (do NOT smear).
    if spans[i]['strong'] in SEATS: return SEATS[spans[i]['strong']], 'span', 'term IS the seat'
    if spans[i]['feat']['state'] == 'construct':
        for j in range(i+1, min(i+3, len(spans))):
            if spans[j]['strong'] in SEATS:
                return SEATS[spans[j]['strong']], 'span', 'construct chain -> seat @w%d' % j
    return None, 'none', 'no construct link to a seat'

def r_target(spans, i, term):
    # RULE: for a verb-term, the object = the next noun/proper after the verb (v1: first noun to the right).
    if not spans[i]['feat']['is_verb']: return None, 'none', 'term not a verb (object via governing verb only)'
    for j in range(i+1, len(spans)):
        if spans[j]['feat']['is_noun']:
            return '%s (%s)' % (spans[j]['surface'], spans[j]['strong']), 'span', 'object noun @w%d' % j
    return None, 'none', 'no object noun to the right'

def r_manner(spans, i, term):
    # RULE (reworked — fixes D6): a NOUN term carrying a preposition (be-/ke-) is adverbial MANNER
    #   on the governing verb. This captures be-perek "ruthlessly" as the manner of the verb.
    if spans[i]['feat']['is_noun'] and spans[i]['feat']['has_prep']:
        verbs = [j for j,s in enumerate(spans) if s['feat']['is_verb']]
        if verbs:
            j = min(verbs, key=lambda j: abs(j-i))
            return 'manner-of: %s (%s)' % (spans[j]['surface'], spans[j]['strong']), 'span', 'prep-marked noun -> manner of verb @w%d' % j
    return None, 'none', 'no preposition-marked adverbial'

def r_source(spans, i, term):
    # RULE (reworked — fixes wrong-direction): assign a source ONLY when a causal particle (ki) is present.
    #   Otherwise NONE — never guess (this removes the false from-source=God / from-source=fears).
    for j,s in enumerate(spans):
        if s['strong'] in CAUSAL_PARTICLES:
            return 'causal-clause @w%d (%s)' % (j, CAUSAL_PARTICLES[s['strong']]), 'span', 'causal particle present'
    return None, 'none', 'no causal particle -> source not stated'

def r_coupling(spans, i, term, verse_terms):
    # RULE (reworked — fixes D9 explosion): ONLY the morphological weld, not every co-term.
    #   the weld = the manner-binding (this term is prep-marked adverbial on a verb that is ALSO a term),
    #   or a construct link to another TAGGED term. Loose co-occurrence is the multi-term web, not D9.
    term_strongs = {canon(t['term_id']): t for t in verse_terms}
    # manner weld: prep-marked noun -> the verb it modifies, if that verb is a tagged term
    if spans[i]['feat']['is_noun'] and spans[i]['feat']['has_prep']:
        for j,s in enumerate(spans):
            if s['feat']['is_verb'] and s['strong'] in term_strongs:
                return 'welds %s (%s) as its manner' % (spans[j]['surface'], s['strong']), 'span', 'prep-manner weld to a co-term verb'
    # construct weld to a tagged term
    if spans[i]['feat']['state'] == 'construct':
        for j in range(i+1, min(i+3, len(spans))):
            if spans[j]['strong'] in term_strongs:
                return 'construct-bound to %s (%s)' % (spans[j]['surface'], spans[j]['strong']), 'span', 'construct weld to a co-term'
    return None, 'none', 'no grammatical weld (loose co-occurrence = multi-term web, not D9)'

# ---------- 4. RUN ----------
def main():
    conn = sqlite3.connect(DB)
    C = Corpus(conn, TEST_REFS)
    for ref in TEST_REFS:
        vid = C.vid.get(ref)
        if not vid: print('\n### %s not in verse index' % ref); continue
        spans = C.spans[vid]; terms = C.terms[vid]
        print('\n' + '='*70)
        print('%s  —  %s' % (ref, (C.text[vid] or '')[:110]))
        print('spans: ' + ' | '.join('%d:%s(%s%s%s)' % (
            s['word_index'], s['surface'], s['pos'][:1],
            '·'+s['feat']['state'][:4] if s['feat']['state'] else '',
            '·prep' if s['feat']['has_prep'] else '') for s in spans))
        # analyse only tagged terms that are NOT T2 (T2 = qualifier, not analysed standalone)
        for t in terms:
            i = span_of_term(spans, t)
            if i is None: continue
            tag = '' if t['cluster_code'] != 'T2' else '  [T2 qualifier]'
            print('\n  TERM %s "%s" [%s]%s' % (t['term_id'], t.get('target_word'), t['cluster_code'], tag))
            for name, res in [
                ('sense',     r_sense(spans, i, t)),
                ('type',      r_type(spans, i, t)),
                ('operation', r_operation(spans, i, t)),
                ('seat',      r_seat(spans, i, t)),
                ('target',    r_target(spans, i, t)),
                ('manner',    r_manner(spans, i, t)),
                ('source',    r_source(spans, i, t)),
                ('coupling',  r_coupling(spans, i, t, terms)),
            ]:
                val, resolution, basis = res
                if val is not None:
                    print('     %-10s = %-34s [%s · %s]' % (name, val, resolution, basis))
                else:
                    print('     %-10s = NONE                               [%s]' % (name, basis))

if __name__ == '__main__':
    main()
