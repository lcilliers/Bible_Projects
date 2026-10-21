"""Cross-check the verses of a list of Strong's against the narrative claim register (read-only on iba.db).

Usage: python life-death-claim-register-crosscheck-v1-20261013.py OUT_PREFIX H4191 H4194 ...
Writes two CSVs:
  OUT_PREFIX-verses-v1-<date>.csv  one row per verse holding any of the Strong's:
      the Strong's in it, where the narrative cites it now (chapter, section, as written),
      where it was cited only in an earlier chapter version, and the register claims that
      name it as a source.
  OUT_PREFIX-claims-v1-<date>.csv  one row per claim linked to the set, either by a source
      verse in the set or by wording (death, die, dead, Sheol, Hades, grave, sleep ...).
A citation is current when its last_version is empty or not older than the chapter's
current_version; otherwise it is "earlier version only".
"""
import csv, re, sqlite3, sys
from collections import defaultdict
from datetime import date

prefix, strongs = sys.argv[1], sys.argv[2:]
stamp = date.today().strftime('%Y%m%d')
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
q = ','.join('?' * len(strongs))
order = {b: o for b, o in db.execute("SELECT book, ordinal FROM cfg_book_order")}

verses, hits = {}, defaultdict(list)
for vid, osis, ref, st, surf in db.execute(f"""SELECT v.id, v.osisId, v.reference, vl.strong, vl.surface
        FROM verse_lexical vl JOIN verse v ON v.id = vl.verse_id AND v.deleted = 0
        WHERE vl.deleted = 0 AND vl.strong IN ({q}) ORDER BY vl.position""", strongs):
    verses[vid] = (osis, ref)
    hits[vid].append(f'{st}:{surf}')

chapters = {i: (no, cur) for i, no, cur in db.execute(
    "SELECT id, chapter_no, current_version FROM narrative_chapter")}
sections = dict(db.execute("SELECT id, heading FROM narrative_section"))

cur_cit, old_cit = defaultdict(list), defaultdict(list)
for vid, ch, sec, written, last in db.execute(
        "SELECT verse_id, chapter_id, section_id, ref_as_written, last_version FROM narrative_citation "
        "WHERE verse_id IS NOT NULL"):
    if vid not in verses:
        continue
    no, curv = chapters[ch]
    label = f'Ch {no}' + (f' / {sections.get(sec)}' if sec else '') + f' [{written}]'
    if last is None or last >= curv:
        cur_cit[vid].append(label)
    else:
        old_cit[vid].append(f'{label} (last v{last}, now v{curv})')

claims = {r[0]: r for r in db.execute(
    """SELECT c.id, c.claim_ref, c.status, c.verdict, c.original_chapter, ch.chapter_no,
              c.claim_text, c.beyond_text
       FROM narrative_claim c LEFT JOIN narrative_chapter ch ON ch.id = c.main_chapter_id""")}
claim_srcs = defaultdict(list)
verse_claims = defaultdict(list)
for cid, vid, written in db.execute(
        "SELECT claim_id, verse_id, coalesce(ref_as_written, ref_normalised) FROM narrative_claim_source "
        "WHERE source_kind = 'verse'"):
    claim_srcs[cid].append((vid, written))
    if vid in verses:
        verse_claims[vid].append(f'{claims[cid][1]} ({claims[cid][2]})')

def vkey(vid):
    b, ch, vs = verses[vid][0].split('.')
    return (order.get(b, 999), int(ch), int(vs))

with open(f'{prefix}-verses-v1-{stamp}.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'strongs_in_verse', 'cited_now', 'cited_earlier_version_only',
                'register_claims', 'status'])
    for vid in sorted(verses, key=vkey):
        now, old, cl = cur_cit[vid], old_cit[vid], verse_claims[vid]
        status = ('claim source' if cl else '') or ('cited' if now else '') or \
                 ('earlier version only' if old else 'not in narrative')
        w.writerow([verses[vid][1], '; '.join(dict.fromkeys(hits[vid])), ' | '.join(dict.fromkeys(now)),
                    ' | '.join(dict.fromkeys(old)), '; '.join(dict.fromkeys(cl)), status])

words = re.compile(r'\b(death|deaths|die|dies|died|dying|dead|Sheol|Hades|grave|graves|pit|'
                   r'sleep|sleeps|slept|asleep)\b', re.I)
with open(f'{prefix}-claims-v1-{stamp}.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['claim_ref', 'status', 'verdict', 'main_chapter', 'original_chapter', 'link',
                'sources_in_set', 'other_sources', 'wording_match', 'claim_text', 'beyond_text'])
    rows = []
    for cid, ref, status, verdict, orig, mainch, text, beyond in claims.values():
        inset = [wr for v, wr in claim_srcs[cid] if v in verses]
        other = [wr for v, wr in claim_srcs[cid] if v not in verses]
        found = sorted({m.lower() for m in words.findall(f'{text} {beyond or ""}')})
        if not inset and not found:
            continue
        link = ' + '.join(x for x, y in (('source verse', inset), ('wording', found)) if y)
        rows.append([ref, status, verdict, mainch or '', orig or '', link,
                     '; '.join(dict.fromkeys(inset)), '; '.join(dict.fromkeys(other)),
                     ', '.join(found), text, beyond or ''])
    w.writerows(rows)

n = len(verses)
print(f'verses: {n}; cited now {sum(1 for v in verses if cur_cit[v])}; '
      f'earlier version only {sum(1 for v in verses if old_cit[v] and not cur_cit[v])}; '
      f'claim source {sum(1 for v in verses if verse_claims[v])}; '
      f'not in narrative {sum(1 for v in verses if not (cur_cit[v] or old_cit[v] or verse_claims[v]))}')
print(f'claims linked: {len(rows)} (by source verse {sum(1 for r in rows if "source" in r[5])}, '
      f'by wording only {sum(1 for r in rows if r[5] == "wording")})')
per = defaultdict(lambda: [0, 0])
for v in verses:
    for s in {h.split(':')[0] for h in hits[v]}:
        per[s][0] += 1; per[s][1] += bool(cur_cit[v])
for s in strongs:
    print(f'  {s}: {per[s][0]} verses, {per[s][1]} cited now')
