"""temp_2236_open_item_test_run.py -- test plan for escalation #2236, registering open items
(outputs/escalation/2236-open-item-design-v2-20261023.md). Run on a copy of iba.db made with lib/dbsnapshot.copy_db
with the migration applied to the copy. Expected values by plain SQL on the copy.

Usage: python iba/app/tools/temp_2236_open_item_test_run.py <scratch dir>
"""
import json
import os
import pathlib
import shutil
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import escalation as esc  # noqa: E402
from iba.app.lib import threadaudit  # noqa: E402
from iba.app.lib import versecollate as vc  # noqa: E402
from iba.app.lib import versescope as vs  # noqa: E402
from iba.app.handlers import openitem as ho  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2236"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
env = {**os.environ, "PYTHONPATH": str(ROOT)}
mig = ROOT / "iba/app/migration/open_item_2236_v1_20261023.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
mo = [(lambda r: (r.stdout or r.stderr).strip())(subprocess.run([sys.executable, str(mig), "--db", str(DB)],
                                                                 capture_output=True, text=True, env=env)) for _ in range(2)]
c = sqlite3.connect(DB)
c.execute("UPDATE cfg_setting SET value=? WHERE key='open_item.output_dir'", (json.dumps(str(S / "out")),))
c.commit()
c.close()
cfg = Cfg(DB)
conn = cfg.conn
db = Db(cfg, DB)
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:400]))
    print(f"{cid} {'PASS' if passed else 'FAIL'}", flush=True)


def q(sql, *a):
    return conn.execute(sql, a).fetchall()


def run(step, **params):
    fn = getattr(ho, step)
    return fn(Ctx(db=db, cfg=cfg, step=None, run_id=f"RUN-TEST-{step}", word="", word_id=None, params=params,
                  step_id=f"open_item.{step}"))


case("O0", "migration applied (or already), then skipped", ("applied" in mo[0] or "already" in mo[0]) and "already" in mo[1], mo)

# a source x target pair from real data: H0639G (anger) against the M58 term it shares the fewest verses with
pair = q("SELECT b.strong, count(DISTINCT a.verse_id) n FROM verse_lexical a JOIN verse_lexical b ON b.verse_id=a.verse_id "
         "AND b.deleted=0 JOIN cluster_strong cs ON cs.strong=b.strong AND cs.cluster_code='M58' AND cs.deleted=0 "
         "WHERE a.deleted=0 AND a.strong='H0639G' GROUP BY b.strong ORDER BY n DESC LIMIT 1")[0]
term, n = pair[0], pair[1]
base = dict(Thread="OT-103", Origin="2172", Anchor="strong:H0639G", Source="H0639G", TargetCluster="M58",
            TargetTerms=term, ReadFor=f"how the anger of H0639G meets {term} of the wicked in these verses",
            Why="the anger strand found these shared verses and did not read the wicked side",
            ComesBackWhen="when M58 Wickedness is read as a strand")
before_items = q("SELECT count(*) FROM escalation_thread_item WHERE escalation_id=(SELECT id FROM escalation WHERE alias='OT-103')")[0][0]
o = run("add", **base)
it = q("SELECT * FROM escalation_thread_item WHERE kind='scope' AND target_terms=? ORDER BY id DESC LIMIT 1", term)
vrows = q("SELECT count(*) FROM escalation_thread_item_verse WHERE item_id=? AND deleted=0", it[0]["id"]) if it else [[0]]
hist = q("SELECT comment FROM escalation WHERE alias='OT-103'")[0][0] or ""
case("O1", f"Add OT-103 H0639G x {term} (M58): a worded item, its {n} verses kept, thread history written",
     o.condition == "ok" and it and it[0]["target_verses"] == n == vrows[0][0] and it[0]["worded_at"]
     and it[0]["origin_escalation_id"] == 2172 and "added" in hist[-400:], f"{o.message[:160]}; verses {vrows[0][0]}")

refusals = {
    "O2a no read-for": {**base, "ReadFor": "x"},
    "O2b origin not a task or issue": {**base, "Origin": str(q("SELECT id FROM escalation WHERE alias='OT-103'")[0][0])},
    "O2c anchor kind unknown": {**base, "Anchor": "file:abc"},
    "O2d target term not in the cluster": {**base, "TargetTerms": "H0639G"},
    "O2e verse with a cluster target but no source": {**{k: v for k, v in base.items() if k != "Source"}, "Verse": "Psa 10:2"},
    "O2f no verse in common": {**base, "Source": "G0002", "TargetTerms": term},
    "O2g over 200 verses": (lambda w: {**base, "Source": "H3068G", "TargetCluster": w[0], "TargetTerms": w[1]})(
        q("SELECT cs.cluster_code, b.strong, count(DISTINCT a.verse_id) n FROM verse_lexical a JOIN verse_lexical b ON "
          "b.verse_id=a.verse_id AND b.deleted=0 JOIN cluster_strong cs ON cs.strong=b.strong AND cs.deleted=0 AND "
          "cs.cluster_code LIKE 'M%' WHERE a.deleted=0 AND a.strong='H3068G' GROUP BY 1, 2 HAVING n > 200 LIMIT 1")[0]),
    "O3 duplicate (same target, same read-for)": base,
}
for cid, params in refusals.items():
    before = conn.total_changes
    o = run("add", **params)
    case(cid.split(" ")[0], f"Add refused: {cid.split(' ', 1)[1]}; nothing written", o.condition == "refused"
         and conn.total_changes == before, o.message[:200])

