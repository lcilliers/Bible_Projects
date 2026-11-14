"""temp_2502_evidence_pairs_test_run.py -- tests for escalation #2502: the layer 2 pairings of the collection evidence report
(lib/collectionevidence.py build_pairs, lib/collectionevidencereport.py _body_pairs and the four workbook sheets).

Each case checks the built data and files against a direct query of the tables written here, not against the builder's own lists, and runs the refusals (a missing
setting, a verse list). Runs against a COPY of iba.db (never the live database): pass its path.

Usage: python iba/app/tools/temp_2502_evidence_pairs_test_run.py <db copy> <scratch dir>
"""
import collections
import pathlib
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


db = pathlib.Path(sys.argv[1])
S = pathlib.Path(sys.argv[2]) / "t2502"
S.mkdir(parents=True, exist_ok=True)
assert db.resolve() != (ROOT / "iba/app/db/iba.db").resolve(), "run against a copy"
cfg = Cfg(db)
conn = cfg.conn
q = lambda sql, *a: conn.execute(sql, a).fetchall()  # noqa: E731
vals = ev.read_settings(cfg)
order = ev.Order(conn)
P = vals["pairs"]

# T1 the setting is read and complete
case("T1", "the setting holds its five keys", set(P) == {"collection_status", "bands", "morph_class", "qualifier", "top_n"}, sorted(P))

# T2 a missing setting refuses (synthetic bad input)
saved = conn.execute("SELECT inactive FROM cfg_setting WHERE key='collection.evidence_pairs'").fetchone()
conn.execute("UPDATE cfg_setting SET inactive=1 WHERE key='collection.evidence_pairs'")
conn.commit()
try:
    cfg2 = Cfg(db)
    try:
        ev.read_settings(cfg2)
        refused = False
    except ev.EvidenceError as exc:
        refused = "collection.evidence_pairs" in str(exc)
finally:
    conn.execute("UPDATE cfg_setting SET inactive=? WHERE key='collection.evidence_pairs'", (saved[0],))
    conn.commit()
case("T2", "a missing collection.evidence_pairs refuses and names the key", refused, "refused" if refused else "no refusal")

# the collection `thought` (real data)
d = ev.build_collection(conn, ev.resolve(conn, ["thought"])[0], vals["tiers"], order)
d["pairs"] = ev.build_pairs(conn, d, vals, order)
pr = d["pairs"]
rows, pairs = pr["rows"], pr["pairs"]
verses = sorted({o["verse_id"] for o in d["occurrences"]})

n_direct = len(ev._in(conn, "SELECT id FROM verse_lexical WHERE deleted=0 AND verse_id IN ({in})", verses))
case("T3", "the verse view holds every live verse_lexical row of the member verses", len(rows) == n_direct, f"view {len(rows)} direct {n_direct}")
case("T4", "the rows marked member are exactly the member occurrences", {x["vl_id"] for x in rows if x["member"]} == {o["vl_id"] for o in d["occurrences"]},
     f"{sum(1 for x in rows if x['member'])} member rows of {len(d['occurrences'])} occurrences")
keys = [(x["sk"], x["position"] if x["position"] is not None else 0) for x in rows]
case("T5", "rows are in Scripture order and word order", keys == sorted(keys), f"{len(keys)} rows")

bad = 0
for x in rows:
    pk, ng = q("SELECT party_kind, is_negator FROM verse_lexical WHERE id=?", x["vl_id"])[0]
    if (pk or None) != (x["party_kind"] or None) or (ng or None) != (x["is_negator"] or None):
        bad += 1
    if x["type"].startswith("entity") and not pk:
        bad += 1
    if x["type"] == "negator" and not (ng or "T5" in x["clusters"].split(", ")):
        bad += 1
case("T6", "the entity and negator types agree with verse_lexical", bad == 0, f"{bad} disagreements over {len(rows)} rows")

bad = 0
for p in pairs:
    m, o = p["member"], p["other"]
    dist = abs(o["position"] - m["position"])
    band = "adjacent" if dist <= P["bands"]["adjacent"] else "near" if dist <= P["bands"]["near"] else "far"
    if dist != p["distance"] or band != p["band"] or p["side"] != ("before" if o["position"] < m["position"] else "after") or o["position"] == m["position"] or o["vl_id"] == m["vl_id"]:
        bad += 1
    if o["verse_id"] != m["verse_id"] or o["type"] == "other":
        bad += 1
case("T7", "every pairing's distance, band and side agree with the positions and the setting", bad == 0 and len(pairs) > 0, f"{len(pairs)} pairings, {bad} wrong")

exp = 0
byv = collections.defaultdict(list)
for x in rows:
    byv[x["verse_id"]].append(x)
for m in rows:
    if m["member"]:
        exp += sum(1 for r in byv[m["verse_id"]] if r["vl_id"] != m["vl_id"] and r["position"] != m["position"] and r["type"] != "other")
case("T8", "the pairings are all member by typed-neighbour combinations in a verse", exp == len(pairs), f"expected {exp} built {len(pairs)}")

