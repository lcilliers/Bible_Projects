"""M08 pride: anchor scan (#2156). Read-only against iba.db and the current chapter files.

Researcher, 2026-10-15 (verbatim): "... cross checking that the narrative is anchored in the claims
register for this group of words". Splits every current chapter file into passages with the register's
own parser (iba/app/lib/narrativeregister.parse_chapter), keeps the passages whose text uses a
pride-group word, and lists the claims each tells (narrative_passage rows matched by opening words,
narrative_claim_telling status current). A passage that tells no claim is read by hand: quote only
(no claim needed), a statement beyond its verses (claim needed), or a statement to restate.

Usage (any folder): python m08-pride-anchor-scan-v1-20261015.py <tag>
Writes m08-pride-anchor-scan-<tag>.csv next to this script.
"""
import csv, os, pathlib, re, sqlite3, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
from iba.app.lib.narrativeregister import parse_chapter, opens_with  # noqa: E402

tag = sys.argv[1] if len(sys.argv) > 1 else 'v1-20261015'
c = sqlite3.connect(f'file:{ROOT / "iba/app/db/iba.db"}?mode=ro', uri=True)
NDIR = ROOT / '_analytics/essay/spirit_soul_body/inner-being-narrative'
WORDS = re.compile(r"\b(pride|proud\w*|arrogan\w*|haught\w*|boast\w*|mock\w*|scoff\w*|scorn\w*|conceit\w*|presum\w*|"
                   r"insolen\w*|lofty|loftiness|lifted[- ]up|puffed|majest\w*|derision|jeer\w*|self-exalt\w*|exalts himself)\b", re.I)
chapters = c.execute("""SELECT id, chapter_no, current_file FROM narrative_chapter
   WHERE inactive = 0 AND current_file IS NOT NULL ORDER BY reading_order""").fetchall()
tells = {}
for pid, ref, kind in c.execute("""SELECT t.passage_id, cl.claim_ref, t.kind FROM narrative_claim_telling t
   JOIN narrative_claim cl ON cl.id = t.claim_id WHERE t.status = 'current'"""):
    tells.setdefault(pid, []).append(f'{ref} ({kind})')
prows = {}
for pid, chid, anchor in c.execute('SELECT id, chapter_id, anchor_text FROM narrative_passage WHERE last_version IS NULL'):
    prows.setdefault(chid, []).append((pid, anchor))

out = HERE / f'm08-pride-anchor-scan-{tag}.csv'
n = untold = 0
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['chapter', 'section', 'ordinal', 'words', 'claims_told', 'text'])
    for chid, no, fname in chapters:
        _, sections, passages = parse_chapter((NDIR / fname).read_text(encoding='utf-8'))
        for p in passages:
            ws = sorted({m.lower() for m in WORDS.findall(p.text)})
            if not ws: continue
            told = [t for pid, a in prows.get(chid, []) if opens_with(p.text, a) for t in tells.get(pid, [])]
            n += 1; untold += not told
            w.writerow([no, sections[p.section].heading, p.ordinal, ' '.join(ws), ' | '.join(told), p.text])
print(n, 'passages with pride-group words;', untold, 'tell no claim ->', out)
