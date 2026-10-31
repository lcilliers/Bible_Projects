"""temp_2339_concept_tables_test_run.py -- escalation #2339 test plan for iba/app/migration/concept_tables_2339_v1_20261031.py,
on COPIES of the live iba.db (never the live one). Usage: python iba/app/tools/temp_2339_concept_tables_test_run.py <scratch dir>.
Prints PASS/FAIL per case."""
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

S = pathlib.Path(sys.argv[1]) / "t2339run"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
MIG = ROOT / "iba/app/migration/concept_tables_2339_v1_20261031.py"
MIG = MIG if MIG.exists() else ROOT / "iba/app/migration/archive" / MIG.name
SPEC = ROOT / "iba/docs/concept-mapping-spec-v1-20261031.json"
spec = json.load(open(SPEC, encoding="utf-8"))
env = {**os.environ, "PYTHONPATH": str(ROOT), "PYTHONUTF8": "1"}
TABLES = ("concept_domain", "concept", "concept_subgroup")
res = []


def case(cid, desc, ok, ev=""):
    ok = bool(ok)
    res.append(ok)
    print(f"{cid} {'PASS' if ok else 'FAIL'} {desc}" + ("" if ok else f"  -- {str(ev)[:900]}"), flush=True)


def run(db, *a, spec_path=None):
    args = [sys.executable, str(MIG), "--db", str(db)] + (["--spec", str(spec_path)] if spec_path else []) + list(a)
    r = subprocess.run(args, capture_output=True, text=True, env=env)
    return r.returncode, (r.stdout + r.stderr).strip()


def con(db):
    c = sqlite3.connect(db)
    c.execute("PRAGMA foreign_keys=ON")
    return c


