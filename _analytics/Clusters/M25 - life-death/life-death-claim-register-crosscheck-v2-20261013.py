"""Verses of a list of Strong's, mapped to the narrative register: citation, paragraph, claims (read-only).

Usage: python life-death-claim-register-crosscheck-v2-20261013.py OUT.csv H4191 H4194 ...
One row per verse x citing paragraph, in canonical verse order; a verse the narrative does not cite
gets one row with the narrative columns empty. Columns:
  reference, strongs_in_verse            the verse, from the Strong's list
  chapter, section, cited_as, quoted     narrative_citation (current citations only)
  paragraph                              the narrative paragraph holding the citation
  paragraph_from                         where the paragraph came from: narrative_citation.passage_id
                                         when the register has it, else the current chapter file
                                         (passage links are the register's R0 step)
  match_note                             set when a short reference ("17:13") matched more than one
                                         paragraph of the section: another book's 17:13 may be one of them
  claims_sourcing_verse                  narrative_claim_source -> narrative_claim (ref, status, text)
Supersedes v1 (two files, no paragraph).
"""
import csv, re, sqlite3, sys
from collections import defaultdict

out, strongs = sys.argv[1], sys.argv[2:]
NARR = '_analytics/essay/spirit_soul_body/inner-being-narrative/'
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
q = ','.join('?' * len(strongs))
order = {b: o for b, o in db.execute("SELECT book, ordinal FROM cfg_book_order")}

verses, hits = {}, defaultdict(list)
for vid, osis, ref, st, surf in db.execute(f"""SELECT v.id, v.osisId, v.reference, vl.strong, vl.surface
        FROM verse_lexical vl JOIN verse v ON v.id = vl.verse_id AND v.deleted = 0
        WHERE vl.deleted = 0 AND vl.strong IN ({q}) ORDER BY vl.position""", strongs):
    verses[vid] = (osis, ref)
    hits[vid].append(f'{st}:{surf}')

chapters = {i: r for i, *r in db.execute(
    "SELECT id, chapter_no, current_version, current_file FROM narrative_chapter")}
sections = dict(db.execute("SELECT id, heading FROM narrative_section"))
passages = dict(db.execute("SELECT id, passage_text FROM narrative_passage"))

_paras = {}
def paragraphs(ch_id):
    """[(heading, paragraph_text)] of a chapter's current file, blank-line separated."""
    if ch_id not in _paras:
        heading, block, out_ = '(opening)', [], []
        def flush():
            if block:
                out_.append((heading, '\n'.join(block).strip()))
                block.clear()
        with open(NARR + chapters[ch_id][2], encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                m = re.match(r'#{2,6}\s+(.*)', line)
                if m:
                    flush(); heading = m.group(1).strip()
                elif line.startswith('# ') or not line.strip():
                    flush()
                else:
                    block.append(line)
        flush()
        _paras[ch_id] = out_
    return _paras[ch_id]

def find(ch_id, sec, written):
    paras = paragraphs(ch_id)
    head = sections.get(sec) if sec else None
    pool = [p for h, p in paras if h == head] if head else paras
    # whole reference only: "3:2" must not match inside "3:24" or "13:2"
    pat = re.compile(r'(?<![\d:])' + re.escape(written) + r'(?!\d)')
    found = [p for p in pool if pat.search(p)]
    if not found:   # the section heading may have been renamed since; search the whole chapter
        found = [p for h, p in paras if pat.search(p)]
    return found

claims_by_verse = defaultdict(list)
for vid, ref, status, text in db.execute(
        """SELECT s.verse_id, c.claim_ref, c.status, c.claim_text FROM narrative_claim_source s
           JOIN narrative_claim c ON c.id = s.claim_id WHERE s.source_kind = 'verse'"""):
    if vid in verses:
        claims_by_verse[vid].append(f'{ref} ({status}): {text}')

cites = defaultdict(list)
for vid, ch, sec, pid, written, quoted, last in db.execute(
        "SELECT verse_id, chapter_id, section_id, passage_id, ref_as_written, quoted, last_version "
        "FROM narrative_citation WHERE verse_id IS NOT NULL"):
    if vid in verses and (last is None or last >= chapters[ch][1]):
        cites[vid].append((ch, sec, pid, written, quoted))

def vkey(vid):
    b, c_, v_ = verses[vid][0].split('.')
    return (order.get(b, 999), int(c_), int(v_))

n_rows = n_missing = n_check = 0
with open(out, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'strongs_in_verse', 'chapter', 'section', 'cited_as', 'quoted',
                'paragraph', 'paragraph_from', 'match_note', 'claims_sourcing_verse'])
    for vid in sorted(verses, key=vkey):
        base = [verses[vid][1], '; '.join(dict.fromkeys(hits[vid]))]
        cl = ' || '.join(dict.fromkeys(claims_by_verse[vid]))
        if not cites[vid]:
            w.writerow(base + ['', '', '', '', '', '', '', cl]); n_rows += 1
            continue
        seen = set()
        for ch, sec, pid, written, quoted in cites[vid]:
            no, curv, fname = chapters[ch]
            if pid and pid in passages:
                found, src = [passages[pid]], f'register passage {pid}'
            else:
                found, src = find(ch, sec, written), f'chapter file {fname}'
            if not found:
                found, src = [''], f'NOT FOUND in {fname}'
                n_missing += 1
            note = ''
            if len(found) > 1 and not re.search('[A-Za-z]', written):
                note = f'short reference found in {len(found)} paragraphs: check which one is this verse'
                n_check += 1
            for para in found:
                key = (no, para)
                if key in seen:
                    continue
                seen.add(key)
                w.writerow(base + [no, sections.get(sec, ''), written, quoted, para, src, note, cl]); n_rows += 1

print(f'{len(verses)} verses -> {n_rows} rows; cited {sum(1 for v in verses if cites[v])}; '
      f'with claims {sum(1 for v in verses if claims_by_verse[v])}; citations with no paragraph found {n_missing}; '
      f'short references to check {n_check}')
