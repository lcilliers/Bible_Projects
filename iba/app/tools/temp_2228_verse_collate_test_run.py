"""temp_2228_verse_collate_test_run.py -- test plan for escalation #2228 tools 3-5, collating a scope
(outputs/escalation/2228-verse-collate-design-v1-20261023.md). Run on a copy of iba.db made with
lib/dbsnapshot.copy_db, the #2228 migrations applied to the copy and the reading index built on the copy from the
live files (read-only on the files). Expected values come from plain SQL on the copy.

Usage: python iba/app/tools/temp_2228_verse_collate_test_run.py <scratch dir>
"""
import json
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import narrativeregister as nr  # noqa: E402
from iba.app.lib import readingindex as ri  # noqa: E402
from iba.app.lib import versecollate as vc  # noqa: E402
from iba.app.lib import versescope as vs  # noqa: E402
from iba.app.handlers import versecollate as hc  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2228vc"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT)}
mo = []
for m in ("reading_index_2228_v1_20261023.py", "verse_collate_2228_v1_20261023.py"):
    mp = ROOT / "iba/app/migration" / m
    mp = mp if mp.exists() else ROOT / "iba/app/migration/archive" / m
    for _ in range(2):
        r = subprocess.run([sys.executable, str(mp), "--db", str(DB)], capture_output=True, text=True, env=env)
        mo.append((r.stdout or r.stderr).strip())
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='verse_collate.output_dir'", (json.dumps(str(S / "out")),))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
ri.build(cfg, nr.Writer(conn, "reading_index.build", "Claude"), ROOT)
conn.commit()
results = []


