"""temp_2477_evidence_report_test_run.py -- tests for escalation #2477: the collection evidence report as a reading (Markdown) plus an Excel workbook
(lib/collectionevidence.py builds the data, lib/collectionevidencereport.py writes the files, handlers/collectionbuild.py evidence).

Each case checks the built files against a direct query of the tables written here, not against the builder's own lists. Read-only on iba.db; every file goes to the scratch dir.

Usage: python iba/app/tools/temp_2477_evidence_report_test_run.py <scratch dir>
"""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from openpyxl import load_workbook  # noqa: E402

from iba.app.lib import collectionevidence as ev  # noqa: E402
from iba.app.lib import collectionevidencereport as rep  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:330]))


S = pathlib.Path(sys.argv[1]) / "t2477"
S.mkdir(parents=True, exist_ok=True)
cfg = Cfg(ROOT / "iba/app/db/iba.db")
conn = cfg.conn
vals = ev.read_settings(cfg)
order = ev.Order(conn)
q = lambda sql, *a: conn.execute(sql, a).fetchall()  # noqa: E731

# ── the collection `search` ──
d = ev.build_collection(conn, ev.resolve(conn, ["search"])[0], vals["tiers"], order)
md = rep.render([d], vals, "TEST-RUN", "2026-11-11T00:00:00Z", "t.xlsx")
xl = S / "search.xlsx"
listed = rep.write_workbook(xl, [d], vals, "TEST-RUN", "2026-11-11T00:00:00Z")
wb = load_workbook(xl, read_only=True)
rows = lambda name: [r for r in wb[name].iter_rows(min_row=2, values_only=True)]  # noqa: E731
surfaces = {t["surface"] for t in d["terms"]}
ph = ",".join("?" * len(surfaces))

# S1 sheets exist and the Read me row counts equal the sheet row counts
readme = {r[0]: r[4] for r in wb["Read me"].iter_rows(min_row=4, values_only=True) if r[0]}
bad = [n for n, k in readme.items() if len(rows(n[:31])) != k]
case("S1", "every sheet listed in Read me exists with the row count Read me states", not bad and len(readme) == 20, f"{len(readme)} sheets; mismatches {bad}")

# S2 occurrences = live verse_lexical rows of the member surfaces (direct query)
n_vl = q(f"SELECT count(*) FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN ({ph})", *surfaces)[0][0]
case("S2", "Occurrences sheet rows = live verse_lexical rows whose surface is a member surface", len(rows("Occurrences")) == n_vl, f"sheet {len(rows('Occurrences'))}, query {n_vl}")

# S3 live + withdrawn observations = the distinct observations of the nodes on the occurrences (direct query)
vl_ids = [r[0] for r in q(f"SELECT id FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN ({ph})", *surfaces)]
mark = ",".join("?" * len(vl_ids))
live_q = q(f"SELECT count(DISTINCT o.id) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.verse_lexical_id IN ({mark}) AND o.deleted=0", *vl_ids)[0][0]
wd_q = q(f"SELECT count(DISTINCT o.id) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.verse_lexical_id IN ({mark}) AND o.deleted=1", *vl_ids)[0][0]
case("S3", "Observations sheet = live observations and Withdrawn observations sheet = withdrawn ones on the occurrences (direct query)",
     len(rows("Observations")) == live_q and len(rows("Withdrawn observations")) == wd_q,
     f"live sheet {len(rows('Observations'))} query {live_q}; withdrawn sheet {len(rows('Withdrawn observations'))} query {wd_q}")

# S4 no withdrawn observation is a card in the Markdown; every live engagement observation is
wd_ids = {r[1] for r in rows("Withdrawn observations")}
md_ids = {int(x) for x in re.findall(r"\*\*Observation (\d+)\*\*", md)}
eng_live = {r[1] for r in rows("Observations") if r[2] == vals["engagement_stage"]}
case("S4", "no withdrawn observation appears in the Markdown body; every live engagement observation does", not (md_ids & wd_ids) and eng_live <= md_ids,
     f"withdrawn in body {len(md_ids & wd_ids)}; engagement observations missing from body {len(eng_live - md_ids)}; engagement observations {len(eng_live)}")

