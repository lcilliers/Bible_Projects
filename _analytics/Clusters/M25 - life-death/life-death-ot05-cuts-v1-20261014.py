"""OT-05 (#2006): further cuts of the body / resurrection / glory verse set (read-only).

Usage: python life-death-ot05-cuts-v1-20261014.py GROUPS.csv OUTPREFIX
GROUPS is the output of life-death-ot05-grouping-v1-20261014.py. Writes:
  OUTPREFIX-cooccur.csv   one row per verse x other word in it: reference, group, strong, gloss,
                          cluster (cluster_strong), confidence, review_flag, alt_clusters
  OUTPREFIX-claims.csv    one row per verse x register claim sourcing it: reference, group,
                          claim_ref, status, chapter, claim_text
  OUTPREFIX-summary.txt   the counts the summary .md is written from
"""
import csv, sqlite3, sys
from collections import defaultdict, Counter

groups_csv, prefix = sys.argv[1:3]
db = sqlite3.connect('file:iba/app/db/iba.db?mode=ro', uri=True)
rows = list(csv.DictReader(open(groups_csv, encoding='utf-8-sig')))
pulled = {s.split(':')[0].strip() for r in rows for s in r['strongs'].split(';')}
grp = {r['reference']: r['group'] for r in rows}
vid = dict(db.execute("SELECT reference, id FROM verse WHERE deleted = 0"))
gloss = {s: g for s, g in db.execute("SELECT strongNumber, stepGloss FROM strong")}
cname = dict(db.execute("SELECT cluster_code, short_name FROM cluster"))
cs = {}
for s, c, conf, flag, alt, rat in db.execute(
        "SELECT strong, cluster_code, confidence, review_flag, alt_clusters, rationale FROM cluster_strong WHERE deleted = 0"):
    cs.setdefault(s, (c, conf or '', flag, alt or '', rat or ''))
chapter = dict(db.execute("SELECT id, chapter_no FROM narrative_chapter"))
out = open(f'{prefix}-summary.txt', 'w', encoding='utf-8')
def p(*a):
    print(*a, file=out)

# --- the pulled words' own codes
p('## Pulled words: their cluster codes')
for s in sorted(pulled):
    c, conf, flag, alt, rat = cs.get(s, ('-', '', 0, '', ''))
    p(s, gloss.get(s), c, cname.get(c), 'conf=' + conf, 'review=' + str(flag), 'alt=' + alt, '|', rat[:220])

# --- co-occurring words
co = []
for r in rows:
    v = vid.get(r['reference'])
    seen = set()
    for (s,) in db.execute("SELECT strong FROM verse_lexical WHERE verse_id = ? AND deleted = 0", (v,)):
        if s in pulled or s in seen or not s:
            continue
        seen.add(s)
        c, conf, flag, alt, _ = cs.get(s, ('', '', 0, '', ''))
        co.append([r['reference'], r['group'], s, gloss.get(s, ''), c, conf, flag, alt])
with open(f'{prefix}-cooccur.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'group', 'strong', 'gloss', 'cluster', 'confidence', 'review_flag', 'alt_clusters'])
    w.writerows(co)

gnames = sorted(set(grp.values()))
gsize = Counter(grp.values())
mverse = defaultdict(set)      # (group, M-code) -> verses
mall = defaultdict(set)        # M-code -> verses
tword = defaultdict(set)       # T-coded strong -> verses
with_m = defaultdict(set)
for ref, g, s, gl, c, conf, flag, alt in co:
    if c.startswith('M'):
        mverse[(g, c)].add(ref); mall[c].add(ref); with_m[g].add(ref)
    elif c.startswith('T'):
        tword[s].add(ref)

p('\n## M-codes across all 640 verses (verses with at least one word of the code)')
for c, vs in sorted(mall.items(), key=lambda x: -len(x[1]))[:40]:
    p(c, cname.get(c), len(vs))
p('\n## Per group: verses with any other M-code; top M-codes')
for g in gnames:
    top = sorted(((c, len(v)) for (gg, c), v in mverse.items() if gg == g), key=lambda x: -x[1])[:8]
    p(f'{g} | {gsize[g]} verses | {len(with_m[g])} with an M-code |',
      ', '.join(f'{c} {cname.get(c, "")} {n}' for c, n in top))

p('\n## T-coded words in the verses (5+ verses), with alt clusters')
for s, vs in sorted(tword.items(), key=lambda x: -len(x[1])):
    if len(vs) >= 5:
        c, conf, flag, alt, _ = cs[s]
        p(s, gloss.get(s), c, cname.get(c), len(vs), 'alt=' + alt, 'review=' + str(flag))

# --- claims
cl = []
claimgroups = defaultdict(set)
claimverses = defaultdict(set)
cinfo = {}
for ref in grp:
    v = vid.get(ref)
    for cid, cref, st, chid, txt in db.execute("""SELECT c.id, c.claim_ref, c.status, c.main_chapter_id, c.claim_text
            FROM narrative_claim_source s JOIN narrative_claim c ON c.id = s.claim_id
            WHERE s.verse_id = ? GROUP BY c.id""", (v,)):
        cl.append([ref, grp[ref], cref, st, chapter.get(chid, ''), txt])
        claimgroups[cref].add(grp[ref][:2]); claimverses[cref].add(ref)
        cinfo[cref] = (st, chapter.get(chid, ''), txt)
with open(f'{prefix}-claims.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['reference', 'group', 'claim_ref', 'status', 'chapter', 'claim_text'])
    w.writerows(cl)
p('\n## Claims sourced by these verses:', len(claimverses), 'claims,', len({r[0] for r in cl}), 'verses')
for cref in sorted(claimverses, key=lambda c: (-len(claimgroups[c]), c)):
    st, ch, txt = cinfo[cref]
    total = db.execute("""SELECT count(*) FROM narrative_claim_source s JOIN narrative_claim c ON c.id = s.claim_id
            WHERE c.claim_ref = ? AND s.source_kind = 'verse'""", (cref,)).fetchone()[0]
    p(cref, st, 'ch', ch, '| groups', ','.join(sorted(claimgroups[cref])), '| verses here', len(claimverses[cref]),
      'of', total, '|', (txt or '')[:200].replace('\n', ' '))
p('\n## Per group: verses cited in the narrative but behind no claim')
for g in gnames:
    cited = [r['reference'] for r in rows if r['group'] == g and r['cited'] == 'Y' and r['claim'] != 'Y']
    p(g, len(cited), ' '.join(cited))
# claims on the topic with none of these verses
p('\n## Current claims whose text speaks of the topic but cite none of these verses')
for cref, st, txt in db.execute("SELECT claim_ref, status, claim_text FROM narrative_claim WHERE status = 'current'"):
    t = (txt or '').lower()
    if cref not in claimverses and any(k in t for k in ('resurrect', 'raised', 'body', 'bodies', 'glori', 'imperishable', 'mortal')):
        p(cref, '|', (txt or '')[:200].replace('\n', ' '))
out.close()
print('done', len(co), 'co-occurrence rows;', len(cl), 'verse-claim rows')