def tables(db):
    c = con(db)
    t = {r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    c.close()
    return t


def cfg_rows(db):
    c = con(db)
    n = c.execute(f"SELECT count(*) FROM cfg_table WHERE name IN {TABLES}").fetchone()[0]
    c.close()
    return n


# ---- DB1: the real spec ----
DB1 = copy_db(S / "iba1.db", ROOT / "iba/app/db/iba.db")
rc, out = run(DB1, "--dry-run")
case("T1", "dry run reports the plan and writes nothing",
     rc == 0 and out.startswith("DRY RUN") and "14 domains, 101 concepts, 411 concept_subgroup" in out
     and not (set(TABLES) & tables(DB1)) and cfg_rows(DB1) == 0, out[:300])
rc, out = run(DB1)
case("T2", "apply builds the tables and loads 14, 101, 411", rc == 0 and "loaded 14 domains, 101 concepts, 411" in out, out)
c = con(DB1)
cnt = lambda t: c.execute(f"SELECT count(*) FROM {t} WHERE deleted=0").fetchone()[0]  # noqa: E731
case("T3", "live row counts are 14, 101, 411", (cnt("concept_domain"), cnt("concept"), cnt("concept_subgroup")) == (14, 101, 411),
     (cnt("concept_domain"), cnt("concept"), cnt("concept_subgroup")))
before = (cnt("concept_domain"), cnt("concept"), cnt("concept_subgroup"), c.execute("SELECT count(*) FROM cfg_change_detail").fetchone()[0])
rc2, out2 = run(DB1)
c.close()
c = con(DB1)
after = (cnt("concept_domain"), cnt("concept"), cnt("concept_subgroup"), c.execute("SELECT count(*) FROM cfg_change_detail").fetchone()[0])
case("T4", "a second run is refused as already applied and changes nothing", rc2 == 0 and out2.startswith("already applied") and before == after,
     (out2, before, after))
bad = c.execute("""SELECT count(*) FROM cluster_subgroup g WHERE g.kind IN ('group','qualifier') AND g.delete_flagged=0
                   AND (SELECT count(*) FROM concept_subgroup s JOIN concept k ON k.id=s.concept_id AND k.deleted=0
                        WHERE s.cluster_subgroup_id=g.id AND s.deleted=0)<>1""").fetchone()[0]
stray = c.execute("""SELECT count(*) FROM concept_subgroup s WHERE s.deleted=0 AND s.cluster_subgroup_id NOT IN
                     (SELECT id FROM cluster_subgroup WHERE kind IN ('group','qualifier') AND delete_flagged=0)""").fetchone()[0]
case("T5", "every live group and qualifier subgroup is in exactly one live concept, and no other subgroup is", bad == 0 and stray == 0, (bad, stray))
mism = []
for d in spec["domains"]:
    dr = c.execute("SELECT id, ordinal FROM concept_domain WHERE name=?", (d["domain"],)).fetchone()
    if not dr or dr[1] != d["ordinal"]:
        mism.append(("domain", d["domain"]))
        continue
    for k in d["concepts"]:
        kr = c.execute("SELECT id, ordinal FROM concept WHERE domain_id=? AND name=?", (dr[0], k["concept"])).fetchone()
        if not kr or kr[1] != k["ordinal"]:
            mism.append(("concept", k["concept"]))
            continue
        ids = {r[0] for r in c.execute("SELECT cluster_subgroup_id FROM concept_subgroup WHERE concept_id=?", (kr[0],))}
        if ids != set(k["subgroup_ids"]):
            mism.append(("subgroups", k["concept"]))
case("T6", "every domain, concept, ordinal and subgroup set equals the spec", not mism, mism[:5])


def raises(sql, *a):
    try:
        c.execute(sql, a)
        c.rollback()
        return False
    except sqlite3.IntegrityError:
        c.rollback()
        return True


sid = c.execute("SELECT cluster_subgroup_id, concept_id FROM concept_subgroup LIMIT 1").fetchone()
other = c.execute("SELECT id FROM concept WHERE id<>?", (sid[1],)).fetchone()[0]
case("T7", "a second live concept for a subgroup is rejected",
     raises("INSERT INTO concept_subgroup (concept_id, cluster_subgroup_id) VALUES (?,?)", other, sid[0]))
c.execute("UPDATE concept_subgroup SET deleted=1 WHERE cluster_subgroup_id=?", (sid[0],))
ok_after_delete = not raises("INSERT INTO concept_subgroup (concept_id, cluster_subgroup_id) VALUES (?,?)", other, sid[0])
c.rollback()
case("T8", "after the old membership is soft-deleted, the subgroup can join another concept", ok_after_delete)
case("T9", "a concept_subgroup naming a missing concept or subgroup is rejected (foreign keys)",
     raises("INSERT INTO concept_subgroup (concept_id, cluster_subgroup_id) VALUES (999999, ?)", sid[0])
     and raises("INSERT INTO concept_subgroup (concept_id, cluster_subgroup_id) VALUES (?, 999999)", other))
dn = c.execute("SELECT name, id FROM concept_domain LIMIT 1").fetchone()
cn = c.execute("SELECT name, domain_id FROM concept LIMIT 1").fetchone()
case("T10", "a duplicate live domain name, or concept name in a domain, is rejected",
     raises("INSERT INTO concept_domain (name, ordinal) VALUES (?, 99)", dn[0])
     and raises("INSERT INTO concept (domain_id, name, ordinal) VALUES (?, ?, 99)", cn[1], cn[0]))
case("T11", "the narrative links are NULL on every row",
     c.execute("SELECT count(*) FROM concept_domain WHERE narrative_chapter_id IS NOT NULL").fetchone()[0] == 0
     and c.execute("SELECT count(*) FROM concept WHERE narrative_section_id IS NOT NULL").fetchone()[0] == 0)
drift = []
for t in TABLES:
    live_cols = {r[1] for r in c.execute(f"PRAGMA table_info({t})")}
    cfg_cols = {r[0] for r in c.execute("SELECT name FROM cfg_column WHERE database='iba' AND table_name=? AND inactive=0", (t,))}
    if live_cols != cfg_cols:
        drift.append((t, live_cols ^ cfg_cols))
case("T12", "cfg_column holds exactly the live columns of each table", not drift, drift)
case("T13", "cfg_table (3, category data), cfg_write_grant (writer migration), cfg_unique, cfg_utility and the change log are present",
     c.execute(f"SELECT count(*) FROM cfg_table WHERE name IN {TABLES} AND category='data' AND inactive=0").fetchone()[0] == 3
     and c.execute(f"SELECT count(*) FROM cfg_write_grant WHERE writer='migration' AND table_name IN {TABLES} AND inactive=0").fetchone()[0] == 3
     and c.execute(f"SELECT count(*) FROM cfg_unique WHERE table_name IN {TABLES}").fetchone()[0] == 4
     and c.execute("SELECT inactive FROM cfg_utility WHERE module='concept_tables_2339_v1_20261031'").fetchone() == (1,)
     and c.execute("SELECT count(*) FROM cfg_change_detail WHERE run_id='DEVMODE-2339-CONCEPT-TABLES-20261031'").fetchone()[0] > 30)
c.close()

# ---- DB2: refusals (synthetic bad input) and rollback ----
DB2 = copy_db(S / "iba2.db", ROOT / "iba/app/db/iba.db")


def variant(name, fn):
    s = json.loads(json.dumps(spec))
    fn(s)
    p = S / f"{name}.json"
    p.write_text(json.dumps(s), encoding="utf-8")
    return p


def not_live(s):
    s["domains"][0]["concepts"][0]["subgroup_ids"][0] = 9999999


def missing(s):
    s["domains"][0]["concepts"][0]["subgroup_ids"].pop()
    s["domains"][0]["concepts"][0]["subgroup_codes"].pop()


def twice(s):
    s["domains"][0]["concepts"][1]["subgroup_ids"].append(s["domains"][0]["concepts"][0]["subgroup_ids"][0])
    s["domains"][0]["concepts"][1]["subgroup_codes"].append(s["domains"][0]["concepts"][0]["subgroup_codes"][0])


def wrong_code(s):
    s["domains"][0]["concepts"][0]["subgroup_codes"][0] = "NOT_A_CODE"


for cid, name, fn, needle in (("T14", "not_live", not_live, "not a live group or qualifier"),
                              ("T15", "missing", missing, "is in no concept"),
                              ("T16", "twice", twice, "is in two concepts"),
                              ("T17", "wrong_code", wrong_code, "spec code")):
    rc, out = run(DB2, spec_path=variant(name, fn))
    case(cid, f"synthetic bad spec ({name}) is refused with a reason and nothing is written",
         rc == 2 and "REFUSED" in out and needle in out and not (set(TABLES) & tables(DB2)) and cfg_rows(DB2) == 0, out[:300])
c2 = con(DB2)
c2.execute("CREATE TABLE concept (x INTEGER)")
c2.commit()
c2.close()
rc, out = run(DB2)
t2 = tables(DB2)
case("T18", "a failure after the cfg writes rolls everything back (table concept pre-made with the wrong shape)",
     rc != 0 and "concept_domain" not in t2 and "concept_subgroup" not in t2 and cfg_rows(DB2) == 0, (rc, out[-300:], t2 & set(TABLES)))

print(f"{sum(res)} of {len(res)} PASS")
sys.exit(0 if all(res) else 1)