# S5 own and shared occurrences: the shared table holds every surface_kind <> own row (direct query)
shared_q = q(f"SELECT count(*) FROM verse_lexical WHERE deleted=0 AND lower(trim(surface)) IN ({ph}) AND surface_kind<>'own'", *surfaces)[0][0]
m = re.search(r"### 3\.\d+ Occurrences where the member surface is shared with another code's unit \((\d+)\)", md)
case("S5", "the shared-surface section counts every surface_kind <> own occurrence (direct query)", m is not None and int(m.group(1)) == shared_q, f"section {m and m.group(1)}, query {shared_q}")

# S6 the `find` rows with a code other than H4672 or G2147 are all in the Occurrences sheet with the kind as stored
other = q("SELECT id, strong, surface_kind FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))='find' AND strong NOT IN ('H4672','G2147')")
occ = {r[4]: r for r in rows("Occurrences")}
kinds = collections.Counter(occ[i][12] for i, _, _ in other if i in occ)
case("S6", "the rows of `find` with a code other than H4672/G2147 are all in the Occurrences sheet, own or shared as stored", len(other) == sum(kinds.values()) and len(other) == 30,
     f"{len(other)} rows: sheet kinds {dict(kinds)}; stored surface_kind {dict(collections.Counter(k for _, _, k in other))}")

# S7 claims: a by-verse claim names a reaching verse and a member word; a direct claim names an observation
cl = rows("Claims")
bad = [r[1] for r in cl if (r[9] == "verse" and not (r[13] or "").strip()) or (r[9] != "verse" and not (r[12] or "").strip())]
claims_q = q("SELECT count(DISTINCT claim_id) FROM narrative_claim_source WHERE observation_id IN (SELECT observation_id FROM ib_node WHERE verse_lexical_id IN (%s)) "
             "OR verse_id IN (SELECT verse_id FROM verse_lexical WHERE id IN (%s))" % (mark, mark), *vl_ids, *vl_ids)[0][0]
case("S7", "Claims sheet = distinct claims reaching the occurrences (direct query); each states what reached it", not bad and len(cl) == claims_q,
     f"sheet {len(cl)}, query {claims_q}, claims with no reach text {bad}")

# S8 faults: the live nodes on deleted observations (direct query), each with verse and word
fa = [r for r in rows("Faults") if r[1] == "live-node-on-deleted-observation"]
f_q = q(f"SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=1 AND n.verse_lexical_id IN ({mark})", *vl_ids)[0][0]
blank = [r[3] for r in fa if not r[9] or not r[10]]
case("S8", "Faults sheet lists every live node on a deleted observation with its verse and word (direct query)", len(fa) == f_q and not blank,
     f"sheet {len(fa)}, query {f_q}, rows with no verse or word {len(blank)}")

# S9 phrases = live links of tier phrase
ph_q = q("SELECT count(*) FROM collection_link l JOIN collection c ON c.id=l.collection_id WHERE c.name='search' AND l.deleted=0 AND l.tier='phrase'")[0][0]
case("S9", "Phrases sheet = live tier-phrase links of the collection (direct query); the Markdown has the section", len(rows("Phrases")) == ph_q and f"## 6. Phrases attached to the collection ({ph_q})" in md,
     f"sheet {len(rows('Phrases'))}, query {ph_q}")

# S10 size and shape of the Markdown against the 3.6 MB report of #2477
case("S10", "the Markdown is a fraction of the 3.6 MB report: under 600 KB and under 4000 lines", len(md.encode("utf-8")) < 600_000 and md.count("\n") < 4000,
     f"{len(md.encode('utf-8'))} bytes, {md.count(chr(10))} lines")