legacy = ("SELECT i.*, e.alias FROM escalation_thread_item i JOIN escalation e ON e.id=i.escalation_id WHERE e.type='thread' "
          "AND e.state IN ('on-hold','in-progress') AND i.kind='cluster' AND i.status='open' ORDER BY e.id, i.item_no")
leg = q(legacy)[0]                 # a legacy (not yet worded) cluster item on any open thread
ref = f"{leg['alias']}.{leg['item_no']}"
o = run("reword", Item=ref, **{**{k: v for k, v in base.items() if k != "Thread"},
                                "ReadFor": base["ReadFor"] + " (reworded)"})
now = q("SELECT * FROM escalation_thread_item WHERE id=?", leg["id"])[0]
note = q("SELECT text FROM escalation_thread_item_response WHERE item_id=? ORDER BY id DESC LIMIT 1", leg["id"])
case("O4", f"Reword {ref} (cluster:{leg['value']}, legacy): now worded, scoped; the old wording in its history", o.condition == "ok"
     and now["kind"] == "scope" and now["status"] == "open" and now["target_verses"] == n and note
     and f"was: cluster:{leg['value']}" in note[0][0], f"{o.message[:150]}; history: {note[0][0][:120] if note else None}")
o2 = run("reword", Item=ref, **{**{k: v for k, v in base.items() if k not in ("Thread", "Source", "TargetCluster", "TargetTerms")},
                                 "Verse": "Pro 29:22", "ReadFor": "how the angry man stirs up strife here"})
dead = q("SELECT count(*) FROM escalation_thread_item_verse WHERE item_id=? AND deleted=1", leg["id"])[0][0]
live = q("SELECT count(*) FROM escalation_thread_item_verse WHERE item_id=? AND deleted=0", leg["id"])[0][0]
case("O5", "Reword again to a verse target: the earlier target verses kept as deleted, the new one live",
     o2.condition == "ok" and dead == n and live == 1, f"{o2.message[:120]}; deleted {dead}, live {live}")

leg2 = q(legacy)[0]                # the next legacy cluster item (the first was reworded above)
parts = [{"origin": 2172, "anchor": "verse:Ecc 7:9", "verse": "Ecc 7:9", "read_for": "the bosom where anger lodges, for the target side",
          "why": "split test: one purpose of the wide item", "comes_back_when": "when the cluster is read"},
         {"origin": 2172, "anchor": "verse:Pro 14:29", "verse": "Pro 14:29", "read_for": "slow to anger and great understanding",
          "why": "split test: the other purpose of the wide item", "comes_back_when": "when the cluster is read"}]
pf = S / "parts.json"
pf.write_text(json.dumps(parts), encoding="utf-8")
o = run("split", Item=f"{leg2['alias']}.{leg2['item_no']}", File=str(pf))
old = q("SELECT status FROM escalation_thread_item WHERE id=?", leg2["id"])[0][0]
st = q("SELECT state FROM escalation WHERE alias='OT-103'")[0][0]
case("O6", f"Split {leg2['alias']}.{leg2['item_no']} into two: the old one superseded naming them; the thread still open",
     o.condition == "ok" and old == "superseded" and st in ("on-hold", "in-progress"), f"{o.message[:160]}; old {old}; thread {st}")

tv = q("SELECT v.reference FROM escalation_thread_item_verse x JOIN verse v ON v.id=x.verse_id WHERE x.item_id=? AND x.deleted=0 LIMIT 1", it[0]["id"])[0][0]
other = q("SELECT v.reference FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id JOIN cluster_strong cs ON cs.strong=vl.strong "
          "AND cs.cluster_code='M58' AND cs.deleted=0 WHERE vl.deleted=0 AND vl.verse_id NOT IN (SELECT verse_id FROM "
          "escalation_thread_item_verse WHERE item_id=?) LIMIT 1", it[0]["id"])[0][0]
iid = it[0]["id"]
m_in = [x for x in esc.match_open_items(db, verses=[tv]) if x[1]["id"] == iid]
m_out = [x for x in esc.match_open_items(db, verses=[other]) if x[1]["id"] == iid]
m_home = [x for x in esc.match_open_items(db, clusters=["M58"]) if x[1]["id"] == iid]
m_nohome = [x for x in esc.match_open_items(db, clusters=["M58"], home=False) if x[1]["id"] == iid]
case("O7", "Matching: a worded item matches its target verses only; its home cluster only when home is on",
     m_in and not m_out and m_home and not m_nohome, f"in {len(m_in)}, other verse {len(m_out)}, home {len(m_home)}, no home {len(m_nohome)}")