sample = [x for x in rows if x["type"] == "word of another collection"][:40]
bad = 0
for x in sample:
    names = {r[0] for r in q("SELECT DISTINCT c.name FROM collection_link l JOIN collection c ON c.id=l.collection_id JOIN surface_term t ON t.id=l.term_id "
                             "WHERE l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND l.tier IN ('core','synonym','opposite','gathered','phrase') AND lower(trim(t.surface))=?", x["surface"])}
    via_base = {r[0] for r in q("SELECT DISTINCT c.name FROM collection_link l JOIN collection c ON c.id=l.collection_id JOIN surface_term b ON b.id=l.term_id "
                                "JOIN surface_term t ON t.base_id=b.id WHERE l.deleted=0 AND c.deleted=0 AND c.status='confirmed' AND lower(trim(t.surface))=?", x["surface"])}
    if not set(x["collections"]) <= (names | via_base):
        bad += 1
case("T9", "a sample of 40 neighbour collections traces to confirmed collections by link or base", bad == 0, f"{len(sample)} sampled, {bad} untraced")

bad = 0
for x in [r for r in rows if r["obs"]][:60] + [r for r in rows if not r["obs"]][:60]:
    n = q("SELECT count(*) FROM ib_node n JOIN ib_observation o ON o.id=n.observation_id WHERE n.deleted=0 AND o.deleted=0 AND n.verse_lexical_id=?", x["vl_id"])[0][0]
    if (n > 0) != bool(x["obs"]):
        bad += 1
case("T10", "the read status agrees with the live nodes of 120 sampled rows", bad == 0, f"{bad} wrong")

pr_rows = rep.pair_rows(d)
code_links = sum(r[4] for r in pr_rows if r[0] == "Strong's code")
surf_links = sum(r[4] for r in pr_rows if r[0] == "surface")
case("T11", "links at the code and surface levels equal the pairings", code_links == len(pairs) == surf_links, f"code {code_links} surface {surf_links} pairings {len(pairs)}")

xl = S / "thought.xlsx"
rep.write_workbook(xl, [d], vals, "TEST-RUN", "2026-11-14T00:00:00Z")
wb = load_workbook(xl)
names = wb.sheetnames
need = ["Verse view", "Pairings", "Pairing summary", "Verse observations"]
case("T12", "the four new sheets are in the workbook", all(n in names for n in need), names)
case("T13", "sheet rows: Verse view = verse_lexical rows; Pairings = pairings; Pairing summary = counted rows; Verse observations = nodes",
     wb["Verse view"].max_row - 1 == len(rows) and wb["Pairings"].max_row - 1 == len(pairs) and wb["Pairing summary"].max_row - 1 == len(pr_rows)
     and wb["Verse observations"].max_row - 1 == len(pr["observations"]),
     f"{wb['Verse view'].max_row - 1}/{len(rows)} {wb['Pairings'].max_row - 1}/{len(pairs)} {wb['Pairing summary'].max_row - 1}/{len(pr_rows)} {wb['Verse observations'].max_row - 1}/{len(pr['observations'])}")
blank = all(c.value in (None, "") for c in wb["Pairings"]["X"][1:]) and all(c.value in (None, "") for c in wb["Pairing summary"]["L"][1:])     # the reading column (#2503 added two subgroup columns before it)
case("T14", "the reading column is empty on the pairings and the summary", blank, "empty" if blank else "filled")
formulas = sum(1 for ws in wb.worksheets for row in ws.iter_rows() for c in row if c.data_type == "f")
case("T15", "no cell of any sheet is stored as a formula (text starting with '=' is text)", formulas == 0, f"{formulas} formula cells")

md = rep.render([d], vals, "TEST-RUN", "2026-11-14T00:00:00Z", xl.name)
case("T16", "the Markdown has section 3a with its five subsections, between sections 3 and 4",
     all(s in md for s in ("## 3a.", "### 3a.1", "### 3a.2", "### 3a.3", "### 3a.4", "### 3a.5")) and md.index("## 3. ") < md.index("## 3a.") < md.index("## 4. "),
     "found" if "## 3a." in md else "missing")
(S / "thought.md").write_text(md, encoding="utf-8")

qual = sum(1 for p in pairs if p["other"]["qualifier"])
case("T17", "qualifier candidates appear among the pairings", qual > 0, f"{qual} pairings with a qualifier candidate")

dv = ev.build_verses(conn, ev.resolve_verses(conn, cfg, "Pro 20:27", order), order)
xv = S / "verse.xlsx"
rep.write_workbook(xv, [dv], vals, "TEST-RUN", "2026-11-14T00:00:00Z")
wv = load_workbook(xv)
case("T18", "a verse report is built as before, without pairing sheets", "Pairings" not in wv.sheetnames and "Occurrences" in wv.sheetnames, wv.sheetnames[:4])

tiny = q("SELECT c.name FROM collection c WHERE c.deleted=0 AND c.status='confirmed' ORDER BY (SELECT count(*) FROM collection_link l WHERE l.collection_id=c.id) LIMIT 1")[0][0]
dt = ev.build_collection(conn, ev.resolve(conn, [tiny])[0], vals["tiers"], order)
dt["pairs"] = ev.build_pairs(conn, dt, vals, order)
rep.render([dt], vals, "TEST-RUN", "2026-11-14T00:00:00Z", "t.xlsx")
case("T19", f"the smallest collection ({tiny}) builds with {len(dt['occurrences'])} occurrences", True, f"{len(dt['pairs']['pairs'])} pairings")

print("\n| case | what | result | evidence |\n|---|---|---|---|")
for r in results:
    print("| " + " | ".join(r) + " |")
print(f"\n{sum(1 for r in results if r[2] == 'PASS')} pass, {sum(1 for r in results if r[2] == 'FAIL')} fail; files in {S}")
sys.exit(0 if all(r[2] == "PASS" for r in results) else 1)