def case(cid, desc, passed, evidence, secs=None):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:400],
                    f"{secs:.1f}" if secs is not None else ""))
    print(f"{cid} {'PASS' if passed else 'FAIL'}", flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def collate(req, root=ROOT):
    t0 = time.time()
    out = vc.collate(cfg, vs.normalise_request(req), root)
    return out, time.time() - t0


case("C0", "migrations applied (or already), then skipped", all(("applied" in mo[i] or "already" in mo[i]) and "already" in mo[i + 1]
                                                               for i in (0, 2)), mo)
changes = conn.total_changes

out, s = collate({"Cluster": "M02", "OnlyStrong": "H3708A"})
V = {r["verse_id"]: r for r in out["verses"]}
J = json.dumps(list(V))
want = {k: dict(q(sql, J)) for k, sql in {
    "obs": "SELECT v.id, count(DISTINCT o.id) FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference JOIN ib_observation o "
           "ON o.id=n.observation_id AND o.status='draft' WHERE v.id IN (SELECT value FROM json_each(?)) GROUP BY v.id",
    "hits": "SELECT verse_id, count(*) FROM reading_strand_hit WHERE verse_id IN (SELECT value FROM json_each(?)) GROUP BY 1",
    "claims": "SELECT s.verse_id, count(DISTINCT s.claim_id) FROM narrative_claim_source s JOIN narrative_claim c ON c.id=s.claim_id "
              "AND c.status IN ('current','held') WHERE s.verse_id IN (SELECT value FROM json_each(?)) GROUP BY 1",
    "blocks": "SELECT ci.verse_id, count(DISTINCT s.id) FROM narrative_citation ci JOIN narrative_section s ON s.id=ci.section_id "
              "AND s.last_version IS NULL JOIN narrative_chapter ch ON ch.id=s.chapter_id AND ch.inactive=0 "
              "WHERE ci.last_version IS NULL AND ci.verse_id IN (SELECT value FROM json_each(?)) GROUP BY 1",
    "lines": "SELECT x.verse_id, count(*) FROM reading_ref x JOIN reading_file f ON f.id=x.file_id AND f.removed=0 "
             "WHERE x.deleted=0 AND x.verse_id IN (SELECT value FROM json_each(?)) GROUP BY 1"}.items()}
got = {"obs": {v: len(r["observations"]) for v, r in V.items() if r["observations"]},
       "hits": {v: len(r["strand_hits"]) for v, r in V.items() if r["strand_hits"]},
       "claims": {v: len(r["claims"]) for v, r in V.items() if r["claims"]},
       "blocks": {v: len(r["narrative"]) for v, r in V.items() if r["narrative"]},
       "lines": {v: len(r["file_lines"]) for v, r in V.items() if r["file_lines"]}}
case("C1", "M02 -OnlyStrong H3708A (22 verses): per verse, observations, strand hits, claims, citing blocks and file lines "
     "equal plain SQL", len(V) == 22 and all(got[k] == want[k] for k in want),
     {k: (sum(got[k].values()), sum(want[k].values())) for k in want}, s)
bad = [(r["reference"], fl["file"], fl["line"]) for r in V.values() for fl in r["file_lines"]
       if not fl["text"] or fl["as_written"] not in fl["text"]]
case("C2", "every extracted file line is the line that names the verse (holds the reference as written)", not bad,
     f"{sum(len(r['file_lines']) for r in V.values())} lines; odd {bad[:5]}")

gap_bad = []
for v, r in V.items():
    obs, faced = bool(r["observations"]), any(h["face"] for h in r["strand_hits"])
    exp = {"not read": not obs and not faced, "read in files only": bool(r["file_lines"]) and not obs,
           "hit unread": any(not h["face"] and not h["reason"] for h in r["strand_hits"]),
           "observed, no claim": obs and not any(c["status"] == "current" for c in r["claims"]),
           "claim not told": any(c["status"] == "current" and not c["told_in"] for c in r["claims"]),
           "open item": bool(r["open_items"])}
    for k, e in exp.items():
        if (k in r["gaps"]) != e:
            gap_bad.append((r["reference"], k))
case("C3", "the gaps follow their rules for every verse; the totals equal the per-verse gaps", not gap_bad and
     all(out["gaps"][k] == sum(1 for r in V.values() if k in r["gaps"]) for k in vc.GAPS), f"{out['gaps']}; off {gap_bad[:5]}")
e = next((r for r in out["verses"] if r["osis"] == "Eccl.7.9"), None)
case("C4", "Ecc 7:9: observation 12478 and the anger strand's faced hits are collated",
     e is not None and any(o["id"] == 12478 for o in e["observations"]) and any(h["strand"] == "anger" and h["face"]
                                                                              for h in e["strand_hits"]),
     e and {"obs": [o["id"] for o in e["observations"]], "hits": [(h["strand"], bool(h["face"])) for h in e["strand_hits"]]})

pv = q("SELECT value FROM escalation_thread_item WHERE kind='verse' AND status='open' AND value NOT LIKE '%-%' AND value NOT LIKE '%,%' LIMIT 1")[0][0]
out2, s = collate({"Verse": pv})
case("C5", f"-Verse \"{pv}\" (an open thread item's verse): the item is collated as an open item",
     out2["verses"] and any(o["kind"] == "verse" for o in out2["verses"][0]["open_items"]) and "open item" in out2["verses"][0]["gaps"],
     out2["verses"][0]["open_items"][:3] if out2["verses"] else out2["scope"], s)
vh = q("SELECT DISTINCT v.reference FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id JOIN cluster_strong cs ON cs.strong=vl.strong "
       "AND cs.deleted=0 AND cs.cluster_code LIKE 'M%' WHERE vl.deleted=0 AND vl.strong='G6094' LIMIT 1")
if vh:
    out3, s = collate({"Verse": vh[0][0]})
    case("C6", f"-Verse \"{vh[0][0]}\" (holds G6094, an M-cluster Greek word with no Mounce entry, #2205): 'meaning missing'",
         "meaning missing" in out3["verses"][0]["gaps"], out3["verses"][0]["gaps"], s)
else:
    case("C6", "a verse holding G6094 in an M cluster", False, "none found")
lex_missing = [w["strong"] for r in V.values() for w in r["words"] if w["strong"] not in out["lexicon"]]
case("C7", "the lexicon has an entry for every inner-being word in the scope", not lex_missing, lex_missing[:5])

try:
    collate({"Thread": "OT-108"})
    case("C8", "-Thread OT-108: refused by the scope guard", False, "not refused")
except vs.ScopeError as ex:
    case("C8", "-Thread OT-108: refused by the scope guard", "too wide" in str(ex), str(ex)[:150])
c2 = sqlite3.connect(DB)
c2.execute("UPDATE cfg_setting SET value='0' WHERE key='verse_collate.max_seconds'")
c2.commit()
try:
    collate({"Cluster": "M02"})
    case("C9", "collate time guard (max_seconds 0 on the copy): refused", False, "not refused")
except vc.CollateError as ex:
    case("C9", "collate time guard (max_seconds 0 on the copy): refused", "time limit" in str(ex), str(ex)[:150])
c2.execute("UPDATE cfg_setting SET value='120' WHERE key='verse_collate.max_seconds'")
c2.commit()
c2.close()

repo = S / "repo"
f0 = q("SELECT f.path FROM reading_ref x JOIN reading_file f ON f.id=x.file_id WHERE x.deleted=0 AND f.removed=0 AND "
       "x.verse_id IN (SELECT value FROM json_each(?)) LIMIT 1", J)[0][0]
(repo / f0).parent.mkdir(parents=True)
shutil.copy2(ROOT / f0, repo / f0)
(repo / f0).write_text((repo / f0).read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
out4, s = collate({"Cluster": "M02", "OnlyStrong": "H3708A"}, root=repo)
case("C10", "a cluster file changed since it was indexed is named", f0 in out4["files_changed_since_indexed"],
     out4["files_changed_since_indexed"][:3])

o = hc.collate(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-VC", word="", word_id=None,
                   params={"Label": "t-anger", "Cluster": "M02", "OnlyStrong": "H3708A"}, step_id="verse_collate.collate"))
md = sorted((S / "out").glob("t-anger-*.md"))
js = sorted((S / "out").glob("t-anger-*.json"))
dj = json.loads(js[0].read_text(encoding="utf-8")) if js else {}
case("C11", "through the handler: the .json and .md written; the .md gap table equals the JSON",
     o.condition == "ok" and md and js and all(f"| {k} | {v} |" in md[0].read_text(encoding="utf-8") for k, v in dj["gaps"].items()),
     o.message[:200])
t0 = time.time()
out5, s5 = collate({"Cluster": "M25"})
case("C12", "speed: M25 Life and death (2,027 verses) within the guard", s5 < 120, f"{out5['counts']}", s5)
case("C13", "read-only: no row written by collating", conn.total_changes == changes, f"{changes} -> {conn.total_changes}")

lines = ["| # | case | result | evidence | s |", "|---|---|---|---|---|"] + [f"| {a} | {b} | {r} | {e} | {t} |" for a, b, r, e, t in results]
(S / "results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
print(f"\n{sum(r[2] == 'PASS' for r in results)}/{len(results)} PASS")