out = vc.collate(cfg, vs.normalise_request({"Verse": f"{tv}; {other}"}), ROOT)
by = {r["reference"]: [o["item"] for o in r["open_items"]] for r in out["verses"]}
label = f"OT-103.{it[0]['item_no']}"
case("O8", "Collation: the worded item shows on its target verse, not on another M58 verse",
     label in by.get(tv, []) and label not in by.get(other, []), {k: [x for x in v if x.startswith('OT-103')] for k, v in by.items()})
o = run("due", Cluster="M58")
case("O9", "Due -Cluster M58 lists the worded M58 items", o.condition == "ok" and label in o.message, o.message[:200])
o = run("review")
rp = pathlib.Path(o.counts["path"])
worded = q("SELECT count(*) FROM escalation_thread_item i JOIN escalation e ON e.id=i.escalation_id WHERE i.status='open' "
           "AND i.worded_at IS NOT NULL AND e.type='thread' AND e.state IN ('on-hold','in-progress')")[0][0]
case("O10", "Review: the report written; its worded total equals the tables", o.condition == "ok" and f"**{worded}**" in rp.read_text(encoding="utf-8"),
     f"{rp.name}; worded {worded}")
bad = [{**{k.lower(): v for k, v in base.items()}, "read_for": "another purpose entirely for the batch test",
        "target_terms": term}, {**{k.lower(): v for k, v in base.items()}, "why": "x"}]
bf = S / "batch.json"
bf.write_text(json.dumps([{"thread": "OT-103", "origin": 2172, "anchor": "strong:H0639G", "source": "H0639G",
                           "target_cluster": "M58", "target_terms": term, "read_for": "another purpose entirely for the batch test",
                           "why": "batch test: the first item is fine", "comes_back_when": "when M58 Wickedness is read"},
                          {"thread": "OT-103", "origin": 2172, "anchor": "strong:H0639G", "verse": "Ecc 7:9", "read_for": "x",
                           "why": "batch test: the second item has no purpose", "comes_back_when": "never"}]), encoding="utf-8")
before = q("SELECT count(*) FROM escalation_thread_item")[0][0]
o = run("add", File=str(bf))
after = q("SELECT count(*) FROM escalation_thread_item")[0][0]
case("O11", "A -File batch with one bad spec: refused, nothing written (one unit)", o.condition == "refused" and before == after,
     o.message[:150])
F = threadaudit.audit(cfg, db)
scope_flags = [f for f in F if "scope:" in str(f) or "OT-103." + str(it[0]["item_no"]) in str(f)]
case("O12", "Thread audit raises nothing on the worded items", not [f for f in scope_flags if "T-a" in str(f) or "T-b" in str(f)],
     scope_flags[:3])
from iba.app.handlers import configmaint as cm  # noqa: E402
from iba.app.lib import cfgquality  # noqa: E402
for (k, v) in sqlite3.connect(DB).execute("SELECT key, value FROM cfg_setting WHERE key LIKE 'database.%.path' AND inactive=0").fetchall():
    conn.execute("UPDATE cfg_setting SET value=? WHERE key=?", (json.dumps(str(ROOT / json.loads(v))), k))
errs = cm._validate_live(conn) + cfgquality.find_rule_scope_gaps(conn, ROOT / "iba" / "app") + [
    e for e in cfgquality.find_unregistered_project_scripts(conn, ROOT) if "iba/app/migration/" not in e]
case("O13", "configmaint.validate hard checks on the copy (a migration not yet archived set aside)", not errs, errs or "none")

vt = q("SELECT v.reference FROM escalation_thread_item_verse x JOIN verse v ON v.id=x.verse_id WHERE x.item_id=? AND x.deleted=0", iid)
o = run("add", **{**base, "Verse": "; ".join(r[0] for r in vt), "ReadFor": "the purpose's own verses read for both terms (#2236 form)"})
new = q("SELECT * FROM escalation_thread_item WHERE kind='scope' AND read_for LIKE 'the purpose''s own verses%'")
case("O14", "Add with -Verse and its source and target terms: the given verses kept, the terms recorded",
     o.condition == "ok" and new and new[0]["target_verses"] == len(vt) and new[0]["target_cluster"] == "M58"
     and new[0]["source_terms"] == "H0639G", o.message[:160])

L = ["| # | case | result | evidence |", "|---|---|---|---|"] + [f"| {a} | {b} | {r} | {e} |" for a, b, r, e in results]
(S / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
print(f"\n{sum(r[2] == 'PASS' for r in results)}/{len(results)} PASS")