# S11 the counts of section 2.2 add up to the occurrences
tot = sum(int(a) + int(b) for a, b in re.findall(r"^\| [HG]\d+\S* [^|]*\| (\d+) \| (\d+) \|", md, re.M))
case("S11", "section 2.2 own + shared counts add up to the occurrences", tot == n_vl, f"table {tot}, occurrences {n_vl}")

# ── the layout of a verse list and of two collections ──
dv = ev.build_verses(conn, ev.resolve_verses(conn, cfg, "Pro 6:14-16; Mat 11:29", order), order)
mdv = rep.render([dv], vals, "TEST-RUN", "2026-11-11T00:00:00Z", "v.xlsx")
rep.write_workbook(S / "verses.xlsx", [dv], vals, "TEST-RUN", "2026-11-11T00:00:00Z")
wv = load_workbook(S / "verses.xlsx", read_only=True)
case("V1", "a verse list: every requested verse has a section and the Verses sheet has one row for each",
     all(f"### {v['reference']}" in mdv for v in dv["verses"]) and len(list(wv["Verses"].iter_rows(min_row=2))) == len(dv["verses"]), f"{len(dv['verses'])} verses; sheets {wv.sheetnames[:6]}")
d2 = ev.build_collection(conn, ev.resolve(conn, ["righteous"])[0], vals["tiers"], order)
md2 = rep.render([d, d2], vals, "TEST-RUN", "2026-11-11T00:00:00Z", "m.xlsx")
rep.write_workbook(S / "two.xlsx", [d, d2], vals, "TEST-RUN", "2026-11-11T00:00:00Z")
w2 = load_workbook(S / "two.xlsx", read_only=True)
scopes = {r[0] for r in w2["Occurrences"].iter_rows(min_row=2, values_only=True)}
case("V2", "two collections: both are reported and the sheets carry a scope column telling them apart", "search" in scopes and "righteous" in scopes and md2.count("## 2. The collection") == 2,
     f"scopes {scopes}")

# ── synthetic bad input ──
errs = []
for label, f in (("unknown collection", lambda: ev.resolve(conn, ["no-such-collection"])), ("named twice", lambda: ev.resolve(conn, ["search", "search"])),
                 ("no name", lambda: ev.resolve(conn, [""])), ("bad reference", lambda: ev.resolve_verses(conn, cfg, "Nonsense 99:99", order)),
                 ("overlapping verses", lambda: ev.resolve_verses(conn, cfg, "Pro 6:14-16; Pro 6:15", order))):
    try:
        f()
        errs.append(f"{label}: not refused")
    except ev.EvidenceError:
        pass
case("B1", "bad input is refused with EvidenceError and nothing is written", not errs, errs or "5 of 5 refused")
dirty = rep._clean("a\x00b\x0bc") + "|" + rep._clean("x" * 40000)[-40:]
case("B2", "a control character is removed and an over-long cell is cut at the cell limit, so the workbook opens", "\x00" not in dirty and "cut at the cell limit" in dirty, repr(dirty[:20]))
case("B3", "a pipe in stored text cannot break a Markdown table cell", rep._cell("a|b\nc") == "a\\|b c", repr(rep._cell("a|b\nc")))
case("B4", "marking a member word: found whole word marked, not found left as stored",
     rep._mark("He sought the Lord", "sought") == "He **sought** the Lord" and rep._mark("He sought", "seek") == "He sought", rep._mark("He sought the Lord", "sought"))
case("B5", "plural helper reads 1 verse and 2 verses", rep._n(1, "verse") == "1 verse" and rep._n(2, "verse") == "2 verses", f"{rep._n(1, 'verse')}; {rep._n(2, 'verse')}")

out = ["| id | case | result | evidence |", "|---|---|---|---|"] + [f"| {a} | {b} | {c} | {e} |" for a, b, c, e in results]
(S / "results.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out))
print(f"\n{sum(r[2] == 'PASS' for r in results)} of {len(results)} passed")
sys.exit(0 if all(r[2] == "PASS" for r in results) else 1)
